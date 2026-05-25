"""
SKILLOGIC — Login Page
Auth form with demo access and registration link.
"""

import reflex as rx
from SKILLOGIC.state import AppState
from SKILLOGIC.styles import theme as T

# Hardcoded accent colors that don't change with theme
_VIOLET = "#a855f7"
_LILAC  = "#a78bfa"


def login_page() -> rx.Component:
    """Login page — no sidebar, centered card layout."""

    return rx.box(
        # Background glow effects
        rx.box(
            position="absolute",
            width="600px",
            height="600px",
            border_radius="50%",
            background=f"radial-gradient(circle, {T.BRAND_LIGHT} 0%, transparent 70%)",
            top="-200px",
            right="-100px",
            pointer_events="none",
        ),
        rx.box(
            position="absolute",
            width="400px",
            height="400px",
            border_radius="50%",
            background="radial-gradient(circle, rgba(249,115,22,0.06) 0%, transparent 70%)",
            bottom="-100px",
            left="-100px",
            pointer_events="none",
        ),

        # Card
        rx.box(
            # Logo
            rx.hstack(
                rx.box(
                    rx.text("⚡", font_size="22px"),
                    width="44px",
                    height="44px",
                    background=f"linear-gradient(135deg, {T.BRAND}, #a855f7)",
                    border_radius=T.RADIUS_LG,
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    box_shadow=T.SHADOW_BRAND,
                ),
                rx.text(
                    "SKILLOGIC",
                    font_size=T.TEXT_XL,
                    font_weight=T.WEIGHT_EXTRABOLD,
                    letter_spacing="-0.5px",
                    color=rx.cond(AppState.is_dark, "transparent", "#1F2328"),
                    background=rx.cond(
                        AppState.is_dark,
                        "linear-gradient(135deg, #E6EDF3, #a78bfa)",
                        "none",
                    ),
                    background_clip=rx.cond(AppState.is_dark, "text", "initial"),
                    webkit_background_clip=rx.cond(AppState.is_dark, "text", "initial"),
                    webkit_text_fill_color=rx.cond(AppState.is_dark, "transparent", "#1F2328"),
                ),
                align="center",
                gap=T.SPACE_3,
                justify="center",
                margin_bottom=T.SPACE_8,
            ),

            # Title
            rx.text(
                rx.cond(AppState.is_spanish, "Bienvenido de vuelta", "Welcome back"),
                font_size=T.TEXT_2XL,
                font_weight=T.WEIGHT_BOLD,
                text_align="center",
                color=T.TEXT_PRIMARY,
                margin_bottom=T.SPACE_1,
            ),
            rx.text(
                rx.cond(
                    AppState.is_spanish,
                    "Continúa aprendiendo Python donde lo dejaste",
                    "Continue learning Python where you left off",
                ),
                font_size=T.TEXT_SM,
                color=T.TEXT_MUTED,
                text_align="center",
                margin_bottom=T.SPACE_8,
            ),

            # Email field
            rx.vstack(
                rx.text(
                    rx.cond(AppState.is_spanish, "Correo electrónico", "Email address"),
                    font_size=T.TEXT_SM,
                    font_weight=T.WEIGHT_MEDIUM,
                    color=T.TEXT_SECONDARY,
                    align_self="start",
                ),
                rx.el.input(
                    type="email",
                    placeholder=rx.cond(AppState.is_spanish, "tu@email.com", "you@email.com"),
                    id="login-email",
                    width="100%",
                    height="44px",
                    background=T.BG_ELEVATED,
                    border=f"1px solid {T.BORDER}",
                    border_radius=T.RADIUS_MD,
                    color=T.TEXT_PRIMARY,
                    font_size=T.TEXT_BASE,
                    padding=f"0 {T.SPACE_4}",
                    outline="none",
                    font_family=T.FONT_BODY,
                    _placeholder={"color": T.TEXT_DISABLED},
                    _focus={
                        "border_color": T.BRAND,
                        "box_shadow": f"0 0 0 3px {T.BRAND_LIGHT}",
                    },
                ),
                spacing="2",
                width="100%",
                margin_bottom=T.SPACE_4,
            ),

            # Password field
            rx.vstack(
                rx.text(
                    rx.cond(AppState.is_spanish, "Contraseña", "Password"),
                    font_size=T.TEXT_SM,
                    font_weight=T.WEIGHT_MEDIUM,
                    color=T.TEXT_SECONDARY,
                    align_self="start",
                ),
                rx.el.input(
                    type="password",
                    placeholder="••••••••",
                    id="login-password",
                    width="100%",
                    height="44px",
                    background=T.BG_ELEVATED,
                    border=f"1px solid {T.BORDER}",
                    border_radius=T.RADIUS_MD,
                    color=T.TEXT_PRIMARY,
                    font_size=T.TEXT_BASE,
                    padding=f"0 {T.SPACE_4}",
                    outline="none",
                    font_family=T.FONT_BODY,
                    _placeholder={"color": T.TEXT_DISABLED},
                    _focus={
                        "border_color": T.BRAND,
                        "box_shadow": f"0 0 0 3px {T.BRAND_LIGHT}",
                    },
                ),
                spacing="2",
                width="100%",
                margin_bottom=T.SPACE_2,
            ),

            # Submit button
            rx.button(
                rx.cond(AppState.is_spanish, "Iniciar sesión", "Sign in"),
                width="100%",
                height="48px",
                background=T.BRAND,
                color="white",
                border_radius=T.RADIUS_MD,
                font_size=T.TEXT_BASE,
                font_weight=T.WEIGHT_SEMIBOLD,
                cursor="pointer",
                box_shadow=T.SHADOW_BRAND,
                margin_top=T.SPACE_2,
                transition=f"all {T.EASE_FAST}",
                _hover={
                    "background": T.BRAND_HOVER,
                    "transform": "translateY(-1px)",
                    "box_shadow": f"0 6px 28px {T.BRAND_GLOW}",
                },
                on_click=AppState.login_mock,
            ),

            # Divider
            rx.hstack(
                rx.divider(color=T.BORDER),
                rx.text(
                    rx.cond(AppState.is_spanish, "o", "or"),
                    font_size=T.TEXT_XS,
                    color=T.TEXT_MUTED,
                    white_space="nowrap",
                    padding=f"0 {T.SPACE_4}",
                ),
                rx.divider(color=T.BORDER),
                align="center",
                margin=f"{T.SPACE_5} 0",
                width="100%",
            ),

            # Demo access button
            rx.button(
                rx.cond(AppState.is_spanish, "🚀 Entrar con cuenta demo", "🚀 Enter with demo account"),
                width="100%",
                height="44px",
                background="transparent",
                color=T.TEXT_PRIMARY,
                border=f"1px solid {T.BORDER_STRONG}",
                border_radius=T.RADIUS_MD,
                font_size=T.TEXT_BASE,
                font_weight=T.WEIGHT_SEMIBOLD,
                cursor="pointer",
                transition=f"all {T.EASE_FAST}",
                _hover={"background": T.BG_HOVER},
                on_click=AppState.login_mock,
            ),

            # Register link
            rx.hstack(
                rx.text(
                    rx.cond(AppState.is_spanish, "¿No tienes cuenta?", "Don't have an account?"),
                    font_size=T.TEXT_SM,
                    color=T.TEXT_MUTED,
                ),
                rx.link(
                    rx.cond(AppState.is_spanish, "Regístrate gratis", "Sign up for free"),
                    href="/register",
                    font_size=T.TEXT_SM,
                    color=T.BRAND,
                    font_weight=T.WEIGHT_MEDIUM,
                    _hover={"color": "#a78bfa"},
                ),
                justify="center",
                gap=T.SPACE_2,
                margin_top=T.SPACE_6,
            ),

            # Card styles
            background=T.BG_SECONDARY,
            border=f"1px solid {T.BORDER}",
            border_radius=T.RADIUS_2XL,
            padding=f"{T.SPACE_10} {T.SPACE_8}",
            width="100%",
            max_width="420px",
            position="relative",
            z_index="1",
            box_shadow=T.SHADOW_XL,
        ),

        # Full-page container
        data_theme=AppState.theme,
        display="flex",
        align_items="center",
        justify_content="center",
        min_height="100vh",
        width="100%",
        padding=T.SPACE_4,
        background=T.BG_PRIMARY,
        font_family=T.FONT_BODY,
        position="relative",
        overflow="hidden",
    )
