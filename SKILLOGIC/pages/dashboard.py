"""
SKILLOGIC — Dashboard Page
Hero + learning path + current lesson preview + right panel.
"""

import reflex as rx
from SKILLOGIC.state import AppState
from SKILLOGIC.components.layout import app_layout
from SKILLOGIC.styles import theme as T

# Decorative accents — same across themes
_VIOLET = "#a855f7"
_LILAC  = "#a78bfa"

# ── Mock data (will come from DB in Phase 1) ──────────────────

MODULES = [
    {"emoji": "⌨️", "name_es": "Fundamentos Reales",   "name_en": "Real Fundamentals",   "progress": 100, "status": "completed"},
    {"emoji": "🔧", "name_es": "Estructuras de Datos",  "name_en": "Data Structures",     "progress": 75,  "status": "active"},
    {"emoji": "📐", "name_es": "Funciones y Módulos",   "name_en": "Functions & Modules", "progress": 40,  "status": "active"},
    {"emoji": "🧩", "name_es": "POO",                   "name_en": "OOP",                 "progress": 20,  "status": "upcoming"},
    {"emoji": "🚀", "name_es": "Proyectos",             "name_en": "Projects",            "progress": 3,   "status": "upcoming"},
]

PROJECTS = [
    {"icon": "🔐", "name_es": "Generador de Contraseñas", "name_en": "Password Generator", "level": "intermediate", "progress": 75},
    {"icon": "🌐", "name_es": "Web Scraper",              "name_en": "Web Scraper",         "level": "basic",        "progress": 0},
    {"icon": "📋", "name_es": "Lista de Tareas",          "name_en": "Task List",           "level": "intermediate", "progress": 25},
    {"icon": "📊", "name_es": "Análisis de Datos",        "name_en": "Data Analysis",       "level": "advanced",     "progress": 0},
]


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
                    color=T.TEXT_PRIMARY,
                    line_height="1.2",
                    letter_spacing="-0.5px",
                ),
                rx.text(
                    rx.cond(AppState.is_spanish, "Construye el futuro. 🚀", "Build the future. 🚀"),
                    font_size=T.TEXT_3XL,
                    font_weight=T.WEIGHT_EXTRABOLD,
                    background=f"linear-gradient(90deg, #a78bfa, {T.BRAND})",
                    background_clip="text",
                    webkit_background_clip="text",
                    webkit_text_fill_color="transparent",
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
            # Python emoji visual
            rx.text(
                "🐍",
                font_size="80px",
                opacity="0.9",
                flex_shrink="0",
                style={"animation": "float 4s ease-in-out infinite"},
            ),
            align="center",
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
    bar_color = T.SUCCESS if status_class == "completed" else T.BRAND

    return rx.box(
        rx.text(mod["emoji"], font_size="28px", margin_bottom=T.SPACE_2, display="block"),
        rx.text(
            f"{index + 1}. ",
            rx.cond(AppState.is_spanish, mod["name_es"], mod["name_en"]),
            font_size=T.TEXT_SM,
            font_weight=T.WEIGHT_SEMIBOLD,
            color=T.TEXT_PRIMARY,
            margin_bottom=T.SPACE_3,
            line_height="1.3",
        ),
        rx.text(
            f"{mod['progress']}%",
            font_size=T.TEXT_XS,
            color=T.TEXT_SECONDARY,
            margin_bottom=T.SPACE_1,
            font_weight=T.WEIGHT_MEDIUM,
        ),
        rx.box(
            rx.box(
                height="100%",
                width=f"{mod['progress']}%",
                background=bar_color,
                border_radius=T.RADIUS_FULL,
            ),
            height="4px",
            background=T.BG_HOVER,
            border_radius=T.RADIUS_FULL,
            overflow="hidden",
        ),
        flex_shrink="0",
        width="148px",
        background=bg,
        border=f"1px solid {border_color}",
        border_radius=T.RADIUS_LG,
        padding=f"{T.SPACE_4} {T.SPACE_3}",
        cursor="pointer",
        transition=f"all {T.EASE_BASE}",
        _hover={
            "transform": "translateY(-2px)",
            "box_shadow": T.SHADOW_MD,
        },
    )


def _learning_path() -> rx.Component:
    module_cards = [_module_card(mod, i) for i, mod in enumerate(MODULES)]
    # Interleave connectors
    items = []
    for i, card in enumerate(module_cards):
        items.append(card)
        if i < len(module_cards) - 1:
            items.append(rx.text("→", color=T.BORDER, flex_shrink="0", margin_top="20px"))

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
            *items,
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
                    rx.text("⭐ 25 XP", font_size=T.TEXT_XS, font_weight=T.WEIGHT_SEMIBOLD, color=T.WARNING),
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
            rx.text(
                rx.cond(AppState.is_spanish, "📖 Instrucciones", "📖 Instructions"),
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_MEDIUM,
                color=T.TEXT_PRIMARY,
                border_bottom=f"2px solid {T.BRAND}",
                padding=f"{T.SPACE_3} {T.SPACE_4}",
                cursor="pointer",
            ),
            rx.text(
                rx.cond(AppState.is_spanish, "💡 Pista", "💡 Hint"),
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_MEDIUM,
                color=T.TEXT_MUTED,
                padding=f"{T.SPACE_3} {T.SPACE_4}",
                cursor="pointer",
                _hover={"color": T.TEXT_SECONDARY},
            ),
            rx.text(
                rx.cond(AppState.is_spanish, "💬 Discusión", "💬 Discussion"),
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_MEDIUM,
                color=T.TEXT_MUTED,
                padding=f"{T.SPACE_3} {T.SPACE_4}",
                cursor="pointer",
                _hover={"color": T.TEXT_SECONDARY},
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
                        rx.cond(AppState.is_spanish, "⟳ Reiniciar", "⟳ Reset"),
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
                    rx.text("✅ ", rx.cond(AppState.is_spanish, "¡Correcto! 🎉", "Correct! 🎉"),
                            font_size=T.TEXT_SM, color=T.SUCCESS),
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
                rx.cond(AppState.is_spanish, "💡 Pista", "💡 Hint"),
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
                    rx.cond(AppState.is_spanish, "⟳ Reiniciar", "⟳ Reset"),
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
                    rx.cond(AppState.is_spanish, "▶ Ejecutar", "▶ Run"),
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


def _projects_grid() -> rx.Component:
    level_colors = {
        "basic":        (T.INFO_LIGHT, T.INFO),
        "intermediate": (T.WARNING_LIGHT, T.WARNING),
        "advanced":     (T.ERROR_LIGHT, T.ERROR),
    }
    level_labels_es = {"basic": "Básico", "intermediate": "Intermedio", "advanced": "Avanzado"}
    level_labels_en = {"basic": "Basic", "intermediate": "Intermediate", "advanced": "Advanced"}

    cards = []
    for proj in PROJECTS:
        bg, fg = level_colors.get(proj["level"], (T.BRAND_LIGHT, T.BRAND))
        card = rx.hstack(
            rx.box(
                rx.text(proj["icon"], font_size="20px"),
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
                    rx.cond(AppState.is_spanish, proj["name_es"], proj["name_en"]),
                    font_size=T.TEXT_SM,
                    font_weight=T.WEIGHT_SEMIBOLD,
                    color=T.TEXT_PRIMARY,
                    white_space="nowrap",
                    overflow="hidden",
                    text_overflow="ellipsis",
                ),
                rx.box(
                    rx.text(
                        rx.cond(AppState.is_spanish,
                            level_labels_es[proj["level"]],
                            level_labels_en[proj["level"]],
                        ),
                        font_size=T.TEXT_XS,
                        font_weight=T.WEIGHT_MEDIUM,
                        color=fg,
                    ),
                    background=bg,
                    border_radius=T.RADIUS_FULL,
                    padding=f"2px {T.SPACE_2}",
                ),
                *([
                    rx.box(
                        rx.box(height="100%", width=f"{proj['progress']}%", background=T.BRAND, border_radius=T.RADIUS_FULL),
                        height="4px", background=T.BG_HOVER, border_radius=T.RADIUS_FULL, overflow="hidden",
                        margin_top="4px",
                    ),
                ] if proj["progress"] > 0 else []),
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
        cards.append(card)

    return rx.box(
        rx.hstack(
            rx.text(
                rx.cond(AppState.is_spanish, "Proyectos para ti", "Projects for you"),
                font_size=T.TEXT_MD,
                font_weight=T.WEIGHT_SEMIBOLD,
                color=T.TEXT_PRIMARY,
            ),
            rx.text(
                rx.cond(AppState.is_spanish, "Ver todos →", "See all →"),
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
        rx.grid(
            *cards,
            columns="2",
            gap=T.SPACE_4,
        ),
    )


# ── Right Panel subcomponents ─────────────────────────────────

def _right_streak() -> rx.Component:
    return rx.box(
        rx.text(
            rx.cond(AppState.is_spanish, "Racha actual 🔥", "Current streak 🔥"),
            font_size=T.TEXT_SM,
            font_weight=T.WEIGHT_SEMIBOLD,
            color=T.TEXT_PRIMARY,
            margin_bottom=T.SPACE_3,
        ),
        rx.text(
            AppState.user_streak.to_string() + " ",
            rx.cond(AppState.is_spanish, "días", "days"),
            font_size=T.TEXT_4XL,
            font_weight=T.WEIGHT_EXTRABOLD,
            color=T.TEXT_PRIMARY,
            line_height="1",
        ),
        rx.text(
            rx.cond(AppState.is_spanish, "¡Sigue así! 👋", "Keep it up! 👋"),
            font_size=T.TEXT_SM,
            color=T.TEXT_MUTED,
            margin_top="4px",
            margin_bottom=T.SPACE_4,
        ),
        margin_bottom=T.SPACE_5,
        padding_bottom=T.SPACE_5,
        border_bottom=f"1px solid {T.BORDER_SUBTLE}",
    )


def _right_plan() -> rx.Component:
    plan_es = [
        ("✅", "Funciones en Python",       "Lección 5",   True),
        ("○",  "Desafío: Calculadora",      "Intermedio",  False),
        ("○",  "Proyecto: Habit Tracker",   "Práctico",    False),
    ]
    plan_en = [
        ("✅", "Functions in Python",       "Lesson 5",    True),
        ("○",  "Challenge: Calculator",     "Intermediate", False),
        ("○",  "Project: Habit Tracker",    "Practical",   False),
    ]

    def plan_item(es_item, en_item) -> rx.Component:
        return rx.hstack(
            rx.box(
                rx.text("✓" if es_item[3] else "", font_size="11px", color="white", font_weight="bold"),
                width="20px",
                height="20px",
                border_radius="50%",
                background=T.SUCCESS if es_item[3] else "transparent",
                border=f"2px solid {T.SUCCESS if es_item[3] else T.BORDER}",
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
            ),
            rx.vstack(
                rx.text(
                    rx.cond(AppState.is_spanish, es_item[1], en_item[1]),
                    font_size=T.TEXT_SM,
                    color=T.TEXT_MUTED if es_item[3] else T.TEXT_PRIMARY,
                    text_decoration="line-through" if es_item[3] else "none",
                    white_space="nowrap",
                    overflow="hidden",
                    text_overflow="ellipsis",
                ),
                rx.text(
                    rx.cond(AppState.is_spanish, es_item[2], en_item[2]),
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
        plan_item(plan_es[0], plan_en[0]),
        plan_item(plan_es[1], plan_en[1]),
        plan_item(plan_es[2], plan_en[2]),
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
    return rx.box(
        rx.hstack(
            rx.text(
                rx.cond(AppState.is_spanish, "Desafío diario", "Daily challenge"),
                font_size=T.TEXT_SM, font_weight=T.WEIGHT_SEMIBOLD, color=T.TEXT_PRIMARY,
            ),
            rx.box(
                rx.text(
                    rx.cond(AppState.is_spanish, "Nuevo", "New"),
                    font_size=T.TEXT_XS, font_weight=T.WEIGHT_BOLD, color="white",
                ),
                background=T.BRAND,
                border_radius=T.RADIUS_FULL,
                padding=f"2px {T.SPACE_2}",
            ),
            justify="between", align="center", margin_bottom=T.SPACE_3,
        ),
        rx.box(
            rx.hstack(
                rx.text(
                    rx.cond(AppState.is_spanish, "Suma de números pares", "Sum of even numbers"),
                    font_size=T.TEXT_BASE, font_weight=T.WEIGHT_SEMIBOLD, color=T.TEXT_PRIMARY,
                ),
            ),
            rx.text(
                rx.cond(AppState.is_spanish, "Dificultad: ", "Difficulty: "),
                rx.text.span(
                    rx.cond(AppState.is_spanish, "Fácil", "Easy"),
                    color=T.SUCCESS, font_weight=T.WEIGHT_SEMIBOLD,
                ),
                font_size=T.TEXT_XS, color=T.TEXT_MUTED, margin="4px 0",
            ),
            rx.text(
                rx.cond(
                    AppState.is_spanish,
                    "Crea una función que reciba un número n y devuelva la suma de todos los números pares hasta n.",
                    "Create a function that receives a number n and returns the sum of all even numbers up to n.",
                ),
                font_size=T.TEXT_SM, color=T.TEXT_SECONDARY, line_height="1.5", margin_bottom=T.SPACE_3,
            ),
            rx.button(
                rx.cond(AppState.is_spanish, "▶ Resolver desafío", "▶ Solve challenge"),
                width="100%",
                background=T.BRAND,
                color="white",
                border_radius=T.RADIUS_MD,
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_SEMIBOLD,
                padding=f"{T.SPACE_2} 0",
                cursor="pointer",
                _hover={"background": T.BRAND_HOVER},
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
        _current_lesson_preview(),
        _projects_grid(),
        padding=T.SPACE_6,
        flex="1",
        min_width="0",
        overflow_y="auto",
    )

    right_panel = rx.box(
        _right_streak(),
        _right_plan(),
        _right_challenge(),
        _right_community(),
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
            right_panel,
            align="stretch",
            gap="0",
            min_height=f"calc(100vh - {T.TOPBAR_HEIGHT})",
        ),
    )
