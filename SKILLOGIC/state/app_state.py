"""
SKILLOGIC — Global App State
Single rx.State subclass that manages all application-level state.
Lesson-specific state is handled in page-level State classes.
"""

import reflex as rx
from typing import List
from SKILLOGIC.styles.theme import LEVELS


class AppState(rx.State):
    """
    Global state: auth, theme, language, user stats.
    Follows the Immutability-by-default principle:
    all mutations go through explicit EventHandlers.
    """

    # ── Auth ──────────────────────────────────────────────────
    is_authenticated: bool = False
    user_name: str = ""
    user_email: str = ""
    user_initials: str = ""

    # ── User progress ─────────────────────────────────────────
    user_level: int = 4
    user_xp: int = 820
    user_xp_to_next: int = 1200
    user_streak: int = 7
    user_rank: str = "Explorer"
    streak_days: List[bool] = [True, True, True, True, False, False, False]

    # ── Theme ─────────────────────────────────────────────────
    # dark = ES (primary),  light = EN (secondary)
    theme: str = "dark"   # "dark" | "light"
    lang: str = "es"      # "es"   | "en"

    # ── Navigation & UI ────────────────────────────────────────────
    active_nav: str = "home"
    cookies_accepted: bool = False

    @rx.event
    def accept_cookies(self):
        self.cookies_accepted = True

    
    def set_home_active(self):
        if self.active_nav not in ["home", "lessons"]:
            self.active_nav = "home"

    # ── Computed helpers ──────────────────────────────────────
    @rx.var
    def xp_percent(self) -> int:
        """XP progress as integer percentage 0-100."""
        if self.user_xp_to_next == 0:
            return 100
        return min(int((self.user_xp / self.user_xp_to_next) * 100), 100)

    @rx.var
    def level_name(self) -> str:
        """Human-readable level name derived from XP."""
        for lvl in reversed(LEVELS):
            if self.user_xp >= lvl["xp_required"]:
                return lvl["name"]
        return LEVELS[0]["name"]

    @rx.var
    def is_dark(self) -> bool:
        return self.theme == "dark"

    @rx.var
    def is_spanish(self) -> bool:
        return self.lang == "es"

    @rx.var
    def toggle_theme_label(self) -> str:
        return "🌙" if self.is_dark else "☀️"

    @rx.var
    def toggle_theme_title(self) -> str:
        if self.is_dark:
            return "Cambiar a modo claro / Switch to light mode"
        return "Cambiar a modo oscuro / Switch to dark mode"

    @rx.var
    def toggle_lang_label(self) -> str:
        return "ES" if self.is_spanish else "EN"

    @rx.var
    def toggle_lang_title(self) -> str:
        return "Switch to English" if self.is_spanish else "Cambiar a Español"

    # ── Theme toggle (independent) ────────────────────────────
    def toggle_theme(self):
        """Toggle dark ↔ light mode independently."""
        self.theme = "light" if self.theme == "dark" else "dark"

    # ── Language toggle (independent) ─────────────────────────
    def toggle_lang(self):
        """Toggle es ↔ en independently."""
        self.lang = "en" if self.lang == "es" else "es"

    # ── Auth actions ─────────────────────────────────────────
    def login_mock(self):
        """Mock login for Phase 0 — replace with real JWT in Phase 1."""
        self.is_authenticated = True
        self.user_name = "Juan"
        self.user_email = "juan@example.com"
        self.user_initials = "JU"
        return rx.redirect("/dashboard")

    def logout(self):
        self.is_authenticated = False
        self.user_name = ""
        self.user_email = ""
        self.user_initials = ""
        return rx.redirect("/login")

    # ── Navigation ───────────────────────────────────────────
    def set_active_nav(self, item: str):
        self.active_nav = item
