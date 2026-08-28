# VUELTA 100, TAREA 6: LA FASE 04 CONTRA LA EVIDENCIA (medicion, sin tocar `estado`)

Remedio de la caida de encargo del auditor (acta 99, 4.8): la pregunta "ejecutable
hoy" se hace contra la EVIDENCIA de las paginas (registro de cierre escrito), no
contra el campo `estado`, que el propio acta midio rancio (70 de 71 en `LISTA`).
NADA de esto toca `estado`: es medicion, y va a `docs/loop/` y al reporte, no al plan.

## LAS 26 DEPENDENCIAS TRANSITIVAS UNICAS DE LAS 10 OPERACIONES DE LA FASE 04

Computadas con el grafo `depende_de` de `docs/plan/OPERACIONES.jsonl` (71 filas,
leido hoy), BFS completo por operacion.

| id | fase | tiene registro de cierre escrito | cita, leida hoy |
|---|---|---|---|
| `OP-D-01` | 02_DESTEJIDOS | **SI** | `docs/plan/02_DESTEJIDOS.md:3581` (frase `REGISTRO DE OPERACION HECHA`), tabla del cierre de fase en `:4479` |
| `OP-D-02` | 02_DESTEJIDOS | **SI** | `docs/plan/02_DESTEJIDOS.md:3581`, tabla `:4480` |
| `OP-D-03` | 02_DESTEJIDOS | **SI** | `docs/plan/02_DESTEJIDOS.md:1197` (`OP-D-03 CERRADA`), tabla `:4481` |
| `OP-D-04` | 02_DESTEJIDOS | **SI** | `docs/plan/02_DESTEJIDOS.md:1614` (`OP-D-04 CERRADA`), tabla `:4482` |
| `OP-D-05` | 02_DESTEJIDOS | **SI** | `docs/plan/02_DESTEJIDOS.md:1765` (`OP-D-05 SELLADA`), tabla `:4483` |
| `OP-D-06` | 02_DESTEJIDOS | **SI** | `docs/plan/02_DESTEJIDOS.md:3403`, tabla `:4484` |
| `OP-D-07` | 02_DESTEJIDOS | **SI** | `docs/plan/02_DESTEJIDOS.md:4591` (corregida) y `:4597` (`OP-D-07 SELLADA`), tabla `:4485` |
| `OP-F-01` | 01_FUENTES | **SI** | `docs/plan/01_FUENTES.md:1146`, seccion "LA FASE 01 QUEDA CERRADA" (`:1139`) |
| `OP-F-02` | 01_FUENTES | **SI** | `docs/plan/01_FUENTES.md:1147` |
| `OP-F-03` | 01_FUENTES | **SI** | `docs/plan/01_FUENTES.md:1148` |
| `OP-U-01` | 03_FUSIONES | **SI** | `docs/plan/03_FUSIONES.md:9245` (RESUELTA, "servida por sus 14 registros"), dentro de "LA FASE 03 QUEDA CERRADA CON REMISION" (`:9229`) |
| `OP-U-02` | 03_FUSIONES | **SI** | `docs/plan/03_FUSIONES.md:9245` (RESUELTA, 11 registros) |
| `OP-M-03-I` | 03_FUSIONES | **SI** | `docs/plan/03_FUSIONES.md:9245` (EJECUTADA) |
| `OP-M-03-II` | 03_FUSIONES | **SI** | `docs/plan/03_FUSIONES.md:9245` (EJECUTADA) |
| `OP-E-01` | 04_ENLACES | **SI** | nota propia en `OPERACIONES.jsonl`: "CIERRE MEDIDO (27 ago 2026, vuelta 87...)", cifra final 220/98/122 (vuelta 89); tambien `docs/plan/04_ENLACES.md`, apartado "OP-E-01 CIERRE MEDIDO" |
| `OP-C-01` | 00_CODIGO | **NO** | nota propia describe el ARREGLO pendiente ("resolver nid al entrar en..."), sin declaracion de cierre; no existe pagina `00_CODIGO.md` con registro |
| `OP-C-02` | 00_CODIGO | **NO** | idem, nota describe el ARREGLO pendiente sobre `plan/route.ts` |
| `OP-C-03` | 00_CODIGO | **NO** | idem, nota describe el ARREGLO pendiente sobre `resumenNodo` |
| `OP-C-04` | 00_CODIGO | **NO** | la nota dice "DOS PREGUNTAS... QUEDAN CERRADAS", pero son dos preguntas de diseno, no la ejecucion de la guarda; el ARREGLO ("anadir a Gate 0 la comprobacion...") sigue en la nota como pendiente, sin frase de cierre de la operacion |
| `OP-S-06` | 00_CODIGO | **NO** | nota describe el mapeo hallado, sin frase de cierre |
| `OP-S-07` | 00_CODIGO | **NO** | nota describe la consecuencia de maquinaria, sin frase de cierre |
| `OP-M-01` | 06_MESAS | **NO** | nota propia: "RESERVA ESCRITA... TRES pendientes... LA MESA SIGUE EN PIE"; `docs/plan/03_FUSIONES.md:9272` ("LAS CINCO MESAS SON TERRITORIO INTEGRO DE LA FASE 06"): la mesa no se ha sentado |
| `OP-M-01-FUSION` | 03_FUSIONES | **NO** | `docs/plan/03_FUSIONES.md:9246`: ENRUTADA a la fase 06, no CERRADA; `03_FUSIONES.md:9255` ("quedan ENRUTADAS a la fase 06... se ejecutan cuando sus mesas se sienten") |
| `OP-M-03` | 06_MESAS | **NO** | nota propia: "LA MESA SIGUE EN PIE sin cambios", pares en B sin resolver; `03_FUSIONES.md:9277` ("no toca la mesa OP-M-03 ni sus colisiones") |
| `OP-M-03-III` | 03_FUSIONES | **NO** | `docs/plan/03_FUSIONES.md:9246`: ENRUTADA a la fase 06, no CERRADA |
| `OP-E-06` | 04_ENLACES | **NO** | nota propia declara "OP-E-06 ABRE" y describe una tanda ejecutada (113 escritas, 1 ya_estaba, 3 enlace mutuo aparte de 117), pero NINGUNA frase de cierre de la operacion entera; no hay apartado "OP-E-06 CIERRE" en `04_ENLACES.md` (buscado hoy, cero resultados) |

