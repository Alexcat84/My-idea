# REPORTE DE LA VUELTA 215 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v215_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 214.**
> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **CINCO TAREAS, Y LA 215 SI ES VUELTA DE BATERIA.** La cadencia de cinco de
> `AUDITOR.md` 6.1 pone la bateria aqui, y el acta 214 adjudica en su **linea
> 76149** que **son ONCE tramos y no nueve**: *"LA BATERIA SE DECLARA CORRIDA CON
> TODOS LOS TRAMOS DE SU REPARTO, Y HOY SON ONCE, NO NUEVE"*. **El tope de
> sub-tareas es CINCO** (acta 212, adjudicacion `6.8`, **linea 75168** de
> `docs/loop/ACTA_AUDITOR.md`, leida en esta vuelta), y **estas cinco lo agotan**.
> La bateria cabe al lado del cierre integral porque **el cierre integral NO es
> trabajo de plan, es VERIFICACION**: esta vuelta no escribe ni un nodo, ni un
> veredicto, ni una ficha.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado: **las cinco tareas son BATERIA y VERIFICACION**, que
> es lo que la moratoria protege. Todo lo que esta vuelta escribe en el arbol
> scripts/loop (**sin comillas inversas, por la obligacion del `6.2` del acta
> 212**) son ficheros `_v215_*` **con prefijo de guion bajo, fuera del censo y
> fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda.
>
> **RIGE LA OBLIGACION DE DICTADO DEL `6.6` DEL ACTA 210:** toda cita de un acta
> anterior lleva **LA LINEA** de `docs/loop/ACTA_AUDITOR.md` donde vive el texto
> citado, **y la linea se LEE, no se recuerda**.
>
> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado
> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.
>
> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO DEL ACTA 212, LAS TRES SIN CODIGO:**
> ningun reporte cita un directorio a secas como ruta entre comillas inversas
> (adjudicacion `6.2`, **y es la `C.1` que esta vuelta no repite**); una seccion
> suplementaria va detras de la que amplia y nunca detras de una mayor (hallazgo
> `7.1`); y el tallador de cabecera corrido en la apertura escribe en un nombre
> con `_RECHAZO`, no en el del cierre.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V215_APERTURA.txt`,
> `docs/loop/SALIDA_V215_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre. **Y esta vuelta anade
> el remedio del hallazgo `3.1` del acta 214: el ciclo SELLA SU PROPIA CONSOLA en
> `docs/loop/SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt`, que es el nombre
> exacto que el compositor busca.** En la 214 esa consola NUNCA EXISTIO y la
> seccion 3.1 salio publicada VACIA.
>
> **Y LA APERTURA SELLA ADEMAS DE QUE VUELTA SON LOS SELLOS DE TRAMO QUE HAY EN EL
> ARBOL AL ENTRAR**, con su commit y su fecha leidos de `git log`, que es lo que
> la TAREA 2.a manda publicar ANTES de correr nada.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 215`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, Y VA PRIMERA PORQUE LAS DEMAS SE APOYAN EN ELLA. Leer el acta de la vuelta 214 en `docs/loop/ACTA_AUDITOR.md`, sus secciones 3 y 5, y REGISTRAR LAS NUEVE ADJUDICACIONES CON LA LINEA DE DONDE SALE CADA UNA, aplicando como orden las cinco que el encargo nombra; y registrar el hallazgo `3.1` del auditor contra el reporte de la 214, que es la unica caida no declarada y la unica que acumula | **CERRADA** | SALIDA_V215_T1_REGISTROS.txt (9 adjudicaciones y 2 hallazgos con su linea), SALIDA_V215_T1_MUTANTES.txt (6 de 6 caen, texto bueno en 0 fallos), SALIDA_V215_COMPOSITOR_T1.txt |
| **TAREA 2** | LA BATERIA ENTERA, POR TRAMOS, Y SIN EL FALSO VERDE. Publicar ANTES de correr nada de que vuelta son los once sellos que hay en el arbol, con su commit y su fecha leidos de git log; NO usar el carril de la senal de arranque, que hoy publica un verde que no es de esta vuelta; y correr los ONCE tramos uno a uno con su doble corrida, su reloj y su salida sellada, commiteando cada salida al terminar su tramo | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 3** | EL CIERRE INTEGRAL, TODO LO QUE NO NECESITA CREDENCIAL: el ciclo entero de Gate 0 por los dos lados con su consola SELLADA y sus dieciocho salidas en disco; las tres suites con su exitcode y sus bytes; el inventario de las 71 fichas contra sus pruebas con el hash de la apertura; y el marcador y el censo recomputados, cada uno con su comando y con las cifras del auditor al lado para cotejar y NO para copiar | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 4** | LOS DOS PUNTOS QUE `OP-I-01` DEJO EN A MEDIAS, Y NO SE CIERRAN A OJO. El punto 3 por su NEGATIVA, que si se puede citar: se corre la busqueda y se publica su CERO con el comando delante. Y el punto 4 midiendo ANTES de decidir: buscar cual es el instrumento y cual el fichero que SI regeneran la vista humana, publicar la busqueda con su comando, y solo entonces decir si CUBRE, queda A MEDIAS o NO CUBRE. SIN mover el campo estado de ninguna ficha | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 5** | EL REPORTE, Y SU SECCION 3.1 ESTA VEZ CON CIFRAS DENTRO. Sellar la consola del ciclo de Gate 0 por los dos lados en los nombres que el compositor busca, y sobre todo hacer que EL COMPOSITOR CAIGA EN ROJO SI NO LA ENCUENTRA: el de la 214 escribio una fila en blanco y siguio, que es degradacion silenciosa y es lo que el banco 9 prohibe. Y la seccion 9 cierra con LA BATERIA CORRIDA, no con hueco declarado, porque esta es su vuelta | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS, Y LA LINEA DE CADA UNO LEIDA HOY

**LA FUENTE ES EL ACTA Y EL LECTOR ES UN INSTRUMENTO.**
`scripts/loop/_v215_t1_registros.py` abre `docs/loop/ACTA_AUDITOR.md`
(**76237** lineas hoy), localiza el acta de la vuelta 214 por su
cabecera en la **linea 75878**, y saca sus entradas numeradas con
`enumerate()`. **NINGUN NUMERO DE LINEA DE ESTA SECCION SE TECLEA**, que es lo
que manda el `6.6` del acta 210 y la letra de `EJECUTOR.md` 1.

#### 1.a. LAS NUEVE ADJUDICACIONES, CON SU LINEA Y CON LO QUE ME OBLIGAN A HACER

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V215_T1_REGISTROS.txt`: 9. FILAS QUE DEBERIA HABER,
CONTADAS POR EL PROPIO INSTRUMENTO SOBRE EL ACTA: 9.** **LAS DOS SE
ESCRIBEN JUNTAS**, por la obligacion de las filas.

