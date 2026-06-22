import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

# Para modo de pruebas usamos el dominio de resend (solo envía a tu propio correo verificado en resend)
# Cuando tengas un dominio verificado (ej: hi@skillogic.app), se cambia aquí.
FROM_EMAIL = "onboarding@resend.dev"

def send_welcome_email(to_email: str, name: str = "Developer"):
    """
    1. Correo de Bienvenida y Onboarding
    Fórmula: PAS (Problema -> Agitación -> Solución)
    """
    subject = "Tu viaje en Python empieza hoy 🐍 (Adiós a los tutoriales aburridos)"
    html_content = f"""
    <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; color: #333;">
        <h2>¡Bienvenido al Dojo, {name}! 🥋</h2>
        <p>¿Cuántas veces has intentado aprender a programar viendo videos de horas en YouTube, solo para quedarte en blanco cuando te toca escribir código desde cero?</p>
        <p>Ese es el famoso <strong>'Tutorial Hell'</strong>. Pasa porque ver a otro programar no te enseña a programar, de la misma forma que ver fútbol no te hace futbolista.</p>
        <p>En SKILLOGIC hemos diseñado un sistema diferente:</p>
        <ul>
            <li>Escribes código desde el <strong>minuto uno</strong>.</li>
            <li>Obtienes <strong>feedback instantáneo</strong> cuando te equivocas.</li>
            <li>Construyes <strong>memoria muscular</strong> ganando XP y manteniendo rachas.</li>
        </ul>
        <div style="text-align: center; margin: 30px 0;">
            <a href="https://skillogic.app/dashboard" style="background-color: #6C63FF; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold;">Escribir mi primera línea de código</a>
        </div>
        <p>Prepárate para subir de nivel.</p>
        <p>Un saludo,<br><strong>El equipo de SKILLOGIC</strong></p>
    </div>
    """
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
    """
    2. El Kata del Día (Retención Diaria)
    Fórmula: Gamificación / Urgencia
    """
    subject = "⚔️ Nuevo Kata de Python disponible (XP x2)"
    html_content = f"""
    <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; color: #333;">
        <h2 style="color: #6C63FF;">¡El Kata del Día te espera!</h2>
        <p>El algoritmo de hoy evaluará tu lógica. Tienes 24 horas para resolver el desafío <strong>"{kata_title}"</strong> y llevarte el doble de Puntos de Experiencia (XP).</p>
        <div style="text-align: center; margin: 30px 0;">
            <a href="https://skillogic.app/katas" style="background-color: #10b981; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold;">Aceptar el Reto</a>
        </div>
        <p>Recuerda que resolver problemas diarios es la única forma real de construir memoria muscular como programador.</p>
    </div>
    """
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
    """
    3. Correo Promocional (Invitación Newsletter desde la Landing)
    Fórmula: AIDA o Beneficio Directo. Para leads no registrados.
    """
    subject = "El secreto para dominar Python en tiempo récord 🚀"
    html_content = f"""
    <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; color: #333;">
        <h2 style="color: #6C63FF;">Gracias por suscribirte a nuestro Newsletter 🎉</h2>
        <p>A partir de hoy, recibirás tips semanales para mejorar tu lógica de programación.</p>
        <p>Pero... ¿sabías que la mejor forma de aprender no es leyendo, sino haciendo?</p>
        <p>Miles de estudiantes ya están ganando experiencia y subiendo de nivel en nuestro Dojo interactivo. No necesitas instalar nada, todo funciona en tu navegador.</p>
        <div style="background-color: #f3f4f6; padding: 15px; border-radius: 8px; margin: 20px 0;">
            <strong>Regístrate hoy gratis</strong> y accede a nuestros módulos interactivos y Katas de código.
        </div>
        <div style="text-align: center; margin: 30px 0;">
            <a href="https://skillogic.app/register" style="background-color: #f59e0b; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold;">Crear mi cuenta gratis</a>
        </div>
        <p>Te esperamos adentro.</p>
    </div>
    """
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
    """
    4. El Salvavidas de Racha (Re-engagement)
    Fórmula: Loss Aversion (Aversión a la pérdida)
    """
    subject = "🔥 Tu racha de programación está en peligro"
    html_content = f"""
    <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; color: #333;">
        <h2 style="color: #ef4444;">¡No pierdas tu progreso, {name}!</h2>
        <p>Llevas <strong>{current_streak} días</strong> seguidos programando. Has construido un hábito increíble que muy pocos logran.</p>
        <p>Hemos notado que hoy no has resuelto ningún ejercicio. Si el día termina sin que escribas código, tu racha volverá a cero 🥶.</p>
        <p>Solo te tomará 2 minutos entrar y resolver un Kata rápido para mantener la llama viva.</p>
        <div style="text-align: center; margin: 30px 0;">
            <a href="https://skillogic.app/dashboard" style="background-color: #ef4444; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold;">Salvar mi racha ahora</a>
        </div>
        <p>Tú puedes.</p>
    </div>
    """
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
