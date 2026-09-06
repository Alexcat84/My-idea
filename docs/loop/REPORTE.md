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

**EL VEREDICTO DE UNA LINEA: **EL VEREDICTO DE UNA LINEA: LAS CINCO TAREAS CERRARON Y VOLVIO EL TOPE DE CINCO, LA GUARDA DEL SUJETO CONGELADO ESTA DE VUELTA EN EL VEREDICTO Y ESA TAREA CIERRA EN ROJO POR DEUDA DECLARADA CON EXITCODE 2 SIN QUE SE AFLOJE NINGUNA GUARDA, EL EXITCODE DE LA BATERIA YA SEPARA EL ARNES CAIDO DE LA DEUDA Y LA BATERIA RESTAURA SOLA LAS SALIDAS SELLADAS AJENAS QUE PISA, LA RELECTURA AL DOBLE DEL TRAMO DEL 2422 SE HIZO CON 20 COINCIDENCIAS Y 10 DISCREPANCIAS DE LAS QUE UNA CAE FUERA DE MIS DUDOSOS Y LA TRAIGO ENTERA, Y LA SEDE DE OP-L-02 SE BUSCO SIN INVENTARLA: LAS TRES NOMINAS SI LA TIENEN Y LO QUE FALTA SE ELEVA.****
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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 190`, y su salida
cruda vive en `docs/loop/SALIDA_V190_TALLADOR_CABECERA.txt` (2721 bytes en disco y 2700 normalizado a LF, 12 filas de
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
| marcador del cribado `A` / `B` / `C` / `D`, `n` | (sin cambio esta vuelta: no se remidio) | **551 / 72 / 5 / 2.760, n 3.388** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `bbeea713` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 189: LA 188 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA, ADJUDICO LOS SEIS DISCUTIBLES A FAVOR Y CONTESTO LAS TRES PREGUNTAS, DECLARO DOS CAIDAS PROPIAS MIAS Y CERO DEL EJECUTOR, Y CAZO QUE EL LANZADOR DE LA BATERIA YA REPARTE EN DIEZ TRAMOS Y SU --siguiente HABRIA CORRIDO OCHO ARNESES DE 125 DECLARANDOSE CORRIDO.'), HEAD real de apertura `b393347f` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `581330e4` (leido de `SALIDA_V190_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 190 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus DIEZ adjudicaciones `4.1` a `4.10`, QUE NO SON DIEZ A FAVOR: seis son los discutibles del ejecutor y de esos CINCO van A FAVOR (`D.1`, `D.2`, `D.3`, `D.4`, `D.6`) y UNO EN CONTRA, el `D.5`, la guarda del sujeto congelado fuera del veredicto. La marca de EN CONTRA tiene que EXISTIR y tiene que SALIR EN LA CUENTA, probada por mutacion con un acta fabricada. Mas las TRES preguntas contestadas (`4.4` la `P.1`, `4.8` la `P.2`, `4.9` la `P.3`), los DOS hallazgos de la seccion 5 que no salen de ningun discutible (las dos convenciones de `lineas` en `5.1` y las ocho actas sin entrada propia en `5.2`), CERO caidas propias del auditor ESCRITO COMO CERO Y NO OMITIDO y TRES del ejecutor, las tres DE METODO y ninguna de racha, y LA VARA CORRIDA POR EL AUDITOR (`5.4`) con sus cifras. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido, no escribe nada, y se prueba re corriendolo con la sede medida antes y despues | **CERRADA EN VERDE** | `SALIDA_V190_T1A_MUTACION_REGISTRADOR.txt`, `SALIDA_V190_T1A_SIMULACION.txt`, `SALIDA_V190_T1A_REGISTRO_R52.txt` y `SALIDA_V190_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, con sus bytes por las dos convenciones, disco y LF, en la tabla de la seccion 2 |
| **TAREA 2** | LA GUARDA DEL SUJETO CONGELADO: SEPARA LA DEUDA DEL FALLO, Y VUELVE AL VEREDICTO. Son las adjudicaciones `4.4` y `4.6` del acta 190 y las dos mitades van juntas porque una sin la otra no sirve. (a) la guarda SEPARA EN SU SALIDA las entradas `NO DECIDIBLE` que traen MOTIVO ESCRITO de las que no lo traen, y publica LAS DOS CIFRAS CON SUS NOMBRES; hoy "3 entradas sin congelar" no distingue una deuda de una decision, y esa es la `P.1` que el acta 189 dejo encargada en su `4.7`. Las tres de hoy son `vuelta186_tarea2c_mutacion_cierre_tardio.py`, `vuelta187_tarea4_mutacion_dos_convenciones.py` y `vuelta188_tarea4_mutacion_cobertura_parejas.py`, y cuantas traen motivo escrito SE MIDE. (b) LA GUARDA VUELVE AL VEREDICTO del instrumento de la nomina: el `D.5` de la 189 la saco y el acta 190 lo TUMBA, porque publicar los tres nombres arriba y cerrar en verde deja sin sintoma al que solo mire el veredicto. Con la separacion de (a) puesta, el veredicto ya puede decir ROJO POR DEUDA DECLARADA distinto de ROJO POR FALLO sin dejar de ser rojo. NO SE AFLOJA NINGUNA GUARDA, y el rojo que salga se trae con su nombre. Con simulacion previa sobre copia en memoria y caso positivo por mutacion | **CERRADA, Y CIERRA EN ROJO POR DEUDA DECLARADA CON SU NOMBRE (exitcode 2)** | `SALIDA_V190_T2A_SIMULACION.txt`, `SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt` y `SALIDA_V190_T2_NOMINA.txt`, con sus bytes por las dos convenciones, disco y LF, en la tabla de la seccion 2 |
| **TAREA 3** | LA BATERIA: QUE SU EXITCODE SEPARE, Y QUE RESTAURE SOLA LO QUE PISA. Son las adjudicaciones `4.4` y `4.9` del acta 190, y NO SE CORRE LA BATERIA en esta vuelta: se arregla su lanzador y se prueba con sus arneses. (a) EL EXITCODE SEPARA: hoy los diez tramos de la 189 salieron con exitcode 1 y en NUEVE de ellos no cayo ni un arnes, porque la fuente era siempre la guarda de nomina en deuda, y un unico `1` para un arnes caido y para una deuda declarada es degradacion silenciosa (banco 9). Que el lanzador distinga los dos casos en su salida sellada y en su codigo de salida, y que lo diga con su cifra. (b) LA BATERIA RESTAURA SOLA LAS SALIDAS SELLADAS AJENAS QUE PISA, como ya restaura `dataset/`: en la 189 piso TRES y las restauro una persona a mano, en dos vueltas distintas y a dos personas distintas. La restauracion va EN LF, y si el corte nuevo interesa se escribe AL LADO con nombre nuevo y su vuelta, nunca encima. Con simulacion previa y caso positivo por mutacion que CAIGA si una salida sellada ajena se queda pisada | **CERRADA EN VERDE, Y LA BATERIA NO SE CORRIO** | `SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt`, `SALIDA_V190_T3_PLAN.txt`, `SALIDA_V190_T3_SIGUIENTE.txt` y `SALIDA_V190_T3_COTEJO_CLON.txt`, con sus bytes por las dos convenciones, disco y LF, en la tabla de la seccion 2 |
| **TAREA 4** | LA RELECTURA AL DOBLE DEL TRAMO DEL PUESTO 2422. ES UNA DEUDA DEL ACTA 189 Y NO SE SALTA DOS VUELTAS SEGUIDAS: la 189 la aplazo con razon por ser vuelta de bateria, y esa razon ya no vale. El acta 189 encontro la discrepancia del puesto `2422` FUERA de sus dudosos marcados, y `AUDITOR.md` 1.2 dice que eso baja el credito de la tanda y obliga a releer ese tramo AL DOBLE. Corre la relectura con `scripts/loop/aislador_de_ciega.py`, sobre los vecinos deterministas del tramo del `2422`, con el criterio escrito, la ciega y el destape en ficheros separados, y las clases escritas ANTES de abrir el destape. Publica cuantos coinciden y cuantos discrepan. NO SE TOCA NINGUNA CLASE del archivo: si de la relectura sale una correccion se declara y se trae, y no se escribe sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en esta vuelta. El `sha256` del archivo abre y cierra en `0a77b5a35a962621` por las dos convenciones, en disco y normalizado a LF | **CERRADA, CON UNA DISCREPANCIA FUERA DEL MARCADO QUE SE TRAE ENTERA** | `SALIDA_V190_T4_AISLAMIENTO.txt`, `SALIDA_V190_T4_CIEGA.txt`, `SALIDA_V190_T4_MIS_CLASES.txt`, `SALIDA_V190_T4_DESTAPE.txt` y `SALIDA_V190_T4_COTEJO.txt`, con sus bytes por las dos convenciones, disco y LF, en la tabla de la seccion 2 |
| **TAREA 5** | LA SEDE DE `OP-L-02`: BUSCARLA, NO INVENTARLA. Es la `4.1` del acta 189 y la vara del acta 190 (`5.4`) la confirma medida: corrida con `--corte 63d0c5b4` da 71 fichas, 6 en LISTA sin ninguna prueba, 2 de ellas CONSUMIDAS por `OP-U-01` y 4 de TRABAJO REAL; de esas cuatro, tres son mesas cuyo producto documental SI existe en disco, y `OP-L-02` es LA UNICA SIN DOCUMENTO QUE MEDIR, con 0 menciones de fichero en su evidencia. Su `verificacion` habla de "las tres nominas afectadas" y de "cada grupo del backlog": BUSCA SI ESAS TRES NOMINAS TIENEN SEDE EN EL REPO, con comandos propios, y publica la busqueda entera (que se busco, donde, y que se encontro). Y EL LIMITE, ESCRITO PARA QUE NO SE CRUCE: si la busqueda no encuentra sede en ninguna parte, ESO ES EL RESULTADO Y SE PUBLICA COMO TAL. NO se le inventa una sede a la ficha, ni se declara HECHA, ni se mueve de estado: inventarle una sede es cambiar el alcance de la campana, y eso lo reserva el fundador | **CERRADA. LAS TRES NOMINAS SI TIENEN SEDE; LO QUE FALTA SE ELEVA SIN CRUZAR EL LIMITE** | `SALIDA_V190_T5_SEDE_OP_L_02.txt`, con sus bytes por las dos convenciones, disco y LF, en la tabla de la seccion 2 |
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

**LA ENTRADA:** `R.52` en `docs/PENDIENTES.md`, **18764 bytes** (una entrada NO es un fichero: no hay disco ni LF que separar, y por eso esta cifra no lleva pareja de convenciones), **198 lineas por
`count(NL)` y 199 por `len(split(NL))`** (las dos convenciones publicadas, que es
justo el hallazgo `5.1` del acta) y **0 guiones largos o medios**. El numero **no
esta tecleado**: lo devuelve `scripts/loop/serie_de_registros.py`, que recompone
la serie de sus **dos** sedes y da **43 entradas, 0 colisiones, 0 huecos,
siguiente libre R.52**. Despues de escribir, remedido: **44 entradas, 0
colisiones, 0 huecos, siguiente libre R.53**. La sede crece en **18765**, que son los **18764** de la
entrada mas su salto de linea. **Esa cifra es una DIFERENCIA y no el tamano de
ningun fichero**, asi que no lleva pareja de convenciones;
sus dos mediciones, la de antes y la de despues, van con su corte en la tabla de
la idempotencia de mas abajo, porque **la de antes ya no es la del disco de
hoy**.

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
`docs/loop/_auditor_v190_vara.txt`, mide **17445 bytes en disco y 17164 normalizado a LF**, y nombra `OP-L-02` **3 veces**.

**LA IDEMPOTENCIA, PROBADA POR MI Y NO HEREDADA, CON LA SEDE MEDIDA ANTES Y
DESPUES.** Es lo que el encargo pide con esas palabras:

La sede es `docs/PENDIENTES.md`, y **cada cifra va con su corte** porque la
primera de las tres **ya no es la del disco de hoy**: es el estado del arbol en
`70d5662c`, antes de que esta tarea escribiera nada. Las tres, con las dos
convenciones:

| corte | bytes en disco | bytes en LF |
|---|---:|---:|
| antes de la primera corrida (arbol de `70d5662c`) | 961248 | 961248 |
| despues de escribir el `R.52` | 980013 | 980013 |
| **despues del RE CORRIDO, que es el disco de hoy** | **980013** | **980013** |

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

El fuente tocado entra en la vuelta con **131802 bytes en `HEAD`**, leido con `git cat-file -s`, que es su medida normalizada a LF, y sale con **144320 bytes en disco y 144320 normalizado a LF**.

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
   `vuelta190_tarea2_nomina.py` la tumbo. **La cifra de antes lleva su corte porque
   ya no es la del disco de hoy:** en el arbol previo a la correccion, esa salida
   media **los mismos 6650 bytes en disco y 6650 normalizado a LF** y sacaba **tres `sha256` distintos** en tres corridas (`4678b6db...`, `15fc1632...`, `5c00bdde...`). La causa, medida: el arnes imprimia la ruta de su temporal, y
   `tempfile.mkdtemp` le pone un sufijo al azar. **Corregido publicando el
   prefijo estable en vez de la ruta entera**, y remedido: las dos corridas dan
   ahora el mismo **`sha256` `bc1f0f27849ffced` por las dos convenciones, en disco y normalizado a LF**, y sus bytes de hoy estan en la tabla de arriba.
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

### TAREA 5. LA SEDE DE `OP-L-02`. CERRADA, Y LA RESPUESTA NO ES LA QUE EL ENCARGO TEMIA

**LA CABECERA DE UNA LINEA: LAS TRES NOMINAS SI TIENEN SEDE EN EL REPO, Y ESTAN
MEDIDAS CON COBERTURA COMPLETA DESDE LA VUELTA 169. LO QUE `OP-L-02` NO TIENE ES
UN PRODUCTO DOCUMENTAL PROPIO EN `docs/plan/` NI UNA SOLA MENCION DE FICHERO EN SU
CAMPO `evidencia`.** No se le inventa ninguna sede, no se la declara HECHA y no se
la mueve de estado: sigue en `LISTA`.

**LOS FICHEROS, MEDIDOS POR LAS DOS CONVENCIONES:**

| fichero | bytes en disco | bytes en LF | lineas | `sha256` LF |
|---|---:|---:|---:|---|
| `scripts/loop/vuelta190_tarea5_sede_de_op_l_02.py` | 14028 | 14028 | 321 | `28431e872f3e7af8` |
| `docs/loop/SALIDA_V190_T5_SEDE_OP_L_02.txt` | 17879 | 17879 | 265 | `d39e232063a41eec` |

#### LO QUE SE BUSCO, DONDE, Y CON QUE UNIVERSO DICHO ANTES DE BUSCAR

- **El universo:** `docs/` y `scripts/`, extensiones `.md`, `.jsonl`, `.txt`,
  `.json`, `.py` y `.mjs`, excluyendo `__pycache__`, `node_modules` y `.git`.
  **CIFRA ficheros del universo: 10901.**
- **Que se busco:** los nombres de **las tres nominas** y de **los cuatro grupos
  del backlog**, leidos **del campo `nota` de la propia ficha** y no de una lista
  tecleada, cada uno con su literal al lado.
- **La busqueda negativa se hizo con su comando y no se cita** (`EJECUTOR.md` 9):
  cada busqueda queda escrita con lo que se busco y donde, para que el cero se
  pueda repetir.

**Y UNA CORRECCION DECLARADA SOBRE MI PROPIA APERTURA:** el bloque **H.7** del
sello de apertura de esta vuelta publica **`CIFRA fichas con id OP-L-02: 0`** sobre
las 71 fichas. **Esa cifra es cierta y engana:** busque por las claves `id` y
`operacion`, y **la clave del id en `docs/plan/OPERACIONES.jsonl` es `id_op`**. La
ficha existe y vive en la **linea 42**. **El texto viejo no se borra:** queda en el
sello de apertura, ya commiteado, con esta correccion al lado.

#### LA BUSQUEDA, CON SUS CIFRAS

**LAS TRES NOMINAS AFECTADAS:**

| nomina (literal de la ficha) | ficheros que la nombran | candidatos a sede en `docs/plan/` |
|---|---:|---:|
| `cuadrantes de mercado (8)` | 518 | 3 |
| `ecuacion de valor (5)` | 356 | 2 |
| `el bloque humano de la supervision de la IA (3)` | 103 | 4 |

**LOS CUATRO GRUPOS DEL BACKLOG:**

| grupo | ficheros que lo nombran |
|---|---:|
| 126 esperan destejido | 435 |
| 55 resto sin mesa ni nomina | 17 |
| 5 de sales roadmap | 137 |
| 3 ya leidas en la primera tanda | 32 |

**LAS SIETE RUTAS QUE LA PROPIA FICHA NOMBRA EXISTEN LAS SIETE Y NINGUNA MIDE CERO
BYTES**, comprobadas una a una en disco (una ruta publicada como prueba es CIFRA,
`EJECUTOR.md` 1): `SALIDA_V169_T5_COBERTURA_OP_L_02.txt` (5559), 
`SALIDA_V169_T5_LOTE_SALES_ROADMAP.txt` (7945),
`SALIDA_V170_T3_DEUDAS_DE_CORTE.txt` (5337), `SALIDA_V170_T4B_PUENTES.txt` (4564),
`docs/plan/LD_SALES_ROADMAP.md` (20563), `docs/plan/LECTURAS_DIRIGIDAS.md`
(214916) y `docs/plan/INVENTARIO.jsonl` (584554).

#### LA RESPUESTA, Y VA CON LA DISTINCION QUE LA VARA NO HACE

**LAS TRES NOMINAS TIENEN SEDE, Y ADEMAS ESTAN MEDIDAS.** Su cobertura se computo
en la vuelta 169 y vive en `docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt`
(**5559 bytes en disco y 5449 normalizado a LF**, **110 lineas**), cuya tabla final,
contada de ese fichero, dice: **46 pares posibles en las seis nominas, 0 pares SIN
veredicto, y 6 de 6 nominas con cobertura COMPLETA**. Y su contenido vive en
`docs/plan/LECTURAS_DIRIGIDAS.md`, `docs/plan/INVENTARIO.jsonl`,
`docs/plan/RECOMPUTO_3388.md` y `docs/plan/LD_SALES_ROADMAP.md`.

**LO QUE NO TIENE, MEDIDO Y NO SUPUESTO, SON DOS COSAS DISTINTAS Y CONVIENE NO
CONFUNDIRLAS:**

1. **CERO MENCIONES DE FICHERO EN SU CAMPO `evidencia`.** Su evidencia entera son
   **73 caracteres de prosa**: *"MEDIDO el 11 ago 2026: 205 pares fuera de cola,
   11 leidos, 194 pendientes"*. **Eso es lo que la vara del acta 190 mide**, y por
   eso la saca como **la unica de las cuatro mesas de TRABAJO REAL sin documento
   que medir**. La linea de la vara, leida de `docs/loop/_auditor_v190_vara.txt`:
   *"`OP-L-02` | 09_LECTURAS_DIRIGIDAS | ninguna | (su evidencia entera es prosa:
   no nombra ningun fichero) | NO"*.
2. **NINGUN PRODUCTO DOCUMENTAL PROPIO EN `docs/plan/`.** De los **178** ficheros
   que nombran `OP-L-02`, **solo UNO vive en `docs/plan/`**, y es
   `docs/plan/RECOMPUTO_3388.md`, que no es suyo. Es justo lo que la separa de sus
   hermanas: `OP-L-03` nombra `docs/plan/BANCO_DEL_PLAN.md` y
   `docs/plan/LECTURAS_DIRIGIDAS.md`, y `OP-I-01` nombra
   `docs/plan/INVENTARIO.jsonl` y `docs/plan/10_INVENTARIO.md`.

**Y AQUI VA LO QUE TRAIGO YO, QUE LA VARA NO MIDE PORQUE NO MIRA ESE CAMPO:** su
campo **`nota`** tiene **5578 caracteres** y **nombra 13 ficheros**, y su campo
`verificacion` **1682 caracteres** y **2 ficheros**. **La ficha SI apunta a
documentos; lo que no lo hace es el campo que la vara lee.** Ademas, **DOS ficheros
llevan su nombre dentro del suyo propio y los dos existen con bytes**:
`docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt` (5559) y
`docs/loop/SALIDA_V170_T5B_VEREDICTO_OP_L_02.txt` (5074). **Pero los dos viven en
`docs/loop/`, que es donde van las salidas de una vuelta, y no en `docs/plan/`, que
es donde vive el producto de una mesa.**

#### EL LIMITE, QUE NO SE CRUZA

**NO SE LE INVENTA UNA SEDE A LA FICHA.** Podria sostenerse que
`SALIDA_V169_T5_COBERTURA_OP_L_02.txt` **es** su producto documental, porque lleva
su nombre, mide sus nominas y existe con bytes. **No lo declaro yo:** decidir que
una salida de vuelta cuenta como producto de mesa **cambia el alcance de la
campana**, y el encargo reserva eso al fundador con esas palabras. **Lo mido, lo
publico entero, y lo elevo.**

**NO SE DECLARA HECHA Y NO SE MUEVE DE ESTADO:** sigue en **`LISTA`**. `docs/plan/OPERACIONES.jsonl` se abrio **solo en lectura** y mide **498085 bytes en disco y 498085 normalizado a LF** al entrar y al salir, **identicos**.

**LA PREGUNTA QUE TRAIGO, PARA QUE EL AUDITOR LA ELEVE:** dado que las tres
nominas **si** tienen sede y **si** estan medidas con cobertura completa desde la
169, y que `docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt` lleva el nombre de la
ficha y mide justo lo que su `verificacion` pide, **falta decidir si a `OP-L-02` le
falta un documento o solo le falta que su campo `evidencia` NOMBRE los que ya
existen**. **Son dos deudas muy distintas y la segunda es barata.** Yo no elijo
entre las dos.

<!-- FIN ANEXO DE TAREAS -->

## 3. LO QUE ESTA VUELTA SOSTIENE, Y NI UNA PALABRA MAS

1. **LAS CINCO TAREAS DEL ENCARGO CERRARON, Y VOLVIO EL TOPE DE CINCO.** El
   disparador de salida de la `AUDITOR.md` 6.2 pedia **DOS vueltas seguidas
   cerrando su propio reporte** y **son TRES**, localizadas **en git y no de
   memoria** por el bloque **B.2** del sello de apertura, con sus tres ficheros de
   cierre midiendo **`CIFRA piezas que faltan: 0`** los tres.
2. **EL ACTA 190 QUEDA REGISTRADA COMO `R.52`** (**18764 bytes**, y una entrada NO es un fichero: no hay disco ni LF que separar, y por eso esa cifra no lleva pareja de convenciones; **198 lineas por `count(NL)` y 199 por `len(split(NL))`**, **0 guiones**), con sus **10
   adjudicaciones**, y **NO SON DIEZ A FAVOR: 6 discutibles, 5 A FAVOR y 1 EN
   CONTRA**, el `D.5`, **medido del titulo literal y no tecleado**. La serie cierra
   en **44 entradas, 0 colisiones, 0 huecos**.
3. **LA MARCA `EN CONTRA` NO EXISTIA Y HABRIA HECHO PARAR AL REGISTRADOR.** El de
   la 189 conoce **cinco** marcas, ninguna es `EN CONTRA`, y ademas **PARABA si
   algun discutible no llevaba `A FAVOR`**. Y su maquina de caidas tampoco
   alcanzaba: la cabecera del acta 190 es **`## 6. LAS CAIDAS`, a secas**, y sus
   tres caidas van **dentro de un parrafo**, asi que **los cinco patrones de
   cabeza de linea dan 0** y `caidas_por_seccion()` da **(0, 0, 0)**.
