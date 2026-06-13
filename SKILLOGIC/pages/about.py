import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.components.landing.navbar import landing_navbar
from SKILLOGIC.components.landing.footer import footer
from SKILLOGIC.components.landing.cta import bottom_cta_section

def _pas_section() -> rx.Component:
    """Problem -> Agitate -> Solution marketing section."""
    return rx.box(
        rx.vstack(
            rx.heading("El problema de aprender a programar hoy", size="7", color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_4, text_align="center"),
            
            rx.grid(
                # Problem
                rx.box(
                    rx.icon("monitor-off", size=32, color=T.ERROR),
                    rx.heading("El Infierno de los Tutoriales", size="5", color=T.TEXT_PRIMARY, margin_y=T.SPACE_3),
                    rx.text("Pasas 10 horas viendo videos en YouTube. Sientes que entiendes todo. Pero cuando abres un editor de código en blanco, tu mente se queda en blanco. Leer código no es lo mismo que escribirlo.", color=T.TEXT_SECONDARY),
                    background=T.BG_ELEVATED,
                    padding=T.SPACE_6,
                    border_radius=T.RADIUS_LG,
                    border=f"1px solid {T.BORDER}",
                ),
                # Agitate
                rx.box(
                    rx.icon("trending-down", size=32, color=T.WARNING),
                    rx.heading("Falsa Sensación de Progreso", size="5", color=T.TEXT_PRIMARY, margin_y=T.SPACE_3),
                    rx.text("Copiar y pegar código de instructores crea una falsa ilusión de conocimiento. Sin enfrentarte a errores reales de sintaxis, nunca desarrollas la memoria muscular necesaria para una entrevista técnica.", color=T.TEXT_SECONDARY),
                    background=T.BG_ELEVATED,
                    padding=T.SPACE_6,
                    border_radius=T.RADIUS_LG,
                    border=f"1px solid {T.BORDER}",
                ),
                # Solution
                rx.box(
                    rx.icon("rocket", size=32, color=T.SUCCESS),
                    rx.heading("La Solución: Práctica Activa", size="5", color=T.TEXT_PRIMARY, margin_y=T.SPACE_3),
                    rx.text("SKILLOGIC invierte la ecuación. 90% del tiempo estás escribiendo código en tu navegador y 10% leyendo teoría. Aprendes rompiendo cosas, arreglándolas y superando retos lógicos reales.", color=T.TEXT_SECONDARY),
                    background=T.BG_ELEVATED,
                    padding=T.SPACE_6,
                    border_radius=T.RADIUS_LG,
                    border=f"1px solid {T.BRAND_LIGHT}",
                    box_shadow=f"0 0 20px {T.BRAND_GLOW}",
                ),
                columns=rx.breakpoints(initial="1", md="3"),
                gap=T.SPACE_6,
                width="100%",
                margin_top=T.SPACE_8,
            ),
        ),
        width="100%",
        max_width="1200px",
        margin="0 auto",
        padding=f"{T.SPACE_16} {T.SPACE_4}",
    )

