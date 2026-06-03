"""
SKILLOGIC — Topbar Component
Search + theme/language toggle + notifications + avatar.
"""

import reflex as rx
from SKILLOGIC.state import AppState
from SKILLOGIC.state.progress_state import ProgressState
from SKILLOGIC.styles import theme as T


from SKILLOGIC.components.sidebar import sidebar

def topbar() -> rx.Component:
    """Top navigation bar fixed at the top of the main area."""

    search_placeholder = rx.cond(
        AppState.is_spanish,
        "Buscar lecciones, temas o desafíos...",
        "Search lessons, topics or challenges...",
    )

    return rx.box(
        # Mobile Menu Toggle with Drawer
        rx.drawer.root(
            rx.drawer.trigger(
                rx.box(
                    rx.icon("menu", size=24, color=T.TEXT_PRIMARY),
                    display=rx.breakpoints(initial="flex", lg="none"),
                    cursor="pointer",
                    padding=T.SPACE_2,
                    border_radius=T.RADIUS_MD,
                    _hover={"background": T.BG_HOVER},
                )
            ),
            rx.drawer.overlay(z_index="100", background_color="rgba(0,0,0,0.5)", backdrop_filter="blur(4px)"),
            rx.drawer.portal(
                rx.drawer.content(
                    sidebar(),
                    top="0",
                    bottom="0",
                    left="0",
                    width=T.SIDEBAR_WIDTH,
                    position="fixed",
                    z_index="101",
                    background="transparent",
                    outline="none",
                )
            ),
            direction="left",
        ),

        # Spacer
        rx.spacer(),

        # ── Theme toggle (🌙 dark / ☀️ light) ────────────────
        rx.button(
            AppState.toggle_theme_label,
            title=AppState.toggle_theme_title,
            background=T.BG_HOVER,
            border=f"1px solid {T.BORDER}",
            border_radius=T.RADIUS_FULL,
            padding=f"{T.SPACE_1} {T.SPACE_3}",
            font_size="16px",
            cursor="pointer",
            transition=f"all {T.EASE_FAST}",
            _hover={
                "background": T.BG_ELEVATED,
                "border_color": T.BORDER_STRONG,
                "transform": "scale(1.08)",
            },
            on_click=AppState.toggle_theme,
        ),

        # ── Language toggle (🇪🇸 ES / 🇬🇧 EN) ──────────────────
        rx.button(
            AppState.toggle_lang_label,
            title=AppState.toggle_lang_title,
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
            on_click=AppState.toggle_lang,
        ),

        # Streak badge (MVP Cleanup)
        # rx.box(
        # ...
        # ),

        # Notifications icon (MVP Cleanup)
        # rx.box(
        # ...
        # ),

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
