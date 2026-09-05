# REPORTE DE LA VUELTA 170 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta170_esqueleto_reporte.py` **antes de la primera tarea**;
> cada tarea ANEXA SU FILA AL CERRARSE, no al final; y el cierre talla la
> cabecera. **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se
> hizo, y las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se
> hicieron.** Tope de cinco tareas, y el encargo trae exactamente cinco.

**EL VEREDICTO DE UNA LINEA: LA VUELTA 170 HIZO SUS CINCO TAREAS Y NO CERRO
SU REPORTE; ESTE CIERRE LO ESCRIBE LA VUELTA 171, Y LO DICE EN VEZ DE
DISIMULARLO.**

> **QUIEN ESCRIBE ESTE CIERRE, Y CUANDO, PORQUE CALLARLO SERIA MAQUILLARLO.**
> Las secciones 3 a 9 de abajo NO se commitearon en la vuelta 170. Su borrador
> quedo en `scripts/loop/_v170_cierre_texto.md` y el commit `29f04e86`,
> titulado *"EL BLOQUE DE CIERRE DE LA VUELTA 170, ENTERO"*, **toca doce
> ficheros y `docs/loop/REPORTE.md` no es ninguno de ellos** (medido en la
> vuelta 171 por `scripts/loop/vuelta171_apertura.py`, bloque H, salida
> `docs/loop/SALIDA_V171_APERTURA.txt`). **La vuelta 171 las pega aqui TAL COMO
> ESTAN**, sin reescribir una palabra y sin suavizar ninguno de sus **ocho**
> discutibles ni de sus **cinco** caidas (las dos cifras contadas del
> borrador, no tecleadas). **Lo unico que la 171 escribe de su mano en este
> reporte son este recuadro y la seccion 9**, que el borrador dejo con
> cabecera y sin cuerpo.

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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 170`, corrido al
cierre de la vuelta 170, y su salida cruda vive en
`docs/loop/SALIDA_V170_TALLADOR_CABECERA.txt` (2443 bytes, 11 filas de tabla,
contadas por `scripts/loop/vuelta171_tarea1b_cerrar_reporte_170.py`). **Es la
primera vez en dos vueltas que el tallador saca la tabla entera con sus dos
columnas**, y por eso aqui no queda ningun hueco que rellenar.

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `46208790` (asunto real leido de git log: 'ACTA DE LA VUELTA 169 DEL AUDITOR: LAS CINCO TAREAS REPRODUCEN AL DIGITO Y LA BATERIA SALE VERDE POR MI MANO, PERO LA VUELTA SE CONTRADIJO A SI MISMA EN LA MISMA SESION Y ESO ES CIFRA PUBLICADA. NO HAY PARADA'), HEAD real de apertura `46208790` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `220ecb86` (leido de `SALIDA_V170_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | BLOQUEANTE. LOS REGISTROS Y LA CAIDA DE CIFRA PUBLICADA (1.a el acta 169 al `R.39`, 1.b la adjudicacion 6.2 corregida por 9.10 con su tabla de commits medida, 1.c el arnes gana el caso que ANCLA POR MEDICION el nacimiento de la decimotercera tachada) | **CERRADA**, con la bateria declarada al cierre | `SALIDA_V170_T1_REGISTRO_ACTA_169.txt`, `_T1A_MUTACION_REGISTRO`, `_T1B_TACHADAS_POR_COMMIT`, `_T1B_RELECTURA_CONTRA_GIT`, `_T1C_ARNES_RETRATO` |
| **TAREA 2** | LOS DOS INSTRUMENTOS DE PROCESO (2.a el AISLADOR DE LA CIEGA, 2.b el ARCHIVADOR DE REPORTES y el archivado hacia atras del de la 168) | **CERRADA** | `SALIDA_V170_T2A_MUTACION_AISLADOR.txt`, `_T2A_AISLADOR_DEMO`, `_T2B_ARCHIVADOR_168`, `_T2B_MUTACION_ARCHIVADOR` |
| **TAREA 3** | LAS DEUDAS DE CORTE, por 9.21 mas 9.10 (3.a las '53 familias' de `OP-I-01` y su aritmetica de 671, 3.b la fecha de corte del '2.117' en la clausula 2 de `OP-L-01` y de `OP-L-02`) | **CERRADA**, con una discrepancia declarada | `SALIDA_V170_T3_DEUDAS_DE_CORTE.txt` |
| **TAREA 4** | LOS NUMEROS QUE FALTAN (4.a las lecturas dirigidas de la segunda tanda ganan numero `LD` por adicion pura, 4.b los cinco nodos puente del sales roadmap se registran MEDIDOS y NO se ejecutan) | **4.b CERRADA; 4.a MEDIDA Y TRAIDA COMO PARADA** | `SALIDA_V170_T4A_LECTURAS_SIN_NUMERO.txt`, `_T4A_CONTAR_LD`, `_T4B_PUENTES` |
| **TAREA 5** | EL TRABAJO DE VERDAD: CERRAR `OP-L-02` (5.a la FORMA de cada nomina afectada re escrita por 9.26, con su cobertura al lado y el resolutor delante; 5.b el veredicto de las tres clausulas y, solo entonces, la apertura de `OP-L-03`) | **CERRADA**: las tres clausulas de `OP-L-02` CUMPLIDAS, y `OP-L-03` abierta y leida | `SALIDA_V170_T5A_FORMA_NOMINAS.txt`, `_T5B_VEREDICTO_OP_L_02` |
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

