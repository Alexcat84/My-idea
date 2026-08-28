# VUELTA 101, TAREA 3: LA FASE 0 CONTRA LA EVIDENCIA REAL (medicion, sin tocar `estado`)

Responde la pregunta que la propia caida del auditor abrio (acta de la vuelta
100, seccion 7.3/7.4): de `OP-C-01`, `OP-C-02`, `OP-C-03`, `OP-C-04`,
`OP-S-06`, `OP-S-07` (las seis que la TAREA 6 de la vuelta 100 marco
bloqueantes de `OP-E-03`), el auditor dejo CUATRO "A VERIFICAR, sin medicion
propia". NADA de esto toca `estado`, no abre fase 05 ni 06, no mueve ninguna
operacion de fase.

## LAS TRES SEDES, POR OPERACION

| operacion | (a) pagina + nota `OPERACIONES.jsonl` | (b) `ACTA_AUDITOR.md` | (c) commit en la rama |
|---|---|---|---|
| `OP-C-01` | `docs/plan/FASE_0_CODIGO.md:27` (no `00_CODIGO.md`, nunca existio), sin frase de cierre; nota propia describe el arreglo pendiente | sin registro de cierre (confirmado por el auditor, 7.4: "A VERIFICAR") | **`8b2ba536`, 2026-08-14, "FASE 0, OP-C-01 EJECUTADA: los tres sitios de fuera resuelven antes de leer"** |
| `OP-C-02` | `docs/plan/FASE_0_CODIGO.md:59`, sin frase de cierre | sin registro de cierre | **`41a9c570`, 2026-08-14, "FASE 0, OP-C-02 EJECUTADA: los dos que CALLABAN dejan de callar"** |
| `OP-C-03` | `docs/plan/FASE_0_CODIGO.md:85`, sin frase de cierre | sin registro de cierre | **`1578e641`, 2026-08-14, "FASE 0, OP-C-03 EJECUTADA: los que ROMPEN dejan de romper"** |
| `OP-C-04` | `docs/plan/FASE_0_CODIGO.md:109`, sin frase de cierre | **`ACTA_AUDITOR.md:5056`, acta de la vuelta 25, "la fase 0 cerrada (`OP-S-07` y `OP-C-04`)"** | (no buscado: ya cerrado por (b)) |
| `OP-S-06` | `docs/plan/05_SANEO.md:217`, sin frase de cierre | sin registro de cierre | **`a1c39585`, 2026-08-14, "FASE 0, OP-S-06 EJECUTADA: los campos sucios del esquema, sin perder un dato"**; ademas `9707a67d` (mismo dia, "el ciclo del Gate 0 es PUNTO FIJO contra el HEAD nuevo") |
| `OP-S-07` | `docs/plan/05_SANEO.md:248`, sin frase de cierre | **`ACTA_AUDITOR.md:5056`** (idem `OP-C-04`) | (no buscado: ya cerrado por (b)) |

**LAS CUATRO QUE EL AUDITOR DEJO "A VERIFICAR" (`OP-C-01`, `OP-C-02`,
`OP-C-03`, `OP-S-06`) SI TIENEN REGISTRO DE CIERRE ESCRITO: vive en la
SEDE (c), el mensaje del commit, la unica de las tres sedes que el criterio
de la TAREA 6 de la vuelta 100 no miraba.** Los cuatro commits son del mismo
dia (14 ago 2026) y estan en `pasada-unica` (`git branch --contains`,
confirmado hoy).

## LA VARA DEL CODIGO VIVO (3.2), CADA UNA CON SU CITA DE HOY

