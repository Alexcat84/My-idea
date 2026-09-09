## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE ESTA SECCION CITA EL FICHERO DEL QUE SALE** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO). Las de las dos tareas van en su anexo, talladas por `scripts/loop/_v213_t1_seccion.py` y `scripts/loop/_v213_t2_seccion.py`, y **aqui no se repiten**.

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, NUNCA `run_phase1.py` A SECAS

Corrido con `scripts/loop/_v213_ciclo_gate0.py`, que **IMPORTA** los ocho comandos de `scripts/loop/_v205_ciclo_gate0.py` y solo le corrige el numero de vuelta, computado de su propio nombre y no tecleado.

**EL CICLO DE GATE 0, LOS DOS LADOS.** **FILAS ARMADAS LEYENDO las DIECIOCHO salidas `docs/loop/SALIDA_V213_*_APERTURA.txt` y `_CIERRE.txt`: 9; FILAS QUE DEBERIA HABER: 9.**

| # | comando | APERTURA | CIERRE |
|---|---|---|---|
| 1 | `run_phase1.py --reaplico-curaduria` | EXITCODE 0, 4790 bytes | EXITCODE 0, 4790 bytes |
| 2 | `etiquetas_de_cara.py --aplicar` | EXITCODE 0, 7928 bytes | EXITCODE 0, 7928 bytes |
| 3 | `sync_assets_web.py` | EXITCODE 0, 574 bytes | EXITCODE 0, 574 bytes |
| 4 | `git diff HEAD --numstat` | EXITCODE 0, **0 filas**, 140 bytes | EXITCODE 0, **0 filas**, 140 bytes |
| 5 | `vuelta83_conteo_aristas.py WORK` | EXITCODE 0, 168 bytes | EXITCODE 0, 168 bytes |
| 6 | `vuelta85_medir_desfase_calibrado` | EXITCODE 0, 498 bytes | EXITCODE 0, 498 bytes |
| 7 | `engine/run_all_tests.py` | EXITCODE 0, 1131 bytes | EXITCODE 0, 1131 bytes |
| 8a | `npx tsc --noEmit` | EXITCODE 0, 7 bytes | EXITCODE 0, 7 bytes |
| 8b | `pnpm test` | EXITCODE 0, 336 bytes | EXITCODE 0, 336 bytes |

**LAS DIECIOCHO CELDAS SE CUENTAN DE SUS DIECIOCHO FICHEROS**, una a una, y el `EXITCODE` sale de la ultima linea de cada uno. **PEOR EXITCODE DE LOS OCHO: 0 en los dos lados**, leido de las dos consolas selladas (`docs/loop/SALIDA_V213_CICLO_GATE0_APERTURA_CONSOLA.txt` y su gemela de cierre). **`git diff HEAD --numstat` da CERO FILAS en los dos lados: el grafo no se movio ni al abrir ni al cerrar**, que es la quinta prohibicion de la TAREA 2.

### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES

