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

**EL VEREDICTO DE UNA LINEA: LAS DOS TAREAS DEL ENCARGO CIERRAN Y ESTA VUELTA CIERRA SU PROPIO REPORTE, QUE ES LA SEGUNDA SEGUIDA Y DEVUELVE EL TOPE A CINCO; LAS DOS ADJUDICACIONES DEL ACTA 186 QUEDAN APLICADAS CON UN ARNES CADA UNA, EL REPORTE DE LA 184 CIERRA EN VERDE POR EL CARRIL DE CIERRE TARDIO CON SUS DIEZ CIFRAS SIN PAREJA DECLARADAS, Y LA ESCALADA DE LA SECCION 4 CAZA LA CAIDA QUE LA TRAJO; UNA CAIDA PROPIA, LEVANTADA POR MI ANTES DE QUE LA MIDA NADIE.**
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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 186`, y su salida
cruda vive en `docs/loop/SALIDA_V186_TALLADOR_CABECERA.txt` (2501 bytes en disco y 2481 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `5834632b` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 185: LA 184 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA, ADJUDICO LOS SIETE DISCUTIBLES A FAVOR, CIERRO PD.2, PD.3 Y PD.4 POR CITA, Y EL ROJO QUE IMPIDE CERRAR EL REPORTE QUEDA DECLARADO FALSO ROJO CON SU REPARACION ENCARGADA.'), HEAD real de apertura `620dc837` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `8c952bb1` (leido de `SALIDA_V186_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LAS DOS CUENTAS QUE VENCEN. BLOQUEANTE. (a) El acta 186 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus SIETE adjudicaciones `5.1` a `5.7` todas a favor, los CUATRO pendientes de doctrina de la seccion 6 (`PD.5` y `PD.6` CERRADAS por cita, `PD.1` ABIERTA con sus cinco puestos leidos del acta, y el `6.4` como ANOTACION y no como pendiente propio), las TRES preguntas de la seccion 7 las tres CONTESTADAS, CERO caidas propias del auditor registradas COMO CERO Y NO OMITIDAS, UNA caida de reporte del ejecutor (`R.1`, la del `git status` en cero lineas) que NO acumula por vivir en prosa, y la deuda de la serie REMEDIDA en esta vuelta y no heredada del `R.47`, mas su caso positivo por mutacion sobre un acta FABRICADA con el esperado mutado cayendo. (b) LOS DOS ARNESES DE LA 185 ENTRAN EN LA NOMINA, que es la respuesta a la `P.3`: `arneses_que_faltan()` tiene que devolver 0 despues, con el tamano de la nomina antes y despues, y los dos arneses corridos DOS VECES CADA UNO EN PROCESOS APARTE exigiendo el mismo `sha256`. NO SE PODA NADA. (c) LA RELECTURA AL DOBLE del tramo de la ciega del acta 186, con el cotejo de `sha256` contra el sello `V187` ANTES de leer un solo puesto, 30 puestos mas 30 vecinos deterministas con `vecinos()` IMPORTADA, solape 0 por los dos lados MEDIDO, las cuatro discrepancias del auditor miradas con la misma vara, y la cuenta de clases `B` del universo releido | **CERRADA** | `SALIDA_V186_T1A_REGISTRO_R48.txt`, `SALIDA_V186_T1A_MUTACION_REGISTRO_186.txt`, `SALIDA_V186_T1B_NOMINA.txt`, `SALIDA_V186_T1C_RELECTURA_AL_DOBLE.txt`, `SALIDA_V186_COTEJO_DE_CLONES.txt` |
| **TAREA 2** | LAS TRES REPARACIONES DE `cerrar_reporte.py`, LA ESCALADA Y EL CIERRE DE DOS REPORTES. (a) La pieza (4) deja de llevar su propia copia de `ajena != vuelta` y LLAMA a la unica sede, con parametro nuevo cuyo valor por defecto conserva EXACTAMENTE la conducta de hoy y computado en `main()` sin bandera, con arnes propio. (b) La pieza (2) busca el hueco de cabecera FUERA de los bloques cercados REUSANDO el desbloqueador que `cifras_sin_pareja()` ya tenia, separado a una sede y llamado por las dos, con arnes propio. (c) El carril de CIERRE TARDIO, computado y no pasado por bandera, donde las cifras sin pareja NO bloquean pero SE DECLARAN una a una dentro del propio reporte cerrado, con arnes propio; y DESPUES, y no antes, el reporte de la 184 se cierra y se archiva tras cotejar sus tres piezas por `sha256` y por bytes. (d) LA ESCALADA de `AUDITOR.md` 1.2: una guarda que extrae de `SALIDA_V<N>_APERTURA.txt` las dos cifras del estado del arbol y las coteja contra lo que la seccion 4 del reporte afirma, cayendo en ROJO si discrepan o si el reporte no las afirma, con arnes propio que exige que HUBIERA CAZADO LA `R.1`. (e) El reporte de la 186 se abre en su esqueleto, cada tarea anexa su fila al cerrarse, la cabecera se talla y `--comparar` tiene que dar CABECERA IDENTICA AL TALLADOR, y su SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO | **CERRADA** | `SALIDA_V186_T2A_MUTACION_PIEZA4.txt`, `SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt`, `SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt`, `SALIDA_V186_T2C_CERRAR_REPORTE_184.txt`, `SALIDA_V186_T2D_MUTACION_SECCION4.txt`, `SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt` |
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

