import reflex as rx
import io
import contextlib
import builtins
import time
from typing import Optional, Dict

from SKILLOGIC.data.katas import get_kata_by_id
from SKILLOGIC.state.progress_state import ProgressState
from SKILLOGIC.state.auth_state import AuthState

class KataState(rx.State):
    """Maneja el estado y ejecución de un Kata individual."""
    
    @rx.var
    def current_kata_id(self) -> str:
        return self.kata_id
    user_code: str = ""
    terminal_output: str = ""
    is_success: bool = False
    is_loading: bool = False
    feedback_message: str = ""
    last_kata_id: str = ""
    
    @rx.var
    def next_kata_id(self) -> str:
        from SKILLOGIC.data.katas import KATAS_DB
        for i, k in enumerate(KATAS_DB):
            if k["id"] == self.current_kata_id:
                if i + 1 < len(KATAS_DB):
                    return KATAS_DB[i + 1]["id"]
                break
        return ""

    @rx.var
    def kata_data(self) -> dict:
        return get_kata_by_id(self.current_kata_id) or {}
        
    def set_user_code(self, val: str):
        self.user_code = val
        
    def on_load(self):
        # Reiniciar estado de la consola
        self.terminal_output = ""
        self.is_success = False
        self.feedback_message = ""
        self.is_loading = False
        
        # Cargar código inicial solo si entramos a un nuevo Kata
        if self.kata_id != self.last_kata_id:
            self.last_kata_id = self.kata_id
            kata = self.kata_data
            if kata:
                self.user_code = kata.get("initial_code", "")

    async def run_kata(self):
        """Ejecuta el código del usuario y las pruebas ocultas."""
        self.is_loading = True
        self.terminal_output = ""
        self.is_success = False
        self.feedback_message = ""
        yield
        
        kata = self.kata_data
        if not kata:
            self.terminal_output = "Error: Kata no encontrado."
            self.is_loading = False
            yield
            return
            
        full_code = self.user_code + "\n\n" + kata.get("test_code", "")
        
        f = io.StringIO()
        
        try:
            with contextlib.redirect_stdout(f):
                # Usar diccionario de globals con el código del usuario accesible para tests
                exec(full_code, {"USER_CODE": self.user_code})
            
            output = f.getvalue()
            self.terminal_output = output
            
            if "ALL_TESTS_PASSED" in output:
                self.is_success = True
                self.feedback_message = "¡Excelente! Todas las pruebas pasaron correctamente."
                
                # Otorgar XP y marcar como completado
                progress = await self.get_state(ProgressState)
                async for update in progress.mark_kata_completed(self.current_kata_id, kata.get("xp_reward", 0)):
                    yield update
            else:
                self.feedback_message = "El código se ejecutó, pero no pasó todas las pruebas."
                
        except Exception as e:
            output = f.getvalue()
            self.terminal_output = output + f"\nError de Ejecución: {str(e)}"
            self.feedback_message = "Tu código tiene errores. Revisa la consola."
            
        self.is_loading = False
        yield