**11 de 26 CON registro de cierre escrito; 15 SIN el.**

## LAS 10 OPERACIONES DE LA FASE 04, CADA UNA CONTRA SUS DEPENDENCIAS TRANSITIVAS

| operacion | deps transitivas (n) | todas con cierre escrito | bloqueantes reales (sin cierre escrito) |
|---|---:|---|---|
| `OP-E-01` | 0 | **SI (vacuo)** | ninguno |
| `OP-E-02` (ya `HECHA`) | 0 | **SI (vacuo)** | ninguno |
| `OP-E-03` | 18 | NO | `OP-C-01`, `OP-C-02`, `OP-C-03`, `OP-C-04`, `OP-S-06`, `OP-S-07` (6) |
| `OP-M-03-ENLACES` | 5 | NO | `OP-M-03`, `OP-M-03-III` (2) |
| `OP-E-04` | 6 | NO | `OP-M-01`, `OP-M-01-FUSION` (2) |
| `OP-E-05` | 6 | NO | `OP-M-01`, `OP-M-01-FUSION` (2) |
| `OP-M-01-ESLABONES` | 6 | NO | `OP-M-01`, `OP-M-01-FUSION` (2) |
| `OP-M-01-SEXTO` | 6 | NO | `OP-M-01`, `OP-M-01-FUSION` (2) |
| `OP-E-06` | 10 | NO | `OP-M-03` (1) |
| `OP-E-07` | 11 | NO | `OP-M-03`, `OP-E-06` (2) |

## LA CUENTA QUE PIDE EL ENCARGO

**CUANTAS DE LAS DIEZ TIENEN TODAS SUS DEPENDENCIAS TRANSITIVAS CON CIERRE ESCRITO:
DOS** (`OP-E-01` y `OP-E-02`, las dos vacuamente: `depende_de` esta vacio en las
dos). Contando solo entre las **LISTA** (excluyendo la ya `HECHA` `OP-E-02`):
**1 EJECUTABLE HOY POR EVIDENCIA** (`OP-E-01`), **8 BLOQUEADAS POR EVIDENCIA**
(`OP-E-03`, `OP-M-03-ENLACES`, `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES`,
`OP-M-01-SEXTO`, `OP-E-06`, `OP-E-07`).

## LA DIVERGENCIA, DECLARADA Y NO RESUELTA (per encargo, TAREA 6 no adjudica)

**EL TOTAL COINCIDE CON LA CIFRA DE LA ADJUDICACION 4.7 DEL ACTA 99** (1 HECHA, 1
EJECUTABLE, 8 BLOQUEADAS), pero **LA COMPOSICION NO ES LA MISMA**, y esto SI es una
divergencia real entre medir por campo y medir por evidencia: bajo el criterio del
campo `estado` (que la 4.8 del acta declaro rancio), CUALQUIER dependencia con
`estado != HECHA` cuenta como bloqueante, y de las 26 dependencias transitivas
**25 tienen `estado = LISTA`** (solo `OP-E-02` esta en `HECHA`), asi que ese
criterio marcaria a `OP-E-07` con SUS ONCE dependencias como bloqueantes por igual,
sin distinguir. **BAJO LA EVIDENCIA, SOLO 15 DE LAS 26 SON BLOQUEO REAL**: las otras
**11** (`OP-D-01` a `OP-D-07`, `OP-F-01` a `OP-F-03`, `OP-U-01`, `OP-U-02`,
`OP-M-03-I`, `OP-M-03-II`, `OP-E-01`, quince nombres, once ids) tienen `estado =
LISTA` pero SI cuentan con registro de cierre escrito, y el campo por si solo las
habria contado como bloqueo sin serlo. **QUE EL TOTAL DE LA FASE 04 COINCIDA (1/1/8)
ES EL RESULTADO, NO LA PRUEBA**: la composicion interna de cada bloqueo cambia de
sitio (por ejemplo `OP-E-06`, que bajo el campo se veria con potencialmente varios
bloqueantes de fase 02 y 01 que en realidad SI estan cerrados, y bajo la evidencia
tiene UN SOLO bloqueante real, `OP-M-03`). Esta divergencia se declara aqui, sin
resolverla y sin abrir ninguna fase nueva: que se hace con la fase 04 es decision
del acta 100 o del fundador, por letra del propio encargo.

## LO QUE ESTA MEDICION NO HACE

No toca `estado` de ninguna operacion. No abre la fase 05 ni la 06. No adjudica si
`OP-E-06` deberia tener su propio apartado de cierre en `04_ENLACES.md`: se declara
la ausencia, no se remedia (remediarlo es escribir en el plan, y `EJECUTOR.md` 4
prohibe reparar nodos o plan fuera de una fase de EJECUCION declarada por el
encargo).
