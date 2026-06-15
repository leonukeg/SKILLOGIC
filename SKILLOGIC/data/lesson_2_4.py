# Contenido de la Lección 2.4: Funciones Avanzadas — Lambdas, Map, Filter, Sorted
# Siguiendo la metodología SKILLOGIC

LESSON_2_4 = {
    "title": "Funciones Avanzadas — Lambdas, Map, Filter, Sorted",
    "level": "Intermedio",
    
    "steps": {
        "1_hook": {
            "type": "text",
            "content": "Imagínate tener que escribir 5 líneas de código y crear una función completa solo para multiplicar un número por 2. Es como comprar una caja de herramientas gigante cuando solo necesitas apretar un tornillo. Para esos trabajos relámpago, Python tiene las Funciones Lambda: código ninja de una sola línea."
        },
        
        "2_challenge": {
            "type": "parsons",
            "blocks": [
                {"id": "b1", "text": "numeros = [1, 2, 3, 4]"},
                {"id": "b2", "text": "dobles = list(map(lambda x: x * 2, numeros))"},
                {"id": "b3", "text": "print(dobles)"}
            ],
            "correct_order": ["b1", "b2", "b3"],
            "explanation": "Aquí ocurren dos magias a la vez. 'map' agarra una lista de números y le aplica una función a CADA UNO. Pero en lugar de llamar a una función normal, le pasamos una función anónima y desechable ('lambda x: x*2') que se crea y destruye en la misma línea."
        },
        
        "3_theory": {
            "type": "text",
            "content": "### Lambdas: Las funciones anónimas 🥷\nUna lambda es una función comprimida sin nombre. Se usa para operaciones muy simples y matemáticas rápidas.\n`doble = lambda x: x * 2`\n(Recibe `x`, y retorna automáticamente `x * 2`).\n\n### Programación Funcional: Tratar al código como Data\nEn Python, las funciones son \"ciudadanos de primera clase\". ¡Puedes enviar una función como parámetro a otra función!\n\n### El Trío Dinámico del Procesamiento de Datos 🛠️\n1. **`map(función, lista)`**: Agarra CADA elemento de la lista y lo pasa por la función, creando una lista nueva.\n2. **`filter(función, lista)`**: Evalúa CADA elemento. Si la función devuelve `True`, lo mantiene; si es `False`, lo elimina.\n3. **`sorted(lista, key=función)`**: Ordena una lista, usando la función para saber qué criterio de orden usar.\n\n*Nota crítica: En Python 3, `map` y `filter` devuelven \"objetos iteradores\" (optimizados para no gastar memoria). Si quieres verlos enteros, debes envolverlos en `list(map(...))`.*"
        },
        
        "4_guided_build": {
            "type": "code",
            "statement": "Tienes una lista de nombres. Usa la función `sorted()` combinada con una lambda para ordenar esta lista NO por orden alfabético, sino por LA CANTIDAD DE LETRAS de cada palabra (su `len(x)`).",
            "starter_code": "nombres = [\"Ana\", \"Maximiliano\", \"Jose\", \"Lu\"]\n# Usa sorted con key=lambda\nordenados = sorted(nombres, ____=lambda x: ____(x))\nprint(ordenados)\n",
            "solution": "nombres = [\"Ana\", \"Maximiliano\", \"Jose\", \"Lu\"]\nordenados = sorted(nombres, key=lambda x: len(x))\nprint(ordenados)\n"
        },
        
        "5_struggle": {
            "type": "code",
            "statement": "Tienes una lista de pagos: `pagos = [15, 200, 8, 45, 120]`.\nTu misión en una sola línea (usando `filter` y `lambda`):\nExtrae SÓLO los pagos mayores o iguales a 50 y guárdalos en la variable `pagos_altos`.\n*¡Recuerda envolver todo en `list()`!*",
            "starter_code": "pagos = [15, 200, 8, 45, 120]\n# Haz el filter aquí\npagos_altos = \nprint(pagos_altos)\n",
            "solution": "pagos = [15, 200, 8, 45, 120]\npagos_altos = list(filter(lambda x: x >= 50, pagos))\nprint(pagos_altos)\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["[200, 120]"]
            }
        },
        
        "6_feedback": {
            "type": "mapping",
            "errors": [
                {
                    "error_type": "NoneType",
                    "free": "<map object at",
                    "pro": "¡Te olvidaste de la envoltura! Si imprimes un map o filter directamente, Python te dice la dirección de memoria donde está. Tienes que forzarlo a ser una lista haciendo `list(map(...))`."
                },
                {
                    "error_type": "SyntaxError",
                    "free": "SyntaxError: invalid syntax",
                    "pro": "Las lambdas son delicadas con la sintaxis. Recuerda: es la palabra `lambda`, luego la variable, luego dos puntos `:`, y por último la operación a retornar. NO escribas la palabra `return`."
                }
            ]
        },
        
        "7_build": {
            "type": "code",
            "statement": "MINI PROYECTO: Pipeline de Datos.\nImagina que eres un Data Scientist.\nTienes edades sucias en formato string: `data = [\"18\", \"25\", \"15\", \"30\"]`.\n1. En una línea, usa `map` para convertirlas todas en enteros (puedes pasarle la función `int` directamente, sin lambda).\n2. En otra línea, usa `filter` y lambda para quedarte SOLO con los mayores o iguales a 18.\n3. Imprime la lista final de adultos.",
            "starter_code": "data = [\"18\", \"25\", \"15\", \"30\"]\n# 1. Map a int\n# 2. Filter adultos\n",
            "solution": "data = [\"18\", \"25\", \"15\", \"30\"]\nenteros = list(map(int, data))\nadultos = list(filter(lambda x: x >= 18, enteros))\nprint(adultos)\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["[18, 25, 30]"]
            }
        },
        
        "8_retrieval": {
            "type": "code",
            "statement": "RETO SORPRESA: Si aplicas esta lambda: `lambda x: x[0] == \"A\"` como filtro para la lista `[\"Alex\", \"Bob\", \"Ana\"]`, ¿cuál es el resultado al convertirlo a lista?",
            "starter_code": "print(____)\n",
            "solution": "print(\"['Alex', 'Ana']\")\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["['Alex', 'Ana']"]
            }
        },
        
        "9_summary": {
            "type": "text",
            "content": "## ¡Escribes Código como un Senior! 🧠\n\nEl paso de usar bucles for pesados a usar programación funcional es el salto evolutivo más grande que da un programador.\n\n### Resumen de tu Arsenal 🧠:\n1. **Lambdas:** Las funciones desechables y veloces para trabajos matemáticos de una línea.\n2. **`map()` y `filter()`:** Los motores pesados para procesar listas masivas de datos sin necesidad de escribir múltiples líneas de bucles `for`.\n3. **Funciones como Datos:** Entendiste el concepto profundo de que en Python, las funciones pueden viajar libremente de un lado a otro como si fueran números o textos.\n\n### ¡HAS COMPLETADO EL MÓDULO 2! 🏆🚀\nOficialmente has conquistado la barrera del 50% de todo el currículum de SKILLOGIC. Tienes los fundamentos sólidos y la capacidad de abstraer ideas complejas.\n\nDirígete ahora mismo al Dojo de Katas y pon a prueba todo esto enfrentándote a los Desafíos de **Nivel Medio / Complicado**. Tu XP se disparará."
        }
    }
}
