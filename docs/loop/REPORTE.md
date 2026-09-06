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
| **TAREA 2** | LA GUARDA DEL SUJETO CONGELADO: SEPARA LA DEUDA DEL FALLO, Y VUELVE AL VEREDICTO. Son las adjudicaciones `4.4` y `4.6` del acta 190 y las dos mitades van juntas porque una sin la otra no sirve. (a) la guarda SEPARA EN SU SALIDA las entradas `NO DECIDIBLE` que traen MOTIVO ESCRITO de las que no lo traen, y publica LAS DOS CIFRAS CON SUS NOMBRES; hoy "3 entradas sin congelar" no distingue una deuda de una decision, y esa es la `P.1` que el acta 189 dejo encargada en su `4.7`. Las tres de hoy son `vuelta186_tarea2c_mutacion_cierre_tardio.py`, `vuelta187_tarea4_mutacion_dos_convenciones.py` y `vuelta188_tarea4_mutacion_cobertura_parejas.py`, y cuantas traen motivo escrito SE MIDE. (b) LA GUARDA VUELVE AL VEREDICTO del instrumento de la nomina: el `D.5` de la 189 la saco y el acta 190 lo TUMBA, porque publicar los tres nombres arriba y cerrar en verde deja sin sintoma al que solo mire el veredicto. Con la separacion de (a) puesta, el veredicto ya puede decir ROJO POR DEUDA DECLARADA distinto de ROJO POR FALLO sin dejar de ser rojo. NO SE AFLOJA NINGUNA GUARDA, y el rojo que salga se trae con su nombre. Con simulacion previa sobre copia en memoria y caso positivo por mutacion | **CERRADA, Y CIERRA EN ROJO POR DEUDA DECLARADA CON SU NOMBRE (exitcode 2)** | `SALIDA_V190_T2A_SIMULACION.txt` (4621 bytes), `SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt` (6763), `SALIDA_V190_T2_NOMINA.txt` (4510) |
| **TAREA 3** | LA BATERIA: QUE SU EXITCODE SEPARE, Y QUE RESTAURE SOLA LO QUE PISA. Son las adjudicaciones `4.4` y `4.9` del acta 190, y NO SE CORRE LA BATERIA en esta vuelta: se arregla su lanzador y se prueba con sus arneses. (a) EL EXITCODE SEPARA: hoy los diez tramos de la 189 salieron con exitcode 1 y en NUEVE de ellos no cayo ni un arnes, porque la fuente era siempre la guarda de nomina en deuda, y un unico `1` para un arnes caido y para una deuda declarada es degradacion silenciosa (banco 9). Que el lanzador distinga los dos casos en su salida sellada y en su codigo de salida, y que lo diga con su cifra. (b) LA BATERIA RESTAURA SOLA LAS SALIDAS SELLADAS AJENAS QUE PISA, como ya restaura `dataset/`: en la 189 piso TRES y las restauro una persona a mano, en dos vueltas distintas y a dos personas distintas. La restauracion va EN LF, y si el corte nuevo interesa se escribe AL LADO con nombre nuevo y su vuelta, nunca encima. Con simulacion previa y caso positivo por mutacion que CAIGA si una salida sellada ajena se queda pisada | **CERRADA EN VERDE, Y LA BATERIA NO SE CORRIO** | `SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt` (7489 bytes), `SALIDA_V190_T3_PLAN.txt` (7229), `SALIDA_V190_T3_SIGUIENTE.txt` (1555), `SALIDA_V190_T3_COTEJO_CLON.txt` (14332) |
| **TAREA 4** | LA RELECTURA AL DOBLE DEL TRAMO DEL PUESTO 2422. ES UNA DEUDA DEL ACTA 189 Y NO SE SALTA DOS VUELTAS SEGUIDAS: la 189 la aplazo con razon por ser vuelta de bateria, y esa razon ya no vale. El acta 189 encontro la discrepancia del puesto `2422` FUERA de sus dudosos marcados, y `AUDITOR.md` 1.2 dice que eso baja el credito de la tanda y obliga a releer ese tramo AL DOBLE. Corre la relectura con `scripts/loop/aislador_de_ciega.py`, sobre los vecinos deterministas del tramo del `2422`, con el criterio escrito, la ciega y el destape en ficheros separados, y las clases escritas ANTES de abrir el destape. Publica cuantos coinciden y cuantos discrepan. NO SE TOCA NINGUNA CLASE del archivo: si de la relectura sale una correccion se declara y se trae, y no se escribe sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en esta vuelta. El `sha256` LF del archivo abre y cierra en `0a77b5a35a962621` | **CERRADA, CON UNA DISCREPANCIA FUERA DEL MARCADO QUE SE TRAE ENTERA** | `SALIDA_V190_T4_AISLAMIENTO.txt` (5301 bytes), `SALIDA_V190_T4_CIEGA.txt` (39678), `SALIDA_V190_T4_MIS_CLASES.txt` (4934), `SALIDA_V190_T4_DESTAPE.txt` (31816), `SALIDA_V190_T4_COTEJO.txt` (20783) |
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

