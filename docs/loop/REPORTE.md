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

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

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
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 172`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Son todas del lado CIERRE, que al abrir todavia no existe.
Este hueco se rellena con la tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | BLOQUEANTE Y VA PRIMERA. EL CIERRE QUE FALTA Y LOS REGISTROS (1.a el reporte de la 171 CERRADO con la cabecera tallada pegada, sus cuatro discutibles y su caida sin suavizar, y la seccion 9 diciendo que la bateria NO corrio; 1.b el acta 171 y sus adjudicaciones 6.1 a 6.12 al `R.41` con su arnes de mutacion del registro; 1.c el archivador para la 171 y este esqueleto) | **CERRADA** | `SALIDA_V172_T1A_CERRAR_REPORTE_171.txt`, `_T1A_COMPARAR_CABECERA_171`, `_T1A_RELECTURA_DESDE_GIT`, `_T1B_REGISTRO_ACTA_171`, `_T1B_MUTACION_REGISTRO`, `_T1B_SERIE`, `_T1C_GUARDA_QUE_MORDIO`, `_T1C_ESQUELETO` |
| **TAREA 2** | BLOQUEANTE PARA LA 3. SE DESENVENENA EL CONTADOR Y SE CORRIGE EL `R.40` (adjudicaciones 6.1 y 6.3): 2.a `docs/loop/reportes/REPORTE_V<N>.md` entra en los narrativos del bucle POR PATRON, con su caso positivo por mutacion; 2.b la afirmacion falsa del `R.40` corregida por el carril del `9.10` con el reparto recomputado; 2.c el contador otra vez, con la atribucion fichero a fichero y linea a linea | **CERRADA** | `SALIDA_V172_T2_CONTAR_LD_ANTES.txt`, `_T2A_MUTACION_EXCLUSION`, `_T2A_CONTAR_LD_DESPUES`, `_T2B_CORREGIR_R40`, `_T2C_ATRIBUCION` |
| **TAREA 3** | LA NUMERACION `LD`, QUE AHORA SI SE ESCRIBE (adjudicacion 6.2): las 16 filas de la segunda tanda de `docs/plan/LECTURAS_DIRIGIDAS.md` ganan `LD-139` a `LD-154` POR ADICION PURA, con los numeros COMPUTADOS y con dos guardas que tienen que caer por mutacion; y despues la fila de `docs/plan/00_INDICE.md` recibe su cifra de hoy por `9.21` (adjudicacion 6.10) | **CERRADA** | `SALIDA_V172_T3_NUMERAR_LD.txt`, `_T3_MUTACION_NUMERACION`, `_T3_ATRIBUCION_DESPUES`, `_T3_CONTAR_LD`, `_T3B_INDICE` |
| **TAREA 4** | LOS TRES ARNESES Y LA BATERIA (adjudicaciones 6.4 y 6.5), Y EL ORDEN ES OBLIGATORIO: 4.a el caso `F` de `vuelta171_tarea5a_mutacion_enchufe.py` refundado sobre SUJETO CONGELADO; 4.b los tres arneses de la 171 dentro de la nomina de `verificar_mutaciones_viejas.py`; 4.c la bateria corrida ENTERA Y SOLA al cierre, con su salida en la seccion 9 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | EL CIERRE DEL REPORTE DEJA DE SER UN PASO A MANO (adjudicacion 6.6): nace `scripts/loop/cerrar_reporte.py`, de nombre estable y sin numero de vuelta, que pega la cabecera, anexa el cuerpo, escribe el veredicto y CAE EN ROJO si al terminar falta cualquiera de las cuatro piezas. Con su caso positivo por mutacion, y esta vuelta se cierra con el | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

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

<!-- FIN ANEXO DE TAREAS -->
