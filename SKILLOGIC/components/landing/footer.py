import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.components.landing.helpers import t

def footer() -> rx.Component:
    """Simple footer for the landing page."""
    return rx.box(
        rx.flex(
            rx.flex(
                rx.text(t("© 2026 SKILLOGIC. Todos los derechos reservados.", "© 2026 SKILLOGIC. All rights reserved."), font_size=T.TEXT_SM, color=T.TEXT_MUTED),
                rx.text("•", font_size=T.TEXT_SM, color=T.TEXT_MUTED, opacity="0.5"),
                rx.link(t("Construido con Reflex", "Built with Reflex"), id="my-footer-link", href="https://reflex.dev", is_external=True, font_size=T.TEXT_SM, color=T.TEXT_MUTED, text_decoration="none", _hover={"color": T.TEXT_PRIMARY}, transition=f"all {T.EASE_BASE}"),
                gap="2",
                align="center",
                flex_wrap="wrap",
                justify="center",
            ),
            rx.spacer(display=rx.breakpoints(initial="none", md="block")),
            rx.flex(
                rx.link(t("Términos", "Terms"), href="/terms", font_size=T.TEXT_SM, color=T.TEXT_MUTED, _hover={"color": T.TEXT_PRIMARY}, text_decoration="none"),
                rx.link(t("Privacidad", "Privacy"), href="/privacy", font_size=T.TEXT_SM, color=T.TEXT_MUTED, _hover={"color": T.TEXT_PRIMARY}, text_decoration="none"),
                rx.link(t("Cookies", "Cookies"), href="/cookies", font_size=T.TEXT_SM, color=T.TEXT_MUTED, _hover={"color": T.TEXT_PRIMARY}, text_decoration="none"),
                gap=T.SPACE_4,
                flex_wrap="wrap",
                justify="center",
            ),
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding=f"{T.SPACE_6} {T.SPACE_4}",
            direction=rx.breakpoints(initial="column-reverse", md="row"),
            align="center",
            gap=T.SPACE_4,
        ),
        border_top=f"1px solid {T.BORDER_SUBTLE}",
        background=T.BG_PRIMARY,
        margin_top=T.SPACE_4,
    )