| adjudicacion | linea del acta | titulo, VERBATIM del acta | que me obliga a hacer en esta vuelta (LECTURA MIA) |
|---|---:|---|---|
| **`5.1`** | **76149** | LA BATERIA SE DECLARA CORRIDA CON TODOS LOS TRAMOS DE SU REPARTO, Y HOY SON ONCE, NO NUEVE. ADJUDICADO, Y NO HACE FALTA DOCTRINA NUEVA. | CORRO ONCE TRAMOS Y NO PARO EN NUEVE. La bateria se declara corrida cuando los ONCE que el reparto compute tengan salida sellada del mismo calibre. NO reescribo el fichero del auditor: el nueve es la cifra a su corte y se corrige por declaracion. |
| **`5.2`** | **76159** | EL `--siguiente` NO ES SENAL DE ARRANQUE. ADJUDICADO A FAVOR DEL EJECUTOR. | NO USO EL CARRIL DE LA SENAL DE ARRANQUE PARA DECIDIR NADA. Corro tramo por tramo del 1 al 11 y commiteo cada salida al terminar, y publico ANTES el commit y la fecha de los sellos viejos. |
| **`5.3`** | **76166** | EL `2.117` CONTRA EL `3388`: MANDA EL CORTE, NO LA LETRA. ADJUDICADO, PENDIENTE CERRADO. | NO VUELVO A TRAER EL MARCADOR COMO PENDIENTE DE DOCTRINA. La clausula pide que ESA operacion no mueva el marcador, no afirma cuanto vale. PENDIENTE CERRADO, y esta vuelta no mueve el marcador. |
| **`5.4`** | **76174** | EL PUNTO 3 DE `OP-I-01`: UNA NEGATIVA SI SE PUEDE CITAR. ADJUDICADO CONTRA EL EJECUTOR. | MIDO EL PUNTO 3 DE `OP-I-01` CORRIENDO LA BUSQUEDA Y PUBLICANDO SU CERO CON EL COMANDO DELANTE. Lo que se prohibe es afirmar una busqueda NO CORRIDA, no publicar la que da cero. Va en la TAREA 4. |
| **`5.5`** | **76183** | EL PUNTO 4 DE `OP-I-01`: NO LO ADJUDICO, LO ENCARGO, Y DIGO POR QUE. | BUSCO LA SEDE QUE SI REGENERA LA VISTA HUMANA ANTES DE DECIR SI EL PUNTO 4 CUBRE. No la invento: publico la busqueda con su comando, y si la sede no existe eso tambien es un resultado. Va en la TAREA 4. |
| **`5.6`** | **76188** | LAS TRES FILAS VAN DENTRO DE LA TABLA. RESPONDIDA SU PREGUNTA 1. | REGISTRADA, no me da orden nueva. |
| **`5.7`** | **76193** | NO, NO NECESITABA NADA MAS. RESPONDIDA SU PREGUNTA 2. | REGISTRADA, no me da orden nueva. |
| **`5.8`** | **76198** | SUS TRES DISCUTIBLES, LOS TRES A SU FAVOR. | REGISTRADA, no me da orden nueva. |
| **`5.9`** | **76206** | SU `D.3` SE CONFIRMA Y NO LE PERJUDICA. | REGISTRADA, no me da orden nueva. |

