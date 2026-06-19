import reflex as rx
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.state.progress_state import ProgressState
from SKILLOGIC.components.layout import app_layout
from SKILLOGIC.styles import theme as T
from SKILLOGIC.data.katas import KATAS_DB, get_daily_kata

def _katas_stats_header() -> rx.Component:
    """Renderiza una sección superior con las estadísticas de Katas del usuario."""
    completed_count = ProgressState.completed_katas_count
    xp_earned = ProgressState.katas_xp_earned
    
    # Calcular porcentaje de completitud
    completed_percent = ((completed_count * 100) / 10).to(int)
    
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
                        rx.text(completed_count.to_string() + " / 10", font_size=T.TEXT_XL, font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
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
    
    # En el Dojo, todos los katas están desbloqueados por defecto
    is_completed = ProgressState.completed_katas.contains(kata_id)
    is_locked = False
    
    # Definir icono de estado
    status_icon = rx.cond(
        is_completed,
        rx.icon("circle_check", color=T.SUCCESS, size=18),
        rx.icon("play", color=T.BRAND, size=18)
    )

    desc_text = rx.cond(AppState.is_spanish, kata["description_es"], kata["description_en"])
    title_text = rx.cond(AppState.is_spanish, kata["title_es"], kata["title_en"])

    return rx.box(
        rx.vstack(
            # Cabecera de la tarjeta: Icono + Badges
            rx.hstack(
                rx.box(
                    status_icon,
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    width="36px",
                    height="36px",
                    border_radius=T.RADIUS_MD,
                    background=rx.cond(is_completed, T.SUCCESS_LIGHT, T.BRAND_LIGHT),
                ),
                rx.spacer(),
                rx.badge(
                    rx.cond(AppState.is_spanish, difficulty.capitalize(), difficulty.capitalize()),
                    color_scheme=rx.cond(difficulty == "facil", "green", rx.cond(difficulty == "medio", "yellow", "red")),
                    variant="soft",
                    radius="full",
                    size="1",
                ),
                width="100%",
            ),
            
            # Título y Descripción (cuerpo de la tarjeta)
            rx.vstack(
                rx.text(
                    title_text,
                    font_weight=T.WEIGHT_BOLD,
                    font_size=T.TEXT_SM,
                    color=T.TEXT_PRIMARY,
                    line_height="1.3",
                    no_of_lines=2,
                ),
                rx.hover_card.root(
                    rx.hover_card.trigger(
                        rx.text(
                            desc_text,
                            font_size=T.TEXT_XS,
                            color=T.TEXT_SECONDARY,
                            no_of_lines=3,
                            cursor="pointer",
                        )
                    ),
                    rx.hover_card.content(
                        rx.text(desc_text, font_size=T.TEXT_SM, color=T.TEXT_PRIMARY, line_height="1.5"),
                        max_width="320px",
                        background=T.BG_ELEVATED,
                        padding=T.SPACE_3,
                        border=f"1px solid {T.BORDER}",
                        border_radius=T.RADIUS_MD,
                        box_shadow=T.SHADOW_LG,
                    )
                ),
                spacing="2",
                align_items="start",
                width="100%",
                flex="1",
                margin_top=T.SPACE_2,
                overflow="hidden",
            ),
            
            # Pie de la tarjeta: XP y Botón
            rx.box(
                rx.hstack(
                rx.text(
                    f"+{kata['xp_reward']} XP",
                    font_weight=T.WEIGHT_EXTRABOLD,
                    font_size=T.TEXT_SM,
                    color=T.BRAND,
                ),
                rx.spacer(),
                rx.button(
                    rx.cond(is_completed, "Repetir", "Resolver"),
                    size="1",
                    color_scheme=rx.cond(is_completed, "gray", "violet"),
                    on_click=rx.redirect(f"/kata/{kata_id}"),
                    cursor="pointer",
                ),
                width="100%",
                align_items="center",
            ),
            width="100%",
            margin_top=T.SPACE_4,
            border_top=f"1px solid {T.BORDER_SUBTLE}",
            padding_top=T.SPACE_3,
        ),
        width="100%",
        height="100%", # Ocupar todo el espacio de la caja
            padding=T.SPACE_4,
        ),
        background=T.BG_SECONDARY,
        border=f"1px solid {T.BORDER}",
        border_radius=T.RADIUS_LG,
        transition=f"all {T.EASE_BASE}",
        height="100%",
        display="flex",
        flex_direction="column",
        _hover={
            "border_color": T.BRAND_MEDIUM,
            "background": T.BG_HOVER,
            "transform": "translateY(-4px)",
            "box_shadow": T.SHADOW_MD,
        },
    )

def _daily_kata_banner() -> rx.Component:
    kata = get_daily_kata()
    title = rx.cond(AppState.is_spanish, kata["title_es"], kata["title_en"])
    desc = rx.cond(AppState.is_spanish, kata["description_es"], kata["description_en"])
    
    return rx.box(
        rx.flex(
            rx.box(
                rx.icon("flame", color="white", size=32),
                background=f"linear-gradient(135deg, {T.BRAND}, {T.WARNING})",
                border_radius=T.RADIUS_LG,
                padding=T.SPACE_3,
                box_shadow=f"0 0 15px {T.BRAND_GLOW}",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text("EL KATA DEL DÍA", font_weight=T.WEIGHT_EXTRABOLD, font_size=T.TEXT_SM, color=T.WARNING, letter_spacing="1px"),
                    rx.badge("XP x2", color_scheme="orange", variant="solid"),
                    align_items="center",
                    spacing="2"
                ),
                rx.text(title, font_size=T.TEXT_LG, font_weight=T.WEIGHT_BOLD, color="white"),
                rx.text(desc, font_size=T.TEXT_SM, color=T.TEXT_SECONDARY, no_of_lines=2, max_width="500px"),
                spacing="1",
                align_items="start",
            ),
            rx.spacer(),
            rx.button(
                "Resolver Reto",
                size="3",
                on_click=rx.redirect(f"/kata/{kata['id']}"),
                background="white",
                color=T.BG_PRIMARY,
                _hover={"background": T.BG_HOVER, "color": "white"},
            ),
            direction=rx.breakpoints(initial="column", sm="row"),
            align="center",
            gap=T.SPACE_4,
            padding=T.SPACE_5,
            width="100%"
        ),
        background=f"linear-gradient(to right, #1f1a30, #141120)",
        border=f"1px solid {T.BRAND_MEDIUM}",
        border_radius=T.RADIUS_XL,
        margin_bottom=T.SPACE_6,
        box_shadow=f"0 10px 30px {T.BRAND_GLOW}",
        width="100%",
        overflow="hidden",
        position="relative"
    )