### TAREA 5. EL TRABAJO DE VERDAD: CERRAR `OP-L-02`

**5.a LA FORMA DE LAS TRES NOMINAS, RE ESCRITA POR ADICION.** Instrumento
`scripts/loop/vuelta170_tarea5_forma_de_las_nominas.py`, salida
`docs/loop/SALIDA_V170_T5A_FORMA_NOMINAS.txt`, **exit 0**. Corrido antes en modo
medicion, que no toca el inventario.

**LO QUE EL RESOLUTOR SEPARA, Y ES LA MITAD QUE HACIA FALTA.** Una forma escrita
el 11 ago 2026 habla de una nomina que ese dia tenia N nodos vivos. **Desde
entonces la campana ha fundido**, y contar sin resolver haria que una nomina
fundida siguiera pareciendo entera. Cada nomina se mide **dos veces**: como esta
escrita y como queda tras resolver.

| nomina (racimo del inventario) | miembros escritos | vivos tras resolver | pares posibles | leidos | SIN | puentes `P.10` |
|---|---:|---:|---:|---:|---:|---:|
| los cuadrantes de mercado | 6 | **1** | 0 | 0 | 0 | 0 |
| la ecuacion de valor | 5 | 5 | 10 | 10 | 0 | 4 |
| la supervision de la IA | 10 | **7** | 21 | 13 | **8** | 3 |

**LA GORDA, Y NO ESTABA PREVISTA: `los cuadrantes de mercado` ESTA FUNDIDA.** Sus
seis miembros resuelven **todos** a `marco_analisis_mercado_cadena_suministro`
(cinco colapsos por `ids_alias`, nombrados uno a uno en la salida). **No queda
ningun par que leer, asi que ya no tiene forma que medir.** Su `MEZCLADO` con
`15 de 15` era cierto en su corte y se queda entero al lado.

**LA SEGUNDA, Y OBLIGA A ESCRIBIR DOS CIFRAS EN VEZ DE UNA:** `la supervision de
la IA` **como racimo entero** esta **PROVISIONAL, 13 de 21**, con 8 pares sin
leer y 3 colapsos; **pero la nomina que `OP-L-02` cerro es un SUBCONJUNTO suyo**,
el bloque humano, y **esa si esta 10 de 10, cero sin veredicto, reparto A 5 D 5**.
**Las dos cifras son ciertas y hablan de universos distintos**, y por eso las dos
van escritas en el mismo campo, medidas por **la misma maquina en la misma
corrida**. Escribir solo la del racimo habria hecho parecer que la segunda tanda
no cerro nada.

**`9.16` VIAJA CON CADA FORMA QUE SE ESCRIBE**, y no de adorno: `la ecuacion de
valor` cierra 10 de 10 **pero NO se funde**, porque trae **4 nodos puente de
`P.10`** y `P.10` dice que la componente no se funde hasta que el triangulo se
cierre. La forma lo dice con sus puentes nombrados.

**LAS GUARDAS:** la forma vieja y la cobertura vieja **siguen enteras dentro de
las tres** (comprobado antes de escribir, y el instrumento cae en rojo si no);
**672 entradas antes y despues**; **reparto por tipo identico** antes y despues;
las tres siguen en sus lineas 237, 233 y 241; **9 claves antes y 9 despues**;
**cero campos movidos** ademas de `forma` y `cobertura`; y **el `estado` de las
tres sin mover**.

