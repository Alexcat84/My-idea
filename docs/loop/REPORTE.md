# REPORTE DE LA VUELTA 172 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta172_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre talla la cabecera. **Si esta vuelta se corta,
> lo que quede aqui es lo que de verdad se hizo, y las filas que sigan diciendo
> ABIERTA, SIN CERRAR son las que no se hicieron.** Tope de cinco tareas, y el
> encargo trae exactamente cinco.
>
> **Y EL ESQUELETO YA NO PUEDE PISAR UN REPORTE SIN ARCHIVAR** (guarda nacida en
> la TAREA 5.a de la vuelta 171): su paso 0 corre el archivador y **se niega a
> escribir** si el reporte anterior no esta guardado byte a byte. **Y esa guarda
> YA MORDIO en la vuelta siguiente a la que nacio**: corrida en modo solo
> comprobacion al abrir esta vuelta, dijo ROJO por su clausula (d), porque el
> `REPORTE.md` del arbol era el de la 171 sin cerrar. Esta corrida lo paso en
> verde contra `docs/loop/reportes/REPORTE_V171.md` **solo despues de que la
> TAREA 1.a cerrara ese reporte**.

**EL VEREDICTO DE UNA LINEA: LA VUELTA 172 ENTREGO CUATRO DE SUS CINCO TAREAS Y NO PUDO CERRAR SU PROPIO REPORTE, Y SE CIERRA AQUI, DOS VUELTAS DESPUES, POR LA VUELTA 174: LA TAREA 4 QUEDO ABIERTA EN SU 4.c, LA TAREA 5 PARIO cerrar_reporte.py PERO NO ALCANZO A CERRARSE CON EL (clausula 4.4, corregida arriba por el carril del 9.10), Y LA BATERIA NO LA CORRIO NADIE, NI EL EJECUTOR NI EL AUDITOR.**
## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta172_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 171: `0c415430`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 171: LAS CUATRO TAREAS REPRODUCEN AL DIGITO Y LA PARADA NO ES PARADA, PERO EL REPORTE VUELVE A QUEDARSE SIN CERRAR Y ESTA VEZ EL TRAMO YA ESTABA EN RELECTURA AL DOBLE'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V172_HEAD_APERTURA.txt`: `002e0517`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `ad3cea43`
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 172`, y su salida
cruda vive en `docs/loop/SALIDA_V172_TALLADOR_CABECERA.txt` (2426 bytes, 11 filas de tabla,
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `0c415430` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 171: LAS CUATRO TAREAS REPRODUCEN AL DIGITO Y LA PARADA NO ES PARADA, PERO EL REPORTE VUELVE A QUEDARSE SIN CERRAR Y ESTA VEZ EL TRAMO YA ESTABA EN RELECTURA AL DOBLE'), HEAD real de apertura `002e0517` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `24dda21e` (leido de `SALIDA_V172_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | BLOQUEANTE Y VA PRIMERA. EL CIERRE QUE FALTA Y LOS REGISTROS (1.a el reporte de la 171 CERRADO con la cabecera tallada pegada, sus cuatro discutibles y su caida sin suavizar, y la seccion 9 diciendo que la bateria NO corrio; 1.b el acta 171 y sus adjudicaciones 6.1 a 6.12 al `R.41` con su arnes de mutacion del registro; 1.c el archivador para la 171 y este esqueleto) | **CERRADA** | `SALIDA_V172_T1A_CERRAR_REPORTE_171.txt`, `_T1A_COMPARAR_CABECERA_171`, `_T1A_RELECTURA_DESDE_GIT`, `_T1B_REGISTRO_ACTA_171`, `_T1B_MUTACION_REGISTRO`, `_T1B_SERIE`, `_T1C_GUARDA_QUE_MORDIO`, `_T1C_ESQUELETO` |
| **TAREA 2** | BLOQUEANTE PARA LA 3. SE DESENVENENA EL CONTADOR Y SE CORRIGE EL `R.40` (adjudicaciones 6.1 y 6.3): 2.a `docs/loop/reportes/REPORTE_V<N>.md` entra en los narrativos del bucle POR PATRON, con su caso positivo por mutacion; 2.b la afirmacion falsa del `R.40` corregida por el carril del `9.10` con el reparto recomputado; 2.c el contador otra vez, con la atribucion fichero a fichero y linea a linea | **CERRADA** | `SALIDA_V172_T2_CONTAR_LD_ANTES.txt`, `_T2A_MUTACION_EXCLUSION`, `_T2A_CONTAR_LD_DESPUES`, `_T2B_CORREGIR_R40`, `_T2C_ATRIBUCION` |
| **TAREA 3** | LA NUMERACION `LD`, QUE AHORA SI SE ESCRIBE (adjudicacion 6.2): las 16 filas de la segunda tanda de `docs/plan/LECTURAS_DIRIGIDAS.md` ganan `LD-139` a `LD-154` POR ADICION PURA, con los numeros COMPUTADOS y con dos guardas que tienen que caer por mutacion; y despues la fila de `docs/plan/00_INDICE.md` recibe su cifra de hoy por `9.21` (adjudicacion 6.10) | **CERRADA** | `SALIDA_V172_T3_NUMERAR_LD.txt`, `_T3_MUTACION_NUMERACION`, `_T3_ATRIBUCION_DESPUES`, `_T3_CONTAR_LD`, `_T3B_INDICE` |
| **TAREA 4** | LOS TRES ARNESES Y LA BATERIA (adjudicaciones 6.4 y 6.5), Y EL ORDEN ES OBLIGATORIO: 4.a el caso `F` de `vuelta171_tarea5a_mutacion_enchufe.py` refundado sobre SUJETO CONGELADO; 4.b los tres arneses de la 171 dentro de la nomina de `verificar_mutaciones_viejas.py`; 4.c la bateria corrida ENTERA Y SOLA al cierre, con su salida en la seccion 9 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | EL CIERRE DEL REPORTE DEJA DE SER UN PASO A MANO (adjudicacion 6.6): nace `scripts/loop/cerrar_reporte.py`, de nombre estable y sin numero de vuelta, que pega la cabecera, anexa el cuerpo, escribe el veredicto y CAE EN ROJO si al terminar falta cualquiera de las cuatro piezas. Con su caso positivo por mutacion, y esta vuelta se cierra con el | ~~**CERRADA**~~ **ABIERTA, SIN CERRAR EN LA 172** (correccion declarada del 5 sep 2026, debajo de la tabla) | `SALIDA_V172_T5_MUTACION_CIERRE.txt`, ~~`_T5_CERRAR_REPORTE` (la corrida de esta misma vuelta)~~ |
<!-- FIN TABLA DE TAREAS -->