4. **UN CERO DE RACHA NO ES UN CERO DE CUENTA, Y CONFUNDIRLOS HABRIA BORRADO TRES
   CIFRAS.** El acta 190 dice **`DEL EJECUTOR: CERO QUE ACUMULEN`** y **en ese
   mismo parrafo declara TRES**. Tratado como el `CERO SON DEL EJECUTOR` de la
   189, el reparto sale **ejecutor 0** en vez de **3**. Las dos especies van
   separadas con sus dos literales y probadas en los dos sentidos.
5. **LA GUARDA DEL SUJETO CONGELADO VOLVIO AL VEREDICTO Y ESTA VUELTA CIERRA ESA
   TAREA EN `ROJO POR DEUDA DECLARADA`, EXITCODE 2.** Es la `4.6`, el unico
   discutible que el acta tumbo. **Con el `D.5` puesto, esa misma medicion habria
   cerrado en `VERDE` exitcode 0 con tres entradas en deuda**, y las dos cifras se
   publican juntas. **Ese rojo se trae con su nombre y no se apaga.**
6. **LA RESPUESTA A LA `P.1`, MEDIDA Y NO SUPUESTA: LAS TRES ENTRADAS TRAEN MOTIVO
   ESCRITO.** `SUJETO VIVO` **0**, `NO DECIDIBLE CON MOTIVO ESCRITO` **3**,
   `NO DECIDIBLE SIN MOTIVO ESCRITO` **0**, y la suma de las tres calza con los
   **3** de la guarda sin separar. **La vara quedo escrita ANTES de medir** y la
   simulacion previa **probo** que no habia tocado el fuente (`git status` sobre
   el en **0 filas**).