**LAS SEDES, AL ENTRAR Y AL CERRAR.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_APERTURA.txt` para la apertura y una medicion de AHORA para el cierre: 8; FILAS QUE DEBERIA HABER: 8.**

| sede | al entrar (disco / LF) | al cerrar (disco / LF) | `sha256` de cierre (disco / LF) | la movio esta vuelta |
|---|---|---|---|---|
| `docs/plan/03_FUSIONES.md` | 831759 / 826733 | 833308 / 828282 | `f06d25b41c587316` / `46c592fa8da942e2` | **SI**, la `TAREA 1.b`: la correccion declarada del `9.10` |
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 4057130 / 4057130 | 4057130 / 4057130 | `758edf1f5c313c18` / `758edf1f5c313c18` | NO, y era guarda expresa de la TAREA 1 |
| `docs/INTRA_DOMINIO_INFORME.md` | 943970 / 943970 | 943970 / 943970 | `c05b6bcd20188a9c` / `c05b6bcd20188a9c` | NO, y su linea 6941 era prohibicion expresa |
| `docs/plan/OPERACIONES.jsonl` | 514452 / 514452 | 514452 / 514452 | `ca1d95b5b3d19e9e` / `ca1d95b5b3d19e9e` | NO, y era la prohibicion 1 de la TAREA 2 |
| `docs/plan/INVENTARIO.jsonl` | 584554 / 584554 | 584554 / 584554 | `69666b73339f2afe` / `69666b73339f2afe` | NO, y era la prohibicion 2 de la TAREA 2 |
| `docs/plan/08_VERIFICACION.md` | 69068 / 69068 | 69068 / 69068 | `76bfebb6b2d8ef72` / `76bfebb6b2d8ef72` | NO, y era la prohibicion 3 de la TAREA 2 |
| `dataset/metadata/master_graph.json` | 8375817 / 8375817 | 8375817 / 8375817 | `627cc662296f7f00` / `627cc662296f7f00` | NO, solo se leyo |
| `docs/BANCO_DE_TEXTOS.md` | 186490 / 186490 | 186490 / 186490 | `8adbd60239509bb4` / `8adbd60239509bb4` | NO, solo se leyeron sus `9.10` y `9.26` |

**LA UNICA QUE SE MOVIO SE MOVIO UNA SOLA VEZ, Y LO PRUEBA CON `sha256` DISTINTO AL SALIR:** el sha256 LF de docs/plan/03_FUSIONES.md SE MUEVE: 515fd9ff9541ae8a -> 46c592fa8da942e2 (SI, como se exige). **`docs/plan/03_FUSIONES.md` es tambien la unica sede cuyas dos convenciones NO COINCIDEN**, y no es cosa de esta vuelta: entra y sale asi.

**Y LAS SIETE QUE NO SE MOVIERON LO PRUEBAN CON SU PROPIO `sha256`, NO CON UNA PROMESA:** el del archivo de veredictos y el del informe se publican al entrar y al salir en `docs/loop/SALIDA_V213_T1B_BARRIDO_9_10.txt`, y el de `docs/plan/OPERACIONES.jsonl` en `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`.

### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, MEDIDAS CON EL INSTRUMENTO DE LA CASA

**LA CIFRA NO SE PUBLICA AQUI, Y NO ES OMISION: ES LA REGLA.** El instrumento que las cuenta es `scripts/loop/vuelta186_rutas_del_reporte.py` y **necesita el reporte YA CERRADO** para contar las rutas que el propio cierre anade. Publicar aqui la cifra de antes del cierre seria medir temprano y publicar tarde, que es la caida de la vuelta 28 (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE). **Su salida sellada es `docs/loop/SALIDA_V186_RUTAS_DEL_REPORTE.txt` y ahi vive la cifra**, corrida sobre el reporte cerrado y commiteada con el.

**Y ESTE REPORTE ESTA ESCRITO PARA QUE ESE INSTRUMENTO PUEDA LLEGAR A IMPRIMIR:** por la obligacion 1 del encargo, **ninguna ruta de directorio va entre comillas inversas en ninguna de sus secciones**. Donde hay que nombrar un arbol, se nombra sin ellas o se nombra un fichero suyo.

## 4. LO QUE SE TOCO, Y LO QUE NO

**SE TOCO UNA SOLA SEDE Y EN UN SOLO SITIO:** `docs/plan/03_FUSIONES.md`, con una correccion declarada y aditiva pegada tras su linea 5425. **NI UN NODO DEL GRAFO**, que es lo que la regla 4 de `EJECUTOR.md` manda en modo de cierre, y lo prueban las dos celdas de `git diff HEAD --numstat` de la `3.1`, las dos en cero filas.

**LO QUE MI APERTURA SELLADA DICE, COTEJADO Y NO TECLEADO** (`docs/loop/SALIDA_V213_APERTURA.txt`): **`git status --porcelain` AL ENTRAR daba 1 linea(s)**, y era mi propio computo `_v213_apertura.py` sin seguir todavia, no trabajo ajeno colgando; y **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0**, o sea que la vuelta empezo con el grafo limpio.

### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO

**TODO LO QUE ESTA VUELTA ESCRIBIO EN EL ARBOL scripts/loop, LISTADO CON `os.listdir` EN ESTA CORRIDA.** **FILAS ARMADAS LEYENDO un `os.listdir` de ese arbol filtrado por el prefijo: 12; FILAS QUE DEBERIA HABER: 12.**

| fichero | que es |
|---|---|
| `scripts/loop/_v213_apertura.py` | computo de la vuelta |
| `scripts/loop/_v213_arreglar_esqueleto.py` | computo de la vuelta |
| `scripts/loop/_v213_ciclo_gate0.py` | computo de la vuelta |
| `scripts/loop/_v213_cierre_texto.md` | cuerpo compuesto, no fuente |
| `scripts/loop/_v213_cierre_texto.py` | computo de la vuelta |
| `scripts/loop/_v213_esqueleto.py` | computo de la vuelta |
| `scripts/loop/_v213_t1_seccion.md` | cuerpo compuesto, no fuente |
| `scripts/loop/_v213_t1_seccion.py` | computo de la vuelta |
| `scripts/loop/_v213_t1b_barrido_9_10.py` | computo de la vuelta |
| `scripts/loop/_v213_t2_cierre_fase_iii.py` | computo de la vuelta |
| `scripts/loop/_v213_t2_seccion.md` | cuerpo compuesto, no fuente |
| `scripts/loop/_v213_t2_seccion.py` | computo de la vuelta |

**CIFRA ficheros con prefijo `_v213_`: 12, de ellos 9 con extension `.py` y 3 con extension `.md`.** **LA CIFRA Y LA LISTA SALEN DEL MISMO `os.listdir`, en la misma linea de codigo.**

**LOS 12 LLEVAN LOS 12 EL PREFIJO DE GUION BAJO**, o sea que estan **fuera del censo y fuera de la nomina**, y mueren con la vuelta. **NINGUNO ES ARNES, GUARDA NI LECTOR NUEVO, Y NINGUNO REPARA NADA:** el de la `1.b` importa `medir_en_disco()` de `scripts/loop/vuelta186_rutas_del_reporte.py`; el de la TAREA 2 **importa la vara entera**, `scripts/loop/vuelta150_3_relectura_expediente.py`, y llama a sus propias funciones en vez de reescribirlas; el del ciclo importa `scripts/loop/_v205_ciclo_gate0.py`; y los compositores solo leen salidas y arman texto. **LA NOMINA DE LA BATERIA SIGUE CONGELADA EN 135 Y NADIE LA PODO.**

**LOS DOS INSTRUMENTOS QUE EL ENCARGO PROHIBE REPARAR SIGUEN SIN TOCAR:** `scripts/loop/vuelta186_rutas_del_reporte.py` (su `main()` con `os.path.exists`) y `secciones_fuera_de_orden()`. **Los dos estan levantados y los dos esperan a la integral.**

### 4.2. LAS TRES OBLIGACIONES DE DICTADO NUEVAS, CUMPLIDAS Y MEDIDAS

**LAS TRES OBLIGACIONES NUEVAS.** **FILAS ARMADAS LEYENDO el propio reporte y los dos ficheros del tallador: 3; FILAS QUE DEBERIA HABER: 3.**

| cual | que hice |
|---|---|
| **1.** ningun reporte cita un directorio a secas como ruta entre comillas inversas (adjudicacion `6.2` del acta 212) | **CUMPLIDA, Y CON UNA EDICION DECLARADA QUE NO PIENSO CALLARME.** Donde hay que nombrar un arbol, este reporte escribe *el arbol scripts/loop* o *el arbol del plan*, sin comillas inversas, o nombra un fichero suyo. **PERO UNA CITA VERBATIM DEL ACTA TRAIA UNO DENTRO** (su linea 74607), y una cita no se reescribe: lo que hice fue **quitarle las comillas inversas al directorio y dejar el texto intacto**, en `sin_dir()`, que **apunta y publica cada limpieza**. Su cifra, leida de `docs/loop/SALIDA_V213_COMPOSITOR_T2.txt`: CIFRA comillas inversas quitadas a un directorio citado: 1 ['docs/plan/'], y CIFRA directorios que AUN van entre comillas inversas: 0 (se exigen 0). **La prueba de que basta es que `vuelta186_rutas_del_reporte.py` LLEGA A IMPRIMIR** sobre el reporte cerrado, y su salida va commiteada |
| **2.** una seccion suplementaria va detras de la que amplia, nunca detras de una mayor (hallazgo `7.1` del acta 212) | **CUMPLIDA POR LA VIA MAS BARATA: ESTE REPORTE NO TIENE NINGUNA CABECERA `## N BIS.`.** El hallazgo de la vuelta va como **subseccion numerada de la seccion que amplia**, asi que `secciones_fuera_de_orden()` lo ve sin que haya que repararla |
| **3.** el tallador de cabecera corrido en apertura escribe en un nombre con `_RECHAZO` (mi propia `C.1` de la 212, adoptada como obligacion en la `4.1`, linea 75028) | **CUMPLIDA A LA PRIMERA.** La corrida de apertura fue a `docs/loop/SALIDA_V213_TALLADOR_RECHAZO.txt` y la del cierre a `docs/loop/SALIDA_V213_TALLADOR_CABECERA.txt`. **Ningun commit de esta vuelta tuvo un rechazo dentro del fichero que promete una cabecera** |