**LAS CUATRO ULTIMAS (`5.6` a `5.9`) NO ME DAN ORDEN NUEVA Y LO DIGO EN VEZ DE
INFLARLAS:** dos responden preguntas de la 214, una adjudica sus tres discutibles
a su favor, y la `5.9` confirma su `D.3`. **Se registran porque el encargo manda
registrar LAS NUEVE, no solo las cinco que mandan.**

#### 1.b. EL HALLAZGO CONTRA MI PROPIO REPORTE DE LA 214, QUE ES LA CAIDA QUE ACUMULA

**FILAS ARMADAS: 2.** El acta trae dos entradas en su seccion 3 y
las dos van aqui, porque esconder la que me favorece seria elegir.

| hallazgo | linea del acta | titulo, VERBATIM del acta |
|---|---:|---|
| **`3.1`** | **76086** | LA SECCION 3.1 DE SU REPORTE, QUE ES LA DEL CICLO ENTERO DE GATE 0, SALIO PUBLICADA VACIA. Y ES CAIDA DE REPORTE QUE ACUMULA, PORQUE VIVE EN U |
| **`3.2`** | **76120** | UNA PRECISION MENOR QUE NO ES CAIDA Y LA DIGO PARA QUE NADIE LA CUENTE COMO TAL. |

**LO REGISTRO SIN ATENUARLO, PORQUE ES MIO Y ES EL UNICO QUE ACUMULA.** Mi
seccion 3.1 de la 214, la del ciclo entero de Gate 0, **salio publicada VACIA**:
sus dos filas decian que no habia fichero de consola y las tres columnas de
medicion salieron en blanco. **La causa esta medida y no supuesta: el fichero de
consola que mi compositor buscaba NUNCA EXISTIO**, ni en el arbol ni en la
historia, porque el ciclo imprime su consola por `stdout` y yo no la redirigi. **Y
lo que importa mas que la celda vacia: mi compositor escribio una fila en blanco
y siguio**, que es degradacion silenciosa, que es justo lo que el banco 9
prohibe.

**MI RACHA DE CAIDA DE REPORTE QUEDA EN UNO**, y el remedio de las dos mitades va
en la **TAREA 5** de esta vuelta, que es bloqueante: la consola se sella **desde
dentro del propio instrumento** y el compositor **CAE EN ROJO** si no la
encuentra, en vez de rellenar con un hueco.

#### 1.c. LA GUARDA DE ESTA TAREA, Y SU PRUEBA DE MUTACION

**Las cuatro comprobaciones viven en una funcion pura, `juzgar()`, para que se
puedan mutar sin tocar el acta**: que las adjudicaciones sean nueve, que sus
etiquetas vayan de `5.1` a `5.9` sin huecos ni repeticiones, que las cinco que el
encargo manda aplicar esten, y que el hallazgo `3.1` aparezca.

**`docs/loop/SALIDA_V215_T1_MUTANTES.txt`: 6 mutantes, CAEN 6, y el texto bueno pasa el
mismo juicio en 0 fallos.** El mutante `F` es el que de verdad me
importaba: **las dos listas vacias**, que es lo que devuelve un lector que no
encuentra nada, **cae con 4 fallos**. Un lector roto que no cae es exactamente la
enfermedad de mi `3.1`.

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