### TAREA 2. LA GUARDA DEL SUJETO CONGELADO. CERRADA, Y CIERRA EN ROJO CON SU NOMBRE

**EL VEREDICTO DE ESTA TAREA ES `ROJO POR DEUDA DECLARADA`, EXITCODE 2, Y ESE ROJO
SE TRAE SIN APAGARLO**, que es lo que el encargo manda con esas palabras. No se
afloja ninguna guarda para conseguirlo.

**LOS FICHEROS, MEDIDOS EN DISCO POR LAS DOS CONVENCIONES:**

| fichero | bytes en disco | bytes en LF | lineas | `sha256` LF |
|---|---:|---:|---:|---|
| `scripts/loop/vuelta190_tarea2a_simulacion.py` | 11228 | 11228 | 226 | `6105d791a048fb7e` |
| `scripts/loop/vuelta190_tarea2b_mutacion_deuda_y_fallo.py` | 17942 | 17942 | 338 | `7c4bfef637e33c40` |
| `scripts/loop/vuelta190_tarea2_nomina.py` | 11615 | 11615 | 248 | `a14806a6c48a76df` |
| `scripts/loop/verificar_mutaciones_viejas.py` (el sujeto tocado) | 144320 | 144320 | 2533 | `4461658cb4715172` |
| `docs/loop/SALIDA_V190_T2A_SIMULACION.txt` | 4621 | 4621 | 83 | `e409868bd13f1164` |
| `docs/loop/SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt` | 6763 | 6763 | 95 | `bc1f0f27849ffced` |
| `docs/loop/SALIDA_V190_T2_NOMINA.txt` | 4510 | 4510 | 77 | `82cc350f1dfbd694` |

El fuente tocado entra en la vuelta con **131802 bytes en `HEAD`** (leido con
`git cat-file -s`) y sale con **144320 bytes en disco y 144320 normalizado a LF**.

#### (a) LA SEPARACION, Y LA VARA VA ESCRITA ANTES DE MEDIR

**LA SIMULACION PREVIA CORRIO SOBRE COPIA EN MEMORIA Y ANTES DE TOCAR EL FUENTE**,
y lo probo en vez de prometerlo: su bloque F publica
`git status sobre el fuente que se va a tocar: 0 fila(s)`. La vara quedo escrita
en esa salida **antes** de medir nada:

- **marcas literales (7):** `GIT SHOW`, `CAT-FILE`, `COMMIT`, `SUJETO_FIJO`,
  `SHA256`, `NO SE TOCA`, `NO SE ESCRIBE`. Las cinco primeras son formas de la
  casa de nombrar un sujeto que no se mueve; las dos ultimas son la declaracion
  expresa de que el fichero vivo no se toca.
