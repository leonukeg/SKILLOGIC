import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.components.landing.helpers import t

def testimonials_section() -> rx.Component:
    """Social proof section with fake/placeholder testimonials."""
    
    def testimonial_card(name: str, role: str, content: str, avatar_color: str) -> rx.Component:
        initials = "".join([n[0] for n in name.split()[:2]])
        
        return rx.box(
            rx.vstack(
                rx.hstack(
                    rx.icon(tag="quote", size=24, color=T.BRAND, opacity="0.5"),
                    rx.spacer(),
                    rx.hstack(
                        rx.icon(tag="star", size=14, color="#F59E0B", fill="currentColor"),
                        rx.icon(tag="star", size=14, color="#F59E0B", fill="currentColor"),
                        rx.icon(tag="star", size=14, color="#F59E0B", fill="currentColor"),
                        rx.icon(tag="star", size=14, color="#F59E0B", fill="currentColor"),
                        rx.icon(tag="star", size=14, color="#F59E0B", fill="currentColor"),
                        gap="2px"
                    ),
                    width="100%"
                ),
                rx.text(content, font_size=T.TEXT_BASE, color=T.TEXT_PRIMARY, line_height="1.6", font_style="italic", margin_y=T.SPACE_4),
                rx.hstack(
                    rx.flex(
                        rx.text(initials, font_weight=T.WEIGHT_BOLD, color="white", font_size=T.TEXT_SM, margin="0", line_height="1"),
                        width="40px", height="40px", border_radius="50%",
                        background=avatar_color,
                        align="center", justify="center",
                    ),
                    rx.vstack(
                        rx.text(name, font_weight=T.WEIGHT_BOLD, font_size=T.TEXT_SM, color=T.TEXT_PRIMARY),
                        rx.text(role, font_size=T.TEXT_XS, color=T.TEXT_MUTED),
                        spacing="0"
                    ),
                    align="center",
                    gap=T.SPACE_3,
                    margin_top="auto"
                ),
                align="start",
                height="100%",
            ),
            background=T.BG_SECONDARY,
            padding=T.SPACE_6,
            border_radius=T.RADIUS_XL,
            border=f"1px solid {T.BORDER}",
            transition=f"transform {T.EASE_BASE}",
            _hover={"transform": "translateY(-5px)", "border_color": T.BORDER_STRONG, "box_shadow": T.SHADOW_MD},
            height="100%"
        )

    return rx.box(
        rx.vstack(
            rx.text(t("Testimonios", "Testimonials"), font_size=T.TEXT_SM, font_weight=T.WEIGHT_BOLD, color=T.BRAND, letter_spacing="1px", text_transform="uppercase"),
            rx.text(t("Lo que dicen nuestros estudiantes", "What our students say"), font_size=T.TEXT_3XL, font_weight=T.WEIGHT_EXTRABOLD, color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_8, text_align="center"),
            
            rx.grid(
                testimonial_card(
                    "Carlos Mendoza", 
                    t("Estudiante de Ingeniería", "Engineering Student"),
                    t("Había intentado aprender Python con videos de YouTube pero me aburría y lo dejaba. La gamificación y los Katas interactivos de SKILLOGIC hicieron que me volviera adicto a programar todos los días.", "I had tried learning Python with YouTube videos but I'd get bored and quit. The gamification and interactive Katas of SKILLOGIC made me addicted to coding every day."),
                    f"linear-gradient(135deg, {T.BRAND}, #a855f7)"
                ),
                testimonial_card(
                    "Ana Torres", 
                    t("Desarrolladora Junior", "Junior Developer"),
                    t("El módulo de Estructuras de Control cambió mi forma de pensar. Al tener que resolver los problemas en el editor directamente en el navegador, retienes la información muchísimo mejor.", "The Control Structures module changed the way I think. By having to solve the problems in the editor right in the browser, you retain information much better."),
                    "linear-gradient(135deg, #10b981, #059669)"
                ),
                testimonial_card(
                    "Roberto Díaz", 
                    t("Analista de Datos", "Data Analyst"),
                    t("Llevaba meses posponiendo aprender Python para mi trabajo. Entré a SKILLOGIC y en dos semanas ya estaba automatizando reportes. La curva de aprendizaje es perfecta.", "I had been putting off learning Python for my job for months. I joined SKILLOGIC and in two weeks I was automating reports. The learning curve is perfect."),
                    "linear-gradient(135deg, #f59e0b, #d97706)"
                ),
                columns=rx.breakpoints(initial="1", md="3"),
                gap=T.SPACE_6,
                width="100%"
            ),
            
            align="center",
            max_width="1200px",
            margin="0 auto",
            padding=f"{T.SPACE_16} {T.SPACE_4}",
        ),
        background=T.BG_PRIMARY,
        margin_top=T.SPACE_10,
    )