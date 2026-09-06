### TAREA 1. LOS REGISTROS. CERRADA EN VERDE, Y LA MARCA `EN CONTRA` EXISTE Y SALE EN LA CUENTA

**EL INSTRUMENTO:** `scripts/loop/vuelta190_tarea1a_registrar_acta190.py`
(**78499 bytes en disco y 78499 normalizado a LF**, **1520 lineas**, `sha256` LF
`52b8b0ee20f8780c`). **LA MAQUINA NO SE CLONA, SE IMPORTA** (`6.6` del acta 172):
de la cadena de registradores se importan `titulo_de_la_negrita`,
`claves_de_adjudicacion`, `claves_entrecomilladas`, `cuenta_por_patron`,
`actas_sin_entrada`, `PALABRA_CON_CERO`, `seccion_que_contiene`, los cinco
patrones de caida, `caidas_por_seccion`, y **la idempotencia entera**
(`marcas_del_acta` y `entradas_que_registran` del registrador de la 189).

**TODAS LAS CIFRAS DE ABAJO SE CUENTAN DEL FICHERO DE SALIDA QUE SE NOMBRA AL
LADO** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO). Las cuatro salidas de
esta tarea, medidas en disco por las dos convenciones:

| fichero de salida | bytes en disco | bytes en LF | lineas | `sha256` LF |
|---|---:|---:|---:|---|
| `docs/loop/SALIDA_V190_T1A_MUTACION_REGISTRADOR.txt` | 6373 | 6373 | 82 | `21ecbc87103369bd` |
| `docs/loop/SALIDA_V190_T1A_SIMULACION.txt` | 28285 | 28285 | 345 | `a8befe8675e1a49f` |
| `docs/loop/SALIDA_V190_T1A_REGISTRO_R52.txt` | 8854 | 8854 | 151 | `c3d60058ec7fe662` |
| `docs/loop/SALIDA_V190_T1A_RECORRIDO_SIN_ESCRIBIR.txt` | 9230 | 9230 | 151 | `0a2717e2cb782c0c` |

**LA ENTRADA:** `R.52` en `docs/PENDIENTES.md`, **18764 bytes**, **198 lineas por
`count(NL)` y 199 por `len(split(NL))`** (las dos convenciones publicadas, que es
justo el hallazgo `5.1` del acta) y **0 guiones largos o medios**. El numero **no
esta tecleado**: lo devuelve `scripts/loop/serie_de_registros.py`, que recompone
la serie de sus **dos** sedes y da **43 entradas, 0 colisiones, 0 huecos,
siguiente libre R.52**. Despues de escribir, remedido: **44 entradas, 0
colisiones, 0 huecos, siguiente libre R.53**. La sede pasa de **961248 bytes** a
**980013 bytes**, o sea **18765 bytes** mas, que son los **18764** de la entrada
mas su salto de linea.

#### LO QUE ESTE REGISTRADOR ESTRENA, Y POR QUE NO SE PODIA HEREDAR

**1. LA MARCA `EN CONTRA`, QUE ES LA QUE EL ENCARGO AVISA QUE SE CUENTA MAL.** El
`estado_de_la_adjudicacion()` del registrador de la 189 conoce **cinco** marcas y
ninguna es `EN CONTRA`; corrido sobre el titulo de la `4.6` del acta 190 daria
`SIN DECIR` y este instrumento haria PARADA. Y su regla de cuenta era peor de
heredar: **PARABA si algun discutible no llevaba `A FAVOR`**, porque los seis del
acta 189 lo llevaban. Aqui `EN CONTRA` **se busca literal y ANTES que `A FAVOR`**,
y las dos cifras se publican por separado. Medido sobre el acta:

| medicion | cifra |
|---|---:|
| adjudicaciones `4.n`, patron SIN comillas inversas | 10 |
| adjudicaciones `4.n`, patron CON comillas inversas (el del acta 188) | 0 |
| de esas, discutibles (su titulo nombra un `D.n`) | 6 |
| de esas, preguntas (su titulo nombra un `P.n`) | 3 |
| de esas, ni una cosa ni la otra | 1 |
| **discutibles A FAVOR** | **5** |
| **discutibles EN CONTRA** | **1** |

**EL QUE VA EN CONTRA ES LA `4.6`, EL `D.5`**, y su titulo literal, leido hoy de
`docs/loop/ACTA_AUDITOR.md:67231`, es: *"4.6 `D.5`, dejar
`guarda_del_sujeto_congelado()` FUERA DEL VEREDICTO. EN CONTRA, Y ES EL UNICO QUE
TUMBO."*

