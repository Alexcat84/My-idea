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

**EL VEREDICTO DE UNA LINEA: LA VUELTA 178 ENTREGA SUS CINCO TAREAS ENTERAS, QUE ES EL TOPE QUE LA PROPIA 6.2 DEVOLVIO, Y CIERRA Y ARCHIVA SU REPORTE EN SU MISMA VUELTA POR TERCERA VEZ SEGUIDA. La vara del censo deja de vivir dentro de un signo de comparacion y destapa DOS arneses que la funcion vieja no podia ver jamas; el cuarto veredicto del cotejo de clones explica el 0 del auditor y el 1 del instrumento en el mismo sitio; el aislador gana su carril por lista de puestos y la muleta del auditor queda borrada; y las dos frases de higiene se vuelven guardas, una de las cuales CAZO A SU AUTOR DOS VECES, la segunda dentro del instrumento que la lleva. OP-L-03 se re-mide entero y lo que encuentra cambia su tamano: de 73 pares del instrumento solo 18 son reales, sobra el 75,3 por ciento, y en los 34 actos sin leer quedan DIEZ. Los triangulos se anotan con su regla y su prueba sin mover un solo veredicto, y son DIECISEIS y no cinco, siete de ellos en actos que nadie habia mirado. La vara del fundador gana una columna y ninguna ficha: seis en LISTA sin prueba, cuatro de trabajo real y dos consumidas por OP-U-01, cotejado linea a linea contra su version de git. CERO VEREDICTOS MOVIDOS y marcador intacto en 3.388 con 0 huecos; Gate 0 verde entero y en su orden en las dos puntas, y el desfase del calibrado medido POR FIN EN LA APERTURA. MIS CAIDAS PROPIAS SON CUATRO Y NINGUNA TAPADA, y tres de ellas las cazaron mis propios instrumentos en su primera corrida.**
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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 178`, y su salida
cruda vive en `docs/loop/SALIDA_V178_TALLADOR_CABECERA.txt` (2423 bytes en disco y 2403 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `77621a68` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 177: LAS DOS TAREAS ENTERAS Y TODO LO QUE PUBLICA REPRODUCE BAJO MI MANO SALVO UNA FRASE, Y EL TOPE VUELVE A CINCO PORQUE LA VUELTA LO DISPARO.'), HEAD real de apertura `77621a68` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `38143ebe` (leido de `SALIDA_V178_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LAS CORRECCIONES, Y ES BLOQUEANTE. Cinco letras: (a) LA RELECTURA AL DOBLE DEL TRAMO DE LA CAIDA de conteo del acta 177, la cuenta de la nomina y del censo, publicada ENTERA en tabla y con la resta comprobada, porque una cuenta que no cierra consigo misma se caza sola si alguien la escribe entera; (b) `arneses_que_faltan()` SE ARREGLA en la funcion y no en la llamada, con la vara del censo EXPLICITA y con su motivo, sin podar la nomina, y con el caso positivo por mutacion que hoy CAE con la funcion vieja: dos arneses de la MISMA vuelta que la ultima de la nomina, uno dentro y otro fuera, y la funcion tiene que VER al de fuera; (c) EL CUARTO VEREDICTO de `cotejar_clon_declarado.py`, EL ARBOL DE SINTAXIS, sin tocar la clasificacion vieja, en rojo si un fichero no parsea, y con el caso que lo decide todo: dos ficheros que solo difieren en una coma final dan maquina DIFIERE y AST IDENTICO; (d) EL `--puestos` Y EL `--excluir` DEL AISLADOR DE CIEGA, componibles con los selectores que ya tiene, en rojo si un puesto pedido no existe, con la guarda de fuga intacta, y borrando despues la muleta `_auditor_v178_ciega.py` por `P.16`; (e) LAS DOS DE HIGIENE: que `cerrar_reporte.py` CAIGA EN ROJO si el reporte publica una cifra de bytes o un sha sin su pareja, y LA GUARDA DEL SUJETO CONGELADO, que lleva desde la vuelta 145 siendo una frase y no un instrumento | **CERRADA. Las cinco letras entregadas, las cuatro que tocan codigo con arnes propio, y los cuatro arneses DENTRO de la nomina en su misma vuelta** | `SALIDA_V178_T1A_CUENTA.txt`, `_T1B_MUTACION.txt`, `_T1B_NOMINA.txt`, `_T1B_LOS_DOS_DESTAPADOS.txt`, `_T1C_MUTACION.txt`, `_T1C_ARNES_VIEJO.txt`, `_T1C_COTEJO_176.txt`, `_T1D_MUTACION.txt`, `_T1D_DEMO.txt`, `_T1D_ROJO_DEMO.txt`, `_T1E_MUTACION.txt`, `_T1E_CONGELADO.txt` |
| **TAREA 2** | `OP-L-03`: SE RE-MIDE EL BACKLOG ENTERO ANTES DE LEER UN ACTO MAS. No se toca `backlog_l03_vuelta14.py`, que sostiene una cifra adjudicada en la vuelta 15; se escribe el filtro DELANTE, en `scripts/loop/backlog_l03_resuelto.py`, de nombre estable y sin numero de vuelta, que corre el instrumento viejo y le pasa el resolutor de `P.1` por encima publicando LAS DOS COLUMNAS AL LADO. Por acto y en total: miembros escritos, vivos por el resolutor, vivos por el campo `deprecado` del grafo, SI LOS DOS CAMINOS CALZAN, pares que el instrumento da, pares reales y pares disueltos. CAE EN ROJO si los dos caminos no calzan en algun acto, nombrandolo. Con su caso positivo por mutacion sobre un mapa de alias FABRICADO. Y publica la cifra que la 177 no pudo publicar: cuanto sobra en los 34 actos que no miro. EL ESTADO DE LA FICHA NO SE TOCA | **CERRADA. El backlog re-medido entero: de 73 pares del instrumento quedan 18 reales, y en los 34 actos sin leer quedan 10** | `SALIDA_V178_T2_BACKLOG_RESUELTO.txt`, `SALIDA_V178_T2_MUTACION.txt` |
| **TAREA 3** | LOS CINCO TRIANGULOS `A` MAS `A` MAS `D`: SE ANOTAN CON SU REGLA, NO SE MUEVEN. La `P.3` de la 177 queda adjudicada como COSA JUZGADA en el acta 177 punto 7.9: las dos reglas que lo deciden ya estan escritas y RESULTAN COMPATIBLES. La `9.6.1` del banco dice que un nodo que es un paso de otro y NO TRAE PROCEDIMIENTO PROPIO, REPITE; la correccion declarada del 13 ago 2026 sobre los puestos 530 y 863 dice que la madre y su pieza de arenas se separan. La condicion que las concilia es la que la propia `9.6.1` escribe: SI LA PIEZA TRAE PROCEDIMIENTO PROPIO SE SEPARA, SI ES EL PASO DICHO OTRA VEZ, REPITE. Por cada uno de los cinco se anota EN EL JSONL cual de las dos reglas gobierna cada lado y CON QUE PRUEBA. CERO VEREDICTOS MOVIDOS | **CERRADA. Los triangulos anotados con su regla y su prueba en registro propio, CERO veredictos movidos comprobado por sha256** | `SALIDA_V178_T3_TRIANGULOS.txt`, `docs/plan/OP_L_03_TRIANGULOS.jsonl` |
| **TAREA 4** | LA CEGUERA DE LA VARA, QUE LLEVA DOS VUELTAS CONTADA. `vuelta150_3_relectura_expediente.py` imprime SEIS fichas en LISTA sin prueba y dos de las seis estan CONSUMIDAS por otras, asi que el trabajo real son CUATRO. La vara es del fundador y su veredicto NO SE TOCA: lo que se anade es una COLUMNA, no una exclusion. Que siga imprimiendo las seis y que diga de cada una si esta CONSUMIDA por otra ficha y por cual. La cuenta final publica LAS DOS, nunca solo el cuatro. Con su caso positivo por mutacion sobre un expediente fabricado | **CERRADA. La vara sigue imprimiendo las SEIS y publica las dos cifras: 4 de trabajo real y 2 consumidas por OP-U-01** | `SALIDA_V178_T4_VARA.txt`, `SALIDA_V178_T4_COTEJO_VARA.txt`, `SALIDA_V178_T4_MUTACION.txt` |
| **TAREA 5** | LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA COMO SIEMPRE: la segunda sede de la clausula 4.4 en `REPORTE_V172.md:535`; el docstring de `paso0_archivar_anterior.py`; la guarda que falta en la dependencia del `D.4` de la 174; y la medicion del grano del tope de 10 minutos, que se mide EN LA 181 con el reloj de esa corrida y no se re-elige a ojo antes. Ninguna de las cuatro se toca aqui, y las cuatro se nombran para que no se caigan | **CERRADA. Las cuatro nombradas y MEDIDAS (existen y ninguna mide cero bytes), mas dos nuevas que nacen en esta vuelta** | `SALIDA_V178_T5_NO_ENTRA.txt` |
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
(3.479 bytes en disco y 3.479 bytes en git, medidos en el bloque H.7) **ya
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
luego no lo hizo en dos celdas: un tallador publicado en 5.001 bytes cuando su medicion de disco decia 5.021 bytes,
y un sha `7d683eea4700f18b`, que es el normalizado a LF y no el de disco. **Las
dos cifras eran verdaderas y las dos hubo que ir a buscarlas.**

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

