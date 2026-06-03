import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState

def cookie_banner() -> rx.Component:
    """Cookie consent banner displayed at the bottom of the screen."""
    return rx.cond(
        ~AppState.cookies_accepted,
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.text("Utilizamos cookies", font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY, font_size=T.TEXT_MD),
                    rx.text(
                        "Usamos cookies propias y de terceros para mejorar nuestros servicios y mostrarle publicidad relacionada con sus preferencias mediante el análisis de sus hábitos de navegación.",
                        font_size=T.TEXT_SM, color=T.TEXT_SECONDARY, max_width="600px", line_height="1.5"
                    ),
                    align_items="flex-start",
                ),
                rx.spacer(),
                rx.hstack(
                    rx.link("Leer más", href="/cookies", font_size=T.TEXT_SM, color=T.BRAND_LIGHT, text_decoration="underline"),
                    rx.button(
                        "Aceptar cookies",
                        on_click=AppState.accept_cookies,
                        color_scheme="purple",
                        variant="solid",
                        size="2",
                        border_radius=T.RADIUS_MD,
                    ),
                    align="center",
                    gap=T.SPACE_4,
                ),
                width="100%",
                align="center",
                flex_direction=["column", "column", "row"],
                gap=T.SPACE_4,
            ),
            position="fixed",
            bottom="0",
            left="0",
            width="100%",
            background=T.BG_SECONDARY,
            border_top=f"1px solid {T.BORDER_SUBTLE}",
            padding=T.SPACE_4,
            z_index="50",
            box_shadow="0 -4px 10px rgba(0,0,0,0.2)",
        ),
        rx.fragment()
    )