7. **EL EXITCODE DE LA BATERIA YA SEPARA, Y LA BATERIA NO SE CORRIO.** `VERDE` 0,
   `ROJO POR FALLO` 1, `ROJO POR DEUDA DECLARADA` 2, **con los dos rojos distintos
   de cero**: nadie que compruebe `!= 0` cambia de conducta. El lanzador **lee el
   codigo, lo NOMBRA en la salida sellada del tramo y lo PROPAGA sin aplanarlo**.
   **La siguiente bateria cae en la 194.**
8. **LA BATERIA RESTAURA SOLA LAS SALIDAS SELLADAS AJENAS QUE PISA.** Es el
   **PASO 6** nuevo, con el corte nuevo escrito **al lado en LF y nunca encima**, y
   **remedido despues**. **Las TRES que la 189 piso salen AJENAS** con esta vara,
   o sea que la restauracion las habria cubierto a las tres.
9. **LA RELECTURA AL DOBLE DEL TRAMO DEL 2422 SE HIZO, Y ME SALE UNA DISCREPANCIA
   FUERA DEL MARCADO.** **30 puestos, 20 coinciden, 10 discrepan; 9 dentro de mis
   dudosos y 1 fuera, el 3182.** El solape con el tramo y con el universo consumido
   sale **0 y 0 POR CONSTRUCCION**. **Ninguna clase se toca** y las diez se
   resuelven **a favor del archivo**.