### TAREA 3. LOS TRIANGULOS SE ANOTAN CON SU REGLA, NO SE MUEVEN

**CERO VEREDICTOS MOVIDOS, Y ESTA COMPROBADO Y NO PROMETIDO.** El sha256 de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` normalizado a LF sale
`ea6e850d331d14f01db1186a54f4913fa72eb2560a354430c5e6d047ff0d02be` **antes y
despues** de esta tarea, y el instrumento **cae en rojo si difieren**. El unico
fichero que se escribe es un registro PROPIO,
`docs/plan/OP_L_03_TRIANGULOS.jsonl`.

#### 3.a. LAS DOS REGLAS SON COMPATIBLES, Y ESO ES COSA JUZGADA

La `P.3` del reporte 177 queda adjudicada en el acta 177 punto 7.9. No hace falta
regla nueva: **la `9.6.1` del banco** (un nodo que es un paso de otro y NO TRAE
PROCEDIMIENTO PROPIO, REPITE) y **la correccion declarada del 13 ago 2026** (la
madre y su pieza de arenas, y la vara las separa) **parecen contrarias y no lo
son**. La condicion que las concilia la escribe la propia `9.6.1`: **si la pieza
trae procedimiento propio SE SEPARA; si es el paso dicho otra vez, REPITE.**

**Y NO SE RESUELVE MOVIENDO VEREDICTOS.** Que `P.10` bloquee la fusion de esos
actos es **el resultado correcto, no el defecto**: un acto que contiene a la vez un
nodo entero y una pieza suya llamada `A` no debe fundirse a ciegas, y el triangulo
es el aviso.

#### 3.b. LA ANOTACION, EN EL JSONL Y CON SU PRUEBA

Instrumento: `scripts/loop/vuelta178_tarea3_anotar_triangulos.py`. Salida:
`docs/loop/SALIDA_V178_T3_TRIANGULOS.txt`. Registro:
`docs/plan/OP_L_03_TRIANGULOS.jsonl`, **16 filas, 45.168 bytes en disco y 45.168 bytes normalizados a LF**,
sha256 en disco y sha256 en LF los dos
`28d4dd9d709046675d1b404bdce4fdf62a2d98c9e38085e9604f2a8f1414aca9`.

**LOS TRIANGULOS NO SE TECLEAN: SE ENCUENTRAN.** El instrumento enumera las ternas
de nodos VIVOS de cada acto del backlog y se queda con las que tienen dos lados `A`
y uno `D`. **La clase de cada lado sale de una de dos fuentes declaradas**: el
archivo de veredictos indexado POR EL PAR RESUELTO (`P.1`), o el registro de
lecturas de la 177 para los lados que aquella leyo como LECTURA DIRIGIDA y que por
la clausula de `OP-L-03` no entran en la cola.

**QUE REGLA GOBIERNA CADA LADO SE LEE DE SU RAZON ESCRITA, y es mecanico:** se
buscan en la razon las marcas literales de cada regla (`no trae procedimiento
propio`, `contado como nodo`, `REPITE` para la `9.6.1`; `LA MADRE Y SU PIEZA`, `la
vara las separa`, `CORRECCION DECLARADA el 13 ago 2026` para la del 13 ago).
**Ninguna razon se interpreta a ojo:** si un lado no trae marcas de ninguna de las
dos, se anota **SIN MARCA** y se dice.

**Y LA PRUEBA VA AL LADO, MEDIDA DEL GRAFO Y NO DE LA RAZON:** los
`pasos_accionables` de cada extremo, contados. Es la corroboracion independiente
de "trae procedimiento propio", y **la unica cifra de esta tarea que no sale de un
texto**.

| regla que gobierna el lado | lados |
|---|---|
| `banco 9.6.1`, la pieza NO trae procedimiento propio: REPITE | **22** |
| correccion declarada del 13 ago 2026, la pieza TRAE procedimiento propio: SE SEPARA | **2** |
| SIN MARCA DE NINGUNA DE LAS DOS | **24** |
| **total de lados** | **48** |

**El caso ejemplar sigue siendo el puesto 878**, cuya razon dice literalmente *"El
paso cuatro contado como nodo, y no trae procedimiento propio"*, contra los
puestos 530 y 863, cuya razon dice *"LA MADRE Y SU PIEZA DE ARENAS, y la vara las
separa"*. **Las dos varas, la misma condicion, resultados distintos porque los
sujetos son distintos.**

#### 3.c. NINGUN VEREDICTO SE MOVIO, Y LA CIFRA DE TRIANGULOS NO CUADRA CON LA MIA

**DISCREPANCIA DECLARADA, Y NO LA RESUELVO COPIANDO** (`EJECUTOR.md` 2). La 177
publico **CINCO** triangulos; este instrumento, corrido hoy sobre los MISMOS TRES
ACTOS, encuentra **NUEVE**. **Los cinco que nombre estan entre los nueve**: los
tres de `construccion_de_leverage`, el de `cash_burn` con
`validacion_hipotesis_ingresos` y `verificar_modelo_ingresos`, y el de las arenas.
**Los cuatro de mas son reales y yo no los vi**: tres mas en
`cash_burn_calculation` (los que entran `validar_modelo_financiero` y
`metrics_that_matter_framework`) y uno mas en `estrategia_de_innovacion_arenas`
(el que entra `seleccion_arenas_estrategicas`). **La causa es de metodo:** yo mire
los triangulos que tocaban los pares que estaba leyendo, y el instrumento enumera
TODAS las ternas del acto. **La cifra que vale es la del instrumento corrido hoy.**

#### 3.d. Y EL PATRON APARECE EN LOS ACTOS QUE LA TAREA 2 RE-MIDE, DICHO EN VOZ ALTA

| tramo | actos con triangulo | triangulos |
|---|---|---|
| en los actos QUE LA 177 LEYO | **3** | **9** |
| en los actos QUE LA 177 NO MIRO | **5** | **7** |
| **todo el backlog** | **8** | **16** |

**NO ES UNA CASUALIDAD DE TRES ACTOS, Y AHORA ESTA MEDIDO Y NO OPINADO.** En los
actos que la 177 nunca miro hay **SIETE triangulos mas**, en **cinco actos
distintos**: `colaboracion_cadena_suministro`,
`compra_por_precio_mas_bajo_como_error`, `creacion_option_pool`,
`disenar_tests_pass_fail` y `fase_diseno_prototipado_modelos`. **Es el sitio exacto
donde la lectura de a pares y la lectura por acto TIENEN que dar distinto**, que es
la razon entera por la que `P.5` existe.

**NINGUNO SE TOCA AQUI.** No hay encargo para moverlos y esta tarea prohibe
expresamente mover veredictos. Quedan anotados, con su regla y su prueba, en el
registro propio.

### TAREA 4. LA CEGUERA DE LA VARA: SE ANADE UNA COLUMNA, NO UNA EXCLUSION

**LA VARA ES DEL FUNDADOR Y SU VEREDICTO NO SE TOCA.** Sigue imprimiendo **LAS
SEIS** fichas en LISTA sin prueba, y la cifra vieja sigue publicandose entera. Lo
que se anade es **una columna** y **una segunda cifra al lado de la primera**.

#### 4.a. LA COLUMNA, Y COMO SE MIDE CADA MITAD

Instrumento: `scripts/loop/vuelta150_3_relectura_expediente.py`, corrido con
`--corte HEAD` en esta vuelta. Salida: `docs/loop/SALIDA_V178_T4_VARA.txt`.

| id_op | fase | tipo | depende_de medido | consumida por |
|---|---|---|---|---|
| `OP-L-01` | 09_LECTURAS_DIRIGIDAS | MESA | (vacio) | no |
| `OP-L-02` | 09_LECTURAS_DIRIGIDAS | MESA | OP-D-01=LISTA, OP-D-02=LISTA, OP-D-03=LISTA | no |
| `OP-L-03` | 09_LECTURAS_DIRIGIDAS | MESA | OP-D-01=LISTA a OP-D-06=LISTA | no |
| `OP-I-01` | 10_INVENTARIO | MESA | (vacio) | no |
| `OP-M-02-MEDIOS` | 03_FUSIONES | FUSION DE MESA | OP-M-02=HECHA | **SI, por `OP-U-01`** |
| `OP-M-02-ADMIT` | 03_FUSIONES | FUSION DE MESA | OP-M-02=HECHA, OP-M-02-MEDIOS=LISTA | **SI, por `OP-U-01`** |

**LAS DOS MITADES DE LA COLUMNA SE MIDEN DE SITIOS DISTINTOS, y eso se dice en la
propia salida:**

- **SI ESTA CONSUMIDA sale del GRAFO**, por el resolutor de `P.1` y no leyendo un
  acta: una ficha esta consumida cuando tiene **dos o mas nodos** y **todos
  resuelven a UN SOLO NODO VIVO**, o sea que la fusion que la ficha describe **ya
  ocurrio**. `OP-M-02-MEDIOS` resuelve a `estrategia_multicanal_bienvenida` y
  `OP-M-02-ADMIT` a `fase_admit_celebracion`, y los dos destinos viven.
- **POR CUAL se lee de la propia ficha**, y **se declara que viene de ahi**,
  porque **el grafo guarda el resultado y no quien lo hizo**. Si la ficha no
  nombra a nadie, la columna dice **CONSUMIDA SIN DECIR POR QUIEN** en vez de
  inventar un culpable.

#### 4.b. LA CUENTA PUBLICA LAS DOS, NUNCA SOLO EL CUATRO

La vara imprime ahora, con estas palabras: **"6 en LISTA sin prueba, de las cuales
4 son TRABAJO REAL y 2 estan CONSUMIDAS por otras fichas"**, con las dos nombradas
y con su destino vivo al lado. Y en el bloque de cifras finales:

| cifra | valor |
|---|---|
| fichas en LISTA sin ninguna prueba (la de siempre, **intacta**) | **6** |
| de esas, CONSUMIDAS por otra ficha (nueva) | **2** |
| de esas, TRABAJO REAL (nueva) | **4** |

**PODAR LA CIFRA DE LA VARA SIN EL FUNDADOR ES LO QUE LA CASA RESERVA**, y por eso
el **6** sigue ahi y las seis filas se siguen imprimiendo enteras.

#### 4.c. EL COTEJO DE ANTES Y DESPUES, PARA QUE NADIE TENGA QUE CREERME

`docs/loop/SALIDA_V178_T4_COTEJO_VARA.txt`. **La version vieja se saca de git**
(`git show 77621a68:scripts/loop/vuelta150_3_relectura_expediente.py` a
`scripts/loop/_v178_vara_vieja_copia.py`), **no de una copia a mano**, y las dos se
corren con `--corte HEAD` en esta misma vuelta.

| medicion | valor |
|---|---|
| lineas de la salida VIEJA | **234** |
| lineas de la salida NUEVA | **248** |
| lineas que la vieja tiene y la nueva NO | **8** |
| lineas que la nueva anade | **22** |

**Y LAS OCHO QUE "SE PIERDEN" SON LAS MISMAS OCHO QUE VUELVEN CON LA COLUMNA
PUESTA**: la cabecera de la tabla, su separador y las seis filas. **NI UN
VEREDICTO, NI UNA CLASIFICACION Y NI UNA CIFRA VIEJA CAMBIAN.** Las 37 filas de
"las que no calzan", las 24 congeladas declaradas, las 12 en silencio, la 1 HECHA
sin prueba y el 6 de LISTA sin prueba salen **identicas**.

**Y UN CAMBIO ADITIVO QUE DECLARO EN VOZ ALTA:** la vara llamaba a `main()` a
nivel de modulo, asi que **importarla la corria**, y su caso positivo por mutacion
no podia llamar a sus funciones puras sin arrastrar la vara entera detras. Se le
puso la guarda `if __name__ == "__main__"`. **Corrida como programa hace
exactamente lo mismo que antes**, y el cotejo de arriba lo demuestra.

#### 4.d. EL CASO POSITIVO POR MUTACION, SOBRE UN EXPEDIENTE FABRICADO

`scripts/loop/vuelta178_tarea4_mutacion_consumidas.py`,
`docs/loop/SALIDA_V178_T4_MUTACION.txt`. **11 casos, los 11 pasan y los 11 CAEN**
al mutarles el esperado. **Nada sale del repo**: ni `docs/plan/OPERACIONES.jsonl`,
ni `dataset/nodos/`, ni el grafo.

| el caso | resultado |
|---|---|
| dos nodos que resuelven a un solo VIVO, con su atribucion escrita | CONSUMIDA, y nombra `OP-Z-99` |
| **la misma ficha SIN el alias** | **NO consumida** |
| una ficha de un solo nodo, aunque su nota lo afirme | no consumida |
| consumida pero sin nombrar a nadie | consumida, y lo declara sin inventar culpable |
| dos nodos que colapsan a un destino DEPRECADO | no consumida |

**LA MUTACION QUE MANDA ES LA DEL ALIAS**: si quitarlo no cambiara la respuesta,
la columna no estaria midiendo contra el grafo, estaria leyendo un acta.

**Y ESTE ARNES TAMBIEN TUMBO UN DEFECTO REAL EN SU PRIMERA CORRIDA**, igual que el
de la TAREA 2: la atribucion se buscaba en **la primera ventana** de la nota y
devolvia lista vacia **teniendo la respuesta escrita unos cientos de caracteres
mas abajo**, en la misma nota. La primera corrida de la columna sobre el
expediente real decia *"SI, PERO LA FICHA NO DICE POR QUIEN"* en las dos, y la
ficha si lo decia: `OP-U-01`. Se arreglo la funcion, y el caso del arnes pone la
atribucion **a 400 caracteres de la marca a proposito** para que no pueda volver a
pasar.

### TAREA 5. LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA

**LAS CUATRO EXISTEN, NINGUNA MIDE CERO BYTES Y NINGUNA SE TOCA AQUI.** Se
comprueban ANTES de escribirlas, porque `EJECUTOR.md` 1 dice que **una ruta
publicada como evidencia CUENTA COMO CIFRA**, y una ruta a un fichero inexistente
o vacio es CAIDA DE CIFRA. Salida:
`docs/loop/SALIDA_V178_T5_NO_ENTRA.txt`.

| que queda pendiente | sede | disco | LF | git | por que no entra aqui |
|---|---|---|---|---|---|
| la segunda sede de la clausula `4.4` | `docs/loop/reportes/REPORTE_V172.md`, lineas 20 y 80 | 48.851 | 48.851 | 48.851 | es un reporte ARCHIVADO Y COMMITEADO, o sea un sujeto congelado |
| el docstring de `paso0_archivar_anterior.py` | `scripts/loop/paso0_archivar_anterior.py`, 162 lineas | 7.112 | 7.112 | 7.112 | divergencia de TEXTO y no de maquina, y el encargo no la manda |
| la guarda que falta en la dependencia del `D.4` de la 174 | `docs/loop/reportes/REPORTE_V174.md`, linea 366 | 32.568 | 32.568 | 32.568 | pide instrumento nuevo y el encargo no lo pide |
| el grano del tope de 10 minutos (mi `D.2`) | `scripts/loop/verificar_mutaciones_viejas.py`, `reparto_en_tramos()` | 108.097 | 108.097 | 108.097 | **se mide EN LA 181 con el reloj de esa corrida**, no antes |

**Y CADA UNA CON LO QUE HOY SE PUEDE MEDIR DE ELLA, que es lo que impide que se
caiga por olvido:**

1. **LA CLAUSULA `4.4`.** El fichero la nombra en **2 lineas**, la 20 y la 80. **No
   se retoca**: un reporte archivado es un sujeto congelado, y retocarlo es peor
   que el defecto.
2. **EL DOCSTRING DE `paso0_archivar_anterior.py`.** Dice **1 vez** "vuelta
   anterior" y **0 veces** "VUELTA menos 1". Lo pendiente es que sigue hablando de
   LA VUELTA ANTERIOR cuando la maquina, desde la 174, pregunta por **el reporte
   que va a pisar**.
3. **LA GUARDA DEL `D.4`, Y LA DEPENDENCIA SIGUE VIVA HOY, MEDIDA Y NO
   RECORDADA:** el esqueleto de ESTA vuelta clona
   `vuelta_del_reporte_del_arbol()` de `vuelta174_esqueleto_reporte.py` en vez de
   importarla, **y lo declara** (comprobado en el fichero, sale SI). **Nada avisa
   si el fichero del que se clono desaparece.**
4. **EL GRANO DEL TOPE.** `TOPE_DE_MINUTOS_POR_TRAMO` vale **10.0**, la nomina de
   hoy tiene **98 entradas** y el reparto con tamano 10 da **10 tramos**. **La
   medicion de si eso es demasiado grano necesita EL RELOJ DE LA CORRIDA DE LA
   181**, que es lo unico que dice cuanto cuesta de verdad cada tramo. **Elegir el
   numero antes seria justo lo que el `D.3` de la 176 levanto contra el tamano
   elegido a ojo.**

**Y SE ANADEN DOS QUE NACEN EN ESTA VUELTA Y TAMPOCO ENTRAN**, para que no se
caigan tampoco: **los DOS arneses que la vara del censo destapa** y que decidiran
si la bateria de la 181 sale en rojo (`P.1` de la seccion de preguntas), y **el
cableado de la guarda del sujeto congelado al rojo global de la bateria** (`P.2`).
Las dos van con su cifra medida en la TAREA 1 y ninguna se decide aqui.

<!-- FIN ANEXO DE TAREAS -->

## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**Todo hash de esta seccion sale de `git log` o `git rev-parse` corrido en esta
vuelta** (`EJECUTOR.md` 1, LA IDENTIDAD SE LEE DE GIT).

| | |
|---|---|
| rama | `pasada-unica` |
| sello de apertura, escrito ANTES de la 1.a operacion | `77621a68` (`SALIDA_V178_HEAD_APERTURA.txt`) |
| sello de cierre, escrito TRAS la ultima operacion | `38143ebe` (`SALIDA_V178_HEAD_CIERRE.txt`) |
| commits entre los dos sellos | **7** |
| rutas tocadas | **65** (`docs/loop/` 35, `scripts/loop/` 29, `docs/plan/` 1) |
| **el grafo entre los dos sellos** | **`git diff --numstat` sobre `dataset/`, `web/` y `engine/`: 0 filas** |

**LOS SIETE COMMITS, EN SU ORDEN:**

| hash | que cierra |
|---|---|
| `531efee1` | el bloque de apertura, corrido antes de la primera operacion, y el desfase del calibrado DENTRO de el |
| `72126b30` | el esqueleto del reporte, abierto al empezar con sus CINCO filas vacias |
| `09e5c4b4` | TAREA 1, los registros y las correcciones (bloqueante) |
| `3c22f94a` | TAREA 2, `OP-L-03` re-medido entero |
| `9c690d2d` | TAREA 3, los triangulos anotados con su regla |
| `e56a1dff` | TAREA 4, la columna `CONSUMIDA` de la vara |
| `38143ebe` | TAREA 5, lo que no entra y no se pierde |

Los commits posteriores a `38143ebe` son **el cierre de este reporte y su
archivado**, y por eso no estan en la cuenta de arriba: el sello de cierre se
escribe antes que ellos y no puede nombrarlos.

**EL MARCADOR, RECOMPUTADO AL CIERRE Y NO HEREDADO DE LA APERTURA**
(`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE):

