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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 207`, y su salida
cruda vive en `docs/loop/SALIDA_V207_TALLADOR_CABECERA.txt` (3112 bytes en disco y 3092 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `3e523b74` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 206: LA VUELTA CUMPLIO SU ENCARGO ENTERO Y CERRO SU PROPIO REPORTE, Y LA PARADA QUE EL EJECUTOR LEVANTA ES CIERTA PERO NO ES CONDICION DE PARADA. Toda cifra del reporte reproduce al digito con mis comandos salvo DOS, y las dos son caidas de REPORTE que NO acumulan por la letra afinada del 27 ago. LA CIFRA FALSA GRANDE ES MIA, NO DEL EJECUTOR: la adjudicacion 5.3 del acta 205 decia "una sola causa" y hoy, contando yo los once ficheros sellados con mi propio lector, salen 3 familias distintas de la tupla CIFRA de FALLO ((0,0,0,2) en siete tramos, (0,1,0,2) en tres, (0,2,0,2) en uno) y 5 entradas de la nomina que NO MORDIERON en 4 tramos. Queda CORREGIDA POR DECLARACION con el texto viejo intacto. Lo que si se sostenia: ANCLA PERDIDA 0 en los once, NO REPRODUCIBLE 0 en los once y 2 fuera de la nomina en 11 de 11.'), HEAD real de apertura `3e523b74` (sello RECONSTRUIDO DESPUES (commit 3a0ac809), leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `5c1aa77a` (leido de `SALIDA_V207_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

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
normalizado a LF, con sha256 disco `f933b87fcbd7ba12` y sha256 LF `f933b87fcbd7ba12`,
a **1171455** bytes en disco y **1171455** normalizado a LF, con sha256 disco `c2129e11ec925f1f` y sha256 LF `c2129e11ec925f1f`.
La entrada mide **9908** bytes.

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

<!-- CORRECCION DECLARADA V208 T1D -->

> **CORRECCION DECLARADA (7 sep 2026, vuelta 208, TAREA 1.d), POR ADICION,
> CON EL TEXTO VIEJO ENTERO ARRIBA, SIN TACHARLO Y SIN CLAVE NUEVA DE
> ESQUEMA.** El parrafo de aqui arriba publica **6** elementos de
> `verificacion` y son **SIETE**. La caida la levanto el auditor en la
> `4.1` de su acta de la vuelta 207, y **no la corrijo copiandole**
> (`EJECUTOR.md` 2, EL INSTRUMENTO MANDA): la remedi yo en la vuelta 208
> sobre la linea **41** de `docs/plan/OPERACIONES.jsonl`, que da
> **18** campos, **4** elementos de `evidencia` y **7** de
> `verificacion`, de los cuales **4** son CORRECCIONES DECLARADAS.
>
> **Y NO HACIA FALTA IR A LA FICHA: MI PROPIA SALIDA SELLADA YA LO DECIA.**
> `docs/loop/SALIDA_V207_T2_VARA.txt`, en su linea **21**, imprime
> literalmente `CIFRA elementos de `verificacion`: 7`. **El instrumento midio bien y la transcripcion al
> reporte perdio uno.**
>
> **LA COBERTURA NO CAMBIA NI EN UN PUNTO, Y ESO TAMBIEN VA MEDIDO.**
> `V.12`, `V.13` y `V.14` salen de `verificacion[0]`, `[1]` y `[2]`, que
> son las **3** clausulas que no son correcciones; los **4** elementos
> que faltaban de contar son las CORRECCIONES DECLARADAS, **que nunca
> fueron puntos de la vara**. **Puntos de la vara que se mueven por esta
> correccion: 0.** El cotejo de la `2.b` y la cobertura de la `2.c` se
> quedan exactamente como estan.


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

