# REPORTE DE LA VUELTA 170 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta170_esqueleto_reporte.py` **antes de la primera tarea**;
> cada tarea ANEXA SU FILA AL CERRARSE, no al final; y el cierre talla la
> cabecera. **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se
> hizo, y las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se
> hicieron.** Tope de cinco tareas, y el encargo trae exactamente cinco.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta170_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 169: `46208790`, asunto real leido de git log:
  'ACTA DE LA VUELTA 169 DEL AUDITOR: LAS CINCO TAREAS REPRODUCEN AL DIGITO Y LA BATERIA SALE VERDE POR MI MANO, PERO LA VUELTA SE CONTRADIJO A SI MISMA EN LA MISMA SESION Y ESO ES CIFRA PUBLICADA. NO HAY PARADA'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V170_HEAD_APERTURA.txt`: `46208790`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `abb85566`
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 170`. **Esta
vuelta SI corrio el bloque de apertura entero**, asi que la mitad izquierda ya
se puede leer: corrido en la apertura, el tallador dice **"ROJO, 19
celdas no se pudieron leer"** y de esas lineas de rojo, **0 mencionan
APERTURA**. Son todas del lado CIERRE, que en la apertura todavia no existe.
Este hueco se rellena con la tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | BLOQUEANTE. LOS REGISTROS Y LA CAIDA DE CIFRA PUBLICADA (1.a el acta 169 al `R.39`, 1.b la adjudicacion 6.2 corregida por 9.10 con su tabla de commits medida, 1.c el arnes gana el caso que ANCLA POR MEDICION el nacimiento de la decimotercera tachada) | **CERRADA**, con la bateria declarada al cierre | `SALIDA_V170_T1_REGISTRO_ACTA_169.txt`, `_T1A_MUTACION_REGISTRO`, `_T1B_TACHADAS_POR_COMMIT`, `_T1B_RELECTURA_CONTRA_GIT`, `_T1C_ARNES_RETRATO` |
| **TAREA 2** | LOS DOS INSTRUMENTOS DE PROCESO (2.a el AISLADOR DE LA CIEGA, 2.b el ARCHIVADOR DE REPORTES y el archivado hacia atras del de la 168) | **CERRADA** | `SALIDA_V170_T2A_MUTACION_AISLADOR.txt`, `_T2A_AISLADOR_DEMO`, `_T2B_ARCHIVADOR_168`, `_T2B_MUTACION_ARCHIVADOR` |
| **TAREA 3** | LAS DEUDAS DE CORTE, por 9.21 mas 9.10 (3.a las '53 familias' de `OP-I-01` y su aritmetica de 671, 3.b la fecha de corte del '2.117' en la clausula 2 de `OP-L-01` y de `OP-L-02`) | **CERRADA**, con una discrepancia declarada | `SALIDA_V170_T3_DEUDAS_DE_CORTE.txt` |
| **TAREA 4** | LOS NUMEROS QUE FALTAN (4.a las lecturas dirigidas de la segunda tanda ganan numero `LD` por adicion pura, 4.b los cinco nodos puente del sales roadmap se registran MEDIDOS y NO se ejecutan) | **4.b CERRADA; 4.a MEDIDA Y TRAIDA COMO PARADA** | `SALIDA_V170_T4A_LECTURAS_SIN_NUMERO.txt`, `_T4A_CONTAR_LD`, `_T4B_PUENTES` |
| **TAREA 5** | EL TRABAJO DE VERDAD: CERRAR `OP-L-02` (5.a la FORMA de cada nomina afectada re escrita por 9.26, con su cobertura al lado y el resolutor delante; 5.b el veredicto de las tres clausulas y, solo entonces, la apertura de `OP-L-03`) | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
### TAREA 1 (BLOQUEANTE). LOS REGISTROS Y LA CAIDA DE CIFRA PUBLICADA

**1.a EL ACTA 169 ENTERA QUEDA EN EL `R.39`.** Instrumento
`scripts/loop/vuelta170_tarea1_registrar_acta169.py`, salida
`docs/loop/SALIDA_V170_T1_REGISTRO_ACTA_169.txt`, **exit 0**. Ninguna cifra
tecleada, todas contadas del acta y de la serie:

