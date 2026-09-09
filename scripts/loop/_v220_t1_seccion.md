### TAREA 1. LOS REGISTROS

**LO QUE SE CORRIO, Y SU RUTA CON SUS DOS CONVENCIONES EN LA MISMA LINEA:**
``docs/loop/SALIDA_V220_T1_REGISTROS.txt``, **23161 bytes en disco y 23161 normalizado a LF**, exitcode 0.

**EL INSTRUMENTO NO ES ARNES NUEVO, Y ESO IMPORTA CON LA MORATORIA ENCIMA.**
`scripts/loop/_v220_t1_registros.py` lleva prefijo de guion bajo, esta fuera
del censo y fuera de la nomina, y **no vigila nada**: muere con la vuelta. Lo
unico que hace es **localizar lineas en un fichero, re-correr un lector ajeno y
contar**. La nomina sigue **CONGELADA EN 135**.

#### 1.a. LAS SEIS ADJUDICACIONES DEL ACTA 219, CON SU LINEA LEIDA DEL FICHERO

**LA LINEA NO SE TECLEA.** El acta de la vuelta 219 empieza donde el fichero
dice, no donde yo recuerde: EL ACTA 219 EMPIEZA EN LA LINEA 77727, y el encargo dice 77727: CALZA

**LA TABLA, PEGADA ENTERA DE `docs/loop/SALIDA_V220_T1_REGISTROS.txt` Y NO TECLEADA** (6 filas
armadas leyendo ese fichero, y **la cifra que deberia haber es 6**):

| rotulo | adjudicacion | linea del acta 219, LEIDA DEL FICHERO | que se sostiene |
|---|---|---:|---|
| `TAREA 1 D.1` | `4.1` | **77901** | remedir no era recomputar: el mismo instrumento es el mismo instrumento, y el auditor ademas re-corrio mi lector y salio identico |
| `TAREA 1 D.2` | `4.2` | **77907** | no se adjudico por mi palabra: se midio. Sello del sha256 de nueve ficheros, corrida de _v219_t2_lecturas.py, y CERO se movieron. No es la especie de la C.3 de la 218 |
| `TAREA 1 D.3` | `4.3` | **77913** | la glosa es registro y no lectura mia, y decir esto no lo he vuelto a medir yo se cuenta a favor |
| `TAREA 2 D.1` | `4.4` | **77918** | 01 FUENTES idx 1 se sostiene en CUBRE, con la prueba que yo no use: P.19 punto 2 deja el nodo MULTIFUENTE LEGITIMO y sus dos ejemplares nombrados son coeficiente_viral y decision_de_vender_startup, dos de los cinco de mi tabla |
| `TAREA 2 D.2 y P.1` | `4.5` | **77935** | LA FRONTERA ADJUDICADA: el tercero queda FUERA DEL ALCANCE. El punto de verificacion de 05 SANEO idx 1 se acota POR CORRECCION DECLARADA a los dos nodos que OP-S-02 alcanza, y 05 SANEO idx 1 SUBE A CUBRE |
| `TAREA 2 D.3` | `4.6` | **77969** | el reparto de tanda a libro es mio, con su guarda, y decir el limite de la propia guarda es lo contrario de venderla como mordiendo |

**LAS SEIS CAEN DE MI LADO, Y DOS DE ELLAS TRAEN ALGO QUE NO ERA MIO.** La
`4.1` fija que **el mismo instrumento es el mismo instrumento**, y ademas el
auditor re-corrio mi lector y le salio identico, con lo que mi duda queda
contestada por medicion y no por criterio. La `4.2` **no se adjudico por mi
palabra sino por su medicion**: sello nueve `sha256`, corrio el lector y cero se
movieron a su corte. La `4.3` cuenta a favor **decir que algo no lo he vuelto a
medir yo**. La `4.4` refuerza `01 FUENTES` idx 1 **con una prueba que yo no
use**, la del `P.19` punto 2, cuyos **dos ejemplares nombrados son
`coeficiente_viral` y `decision_de_vender_startup`**, dos de los cinco de mi
propia tabla. La `4.5` **adjudica la frontera que yo deje marcada como
discutible**: el tercero queda **FUERA DEL ALCANCE**, no como incumplimiento. Y
la `4.6` acepta el reparto de tanda a libro **con su limite dicho**.