**LA ENTRADA ESCRITA:** `docs/PENDIENTES.md` pasa de **894124 bytes en disco a 909780 bytes**, la entrada mide **15655 bytes en disco y 15655 normalizados a LF**
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

- `docs/loop/SELLO_APERTURA_AUDITOR_V187.json`: **799 bytes en disco y 799 bytes normalizados a LF**
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

| ruta | bytes en disco, iguales normalizados a LF salvo donde se diga |
|---|---:|
| `docs/loop/SALIDA_V186_T1A_REGISTRO_R48.txt` | **5751** |
| `docs/loop/SALIDA_V186_T1A_MUTACION_REGISTRO_186.txt` | **5760** |
| `docs/loop/SALIDA_V186_T1B_NOMINA.txt` | **3693** |
| `docs/loop/SALIDA_V186_T1C_RELECTURA_AL_DOBLE.txt` | **13632** |
| `docs/loop/SALIDA_V186_COTEJO_DE_CLONES.txt` | **49804** en disco y **49036** en LF |

### TAREA 2. LAS TRES REPARACIONES, LA ESCALADA Y EL CIERRE DE DOS REPORTES. CERRADA

**LO QUE ESTA TAREA SOSTIENE, EN UNA LINEA: las dos adjudicaciones del acta 186
que dejaban a `cerrar_reporte.py` diciendo dos cosas del mismo caso quedan
aplicadas, cada una con su arnes propio; el carril de CIERRE TARDIO existe y se
computa de git; el reporte de la 184 CIERRA EN VERDE con sus diez cifras sin
pareja DECLARADAS una a una; y la escalada de la `2.d` esta en codigo y su arnes
prueba que HABRIA CAZADO la `R.1`.**

#### 2.a LA PIEZA (4) DEJA DE LLEVAR SU PROPIA COPIA DE LA REGLA. ES LA `PD.6`

La comparacion `ajena != vuelta` vivia **dos veces** en el fichero, medido en el
bloque de apertura de esta vuelta antes de tocar nada: **lineas 438 y 905**. La
de la linea 438 vive en `rama_de_la_seccion9()`, que la 185 ya reparo; la de la
905 era la copia de la pieza (4), que no recibia la evidencia de los tramos.

**LO QUE SE HIZO, Y ES LA MITAD QUE IMPORTA:** la pieza (4) **NO recibio una
copia sincronizada**. `piezas_que_faltan()` gano un sexto parametro,
`tramos_sellados_en_esta_vuelta`, con valor por defecto `None`, y la pieza (4)
**LLAMA** a `rama_de_la_seccion9()` y cae solo cuando esa rama dice `ROJO`. En
`main()` ese valor **se computa con `tramos_por_vuelta()`** y se le pasa la misma
lista que ya recibia la rama: **no se anadio ninguna opcion de linea de ordenes**,
porque una evidencia que se puede teclear no es una evidencia.

**EL ROJO VIEJO NO SE REESCRIBIO:** la pieza (4) sigue cayendo con su texto de
hoy, palabra por palabra, y el arnes lo exige letra por letra.

Los casos, todos cayendo al mutar su esperado
(`docs/loop/SALIDA_V186_T2A_MUTACION_PIEZA4.txt`, **3601 bytes en disco y 3601 bytes normalizados a LF**):

| caso | que exige | resultado |
|---|---|---|
| A | la bateria de la 183 cerrando la 184 CON tramos sellados: la pieza (4) NO falta | CALZA |
| B | la misma con la lista VACIA: falta, con el motivo LITERAL de hoy | CALZA, letra por letra |
| C | la bateria de la 185 cerrando la 184, con tramos y sin ellos: falta las dos veces | CALZA |
| D | el defecto `None` se comporta igual que la logica vieja, en 8 escenarios | **difieren en 0** |
| E | las apariciones de la comparacion en el fichero: se exige **1** | **2 crudas** (lineas 438 y 917) y **1 en codigo** |

