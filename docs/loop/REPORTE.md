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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 215`, y su salida
cruda vive en `docs/loop/SALIDA_V215_TALLADOR_CABECERA.txt` (2352 bytes en disco y 2332 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `416c7a43` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 214: LA VUELTA CIERRA BIEN, Y LA UNICA CAIDA GRAVE DE LA JORNADA ES MIA.'), HEAD real de apertura `416c7a43` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `c9747886` (leido de `SALIDA_V215_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, Y VA PRIMERA PORQUE LAS DEMAS SE APOYAN EN ELLA. Leer el acta de la vuelta 214 en `docs/loop/ACTA_AUDITOR.md`, sus secciones 3 y 5, y REGISTRAR LAS NUEVE ADJUDICACIONES CON LA LINEA DE DONDE SALE CADA UNA, aplicando como orden las cinco que el encargo nombra; y registrar el hallazgo `3.1` del auditor contra el reporte de la 214, que es la unica caida no declarada y la unica que acumula | **CERRADA** | SALIDA_V215_T1_REGISTROS.txt (9 adjudicaciones y 2 hallazgos con su linea), SALIDA_V215_T1_MUTANTES.txt (6 de 6 caen, texto bueno en 0 fallos), SALIDA_V215_COMPOSITOR_T1.txt |
| **TAREA 2** | LA BATERIA ENTERA, POR TRAMOS, Y SIN EL FALSO VERDE. Publicar ANTES de correr nada de que vuelta son los once sellos que hay en el arbol, con su commit y su fecha leidos de git log; NO usar el carril de la senal de arranque, que hoy publica un verde que no es de esta vuelta; y correr los ONCE tramos uno a uno con su doble corrida, su reloj y su salida sellada, commiteando cada salida al terminar su tramo | **CERRADA, CON DOS PARADAS TRAIDAS** | SALIDA_V215_T2_PLAN.txt, SALIDA_V215_T2_SIGUIENTE_FALSO_VERDE.txt, los ONCE SALIDA_V183_BATERIA_TRAMO_N.txt, SALIDA_V183_BATERIA.txt, SALIDA_V215_T2_TABLA.txt, SALIDA_V215_T2_MUTANTES.txt |
| **TAREA 3** | EL CIERRE INTEGRAL, TODO LO QUE NO NECESITA CREDENCIAL: el ciclo entero de Gate 0 por los dos lados con su consola SELLADA y sus dieciocho salidas en disco; las tres suites con su exitcode y sus bytes; el inventario de las 71 fichas contra sus pruebas con el hash de la apertura; y el marcador y el censo recomputados, cada uno con su comando y con las cifras del auditor al lado para cotejar y NO para copiar | **CERRADA, CON UNA DISCREPANCIA DECLARADA** | SALIDA_V215_T3_SUITE_MOTOR/TSC/WEB.txt, SALIDA_V215_T3_EXPEDIENTE.txt, SALIDA_V215_T3_EXPEDIENTE_CORTE_AUDITOR.txt, SALIDA_V215_T3_MARCADOR.txt, SALIDA_V215_T3_ARISTAS.txt, SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt |
| **TAREA 4** | LOS DOS PUNTOS QUE `OP-I-01` DEJO EN A MEDIAS, Y NO SE CIERRAN A OJO. El punto 3 por su NEGATIVA, que si se puede citar: se corre la busqueda y se publica su CERO con el comando delante. Y el punto 4 midiendo ANTES de decidir: buscar cual es el instrumento y cual el fichero que SI regeneran la vista humana, publicar la busqueda con su comando, y solo entonces decir si CUBRE, queda A MEDIAS o NO CUBRE. SIN mover el campo estado de ninguna ficha | **CERRADA, UN PUNTO SE MUEVE A CUBRE** | SALIDA_V215_T4_DOS_PUNTOS.txt (los dos puntos con su busqueda, su caso positivo y la guarda de los dos sha256), SALIDA_V215_COMPOSITOR_T4.txt |
| **TAREA 5** | EL REPORTE, Y SU SECCION 3.1 ESTA VEZ CON CIFRAS DENTRO. Sellar la consola del ciclo de Gate 0 por los dos lados en los nombres que el compositor busca, y sobre todo hacer que EL COMPOSITOR CAIGA EN ROJO SI NO LA ENCUENTRA: el de la 214 escribio una fila en blanco y siguio, que es degradacion silenciosa y es lo que el banco 9 prohibe. Y la seccion 9 cierra con LA BATERIA CORRIDA, no con hueco declarado, porque esta es su vuelta | **CERRADA, LA GUARDA PROBADA POR MUTACION** | SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt (912 bytes en disco y 912 bytes normalizado a LF, sellada por el propio ciclo), SALIDA_V215_T5_MUTANTES.txt (4 casos, 4 CALZA, 0 casos malos que produzcan fila), SALIDA_V215_COMPOSITOR_T5.txt |
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
(`docs/loop/SALIDA_V183_BATERIA.txt`, 93498 bytes en disco y 93498 bytes normalizado a LF, 1433 lineas): entradas que
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
**ultimo es 6b8fd72b 2026-08-14**. **Sus 34258 bytes en disco y 33845 bytes normalizado a LF de hoy son de esa fecha.**

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

### TAREA 5. MI REPORTE, Y LA GUARDA QUE ME FALTO EN LA 214

**LA CAIDA QUE REMEDIA ESTA TAREA ES MIA Y ES LA UNICA QUE ACUMULA**, y va
registrada entera en la TAREA 1.b con la linea del acta donde vive. Aqui va el
remedio, que son **DOS MITADES Y NO UNA**, y la segunda es la que importa.

#### 5.a. LA PRIMERA MITAD: LA CONSOLA SE SELLA DESDE DENTRO DEL INSTRUMENTO

**El ciclo imprime su consola por `stdout` y en la 214 nadie la redirigio.** El
encargo dice *"redirigela"*, y **acordarse de redirigir es exactamente lo que
esta casa lleva vueltas demostrando que no funciona**: por eso no la redirijo
desde fuera, **la escribe el propio instrumento**.

`scripts/loop/_v215_ciclo_gate0.py` duplica su salida con un `Tee`, la sigue
imprimiendo por pantalla, y **la escribe en el nombre exacto que el compositor
busca**, compuesto del numero de vuelta que sale del nombre del fichero y del
lado que llega por argumento. **Y si el fichero saliera de CERO BYTES, el propio
ciclo sale en rojo**, porque una salida sellada de cero bytes no cuenta como
hecha (`EJECUTOR.md` 1).

**MEDIDO:** `docs/loop/SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt` existe, mide **912 bytes en disco y 912 bytes normalizado a LF**, y publica **PEOR
EXITCODE DE LOS OCHO: 0**. **El lado CIERRE se sella igual al cerrar la
vuelta, y sus dos filas van en la seccion 3.1.**

#### 5.b. LA SEGUNDA MITAD, Y ES LA QUE IMPORTA: EL COMPOSITOR REVIENTA

**Lo que el acta 214 senala no es la celda vacia: es que mi compositor
ESCRIBIERA UNA FILA EN BLANCO Y SIGUIERA.** Eso es degradacion silenciosa, que es
lo que el banco 9 prohibe.

**LA DIFERENCIA NO ES UNA PROMESA, ES CODIGO, Y SE LEE DE LOS DOS FICHEROS:**

- El de la 214, **scripts/loop/_v214_cierre_texto.py linea 78: filas_gate.append("| **%s** | (sin fichero de consola) | | |" % lado)**
- El mio: **no tiene esa rama**. `fila_de_gate()` devuelve `(None, motivo)` y
  quien la llama **acumula el fallo duro y sale con exitcode 1 sin escribir una
  sola linea del cuerpo**.

**LA PRUEBA DE MUTACION, QUE VA DELANTE Y NO DETRAS** (`docs/loop/SALIDA_V215_T5_MUTANTES.txt`). Se muta **la
entrada de la funcion pura**, no el repo: ningun fichero se toca, ni se borra, ni
se renombra.

**FILAS ARMADAS: 4. FILAS QUE DEBERIA HABER: 4.**

| caso | que se le da a la guarda | da fila | se esperaba | veredicto |
|---|---|---|---|---|
| **LITERAL DE LA VUELTA 214** | LITERAL DE LA VUELTA 214 | NO | NO | **CALZA** |
| **B** | EL FICHERO EXISTE PERO NO TRAE NI UNA LINEA CON EXITCODE | NO | NO | **CALZA** |
| **C** | TRAE EXITCODES PERO NO SU PEOR EXITCODE | NO | NO | **CALZA** |
| **D** | LA CONSOLA DE VERDAD DE ESTA VUELTA, QUE TIENE QUE DAR FILA | SI | SI | **CALZA** |

**Y LA CIFRA QUE DE VERDAD MIDE EL REMEDIO, PORQUE UNA FILA CON CELDAS VACIAS
SIGUE SIENDO UNA FILA:** **CIFRA casos malos que AUN ASI producen una fila:
0** (se exige 0). **CIFRA casos malos que revientan CON SU MOTIVO
ESCRITO: 3 de 3**, porque reventar sin decir por que es la otra
mitad de la misma enfermedad.

**EL CASO `A` ES EL DE LA 214 LITERAL:** fichero que no existe. **Hoy no da fila,
da un rojo con su motivo.**

