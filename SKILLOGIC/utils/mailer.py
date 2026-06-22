import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

# Para modo de pruebas usamos el dominio de resend (solo envía a tu propio correo verificado en resend)
# Cuando tengas un dominio verificado (ej: hi@skillogic.app), se cambia aquí.
FROM_EMAIL = "onboarding@resend.dev"

def load_template(filename: str, **kwargs) -> str:
    template_path = os.path.join(os.path.dirname(__file__), "email_templates", filename)
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()
            return content.format(**kwargs)
    except Exception as e:
        print(f"Error cargando plantilla {filename}: {e}")
        return ""

def send_welcome_email(to_email: str, name: str = "Developer"):
    subject = "Tu viaje en Python empieza hoy 🐍 (Adiós a los tutoriales aburridos)"
    html_content = load_template("welcome.html", name=name)
    try:
        r = resend.Emails.send({
            "from": FROM_EMAIL,
            "to": to_email,
            "subject": subject,
            "html": html_content
        })
        return r
    except Exception as e:
        print(f"Error enviando correo: {e}")
        return None

def send_daily_kata_email(to_email: str, kata_title: str):
    subject = "⚔️ Nuevo Kata de Python disponible (XP x2)"
    html_content = load_template("daily_kata.html", kata_title=kata_title)
    try:
        r = resend.Emails.send({
            "from": FROM_EMAIL,
            "to": to_email,
            "subject": subject,
            "html": html_content
        })
        return r
    except Exception as e:
        print(f"Error enviando correo: {e}")
        return None

def send_newsletter_promo_email(to_email: str):
    subject = "El secreto para dominar Python en tiempo récord 🚀"
    html_content = load_template("newsletter.html")
    try:
        r = resend.Emails.send({
            "from": FROM_EMAIL,
            "to": to_email,
            "subject": subject,
            "html": html_content
        })
        return r
    except Exception as e:
        print(f"Error enviando correo: {e}")
        return None

def send_streak_recovery_email(to_email: str, name: str, current_streak: int):
    subject = "🔥 Tu racha de programación está en peligro"
    html_content = load_template("streak_recovery.html", name=name, current_streak=current_streak)
    try:
        r = resend.Emails.send({
            "from": FROM_EMAIL,
            "to": to_email,
            "subject": subject,
            "html": html_content
        })
        return r
    except Exception as e:
        print(f"Error enviando correo: {e}")
        return None