| celda | de donde sale | valor |
|---|---|---:|
| cuerpo del acta 169 acotado | cabecera y final del fichero | lineas 56.702 a 57.287 |
| adjudicaciones `6.n` | barrido del acta, para en el primer hueco | **12** (6.1 a 6.12) |
| caidas propias del auditor | negritas `CAIDA n` del cuerpo acotado | **3** |
| serie antes de escribir | `serie_de_registros.py`, sus DOS sedes | 30 entradas, 0 colisiones, 0 huecos |
| siguiente libre, computado | mayor mas uno | **R.39** |
| sede, leida de la regla | `docs/loop/ACTA_AUDITOR.md:53933` | `docs/PENDIENTES.md` |
| reparto por via, computado | del mapa `VIA` | **EJECUTADA 7** (6.1, 6.2, 6.3, 6.4, 6.9, 6.10, 6.11); **SIN TOCAR NADA 5** (6.5, 6.6, 6.7, 6.8, 6.12) |
| que suben al fundador | del reparto | **0** |
| serie despues de escribir | recomputada | 31 entradas, 0 colisiones, 0 huecos |
| donde vive | recomputado | `R.39` en `docs/PENDIENTES.md:12167` |

**LOS DOS NUMERALES DEL TITULO SUBIERON SOLOS:** el `R.38` registro *diez* y
*dos*; este registra **doce** y **tres**, y ninguna de las dos palabras esta
tecleada. Y el barrido llega por primera vez a `6.12`.

**Y AQUI VA UN HALLAZGO QUE NO ME PIDIERON, MEDIDO Y NO SUPUESTO.** La entrada
`R.38`, escrita por la vuelta 169, afirma que *"el arnes hermano lo prueba por
mutacion en vez de afirmarlo"*. **Ese arnes no existe.** Medido con
`ls scripts/loop/ | grep mutacion_registro`: existen los de las vueltas 164,
165, 166, 167 y 168, y **no existe el de la 169**; su registrador
`vuelta169_tarea1_registrar_acta168.py` se quedo sin `prueba_de_mutacion`. **No
lo corrijo**: no es mio y el encargo no me manda tocarlo. **Lo que si hago es no
repetirlo:** el `R.39` usa la misma frase, y por eso esta vuelta escribe
`scripts/loop/vuelta170_tarea1a_mutacion_registro.py`, que la hace cierta. **38
casos, 38 pasan, 38 caen al mutar el esperado**, salida
`docs/loop/SALIDA_V170_T1A_MUTACION_REGISTRO.txt`, exit 0.

**1.b LA CAIDA DE CIFRA PUBLICADA, CORREGIDA POR EL CARRIL DEL BANCO `9.10`.**
La frase falsa de `scripts/loop/vuelta166_tarea3_mutacion_retrato.py` **queda
entera y tachada** con `~~...~~`, y debajo va la correccion fechada con la tabla
**medida por mi en esta vuelta**, no copiada del acta. Instrumento
`scripts/loop/vuelta170_tarea1b_medir_tachadas_por_commit.py`, salida
`docs/loop/SALIDA_V170_T1B_TACHADAS_POR_COMMIT.txt`, **exit 0**: recorre los
**38** commits que tocan `docs/plan/RECOMPUTO_3388.md`, lee el **blob** de cada
uno y cuenta la cadena con `T.localizar_filas` y `T.anatomia`, **el localizador y
el contador del propio instrumento del retrato**, no con un `grep`.

| commit | vuelta | fecha | tachadas |
|---|---:|---|---:|
| `7f4ec6d9` | 11 | 2026-08-13 | 0 (la primera de la serie) |
| `3ffc2091` | 58 | 2026-08-20 | 12 |
| `33fe1380` | **166** | 2026-09-04 | **13, LA DECIMOTERCERA ENTRA AQUI** |
| `c6ac70f6` | **167** | 2026-09-04 | 13 (ultimo commit que toca el fichero) |
| el arbol de trabajo de hoy | | 2026-09-04 | 13 |

