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
| **TAREA 2** | LA BATERIA ENTERA, POR TRAMOS, Y SIN EL FALSO VERDE. Publicar ANTES de correr nada de que vuelta son los once sellos que hay en el arbol, con su commit y su fecha leidos de git log; NO usar el carril de la senal de arranque, que hoy publica un verde que no es de esta vuelta; y correr los ONCE tramos uno a uno con su doble corrida, su reloj y su salida sellada, commiteando cada salida al terminar su tramo | **CERRADA, CON DOS PARADAS TRAIDAS** | SALIDA_V215_T2_PLAN.txt, SALIDA_V215_T2_SIGUIENTE_FALSO_VERDE.txt, los ONCE SALIDA_V183_BATERIA_TRAMO_N.txt, SALIDA_V183_BATERIA.txt, SALIDA_V215_T2_TABLA.txt, SALIDA_V215_T2_MUTANTES.txt |
| **TAREA 3** | EL CIERRE INTEGRAL, TODO LO QUE NO NECESITA CREDENCIAL: el ciclo entero de Gate 0 por los dos lados con su consola SELLADA y sus dieciocho salidas en disco; las tres suites con su exitcode y sus bytes; el inventario de las 71 fichas contra sus pruebas con el hash de la apertura; y el marcador y el censo recomputados, cada uno con su comando y con las cifras del auditor al lado para cotejar y NO para copiar | **CERRADA, CON UNA DISCREPANCIA DECLARADA** | SALIDA_V215_T3_SUITE_MOTOR/TSC/WEB.txt, SALIDA_V215_T3_EXPEDIENTE.txt, SALIDA_V215_T3_EXPEDIENTE_CORTE_AUDITOR.txt, SALIDA_V215_T3_MARCADOR.txt, SALIDA_V215_T3_ARISTAS.txt, SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt |
| **TAREA 4** | LOS DOS PUNTOS QUE `OP-I-01` DEJO EN A MEDIAS, Y NO SE CIERRAN A OJO. El punto 3 por su NEGATIVA, que si se puede citar: se corre la busqueda y se publica su CERO con el comando delante. Y el punto 4 midiendo ANTES de decidir: buscar cual es el instrumento y cual el fichero que SI regeneran la vista humana, publicar la busqueda con su comando, y solo entonces decir si CUBRE, queda A MEDIAS o NO CUBRE. SIN mover el campo estado de ninguna ficha | **CERRADA, UN PUNTO SE MUEVE A CUBRE** | SALIDA_V215_T4_DOS_PUNTOS.txt (los dos puntos con su busqueda, su caso positivo y la guarda de los dos sha256), SALIDA_V215_COMPOSITOR_T4.txt |
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

### TAREA 2. LA BATERIA ENTERA, ONCE TRAMOS, Y SIN EL FALSO VERDE

#### 2.a. DE QUE VUELTA SON LOS SELLOS QUE HABIA EN EL ARBOL, PUBLICADO ANTES DE CORRER NADA

**ESTA TABLA SE TALLO EN LA APERTURA, ANTES DE LA PRIMERA OPERACION.** Vive en
`docs/loop/SALIDA_V215_APERTURA.txt`, con el commit y la fecha de cada sello **leidos de `git log` y no
tecleados**, que es lo que la TAREA 2.a manda.

**FILAS ARMADAS: 11. FILAS QUE DEBERIA HABER, contadas por la propia
apertura: 11.**

