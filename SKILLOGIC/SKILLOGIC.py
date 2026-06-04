"""
SKILLOGIC — Application Entry Point
Registers all pages, applies global styles, bootstraps the Reflex app.
"""

import reflex as rx

from SKILLOGIC.pages.login import login_page
from SKILLOGIC.pages.register import register_page
from SKILLOGIC.pages.dashboard import dashboard_page
from SKILLOGIC.pages.admin import admin_page
from SKILLOGIC.pages.lesson import lesson_page
from SKILLOGIC.pages.update_password import update_password_page
from SKILLOGIC.pages.katas_list import katas_list_page
from SKILLOGIC.pages.kata_solver import kata_page
from SKILLOGIC.pages.landing import landing_page
from SKILLOGIC.pages.roadmap import roadmap_page
from SKILLOGIC.pages import legal
from SKILLOGIC.state.curriculum_state import CurriculumState
from SKILLOGIC.state.admin_users_state import AdminUsersState
from SKILLOGIC.state.update_password_state import UpdatePasswordState
from SKILLOGIC.state.auth_state import AuthState
from SKILLOGIC.state.progress_state import ProgressState
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.styles.theme import GOOGLE_FONTS_URL

# ── Global stylesheet ─────────────────────────────────────────
# Defines the CSS custom property structure for the dark/light token system
# that backs the design tokens imported from styles/theme.py.

GLOBAL_STYLES = {
    "body": {
        "background": "var(--bg-primary, #0D1117)",
        "color": "var(--text-primary, #E6EDF3)",
        "font_family": "'Inter', system-ui, -apple-system, sans-serif",
        "margin": "0",
        "padding": "0",
        "-webkit-font-smoothing": "antialiased",
        "-moz-osx-font-smoothing": "grayscale",
    },
    "*": {
        "box_sizing": "border-box",
    },
    "::selection": {
        "background": "rgba(124, 58, 237, 0.3)",
    },
    # Scrollbar styling (Webkit)
    "::-webkit-scrollbar": {
        "width": "6px",
        "height": "6px",
    },
    "::-webkit-scrollbar-track": {
        "background": "transparent",
    },
    "::-webkit-scrollbar-thumb": {
        "background": "#30363D",
        "border_radius": "3px",
    },
    "::-webkit-scrollbar-thumb:hover": {
        "background": "#484F58",
    },
    # Float animation for hero element
    "@keyframes float": {
        "0%, 100%": {"transform": "translateY(0px) rotate(-3deg)"},
        "50%":      {"transform": "translateY(-14px) rotate(3deg)"},
    },
    # Python logo — smooth float + tilt
    "@keyframes pythonFloat": {
        "0%, 100%": {"transform": "translateY(0px) rotate(0deg) scale(1)"},
        "33%":      {"transform": "translateY(-30px) rotate(10deg) scale(1.08)"},
        "66%":      {"transform": "translateY(15px) rotate(-8deg) scale(0.95)"},
    },
    "@keyframes fadeIn": {
        "from": {"opacity": "0", "transform": "translateY(-8px)"},
        "to":   {"opacity": "1", "transform": "translateY(0)"},
    },
    # Hide Reflex watermark
    "a[href='https://reflex.dev']:not(#my-footer-link)": {
        "display": "none !important",
    },
    ".rt-r-position-fixed.rt-r-bottom-4.rt-r-right-4.rt-r-z-index-50": {
        "display": "none !important",
    },
    "#reflex-logo": {
        "display": "none !important",
    },
}

# ── App bootstrap ─────────────────────────────────────────────

app = rx.App(
    theme=rx.theme(appearance="dark", accent_color="purple", radius="large"),
    style=GLOBAL_STYLES,
    stylesheets=[
        GOOGLE_FONTS_URL,
        "/theme.css",   # dark / light CSS custom properties
    ],
    # HTML metadata
    head_components=[
        rx.el.meta(charset="UTF-8"),
        rx.el.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        rx.el.meta(
            name="description",
            content=(
                "SKILLOGIC — Aprende Python desde cero hasta nivel profesional. "
                "Lecciones prácticas, proyectos reales, editor de código integrado."
            ),
        ),
        rx.el.meta(property="og:title", content="SKILLOGIC — Aprende Python"),
        rx.el.title("SKILLOGIC — Aprende Python"),
    ],
)

# ── Page registration ─────────────────────────────────────────

app.add_page(
    login_page,
    route="/login",
    title="SKILLOGIC — Iniciar sesión",
    description="Inicia sesión en tu cuenta de SKILLOGIC.",
)

app.add_page(
    register_page,
    route="/register",
    title="SKILLOGIC — Registrarse",
)

# app.add_page for landing is not needed because it uses @rx.page(route="/") in landing.py

app.add_page(
    dashboard_page,
    route="/dashboard",
    title="SKILLOGIC — Dashboard",
    description="Tu panel de aprendizaje personalizado.",
    on_load=[AppState.set_home_active, AuthState.on_load, CurriculumState.load_data, ProgressState.load_stats],
)

app.add_page(
    admin_page,
    route="/admin",
    title="SKILLOGIC — Admin",
    description="Panel de administración de SKILLOGIC.",
    on_load=[AuthState.on_load, CurriculumState.load_data, AdminUsersState.load_users],
)

app.add_page(
    update_password_page,
    route="/update-password",
    title="SKILLOGIC — Actualizar Contraseña",
    description="Actualiza tu contraseña de forma segura.",
    on_load=UpdatePasswordState.on_load,
)

app.add_page(legal.terms_page, route="/terms", title="SKILLOGIC — Términos y Condiciones")
app.add_page(legal.privacy_page, route="/privacy", title="SKILLOGIC — Política de Privacidad")
app.add_page(legal.cookies_page, route="/cookies", title="SKILLOGIC — Política de Cookies")