10. **LA SEDE DE `OP-L-02`: LAS TRES NOMINAS SI LA TIENEN Y ESTAN MEDIDAS.** Su
    cobertura vive desde la 169 en `docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt`
    (**46 pares posibles, 0 sin veredicto, 6 de 6 nominas completas**). **Lo que la
    ficha no tiene es producto documental propio en `docs/plan/` ni una sola
    mencion de fichero en su campo `evidencia`. No se le invento ninguna sede, no
    se declaro HECHA y no se movio de estado.**
11. **NADA SE MOVIO DE LO QUE NO SE PODIA MOVER.** El `sha256` LF de
    `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` **abre y cierra en `0a77b5a35a962621`** y
    **no se toco ninguna clase**. `git diff --numstat -- dataset/` da **0 filas al
    entrar y 0 al salir**. **La nomina NO se podo**: crece de **125 a 127** con los
    dos arneses que nacen hoy, que es lo que la regla manda.
12. **LO QUE NO ENTRO, DICHO PARA QUE NO SE BUSQUE:** ni cribado, ni recomputo, ni
    operaciones del plan que no fueran la **busqueda** de la TAREA 5, ni las mesas
    anotadas, ni **podar la nomina**, ni la bateria. **Y las SEIS que el encargo
    dejo nombradas a proposito siguen fuera**: las dos convenciones de `lineas`,
    `acumulan()` contra la tabla, el cotejo de clon que separa, la excepcion que
    publica siempre su lista, la medicion del censo de arneses sin fichero, y las
    ocho actas sin entrada propia.

