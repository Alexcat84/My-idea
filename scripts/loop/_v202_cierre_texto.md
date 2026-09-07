## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE ESTA SECCION CITA EL FICHERO DEL QUE SALE Y SE RECONSTRUYO
CONTANDO ESE FICHERO ANTES DE PUBLICARLA** (`EJECUTOR.md` 1, LA TABLA SE CUENTA
DE SU FICHERO).

| lo que se mide | cifra de hoy | fichero del que sale |
|---|---|---|
| ficheros `SALIDA_V202_*` en `docs/loop/` | **37**, de ellos **37 vivos** y **0 de cero bytes** | `docs/loop/SALIDA_V202_CIERRE_MEDICIONES.txt` bloque `G` |
| racha de cierres al abrir | **3**, con las vueltas 199, 200 y 201 | `docs/loop/SALIDA_V202_APERTURA.txt` bloque `E` |
| nomina de la bateria, al abrir y al cerrar | **135** y **135**, contra el congelado **135** | bloques `F` del sello y `D` de las mediciones |
| arneses del censo fuera de la nomina | **2** con la vara **148** y **62** sin vara | los mismos dos bloques |
| serie de registros, al abrir y al cerrar | **54** y **56** entradas, **0** y **0** colisiones, **0** y **0** huecos | `SALIDA_V202_SERIE_APERTURA.txt` y `SALIDA_V202_CIERRE_MEDICIONES.txt` bloque `F` |
| siguiente libre, al abrir y al cerrar | **R.63** y **R.65** | los mismos dos ficheros |
| deuda de actas sin entrada propia, 173 a 200 | **6**, las 175 a 180 | `docs/loop/SALIDA_V202_T4_REGISTROS.txt` |
| marcador del cribado, recontado | **3388** filas, **A 551, B 72, C 5 y D 2760**, que suma **3388** | `docs/loop/SALIDA_V202_T2_OP_L_02.txt` bloque `E` |
| puestos del archivo | **3388** distintos, maximo **3388**, **0** huecos | el mismo fichero |
| vara del trabajo pendiente | **71** fichas, **37** que no calzan, **6** en LISTA sin prueba, **4** de trabajo real, **2** consumidas | `docs/loop/SALIDA_V202_VARA_DEL_PLAN.txt` |
| casos de la prueba de mutacion de la guarda de la TAREA 1 | **6 casos**, y **los 6 pasan** | `docs/loop/SALIDA_V202_T1_MUTACION_GUARDA.txt` |
| ficheros con reporte archivado ausente, rango 168 a 199 | **2**, la **173** y la **198** | `docs/loop/SALIDA_V202_APERTURA.txt` bloque `H.2` |

**LAS CIFRAS DEL PLAN QUE ESTA VUELTA MIDIO Y NADIE HABIA MEDIDO, todas con
fecha de corte 2026-09-07:**

| medicion | cifra | donde |
|---|---|---|
| `LECTURAS_DIRIGIDAS.md`, apariciones de `reparto por acto` y de `OP-L-03` | **0** y **0**, con **8** variantes de busqueda positiva en cero | `SALIDA_V202_T1_CORRECCION_OP_L_03.txt` |
| cobertura real de `OP-L-03` contra su promesa de **55 pares en 29 actos** | **14** actos con ficha, **11** con `leido` en true, **19** pares leidos | el mismo fichero |
| `OP-L-02`, clausulas cumplidas | **2 de 3** segun el instrumento, **3 de 3** con la clausula 2 remedida | `SALIDA_V202_T2_OP_L_02.txt` |
| `OP-L-01`, cifras de la corrida vieja contra la de hoy | **7** cotejadas y **3** que discrepan | `SALIDA_V202_T3_OP_L_01.txt` |
| TABLA VIVA DE LOS PUROS al corte 3388 | **11** filas: **6** en pie, **0** caidas y **5** no medibles; **4** citan un puesto por encima de su vigencia | el mismo fichero |

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO EN ESTA PROSA.**
`docs/loop/SALIDA_V202_APERTURA.txt`, bloque `C`, publica las dos cifras del
estado del arbol con la redaccion exacta que la guarda coteja, y aqui se repiten
LEIDAS de ella:

`git status --porcelain` 3 lineas al entrar, que eran el propio bloque de
apertura y sus dos piezas de generacion, todavia sin commitear.

`git diff --numstat -- dataset/` 0 filas al entrar.

**La apertura sellada no se toco al cierre ni una vez.**