- **ventana:** mas o menos **3** lineas, sobre LA MAQUINA (el fichero sin su
  docstring de modulo), que es donde `anclaje_de()` ya busca las huellas de vivo.
- **regla:** TODAS las apariciones con marca da MOTIVO ESCRITO; ALGUNA sin marca
  da SIN MOTIVO ESCRITO. **El lado seguro es ese:** una apertura del fichero vivo
  sin explicar es deuda, no decision.

**LA MEDICION, QUE ES LO QUE EL ENCARGO PIDE CON ESAS PALABRAS** (*mide cuantas de
las tres traen motivo escrito, no lo supongas*), contada de
`docs/loop/SALIDA_V190_T2_NOMINA.txt`:

| entrada `NO DECIDIBLE` | apariciones en la maquina | marcas halladas | motivo escrito |
|---|---:|---|---|
| `vuelta186_tarea2c_mutacion_cierre_tardio.py` | 1 (linea 486) | `NO SE TOCA`, `NO SE ESCRIBE` | **SI** |
| `vuelta187_tarea4_mutacion_dos_convenciones.py` | 2 (lineas 140 y 144) | `GIT SHOW`, `COMMIT` / `COMMIT` | **SI** |
| `vuelta188_tarea4_mutacion_cobertura_parejas.py` | 1 (linea 15) | `COMMIT` | **SI** |

**LA RESPUESTA A LA `P.1`, MEDIDA Y NO SUPUESTA: LAS TRES TRAEN MOTIVO ESCRITO.
`SUJETO VIVO` 0, `NO DECIDIBLE CON MOTIVO ESCRITO` 3, `NO DECIDIBLE SIN MOTIVO
ESCRITO` 0**, y **la suma de las tres es 3, que es exactamente lo que devuelve la
guarda sin separar: CALZA**. Los tres ceros van escritos y no omitidos.

**Y NO SE EXIME A NADIE.** Las tres listas siguen contando para el veredicto y
`CASOS_DECLARADOS` no se abre: lo unico que cambia es que el rojo dice de que
especie es. **La guarda vieja tampoco se toca:** `guarda_del_sujeto_congelado()`
sigue devolviendo tuplas de **3** campos, que es lo que llaman los tres arneses
viejos, y eso se comprueba en el bloque H del arnes.

#### (b) LA GUARDA VUELVE AL VEREDICTO, Y SE PRUEBA QUITANDOLE LA PIEZA

`scripts/loop/vuelta190_tarea2_nomina.py` publica la comparacion que hace visible
lo que la `4.6` arregla, contada de su propia salida:

| | clase | exitcode |
|---|---|---:|
| **CON la guarda DENTRO del veredicto (hoy)** | **`ROJO POR DEUDA DECLARADA`** | **2** |
| SIN la guarda, que es lo que el `D.5` de la 189 hacia | `VERDE` | 0 |

**LAS DOS SON DISTINTAS.** Si fueran iguales, la guarda no estaria enchufada y
esto no probaria nada. **Con el `D.5` puesto, esta misma vuelta habria cerrado en
VERDE con tres entradas en deuda**, que es literalmente lo que el acta 190
describe: *deja sin sintoma al que solo mire el veredicto*.

**LOS TRES CODIGOS, Y NINGUNO AFLOJA:** `VERDE` 0, `ROJO POR FALLO` 1,
`ROJO POR DEUDA DECLARADA` 2. **Los dos rojos siguen siendo distintos de cero**,
asi que nadie que compruebe `!= 0` cambia de conducta. **La precedencia va escrita
y no es discutible: el fallo gana.** Publicar deuda habiendo un arnes caido seria
la misma degradacion silenciosa, pero al reves. Y `SUJETO VIVO` cuenta como
**fallo y no como deuda**, porque un arnes que abre el fichero de hoy sin nada que
lo module no mide su maquina, mide el dia.

#### EL ARNES, Y LOS DOS ROJOS QUE ME CAZO A MI ANTES DE DEJARME CERRAR

