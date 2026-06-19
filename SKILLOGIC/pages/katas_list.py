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
        rx.flex(
            # Icono a la izquierda
            rx.box(
                status_icon,
                display="flex",
                align_items="center",
                justify_content="center",
                width="32px",
                height="32px",
                border_radius=T.RADIUS_MD,
                background=rx.cond(is_locked, T.BG_HOVER, rx.cond(is_completed, T.SUCCESS_LIGHT, T.BRAND_LIGHT)),
                flex_shrink="0",
            ),
            
            # Contenido principal a la derecha
            rx.flex(
                # Título
                rx.text(
                    title_text,
                    font_weight=T.WEIGHT_SEMIBOLD,
                    font_size=T.TEXT_SM,
                    color=rx.cond(is_locked, T.TEXT_MUTED, T.TEXT_PRIMARY),
                    margin_bottom="2px",
                ),
                
                # Descripción con Popover (Hover Card)
                rx.hover_card.root(
                    rx.hover_card.trigger(
                        rx.text(
                            desc_text,
                            font_size=T.TEXT_XS,
                            color=T.TEXT_SECONDARY,
                            no_of_lines=1,
                            cursor="pointer",
                            _hover={"color": T.TEXT_PRIMARY},
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
                
                # Fila inferior: Badge, Spacer, XP, Botón
                rx.flex(
                    rx.badge(
                        rx.cond(AppState.is_spanish, difficulty.capitalize(), difficulty.capitalize()),
                        color_scheme=rx.cond(difficulty == "facil", "green", rx.cond(difficulty == "medio", "yellow", "red")),
                        variant="soft",
                        radius="full",
                        size="1",
                    ),
                    rx.spacer(),
                    rx.text(
                        f"+{kata['xp_reward']} XP",
                        font_weight=T.WEIGHT_BOLD,
                        font_size=T.TEXT_SM,
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
                    direction="row",
                    align="center",
                    gap=T.SPACE_3,
                    width="100%",
                    margin_top=T.SPACE_3,
                    flex_wrap="wrap",
                ),
                direction="column",
                flex="1",
                min_width="0",
            ),
            direction="row",
            align="start",
            gap=T.SPACE_3,
            width="100%",
            padding=T.SPACE_3,
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
        margin_bottom=T.SPACE_2,
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

def _render_grouped_katas() -> list[rx.Component]:
    from collections import defaultdict
    groups = defaultdict(list)
    for k in KATAS_DB:
        # Group by category (we'll use the english string as key internally, and map back to dict)
        cat_key = k.get("category_en", "Advanced Algorithms (FAANG)")
        groups[cat_key].append(k)

    components = []
    
    for key, items in groups.items():
        title_es = items[0].get("category_es", key)
        title_en = items[0].get("category_en", key)
            
        components.append(
            rx.box(
                rx.text(rx.cond(AppState.is_spanish, title_es, title_en), font_weight=T.WEIGHT_BOLD, color=T.BRAND, font_size=T.TEXT_MD, letter_spacing="1px", text_transform="uppercase"),
                border_bottom=f"1px solid {T.BORDER_SUBTLE}",
                width="100%",
                padding_bottom=T.SPACE_2,
                margin_top=rx.cond(len(components) > 0, T.SPACE_6, T.SPACE_2),
                margin_bottom=T.SPACE_4,
            )
        )
        for k in items:
            components.append(_kata_list_item(k))
            
    return components

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
            
            # Katas List
            rx.vstack(
                *_render_grouped_katas(),
                width="100%",
                spacing="0",
            ),
            
            padding=rx.breakpoints(initial=f"{T.SPACE_4}", md=f"{T.SPACE_8}"),
            width="100%",
            max_width="1000px",
            margin="0 auto"
        )
    )
