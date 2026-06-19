"""
SKILLOGIC — Katas Data Database
Stores the coding challenges (katas) with their difficulties, xp rewards, and test cases.
"""

from SKILLOGIC.data.katas_1_1 import KATAS_1_1
from SKILLOGIC.data.katas_1_2 import KATAS_1_2
from SKILLOGIC.data.katas_1_3 import KATAS_1_3
from SKILLOGIC.data.katas_1_4 import KATAS_1_4
from SKILLOGIC.data.katas_1_5 import KATAS_1_5
from SKILLOGIC.data.katas_2_1 import KATAS_2_1
from SKILLOGIC.data.katas_2_2 import KATAS_2_2
from SKILLOGIC.data.katas_2_3 import KATAS_2_3
from SKILLOGIC.data.katas_2_4 import KATAS_2_4

OLD_KATAS = [
    # ------------------- "FÁCIL" (En realidad Difícil) -------------------
    {
        "id": "kata_facil_1",
        "module_id": "module_1",
        "difficulty": "facil",
        "xp_reward": 2,
        "requires_kata": None,
        "title_es": "1. El Truco Matemático",
        "title_en": "1. The Math Trick",
        "description_es": "Declara una variable `secreto`. Usa operaciones matemáticas para que `secreto` contenga la suma de todos los números del 1 al 100 inclusive. **Restricción:** ¡No puedes usar bucles `for` ni `while`, ni la función `sum()`!",
        "description_en": "Declare a variable `secreto`. Use mathematical operations so that `secreto` contains the sum of all numbers from 1 to 100 inclusive. **Constraint:** You cannot use `for` or `while` loops, nor the `sum()` function!",
        "initial_code": "# Calcula la suma del 1 al 100 matemáticamente sin usar bucles\nsecreto = 0\n",
        "test_code": """
# -- hidden tests --
try:
    assert "for " not in USER_CODE, "No se permiten bucles for"
    assert "while " not in USER_CODE, "No se permiten bucles while"
    assert "sum(" not in USER_CODE, "No se permite usar sum()"
    assert secreto == 5050, "Error: secreto debe ser 5050. Pista: Investiga la fórmula de la suma de Gauss."
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: Asegúrate de definir la variable 'secreto'.")
"""
    },
    {
        "id": "kata_facil_2",
        "module_id": "module_1",
        "difficulty": "facil",
        "xp_reward": 2,
        "requires_kata": "kata_facil_1",
        "title_es": "2. Cifrado Espejo",
        "title_en": "2. Mirror Cipher",
        "description_es": "Tienes un mensaje secreto: `mensaje = \"zereP nauJ\"`. Usando **exclusivamente slicing avanzado de strings** (`[::]`), crea una variable `descifrado` que invierta el texto y omita la primera y la última letra del resultado original. \n\nEjemplo: Si fuera 'oiraM', invertido es 'Mario', omitiendo bordes queda 'ari'.",
        "description_en": "You have a secret message: `mensaje = \"zereP nauJ\"`. Using **exclusively advanced string slicing** (`[::]`), create a variable `descifrado` that reverses the text and omits the first and last letter of the resulting string.",
        "initial_code": "mensaje = \"zereP nauJ\"\n# Escribe tu código aquí usando [::] en una sola línea\ndescifrado = \"\"\n",
        "test_code": """
# -- hidden tests --
try:
    assert "for" not in USER_CODE, "No puedes usar bucles."
    assert descifrado == "uan Pere", f"Error: Esperado 'uan Pere', pero tu variable es '{descifrado}'"
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: La variable 'descifrado' no está definida.")
"""
    },
    {
        "id": "kata_facil_3",
        "module_id": "module_1",
        "difficulty": "facil",
        "xp_reward": 3,
        "requires_kata": "kata_facil_2",
        "title_es": "3. Intercambio Cuántico",
        "title_en": "3. Quantum Swap",
        "description_es": "Tienes tres variables: `a = 10`, `b = 20`, `c = 30`. Debes rotar sus valores de forma que `a` tenga el valor de `c`, `b` tenga el de `a`, y `c` tenga el de `b`.\n\n**Restricción Estricta:** Debes hacerlo en **una sola línea de código** utilizando empaquetado/desempaquetado de tuplas. No puedes escribir los números directamente.",
        "description_en": "You have three variables: `a = 10`, `b = 20`, `c = 30`. You must rotate their values so that `a` has the value of `c`, `b` has the value of `a`, and `c` has the value of `b`.\n\n**Strict Constraint:** You must do this in **a single line of code** using tuple packing/unpacking. You cannot write the numbers directly.",
        "initial_code": "a = 10\nb = 20\nc = 30\n# Rota los valores en UNA SOLA LÍNEA aquí:\n",
        "test_code": """
# -- hidden tests --
try:
    lines = [line.strip() for line in USER_CODE.split('\\n') if line.strip() and not line.strip().startswith('#')]
    assert len(lines) <= 4, "Debe ser hecho en una sola línea después de la declaración inicial."
    assert "10" not in USER_CODE.split("30")[1] and "20" not in USER_CODE.split("30")[1], "No escribas los números."
    assert a == 30, "Error: 'a' debe valer 30"
    assert b == 10, "Error: 'b' debe valer 10"
    assert c == 20, "Error: 'c' debe valer 20"
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: Las variables a, b o c no existen.")
"""
    },

    # ------------------- "MEDIO" (En realidad Complicado) -------------------
    {
        "id": "kata_medio_1",
        "module_id": "module_2",
        "difficulty": "medio",
        "xp_reward": 4,
        "requires_kata": "kata_facil_3",
        "title_es": "4. El Año Bisiesto Absoluto",
        "title_en": "4. The Absolute Leap Year",
        "description_es": "Crea una función llamada `es_bisiesto(year)` que retorne `True` si es bisiesto y `False` si no lo es.\n\nReglas matemáticas: Es bisiesto si es divisible por 4. PERO si es divisible por 100, NO lo es, A MENOS que también sea divisible por 400.\n**Restricción diabólica:** Toda la lógica matemática dentro de la función debe retornar el resultado en una sola expresión booleana. Cero sentencias `if/else`.",
        "description_en": "Create a function called `es_bisiesto(year)` that returns `True` if leap year and `False` if not.\n\nMath rules: Leap if divisible by 4. BUT if divisible by 100, it is NOT, UNLESS it is also divisible by 400.\n**Diabolical Constraint:** The entire logic inside the function must return the result in a single boolean expression. Zero `if/else` statements.",
        "initial_code": "def es_bisiesto(year):\n    # Reemplaza el pass con tu expresión de una línea\n    pass\n",
        "test_code": """
# -- hidden tests --
try:
    import inspect
    func_source = inspect.getsource(es_bisiesto)
    assert "if" not in func_source, "No puedes usar la palabra reservada 'if'. Usa solo operadores lógicos (and, or, ==, %)."
    assert es_bisiesto(2024) is True, "2024 es bisiesto"
    assert es_bisiesto(1900) is False, "1900 NO es bisiesto"
    assert es_bisiesto(2000) is True, "2000 es bisiesto"
    assert es_bisiesto(2023) is False, "2023 NO es bisiesto"
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: Debes definir la función es_bisiesto")
except AssertionError as e:
    print(e)
"""
    },
    {
        "id": "kata_medio_2",
        "module_id": "module_2",
        "difficulty": "medio",
        "xp_reward": 5,
        "requires_kata": "kata_medio_1",
        "title_es": "5. Compresión Rúnica",
        "title_en": "5. Runic Compression",
        "description_es": "Escribe una función `comprimir(texto)` que reciba una cadena (ej. `\"AAAABBBCCDAA\"`) y la comprima contando los caracteres consecutivos (`\"A4B3C2D1A2\"`). Si la cadena resultante es del mismo tamaño o mayor que la original, debe devolver la original.\n\nNo uses librerías externas. Solo bucles y lógica pura.",
        "description_en": "Write a function `comprimir(texto)` that receives a string (e.g. `\"AAAABBBCCDAA\"`) and compresses it by counting consecutive characters (`\"A4B3C2D1A2\"`). If the resulting string is the same size or larger than the original, it must return the original.",
        "initial_code": "def comprimir(texto):\n    # Escribe aquí tu algoritmo de compresión\n    return texto\n",
        "test_code": """
# -- hidden tests --
try:
    assert comprimir("AAAABBBCCDAA") == "A4B3C2D1A2", f"Fallo prueba 1: {comprimir('AAAABBBCCDAA')}"
    assert comprimir("A") == "A", f"Fallo prueba 2: {comprimir('A')}"
    assert comprimir("AABB") == "AABB", f"Fallo prueba 3: {comprimir('AABB')} (El original es igual o menor longitud que A2B2)"
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: Función comprimir no encontrada")
except AssertionError as e:
    print(e)
"""
    },
    {
        "id": "kata_medio_3",
        "module_id": "module_2",
        "difficulty": "medio",
        "xp_reward": 5,
        "requires_kata": "kata_medio_2",
        "title_es": "6. Anagramas Estrictos",
        "title_en": "6. Strict Anagrams",
        "description_es": "Crea una función `es_anagrama(p1, p2)` que devuelva `True` si `p1` y `p2` son anagramas (mismas letras, distinto orden) ignorando espacios y diferencias entre mayúsculas y minúsculas. \n\n**Restricción:** Está estrictamente prohibido usar las funciones `sorted()`, `.sort()` o librerías como `collections`. Usa diccionarios o listas para contar.",
        "description_en": "Create a function `es_anagrama(p1, p2)` returning `True` if they are anagrams ignoring spaces and cases.\n\n**Constraint:** You are strictly forbidden to use `sorted()`, `.sort()`, or `collections`. Use dicts or lists to count.",
        "initial_code": "def es_anagrama(p1, p2):\n    # Escribe tu lógica sin usar sort()\n    pass\n",
        "test_code": """
# -- hidden tests --
try:
    assert "sort" not in USER_CODE, "No uses sort ni sorted"
    assert "Counter" not in USER_CODE, "No uses Counter"
    assert es_anagrama("Listen", "Silent") is True, "Listen y Silent son anagramas"
    assert es_anagrama("Rata", "Toro") is False, "Rata y Toro no lo son"
    assert es_anagrama("Tom Marvolo Riddle", "I am Lord Voldemort") is True, "Voldemort es anagrama de Tom Riddle"
    print("ALL_TESTS_PASSED")
except Exception as e:
    print(f"Error: {e}")
"""
    },
    {
        "id": "kata_medio_4",
        "module_id": "module_2",
        "difficulty": "medio",
        "xp_reward": 6,
        "requires_kata": "kata_medio_3",
        "title_es": "7. Aplanador de Dimensiones",
        "title_en": "7. Dimension Flattener",
        "description_es": "Tienes una lista con anidamiento infinito impredecible: `[1, [2, [3, 4], 5], 6]`. Crea una función recursiva `aplanar(lista)` que devuelva una lista de 1 dimensión: `[1, 2, 3, 4, 5, 6]`.\n\nPista: Usa `isinstance(item, list)` o `type(item) == list` para saber si un elemento es una lista.",
        "description_en": "You have a list with unpredictable infinite nesting. Create a recursive function `aplanar(lista)` that returns a 1D list.\n\nHint: Use `isinstance(item, list)` or `type(item) == list` to check for nested lists.",
        "initial_code": "def aplanar(lista):\n    resultado = []\n    # Implementa la lógica aquí\n    return resultado\n",
        "test_code": """
# -- hidden tests --
try:
    assert aplanar([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6], "Fallo prueba de aplanado estándar"
    assert aplanar([[[[9]]]]) == [9], "Fallo prueba de anidación profunda extrema"
    assert aplanar([]) == [], "Fallo prueba de lista vacía"
    print("ALL_TESTS_PASSED")
except Exception as e:
    print(f"Error: {e}")
"""
    },

    # ------------------- "DIFÍCIL" (En realidad Imposible / Entrevista FAANG) -------------------
    {
        "id": "kata_dificil_1",
        "module_id": "module_3",
        "difficulty": "dificil",
        "xp_reward": 8,
        "requires_kata": "kata_medio_4",
        "title_es": "8. Paréntesis Caóticos",
        "title_en": "8. Chaotic Parentheses",
        "description_es": "Crea una función `es_valido(texto)` que verifique si una cadena de corchetes `()`, `[]`, `{}` está perfectamente balanceada.\n\nEjemplo válido: `\"{[()]}\"`. Ejemplo inválido: `\"[(])\"`.\nSi eres un verdadero programador, resolverás esto usando una estructura de datos de tipo **Pila** (Stack).",
        "description_en": "Create a function `es_valido(texto)` verifying if a string of brackets `()`, `[]`, `{}` is balanced.\n\nValid: `\"{[()]}\"`. Invalid: `\"[(])\"`.\nUse a Stack data structure.",
        "initial_code": "def es_valido(texto):\n    pila = []\n    # Escribe la validación\n    return True\n",
        "test_code": """
# -- hidden tests --
try:
    assert es_valido("{[()]}") is True, "Prueba '{[()]}' falló"
    assert es_valido("[(])") is False, "Prueba '[(])' falló, se cruzaron"
    assert es_valido("(((((((((())))))))))") is True, "Prueba profundidad máxima falló"
    assert es_valido("}") is False, "Prueba '}' falló (empezar cerrando)"
    print("ALL_TESTS_PASSED")
except Exception as e:
    print(f"Error: {e}")
"""
    },
    {
        "id": "kata_dificil_2",
        "module_id": "module_3",
        "difficulty": "dificil",
        "xp_reward": 10,
        "requires_kata": "kata_dificil_1",
        "title_es": "9. Algoritmo de Kadane",
        "title_en": "9. Kadane's Algorithm",
        "description_es": "Dada una lista de enteros (positivos y negativos), escribe la función `max_suma(arreglo)` que encuentre la suma máxima de cualquier subarreglo contiguo.\n\nEj: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` devuelve `6` (por el subarreglo `[4, -1, 2, 1]`).\nOjo, si todos los números son negativos, debe devolver el negativo más alto.",
        "description_en": "Given an array of integers, write `max_suma(arreglo)` to find the maximum sum of any contiguous subarray.\n(Known as Kadane's Algorithm).",
        "initial_code": "def max_suma(arreglo):\n    # Tu lógica aquí (O(n) idealmente)\n    pass\n",
        "test_code": """
# -- hidden tests --
try:
    assert max_suma([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "Fallo Kadane clásico"
    assert max_suma([-5, -2, -9]) == -2, "Fallo caso donde todos son negativos"
    assert max_suma([100]) == 100, "Fallo con 1 solo elemento"
    print("ALL_TESTS_PASSED")
except Exception as e:
    print(f"Error: {e}")
"""
    },
    {
        "id": "kata_dificil_3",
        "module_id": "module_3",
        "difficulty": "dificil",
        "xp_reward": 15,
        "requires_kata": "kata_dificil_2",
        "title_es": "10. Atrapando la Lluvia",
        "title_en": "10. Trapping Rain Water",
        "description_es": "¡El problema final! Te dan una lista de alturas de edificios contiguos de ancho 1. Crea la función `atrapada(alturas)` que calcule cuántas unidades de agua de lluvia pueden quedar atrapadas entre ellos después de llover.\n\nEjemplo: `[0,1,0,2,1,0,1,3,2,1,2,1]` atrapa exactamente `6` unidades de agua. ¡Piénsalo bien, este problema ha reprobado a miles en FAANG!",
        "description_en": "The final boss! You are given an array of building heights. Create `atrapada(alturas)` to calculate how many units of rain water are trapped after raining.\n\nExample: `[0,1,0,2,1,0,1,3,2,1,2,1]` traps exactly `6` units.",
        "initial_code": "def atrapada(alturas):\n    # El Boss Final de SKILLOGIC\n    pass\n",
        "test_code": """
# -- hidden tests --
try:
    assert atrapada([0,1,0,2,1,0,1,3,2,1,2,1]) == 6, "Fallo caso base de agua"
    assert atrapada([4,2,0,3,2,5]) == 9, "Fallo valle profundo"
    assert atrapada([1,2,3,4,5]) == 0, "Fallo escalera sin huecos"
    print("ALL_TESTS_PASSED")
except Exception as e:
    print(f"Error: {e}")
"""
    }
]

