# Contenido de la Lección 1.4: For Loops y While Loops
# Siguiendo la metodología SKILLOGIC

LESSON_1_4 = {
    "title": "For Loops y While Loops — Repetición con Control",
    "level": "Principiante",
    
    "steps": {
        "1_hook": {
            "type": "text",
            "content": "Si tu jefe te pide enviar 10 correos electrónicos, podrías copiar y pegar tu código 10 veces. Pero, ¿qué pasa si te pide enviar 100,000 correos? Copiar y pegar destruiría tu archivo. Aquí es donde entran los bucles (loops), la verdadera fuerza bruta incansable de una computadora."
        },
        
        "2_challenge": {
            "type": "parsons",
            "blocks": [
                {"id": "b1", "text": "contador = 3"},
                {"id": "b2", "text": "while contador > 0:"},
                {"id": "b3", "text": "    print(contador)"},
                {"id": "b4", "text": "    contador = contador - 1"},
                {"id": "b5", "text": "print('¡Despegue!')"}
            ],
            "correct_order": ["b1", "b2", "b3", "b4", "b5"],
            "explanation": "Un bucle 'while' (mientras) repite el código que tiene dentro siempre que su condición sea True. Para evitar que se repita infinitamente, debemos cambiar el valor del contador por dentro (restándole 1 en cada vuelta)."
        },
        
        "3_theory": {
            "type": "text",
            "content": "### Los dos motores de repetición 🔄\nPython te da dos formas de repetir código dependiendo de lo que necesites.\n\n### 1. El Bucle `for` (El Recorredor Seguro)\nSe usa cuando **sabes exactamente** cuántas veces quieres repetir algo o tienes una colección definida de elementos.\n```python\nfor i in range(5):\n    print(i)\n```\n- `range(5)` genera los números: 0, 1, 2, 3, 4.\n- La variable `i` toma cada uno de esos valores en cada vuelta.\n\n### 2. El Bucle `while` (El Vigía Persistente)\nSe usa cuando **NO sabes** cuántas veces se repetirá, solo sabes que debe detenerse cuando se cumpla una condición.\n```python\nwhile bateria > 0:\n    jugar()\n```\n**Peligro Mortal ☠️:** Si la condición del `while` nunca se vuelve falsa, crearás un 'bucle infinito' y colgarás la computadora.\n\n### Controles de Emergencia 🛑\n- `break`: Destruye el bucle y te saca de él inmediatamente.\n- `continue`: Salta el resto del código de esta vuelta y pasa directamente a la siguiente iteración."
        },
        
        "4_guided_build": {
            "type": "code",
            "statement": "Usa un bucle `for` y la función `range()` para imprimir la palabra 'Cargando...' exactamente 3 veces.",
            "starter_code": "____ _ in ____(3):\n    print(\"Cargando...\")\n",
            "solution": "for _ in range(3):\n    print(\"Cargando...\")\n"
        },
        
        "5_struggle": {
            "type": "code",
            "statement": "Crea una cuenta regresiva para un cohete usando un bucle `while`.\n1. Crea una variable `tiempo = 5`.\n2. Mientras el `tiempo` sea mayor a 0, imprime el número.\n3. NO TE OLVIDES de restarle 1 a la variable `tiempo` en cada vuelta.\n4. Cuando el bucle termine, imprime exactamente '¡Despegue!'.",
            "starter_code": "tiempo = 5\n# Escribe tu bucle while aquí\n",
            "solution": "tiempo = 5\nwhile tiempo > 0:\n    print(tiempo)\n    tiempo = tiempo - 1\nprint(\"¡Despegue!\")\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["5\n4\n3\n2\n1\n¡Despegue!"]
            }
        },
        
        "6_feedback": {
            "type": "mapping",
            "errors": [
                {
                    "error_type": "TimeoutError",
                    "free": "Execution timed out",
                    "pro": "¡Creaste un bucle infinito! Esto pasa en los bucles 'while' cuando te olvidas de actualizar la variable de control (por ejemplo, restar el tiempo). Si 'tiempo' siempre vale 5, 'tiempo > 0' siempre será True y nunca parará."
                },
                {
                    "error_type": "NameError",
                    "free": "NameError: name 'range' is not defined",
                    "pro": "Asegúrate de haber escrito bien la palabra 'range' con minúsculas."
                }
            ]
        },
        
        "7_build": {
            "type": "code",
            "statement": "MINI PROYECTO: Sistema de Seguridad Bancario.\nCrea un programa que pida un PIN de 4 dígitos usando `input(\"PIN: \")`.\n- Mientras el PIN introducido no sea '1234', el programa debe imprimir 'PIN incorrecto' y volver a pedirlo.\n- Cuando el usuario introduzca '1234', el bucle debe romperse e imprimir 'Caja fuerte abierta'.\n\nTIP: Esto es perfecto para un bucle `while` porque no sabes si el usuario acertará al primer intento o al intento 100.",
            "starter_code": "# Proyecto de Seguridad\npin = input(\"PIN: \")\n",
            "solution": "pin = input(\"PIN: \")\nwhile pin != \"1234\":\n    print(\"PIN incorrecto\")\n    pin = input(\"PIN: \")\nprint(\"Caja fuerte abierta\")\n",
            "validation": {
                "inputs": [["0000", "9999", "1234"], ["1234"]],
                "expected_outputs": ["PIN incorrecto\nPIN incorrecto\nCaja fuerte abierta", "Caja fuerte abierta"]
            }
        },
        
        "8_retrieval": {
            "type": "code",
            "statement": "RETO SORPRESA: La magia de range().\nUn `range(1, 4)` NO imprime el número 4. Escribe un `for` usando `range` que imprima los números 1, 2 y 3 (uno en cada línea).",
            "starter_code": "# Haz el loop aquí\n",
            "solution": "for i in range(1, 4):\n    print(i)\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["1\n2\n3"]
            }
        },
        
        "9_summary": {
            "type": "text",
            "content": "## ¡Has domado a la bestia repetitiva! 🔄\n\nAcabas de automatizar el tiempo y esfuerzo. Tu código ahora hace miles de tareas en milisegundos.\n\n### Resumen de tu Arsenal 🧠:\n1. **`for` loop:** Tu mejor amigo cuando sabes la cantidad exacta de repeticiones (ej. `for i in range(10)`).\n2. **`while` loop:** Tu aliado cuando dependes de una condición (ej. \"mientras el usuario no adivine la clave\").\n3. **Cuidado:** Aprendiste por las malas (o buenas) lo que es un bucle infinito y cómo el control de estado salva tu PC de colapsar.\n\n### Próximo Paso 🚀\nEstás escribiendo programas más grandes, y con ellos... llegan los errores más grandes. En la última lección de este módulo nos convertiremos en forenses de código. Aprenderás a leer e interpretar el texto rojo de terror en la consola: el **Debugging**."
        }
    }
}
