import reflex as rx
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.state.kata_state import KataState
from SKILLOGIC.styles import theme as T

def render_kata_content() -> rx.Component:
    """Left/Top panel: Kata description."""
    kata = KataState.kata_data
    
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.badge(
                    rx.cond(AppState.is_spanish, kata["difficulty"], kata["difficulty"]), # Simplified for MVP
                    variant="soft",
                    color_scheme="violet"
                ),
                rx.badge(
                    f"{kata['xp_reward']} XP",
                    variant="solid",
                    color_scheme="yellow"
                ),
                margin_bottom=T.SPACE_2
            ),
            rx.heading(
                rx.cond(AppState.is_spanish, kata["title_es"], kata["title_en"]),
                size="6",
                margin_bottom=T.SPACE_4
            ),
            rx.markdown(
                rx.cond(AppState.is_spanish, kata["description_es"], kata["description_en"]),
                custom_styles={
                    "h1": {"font_size": T.TEXT_2XL, "margin_bottom": T.SPACE_4},
                    "h2": {"font_size": T.TEXT_XL, "margin_bottom": T.SPACE_3, "margin_top": T.SPACE_6},
                    "p": {"font_size": T.TEXT_BASE, "line_height": "1.6", "margin_bottom": T.SPACE_4, "color": T.TEXT_SECONDARY},
                    "code": {
                        "background": T.BG_ELEVATED,
                        "padding": f"{T.SPACE_1} {T.SPACE_2}",
                        "border_radius": T.RADIUS_SM,
                        "font_family": T.FONT_CODE,
                        "font_size": "0.9em",
                        "color": T.BRAND,
                    },
                }
            ),
            align_items="start",
            padding=T.SPACE_6,
            background=T.BG_PRIMARY,
            height="100%",
            overflow_y="auto"
        ),
        height="100%",
        border_right=f"1px solid {T.BORDER}"
    )

def render_kata_workspace() -> rx.Component:
    """Right/Bottom panel: Code Editor and Console."""
    return rx.box(
        rx.vstack(
            # Code Editor with MacOS style window
            rx.box(
                # Window header
                rx.hstack(
                    rx.hstack(
                        rx.box(width="12px", height="12px", border_radius="50%", background="#ff5f56"),
                        rx.box(width="12px", height="12px", border_radius="50%", background="#ffbd2e"),
                        rx.box(width="12px", height="12px", border_radius="50%", background="#27c93f"),
                        spacing="2"
                    ),
                    rx.text("main.py", color="#858585", font_size="12px", font_family="monospace"),
                    rx.box(width="48px"), # Spacer balancer
                    justify="between",
                    padding=f"{T.SPACE_2} {T.SPACE_4}",
                    background="#2d2d2d",
                    border_top_radius=T.RADIUS_MD,
                    align="center"
                ),
                rx.text_area(
                    value=KataState.user_code,
                    on_change=KataState.set_user_code,
                    height="45vh",
                    width="100%",
                    font_family="'Fira Code', 'Consolas', monospace",
                    font_size="md",
                    background="#1e1e1e",
                    color="#d4d4d4",
                    padding=T.SPACE_4,
                    border="none",
                    border_radius="0",
                    border_bottom_radius=T.RADIUS_MD,
                    resize="none",
                    _focus={"outline": "none", "box_shadow": f"inset 0 0 0 1px {T.BRAND}"}
                ),
                width="100%",
                box_shadow=T.SHADOW_LG,
                border_radius=T.RADIUS_MD,
                margin_bottom=T.SPACE_4
            ),
            
            # Run Button
            rx.button(
                rx.icon("play", size=18),
                rx.cond(AppState.is_spanish, "Ejecutar Pruebas", "Run Tests"),
                on_click=KataState.run_kata,
                loading=KataState.is_loading,
                color_scheme="green",
                size="3",
                align_self="flex-end",
                cursor="pointer",
                box_shadow=f"0 4px 14px 0 rgba(34, 197, 94, 0.39)",
                _hover={"transform": "translateY(-1px)", "box_shadow": f"0 6px 20px rgba(34, 197, 94, 0.23)"},
                transition="all 0.2s ease"
            ),
            
            # Terminal
            rx.box(
                rx.text("TERMINAL", color="#555", font_size="10px", font_weight="bold", margin_bottom=T.SPACE_2, letter_spacing="1px"),
                rx.cond(
                    KataState.terminal_output != "",
                    rx.text(
                        KataState.terminal_output,
                        font_family="'Fira Code', 'Consolas', monospace",
                        color=rx.cond(KataState.is_success, "#4ade80", "#d4d4d4"),
                        white_space="pre-wrap",
                        text_shadow=rx.cond(KataState.is_success, "0 0 5px rgba(74, 222, 128, 0.5)", "none")
                    ),
                    rx.text("Esperando ejecución...", color=T.TEXT_MUTED, font_style="italic")
                ),
                rx.cond(
                    KataState.feedback_message != "",
                    rx.box(
                        rx.divider(margin_y=T.SPACE_3, border_color="#333"),
                        rx.hstack(
                            rx.icon("zap", color="#fbbf24", size=16),
                            rx.text("SKILLOGIC AI:", font_weight="bold", color="#fbbf24", font_family="monospace"),
                            align="center", margin_bottom=T.SPACE_1
                        ),
                        rx.text(KataState.feedback_message, color=rx.cond(KataState.is_success, "#4ade80", "#f87171"), font_family="monospace"),
                    )
                ),
                background="#0f172a", # Slate 900
                width="100%",
                height="35vh",
                padding=T.SPACE_5,
                border_radius=T.RADIUS_MD,
                border="1px solid #1e293b",
                box_shadow="inset 0 2px 10px rgba(0,0,0,0.5)",
                overflow_y="auto",
                margin_top=T.SPACE_4
            ),
            width="100%",
            height="100%",
            spacing="0",
        ),
        padding=T.SPACE_8,
        background=T.BG_SECONDARY,
        height="100%",
        overflow_y="auto"
    )