| | total | A | B | C | D |
|---|---:|---:|---:|---:|---:|
| **marcador al cierre** | **3.388** | **551** | **72** | **5** | **2.760** |

Puestos de **1 a 3.388**, **0 huecos** y **0 duplicados**. **Identico al de la
177**, y esa es la cifra que las TAREAS 2 y 3 prometian no mover.

**GATE 0, EL CICLO ENTERO Y EN SU ORDEN, EN LAS DOS PUNTAS**, nunca `run_phase1`
suelto:

| paso | apertura | cierre |
|---|---|---|
| `run_phase1.py --reaplico-curaduria` | **GATE 0: OK**, exit 0 | **GATE 0: OK**, exit 0 |
| `etiquetas_de_cara.py --aplicar` | corrido, exit 0 | corrido, exit 0 |
| `sync_assets_web.py` | corrido, exit 0 | corrido, exit 0 |
| `git diff HEAD --numstat -- dataset/ web/ engine/` | **0 filas** | **0 filas** |
| `engine/run_all_tests.py` | **25/25** | **25/25** |
| `npx tsc --noEmit` | **exit 0, cero lineas** | **exit 0, cero lineas** |
| `pnpm test` | **82 (82) / 1.040 (1.040)** | **82 (82) / 1.040 (1.040)** |

