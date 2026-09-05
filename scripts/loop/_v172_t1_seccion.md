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
