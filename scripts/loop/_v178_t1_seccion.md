### TAREA 1. LOS REGISTROS Y LAS CORRECCIONES

**LAS CINCO LETRAS ENTREGADAS, LAS CUATRO QUE TOCAN CODIGO CON ARNES PROPIO Y LOS
CUATRO ARNESES DENTRO DE LA NOMINA EN SU MISMA VUELTA.** Ninguna cifra de aqui
esta tecleada: cada una cita el fichero de salida del que sale y ese fichero se
cuenta antes de publicarla (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO).

#### 1.a. LA RELECTURA AL DOBLE DEL TRAMO DE LA CAIDA, ESCRITA ENTERA

**MI CAIDA DE LA 177, SIN TAPARLA.** Publique en prosa que *"el censo ve 153
arneses"* y que *"los 2 de la 177 no lo eran, la nomina va de 89 a 92"*. **Las dos
cifras estaban mal.** El auditor midio 154 y TRES, commit a commit, y su medicion
es la que gobierna. **El fondo era correcto y la accion fue correcta** (los cuatro
arneses entraron y la nomina fue de 88 a 92 sin podar ninguna); lo que estaba mal
eran los numeros.

**Y LA CAIDA SE DELATABA SOLA, QUE ES EL MOTIVO ENTERO DE ESTA LETRA:** 153 menos
92 son 61, y el mismo reporte publicaba 62 dos parrafos mas abajo. **En prosa cada
cifra suelta parece verdadera; en una tabla con su resta al lado, la que sobra
canta.** Por eso el instrumento nace imprimiendo la resta dentro.

**LA TABLA, PEGADA DE `docs/loop/SALIDA_V178_T1A_CUENTA.txt` y contada de ese
fichero.** Instrumento: `scripts/loop/vuelta178_tarea1a_cuenta_censo.py`.

| que se cuenta | instrumento | en la APERTURA | al CIERRE DE LA TAREA 1 |
|---|---|---|---|
| arneses que ve el censo | `arneses_del_directorio()` | **154** | **158** |
| entradas de la nomina | `len(VIEJAS)` | **92** | **96** |
| del censo, FUERA de la nomina | conjuntos | **62** | **62** |
| de la nomina que el censo NO VE | `nomina_invisible_al_censo()` | **0** | **0** |
| del censo y de la nomina a la vez | conjuntos | **92** | **96** |

**LAS DOS COLUMNAS VAN LAS DOS, y la de la izquierda es de la APERTURA de verdad:**
sale del bloque H.5 de `docs/loop/SALIDA_V178_APERTURA.txt`, sellado antes de la
primera operacion. **LA OPERACION QUE MOVIO LA COLUMNA DERECHA TIENE NOMBRE:** los
CUATRO arneses que esta misma TAREA 1 escribe entran en el censo y en la nomina a
la vez, asi que las dos suben cuatro y **la resta no se mueve**.

**LA RESTA COMPROBADA, que es lo que caza una cifra suelta:**

| identidad | apertura | cierre | calzan |
|---|---|---|---|
| censo menos nomina igual a (fuera de nomina) menos (invisibles) | 154 menos 92 igual 62, contra 62 menos 0 igual 62 | 158 menos 96 igual 62, contra 62 menos 0 igual 62 | **SI las dos** |
| censo menos nomina igual a fuera de nomina (solo si invisibles son 0) | 62 contra 62 | 62 contra 62 | **SI las dos** |

**LAS SEDES, AL LADO Y SIN BORRAR NINGUNA** (banco 9.10):

| sede | censo | nomina | faltaban | su resta | cuadra consigo misma |
|---|---|---|---|---|---|
| reporte de la 177, mio, prosa del cuerpo | 153 | 92 | 2 | 61 | **NO**: su resta da 61 y fuera de la nomina hay 62 |
| acta 178 del auditor, commit a commit | 154 | 92 | 3 | 62 | SI |
| medicion de HOY, apertura | 154 | 92 | 0 con la funcion vieja | 62 | SI |
| medicion de HOY, cierre de la TAREA 1 | 158 | 96 | 2, y se nombran en la 1.b | 62 | SI |

#### 1.b. `arneses_que_faltan()` ARREGLADA EN LA FUNCION, CON LA VARA EXPLICITA

**QUE SE CAMBIO.** El filtro viejo era *"vuelta estrictamente posterior a la ultima
de la nomina"*, y esa vara vivia **implicita dentro de un signo de comparacion**.
El nuevo es el que el encargo escribe: **esta en el censo y NO esta en la nomina,
menos los anteriores a la vara del censo.** Se arreglo LA FUNCION, no la llamada.