**EL CASO D NO SE AFIRMA, SE MIDE:** el arnes lleva dentro una copia declarada de
la logica vieja de la pieza (4) y compara escenario a escenario. **Difieren en 0
de 8.**

**Y EL CASO E CUENTA APARTE LAS LINEAS DE COMENTARIO, Y SE DICE EN VEZ DE
ESCONDERLO.** La reparacion deja un comentario que NOMBRA la comparacion para
explicar por que la pieza (4) llama en vez de comparar, y un comentario no es una
copia de la regla. Por eso el conteo crudo da **2** y el de codigo da **1**, y
**las dos cifras se publican**. El propio arnes prueba que sabe contar: sobre un
texto fabricado con dos copias en codigo y una en comentario, saca **2 en codigo
y 3 crudo**.

#### 2.b LA PIEZA (2) DEJA DE CAER SOBRE UNA CITA. ES LA `PD.5`

Nace `renglones_fuera_de_cerca()`, que **no es codigo nuevo**: es el
desbloqueador que `cifras_sin_pareja()` ya tenia dentro, **separado a una sede**.
Ahora lo llaman `cifras_sin_pareja()` y la pieza (2), y **no se escribio un
tercero**.

**Y SE DECLARA LO QUE NO SE TOCO:** `parrafos_fuera_de_cerca()` conserva su propio
recorrido de cercas porque hace **otro trabajo** (agrupa renglones en parrafos y
corta el parrafo en la frontera). Fundirla habria cambiado de paso la guarda de
las citas de arnes, que no es lo que esta vuelta viene a hacer.

**LO DEMAS DE LA PIEZA (2) NO SE TOCO**, y el arnes lo exige: el tallador sin
filas sigue siendo rojo con su texto de hoy, y una fila sin pegar sigue siendo
rojo.

Los casos (`docs/loop/SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt`, **2607 bytes en disco y 2607 bytes normalizados a LF**), **9 casos y los 9 caen al mutar su
esperado**:

| caso | resultado |
|---|---|
| A. la marca FUERA de toda cerca | **falta** |
| B. la marca SOLO DENTRO de una cerca | **no falta** |
| C. la marca EN LAS DOS | **falta** |
| D. cero marcas | **no falta** |
| E. una cerca SIN CERRAR y la marca detras | **no falta**, y con su valor exacto afirmado: **0 renglones con la marca fuera de cerca**, no un "lo que salga" |
| F. el texto REAL del reporte de la 184 cerrado en rojo | **ya no falta** |
| G. el tallador sin filas | **sigue siendo rojo**, con su texto de hoy |
| H. una fila sin pegar | **sigue siendo rojo** |

**EL CASO F ES EL QUE TRAJO LA ADJUDICACION**, y esta medido sobre el fichero
real de **122030 bytes en disco y 122030 normalizados a LF**: la marca aparece
**1 vez DENTRO de cerca y 0 veces fuera**, exactamente como la `PD.5` decia.

#### 2.c EL CARRIL DE CIERRE TARDIO, Y EL REPORTE DE LA 184 CIERRA. ES LA `P.2`

Nacen tres funciones: `vuelta_en_curso()`, que lee del asunto del ultimo commit
con `git log` y es la unica que toca git; `es_cierre_tardio()`, que es **PURA**;
y `declaracion_de_cifras_sin_pareja()`, que tambien lo es. **La condicion se
computa y no se pasa por bandera**, y **si la vuelta en curso no se puede leer,
el carril NO se abre**: la falta de evidencia lo cierra, no lo abre.

**EN EL CARRIL NORMAL NO CAMBIA NADA**, y eso se comprobo con el arnes y no con
la vista: la comprobacion de las cifras sin pareja lleva una columna `bloquea`
que solo ella pone a `not tardio`, y el arnes **cuenta las apariciones de esa
expresion en el instrumento y exige 1**.

Los casos (`docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt`, **5040 bytes en disco y 5040 bytes normalizados a LF**), **18 casos y los 18 caen al mutar su
esperado**: la condicion del carril en cinco escenarios; las cifras sin pareja
bloqueando en normal y no bloqueando en tardio; **la declaracion cotejada por
contencion renglon a renglon, 3 de 3**; su cuenta total; la prueba de que la
declaracion **va dentro de una cerca y por eso no se acusa a si misma**; el cero
declarado y no omitido; y las cuatro piezas rotas una a una para exigir que
**ninguna se afloje**.

**LA PRUEBA MAS FUERTE DE QUE EL CARRIL NO TOCA LAS CUATRO PIEZAS ES DE FORMA:**
`piezas_que_faltan()` **ni siquiera tiene un parametro de carril**, asi que no
puede saber en cual esta. El arnes lo comprueba leyendo su firma.

**EL CIERRE DEL REPORTE DE LA 184, DESPUES Y NO ANTES.**