KATAS_DB = KATAS_1_1 + KATAS_1_2 + KATAS_1_3 + KATAS_1_4 + KATAS_1_5 + KATAS_2_1 + KATAS_2_2 + KATAS_2_3 + KATAS_2_4 + OLD_KATAS

# Post-process to make Katas independent (Dojo Revolution)
CATEGORY_MAP = {
    "lesson_1_1": ("Fundamentos y Variables", "Basics & Variables"),
    "lesson_1_2": ("Strings y Textos", "Strings & Text"),
    "lesson_1_3": ("Listas y Arrays", "Lists & Arrays"),
    "lesson_1_4": ("Diccionarios", "Dictionaries"),
    "lesson_1_5": ("Debugging y Errores", "Debugging & Errors"),
    "lesson_2_1": ("Condicionales (If/Else)", "Conditionals (If/Else)"),
    "lesson_2_2": ("Bucles (For/While)", "Loops (For/While)"),
    "lesson_2_3": ("Funciones", "Functions"),
    "lesson_2_4": ("Programación Funcional", "Functional Programming"),
}

import datetime

def get_daily_kata() -> dict:
    # Use deterministic hash of today's date to pick a kata
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    idx = hash(today_str) % len(KATAS_DB)
    return KATAS_DB[idx]

for kata in KATAS_DB:
    # Unlock all katas
    kata["requires_kata"] = None
    
    # Assign category
    lid = kata.get("lesson_id", "")
    cats = CATEGORY_MAP.get(lid, ("Algoritmos Avanzados (FAANG)", "Advanced Algorithms (FAANG)"))
    kata["category_es"] = cats[0]
    kata["category_en"] = cats[1]

def get_kata_by_id(kata_id: str) -> dict | None:
    for kata in KATAS_DB:
        if kata["id"] == kata_id:
            return kata
    return None