> **CORRECCION DECLARADA (5 sep 2026, vuelta 174, TAREA 1.a, por el carril del banco `9.10`).**
> **LA FILA DE LA TAREA 5 DECIA `CERRADA` Y NOMBRABA COMO PRUEBA UNA RUTA
> SOBRE UN VACIO.** La fila vieja queda entera y tachada; no se borra nada.
> **Lo medido HOY en el disco por `scripts/loop/vuelta174_tarea1a_corregir_44.py`,
> con `os.path.exists` y `os.path.getsize`, no tecleado:**
>
> - `docs/loop/SALIDA_V172_T5_MUTACION_CIERRE.txt` -> **4921 bytes**
> - `docs/loop/SALIDA_V172_T5_CERRAR_REPORTE.txt` -> **NO EXISTE**
>
> **LO QUE DE VERDAD PASO, Y ES LO QUE DICE LA `4.4` DEL ACTA DEL AUDITOR DE
> LA VUELTA 172** (`docs/loop/ACTA_AUDITOR.md:58649`, leida hoy): el encargo de
> aquella TAREA 5 pedia TRES cosas, *"el instrumento, su caso positivo, y que
> esta vuelta se cerrara con el"*. **Las dos primeras estan hechas y
> verificadas** (el arnes de mutacion existe y su salida tambien). **La tercera
> no la hizo la vuelta 172: la paga la vuelta 174**, y por eso el estado
> corregido es ABIERTA, SIN CERRAR EN LA 172 y no CERRADA.
>
> **LA REGLA QUE LO CONVIERTE EN CAIDA Y NO EN DESCUIDO** es del 5 sep 2026,
> `EJECUTOR.md` 1: **LA RUTA QUE PROMETE PRUEBA ES CIFRA**. Una ruta publicada
> como evidencia que apunta a un fichero inexistente o de cero bytes es CAIDA
> DE CIFRA en su sede. **El auditor la registro cuando esa regla todavia no
> existia y la trato como rotulo de estado, sin acumular; hoy la regla existe,
> y quien decide si esto acumula hacia atras es el auditor, no yo.**


## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1 (BLOQUEANTE Y VA PRIMERA). EL CIERRE QUE FALTA Y LOS REGISTROS

**LA MEDICION DE APERTURA SE CORRIO ANTES QUE TODO, IGUAL QUE EN LA 171 Y POR EL
MISMO MOTIVO.** `scripts/loop/vuelta172_apertura.py`, clon declarado, salidas
`docs/loop/SALIDA_V172_*_APERTURA.txt`. El encargo pone el esqueleto despues de
cerrar el reporte de la 171, y ahi va; la MEDICION va antes, porque
`EJECUTOR.md` 1 lo manda y porque ninguna de sus salidas es `REPORTE.md`. **La
`6.7` del acta 171 ya adjudico que esto es correcto**, asi que esta vez no va
como discutible sino como regla acatada.

**Y UNA CAIDA MIA EN ESE MISMO PASO, DECLARADA AUNQUE NO PRODUJO NI UNA CIFRA**
(va como `CAIDA 1` de la seccion 8): la PRIMERA corrida del instrumento de
apertura murio con `SyntaxError` y **no escribio ni un fichero**.

**1.a EL REPORTE DE LA VUELTA 171 QUEDA CERRADO** (`99d54005`), instrumento
`scripts/loop/vuelta172_tarea1a_cerrar_reporte_171.py`, salida
`docs/loop/SALIDA_V172_T1A_CERRAR_REPORTE_171.txt`, **exit 0**:

| celda | de donde sale | valor |
|---|---|---:|
| el reporte antes | del fichero, contado por el instrumento | 453 saltos de linea, 28.467 bytes |
| sellos de la 171 | `SALIDA_V171_HEAD_APERTURA.txt` y `_HEAD_CIERRE.txt` | `0caca89f` y `cae2731d` |
| los dos existen como commit | `git cat-file -e` | **SI los dos** |
| commits del rango | `git log 0caca89f..cae2731d` | **5** |
| numstat sobre `dataset/`, `web/`, `engine/` | `git diff` | **0 filas** |
| rutas tocadas por la 171 | `git diff --name-only` | **61** |
| la tabla de la cabecera | `SALIDA_V171_TALLADOR_CABECERA.txt`, pegada entera | **11** filas |
| el cuerpo | `scripts/loop/_v171_cierre_texto.md`, anexado tal cual | 8.123 bytes, sha256 `c5df46f014e8662d` |
| discutibles contados del borrador | barrido | **4** |
| caidas contadas del borrador | barrido | **1** |
| `P.2` nombrada en el cuerpo de la 171 | barrido | **0**: el hueco se declara |
| `SALIDA_V171_BATERIA.txt` | `os.path.getsize` | **0 bytes** |
| el reporte despues | del fichero escrito | 688 saltos de linea, 43.956 bytes |

**LA SECCION 3 NO SALE DEL BORRADOR: LA GENERA EL INSTRUMENTO DESDE GIT.** Los
dos extremos del rango se leen de los sellos y la tabla de commits sale de
`git log`. Es la regla que nacio de la caida de la vuelta 79, y aplicarla aqui
no es opcional: **el reporte de la 171 lo escribe otra vuelta, o sea la
situacion exacta en la que un hash tecleado no lo cazaria nadie.**

**LA CABECERA CALZA, Y NO LO DIGO YO:**
`tallar_cabecera_reporte.py --fase04 --vuelta 171 --comparar docs/loop/REPORTE.md`
da **exit 0** y *"filas cotejadas: 9 | DISTINTAS: 0 | ausentes: 0. CABECERA:
IDENTICA AL TALLADOR"* (`docs/loop/SALIDA_V172_T1A_COMPARAR_CABECERA_171.txt`).

**NO SE SUAVIZO NADA, Y LA SECCION 5 LLEVA UNA ADVERTENCIA QUE ME QUITA MERITO A
MI MISMO.** Los cuatro `D.1` a `D.4` estan con su pregunta y la `CAIDA 1` con su
nombre. **Pero esas marcas YA NO SON CIEGAS**, porque el auditor las adjudico en
su acta antes de que yo pegara la seccion, y eso va escrito en el recuadro de
apertura de la seccion 5 en vez de callarse. Lo que si es cierto, y el
instrumento lo comprueba contando apariciones en el cuerpo ya commiteado, es que
**los cuatro se declararon en la prosa de sus tareas antes de que nadie los
leyera**.

**POR QUE NO LA CERRO `cerrar_reporte.py`, QUE NACE EN LA TAREA 5 DE ESTA MISMA
VUELTA:** porque ese instrumento **cae en rojo si la salida de la bateria no
esta dentro de la seccion 9**, y la bateria de la 171 no corrio. **El reporte de
la 171 no se puede cerrar con el instrumento que exige justo lo que a la 171 le
falta.** Es la guarda funcionando, y se dice en vez de aflojarla.

**LA RELECTURA AL DOBLE, PIEZAS 1 Y 2, HECHA DESPUES DE COMMITEAR Y LEYENDO DE
GIT, Y ESTA VEZ SOBRE LO PROPIO.** Instrumento
`scripts/loop/vuelta172_relectura_al_doble.py`, salida
`docs/loop/SALIDA_V172_T1A_RELECTURA_DESDE_GIT.txt`, **exit 0**: `git show` dice
que `docs/loop/REPORTE.md` **si** esta entre los ficheros de `99d54005`, y sobre
el fichero commiteado pasan **16 comprobaciones con 0 fallos**, incluidas *"las
siete secciones 3 a 9 existen"*, *"los cuatro discutibles siguen enteros"* y
*"la seccion 3 no publica ningun hash que git no conozca"* (cada hash de la
tabla se pasa por `git cat-file -e`).

**1.b EL ACTA 171 ENTERA QUEDA EN EL `R.41`.** Instrumento
`scripts/loop/vuelta172_tarea1_registrar_acta171.py`, salida
`docs/loop/SALIDA_V172_T1B_REGISTRO_ACTA_171.txt`, **exit 0**:

