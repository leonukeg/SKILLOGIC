# Contenido de la Lección 2.1: Funciones — La Unidad de Abstracción
# Siguiendo la metodología SKILLOGIC

LESSON_2_1 = {
    "title": "Funciones — La Unidad de Abstracción",
    "level": "Intermedio",
    
    "steps": {
        "1_hook": {
            "type": "text",
            "content": "Imagina que eres un cajero en un supermercado y te dan las instrucciones matemáticas detalladas para calcular el IVA cada vez que cobras un producto. Te volverías loco. En su lugar, simplemente aprietas un botón llamado 'Calcular Impuesto' en la caja registradora. En programación, tú eres quien construye esos botones. Ese botón se llama Función."
        },
        
        "2_challenge": {
            "type": "parsons",
            "blocks": [
                {"id": "b1", "text": "def saludar(nombre):"},
                {"id": "b2", "text": "    mensaje = f'Hola {nombre}'"},
                {"id": "b3", "text": "    return mensaje"},
                {"id": "b4", "text": "saludo_final = saludar('Alex')"},
                {"id": "b5", "text": "print(saludo_final)"}
            ],
            "correct_order": ["b1", "b2", "b3", "b4", "b5"],
            "explanation": "Primero 'definimos' (def) la función y qué necesita (un nombre). Dentro de su bloque, procesamos los datos y USAMOS 'return' para devolver el resultado al mundo exterior. Finalmente, llamamos a la función enviándole 'Alex' y guardamos su regalo en una variable antes de imprimirlo."
        },
        
        "3_theory": {
            "type": "text",
            "content": "### ¿Qué es una Función? ⚙️\nUna función es una mini-fábrica. Toma materias primas (**parámetros**), hace un trabajo interno usando variables locales, y escupe un producto final (**return**).\n\n### `def` y la Anatomía\nPara crear (definir) una función en Python usamos `def`, seguido del nombre (en minúsculas), paréntesis `()` y dos puntos `:`.\n\n```python\ndef sumar(a, b):\n    resultado = a + b\n    return resultado\n```\n\n### La regla de oro: `return` vs `print` 👑\n- `print()` simplemente muestra un texto en la pantalla para que un humano lo lea. El programa lo olvida al instante.\n- `return` le devuelve físicamente un dato al programa para que pueda ser almacenado en una variable o usado en cálculos futuros. **Las funciones serias usan return.**\n\n### Scope (El efecto Las Vegas) 🎲\nLo que pasa dentro de una función, se queda dentro de la función. Si creas una variable `total` dentro del bloque `def`, esa variable dejará de existir en cuanto termine la función. Se llama *Scope Local*."
        },
        
        "4_guided_build": {
            "type": "code",
            "statement": "Completa la fábrica de sumar. Debe recibir `a` y `b`, sumarlos y RETORNAR (no imprimir) el resultado.",
            "starter_code": "____ sumar(a, b):\n    total = a + b\n    ____ total\n",
            "solution": "def sumar(a, b):\n    total = a + b\n    return total\n"
        },
        
        "5_struggle": {
            "type": "code",
            "statement": "Crea una función llamada `es_mayor_de_edad(edad)`.\nDebe retornar el booleano `True` si la edad es mayor o igual a 18.\nDebe retornar el booleano `False` si es menor a 18.\n*(Asegúrate de que retorne booleanos, no textos)*.",
            "starter_code": "# Escribe tu función aquí\n",
            "solution": "def es_mayor_de_edad(edad):\n    if edad >= 18:\n        return True\n    else:\n        return False\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": []
            } # Reflex testará la función importando o corriendo comprobaciones manuales (simplificado aquí).
        },
        
        "6_feedback": {
            "type": "mapping",
            "errors": [
                {
                    "error_type": "NameError",
                    "free": "NameError: name 'es_mayor_de_edad' is not defined",
                    "pro": "No nombraste la función correctamente. Recuerda usar `def es_mayor_de_edad(edad):`"
                },
                {
                    "error_type": "AssertionError",
                    "free": "None",
                    "pro": "¿Imprimiste en lugar de retornar? Si usas print, la función por debajo devuelve 'None' y por eso falla. Cambia 'print' por 'return'."
                }
            ]
        },
        
        "7_build": {
            "type": "code",
            "statement": "MINI PROYECTO: La Calculadora de Descuentos.\nCrea una función `calcular_descuento(precio, porcentaje_descuento)`.\n1. Calcula el descuento matemático: `descuento = precio * (porcentaje_descuento / 100)`\n2. Calcula el precio final: `precio - descuento`\n3. Retorna el precio final.\n\nEjemplo: `calcular_descuento(100, 20)` debe retornar `80`.",
            "starter_code": "def calcular_descuento(precio, porcentaje_descuento):\n    # Tu lógica aquí\n    pass\n",
            "solution": "def calcular_descuento(precio, porcentaje_descuento):\n    descuento = precio * (porcentaje_descuento / 100)\n    precio_final = precio - descuento\n    return precio_final\n"
        },
        
        "8_retrieval": {
            "type": "code",
            "statement": "RETO SORPRESA: Identificando el retorno.\nSi una función usa `print(\"Hola\")` pero NUNCA tiene la palabra `return` escrita en su código... ¿qué valor exacto devuelve Python por defecto al llamarla? Imprime la respuesta.",
            "starter_code": "print(____)\n",
            "solution": "print(\"None\")\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["None"]
            }
        },
        
        "9_summary": {
            "type": "text",
            "content": "## ¡Te convertiste en un Arquitecto! 🏛️\n\nYa no escribes simples scripts lineales. Acabas de aprender a crear bloques de construcción reutilizables.\n\n### Resumen de tu Arsenal 🧠:\n1. **`def`:** La palabra mágica que le enseña a Python un nuevo verbo.\n2. **Parámetros:** La materia prima que necesita tu función para operar.\n3. **`return`:** El puente que envía los datos procesados de vuelta al programa principal.\n\n### Próximo Paso 🚀\nTus funciones ahora pueden procesar un dato a la vez. ¿Pero qué pasaría si quisieras pasarle una base de datos con 10,000 usuarios a tu función? En la siguiente lección entraremos en la estructura de datos más famosa del mundo: Las **Listas**."
        }
    }
}