**UNA CAIDA MIA, CAZADA POR MI Y DECLARADA:** mi primer parche pego la coletilla
del subconjunto **dos veces** en `la supervision de la IA`. Lo vi al leer el
campo en disco, restaure `INVENTARIO.jsonl` con `git checkout`, arregle el
instrumento y lo volvi a correr. **La forma pasa de 1.064 a 753 caracteres**, que
es la diferencia exacta de la coletilla repetida.

**5.b EL VEREDICTO DE `OP-L-02`, CON LA MEDICION DELANTE.** Instrumento
`scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py`, salida
`docs/loop/SALIDA_V170_T5B_VEREDICTO_OP_L_02.txt`, **exit 0**. Las clausulas
**se leen de la ficha**, y las `CORRECCION DECLARADA` se separan de ellas porque
**una correccion no es una clausula que cumplir**: 4 elementos en
`verificacion`, **3 clausulas** y 1 correccion.

| clausula | como se midio | veredicto |
|---|---|:-:|
| **1**. *las tres nominas afectadas quedan con cobertura COMPLETA y su forma reescrita* | las **seis** nominas de `OP-L-02` con el resolutor delante dan **0 pares sin veredicto**; y las tres formas llevan hoy el corte `2026-09-04` escrito | **CUMPLIDA** |
| **2**. *el marcador del cribado no se mueve: sigue en 2.117* | marcador recomputado **3.388** (A 551, B 72, C 5, D 2.760); `git diff 46208790 HEAD --numstat -- docs/INTRA_DOMINIO_VEREDICTOS.jsonl` da **0 filas**, y sin commitear **0 filas** | **CUMPLIDA** |
| **3**. *cada grupo del backlog lleva su motivo escrito, no solo su cuenta* | la tabla del backlog de `LECTURAS_DIRIGIDAS.md`, contada fila a fila: **4 grupos, 4 con motivo escrito, 0 sin** | **CUMPLIDA** |

**LAS TRES CLAUSULAS QUEDAN CUMPLIDAS, 3 de 3, Y LO DIGO CON LA MEDICION
DELANTE.** Y **el campo `estado` NO SE TOCA**: sigue diciendo `LISTA` y **no es
la vara**, por la decision del fundador del 4 sep 2026. La vara corrida al lado,
`scripts/loop/vuelta150_3_relectura_expediente.py --corte HEAD`: **71 fichas, 37
que no calzan, 24 congeladas declaradas, 12 congeladas en silencio, 1 HECHA sin
prueba y 6 en LISTA sin prueba**, exit 0.

**Y SOLO ENTONCES, `OP-L-03` SE ABRE LEYENDO SU FICHA Y SIN EJECUTAR NADA.**
Linea 43, tipo `MESA`, `estado` `LISTA`, `fecha_corte` 2026-08-11, `depende_de`
las seis `OP-D-*`, `bloquea_a` `OP-U-01` y `OP-U-02`.

**AQUI VA UN CONTRASTE MEDIDO QUE NO CALZA CON EL ENCARGO, Y NO ES PARADA:** el
encargo dice *"leer sus cuatro clausulas"*, y la ficha trae **4 elementos** en
`verificacion` **pero solo 3 son clausulas**; el cuarto es una `CORRECCION
DECLARADA`. **Cuento 3, no 4.** No paro por esto porque la tarea era leerlas y
las tres estan leidas, pero **la cifra del encargo se corrige con la medicion
delante en vez de repetirse**:

1. *ningun acto se funde con un par interno sin veredicto*
2. *las 55 lecturas marcadas LECTURA DIRIGIDA: no entran en la cola ni mueven su marcador*
3. *cada acto cuya lectura completa cambie su forma se re-mide con su cobertura al lado*

Su `adjudicacion`, leida hoy: *"LOS 55 DEJAN DE SER BACKLOG. Por la regla `P.5`,
cada acto que vaya a fundirse se lee ENTERO despues de su destejido y antes de su
fusion. Los 55 pares se reparten entre 29 actos y bajan del backlog."*

**NINGUNA DE LAS TRES SE EJECUTA EN ESTA VUELTA**, y no por prudencia: el tope de
cinco tareas esta agotado y esta es la quinta. **Lo leido queda aqui para que la
vuelta siguiente empiece con la ficha abierta y no con la ficha por abrir.**