Las tres piezas se cotejaron **recomputandolas hoy**, y las tres **CALZAN** con
lo que la 184 midio y la 185 confirmo
(`docs/loop/SALIDA_V186_T2C_VEREDICTO_184.txt`, **2322 bytes en disco y 2322 bytes normalizados a LF**):

| pieza | lo medido hoy | lo que midio la 184 |
|---|---|---|
| `docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt` | **2435 bytes en disco y 2415 normalizados a LF** | lo mismo |
| `scripts/loop/_v184_cierre_texto.md` | **13982 bytes en disco y 13982 en LF**, `sha256` de LF `050cdbb4ea99e11c` | lo mismo |
| `docs/loop/SALIDA_V183_BATERIA.txt` | **71753 bytes en disco y 71753 en LF**, `sha256` de LF `422a909ad6ffb167` | lo mismo |

El veredicto de una linea fue **TALLADO y no tecleado**, con sus dos numerales en
palabra computados del cuerpo, y la guarda `B.1` dio **`CIFRA numerales que NO
calzan: 0`**. El tallador corre ademas su propia mutacion: al cambiar un numeral
por otro, la guarda **CAE**.

`scripts/loop/cerrar_reporte.py --vuelta 184` salio con **`EXITCODE 0`** y
**VERDE con sus cuatro piezas**
(`docs/loop/SALIDA_V186_T2C_CERRAR_REPORTE_184.txt`, **6128 bytes en disco y 6030 bytes normalizados a LF**). El carril salio **CIERRE TARDIO**, con la vuelta en curso
leida de git en **186** y la del reporte en **184**. Las **10** cifras sin pareja
quedaron **declaradas una a una con su linea y su cuenta total** en una seccion
10 nueva.

**EL ARCHIVADO SE CORRIO DOS VECES Y LAS DOS SALIDAS SE PUBLICAN**, porque
esconder la decision seria peor que tomarla:

| corrida | exitcode | que dijo |
|---|---:|---|
| sin `--forzar` (`docs/loop/SALIDA_V186_T2C_ARCHIVAR_184_SIN_FORZAR.txt`, **790 bytes en disco y 780 bytes en LF**) | **1** | el destino ya existia con contenido DISTINTO, el reporte de la 184 **sin cerrar** |
| con `--forzar` (`docs/loop/SALIDA_V186_T2C_ARCHIVAR_184.txt`, **965 bytes en disco y 948 bytes en LF**) | **0** | VERDE |

**NADA SE PIERDE AL PISARLO, Y SE COMPROBO ANTES DE PISARLO:** el texto viejo de
**33608 bytes en disco y 33608 normalizados a LF** sigue entero en
`docs/loop/SALIDA_V185_T2A_REPORTE_184_ANTES.md`, **byte a byte identico** al que
se piso, con los dos `sha256`, el de disco y el de LF, en `6bbeb09c5822c192`.

**Y SI, EL ARCHIVADO ES EL CERRADO.** `docs/loop/reportes/REPORTE_V184.md` mide
ahora **124249 bytes en disco y 124249 normalizados a LF**, en **1902 lineas**,
con `sha256` de disco y de LF iguales en `6e1a55a3d33be771`. Lleva la seccion 10
del carril tardio y **ya no lleva** el veredicto `SIN ESCRIBIR TODAVIA`. La marca
del hueco de cabecera sigue apareciendo **una vez, en la linea 353, DENTRO de una
cerca**: es la cita de la salida roja de la 185, o sea el falso positivo que la
`2.b` acaba de cerrar, y por eso este cierre pudo hacerse.

#### 2.d LA ESCALADA: LA SECCION 4 CONTRA LA APERTURA SELLADA. `AUDITOR.md` 1.2

**ESTO ES LA OPERACION DE CODIGO DE UNA ESCALADA CON LA RACHA EN DOS, NO UNA
MEJORA.** Nacen cuatro funciones **PURAS** (`cifras_de_la_apertura()`,
`primer_numero()`, `cifras_que_afirma_la_seccion4()` y
`seccion4_que_no_calza()`) y un lector que es la unica pieza que toca disco. La
que lee la seccion 4 **REUSA `renglones_fuera_de_cerca()`**, la sede que nacio en
la `2.b`: **una cita pegada no es una afirmacion del reporte**.

**LAS TRES FORMAS DE CAER, Y LA TERCERA ES LA QUE MAS IMPORTA:** la apertura no
publica la cifra; las cifras **discrepan**, y el motivo **nombra las dos cifras y
sus dos sedes**; o **la seccion 4 no la afirma**, que **NO es verde: es su propio
rojo**. Una cifra ausente y una cifra que calza no son lo mismo.