### 4.3. LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA, PORQUE ESTA CRUZO LA MEDIANOCHE

**LO DIGO YO ANTES DE QUE ME LO PREGUNTEN.** El bloque de correccion que la `1.b` escribio en `docs/plan/03_FUSIONES.md` lleva dentro la fecha **8 sep 2026**, y el commit que lo transporta esta fechado el **9 sep 2026**. **NO ES UNA FECHA SUPUESTA NI UNA INCOHERENCIA: ES QUE LA VUELTA CRUZO LA MEDIANOCHE**, y las dos cifras estan medidas y selladas en `docs/loop/SALIDA_V213_FECHA_MEDIDA.txt`.

**LAS CUATRO FECHAS, LEIDAS DEL RELOJ Y DE GIT.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_FECHA_MEDIDA.txt`: 4; FILAS QUE DEBERIA HABER: 4.**

| que se midio | lo que dice el instrumento |
|---|---|
| cuando se escribio de verdad el bloque (mtime del fichero) | 2026-09-08 23:58:39.082757500 -0400 |
| la fecha que el bloque lleva escrita dentro | 8 sep 2026 |
| el commit que lo transporta y su fecha | d5fe887e64c7dd00ceb97a6f51aac223d92e47e5 2026-09-09 00:02:14 -0400 |
| el commit de apertura de la vuelta y su fecha | 2026-09-08 04:28:57 -0400 |

**LA REGLA QUE OBEDEZCO ES LA CORRECCION DECLARADA DE LA VUELTA 60**, que vive en `docs/plan/03_FUSIONES.md` linea 2471: *la fecha de todo reporte y de toda nota fechada SE MIDE (del reloj del sistema o del commit) y no se supone*. **La fecha del bloque es la del reloj cuando se escribio, y aqui queda dicho al lado la del commit.**

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**LOS TRES DISCUTIBLES.** **FILAS ARMADAS LEYENDO las dos secciones de tarea de este mismo reporte: 3; FILAS QUE DEBERIA HABER: 3.**

| cual | donde | que dudo |
|---|---|---|
| `D.1` | TAREA 1.b | **EL ENCARGO DICE *ES UNA LINEA* Y MI BLOQUE DE CORRECCION MIDE 23.** Entiendo que la UNA es la linea CORREGIDA y no el tamaño del remedio, y que el carril del `9.10` obliga a dejar el texto viejo entero y a citar vuelta y commit, cosa que no cabe en una linea. **Si la lectura buena era que el remedio entero cupiera en una linea, esto es largo de mas y se acorta.** |
| `D.2` | TAREA 2.a | **EL VEREDICTO `CONSUMIDA` MEZCLA DOS FUENTES EN UNA CELDA.** La medicion la da el grafo (los nodos resuelven por `P.1` a un solo nodo vivo) y la atribucion la da el texto de la propia ficha. Uso `consumida_por()` de la vara tal cual, que devuelve las dos separadas, y **las publico juntas**. Si la casa las quiere en dos columnas, esta tabla las tiene en una. |
| `D.3` | TAREA 2.b | **TRES DE LOS CUATRO ESTADOS DE `OP-I-01` SON CITA Y NO MEDICION DE HOY.** El unico que el encargo manda recontar es el del punto 2, y ese lo recompute yo. Los otros tres los cito de `docs/loop/SALIDA_V211_T2_OP_I_01.txt` con su atribucion. **Si la vara buena era volver a medir los cuatro hoy, esto es una cita donde tenia que haber una medicion.** |

**LOS TRES ESTAN MARCADOS ANTES DE SABER SI ACIERTO**, que es la condicion de la regla 7 de `EJECUTOR.md`, y los tres viven tambien dentro de su propia seccion de tarea, no solo aqui.

## 6. LAS PREGUNTAS

**LAS DOS PREGUNTAS.** **FILAS ARMADAS LEYENDO las dos secciones de tarea de este mismo reporte: 2; FILAS QUE DEBERIA HABER: 2.**

| cual | que pregunto |
|---|---|
| `P.1` | **EL INVENTARIO DE CIERRE EXISTE. ¿DONDE VIVE A PARTIR DE HOY?** La TAREA 2 lo produce entero y su salida cruda esta sellada, pero **su unica sede publicada es este reporte**, y los reportes se archivan y no se releen. Si la auditoria integral o el cierre de campaña lo van a necesitar, **alguien tiene que decidir si eso baja a un fichero propio del arbol del plan**. Yo no lo bajo: escribir en ese arbol es lo que la TAREA 2 tiene prohibido. |
| `P.2` | **EL PLAN ESTA AGOTADO Y LA UNICA FICHA VIVA NO LA PUEDE CERRAR EL BUCLE. ¿QUE HACE LA 214?** La cifra 3 de mi TAREA 2 mide **5 SIN EJECUTAR**, y de esas **cuatro** son fichas cuyo campo dice `HECHA` sin prueba en el repo y **una** es `OP-I-01`, que espera al fundador. **No hay trabajo de plan que encargar que no sea una de esas dos cosas**, y las dos son decisiones que no me tocan. **Lo pregunto en vez de inventarme una tarea.** |


## 7. PENDIENTES DE DOCTRINA

**EL PENDIENTE DE DOCTRINA.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_VARA.txt` y `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 1; FILAS QUE DEBERIA HABER: 1.**

| cual | que falta escrito |
|---|---|
| `PD.1` | **NINGUNA REGLA DICE SI LA PRUEBA DOCUMENTAL ASCIENDE A UNA FICHA A EJECUTADA.** La vara publica la cuenta vieja y la de la pata documental **una al lado de la otra, con su diferencia nombrada**, y dice expresamente que no poda nada; pero **no dice cual de las dos gobierna un veredicto de cierre**. Yo tome la estrecha (la documental **no** asciende) y lo escribi en la seccion de la tarea, con `OP-I-01` como el ejemplar que sale `documental` y `SIN EJECUTAR` a la vez. **PENDIENTE DE DOCTRINA, registrado y no inventado.** |


## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**NO DECLARO NINGUNA CAIDA DE CIFRA PUBLICADA NI DE CLASE EN ESTA VUELTA, Y LO DIGO CON LO QUE LA SOSTIENE, NO COMO AFIRMACION SUELTA.** Ninguna cifra de este reporte esta tecleada: las dos secciones de tarea y estas seis las arman compositores que leen ficheros de salida y caen en rojo si la linea no esta. **PERO SI DECLARO UNA OBLIGACION ROTA, LA `C.1`, Y ES LA TERCERA FILA DE LA TABLA DE ABAJO:** rompi la obligacion 1 de mi propio encargo en la prosa del esqueleto. **Las otras dos filas son guardas que mordieron antes de publicar nada, y las cuento porque una guarda que solo se ve pasar no prueba nada.**

**LAS TRES GUARDAS QUE MORDIERON, Y LA TERCERA ES CULPA MIA.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T1B_BARRIDO_9_10.txt`, `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt` y `docs/loop/SALIDA_V213_ARREGLAR_ESQUELETO.txt`: 3; FILAS QUE DEBERIA HABER: 3.**

