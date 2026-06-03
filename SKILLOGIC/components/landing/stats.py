import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.components.landing.helpers import t

def stats_section() -> rx.Component:
    """Social proof statistics bar."""
    def stat_item(value: str, label_es: str, label_en: str) -> rx.Component:
        return rx.vstack(
            rx.text(value, font_size=T.TEXT_4XL, font_weight=T.WEIGHT_EXTRABOLD, color="white", style={"text_shadow": f"0 0 15px {T.BRAND}"}),
            rx.text(t(label_es, label_en), font_size=T.TEXT_SM, color=T.TEXT_SECONDARY, text_transform="uppercase", letter_spacing="1px"),
            align="center",
            padding=T.SPACE_4,
        )

    return rx.box(
        rx.hstack(
            stat_item("+50", "Katas Interactivos", "Interactive Katas"),
            rx.divider(orientation="vertical", border_color=T.BORDER_SUBTLE, height="40px", display=rx.breakpoints(initial="none", md="block")),
            stat_item("5", "Módulos Intensivos", "Intensive Modules"),
            rx.divider(orientation="vertical", border_color=T.BORDER_SUBTLE, height="40px", display=rx.breakpoints(initial="none", md="block")),
            stat_item("10x", "Aprendizaje Más Rápido", "Faster Learning"),
            width="100%",
            justify="center",
            align="center",
            gap=rx.breakpoints(initial=T.SPACE_8, md=T.SPACE_16),
            flex_wrap="wrap",
        ),
        padding=f"{T.SPACE_8} {T.SPACE_4}",
        background=T.BG_ELEVATED,
        border_top=f"1px solid {T.BORDER_SUBTLE}",
        border_bottom=f"1px solid {T.BORDER_SUBTLE}",
        margin_bottom=T.SPACE_16,
    )