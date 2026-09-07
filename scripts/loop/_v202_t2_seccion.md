### TAREA 2. `OP-L-02` CONTRA EL CRITERIO DE HECHO. SE PROPONE Y NO SE CIERRA

**LO PRIMERO, Y SIN CLONAR NADA.** Los dos instrumentos se **importaron y se
corrieron tal cual**, y **ninguno se toco**: `scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py`
mide **9310 bytes en disco y 9310 bytes normalizados a LF**, y
`scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py` mide **13487 bytes en disco
y 13487 bytes normalizados a LF**. **Se comprobo ANTES de correrlos que ninguno
escribe ficheros**: **0 lineas con marca de escritura en disco** en cada uno, y
despues de correrlos **0 lineas de `git status` que no sean salidas de esta
tarea**. Selladas con nombre de esta vuelta en
`docs/loop/SALIDA_V202_T2_COBERTURA_169.txt` (**5559 bytes en disco y 5449 en
LF**) y `docs/loop/SALIDA_V202_T2_VEREDICTO_170.txt` (**5880 bytes en disco y
5789 en LF**). La lectura entera vive en `docs/loop/SALIDA_V202_T2_OP_L_02.txt`.

#### EL CRITERIO DE HECHO, CITADO POR LINEA

`docs/plan/08_VERIFICACION.md` mide **69068 bytes en disco y 69068 bytes
normalizados a LF** y trae **913 lineas**. Su cabecera esta en la **linea 7**, con
**1 solo acierto**, y el criterio, verbatim:

- **linea 9**: *UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE CAERIA SI EL FALLO
  VOLVIERA.*
- **linea 11**: *No cuando pasa verde: cuando se CAERIA.*
- **lineas 13 a 15**: *Es el criterio del CASO POSITIVO de la FASE 0, aplicado a
  todo el plan. Y tiene una comprobacion barata: correr la prueba ANTES del
  arreglo. Si pasa, no prueba nada.*

Y en ese mismo documento `OP-L-02` se nombra en **1 sola linea, la 409**, que
dice *"DECISION PENDIENTE"* y *"el universo de 205 se remide"*. **Esa fila es del
apartado del recomputo y no es la verificacion de la ficha**, que es lo que aqui
se mide.

#### LAS TRES CLAUSULAS, CITADAS POR LINEA MAS INDICE

La ficha vive en la **linea 42** de `docs/plan/OPERACIONES.jsonl`, con **1 solo
acierto**. Su `verificacion` tiene **4 elementos**, de los cuales **3 son
clausulas** y **1 es una CORRECCION DECLARADA**, que no es una clausula que
cumplir. Su `evidencia` tiene **1 elemento**.

| coordenada | caracteres | literal |
|---|---:|---|
| linea 42 + indice 0 (elemento 1) | 77 | `las tres nominas afectadas quedan con cobertura COMPLETA y su forma reescrita` |
| linea 42 + indice 1 (elemento 2) | 51 | `el marcador del cribado no se mueve: sigue en 2.117` |
| linea 42 + indice 2 (elemento 3) | 65 | `cada grupo del backlog lleva su motivo escrito, no solo su cuenta` |
| linea 42 + indice 3 (elemento 4) | 1486 | CORRECCION DECLARADA, no es clausula |

**LA PARADA DE LA 201 NO SE VUELVE A LEVANTAR**, porque el acta 201 la disolvio en
su `4.1`: la clausula 1 **si se puede medir sin decidir**, y el instrumento la
mide. Sus seis nominas viven **por id** en la constante `NOMINAS_OP_L_02`, y su
salida de hoy da **6 nominas parseadas** y **0 pares SIN veredicto** en las seis.

#### LOS VEREDICTOS, LEIDOS DE LA SELLADA Y NO TECLEADOS

| clausula | veredicto del instrumento | de donde sale la cifra |
|---|---|---|
| 1, cobertura completa y forma reescrita | **CUMPLIDA** | **0** pares sin veredicto en las seis nominas; las tres nominas con su `forma` reescrita y el corte dentro |
| 2, el marcador no se mueve | **NO CUMPLIDA** | **1** fila de `numstat`, y esa es la trampa que se remide abajo |
| 3, cada grupo con su motivo | **CUMPLIDA** | **4** grupos del backlog y **0** sin motivo escrito |

**CIFRA clausulas cumplidas segun el instrumento, tal cual se corrio: 2 de 3.**

#### LA CLAUSULA 2, REMEDIDA. LAS DOS LECTURAS JUNTAS Y LA DISCREPANCIA DECLARADA

