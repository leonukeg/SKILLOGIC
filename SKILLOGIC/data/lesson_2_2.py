# Contenido de la Lección 2.2: Listas — Colecciones Ordenadas y Mutables
# Siguiendo la metodología SKILLOGIC

LESSON_2_2 = {
    "title": "Listas — Colecciones Ordenadas y Mutables",
    "level": "Intermedio",
    
    "steps": {
        "1_hook": {
            "type": "text",
            "content": "Si estás programando WhatsApp, ¿cómo guardas los nombres de los contactos de un usuario? Si tiene 5 contactos, ¿creas las variables 'c1', 'c2', 'c3', 'c4', 'c5'? ¿Y si agrega 500 contactos más? Necesitas un contenedor dinámico que pueda guardar millones de datos bajo un solo nombre. Eso es una Lista."
        },
        
        "2_challenge": {
            "type": "parsons",
            "blocks": [
                {"id": "b1", "text": "inventario = ['espada', 'escudo']"},
                {"id": "b2", "text": "inventario.append('poción')"},
                {"id": "b3", "text": "primer_item = inventario[0]"},
                {"id": "b4", "text": "inventario[1] = 'armadura'"},
                {"id": "b5", "text": "print(inventario)"}
            ],
            "correct_order": ["b1", "b2", "b3", "b4", "b5"],
            "explanation": "Creamos una lista con corchetes []. Le agregamos un elemento al final con .append(). Accedemos a posiciones igual que con los strings (índice 0). Y la magia de las listas: son mutables, por lo que podemos sobreescribir la posición [1] con un dato nuevo."
        },
        
        "3_theory": {
            "type": "text",
            "content": "### Las Listas: Trenes de carga 🚂\nEn Python, una lista se define usando corchetes `[]` separando sus elementos con comas `,`. Pueden guardar cualquier tipo de dato (incluso otras listas).\n`numeros = [10, 20, 30, 40]`\n\n### Acceder y Mutar (Cambiar)\nIgual que los strings, accedemos usando índices que empiezan en `0`.\n- `numeros[0]` devuelve `10`.\n- A diferencia de los strings, las listas sí pueden mutar: `numeros[0] = 99` cambia el 10 por un 99 al instante.\n\n### Los Superpoderes de la Lista ⚡\n- `.append(dato)`: Empuja un dato al final de la lista.\n- `.insert(indice, dato)`: Mete un dato en una posición exacta, empujando a los demás a la derecha.\n- `.pop()`: Arranca y te devuelve el último elemento de la lista (o el índice que le pases).\n- `len(lista)`: Te dice cuántos elementos viven dentro del contenedor.\n\n### Slicing en Listas 🔪\nFunciona exactamente igual que en los strings: `numeros[1:3]` devuelve un pedazo de la lista."
        },
        
        "4_guided_build": {
            "type": "code",
            "statement": "Usa el método correcto para agregar la palabra 'C++', como último elemento en la lista `lenguajes`.",
            "starter_code": "lenguajes = [\"Python\", \"JavaScript\", \"Java\"]\n# Agrega 'C++' al final\nlenguajes.____(\"C++\")\nprint(lenguajes)\n",
            "solution": "lenguajes = [\"Python\", \"JavaScript\", \"Java\"]\nlenguajes.append(\"C++\")\nprint(lenguajes)\n"
        },
        
        "5_struggle": {
            "type": "code",
            "statement": "Tienes una lista con errores: `compras = [\"leche\", \"piedras\", \"pan\"]`.\nTu misión:\n1. Reemplaza el elemento \"piedras\" (índice 1) por \"huevos\".\n2. Agrega al final de la lista la palabra \"manzanas\" usando el método adecuado.\n3. Imprime la lista completa resultante.",
            "starter_code": "compras = [\"leche\", \"piedras\", \"pan\"]\n# Escribe tus correcciones aquí\n\n",
            "solution": "compras = [\"leche\", \"piedras\", \"pan\"]\ncompras[1] = \"huevos\"\ncompras.append(\"manzanas\")\nprint(compras)\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["['leche', 'huevos', 'pan', 'manzanas']"]
            }
        },
        
        "6_feedback": {
            "type": "mapping",
            "errors": [
                {
                    "error_type": "IndexError",
                    "free": "IndexError: list assignment index out of range",
                    "pro": "Si intentas usar un índice como `compras[10] = 'queso'` y la lista solo tiene 3 elementos, Python entra en pánico. Para agregar elementos que no caben en los asientos actuales, usa `.append()`."
                },
                {
                    "error_type": "AttributeError",
                    "free": "AttributeError: 'list' object has no attribute 'add'",
                    "pro": "¡Cuidado! En algunos lenguajes se usa `.add()`, pero en Python el método para insertar al final de una lista es `.append()`."
                }
            ]
        },
        
        "7_build": {
            "type": "code",
            "statement": "MINI PROYECTO: Sistema de Colas (FIFO).\nEstás programando un servidor web básico usando una lista de peticiones.\n1. Crea una lista vacía llamada `cola`.\n2. Agrega en este orden (usando `.append()`): 'request_1', 'request_2', 'request_3'.\n3. Para procesar peticiones en orden, usamos `.pop(0)` (que saca siempre al que llegó primero). Ejecuta `.pop(0)` dos veces.\n4. Imprime cómo quedó la lista `cola` al final.",
            "starter_code": "# Proyecto Colas\n",
            "solution": "cola = []\ncola.append(\"request_1\")\ncola.append(\"request_2\")\ncola.append(\"request_3\")\ncola.pop(0)\ncola.pop(0)\nprint(cola)\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["['request_3']"]
            }
        },
        
        "8_retrieval": {
            "type": "code",
            "statement": "RETO SORPRESA: Extracción agresiva.\nTienes la lista `letras = ['a', 'b', 'c', 'd', 'e']`. ¿Cómo usas slicing para imprimir los últimos 2 elementos de la lista en una sola línea de código?",
            "starter_code": "letras = ['a', 'b', 'c', 'd', 'e']\nprint(____)\n",
            "solution": "letras = ['a', 'b', 'c', 'd', 'e']\nprint(letras[-2:])\n",
            "validation": {
                "inputs": [[]],
                "expected_outputs": ["['d', 'e']"]
            }
        },
        
        "9_summary": {
            "type": "text",
            "content": "## ¡Eres el Señor de los Datos! 🗃️\n\nHas dominado tu primera estructura de datos compleja.\n\n### Resumen de tu Arsenal 🧠:\n1. **Listas `[]`:** Contenedores masivos que guardan el orden de llegada.\n2. **Mutabilidad:** La capacidad de sobreescribir datos `lista[0] = \"nuevo\"` en tiempo real.\n3. **Crecimiento y Reducción:** Dominaste `.append()` para meter datos y `.pop()` para destruirlos.\n\n### Próximo Paso 🚀\nLas listas son increíbles porque guardan el orden. Pero... ¿Qué pasa si necesitas encontrar a un usuario específico entre 1 millón de registros? En una lista tendrías que revisar uno por uno (lento). En la siguiente lección conocerás la estructura de datos más rápida del universo computacional: Los **Diccionarios** (Mapas Hash)."
        }
    }
}