## 4. EL ESTADO DEL ARBOL, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO

**LAS CIFRAS DE ESTA SECCION SALEN DE `docs/loop/SALIDA_V190_APERTURA.txt`**, que
se escribio **antes de la primera operacion**, y no de lo que yo recuerde.

- El arbol abrio con **`git status --porcelain`** en **1** linea, y es
  **`?? scripts/loop/vuelta190_apertura.py`**: **el propio bloque de apertura**,
  todavia sin seguir por git cuando su bloque C corrio. **`CIFRA ficheros no
  seguidos: 1`**, ese mismo, con **28607 bytes en disco y 28607 normalizado a LF**.
- **`git diff --numstat -- dataset/` AL ENTRAR: 0 filas.** **AL SALIR: 0 filas**,
  medido por el paso 4 del ciclo del bloque de cierre. **Las dos cifras se
  publican.**
- **HEAD real de apertura: `b393347f`**, sellado en
  `docs/loop/SALIDA_V190_HEAD_APERTURA.txt` **antes de la primera operacion**.
  **HEAD de cierre: `581330e4`**, leido de `git rev-parse HEAD` **despues de la
  ultima operacion**.
- **EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA**, dentro de su bloque y
  **antes de la primera operacion**: **4 filas**, las mismas que al cierre. Una
  columna de apertura medida al cierre es caida que acumula, y por eso se midio
  donde toca.