**LOS DOS HEAD SE LEEN DE SU SELLO Y NINGUNO SE TECLEA.** El instrumento lee
`docs/loop/SALIDA_V170_HEAD_APERTURA.txt`, que dice **`46208790`**; esta vuelta
lee su propio `docs/loop/SALIDA_V202_HEAD_APERTURA.txt`, que dice **`ebe04895`**.

| lectura | comando | filas de `numstat` | sin commitear | veredicto |
|---|---|---:|---:|---|
| la del instrumento | `git diff 46208790 HEAD --numstat -- docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **1** | 0 | **NO CUMPLIDA** |
| la de esta vuelta | `git diff ebe04895 HEAD --numstat -- docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **0** | 0 | **CUMPLIDA** |

**LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO.** El acta 201 ya la
adjudico en su `4.2`: es **FALSO ROJO**, porque el instrumento diffea contra un
HEAD sellado en la vuelta **170** y desde entonces han pasado vueltas que **si**
movieron el fichero. **Su reparacion es de codigo, la moratoria la prohibe hoy y
va a la auditoria integral. AQUI NO SE ARREGLA.**

**EL MARCADOR, RECONTADO AQUI Y NO COPIADO:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
mide **4054129 bytes en disco y 4054129 bytes normalizados a LF**, con **3388
filas no vacias**, **0 lineas que no sean JSON valido**, reparto **A 551, B 72, C
5 y D 2760** que **suma 3388**, **3388 puestos distintos**, **maximo 3388** y **0
huecos**. **NO PASA POR EL RESOLUTOR, Y ESO SE DICE EN VEZ DE CALLARLO:** `P.1`
manda pasar por el resolutor todo conteo que **toque ids**, y contar filas, clases
y puestos **no toca ninguno**. **La clausula pide que la OPERACION no lo mueva, no
que valga 2.117 hoy**, y su propia CORRECCION DECLARADA lo dice: el 2.117 es el
valor en la `fecha_corte` de la ficha, **testigo y no condicion**.

#### EL CRITERIO DE HECHO APLICADO: LOS TRES VEREDICTOS SE PUEDEN CAER

El criterio pide que **la verificacion se caeria si el fallo volviera**, y trae su
propia comprobacion barata. Aqui se comprueba **leyendo el codigo del instrumento
y sin tocarlo** que cada veredicto sale de **una expresion computada y no de un
literal**, que es lo que `EJECUTOR.md` 1 llama **un caso rojo que no puede
fallar**:

| clausula | linea de `vuelta170_tarea5b_veredicto_op_l_02.py` | asignacion | sale de un literal |
|---|---:|---|---|
| 1 | 166 | `cumple1 = (sin_total == 0 and con_corte == len(LAS_TRES))` | **NO** |
| 2 | 195 | `cumple2 = (len(filas) == 0 and len(filas2) == 0)` | **NO** |
| 3 | 222 | `cumple3 = (len(grupos) > 0 and not sin_motivo)` | **NO** |

**Las tres se caerian**: si un par de las seis nominas perdiera su veredicto,
`sin_total` dejaria de ser 0; si la operacion moviera el archivo, el `numstat`
dejaria de ser 0; si un grupo del backlog perdiera su motivo, `sin_motivo` dejaria
de estar vacio.

#### LA PROPUESTA, QUE NO CIERRA NADA

**CON LA CLAUSULA 2 REMEDIDA CONTRA EL HEAD DE ESTA VUELTA, LAS TRES QUEDAN
CUMPLIDAS: 3 de 3.** **Y AUN ASI NO SE CIERRA.** El encargo dice **PROPONLO Y NO
LO CIERRES**, y `AUDITOR.md` 0 dice que **el campo `estado` no es la vara**. El
`estado` de `OP-L-02` **entra y sale en `LISTA`**, y este computo cambia **0
lineas** de `docs/plan/OPERACIONES.jsonl`.

**LA EVIDENCIA DE LA PROPUESTA, ENTERA:** `docs/loop/SALIDA_V202_T2_COBERTURA_169.txt`,
`docs/loop/SALIDA_V202_T2_VEREDICTO_170.txt` y
`docs/loop/SALIDA_V202_T2_OP_L_02.txt`, mas la ficha en la **linea 42** de
`docs/plan/OPERACIONES.jsonl`. **Lo adjudica el auditor.**

**DISCUTIBLE, MARCADO ANTES DE SABER SI ACIERTO:** la propuesta descansa en una
lectura de la clausula 2 que **el instrumento de la casa da como NO CUMPLIDA**. Yo
sostengo que el 0 contra `ebe04895` es la lectura correcta **porque la clausula
pide que la operacion no mueva el archivo y la operacion es esta vuelta**, y el
acta 201 ya llamo falso rojo al otro. **Pero quien decide si una clausula se puede
dar por cumplida contra una vara distinta de la que el instrumento usa no soy yo.**
