import reflex as rx
from SKILLOGIC.state.curriculum_state import CurriculumState
from SKILLOGIC.state.admin_users_state import AdminUsersState
from SKILLOGIC.components.layout import app_layout
from SKILLOGIC.styles import theme as T

def _admin_modules() -> rx.Component:
    return rx.vstack(
        rx.heading("Módulos y Lecciones", size="5", margin_bottom=T.SPACE_4),
        rx.accordion.root(
            rx.foreach(
                CurriculumState.modules,
                lambda mod, i: rx.accordion.item(
                    header=rx.hstack(
                        rx.icon(tag=mod["icon_tag"].to(str), color=T.BRAND),
                        rx.text(mod["name_es"], font_weight="bold"),
                        align="center",
                        gap=T.SPACE_3,
                    ),
                    content=rx.vstack(
                        rx.foreach(
                            mod["lessons"].to(list),
                            lambda lesson, j: rx.hstack(
                                rx.text(lesson.to(dict)["id"].to(str), font_weight="bold", color=T.TEXT_MUTED, width="30px"),
                                rx.text(lesson.to(dict)["title"].to(str), flex="1"),
                                rx.button(
                                    rx.icon(tag="trash", size=14),
                                    on_click=lambda _: CurriculumState.remove_lesson(i, j),
                                    color_scheme="red", variant="ghost", cursor="pointer",
                                    padding="0",
                                ),
                                width="100%", align="center", gap=T.SPACE_2, padding=f"{T.SPACE_2} 0",
                                border_bottom=f"1px solid {T.BORDER_SUBTLE}",
                            )
                        ),
                        rx.hstack(
                            rx.input(
                                placeholder="Título de Nueva Lección...",
                                value=CurriculumState.new_lesson_title_es,
                                on_change=CurriculumState.set_new_lesson_title_es,
                                flex="1", background=T.BG_SECONDARY, color=T.TEXT_PRIMARY,
                            ),
                            rx.button(
                                "Añadir Lección",
                                on_click=lambda _: CurriculumState.add_lesson(i),
                                background=T.BRAND, color="white", cursor="pointer",
                            ),
                            width="100%", margin_top=T.SPACE_3,
                        ),
                        rx.button(
                            rx.icon(tag="trash", size=16),
                            "Eliminar Módulo Completo",
                            on_click=lambda _: CurriculumState.remove_module(i),
                            color_scheme="red", variant="soft", cursor="pointer", margin_top=T.SPACE_6,
                            width="100%",
                        ),
                        width="100%", padding=T.SPACE_4, background=T.BG_HOVER,
                    ),
                    value=mod["name_es"],
                )
            ),
            width="100%",
            collapsible=True,
            type="multiple",
        ),
        rx.divider(margin_top=T.SPACE_6, margin_bottom=T.SPACE_6),
        rx.heading("Añadir Nuevo Módulo", size="4", margin_bottom=T.SPACE_4),
        rx.hstack(
            rx.input(
                placeholder="Nombre (ES)",
                value=CurriculumState.new_module_name_es,
                on_change=CurriculumState.set_new_module_name_es,
                flex="1", background=T.BG_SECONDARY, color=T.TEXT_PRIMARY,
            ),
            rx.input(
                placeholder="Icono (ej: folder, terminal)",
                value=CurriculumState.new_module_icon,
                on_change=CurriculumState.set_new_module_icon,
                width="200px", background=T.BG_SECONDARY, color=T.TEXT_PRIMARY,
            ),
            rx.button(
                "Añadir Módulo", on_click=CurriculumState.add_module,
                background=T.BRAND, color="white", cursor="pointer",
            ),
            width="100%",
        ),
        width="100%", align_items="start",
    )

