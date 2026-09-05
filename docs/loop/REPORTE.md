# REPORTE DE LA VUELTA 178 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta178_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y LA CADENCIA NO SE ELIGE AQUI: ESTA
> ADJUDICADA Y RECONFIRMADA.** El acta 176, punto 7.8, reanclo el contador a la
> vuelta que de verdad corrio la bateria y no a la que la tenia encargada, y el
> encargo de esta vuelta lo repite con todas las letras: **la proxima vuelta de
> bateria es la 181**, y la 178, la 179 y la 180 cierran su seccion 9 con el
> **HUECO DECLARADO Y MEDIDO**, con su nombre, sus bytes medidos y su atribucion,
> las tres juntas. Un hueco declarado no es un hueco escondido.
>
> **EL TOPE VUELVE A CINCO, Y NO LO DECIDE NADIE: LO DISPARO LA VUELTA
> ANTERIOR.** `AUDITOR.md` 6.2 dice que el regimen temporal de dos sub-tareas
> dura **hasta que DOS vueltas seguidas cierren su propio reporte** con
> `cerrar_reporte.py`. **La 176 y la 177 lo hicieron, cada una en su misma
> vuelta, y las dos archivaron ademas su reporte sin esperar a la siguiente.**
> El tope vuelve a CINCO por la propia letra de la 6.2, sin que nadie tenga que
> decidirlo, y este encargo trae cinco. **El regimen temporal queda CUMPLIDO Y
> CITABLE, no borrado**, y los cuatro commits que lo cumplen se localizan EN GIT
> en el bloque B.1 de `scripts/loop/vuelta178_apertura.py`, no se teclean.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, QUE ES LA CAIDA
> PROPIA QUE LA 177 SE ANOTO.** El remedio quedo cableado en
> `vuelta177_apertura.py` y aqui se estrena de verdad: el medidor corre dentro
> del bloque de apertura, antes de la primera operacion. **Desde esta vuelta, una
> columna de apertura medida al cierre es caida que ACUMULA**, y eso lo dice el
> encargo, no este reporte.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas coinciden, porque la
> 177 escribio su reporte, lo cerro y lo archivo; el fichero corre LAS DOS
> igualmente y publica lo que salga de cada una, porque una guarda que solo se
> mira cuando difiere no se puede auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta178_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 177: `77621a68`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 177: LAS DOS TAREAS ENTERAS Y TODO LO QUE PUBLICA REPRODUCE BAJO MI MANO SALVO UNA FRASE, Y EL TOPE VUELVE A CINCO PORQUE LA VUELTA LO DISPARO.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V178_HEAD_APERTURA.txt`: `77621a68`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `531efee1`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **177**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 178`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LAS CORRECCIONES, Y ES BLOQUEANTE. Cinco letras: (a) LA RELECTURA AL DOBLE DEL TRAMO DE LA CAIDA de conteo del acta 177, la cuenta de la nomina y del censo, publicada ENTERA en tabla y con la resta comprobada, porque una cuenta que no cierra consigo misma se caza sola si alguien la escribe entera; (b) `arneses_que_faltan()` SE ARREGLA en la funcion y no en la llamada, con la vara del censo EXPLICITA y con su motivo, sin podar la nomina, y con el caso positivo por mutacion que hoy CAE con la funcion vieja: dos arneses de la MISMA vuelta que la ultima de la nomina, uno dentro y otro fuera, y la funcion tiene que VER al de fuera; (c) EL CUARTO VEREDICTO de `cotejar_clon_declarado.py`, EL ARBOL DE SINTAXIS, sin tocar la clasificacion vieja, en rojo si un fichero no parsea, y con el caso que lo decide todo: dos ficheros que solo difieren en una coma final dan maquina DIFIERE y AST IDENTICO; (d) EL `--puestos` Y EL `--excluir` DEL AISLADOR DE CIEGA, componibles con los selectores que ya tiene, en rojo si un puesto pedido no existe, con la guarda de fuga intacta, y borrando despues la muleta `_auditor_v178_ciega.py` por `P.16`; (e) LAS DOS DE HIGIENE: que `cerrar_reporte.py` CAIGA EN ROJO si el reporte publica una cifra de bytes o un sha sin su pareja, y LA GUARDA DEL SUJETO CONGELADO, que lleva desde la vuelta 145 siendo una frase y no un instrumento | **CERRADA. Las cinco letras entregadas, las cuatro que tocan codigo con arnes propio, y los cuatro arneses DENTRO de la nomina en su misma vuelta** | `SALIDA_V178_T1A_CUENTA.txt`, `_T1B_MUTACION.txt`, `_T1B_NOMINA.txt`, `_T1B_LOS_DOS_DESTAPADOS.txt`, `_T1C_MUTACION.txt`, `_T1C_ARNES_VIEJO.txt`, `_T1C_COTEJO_176.txt`, `_T1D_MUTACION.txt`, `_T1D_DEMO.txt`, `_T1D_ROJO_DEMO.txt`, `_T1E_MUTACION.txt`, `_T1E_CONGELADO.txt` |
| **TAREA 2** | `OP-L-03`: SE RE-MIDE EL BACKLOG ENTERO ANTES DE LEER UN ACTO MAS. No se toca `backlog_l03_vuelta14.py`, que sostiene una cifra adjudicada en la vuelta 15; se escribe el filtro DELANTE, en `scripts/loop/backlog_l03_resuelto.py`, de nombre estable y sin numero de vuelta, que corre el instrumento viejo y le pasa el resolutor de `P.1` por encima publicando LAS DOS COLUMNAS AL LADO. Por acto y en total: miembros escritos, vivos por el resolutor, vivos por el campo `deprecado` del grafo, SI LOS DOS CAMINOS CALZAN, pares que el instrumento da, pares reales y pares disueltos. CAE EN ROJO si los dos caminos no calzan en algun acto, nombrandolo. Con su caso positivo por mutacion sobre un mapa de alias FABRICADO. Y publica la cifra que la 177 no pudo publicar: cuanto sobra en los 34 actos que no miro. EL ESTADO DE LA FICHA NO SE TOCA | **CERRADA. El backlog re-medido entero: de 73 pares del instrumento quedan 18 reales, y en los 34 actos sin leer quedan 10** | `SALIDA_V178_T2_BACKLOG_RESUELTO.txt`, `SALIDA_V178_T2_MUTACION.txt` |
| **TAREA 3** | LOS CINCO TRIANGULOS `A` MAS `A` MAS `D`: SE ANOTAN CON SU REGLA, NO SE MUEVEN. La `P.3` de la 177 queda adjudicada como COSA JUZGADA en el acta 177 punto 7.9: las dos reglas que lo deciden ya estan escritas y RESULTAN COMPATIBLES. La `9.6.1` del banco dice que un nodo que es un paso de otro y NO TRAE PROCEDIMIENTO PROPIO, REPITE; la correccion declarada del 13 ago 2026 sobre los puestos 530 y 863 dice que la madre y su pieza de arenas se separan. La condicion que las concilia es la que la propia `9.6.1` escribe: SI LA PIEZA TRAE PROCEDIMIENTO PROPIO SE SEPARA, SI ES EL PASO DICHO OTRA VEZ, REPITE. Por cada uno de los cinco se anota EN EL JSONL cual de las dos reglas gobierna cada lado y CON QUE PRUEBA. CERO VEREDICTOS MOVIDOS | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LA CEGUERA DE LA VARA, QUE LLEVA DOS VUELTAS CONTADA. `vuelta150_3_relectura_expediente.py` imprime SEIS fichas en LISTA sin prueba y dos de las seis estan CONSUMIDAS por otras, asi que el trabajo real son CUATRO. La vara es del fundador y su veredicto NO SE TOCA: lo que se anade es una COLUMNA, no una exclusion. Que siga imprimiendo las seis y que diga de cada una si esta CONSUMIDA por otra ficha y por cual. La cuenta final publica LAS DOS, nunca solo el cuatro. Con su caso positivo por mutacion sobre un expediente fabricado | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA COMO SIEMPRE: la segunda sede de la clausula 4.4 en `REPORTE_V172.md:535`; el docstring de `paso0_archivar_anterior.py`; la guarda que falta en la dependencia del `D.4` de la 174; y la medicion del grano del tope de 10 minutos, que se mide EN LA 181 con el reloj de esa corrida y no se re-elige a ojo antes. Ninguna de las cuatro se toca aqui, y las cuatro se nombran para que no se caigan | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

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

