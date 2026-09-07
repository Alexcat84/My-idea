# REPORTE DE LA VUELTA 207 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v207_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE; y el cierre lo talla entero
> `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se corta, las filas que sigan
> diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VEZ EL ESQUELETO SI VA PRIMERO, Y LA 206 NO PUDO.** La `C.2` del reporte
> de la 206 y su `P.3` decian que `docs/loop/REPORTE.md` era el sujeto que su
> TAREA 1 tenia que cerrar. Aqui no lo es, asi que el esqueleto se talla antes de
> tocar nada, que es lo que la casa manda.
>
> **PERO EL REPORTE DE LA 206 NO ESTABA ARCHIVADO, CONTRA LO QUE EL ENCARGO DICE,
> Y ESO SE DECLARA EN VEZ DE COPIARSE** (`EJECUTOR.md` 2, EL INSTRUMENTO MANDA).
> Mi sello de apertura, `docs/loop/SALIDA_V207_APERTURA.txt`, escrito **antes de
> la primera operacion**, publica `CIFRA docs/loop/reportes/REPORTE_V206.md existe
> al entrar: NO`. El encargo dice *"el reporte de la 206 ya esta cerrado y
> archivado"*. **Cerrado si, archivado no.** Lo archiva el PASO 0 de este mismo
> esqueleto, que es su sitio, y la salida va sellada.
>
> **DOS SUB-TAREAS Y NINGUNA MAS** (`AUDITOR.md` 6.2, adjudicacion `6.6` del acta
> 206: la racha de cierres esta en UNA y el tope de cinco todavia no vuelve).
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA**
> (`AUDITOR.md` 6.1, adjudicacion `6.7` del acta 206). La ultima fue la **205** y
> la siguiente es la **210**. La **seccion 9 cierra igual**, con el **HUECO
> DECLARADO Y MEDIDO** y sus **tres piezas juntas**: el nombre del fichero, los
> bytes medidos **distinguiendo el cero de ausencia del cero de fichero vacio**, y
> la atribucion.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Todo lo que esta
> vuelta escribe son ficheros `_v207_*` **con prefijo de guion bajo, fuera del
> censo y fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda.
> **EL TRABAJO ES EL PLAN**, y por eso la TAREA 2 es una mesa del plan.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 207`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS DE LA VUELTA 206. Leer el acta 206 entera y REMEDIR sus cifras de crecimiento; escribir `R.71` en `docs/PENDIENTES.md` **por adicion pura y en su sede**, con el numero COMPUTADO por `scripts/loop/serie_de_registros.py` y las dos puntas publicadas; registrar **las seis adjudicaciones** del acta 206 por su numero; y corregir **las dos caidas de reporte** (`E.1` y `E.2`) en el reporte ARCHIVADO de la 206, por CORRECCION DECLARADA y con el texto viejo entero encima | **CERRADA** | `SALIDA_V207_T1_REGISTROS.txt`, `SALIDA_V207_T1_REGISTROS_IDEM.txt`, `SALIDA_V207_T1D_CORRECCIONES.txt`, `SALIDA_V207_SERIE_APERTURA.txt`, `SALIDA_V207_SERIE_CIERRE.txt` |
| **TAREA 2** | EL PLAN. LA MESA `OP-L-01`, LEIDA CONTRA LOS TRES DOCUMENTOS QUE SU PROPIA FICHA NOMBRA. La vara se escribe ANTES de abrir ningun documento; cada punto lleva su fila con CUBRE, A MEDIAS o NO CUBRE y **su cita con fichero y linea**; la cobertura se publica MEDIDA y no narrada. **NO SE CIERRA LA FICHA Y NO SE TOCA EL CAMPO `estado`** | **CERRADA, CON LA COBERTURA PUBLICADA Y LA FICHA SIN CERRAR** | `SALIDA_V207_T2_VARA.txt` (sellada en `d7ab4545`), `SALIDA_V207_T2_COTEJO.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS DE LA VUELTA 206: `R.71`, LAS OCHO ADJUDICACIONES Y LAS DOS CORRECCIONES DECLARADAS

**LO QUE DEJO SELLADO, CON LAS DOS CONVENCIONES EN EL MISMO RENGLON:**

| salida sellada | bytes | exitcode |
|---|---|---:|
| `docs/loop/SALIDA_V207_T1_REGISTROS.txt` | 9971 bytes en disco y 9971 normalizado a LF | 0 |
| `docs/loop/SALIDA_V207_T1_REGISTROS_SECO.txt` | 9912 bytes en disco y 9912 normalizado a LF | 0 |
| `docs/loop/SALIDA_V207_T1_REGISTROS_IDEM.txt` | 9922 bytes en disco y 9922 normalizado a LF | 0 |
| `docs/loop/SALIDA_V207_T1D_CORRECCIONES.txt` | 3963 bytes en disco y 3963 normalizado a LF | 0 |
| `docs/loop/SALIDA_V207_SERIE_APERTURA.txt` | 8974 bytes en disco y 8887 normalizado a LF | 0 |
| `docs/loop/SALIDA_V207_SERIE_CIERRE.txt` | 9113 bytes en disco y 9025 normalizado a LF | 0 |
| `docs/loop/SALIDA_V207_MARCAS_ANEXO.txt` | 1865 bytes en disco y 1865 normalizado a LF | 0 |

#### 1.a. EL ACTA 206, LEIDA ENTERA Y CON SUS CIFRAS REMEDIDAS POR MI

**LAS CIFRAS DEL ENCARGO SON CONTRASTE Y LAS REMEDI, Y LAS TRES CALZAN AL
DIGITO.** Comando: `git show 3e523b74^:docs/loop/ACTA_AUDITOR.md | wc -c` y su
pareja sin el acento circunflejo.

| cifra | el encargo, como contraste | mi medicion de hoy | calza |
|---|---:|---:|---|
| bytes del acta ANTES | 4771842 | 4771842 | SI |
| bytes del acta DESPUES | 4793964 | 4793964 | SI |
| bytes anadidos | 22122 | 22122 | SI |

**Y LA ADICION PURA NO LA AFIRMO: LA MIDE `git`.**
`git show --numstat 3e523b74 -- docs/loop/ACTA_AUDITOR.md` da **360** lineas
anadidas y **0** borradas. El acta 206 empieza en la linea **72281** de un
fichero de **72639** lineas, o sea que el texto viejo sigue entero delante.

**EL FICHERO, POR LAS DOS CONVENCIONES**, medido en mi sello de apertura antes
de la primera operacion: **4793964** bytes en disco y **4793964** normalizado a
LF, sha256 disco `9375748c02fd26b7` y sha256 LF `9375748c02fd26b7`.

#### 1.b. `R.71`, ESCRITA POR ADICION PURA Y CON EL NUMERO COMPUTADO

**EL NUMERO NO SE TECLEO.** `scripts/loop/serie_de_registros.py` corrido por mi
al entrar y al salir, recomputando la serie de sus DOS sedes:

| punta | entradas | colisiones | huecos | mayor | siguiente libre |
|---|---:|---:|---:|---|---|
| AL ENTRAR (`SALIDA_V207_SERIE_APERTURA.txt`) | 62 | 0 | 0 | `R.70` | `R.71` |
| AL SALIR (`SALIDA_V207_SERIE_CIERRE.txt`) | 63 | 0 | 0 | `R.71` | `R.72` |

**LA PUNTA DE ENTRADA CALZA AL DIGITO CON EL CONTRASTE DEL ENCARGO** (62, 0, 0,
`R.70`, `R.71`).

**LA GUARDA DE ADICION PURA, CON SUS DOS MEDIDAS:**

| guarda | cifra |
|---|---:|
| `git diff --numstat -- docs/PENDIENTES.md`, lineas anadidas | 146 |
| `git diff --numstat -- docs/PENDIENTES.md`, lineas BORRADAS | 0 |
| lineas del texto de ENTRADA que no estan, en orden, en el de SALIDA | 0 |
| crecimiento de la SEGUNDA corrida, en bytes | 0 |
| entradas escritas por la SEGUNDA corrida | 0 |

`docs/PENDIENTES.md` pasa de **1161546** bytes en disco y **1161546**
normalizado a LF (sha256 LF `f933b87fcbd7ba12`) a **1171455** y **1171455**
(sha256 LF `c2129e11ec925f1f`). La entrada mide **9908** bytes.

**LA PRUEBA POR MUTACION DEL ENSANCHE CORRIO OTRA VEZ ANTES DE ESCRIBIR NADA**,
porque es el mismo fichero importado y no se hereda un verde de otra corrida:
`CIFRA casos: 9 | verdes: 9 | rojos: 0`, y `CIFRA casos que CAEN con el esperado
mutado: 9 de 9`. Contado de `docs/loop/SALIDA_V207_T1_REGISTROS.txt`.

#### 1.b.1 LA VARA DEL `4.1` NO ALCANZA SOBRE UN ACTA MODERNA, Y ESO SE MIDE

**ESTA ES LA CIFRA QUE MAS ME COSTO Y LA QUE SUBE COMO HALLAZGO.** `R.69` y
`R.70` registraron actas ANTERIORES a la 184. El acta 206 es POSTERIOR, escribe
sus claves con comillas inversas, y aun asi **CUATRO de los cinco numerales
salen vacios o apuntando a otra seccion**, no por el acta sino por las marcas de
titulo del lector. Contado de `docs/loop/SALIDA_V207_T1_REGISTROS.txt`:

| numeral | lo que la VARA da | lo que hay de verdad, medido | por que |
|---|---|---|---|
| adjudicaciones | **0**, sobre la seccion **5** | **8**, `6.1` a `6.8`, seccion **6** | `MARCAS["adjudicaciones"]` es `("ADJUDICACIONES", "LA ADJUDICACION")` y casa con la seccion 5, *"LA ADJUDICACION 5.3 DEL ACTA 205 ES FALSA"*, que es la correccion de una adjudicacion vieja. La seccion real se titula `LO QUE ADJUDICO` y ninguna marca la nombra |
| hallazgos | **4** | **4**, `7.1` a `7.4` | calza, y es el unico que calza |
| caidas propias del auditor | (ninguna seccion) | **3**, `C.1` a `C.3`, seccion **9** | sus marcas son `MIS CAIDAS PROPIAS` y `MIS PROPIAS CAIDAS`, y el acta titula `MIS CAIDAS, CON SU NOMBRE` |
| caidas del ejecutor | **0** por las TRES formas | **2**, `E.1` y `E.2`, seccion **4** | la seccion SI se encuentra, pero sus claves son `E.n` y las tres formas miran `4.M`, `CAIDA n` y el lead en negrita |
| preguntas | **0** y *"la seccion de PREGUNTAS aparece 0 veces"* | **3**, `P.1` a `P.3` | el patron de `preguntas_del_reporte()` exige la palabra pegada al numero y el articulo `LAS` se lo rompe (acta 204 `4.4`, linea **196**) |

**NINGUNO DE ESOS CEROS SE PUBLICO COMO UN HECHO DEL MUNDO** (`EJECUTOR.md` 9).
`R.71` los DECLARA no computables uno a uno con su motivo medido, publica la
lectura cruda de la vara al lado y pone el reparto medido DEBAJO, marcado como
MEDICION y no como numeral (acta 204 `4.6`). **NO SE TOCO NI UNA LINEA DE CODIGO
DE NINGUN LECTOR:** rige la moratoria, y lo unico que mi computo cambia es a que
seccion y a que prefijo de clave se apunta el MISMO lector importado.

#### 1.c. LAS ADJUDICACIONES, REGISTRADAS POR SU NUMERO

**EL ENCARGO DICE SEIS Y MI MEDICION DICE OCHO, Y LA DISCREPANCIA SE DECLARA EN
VEZ DE RESOLVERSE COPIANDO** (`EJECUTOR.md` 2). El encargo enumera `6.2` a `6.7`
en su punto 1.c y nombra la `6.8` aparte dentro de su TAREA 2; la `6.1` no la
enumera. **Contadas del acta con el lector importado, son 8.** Las ocho van con
su linea dentro de `R.71`, y aqui van las tres que cierran pendientes que venian
arrastrandose:

| clave | linea del acta | que cierra | con que |
|---|---:|---|---|
| `6.2` | 72488 | mi `P.2` | el `exit 3221225794` es `0xc0000142`, un proceso que NO ARRANCO, o sea un hecho que el instrumento no midio. **La cuenta se parte: 4 que corrieron y no mordieron, mas 1 que no corrio** |
| `6.3` | 72498 | mi `P.3` | con medicion: `cerrar_reporte.py` **no tiene ningun argumento de ruta**, asi que el cierre tardio solo puede hacerse sobre `docs/loop/REPORTE.md`. **Mi `C.2` de la 206 NO cuenta como caida** |
| `6.4` | 72509 | mi `PD.1` | una columna de apertura reconstruida vale si y solo si la propia celda publica que es reconstruccion, con su commit y su prueba |
| `6.5` | 72517 | mi `PD.2` | **importar no es clonar**, como letra general |
| `6.6` | 72525 | (ninguna) | el tope sigue en DOS sub-tareas: la racha esta en UNA |
| `6.7` | 72530 | (ninguna) | la bateria no corre en la 207; la siguiente es la 210 |
| `6.1` | 72472 | (ninguna) | la parada de mi `3.0` es cierta y NO es condicion de parada; las cinco van a la integral |
| `6.8` | 72534 | (ninguna) | las fichas reales son CUATRO y no tres, y la omision era de las actas 203 y 204 |

**LAS TRES PREGUNTAS DE MI REPORTE DE LA 206 QUEDAN CONTESTADAS, Y ESO SE MIDE:**
`P.1` en el cuerpo de la `6.1`, `P.2` en el de la `6.2` y `P.3` en el TITULO de
la `6.3`. **Por la via del `4.7` del acta 201 solo la `P.3` cuenta**, porque es
la unica que un titulo nombra, y las dos cifras quedan escritas en `R.71` sin
elegir una en silencio.

#### 1.d. LAS DOS CAIDAS DE REPORTE, CORREGIDAS EN EL REPORTE ARCHIVADO DE LA 206

**CORRECCION DECLARADA, LAS DOS, CON EL TEXTO VIEJO ENTERO ENCIMA**
(`EJECUTOR.md` 8). Sede: `docs/loop/reportes/REPORTE_V206.md`, que pasa de
**38335** bytes en disco y **38335** normalizado a LF (sha256 disco
`87e5be03f5773616` y sha256 LF `87e5be03f5773616`) a **41867** y **41867**
(sha256 disco `672a1046012af2f9` y sha256 LF `672a1046012af2f9`).
`git diff --numstat` da **57** lineas anadidas y **0** borradas, y las lineas del
texto de entrada que no estan, en orden, en el de salida son **0**.

**`E.1`, MEDIDA POR MI Y NO COPIADA**, como el encargo manda expresamente.
`docs/loop/SALIDA_V206_NO_MORDIO.txt` mide **4151** bytes en disco y **4103**
normalizado a LF; sha256 de disco `f38bd7855d7760b5` y sha256 LF
`cffa5cd0724d0427`. **Son distintos**, y la propia linea corregida ya lo probaba
sin saberlo: 4151 contra 4103 solo sale de que el fichero tiene `CRLF`, y
entonces los dos sha no pueden coincidir. Los dos completos van dentro de la
correccion. **La cifra de bytes era correcta; el sha de disco era el de LF
escrito dos veces.**

**`E.2`, CON LA FUENTE CORRECTA Y NO CON EL FICHERO DE HOY.** Aqui es donde la
regla `1.e` del encargo, que es el hallazgo `7.3` del acta 206, cambia el
resultado:

| fuente | bytes | sha256 LF | celdas | APERTURA | CIERRE | SIN LADO |
|---|---|---|---:|---:|---:|---:|
| `git show 78ca7176:...RECHAZO.txt`, **lo que la 205 SELLO** | 3188 bytes en disco y 3188 normalizado a LF | `b9df894ff422dc77` | **39** | **19** | **19** | **1** |
| el mismo nombre HOY en disco, escrito por la 206 en `a75ff760` | 1922 bytes en disco y 1922 normalizado a LF | `254c2257ae55a0f2` | **19** | **18** | **1** | **0** |

**El `19 / 18` del `D.1` sale de la fila de abajo, no de la de arriba.** Se
corrige LA PROCEDENCIA y no el hecho: la conclusion del `D.1` se sostiene, y el
propio acta 206 la verifico aparte midiendo que los seis
`SALIDA_V205_*_APERTURA.txt` se anaden una sola vez en toda la historia de git y
es en `a75ff760`. **La historia de `git log` sobre ese fichero tiene DOS commits,
`a75ff760` y `78ca7176`, y esa es la prueba de que se volvio a correr.**

**LA SEGUNDA CORRIDA DE LAS CORRECCIONES NO ESCRIBE NADA:** crecimiento **0**
bytes, por el literal de la marca. **NINGUNA DE LAS DOS ACUMULA**, por la letra
afinada del 27 ago 2026 que el propio acta 206 cita.

#### 1.e. LA REGLA DE LA SALIDA SELLADA, APLICADA Y NO SOLO CITADA

**Una salida sellada que una vuelta posterior vuelve a correr deja de ser
evidencia de la vuelta que la sello.** La use en la `E.2` y la volvi a usar sobre
`SALIDA_V206_NO_MORDIO.txt`: corri `git log` sobre el fichero **antes** de citarlo
y sale **un solo commit**, `a75ff760`, o sea que nadie lo volvio a correr y el
fichero de hoy SI es evidencia de la 206. **La regla no solo prohibe: tambien
permite cuando la medicion lo sostiene.**

#### LA DEUDA DE REGISTROS, REMEDIDA AL CIERRE Y ENSANCHADA HASTA LA 206

La deuda del `4.9` del acta 201 (actas 173 a 180) sigue en **0**, y esa la agoto
la vuelta 206. **Lo que mido yo, ensanchando la ventana hasta la 206**, contado
de `docs/loop/SALIDA_V207_T1_REGISTROS.txt`:

| ventana | actas SIN entrada propia | cuales |
|---|---:|---|
| 173 a 206, ANTES de escribir `R.71` | 6 | 201, 202, 203, 204, 205, 206 |
| 173 a 206, DESPUES de escribir `R.71` | 5 | 201, 202, 203, 204, 205 |

**NO LA CIERRO NI LA ENCARGO: la mido y la subo.** Encargar es del auditor.

### TAREA 2. LA MESA `OP-L-01`, LEIDA CONTRA LOS TRES DOCUMENTOS QUE SU PROPIA FICHA NOMBRA

**LO QUE DEJO SELLADO, CON LAS DOS CONVENCIONES EN EL MISMO RENGLON:**

| salida sellada | bytes | exitcode |
|---|---|---:|
| `docs/loop/SALIDA_V207_T2_VARA.txt` | 6533 bytes en disco y 6533 normalizado a LF | 0 |
| `docs/loop/SALIDA_V207_T2_COTEJO.txt` | 10620 bytes en disco y 10620 normalizado a LF | 0 |

#### 2.a. LA VARA, ESCRITA Y SELLADA ANTES DE ABRIR NINGUN DOCUMENTO

**VA EN SU PROPIO COMMIT, `d7ab4545`, Y ESE ES EL PUNTO.** Una vara escrita
despues de mirar se acomoda a lo que se vio, y la unica forma de probar que la
mia no se acomodo es que exista en git ANTES del commit que abre los documentos.

**CATORCE PUNTOS, `V.1` A `V.14`, CADA UNO CON LA CITA LITERAL DEL CAMPO Y DEL
ELEMENTO DE LA FICHA DEL QUE SALE**, y **las catorce citas comprobadas VERBATIM
por el propio computo contra la ficha**: `CIFRA citas que NO aparecen verbatim: 0`.
Si una sola no hubiera aparecido, el computo caia en rojo y no sellaba nada.

**LA SEDE FINA ES `campo[indice]` Y NO UN NUMERO DE LINEA**, y se dice por que:
la ficha entera vive en **UNA sola linea** de `docs/plan/OPERACIONES.jsonl`, la
**41**. Decir *"linea 41"* catorce veces no localiza nada.

**LA FICHA, MEDIDA:** **18** campos, **4** elementos de `evidencia`, **6** de
`verificacion` de los cuales **4** son CORRECCIONES DECLARADAS, `fecha_corte`
**2026-08-11**, `depende_de` vacio (**0**) y `bloquea_a` vacio (**0**), que es
justo por lo que el encargo la elige primera de las cuatro.

**EL CAMPO `estado` SE LEE COMO DATO Y NO SE TOCA** (`AUDITOR.md` 0): dice
`LISTA`. No lo levante, no lo baje y no lo mire para decidir nada.

**Y EL REPARTO TAMBIEN SE SELLO ANTES DE MIRAR**, que es la mitad que suele
faltar: **10** puntos declarados documentales y **4** declarados NO documentales
con su motivo escrito. Si el cotejo hubiera querido mover un punto de un lado al
otro despues de ver los documentos, el sello lo delataria.

#### 2.b. EL COTEJO, PUNTO POR PUNTO, CON SU FICHERO Y SU LINEA

**LOS TRES DOCUMENTOS, REMEDIDOS POR MI Y NO COPIADOS DEL ENCARGO**, y los tres
calzan al digito con su contraste:

| documento | bytes | sha256 |
|---|---|---|
| `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 bytes en disco y 214916 normalizado a LF | sha256 disco `dda1cdd67042c733` y sha256 LF `dda1cdd67042c733` |
| `docs/INTRA_DOMINIO_INFORME.md` | 943970 bytes en disco y 943970 normalizado a LF | sha256 disco `c05b6bcd20188a9c` y sha256 LF `c05b6bcd20188a9c` |
| `docs/BANCO_DE_TEXTOS.md` | 182228 bytes en disco y 182228 normalizado a LF | sha256 disco `68557cd00a3124f4` y sha256 LF `68557cd00a3124f4` |