**LA VARA ES 148 Y TIENE SU MOTIVO ESCRITO AL LADO, no un numero suelto.** La
letra del propio fichero *desde la vuelta 148* dice que un arnes entra en la
nomina y que la condicion es sujeto congelado, no plazo; y todo lo anterior a la
148 **ya se midio y ya se adjudico fuera**: `scripts/loop/vuelta164_tarea5_medir_pre148.py`
lo hizo con `CORTE = 148` por la adjudicacion 6.9 del acta 163, y su primer punto
dice *"NINGUNO ENTRA EN VIEJAS"*. **Ensanchar la vara hacia atras sin adjudicacion
nueva seria legislar**, asi que no se ensancha. La vara va ademas **por parametro**,
que es lo que permite que su arnes la mueva sin tocar el fichero.

**LA NOMINA NO SE PODO. CRECE DE 92 A 96** con los cuatro arneses de esta vuelta,
y **esta vez no se anadieron a ciegas**: la funcion arreglada los nombro ella sola
antes de que se escribieran sus cuatro lineas.

**EL CASO POSITIVO POR MUTACION, CON LAS DOS CORRIDAS DEL MISMO CASO.** Vive en
`scripts/loop/vuelta178_tarea1b_mutacion_hermano.py` y su salida en
`docs/loop/SALIDA_V178_T1B_MUTACION.txt`. La funcion vieja **no se re-implemento**:
esta congelada en `scripts/loop/_v178_arneses_que_faltan_viejo_copia.py`, porque un
caso rojo que no se puede correr no es una prueba.

| el caso | la funcion NUEVA | la funcion VIEJA |
|---|---|---|
| directorio con `vuelta200_a_mutacion_dentro.py` y `vuelta200_b_mutacion_fuera.py`, nomina con solo el primero | **VE al de fuera** | **NO lo ve** |
| CIFRA que dice que faltan | 1 | 0 |

**Es la caida de la 177 entera reproducida sobre un directorio de mentira.** El
arnes da **5 casos, los 5 pasan y los 5 CAEN** al mutarles el esperado, y la vara
se prueba MOVIENDOLA (con la vara en 100 el arnes de la vuelta 50 no se reclama;
con la vara en 0 si), no afirmandola. La prueba de la nomina de la propia bateria
pasa de 5 casos a **8, los 8 pasan y los 8 caen**
(`docs/loop/SALIDA_V178_T1B_NOMINA.txt`), y su caso `E` **se re-fundo**: antes
exigia que en el repo de hoy no faltara ninguno, que es una expectativa sobre el
estado del repo y no sobre la conducta de la funcion; ahora **re-deriva el
resultado por conjuntos sin llamarla** y exige que calcen.

**LO QUE LA VARA ARREGLADA DESTAPA, Y ES UN HALLAZGO Y NO UN EFECTO SECUNDARIO.**
Con el filtro correcto, **DOS arneses del censo que no estan en la nomina y que no
son anteriores a la vara aparecen por primera vez**:
`vuelta150_2d_simular_op_c_05.py` y `vuelta160_tarea3b_caso_positivo.py`. **La
funcion vieja no podia verlos jamas.** Los corri una vez cada uno para que la
decision se tome con cifras y no a ojo
(`docs/loop/SALIDA_V178_T1B_LOS_DOS_DESTAPADOS.txt`):

| arnes | exit | lineas de salida | `git diff --numstat -- dataset/` tras correrlo |
|---|---|---|---|
| `vuelta150_2d_simular_op_c_05.py` | 0 | 35 | 0 filas |
| `vuelta160_tarea3b_caso_positivo.py` | 0 | 62 | 0 filas |

**NO LOS METI EN LA NOMINA, y digo por que sin adornarlo:** meterlos compromete a
la bateria de la 181 a correrlos DOS VECES cada uno con cotejo de reproducibilidad,
y eso es una decision sobre lo que la 181 corre, que no esta en este encargo. **Lo
dejo medido, nombrado y con su consecuencia dicha en voz alta: mientras no entren,
la bateria de la 181 dara ROJO por esta cuenta**, y ese rojo sera correcto. Va como
pregunta `P.1` y marcado como **DISCUTIBLE**.

#### 1.c. EL CUARTO VEREDICTO DE `cotejar_clon_declarado.py`, EL ARBOL DE SINTAXIS

**LA CLASIFICACION VIEJA NO SE TOCO Y SIGUE PUBLICANDO SU 1.** Lo que se anade es
una vara distinta AL LADO, y las dos mitades que el docstring del propio fichero
pedia: `AST DEL FICHERO ENTERO` y `AST SIN EL DOCSTRING`. **El docstring de un clon
cambia siempre**, asi que un unico AST sobre el fichero entero diria DIFIERE en
todos los clones reales y no responderia nada.

