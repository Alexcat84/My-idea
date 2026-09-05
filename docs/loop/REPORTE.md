# REPORTE DE LA VUELTA 180 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta180_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA Y LA SIGUIENTE SI, Y LA CADENCIA NO SE ELIGE
> AQUI: ESTA ADJUDICADA Y RECONFIRMADA TRES VECES.** El acta 176, punto 7.8,
> reanclo el contador a la vuelta que de verdad corrio la bateria y no a la que la
> tenia encargada; **el acta 178, punto 11, y el acta 179, punto 11, lo
> reconfirmaron**; y el encargo de esta vuelta lo repite con todas las letras:
> **la proxima vuelta de bateria es la 181**. Esta es **LA ULTIMA VUELTA QUE
> DECLARA EL HUECO**: la seccion 9 cierra con el **HUECO DECLARADO Y MEDIDO** y
> sus TRES piezas juntas, el nombre del fichero, sus bytes por las dos
> convenciones y la atribucion. Un hueco declarado no es un hueco escondido, y
> **la 181 lo corre**.
>
> **EL TOPE SIGUE EN CINCO, Y NO LO DECIDE NADIE: LO DISPARO LA 177 Y LA 178 Y LA
> 179 LO CONFIRMARON ENTREGANDO CINCO.** `AUDITOR.md` 6.2 dice que el regimen
> temporal de dos sub-tareas dura **hasta que DOS vueltas seguidas cierren su
> propio reporte** con `cerrar_reporte.py`, y eso se cumplio. **El regimen
> temporal queda CUMPLIDO Y CITABLE, no borrado**, y los cuatro commits que lo
> sostienen se localizan EN GIT en el bloque B.1 de
> `scripts/loop/vuelta180_apertura.py`, no se teclean.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno, la 179 lo repitio y aqui vuelve a
> correr en su sitio. **Desde la 178, una columna de apertura medida al cierre es
> caida que ACUMULA**, y eso lo dice el encargo, no este reporte.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> 179 escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el
> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una
> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.
> **Y LA TAREA 4.a DE ESTA VUELTA FABRICA EL DIA EN QUE DIFIEREN**, que es lo que
> a esta guarda le faltaba desde la 174: hasta hoy nadie la habia visto responder
> a la pregunta buena cuando las dos preguntas dan cosas distintas.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta180_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 179: `d3240915`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 179: NI UNA CAIDA CONTRA EL EJECUTOR, LA ESCALADA QUE ENCARGUE CAZA LA CAIDA DE LA 178 BAJO MI MANO, Y LA RACHA DE REPORTE VUELVE A CERO.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V180_HEAD_APERTURA.txt`: `d3240915`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `122ca81f`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **179**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 180`. **Esta
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
| **TAREA 1** | LOS REGISTROS Y LA ETIQUETA DE FUENTE, Y ES BLOQUEANTE. (a) El acta del auditor de la vuelta 179 vive en `docs/loop/ACTA_AUDITOR.md` y NO levanta ninguna caida contra la 179: la racha de reporte vuelve a CERO, la de cifra publicada sigue en CERO y no hay correccion declarada que arrastrar. (b) LA ETIQUETA DE FUENTE, ARREGLADA, y eso LEVANTA LA PARADA DE LA 3.f DE LA 179: `clases_por_par()` LEE LA VUELTA DE LA FILA DEL REGISTRO en vez del literal `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)` clavado, con `sha256` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y de `docs/plan/OP_L_03_LECTURAS.jsonl` ANTES y DESPUES dentro del propio instrumento y los CUATRO publicados, con `vuelta179_tarea3_etiqueta_de_fuente.py` re-corrido y las DOS mediciones al lado (la de antes y la de despues, y la de despues en CERO falsos o se para), con `vuelta178_tarea3_anotar_triangulos.py` re-corrido y el total de triangulos y de lados sin moverse, y con su caso positivo por mutacion sobre un registro fabricado de dos vueltas distintas | **CERRADA** | `SALIDA_V180_T1B_TRIANGULOS.txt`, `SALIDA_V180_T1B_ETIQUETA_DESPUES.txt`, `SALIDA_V180_T1B_MUTACION_ETIQUETA.txt`, `SALIDA_V180_APERTURA.txt` H.6 |
| **TAREA 2** | EL SUJETO CONGELADO, RESUELTO Y CABLEADO, Y ES LA QUE LIMPIA LA PISTA DE LA 181. El orden es: los trece declaran, los cuatro congelan, y SOLO ENTONCES se cablea. (a) LOS TRECE QUE NO ABREN NADA VIVO DECLARAN SU SUJETO, once `LO NOMBRA SIN ABRIRLO` y dos `ABRE UN SUJETO YA CLAVADO`, una linea por arnes con el literal que la guarda busca y NINGUNA otra linea tocada, comprobado con `git diff --numstat` sobre `scripts/loop/` publicando las lineas anadidas por fichero. (b) LOS CUATRO QUE SI ABREN, CONGELADOS DE VERDAD, cada uno con que abria, que abre ahora y la prueba de que su resultado ya no se mueve. (c) Y SOLO ENTONCES EL CABLEADO al rojo global de la bateria, con la cifra de antes y su corte pegado y la de despues, que TIENE QUE DAR 0 o no se cablea. (d) NADA SE PODA DE LA NOMINA: todo arnes que esta vuelta escriba entra en `verificar_mutaciones_viejas.py` con la cuenta entera y la resta comprobada, antes de la 181 | **CERRADA** | `SALIDA_V180_T2A_DECLARAR.txt`, `SALIDA_V180_T2A_GUARDA_TRAS_DECLARAR.txt`, `SALIDA_V180_T2B_CONGELACION.txt`, `SALIDA_V180_T2B_RELECTURA.txt`, `SALIDA_V180_T2C_GUARDA_DESPUES.txt`, `SALIDA_V180_T2C_TRAMO_CABLEADO.txt`, `SALIDA_V180_T2C_MUTACION_CABLEADO.txt`, `SALIDA_V180_T2_NUMSTAT.txt` |
| **TAREA 3** | EL CORTE, CABLEADO DONDE TODAVIA FALTA. El hallazgo es del fundador y esta medido en la seccion 6 del acta 179: la tabla de tramos de la 2.a de la 179 esta contada de su fichero y sus cifras eran verdad, pero LE FALTA EL CORTE, y sin corte no hay manera de saber cual mira que. Se cablea el sello de `sello_de_corte()` DONDE SE GENERA LA TABLA DE TRAMOS de `backlog_l03_resuelto.py`, no en una frase del reporte, por `banco 9.21` y el punto 7.2 del acta 178. Y SE BARRE EL RESTO: la lista de toda cifra de ese instrumento y de `vuelta179_tarea2_cobertura_final.py` que pueda moverse dentro de una vuelta, diciendo cuales llevan corte y cuales no, y las que no lo lleven lo llevan al terminar. Con su caso positivo por mutacion: dos cortes distintos con la misma cifra no se confunden, y la misma cifra con dos cortes distintos tampoco | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LAS DOS PENDIENTES BARATAS QUE YA LLEVAN VUELTAS SUBIENDO, LAS DOS TEXTO QUE MIENTE SOBRE SU PROPIA MAQUINA. (a) EL DOCSTRING DE `scripts/loop/paso0_archivar_anterior.py`, que sigue hablando de LA VUELTA ANTERIOR cuando la maquina ya pregunta por EL REPORTE QUE VA A PISAR: se arregla, se publican la linea vieja y la nueva sin borrar la vieja del reporte, y SE ESCRIBE LA GUARDA QUE HACE VISIBLE LA DIFERENCIA, un caso fabricado donde las dos preguntas NO coinciden y que demuestra que la maquina responde a la buena. (b) LA GUARDA QUE FALTA EN LA DEPENDENCIA DEL `D.4` DE LA 174: el esqueleto CLONA `vuelta_del_reporte_del_arbol()` en vez de importarla y nada avisa si el fichero del que se clono desaparece; la guarda CAE EN ROJO nombrandolo, con su caso positivo por mutacion sobre una ruta fabricada que no existe | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | EL BACKLOG DE `OP-L-02`, MEDIDO Y NO LEIDO, CON LA MISMA VARA RESUELTA QUE CERRO `OP-L-03`. Se corre el instrumento viejo de `OP-L-02` por dentro y sin citarlo de memoria y se publican LOS PARES QUE DA; se le pone encima el resolutor de `P.1` y se publican LOS PARES REALES, o sea los que no estan ya en el archivo tras resolver a nodo vivo; LAS DOS COLUMNAS VAN LAS DOS Y LA VIEJA NO SE BORRA (`banco 9.10`); el reparto por tramo va CON SU CORTE PEGADO por la TAREA 3 de este mismo encargo; y LOS DOS CAMINOS TIENEN QUE CALZAR en todos los actos medidos o se publica donde y se para. LO QUE NO SE HACE: no se lee ningun par, no se escribe ningun veredicto, no se toca el marcador, no se toca el estado de ninguna ficha (`EJECUTOR.md` 4, modo de cierre) y NO SE TOCAN LOS CINCO PARES DE SALES ROADMAP, que `docs/plan/LECTURAS_DIRIGIDAS.md` deja como decision revocable del fundador: se nombran y se dejan | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1 (BLOQUEANTE). LOS REGISTROS Y LA ETIQUETA DE FUENTE, ARREGLADA

