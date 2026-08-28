# VUELTA 99, TAREA 4: EL ESTADO REAL DE LA FASE 04_ENLACES

Medicion pura, corrida con `scripts/loop/vuelta99_tarea4_medir_fase04.py`
(`docs/loop/SALIDA_V99_TAREA4_MEDIR_FASE04.txt`, EXIT 0). NINGUN ESTADO SE
TOCA: esto se escribe en `docs/loop/`, no en `docs/plan/`.

## (4.1) Las diez operaciones, tal como estan hoy

| id_op | orden | estado | depende_de | dependencias NO HECHA |
|---|---:|---|---|---|
| `OP-E-01` | 1 | LISTA | (ninguna) | (ninguna) |
| `OP-E-02` | 2 | **HECHA** | (ninguna) | (ninguna) |
| `OP-E-03` | 3 | LISTA | `OP-E-01`, `OP-U-02` | las dos |
| `OP-M-03-ENLACES` | 4 | LISTA | `OP-M-03-I`, `OP-M-03-II`, `OP-M-03-III` | las tres |
| `OP-E-04` | 5 | LISTA | `OP-M-01`, `OP-M-01-FUSION` | las dos |
| `OP-E-05` | 6 | LISTA | `OP-M-01`, `OP-M-01-FUSION` | las dos |
| `OP-M-01-ESLABONES` | 7 | LISTA | `OP-M-01`, `OP-M-01-FUSION` | las dos |
| `OP-M-01-SEXTO` | 8 | LISTA | `OP-M-01`, `OP-M-01-FUSION` | las dos |
| `OP-E-06` | 9 | LISTA | `OP-D-01` a `OP-D-07` (7) | las siete |
| `OP-E-07` | 10 | LISTA | `OP-E-06` | la una |

Nueve de diez siguen en `LISTA`; solo `OP-E-02` esta en `HECHA`.

## (4.2) El campo `estado` contra la evidencia de su nota y de `04_ENLACES.md`

**LA DIVERGENCIA QUE EL ENCARGO YA SENALABA SE CONFIRMA, MEDIDA:** `OP-E-01`
tiene una seccion propia titulada `OP-E-01, CIERRE MEDIDO` en
`docs/plan/04_ENLACES.md` (linea 705) y su nota termina citando esa misma
seccion con una cifra cerrada (**220 / 98 ESCRITA / 122 NO SE ENLAZA**,
correccion declarada del 29 ago 2026), y sigue en `LISTA`. `OP-E-03`, que se
cerro literalmente HOY MISMO en esta vuelta (183 de 183, TAREA 3), tambien se
queda en `LISTA` a proposito: su propio addendum de cierre lo declara
("cambiar `estado` es una decision que este addendum no toma").

**TRES OPERACIONES DICEN, EN SU PROPIA NOTA, POR QUE `estado` NO SUBE A
`HECHA` AUNQUE EL TRABAJO ESTE HECHO**, con la MISMA frase, palabra por
palabra: `OP-E-06` y `OP-E-07` citan "*el estado de verdad es el repo y el
commit, no un campo nuevo (backlog del 14 ago 2026, decidido SIN estado
nuevo)*", y nombran a `OP-E-01` y `OP-E-04` como parte del mismo criterio.
**ES UNA POLITICA DECLARADA, NO UN OLVIDO**: el campo `estado` de estas
operaciones no se disenó para reflejar "trabajo terminado", asi que leerlo
como tal es el error que la TAREA 4 pide medir, no una caida de nadie.

**DOS OPERACIONES (`OP-E-05`, `OP-M-01-ESLABONES`) usan tiempo pasado en su
nota** ("*borrara ESTAS CUATRO aristas*", "*el segundo peldano YA ESTABA
puesto*"), lo que sugiere trabajo ya hecho, pero SIN la frase explicita de
"estado se queda en LISTA por..." que si traen `OP-E-01`, `OP-E-04`,
`OP-E-06` y `OP-E-07`. **NO SE RESUELVE AQUI**: se declara la ambiguedad y no
se decide si son parte de la misma politica o si de verdad esperan a que
`OP-M-01` corra.

**`OP-E-04` es la unica cuya propia nota explica por que SIGUE BLOQUEADA de
verdad** ("*SEIS de los nueve destinos mueren el mismo dia, asi que esta
operacion NO PUEDE correr antes que ellas*"): aqui `estado=LISTA` SI describe
la realidad.

**Solo cuatro de las diez tienen seccion propia en `04_ENLACES.md`** (por
titulo con su id): `OP-E-01`, `OP-E-03`, `OP-E-06` y `OP-E-07`. Las otras seis
(`OP-E-02`, `OP-M-03-ENLACES`, `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES`,
`OP-M-01-SEXTO`) no traen una seccion buscable por su id: su unica
documentacion vive en la `nota` de `OPERACIONES.jsonl`. Esto no se declara
caida: el plan no exige una seccion por operacion, y `04_ENLACES.md` trae
prosa general (`LOS SUELTOS DE RACIMOS`, `LAS DOS OPERACIONES`) que puede
cubrirlas sin nombrarlas literalmente; no se leyo esa prosa entera para esta
medicion.

## (4.3) La cuenta que importa: cuantas son ejecutables hoy

Con el criterio del encargo (**sin dependencia VIVA de OTRA fase**):

| grupo | cuantas | cuales |
|---|---:|---|
| YA `HECHA` | **1** | `OP-E-02` |
| EJECUTABLE HOY (cero dependencia externa viva) | **2** | `OP-E-01` (sin ninguna dependencia); `OP-E-07` (solo depende de `OP-E-06`, que es DE LA MISMA FASE y sigue en `LISTA`) |
| ESPERA DEPENDENCIA VIVA DE OTRA FASE | **7** | `OP-E-03` (fase 03), `OP-M-03-ENLACES` (fase 03), `OP-E-04` (fases 03 y 06), `OP-E-05` (fases 03 y 06), `OP-M-01-ESLABONES` (fases 03 y 06), `OP-M-01-SEXTO` (fases 03 y 06), `OP-E-06` (fase 02) |

**SALE LO QUE EL ENCARGO SOSPECHABA, CON LA CIFRA:** de las siete que
esperan, **CUATRO esperan a `OP-M-01` o a `OP-M-01-FUSION`** (fase
`06_MESAS` y `03_FUSIONES`: `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES`,
`OP-M-01-SEXTO`) y **UNA espera a las siete `OP-D`** (fase `02_DESTEJIDOS`:
`OP-E-06`). Las otras dos (`OP-E-03`, `OP-M-03-ENLACES`) esperan a la fase
`03_FUSIONES` por otra via (`OP-U-02` y las tres `OP-M-03-*`).

**PARO AQUI, TAL COMO EL ENCARGO PIDE.** No abro ninguna fase nueva y no
decido que hacer con `OP-E-01` (sin dependencia y con cierre medido en su
nota, pero en `LISTA`) ni con `OP-E-07` (formalmente ejecutable hoy, pero su
unica dependencia, `OP-E-06`, tampoco esta en `HECHA`). La decision de que
se hace con la fase 04 es del auditor en el acta 99, y si me pasa de el, del
fundador.
