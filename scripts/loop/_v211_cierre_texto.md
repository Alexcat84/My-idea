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

`AUDITOR.md` 6.3 prohibe arneses, guardas y lectores nuevos. **Los seis ficheros
que esta vuelta escribio en `scripts/loop/` llevan los seis el prefijo `_v211_`**,
o sea **fuera del censo y fuera de la nomina**, y ninguno se queda vigilando nada:
`_v211_apertura.py`, `_v211_ciclo_gate0.py`, `_v211_esqueleto.py`,
`_v211_t1b_cerrar_dos_estados.py`, `_v211_t1e_grupo_horowitz.py`,
`_v211_t1_seccion.py`, `_v211_t2_op_i_01.py` y `_v211_t2_seccion.py`.

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

**SON DOS, LAS DOS MIAS, Y LAS DOS LAS CACE YO DENTRO DE LA VUELTA.** Ninguna
llego al reporte publicado, y las declaro igual porque **una caida que no deja
rastro en disco sigue siendo una caida** y el encargo manda declararlas con nombre.

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
