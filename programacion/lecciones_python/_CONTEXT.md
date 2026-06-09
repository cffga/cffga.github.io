# Contexto del proyecto: serie de lecciones de Python

## Qué es este proyecto

Una serie de lecciones de Python en formato `.qmd` (Quarto Markdown, renderizado como HTML) dirigida a estudiantes universitarios con formación en matemáticas, física o actuaría. El objetivo final es prepararlos para ciencia de datos. El entorno de práctica es Google Colab.

---

## Paradigma de redacción

El texto debe producir una sensación ininterrumpida de **continuidad y conexidad**. El lector nunca debe preguntarse "¿por qué estamos hablando de esto ahora?". Cada unidad del texto —párrafo, sección, lección— tiene dos bordes obligatorios: un borde de entrada que conecta con lo anterior, y un borde de salida que deja una tensión concreta que el texto siguiente vendrá a resolver.

**El concepto nace de su necesidad.** Ningún concepto se introduce porque "viene a continuación". Primero se articula la limitación del estado actual; después aparece la herramienta que la resuelve. La herramienta nunca precede a la necesidad.

**La intuición precede al formalismo.** Primero se construye la idea en términos familiares; después se le da forma precisa. El orden nunca se invierte.

**Las conexiones se nombran.** Cuando algo nuevo se apoya en algo ya visto, el texto lo dice explícitamente. No se asume que el lector verá la conexión solo.

**Las dudas se responden donde surgen.** Cuando un lector razonable levantaría una objeción al leer cierta línea, la respuesta aparece en ese párrafo o en el siguiente. Nunca en notas, apéndices ni secciones posteriores.

**El texto avanza, no circula.** Cada párrafo añade algo que el anterior no tenía. No hay resúmenes intermedios, no hay anuncios de lo que el siguiente párrafo dirá, no hay relleno de ningún tipo.

**Tono:** académico sin ser árido, preciso sin ser oscuro. Las ideas se desarrollan en prosa continua. Las listas se reservan para enumeraciones donde la separación visual es parte del significado. No aparecen nunca frases motivacionales, entusiasmo performativo ni introducciones que anuncian en lugar de decir.

---

## Restricciones específicas de este proyecto

### Restricción absoluta: currículum acumulado

Ningún concepto, función, operador, método, módulo o construcción sintáctica puede aparecer en **código ejecutable** antes de haber sido formalmente introducido en la misma lección o en una anterior. Esta regla no tiene excepciones. Si algo no puede usarse sin violarla, se busca una alternativa con las herramientas disponibles o se reordena la secuencia de lecciones.

Si algo pendiente de explicación se menciona en **prosa**, debe nombrarse explícitamente como anticipo e indicar en qué lección llegará su explicación.

### Currículum disponible por lección

| # | Lección | Introduce |
|---|---------|-----------|
| 1 | Introducción | Aritmética, tipos numéricos (`int`, `float`, `complex`), variables, comentarios |
| 2 | Operadores y secuencias | Booleanos, operadores de comparación, `and`/`or`/`not`, listas, tuplas, cadenas, indexación, slicing, `in`, anidamiento |
| 3 | Funciones | Built-ins: `len`, `min`, `max`, `round`, `print`, `sum`, `sorted`, `set`, `list`, `tuple`; `def`, parámetros, `return`, variables locales, keyword arguments, `help`, f-strings |
| 4 | Estructuras de datos | `list`, `tuple`, `set`, `dict`; desempaquetado, operaciones de conjuntos (`\|`,`&`,`-`,`^`), acceso por clave, conversión entre estructuras |
| 5 | Estructuras de control | `if`, `elif`, `else`, condiciones compuestas, `if` anidados, múltiples `return`, `None`, retorno temprano, cláusulas de guarda, `is not None` |
| 6 | Bucles | `for`, `while`, `break`, `continue`, `range()`, `enumerate()`, `zip()`, acumulación, construcción de listas con concatenación |
| 7 | Comprensiones | Comprensiones de lista, conjunto y diccionario, con filtro y anidadas |
| 8 | Errores y excepciones | `try`/`except`/`else`/`finally`, tipos de excepción, `raise`, `as e` |
| 9 | Objetos y métodos | Notación de punto, `type()`, `dir()`; métodos de `list`, `str`, `dict`, `set` |
| 10 | Clases y atributos | `class`, `__init__`, `self`, atributos de instancia y de clase |
| 11 | Métodos propios | Métodos propios, `__str__`, `__repr__`, métodos especiales |
| 12 | Herencia y composición | Herencia, `super()`, override, `isinstance()`, composición |
| 13 | Funciones como objetos | Funciones como argumentos, `key=`, `lambda`, `map()`, `filter()`, clausuras |
| 14 | Módulos | `import` y sus formas, `math`, `statistics`, `random`, `json`, `os.path`, `decimal`, paquetes externos |
| 15 | Archivos | `open()`, `with`, modos de apertura, lectura y escritura de texto, CSV, JSON con archivos |

### Lo que aún no existe en lecciones anteriores a su introducción

Antes de la lección 9: ningún método de objeto (notación `objeto.método()`). Antes de la lección 14: ningún `import`. Antes de la lección 15: ninguna operación de archivo.

### Hilo conductor de datos

A lo largo de toda la serie aparecen los mismos datos: lecturas de temperatura de un sensor, calificaciones de un grupo de estudiantes, la función `clasificar()` (introducida en la lección 5), y el grupo de alumnos como lista de diccionarios (desde la lección 4). Los ejemplos nuevos deben reutilizar estos datos siempre que sea posible. El alumno no debe invertir energía cognitiva en entender el dominio del problema: toda su atención debe ir al concepto nuevo.

---

## Estructura de cada lección

**Apertura.** Conecta con la limitación articulada al cierre de la lección anterior. No es un resumen de lo anterior ni una lista de "en esta lección veremos". Es la identificación precisa de la grieta que esta lección viene a llenar.

**Secciones.** Cada sección sigue la secuencia: motivación → explicación en prosa → bloque de código mínimo y enfocado → párrafo que explica el código y anticipa dudas → extensión si hay matices adicionales. El código nunca aparece antes de la explicación que lo justifica.

**Cierre (`## Lo que sigue`).** No resume lo visto. Articula la limitación concreta que las herramientas recién aprendidas todavía no pueden resolver, de forma que la siguiente lección parezca inevitable. Una promesa genérica ("la siguiente lección introduce X") es un cierre fallido; una necesidad concreta es un cierre bien construido.

---

## Lista de verificación antes de entregar cualquier contenido

- [ ] ¿Cada concepto nuevo está motivado por una limitación concreta del estado anterior?
- [ ] ¿Algún bloque ejecutable usa algo no introducido aún en el currículum?
- [ ] ¿Algún método de objeto aparece antes de la lección 9?
- [ ] ¿Algún `import` aparece antes de la lección 14?
- [ ] ¿Las dudas más previsibles del lector están respondidas en el lugar donde surgen?
- [ ] ¿La apertura conecta con el cierre de la lección anterior?
- [ ] ¿El cierre articula una necesidad concreta, no una promesa genérica?
- [ ] ¿Los ejemplos reutilizan el hilo de datos de la serie?
- [ ] ¿El texto avanza sin circular, sin resúmenes intermedios, sin relleno?