**LA VUELTA DE LOS DOS ULTIMOS NO SE SUPONE:** su asunto no la nombra, asi que
se **computa** por el invariante de la casa (los commits posteriores al `ACTA DE
LA VUELTA N` son de la N mas 1). El ultimo acta anterior a `33fe1380` es
`00cfe6e0`, `ACTA DE LA VUELTA 165`; luego `33fe1380` es de la **166**.

**Y UNA PRECISION QUE LA RELECTURA AL DOBLE ME OBLIGO A ANADIR, porque mi propia
primera version de esa tabla puso `c6ac70f6` en la 166 y esta en la 167:** LA
VUELTA 167 **SI** TOCO EL FICHERO, en `c6ac70f6`, **pero NO TOCO ESTA FILA**.
Comparadas las cuatro filas del PASO 1 entre los dos blobs: `colapsos` IGUAL,
`crudas` IGUAL, `distintos` IGUAL, y solo `multiples` DISTINTA, que es el rotulo
que aquella TAREA 4 arreglaba. **Por eso el reporte de la 168 acerto al decir
"la 167 NO movio esa fila", y lo unico falso es "anadio una tachada".**

**LAS DOS COSAS QUE LA CORRECCION DICE, COMO EL ACTA MANDA:** (1) quien anadio
la decimotercera, **la vuelta 166 en `33fe1380`, el mismo commit que creo este
arnes** (comprobado con `git log --diff-filter=A` sobre el fichero del arnes);
(2) por que el computo dice **CATORCE**: no porque nadie anadiera nada en la
167, sino porque **trece tachadas hacen que la siguiente sea la decimocuarta**.

**LA RELECTURA AL DOBLE DE LA CUARTA SEDE, EJECUTADA Y CON SU COMANDO.** Toda
afirmacion de la correccion se comprobo **contra git antes de escribirla**,
salida `docs/loop/SALIDA_V170_T1B_RELECTURA_CONTRA_GIT.txt`: el acta anterior a
`33fe1380` (`git log --format="%H %s" 33fe1380~1`), el commit que crea el arnes
(`git log --diff-filter=A`), los asuntos literales de `33fe1380` y `c6ac70f6`
(`git log -1 --format=%s`), la frase del reporte de la 168 (`git show
1eec382f:docs/loop/REPORTE.md`), el conteo de 38 commits y el commit `a56b2dfd`
que escribio la frase falsa. **Siete comprobaciones, siete calzan.**

**1.c EL REMEDIO: LA HISTORIA DEJA DE VIVIR EN UN COMENTARIO.** El arnes gana la
seccion **F**, que **ancla por medicion contra git** el nacimiento de la
decimotercera tachada: importa `serie_medida`, `nacimiento_de_la_tachada` y
`vuelta_computada_de` del instrumento de la 1.b (**una sola fuente, sin copia**)
y comprueba en cada corrida que el primer commit que llega a 13 es `33fe1380`,
que su vuelta computada es 166, que el anterior es `3ffc2091` con 12, que
**cero** commits de la vuelta 167 suben el conteo, que `c6ac70f6` **es** de la
167 y **no** movio la fila, y que trece hacen catorce.

**El arnes pasa de 24 casos a 35.** Salida
`docs/loop/SALIDA_V170_T1C_ARNES_RETRATO.txt`, **exit 0**: *"los 35 casos pasan
tal cual y los 35 caen al mutar el esperado"*. **Ninguna comprobacion vieja se
quito y ninguna se aflojo.**

**LO QUE ESTA TAREA DEJA PENDIENTE Y SE DICE EN VEZ DE CALLARLO:** la corrida de
la bateria de mutaciones. **No se corre aqui a proposito**: las TAREAS 3, 4 y 5
escriben ficheros en `docs/loop/`, y una bateria de 30 minutos corriendo al lado
de esas escrituras es exactamente el escenario de RUIDO DE CONCURRENCIA que el
acta 157 documento. **Se corre ENTERA y SOLA al cierre**, y su resultado va en la
seccion de cierre de este reporte, no aqui.

