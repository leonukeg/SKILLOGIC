import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Configurar API Key
api_key = os.getenv("GEMINI_API_KEY", "")
if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None

def get_ai_hint(user_code: str, error_message: str, kata_description: str) -> str:
    """
    Envía el código fallido a la IA para que devuelva una pequeña pista.
    """
    if not api_key:
        # Fallback si no hay API Key configurada
        return f"🚨 Error crudo de Python detectado: {error_message.splitlines()[-1] if error_message.splitlines() else error_message}\n\n(Tip CPO: Configura tu GEMINI_API_KEY en .env para activar al AI Sensei y recibir pistas personalizadas)."

    try:
        prompt = f"""
        Actúa como un profesor de programación experto pero muy estricto y socrático (al estilo del Señor Miyagi o un Sensei zen).
        Un estudiante está resolviendo este desafío de Python:
        "{kata_description}"
        
        Su código actual es:
        ```python
        {user_code}
        ```
        
        Y al ejecutarlo, arrojó este error o falló en el test:
        ```
        {error_message}
        ```
        
        TU MISIÓN:
        Dale una sola pista corta (máximo 2 líneas) de lo que está haciendo mal o de la línea donde está el error.
        REGLAS ESTRICTAS:
        1. NUNCA, bajo NINGUNA circunstancia, le des el código corregido o la respuesta directa.
        2. Mantén un tono alentador pero enigmático.
        3. Háblale directamente al estudiante.
        """
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"Error llamando a Gemini: {e}")
        return f"El AI Sensei está meditando ahora mismo... (Falla de conexión: {str(e)})"
