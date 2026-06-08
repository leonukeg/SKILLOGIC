import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.components.landing.helpers import t

def hero_section() -> rx.Component:
    """Hero section following PAS/AIDA marketing formulas with floating python logo."""
    
    text_content = rx.vstack(
        # Pill badge
        rx.hstack(
            rx.icon(tag="sparkles", size=14, color="#F59E0B"),
            rx.text(t("La nueva forma de dominar Python", "The new way to master Python"), font_size=T.TEXT_SM, font_weight=T.WEIGHT_SEMIBOLD, color=T.ACCENT_LILAC),
            background=f"linear-gradient(135deg, rgba(124, 58, 237, 0.15), rgba(168, 85, 247, 0.15))",
            border=f"1px solid rgba(168, 85, 247, 0.4)",
            padding=f"6px {T.SPACE_4}",
            border_radius=T.RADIUS_FULL,
            margin_bottom=T.SPACE_6,
            align="center",
            gap=T.SPACE_2,
            box_shadow=f"0 0 20px rgba(124, 58, 237, 0.15)",
            animation="fadeIn 1s ease-out",
        ),
        
        # Hook / Headline
        rx.text(
            t("Aprende Python escribiendo ", "Learn Python by writing "),
            rx.text.span(t("código real", "real code"), color="transparent", background_image=f"linear-gradient(90deg, {T.BRAND}, #a855f7)", background_clip="text", webkit_background_clip="text"),
            t(", no solo leyendo tutoriales.", ", not just reading tutorials."),
            font_size=rx.breakpoints(initial="2.5rem", md="3.5rem", lg="4rem"),
            font_weight=T.WEIGHT_EXTRABOLD,
            color=T.TEXT_PRIMARY,
            line_height="1.1",
            max_width="700px",
            margin_bottom=T.SPACE_6,
        ),
        
        # Problem / Solution (Subheadline)
        rx.text(
            t("¿Cansado de cursos aburridos que nunca terminas? SKILLOGIC combina lecciones prácticas, ", "Tired of boring courses you never finish? SKILLOGIC combines practical lessons, "),
            t("katas interactivos y gamificación para que programar sea tu nueva adicción.", "interactive katas, and gamification to make coding your new addiction."),
            font_size=T.TEXT_LG,
            color=T.TEXT_SECONDARY,
            max_width="600px",
            margin_bottom=T.SPACE_8,
            line_height="1.5",
        ),
        
        # CTA
        # CTA
        rx.flex(
            rx.button(
                rx.icon(tag="rocket", size=18),
                rx.text(t("Crear cuenta gratuita", "Create free account")),
                on_click=rx.redirect("/register"),
                size="4",
                variant="solid",
                style={
                    "background_color": f"{T.BRAND} !important",
                    "color": "white !important",
                },
                border_radius=T.RADIUS_LG,
                box_shadow=f"0 10px 25px -5px {T.BRAND_MEDIUM}",
                _hover={"transform": "translateY(-2px)", "box_shadow": f"0 15px 30px -5px {T.BRAND_MEDIUM}"},
                transition=f"all {T.EASE_BASE}",
                padding=f"{T.SPACE_4} {T.SPACE_6}",
                font_weight=T.WEIGHT_BOLD,
                font_size=T.TEXT_LG,
                gap=T.SPACE_2,
                width=rx.breakpoints(initial="100%", sm="auto"),
            ),

            gap=T.SPACE_4,
            direction=rx.breakpoints(initial="column", sm="row"),
            align="center",
        ),
        
        # Social Proof / Trust markers
        rx.text(t("Únete a programadores que ya están construyendo el futuro.", "Join programmers who are already building the future."), font_size=T.TEXT_SM, color=T.TEXT_MUTED, margin_top=T.SPACE_8),
        
        align="start",
        justify="center",
        flex="1",
        padding_right=rx.breakpoints(initial="0", lg=T.SPACE_10),
        z_index="2",
    )

    logo_content = rx.box(
        rx.box(
            width="450px",
            height="450px",
            background="radial-gradient(circle, rgba(124, 58, 237, 0.2) 0%, transparent 70%)",
            border_radius="50%",
            position="absolute",
            top="50%",
            left="50%",
            transform="translate(-50%, -50%)",
            filter="blur(30px)",
            z_index="0"
        ),
        rx.image(
            src="/python_logo.svg",
            width="420px",
            height="420px",
            alt="Python logo",
            z_index="1",
            style={
                "animation": "pythonFloat 6s ease-in-out infinite",
                "filter": "drop-shadow(0 30px 40px rgba(0,0,0,0.5))"
            }
        ),
        position="relative",
        display=rx.breakpoints(initial="none", lg="flex"),
        align_items="center",
        justify_content="center",
        flex="1",
        z_index="1",
    )

    background_orbs = rx.box(
        rx.box(
            position="absolute", top="-10%", left="-5%", width="400px", height="400px",
            background="radial-gradient(circle, rgba(168, 85, 247, 0.15) 0%, transparent 70%)",
            filter="blur(60px)", border_radius="50%",
        ),
        rx.box(
            position="absolute", bottom="-10%", right="20%", width="500px", height="500px",
            background="radial-gradient(circle, rgba(56, 189, 248, 0.1) 0%, transparent 70%)",
            filter="blur(60px)", border_radius="50%",
        ),
        position="absolute", top="0", left="0", right="0", bottom="0", z_index="0", overflow="hidden", pointer_events="none"
    )

    return rx.box(
        background_orbs,
        rx.flex(
            text_content,
            logo_content,
            direction=rx.breakpoints(initial="column", lg="row"),
            align="center",
            justify="between",
            max_width="1200px",
            margin="0 auto",
            padding=f"{T.SPACE_16} {T.SPACE_8}",
            position="relative",
            z_index="1"
        ),
        position="relative",
        width="100%",
        overflow="hidden"
    )