def _render_kata_grid() -> rx.Component:
    """Renderiza todos los katas en un grid, como un álbum de colección."""
    return rx.grid(
        *[_kata_list_item(k) for k in KATAS_DB],
        columns=rx.breakpoints(initial="1", sm="2", md="3", lg="4", xl="5"),
        gap=T.SPACE_4,
        width="100%",
        margin_bottom=T.SPACE_8,
    )

@rx.page(route="/katas", title="Katas | SKILLOGIC", on_load=ProgressState.load_stats)
def katas_list_page() -> rx.Component:
    """Página principal de Katas."""
    return app_layout(
        rx.box(
            # Header
            rx.vstack(
                rx.heading(
                    "El Dojo: Katas y Retos",
                    size="8",
                    font_weight=T.WEIGHT_EXTRABOLD,
                    color=T.TEXT_PRIMARY,
                    letter_spacing="-1px",
                ),
                rx.text(
                    "Ejercita tus habilidades lógicas y gana experiencia extra. Elige cualquier reto y demuestra de qué estás hecho.",
                    font_size=T.TEXT_BASE,
                    color=T.TEXT_SECONDARY,
                    max_width="600px",
                    text_align="center",
                ),
                align_items="center",
                spacing="3",
                margin_bottom=T.SPACE_8,
            ),
            
            # Stats Header
            _katas_stats_header(),
            
            # Daily Kata Banner
            _daily_kata_banner(),
            
            # Katas Grid
            _render_kata_grid(),
            
            padding=rx.breakpoints(initial=f"{T.SPACE_4}", md=f"{T.SPACE_8}"),
            width="100%",
            max_width="1000px",
            margin="0 auto"
        )
    )