`scripts/loop/vuelta190_tarea2b_mutacion_deuda_y_fallo.py`, **8 bloques, CIFRA
casos que CAEN 0, CIFRA mutaciones que NO cayeron 0, VEREDICTO VERDE**, contado de
`docs/loop/SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt`. Sus mutaciones caen todas,
y la que decide es la del bloque F: **con la pieza el veredicto es
`ROJO POR DEUDA DECLARADA` y sin ella es `VERDE`**.

**Y LAS DOS COSAS QUE LA CASA ME CAZO A MI, DECLARADAS EN VEZ DE ARREGLADAS EN
SILENCIO:**

1. **MI PROPIO ARNES ESCRIBIA UNA SALIDA QUE CAMBIABA SOLA.** La doble corrida de
   `vuelta190_tarea2_nomina.py` la tumbo: **mismos 6650 bytes y `sha256` distinto
   en cada corrida** (`4678b6db...`, `15fc1632...`, `5c00bdde...`). La causa,
   medida: el arnes imprimia la ruta de su temporal, y `tempfile.mkdtemp` le pone
   un sufijo al azar. **Corregido publicando el prefijo estable en vez de la ruta
   entera**, y remedido: las dos corridas dan ahora **6763 bytes y el mismo
   `sha256` `bc1f0f27849ffced`**.
2. **MI ARNES NUEVO NO ESTABA EN LA NOMINA.** `arneses_que_faltan()` lo acuso con
   su nombre. La regla de la casa es que **un arnes entra en la nomina en su misma
   vuelta** (acta 176, punto 7.2), asi que entran los **dos** que nacen hoy y **la
   nomina pasa de 125 a 127**. **NO SE PODA NADA**: el fundador RECHAZO podarla el
   5 sep 2026.

**Y UNA TERCERA, QUE ES LA `4.9` APLICADA A MANO ANTES DE TENERLA EN CODIGO.** Re
correr `vuelta179_tarea4_juzgar_sujeto.py` (uno de los tres arneses viejos que
usan esta guarda, corrido para comprobar que no rompo nada) **piso una salida
sellada de la vuelta 179**: `docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl` paso de
**17 filas a 3**. Se aplico la doctrina de la `4.9` con la mano: **el corte nuevo
al lado con su nombre y su vuelta** (`docs/plan/SUJETO_CONGELADO_VEREDICTOS_V190.jsonl`,
**4356 bytes en disco y 4356 normalizado a LF**, **3 filas**, `sha256` LF
`8f7ad886cf93ca6d`) y **el original restaurado con `git checkout --`** y remedido:
**20956 bytes en disco, 20939 normalizado a LF, 17 filas**, `sha256` LF
`4fa7413a97727357`. **El corte nuevo interesa y por eso se conserva:** dice que la
deuda de aquella vuelta bajo de 17 a 3.

**LOS TRES ARNESES VIEJOS QUE USAN ESTA GUARDA SIGUEN VERDES**, corridos por mi
despues del cambio: `vuelta178_tarea1e_mutacion_higiene.py` (exit 0, 18 casos),
`vuelta180_tarea2c_mutacion_cableado.py` (exit 0, 10 comprobaciones, 0 fallan) y
`vuelta179_tarea4_juzgar_sujeto.py` (exit 0).

**EL CARRIL `--sujeto-congelado` DEL PROPIO INSTRUMENTO**, corrido por mi, cierra
con **`ROJO POR DEUDA DECLARADA`** y **`CIFRA exitcode de este carril: 2`**.

**GATE 0 AL CERRAR LA TAREA:** `GATE 0: OK`, motor **25/25**, `tsc` exit **0**, y
`git diff --numstat -- dataset/` en **0 filas**.

### TAREA 3. EL LANZADOR DE LA BATERIA. CERRADA EN VERDE, Y LA BATERIA NO SE CORRE

