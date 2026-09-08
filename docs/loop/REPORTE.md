# REPORTE DE LA VUELTA 208 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v208_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se
> hicieron.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, Y ESO ES EL REMIENDO DE MI
> `C.1` DE LA 207.** Aquella vuelta tallo su esqueleto sin la marca de apertura de
> la tabla de tareas, sin la del anexo y sin sus dos cierres, y hubo que ponerselas
> a mano despues con `_v207_marcas_anexo.py`. **Aqui no se teclean: se IMPORTAN de
> `anexar_tarea_al_reporte.py`**, que es el instrumento que las lee, y se comprueba
> ANTES de tallar que es lo que ese instrumento exige. **Las cuatro no se citan
> literalmente en esta prosa a proposito**: la guarda las cuenta sobre el fichero
> entero, y una cita en prosa las duplicaria. Es lo que esta corrida cazo en su
> primer intento, en rojo, y por eso la prosa las nombra en vez de copiarlas.
>
> **EL REPORTE DE LA 207 TAMPOCO ESTABA ARCHIVADO AL ENTRAR, Y ESO SE DECLARA EN
> VEZ DE COPIARSE** (`EJECUTOR.md` 2, EL INSTRUMENTO MANDA). Mi sello de apertura,
> `docs/loop/SALIDA_V208_APERTURA.txt`, escrito **antes de la primera operacion**,
> publica `CIFRA docs/loop/reportes/REPORTE_V207.md existe al entrar: NO`. Lo
> archiva el PASO 0, que es su sitio, y su salida va sellada en
> `docs/loop/SALIDA_V208_PASO0_ARCHIVAR.txt`.
>
> **TRES SUB-TAREAS.** El tope volvio a CINCO (`AUDITOR.md` 6.2, adjudicacion `6.5`
> del acta 207: la 206 y la 207 cerraron las dos su propio reporte con
> `cerrar_reporte.py`), y el encargo pone TRES y no cinco porque la TAREA 2 toca una
> sede sellada del banco.
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA**
> (`AUDITOR.md` 6.1, adjudicacion `6.7` del acta 207). La ultima fue la **205** y
> la siguiente es la **210**. La **seccion 9 cierra igual**, con el **HUECO
> DECLARADO Y MEDIDO** y sus **tres piezas juntas**: el nombre del fichero, los
> bytes medidos **distinguiendo el cero de ausencia del cero de fichero vacio**, y
> la atribucion.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Todo lo que esta vuelta
> escribe son ficheros `_v208_*` **con prefijo de guion bajo, fuera del censo y
> fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda. **EL
> TRABAJO ES EL PLAN**, y por eso las TAREAS 2 y 3 son mesas del plan.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 208`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TRES TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS DE LA VUELTA 207. Leer el acta 207 entera y REMEDIR sus cifras de crecimiento; escribir `R.72` en `docs/PENDIENTES.md` **por adicion pura y en su sede**, con el numero COMPUTADO por `scripts/loop/serie_de_registros.py` y las dos puntas publicadas; registrar **las ocho adjudicaciones** `6.1` a `6.8` por su numero y su linea, con la vara del `4.1` del acta 202 corrida por mi; y CORREGIR LA CAIDA `4.1` DEL AUDITOR CONTRA MI en el reporte ARCHIVADO de la 207, por CORRECCION DECLARADA y con el texto viejo entero encima | **CERRADA** | `SALIDA_V208_T1_REGISTROS.txt`, `SALIDA_V208_T1_REGISTROS_IDEM.txt`, `SALIDA_V208_T1D_CORRECCION.txt`, `SALIDA_V208_SERIE_APERTURA.txt`, `SALIDA_V208_SERIE_CIERRE.txt` |
| **TAREA 2** | LA `TABLA VIVA DE LOS PUROS` DE `docs/BANCO_DE_TEXTOS.md`, PUESTA AL DIA POR EL CARRIL DEL BANCO `9.10`. **Primero el DENOMINADOR** de las dos nominas, recomputado de su nomina de miembros y no de la tabla; despues las dos filas escritas por CORRECCION DECLARADA con el texto viejo entero encima; y la `V.3` de la vara de `OP-L-01` dejada MEDIDA con su cita. **NO SE CIERRA `OP-L-01` Y NO SE TOCA SU CAMPO `estado`** | **CERRADA, CON LAS DOS FILAS ESCRITAS, LA COBERTURA MEDIDA Y LA FICHA SIN CERRAR** | `SALIDA_V208_T2A_DENOMINADOR.txt`, `SALIDA_V208_T2B_TABLA_VIVA.txt`, `SALIDA_V208_T2D_V3.txt`, `SALIDA_V208_T2E_V14.txt` |
| **TAREA 3** | LA MESA `OP-L-03`, MEDIDA CONTRA LOS DOCUMENTOS QUE SU FICHA NOMBRA, POR EL MISMO METODO QUE LA `OP-L-01` DE LA 207. La vara SELLADA EN SU PROPIO COMMIT antes de abrir ningun documento, con cada cita comprobada VERBATIM y el reparto documental sellado antes de mirar; el cotejo punto por punto con CUBRE, A MEDIAS o NO CUBRE **y su cita de fichero y linea**; la cobertura MEDIDA y no narrada. **NO SE CIERRA LA FICHA Y NO SE TOCA SU CAMPO `estado`** | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS DE LA VUELTA 207: `R.72`, LAS OCHO ADJUDICACIONES Y LA CORRECCION DECLARADA DE LA `4.1`

**LO QUE DEJO SELLADO, CON LAS DOS CONVENCIONES EN EL MISMO RENGLON:**

| salida sellada | bytes | exitcode |
|---|---|---:|
| `docs/loop/SALIDA_V208_SERIE_APERTURA.txt` | 9113 bytes en disco y 9025 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_SERIE_CIERRE.txt` | 9252 bytes en disco y 9163 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1_REGISTROS_SECO.txt` | 14269 bytes en disco y 14269 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1_REGISTROS.txt` | 14328 bytes en disco y 14328 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1_REGISTROS_IDEM.txt` | 14279 bytes en disco y 14279 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1D_CORRECCION_SECO.txt` | 3269 bytes en disco y 3269 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1D_CORRECCION.txt` | 3303 bytes en disco y 3303 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1D_CORRECCION_IDEM.txt` | 3287 bytes en disco y 3287 normalizado a LF | 0 |