La guarda lee **digitos y numerales en palabra**, y **cruza el salto de renglon**
que el markdown mete, porque la `R.1` esta escrita con el marcador al final de una
linea y el `cero` al principio de la siguiente. **Una guarda que no cruzara ese
salto se comeria la mitad del caso que la trajo.**

Los casos (`docs/loop/SALIDA_V186_T2D_MUTACION_SECCION4.txt`, **5007 bytes en disco y 5007 bytes normalizados a LF**), **11 casos y los 11 caen al mutar su
esperado**: las dos calzando; la de status mutada; la de numstat mutada; la
seccion 4 muda; la apertura incompleta; la frase partida en dos renglones; la
cifra citada dentro de una cerca, que **no cuenta**; y las dos sedes nombradas.

**Y EL CASO QUE PRUEBA LA ESCALADA, SOBRE LOS FICHEROS REALES DE LA 185:**

- la apertura sellada de la 185 publica **`CIFRA lineas de status: 2`** y
  **`CIFRA filas de numstat AL ENTRAR: 0`**
- la seccion 4 de `docs/loop/reportes/REPORTE_V185.md` afirma **15** en su linea
  **574** y **cero** en su linea **581**, y **0** para el numstat en la **575**
- la guarda saca **2 motivos en rojo**, los dos nombrando las dos sedes

**LA GUARDA HUBIERA CAZADO LA `R.1`: SI.** Y **la de numstat de ese mismo reporte
SI calza**, con **0 motivos**, que es lo que hace que no sea un rojo
indiscriminado.

**ESTA GUARDA NO SE AFLOJA EN NINGUN CARRIL, NI SIQUIERA EN EL TARDIO**, y por eso
va cableada fuera de la columna que el carril tardio toca.

#### EL ARNES VIEJO, CORRIDO SIN TOCARLO AL TERMINAR LAS TRES REPARACIONES

`scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py`, **sin tocarlo**, sale
**VERDE con sus 9 casos** y **`CIFRA fallos: 0`**
(`docs/loop/SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt`, **5802 bytes en disco y 5802 bytes normalizados a LF**). **No cambio de color.** Y los dos arneses sellados de
la 185 tambien siguen verdes despues de las tres reparaciones, con su `sha256`
intacto.

#### LAS RUTAS DE PRUEBA DE ESTA TAREA, TODAS COMPROBADAS Y NINGUNA DE CERO BYTES

| ruta | bytes en disco, iguales normalizados a LF salvo donde se diga |
|---|---:|
| `docs/loop/SALIDA_V186_T2A_MUTACION_PIEZA4.txt` | **3601** |
| `docs/loop/SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt` | **2607** |
| `docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt` | **5040** |
| `docs/loop/SALIDA_V186_T2C_VEREDICTO_184.txt` | **2322** |
| `docs/loop/SALIDA_V186_T2C_VEREDICTO_184_FRASE.txt` | **356** |
| `docs/loop/SALIDA_V186_T2C_CERRAR_REPORTE_184.txt` | **6128** en disco y **6030** en LF |
| `docs/loop/SALIDA_V186_T2C_ARCHIVAR_184_SIN_FORZAR.txt` | **790** en disco y **780** en LF |
| `docs/loop/SALIDA_V186_T2C_ARCHIVAR_184.txt` | **965** en disco y **948** en LF |
| `docs/loop/SALIDA_V186_T2D_MUTACION_SECCION4.txt` | **5007** |
| `docs/loop/SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt` | **5802** |
| `docs/loop/reportes/REPORTE_V184.md` | **124249** |

<!-- FIN ANEXO DE TAREAS -->

## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LAS DOS TAREAS DEL ENCARGO CERRARON.** El tope era dos, por el regimen temporal
de `AUDITOR.md` 6.2, y son dos. **Y ESTA VUELTA CIERRA SU PROPIO REPORTE: es la
SEGUNDA de las dos seguidas que el regimen pide, y el tope vuelve a CINCO en la
187.**

- rama, leida con `git rev-parse --abbrev-ref HEAD`: `pasada-unica`
- HEAD de apertura, sellado **antes de la primera operacion** en
  `docs/loop/SALIDA_V186_HEAD_APERTURA.txt`: **`620dc837`**
- HEAD del ultimo commit antes de cerrar, leido con `git rev-parse HEAD`
  **despues de la ultima operacion**: **`8c952bb1`**
- commit del acta 186, localizado en el log y no tecleado: **`620dc837`**
- commit de nacimiento del bloque de apertura, `git log --diff-filter=A`:
  **`793ad9a1`**