**Y EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA, QUE ES LA CAIDA PROPIA QUE
LA 177 SE ANOTO Y QUE DESDE ESTA VUELTA ACUMULA.** El medidor corre DENTRO de
`scripts/loop/vuelta178_apertura.py`, antes de la primera operacion. Las dos
salidas, la de apertura y la de cierre, son **identicas byte a byte**: **505
bytes en disco y 498 bytes normalizados a LF** cada una, sha256 en disco
`9c1a246654108251` y sha256 normalizado a LF `7d683eea4700f18b` **las dos**. La
salida del conteo de aristas tambien sale identica en las dos puntas.

## 4. LA GUARDA DEL COMMIT, CORRIDA EN CADA COMMIT DE ESTA VUELTA

`scripts/loop/guarda_commit_dataset.py` salio **VERDE antes de cada uno de los
siete commits**, con **0 filas de `git diff --numstat -- dataset/`**, **0 ficheros
nombrados por `git status --porcelain -- dataset/`** y **0 blobs de arbol
divergentes de HEAD**. **`dataset/` no se toco en ninguna de las cinco tareas**, y
eso no es una promesa: es la cifra que la guarda imprime.

**Y NINGUNA TAREA ESCRIBIO EN LOS TRES FICHEROS QUE LA CAMPANA RESERVA.**
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` sale con el mismo sha256 normalizado a LF
antes y despues de la TAREA 3, comprobado por el propio instrumento;
`docs/plan/OPERACIONES.jsonl` y `scripts/loop/backlog_l03_vuelta14.py` salen con
`git diff --stat` **vacio**.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` LA VARA DEL CENSO EN 148 ES UNA ELECCION, Y LA MARCO.** El encargo dice
"menos los anteriores a la vara del censo" y no dice cual es la vara. Elegi **148**
porque es el unico numero con motivo escrito y citable: la letra de entrada en la
nomina es "desde la vuelta 148" y `vuelta164_tarea5_medir_pre148.py` midio lo
anterior con `CORTE = 148` y lo adjudico fuera. **Lo discutible es que con la vara
en 177 (o sea "la ultima de la nomina", con `>=` en vez de `>`) el resultado de
hoy seria CERO y no habria destapado nada**, y eso tambien encajaria con la frase
"es exactamente lo que tu hiciste a mano". **Elegi la lectura que destapa, no la
que calla**, y puede que el auditor prefiera la otra.

