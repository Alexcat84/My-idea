# PARA ALEXIS: EL BUCLE SE DETIENE EN LA PRIMERA OPERACION DE LA FASE 05

**Fecha:** 28 ago 2026 (leida de git). **Escrito por:** el auditor (Opus 5), acta de la
vuelta 118, `docs/loop/ACTA_AUDITOR.md` linea 41020.

## 1. EL MOTIVO, EN UN PARRAFO

La fase 04 quedo cerrada con remision y la fase 05 se abrio. Su primera operacion, `OP-S-01`
(FUSION de `nafta_free_trade_agreements` dentro de
`certificado_de_origen_tratados_libre_comercio`), **ya tiene su acto material hecho**: la fase 03
lo hizo en la vuelta 57 (commit `a1d7269d`, 20 ago 2026), y lo verifique hoy con `git log -S`
sobre los dos ficheros de nodo. De sus **siete puntos de verificacion**, medidos hoy uno por uno
contra el grafo, **cinco CUMPLEN, uno es procedimental, y uno NO CUMPLE**: el punto 4 pide que
**ningun nodo VIVO lleve NAFTA en su id ni en su titulo**, y el titulo del superviviente sigue
diciendo *"Certificado de Origen y Tratados de Libre Comercio (NAFTA, Rules of Origin, RVC)"*.

**Y ningun texto de la casa dice que tiene que decir ese titulo.** Lo busque en los siete puntos,
en la `nota`, en la `adjudicacion`, en el `preservar` de la propia operacion, en las ordenes 1 a
5 de la ficha `vigencia-del-marco-internacional` de `docs/PENDIENTES.md`, en `BANCO_DEL_PLAN.md`
(P.1 a P.18: **cero apariciones de la palabra titulo**) y en `BANCO_DE_TEXTOS.md`. El ejecutor
midio, clasifico **PARCIALMENTE CUMPLIDA** y se detuvo sin tocar nada, que es exactamente lo que
`AUDITOR.md` seccion 3 manda: *"Una operacion cuyo texto no alcance para ejecutarse sin decidir
es PARADA, no una improvisacion"*. **Yo tampoco puedo adjudicarlo**, y por tres razones que se
disparan juntas (`AUDITOR.md` seccion 4): hace falta doctrina nueva, cualquiera de las dos
salidas choca con una regla vigente, y la decision cambia el alcance de la campaña.

## 2. LAS DOS SALIDAS, NOMBRADAS, Y NINGUNA ELEGIDA AQUI

**SALIDA A, LA BARATA: quitar el token.** El titulo pasaria a *"Certificado de Origen y Tratados
de Libre Comercio (Rules of Origin, RVC)"*. Satisface el punto 4 al pie de la letra y no inventa
redaccion. **Lo que rompe:** la doctrina fundacional de la ficha que ordena este trabajo dice
*"Las instituciones-de-libro jamas se omiten: se mantienen al dia"* y *"un catalogo que lo cite
desactualizado miente con precision"*. **Borrar es omitir**, y deja el catalogo mudo sobre el
tratado que si rige.

**SALIDA B, LA CARA: poner el sucesor.** NAFTA se extinguio el **1 de julio de 2020** y lo
sustituyo el **USMCA** (T-MEC en Mexico, CUSMA en Canada). Cumple la doctrina de la ficha, pero
**elige un nombre**, que es contenido de catalogo y voz de producto, o sea tuyo. Y si se elige,
la pregunta se extiende: hoy hay **cinco nodos vivos que nombran NAFTA y cero que nombren su
sustituto** (medido hoy sobre los 3.188 vivos): `certificado_de_origen_coo`,
`certificado_de_origen_tratados_libre_comercio`, `documentacion_exportacion`,
`regla_de_minimis`, `reglas_origen_sectoriales`.

**Y HAY UNA TERCERA COSA QUE DECIDIR, Y ES LA DE FONDO:** el barrido de NAFTA **no es dueño de
ninguna operacion del plan**. Lo medi sobre las 71 filas de `OPERACIONES.jsonl`: `OP-S-02` es
Incoterms (tres nodos), `OP-S-03` es `export.gov` (tres nodos, cuatro menciones), `OP-S-09` son
sufijos numericos y `OP-S-10` es franquicias. El barrido vive **solo** como entrada de ficha en
`PENDIENTES.md`. O sea que la pregunta no es solo que dice un titulo: es **si la campaña se hace
cargo del barrido de vigencia o lo deja anotado para despues**.

## 3. EL ESTADO EXACTO, MEDIDO POR MI HOY

| | |
|---|---|
| rama | `pasada-unica` (nunca se toco staging ni produccion) |
| HEAD | `d13be5c06394405842edde5f9c086238b8f04edc` |
| fase | **04 CERRADA CON REMISION**; **05 ABIERTA y DETENIDA en `OP-S-01`** |
| censo del grafo | 3.853 nodos / 3.188 vivos / 665 deprecados, `sha256=f0e399396745`, 8.391.653 bytes |
| aristas | `nodos_siguientes` 9.190, `nodos_previos` 9.169, suma 18.359, union 9.813, auto-aristas 0 |
| Gate 0 | **OK** (duplicadas 0, divergentes 0, auto-aristas tras resolver 0, alcanzabilidad 100,0% con 3188/3188 y 85 semillas) |
| suites | motor **25/25**, web **80 (80) / 1.030 pasadas y 3 saltadas**, `tsc` **EXIT 0 y cero lineas** |
| marcador del cribado | **A 551 / B 72 / C 5 / D 2.760, n 3.388**, cero huecos |
| operaciones | 71 filas, **LISTA 70 / HECHA 1**; el campo `estado` **no se movio** en toda la vuelta |
| movimiento del arbol | `dataset/`, `web/` y `engine/` con **CERO lineas** commit a commit sobre los once commits de la vuelta |

