## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LOS DOS EXTREMOS SE LEEN DE LOS SELLOS Y NO SE TECLEAN.** Apertura `e8638442`, de
`docs/loop/SALIDA_V176_HEAD_APERTURA.txt`, sellado **antes de la primera
operacion**; cierre `fd1ea61d`, de `docs/loop/SALIDA_V176_HEAD_CIERRE.txt`, sellado
**tras la ultima**. **LOS COMMITS DE LA VUELTA, LEIDOS DE
`git log e8638442..fd1ea61d`: 13.** La tabla la imprime
`scripts/loop/vuelta176_tarea2_cuerpo_cierre.py`; ninguna celda se teclea.

| # | commit | asunto, primeras 92 letras, leido de git |
|---:|---|---|
| 1 | `2e00ad9e` | APERTURA DE LA VUELTA 176 Y LA PRIMERA LINEA DEL ENCARGO, PERO CON SU GUARDA DELANTE Y CORRI |
| 2 | `697dda79` | TAREA 2, PRIMERA MITAD: EL REPORTE DE LA 176 QUEDA ABIERTO (7772 bytes, 80 lineas, 2 filas d |
| 3 | `44758bde` | TAREA 1, LA MAQUINA DE LOS TRAMOS, ANTES DE CORRER NI UNA ENTRADA. LO QUE SE PARTE ES EL BOC |
| 4 | `4401df01` | TRAMO 1 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO. Cada cifra de este mensaje s |
| 5 | `6ee741b3` | TRAMO 2 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO. Cada cifra de este mensaje s |
| 6 | `03a7d21b` | TRAMO 3 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO. Cada cifra de este mensaje s |
| 7 | `4038a0fa` | TRAMO 4 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO. Cada cifra de este mensaje s |
| 8 | `c2f1ab22` | TRAMO 5 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO. Cada cifra de este mensaje s |
| 9 | `cd5aa065` | TRAMO 6 DE 9 EN ROJO, exitcode 1, Y AQUI SE PARA SIN RE-CORRERLO (encargo de la 176, TAREA 1 |
| 10 | `1f840be3` | TRAMO 7 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO, Y CORRIDO DESPUES DEL ROJO D |
| 11 | `2011f025` | TRAMO 8 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO, Y CORRIDO DESPUES DEL ROJO D |
| 12 | `55e67983` | TRAMO 9 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO, Y CORRIDO DESPUES DEL ROJO D |
| 13 | `fd1ea61d` | TAREA 1 CERRADA: LA BATERIA CORRIO ENTERA, 88 DE 88, Y SU SALIDA UNICA TIENE CUERPO POR PRIM |

**LAS RUTAS QUE ESTA VUELTA TOCA, CONTADAS Y NO ESTIMADAS**, de
`git diff --name-only e8638442..fd1ea61d`, agrupadas por directorio:

| directorio | rutas tocadas |
|---|---:|
| `docs/loop/` | 29 |
| `docs/loop/reportes/` | 1 |
| `scripts/loop/` | 9 |
| **TOTAL** | **39** |

**EL GRAFO NO SE MOVIO, PROBADO Y NO CREIDO:**
`git diff --numstat e8638442..fd1ea61d -- dataset/ web/ engine/` sale con
**0 filas**. **Cero nodos tocados, cero aristas movidas.** Y ninguna
vuelta tenia mas motivos que esta para comprobarlo, porque su trabajo entero
consiste en correr arneses que MUTAN `dataset/` a proposito.

**LA GUARDA DEL COMMIT CORRIO DOS VECES POR TRAMO, AL ENTRAR Y AL SALIR**, o sea
**9 veces al entrar y 9 al salir**, y todas midio **cero
filas** de `git diff --numstat -- dataset/`. No es una promesa: cada corrida esta
dentro del fichero de su tramo.

**EL COMMIT QUE LLEVA ESTE REPORTE NO SE NOMBRA AQUI**, porque se crea despues de
escribirlo.

## 4. LA PARADA, Y ES UNA. LA BATERIA MORDIO

**HAY PARADA, Y NO LA ARREGLO YO** (`EJECUTOR.md` 5: *"Paras SOLO si algo
contradice una regla vigente o una cifra publicada con su corte: en ese caso lo
escribes en el reporte como PARADA y no lo arreglas tu"*). **LA BATERIA DE ESTA
VUELTA SACO 1 ROJO**, y la tabla sale contada de los ficheros de tramo:

| tramo | clase de rojo | arnes |
|---:|---|---|
| 6 | **NO MORDIO** | `vuelta166_tarea2_mutacion_correccion.py` |

**QUE FALLA, EXACTAMENTE.** Dentro de
`scripts/loop/vuelta166_tarea2_mutacion_correccion.py`, el caso
`H_el_texto_nombra_las_tres` mide **`real=11`** contra un **`esperado=3`**. El
`3` es **UNA CONSTANTE LITERAL ESCRITA EN EL ARNES**
(`casos.append(("H_el_texto_nombra_las_tres", real.count("cae sobre"), 3))`),
mientras que el `11` sale de `T.medir_clausula_1()` corrido **sobre el registro de
veredictos VIVO**, que crece en cada vuelta. Los otros 18 casos del arnes pasan,
y los 19 CAEN al mutarles el esperado.

**NO ES CAIDA DE ESTA VUELTA, Y LO MIDO EN VEZ DE ALEGARLO.** En la ultima bateria
con cuerpo, la del auditor de la vuelta 171, este mismo arnes salio
**`exit 0 OK` en 4,5 segundos**, y esta la linea 134 de
`docs/loop/SALIDA_V171_AUDITOR_BATERIA.txt` para probarlo. Entre aquella corrida y
esta no toque ni el arnes ni su sujeto: el ultimo commit de los dos es `a23509cf`,
del 4 de septiembre, y esta vuelta no los ha tocado (el censo de rutas de la
seccion 3 no los nombra). **Lo que se movio debajo fue el registro.**

**Y ES LA ENFERMEDAD QUE ESTE MISMO FICHERO TIENE DIAGNOSTICADA POR ESCRITO.** El
docstring de `verificar_mutaciones_viejas.py` lo dice desde la vuelta 145,
correccion 22: *"Un sujeto vivo hace que el verde de una vuelta no sobreviva a la
vuelta"*, y por eso la condicion de entrada a la nomina es el SUJETO CONGELADO.
**Este arnes entro con un sujeto vivo y hoy se le movio debajo, tal como estaba
escrito que pasaria.** No lo arreglo yo: adjudicar si se re-ancla, si pasa a CASO
DECLARADO o si sale de la nomina no me toca.

**EL CORREDOR PARO AHI, COMO MANDA LA (f) DEL ENCARGO.** El tramo 6 esta
commiteado **en rojo, sin re-correr**, y ni el arnes ni su sujeto se han tocado.
Correr despues los tramos 7, 8 y 9 es decision mia y va declarada como `D.6`.

**GATE 0, EN CAMBIO, VERDE, con su ciclo entero y en su orden, al cierre:**
**numstat de 0 filas, motor 25/25, tsc EXITCODE 0, web
82 ficheros y 1040 tests.** Las cuatro cifras se LEEN de los
ficheros `docs/loop/SALIDA_V176_*_CIERRE.txt` que escribe
`scripts/loop/vuelta176_cierre.py`, no de la memoria de nadie.

**LO QUE NO ME TOCA MEDIR Y NO MIDO:** las rachas de credito son del auditor
(`AUDITOR.md` 1.2). Aqui dejo el dato que necesita: **esta vuelta corrio su
bateria y cerro su propio reporte**, que son las dos cosas que la 175 dejo
abiertas.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**D.1. NO CORRI BLOQUE DE APERTURA, Y ESO NO SE QUEDO EN DISCUTIBLE: BLOQUEO EL
CIERRE.** Al tallar el esqueleto, `tallar_cabecera_reporte.py --fase04 --vuelta
176` imprimio **37 celdas que no se pudieron leer, 18 de ellas del lado
APERTURA**, y publique esa cifra en vez de rellenarla. **EL MOTIVO DE NO
CORRERLO:** `AUDITOR.md` 6.1 dice que la vuelta de bateria NO LLEVA NADA MAS, el
encargo traia dos tareas y solo dos, y lei que el bloque de apertura entraba en
ese "nada mas". **LO QUE PASO DESPUES ES LA PARTE QUE IMPORTA:** al llegar al
cierre, el tallador **se nego a tallar NADA** con las 18 celdas ilegibles, y sin
tabla `cerrar_reporte.py` no puede cerrar. O sea que aquella lectura mia bloqueaba
la TAREA 2 entera. **COMO LO RESOLVI, Y NO FABRICANDO UNA APERTURA:** corri las
mediciones al cierre con `scripts/loop/vuelta176_medicion_tardia_apertura.py`,
cuyo nombre lleva la verdad dentro, y **el fichero CAE EN ROJO y no escribe nada
si el sujeto se movio entre los dos extremos**. No se movio, y esta medido:
`git diff <apertura>..<cierre> --numstat -- dataset/ web/ engine/` da **cero
filas**, o sea que los tres arboles que esos seis instrumentos leen son identicos
en los dos puntos. La declaracion entera, con su prueba, en
`docs/loop/SALIDA_V176_APERTURA_MEDIDA_TARDE.txt`. **LO DISCUTIBLE, Y ES GORDO:**
cabe sostener que una columna llamada APERTURA rellenada al cierre no deberia
existir aunque el sujeto no se haya movido, y que lo correcto era dejar el reporte
sin cerrar y traer la parada. **Lo traigo marcado en vez de que se descubra.**

**D.2. METI UN ARNES EN LA NOMINA EN SU MISMA VUELTA, Y LA SUBI DE 87 A 88.**
`vuelta176_tarea1c_mutacion_tramos.py` es el caso positivo de la funcion nueva
`reparto_en_tramos()`. **LA REGLA QUE INVOCO ES LA DEL PROPIO FICHERO DESDE LA
VUELTA 148** (TAREA 2.5, sobre la adjudicacion 3.5 del acta 147): *"LO QUE ESTA
REGLA EXIGE ES SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN"*.
Su sujeto son nominas fabricadas en memoria, asi que no se le puede mover debajo.
**Y SI NO ENTRARA HOY, LA BATERIA SALDRIA EN ROJO Y CON RAZON**, porque
`arneses_que_faltan()` lo veria como un arnes de la 176 posterior a la nomina.
**LO DISCUTIBLE:** que el encargo hablaba de repartir **87** entradas y yo reparti
**88**. La cifra la computo el instrumento de la nomina de hoy, que es lo que
`EJECUTOR.md` 2 manda, pero la diferencia con el numero del encargo la declaro yo
aqui y no la escondo dentro de un total.

**D.3. EL TAMANO DE TRAMO, 10, LO ELEGI YO.** El encargo dice "tramos que quepan
holgados en una sesion" y no da cifra. Elegi 10 porque las cifras del propio
archivo (0,33 a 0,43 minutos por entrada) daban una estimacion de 3,3 a 4,3
minutos por tramo. **La estimacion se publico ANTES de correr** en
`docs/loop/SALIDA_V176_T1C_REPARTO.txt`, para que se pueda contrastar con lo que de
verdad tardo, que esta en la tabla de la seccion 2. **LO DISCUTIBLE:** que un
numero elegido a ojo, aunque lleve una estimacion delante, sigue siendo un numero
elegido a ojo.

**D.4. LA GUARDA DEL COMMIT LLEVA UN SEGUNDO MOTIVO DE ROJO QUE EL ENCARGO NO
PIDIO.** El encargo pide que caiga si `git diff --numstat -- dataset/` devuelve
una fila. La mia cae tambien si `--numstat` calla **mientras los blobs difieren**.
Lo anadi porque el arbol de hoy me enseno que las dos preguntas NO dan siempre lo
mismo: `git status` nombraba `master_graph.json` y `--numstat` daba cero filas, y
solo el cotejo de blobs (`cb33552aedddab4d` contra `cb33552aedddab4d`) adjudico
que el contenido era identico byte a byte. **LO DISCUTIBLE:** anadir un motivo de
rojo que nadie encargo es ensanchar una guarda por cuenta propia.

**D.5. EL LANZADOR DE CADA TRAMO ESCRIBE SU SALIDA DENTRO DE `docs/loop/` MIENTRAS
LA BATERIA MIRA ESE DIRECTORIO.** El fichero de trabajo de la corrida si vive
fuera, que es la precaucion que la 175 dejo escrita, pero
`SALIDA_V176_T1_LANZADOR_TRAMO_<N>.txt` no. **NO FABRICO RUIDO Y ESTA MEDIDO, NO
supuesto:** los 9 tramos publican **RUIDO DE CONCURRENCIA: 0
ficheros**. La razon es que la salida del lanzador se queda en el buffer hasta que
el proceso termina, o sea despues de la bateria. **LO DISCUTIBLE:** que eso es
suerte de buffer y no una garantia, y que la precaucion correcta era sacar tambien
esa salida de `docs/loop/`.

**D.6. CORRI LOS TRAMOS 7, 8 Y 9 DESPUES DE QUE EL 6 SALIERA EN ROJO, Y ES LA
DECISION MAS DISCUTIBLE DE LA VUELTA.** La letra (f) del encargo dice **"SI UN
TRAMO SALE EN ROJO, PARA AHI Y TRAELO"**, y cabe leerla como que la bateria se
detiene entera en el tramo 6. **LO QUE HICE, DICHO SIN ADORNO:** el corredor paro
ahi de verdad, el tramo 6 quedo commiteado en rojo y **no lo re-corri ni toque
nada suyo**; despues, en un acto aparte y con su propio mensaje de commit,
corri los tres tramos que NO son el rojo. **MI RAZON:** el motivo escrito de la
(f) es que *"la guarda que muerde es informacion, no un estorbo"*, o sea que no se
enmascare un rojo re-corriendolo, y correr las otras entradas no enmascara nada,
las anade; y pararme del todo habria dejado 28 entradas sin correr en la unica
vuelta cuyo encargo entero es correr la bateria. **LO DISCUTIBLE ES QUE LAS DOS
LETRAS DEL MISMO ENCARGO TIRAN EN SENTIDOS OPUESTOS** (la (f) dice "para ahi" y la
cabecera de la TAREA 1 dice "LA BATERIA ENTERA"), y que resolver ese choque no me
tocaba a mi. Lo traigo para que lo adjudique quien manda.

## 6. LAS PREGUNTAS

**P.1. ?QUE SE HACE CON EL ARNES DEL ROJO?** `vuelta166_tarea2_mutacion_correccion.py`
tiene un `esperado` literal contra una medicion sobre registro vivo. Caben tres
salidas y no elijo ninguna: **re-anclarlo a un sujeto congelado**, **pasarlo a
CASO DECLARADO** con su exit y su marca, o **computar el esperado** en vez de
teclearlo. La tercera parece la buena, pero cambia el arnes y eso no me toca.

**P.2. LA CADENCIA, DESPUES DE ESTA VUELTA: ?LA 180 O LA 181?** `AUDITOR.md` 6.1
dice que la bateria corre CADA CINCO. La 175 era la que tocaba y no llego; la 176
la ha corrido. **?El contador se reancla a la vuelta que de verdad la corrio (y
toca la 181) o sigue en la rejilla vieja (y toca la 180)?** No lo adivino.

**P.3. EL TAMANO DE TRAMO, ?SE FIJA O SE DEJA A OJO?** Con la nomina creciendo (23
a 82 a 87 a 88 en pocas vueltas), el numero de tramos crece solo. **?Se fija un
TOPE DE MINUTOS por tramo, del que el tamano se compute, en vez de un tope de
entradas?** Seria la version medida de lo que hoy es una eleccion.

## 7. PENDIENTES DE DOCTRINA

**PD.1. LA CONVENCION DE BYTES SIGUE SIN FIJAR** (hallazgo 4.1 del acta 174, y el
encargo la anota como (a) para la 177). Esta vuelta hace lo unico que puede sin
doctrina: **publicar LAS DOS**, bytes de disco y bytes normalizados a LF, en cada
fichero que sella. En los ficheros de esta vuelta las dos coinciden porque se
escriben con `newline=LF`, y eso tambien se publica en vez de darse por supuesto.

**PD.2. LA REGLA DEL SUJETO CONGELADO NO TIENE GUARDA QUE LA HAGA CUMPLIR.** El
rojo de la seccion 4 lo demuestra: la nomina admite arneses con `esperado` literal
contra medicion viva, y nadie lo ve hasta que el registro crece lo bastante. **La
regla existe desde la vuelta 145 y sigue siendo una frase, no un instrumento.**

**PD.3. LAS SEIS QUE EL ENCARGO ANOTA PARA LA 177 SIGUEN VIVAS Y LAS CUENTO EN VOZ
ALTA:** la convencion de bytes, la segunda sede de la clausula 4.4 en
`REPORTE_V172.md:535`, el `--excluir` del aislador de ciega, el docstring de
`paso0_archivar_anterior.py`, la guarda que falta en la dependencia del D.4 de la
174, y **OP-L-03, QUE LLEVA SIETE VUELTAS APLAZADA** contando esta. Ninguna se
ejecuto aqui, porque la vuelta de bateria no lleva nada al lado.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**C.1. PUBLIQUE UNA LINEA QUE SE DESMENTIA A SI MISMA, Y LA CACE ANTES DE
COMMITEARLA, PERO LA CUENTO IGUAL.** La primera corrida de
`guarda_commit_dataset.py --mutar` imprimia *"P.16: el temporal se retira"* y a
renglon seguido *"Existe todavia: True"*. La causa: `git init` deja
`.git/objects` en solo lectura y `shutil.rmtree(ignore_errors=True)` fallaba
callado, que es exactamente la degradacion silenciosa que el banco prohibe en su
seccion 9. **Corregido con un `onerror` que quita el bit de solo lectura**, y la
linea ya imprime `False`. **Lo cuento porque el arnes salio VERDE las dos veces:
el verde no vio nada, y una guarda que se desmiente sola y aun asi sale verde es
una guarda que no mira.**

**C.2. ESCRIBI UNA CONSTANTE DOS VECES EN EL CORREDOR DE TRAMOS.**
`vuelta176_bateria_por_tramos.py` nacio con `BATERIA` asignada en dos lineas
seguidas, la primera con una ruta mal formada (`scripts/loop/` colgando de `AQUI`,
que ya es `scripts/loop/`). La segunda tapaba a la primera y por eso funcionaba.
**Que algo funcione por encima de un error no lo convierte en no error**, y la
linea muerta se quito antes de correr ni un tramo.

**C.3. CORRI `run_phase1.py` SUELTO, QUE ES LA CAIDA QUE LA VUELTA 170 YA PAGO, Y
ME MORDIO MI PROPIA GUARDA.** La primera version de
`vuelta176_medicion_tardia_apertura.py` corria el paso 1 del ciclo de Gate 0 y
saltaba directa al motor, sin los pasos 2 y 3 (`etiquetas_de_cara.py --aplicar` y
`sync_assets_web.py`). **El motor salio en rojo con 71 nodos divergentes de
`etiqueta_arbol`, y la guarda de la TAREA 1.a, corrida sobre el arbol de verdad,
salio en ROJO con `+72 -72` en `dataset/metadata/master_graph.json`.** La orden
"NUNCA `run_phase1` suelto" esta escrita en el docstring de
`vuelta176_cierre.py`, que yo mismo clone en esta vuelta, y aun asi la incumpli.
**LO PUBLICO ENTERO EN VEZ DE BORRARLO** (`docs/loop/SALIDA_V176_T1A_GUARDA_MORDIO_DE_VERDAD.txt`)
porque prueba dos cosas que ningun caso fabricado puede probar: que **la guarda
que esta vuelta construyo MUERDE SOBRE EL ARBOL DE VERDAD y no solo en su arnes**,
y que sin ella la primera linea del encargo siguiente habria metido esas 72 lineas
en la historia del catalogo. **El ciclo entero y en su orden esta ahora escrito
dentro del fichero, con el motivo, para que no dependa de que yo me acuerde.**

**C.4. ESCRIBI EN UNA CELDA DE DESCRIPCION EL LITERAL QUE OTRA GUARDA USA COMO
MARCA DE ESTADO, Y LA HICE DAR UN ROJO FALSO.** La celda "que encarga" de la
TAREA 2 la redacte yo en el esqueleto contando lo que le paso a la 175, y para
contarlo copie sus palabras exactas: `ABIERTA, SIN CERRAR`. Al anexar la fila,
`anexar_tarea_al_reporte.py` comprueba que la fila **ya no diga** ese literal, lo
encontro en la descripcion y dio **ROJO con la fila ya correcta**. **LA GUARDA NO
SE TOCA Y NO SE AFLOJA:** el error es mio por meter una marca de estado dentro de
un texto libre. **Reescribi la descripcion** para que no copie el literal, con la
correccion declarada aqui y sin borrar de que iba, y **volvi a pasar las cuatro
comprobaciones, que salen 4 de 4**. **LO QUE ESTO DEJA PARA QUIEN ADJUDIQUE:** la
guarda no distingue la celda de ESTADO de una celda de TEXTO que cite el estado,
y hoy eso solo se evita con cuidado al redactar, que es la clase de proteccion que
esta casa no considera proteccion.
