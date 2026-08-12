# FASE 0: PRERREQUISITOS DE CODIGO

**Primera de todas, y el motivo es de secuencia, no de importancia.**

> **LA PASADA UNICA ES LO QUE MUEVE IDS.** Renombra, deprecia y funde. **Todo
> camino del runtime que resuelva un id a pelo se rompe o se calla el dia que la
> pasada empiece**, y se rompe con el usuario dentro.

**Operaciones: `OP-C-01` a `OP-C-04`. LAS CUATRO LISTAS.** Bloquean a `OP-S-01`,
`OP-S-09` y `OP-F-01`, o sea **a todo lo que mueve un id**.

---

## LA REGLA DE VERIFICACION DE ESTA FASE: EL CASO POSITIVO

> **Una prueba que hoy pase en verde no sirve.** Si pasa antes del arreglo, no
> esta probando el arreglo: esta probando otra cosa.
>
> **LA PRUEBA TIENE QUE CAERSE SI EL FALLO VUELVE.** Es el mismo criterio que
> `OP-S-07` fijo para la guarda de Gate 0, aplicado a las cuatro operaciones.

**Comprobacion barata de que una prueba de esta fase esta bien escrita: correrla
ANTES del arreglo. Si pasa, esta mal escrita.**

---

## `OP-C-01`: LOS TRES ARREGLOS QUE CUBREN CATORCE . **LISTA**

**Es el mas rentable de la fase: tres cambios cubren CATORCE de los veinte accesos
externos.**

| arreglo | donde | cubre |
|---|---|---:|
| resolver `nid` al entrar en `aMaterial` | `planRedactor.ts:53`, y sus dos llamadas en 183 y 194 | **3** |
| llamar `cargarEntrySeeds(graph)` | `organizer/route.ts:66,67,68` y `organizer/stream/route.ts:87,88,89` | **6** |
| resolver antes de puntuar en `compass` | `compass.ts:153`, y las tres que hereda en `interprete.ts:331,332,333` | **4** |

> **El segundo no escribe codigo nuevo: usa el que ya hay.** `cargarEntrySeeds`
> **ya filtra por `esOfrecible` cuando recibe el grafo**; los dos organizer la
> llaman sin pasarselo. **Es un argumento que falta, no una funcion que falte.**

**EL HUECO AL REVES, y es unico en el inventario.** `compass.ts:153` dice
`if (opts.graph && opts.graph[id] && !esOfrecible(...)) continue;`. **Si
`opts.graph[id]` es `undefined`, la condicion entera es falsa y el `continue` NO
se ejecuta: el id desconocido PASA el filtro.** La guarda esta escrita de forma
que **lo raro sobrevive**.

**CASOS POSITIVOS:**

1. **`aMaterial`**: una ruta con un id **deprecado con alias vivo** produce un
   plan completo. **Hoy la prueba se cae.** Y si manana alguien quita el
   resolutor, **vuelve a caerse**.
2. **organizer**: un seed deprecado en el fixture **no llega a la respuesta**.
   **Hoy llega.**
3. **`compass`**: un id que ya no es nodo **no se ofrece**. **Hoy si se ofrece.**

---

## `OP-C-02`: LOS DOS SILENCIOSOS . **LISTA**

**Los dos mas caros del inventario, y no porque rompan: porque CALLAN.**

| sitio | que hace hoy | que ve el usuario |
|---|---|---|
| `session/plan:267` | filtra con `nid in graph` | **su plan sale con menos conceptos**, sin aviso |
| `session/plan:405` | `?.` con fallback a `ideacion` | **su proyecto retrocede de fase**, sin aviso |

> **Ninguno lanza un error. Ninguno aparece en una prueba verde. Y los dos
> degradan lo que el usuario ve.** Son exactamente el modo de fallo que el canon
> de fallar ruidoso prohibe: **la degradacion silenciosa no deja sintoma.**

**EL ARREGLO ES EL MISMO EN LOS DOS: RESOLVER en vez de filtrar o de caer al
fallback.**

**CASOS POSITIVOS:**

1. **267**: una sesion cuya ruta contiene un id historico con alias vivo produce
   un plan con **todos** sus conceptos. **La prueba compara el numero de conceptos
   contra el largo de la ruta, y hoy no cuadra.**
2. **405**: un proyecto cuyo ultimo nodo es historico termina en **su** fase.
   **La prueba fija la fase esperada, y hoy recibe `ideacion`.**

---

## `OP-C-03`: LOS SEIS RESTANTES . **LISTA**

| sitio | arreglo |
|---|---|
| `graph.ts:244`, `resumenNodo` | resolver al entrar, **como ya hacen `etiquetaArbol` y `tituloDeNodo` dos funciones mas arriba** |
| `recorrido.ts:271` y `:649` | resolver antes de `obtenerPregunta` |
| `clasificar.ts:34,35,36` | recibir los seeds **ya pasados por la puerta unica** |
| `start/route.ts:255` | cambiar la comprobacion de la linea 149: de *esta en el grafo* a *resuelve* |

> **`resumenNodo` es el caso que mas llama la atencion: esta en el MISMO fichero
> que el resolutor, dos funciones mas abajo que sus dos consumidores, y no lo
> usa.**

> **Y `start/route.ts` es el unico de los veinte que YA esta guardado**, con un
> `console.warn` en la 149. **El arreglo no le anade una guarda: le cambia el
> criterio.** Hoy una semilla renombrada **mata el arranque del mundo que el
> usuario acaba de pagar**, cuando podria resolver y seguir.

**CASOS POSITIVOS**: pedir el resumen de un id historico (hoy `TypeError`);
reanudar una sesion cuyo nodo actual es historico (hoy rompe al pedir la
pregunta); arrancar un mundo cuya semilla fue renombrada (hoy avisa y aborta).

---

## `OP-C-04`: LA GUARDA DE GATE 0 QUE RESUELVE . **LISTA**

**Es la que hace PERMANENTES a `OP-S-07` y `OP-S-06`.** Sin ella, la reparacion de
las 27 auto-aristas **dura hasta la proxima integracion**.

| guarda | que comprueba |
|---|---|
| **auto-arista CON RESOLUCION** | cada id de `nodos_previos` y `nodos_siguientes` **se pasa por el resolutor** y se compara con el id del propio nodo |
| **lista blanca de claves** | ninguna clave desconocida en un nodo: es lo que impide que vuelva `fase_proekto` |

> **LA GUARDA DEBE RESOLVER, NO COMPARAR.** Un chequeo literal **da CERO sobre un
> grafo con VEINTISIETE**, porque ninguna de las 33 es directa. **Una guarda asi
> pasaria verde el dia de la reparacion y seguiria verde si manana vuelve a entrar
> una: es una guarda que no guarda.**

**CASOS POSITIVOS:**

1. **reinyectar** el enlace de `analisis_flujo_de_valor` a
   `value_stream_analysis_lean` y comprobar que **Gate 0 se cae**. Una guarda
   literal pasaria verde.
2. **anadir** a un nodo de prueba una clave `fase_proekto` con letras cirilicas y
   comprobar que **Gate 0 se cae**.

---

## LO QUE ESTA FASE LE DEJA A LAS DEMAS

> **Permiso para mover ids.** Sin ella, cada renombre de `OP-S-09`, cada
> deprecacion de `OP-S-01` y cada fusion de la fase 03 **puede dejar a un usuario
> mirando un id crudo, o peor, un plan mas corto sin saber por que.**
