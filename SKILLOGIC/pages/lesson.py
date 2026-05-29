import reflex as rx
from SKILLOGIC.state.lesson_state import LessonState
from SKILLOGIC.state.app_state import AppState
import SKILLOGIC.styles.theme as T

def render_content() -> rx.Component:
    """Renders the left panel content based on phase type."""
    return rx.box(
        # Phase header
        rx.hstack(
            rx.badge(
                LessonState.current_phase_key,
                color_scheme="purple",
                size="3"
            ),
            rx.spacer(),
            rx.text(f"Fase {LessonState.current_phase_index + 1} de 7", color=T.TEXT_MUTED, font_size="sm"),
            width="100%",
            margin_bottom=T.SPACE_4,
        ),
        
        # Content based on type
        rx.match(
            LessonState.phase_data["type"],
            ("text", 
                rx.markdown(
                    LessonState.phase_data["content"],
                    # custom styles for markdown
                    component_map={
                        "p": lambda text: rx.text(text, font_size="lg", line_height="1.7", margin_bottom=T.SPACE_4, color=T.TEXT_SECONDARY),
                        "strong": lambda text: rx.text(text, as_="b", font_weight="bold", color=T.TEXT_PRIMARY),
                        "code": lambda text: rx.code(text, color=T.BRAND, background=T.BG_ELEVATED, padding="0.1em 0.3em", border_radius="4px", border=f"1px solid {T.BORDER_SUBTLE}", font_weight="bold"),
                    }
                )
            ),
            ("code", 
                rx.box(
                    rx.text(
                        LessonState.phase_data["statement"],
                        font_size="lg",
                        margin_bottom=T.SPACE_4,
                        white_space="pre-wrap"
                    ),
                    rx.cond(
                        LessonState.current_phase_key == "4_guided_build",
                        rx.callout(
                            "Llena los espacios en blanco (____) en el editor de la derecha.",
                            icon="info",
                            color_scheme="blue"
                        )
                    )
                )
            ),
            ("parsons",
                rx.box(
                    rx.text(
                        "Desafío: Ordena estos pasos lógicos arrastrándolos o leyéndolos para entender el flujo.",
                        font_size="lg", margin_bottom=T.SPACE_4
                    ),
                    # Simple MVP for Parsons: Display them in order and ask user to type the order 
                    # OR we could just display them scrambled. Since true drag&drop in pure reflex needs custom components,
                    # we will show the blocks scrambled, and have input fields to order them, OR just a button to reveal solution.
                    # For now, let's just show them as a list.
                    rx.vstack(
                        rx.foreach(
                            LessonState.parsons_blocks,
                            lambda block: rx.box(
                                rx.hstack(
                                    rx.icon("grip-vertical", color=T.TEXT_MUTED, size=16),
                                    rx.text(block["text"], width="100%", font_family="monospace", font_size="sm"),
                                    rx.vstack(
                                        rx.icon_button(
                                            rx.icon("chevron-up"),
                                            on_click=lambda: LessonState.move_block_up(block["id"]),
                                            size="1",
                                            variant="ghost",
                                            color_scheme="gray",
                                            cursor="pointer"
                                        ),
                                        rx.icon_button(
                                            rx.icon("chevron-down"),
                                            on_click=lambda: LessonState.move_block_down(block["id"]),
                                            size="1",
                                            variant="ghost",
                                            color_scheme="gray",
                                            cursor="pointer"
                                        ),
                                        spacing="0",
                                    ),
                                    align="center",
                                    width="100%",
                                    gap="3"
                                ),
                                width="100%",
                                margin_bottom=T.SPACE_2,
                                padding=T.SPACE_3,
                                background=T.BG_SECONDARY,
                                border=f"1px solid {T.BORDER}",
                                border_radius=T.RADIUS_MD,
                                box_shadow=T.SHADOW_SM,
                                _hover={"border_color": T.BRAND, "transform": "translateY(-1px)"},
                                transition=f"all {T.EASE_FAST}"
                            )
                        ),
                        rx.button("Comprobar respuesta", on_click=LessonState.check_parsons, margin_top=T.SPACE_4),
                        rx.cond(
                            LessonState.feedback_message != "",
                            rx.callout(
                                LessonState.feedback_message,
                                icon=rx.cond(LessonState.is_success, "check", "info"),
                                color_scheme=rx.cond(LessonState.is_success, "green", "orange"),
                                margin_top=T.SPACE_2,
                                width="100%"
                            )
                        )
                    )
                )
            ),
            rx.text("Contenido no soportado.")
        ),
        
        # Navigation
        rx.hstack(
            rx.button(
                rx.icon("arrow-left", size=16),
                "Atrás", 
                on_click=LessonState.prev_phase,
                disabled=LessonState.current_phase_index == 0,
                variant="outline",
                color_scheme="gray",
                size="3",
                cursor="pointer",
                background=T.BG_ELEVATED,
                color=T.TEXT_PRIMARY,
                box_shadow=T.SHADOW_SM,
                _hover={"background": T.BG_HOVER}
            ),
            rx.spacer(),
            rx.cond(
                LessonState.current_phase_index == 6,
                rx.button(
                    "Completar",
                    rx.icon("check", size=16),
                    on_click=LessonState.finish_lesson,
                    disabled=~LessonState.can_advance,
                    color_scheme="green",
                    size="3",
                    cursor="pointer",
                    box_shadow=T.SHADOW_MD
                ),
                rx.button(
                    "Siguiente", 
                    rx.icon("arrow-right", size=16),
                    on_click=LessonState.next_phase,
                    disabled=~LessonState.can_advance,
                    color_scheme="purple",
                    size="3",
                    cursor="pointer",
                    box_shadow=f"0 4px 10px {T.BRAND_LIGHT}",
                    _hover={"transform": "translateY(-1px)", "box_shadow": f"0 6px 15px {T.BRAND_MEDIUM}"}
                )
            ),
            margin_top=T.SPACE_8,
            width="100%"
        ),
        
        padding=T.SPACE_8,
        height="100%",
        overflow_y="auto"
    )

