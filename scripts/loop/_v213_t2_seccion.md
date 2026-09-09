### `2.a` EL INVENTARIO DE CIERRE DE LA FASE III, DE LAS 71 FICHAS, LEIDO DEL REPO

**POR QUE ESTA TAREA Y NO OTRA, Y ES UNA CIFRA MIA Y NO HEREDADA.** Corri `scripts/loop/vuelta150_3_relectura_expediente.py` **en esta vuelta**, con el reloj de git congelado en mi HEAD de apertura, y su salida cruda vive en `docs/loop/SALIDA_V213_T2_VARA.txt`. Su cabecera dice, leida de ahi: *RELOJ DE GIT CONGELADO EN --corte 7be7476e (7be7476e). RANGO PROPIO DE LA VUELTA: 7be7476e..HEAD (7be7476e)*. **El plan esta agotado**, y lo que queda es el cierre.

**LA FUENTE ES LA VARA, NUNCA EL CAMPO** (recuadro 0 de `AUDITOR.md`). La columna `estado` va publicada **al lado y etiquetada como HISTORICA en la propia cabecera de la tabla**, y donde los dos discrepan **lo digo y no lo resuelvo**.

#### 1. COMO SE COMPUSO LA TABLA, Y LA GUARDA QUE LA SOSTIENE

**LA VARA IMPRIME SOLO LAS QUE NO CALZAN, Y EL ENCARGO PIDE LAS 71.** Su propia salida lo dice: *TABLA DE LAS QUE NO CALZAN (40 de 71). Las 31 que calzan NO se imprimen.*. Las 31 que calzan **no existen en ningun fichero de salida**, asi que no se pueden pegar de ninguno. **No reimplemente la vara: la IMPORTE** y llame a sus propias funciones con el mismo corte, que es lo que hace `scripts/loop/_v213_t2_cierre_fase_iii.py`.

**Y LA GUARDA QUE PRUEBA QUE MI COMPUTO ES EL SUYO:** para las filas que la vara **SI** imprime, mi celda de pruebas se coteja contra la suya fila a fila.

**LO QUE SOSTIENE LA TABLA.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 5; FILAS QUE DEBERIA HABER: 5.**

| que se comprobo | lo que dice el instrumento |
|---|---|
| filas que la vara imprime en su tabla de las que no calzan | 40 |
| filas cotejadas contra las mias, y cuantas difieren | CIFRA filas cotejadas: 40 \| CIFRA que DIFIEREN: 0 (se exigen 0) |
| fichas contadas de `docs/plan/OPERACIONES.jsonl` | 71 |
| `id_op` distintos (que no haya dos con el mismo nombre) | 71 |
| **el `sha256` de `docs/plan/OPERACIONES.jsonl` al entrar y al salir** | **SI, QUIETO como se exige** |

**LA GUARDA SE ME CAYO EN SU PRIMERA CORRIDA Y LO DIGO**: cote las filas del fichero entero y me trague **tres filas de OTRAS DOS TABLAS** de la misma salida (la de las desbloqueadas y la de la vara documental), que tambien empiezan por el mismo prefijo y llevan las columnas en otro sitio. **Salieron 43 filas y 3 diferencias.** Acote la lectura a la tabla que toca y las diferencias cayeron a **0** sobre **40**. **Una guarda que solo se ve pasar no prueba nada; esta mordio.**

#### 2. LA TABLA, UNA FILA POR FICHA, LAS 71 Y SIN CORTAR

**LA TABLA ENTERA, PEGADA DE `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt` Y NO TECLEADA.** **FILAS ARMADAS LEYENDO ESE FICHERO: 71; FILAS QUE DEBERIA HABER: 71.** El propio fichero lo vuelve a decir con sus dos cifras juntas: *CIFRA filas de la tabla: 71 | CIFRA fichas que deberia haber: 71*.

