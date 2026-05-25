"""
SKILLOGIC — Topbar Component
Search + theme/language toggle + notifications + avatar.
"""

import reflex as rx
from SKILLOGIC.state import AppState
from SKILLOGIC.styles import theme as T


def topbar() -> rx.Component:
    """Top navigation bar fixed at the top of the main area."""

    search_placeholder = rx.cond(
        AppState.is_spanish,
        "Buscar lecciones, temas o desafíos...",
        "Search lessons, topics or challenges...",
    )

    return rx.box(
        # Search bar
        rx.box(
            rx.el.input(
                placeholder=search_placeholder,
                background=T.BG_HOVER,
                border=f"1px solid {T.BORDER}",
                border_radius=T.RADIUS_MD,
                color=T.TEXT_PRIMARY,
                font_size=T.TEXT_SM,
                padding=f"0 {T.SPACE_8} 0 {T.SPACE_8}",
                height="36px",
                width="100%",
                outline="none",
                font_family=T.FONT_BODY,
                _placeholder={"color": T.TEXT_MUTED},
                _focus={
                    "border_color": T.BRAND,
                    "box_shadow": f"0 0 0 3px {T.BRAND_LIGHT}",
                },
            ),
            # Search icon
            rx.text(
                "🔍",
                position="absolute",
                left=T.SPACE_3,
                top="50%",
                transform="translateY(-50%)",
                font_size="12px",
                pointer_events="none",
                color=T.TEXT_MUTED,
            ),
            # Keyboard shortcut badge
            rx.box(
                rx.text("⌘K", font_size="10px", color=T.TEXT_MUTED),
                position="absolute",
                right=T.SPACE_3,
                top="50%",
                transform="translateY(-50%)",
                background=T.BG_SECONDARY,
                border=f"1px solid {T.BORDER}",
                border_radius="4px",
                padding="2px 5px",
                pointer_events="none",
            ),
            position="relative",
            flex="1",
            max_width="420px",
        ),

        # Spacer
        rx.spacer(),

        # ── Theme + Language toggle (one button, one action) ──
        rx.button(
            AppState.toggle_label,
            title=AppState.toggle_title,
            background=T.BG_HOVER,
            border=f"1px solid {T.BORDER}",
            border_radius=T.RADIUS_FULL,
            padding=f"{T.SPACE_1} {T.SPACE_3}",
            font_size=T.TEXT_SM,
            font_weight=T.WEIGHT_SEMIBOLD,
            color=T.TEXT_SECONDARY,
            cursor="pointer",
            transition=f"all {T.EASE_FAST}",
            _hover={
                "background": T.BG_ELEVATED,
                "color": T.TEXT_PRIMARY,
                "border_color": T.BORDER_STRONG,
            },
            on_click=AppState.toggle_theme_and_lang,
        ),

        # Streak badge
        rx.box(
            rx.text("🔥"),
            rx.text(
                AppState.user_streak.to_string() + " ",
                rx.cond(AppState.is_spanish, "días", "days"),
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_SEMIBOLD,
                color=T.STREAK,
            ),
            display="flex",
            align_items="center",
            gap=T.SPACE_1,
            background=T.STREAK_LIGHT,
            border=f"1px solid rgba(249, 115, 22, 0.3)",
            border_radius=T.RADIUS_FULL,
            padding=f"{T.SPACE_1} {T.SPACE_3}",
        ),

        # Notifications icon
        rx.box(
            rx.text("🔔", font_size="16px"),
            rx.box(
                width="7px",
                height="7px",
                background=T.BRAND,
                border_radius="50%",
                border=f"1.5px solid {T.BG_SECONDARY}",
                position="absolute",
                top="6px",
                right="6px",
            ),
            width="36px",
            height="36px",
            border_radius=T.RADIUS_MD,
            display="flex",
            align_items="center",
            justify_content="center",
            color=T.TEXT_SECONDARY,
            cursor="pointer",
            position="relative",
            transition=f"background {T.EASE_FAST}",
            _hover={"background": T.BG_HOVER},
        ),

        # User avatar
        rx.box(
            rx.text(
                AppState.user_initials,
                font_size=T.TEXT_SM,
                font_weight=T.WEIGHT_BOLD,
                color="white",
            ),
            width="34px",
            height="34px",
            border_radius="50%",
            background=f"linear-gradient(135deg, {T.BRAND}, #a855f7)",
            display="flex",
            align_items="center",
            justify_content="center",
            border=f"2px solid {T.BORDER}",
            cursor="pointer",
            transition=f"border-color {T.EASE_FAST}",
            _hover={"border_color": T.BRAND},
            on_click=AppState.logout,
            title=rx.cond(AppState.is_spanish, "Cerrar sesión", "Sign out"),
        ),

        # Topbar container
        height=T.TOPBAR_HEIGHT,
        background=T.BG_SECONDARY,
        border_bottom=f"1px solid {T.BORDER}",
        display="flex",
        align_items="center",
        gap=T.SPACE_3,
        padding=f"0 {T.SPACE_6}",
        position="sticky",
        top="0",
        z_index="10",
    )
