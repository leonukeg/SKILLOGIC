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

@keyframes trophy-bounce {
  0%, 100% { transform: scale(1) translateY(0); }
  50% { transform: scale(1.2) translateY(-10px); }
}
.trophy-anim {
    display: inline-block;
    animation: trophy-bounce 1s ease-in-out infinite;
    text-shadow: 0 0 30px rgba(250, 204, 21, 0.8);
}

/* Confetti Burst CSS */
.confetti {
    position: absolute;
    font-size: 2.5rem;
    top: 50%;
    left: 50%;
    opacity: 0;
    pointer-events: none;
    z-index: 0;
}
.c-1 { animation: burst1 1.5s ease-out infinite; }
.c-2 { animation: burst2 1.5s ease-out infinite 0.1s; }
.c-3 { animation: burst3 1.5s ease-out infinite 0.2s; }
.c-4 { animation: burst4 1.5s ease-out infinite 0.3s; }
.c-5 { animation: burst5 1.5s ease-out infinite 0.4s; }
.c-6 { animation: burst6 1.5s ease-out infinite 0.25s; }

@keyframes burst1 {
    0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
    100% { transform: translate(-300%, -300%) scale(1.5) rotate(45deg); opacity: 0; }
}
@keyframes burst2 {
    0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
    100% { transform: translate(250%, -280%) scale(1.2) rotate(-30deg); opacity: 0; }
}
@keyframes burst3 {
    0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
    100% { transform: translate(-280%, 250%) scale(1.4) rotate(90deg); opacity: 0; }
}
@keyframes burst4 {
    0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
    100% { transform: translate(280%, 280%) scale(1.3) rotate(-90deg); opacity: 0; }
}
@keyframes burst5 {
    0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
    100% { transform: translate(0%, -350%) scale(1.6) rotate(180deg); opacity: 0; }
}
@keyframes burst6 {
    0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
    100% { transform: translate(-350%, 0%) scale(1.6) rotate(180deg); opacity: 0; }
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
            
            # Confetti Elements
            rx.box("✨", class_name="confetti c-1"),
            rx.box("🎉", class_name="confetti c-2"),
            rx.box("🎊", class_name="confetti c-3"),
            rx.box("⭐", class_name="confetti c-4"),
            rx.box("🔥", class_name="confetti c-5"),
            rx.box("✨", class_name="confetti c-6"),

            rx.vstack(
                # Icono de Copa Animada GIGANTE
                rx.box(
                    rx.text(ProgressState.achievement_icon, font_size="8rem", line_height="1"),
                    class_name="trophy-anim",
                    margin_bottom=T.SPACE_4,
                    z_index="2",
                    position="relative"
                ),
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