**Y ESTO NO FABRICA MAQUINARIA**, que es lo que la moratoria protege: el
compositor de cierre **se escribe cada vuelta de todas formas**, lleva prefijo de
guion bajo, **muere con la vuelta** y no entra en ninguna nomina. **Lo unico que
cambia es que falle ruidoso.**

**LA GUARDA NO SE QUEDO EN EL CIERRE:** los compositores de las TAREAS 3 y 4
llevan la misma negativa a rellenar, y **la de la TAREA 3 me mordio de verdad**
en su primera corrida (su lector de las cuatro clases del marcador devolvia
vacio, y **no escribio nada**).

#### 5.c. LA SECCION 9 CIERRA CON LA BATERIA CORRIDA, NO CON HUECO

**Esta es su vuelta y la bateria corrio.** La seccion 9 la talla
`scripts/loop/cerrar_reporte.py` con la salida compuesta de los once tramos
dentro, y **no lleva hueco declarado**, porque no hay hueco que declarar.

**LO QUE SI LLEVA, Y NO ES LO MISMO QUE UN HUECO:** los once tramos salen en
**exitcode 1**, y eso va dicho en la seccion 5 como **PARADA 2**, con su
contradiccion nombrada y sin que yo elija cual de las dos reglas cede. **Una
bateria corrida con su rojo dicho no es una bateria sin correr.**

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: LA VUELTA 215 ENTREGA SUS CINCO TAREAS Y NO DECLARA LA CAMPANA CONSUMADA: la bateria corrio ENTERA por sus ONCE tramos con las 135 entradas cubiertas una vez cada una y dos corridas cada una, 126 en OK, pero los once salen en exitcode 1 y CAEN SIETE arneses de la nomina, los siete ya caidos desde la 210 y NINGUNO nuevo, asi que la primera de las tres condiciones de la parada feliz NO se cumple y las DOS PARADAS suben con su cifra en vez de un verde; el cierre integral SI sale limpio, con Gate 0 en sus DOS lados a peor exitcode 0 y sus DIECIOCHO salidas presentes, las tres suites en 0, las 71 fichas medidas en 40 que no calzan y CUATRO en HECHA sin prueba contra las dos que el encargo nombra, y las TRECE cifras del encargo cotejadas con 0 que no calzan; el punto 3 de OP-I-01 pasa a CUBRE por su negativa CORRIDA y el punto 4 se queda en A MEDIAS con su sede buscada en todo el arbol y NO ENCONTRADA; y la guarda del hallazgo 3.1 existe, es codigo y no promesa, con sus 4 casos de mutacion y CERO casos malos que produzcan una fila.**

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, Y ESTA VEZ CON CIFRAS DENTRO

**ESTA ES LA SECCION QUE EN LA 214 SALIO PUBLICADA VACIA**, y el remedio son las
dos mitades de la TAREA 5, no una: **la consola se sella desde dentro del propio
instrumento**, y **el compositor CAE EN ROJO si no la encuentra**. La segunda es
la que importa: en la 214 el fichero no existia y mi compositor **escribio una
fila en blanco y siguio**.

**Contado de las dos consolas selladas, no de memoria. FILAS ARMADAS:
2. FILAS QUE DEBERIA HABER: 2.**

| lado | comandos con exitcode leido | los que no dan 0 | peor exitcode | consola sellada |
|---|---:|---:|---|---|
| **APERTURA** | 9 | 0 | **0** | `docs/loop/SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt` |
| **CIERRE** | 9 | 0 | **0** | `docs/loop/SALIDA_V215_CICLO_GATE0_CIERRE_CONSOLA.txt` |

**Y LAS DIECIOCHO SALIDAS EN DISCO, CADA UNA CON SU EXITCODE LEIDO DE DENTRO DEL
PROPIO FICHERO Y SUS BYTES MEDIDOS.** **FILAS ARMADAS: 9. FILAS QUE
DEBERIA HABER: 9, una por comando, con sus DOS lados en la misma fila, o sea
DIECIOCHO celdas.** **CIFRA salidas ausentes o sin exitcode dentro: 0**, y si
hubiera una sola este cuerpo no existiria.

| # | comando | APERTURA (exitcode / bytes) | CIERRE (exitcode / bytes) |
|---|---|---|---|
| **1** | `run_phase1.py --reaplico-curaduria` | 0 / 4790 bytes | 0 / 4790 bytes |
| **2** | `etiquetas_de_cara.py --aplicar` | 0 / 7928 bytes | 0 / 7928 bytes |
| **3** | `sync_assets_web.py` | 0 / 574 bytes | 0 / 574 bytes |
| **4** | `git diff HEAD --numstat` | 0 / 140 bytes | 0 / 140 bytes |
| **5** | `vuelta83_conteo_aristas.py WORK` | 0 / 168 bytes | 0 / 168 bytes |
| **6** | `vuelta85_medir_desfase_calibrado` | 0 / 498 bytes | 0 / 498 bytes |
| **7** | `engine/run_all_tests.py` | 0 / 1131 bytes | 0 / 1131 bytes |
| **8a** | `npx tsc --noEmit` | 0 / 7 bytes | 0 / 7 bytes |
| **8b** | `pnpm test` | 0 / 336 bytes | 0 / 336 bytes |

**`numstat` de los arboles del dataset al cerrar: 0 fila(s). Del
arbol del plan: 0 fila(s).**

### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES

**El `sha256` de apertura se LEE de `docs/loop/SALIDA_V215_APERTURA.txt`, que se
sello antes de la primera operacion; el de cierre se computa ahora.**

| sede | sha256 LF al abrir | sha256 LF al cerrar | | bytes disco / LF |
|---|---|---|---|---|
| `docs/plan/INVENTARIO.jsonl` | 43cea06634e6fc1a | 43cea06634e6fc1a | quieta | 629533 / 629533 |
| `docs/plan/OPERACIONES.jsonl` | 650578474361eb2b | 650578474361eb2b | quieta | 517181 / 517181 |
| `docs/plan/08_VERIFICACION.md` | 578eeefab6db2fd4 | 578eeefab6db2fd4 | quieta | 73652 / 73652 |
| `docs/plan/10_INVENTARIO.md` | 67f464d3d0b9e067 | 67f464d3d0b9e067 | quieta | 34258 / 33845 |
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 758edf1f5c313c18 | 758edf1f5c313c18 | quieta | 4057130 / 4057130 |
| `docs/INTRA_DOMINIO_INFORME.md` | c05b6bcd20188a9c | c05b6bcd20188a9c | quieta | 943970 / 943970 |
| `docs/plan/00_INDICE.md` | 2e71336cc2fdc387 | 2e71336cc2fdc387 | quieta | 45278 / 45278 |
| `docs/BANCO_DE_TEXTOS.md` | 8adbd60239509bb4 | 8adbd60239509bb4 | quieta | 186490 / 186490 |
| `docs/plan/BANCO_DEL_PLAN.md` | 7836c8976c585143 | 7836c8976c585143 | quieta | 61554 / 61554 |
| `dataset/metadata/master_graph.json` | 627cc662296f7f00 | 627cc662296f7f00 | quieta | 8375817 / 8375817 |
| `docs/loop/ACTA_AUDITOR.md` | c072020f7b7c8b9c | c072020f7b7c8b9c | quieta | 5036598 / 5036598 |
| `docs/loop/PROMPT_SIGUIENTE.md` | e14899642d324038 | e14899642d324038 | quieta | 8281 / 8281 |

**CIFRA sedes cotejadas: 12 | CIFRA que se movieron: 0.**
**LAS DOCE ESTAN QUIETAS, Y ESA ES LA PRUEBA MEDIDA DE QUE ESTA VUELTA NO
ESCRIBIO NI UN NODO, NI UN VEREDICTO, NI UNA FICHA.** La 6.1 prohibe trabajo de
plan al lado de la bateria, y **el cierre integral no es trabajo de plan, es
verificacion**: aqui esta la cifra que lo sostiene. **`docs/loop/ACTA_AUDITOR.md`
y `docs/loop/PROMPT_SIGUIENTE.md`, que son sede del auditor, tambien quedan
quietas.**

### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, MEDIDAS CON EL INSTRUMENTO DE LA CASA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y su salida se cita en el commit
de cierre. **Y ademas va metido como guarda previa en los CUATRO compositores de
tarea de esta vuelta**: los cuatro cuentan las rutas inexistentes o de cero bytes
y los directorios de dos tramos entre comillas inversas **antes de escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO

**Ningun arnes, guarda ni lector nuevo que se quede vigilando, y ninguno
reparado.** **NO SE TOCO EL LANZADOR DE LA BATERIA**, que es lo que el encargo
nombra: `scripts/loop/vuelta183_bateria_por_tramos.py` no cambia ni un byte, y se
uso tal cual. **La nomina sigue CONGELADA EN 135.**

**CONTADO DE `git diff --name-only` entre el HEAD de apertura y el de ahora:
21 fichero(s) tocados en el arbol de scripts del bucle, de los cuales
21 llevan el prefijo `_v215_` y 0 no lo llevan.**

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **`git status --porcelain` al entrar: 1 linea**, y era mi propio
  script de apertura sin rastrear.
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0.**

### 4.2. LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE

- **No escribio el PARA_ALEXIS del bucle, y no lo escribe.** Es **sede del
  auditor** por la adjudicacion `4.2` del acta 203, **linea 71543**, ratificada
  por el fundador el 9 sep 2026. **Yo lo PROPONGO en mi reporte, que es mi
  sede**, y va al final.
- **No escribio una linea en la sede del auditor**, y esta medido arriba con los
  `sha256` quietos.
- **No movio ningun campo `estado`**, y la TAREA 4 lo prueba con los dos `sha256`
  del expediente y su `numstat` en cero.
- **No toco ni un nodo, ni un veredicto, ni la vara del expediente.**
- **No arreglo ningun arnes en rojo**: los trae como PARADA, que es lo que la
  TAREA 2.d manda.
- **No pidio ningun merge. El bucle no funde ramas.**

### 4.3. LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA

- **commit de apertura**: 2026-09-09 07:31:07 -0400
- **ultimo commit al componer este cierre**: 2026-09-09 08:33:27 -0400

## 5. LAS DOS PARADAS QUE TRAIGO, Y NO LAS ARREGLO YO

**`EJECUTOR.md` 5: se para cuando algo contradice una regla vigente o una cifra
publicada con su corte, se escribe en el reporte como PARADA y no lo arregla el
ejecutor.** Aqui van las dos, cada una con su cifra.

### PARADA 1. CAEN 7 ARNESES DE LA NOMINA, Y LA TAREA 2.d MANDA TRAERLOS

**La cifra y los nombres estan en la TAREA 2, tabla de la `2.d`, contados de los
once ficheros sellados.** Lo que importa para la parada es el cotejo: **CAEN
7 y NUEVOS RESPECTO DE LA CORRIDA ANTERIOR: 0.** **Los
7 ya caian en la vuelta 210**, medido con `git show` sobre el commit que
sello cada fichero entonces.

**NO LOS TOCO, Y DOY LOS DOS MOTIVOS:** mi encargo dice con estas palabras que
*"un arnes en rojo en la vuelta del cierre integral no se arregla de paso"*, y
repararlos seria **fabricar maquinaria bajo la moratoria**. **Se suben con su
nombre.**

### PARADA 2. EL ROJO ESTRUCTURAL DE LOS ONCE TRAMOS ES UNA CONTRADICCION ENTRE DOS REGLAS VIGENTES

**Los once tramos salen en exitcode 1 tambien por otra cosa, y esa otra cosa no
la puede apagar ninguna corrida.** La regla que el propio lanzador lleva escrita
desde la vuelta 148 dice que **UN ARNES ENTRA EN LA NOMINA**; la moratoria del 7
sep 2026 (`AUDITOR.md` 6.3) dice que **la nomina queda CONGELADA EN 135,
ni crece ni se poda**. **Mientras las dos rijan, los dos arneses nacidos despues
de la vara 148 se quedan fuera y el rojo es automatico.**

**LO DIGO CON SU PRECEDENTE MEDIDO Y NO RECORDADO:** la bateria de la vuelta 210
encendio **exactamente este mismo rojo, con los dos mismos nombres**, y se
declaro corrida igual. **No propongo cual de las dos reglas cede: eso no es
mio.**

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

- **`D.a` EL VOCABULARIO DE RELLENO DE LA TAREA 4 ES MIO.** Las 23 palabras que
  definen que es un hueco RELLENADO **las elegi yo**, y van escritas enteras en
  el instrumento para que se puedan discutir. **Otra lista habria dado otro
  numero.** Lo que si esta medido es que la que hay **no es demasiado laxa**
  (compara el campo entero, nunca por subcadena) y **no es demasiado estrecha**
  (su caso positivo caza el relleno y el vacio de una entrada fabricada).
- **`D.b` LA REGLA DEL DESCARTE POR VOCABULARIO DEL CAMPO TAMBIEN ES MIA.** Que
  `pendiente` en `estado` sea vocabulario y no relleno **lo decido yo**, aunque
  la evidencia sea mecanica (el mismo campo trae su forma larga). **Sin esa
  regla, el punto 3 saldria NO CUBRE.** **Es el discutible mas caro de esta
  vuelta y por eso va con su tabla de seis filas delante.**
- **`D.c` CORRI LOS ONCE TRAMOS AUNQUE EL PRIMERO SALIERA EN ROJO.** El lanzador
  dice, al acabar un tramo en rojo, *"Y AQUI SE PARA"*. Lo lei como que **para
  ESE tramo**, no la bateria, y segui con `--tramo 2`. **Me apoyo en el
  precedente medido de la vuelta 210, que hizo lo mismo con el mismo rojo**, pero
  **es una lectura mia** y la marco.
- **`D.d` PUBLICO EL PUNTO 3 COMO CUBRE CON UNA BUSQUEDA QUE DA CERO.** Es lo que
  la adjudicacion `5.4` manda, pero **un cero solo vale lo que valga su
  busqueda**, y la mia es la de arriba. **Si el auditor lee que la clausula pide
  otra cosa, el CUBRE se cae y lo digo antes de que lo mida nadie.**

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

**PREGUNTA 1. LOS ONCE TRAMOS SALEN EN EXITCODE 1 POR EL ROJO ESTRUCTURAL. ESO,
LA CASA, LO CUENTA COMO BATERIA CORRIDA O NO?** La `6.1` dice que se declara
corrida cuando los tramos de su reparto tienen **salida sellada del mismo
calibre**, y **los once la tienen**: mismo formato, misma doble corrida, las 135
entradas cubiertas una vez cada una. **Pero once exitcodes en 1 no son un verde**,
y prefiero preguntarlo a decidirlo.

**PREGUNTA 2. LAS CUATRO FICHAS EN HECHA SIN NINGUNA PRUEBA BLOQUEAN EL CIERRE DE
LA CAMPANA?** Mido **4**, el encargo nombra dos, y **ninguna vuelta
las puede cerrar sin escribir en el expediente**, cosa que esta vuelta tiene
prohibida.

**PENDIENTE DE DOCTRINA 1. UN PUNTO EN `A MEDIAS` CUYA SEDE NO EXISTE.** El punto
4 de `OP-I-01` queda en A MEDIAS porque **ningun instrumento del repo escribe la
vista humana** (`CIFRA ficheros .py que la ESCRIBEN: 0`). **Nada dice
si un pendiente sin sede bloquea un cierre de fase o si se declara y se pasa.**

**Y UN PENDIENTE QUE YA NO LO ES, Y LO DIGO PARA QUE NO SE BUSQUE:** el del
marcador contra su cifra vieja **quedo CERRADO por la adjudicacion `5.3`, linea
76166**, y **no lo vuelvo a traer**.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**Son TRES, y las tres las cazaron mis propias guardas ANTES de que el veredicto se
publicara. LA PRIMERA SALIO EN UN COMMIT Y LA CORREGI POR DECLARACION; LAS OTRAS
DOS NO LLEGARON A SALIR.**

- **`D.1` MI PROSA CONTRADECIA A LAS CIFRAS DE SU PROPIO PARRAFO, Y SALIO EN EL
  COMMIT DEL TRAMO 3.** Mi compositor de mensajes de tramo llevaba la frase *"y
  ninguno cae"* **clavada en el texto**, con sus tres ceros tecleados, al lado de
  cifras que si se leian del fichero sellado. En los tramos 1 y 2 coincidieron y
  la mentira no molesto a nadie; **en el 3 el medidor leyo NO MORDIO 1 y la prosa
  siguio diciendo que ninguno cae**. **El texto viejo no se borra: esta en git y
  la correccion va declarada en el commit del tramo 4.** Remedio: la frase se
  **COMPUTA** de las tres cifras, y el instrumento **cae en rojo** si la prosa y
  las cifras no dicen lo mismo. **Mutacion: 5 casos, 0 que no calzan.**
- **`D.2` MI SONDA DEL PUNTO 3 ERA MAS LAXA QUE SU CLAUSULA Y HABRIA PUBLICADO UN
  `NO CUBRE` FALSO.** Contaba **6** campos de relleno, los seis con `pendiente`
  en el campo `estado`, **que ahi no es relleno: es el estado**. **Es la misma
  especie que la `D.7` de la 214**, y esta vez me mordio a mi solo. Remedio: la
  regla del vocabulario del campo, con la forma larga medida en el MISMO campo, y
  **los seis descartes publicados con su nombre**.

- **`C.1` CITE UN FICHERO QUE NO EXISTE COMO SI FUERA RUTA DE PRUEBA, DOS
  VECES, Y ES EXACTAMENTE LA `C.3` DE LA 214 REPITIENDOSE.** El PARA_ALEXIS del
  bucle **todavia no esta escrito**, y nombrarlo entre comillas inversas es una
  ruta que promete prueba apuntando a nada (`EJECUTOR.md` 1, LA RUTA QUE PROMETE
  PRUEBA ES CIFRA). **Me lo conto la guarda de rutas de este mismo compositor,
  que conto 2 rutas malas de 22 y NO ESCRIBIO NADA**, y el texto se reescribio
  sin comillas. **Se registra porque una guarda que muerde y no se cuenta es una
  guarda que la vuelta siguiente no sabe que existe.**