**LA BATERIA NO SE CORRIO EN ESTA VUELTA, Y ESO NO ES UN HUECO SINO EL ENCARGO.**
La 189 la corrio entera y por `AUDITOR.md` 6.1 la siguiente cae en la **194**. Lo
que se hizo aqui es **arreglar su lanzador y probarlo con sus arneses**. De el se
corrieron **`--plan` y `--siguiente`**, que no escriben ninguna salida sellada de
tramo y no corren ningun arnes; **`--tramo` no se invoco ni una vez**.

**LOS FICHEROS, MEDIDOS EN DISCO POR LAS DOS CONVENCIONES:**

| fichero | bytes en disco | bytes en LF | lineas | `sha256` LF |
|---|---:|---:|---:|---|
| `scripts/loop/vuelta190_bateria_por_tramos.py` | 44857 | 44857 | 949 | `01e40dcf9ab20f9b` |
| `scripts/loop/vuelta190_tarea3b_mutacion_selladas_ajenas.py` | 14532 | 14532 | 283 | `25455d33314884b4` |
| `docs/loop/SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt` | 7489 | 7489 | 91 | `6a4f66f26dfbadbb` |
| `docs/loop/SALIDA_V190_T3_PLAN.txt` | 7229 | 7069 | 160 | `a45e5ce2636f8b7a` |
| `docs/loop/SALIDA_V190_T3_SIGUIENTE.txt` | 1555 | 1524 | 31 | `cf4c4a0a8f426272` |
| `docs/loop/SALIDA_V190_T3_COTEJO_CLON.txt` | 14332 | 14078 | 254 | `080e6ec950149ec9` |

**EL CLON, DECLARADO Y COTEJADO SALGA LO QUE SALGA.**
`scripts/loop/vuelta190_bateria_por_tramos.py` es clon declarado del de la 189, y
`scripts/loop/cotejar_clon_declarado.py` lo publica sin adornos: **docstring A 43
lineas y B 62; maquina A 706 y B 888; 184 lineas de maquina que difieren; 848
tokens que difieren; 165 SENTENCIAS DE CODIGO y 19 LITERALES DE TEXTO.** **Este
clon CAMBIA CODIGO y el cotejo lo dice**, que es exactamente el caso que la `4.8`
del acta 189 manda separar y cuya separacion en codigo **queda fuera de esta
vuelta y va nombrada en el encargo**.

#### (a) EL EXITCODE SEPARA, Y LA CIFRA SE DICE

La causa esta medida en la `4.4` y no supuesta: **los diez tramos de la 189
salieron con `exitcode 1` y en NUEVE de ellos no cayo ni un arnes**; la fuente era
siempre la guarda de nomina en deuda. **Un unico `1` para un arnes caido y para
una deuda declarada es degradacion silenciosa (banco 9).**

Desde la TAREA 2, `verificar_mutaciones_viejas.py` devuelve **0, 1 o 2** segun la
clase. El lanzador **lee ese codigo, lo NOMBRA en su salida sellada y lo PROPAGA a
su propio codigo de salida**, sin aplanarlo a 1:

| codigo | clase | donde se dice |
|---:|---|---|
| 0 | `VERDE` | `CIFRA clase del exitcode del tramo` (dentro de la salida sellada del tramo) |
| 1 | `ROJO POR FALLO` | idem, y `CIFRA clase del exitcode del lanzador` al terminar |
| 2 | `ROJO POR DEUDA DECLARADA` | idem |

**LOS TRES NOMBRES NO SE TECLEAN EN EL LANZADOR:** salen del diccionario
`CODIGO_DE_LA_CLASE` de `verificar_mutaciones_viejas.py`, para que las dos mitades
no puedan discrepar. **Y un codigo que nadie declaro no se traga:** sale como
`ROJO DE ESPECIE DESCONOCIDA`, que sigue siendo rojo y ademas dice que no se sabe
de que es, que es mas informacion que un `1` mudo.

#### (b) LA BATERIA RESTAURA SOLA LAS SALIDAS SELLADAS AJENAS QUE PISA