def _admin_projects() -> rx.Component:
    return rx.vstack(
        rx.heading("Portafolio de Proyectos", size="5", margin_bottom=T.SPACE_4),
        rx.vstack(
            rx.foreach(
                CurriculumState.projects,
                lambda proj, i: rx.hstack(
                    rx.vstack(
                        rx.text(proj["title_es"], font_weight="bold"),
                        rx.text(proj["desc_es"], font_size=T.TEXT_XS, color=T.TEXT_MUTED),
                        spacing="1", flex="1", align_items="start",
                    ),
                    rx.badge(proj["level"].to(str), color_scheme="purple"),
                    rx.button(
                        rx.icon(tag="trash", size=16),
                        on_click=lambda _: CurriculumState.remove_project(i),
                        color_scheme="red", variant="ghost", cursor="pointer",
                    ),
                    width="100%", align="center", padding=T.SPACE_3,
                    border=f"1px solid {T.BORDER}", border_radius=T.RADIUS_MD,
                    background=T.BG_SECONDARY,
                )
            ),
            width="100%", spacing="2",
        ),
        rx.divider(margin_top=T.SPACE_6, margin_bottom=T.SPACE_6),
        rx.heading("Añadir Nuevo Proyecto", size="4", margin_bottom=T.SPACE_4),
        rx.vstack(
            rx.input(
                placeholder="Título (ES)",
                value=CurriculumState.new_project_title_es,
                on_change=CurriculumState.set_new_project_title_es,
                width="100%", background=T.BG_SECONDARY, color=T.TEXT_PRIMARY,
            ),
            rx.text_area(
                placeholder="Descripción (ES)",
                value=CurriculumState.new_project_desc_es,
                on_change=CurriculumState.set_new_project_desc_es,
                width="100%", background=T.BG_SECONDARY, color=T.TEXT_PRIMARY,
            ),
            rx.select(
                ["basic", "intermediate", "advanced"],
                value=CurriculumState.new_project_level,
                on_change=CurriculumState.set_new_project_level,
                width="100%",
            ),
            rx.button(
                "Añadir Proyecto", on_click=CurriculumState.add_project,
                background=T.BRAND, color="white", cursor="pointer", margin_top=T.SPACE_3,
            ),
            width="100%", align_items="start",
        ),
        width="100%", align_items="start",
    )

def _admin_daily() -> rx.Component:
    return rx.vstack(
        rx.heading("Plan de Hoy", size="5", margin_bottom=T.SPACE_4),
        rx.vstack(
            rx.foreach(
                CurriculumState.todays_plan,
                lambda item, i: rx.hstack(
                    rx.checkbox(
                        checked=item["completed"].to(bool),
                        on_change=lambda val: CurriculumState.toggle_plan_completion(i, val)
                    ),
                    rx.input(
                        value=item["title_es"],
                        on_change=lambda val: CurriculumState.set_plan_title(i, val),
                        width="100%", background=T.BG_SECONDARY, border=f"1px solid {T.BORDER}", color=T.TEXT_PRIMARY,
                    ),
                    width="100%", align="center", gap=T.SPACE_3, padding=T.SPACE_2,
                    background=T.BG_HOVER, border=f"1px solid {T.BORDER}", border_radius=T.RADIUS_MD,
                )
            ),
            width="100%", spacing="3",
        ),
        
        rx.heading("Desafío Diario", size="5", margin_top=T.SPACE_8, margin_bottom=T.SPACE_4),
        rx.vstack(
            rx.text("Título (ES)", font_weight="bold", color=T.TEXT_PRIMARY),
            rx.input(
                value=CurriculumState.daily_challenge["title_es"],
                on_change=CurriculumState.set_challenge_title,
                width="100%", background=T.BG_SECONDARY, border=f"1px solid {T.BORDER}", color=T.TEXT_PRIMARY,
            ),
            rx.text("Descripción (ES)", font_weight="bold", margin_top=T.SPACE_2, color=T.TEXT_PRIMARY),
            rx.text_area(
                value=CurriculumState.daily_challenge["desc_es"],
                on_change=CurriculumState.set_challenge_desc,
                width="100%", background=T.BG_SECONDARY, border=f"1px solid {T.BORDER}", color=T.TEXT_PRIMARY, min_height="100px",
            ),
            width="100%", spacing="2",
        ),
        rx.button(
            "Guardar Cambios Rápidos", on_click=CurriculumState.save_data,
            margin_top=T.SPACE_8, background=T.BRAND, color="white",
            padding=f"{T.SPACE_3} {T.SPACE_6}", border_radius=T.RADIUS_MD,
            cursor="pointer", _hover={"background": T.BRAND_HOVER},
        ),
        width="100%", align_items="start", max_width="600px",
    )

