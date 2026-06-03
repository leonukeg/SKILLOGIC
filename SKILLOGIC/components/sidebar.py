"""
SKILLOGIC — Sidebar Component
Navigation + user progress + streak calendar.
UI-only: reads from AppState, dispatches AppState events.
"""

import reflex as rx
from SKILLOGIC.state import AppState
from SKILLOGIC.state.auth_state import AuthState
from SKILLOGIC.state.progress_state import ProgressState
from SKILLOGIC.styles import theme as T


def _nav_item(icon: str, label_es: str, label_en: str, route: str, nav_key: str) -> rx.Component:
    """Single navigation item with active state and hover effect."""
    label = rx.cond(AppState.is_spanish, label_es, label_en)
    is_active = AppState.active_nav == nav_key

    return rx.box(
        rx.icon(tag=icon, size=16),
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
    """Weekly streak calendar — visual based on ProgressState.streak_days."""
    pairs = [
        ("L", "M"), ("M", "T"), ("M", "W"), ("J", "T"),
        ("V", "F"), ("S", "S"), ("D", "S"),
    ]
    dots = [
        _streak_dot(es, en, ProgressState.streak_days > i)
        for i, (es, en) in enumerate(pairs)
    ]
    return rx.grid(
        *dots,
        columns="7",
        gap=T.SPACE_1,
        margin_top=T.SPACE_2,
        width="100%",
    )


def _objective_widget() -> rx.Component:
    """Componente dinámico de objetivos de gamificación."""
    completed_count = ProgressState.completed_katas.length()
    
    # Próximo objetivo: si es 0 -> resolver 1, si es < 3 -> resolver 3, si es < 8 -> resolver 8
    target = rx.cond(
        completed_count == 0,
        1,
        rx.cond(completed_count < 3, 3, 8)
    )
    
    objective_text_es = rx.cond(
        completed_count == 0,
        "Resuelve tu primer Kata",
        rx.cond(
            completed_count < 3,
            "Completa 3 Katas",
            rx.cond(completed_count < 8, "Completa todos los Katas", "¡Maestro de Katas!")
        )
    )
    
    objective_text_en = rx.cond(
        completed_count == 0,
        "Solve your first Kata",
        rx.cond(
            completed_count < 3,
            "Complete 3 Katas",
            rx.cond(completed_count < 8, "Complete all Katas", "Katas Master!")
        )
    )
    
    objective_text = rx.cond(AppState.is_spanish, objective_text_es, objective_text_en)
    
    # Calcular porcentaje para la barra de progreso
    percent = rx.cond(
        target > 0,
        ((completed_count * 100) / target).to(int),
        100
    )
    
    return rx.box(
        rx.text(
            rx.cond(AppState.is_spanish, "Próximo objetivo", "Next objective"),
            font_size=T.TEXT_XS,
            color=T.TEXT_MUTED,
            margin_bottom=T.SPACE_1,
        ),
        rx.text(
            objective_text,
            font_size=T.TEXT_SM,
            font_weight=T.WEIGHT_SEMIBOLD,
            color=T.TEXT_PRIMARY,
            margin_bottom=T.SPACE_2,
        ),
        rx.box(
            rx.box(
                height="100%",
                width=percent.to_string() + "%",
                background=T.BRAND,
                border_radius=T.RADIUS_FULL,
                transition=f"width {T.EASE_SLOW}",
            ),
            height="4px",
            background=T.BG_HOVER,
            border_radius=T.RADIUS_FULL,
            overflow="hidden",
        ),
        padding=f"{T.SPACE_3} {T.SPACE_4}",
        border_top=f"1px solid {T.BORDER_SUBTLE}",
    )


def sidebar() -> rx.Component:
    """Full sidebar component."""

    # ── XP Progress bar
    xp_bar = rx.box(
        rx.box(
            height="100%",
            border_radius=T.RADIUS_FULL,
            background=f"linear-gradient(90deg, {T.BRAND}, #a855f7)",
            width=ProgressState.xp_progress_percent.to_string() + "%",
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
        _nav_item("home",      "Inicio",              "Home",          "/dashboard", "home"),
        _nav_item("book-open", "Lecciones",           "Lessons",       "/dashboard", "lessons"),
        _nav_item("swords",    "Katas",               "Katas",         "/katas",     "katas"),
        
        # Settings menu for master users
        rx.cond(
            AuthState.is_master,
            rx.accordion.root(
                rx.accordion.item(
                    header=rx.hstack(
                        rx.icon(tag="settings", size=16),
                        rx.text(rx.cond(AppState.is_spanish, "Ajustes", "Settings"), font_size=T.TEXT_SM, font_weight=T.WEIGHT_MEDIUM),
                        align="center", gap=T.SPACE_3, padding=f"{T.SPACE_2} {T.SPACE_3}",
                        color=T.TEXT_SECONDARY, _hover={"color": T.TEXT_PRIMARY},
                    ),
                    content=rx.vstack(
                        _nav_item("users", "Usuarios", "Users", "/admin", "admin_users"),
                        padding_left=T.SPACE_4,
                    ),
                    value="settings",
                    border_bottom="none",
                ),
                width="100%", collapsible=True, margin_top=T.SPACE_4, border_top=f"1px solid {T.BORDER_SUBTLE}", padding_top=T.SPACE_2,
                variant="ghost",
                color_scheme="gray",
            )
        ),
        
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
                    ProgressState.level.to_string(),
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
                ProgressState.xp.to_string() + " / " + ProgressState.xp_to_next_level.to_string() + " XP",
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_SEMIBOLD,
                color=T.TEXT_SECONDARY,
            ),
            justify="between",
            align="center",
        ),
        xp_bar,
        rx.hstack(
            rx.icon(tag="trophy", size=14, color=T.TEXT_MUTED),
            rx.text(
                rx.cond(AppState.is_spanish, "Rango", "Rank"),
                font_size=T.TEXT_XS,
                color=T.TEXT_MUTED,
            ),
            rx.text(
                rx.cond(
                    ProgressState.xp == 0, "Novato", 
                    rx.cond(ProgressState.level < 5, "Explorer", 
                    rx.cond(ProgressState.level < 10, "Pioneer", "Master"))
                ),
                font_size=T.TEXT_XS,
                font_weight=T.WEIGHT_SEMIBOLD,
                color=T.TEXT_SECONDARY,
                margin_left="auto",
            ),
            align="center",
            gap=T.SPACE_2,
            margin_bottom=T.SPACE_4,
        ),
        
        # DISTRIBUCIÓN DE XP
        rx.box(
            rx.text(
                rx.cond(AppState.is_spanish, "DISTRIBUCIÓN", "XP DISTRIBUTION"),
                font_size="9px", font_weight=T.WEIGHT_BOLD, color=T.TEXT_MUTED, letter_spacing="1px", margin_bottom=T.SPACE_2
            ),
            rx.vstack(
                rx.hstack(
                    rx.icon(tag="book-open", size=12, color=T.INFO),
                    rx.text(rx.cond(AppState.is_spanish, "Teoría", "Theory"), font_size="10px", color=T.TEXT_SECONDARY),
                    rx.spacer(),
                    rx.text(ProgressState.lessons_xp_earned.to_string() + " XP", font_size="10px", font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
                    width="100%", align="center"
                ),
                rx.hstack(
                    rx.icon(tag="code", size=12, color=T.SUCCESS),
                    rx.text("Katas", font_size="10px", color=T.TEXT_SECONDARY),
                    rx.spacer(),
                    rx.text(ProgressState.katas_xp_earned.to_string() + " XP", font_size="10px", font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
                    width="100%", align="center"
                ),
                rx.hstack(
                    rx.icon(tag="flame", size=12, color="#f97316"),
                    rx.text(rx.cond(AppState.is_spanish, "Racha", "Streak"), font_size="10px", color=T.TEXT_SECONDARY),
                    rx.spacer(),
                    rx.text(ProgressState.streak_xp_earned.to_string() + " XP", font_size="10px", font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
                    width="100%", align="center"
                ),
                width="100%",
                spacing="1",
            ),
            background=T.BG_ELEVATED,
            padding=T.SPACE_3,
            border_radius=T.RADIUS_MD,
            border=f"1px solid {T.BORDER}",
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
            rx.icon(tag="flame", size=18, color=T.STREAK),
            rx.text(
                ProgressState.streak_days.to_string(),
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
                rx.icon(tag="zap", size=16, color="white"),
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
                # Dark: gradient clip (premium look). Light: solid dark text (always readable).
                color=rx.cond(AppState.is_dark, "transparent", "#1F2328"),
                background=rx.cond(
                    AppState.is_dark,
                    "linear-gradient(135deg, #E6EDF3, #a78bfa)",
                    "none",
                ),
                background_clip=rx.cond(AppState.is_dark, "text", "initial"),
                webkit_background_clip=rx.cond(AppState.is_dark, "text", "initial"),
                webkit_text_fill_color=rx.cond(AppState.is_dark, "transparent", "#1F2328"),
            ),
            align="center",
            gap=T.SPACE_2,
            padding=f"{T.SPACE_5} {T.SPACE_4}",
            border_bottom=f"1px solid {T.BORDER_SUBTLE}",
        ),
        nav,
        progress_section,
        streak_section,
        _objective_widget(),
        cta,
        width=T.SIDEBAR_WIDTH,
        min_height="100vh",
        background=T.BG_SECONDARY,
        border_right=f"1px solid {T.BORDER}",
        flex_direction="column",
        overflow_y="auto",
        overflow_x="hidden",
    )
