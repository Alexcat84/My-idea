# SELLO DE LA SESION CON CREDENCIAL (3 sep 2026)

**Decision del fundador del 3 sep 2026. Rama `pasada-unica`, bucle DETENIDO,
`.env` presente en la raiz para esta sesion (gitignored, linea 1 de `.gitignore`).**

Objetivo: cerrar el muro de la fase 08. Este fichero sella lo corrido, con su
salida, punto por punto de la verificacion transversal.

## LA VARA, CITADA POR SU LINEA

- **`docs/plan/08_VERIFICACION.md` lineas 60 a 64**, la verificacion transversal y
  su orden: **1** Gate 0 verde, **2** suite verde, **3** vuelo completo, **4**
  prueba de rumbos, **5** reindexado semantico.
- **El criterio de HECHO**, citado por el acta 149: *"UNA FASE ESTA HECHA CUANDO
  SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA. No cuando pasa verde: cuando se
  CAERIA."*
- **`docs/loop/ACTA_AUDITOR.md` linea 50182, acta 149 seccion 3.10**: la fase 08
  queda abierta hasta la sesion con credencial, porque **una verificacion que no
  se puede correr no se puede caer**.
- **`docs/loop/ACTA_AUDITOR.md` linea 50195, acta 149 seccion 3.11**: el
  reindexado ES el punto 5, y una corrida completa mete los 18 y saca los 370 en
  la misma pasada.

## LOS CINCO PUNTOS

### Punto 1, GATE 0 VERDE. **VERDE.** No pedia credencial.

**El ciclo ENTERO y en orden**, que es el criterio escrito (no la invocacion a
secas del validador):

| # | comando | resultado |
|---:|---|---|
| 1 | `python scripts/run_phase1.py --reaplico-curaduria` | **EXITCODE 0**, `GATE 0: OK` |
| 2 | `python scripts/etiquetas_de_cara.py --aplicar` | `master_graph.json` **byte identico a HEAD**, blob `cb33552a` |
| 3 | `python scripts/sync_assets_web.py` | las **dos copias** con el mismo blob `cb33552a` que HEAD |
| 4 | `git diff --numstat -- dataset/ web/ engine/` | **SIN FILAS** |

**Comprobaciones: 26 de 26 en `[OK]`, 0 en `[FALLO]`**, contadas de una corrida
limpia con el ciclo cerrado.

### Punto 2, SUITE VERDE. **VERDE.** No pedia credencial.

- **Motor:** `python engine/run_all_tests.py`, **25/25**, exitcode 0.
- **Web:** `npx vitest run`, **80 ficheros (80) y 1.033 pasadas (1.033)**.
- **`tsc`:** `npx tsc --noEmit`, **exitcode 0**, cero lineas.

### Punto 3, VUELO COMPLETO. **NO CORRIDO. ES LO UNICO QUE QUEDA ABIERTO.**

**No es un rojo del catalogo ni del codigo: es que faltan dos variables y el acto
esta reservado.** Medido hoy, no supuesto:

- El vuelo (`web/scripts/vuelo.ts`, linea 49) exige **`NEXT_PUBLIC_SUPABASE_URL`**
  y, por `@supabase/ssr`, **`NEXT_PUBLIC_SUPABASE_ANON_KEY`**.
- El `.env` de esta sesion trae los valores pero **con otro nombre**:
  `SUPABASE_URL`, `SUPABASE_ANON_KEY` y `SUPABASE_SERVICE_ROLE_KEY`.
- **`web/.env.local` NO EXISTE** (comprobado en disco, no por patron de ignore).
- El vuelo **escribe en la base real** (`sessions`, `projects`, `project_nodes`,
  `plans`, `project_bitacora`) y **gasta credito de Anthropic** en una entrevista
  completa mas el plan por streaming.
- Y la casa **ya lo reservo por escrito**:
  `docs/FASE_3_3_y_3_5_BACKEND_MUNDOS.md` linea 52 dice *"**YO** (avisame): correr
  el vuelo completo"*.

**Por eso se para y se trae, en vez de fabricarle un fichero de credenciales y
apuntarlo a la base de produccion por cuenta propia.**

### Punto 4, PRUEBA DE RUMBOS. **VERDE.** Pedia credencial y hoy corrio.

`python scripts/rumbos/prueba_rumbos.py`, **EXITCODE 0**.

> **MARCADOR: 42 verdes, 1 ambares, 0 rojos (97,7% verde de 43 en la vara)**
> **Sin deriva contra la linea base (97,7% verde).**
> Costo: 929 tokens de consulta.

Es la que el auditor de la vuelta 149 **no pudo correr** y que fallaba visible con
`exitcode 2` y *"ERROR: falta VOYAGE_API_KEY en .env"*. **Hoy corre y pasa.**

### Punto 5, REINDEXADO SEMANTICO. **VERDE.** Pedia credencial y hoy corrio.

`python scripts/build_semantic_index_voyage.py`. 3.169 nodos con `voyage-4-lite`
dim 512, siete lotes, ~532.646 tokens.

| medida | antes | despues |
|---|---:|---:|
| ids en el indice | 3.521 | **3.169** |
| vivos sin vector | **18** | **0** |
| deprecados en el indice | **370** | **0** |
| fantasmas | 0 | **0** |

**Cuadra por los dos lados:** indice == vivos (3.169 == 3.169) y vivos +
deprecados == censo (3.169 + 684 == 3.853). Sello del indice: de 24.282.332 bytes
`sha256 d70adc1d` a **21.854.994 bytes `sha256 42223fcc`**.

## LO QUE QUEDA, EN UNA LINEA

**Cuatro de los cinco puntos verdes y sellados. El punto 3 sin correr.** Por el
criterio de la propia pagina, **la fase 08 NO se declara cerrada hoy**: una
verificacion que no se ha corrido no se puede caer, que es exactamente el
razonamiento con el que el acta 149 la dejo abierta.

**El `.env` se queda en la raiz** hasta que el fundador diga lo contrario.