#### 1.a. EL ACTA 207, LEIDA ENTERA Y CON SUS CIFRAS REMEDIDAS POR MI

**LAS CIFRAS DEL ENCARGO SON CONTRASTE Y LAS REMEDI. LAS SEIS CALZAN AL DIGITO.**

| cifra | el encargo, como contraste | mi medicion de hoy | calza |
|---|---:|---:|---|
| bytes del acta ANTES | 4793964 | 4793964 | SI |
| bytes del acta DESPUES, en disco | 4820516 | 4820516 | SI |
| bytes del acta DESPUES, normalizado a LF | 4820516 | 4820516 | SI |
| bytes anadidos | 26552 | 26552 | SI |
| lineas del fichero | 73081 | 73081 | SI |
| linea donde empieza la seccion del auditor | 72641 | 72641 | SI |

**Y LOS DOS `sha256` TAMBIEN**, leidos de mi sello de apertura: **`0ca61c2ee053dd0d`**
por disco y **`0ca61c2ee053dd0d`** por LF, los mismos dos que el encargo publica.

**EL AVISO MEDIDO DEL ENCARGO LO COMPROBE ANTES DE RESTAR, NO DESPUES.** El
encargo avisa que el acento circunflejo se lo come el shell. Lo mire: en el mio
`git rev-parse 0d9e71a3~1` y `git rev-parse '0d9e71a3^'` devuelven **el mismo**
`bdfbe52555299a6740e8b44d2b2ed7805aeaf2c9`, que **NO** es el hijo
`0d9e71a3f6a540860452afbb4bfc1552f32f11f9`. **Los dos valores son distintos, que
es la condicion que el encargo pide comprobar**, y aun asi la resta la hice con
`~1`.

**LA ADICION PURA NO LA AFIRMO: LA MIDE `git`.**
`git show --numstat 0d9e71a3 -- docs/loop/ACTA_AUDITOR.md` da **442** lineas
anadidas y **0** borradas. El acta 207 abre en la linea **72641** de un fichero de
**73081** lineas, o sea **441** lineas de cuerpo; **la 442.a es la linea en blanco
de la 72640**, que es el separador, y lo digo en vez de dejar la resta coja.

#### 1.b. `R.72`, ESCRITA POR ADICION PURA Y CON EL NUMERO COMPUTADO

