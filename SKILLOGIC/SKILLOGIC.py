"""
SKILLOGIC — Application Entry Point
Registers all pages, applies global styles, bootstraps the Reflex app.
"""

import reflex as rx

from SKILLOGIC.pages.login import login_page
from SKILLOGIC.pages.dashboard import dashboard_page
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
    # Python logo — float + subtle spin
    "@keyframes pythonFloat": {
        "0%, 100%": {"transform": "translateY(0px) rotate(0deg) scale(1)"},
        "25%":      {"transform": "translateY(-10px) rotate(6deg) scale(1.04)"},
        "75%":      {"transform": "translateY(-6px) rotate(-4deg) scale(1.02)"},
    },
    # Soft glow pulse for the logo
    "@keyframes pythonGlow": {
        "0%, 100%": {"filter": "drop-shadow(0 0 8px rgba(55, 118, 171, 0.5))"},
        "50%":      {"filter": "drop-shadow(0 0 20px rgba(55, 118, 171, 0.85)) drop-shadow(0 0 8px rgba(255, 212, 59, 0.6))"},
    },
    "@keyframes fadeIn": {
        "from": {"opacity": "0", "transform": "translateY(-8px)"},
        "to":   {"opacity": "1", "transform": "translateY(0)"},
    },
}

# ── App bootstrap ─────────────────────────────────────────────

app = rx.App(
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
    login_page,
    route="/",
    title="SKILLOGIC — Bienvenido",
)

app.add_page(
    dashboard_page,
    route="/dashboard",
    title="SKILLOGIC — Dashboard",
    description="Tu panel de aprendizaje personalizado.",
)