Es el **PASO 6** nuevo del tramo, y va **despues** del sellado a proposito: si
corriera antes, restauraria la salida del propio tramo, que es justo lo que acaba
de escribirse. La disciplina es la misma que la de `dataset/` porque es el mismo
problema: **se mide lo que se movio, se guarda el corte nuevo al lado, se restaura
el original, y SE VUELVE A MEDIR.** Restaurar sin remedir es prometer, no
comprobar.

- **QUE ES AJENA NO SE TECLEA:** sale de que el nombre del fichero lleve dentro un
  numero de vuelta distinto del de este lanzador, que a su vez se computa de
  `os.path.basename(__file__)`. **Una lista tecleada de ficheros a proteger seria
  proteger lo que uno se acuerda, no lo que hay.**
- **UNA SELLADA PROPIA PISADA NO ES ROJO:** lo que esta corrida escribe es suyo, y
  restaurarlo seria borrar el dia.
- **SI EL CORTE NUEVO INTERESA, SE ESCRIBE AL LADO CON NOMBRE NUEVO Y SU VUELTA,
  NUNCA ENCIMA**, y eso es una funcion (`nombre_del_corte_nuevo`) y no una
  costumbre. **La escritura va EN LF**, que es la convencion de la casa en disco.
- **Y SI AL REMEDIR QUEDA ALGUNA PISADA, EL TRAMO SALE EN ROJO** con esas
  palabras: *eso borra el registro de otra vuelta*.

**LAS TRES QUE LA 189 PISO, CLASIFICADAS POR ESTA VARA SIN ABRIRLAS NI TOCARLAS**
(bloque G del arnes): `SALIDA_V184_T1C_MUTACION_ESTIMACION.txt` (vuelta 184),
`SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt` (187) y
`SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt` (188). **Las TRES salen AJENAS
respecto de esta vuelta**, o sea que la restauracion automatica **las habria
cubierto a las tres**, que es lo que en la 189 tuvo que hacer una persona a mano,
en dos vueltas distintas y a dos personas distintas.

#### EL ARNES, CON EL CASO QUE EL ENCARGO PIDE CON ESAS PALABRAS

`scripts/loop/vuelta190_tarea3b_mutacion_selladas_ajenas.py`, **7 bloques, CIFRA
casos que CAEN 0, CIFRA mutaciones que NO cayeron 0, VEREDICTO VERDE**, contado de
`docs/loop/SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt`. **El caso que el encargo
pide es el bloque E: CAE si una salida sellada ajena se queda pisada.** Sobre un
escenario fabricado, restaurada del todo da `VERDE`, una pisada da `ROJO`, las dos
pisadas dan `ROJO`, y una **propia** pisada da `VERDE`. **Si los dos escenarios
dieran lo mismo, la guarda no estaria mirando nada.**

**Y EL ARNES ME CAZO A MI OTRA VEZ, Y SE DECLARA:** en su bloque F teclee a mano
los bytes esperados del fichero fabricado (**22 y 20**) y **los dos CAYERON**: son
**23 y 21**. Corregido no metiendo las cifras buenas, sino **cambiando el esperado
por una RELACION medida sobre el propio fichero** (`bytes del corte = bytes en
disco menos los retornos de carro`), que es lo que no se puede equivocar al contar
de cabeza. **Es la misma especie que esta casa persigue desde la vuelta 74, y me
mordio dentro de mi propio arnes.**

#### LO QUE `--plan` Y `--siguiente` DICEN HOY, CORRIDOS POR MI

- **`--plan`** (exit 0): guarda de la atribucion **VERDE, 0 literales de vuelta
  clavados**; **nomina 127**, tamano de tramo **13**, **10 tramos**, **suma de las
  entradas de todos los tramos 127**; estimacion **entre 41,9 y 54,6 minutos**
  para la nomina entera, **con su corte pegado en la misma linea**
  (`HEAD bbe8af367232, nomina de 127 entradas contada en esta corrida`).
