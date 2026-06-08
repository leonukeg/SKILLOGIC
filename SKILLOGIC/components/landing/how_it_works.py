import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.components.landing.helpers import t

def how_it_works_section() -> rx.Component:
    """Vertical timeline step-by-step guide."""
    
    def timeline_step(number: str, title_es: str, title_en: str, desc_es: str, desc_en: str, is_last: bool = False) -> rx.Component:
        return rx.hstack(
            rx.vstack(
                rx.flex(
                    rx.text(number, font_weight=T.WEIGHT_EXTRABOLD, font_size=T.TEXT_LG, color="white"),
                    width="48px", height="48px", border_radius="50%",
                    background=f"linear-gradient(135deg, {T.BRAND}, #a855f7)",
                    box_shadow=f"0 0 20px rgba(168, 85, 247, 0.4)",
                    align="center", justify="center", z_index="2"
                ),
                rx.cond(
                    not is_last,
                    rx.box(width="2px", height="100%", background=f"linear-gradient(to bottom, {T.BRAND}, transparent)", margin_top=T.SPACE_2, flex="1")
                ),
                align="center",
                height="100%",
                min_height="120px",
                width="60px",
            ),
            rx.vstack(
                rx.text(t(title_es, title_en), font_size=T.TEXT_2XL, font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
                rx.text(t(desc_es, desc_en), font_size=T.TEXT_BASE, color=T.TEXT_SECONDARY, line_height="1.6", max_width="500px"),
                align="start",
                padding_top=T.SPACE_2,
                padding_bottom=T.SPACE_8 if not is_last else "0",
            ),
            align="start",
            gap=T.SPACE_6,
            width="100%",
        )

    return rx.box(
        rx.vstack(
            rx.text(t("El Proceso", "The Process"), font_size=T.TEXT_SM, font_weight=T.WEIGHT_BOLD, color=T.BRAND, letter_spacing="1px", text_transform="uppercase"),
            rx.text(t("Cómo funciona SKILLOGIC", "How SKILLOGIC works"), font_size=T.TEXT_3XL, font_weight=T.WEIGHT_EXTRABOLD, color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_12, text_align="center"),
            
            rx.vstack(
                timeline_step(
                    "1",
                    "Aprende el concepto", "Learn the concept",
                    "Lecciones cortas, directas al grano. Sin relleno. Solo la teoría estrictamente necesaria para entender el porqué de las cosas.",
                    "Short, straight to the point lessons. No fluff. Only the strictly necessary theory to understand the why of things."
                ),
                timeline_step(
                    "2",
                    "Escribe código al instante", "Write code instantly",
                    "Te enfrentamos a un reto inmediatamente. Tienes un editor en el navegador listo para que pruebes tu comprensión.",
                    "We face you with a challenge immediately. You have an in-browser editor ready for you to test your understanding."
                ),
                timeline_step(
                    "3",
                    "Gana XP y sube de nivel", "Earn XP and level up",
                    "Si tu código pasa las pruebas (tests invisibles), ganas puntos de experiencia. ¡Siente el progreso en cada lección!",
                    "If your code passes the tests (invisible tests), you earn experience points. Feel the progress in every lesson!",
                    is_last=True
                ),
                align="start",
                max_width="700px",
                margin="0 auto"
            ),
            align="center",
            width="100%",
        ),
        padding=f"{T.SPACE_16} {T.SPACE_4}",
        background=T.BG_SECONDARY,
    )