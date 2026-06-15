# Contenido de la Lección 2.3: Diccionarios y Sets — Mapas y Unicidad
# Siguiendo la metodología SKILLOGIC

LESSON_2_3 = {
    "title": "Dicts y Sets — Mapas y Unicidad",
    "level": "Intermedio",
    
    "steps": {
        "1_hook": {
            "type": "text",
            "content": "Si tienes una Lista con 1 billón de usuarios de Netflix y buscas a 'Alex', la computadora tiene que leer usuario por usuario hasta encontrarlo. Tardaría segundos, lo cual es inaceptable. ¿Cómo logran los servidores encontrar datos instantáneamente? Usan la estructura de datos más poderosa que existe: El Mapa Hash (En Python, los Diccionarios)."
        },
        
        "2_challenge": {
            "type": "parsons",
            "blocks": [
                {"id": "b1", "text": "usuario = {'nombre': 'Alex', 'edad': 25}"},
                {"id": "b2", "text": "edad_usuario = usuario['edad']"},
                {"id": "b3", "text": "usuario['suscripcion'] = 'Premium'"},
                {"id": "b4", "text": "print(usuario)"}
            ],
            "correct_order": ["b1", "b2", "b3", "b4"],
            "explanation": "Creamos un Diccionario usando llaves {}. A diferencia de las Listas, no usamos índices numéricos, usamos 'Llaves' (claves en formato texto) para acceder a los 'Valores'. Y si le asignas un valor a una llave que no existe, ¡la crea automáticamente!"
        },
        
        "3_theory": {
            "type": "text",
            "content": "### Diccionarios: Llave y Valor 🔑\nLos diccionarios (`dict`) agrupan datos usando etiquetas en lugar de posiciones.\n`perfil = {\"username\": \"neo\", \"level\": 50}`\n\n### El Poder de la Velocidad O(1) ⚡\nLa magia de un diccionario es matemática. Cuando buscas `perfil[\"username\"]`, Python usa una fórmula matemática para saber EXACTAMENTE en qué microchip está guardado. No busca, simplemente va directamente. Es instantáneo.\n\n### Funciones clave de los Diccionarios\n- `.keys()`: Te da todas las llaves.\n- `.values()`: Te da todos los valores.\n- `.items()`: Te da pares de (llave, valor) perfectos para usar con un bucle `for`.\n\n### Sets (Conjuntos): La Unicidad Absoluta 🛡️\nLos Sets usan la misma sintaxis de llaves `{}` pero sin valores, solo elementos sueltos: `numeros = {1, 2, 3}`. \n**Superpoder del Set:** ¡NO permiten duplicados! Si intentas meter un `2` otra vez, simplemente lo ignora. Son perfectos para limpiar datos repetidos."
        },
        
        "4_guided_build": {
            "type": "code",
            "statement": "Extrae el valor del daño del arma y guárdalo en la variable. Luego agrégale un nuevo par llave-valor llamado `\"durabilidad\": 100` al diccionario.",
            "starter_code": "arma = {\"nombre\": \"Espada\", \"daño\": 45}\n# Extrae el daño usando su llave\npoder = arma[____]\n# Agrega la durabilidad\narma[____] = 100\nprint(arma)\n",
            "solution": "arma = {\"nombre\": \"Espada\", \"daño\": 45}\npoder = arma[\"daño\"]\narma[\"durabilidad\"] = 100\nprint(arma)\n"
        },
        
        "5_struggle": {
            "type": "code",
            "statement": "Tienes una lista enorme de emails de clientes que asistieron a eventos, pero hay muchos duplicados porque fueron a varios eventos.\n`correos = [\"a@mail.com\", \"b@mail.com\", \"a@mail.com\", \"c@mail.com\", \"b@mail.com\"]`\n\nTu misión en 2 líneas:\n1. Convierte la lista en un `set()` para destruir instantáneamente todos los duplicados.\n2. Convierte ese Set de vuelta a una `list()` y guárdalo en la variable `unicos`.\n3. Imprime `unicos`.",
            "starter_code": "correos = [\"a@mail.com\", \"b@mail.com\", \"a@mail.com\", \"c@mail.com\", \"b@mail.com\"]\n# Escribe tu magia de limpieza aquí\n",
            "solution": "correos = [\"a@mail.com\", \"b@mail.com\", \"a@mail.com\", \"c@mail.com\", \"b@mail.com\"]\nunicos = list(set(correos))\nprint(unicos)\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["['a@mail.com', 'b@mail.com', 'c@mail.com']"] # Nota: el orden puede variar en sets, el validador final debe contemplar esto.
            }
        },
        
        "6_feedback": {
            "type": "mapping",
            "errors": [
                {
                    "error_type": "KeyError",
                    "free": "KeyError: 'nivel'",
                    "pro": "¡Clásico error! Intentaste pedirle al diccionario el valor de la llave 'nivel', pero esa llave no existe adentro. Para evitar que el programa explote, los pros usan el método `.get('nivel')`, que devuelve None en lugar de dar error si no existe."
                },
                {
                    "error_type": "TypeError",
                    "free": "TypeError: unhashable type: 'list'",
                    "pro": "Intentaste meter una lista dentro de un Set (o usarla como llave de un diccionario). Recuerda la regla sagrada: las llaves de diccionario y los elementos de un Set DEBEN ser inmutables (como strings, números o tuplas), no pueden ser listas."
                }
            ]
        },
        
        "7_build": {
            "type": "code",
            "statement": "MINI PROYECTO: Inventario RPG.\nTienes un diccionario de inventario. Debes crear un bucle `for` que use el método `.items()` para recorrer cada elemento.\nPor cada elemento, imprime el formato: 'Tienes [cantidad] [item]'.",
            "starter_code": "inventario = {\"Pociones\": 5, \"Monedas\": 150, \"Mapas\": 1}\n# Usa un for para iterar el diccionario\n",
            "solution": "inventario = {\"Pociones\": 5, \"Monedas\": 150, \"Mapas\": 1}\nfor item, cantidad in inventario.items():\n    print(f\"Tienes {cantidad} {item}\")\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["Tienes 5 Pociones\nTienes 150 Monedas\nTienes 1 Mapas"]
            }
        },
        
        "8_retrieval": {
            "type": "code",
            "statement": "RETO SORPRESA: Matemáticas de Sets.\nSi yo creo un set así: `s = {1, 1, 1, 2, 2, 3}`. ¿Qué número devolverá si hago un `len(s)`? (Imprímelo).",
            "starter_code": "print(____)\n",
            "solution": "print(3)\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["3"]
            }
        },
        
        "9_summary": {
            "type": "text",
            "content": "## ¡Has dominado la base de datos nativa! 🗄️\n\nEl Diccionario y el Set son el pan de cada día de los programadores profesionales.\n\n### Resumen de tu Arsenal 🧠:\n1. **Diccionarios `{k: v}`:** Estructuras llave-valor ultrarrápidas, indispensables para manejar datos estilo JSON.\n2. **`.items()`:** Tu atajo favorito para recorrer ambas mitades del diccionario en un bucle `for`.\n3. **Sets `{}`:** El guardián de la unicidad. El truco sucio y rápido para eliminar duplicados masivos.\n\n### Próximo Paso 🚀\nYa sabes usar Datos y ya sabes crear Funciones. En la última lección de este módulo vamos a mezclar ambas y aprender sobre **Programación Funcional**, el estilo ninja que usan las librerías modernas para procesar datos complejos en una sola línea de código."
        }
    }
}
