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
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.button(
                        rx.icon(tag="book-open", size=18),
                        rx.text(t("Ver currículum", "View curriculum")),
                        variant="outline",
                        style={
                            "color": f"{T.TEXT_PRIMARY} !important",
                            "border_color": f"{T.BORDER_STRONG} !important",
                        },
                        size="4",
                        border_radius=T.RADIUS_LG,
                        _hover={"background": T.BG_HOVER},
                        transition=f"all {T.EASE_BASE}",
                        padding=f"{T.SPACE_4} {T.SPACE_6}",
                        font_weight=T.WEIGHT_BOLD,
                        font_size=T.TEXT_LG,
                        gap=T.SPACE_2,
                        cursor="pointer",
                        width=rx.breakpoints(initial="100%", sm="auto"),
                    )
                ),
                rx.drawer.overlay(z_index="100", background_color="rgba(0,0,0,0.4)", backdrop_filter="blur(4px)"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="graduation-cap", size=24, color=T.BRAND_LIGHT),
                                rx.text(t("Ruta de Aprendizaje", "Learning Path"), font_size=T.TEXT_2XL, font_weight=T.WEIGHT_EXTRABOLD, color="white"),
                                align="center",
                                gap="3",
                                margin_bottom=T.SPACE_6,
                                padding_bottom=T.SPACE_4,
                                border_bottom=f"1px solid {T.BORDER_SUBTLE}",
                                width="100%",
                            ),
                            rx.scroll_area(
                                rx.vstack(
                                    rx.box(
                                        rx.vstack(
                                            rx.text(t("Módulo 1: Fundamentos", "Module 1: Fundamentals"), font_size=T.TEXT_LG, font_weight=T.WEIGHT_BOLD, color=T.ACCENT_LILAC),
                                            rx.text(t("Variables, tipos de datos y operadores lógicos. Tu primer paso en Python.", "Variables, data types, and logical operators. Your first step in Python."), font_size=T.TEXT_SM, color=T.TEXT_SECONDARY, line_height="1.5"),
                                        ),
                                        margin_bottom=T.SPACE_6,
                                    ),
                                    rx.box(
                                        rx.vstack(
                                            rx.text(t("Módulo 2: Estructuras de Control", "Module 2: Control Structures"), font_size=T.TEXT_LG, font_weight=T.WEIGHT_BOLD, color=T.ACCENT_LILAC),
                                            rx.text(t("Condicionales (if/else) y bucles (for/while). Domina el flujo de tu código.", "Conditionals (if/else) and loops (for/while). Master the flow of your code."), font_size=T.TEXT_SM, color=T.TEXT_SECONDARY, line_height="1.5"),
                                        ),
                                        margin_bottom=T.SPACE_6,
                                    ),
                                    rx.box(
                                        rx.vstack(
                                            rx.text(t("Módulo 3: Colecciones de Datos", "Module 3: Data Collections"), font_size=T.TEXT_LG, font_weight=T.WEIGHT_BOLD, color=T.ACCENT_LILAC),
                                            rx.text(t("Listas, diccionarios, tuplas y sets. Organiza y manipula información masiva.", "Lists, dictionaries, tuples, and sets. Organize and manipulate massive information."), font_size=T.TEXT_SM, color=T.TEXT_SECONDARY, line_height="1.5"),
                                        ),
                                        margin_bottom=T.SPACE_6,
                                    ),
                                    rx.box(
                                        rx.vstack(
                                            rx.text(t("Módulo 4: Funciones y Modularidad", "Module 4: Functions & Modularity"), font_size=T.TEXT_LG, font_weight=T.WEIGHT_BOLD, color=T.ACCENT_LILAC),
                                            rx.text(t("Crea código reutilizable y elegante. Aprende el principio DRY (Don't Repeat Yourself).", "Create reusable and elegant code. Learn the DRY (Don't Repeat Yourself) principle."), font_size=T.TEXT_SM, color=T.TEXT_SECONDARY, line_height="1.5"),
                                        ),
                                        margin_bottom=T.SPACE_6,
                                    ),
                                    rx.box(
                                        rx.vstack(
                                            rx.text(t("Módulo 5: Programación Orientada a Objetos", "Module 5: Object-Oriented Programming"), font_size=T.TEXT_LG, font_weight=T.WEIGHT_BOLD, color=T.ACCENT_LILAC),
                                            rx.text(t("Clases, objetos, herencia y polimorfismo. El paradigma de la industria.", "Classes, objects, inheritance, and polymorphism. The industry paradigm."), font_size=T.TEXT_SM, color=T.TEXT_SECONDARY, line_height="1.5"),
                                        ),
                                        margin_bottom=T.SPACE_8,
                                    ),
                                    width="100%",
                                    align_items="start",
                                ),
                                type="scroll",
                            ),
                            rx.button(
                                t("¡Quiero aprender todo esto!", "I want to learn all this!"),
                                on_click=rx.redirect("/register"),
                                width="100%",
                                size="4",
                                background=T.BRAND,
                                color="white",
                                margin_top="auto",
                                box_shadow=T.SHADOW_BRAND,
                                _hover={"background": T.BRAND_HOVER},
                            ),
                            height="100%",
                            padding=T.SPACE_6,
                            background=T.BG_PRIMARY,
                            border_radius=T.RADIUS_XL,
                            border=f"1px solid {T.BORDER}",
                        ),
                        top="16px",
                        bottom="16px",
                        right="16px",
                        left="auto",
                        position="fixed",
                        width=rx.breakpoints(initial="calc(100% - 32px)", sm="400px"),
                        background="transparent",
                        z_index="101",
                        border_radius=T.RADIUS_XL,
                        box_shadow=f"-10px 10px 40px rgba(0,0,0,0.5)",
                        outline="none",
                    )
                ),
                direction="right",
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

