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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 211`, y su salida
cruda vive en `docs/loop/SALIDA_V211_TALLADOR_CABECERA.txt` (2438 bytes en disco y 2418 normalizado a LF, 11 filas de
tabla,
contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN
INSTRUMENTO NO SE ESCRIBE.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 82 passed (82) / 1.040 passed (1.040) | **82 passed (82) / 1.040 passed (1.040)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `276b8421` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 210: LA UNICA TAREA ENTREGADA Y TODA CIFRA REPRODUCE AL DIGITO SALVO UNA CITA QUE ACREDITA AL ACTA 205 UNA CUENTA QUE VIVE EN EL 206. MI CIEGA SALIO 72 DE 80.'), HEAD real de apertura `276b8421` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `a770a58c` (leido de `SALIDA_V211_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

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
que mi apertura mide en **4902898** bytes en disco y **4902898** normalizado a LF (4788.0 KB), con `sha256` **`7217a5d76c98d65f`** en disco y **`7217a5d76c98d65f`** normalizado a LF.
**Calza al digito con el encargo**, que publica **4902898** y **`7217a5d76c98d65f`**.

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

**EL VEREDICTO DE UNA LINEA: LA VUELTA 211 ENTREGA SUS DOS TAREAS: los dos estados en HECHA con las tres guardas verdes y el rojo probado por mutacion, y OP-I-01 medida entera con PARADA declarada porque la fila 10 INVENTARIO que su criterio de hecho necesita NO EXISTE. Tres caidas propias, las tres mias, y la tercera la cace despues de cerrar en verde.**

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE ESTA SECCION CITA EL FICHERO DEL QUE SALE** (`EJECUTOR.md` 1, LA
TABLA SE CUENTA DE SU FICHERO). Las de las dos tareas ya van en su anexo, tallado
por `_v211_t1_seccion.py` y `_v211_t2_seccion.py`, y **aqui no se repiten**: lo
que va aqui es lo que ninguna de las dos tareas produjo.

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, NUNCA `run_phase1.py` A SECAS

Corrido con `scripts/loop/_v211_ciclo_gate0.py`, que **IMPORTA** los ocho comandos
de `_v205_ciclo_gate0.py` y solo le corrige el numero de vuelta, computado de su
propio nombre. **PEOR EXITCODE DE LOS OCHO: 0 en APERTURA y 0 en CIERRE.**

| # | comando | APERTURA | CIERRE |
|---:|---|---|---|
| 1 | `run_phase1.py --reaplico-curaduria` | EXITCODE 0, 4790 bytes | EXITCODE 0, 4790 bytes |
| 2 | `etiquetas_de_cara.py --aplicar` | EXITCODE 0, 7928 bytes | EXITCODE 0, 7928 bytes |
| 3 | `sync_assets_web.py` | EXITCODE 0, 574 bytes | EXITCODE 0, 574 bytes |
| 4 | `git diff HEAD --numstat` | EXITCODE 0, **0 filas**, 140 bytes | EXITCODE 0, **0 filas**, 140 bytes |
| 5 | `vuelta83_conteo_aristas.py WORK` | EXITCODE 0, 168 bytes | EXITCODE 0, 168 bytes |
| 6 | `vuelta85_medir_desfase_calibrado` | EXITCODE 0, 498 bytes | EXITCODE 0, 498 bytes |
| 7 | `engine/run_all_tests.py` | EXITCODE 0, 1131 bytes | EXITCODE 0, 1131 bytes |
| 8a | `npx tsc --noEmit` | EXITCODE 0, 7 bytes | EXITCODE 0, 7 bytes |
| 8b | `pnpm test` | EXITCODE 0, 336 bytes | EXITCODE 0, 336 bytes |

Las dieciocho celdas salen de las dieciocho salidas `SALIDA_V211_*_APERTURA.txt` y
`SALIDA_V211_*_CIERRE.txt`, y de la linea de resumen que el propio ciclo imprime.

### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES

