### TAREA 1. LA CORRECCION DECLARADA DE LA `evidencia` DE `OP-L-03`, EN SU SEDE Y POR ADICION

**ADJUDICADA POR EL ACTA 201 EN SU `4.3`.** El ejecutor de la 201 la propuso y no
la escribio sin adjudicacion; **ahora esta adjudicada y esta escrita**.

**EL CARRIL ES EL DE `OP-I-01` DE LA VUELTA 201 Y NO OTRO:** banco `9.10`, **POR
ADICION**, como **un elemento mas de la misma lista `evidencia`**, **sin clave
nueva de esquema** y **sin tocar ni tachar el texto viejo**. Es la via de la
gemela `OP-L-01` en la vuelta 166, que el **acta 71, seccion 6, adjudicacion 3**
adjudico **con las palabras NO ES PARADA**. Instrumento:
`scripts/loop/_v202_t1_correccion_op_l_03.py`, salida sellada en
`docs/loop/SALIDA_V202_T1_CORRECCION_OP_L_03.txt`.

**LA COORDENADA VA POR LINEA MAS INDICE** (acta 201, `4.4`), **y se publican las
dos numeraciones** para que ninguna cita quede ambigua: la ficha `OP-L-03` vive
en **la linea 43** de `docs/plan/OPERACIONES.jsonl`, con **1 solo acierto** de las
**71** lineas no vacias, y su `evidencia` tenia **3** elementos.

| elemento | indice base 0 | literal, citado verbatim de la ficha |
|---|---|---|
| 1 | 0 | `BANCO_DEL_PLAN.md P.5` |
| 2 | 1 | `MEDIDO el 11 ago 2026: 55 pares en 29 actos, corte puesto 2117` |
| 3 | 2 | `LECTURAS_DIRIGIDAS.md, el reparto por acto` |

#### LAS TRES COSAS OBLIGATORIAS, MEDIDAS AQUI Y NO COPIADAS DEL ENCARGO

**(1) EL DOCUMENTO QUE LA `evidencia` NOMBRA NO TRAE LO QUE PROMETE.** El
elemento **3** (indice **2**) nombra `LECTURAS_DIRIGIDAS.md`, y ese documento,
que en `docs/plan/LECTURAS_DIRIGIDAS.md` mide **214916 bytes en disco y 214916
bytes normalizados a LF** y **2230 lineas** por `count(NL)`, trae **0 apariciones
del literal `reparto por acto`** y **0 menciones de `OP-L-03`**. **LAS DOS CIFRAS
SE CONTARON AQUI.** Y la busqueda se corrio tambien **POSITIVA sobre 8
variantes**, porque `EJECUTOR.md` 9 dice que **una busqueda negativa no se puede
citar sola**: `reparto por acto`, `reparto por`, `por acto`, `OP-L-03`,
`OP_L_03`, `OP L 03`, `OP_L_03_LECTURAS` y `OP_L_03_TRIANGULOS`, **las 8 en
cero**.

**(2) DONDE VIVE DE VERDAD EL REPARTO POR ACTO, LOS DOS NOMBRADOS Y CON SUS
BYTES EXACTOS** (`P.2`: bytes exactos, nunca redondeados, KB solo entre
parentesis y detras del byte):

| fichero | bytes | filas | actos distintos | lineas no JSON |
|---|---|---|---|---|
| `docs/plan/OP_L_03_LECTURAS.jsonl` | **51368** en disco (50.2 KB) y **51368** en LF | 14 | 14 | 0 |
| `docs/plan/OP_L_03_TRIANGULOS.jsonl` | **55705** en disco (54.4 KB) y **55705** en LF | 19 | 8 | 0 |

**(3) LA COBERTURA REAL CON SU FECHA DE CORTE, QUE ES LA CIFRA QUE NO PODIA
FALTAR.** El elemento **2** promete **55 pares en 29 actos** con corte **11 ago
2026** y **puesto 2117**, leido de la propia ficha y no tecleado.
`docs/plan/OP_L_03_LECTURAS.jsonl`, recontado hoy, trae **14 actos distintos**,
de los cuales **11 tienen `leido` en true y 3 en false**, y sus campos
`cifra_pares_leidos` **suman 19 pares**. O sea: **15 de los 29 actos prometidos
siguen sin ficha de lectura** y **36 de los 55 pares prometidos siguen sin
lectura registrada**, con **fecha de corte 2026-09-07**.