- **`C.2` MI PROPIA CORRECCION DECLARADA LE TAPO EL ASUNTO AL COMMIT DEL TRAMO
  4, Y LO DIGO ANTES DE QUE LO MIDA NADIE.** La salida sellada de
  `scripts/loop/cerrar_reporte.py` publica *"tramo 4 a vuelta None"* y
  *"CIFRA tramos sellados EN LA VUELTA 215: 10"*, **diez de once**. **El que
  falta es el 4 y la causa es mia:** ese lector atribuye cada tramo a su vuelta
  leyendo **el asunto de su ultimo commit**, o sea su primera linea, y el commit
  del tramo 4 **no empieza por el titulo del tramo**: empieza por la correccion
  declarada del mensaje del tramo 3, que meti delante. **El fichero del tramo 4
  SI cambio en un commit de la 215**, y su medicion esta sellada como los otros
  diez. **NO TOCO EL LECTOR:** rige la moratoria y ademas **no esta roto, mide lo
  que dice medir**. **La rama de la seccion 9 sale CORRIDA igual**, porque le
  basta con que al menos un tramo se sellara en esta vuelta, y se sellaron diez.

**Y UNA TERCERA QUE NO CUENTO COMO CAIDA Y DIGO POR QUE, PARA QUE NADIE LA CUENTE
POR MI:** mi compositor de la TAREA 3 salio en **ROJO** en su primera corrida
porque su lector de las cuatro clases del marcador devolvia vacio. **NO ESCRIBIO
NADA.** Eso no es una caida de reporte: **es exactamente la guarda de la TAREA 5
haciendo su trabajo**, y si la contara como caida estaria penalizando lo unico
que el hallazgo `3.1` me pidio construir.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**LA CONDICION DE LA PARADA FELIZ, MEDIDA CONTRA LO QUE EL ENCARGO ESCRIBIO ANTES
DE SABER EL RESULTADO.** El encargo dice: *si la bateria da los ONCE tramos en
verde y del mismo calibre, si el cierre integral sale limpio, y si los dos puntos
de la TAREA 4 quedan medidos y dichos*, entonces la campana esta consumada en lo
que el bucle puede consumar.

**LAS TRES, UNA A UNA, CON MI CIFRA DELANTE:**

1. **LOS ONCE TRAMOS: DEL MISMO CALIBRE SI, EN VERDE NO.** Los once tienen salida
   sellada, las **135** entradas corrieron una vez cada una y dos veces
   cada una, **126 en OK**. **Pero los once exitcodes son 1**, y **caen
   7 arneses**. **NO DECLARO ESTO VERDE.**
2. **EL CIERRE INTEGRAL: LIMPIO.** Gate 0 con sus dos lados y sus dieciocho
   salidas, las tres suites en 0, marcador **3388** y censo calzando
   con las trece cifras del encargo, **0 que no calzan**. **Con una cifra que no
   es verde y no la escondo: 40 fichas de 71 no calzan.**
3. **LOS DOS PUNTOS: MEDIDOS Y DICHOS, SI.** El 3 pasa a **CUBRE** con su
   busqueda corrida; el 4 se queda en **A MEDIAS** con su sede buscada y **no
   encontrada**.

**MI PROPUESTA, Y ES LA UNICA HONESTA CON LAS CIFRAS DE ARRIBA: NO SE DECLARA LA
CAMPANA CONSUMADA EN ESTA VUELTA.** Falla la primera de las tres condiciones, y
falla por una cifra que **ni yo ni la vuelta siguiente podemos apagar sin una
decision del fundador**, porque es la contradiccion de la PARADA 2.

**LO QUE SI PROPONGO QUE HAGA LA 215 DEL AUDITOR, EN SU SEDE Y NO EN LA MIA:**

- **Llevar al fundador las DOS PARADAS**, que son las dos que bloquean el verde:
  la contradiccion entre la regla de la nomina y la moratoria, y los **7**
  arneses que llevan cayendo desde antes de la 210.
- **Decidir, o hacer decidir, la PREGUNTA 1**: once tramos del mismo calibre con
  exitcode 1 estructural, **se cuentan como bateria corrida o no**. De esa
  respuesta cuelga si la condicion 1 se puede dar por cumplida.
- **Y NO ESCRIBIR EL PARA_ALEXIS TODAVIA SI LA RESPUESTA NO LLEGA**,
  porque una parada feliz escrita sobre una condicion que no se cumple es
  exactamente la especie de verde que esta casa lleva doscientas vueltas
  cazando. **Si llega y es que si, quien lo escribe es EL AUDITOR de la 215, no
  su ejecutor**, por la `4.2` del acta 203.
- **Y EL MERGE NO SE PIDE EN NINGUN CASO.** Es decision del fundador y viene
  despues de la auditoria integral con credencial. **El bucle no funde ramas.**

## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE

**CORRIDA ENTERA Y SOLA, Y SU SALIDA VA AQUI COMPLETA Y SIN RECORTAR.**
Fichero: `docs/loop/SALIDA_V183_BATERIA.txt` (**93498 bytes en disco y 93498 normalizado a LF**, **1321 lineas
no vacias**, contadas
por `scripts/loop/cerrar_reporte.py`). **Este instrumento CAE EN ROJO si esta
seccion se queda sin ella**, que es la cuarta de sus cuatro piezas.

