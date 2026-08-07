# Censo de duplicación y calidad del catálogo

Medición de los 3.835 nodos contra la vara vigente. **Estrictamente de solo
lectura**: no se tocó un nodo, un pack, el grafo ni producción. Nada se depreca
y nada se cambia; este documento no decide, informa.

Corrido el 2026-08-07 con `scripts/censo_duplicacion.py`. **Costo medido: $0,62.**

---

## 1. El instrumento y su umbral

**El instrumento** es la etapa de consolidación de `extraer_mundo.py`, la misma
que curó a los dos packs de control, en modo solo-propuesta. Se adaptó a un
script suelto de lectura porque allí juzga *conceptos de índice* (título más una
línea) y aquí juzga *nodos ya nacidos* (título, resumen, pasos). El original no
se tocó.

Funciona en dos pasos, y el orden es el que hace válido el número:

1. **Candidatos, local y gratis.** Coseno sobre los embeddings Voyage que ya
   existen (3.835 nodos, 512 dimensiones). Solo intra-pack: dos mundos pueden
   repetir un concepto a propósito, y compararlos entre sí no diría nada.
2. **Veredicto, el consolidador.** Cada cluster candidato se le pasa al modelo
   con la pregunta de la vara: *¿es el mismo concepto con dos nombres, o son dos
   que llevan a acciones distintas?*

**El umbral: coseno ≥ 0,90, idéntico para los diez packs.** Calibrado contra el
control: a 0,90 compras da 0 pares y entrega 6; a 0,85 dan 25 y 32, que ya es
ruido de un espacio de embeddings denso.

**Por qué el segundo paso no es opcional.** Entrega, que es control, produjo
**21,3% de candidatos** y el consolidador rechazó **los cuatro clusters**: en un
mundo de empaque, "elegir la caja", "elegir el relleno" y "elegir sobre o caja"
se parecen muchísimo y llevan a acciones distintas. Sin el veredicto, este censo
habría acusado al propio control de estar tan inflado como Calidad.

---

## 2. La tabla, estratificada por era del pipeline

La era es lo que explica los números. No es lo mismo un pack troceado a granel
que uno curado concepto a concepto.

| Pack | Nodos | Era del pipeline | Clusters | Confirmados | Nodos en duplicado | **Tasa** |
|---|---:|---|---:|---:|---:|---:|
| **Compras** | 46 | vara vigente · CONTROL | 0 | 0 | 0 | **0,0 %** |
| **Entrega** | 47 | vara vigente · CONTROL | 4 | 0 | 0 | **0,0 %** |
| Seguridad Digital | 55 | intermedia | 1 | 1 | 2 | 3,6 % |
| Riesgos | 55 | SOP v1.4 | 2 | 1 | 2 | 3,6 % |
| Exportación | 158 | intermedia | 8 | 7 | 15 | 9,5 % |
| Ambiente | 311 | a granel puro | 20 | 17 | 34 | 10,9 % |
| **Núcleo** | 1.721 | a granel puro | 93 | 90 | 194 | 11,3 % |
| Franquicias | 214 | intermedia | 16 | 13 | 26 | 12,1 % |
| Seguridad y Personas | 332 | a granel puro | 29 | 27 | 57 | 17,2 % |
| Calidad | 896 | a granel puro | 69 | 66 | 156 | **17,4 %** |

**Por era, promedio ponderado por nodos:**

| Era | Packs | Nodos | Tasa |
|---|---|---:|---:|
| Vara vigente (control) | compras, entrega | 93 | **0,0 %** |
| SOP v1.4 | risk_management | 55 | 3,6 % |
| Intermedia | franquicias, exportacion, seguridad_digital | 427 | 9,8 % |
| A granel puro | core, quality, health_safety, environmental | 3.260 | 13,2 % |

La escalera es limpia y monotónica: **cada vuelta del proceso bajó la
duplicación**, y la vara vigente la lleva a cero. El SOP v1.4 (Riesgos) ya
llegaba a 3,6% sin consolidador, lo que dice que el salto grande lo dio el
**índice curado**, y el consolidador cerró el resto.

**Total del catálogo: 486 nodos en 222 clusters confirmados, un 12,7% de los
3.835.**

---

## 3. Los peores clusters (muestra legible)

### Calidad — el caso extremo

