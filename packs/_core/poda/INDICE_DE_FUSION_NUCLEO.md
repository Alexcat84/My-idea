# FASE 2 — El índice de fusión del núcleo (SOLO PROPUESTA)

Cero fusión, cero cambio a nodos. Lo único que se gastó en API son los
veredictos del consolidador: **$0.20**, anotados en el libro mayor.

El índice completo, máquina a máquina, en `_clusters_nucleo.json`. Esto es su
lectura.

---

## Los números de partida

| | |
|---|---:|
| núcleo activo | **1.721** |
| clusters a 0,90 | **93** (el encargo decía ~90) |
| nodos implicados | **200** (11,6% del núcleo) |
| telemetría real | **4.463 visitas** sobre 809 nodos |
| clusters con alguna visita real | **45 de 93** |
| veredicto del consolidador: fundir | **89** |
| veredicto: son distintos | **4** |

Los 93 no son una lista plana. Por etapa, los que el consolidador propone
fundir: **ejecución 38, validación 19, planificación 17, ideación 15**.

---

## (a) LA CAUTELA DE PUERTAS — y un hallazgo que la justifica entera

De los 93 clusters, **solo 3 tocan una puerta**, y los tres de la misma forma:
contienen **una semilla de entrada y un nodo que no lo es**. **Cero clusters
contienen una cabeza de rama.**

Así que la sospecha de "cinco textos parecidos son cinco puertas distintas"
**no se materializa en el núcleo**: no hay ni un cluster de puertas. Lo digo con
los datos delante en vez de repetir la sospecha.

**Pero el chequeo encontró otra cosa, y es más peligrosa.**

| cluster | semilla (visitas) | el otro (visitas) | a quién elegiría la regla de telemetría |
|---|---|---|---|
| 11 | `analisis_flujo_de_valor` (**0**) | `value_stream_analysis_lean` (**1**) | **`value_stream_analysis_lean` — MATARÍA LA SEMILLA** |
| 31 | `cuatro_etapas_del_pensamiento_creativo` (1) | `wallas_cuatro_etapas_pensamiento_creativo` (0) | la semilla, ok |
| 78 | `metricas_accionables` (**42**) | `vanity_metrics_vs_accionables` (25) | la semilla, ok |

