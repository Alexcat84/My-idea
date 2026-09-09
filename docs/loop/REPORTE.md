# REPORTE DE LA VUELTA 213 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v213_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO EN LA 209, LA 210, LA
> 211 Y LA 212.** No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**,
> que es el instrumento que las lee, y se comprueba ANTES de tallar que es lo que
> ese instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **DOS TAREAS, Y LA 213 NO ES VUELTA DE BATERIA.** La cadencia de cinco de
> `AUDITOR.md` 6.1 pone la siguiente bateria en la **215**, y esta vuelta no la
> corre. **El tope de sub-tareas volvio a CINCO** (adjudicacion `6.8` del acta
> 212) y el encargo trae dos igualmente, **no por el tope, sino porque es lo que
> queda del plan**.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado. Todo lo que esta vuelta escribe en
> `scripts/loop/` son ficheros `_v213_*` **con prefijo de guion bajo, fuera del
> censo y fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda.
>
> **RIGE LA OBLIGACION DE DICTADO DEL `6.6` DEL ACTA 210:** toda cita de un acta
> anterior lleva **LA LINEA** de `docs/loop/ACTA_AUDITOR.md` donde vive el texto
> citado, **y la linea se LEE, no se recuerda**.
>
> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado
> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.
>
> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO NUEVAS DEL ACTA 212, LAS TRES SIN
> CODIGO:** ningun reporte cita un directorio a secas como ruta entre comillas
> inversas (adjudicacion `6.2`); una seccion suplementaria va detras de la que
> amplia y nunca detras de una mayor (hallazgo `7.1`); y el tallador de cabecera
> corrido en la apertura escribe en un nombre con `_RECHAZO`, no en el del cierre
> (`C.1` del reporte 212, adoptada como obligacion).
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V213_APERTURA.txt`,
> `docs/loop/SALIDA_V213_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 213`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y EL BARRIDO DEL `9.10`: leer el acta que cubre la 212 desde su linea de apertura y registrar por linea leida hoy sus adjudicaciones `6.1` a `6.7` y su `4.1`, mas las CUATRO cosas que suben al fundador y cual de ellas bloquea el cierre de la campaña; y ejecutar la `P.1` adjudicada, que es UNA sola linea: `docs/plan/03_FUSIONES.md` 5424 se corrige por el carril del banco `9.10`, correccion DECLARADA con el texto viejo entero encima y sin tachar, citando la vuelta y el commit del volteo del `730`, mientras `docs/INTRA_DOMINIO_INFORME.md` 6941 NO SE TOCA. Con simulacion previa, caso rojo por mutacion antes de escribir, sede por las dos convenciones y el `sha256` del archivo de veredictos quieto | **CERRADA, LAS DOS MITADES** | `SALIDA_V213_T1B_BARRIDO_9_10.txt`, y las lineas del acta leidas por `_v213_t1_seccion.py` |
| **TAREA 2** | EL CIERRE DE LA FASE III, MEDIDO: un inventario de las 71 fichas LEIDO DEL REPO Y NO DEL CAMPO `estado`, con la vara `vuelta150_3_relectura_expediente.py` corrida en esta vuelta como fuente y el campo publicado al lado como contraste; una fila por ficha, las cuatro cifras contadas de la tabla, y la cuarta con la cautela de la `6.8` del acta 211 pegada. Mas la `2.b`, la unica que queda abierta (`OP-I-01`), con sus cuatro puntos de `verificacion` pegados enteros, el que esta en `NO CUBRE` aparte, el recuento propio de las entradas del inventario con cobertura incompleta y la frase de que decide el fundador. NO se escribe en `OPERACIONES.jsonl`, NO se marca el inventario, NO se toca `08_VERIFICACION.md` | **CERRADA, CON LA 2.b DENTRO** | `SALIDA_V213_T2_VARA.txt`, `SALIDA_V213_T2_CIERRE_FASE_III.txt`, `SALIDA_V213_T2_RECUENTO_95.txt`, `SALIDA_V213_T2_NUMSTAT.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### `1.a` LOS REGISTROS: EL ACTA QUE CUBRE LA 212, LEIDA DESDE SU LINEA

El acta abre en la linea **74821** de `docs/loop/ACTA_AUDITOR.md`, que es donde el encargo dice que abre, y de ahi la lei entera. **Rige la obligacion de dictado del `6.6` del acta 210** (linea **74203**): toda cita lleva LA LINEA, y **la linea se LEE, no se recuerda**. Las de abajo las lee este compositor con `linea_de()` en esta corrida.

**LAS CITAS DE ACTA DE ESTE REPORTE, LEIDAS UNA A UNA DE SU LINEA.** **FILAS ARMADAS LEYENDO `docs/loop/ACTA_AUDITOR.md` linea a linea: 14; FILAS QUE DEBERIA HABER: 14.**