**1.a. LOS REGISTROS, LEIDOS HOY Y CITADOS CON SU LINEA.** El acta del auditor de
la vuelta 179 esta escrita en `docs/loop/ACTA_AUDITOR.md`, cabecera en la
**linea 62019**, y **no levanta ninguna caida contra la 179**:

| lo que dice el acta 179 | linea leida hoy | literal |
|---|---:|---|
| caidas del ejecutor | `62232` | "CAIDAS DEL EJECUTOR: NINGUNA, Y LO DIGO CON LA LISTA DE LO QUE BUSQUE" |
| racha de reporte | `62238` | "La racha de reporte, que mi acta 178 dejo en DOS, vuelve a CERO" |
| racha de cifra publicada | `62406` | "caidas del ejecutor que ACUMULAN **0** / racha de cifra publicada **0**" |
| racha de reporte en la metrica | `62407` | "caidas del ejecutor de reporte **0** / racha de reporte **0**" |
| parada | `62437` | "## 12. PARADA: NO" |

**NO HAY NINGUNA CORRECCION DECLARADA QUE ARRASTRAR DE LA 179.** El acta declara
UNA caida propia del auditor (`C.1`, seccion 2, linea `62031`), que es suya y no
mia, y **seis caidas que el propio ejecutor se levanto** y que el acta declara
expresamente **NO caidas de esa acta** (linea `62240`).

