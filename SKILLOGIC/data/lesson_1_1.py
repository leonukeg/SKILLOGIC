# Contenido de la Lección 1.1: Como piensa una computadora + Variables y Tipos
# Siguiendo la metodología SKILLOGIC

LESSON_1_1 = {
    "title": "Cómo piensa una computadora + Variables y Tipos",
    "level": "Principiante absoluto",
    
    "steps": {
        "1_hook": {
            "type": "text",
            "content": "Un banco guarda tu saldo bancario como texto en lugar de número. Cuando el sistema intenta sumarle tu último depósito, en lugar de 100 + 50 = 150, la pantalla muestra '10050'. ¿Por qué una computadora necesita que le digas explícitamente la diferencia entre el texto '100' y el número 100?"
        },
        
        "2_challenge": {
            "type": "parsons",
            "blocks": [
                {"id": "b1", "text": "Guarda la respuesta en una etiqueta llamada 'edad'."},
                {"id": "b2", "text": "Pídele al usuario que escriba su edad."},
                {"id": "b3", "text": "Muestra en pantalla: 'El próximo año tendrás X años'."},
                {"id": "b4", "text": "Súmale 1 a la 'edad' para saber cuántos años tendrá el próximo año."}
            ],
            "correct_order": ["b2", "b1", "b4", "b3"],
            "explanation": "El computador procesa línea por línea. Primero debe pedir la información (input), luego almacenarla en una etiqueta (variable), procesar la lógica (sumar 1) y finalmente mostrar el resultado (print). No puedes procesar ni guardar algo que aún no has pedido."
        },
        
        "3_theory": {
            "type": "text",
            "content": "### La Computadora es literal 🤖\nUna computadora lee las instrucciones línea por línea, de arriba hacia abajo. No sabe adivinar ni asumir absolutamente nada. Si le dices que sume dos cosas, intentará hacerlo literalmente según su tipo.\n\n### Las Variables: Tu memoria a corto plazo 📦\nPara recordar información, usamos **variables**. Imagina una variable como una etiqueta con un nombre que le pegas a un dato para encontrarlo después. No es una caja donde metes cosas, es solo una etiqueta apuntando a un valor.\nPor ejemplo: `edad = 25`. Has pegado la etiqueta 'edad' al valor 25.\n\n### Tipos de Datos: Hablando el mismo idioma 🗣️\nLa computadora distingue estrictamente entre los **tipos** de datos:\n- `int` (Integer): Números enteros puros (ej. `10`, `42`). ¡Ideales para matemáticas!\n- `str` (String): Texto (ej. `'10'`, `'Hola'`). Va siempre entre comillas. Para la computadora, un string es solo un dibujo de caracteres.\n\n**¿Qué pasa si los mezclas?**\n- Si sumas `10 + 10` (enteros), obtienes `20`.\n- Si sumas `'10' + '10'` (strings), la computadora los pega uno al lado del otro (concatenación) y obtienes `'1010'`.\n- Si sumas `10 + '10'`, ¡la computadora entra en pánico y lanza un error! No sabe si sumar matemáticamente o pegar los textos.\n\n### Herramientas clave (Funciones Integradas) 🛠️\n- `input(\"Pregunta: \")`: Detiene el programa, hace una pregunta y **espera** a que el usuario escriba algo. **Regla de oro:** Todo lo que el usuario escribe, el computador lo captura como texto (`str`).\n- `int(texto)`: Convierte un texto que contiene un número (como `'25'`) en un entero real (`25`) con el que puedes hacer matemáticas.\n- `len(texto)`: Cuenta cuántos caracteres (letras/espacios) tiene un texto.\n- **f-strings** (`f\"Hola {nombre}\"`): La magia moderna de Python. Permiten inyectar variables directamente dentro del texto. Solo pon una `f` antes de las comillas y la variable entre llaves `{}`."
        },
        
        "4_guided_build": {
            "type": "code",
            "statement": "Completa el código para saludar al usuario y mostrar cuántos caracteres tiene su nombre.\nUsa la función `input()` para pedir el texto, `len()` para contar la longitud, y una f-string (texto con una 'f' al principio) para imprimir.",
            "starter_code": "nombre = ____(\"¿Cuál es tu nombre? \")\ncantidad = len(____)\nprint(f\"Hola {____}, tu nombre tiene {____} letras.\")\n",
            "solution": "nombre = input(\"¿Cuál es tu nombre? \")\ncantidad = len(nombre)\nprint(f\"Hola {nombre}, tu nombre tiene {cantidad} letras.\")\n"
        },
        
        "5_struggle": {
            "type": "code",
            "statement": "Crea un programa que calcule en qué año naciste. Debe:\n1. Preguntar '¿Cuántos años tienes?'\n2. Convertir esa respuesta en un número entero usando `int()`.\n3. Restarlo al año actual (2024).\n4. Imprimir exactamente: 'Naciste en el año XXXX' (reemplazando XXXX por el resultado).",
            "starter_code": "# Escribe tu código aquí\n",
            "solution": "edad_str = input(\"¿Cuántos años tienes? \")\nedad = int(edad_str)\nanio = 2024 - edad\nprint(f\"Naciste en el año {anio}\")\n",
            "validation": {
                "inputs": [["25"], ["30"]],
                "expected_outputs": ["Naciste en el año 1999", "Naciste en el año 1994"]
            }
        },
        
        "6_feedback": {
            "type": "mapping",
            "errors": [
                {
                    "error_type": "TypeError",
                    "free": "TypeError: unsupported operand type(s) for -: 'int' and 'str'",
                    "pro": "Estás intentando restar un número y un texto. Recuerda que la función input() SIEMPRE devuelve texto (str). ¿Con qué función puedes convertir ese texto en un número entero antes de hacer la resta matemática?"
                },
                {
                    "error_type": "NameError",
                    "free": "NameError: name '...' is not defined",
                    "pro": "Python te está diciendo que no conoce una palabra que acabas de usar. Revisa cómo escribiste la función para pedir datos o el nombre de tu variable. Las etiquetas tienen que escribirse exactamente igual en todos lados."
                },
                {
                    "error_type": "ValueError",
                    "free": "ValueError: invalid literal for int() with base 10",
                    "pro": "Le pasaste un texto inválido a int(), pero int() solo sabe convertir textos que contienen puramente números, como '20'. Asegúrate de que cuando te pregunte, ingreses un número y no letras."
                }
            ]
        },
        
        "7_build": {
            "type": "code",
            "statement": "MINI PROYECTO: Calculadora de IMC (Índice de Masa Corporal).\nCrea un programa que:\n1. Pida el peso en kilogramos.\n2. Pida la altura en metros.\n3. Calcule el IMC con la fórmula: peso / (altura * altura)\n4. Imprima: 'Tu IMC es de [resultado]'.\n\nTIP: Para la altura vas a necesitar decimales. Usa `float()` en lugar de `int()` para convertir el input.",
            "starter_code": "# Proyecto IMC\n",
            "solution": "peso = float(input(\"Peso (kg): \"))\naltura = float(input(\"Altura (m): \"))\nimc = peso / (altura * altura)\nprint(f\"Tu IMC es de {imc}\")\n",
            "validation": {
                "inputs": [["70", "1.75"]],
                "expected_outputs": ["Tu IMC es de 22.857142857142858"]
            }
        },
        
        "8_retrieval": {
            "type": "code",
            "statement": "RETO SORPRESA: Tienes la variable `precio = '50'` y la variable `impuesto = 10`. Calcula y muestra en pantalla el total de sumarlos. Recuerda arreglar el tipo de dato que está mal.",
            "starter_code": "precio = \"50\"\nimpuesto = 10\n# Calcula e imprime el total abajo\n",
            "solution": "precio = \"50\"\nimpuesto = 10\ntotal = int(precio) + impuesto\nprint(total)\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["60"]
            }
        },
        
        "9_summary": {
            "type": "text",
            "content": "## ¡Módulo 1 Completado con Éxito! 🏆\n\nHas dominado los cimientos absolutos de la programación.\n\n### Resumen de tu Arsenal 🧠:\n1. **Variables:** Las etiquetas que usamos para guardar información en la memoria (`nombre = \"Alex\"`).\n2. **Tipos de Datos:** Entendiste por qué `10` (entero) y `'10'` (texto) son mundos distintos para la máquina.\n3. **Inputs:** Aprendiste a interactuar con el usuario pausando el programa con `input()`.\n4. **Conversión:** Descubriste cómo usar `int()` y `float()` para transformar textos en números reales.\n5. **F-Strings:** Dominaste la forma más elegante de mezclar texto y variables (`f\"Hola {nombre}\"`).\n\n### ¿Qué sigue ahora? 🚀\nLa teoría sin práctica se evapora. Tu siguiente paso es el **Dojo de Katas**.\n\nDirígete a la sección de **Katas** en tu panel principal y resuelve los desafíos de Nivel Fácil (como el 'Intercambio de Colores' o 'El Contador de Letras'). Cada Kata te dará Puntos de Experiencia (XP) para subir tu rango de programación.\n\n¡La lógica ya está en ti, ahora toca entrenarla!"
        }
    }
}