**LO QUE SE TOCO:**

- `docs/plan/OPERACIONES.jsonl`: **un elemento mas** en la `evidencia` de
  `OP-L-03`, en su linea **43**. **1 linea anadida y 1 borrada**, que es lo que un
  `jsonl` da siempre al reescribir una linea, y es **la unica escritura de esta
  vuelta en `docs/plan/`**. Va con su guarda medida contra `HEAD` y corrida dos
  veces.
- `docs/PENDIENTES.md`: las entradas **`R.63`** (acta 173) y **`R.64`** (acta
  174), anadidas al final. **188 lineas anadidas y 0 borradas**, contadas con
  `git diff --numstat` contra el HEAD de apertura.
- `docs/loop/reportes/REPORTE_V201.md`: el reporte de la 201 **archivado byte a
  byte** antes de pisarlo, **745 lineas anadidas y 0 borradas**.
- `scripts/loop/`: el bloque de apertura, el esqueleto, el bloque de cierre y el
  registrador de la TAREA 4 (los cuatro **clones declarados**, y tres de ellos
  generados programaticamente para que su codigo vaya byte a byte), **seis
  computos de un solo uso con prefijo de guion bajo**, **cuatro moldes de
  generacion** y **cuatro cuerpos de tarea**.
- `docs/loop/`: las salidas selladas de esta vuelta y el reporte.

**LO QUE NO SE TOCO, Y SE MIDE EN VEZ DE PROMETERSE:**

- **`dataset/` no se toco a mano.** El `numstat` contra `HEAD` sale con **0
  filas** al entrar y **0 al salir**, medido en
  `SALIDA_V202_CICLO_NUMSTAT_APERTURA.txt` y en
  `SALIDA_V202_CICLO_NUMSTAT_CIERRE.txt`, y **contra el HEAD de apertura tambien
  sale en 0 filas**, medido en `SALIDA_V202_CIERRE_MEDICIONES.txt` bloque `C`.
- **`web/` y `engine/` en cero filas de `numstat`** por las dos varas, la de
  `HEAD` y la del HEAD de apertura `ebe04895`, leido de su sello y no tecleado.
- **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se movio.** **4054129 bytes en disco y 4054129 bytes normalizados a LF**, con `sha256` `0a77b5a35a962621` de disco y `0a77b5a35a962621` de LF, **al entrar y al salir**. **Ninguna clase y ningun
  veredicto se mueven, porque mover una clase es del RECOMPUTO.**
- **NINGUN CAMPO `estado` SE MOVIO**, y no se afirma: se mide contra `HEAD` en
  `SALIDA_V202_T1_GUARDA_ESTADO.txt` y en su gemela `_IDEM`, que salen **VERDE**
  las dos con **0 de 71 fichas** cambiando su `estado`. La vara del trabajo
  pendiente es el instrumento, nunca el campo (recuadro de `AUDITOR.md` 0).
- **La nomina no crecio ni se podo**: **135** al entrar y **135** al salir, con
  `CASOS_DECLARADOS` en **2** y el censo en **197** las dos veces. **Los dos
  arneses que quedan fuera con la vara 148 siguen fuera**, y son
  `vuelta197_tarea2_mutacion_orden_del_turno.py` y
  `vuelta199_tarea1_mutacion_guardas_revividas.py`.
- **NINGUN INSTRUMENTO AJENO SE TOCO NI SE CLONO.** Los cuatro que esta vuelta
  necesitaba se **importaron y se corrieron tal cual**: los dos de `OP-L-02` y los
  dos de `OP-L-01`. **El `sha256` de `docs/plan/OPERACIONES.jsonl` vale
  `6006fd16dc08dc58` antes y despues** de las dos corridas de la TAREA 3, que
  corrieron **en modo medicion y sin `--aplicar`**.
- **`AUDITOR.md`, `EJECUTOR.md` y `docs/BANCO_DE_TEXTOS.md` no se tocaron.** El
  hueco de la vigencia de la TABLA VIVA **se nombra y se mide, y no se corrige**:
  actualizar esa cabecera es tocar el banco y no lo decide el ejecutor.
- **`OP-L-01`, `OP-L-02` y `OP-L-03` se LEYERON y no se cerraron:** las tres
  entran y salen en `LISTA` y **ninguna ficha se cerro por cuenta del ejecutor**.
