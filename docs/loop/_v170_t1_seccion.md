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
