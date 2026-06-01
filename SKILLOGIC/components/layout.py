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
                rx.box(
                    *page_content,
                    flex="1",
                ),
                # Footer sutil
                rx.hstack(
                    rx.text("Crafted by", color=T.TEXT_MUTED, font_size="11px"),
                    rx.link(
                        "leonukeg",
                        href="https://leonukeg.github.io/leonukeg-portfolio/",
                        is_external=True,
                        color=T.BRAND,
                        font_size="11px",
                        font_weight=T.WEIGHT_MEDIUM,
                        text_decoration="none",
                        _hover={"opacity": 0.8}
                    ),
                    rx.text("•", color=T.BORDER, font_size="10px"),
                    rx.text("Powered by", color=T.TEXT_MUTED, font_size="11px"),
                    rx.link(
                        rx.hstack(
                            rx.icon(tag="zap", size=12, color=T.TEXT_MUTED),
                            rx.text("Reflex", color=T.TEXT_MUTED, font_size="11px", font_weight=T.WEIGHT_MEDIUM),
                            spacing="1",
                            align="center"
                        ),
                        href="https://reflex.dev/",
                        is_external=True,
                        text_decoration="none",
                        _hover={"opacity": 0.8}
                    ),
                    justify="center",
                    align="center",
                    spacing="2",
                    padding_y=T.SPACE_6,
                    padding_x=T.SPACE_8,
                    width="100%",
                ),
                flex="1",
                overflow_y="auto",
                overflow_x="hidden",
                display="flex",
                flex_direction="column",
            ),
            margin_left=rx.breakpoints(initial="0", lg=T.SIDEBAR_WIDTH),
            width=rx.breakpoints(initial="100%", lg=f"calc(100% - {T.SIDEBAR_WIDTH})"),
            display="flex",
            flex_direction="column",
            min_height="100vh",
        ),
        # ── Theme attribute — THIS is what drives dark/light CSS vars ──
        data_theme=AppState.theme,
        display="flex",
        min_height="100vh",
        width="100%",
        background=T.BG_PRIMARY,
        font_family=T.FONT_BODY,
    )
