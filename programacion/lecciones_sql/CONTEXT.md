# Contexto del proyecto: serie de lecciones de SQL

## Qué es este proyecto

Una serie de lecciones de SQL en formato `.qmd` (Quarto Markdown, renderizado como HTML), continuación del curso de Python del mismo autor. El motor de referencia es **PostgreSQL**. El público son los mismos estudiantes que completaron el curso de Python: gente con formación matemática que ya sabe programar. El objetivo es prepararlos para trabajar con datos reales, en el camino hacia la ciencia de datos.

**Premisa fundamental:** el alumno ya domina Python. Conoce tipos, estructuras de datos (en particular las listas de diccionarios, que son casi una tabla), funciones, control de flujo, comprensiones y objetos. El curso de SQL aprovecha ese conocimiento constantemente: cada concepto nuevo de SQL se presenta como la contraparte declarativa de algo que el alumno ya hacía imperativamente en Python.

---

## Paradigma de redacción

El texto debe producir una sensación ininterrumpida de **continuidad y conexidad**. El lector nunca debe preguntarse "¿por qué estamos hablando de esto ahora?". Cada unidad —párrafo, sección, lección— tiene un borde de entrada que conecta con lo anterior y un borde de salida que deja una tensión concreta que el texto siguiente resolverá.

**El concepto nace de su necesidad.** Ningún concepto se introduce porque "viene a continuación". Primero se articula la limitación del estado actual; después aparece la herramienta que la resuelve.

**La intuición precede al formalismo.** Primero la idea en términos familiares (casi siempre, su equivalente en Python); después la sintaxis precisa de SQL.

**Las conexiones se nombran.** Cuando algo de SQL corresponde a algo de Python ya conocido, el texto lo dice explícitamente: "esto es la comprensión con filtro que ya conoces, ahora declarativa".

**Las dudas se responden donde surgen.** Nunca en notas, apéndices ni secciones posteriores.

**El texto avanza, no circula.** Sin resúmenes intermedios, sin anuncios de lo que el siguiente párrafo dirá, sin relleno.

**Tono:** académico sin ser árido, preciso sin ser oscuro. Prosa continua. Las listas solo para enumeraciones genuinas. Nada de frases motivacionales ni entusiasmo performativo.

---

## El puente Python → SQL

La diferencia conceptual central que el curso explota una y otra vez: Python es **imperativo** (describes *cómo* obtener el resultado, paso a paso, con bucles y condiciones), SQL es **declarativo** (describes *qué* resultado quieres, y el motor decide cómo obtenerlo). Cada construcción de SQL se ancla en su equivalente imperativo de Python:

| SQL | Equivalente en Python que el alumno ya conoce |
|-----|-----------------------------------------------|
| Una tabla | Una lista de diccionarios |
| `SELECT col FROM t` | `[fila["col"] for fila in tabla]` |
| `WHERE cond` | `[f for f in tabla if cond]` |
| `ORDER BY` | `sorted(..., key=...)` |
| `LIMIT n` | slicing `[:n]` |
| `COUNT`, `SUM`, `AVG` | `len`, `sum`, `sum/len` |
| `GROUP BY` | acumular por clave en un diccionario |
| `JOIN` | bucle anidado emparejando por clave |

---

## Restricciones específicas

### Restricción de currículum acumulado (absoluta)

Ninguna palabra clave, función o cláusula de SQL puede aparecer en una consulta ejecutable antes de haber sido introducida en la misma lección o en una anterior. Si algo se menciona en prosa antes de su introducción formal, debe nombrarse como anticipo, indicando en qué lección se explicará.

### Currículum por lección

| # | Lección | Introduce |
|---|---------|-----------|
| 1 | Bases de datos y SELECT | Tabla, fila, columna; `SELECT`, `FROM`, `*`, alias `AS`, `DISTINCT`, columnas calculadas |
| 2 | WHERE | `WHERE`, operadores de comparación, `AND`/`OR`/`NOT`, `BETWEEN`, `IN`, `LIKE`, `IS NULL` |
| 3 | ORDER BY, LIMIT, agregación | `ORDER BY` (ASC/DESC), `LIMIT`, `OFFSET`, `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` |
| 4 | GROUP BY y HAVING | `GROUP BY`, `HAVING`, agregación por grupo |
| 5 | Diseño y CREATE TABLE | Tipos de datos, `CREATE TABLE`, `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, normalización |
| 6 | JOIN | `INNER JOIN`, `LEFT JOIN`, `ON`, alias de tabla, claves foráneas en acción |
| 7 | Subconsultas | Subconsultas escalares, en `WHERE`, con `IN`, `EXISTS`, subconsultas correlacionadas |
| 8 | INSERT, UPDATE, DELETE | `INSERT INTO`, `UPDATE ... SET`, `DELETE`, `RETURNING`, transacciones básicas |
| 9 | Vistas e índices | `CREATE VIEW`, `CREATE INDEX`, cuándo y por qué usarlos |
| 10 | Conexión desde Python | Driver (`psycopg`/`sqlite3`), conexión, cursor, `execute`, consultas parametrizadas, `fetchall`/`fetchone`, `commit`, `with`, puente con pandas |

### Dominio de datos (hilo conductor)

Una **biblioteca**. Las tablas centrales que recorren todo el curso:

- `libros` (id, titulo, autor_id, anio, genero, ejemplares)
- `autores` (id, nombre, nacionalidad, anio_nacimiento)
- `lectores` (id, nombre, email, fecha_registro)
- `prestamos` (id, libro_id, lector_id, fecha_prestamo, fecha_devolucion)

Este dominio es rico en relaciones naturales (un libro tiene un autor; un préstamo conecta un libro con un lector), lo que motiva los JOIN sin artificio. Las primeras lecciones usan solo `libros` y `autores`; las tablas de `lectores` y `prestamos` entran cuando se necesitan los JOIN.

---

## Estructura de cada lección

**Apertura.** Conecta con la limitación del cierre anterior. En la lección 1, conecta con lo que el alumno ya sabe de Python.

**Secciones.** Motivación → equivalente en Python (cuando aplica) → sintaxis SQL → consulta de ejemplo → explicación del resultado y anticipación de dudas → variantes.

**Cierre (`## Lo que sigue`).** Articula la limitación concreta que las herramientas de la lección no resuelven, de modo que la siguiente parezca inevitable.

---

## Nota técnica sobre los ejemplos en `.qmd`

Como PostgreSQL requiere un servidor, los ejemplos se muestran como bloques de código SQL (` ```sql `) acompañados de su resultado esperado en una tabla de texto, en lugar de ejecutarse en vivo. Cuando convenga mostrar ejecución real reproducible, se puede usar un bloque Python con `sqlite3` (compatible en lo esencial para las consultas del curso) o `psycopg`, señalando las diferencias de dialecto cuando existan. El SQL enseñado es PostgreSQL estándar.

---

## Lista de verificación antes de entregar

- [ ] ¿Cada concepto nace de una limitación concreta del estado anterior?
- [ ] ¿Alguna consulta usa una cláusula no introducida aún?
- [ ] ¿Se nombró el equivalente en Python cuando existía?
- [ ] ¿Las dudas previsibles se responden donde surgen?
- [ ] ¿La apertura conecta con el cierre anterior?
- [ ] ¿El cierre articula una necesidad concreta, no una promesa genérica?
- [ ] ¿Los ejemplos usan el dominio de la biblioteca de forma consistente?
- [ ] ¿El texto avanza sin circular ni rellenar?