| Sim. | Nodos del cluster | Etapa |
|---|---|---|
| 0,967 | **Siete** nodos de *Costo de Mala Calidad*: "Cost of Poor Quality" · "COPQ (Costos que…)" · "COPQ (Cómo se Mide)" · "COPQ (Incumplimiento)" · "En Promedio 15% de…" · "Cost of Poor Quality" · "Costo de la Calidad Pobre (COPQ / COP3)" | ejecución |
| 0,952 | **Seis** nodos de *Calidad como Conformidad con los Requisitos* (la misma definición de Crosby, seis veces) | validación |
| 0,957 | **Cuatro** de *Cero Defectos*: "Zero Defects (ZD)" · "ZD como Actitud de Prevención" · "Concepto de Zero Defects" · "Programa de Cero Defectos" | planificación |

### Núcleo

| Sim. | Nodos del cluster | Etapa |
|---|---|---|
| 0,955 | **Cinco** definiciones de *startup*: "Búsqueda vs. Ejecución" · "Definición de Startup" · "Organización Temporal en Búsqueda" · "bajo Incertidumbre Extrema" · "Búsqueda vs. Ejecución" | ideación |
| 0,937 | **Cinco** de *Pivotar o Proceder*: "Decisión: Pivotar o Proceder" · "Pivot or Proceed" · "Re-validar el Modelo" · "Re-Validación del Modelo" · "Re-Validar el Business Model" | validación |
| 0,948 | **Cuatro** de *preguntas Need-Payoff* de SPIN | ejecución |

### Seguridad y Personas

| Sim. | Nodos del cluster |
|---|---|
| 0,924 | *Fallas Activas y Condiciones Latentes* ×3 (dos con la misma redacción, una con "Fallos") |
| 0,923 | *Evaluación del Programa de Seguridad* ×3 |
| 0,907 | *Safety-II* ×3: "Resiliencia y Safety Differently" · "Safety I versus Safety II" · "Safety II como Capacidad de Éxito" |

Los diez peores de cada pack, con el veredicto textual del consolidador, están
en `docs/_censo_muestras.json`.

---

## 4. Dónde se infló: granularidad por fuente

El patrón es consistente y dice mucho: **los libros más troceados son los que
más duplican**, y los manuales cortos duplican por otra razón (el mismo tema
cubierto por dos publicaciones).

| Pack | Fuente | Nodos duplicados / total | Tasa |
|---|---|---:|---:|
| Seguridad y Personas | OSHA 3885 | 11 / 24 | **45,8 %** |
| Seguridad y Personas | OSHA 3886 | 9 / 27 | **33,3 %** |
| Núcleo | Businessperson's Guide to Federal Warranty Law | 4 / 12 | 33,3 % |
| Calidad | *Quality is Free* (Crosby) | 38 / 130 | **29,2 %** |
| Núcleo | *The Startup Owner's Manual* | 69 / 233 | **29,6 %** |
| Núcleo | SPIN Selling | 10 / 53 | 18,9 % |
| Núcleo | Winning at New Products | 32 / 183 | 17,5 % |
| Seguridad y Personas | Managing the Risks of Organizational Accidents | 19 / 112 | 17,0 % |
| Calidad | Juran's Quality Handbook | 92 / 570 | 16,1 % |
| Calidad | *Out of the Crisis* (Deming) | 26 / 196 | 13,3 % |
| Ambiente | The Green to Gold Business Playbook | 30 / 242 | 12,4 % |
| Franquicias | Franchise Your Business | 26 / 214 | 12,1 % |
| Exportación | A Basic Guide to Exporting | 15 / 158 | 9,5 % |

Las dos guías de OSHA se llevan el récord: **casi la mitad de OSHA 3885 está
duplicada**, casi con seguridad contra su gemela OSHA 3886, que cubre el mismo
marco. Son documentos cortos que el troceo a 5.000 palabras partió en pedazos
solapados.

*The Startup Owner's Manual* aporta **69 nodos duplicados**, el mayor volumen
absoluto del catálogo: es el libro más largo y el más troceado del núcleo.

---

## 5. Las otras tres barandas (muestreo)

Diez nodos al azar por pack (semilla fija `20260807`, repetible), contra las tres
barandas que los packs viejos no vivieron. **Los hallazgos son pocos, y hay que
leerlos con cuidado: dos de los siete son falsos positivos de mi detector, y lo
digo antes de que el número pase por bueno.**

| Pack | Nodos con hallazgo | Tipo |
|---|---:|---|
| Núcleo | 1 / 10 | residuo corporativo |
| Seguridad y Personas | 2 / 10 | dato local · matriz |
| Ambiente | 1 / 10 | residuo corporativo |
| Exportación | 2 / 10 | residuo corporativo ×2 |
| Riesgos | 1 / 10 | *falso positivo* |
| Calidad · Franquicias · Seg. Digital | 0 / 10 | — |
| **Compras · Entrega (control)** | **0 / 10** | — |