- **`OP-C-01`** (tres arreglos): `web/lib/engine/planRedactor.ts:65`
  `const real = resolverId(nid, graph) ?? nid;` dentro de `aMaterial`;
  `web/app/api/organizer/route.ts:67` y `.../stream/route.ts:88`, los dos
  `cargarEntrySeeds(graph)` con comentario propio `// OP-C-01: CON el
  grafo...`; `web/lib/compass.ts:171` resuelve el id ANTES del filtro
  `esOfrecible`, con el hueco al reves ya retirado (comentario: "el
  `opts.graph[id] &&` que estaba aqui era el unico HUECO AL REVES"). **LAS
  TRES CORREN HOY.**
- **`OP-C-02`** (dos silenciosos): `web/lib/engine/graph.ts:194`
  (`conceptosDeRuta`, ya NO filtra por `nid in graph`, resuelve titulo) y
  `:206` (`faseDeNodo`, resuelve antes de caer al defecto `"ideacion"`), los
  dos con comentario propio `// OP-C-02`. Llamadas reales en
  `web/app/api/session/[id]/plan/route.ts:265` y `:403`. **LAS DOS CORREN
  HOY.**
- **`OP-C-03`** (los seis restantes): `graph.ts:302` (`resumenNodo`,
  resuelve); `graph.ts:279` (`preguntaDeNodo`, con comentario `// OP-C-03`),
  usada en `web/lib/engine/recorrido.ts:271` y `:649` (las dos lineas EXACTAS
  que la pagina cita); `clasificar.ts` recibe `entrySeeds` ya filtrados por
  `cargarEntrySeeds(graph)` (`session/start/route.ts:100`, la puerta unica de
  `OP-C-01`); `web/app/api/project/[id]/world/[pack]/start/route.ts:154`
  `resolverId(brecha.semillaId, graph)` reemplaza el chequeo literal. **LAS
  CUATRO CORREN HOY.**
- **`OP-C-04`** (ya medido por el auditor, confirmado hoy): Gate 0 de esta
  vuelta (`docs/loop/SALIDA_V101_GATE0_CMD1_APERTURA.txt`) imprime las dos
  guardas en verde: `[OK] Ningun nodo VIVO se cita a si mismo tras RESOLVER
  ... 0 auto-aristas` y `[OK] Ninguna clave de nodo fuera de la lista blanca
  del esquema ... 0 renegadas`. **CORRE HOY.**
- **`OP-S-06`** (campos sucios): los seis nodos de la tabla
  (`crosby_habilidad_transmision`, `mapa_flujo_trabajo_cliente`,
  `arquetipos_de_cliente`, `composicion_board_directors`,
  `definicion_startup`, `preferencia_de_liquidacion`), leidos hoy de
  `dataset/metadata/master_graph.json`: CERO tienen `fase_проekto`,
  `fase_project` ni `fuentes_adicionales`; los cuatro con `fuentes_adicionales`
  tienen su contenido migrado al campo `fuente`. **LA REPARACION ESTA
  APLICADA EN EL DATO DE HOY.**
- **`OP-S-07`** (auto-aristas): `analisis_flujo_de_valor` (el ejemplar de la
  pagina), leido hoy: `nodos_previos` ya NO trae `value_stream_analysis_lean`,
  que sigue en `ids_alias` (el alias se conserva, la arista se retiro, tal
  como ordena la operacion). **APLICADA EN EL DATO DE HOY.**

## 3.3: LA CUENTA

**BAJO LA SEDE (c) MAS LA VARA DEL CODIGO VIVO, LAS SEIS CAEN: CERO
BLOQUEANTES REALES.** Los seis registros de cierre viven en commits
(`OP-C-01/02/03/S-06`) o en acta (`OP-C-04/S-07`), y las seis reparaciones
corren o estan aplicadas hoy, medidas directamente contra el codigo y el
dato, no contra la pagina.

De las 10 operaciones de la fase 04 (tabla de la TAREA 6 de la vuelta 100),
la UNICA bloqueada exclusivamente por estas seis es `OP-E-03` (sus 6
bloqueantes son exactamente estas seis). Las otras siete bloqueadas
(`OP-M-03-ENLACES`, `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES`,
`OP-M-01-SEXTO`, `OP-E-06`, `OP-E-07`) dependen de `OP-M-01`,
`OP-M-01-FUSION`, `OP-M-03`, `OP-M-03-III`: las CUATRO mesas de la fase 06,
que esta TAREA no mide ni toca.

**SI SE ACEPTA LA SEDE (c) Y LA VARA DEL CODIGO VIVO COMO EVIDENCIA DE
CIERRE, LA CUENTA DE LA FASE 04 CAMBIA DE "1 HECHA, 1 EJECUTABLE, 8
BLOQUEADAS" A "1 HECHA (`OP-E-02`), 2 EJECUTABLE (`OP-E-01`, `OP-E-03`), 7
BLOQUEADAS", Y LA FASE 04 DEJARIA DE ESTAR BLOQUEADA POR CODIGO: SOLO
SEGUIRIA BLOQUEADA POR LAS MESAS DE LA FASE 06.**

**ESTO SE DECLARA Y SE PARA AQUI, SIN RESOLVERLO**: aceptar un commit sin
frase de cierre en la pagina o en el acta como "registro de cierre escrito"
es una decision de CRITERIO DE EVIDENCIA (que sede cuenta y cual no), no una
medicion. Es pregunta de orden de campana para el auditor o el fundador. No
se abre la fase 05 ni la 06, no se mueve ninguna operacion de fase, no se
escribe ninguna arista ni se toca `docs/plan/` ni `estado` por esta TAREA.