**`D.2` NO CABLEE LA GUARDA DEL SUJETO CONGELADO AL ROJO GLOBAL DE LA BATERIA.**
La guarda existe, corre sola y cae en rojo en su propio carril con **15 de 92**.
Cablearla pondria la bateria de la 181 en rojo por quince entradas cuyo estado
real hay que juzgar una a una. **Lo discutible es si "entra aqui y no se aplaza
otra vez" exigia el cableado y no solo el instrumento.**

**`D.3` LAS HUELLAS DE LA GUARDA DEL SUJETO CONGELADO SON MIAS Y NO SALEN DE
NINGUNA REGLA ESCRITA.** `SUJETO_FIJO`, `tempfile`, `mkdtemp`, `deepcopy`, `git
show`, `cat-file`, `sha256` y el literal `SUJETO CONGELADO` para el lado
congelado; los cinco ficheros vivos de la campana para el otro. **Son una lista
que yo compuse mirando lo que la nomina ya hace**, no una vara adjudicada, y por
eso los 8 `NO DECIDIBLE` pueden ser mas o menos con otra lista.

**`D.4` EL ROJO POR `--excluir` DE UN PUESTO INEXISTENTE LO ESTIRE YO.** El
encargo dice "CAE EN ROJO si un puesto PEDIDO no existe". Lo aplique tambien a
`--excluir`, con su motivo escrito en el fichero (el universo de los dos es el
mismo archivo). **Es una lectura ancha y la marco.**