**1.b. LA ETIQUETA DE FUENTE, ARREGLADA, Y ESO LEVANTA MI PARADA DE LA 3.f DE LA
179.** La adjudicacion **7.7 del acta 179** estrecha la instruccion que me hacia
parar: lo que aquel encargo protegia era que ninguna clase ni su procedencia se
movieran, y un literal que atribuye a la 177 cinco lecturas de la 179 no protege
eso, lo rompe, contra `EJECUTOR.md` 8.

**LO QUE CAMBIA EN LA MAQUINA, Y NADA MAS QUE ESO.** En
`scripts/loop/vuelta178_tarea3_anotar_triangulos.py`:

- nace `etiqueta_del_registro(vuelta)`, **PURA**, que compone la etiqueta con la
  vuelta que se le pasa y dice `(vuelta desconocida)` si la fila no la trae, en
  vez de inventar un numero;
- `clases_por_par()` **lee `d.get("vuelta")` de la fila del registro** y llama a
  esa funcion, en vez del literal `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)`
  que estaba clavado en la **linea 160** del fichero de apertura;
- `clases_por_par()` gana los parametros `lecturas` y `filas`, para que su caso
  positivo por mutacion pueda apuntarla a un registro fabricado sin tocar nada
  vivo;
- el sello de `sha256` pasa de UN registro a **LOS DOS**, antes y despues, dentro
  del propio instrumento, y el ROJO cubre a los dos.

**LOS CUATRO `sha256`, IMPRESOS POR EL PROPIO INSTRUMENTO** (bloques `A)` y `H)`
de `docs/loop/SALIDA_V180_T1B_TRIANGULOS.txt`):

| registro | sha256 ANTES | sha256 DESPUES | identicos |
|---|---|---|---|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | `ea6e850d331d14f0...` | `ea6e850d331d14f0...` | **SI** |
| `docs/plan/OP_L_03_LECTURAS.jsonl` | `d93c59a86372cf50...` | `d93c59a86372cf50...` | **SI** |

