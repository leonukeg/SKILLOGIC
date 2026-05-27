"""
SKILLOGIC — Dashboard Page
Hero + learning path + current lesson preview + right panel.
"""

import reflex as rx
from SKILLOGIC.state import AppState
from SKILLOGIC.state.curriculum_state import CurriculumState
from SKILLOGIC.state.progress_state import ProgressState
from SKILLOGIC.components.layout import app_layout
from SKILLOGIC.styles import theme as T

# Decorative accents — same across themes
_VIOLET = "#a855f7"
_LILAC  = "#a78bfa"

# ── Subcomponents ─────────────────────────────────────────────

def _hero_card() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Content
            rx.vstack(
                rx.text(
                    rx.cond(AppState.is_spanish, "Aprende Python.", "Learn Python."),
                    font_size=T.TEXT_3XL,
                    font_weight=T.WEIGHT_EXTRABOLD,
                    color=rx.cond(AppState.is_dark, "#E6EDF3", "#1F2328"),
                    line_height="1.2",
                    letter_spacing="-0.5px",
                ),
                rx.text(
                    rx.cond(AppState.is_spanish, "Construye el futuro. 🚀", "Build the future. 🚀"),
                    font_size=T.TEXT_3XL,
                    font_weight=T.WEIGHT_EXTRABOLD,
                    # Dark: fancy gradient clip text. Light: solid deep-purple (always readable)
                    color=rx.cond(AppState.is_dark, "transparent", "#5B21B6"),
                    background=rx.cond(
                        AppState.is_dark,
                        "linear-gradient(90deg, #a78bfa, #7C3AED)",
                        "none",
                    ),
                    background_clip=rx.cond(AppState.is_dark, "text", "initial"),
                    webkit_background_clip=rx.cond(AppState.is_dark, "text", "initial"),
                    webkit_text_fill_color=rx.cond(AppState.is_dark, "transparent", "#5B21B6"),
                    line_height="1.2",
                    letter_spacing="-0.5px",
                ),
                rx.text(
                    rx.cond(
                        AppState.is_spanish,
                        "Un camino práctico, moderno y efectivo para llevar tus habilidades de Python al siguiente nivel.",
                        "A practical, modern and effective path to take your Python skills to the next level.",
                    ),
                    font_size=T.TEXT_BASE,
                    color=T.TEXT_SECONDARY,
                    max_width="380px",
                    line_height="1.5",
                ),
                rx.hstack(
                    rx.button(
                        rx.cond(AppState.is_spanish, "▶ Continuar aprendiendo", "▶ Continue learning"),
                        background=T.BRAND,
                        color="white",
                        border_radius=T.RADIUS_MD,
                        font_size=T.TEXT_MD,
                        font_weight=T.WEIGHT_SEMIBOLD,
                        padding=f"{T.SPACE_3} {T.SPACE_6}",
                        cursor="pointer",
                        box_shadow=T.SHADOW_BRAND,
                        transition=f"all {T.EASE_FAST}",
                        _hover={
                            "background": T.BRAND_HOVER,
                            "transform": "translateY(-1px)",
                            "box_shadow": f"0 6px 28px {T.BRAND_GLOW}",
                        },
                        on_click=rx.redirect("/lesson/funciones"),
                    ),
                    rx.button(
                        rx.cond(AppState.is_spanish, "Ver mi ruta", "View my path"),
                        background="transparent",
                        color=T.TEXT_PRIMARY,
                        border=f"1px solid {T.BORDER_STRONG}",
                        border_radius=T.RADIUS_MD,
                        font_size=T.TEXT_MD,
                        font_weight=T.WEIGHT_SEMIBOLD,
                        padding=f"{T.SPACE_3} {T.SPACE_6}",
                        cursor="pointer",
                        transition=f"all {T.EASE_FAST}",
                        _hover={"background": T.BG_HOVER},
                    ),
                    gap=T.SPACE_3,
                    flex_wrap="wrap",
                ),
                spacing="4",
                align_items="start",
                flex="1",
            ),
            # Python logo — bigger, float only, centered
            rx.box(
                rx.image(
                    src="/python_logo.svg",
                    width="130px",
                    height="130px",
                    alt="Python logo",
                ),
                style={"animation": "pythonFloat 5s ease-in-out infinite"},
                flex_shrink="0",
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            align="center",
            justify="between",
            gap=T.SPACE_6,
        ),
        border_radius=T.RADIUS_XL,
        background=T.HERO_GRADIENT,
        border=f"1px solid {T.HERO_BORDER}",
        padding=f"{T.SPACE_8} {T.SPACE_8}",
        margin_bottom=T.SPACE_6,
        min_height="180px",
        position="relative",
        overflow="hidden",
    )


