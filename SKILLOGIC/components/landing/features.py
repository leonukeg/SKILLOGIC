import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.components.landing.helpers import t

def features_section() -> rx.Component:
    """Bento Box style features grid with Glassmorphism."""
    
    def bento_card(title_es: str, title_en: str, desc_es: str, desc_en: str, icon_tag: str, span_col: str, gradient: str) -> rx.Component:
        return rx.box(
            rx.vstack(
                rx.box(
                    rx.icon(tag=icon_tag, size=28, color="white"),
                    background=gradient,
                    padding="12px",
                    border_radius=T.RADIUS_LG,
                    box_shadow=f"0 4px 15px {gradient.split(',')[1]}40",
                    margin_bottom=T.SPACE_4,
                ),
                rx.text(t(title_es, title_en), font_size=T.TEXT_XL, font_weight=T.WEIGHT_EXTRABOLD, color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_2),
                rx.text(t(desc_es, desc_en), font_size=T.TEXT_BASE, color=T.TEXT_SECONDARY, line_height="1.5"),
                align="start",
                height="100%",
                justify="center",
            ),
            background="rgba(30, 35, 45, 0.4)",
            backdrop_filter="blur(12px)",
            border=f"1px solid {T.BORDER_SUBTLE}",
            border_radius=T.RADIUS_2XL,
            padding=T.SPACE_8,
            transition=f"all {T.EASE_BASE}",
            _hover={"transform": "translateY(-4px)", "border_color": T.BORDER_STRONG, "box_shadow": f"0 15px 30px -10px rgba(0,0,0,0.5)"},
            grid_column=rx.breakpoints(initial="span 1", md=span_col),
            height="100%",
            min_height="250px",
        )

    return rx.box(
        rx.vstack(
            rx.text(t("Características", "Features"), font_size=T.TEXT_SM, font_weight=T.WEIGHT_BOLD, color=T.BRAND, letter_spacing="1px", text_transform="uppercase"),
            rx.text(t("Todo lo que necesitas para dominar Python", "Everything you need to master Python"), font_size=T.TEXT_3XL, font_weight=T.WEIGHT_EXTRABOLD, color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_8, text_align="center"),
            
            rx.grid(
                bento_card(
                    "Aprende Haciendo", "Learn by Doing",
                    "Escribe código real en el navegador desde el primer minuto. Sin configuraciones locales, sin instalaciones.", "Write real code in the browser from minute one. No local setups, no installations.",
                    "code", "span 2", f"linear-gradient(135deg, {T.BRAND}, #a855f7)"
                ),
                bento_card(
                    "Gamificación Real", "Real Gamification",
                    "Gana XP, mantén tu racha de días y desbloquea logros mientras aprendes.", "Earn XP, keep your daily streak and unlock achievements while learning.",
                    "gamepad-2", "span 1", "linear-gradient(135deg, #10b981, #059669)"
                ),
                bento_card(
                    "Katas Diarios", "Daily Katas",
                    "Practica tu lógica con mini-retos de código que fortalecen tu memoria muscular.", "Practice your logic with code mini-challenges that build your muscle memory.",
                    "swords", "span 1", "linear-gradient(135deg, #f59e0b, #d97706)"
                ),
                bento_card(
                    "Feedback Instantáneo", "Instant Feedback",
                    "Nuestro sistema evalúa tu código al instante y te da pistas si te equivocas.", "Our system evaluates your code instantly and gives you hints if you make a mistake.",
                    "zap", "span 2", "linear-gradient(135deg, #3b82f6, #2563eb)"
                ),
                columns=rx.breakpoints(initial="1", md="3"),
                gap=T.SPACE_6,
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