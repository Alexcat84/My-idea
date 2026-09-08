### TAREA 2. `OP-I-01`, LA ULTIMA DE LAS CUATRO FICHAS REALES DE LA MORATORIA

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN con
`scripts/loop/_v211_t2_seccion.py` de `docs/loop/SALIDA_V211_T2_OP_I_01.txt`,
`docs/loop/SALIDA_V211_T2_VARA.txt` y
`docs/loop/SALIDA_V211_T2_VARA_ANTES_DE_MI_1B.txt`, **y ese compositor cae en rojo si
no puede leer una sola de ellas**.

#### 2.a. LA VARA, CORRIDA AL EMPEZAR, DICE OTRA COSA QUE EL ENCARGO. MANDA MI MEDICION

El encargo escribe que `vuelta150_3_relectura_expediente.py --corte HEAD` da **3** fichas
de trabajo real, **2** con producto documental en disco (`OP-L-02` y `OP-L-03`) y **1**
sin el: `OP-I-01`. **Mi corrida de hoy sobre `HEAD` da 1 ficha de trabajo real**,
sobre **3** en `LISTA` sin ninguna prueba, de las que **2** estan
CONSUMIDAS. Y de esa 1 de trabajo real, **1** tiene su producto
documental en disco y **0** no lo tiene.

**LA CAUSA ES MIA Y LA MIDO, NO LA SUPONGO.** La `TAREA 1.b` de esta misma vuelta movio
`OP-L-02` y `OP-L-03` a `HECHA`, y esa vara lee el campo `estado` para repartir. Para
separar lo que movio mi propia mano de lo que el encargo tuviera mal, **corri la vara
otra vez en un `git worktree` desechable plantado en mi commit de apertura**, o sea con
el fichero como estaba ANTES de mi `1.b`, y la retire al terminar. Ahi la vara da
**5** en `LISTA` sin prueba, **2** CONSUMIDAS y **3** de
TRABAJO REAL, con **2** con producto documental y **1** sin el.
**Las tres cifras del encargo reproducen al digito en su propio corte**: el encargo tenia
razon y **fui yo quien movio la vara**.

**PERO UNA CELDA DEL ENCARGO SI ESTA CAMBIADA DE SITIO, Y NO ES POR MI MANO.** En esa
misma corrida de apertura, la ficha que **NO** tiene producto documental es
**`OP-L-02`**, con **0** menciones de fichero en su evidencia, y no `OP-I-01`.
`OP-I-01` **si** tiene los suyos: su evidencia nombra `INVENTARIO.jsonl`,
`10_INVENTARIO.md` y `AUDITOR.md`, **y los tres existen en disco en las dos corridas**.
El encargo pone a `OP-L-02` entre las que lo tienen y a `OP-I-01` entre las que no,
**y esta justo al reves**. Lo declaro y no lo arreglo.

#### 2.b. LA FORMA DE LA FICHA (paso 1 del encargo)

Linea **44** de `docs/plan/OPERACIONES.jsonl`, **18** campos.
`tipo` **MESA**, `orden` **1**, `fase` **10_INVENTARIO**, `fecha_corte`
**2026-08-11**, `depende_de` **vacio** (0 elementos) y `bloquea_a` **vacio**
(0 elementos). Los cuatro campos que el encargo pide por tamano: `evidencia`
**4** elementos y **1522** caracteres, `verificacion` **4** y
**200**, `adjudicacion` **186** caracteres y `nota` **12772**.

#### 2.c. PARADA. LA FILA `10 INVENTARIO` NO EXISTE (paso 2 del encargo)

**ESTO ES PARADA Y NO IMPROVISACION** (punto 6 del encargo, `AUDITOR.md` 3). El encargo
manda medir el criterio de hecho *"contra la fila `10 INVENTARIO` de
`docs/plan/08_VERIFICACION.md`, citada literal, y contra ella y no contra tu idea de lo
que la ficha deberia ser"*. **Esa fila no esta.** Barrida la tabla `POR FASE` del
fichero: **10** filas, **0** cuyo numero de fase sea 10, y
**0** menciones del literal `10 INVENTARIO` en el fichero entero.

| fila | linea |
|---|---:|
| `0 CODIGO` | 23 |
| `01 FUENTES` | 24 |
| `02 DESTEJIDOS` | 25 |
| `03 FUSIONES` | 26 |
| `04 ENLACES` | 27 |
| `05 SANEO` | 28 |
| `06 MESAS` | 29 |
| `07 ADUANA` | 30 |
| `LA VARA OPERATIVA` | 199 |
| `LA CIFRA QUE SE VIGILA` | 200 |

(las dos ultimas no son de la tabla `POR FASE`; salen del mismo barrido y se publican
para no recortar lo que el instrumento vio)

**LO QUE SI EXISTE Y NO USO:** la linea **9** del mismo fichero lleva el
criterio general, *"UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE CAERIA SI EL FALLO
VOLVIERA"*, bajo un titulo que dice **"EL CRITERIO DE HECHO, y es uno solo"**. **Que ese
criterio general valga para una ficha de fase 10 sin fila propia es exactamente la
decision que no me toca**, y por eso lo traigo en vez de usarlo. **Sin esa fila no
adjudico el criterio de hecho de `OP-I-01`.**

#### 2.d. PUNTO POR PUNTO DE SU `verificacion` (paso 3 del encargo)

