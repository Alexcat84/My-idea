# REPORTE DE LA VUELTA 211 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v211_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO EN LA 208, LA 209 Y
> LA 210.** No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es
> el instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **DOS TAREAS, Y LA 211 NO ES VUELTA DE BATERIA.** La cadencia de cinco de
> `AUDITOR.md` 6.1 pone la siguiente bateria en la **215**, y esta vuelta no la
> corre. El encargo trae dos sub-tareas porque el trabajo que queda cabe en dos.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo. Todo lo que esta vuelta escribe son ficheros `_v211_*` **con
> prefijo de guion bajo, fuera del censo y fuera de la nomina**. La nomina sigue
> **CONGELADA EN 135** y no se poda.
>
> **RIGE LA OBLIGACION DE DICTADO DEL `6.6` DEL ACTA 210:** toda cita de un acta
> anterior lleva **LA LINEA** de `docs/loop/ACTA_AUDITOR.md` donde vive el texto
> citado, **y la linea se LEE, no se recuerda**.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V211_APERTURA.txt`,
> `docs/loop/SALIDA_V211_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 211`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LOS DOS CAMPOS `estado` QUE EL ACTA 209 DEJO ADJUDICADOS: leer el acta 210 desde su linea de apertura y citar por linea; poner `OP-L-02` y `OP-L-03` en `HECHA` EN EL MISMO COMPUTO con las tres guardas del `2.c` de la 209 (sede por las dos convenciones al entrar y al salir, cuentas por `estado` antes y despues mas `git diff --numstat` sobre `docs/plan/`, y el caso positivo de recarga del `jsonl`); y LA MEDICION DEL 1357 QUE NO ARREGLA NADA: el grupo HOROWITZ contado, con su particion | **CERRADA, LAS DOS MITADES** | `SALIDA_V211_T1B_CERRAR_DOS_ESTADOS.txt`, `SALIDA_V211_T1B_CERRAR_DOS_ESTADOS_MUTADO.txt`, `SALIDA_V211_T1E_GRUPO_HOROWITZ.txt`, `SALIDA_V211_T1E_GRUPO_HOROWITZ_MUTADO.txt` |
| **TAREA 2** | `OP-I-01`, LA ULTIMA DE LAS CUATRO FICHAS REALES DE LA MORATORIA: correr la vara `vuelta150_3_relectura_expediente.py --corte HEAD` al empezar; leer la ficha entera y publicar su forma; medirla contra la fila `10 INVENTARIO` de `docs/plan/08_VERIFICACION.md` citada literal; punto por punto de su `verificacion` con cita, fichero y linea; remedir sus TRES SEDES al entrar y al salir; y RECOMPUTAR DEL FICHERO las 336 entradas que la seccion 5 de `AUDITOR.md` lleva publicadas. **El campo `estado` de `OP-I-01` NO SE TOCA** | **CERRADA COMO MEDICION, CON PARADA DECLARADA** | `SALIDA_V211_T2_OP_I_01.txt`, `SALIDA_V211_T2_VARA.txt`, `SALIDA_V211_T2_VARA_ANTES_DE_MI_1B.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS, Y LOS DOS CAMPOS `estado` QUE EL ACTA 209 DEJO ADJUDICADOS

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN con
`scripts/loop/_v211_t1_seccion.py` de `docs/loop/SALIDA_V211_T1B_CERRAR_DOS_ESTADOS.txt`,
`docs/loop/SALIDA_V211_T1B_CERRAR_DOS_ESTADOS_MUTADO.txt`,
`docs/loop/SALIDA_V211_T1E_GRUPO_HOROWITZ.txt`,
`docs/loop/SALIDA_V211_T1E_GRUPO_HOROWITZ_MUTADO.txt` y
`docs/loop/SALIDA_V211_APERTURA.txt`, **y ese compositor cae en rojo si no puede leer
una sola de ellas**. Las lineas de acta que se citan aqui las **busca el propio
compositor en `docs/loop/ACTA_AUDITOR.md`** y caen en rojo si el texto no vive en
exactamente una linea: **se leen, no se recuerdan** (`6.6` del acta 210, linea **74203**).

#### 1.a. EL ACTA 210, LEIDA Y NO REESCRITA

La seccion de la **210** abre en la linea **73924** de `docs/loop/ACTA_AUDITOR.md`,
que mi apertura mide en **4902898** bytes en disco y **4902898** normalizado
a LF, `sha256` **`7217a5d76c98d65f`** (4788.0 KB). **Calza al digito con el encargo**,
que publica **4902898** y **`7217a5d76c98d65f`**.

#### 1.b. LOS DOS CAMPOS `estado`, EN EL MISMO COMPUTO Y CON LAS TRES GUARDAS