### Los hallazgos reales, citados

**Residuo corporativo** — la lente de persona sola:

> **Núcleo · El Blueprint de Experiencia:** *"…rediseñar el 'handoff' entre **el
> equipo de ventas** y **el equipo de cuentas/soporte**…"*

> **Ambiente · Mapeo de Stakeholders (Stakeholder Wheel):** *"…identificar y
> mapear **los stakeholders** críticos…"* — el anglicismo está hasta en el
> título del nodo.

> **Exportación · Evaluación de la Preparación de la Empresa:** *"…si **la
> gerencia** necesita justificar la inversión en exportación…"*

**Dato local cableado** — lo que cambia por país:

> **Seguridad y Personas · Programa de Seguridad y Salud Ocupacional:** *"marco
> flexible y proactivo propuesto por **OSHA**…"* — OSHA es el regulador de
> Estados Unidos. Para un emprendedor en otro país, el marco puede servir; el
> nombre del organismo, no.

**Matriz o puntaje** — contra la doctrina anti-matriz:

> **Seguridad y Personas · Caracterización y Priorización de Peligros:**
> *"**Matriz de riesgos priorizada** con peligros clasificados por severidad
> y…"* — este sí es una violación de la doctrina.

### Los dos falsos positivos, dichos

- **Exportación · Asistencia de la Agencia MBDA:** mi patrón cazó *"el
  **Departamento** de Comercio"*, que es un **nombre propio** del gobierno de
  Estados Unidos, no un supuesto de que el lector tenga departamentos. (Sí es,
  en cambio, un dato local de otro tipo, que el detector de datos locales no
  cubre: un recurso que solo existe en un país.)
- **Riesgos · Por Qué la Matriz de Riesgo No Funciona:** el nodo **argumenta
  contra** la matriz. Es la doctrina anti-matriz escrita, no su violación. Mi
  patrón solo vio la palabra.

**Lectura honesta del muestreo:** con 10 nodos por pack, esto detecta problemas
sistémicos, no mide su prevalencia. Que Calidad dé 0/10 no significa que esté
limpio de las tres barandas; significa que el problema no es tan denso como para
salir en una muestra de diez. La duplicación sí está medida sobre el 100%.

---

## 6. Verificación arquitectónica: qué ataría una cirugía

| Qué referencia ids | Cuántos | Atadura |
|---|---:|---|
| Aristas del grafo | 14.848 | Media. Borrar un nodo deja aristas rotas, y **el Gate 0 lo caza** |
| Índice semántico Voyage | 3.835 | **Blanda.** Se regenera entero, sin migración |
| Familias de readiness | 3.835 | **Blanda.** Se regenera gratis |
| Caché de preguntas | 3.558 | **Blanda.** `--patch-file` regenera solo lo tocado |
| Puentes core↔pack | 224 | Media. Bidireccionales, escritos en los nodos fuente |
| Semillas de packs | 65 | Media. Horneadas **a mano**: `integrar_packs` no las produce |
| Mapa de brecha | 48 | Media. A mano, fase → semilla |
| Semillas del núcleo | 20 | Media. Gate 0 exige alcance ≥ 99,5% desde aquí |
| **`project_nodes`** | **809 nodos distintos** | **DURA.** Es historia de usuarios reales; no se regenera |

### Veredicto arquitectónico

**Una limpieza sería deprecar-de-la-selección con reindex, no borrado.** Ocho de
las nueve ataduras se regeneran o las cubre el Gate 0. La única dura es
`project_nodes`: si un nodo visitado desaparece, la ruta histórica de un usuario
apunta al vacío y su expediente, su bitácora y su timeline quedan cojos.

El camino seguro es: marcar el nodo como no elegible (fuera de la selección y
del índice semántico), **conservar el archivo y su id**, redirigir sus aristas
al superviviente, y regenerar caché e índice. El Gate 0 valida el resultado sin
tocar la historia de nadie.

### Telemetría cruzada

Leída de `project_nodes` con **paginado** (4.463 filas). *Nota de método: un
`select` simple se corta en 1.000 filas sin avisar; con el corte este censo
reportaba 66 nodos visitados y el número real es 172. Un dato truncado que
parece completo es peor que no tenerlo.*