<!-- FIN ANEXO DE TAREAS -->

## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LOS COMMITS DE LA VUELTA, LEIDOS DE `git log 46208790..HEAD`: OCHO.**

| # | commit | que cierra |
|---:|---|---|
| 1 | `abb85566` | la apertura, el bloque ENTERO |
| 2 | `4c6fd7c1` | el archivador, el archivado hacia atras y el esqueleto |
| 3 | `e6840378` | TAREA 1 (y el aislador de la 2.a) |
| 4 | `47323f12` | TAREA 2 |
| 5 | `222ca6a7` | TAREA 3 |
| 6 | `28c5a5dc` | TAREA 4 |
| 7 | `220ecb86` | TAREA 5 |
| 8 | `29f04e86` | el bloque de cierre y la cabecera tallada |

**EL GRAFO NO SE MOVIO, PROBADO Y NO CREIDO:**
`git diff 46208790 HEAD --numstat -- dataset/ web/ engine/` sale **VACIO, cero
filas**. Las **69 rutas** que la vuelta toca son **47 de `docs/loop/`, 17 de
`scripts/loop/`, 2 de `docs/plan/`, 2 de `docs/loop/reportes/` y 1 de `docs/`**.
**Cero nodos tocados, cero aristas movidas, cero clases movidas.**

**EL COMMIT QUE LLEVA ESTE REPORTE NO SE NOMBRA AQUI**, porque se crea despues
de escribirlo. El `HEAD` de cierre que la cabecera publica, `220ecb86`, es el
sello leido de `git rev-parse HEAD` **tras la ultima operacion**, que es lo unico
que se puede leer sin inventarlo.

## 4. LA PARADA, Y ES UNA

**LA NUMERACION `LD` DE LAS 16 LECTURAS DE LA SEGUNDA TANDA NO SE PUEDE ESCRIBIR
SIN INVENTAR UNA REGLA.** Esta medida entera en la TAREA 4.a y no se repite aqui.
En una linea: **la serie `R.n` tiene 0 huecos y la serie `LD` tiene 54**, asi que
*"el siguiente libre"* significa **`LD-139`** por la vara que el encargo nombra y
**`LD-12`** por el tramo que encaja al numero, y **elegir entre los dos es
escribir doctrina**. `EJECUTOR.md` 5 lo prohibe y el propio encargo manda parar.

**LO QUE HACE FALTA PARA CERRARLA CABE EN UNA LINEA:** decir si el siguiente
libre de la serie `LD` es **el mayor mas uno** o **el primer hueco**. Con eso, el
instrumento escribe los 16 numeros en una vuelta, por adicion pura y sin tocar
una palabra de su texto.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Los marco ahora, con la relectura ciega del auditor por delante y sin saber
como va a adjudicarlos.**

- **`D.1` `node_modules/` NO ENTRA EN `.gitignore` POR MI MANO.** El arbol abrio
  con un solo fichero no seguido, `node_modules/.vite/vitest/.../results.json`,
  **12.460 bytes**, cache de `vitest`. Lo medi y lo declare, **pero no lo meti en
  `.gitignore`**: eso seria decidir por el fundador sobre un fichero que el
  encargo no nombra. **Discutible: puede que la decision correcta fuera anadirlo
  y que dejarlo suelto sea dejar basura ocho vueltas mas.**
- **`D.2` EL ARCHIVADOR NO SE ENCHUFA SOLO.** `archivar_reporte.py` existe y
  archivo dos reportes, **pero nadie lo llama automaticamente en la apertura**.
  Esta vuelta lo corrio a mano. **Discutible: puede que la adjudicacion 6.4
  quisiera el automatismo dentro del esqueleto, y yo lea de menos.**
- **`D.3` A `OP-L-01` NO LE ESCRIBI UNA SEGUNDA CORRECCION.** Su clausula 2 ya
  tiene una fechada desde la vuelta 166 y escribir otra igual seria dejar dos
  versiones de lo mismo. **Discutible: el encargo dice "se le pone por adicion" a
  las dos, y yo se lo puse a una.**
- **`D.4` EL CAMPO `forma` DE `la supervision de la IA` LLEVA DOS UNIVERSOS.**
  Escribi la del **racimo entero** (PROVISIONAL, 13 de 21) como cuerpo y la de la
  **nomina de `OP-L-02`** (10 de 10) como coletilla. **Discutible: puede que el
  campo `forma` de un racimo deba hablar SOLO del racimo, y la nomina tenga que
  ir a otro sitio.**