| id_op | fase | tipo | estado HISTORICO (contraste) | pruebas que dan positivo, de la vara de esta vuelta | veredicto del repo | calza el campo con el repo |
|---|---|---|---|---|---|---|
| `OP-F-01` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-F-02` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-F-03` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-D-01` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-D-02` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P1+P2+P3a | EJECUTADA | NO |
| `OP-D-03` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P3a | EJECUTADA | NO |
| `OP-D-04` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-D-05` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P1+P3a | EJECUTADA | NO |
| `OP-D-06` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P3a | EJECUTADA | NO |
| `OP-S-01` | 05_SANEO | FUSION | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-S-02` | 05_SANEO | VIGENCIA | HECHA | P3a | EJECUTADA | SI |
| `OP-S-03` | 05_SANEO | VIGENCIA | HECHA | P3a | EJECUTADA | SI |
| `OP-S-04` | 05_SANEO | HERRAMIENTA | HECHA | P3a | EJECUTADA | SI |
| `OP-S-05` | 05_SANEO | HERRAMIENTA | HECHA | P3a | EJECUTADA | SI |
| `OP-S-06` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-S-08` | 05_SANEO | CAMPO_SUCIO | HECHA | P2 | EJECUTADA | SI |
| `OP-S-07` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-S-09` | 05_SANEO | RENOMBRE_CON_ALIAS | HECHA | P3a | EJECUTADA | SI |
| `OP-S-10` | 05_SANEO | REENCUADRE_DE_MARCO | HECHA | P3a | EJECUTADA | SI |
| `OP-C-01` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-C-02` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-C-03` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-C-04` | 00_CODIGO | CAMPO_SUCIO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-U-01` | 03_FUSIONES | FUSION | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-E-01` | 04_ENLACES | ENLACE | LISTA | P3a | EJECUTADA | NO |
| `OP-E-02` | 04_ENLACES | ENLACE | HECHA | P3a | EJECUTADA | SI |
| `OP-M-01` | 06_MESAS | MESA ADJUDICADA: LAS DOS MITADES QUEDAN, CON FRONTERA ADOPTADA | HECHA | P3a | EJECUTADA | SI |
| `OP-M-02` | 06_MESAS | MESA ADJUDICADA: SERIE DECLARADA | HECHA | P3a | EJECUTADA | SI |
| `OP-M-03` | 06_MESAS | MESA ADJUDICADA: DOS PUERTAS MAS UN ACTO | HECHA | P3a | EJECUTADA | SI |
| `OP-M-04` | 06_MESAS | MESA ADJUDICADA: DOS FUSIONES MAS UN ENLACE | HECHA | P3a | EJECUTADA | SI |
| `OP-M-05` | 06_MESAS | MESA ADJUDICADA: DOS ETAPAS, CON FRONTERA REGISTRADA | HECHA | P3a | EJECUTADA | SI |
| `OP-A-01` | 07_ADUANA | FRONTERA_DECLARADA | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-A-02` | 07_ADUANA | MESA | LISTA | P2+P3a+documental | EJECUTADA | NO |
| `OP-V-01` | 08_VERIFICACION | MESA | HECHA | documental | SIN EJECUTAR | NO |
| `OP-U-02` | 03_FUSIONES | FUSION | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-S-11` | 05_SANEO | CAMPO_SUCIO | HECHA | P2+P3a+P3b | EJECUTADA | SI |
| `OP-F-04-COL` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-F-04-HOR` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-F-04-WEI` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-F-04-RAC` | 01_FUENTES | DECISION_DE_FUENTE | LISTA | P3a | EJECUTADA | NO |
| `OP-L-01` | 09_LECTURAS_DIRIGIDAS | MESA | HECHA | documental | SIN EJECUTAR | NO |
| `OP-L-02` | 09_LECTURAS_DIRIGIDAS | MESA | HECHA | ninguna | SIN EJECUTAR | NO |
| `OP-L-03` | 09_LECTURAS_DIRIGIDAS | MESA | HECHA | documental | SIN EJECUTAR | NO |
| `OP-I-01` | 10_INVENTARIO | MESA | LISTA | documental | SIN EJECUTAR | SI |
| `OP-E-03` | 04_ENLACES | LECTURA DIRIGIDA | LISTA | P3b | EJECUTADA | NO |
| `OP-S-12` | 05_SANEO | SANEO MECANICO | HECHA | P2+P3a | EJECUTADA | SI |
| `OP-C-05` | 00_CODIGO | GUARDA | HECHA | P2+P3a+P3b | EJECUTADA | SI |
| `OP-M-02-PROG` | 03_FUSIONES | FUSION DE MESA | LISTA | P1+P3a | EJECUTADA | NO |
| `OP-M-02-MEDIOS` | 03_FUSIONES | FUSION DE MESA | LISTA | ninguna | CONSUMIDA por OP-U-01 | SI |
| `OP-M-02-ASSESS` | 03_FUSIONES | FUSION DE MESA | LISTA | P1 | EJECUTADA | NO |
| `OP-M-02-ADMIT` | 03_FUSIONES | FUSION DE MESA | LISTA | ninguna | CONSUMIDA por OP-U-01 | SI |
| `OP-M-02-ACTIVATE` | 03_FUSIONES | FUSION DE MESA | LISTA | P1 | EJECUTADA | NO |
| `OP-M-02-ACCLIMATE` | 03_FUSIONES | FUSION DE MESA | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-02-ACCOMPLISH` | 03_FUSIONES | FUSION DE MESA | LISTA | P1 | EJECUTADA | NO |
| `OP-D-07` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P2+P3a | EJECUTADA | NO |
| `OP-M-03-I` | 03_FUSIONES | FUSION DE MESA | LISTA | P1+P3a | EJECUTADA | NO |
| `OP-M-03-II` | 03_FUSIONES | FUSION DE MESA | LISTA | P1+P3a | EJECUTADA | NO |
| `OP-M-03-III` | 03_FUSIONES | FUSION DE MESA | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-03-ENLACES` | 04_ENLACES | ENLACE | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-01-FUSION` | 03_FUSIONES | FUSION DE MESA: LA CAMARILLA DE CINCO | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-E-04` | 04_ENLACES | ENLACE | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-E-05` | 04_ENLACES | ENLACE MUTUO | HECHA | P1+P2+P3a | EJECUTADA | SI |
| `OP-M-01-ESLABONES` | 04_ENLACES | ENLACE | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-05-INDICE` | 03_FUSIONES | FUSION DE MESA | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-05-EDIFICIO` | 03_FUSIONES | FUSION DE MESA | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-05-APERTURA` | 03_FUSIONES | FUSION DE MESA | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-M-01-SEXTO` | 04_ENLACES | ENLACE MAS PODA DEL SOLAPE | HECHA | P1+P3a | EJECUTADA | SI |
| `OP-E-06` | 04_ENLACES | ENLACE CON EVIDENCIA DE LECTURA | LISTA | P3a | EJECUTADA | NO |
| `OP-E-07` | 04_ENLACES | LECTURA DIRIGIDA CORTA | LISTA | P3a+P3b | EJECUTADA | NO |
| `OP-D-08` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P3a | EJECUTADA | NO |
| `OP-D-09` | 02_DESTEJIDOS | DESTEJIDO | LISTA | P3a | EJECUTADA | NO |

**LA COLUMNA `documental` NO ASCIENDE A NADIE, Y SE DICE:** la vara documental es la cuarta prueba y **solo aplica a las fichas de tipo `MESA`**; el propio instrumento la publica **al lado** y no la funde con las otras tres. Yo hago lo mismo: una ficha cuyo unico positivo sea `documental` **sigue saliendo SIN EJECUTAR** en la columna del veredicto. **`OP-I-01` es exactamente ese caso**, y por eso aparece con `documental` y con `SIN EJECUTAR` a la vez.

#### 3. LAS CUATRO CIFRAS, CADA UNA CONTADA DE LA TABLA

**LAS CUATRO CIFRAS.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 5; FILAS QUE DEBERIA HABER: 5** (las cuatro que el encargo pide mas la suma que las cuadra).

| cifra | lo que dice el instrumento |
|---|---|
| **1. cuantas de las 71 tienen PRUEBA DE EJECUCION en el repo** | **64** |
| **2. cuantas estan CONSUMIDAS, y por quien** | **2**, y las dos son `OP-M-02-MEDIOS` y `OP-M-02-ADMIT`, **las dos por `OP-U-01`** |
| **3. cuantas estan SIN EJECUTAR** | **5** |
| **4. cuantas tienen el campo `estado` en desacuerdo con el repo** | **40**, que se parten en **4** por un lado y **36** por el otro |
| la suma, comprobada contra las 71 | LA SUMA SE COMPRUEBA: 64 con prueba + 2 consumidas + 5 sin ejecutar = 71, y las fichas son 71 |

**LA LISTA ENTERA DE LAS SIN EJECUTAR, QUE EL ENCARGO PIDE ENTERA:**

**LAS SIN EJECUTAR, UNA A UNA.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 5; FILAS QUE DEBERIA HABER: 5.**

| la fila, tal como sale del instrumento |
|---|
| SIN EJECUTAR: OP-V-01                fase 08_VERIFICACION, tipo MESA, estado historico HECHA |
| SIN EJECUTAR: OP-L-01                fase 09_LECTURAS_DIRIGIDAS, tipo MESA, estado historico HECHA |
| SIN EJECUTAR: OP-L-02                fase 09_LECTURAS_DIRIGIDAS, tipo MESA, estado historico HECHA |
| SIN EJECUTAR: OP-L-03                fase 09_LECTURAS_DIRIGIDAS, tipo MESA, estado historico HECHA |
| SIN EJECUTAR: OP-I-01                fase 10_INVENTARIO, tipo MESA, estado historico LISTA |

**AQUI DISCREPO DE LA CIFRA QUE EL ENCARGO CITA, Y LA DECLARO EN VEZ DE RESOLVERLA COPIANDO** (`EJECUTOR.md` 2). El encargo dice que la vara mide **3** en `LISTA` sin ninguna prueba. **Eso reproduce exacto** y esta en su propia salida: *CONTADO: 3 ficha(s) en LISTA sin ninguna prueba de ejecucion.*. **Mi cifra 3 no es esa y no mide lo mismo:** la vara cuenta las que estan **en `LISTA`** sin prueba, y la columna que el encargo me manda escribir es **el veredicto del REPO, que no mira el campo**. Por eso a mis SIN EJECUTAR se suman las **cuatro** que el campo declara `HECHA` y el repo no sostiene (`OP-V-01`, `OP-L-01`, `OP-L-02` y `OP-L-03`), menos las **dos** consumidas, que salen a su propia cifra. **Las dos cuentas son ciertas y miden cosas distintas, y por eso van las dos escritas.**

**Y LA CAUTELA DE LA CUARTA VA PEGADA A ELLA, NO SUELTA** (adjudicacion `6.8` del acta 211): **si cada ficha va poniendo su campo al dia, esa cifra tiende a cero sin que se haya ejecutado nada mas.** Mide **cuanto miente el campo**, no cuanto trabajo queda. **El trabajo que queda es la tercera.**

#### 4. LAS CINCO PROHIBICIONES DE LA TAREA 2, UNA A UNA

**LAS CINCO PROHIBICIONES.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 5; FILAS QUE DEBERIA HABER: 5.**

| que estaba prohibido | que paso |
|---|---|
| **1.** no cambiar el campo `estado` de ninguna ficha | **CUMPLIDA Y PROBADA CON EL `sha256`.** CIFRA sede docs/plan/OPERACIONES.jsonl AL ENTRAR: 514452 bytes, sha256 disco ca1d95b5b3d19e9e, sha256 LF ca1d95b5b3d19e9e y al salir 514452 bytes, sha256 disco ca1d95b5b3d19e9e, sha256 LF ca1d95b5b3d19e9e |
| **2.** no marcar las entradas del inventario | **CUMPLIDA.** El instrumento **abre `docs/plan/INVENTARIO.jsonl` solo para leer**, su `numstat` mide **0** filas, y su recuento no escribe: las incompletas siguen siendo **95** y las marcadas **0** |
| **3.** no escribir ni una fila nueva en `docs/plan/08_VERIFICACION.md` | **CUMPLIDA.** Ese fichero no se abre para escritura en ningun camino de esta tarea, y su `numstat` al cerrar la tarea, sellado en `docs/loop/SALIDA_V213_T2_NUMSTAT.txt`, mide **0** filas |
| **4.** no declarar la campaña consumada ni escribir `PARA_ALEXIS.md` | **CUMPLIDA.** CIFRA PARA_ALEXIS.md existe en el arbol: NO, y esta tarea no lo crea. **No lo esta:** `OP-I-01` sigue abierta y lo que necesita es del fundador |
| **5.** no tocar el grafo | **CUMPLIDA.** El ciclo de Gate 0 mide `git diff HEAD --numstat` en **0** filas en los dos lados |

### `2.b` LA UNICA QUE QUEDA ABIERTA: `OP-I-01`, ESCRITA PARA QUE SE PUEDA DECIDIR

**LO QUE LA FICHA ESCRIBE Y LO QUE NO, DICHO ANTES DE LA TABLA Y NO DESPUES.** La ficha escribe **los cuatro puntos**; **no escribe su estado**. `CUBRE`, `A MEDIAS` y `NO CUBRE` son **veredictos MEDIDOS**, no campos de la ficha: salen de `docs/loop/SALIDA_V211_T2_OP_I_01.txt` y los ratifico el acta 211 en su `6.3` (linea **74595**, leida hoy: ***`6.3` `OP-I-01` NO SE CIERRA, Y AHORA CON EL CRITERIO PUESTO.** Aplicado el criterio*). **No los invento aqui y no se los atribuyo a la ficha.**

**LOS CUATRO PUNTOS DE `verificacion`, PEGADOS ENTEROS DEL FICHERO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 4; FILAS QUE DEBERIA HABER: 4.**

| punto | el texto, pegado entero de la ficha | estado MEDIDO (no es campo de la ficha) |
|---|---|---|
| **1** | toda entrada lleva su fecha_corte | **CUBRE** |
| **2** | toda forma con cobertura incompleta va marcada PROVISIONAL | **NO CUBRE** |
| **3** | todo hueco va NOMBRADO, nunca rellenado | **A MEDIAS** |
| **4** | el inventario se recomputa entero con el disparador de 08_VERIFICACION | **A MEDIAS** |

**EL PUNTO QUE ESTA EN `NO CUBRE`, APARTE Y ENTERO:** PUNTO 2: toda forma con cobertura incompleta va marcada PROVISIONAL

**QUE HARIA FALTA EXACTAMENTE PARA QUE DEJARA DE ESTARLO.** La `6.4` del acta 211 lo deja escrito y lo cito con sus lineas, leidas hoy:

**LAS TRES LINEAS DE LA `6.4`.** **FILAS ARMADAS LEYENDO `docs/loop/ACTA_AUDITOR.md`: 3; FILAS QUE DEBERIA HABER: 3.**

| linea | lo que dice, leido hoy |
|---|---|
| **74601** | **`6.4` LA `D.3` SE ADJUDICA Y EL `NO CUBRE` SE SOSTIENE.** El banco `9.26`, verbatim: |
| **74606** | dice que la forma sea provisional.** **95 formas incompletas y 0 que lo digan: NO CUBRE.** |
| **74607** | **Marcar las 95 es una edicion de datos de docs/plan/ que ninguna regla ordena hoy**, y |

**EN UNA FRASE, Y SALE DE ESAS TRES LINEAS: no hace falta COMPLETAR la cobertura, hace falta MARCARLA.** El banco `9.26` admite una cobertura incompleta como cumplimiento **si se dice asi**, y hoy ninguna lo dice.

**EL RECUENTO, HECHO POR MI EN ESTA VUELTA Y NO COPIADO.** El comando esta escrito entero en `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt` y su corrida suelta quedo sellada en `docs/loop/SALIDA_V213_T2_RECUENTO_95.txt`, que dice: *entradas 672 | con forma N de M 555 | INCOMPLETAS 95*.

**EL RECUENTO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`: 5; FILAS QUE DEBERIA HABER: 5.**