**EL NUMERO NO SE TECLEO.** `scripts/loop/serie_de_registros.py` corrido por mi al
entrar y al salir, recomputando la serie de sus DOS sedes:

| punta | entradas | en `PENDIENTES.md` | en `CORRECCIONES_A_APLICAR.md` | colisiones | huecos | mayor | siguiente libre |
|---|---:|---:|---:|---:|---:|---|---|
| AL ENTRAR (`SALIDA_V208_SERIE_APERTURA.txt`) | 63 | 62 | 1 | 0 | 0 | `R.71` | `R.72` |
| AL SALIR (`SALIDA_V208_SERIE_CIERRE.txt`) | 64 | 63 | 1 | 0 | 0 | `R.72` | `R.73` |

**LA PUNTA DE ENTRADA CALZA AL DIGITO CON EL CONTRASTE DEL ENCARGO** (63, 62, 1,
0 colisiones, 0 huecos, mayor `R.71`, siguiente libre `R.72`).

**LA ADICION ES PURA, Y LO MIDE `git`, NO YO:**
`git diff --numstat -- docs/PENDIENTES.md` da **140** lineas anadidas y **0
BORRADAS**. La sede pasa de **1171455** bytes en disco y **1171455** normalizado a
LF a **1180091** y **1180091**, o sea **8636** anadidos, y de **17040** a **17180**
lineas.

**Y LA GUARDA DEL TEXTO VIEJO SE CORRIO ENTERA:** las lineas del texto de ENTRADA
que NO estan, en orden, en el de SALIDA son **0**.

**LA SEGUNDA CORRIDA CRECE 0 BYTES, COMO EL ENCARGO PIDE.**
`SALIDA_V208_T1_REGISTROS_IDEM.txt` publica `NO SE ESCRIBE: la entrada ya estaba.
IDEMPOTENTE.` y `CIFRA crecimiento en bytes de disco: 0` y `CIFRA crecimiento en
bytes LF: 0`. El `numstat` sigue en **140 / 0** despues de la segunda corrida.

#### 1.c. LAS OCHO ADJUDICACIONES, POR SU NUMERO Y CON SU LINEA

**LA VARA DEL `4.1` DEL ACTA 202 LA CORRI YO, CON EL LECTOR IMPORTADO Y SIN
TOCARLE UNA LINEA, Y DA LO MISMO QUE EL ACTA PUBLICA.**

| acta | numerales COMPUTABLES de 4, medidos por mi | el acta 207 en su `7.1`, como contraste | calza |
|---|---:|---:|---|
| **206** | **1** | 1 | SI |
| **207** | **4** | 4 | SI |

**Sobre la 207 la vara saca las cuatro:** adjudicaciones **8**, hallazgos **5**,
caidas del auditor **4** y caidas del ejecutor **1**. **Sobre la 206 saca una
sola:** hallazgos **4**; adjudicaciones y caidas del ejecutor dan seccion hallada
con **0 claves**, y caidas del auditor no tiene seccion que la titule.
**Ninguna discrepancia con el contraste, asi que esto no sube a la `3.0`.**

**LAS OCHO, CON SU LINEA MEDIDA Y CON LO QUE CIERRAN:**

| clave | linea | cierra pendiente | que es |
|---|---:|---|---|
| `6.1` | 72858 | **`P.2`** | una evidencia que no lleva la cobertura al lado no cubre una mesa |
| `6.2` | 72879 | (ninguno) | `OP-L-01` no se cierra, y eso no es una parada |
| `6.3` | 72886 | **`P.3`** | las dos filas las escribe la vuelta 208, con el denominador recomputado primero |
| `6.4` | 72894 | **`PD.1`** | un punto de una vara sellada que aparece del otro lado se corrige por adicion declarada |
| `6.5` | 72906 | **el TOPE de sub-tareas** | vuelve a cinco: el disparador se cumplio |
| `6.6` | 72916 | (ninguno) | la moratoria se respeto, 11 de 11 con prefijo y nomina en 135 |
| `6.7` | 72921 | (ninguno) | la bateria no corre en la 208 |
| `6.8` | 72925 | **`P.1`** | el `3.0.a` no rompe la moratoria y el remedio es como titula el auditor |

