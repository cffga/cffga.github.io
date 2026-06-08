# Progreso del Proyecto

> Traducción al español de **An Introduction to Statistical Learning with Applications in Python (ISLP)**.

## Resumen

| Capítulo | Estado | Figuras | Laboratorio |
|----------|--------|---------|-------------|
| Prefacio | ✅ Completado | — | — |
| 1. Introducción | ✅ Completado | 4 | — |
| 2. Aprendizaje Estadístico | ✅ Completado | 17 | Externo |
| 3. Regresión Lineal | ✅ Completado | 20 | Externo |
| 4. Clasificación | ⏳ Pendiente | 17 | Externo |
| 5. Métodos de Remuestreo | ⏳ Pendiente | 11 | Externo |
| 6. Selección de Modelos Lineales y Regularización | ⏳ Pendiente | 24 | Externo |
| 7. Más Allá de la Linealidad | ⏳ Pendiente | 14 | Externo |
| 8. Métodos Basados en Árboles | ⏳ Pendiente | 17 | Externo |
| 9. Máquinas de Vectores de Soporte | ⏳ Pendiente | 12 | Externo |
| 10. Aprendizaje Profundo | ⏳ Pendiente | 29 | Externo |
| 11. Análisis de Supervivencia y Datos Censurados | ⏳ Pendiente | 9 | Externo |
| 12. Aprendizaje No Supervisado | ⏳ Pendiente | 20 | Externo |
| 13. Pruebas Múltiples | ⏳ Pendiente | 11 | Externo |

## Flujo de Trabajo

Cada capítulo se traduce siguiendo estas fases:

| Fase | Acción | Verificación |
|------|--------|-------------|
| 0 | Extraer texto del PDF (teoría, págs. según `CLAUDE.md`) | Segmentos alineados con el original |
| 1 | Traducir párrafo a párrafo aplicando glosario y formato | `CLAUDE.md` criterios 1–9 |
| 2 | Verificar terminología y notación contra `CLAUDE.md` y `NOTATION.md` | Consistencia interna |
| 3 | Pase de fluidez académica: eliminar calcos, reestructurar pasivas | Lectura natural en español |
| 4 | `quarto render` + revisión visual de figuras, ecuaciones, tooltips | Sin errores de compilación |
| 5 | Marcar en PROGRESS.md y commit si aplica | Capítulo completo |

## Convenciones del Sistema

- **Notación:** `NOTATION.md` — vinculante para todos los capítulos.
- **Figuras:** Originales del libro en `Figures/ChapterX/png/`.
- **Tooltip hover:** Las referencias `@fig-*` a otros capítulos muestran vista previa al pasar el ratón.
- **Laboratorios:** No se incluyen. Se redirige al sitio oficial.
- **Etiquetas de figuras:** `@fig-{cap}-{num}` (ej: `@fig-2-1`).