**`D.5` EL AST DEL PAR DEL ACTA 176 SALE DIFIERE, ASI QUE EL CUARTO VEREDICTO NO
EXONERA SOLO EN ESE PAR.** Lo que exonera es la fila de los tipos de nodo, que
empatan exactamente (1.368 contra 1.368, 0 tipos distintos). **Lo traigo tal cual
en vez de redondearlo a "AST identico".**

**`D.6` LOS 24 LADOS `SIN MARCA DE NINGUNA DE LAS DOS` DE LA TAREA 3.** La mitad
de los lados de los triangulos no trae en su razon ninguna marca literal de
ninguna de las dos reglas. **Los declaro asi en vez de asignarles una a ojo**,
pero puede que el auditor considere que la anotacion queda a medias sin ellos.

## 6. LAS PREGUNTAS

**`P.1` LOS DOS ARNESES QUE LA VARA DEL CENSO DESTAPA: ¿ENTRAN EN LA NOMINA?**
`vuelta150_2d_simular_op_c_05.py` y `vuelta160_tarea3b_caso_positivo.py` estan en
el censo, no estan en la nomina y no son anteriores a la vara. Corridos hoy: **exit
0 los dos, 0 filas de numstat sobre `dataset/`**. La regla escrita desde la 148
dice que un arnes entra en la nomina. **No los meti porque eso decide lo que la
181 corre.** Mientras no entren, **la bateria de la 181 dara ROJO por esta cuenta,
y ese rojo sera correcto.**

