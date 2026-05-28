import reflex as rx
from SKILLOGIC.lib.supabase_client import get_supabase
from SKILLOGIC.state.auth_state import AuthState

class UpdatePasswordState(rx.State):
    """Maneja el flujo de actualización de contraseña segura desde el link del correo."""
    
    password: str = ""
    confirm_password: str = ""
    error_message: str = ""
    is_loading: bool = False
    is_success: bool = False
    
    async def on_load(self):
        # Capturamos el código PKCE o el access_token del implicit flow
        code = self.router.page.params.get("code")
        access_token = self.router.page.params.get("access_token")
        refresh_token = self.router.page.params.get("refresh_token")
        
        client = get_supabase()
        if not client: return
        
        try:
            if code:
                client.auth.exchange_code_for_session({"auth_code": code})
            elif access_token and refresh_token:
                # Si viene del script JS de la vista (Implicit Flow)
                client.auth.set_session(access_token, refresh_token)
            elif access_token:
                # A veces Supabase no manda refresh_token en reset
                client.auth.set_session(access_token, "")
        except Exception as e:
            self.error_message = f"Error validando el link: {str(e)}"
                    
    def set_password(self, val: str):
        self.password = val
        self.error_message = ""
        
    def set_confirm_password(self, val: str):
        self.confirm_password = val
        self.error_message = ""
    
    def handle_update_password(self):
        self.error_message = ""
        
        if not self.password or not self.confirm_password:
            self.error_message = "Por favor, completa ambos campos."
            return
            
        if self.password != self.confirm_password:
            self.error_message = "Las contraseñas no coinciden."
            return
            
        if len(self.password) < 6:
            self.error_message = "La contraseña debe tener al menos 6 caracteres."
            return
            
        self.is_loading = True
        client = get_supabase()
        
        if client:
            try:
                # El usuario ya debería estar autenticado temporalmente por la sesión del link
                res = client.auth.update_user({"password": self.password})
                if res.user:
                    self.is_success = True
                    self.error_message = ""
                    # Opcionalmente, podemos redirigir inmediatamente
                    # return rx.redirect("/dashboard")
            except Exception as e:
                self.error_message = f"Error al actualizar la contraseña: {str(e)}"
                
        self.is_loading = False
        
    def redirect_to_dashboard(self):
        return rx.redirect("/dashboard")