**EL CASO QUE LO DECIDE TODO, CORRIDO Y NO PROMETIDO** (caso 1 de
`docs/loop/SALIDA_V178_T1C_MUTACION.txt`): dos ficheros que solo se diferencian en
**una coma final**.

| vara | veredicto |
|---|---|
| SOLO LA MAQUINA (lineas y tokens) | **DIFIERE** |
| SENTENCIAS DE CODIGO que la clasificacion vieja cuenta | **1** |
| AST DEL FICHERO ENTERO | **IDENTICO** |
| AST SIN EL DOCSTRING | **IDENTICO** |

**Las dos cifras son verdaderas y ahora estan las dos en el mismo sitio**, que es
exactamente lo que el acta 177 punto 7.7 pedia.

**CAE EN ROJO SI UN FICHERO NO PARSEA, Y LO DICE CON SU LINEA.** Comprobado de
extremo a extremo dentro del arnes: sobre un fichero roto el instrumento imprime
`SyntaxError en la linea 9: invalid syntax` y sale con **exit 1**; con los dos
ficheros buenos, **exit 0**. El arnes da **20 casos, los 20 pasan y los 20 CAEN**.
**Y EL ARNES VIEJO NO SE TOCO Y SIGUE VERDE:** `vuelta177_tarea1d_mutacion_cotejo.py`
da **28 casos, los 28 pasan y los 28 caen** (`docs/loop/SALIDA_V178_T1C_ARNES_VIEJO.txt`).

**EL INSTRUMENTO ENTERO SOBRE EL PAR DEL ACTA 176**, pegado en
`docs/loop/SALIDA_V178_T1C_COTEJO_176.txt` (`vuelta175_esqueleto_reporte.py` contra
`vuelta176_esqueleto_reporte.py`, con 175 y 176 sustituidos por NNN en los dos):

| vara | resultado |
|---|---|
| FICHERO ENTERO | DIFIERE |
| SOLO DOCSTRING | DIFIERE |
| SOLO LA MAQUINA | DIFIERE, 33 lineas |
| SENTENCIAS DE CODIGO / LITERALES DE TEXTO | **1 y 32** |
| tokens de maquina | A 1.260, B 1.259, y **1 token** que difiere |
| AST DEL FICHERO ENTERO | DIFIERE |
| AST SIN EL DOCSTRING | DIFIERE |
| nodos del arbol sin docstring | A **1.368**, B **1.368** |
| tipos de nodo que NO empatan | **0** |

**Y ESTO EXPLICA EL 0 DEL AUDITOR Y EL 1 DEL INSTRUMENTO EN EL MISMO SITIO, que es
lo que se pedia.** El censo de nodos por tipo **empata exactamente** y el total es
el mismo a los dos lados: **la forma del programa es identica**, y lo que difiere
es el VALOR de nodos de texto mas UN token que no es un nodo. La cifra 1 del
instrumento es verdadera midiendo tokens; el 0 del auditor es verdadero mirando lo
que el programa hace. **DISCUTIBLE:** el AST de este par sale DIFIERE por los
valores de texto, asi que en este par concreto el cuarto veredicto NO exonera solo,
y lo que exonera es la fila de los tipos de nodo. Lo traigo tal cual en vez de
redondearlo.

#### 1.d. EL `--puestos` Y EL `--excluir` DEL AISLADOR DE CIEGA

**LOS DOS, COMPONIBLES CON LOS SELECTORES VIEJOS Y CON EL ORDEN ESCRITO EN EL
FICHERO:** primero dominio, clase, banda y rango; **despues** la lista. `--dominio
ventas --puestos 334,404` es *"de los de ventas, esos dos"*, y eso esta probado y
no supuesto.

**CAE EN ROJO SI UN PUESTO PEDIDO NO EXISTE, NOMBRANDOLO, y la comprobacion es
contra EL ARCHIVO ENTERO y no contra la seleccion**, para que "no existe" y "lo
filtro otro selector" no se confundan. El rojo alcanza tambien a `--excluir`, y se
declara por que: el universo de los dos es el mismo archivo.

**CORRIDO SOBRE EL ARCHIVO DE VERDAD** (`docs/loop/SALIDA_V178_T1D_DEMO.txt`):
3.388 filas, `--puestos 334,394,404 --excluir 878`, **3 pares elegidos**, **0 fugas
del destape**, y las dos salidas escritas. **Y EL ROJO, CORRIDO TAMBIEN**
(`docs/loop/SALIDA_V178_T1D_ROJO_DEMO.txt`): `--puestos 334,999999` sale con
**exit 1**, imprime `NO EXISTE EN EL ARCHIVO: puesto 999999` y **no escribe nada**.