def _module_card(mod: dict, index: int) -> rx.Component:
    status_class = mod["status"]
    border_color = (
        T.BRAND if status_class == "active"
        else T.SUCCESS if status_class == "completed"
        else T.BORDER
    )
    bg = (
        T.BRAND_LIGHT if status_class == "active"
        else T.SUCCESS_LIGHT if status_class == "completed"
        else T.BG_SECONDARY
    )
def _module_card(mod: rx.Var[dict]) -> rx.Component:
    is_locked = mod["status"] == "locked"
    is_completed = mod["status"] == "completed"
    
    # Colores dinámicos
    status_color = rx.cond(is_locked, T.TEXT_MUTED, rx.cond(is_completed, T.SUCCESS, T.BRAND))
    bg_color = rx.cond(is_locked, T.BG_HOVER, rx.cond(is_completed, T.SUCCESS_LIGHT, T.BRAND_LIGHT))
    border_color = rx.cond(is_locked, T.BORDER, rx.cond(is_completed, "transparent", T.BRAND_MEDIUM))
    text_color = rx.cond(is_locked, T.TEXT_MUTED, T.TEXT_PRIMARY)

    return rx.box(
        rx.box(
            rx.icon(tag=mod["icon_tag"].to(str), size=24, color=status_color),
            width="48px",
            height="48px",
            border_radius=T.RADIUS_LG,
            background=bg_color,
            display="flex",
            align_items="center",
            justify_content="center",
            margin_bottom=T.SPACE_4,
            border=f"1px solid {border_color}",
        ),
        rx.text(
            rx.cond(AppState.is_spanish, mod["name_es"], mod["name_en"]),
            font_size=T.TEXT_BASE,
            font_weight=T.WEIGHT_SEMIBOLD,
            color=text_color,
            margin_bottom=T.SPACE_2,
            min_height="48px",
            line_height="1.3",
        ),
        rx.box(
            rx.box(height="100%", width=mod["progress"].to(str) + "%", background=status_color, border_radius=T.RADIUS_FULL),
            height="6px",
            background=T.BG_HOVER,
            border_radius=T.RADIUS_FULL,
            overflow="hidden",
            margin_bottom=T.SPACE_2,
        ),
        rx.hstack(
            rx.text(mod["progress"].to(str) + "%", font_size=T.TEXT_XS, font_weight=T.WEIGHT_BOLD, color=status_color),
            rx.text(
                rx.cond(is_locked, rx.cond(AppState.is_spanish, "Bloqueado", "Locked"),
                rx.cond(is_completed, rx.cond(AppState.is_spanish, "Completado", "Completed"), rx.cond(AppState.is_spanish, "En progreso", "In progreso"))),
                font_size=T.TEXT_XS, color=T.TEXT_MUTED
            ),
            justify="between",
        ),
        padding=T.SPACE_5,
        background=T.BG_SECONDARY,
        border=f"1px solid {T.BORDER}",
        border_radius=T.RADIUS_XL,
        position="relative",
        overflow="hidden",
        cursor=rx.cond(is_locked, "not-allowed", "pointer"),
        transition=f"all {T.EASE_BASE}",
        _hover={
            "border_color": rx.cond(is_locked, T.BORDER, T.BORDER_STRONG),
            "transform": rx.cond(is_locked, "none", "translateY(-4px)"),
            "box_shadow": rx.cond(is_locked, "none", T.SHADOW_MD),
        },
    )


def _learning_path() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                rx.cond(AppState.is_spanish, "Tu ruta de aprendizaje", "Your learning path"),
                font_size=T.TEXT_MD,
                font_weight=T.WEIGHT_SEMIBOLD,
                color=T.TEXT_PRIMARY,
            ),
            rx.link(
                rx.cond(AppState.is_spanish, "Ver ruta completa →", "View full path →"),
                font_size=T.TEXT_SM,
                color=T.BRAND,
                font_weight=T.WEIGHT_MEDIUM,
                cursor="pointer",
                _hover={"color": "#a78bfa"},
            ),
            justify="between",
            align="center",
            margin_bottom=T.SPACE_4,
        ),
        rx.hstack(
            rx.foreach(CurriculumState.modules, _module_card),
            gap=T.SPACE_3,
            overflow_x="auto",
            padding_bottom=T.SPACE_2,
        ),
        margin_bottom=T.SPACE_6,
    )