**LAS ONCE SE CUENTAN CON `CABECERA_LD` IMPORTADA Y NO CON UN PATRON MIO**, que
es la vara que esta campana ya usa y que el acta 203 cita por su nombre. Da
**27** cabeceras `LD` en el documento de hoy, de las cuales **11** son de la
tanda (`LD-01` a `LD-11`) y **16** son de fuera. **CIFRA de las once que el
patron NO encontro: 0.**

**LA TABLA DEL COTEJO. UNA FILA SIN CITA NO VALE:**

| punto | doc | veredicto | cita, con fichero y linea |
|---|---|---|---|
| `V.1` las once con su razon | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:74` `## LAS ONCE, una por una`. Las 11 con veredicto leido de su cabecera y las 11 con prosa y linea de cita. **CIFRA sin razon: 0** |
| `V.2` seccion 52 con las parejas que el ejercicio no puede cerrar | INF | **CUBRE** | `INTRA_DOMINIO_INFORME.md:10055` `## 52. LAS PAREJAS QUE EL EJERCICIO NO PUEDE CERRAR`, lineas 10055 a 10111 |
| `V.3` la `TABLA VIVA DE LOS PUROS` | BAN | **A MEDIAS** | `BANCO_DE_TEXTOS.md:938` `#### TABLA VIVA DE LOS PUROS, al 14 ago 2026 (vigente al puesto 1157)`, 11 filas de racimo. **Existe, pero no lleva el efecto de esta mesa. Ver la `D.1`** |
| `V.4` la cifra 205 sobre 221 componentes | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:17` y la cifra 205 en la linea **21**. **Iba sellado como NO documental y resulta que SI tiene sede documental. Ver la `D.2`** |
| `V.5` la tanda de once, 11 ago 2026 | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:44` `## ESTA TANDA: ONCE LECTURAS`, y la fecha en la linea **17** |
| `V.6` misma vara, marcadas LECTURA DIRIGIDA | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:10`, y la segunda mitad de la clausula en la **11** |
| `V.7` el saldo, 2 `A` y 9 `D` | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:60` `## EL SALDO`. **Y su cifra calza con MI recuento de las cabeceras: 2 que empiezan por A y 9 que son D** |
| `V.8` las once nombradas una a una | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:74`. **CIFRA con cabecera propia y veredicto: 11 de 11** |
| `V.9` la clase nueva `A DE BLOQUE` | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:177`, la definicion entera; la clase se nombra en **4** lineas |
| `V.10` destejido mas fusion parcial | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:180`, y se repite en la tabla de formas en la **296** |
| `V.11` la leccion del saldo, 9 de 11 sanas | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:299`, con su motivo detras |
| `V.12` clausula 1 de verificacion | (LD) | **NO DOCUMENTAL** | sellado antes de mirar: es clausula contra `INTRA_DOMINIO_VEREDICTOS.jsonl`, que no es ninguno de los tres. Se busco igual y el literal aparece en `LECTURAS_DIRIGIDAS.md:1826` |
| `V.13` clausula 2 de verificacion | (LD) | **NO DOCUMENTAL** | sellado antes de mirar: es clausula contra el marcador del cribado. Se busco igual y aparece en `LECTURAS_DIRIGIDAS.md:11` |
| `V.14` clausula 3 de verificacion | (LD) | **NO DOCUMENTAL** | sellado antes de mirar: es clausula contra las nominas del inventario. Se busco igual y aparece en `LECTURAS_DIRIGIDAS.md:51` |

