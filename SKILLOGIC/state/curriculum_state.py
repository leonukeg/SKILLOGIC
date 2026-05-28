import reflex as rx
from typing import Any, List, Dict
from SKILLOGIC.data.curriculum import load_curriculum, save_curriculum
from SKILLOGIC.lib.supabase_client import fetch_user_profile, update_user_progress
from pydantic import BaseModel
from SKILLOGIC.state.auth_state import AuthState
from SKILLOGIC.state.progress_state import ProgressState

class LessonItem(BaseModel):
    id: str
    title: str

class ModuleItem(BaseModel):
    icon_tag: str
    name_es: str
    name_en: str
    progress: str | int
    status: str
    lessons: list[LessonItem]

class CurriculumState(rx.State):
    """Holds curriculum data loaded from JSON to make it reactive."""
    
    modules: list[ModuleItem] = []
    projects: list[dict[str, Any]] = []
    todays_plan: list[dict[str, Any]] = []
    daily_challenge: dict = {}
    
    # Form variables for new Module
    new_module_name_es: str = ""
    new_module_name_en: str = ""
    new_module_icon: str = "folder"
    
    # Form variables for new Project
    new_project_title_es: str = ""
    new_project_title_en: str = ""
    new_project_desc_es: str = ""
    new_project_desc_en: str = ""
    new_project_level: str = "basic"
    
    # Form variables for new Lesson
    new_lesson_title_es: str = ""

    def set_new_module_name_es(self, val: str): self.new_module_name_es = val
    def set_new_module_icon(self, val: str): self.new_module_icon = val
    def set_new_project_title_es(self, val: str): self.new_project_title_es = val
    def set_new_project_desc_es(self, val: str): self.new_project_desc_es = val
    def set_new_project_level(self, val: str): self.new_project_level = val
    def set_new_lesson_title_es(self, val: str): self.new_lesson_title_es = val

    async def load_data(self):
        """Load data from JSON into the state variables, merging with Supabase if logged in."""
        data = load_curriculum()
        raw_modules = data.get("MODULES", [])
        self.modules = [ModuleItem(**m) for m in raw_modules]
        
        self.projects = data.get("PROJECTS", [])
        self.todays_plan = data.get("TODAYS_PLAN", [])
        self.daily_challenge = data.get("DAILY_CHALLENGE", {})
        
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return rx.redirect("/login")
            
        # Si el usuario está logueado, sobreescribimos su progreso
        profile = fetch_user_profile(auth.user_id)
        if profile and "progress" in profile:
            user_prog = profile["progress"]
            # Mezclar progreso (simplificado para MVP: reemplazamos TODAYS_PLAN u otros)
            if "todays_plan" in user_prog:
                self.todays_plan = user_prog["todays_plan"]
                
            # Actualizar el progreso y estado de los módulos
            user_lessons = user_prog.get("lessons", {})
            previous_completed = True
            
            for mod in self.modules:
                total_lessons = len(mod.lessons)
                
                if total_lessons == 0:
                    if previous_completed:
                        mod.status = "active"
                    continue
                    
                completed_count = 0.0
                for lesson in mod.lessons:
                    lesson_data = user_lessons.get(lesson.id)
                    if lesson_data:
                        if lesson_data.get("status") == "completed":
                            completed_count += 1.0
                        elif lesson_data.get("status") == "in_progress":
                            # Calculamos progreso parcial basado en la fase actual (asumiendo 7 fases por lección)
                            fase_actual = lesson_data.get("phase", 0)
                            completed_count += min(fase_actual / 7.0, 0.99)
                        
                progress_percent = int((completed_count / total_lessons) * 100)
                mod.progress = str(progress_percent)
                
                # Consider complete only if all lessons are fully 1.0
                if int(completed_count) == total_lessons:
                    mod.status = "completed"
                    previous_completed = True
                elif completed_count > 0:
                    mod.status = "active"
                    previous_completed = False
                elif previous_completed:
                    mod.status = "active"
                    previous_completed = False
                else:
                    mod.status = "locked"
                    previous_completed = False
                    
            # Forzar actualización en Reflex (ya que modificamos propiedades internas)
            self.modules = self.modules

    async def save_data(self):
        """Save the current state back to JSON and to Supabase if logged in."""
        # Convert rx.Base objects to dict for JSON serialization
        modules_list = [m.dict() if hasattr(m, "dict") else dict(m) for m in self.modules]
        
        # 1. Guardar siempre en JSON para persistencia local de la app
        save_curriculum({
            "MODULES": modules_list,
            "PROJECTS": self.projects,
            "TODAYS_PLAN": self.todays_plan,
            "DAILY_CHALLENGE": self.daily_challenge
        })
        
        # 2. Si está logueado, guardar su progreso en su perfil de Supabase
        auth = await self.get_state(AuthState)
        if auth.is_authenticated:
            user_prog = {
                "todays_plan": self.todays_plan,
                # En el futuro se puede añadir progreso por lección específica
            }
            update_user_progress(auth.user_id, user_prog)
        
    async def set_plan_title(self, index: int, value: str):
        self.todays_plan[index]["title_es"] = value
        self.todays_plan = self.todays_plan
        return await self.save_data()
        
    async def toggle_plan_completion(self, index: int, val: bool):
        # Asegurar que el estado "completed" se maneje como string ("True"/"False")
        # ya que list[dict[str, str]] espera strings
        self.todays_plan[index]["completed"] = "True" if val else "False"
        self.todays_plan = self.todays_plan
        
        if val:
            progress = await self.get_state(ProgressState)
            await progress.complete_lesson()
            
        return await self.save_data()
        
    async def toggle_plan_by_title(self, title_en: str, val: bool):
        for i, item in enumerate(self.todays_plan):
            if item.get("title_en") == title_en:
                self.todays_plan[i]["completed"] = "True" if val else "False"
                self.todays_plan = self.todays_plan
                
                if val:
                    progress = await self.get_state(ProgressState)
                    await progress.complete_lesson()
                break
                
        return await self.save_data()
        
    async def set_challenge_title(self, value: str):
        self.daily_challenge["title_es"] = value
        self.daily_challenge = self.daily_challenge
        return await self.save_data()
        
    async def set_challenge_desc(self, value: str):
        self.daily_challenge["desc_es"] = value
        self.daily_challenge = self.daily_challenge
        return await self.save_data()

    async def add_module(self):
        if not self.new_module_name_es.strip():
            return
        self.modules.append(ModuleItem(
            icon_tag=self.new_module_icon,
            name_es=self.new_module_name_es,
            name_en=self.new_module_name_en or self.new_module_name_es,
            progress="0",
            status="locked",
            lessons=[]
        ))
        self.modules = self.modules
        self.new_module_name_es = ""
        self.new_module_name_en = ""
        self.new_module_icon = "folder"
        return await self.save_data()
        
    async def remove_module(self, index: int):
        if 0 <= index < len(self.modules):
            self.modules.pop(index)
            self.modules = self.modules
            return await self.save_data()

    async def add_lesson(self, module_index: int):
        if not self.new_lesson_title_es.strip():
            return
        if 0 <= module_index < len(self.modules):
            mod = self.modules[module_index]
            lessons = getattr(mod, "lessons", [])
            new_id = f"{module_index + 1}.{len(lessons) + 1}"
            lessons.append(LessonItem(
                id=new_id,
                title=self.new_lesson_title_es
            ))
            mod.lessons = lessons
            self.modules = self.modules
            self.new_lesson_title_es = ""
            return await self.save_data()
            
    async def remove_lesson(self, module_index: int, lesson_index: int):
        if 0 <= module_index < len(self.modules):
            mod = self.modules[module_index]
            lessons = getattr(mod, "lessons", [])
            if 0 <= lesson_index < len(lessons):
                lessons.pop(lesson_index)
                mod.lessons = lessons
                self.modules = self.modules
                return await self.save_data()

    async def add_project(self):
        if not self.new_project_title_es.strip():
            return
        self.projects.append({
            "title_es": self.new_project_title_es,
            "title_en": self.new_project_title_en or self.new_project_title_es,
            "desc_es": self.new_project_desc_es,
            "desc_en": self.new_project_desc_en or self.new_project_desc_es,
            "level": self.new_project_level,
        })
        self.projects = self.projects
        self.new_project_title_es = ""
        self.new_project_title_en = ""
        self.new_project_desc_es = ""
        self.new_project_desc_en = ""
        self.new_project_level = "basic"
        return await self.save_data()
        
    async def remove_project(self, index: int):
        if 0 <= index < len(self.projects):
            self.projects.pop(index)
            self.projects = self.projects
            return await self.save_data()