| linea de `ACTA_AUDITOR.md` | que es | el texto que vive ahi, leido hoy |
|---|---|---|
| **74821** | la apertura del acta que cubre la 212 | # ACTA DEL AUDITOR, VUELTA 212 (8 sep 2026, auditor Opus 5) |
| **74203** | la obligacion de dictado del `6.6` del acta 210, que sigue rigiendo | **`6.6` LA FAMILIA DE LA CITA MAL ATRIBUIDA GANA SU REMEDIO DE DICTADO, Y NO ES |
| **75082** | la `6.1`, la `P.1` adjudicada: es lo que ejecuto en la `1.b` | **`6.1` LA `P.1` SE ADJUDICA: EL BARRIDO DEL `9.10` SE DEBE, ES UNA SOLA LINEA, Y NO ES |
| **75112** | la `6.2`, la `P.2` contestada: el crash ESPERA | **`6.2` LA `P.2` SE CONTESTA: EL CRASH DEL INSTRUMENTO DE RUTAS **NO** ENTRA POR LA PUERTA |
| **75128** | la mitad de la `6.2` que si se pone hoy, y es obligacion de dictado | **LA MITAD QUE NO CUESTA CODIGO SI SE PONE, Y ES OBLIGACION DE DICTADO DESDE HOY: |
| **75133** | la `6.3`, mi `D.1` resuelta, y la marca se me paga | **`6.3` LA `D.1` SE RESUELVE CON LA `6.1` Y EL EJECUTOR ACERTO EN NO TOCARLAS SOLO.** Marco |
| **75138** | la `6.4`, mi `D.2`: el `474` NO SE MUEVE | **`6.4` LA `D.2` SE ADJUDICA Y EL `474` NO SE MUEVE.** Lei sus dos anclas del banco |
| **75145** | la `6.5`, mi `D.3`: tenia razon, y queda contra el acta 211 | **`6.5` LA `D.3` SE ADJUDICA A FAVOR DEL EJECUTOR, Y ES CONTRA MI PROPIA CASA.** |
| **75156** | la `6.6`, mi `D.4` y mi `PD.2`, cerradas sin doctrina nueva | **`6.6` LA `D.4`, LA `PD.2` Y EL VERBATIM DENTRO DE CERCA: SE ADMITE LO QUE HIZO Y NO SE |
| **75164** | la `6.7`, mi `PD.1`, cerrada con la `6.1` | **`6.7` LA `PD.1` SE CIERRA CON LA `6.1`.** Lo que el ejecutor no encontraba escrito **es |
| **75168** | la `6.8`, el tope de sub-tareas vuelve a CINCO | **`6.8` EL TOPE DE SUB-TAREAS VUELVE A CINCO, Y LO MIDO EN DISCO Y EN GIT.** `AUDITOR.md` |
| **75009** | la `4.1`, mi `C.1`: se acepta la declaracion | **`4.1` (`C.1` SUYA). EL FICHERO `SALIDA_V212_TALLADOR_CABECERA.txt` LLEVO UN RECHAZO |
| **75028** | la linea de la `4.1` que adopta mi remedio como obligacion | **LO REGISTRO IGUAL Y ADOPTO SU REMEDIO COMO OBLIGACION**, porque el nombre de un fichero |
| **75188** | la `7.1`, el punto ciego de `secciones_fuera_de_orden()` | **`7.1` `secciones_fuera_de_orden()` NO PUEDE VER UNA CABECERA `## N BIS.`, Y ESTE REPORTE |

**LOS SIETE REGISTROS QUE EL ENCARGO PIDE, UNO A UNO Y CON LO QUE HAGO CON CADA UNO.** Ninguno se ejecuta salvo la `6.1`, que es la `1.b`.

**LOS REGISTROS DEL ENCARGO.** **FILAS ARMADAS LEYENDO `docs/loop/ACTA_AUDITOR.md`: 7; FILAS QUE DEBERIA HABER: 7.**

| adjudicacion | su linea | que dice, resumido de la linea leida hoy | que hago con ella |
|---|---|---|---|
| **`6.1`** | **75082** | LA `P.1` SE ADJUDICA: el barrido del `9.10` se debe, es UNA sola linea y no es doctrina nueva. De las dos citas vivas del 730, la del informe NO se toca y la de `03_FUSIONES.md` SE CORRIGE | **EJECUTADA en mi `1.b`** |
| **`6.2`** | **75112** | LA `P.2` SE CONTESTA: el crash de `vuelta186_rutas_del_reporte.py` NO entra por la puerta de la caida de dato y **ESPERA**, porque `cerrar_reporte.py` no importa `main()` sino `medir_en_disco()` (su linea **154**), que usa `os.path.isfile` | **REGISTRADA. No reparo nada** (moratoria). **La obligacion de dictado va puesta**: este reporte no cita ningun directorio a secas entre comillas inversas |
| **`6.3`** | **75133** | MI `D.1` SE RESUELVE CON LA `6.1`, y acerte en no tocarlas solo. **Estaba equivocado en una de las dos mitades y la marca es lo que permitio verlo** | **REGISTRADA. La marca se me paga** y la conducta se repite: en esta vuelta vuelvo a marcar lo que no se |
| **`6.4`** | **75138** | MI `D.2`, el `474`, **NO SE MUEVE**, y mi decision de no moverlo es correcta como decision, no solo como marca | **REGISTRADA. No lo toco.** No hay cola de re-cribado abierta en esta vuelta |
| **`6.5`** | **75145** | MI `D.3` se adjudica a mi favor: mis nueve cifras de cerco reproducen al digito y las dos del acta 211 no. **Queda registrada contra el acta 211, no contra mi** | **REGISTRADA. No recomputo el cerco otra vez**: el encargo no lo pide y el cerco esta cerrado |
| **`6.6` y `6.7`** | **75156** y **75164** | MI `D.4`, mi `PD.1` y mi `PD.2` se cierran **sin doctrina nueva**. Pegar la razon entera era lo que el encargo pedia; el alcance del `9.10` fuera de las tablas queda adjudicado por extension citable | **REGISTRADAS. Ninguna abre trabajo.** La `PD.1` deja de estar pendiente |
| **`4.1`** | **75009** | MI `C.1` se acepta y **NO ACUMULA**, por dos motivos medidos: la letra del 5 sep define la especie como ruta a fichero inexistente o de cero bytes, y el mio media **1603** bytes; y **ninguna sede publicaba esa ruta**. Me acuse de mas de lo que los hechos sostienen | **REGISTRADA. Mi remedio se adopta como obligacion y lo cumplo en esta misma vuelta**: el tallador de apertura escribio en `SALIDA_V213_TALLADOR_RECHAZO.txt` |

