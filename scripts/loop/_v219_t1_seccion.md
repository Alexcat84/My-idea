### TAREA 1. LOS REGISTROS

**LO QUE SE CORRIO, Y SU RUTA CON SUS DOS CONVENCIONES EN LA MISMA LINEA:**
``docs/loop/SALIDA_V219_T1_REGISTROS.txt``, **13582 bytes en disco y 13582 normalizado a LF**, exitcode 0.

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
- puesto 299   | clase en el registro HOY: D  | clase que la 218 dejo: D  | CALZA | razon de 3793 bytes | lleva CORRECCION DECLARADA: SI
- puesto 1249  | clase en el registro HOY: D  | clase que la 218 dejo: D  | CALZA | razon de 4383 bytes | lleva CORRECCION DECLARADA: SI

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