**EL VEREDICTO DE UNA LINEA: LAS DOS SUB-TAREAS CIERRAN Y NINGUNA SE QUEDA A MEDIAS: R.71 queda escrita por adicion pura con 146 lineas anadidas y 0 borradas y el numero computado por el instrumento, las OCHO adjudicaciones del acta 206 quedan registradas por su numero contra las seis que el encargo decia, y la E.1 y la E.2 quedan corregidas en el reporte archivado de la 206 con el texto viejo entero encima y los dos sha256 medidos por mi; y la mesa OP-L-01 queda MEDIDA contra los tres documentos que su propia ficha nombra, con la vara sellada antes de abrir ninguno de ellos y una cobertura de 10 CUBRE, 1 A MEDIAS y 0 NO CUBRE, propuesta para cierre y sin cerrarla yo. LO QUE SUBE SIN SER PARADA es que la vara del 4.1 del acta 202 no alcanza sobre un acta moderna y da cuatro numerales falsos o vacios, y que la TABLA VIVA DE LOS PUROS no lleva el efecto de la mesa que la nombra como evidencia.**

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**NINGUNA CELDA DE ESTA SECCION SE TECLEO.** Cada tabla dice de que fichero de
salida sale y se reconstruyo contando ese fichero antes de publicarla
(`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO).

### 3.0 LO QUE SUBE PRIMERO, PORQUE ES LO MAS CARO QUE ENCONTRE

**NO ES UNA PARADA.** No contradice ninguna regla vigente ni ninguna cifra
publicada con su corte: es un hallazgo de instrumento, y lo dejo medido para que
el auditor decida. Van dos, en orden de coste.

**`3.0.a` LA VARA DEL `4.1` DEL ACTA 202 NO ALCANZA SOBRE UN ACTA MODERNA, Y
CUATRO DE SUS CINCO NUMERALES SALEN VACIOS O APUNTANDO A OTRA SECCION.** La vara
se escribio para actas ANTERIORES a la 184. El acta 206 es POSTERIOR y escribe
sus claves con comillas inversas, que es justo lo que el lector heredado pide, y
aun asi:

| numeral | lo que la VARA da | lo que hay, medido | la causa, leida del codigo |
|---|---|---|---|
| adjudicaciones | **0**, sobre la seccion **5** | **8**, `6.1` a `6.8`, seccion **6** | `MARCAS["adjudicaciones"]` es `("ADJUDICACIONES", "LA ADJUDICACION")` y casa con la seccion 5, *"LA ADJUDICACION 5.3 DEL ACTA 205 ES FALSA"*, que es una correccion y no la seccion de adjudicaciones. La real se titula `LO QUE ADJUDICO` |
| caidas propias del auditor | (ninguna seccion) | **3**, `C.1` a `C.3`, seccion **9** | sus marcas son `MIS CAIDAS PROPIAS` y `MIS PROPIAS CAIDAS`; el acta titula `MIS CAIDAS, CON SU NOMBRE` |
| caidas del ejecutor | **0** por las TRES formas | **2**, `E.1` y `E.2`, seccion **4** | la seccion SI se encuentra, pero sus claves son `E.n` y las tres formas miran `4.M`, `CAIDA n` y el lead en negrita |
| preguntas | **0**, y ademas *"la seccion de PREGUNTAS aparece 0 veces"* | **3**, `P.1` a `P.3` | el patron de `preguntas_del_reporte()` exige la palabra pegada al numero y el articulo `LAS` se lo rompe (acta 204 `4.4`, linea **196**) |
| hallazgos | **4** | **4**, `7.1` a `7.4` | calza, y es el unico de los cinco que calza |

**LO QUE ESTO CUESTA, DICHO SIN ADORNARLO:** el numeral de adjudicaciones no sale
0 por casualidad, sale 0 **contando bien una seccion equivocada**, que es la
especie de cero mas cara que hay: no se parece a un fallo. **Si una vuelta
publicara ese 0 sin mirar, el registro diria que el acta 206 no adjudico nada, y
adjudico ocho cosas, tres de ellas cerrando pendientes.** No lo arreglo:
ensanchar `MARCAS` toca un lector, y eso es moratoria.

**`3.0.b` LA `TABLA VIVA DE LOS PUROS` NO LLEVA EL EFECTO DE LA MESA QUE LA
NOMBRA COMO SU EVIDENCIA.** Medido en la TAREA 2 y marcado como mi `D.1`:

| nomina | lo que la mesa declara que dejo | lo que la tabla lleva hoy | cierra |
|---|---|---|---|
| junta asesora | **6 de 6, cobertura COMPLETA** (`LECTURAS_DIRIGIDAS.md:290`) | **5** leidos de **6** posibles (`BANCO_DE_TEXTOS.md:961`) | **NO** |
| seleccion de canal | **10 de 10, cobertura COMPLETA** (`LECTURAS_DIRIGIDAS.md:291`) | **8** leidos de **15** posibles (`BANCO_DE_TEXTOS.md:965`) | **NO** |

**Y NO ES QUE LA TABLA SEA VIEJA:** su corte es **14 ago 2026**, al puesto
**1157**, **tres dias DESPUES** del `fecha_corte` de la ficha, que es
**2026-08-11**. Es posterior y aun asi no lo lleva.

### 3.1 LA TAREA 1, CONTADA DE SUS FICHEROS

**LAS CIFRAS DEL ACTA 206, REMEDIDAS POR MI**, con
`git show 3e523b74^:docs/loop/ACTA_AUDITOR.md | wc -c` y su pareja sin el acento
circunflejo. Las tres calzan al digito con el contraste del encargo: **4771842**
antes, **4793964** despues, **22122** anadidos. Y la adicion pura la mide `git`:
`git show --numstat 3e523b74` da **360** lineas anadidas y **0** borradas.

**LA SERIE DE REGISTROS, CORRIDA AL ENTRAR Y AL SALIR**, contada de
`docs/loop/SALIDA_V207_SERIE_APERTURA.txt` y
`docs/loop/SALIDA_V207_SERIE_CIERRE.txt`:

| punta | entradas | colisiones | huecos | mayor | siguiente libre |
|---|---:|---:|---:|---|---|
| AL ENTRAR | 62 | 0 | 0 | `R.70` | `R.71` |
| AL SALIR | 63 | 0 | 0 | `R.71` | `R.72` |

**LA GUARDA DE ADICION PURA DE `R.71`:** `git diff --numstat` da **146** lineas
anadidas y **0** borradas sobre `docs/PENDIENTES.md`; las lineas del texto de
entrada que no estan, en orden, en el de salida son **0**; y la SEGUNDA corrida
escribe **0** entradas y crece **0** bytes. La sede pasa de **1161546** bytes en
disco y **1161546** normalizado a LF, sha256 disco `f933b87fcbd7ba12` y sha256 LF
`f933b87fcbd7ba12`, a **1171455** bytes en disco y **1171455** normalizado a LF,
sha256 disco `c2129e11ec925f1f` y sha256 LF `c2129e11ec925f1f`.

**LAS DOS CAIDAS DE REPORTE, CORREGIDAS.** `docs/loop/reportes/REPORTE_V206.md`
pasa de **38335** bytes en disco y **38335** normalizado a LF a **41867** bytes en
disco y **41867** normalizado a LF, con **57** lineas anadidas y **0** borradas.

**`E.1`, MEDIDA POR MI Y NO COPIADA:** `docs/loop/SALIDA_V206_NO_MORDIO.txt` mide
**4151** bytes en disco y **4103** normalizado a LF, sha256 de disco
`f38bd7855d7760b5` y sha256 LF `cffa5cd0724d0427`. **Son distintos**, y la propia
linea corregida ya lo probaba sin saberlo.

**`E.2`, CON LA FUENTE CORRECTA:** `git show 78ca7176:` sobre
`docs/loop/SALIDA_V205_TALLADOR_RECHAZO.txt` da **3188** bytes en disco y **3188**
normalizado a LF, sha256 LF `b9df894ff422dc77`, y dice **39** celdas (**19** de
APERTURA, **19** de CIERRE, **1** SIN LADO). El mismo nombre HOY mide **1922** bytes en disco y **1922** normalizado a LF, con sha256 disco `254c2257ae55a0f2` y sha256 LF `254c2257ae55a0f2`, y dice **19** celdas con **18** de APERTURA. **El
`19 / 18` sale del segundo, que la vuelta 206 escribio en `a75ff760`.**

### 3.2 LA TAREA 2, CONTADA DE SUS FICHEROS

**LA VARA, SELLADA ANTES DE ABRIR NINGUN DOCUMENTO Y EN SU PROPIO COMMIT
`d7ab4545`:** **14** puntos, **14** citas comprobadas verbatim contra la ficha y
**0** que no aparezcan; **10** sellados como documentales y **4** como no
documentales, con su motivo escrito antes de mirar.

**LAS ONCE, CONTADAS CON `CABECERA_LD` IMPORTADA Y NO CON UN PATRON MIO:** **27**
cabeceras `LD` en el documento de hoy, **11** de la tanda, **16** de fuera, **0**
de las once que el patron no encuentre. Sus veredictos, **leidos de las cabeceras
y no tecleados**, dan **2** que empiezan por `A` y **9** que son `D`, y eso
**calza** con el `SALDO: 2 A y 9 D` que la ficha declara.

**LA COBERTURA, QUE ES LA CIFRA QUE ESTA MESA LLEVABA DOS VUELTAS SIN TENER**,
contada de `docs/loop/SALIDA_V207_T2_COTEJO.txt`:

| veredicto | cuantos | cuales |
|---|---:|---|
| **CUBRE** | **10** | `V.1`, `V.2`, `V.4`, `V.5`, `V.6`, `V.7`, `V.8`, `V.9`, `V.10`, `V.11` |
| **A MEDIAS** | **1** | `V.3` |
| **NO CUBRE** | **0** | (NINGUNO) |
| **NO DOCUMENTAL** | **3** | `V.12`, `V.13`, `V.14` |

**LA LISTA NOMINAL DE LOS QUE NO CUBREN: NINGUNO.** Sobre los **10** puntos
documentales sellados: **9** cubren, **1** a medias, **0** no cubren.

**NO CIERRO LA FICHA Y LO DEJO PROPUESTO** (`2.d` del encargo). **No toque el
campo `estado`**, y no lo digo: lo mide el `sha256` de la seccion 4.3.

### 3.3 EL CICLO ENTERO DE GATE 0, CORRIDO POR MI Y NUNCA `run_phase1.py` A SECAS

**LOS OCHO COMANDOS EN SU ORDEN, LOS DOS LADOS**, por el envoltorio
`scripts/loop/_v207_ciclo_gate0.py`, que **IMPORTA** `_v205_ciclo_gate0.py` y solo
le corrige el dato de la vuelta, que ademas computa de su propio nombre:

| corrida | salida | peor exitcode de los ocho |
|---|---|---:|
| lado APERTURA | `docs/loop/SALIDA_V207_CICLO_APERTURA.txt` | 0 |
| lado CIERRE | `docs/loop/SALIDA_V207_CICLO_CIERRE.txt` | 0 |

**`git diff HEAD --numstat` sobre `dataset/`, `web/`, `engine/` y `docs/plan/` da
0 filas DESPUES de correr yo el ciclo entero**, en las dos corridas.

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ESTADO DEL ARBOL AL ENTRAR, MEDIDO ANTES DE LA PRIMERA OPERACION** y sellado
en `docs/loop/SALIDA_V207_APERTURA.txt`:

CIFRA lineas de status, medidas con `git status --porcelain`: 1

CIFRA filas de `git diff --numstat -- dataset/` AL ENTRAR: 0

**LA UNICA LINEA DE STATUS SE DICE EN VEZ DE ESCONDERSE DETRAS DEL NUMERO:** era
`?? scripts/loop/_v207_apertura.py`, mi propio computo de apertura sin trackear,
escrito por el comando que estaba midiendo. **El arbol entro limpio**, y
`git rev-list --left-right --count origin/pasada-unica...HEAD` daba **0** y **0**,
asi que no habia nada pendiente que committear ni que pushear (`EJECUTOR.md` 3).

**TODO LO DE ESTA SECCION SALE DE `git` CORRIDO EN ESTA VUELTA Y NO SE HEREDA DE
LA APERTURA** (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE). El HEAD de
apertura contra el que se mide todo es `3e523b74`.

### 4.1 LAS CUATRO SEDES QUE EL ENCARGO EXIGE EN CERO, MEDIDAS AL CIERRE

Comando: `git diff 3e523b74 --numstat -- <sede>`

| sede | filas de numstat |
|---|---:|
| `dataset/` | 0 |
| `web/` | 0 |
| `engine/` | 0 |
| `docs/plan/` | 0 |

**CIFRA suma de filas de las cuatro sedes: 0.**

### 4.2 LAS TRES SEDES DEL AUDITOR, QUE EL EJECUTOR NO ESCRIBE

**EL CERO DE `PARA_ALEXIS.md` ES DE AUSENCIA DE FICHERO, Y ASI SE DICE**
(`4.5` del acta 204). Comando: `git diff 3e523b74 --numstat -- <sede>`.

| sede del auditor | existe en disco | filas de numstat | de que es el cero |
|---|---|---:|---|
| `docs/loop/PROMPT_SIGUIENTE.md` | SI | 0 | de no haberla tocado |
| `docs/loop/ACTA_AUDITOR.md` | SI | 0 | de no haberla tocado |
| `docs/loop/PARA_ALEXIS.md` | NO | 0 | **de ausencia de fichero**, no de no haberla tocado |

### 4.3 LAS SEDES SELLADAS, REMEDIDAS AL CIERRE Y NO HEREDADAS

| fichero | bytes (disco y LF, en el mismo renglon) | sha256 (disco y LF, en el mismo renglon) |
|---|---|---|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 4054129 bytes en disco y 4054129 bytes normalizado a LF | sha256 disco `0a77b5a35a962621` y sha256 LF `0a77b5a35a962621` |
| `docs/plan/OPERACIONES.jsonl` | 513043 bytes en disco y 513043 bytes normalizado a LF | sha256 disco `829c583eb779cab6` y sha256 LF `829c583eb779cab6` |
| `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 bytes en disco y 214916 bytes normalizado a LF | sha256 disco `dda1cdd67042c733` y sha256 LF `dda1cdd67042c733` |
| `docs/INTRA_DOMINIO_INFORME.md` | 943970 bytes en disco y 943970 bytes normalizado a LF | sha256 disco `c05b6bcd20188a9c` y sha256 LF `c05b6bcd20188a9c` |
| `docs/BANCO_DE_TEXTOS.md` | 182228 bytes en disco y 182228 bytes normalizado a LF | sha256 disco `68557cd00a3124f4` y sha256 LF `68557cd00a3124f4` |

**NINGUN campo `estado`, NINGUNA clase y NINGUN veredicto se movio, y no lo digo:
lo miden los `sha256` de arriba, identicos por las dos convenciones a los de mi
propio sello de apertura.** Los tres documentos de la TAREA 2 **se leyeron y no
se escribieron**, y sus `sha256` al cierre son los mismos con los que los abri.

### 4.4 LO QUE LA VUELTA SI TOCO, LEIDO DE `git` Y NO NARRADO

Comando: `git diff 3e523b74 --numstat` sobre el arbol entero.

| directorio tocado | ficheros |
|---|---:|
| `docs/loop` | 36 |
| `scripts/loop` | 10 |
| `docs/loop/reportes` | 1 |
| `docs` | 1 |

**CIFRA ficheros tocados contra el HEAD de apertura: 48.**

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. BAJE LA `V.3` A `A MEDIAS` POR UNA VARA QUE LA FICHA NO ESCRIBE.** La
`evidencia[2]` de `OP-L-01` dice, verbatim, *"BANCO_DE_TEXTOS.md, TABLA VIVA DE
LOS PUROS"*. **Con la letra estrecha, ese punto se cumple: la tabla existe, con
ese nombre exacto, en la linea 938.** Yo le exigi ademas **que llevara el efecto
de la mesa**, y como no cierra ninguna de las dos nominas que la mesa declara
completas, la baje a `A MEDIAS`.

**POR DONDE ME PUEDO ESTAR EQUIVOCANDO:** la ficha nombra el documento como sede
de evidencia, **no promete que ese documento quede actualizado**. Si el auditor
lee que la evidencia es *"existe la tabla y ahi se mira"*, mi `A MEDIAS` sobra y
la cobertura es **11 de 11**. **Yo creo que una evidencia que no lleva el efecto
de lo que evidencia no evidencia nada, pero la letra es del auditor y no mia**, y
por eso publico las dos lecturas con sus lineas para que se pueda revocar sin
volver a medir.

**`D.2`. LA `V.4` IBA SELLADA COMO NO DOCUMENTAL Y RESULTA QUE SI TIENE SEDE, Y
NO LA MOVI DE LADO.** Antes de abrir nada declare que la cifra *"205 pares
internos fuera de cola sobre 221 componentes"* no era documental, porque su sede
seria una salida de instrumento. **Abri el documento y esta ahi**, en
`LECTURAS_DIRIGIDAS.md:17` y `:21`. **Lo coteje y lo publique como CUBRE, pero
NO lo movi a la lista de documentales del sello**, porque mover un punto de lado
despues de mirar es exactamente lo que sellar el reparto viene a impedir.

**POR DONDE ME PUEDO ESTAR EQUIVOCANDO:** el resultado es que mis cifras de
cobertura tienen **10** puntos sellados como documentales pero **11** filas con
veredicto documental, y esa asimetria hay que leerla con la nota al lado. **Un
auditor podria decir con razon que lo limpio era declarar el sello equivocado y
rehacerlo**, en vez de arrastrar dos cuentas.

**`D.3`. LE PUSE LAS CUATRO MARCAS DEL ANEXO A MI PROPIO ESQUELETO YA ESCRITO, EN
VEZ DE PARARME.** Mi esqueleto nacio sin `<!-- TABLA DE TAREAS -->` y sus tres
hermanas, que son las que `anexar_tarea_al_reporte.py` busca. Sin ellas la fila
de cada tarea habria que teclearla, que es lo que `EJECUTOR.md` 1 prohibe. Lo
arregle con `scripts/loop/_v207_marcas_anexo.py`, **por adicion, con las dos filas
de tarea comprobadas byte a byte y publicando entera la tabla de sitio que
sustitui**. Va tambien como caida mia en la `C.1`.

**POR DONDE ME PUEDO ESTAR EQUIVOCANDO:** toque un reporte ya abierto y
committeado. **No re-lance el esqueleto a proposito**, porque a esas alturas el
PASO 0 habria intentado archivar la vuelta 207, que no ha cerrado.

## 6. LAS PREGUNTAS

**`P.1`. LA VARA DEL `4.1` DEL ACTA 202 SE ESCRIBIO PARA ACTAS ANTERIORES A LA
184. QUE VARA RIGE PARA LAS POSTERIORES?** Medido en la `3.0.a`: sobre el acta
206 da **0** adjudicaciones contando bien una seccion equivocada, y **0** caidas
del ejecutor sobre una seccion que se titula DOS. **Cada vuelta que registre un
acta moderna va a chocar con esto**, y ensanchar `MARCAS` toca un lector, que es
moratoria. **No lo decido yo.**

**`P.2`. UNA EVIDENCIA QUE NO LLEVA EL EFECTO DE LO QUE EVIDENCIA, CUBRE O NO
CUBRE?** Es la `D.1` en forma de pregunta, y no es solo de `OP-L-01`: las otras
tres fichas reales nombran documentos igual, y la respuesta decide como se
cotejan las tres.

**`P.3`. LAS DOS FILAS DE LA `TABLA VIVA DE LOS PUROS` SE ACTUALIZAN, Y QUIEN?**
Si la respuesta a la `P.2` es que no cubre, alguien tiene que escribir esas dos
filas por el carril del banco `9.10`, con correccion declarada y sin borrar el
texto viejo. **No lo hice yo**: no cabia con sus guardas al lado de las dos
sub-tareas, y una mesa a medias es peor que una mesa pendiente.

## 7. PENDIENTES DE DOCTRINA

**`PD.1`. QUE SE HACE CON UN PUNTO DE UNA VARA SELLADA QUE, AL MIRAR, RESULTA
ESTAR DEL OTRO LADO.** Es la `D.2`. La casa manda sellar antes de mirar y manda
declarar en vez de resolver copiando, **pero no dice si el sello se corrige por
adicion declarada o se arrastra entero con su nota**. Hoy lo arrastre entero.
**Registro lo mejor sostenido y sigo** (`EJECUTOR.md` 5).

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**`C.1`. MI ESQUELETO NACIO SIN LAS CUATRO MARCAS DEL ANEXO.** `EJECUTOR.md` 1
dice que el reporte crece por anexion, y el instrumento que anexa busca cuatro
marcas literales que mi esqueleto no puso. **Lo cace al ir a anexar la TAREA 1**,
no despues, y lo arregle por adicion con las dos filas comprobadas byte a byte.
**Es la misma familia de las dos marcas que le faltaban al esqueleto de la 205**,
y me la encontre por no haber mirado que exigia el anexador antes de tallar. Sube
tambien como `D.3`.

**`C.2`. `docs/loop/SALIDA_V207_HEAD_APERTURA.txt` NACIO AL CIERRE, CON LAS DOS
TAREAS YA HECHAS.** El VALOR que lleva, `3e523b74948ee5ec0168c016fddc40ae02506229`,
**es de apertura de verdad y no lo teclee**: lo leyo un computo de
`docs/loop/SALIDA_V207_APERTURA.txt`, que escribi **antes de la primera
operacion** y que quedo committeado en `70044f73`. **Pero el fichero con ese
nombre nace ahora**, y el tallador lo exige para tallar la fila de identidad.
**Es la misma especie que la `C.3` del reporte de la 206 y la cuento una sola
vez, aqui.**

**`C.3`. MI PRIMERA BUSQUEDA DE LAS DOS FILAS DE LA `TABLA VIVA` NO ENCONTRO
NINGUNA, Y CASI PUBLICO UN `CUBRE` FALSO.** Exigi el literal `| nombre |` y la
tabla escribe `la junta asesora`, con articulo y con negritas. **Mi computo
concluyo `CIFRA nominas que la mesa declara CERRADAS y la tabla NO lleva
cerradas: 0` y de ahi salio un `CUBRE`**, que es exactamente el cero de un
instrumento publicado como un hecho del mundo que `EJECUTOR.md` 9 prohibe. **La
cace porque el resultado 11 de 11 me parecio demasiado limpio y fui a mirar la
tabla a mano.** La arregle, y ahora el computo **cae en `NO CUBRE` si no halla la
fila** en vez de concluir que no hay desajuste. **No llego a ningun documento**,
pero la casi caida tambien se cuenta, y el comentario que lo explica quedo dentro
del propio codigo para que no se pierda.

**`C.4`. CORRI `cerrar_reporte.py` TRES VECES, Y LA SEGUNDA DEJO EL REPORTE
ESCRITO Y EN ROJO.** El instrumento **escribe primero y valida despues**: su
segunda corrida pego cuerpo y cabecera, luego cayo en la guarda `D.1` y publico
`ROJO`, dejando en disco un `docs/loop/REPORTE.md` cerrado **con el cuerpo viejo
dentro**, el que todavia tenia las dos cifras sin pareja. **Lo cace en la tercera
corrida, porque el propio instrumento me dijo que el sujeto ya no estaba en
estado de reporte SIN CERRAR**, y lo devolvi a su sitio con
`git checkout HEAD -- docs/loop/REPORTE.md`, que lo restaura byte a byte del
commit de la TAREA 2. **NO llego a ningun commit** y ningun texto se perdio,
porque lo que se restaura estaba committeado.

**LOS TRES MOTIVOS POR LOS QUE LAS DOS PRIMERAS CAYERON, Y LOS TRES ERAN MIOS:**
mi veredicto decia *"las dos caidas de reporte"* hablando de las del acta 206, y
la guarda de numerales lo leyo como una cuenta de MIS caidas, que son tres, e
hizo bien: su propio docstring avisa de que una cuenta AJENA no se escribe como
`N caidas` a secas. Mi sello de apertura escribia `CIFRA lineas de status,
medidas con git status --porcelain: 1`, y el patron de la guarda `D.1` exige los
dos puntos pegados a la palabra `status`, asi que **no podia cotejar mi seccion 4
y se nego a cerrar a ciegas**, que es exactamente lo que tiene que hacer. Y dos
`sha256` mios iban sin su pareja en la misma linea. **Las tres las arregle yo y
ninguna es del instrumento.**

**LA DEL SELLO VA POR EL CARRIL DE LA CORRECCION DECLARADA:** anadi a
`docs/loop/SALIDA_V207_APERTURA.txt` la misma cifra en la forma que la guarda
sabe leer, **por adicion pura, con el texto viejo entero arriba** y con el valor
**leido del propio fichero y no tecleado**. `git diff --numstat` sobre ese sello
da **13** lineas anadidas y **0** borradas, y las lineas de la entrada que no
estan, en orden, en la salida son **0**. **La medicion es la de la apertura; lo
que llego tarde es la forma de escribirla.**

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**PROPONER ES MIO Y ENCARGAR ES DEL AUDITOR.** No escribo `PROMPT_SIGUIENTE.md`,
`ACTA_AUDITOR.md` ni `PARA_ALEXIS.md`, y el `numstat` de las tres contra mi HEAD
de apertura va en la seccion 4.2, en **0**, **0** y **0**, con el cero de
`PARA_ALEXIS.md` distinguido como **de ausencia de fichero**.

1. **`OP-L-01` ESTA MEDIDA Y PROPUESTA PARA CIERRE, CON 0 PUNTOS SIN CUBRIR Y 1 A
   MEDIAS.** Cerrarla es adjudicacion del auditor. Si la `D.1` se revoca, la
   cobertura es **11 de 11** y la ficha cierra limpia.
2. **LA SIGUIENTE DE LAS CUATRO FICHAS REALES.** Quedan `OP-L-02`, `OP-L-03` y
   `OP-I-01`. **`OP-L-02` sigue sin ningun documento que medir** y el encargo
   dice expresamente que no se toque todavia.
3. **LA OPERACION DE CODIGO DE LA ESCALADA SIGUE ENCARGADA Y CON SU EJECUCION
   SUSPENDIDA** (acta 202 `4.6`, ratificada por la 203 `4.9`, la 204 `4.10`, la
   205, la 206 y esta): se ejecuta en la primera vuelta despues de que la
   moratoria se levante. **La arrastro para que la 208 no la pierda.**
4. **LA COLA DE LA AUDITORIA INTEGRAL, QUE HOY CRECE A SIETE ENTRADAS
   NOMBRADAS:** las **5** entradas de la nomina que no muerden, partidas en 4 mas
   1 por la `6.2` del acta 206; el `--siguiente` del lanzador, que responde
   **183** en cualquier vuelta (acta 205 `5.2`); el patron de
   `preguntas_del_reporte()`, roto en la linea **196** de
   `scripts/loop/_v203_reparto_de_actas_viejas.py` (acta 204 `4.4`); la guarda de
   las dos convenciones, que solo mira BYTES y no `sha256` (acta 206 `7.2`); la
   falta de argumento de ruta en `cerrar_reporte.py` (acta 206 `6.3`); y **las
   DOS que anado yo hoy**: las `MARCAS` de la vara del `4.1`, que sobre un acta
   moderna eligen la seccion equivocada (`3.0.a`), y **`preguntas_del_reporte()`
   otra vez, que ya va por su tercera vuelta rodeada a mano**.
5. **LA DEUDA DE REGISTROS, ENSANCHADA HASTA LA 206 Y REMEDIDA AL CIERRE:** de la
   173 a la 206 quedan **5** actas sin entrada propia, y son la **201**, la
   **202**, la **203**, la **204** y la **205**. La del `4.9` del acta 201 sigue
   agotada en **0**. **La mido y la subo; encargarla es del auditor.**
6. **LA BATERIA NO CORRE HASTA LA 210** (`AUDITOR.md` 6.1), y cuando corra se va
   a encontrar las mismas cinco entradas que no muerden.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 207 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V207_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: NADIE la corrio en la vuelta 207, y no es un olvido: por AUDITOR.md 6.1 la bateria de mutaciones corre CADA CINCO vueltas, en una vuelta propia que no lleva nada al lado, y la adjudicacion 6.7 del acta 206 lo dice con sus numeros: la ultima de la cadencia fue la 205 y la siguiente es la 210. Esta vuelta traia DOS sub-tareas por AUDITOR.md 6.2 y ninguna de las dos era la bateria, asi que aqui NO hay corrida propia que pegar y lo que va es este hueco declarado y medido.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