**GATE 0 VERDE ENTERO EN SU CICLO, EN LA APERTURA Y OTRA VEZ AL CIERRE.** Sus
salidas son `docs/loop/SALIDA_V186_GATE0_CMD1_APERTURA.txt` (**4859 bytes en disco y 4790 bytes normalizados a LF**)
y `docs/loop/SALIDA_V186_GATE0_CMD1_CIERRE.txt` (**4859 bytes en disco y 4790 bytes normalizados a LF**),
con motor **25/25** en la apertura y **25/25** al cierre, `tsc` **EXIT=0** y **EXIT=0**,
y web **82 ficheros y 1040 passed (1040)** en las dos. La apertura entera vive en
`docs/loop/SALIDA_V186_APERTURA.txt` (**27078 bytes en disco y 27078 bytes normalizados a LF**)
y **la sello el PRIMER commit de la vuelta**.

**EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA, ANTES DE LA PRIMERA
OPERACION**, que es donde `EJECUTOR.md` 1 lo manda desde la 178: **4 filas** en la
apertura y **4 filas** al cierre. Sus dos salidas miden **505 bytes en disco y 498 bytes normalizados a LF** cada una.

**EL ARCHIVO DE VEREDICTOS NO SE MOVIO, Y ESA ES LA PRUEBA INDEPENDIENTE DE QUE
ESTA VUELTA NO TOCO NINGUN VEREDICTO.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:
**3388 filas**, **A 551, B 72, C 5, D 2760**, **0 huecos y 0 duplicados**,
**4051967 bytes en disco y 4051967 bytes normalizados a LF**, y `sha256`
**identico por las dos convenciones, disco `ea6e850d331d14f0` y LF `ea6e850d331d14f0`**.
Es el mismo que la apertura de esta vuelta midio y el mismo que las actas 179 a
186 publican. **El plan lleva seis vueltas sin moverse, y esta vuelta tampoco lo
mueve: el acta 186 explica en su seccion 12 por que, y el par 2.464 encabeza la
187.**

## 4. LA GUARDA DEL COMMIT DE `dataset/`, CORRIDA EL DIA QUE SERVIA

**ESTA ES LA PRIMERA SECCION 4 QUE SU PROPIA ESCALADA VIGILA.** La guarda de la
TAREA 2.d lee las dos cifras de `docs/loop/SALIDA_V186_APERTURA.txt` y las coteja
contra lo que esta seccion afirma, cayendo en ROJO si discrepan o si esta seccion
no las afirma. **Las dos que van aqui salen de ese fichero y no de la memoria.**

`git status --porcelain` da **1 linea** en la apertura, medida en el bloque de
apertura antes de la primera operacion, y
`git diff --numstat -- dataset/` da **0 filas** AL ENTRAR.
**Ninguna perdida de catalogo que declarar**, y `dataset/` no se commitea en esta
vuelta.

**LA UNICA LINEA DE ESA APERTURA ERA EL PROPIO FICHERO DEL BLOQUE DE APERTURA,
TODAVIA SIN SEGUIR POR GIT**, y su docstring lo predijo **con esa cifra y no con
cero**, que es justo la leccion de la `R.1` del acta 186: aquella vuelta le
atribuyo al bloque C una medicion que el bloque C contradecia. **Aqui la
prediccion se escribio con el fichero ya contado.**

**LAS MEDICIONES DEL CIERRE NO SE TECLEAN EN ESTA PROSA, Y SE DICE POR QUE.** El
estado del arbol al cerrar es un instante que los commits del cierre consumen, y
la `R.1` y la cifra no verificable de las 15 lineas del reporte de la 185 son la
misma enfermedad. **Lo que el cierre midio vive en sus ficheros sellados**
(`docs/loop/SALIDA_V186_CICLO_NUMSTAT_CIERRE.txt`, **140 bytes en disco y 140 bytes normalizados a LF**),
y el recuento de filas de `dataset/` **volvio a dar 0 al salir**, medido con el
comando entero y no de memoria.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**SON SEIS Y VAN MARCADOS ANTES DE SABER SI ACIERTO.** Los cinco primeros son de
METODO; **el sexto es de CLASE**, que es lo que el encargo pide expresamente
despues de dos vueltas sin ninguno.

- **`D.1`. EL ARNES DE LA `2.a` NO CUENTA LAS LINEAS DE COMENTARIO.** El encargo
  dice *"contando sus apariciones y exigiendo 1"*, y la reparacion deja un
  comentario que NOMBRA la comparacion, asi que el conteo crudo da **2**. Decidi
  que un comentario no es una copia de la regla, **publico las dos cifras** y el
  arnes prueba que sabe contar sobre un texto fabricado. **Se puede leer que la
  letra pedia el conteo crudo y que entonces la reparacion no cumple.**
