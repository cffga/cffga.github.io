# ISL — Introducción al Aprendizaje Estadístico

Traducción al español del libro **An Introduction to Statistical Learning with Applications in Python (ISLP)** de Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani y Jonathan Taylor.

Este proyecto genera un sitio web estático con Quarto que contiene la traducción al español del libro, incluyendo todas las figuras originales. Los laboratorios prácticos y ejercicios no se incluyen; en su lugar se redirige al lector a las fuentes oficiales.

> **Nota:** Toda traducción se realiza **desde cero** a partir del PDF original `ISL (Python).pdf`, siguiendo las directrices de [`CLAUDE.md`](CLAUDE.md). Las convenciones notacionales están definidas en [`NOTATION.md`](NOTATION.md).

## Estructura del proyecto

```
ISL_esp/
├── _quarto.yml                  # Configuración global del sitio
├── index.qmd                    # Portada
├── custom.scss                  # Estilos (tooltips, tipografía)
├── CLAUDE.md                    # Directrices vinculantes de traducción
├── NOTATION.md                  # Convenciones notacionales
├── figures-map.json             # Mapeo @fig-* → rutas de imágenes
├── scripts/
│   ├── preview.html             # JS para tooltip hover en figuras
│   └── generate-figures-map.sh  # Regenerar figures-map.json
├── Figures/                     # Figuras originales del libro
│   └── ChapterX/png/            #    Cap. X (PNG, 200 DPI)
├── chapters/
│   ├── 00-prefacio/             # Prefacio
│   ├── 01-introduccion/         # Cap. 1 — Introducción
│   ├── 02-aprendizaje-estadistico/ # Cap. 2 — Aprendizaje Estadístico
│   └── ...                      # Caps. 3–13
├── _site/                       # Sitio generado (no trackeado)
└── _freeze/                     # Cache de ejecución (no trackeado)
```

Cada capítulo es un archivo `chapters/XX-tema/index.qmd` que contiene:
- Texto traducido al español con numeración de secciones del original
- Figuras desde `Figures/ChapterX/png/` etiquetadas como `@fig-{cap}-{num}`
- Enlace a los laboratorios oficiales al final

## Requisitos

- [Quarto](https://quarto.org/) >= 1.9

## Cómo construir el sitio

```bash
quarto render
```

El sitio generado estará en `_site/`. Para vista previa:

```bash
quarto preview
```

## Flujo de Traducción

Ver [`PROGRESS.md`](PROGRESS.md) para el estado actual.

Cada capítulo se traduce en 5 fases (detalle en `CLAUDE.md`):

1. **Preparación** — extraer texto del PDF, segmentar por subsección
2. **Traducción** — párrafo a párrafo con glosario, preservando LaTeX, `@fig-*`, negritas/cursivas/monospace y numeración
3. **Terminología y notación** — verificar contra `CLAUDE.md` y `NOTATION.md`
4. **Fluidez académica** — eliminar calcos, reestructurar pasivas
5. **Verificación técnica** — `quarto render`, revisar figuras y tooltips

## Hover Preview

Las referencias a figuras (`@fig-2-1`, `@fig-3-5`, etc.) muestran automáticamente una vista previa de la imagen al pasar el ratón, incluso para figuras de otros capítulos. No requiere marcado adicional.

## Despliegue

El workflow de GitHub Actions (`.github/workflows/deploy.yml`) construye y publica automáticamente en GitHub Pages.

## Licencia

El libro original es © Springer Nature Switzerland AG 2023. Esta traducción es un proyecto comunitario sin fines de lucro.