**LAS CINCO QUE CIERRAN PENDIENTES QUEDAN DICHAS AL REGISTRARLAS**, dentro de
`R.72`, y el computo cae en rojo si alguna de las cinco no aparece entre las
medidas: `CIFRA de las cinco que cierran pendientes que NO estan entre las
medidas: 0`.

**UN CERO FALSO CAZADO ANTES DE PUBLICARLO, Y ESTE ES MIO.** `REG206.titulo_de()`
cuenta las caidas con `numeral(dato, 'viejas')`, o sea por la forma antigua
`CAIDA n`, y **el acta 207 escribe las suyas como `9.1` a `9.4` y `4.1`**. Corrido
tal cual, el titulo de `R.72` habria dicho **las 0 caidas propias del auditor**
sobre un acta que trae **cuatro**. Lo cace corriendolo, y **no toque el lector**:
le pase a la misma funcion importada el dato contado por la forma que esa acta usa.
**Las dos cuentas van juntas dentro de `R.72` y el titulo crudo queda escrito ahi
entero y sin tachar.** Va como `D.1`.

#### 1.d. LA CAIDA `4.1` DEL AUDITOR CONTRA MI, CORREGIDA POR CORRECCION DECLARADA

**EL AUDITOR TIENE RAZON Y NO LO CORRIJO COPIANDOLE** (`EJECUTOR.md` 2). Las dos
mediciones son mias y las dos dan **7**:

| via | cifra |
|---|---:|
| remedida por mi sobre la linea **41** de `docs/plan/OPERACIONES.jsonl` | **7** |
| leida de la **linea 21** de mi propia salida sellada `docs/loop/SALIDA_V207_T2_VARA.txt` | **7** |
| lo que el reporte de la 207 publicaba | 6 |

Esa linea 21, pegada entera y no parafraseada:
``   CIFRA elementos de `verificacion`: 7``.
**El instrumento midio bien; la transcripcion al reporte perdio uno.**

**LA COBERTURA NO CAMBIA, Y NO LO AFIRMO: LO COMPRUEBA EL COMPUTO.** De los
**7** elementos, **3** son clausulas (indices **0**, **1** y **2**) y **4** son
CORRECCIONES DECLARADAS (indices **3**, **4**, **5** y **6**). `V.12`, `V.13` y
`V.14` salen de `verificacion[0]`, `[1]` y `[2]`, que son justamente las tres
clausulas; **los cuatro que faltaban de contar son las CORRECCIONES DECLARADAS,
que nunca fueron puntos de la vara**. `CIFRA puntos de la vara que se mueven por
esta correccion: 0`. Si el reparto no hubiera sido ese, el computo caia en rojo y
no escribia nada.

**LA CORRECCION ES POR ADICION Y CON EL TEXTO VIEJO ENTERO ENCIMA.** El bloque se
inserta **debajo** del parrafo que falla, en `docs/loop/reportes/REPORTE_V207.md`,
que pasa de **50306** bytes en disco y **50306** normalizado a LF (sha256
`e0d67989e21687ce` por las dos) a **51699** y **51699** (sha256 `231b2df5d3414bf1`
por las dos). `git diff --numstat` da **26** anadidas y **0 BORRADAS**, y las
lineas del texto de entrada que faltan del de salida son **0**.
**Segunda corrida IDEMPOTENTE: 0 bytes de crecimiento.**

**Y LA FICHA SOLO SE LEYO:** `docs/plan/OPERACIONES.jsonl` entra y sale de esta
sub-tarea en **513043** bytes por las dos convenciones, con sha256
`829c583eb779cab6` por disco y `829c583eb779cab6` por LF.

### TAREA 2. LA `TABLA VIVA DE LOS PUROS`, PUESTA AL DIA POR EL CARRIL DEL `9.10`

**LO QUE DEJO SELLADO, CON LAS DOS CONVENCIONES EN EL MISMO RENGLON:**