def render_workspace() -> rx.Component:
    """Renders the right panel code editor and terminal."""
    return rx.box(
        rx.cond(
            LessonState.phase_data["type"] == "code",
            rx.vstack(
                # Code Editor with MacOS style window
                rx.box(
                    # Window header
                    rx.hstack(
                        rx.hstack(
                            rx.box(width="12px", height="12px", border_radius="50%", background="#ff5f56"),
                            rx.box(width="12px", height="12px", border_radius="50%", background="#ffbd2e"),
                            rx.box(width="12px", height="12px", border_radius="50%", background="#27c93f"),
                            spacing="2"
                        ),
                        rx.text("main.py", color="#858585", font_size="12px", font_family="monospace"),
                        rx.box(width="48px"), # Spacer balancer
                        justify="between",
                        padding=f"{T.SPACE_2} {T.SPACE_4}",
                        background="#2d2d2d",
                        border_top_radius=T.RADIUS_MD,
                        align="center"
                    ),
                    rx.text_area(
                        value=LessonState.user_code,
                        on_change=LessonState.set_user_code,
                        height="45vh",
                        width="100%",
                        font_family="'Fira Code', 'Consolas', monospace",
                        font_size="md",
                        background="#1e1e1e",
                        color="#d4d4d4",
                        padding=T.SPACE_4,
                        border="none",
                        border_radius="0",
                        border_bottom_radius=T.RADIUS_MD,
                        _focus={"outline": "none", "box_shadow": f"inset 0 0 0 1px {T.BRAND}"}
                    ),
                    width="100%",
                    box_shadow=T.SHADOW_LG,
                    border_radius=T.RADIUS_MD,
                    margin_bottom=T.SPACE_4
                ),
                
                # Run Button
                rx.button(
                    rx.icon("play", size=18),
                    "Ejecutar Código",
                    on_click=LessonState.run_code,
                    color_scheme="green",
                    size="3",
                    align_self="flex-end",
                    cursor="pointer",
                    box_shadow=f"0 4px 14px 0 rgba(34, 197, 94, 0.39)",
                    _hover={"transform": "translateY(-1px)", "box_shadow": f"0 6px 20px rgba(34, 197, 94, 0.23)"},
                    transition="all 0.2s ease"
                ),
                
                # Terminal
                rx.box(
                    rx.text("TERMINAL", color="#555", font_size="10px", font_weight="bold", margin_bottom=T.SPACE_2, letter_spacing="1px"),
                    rx.text(
                        LessonState.terminal_output,
                        font_family="'Fira Code', 'Consolas', monospace",
                        color=rx.cond(LessonState.is_success, "#4ade80", "#f87171"),
                        white_space="pre-wrap",
                        text_shadow=rx.cond(LessonState.is_success, "0 0 5px rgba(74, 222, 128, 0.5)", "0 0 5px rgba(248, 113, 113, 0.5)")
                    ),
                    rx.cond(
                        LessonState.feedback_message != "",
                        rx.box(
                            rx.divider(margin_y=T.SPACE_3, border_color="#333"),
                            rx.hstack(
                                rx.icon("zap", color="#fbbf24", size=16),
                                rx.text("SKILLOGIC AI:", font_weight="bold", color="#fbbf24", font_family="monospace"),
                                align="center", margin_bottom=T.SPACE_1
                            ),
                            rx.text(LessonState.feedback_message, color="#fef3c7", font_family="monospace"),
                        )
                    ),
                    background="#0f172a", # Slate 900
                    width="100%",
                    height="35vh",
                    padding=T.SPACE_5,
                    border_radius=T.RADIUS_MD,
                    border="1px solid #1e293b",
                    box_shadow="inset 0 2px 10px rgba(0,0,0,0.5)",
                    overflow_y="auto",
                    margin_top=T.SPACE_4
                ),
                width="100%",
                height="100%"
            ),
            # Empty state for non-code phases
            rx.center(
                rx.vstack(
                    rx.box(
                        rx.icon("brain-circuit", size=48, color=T.BRAND),
                        padding=T.SPACE_4,
                        background=f"rgba(124, 58, 237, 0.1)",
                        border_radius="50%",
                        margin_bottom=T.SPACE_4,
                        box_shadow=f"0 0 20px rgba(124, 58, 237, 0.3)"
                    ),
                    rx.text("Modo Lectura / Reto Lógico", font_weight="bold", font_size="lg", color=T.TEXT_PRIMARY),
                    rx.text("Concéntrate en el panel izquierdo para aprender la teoría antes de codificar.", color=T.TEXT_MUTED, text_align="center", max_width="300px"),
                    align_items="center"
                ),
                height="100%"
            )
        ),
        padding=T.SPACE_8,
        background=T.BG_SECONDARY,
        border_left=f"1px solid {T.BORDER}",
        height="100%",
        overflow_y="auto"
    )