Los cuatro completos: `ea6e850d331d14f01db1186a54f4913fa72eb2560a354430c5e6d047ff0d02be`
dos veces, y `d93c59a86372cf501f407a82cc79d649d02fd73c404429489ec6c07b4272719f`
dos veces. **NINGUNA CLASE SE MOVIO.** Bytes de los dos, por las dos
convenciones: `4.051.967` en disco y `4.051.967` normalizado a LF el primero;
`51.368` y `51.368` el segundo.

**LAS DOS MEDICIONES DE LA ETIQUETA, CADA UNA CON SU CORTE, Y LA VIEJA NO SE
BORRA** (`banco 9.10`). Las dos salen del mismo instrumento,
`scripts/loop/vuelta179_tarea3_etiqueta_de_fuente.py`, corrido dos veces:

| medicion | corte | fichero contado | etiquetados como de la 177 | verdaderos | **falsos** |
|---|---|---|---:|---:|---:|
| ANTES del arreglo | HEAD `d3240915e994`, apertura de la 180 | `docs/loop/SALIDA_V180_APERTURA.txt`, bloque `H.6` | 15 | 10 | **5** |
| DESPUES del arreglo | HEAD `122ca81fb96e`, tras la 1.b de la 180 | `docs/loop/SALIDA_V180_T1B_ETIQUETA_DESPUES.txt`, bloque `C)` | 10 | 10 | **0** |

**DA CERO FALSOS Y POR ESO NO PARO.** Los cinco que antes salian falsos, nombrados
uno a uno por el instrumento de apertura, eran dos lados de
`colaboracion_cadena_suministro`, uno de `creacion_option_pool` y dos de
`fase_diseno_prototipado_modelos`, **los cinco escritos por la vuelta 179**.

**EL REPARTO DE LADOS POR FUENTE CON LAS ETIQUETAS NUEVAS**, contado del bloque
`D.1)` de `docs/loop/SALIDA_V180_T1B_TRIANGULOS.txt`:

| que se cuenta | cuantos |
|---|---:|
| lados con clase leida de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **42** |
| lados con clase leida de `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)` | **10** |
| lados con clase leida de `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 179)` | **5** |
| **total de lados** | **57** |
| **total de triangulos** | **19** |

**EL TOTAL NO SE MOVIO: 19 triangulos y 57 lados**, que es lo que el encargo
exige, y `42 + 10 + 5 = 57` calza. Antes del arreglo el mismo reparto daba **42 y
15** en dos filas; ahora son tres filas y la de la 179 sale a la luz. La particion
de triangulos tampoco se movio: **8 enteros del archivo, 11 apoyados en un lado de
fuera, 9 de ellos con el `D` fuera**.

**EL CASO POSITIVO POR MUTACION, CORRIDO Y NO PROMETIDO**
(`scripts/loop/vuelta180_tarea1b_mutacion_etiqueta.py`, salida en
`docs/loop/SALIDA_V180_T1B_MUTACION_ETIQUETA.txt`, exit **0**). Registro
**fabricado en un temporal**, dos filas de **dos vueltas distintas** (177 y 180),
mapa de alias vacio y veredictos vacios: **ni un fichero vivo**.

| caso | que hace | etiquetas distintas | veredicto |
|---|---|---:|---|
| 1, el codigo de hoy | cada lado con su vuelta | **2** | **VERDE** |
| 2, la mutacion: etiqueta clavada en el literal de la 177 | los dos lados iguales | **1** | **CAE, VERDE** |

**UN REGISTRO DE UNA SOLA VUELTA NO PODRIA CAZAR ESTO**, porque con una sola
vuelta el literal acierta por casualidad; por eso el registro fabricado tiene dos.
La mutacion se deshace en `finally` y el temporal se retira (`P.16`), las dos
cosas comprobadas y publicadas por el propio arnes.

**LO QUE ESTA TAREA MOVIO EN EL ARBOL, contado con `git diff --numstat`:**
`docs/plan/OP_L_03_TRIANGULOS.jsonl` **3 lineas mas 3 menos** (las tres filas cuyos
lados cambian de etiqueta) y
`scripts/loop/vuelta178_tarea3_anotar_triangulos.py` **83 mas 21**. La guarda de
`dataset/` sale **VERDE con 0 filas, 0 ficheros y 0 blobs divergentes**.

