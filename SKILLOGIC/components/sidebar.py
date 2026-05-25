"""
SKILLOGIC — Sidebar Component
Navigation + user progress + streak calendar.
UI-only: reads from AppState, dispatches AppState events.
"""

import reflex as rx
from SKILLOGIC.state import AppState
from SKILLOGIC.styles import theme as T


def _nav_item(icon: str, label_es: str, label_en: str, route: str, nav_key: str) -> rx.Component:
    """Single navigation item with active state and hover effect."""
    label = rx.cond(AppState.is_spanish, label_es, label_en)
    is_active = AppState.active_nav == nav_key

    return rx.box(
        rx.text(icon, font_size="16px", line_height="1"),
        rx.text(
            label,
            font_size=T.TEXT_SM,
            font_weight=T.WEIGHT_MEDIUM,
        ),
        display="flex",
        align_items="center",
        gap=T.SPACE_3,
        padding=f"{T.SPACE_2} {T.SPACE_3}",
        border_radius=T.RADIUS_MD,
        color=rx.cond(is_active, "#a78bfa", T.TEXT_SECONDARY),
        background=rx.cond(is_active, T.BRAND_LIGHT, "transparent"),
        cursor="pointer",
        transition=f"all {T.EASE_FAST}",
        margin_bottom="2px",
        _hover={
            "background": T.BG_HOVER,
            "color": T.TEXT_PRIMARY,
        },
        on_click=[
            AppState.set_active_nav(nav_key),
            rx.redirect(route),
        ],
    )


def _streak_dot(label_es: str, label_en: str, active_var) -> rx.Component:
    """Single streak dot with day label."""
    return rx.vstack(
        rx.text(
            rx.cond(AppState.is_spanish, label_es, label_en),
            font_size="9px",
            color=T.TEXT_MUTED,
            font_weight=T.WEIGHT_SEMIBOLD,
            text_align="center",
        ),
        rx.box(
            width="20px",
            height="20px",
            border_radius="50%",
            background=rx.cond(active_var, T.STREAK, T.BG_HOVER),
            border=rx.cond(active_var, "none", f"1px solid {T.BORDER}"),
            box_shadow=rx.cond(active_var, f"0 0 6px {T.STREAK_GLOW}", "none"),
            margin="0 auto",
        ),
        spacing="1",
        align_items="center",
    )


def _streak_calendar() -> rx.Component:
    """Weekly streak calendar — static 7 days, reads AppState.streak_days[i] directly."""
    # ES / EN day names for each position (0=Mon ... 6=Sun)
    pairs = [
        ("L", "M"), ("M", "T"), ("M", "W"), ("J", "T"),
        ("V", "F"), ("S", "S"), ("D", "S"),
    ]
    dots = [
        _streak_dot(es, en, AppState.streak_days[i])
        for i, (es, en) in enumerate(pairs)
    ]
    return rx.grid(
        *dots,
        columns="7",
        gap=T.SPACE_1,
        margin_top=T.SPACE_2,
    )