| sede | al entrar (disco / LF) | al cerrar (disco / LF) | `sha256` de cierre (disco / LF) | la movio esta vuelta |
|---|---:|---:|---|---|
| `docs/plan/OPERACIONES.jsonl` | 513043 / 513043 | 513043 / 513043 | `7a52387bb8a4aa4f` / `7a52387bb8a4aa4f` | **SI**, la `TAREA 1.b`: mismos bytes y `sha256` distinto |
| `docs/loop/ACTA_AUDITOR.md` | 4902898 / 4902898 | 4902898 / 4902898 | `7217a5d76c98d65f` / `7217a5d76c98d65f` | NO, solo se leyo |
| `docs/plan/INVENTARIO.jsonl` | 584554 / 584554 | 584554 / 584554 | `69666b73339f2afe` / `69666b73339f2afe` | NO, solo se leyo |
| `dataset/metadata/master_graph.json` | 8375817 / 8375817 | 8375817 / 8375817 | `627cc662296f7f00` / `627cc662296f7f00` | **NO, Y ESO ES EL PUNTO DE LA `1.e`** |

**AL CIERRE, `git diff --numstat` sobre `docs/plan/`, `dataset/`, `web/` y
`engine/` da 0 filas**, porque cada tramo se commiteo al cerrarse.

### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, CONTADAS Y COMPROBADAS

**CIFRA rutas citadas: 24. CIFRA ausentes: 0. CIFRA de cero bytes: 0.** Se cuenta
porque **una ruta publicada como evidencia es CIFRA PUBLICADA** (`EJECUTOR.md` 1,
LA RUTA QUE PROMETE PRUEBA ES CIFRA), y apuntar a un fichero que no esta o que
mide cero es caida de cifra.

## 4. LO QUE SE TOCO, Y LO QUE NO

**SE TOCO UNA SOLA SEDE DEL PLAN Y DOS CAMPOS:** el `estado` de `OP-L-02` y el de
`OP-L-03` en `docs/plan/OPERACIONES.jsonl`, con `numstat` de **2 anadidas y 2
borradas en una sola fila** y **0 otros `id_op` movidos**.

**LO QUE MI APERTURA SELLADA DICE, COTEJADO CONTRA ESTA SECCION Y NO TECLEADO**
(`docs/loop/SALIDA_V211_APERTURA.txt`): **`git status --porcelain` AL ENTRAR daba
2 lineas** (CIFRA lineas de status: 2), y las dos eran mis propios computos
`_v211_` sin seguir todavia, no trabajo ajeno colgando; y
**CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0**, o sea que la
vuelta empezo con el grafo limpio.

**NO SE TOCO NI UN NODO.** La `TAREA 1.e` y la `TAREA 2` abrieron
`dataset/metadata/master_graph.json`, `docs/plan/INVENTARIO.jsonl`,
`docs/plan/10_INVENTARIO.md` y `docs/plan/08_VERIFICACION.md` **en lectura**, y
las cuatro salen del cierre con el `sha256` con el que entraron. El `estado` de
`OP-I-01` sigue en `LISTA`.

### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO

`AUDITOR.md` 6.3 prohibe arneses, guardas y lectores nuevos.

> **CORRECCION DECLARADA DENTRO DE LA PROPIA VUELTA 211, POR EL CARRIL DEL BANCO
> `9.10` Y SIN TACHAR LO QUE CORRIGE.** Lo que esta frase decia, escrito aqui
> entero: *"Los seis ficheros que esta vuelta escribio en `scripts/loop/` llevan
> los seis el prefijo `_v211_`"*. **El SEIS estaba TECLEADO y es falso.** Contado
> con `ls scripts/loop/_v211_*`: **8** ficheros `.py` y **11** en total con los
> tres `.md`. Es mi caida `C.3`.