**LO QUE LA `V.2` MIDE ADEMAS, Y VA COMO DATO Y NO COMO REPROCHE:** de las once,
**8** tienen sus DOS identificadores dentro de la seccion 52 (`LD-04` a `LD-11`)
y **3** no (`LD-01`, `LD-02`, `LD-03`). **No es un fallo de la seccion:** esas
tres son las que la propia tanda clasifica como *cierran una nomina* y no salen
de esa lista, y el documento lo dice en su linea **51**.

#### 2.c. LA COBERTURA, MEDIDA Y NO NARRADA

| veredicto | cuantos | cuales |
|---|---:|---|
| **CUBRE** | **10** | `V.1`, `V.2`, `V.4`, `V.5`, `V.6`, `V.7`, `V.8`, `V.9`, `V.10`, `V.11` |
| **A MEDIAS** | **1** | `V.3` |
| **NO CUBRE** | **0** | (NINGUNO) |
| **NO DOCUMENTAL** | **3** | `V.12`, `V.13`, `V.14` |

**LA LISTA NOMINAL DE LOS QUE NO CUBREN: NINGUNO.**
**LA LISTA NOMINAL DE LOS QUE CUBREN A MEDIAS: `V.3`.**

**SOBRE LOS 10 PUNTOS DOCUMENTALES SELLADOS: 9 CUBREN, 1 a medias, 0 no cubren.**

