import reflex as rx
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.state.progress_state import ProgressState
from SKILLOGIC.components.layout import app_layout
from SKILLOGIC.styles import theme as T
from SKILLOGIC.data.katas import KATAS_DB

def _katas_stats_header() -> rx.Component:
    """Renderiza una sección superior con las estadísticas de Katas del usuario."""
    completed_count = ProgressState.completed_katas_count
    xp_earned = ProgressState.katas_xp_earned
    
    # Calcular porcentaje de completitud
    completed_percent = ((completed_count * 100) / 8).to(int)
    
    # Rango del usuario
    rank = rx.cond(
        ProgressState.xp == 0, "Novato", 
        rx.cond(ProgressState.level < 5, "Explorer", 
        rx.cond(ProgressState.level < 10, "Pioneer", "Master"))
    )

    return rx.grid(
        # Card 1: Progreso de Resolución
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.icon("award", color=T.BRAND, size=20),
                        background=T.BRAND_LIGHT,
                        border_radius=T.RADIUS_MD,
                        padding=T.SPACE_2,
                    ),
                    rx.vstack(
                        rx.text(rx.cond(AppState.is_spanish, "Progreso", "Progress"), font_size=T.TEXT_XS, color=T.TEXT_MUTED, font_weight=T.WEIGHT_SEMIBOLD, text_transform="uppercase"),
                        rx.text(completed_count.to_string() + " / 8", font_size=T.TEXT_XL, font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
                        spacing="0",
                        align_items="start"
                    ),
                    align_items="center",
                    spacing="3",
                ),
                rx.box(
                    rx.box(
                        width=completed_percent.to_string() + "%",
                        height="100%",
                        background=T.BRAND,
                        border_radius=T.RADIUS_FULL,
                        transition="width 0.5s ease",
                    ),
                    width="100%",
                    height="6px",
                    background=T.BG_HOVER,
                    border_radius=T.RADIUS_FULL,
                    overflow="hidden",
                    margin_top=T.SPACE_2,
                ),
                align_items="stretch",
                spacing="2",
            ),
            background=T.BG_SECONDARY,
            border=f"1px solid {T.BORDER}",
            border_radius=T.RADIUS_XL,
            padding=T.SPACE_4,
        ),
        
        # Card 2: XP Acumulada
        rx.box(
            rx.hstack(
                rx.box(
                    rx.icon("star", color=T.WARNING, size=20),
                    background=T.WARNING_LIGHT,
                    border_radius=T.RADIUS_MD,
                    padding=T.SPACE_2,
                ),
                rx.vstack(
                    rx.text(rx.cond(AppState.is_spanish, "XP de Katas", "Katas XP"), font_size=T.TEXT_XS, color=T.TEXT_MUTED, font_weight=T.WEIGHT_SEMIBOLD, text_transform="uppercase"),
                    rx.text(xp_earned.to_string() + " XP", font_size=T.TEXT_XL, font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
                    spacing="0",
                    align_items="start"
                ),
                align_items="center",
                spacing="3",
            ),
            background=T.BG_SECONDARY,
            border=f"1px solid {T.BORDER}",
            border_radius=T.RADIUS_XL,
            padding=T.SPACE_4,
        ),
        
        # Card 3: Rango de Programación
        rx.box(
            rx.hstack(
                rx.box(
                    rx.icon("zap", color=T.STREAK, size=20),
                    background=T.STREAK_LIGHT,
                    border_radius=T.RADIUS_MD,
                    padding=T.SPACE_2,
                ),
                rx.vstack(
                    rx.text(rx.cond(AppState.is_spanish, "Rango de Nivel", "Level Rank"), font_size=T.TEXT_XS, color=T.TEXT_MUTED, font_weight=T.WEIGHT_SEMIBOLD, text_transform="uppercase"),
                    rx.text(rank, font_size=T.TEXT_XL, font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
                    spacing="0",
                    align_items="start"
                ),
                align_items="center",
                spacing="3",
            ),
            background=T.BG_SECONDARY,
            border=f"1px solid {T.BORDER}",
            border_radius=T.RADIUS_XL,
            padding=T.SPACE_4,
        ),
        
        columns=rx.breakpoints(initial="1", sm="3"),
        gap=T.SPACE_4,
        width="100%",
        margin_bottom=T.SPACE_6,
    )

def _kata_list_item(kata: dict) -> rx.Component:
    """Renderiza una fila para un Kata en la lista."""
    kata_id = kata["id"]
    difficulty = kata["difficulty"]
    
    # Verificar si está completado o bloqueado
    is_completed = ProgressState.completed_katas.contains(kata_id)
    requires = kata.get("requires_kata")
    is_locked = rx.cond(
        requires != None,
        ~ProgressState.completed_katas.contains(requires),
        False
    )
    
    # Definir icono de estado
    status_icon = rx.cond(
        is_locked,
        rx.icon("lock", color=T.TEXT_MUTED, size=18),
        rx.cond(
            is_completed,
            rx.icon("circle_check", color=T.SUCCESS, size=18),
            rx.icon("play", color=T.BRAND, size=18)
        )
    )

    return rx.box(
        rx.hstack(
            # Icono + Badge + Título y Descripción (en stack)
            rx.hstack(
                # Icono de estado
                rx.box(
                    status_icon,
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    width="36px",
                    height="36px",
                    border_radius=T.RADIUS_MD,
                    background=rx.cond(is_locked, T.BG_HOVER, rx.cond(is_completed, T.SUCCESS_LIGHT, T.BRAND_LIGHT)),
                    flex_shrink="0",
                ),
                
                # Dificultad (Badge)
                rx.box(
                    rx.badge(
                        rx.cond(AppState.is_spanish, difficulty.capitalize(), difficulty.capitalize()),
                        color_scheme=rx.cond(difficulty == "facil", "green", rx.cond(difficulty == "medio", "yellow", "red")),
                        variant="soft",
                        radius="full",
                        size="1",
                    ),
                    width="70px",
                    display="flex",
                    justify_content="center",
                    flex_shrink="0",
                ),
                
                # Título y Descripción
                rx.vstack(
                    rx.text(
                        rx.cond(AppState.is_spanish, kata["title_es"], kata["title_en"]),
                        font_weight=T.WEIGHT_SEMIBOLD,
                        font_size=T.TEXT_MD,
                        color=rx.cond(is_locked, T.TEXT_MUTED, T.TEXT_PRIMARY),
                    ),
                    rx.text(
                        rx.cond(AppState.is_spanish, kata["description_es"], kata["description_en"]),
                        font_size=T.TEXT_SM,
                        color=T.TEXT_SECONDARY,
                        no_of_lines=1,
                    ),
                    spacing="1",
                    align_items="start",
                    flex="1",
                ),
                align_items="center",
                spacing="4",
                flex="1",
                min_width="0",
            ),
            
            # Puntos XP + Botón
            rx.hstack(
                rx.text(
                    f"+{kata['xp_reward']} XP",
                    font_weight=T.WEIGHT_BOLD,
                    color=rx.cond(is_locked, T.TEXT_MUTED, T.BRAND),
                    white_space="nowrap",
                ),
                rx.button(
                    rx.cond(
                        is_locked, 
                        "Bloqueado", 
                        rx.cond(is_completed, "Repetir", "Resolver")
                    ),
                    size="1",
                    color_scheme=rx.cond(is_locked, "gray", rx.cond(is_completed, "gray", "violet")),
                    disabled=is_locked,
                    on_click=rx.redirect(f"/kata/{kata_id}"),
                    cursor=rx.cond(is_locked, "not-allowed", "pointer"),
                ),
                spacing="4",
                align_items="center",
                flex_shrink="0",
            ),
            
            width="100%",
            justify="between",
            align_items="center",
            padding=T.SPACE_4,
        ),
        background=T.BG_SECONDARY,
        border=f"1px solid {T.BORDER}",
        border_radius=T.RADIUS_LG,
        opacity=rx.cond(is_locked, "0.65", "1"),
        transition=f"all {T.EASE_BASE}",
        _hover={
            "border_color": rx.cond(is_locked, T.BORDER, T.BRAND_MEDIUM),
            "background": rx.cond(is_locked, T.BG_SECONDARY, T.BG_HOVER),
            "transform": rx.cond(is_locked, "none", "translateX(4px)"),
        },
        width="100%",
        margin_bottom=T.SPACE_3,
    )

@rx.page(route="/katas", title="Katas | SKILLOGIC", on_load=ProgressState.load_stats)
def katas_list_page() -> rx.Component:
    """Página principal de Katas."""
    return app_layout(
        rx.box(
            # Header
            rx.vstack(
                rx.heading(
                    rx.cond(AppState.is_spanish, "Katas de Programación", "Programming Katas"),
                    size="8",
                    color=T.TEXT_PRIMARY,
                    margin_bottom=T.SPACE_2
                ),
                rx.text(
                    rx.cond(
                        AppState.is_spanish, 
                        "\"A programar se aprende programando\". Resuelve estos retos en orden para ganar experiencia y construir memoria muscular.", 
                        "\"To learn programming you learn by programming\". Solve these challenges in order to earn experience and build muscle memory."
                    ),
                    color=T.TEXT_SECONDARY,
                    font_size=T.TEXT_LG
                ),
                align_items="start",
                margin_bottom=T.SPACE_8
            ),
            
            # Stats Header Widget
            _katas_stats_header(),
            
            # Lista de Katas
            rx.vstack(
                *[ _kata_list_item(k) for k in KATAS_DB ],
                width="100%",
                spacing="0",
            ),
            
            padding=rx.breakpoints(initial=f"{T.SPACE_4}", md=f"{T.SPACE_8}"),
            width="100%",
            max_width="1000px",
            margin="0 auto"
        )
    )
