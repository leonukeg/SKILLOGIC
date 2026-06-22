import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.components.landing.navbar import landing_navbar
from SKILLOGIC.components.landing.hero import hero_section
from SKILLOGIC.components.landing.stats import stats_section
from SKILLOGIC.components.landing.problem_solution import problem_solution_section
from SKILLOGIC.components.landing.features import features_section
from SKILLOGIC.components.landing.how_it_works import how_it_works_section
from SKILLOGIC.components.landing.testimonials import testimonials_section
from SKILLOGIC.components.landing.faq import faq_section
from SKILLOGIC.components.landing.cta import bottom_cta_section
from SKILLOGIC.components.landing.footer import footer
from SKILLOGIC.components.landing.cookie_banner import cookie_banner
from SKILLOGIC.components.landing.newsletter_banner import newsletter_banner

@rx.page(
    route="/",
    title="SKILLOGIC — Aprende Python desde cero de forma interactiva",
    description="Aprende Python desde cero resolviendo problemas reales en tu navegador. Gana experiencia, sube de nivel y domina la programación. ¡Empieza gratis hoy!",
    meta=[
        {"name": "keywords", "content": "aprender python, curso de python, python desde cero, programación interactiva, aprender a programar, python en español"},
        {"name": "robots", "content": "index, follow"},
        {"property": "og:type", "content": "website"},
        {"property": "og:title", "content": "SKILLOGIC — Aprende Python de forma interactiva"},
        {"property": "og:description", "content": "Aprende Python desde cero resolviendo problemas reales en tu navegador. ¡Empieza gratis hoy!"},
        {"property": "og:site_name", "content": "SKILLOGIC"},
        {"property": "twitter:card", "content": "summary_large_image"},
        {"property": "twitter:title", "content": "SKILLOGIC — Aprende Python"},
        {"property": "twitter:description", "content": "Aprende a programar resolviendo problemas reales en tu navegador."},
        {"rel": "canonical", "href": "https://skillogic.app/"}
    ]
)
def landing_page() -> rx.Component:
    """The main landing page composed of multiple marketing sections."""
    return rx.box(
        landing_navbar(),
        hero_section(),
        stats_section(),
        problem_solution_section(),
        features_section(),
        how_it_works_section(),
        testimonials_section(),
        faq_section(),
        bottom_cta_section(),
        footer(),
        cookie_banner(),
        newsletter_banner(),
        background=T.BG_PRIMARY,
        min_height="100vh",
        width="100%",
        font_family=T.FONT_BODY,
    )

