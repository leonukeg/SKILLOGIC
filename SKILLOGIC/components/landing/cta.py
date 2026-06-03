import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.components.landing.helpers import t

def bottom_cta_section() -> rx.Component:
    """Strong bottom call to action before the footer."""
    return rx.box(
        rx.vstack(
            rx.text(t("¿Listo para escribir tu primera línea?", "Ready to write your first line?"), font_size=T.TEXT_3XL, font_weight=T.WEIGHT_EXTRABOLD, color="white", text_align="center", margin_bottom=T.SPACE_4),
            rx.text(t("Únete a SKILLOGIC hoy y transforma tu carrera aprendiendo la tecnología más demandada del mercado.", "Join SKILLOGIC today and transform your career by learning the most in-demand technology in the market."), font_size=T.TEXT_LG, color="rgba(255,255,255,0.8)", text_align="center", max_width="600px", margin_bottom=T.SPACE_8),
            rx.button(
                t("Comenzar mi aprendizaje gratis", "Start my learning for free"),
                on_click=rx.redirect("/register"),
                size="4",
                variant="solid",
                bg="white",
                color_scheme="gray",
                color=T.BRAND,
                border_radius=T.RADIUS_LG,
                padding=f"{T.SPACE_4} {T.SPACE_8}",
                font_weight=T.WEIGHT_EXTRABOLD,
                font_size=T.TEXT_LG,
                box_shadow=f"0 10px 30px rgba(0,0,0,0.3)",
                _hover={"transform": "translateY(-2px)", "box_shadow": f"0 15px 40px rgba(0,0,0,0.4)"},
                transition=f"all {T.EASE_BASE}",
            ),
            align="center",
            padding=f"{T.SPACE_16} {T.SPACE_4}",
            background=f"linear-gradient(135deg, {T.BRAND}, #a855f7)",
            border_radius=T.RADIUS_2XL,
            box_shadow=T.SHADOW_BRAND,
            max_width="1000px",
            margin="0 auto",
        ),
        padding=f"{T.SPACE_10} {T.SPACE_4}",
        margin_top=T.SPACE_10,
        margin_bottom=T.SPACE_10,
    )

