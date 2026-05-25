"""
SKILLOGIC — App Layout (base shell)
Wraps authenticated pages with sidebar + topbar.
All authenticated pages use this layout via rx.layout() or direct composition.
"""

import reflex as rx
from SKILLOGIC.components.sidebar import sidebar
from SKILLOGIC.components.topbar import topbar
from SKILLOGIC.styles import theme as T


def app_layout(*page_content: rx.Component) -> rx.Component:
    """
    Base layout for all authenticated pages.
    Sidebar (fixed left) + main area (topbar + scrollable content).
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
        display="flex",
        min_height="100vh",
        background=T.BG_PRIMARY,
        font_family=T.FONT_BODY,
    )
