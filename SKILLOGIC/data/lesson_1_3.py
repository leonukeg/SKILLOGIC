# Contenido de la Lección 1.3: Condicionales — Bifurcar el Flujo
# Siguiendo la metodología SKILLOGIC

LESSON_1_3 = {
    "title": "Condicionales — Bifurcar el Flujo",
    "level": "Principiante",
    
    "steps": {
        "1_hook": {
            "type": "text",
            "content": "Imagina que entras a Netflix. El sistema debe revisar si tu suscripción está activa. Si lo está, te deja ver películas; si no, te envía a la página de pago. Esta capacidad de tomar caminos distintos basándose en una condición es lo que le da \"inteligencia\" a todo el software del mundo."
        },
        
        "2_challenge": {
            "type": "parsons",
            "blocks": [
                {"id": "b1", "text": "edad = int(input('¿Qué edad tienes? '))"},
                {"id": "b2", "text": "if edad >= 18:"},
                {"id": "b3", "text": "    print('Puedes entrar al club.')"},
                {"id": "b4", "text": "else:"},
                {"id": "b5", "text": "    print('Vuelve a tu casa, niño.')"}
            ],
            "correct_order": ["b1", "b2", "b3", "b4", "b5"],
            "explanation": "El flujo es simple: Primero preguntamos la edad. Luego verificamos SI (if) es mayor o igual a 18. Si esa afirmación es verdadera, ejecutamos el código indentado debajo. SINO (else), ejecutamos la ruta alternativa."
        },
        
        "3_theory": {
            "type": "text",
            "content": "### Booleanos: Blanco o Negro ⚖️\nEl lenguaje de las computadoras en su nivel más básico. Un dato booleano solo puede tener dos valores:\n- `True` (Verdadero)\n- `False` (Falso)\n\n### Operadores de Comparación 🔍\nGeneran resultados booleanos:\n- `==` (Es exactamente igual a. ¡Ojo! Son DOS iguales. Un solo igual `=` es para asignar variables).\n- `!=` (Es diferente a).\n- `>`, `<`, `>=`, `<=` (Mayor, Menor, Mayor o igual, Menor o igual).\n\n### Estructura if / elif / else 🚦\n- `if` (SI): Abre la condición. Si es `True`, se ejecuta su bloque.\n- `elif` (SINO, SI): Evaluado solo si el `if` anterior falló. Puedes poner tantos como quieras.\n- `else` (SINO): El camino por defecto. Se ejecuta si absolutamente todo lo de arriba falló.\n\n### La Indentación importa 📐\nEn Python no usamos llaves `{}`. Usamos **espacios**. Todo el código que pertenece a un `if` debe estar empujado 4 espacios hacia la derecha. Si rompes la indentación, rompes el programa."
        },
        
        "4_guided_build": {
            "type": "code",
            "statement": "Completa el código del termostato. Si la temperatura es mayor a 30, imprime 'Hace calor'. Si es menor a 15, imprime 'Hace frío'. Si no, imprime 'Clima perfecto'.",
            "starter_code": "temp = 25\n\nif temp ____ 30:\n    print(\"Hace calor\")\n____ temp < 15:\n    print(\"Hace frío\")\n____:\n    print(\"Clima perfecto\")\n",
            "solution": "temp = 25\n\nif temp > 30:\n    print(\"Hace calor\")\nelif temp < 15:\n    print(\"Hace frío\")\nelse:\n    print(\"Clima perfecto\")\n"
        },
        
        "5_struggle": {
            "type": "code",
            "statement": "Crea un sistema de control de acceso para un concierto.\n1. Pide al usuario su edad con `int(input(\"Edad: \"))`.\n2. Si la edad es menor de 13, imprime: 'Prohibido'.\n3. Si la edad está entre 13 y 17 (inclusive), imprime: 'Necesitas acompañante'.\n4. Si es 18 o mayor, imprime: 'Bienvenido al concierto'.",
            "starter_code": "edad = int(input(\"Edad: \"))\n# Escribe tus condicionales aquí\n",
            "solution": "edad = int(input(\"Edad: \"))\nif edad < 13:\n    print(\"Prohibido\")\nelif edad <= 17:\n    print(\"Necesitas acompañante\")\nelse:\n    print(\"Bienvenido al concierto\")\n",
            "validation": {
                "inputs": [["12"], ["15"], ["20"]],
                "expected_outputs": ["Prohibido", "Necesitas acompañante", "Bienvenido al concierto"]
            }
        },
        
        "6_feedback": {
            "type": "mapping",
            "errors": [
                {
                    "error_type": "IndentationError",
                    "free": "IndentationError: expected an indented block",
                    "pro": "¡Te olvidaste de indentar (dar espacios)! Después de los dos puntos `:` de un if/elif/else, la siguiente línea DEBE estar empujada a la derecha."
                },
                {
                    "error_type": "SyntaxError",
                    "free": "SyntaxError: invalid syntax",
                    "pro": "Suele ocurrir si te faltaron los dos puntos `:` al final de la línea del if/elif/else, o si usaste un solo `=` en lugar de `==` para comparar."
                }
            ]
        },
        
        "7_build": {
            "type": "code",
            "statement": "MINI PROYECTO: Verificador de Contraseña Seguro.\nCrea un sistema de login.\n1. Pide al usuario el 'Usuario: ' y la 'Contraseña: '.\n2. Si el usuario es 'admin' Y la contraseña es 'secreto123', imprime 'Acceso concedido'.\n3. Si el usuario es 'admin' pero la contraseña es incorrecta, imprime 'Contraseña incorrecta'.\n4. En cualquier otro caso, imprime 'Usuario no encontrado'.",
            "starter_code": "# Proyecto Login\n",
            "solution": "usuario = input(\"Usuario: \")\npassword = input(\"Contraseña: \")\n\nif usuario == \"admin\" and password == \"secreto123\":\n    print(\"Acceso concedido\")\nelif usuario == \"admin\":\n    print(\"Contraseña incorrecta\")\nelse:\n    print(\"Usuario no encontrado\")\n",
            "validation": {
                "inputs": [["admin", "secreto123"], ["admin", "clavemala"], ["invitado", "secreto123"]],
                "expected_outputs": ["Acceso concedido", "Contraseña incorrecta", "Usuario no encontrado"]
            }
        },
        
        "8_retrieval": {
            "type": "code",
            "statement": "RETO SORPRESA: Operadores Lógicos.\nPython evalúa `and`, `or` y `not`. Adivina e imprime qué devuelve esta operación booleana: `not (True and False)`",
            "starter_code": "# Imprime el resultado de: not (True and False)\nprint(____)\n",
            "solution": "print(not (True and False))\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["True"]
            }
        },
        
        "9_summary": {
            "type": "text",
            "content": "## ¡Tu código ahora piensa! 🤔\n\nAcabas de desbloquear la capacidad de bifurcar la realidad de tu programa.\n\n### Resumen de tu Arsenal 🧠:\n1. **Booleanos:** La base de toda la lógica computacional (`True` / `False`).\n2. **Comparadores:** Las lupas que evalúan la realidad (`==`, `>`, `<`).\n3. **if / elif / else:** Los directores de tráfico que deciden qué bloque de código ejecutar dependiendo de las condiciones.\n\n### Próximo Paso 🚀\nAhora puedes tomar una decisión a la vez. Pero ¿qué pasa si necesitas evaluar a 10,000 usuarios de Netflix de una sola vez? En la siguiente lección, descubriremos el poder destructivo y maravilloso de los **Bucles (Loops)**, la capacidad de repetir código miles de veces en una fracción de segundo."
        }
    }
}