**ESTA ES LA CIFRA QUE LA MESA LLEVABA DOS VUELTAS SIN TENER**, y es exactamente
lo que la vara del trabajo pendiente dice de si misma que no hace: *"Si cubre lo
que la ficha describe es LECTURA, y esta vara no la hace."*

#### 2.d. NO CIERRO LA FICHA. LO DEJO PROPUESTO

**PROPUESTA, Y NO ADJUDICACION:** con **0 puntos sin cubrir** y **1 a medias**,
`OP-L-01` **esta sustancialmente cubierta por los tres documentos que su propia
ficha nombra**, y **propongo cerrarla**. **Cerrar una ficha del plan es
adjudicacion del auditor y no mia**, asi que aqui se para.

**LO QUE FALTA PARA QUE SEA UN CIERRE LIMPIO, NOMBRADO Y NO EJECUTADO:** el unico
punto que no cubre entero es la `V.3`, y **no lo arreglo en esta vuelta**.
Arreglarlo seria reescribir dos filas de la `TABLA VIVA DE LOS PUROS` en
`docs/BANCO_DE_TEXTOS.md`, que es una sede sellada del banco, por el carril del
`9.10` y con su correccion declarada. **No cabe con sus guardas al lado de las
dos sub-tareas de esta vuelta, y una mesa a medias es peor que una mesa
pendiente.**

**NO SE TOCO EL CAMPO `estado`**, y no lo digo: lo mide el `sha256`.
`docs/plan/OPERACIONES.jsonl` sigue en **513043** bytes en disco y **513043**
normalizado a LF, sha256 disco `829c583eb779cab6` y sha256 LF `829c583eb779cab6`,
identicos a los de mi apertura. **`git diff --numstat` sobre `docs/plan/`,
`docs/BANCO_DE_TEXTOS.md` y `docs/INTRA_DOMINIO_INFORME.md` da 0 filas.**

#### 2.e. EL COMPUTO, CON PREFIJO DE GUION BAJO

`scripts/loop/_v207_t2_vara.py` y `scripts/loop/_v207_t2_cotejo.py`, los dos
**fuera del censo y fuera de la nomina**, que sigue congelada en **135**.
**NINGUN LECTOR NUEVO DE PROPOSITO GENERAL:** `CABECERA_LD` se IMPORTA de
`scripts/loop/vuelta165_tarea6_op_l_01.py` y la vara se IMPORTA del fichero
sellado. El resto es busqueda de literal que devuelve linea.

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

