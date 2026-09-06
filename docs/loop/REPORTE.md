# REPORTE DE LA VUELTA 186 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta186_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que no lleva nada
> mas. **Cerro entera en la 184**, con sus nueve tramos sellados, asi que **la
> siguiente vuelta de bateria es la 189**. En las vueltas intermedias la seccion 9
> se cierra igual, con el **nombre del fichero, sus bytes medidos y su
> atribucion**, las tres juntas o no vale.
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, PERO LA CUENTA YA NO ESTA EN CERO.**
> El regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas
> seguidas cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. **La
> 185 cerro el suyo** y es la **PRIMERA de las dos**. **Si esta vuelta cierra el
> suyo, es la SEGUNDA y la 187 recupera el tope de CINCO.** Van dos tareas y no hay
> una tercera.
>
> **EL TRABAJO DE ESTA VUELTA ES APLICAR LAS DOS ADJUDICACIONES DEL ACTA 186 QUE
> DEJAN UN INSTRUMENTO DICIENDO DOS COSAS DEL MISMO CASO**, meter en la nomina los
> dos arneses que si no dejarian la bateria de la 189 abriendo en rojo, y cerrar el
> reporte de la 184, que lleva dos vueltas sin conseguirse.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee el
> par **2.464** ni ningun otro de la cola post fusion (**encabeza el encargo de la
> 187**, y el acta 186 explica en su seccion 12 que el tope de dos sub-tareas es
> aritmetica y no preferencia); **no se vuelve a decidir ninguna clase** en la
> relectura al doble; no se toca el marcador, ni un veredicto, ni `dataset/`; **no
> se poda la nomina de la bateria**, que es la opcion `c` que el fundador RECHAZO
> el 5 sep, y aqui se hace lo contrario, que es completarla; y **no se abre la mesa
> de los tres nodos de la puerta del `PMF`** que el acta 186 anota en su `6.4`, que
> es trabajo de plan y no de esta vuelta.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py` y desde la 178 vuelve a correr en su sitio. **Una
> columna de apertura medida al cierre es caida que ACUMULA.**
>
> **Y EL ESQUELETO VUELVE A SU SITIO DE SIEMPRE, LA APERTURA, AL REVES QUE EN LA
> 185.** Alli tuvo que esperar porque su PASO 0 habria archivado el reporte de la
> 184 sin cerrar. Aqui no hay nada de eso: el reporte del arbol es el de la 185, ya
> cerrado y ya archivado, y el de la 184 tambien esta archivado desde la TAREA 2.a
> de la 185. **El PASO 0 se corre igual y su salida se pega con lo que salga**,
> diga lo que diga, en vez de dejar la fila muda.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta186_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 185: `5834632b`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 185: LA 184 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA, ADJUDICO LOS SIETE DISCUTIBLES A FAVOR, CIERRO PD.2, PD.3 Y PD.4 POR CITA, Y EL ROJO QUE IMPIDE CERRAR EL REPORTE QUEDA DECLARADO FALSO ROJO CON SU REPARACION ENCARGADA.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V186_HEAD_APERTURA.txt`: `620dc837`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `793ad9a1`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **185**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 186`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LAS DOS CUENTAS QUE VENCEN. BLOQUEANTE. (a) El acta 186 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus SIETE adjudicaciones `5.1` a `5.7` todas a favor, los CUATRO pendientes de doctrina de la seccion 6 (`PD.5` y `PD.6` CERRADAS por cita, `PD.1` ABIERTA con sus cinco puestos leidos del acta, y el `6.4` como ANOTACION y no como pendiente propio), las TRES preguntas de la seccion 7 las tres CONTESTADAS, CERO caidas propias del auditor registradas COMO CERO Y NO OMITIDAS, UNA caida de reporte del ejecutor (`R.1`, la del `git status` en cero lineas) que NO acumula por vivir en prosa, y la deuda de la serie REMEDIDA en esta vuelta y no heredada del `R.47`, mas su caso positivo por mutacion sobre un acta FABRICADA con el esperado mutado cayendo. (b) LOS DOS ARNESES DE LA 185 ENTRAN EN LA NOMINA, que es la respuesta a la `P.3`: `arneses_que_faltan()` tiene que devolver 0 despues, con el tamano de la nomina antes y despues, y los dos arneses corridos DOS VECES CADA UNO EN PROCESOS APARTE exigiendo el mismo `sha256`. NO SE PODA NADA. (c) LA RELECTURA AL DOBLE del tramo de la ciega del acta 186, con el cotejo de `sha256` contra el sello `V187` ANTES de leer un solo puesto, 30 puestos mas 30 vecinos deterministas con `vecinos()` IMPORTADA, solape 0 por los dos lados MEDIDO, las cuatro discrepancias del auditor miradas con la misma vara, y la cuenta de clases `B` del universo releido | **CERRADA** | `SALIDA_V186_T1A_REGISTRO_R48.txt`, `SALIDA_V186_T1A_MUTACION_REGISTRO_186.txt`, `SALIDA_V186_T1B_NOMINA.txt`, `SALIDA_V186_T1C_RELECTURA_AL_DOBLE.txt`, `SALIDA_V186_COTEJO_DE_CLONES.txt` |
| **TAREA 2** | LAS TRES REPARACIONES DE `cerrar_reporte.py`, LA ESCALADA Y EL CIERRE DE DOS REPORTES. (a) La pieza (4) deja de llevar su propia copia de `ajena != vuelta` y LLAMA a la unica sede, con parametro nuevo cuyo valor por defecto conserva EXACTAMENTE la conducta de hoy y computado en `main()` sin bandera, con arnes propio. (b) La pieza (2) busca el hueco de cabecera FUERA de los bloques cercados REUSANDO el desbloqueador que `cifras_sin_pareja()` ya tenia, separado a una sede y llamado por las dos, con arnes propio. (c) El carril de CIERRE TARDIO, computado y no pasado por bandera, donde las cifras sin pareja NO bloquean pero SE DECLARAN una a una dentro del propio reporte cerrado, con arnes propio; y DESPUES, y no antes, el reporte de la 184 se cierra y se archiva tras cotejar sus tres piezas por `sha256` y por bytes. (d) LA ESCALADA de `AUDITOR.md` 1.2: una guarda que extrae de `SALIDA_V<N>_APERTURA.txt` las dos cifras del estado del arbol y las coteja contra lo que la seccion 4 del reporte afirma, cayendo en ROJO si discrepan o si el reporte no las afirma, con arnes propio que exige que HUBIERA CAZADO LA `R.1`. (e) El reporte de la 186 se abre en su esqueleto, cada tarea anexa su fila al cerrarse, la cabecera se talla y `--comparar` tiene que dar CABECERA IDENTICA AL TALLADOR, y su SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS Y LAS DOS CUENTAS QUE VENCEN. CERRADA

**LO QUE ESTA TAREA SOSTIENE, EN UNA LINEA: el acta 186 entra en la serie como
`R.48` con sus cinco numerales computados del acta y ninguno tecleado; los dos
arneses de la 185 entran en la nomina y `arneses_que_faltan()` pasa de 2 a 0, con
los dos corridos dos veces en procesos aparte dando el mismo `sha256`; y el tramo
de la ciega del acta 186 se relee AL DOBLE, 60 puestos con solape 0 por los dos
lados.**

#### 1.a EL ACTA 186 EN LA SERIE, CON EL NUMERO LLAMADO Y NO TECLEADO

`scripts/loop/serie_de_registros.py`, corrido en esta vuelta desde el instrumento
de la 1.a, devolvio **`R.48`**. El encargo decia `R.48` y aqui NO se copio: se
llamo. La serie recomputada de sus DOS sedes daba **39 entradas** antes de
escribir y **40** despues, con **0 colisiones** y **0 huecos** en las dos
mediciones.

El acta se acoto ANTES de contar nada: `docs/loop/ACTA_AUDITOR.md`, **lineas
64908 a 65440**, o sea **533 lineas**. Todo lo que sigue esta contado de ese
tramo.

Lo contado, y cada cifra sale de su patron corrido hoy:

| que | cifra | como se conto |
|---|---:|---|
| adjudicaciones numeradas `5.1` a `5.7` | **7** | patron entrecomillado, importado del registrador de la 184 |
| numerales de la seccion 6, `6.1` a `6.4` | **4** | el mismo patron con otro prefijo |
| preguntas de la seccion 7, `7.1` a `7.3` | **3** | el mismo patron con otro prefijo, y ningun registrador anterior las contaba |
| caidas propias del auditor | **0** | patron `A.n` de cabecera de tercer nivel |
| caidas de reporte del ejecutor | **1** | patron `R.n`, en la linea 65301 |
| patron SIN comillas del acta 183, de contraste | **0** | se conserva intacto y su cero se publica |
| patron `C.n` de linea, de contraste | **0** | |
| patron `C.n` de negrita de frase, de contraste | **0** | |
| patron `E.n` de las actas 182 y 184, de contraste | **0** | |

**EL CERO DE CAIDAS PROPIAS VA CONTADO Y DECLARADO, QUE NO ES LO MISMO QUE
OMITIDO.** El patron da 0, pero un cero que sale de un patron que no muerde no es
evidencia de nada, asi que va con la declaracion del acta al lado: la frase `CERO
CAIDAS PROPIAS` aparece en **la linea 64925** del acta, y la frase que usaba el
acta 185, `NINGUNA CAIDA PROPIA`, aparece en **0 lineas**. Ese cambio de frase es
la razon por la que este registrador anade el patron nuevo en vez de ensanchar el
viejo. El instrumento hace PARADA si sale cero sin que el acta lo declare por
ninguna de las dos.

**EL REPARTO DE LA SECCION 6 SE LEE DEL TITULO Y NO SE TECLEA, Y HAY UN ESTADO
NUEVO.** El registrador de la 185 solo sabia leer ABIERTA o CERRADA, y con el
acta 186 habria hecho PARADA en el `6.4`. El reparto medido hoy:

- `6.1` nombra `PD.6`, estado **CERRADA** (linea 65210)
- `6.2` nombra `PD.5`, estado **CERRADA** (linea 65226)
- `6.3` nombra `PD.1`, estado **ABIERTA** (linea 65244)
- `6.4` no nombra ningun `PD`, estado **ANOTACION** (linea 65250)

El `6.4` no es un pendiente y no se convierte en uno: el propio acta escribe que
*"no lo encargo y no lo adjudico"*, y meterlo en el saco de los cerrados o en el
de los abiertos habria publicado una cifra falsa de pendientes. El estado sale de
buscar en el titulo literal, en ese orden, `NO LO CONVIERTO EN UNO`, `SIGUE
ABIERTA` y `ADJUDICAD`.

**LOS CINCO PUESTOS DE LA `PD.1` NO SE COPIARON DEL ENCARGO: SE LEYERON DEL
PARRAFO DEL NUMERAL QUE EL PROPIO TITULO DECLARA ABIERTO**, y salieron **1778,
2530, 2540, 3141, 3232**, que es lo que el encargo decia. Si el acta hubiera dicho
otros, la entrada diria otros, y el arnes lo prueba con actas fabricadas que
llevan puestos distintos.

**EL ESTADO DE LAS TRES PREGUNTAS TAMPOCO SE SUPONE:** sale de la cabecera literal
de la seccion 7, `docs/loop/ACTA_AUDITOR.md:65256`, que dice *"## 7. LAS TRES
PREGUNTAS, QUE ERAN MIAS Y LAS CONTESTO"*. Si esa cabecera no dijera `LAS
CONTESTO`, el instrumento haria PARADA en vez de registrarlas como contestadas, y
el arnes corre ese caso sobre un acta fabricada muda.

**LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL `R.47`:** en el
tramo de las actas 173 a 185 hay **8 actas sin entrada propia**, las **173 a 180**,
con extremo bajo **`R.42` cubre el acta 172** y extremo alto **`R.43` cubre el acta
181**. No se rellenan aqui.

**EL CASO POSITIVO POR MUTACION, SOBRE UN ACTA FABRICADA Y NUNCA SOBRE LA REAL.**
Diez mutaciones, cada una con su esperado mutado cayendo. Su fichero de salida
`docs/loop/SALIDA_V186_T1A_MUTACION_REGISTRO_186.txt` dice `CIFRA fallos: 0` y
`VEREDICTO: VERDE`, y mide 5760 bytes en disco y 5760 normalizados a LF. La cuarta
mutacion es la que prueba el estado nuevo: sobre un acta fabricada CON anotacion el
reparto sale `ANOTACION 1, ABIERTA 1, CERRADA 2, SIN DECIR 0`, y sobre una
fabricada SIN anotacion la palabra ANOTACION no aparece.

**LA ENTRADA ESCRITA:** `docs/PENDIENTES.md` pasa de **894124 bytes en disco a
909780 bytes**, la entrada mide **15655 bytes en disco y 15655 normalizados a LF**
en **154 lineas**, se releyo del disco byte a byte, y trae **0 guiones largos o
medios**.

#### 1.b LOS DOS ARNESES DE LA 185 EN LA NOMINA, QUE ES LA RESPUESTA A LA `P.3`

**LA NOMINA CRECIO EN DOS Y EN NADA MAS.** La cifra de ANTES no se recuerda: sale
del bloque de apertura sellado de esta vuelta, que la publica como `CIFRA nomina
ANTES: 113`, y la de DESPUES se cuenta de `VIEJAS` en el propio proceso:

| | cifra | de donde sale |
|---|---:|---|
| nomina ANTES | **113** | `docs/loop/SALIDA_V186_APERTURA.txt`, bloque H.3 |
| nomina DESPUES | **115** | `len(VIEJAS)` contado en el proceso de la 1.b |
| crecimiento | **+2** | computado, no tecleado |
| entradas duplicadas | **0** | |
| `arneses_que_faltan()` ANTES | **2** | apertura, bloque H.3 |
| `arneses_que_faltan()` DESPUES | **0** | y esa es la prueba que el acta 186 pide en su `7.3` |
| `nomina_invisible_al_censo()` | **0** | |
| `guarda_del_sujeto_congelado()` | **0** | no cableada al rojo global por el encargo de la 179 |
| censo | **175** | y `VARA_DEL_CENSO` sigue en **148** |

**NO SE PODO NADA, Y NO SOBRABA NADA.** La opcion `c` de la parada del 5 sep
(jubilar arneses viejos) esta RECHAZADA por el fundador; aqui la nomina crece, que
es lo contrario. No se toco ninguna entrada existente y las dos nuevas se anadieron
en la sede que `arneses_que_faltan()` consulta, que es `VIEJAS` en
`scripts/loop/verificar_mutaciones_viejas.py`.

**Y LA DOBLE CORRIDA, HECHA HOY PARA NO ENTERARSE EN LA 189.** Cada arnes corrio
DOS VECES EN PROCESOS APARTE. Las dos pasadas de cada uno dieron el mismo `sha256`,
y ademas el mismo que estaba commiteado antes de correr:

| arnes | su salida sellada | bytes en disco, iguales normalizados a LF | `sha256` de disco y de LF, iguales |
|---|---|---:|---|
| `vuelta185_tarea1b_mutacion_sin_temporal.py` | `docs/loop/SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt` | **6100** | `4de055338ac9412b43ef17832fed78cb` |
| `vuelta185_tarea1c_mutacion_bateria_continuada.py` | `docs/loop/SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt` | **7937** | `6a2d8721c1a1b75d6c0350c4697b1ebb` |

Los dos salieron con `EXITCODE 0` en las cuatro corridas. **Ninguno cambia solo**,
que era lo que hundio al arnes de la 182 en la bateria de la 184.

#### 1.c LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 186

**EL SELLO SE COTEJO ANTES DE LEER UN SOLO PUESTO, Y SU CIFRA SE COMPUTO EN VEZ DE
COPIARSE DEL ENCARGO.** El sello se llama **`V187`** y no `V186`, porque la casa
nombra el sello del acta N como `V(N+1)`; el `V186` no existe y no se fabrico.

- `docs/loop/SELLO_APERTURA_AUDITOR_V187.json`: **799 bytes en disco y 799
  normalizados a LF**
- la ciega mide **39911 bytes en disco y 39911 normalizados a LF**, que es lo que
  el sello declara
- su `sha256` computado hoy, de disco y normalizado a LF iguales:
  `fd1275d43498fc9f1bd716da33355f7d`
- **EL FICHERO ES EL QUE EL SELLO DICE: SI**

**EL DOBLE, Y LOS DOS SOLAPES MEDIDOS Y NO SUPUESTOS:**

| que | cifra |
|---|---:|
| puestos del tramo, leidos de la ciega sellada | **30** |
| vecinos deterministas, con `vecinos()` IMPORTADA y no copiada | **30** |
| solape entre tramo y vecinos | **0** |
| solape con la ciega inmediatamente anterior, la `V185b` | **0** |
| puestos releidos EN TOTAL | **60**, que es el doble exacto |
| declaran diferenciador | **5** |
| con lesion exacta | **1**, el puesto 2230 |
| con algun nodo muerto en el grafo de hoy | **0** |
| clase `A` en el universo | **11** |
| clase `B` en el universo | **1** |
| clase `D` en el universo | **48** |

**LAS CUATRO DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA VARA, Y NINGUNA CLASE
SE VUELVE A DECIDIR.** Las cuatro caen DENTRO del universo releido:

| puesto | clase del archivo | declara diferenciador | lesion exacta | nodo muerto |
|---:|:-:|:-:|:-:|:-:|
| **338** | `B` | no | no | no |
| **491** | `D` | no | no | no |
| **1775** | `D` | no | no | no |
| **2599** | `D` | no | no | no |

**LO QUE LA VARA VE EN LAS CUATRO ES: NADA.** Ninguna declara diferenciador,
ninguna tiene lesion exacta y ninguna tiene un nodo muerto. **Y eso es exactamente
lo que se afirma y ni una palabra mas:** las cuatro son discrepancias de JUICIO
sobre el solape, y la vara mecanica no juzga solape. Lo que la vara no ve, esta
salida no lo afirma.

**LA CIFRA DE CLASES `B`, QUE EL ENCARGO PIDE Y QUE AQUI SOLO SE CUENTA:** en el
universo releido hay **1 clase `B` de 60**, y es el puesto **338**. En todo el
archivo, contadas del archivo y no del encargo, hay **72 clases `B` de 3388
filas**. **No se interpreta ni se adjudica.**

**LA UNICA LESION EXACTA DEL UNIVERSO ES EL PUESTO 2230**, que es un VECINO y no
del tramo: la vara dice que hoy el paso 5 de `responsabilidad_prospectiva` cubre 5
palabras del diferenciador declarado, con cobertura 0.71. **Se nombra y no se
toca**, porque esta vuelta no mueve ningun veredicto.

#### LOS CLONES DECLARADOS DE ESTA TAREA, COTEJADOS, Y SE PEGA LO QUE SALGA

Tres clones se declararon y los tres se cotejaron con
`scripts/loop/cotejar_clon_declarado.py`. **No se afirma que ningun diff salga
vacio**, y de hecho ninguno lo sale:

| clon | contra | lineas de maquina que difieren |
|---|---|---:|
| `vuelta186_apertura.py` | `vuelta185_apertura.py` | **468** |
| `vuelta186_esqueleto_reporte.py` | `vuelta185_esqueleto_reporte.py` | **50** |
| `vuelta186_tarea1c_relectura_al_doble.py` | `vuelta185_tarea1e_relectura_al_doble.py` | **82** |

Los tres cotejos salieron con `EXITCODE 0` y su salida entera vive en
`docs/loop/SALIDA_V186_COTEJO_DE_CLONES.txt`. **La diferencia que el encargo manda
declarar aparte esta declarada: el clon de la relectura apunta al sello `V187`, no
al `V185b`**, y ademas cambia la ciega anterior, la lista de discrepancias (de
siete a cuatro), el nombre de la salida y el bloque nuevo de la cuenta de `B`.

#### LAS RUTAS DE PRUEBA DE ESTA TAREA, TODAS COMPROBADAS Y NINGUNA DE CERO BYTES

| ruta | bytes en disco, iguales normalizados a LF |
|---|---:|
| `docs/loop/SALIDA_V186_T1A_REGISTRO_R48.txt` | **5751** |
| `docs/loop/SALIDA_V186_T1A_MUTACION_REGISTRO_186.txt` | **5760** |
| `docs/loop/SALIDA_V186_T1B_NOMINA.txt` | **3693** |
| `docs/loop/SALIDA_V186_T1C_RELECTURA_AL_DOBLE.txt` | **13632** |
| `docs/loop/SALIDA_V186_COTEJO_DE_CLONES.txt` | **49804** |

<!-- FIN ANEXO DE TAREAS -->