def _current_lesson_preview() -> rx.Component:
    """Preview of the current lesson with a static code snippet."""

    code_snippet = (
        "def saludar(nombre):\n"
        '    """\n'
        "    Esta función recibe un nombre\n"
        "    y devuelve un saludo personalizado.\n"
        '    """\n'
        '    saludo = f"¡Hola, {nombre}!"\n'
        "    return saludo\n\n"
        "# Prueba tu función\n"
        'resultado = saludar("Ana")\n'
        "print(resultado)"
    )

    return rx.box(
        # Header
        rx.hstack(
            rx.vstack(
                rx.text(
                    rx.cond(AppState.is_spanish, "Lección actual", "Current lesson"),
                    font_size=T.TEXT_XS,
                    color=T.TEXT_MUTED,
                    font_weight=T.WEIGHT_SEMIBOLD,
                    text_transform="uppercase",
                    letter_spacing="0.5px",
                ),
                rx.text(
                    rx.cond(AppState.is_spanish, "Funciones en Python", "Functions in Python"),
                    font_size=T.TEXT_MD,
                    font_weight=T.WEIGHT_SEMIBOLD,
                    color=T.TEXT_PRIMARY,
                ),
                spacing="1",
                align_items="start",
            ),
            rx.hstack(
                rx.box(
                    rx.hstack(
                        rx.icon(tag="star", size=14, color=T.WARNING),
                        rx.text("25 XP", font_size=T.TEXT_XS, font_weight=T.WEIGHT_SEMIBOLD, color=T.WARNING),
                        gap=T.SPACE_1, align="center"
                    ),
                    background=T.WARNING_LIGHT,
                    border_radius=T.RADIUS_FULL,
                    padding=f"2px {T.SPACE_2}",
                ),
                rx.button(
                    rx.cond(AppState.is_spanish, "Abrir lección", "Open lesson"),
                    background=T.BRAND,
                    color="white",
                    border_radius=T.RADIUS_MD,
                    font_size=T.TEXT_XS,
                    font_weight=T.WEIGHT_SEMIBOLD,
                    padding=f"{T.SPACE_1} {T.SPACE_3}",
                    cursor="pointer",
                    _hover={"background": T.BRAND_HOVER},
                    on_click=rx.redirect("/lesson/funciones"),
                ),
                gap=T.SPACE_2,
                align="center",
            ),
            justify="between",
            align="center",
            padding=f"{T.SPACE_4} {T.SPACE_5}",
            border_bottom=f"1px solid {T.BORDER}",
        ),

        # Tabs
        rx.hstack(
            rx.hstack(
                rx.icon(tag="book-open", size=16),
                rx.text(rx.cond(AppState.is_spanish, "Instrucciones", "Instructions")),
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_MEDIUM,
                color=T.TEXT_PRIMARY,
                border_bottom=f"2px solid {T.BRAND}",
                padding=f"{T.SPACE_3} {T.SPACE_4}",
                cursor="pointer",
                align="center",
                gap=T.SPACE_2,
            ),
            rx.hstack(
                rx.icon(tag="lightbulb", size=16),
                rx.text(rx.cond(AppState.is_spanish, "Pista", "Hint")),
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_MEDIUM,
                color=T.TEXT_MUTED,
                padding=f"{T.SPACE_3} {T.SPACE_4}",
                cursor="pointer",
                _hover={"color": T.TEXT_SECONDARY},
                align="center",
                gap=T.SPACE_2,
            ),
            rx.hstack(
                rx.icon(tag="message-circle", size=16),
                rx.text(rx.cond(AppState.is_spanish, "Discusión", "Discussion")),
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_MEDIUM,
                color=T.TEXT_MUTED,
                padding=f"{T.SPACE_3} {T.SPACE_4}",
                cursor="pointer",
                _hover={"color": T.TEXT_SECONDARY},
                align="center",
                gap=T.SPACE_2,
            ),
            border_bottom=f"1px solid {T.BORDER}",
            padding=f"0 {T.SPACE_5}",
            gap="0",
        ),

        # 3-panel preview
        rx.hstack(
            # Instructions
            rx.box(
                rx.text(
                    rx.cond(AppState.is_spanish,
                        "Las funciones permiten reutilizar código y mantener nuestros programas organizados.",
                        "Functions let you reuse code and keep your programs organized.",
                    ),
                    font_size=T.TEXT_SM,
                    color=T.TEXT_SECONDARY,
                    line_height="1.7",
                    margin_bottom=T.SPACE_3,
                ),
                rx.text(
                    rx.cond(AppState.is_spanish,
                        "Crea una función llamada saludar que reciba un nombre y devuelva un saludo personalizado.",
                        "Create a function called greet that receives a name and returns a personalized greeting.",
                    ),
                    font_size=T.TEXT_SM,
                    color=T.TEXT_SECONDARY,
                    line_height="1.7",
                ),
                width="280px",
                flex_shrink="0",
                padding=T.SPACE_5,
                border_right=f"1px solid {T.BORDER}",
                overflow_y="auto",
            ),

            # Code display (static in dashboard preview)
            rx.box(
                rx.hstack(
                    rx.hstack(
                        rx.text("●", color=T.BRAND),
                        rx.text("Python 3", font_size=T.TEXT_XS, color=T.TEXT_MUTED, font_family=T.FONT_CODE),
                        gap=T.SPACE_2,
                        align="center",
                    ),
                    rx.button(
                        rx.icon(tag="rotate-cw", size=12),
                        rx.text(rx.cond(AppState.is_spanish, "Reiniciar", "Reset")),
                        background="transparent",
                        color=T.TEXT_MUTED,
                        font_size=T.TEXT_XS,
                        cursor="pointer",
                        padding=f"{T.SPACE_1} {T.SPACE_2}",
                        border_radius=T.RADIUS_SM,
                        _hover={"background": T.BG_HOVER, "color": T.TEXT_PRIMARY},
                    ),
                    justify="between",
                    padding=f"{T.SPACE_2} {T.SPACE_4}",
                    border_bottom=f"1px solid {T.BORDER}",
                    background=T.BG_ELEVATED,
                ),
                rx.code_block(
                    code_snippet,
                    language="python",
                    font_size="12px",
                    background=T.BG_PRIMARY,
                    color=T.TEXT_PRIMARY,
                    width="100%",
                    border_radius="0",
                    padding=T.SPACE_4,
                    font_family=T.FONT_CODE,
                ),
                flex="1",
                border_right=f"1px solid {T.BORDER}",
                overflow="hidden",
            ),

            # Output panel
            rx.box(
                rx.text(
                    rx.cond(AppState.is_spanish, "Salida", "Output"),
                    font_size=T.TEXT_XS,
                    font_weight=T.WEIGHT_SEMIBOLD,
                    color=T.TEXT_MUTED,
                    text_transform="uppercase",
                    letter_spacing="0.5px",
                    margin_bottom=T.SPACE_3,
                ),
                rx.box(
                    rx.hstack(
                        rx.icon(tag="check-circle", size=16, color=T.SUCCESS),
                        rx.text(rx.cond(AppState.is_spanish, "¡Correcto! 🎉", "Correct! 🎉"),
                                font_size=T.TEXT_SM, color=T.SUCCESS),
                        align="center",
                        gap=T.SPACE_2,
                    ),
                    background=T.SUCCESS_LIGHT,
                    border_radius=T.RADIUS_MD,
                    padding=f"{T.SPACE_2} {T.SPACE_3}",
                    margin_bottom=T.SPACE_2,
                ),
                rx.box(
                    rx.text("¡Hola, Ana!", font_size=T.TEXT_SM, color=T.TEXT_PRIMARY, font_family=T.FONT_CODE),
                    background=T.BG_HOVER,
                    border_radius=T.RADIUS_MD,
                    padding=T.SPACE_3,
                    font_family=T.FONT_CODE,
                    font_size=T.TEXT_XS,
                ),
                width="240px",
                flex_shrink="0",
                padding=T.SPACE_4,
                background=T.BG_ELEVATED,
                overflow_y="auto",
            ),
            align="stretch",
            min_height="280px",
            gap="0",
        ),

        # Actions bar
        rx.hstack(
            rx.button(
                rx.icon(tag="lightbulb", size=14),
                rx.text(rx.cond(AppState.is_spanish, "Pista", "Hint")),
                background="transparent",
                color=T.TEXT_SECONDARY,
                font_size=T.TEXT_SM,
                cursor="pointer",
                padding=f"{T.SPACE_1} {T.SPACE_3}",
                border_radius=T.RADIUS_SM,
                _hover={"background": T.BG_HOVER},
            ),
            rx.hstack(
                rx.button(
                    rx.icon(tag="rotate-cw", size=14),
                    rx.text(rx.cond(AppState.is_spanish, "Reiniciar", "Reset")),
                    background="transparent",
                    color=T.TEXT_SECONDARY,
                    border=f"1px solid {T.BORDER_STRONG}",
                    border_radius=T.RADIUS_MD,
                    font_size=T.TEXT_SM,
                    font_weight=T.WEIGHT_SEMIBOLD,
                    padding=f"{T.SPACE_1} {T.SPACE_3}",
                    cursor="pointer",
                    _hover={"background": T.BG_HOVER},
                ),
                rx.button(
                    rx.icon(tag="play", size=14),
                    rx.text(rx.cond(AppState.is_spanish, "Ejecutar", "Run")),
                    background=T.BRAND,
                    color="white",
                    border_radius=T.RADIUS_MD,
                    font_size=T.TEXT_SM,
                    font_weight=T.WEIGHT_SEMIBOLD,
                    padding=f"{T.SPACE_2} {T.SPACE_5}",
                    cursor="pointer",
                    box_shadow=T.SHADOW_BRAND,
                    _hover={"background": T.BRAND_HOVER},
                    on_click=rx.redirect("/lesson/funciones"),
                ),
                gap=T.SPACE_2,
            ),
            justify="between",
            align="center",
            padding=f"{T.SPACE_3} {T.SPACE_5}",
            border_top=f"1px solid {T.BORDER}",
        ),

        background=T.BG_SECONDARY,
        border=f"1px solid {T.BORDER}",
        border_radius=T.RADIUS_XL,
        margin_bottom=T.SPACE_6,
        overflow="hidden",
    )