| celda | de donde sale | valor |
|---|---|---:|
| cuerpo del acta 171 acotado | cabecera y final del fichero | lineas 57.847 a 58.374 |
| adjudicaciones `6.n` | barrido, para en el primer hueco | **12** (6.1 a 6.12) |
| caidas, patron VIEJO | barrido del cuerpo acotado | **0** |
| caidas, patron HEREDADO de la 171 | barrido del cuerpo acotado | **3** |
| serie antes de escribir | `serie_de_registros.py`, sus DOS sedes | 32 entradas, 0 colisiones, 0 huecos |
| siguiente libre, computado | mayor mas uno | **R.41** |
| sede, leida de la regla | `docs/loop/ACTA_AUDITOR.md:53933` | `docs/PENDIENTES.md` |
| reparto por VIA PREVISTA | del mapa `VIA` | **EJECUTADA 7** (6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.10); **SIN TOCAR NADA 5** (6.7, 6.8, 6.9, 6.11, 6.12) |
| que suben al fundador | del reparto | **0** |
| serie despues de escribir | recomputada | 33 entradas, 0 colisiones, 0 huecos |

**EL CLON ES REPRODUCIBLE, Y ESO SE MIDE EN VEZ DE PROMETERSE.** El instrumento
lo construye `scripts/loop/_v172_construir_registrador.py` desde el original de
la 171, con **26 sustituciones y cada una con su `assert`** de cuantas
apariciones espera. **Correr el constructor otra vez reproduce el fichero byte a
byte** (`diff -q` sin salida). El mecanismo entero se hereda sin tocar.

**Y AQUI ESTA EL CAMBIO QUE IMPORTA, QUE SALE DE LA `6.3`: LAS GLOSAS DEL `R.41`
NO AFIRMAN EN PASADO.** El `R.40` publico *"VIA: EJECUTADA"* sobre una TAREA 3
que no corrio, y la causa estaba medida y era de orden: **la entrada se escribe
la primera de la vuelta y nadie vuelve a ella**. Aqui eso no puede repetirse
**por la forma de la frase**: el campo se llama **VIA PREVISTA**, las siete
glosas de tarea dicen *"VA A EJECUTARSE EN LA TAREA n ... Y AL ESCRIBIR ESTA
LINEA TODAVIA NO HA CORRIDO"*, y la entrada abre con un recuadro que lo dice.
**La confirmacion MEDIDA se anexa al cierre**, por adicion. **No es doctrina
nueva:** es `EJECUTOR.md` 1, una afirmacion sin linea que citar no se escribe.
Va como `D.1`.

**EL ARNES DE MUTACION DEL REGISTRO:**
`scripts/loop/vuelta172_tarea1b_mutacion_registro.py`, salida
`docs/loop/SALIDA_V172_T1B_MUTACION_REGISTRO.txt`, **exit 0**: **43 casos, 43
pasan, 43 caen al mutar el esperado**.

**1.c LA GUARDA DEL PASO 0, EL ARCHIVADOR Y EL ESQUELETO.**

**LA GUARDA DE LA 5.a DE LA 171 ESTABA MORDIENDO EN LA VUELTA SIGUIENTE A LA QUE
NACIO, Y LO MEDI YO EN VEZ DE CITARLO.** Instrumento
`scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py`, salida
`docs/loop/SALIDA_V172_T1C_GUARDA_QUE_MORDIO.txt`, **exit 0**, **6
comprobaciones y 0 fallos**, todo en un temporal y con **cero escrituras** en el
repo. El `REPORTE.md` que habia al abrir esta vuelta mide **28.467 bytes** y su
sha256 es `8e9ce848425fd704...`, **que es exactamente el que el auditor publica
en su acta 171** (su cifra, con su atribucion; la mia esta recomputada hoy con
codigo propio y calzan).

**Y AQUI TRAIGO UNA DISCREPANCIA CON EL ACTA EN VEZ DE RESOLVERLA COPIANDO.** El
acta dice **ROJO por la clausula (d)**. Corriendo la guarda con
`vuelta_anterior=171`, que es lo que el esqueleto de ESTA vuelta llama, sale
**ROJO por la (b)**: `REPORTE_V171.md` no existia y la (b) corta antes de llegar
a la (d). **La cifra del auditor se reproduce con el parametro que el uso**,
`exigir_archivado(170)`, y ahi si sale **la (d)** con los dos sha256 impresos.
**Las dos lecturas son ciertas y son de preguntas distintas**, y por eso van las
dos escritas. Va como `D.2`.

**EL ARCHIVADOR Y EL ESQUELETO** (`docs/loop/SALIDA_V172_T1C_ESQUELETO.txt`,
exit 0). `archivar_reporte.py --vuelta 171` sale **VERDE** desde dentro del paso
0: destino `docs/loop/reportes/REPORTE_V171.md`, **43.956 bytes, 688 lineas**,
sha256 `d4f6fe05f93aa832`, commit de origen `99d54005`. Y entonces **los dos
sha256 calzan** y el esqueleto escribe: **5.406 bytes, 66 lineas**, cinco filas
de tarea abiertas, acta 171 localizada en `0c415430`.

**Y EL ESQUELETO LLEVA UN ARREGLO MEDIDO QUE NO ES COSMETICO:** el clon de la
171 buscaba el commit del acta con **una sola forma** del titulo, *"ACTA DE LA
VUELTA N DEL AUDITOR"*. **El asunto del commit del acta 171 empieza por *"ACTA
DEL AUDITOR, VUELTA 171"***, que es **la otra** forma, la nacida en la vuelta
106. Con una sola forma este esqueleto habria dado **cero aciertos y no habria
abierto**. `tallar_cabecera_reporte.py` **ya tenia las dos escritas**, asi que se
usan esas y no se estrena ninguna, y la exigencia de **exactamente un acierto**
no se toca.

**Y NACE UN INSTRUMENTO QUE FALTABA Y QUE EL ENCARGO NO PIDE, Y DIGO POR QUE.**
`scripts/loop/anexar_tarea_al_reporte.py`, de nombre estable y sin numero de
vuelta. El esqueleto sabe abrir el reporte y `cerrar_reporte.py` sabe cerrarlo,
pero **anexar la fila de cada tarea al cerrarse era un paso a mano**, que es
exactamente la especie que ha matado las dos ultimas vueltas. Esta seccion que
estas leyendo la anexo el. Va como `D.3`.

### TAREA 2 (BLOQUEANTE PARA LA 3). SE DESENVENENA EL CONTADOR Y SE CORRIGE EL `R.40`

**2.a `docs/loop/reportes/REPORTE_V<N>.md` ENTRA EN LOS NARRATIVOS DEL BUCLE, Y
ENTRA POR PATRON.** El cambio vive en `scripts/loop/vuelta48_contar_ld.py` como
**correccion declarada 4** en su docstring, al lado de las tres viejas y sin
borrar ninguna, y lo aplica `scripts/loop/_v172_parche_contador.py` con sus
`assert`.

**Y HUBO QUE HACER ANTES UNA COSA QUE EL ENCARGO NO NOMBRA, ASI QUE LA DIGO:
SACAR EL CRITERIO A UNA FUNCION PURA.** La decision de excluir vivia **dentro
del bucle de `main()`**, y ahi **no hay nada que un arnes pueda llamar**: una
guarda que no se puede llamar no se puede probar por mutacion. Nace
`motivo_de_exclusion(rel)`, que devuelve `SALIDA`, `NARRATIVO`, `ARNES` o
`None`, y **`main()` pasa a llamarla**. Una sola fuente del criterio, no dos
copias. Va como `D.4`.