| que se conto | cifra de hoy |
|---|---|
| entradas del inventario | 672 |
| de esas, con cobertura de la forma *N de M pares leidos* | 555 |
| **de esas, INCOMPLETAS (`N` menor que `M`)** | **95** |
| de esas incompletas, cuantas llevan `PROVISIONAL` en algun campo | 0 |
| entradas del inventario entero que llevan `PROVISIONAL` | 3 |

**CONTRA LA CIFRA VIEJA, Y LO DIGO AUNQUE COINCIDA.** El acta 211 publica su cifra en la `6.4`, linea **74606**, leida hoy: *dice que la forma sea provisional.** **95 formas incompletas y 0 que lo digan: NO CUBRE.***. Y mi conteo de hoy, del fichero y no del acta: **95, o sea que REPRODUCE al digito.**

**QUE DECIDE EL FUNDADOR Y QUE NO, EN UNA LINEA:** marcar esas **95** entradas es **edicion de datos de `docs/plan/OPERACIONES.jsonl` y sus vecinos que ninguna regla ordena hoy**, y las filas que faltan en `docs/plan/08_VERIFICACION.md` para las fases 09 y 10 **cambian la forma del plan**: **las dos son suyas y ninguna es del bucle.**

**DOS DISCUTIBLES MARCADOS, LOS DOS ANTES DE SABER SI ACIERTO.**

1. **EL VEREDICTO `CONSUMIDA` LO DECIDE EL GRAFO Y LA ATRIBUCION LA FICHA, Y LAS DOS VAN EN LA MISMA CELDA.** Uso `consumida_por()` de la vara tal cual, que resuelve los nodos por `P.1` y exige que caigan en **un solo nodo vivo**; el **por quien** sale del texto de la propia ficha. **Si la casa quisiera esas dos cosas en dos columnas separadas, esta tabla las tiene juntas.** DISCUTIBLE MARCADO.
2. **PUBLICO LOS CUATRO ESTADOS DE `OP-I-01` DE UNA MEDICION DE LA VUELTA 211 Y NO DE UNA MIA DE HOY.** El unico que el encargo me manda recontar es el del punto 2, y ese lo recompute yo (**95**, reproduce). Los otros tres los cito de su fichero con su atribucion en vez de re correrlos, porque el encargo no lo pide y la moratoria manda plan antes que volumen. **Si la vara buena era volver a medir los cuatro hoy, esto es una cita donde tenia que haber una medicion.** DISCUTIBLE MARCADO.