**LOS 8 FICHEROS `.py` QUE ESTA VUELTA ESCRIBIO EN `scripts/loop/` LLEVAN LOS 8 EL
PREFIJO `_v211_`**, o sea **fuera del censo y fuera de la nomina**, y ninguno se
queda vigilando nada: `_v211_apertura.py`, `_v211_ciclo_gate0.py`,
`_v211_esqueleto.py`, `_v211_t1b_cerrar_dos_estados.py`,
`_v211_t1e_grupo_horowitz.py`, `_v211_t1_seccion.py`, `_v211_t2_op_i_01.py` y
`_v211_t2_seccion.py`. Los otros **3** son los borradores `.md` que los
compositores producen y que `anexar_tarea_al_reporte.py` y `cerrar_reporte.py`
consumen: `_v211_t1_seccion.md`, `_v211_t2_seccion.md` y `_v211_cierre_texto.md`.

**LA NOMINA DE LA BATERIA SIGUE CONGELADA EN 135 Y NO SE PODO:** esta vuelta no la
toco ni por arriba ni por abajo.

**Y NO CLONE NINGUN INSTRUMENTO, LOS IMPORTE** (acta 206 `6.5`, IMPORTAR NO ES
CLONAR): `git`, `shas` y `RAIZ` de `_v210_apertura`; los ocho comandos de
`_v205_ciclo_gate0`; `dos_convenciones` y `censo` de `_v209_t2c_cerrar_opl01`; y
las cuatro marcas del anexo de `anexar_tarea_al_reporte`.

### 4.2. LA `1.d` DEL ENCARGO, CUMPLIDA POR OMISION Y DICHA EN VOZ ALTA

