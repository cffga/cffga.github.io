# cffga.github.io

Página personal [cffga.github.io](https://cffga.github.io). Sitio estático de una sola página (SPA) servido desde `main` mediante GitHub Pages con Jekyll desactivado (`.nojekyll`).

## Estructura

```
/
├── index.html                  ← Página principal (SPA con navegador de artículos)
├── .nojekyll
│
├── piezas-sueltas/             ← Artículos y escritos personales
├── programacion/
│   └── lecciones_python/       ← Curso de Python (Quarto)
├── proyectos/
│   └── isl-esp/                ← Traducción ISL (Quarto)
│       ├── index.html          ← Redirección → _site/
│       ├── _quarto.yml
│       ├── index.qmd           ← Portada del libro
│       ├── chapters/           ← 13 capítulos traducidos
│       ├── Figures/            ← Figuras originales (PDF + PNG)
│       ├── PROGRESS.md         ← Bitácora del proyecto
│       ├── environment.yml     ← Entorno Conda para compilar
│       └── _site/              ← Sitio compilado (trackeado para GitHub Pages)
├── notas/
└── material-recomendado/
```

## Gestión del SPA (secciones del sitio personal)

Cada sección (Piezas sueltas, Programación, Proyectos, Notas, Material recomendado) es una lista de entradas definida directamente en `index.html` dentro de un `<ul class="entry-list">`.

Para agregar contenido nuevo:

```html
<li>
  <div class="entry-title" data-md="ruta/al/archivo.md">Título</div>
  <div class="entry-meta">Tema · Tipo</div>
  <div class="entry-desc">Descripción breve.</div>
</li>
```

- `data-md="ruta/al/archivo.md"` → se renderiza con marked.js (Markdown → HTML)
- `data-pdf="ruta/al/archivo.pdf"` → se muestra con visor de PDF nativo
- Sin atributo → entrada informativa sin archivo (usar `<span>` en vez de `<div>`)

## Gestión de ISL — Introducción al Aprendizaje Estadístico

Traducción al español de *An Introduction to Statistical Learning with Applications in Python* (James, Witten, Hastie, Tibshirani, Taylor).

**URL**: [cffga.github.io/proyectos/isl-esp/](https://cffga.github.io/proyectos/isl-esp/) (redirige a `_site/`)

### Requisitos para compilar

- [Quarto](https://quarto.org/) >= 1.4
- Python >= 3.12
- `conda env create -f environment.yml && conda activate ISL`

### Cómo actualizar

```bash
conda activate ISL
quarto render
git add -A && git commit -m "Actualiza ISL" && git push
```

### Detalles técnicos importantes

| Aspecto | Explicación |
|---|---|
| `_site/` trackeado | Normalmente se ignora; aquí se trackea porque GitHub Pages sirve desde este directorio. Sin CI/CD, es la única forma de desplegar. |
| `index.html` redirect | `proyectos/isl-esp/index.html` redirige a `_site/` con `<meta http-equiv="refresh" content="0;url=_site/">`. Sin él, la URL limpia da 404. |
| `.gitignore` modificado | Se eliminaron las reglas `_site/` y `*.pdf` del ignore original (ver `proyectos/isl-esp/.gitignore`). |
| `_freeze/` | Cache de ejecución de Quarto. Se regenera solo, se ignora en git. |
| Traducción | Solo cubre el texto explicativo. Laboratorios y ejercicios no traducidos (enlaces a fuentes oficiales al final de cada capítulo). |
| Origen | Copia del repositorio original `~/Projects/ISL_esp/` (con historial git propio), migrada aquí sin historial. |

## Despliegue

```bash
git add -A
git commit -m "mensaje"
git push
```

GitHub Pages despliega desde `main`. Los cambios tardan ~30 s – 2 min en reflejarse.