- **809** nodos distintos visitados alguna vez · **697** cosechados
- De los **486** nodos en clusters confirmados, **165 han sido visitados** y
  **152 cosechados**

**Un tercio de los duplicados ya vivió en el recorrido de alguien.** Eso no
bloquea la limpieza —el camino de deprecación conserva los ids— pero sí descarta
de plano cualquier borrado físico.

---

## 7. Recomendación por pack

La moneda cara no es la API: son **tus horas de poda**. La estimación asume que
te llego con los clusters ya agrupados y el veredicto del consolidador al lado, y
que tu decisión por cluster es elegir superviviente y qué se rescata del resto.

| Pack | Recomendación | Clusters | **Tus horas** | Por qué |
|---|---|---:|---:|---|
| **Calidad** | **SÍ, primero** | 66 | ~3,5 h | Peor tasa (17,4%) y el peor cluster del catálogo (7 nodos de COPQ). Máximo retorno por hora tuya |
| **Seguridad y Personas** | **SÍ** | 27 | ~1,5 h | 17,2%, y el foco está localizado: las dos guías OSHA son casi la mitad del problema |
| **Ambiente** | **PARCIAL** | 17 | ~1 h | 10,9% concentrado en un solo libro. Poda quirúrgica de *Green to Gold* |
| **Franquicias** | **PARCIAL** | 13 | ~45 min | 12,1% en un único libro fuente. Barato de cerrar |
| **Exportación** | **PARCIAL** | 7 | ~30 min | 9,5%. Vale más por sus datos locales (organismos de EE. UU.) que por su duplicación |
| **Seguridad Digital** | **NO** | 1 | ~5 min | 3,6%, un solo cluster. Está en la vara |
| **Riesgos** | **NO** | 1 | ~5 min | 3,6%, un cluster. El SOP v1.4 hizo su trabajo |
| **Compras · Entrega** | **NO** | 0 | — | Son el control. Están en la vara por construcción |
| **NÚCLEO** | **ver abajo** | 90 | ~5 h | Vara especial |

**Total si se hace todo lo recomendable menos el núcleo: ~7,25 horas tuyas.**

### El núcleo lleva vara especial

El censo dice 11,3% y 90 clusters, con cinco definiciones de *startup* y cinco de
*pivotar o proceder*. **Y aun así, para el núcleo el censo informa, no receta.**

El núcleo es el único pack **validado por meses de uso real**. De los 809 nodos
visitados en `project_nodes`, la enorme mayoría son suyos: esos duplicados no son
teoría, son piezas por las que ya pasó gente. Cinco definiciones de startup
pueden ser cinco nodos que sobran, o pueden ser cinco puertas por las que
entraron cinco personas distintas según cómo formularon su idea.

**El censo no puede distinguir esas dos cosas. La telemetría de beta sí.**

Mi recomendación para el núcleo: **esperar**. Los datos que faltan son cuáles de
esos 90 clusters tienen nodos que la gente visita de verdad y cuáles están
muertos. Un nodo duplicado que nadie pisa se depreca sin riesgo; uno duplicado
que es puerta de entrada frecuente merece quedarse aunque su gemelo diga lo
mismo. Ese corte se hace con la beta corriendo, no con este documento.

Si aun así quisieras avanzar antes, el subconjunto seguro son los clusters del
núcleo **cuyos nodos no aparecen en `project_nodes`**: duplicados que nadie ha
tocado nunca. Ese recorte está en los datos y puedo aislarlo cuando lo pidas.

---

## 8. Lo que este censo NO midió

Dicho para que no se lea de más:

- **Calidad de escritura.** El censo mide duplicación y tres barandas. No mide si
  un resumen está bien escrito, si los pasos son accionables o si el tono le
  habla a una persona sola más allá de los patrones detectados.
- **Prevalencia de las barandas.** Diez nodos por pack detectan problemas
  sistémicos; no miden cuánto hay. Un censo completo de las tres barandas sobre
  3.835 nodos es otro trabajo, y más caro.
- **Duplicación entre packs.** Deliberado: dos mundos pueden cubrir el mismo
  concepto a propósito, cada uno desde su oficio.
- **Si fundir mejora la experiencia.** El consolidador dice que dos nodos son el
  mismo concepto. Que al usuario le convenga ver uno en vez de dos es una
  decisión de producto, y es tuya.

---

*Datos crudos: `docs/_censo_duplicacion.json` (censo completo),
`docs/_censo_muestras.json` (los diez peores clusters por pack con veredicto),
`docs/_censo_fuentes.json` (granularidad por libro).*
