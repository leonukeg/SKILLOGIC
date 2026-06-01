"""
SKILLOGIC — Katas Data Database
Stores the coding challenges (katas) with their difficulties, xp rewards, and test cases.
"""

KATAS_DB = [
    {
        "id": "kata_variables_1",
        "module_id": "module_1",
        "difficulty": "facil",
        "xp_reward": 1,
        "requires_kata": None,
        "title_es": "1. Declarando Variables",
        "title_en": "1. Declaring Variables",
        "description_es": "Declara una variable `x` con el valor `15` y una variable `y` con el valor `4`. Luego, calcula el resto (módulo) de dividir `x` entre `y` y guárdalo en una variable llamada `resto`.",
        "description_en": "Declare a variable `x` with value `15` and a variable `y` with value `4`. Then, calculate the remainder (modulo) of dividing `x` by `y` and store it in a variable called `resto`.",
        "initial_code": "# Declara las variables x, y, y resto aquí\n",
        "test_code": """
# -- hidden tests --
try:
    assert x == 15, "Error: x debe ser igual a 15"
    assert y == 4, "Error: y debe ser igual a 4"
    assert resto == 3, "Error: resto debe ser igual a 3 (15 % 4)"
    print("ALL_TESTS_PASSED")
except NameError as ne:
    print(f"Error: Asegúrate de definir las variables indicadas: {ne}")
"""
    },
    {
        "id": "kata_strings_1",
        "module_id": "module_1",
        "difficulty": "facil",
        "xp_reward": 1,
        "requires_kata": "kata_variables_1",
        "title_es": "2. Uniendo Textos",
        "title_en": "2. Joining Text",
        "description_es": "Tienes dos variables: `nombre = \"Guido\"` y `apellido = \"van Rossum\"`. Crea una nueva variable llamada `nombre_completo` que contenga ambos textos unidos y separados por un espacio.",
        "description_en": "You have two variables: `nombre = \"Guido\"` and `apellido = \"van Rossum\"`. Create a new variable called `nombre_completo` containing both texts joined and separated by a space.",
        "initial_code": "nombre = \"Guido\"\napellido = \"van Rossum\"\n# Crea la variable nombre_completo aquí\n",
        "test_code": """
# -- hidden tests --
try:
    assert nombre_completo == "Guido van Rossum", "Error: nombre_completo debe ser 'Guido van Rossum'"
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: Asegúrate de definir la variable 'nombre_completo'")
"""
    },
    {
        "id": "kata_swap_1",
        "module_id": "module_1",
        "difficulty": "facil",
        "xp_reward": 2,
        "requires_kata": "kata_strings_1",
        "title_es": "3. Intercambio de Colores",
        "title_en": "3. Colors Swap",
        "description_es": "Tienes dos variables: `color_a = \"rojo\"` y `color_b = \"azul\"`. Intercambia sus valores para que `color_a` contenga `\"azul\"` y `color_b` contenga `\"rojo\"`. ¡Hazlo sin escribir los textos directamente en tu código!",
        "description_en": "You have two variables: `color_a = \"rojo\"` and `color_b = \"azul\"`. Swap their values so that `color_a` contains `\"azul\"` and `color_b` contains `\"rojo\"`. Do it without writing the text strings directly!",
        "initial_code": "color_a = \"rojo\"\ncolor_b = \"azul\"\n# Intercambia los valores aquí sin escribir 'rojo' ni 'azul'\n",
        "test_code": """
# -- hidden tests --
try:
    assert "rojo" not in USER_CODE.replace('color_a = "rojo"', '').replace("color_a = 'rojo'", ''), "No debes escribir 'rojo' directamente en tu código para hacer el intercambio"
    assert "azul" not in USER_CODE.replace('color_b = "azul"', '').replace("color_b = 'azul'", ''), "No debes escribir 'azul' directamente en tu código para hacer el intercambio"
    assert color_a == "azul", "Error: color_a debe terminar siendo 'azul'"
    assert color_b == "rojo", "Error: color_b debe terminar siendo 'rojo'"
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: Las variables color_a o color_b no están definidas")
"""
    },
    {
        "id": "kata_cond_1",
        "module_id": "module_2",
        "difficulty": "medio",
        "xp_reward": 2,
        "requires_kata": "kata_swap_1",
        "title_es": "4. Control del Clima",
        "title_en": "4. Climate Control",
        "description_es": "Tienes una variable `temperatura = 28`. Crea una variable de texto llamada `mensaje`. Si la `temperatura` es mayor o igual a 30, el mensaje debe ser `\"Calor\"`. De lo contrario, debe ser `\"Templado\"`.",
        "description_en": "You have a variable `temperatura = 28`. Create a text variable called `mensaje`. If the `temperatura` is 30 or greater, the message must be `\"Calor\"`. Otherwise, it must be `\"Templado\"`.",
        "initial_code": "temperatura = 28\n# Define la variable mensaje usando condicionales aquí\n",
        "test_code": """
# -- hidden tests --
try:
    assert "if" in USER_CODE, "Error: Debes utilizar una estructura condicional 'if'"
    assert mensaje == "Templado", "Error: Con temperatura = 28, el mensaje debe ser 'Templado'"
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: Asegúrate de declarar la variable 'mensaje'")
"""
    },
    {
        "id": "kata_cond_2",
        "module_id": "module_2",
        "difficulty": "medio",
        "xp_reward": 3,
        "requires_kata": "kata_cond_1",
        "title_es": "5. Clasificación Académica",
        "title_en": "5. Grade Classification",
        "description_es": "Tienes una variable `calificacion = 85`. Crea una variable llamada `letra`. Si la calificación es 90 o más, `letra` es `\"A\"`. Si es 80 o más (pero menor a 90), es `\"B\"`. Si es 70 o más (pero menor a 80), es `\"C\"`. De lo contrario, es `\"F\"`.",
        "description_en": "You have a variable `calificacion = 85`. Create a variable called `letra`. If the score is 90 or more, `letra` is `\"A\"`. If it is 80 or more (but less than 90), it is `\"B\"`. If it is 70 or more (but less than 80), it is `\"C\"`. Otherwise, it is `\"F\"`.",
        "initial_code": "calificacion = 85\n# Define la variable letra usando if, elif, else aquí\n",
        "test_code": """
# -- hidden tests --
try:
    assert "if" in USER_CODE and "elif" in USER_CODE, "Error: Debes utilizar condicionales 'if' y 'elif'"
    assert letra == "B", "Error: Con calificación = 85, letra debe ser 'B'"
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: Asegúrate de declarar la variable 'letra'")
"""
    },
    {
        "id": "kata_loops_1",
        "module_id": "module_2",
        "difficulty": "dificil",
        "xp_reward": 3,
        "requires_kata": "kata_cond_2",
        "title_es": "6. Sumando Números",
        "title_en": "6. Summing Numbers",
        "description_es": "Tienes una lista `valores = [2, 4, 6, 8]`. Crea una variable `suma_total` inicializada en `0`. Utiliza un bucle `for` para recorrer `valores` y sumar todos sus elementos dentro de `suma_total`.",
        "description_en": "You have a list `valores = [2, 4, 6, 8]`. Create a variable `suma_total` initialized to `0`. Use a `for` loop to iterate through `valores` and sum all its elements in `suma_total`.",
        "initial_code": "valores = [2, 4, 6, 8]\nsuma_total = 0\n# Escribe el bucle for para sumar los elementos aquí\n",
        "test_code": """
# -- hidden tests --
try:
    assert "for" in USER_CODE, "Error: Debes utilizar un bucle 'for'"
    assert suma_total == 20, "Error: La suma total de [2, 4, 6, 8] debe ser 20"
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: Asegúrate de declarar la variable 'suma_total'")
"""
    },
    {
        "id": "kata_filter_1",
        "module_id": "module_2",
        "difficulty": "dificil",
        "xp_reward": 4,
        "requires_kata": "kata_loops_1",
        "title_es": "7. Filtrar por Edad",
        "title_en": "7. Filter by Age",
        "description_es": "Tienes una lista `edades = [12, 18, 25, 15, 30, 8]`. Crea una lista vacía llamada `adultos`. Utiliza un bucle `for` y una condición `if` para recorrer `edades` y añadir a `adultos` solo las edades que sean mayores o iguales a `18`.",
        "description_en": "You have a list `edades = [12, 18, 25, 15, 30, 8]`. Create an empty list called `adultos`. Use a `for` loop and an `if` condition to iterate through `edades` and add to `adultos` only those ages that are greater than or equal to `18`.",
        "initial_code": "edades = [12, 18, 25, 15, 30, 8]\nadultos = []\n# Recorre edades y añade los >= 18 a adultos aquí\n",
        "test_code": """
# -- hidden tests --
try:
    assert "for" in USER_CODE, "Error: Debes usar un bucle 'for'"
    assert "if" in USER_CODE, "Error: Debes usar una condición 'if'"
    assert adultos == [18, 25, 30], "Error: La lista de adultos debe ser [18, 25, 30]"
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: Asegúrate de declarar la variable 'adultos'")
"""
    },
    {
        "id": "kata_break_1",
        "module_id": "module_2",
        "difficulty": "dificil",
        "xp_reward": 4,
        "requires_kata": "kata_filter_1",
        "title_es": "8. Parada de Emergencia",
        "title_en": "8. Emergency Stop",
        "description_es": "Tienes una lista de palabras `palabras = [\"manzana\", \"platano\", \"STOP\", \"naranja\"]`. Crea una lista vacía llamada `resultado`. Utiliza un bucle `for` para recorrer `palabras` y añadir cada una a `resultado`. Si encuentras la palabra `\"STOP\"`, debes detener el bucle de inmediato usando `break` sin añadirla.",
        "description_en": "You have a list of words `palabras = [\"manzana\", \"platano\", \"STOP\", \"naranja\"]`. Create an empty list called `resultado`. Use a `for` loop to iterate through `palabras` and add each to `resultado`. If you find the word `\"STOP\"`, stop the loop immediately using `break` without adding it.",
        "initial_code": "palabras = [\"manzana\", \"platano\", \"STOP\", \"naranja\"]\nresultado = []\n# Recorre palabras y detén el bucle al encontrar 'STOP'\n",
        "test_code": """
# -- hidden tests --
try:
    assert "for" in USER_CODE, "Error: Debes usar un bucle 'for'"
    assert "break" in USER_CODE, "Error: Debes usar la palabra clave 'break'"
    assert resultado == ["manzana", "platano"], "Error: resultado debe contener ['manzana', 'platano']"
    print("ALL_TESTS_PASSED")
except NameError:
    print("Error: Asegúrate de declarar la variable 'resultado'")
"""
    }
]

def get_kata_by_id(kata_id: str) -> dict | None:
    for kata in KATAS_DB:
        if kata["id"] == kata_id:
            return kata
    return None
