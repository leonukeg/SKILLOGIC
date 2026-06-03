import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.components.landing.helpers import t

def problem_solution_section() -> rx.Component:
    """Old Way vs New Way (PAS Formula) contrast section."""
    def column(title_es: str, title_en: str, items_es: list[str], items_en: list[str], is_bad: bool) -> rx.Component:
        color = T.ERROR if is_bad else T.SUCCESS
        icon = "circle-x" if is_bad else "circle-check"
        bg_color = "rgba(239, 68, 68, 0.05)" if is_bad else "rgba(34, 197, 94, 0.05)"
        
        return rx.vstack(
            rx.text(t(title_es, title_en), font_size=T.TEXT_XL, font_weight=T.WEIGHT_BOLD, color=color, margin_bottom=T.SPACE_6),
            *[
                rx.hstack(
                    rx.icon(tag=icon, size=20, color=color, margin_top="2px"),
                    rx.text(t(es, en), font_size=T.TEXT_BASE, color=T.TEXT_PRIMARY, line_height="1.5"),
                    align="start",
                    gap=T.SPACE_3,
                    margin_bottom=T.SPACE_4
                ) for es, en in zip(items_es, items_en)
            ],
            background=bg_color,
            border=f"1px solid {color}",
            border_radius=T.RADIUS_XL,
            padding=T.SPACE_8,
            width="100%",
            height="100%",
            box_shadow=f"0 10px 30px -15px {color}" if not is_bad else "none",
        )

    return rx.box(
        rx.vstack(
            rx.text(t("El Problema", "The Problem"), font_size=T.TEXT_SM, font_weight=T.WEIGHT_BOLD, color=T.BRAND, letter_spacing="1px", text_transform="uppercase"),
            rx.text(t("Por qué abandonar cursos es tan común", "Why dropping courses is so common"), font_size=T.TEXT_3XL, font_weight=T.WEIGHT_EXTRABOLD, color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_8, text_align="center"),
            
            rx.grid(
                column(
                    "La Forma Tradicional (Aburrida)",
                    "The Traditional Way (Boring)",
                    [
                        "Miras horas de videos pasivamente sin escribir código.",
                        "Configuras entornos locales frustrantes antes de empezar.",
                        "Te quedas atascado en el 'Tutorial Hell' sin saber qué construir.",
                        "Pierdes la motivación a los pocos días por falta de progreso."
                    ],
                    [
                        "You passively watch hours of videos without writing code.",
                        "You set up frustrating local environments before starting.",
                        "You get stuck in 'Tutorial Hell' not knowing what to build.",
                        "You lose motivation after a few days due to lack of progress."
                    ],
                    True
                ),
                column(
                    "El Método SKILLOGIC",
                    "The SKILLOGIC Method",
                    [
                        "Escribes código desde el minuto uno, directo en el navegador.",
                        "Gamificación real: ganas XP, subes de nivel y mantienes rachas.",
                        "Feedback instantáneo si tu código falla, guiándote a la solución.",
                        "Construyes memoria muscular resolviendo problemas reales."
                    ],
                    [
                        "You write code from minute one, directly in the browser.",
                        "Real gamification: earn XP, level up, and maintain streaks.",
                        "Instant feedback if your code fails, guiding you to the solution.",
                        "You build muscle memory by solving real problems."
                    ],
                    False
                ),
                columns=rx.breakpoints(initial="1", md="2"),
                gap=T.SPACE_8,
                width="100%",
                max_width="1000px",
                margin="0 auto"
            ),
            align="center",
            width="100%",
        ),
        padding=f"{T.SPACE_16} {T.SPACE_4}",
        background=T.BG_PRIMARY,
        margin_top=T.SPACE_10,
    )