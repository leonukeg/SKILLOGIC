import reflex as rx
from SKILLOGIC.state.update_password_state import UpdatePasswordState
from SKILLOGIC.styles import theme as T

def update_password_page() -> rx.Component:
    """Página de reseteo de contraseña segura."""
    return rx.center(
        # Script mágico para convertir #access_token de Supabase en ?access_token visible para Python
        rx.script(
            """
            if (window.location.hash && window.location.hash.includes("access_token=")) {
                window.location.replace(
                    window.location.pathname + "?" + window.location.hash.substring(1)
                );
            }
            """
        ),
        rx.box(
            rx.vstack(
                # Logo
                rx.hstack(
                    rx.box(
                        rx.icon(tag="zap", size=24, color="white"),
                        width="48px",
                        height="48px",
                        background=f"linear-gradient(135deg, {T.BRAND}, #a855f7)",
                        border_radius=T.RADIUS_LG,
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        box_shadow=T.SHADOW_BRAND,
                    ),
                    rx.text(
                        "SKILLOGIC",
                        font_size=T.TEXT_XL,
                        font_weight=T.WEIGHT_BOLD,
                        letter_spacing="-0.5px",
                        color="transparent",
                        background="linear-gradient(135deg, #E6EDF3, #a78bfa)",
                        background_clip="text",
                        webkit_background_clip="text",
                    ),
                    align="center",
                    gap=T.SPACE_3,
                    margin_bottom=T.SPACE_6,
                ),
                
                # Header
                rx.heading(
                    "Actualiza tu contraseña",
                    size="6",
                    weight="bold",
                    color=T.TEXT_PRIMARY,
                    margin_bottom=T.SPACE_2,
                ),
                rx.text(
                    "Introduce tu nueva contraseña a continuación.",
                    color=T.TEXT_SECONDARY,
                    font_size=T.TEXT_SM,
                    margin_bottom=T.SPACE_6,
                    text_align="center",
                ),

                # Error Message
                rx.cond(
                    UpdatePasswordState.error_message != "",
                    rx.box(
                        rx.hstack(
                            rx.icon(tag="circle-alert", size=16, color=T.ERROR),
                            rx.text(UpdatePasswordState.error_message, font_size=T.TEXT_SM, color=T.ERROR),
                            align="center",
                            gap=T.SPACE_2,
                        ),
                        background="rgba(244, 63, 94, 0.1)",
                        border=f"1px solid rgba(244, 63, 94, 0.2)",
                        border_radius=T.RADIUS_MD,
                        padding=f"{T.SPACE_3} {T.SPACE_4}",
                        margin_bottom=T.SPACE_6,
                        width="100%",
                    )
                ),
                
                # Success state
                rx.cond(
                    UpdatePasswordState.is_success,
                    rx.vstack(
                        rx.icon("circle-check", size=48, color=T.SUCCESS),
                        rx.heading("¡Contraseña Actualizada!", size="4"),
                        rx.text("Tu contraseña ha sido cambiada exitosamente.", color=T.TEXT_MUTED, text_align="center"),
                        rx.button(
                            "Ir al Dashboard",
                            on_click=UpdatePasswordState.redirect_to_dashboard,
                            width="100%",
                            size="3",
                            margin_top=T.SPACE_4,
                        ),
                        width="100%", align="center", spacing="4"
                    ),
                    
                    # Form state
                    rx.vstack(
                        rx.vstack(
                            rx.text("Nueva Contraseña", font_size=T.TEXT_SM, font_weight=T.WEIGHT_MEDIUM, color=T.TEXT_PRIMARY),
                            rx.input(
                                placeholder="••••••••",
                                type="password",
                                size="3",
                                value=UpdatePasswordState.password,
                                on_change=UpdatePasswordState.set_password,
                                width="100%",
                                background=T.BG_SECONDARY,
                            ),
                            width="100%",
                            align_items="start",
                            spacing="2",
                        ),
                        rx.vstack(
                            rx.text("Confirmar Contraseña", font_size=T.TEXT_SM, font_weight=T.WEIGHT_MEDIUM, color=T.TEXT_PRIMARY),
                            rx.input(
                                placeholder="••••••••",
                                type="password",
                                size="3",
                                value=UpdatePasswordState.confirm_password,
                                on_change=UpdatePasswordState.set_confirm_password,
                                width="100%",
                                background=T.BG_SECONDARY,
                            ),
                            width="100%",
                            align_items="start",
                            spacing="2",
                        ),
                        
                        rx.button(
                            rx.cond(
                                UpdatePasswordState.is_loading,
                                rx.spinner(size="2"),
                                "Guardar Contraseña"
                            ),
                            width="100%",
                            size="3",
                            background=T.BRAND,
                            color="white",
                            on_click=UpdatePasswordState.handle_update_password,
                            disabled=UpdatePasswordState.is_loading,
                            cursor="pointer",
                            margin_top=T.SPACE_4,
                        ),
                        width="100%", spacing="4"
                    ),
                ),
                
                width="100%",
                align_items="center",
            ),
            background=T.BG_PRIMARY,
            padding=T.SPACE_8,
            border_radius=T.RADIUS_XL,
            border=f"1px solid {T.BORDER}",
            box_shadow=f"0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 0 1px {T.BORDER_SUBTLE}",
            width="100%",
            max_width="440px",
            position="relative",
            overflow="hidden",
            _before={
                "content": '""',
                "position": "absolute",
                "top": 0,
                "left": 0,
                "right": 0,
                "height": "2px",
                "background": f"linear-gradient(90deg, {T.BRAND}, #a855f7)",
            }
        ),
        width="100vw",
        height="100vh",
        background=T.BG_SECONDARY,
        position="relative",
        overflow="hidden",
        _after={
            "content": '""',
            "position": "absolute",
            "width": "600px",
            "height": "600px",
            "background": T.BRAND,
            "filter": "blur(120px)",
            "opacity": "0.05",
            "border_radius": "50%",
            "top": "50%",
            "left": "50%",
            "transform": "translate(-50%, -50%)",
            "z_index": 0,
            "pointer_events": "none",
        }
    )