### TAREA 2 (BLOQUEANTE). EL SUJETO CONGELADO, RESUELTO Y CABLEADO

**EL ORDEN SE RESPETO Y ES LA MITAD DE LA TAREA:** primero declararon los trece,
despues se congelaron los cuatro, la guarda dio **0**, **y solo entonces se
cablea**. Cablear con 17 habria dejado la 181 en un rojo permanente, que es
degradacion silenciosa del `banco 9`.

**2.a. LOS TRECE QUE NO ABREN NADA VIVO DECLARAN SU SUJETO.** Instrumento:
`scripts/loop/vuelta180_tarea2a_declarar_sujeto.py`, salida
`docs/loop/SALIDA_V180_T2A_DECLARAR.txt`, exit **0**. **A quien le toca NO SE
TECLEA**: sale del registro `docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl`, contado
en la corrida, **17 filas**, de las cuales `LO NOMBRA SIN ABRIRLO` **11**, `ABRE
UN SUJETO YA CLAVADO` **2** y `ABRE FICHERO VIVO` **4**. Los `11 + 2 = 13`
declaran aqui.

**LA LINEA DE CADA UNO SE COMPONE DE SU PROPIA FILA**, no de una lista tecleada:
el fichero vivo que nombra y sus tres cifras (apariciones, llamadas que leen,
lecturas del fichero vivo) salen del registro. Va **dentro del docstring de
modulo**, y eso no es capricho: `anclaje_de()` busca las huellas de congelado en
el texto entero y las de sujeto vivo **solo en la maquina**, asi que declarar en
el docstring garantiza que **la maquina no cambia**. El propio instrumento lo
comprueba con `sin_docstring_de_modulo()` antes y despues de escribir, fichero a
fichero: **13 de 13 con la maquina identica**, y **13 de 13 parsean**.

**LAS LINEAS ANADIDAS POR FICHERO**, contadas de
`docs/loop/SALIDA_V180_T2_NUMSTAT.txt` con `git diff HEAD --numstat -- scripts/loop/`:
los trece salen **`1 0`** exactos, o sea **una linea anadida y CERO borradas** en
cada uno. Son `vuelta135_2e_mutacion_1.py`, `vuelta135_2e_mutacion_2.py`,
`vuelta145_2a_mutacion_ancla_unica.py`, `vuelta148_2d_mutacion_exencion.py`,
`vuelta150_5c_mutacion_ciclo.py`, `vuelta162_tarea2a_mutacion_puerta.py`,
`vuelta162_tarea2b_mutacion_excepcion.py`, `vuelta163_tarea4b_mutacion_re_sellado.py`,
`vuelta165_tarea6_mutacion_op_l_01.py`, `vuelta166_tarea2_mutacion_correccion.py`,
`vuelta166_tarea6_mutacion_guarda.py`, `vuelta177_tarea1b_mutacion_esperado_vivo.py`
y `vuelta179_tarea3_mutacion_triangulos.py`. **NINGUNA otra linea de esos trece se
toco.**

**2.b. LOS CUATRO QUE SI ABREN. Y AQUI LEVANTO UNA CORRECCION AL ENCARGO, MEDIDA
Y NO OPINADA.** El instrumento nuevo `scripts/loop/sujeto_congelado_de_git.py`
(nombre estable, sin numero de vuelta) lee un blob de git clavado por su commit y
**comprueba su `sha256` contra el que el arnes declara**, con dos candados en vez
de uno.

