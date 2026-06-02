import reflex as rx
from SKILLOGIC.components.layout import app_layout
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.state.curriculum_state import CurriculumState, ModuleItem
from SKILLOGIC.styles import theme as T

def t(es: str, en: str) -> rx.Component:
    """Helper for bilingual text"""
    return rx.text(rx.cond(AppState.is_spanish, es, en), as_="span")

def _lesson_item(lesson) -> rx.Component:
    return rx.hstack(
        rx.icon(tag="play", size=16, color=T.BRAND_LIGHT),
        rx.text(lesson.title, font_size=T.TEXT_SM, color=T.TEXT_SECONDARY),
        align="center",
        gap=T.SPACE_2,
        padding_y=T.SPACE_2,
        padding_x=T.SPACE_4,
        width="100%",
    )

def _module_timeline_node(module: ModuleItem) -> rx.Component:
    is_locked = module.status == "locked"
    is_completed = module.status == "completed"
    
    # Colors based on status
    node_bg = rx.cond(is_completed, T.BRAND, rx.cond(is_locked, T.BG_ELEVATED, T.BRAND_LIGHT))
    border_color = rx.cond(is_completed, T.BRAND, rx.cond(is_locked, T.BORDER, T.BRAND_LIGHT))
    icon_color = rx.cond(is_locked, T.TEXT_MUTED, "white")
    
    return rx.hstack(
        # Vertical Line & Node
        rx.vstack(
            rx.box(
                rx.icon(tag=module.icon_tag, size=18, color=icon_color),
                width="40px",
                height="40px",
                border_radius="50%",
                background=node_bg,
                border=f"2px solid {border_color}",
                display="flex",
                align_items="center",
                justify_content="center",
                z_index="2",
            ),
            rx.box(
                width="2px",
                flex="1",
                background=border_color,
                min_height="40px",
                opacity="0.5",
            ),
            align="center",
            spacing="0",
        ),
        # Module Content Card
        rx.box(
            rx.accordion.root(
                rx.accordion.item(
                    header=rx.hstack(
                        rx.vstack(
                            rx.text(rx.cond(AppState.is_spanish, module.name_es, module.name_en), font_size=T.TEXT_LG, font_weight=T.WEIGHT_BOLD, color=T.TEXT_PRIMARY),
                            rx.text(
                                rx.cond(
                                    is_locked,
                                    t("Módulo Bloqueado", "Module Locked"),
                                    rx.cond(
                                        is_completed,
                                        t("Completado", "Completed"),
                                        t("En progreso", "In progress")
                                    )
                                ),
                                font_size=T.TEXT_XS,
                                color=rx.cond(is_locked, T.TEXT_MUTED, T.TEXT_SECONDARY)
                            ),
                            align_items="start",
                            spacing="1"
                        ),
                        rx.spacer(),
                        rx.cond(
                            is_locked,
                            rx.box(),
                            rx.hstack(
                                rx.box(
                                    rx.box(
                                        width=f"{module.progress}%",
                                        height="100%",
                                        background=f"linear-gradient(90deg, {T.BRAND}, {T.BRAND_LIGHT})",
                                        border_radius=T.RADIUS_FULL,
                                        transition=f"width {T.EASE_BASE}",
                                        box_shadow=f"0 0 8px {T.BRAND}",
                                    ),
                                    width="120px",
                                    height="10px",
                                    background="rgba(108, 99, 255, 0.15)",
                                    border_radius=T.RADIUS_FULL,
                                    border=f"1px solid rgba(108, 99, 255, 0.3)",
                                ),
                                rx.text(
                                    f"{module.progress}%",
                                    font_size=T.TEXT_SM,
                                    font_weight=T.WEIGHT_EXTRABOLD,
                                    color=rx.cond(is_completed, T.BRAND_LIGHT, T.TEXT_PRIMARY),
                                ),
                                align="center",
                                gap="3",
                            )
                        ),
                        width="100%",
                        align="center",
                    ),
                    content=rx.cond(
                        module.lessons.length() > 0,
                        rx.vstack(
                            rx.foreach(module.lessons, _lesson_item),
                            width="100%",
                            padding_top=T.SPACE_2,
                            align_items="start",
                        ),
                        rx.text(t("Próximamente...", "Coming soon..."), font_size=T.TEXT_SM, color=T.TEXT_MUTED, padding_top=T.SPACE_2)
                    ),
                    value=module.name_es, # Unique value
                    border_bottom="none",
                ),
                type="multiple",
                collapsible=True,
                width="100%",
                background="transparent",
            ),
            background=T.BG_ELEVATED,
            border=f"1px solid {border_color}",
            border_radius=T.RADIUS_LG,
            padding=T.SPACE_4,
            width="100%",
            box_shadow=T.SHADOW_SM,
            opacity=rx.cond(is_locked, "0.6", "1.0"),
            transition=f"all {T.EASE_BASE}",
            _hover={"transform": rx.cond(is_locked, "none", "translateX(4px)"), "box_shadow": rx.cond(is_locked, "none", T.SHADOW_MD)},
        ),
        width="100%",
        align_items="stretch",
        gap=T.SPACE_6,
        padding_bottom=T.SPACE_4,
    )

@rx.page(route="/roadmap", title="Roadmap | SKILLOGIC", on_load=CurriculumState.load_data)
def roadmap_page() -> rx.Component:
    """The full learning roadmap page with a vertical timeline design."""
    return app_layout(
        rx.vstack(
            rx.hstack(
                rx.icon(tag="map", size=24, color=T.BRAND),
                rx.text(
                    t("Ruta de Aprendizaje", "Learning Roadmap"),
                    font_size=T.TEXT_2XL,
                    font_weight=T.WEIGHT_EXTRABOLD,
                    color=T.TEXT_PRIMARY,
                ),
                align="center",
                gap=T.SPACE_3,
            ),
            rx.text(
                t(
                    "Sigue tu progreso a través del currículum de SKILLOGIC. Desbloquea módulos completando las lecciones anteriores.",
                    "Track your progress through the SKILLOGIC curriculum. Unlock modules by completing previous lessons."
                ),
                font_size=T.TEXT_MD,
                color=T.TEXT_SECONDARY,
                margin_bottom=T.SPACE_8,
            ),
            
            rx.box(
                rx.foreach(
                    CurriculumState.modules,
                    _module_timeline_node
                ),
                width="100%",
                max_width="800px",
            ),
            
            width="100%",
            padding=rx.breakpoints(initial=T.SPACE_4, md=T.SPACE_8),
            align_items="start",
        )
    )
