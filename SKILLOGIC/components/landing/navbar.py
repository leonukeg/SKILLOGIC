import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.components.landing.helpers import t

class NavbarState(rx.State):
    """Local state for the landing navbar mobile menu."""
    is_open: bool = False

    def toggle_menu(self):
        self.is_open = not self.is_open
        
    def close_menu(self):
        self.is_open = False

def landing_navbar() -> rx.Component:
    """Navbar for the landing page with responsive mobile menu."""
    return rx.box(
        rx.flex(
            # Logo
            rx.hstack(
                rx.flex(
                    rx.icon(tag="zap", size=18, color="white"),
                    width="36px", height="36px",
                    background=f"linear-gradient(135deg, {T.BRAND}, #a855f7)",
                    border_radius=T.RADIUS_MD,
                    box_shadow=T.SHADOW_BRAND,
                    align="center", justify="center",
                ),
                rx.text(
                    "SKILLOGIC",
                    font_size=T.TEXT_LG,
                    font_weight=T.WEIGHT_EXTRABOLD,
                    letter_spacing="-0.3px",
                    color=T.TEXT_PRIMARY,
                ),
                align="center", gap=T.SPACE_2,
            ),
            
            # Auth Buttons & Lang Toggle (Desktop)
            rx.flex(
                rx.button(
                    AppState.toggle_lang_label,
                    on_click=AppState.toggle_lang,
                    variant="ghost",
                    color_scheme="gray",
                    size="2",
                    title=AppState.toggle_lang_title,
                    font_weight=T.WEIGHT_BOLD,
                ),
                rx.button(
                    t("Iniciar sesión", "Log in"),
                    on_click=rx.redirect("/login"),
                    variant="ghost",
                    color=T.TEXT_SECONDARY,
                    _hover={"color": T.TEXT_PRIMARY},
                    font_weight=T.WEIGHT_SEMIBOLD,
                ),
                rx.button(
                    t("Comenzar gratis", "Start for free"),
                    on_click=rx.redirect("/register"),
                    variant="solid",
                    style={
                        "background_color": f"{T.BRAND} !important",
                        "color": "white !important",
                    },
                    border_radius=T.RADIUS_MD,
                    box_shadow=T.SHADOW_BRAND,
                    _hover={"background_color": f"{T.BRAND_HOVER} !important"},
                    font_weight=T.WEIGHT_SEMIBOLD,
                    padding=f"{T.SPACE_2} {T.SPACE_4}",
                ),
                gap=T.SPACE_4,
                align="center",
                display=rx.breakpoints(initial="none", md="flex"),
            ),
            
            # Hamburger Menu Button (Mobile)
            rx.box(
                rx.icon_button(
                    rx.icon(tag=rx.cond(NavbarState.is_open, "x", "menu")),
                    on_click=NavbarState.toggle_menu,
                    variant="ghost",
                    color=T.TEXT_PRIMARY,
                    size="3",
                ),
                display=rx.breakpoints(initial="block", md="none"),
            ),
            
            width="100%",
            padding=rx.breakpoints(initial=f"{T.SPACE_4}", md=f"{T.SPACE_4} {T.SPACE_8}"),
            max_width="1200px",
            margin="0 auto",
            align="center",
            justify="between",
        ),
        
        # Mobile Menu Dropdown
        rx.cond(
            NavbarState.is_open,
            rx.box(
                rx.vstack(
                    rx.button(
                        AppState.toggle_lang_label,
                        on_click=[AppState.toggle_lang, NavbarState.close_menu],
                        variant="ghost",
                        color_scheme="gray",
                        size="3",
                        title=AppState.toggle_lang_title,
                        font_weight=T.WEIGHT_BOLD,
                        width="100%",
                    ),
                    rx.button(
                        t("Iniciar sesión", "Log in"),
                        on_click=[rx.redirect("/login"), NavbarState.close_menu],
                        variant="ghost",
                        color=T.TEXT_SECONDARY,
                        _hover={"color": T.TEXT_PRIMARY},
                        font_weight=T.WEIGHT_SEMIBOLD,
                        size="3",
                        width="100%",
                    ),
                    rx.button(
                        t("Comenzar gratis", "Start for free"),
                        on_click=[rx.redirect("/register"), NavbarState.close_menu],
                        variant="solid",
                        style={
                            "background_color": f"{T.BRAND} !important",
                            "color": "white !important",
                        },
                        border_radius=T.RADIUS_MD,
                        box_shadow=T.SHADOW_BRAND,
                        font_weight=T.WEIGHT_SEMIBOLD,
                        size="3",
                        width="100%",
                    ),
                    gap=T.SPACE_4,
                    width="100%",
                    align="center",
                    padding=T.SPACE_6,
                ),
                position="absolute",
                top="100%",
                left="0",
                width="100%",
                background=T.BG_PRIMARY,
                border_bottom=f"1px solid {T.BORDER}",
                box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1)",
                z_index="50",
                display=rx.breakpoints(initial="block", md="none"),
                animation="fadeIn 0.2s ease-out",
            ),
        ),
        
        position="relative",
        width="100%",
        z_index="40",
    )