def _user_modal() -> rx.Component:
    """Modal de detalles del usuario."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Perfil de Usuario"),
            rx.dialog.description("Visualiza y gestiona los detalles y privilegios de este usuario.", margin_bottom=T.SPACE_4),
            
            rx.vstack(
                # Información
                rx.hstack(
                    rx.vstack(
                        rx.hstack(
                            rx.text("Email de Acceso (Usuario)", font_size=T.TEXT_XS, color=T.TEXT_MUTED),
                            rx.spacer(),
                            rx.cond(AdminUsersState.email_edit_success, rx.text("¡Guardado!", font_size="10px", color=T.SUCCESS)),
                            rx.cond(AdminUsersState.email_edit_error != "", rx.text(AdminUsersState.email_edit_error, font_size="10px", color=T.ERROR)),
                            width="100%"
                        ),
                        rx.hstack(
                            rx.input(
                                value=AdminUsersState.editing_email, 
                                on_change=AdminUsersState.set_editing_email,
                                width="100%", 
                                background=T.BG_SECONDARY
                            ),
                            rx.button(
                                rx.cond(AdminUsersState.is_saving_email, rx.spinner(size="2"), rx.icon("save", size=16)),
                                on_click=AdminUsersState.save_user_email,
                                disabled=AdminUsersState.is_saving_email,
                                color_scheme="purple",
                                variant="solid",
                                cursor="pointer"
                            ),
                            width="100%"
                        ),
                        width="100%",
                        align_items="start"
                    ),
                    rx.vstack(
                        rx.text("Recuperación", font_size=T.TEXT_XS, color=T.TEXT_MUTED),
                        rx.button(
                            "Enviar enlace de reseteo",
                            on_click=AdminUsersState.send_reset_email,
                            disabled=AdminUsersState.reset_email_sent,
                            color_scheme=rx.cond(AdminUsersState.reset_email_sent, "green", "blue"),
                            variant="soft",
                            width="100%",
                            cursor="pointer"
                        ),
                        rx.cond(AdminUsersState.reset_email_sent, rx.text("¡Email enviado con éxito!", font_size="10px", color="green")),
                        rx.cond(AdminUsersState.reset_email_error != "", rx.text(AdminUsersState.reset_email_error, font_size="10px", color="red")),
                        width="100%",
                        align_items="start"
                    ),
                    width="100%", spacing="3", align_items="start"
                ),
                
                rx.text("Nota: El usuario recibirá un correo oficial de Supabase con un enlace seguro.", font_size="10px", color=T.TEXT_MUTED),
                
                rx.divider(margin_top=T.SPACE_4, margin_bottom=T.SPACE_2),
                
                # Gestión
                rx.heading("Privilegios y Progreso", size="3"),
                
                rx.hstack(
                    rx.vstack(
                        rx.text("Rol de Sistema", font_weight="bold"),
                        rx.text("El rol master permite ver el panel de administración.", font_size=T.TEXT_XS, color=T.TEXT_MUTED),
                        align_items="start"
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.cond(AdminUsersState.selected_user["role"] == "master", "Revocar Máster", "Otorgar Máster"),
                        on_click=AdminUsersState.toggle_selected_role,
                        color_scheme=rx.cond(AdminUsersState.selected_user["role"] == "master", "orange", "purple"),
                        variant="soft",
                        cursor="pointer"
                    ),
                    width="100%", align="center", padding=T.SPACE_3, background=T.BG_SECONDARY, border_radius=T.RADIUS_MD,
                ),
                
                rx.hstack(
                    rx.vstack(
                        rx.text("Resetear Cuenta", font_weight="bold", color="red"),
                        rx.text("Borra todo el progreso, XP y racha del usuario.", font_size=T.TEXT_XS, color=T.TEXT_MUTED),
                        align_items="start"
                    ),
                    rx.spacer(),
                    rx.dialog.root(
                        rx.dialog.trigger(rx.button("Reset Total", color_scheme="red", cursor="pointer")),
                        rx.dialog.content(
                            rx.dialog.title("¿Estás seguro?"),
                            rx.dialog.description("Esta acción borrará todas las lecciones completadas y el XP de este usuario. No se puede deshacer."),
                            rx.hstack(
                                rx.dialog.close(rx.button("Cancelar", variant="soft", color_scheme="gray")),
                                rx.dialog.close(rx.button("Sí, Resetear", color_scheme="red", on_click=AdminUsersState.reset_selected_progress)),
                                justify="end", margin_top=T.SPACE_4, gap=T.SPACE_2
                            )
                        )
                    ),
                    width="100%", align="center", padding=T.SPACE_3, background="rgba(239,68,68,0.1)", border_radius=T.RADIUS_MD, margin_top=T.SPACE_2,
                ),
                
                width="100%", align_items="start", spacing="3"
            ),
            
            rx.hstack(
                rx.dialog.close(
                    rx.button(
                        "Cerrar",
                        variant="soft",
                        color_scheme="gray",
                        on_click=AdminUsersState.close_user_modal,
                    ),
                ),
                justify="end",
                margin_top=T.SPACE_6,
            ),
            max_width="500px",
            background=T.BG_PRIMARY,
        ),
        open=AdminUsersState.is_modal_open,
        on_open_change=lambda is_open: rx.cond(is_open, rx.console_log("open"), AdminUsersState.close_user_modal)
    )

def _admin_users() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading("Gestión de Usuarios", size="5"),
            rx.button(
                rx.icon("refresh-cw", size=16),
                "Refrescar", 
                on_click=AdminUsersState.load_users,
                variant="soft",
                cursor="pointer",
            ),
            justify="between",
            align="center",
            margin_bottom=T.SPACE_4,
        ),
        rx.cond(
            AdminUsersState.is_loading,
            rx.center(rx.spinner(size="3"), height="200px"),
            rx.vstack(
                rx.foreach(
                    AdminUsersState.users,
                    lambda user: rx.hstack(
                        rx.vstack(
                            rx.text(user["email"].to(str), font_weight="bold"),
                            rx.hstack(
                                rx.badge(user["role"].to(str), color_scheme=rx.cond(user["role"] == "master", "purple", "gray")),
                                rx.text(f"XP: {user['xp'].to(str)} | Racha: {user['streak'].to(str)}", font_size=T.TEXT_XS, color=T.TEXT_MUTED),
                                gap=T.SPACE_2,
                            ),
                            align_items="start",
                            flex="1",
                        ),
                        rx.button(
                            rx.icon("eye", size=16),
                            on_click=lambda _: AdminUsersState.open_user_modal(user),
                            color_scheme="gray",
                            variant="ghost",
                            cursor="pointer",
                        ),
                        width="100%", align="center", padding=T.SPACE_4,
                        border=f"1px solid {T.BORDER}", border_radius=T.RADIUS_MD,
                        background=T.BG_SECONDARY,
                        _hover={"border_color": T.BRAND_MEDIUM}
                    )
                ),
                width="100%", spacing="3",
            )
        ),
        _user_modal(),
        width="100%",
    )


def admin_page() -> rx.Component:
    return app_layout(
        rx.box(
            rx.heading("Panel de Administración", size="8", margin_bottom=T.SPACE_6),
            rx.text("Aquí puedes gestionar todo el contenido de SKILLOGIC.", color=T.TEXT_SECONDARY, margin_bottom=T.SPACE_8),
            
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Usuarios", value="users"),
                    rx.tabs.trigger("Módulos", value="modules"),
                    rx.tabs.trigger("Proyectos", value="projects"),
                    rx.tabs.trigger("Día a Día", value="daily"),
                    margin_bottom=T.SPACE_6,
                ),
                rx.tabs.content(_admin_users(), value="users"),
                rx.tabs.content(_admin_modules(), value="modules"),
                rx.tabs.content(_admin_projects(), value="projects"),
                rx.tabs.content(_admin_daily(), value="daily"),
                default_value="users",
            ),
            
            padding=T.SPACE_8,
            width="100%",
            max_width="800px",
            margin="0 auto",
        )
    )