**LA GUARDA DE FUGA NO SE TOCO Y SE COMPROBO QUE SIGUE MORDIENDO SOBRE LA SELECCION
NUEVA**, de las dos maneras: con la lista blanca de siempre da **0 fugas**, y
ensanchada a `clase` y `razon` sobre una seleccion hecha con `--puestos` **caza las
6** de los tres pares. El arnes
(`scripts/loop/vuelta178_tarea1d_mutacion_puestos.py`,
`docs/loop/SALIDA_V178_T1D_MUTACION.txt`) da **24 casos, los 24 pasan y los 24
CAEN**, y **no lee `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en ningun caso**: fabrica
sus cinco filas.

**Y LA MULETA SE BORRA, QUE ES `P.16`.** `scripts/loop/_auditor_v178_ciega.py`
(3.479 bytes en disco y 3.479 en git, medidos en el bloque H.7 de la apertura) **ya
no existe en el arbol**: el lanzador hace su trabajo.

#### 1.e. LAS DOS DE HIGIENE, LAS DOS CON GUARDA Y NO CON FRASE

**(1) LA PAREJA DE CIFRAS, CABLEADA DONDE SE CUMPLE SOLA.**
`scripts/loop/cerrar_reporte.py` **CAE EN ROJO** si el reporte publica una cifra de
bytes o un sha **sin su pareja**. La regla es mecanica y esta escrita en el propio
fichero: una cifra esta emparejada si en su MISMA LINEA hay dos o mas apariciones
de su especie, o si la linea nombra al menos DOS marcas de convencion (`disco`,
`LF`, `normalizado`, `cat-file`, `getsize`). **Quedan fuera los bloques cercados**,
porque ahi va pegada la salida cruda de un instrumento y **una cita que se retoca
deja de ser una cita**; y los sha **solo se buscan en lineas que digan `sha`**, para
no confundir un hash corto de commit, que es identidad, con el sha de un contenido.
**Y el propio `cerrar_reporte.py` se puso al dia:** su cabecera y su seccion 9
publican ahora las dos cifras, disco y LF.

**Esto es la mitad de mi propia falta de la 177**, que declaraba publicar las dos y
luego no lo hizo en dos celdas: un tallador en "5.001 bytes" cuando el disco decia
5.021, y un sha `7d683eea4700f18b` que era el de LF. **Las dos cifras eran
verdaderas y las dos hubo que ir a buscarlas.**

**(2) LA GUARDA DEL SUJETO CONGELADO, QUE LLEVA DESDE LA VUELTA 145 SIENDO UNA
FRASE.** Ahora es un instrumento: `verificar_mutaciones_viejas.py
--sujeto-congelado`. Clasifica por la huella que el sujeto deja EN EL CODIGO, y **la
huella de sujeto vivo se busca SOLO en la maquina, sin el docstring de modulo**,
porque un docstring que NOMBRA un fichero no lo abre. **La clasificacion es de
cuatro estados y no de dos**: si un arnes trae las dos huellas, la guarda NO ADIVINA
y pide que el propio arnes lo declare; sin esa declaracion sale `NO DECIDIBLE`, y
**NO DECIDIBLE no es verde**.

**LO QUE MIDE HOY, contado de `docs/loop/SALIDA_V178_T1E_CONGELADO.txt`:**

| veredicto | entradas |
|---|---|
| CONGELADO | **75** |
| CASO DECLARADO | **2** |
| SUJETO VIVO | **7** |
| NO DECIDIBLE | **8** |
| **total** | **92** |

**LA GUARDA SALE EN ROJO, exit 1, con 15 de 92.** Entre las 7 de `SUJETO VIVO` esta
`vuelta166_tarea2_mutacion_correccion.py`, que es **el mismo arnes cuyo esperado
tecleado la 177 tuvo que arreglar**: la guarda caza sola el caso que motivo su
propia peticion. **NO LA CABLEE AL ROJO GLOBAL DE LA BATERIA, y digo por que:**
hacerlo pondria la bateria de la 181 en rojo por 15 entradas cuyo estado real hay
que juzgar UNA A UNA, y eso no esta en este encargo. **La guarda existe, corre sola
y cae en rojo en su propio carril**, que es lo que "entra aqui y no se aplaza otra
vez" pide; lo que queda por decidir es su cableado, y va como pregunta `P.2` y
marcado **DISCUTIBLE**.

**Su arnes** es `scripts/loop/vuelta178_tarea1e_mutacion_higiene.py`
(`docs/loop/SALIDA_V178_T1E_MUTACION.txt`), **16 casos, los 16 pasan y los 16
CAEN**, y prueba las dos guardas: la de la pareja caza una cifra de bytes sola y un
sha solo, deja pasar las emparejadas, no se equivoca con un hash corto ni entra en
los bloques cercados; la del sujeto congelado separa los cuatro estados **y no acusa
a un arnes por NOMBRAR un fichero vivo en su docstring**, que es el falso rojo que
la primera version si tenia.