- **EL SELLO DEL AUDITOR, MEDIDO Y NO CREIDO:**
  `docs/loop/SELLO_APERTURA_AUDITOR_V190.json` mide **765 bytes en disco y 765 normalizado a LF**, su ciega **41948 en disco y 41948 normalizado a LF** y su destape **37856 en disco y 37856 normalizado a LF**,
  los tres **CALZA** contra lo que el propio sello declara. **411 puestos
  excluidos**, con **solape 0** contra la ciega del acta 190.

## 5. LAS CORRECCIONES DECLARADAS DE ESTA VUELTA

**`5.1` LA CIFRA DE MI PROPIO BLOQUE H.7 ES CIERTA Y ENGANA, Y NO SE BORRA.** El
sello de apertura publica **`CIFRA fichas con id OP-L-02: 0`** sobre las 71 fichas
de `docs/plan/OPERACIONES.jsonl`. **Busque por las claves `id` y `operacion`, y la
clave en ese fichero es `id_op`.** La ficha existe y vive en la **linea 42**. **El
texto viejo queda entero donde esta**, ya commiteado en `70d5662c`, y esta
correccion va al lado.

**`5.2` MI PROPIO ARNES DE LA TAREA 2 ESCRIBIA UNA SALIDA QUE CAMBIABA SOLA, Y ME
LO CAZO LA DOBLE CORRIDA.** `docs/loop/SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt` salia con **el mismo
tamano por las dos convenciones y tres `sha256` distintos** (`4678b6db...`,
`15fc1632...`, `5c00bdde...`) en tres corridas. **La causa, medida:** el arnes
imprimia la ruta de su temporal y `tempfile.mkdtemp` le pone un sufijo al azar.
**Corregido publicando el prefijo estable en vez de la ruta**, y **remedido**:
las dos corridas dan el mismo **`sha256` `bc1f0f27849ffced` por las dos convenciones, en disco y normalizado a LF**, y el tamano de hoy va en la tabla de la seccion 2.

