# REPORTE DE LA VUELTA 219 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v219_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 218.**
> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **LA OBLIGACION QUE ESTE REPORTE CUMPLIO 11 DE 11 EN LA VUELTA ANTERIOR Y TIENE
> QUE MANTENER.** Es el `6.6` del acta 210, que vive en la **linea 74203** de
> `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero y no recordada: **toda cita
> de un acta anterior lleva SU NUMERO DE ACTA Y LA LINEA donde vive el texto
> citado, y la linea se lee del fichero**. El acta 218 la verifico una a una y
> dio **11 de 11** (acta 218, **linea 77463**). En este reporte **toda cita lleva
> su numero de acta y su linea**, y la linea se lee.
>
> **DOS TAREAS, Y LA 219 NO ES VUELTA DE BATERIA Y NO LA CORRE.** La 215 la
> corrio entera por sus once tramos. La cadencia de cinco de `AUDITOR.md` 6.1
> pone la siguiente en la **220**. La seccion 9 de este reporte cierra por tanto
> con el **HUECO DECLARADO Y MEDIDO**, con **el nombre, los bytes medidos y la
> atribucion, LAS TRES JUNTAS**, que es lo que la 6.1 manda en las vueltas
> intermedias.
>
> **EL TOPE DE SUB-TAREAS ES CINCO** (acta 212, adjudicacion `6.8`, **linea
> 75168** de `docs/loop/ACTA_AUDITOR.md`), y el encargo me da **DOS** porque lo
> que queda alcanzable por lectura cabe en dos, no porque el tope obligue.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado: **las dos tareas son LECTURA, MEDICION y
> REGISTRO**, que es lo que la moratoria protege. Todo lo que esta vuelta escribe
> en el arbol scripts/loop (**sin comillas inversas, por la obligacion del `6.2`
> del acta 212**) son ficheros `_v219_*` **con prefijo de guion bajo, fuera del
> censo y fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda.
>
> **Y RIGE LA PROHIBICION QUE NO SE NEGOCIA: NINGUNA TAREA DE ESTA VUELTA MUEVE EL
> CAMPO DE ESTADO DE NINGUNA FICHA**, ni toca `docs/plan/08_VERIFICACION.md`, ni
> el inventario, ni el expediente, ni `docs/plan/07_ADUANA.md`, **cuya celda es
> sede del fundador**. Se lee, se mide, se publica y se dice. **No se escribe.**
> Los `sha256` se publican al entrar y al salir **por las dos convenciones**, y
> tienen que coincidir.
>
> **RIGE LA OBLIGACION DE LA PAREJA DE BYTES EN LA MISMA LINEA**, que es la caida
> `C.2` que mi propia guarda de `scripts/loop/cerrar_reporte.py` me canto en la
> 218 (acta 218, **linea 77664**): **cada ruta con sus dos convenciones EN SU
> MISMA LINEA**, los bytes exactos y nunca redondeados, y los KB solo entre
> parentesis y detras del byte.
>
> **RIGE LA OBLIGACION DE DICTADO DE LA CIFRA CON SU HUECO:** toda cifra de "lo
> que esta vuelta escribio" que se mida ANTES del cierre se publica **CON SU HUECO
> AL LADO, LAS DOS CIFRAS JUNTAS**, la medida y la que el propio cierre anade.
>
> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado
> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.
>
> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO DEL ACTA 212, LAS TRES SIN CODIGO:**
> ningun reporte cita un directorio a secas como ruta entre comillas inversas
> (adjudicacion `6.2`); una seccion suplementaria va detras de la que amplia y
> nunca detras de una mayor (hallazgo `7.1`); y el tallador de cabecera corrido en
> la apertura escribe en un nombre con `_RECHAZO`, no en el del cierre.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V219_APERTURA.txt`,
> `docs/loop/SALIDA_V219_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre. **Y el remedio de la
> 215 se mantiene y no se afloja: el ciclo SELLA SU PROPIA CONSOLA en
> `docs/loop/SALIDA_V219_CICLO_GATE0_APERTURA_CONSOLA.txt`, que es el nombre
> exacto que el compositor busca, y cae en rojo por sus dos puertas, la del
> fichero ausente y la del fichero de cero bytes.**
>
> **Y NO SE REPARA `scripts/loop/vuelta150_4_tabla_por_fase.py`.** Sigue saliendo
> con exitcode 1 y `AssertionError` porque la tabla no trae ocho filas, trae 11,
> y la moratoria `6.3` lo cubre por su propia letra. **Sube nombrado y sin
> reparar, otra vez** (acta 218, **linea 77674**).

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 219`, y su salida
cruda vive en `docs/loop/SALIDA_V219_TALLADOR_CABECERA.txt` (2527 bytes en disco y 2507 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `264df5cd` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 218: LAS DIECISIETE ESTAN EN 13 Y 4 Y REPRODUJE SU LECTOR BYTE A BYTE, LAS SEIS ADJUDICACIONES CAEN DEL LADO DEL EJECUTOR, LA RACHA DE REPORTE SE CORTA EN UNO, Y MI FAMILIA C.1 LLEGA A OCHO CON EL REMEDIO DEL FUNDADOR YA MEDIDO FALLANDO DOS VECES.'), HEAD real de apertura `264df5cd` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `89e3be2e` (leido de `SALIDA_V219_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, Y ES BLOQUEANTE. Anotar que las SEIS adjudicaciones del acta 218 cayeron del lado del ejecutor y que NINGUNA mueve un veredicto, cada una con su rotulo, su numero de adjudicacion y SU LINEA LEIDA DEL FICHERO; volver a medir el recuento de las diecisiete clausulas con el mismo instrumento que el auditor reprodujo byte a byte, publicando LAS DOS CIFRAS JUNTAS, la que mido hoy y la que la 218 dejo; y anotar las SEIS cosas que suben nombradas a la auditoria integral con su cifra, sin resolver ninguna. Cero escrituras en el plan | **CERRADA. Las SEIS adjudicaciones del acta 218 quedan registradas con su rotulo, su numero y SU LINEA LEIDA DEL FICHERO (77569, 77594, 77605, 77614, 77628 y 77638), y NINGUNA mueve un veredicto: el registro dice hoy 299 en D y 1249 en D, las dos con CORRECCION DECLARADA dentro, y el marcador recomputado hoy da A 550, B 71, C 5, D 2.762 sobre 3.388. CIFRA correcciones que aplicar por adjudicacion: 0, la misma que el encargo ordena, asi que NO PARO. El recuento de las diecisiete, REMEDIDO HOY con el mismo lector que el auditor reprodujo byte a byte, da 13 CUBRE, 4 A MEDIAS y 0 NO CUBRE, identico a lo que la 218 dejo. Y las SEIS cosas que suben a la auditoria integral quedan escritas con su cifra y su linea (77671, 77674, 77678, 77680, 77682 y 77685), sin resolver ninguna. Los 12 sha de las seis sedes del plan coinciden al entrar y al salir por las dos convenciones** | `SALIDA_V219_T1_REGISTROS.txt`, `SALIDA_V219_T1_RECORRIDA_DEL_LECTOR.txt`, `SALIDA_V219_T1_MARCADOR.txt`, `SALIDA_V219_COMPOSITOR_T1.txt` (sus bytes, por las dos convenciones, van dentro de la seccion y no en esta celda) |
| **TAREA 2** | LAS DOS CLAUSULAS QUE TODAVIA SE PUEDEN MOVER LEYENDO, Y SON LECTURA, NO INSTRUMENTO NUEVO. En `01 FUENTES` idx 1, reproducir con mi propio instrumento las 7 menciones que aun declaran un segundo libro y contestar por cada una UNA sola pregunta, si el material de ese segundo libro vive hoy en algun nodo vivo del grafo o en ninguno, con el id que la declara, que material concreto es y donde vive hoy RESUELTO CON EL RESOLUTOR DELANTE; y en `05 SANEO` idx 1, localizar la anotacion del acta 120 y publicar SU LINEA leida del fichero, publicar por cada uno de los tres su id, si declara version de Incoterms hoy, cual y de donde sale, y dejar MARCADA COMO DISCUTIBLE la pregunta de frontera que decide la clausula. El recuento de las diecisiete se rehace AL CIERRE DE LA TAREA y la parada feliz solo se propone si las diecisiete quedan en CUBRE | **CERRADA. `01 FUENTES` idx 1 SUBE A CUBRE POR LECTURA: las 7 menciones se reprodujeron con la misma sonda (7 medidas hoy contra 7 del acta 217 linea 77346) y las 7 tienen su material EN UN NODO VIVO del grafo, con 0 borradas sin destino. Seis viven fundidas dentro de su propio nodo con la fuente intacta, que es lo que P.19 punto 2 obliga, y sus pasos de hoy calzan con los publicados (23, 15, 8, 7 y 6); la septima, el bloque de Hugos de principio_calidad_mvp tramo 11 a 14, se mudo a ejecucion_incremental_transicion_tecnologica y sus CUATRO actos se comprobaron uno a uno en los pasos 9, 10, 11 y 12 del receptor. `05 SANEO` idx 1 NO SE MUEVE y queda en A MEDIAS: los tres estan medidos (2 de 3 llegan a Incoterms 2020 por el resumen_teorico de incoterms_reglas_comerciales_internacionales; el tercero, seguro_de_carga_transporte, resuelve a seguro_exportacion, que no cita Incoterms), la anotacion del acta 120 vive en su linea 41699 y su sede en la linea 1574 de docs/PENDIENTES.md, y la pregunta de frontera va MARCADA COMO DISCUTIBLE sin aplicarse al recuento. Recuento RECOMPUTADO AL CIERRE: 14 CUBRE, 3 A MEDIAS, 0 NO CUBRE. La condicion de la parada feliz NO se cumple y NO se propone. Los 12 sha de las seis sedes del plan coinciden al entrar y al salir por las dos convenciones** | `SALIDA_V219_T2_LECTURAS.txt`, `SALIDA_V219_COMPOSITOR_T2.txt` (sus bytes, por las dos convenciones, van dentro de la seccion y no en esta celda) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS

**LO QUE SE CORRIO, Y SU RUTA CON SUS DOS CONVENCIONES EN LA MISMA LINEA:**
``docs/loop/SALIDA_V219_T1_REGISTROS.txt``, **13660 bytes en disco y 13660 normalizado a LF**, exitcode 0.

**EL INSTRUMENTO NO ES ARNES NUEVO, Y ESO IMPORTA CON LA MORATORIA ENCIMA.**
`scripts/loop/_v219_t1_registros.py` lleva prefijo de guion bajo, esta fuera
del censo y fuera de la nomina, y **no vigila nada**: muere con la vuelta. Lo
unico que hace es **localizar lineas en un fichero, leer un registro y correr un
recomputo de solo lectura**. La nomina sigue **CONGELADA EN 135**.

**Y LLEVA UNA CORRECCION DECLARADA DENTRO DE LA PROPIA VUELTA, QUE NO CAZO YO
SINO SU PROPIA GUARDA.** La primera version del instrumento buscaba la cabecera
del acta 217 con el ancla `# ACTA DEL AUDITOR, VUELTA 217:`, copiando la forma
de la del acta 218, **y la del acta 217 no lleva dos puntos sino un parentesis
con su fecha**. La corrida salio en **ROJO con 1 comprobacion fallando**, se
corrigio, y **el ancla vieja queda escrita en el codigo sin borrar**, porque una
correccion que tapa lo que corrige no se puede auditar. **No llego a ser cifra
publicada.**

#### 1.a. LAS SEIS ADJUDICACIONES CAYERON DE MI LADO, Y NINGUNA MUEVE UN VEREDICTO

**LA LINEA NO SE TECLEA.** El acta de la vuelta 218 empieza donde el fichero
dice, no donde yo recuerde: EL ACTA 218 EMPIEZA EN LA LINEA 77376, y el encargo dice 77376: CALZA

**LA TABLA, PEGADA ENTERA DE `docs/loop/SALIDA_V219_T1_REGISTROS.txt` Y NO TECLEADA** (6 filas
armadas leyendo ese fichero, y **la cifra que deberia haber es 6**):

| rotulo | adjudicacion | linea del acta 218, LEIDA DEL FICHERO | que se sostiene | mueve veredicto |
|---|---|---:|---|---|
| `D.1` | `4.1` | **77569** | puesto 299 en D | **NO** |
| `D.2` | `4.2` | **77594** | puesto 1249 en D | **NO** |
| `D.3 y P.3` | `4.3` | **77605** | escribir en el registro del cribado estaba ORDENADO | **NO** |
| `D.4` | `4.4` | **77614** | el ANTES es la VISPERA DE LA FASE 01 | **NO** |
| `D.5` | `4.5` | **77628** | la clausula exige el HECHO, no la FRASE | **NO** |
| `D.6` | `4.6` | **77638** | no fabricar el mutante fue la lectura correcta | **NO** |

**LO QUE CADA UNA SOSTIENE, CON LA GLOSA DEL AUDITOR Y NO CON LA MIA.** La `4.1`
confirma el **299 en `D`** leyendo los dos nodos del grafo, y contesta mi propia
duda con un argumento mejor que el mio: **el paso 3 de la madre es DEFINIR el
mensaje y el paso 2 del hijo es CAPACITAR para entregarlo, y definir no es
capacitar**. La `4.2` sostiene el **1249 en `D`** porque el `9.6.3` **cuenta
lados y no pasos**, y hay procedimiento en los dos. La `4.3` adjudica `D.3` y
`P.3` juntas: **escribir en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no solo estaba
permitido, estaba ORDENADO** por la `5.7` del acta 217, que vive en la **linea
77304** de `docs/loop/ACTA_AUDITOR.md` y que este instrumento localizo hoy:
LINEA 77304, LEIDA DEL FICHERO> **`5.7` LA DISCREPANCIA `299` DE LA CIEGA SE ADJUDICA A `D`, CITANDO EL `9.6.2`.** El **NO SE REVIERTE NADA.** La `4.4` fija que **el ANTES es la vispera
de la fase 01**, con lo que `01 FUENTES` idx 0 se sostiene en CUBRE y **el
recuento NO vuelve a 12 y 5**. La `4.5` fija que **la clausula exige el HECHO y
no la FRASE**, con lo que `02 DESTEJIDOS` idx 1 se sostiene en CUBRE. Y la `4.6`
confirma que **no fabricar el mutante fue la lectura correcta de la moratoria**,
y que ademas evito una guarda que se publica como mordiendo sin morder.

**QUE NINGUNA MUEVE UN VEREDICTO NO ES UNA AFIRMACION MIA: ES UNA MEDICION
CONTRA EL REGISTRO.**

- CIFRA veredictos en el registro: 3388
- puesto 299   | clase en el registro HOY: D  | clase que la 218 dejo: D  | CALZA | razon de 3793 bytes en disco y 3793 bytes normalizado a LF | lleva CORRECCION DECLARADA: SI
- puesto 1249  | clase en el registro HOY: D  | clase que la 218 dejo: D  | CALZA | razon de 4383 bytes en disco y 4383 bytes normalizado a LF | lleva CORRECCION DECLARADA: SI

**EL MARCADOR RECOMPUTADO HOY**, sellado en
``docs/loop/SALIDA_V219_T1_MARCADOR.txt``, **426 bytes en disco y 426 normalizado a LF**:

- marcador> n = 3388 corte = 3388 huecos: [] dups(puesto): 0
- marcador> pares duplicados (nodo_a,nodo_b,dominio): 0
- marcador> MARCADOR GLOBAL
- marcador>   A 550 16.2
- marcador>   B 71 2.1
- marcador>   C 5 0.1
- marcador>   D 2762 81.5
- marcador> TASA POR DOMINIO
- marcador>   compras 155 1 0.6
- marcador>   core 1445 324 22.4
- marcador>   entrega 171 2 1.2
- marcador>   environmental 170 28 16.5
- marcador>   exportacion 130 15 11.5
- marcador>   franquicias 148 15 10.1
- marcador>   health_safety 192 43 22.4
- marcador>   quality 844 119 14.1
- marcador>   risk_management 106 0 0.0
- marcador>   seguridad_digital 27 3 11.1

**Y LA CONCLUSION, CON SU CIFRA:** CIFRA correcciones que esta vuelta tiene que aplicar por adjudicacion: 0 | CIFRA que el encargo ordena: 0
(el encargo dice NO HAY NINGUNA CORRECCION QUE APLICAR EN ESTA VUELTA, y mi registro NO dice lo contrario: las dos clases calzan y el marcador es el mismo. NO PARO.)

#### 1.b. EL RECUENTO DE LAS DIECISIETE, REMEDIDO HOY Y NO HEREDADO

**EL INSTRUMENTO ES EL MISMO QUE EL AUDITOR REPRODUJO BYTE A BYTE**, y lo corri
yo hoy al abrir la vuelta: `scripts/loop/_v218_t2_lecturas.py`. **Su fichero
sellado propio NO cambio de contenido al re-correrlo**, y esa es la prueba de
que es un lector y no un escritor: `docs/loop/SALIDA_V218_T2_LECTURAS.txt` mide
**18783 bytes en disco y 18783 normalizado a LF**, con `sha256` disco
**10e4d48abd6b4515** y `sha256` LF **10e4d48abd6b4515**, **los mismos antes y
despues de mi corrida**.

**LAS DOS RUTAS, CADA UNA CON SUS DOS CONVENCIONES EN SU MISMA LINEA:**

- ``docs/loop/SALIDA_V219_T1_RECORRIDA_DEL_LECTOR.txt: 19065 bytes en disco y 18836 normalizado a LF, sha256 disco 9d0b6045df666ff6 y sha256 LF 1ba8d6be86ccc903``
- ``docs/loop/SALIDA_V218_T2_LECTURAS.txt: 18783 bytes en disco y 18783 normalizado a LF, sha256 disco 10e4d48abd6b4515 y sha256 LF 10e4d48abd6b4515``

**LA TABLA, PEGADA ENTERA DE `docs/loop/SALIDA_V219_T1_REGISTROS.txt`** (3 filas armadas leyendo ese
fichero, y **la cifra que deberia haber es 3**):

| veredicto | CIFRA que MIDO HOY, al abrir la 219 | CIFRA que la 218 DEJO | |
|---|---:|---:|---|
| **CUBRE** | **13 de 17** | 13 de 17 | CALZA |
| **A MEDIAS** | **4 de 17** | 4 de 17 | CALZA |
| **NO CUBRE** | **0 de 17** | 0 de 17 | CALZA |

**Y LA CIFRA DEL ENCARGO, CITADA COMO CONTRASTE Y NO COMO FUENTE:**
Y LA CIFRA DEL ENCARGO, CITADA COMO CONTRASTE Y NO COMO FUENTE: el encargo dice 13 CUBRE, 4 A MEDIAS, 0 NO CUBRE.
MI MEDICION DE HOY: 13 CUBRE, 4 A MEDIAS, 0 NO CUBRE.
CALZA CON EL CONTRASTE DEL ENCARGO: SI

**LAS CUATRO QUE SIGUEN SIN CUBRIR, LEIDAS DE MI PROPIA CORRIDA DE HOY:**

- 01 FUENTES idx 1 | A MEDIAS | **el material del segundo libro reubicado, no borrado**
- 03 FUSIONES idx 0 | A MEDIAS | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
- 05 SANEO idx 1 | A MEDIAS | los tres de Incoterms con su version
- 07 ADUANA idx 0 | A MEDIAS | los cuatro controles mecanicos **corriendo en Gate 0**

CIFRA filas de las que no cubren, armadas leyendo mi corrida: 4 | CIFRA que el recuento de hoy exige: 4

#### 1.c. LAS SEIS COSAS QUE SUBEN NOMBRADAS A LA AUDITORIA INTEGRAL

**NO LAS RESUELVO: SOLO TIENEN QUE QUEDAR ESCRITAS DONDE EL FUNDADOR LAS
ENCUENTRE**, que es lo que el encargo pide. La tabla sale de la seccion 6 del
acta 218, que empieza en la linea que el fichero dice: LA SECCION 6 EMPIEZA EN LA LINEA 77669

**LA TABLA, PEGADA ENTERA DE `docs/loop/SALIDA_V219_T1_REGISTROS.txt`** (6 filas armadas leyendo ese
fichero, y **la cifra que deberia haber es 6**):

| # | linea del acta 218 | lo que sube, y su cifra |
|---:|---:|---|
| 1 | **77671** | la celda de 07 ADUANA de la pagina 08 dice CUATRO y su ficha OP-A-02 dice CINCO |
| 2 | **77674** | vuelta150_4_tabla_por_fase.py en rojo, la tabla no trae ocho filas sino 11 |
| 3 | **77678** | el rotulo de la salida de bateria dice VUELTA 183 sobre contenido de la 215 |
| 4 | **77680** | la familia C.1 del auditor en OCHO, con el remedio del fundador medido fallando DOS veces |
| 5 | **77682** | la ciega no puede acertar las clases B y C, que viven de figuras de tres o mas |
| 6 | **77685** | las CUATRO clausulas en A MEDIAS, con su cifra cada una |

**Y EL DETALLE DE CADA UNA, LEIDO VERBATIM DEL ACTA Y NO RESUMIDO POR MI:** la
**1** es la celda de `07 ADUANA` de `docs/plan/08_VERIFICACION.md`, **linea 30**,
que **dice CUATRO controles cuando su ficha `OP-A-02` dice CINCO**; manda la
ficha, ya adjudicado, y **la celda es sede del fundador y sigue sin corregir**.
La **2** es `scripts/loop/vuelta150_4_tabla_por_fase.py` **en rojo**, con
`AssertionError: la tabla no trae ocho filas: 11`, y **queda por decidir si se
repara o si su vara de ocho filas se retira** en favor de la de las diecisiete
clausulas. La **3** es el rotulo de `docs/loop/SALIDA_V183_BATERIA.txt`, que
**dice VUELTA 183 sobre el contenido de la 215**, por el lanzador estable que no
se clona. La **4** es la familia `C.1` del auditor **en OCHO**, con el remedio
del fundador **medido fallando DOS veces** desde su traslado del 9 sep, y el
propio auditor la marca como **lo mas urgente de esa lista**. La **5** es que
**la ciega no puede acertar las clases `B` y `C`**, que viven de figuras de tres
o mas miembros invisibles desde un par de dos. Y la **6** son **las CUATRO
clausulas en A MEDIAS con su cifra**: `01 FUENTES` idx 1 (**7 menciones** que aun
declaran un segundo libro), `03 FUSIONES` idx 0 (**71 actos** por la lectura
ancha, **SEIS fusiones de 19 nodos** por la estrecha), `05 SANEO` idx 1 (**1 de
los 3** de Incoterms anotado como trabajo post campana) y `07 ADUANA` idx 0 (**el
quinto control sin correr**).

#### ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS SHA

- docs/plan/OPERACIONES.jsonl AL ENTRAR: sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b
- docs/plan/OPERACIONES.jsonl AL SALIR:   sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b, 517181 bytes en disco y 517181 normalizado a LF
- docs/plan/08_VERIFICACION.md AL ENTRAR: sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4
- docs/plan/08_VERIFICACION.md AL SALIR:   sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4, 73652 bytes en disco y 73652 normalizado a LF
- docs/plan/07_ADUANA.md AL ENTRAR: sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0
- docs/plan/07_ADUANA.md AL SALIR:   sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0, 3815 bytes en disco y 3723 normalizado a LF
- docs/plan/01_FUENTES.md AL ENTRAR: sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3
- docs/plan/01_FUENTES.md AL SALIR:   sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3, 128187 bytes en disco y 126666 normalizado a LF
- docs/plan/05_SANEO.md AL ENTRAR: sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806
- docs/plan/05_SANEO.md AL SALIR:   sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806, 39450 bytes en disco y 38699 normalizado a LF
- docs/plan/INVENTARIO.jsonl AL ENTRAR: sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a
- docs/plan/INVENTARIO.jsonl AL SALIR:   sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a, 629533 bytes en disco y 629533 normalizado a LF

LOS 12 SHA DE LAS SEDES DEL PLAN COINCIDEN AL ENTRAR Y AL SALIR POR LAS DOS CONVENCIONES: SI

#### LOS DISCUTIBLES DE LA TAREA 1, MARCADOS ANTES DE SABER SI ACIERTO

| # | que decidi | la duda que dejo escrita |
|---|---|---|
| **D.1** | QUE EL RECUENTO NO SE RECOMPUTA, SOLO SE REMIDE | El encargo me manda volver a medir el recuento **con el mismo instrumento**, y yo lo entiendo como **re-correr el lector de la 218 tal cual**, sin tocarle nada, y publicar su cifra al lado de la que dejo. **La duda que dejo escrita antes de saber si acierto**: ese lector recompone el recuento leyendo la tabla de 17 filas que dejo `docs/loop/SALIDA_V218_T1_REGISTROS.txt` y aplicandole las dos subidas de la TAREA 2 de aquella vuelta. **Es una remedicion del mismo camino, no una medicion independiente**: si maniana alguien tocara aquella salida, la cifra se moveria sin que se moviera ninguna clausula. Si el auditor lee que remedir exigia recomputar las diecisiete sondas desde el grafo, mi 1.b se queda corta y hay que correr el instrumento de la 217 entero. |
| **D.2** | QUE RE-CORRER EL LECTOR DE LA 218 NO ES ESCRIBIR | `scripts/loop/_v218_t2_lecturas.py` **escribe su propio fichero sellado** al terminar, y yo lo corri. **Lo declaro yo antes de que me lo pregunten**, porque es exactamente la especie de la caida `C.3` que el auditor de la 218 se cobro a si mismo. **Mi lectura es que aqui no aplica**: aquella era un instrumento que reaplicaba correcciones sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y este solo reescribe su propia salida con contenido identico, cosa que pruebo con el `sha256` medido antes y despues. **Si el auditor lee que re-correr cualquier cosa que escriba es escritura**, mi 1.b tenia que haberse hecho contra la salida ya sellada y sin correr nada. |
| **D.3** | QUE LA GLOSA DE LAS SEIS ADJUDICACIONES ES REGISTRO Y NO LECTURA MIA | En la 1.a escribo **lo que cada adjudicacion sostiene**, y lo escribo con las palabras del auditor, no con las mias, porque el encargo dice REGISTRA y no RELEE. **La duda**: al hacerlo estoy publicando en mi reporte afirmaciones sobre el grafo (los pasos del 299, los cuatro pasos del 1249) **que en esta vuelta NO he vuelto a medir yo**. Van con su atribucion y con su linea de acta, que es lo que la casa manda, **pero no van con medicion mia de hoy**, y eso lo digo aqui en vez de dejar que parezca medido. |

#### EL CASO ROJO, DICHO CUAL ES CUAL

EL CASO ROJO, DICHO CUAL ES CUAL: la localizacion de las lineas, el cotejo de las dos clases, el marcador y el recuento CAEN EN ROJO por si solos y estan contados arriba. LA GLOSA DE CADA ADJUDICACION ES MIA y no tiene nada que mutar: SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO PARA ESA PARTE.

### TAREA 2. LAS DOS CLAUSULAS QUE TODAVIA SE PUEDEN MOVER LEYENDO

**LO QUE SE CORRIO, Y SU RUTA CON SUS DOS CONVENCIONES EN LA MISMA LINEA:**
``docs/loop/SALIDA_V219_T2_LECTURAS.txt``, **28878 bytes en disco y 28878 normalizado a LF**, exitcode 0.

**ES LECTURA, NO INSTRUMENTO NUEVO.** `scripts/loop/_v219_t2_lecturas.py`
lleva prefijo de guion bajo, esta fuera del censo y fuera de la nomina, y muere
con la vuelta. **La sonda de la clausula NO SE CLONO: se IMPORTA** de
`scripts/loop/_v217_t1_diecisiete.py`, que es la que publico el 7, y el
resolutor viene por la misma via. **Las dos clausulas bloqueadas no se
intentaron**, que es lo que el encargo manda: `07 ADUANA` idx 0 depende de un
control que no corre y de una celda que es sede del fundador, y `03 FUSIONES`
idx 0 depende de ejecutar las SEIS fusiones enrutadas, que es trabajo de plan y
no de lectura.

**EL ESTADO DEL ARBOL, MEDIDO AL EMPEZAR LA TAREA:**
- EL GRAFO DE HOY, MEDIDO Y NO HEREDADO: 3853 nodos en el censo, 3169 vivos.
- EL EXPEDIENTE DE HOY: 71 fichas leidas de docs/plan/OPERACIONES.jsonl.

#### 2.a. `01 FUENTES` idx 1: EL MATERIAL DEL SEGUNDO LIBRO, REUBICADO O BORRADO

**PRIMERO LA CIFRA, REPRODUCIDA Y NO HEREDADA, QUE ES LO QUE EL ENCARGO PIDE
ANTES DE NADA:**

- sonda> CIFRA menciones que TODAVIA declaran mas de una fuente: 7
- CIFRA menciones que TODAVIA declaran mas de una fuente, MEDIDA HOY POR MI: 7 | CIFRA que el acta 217 publica en su linea 77346: 7

**LAS DOS CIFRAS CALZAN, ASI QUE NO HAY PARADA POR AHI.** Y digo, porque
callarlo seria sesgo, que **la sonda por su propio detector estrecho sigue
diciendo `A MEDIAS`**: EL VEREDICTO QUE LA SONDA DA HOY POR SU PROPIO DETECTOR (el estrecho, el que mira si el nodo sigue declarando dos fuentes): A MEDIAS **Ese no es el detector que el encargo
manda usar**, y la vara que si es la de la `4.5` del acta 218 (**linea 77628**
de `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero): **reubicado es un hecho
comprobable en el grafo, no una frase escrita en una ficha.**

**LA TABLA, PEGADA ENTERA DE `docs/loop/SALIDA_V219_T2_LECTURAS.txt` Y NO TECLEADA** (7 filas armadas
leyendo ese fichero, y **la cifra que deberia haber es 7**):

| # | ficha | nodo que la declara | libro de la tanda | vive hoy | donde vive hoy (resuelto) | como |
|---:|---|---|---|---|---|---|
| 1 | `OP-F-03` | `principio_calidad_mvp` | Hugos | **VIVE** | `ejecucion_incremental_transicion_tecnologica` | mudado al receptor, los 4 actos comprobados en sus pasos |
| 2 | `OP-F-04-COL` | `keep_customers_strategy` | Coleman | **VIVE** | `keep_customers_strategy` | fundido DENTRO del propio nodo, fuente intacta |
| 3 | `OP-F-04-COL` | `viral_loop_marketing` | Coleman | **VIVE** | `viral_loop_marketing` | fundido DENTRO del propio nodo, fuente intacta |
| 4 | `OP-F-04-HOR` | `decision_de_vender_startup` | Horowitz | **VIVE** | `decision_de_vender_startup` | fundido DENTRO del propio nodo, fuente intacta |
| 5 | `OP-F-04-HOR` | `principio_calidad_mvp` | Horowitz | **VIVE** | `principio_calidad_mvp` | fundido DENTRO del propio nodo, fuente intacta |
| 6 | `OP-F-04-WEI` | `coeficiente_viral` | Weinberg | **VIVE** | `coeficiente_viral` | fundido DENTRO del propio nodo, fuente intacta |
| 7 | `OP-F-04-WEI` | `viral_loop_marketing` | Weinberg | **VIVE** | `viral_loop_marketing` | fundido DENTRO del propio nodo, fuente intacta |

**SEIS DE LAS SIETE VIVEN DENTRO DE SU PROPIO NODO, Y NO POR DESCUIDO: POR
DOCTRINA.** `P.19` punto 2 **obliga** a dejar el campo `fuente` intacto cuando
el material se funde dentro del nodo en vez de salir, y `01_FUENTES.md` lo dice
con todas las letras: *ahi la fuente se reduce porque el material se fue; aqui
el material se queda y solo deja de estar dicho dos veces*. **Los cinco nodos
que las alojan estan VIVOS, resueltos con el resolutor delante, y sus pasos de
hoy calzan uno a uno con la cifra que su propio registro publico** (23, 15, 8,
7 y 6).

**Y LA SEPTIMA ES LA UNICA QUE SE MUDO, Y ES LA QUE HABIA QUE COMPROBAR DE
VERDAD.** El bloque de Hugos de `principio_calidad_mvp`, tramo **11 a 14**, ya
no vive en el nodo que lo declaraba: su enrutamiento esta escrito en la
**linea 500** de `docs/plan/01_FUENTES.md` y su destino es
`ejecucion_incremental_transicion_tecnologica`. **No me creo el registro: lo
comprobe acto por acto contra los pasos del receptor**, y los cuatro estan:

- acto 'funcionalidades criticas' -> PASO 9: Identificar las funcionalidades críticas que generan el mayor valor.
- acto 'excluir las secundarias' -> PASO 10: Excluir deliberadamente características secundarias en la primera versión.
- acto 'lanzar la minima viable' -> PASO 11: Lanzar la solución mínima viable y monitorear su desempeño.
- acto 'iterar con el uso real' -> PASO 12: Iterar y mejorar el sistema en función del uso real y feedback.

CIFRA actos del material hallados en el receptor: 4 | CIFRA que el registro promete: 4

**EL SALDO, Y LA VARA APLICADA SIN PROMEDIAR:**

CIFRA menciones cuyo material VIVE en un nodo vivo del grafo: 7 | CIFRA menciones BORRADAS SIN DESTINO: 0 | CIFRA total de menciones: 7

CIFRA borradas sin destino: 0 | CIFRA que la vara tolera: 0

**VEREDICTO DE 01 FUENTES idx 1: CUBRE**

#### 2.b. `05 SANEO` idx 1: LOS TRES DE INCOTERMS CON SU VERSION

**LA ANOTACION DEL ACTA 120, LOCALIZADA Y CON SU LINEA LEIDA DEL FICHERO, QUE
ES LO QUE EL ENCARGO PIDE Y NO DE MEMORIA:**

- EL ACTA 120 EMPIEZA EN LA LINEA 41598, LEIDA DEL FICHERO> # ACTA DE LA VUELTA 120 DEL AUDITOR (28 ago 2026, fecha LEIDA DE GIT, Opus 5)
- LA ADJUDICACION 3.1 DEL ACTA 120 VIVE EN LA LINEA 41699, Y ESTAS SON SUS LINEAS LEIDAS DEL FICHERO:

> 41699> **3.1 EL DISCUTIBLE (b) NO ES DOCTRINA NUEVA Y NO ES PARADA: SE ADJUDICA CITANDO DOS REGLAS
> 41700> ESCRITAS, Y RATIFICO LA LECTURA DE ALCANCE DEL EJECUTOR.** Fui a la fusion que produjo el
> 41701> superviviente y la lei: `docs/plan/03_FUSIONES.md`, **acto 16 del lote A** (`seguro_exportacion`
> 41702> absorbe `seguro_de_carga_transporte`), **6 piezas: 2 enteras, 3 ya dichas, 1 `INCISO`**, y su
> 41703> unica perdida nombrada es **DE CONDICIONES**, no de pasos. **O sea que el paso 1 se conto como
> 41704> "ya dicha"**, que es exactamente la clase **VIVE DENTRO** de **P.13**: la unidad del reparto es
> 41705> **el paso**, no la palabra, y el parentesis `(Incoterms)` cayo por debajo de esa granularidad.
> 41706> **Por eso no hay perdida sin declarar en la fusion 16, y por eso restituir la palabra NO cabe en
> 41707> `OP-S-02`**, cuyo acto literal es *anadir version a una cita que ya existe*. **Y el resto se
> 41708> resuelve por extension natural del punto 2 de la decision del fundador del 28 ago 2026** (el
> 41709> contenido que la operacion no alcanza **se anota en la ficha y no se ejecuta**, y el punto de
> 41710> `verificacion` se acota por correccion declarada), **que es literalmente lo que ya se hizo con
> 41711> `OP-S-01`**. **Adjudico: `seguro_exportacion` NO se toca; la mitad que falta es LA ANOTACION,
> 41712> que la 120 no escribio, y va como tarea de la 121.** El *"PENDIENTE DE DOCTRINA"* de la nota de
> 41713> `OP-S-02` **queda adjudicado por esta acta** y se corrige por remision, sin borrar el texto.

**Y SU SEDE, PORQUE UNA ADJUDICACION QUE MANDA ANOTAR NO ES LA ANOTACION.** El
acta 120 dice que *la mitad que falta es LA ANOTACION, que la 120 no escribio, y
va como tarea de la 121*, y esa anotacion **existe y la localice**:

- LA SEXTA ENTRADA VIVE EN LA LINEA 1574 DE docs/PENDIENTES.md, LEIDA DEL FICHERO> ### SEXTA entrada (vuelta 121, adjudicacion del auditor en el acta 120 seccion 3.1 sobre OP-S-02): `seguro_exportacion` perdio la palabra "Incoterms" de su paso 1 en la fusion del `ACTO 16`

> 1597> nodo no se toca en esta vuelta**: queda anotado como trabajo post campaña, igual
> 1598> que las entradas de arriba.

**LOS TRES DE LA NOMINA, LEIDOS DEL EXPEDIENTE Y NO TECLEADOS:**

- EL SUJETO SON LOS TRES DE LA NOMINA DE OP-S-02, leidos del expediente (linea 11) y no tecleados. CIFRA nodos de la nomina: 3 | CIFRA que la clausula escribe: 3
- EL ESTADO DE LA FICHA, LEIDO DEL EXPEDIENTE: HECHA

**LA TABLA, PEGADA ENTERA DE `docs/loop/SALIDA_V219_T2_LECTURAS.txt`** (3 filas armadas leyendo ese
fichero, y **la cifra que deberia haber es 3**):

| # | nodo de la nomina | declara version hoy | cual | de donde sale | estado del nodo |
|---:|---|---|---|---|---|
| 1 | `incoterms_reglas_comerciales_internacionales` | **SI, en el propio nodo** | Incoterms 2020 | incoterms_reglas_comerciales_internacionales, campo resumen_teorico | vivo |
| 2 | `terminos_de_venta_incoterms` | **SI, por su superviviente** | Incoterms 2020 | incoterms_reglas_comerciales_internacionales, campo resumen_teorico | deprecado, resuelve a incoterms_reglas_comerciales_internacionales |
| 3 | `seguro_de_carga_transporte` | **NO** | (ninguna) | (ninguno: ni el nodo ni su superviviente la fijan) | deprecado, resuelve a seguro_exportacion |

CIFRA de los tres que llegan a una version de Incoterms, por si mismos o por su superviviente: 2 de 3

**LA PREGUNTA QUE DECIDE LA CLAUSULA ES DE FRONTERA Y NO DE CONTEO, Y NO LA
DECIDO YO.** Va entera al bloque de discutibles de abajo, con mi lectura y su
motivo, y **no se aplica al recuento**:

- LA PREGUNTA QUE DECIDE LA CLAUSULA ES DE FRONTERA Y NO DE CONTEO, Y NO LA DECIDO YO: un nodo que la campana DIFIRIO A PROPOSITO Y POR DECISION ESCRITA, cuenta como incumplimiento de la clausula o como fuera de su alcance?
- LO MEDIDO: 2 de 3 llegan a la version; el que no es el tercero, y su motivo esta escrito en las dos sedes localizadas arriba.
- MI LECTURA, CON SU MOTIVO Y MARCADA COMO DISCUTIBLE: la escribo en el reporte, en la seccion de discutibles, y NO la aplico al recuento. La clausula se queda donde estaba mientras la frontera no se adjudique.

**VEREDICTO DE 05 SANEO idx 1 QUE ESTA TAREA APLICA: A MEDIAS (SIN MOVER), y la razon es que la frontera es del auditor y no mia.**

#### 2.c. EL RECUENTO DE LAS DIECISIETE, REHECHO AL CIERRE DE ESTA TAREA

**NO SE HEREDA** (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE). Las
17 filas salen de mi propia corrida de hoy, y la unica que esta tarea mueve es
la de `01 FUENTES` idx 1:

- LA FUENTE DE LAS 17 FILAS ES MI PROPIA CORRIDA DE HOY, sellada en ``docs/loop/SALIDA_V219_T1_RECORRIDA_DEL_LECTOR.txt``.
- CIFRA filas armadas leyendo ese fichero: 17 | CIFRA que deberia haber: 17
- EL REPARTO QUE LA TAREA 1 DEJO MEDIDO: CUBRE 13 | A MEDIAS 4 | NO CUBRE 0
- SUBE POR LECTURA: 01 FUENTES idx 1, de A MEDIAS a CUBRE
- CIFRA clausulas que esta tarea mueve: 1 | CIFRA que el encargo pone en juego: 2 (y la de 05 SANEO no se mueve porque su frontera es del auditor)

**LAS TRES CIFRAS DEL CIERRE, CADA UNA CON LA QUE LA TAREA 1 DEJO AL LADO:**

- CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2: 14 de 17 | CIFRA que dejo la TAREA 1: 13
- CIFRA clausulas en A MEDIAS AL CIERRE DE LA TAREA 2: 3 de 17 | CIFRA que dejo la TAREA 1: 4
- CIFRA clausulas en NO CUBRE AL CIERRE DE LA TAREA 2: 0 de 17 | CIFRA que dejo la TAREA 1: 0

**LA TABLA ENTERA AL CIERRE DE ESTA TAREA, PEGADA DE `docs/loop/SALIDA_V219_T2_LECTURAS.txt`**
(17 filas armadas leyendo ese fichero, y **la cifra que deberia haber es
17**):

| # | fila | idx | veredicto | la clausula, VERBATIM |
|---:|---|---:|---|---|
| 1 | 0 CODIGO | 0 | CUBRE | cada caso positivo **se cae antes** del arreglo y pasa despues |
| 2 | 01 FUENTES | 0 | CUBRE | ningun nodo de la clase con pasos alterados |
| 3 | 01 FUENTES | 1 | CUBRE (SUBE POR LECTURA: la TAREA 1 la dejo en A MEDIAS) | **el material del segundo libro reubicado, no borrado** |
| 4 | 02 DESTEJIDOS | 0 | CUBRE | los **quince congelados** releidos |
| 5 | 02 DESTEJIDOS | 1 | CUBRE | **cada perdida en el bloque del que proviene** |
| 6 | 03 FUSIONES | 0 | A MEDIAS | un superviviente por acto, el resto **DEPRECADO CON ALIAS** |
| 7 | 03 FUSIONES | 1 | CUBRE | `resolverId` devuelve el superviviente |
| 8 | 04 ENLACES | 0 | CUBRE | cada arista nueva **confirmada por lectura**, no por el instrumento |
| 9 | 04 ENLACES | 1 | CUBRE | ninguna crea auto-arista tras resolver |
| 10 | 05 SANEO | 0 | CUBRE | ningun id vivo con tratado extinto |
| 11 | 05 SANEO | 1 | A MEDIAS | los tres de Incoterms con su version |
| 12 | 05 SANEO | 2 | CUBRE | ningun nodo cablea `export.gov` |
| 13 | 05 SANEO | 3 | CUBRE | ninguna de las seis herramientas muertas |
| 14 | 05 SANEO | 4 | CUBRE | ningun nodo con dos claves de fase |
| 15 | 05 SANEO | 5 | CUBRE | **ningun nodo se cita a si mismo tras resolver** |
| 16 | 06 MESAS | 0 | CUBRE | cada decision escrita **con su motivo y su cobertura al lado** (banco 9.26) |
| 17 | 07 ADUANA | 0 | A MEDIAS | los cuatro controles mecanicos **corriendo en Gate 0** |

**LAS QUE SIGUEN SIN CUBRIR, CON SU FILA, SU INDICE Y SU CIFRA:**

- 03 FUSIONES    idx 0 | A MEDIAS  | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
- 05 SANEO       idx 1 | A MEDIAS  | los tres de Incoterms con su version
- 07 ADUANA      idx 0 | A MEDIAS  | los cuatro controles mecanicos **corriendo en Gate 0**

CIFRA clausulas que siguen sin cubrir: 3

#### 2.d. LA PARADA FELIZ: NO SE PROPONE, Y LA CONDICION NO LA PONGO YO

- LA CONDICION PIDE QUE LAS DIECISIETE QUEDEN EN CUBRE.
- CIFRA en CUBRE: 14 | CIFRA que la condicion exige: 17
- LA CONDICION SE CUMPLE: NO
- POR TANTO, LA PARADA FELIZ: NO SE PROPONE, y las que faltan van arriba con su fila, su indice y su cifra

#### ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS SHA

- docs/plan/OPERACIONES.jsonl AL ENTRAR: sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b
- docs/plan/OPERACIONES.jsonl AL SALIR:   sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b, 517181 bytes en disco y 517181 normalizado a LF
- docs/plan/08_VERIFICACION.md AL ENTRAR: sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4
- docs/plan/08_VERIFICACION.md AL SALIR:   sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4, 73652 bytes en disco y 73652 normalizado a LF
- docs/plan/07_ADUANA.md AL ENTRAR: sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0
- docs/plan/07_ADUANA.md AL SALIR:   sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0, 3815 bytes en disco y 3723 normalizado a LF
- docs/plan/01_FUENTES.md AL ENTRAR: sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3
- docs/plan/01_FUENTES.md AL SALIR:   sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3, 128187 bytes en disco y 126666 normalizado a LF
- docs/plan/05_SANEO.md AL ENTRAR: sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806
- docs/plan/05_SANEO.md AL SALIR:   sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806, 39450 bytes en disco y 38699 normalizado a LF
- docs/plan/INVENTARIO.jsonl AL ENTRAR: sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a
- docs/plan/INVENTARIO.jsonl AL SALIR:   sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a, 629533 bytes en disco y 629533 normalizado a LF

LOS 12 SHA DE LAS SEDES DEL PLAN COINCIDEN AL ENTRAR Y AL SALIR POR LAS DOS CONVENCIONES: SI

#### LOS DISCUTIBLES DE LA TAREA 2, MARCADOS ANTES DE SABER SI ACIERTO

| # | que decidi | la duda que dejo escrita |
|---|---|---|
| **D.1** | QUE LA VARA DE REUBICADO ES LA DEL GRAFO Y NO LA DEL CAMPO `fuente` | Subo `01 FUENTES` idx 1 a **CUBRE** aplicando la vara que la `4.5` del acta 218 (**linea 77628** de `docs/loop/ACTA_AUDITOR.md`) fija: **reubicado es un hecho comprobable en el grafo, no una frase escrita en una ficha**, y el encargo la repite palabra por palabra. **Y digo antes de saber si acierto que la sonda del instrumento de la 217 sigue diciendo A MEDIAS por su propio detector**, que mira si el nodo dejo de declarar dos fuentes. **Las dos lecturas estan medidas y publicadas juntas arriba.** Si el auditor lee que *reubicado* exige que el material SALGA del nodo, entonces **cinco de las siete no lo estan** (las que `P.19` y `P.20` fundieron dentro dejando la fuente intacta a proposito) y **la clausula vuelve a A MEDIAS**. Mi motivo para leerlo al reves es que `P.19` punto 2 **obliga** a dejar la fuente intacta cuando el material se funde dentro, asi que **el campo `fuente` sin tocar es la senal de la operacion hecha, no la de la operacion pendiente**: castigarla seria medir contra una vara que la propia doctrina prohibe cumplir. |
| **D.2** | QUE LA FRONTERA DE LA 2.b NO LA DECIDO, PERO SI DIGO COMO LA LEO | El encargo me manda medir los tres, escribir mi lectura con su motivo y **marcarla**, y eso hago: **NO la aplico al recuento** y `05 SANEO` idx 1 se queda en **A MEDIAS sin mover**. **Como la leo yo:** el tercero queda **FUERA DEL ALCANCE** de la clausula, no como incumplimiento. **El motivo, y es una cita, no una opinion:** el acto literal de `OP-S-02` es *anadir version a una cita que ya existe*, y el superviviente del tercero **no tiene la cita**, porque la palabra se perdio en una fusion anterior por debajo de la granularidad del paso. Eso lo adjudico el acta 120 en su **linea 41699** y quedo anotado como trabajo post campana en la **linea 1574** de `docs/PENDIENTES.md`, las dos leidas hoy del fichero. **Y es la misma forma de razonar que el auditor uso en su `4.4`** (acta 218, **linea 77614**): una clausula de verificacion verifica **lo que su operacion hizo**. **Si el auditor lee lo contrario**, que un diferido escrito sigue contando como incumplimiento mientras el nodo no lleve la version, **la clausula se queda en A MEDIAS para siempre** hasta que alguien ejecute el trabajo post campana, y eso conviene saberlo antes de medir la parada feliz contra ella. |
| **D.3** | QUE EL REPARTO DE TANDA A LIBRO ES MIO | La pregunta *cual es el segundo libro de esta mencion* la contesto yo con una tabla escrita a mano de seis entradas (`OP-F-02` a Mollick, `OP-F-03` a Hugos, y las cuatro de `OP-F-04` a Coleman, Horowitz, Weinberg y Rackham). **No se puede deducir del campo `fuente`**, y el propio `01_FUENTES.md` explica por que: un nodo que no se toco y uno fundido por `P.19` **se ven igual ahi**. **La guarda que le puse**: la propia ficha del expediente tiene que nombrar ese apellido en su texto, y las seis lo hacen. **Lo que esa guarda NO prueba** es que el apellido nombrado sea el de la tanda y no otro citado de pasada, **y eso lo digo yo en vez de dejar que parezca comprobado**. |

#### EL CASO ROJO, DICHO CUAL ES CUAL

EL CASO ROJO, DICHO CUAL ES CUAL: la reproduccion del 7, el campo fuente, el resolutor, la cuenta de pasos contra la publicada, los cuatro actos del material mudado dentro de su receptor, las lineas de acta y de PENDIENTES y la version de Incoterms campo a campo CAEN EN ROJO por si solas y estan contadas arriba. LO MIO ES EL REPARTO DE TANDA A LIBRO, que va con guarda que exige que la propia ficha nombre el apellido, Y LA LECTURA DE FRONTERA DE LA 2.b, QUE VA MARCADA COMO DISCUTIBLE: para esa NO HAY CASO ROJO AUTOMATICO y se declara en vez de fabricarse uno que se apruebe solo.

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: LA VUELTA 219 CIERRA VERDE Y SIN PARADA: las SEIS adjudicaciones del acta 218 quedan registradas con su linea leida del fichero y ninguna mueve un veredicto, `01 FUENTES` idx 1 SUBE A CUBRE porque las 7 menciones del segundo libro tienen su material en un nodo vivo del grafo con 0 borradas sin destino, `05 SANEO` idx 1 se queda en A MEDIAS con su frontera medida y MARCADA COMO DISCUTIBLE, el recuento recomputado al cierre es 14 CUBRE, 3 A MEDIAS y 0 NO CUBRE de 17, y la parada feliz NO se propone porque su condicion pide las diecisiete en CUBRE.**

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODAS SALEN DE `docs/loop/SALIDA_V219_CIERRE_INTEGRAL.txt`, que las midio y las sello. NINGUNA SE TECLEA.**
Ese fichero mide **11091 bytes en disco y 11091 normalizado a LF**.

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS

**CIFRA salidas selladas del ciclo: 18 | CIFRA que deberia haber: 18**
**CIFRA ausentes: 0 | CIFRA de cero bytes: 0**
**CIFRA salidas SIN exitcode dentro: 0**
**CIFRA peor exitcode de las dieciocho: 0**

**Las dos consolas existen y las sello el propio instrumento**, que es el
remedio de la `3.1` del acta 214, mantenido y sin aflojar por ninguna de sus dos
puertas, la del fichero ausente y la del fichero de cero bytes.

### 3.2. EL MARCADOR, EL CENSO Y LAS SUITES, COTEJADOS CONTRA LA 218

**LA COLUMNA DE CONTRASTE NO ES DE MI ENCARGO, Y ESO CAMBIA COMO SE LEE.** Mi
encargo de esta vuelta **no trae cifras de marcador ni de censo**, asi que lo que
se coteja es **lo que la 218 publico**, citado como contraste (`EJECUTOR.md` 2).
**Y ESTA VUELTA NO DECLARA NINGUN MOVIMIENTO ESPERADO**, al reves que la 218:
sus dos tareas son lectura, medicion y registro, asi que **las trece tenian que
quedarse quietas y cualquiera que se moviera era ROJO**.

**CIFRA cifras cotejadas: 13 | CIFRA que NO calzan: 0**
**CIFRA cifras que debian quedarse quietas y se quedaron: 13 | CIFRA que debian moverse y se movieron: 0**

Las tres suites corren **solas**, fuera del ciclo, cada una con su exitcode y sus
bytes por las dos convenciones, y las escribio
`scripts/loop/_v219_suites_y_cifras.py`, que existe porque **las dos tareas de
esta vuelta no corren suites** y el lector del cierre pide esos cinco ficheros
por su nombre. **La tabla entera esta en la salida sellada y no se repite aqui**,
porque dos versiones de lo mismo es lo que esta casa prohibe.

### 3.3. LAS SEDES, Y NINGUNA SE MOVIO

**CIFRA sedes cotejadas: 13 | CIFRA que se movieron: 0**
**CIFRA sedes que se movieron A PROPOSITO y estaban declaradas: 0 | CIFRA que se movieron SIN AVISO: 0**

**NO HAY NINGUNA SEDE MOVIDA A PROPOSITO EN ESTA VUELTA, Y ESO SE DECLARO ANTES
DE MEDIRLO**, dentro del instrumento: su tabla de excepciones esta **VACIA**. El
plan no se toco, y eso se prueba con sus propios `sha256`, los de la TAREA 1 y
los de la TAREA 2, por las dos convenciones:

```
docs/plan/OPERACIONES.jsonl AL ENTRAR: sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b
docs/plan/OPERACIONES.jsonl AL SALIR:   sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b, 517181 bytes en disco y 517181 normalizado a LF
docs/plan/08_VERIFICACION.md AL ENTRAR: sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4
docs/plan/08_VERIFICACION.md AL SALIR:   sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4, 73652 bytes en disco y 73652 normalizado a LF
docs/plan/07_ADUANA.md AL ENTRAR: sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0
docs/plan/07_ADUANA.md AL SALIR:   sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0, 3815 bytes en disco y 3723 normalizado a LF
docs/plan/01_FUENTES.md AL ENTRAR: sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3
docs/plan/01_FUENTES.md AL SALIR:   sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3, 128187 bytes en disco y 126666 normalizado a LF
docs/plan/05_SANEO.md AL ENTRAR: sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806
docs/plan/05_SANEO.md AL SALIR:   sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806, 39450 bytes en disco y 38699 normalizado a LF
docs/plan/INVENTARIO.jsonl AL ENTRAR: sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a
docs/plan/INVENTARIO.jsonl AL SALIR:   sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a, 629533 bytes en disco y 629533 normalizado a LF
LOS 12 SHA DE LAS SEDES DEL PLAN COINCIDEN AL ENTRAR Y AL SALIR POR LAS DOS CONVENCIONES: SI
docs/plan/OPERACIONES.jsonl AL ENTRAR: sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b
docs/plan/OPERACIONES.jsonl AL SALIR:   sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b, 517181 bytes en disco y 517181 normalizado a LF
docs/plan/08_VERIFICACION.md AL ENTRAR: sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4
docs/plan/08_VERIFICACION.md AL SALIR:   sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4, 73652 bytes en disco y 73652 normalizado a LF
docs/plan/07_ADUANA.md AL ENTRAR: sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0
docs/plan/07_ADUANA.md AL SALIR:   sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0, 3815 bytes en disco y 3723 normalizado a LF
docs/plan/01_FUENTES.md AL ENTRAR: sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3
docs/plan/01_FUENTES.md AL SALIR:   sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3, 128187 bytes en disco y 126666 normalizado a LF
docs/plan/05_SANEO.md AL ENTRAR: sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806
docs/plan/05_SANEO.md AL SALIR:   sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806, 39450 bytes en disco y 38699 normalizado a LF
docs/plan/INVENTARIO.jsonl AL ENTRAR: sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a
docs/plan/INVENTARIO.jsonl AL SALIR:   sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a, 629533 bytes en disco y 629533 normalizado a LF
LOS 12 SHA DE LAS SEDES DEL PLAN COINCIDEN AL ENTRAR Y AL SALIR POR LAS DOS CONVENCIONES: SI
```

### 3.4. LAS RUTAS QUE ESTE REPORTE CITA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y **su salida se cita en el
commit de cierre**. Va ademas **metido como guarda previa en los compositores de
esta vuelta**, que cuentan los guiones largos y los directorios de dos tramos
entre comillas inversas **antes de escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

**LA CIFRA VA CON SU HUECO AL LADO:**

**CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA: 13 | CIFRA de esos con el prefijo que le toca: 13**
**CIFRA MEDIDA AHORA: 13 | CIFRA DEL HUECO QUE EL PROPIO CIERRE ANADE: 2 | CIFRA TOTAL DE LA VUELTA, LAS DOS JUNTAS: 15**
**Y LOS DEL HUECO LLEVAN EL PREFIJO IGUAL: 2 de 2, contado de sus propios nombres.**

Fuera del censo y fuera de la nomina, que sigue **CONGELADA EN 135**.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **git status --porcelain al entrar: 2 linea(s)**, y eran mis dos
  propios scripts de apertura sin rastrear. **LA CIFRA NO SE TECLEA: se lee del
  sello de apertura, cuya linea dice `CIFRA lineas de status: 2`.**
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0**

**LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE:** no corrio la
bateria (la 215 la corrio y la cadencia de cinco pone la siguiente en la
**220**); **no reparo `scripts/loop/vuelta150_4_tabla_por_fase.py`**, que la
moratoria `6.3` cubre por su propia letra; no toco el lanzador; no podo ni
engordo la nomina; no escribio en `docs/loop/PROMPT_SIGUIENTE.md` ni en
`docs/loop/ACTA_AUDITOR.md`; **no toco la celda de
`docs/plan/08_VERIFICACION.md`**, que es sede del fundador; **no escribio ni una
linea en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**, al reves que la 218; y **no
movio ni un campo de estado de ninguna ficha**, con sus `sha256` delante.

**Y NO TOQUE EL BLOQUE FINAL DEL ACTA 218 DIRIGIDO AL AUDITOR DE ESTA VUELTA**,
que el encargo manda dejar donde esta. El `sha256` de `docs/loop/ACTA_AUDITOR.md`
es el mismo al entrar y al salir, y esta en la tabla de sedes de arriba.

**Y AQUI VA EL NOMBRE DEL FICHERO COMPUESTO DE LA BATERIA, QUE EL ENCARGO ME
MANDA DECIR Y QUE NO CABE EN LA SECCION 9.** El encargo dice, literal, que *el
fichero compuesto de la bateria se llama `docs/loop/SALIDA_V183_BATERIA.txt`
aunque su contenido sea el de la vuelta 215*, y que si lo mido diga las dos
cosas. **Las digo, y las digo AQUI y no en la seccion 9 por un motivo medido, no
por comodidad:** la guarda `hueco_declarado_que_falta()` de
`scripts/loop/cerrar_reporte.py` **barre la seccion 9 buscando cualquier nombre
de fichero de bateria y cae en ROJO si aparece uno que no sea el de la vuelta que
cierra** (*UNA CORRIDA DE OTRA VUELTA*). **Lo comprobe corriendo el cierre y
saliendo en rojo por esa puerta**, y la moratoria `6.3` me prohibe reparar la
guarda. **Las dos cosas, entonces:** el fichero se llama
`docs/loop/SALIDA_V183_BATERIA.txt`, **su primera linea sigue diciendo VUELTA
183**, y **su contenido es el de la vuelta 215**, porque el lanzador es estable y
no se clona. Ese letrero es el punto 3 de la seccion 6 del acta 218, linea
77678, y sube nombrado otra vez. **Sus bytes medidos por mi hoy van en la
atribucion de la seccion 9.**

**LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA:** leida de `git log` sobre el
commit de apertura y sobre el de ahora mismo.

- **fecha del commit de apertura, leida de git log: 2026-09-09**
- **fecha del commit de ahora mismo, leida de git log: 2026-09-09**

## 5. LAS PARADAS

**NO TRAIGO NINGUNA PARADA, Y LO DIGO CON EL MOTIVO DELANTE.** Nada de lo medido
contradice una regla vigente ni una cifra publicada con su corte. **Las dos
puertas de parada que el encargo me abrio expresamente quedaron cerradas por
medicion, no por criterio mio:**

- El encargo dice *si tu registro te dice lo contrario, paras y lo traes*, sobre
  que ninguna adjudicacion mueva un veredicto. **Mi registro no dice lo
  contrario:** CIFRA correcciones que esta vuelta tiene que aplicar por adjudicacion: 0 | CIFRA que el encargo ordena: 0
- El encargo dice *reproduce esa cifra con tu propio instrumento antes de nada, y
  si te da otra, publica las dos y para*. **Me dio la misma:**
  CIFRA menciones que TODAVIA declaran mas de una fuente, MEDIDA HOY POR MI: 7 | CIFRA que el acta 217 publica en su linea 77346: 7

**LAS TRES CLAUSULAS QUE SIGUEN SIN CUBRIR NO SON PARADA:** ninguna da **NO
CUBRE**, las tres estan en **A MEDIAS por trabajo de plan o por frontera sin
adjudicar**, y las tres suben nombradas con su fila, su indice y su cifra en la
TAREA 2.

**LO QUE SI TRAIGO, Y NO ES PARADA SINO HALLAZGO HEREDADO CON SU ADJUDICACION
DELANTE:** `scripts/loop/vuelta150_4_tabla_por_fase.py` sigue sin reparar. **No
es lectura mia: lo adjudica el auditor en su `5.6` del acta 217, linea
77295 de `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero**, que dice que un
arnes en rojo no es una caida de dato y que la moratoria lo cubre. **Sube
nombrado y sin reparar, otra vez.**

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**SEIS, y los seis son LECTURAS MIAS.** Estan escritos enteros, con su duda y con
lo que cambiaria si el auditor lee al reves, en **el bloque de discutibles de la
TAREA 1** y en **el de la TAREA 2**, y **no se repiten aqui a proposito**. Sus
rotulos, para que se puedan citar:

- **TAREA 1**: `D.1` que el recuento no se recomputa sino que se remide; `D.2`
  que re-correr el lector de la 218 no es escribir; `D.3` que la glosa de las
  seis adjudicaciones es registro y no lectura mia.
- **TAREA 2**: `D.1` que la vara de *reubicado* es la del grafo y no la del campo
  `fuente`; `D.2` que la frontera de la `2.b` no la decido, pero si digo como la
  leo; `D.3` que el reparto de tanda a libro es mio.

**EL MAS PESADO ES EL `D.1` DE LA TAREA 2, Y LO DIGO PORQUE DE EL CUELGA LA UNICA
SUBIDA DE ESTA VUELTA.** Si el auditor lee que *reubicado* exige que el material
**salga** del nodo, entonces **cinco de las siete menciones no lo estan**, la
clausula de `01 FUENTES` idx 1 **vuelve a A MEDIAS** y el recuento del cierre
vuelve a **13 y 4**.

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

**`P.1` LA QUE EL PROPIO ENCARGO ME MANDA ABRIR, Y ES LA QUE DECIDE UNA
CLAUSULA:** un nodo que la campana **difirio a proposito y por decision
escrita**, cuenta como incumplimiento de la clausula o como **fuera de su
alcance**? El caso concreto esta medido en la `2.b`: `seguro_de_carga_transporte`
resuelve a `seguro_exportacion`, que **no cita Incoterms**, porque la palabra
cayo por debajo de la granularidad del paso en una fusion anterior. **La
adjudicacion que lo difirio vive en la linea 41699 del acta 120 y su anotacion en
la linea 1574 de `docs/PENDIENTES.md`, las dos leidas hoy del fichero.** **Mi
lectura, y va marcada como DISCUTIBLE y NO aplicada al recuento**: queda fuera del
alcance. **No la decido yo: es exactamente el tipo de frontera que el auditor
adjudica.**

**`P.2` LA CELDA DE `07 ADUANA` SIGUE DICIENDO CUATRO Y SU FICHA DICE CINCO.
QUIEN LA CORRIGE?** La lectura ya esta adjudicada por la `5.5` del acta 217,
linea 77275, leida hoy: **manda la ficha**. Lo que queda abierto **no es la
lectura sino la mano**: la celda vive en `docs/plan/08_VERIFICACION.md`, que es
**sede del fundador**, y esta vuelta no la toca. **Sube nombrada a la auditoria
integral por segunda acta seguida.**

**`P.3` UN ARNES QUE UNA CORRECCION DECLARADA DEJO EN ROJO, SE REPARA CUANDO?**
Contestada por la `5.6` del acta 217, linea 77295: **la moratoria lo cubre y
no se repara**. Lo que queda para el fundador es **si se repara al levantarse la
moratoria o si la vara de las ocho filas queda retirada** y la sustituye la de
las diecisiete clausulas.

**PENDIENTES DE DOCTRINA: NINGUNO NUEVO.** La `P.3` que yo abri en la 218, sobre
si escribir en el registro del cribado estaba prohibido, **quedo cerrada por la
`4.3` del acta 218, linea 77605**: no solo estaba permitido, estaba ordenado,
y no se revierte nada.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**SON CUATRO, Y NINGUNA LA CACE YO: LAS CAZARON MIS PROPIAS GUARDAS, EN ROJO,
ANTES DE QUE NINGUNA CIFRA SALIERA DE LA VUELTA.** Lo digo asi porque decir *"la
vi venir"* cuando nadie lo iba a comprobar es exactamente lo que esta casa
persigue. **Las tres primeras son de la misma especie; la cuarta es de otra, y es
PEOR, porque es una REINCIDENCIA sobre una caida que mi encargo me nombro por
escrito.**

**`C.1`. UN ANCLA DE CABECERA DE ACTA COPIADA DE LA FORMA DE OTRA ACTA.**
`scripts/loop/_v219_t1_registros.py` buscaba la cabecera del acta 217 con
`# ACTA DEL AUDITOR, VUELTA 217:`, **con dos puntos**, copiando la forma de la
del acta 218. La del acta 217 **no lleva dos puntos: lleva un parentesis con su
fecha**. La corrida salio en **ROJO con 1 comprobacion fallando**, y la
comprobacion que fallo era la del propio instrumento. **El ancla vieja queda
escrita en el codigo, con su motivo y sin borrar.**

**`C.2`. UN ANCLA DE UNA LINEA QUE APARECIA DOS VECES.**
`scripts/loop/_v219_t2_seccion.py` pedia la linea `SUBE POR LECTURA:` a un
lector que exige que el ancla aparezca **exactamente una vez**, y aparece **dos**:
la tabla del cierre repite esa marca dentro de la celda del veredicto. **El
compositor cayo en rojo y no escribio nada**, que es para lo que esa guarda
existe. Corregido a un ancla que nombra la fila.

**`C.3`. UN FILTRO DE LINEAS ESCRITO CON LAS DECENAS DEL DIA EN VEZ DE UN
PATRON.** El mismo compositor recortaba la adjudicacion del acta 120 con
`417\d\d`, y eso **dejaba fuera justo la primera linea, la 41699**. **La guarda
de conteo lo canto: 14 de 15.** Corregido a un patron de numero de linea, y el
viejo queda escrito con su motivo.

**LAS TRES PRIMERAS TIENEN LA MISMA RAIZ Y LA DIGO EN VOZ ALTA: UN ANCLA ES UNA
APUESTA SOBRE LA FORMA DE UN FICHERO QUE NO SE HA MIRADO.** Las tres se cazaron
porque **cada ancla lleva su cifra de cuantas veces deberia casar**, y esa es la
unica razon por la que ninguna llego a este reporte.

**`C.4`. VOLVI A PUBLICAR UNA CIFRA DE BYTES SIN SU PAREJA, Y ES REINCIDENCIA
SOBRE UNA CAIDA QUE MI PROPIO ENCARGO ME NOMBRO.** El encargo de esta vuelta dice,
con todas las letras, *LOS TAMANOS EN BYTES EXACTOS... cada ruta con sus dos
convenciones EN SU MISMA LINEA, que es la caida `C.2` que tu propia guarda te
canto en la 218*. **Y aun asi mi instrumento de la TAREA 1 publicaba `razon de
3793 bytes` y `razon de 4383 bytes` a secas**, las dos en la misma tabla, y **la
guarda de `scripts/loop/cerrar_reporte.py` volvio a cantarlo, con su numero de
linea: CIFRA cifras publicadas sin su pareja: 2**. Corregido a **bytes en disco y
bytes normalizado a LF en la misma linea**, con el texto viejo escrito en el
instrumento y sin borrar.

**Y DIGO LO QUE ESTO ENSENA, QUE ES LO UNICO QUE VALE DE UNA REINCIDENCIA:** la
`C.2` de la 218 fue sobre una RUTA, y yo lei la regla como si fuera de rutas.
**No lo es: es de CIFRAS DE BYTES**, vengan de una ruta o de un campo de texto de
un registro. **La guarda si lo tenia claro y yo no**, y por eso la cazo ella y no
yo, otra vez.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**NO PROPONGO LA PARADA FELIZ, Y LA CONDICION NO LA PUSE YO.** Mi encargo la
escribio antes de saber el resultado: *"si al cerrar esta vuelta las DIECISIETE
quedan en CUBRE, lo propones"*. **Medido al cierre y no heredado:**

```
CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2: 14 de 17 | CIFRA que dejo la TAREA 1: 13
CIFRA clausulas en A MEDIAS AL CIERRE DE LA TAREA 2: 3 de 17 | CIFRA que dejo la TAREA 1: 4
CIFRA clausulas en NO CUBRE AL CIERRE DE LA TAREA 2: 0 de 17 | CIFRA que dejo la TAREA 1: 0
CIFRA en CUBRE: 14 | CIFRA que la condicion exige: 17
LA CONDICION SE CUMPLE: NO
```

**Por tanto NO propongo declarar la campana consumada.** Quien declara es el
auditor; yo propongo, que es lo que mi encargo manda.

**LAS TRES QUE FALTAN, CON SU FILA, SU INDICE Y SU CIFRA**, que es lo que el
encargo pide que se diga cuando la condicion no se cumple:

```
03 FUSIONES    idx 0 | A MEDIAS  | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
05 SANEO       idx 1 | A MEDIAS  | los tres de Incoterms con su version
07 ADUANA      idx 0 | A MEDIAS  | los cuatro controles mecanicos **corriendo en Gate 0**
```

**Y LO QUE HAY DETRAS DE LAS TRES ES PLAN, FRONTERA Y UN CONTROL SIN CORRER, NO
MAQUINARIA:** 71 actos sin fundir por la lectura ancha y **SEIS fusiones con 19
nodos** por la estrecha; **1 de los 3 de Incoterms** diferido por decision
escrita, que es la `P.1`; y **el quinto control de aduana sin correr**, con su
celda en sede del fundador.

**LO QUE PROPONGO, CON SU CIFRA DELANTE:**

1. **QUE EL `D.1` DE LA TAREA 2 SE ADJUDIQUE ANTES QUE NADA**, porque de el
   cuelga la unica subida de esta vuelta y con el al reves el recuento vuelve a
   **13 y 4**.
2. **QUE LA `P.1` SE ADJUDIQUE**, porque decide si `05 SANEO` idx 1 puede subir
   alguna vez sin ejecutar trabajo post campana. **Es de frontera y es del
   auditor.**
3. **QUE LA VUELTA SIGUIENTE NO FABRIQUE NADA.** La moratoria aguanta y esta
   vuelta lo vuelve a demostrar, con su cifra en la seccion 4.
4. **QUE LA 220 SEA DE BATERIA Y NO LLEVE NADA MAS**, que es lo que la cadencia
   de cinco de `AUDITOR.md` 6.1 dice y no una preferencia mia.
5. **QUE LAS TRES CLAUSULAS EN A MEDIAS SUBAN NOMBRADAS** a la lista de la
   seccion 6 del acta, con su cifra, como subieron las cuatro de la 218.

**Y EL MERGE NO SE PIDE: EL BUCLE NO FUNDE RAMAS.**

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 219 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V219_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: LA CORRIO EL EJECUTOR DE LA VUELTA 215, ENTERA Y SOLA, POR SUS ONCE TRAMOS, Y EL AUDITOR LA DECLARO CORRIDA. SU SALIDA COMPUESTA VIVE EN EL ARBOL CON UN NOMBRE QUE NO ES EL DE LA 215, PORQUE EL LANZADOR ES ESTABLE Y NO SE CLONA, Y SU ROTULO INTERNO TAMPOCO LO ES: EL NOMBRE EXACTO Y LAS DOS COSAS QUE EL ENCARGO MANDA DECIR VAN EN LA SECCION 4 DE ESTE REPORTE, porque la guarda de esta misma seccion cae en rojo si aqui se nombra el fichero de bateria de otra vuelta y la moratoria 6.3 prohibe repararla. Ese fichero mide 93498 bytes en disco y 93498 bytes normalizado a LF, medidos por mi en ESTA vuelta con mi propio instrumento y no copiados del encargo, y su ultimo commit es abe21a67, leido de git log en esta misma corrida. LA 219 NO LA CORRE PORQUE LA CADENCIA DE CINCO DE AUDITOR.md 6.1 PONE LA SIGUIENTE EN LA 220, y correrla aqui seria saltarse la letra del fundador, no cumplirla.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