Las dos adjudicaciones que lo mandan viven en el acta **209**: la **`6.4`** en la linea
**73760** (*"`OP-L-02` SE CIERRA. 18 DE 18"*) y la **`6.5`** en la **73765**
(*"`OP-L-03` LLEVA UNA VUELTA CERRADA POR ACTA Y SU `estado` SIGUE EN `LISTA`"*). Las
tres guardas son las que esa misma acta nombra en su linea **73763**: *"el pase se
ejecuta con las mismas tres guardas del `2.c` de esta vuelta, que salieron limpias"*.

**EL CASO ROJO SE PROBO POR MUTACION ANTES DE ESCRIBIR NADA** (`EJECUTOR.md` 1). Con el
nombre de la segunda ficha cambiado a `OP-L-99`, el computo iba a cerrar con codigo
**1** y la prueba dio **VERDE, LA GUARDA MUERDE**. Sellado en
`docs/loop/SALIDA_V211_T1B_CERRAR_DOS_ESTADOS_MUTADO.txt`.

**GUARDA (1). LA SEDE POR LAS DOS CONVENCIONES, AL ENTRAR Y AL SALIR:**

| `docs/plan/OPERACIONES.jsonl` | bytes en disco | bytes normalizado a LF | `sha256` disco | `sha256` LF |
|---|---:|---:|---|---|
| **AL ENTRAR** | **513043** | **513043** | **`e96dbe74485814e9`** | **`e96dbe74485814e9`** |
| **AL SALIR** | **513043** | **513043** | **`7a52387bb8a4aa4f`** | **`7a52387bb8a4aa4f`** |

Los bytes no se mueven porque `LISTA` y `HECHA` miden lo mismo, **y los `sha256` si
cambian**, que es lo que prueba que algo se escribio. **2 de 2**
fichas pasaron la guarda del valor viejo, las dos leyendo `LISTA` del fichero.

**GUARDA (2). SOLO CAMBIAN ESOS DOS CAMPOS.** `git diff --numstat` sobre `docs/plan/`
da **1** fila, con **2** lineas anadidas y **2** borradas.
Las dos cuentas por `estado`, las dos publicadas:

| `estado` | ANTES | DESPUES |
|---|---:|---:|
| `HECHA` | **30** | **32** |
| `LISTA` | **41** | **39** |
| **TOTAL** | **71** | **71** |

**CIFRA fichas que se movieron: 2.** **CIFRA otros `id_op` cuyo `estado`
cambio: 0.**

**GUARDA (3), EL CASO POSITIVO.** El `jsonl` se recarga linea a linea: **71**
fichas releidas del disco contra las **71** de antes, y **0** lineas que
no son JSON valido. **VEREDICTO DE LAS TRES GUARDAS: VERDE, LAS TRES.**

**LA VARA NO ES ESTE CAMPO, Y SE DICE AQUI PARA QUE NADIE LO LEA AL REVES:** el `estado`
es **HISTORICO** y no decide que queda por ejecutar (recuadro 0 de `AUDITOR.md`). Se
pone al dia porque **un campo que contradice al acta que cerro la ficha engana a quien
venga**, no porque mida nada.

#### 1.e. LA MEDICION QUE NO ARREGLA NADA, Y SE QUEDO EN MEDICION

El hallazgo `7.1` del acta 210 vive en la linea **74223**. **Lo reproduje al digito y
no toque ni un nodo:** en `dataset/metadata/master_graph.json` (**3853** nodos
contados hoy) `posicionamiento_de_empresa` tiene **CINCO** `pasos_accionables`, los de
Blank, y `la_historia_de_la_empresa` tiene los **CUATRO** de Horowitz. **Cinco mas
cuatro dan nueve.** El veredicto del **1357** NO SE TOCA: su clausula
*"El solape de este par cae en el primer bloque y el veredicto es INVARIANTE"* la cita
el acta en sus lineas **74232** y **74233**, donde la frase parte en dos.

**(a) LAS DOS PREGUNTAS DEL ENCARGO, CONTESTADAS CON MI CONTEO DE HOY.** Menciones de
`posicionamiento_de_empresa` en `docs/plan/02_DESTEJIDOS.md`: **0**, que calza
con el **0** del encargo. Operaciones de `docs/plan/OPERACIONES.jsonl` en cuyo campo
`nodos` vive: **1**, que calza con el **1** del encargo, y es
**`OP-F-04-HOR`**, `DECISION_DE_FUENTE` en **`LISTA`**, fase `01_FUENTES`,
linea **38**.

**PERO LA TERCERA CIFRA NO CALZA, Y NO LA RESUELVO COPIANDO** (`AUDITOR.md` 1.1). El
encargo dice *"con sus **13** nodos"* y la propia adjudicacion de la ficha dice *"LEIDOS
LOS 13"*. **Mi conteo de hoy del campo `nodos` da 14.** La explicacion no la
pongo yo: vive en `docs/plan/01_FUENTES.md`, que en su linea **1453** declara *"El que
sobra es `principio_calidad_mvp`"* y en su linea **1168** que una decision del fundador
*"devolvio `principio_calidad_mvp` a la operacion y la nomina volvio a CATORCE"*.
**La discrepancia queda declarada: la adjudicacion de la ficha lleva el corte viejo, y
el campo lleva el nuevo. No toco ninguno de los dos.**