#### 1.b. EL RECUENTO NUEVO, CON LAS DOS CIFRAS JUNTAS Y DICIENDO CUAL ES CUAL

**PRIMERO LA PRUEBA DE QUE EL LECTOR LEE, Y AQUI HAY UN HALLAZGO QUE NO ESTABA
EN NINGUN ENCARGO.** Selle los `sha256` de nueve ficheros, re-corri
`scripts/loop/_v219_t2_lecturas.py` y volvi a medirlos:

- CIFRA ficheros que se movieron al correr el lector: 1 | CIFRA de ellos que NO son la propia salida sellada del lector: 0
- CIFRA lineas en que la salida sellada del lector difiere de la que estaba en disco: 1 | CIFRA que la regla admite: 1 (y solo la del conteo del acta)

**LA UNICA QUE DIFIERE, LEIDA DE MI PROPIA SALIDA Y NO CONTADA DE MEMORIA:**

```
LINEA 157, LA QUE ESTABA> LOS DOS FICHEROS DE LAS CITAS, MEDIDOS HOY: docs/loop/ACTA_AUDITOR.md con 77726 lineas, y docs/PENDIENTES.md con 17347 lineas.
LINEA 157, LA DE HOY>     LOS DOS FICHEROS DE LAS CITAS, MEDIDOS HOY: docs/loop/ACTA_AUDITOR.md con 78126 lineas, y docs/PENDIENTES.md con 17347 lineas.
```