def _project_card(proj: rx.Var[dict]) -> rx.Component:
    level = proj["level"].to(str)
    bg = rx.cond(level == "advanced", T.ERROR_LIGHT, rx.cond(level == "intermediate", T.WARNING_LIGHT, T.INFO_LIGHT))
    fg = rx.cond(level == "advanced", T.ERROR, rx.cond(level == "intermediate", T.WARNING, T.INFO))

    level_es = rx.cond(level == "advanced", "Avanzado", rx.cond(level == "intermediate", "Intermedio", "Básico"))
    level_en = rx.cond(level == "advanced", "Advanced", rx.cond(level == "intermediate", "Intermediate", "Basic"))

    return rx.hstack(
        rx.box(
            rx.icon(tag="folder", size=20, color=T.TEXT_PRIMARY),
            width="40px",
            height="40px",
            border_radius=T.RADIUS_MD,
            background=T.BG_HOVER,
            display="flex",
            align_items="center",
            justify_content="center",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.text(
                rx.cond(AppState.is_spanish, proj["title_es"], proj["title_en"]),
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_SEMIBOLD,
                color=T.TEXT_PRIMARY,
                white_space="nowrap",
                overflow="hidden",
                text_overflow="ellipsis",
            ),
            rx.box(
                rx.text(
                    rx.cond(AppState.is_spanish, level_es, level_en),
                    font_size=T.TEXT_XS,
                    font_weight=T.WEIGHT_MEDIUM,
                    color=fg,
                ),
                background=bg,
                border_radius=T.RADIUS_FULL,
                padding=f"2px {T.SPACE_2}",
            ),
            spacing="1",
            align_items="start",
            flex="1",
            min_width="0",
        ),
        background=T.BG_SECONDARY,
        border=f"1px solid {T.BORDER}",
        border_radius=T.RADIUS_LG,
        padding=T.SPACE_4,
        cursor="pointer",
        transition=f"all {T.EASE_BASE}",
        _hover={
            "border_color": T.BORDER_STRONG,
            "transform": "translateY(-2px)",
            "box_shadow": T.SHADOW_MD,
        },
        align="center",
        gap=T.SPACE_3,
    )