- **`D.5` ESCRIBI LA PALABRA `FUNDIDA` EN UN CAMPO `forma`.** Los cuadrantes de
  mercado resuelven a un solo nodo vivo y no tienen forma que medir, asi que
  escribi `FUNDIDA`. **Discutible: no he encontrado esa palabra en el vocabulario
  de formas de la casa (`MEZCLADO`, `SUB-PURO`, `PARTIDO`, `PROVISIONAL`,
  `REPITE`), y puede que estrenar una palabra sea inventar doctrina.**
- **`D.6` PARE EN LA 4.a EN VEZ DE RELLENAR EL HUECO.** El tramo `LD-12` a
  `LD-27` mide **exactamente 16** y esta **exactamente** entre la primera tanda y
  la tercera. **Discutible: puede que la coincidencia sea tan cerrada que no haya
  regla que inventar, y que parar sea de mas.**
- **`D.7` LOS DOS ARNESES NUEVOS ENTRAN EN LA NOMINA DE LA BATERIA EL MISMO DIA
  QUE NACEN.** La condicion desde la vuelta 148 es **sujeto congelado**, no el
  plazo, y creo que los dos la cumplen (actas de mentira en memoria mas un acta
  ya firmada; filas y pasos fabricados en memoria). **Discutible: puede que el
  acta 169 quiera plazo igual, como lo discutio para el de la 169.**
- **`D.8` TRAIGO EL AGUJERO DEL `R.38` COMO HALLAZGO Y NO LO CORRIJO.** La
  entrada `R.38` afirma que su arnes hermano prueba el barrido por mutacion y ese
  arnes no existe. **No lo corrijo porque no es mio y el encargo no lo nombra.**
  **Discutible: puede que una afirmacion falsa en `docs/PENDIENTES.md` haya que
  corregirla la vea quien la vea.**

## 6. LAS PREGUNTAS

- **`P.1`** ¿El siguiente libre de la serie `LD` es **el mayor mas uno** o **el
  primer hueco**? Es la PARADA, y es lo unico que bloquea 16 numeros.
- **`P.2`** La celda de `docs/plan/00_INDICE.md:644` publica **81** lecturas
  hechas con corte **19 ago 2026** y el mismo instrumento mide **82** hoy (entro
  `LD-138-01`). **No es una mentira**, lleva su corte escrito. ¿Se le adosa la
  cifra de hoy por `9.21`, o se deja hasta que alguien la encargue?
- **`P.3`** Cuando la nomina de una operacion es un **subconjunto** de un racimo
  del inventario, ¿que universo manda en el campo `forma` del racimo?
- **`P.4`** ¿Existe un vocabulario cerrado para el campo `forma`? Si existe, ¿en
  que pagina, y cabe `FUNDIDA` en el?
- **`P.5`** Los 8 pares sin leer de `la supervision de la IA` (racimo entero)
  quedan medidos y nombrados uno a uno. ¿Entran en alguna operacion escrita, o
  son backlog nuevo?

## 7. PENDIENTES DE DOCTRINA

- **`PD.1` NO HAY REGLA PARA "EL SIGUIENTE LIBRE" DE UNA SERIE CON HUECOS.**
  `serie_de_registros.py` computa `mayor mas uno` porque su serie no tiene
  huecos; la serie `LD` tiene 54. La regla que falta es de una linea y sirve para
  las dos series a la vez. **Es la PARADA de la 4.a.**
- **`PD.2` NO HAY VOCABULARIO ESCRITO PARA EL CAMPO `forma`.** El inventario usa
  hoy `MEZCLADO`, `SUB-PURO`, `PARTIDO n mas m mas k`, `PROVISIONAL` y frases
  libres. Sin nomina cerrada, cada vuelta puede estrenar una palabra sin que nada
  lo cace. **Yo estrene una (`FUNDIDA`) y lo declaro en `D.5`.**
- **`PD.3` NO HAY REGLA SOBRE EL SUBCONJUNTO.** Cuando una operacion cierra una
  nomina que es parte de un racimo, no esta escrito si la forma del racimo se
  reescribe, se deja, o se reescribe con las dos cifras. **Yo elegi las dos
  cifras y lo declaro en `D.4`.**

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