- **Las dos paradas que la 200 levanto y las que el acta 201 adjudico no se
  volvieron a levantar.**

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` LA CLAUSULA 2 DE `OP-L-02`, DADA POR CUMPLIDA CONTRA UNA VARA DISTINTA DE
LA DEL INSTRUMENTO.** El instrumento la da **NO CUMPLIDA** porque diffea contra
`46208790`, un HEAD de la vuelta 170; remedida contra el HEAD de apertura de esta
vuelta sale **CUMPLIDA**. Sostengo que la segunda lectura es la correcta **porque
la clausula pide que la OPERACION no mueva el archivo y la operacion es esta
vuelta**, y el acta 201 ya llamo falso rojo al otro en su `4.2`. **Pero quien
decida que una clausula no se puede dar por cumplida contra una vara distinta de
la que el instrumento usa tendra un argumento, y no lo cierro yo.**

**`D.2` LA DISCREPANCIA DE `las_once()` NO TUMBA LA CLAUSULA 1 DE `OP-L-01`.** El
universo del instrumento paso de **11** a **27** cabeceras `LD` y su comparacion
resuelta de **3** a **11**. Sostengo que **la clausula sigue cumplida** porque en
comparacion **LITERAL** siguen apareciendo **0**, que es lo que la clausula
pregunta, y lo que envejecio es **la cifra de la excepcion nombrada**. **Quien
sostenga que una excepcion mal contada si tumba la clausula tendra un argumento.**

**`D.3` ESCRIBI `R.63` Y `R.64` AUNQUE SU REPARTO NO SE PUDIERA COMPUTAR.**
Podia no escribirlas y traer solo la parada. Elegi **pagar la deuda con todo lo
medible y nombrar en voz alta lo que no pude medir**. **Quien prefiera que una
entrada sin reparto no se escriba tendra un argumento, y no lo cierro yo.**

**`D.4` LA VARA DEL HUECO DE LA VIGENCIA MIDE PRESENCIA Y NO CALIDAD.** La escribi
**antes de correrla**, en una constante del propio fichero, y con ella **5 de las
11 filas salen NO MEDIBLES**. Una vara mas ancha, de numerales sueltos, mediria
mas filas **y confundiria el ano 2026 con el puesto 2026**, que es justo lo que la
salida muestra. **Sostengo que es mejor medir menos y bien; quien prefiera una
vara mas ancha con sus falsos positivos declarados tendra un argumento.**

**`D.5` LOS CUATRO CLONES DE ESTA VUELTA SON MAQUINARIA O NO LO SON.** El bloque
de apertura, el esqueleto, el bloque de cierre y el registrador de la TAREA 4 son
**instancias de un computo ordenado**, y la adjudicacion `4.5` del acta 199 dice
que eso **no es maquinaria**. **Sostengo que la moratoria no los prohibe porque
sin ellos no hay vuelta; quien lea la moratoria mas estrecha tendra un argumento.**

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` LA VIGENCIA DE LA TABLA VIVA DE LOS PUROS DICE `1157` Y SUS PROPIAS
CELDAS LA DESMIENTEN.** **4 de sus 11 filas** citan un puesto por encima de esa
vigencia, y el marcador de hoy vale **3388**, **2231 puestos mas alla**.
**Actualizar esa cabecera es tocar `docs/BANCO_DE_TEXTOS.md`, y no se hace sin
decirlo. Que se hace con ella.**

**`P.2` LA CORRECCION DE LA `verificacion` DE `OP-L-01` ESTA MEDIDA Y NO
ESCRITA.** Es la misma especie que `OP-I-01` en la 201 y `OP-L-03` en esta vuelta,
y va **por el carril del banco `9.10` y por adicion**. **El encargo de la TAREA 3
decia PROPON, NO CIERRES, asi que no la escribi. Se adjudica o no.**

**`P.3` `OP-L-02` QUEDA EN 3 DE 3 CON LA CLAUSULA 2 REMEDIDA.** **No la cerre y no
movi su `estado`.** La propuesta va con su evidencia entera en la TAREA 2. **Se
adjudica o no.**

**`P.4` EL REPARTO DE LAS ACTAS ANTERIORES A LA 184 NO SE PUEDE COMPUTAR CON LOS
LECTORES DE HOY.** Quedan **6 actas de la deuda** y **todas son de esa
convencion**: las **175 a 180**. **O se autoriza un lector para la convencion
vieja, y eso es codigo bajo moratoria, o se decide que seccion cuenta como cada
numeral, y eso es una decision. Las dos me estan cerradas.**

## 7. PENDIENTES DE DOCTRINA