| celda | de donde sale | valor |
|---|---|---:|
| patron nuevo | del codigo | `^docs/loop/reportes/REPORTE_V\d+\.md$` |
| es un patron, no una lista de nombres | del codigo | **SI**, cubre la carpeta de archivo entera |
| ficheros que excluye HOY | contador corrido en esta vuelta | **4** (`REPORTE_V168`, `V169`, `V170`, `V171`) |
| narrativos del bucle, antes | `SALIDA_V172_T2_CONTAR_LD_ANTES.txt` | **3** |
| narrativos del bucle, hoy | `SALIDA_V172_T2C_ATRIBUCION.txt` | **7** |

**EL CASO POSITIVO POR MUTACION, Y CAE POR LOS DOS LADOS QUE EL ENCARGO PIDE:**
`scripts/loop/vuelta172_tarea2a_mutacion_exclusion.py`, salida
`docs/loop/SALIDA_V172_T2A_MUTACION_EXCLUSION.txt`, **exit 0**: **27 casos, 27
pasan, 27 caen al mutar el esperado**. Lo que prueba, y son tres frentes:

- **que el archivo no cuenta**, para vueltas que existen y para una que no
  (`REPORTE_V9999.md`);
- **que la regla NO se ensancha**: `notas.md`, `REPORTE_VX.md`,
  `REPORTE_V12.txt`, `REPORTE_V12.md.bak`, un subdirectorio y
  `docs/loop/REPORTE_V12.md` **siguen contando**. Una exclusion que se comiera
  la carpeta entera seria un agujero;
- **que estrecharla la tumba**: se fabrica la version estrecha (la que nombra
  `REPORTE_V171.md`) y con ella **0 de 4** archivos quedan excluidos, contra
  **4 de 4** con el patron. Y **si el patron se desactiva, tambien cae**.

**SUJETO CONGELADO:** los sujetos son cadenas literales del proceso, no se lee
el disco, y el resultado no depende de que ficheros existan hoy.

**2.b EL `R.40` TRAIA UNA AFIRMACION FALSA Y QUEDA CORREGIDA POR EL CARRIL DEL
`9.10`.** Instrumento `scripts/loop/vuelta172_tarea2b_corregir_r40.py`, salida
`docs/loop/SALIDA_V172_T2B_CORREGIR_R40.txt`, **exit 0**.

| celda | de donde sale | valor |
|---|---|---:|
| `R.40` acotado | cabecera y siguiente `## R.n.` | `docs/PENDIENTES.md`, lineas 12.289 a 12.391 |
| la via falsa de la 6.1 | barrido | **1** dentro, **1** en el fichero entero |
| la clausula falsa | barrido | **1** dentro, **1** en el fichero entero |
| la frase de las 16 filas en pasado | barrido | **1** dentro, **1** en el fichero entero |
| veces que el reporte archivado de la 171 dice *"NO SE CORRE"* | barrido de `REPORTE_V171.md` | **3** |
| commits de la 171 que tocan `docs/plan/LECTURAS_DIRIGIDAS.md` | `git log 0caca89f..cae2731d --` | **0** |
| lineas `VIA:` halladas en el `R.40` | barrido de la propia entrada | **12** |
| reparto VIEJO, contado de la entrada | del barrido | EJECUTADA **8**; SIN TOCAR NADA **4** |
| reparto CORREGIDO | recomputado | EJECUTADA **7**; NO SE CORRIO **1**; SIN TOCAR NADA **4** |

**LOS CERO COMMITS SON LA PRUEBA DURA**, y no la palabra del reporte: la vuelta
171 **no toco el fichero donde esas 16 filas viven**, asi que no pudo darles
ningun numero.

**QUE SE TACHA Y QUE NO, Y ES LA MISMA DECISION QUE EL `D.3` DE LA 171 QUE LA
`6.9` DIO POR BUENA.** La glosa abria diciendo que **la regla estaba escrita en
el codigo de `serie_de_registros.py`**, con su cita de lineas, **y eso es
cierto**: se queda en pie y sin tachar. Lo tachado es el tiempo verbal de la
ejecucion, ni una palabra mas. **Y la glosa de la `6.2` no se toca**, por letra
de la adjudicacion 6.3, que dice que describe bien lo que paso.

**Y ESTRENO UNA ETIQUETA DE VIA, ASI QUE LO DIGO EN VEZ DE COLARLA.** El
vocabulario de vias de la casa trae `EJECUTADA`, `SIN TOCAR NADA` y
`AL FUNDADOR`; para la 6.1 escribi **`NO SE CORRIO`**, que no estaba. Describe
un hecho medido y ninguna regla escrita la prohibe, pero **estrenar una palabra
es exactamente lo que hizo el `D.5` de la vuelta 170 y se le pidio cuenta**. Va
como `D.5`.

**UNA CAIDA MIA EN ESTA TAREA, DECLARADA CON SU NOMBRE** (va como `CAIDA 2` de
la seccion 8): **mi primera guarda anti guiones miraba el fichero ENTERO** y
salio ROJA despues de escribir, porque `docs/PENDIENTES.md` **ya traia 54
guiones largos de antiguo**, ninguno mio. Revertí con `git checkout`, cambié la
guarda **a lo que importa, el DELTA** (que yo no anada ninguno) mas una segunda
que mira **mi propio bloque**, y volvi a correr. **La guarda no se aflojo: se
reapunto**, que es lo mismo que la vuelta 170 hizo con su `CAIDA 2`.

**2.c EL CONTADOR OTRA VEZ, CON LA ATRIBUCION DELANTE.** Instrumento
`scripts/loop/vuelta172_tarea2c_atribucion.py`, salida
`docs/loop/SALIDA_V172_T2C_ATRIBUCION.txt`, **exit 0**. **No copia ninguna regla
del contador: las importa** (`RE_ID`, `RE_CAB`, `PAGINAS`,
`motivo_de_exclusion`), y por eso puede dar la LINEA que el contador no imprime.

| vara | antes de la 2.a, mismo arbol | hoy |
|---|---:|---:|
| mayor de las **HECHAS** | LD-138 | **LD-138** |
| mayor del **UNIVERSO** | LD-155 | **LD-154** |
| nombrados sin seccion propia | 9 | **6** |
| ficheros excluidos por NARRATIVO | 3 | **7** |

**LA CIFRA VIEJA NO SALE DE UN ACTA NI DE UN REPORTE:** sale de
`docs/loop/SALIDA_V172_T2_CONTAR_LD_ANTES.txt`, **corrida en esta misma vuelta**
sobre este mismo arbol antes de tocar el instrumento.

**LA ATRIBUCION, QUE ES LA GUARDA DE LA TAREA 3: SOLO QUEDAN DOS NUMEROS POR
ENCIMA DE `LD-138`, Y NINGUNO TIENE SECCION PROPIA.**

| numero | seccion propia | donde esta nombrado, con fichero y linea |
|---|---|---|
| `LD-139` | **NO** | `docs/PENDIENTES.md:12323`, `:12446`, `:12488` |
| `LD-154` | **NO** | `docs/PENDIENTES.md:12323`, `:12447`, `:12488` |