@rx.page(route="/kata/[kata_id]", title="Kata | SKILLOGIC", on_load=KataState.on_load)
def kata_page() -> rx.Component:
    """Main page for solving a kata."""
    
    # Topbar for Kata
    topbar = rx.hstack(
        rx.hstack(
            rx.button(
                rx.icon("arrow-left", size=18),
                variant="ghost",
                on_click=rx.redirect("/katas"),
                color=T.TEXT_SECONDARY,
                _hover={"background": T.BG_HOVER}
            ),
            rx.text(
                "Katas / Resolución",
                font_weight=T.WEIGHT_SEMIBOLD,
                color=T.TEXT_PRIMARY
            ),
            spacing="4",
            align="center"
        ),
        rx.spacer(),
        rx.button(
            AppState.toggle_theme_label,
            variant="ghost",
            on_click=AppState.toggle_theme
        ),
        padding=f"{T.SPACE_4} {T.SPACE_8}",
        border_bottom=f"1px solid {T.BORDER}",
        background=T.BG_PRIMARY,
        width="100%",
        height=T.TOPBAR_HEIGHT,
        align="center"
    )

    # Split Pane (Vertical on mobile, Horizontal on desktop)
    content = rx.flex(
        rx.box(
            render_kata_content(),
            width=rx.breakpoints(initial="100%", lg="40%"),
            height=rx.breakpoints(initial="auto", lg="100%"),
            overflow=rx.breakpoints(initial="visible", lg="hidden")
        ),
        rx.box(
            render_kata_workspace(),
            width=rx.breakpoints(initial="100%", lg="60%"),
            height=rx.breakpoints(initial="auto", lg="100%"),
            overflow=rx.breakpoints(initial="visible", lg="hidden")
        ),
        width="100%",
        height=rx.breakpoints(initial="auto", lg=f"calc(100vh - {T.TOPBAR_HEIGHT})"),
        direction=rx.breakpoints(initial="column", lg="row"),
        align="stretch",
        spacing="0"
    )
    
    return rx.box(
        topbar,
        content,
        width="100vw",
        min_height="100vh",
        background=T.BG_PRIMARY,
        color=T.TEXT_PRIMARY,
        data_theme=AppState.theme
    )
