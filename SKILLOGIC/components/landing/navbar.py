import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.components.landing.helpers import t

def landing_navbar() -> rx.Component:
    """Navbar for the landing page."""
    return rx.flex(
        # Logo
        rx.hstack(
            rx.flex(
                rx.icon(tag="zap", size=18, color="white"),
                width="36px", height="36px",
                background=f"linear-gradient(135deg, {T.BRAND}, #a855f7)",
                border_radius=T.RADIUS_MD,
                box_shadow=T.SHADOW_BRAND,
                align="center", justify="center",
            ),
            rx.text(
                "SKILLOGIC",
                font_size=T.TEXT_LG,
                font_weight=T.WEIGHT_EXTRABOLD,
                letter_spacing="-0.3px",
                color=T.TEXT_PRIMARY,
            ),
            align="center", gap=T.SPACE_2,
        ),
        
        # Auth Buttons & Lang Toggle
        rx.flex(
            rx.button(
                AppState.toggle_lang_label,
                on_click=AppState.toggle_lang,
                variant="ghost",
                color_scheme="gray",
                size="2",
                title=AppState.toggle_lang_title,
                font_weight=T.WEIGHT_BOLD,
            ),
            rx.button(
                t("Iniciar sesión", "Log in"),
                on_click=rx.redirect("/login"),
                variant="ghost",
                color_scheme="gray",
                color=T.TEXT_SECONDARY,
                _hover={"color": T.TEXT_PRIMARY},
                font_weight=T.WEIGHT_SEMIBOLD,
            ),
            rx.button(
                t("Comenzar gratis", "Start for free"),
                on_click=rx.redirect("/register"),
                variant="solid",
                color_scheme="purple",
                color="white",
                border_radius=T.RADIUS_MD,
                box_shadow=T.SHADOW_BRAND,
                _hover={"background_color": T.BRAND_HOVER},
                font_weight=T.WEIGHT_SEMIBOLD,
                padding=f"{T.SPACE_2} {T.SPACE_4}",
            ),
            gap=T.SPACE_4,
            align="center",
            flex_wrap="wrap",
            justify="center",
            margin_top=rx.breakpoints(initial=T.SPACE_4, sm="0"),
        ),
        width="100%",
        padding=rx.breakpoints(initial=f"{T.SPACE_4}", md=f"{T.SPACE_4} {T.SPACE_8}"),
        max_width="1200px",
        margin="0 auto",
        align="center",
        justify="between",
        flex_direction=rx.breakpoints(initial="column", sm="row"),
    )

