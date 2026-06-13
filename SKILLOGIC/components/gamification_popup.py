import reflex as rx
from SKILLOGIC.state.progress_state import ProgressState
from SKILLOGIC.styles import theme as T

SNAKE_CSS = """
<style>
.snake-top {
    position: absolute; top: 0; left: 0; width: 40px; height: 6px;
    background: #4ade80; box-shadow: 0 0 10px #4ade80, 0 0 20px #4ade80;
    animation: snake-top 1.5s linear infinite;
}
.snake-right {
    position: absolute; top: 0; right: 0; width: 6px; height: 40px;
    background: #4ade80; box-shadow: 0 0 10px #4ade80, 0 0 20px #4ade80;
    animation: snake-right 1.5s linear infinite;
}
.snake-bottom {
    position: absolute; bottom: 0; right: 0; width: 40px; height: 6px;
    background: #4ade80; box-shadow: 0 0 10px #4ade80, 0 0 20px #4ade80;
    animation: snake-bottom 1.5s linear infinite;
}
.snake-left {
    position: absolute; bottom: 0; left: 0; width: 6px; height: 40px;
    background: #4ade80; box-shadow: 0 0 10px #4ade80, 0 0 20px #4ade80;
    animation: snake-left 1.5s linear infinite;
}

@keyframes snake-top {
  0% { left: -40px; opacity: 1; }
  25% { left: 100%; opacity: 1; }
  25.01% { opacity: 0; }
  100% { opacity: 0; }
}
@keyframes snake-right {
  0% { opacity: 0; }
  24.99% { top: -40px; opacity: 0; }
  25% { top: -40px; opacity: 1; }
  50% { top: 100%; opacity: 1; }
  50.01% { opacity: 0; }
  100% { opacity: 0; }
}
@keyframes snake-bottom {
  0% { opacity: 0; }
  49.99% { right: -40px; opacity: 0; }
  50% { right: -40px; opacity: 1; }
  75% { right: 100%; opacity: 1; }
  75.01% { opacity: 0; }
  100% { opacity: 0; }
}
@keyframes snake-left {
  0% { opacity: 0; }
  74.99% { bottom: -40px; opacity: 0; }
  75% { bottom: -40px; opacity: 1; }
  100% { bottom: 100%; opacity: 1; }
}
</style>
"""

def gamification_popup() -> rx.Component:
    """Popup de logro/gamificación, que aparece cuando el usuario gana XP o sube de nivel."""
    return rx.cond(
        ProgressState.show_achievement,
        rx.box(
            rx.html(SNAKE_CSS),
            # Partes de la serpiente borde
            rx.box(class_name="snake-top"),
            rx.box(class_name="snake-right"),
            rx.box(class_name="snake-bottom"),
            rx.box(class_name="snake-left"),
            
            rx.vstack(
                # Texto principal
                rx.text(
                    ProgressState.achievement_message,
                    color="white",
                    font_family="'Fira Code', monospace",
                    font_weight=T.WEIGHT_BOLD,
                    font_size=rx.breakpoints(initial=T.TEXT_LG, sm=T.TEXT_XL),
                    line_height="1.2",
                    text_align="center",
                    white_space="nowrap"
                ),
                # XP
                rx.text(
                    f"+", ProgressState.achievement_xp, " XP",
                    color="#4ade80",
                    font_family="'Fira Code', monospace",
                    font_weight=T.WEIGHT_EXTRABOLD,
                    font_size=rx.breakpoints(initial="3rem", sm="4rem"),
                    line_height="1",
                    text_shadow="0 0 10px rgba(74, 222, 128, 0.3)",
                    margin_top=T.SPACE_2,
                    white_space="nowrap"
                ),
                spacing="2",
                align_items="center",
            ),
            position="fixed",
            top="50%",
            left="50%",
            transform="translate(-50%, -50%) scale(1)",
            z_index="9999",
            background="#0f172a", # Fondo oscuro estilo consola
            border="2px solid #1e293b",
            overflow="hidden", # Importante para que la serpiente no salga de las esquinas
            box_shadow="0 25px 50px -12px rgba(0, 0, 0, 0.75)",
            border_radius="16px",
            padding=rx.breakpoints(initial=f"{T.SPACE_6} {T.SPACE_6}", sm=f"{T.SPACE_8} {T.SPACE_12}"),
            min_width=rx.breakpoints(initial="80vw", sm="auto"),
            transition="all 0.4s ease-out",
        ),
        rx.fragment() # Retorna vacío si no se muestra
    )