| arnes | que abria | que abre ahora | prueba de que ya no se mueve |
|---|---|---|---|
| `vuelta157_tarea4b_mutacion_tachado.py` | `io.open(LD).read()` sobre `docs/plan/LECTURAS_DIRIGIDAS.md` **VIVO** | blob `24bd395b0cde:docs/plan/LECTURAS_DIRIGIDAS.md`, `sha256 dda1cdd67042c733...` comprobado dentro | dos corridas, salida enmascarada identica, `sha 231f53052759b502` las dos, exit 0 y 0 |
| `vuelta160_tarea7c_mutacion_guarda_cita.py` | `shutil.copy` de **TRES ficheros VIVOS** a un temporal, en cada corrida | `volcar_blob` de los tres blobs clavados (`7dff83ab6a17`, `24bd395b0cde`, `2743bd88faed`), los tres con su `sha256` comprobado | dos corridas, `sha 558a488b8793407f` las dos, exit 0 y 0 |
| `vuelta150_2d_simular_op_c_05.py` | `json.load(open("dataset/metadata/master_graph.json"))` **VIVO** | blob `a34328b23a7d:dataset/metadata/master_graph.json`, `sha256 627cc662296f7f00...` comprobado | dos corridas, `sha c2951c5e99c94698` las dos, exit 0 y 0 |
| `vuelta174_tarea1b_mutacion_esqueleto.py` | **NADA VIVO, y esto es la correccion** | lo mismo que antes: un `REPORTE.md` **fabricado por el en un `tempfile.mkdtemp`** | dos corridas, `sha 09f85ae25297d0ec` las dos, exit 0 y 0 |

**LA CORRECCION, DECLARADA SIN BORRAR LO QUE CORRIGE** (`EJECUTOR.md` 8). El
encargo pone `vuelta174_tarea1b_mutacion_esqueleto.py` entre los cuatro que **si
abren**, nombrando `REPORTE.md`. **Medido, no abre ninguno vivo**, y la prueba la
da el propio registro de la 179 en su campo `evidencia.codigo`, linea 182:
`vivo -> os.path.join(tmp, "REPORTE.md") | io.open(vivo).read()`, donde `tmp` es
el `tempfile.mkdtemp(prefix="v174_mut_")` que el mismo fichero crea y borra. **Lo
que le faltaba era declararlo**, no congelarlo: la guarda buscaba la huella
`REPORTE.md` en la maquina, la encontraba en el nombre del fichero fabricado y no
podia distinguir un sujeto fabricado de uno vivo. **NO PARO POR ESTO**, porque no
hace falta decidir nada que el encargo no diga: el criterio del propio encargo es
*"un sujeto que no dependa de lo que el fichero vivo diga hoy"*, y este ya lo
cumplia; lo unico pendiente era la declaracion y la prueba, y las dos estan.

**LA PRUEBA DE ESTABILIDAD, CORRIDA:**
`scripts/loop/vuelta180_tarea2b_prueba_de_congelacion.py`, salida
`docs/loop/SALIDA_V180_T2B_CONGELACION.txt`, exit **0**. **4 arneses medidos, 4
estables**, y los **5 ficheros vivos** que tenian atribuidos **no se movieron ni
un byte** en las ocho corridas. **EL PRECIO VA DECLARADO Y NO ESCONDIDO:** la
comparacion enmascara toda ruta absoluta, porque tres de los cuatro imprimen su
temporal de sufijo aleatorio; el enmascarado tapa tambien las rutas del repo, asi
que esta prueba **no cazaria un cambio que solo afectara a una ruta impresa**. Lo
que si compara sin tapar es toda cifra, todo `sha256`, todo veredicto y el exit.

**Y UNA SEGUNDA MEDIDA INDEPENDIENTE:**
`scripts/loop/vuelta179_tarea4_juzgar_sujeto.py --solo-mirar`, corrido hoy sin
escribir el registro (`docs/loop/SALIDA_V180_T2B_RELECTURA.txt`), dice **"CIFRA
entradas que la guarda senala: 0"** al corte `HEAD 7aacaa474fcc`. El juez de la
179 reconoce `git cat-file` sobre un blob como sujeto clavado, asi que **los tres
congelados ya no son lecturas vivas para su propio metodo**, y el cuarto tampoco.

**2.c. EL CABLEADO, Y SOLO ENTONCES.** Las dos mediciones, cada una con su corte:

| medicion | corte | fichero contado | entradas que no cumplen | denominador |
|---|---|---|---:|---:|
| ANTES de la 2.a y la 2.b | HEAD `d3240915e994`, apertura de la 180 | `docs/loop/SALIDA_V180_APERTURA.txt`, bloque `H.7` | **17** | 103 |
| DESPUES de la 2.a | HEAD `7aacaa474fcc` | `docs/loop/SALIDA_V180_T2A_GUARDA_TRAS_DECLARAR.txt` | **4** | 103 |
| DESPUES de la 2.b | HEAD `7aacaa474fcc` | `docs/loop/SALIDA_V180_T2C_GUARDA_DESPUES.txt` | **0** | 104 |