**LAS CUATRO COSAS QUE SUBEN AL FUNDADOR, REGISTRADAS SIN EJECUTARLAS.** Estan en la seccion **8** del acta (abre en la linea **75223**).

**LO QUE SUBE AL FUNDADOR, LEIDO DE SU LINEA.** **FILAS ARMADAS LEYENDO `docs/loop/ACTA_AUDITOR.md` seccion 8: 4; FILAS QUE DEBERIA HABER: 4.**

| punto | linea | su primera linea, leida hoy | bloquea el cierre |
|---|---|---|---|
| **1** | **75225** | 1. **EL PLAN ESTA AGOTADO SALVO UNA FICHA, Y ESA UNA NO LA PUEDE CERRAR EL BUCLE.** La | **ESTA ES LA QUE BLOQUEA EL CIERRE DE LA CAMPAÑA** |
| **2** | **75232** | 2. **LA COLA DE LA AUDITORIA INTEGRAL SUBE A VEINTIOCHO ENTRADAS NOMBRADAS:** las | no bloquea: es cola de la integral |
| **3** | **75238** | 3. **EL MARCADOR SE MOVIO POR PRIMERA VEZ DESDE LA 208, Y ES CIFRA PUBLICADA:** de **A 551 | no bloquea: es aviso de cifra publicada |
| **4** | **75242** | 4. **DOS AUDITORES SEGUIDOS HAN ROTO LA MISMA LETRA DE APERTURA CON EL REMEDIO DE CODIGO | no bloquea: es del regimen del auditor |

**LO DIGO EN VOZ ALTA, QUE ES LO QUE EL ENCARGO PIDE: LA QUE BLOQUEA EL CIERRE DE LA CAMPAÑA ES LA PRIMERA.** `OP-I-01` esta abierta, tiene un punto en `NO CUBRE`, y **lo que ese punto necesita no lo puede dar el bucle**: marcar las entradas del inventario y anadir filas a `docs/plan/08_VERIFICACION.md` es del fundador por las adjudicaciones `6.3` y `6.4` del acta 211. **Mientras eso no se decida, la FASE III no se declara consumida y `PARA_ALEXIS.md` no se escribe.** Las otras tres son reales y ninguna es puerta: la 2 es cola de la integral, la 3 es un aviso de cifra publicada y la 4 es del regimen del auditor.

### `1.b` EL BARRIDO DEL `9.10`: UNA LINEA CORREGIDA, Y LA OTRA CITA INTACTA

**LA MEDICION ENTERA VIVE EN `docs/loop/SALIDA_V213_T1B_BARRIDO_9_10.txt`**, y de ahi sale cada cifra de aqui abajo. El orden fue el de la casa: sede, lectura del disco, composicion en memoria, juicio, **caso rojo por mutacion ANTES de escribir**, y solo entonces la escritura.

#### 1. LO QUE LEI DEL DISCO ANTES DE TOCAR NADA, Y UNA DISCREPANCIA QUE DECLARO

**LAS TRES LINEAS EN JUEGO, LEIDAS DEL DISCO EN ESTA VUELTA.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T1B_BARRIDO_9_10.txt`: 3; FILAS QUE DEBERIA HABER: 3.**

| cual | lo que dice, leido hoy |
|---|---|
| linea **5424** de `docs/plan/03_FUSIONES.md`, leida hoy | > puesto **730** declara que la clase queda en `A` **por la lectura vieja del cero-enlazados** y que |
| linea **5425**, leida hoy | > **si mandara el contenido seria `D`**, y lo deja anotado en vez de elegir. |
| linea **6941** de `docs/INTRA_DOMINIO_INFORME.md`, leida hoy y **NO TOCADA** | **El puesto 730** es el primer veredicto nuevo emitido **despues** de que el |

**DECLARO UNA DISCREPANCIA EN VEZ DE RESOLVERLA COPIANDO** (`EJECUTOR.md` 2). El encargo y la `6.1` del acta citan **la linea 5424**. Leidas del disco, la **5424** lleva la primera mitad de la frase (*la clase queda en `A` por la lectura vieja*) y **la clausula que envejecio vive en la 5425** (*y lo deja anotado en vez de elegir*). **Es UNA sola frase que arranca en la 5424 y cierra en la 5425**, asi que la cita del acta apunta bien a la frase y no a la linea exacta de la clausula. **La correccion entra pegada a la 5425**, que es donde acaba lo que se corrige, y la guarda `(3)` del juicio lo exige por numero: si la insercion entrara en otro sitio, cae.

#### 2. EL VOLTEO QUE LA CORRECCION CITA, MEDIDO EN GIT Y EN EL ARCHIVO

**EL PASO DE `A` A `D`, LEIDO Y NO RECORDADO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T1B_BARRIDO_9_10.txt`: 4; FILAS QUE DEBERIA HABER: 4.**

| que se midio | lo que dice el instrumento |
|---|---|
| commit que toco `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` por ultima vez | 9140d524 (2026-09-08 03:25:53 -0400) |
| clase del puesto **730** en el padre de ese commit | A |
| clase del puesto **730** en el disco de hoy | D |
| los dos nodos del puesto | colaboracion_cadena_suministro -> efecto_bullwhip |

**LA CITA DE LA CORRECCION NO ES UN RECUERDO: ES ESTA MEDICION.** El bloque escrito nombra la **vuelta 212** y el commit **`9140d524`**, y la guarda `(8)` del juicio compara ese literal contra lo que devuelve `git log` en esta corrida.