**EL ARBOL SUCIO DE LA APERTURA, TRATADO Y NO BARRIDO** (lo que el encargo manda
hacer dentro de esta tarea). `git status --porcelain` al abrir daba dos lineas,
selladas antes de la primera operacion en `docs/loop/SALIDA_V170_APERTURA.txt`:

| ruta | medicion | que se hace |
|---|---|---|
| `dataset/metadata/master_graph.json` | modificado, diff de **0 bytes**, y **0 bytes tambien ignorando el CR de fin de linea** | **NO se commitea**: es suciedad de indice, exactamente lo que la 169 midio y declaro |
| `node_modules/` | **un solo fichero**, `node_modules/.vite/vitest/da39a3ee5e6b4b0d3255bfef95601890afd80709/results.json`, **12.460 bytes** | **NO se commitea**: es cache de `vitest`, artefacto de runtime de la propia suite de la web. **No lo meto en `.gitignore` por cuenta propia**: eso seria decidir por el fundador sobre un fichero que el encargo no nombra. **Queda declarado como DISCUTIBLE `D.1`.** |

### TAREA 2. LOS DOS INSTRUMENTOS DE PROCESO

**2.a EL AISLADOR DE LA CIEGA** (adjudicacion 6.1, la bloqueante; nace de la
`CAIDA 1` del acta 169, que es la **segunda vuelta seguida** en que un auditor
quema su sujeto de ciega). Nace `scripts/loop/aislador_de_ciega.py`, con
**nombre estable y sin numero de vuelta**, como `tallar_cabecera_reporte.py`,
`verificar_apertura_sellada.py` y el archivador de abajo.

**LO QUE HACE, EN SU ORDEN, QUE ES LO QUE IMPORTA:** (1) exige un **criterio
escrito** (`--criterio`) y sin el no corre, y lo copia literal a los **dos**
ficheros para que despues no se pueda discutir por que se eligieron esos pares;
(2) elige con selectores deterministas (dominio, clase, banda, rango, muestra
con semilla via `random.Random`, asi que la eleccion se reproduce); (3) escribe
la salida ciega con **solo** `puesto_intra`, `nodo_a`, `nodo_b` y los pasos de
los dos nodos; (4) escribe el destape (`clase`, `razon`) **en otro fichero**;
(5) **antes de escribir nada** pasa la guarda de fuga, y si algo se cuela **no
escribe ninguno de los dos**.

**LA DECISION DE DISENO QUE HACE QUE ESTO FUNCIONE, Y NO ES DE ESTILO:** la
salida ciega **se construye campo a campo desde una LISTA BLANCA**
(`CAMPOS_CIEGOS`), no copiando la fila y quitando lo prohibido. **Una lista
negra se queda ciega ante un campo nuevo del archivo; una lista blanca no.**

**CASO POSITIVO POR MUTACION, y es exactamente el que el acta pide.**
`scripts/loop/vuelta170_tarea2a_mutacion_aislador.py`, salida
`docs/loop/SALIDA_V170_T2A_MUTACION_AISLADOR.txt`, **exit 0**: **24 casos, 24
pasan, 24 caen al mutar el esperado**. El caso central **ensancha la lista
blanca** con `razon`, con `clase` y con **los dos**, y exige que la guarda
muerda **3, 3 y 6** fugas respectivamente. **El parametro `campos` existe en la
firma para esto**: para poder mutar la lista sin tocar el fichero real ni el
disco. **Cero escrituras**: filas y pasos fabricados en memoria.

**Y SE CORRIO EN VIVO SOBRE EL ARCHIVO DE VERDAD**, salida
`docs/loop/SALIDA_V170_T2A_AISLADOR_DEMO.txt`: 3.388 filas leidas, **6 pares
elegidos** (puestos 1174, 1482, 1757, 1768, 1922, 3190), **0 fugas**, ciega de
8.364 bytes y destape de 6.344 bytes en ficheros distintos. **El destape no se
abrio**, y `grep -c "clase\|razon"` sobre la ciega da **0**. El criterio escrito
dice con todas sus letras que **no es el sujeto de ninguna ciega en curso**,
para no quemarle nada al auditor con una demostracion.

