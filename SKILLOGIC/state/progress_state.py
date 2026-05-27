import reflex as rx
from datetime import datetime, timezone
from SKILLOGIC.state.auth_state import AuthState
from SKILLOGIC.lib.supabase_client import fetch_user_stats, update_user_stats

# Constante base para calcular experiencia necesaria por nivel
XP_PER_LEVEL = 500

class ProgressState(rx.State):
    """Maneja el progreso, XP, niveles y rachas del usuario. Sigue el principio SoC."""
    
    xp: int = 0
    level: int = 1
    streak_days: int = 0
    last_active: str = ""

    async def load_stats(self):
        """Carga las estadísticas desde Supabase."""
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return
            
        stats = fetch_user_stats(auth.user_id)
        if stats:
            self.xp = stats.get("xp", 0)
            self.level = stats.get("level", 1)
            self.streak_days = stats.get("streak_days", 0)
            self.last_active = stats.get("last_active", "")
            
            # Recalcular la racha (ejemplo básico: si la última actividad fue hace más de 48h, se pierde)
            self._check_streak()

    def _check_streak(self):
        """Verifica si la racha se mantiene o se rompe basado en la fecha actual."""
        if not self.last_active:
            return
        # Lógica simplificada para MVP: 
        # En una app real usaríamos datetime.fromisoformat(self.last_active) y compararíamos con hoy.
        # Aquí lo dejamos preparado.
        pass

    @rx.var
    def xp_to_next_level(self) -> int:
        """Calcula cuánta XP falta para el siguiente nivel."""
        return self.level * XP_PER_LEVEL

    @rx.var
    def xp_progress_percent(self) -> int:
        """Calcula el porcentaje de progreso hacia el siguiente nivel."""
        current_level_xp = self.xp - ((self.level - 1) * XP_PER_LEVEL)
        percent = int((current_level_xp / self.xp_to_next_level) * 100)
        return min(max(percent, 0), 100)

    async def add_xp(self, amount: int):
        """Suma XP y actualiza en Supabase."""
        self.xp += amount
        
        # Subida de nivel
        while self.xp >= self.level * XP_PER_LEVEL:
            self.level += 1
            
        # Actualizar racha y fecha
        self.streak_days = max(1, self.streak_days) # Al menos 1 día de racha si hizo algo
        # self.last_active = datetime.now(timezone.utc).isoformat()
        
        auth = await self.get_state(AuthState)
        if auth.is_authenticated:
            update_user_stats(auth.user_id, {
                "xp": self.xp,
                "level": self.level,
                "streak_days": self.streak_days,
                # "last_active": self.last_active
            })
            
    async def complete_lesson(self):
        """Simula completar una lección."""
        await self.add_xp(50)
        
    async def complete_challenge(self):
        """Simula completar un reto."""
        await self.add_xp(100)