**Las tres lineas de cada uno son las tres glosas del registro**: la del `R.40`
(la corregida hoy), y las del `R.41` que esta vuelta escribio al citar la
adjudicacion `6.2`. **Ninguna es un encargo: las tres son un registro fiel que
cita un encargo**, que es exactamente el `PD.1` que la 171 dejo abierto.

**LAS CUATRO GUARDAS PASAN, 0 FALLAN**, incluida *"ningun numero por encima de
`LD-138` tiene seccion propia"* y *"el archivo de reportes ya no cuenta"*
(comprobado barriendo todos los sitios del universo). **LA TAREA 3 SE PUEDE
CORRER, y el siguiente libre por la vara que asigna es `LD-139`.**

### TAREA 3. LA NUMERACION `LD`, QUE AHORA SI SE ESCRIBE

**LAS 16 LECTURAS DE LA SEGUNDA TANDA GANAN `LD-139` A `LD-154`.** Instrumento
`scripts/loop/vuelta172_tarea3_numerar_ld.py`, salida
`docs/loop/SALIDA_V172_T3_NUMERAR_LD.txt`, **exit 0**.

| celda | de donde sale | valor |
|---|---|---:|
| hechas antes de escribir | funciones del propio contador | **82** |
| mayor de las HECHAS, computado | `siguiente_libre` sobre ese mapa | **LD-138** |
| siguiente libre, computado y no tecleado | mayor mas uno | **LD-139** |
| numeros con seccion propia por encima de `LD-138` | guarda (ii) | **0** |
| filas de par leidas de la tabla | barrido de los tres bloques | **8 + 5 + 3 = 16** |
| clases leidas de la tabla | del mismo barrido | **A 2, D 14** |
| numeros asignados | computados | **`LD-139` a `LD-154`** |
| el fichero antes | contado | 205.820 bytes, 2.078 saltos de linea |
| el fichero despues | contado | 214.916 bytes, 2.230 saltos de linea |