| # | donde | que paso |
|---|---|---|
| **1.** | TAREA 1.b, antes de escribir en el disco | **LA GUARDA `(6)` ME TUMBO LA COMPOSICION.** Exigia que el bloque citara la vuelta del volteo y mi texto la escribia en mayusculas; la simulacion dio **1 fallo** y **no escribio**. Corregi la guarda para que compare sin distinguir mayusculas y volvi a correr. **El disco no se toco en la corrida caida.** |
| **2.** | TAREA 2.a, antes de publicar la tabla | **LA GUARDA DEL COTEJO ME CAZO TRES FILAS AJENAS.** Cotejaba contra el fichero entero de la vara y me tragaba filas de otras dos tablas suyas: **43 filas y 3 diferencias**. Acotada a la tabla que toca, **40 cotejadas y 0 diferencias.** **La tabla mala no llego a ningun reporte.** |
| **3.** | MI PROPIO ESQUELETO DE APERTURA, y esta si es mia de verdad | **ROMPI LA OBLIGACION 1 EN LA PROSA QUE YO MISMO TALLE AL ABRIR.** El bloque de la moratoria del esqueleto citaba el arbol scripts/loop **entre comillas inversas**, que es exactamente el directorio a secas que la adjudicacion `6.2` del acta 212 prohibe. **La cazo `vuelta186_rutas_del_reporte.py` corriendo sobre el reporte cerrado**, o sea el instrumento que esa obligacion existe para que pueda llegar a imprimir: revento con `FileNotFoundError` sobre ese directorio. **LA CORRECCION VA DECLARADA Y MEDIDA** en `docs/loop/SALIDA_V213_ARREGLAR_ESQUELETO.txt` (el texto nuevo se lee del fuente del esqueleto, no se teclea; el viejo tenia que aparecer exactamente una vez; y despues quedan **0** directorios de dos tramos entre comillas inversas). **NO ES CAIDA DE CIFRA PUBLICADA NI DE CLASE, pero ES romper una obligacion escrita en mi propio encargo, y la cuento yo antes de que me la cuenten.** |