**`5.3` TECLEE DOS CIFRAS EN MI PROPIO ARNES DE LA TAREA 3 Y LAS DOS CAYERON.** En
su bloque F escribi **22 y 20** bytes esperados de un fichero fabricado, y son
**23 y 21**. **La correccion no fue meter la cifra buena**, que se puede volver a
equivocar: el esperado pasa a ser **una RELACION medida sobre el propio fichero**
(`bytes del corte = bytes en disco menos los retornos de carro`). **Es la misma
especie que esta casa persigue desde la vuelta 74, y me mordio dentro del arnes
que escribi para cazarla.**

**`5.4` LA `4.9` APLICADA A MANO ANTES DE TENERLA EN CODIGO.** Re correr
`vuelta179_tarea4_juzgar_sujeto.py`, uno de los tres arneses viejos que usan la
guarda que toque, **piso una salida sellada de la vuelta 179**:
`docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl` paso de **17 filas a 3**. **El corte
nuevo se escribio al lado con su nombre y su vuelta**
(`docs/plan/SUJETO_CONGELADO_VEREDICTOS_V190.jsonl`, **4356 bytes en disco y 4356 normalizado a LF**, **3 filas**) **y el original se restauro y se remidio**: **20956 bytes en disco y 20939 normalizado a LF, 17 filas**. **El corte nuevo
interesa y por eso se conserva:** dice que la deuda de aquella vuelta bajo de 17 a
3.

## 6. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Las cinco tareas salen de regla escrita o de adjudicacion
citable, y las decisiones que tome dentro de ellas van marcadas como discutibles
en la seccion 8, que es su sitio, y no como doctrina.

## 7. LAS PREGUNTAS QUE TRAIGO

**`P.1` A `OP-L-02` LE FALTA UN DOCUMENTO O SOLO LE FALTA QUE SU `evidencia`
NOMBRE LOS QUE YA EXISTEN.** Medido: las tres nominas **si** tienen sede, su
cobertura **esta medida** desde la 169 con **6 de 6 completas**, y
`docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt` **lleva el nombre de la ficha** y
mide justo lo que su `verificacion` pide. Pero vive en `docs/loop/`, que es donde
van las salidas de una vuelta, **y no en `docs/plan/`, que es donde vive el
producto de una mesa**. **Son dos deudas muy distintas y la segunda es barata. No
elijo entre las dos:** decidir que una salida de vuelta cuenta como producto de
mesa **cambia el alcance de la campana**, y eso lo reserva el fundador.

**`P.2` LA DISCREPANCIA DEL 3182 CAE FUERA DE MIS DUDOSOS Y BAJA EL CREDITO DE MI
TANDA.** `AUDITOR.md` 1.2 dice que ese tramo **se relee al doble**. **Yo no me lo
auto encargo**: el encargo de esta vuelta trae cinco tareas y ese es el tope, y
quien encarga las relecturas al doble es el auditor. **Lo traigo medido, con su
nombre y su cifra, para que la 191 lo encuentre escrito.**

**`P.3` SI EL EXITCODE 2 DEBE PROPAGARSE TAMBIEN A `--componer`.** Esta vuelta lo
puso en el **tramo** y en el **codigo de salida del lanzador**, que es lo que la
`4.4` nombra. **No toque `--componer`**, que compone la salida unica de los tramos
ya sellados: si la casa quiere que la composicion tambien diga la especie del
rojo, es una linea mas y **no la escribo sin que se me pida**.

## 8. LAS CAIDAS PROPIAS DE ESTA VUELTA, LO QUE QUEDA EN ROJO, Y LOS DISCUTIBLES

