import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.components.landing.helpers import t

def faq_section() -> rx.Component:
    """FAQ section with accordion."""
    
    def faq_item(question: str, answer: str) -> rx.Component:
        return rx.accordion.item(
            header=rx.accordion.trigger(
                rx.text(question, font_weight=T.WEIGHT_BOLD, font_size=T.TEXT_LG, color=T.TEXT_PRIMARY),
            ),
            content=rx.accordion.content(
                rx.text(answer, color=T.TEXT_SECONDARY, line_height="1.6", font_size=T.TEXT_BASE),
            ),
            value=question,
            border_bottom=f"1px solid {T.BORDER_SUBTLE}",
            padding_y=T.SPACE_2,
        )

    return rx.box(
        rx.vstack(
            rx.text(
                t("Preguntas Frecuentes", "Frequently Asked Questions"), 
                font_size=T.TEXT_SM, font_weight=T.WEIGHT_BOLD, color=T.BRAND, letter_spacing="1px", text_transform="uppercase"
            ),
            rx.text(
                t("Resolvemos tus dudas", "We answer your questions"), 
                font_size=T.TEXT_3XL, font_weight=T.WEIGHT_EXTRABOLD, color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_8, text_align="center"
            ),
            rx.accordion.root(
                faq_item(
                    t("¿Necesito conocimientos previos?", "Do I need prior knowledge?"),
                    t("No. SKILLOGIC está diseñado para llevarte desde cero absoluto hasta dominar la programación con Python. Empezamos con los conceptos más básicos.", "No. SKILLOGIC is designed to take you from absolute zero to mastering Python programming. We start with the most basic concepts.")
                ),
                faq_item(
                    t("¿Tengo que instalar algo en mi computadora?", "Do I need to install anything on my computer?"),
                    t("Para nada. Nuestro IDE interactivo funciona 100% en tu navegador. Puedes escribir, ejecutar y validar tu código directamente en la plataforma.", "Not at all. Our interactive IDE works 100% in your browser. You can write, execute and validate your code directly on the platform.")
                ),
                faq_item(
                    t("¿Cómo funciona el sistema de gamificación?", "How does the gamification system work?"),
                    t("Cada vez que completas una lección o resuelves un Kata, ganas Puntos de Experiencia (XP). También mantienes una racha por días consecutivos programando, lo que te ayuda a construir el hábito.", "Every time you complete a lesson or solve a Kata, you earn Experience Points (XP). You also keep a streak for consecutive days coding, helping you build the habit.")
                ),
                faq_item(
                    t("¿El acceso es gratuito?", "Is access free?"),
                    t("Sí, puedes crear tu cuenta de forma completamente gratuita y acceder a los primeros módulos y katas sin ningún costo para empezar a aprender hoy mismo.", "Yes, you can create your account completely for free and access the first modules and katas at no cost to start learning today.")
                ),
                width="100%",
                max_width="800px",
                type="multiple",
                collapsible=True,
                variant="ghost",
                color_scheme="gray",
            ),
            align="center",
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding=f"{T.SPACE_16} {T.SPACE_4}",
        ),
        background=T.BG_PRIMARY,
    )