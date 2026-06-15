# Contenido de la Lección 1.5: Debugging
# Siguiendo la metodología SKILLOGIC

LESSON_1_5 = {
    "title": "Debugging — Leer Errores como Programador",
    "level": "Principiante",
    
    "steps": {
        "1_hook": {
            "type": "text",
            "content": "La mayoría de los principiantes entran en pánico cuando ven una pared de texto rojo en la consola. Un profesional sonríe, porque sabe que la computadora le está diciendo EXACTAMENTE qué pasó y en qué línea de código ocurrió. Bienvenido al arte de investigar escenas del crimen digital."
        },
        
        "2_challenge": {
            "type": "parsons",
            "blocks": [
                {"id": "b1", "text": "Traceback (most recent call last):"},
                {"id": "b2", "text": "  File \"main.py\", line 4, in <module>"},
                {"id": "b3", "text": "    print(mensaje)"},
                {"id": "b4", "text": "NameError: name 'mensaje' is not defined"}
            ],
            "correct_order": ["b1", "b2", "b3", "b4"],
            "explanation": "Esta es la anatomía real de un error en Python. 1) Te dice que es un error (Traceback). 2) Te dice el archivo y la línea exacta (línea 4). 3) Te muestra el pedazo de código que explotó. 4) Te dice el tipo de error (NameError) y por qué (mensaje no está definido)."
        },
        
        "3_theory": {
            "type": "text",
            "content": "### El Arte del Debugging 🐞\nProgramar es 20% escribir código y 80% arreglar por qué no funciona. No te frustres, es el estado natural del software.\n\n### Los sospechosos habituales (Tipos de Errores)\n- **`SyntaxError`**: Escribiste mal la gramática de Python. Te faltaron dos puntos `:`, paréntesis `()`, o comillas `\"\"`.\n- **`IndentationError`**: Un error de espacios. Olvidaste indentar dentro de un `if` o bucle, o pusiste un espacio de más.\n- **`NameError`**: Intentas usar una variable o función que no existe (o tiene un error ortográfico).\n- **`TypeError`**: Intentas hacer una operación ilegal entre dos tipos de datos incompatibles (ej. sumar un número y una letra).\n- **`IndexError`**: Intentaste acceder a una posición en un string (o lista) que no existe.\n\n### La regla de oro 🛡️\nLee siempre la **última línea** del error. Ahí está el tipo de error y la explicación. Luego lee la línea que dice **\"line X\"** para saber dónde ir a corregirlo."
        },
        
        "4_guided_build": {
            "type": "code",
            "statement": "Este código lanza un `SyntaxError` porque le falta algo crítico al final de la línea del `if`. ¡Arréglalo!",
            "starter_code": "edad = 20\n\nif edad >= 18\n    print(\"Es mayor de edad\")\n",
            "solution": "edad = 20\n\nif edad >= 18:\n    print(\"Es mayor de edad\")\n"
        },
        
        "5_struggle": {
            "type": "code",
            "statement": "¡Desastre! Este programa tiene un `NameError` y un `TypeError`. Ejecuta el código para leer los errores, identifícalos y soluciónalos para que imprima 'Total a pagar: 150'.",
            "starter_code": "precio = \"100\"\nimpuesto = 50\n\ntotal = precia + impuesto\n\nprint(\"Total a pagar: \" + total)\n",
            "solution": "precio = \"100\"\nimpuesto = 50\n\ntotal = int(precio) + impuesto\n\nprint(f\"Total a pagar: {total}\")\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["Total a pagar: 150"]
            }
        },
        
        "6_feedback": {
            "type": "mapping",
            "errors": [
                {
                    "error_type": "NameError",
                    "free": "NameError: name 'precia' is not defined",
                    "pro": "Fíjate bien en cómo declaraste la variable arriba (`precio`) y cómo la estás usando abajo (`precia`). Python no perdona ni una sola letra."
                },
                {
                    "error_type": "TypeError",
                    "free": "TypeError: can only concatenate str (not \"int\") to str",
                    "pro": "En el print intentas concatenar con `+` un texto y un número entero. Para solucionar esto fácilmente, usa las f-strings: `f\"Total a pagar: {total}\"` o convierte el número a string con `str()`."
                }
            ]
        },
        
        "7_build": {
            "type": "code",
            "statement": "MINI PROYECTO: El Inspector de Código.\nTe entrego un código completamente destrozado. Tu misión es arreglarlo para que pregunte el año de nacimiento, calcule la edad y si es mayor a 18 imprima 'Aprobado'.\nEncuentra los errores de sintaxis, indentación y tipos lógicos.",
            "starter_code": "nacimiento = input(\"Año de nacimiento: \")\n\nedad = 2024 - nacimiento\n\nif edad >= 18:\nprint(\"Aprobado\")\n",
            "solution": "nacimiento = int(input(\"Año de nacimiento: \"))\n\nedad = 2024 - nacimiento\n\nif edad >= 18:\n    print(\"Aprobado\")\n",
            "validation": {
                "inputs": [["2000"]],
                "expected_outputs": ["Aprobado"]
            }
        },
        
        "8_retrieval": {
            "type": "code",
            "statement": "RETO SORPRESA: Identificación de errores.\nSi yo escribo `palabra = \"Gato\"` e inmediatamente debajo escribo `print(palabra[5])`, ¿qué tipo de error saltará? Imprime literalmente el nombre del error como respuesta (ej. 'SyntaxError').",
            "starter_code": "# Imprime el nombre del error esperado\nprint(____)\n",
            "solution": "print(\"IndexError\")\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["IndexError"]
            }
        },
        
        "9_summary": {
            "type": "text",
            "content": "## ¡Eres un Cazador de Bugs! 🔎\n\nEl miedo al texto rojo ha desaparecido. Ahora lo ves como lo que es: tu asistente personal indicándote dónde trabajar.\n\n### Resumen de tu Arsenal 🧠:\n1. **Traceback:** Tu mapa del tesoro. Sabes leer de abajo hacia arriba para encontrar la línea maldita.\n2. **Clasificación de Bugs:** Reconoces fácilmente errores de tipeo (`NameError`), errores de tipo (`TypeError`) y falta de formato (`SyntaxError` / `IndentationError`).\n\n### ¡HAS COMPLETADO EL MÓDULO 1! 🏆🎉\nEste es un hito gigante. Tienes las herramientas básicas que componen el 90% del software global. Ahora que dominas el flujo y los datos, el **Módulo 2** te adentrará en el mundo de las **Abstracciones y Estructuras Complejas**, aprendiendo a crear tus propios comandos con Funciones y guardar millones de datos con Listas y Diccionarios."
        }
    }
}