**2. LA SECCION 6 NO DICE DE QUIEN SON LAS CAIDAS, Y LAS ESCRIBE EN LINEA.** Su
cabecera literal, leida del fichero, es **`## 6. LAS CAIDAS`**: a secas. Y sus
tres caidas van **dentro de un parrafo, entre parentesis**. Las dos mediciones que
prueban que la maquina heredada no alcanza, en vez de afirmarlo:

| patron o maquina | cifra sobre el acta 190 |
|---|---:|
| patron `C.n` de la 187 (coma o punto pegados) | 0 |
| patron `C.n` de la 188 (admite tambien un espacio) | 0 |
| patron `A.n` de cabecera de tercer nivel (acta 185) | 0 |
| patron `R.n` de caida de reporte | 0 |
| patron `E.n` de las actas 182 y 184 | 0 |
| `caidas_por_seccion()` de la 189 sobre la seccion 6 | ejecutor 0, auditor 0, huerfanas 0 |
| **`caidas_en_linea()` de esta vuelta** | **ejecutor 3, auditor 0, huerfanas 0** |

La atribucion la hace **la negrita que abre cada parrafo** (`DEL EJECUTOR: ...`
frente a `MIAS: ...`), y las tres del ejecutor son `C.1`, `C.2` y `C.3`, las tres
bajo la negrita `DEL EJECUTOR: CERO QUE ACUMULEN.` en el parrafo de la linea
**67323**. **La PARADA se conserva entera:** el arnes fabrica un acta con una
negrita muda y la maquina saca **3 huerfanas**, que es PARADA.

**3. UN CERO DE RACHA NO ES UN CERO DE CUENTA, Y ESTA ES LA TRAMPA QUE MAS CERCA
ESTUVO DE BORRAR TRES CIFRAS.** El acta 189 traia `CERO SON DEL EJECUTOR`, que es
un cero de **CUENTA**, y por eso la `4.1` adjudico que NEUTRALIZA la atribucion.
El acta 190 trae `DEL EJECUTOR: CERO QUE ACUMULEN`, que es un cero de **RACHA**, y
**en ese mismo parrafo declara TRES caidas**. Corrido a proposito con la marca de
racha tratada como marca de cuenta, **el ejecutor sale con 0 caidas en vez de 3**:

| como se trate el cero | caidas del ejecutor | caidas del auditor |
|---|---:|---:|
| con la separacion puesta (lo que hace este instrumento) | **3** | **0** |
| tratando el cero de RACHA como cero de CUENTA | 0 | 0 |

**La marca de cuenta de la `4.1` NO se toca:** se importa literal del registrador
de la 189 y su conducta se vuelve a probar en el arnes, sobre una negrita
fabricada que dice `CERO SON DEL EJECUTOR` y que sigue sin atribuir ninguna.

**4. LOS HALLAZGOS DE LA SECCION 5 SON CUATRO Y SOLO DOS CUENTAN FUERA DEL
MARCADO, Y CUAL NO SE TECLEA.** La seccion trae `5.1`, `5.2`, `5.3` y `5.4`. Quien
decide cuales cuentan es **la fila `discrepancias y hallazgos FUERA del marcado`
de la tabla de credito del propio acta** (`docs/loop/ACTA_AUDITOR.md:67343`),
cuyo parentesis se parte por `;`, se normaliza y se busca dentro del titulo
literal de cada `5.n`. Las piezas que salen son *dos convenciones de lineas* y
*ocho actas sin entrada propia*, y casan con la `5.1` y la `5.2`
respectivamente. **La `5.3` y la `5.4` NO salen en ese parentesis y se publican
igual, dichas como lo que son.**

#### LO QUE EL ENCARGO PEDIA, PUNTO POR PUNTO, CON SU CIFRA

