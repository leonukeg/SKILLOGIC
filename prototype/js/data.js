/* ================================================================
   SKILLOGIC — Data Layer
   All lesson content, exercises, and test cases.
   Pure data: no UI logic, no side effects.
   ================================================================ */

'use strict';

const SKILLOGIC_DATA = {

  modules: [
    { id: 1, icon: '>_', emoji: '⌨️', title: 'Fundamentos Reales',        lessonsCount: 4, progress: 100, status: 'completed' },
    { id: 2, icon: '⚙️', emoji: '🔧', title: 'Estructuras de Datos',       lessonsCount: 4, progress: 75,  status: 'active' },
    { id: 3, icon: 'fx', emoji: '📐', title: 'Funciones y Módulos',         lessonsCount: 4, progress: 40,  status: 'active' },
    { id: 4, icon: '□',  emoji: '🧩', title: 'POO',                         lessonsCount: 4, progress: 20,  status: 'upcoming' },
    { id: 5, icon: '🚀', emoji: '🚀', title: 'Proyectos',                   lessonsCount: 5, progress: 3,   status: 'upcoming' },
  ],

  lessons: [
    /* ---- LESSON 1 ---- */
    {
      id:        1,
      slug:      'como-piensa-computadora',
      module:    1,
      moduleTitle: 'Fundamentos Reales',
      title:     'Cómo piensa una computadora',
      hook:      '¿Cómo le explicarías a alguien que nunca ha visto una computadora cómo hacer una tostada?',
      concept:   'Instrucciones secuenciales · Variables · Estado del programa',
      completed: true,
      description: `Las computadoras ejecutan instrucciones <strong>una por una</strong>, en orden estricto. No piensan. No improvisan. Siguen exactamente lo que tú escribes.\n\nUna <strong>variable</strong> es como una caja etiquetada en la memoria del programa. Guardas un valor en ella y puedes consultarlo o modificarlo cuando quieras.\n\nEl <strong>estado</strong> del programa es el conjunto de todos los valores almacenados en un momento dado.`,
      codeExample: `nombre = "Ana"    <span class="comment"># caja "nombre" ← "Ana"</span>
edad   = 25        <span class="comment"># caja "edad"   ← 25</span>
<span class="fn">print</span>(nombre)    <span class="comment"># abre la caja y muestra su contenido</span>`,
      exercises: [
        {
          id:          'l1-e1',
          level:       'basic',
          levelLabel:  'Básico',
          xp:          10,
          title:       'Tu primera variable',
          description: 'Crea una variable llamada <code>saludo</code> que contenga el texto <code>"¡Hola, mundo!"</code> y luego imprímela con <code>print()</code>.',
          starterCode: `# Crea tu variable aquí
saludo = "___"

# Imprímela
print(saludo)`,
          solution:    `saludo = "¡Hola, mundo!"\nprint(saludo)`,
          hints:       ['Recuerda que los textos (strings) van entre comillas dobles o simples.'],
          tests: [
            { description: 'La salida contiene "Hola, mundo"', check: (out) => out.includes('Hola') && out.includes('mundo') },
          ],
        },
        {
          id:          'l1-e2',
          level:       'intermediate',
          levelLabel:  'Intermedio',
          xp:          25,
          title:       'Intercambio de valores',
          description: 'Tienes <code>a = 5</code> y <code>b = 10</code>. Intercambia sus valores sin usar números directamente. Al final imprime <code>a</code> y luego <code>b</code> en líneas separadas.',
          starterCode: `a = 5
b = 10

# Intercambia los valores usando Python idiomático
# (una sola línea es suficiente)


print(a)
print(b)`,
          solution:    `a = 5\nb = 10\na, b = b, a\nprint(a)\nprint(b)`,
          hints:       ['Python permite asignación múltiple: a, b = b, a'],
          tests: [
            { description: 'a es 10', check: (out) => { const lines = out.trim().split('\n'); return lines[0]?.trim() === '10'; } },
            { description: 'b es 5',  check: (out) => { const lines = out.trim().split('\n'); return lines[1]?.trim() === '5'; } },
          ],
        },
        {
          id:          'l1-e3',
          level:       'advanced',
          levelLabel:  'Avanzado',
          xp:          50,
          title:       'Calculadora de temperatura',
          description: 'Escribe una función <code>celsius_a_fahrenheit(celsius)</code> que convierta temperatura. Fórmula: <code>F = (C × 9/5) + 32</code>. Luego imprime el resultado para 0, 100 y -40.',
          starterCode: `def celsius_a_fahrenheit(celsius):
    # Implementa la conversión aquí
    pass

print(celsius_a_fahrenheit(0))
print(celsius_a_fahrenheit(100))
print(celsius_a_fahrenheit(-40))`,
          solution:    `def celsius_a_fahrenheit(celsius):\n    return (celsius * 9/5) + 32\n\nprint(celsius_a_fahrenheit(0))\nprint(celsius_a_fahrenheit(100))\nprint(celsius_a_fahrenheit(-40))`,
          hints:       ['La fórmula es F = (C × 9/5) + 32. En Python: return (celsius * 9/5) + 32'],
          tests: [
            { description: '0°C = 32.0°F',   check: (out) => out.includes('32.0') || (out.includes('32') && !out.includes('212')) },
            { description: '100°C = 212.0°F', check: (out) => out.includes('212.0') || out.includes('212') },
            { description: '-40°C = -40.0°F', check: (out) => out.includes('-40.0') || (out.includes('-40') && out.split('\n').length >= 3) },
          ],
        },
      ],
    },

    /* ---- LESSON 2 ---- */
    {
      id:        2,
      slug:      'variables-y-tipos',
      module:    1,
      moduleTitle: 'Fundamentos Reales',
      title:     'Variables y tipos — la memoria importa',
      hook:      '¿Por qué a = b no es lo mismo que en matemáticas?',
      concept:   'Tipos · Mutabilidad · Referencias vs valores',
      completed: true,
      description: `En Python, cada valor tiene un <strong>tipo</strong>. El tipo determina qué operaciones puedes hacer con él y cuánta memoria ocupa.\n\nCuando escribes <code>a = b</code>, no copias el valor: <strong>apuntas a la misma caja de memoria</strong>. Esto importa más de lo que parece.\n\nLos tipos básicos son: <code>str</code>, <code>int</code>, <code>float</code>, <code>bool</code>, y <code>None</code>.`,
      codeExample: `nombre  = <span class="str">"Ana"</span>      <span class="comment"># str</span>
edad    = <span class="num">25</span>         <span class="comment"># int</span>
altura  = <span class="num">1.65</span>       <span class="comment"># float</span>
activo  = <span class="kw">True</span>       <span class="comment"># bool</span>
<span class="fn">print</span>(<span class="fn">type</span>(nombre))  <span class="comment"># &lt;class 'str'&gt;</span>`,
      exercises: [
        {
          id:          'l2-e1',
          level:       'basic',
          levelLabel:  'Básico',
          xp:          10,
          title:       'Inspeccionar tipos',
          description: 'Crea una variable de cada tipo: <code>str</code>, <code>int</code>, <code>float</code> y <code>bool</code>. Imprime el <code>type()</code> de cada una.',
          starterCode: `mi_texto    = "Python"
mi_entero   = 42
mi_decimal  = 3.14
mi_booleano = True

print(type(mi_texto))
print(type(mi_entero))
print(type(mi_decimal))
print(type(mi_booleano))`,
          solution:    `mi_texto = "Python"\nmi_entero = 42\nmi_decimal = 3.14\nmi_booleano = True\nprint(type(mi_texto))\nprint(type(mi_entero))\nprint(type(mi_decimal))\nprint(type(mi_booleano))`,
          hints:       ['Usa type(variable) para conocer el tipo de cualquier valor.'],
          tests: [
            { description: "Muestra <class 'str'>",   check: (o) => o.includes("class 'str'") },
            { description: "Muestra <class 'int'>",   check: (o) => o.includes("class 'int'") },
            { description: "Muestra <class 'float'>", check: (o) => o.includes("class 'float'") },
            { description: "Muestra <class 'bool'>",  check: (o) => o.includes("class 'bool'") },
          ],
        },
        {
          id:          'l2-e2',
          level:       'intermediate',
          levelLabel:  'Intermedio',
          xp:          25,
          title:       'Conversión de tipos',
          description: 'El usuario ingresa su edad como texto: <code>edad_texto = "28"</code>. Conviértela a entero, suma 5 y muestra el resultado. Luego conviértela a float y muéstrala también.',
          starterCode: `edad_texto = "28"

# Convierte a entero y suma 5
edad_int = ___
print(edad_int + 5)

# Convierte a float
edad_float = ___
print(edad_float)`,
          solution:    `edad_texto = "28"\nedad_int = int(edad_texto)\nprint(edad_int + 5)\nedad_float = float(edad_texto)\nprint(edad_float)`,
          hints:       ['Usa int() para convertir a entero y float() para convertir a decimal.'],
          tests: [
            { description: 'Edad + 5 = 33', check: (o) => o.includes('33') },
            { description: 'Como float: 28.0', check: (o) => o.includes('28.0') },
          ],
        },
        {
          id:          'l2-e3',
          level:       'advanced',
          levelLabel:  'Avanzado',
          xp:          50,
          title:       'Mutabilidad profunda',
          description: 'Crea una lista <code>original = [1, 2, 3]</code>. Crea <code>copia = original</code>. Añade el número 4 a <code>copia</code>. Imprime ambas listas. ¿Por qué cambia también <code>original</code>? Luego crea una copia real usando slicing y demuestra que ahora son independientes.',
          starterCode: `original = [1, 2, 3]
copia = original
copia.append(4)

print("original:", original)
print("copia:", copia)

# Ahora crea una copia REAL (independiente)
original2 = [1, 2, 3]
copia_real = ___
copia_real.append(99)

print("original2:", original2)
print("copia_real:", copia_real)`,
          solution:    `original = [1, 2, 3]\ncopia = original\ncopia.append(4)\nprint("original:", original)\nprint("copia:", copia)\n\noriginal2 = [1, 2, 3]\ncopia_real = original2[:]\ncopia_real.append(99)\nprint("original2:", original2)\nprint("copia_real:", copia_real)`,
          hints:       ['Para copiar una lista sin referenciar la original usa original2[:] o list(original2).'],
          tests: [
            { description: 'original también cambia a [1,2,3,4]', check: (o) => o.includes('[1, 2, 3, 4]') },
            { description: 'original2 NO cambia con la copia real',check: (o) => o.includes('original2: [1, 2, 3]') },
          ],
        },
      ],
    },

    /* ---- LESSON 3 ---- */
    {
      id:        3,
      slug:      'condicionales',
      module:    1,
      moduleTitle: 'Fundamentos Reales',
      title:     'Condicionales — lógica booleana',
      hook:      '¿Cómo sabe tu banco si debe rechazar una transacción?',
      concept:   'if/elif/else · Boolean algebra · De Morgan · Short-circuit evaluation',
      completed: false,
      description: `Los condicionales permiten que tu programa <strong>tome decisiones</strong>. Sin ellos, el código haría lo mismo sin importar qué datos recibe.\n\nPython evalúa expresiones <strong>booleanas</strong>: cosas que son <code>True</code> o <code>False</code>. Puedes combinarlas con <code>and</code>, <code>or</code> y <code>not</code>.\n\nLa <strong>evaluación corta (short-circuit)</strong>: si en <code>A and B</code>, A es False, Python ni evalúa B.`,
      codeExample: `saldo = <span class="num">150</span>
monto = <span class="num">200</span>

<span class="kw">if</span> saldo >= monto:
    <span class="fn">print</span>(<span class="str">"Transacción aprobada"</span>)
<span class="kw">elif</span> saldo > <span class="num">0</span>:
    <span class="fn">print</span>(<span class="str">"Saldo insuficiente"</span>)
<span class="kw">else</span>:
    <span class="fn">print</span>(<span class="str">"Cuenta sin fondos"</span>)`,
      exercises: [
        {
          id:          'l3-e1',
          level:       'basic',
          levelLabel:  'Básico',
          xp:          10,
          title:       'Clasificador de edades',
          description: 'Dado <code>edad = 17</code>, imprime <code>"menor de edad"</code> si es menor de 18, <code>"adulto"</code> si tiene entre 18 y 64, y <code>"adulto mayor"</code> si tiene 65 o más.',
          starterCode: `edad = 17

if ___:
    print("menor de edad")
elif ___:
    print("adulto")
else:
    print("adulto mayor")`,
          solution:    `edad = 17\nif edad < 18:\n    print("menor de edad")\nelif edad < 65:\n    print("adulto")\nelse:\n    print("adulto mayor")`,
          hints:       ['Recuerda: usa < para "menor que" y >= para "mayor o igual que".'],
          tests: [
            { description: 'edad=17 → "menor de edad"', check: (o) => o.includes('menor de edad') },
          ],
        },
        {
          id:          'l3-e2',
          level:       'intermediate',
          levelLabel:  'Intermedio',
          xp:          25,
          title:       'Validador de contraseña',
          description: 'Escribe una función <code>es_contrasena_valida(pwd)</code> que retorne <code>True</code> si la contraseña tiene al menos 8 caracteres, contiene al menos un número y al menos una mayúscula. Pruébala con 3 contraseñas distintas.',
          starterCode: `def es_contrasena_valida(pwd):
    tiene_largo = len(pwd) >= 8
    tiene_numero = any(c.isdigit() for c in pwd)
    tiene_mayuscula = ___
    return tiene_largo and tiene_numero and tiene_mayuscula

print(es_contrasena_valida("Python3!"))   # True
print(es_contrasena_valida("python3"))    # False (sin mayúscula)
print(es_contrasena_valida("Py3"))        # False (muy corta)`,
          solution:    `def es_contrasena_valida(pwd):\n    tiene_largo = len(pwd) >= 8\n    tiene_numero = any(c.isdigit() for c in pwd)\n    tiene_mayuscula = any(c.isupper() for c in pwd)\n    return tiene_largo and tiene_numero and tiene_mayuscula\n\nprint(es_contrasena_valida("Python3!"))\nprint(es_contrasena_valida("python3"))\nprint(es_contrasena_valida("Py3"))`,
          hints:       ['Usa any(c.isupper() for c in pwd) para verificar si hay alguna mayúscula.'],
          tests: [
            { description: '"Python3!" → True',  check: (o) => { const l = o.trim().split('\n'); return l[0]?.trim() === 'True'; } },
            { description: '"python3" → False', check: (o) => { const l = o.trim().split('\n'); return l[1]?.trim() === 'False'; } },
          ],
        },
        {
          id:          'l3-e3',
          level:       'advanced',
          levelLabel:  'Avanzado',
          xp:          50,
          title:       'Clasificador FizzBuzz',
          description: 'Escribe una función <code>fizzbuzz(n)</code> que retorne <code>"FizzBuzz"</code> si n es divisible por 3 y 5, <code>"Fizz"</code> si solo por 3, <code>"Buzz"</code> si solo por 5, o el número como string en caso contrario. Pruébala con los números del 1 al 20.',
          starterCode: `def fizzbuzz(n):
    # Implementa la lógica aquí
    # Pista: el orden de las condiciones importa
    pass

for i in range(1, 21):
    print(fizzbuzz(i))`,
          solution:    `def fizzbuzz(n):\n    if n % 3 == 0 and n % 5 == 0:\n        return "FizzBuzz"\n    elif n % 3 == 0:\n        return "Fizz"\n    elif n % 5 == 0:\n        return "Buzz"\n    else:\n        return str(n)\n\nfor i in range(1, 21):\n    print(fizzbuzz(i))`,
          hints:       ['Verifica primero la condición de 15 (FizzBuzz) antes que las individuales. El orden importa.'],
          tests: [
            { description: '15 → "FizzBuzz"', check: (o) => { const l = o.trim().split('\n'); return l[14]?.trim() === 'FizzBuzz'; } },
            { description: '3 → "Fizz"',     check: (o) => { const l = o.trim().split('\n'); return l[2]?.trim() === 'Fizz'; } },
            { description: '5 → "Buzz"',     check: (o) => { const l = o.trim().split('\n'); return l[4]?.trim() === 'Buzz'; } },
          ],
        },
      ],
    },

    /* ---- LESSON 4 ---- */
    {
      id:        4,
      slug:      'loops',
      module:    1,
      moduleTitle: 'Fundamentos Reales',
      title:     'Loops — iteración como superpoder',
      hook:      '¿Cómo imprimirías 10,000 emails sin copiar y pegar?',
      concept:   'for · while · range · break/continue · Off-by-one errors',
      completed: false,
      description: `Los loops son el mecanismo que convierte 10,000 instrucciones repetidas en <strong>3 líneas de código</strong>.\n\n<code>for</code> itera sobre una secuencia (lista, string, range). <code>while</code> itera mientras una condición sea True.\n\nEl error más común en loops es el <strong>off-by-one</strong>: contar de 1 a 10 pero obtener del 1 al 9, o del 1 al 11.`,
      codeExample: `nombres = [<span class="str">"Ana"</span>, <span class="str">"Luis"</span>, <span class="str">"María"</span>]

<span class="kw">for</span> nombre <span class="kw">in</span> nombres:
    <span class="fn">print</span>(<span class="str">f"Hola, {nombre}!"</span>)

<span class="comment"># range(5) genera: 0, 1, 2, 3, 4</span>
<span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">5</span>):
    <span class="fn">print</span>(i)`,
      exercises: [
        {
          id:          'l4-e1',
          level:       'basic',
          levelLabel:  'Básico',
          xp:          10,
          title:       'Suma de lista',
          description: 'Dada la lista <code>numeros = [3, 7, 2, 9, 1, 5]</code>, usa un <code>for</code> loop para sumar todos los elementos. Imprime el total.',
          starterCode: `numeros = [3, 7, 2, 9, 1, 5]
total = 0

for numero in numeros:
    total = ___

print(total)`,
          solution:    `numeros = [3, 7, 2, 9, 1, 5]\ntotal = 0\nfor numero in numeros:\n    total = total + numero\nprint(total)`,
          hints:       ['Acumula el valor: total = total + numero, o más idiomático: total += numero'],
          tests: [
            { description: 'La suma es 27', check: (o) => o.trim() === '27' },
          ],
        },
        {
          id:          'l4-e2',
          level:       'intermediate',
          levelLabel:  'Intermedio',
          xp:          25,
          title:       'Analizador de palabras',
          description: 'Escribe una función <code>contar_palabras_largas(texto)</code> que cuente cuántas palabras en el texto tienen más de 5 letras. Pruébala con la frase: <code>"Python es un lenguaje de programacion poderoso"</code>.',
          starterCode: `def contar_palabras_largas(texto):
    palabras = texto.split()
    contador = 0
    for palabra in palabras:
        if ___:
            contador += 1
    return contador

resultado = contar_palabras_largas("Python es un lenguaje de programacion poderoso")
print(resultado)`,
          solution:    `def contar_palabras_largas(texto):\n    palabras = texto.split()\n    contador = 0\n    for palabra in palabras:\n        if len(palabra) > 5:\n            contador += 1\n    return contador\n\nresultado = contar_palabras_largas("Python es un lenguaje de programacion poderoso")\nprint(resultado)`,
          hints:       ['Usa len(palabra) > 5 para verificar si una palabra tiene más de 5 letras.'],
          tests: [
            { description: 'Resultado es 3', check: (o) => o.trim() === '3' },
          ],
        },
        {
          id:          'l4-e3',
          level:       'advanced',
          levelLabel:  'Avanzado',
          xp:          50,
          title:       'Analizador de frecuencias',
          description: 'Escribe una función <code>frecuencia_palabras(texto)</code> que retorne un diccionario con la frecuencia de cada palabra, case-insensitive (todo en minúsculas). Pruébala e imprime el resultado.',
          starterCode: `def frecuencia_palabras(texto):
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        # Si la palabra ya existe, suma 1; si no, inicializa en 1
        ___
    return frecuencias

texto = "Python es genial Python es rapido Python"
resultado = frecuencia_palabras(texto)
print(resultado)`,
          solution:    `def frecuencia_palabras(texto):\n    palabras = texto.lower().split()\n    frecuencias = {}\n    for palabra in palabras:\n        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1\n    return frecuencias\n\ntexto = "Python es genial Python es rapido Python"\nresultado = frecuencia_palabras(texto)\nprint(resultado)`,
          hints:       ["Usa dict.get(key, 0) para obtener el valor actual o 0 si no existe: frecuencias[p] = frecuencias.get(p, 0) + 1"],
          tests: [
            { description: 'python aparece 3 veces', check: (o) => o.includes("'python': 3") || o.includes('"python": 3') },
            { description: 'es aparece 2 veces',     check: (o) => o.includes("'es': 2") || o.includes('"es": 2') },
          ],
        },
      ],
    },

    /* ---- LESSON 5 ---- */
    {
      id:        5,
      slug:      'funciones',
      module:    2,
      moduleTitle: 'Estructuras de Datos',
      title:     'Funciones — abstracciones',
      hook:      '¿Qué es una función matemática? ¿Por qué Python las tiene?',
      concept:   'def · return · Scope · Pure functions · Recursión básica',
      completed: false,
      description: `Una función es un <strong>bloque de código reutilizable</strong> con un nombre. La defines una vez y la llamas cuantas veces quieras.\n\nUna función <strong>pura</strong> (la mejor clase de función): dado el mismo input, siempre devuelve el mismo output. Sin efectos secundarios.\n\nEl <strong>scope</strong>: las variables creadas dentro de una función no existen fuera. Esto evita bugs entre partes del código.`,
      codeExample: `<span class="kw">def</span> <span class="fn">saludar</span>(nombre):
    <span class="str">"""Recibe un nombre y devuelve un saludo."""</span>
    saludo = <span class="str">f"¡Hola, {nombre}!"</span>
    <span class="kw">return</span> saludo

resultado = <span class="fn">saludar</span>(<span class="str">"Ana"</span>)
<span class="fn">print</span>(resultado)  <span class="comment"># ¡Hola, Ana!</span>`,
      exercises: [
        {
          id:          'l5-e1',
          level:       'basic',
          levelLabel:  'Básico',
          xp:          10,
          title:       'Función de saludo',
          description: 'Crea una función <code>saludar(nombre)</code> que devuelva el string <code>"¡Hola, [nombre]!"</code>. Llámala con tu nombre e imprímela.',
          starterCode: `def saludar(nombre):
    # Escribe la función aquí
    pass

resultado = saludar("Python")
print(resultado)`,
          solution:    `def saludar(nombre):\n    return f"¡Hola, {nombre}!"\n\nresultado = saludar("Python")\nprint(resultado)`,
          hints:       ['Usa f-strings: f"¡Hola, {nombre}!" para insertar variables en strings.'],
          tests: [
            { description: 'Devuelve "¡Hola, Python!"', check: (o) => o.includes('Hola') && o.includes('Python') },
          ],
        },
        {
          id:          'l5-e2',
          level:       'intermediate',
          levelLabel:  'Intermedio',
          xp:          25,
          title:       'Calculadora de descuento',
          description: 'Escribe una función <code>calcular_precio_final(precio, descuento_pct)</code> que aplique un descuento porcentual y devuelva el precio redondeado a 2 decimales. Si el descuento es negativo, lanza un ValueError con el mensaje <code>"El descuento no puede ser negativo"</code>.',
          starterCode: `def calcular_precio_final(precio, descuento_pct):
    if descuento_pct < 0:
        raise ValueError("El descuento no puede ser negativo")
    # Calcula el precio con descuento
    ___

print(calcular_precio_final(100, 20))  # 80.0
print(calcular_precio_final(59.99, 10)) # 53.99`,
          solution:    `def calcular_precio_final(precio, descuento_pct):\n    if descuento_pct < 0:\n        raise ValueError("El descuento no puede ser negativo")\n    factor = 1 - (descuento_pct / 100)\n    return round(precio * factor, 2)\n\nprint(calcular_precio_final(100, 20))\nprint(calcular_precio_final(59.99, 10))`,
          hints:       ['El factor de descuento es: 1 - (pct / 100). Luego multiplica el precio por ese factor.'],
          tests: [
            { description: '100 con 20% → 80.0',    check: (o) => o.includes('80.0') },
            { description: '59.99 con 10% → 53.99', check: (o) => o.includes('53.99') },
          ],
        },
        {
          id:          'l5-e3',
          level:       'advanced',
          levelLabel:  'Avanzado',
          xp:          50,
          title:       'Habit Tracker mini',
          description: 'Crea un sistema simple de hábitos. Necesitas: <code>agregar_habito(lista, nombre)</code>, <code>completar_habito(lista, nombre)</code> y <code>mostrar_resumen(lista)</code>. Prueba el sistema completo.',
          starterCode: `def agregar_habito(lista, nombre):
    lista.append({"nombre": nombre, "completado": False})

def completar_habito(lista, nombre):
    for habito in lista:
        if habito["nombre"] == nombre:
            habito["completado"] = True
            return
    raise ValueError(f"Hábito '{nombre}' no encontrado")

def mostrar_resumen(lista):
    # Imprime cada hábito con ✅ o ⏳
    ___

# Prueba el sistema
habitos = []
agregar_habito(habitos, "Ejercicio")
agregar_habito(habitos, "Leer")
agregar_habito(habitos, "Meditar")
completar_habito(habitos, "Ejercicio")
completar_habito(habitos, "Leer")
mostrar_resumen(habitos)`,
          solution:    `def agregar_habito(lista, nombre):\n    lista.append({"nombre": nombre, "completado": False})\n\ndef completar_habito(lista, nombre):\n    for habito in lista:\n        if habito["nombre"] == nombre:\n            habito["completado"] = True\n            return\n    raise ValueError(f"Hábito '{nombre}' no encontrado")\n\ndef mostrar_resumen(lista):\n    for habito in lista:\n        icono = "✅" if habito["completado"] else "⏳"\n        print(f"{icono} {habito['nombre']}")\n\nhabitos = []\nagregar_habito(habitos, "Ejercicio")\nagregar_habito(habitos, "Leer")\nagregar_habito(habitos, "Meditar")\ncompletar_habito(habitos, "Ejercicio")\ncompletar_habito(habitos, "Leer")\nmostrar_resumen(habitos)`,
          hints:       ['Usa un emoji para el estado: "✅" if habito["completado"] else "⏳"'],
          tests: [
            { description: 'Ejercicio está completado (✅)', check: (o) => o.includes('✅') && o.includes('Ejercicio') },
            { description: 'Meditar está pendiente (⏳)',    check: (o) => o.includes('⏳') && o.includes('Meditar') },
          ],
        },
      ],
    },
  ],

  /* -- Plan items for the right panel -- */
  todayPlan: [
    { id: 'p1', title: 'Funciones en Python', sub: 'Lección 5',           done: true },
    { id: 'p2', title: 'Desafío: Calculadora', sub: 'Intermedio',         done: false },
    { id: 'p3', title: 'Proyecto: Habit Tracker', sub: 'Práctico',        done: false },
  ],

  /* -- Community feed -- */
  communityFeed: [
    { id: 'c1', initials: 'ML', color: '#7C3AED', msg: 'María completó el proyecto Habit Tracker 🎉', time: 'hace 2h' },
    { id: 'c2', initials: 'JC', color: '#2EA043', msg: 'Juan respondió en "List comprehensions"',      time: 'hace 3h' },
    { id: 'c3', initials: 'PL', color: '#F97316', msg: 'PythonLover14 logró una racha de 30 días 🔥', time: 'hace 5h' },
  ],

  /* -- Pedagogical error → human feedback map -- */
  errorFeedback: {
    'IndexError':         'Tu código falla cuando la lista está vacía. ¿Qué pasa si llamas a la función con []?',
    'ZeroDivisionError':  'Estás dividiendo sin verificar que el denominador sea cero. Agrega un condicional antes de dividir.',
    'AttributeError':     'Estás llamando un método que no existe en ese tipo de dato. ¿Cuál es el tipo exacto del resultado?',
    'NameError':          'Estás usando una variable que no has definido aún. Revisa el scope de tu función.',
    'TypeError':          'Estás mezclando tipos incompatibles (ej: sumar un string con un número). Usa type() para verificar.',
    'SyntaxError':        'Hay un error de sintaxis. Python no puede leer tu código. Revisa los dos puntos, paréntesis e indentación.',
    'IndentationError':   'La indentación no es consistente. Python usa espacios para definir bloques. Revisa que cada nivel tenga 4 espacios.',
    'ValueError':         'El valor que estás usando no es válido para esa operación (ej: convertir "abc" a int).',
    'KeyError':           'Estás accediendo a una clave que no existe en el diccionario. Usa .get() para evitar este error.',
    'RecursionError':     'Tu función se llama a sí misma infinitamente. Asegúrate de tener un caso base claro.',
    'default':            'Hay un error en tu código. Lee el mensaje de error línea por línea. ¿Qué dice exactamente?',
  },
};
