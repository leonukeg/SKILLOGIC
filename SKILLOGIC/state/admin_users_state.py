import reflex as rx
from SKILLOGIC.lib.supabase_client import get_supabase, get_supabase_admin
from SKILLOGIC.state.auth_state import AuthState

class AdminUsersState(rx.State):
    """Maneja la lista de usuarios y operaciones de administrador para la vista de master."""
    
    users: list[dict] = []
    is_loading: bool = False
    
    # Modal state
    selected_user: dict = {}
    is_modal_open: bool = False
    
    # State for email editing
    editing_email: str = ""
    editing_name: str = ""
    profile_edit_success: bool = False
    profile_edit_error: str = ""
    is_saving_profile: bool = False
    
    reset_email_sent: bool = False
    reset_email_error: str = ""
    
    async def load_users(self):
        from SKILLOGIC.state.app_state import AppState
        app_state = await self.get_state(AppState)
        app_state.active_nav = "admin_users"
        
        auth = await self.get_state(AuthState)
        if getattr(auth, "role", "basic") != "master" and auth.user_email not in ["admin@skillogic.com", "chemaruan@gmail.com"]:
            return # No es master, no carga
            
        self.is_loading = True
        client = get_supabase()
        if client:
            try:
                # Usamos la anon key para obtener profiles (RLS debe permitir select)
                res = client.table("profiles").select("*").execute()
                
                # Transformamos la data para que sea facil de leer en UI
                formatted_users = []
                for p in res.data:
                    prog = p.get("progress", {})
                    # Extraer rol, por defecto basic
                    role = prog.get("role", "basic")
                    if p.get("email") in ["admin@skillogic.com", "chemaruan@gmail.com"]:
                        role = "master" # overrides de seguridad
                        
                    formatted_users.append({
                        "id": p["id"],
                        "name": p.get("full_name", p.get("email", "Sin nombre").split("@")[0]),
                        "email": p.get("email", "Sin email"),
                        "role": role,
                        "xp": p.get("xp", 0),
                        "streak": p.get("streak", 0),
                        "completed_lessons": len(prog.get("lessons", {})),
                    })
                
                self.users = formatted_users
            except Exception as e:
                print("Error loading users:", e)
                
        self.is_loading = False

    def open_user_modal(self, user: dict):
        self.selected_user = user
        self.is_modal_open = True
        self.reset_email_sent = False
        self.reset_email_error = ""
        
        # Reset profile editing state
        self.editing_email = user.get("email", "")
        self.editing_name = user.get("name", "")
        self.profile_edit_success = False
        self.profile_edit_error = ""
        self.is_saving_profile = False
        
    def close_user_modal(self):
        self.is_modal_open = False
        self.selected_user = {}

    def set_editing_email(self, val: str):
        self.editing_email = val
        self.profile_edit_success = False
        self.profile_edit_error = ""
        
    def set_editing_name(self, val: str):
        self.editing_name = val
        self.profile_edit_success = False
        self.profile_edit_error = ""

    def save_user_profile(self):
        if not self.selected_user: return
        user_id = self.selected_user["id"]
        
        if not self.editing_email or "@" not in self.editing_email:
            self.profile_edit_error = "Introduce un correo válido."
            return
            
        if not self.editing_name:
            self.profile_edit_error = "Introduce un nombre válido."
            return
            
        admin_client = get_supabase_admin()
        if not admin_client:
            self.profile_edit_error = "Llave de servicio no configurada."
            return
            
        self.is_saving_profile = True
        try:
            # 1. Update in Auth (requires SERVICE_ROLE_KEY)
            admin_client.auth.admin.update_user_by_id(
                user_id, 
                {"email": self.editing_email, "user_metadata": {"full_name": self.editing_name}}
            )
            
            # 2. Update in Public Profiles Table (requires SERVICE_ROLE_KEY to bypass RLS)
            admin_client.table("profiles").update({
                "email": self.editing_email,
                "full_name": self.editing_name
            }).eq("id", user_id).execute()
            
            # 3. Update local state
            for u in self.users:
                if u["id"] == user_id:
                    u["email"] = self.editing_email
                    u["name"] = self.editing_name
                    self.selected_user["email"] = self.editing_email
                    self.selected_user["name"] = self.editing_name
            
            self.users = self.users
            self.profile_edit_success = True
            self.profile_edit_error = ""
        except Exception as e:
            self.profile_edit_error = f"Error: {str(e)}"
            self.profile_edit_success = False
            
        self.is_saving_profile = False

    def send_reset_email(self):
        if not self.selected_user: return
        user_email = self.selected_user.get("email")
        if not user_email or user_email == "Sin email":
            self.reset_email_error = "El usuario no tiene un email válido."
            return
            
        client = get_supabase()
        if not client: return
        
        try:
            # We must pass the redirect_to URL where the user will change the password
            client.auth.reset_password_for_email(
                user_email,
                options={"redirect_to": "http://localhost:3000/update-password"}
            )
            self.reset_email_sent = True
            self.reset_email_error = ""
        except Exception as e:
            self.reset_email_error = f"Error: {str(e)}"
            self.reset_email_sent = False

    def toggle_selected_role(self):
        if not self.selected_user: return
        user_id = self.selected_user["id"]
        current_role = self.selected_user["role"]
        
        client = get_supabase()
        if not client: return
        
        new_role = "master" if current_role != "master" else "basic"
        
        # Hay que hacer fetch primero para no machacar el progreso
        res = client.table("profiles").select("progress").eq("id", user_id).execute()
        if res.data and len(res.data) > 0:
            prog = res.data[0].get("progress", {})
            prog["role"] = new_role
            client.table("profiles").update({"progress": prog}).eq("id", user_id).execute()
            
            # Actualizamos estado local
            for u in self.users:
                if u["id"] == user_id:
                    u["role"] = new_role
                    self.selected_user["role"] = new_role # update modal view
            self.users = self.users

    def reset_selected_progress(self):
        if not self.selected_user: return
        user_id = self.selected_user["id"]
        
        client = get_supabase()
        if not client: return
        
        res = client.table("profiles").select("progress").eq("id", user_id).execute()
        if res.data and len(res.data) > 0:
            prog = res.data[0].get("progress", {})
            prog["lessons"] = {} # Borra historial de lecciones
            
            client.table("profiles").update({
                "progress": prog,
                "xp": 0,
                "streak": 0
            }).eq("id", user_id).execute()
            
            # Actualizamos estado local
            for u in self.users:
                if u["id"] == user_id:
                    u["xp"] = 0
                    u["streak"] = 0
                    u["completed_lessons"] = 0
                    self.selected_user["xp"] = 0
                    self.selected_user["streak"] = 0
                    self.selected_user["completed_lessons"] = 0
            self.users = self.users
