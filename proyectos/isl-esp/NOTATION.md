# Convenciones Notacionales

> Este documento recoge las convenciones de notación establecidas en el capítulo 1 del libro original. **Toda traducción debe respetarlas rigurosamente en todos los capítulos.**

## Observaciones y variables

| Símbolo | Significado |
|---------|-------------|
| $n$ | Número de observaciones (unidades muestrales) |
| $p$ | Número de variables (predictores, características) |
| $x_{ij}$ | Valor de la $j$-ésima variable para la $i$-ésima observación |
| $\mathbf{X}$ | Matriz $n \times p$ de predictores |
| $x_i$ | Vector fila que contiene los $p$ predictores de la $i$-ésima observación |
| $\mathbf{x}_j$ | Vector columna que contiene las $n$ observaciones de la $j$-ésima variable |
| $y_i$ | Valor de la respuesta para la $i$-ésima observación |
| $\mathbf{y}$ | Vector de respuestas de longitud $n$ |
| $\hat{y}_i$ | Predicción de $y_i$ |
| $\hat{\beta}_j$ | Coeficiente estimado para el $j$-ésimo predictor |

## Tipografía

| Elemento | Formato | Ejemplo |
|----------|---------|---------|
| Escalares | Redonda normal | $a$, $n$, $p$, $\beta$, $\hat{\beta}$ |
| Vectores de longitud $n$ | Negrita minúscula | $\mathbf{a}$, $\mathbf{x}$, $\mathbf{y}$ |
| Vectores cortos (no $n$) | Redonda normal | $a$, $x$, $y$ |
| Matrices | Negrita mayúscula | $\mathbf{A}$, $\mathbf{X}$ |
| Espacios ambientales | $\mathbb{R}$ | $\mathbb{R}$, $\mathbb{R}^n$, $\mathbb{R}^{r \times s}$ |

**Nota:** $a \in \mathbb{R}$, $\mathbf{a} \in \mathbb{R}^n$, $\mathbf{A} \in \mathbb{R}^{r \times s}$.

## Números grandes

Usar separador de miles con llaves: $3{,}000$, $10{,}000$, $100{,}000$.

## Ecuaciones

- Las ecuaciones llevan numeración explícita con `\tag{2.1}` (número de capítulo + correlativo).
- Se referencian como `@eq-2-1` o simplemente "Ecuación 2.1".

## Formato de términos específicos

- Variables ($Y$, $X$, $X_1$), datasets (`Wage`, `Smarket`, `NCI60`), funciones (`lm()`, `predict()`, `summary()`) y parámetros en **monospace** con backticks: `` `Y` ``, `` `X_1` ``, `` `lm()` ``.
- Términos extranjeros sin traducción aceptada van en *cursiva* la primera vez en cada capítulo, seguidos de explicación entre paréntesis si es necesario.
- Las negritas y cursivas del original se preservan exactamente en la traducción.

## Nombres de conjuntos de datos

| Dataset | Descripción |
|---------|-------------|
| `Wage` | Datos salariales (Cap. 1, 2, 3, 6, 7, 8) |
| `Smarket` | Datos de mercado de valores (Cap. 1, 4, 9) |
| `NCI60` | Datos de expresión génica (Cap. 1, 10, 12) |
| `Advertising` | Datos de publicidad y ventas (Cap. 2, 3, 4) |
| `Credit` | Datos de crédito bancario (Cap. 3, 6, 7) |
| `Default` | Datos de impago bancario (Cap. 4) |
| `Boston` | Datos de vivienda en Boston (Cap. 2, 3, 5, 6, 8) |
| `Caravan` | Datos de seguros (Cap. 4) |
| `Khan` | Datos de expresión génica (Cap. 4) |
| `OJ` | Datos de jugo de naranja (Cap. 8) |
| `College` | Datos de universidades (Cap. 2, 6) |
| `Auto` | Datos de automóviles (Cap. 2, 3, 5, 6, 7) |
| `Carseats` | Datos de sillas infantiles (Cap. 3) |
| `Portfolio` | Datos financieros (Cap. 5) |
| `USArrests` | Datos de crímenes (Cap. 12) |

## Abreviaciones estándar

| Abrev. | Significado |
|--------|-------------|
| MSE | Error Cuadrático Medio |
| RSS | Suma de Cuadrados Residual |
| $R^2$ | Coeficiente de Determinación |
| EMV | Estimación de Máxima Verosimilitud |
| LDA | Análisis Discriminante Lineal |
| QDA | Análisis Discriminante Cuadrático |
| KNN | $K$ Vecinos Más Cercanos |
| CV | Validación Cruzada |
| LOOCV | Validación Cruzada Dejando Uno Fuera |
| AIC | Criterio de Información de Akaike |
| BIC | Criterio de Información Bayesiano |
| PCA | Análisis de Componentes Principales |
| PCR | Regresión por Componentes Principales |
| PLS | Regresión por Mínimos Cuadrados Parciales |
| GAM | Modelo Aditivo Generalizado |
| SVM | Máquina de Vectores de Soporte |
| SVR | Regresión por Vectores de Soporte |
| RBF | Función de Base Radial |
| CNN | Red Neuronal Convolucional |
| RNN | Red Neuronal Recurrente |
| LSTM | Memoria a Largo y Corto Plazo |
| GAN | Red Generativa Antagónica |
| VAE | Autoencoder Variacional |
| FWER | Tasa de Error por Familia |
| FDR | Tasa de Falsos Descubrimientos |
| ROC | Característica Operativa del Receptor |
| AUC | Área Bajo la Curva ROC |