- **`--siguiente`** (exit 0): **10 tramos del reparto, 0 con salida sellada no
  vacia, 10 que FALTAN, EL SIGUIENTE ES EL TRAMO 1.** **Cuenta desde cero**, que es
  lo que un clon con su propio numero de vuelta tiene que hacer, y **no hereda ni
  una salida sellada de la corrida de la 189**.

**GATE 0 AL CERRAR LA TAREA:** `GATE 0: OK`, motor **25/25**, `tsc` exit **0**, y
`git diff --numstat -- dataset/` en **0 filas**.

### TAREA 4. LA RELECTURA AL DOBLE DEL TRAMO DEL 2422. CERRADA, Y ME SALE UNA DISCREPANCIA FUERA DEL MARCADO

**LA CABECERA DE UNA LINEA DE ESTA TAREA: 30 PUESTOS RELEIDOS A CIEGAS, 20
COINCIDEN Y 10 DISCREPAN; NUEVE CAEN DENTRO DE MIS DUDOSOS MARCADOS Y UNA CAE
FUERA, EL PUESTO 3182.** Las diez se resuelven **a favor del archivo** y **ninguna
clase se toca**.

**LOS FICHEROS, MEDIDOS POR LAS DOS CONVENCIONES:**

| fichero | bytes en disco | bytes en LF | lineas | `sha256` LF |
|---|---:|---:|---:|---|
| `scripts/loop/vuelta190_tarea4_relectura_al_doble.py` | 11340 | 11340 | 256 | `037bad0ee9024324` |
| `docs/loop/SALIDA_V190_T4_AISLAMIENTO.txt` | 5301 | 5301 | 78 | `9df007a50a1add26` |
| `docs/loop/SALIDA_V190_T4_CIEGA.txt` | 39678 | 39678 | 494 | `0e2e4f4c6b9ed113` |
| `docs/loop/SALIDA_V190_T4_MIS_CLASES.txt` | 4934 | 4934 | 57 | `726833347bd0c798` |
| `docs/loop/SALIDA_V190_T4_DESTAPE.txt` | 31816 | 31816 | 132 | `3e38cb6863405a73` |
| `docs/loop/SALIDA_V190_T4_COTEJO.txt` | 20783 | 20497 | 286 | `f8e1a8f6b2f5b296` |

**EL ORDEN NO SE PROMETE, SE LEE DE GIT.** El aislamiento y los dos ficheros
quedaron commiteados en **`a0148267`**, mis clases en **`92b22813`**, y el cotejo
solo existe despues. **Unas clases escritas despues del destape no prueban nada**,
y por eso van en ficheros y en commits separados.

#### EL SUJETO, ELEGIDO Y AISLADO ANTES DE MIRAR NADA

**QUE ES "EL TRAMO DEL 2422", MEDIDO Y NO TECLEADO:** la ciega del acta 189,
`docs/loop/_auditor_v189b_ciega_blind.txt`, **30 puestos**, y el **2422 esta
DENTRO** (contado de su fichero; si no lo estuviera, este instrumento hace PARADA
y no relee nada).

**QUE ES "AL DOBLE":** sus **30 vecinos deterministas**, con `vecinos()`
**IMPORTADA** de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no
copiada. **30 del tramo mas 30 vecinos son 60 puestos: el doble exacto.**

**EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO** (acta 188, `5.2` y `7.3`): a
`vecinos()` se le pasa `evitar` con los **441** puestos ya consumidos, contados de
sus **cuatro** ficheros (las dos exclusiones, 411 y 381, y las dos ciegas, 30 y
30). **Solape de los vecinos con el propio tramo: 0. Solape con el universo
consumido: 0. Los dos POR CONSTRUCCION**, porque `evitar` va dentro de la llamada
y no comprobado despues. **Su regla no se toca: cambia lo que se le pasa.**