from SKILLOGIC.state.auth_state import AuthState

@rx.page(route="/lesson/[lesson_id]", on_load=[AuthState.on_load, LessonState.load_lesson])
def lesson_page() -> rx.Component:
    """Main lesson page with split-pane layout."""
    
    # Deep Focus Topbar
    topbar = rx.hstack(
        # Progress on the left
        rx.hstack(
            rx.progress(value=LessonState.progress_percent, width="150px", color_scheme="purple"),
            rx.text(f"{LessonState.progress_percent}%", color=T.TEXT_SECONDARY, font_size="sm", font_weight="bold"),
            align="center",
            width="250px"
        ),
        rx.spacer(),
        # Title in the center
        rx.text("Lección: Cómo piensa una computadora", font_weight="bold"),
        rx.spacer(),
        # Save and Exit on the right
        rx.box(
            rx.hstack(
                rx.icon("save", size=16),
                rx.text("Guardar y Salir"),
                align="center",
                spacing="2"
            ),
            on_click=LessonState.save_and_exit,
            cursor="pointer",
            color=T.TEXT_PRIMARY,
            background=T.BG_ELEVATED,
            padding=f"{T.SPACE_2} {T.SPACE_4}",
            border_radius=T.RADIUS_MD,
            border=f"1px solid {T.BORDER}",
            _hover={"background": T.BG_HOVER, "color": T.BRAND_LIGHT},
            width="250px",
            display="flex",
            justify_content="flex-end"
        ),
        padding=f"{T.SPACE_4} {T.SPACE_8}",
        border_bottom=f"1px solid {T.BORDER}",
        background=T.BG_PRIMARY,
        width="100%",
        height=T.TOPBAR_HEIGHT,
        align="center"
    )

    # Split Pane (Vertical on mobile, Horizontal on desktop)
    content = rx.flex(
        rx.box(
            render_content(),
            width=["100%", "100%", "40%"],
            min_height=["50vh", "50vh", "100%"]
        ),
        rx.box(
            render_workspace(),
            width=["100%", "100%", "60%"],
            min_height=["50vh", "50vh", "100%"]
        ),
        width="100%",
        height=["auto", "auto", f"calc(100vh - {T.TOPBAR_HEIGHT})"],
        direction=["column", "column", "row"],
        align="stretch",
        spacing="0" # Ensure no gap between panels
    )
    
    return rx.box(
        topbar,
        content,
        width="100vw",
        min_height="100vh",
        background=T.BG_PRIMARY,
        color=T.TEXT_PRIMARY,
        data_theme=AppState.theme
    )