**LAS DOS MEDICIONES SON CIERTAS Y NO SE CONTRADICEN, Y LO DIGO ASI PORQUE LA
OTRA ES DEL AUDITOR.** El acta 219, adjudicacion `4.2` (**linea 77907** de
`docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero), dice que sello nueve
ficheros, corrio ese mismo lector y **CERO se movieron**. Yo mido **UNO**, y es
**su propia salida sellada**. La causa esta medida y no supuesta: **ese lector
imprime el numero de lineas que el acta tiene HOY**, y entre su corrida y la mia
el acta crecio con el acta 219 entera. **Es diferencia de FECHA DE CORTE, no de
conducta del lector**, y por eso la 4.2 sigue en pie tal como esta escrita.

**Y LA SALIDA DE LA 219 SE RESTAURA BYTE A BYTE, PORQUE NO ES MIA PARA
REESCRIBIRLA:** docs/loop/SALIDA_V219_T2_LECTURAS.txt TRAS RESTAURAR: 28878 bytes en disco y 28878 normalizado a LF, sha256 disco f5b55ff575d5af1d y sha256 LF f5b55ff575d5af1d | IDENTICA A LA DE ENTRADA

**MI CORRIDA DE HOY QUEDA SELLADA EN SU PROPIO FICHERO DE LA 220, CON SUS DOS
CONVENCIONES EN LA MISMA LINEA:** ``docs/loop/SALIDA_V220_T1_RECORRIDA_DEL_LECTOR.txt``, **28931 bytes en disco y 28931 normalizado a LF**.

**LA TABLA, PEGADA ENTERA DE `docs/loop/SALIDA_V220_T1_REGISTROS.txt`** (3 filas armadas leyendo ese
fichero, y **la cifra que deberia haber es 3**):

| veredicto | CIFRA que MI LECTOR MIDE HOY, SIN la adjudicacion 4.5 | CIFRA que la ADJUDICACION 4.5 DEJA |
|---|---:|---:|
| **CUBRE** | 14 de 17 | **15 de 17** |
| **A MEDIAS** | 3 de 17 | **2 de 17** |
| **NO CUBRE** | 0 de 17 | **0 de 17** |

**CUAL ES CUAL, DICHO SIN rodeos y con la cifra delante:**

- CIFRA clausulas en CUBRE, MEDIDA HOY POR MI LECTOR SIN LA ADJUDICACION: 14 de 17
- CIFRA clausulas en CUBRE, CON LA ADJUDICACION 4.5 APLICADA: 15 de 17
- CIFRA clausulas en A MEDIAS, MEDIDA HOY POR MI LECTOR SIN LA ADJUDICACION: 3 de 17
- CIFRA clausulas en A MEDIAS, CON LA ADJUDICACION 4.5 APLICADA: 2 de 17
- CIFRA clausulas en NO CUBRE, por las dos: 0 de 17

**Y LAS CIFRAS DEL ENCARGO, CITADAS COMO CONTRASTE Y NO COMO FUENTE:**
Y LAS CIFRAS DEL ENCARGO, CITADAS COMO CONTRASTE Y NO COMO FUENTE: el encargo dice que al cierre de la 219 quedo en 14 CUBRE, 3 A MEDIAS y 0 NO CUBRE, y que con la 4.5 aplicada queda en 15 CUBRE, 2 A MEDIAS y 0 NO CUBRE.
MI MEDICION SIN LA ADJUDICACION CALZA CON EL CONTRASTE: SI
MI COMPUTO CON LA ADJUDICACION CALZA CON EL CONTRASTE: SI

**LAS DOS QUE QUEDAN, CON SU CIFRA:**

- 03 FUSIONES    idx 0 | A MEDIAS  | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
- 07 ADUANA      idx 0 | A MEDIAS  | los cuatro controles mecanicos **corriendo en Gate 0**

CIFRA clausulas que siguen sin cubrir: 2 | CIFRA que el recuento con la adjudicacion exige: 2

- **`03 FUSIONES` idx 0: 71 actos** sin fundir por la lectura ancha, y **SEIS
  fusiones de 19 nodos** por la estrecha.
- **`07 ADUANA` idx 0: el quinto control sin correr.**

**LO QUE NO SE TOCA, Y SE DICE EN VEZ DE HACERSE.**
`docs/plan/08_VERIFICACION.md` **NO SE ESCRIBE**. Su `sha256` al entrar y al
salir esta abajo y coincide por las dos convenciones. **La divergencia sube
nombrada**, que es lo que el acta 219 ya adjudico: son **dos** y no una, la de
la **linea 30** (dice CUATRO controles y su ficha `OP-A-02` dice CINCO) y la de
la **linea 28** (lleva el punto de verificacion de `05 SANEO` idx 1 acotado por
correccion declarada y su texto sin acotar).

#### 1.c. LAS SIETE COSAS QUE SUBEN NOMBRADAS A LA AUDITORIA INTEGRAL

**NO LAS RESUELVO: SOLO TIENEN QUE QUEDAR ESCRITAS DONDE EL FUNDADOR LAS
ENCUENTRE**, que es lo que el encargo pide. La tabla sale de la seccion 6 del
acta 219, que empieza en la linea que el fichero dice: LA SECCION 6 EMPIEZA EN LA LINEA 78024

**LA TABLA, PEGADA ENTERA DE `docs/loop/SALIDA_V220_T1_REGISTROS.txt`** (7 filas armadas leyendo ese
fichero, y **la cifra que deberia haber es 7**):

| # | linea del acta 219 | lo que sube, y su cifra |
|---:|---:|---|
| 1 | **78026** | la familia C.1 del auditor en NUEVE actas seguidas, con TRES mediciones de fallo del remedio del fundador, y SUBE CON TRES OPCIONES concretas |
| 2 | **78039** | DOS divergencias, ya no una, entre la pagina 08 del plan y lo adjudicado: la linea 30 dice CUATRO controles y su ficha OP-A-02 dice CINCO (tercera acta seguida), y la linea 28 lleva desde el acta 219 el punto de verificacion de 05 SANEO idx 1 acotado por correccion declarada y su texto sin acotar |
| 3 | **78044** | el carril del lanzador de la bateria que dice cual tramo toca no distingue la vuelta de las salidas que mira, y hoy responde que no falta ningun tramo; hermano del rotulo de la salida compuesta, que dice VUELTA 183 sobre el contenido de la 215 |
| 4 | **78049** | scripts/loop/vuelta150_4_tabla_por_fase.py en rojo, AssertionError la tabla no trae ocho filas: 11, y queda por decidir si se repara o si su vara de ocho filas se retira |
| 5 | **78053** | la ciega no puede acertar lo que el archivo decide por BARRIDO DE FAMILIA, por transitividad sobre veredictos de otros puestos: NUEVE de los catorce fallos del auditor son de esa especie |
| 6 | **78059** | las DOS clausulas que quedan, con su cifra: 03 FUSIONES idx 0 (71 actos sin fundir por la lectura ancha, SEIS fusiones de 19 nodos por la estrecha) y 07 ADUANA idx 0 (el quinto control sin correr, mas la celda del punto 2) |
| 7 | **78062** | el remedio de dictado de mi C.4, en mis propias palabras: la pareja de bytes no es una regla de RUTAS, es una regla de CIFRAS DE BYTES, vengan de una ruta o de un campo de texto |

**LA 1 SUBE CON TRES OPCIONES, Y ESO ES LO QUE LA HACE DECIDIBLE.** Van
verbatim del acta y no resumidas por mi (CIFRA opciones halladas en el texto del punto 1: 3 | CIFRA que el encargo exige: 3 halladas, y **la cifra que el
encargo exige es 3**):

- OPCION (a), VERBATIM DEL ACTA> que la orden deje de ser texto y pase a ser lo primero que el turno EJECUTA, moviendo los tres comandos de apertura al principio del propio encargo del auditor y no a un fichero que hay que abrir
- OPCION (b), VERBATIM DEL ACTA> levantar la moratoria `6.3` **solo para esta guarda**, para que el turno pueda apuntar los toques que hoy se le escapan por correr fuera de las funciones instrumentadas
- OPCION (c), VERBATIM DEL ACTA> aceptar la caida como coste conocido y **retirar la letra**, porque nueve actas seguidas rompiendo una regla que nunca ha quemado un sujeto dicen o que la regla no se puede cumplir o que protege menos de lo que cuesta. **Yo no elijo, pero digo cual descartaria: la (c) no, mientras nadie mida que el sujeto esta a salvo por otra via.**

**Y LO QUE EL AUDITOR ANADE SOBRE SU PROPIA LISTA, TAMBIEN DEL FICHERO:** dice
que el no elige, pero que **descartaria la (c)** mientras nadie mida que el
sujeto esta a salvo por otra via. **Yo no elijo ninguna: no es mio.**
CIFRA opciones que ESTA VUELTA resuelve: 0 | CIFRA que el encargo ordena resolver: 0

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
- docs/plan/03_FUSIONES.md AL ENTRAR: sha256 disco f06d25b41c587316 y sha256 LF 46c592fa8da942e2
- docs/plan/03_FUSIONES.md AL SALIR:   sha256 disco f06d25b41c587316 y sha256 LF 46c592fa8da942e2, 833308 bytes en disco y 828282 normalizado a LF
- docs/plan/INVENTARIO.jsonl AL ENTRAR: sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a
- docs/plan/INVENTARIO.jsonl AL SALIR:   sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a, 629533 bytes en disco y 629533 normalizado a LF

LOS 14 SHA DE LAS SEDES DEL PLAN COINCIDEN AL ENTRAR Y AL SALIR POR LAS DOS CONVENCIONES: SI

#### LOS DISCUTIBLES DE LA TAREA 1, MARCADOS ANTES DE SABER SI ACIERTO

| # | que decidi | la duda que dejo escrita |
|---|---|---|
| **D.1** | QUE LA CIFRA SIN LA ADJUDICACION SE MIDE RE-CORRIENDO EL LECTOR DE LA 219, Y NO EL DE LA 217 DESDE EL GRAFO | El encargo me pide **las dos cifras juntas**, la que mi lector mide hoy sin la adjudicacion y la que la adjudicacion deja. Yo entiendo *mi lector* como **`scripts/loop/_v219_t2_lecturas.py` tal cual**, que es el que el auditor reprodujo byte a byte. **La duda que dejo escrita antes de saber si acierto**: ese lector recompone el recuento leyendo la tabla de 17 filas de `docs/loop/SALIDA_V219_T1_RECORRIDA_DEL_LECTOR.txt`, o sea **es una remedicion del mismo camino y no una medicion independiente desde el grafo**. Si el auditor lee que la cifra de hoy tenia que salir de re-sondar las diecisiete clausulas contra el grafo, mi 1.b se queda corta. |
| **D.2** | QUE LA SUBIDA DE `05 SANEO` idx 1 SE APLICA EN MI ARITMETICA Y NO EN NINGUN FICHERO DEL PLAN | La `4.5` sube `05 SANEO` idx 1 a CUBRE, y yo la aplico **solo sobre la tabla que el lector imprime**, en memoria, para publicar la segunda cifra. **No toco `docs/plan/08_VERIFICACION.md` ni ninguna ficha**, porque el encargo lo prohibe por su nombre. **La duda**: eso deja el arbol diciendo 14 y mi reporte diciendo 15, y **la divergencia la sostengo yo en prosa**, no un fichero. Si el auditor lee que una adjudicacion suya tenia que quedar escrita en algun sitio del plan, esa escritura no esta y **no la hago yo**: es sede del fundador. |
| **D.3** | QUE EL MOVIMIENTO DE LA SALIDA SELLADA DE LA 219 NO ES UNA CAIDA DE NADIE | Mi guarda midio que **`docs/loop/SALIDA_V219_T2_LECTURAS.txt` se mueve** al re-correr su lector, y el acta 219 dice que a su corte no se movio ninguno. **Lo declaro yo antes de que me lo pregunten.** Mi lectura es que **no es caida de nadie**: la unica linea que cambia es la del conteo de lineas del acta, que crecio porque el auditor escribio la 219 despues de correrlo. **Si el auditor lee que una salida sellada que no reproduce byte a byte es de suyo una caida de dato**, entonces esto es un hallazgo que sube y no una nota, y **el que decide es el**. |

#### EL CASO ROJO, PROBADO POR MUTACION ANTES DE PUBLICARLO

**LA GUARDA QUE ESTA TAREA PUBLICA COMO PRUEBA SALIO EN VERDE EN LA CORRIDA
REAL, Y UN CASO QUE SOLO SE HA VISTO EN VERDE NO ES UNA PRUEBA.**
`scripts/loop/_v220_t1_mutacion.py` le cambia el valor esperado caso por caso
y comprueba que CAE. Su salida vive en ``docs/loop/SALIDA_V220_T1_MUTACION.txt``, **2326 bytes en disco y 2326 normalizado a LF**:

- PRUEBA DE MUTACION DEL CASO ROJO DE LA TAREA 1 DE LA VUELTA 220
- CASO 1 VERDE DE CONTROL: solo la salida propia, y solo la linea del conteo del acta
- EL CASO NO CAE: CALZA
- CASO 2 ROJO POR FICHERO AJENO: se movio ademas una sede del plan
- EL CASO CAE: CALZA
- CASO 3 ROJO POR DOS LINEAS: la salida propia difiere en dos
- EL CASO CAE: CALZA
- CASO 4 ROJO POR OTRA LINEA: una sola, pero no la del conteo del acta
- EL CASO CAE: CALZA
- CIFRA casos que CAEN: 3 de 4
- CIFRA comprobaciones que fallan: 0

EL CASO ROJO, DICHO CUAL ES CUAL: la localizacion de las lineas, la re-corrida del lector, el cotejo de los nueve sha, el cotejo entre las tres lineas de CIFRA y la tabla contada, y la aritmetica de las dos cifras CAEN EN ROJO por si solos y estan contados arriba. LA GLOSA DE CADA ADJUDICACION ES MIA y no tiene nada que mutar: SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO PARA ESA PARTE.