**2.b EL ARCHIVADOR DE REPORTES** (adjudicacion 6.4; resuelve el `D.1` y la
pregunta `P.1` del reporte de la 169 **sin doctrina nueva**). Nace
`scripts/loop/archivar_reporte.py`. **No borra nada, no cambia ninguna regla y
no crea sede nueva: le da nombre de fichero a la que ya existia, que era el
commit.**

**LA DECISION DE DISENO, Y ES LA QUE HACE QUE ESTO SE PUEDA CORRER TARDE:** el
texto **se lee de git** (`git show <commit>:docs/loop/REPORTE.md`), **no del
arbol de trabajo**. Un archivador que copiase el arbol solo podria correr en la
ventana exacta anterior al esqueleto, y **si esa ventana se pierde el reporte
queda sin archivar para siempre**. Leyendo de git, **cualquier reporte de
cualquier vuelta pasada se puede archivar en cualquier momento**, que es justo
lo que hacia falta para archivar hacia atras el de la 168.

| que se archiva | de que commit | bytes | lineas | sha256 (LF) |
|---|---|---:|---:|---|
| `docs/loop/reportes/REPORTE_V169.md` | `a77b206f` | 43.586 | 724 | `262f8409de09...` |
| `docs/loop/reportes/REPORTE_V168.md` | `1eec382f` | 31.263 | 530 | `068fe39fb36a...` |

**LAS DOS COPIAS SE COTEJAN CONTRA EL BLOB DE GIT CON `sha256sum`: IDENTICAS
LAS DOS.** Y las cifras de la 168 (31.263 bytes, 530 lineas) **coinciden con las
que el propio mensaje de `1eec382f` publica**, que es una vara independiente.

**EL ORDEN IMPORTA Y SE RESPETO:** el archivador corrio **antes** de que el
esqueleto sobrescribiera `docs/loop/REPORTE.md`. Tallar antes de archivar habria
dejado el reporte de la 169 otra vez sin mas sede que su commit.

**CASO POSITIVO POR MUTACION**, salida
`docs/loop/SALIDA_V170_T2B_MUTACION_ARCHIVADOR.txt`: cuatro mutaciones y un
control. (1) `--vuelta 168` apuntando al commit del reporte de la 169: **CAE**,
exit 1. (2) `--vuelta 169` apuntando al de la 168: **CAE**, exit 1. (3) destino
existente con contenido **distinto** sin `--forzar`: **CAE**, exit 1. (4) la
misma con `--forzar`: **VERDE**, y restituye el `sha256` original. Control: el
par correcto sigue **VERDE**, exit 0.

**UNA CORRECCION DECLARADA POR ADICION DENTRO DE ESA MISMA SALIDA:** la
comprobacion final original murio por una ruta `/tmp` que python no ve en
Windows. **El parrafo no se borra** y la comprobacion se rehace debajo con
`sha256sum`, que ademas es mejor vara que la que fallo.

**LO QUE ESTA TAREA NO HACE, DICHO PARA QUE NADIE LEA DE MAS:** el archivador
**no se enchufa solo** a ninguna secuencia de apertura. Esta vuelta lo corrio a
mano en su apertura. **Automatizarlo dentro del esqueleto seria decidir por el
fundador** sobre el orden de la apertura, y el encargo no lo pide. Queda como
**DISCUTIBLE `D.2`**.

### TAREA 3. LAS DEUDAS DE CORTE, POR `9.21` MAS `9.10`

Instrumento `scripts/loop/vuelta170_tarea3_deudas_de_corte.py`, salida
`docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt`, **exit 0**. Corrido antes con
`--comprobar`, que mide y no escribe.

**NINGUNA DE LAS TRES CIFRAS ES UNA MENTIRA, Y ESO VA PRIMERO:** las tres son
ciertas en su corte y lo unico que les falta es el corte escrito al lado. Por
eso **no se sustituye ni una letra**.

**3.a LAS APARICIONES DEL 53 EN LA NOTA DE `OP-I-01`, CONTADAS AQUI Y NO
COPIADAS DEL ACTA.** Contadas del propio campo `nota` (10.928 caracteres):

