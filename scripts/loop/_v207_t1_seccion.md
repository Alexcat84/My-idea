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
