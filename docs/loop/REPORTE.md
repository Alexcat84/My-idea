# REPORTE DE LA VUELTA 190 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta190_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que **no lleva
> nada mas**. **La 189 la corrio entera** (sus diez tramos siguen sellados en
> disco y el bloque **H.5** del sello de apertura los remidio uno a uno antes de
> tocar nada), asi que **la siguiente cae en la 194**. El hueco va **con su
> medicion, su atribucion y su corrida, por el carril de `cerrar_reporte.py`**:
> un hueco declarado no es un hueco escondido.
>
> **Y VAN CINCO SUB-TAREAS Y NO DOS.** El tope temporal de la `AUDITOR.md` 6.2
> **se cumplio y caduca**: su disparador de salida pedia **DOS vueltas seguidas
> cerrando su propio reporte** con `cerrar_reporte.py`, y **son TRES**. El bloque
> **B.2** del sello de apertura las localizo **en git y no de memoria**, por el
> asunto de su commit, y midio ademas sus tres ficheros de cierre con
> `CIFRA piezas que faltan: 0` en los tres. **Vuelve el tope de CINCO** de la
> seccion 6 de `EJECUTOR.md`.
>
> **DONDE SE TALLO ESTE ESQUELETO: EN LA APERTURA Y EN SU PROPIO COMMIT.** Desde
> el segundo commit de esta vuelta ya hay reporte parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** ni cribado, ni
> recomputo, ni operaciones del plan que no sean la **busqueda** de la TAREA 5,
> ni las mesas anotadas, ni **podar la nomina** (la opcion `c` que el fundador
> RECHAZO el 5 sep 2026: **la nomina sigue creciendo y nadie la poda sin el
> fundador**). **Y no entran las SEIS que el encargo deja nombradas a proposito
> para que la 191 no las redescubra:** las dos convenciones de `lineas`,
> `acumulan()` contra la tabla, el cotejo de clon declarado que separa, la
> excepcion que publica siempre su lista, la medicion del censo de arneses sin
> fichero, y las ocho actas sin entrada propia en la serie. **Y no se corre la
> bateria.**
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo
> valor. **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al
> salir y **las dos cifras se publican**.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** **Una columna de apertura medida
> al cierre es caida que ACUMULA.**

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta190_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 189: `bbeea713`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 189: LA 188 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA, ADJUDICO LOS SEIS DISCUTIBLES A FAVOR Y CONTESTO LAS TRES PREGUNTAS, DECLARO DOS CAIDAS PROPIAS MIAS Y CERO DEL EJECUTOR, Y CAZO QUE EL LANZADOR DE LA BATERIA YA REPARTE EN DIEZ TRAMOS Y SU --siguiente HABRIA CORRIDO OCHO ARNESES DE 125 DECLARANDOSE CORRIDO.'
- **DESFASE DECLARADO, SEXTA VUELTA:** la linea de arriba nombra el acta
  **189** porque `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que
  ORDENA esta vuelta es la 190**. Es el `D.2` del reporte de la 184, adjudicado a
  favor con reparacion encargada por la `5.2` del acta 185. **Esta vuelta no la
  ejecuta** porque no es ninguna de sus cinco tareas y el encargo nombra una a
  una las seis que quedan fuera. Se declara en vez de colarse.
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V190_HEAD_APERTURA.txt`: `b393347f`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `70d5662c`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **189**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 190`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 190 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus DIEZ adjudicaciones `4.1` a `4.10`, QUE NO SON DIEZ A FAVOR: seis son los discutibles del ejecutor y de esos CINCO van A FAVOR (`D.1`, `D.2`, `D.3`, `D.4`, `D.6`) y UNO EN CONTRA, el `D.5`, la guarda del sujeto congelado fuera del veredicto. La marca de EN CONTRA tiene que EXISTIR y tiene que SALIR EN LA CUENTA, probada por mutacion con un acta fabricada. Mas las TRES preguntas contestadas (`4.4` la `P.1`, `4.8` la `P.2`, `4.9` la `P.3`), los DOS hallazgos de la seccion 5 que no salen de ningun discutible (las dos convenciones de `lineas` en `5.1` y las ocho actas sin entrada propia en `5.2`), CERO caidas propias del auditor ESCRITO COMO CERO Y NO OMITIDO y TRES del ejecutor, las tres DE METODO y ninguna de racha, y LA VARA CORRIDA POR EL AUDITOR (`5.4`) con sus cifras. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido, no escribe nada, y se prueba re corriendolo con la sede medida antes y despues | **CERRADA EN VERDE** | `SALIDA_V190_T1A_MUTACION_REGISTRADOR.txt` (6373 bytes), `SALIDA_V190_T1A_SIMULACION.txt` (28285), `SALIDA_V190_T1A_REGISTRO_R52.txt` (8854), `SALIDA_V190_T1A_RECORRIDO_SIN_ESCRIBIR.txt` (9230) |
| **TAREA 2** | LA GUARDA DEL SUJETO CONGELADO: SEPARA LA DEUDA DEL FALLO, Y VUELVE AL VEREDICTO. Son las adjudicaciones `4.4` y `4.6` del acta 190 y las dos mitades van juntas porque una sin la otra no sirve. (a) la guarda SEPARA EN SU SALIDA las entradas `NO DECIDIBLE` que traen MOTIVO ESCRITO de las que no lo traen, y publica LAS DOS CIFRAS CON SUS NOMBRES; hoy "3 entradas sin congelar" no distingue una deuda de una decision, y esa es la `P.1` que el acta 189 dejo encargada en su `4.7`. Las tres de hoy son `vuelta186_tarea2c_mutacion_cierre_tardio.py`, `vuelta187_tarea4_mutacion_dos_convenciones.py` y `vuelta188_tarea4_mutacion_cobertura_parejas.py`, y cuantas traen motivo escrito SE MIDE. (b) LA GUARDA VUELVE AL VEREDICTO del instrumento de la nomina: el `D.5` de la 189 la saco y el acta 190 lo TUMBA, porque publicar los tres nombres arriba y cerrar en verde deja sin sintoma al que solo mire el veredicto. Con la separacion de (a) puesta, el veredicto ya puede decir ROJO POR DEUDA DECLARADA distinto de ROJO POR FALLO sin dejar de ser rojo. NO SE AFLOJA NINGUNA GUARDA, y el rojo que salga se trae con su nombre. Con simulacion previa sobre copia en memoria y caso positivo por mutacion | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | LA BATERIA: QUE SU EXITCODE SEPARE, Y QUE RESTAURE SOLA LO QUE PISA. Son las adjudicaciones `4.4` y `4.9` del acta 190, y NO SE CORRE LA BATERIA en esta vuelta: se arregla su lanzador y se prueba con sus arneses. (a) EL EXITCODE SEPARA: hoy los diez tramos de la 189 salieron con exitcode 1 y en NUEVE de ellos no cayo ni un arnes, porque la fuente era siempre la guarda de nomina en deuda, y un unico `1` para un arnes caido y para una deuda declarada es degradacion silenciosa (banco 9). Que el lanzador distinga los dos casos en su salida sellada y en su codigo de salida, y que lo diga con su cifra. (b) LA BATERIA RESTAURA SOLA LAS SALIDAS SELLADAS AJENAS QUE PISA, como ya restaura `dataset/`: en la 189 piso TRES y las restauro una persona a mano, en dos vueltas distintas y a dos personas distintas. La restauracion va EN LF, y si el corte nuevo interesa se escribe AL LADO con nombre nuevo y su vuelta, nunca encima. Con simulacion previa y caso positivo por mutacion que CAIGA si una salida sellada ajena se queda pisada | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LA RELECTURA AL DOBLE DEL TRAMO DEL PUESTO 2422. ES UNA DEUDA DEL ACTA 189 Y NO SE SALTA DOS VUELTAS SEGUIDAS: la 189 la aplazo con razon por ser vuelta de bateria, y esa razon ya no vale. El acta 189 encontro la discrepancia del puesto `2422` FUERA de sus dudosos marcados, y `AUDITOR.md` 1.2 dice que eso baja el credito de la tanda y obliga a releer ese tramo AL DOBLE. Corre la relectura con `scripts/loop/aislador_de_ciega.py`, sobre los vecinos deterministas del tramo del `2422`, con el criterio escrito, la ciega y el destape en ficheros separados, y las clases escritas ANTES de abrir el destape. Publica cuantos coinciden y cuantos discrepan. NO SE TOCA NINGUNA CLASE del archivo: si de la relectura sale una correccion se declara y se trae, y no se escribe sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en esta vuelta. El `sha256` LF del archivo abre y cierra en `0a77b5a35a962621` | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LA SEDE DE `OP-L-02`: BUSCARLA, NO INVENTARLA. Es la `4.1` del acta 189 y la vara del acta 190 (`5.4`) la confirma medida: corrida con `--corte 63d0c5b4` da 71 fichas, 6 en LISTA sin ninguna prueba, 2 de ellas CONSUMIDAS por `OP-U-01` y 4 de TRABAJO REAL; de esas cuatro, tres son mesas cuyo producto documental SI existe en disco, y `OP-L-02` es LA UNICA SIN DOCUMENTO QUE MEDIR, con 0 menciones de fichero en su evidencia. Su `verificacion` habla de "las tres nominas afectadas" y de "cada grupo del backlog": BUSCA SI ESAS TRES NOMINAS TIENEN SEDE EN EL REPO, con comandos propios, y publica la busqueda entera (que se busco, donde, y que se encontro). Y EL LIMITE, ESCRITO PARA QUE NO SE CRUCE: si la busqueda no encuentra sede en ninguna parte, ESO ES EL RESULTADO Y SE PUBLICA COMO TAL. NO se le inventa una sede a la ficha, ni se declara HECHA, ni se mueve de estado: inventarle una sede es cambiar el alcance de la campana, y eso lo reserva el fundador | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

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

<!-- FIN ANEXO DE TAREAS -->