### TAREA 2. `OP-L-03`: EL BACKLOG SE RE-MIDE ENTERO ANTES DE LEER UN ACTO MAS

**LO QUE SALE, DICHO PRIMERO PORQUE CAMBIA EL TAMANO DE LO QUE QUEDA: DE LOS 73
PARES QUE EL INSTRUMENTO DA, SOLO 18 SON REALES. SOBRAN 55, QUE ES EL 75,3 POR
CIENTO.** Y de los **34 actos que la 177 no miro, quedan 10 pares reales**, no 44.

#### 2.a. EL INSTRUMENTO VIEJO NO SE TOCA, Y ESO CONTESTA MI `P.2`

`scripts/loop/backlog_l03_vuelta14.py` **no se modifico en esta vuelta**, y esta
comprobado y no afirmado: `git diff --stat` sobre esa ruta sale **vacio**. Es el
instrumento que la nota de la ficha cita y el que sostiene la cifra ADJUDICADA EN
LA VUELTA 15. **Cambiarlo cambiaria esa cifra por la puerta de atras.**

#### 2.b. EL FILTRO VA DELANTE, EN FICHERO PROPIO Y DE NOMBRE ESTABLE

Nace `scripts/loop/backlog_l03_resuelto.py`, **sin numero de vuelta**, como sus
hermanos de nombre estable. Corre el instrumento viejo **como subproceso** y le
pone encima el resolutor de `P.1`, el `mapa_de_alias()` de
`scripts/loop/vuelta166_tarea2_correccion_op_l_01.py`. **PUBLICA LAS DOS COLUMNAS
AL LADO, NUNCA UNA SOLA**, que es la forma de la correccion declarada del banco
9.10 aplicada a un instrumento: la cifra vieja no se borra, se le pone la nueva al
lado con su procedencia.