| tramo | bytes al entrar | ultimo commit ANTES de esta vuelta | fecha | asunto (primeros 70) |
|---:|---:|---|---|---|
| **1** | 9544 | `ca702058` | **2026-09-08** | VUELTA 210, BATERIA TRAMO 1 DE 11, SELLADO Y COMMITEADO AL TERMINAR, u |
| **2** | 7795 | `4895fb06` | **2026-09-08** | VUELTA 210, BATERIA TRAMO 2 DE 11, SELLADO Y COMMITEADO AL TERMINAR, u |
| **3** | 8050 | `3fa5b035` | **2026-09-08** | VUELTA 210, BATERIA TRAMO 3 DE 11, RE CORRIDO SOLO Y RE SELLADO. CORRE |
| **4** | 7862 | `a9a8fff9` | **2026-09-08** | VUELTA 210, BATERIA TRAMO 4 DE 11, RE CORRIDO SOLO Y RE SELLADO: EL RU |
| **5** | 8274 | `274a0aed` | **2026-09-08** | VUELTA 210, BATERIA TRAMO 5 DE 11, SELLADO Y COMMITEADO AL TERMINAR. T |
| **6** | 8205 | `fc68e550` | **2026-09-08** | VUELTA 210, BATERIA TRAMO 6 DE 11, SELLADO Y COMMITEADO AL TERMINAR. D |
| **7** | 7893 | `3d79c288` | **2026-09-08** | VUELTA 210, BATERIA TRAMO 7 DE 11, SELLADO Y COMMITEADO AL TERMINAR: T |
| **8** | 7848 | `97185bc4` | **2026-09-08** | VUELTA 210, BATERIA TRAMO 8 DE 11, SELLADO Y COMMITEADO AL TERMINAR: T |
| **9** | 8525 | `ed74786d` | **2026-09-08** | VUELTA 210, BATERIA TRAMO 9 DE 11, SELLADO Y COMMITEADO AL TERMINAR. Y |
| **10** | 8472 | `08e9acdd` | **2026-09-08** | VUELTA 210, BATERIA TRAMO 10 DE 11, SELLADO Y COMMITEADO AL TERMINAR:  |
| **11** | 6273 | `7dfbfdf7` | **2026-09-08** | VUELTA 210, BATERIA TRAMO 11 DE 11, SELLADO Y COMMITEADO AL TERMINAR:  |

**LOS ONCE ERAN DE LA VUELTA 210 Y LOS ONCE ESTABAN FECHADOS EL 2026-09-08.**
Esa es la tabla que hace distinguible mi corrida nueva: el lanzador nombra sus
salidas con el numero de SU PROPIO fichero, asi que una corrida vieja y una
fresca **comparten nombre**, y lo unico que prueba de que vuelta es cada tramo es
**que su fichero cambie en un commit de esta vuelta**. Los once cambiaron, uno a
uno, en once commits de la 215.

#### 2.b. EL FALSO VERDE, MEDIDO POR MI Y NO USADO COMO SENAL

**Corri el carril de la senal de arranque UNA VEZ, y solo para medir la trampa,
NO para decidir nada** (adjudicacion `5.2`). Su salida esta en `docs/loop/SALIDA_V215_T2_SIGUIENTE_FALSO_VERDE.txt` y
dice **`CIFRA tramos que FALTAN: 0`** y **LOS 11 TRAMOS TIENEN
SALIDA SELLADA**, sobre los sellos de la 210 que la tabla de arriba acaba de
fechar. **Si esta vuelta lo hubiera usado como senal de arranque, habria
declarado corrida una bateria que no habia corrido ni un tramo.**

**EL REPARTO, COMPUTADO Y NO TECLEADO** (`docs/loop/SALIDA_V215_T2_PLAN.txt`): nomina **135**,
tramo de **13**, **11 TRAMOS**, y la suma de los tramos
reproduce las **135**. **ONCE, no nueve**, por la adjudicacion `5.1`.