**Y UNA COSA MAS QUE DIGO YO Y QUE NADIE ME HA PREGUNTADO, PORQUE ES LA ESPECIE QUE ESTA CASA PERSIGUE:** las unicas cifras de este reporte que **no** salen de un instrumento mio de esta vuelta son **las del acta 212 que registro en la `1.a`** (su **1603** bytes, su **95**, sus rachas). **Van todas con la linea del acta donde viven y con su atribucion**, y ninguna se usa como fuente de una cifra nueva: donde el encargo me manda recontar una, la reconte (el **95** del inventario, que reproduce al digito).

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

1. **NO ENCARGAR TRABAJO DE PLAN, PORQUE NO QUEDA.** Mi TAREA 2 lo mide: **64** de **71** tienen prueba de ejecucion en el repo, **2** estan consumidas y **5** salen SIN EJECUTAR, y **ninguna de esas cinco la puede cerrar el bucle solo**.
2. **LA 215 ES LA VUELTA DE BATERIA**, por la cadencia de cinco de `AUDITOR.md` 6.1. La 213 no lo es y su seccion 9 lo declara con su hueco medido. **La 214 tampoco.**
3. **SI HAY QUE ELEGIR UNA TAREA, QUE SEA LA `P.1` DE MI SECCION 6:** bajar el inventario de cierre a una sede propia, si el auditor decide que debe existir fuera de un reporte archivado. **Eso es escribir en el arbol del plan y hoy lo tengo prohibido**, asi que no lo hago por mi cuenta.
4. **LO QUE NO PROPONGO, Y LO DIGO PARA QUE NO SE IMPROVISE:** no proponer reparar `vuelta186_rutas_del_reporte.py` ni `secciones_fuera_de_orden()`; **los dos estan levantados, los dos esperan a la integral y la moratoria sigue en pie**.

