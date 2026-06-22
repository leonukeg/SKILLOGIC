import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.utils.mailer import send_newsletter_promo_email

class NewsletterState(rx.State):
    email: str = ""
    is_loading: bool = False
    is_success: bool = False
    error_message: str = ""

    @rx.event
    async def subscribe(self, form_data: dict):
        self.is_loading = True
        self.error_message = ""
        self.is_success = False
        yield
        
        email = form_data.get("email", "").strip()
        if not email or "@" not in email:
            self.error_message = "Por favor ingresa un email válido."
            self.is_loading = False
            return
            
        try:
            result = send_newsletter_promo_email(email)
            if result:
                self.is_success = True
                self.email = ""
            else:
                self.error_message = "Hubo un problema. Intenta nuevamente."
        except Exception as e:
            self.error_message = "Hubo un error de conexión."
            print(e)
        finally:
            self.is_loading = False

def newsletter_banner() -> rx.Component:
    """Fixed banner that appears when scrolled 50%"""
    banner = rx.box(
        rx.box(
            rx.flex(
                rx.vstack(
                    rx.text("🔥 Únete al Newsletter", font_weight=T.WEIGHT_BOLD, color="white", font_size=T.TEXT_LG),
                    rx.text("Tips de Python y nuevos Katas cada semana.", color="rgba(255,255,255,0.7)", font_size=T.TEXT_SM),
                    align="start",
                    spacing="0"
                ),
                rx.spacer(),
                rx.cond(
                    NewsletterState.is_success,
                    rx.hstack(
                        rx.icon(tag="circle-check", color=T.SUCCESS),
                        rx.text("¡Suscrito con éxito! Revisa tu correo.", color="white", font_weight=T.WEIGHT_BOLD)
                    ),
                    rx.form(
                        rx.hstack(
                            rx.input(
                                name="email",
                                placeholder="tu@email.com",
                                type="email",
                                bg="rgba(255,255,255,0.05)",
                                border="1px solid rgba(255,255,255,0.1)",
                                color="white",
                                _placeholder={"color": "rgba(255,255,255,0.4)"},
                                required=True,
                                outline="none",
                                _focus={"border_color": T.BRAND}
                            ),
                            rx.button(
                                "Suscribirme",
                                type="submit",
                                loading=NewsletterState.is_loading,
                                bg=T.BRAND,
                                color="white",
                                _hover={"bg": "#8B5CF6"},
                                border_radius=T.RADIUS_MD
                            )
                        ),
                        on_submit=NewsletterState.subscribe
                    )
                ),
                align="center",
                width="100%",
                flex_direction=rx.breakpoints(initial="column", md="row"),
                gap="4"
            ),
            rx.cond(
                NewsletterState.error_message != "",
                rx.text(NewsletterState.error_message, color=T.ERROR, font_size=T.TEXT_XS, margin_top="2", text_align="right")
            ),
            bg="rgba(15, 23, 42, 0.8)", # Slate 900 con opacidad
            backdrop_filter="blur(16px)",
            padding=T.SPACE_4,
            border_radius=T.RADIUS_LG,
            box_shadow="0 10px 40px rgba(0,0,0,0.5)",
            border="1px solid rgba(255,255,255,0.1)",
            width="100%",
            max_width="800px",
            margin="0 auto"
        ),
        id="newsletter-banner",
        position="fixed",
        bottom="-150px", # Hidden initially
        left="0",
        right="0",
        z_index="50",
        padding="0 20px",
        transition="all 0.6s cubic-bezier(0.16, 1, 0.3, 1)", # Smooth ease out
        opacity="0",
        pointer_events="none", # To prevent clicks when hidden
    )
    
    # Custom JS to toggle the banner at 50% scroll
    script = rx.script("""
        window.addEventListener('scroll', () => {
            const banner = document.getElementById('newsletter-banner');
            if (banner) {
                const scrollPosition = window.scrollY;
                const windowHeight = window.innerHeight;
                const documentHeight = document.body.scrollHeight;
                
                // Show if scrolled more than 50% of the total scrollable area
                if (scrollPosition > (documentHeight - windowHeight) * 0.5) {
                    banner.style.bottom = '24px';
                    banner.style.opacity = '1';
                    banner.style.pointerEvents = 'auto';
                } else {
                    banner.style.bottom = '-150px';
                    banner.style.opacity = '0';
                    banner.style.pointerEvents = 'none';
                }
            }
        });
    """)
    
    return rx.fragment(banner, script)