def _projects_grid() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                rx.cond(AppState.is_spanish, "Proyectos para ti", "Projects for you"),
                font_size=T.TEXT_MD,
                font_weight=T.WEIGHT_SEMIBOLD,
                color=T.TEXT_PRIMARY,
            ),
            rx.text(
                rx.cond(AppState.is_spanish, "Ver portafolio →", "View portfolio →"),
                font_size=T.TEXT_SM,
                color=T.BRAND,
                cursor="pointer",
                _hover={"color": "#a78bfa"},
            ),
            justify="between",
            align="center",
            margin_bottom=T.SPACE_4,
        ),
        rx.grid(
            rx.foreach(CurriculumState.projects, _project_card),
            columns="2",
            gap=T.SPACE_4,
        ),
    )


# ── Right Panel subcomponents ─────────────────────────────────

def _right_stats() -> rx.Component:
    return rx.box(
        # TU PROGRESO Header
        rx.text(
            rx.cond(AppState.is_spanish, "TU PROGRESO", "YOUR PROGRESS"),
            font_size=T.TEXT_XS, font_weight=T.WEIGHT_BOLD, color=T.TEXT_MUTED, letter_spacing="1px", margin_bottom=T.SPACE_3
        ),
        # Nivel y XP
        rx.hstack(
            rx.box(
                rx.text(ProgressState.level.to_string(), font_size=T.TEXT_LG, font_weight=T.WEIGHT_EXTRABOLD, color="white"),
                width="40px", height="40px", border_radius="50%", background=f"linear-gradient(135deg, {T.BRAND}, #a855f7)", display="flex", align_items="center", justify_content="center", box_shadow=T.SHADOW_BRAND,
            ),
            rx.spacer(),
            rx.text(ProgressState.xp.to_string() + " / " + ProgressState.xp_to_next_level.to_string() + " XP", font_size=T.TEXT_SM, font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
            align="center", margin_bottom=T.SPACE_2
        ),
        # Barra principal
        rx.box(
            rx.box(width=ProgressState.xp_progress_percent.to_string() + "%", height="100%", background=f"linear-gradient(90deg, {T.BRAND}, #a855f7)", border_radius=T.RADIUS_FULL, transition="width 0.5s ease"),
            width="100%", height="6px", background=T.BG_ELEVATED, border_radius=T.RADIUS_FULL, overflow="hidden", margin_bottom=T.SPACE_2
        ),
        # Rango
        rx.hstack(
            rx.icon(tag="award", size=14, color=T.TEXT_MUTED),
            rx.text("Rango", font_size=T.TEXT_XS, color=T.TEXT_MUTED),
            rx.spacer(),
            rx.text(
                rx.cond(
                    ProgressState.xp == 0, "Novato", 
                    rx.cond(ProgressState.level < 5, "Explorer", 
                    rx.cond(ProgressState.level < 10, "Pioneer", "Master"))
                ), 
                font_size=T.TEXT_XS, font_weight=T.WEIGHT_BOLD, color=T.BRAND_LIGHT
            ),
            align="center", margin_bottom=T.SPACE_6
        ),

        # RACHA ACTUAL
        rx.text(
            rx.cond(AppState.is_spanish, "RACHA ACTUAL", "CURRENT STREAK"),
            font_size=T.TEXT_XS, font_weight=T.WEIGHT_BOLD, color=T.TEXT_MUTED, letter_spacing="1px", margin_bottom=T.SPACE_3
        ),
        rx.hstack(
            rx.icon(tag="flame", size=20, color="#f97316"),
            rx.text(ProgressState.streak_days.to_string(), font_size=T.TEXT_2XL, font_weight=T.WEIGHT_EXTRABOLD, color="#f97316", line_height="1"),
            rx.text(rx.cond(AppState.is_spanish, "días", "days"), font_size=T.TEXT_SM, color=T.TEXT_MUTED, align_self="end", margin_bottom="2px"),
            align="end", gap=T.SPACE_2, margin_bottom=T.SPACE_3
        ),
        # Dias de la semana (Mock visual)
        rx.hstack(
            rx.foreach(
                ["L", "M", "M", "J", "V", "S", "D"],
                lambda d, i: rx.vstack(
                    rx.text(d, font_size="10px", color=T.TEXT_MUTED, font_weight=T.WEIGHT_BOLD),
                    rx.box(width="24px", height="24px", border_radius="50%", background=rx.cond(i < 4, "#f97316", "transparent"), border=rx.cond(i < 4, "none", f"2px solid {T.BORDER_STRONG}")),
                    align_items="center", spacing="1"
                )
            ),
            justify="between", margin_bottom=T.SPACE_6
        ),

        # Proximo Objetivo
        rx.text("Próximo objetivo", font_size=T.TEXT_XS, color=T.TEXT_MUTED, margin_bottom=T.SPACE_1),
        rx.text("Completa 3 ejercicios", font_size=T.TEXT_MD, font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_2),
        rx.box(
            rx.box(width="33%", height="100%", background=f"linear-gradient(90deg, {T.BRAND}, #a855f7)", border_radius=T.RADIUS_FULL),
            width="100%", height="4px", background=T.BG_ELEVATED, border_radius=T.RADIUS_FULL, overflow="hidden", margin_bottom=T.SPACE_6
        ),

        margin_bottom=T.SPACE_5,
        padding_bottom=T.SPACE_2,
        border_bottom=f"1px solid {T.BORDER_SUBTLE}",
    )


def _right_plan() -> rx.Component:
    def plan_item(item: rx.Var[dict]) -> rx.Component:
        is_completed = item["completed"] == "True"
        return rx.hstack(
            rx.box(
                rx.icon(
                    tag=rx.cond(is_completed, "check", "circle"), 
                    size=12, 
                    color=rx.cond(is_completed, "white", "transparent")
                ),
                width="20px",
                height="20px",
                border_radius="50%",
                background=rx.cond(is_completed, T.SUCCESS, "transparent"),
                border=rx.cond(is_completed, f"2px solid {T.SUCCESS}", f"2px solid {T.BORDER}"),
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
            ),
            rx.vstack(
                rx.text(
                    rx.cond(AppState.is_spanish, item["title_es"], item["title_en"]),
                    font_size=T.TEXT_SM,
                    color=rx.cond(is_completed, T.TEXT_MUTED, T.TEXT_PRIMARY),
                    text_decoration=rx.cond(is_completed, "line-through", "none"),
                    white_space="nowrap",
                    overflow="hidden",
                    text_overflow="ellipsis",
                ),
                rx.text(
                    rx.cond(AppState.is_spanish, item["subtitle_es"], item["subtitle_en"]),
                    font_size=T.TEXT_XS,
                    color=T.TEXT_MUTED,
                ),
                spacing="0",
                align_items="start",
                flex="1",
                min_width="0",
            ),
            align="center",
            gap=T.SPACE_3,
            padding=f"{T.SPACE_2} 0",
            cursor="pointer",
            on_click=lambda: CurriculumState.toggle_plan_by_title(item["title_en"], ~is_completed),
        )

    return rx.box(
        rx.hstack(
            rx.text(
                rx.cond(AppState.is_spanish, "Plan de hoy", "Today's plan"),
                font_size=T.TEXT_SM, font_weight=T.WEIGHT_SEMIBOLD, color=T.TEXT_PRIMARY,
            ),
            rx.text(
                rx.cond(AppState.is_spanish, "Ver todo", "See all"),
                font_size=T.TEXT_XS, color=T.BRAND, cursor="pointer",
                _hover={"color": "#a78bfa"},
            ),
            justify="between", align="center", margin_bottom=T.SPACE_3,
        ),
        rx.vstack(
            rx.foreach(CurriculumState.todays_plan, plan_item),
            width="100%",
        ),
        rx.button(
            rx.cond(AppState.is_spanish, "Continuar plan", "Continue plan"),
            width="100%",
            background=T.BRAND,
            color="white",
            border_radius=T.RADIUS_MD,
            font_size=T.TEXT_SM,
            font_weight=T.WEIGHT_SEMIBOLD,
            padding=f"{T.SPACE_2} 0",
            cursor="pointer",
            margin_top=T.SPACE_3,
            box_shadow=T.SHADOW_BRAND,
            _hover={"background": T.BRAND_HOVER},
        ),
        margin_bottom=T.SPACE_5,
        padding_bottom=T.SPACE_5,
        border_bottom=f"1px solid {T.BORDER_SUBTLE}",
    )


def _right_challenge() -> rx.Component:
    dc = CurriculumState.daily_challenge
    diff = dc["difficulty_level"].to(str)
    diff_color = rx.cond(
        diff == "advanced", T.ERROR,
        rx.cond(diff == "intermediate", T.WARNING, T.SUCCESS)
    )

    return rx.box(
        rx.hstack(
            rx.text(
                rx.cond(AppState.is_spanish, "Desafío diario", "Daily challenge"),
                font_size=T.TEXT_SM, font_weight=T.WEIGHT_SEMIBOLD, color=T.TEXT_PRIMARY,
            ),
            rx.cond(
                dc["is_new"].to(bool),
                rx.box(
                    rx.text(
                        rx.cond(AppState.is_spanish, "Nuevo", "New"),
                        font_size=T.TEXT_XS, font_weight=T.WEIGHT_BOLD, color="white",
                    ),
                    background=T.BRAND,
                    border_radius=T.RADIUS_FULL,
                    padding=f"2px {T.SPACE_2}",
                ),
                rx.box(),
            ),
            justify="between", align="center", margin_bottom=T.SPACE_3,
        ),
        rx.box(
            rx.hstack(
                rx.text(
                    rx.cond(AppState.is_spanish, dc["title_es"], dc["title_en"]),
                    font_size=T.TEXT_BASE, font_weight=T.WEIGHT_SEMIBOLD, color=T.TEXT_PRIMARY,
                ),
            ),
            rx.text(
                rx.cond(AppState.is_spanish, "Dificultad: ", "Difficulty: "),
                rx.text.span(
                    rx.cond(AppState.is_spanish, dc["difficulty_es"], dc["difficulty_en"]),
                    color=diff_color, font_weight=T.WEIGHT_SEMIBOLD,
                ),
                font_size=T.TEXT_XS, color=T.TEXT_MUTED, margin="4px 0",
            ),
            rx.text(
                rx.cond(AppState.is_spanish, dc["desc_es"], dc["desc_en"]),
                font_size=T.TEXT_SM, color=T.TEXT_SECONDARY, line_height="1.5", margin_bottom=T.SPACE_3,
            ),
            rx.button(
                rx.icon(tag="play", size=14),
                rx.text(rx.cond(AppState.is_spanish, "Resolver desafío", "Solve challenge")),
                width="100%",
                background=T.BRAND,
                color="white",
                border_radius=T.RADIUS_MD,
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_SEMIBOLD,
                padding=f"{T.SPACE_2} 0",
                cursor="pointer",
                _hover={"background": T.BRAND_HOVER},
                display="flex",
                align_items="center",
                justify_content="center",
                gap=T.SPACE_2,
            ),
            background=T.BG_HOVER,
            border=f"1px solid {T.BORDER}",
            border_radius=T.RADIUS_LG,
            padding=T.SPACE_4,
        ),
        rx.text(
            rx.cond(AppState.is_spanish, "Ver todos los desafíos →", "See all challenges →"),
            font_size=T.TEXT_XS, color=T.BRAND, cursor="pointer",
            margin_top=T.SPACE_3, display="block",
            _hover={"color": "#a78bfa"},
        ),
        margin_bottom=T.SPACE_5,
        padding_bottom=T.SPACE_5,
        border_bottom=f"1px solid {T.BORDER_SUBTLE}",
    )


def _right_community() -> rx.Component:
    feed_es = [
        ("ML", "#7C3AED", "María completó el proyecto Habit Tracker 🎉", "hace 2h"),
        ("JC", "#2EA043", "Juan respondió en \"List comprehensions\"",     "hace 3h"),
        ("PL", "#F97316", "PythonLover14 logró una racha de 30 días 🔥",  "hace 5h"),
    ]
    feed_en = [
        ("ML", "#7C3AED", "María completed the Habit Tracker project 🎉", "2h ago"),
        ("JC", "#2EA043", "Juan replied in \"List comprehensions\"",        "3h ago"),
        ("PL", "#F97316", "PythonLover14 reached a 30-day streak 🔥",     "5h ago"),
    ]

    def feed_item(es, en) -> rx.Component:
        return rx.hstack(
            rx.box(
                rx.text(es[0], font_size=T.TEXT_XS, font_weight=T.WEIGHT_BOLD, color="white"),
                width="30px", height="30px", border_radius="50%",
                background=es[1], display="flex",
                align_items="center", justify_content="center", flex_shrink="0",
            ),
            rx.vstack(
                rx.text(
                    rx.cond(AppState.is_spanish, es[2], en[2]),
                    font_size=T.TEXT_XS, color=T.TEXT_SECONDARY, line_height="1.4",
                ),
                rx.text(
                    rx.cond(AppState.is_spanish, es[3], en[3]),
                    font_size="10px", color=T.TEXT_MUTED,
                ),
                spacing="0", align_items="start",
            ),
            align="start", gap=T.SPACE_3, padding=f"{T.SPACE_2} 0",
        )

    return rx.box(
        rx.text(
            rx.cond(AppState.is_spanish, "Comunidad activa", "Active community"),
            font_size=T.TEXT_SM, font_weight=T.WEIGHT_SEMIBOLD, color=T.TEXT_PRIMARY,
            margin_bottom=T.SPACE_3,
        ),
        feed_item(feed_es[0], feed_en[0]),
        feed_item(feed_es[1], feed_en[1]),
        feed_item(feed_es[2], feed_en[2]),
        rx.button(
            rx.cond(AppState.is_spanish, "Ir a la comunidad →", "Go to community →"),
            width="100%", background="transparent", color=T.TEXT_SECONDARY,
            border_radius=T.RADIUS_MD, font_size=T.TEXT_SM, font_weight=T.WEIGHT_SEMIBOLD,
            padding=f"{T.SPACE_2} 0", cursor="pointer",
            margin_top=T.SPACE_2,
            _hover={"background": T.BG_HOVER, "color": T.TEXT_PRIMARY},
        ),
    )


# ── Main dashboard page ───────────────────────────────────────

def dashboard_page() -> rx.Component:
    """Full dashboard with main content + right panel."""

    main_content = rx.box(
        _hero_card(),
        _learning_path(),
        # MVP Cleanup
        # _current_lesson_preview(),
        # _projects_grid(),
        padding=T.SPACE_6,
        flex="1",
        min_width="0",
        overflow_y="auto",
    )

    right_panel = rx.box(
        _right_stats(),
        # MVP Cleanup
        # _right_plan(),
        # _right_challenge(),
        # _right_community(),
        width=T.RIGHT_PANEL_WIDTH,
        flex_shrink="0",
        border_left=f"1px solid {T.BORDER}",
        background=T.BG_SECONDARY,
        padding=T.SPACE_5,
        overflow_y="auto",
    )

    return app_layout(
        rx.hstack(
            main_content,
            # MVP Cleanup: right panel hidden for now
            # right_panel,
            align="stretch",
            gap="0",
            min_height=f"calc(100vh - {T.TOPBAR_HEIGHT})",
        ),
    )