- **`D.2`. LA GUARDA DE LA `2.d` CAE EN ROJO SI EL FICHERO DE APERTURA NO
  EXISTE**, y eso el encargo no lo dice. Lo escribi asi porque una guarda que se
  calla cuando le falta la vara no sirve, pero **es una regla que nadie escribio**
  y hace imposible cerrar tarde un reporte de una vuelta que no dejo apertura
  sellada.
- **`D.3`. `es_cierre_tardio()` USA LA LETRA EXACTA DEL ENCARGO Y NO LA
  ESTRECHA.** Devuelve verdadero cuando la vuelta en curso **no es** la del
  reporte, asi que una vuelta ANTERIOR tambien abriria el carril. Se puede leer
  que un cierre solo puede ser tardio, nunca adelantado, y que la condicion
  deberia exigir ademas que la vuelta en curso sea la mayor. **No lo estreche
  porque seria doctrina nueva dentro de una guarda.**
- **`D.4`. FORCE EL ARCHIVADO DEL REPORTE DE LA 184 CON LA BANDERA DE FORZAR**,
  pisando el archivo viejo. Comprobe ANTES que el texto viejo sigue entero y byte
  a byte en otra sede, y publique las DOS corridas, pero **el encargo no nombra
  esa bandera** y se puede leer que pisar un archivo pide permiso.
- **`D.5`. LA GUARDA DE LA `2.d` SE CABLEO DESPUES DE CERRAR EL REPORTE DE LA
  184**, que es el orden de las letras del encargo. **Si hubiera corrido antes, el
  reporte de la 184 NO habria cerrado**, porque su seccion 4 no cita las cifras de
  su apertura sellada. Lo digo yo antes de que lo mida nadie.
- **`D.6`. Y ESTE ES DE CLASE, NO DE METODO: EL PUESTO 338.** La relectura al
  doble lo mira con la vara mecanica y **no ve nada** (no declara diferenciador,
  no tiene lesion, no tiene nodo muerto), y su clase de archivo es **`B`**, la
  unica `B` del universo releido. **Yo no la vuelvo a decidir y el encargo me lo
  prohibe**, pero **marco que la vara con la que reviso no puede ver lo que el
  auditor vio ahi**: el archivo lo clasifico por la correspondencia uno a uno de
  los pasos, y ninguna de mis cuatro comprobaciones mecanicas mira eso. **Si
  alguien quiere discutir una clase de esta vuelta, es esta.**

## 6. LAS PREGUNTAS

- **`P.1`. LA `D.1` DE ARRIBA, CONVERTIDA EN PREGUNTA: EL CONTEO DE LA SEGUNDA
  COPIA, CRUDO O SOLO EN CODIGO.** Si la casa quiere el crudo, la reparacion tiene
  que quitar la comparacion del comentario y el arnes se aprieta en una linea.
  **No lo hago yo porque el comentario es lo que explica por que la pieza (4)
  llama en vez de comparar.**
- **`P.2`. LA `D.2` DE ARRIBA: QUE HACE LA GUARDA DE LA `2.d` CUANDO SE CIERRA
  TARDE UN REPORTE SIN APERTURA SELLADA.** Hoy cae en rojo. Las salidas son
  eximirla en el carril tardio, o declarar que ese reporte no se cierra. **Las dos
  son doctrina y ninguna es mia.**
- **`P.3`. ENTRAN EN LA NOMINA LOS CUATRO ARNESES QUE NACEN EN ESTA VUELTA.** Son
  `vuelta186_tarea2a_mutacion_pieza4.py`, `vuelta186_tarea2b_mutacion_pieza2_cercas.py`,
  `vuelta186_tarea2c_mutacion_cierre_tardio.py` y
  `vuelta186_tarea2d_mutacion_seccion4.py`. **Medido al cerrar esta vuelta,
  `arneses_que_faltan()` los devuelve a los cuatro.** El tope de dos sub-tareas no
  me daba sitio para meterlos, igual que le paso a la 185 con los suyos, **y lo
  digo aqui para que la 187 no se entere en la 189**.

## 7. PENDIENTES DE DOCTRINA

- **`PD.1` SIGUE ABIERTA, QUINTA VUELTA.** Las cinco `D` con el diferenciador ya
  presente el dia del veredicto (**1778, 2530, 2540, 3141, 3232**) siguen sin
  pasar el disparador escrito de la cola post fusion. **Esta vuelta no la toca**,
  y sus cinco puestos quedan en el `R.48` leidos del acta.
- **`PD.7` NUEVA: LA MESA DE LOS TRES NODOS DE LA PUERTA DEL `PMF`.** El acta 186
  la ANOTA en su `6.4` y dice expresamente que **no la encarga y no la adjudica**,
  porque es trabajo de plan. **Aqui se registra como pendiente de doctrina para
  que tenga sede**, y esta vuelta no la abre porque su encargo se lo prohibe con
  esas palabras. Los nodos son los de los puestos **338** y **297**.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**UNA CAIDA PROPIA, Y LA LEVANTO YO ANTES DE QUE LA MIDA NADIE.**

