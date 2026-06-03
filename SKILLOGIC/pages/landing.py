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

@rx.page(
    route="/",
    title="SKILLOGIC — Aprende Python de forma interactiva",
    description="Plataforma gamificada para aprender Python. Supera Katas interactivos, gana XP, mantén tu racha y domina la programación desde cero.",
    meta=[
        {"name": "keywords", "content": "python, aprender python, curso de python, programación interactiva, katas python, python desde cero, tutorial python"},
        {"property": "og:type", "content": "website"},
        {"property": "og:title", "content": "SKILLOGIC — Aprende Python de forma interactiva"},
        {"property": "og:description", "content": "Plataforma gamificada para aprender Python. Supera Katas interactivos, gana XP, mantén tu racha y domina la programación."},
        {"property": "og:site_name", "content": "SKILLOGIC"},
        {"property": "twitter:card", "content": "summary_large_image"},
        {"property": "twitter:title", "content": "SKILLOGIC — Aprende Python"},
        {"property": "twitter:description", "content": "Aprende a programar resolviendo problemas reales en tu navegador."},
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
        background=T.BG_PRIMARY,
        min_height="100vh",
        width="100%",
        font_family=T.FONT_BODY,
    )