**DA 0, ASI QUE SE CABLEA.** El cableado vive en `verificar_mutaciones_viejas.py`,
al cierre de la corrida y **recomputado ahi**, no heredado de la cabecera: nace
`hay_rojo_al_cierre()`, **PURA**, que decide el rojo global con sus **seis
piezas** en un solo sitio, y `main()` la llama. La cifra se imprime con su sello
de corte al lado. **La guarda entra al rojo tambien en modo `--tramo`**, como ya
hacia la mirada de la nomina sobre si misma, y esta comprobado corriendo
`--tramo 1 --tamano-tramo 2` (`docs/loop/SALIDA_V180_T2C_TRAMO_CABLEADO.txt`,
exit **0**): imprime **"CIFRA entradas cuyo SUJETO NO ESTA CONGELADO
(recomputado al cierre): 0, de 104"**.

**LA CONDICION SE EXTRAJO A UNA FUNCION PURA POR UN MOTIVO, Y NO ES DE ESTILO:**
mientras vivio dentro de un `if` de `main()`, la unica forma de probar que una
guarda estaba enchufada era correr la bateria entera y mirar el color. Ahora se le
quita una pieza a la vez.

**EL CASO POSITIVO POR MUTACION DEL CABLEADO**
(`scripts/loop/vuelta180_tarea2c_mutacion_cableado.py`, salida
`docs/loop/SALIDA_V180_T2C_MUTACION_CABLEADO.txt`, exit **0**), sobre un
directorio de arneses de mentira fabricado en un temporal y una nomina fabricada,
**sin leer ni un fichero de la campana**: **10 comprobaciones, 0 fallan.**

| caso | que prueba | resultado |
|---|---|---|
| A1 | un arnes que abre un fichero vivo y no lo declara **sale senalado** | 1 senalado |
| A2 | el MISMO con la linea de declaracion **deja de salir** | 0 senalados |
| B | las seis piezas vacias: **no hay rojo** | `False` |
| C | **solo** la pieza del sujeto congelado: **hay rojo** | `True` |
| **D, LA MUTACION** | la condicion **VIEJA** sobre el mismo escenario de C | `False`, **el caso CAE** |
| E, cinco veces | cada una de las otras cinco piezas **sola** enciende el rojo | `True` las cinco |

**2.d. NADA SE PODA DE LA NOMINA, Y LA RESTA VA COMPROBADA.** La nomina crece de
**103 a 105** con los dos arneses que esta vuelta escribe, y la cuenta se recompone
al cierre de la tarea:

| cifra | valor | corte |
|---|---:|---|
| arneses que el censo ve | **165** | HEAD `7aacaa474fcc` |
| entradas de la nomina | **105** | HEAD `7aacaa474fcc` |
| censo menos nomina | **60** | HEAD `7aacaa474fcc` |
| los que estan FUERA de la nomina | **60** | HEAD `7aacaa474fcc` |
| `arneses_que_faltan()` | **0** | HEAD `7aacaa474fcc` |
| entradas invisibles al censo | **0** | HEAD `7aacaa474fcc` |
| entradas con el sujeto sin congelar | **0** | HEAD `7aacaa474fcc` |

**LA RESTA CALZA: `165 - 105 = 60`, y fuera de la nomina son 60.** Los dos que
entran son `vuelta180_tarea1b_mutacion_etiqueta.py` (103 a 104) y
`vuelta180_tarea2c_mutacion_cableado.py` (104 a 105), cada uno con su motivo
escrito en la propia nomina. **Los otros dos ficheros nuevos de esta tarea NO son
arneses y por eso no entran**, y se dice cual es la vara y no una opinion: el
patron del censo es `vuelta<N>...<familia>...py` con familia en `mutacion`,
`caso_positivo` o `simular`, y ni `sujeto_congelado_de_git.py` (sin numero de
vuelta, es instrumento estable) ni `vuelta180_tarea2a_declarar_sujeto.py` ni
`vuelta180_tarea2b_prueba_de_congelacion.py` traen ninguna de las tres familias.
**Ninguno de los tres se publica como caso positivo por mutacion**: el primero es
un lector, el segundo una operacion de una sola corrida y el tercero una MEDICION
de estabilidad, y asi esta escrito en sus docstrings.

<!-- FIN ANEXO DE TAREAS -->