**(b) LA PARTICION DE LOS 14, CONTADA Y CON SUS NOMBRES.** La vara no es mia:
es la tabla de `docs/plan/01_FUENTES.md`, **lineas 1462 a 1477**, que publica por nodo
los libros declarados y **la frontera leida** el 11 y el 14 ago 2026. De esa frontera
salen dos cifras por nodo sin teclear ninguna (el fin del bloque 1 y el total), y contra
ellas se pone la CIFRA de `pasos_accionables` de HOY. **14** filas leidas,
**0** nodos de la tabla que faltan en el campo y **0** del campo que faltan
en la tabla. **La tabla que sigue esta PEGADA ENTERA de
`docs/loop/SALIDA_V211_T1E_GRUPO_HOROWITZ.txt`, no recompuesta:**

| # | nodo | frontera leida | fin bloque 1 | total de la frontera | pasos HOY | veredicto |
|---:|---|---|---:|---:|---:|---|
| 1 | `actualizacion_posiciones_existentes` | 1 a 4 / 5 a 19 | 4 | 19 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 2 | `background_startup_vs_corporativo` | 1 a 4 / 5 a 9 | 4 | 9 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 3 | `contratacion_experiencia_vs_potencial` | 1 a 4 / 5 a 10 | 4 | 10 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 4 | `decision_de_salir_a_bolsa` | 1 a 5 / 6 a 10 | 5 | 10 | 5 | **EL BLOQUE YA VIVE APARTE** |
| 5 | `decision_de_vender_startup` | 1 a 10 / 11 a 34 | 10 | 34 | 15 | **NI UNA COSA NI LA OTRA** |
| 6 | `estrategia_de_innovacion_producto` | 1 a 3 / 4 a 7 | 3 | 7 | 3 | **EL BLOQUE YA VIVE APARTE** |
| 7 | `manejo_empleados_en_adquisicion` | 1 a 4 / 5 a 9 | 4 | 9 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 8 | `metas_vs_proposito` | 1 a 4 / 5 a 9 / 10 a 14 | 4 | 14 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 9 | `organizacion_adaptativa` | 1 a 4 / 5 a 8 | 4 | 8 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 10 | `plan_mejora_procesos` | 1 a 5 / 6 a 10 / 11 a 15 | 5 | 15 | 5 | **EL BLOQUE YA VIVE APARTE** |
| 11 | `posicionamiento_de_empresa` | 1 a 5 / 6 a 9 | 5 | 9 | 5 | **EL BLOQUE YA VIVE APARTE** |
| 12 | `principio_calidad_mvp` | 1 a 5 / 6 a 10 / 11 a 14 | 5 | 14 | 7 | **NI UNA COSA NI LA OTRA** |
| 13 | `revisiones_regulares_desempeno_ceo` | 1 a 4 / 5 a 10 | 4 | 10 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 14 | `seleccion_ceo_fundador` | 1 a 4 / 5 a 12 | 4 | 12 | 6 | **NI UNA COSA NI LA OTRA** |

**EL REPARTO: 11 con EL BLOQUE YA VIVE APARTE, 3 con NI UNA COSA NI
LA OTRA, y 0 con EL BLOQUE SIGUE DENTRO**, sobre **14** repartidos y
**0** sin medir.

**LA MUTACION, CORRIDA:** desplazando en uno el fin del bloque 1 de cada fila, el cubo
`NI UNA COSA NI LA OTRA` pasa de **3** a **14**. La comparacion
compara. Sellada en `docs/loop/SALIDA_V211_T1E_GRUPO_HOROWITZ_MUTADO.txt`.

**(c) LA PARTICION NO ES UNIFORME (NO), Y AQUI PARO, QUE ES LO QUE EL ENCARGO
MANDA.** Los tres que no calzan con ninguna de las dos son
`decision_de_vender_startup`, `principio_calidad_mvp` y `seleccion_ceo_fundador`.
**Decidir que hacer con una operacion de fuente sin destino no es de esta vuelta**, y no
lo decido.

**LO QUE NO AFIRMO, Y ES LA MITAD HONESTA DE ESTA MEDICION:** *EL BLOQUE YA VIVE APARTE*
es el nombre de **una coincidencia de cifras** (los pasos de hoy son exactamente los del
bloque 1 de la frontera de agosto), **no la prueba de que el bloque 2 exista hoy como
nodo propio**. Eso lo comprobe **para un solo nodo**, el del `7.1`, donde
`la_historia_de_la_empresa` esta y lleva los cuatro pasos. **Para los otros diez no lo
comprobe**, y por eso no lo escribo.

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

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