La adjudicacion `6.3` del acta 210 (linea **74168** de `docs/loop/ACTA_AUDITOR.md`)
prohibe **citar un arnes de la lista `NO MORDIO` como prueba de que algo esta
vigilado**. **Esta vuelta no cita ninguno de los siete**, ni para apoyarse ni de
pasada, y las dos pruebas de mutacion que si publica son **de arneses que corri
yo hoy y que salieron mordiendo**, no de la lista apagada.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` LA PARTICION DE LA `1.e` MIDE UNA COINCIDENCIA DE CIFRAS, NO UN HECHO DEL
GRAFO, Y EL NOMBRE QUE LE PUSE ES MAS FUERTE QUE LO QUE PRUEBA.** Llamo *EL BLOQUE
YA VIVE APARTE* a que los `pasos_accionables` de hoy sean exactamente los del
bloque 1 de una frontera de agosto. **POR DONDE ME PUEDO ESTAR EQUIVOCANDO:** esa
igualdad tambien saldria si a un nodo le hubieran **podado** el bloque 2 sin
hacerlo nodo propio, que es justo lo que la `verificacion` de `OP-F-04-HOR`
prohibe (*"el bloque separado va a su familia o a nodo propio: NO se poda"*).
**Comprobe el nodo propio para UNO de los once** (el del `7.1`); para los otros
diez **no lo comprobe**, y once nodos con el bloque podado se leerian en mi tabla
igual que once bien reubicados. Lo digo en el anexo y lo repito aqui.

**`D.2` LOS TRES DE `NI UNA COSA NI LA OTRA` PUEDEN NO SER TRES ANOMALIAS SINO UNA
VARA VIEJA.** `decision_de_vender_startup`, `principio_calidad_mvp` y
`seleccion_ceo_fundador` no calzan con ninguna de las dos cifras. **POR DONDE ME
PUEDO ESTAR EQUIVOCANDO:** los tres son **exactamente los que el propio
`01_FUENTES.md` marca como raros** (dos de ellos con frontera de TRES bloques y el
tercero entre "LOS TRES CASOS QUE NO SON UN SIMPLE APENDICE"), asi que su
desajuste puede ser **de mi vara**, que solo mira el primer y el ultimo tramo, y
no del grafo. **Por eso no los llamo anomalias y paro**, que es lo que el encargo
manda.

**`D.3` EL VEREDICTO `NO CUBRE` DEL PUNTO 2 DE `OP-I-01` LO SOSTENGO SOBRE UNA
LECTURA LITERAL DE "INCOMPLETA".** El punto dice *"toda forma con cobertura
incompleta va marcada PROVISIONAL"* y yo leo *incompleta* como **N menor que M en
`N de M pares leidos`**, que da 95 sin marca. **POR DONDE ME PUEDO ESTAR
EQUIVOCANDO:** el campo `estado` de esas entradas si dice cosas como *"repite,
acto ABIERTO"*, y **puede que la casa considere ESE el marcado equivalente** y la
palabra PROVISIONAL este reservada a los `racimo`, que son las tres unicas que la
llevan. Si es asi, mi `NO CUBRE` deberia ser `A MEDIAS`. **No lo decido yo.**

**`D.4` DECLARO PARADA EN EL PASO 2 DE LA `TAREA 2` EN VEZ DE USAR EL CRITERIO
GENERAL, Y SE PUEDE ARGUMENTAR QUE ME PASE DE PRUDENTE.** El fichero titula su
criterio **"EL CRITERIO DE HECHO, y es uno solo"**, lo que se puede leer como que
la tabla `POR FASE` **detalla** un criterio que ya aplica a todas. **POR DONDE ME
PUEDO ESTAR EQUIVOCANDO:** con esa lectura no habria parada, solo una fila que
falta. **Pare igual** porque el encargo dice *"contra ella y no contra tu idea de
lo que la ficha deberia ser"*, y elegir cual de las dos lecturas vale **es
exactamente la idea propia que esa frase prohibe**.

## 6. LAS PREGUNTAS

**`P.1` LA FILA `10 INVENTARIO` NO EXISTE, Y NO SE SI FALTA O SI NO DEBE EXISTIR.**
La tabla `POR FASE` de `docs/plan/08_VERIFICACION.md` llega a `07 ADUANA`, y el
plan tiene fases **09** y **10** con fichas vivas. **La pregunta es de dos filos:**
si a esas fases les falta su fila, `OP-I-01` **no se puede cerrar contra nada**; y
si no les corresponde tenerla, entonces **el criterio de hecho de una ficha de fase
10 es el general** y conviene escribirlo, porque hoy hay que deducirlo.

**`P.2` EL CAMPO `nodos` DE `OP-F-04-HOR` DICE 14 Y SU PROPIA `adjudicacion` DICE
13.** Las dos cifras estan en la misma ficha y se contradicen. `01_FUENTES.md`
explica el porque (el 14.º volvio por decision del fundador), pero **la
adjudicacion no se actualizo**, y es la misma especie que el acta 209 arreglo con
los dos `estado`: **un campo que contradice a su vecino engana a quien venga.**
No lo toco.

**`P.3` LA VARA DEL TRABAJO PENDIENTE LEE EL CAMPO `estado`, Y EL RECUADRO 0 DICE
QUE ESE CAMPO NO MIDE NADA.** Mi `TAREA 1.b` puso al dia dos campos historicos y
**la vara cambio de cifra**: 5 en `LISTA` sin prueba pasaron a 3, y 3 de trabajo
real a 1. Las dos fichas no se ejecutaron mas ni menos por eso. **La pregunta:
que una vara que la casa declara canonica se mueva al tocar un campo que la casa
declara historico, es contradiccion o es correcto y solo lo parece.**

## 7. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Todo lo que esta vuelta encontro sin regla vigente se registro
como pregunta (`P.1` a `P.3`) o como parada declarada, que es lo que
`EJECUTOR.md` 5 manda cuando la regla no existe: **no parar, registrar lo mejor
sostenido y seguir.**

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**SON TRES, LAS TRES MIAS, Y LAS TRES LAS CACE YO.** Las dos primeras dentro de
la vuelta y antes de publicar nada; **la tercera DESPUES de cerrar el reporte en
verde**, al recontar un fichero que la prosa nombraba de memoria, y por eso el
reporte se reconstruyo entero desde su esqueleto. Las declaro todas porque **una
caida que no deja rastro en disco sigue siendo una caida**.

**`C.1`. LLAME UNIFORME A UNA PARTICION QUE NO HABIA PODIDO MEDIR, Y ES UN FALSO
VERDE DE LIBRO.** Mi primer barrido de la tabla de `01_FUENTES.md` partia las
filas por `|` a secas, y esa tabla lleva **pipes escapados** (`Wasserman \|
Horowitz`) en la celda de libros, asi que las columnas corrieron una plaza y la
frontera salio ilegible en **las catorce filas**. Las catorce cayeron en un solo
cubo, `SIN FRONTERA LEGIBLE`, y **mi guarda leyo "un solo cubo" como PARTICION
UNIFORME y lo publico en verde**. Es exactamente la especie del banco `9`: la
degradacion silenciosa que no deja sintoma. **EL REMEDIO, ya en el codigo:** el
barrido respeta el escape, y **se anadio una guarda que prohibe escribir la
palabra UNIFORME si queda un solo nodo sin medir**, porque un reparto que no pudo
medir nada no es uniforme, es un reparto que no existe.

**`C.2`. TECLEE UNA CIFRA EN EL COMPOSITOR QUE EXISTE PARA NO TECLEAR CIFRAS.** En
`_v211_t2_seccion.py` puse `"r_hoy": "672"` a mano, en un fichero cuyo propio
docstring dice **NINGUNA CIFRA SE TECLEA**. Era la cifra correcta, y eso no la
salva: `EJECUTOR.md` 1 no prohibe equivocarse de numero, prohibe **el numero que
no sale de un instrumento**. **EL REMEDIO, ya en el codigo:** se lee de
`SALIDA_V211_T2_OP_I_01.txt` como las otras cuarenta y tantas, con la correccion
declarada en el propio fichero y sin borrar lo que corrige.

**`C.3`. ESCRIBI "LOS SEIS FICHEROS" Y ERAN OCHO, EN LA SECCION QUE EXISTE PARA
DECIR QUE NO ROCE LA MORATORIA.** La `4.1` publicaba **seis** y a continuacion
**listaba ocho nombres**, o sea que la frase se desmentia a si misma en su propia
linea. **Nadie me cazo:** ninguna guarda mira esa cifra, porque es prosa que no
cita fichero de salida, y por ahi es justo por donde entraron las caidas de las
vueltas 74 a 76 que obligaron a tallar las tablas. **La cace yo al recontar
`ls scripts/loop/_v211_*` despues de cerrar el reporte, y por eso el reporte se
reconstruyo entero desde su esqueleto en vez de parchearse.** **EL REMEDIO:** la
cifra se recuenta y la frase vieja queda escrita entera arriba, con la
correccion declarada al lado. **Es la peor de las tres**, porque las otras dos
las mordio un instrumento y esta no la mordio nada.

**LO QUE NO CUENTO COMO CAIDA, Y DIGO POR QUE:** el rechazo del tallador por falta
de `SALIDA_V211_HEAD_CIERRE.txt` **no es una caida, es la guarda funcionando**: el
sello del HEAD de cierre no puede existir antes de la ultima operacion, y el
tallador esta escrito para negarse hasta que exista. Y el heredoc de comillas
simples que se cayo al escribir el esqueleto **es la trampa del entorno que el
propio encargo declara**; use la herramienta de fichero, como el encargo permite, y
lo digo aqui porque el encargo pide decir cual use.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**LAS CUATRO FICHAS REALES DE LA MORATORIA ESTAN AGOTADAS COMO TRABAJO DE
EJECUTOR:** `OP-L-01`, `OP-L-02` y `OP-L-03` cerradas por acta y con su campo al
dia, y `OP-I-01` **medida entera y trabada por una fila que no existe**. Lo que
queda no es medicion, son **tres decisiones que no me tocan**: la fila
`10 INVENTARIO` (`P.1`), la `adjudicacion` de `OP-F-04-HOR` que dice 13 sobre un
campo de 14 (`P.2`), y el destino de los tres injertos que no calzan (`D.2`).
**La 212 puede cerrarse en una sola tarea de lectura si el acta contesta esas
tres**, y la bateria sigue en la **215** por la cadencia de `AUDITOR.md` 6.1.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 211 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V211_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: NADIE la corrio, y no por olvido: la 211 NO ES VUELTA DE BATERIA. La cadencia de cinco de AUDITOR.md 6.1 pone la siguiente en la 215, y el encargo de esta vuelta lo escribe con todas las letras.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
