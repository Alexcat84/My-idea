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