**Ninguno nuevo en esta vuelta.** Todo lo que esta vuelta midio se resolvio con
doctrina ya escrita: el banco `9.10` para las correcciones por adicion, el `9.21`
para las cifras con su corte, `P.1` para el resolutor, `P.2` para los bytes
exactos, `AUDITOR.md` 0 para el campo `estado`, `AUDITOR.md` 3 para la parada, y
`AUDITOR.md` 6.1, 6.2 y 6.3 para la cadencia, el tope y la moratoria.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE

**Las tres se cazaron ANTES de publicarse y las tres van escritas con el texto
viejo entero, que es lo que `EJECUTOR.md` 8 manda: una correccion que tapa lo que
corrige no se puede auditar.**

**`C.1`. MI RECUENTO DEL MARCADOR BUSCABA UNA CLAVE QUE NO EXISTE.** En
`scripts/loop/_v202_t2_op_l_02.py` miraba la clave `puesto` de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y publicaba **0 puestos distintos**. La
clave de ese archivo se llama **`puesto_intra`**: el **0** no era una medicion,
era **el sintoma de mirar donde no hay nada**. Contado bien son **3388 puestos
distintos, maximo 3388 y 0 huecos**. **La correccion queda escrita dentro del
fichero y no solo aqui.**

**`C.2`. MI EXTRACTOR DE FILAS DE LA TABLA VIVA COGIA CINCO TABLAS EN VEZ DE
UNA.** En `scripts/loop/_v202_t3_op_l_01.py` tomaba **toda** linea de tabla
posterior a la cabecera de la linea 938 y sacaba **32 filas**, que eran las de la
TABLA VIVA **mas las de otras tablas de mas abajo del banco** (lineas 1056, 1674,
2024 y 2591 entre otras). Con el extractor malo el reparto salia **9 en pie, 0
caidas y 23 no medibles**; acotado al bloque contiguo, la tabla tiene **11 filas**
y el reparto real es **6, 0 y 5**. **La cifra mala no se borra: va escrita dentro
del fichero y en la seccion de la TAREA 3.**

**`C.3`. ESCRIBI DOS CIFRAS DE BYTES SIN HABERLAS CONTADO.** En el cuerpo de la
TAREA 3 publique las selladas de los dos instrumentos como **32752** y **3971**
bytes normalizados a LF. Contadas, miden **32684** y **3963**. **Se corrigieron
contando los ficheros antes de anexar la tarea**, asi que la cifra mala **no llego
al reporte**, pero **la escribi**, y eso es una caida de cifra igual: la unica
diferencia es que la caze yo.

**Y UNA QUE NO CUENTO COMO CAIDA DE CIFRA, DICHA PARA NO ESCONDERLA:**
`scripts/loop/_v202_t3_op_l_01.py` **se cayo con un error de formato** en su
primera corrida, un `%` sin su hueco. **No publico ninguna cifra falsa porque no
publico nada**, y por eso no lleva numero de caida; queda dicho porque un
instrumento que revienta y se arregla en silencio tambien envejece mal.

**Y UNA CORRECCION MAS, DECLARADA, QUE NO ES CAIDA DE CIFRA SINO DE FORMA, Y QUE
NO CAZE YO SINO UNA GUARDA DE LA CASA:** al cerrar este reporte,
`scripts/loop/cerrar_reporte.py` lo **reprobo DOS VECES antes de dejarme
cerrar**. **La primera, con 12 cifras publicadas sin su pareja**: las 12 cifras
eran correctas, y lo que fallaba es que **el markdown parte la frase donde le cabe
el ancho** y dejaba el numero solo en su renglon, sin la segunda convencion al
lado. **La segunda, con 2 parejas que estaban COMPLETAS y eran FALSAS**: la frase
publicaba, **pegado a la ruta, el tamano de ANTES**, y la guarda lo leia como el
tamano de esa ruta, **con razon**, porque lo que va detras de una ruta es el
tamano de esa ruta. **Las dos veces se arreglo JUNTANDO la cifra con su pareja o
poniendo detras de cada ruta SU tamano medido, y NUNCA quitando una cifra**, con
`scripts/loop/_v202_juntar_parejas.py`, que lleva **13 arreglos declarados** y los
aplica **igual en el reporte y en las fuentes de las que salio**, para que las dos
sedes no se separen. **Es la misma especie que tumbo el cierre de la 201 dos
veces, y el remedio es el mismo que aquella dejo escrito.**