**EL AISLADOR EN VERDE**, exitcode **0**: **30 pares elegidos, los 30 existen en el
archivo, `CIFRA fugas del destape en la salida ciega: 0`**. Ciega y destape en
**ficheros separados**, con el **criterio escrito literal** dentro de los dos.

#### EL COTEJO, CON LAS CIFRAS QUE EL ENCARGO PIDE

| medicion | cifra |
|---|---:|
| puestos releidos | **30** |
| **coinciden** | **20** |
| **discrepan** | **10** |
| discrepancias DENTRO de mis dudosos marcados | **9** |
| **discrepancias FUERA de mis dudosos marcados** | **1** |
| dudosos que marque y que SI coincidieron | 4 |

**MI REPARTO: A 7, B 3, C 0, D 20. EL DEL ARCHIVO: A 7, B 1, C 0, D 22.**

**LAS NUEVE DE DENTRO:** 648, 872, 904, 963, 1201, 1366, 2423, 3067 y 3086. Las
nueve las marque como dudosas **antes de saber si acertaba**, y las nueve se
resuelven a favor del archivo. Los casos que mas ensenan: el **1366**, donde el
archivo mide que **cuatro de los cinco pasos de cada uno se corresponden** y yo
me quede en que uno hablaba de embudo y el otro de capacidad; y el **2423**, el
vecino del propio 2422, donde el archivo separa **la linea contra su
procedimiento** con ids gemelos y misma fuente, y yo lo di por dudoso.

#### LA QUE CAE FUERA, Y SE TRAE ENTERA PORQUE ESO ES LO QUE BAJA EL CREDITO

**EL PUESTO 3182. YO DIJE `D` Y EL ARCHIVO DICE `A`, Y NO LO MARQUE COMO DUDOSO.**

- **mi motivo, literal de mi propio fichero de clases:** *"el plan de control del
  proceso del proveedor contra la planificacion tecnologica conjunta, **aunque
  comparten seis pasos**"*.
- **la razon del archivo:** misma fuente (Juran), `sim_tit 53,3`, sin arista,
  **`DISCUTIBLE MARCADO fuerte`** escrito en su propia razon, **tres pasos casi
  verbatim compartidos**, y **`A POR FUSION MUTUA`**, que mueve el contador de
  fusiones mutuas de veintiseis a veintisiete.

**ME EQUIVOQUE YO, Y LA PRUEBA ESTA EN MI PROPIA LINEA:** escribi *"aunque
comparten seis pasos"* y aun asi clasifique `D` **sin marcarlo dudoso**. Si seis
de los seis pasos del nodo corto estan en el largo, mi propio criterio escrito
(*"A cuando la mayoria de los pasos del nodo mas corto estan en el mas largo"*)
manda `A`. **La discrepancia es a favor del archivo y no hay ninguna correccion
que hacerle.**

**LO QUE ESO DISPARA, DICHO Y NO ESCONDIDO.** `AUDITOR.md` 1.2: *"si una
discrepancia aparece FUERA de los discutibles marcados, baja el credito de toda la
tanda: ese tramo se relee al doble y lo dices en el acta"*. **Esta tanda de 30 la
lei yo, y su credito baja por mi cuenta.** El tramo que habria que releer al doble
es el de estos 30 vecinos. **Yo no me lo auto encargo:** el encargo de esta vuelta
trae CINCO tareas y ese es el tope, y quien encarga las relecturas al doble es el
auditor. **Lo traigo medido, con su nombre y su cifra, para que la 191 lo
encuentre escrito.**

#### LO QUE ESTA TAREA NO HIZO

**NO SE TOCO NINGUNA CLASE.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abrio
**solo en lectura**, y su `sha256` LF abre y cierra en
**`0a77b5a35a962621`** (medido al entrar por el bloque A del aislamiento, al salir
por su bloque G, y otra vez en el bloque E del cotejo). **Las diez discrepancias
se resuelven a favor del archivo y no se escribe ni una fila.**

<!-- FIN ANEXO DE TAREAS -->
