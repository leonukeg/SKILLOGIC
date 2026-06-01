import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState

def landing_navbar() -> rx.Component:
    """Navbar for the landing page."""
    return rx.hstack(
        # Logo
        rx.hstack(
            rx.box(
                rx.icon(tag="zap", size=18, color="white"),
                width="36px", height="36px",
                background=f"linear-gradient(135deg, {T.BRAND}, #a855f7)",
                border_radius=T.RADIUS_MD,
                display="flex", align_items="center", justify_content="center",
                box_shadow=T.SHADOW_BRAND,
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
        rx.spacer(),
        # Auth Buttons
        rx.hstack(
            rx.button(
                "Iniciar sesión",
                on_click=rx.redirect("/login"),
                background="transparent",
                color=T.TEXT_SECONDARY,
                _hover={"color": T.TEXT_PRIMARY},
                font_weight=T.WEIGHT_SEMIBOLD,
            ),
            rx.button(
                "Comenzar gratis",
                on_click=rx.redirect("/register"),
                background=T.BRAND,
                color="white",
                border_radius=T.RADIUS_MD,
                box_shadow=T.SHADOW_BRAND,
                _hover={"background": T.BRAND_HOVER},
                font_weight=T.WEIGHT_SEMIBOLD,
                padding=f"{T.SPACE_2} {T.SPACE_4}",
            ),
            gap=T.SPACE_4,
        ),
        width="100%",
        padding=f"{T.SPACE_4} {T.SPACE_8}",
        max_width="1200px",
        margin="0 auto",
        align="center",
    )

def hero_section() -> rx.Component:
    """Hero section following PAS/AIDA marketing formulas with floating python logo."""
    
    text_content = rx.vstack(
        # Pill badge
        rx.hstack(
            rx.icon(tag="sparkles", size=14, color="#F59E0B"),
            rx.text("La nueva forma de dominar Python", font_size=T.TEXT_SM, font_weight=T.WEIGHT_SEMIBOLD, color=T.ACCENT_LILAC),
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
            "Aprende Python escribiendo ",
            rx.text.span("código real", color="transparent", background_image=f"linear-gradient(90deg, {T.BRAND}, #a855f7)", background_clip="text", webkit_background_clip="text"),
            ", no solo leyendo tutoriales.",
            font_size=rx.breakpoints(initial="2.5rem", md="3.5rem", lg="4rem"),
            font_weight=T.WEIGHT_EXTRABOLD,
            color=T.TEXT_PRIMARY,
            line_height="1.1",
            max_width="700px",
            margin_bottom=T.SPACE_6,
        ),
        
        # Problem / Solution (Subheadline)
        rx.text(
            "¿Cansado de cursos aburridos que nunca terminas? SKILLOGIC combina lecciones prácticas, ",
            "katas interactivos y gamificación para que programar sea tu nueva adicción.",
            font_size=T.TEXT_LG,
            color=T.TEXT_SECONDARY,
            max_width="600px",
            margin_bottom=T.SPACE_8,
            line_height="1.5",
        ),
        
        # CTA
        rx.hstack(
            rx.button(
                rx.icon(tag="rocket", size=18),
                rx.text("Crear cuenta gratuita"),
                on_click=rx.redirect("/register"),
                size="4",
                background=T.BRAND,
                color="white",
                border_radius=T.RADIUS_LG,
                box_shadow=f"0 10px 25px -5px {T.BRAND_MEDIUM}",
                _hover={"transform": "translateY(-2px)", "box_shadow": f"0 15px 30px -5px {T.BRAND_MEDIUM}"},
                transition=f"all {T.EASE_BASE}",
                padding=f"{T.SPACE_4} {T.SPACE_6}",
                font_weight=T.WEIGHT_BOLD,
                font_size=T.TEXT_LG,
                gap=T.SPACE_2,
            ),
            rx.button(
                rx.icon(tag="book-open", size=18),
                rx.text("Ver currículum"),
                on_click=rx.redirect("/dashboard"),
                size="4",
                background=T.BG_ELEVATED,
                color=T.TEXT_PRIMARY,
                border=f"1px solid {T.BORDER_STRONG}",
                border_radius=T.RADIUS_LG,
                _hover={"background": T.BG_HOVER},
                transition=f"all {T.EASE_BASE}",
                padding=f"{T.SPACE_4} {T.SPACE_6}",
                font_weight=T.WEIGHT_BOLD,
                font_size=T.TEXT_LG,
                gap=T.SPACE_2,
            ),
            gap=T.SPACE_4,
            flex_direction=rx.breakpoints(initial="column", md="row"),
            align_items="start"
        ),
        
        # Social Proof / Trust markers
        rx.text("Únete a programadores que ya están construyendo el futuro.", font_size=T.TEXT_SM, color=T.TEXT_MUTED, margin_top=T.SPACE_8),
        
        align="start",
        justify="center",
        flex="1",
        padding_right=rx.breakpoints(initial="0", lg=T.SPACE_10),
        z_index="2",
    )

    logo_content = rx.box(
        rx.box(
            width="350px",
            height="350px",
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
            width="320px",
            height="320px",
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

    return rx.flex(
        text_content,
        logo_content,
        direction=rx.breakpoints(initial="column", lg="row"),
        align="center",
        justify="between",
        max_width="1200px",
        margin="0 auto",
        padding=f"{T.SPACE_16} {T.SPACE_8}",
    )

def features_section() -> rx.Component:
    """Pedagogical approach breakdown."""
    def feature_card(icon: str, title: str, description: str, color: str) -> rx.Component:
        return rx.vstack(
            rx.box(
                rx.icon(tag=icon, size=24, color=color),
                padding=T.SPACE_3,
                background=f"rgba(255,255,255,0.05)",
                border_radius=T.RADIUS_LG,
                margin_bottom=T.SPACE_3,
            ),
            rx.text(title, font_size=T.TEXT_XL, font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
            rx.text(description, font_size=T.TEXT_BASE, color=T.TEXT_SECONDARY, line_height="1.5"),
            background=T.BG_ELEVATED,
            padding=T.SPACE_6,
            border_radius=T.RADIUS_XL,
            border=f"1px solid {T.BORDER}",
            transition=f"all {T.EASE_BASE}",
            _hover={"transform": "translateY(-5px)", "border_color": color, "box_shadow": f"0 10px 30px -10px {color}"},
            width="100%",
        )

    return rx.box(
        rx.vstack(
            rx.text("Metodología Comprobada", font_size=T.TEXT_SM, font_weight=T.WEIGHT_BOLD, color=T.BRAND, letter_spacing="1px", text_transform="uppercase"),
            rx.text("Cómo te convertimos en desarrollador", font_size=T.TEXT_3XL, font_weight=T.WEIGHT_EXTRABOLD, color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_8, text_align="center"),
            rx.grid(
                feature_card("book-open", "Teoría al Grano", "Sin rodeos. Conceptos explicados con analogías claras y directas para que entiendas el 'por qué' detrás del código.", T.INFO),
                feature_card("terminal", "Katas Interactivas", "Un IDE integrado en tu navegador. Resuelve problemas reales escribiendo código, con validación instantánea.", T.SUCCESS),
                feature_card("flame", "Gamificación", "Mantén tu racha de días, gana experiencia (XP) y sube de nivel. Aprender a programar ahora es tan adictivo como un juego.", "#f97316"),
                columns=rx.breakpoints(initial="1", md="3"),
                gap=T.SPACE_6,
                width="100%",
            ),
            align="center",
            max_width="1200px",
            margin="0 auto",
            padding=f"{T.SPACE_10} {T.SPACE_4}",
        )
    )

def how_it_works_section() -> rx.Component:
    """Step-by-step guide on how the platform works."""
    def step_card(number: str, title: str, desc: str) -> rx.Component:
        return rx.hstack(
            rx.box(
                rx.text(number, font_size=T.TEXT_2XL, font_weight=T.WEIGHT_EXTRABOLD, color=T.BRAND_LIGHT),
                width="60px", height="60px", border_radius="50%",
                background=f"linear-gradient(135deg, {T.BRAND}, {T.BG_ELEVATED})",
                display="flex", align_items="center", justify_content="center",
                flex_shrink="0", box_shadow=T.SHADOW_BRAND,
            ),
            rx.vstack(
                rx.text(title, font_size=T.TEXT_LG, font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
                rx.text(desc, font_size=T.TEXT_BASE, color=T.TEXT_SECONDARY, line_height="1.5"),
                spacing="1"
            ),
            background=T.BG_SECONDARY,
            padding=T.SPACE_6,
            border_radius=T.RADIUS_LG,
            border=f"1px solid {T.BORDER}",
            gap=T.SPACE_6,
            align="center",
            width="100%",
            max_width="800px",
            margin_bottom=T.SPACE_4,
            transition=f"transform {T.EASE_BASE}",
            _hover={"transform": "translateX(10px)", "border_color": T.BORDER_STRONG}
        )

    return rx.box(
        rx.vstack(
            rx.text("Tu Ruta al Éxito", font_size=T.TEXT_SM, font_weight=T.WEIGHT_BOLD, color=T.BRAND, letter_spacing="1px", text_transform="uppercase"),
            rx.text("Aprender nunca fue tan directo", font_size=T.TEXT_3XL, font_weight=T.WEIGHT_EXTRABOLD, color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_8, text_align="center"),
            
            step_card("1", "Aprende la teoría necesaria", "Nada de textos interminables. Solo el conocimiento exacto que necesitas para entender el concepto, apoyado con ejemplos de la vida real."),
            step_card("2", "Resuelve Katas en el navegador", "No necesitas instalar nada. Escribe tu código directamente en nuestro IDE en el navegador y recibe validación y feedback instantáneo."),
            step_card("3", "Construye proyectos reales", "Combina todo lo que has aprendido para construir aplicaciones que puedes mostrar en tu portafolio, no solo calculadoras de consola."),
            
            align="center",
            width="100%",
        ),
        padding=f"{T.SPACE_10} {T.SPACE_4}",
        background=T.BG_PRIMARY,
        margin_top=T.SPACE_10,
    )

def bottom_cta_section() -> rx.Component:
    """Strong bottom call to action before the footer."""
    return rx.box(
        rx.vstack(
            rx.text("¿Listo para escribir tu primera línea?", font_size=T.TEXT_3XL, font_weight=T.WEIGHT_EXTRABOLD, color="white", text_align="center", margin_bottom=T.SPACE_4),
            rx.text("Únete a SKILLOGIC hoy y transforma tu carrera aprendiendo la tecnología más demandada del mercado.", font_size=T.TEXT_LG, color="rgba(255,255,255,0.8)", text_align="center", max_width="600px", margin_bottom=T.SPACE_8),
            rx.button(
                "Comenzar mi aprendizaje gratis",
                on_click=rx.redirect("/register"),
                size="4",
                background="white",
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

def footer() -> rx.Component:
    """Simple footer for the landing page."""
    return rx.box(
        rx.hstack(
            rx.text("© 2026 SKILLOGIC. Todos los derechos reservados.", font_size=T.TEXT_SM, color=T.TEXT_MUTED),
            rx.spacer(),
            rx.hstack(
                rx.text("Términos", font_size=T.TEXT_SM, color=T.TEXT_MUTED, cursor="pointer", _hover={"color": T.TEXT_PRIMARY}),
                rx.text("Privacidad", font_size=T.TEXT_SM, color=T.TEXT_MUTED, cursor="pointer", _hover={"color": T.TEXT_PRIMARY}),
                gap=T.SPACE_4,
            ),
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding=f"{T.SPACE_6} {T.SPACE_4}",
        ),
        border_top=f"1px solid {T.BORDER_SUBTLE}",
        background=T.BG_PRIMARY,
        margin_top=T.SPACE_4,
    )

@rx.page(
    route="/",
    title="SKILLOGIC — Aprende Python de forma interactiva",
    description="Plataforma gamificada para aprender Python. Supera Katas interactivos, gana XP, mantén tu racha y domina la programación desde cero.",
    meta=[
        {"name": "keywords", "content": "python, aprender python, curso de python, programación interactiva, katas python, python desde cero, tutorial python"},
        {"property": "og:type", "content": "website"},
        {"property": "og:title", "content": "SKILLOGIC — Aprende Python de forma interactiva"},
        {"property": "og:description", "content": "Plataforma gamificada para aprender Python. Supera Katas interactivos, gana XP, mantén tu racha y domina la programación."},
        {"property": "og:site_name", "content": "SKILLOGIC"},
        {"property": "twitter:card", "content": "summary_large_image"},
        {"property": "twitter:title", "content": "SKILLOGIC — Aprende Python"},
        {"property": "twitter:description", "content": "Aprende a programar resolviendo problemas reales en tu navegador."},
    ]
)
def landing_page() -> rx.Component:
    """The main landing page composed of multiple marketing sections."""
    return rx.box(
        landing_navbar(),
        hero_section(),
        features_section(),
        how_it_works_section(),
        bottom_cta_section(),
        footer(),
        background=T.BG_PRIMARY,
        min_height="100vh",
        width="100%",
        font_family=T.FONT_BODY,
    )