| que se cuenta | cifra |
|---|---:|
| apariciones del literal `53` en la nota | **7** |
| de ellas escritas `53 familias` | 6 |
| de ellas escritas `53 familia_de_ids` | 1 |

**El encargo dice SIETE y yo cuento SIETE: CALZA.** La cifra se publica aunque
coincida, porque la vara es el conteo y no el acta.

**LAS TRES ARITMETICAS QUE LLEVAN UN 53, SUMADAS Y NO CREIDAS.** El instrumento
extrae los sumandos escritos y los suma:

| total escrito | sumandos | suma real | veredicto |
|---:|---|---:|:-:|
| 450 | 335, 53, 19, 13, 20, 10 | 450 | CUADRA |
| 671 | 556, 53, 19, 13, 20, 10 | 671 | CUADRA |
| 323 | 221, 53, 14, 13, 12, 10 | 323 | CUADRA |

**LAS TRES CUADRAN CONSIGO MISMAS, Y ESO ES EL HALLAZGO:** el problema **no es
aritmetico, es de corte**. Cada una suma bien con el 53 que tenia delante; con
el 54 de hoy cada total subiria en uno, y la de 671 seria **672**, que es justo
lo que el fichero mide hoy.

**EL INVENTARIO DE HOY, CONTADO DE `docs/plan/INVENTARIO.jsonl` LINEA A LINEA:**
**672** entradas (556 `acto`, **54** `familia_de_ids`, 20 `figura`, 19
`defecto`, 13 `racimo`, 10 `dominio`), y **la suma de los tipos da 672**, o sea
que el conteo cuadra consigo mismo.

**LO ESCRITO:** una `CORRECCION DECLARADA (2026-09-04, vuelta 170, TAREA 3.a)`
**dentro del campo `nota` que ya existe**, sin clave nueva de esquema. La nota
pasa de **10.928 a 12.772 caracteres** y **solo crece**. **Las siete apariciones
viejas sobreviven enteras: 7 de 7**, comprobado trozo a trozo con 60 caracteres
de contexto cada uno.

**3.b EL MARCADOR, RECOMPUTADO DEL ARCHIVO EN ESTA VUELTA:** **3.388** filas en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, **A 551, B 72, C 5, D 2.760**, 3.388
puestos distintos, maximo 3.388, **cero huecos**.