#### 2.c. LO QUE PUBLICA, POR ACTO Y EN TOTAL

**Contado de `docs/loop/SALIDA_V178_T2_BACKLOG_RESUELTO.txt` y pegado de ahi.**

| cifra | valor |
|---|---|
| actos que el instrumento da | **40** |
| pares POSIBLES entre los miembros escritos | **202** |
| PARES QUE EL INSTRUMENTO DA (la cifra vieja, que NO se borra) | **73** |
| pares DISUELTOS (los dos extremos en el mismo nodo tras resolver) | **134** |
| pares que YA TIENEN VEREDICTO, buscados por el par RESUELTO | **47** |
| PARES REALES (la cifra nueva, al lado de la vieja) | **18** |
| actos SIN NINGUN PAR REAL | **29 de 40** |

**Los dos caminos van SIEMPRE los dos** (`EJECUTOR.md` 9): el resolutor de `P.1`
(761 alias sobre 3.853 ficheros de `dataset/nodos/`) y el campo `deprecado` del
grafo (3.853 nodos, 3.169 vivos). La tabla por acto trae las dos columnas para los
**40** actos, y esta entera en el fichero de salida.

**LOS SEIS ACTOS GRANDES, que son los que la 177 leyo:**

| acto | miembros | vivos por resolutor | vivos por grafo | calzan | pares del instrumento | pares reales | disueltos |
|---|---|---|---|---|---|---|---|
| `breakthrough_desempeno_actual` | 6 | 1 | 1 | SI | 8 | **0** | 15 |
| `cierre_segun_complejidad_venta` | 6 | 1 | 1 | SI | 6 | **0** | 15 |
| `cash_burn_calculation` | 5 | 5 | 5 | SI | 4 | 4 | 0 |
| `construccion_de_leverage` | 5 | 5 | 5 | SI | 3 | 3 | 0 |
| `encuadre_desafio_diseno` | 5 | 1 | 1 | SI | 6 | **0** | 10 |
| `estrategia_de_innovacion_arenas` | 5 | 4 | 4 | SI | 2 | **1** | 1 |

#### 2.d. EL ROJO DE LOS DOS CAMINOS, Y QUE DIO HOY