- **`CAIDA 1`. CORRI `run_phase1.py` SUELTO**, sin los pasos 2, 3 y 4 del ciclo,
  que es exactamente lo que el encargo prohibe con esas palabras. **La cazo el
  guardian del commit**: 71 nodos divergentes de `etiqueta_arbol`, commit
  ABORTADO. **El remedio no fue saltarse el guardian**: corri el ciclo entero
  **dos veces seguidas** para probar que cierra, y las dos dan Gate 0 OK y
  `numstat` en cero filas (`docs/loop/SALIDA_V170_T3_CICLO_REPARADO.txt`).
- **`CAIDA 2`. UNA GUARDA MIA MIDIO LO COMODO EN VEZ DE LO QUE IMPORTA.** En la
  TAREA 3 comprobaba que el **total** de apariciones del `53` no cambiara, y la
  correccion nueva nombra esa cifra varias veces porque **es de lo que habla**:
  salio ROJA **despues** de escribir. Restaure `OPERACIONES.jsonl` con
  `git checkout`, cambie la guarda a lo que importa (**que las siete viejas
  sobrevivan enteras**) y la volvi a correr. **La guarda no se aflojo: se
  reapunto.**
- **`CAIDA 3`. PEGUE LA MISMA COLETILLA DOS VECES.** En la TAREA 5.a, el campo
  `forma` de `la supervision de la IA` salio con la coletilla del subconjunto
  duplicada. **La vi leyendo el campo en disco despues de escribir**, restaure
  `INVENTARIO.jsonl` con `git checkout`, arregle el instrumento y lo volvi a
  correr: **de 1.064 a 753 caracteres**, la diferencia exacta.
- **`CAIDA 4`, Y ESTA LA CAZO LA RELECTURA AL DOBLE ANTES DE PUBLICARLA.** Mi
  primera version de la tabla de commits del comentario del arnes puso
  `c6ac70f6` en la **vuelta 166**, y es de la **167**. La cazo el propio
  instrumento al computar la vuelta de las actas en vez de leerla del asunto.
  **Habria sido una cifra falsa en la CUARTA SEDE, o sea la misma especie que
  esta vuelta venia a corregir**, y por eso la declaro aunque no llegara a
  commitearse.
- **UNA QUINTA, MECANICA Y SIN CONSECUENCIA, y la digo por no elegir cuales
  cuento:** tres intentos de parchear ficheros con `heredoc` me convirtieron
  secuencias de escape en saltos de linea reales y dejaron ficheros que no
  parseaban. **Ninguno llego a commitearse**, los tres los cazo el propio
  interprete al correr, y el remedio fue escribir los ficheros enteros en vez de
  parchearlos.

## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE

**NO CORRIO. Y SE DICE CON LA MEDICION DELANTE EN VEZ DE RELLENARSE CON UNA
CORRIDA DE OTRA VUELTA.** `docs/loop/SALIDA_V170_BATERIA.txt` **existe y mide
0 bytes**, medido en la vuelta 171 por
`scripts/loop/vuelta171_tarea1b_cerrar_reporte_170.py` con `os.path.getsize`.
El fichero de salida se creo y **la corrida no llego a escribir ni una linea**:
la vuelta 170 se corto antes de lanzarla.

**AQUI NO SE PEGA UNA CORRIDA DE LA VUELTA 171.** Escribir en la seccion 9 del
reporte de la 170 una bateria corrida en otra vuelta seria publicar como de una
vuelta lo medido en otra, que es **exactamente la especie que esta campana
persigue**. El hueco se declara y no se rellena.

**LA BATERIA DE LA VUELTA 170 SI ESTA CORRIDA, PERO POR OTRA MANO Y EN OTRO
SITIO, Y AHI ES DONDE HAY QUE IR A LEERLA:** seccion 5 del acta del auditor de
la vuelta 170, *"LA BATERIA DE MUTACIONES, CORRIDA POR MI MANO"*, en
`docs/loop/ACTA_AUDITOR.md:57574` (linea localizada por este instrumento, no
tecleada). **Su cifra es del auditor y lleva su atribucion**: 75 entradas en la
nomina, exit 0, ANCLA PERDIDA 0, NO MORDIO 0, NO REPRODUCIBLE 0, y los dos
CASO DECLARADO de siempre. **Esa corrida no es de este reporte y por eso se
cita y no se copia como propia.**