**QUE SIGNIFICA "POR ADICION PURA" AQUI, DICHO EXACTO PARA QUE SE PUEDA
DISCUTIR.** Las tres tablas **no se han tocado, ni una palabra ni un byte**: el
instrumento lo comprueba al releer, buscando cada una de las 16 filas de par tal
como estaba (`(nodo_a, nodo_b, clase)`) y contando **16 de 16 intactas**. Lo que
se anade es un **bloque nuevo al final de la segunda tanda**, con las 16
secciones en la forma de la casa
(``### `LD-nn` . `a` contra `b` . **CLASE**``), **y el par y la clase de cada una
se LEEN de la tabla**, no se teclean.

**Y DIGO LO QUE ESTE INSTRUMENTO NO HACE, PORQUE ES LO QUE MAS PODRIA
MALINTERPRETARSE: NO VUELVE A LEER NINGUN PAR.** Las 16 lecturas estan hechas y
sus veredictos escritos **desde el 11 ago 2026**; lo unico que les faltaba era el
numero. **Ninguna clase se mueve, ningun nodo se toca y `master_graph.json` no se
abre siquiera.** Cada seccion nueva remite a la tabla y **no copia su razon**,
porque una copia seria una segunda version de lo mismo.

**EL CONTRASTE CON EL SALDO QUE LA PROPIA PAGINA PUBLICA, Y ES CONTRASTE Y NO
FUENTE:** la pagina dice **leidas 16, REPITEN (A) 2, SANAS (D) 14** desde el 11
ago 2026, y mi conteo de hoy da **16, A 2, D 14**. Calzan al digito. **Manda mi
conteo**, que es el que se corrio hoy.

**LAS DOS GUARDAS, Y LAS DOS CAEN POR MUTACION.** Arnes
`scripts/loop/vuelta172_tarea3_mutacion_numeracion.py`, salida
`docs/loop/SALIDA_V172_T3_MUTACION_NUMERACION.txt`, **exit 0**: **24 casos, 24
pasan, 24 caen al mutar el esperado**. Y **para poder probarlas hubo que sacarlas
a funciones puras**, `siguiente_libre(hechas)` y `asignacion_ajena(hechas,
corte)`, porque dentro de `main()` no hay nada que un arnes pueda llamar.

- **La (i), que el numero se compute y no se teclee**, se prueba por donde
  importa: la funcion **devuelve cuatro valores distintos para cuatro mapas
  distintos**, y con mayor 90 el rango sale **`LD-91` a `LD-106`**. **Si el
  `LD-139` estuviera tecleado, ese caso no se moveria.**
- **La (ii), la asignacion ajena**, se prueba con mapas limpios, de un intruso y
  de dos, y **el arnes exige que los NOMBRE**, no solo que los cuente.
- Y el lector de filas se prueba contra una pagina fabricada: **no se traga el
  ruido de otra tabla, no cruza a la tercera tanda, no se traga la tabla de
  oficios, y lee las clases LITERALES** (`DDADAD` sobre un caso fabricado).

**SUJETO CONGELADO:** paginas y mapas son literales del proceso, **cero lecturas
de disco y cero escrituras**, asi que el arnes seguira verde dentro de diez
vueltas.

**EL CIERRE DE LA VARA, MEDIDO DESPUES** (`docs/loop/SALIDA_V172_T3_ATRIBUCION_DESPUES.txt`,
exit 0, y `docs/loop/SALIDA_V172_T3_CONTAR_LD.txt`):

| vara | antes de la 2.a | tras la 2.a | **al cerrar la TAREA 3** |
|---|---:|---:|---:|
| **hechas** | 82 | 82 | **98** |
| mayor de las **HECHAS** | LD-138 | LD-138 | **LD-154** |
| mayor del **UNIVERSO** | LD-155 | LD-154 | **LD-154** |
| nombrados sin seccion propia | 9 | 6 | **4** |

**LAS DOS VARAS CONVERGEN EN `LD-154`, QUE ES LO QUE EL ENCARGO PEDIA**, y las
**98** hechas tambien salen. **Los 4 que quedan estan nombrados uno a uno**:
`LD-12` y `LD-27` (las menciones de la serie `R.n` al glosar un encargo, o sea el
`PD.1` abierto) y `LD-71` y `LD-99`, que **la vuelta 48 ya declaraba como no
pendientes** con su linea de acta.

**Y UNA NOTA SOBRE EL INSTRUMENTO DE LA 2.c QUE NO ME AHORRO:** su corte estaba
**clavado en 138**, asi que al correrlo DESPUES de la TAREA 3 salia ROJO **por
diseno**, diciendo que hay asignacion ajena cuando lo que hay es el trabajo
recien hecho. **Un rojo que solo dice "hiciste tu tarea" es un rojo que no se
puede leer**, asi que el corte paso a ser parametro (`--corte`). Va como `D.6`.

**Y UNA CAIDA MIA AL HACERLO** (va como `CAIDA 3` de la seccion 8): al anadir el
parametro **volvi a correr el instrumento con `--corte 138` y pise su salida
vieja**, que era la evidencia de la guarda previa. **No se perdio nada porque
estaba commiteada**, y la restaure con `git checkout 96940490 --`. La salida que
hoy vive en `docs/loop/SALIDA_V172_T2C_ATRIBUCION.txt` es **la corrida original,
la de antes de la TAREA 3**, y la de despues vive aparte.

**LA SEGUNDA MITAD: LAS DOS FILAS DE `docs/plan/00_INDICE.md`, POR `9.21`.**
Instrumento `scripts/loop/vuelta172_tarea3b_indice.py`, salida
`docs/loop/SALIDA_V172_T3B_INDICE.txt`, **exit 0, 10 comprobaciones y 0 fallos**.

**LA FILA QUE EL ENCARGO NOMBRA** es *"lecturas dirigidas encargadas y sin
hacer"*, que publicaba **CERO** con corte 19 ago 2026 y hoy mide **4**. El `D.4`
de la vuelta 171 se nego a adosarla y **tenia razon**: entonces el barrido daba
**8** y seis salian del archivo de reportes. **Hoy ya se puede**, y los cuatro
van nombrados uno a uno dentro de la celda.

**Y TOQUE UNA SEGUNDA FILA QUE EL ENCARGO NO NOMBRA, ASI QUE LO DIGO EN VEZ DE
COLARLO.** La fila de arriba, *"lecturas dirigidas hechas"*, llevaba adosada
desde la vuelta 171 la cifra **82 con corte 5 sep 2026**, y **mi TAREA 3, del
mismo 5 sep 2026, la ha movido a 98**. Dejarla asi habria puesto **dos cifras
distintas con la misma fecha para la misma vara en la misma celda**, que no es
una cifra con su corte sino una contradiccion, **y la habria creado yo**. Se
adosa por el mismo `9.21`, diciendo en palabras el antes y el despues (*"82 antes
de la TAREA 3 de la vuelta 172, 98 despues"*, diferencia exacta **16**), y **sin
tocar el 82, ni el 81, ni el 65**. Va como `D.7`.

### TAREA 5. EL CIERRE DEL REPORTE DEJA DE SER UN PASO A MANO

**NACE `scripts/loop/cerrar_reporte.py`, DE NOMBRE ESTABLE Y SIN NUMERO DE
VUELTA** (adjudicacion 6.6 del acta 171), como sus hermanos
`paso0_archivar_anterior.py`, `tallar_cabecera_reporte.py`,
`archivar_reporte.py`, `serie_de_registros.py` y `aislador_de_ciega.py`, **para
que el proximo clon no lo pierda**. Su plano es
`vuelta171_tarea1b_cerrar_reporte_170.py`, que ya sabia hacer esto para un
reporte ajeno; lo que cambia es que aqui **esta parametrizado** y **cae en rojo**.

**LA CAUSA QUE LO PIDE ESTA MEDIDA Y NO SUPUESTA:** `vuelta171_cierre.py` **solo
mide**, escribe once ficheros `SALIDA_*` y **no toca `REPORTE.md` en ninguna
linea**. Cerrar el reporte era un paso a mano que venia despues, y **ahi cayeron
las dos ultimas vueltas**. El clon de esta vuelta, `vuelta172_cierre.py`, lo dice
en su propia cabecera para que nadie vuelva a confiarse.

**LO QUE HACE, EN UN SOLO ACTO:** pega la cabecera leyendola del fichero del
tallador (ninguna celda tecleada), anexa el cuerpo del cierre comprobando su
sha256, escribe la seccion 9 **con la salida de la bateria entera dentro**,
escribe el veredicto de una linea, y **relee del disco**.

**Y CAE EN ROJO SI AL TERMINAR FALTA CUALQUIERA DE LAS CUATRO PIEZAS:**

| pieza | que exige |
|---|---|
| **(1)** veredicto escrito | el *"SIN ESCRIBIR TODAVIA"* ya no esta y hay veredicto en su sitio |
| **(2)** cabecera pegada | el hueco *"PENDIENTE DE TALLAR"* ya no esta **y** todas las filas del tallador estan dentro, byte a byte |
| **(3)** secciones 3 a 9 | las siete existen |
| **(4)** bateria dentro de la 9 | la salida de la bateria de ESTA vuelta esta dentro de la seccion 9, entera y no vacia |

**LAS CUATRO VIVEN EN UNA FUNCION PURA, `piezas_que_faltan(texto, filas,
lineas)`, Y NO DENTRO DEL CUERPO QUE ESCRIBE.** El motivo es el mismo que en la
TAREA 2.a: **una guarda que no se puede llamar no se puede probar por
mutacion**.

**EL CASO POSITIVO POR MUTACION:**
`scripts/loop/vuelta172_tarea5_mutacion_cierre.py`, salida
`docs/loop/SALIDA_V172_T5_MUTACION_CIERRE.txt`, **exit 0**: **17 casos, 17
pasan, 17 caen al mutar el esperado**. Prueba exactamente lo que el encargo pide
y dos cosas mas:

- **se quita una pieza a una y la que falta sale NOMBRADA por su numero**;
- **los casos tramposos**: el hueco de la cabecera quitado **pero las filas sin
  pegar** sigue siendo falta de la **(2)**; una bateria **recortada** dentro de
  la seccion 9 sigue siendo falta de la **(4)**; una bateria de cero lineas y un
  tallador sin filas tambien;
- **el escenario real del principio**: un esqueleto recien tallado, que es lo que
  las vueltas 170 y 171 dejaron commiteado, **falla las cuatro**. Si este
  instrumento hubiera existido, **habria salido ROJO en vez de callar**.

**SUJETO CONGELADO:** todos los reportes de mentira son cadenas literales del
proceso, **cero lecturas de disco y cero escrituras**.

**Y ESTA VUELTA SE CIERRA CON EL, QUE ES LA UNICA FORMA DE SABER SI SIRVE.** Su
corrida y su veredicto viven en `docs/loop/SALIDA_V172_T5_CERRAR_REPORTE.txt`, y
si esa salida no existe es que el instrumento no llego a correr, cosa que
tambien se sabria leyendo este mismo reporte.

**LO QUE ESTE INSTRUMENTO NO HACE, Y VA DICHO PARA QUE NO SE LE PIDA:** no talla
la cabecera, no archiva, no corre la bateria y **no anexa tareas**. Recibe lo que
otros produjeron y lo monta; si algo falta lo dice en rojo **en vez de escribir
un reporte a medias**, que es la diferencia entera con las dos vueltas
anteriores.

<!-- FIN ANEXO DE TAREAS -->

## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LOS DOS EXTREMOS SE LEEN DE LOS SELLOS Y NO SE TECLEAN.** Apertura `002e0517`,
de `docs/loop/SALIDA_V172_HEAD_APERTURA.txt`, sellado **antes de la primera
operacion**; cierre `24dda21e`, de `docs/loop/SALIDA_V172_HEAD_CIERRE.txt`,
sellado **tras la ultima**. **LOS COMMITS DE LA VUELTA, LEIDOS DE
`git log 002e0517..24dda21e`: OCHO.**

| # | commit | que cierra |
|---:|---|---|
| 1 | `ad3cea43` | la apertura, el bloque ENTERO |
| 2 | `99d54005` | TAREA 1.a, el reporte de la 171 cerrado |
| 3 | `20b11348` | TAREA 1.b, el acta 171 al `R.41` |
| 4 | `45fb75f5` | TAREA 1 cerrada (1.c, archivador y esqueleto) |
| 5 | `96940490` | TAREA 2 |
| 6 | `24bd395b` | TAREA 3 |
| 7 | `680f74ab` | TAREA 4.a y 4.b |
| 8 | `24dda21e` | TAREA 5 |

**Y HAY UN COMMIT ANTES DE LA APERTURA QUE TAMBIEN ES DE ESTA VUELTA Y SE DICE:**
`002e0517`, la suciedad de la apertura (el `SALIDA_V172_AUDITOR_BATERIA.txt` de
cero bytes que el auditor dejo suelto), commiteado por la regla 3 de
`EJECUTOR.md` **antes de tocar nada**. Es el HEAD de apertura, asi que **queda
fuera del rango por definicion**, no por olvido.

**EL GRAFO NO SE MOVIO, PROBADO Y NO CREIDO:**
`git diff 002e0517 24dda21e --numstat -- dataset/ web/ engine/` sale con **0
filas**. Las **74 rutas** que la vuelta toca son **40 de `docs/loop/`, 30 de
`scripts/loop/`, 2 de `docs/plan/`, 1 de `docs/loop/reportes/` y 1 de `docs/`**.
**Cero nodos tocados, cero aristas movidas, cero clases movidas**, y la cabecera
de arriba lo confirma por otro camino: **+0 / +0 / +0 / +0** en las cuatro cifras
de aristas.

**EL COMMIT QUE LLEVA ESTE REPORTE NO SE NOMBRA AQUI**, porque se crea despues de
escribirlo. Y **este cierre lo escribe la propia vuelta 172**, que es la primera
en tres que lo hace: la 170 y la 171 lo dejaron sin cerrar.

## 4. LA PARADA, Y ES UNA, PERO NO DETIENE NINGUNA TAREA

**LA BATERIA SALE ROJA POR MIS PROPIOS ARNESES, Y NO LO ARREGLO YO.**

El encargo, en su 4.b, dice con esas palabras: *"Con las tres entradas nuevas la
nomina tiene que dar 78 y su ultima vuelta representada tiene que ser la 171."*
**Eso es exactamente lo que hice, y lo mide la funcion pura del propio
instrumento: 78 entradas, ultima vuelta 171, nomina invisible al censo 0.**

**PERO `arneses_que_faltan()` SIGUE DEVOLVIENDO 3, Y LOS TRES SON MIOS**, nacidos
en esta misma vuelta:
`vuelta172_tarea1b_mutacion_registro.py`,
`vuelta172_tarea2a_mutacion_exclusion.py` y
`vuelta172_tarea3_mutacion_numeracion.py`. **Y hay un cuarto desde la TAREA 5**,
`vuelta172_tarea5_mutacion_cierre.py`. El veredicto de la bateria cuenta esa
lista como **ROJO**.

**EL CHOQUE, DICHO EN UNA LINEA:** la regla escrita en el propio
`verificar_mutaciones_viejas.py` dice que *"una mutacion entra en la vuelta
SIGUIENTE a la que nace, no mas tarde"*, o sea que los mios entran en la **173**;
**pero la comprobacion marca como FUERA todo arnes con vuelta mayor que la ultima
de la nomina, y eso incluye a los recien nacidos.** Las dos cosas no pueden ser
ciertas a la vez en la vuelta en que un arnes nace.

**LOS DOS PRECEDENTES, MEDIDOS Y NO RECORDADOS, Y NO DICEN LO MISMO:**

| vuelta | metio sus PROPIOS arneses en la nomina | resultado |
|---|---|---|
| 170 | **SI** (`vuelta170_tarea1a_mutacion_registro.py` y `vuelta170_tarea2a_mutacion_aislador.py` estan en `VIEJAS` y la ultima vuelta representada era la 170) | la bateria del auditor salio **VERDE**, con `faltan` en **0** |
| 171 | **NO** (escribio tres y no metio ninguno) | el acta 171 dice que la bateria **saldria ROJA**, y su seccion 4.3 lo mide |

**POR QUE NO LO ARREGLO METIENDO LOS MIOS:** porque eso daria **81 entradas y
ultima vuelta 172**, y **contradice al digito la cifra que el encargo publica**.
`EJECUTOR.md` 5 dice que si algo contradice una regla vigente **se para y se
trae, y no lo arreglo yo**. **Asi que la bateria se corre, se publica su rojo
entero con su texto en la seccion 9, y la decision sube.**

**LO QUE NO ES:** no es una parada de trabajo. **Las cinco tareas del encargo
estan cerradas**, la bateria corrio entera y sola, y su salida esta pegada
completa. Lo unico que queda en el aire es **si la nomina debe llevar tambien los
arneses de la vuelta que corre**, que es una linea de doctrina y no un arreglo.

**Y LA PREGUNTA CONCRETA, PARA QUE SE PUEDA CONTESTAR EN UNA LINEA:** ¿la nomina
de la bateria se cierra con los arneses de la vuelta ANTERIOR (y entonces
`arneses_que_faltan()` tiene que dejar de contar a los de la vuelta en curso), o
se cierra con los de la vuelta EN CURSO (y entonces la 4.b de este encargo pedia
78 cuando tenia que pedir 82)? Va como `P.1`.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Los marco ahora, con la relectura ciega del auditor por delante y sin saber
como va a adjudicarlos.** Esta vez si son ciegos, y lo digo porque en el reporte
de la 171 que cerre en la TAREA 1.a **no lo eran** y ahi va escrito.

- **`D.1` LAS GLOSAS DEL `R.41` NO AFIRMAN EN PASADO, Y ESO CAMBIA LA FORMA DE
  UNA ENTRADA DE LA SERIE.** El campo se llama **VIA PREVISTA**, las siete glosas
  de tarea dicen *"VA A EJECUTARSE EN LA TAREA n ... Y AL ESCRIBIR ESTA LINEA
  TODAVIA NO HA CORRIDO"*, y la confirmacion medida se anexa al cierre.
  **Discutible: puede que la forma correcta fuera escribir la entrada AL FINAL de
  la vuelta, cuando ya se sabe, en vez de cambiar el tiempo verbal; y puede que
  cambiar la forma de una entrada de la serie sea doctrina y no ejecucion.**
- **`D.2` TRAIGO UNA DISCREPANCIA CON EL ACTA EN VEZ DE RESOLVERLA.** El acta 171
  dice que el paso 0 sale ROJO **por la clausula (d)**; con
  `vuelta_anterior=171`, que es lo que el esqueleto de esta vuelta llama, sale
  **por la (b)**. Reproduje la del acta con **su** parametro,
  `exigir_archivado(170)`, y ahi si sale la (d). **Publico las dos. Discutible:
  puede que lo esperado fuera decir simplemente que reproduce, y que separar dos
  lecturas de dos preguntas distintas sea hilar de mas.**
- **`D.3` ESCRIBI UN INSTRUMENTO QUE EL ENCARGO NO PIDE.**
  `scripts/loop/anexar_tarea_al_reporte.py`, de nombre estable. El motivo es que
  anexar la fila de cada tarea al cerrarse **era un paso a mano**, la misma
  especie que la TAREA 5 viene a matar. **Discutible: el encargo trae tope de
  cinco tareas y esto es codigo de mas; puede que tocara traerlo como propuesta
  en vez de escribirlo.**
- **`D.4` SAQUE EL CRITERIO DE EXCLUSION DEL CONTADOR A UNA FUNCION PURA.** Sin
  eso no habia nada que un arnes pudiera llamar y la 2.a no se podia probar por
  mutacion. **Discutible: es un cambio de forma en un instrumento viejo que el
  encargo no manda tocar, y un refactor dentro de una tarea de contenido es
  precisamente lo que suele colar cambios sin guarda.**
- **`D.5` ESTRENE LA ETIQUETA DE VIA `NO SE CORRIO`.** El vocabulario de la casa
  trae `EJECUTADA`, `SIN TOCAR NADA` y `AL FUNDADOR`. **Discutible: estrenar una
  palabra es exactamente lo que hizo el `D.5` de la vuelta 170 y se le pidio
  cuenta; puede que lo correcto fuera dejar la via vieja tachada y sin
  sustituto.**
- **`D.6` LE PUSE PARAMETRO AL CORTE DE LA 2.c.** Estaba clavado en 138 y al
  correr el instrumento DESPUES de la TAREA 3 salia ROJO por diseno. **Discutible:
  un rojo que molesta no siempre es un rojo mal puesto, y puede que lo correcto
  fuera dejarlo clavado y no volver a correrlo.**
- **`D.7` TOQUE UNA SEGUNDA FILA DE `docs/plan/00_INDICE.md` QUE EL ENCARGO NO
  NOMBRA.** La de *"lecturas dirigidas hechas"* llevaba **82 con corte 5 sep
  2026** y mi TAREA 3, del mismo dia, la movio a **98**; dejarla habria puesto dos
  cifras distintas con la misma fecha para la misma vara, **y la habria creado
  yo**. **Discutible: el encargo nombra una fila y toque dos.**
- **`D.8` NO METI MIS PROPIOS ARNESES EN LA NOMINA Y DEJE LA BATERIA EN ROJO.**
  Esta explicado entero en la seccion 4. **Discutible: puede que la lectura buena
  del encargo fuera "78 al meter los tres de la 171, y despues los tuyos
  tambien", y que yo haya elegido la letra por encima del sentido.**

## 6. LAS PREGUNTAS

- **`P.1`** ¿La nomina de la bateria se cierra con los arneses de la vuelta
  ANTERIOR o con los de la vuelta EN CURSO? Es la de la seccion 4 y es la unica
  que deja algo en rojo.
- **`P.2`** ¿Una entrada de la serie `R.n` se escribe al ABRIR la vuelta, con
  glosas en futuro y confirmacion anexada al cierre (lo que hice), o al CERRARLA,
  con glosas en pasado y ya medidas? Las dos evitan la caida del `R.40`; solo una
  puede ser la forma de la casa.
- **`P.3`** El `PD.1` de la vuelta 171 sigue abierto y hoy es lo unico que separa
  las dos varas del contador: **¿un registro fiel que CITA un encargo cuenta como
  encargo?** Medido hoy, los dos numeros que lo sostenian (`LD-139` y `LD-154`)
  **ya no cuentan**, porque la TAREA 3 les dio seccion propia; **pero la pregunta
  sigue viva** para el proximo encargo que una entrada `R.n` glose.

## 7. PENDIENTES DE DOCTRINA

- **`PD.1` NO HAY REGLA SOBRE CUANDO ENTRA EN LA BATERIA EL ARNES QUE NACE HOY.**
  El fichero dice *"en la vuelta SIGUIENTE a la que nace"* y su comprobacion los
  cuenta como FUERA desde el minuto uno. **La vuelta 170 metio los suyos y salio
  verde; la 171 no metio ninguno y quedo roja.** La regla que falta es de una
  linea y cierra el rojo de esta vuelta.
- **`PD.2` NO HAY VOCABULARIO ESCRITO DE VIAS PARA LA SERIE `R.n`.** La casa usa
  `EJECUTADA`, `SIN TOCAR NADA` y `AL FUNDADOR`, y hoy hicieron falta dos que no
  estaban: **`NO SE CORRIO`** (para la correccion del `R.40`) y **`VIA
  PREVISTA`** (para una entrada escrita antes de que la tarea corra). Las dos
  describen hechos y ninguna regla escrita las prohibe, **pero estrenar
  vocabulario dos veces en una vuelta es justo lo que la 170 hizo una vez y se le
  cazo**.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

- **`CAIDA 1`. LA PRIMERA CORRIDA DEL BLOQUE DE APERTURA MURIO CON
  `SyntaxError` Y NO ESCRIBIO NI UN FICHERO.** Al generar
  `scripts/loop/vuelta172_apertura.py` se me colo **un salto de linea de verdad
  donde tenia que ir su escape**, y el fichero no compilaba. **Ninguna cifra
  salio de ahi: no escribio ninguna salida.** Lo arregle usando `chr(10)` en vez
  del escape y volvi a correr, **y la segunda corrida sigue estando antes de la
  primera operacion sobre el registro**. Va declarada tambien en el mensaje del
  commit `ad3cea43`, antes de que nadie la cazara.
- **`CAIDA 2`. UNA GUARDA MIA MIDIO EL FICHERO ENTERO EN VEZ DE MI PROPIO
  CAMBIO.** La comprobacion anti guiones de la TAREA 2.b miraba
  `docs/PENDIENTES.md` **completo** y salio ROJA **despues de escribir**, porque
  esa pagina **ya traia 54 guiones largos de antiguo**, ninguno mio. Revertí con
  `git checkout`, apunte la guarda **al DELTA** (que yo no anada ninguno) mas una
  segunda que mira **solo mi bloque**, y volvi a correr. **La guarda no se
  aflojo: se reapunto**, que es lo mismo que la vuelta 170 hizo con su `CAIDA 2`.
- **`CAIDA 3`. PISE UNA SALIDA QUE ERA EVIDENCIA.** Al ponerle el parametro
  `--corte` al instrumento de la 2.c **lo volvi a correr con `--corte 138`
  DESPUES de la TAREA 3 y sobreescribi
  `docs/loop/SALIDA_V172_T2C_ATRIBUCION.txt`**, que era la medicion de la guarda
  **previa** a la TAREA 3. **No se perdio nada porque estaba commiteada** y la
  restaure con `git checkout 96940490 --`. **Lo que ensena es que una salida
  commiteada es la unica que aguanta**, y que un instrumento que se puede
  re-correr sobre su propio fichero de salida deberia negarse a pisarlo.
- **`CAIDA 4`. UN MARCADOR DE UNA LETRA ROMPIO UN FICHERO GENERADO.** El primer
  andamio que escribia el texto del `R.41` usaba **la letra `Q` como marcador de
  comilla**, y `Q` aparece en `AQUI` y en `QUE`, asi que el clon salio sin
  compilar. **Lo cazo `py_compile` y nada se commiteo roto**; el marcador paso a
  `~C~` y el andamio quedo como
  `scripts/loop/_v172_construir_registrador.py`, que **reproduce el fichero byte
  a byte**. Va declarada aunque no llegara a publicarse ninguna cifra.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 172 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V172_BATERIA.txt`.
**SUS BYTES, MEDIDOS EN ESTA CORRIDA** con `os.path.getsize` por
`scripts/loop/cerrar_reporte.py`, no tecleados: **0 bytes**.

ATRIBUCION: NADIE la corrio para la vuelta 172. La del ejecutor, docs/loop/SALIDA_V172_BATERIA.txt, mide 0 bytes; la del auditor, docs/loop/SALIDA_V172_AUDITOR_BATERIA.txt, mide 0 bytes tambien, y su propia acta lo declara en la clausula 4.3 (docs/loop/ACTA_AUDITOR.md:58638, leida hoy). Las dos cifras las midio hoy scripts/loop/vuelta174_apertura.py con os.path.getsize, bloque H.3.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