| salida sellada | bytes | exitcode |
|---|---|---:|
| `docs/loop/SALIDA_V208_T2A_DENOMINADOR.txt` | 11634 bytes en disco y 11634 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2B_TABLA_VIVA_SECO.txt` | 4447 bytes en disco y 4447 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2B_TABLA_VIVA.txt` | 4592 bytes en disco y 4592 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2D_COTEJO_REPETIDO.txt` | 10767 bytes en disco y 10622 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2D_V3.txt` | 5403 bytes en disco y 5403 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2E_V14.txt` | 3492 bytes en disco y 3492 normalizado a LF | 0 |

#### 2.a. EL DENOMINADOR PRIMERO, RECOMPUTADO DE LA NOMINA DE MIEMBROS

**EL ORDEN NO ERA DE ADORNO Y LA MEDICION LO CONFIRMA.** Los pares posibles se
contaron de la **nomina de miembros** de cada familia, en
`docs/INTRA_DOMINIO_INFORME.md`, y **no de la tabla**, con el resolutor puesto
(`P.1`): **3853** ficheros de nodo leidos, **761** alias en el mapa y **3853**
`node_id` distintos en disco.

| nomina | miembros recomputados | posibles recomputados | posibles segun la tabla viva | posibles segun la mesa | veredicto |
|---|---:|---:|---:|---:|---|
| junta asesora | **4** | **6** | 6 | 6 | LAS TRES CALZAN |
| seleccion de canal | **6** | **15** | 15 | **10** | **LA TABLA CALZA, LA MESA NO** |

**Y EL HALLAZGO `7.2` DEL ACTA 207 QUEDA CONFIRMADO CON SU CAUSA MEDIDA, QUE ES
LO QUE FALTABA.** El **10** de la mesa sale de su tabla por nomina,
`docs/plan/LECTURAS_DIRIGIDAS.md:31`, que cuenta **5 miembros**. La nomina de esa
familia, verificada contra el grafo en `docs/INTRA_DOMINIO_INFORME.md:5313` y
enumerada de la **5314** a la **5319**, tiene **SEIS**, y lleva una **CORRECCION
DECLARADA del 11 ago 2026** en la linea **5321** que dice literalmente *"son SEIS
y no cinco"*. **La mesa cuenta sobre el universo anterior a esa correccion.**

**LOS LEIDOS TAMPOCO SE HEREDAN.** De las **27** cabeceras `LD` que hay hoy en el
documento de la mesa, las que tienen **los dos extremos dentro de la nomina tras
resolver** son **1** en la junta asesora (`LD-01`, **D**) y **2** en la seleccion
de canal (`LD-02` **D** y `LD-03` **A**).

| nomina | leidos que la tabla lleva hoy | mas las LD de la mesa | sobre el denominador recomputado | cobertura |
|---|---:|---:|---|---|
| junta asesora | 5 | **6** | **6 de 6** | **COMPLETA** |
| seleccion de canal | 8 | **10** | **10 de 15** | **INCOMPLETA, o sea PROVISIONAL** (banco `9.26`) |

**Y AQUI ESTA LO QUE CAMBIA LA RESPUESTA DE LA MESA, Y NO LO RESUELVO COPIANDO**
(`EJECUTOR.md` 2). La mesa declara en `docs/plan/LECTURAS_DIRIGIDAS.md:291` que
la seleccion de canal queda en *"10 de 10, cobertura COMPLETA"*. **Sobre el
denominador recomputado es 10 de 15 y NO es completa.** Las dos cifras quedan
escritas y ninguna se elige en silencio. **De las DOS nominas que la mesa declara
con cobertura COMPLETA, sobre el denominador recomputado solo UNA lo esta.**

**UNA SEGUNDA CUENTA QUE NADIE PEDIA Y QUE APARECIO AL PONER EL RESOLUTOR, Y LA
DECLARO PORQUE ES MIA Y NO DEL ENCARGO.** Los **4** miembros de la junta asesora
son **2** nodos distintos **tras resolver**: `identificar_junta_asesores` resuelve
hoy a `identificar_consejo_asesores`, y `formalize_advisory_board` a
`formalizar_junta_asesora`. En esa convencion los pares posibles son **1** y no
**6**. **Es HUELLA DE FUSION**, que es como la propia ficha `OP-L-01` llama a este
mismo fenomeno: la campana fundio dos de los cuatro **despues** del `fecha_corte`
de la ficha. **Las columnas de la tabla cuentan en LITERAL**, con los ids tal como
la nomina los escribe, y por eso el cotejo va contra la convencion literal; **la
resuelta se publica al lado y no sustituye a ninguna**. En la seleccion de canal
las dos convenciones dan lo mismo, **15**, y **0** miembros fundidos.

#### 2.b. LAS DOS FILAS, ESCRITAS POR ADICION Y CON CORRECCION DECLARADA

**NINGUNA DE LAS ONCE CIFRAS DE LAS DOS FILAS SE TECLEO:** el computo que las
escribe las **lee de la salida del 2.a** y cae en rojo si no puede leer una.

Las dos filas corregidas, pegadas enteras de la salida del instrumento:

| # | racimo | miembros | pares posibles | leidos | en A |
|---:|---|---:|---:|---:|---:|
| **7** | la junta asesora (fila corregida) | **4** | **6** | **6** | **4** |
| **11** | la seleccion de canal (fila corregida) | **6** | **15** | **10** | **9** |

La **7** queda **MEZCLADO con COBERTURA COMPLETA, 6 de 6**, cerrada por `LD-01`
(**D**, `docs/plan/LECTURAS_DIRIGIDAS.md:76`), que es el par que nunca entro a la
cola; **la clase no cambia, ya era MEZCLADO por el puesto 1190**. La **11** pasa
de **SUB-PURO** a **MEZCLADO**, porque `LD-02` (**D**, linea **95**) mete el
primer `D` dentro de la nomina y el sub-puro cae, y su cobertura queda en
**10 de 15, INCOMPLETA y por tanto PROVISIONAL**, con `LD-03` (**A**, linea
**112**) sumando el otro par.

**LA MARCA `(FILA CORREGIDA EN LA VUELTA 208)` EN LA CELDA DE RACIMO NO ES
ADORNO, Y LA CAZO LA PROPIA GUARDA.** Sin ella, la fila corregida de la junta
asesora empezaba con el mismo texto que la vieja, la guarda del cierre contaba
**dos** apariciones del ancla y no podia distinguir el texto viejo del nuevo. Se
vio corriendo el computo, no razonandolo.

#### 2.c. LAS DOS CONVENCIONES, ANTES Y DESPUES, Y CERO LINEAS BORRADAS

| momento | bytes en disco | bytes normalizado a LF | sha256 disco | sha256 LF |
|---|---:|---:|---|---|
| ANTES | 182228 | 182228 | `68557cd00a3124f4` | `68557cd00a3124f4` |
| DESPUES | 186490 | 186490 | `8adbd60239509bb4` | `8adbd60239509bb4` |

**LAS CUATRO CIFRAS DE ANTES CALZAN AL DIGITO CON EL CONTRASTE DEL ENCARGO.**
El fichero crece **4262** bytes por las dos convenciones y pasa de **3119** a
**3185** lineas.

**`git diff --numstat` da 66 lineas ANADIDAS y 0 BORRADAS.** El encargo dice que
borrar una sola linea de texto viejo es rojo: **son cero**. Y la guarda propia lo
mide por su lado: las lineas del texto de entrada que **no estan, en orden**, en
el de salida son **0**; las dos filas viejas siguen apareciendo **una vez cada
una**, ahora en las lineas **970** y **974**; y la cabecera con su corte de
**14 ago 2026** sigue entera.

**EL CORTE SE ACTUALIZA POR ADICION Y NO PISANDO LA CABECERA, Y ESO VA MARCADO
COMO DISCUTIBLE `D.2`.** El encargo dice que el corte de la tabla se actualiza
tambien; el 2.c dice que borrar una linea vieja es rojo. **Las dos cosas juntas
solo se pueden cumplir anadiendo:** debajo de la cabecera va un **puntero** que
declara que hay una correccion posterior con corte **7 sep 2026** y a que filas
toca, y la cabecera vieja no se toca ni se tacha.

**LO QUE ESTA CORRIDA ESCRIBIO NO TRAE NI UN GUION LARGO NI UNO MEDIO:** puntero
**0** y **0**, bloque **0** y **0**, medidos antes de escribir. El fichero entero
tenia **22** guiones largos y **1** medio al entrar, **todos del texto viejo**, y
no se toco ninguno.

#### 2.d. LA `V.3`, DEJADA MEDIDA PARA QUE EL AUDITOR LA CIERRE EN LA 209

**NO CIERRO `OP-L-01` Y NO TOQUE SU CAMPO `estado`.** `docs/plan/OPERACIONES.jsonl`
sale de esta tarea en **513043** bytes en disco y **513043** normalizado a LF, con
sha256 `829c583eb779cab6` por disco y `829c583eb779cab6` por LF, **identico al de
mi apertura**.

**TRES LECTURAS, Y NINGUNA SE ELIGE EN SILENCIO:**

| lectura | criterio | veredicto de la `V.3` | cita |
|---|---|---|---|
| **(1)** el instrumento sellado de la 207, corrido tal cual | toma la PRIMERA fila que case, y esa es la VIEJA | **A MEDIAS** | `docs/loop/SALIDA_V208_T2D_COTEJO_REPETIDO.txt` |
| **(2)** el mismo criterio, sobre las filas CORREGIDAS | `leidos` igual a `posibles` en las DOS nominas | **A MEDIAS** | `docs/BANCO_DE_TEXTOS.md:999` y `:1000` |
| **(3)** el criterio de la adjudicacion `6.1` del acta 207 | la cobertura ESCRITA al lado, con su motivo, y lo incompleto dicho PROVISIONAL | **CUBRE** | `docs/BANCO_DE_TEXTOS.md:999` y `:1000` |

**LA (1) HAY QUE LEERLA CON SU DEFECTO DELANTE, Y ES UN HALLAZGO MIO.** Corri el
instrumento sellado de la 207 sin tocarle una linea y sigue diciendo *"de las 2
nominas que la mesa declara con cobertura COMPLETA, 2 siguen sin cerrar"*. **Esa
frase ya no es cierta entera**: la junta asesora SI cierra en su fila corregida.
La causa esta medida: su busqueda toma `fila_ban[0]`, **la primera fila cuya celda
de nombre case**, y una correccion por adicion deja **dos** filas por nomina.
**El instrumento lee la vieja.** No lo ensancho, porque rige la moratoria: lo
declaro y va a la seccion 3.0.

**LO QUE LAS TRES LECTURAS TIENEN EN COMUN, Y ES LO UNICO QUE NO SE DISCUTE: la
tabla AHORA LLEVA EL EFECTO DE LA MESA**, que es exactamente lo que no llevaba y
lo que dejaba la `V.3` en `A MEDIAS`. **Lo que queda por adjudicar es si una
cobertura que la propia fila declara PROVISIONAL cubre el punto o no**, y esa
letra es del auditor.

**MI PROPUESTA, Y PARO AHI:** por la lectura (3), que es la del criterio que la
`6.1` escribio, la `V.3` pasa a **CUBRE** y `OP-L-01` queda en **11 de 11**.
**No la cierro yo.**

#### 2.e. LA `V.14`, CORREGIDA POR ADICION Y NO REHECHA

**EL SELLO NO SE REESCRIBE Y LO MIDE EL `sha256`.**
`scripts/loop/_v207_t2_vara.py` entra y sale de esta tarea en **10846** bytes en
disco y **10846** normalizado a LF, con sha256 `e5e1c0904ea135b2` por las dos
convenciones. Sigue diciendo, verbatim, que la `V.14` *"es una CLAUSULA DE
VERIFICACION contra las nominas del inventario, que NO viven en ninguno de los
tres"*.

**Y ESA SEDE SI EXISTE, MEDIDA HOY.** La cobertura de esas nominas vive en la
`TABLA VIVA DE LOS PUROS`, que abre en `docs/BANCO_DE_TEXTOS.md:938`, **que es
uno de los tres documentos de la evidencia**. Las **2** filas que esta vuelta
corrige estan en las lineas **999** y **1000**, y **las 2 llevan la palabra
COBERTURA escrita**. **La `V.14` es DOCUMENTAL y su sede es
`docs/BANCO_DE_TEXTOS.md`.**

**LAS CUENTAS, PUBLICADAS JUNTAS, QUE ES LO QUE LA `6.4` PIDE:**

| cuenta | cifra | cuales |
|---|---:|---|
| **la del SELLO**, que no se reescribe | **10** | `V.1`, `V.2`, `V.3`, `V.5`, `V.6`, `V.7`, `V.8`, `V.9`, `V.10`, `V.11` |
| **la de los VEREDICTOS de hoy**, leida del fichero de salida | **11** | las diez de arriba mas `V.4` |
| **la que esta declaracion anade**, y que el instrumento no puede ver porque lee el sello | **12** | las once de arriba mas `V.14` |

**LA ASIMETRIA SE DECLARA Y NO SE ARREGLA MOVIENDO EL SELLO.** Mover un punto de
lado despues de mirar es exactamente lo que sellar el reparto viene a impedir, y
la `6.4` lo adjudico asi con todas las letras. **Es la misma especie que la `D.2`
de la 207 con la `V.4`, y por eso se trata igual.**

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

