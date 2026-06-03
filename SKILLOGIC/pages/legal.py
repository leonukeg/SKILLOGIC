import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.components.landing.navbar import landing_navbar
from SKILLOGIC.components.landing.footer import footer

def page_layout(title: str, content: str) -> rx.Component:
    return rx.box(
        landing_navbar(),
        rx.box(
            rx.vstack(
                rx.heading(title, size="8", color=T.TEXT_PRIMARY, margin_bottom=T.SPACE_8),
                rx.text(content, color=T.TEXT_SECONDARY, line_height="1.6", white_space="pre-wrap"),
                width="100%",
                max_width="800px",
                margin="0 auto",
                padding_y=T.SPACE_16,
            ),
            padding_x=T.SPACE_4,
            min_height="70vh",
        ),
        footer(),
        background=T.BG_PRIMARY,
        min_height="100vh",
        width="100%",
        font_family=T.FONT_BODY,
    )

@rx.page(route="/terms", title="SKILLOGIC — Términos y Condiciones")
def terms_page() -> rx.Component:
    text = """Última actualización: Junio 2026

Bienvenido a SKILLOGIC. Al acceder o utilizar nuestro sitio web, servicios o contenido, aceptas estar sujeto a estos Términos y Condiciones.

1. Uso del Servicio
SKILLOGIC es una plataforma educativa gamificada para aprender Python. El acceso a ciertas partes de la plataforma es gratuito, mientras que otras pueden requerir una suscripción o pago.

2. Cuentas de Usuario
Eres responsable de mantener la confidencialidad de tu cuenta y contraseña. Nos reservamos el derecho de suspender o cancelar cuentas que violen nuestras políticas.

3. Propiedad Intelectual
Todo el contenido, incluyendo ejercicios, katas, currículum, código fuente (excepto el generado por el usuario), textos y gráficos son propiedad de SKILLOGIC.

4. Conducta del Usuario
Te comprometes a utilizar la plataforma con fines educativos lícitos. Queda prohibido el uso de bots, scraping, o cualquier acción que comprometa la integridad de la plataforma.

Para más información, contáctanos a soporte@skillogic.dev."""
    return page_layout("Términos y Condiciones", text)

@rx.page(route="/privacy", title="SKILLOGIC — Política de Privacidad")
def privacy_page() -> rx.Component:
    text = """Última actualización: Junio 2026

En SKILLOGIC valoramos y respetamos tu privacidad. Esta política describe cómo recopilamos, usamos y protegemos tus datos.

1. Información que recopilamos
Recopilamos la información que nos proporcionas al registrarte (nombre, correo electrónico) y datos sobre tu uso de la plataforma (progreso, código escrito en los katas, tiempo de sesión).

2. Uso de la información
Utilizamos tus datos para:
- Proporcionarte el servicio educativo.
- Guardar tu progreso y XP.
- Mejorar nuestros algoritmos y currículum.
- Enviarte notificaciones importantes sobre tu cuenta.

3. Protección de datos
Implementamos medidas de seguridad estándar de la industria para proteger tu información. No vendemos tus datos a terceros.

4. Tus derechos
Puedes solicitar la eliminación de tu cuenta y todos los datos asociados en cualquier momento contactando a soporte@skillogic.dev."""
    return page_layout("Política de Privacidad", text)

@rx.page(route="/cookies", title="SKILLOGIC — Política de Cookies")
def cookies_page() -> rx.Component:
    text = """Última actualización: Junio 2026

1. ¿Qué son las cookies?
Las cookies son pequeños archivos de texto que se almacenan en tu dispositivo cuando visitas un sitio web. Ayudan a que el sitio funcione correctamente y ofrecen información sobre cómo interactúas con él.

2. ¿Cómo usamos las cookies?
En SKILLOGIC utilizamos:
- Cookies estrictamente necesarias: Para mantener tu sesión activa y guardar tu progreso.
- Cookies de rendimiento: Para entender cómo los usuarios navegan por la plataforma y mejorar el servicio.
- Cookies de preferencias: Para recordar tus ajustes, como el tema oscuro/claro o el idioma.

3. Gestión de cookies
Puedes configurar tu navegador para rechazar las cookies, pero ten en cuenta que algunas funcionalidades de SKILLOGIC (como mantener la sesión iniciada) podrían dejar de funcionar correctamente.

Si tienes dudas, contáctanos a soporte@skillogic.dev."""
    return page_layout("Política de Cookies", text)
