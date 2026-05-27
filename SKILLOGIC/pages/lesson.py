import reflex as rx
from SKILLOGIC.state.lesson_state import LessonState
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
                rx.text(
                    LessonState.phase_data["content"], 
                    font_size="lg", 
                    line_height="1.6",
                    white_space="pre-wrap"
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
                            lambda block: rx.card(
                                rx.hstack(
                                    rx.text(block["text"], width="100%"),
                                    rx.vstack(
                                        rx.icon_button(
                                            rx.icon("chevron-up"),
                                            on_click=lambda: LessonState.move_block_up(block["id"]),
                                            size="1",
                                            variant="ghost",
                                        ),
                                        rx.icon_button(
                                            rx.icon("chevron-down"),
                                            on_click=lambda: LessonState.move_block_down(block["id"]),
                                            size="1",
                                            variant="ghost",
                                        ),
                                        spacing="0",
                                    ),
                                    align="center",
                                    width="100%"
                                ),
                                width="100%",
                                margin_bottom=T.SPACE_2
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
                "Atrás", 
                on_click=LessonState.prev_phase,
                disabled=LessonState.current_phase_index == 0,
                variant="outline"
            ),
            rx.spacer(),
            rx.cond(
                LessonState.current_phase_index == 6,
                rx.button(
                    "Terminar Lección",
                    on_click=LessonState.finish_lesson,
                    disabled=~LessonState.can_advance,
                    color_scheme="green"
                ),
                rx.button(
                    "Siguiente", 
                    on_click=LessonState.next_phase,
                    disabled=~LessonState.can_advance,
                    color_scheme="purple"
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
                # Code Editor
                rx.box(
                    rx.text_area(
                        value=LessonState.user_code,
                        on_change=LessonState.set_user_code,
                        height="45vh",
                        width="100%",
                        font_family="monospace",
                        font_size="md",
                        background="#1e1e1e",
                        color="#d4d4d4",
                        padding=T.SPACE_4,
                        border="none",
                        border_radius=T.RADIUS_MD,
                    ),
                    width="100%",
                    position="relative"
                ),
                
                # Run Button
                rx.button(
                    rx.icon("play"),
                    "Run Code",
                    on_click=LessonState.run_code,
                    color_scheme="green",
                    size="3",
                    margin_top=T.SPACE_2,
                    align_self="flex-end"
                ),
                
                # Terminal
                rx.box(
                    rx.text(
                        LessonState.terminal_output,
                        font_family="monospace",
                        color=rx.cond(LessonState.is_success, "green", "red"),
                        white_space="pre-wrap"
                    ),
                    rx.cond(
                        LessonState.feedback_message != "",
                        rx.box(
                            rx.divider(margin_y=T.SPACE_2),
                            rx.text("SKILLOGIC Feedback:", font_weight="bold", color="orange"),
                            rx.text(LessonState.feedback_message, color="orange"),
                        )
                    ),
                    background="#000000",
                    width="100%",
                    height="40vh",
                    padding=T.SPACE_4,
                    border_radius=T.RADIUS_MD,
                    overflow_y="auto",
                    margin_top=T.SPACE_2
                ),
                width="100%",
                height="100%"
            ),
            # Empty state for non-code phases
            rx.center(
                rx.icon("code", size=64, color=T.TEXT_MUTED, opacity="0.3"),
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

    # Split Pane
    content = rx.hstack(
        rx.box(
            render_content(),
            width="40%",
            height="100%"
        ),
        rx.box(
            render_workspace(),
            width="60%",
            height="100%"
        ),
        width="100%",
        height=f"calc(100vh - {T.TOPBAR_HEIGHT})",
        align="stretch",
        spacing="0" # Ensure no gap between panels
    )
    
    return rx.box(
        topbar,
        content,
        width="100vw",
        height="100vh",
        background=T.BG_PRIMARY,
        color=T.TEXT_PRIMARY
    )