**Y AQUI VA LO QUE MIDO Y EL ENCARGO NO ANTICIPA, DECLARADO EN VEZ DE
RESUELTO COPIANDO** (`EJECUTOR.md` 2: *"si discrepan de la medicion de hoy, la
discrepancia se declara en vez de resolverse copiando"*):

| ficha | elementos en `verificacion` | la clausula literal | correccion fechada que la cita |
|---|---:|---|---|
| `OP-L-01` | 6 | indice 1 | **SI, indice 4**, `CORRECCION DECLARADA (2026-09-04, vuelta 166, TAREA 2)` |
| `OP-L-02` | 3 | indice 1 | **NO** |

**A `OP-L-01` YA LE PUSIERON EL CORTE, EN LA VUELTA 166.** Su correccion dice
literalmente *"EL NUMERAL 2.117 ES EL VALOR DEL MARCADOR EN LA fecha_corte DE
ESTA FICHA, TESTIGO Y NO CONDICION. MEDIDO HOY: el marcador del cribado vale
3388"*. **Escribir una segunda que diga lo mismo seria dejar dos versiones de la
misma cosa**, que es exactamente lo que la casa no quiere. **Asi que `OP-L-01`
NO SE TOCA**, y se comprueba en disco que su `verificacion` quedo **identica**.

**A `OP-L-02` SI LE FALTABA, Y AHI SE ESCRIBE:** un elemento mas en su lista
`verificacion` que ya existe, **sin clave nueva de esquema**, que es la via que
`OP-L-01` uso en la vuelta 166 y `OP-L-03` en la vuelta 72, y que el acta 71,
seccion 6, adjudicacion 3, adjudico **con las palabras NO ES PARADA**. La lista
pasa de **3 a 4** elementos y **la clausula literal del 2.117 sigue en disco**.

**LO QUE ESTA TAREA NO MUEVE, COMPROBADO Y NO PROMETIDO:** las 71 fichas siguen
siendo 71; `OP-I-01` y `OP-L-02` siguen en sus lineas 44 y 42; las dos siguen
con **18 claves**, **cero campos movidos** ademas de `nota` y `verificacion`, y
**el `estado` de las dos sigue diciendo `LISTA`**, que no es la vara y no se
toca.

### TAREA 4. LOS NUMEROS QUE FALTAN

**4.a LAS LECTURAS DIRIGIDAS SIN NUMERO `LD`: MEDIDAS, Y TRAIDAS COMO PARADA.**
Instrumento `scripts/loop/vuelta170_tarea4a_lecturas_sin_numero.py`, salida
`docs/loop/SALIDA_V170_T4A_LECTURAS_SIN_NUMERO.txt`, **exit 0**.

**LO QUE SE MIDIO PRIMERO, Y CALZA.** La segunda tanda se acota antes de contar
nada (`docs/plan/LECTURAS_DIRIGIDAS.md`, lineas **327 a 518**), sus tablas de
lectura se localizan por su cabecera `| par | clase |` y sus filas se cuentan:

| tabla | filas |
|---|---:|
| LOS CUADRANTES DE MERCADO: 15 de 15, y cae | 8 |
| LA ECUACION DE VALOR: 10 de 10, y cae | 5 |
| LA SUPERVISION DE LA IA, bloque humano: 10 de 10, y cae | 3 |
| **total** | **16** |
| de ellas **sin numero `LD`** | **16** |

La propia tanda dice en prosa **"SE LEEN DIECISEIS"**, y yo cuento **16**:
**CALZA**. Es contraste, no fuente.

**Y AQUI ESTA LA PARADA.** El encargo manda computar *"el siguiente libre ...
igual que `serie_de_registros.py` computa los `R.n`"*, y **la serie `LD` no se
parece a la serie `R.n`**. Corrido HOY el instrumento de la casa que ya existe
para esto, `scripts/loop/vuelta48_contar_ld.py`, salida
`docs/loop/SALIDA_V170_T4A_CONTAR_LD.txt`:

| que se mide | serie `R.n` | serie `LD` |
|---|---:|---:|
| entradas hechas | 31 | **82** |
| rango | R.9 a R.39 | **LD-01 a LD-138** |
| **huecos** | **0** | **54** |
| tramos corridos de huecos | 0 | **2**: LD-12 a LD-27 (**16**) y LD-100 a LD-137 (38) |

**CON CERO HUECOS, "EL SIGUIENTE LIBRE" TIENE UN SOLO SIGNIFICADO. CON 54, NO.**
Los dos caminos dan numeros distintos para las mismas 16 lecturas:

| camino | numeros | a favor | en contra |
|---|---|---|---|
| **1**, la vara literal del encargo (`mayor mas uno`) | **LD-139 a LD-154** | es la vara que el encargo nombra por su nombre, y **no inventa ninguna regla** | pone lecturas del **11 ago 2026** despues de `LD-138`, que es de una tanda muy posterior, y deja los 54 huecos donde estan |
| **2**, rellenar el tramo que encaja | **LD-12 a LD-27** | son **exactamente 16**, los mismos que filas; el tramo **empieza donde acaba la primera tanda (`LD-11`) y acaba donde empieza la tercera (`LD-28`)**, o sea que es el sitio cronologico exacto | **"rellenar huecos" NO es lo que `serie_de_registros.py` hace**, y adoptarlo seria **regla nueva** |

**NO ESCRIBO NINGUNA NUMERACION**, y no es prudencia: es que `EJECUTOR.md` 5
dice que no se inventan reglas, y el propio encargo dice, con estas palabras,
*"Si al contarlas el instrumento dice algo distinto de lo que este encargo
supone, PARAS Y LO TRAES."* **Lo dice, y lo hago.**

**LO QUE HACE FALTA PARA CERRARLA, Y CABE EN UNA LINEA:** decir si el siguiente
libre de la serie `LD` es **el mayor mas uno** o **el primer hueco**. Con esa
linea el instrumento escribe los 16 numeros en una vuelta.

**4.b LOS CINCO NODOS PUENTE DEL SALES ROADMAP: REGISTRADOS MEDIDOS Y NO
EJECUTADOS.** Instrumento
`scripts/loop/vuelta170_tarea4b_registrar_puentes.py`, salida
`docs/loop/SALIDA_V170_T4B_PUENTES.txt`, **exit 0**. Corrido antes en modo
medicion, que no toca la ficha.

**TODO MEDIDO EN ESTA VUELTA CON EL RESOLUTOR DELANTE POR `P.1`**, con la nomina
**parseada** de `scripts/vuelta16_generar_actos.mjs` y no tecleada: 6 miembros
escritos, **6 vivos tras resolver**, 0 colapsados, **15 pares posibles**, **15
con clase y CERO sin clase**, leidos de sus **dos** sedes (10 de la cola de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y 5 de las cabeceras `LD-66` a `LD-70` de
`docs/plan/LD_SALES_ROADMAP.md`).

**LOS CINCO PUENTES, COMPUTADOS DE ESAS CLASES Y NO COPIADOS DE NINGUN ACTA:**

| puente | sus dos `A` |
|---|---|
| `hoja_de_ruta_de_ventas` | `estrategia_de_ventas` , `refinar_sales_roadmap` |
| `refinar_sales_roadmap` | `hoja_de_ruta_de_ventas` , `sales_roadmap_vs_sales_force` |
| `refinar_sales_roadmap` | `sales_roadmap` , `sales_roadmap_vs_sales_force` |
| `sales_roadmap` | `estrategia_de_ventas` , `refinar_sales_roadmap` |
| `sales_roadmap_vs_sales_force` | `customer_validation_sales_roadmap` , `refinar_sales_roadmap` |

**El acta 169 y el reporte de la 169 dicen CINCO; yo computo CINCO: CALZA.**

**Y UNA COSA QUE MI MEDICION ANADE Y NADIE HABIA NOMBRADO:** el par
(`estrategia_de_ventas`, `refinar_sales_roadmap`) lleva **DOS** puentes encima,
`hoja_de_ruta_de_ventas` y `sales_roadmap`. **Eso es lo que `P.10` llama
COSTURA y no punto debil**, con sus palabras: *"un puente puede ser doble ...
y entonces la componente no tiene un punto debil: tiene una costura."*

**LA SALIDA DE `P.10` QUEDA NOMBRADA Y NO SE ELIGE AQUI:** es su **tercera fila
literal**, *"fundir solo el subconjunto CERRADO y enlazar el resto, si todas las
lecturas estan hechas y aun asi se contradicen"*, porque la cobertura es **15 de
15** y por tanto la primera salida, **la unica que resuelve de verdad, ya no
existe**.

**POR QUE NO SE EJECUTA, Y LA BUSQUEDA NEGATIVA VA CON SU COMANDO** (`EJECUTOR.md`
9, *"una busqueda negativa no se puede citar"*): se barrieron **las 71 fichas**
de `docs/plan/OPERACIONES.jsonl` buscando los 6 nodos vivos en los campos
`nodos`, `preservar`, `eliminar` y `superviviente`, y salieron **CERO**.
**Ninguna operacion escrita recoge esta fusion**, y ejecutar una fusion que
ninguna ficha ordena es la improvisacion que `AUDITOR.md` seccion 3 prohibe con
esas palabras.

**LO ESCRITO:** un registro por adicion dentro del campo `nota` de `OP-L-02` que
ya existe, **sin clave nueva de esquema**. La nota pasa de **3.106 a 5.578
caracteres** y **solo crece**; la nota vieja sigue **entera** dentro; los cinco
puentes se nombran en la nota de disco, **5 de 5**; 71 fichas antes y despues;
**cero campos movidos** ademas de `nota`; y el `estado` sigue diciendo `LISTA`.

<!-- FIN ANEXO DE TAREAS -->