**CIFRA puntos: 4. CIFRA puntos sin cita: 0.** El reparto:
**A MEDIAS 2, CUBRE 1, NO CUBRE 1**.

| # | el punto, literal | veredicto | lo medido, y de donde sale |
|---:|---|---|---|
| 1 | *toda entrada lleva su `fecha_corte`* | **CUBRE** | **672** entradas contadas en `docs/plan/INVENTARIO.jsonl`, **672** con `fecha_corte` y **0** sin ella. La regla, en `docs/plan/10_INVENTARIO.md` linea 7 |
| 2 | *toda forma con cobertura incompleta va marcada PROVISIONAL* | **NO CUBRE** | **555** entradas con cobertura de la forma *N de M pares leidos*; de esas, **95 INCOMPLETAS**; de esas incompletas, **0** llevan la palabra PROVISIONAL en algun campo. En el inventario entero solo **3** entradas la llevan, **las tres de tipo `racimo`** y ninguna incompleta por esta cuenta |
| 3 | *todo hueco va NOMBRADO, nunca rellenado* | **A MEDIAS** | La mitad medible sale: **119** entradas nombran HUECO. La otra mitad, *nunca rellenado*, **es una negativa, y una busqueda negativa no se puede citar** (`EJECUTOR.md` 9). Por eso no escribo CUBRE |
| 4 | *el inventario se recomputa entero con el disparador de `08_VERIFICACION`* | **A MEDIAS** | El disparador **ya disparo** (`08_VERIFICACION.md` linea 381: se dispara al puesto 3.388, y el marcador de la 210 mide 3388). **El archivo fuente si se recomputo; la vista humana no**, y lo dice ella misma en `10_INVENTARIO.md` linea 19: *"LA TABLA NO SE REGENERA AQUI, A PROPOSITO"*. La adjudicacion de la ficha nombra **las dos formas**, y solo una esta al dia |

#### 2.e. LAS TRES SEDES, POR LAS DOS CONVENCIONES, AL ENTRAR Y AL SALIR (paso 4)

**Salen identicas a como entraron 3 de 3**, que es lo que se exige, porque
**esta tarea no escribe en ninguna de las tres**. Las tres calzan al digito con los
contrastes del encargo, **incluida la que el propio encargo avisa que no coincide consigo
misma**:

| sede | bytes en disco | bytes normalizado a LF | `sha256` disco | `sha256` LF | las dos convenciones |
|---|---:|---:|---|---|---|
| `docs/plan/INVENTARIO.jsonl` | **584554** | **584554** | **`69666b73339f2afe`** | **`69666b73339f2afe`** | COINCIDEN |
| `docs/loop/AUDITOR.md` | **30581** | **30581** | **`0527e091eb020829`** | **`0527e091eb020829`** | COINCIDEN |

#### 2.f. LAS 336 ENTRADAS, RECOMPUTADAS DEL FICHERO (paso 5 del encargo)

La cifra publicada vive en `docs/loop/AUDITOR.md` lineas **335** y **336**,
y **la recuento de sus propios sumandos: 336**. Mi recomputo de hoy, contando
`docs/plan/INVENTARIO.jsonl` linea a linea:

| tipo | `AUDITOR.md` 5 (corte 12 ago 2026) | mi conteo de hoy | calza |
|---|---:|---:|---|
| `acto` | 221 | 556 | **NO** |
| `defecto` | 19 | 19 | SI |
| `dominio` | 10 | 10 | SI |
| `familia_de_ids` | 53 | 54 | **NO** |
| `figura` | 20 | 20 | SI |
| `racimo` | 13 | 13 | SI |
| **TOTAL** | **336** | **672** | **NO** |

**LAS DOS SE PUBLICAN AL LADO Y LA DISCREPANCIA NO SE RESUELVE COPIANDO NINGUNA**
(`AUDITOR.md` 1.1). La de **336** lleva su corte y el archivo **pudo envejecer
honestamente** (banco `9.21`).

**Y LA DISCREPANCIA TIENE CAUSA MEDIDA, QUE NO ES LA MISMA EN LOS DOS TIPOS QUE NO
CALZAN.** El salto de `acto` de 221 a 556 **ya esta explicado en el propio archivo**, que
publica las 221 viejas marcadas una a una como `SUPERADA POR EL CORTE 3.388`. El de
`familia_de_ids` **no**: `docs/plan/10_INVENTARIO.md` linea **32** publica
`filas totales` **671** para el archivo fuente al corte 3.388 y **hoy cuento
672**, y su linea **33** dice de los otros cinco tipos *"identicos, no se
movieron"*, cuando `familia_de_ids` **si se movio**: **54** hoy contra **53**. La
unidad que separa las dos cifras es **1** entrada, **`HUGOS-SISTEMAS`**, con
`fecha_corte` **2026-08-14**. **Queda declarada y no la toco.**

#### 2.g. EL CIERRE DE LA FICHA SE DEJA AL ACTA (punto 7 del encargo)

El campo `estado` de `OP-I-01`, releido al salir, sigue en **`LISTA`**. **No lo
toque.** Y con la fila de su criterio de hecho ausente y **un punto de su `verificacion`
en NO CUBRE**, esta ficha **no la cierro yo aunque el encargo lo permitiera**: se mide, se
publica y se trae.