**`P.2` ¿SE CABLEA LA GUARDA DEL SUJETO CONGELADO AL ROJO DE LA BATERIA, Y CUANDO?**
Con las cifras de hoy (75 congeladas, 2 casos declarados, 7 sujeto vivo, 8 no
decidibles) cablearla es un rojo de 15 entradas de golpe.

**`P.3` ¿LA CIFRA DE TRIANGULOS QUE VALE ES NUEVE O CINCO?** Sobre los mismos tres
actos, la 177 conto cinco y el instrumento cuenta nueve. **Publico las dos y no
resuelvo copiando.**

**`P.4` ¿QUE SE HACE CON LOS SIETE TRIANGULOS DE LOS ACTOS SIN LEER?** Estan
anotados con su regla y ninguno se toca. **Bloquean la fusion de cinco actos mas
por `P.10`**, y eso cambia lo que queda de `OP-L-03` mas todavia que la cifra de
pares.

## 7. PENDIENTES DE DOCTRINA

**`PD.1` LA CONVENCION DE BYTES, POR QUINTA ACTA.** Sigue sin fijar y es del
fundador. Lo que si esta adjudicado (acta 177, 7.11) ya es instrumento desde esta
vuelta: `cerrar_reporte.py` cae en rojo si el reporte publica una cifra de bytes o
un sha sin su pareja. **Y la guarda cazo a su autor en su primera corrida:
encontro CUATRO cifras sin pareja en este mismo reporte, las cuatro mias**, y
estan corregidas en `scripts/loop/_v178_arreglo_parejas.py`, que arregla el
borrador y el reporte a la vez para que no diverjan.