**CAIDAS PROPIAS: TRES, Y LAS TRES ESTAN EN LA SECCION 5 CON SU CIFRA.** La `5.1`
(la cifra de mi bloque H.7, cierta y enganosa), la `5.2` (mi arnes con salida que
cambiaba sola) y la `5.3` (dos cifras tecleadas en mi propio arnes). **LAS TRES SON
DE METODO**, las tres las cace **antes de publicar ninguna cifra falsa en este
reporte**, y **ninguna es caida de reporte**. **No acumulan.**

**LO QUE QUEDA EN ROJO, Y SE TRAE SIN APAGARLO:** el veredicto de la TAREA 2 cierra
en **`ROJO POR DEUDA DECLARADA`, exitcode 2**, con **3 entradas de la nomina cuyo
sujeto no esta congelado**. **Sigue siendo rojo**, y lo unico que esta vuelta anade
es que el rojo dice de que especie es. **No se aflojo ninguna guarda para
conseguirlo.**

**LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO:**

**`D.1` (DE METODO). AMPLIAR `guarda_del_sujeto_congelado()` POR UNA FUNCION
HERMANA EN VEZ DE CAMBIARLE LA FIRMA.** El encargo dice que la guarda *"SEPARA EN
SU SALIDA"*. Yo deje `guarda_del_sujeto_congelado()` **intacta** (sigue devolviendo
tuplas de 3 campos, que es lo que llaman los tres arneses viejos) y meti la
separacion en `guarda_del_sujeto_congelado_separada()`, que es la que **publica las
dos cifras en la salida** del informe y del instrumento de la nomina.
**Discutible:** cabe leer el encargo como que la firma de la funcion original tenia
que cambiar.

**`D.2` (DE METODO). LA VARA DEL `MOTIVO ESCRITO` LA ESCRIBI YO, PORQUE EL ENCARGO
NO LA DA.** Siete marcas literales de la casa, ventana de mas o menos 3 lineas
sobre la maquina, y la regla del lado seguro. **La escribi ANTES de medir y la
publique en la simulacion previa**, para que no se pudiera ajustar a lo que
conviniera. **Discutible:** otra vara razonable daria otra cifra, y con las tres
entradas de hoy **una vara mas estrecha las sacaria SIN MOTIVO**.

**`D.3` (DE METODO). EL EXITCODE DE LA DEUDA ES `2` Y NO OTRO NUMERO.** Escogi 2
porque deja el 1 donde estaba (el fallo) y **los dos siguen siendo distintos de
cero**. **Discutible:** un `3` o un `10` servirian igual, y el 2 no sale de ninguna
regla escrita.

**`D.4` (DE METODO). `SUJETO VIVO` CUENTA COMO FALLO Y NO COMO DEUDA.** Un arnes
que abre el fichero de hoy sin nada que lo module **no mide su maquina, mide el
dia**, y eso me parece guarda rota y no deuda declarable. **Discutible:** hoy esa
lista esta en **0**, asi que la decision **no cambia ninguna cifra de esta vuelta**
y aun asi decide como se leeran las de las proximas.

**`D.5` (DE METODO). LA TAREA 4 NO SE AUTO ENCARGA SU PROPIA RELECTURA AL DOBLE.**
La discrepancia del 3182 cae fuera de mis dudosos y `AUDITOR.md` 1.2 manda releer
ese tramo al doble. **La traigo como pregunta en vez de ejecutarla**, porque cinco
es el tope de esta vuelta y quien encarga es el auditor. **Discutible:** cabe
sostener que la regla se cumple sola y que debi releerla aqui.

**`D.6` (DE METODO). NO LE DI SEDE A `OP-L-02` PUDIENDO ARGUMENTARLO.**
`SALIDA_V169_T5_COBERTURA_OP_L_02.txt` lleva su nombre, mide sus nominas y existe
con bytes: **se podria sostener que ES su producto documental**. **No lo declaro
yo** porque eso cambia el alcance de la campana. **Discutible:** cabe sostener que
la busqueda ya encontro la sede y que negarla es quedarse corto.

**NINGUNO ES DE CLASE.** Esta vuelta **no decidio ni una clase** y no movio ni un
veredicto: el archivo abre y cierra en el mismo `sha256`.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 190 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V190_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: por AUDITOR.md 6.1, decision del fundador del 5 sep 2026, la bateria de mutaciones corre CADA CINCO VUELTAS en una vuelta propia que no lleva nada mas. La 189 la corrio ENTERA: sus diez tramos siguen sellados en disco y el bloque H.5 del sello de apertura de esta vuelta los remidio uno a uno, por las dos convenciones, en disco y normalizado a LF, antes de tocar nada. Por esa cadencia LA SIGUIENTE VUELTA DE BATERIA ES LA 194, y esta vuelta NO es de bateria: su encargo se lo dice con esas palabras. Lo que esta vuelta SI hizo sobre la bateria es arreglar su lanzador en la TAREA 3, sin correr ni un tramo: --plan y --siguiente son las dos unicas ordenes suyas que se invocaron y ninguna sella salida de tramo ni corre ningun arnes. La nomina cierra en 127 entradas, arneses_que_faltan() en 0, o sea que la 194 la encontrara completa.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