**LA PROMESA VIEJA NO ES UNA MENTIRA Y NO SE RETIRA.** Con su corte era lo que se
iba a hacer. **Lo que la correccion anade es CUANTO DE ESO EXISTE HOY**, con su
propio corte, porque **una evidencia corregida que prometa mas de lo que existe
es exactamente lo que la regla LA RUTA QUE PROMETE PRUEBA ES CIFRA vino a
cazar**. La correccion escrita mide **2405 caracteres** y **0 guiones largos o
medios**.

#### LA GUARDA, CORRIDA DOS VECES Y PROBADA POR MUTACION ANTES DE PUBLICARSE

**LA GUARDA NO ES NUEVA:** es **la misma que la 201 corrio para `OP-I-01`**, y
aqui se escribe en `scripts/loop/_v202_t1_guarda_estado.py` con **prefijo de
guion bajo**, fuera del censo y fuera de la nomina, porque `EJECUTOR.md` 1 exige
que **el caso rojo se pruebe por mutacion** y para mutarla hay que poder llamarla
con datos fabricados. **EL REPO NO SE TOCA EN LA MUTACION:** los casos se
fabrican mutando las lineas **en memoria** y llamando a la funcion pura
`veredicto()`.

**LA PRUEBA DE MUTACION VA DELANTE DE LA PUBLICACION, no detras:** **6 casos** de
mutacion en `docs/loop/SALIDA_V202_T1_MUTACION_GUARDA.txt`, y **los 6 pasan**,
con el caso de control quedando **VERDE 1 de 1**. Los seis: dos lineas difieren
en vez de una; cambia una clave que no es `evidencia`; el `estado` de la ficha se
mueve; el `estado` de otra ficha se mueve; un elemento viejo de `evidencia` se
reescribe en vez de anadirse; y ninguna linea difiere.

**Y LA GUARDA SALE VERDE LAS DOS CORRIDAS**, medida contra `HEAD` con
`git show HEAD:docs/plan/OPERACIONES.jsonl`:

| lo que la guarda mide | corrida 1 | corrida 2 |
|---|---|---|
| lineas no vacias en `HEAD` y en el arbol | 71 y 71 | 71 y 71 |
| lineas que difieren | **1**, la **43** | **1**, la **43** |
| claves de esa ficha que cambian | **1**, y es `evidencia` | **1**, y es `evidencia` |
| `estado` de `OP-L-03` antes y despues | `LISTA` y `LISTA` | `LISTA` y `LISTA` |
| elementos de `evidencia` antes y despues | 3 y 4 | 3 y 4 |
| los 3 viejos identicos y en su orden | SI | SI |
| fichas de las 71 que mueven `estado` | **0** | **0** |
| veredicto | **VERDE** | **VERDE** |

Selladas en `docs/loop/SALIDA_V202_T1_GUARDA_ESTADO.txt` y
`docs/loop/SALIDA_V202_T1_GUARDA_ESTADO_IDEM.txt`.

**LA SEGUNDA CORRIDA DE LA CORRECCION SELLA CRECIMIENTO 0**, que es lo que el
encargo pide: `docs/loop/SALIDA_V202_T1_CORRECCION_OP_L_03_IDEM.txt` dice
**IDEMPOTENTE**, **4 elementos de `evidencia` al entrar** y **crecimiento en
disco 0 bytes**. **El orden de las guardas viene heredado ya arreglado de la
caida declarada de la 201**: la de idempotencia va **delante** de las de cifra,
porque la propia correccion **cita esas cifras verbatim** y una guarda de cifra
puesta delante caeria en la segunda corrida **por el motivo equivocado**.

#### LO QUE NO SE MOVIO, MEDIDO Y NO AFIRMADO

`docs/plan/OPERACIONES.jsonl` entra midiendo **499474 bytes en disco y 499474 en
LF** y sale midiendo **501883 bytes en disco y 501883 en LF**, con un
**crecimiento de 2409 bytes**; tiene **71 lineas no vacias antes y despues** y
**0 lineas que no sean JSON valido**. `git diff HEAD --numstat` da **0 filas en
`dataset/`, 0 en `web/` y 0 en `engine/`**, y en `docs/plan/` da **1 anadida y 1
borrada** en `OPERACIONES.jsonl`, que es lo que un `jsonl` da siempre al
reescribir una linea. **Y ningun veredicto se movio:**
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` mide **4054129 bytes en disco y 4054129 en
LF**, y su `sha256` vale **0a77b5a35a962621** por la convencion de disco y
**0a77b5a35a962621** por la de LF, que es el mismo valor que el sello de apertura.
