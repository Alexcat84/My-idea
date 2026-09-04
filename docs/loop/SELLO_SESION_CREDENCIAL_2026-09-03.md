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

---

## CIERRE POR ADICION (4 sep 2026, vuelta 165 del bucle, TAREA 5)

**NADA DE LO DE ARRIBA SE BORRA, Y LA ULTIMA LINEA DE LA SECCION ANTERIOR SE
QUEDA ENTERA.** Decia *"la fase 08 NO se declara cerrada hoy"* y **era cierta el
3 sep 2026**, cuando se escribio: el punto 3 no se habia corrido. Este fichero no
distinguia sus dos fechas, y esa es la enfermedad que la `CORRECCION 22` tiene
nombrada en otro sitio. Aqui se distingue por adicion y no por sustitucion, que
es como manda la casa.

**QUE PASO DESPUES, Y NO ES DE ESTE FICHERO SINO DEL DIA SIGUIENTE.** El commit
**`e966d896`** (4 sep 2026, 08:10:33 menos 0400), asunto *"LA FASE 08 QUEDA
CERRADA: el vuelo completo en 16 de 16 con exitcode 0, y los cinco puntos de su
verificacion transversal sellados"*, **corre el punto 3 y cierra la fase**. La
ficha `OP-V-01` de `docs/plan/OPERACIONES.jsonl` pasa a `HECHA`. **El vuelo se
cayo DIEZ VECES antes de pasar**, que es lo que el criterio de HECHO pedia: una
verificacion que se caeria si el fallo volviera.

**LAS DOS FRASES SON CIERTAS, CADA UNA CON SU FECHA:**

| fecha | frase | por que era cierta |
|---|---|---|
| **3 sep 2026** | *"la fase 08 NO se declara cerrada hoy"* | el punto 3 no se habia corrido, y una verificacion que no se corre no se puede caer |
| **4 sep 2026** | la fase 08 **queda cerrada** | el punto 3 corrio, **16 de 16 con exitcode 0**, y los cinco puntos quedaron sellados |

**LO QUE EL BUCLE MIDE DE ESTO CON SU PROPIO COMANDO, Y NO COPIA DEL COMMIT**
(salida `docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`, corrida el 4 sep 2026 en la
vuelta 165):

| medida | comando del ejecutor | medido hoy | **contraste, y solo contraste** |
|---|---|---:|---|
| suites de la web | `pnpm test` en `web/` | **82 ficheros (82) y 1.040 pasadas (1.040)**, exitcode 0 | el commit del fundador dice 82 y 1.040; la cabecera de la vuelta 164 decia 80 y 1.030 |
| `tsc` | `npx tsc --noEmit -p tsconfig.json` en `web/` | **exitcode 0, CERO lineas de salida** | el commit del fundador dice exitcode 0 |
| `sha256` del indice semantico | `hashlib` byte a byte sobre la sede que `sync_assets_web.py` declara | **`42223fccc725103e861b40e7681afff135267c5c6c4761c8e13dac4fc076d8fd`**, 21.854.994 bytes | el sello de arriba publica `42223fcc` |

> **La sede del indice no se supone: se lee del propio `sync_assets_web.py`**
> (`DEST = BASE / "web" / "lib" / "assets"`), y **hay UNA sola en disco**. Las
> otras dos rutas que se comprobaron, `dataset/metadata/` y `engine/`, **NO
> EXISTEN**.

**Y UNA CIFRA DE ESTE MISMO FICHERO QUE EL AUDITOR CORRIGIO EN LA 164 Y QUE AQUI
QUEDA ANOTADA:** el cotejo byte a byte de los assets es de **SEIS**, no de cinco.
Cuatro actas arrastraron *"los cinco `sha256`"* y el manifest lleva **seis
claves**. Corrido por el auditor el 4 sep 2026: **6 cotejados, 6 cuadran, 0 no
cuadran.**

**EL `.env` NO SE TOCA Y ESTA ADICION NO LO MUEVE.** Lo que dice la ultima linea
de la seccion anterior sobre el `.env` sigue vigente: se queda en la raiz hasta
que el fundador diga lo contrario.