| lo que el encargo pide | lo que se midio | fichero |
|---|---|---|
| las DIEZ adjudicaciones `4.1` a `4.10` | 10, ninguna repetida | `SALIDA_V190_T1A_REGISTRO_R52.txt` |
| QUE NO SON DIEZ A FAVOR: 5 A FAVOR y 1 EN CONTRA (`D.5`) | discutibles 6, A FAVOR 5, EN CONTRA 1 | idem |
| la marca de EN CONTRA probada por mutacion con acta fabricada | bloque B del arnes: 5 a favor + 1 en contra fabricados, y las tres mutaciones CAEN | `SALIDA_V190_T1A_MUTACION_REGISTRADOR.txt` |
| las TRES preguntas contestadas (`4.4` `P.1`, `4.8` `P.2`, `4.9` `P.3`) | 3, y cuales sale de que su titulo nombre un `P.n` | `SALIDA_V190_T1A_REGISTRO_R52.txt` |
| los DOS hallazgos de la seccion 5 que no salen de ningun discutible | 4 hallazgos `5.n`, y la tabla nombra 2: `5.1` y `5.2` | idem |
| CERO caidas propias del auditor, escrito como cero y no omitido | 0, con `MIAS: CERO` en la linea 67333 y la fila de la tabla en la 67344 | idem |
| TRES del ejecutor, las tres DE METODO y ninguna de racha | 3 (`C.1`, `C.2`, `C.3`), marca `SON DE METODO` en 1 de los 3 parrafos, fila de la tabla en la 67347 | idem |
| LA VARA CORRIDA POR EL AUDITOR (`5.4`) con sus cifras | 7 cifras leidas del parrafo, ninguna tecleada | idem |
| el registrador SIGUE SIENDO IDEMPOTENTE, re corrido por mi | re corrido: NO ESCRIBE NADA | `SALIDA_V190_T1A_RECORRIDO_SIN_ESCRIBIR.txt` |

**LAS CIFRAS DE LA VARA DE LA `5.4`, LEIDAS DEL PARRAFO CON SU PATRON AL LADO Y NO
COPIADAS DEL ENCARGO** (y si alguna no se pudiera leer, este instrumento hace
PARADA en vez de inventarla): **71 fichas**, **37 que no calzan**, **6 en LISTA
sin ninguna prueba**, **2 CONSUMIDAS por `OP-U-01`**, **4 de TRABAJO REAL**, **3
mesas con producto en disco** y **0 menciones de fichero en la evidencia de
`OP-L-02`**. La salida del auditor donde eso vive,
`docs/loop/_auditor_v190_vara.txt`, mide **17445 bytes en disco y 17164
normalizado a LF** y nombra `OP-L-02` **3 veces**.

**LA IDEMPOTENCIA, PROBADA POR MI Y NO HEREDADA, CON LA SEDE MEDIDA ANTES Y
DESPUES.** Es lo que el encargo pide con esas palabras:

| momento | `docs/PENDIENTES.md` |
|---|---:|
| antes de la primera corrida | **961248 bytes** |
| despues de escribir el `R.52` | **980013 bytes** |
| **despues del RE CORRIDO** | **980013 bytes** |

El re corrido dice **`NO SE ESCRIBE NADA`**, que el acta 190 ya tiene entrada en
**4 lineas**, y **no consume el numero `R.53`**. Y **el nombre del fichero de
salida dice lo que paso**: cuando la idempotencia muerde, la salida se llama
`RECORRIDO_SIN_ESCRIBIR` y no `REGISTRO_R53`, porque una ruta que prometiera un
registro que no existe seria una cifra falsa (`EJECUTOR.md` 1).

**LA DEUDA DE LA SERIE, REMEDIDA AQUI Y NO HEREDADA DEL `R.51`:** **8 actas sin
entrada propia**, las **173 a 180**, entre el `R.42` (que cubre la 172) y el
`R.43` (que cubre la 181). **El acta 190 publica 8 en su `5.2` y CALZA.** No se
rellenan: escribir de memoria los registros de unas actas que nadie ha releido en
esta vuelta es justo lo que `AUDITOR.md` 2 prohibe.

**EL ARNES:** `--mutacion` del propio instrumento, **7 bloques, CIFRA casos que
CAEN 0, CIFRA mutaciones que NO cayeron 0, VEREDICTO VERDE**, contado de
`docs/loop/SALIDA_V190_T1A_MUTACION_REGISTRADOR.txt`. Sus mutaciones **CAEN todas**
y la que mas importa es la del bloque D: **3 caidas con la separacion de ceros y 0
sin ella**.

**GATE 0 AL CERRAR LA TAREA:** `GATE 0: OK`, motor **25/25**, y
`git diff --numstat -- dataset/` en **0 filas**. **Y UNA MEDICION QUE ME LLEVE POR
DELANTE Y QUE DECLARO:** corrido `run_phase1.py --reaplico-curaduria` SOLO, sin el
resto del ciclo, `git diff --numstat -- dataset/` da **1 fila (72 mas y 72
menos)**; corrido el ciclo entero (`run_phase1` + `etiquetas_de_cara --aplicar` +
`sync_assets_web`) vuelve a **0 filas**. **El ciclo de Gate 0 va entero o su cifra
no dice lo que parece**, y eso es exactamente lo que `EJECUTOR.md` manda y lo que
el bloque de cierre de esta casa ya hace.