**CAE EN ROJO si los dos caminos no calzan en algun acto, nombrandolo.** Hoy:
**40 actos medidos, 40 calzan, 0 no calzan.** Y el rojo **no es decorativo**: su
arnes le da un grafo fabricado que MIENTE (un alias marcado como vivo) y la fila
sale **NO CALZAN**, o sea que la comprobacion muerde.

#### 2.e. EL CASO POSITIVO POR MUTACION, SOBRE UN MAPA FABRICADO

`scripts/loop/vuelta178_tarea2_mutacion_resolutor.py`,
`docs/loop/SALIDA_V178_T2_MUTACION.txt`. **12 casos, los 12 pasan y los 12 CAEN**
al mutarles el esperado. **Nada sale del repo**: ni `dataset/nodos/`, ni el grafo,
ni `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`. La mutacion que manda va en los dos
sentidos:

| el caso | pares reales |
|---|---|
| acto de 3 miembros CON el alias puesto (colapsan a uno) | **0**, y los 3 disueltos |
| el MISMO acto SIN el alias | **3**, y 0 disueltos |

**Si quitar el alias no cambiara la cifra, el resolutor no estaria puesto** y este
instrumento seria un `combinations()` con adornos.

**Y EL ARNES TUMBO UN DEFECTO REAL DEL INSTRUMENTO EN SU PRIMERA CORRIDA, que es
para lo que sirve.** El caso `C`, el del colapso parcial, salio **2 donde tenia que
salir 1**: el instrumento contaba los pares **ESCRITOS** y no los **RESUELTOS**, asi
que cuando `b` es alias de `a`, las parejas `(a, c)` y `(b, c)` se contaban DOS
VECES siendo la misma lectura. **Inflaba exactamente por el mecanismo que venia a
desinflar.** Se arreglo el instrumento, no el esperado del arnes.

**Y ESO MUEVE UNA CIFRA MIA DE LA 177, QUE DECLARO EN VEZ DE TAPAR** (`EJECUTOR.md`
2 y 8). La 177 publico **9 pares reales** en los seis actos; este instrumento, que
cuenta pares RESUELTOS distintos, dice **8**. **Las dos son verdaderas y miden
cosas distintas**: la 177 conto parejas escritas y leyo las nueve, y una de ellas,
en `estrategia_de_innovacion_arenas`, era **la misma pareja una vez resuelta**. La
cifra que vale para "cuantas lecturas quedan" es la de pares resueltos distintos.
El registro `docs/plan/OP_L_03_LECTURAS.jsonl` **no se retoca**: dice 2 en ese acto
y esa era su medicion, y una correccion que tapa lo que corrige no se puede
auditar.

#### 2.f. LA CIFRA QUE LA 177 NO PUDO PUBLICAR: CUANTO SOBRA EN LOS 34

**Los actos ya leidos NO se teclean: se cuentan del registro
`docs/plan/OP_L_03_LECTURAS.jsonl`**, que da 6, y los 6 siguen apareciendo en la
lista del instrumento.

| tramo | actos | pares del instrumento | pares reales | pares disueltos | sobran |
|---|---|---|---|---|---|
| YA LEIDOS (la 177) | **6** | **29** | **8** | **41** | **21** |
| SIN LEER | **34** | **44** | **10** | **93** | **34** |
| **todos** | **40** | **73** | **18** | **134** | **55** |

**LO QUE ESTO CAMBIA, DICHO CON SU NUMERO:** lo que queda de `OP-L-03` no son 44
pares en 34 actos, son **10 pares reales**, repartidos en los pocos actos que
todavia tienen mas de un nodo vivo. **De los 34 sin leer, 24 no tienen ningun par
real**: sus miembros ya colapsaron. La 177 hizo bien en no extrapolar la cifra; hoy
esta medida.

#### 2.g. EL ESTADO DE LA FICHA NO SE TOCA

`docs/plan/OPERACIONES.jsonl` **no se modifico**: `git diff --stat` sobre esa ruta
sale **vacio**. La vara sigue siendo `scripts/loop/vuelta150_3_relectura_expediente.py`
por decision del fundador del 4 sep 2026, y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
tampoco se toco: **cero veredictos movidos en esta tarea**.

<!-- FIN ANEXO DE TAREAS -->