def sidebar() -> rx.Component:
    """Full sidebar component."""

    # ── XP Progress bar
    xp_bar = rx.box(
        rx.box(
            height="100%",
            border_radius=T.RADIUS_FULL,
            background=f"linear-gradient(90deg, {T.BRAND}, #a855f7)",
            width=AppState.xp_percent.to_string() + "%",
            transition=f"width {T.EASE_SLOW}",
        ),
        height="6px",
        background=T.BG_HOVER,
        border_radius=T.RADIUS_FULL,
        overflow="hidden",
        margin=f"{T.SPACE_2} 0",
    )

    # ── Navigation items
    nav = rx.box(
        _nav_item("🏠", "Inicio",              "Home",          "/dashboard", "home"),
        _nav_item("🗺️", "Ruta de Aprendizaje", "Learning Path", "/dashboard", "path"),
        _nav_item("📖", "Lecciones",           "Lessons",       "/dashboard", "lessons"),
        _nav_item("📁", "Proyectos",           "Projects",      "/dashboard", "projects"),
        _nav_item("🎯", "Desafíos",            "Challenges",    "/dashboard", "challenges"),
        _nav_item("⌨️", "Code Lab",            "Code Lab",      "/dashboard", "codelab"),
        _nav_item("👥", "Comunidad",           "Community",     "/dashboard", "community"),
        _nav_item("📚", "Recursos",            "Resources",     "/dashboard", "resources"),
        padding=f"{T.SPACE_3} {T.SPACE_2}",
    )

    # ── Progress section
    progress_section = rx.box(
        rx.text(
            rx.cond(AppState.is_spanish, "Tu Progreso", "Your Progress"),
            font_size=T.TEXT_XS,
            font_weight=T.WEIGHT_SEMIBOLD,
            color=T.TEXT_MUTED,
            text_transform="uppercase",
            letter_spacing="0.8px",
            margin_bottom=T.SPACE_3,
        ),
        rx.hstack(
            rx.box(
                rx.text(
                    AppState.user_level.to_string(),
                    color="white",
                    font_size=T.TEXT_XS,
                    font_weight=T.WEIGHT_BOLD,
                ),
                width="26px",
                height="26px",
                border_radius=T.RADIUS_FULL,
                background=T.BRAND,
                display="flex",
                align_items="center",
                justify_content="center",
                box_shadow=T.SHADOW_BRAND,
                flex_shrink="0",
            ),
            rx.text(
                AppState.user_xp.to_string() + " / " + AppState.user_xp_to_next.to_string() + " XP",
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_SEMIBOLD,
                color=T.TEXT_SECONDARY,
            ),
            justify="between",
            align="center",
        ),
        xp_bar,
        rx.hstack(
            rx.text("🏆", font_size="14px"),
            rx.text(
                rx.cond(AppState.is_spanish, "Rango", "Rank"),
                font_size=T.TEXT_XS,
                color=T.TEXT_MUTED,
            ),
            rx.text(
                AppState.user_rank,
                font_size=T.TEXT_XS,
                font_weight=T.WEIGHT_SEMIBOLD,
                color=T.TEXT_SECONDARY,
                margin_left="auto",
            ),
            align="center",
            gap=T.SPACE_2,
        ),
        padding=f"{T.SPACE_3} {T.SPACE_4}",
        border_top=f"1px solid {T.BORDER_SUBTLE}",
    )

    # ── Streak section
    streak_section = rx.box(
        rx.text(
            rx.cond(AppState.is_spanish, "Racha Actual", "Current Streak"),
            font_size=T.TEXT_XS,
            font_weight=T.WEIGHT_SEMIBOLD,
            color=T.TEXT_MUTED,
            text_transform="uppercase",
            letter_spacing="0.8px",
            margin_bottom=T.SPACE_2,
        ),
        rx.hstack(
            rx.text("🔥", font_size="18px"),
            rx.text(
                AppState.user_streak.to_string(),
                font_size=T.TEXT_LG,
                font_weight=T.WEIGHT_BOLD,
                color=T.STREAK,
            ),
            rx.text(
                rx.cond(AppState.is_spanish, "días", "days"),
                font_size=T.TEXT_XS,
                color=T.TEXT_MUTED,
                margin_left=T.SPACE_1,
                align_self="end",
                padding_bottom="3px",
            ),
            align="center",
            gap=T.SPACE_1,
        ),
        _streak_calendar(),
        padding=f"{T.SPACE_3} {T.SPACE_4}",
        border_top=f"1px solid {T.BORDER_SUBTLE}",
    )

    # ── Objective widget
    objective = rx.box(
        rx.text(
            rx.cond(AppState.is_spanish, "Próximo objetivo", "Next objective"),
            font_size=T.TEXT_XS,
            color=T.TEXT_MUTED,
            margin_bottom=T.SPACE_1,
        ),
        rx.text(
            rx.cond(AppState.is_spanish, "Completa 3 ejercicios", "Complete 3 exercises"),
            font_size=T.TEXT_SM,
            font_weight=T.WEIGHT_SEMIBOLD,
            color=T.TEXT_PRIMARY,
            margin_bottom=T.SPACE_2,
        ),
        rx.box(
            rx.box(
                height="100%",
                width="33%",
                background=T.BRAND,
                border_radius=T.RADIUS_FULL,
            ),
            height="4px",
            background=T.BG_HOVER,
            border_radius=T.RADIUS_FULL,
            overflow="hidden",
        ),
        padding=f"{T.SPACE_3} {T.SPACE_4}",
        border_top=f"1px solid {T.BORDER_SUBTLE}",
    )

    # ── Community CTA
    cta = rx.box(
        rx.text(
            rx.cond(AppState.is_spanish, "¿Necesitas ayuda?", "Need help?"),
            font_size=T.TEXT_XS,
            font_weight=T.WEIGHT_SEMIBOLD,
            color="#a78bfa",
            margin_bottom="4px",
        ),
        rx.text(
            rx.cond(AppState.is_spanish, "Únete a nuestra comunidad", "Join our community"),
            font_size=T.TEXT_XS,
            color=T.TEXT_MUTED,
            margin_bottom=T.SPACE_2,
        ),
        rx.button(
            rx.cond(AppState.is_spanish, "Ir a la comunidad →", "Go to community →"),
            width="100%",
            background=T.BRAND,
            color="white",
            border_radius=T.RADIUS_SM,
            font_size=T.TEXT_XS,
            font_weight=T.WEIGHT_SEMIBOLD,
            padding=f"{T.SPACE_2} {T.SPACE_3}",
            cursor="pointer",
            _hover={"background": T.BRAND_HOVER},
        ),
        margin=f"{T.SPACE_3} {T.SPACE_4} {T.SPACE_4}",
        padding=T.SPACE_3,
        background=f"linear-gradient(135deg, {T.BRAND_LIGHT}, rgba(249,115,22,0.08))",
        border=f"1px solid {T.BRAND_MEDIUM}",
        border_radius=T.RADIUS_LG,
    )

    return rx.box(
        # Logo
        rx.hstack(
            rx.box(
                rx.text("⚡", font_size="16px"),
                width="32px",
                height="32px",
                background=f"linear-gradient(135deg, {T.BRAND}, #a855f7)",
                border_radius=T.RADIUS_MD,
                display="flex",
                align_items="center",
                justify_content="center",
                box_shadow=T.SHADOW_BRAND,
                flex_shrink="0",
            ),
            rx.text(
                "SKILLOGIC",
                font_size=T.TEXT_MD,
                font_weight=T.WEIGHT_BOLD,
                letter_spacing="-0.3px",
                # Dark: white→purple on dark bg. Light: near-black→purple on light bg.
                background=rx.cond(
                    AppState.is_dark,
                    "linear-gradient(135deg, #E6EDF3, #a78bfa)",
                    "linear-gradient(135deg, #1F2328, #7C3AED)",
                ),
                background_clip="text",
                webkit_background_clip="text",
                webkit_text_fill_color="transparent",
            ),
            align="center",
            gap=T.SPACE_2,
            padding=f"{T.SPACE_5} {T.SPACE_4}",
            border_bottom=f"1px solid {T.BORDER_SUBTLE}",
        ),
        nav,
        progress_section,
        streak_section,
        objective,
        cta,
        width=T.SIDEBAR_WIDTH,
        min_height="100vh",
        background=T.BG_SECONDARY,
        border_right=f"1px solid {T.BORDER}",
        display="flex",
        flex_direction="column",
        position="fixed",
        top="0",
        left="0",
        z_index="10",
        overflow_y="auto",
        overflow_x="hidden",
    )