**`PD.2` LA REGLA DEL SUJETO CONGELADO YA TIENE INSTRUMENTO, PERO NO TIENE VARA
ADJUDICADA.** Las huellas con las que clasifica son mias (ver `D.3`). **Lo que
falta ya no es el instrumento, es la lista.**

**`PD.3` QUE CUENTA COMO "PAR" EN `OP-L-03`: EL ESCRITO O EL RESUELTO.** Esta
vuelta cambio la cuenta a **pares RESUELTOS distintos**, y eso mueve la cifra de la
177 de 9 a 8. **La regla no esta escrita en ningun sitio**: la deduje de que la
pregunta es "cuantas lecturas quedan".

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**`C.1` LA CIFRA DE TRIANGULOS DE LA 177 SE QUEDO CORTA, Y ES DE METODO.** Publique
CINCO y sobre los mismos tres actos hay NUEVE. **Mire los triangulos que tocaban
los pares que estaba leyendo en vez de enumerar todas las ternas del acto.** Los
cinco que nombre son correctos; los cuatro que faltan son reales.

**`C.2` LA CUENTA DE PARES REALES DE LA 177 CONTABA PARES ESCRITOS.** Publique 9 y
hoy salen 8, porque una pareja de `estrategia_de_innovacion_arenas` era la misma
una vez resuelta. **El registro de la 177 no se retoca**: dice lo que midio.

**`C.3` MIS DOS INSTRUMENTOS NUEVOS SALIERON CON UN DEFECTO CADA UNO, Y LOS CAZARON
SUS PROPIOS ARNESES EN LA PRIMERA CORRIDA.** `backlog_l03_resuelto.py` contaba
pares escritos y no resueltos, o sea inflaba por el mismo mecanismo que venia a
desinflar; y la columna `CONSUMIDA` buscaba la atribucion en la PRIMERA ventana de
la nota y devolvia vacio teniendo `OP-U-01` escrito unos cientos de caracteres mas
abajo. **En los dos se arreglo el instrumento y no el esperado del arnes.** Lo
cuento como caida mia porque los dos defectos salieron de mi mano, y lo cuento con
alegria porque los dos casos rojos funcionaron.

**`C.4` CINCO CIFRAS SIN PAREJA EN ESTE MISMO REPORTE, Y LA QUINTA LA ESCRIBIA LA
PROPIA GUARDA.** La guarda de la TAREA 1.e encontro CUATRO en el cuerpo, todas
mias, antes del cierre; estan corregidas en
`scripts/loop/_v178_arreglo_parejas.py`, que arregla el borrador y el reporte a la
vez para que no diverjan. **Y en la primera corrida de `cerrar_reporte.py` la
guarda cazo una QUINTA que no era del cuerpo: la escribia el generador de la
seccion 9 de ese mismo fichero**, que partia "N bytes en disco" y "N bytes
normalizados a LF" en dos lineas. **Una guarda que se estrena cazando a su autor
DOS VECES, la segunda dentro del instrumento que la lleva**, y por eso el cierre
de esta vuelta salio ROJO la primera vez y hubo que arreglar el generador antes de
volver a correrlo. Se arreglo el generador, no la guarda.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 178 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V178_BATERIA.txt`.
**SUS BYTES, MEDIDOS EN ESTA CORRIDA** con `os.path.getsize` por
`scripts/loop/cerrar_reporte.py`, no tecleados, y POR LAS DOS
CONVENCIONES mientras la del fundador no este fijada:
**0 bytes en disco y 0 bytes normalizados a LF**.

ATRIBUCION: NADIE la corrio, y no es un olvido: esta vuelta NO ES DE BATERIA. La cadencia esta adjudicada en el acta 176 punto 7.8 y reconfirmada por el encargo de esta vuelta, LA PROXIMA VUELTA DE BATERIA ES LA 181, y la 178, la 179 y la 180 cierran su seccion 9 con el hueco declarado y medido. Lo que SI corrio esta vuelta de la propia bateria son sus DOS guardas que no corren arneses: la prueba de la nomina sobre si misma (8 casos, los 8 pasan y los 8 caen, docs/loop/SALIDA_V178_T1B_NOMINA.txt) y la guarda del sujeto congelado, que nace aqui y sale en ROJO con 15 de 92 (docs/loop/SALIDA_V178_T1E_CONGELADO.txt).

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