```
LA BATERIA DE MUTACIONES DE LA VUELTA 183, CORRIDA ENTERA Y EN TRAMOS
compuesta por scripts/loop/vuelta183_bateria_por_tramos.py --componer

LO QUE SE PARTIO ES EL BOCADO, NO LA BATERIA. Las cuatro cosas que la
letra del fundador del 5 sep 2026 fija siguen enteras: la cadencia (cada
cinco vueltas), la soledad (vuelta propia sin nada al lado), la
integridad (cada entrada corrida, y corrida DOS VECES) y la prohibicion
de podar la nomina.

CIFRA entradas de la nomina: 135
CIFRA tramos: 11
CIFRA entradas que los tramos dicen haber corrido: 135
CIFRA entradas sin correr: 0 | repetidas: 0 | ajenas: 0
LA COBERTURA SE LEYO DE LAS SALIDAS, no se recalculo del reparto.

  tramo 1 -> SALIDA_V183_BATERIA_TRAMO_1.txt: 9552 bytes disco, 9552 bytes LF, 129 lineas, sha256 4de1654fb3bbc04a
  tramo 2 -> SALIDA_V183_BATERIA_TRAMO_2.txt: 7796 bytes disco, 7796 bytes LF, 123 lineas, sha256 8c1f6ce3013bbdd9
  tramo 3 -> SALIDA_V183_BATERIA_TRAMO_3.txt: 8048 bytes disco, 8048 bytes LF, 125 lineas, sha256 f173275916990bbe
  tramo 4 -> SALIDA_V183_BATERIA_TRAMO_4.txt: 7863 bytes disco, 7863 bytes LF, 123 lineas, sha256 44f5c01f680baca5
  tramo 5 -> SALIDA_V183_BATERIA_TRAMO_5.txt: 8270 bytes disco, 8270 bytes LF, 127 lineas, sha256 dbf5328708addc03
  tramo 6 -> SALIDA_V183_BATERIA_TRAMO_6.txt: 8212 bytes disco, 8212 bytes LF, 126 lineas, sha256 8072bd87c785895a
  tramo 7 -> SALIDA_V183_BATERIA_TRAMO_7.txt: 7896 bytes disco, 7896 bytes LF, 123 lineas, sha256 7328143949bcf7fc
  tramo 8 -> SALIDA_V183_BATERIA_TRAMO_8.txt: 7849 bytes disco, 7849 bytes LF, 123 lineas, sha256 8aa2ce1449432ba1
  tramo 9 -> SALIDA_V183_BATERIA_TRAMO_9.txt: 8512 bytes disco, 8512 bytes LF, 125 lineas, sha256 b733d7eeb0287aeb
  tramo 10 -> SALIDA_V183_BATERIA_TRAMO_10.txt: 8473 bytes disco, 8473 bytes LF, 123 lineas, sha256 0ef8f1995e55106f
  tramo 11 -> SALIDA_V183_BATERIA_TRAMO_11.txt: 6269 bytes disco, 6269 bytes LF, 94 lineas, sha256 c58146cb37928b2d
==============================================================================

==============================================================================
TRAMO 1 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_1.txt
==============================================================================

CORRIDA DEL TRAMO 1 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-09T11:45:08Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD f7c3ace1360f, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD f7c3ace1360f, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD f7c3ace1360f, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 1 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta133_tarea2e_mutacion_cifras.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_1.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_2.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_3.py
      ENTRADA DEL TRAMO: vuelta139_2b_mutaciones.py
      ENTRADA DEL TRAMO: vuelta140_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta141_2_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2b_mutacion_bateria.py
      ENTRADA DEL TRAMO: vuelta143_2c_mutacion_positivo.py
      ENTRADA DEL TRAMO: vuelta144_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_2b_mutacion_giro.py
      ENTRADA DEL TRAMO: vuelta144_2d_mutacion_cobertura.py


  vuelta133_tarea2e_mutacion_cifras.py   exit 0  OK                   3.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta135_2e_mutacion_1.py             exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_1.txt
  vuelta135_2e_mutacion_2.py             exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_2.txt
  vuelta135_2e_mutacion_3.py             exit 1  CASO DECLARADO       3.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_3.txt
      SUJETO FIJO VERIFICADO: SUJETO_FIJO_V135_2E_REPORTE_134.md calza con el blob e12e4c36 (sha256 d1f97a510f17e35046eeec4975e1e0a1adabcfdda5a4646a250aa6db
  vuelta139_2b_mutaciones.py             exit 0  OK                   3.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta140_2a_mutaciones.py             exit 2  CASO DECLARADO       3.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta141_2_mutaciones.py              exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2a_mutaciones.py             exit 0  OK                   4.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2b_mutacion_bateria.py       exit 0  OK                   3.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2c_mutacion_positivo.py      exit 0  OK                   4.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2a_mutaciones.py             exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2b_mutacion_giro.py          exit 0  OK                   6.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2d_mutacion_cobertura.py     exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 47.5
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.8
  CIFRA arnes MAS LENTO: vuelta144_2b_mutacion_giro.py con 6.8s
  CIFRA arnes MAS RAPIDO: vuelta144_2d_mutacion_cobertura.py con 2.5s
  CIFRA mediana por arnes, en segundos: 3.2
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta144_2b_mutacion_giro.py                  6.8s
      vuelta143_2a_mutaciones.py                     4.7s
      vuelta143_2c_mutacion_positivo.py              4.6s
      vuelta139_2b_mutaciones.py                     3.7s
      vuelta143_2b_mutacion_bateria.py               3.7s
      vuelta140_2a_mutaciones.py                     3.6s
      vuelta133_tarea2e_mutacion_cifras.py           3.2s
      vuelta135_2e_mutacion_3.py                     3.0s
      vuelta141_2_mutaciones.py                      3.0s
      vuelta135_2e_mutacion_1.py                     3.0s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 2 (vuelta135_2e_mutacion_3.py, vuelta140_2a_mutaciones.py)
      vuelta135_2e_mutacion_3.py, exit declarado 1, marca obligatoria 'NO TIENE CONVENCION MECANICA DE CONTEO':
         su SUJETO FIJO es el REPORTE.md de la vuelta 134, congelado por banco 9.10, y ES ANTERIOR A LOS DELIMITADORES DE CABECERA TALLADA. Medido en esta vuelta: grep -c 'CABECERA TALLADA' docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md da 0, y sobre docs/loop/REPORTE.md da 3. La ampliacion del vocabulario de la TAREA 2.a (vuelta 142) hace que la guarda vea ahora la celda '3 fila(s)' del desfase del calibrado, que EN UN REPORTE MODERNO vive DENTRO de la cabecera delimitada y queda recortada antes de parsear, y en este sujeto no, porque las marcas no existian aun. LAS DOS CIFRAS QUE ESTA MUTACION PRUEBA SI COTEJAN (la salida publica '2 POR ETIQUETA'): lo que cae es una tercera, ajena al caso. El sujeto NO se retoca, porque su valor es estar congelado.
      vuelta140_2a_mutaciones.py, exit declarado 2, marca obligatoria 'VEREDICTO (iii): NO CALZA':
         su bloque (iii), el caso positivo sobre la fase 05, sale NO CALZA y esta DECLARADO desde la vuelta 140: el auditor lo reconocio como caida SUYA de encargo (acta 140, 4.5, 'EL AUDITOR ELIGIO MAL EL SUJETO CONGELADO'). OP-S-05, OP-S-08, OP-S-11 y OP-S-12 tienen HUELLA DE GRAFO IDENTICA (los cuatro campos vacios) y lo unico que las separa es `estado`, que el encargo prohibe mirar: NINGUNA VARA DE GRAFO PUEDE SEPARARLAS. Los bloques (i) y (ii) SI muerden y son los que esta bateria vigila.
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD f7c3ace1360f, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD f7c3ace1360f, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 1: 1
FIN (reloj de pared, UTC): 2026-09-09T11:45:59Z
DURACION DEL TRAMO (monotona, segundos): 50.4
DURACION DEL TRAMO (monotona, minutos): 0.8


==============================================================================
TRAMO 2 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_2.txt
==============================================================================

CORRIDA DEL TRAMO 2 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-09T11:47:36Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD c6a4c70841ed, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD c6a4c70841ed, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD c6a4c70841ed, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 2 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta144_3a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_3b_mutacion_negativa.py
      ENTRADA DEL TRAMO: vuelta144_3c_caso_positivo_1190.py
      ENTRADA DEL TRAMO: vuelta145_2a_mutacion_ancla_unica.py
      ENTRADA DEL TRAMO: vuelta145_2b_mutacion_arneses.py
      ENTRADA DEL TRAMO: vuelta145_2c_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta146_2b_mutacion_ausencias.py
      ENTRADA DEL TRAMO: vuelta147_2c_mutacion_vitalidad.py
      ENTRADA DEL TRAMO: vuelta147_3d_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta147_3e_simular_a26.py
      ENTRADA DEL TRAMO: vuelta148_0d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta148_1a_mutacion_embebido.py
      ENTRADA DEL TRAMO: vuelta148_2a_mutacion_nomina_commiteada.py


  vuelta144_3a_mutaciones.py             exit 0  OK                   4.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3b_mutacion_negativa.py      exit 0  OK                  10.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3c_caso_positivo_1190.py     exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2a_mutacion_ancla_unica.py   exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2b_mutacion_arneses.py       exit 0  OK                  17.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2c_mutacion_censo.py         exit 0  OK                  11.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta146_2b_mutacion_ausencias.py     exit 0  OK                   3.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_2c_mutacion_vitalidad.py     exit 0  OK                  94.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3d_mutacion_nomina.py        exit 0  OK                   4.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3e_simular_a26.py            exit 0  OK                   4.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_0d_mutacion_corredor.py      exit 0  OK                   3.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_1a_mutacion_embebido.py      exit 0  OK                   5.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2a_mutacion_nomina_commiteada.py exit 0  OK                   3.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 170.8
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.8
  CIFRA arnes MAS LENTO: vuelta147_2c_mutacion_vitalidad.py con 94.7s
  CIFRA arnes MAS RAPIDO: vuelta145_2a_mutacion_ancla_unica.py con 2.7s
  CIFRA mediana por arnes, en segundos: 4.8
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta147_2c_mutacion_vitalidad.py            94.7s
      vuelta145_2b_mutacion_arneses.py              17.1s
      vuelta145_2c_mutacion_censo.py                11.4s
      vuelta144_3b_mutacion_negativa.py             10.8s
      vuelta148_1a_mutacion_embebido.py              5.9s
      vuelta147_3d_mutacion_nomina.py                4.8s
      vuelta147_3e_simular_a26.py                    4.8s
      vuelta144_3a_mutaciones.py                     4.5s
      vuelta148_2a_mutacion_nomina_commiteada.py     3.9s
      vuelta148_0d_mutacion_corredor.py              3.8s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD c6a4c70841ed, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD c6a4c70841ed, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 2: 1
FIN (reloj de pared, UTC): 2026-09-09T11:50:28Z
DURACION DEL TRAMO (monotona, segundos): 172.0
DURACION DEL TRAMO (monotona, minutos): 2.9


==============================================================================
TRAMO 3 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_3.txt
==============================================================================

CORRIDA DEL TRAMO 3 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-09T11:51:47Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 8d89cd4c3d36, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 8d89cd4c3d36, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 8d89cd4c3d36, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 3 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta148_2b_mutacion_cifras_conjunto.py
      ENTRADA DEL TRAMO: vuelta148_2c_mutacion_vara_parada.py
      ENTRADA DEL TRAMO: vuelta148_2d_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta150_5c_mutacion_ciclo.py
      ENTRADA DEL TRAMO: vuelta154_tarea2d_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta154_tarea6_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta156_tarea4b_mutacion_tallador.py
      ENTRADA DEL TRAMO: vuelta156_tarea5d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta157_tarea4b_mutacion_tachado.py
      ENTRADA DEL TRAMO: vuelta157_tarea5c_mutacion_ruido.py
      ENTRADA DEL TRAMO: vuelta157_tarea6b_mutacion_re_sellado.py
      ENTRADA DEL TRAMO: vuelta159_tarea6c_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta160_tarea6b_mutacion_puerta.py


  vuelta148_2b_mutacion_cifras_conjunto.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2c_mutacion_vara_parada.py   exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2d_mutacion_exencion.py      exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta150_5c_mutacion_ciclo.py         exit 0  OK                   3.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta154_tarea2d_mutacion_guarda.py   exit 0  OK                  77.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta154_tarea6_mutacion_corredor.py  exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea4b_mutacion_tallador.py exit 0  OK                   3.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea5d_mutacion_corredor.py exit 0  OK                  12.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea4b_mutacion_tachado.py  exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea5c_mutacion_ruido.py    exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea6b_mutacion_re_sellado.py exit 0  OK                   3.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta159_tarea6c_mutacion_exencion.py exit 0  OK                  71.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea6b_mutacion_puerta.py   exit 1  NO MORDIO            2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 191.8
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 3.2
  CIFRA arnes MAS LENTO: vuelta154_tarea2d_mutacion_guarda.py con 77.4s
  CIFRA arnes MAS RAPIDO: vuelta160_tarea6b_mutacion_puerta.py con 2.5s
  CIFRA mediana por arnes, en segundos: 3.1
  CIFRA arneses que pasan de 30 segundos: 2
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta154_tarea2d_mutacion_guarda.py          77.4s
      vuelta159_tarea6c_mutacion_exencion.py        71.4s
      vuelta156_tarea5d_mutacion_corredor.py        12.6s
      vuelta156_tarea4b_mutacion_tallador.py         3.7s
      vuelta150_5c_mutacion_ciclo.py                 3.7s
      vuelta157_tarea6b_mutacion_re_sellado.py       3.4s
      vuelta154_tarea6_mutacion_corredor.py          3.1s
      vuelta157_tarea5c_mutacion_ruido.py            3.1s
      vuelta148_2b_mutacion_cifras_conjunto.py       2.7s
      vuelta148_2c_mutacion_vara_parada.py           2.7s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 1 (vuelta160_tarea6b_mutacion_puerta.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 8d89cd4c3d36, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 8d89cd4c3d36, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 1 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 1 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 3: 1
FIN (reloj de pared, UTC): 2026-09-09T11:55:00Z
DURACION DEL TRAMO (monotona, segundos): 193.1
DURACION DEL TRAMO (monotona, minutos): 3.2


==============================================================================
TRAMO 4 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_4.txt
==============================================================================

CORRIDA DEL TRAMO 4 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-09T11:56:43Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 5721d70bbe78, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 5721d70bbe78, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 5721d70bbe78, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 4 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta160_tarea7c_mutacion_guarda_cita.py
      ENTRADA DEL TRAMO: vuelta161_tarea1a_mutacion_alcance.py
      ENTRADA DEL TRAMO: vuelta162_tarea1a_mutacion_serie.py
      ENTRADA DEL TRAMO: vuelta162_tarea2a_mutacion_puerta.py
      ENTRADA DEL TRAMO: vuelta162_tarea2b_mutacion_excepcion.py
      ENTRADA DEL TRAMO: vuelta162_tarea3_mutacion_fila.py
      ENTRADA DEL TRAMO: vuelta163_tarea1b_mutacion_relectura.py
      ENTRADA DEL TRAMO: vuelta163_tarea1c_mutacion_tramo.py
      ENTRADA DEL TRAMO: vuelta163_tarea2_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta163_tarea4a_mutacion_cobertura.py
      ENTRADA DEL TRAMO: vuelta163_tarea4b_mutacion_re_sellado.py
      ENTRADA DEL TRAMO: vuelta163_tarea5a_mutacion_contador.py
      ENTRADA DEL TRAMO: vuelta164_tarea1_mutacion_registro.py


  vuelta160_tarea7c_mutacion_guarda_cita.py exit 0  OK                   8.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta161_tarea1a_mutacion_alcance.py  exit 0  OK                  10.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea1a_mutacion_serie.py    exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2a_mutacion_puerta.py   exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2b_mutacion_excepcion.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea3_mutacion_fila.py      exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1b_mutacion_relectura.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1c_mutacion_tramo.py    exit 0  OK                   4.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea2_mutacion_nomina.py    exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4a_mutacion_cobertura.py exit 0  OK                   4.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4b_mutacion_re_sellado.py exit 0  OK                  11.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea5a_mutacion_contador.py exit 0  OK                   3.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta164_tarea1_mutacion_registro.py  exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 60.6
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.0
  CIFRA arnes MAS LENTO: vuelta163_tarea4b_mutacion_re_sellado.py con 11.1s
  CIFRA arnes MAS RAPIDO: vuelta162_tarea2a_mutacion_puerta.py con 2.4s
  CIFRA mediana por arnes, en segundos: 3.1
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta163_tarea4b_mutacion_re_sellado.py      11.1s
      vuelta161_tarea1a_mutacion_alcance.py         10.1s
      vuelta160_tarea7c_mutacion_guarda_cita.py      8.4s
      vuelta163_tarea4a_mutacion_cobertura.py        4.7s
      vuelta163_tarea1c_mutacion_tramo.py            4.6s
      vuelta163_tarea5a_mutacion_contador.py         3.6s
      vuelta162_tarea3_mutacion_fila.py              3.1s
      vuelta163_tarea1b_mutacion_relectura.py        2.6s
      vuelta163_tarea2_mutacion_nomina.py            2.5s
      vuelta162_tarea1a_mutacion_serie.py            2.5s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 5721d70bbe78, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 5721d70bbe78, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 4: 1
FIN (reloj de pared, UTC): 2026-09-09T11:57:45Z
DURACION DEL TRAMO (monotona, segundos): 61.9
DURACION DEL TRAMO (monotona, minutos): 1.0


==============================================================================
TRAMO 5 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_5.txt
==============================================================================

CORRIDA DEL TRAMO 5 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-09T12:01:18Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 3c1ae15cf296, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 3c1ae15cf296, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 3c1ae15cf296, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 5 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta164_tarea4_mutacion_005.py
      ENTRADA DEL TRAMO: vuelta165_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta165_tarea2_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta165_tarea4_mutacion_sujeto.py
      ENTRADA DEL TRAMO: vuelta165_tarea6_mutacion_op_l_01.py
      ENTRADA DEL TRAMO: vuelta166_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta166_tarea2_mutacion_correccion.py
      ENTRADA DEL TRAMO: vuelta166_tarea3_mutacion_retrato.py
      ENTRADA DEL TRAMO: vuelta166_tarea6_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta167_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta167_tarea3_mutacion_ii.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_nota.py


  vuelta164_tarea4_mutacion_005.py       exit 0  OK                   5.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea1_mutacion_registro.py  exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea2_mutacion_censo.py     exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea4_mutacion_sujeto.py    exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea6_mutacion_op_l_01.py   exit 1  NO MORDIO            2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta166_tarea1_mutacion_registro.py  exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea2_mutacion_correccion.py exit 1  NO MORDIO            3.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta166_tarea3_mutacion_retrato.py   exit 0  OK                   6.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea6_mutacion_guarda.py    exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta167_tarea1_mutacion_registro.py  exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta167_tarea3_mutacion_ii.py        exit 0  OK                   3.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_registro.py  exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_nota.py      exit 1  NO MORDIO            2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 42.8
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.7
  CIFRA arnes MAS LENTO: vuelta166_tarea3_mutacion_retrato.py con 6.8s
  CIFRA arnes MAS RAPIDO: vuelta168_tarea1_mutacion_nota.py con 2.5s
  CIFRA mediana por arnes, en segundos: 2.7
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta166_tarea3_mutacion_retrato.py           6.8s
      vuelta164_tarea4_mutacion_005.py               5.4s
      vuelta166_tarea2_mutacion_correccion.py        3.3s
      vuelta167_tarea3_mutacion_ii.py                3.2s
      vuelta165_tarea4_mutacion_sujeto.py            2.9s
      vuelta165_tarea2_mutacion_censo.py             2.7s
      vuelta165_tarea6_mutacion_op_l_01.py           2.7s
      vuelta166_tarea1_mutacion_registro.py          2.7s
      vuelta165_tarea1_mutacion_registro.py          2.7s
      vuelta166_tarea6_mutacion_guarda.py            2.7s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 3 (vuelta165_tarea6_mutacion_op_l_01.py, vuelta166_tarea2_mutacion_correccion.py, vuelta168_tarea1_mutacion_nota.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 3c1ae15cf296, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 3c1ae15cf296, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 3 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 3 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 5: 1
FIN (reloj de pared, UTC): 2026-09-09T12:02:02Z
DURACION DEL TRAMO (monotona, segundos): 44.1
DURACION DEL TRAMO (monotona, minutos): 0.7


==============================================================================
TRAMO 6 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_6.txt
==============================================================================

CORRIDA DEL TRAMO 6 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-09T12:02:27Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 69fda8dfa264, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 69fda8dfa264, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 69fda8dfa264, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 6 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta168_tarea2_mutacion_reconstructor.py
      ENTRADA DEL TRAMO: vuelta168_tarea4_mutacion_op_v_01.py
      ENTRADA DEL TRAMO: vuelta169_tarea2_mutacion_reanclaje.py
      ENTRADA DEL TRAMO: vuelta170_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta170_tarea2a_mutacion_aislador.py
      ENTRADA DEL TRAMO: vuelta98_tarea4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta99_tarea3_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta109_tarea2_4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py
      ENTRADA DEL TRAMO: vuelta113_tarea2_mutacion_tsc.py
      ENTRADA DEL TRAMO: vuelta171_mutacion_busqueda_acta.py
      ENTRADA DEL TRAMO: vuelta171_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta171_tarea5a_mutacion_enchufe.py


  vuelta168_tarea2_mutacion_reconstructor.py exit 1  NO MORDIO            2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta168_tarea4_mutacion_op_v_01.py   exit 0  OK                  19.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta169_tarea2_mutacion_reanclaje.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea1a_mutacion_registro.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea2a_mutacion_aislador.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta98_tarea4_prueba_mutacion.py     exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta99_tarea3_prueba_mutacion.py     exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta109_tarea2_4_prueba_mutacion.py  exit 0  OK                   6.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta113_tarea2_mutacion_tsc.py       exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_mutacion_busqueda_acta.py    exit 1  NO MORDIO            2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta171_tarea1a_mutacion_registro.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_tarea5a_mutacion_enchufe.py  exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 53.0
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.9
  CIFRA arnes MAS LENTO: vuelta168_tarea4_mutacion_op_v_01.py con 19.4s
  CIFRA arnes MAS RAPIDO: vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py con 2.4s
  CIFRA mediana por arnes, en segundos: 2.5
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta168_tarea4_mutacion_op_v_01.py          19.4s
      vuelta109_tarea2_4_prueba_mutacion.py          6.0s
      vuelta168_tarea2_mutacion_reconstructor.py     2.9s
      vuelta170_tarea1a_mutacion_registro.py         2.6s
      vuelta171_mutacion_busqueda_acta.py            2.6s
      vuelta171_tarea5a_mutacion_enchufe.py          2.5s
      vuelta98_tarea4_prueba_mutacion.py             2.5s
      vuelta169_tarea2_mutacion_reanclaje.py         2.5s
      vuelta170_tarea2a_mutacion_aislador.py         2.5s
      vuelta113_tarea2_mutacion_tsc.py               2.5s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 2 (vuelta168_tarea2_mutacion_reconstructor.py, vuelta171_mutacion_busqueda_acta.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 69fda8dfa264, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 69fda8dfa264, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 2 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 2 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 6: 1
FIN (reloj de pared, UTC): 2026-09-09T12:03:21Z
DURACION DEL TRAMO (monotona, segundos): 54.3
DURACION DEL TRAMO (monotona, minutos): 0.9


==============================================================================
TRAMO 7 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_7.txt
==============================================================================

CORRIDA DEL TRAMO 7 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-09T12:03:56Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 5bb1155f339d, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 5bb1155f339d, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 5bb1155f339d, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 7 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta172_tarea1b_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta172_tarea2a_mutacion_exclusion.py
      ENTRADA DEL TRAMO: vuelta172_tarea3_mutacion_numeracion.py
      ENTRADA DEL TRAMO: vuelta172_tarea5_mutacion_cierre.py
      ENTRADA DEL TRAMO: vuelta173_tarea1b_mutacion_hueco.py
      ENTRADA DEL TRAMO: vuelta174_tarea1a_mutacion_44.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_esqueleto.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_sellar.py
      ENTRADA DEL TRAMO: vuelta174_tarea2b_mutacion_confirmar.py
      ENTRADA DEL TRAMO: vuelta176_tarea1c_mutacion_tramos.py
      ENTRADA DEL TRAMO: vuelta177_tarea1b_mutacion_esperado_vivo.py
      ENTRADA DEL TRAMO: vuelta177_tarea1d_mutacion_cotejo.py
      ENTRADA DEL TRAMO: vuelta177_tarea1e_mutacion_correcciones_chicas.py


  vuelta172_tarea1b_mutacion_registro.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea2a_mutacion_exclusion.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea3_mutacion_numeracion.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea5_mutacion_cierre.py    exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta173_tarea1b_mutacion_hueco.py    exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1a_mutacion_44.py       exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_esqueleto.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_sellar.py   exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea2b_mutacion_confirmar.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta176_tarea1c_mutacion_tramos.py   exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1b_mutacion_esperado_vivo.py exit 0  OK                   3.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1d_mutacion_cotejo.py   exit 0  OK                   3.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1e_mutacion_correcciones_chicas.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 35.6
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.6
  CIFRA arnes MAS LENTO: vuelta177_tarea1d_mutacion_cotejo.py con 3.4s
  CIFRA arnes MAS RAPIDO: vuelta177_tarea1e_mutacion_correcciones_chicas.py con 2.5s
  CIFRA mediana por arnes, en segundos: 2.6
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta177_tarea1d_mutacion_cotejo.py           3.4s
      vuelta177_tarea1b_mutacion_esperado_vivo.py     3.3s
      vuelta172_tarea1b_mutacion_registro.py         2.8s
      vuelta174_tarea1b_mutacion_esqueleto.py        2.7s
      vuelta173_tarea1b_mutacion_hueco.py            2.7s
      vuelta176_tarea1c_mutacion_tramos.py           2.7s
      vuelta174_tarea2b_mutacion_confirmar.py        2.6s
      vuelta172_tarea3_mutacion_numeracion.py        2.6s
      vuelta172_tarea2a_mutacion_exclusion.py        2.6s
      vuelta172_tarea5_mutacion_cierre.py            2.6s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 5bb1155f339d, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 5bb1155f339d, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 7: 1
FIN (reloj de pared, UTC): 2026-09-09T12:04:33Z
DURACION DEL TRAMO (monotona, segundos): 36.9
DURACION DEL TRAMO (monotona, minutos): 0.6


==============================================================================
TRAMO 8 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_8.txt
==============================================================================

CORRIDA DEL TRAMO 8 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-09T12:04:56Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD e543130004d8, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD e543130004d8, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD e543130004d8, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 8 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta177_tarea1f_mutacion_tope_minutos.py
      ENTRADA DEL TRAMO: vuelta178_tarea1b_mutacion_hermano.py
      ENTRADA DEL TRAMO: vuelta178_tarea1c_mutacion_ast.py
      ENTRADA DEL TRAMO: vuelta178_tarea1d_mutacion_puestos.py
      ENTRADA DEL TRAMO: vuelta178_tarea1e_mutacion_higiene.py
      ENTRADA DEL TRAMO: vuelta178_tarea2_mutacion_resolutor.py
      ENTRADA DEL TRAMO: vuelta178_tarea4_mutacion_consumidas.py
      ENTRADA DEL TRAMO: vuelta150_2d_simular_op_c_05.py
      ENTRADA DEL TRAMO: vuelta160_tarea3b_caso_positivo.py
      ENTRADA DEL TRAMO: vuelta179_tarea1b_mutacion_citas.py
      ENTRADA DEL TRAMO: vuelta179_tarea3_mutacion_triangulos.py
      ENTRADA DEL TRAMO: vuelta179_tarea1d_mutacion_corte.py
      ENTRADA DEL TRAMO: vuelta180_tarea1b_mutacion_etiqueta.py


  vuelta177_tarea1f_mutacion_tope_minutos.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1b_mutacion_hermano.py  exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1c_mutacion_ast.py      exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1d_mutacion_puestos.py  exit 0  OK                   3.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1e_mutacion_higiene.py  exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea2_mutacion_resolutor.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea4_mutacion_consumidas.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta150_2d_simular_op_c_05.py        exit 0  OK                   3.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea3b_caso_positivo.py     exit 0  OK                  11.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea1b_mutacion_citas.py    exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea3_mutacion_triangulos.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea1d_mutacion_corte.py    exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea1b_mutacion_etiqueta.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 44.4
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.7
  CIFRA arnes MAS LENTO: vuelta160_tarea3b_caso_positivo.py con 11.5s
  CIFRA arnes MAS RAPIDO: vuelta179_tarea3_mutacion_triangulos.py con 2.4s
  CIFRA mediana por arnes, en segundos: 2.6
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta160_tarea3b_caso_positivo.py            11.5s
      vuelta150_2d_simular_op_c_05.py                3.8s
      vuelta178_tarea1d_mutacion_puestos.py          3.2s
      vuelta178_tarea1c_mutacion_ast.py              3.1s
      vuelta178_tarea1b_mutacion_hermano.py          2.9s
      vuelta177_tarea1f_mutacion_tope_minutos.py     2.7s
      vuelta178_tarea1e_mutacion_higiene.py          2.6s
      vuelta179_tarea1b_mutacion_citas.py            2.5s
      vuelta180_tarea1b_mutacion_etiqueta.py         2.5s
      vuelta178_tarea2_mutacion_resolutor.py         2.4s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD e543130004d8, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD e543130004d8, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 8: 1
FIN (reloj de pared, UTC): 2026-09-09T12:05:42Z
DURACION DEL TRAMO (monotona, segundos): 45.7
DURACION DEL TRAMO (monotona, minutos): 0.8


==============================================================================
TRAMO 9 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_9.txt
==============================================================================

CORRIDA DEL TRAMO 9 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-09T12:06:22Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 78b08d72d2f7, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 78b08d72d2f7, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 78b08d72d2f7, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 9 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta180_tarea2c_mutacion_cableado.py
      ENTRADA DEL TRAMO: vuelta180_tarea3_mutacion_corte_de_tramos.py
      ENTRADA DEL TRAMO: vuelta180_tarea4_mutacion_texto_y_clon.py
      ENTRADA DEL TRAMO: vuelta180_tarea5_mutacion_backlog_l02.py
      ENTRADA DEL TRAMO: vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py
      ENTRADA DEL TRAMO: vuelta182_tarea2_mutacion_apertura_auditor.py
      ENTRADA DEL TRAMO: vuelta183_tarea1c_mutacion_veredicto.py
      ENTRADA DEL TRAMO: vuelta183_tarea1b_mutacion_atribucion.py
      ENTRADA DEL TRAMO: vuelta184_tarea1c_mutacion_estimacion.py
      ENTRADA DEL TRAMO: vuelta185_tarea1b_mutacion_sin_temporal.py
      ENTRADA DEL TRAMO: vuelta185_tarea1c_mutacion_bateria_continuada.py
      ENTRADA DEL TRAMO: vuelta186_tarea2a_mutacion_pieza4.py
      ENTRADA DEL TRAMO: vuelta186_tarea2b_mutacion_pieza2_cercas.py


  vuelta180_tarea2c_mutacion_cableado.py exit 0  OK                  16.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea3_mutacion_corte_de_tramos.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea4_mutacion_texto_y_clon.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea5_mutacion_backlog_l02.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta182_tarea2_mutacion_apertura_auditor.py exit 0  OK                   3.2s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt
  vuelta183_tarea1c_mutacion_veredicto.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V183_T1C_MUTACION_VEREDICTO.txt
  vuelta183_tarea1b_mutacion_atribucion.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V183_T1B_MUTACION_ATRIBUCION.txt
  vuelta184_tarea1c_mutacion_estimacion.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V184_T1C_MUTACION_ESTIMACION.txt
  vuelta185_tarea1b_mutacion_sin_temporal.py exit 0  OK                   4.2s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt, SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt
  vuelta185_tarea1c_mutacion_bateria_continuada.py exit 1  NO MORDIO            3.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt
      ARNES DE LA RAMA DE LA BATERIA CONTINUADA (vuelta 185, TAREA 1.c)
  vuelta186_tarea2a_mutacion_pieza4.py   exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2A_MUTACION_PIEZA4.txt
  vuelta186_tarea2b_mutacion_pieza2_cercas.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 51.8
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.9
  CIFRA arnes MAS LENTO: vuelta180_tarea2c_mutacion_cableado.py con 16.2s
  CIFRA arnes MAS RAPIDO: vuelta183_tarea1c_mutacion_veredicto.py con 2.5s
  CIFRA mediana por arnes, en segundos: 2.8
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta180_tarea2c_mutacion_cableado.py        16.2s
      vuelta185_tarea1b_mutacion_sin_temporal.py     4.2s
      vuelta185_tarea1c_mutacion_bateria_continuada.py     3.7s
      vuelta182_tarea2_mutacion_apertura_auditor.py     3.2s
      vuelta183_tarea1b_mutacion_atribucion.py       3.1s
      vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py     2.9s
      vuelta180_tarea4_mutacion_texto_y_clon.py      2.8s
      vuelta184_tarea1c_mutacion_estimacion.py       2.7s
      vuelta180_tarea5_mutacion_backlog_l02.py       2.7s
      vuelta180_tarea3_mutacion_corte_de_tramos.py     2.6s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 1 (vuelta185_tarea1c_mutacion_bateria_continuada.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 78b08d72d2f7, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 78b08d72d2f7, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 1 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 1 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 9: 1
FIN (reloj de pared, UTC): 2026-09-09T12:07:15Z
DURACION DEL TRAMO (monotona, segundos): 53.1
DURACION DEL TRAMO (monotona, minutos): 0.9


==============================================================================
TRAMO 10 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_10.txt
==============================================================================

CORRIDA DEL TRAMO 10 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-09T12:07:47Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 61500a1f4b66, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 61500a1f4b66, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 61500a1f4b66, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 10 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta186_tarea2c_mutacion_cierre_tardio.py
      ENTRADA DEL TRAMO: vuelta186_tarea2d_mutacion_seccion4.py
      ENTRADA DEL TRAMO: vuelta187_tarea4_mutacion_dos_convenciones.py
      ENTRADA DEL TRAMO: vuelta187_tarea5b_mutacion_seccion4_tardio.py
      ENTRADA DEL TRAMO: vuelta188_tarea2_mutacion_pata_documental.py
      ENTRADA DEL TRAMO: vuelta188_tarea3c_mutacion_exclusion_por_rojo.py
      ENTRADA DEL TRAMO: vuelta188_tarea4_mutacion_cobertura_parejas.py
      ENTRADA DEL TRAMO: vuelta188_tarea5a_mutacion_vecinos_evitar.py
      ENTRADA DEL TRAMO: vuelta190_tarea2b_mutacion_deuda_y_fallo.py
      ENTRADA DEL TRAMO: vuelta190_tarea3b_mutacion_selladas_ajenas.py
      ENTRADA DEL TRAMO: vuelta191_tarea3_mutacion_lineas.py
      ENTRADA DEL TRAMO: vuelta191_tarea4_mutacion_veredicto.py
      ENTRADA DEL TRAMO: vuelta191_tarea6_mutacion_bloque_tallado.py


  vuelta186_tarea2c_mutacion_cierre_tardio.py exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt
  vuelta186_tarea2d_mutacion_seccion4.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2D_MUTACION_SECCION4.txt
  vuelta187_tarea4_mutacion_dos_convenciones.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt
  vuelta187_tarea5b_mutacion_seccion4_tardio.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V187_T5B_MUTACION_SECCION4_TARDIO.txt
  vuelta188_tarea2_mutacion_pata_documental.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL.txt
  vuelta188_tarea3c_mutacion_exclusion_por_rojo.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt
  vuelta188_tarea4_mutacion_cobertura_parejas.py exit 0  OK                   3.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt
  vuelta188_tarea5a_mutacion_vecinos_evitar.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T5A_MUTACION_VECINOS_EVITAR.txt
  vuelta190_tarea2b_mutacion_deuda_y_fallo.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt
  vuelta190_tarea3b_mutacion_selladas_ajenas.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt
  vuelta191_tarea3_mutacion_lineas.py    exit 0  OK                  61.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T3_MUTACION_LINEAS.txt
  vuelta191_tarea4_mutacion_veredicto.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T4_MUTACION_VEREDICTO.txt
  vuelta191_tarea6_mutacion_bloque_tallado.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T6_MUTACION_BLOQUE_TALLADO.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 95.6
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.6
  CIFRA arnes MAS LENTO: vuelta191_tarea3_mutacion_lineas.py con 61.0s
  CIFRA arnes MAS RAPIDO: vuelta190_tarea3b_mutacion_selladas_ajenas.py con 2.5s
  CIFRA mediana por arnes, en segundos: 2.8
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta191_tarea3_mutacion_lineas.py           61.0s
      vuelta188_tarea4_mutacion_cobertura_parejas.py     3.4s
      vuelta186_tarea2d_mutacion_seccion4.py         3.1s
      vuelta191_tarea6_mutacion_bloque_tallado.py     3.1s
      vuelta187_tarea4_mutacion_dos_convenciones.py     3.1s
      vuelta186_tarea2c_mutacion_cierre_tardio.py     3.0s
      vuelta190_tarea2b_mutacion_deuda_y_fallo.py     2.8s
      vuelta188_tarea3c_mutacion_exclusion_por_rojo.py     2.7s
      vuelta187_tarea5b_mutacion_seccion4_tardio.py     2.7s
      vuelta191_tarea4_mutacion_veredicto.py         2.7s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 61500a1f4b66, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 61500a1f4b66, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 10: 1
FIN (reloj de pared, UTC): 2026-09-09T12:09:24Z
DURACION DEL TRAMO (monotona, segundos): 97.0
DURACION DEL TRAMO (monotona, minutos): 1.6


==============================================================================
TRAMO 11 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_11.txt
==============================================================================

CORRIDA DEL TRAMO 11 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-09T12:10:01Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD c6d29b754069, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD c6d29b754069, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD c6d29b754069, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 11 de 11
  CIFRA entradas de ESTE tramo: 5
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta192_tarea4_mutacion_cuarta_puerta.py
      ENTRADA DEL TRAMO: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      ENTRADA DEL TRAMO: vuelta194_tarea2c_mutacion_sede_del_turno.py
      ENTRADA DEL TRAMO: vuelta195_tarea3g_mutacion_nomina_enchufada.py
      ENTRADA DEL TRAMO: vuelta195_tarea4c_mutacion_componer_rojo.py


  vuelta192_tarea4_mutacion_cuarta_puerta.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt
  vuelta193_tarea4e_mutacion_sello_entre_procesos.py exit 0  OK                   3.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt
  vuelta194_tarea2c_mutacion_sede_del_turno.py exit 0  OK                   5.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt, SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt, SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt
  vuelta195_tarea3g_mutacion_nomina_enchufada.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V195_T3G_MUTACION_NOMINA_ENCHUFADA.txt
  vuelta195_tarea4c_mutacion_componer_rojo.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V195_T4C_MUTACION_COMPONER_ROJO.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 5
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 17.7
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.3
  CIFRA arnes MAS LENTO: vuelta194_tarea2c_mutacion_sede_del_turno.py con 5.5s
  CIFRA arnes MAS RAPIDO: vuelta192_tarea4_mutacion_cuarta_puerta.py con 2.7s
  CIFRA mediana por arnes, en segundos: 3.1
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta194_tarea2c_mutacion_sede_del_turno.py     5.5s
      vuelta193_tarea4e_mutacion_sello_entre_procesos.py     3.8s
      vuelta195_tarea4c_mutacion_componer_rojo.py     3.1s
      vuelta195_tarea3g_mutacion_nomina_enchufada.py     2.7s
      vuelta192_tarea4_mutacion_cuarta_puerta.py     2.7s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD c6d29b754069, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD c6d29b754069, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 11: 1
FIN (reloj de pared, UTC): 2026-09-09T12:10:20Z
DURACION DEL TRAMO (monotona, segundos): 19.1
DURACION DEL TRAMO (monotona, minutos): 0.3
```
