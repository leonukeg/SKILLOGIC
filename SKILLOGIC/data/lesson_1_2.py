# Contenido de la Lección 1.2: Strings en Profundidad
# Siguiendo la metodología SKILLOGIC

LESSON_1_2 = {
    "title": "Strings en Profundidad",
    "level": "Principiante",
    
    "steps": {
        "1_hook": {
            "type": "text",
            "content": "¿Alguna vez te has preguntado cómo Instagram sabe extraer tu nombre de usuario a partir de tu correo electrónico (ej. 'alex@gmail.com' -> 'alex')? Para hacer esto, no basta con saber qué es un texto (String), necesitas aprender a rebanarlo, modificarlo y manipularlo a tu antojo."
        },
        
        "2_challenge": {
            "type": "parsons",
            "blocks": [
                {"id": "b1", "text": "correo = 'usuario_pro@gmail.com'"},
                {"id": "b2", "text": "partes = correo.split('@')"},
                {"id": "b3", "text": "nombre_usuario = partes[0]"},
                {"id": "b4", "text": "print(f'Tu usuario es: {nombre_usuario}')"}
            ],
            "correct_order": ["b1", "b2", "b3", "b4"],
            "explanation": "Primero necesitamos el texto original. Luego, usamos un 'método' llamado split que corta el texto usando el arroba '@' como tijera. Esto nos da dos partes. Finalmente, tomamos la primera parte (índice 0) que corresponde al usuario."
        },
        
        "3_theory": {
            "type": "text",
            "content": "### Strings: Más que simple texto 🧵\nEn Python, un string es una secuencia de caracteres ordenados. ¡Cada letra tiene su propio asiento numerado!\n\n### Índices: El mapa de asientos 🗺️\nEn programación, siempre **empezamos a contar desde cero (0)**.\nSi `palabra = \"PYTHON\"`:\n- `palabra[0]` es `'P'`\n- `palabra[1]` es `'Y'`\n- `palabra[-1]` es la magia para obtener la **última** letra: `'N'`.\n\n### Slicing: Rebanando texto 🔪\nPuedes extraer pedazos de texto usando la sintaxis `[inicio:fin]` (el fin no se incluye).\n- `palabra[0:2]` devuelve `'PY'` (posiciones 0 y 1).\n- `palabra[:4]` devuelve `'PYTH'` (desde el inicio hasta el 3).\n- `palabra[2:]` devuelve `'THON'` (desde el 2 hasta el final).\n\n### Métodos de String: Superpoderes integrados 🦸‍♂️\nLos strings vienen con herramientas propias. Las usamos poniendo un punto `.` después de la variable:\n- `.upper()`: Convierte todo a MAYÚSCULAS.\n- `.lower()`: Convierte todo a minúsculas.\n- `.replace(\"A\", \"B\")`: Cambia las 'A' por 'B'.\n- `.split(\" \")`: Corta el texto en pedazos cada vez que encuentra un espacio, creando una lista."
        },
        
        "4_guided_build": {
            "type": "code",
            "statement": "Extrae los primeros 3 caracteres del código secreto y conviértelos a mayúsculas usando slicing y el método `.upper()`.",
            "starter_code": "codigo = \"xR5-password_secreta\"\n# Extrae desde el inicio hasta el índice 3 (sin incluirlo)\nprefijo = codigo[____]\n# Convierte a mayúsculas\nprefijo_mayus = prefijo.____()\nprint(prefijo_mayus)\n",
            "solution": "codigo = \"xR5-password_secreta\"\nprefijo = codigo[:3]\nprefijo_mayus = prefijo.upper()\nprint(prefijo_mayus)\n"
        },
        
        "5_struggle": {
            "type": "code",
            "statement": "Tienes la variable `archivo = \"reporte_final.TXT\"`. Tu misión es:\n1. Reemplazar la palabra 'final' por 'aprobado'.\n2. Convertir TODA la extensión (y solo la extensión, o todo el texto, como prefieras, pero debe verse bien) a minúsculas para que quede: 'reporte_aprobado.txt'.\n3. Imprimir el resultado.",
            "starter_code": "archivo = \"reporte_final.TXT\"\n# Escribe tu código aquí\n",
            "solution": "archivo = \"reporte_final.TXT\"\narchivo_nuevo = archivo.replace(\"final\", \"aprobado\")\narchivo_nuevo = archivo_nuevo.lower()\nprint(archivo_nuevo)\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["reporte_aprobado.txt"]
            }
        },
        
        "6_feedback": {
            "type": "mapping",
            "errors": [
                {
                    "error_type": "IndexError",
                    "free": "IndexError: string index out of range",
                    "pro": "Estás intentando acceder a una posición (índice) que no existe en el texto. Recuerda que si el texto tiene 5 letras, el último índice es el 4 (porque empezamos a contar en 0)."
                },
                {
                    "error_type": "TypeError",
                    "free": "TypeError: 'str' object does not support item assignment",
                    "pro": "¡Ah! Intentaste hacer algo como `texto[0] = 'H'`. En Python, los strings son inmutables (no se pueden cambiar directamente letra por letra). Tienes que crear un nuevo string usando slicing o .replace()."
                },
                {
                    "error_type": "AttributeError",
                    "free": "AttributeError: 'str' object has no attribute 'xxx'",
                    "pro": "Escribiste mal el nombre del método (como .uper() en vez de .upper()). ¡Revisa la ortografía!"
                }
            ]
        },
        
        "7_build": {
            "type": "code",
            "statement": "MINI PROYECTO: Limpiador de Datos Básicos.\nEl usuario ingresará un nombre desordenado (ej. '  jUaN pErEz  ').\n1. Usa `input()` para pedir el nombre.\n2. Límpialo quitando los espacios de los bordes usando el método `.strip()`.\n3. Convierte el texto para que cada palabra empiece con mayúscula usando `.title()`.\n4. Imprime el resultado limpio.",
            "starter_code": "# Proyecto Limpiador de Datos\n",
            "solution": "nombre_crudo = input(\"Nombre: \")\nnombre_limpio = nombre_crudo.strip().title()\nprint(nombre_limpio)\n",
            "validation": {
                "inputs": [["   aNa gArCiA  "]],
                "expected_outputs": ["Ana Garcia"]
            }
        },
        
        "8_retrieval": {
            "type": "code",
            "statement": "RETO SORPRESA: Tienes la palabra `palabra = \"PYTHON\"`. ¿Cómo usas slicing con un 'step' negativo para imprimir la palabra al revés en una sola línea?",
            "starter_code": "palabra = \"PYTHON\"\nprint(____)\n",
            "solution": "palabra = \"PYTHON\"\nprint(palabra[::-1])\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["NOHTYP"]
            }
        },
        
        "9_summary": {
            "type": "text",
            "content": "## ¡Dominas los Strings! ✂️\n\nEl texto ya no es solo un bloque estático para ti.\n\n### Resumen de tu Arsenal 🧠:\n1. **Índices:** Aprendiste a apuntar como un francotirador a una letra específica (`texto[0]`).\n2. **Slicing:** Eres capaz de extraer cualquier rebanada del texto usando `[inicio:fin]`.\n3. **Métodos Nativos:** Descubriste herramientas poderosas como `.upper()`, `.lower()`, `.replace()` y `.split()` que te ahorran horas de trabajo.\n\n### Próximo Paso 🚀\nHasta ahora tus programas hacen una sola cosa de arriba a abajo. Pero la verdadera inteligencia de un sistema viene de tomar decisiones. En la siguiente lección entraremos al mundo de los **Condicionales** (`if`, `else`), donde tu código empezará a pensar por sí mismo."
        }
    }
}