**`C.1`. PUBLIQUE CUATRO CIFRAS DE BYTES IGUALANDO LA CONVENCION DE LF A LA DE
DISCO SIN HABERLA MEDIDO.** En la primera escritura de los anexos de las TAREAS 1
y 2 escribi *"N bytes en disco y N normalizados a LF"* para cuatro ficheros cuya
salida se redirigio por la consola y por tanto lleva `CRLF` en disco. **La cifra
de disco era buena; la de LF estaba supuesta, no medida.** Es exactamente la
especie que esta casa persigue: una cifra escrita en vez de leida de un
instrumento.

**COMO SALIO, Y NO POR CASUALIDAD:** el instrumento
`scripts/loop/vuelta186_rutas_del_reporte.py`, escrito en esta misma vuelta para
comprobar que ninguna ruta publicada apunta a un fichero inexistente o de cero
bytes, publica las DOS convenciones de cada ruta, y ahi se vieron las cuatro.

**LO VIEJO NO SE BORRA, QUE ES LA MITAD QUE IMPORTA.** Las cuatro cifras, con lo
que publique y lo que el instrumento mide:

| ruta | lo que publique | lo medido |
|---|---:|---:|
| `docs/loop/SALIDA_V186_COTEJO_DE_CLONES.txt` | 49804 en disco y **49804** en LF | 49804 en disco y **49036** en LF |
| `docs/loop/SALIDA_V186_T2C_CERRAR_REPORTE_184.txt` | 6128 en disco y **6128** en LF | 6128 en disco y **6030** en LF |
| `docs/loop/SALIDA_V186_T2C_ARCHIVAR_184_SIN_FORZAR.txt` | 790 en disco y **790** en LF | 790 en disco y **780** en LF |
| `docs/loop/SALIDA_V186_T2C_ARCHIVAR_184.txt` | 965 en disco y **965** en LF | 965 en disco y **948** en LF |

**QUE ESPECIE ES Y SI ACUMULA, DICHO SIN REGATEAR:** es **caida de cifra
publicada**, y las cuatro viven en TABLAS y en prosa de anexo. **La declaro
entera y no la disfrazo de correccion menor.** Lo que si separo, para no
castigarme de mas ni de menos: **ninguna de las cuatro mueve una decision**, todas
las rutas existen y ninguna mide cero bytes, y la cifra de disco, que es la que la
casa usa para cotejar, era correcta en las cuatro.

**Y LO QUE HAGO CON ELLA:** corrijo las cuatro celdas, **dejo esta tabla con lo
viejo al lado**, y el reporte se **REGENERA desde el esqueleto commiteado** con
`anexar_tarea_al_reporte.py` en vez de retocarse a mano. **El reporte sigue siendo
producto de sus instrumentos.**

**LO DEMAS DE ESTA VUELTA NO TIENE CAIDA PROPIA:** los cuatro arneses nuevos
salieron VERDES en su primera corrida, ningun arnes ya sellado cambio de color, y
el bloque de apertura corrio entero antes de la primera operacion con su
prediccion escrita antes de medir.

**Y ADEMAS DECLARO UNA LIMITACION MEDIDA, QUE NO ES UNA CAIDA:** el bloque de
apertura de esta vuelta contaba los puestos de la ciega con el patron de la
palabra PUESTO en mayusculas, y las ciegas del auditor los escriben con la clave
`puesto_intra`, asi que su bloque H.5 publico **0 puestos** para los cuatro
ficheros que miro. **No movio ninguna decision**, porque la relectura al doble de
la TAREA 1.c usa el patron correcto y leyo sus **30** puestos, pero **la cifra del
H.5 es inutil y se dice en vez de dejarla pasar por buena**.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 186 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V186_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: LA BATERIA DE MUTACIONES NO CORRE EN ESTA VUELTA POR DECISION DEL FUNDADOR DEL 5 SEP 2026, ESCRITA EN AUDITOR.md 6.1: CORRE CADA CINCO VUELTAS, EN UNA VUELTA PROPIA QUE NO LLEVA NADA MAS. CERRO ENTERA EN LA 184 CON SUS NUEVE TRAMOS SELLADOS, ASI QUE LA SIGUIENTE VUELTA DE BATERIA ES LA 189, Y ESTA 186 ES UNA DE LAS CUATRO INTERMEDIAS. NO SE AFLOJA NINGUNA GUARDA Y LA NOMINA NO SE PODA: ESTA VUELTA LA HIZO CRECER DE 113 A 115 EN SU TAREA 1.b.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
