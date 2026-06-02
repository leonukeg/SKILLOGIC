import reflex as rx
from SKILLOGIC.state.app_state import AppState

def t(es: str, en: str) -> rx.Component:
    """Helper for i18n text."""
    return rx.cond(AppState.is_spanish, es, en)