def _fab_section() -> rx.Component:
    """Feature -> Advantage -> Benefit section."""
    return rx.box(
        rx.vstack(
            rx.heading("¿Por qué elegir SKILLOGIC?", size="7", color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_8, text_align="center"),
            
            rx.vstack(
                rx.flex(
                    rx.box(
                        rx.icon("terminal", size=48, color=T.BRAND),
                        background=T.BRAND_LIGHT,
                        padding=T.SPACE_4,
                        border_radius=T.RADIUS_LG,
                        flex_shrink="0",
                    ),
                    rx.vstack(
                        rx.text("FEATURE", color=T.BRAND, font_size=T.TEXT_SM, font_weight=T.WEIGHT_BOLD, letter_spacing="1px"),
                        rx.heading("Consola de Python 100% en el navegador", size="5"),
                        rx.text("Ejecuta código Python real sin instalar nada. Escribe tu algoritmo y SKILLOGIC lo evalúa en milisegundos contra pruebas unitarias ocultas.", color=T.TEXT_SECONDARY),
                        align_items="start",
                    ),
                    direction=rx.breakpoints(initial="column", sm="row"),
                    gap=T.SPACE_6,
                    align="center",
                ),
                rx.divider(margin_y=T.SPACE_6),
                
                rx.flex(
                    rx.box(
                        rx.icon("swords", size=48, color=T.WARNING),
                        background=T.WARNING_LIGHT,
                        padding=T.SPACE_4,
                        border_radius=T.RADIUS_LG,
                        flex_shrink="0",
                    ),
                    rx.vstack(
                        rx.text("ADVANTAGE", color=T.WARNING, font_size=T.TEXT_SM, font_weight=T.WEIGHT_BOLD, letter_spacing="1px"),
                        rx.heading("Katas de Dificultad Real", size="5"),
                        rx.text("Nuestros retos están diseñados basándose en preguntas reales de entrevistas FAANG. Empiezas con sumas básicas y terminas implementando algoritmos de grafos y recursión profunda.", color=T.TEXT_SECONDARY),
                        align_items="start",
                    ),
                    direction=rx.breakpoints(initial="column", sm="row"),
                    gap=T.SPACE_6,
                    align="center",
                ),
                rx.divider(margin_y=T.SPACE_6),
                
                rx.flex(
                    rx.box(
                        rx.icon("gamepad-2", size=48, color=T.SUCCESS),
                        background=T.SUCCESS_LIGHT,
                        padding=T.SPACE_4,
                        border_radius=T.RADIUS_LG,
                        flex_shrink="0",
                    ),
                    rx.vstack(
                        rx.text("BENEFIT", color=T.SUCCESS, font_size=T.TEXT_SM, font_weight=T.WEIGHT_BOLD, letter_spacing="1px"),
                        rx.heading("Adicción al Progreso", size="5"),
                        rx.text("La gamificación (experiencia, rangos, rachas de días) hackea la dopamina de tu cerebro para que quieras seguir programando todos los días. Construirás disciplina sin darte cuenta.", color=T.TEXT_SECONDARY),
                        align_items="start",
                    ),
                    direction=rx.breakpoints(initial="column", sm="row"),
                    gap=T.SPACE_6,
                    align="center",
                ),
                
                width="100%",
                max_width="800px",
                background=T.BG_SECONDARY,
                padding=T.SPACE_8,
                border_radius=T.RADIUS_XL,
                border=f"1px solid {T.BORDER}",
            ),
        ),
        width="100%",
        padding=f"{T.SPACE_8} {T.SPACE_4}",
        display="flex",
        flex_direction="column",
        align_items="center",
    )

@rx.page(route="/about", title="Qué es SKILLOGIC | Aprende Python Activamente")
def about_page() -> rx.Component:
    return rx.box(
        landing_navbar(),
        
        # Hero Header
        rx.box(
            rx.vstack(
                rx.text("NUESTRA MISIÓN", color=T.BRAND, font_weight=T.WEIGHT_EXTRABOLD, letter_spacing="2px"),
                rx.heading("Forjando Programadores.", size="9", text_align="center", margin_bottom=T.SPACE_4, 
                          background=f"linear-gradient(90deg, {T.TEXT_PRIMARY}, {T.BRAND})", 
                          background_clip="text", style={"-webkit-text-fill-color": "transparent"}),
                rx.text("Construimos SKILLOGIC porque la educación tradicional en programación está rota. Creemos en el aprendizaje activo, la práctica intensa y la gamificación como motores del éxito.", 
                        color=T.TEXT_SECONDARY, font_size=T.TEXT_XL, text_align="center", max_width="800px"),
                align_items="center",
                padding=f"{T.SPACE_16} {T.SPACE_4}",
                padding_top="120px",
            ),
            background=f"radial-gradient(circle at center, {T.BRAND_LIGHT} 0%, {T.BG_PRIMARY} 70%)",
            width="100%",
        ),
        
        _pas_section(),
        _fab_section(),
        bottom_cta_section(),
        footer(),
        
        background=T.BG_PRIMARY,
        min_height="100vh",
        width="100%",
        font_family=T.FONT_BODY,
    )