#### 3. LAS GUARDAS OBLIGATORIAS, TODAS DE SU FICHERO DE SALIDA

**LAS GUARDAS DE LA `1.b`.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T1B_BARRIDO_9_10.txt`: 12; FILAS QUE DEBERIA HABER: 12.**

| guarda | lo que dice el instrumento |
|---|---|
| **simulacion en memoria antes de tocar el disco** | **0 fallos** |
| lineas anadidas y lineas quitadas | CIFRA lineas anadidas: 23 \| CIFRA lineas quitadas: 0 |
| **caso rojo por mutacion, corrido ANTES de escribir** | **CIFRA mutantes: 4 \| CIFRA mutantes que caen: 4 (se exigen todos)** |
| sede de `docs/plan/03_FUSIONES.md` **al entrar**, por las dos convenciones | 831759 bytes en disco y 826733 bytes normalizado a LF (NO COINCIDEN), sha256 disco 41f72d59d1b5dc7b y sha256 LF 515fd9ff9541ae8a |
| sede de `docs/plan/03_FUSIONES.md` **al salir**, por las dos convenciones | 833308 bytes en disco y 828282 bytes normalizado a LF (NO COINCIDEN), sha256 disco f06d25b41c587316 y sha256 LF 46c592fa8da942e2 |
| **el `sha256` del fichero corregido CAMBIA** | **515fd9ff9541ae8a -> 46c592fa8da942e2 (SI, como se exige)** |
| **el `sha256` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO se mueve** | **758edf1f5c313c18 -> 758edf1f5c313c18 (QUIETO, como se exige)** |
| **el `sha256` de `docs/INTRA_DOMINIO_INFORME.md` NO se mueve** (la 6941 intacta) | **c05b6bcd20188a9c -> c05b6bcd20188a9c (QUIETO, como se exige)** |
| `git diff HEAD --numstat` acotado a ese fichero | CIFRA filas de numstat de ese fichero           : 1, y la fila es `23  0  docs/plan/03_FUSIONES.md` |
| `git diff HEAD --numstat` sobre el arbol del plan entero | CIFRA filas de numstat de docs/plan entero      : 1 |
| `git diff HEAD --numstat` sobre dataset, web y engine | CIFRA filas de numstat de dataset, web y engine : 0 |
| relectura del disco identica a lo juzgado | SI |


**LOS CUATRO MUTANTES, UNO A UNO, Y LOS CUATRO CAEN.** El encargo exige al menos tres especies y estan las tres, mas una cuarta.

**EL CASO ROJO POR MUTACION, CORRIDO ANTES DE ESCRIBIR.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T1B_BARRIDO_9_10.txt`: 4; FILAS QUE DEBERIA HABER: 4.**

| el mutante y su veredicto, tal como sale del instrumento |
|---|
| MUTANTE A: TAPA EL TEXTO VIEJO (se come tres lineas de la frase)       -> CAE (2 fallo(s)) |
| MUTANTE B: TOCA UNA SEGUNDA LINEA DEL FICHERO ademas de insertar       -> CAE (1 fallo(s)) |
| MUTANTE C: ESCRIBE UNA CITA QUE NO CALZA (commit inventado)            -> CAE (1 fallo(s)) |
| MUTANTE D: AFIRMA UN PASO QUE EL ARCHIVO NO SOSTIENE (clase de hoy fingida en A) -> CAE (1 fallo(s)) |

**LA GUARDA NO ES UNA CONSTANTE Y ESO ES LO QUE PRUEBAN LOS CUATRO:** la misma funcion `juzgar()` que devuelve **0 fallos** sobre la composicion buena devuelve fallos sobre las cuatro mutaciones. **Y una de ellas se me cayo de verdad en la primera corrida**: la guarda `(6)` exigia la vuelta citada y mi bloque la escribia en mayusculas, asi que la simulacion salio en **1 fallo** y **no escribio**. Corregi la guarda para que compare sin distinguir mayusculas y volvi a correr. **Lo digo porque una guarda que solo se ve pasar no prueba nada.**

#### 4. LO QUE NO TOQUE, Y ES LA MITAD DEL ENCARGO

