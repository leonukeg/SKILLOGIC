"""
SKILLOGIC — App Layout (base shell)
Wraps authenticated pages with sidebar + topbar.

CRITICAL: The outermost rx.box carries data_theme=AppState.theme.
This attribute triggers the CSS custom property overrides defined
in assets/theme.css, making all var(--token) values switch
automatically when the user toggles the theme.
"""

import reflex as rx
from SKILLOGIC.state import AppState
from SKILLOGIC.components.sidebar import sidebar
from SKILLOGIC.components.topbar import topbar
from SKILLOGIC.styles import theme as T


def app_layout(*page_content: rx.Component) -> rx.Component:
    """
    Base layout for all authenticated pages.
    Sidebar (fixed left) + main area (topbar + scrollable content).
    data_theme drives the CSS custom property theme switch.
    """
    return rx.box(
        sidebar(),
        rx.box(
            topbar(),
            rx.box(
                *page_content,
                flex="1",
                overflow_y="auto",
                overflow_x="hidden",
            ),
            margin_left=T.SIDEBAR_WIDTH,
            display="flex",
            flex_direction="column",
            min_height="100vh",
        ),
        # ── Theme attribute — THIS is what drives dark/light CSS vars ──
        data_theme=AppState.theme,
        display="flex",
        min_height="100vh",
        background=T.BG_PRIMARY,
        font_family=T.FONT_BODY,
    )