#### 2.c. LOS ONCE TRAMOS CORRIDOS, UNO A UNO Y COMMITEADOS AL TERMINAR

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V215_T2_TABLA.txt`: 11. FILAS QUE DEBERIA HABER:
11.** Cada celda sale de contar el fichero sellado de su tramo.

| tramo | entradas | OK | CASO DECLARADO | NO MORDIO | ANCLA PERDIDA | NO REPRODUCIBLE | exitcode | minutos | bytes | sha256 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **1** | 13 | 11 | 2 | 0 | 0 | 0 | 1 | 0.8 | 9552 | `4de1654fb3bb` |
| **2** | 13 | 13 | 0 | 0 | 0 | 0 | 1 | 2.9 | 7796 | `8c1f6ce3013b` |
| **3** | 13 | 12 | 0 | 1 | 0 | 0 | 1 | 3.2 | 8048 | `f17327591699` |
| **4** | 13 | 13 | 0 | 0 | 0 | 0 | 1 | 1.0 | 7863 | `44f5c01f680b` |
| **5** | 13 | 10 | 0 | 3 | 0 | 0 | 1 | 0.7 | 8270 | `dbf5328708ad` |
| **6** | 13 | 11 | 0 | 2 | 0 | 0 | 1 | 0.9 | 8212 | `8072bd87c785` |
| **7** | 13 | 13 | 0 | 0 | 0 | 0 | 1 | 0.6 | 7896 | `7328143949bc` |
| **8** | 13 | 13 | 0 | 0 | 0 | 0 | 1 | 0.8 | 7849 | `8aa2ce144943` |
| **9** | 13 | 12 | 0 | 1 | 0 | 0 | 1 | 0.9 | 8512 | `b733d7eeb028` |
| **10** | 13 | 13 | 0 | 0 | 0 | 0 | 1 | 1.6 | 8473 | `0ef8f1995e55` |
| **11** | 5 | 5 | 0 | 0 | 0 | 0 | 1 | 0.3 | 6269 | `c58146cb3792` |

**LA COBERTURA, LEIDA DE LA COMPUESTA Y NO RECALCULADA DEL REPARTO**
(`docs/loop/SALIDA_V183_BATERIA.txt`, 93498 bytes, 1433 lineas): entradas que
**NINGUN** tramo corrio **0**, entradas corridas que **NO estan en
la nomina** **0**, entradas corridas **MAS DE UNA VEZ**
**0**. **Las 135 entradas de la nomina corrieron, cada una
EXACTAMENTE UNA VEZ, y cada una DOS VECES por la doble corrida.**

**EL REPARTO DE LAS 135: OK 126, CASO DECLARADO 2, NO MORDIO
7, ANCLA PERDIDA 0, NO REPRODUCIBLE 0.** Las cinco
clases **suman las 135**, y el instrumento lo comprueba antes de
publicar la tabla. **NO REPRODUCIBLE en 0 es la doble corrida diciendo
que las dos corridas de cada entrada dan lo mismo.**

#### 2.d. LO QUE CAE, Y LO TRAIGO EN VEZ DE ARREGLARLO DE PASO

**MI ENCARGO DICE, CON ESTAS PALABRAS: SI ALGUN ARNES DE LA NOMINA CAE, PARAS Y
LO TRAES.** **CAEN 7, y aqui estan con su nombre y su tramo.** **Las dos
PARADAS de esta vuelta van al final del reporte; esta es la tabla que las
sostiene.**

| tramo | clase | arnes | contra la corrida anterior del mismo fichero |
|---:|---|---|---|
| **3** | NO MORDIO | `scripts/loop/vuelta160_tarea6b_mutacion_puerta.py` | **YA CAIA EN LA 210** |
| **5** | NO MORDIO | `scripts/loop/vuelta165_tarea6_mutacion_op_l_01.py` | **YA CAIA EN LA 210** |
| **5** | NO MORDIO | `scripts/loop/vuelta166_tarea2_mutacion_correccion.py` | **YA CAIA EN LA 210** |
| **5** | NO MORDIO | `scripts/loop/vuelta168_tarea1_mutacion_nota.py` | **YA CAIA EN LA 210** |
| **6** | NO MORDIO | `scripts/loop/vuelta168_tarea2_mutacion_reconstructor.py` | **YA CAIA EN LA 210** |
| **6** | NO MORDIO | `scripts/loop/vuelta171_mutacion_busqueda_acta.py` | **YA CAIA EN LA 210** |
| **9** | NO MORDIO | `scripts/loop/vuelta185_tarea1c_mutacion_bateria_continuada.py` | **YA CAIA EN LA 210** |

**Y EL COTEJO QUE HACE LEGIBLE ESA CIFRA, PORQUE UN ARNES QUE LLEVA ROJO DESDE
ANTES Y UNO QUE SE ACABA DE ROMPER NO SON LA MISMA NOTICIA.** La corrida anterior
de **cada uno** de los once ficheros se lee con `git show` sobre el commit que la
sello, y ese commit sale de `git log --skip=1` sobre la ruta, **no de mi
memoria**: los once son de la **vuelta 210**, del 2026-09-08.

- **ARNESES QUE CAEN HOY Y NO CAIAN EN LA 210: 0.**
- **ARNESES QUE CAEN HOY Y YA CAIAN: 7.**
- **ARNESES QUE CAIAN Y HOY NO CAEN: 0.**

**LOS 7 SON LOS MISMOS 7, NI UNO MAS NI UNO MENOS.** **Esta vuelta
no rompio nada y tampoco arreglo nada**, y eso es exactamente lo que se puede
afirmar con la medicion delante. **NO LOS TOCO**: repararlos seria fabricar
maquinaria bajo la moratoria, y arreglar un arnes en rojo de paso, en la vuelta
del cierre integral, es justo lo que mi encargo prohibe.

#### 2.e. MI PROPIA CAIDA DE ESTA TAREA, Y LA GUARDA QUE LA CIERRA

**Va entera en la seccion de mis caidas (`D.1`) y no la escondo aqui.** En una
linea: mi compositor de mensajes de commit llevaba la frase *"y ninguno cae"*
**clavada en el texto** al lado de cifras que si se leian, y en el tramo 3 las
dos cosas se contradijeron dentro del mismo mensaje. **Hoy la frase se COMPUTA de
las tres cifras de fallo y el instrumento CAE EN ROJO si la prosa y las cifras no
dicen lo mismo.**

**SU PRUEBA DE MUTACION VA DELANTE Y NO DETRAS** (`docs/loop/SALIDA_V215_T2_MUTANTES.txt`): **5
casos, 0 que no calzan**, y la cifra que de verdad importa es que los
casos con caidos distinto de cero en los que la frase **aun diria** *"ninguno
cae"* son **0**.

### TAREA 3. EL CIERRE INTEGRAL, TODO LO QUE NO NECESITA CREDENCIAL

**LA GUARDA DE ESTA SECCION ES LA QUE ME FALTO EN LA 214, Y VA DELANTE.** El
compositor mira **las seis fuentes** antes de componer y **CIFRA fuentes
ausentes: 0**; si faltara una, **REVIENTA y no escribe**, en vez de dejar una
celda en blanco y seguir. Lo mismo con las cifras: **necesita 25 y le
faltan 0**.

#### 3.a. EL CICLO ENTERO DE GATE 0, Y POR QUE SUS DOS LADOS NO VAN LOS DOS AQUI

**EL LADO APERTURA CORRIO ANTES DE LA PRIMERA TAREA Y ESTA SELLADO**, con su
consola en `docs/loop/SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt` y sus nueve salidas en disco. **PEOR EXITCODE DE LOS
OCHO, LEIDO DE ESA CONSOLA: 0.**

**EL LADO CIERRE NO SE CORRE AQUI Y DIGO POR QUE, QUE NO ES PEREZA:**
`EJECUTOR.md` 1 dice que **EL ESTADO AL CIERRE SE MIDE AL CIERRE**, y medirlo en
mitad de la vuelta y publicarlo como cierre es la caida de la vuelta 28. **El
lado CIERRE corre al cerrar y sus cifras van en la seccion 3.1**, con las
DIECIOCHO salidas cotejadas y los dos lados juntos.

#### 3.b. LAS TRES SUITES, CADA UNA CORRIDA SOLA Y SELLADA APARTE

**Son las mismas tres que el ciclo corre en sus puestos 7, 8a y 8b, y aqui van
CORRIDAS OTRA VEZ Y SOLAS**, para que su cifra no dependa de leer dentro de la
salida de otro instrumento.

**FILAS ARMADAS: 3. FILAS QUE DEBERIA HABER: 3.**

| suite | comando | exitcode | bytes | salida sellada |
|---|---|---:|---:|---|
| **motor** | `engine/run_all_tests.py` | **0** | 1164 | `docs/loop/SALIDA_V215_T3_SUITE_MOTOR.txt` |
| **tsc** | `npx tsc --noEmit -p tsconfig.json` | **0** | 15 | `docs/loop/SALIDA_V215_T3_SUITE_TSC.txt` |
| **web** | `pnpm test` | **0** | 338 | `docs/loop/SALIDA_V215_T3_SUITE_WEB.txt` |

#### 3.c. EL INVENTARIO DE LAS 71 FICHAS CONTRA SUS PRUEBAS

**Corrido con `scripts/loop/vuelta150_3_relectura_expediente.py --corte` y el
hash de MI apertura, `416c7a43`**, que es el que el encargo pide. Salida sellada
en `docs/loop/SALIDA_V215_T3_EXPEDIENTE.txt`.

**PUBLICO LA CIFRA QUE SALE, NO LA QUE ME GUSTE:**

- **CIFRA fichas del expediente: 71.**
- **CIFRA fichas que NO CALZAN: 40.**
- **CIFRA congeladas DECLARADAS: 24 | congeladas EN SILENCIO:
  12.**
- **CIFRA fichas en HECHA SIN NINGUNA PRUEBA: 4.**
- **CIFRA fichas en LISTA sin ninguna prueba: 3.**

**MI CIFRA DE 40 ES LA SUYA, Y NO LA AJUSTO PORQUE NO HACE FALTA.** Lo comprobe
ademas **con SU corte** (`docs/loop/SALIDA_V215_T3_EXPEDIENTE_CORTE_AUDITOR.txt`, corrido con `--corte 89c7bf23`): da
**40** que no calzan y **4** en HECHA sin prueba.
**Los dos cortes dan lo mismo**, o sea que la cifra no depende de cual de los dos
hashes se use.

**Y AQUI VA UNA DISCREPANCIA QUE DECLARO EN VEZ DE RESOLVER COPIANDO.** El
encargo dice *"dos de ellas, `OP-V-01` y `OP-L-01`, siguen en HECHA SIN NINGUNA
PRUEBA"*. **Yo mido 4, no dos**, y las cuatro van con su nombre:

| id_op | fase | veredicto de la vara |
|---|---|---|
| `OP-V-01` | 08_VERIFICACION | **HECHA SIN NINGUNA PRUEBA** |
| `OP-L-01` | 09_LECTURAS_DIRIGIDAS | **HECHA SIN NINGUNA PRUEBA** |
| `OP-L-02` | 09_LECTURAS_DIRIGIDAS | **HECHA SIN NINGUNA PRUEBA** |
| `OP-L-03` | 09_LECTURAS_DIRIGIDAS | **HECHA SIN NINGUNA PRUEBA** |

**NO DIGO QUE EL AUDITOR SE EQUIVOQUE Y NO TENGO COMO SABERLO:** las dos que
nombra estan entre las cuatro, y nombrar dos de cuatro no es afirmar que sean
dos. **Lo que hago es publicar las cuatro con su nombre**, porque una vuelta que
copia "dos" de un encargo teniendo cuatro delante es la caida que
`EJECUTOR.md` 2 prohibe.

#### 3.d. EL MARCADOR Y EL CENSO, RECOMPUTADOS CADA UNO CON SU COMANDO

**MARCADOR**, con `python scripts/recomputar_marcador.py 3388`, sellado en
`docs/loop/SALIDA_V215_T3_MARCADOR.txt`: **n 3388, corte 3388, A 550, B 72, C 5,
D 2761, huecos 0, duplicados de puesto 0, pares duplicados
0.**

**CENSO Y ARISTAS**, con `python scripts/loop/vuelta83_conteo_aristas.py WORK`,
sellado en `docs/loop/SALIDA_V215_T3_ARISTAS.txt`: **nodos 3853, vivos 3169, deprecados
684; siguientes 8780, previos 8740, suma 17520.** La union sale
**9914** y **la publico sin cotejarla**, porque el encargo no da su pareja y
una cifra sin pareja no se coteja, se dice.

**EL COTEJO CONTRA LAS CIFRAS QUE EL ENCARGO ME DA, PARA COTEJAR Y NO PARA
COPIAR.** Las suyas viven en `docs/loop/PROMPT_SIGUIENTE.md`, TAREA 3, apartados
(c) y (d).

**FILAS ARMADAS: 13. FILAS QUE DEBERIA HABER: 13.**
**CIFRA celdas que NO CALZAN: 0.**

| cifra | la MIA, medida hoy | la del encargo | veredicto |
|---|---:|---:|---|
| `A` | **550** | 550 | calza |
| `B` | **72** | 72 | calza |
| `C` | **5** | 5 | calza |
| `D` | **2761** | 2761 | calza |
| `depre` | **684** | 684 | calza |
| `huecos` | **0** | 0 | calza |
| `marcador_n` | **3388** | 3388 | calza |
| `no_calzan` | **40** | 40 | calza |
| `nodos` | **3853** | 3853 | calza |
| `prev` | **8740** | 8740 | calza |
| `sig` | **8780** | 8780 | calza |
| `suma` | **17520** | 17520 | calza |
| `vivos` | **3169** | 3169 | calza |

**LAS 13 CALZAN UNA A UNA, Y NO ME LAS CREI: LAS MEDI.** Es la unica
manera de que un cotejo signifique algo.

### TAREA 4. LOS DOS PUNTOS DE `OP-I-01` QUE QUEDARON A MEDIAS

**LO PRIMERO, PORQUE ES LO QUE LA `4.c` PROHIBE:** esta tarea **NO ESCRIBE NI UNA
LINEA EN NINGUNA FICHA**, y no lo prometo, lo mido. **`sha256` LF de
`docs/plan/OPERACIONES.jsonl` a los dos lados: CALZAN SI.** **Filas
de `numstat` sobre el expediente: 0. Sobre el inventario: 0.**
**CERO campos `estado` movidos, en `OP-I-01` y en las demas.**

#### 4.a. EL PUNTO 3, POR SU NEGATIVA, QUE SI SE PUEDE CITAR

**ME LO ADJUDICARON EN CONTRA Y TENIAN RAZON** (`5.4`, linea **76174**). Dije que
una busqueda negativa no se puede citar, y lo que se prohibe es **AFIRMAR UNA
BUSQUEDA NO CORRIDA**, no publicar la que da cero. **Aqui esta corrida.**

**EL COMANDO, ESCRITO ANTES DE SU RESULTADO:** por cada una de las
**672** entradas de `docs/plan/INVENTARIO.jsonl` y por cada uno de sus
**4704** campos de texto, se pregunta si el campo **ENTERO**, en minusculas
y sin espacios de los bordes, **es** una de 23 palabras de relleno, y aparte si
esta **VACIO**. **Se compara el campo COMPLETO, NUNCA por subcadena**, que es la
laxitud que me cazo la `D.7` en la 214.

**EL VOCABULARIO ES MIO Y VA ESCRITO ENTERO EN EL INSTRUMENTO PARA QUE SE PUEDA
DISCUTIR.** Una lista que nadie puede leer no se puede auditar. **Lo marco como
discutible.**

**LA MITAD AFIRMATIVA, CON SUS DOS CONVENCIONES, PORQUE UNA SOLA NO SE PUEDE
COTEJAR CON LA CIFRA DE LA 214:** entradas que nombran la marca **tal cual, en
mayusculas: 5**; entradas que la nombran **sin mirar mayusculas:
119**. **La 214 publico 119 con la segunda**, y lo se porque
lei su convencion en la **linea 133** de `scripts/loop/_v214_t1c_op_i_01.py`, no
porque me acuerde.

**LA MITAD NEGATIVA, QUE ES LA QUE ESTABA PENDIENTE, CON SU CERO DELANTE:**

- **CIFRA campos SOSPECHOSOS de relleno, antes de mirar el vocabulario del
  campo: 6.**
- **CIFRA DESCARTADOS porque el campo los usa como estado: 6.**
- **CIFRA campos RELLENADOS DE VERDAD: 0.**
- **CIFRA campos VACIOS, que no estan nombrados ni rellenados: 0.**

**LOS 6 DESCARTES NO SE ESCONDEN: VAN CON SU NOMBRE Y CON LA CIFRA
QUE LOS DESCARTA.** Son mi caida `D.2` de esta vuelta, cazada por mi antes de
publicar el veredicto.

| entrada | sujeto | campo | valor | la forma LARGA que el MISMO campo trae |
|---:|---|---|---|---|
| **7** | health_safety | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |
| **8** | quality | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |
| **9** | risk_management | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |
| **10** | seguridad_digital | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |
| **320** | costuras internas confirmadas | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |
| **322** | racimos con miembro de otro dominio | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |

**LA REGLA DEL DESCARTE ES MECANICA Y NO SE ENSANCHA PARA QUE TRAGUE:** una
palabra sospechosa en el campo `F` se descarta **solo si el propio campo `F`
tiene, en otra entrada, un valor que empieza por esa palabra y sigue con mas
texto**. Pide la forma larga **en el mismo campo**, no en cualquiera. **Su caso
positivo lo prueba:** `pendiente` tiene formas largas en `estado` (**4**) y
**ninguna** en `forma` (**0**), asi que en `forma` seguiria contando como
relleno.

**VEREDICTO MEDIDO HOY DEL PUNTO 3: CUBRE** (la 214 lo dejo en **A MEDIAS**).
**SE MUEVE.**

#### 4.b. EL PUNTO 4, MIDIENDO ANTES DE DECIDIR Y SIN INVENTAR LA SEDE

**LA VISTA HUMANA DECLARA DE SI MISMA QUE AHI NO SE REGENERA, Y LO DICE EN TRES
SITIOS**, no en uno: `docs/plan/10_INVENTARIO.md` **lineas 19, 121 y 182**,
pegadas enteras en la salida sellada. **Eso es lo que el encargo ya sabia. Lo que
faltaba era saber DONDE SI.**

**LA BUSQUEDA, CON SU COMANDO ESCRITO ANTES DE SU RESULTADO:** se recorre **todo
el arbol de scripts**, no solo el del bucle, y por cada fichero de Python se
pregunta si **nombra** la vista humana y si ademas tiene, en la misma linea o en
las tres siguientes, **una apertura en modo escritura o una llamada de escritura
sobre esa ruta**.

- **CIFRA ficheros que la NOMBRAN: 27.**
- **CIFRA ficheros que la ESCRIBEN: 0.**

**Y LA SEGUNDA MITAD DE LA BUSQUEDA, PORQUE UN FICHERO PUEDE ESCRIBIRSE SIN QUE
NINGUN SCRIPT LO NOMBRE:** de que commits sale la vista humana, leido de
`git log` sobre su ruta. **CIFRA commits en toda su historia: 19**, y el
**ultimo es 6b8fd72b 2026-08-14**. **Sus 34258 bytes de hoy son de esa fecha.**

**LA SEDE QUE REGENERARIA LA VISTA HUMANA NO EXISTE EN EL REPO, Y ESO TAMBIEN ES
UN RESULTADO, QUE ES LO QUE EL ENCARGO PIDE QUE DIGA SI PASA.** Los
**27** ficheros que la nombran **la LEEN o la CITAN**; ninguno la
escribe. **Su ultima escritura fue A MANO**, en un commit de agosto.

**VEREDICTO MEDIDO HOY DEL PUNTO 4: A MEDIAS**, y **no por pereza de esta vuelta**:
la mitad que falta **no tiene instrumento que la haga**, y fabricarlo **es
maquinaria nueva bajo la moratoria** (`AUDITOR.md` 6.3). **NO LA FABRICO Y NO ME
LA ADJUDICO: SE SUBE NOMBRADA.**

#### 4.c. LO QUE ESTO DEJA, DICHO SIN ADORNO

**`OP-I-01` QUEDA HOY EN 3 PUNTOS EN CUBRE Y 1 EN A MEDIAS**, contra los 2 y 2
que la 214 midio. **El que se mueve es el 3**, y se mueve porque **se corrio la
busqueda que faltaba**, no porque nadie cambiara de opinion. **El 4 sigue donde
estaba, y ahora se sabe POR QUE: le falta una sede que no existe.**

**CIFRA comprobaciones del instrumento que fallan: 0.**

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