**LAS CUATRO PROHIBICIONES EXPRESAS DE LA `1.b`.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T1B_BARRIDO_9_10.txt`: 4; FILAS QUE DEBERIA HABER: 4.**

| que estaba prohibido | que paso |
|---|---|
| `docs/INTRA_DOMINIO_INFORME.md` linea **6941** | **INTACTA.** Su `sha256` es el mismo al entrar y al salir, y el fichero no se abre para escritura en ningun camino del instrumento |
| los reportes archivados | **NINGUNO TOCADO.** El numstat del arbol del plan mide **1** fila y es `docs/plan/03_FUSIONES.md`; los archivados viven en otro sitio y no aparecen |
| la clase o la razon de cualquier fila del archivo | **NINGUNA.** El `sha256` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se movio en toda la TAREA 1, publicado al entrar y al salir |
| un barrido general de citas de otros veredictos | **NO SE ABRIO.** No corri ninguna busqueda de citas de otros puestos, asi que **no afirmo que no las haya**: una busqueda que no se hizo no se puede citar (`EJECUTOR.md` 9). Lo que si digo es que **no me tropece con ninguna** leyendo las tres lineas de esta tarea |


**UN DISCUTIBLE MARCADO, Y LO MARCO ANTES DE SABER SI ACIERTO.** El encargo dice **ES UNA LINEA**, y **mi bloque de correccion mide 23 lineas** (cifra leida de `docs/loop/SALIDA_V213_T1B_BARRIDO_9_10.txt`). Entiendo que la UNA es **la linea corregida**, no el tamaño del remedio, y que el carril del `9.10` obliga a dejar el texto viejo entero y a citar la vuelta y el commit, cosa que no cabe en una linea. **Si la lectura buena era que el remedio entero tenia que caber en una linea, esto es largo de mas y se acorta.** **DISCUTIBLE MARCADO.**

### `2.a` EL INVENTARIO DE CIERRE DE LA FASE III, DE LAS 71 FICHAS, LEIDO DEL REPO

**POR QUE ESTA TAREA Y NO OTRA, Y ES UNA CIFRA MIA Y NO HEREDADA.** Corri `scripts/loop/vuelta150_3_relectura_expediente.py` **en esta vuelta**, con el reloj de git congelado en mi HEAD de apertura, y su salida cruda vive en `docs/loop/SALIDA_V213_T2_VARA.txt`. Su cabecera dice, leida de ahi: *RELOJ DE GIT CONGELADO EN --corte 7be7476e (7be7476e). RANGO PROPIO DE LA VUELTA: 7be7476e..HEAD (7be7476e)*. **El plan esta agotado**, y lo que queda es el cierre.

**LA FUENTE ES LA VARA, NUNCA EL CAMPO** (recuadro 0 de `AUDITOR.md`). La columna `estado` va publicada **al lado y etiquetada como HISTORICA en la propia cabecera de la tabla**, y donde los dos discrepan **lo digo y no lo resuelvo**.

#### 1. COMO SE COMPUSO LA TABLA, Y LA GUARDA QUE LA SOSTIENE

**LA VARA IMPRIME SOLO LAS QUE NO CALZAN, Y EL ENCARGO PIDE LAS 71.** Su propia salida lo dice: *TABLA DE LAS QUE NO CALZAN (40 de 71). Las 31 que calzan NO se imprimen.*. Las 31 que calzan **no existen en ningun fichero de salida**, asi que no se pueden pegar de ninguno. **No reimplemente la vara: la IMPORTE** y llame a sus propias funciones con el mismo corte, que es lo que hace `scripts/loop/_v213_t2_cierre_fase_iii.py`.

**Y LA GUARDA QUE PRUEBA QUE MI COMPUTO ES EL SUYO:** para las filas que la vara **SI** imprime, mi celda de pruebas se coteja contra la suya fila a fila.

**LO QUE SOSTIENE LA TABLA.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 5; FILAS QUE DEBERIA HABER: 5.**

| que se comprobo | lo que dice el instrumento |
|---|---|
| filas que la vara imprime en su tabla de las que no calzan | 40 |
| filas cotejadas contra las mias, y cuantas difieren | CIFRA filas cotejadas: 40 \| CIFRA que DIFIEREN: 0 (se exigen 0) |
| fichas contadas de `docs/plan/OPERACIONES.jsonl` | 71 |
| `id_op` distintos (que no haya dos con el mismo nombre) | 71 |
| **el `sha256` de `docs/plan/OPERACIONES.jsonl` al entrar y al salir** | **SI, QUIETO como se exige** |

**LA GUARDA SE ME CAYO EN SU PRIMERA CORRIDA Y LO DIGO**: cote las filas del fichero entero y me trague **tres filas de OTRAS DOS TABLAS** de la misma salida (la de las desbloqueadas y la de la vara documental), que tambien empiezan por el mismo prefijo y llevan las columnas en otro sitio. **Salieron 43 filas y 3 diferencias.** Acote la lectura a la tabla que toca y las diferencias cayeron a **0** sobre **40**. **Una guarda que solo se ve pasar no prueba nada; esta mordio.**

#### 2. LA TABLA, UNA FILA POR FICHA, LAS 71 Y SIN CORTAR

**LA TABLA ENTERA, PEGADA DE `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt` Y NO TECLEADA.** **FILAS ARMADAS LEYENDO ESE FICHERO: 71; FILAS QUE DEBERIA HABER: 71.** El propio fichero lo vuelve a decir con sus dos cifras juntas: *CIFRA filas de la tabla: 71 | CIFRA fichas que deberia haber: 71*.

| id_op | fase | tipo | estado HISTORICO (contraste) | pruebas que dan positivo, de la vara de esta vuelta | veredicto del repo | calza el campo con el repo |
|---|---|---|---|---|---|---|
| `OP-F-01` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-F-02` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-F-03` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-D-01` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-D-02` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P1+P2+P3a | EJECUTADA | NO |
| `OP-D-03` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P3a | EJECUTADA | NO |
| `OP-D-04` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-D-05` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P1+P3a | EJECUTADA | NO |
| `OP-D-06` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P3a | EJECUTADA | NO |
| `OP-S-01` | 05_SANEO | FUSION | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-S-02` | 05_SANEO | VIGENCIA | HECHA | P3a | EJECUTADA | SI |
| `OP-S-03` | 05_SANEO | VIGENCIA | HECHA | P3a | EJECUTADA | SI |
| `OP-S-04` | 05_SANEO | HERRAMIENTA | HECHA | P3a | EJECUTADA | SI |
| `OP-S-05` | 05_SANEO | HERRAMIENTA | HECHA | P3a | EJECUTADA | SI |
| `OP-S-06` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-S-08` | 05_SANEO | CAMPO_SUCIO | HECHA | P2 | EJECUTADA | SI |
| `OP-S-07` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-S-09` | 05_SANEO | RENOMBRE_CON_ALIAS | HECHA | P3a | EJECUTADA | SI |
| `OP-S-10` | 05_SANEO | REENCUADRE_DE_MARCO | HECHA | P3a | EJECUTADA | SI |
| `OP-C-01` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-C-02` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-C-03` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-C-04` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-U-01` | 03_FUSIONES | FUSION | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-E-01` | 04_ENLACES | ENLACE | LISTA | P3a | EJECUTADA | NO |
| `OP-E-02` | 04_ENLACES | ENLACE | HECHA | P3a | EJECUTADA | SI |
| `OP-M-01` | 06_MESAS | MESA ADJUDICADA: LAS DOS MITADES QUEDAN, CON FRONTERA ADOPTADA | HECHA | P3a | EJECUTADA | SI |
| `OP-M-02` | 06_MESAS | MESA ADJUDICADA: SERIE DECLARADA | HECHA | P3a | EJECUTADA | SI |
| `OP-M-03` | 06_MESAS | MESA ADJUDICADA: DOS PUERTAS MAS UN ACTO | HECHA | P3a | EJECUTADA | SI |
| `OP-M-04` | 06_MESAS | MESA ADJUDICADA: DOS FUSIONES MAS UN ENLACE | HECHA | P3a | EJECUTADA | SI |
| `OP-M-05` | 06_MESAS | MESA ADJUDICADA: DOS ETAPAS, CON FRONTERA REGISTRADA | HECHA | P3a | EJECUTADA | SI |
| `OP-A-01` | 07_ADUANA | FRONTERA_DECLARADA | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-A-02` | 07_ADUANA | MESA | LISTA | P2+P3a+documental | EJECUTADA | NO |
| `OP-V-01` | 08_VERIFICACION | MESA | HECHA | documental | SIN EJECUTAR | NO |
| `OP-U-02` | 03_FUSIONES | FUSION | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-S-11` | 05_SANEO | CAMPO_SUCIO | HECHA | P2+P3a+P3b | EJECUTADA | SI |
| `OP-F-04-COL` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-F-04-HOR` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-F-04-WEI` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-F-04-RAC` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-L-01` | 09_LECTURAS_DIRIGIDAS | MESA | HECHA | documental | SIN EJECUTAR | NO |
| `OP-L-02` | 09_LECTURAS_DIRIGIDAS | MESA | HECHA | ninguna | SIN EJECUTAR | NO |
| `OP-L-03` | 09_LECTURAS_DIRIGIDAS | MESA | HECHA | documental | SIN EJECUTAR | NO |
| `OP-I-01` | 10_INVENTARIO | MESA | LISTA | documental | SIN EJECUTAR | SI |
| `OP-E-03` | 04_ENLACES | LECTURA DIRIGIDA | LISTA | P3b | EJECUTADA | NO |
| `OP-S-12` | 05_SANEO | SANEO MECANICO | HECHA | P2+P3a | EJECUTADA | SI |
| `OP-C-05` | 00_CODIGO | GUARDA | HECHA | P2+P3a+P3b | EJECUTADA | SI |
| `OP-M-02-PROG` | 03_FUSIONES | FUSION DE MESA | LISTA | P1+P3a | EJECUTADA | NO |
| `OP-M-02-MEDIOS` | 03_FUSIONES | FUSION DE MESA | LISTA | ninguna | CONSUMIDA por OP-U-01 | SI |
| `OP-M-02-ASSESS` | 03_FUSIONES | FUSION DE MESA | LISTA | P1 | EJECUTADA | NO |
| `OP-M-02-ADMIT` | 03_FUSIONES | FUSION DE MESA | LISTA | ninguna | CONSUMIDA por OP-U-01 | SI |
| `OP-M-02-ACTIVATE` | 03_FUSIONES | FUSION DE MESA | LISTA | P1 | EJECUTADA | NO |
| `OP-M-02-ACCLIMATE` | 03_FUSIONES | FUSION DE MESA | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-02-ACCOMPLISH` | 03_FUSIONES | FUSION DE MESA | LISTA | P1 | EJECUTADA | NO |
| `OP-D-07` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-M-03-I` | 03_FUSIONES | FUSION DE MESA | LISTA | P1+P3a | EJECUTADA | NO |
| `OP-M-03-II` | 03_FUSIONES | FUSION DE MESA | LISTA | P1+P3a | EJECUTADA | NO |
| `OP-M-03-III` | 03_FUSIONES | FUSION DE MESA | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-03-ENLACES` | 04_ENLACES | ENLACE | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-01-FUSION` | 03_FUSIONES | FUSION DE MESA: LA CAMARILLA DE CINCO | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-E-04` | 04_ENLACES | ENLACE | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-E-05` | 04_ENLACES | ENLACE MUTUO | HECHA | P1+P2+P3a | EJECUTADA | SI |
| `OP-M-01-ESLABONES` | 04_ENLACES | ENLACE | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-05-INDICE` | 03_FUSIONES | FUSION DE MESA | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-05-EDIFICIO` | 03_FUSIONES | FUSION DE MESA | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-05-APERTURA` | 03_FUSIONES | FUSION DE MESA | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-01-SEXTO` | 04_ENLACES | ENLACE MAS PODA DEL SOLAPE | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-E-06` | 04_ENLACES | ENLACE CON EVIDENCIA DE LECTURA | LISTA | P3a | EJECUTADA | NO |
| `OP-E-07` | 04_ENLACES | LECTURA DIRIGIDA CORTA | LISTA | P3a+P3b | EJECUTADA | NO |
| `OP-D-08` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P3a | EJECUTADA | NO |
| `OP-D-09` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P3a | EJECUTADA | NO |

**LA COLUMNA `documental` NO ASCIENDE A NADIE, Y SE DICE:** la vara documental es la cuarta prueba y **solo aplica a las fichas de tipo `MESA`**; el propio instrumento la publica **al lado** y no la funde con las otras tres. Yo hago lo mismo: una ficha cuyo unico positivo sea `documental` **sigue saliendo SIN EJECUTAR** en la columna del veredicto. **`OP-I-01` es exactamente ese caso**, y por eso aparece con `documental` y con `SIN EJECUTAR` a la vez.

#### 3. LAS CUATRO CIFRAS, CADA UNA CONTADA DE LA TABLA

**LAS CUATRO CIFRAS.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 5; FILAS QUE DEBERIA HABER: 5** (las cuatro que el encargo pide mas la suma que las cuadra).

| cifra | lo que dice el instrumento |
|---|---|
| **1. cuantas de las 71 tienen PRUEBA DE EJECUCION en el repo** | **64** |
| **2. cuantas estan CONSUMIDAS, y por quien** | **2**, y las dos son `OP-M-02-MEDIOS` y `OP-M-02-ADMIT`, **las dos por `OP-U-01`** |
| **3. cuantas estan SIN EJECUTAR** | **5** |
| **4. cuantas tienen el campo `estado` en desacuerdo con el repo** | **40**, que se parten en **4** por un lado y **36** por el otro |
| la suma, comprobada contra las 71 | LA SUMA SE COMPRUEBA: 64 con prueba + 2 consumidas + 5 sin ejecutar = 71, y las fichas son 71 |

**LA LISTA ENTERA DE LAS SIN EJECUTAR, QUE EL ENCARGO PIDE ENTERA:**

**LAS SIN EJECUTAR, UNA A UNA.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 5; FILAS QUE DEBERIA HABER: 5.**

| la fila, tal como sale del instrumento |
|---|
| SIN EJECUTAR: OP-V-01                fase 08_VERIFICACION, tipo MESA, estado historico HECHA |
| SIN EJECUTAR: OP-L-01                fase 09_LECTURAS_DIRIGIDAS, tipo MESA, estado historico HECHA |
| SIN EJECUTAR: OP-L-02                fase 09_LECTURAS_DIRIGIDAS, tipo MESA, estado historico HECHA |
| SIN EJECUTAR: OP-L-03                fase 09_LECTURAS_DIRIGIDAS, tipo MESA, estado historico HECHA |
| SIN EJECUTAR: OP-I-01                fase 10_INVENTARIO, tipo MESA, estado historico LISTA |

**AQUI DISCREPO DE LA CIFRA QUE EL ENCARGO CITA, Y LA DECLARO EN VEZ DE RESOLVERLA COPIANDO** (`EJECUTOR.md` 2). El encargo dice que la vara mide **3** en `LISTA` sin ninguna prueba. **Eso reproduce exacto** y esta en su propia salida: *CONTADO: 3 ficha(s) en LISTA sin ninguna prueba de ejecucion.*. **Mi cifra 3 no es esa y no mide lo mismo:** la vara cuenta las que estan **en `LISTA`** sin prueba, y la columna que el encargo me manda escribir es **el veredicto del REPO, que no mira el campo**. Por eso a mis SIN EJECUTAR se suman las **cuatro** que el campo declara `HECHA` y el repo no sostiene (`OP-V-01`, `OP-L-01`, `OP-L-02` y `OP-L-03`), menos las **dos** consumidas, que salen a su propia cifra. **Las dos cuentas son ciertas y miden cosas distintas, y por eso van las dos escritas.**

**Y LA CAUTELA DE LA CUARTA VA PEGADA A ELLA, NO SUELTA** (adjudicacion `6.8` del acta 211): **si cada ficha va poniendo su campo al dia, esa cifra tiende a cero sin que se haya ejecutado nada mas.** Mide **cuanto miente el campo**, no cuanto trabajo queda. **El trabajo que queda es la tercera.**

#### 4. LAS CINCO PROHIBICIONES DE LA TAREA 2, UNA A UNA

**LAS CINCO PROHIBICIONES.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 5; FILAS QUE DEBERIA HABER: 5.**

| que estaba prohibido | que paso |
|---|---|
| **1.** no cambiar el campo `estado` de ninguna ficha | **CUMPLIDA Y PROBADA CON EL `sha256`.** CIFRA sede docs/plan/OPERACIONES.jsonl AL ENTRAR: 514452 bytes, sha256 disco ca1d95b5b3d19e9e, sha256 LF ca1d95b5b3d19e9e y al salir 514452 bytes, sha256 disco ca1d95b5b3d19e9e, sha256 LF ca1d95b5b3d19e9e |
| **2.** no marcar las entradas del inventario | **CUMPLIDA.** El instrumento **abre `docs/plan/INVENTARIO.jsonl` solo para leer**, su `numstat` mide **0** filas, y su recuento no escribe: las incompletas siguen siendo **95** y las marcadas **0** |
| **3.** no escribir ni una fila nueva en `docs/plan/08_VERIFICACION.md` | **CUMPLIDA.** Ese fichero no se abre para escritura en ningun camino de esta tarea, y su `numstat` al cerrar la tarea, sellado en `docs/loop/SALIDA_V213_T2_NUMSTAT.txt`, mide **0** filas |
| **4.** no declarar la campaña consumada ni escribir `PARA_ALEXIS.md` | **CUMPLIDA.** CIFRA PARA_ALEXIS.md existe en el arbol: NO, y esta tarea no lo crea. **No lo esta:** `OP-I-01` sigue abierta y lo que necesita es del fundador |
| **5.** no tocar el grafo | **CUMPLIDA.** El ciclo de Gate 0 mide `git diff HEAD --numstat` en **0** filas en los dos lados |

### `2.b` LA UNICA QUE QUEDA ABIERTA: `OP-I-01`, ESCRITA PARA QUE SE PUEDA DECIDIR

**LO QUE LA FICHA ESCRIBE Y LO QUE NO, DICHO ANTES DE LA TABLA Y NO DESPUES.** La ficha escribe **los cuatro puntos**; **no escribe su estado**. `CUBRE`, `A MEDIAS` y `NO CUBRE` son **veredictos MEDIDOS**, no campos de la ficha: salen de `docs/loop/SALIDA_V211_T2_OP_I_01.txt` y los ratifico el acta 211 en su `6.3` (linea **74595**, leida hoy: ***`6.3` `OP-I-01` NO SE CIERRA, Y AHORA CON EL CRITERIO PUESTO.** Aplicado el criterio*). **No los invento aqui y no se los atribuyo a la ficha.**

**LOS CUATRO PUNTOS DE `verificacion`, PEGADOS ENTEROS DEL FICHERO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 4; FILAS QUE DEBERIA HABER: 4.**

| punto | el texto, pegado entero de la ficha | estado MEDIDO (no es campo de la ficha) |
|---|---|---|
| **1** | toda entrada lleva su fecha_corte | **CUBRE** |
| **2** | toda forma con cobertura incompleta va marcada PROVISIONAL | **NO CUBRE** |
| **3** | todo hueco va NOMBRADO, nunca rellenado | **A MEDIAS** |
| **4** | el inventario se recomputa entero con el disparador de 08_VERIFICACION | **A MEDIAS** |

**EL PUNTO QUE ESTA EN `NO CUBRE`, APARTE Y ENTERO:** PUNTO 2: toda forma con cobertura incompleta va marcada PROVISIONAL

**QUE HARIA FALTA EXACTAMENTE PARA QUE DEJARA DE ESTARLO.** La `6.4` del acta 211 lo deja escrito y lo cito con sus lineas, leidas hoy:

**LAS TRES LINEAS DE LA `6.4`.** **FILAS ARMADAS LEYENDO `docs/loop/ACTA_AUDITOR.md`: 3; FILAS QUE DEBERIA HABER: 3.**

| linea | lo que dice, leido hoy |
|---|---|
| **74601** | **`6.4` LA `D.3` SE ADJUDICA Y EL `NO CUBRE` SE SOSTIENE.** El banco `9.26`, verbatim: |
| **74606** | dice que la forma sea provisional.** **95 formas incompletas y 0 que lo digan: NO CUBRE.** |
| **74607** | **Marcar las 95 es una edicion de datos de `docs/plan/` que ninguna regla ordena hoy**, y |

**EN UNA FRASE, Y SALE DE ESAS TRES LINEAS: no hace falta COMPLETAR la cobertura, hace falta MARCARLA.** El banco `9.26` admite una cobertura incompleta como cumplimiento **si se dice asi**, y hoy ninguna lo dice.

**EL RECUENTO, HECHO POR MI EN ESTA VUELTA Y NO COPIADO.** El comando esta escrito entero en `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt` y su corrida suelta quedo sellada en `docs/loop/SALIDA_V213_T2_RECUENTO_95.txt`, que dice: *entradas 672 | con forma N de M 555 | INCOMPLETAS 95*.

**EL RECUENTO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 5; FILAS QUE DEBERIA HABER: 5.**

| que se conto | cifra de hoy |
|---|---|
| entradas del inventario | 672 |
| de esas, con cobertura de la forma *N de M pares leidos* | 555 |
| **de esas, INCOMPLETAS (`N` menor que `M`)** | **95** |
| de esas incompletas, cuantas llevan `PROVISIONAL` en algun campo | 0 |
| entradas del inventario entero que llevan `PROVISIONAL` | 3 |

**CONTRA LA CIFRA VIEJA, Y LO DIGO AUNQUE COINCIDA.** El acta 211 publica su cifra en la `6.4`, linea **74606**, leida hoy: *dice que la forma sea provisional.** **95 formas incompletas y 0 que lo digan: NO CUBRE.***. Y mi conteo de hoy, del fichero y no del acta: **95, o sea que REPRODUCE al digito.**

**QUE DECIDE EL FUNDADOR Y QUE NO, EN UNA LINEA:** marcar esas **95** entradas es **edicion de datos de `docs/plan/OPERACIONES.jsonl` y sus vecinos que ninguna regla ordena hoy**, y las filas que faltan en `docs/plan/08_VERIFICACION.md` para las fases 09 y 10 **cambian la forma del plan**: **las dos son suyas y ninguna es del bucle.**

**DOS DISCUTIBLES MARCADOS, LOS DOS ANTES DE SABER SI ACIERTO.**

1. **EL VEREDICTO `CONSUMIDA` LO DECIDE EL GRAFO Y LA ATRIBUCION LA FICHA, Y LAS DOS VAN EN LA MISMA CELDA.** Uso `consumida_por()` de la vara tal cual, que resuelve los nodos por `P.1` y exige que caigan en **un solo nodo vivo**; el **por quien** sale del texto de la propia ficha. **Si la casa quisiera esas dos cosas en dos columnas separadas, esta tabla las tiene juntas.** DISCUTIBLE MARCADO.
2. **PUBLICO LOS CUATRO ESTADOS DE `OP-I-01` DE UNA MEDICION DE LA VUELTA 211 Y NO DE UNA MIA DE HOY.** El unico que el encargo me manda recontar es el del punto 2, y ese lo recompute yo (**95**, reproduce). Los otros tres los cito de su fichero con su atribucion en vez de re correrlos, porque el encargo no lo pide y la moratoria manda plan antes que volumen. **Si la vara buena era volver a medir los cuatro hoy, esto es una cita donde tenia que haber una medicion.** DISCUTIBLE MARCADO.

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

