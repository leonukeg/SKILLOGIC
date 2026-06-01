import reflex as rx
from SKILLOGIC.lib.supabase_client import get_supabase, fetch_user_profile

class AuthState(rx.State):
    """Maneja el estado de la autenticación de Supabase."""
    
    email: str = ""
    password: str = ""
    name: str = ""
    
    user_id: str = ""
    user_email: str = ""
    role: str = "basic"
    error_message: str = ""
    
    # Cookie para persistir la sesión de Auth
    # max_age se pone en varios días para no caducar
    auth_token: str = rx.Cookie(name="sb_token", max_age=60*60*24*7)
    
    def on_load(self):
        """Revisa la cookie para ver si hay sesión guardada."""
        client = get_supabase()
        if not client: return
        
        if self.auth_token:
            try:
                # Intentar refrescar la sesión con el JWT guardado
                res = client.auth.get_user(self.auth_token)
                if res and res.user:
                    self.user_id = res.user.id
                    self.user_email = res.user.email
            except Exception as e:
                # Si falla, borramos el token
                self.auth_token = ""
                self.user_id = ""
                self.user_email = ""
                self.error_message = "Sesión expirada o inválida."
    
    @rx.var
    def is_authenticated(self) -> bool:
        return self.user_id != ""
        
    @rx.var
    def is_master(self) -> bool:
        # We fetch the role from the profile data dynamically, but we can also store it in the state.
        # Let's temporarily store role in AuthState for fast UI.
        return self.user_email in ["admin@skillogic.com", "chemaruan@gmail.com"] or getattr(self, "role", "") == "master"
        
    def set_email(self, val: str):
        self.email = val
        self.error_message = ""
        
    def set_password(self, val: str):
        self.password = val
        self.error_message = ""
        
    def set_name(self, val: str):
        self.name = val
        self.error_message = ""

    def login(self, form_data: dict = None):
        if not self.email or not self.password:
            self.error_message = "Por favor, completa todos los campos."
            return

        client = get_supabase()
        if not client:
            self.error_message = "Error interno: Base de datos no configurada."
            return
            
        login_email = self.email
        if "@" not in login_email:
            if login_email == "admin":
                login_email = "admin@skillogic.com"
            elif login_email == "leonukeg":
                login_email = "chemaruan@gmail.com"
            else:
                login_email = f"{login_email}@skillogic.com"
            
        try:
            res = client.auth.sign_in_with_password({"email": login_email, "password": self.password})
            if res.user:
                self.user_id = res.user.id
                self.user_email = res.user.email
                self.auth_token = res.session.access_token
                self.error_message = ""
                
                # Update email in profiles table to ensure it's visible
                try:
                    profile = fetch_user_profile(res.user.id)
                    if profile:
                        prog = profile.get("progress") or {}
                        # Guardamos el rol en el estado local si existe
                        self.role = prog.get("role", "basic")
                        # Actualizamos el email en supabase
                        client.table("profiles").update({"email": res.user.email}).eq("id", res.user.id).execute()
                except Exception as ex:
                    print("Error updating email on login:", ex)
                return rx.redirect("/dashboard")
        except Exception as e:
            if "Invalid login credentials" in str(e):
                self.error_message = "Credenciales incorrectas."
            else:
                self.error_message = str(e)

    def signup(self, form_data: dict = None):
        if not self.name or not self.email or not self.password:
            self.error_message = "Por favor, completa todos los campos."
            return

        client = get_supabase()
        if not client:
            self.error_message = "Error interno: Base de datos no configurada."
            return
            
        signup_email = self.email
        if "@" not in signup_email:
            signup_email = f"{signup_email}@skillogic.com"
            
        try:
            res = client.auth.sign_up({
                "email": signup_email, 
                "password": self.password,
                "options": {"data": {"full_name": self.name}}
            })
            if res.user:
                self.user_id = res.user.id
                self.user_email = res.user.email
                self.auth_token = res.session.access_token if res.session else ""
                self.role = "basic"
                self.error_message = ""
                
                # Auto-create profile with email
                try:
                    client.table("profiles").insert({
                        "id": self.user_id,
                        "email": self.user_email,
                        "progress": {},
                        "streak": 0,
                        "xp": 0
                    }).execute()
                    
                    # Crear fila en user_stats
                    client.table("user_stats").insert({
                        "user_id": self.user_id,
                        "xp": 0,
                        "level": 1,
                        "streak_days": 0
                    }).execute()
                except Exception as ex:
                    print("Profile insert error:", ex)
                
                if res.session:
                    self.auth_token = res.session.access_token
                    return rx.redirect("/dashboard")
                else:
                    self.user_id = ""
                    self.user_email = ""
                    self.error_message = "Cuenta creada. Por favor, inicia sesión."
                    return rx.redirect("/login")
                    
        except Exception as e:
            if "User already registered" in str(e):
                self.error_message = "El usuario ya está registrado."
            elif "Password should be" in str(e):
                self.error_message = "La contraseña es muy débil."
            else:
                self.error_message = str(e)

    def logout(self):
        client = get_supabase()
        if client:
            client.auth.sign_out()
        self.user_id = ""
        self.user_email = ""
        self.auth_token = ""
        self.email = ""
        self.password = ""
        return rx.redirect("/login")
