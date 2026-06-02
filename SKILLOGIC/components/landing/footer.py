import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.components.landing.helpers import t

def footer() -> rx.Component:
    """Simple footer for the landing page."""
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.text(t("© 2026 SKILLOGIC. Todos los derechos reservados.", "© 2026 SKILLOGIC. All rights reserved."), font_size=T.TEXT_SM, color=T.TEXT_MUTED),
                rx.text("•", font_size=T.TEXT_SM, color=T.TEXT_MUTED, opacity="0.5"),
                rx.link(t("Construido con Reflex", "Built with Reflex"), href="https://reflex.dev", is_external=True, font_size=T.TEXT_SM, color=T.TEXT_MUTED, opacity="0.6", text_decoration="none", _hover={"opacity": "1", "color": T.BRAND_LIGHT}, transition=f"all {T.EASE_BASE}"),
                gap="2",
                align="center",
            ),
            rx.spacer(),
            rx.hstack(
                rx.text(t("Términos", "Terms"), font_size=T.TEXT_SM, color=T.TEXT_MUTED, cursor="pointer", _hover={"color": T.TEXT_PRIMARY}),
                rx.text(t("Privacidad", "Privacy"), font_size=T.TEXT_SM, color=T.TEXT_MUTED, cursor="pointer", _hover={"color": T.TEXT_PRIMARY}),
                gap=T.SPACE_4,
            ),
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding=f"{T.SPACE_6} {T.SPACE_4}",
        ),
        border_top=f"1px solid {T.BORDER_SUBTLE}",
        background=T.BG_PRIMARY,
        margin_top=T.SPACE_4,
    )