La `M` de `dataset/metadata/master_graph.json` en `git status` es la de siempre (fin de linea):
`git diff --numstat` sobre ese fichero da cero lineas. No la commitees y no la arregles.

## 4. LO QUE NECESITO DE TI, Y SON TRES RESPUESTAS CORTAS

1. **El titulo del superviviente**: salida A, salida B, o el texto exacto que quieras. Si es B,
   di **que nombre** (USMCA, T-MEC, CUSMA, o los tres entre parentesis).
2. **El barrido**: si los otros cuatro nodos vivos que nombran NAFTA entran a la campaña (y
   entonces hace falta una operacion nueva en el plan, con su texto), o si quedan anotados en la
   ficha y fuera de esta pasada.
3. **Si `OP-S-01` se declara CUMPLIDA CON REMISION** (su acto material lo consumio la fase 03, y
   el punto 4 se remite a donde tu decidas) **o queda bloqueada** hasta que se resuelva el 1.

## 5. LO QUE YA ADJUDIQUE, PARA QUE NO LO TENGAS QUE MIRAR TU

- **La fase 0 pasa su criterio de HECHO con `OP-C-01` a `OP-C-04` en verde hoy.** `OP-C-05` esta
  **diferida por su propia ficha**, que dice por escrito que *"esta guarda se enciende DESPUES
  del saneo final"* y que las duplicadas de hoy *"no es una regresion, es el estado conocido"*
  (935 medidas por mi hoy sobre 711 nodos). Exigirle verde literal ahora pondria la atadura 1 y
  la atadura 2 en contradiccion mutua. **No es parada.**
- **El caso positivo de `OP-C-04` no se re-corre cada vuelta**: el criterio pide que haya fallado
  una vez, y la evidencia de la vuelta 24 existe y dice lo que se le atribuye.
- **Correccion mia, con treinta vueltas de retraso**: mi acta 88 escribio que la via equivalente
  de `OP-C-05` *"la autoriza la ficha misma"*. **Es falso**: `FASE_0_CODIGO.md` no contiene las
  palabras "equivalente", "no crezca" ni "antes y despues". La via equivalente **es una
  adjudicacion mia por extension** y su cita correcta es el acta 88 seccion 5.4. La adjudicacion
  se sostiene; la atribucion se corrige.

## 6. EL ENCARGO DE CODIGO QUE ESPERA AL RELANZAMIENTO, Y ES DE UNA LINEA

**La via equivalente de `OP-C-05` tiene su caso positivo ROTO, y lo reproduje hoy.**
`scripts/loop/vuelta89_tarea4_guarda_op_c05.py --caso-rojo` se para siempre con *"ROJO: dataset/
ya tenia cambios antes del caso rojo"*, porque su guarda de limpieza mira `git status --porcelain
-- dataset/`, que **siempre** ve la `M` espuria de fin de linea. La fila 0 del plan dice *"Una
guarda que nunca fallo no esta probada"*: **una guarda cuyo caso positivo no puede correr esta en
ese mismo sitio**.

**El remedio:** que esa comprobacion mida contenido, con `git diff --numstat -- dataset/` (cero
lineas), en vez de estado, con `git status --porcelain`. Fichero nuevo, la guarda vieja no se
toca, y el caso rojo se corre y se pega antes de dar la fase 0 por probada. **Esto es lo primero
que debe hacer la vuelta 119**, antes de tocar `OP-S-01` o `OP-S-09`, que son las dos que mueven
ids y que la atadura 1 pone detras de la fase 0.

## 7. COMO RETOMAR

1. Contesta las tres preguntas de la seccion 4, aqui mismo o en un fichero de
   `docs/loop/paradas/` con el patron de siempre (`2026-08-28-titulo-nafta-ops01-DECISION.md`).
2. Escribe el encargo de la **vuelta 119** en `docs/loop/PROMPT_SIGUIENTE.md`, que ahora esta
   **vacio a proposito**. Si quieres, el orden natural es: **TAREA 1** el arreglo de la seccion 6
   con su caso rojo corrido, **TAREA 2** los registros de esta acta en `docs/PENDIENTES.md`, y
   **TAREA 3** `OP-S-01` con tu decision delante y despues `OP-S-02` en adelante.
3. El modelo del ejecutor sigue siendo el que fijo la decision del 26 ago (Sonnet 5 para el tramo
   mecanico); si la 119 vuelve a tocar redaccion de contenido, esa es tu llamada.
4. **El merge de `pasada-unica` sigue siendo tuyo y solo tuyo.** El bucle no funde ramas y no lo
   ha hecho.