**La regla vigente de superviviente es "más historia gana".** En el cluster 11
eso significa que **una visita contra cero** decidiría deprecar una puerta de
entrada del recorrido. El Gate 0 lo cazaría después ("ninguna semilla
deprecada"), pero eso es el paracaídas, no el diseño.

> **Propongo una precedencia nueva, y no la aplico solo: la semilla gana
> siempre. Una puerta no compite en telemetría con un nodo interior, porque el
> número de visitas de un nodo interior mide otra cosa.**

Con esa precedencia, los tres clusters de puerta se pueden fundir sin riesgo: la
semilla sobrevive y hereda las condiciones de activación del absorbido, que es
justo lo que la cautela quería proteger.

**Los tres marcados por mí como listos, con su evidencia arriba.** Ninguno es
CONSERVAR: no son puertas distintas, son una puerta y su duplicado.

### Los 4 que el consolidador dice que NO son el mismo

Van al índice como CONSERVAR de entrada. No los propongo.

---

## (b) LAS FAMILIAS GORDAS — tres de tres, como estaba previsto

El umbral vuelve a dejarlas sin agrupar. Buscadas por vecindad desde una semilla
en vez de por el umbral:

### `definición de startup` — 6 nodos, **1 suelto**
```
1.000  [cluster]  Definición de Startup
0.915  [cluster]  Definición de Startup bajo Incertidumbre Extrema
0.906  [cluster]  Definición de Startup: Búsqueda vs. Ejecución
0.865  [cluster]  Búsqueda vs. Ejecución: Definición de Startup
0.840  [cluster]  La Startup como Organización Temporal en Búsqueda de un Modelo
0.815  [SUELTO]   Búsqueda de un Modelo de Negocio (Search)
```
La más contenida de las tres: el cluster ya recogió 5 de 6.

### `pivotar o proceder` — 4 nodos, **2 sueltos**
```
1.000  [cluster]  Tipos de Pivote (Zoom-in, Segmento de Cliente, Plataforma)
0.909  [cluster]  Catálogo de Tipos de Pivote
0.848  [SUELTO]   Pivot (Pivote)
0.802  [SUELTO]   Reempaquetado del Producto (Estrategia de Pivote)
```

### `validación con clientes` — 8 nodos, **6 sueltos** ← la peor
```
1.000  [SUELTO]   Customer Discovery: Salir del Edificio
0.882  [SUELTO]   No Hay Hechos Dentro del Edificio: Sal a Buscarlos
0.878  [SUELTO]   Get Out of the Building (Salir del Edificio)
0.865  [SUELTO]   Customer Discovery
0.843  [SUELTO]   Introducción al Customer Discovery
0.841  [SUELTO]   Proceso de Customer Development
0.834  [cluster]  Proceso de Customer Discovery (Cuatro Fases)
0.800  [cluster]  Las Cuatro Fases del Customer Discovery
```

**Seis nodos que dicen "sal del edificio" y el umbral solo agrupó dos.** Es la
familia más gorda del núcleo y la que el índice ve peor, porque cada libro le
puso su nombre y el parecido de superficie se diluye entre seis variantes.

Y no es una coincidencia que sea **la misma familia donde vive el blanco del
primer rumbo de diagnóstico**. Ver (d).

---

## (c) LOS 171 HALLAZGOS DEL NÚCLEO, POR CLASE

| clase | nodos | dentro de un cluster |
|---|---:|---:|
| `residuo_corporativo` | **143** | 8 |
| `matriz_o_puntaje` | **21** | 3 |
| `dato_local_cableado` | **10** | 1 |
| **total** | **171** (9,9%) | **12** |

**Solo 12 de los 171 se evaporan al fundir.** Los otros **159 son trabajo de
re-voz que la fusión no toca.**

---

## (d) EL PUENTE CON LOS 5 RUMBOS DE DIAGNÓSTICO

Esto es lo que hace medible la fase, y **el resultado no es el que esperábamos.**

| rumbo | nodo que debería ganar | ¿entre los 171? | ¿en un cluster? |
|---|---|---|---|
| los ahorros | `customer_discovery_get_out_of_building` · `diseno_experimentos_hipotesis` | **NO** · **NO** | no · no |
| "nadie me ha pagado" | `get_out_building_test_sell` | **NO** | no |
| "le sirve a todo el mundo" | `customer_segments_hypothesis` · `segmentos_de_clientes_problema_necesidad` | **NO** · **NO** | no · no |
| "por qué me comprarían a mí" | `value_proposition_startup` | **NO** | no |
| "sacar algo pequeño" | `construir_mvp_baja_fidelidad` · `concierge_mvp` | **NO** · **NO** | no · **sí (cl. 4)** |

**Ninguno de los ocho blancos está entre los 171. Uno solo está en un cluster.**

Si la Fase 3 se limitara a fundir los 93 clusters y re-vozar los 171, **los cinco
rumbos de diagnóstico seguirían ámbar**, porque no tocaría ni uno de sus blancos.

### Entonces, ¿qué tienen esos nodos?

Los leí. Están escritos en **tercera persona de libro de texto y con jerga sin
traducir** — que no es lo que miden las barandas:

| blanco | voz | jerga |
|---|---|---|
| `customer_discovery_get_out_of_building` | *"los fundadores"* | *Customer Discovery* |
| `diseno_experimentos_hipotesis` | *"los fundadores deben"* | — |
| `get_out_building_test_sell` | *"es la fase donde el fundador sale"* | *earlyvangelists*, *pass/fail* |
| `customer_segments_hypothesis` | *"el equipo debe formular"* | — |
| `segmentos_de_clientes_problema_necesidad` | *"se debe entender"* | — |
| `concierge_mvp` | *"el equipo fundador entrega"* | — |
| `construir_mvp_baja_fidelidad` | — | *landing page* |
| `value_proposition_startup` | *"el trabajo que se realiza"* | *(job)* |

**Siete de los ocho los caza un detector de voz-de-libro; cero los cazan las
barandas.** El octavo, `value_proposition_startup`, también lo es leyéndolo
(*"describe el trabajo (job) que se realiza para el cliente"*); mi detector
rápido no lo alcanzó, y por eso las cifras de abajo son un **piso, no un techo**.

### La medida de la clase nueva, sobre los 1.721

| lo que se mide | nodos | % |
|---|---:|---:|
| barandas (**escala corporativa**) | 171 | 9,9% |
| **voz de libro** (tercera persona / impersonal) | **349** | **20,3%** |
| **jerga sin traducir** (inglés crudo) | **177** | **10,3%** |
| **unión: algo que arreglar** | **599** | **34,8%** |

**Las barandas solas se pierden 428 nodos.** De la unión, 81 están dentro de un
cluster.

> Las barandas se construyeron para los packs, donde el defecto era la **escala**
> (una empresa con gerencia y comités hablándole a alguien que trabaja solo). El
> defecto del núcleo es otro: **la persona**. El núcleo no le habla a una empresa
> grande, le habla **sobre** un emprendedor en vez de **a** un emprendedor. Es un
> defecto distinto, y las barandas no lo ven.

**La prueba de fuego de la Fase 3 tiene ahora su blanco exacto**, y es más grande
que los 171: si la Fase 3 re-voza los 599 (o el subconjunto que se adjudique
empezando por los 8 blancos y su familia de validación), los cinco rumbos de
diagnóstico son la medida de si funcionó. Si se re-vozan solo los 171, no se
mueven.

---

## Lo que traigo para adjudicar

1. **La precedencia de superviviente**: ¿la semilla gana siempre sobre la
   telemetría? Sin eso, el cluster 11 deprecaría una puerta por una visita
   contra cero.
2. **Los 89 clusters a fundir**: ¿enteros, o por etapa en lotes?
3. **La clase nueva "voz de libro + jerga"**: ¿se adopta como cuarta baranda con
   su adjudicación, y con qué alcance — los 8 blancos, la familia de validación
   entera, o los 599?
4. **Las tres familias gordas**: los 9 sueltos (1 + 2 + 6), ¿entran al índice
   como clusters a mano?
