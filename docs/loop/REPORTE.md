# REPORTE DE LA VUELTA 212 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v212_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO EN LA 209, LA 210 Y
> LA 211.** No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es
> el instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **DOS TAREAS, Y LA 212 NO ES VUELTA DE BATERIA.** La cadencia de cinco de
> `AUDITOR.md` 6.1 pone la siguiente bateria en la **215**, y esta vuelta no la
> corre. El encargo trae dos sub-tareas porque el trabajo que queda cabe en dos,
> aunque el tope de cinco ya este disponible.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo. Todo lo que esta vuelta escribe son ficheros `_v212_*` **con
> prefijo de guion bajo, fuera del censo y fuera de la nomina**. La nomina sigue
> **CONGELADA EN 135** y no se poda.
>
> **RIGE LA OBLIGACION DE DICTADO DEL `6.6` DEL ACTA 210:** toda cita de un acta
> anterior lleva **LA LINEA** de `docs/loop/ACTA_AUDITOR.md` donde vive el texto
> citado, **y la linea se LEE, no se recuerda**.
>
> **Y RIGE LA OBLIGACION NUEVA QUE EL ENCARGO ANADE, SIN CODIGO:** toda tabla que
> un compositor arme leyendo filas de una salida publica, EN LA MISMA LINEA,
> cuantas filas armo; y si al lado va una cifra de cuantas deberia haber, LAS DOS
> SE ESCRIBEN JUNTAS.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V212_APERTURA.txt`,
> `docs/loop/SALIDA_V212_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 212`, y su salida
cruda vive en `docs/loop/SALIDA_V212_TALLADOR_CABECERA.txt` (2597 bytes en disco y 2577 normalizado a LF, 11 filas de
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
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `ddeb676c` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 211: LAS DOS TAREAS ENTREGADAS Y TODA CIFRA REPRODUCE AL DIGITO SALVO UNA TABLA A LA QUE LE FALTA UNA FILA. La 2.e dice "3 de 3 sedes" y lista DOS, y la que se cae es la unica que decia NO COINCIDEN: lo causa un \\w+ en el compositor y lo pruebo corriendo los dos patrones. Caida de reporte que ACUMULA, racha 1 de 3.'), HEAD real de apertura `ddeb676c` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `e8d2c59f` (leido de `SALIDA_V212_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, LA RELECTURA CONJUNTA DEL PUESTO `730` Y LA `P.2`: leer el acta 212 del auditor desde su linea de apertura y citar por linea; VERIFICAR CONTRA EL GRAFO (no contra el acta) las aristas de `colaboracion_cadena_suministro` y recomputar las cinco cifras de cerco; APLICAR LA VARA del banco `9.6.1` con la direccion del `9.6.2` y la vara de LINEA o PROCEDIMIENTO del informe `67.6`; decidir con la vara y, si se confirma, correccion DECLARADA por el carril del banco `9.10` con el marcador RECOMPUTADO antes y despues; y la `P.2` de `OP-F-04-HOR`, correccion declarada sobre el campo `adjudicacion` citando `docs/plan/01_FUENTES.md` lineas 1168 y 1453, SIN tocar `nodos` ni `estado`. Y registrar sin ejecutarlas las CUATRO adjudicaciones que no piden trabajo | **CERRADA, LAS TRES MITADES** | `SALIDA_V212_T1B_PUESTO_730.txt`, `SALIDA_V212_T1B_ESCRIBIR.txt`, `SALIDA_V212_T1C_OP_F_04_HOR.txt`, `SALIDA_MARCADOR_AUDITOR_V212_T1B.json` |
| **TAREA 2** | LA COLA DE RELECTURA, CONDICIONADA: **solo se abre si la `1.b` CONFIRMA el cambio del 730**. Listar las CUATRO razones en `A` que nombran el cero-enlazados con su puesto, sus dos nodos y su razon entera; publicar para cada una DE QUE depende su clase citando la frase de su propia razon (silueta o contenido); las de contenido se quedan como estan y se dice; y si aparece alguna que dependa de la silueta, NO SE CAMBIA: se marca DISCUTIBLE y se trae | **CERRADA, Y SE ABRIO PORQUE LA 1.b CONFIRMO** | `SALIDA_V212_T2_COLA_RELECTURA.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### `1.a` LOS REGISTROS: EL ACTA 212 LEIDA DESDE SU LINEA, Y CADA CITA CON LA SUYA

El acta del auditor que cubre la vuelta 211 abre en la linea **74334** de `docs/loop/ACTA_AUDITOR.md`, que es donde el encargo dice que empieza, y de ahi la lei entera. **Rige la obligacion de dictado del `6.6` del acta 210** (linea **74203**): toda cita lleva LA LINEA, y la linea se LEE. Las de abajo estan leidas hoy con `sed -n` desde este compositor, no recordadas.

**LAS CITAS DE ACTA DE ESTE REPORTE, LEIDAS UNA A UNA DE SU LINEA.** **FILAS ARMADAS LEYENDO `docs/loop/ACTA_AUDITOR.md` linea a linea: 11; FILAS QUE DEBERIA HABER: 11.**

| linea de `ACTA_AUDITOR.md` | que es | el texto que vive ahi, leido hoy |
|---|---|---|
| **74334** | la apertura del acta que cubre la 211 | # ACTA DEL AUDITOR, VUELTA 211 (8 sep 2026, auditor Opus 5) |
| **74203** | la obligacion de dictado del `6.6` del acta 210, que sigue rigiendo | **`6.6` LA FAMILIA DE LA CITA MAL ATRIBUIDA GANA SU REMEDIO DE DICTADO, Y NO ES |
| **74641** | la `7.1`, que es el caso del 730 y el cuerpo de mi TAREA 1 | **`7.1` EL VEREDICTO DEL PUESTO 730 SE SOSTIENE SOBRE UNA LECTURA QUE SU PROPIA RAZON |
| **74644** | el verbatim que el acta cita de la razon del archivo | **LO QUE LA RAZON DEL ARCHIVO DICE DE SI MISMA, VERBATIM:** *"LA CLASE QUEDA EN A por la |
| **74651** | la ratificacion del banco `9.6.1` tal como el acta la cita | banco `9.6.1`, *EL CERO ENTRA EN LA REGLA*: *"CERO ENLAZADOS ES EL CASO EXTREMO DEL |
| **74584** | la `6.2`, el criterio de hecho de una ficha de fase 10 | **`6.2` LA `D.4` Y LA `P.1` SE CONTESTAN JUNTAS, Y NO ES PARADA: EL CRITERIO DE HECHO DE |
| **74595** | la `6.3`, `OP-I-01` no se cierra | **`6.3` `OP-I-01` NO SE CIERRA, Y AHORA CON EL CRITERIO PUESTO.** Aplicado el criterio |
| **74601** | la `6.4`, el `NO CUBRE` se sostiene | **`6.4` LA `D.3` SE ADJUDICA Y EL `NO CUBRE` SE SOSTIENE.** El banco `9.26`, verbatim: |
| **74610** | la `6.5`, el cubo cambia de nombre | **`6.5` LA `D.1` ESTA BIEN MARCADA Y EL NOMBRE SE CORRIGE SIN TOCAR LA MEDICION.** El |
| **74622** | la `6.7`, la `P.2`, que es lo que ejecuto en la `1.c` | **`6.7` LA `P.2` SE RESUELVE CON LA REGLA DE CORRECCION QUE YA EXISTE, Y SE ENCARGA.** El |
| **74690** | la `7.3`, la familia de patrones que solo ven lo que coincide | **`7.3` LA `4.1` NO ES UN DESCUIDO DE UN COMPOSITOR: ES UNA FAMILIA DE PATRON QUE SOLO VE |

### `1.b` EL PUESTO `730`: LO VERIFIQUE, LA VARA LO CONFIRMA, Y QUEDA CORREGIDO

**LO HICE EN EL ORDEN DEL ENCARGO Y NO EN OTRO.** Primero el grafo, despues la vara, despues la decision, y solo entonces la escritura. La medicion entera vive en `docs/loop/SALIDA_V212_T1B_PUESTO_730.txt` y la escritura en `docs/loop/SALIDA_V212_T1B_ESCRIBIR.txt`.

#### 1. CONTRA EL GRAFO, NO CONTRA EL ACTA

**LO QUE MIDIO EL GRAFO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T1B_PUESTO_730.txt`: 6; FILAS QUE DEBERIA HABER: 6.**

| que se midio | lo que dice el instrumento |
|---|---|
| nodos del grafo cargados / vivos | 3853 / 3169 |
| aristas de salida vivo-vivo de la madre, por las dos vistas y resueltas | LA TABLA DE ARISTAS DE SALIDA DE LA MADRE, ARMADA LEYENDO EL GRAFO: 1 fila(s) armada(s), y la cifra que la madre declara en sus nodos_siguientes es 1 |
| aristas de entrada vivo-vivo de la madre | LA TABLA DE ARISTAS DE ENTRADA DE LA MADRE: 1 fila(s) armada(s), y la cifra que la madre declara en sus nodos_previos es 1 |
| **hijos de paso que la madre ENLAZA** | **0 de 2** |
| la forma, mirada ANTES de contar (caveat de la familia encadenada) | NO HAY CADENA. Los hijos no cuelgan de la madre ni por cadena, asi que se cuentan los radios, y los radios son CERO |
| el caso rojo por mutacion del contador de silueta | EL CASO ROJO CAE COMO TIENE QUE CAER: sin mutar da 0 y mutado da 1 (se exige 0 y 1). |

**LA MADRE ENLAZA CERO DE SUS DOS HIJOS DE PASO, Y NO HAY CADENA QUE LA RESCATE.** Eso es lo que el encargo pedia publicar y es la mitad que decide: el caveat de la `9.6.1` manda mirar la forma antes de contar radios, y aqui ninguno de los dos hijos es alcanzable desde la madre ni a tres saltos. **El contador no es una constante y lo pruebo mutandolo**: metiendole a mano la arista a `efecto_bullwhip` sobre una copia en memoria, pasa de 0 a 1.

#### 2. EL CERCO, RECOMPUTADO POR MI, Y AQUI DISCREPO DEL ACTA EN DOS CIFRAS

**EL CERCO, PATRON POR PATRON, CON EL PATRON DICHO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T1B_PUESTO_730.txt`: 6; FILAS QUE DEBERIA HABER: 6.**

| lo que midio el instrumento |
|---|
| PATRON cero-enlazados, GUION LITERAL                    FILAS ARMADAS 11 (y la tabla de la linea de abajo lleva esas mismas 11); por clase A 3, D 8 |
| PATRON cero enlazados, HOLGADO (guion, espacio o nada)  FILAS ARMADAS 14 (y la tabla de la linea de abajo lleva esas mismas 14); por clase A 4, D 10 |
| PATRON choque de la seccion 19, FRASE ENTERA            FILAS ARMADAS 11 (y la tabla de la linea de abajo lleva esas mismas 11); por clase A 3, D 8 |
| PATRON seccion 19 A SECAS                               FILAS ARMADAS 13 (y la tabla de la linea de abajo lleva esas mismas 13); por clase A 3, D 10 |
| PATRON lectura vieja                                    FILAS ARMADAS  3 (y la tabla de la linea de abajo lleva esas mismas 3); por clase A 1, D 2 |
| PATRON seria D                                          FILAS ARMADAS  5 (y la tabla de la linea de abajo lleva esas mismas 5); por clase A 2, C 1, D 2 |

**LAS CINCO CIFRAS DEL ACTA, COTEJADAS UNA A UNA CON LAS MIAS.** El acta 211 publica **13**, **4**, **9**, **11** y **10** en su `7.1` (linea **74659** y siguientes). **TRES REPRODUCEN AL DIGITO Y DOS NO**, y lo digo en vez de copiarlas (`EJECUTOR.md` 2: si discrepan de la medicion de hoy, la discrepancia se declara).

**LAS CIFRAS DEL ACTA CONTRA LAS MIAS.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T1B_PUESTO_730.txt` contra la `7.1` del acta: 7; FILAS QUE DEBERIA HABER: 7.**

| lo que el acta publica | lo que mide mi instrumento | veredicto |
|---|---|---|
| **4** razones en `A` que nombran el cero-enlazados | 4, y son 474, 568, 586, 730 | **REPRODUCE** |
| **11** que nombran el choque de la seccion 19 | 11 | **REPRODUCE** con la frase entera como patron |
| **10** de esas once ya resueltas por la ratificacion | 10; y cuantas NO: 1 (730) | **REPRODUCE**, y la que sobra es el 730 |
| **13** razones que nombran el cero-enlazados | 11 con el guion literal y 14 con el patron holgado | **NO REPRODUCE con ningun patron.** Ni 11 ni 14 son 13 |
| **9** de esas trece en `D` | 8 con el guion literal y 10 con el patron holgado | **NO REPRODUCE**, y cae con la anterior: es la misma cifra por el otro lado |
| el 730 es **el UNICO** que dice *lectura vieja* | PATRON lectura vieja                                    FILAS ARMADAS  3 (y la tabla de la linea de abajo lleva esas mismas 3); por clase A 1, D 2 | **NO REPRODUCE: son TRES** (730, 2215 y 2371) |
| el 730 es **el UNICO** que dice *seria D* | PATRON seria D                                          FILAS ARMADAS  5 (y la tabla de la linea de abajo lleva esas mismas 5); por clase A 2, C 1, D 2 | **NO REPRODUCE: son CINCO**, aunque el 730 sigue siendo el unico que lo dice de si mismo |

**LO QUE ESTA DISCREPANCIA NO TUMBA, Y HAY QUE DECIRLO ENTERO:** las dos cifras que no reproducen son **de cerco**, no del par. La sustancia del caso del auditor vive en las tres que si reproducen (los CUATRO en `A`, los ONCE del choque, los DIEZ ya resueltos), y sobre todo en lo que mide el grafo. **Su lectura se sostiene y sus cuentas de cerco no**, y las dos cosas se escriben juntas. **Y las de *lectura vieja* y *seria D* fallan por la misma causa que su propia `7.3` nombra**: una cifra de unicidad que nadie conto contra el fichero.

#### 3. LA VARA, APLICADA POR MI, CON LOS DOS LADOS ESCRITOS

**QUE LE QUEDA A CADA NODO CUANDO LE QUITAS LO QUE DICE EL OTRO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T1B_PUESTO_730.txt`: 2; FILAS QUE DEBERIA HABER: 2.**

| lado | lo que mide el instrumento | que es |
|---|---|---|
| **lo que le queda al HIJO** (direccion del `9.6.2`, la unica que manda) | LE QUEDAN AL HIJO 5 de sus 6 pasos: los pasos 2, 3, 4, 5 y 6. | coste en produccion y programacion, coste en transporte y recepcion, inventario de seguridad y su coste, venta perdida por rotura, y la regla de decision que usa esos cuatro numeros |
| **lo que le queda a la MADRE** (el lado que no decide, escrito porque el encargo pide los dos) | LE QUEDAN A LA MADRE 3 de sus 5 pasos: los pasos 3, 4 y 5. | posicion en la cadena, acuerdos de intercambio de datos y POS, y el sistema barato de visibilidad compartida |

**POR EL `67.6`, LO QUE LE QUEDA AL HIJO ES PROCEDIMIENTO Y NO LINEA:** cuatro computos de coste sobre bases distintas, cada uno con decisiones dentro de si y repetido en el tiempo, mas una decision que se alimenta de los cuatro. **CONTINUA, o sea `D`.** Y por el lado que no decide, a la madre tambien le queda procedimiento: **procedimiento en los dos lados es par SANO por el `9.6.3`**, que es otra manera de llegar a que no es duplicacion. **LAS DOS DIRECCIONES DEVUELVEN LO MISMO.**

#### 4. LA DECISION, Y NO ES OBEDIENCIA

**CONFIRMO, Y LO CONFIRMO CON MI MEDICION, NO CON SU CASO.** La ratificacion del banco `9.6.1` (*EL CERO ENTRA EN LA REGLA*, 12 ago 2026) dice que sin ni un hermano enlazado la silueta no dice nada y manda el contenido; el grafo dice cero de dos y sin cadena; y el contenido dice procedimiento. **La `A` del 730 colgaba de la lectura que esa ratificacion jubilo, y su propia razon lo decia de si misma.** VEREDICTO DE ESTA MEDICION: la clase del 730 pasa de A a D. CONFIRMA: SI

#### 5. LA CORRECCION, POR EL CARRIL DEL BANCO `9.10`, Y SUS GUARDAS

**LAS GUARDAS DE LA `1.b`, TODAS DE SU FICHERO DE SALIDA.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T1B_ESCRIBIR.txt`: 11; FILAS QUE DEBERIA HABER: 11.**

| guarda | lo que dice el instrumento |
|---|---|
| filas del archivo al entrar / al salir | 3388 / 3388 (se exige 3388) |
| sede al entrar, por las dos convenciones | 4054129 bytes en disco y 4054129 normalizado a LF (COINCIDEN), sha256 disco 0a77b5a35a962621 y sha256 LF 0a77b5a35a962621 |
| sede al salir, por las dos convenciones | 4057130 bytes en disco y 4057130 normalizado a LF (COINCIDEN), sha256 disco 758edf1f5c313c18 y sha256 LF 758edf1f5c313c18 |
| el `sha256` cambia entre entrada y salida | SI (se exige SI) |
| **marcador AL ENTRAR**, recomputado con `apertura_del_auditor.marcador()` | **3388 filas; A 551, B 72, C 5, D 2760** |
| **marcador AL SALIR**, recomputado con el mismo instrumento | **3388 filas; A 550, B 72, C 5, D 2761** |
| el marcador del disco calza con el que la simulacion predijo | SI |
| la simulacion en memoria, antes de tocar el disco | 0 (se exige 0) |
| el texto viejo, entero y encima, byte a byte | el texto viejo esta ENTERO Y ENCIMA (la razon nueva empieza por la vieja, byte a byte): SI |
| campos que cambian en la fila | campos que cambian: clase, razon (se exigen exactamente clase y razon) |
| **el caso rojo por mutacion, corrido ANTES de escribir** | **4. CIFRA mutantes que CAEN en rojo: 4 (se exige que caigan todos)** |

**EL MARCADOR NO SE RESTO A MANO: SE RECOMPUTO CON SU INSTRUMENTO LAS DOS VECES**, y su salida esta sellada en `docs/loop/SALIDA_MARCADOR_AUDITOR_V212_T1B.json`. **LOS CUATRO MUTANTES CAEN LOS CUATRO**: la correccion que tapa el texto viejo, la que toca una segunda fila, la que escribe una clase que la vara no devuelve y la que mueve el campo `clave`. La guarda que dijo VERDE sobre lo correcto dice ROJO sobre las cuatro.

#### 6. EL BARRIDO DE TABLAS DERIVADAS, MEDIDO Y NO EJECUTADO

**DONDE VIVE CITADO EL 730 FUERA DEL ARCHIVO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T1B_PUESTO_730.txt`: 3; FILAS QUE DEBERIA HABER: 3.**

| la cita, tal como el instrumento la leyo |
|---|
| ocs/INTRA_DOMINIO_INFORME.md linea 6941 :: **El puesto 730** es el primer veredicto nuevo emitido **despues** de que el |
| ocs/plan/03_FUSIONES.md linea 5424 :: > puesto **730** declara que la clase queda en `A` **por la lectura vieja del cero-enlazados** y |
| ocs/loop/reportes/REPORTE_V179.md linea 311 :: | `colaboracion_cadena_suministro` vs `diagnostico_efecto_latigo` | **A** | 730 (`A`) y 329 (`A` |

**EL BANCO `9.10` DICE QUE TODO VOLTEO BARRE SUS TABLAS DERIVADAS EN EL MISMO ACTO, Y YO NO LAS BARRO. DIGO POR QUE Y LO MARCO COMO DISCUTIBLE.** Las tres citas **siguen siendo ciertas como relato**: las dos vivas dicen que el 730 *declara* que la clase queda en `A` por la lectura vieja, y eso es exactamente lo que la fila sigue diciendo, porque la correccion **dejo el texto viejo entero encima**. Lo que envejece no es la frase: es **la clase que el lector infiere**. Y editarlas es prosa sellada del informe y del plan, que es forma que este encargo no ordena y que el propio auditor reserva al fundador en su `6.2` para un caso hermano. **La tercera es un reporte archivado y esos no se tocan.** **Lo traigo entero para que se adjudique, con las tres lineas nombradas.**

### `1.c` LA `P.2`: LA ADJUDICACION DE `OP-F-04-HOR` QUEDA CORREGIDA

**LA CONTRADICCION, MEDIDA:** CIFRA el campo nodos de OP-F-04-HOR mide: 14 (contado del campo, no tecleado), y la propia `adjudicacion` decia *LEIDOS LOS 13* (si que la frase esta). **Los dos son ciertos en su fecha y ninguno se borra.**

**EL MOTIVO, LEIDO DEL DISCO EN SUS DOS LINEAS Y NO RECORDADO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T1C_OP_F_04_HOR.txt`: 2; FILAS QUE DEBERIA HABER: 2.**

| la linea, tal como el instrumento la leyo |
|---|
| docs/plan/01_FUENTES.md linea 1168 :: > **devolvio `principio_calidad_mvp` a la operacion y la nomina volvio a CATORCE**, porque la |
| docs/plan/01_FUENTES.md linea 1453 :: > 2026-08-11, adjudicacion *LEIDOS LOS 13*). **El que sobra es `principio_calidad_mvp`**: medido |

**LAS TRES GUARDAS DE LA `1.c`, MAS LAS DOS PROHIBICIONES EXPRESAS.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T1C_OP_F_04_HOR.txt`: 10; FILAS QUE DEBERIA HABER: 10.**

| guarda | lo que dice el instrumento |
|---|---|
| fichas del plan al entrar / al salir | 71 / 71 (se exige 71) |
| sede al entrar, por las dos convenciones | 513043 bytes en disco y 513043 normalizado a LF (COINCIDEN), sha256 disco 7a52387bb8a4aa4f y sha256 LF 7a52387bb8a4aa4f |
| sede al salir, por las dos convenciones | 514452 bytes en disco y 514452 normalizado a LF (COINCIDEN), sha256 disco ca1d95b5b3d19e9e y sha256 LF ca1d95b5b3d19e9e |
| **cuentas por `estado`, identicas a las de la entrada** | **SI**, y son estado> HECHA    32 y estado> LISTA    39 |
| `git diff --numstat` sobre el arbol docs/plan (sin comillas inversas a proposito: el instrumento de rutas se cae con un directorio, y va en la 5) al entrar / al salir | 0 / 1 (se exige 1, y es docs/plan/OPERACIONES.jsonl) |
| la recarga del `jsonl` linea a linea | 71; lineas que NO parsean: 0 (se exige 0) |
| **el campo `nodos` NO se movio** | **14 (se exige 14)** |
| **el campo `estado` NO se movio** | **'LISTA' (se exige 'LISTA')** |
| el texto viejo, entero y encima, byte a byte | el texto viejo esta ENTERO Y ENCIMA (la adjudicacion nueva empieza por la vieja, byte a byte): SI |
| **el caso rojo por mutacion, corrido ANTES de escribir** | **4. CIFRA mutantes que CAEN en rojo: 4 (se exige que caigan todos)** |

**LOS DOS CAMPOS PROHIBIDOS SIGUEN DONDE ESTABAN, Y NO ES UNA PROMESA: TRES DE LOS CUATRO MUTANTES LO PRUEBAN.** El mutante 2 mueve `nodos`, el 3 mueve `estado` y el 4 toca otra ficha, y la guarda cae en los tres. **La correccion vive solo en la prosa que contradecia a su vecina.**

### `1.d` LAS CUATRO ADJUDICACIONES QUE NO PIDEN TRABAJO, REGISTRADAS SIN EJECUTAR

**LAS CUATRO ADJUDICACIONES REGISTRADAS.** **FILAS ARMADAS LEYENDO `docs/loop/ACTA_AUDITOR.md` y `docs/plan/08_VERIFICACION.md`: 4; FILAS QUE DEBERIA HABER: 4.**

| cual | que dice | su cita, leida hoy de su linea |
|---|---|---|
| `6.2` | **EL CRITERIO DE HECHO DE UNA FICHA DE FASE 10 ES EL GENERAL**, porque el fichero declara que es uno solo. Es extension citable, no doctrina nueva | linea **9** de `docs/plan/08_VERIFICACION.md`, leida hoy: > **UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA.** |
| `6.3` | **`OP-I-01` NO SE CIERRA y su `estado` se queda en `LISTA`**, con motivo escrito: un punto en `NO CUBRE` y dos `A MEDIAS` no cumplen el criterio general. **No lo toque** | linea **74595** del acta: **`6.3` `OP-I-01` NO SE CIERRA, Y AHORA CON EL CRITERIO PUESTO.** Aplicado el criterio |
| `6.4` | **EL `NO CUBRE` DEL PUNTO 2 SE SOSTIENE.** 95 formas incompletas y 0 que lo digan; marcar las 95 sube al fundador y **no lo hago** | linea **74601** del acta: **`6.4` LA `D.3` SE ADJUDICA Y EL `NO CUBRE` SE SOSTIENE.** El banco `9.26`, verbatim: |
| `6.5` | **EL CUBO SE LLAMA DESDE HOY *LOS PASOS DE HOY SON LOS DEL BLOQUE 1***, no *EL BLOQUE YA VIVE APARTE*. La medicion vale y el nombre no | linea **74610** del acta: **`6.5` LA `D.1` ESTA BIEN MARCADA Y EL NOMBRE SE CORRIGE SIN TOCAR LA MEDICION.** El |

**LO QUE NO TOQUE, Y SE DICE COMO CIFRA:** `OP-I-01` sigue en `LISTA` (la `1.c` lo midio al contar por `estado`: estado> LISTA    39 fichas en `LISTA` al entrar y las mismas al salir), y **las 95 entradas del inventario siguen sin marcar**, que es lo que el encargo manda.

### LA TAREA 2 SE ABRE, PORQUE LA `1.b` CONFIRMO

El encargo la condiciona con estas palabras: *esta tarea SOLO se abre si la `1.b` CONFIRMA el cambio del 730*. **Confirmo, y por eso existe.** La puerta la comprueba el propio instrumento leyendo la salida de la `1.b`: CIFRA la 1.b dice CONFIRMA: SI: SI, sobre un fichero que mide 10520 bytes en disco y 10520 normalizado a LF (COINCIDEN), sha256 disco 2991383baa3dbcf6 y sha256 LF 2991383baa3dbcf6.

**Y LA LISTA DE LOS CUATRO NO LA TECLEO: LA LEE.** El instrumento saca los cuatro puestos de la linea de la `1.b` que los publica, y coteja la lista contra la cifra que esa misma linea declara: CIFRA puestos leidos de esa linea: 4, y la cifra que la propia linea declara es 4 (se exige que sean iguales).

**LOS CUATRO EN `A` QUE NOMBRAN EL CERO-ENLAZADOS, CON SU CLASE DE HOY.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T2_COLA_RELECTURA.txt`: 4; FILAS QUE DEBERIA HABER: 4.**

| puesto y clase, tal como el instrumento la leyo del archivo |
|---|
| puesto 474 clase HOY A |
| puesto 568 clase HOY A |
| puesto 586 clase HOY A |
| puesto 730 clase HOY D (era A en la apertura de esta vuelta y la 1.b lo paso a D) |

**CIFRA de los 4, cuantos siguen en A despues de la 1.b: 3 (474, 568, 586)**, que son los que esta tarea mira. **El 730 ya no se mira aqui: es el par que la `1.b` acaba de corregir**, y mirarlo otra vez seria contarlo dos veces.

### DE QUE DEPENDE LA CLASE DE CADA UNO, CITANDO SU PROPIA RAZON

**ESTO ES LECTURA Y CITA, NO RE-CRIBADO**, que es como el encargo lo pide. No resuelvo aristas ni vuelvo a aplicar la vara: leo la razon que el archivo ya tiene y publico QUE FRASE SUYA sostiene la clase. Las anclas de busqueda son fijas y estan en el fuente del instrumento; lo que se publica es **la frase entera** que cada ancla encuentra.

**EL REPARTO DE FRASES, CONTADO POR EL INSTRUMENTO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T2_COLA_RELECTURA.txt`: 3; FILAS QUE DEBERIA HABER: 3.**

| lo que midio |
|---|
| puesto 474: frases de silueta 1, frases de contenido 3, y la frase que CIERRA su clase es de CONTENIDO |
| puesto 568: frases de silueta 3, frases de contenido 4, y la frase que CIERRA su clase es de CONTENIDO |
| puesto 586: frases de silueta 2, frases de contenido 4, y la frase que CIERRA su clase es de CONTENIDO |

**CIFRA puestos cuya clase NO cierra por contenido: 0 (ninguno).** **LOS TRES CIERRAN POR CONTENIDO Y POR ESO LOS TRES SE QUEDAN COMO ESTAN.**

**EL VEREDICTO DE LECTURA, UNO A UNO.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T2_COLA_RELECTURA.txt`, razon entera leida del archivo: 3; FILAS QUE DEBERIA HABER: 3.**

| puesto | sus dos nodos | de que depende su clase |
|---|---|---|
| 474 | `milk_run_deliveries` / `programacion_entregas_delivery_scheduling` | **CONTENIDO, y con un matiz que marco como DISCUTIBLE.** Su frase de cierre es *Y el texto lo confirma por su cuenta: este hijo no solo desarrolla el paso 3, REPITE ademas dos pasos mas de la madre, asi que repite y no continua*. **Eso es contenido puro y no toca la silueta.** |
| 568 | `publicidad_offline_pruebas_locales` / `tracking_publicidad_offline` | **CONTENIDO, y COINCIDO CON EL AUDITOR.** Su frase de cierre es *Y la vara CONFIRMA la A por el lado del contenido, no por el de la arista: lo unico que el hijo anade a los pasos 3 y 4 de la madre es UNA LINEA, la pregunta como se entero de nosotros en el formulario*. |
| 586 | `brainstorming_efectivo` / `construir_sobre_ideas_ajenas` | **CONTENIDO, y COINCIDO CON EL AUDITOR.** Su frase de cierre es *Y la vara CONFIRMA la A por contenido: lo unico que el hijo anade al paso 2 de la madre es UNA LINEA, no atribuir las ideas a una sola persona para que puedan evolucionar*. |

**LOS DOS QUE EL AUDITOR YA HABIA VERIFICADO SON LOS DOS QUE MI LECTURA CONFIRMA.** El `568` y el `586` cierran por la vara de LINEA, y los dos lo dicen con esas palabras en su ultimo bloque. **Coincido con el, y lo digo porque el encargo pide que lo diga tanto si coincido como si no.**

### LAS RAZONES ENTERAS, PEGADAS SIN CORTAR, QUE ES LO QUE EL ENCARGO PIDE

**VAN DENTRO DE CERCA PORQUE SON VERBATIM DEL ARCHIVO**, no prosa de este reporte: sus cifras son del que las escribio, no mias. Las lee el compositor del propio `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.

**PUESTO 474**, clase `A`, `milk_run_deliveries` contra `programacion_entregas_delivery_scheduling`. Su razon entera, sin cortar (los bytes de cada una van contados en la salida sellada de la tarea, y no aqui: un campo de una fila no es un fichero y no tiene dos convenciones):

```
EL HIJO CON CASA PROPIA. Dato del grafo: SIN ARISTA entre los dos, verificado. REESCRITA EL 13 ago 2026 POR EL BARRIDO DE RAZONES: la apertura original citaba la PARAFRASIS ABOLIDA por el banco 9.5.0 como si fuera el argumento. La arista es DATO DEL GRAFO y no argumento, y corta en los dos sentidos: no acusa cuando falta ni exculpa cuando esta. La clase la decide LA VARA del banco 9.6.1, la linea o el procedimiento, como se lee mas abajo, y NO CAMBIA. milk_run_deliveries es el paso 3 de programacion_entregas_delivery_scheduling desarrollado, la rama de disenar rutas milk run cuando el lote economico no llena camion, y repite ademas dos pasos mas de la madre, el calculo del EOQ por ubicacion y la eleccion de la tecnica de ruteo entre matriz de ahorros y asignacion generalizada. La madre es la decision entre entrega directa y milk run; el hijo es una de las dos ramas contada aparte con tres de sus cinco pasos ya dichos arriba. Ninguno enlaza al otro. Detalle anotado: en las aristas de este par hay un nodo DEPRECADO. MEDICION DEL 12 ago 2026, LA MEDICION DE LOS VEINTE, con la regla LA MAYORIA MANDA del banco 9.6.1: FORMA medida: RADIOS. El unico hijo de paso vivo de programacion_entregas_delivery_scheduling es milk_run_deliveries, por el paso 3; ni la matriz de ahorros ni la asignacion generalizada ni las entregas directas tienen nodo propio. PROPORCION: CERO enlazados, o sea que no hay hermanos enlazados y la figura NO APLICA: manda la regla original. Y el texto lo confirma por su cuenta: este hijo no solo desarrolla el paso 3, REPITE ademas dos pasos mas de la madre, asi que repite y no continua. LA CLASE A SE SOSTIENE.
```

**PUESTO 568**, clase `A`, `publicidad_offline_pruebas_locales` contra `tracking_publicidad_offline`. Su razon entera, sin cortar (los bytes de cada una van contados en la salida sellada de la tarea, y no aqui: un campo de una fila no es un fichero y no tiene dos convenciones):

```
EL HIJO CON CASA PROPIA. Dato del grafo: SIN ARISTA entre los dos, verificado resolviendo a nodo vivo. REESCRITA EL 13 ago 2026 POR EL BARRIDO DE RAZONES: la apertura original citaba la PARAFRASIS ABOLIDA por el banco 9.5.0 como si fuera el argumento. La arista es DATO DEL GRAFO y no argumento, y corta en los dos sentidos: no acusa cuando falta ni exculpa cuando esta. La clase la decide LA VARA del banco 9.6.1, la linea o el procedimiento, como se lee mas abajo, y NO CAMBIA. tracking_publicidad_offline es el paso 3 de publicidad_offline_pruebas_locales desarrollado, asignar un codigo unico o una direccion web a cada campana para rastrear que trae clientes, convertido en nodo entero con la direccion web propia por campana, el codigo de descuento distinto por canal y la decision de donde meterle mas, que es el paso 4 de la madre otra vez. Lo unico suyo es la pregunta como se entero de nosotros en el formulario. Los dos son de Traction, Weinberg. OBSERVACION NUEVA, y es de forma: la madre tiene DOS pasos con casa propia, el 2 es publicidad_remanente_remnant_ads, y no enlaza a ninguno de los dos; el que si enlaza al hijo del paso 2 es el hijo del paso 3. La madre no enlaza a sus hijos y los hijos se enlazan entre ellos. MEDICION DEL 12 ago 2026, LA MEDICION DE LOS VEINTE, con la regla LA MAYORIA MANDA del banco 9.6.1: FORMA medida: RADIOS. Hijos de paso vivos de publicidad_offline_pruebas_locales: publicidad_remanente_remnant_ads por el paso 2 y tracking_publicidad_offline por el paso 3. PROPORCION: CERO enlazados, que es lo que la razon ya decia; las dos aristas de la madre van a content_marketing_blog y seo_estrategia_fat_head. La figura NO APLICA, manda la regla original. LA CLASE A SE SOSTIENE. RATIFICADO EL 12 ago 2026: el fundador incorporo el limite del cero-enlazados DENTRO de la regla del banco 9.6.1, como caso extremo del mitad-o-menos. La redaccion queda asi: si no hay ni un hermano enlazado no hay mayoria de la que tirar, la silueta no dice nada y manda el contenido. Este veredicto deja de colgar de una nota mia y pasa a citar la regla. CHOQUE DECLARADO EL 12 ago 2026, Y LO TRAIGO EN VEZ DE RESOLVERLO: la razon de arriba dice dos cosas que no encajan. La parte vieja dice que con cero enlazados LA FIGURA NO APLICA y manda la regla original, sin arista igual a duplicacion, que es lo que sostiene la A. La ratificacion dice que cero enlazados es el caso extremo del mitad-o-menos y que entonces MANDA EL CONTENIDO. No son lo mismo: si manda el contenido, este par hay que juzgarlo por continua-o-repite y no por la ausencia de arista. NO CAMBIO LA CLASE por mi cuenta porque el encargo dice que estos diez quedan citando la regla, pero dejo el choque escrito aqui y en la seccion 19 del informe, con la cuenta de cuales aguantarian el test de contenido y cuales no. Sin el visto del auditor este veredicto queda con las dos lecturas encima. EJECUCION DEL 12 ago 2026 CON LA VARA NOMBRADA, LA LINEA O EL PROCEDIMIENTO del banco 9.6.1, que resuelve el choque de la seccion 19 en la rama contenido-manda. Par verificado otra vez contra el grafo al escribir el cambio: la madre publicidad_offline_pruebas_locales NO enlaza a tracking_publicidad_offline, verificado resolviendo a nodo vivo. Y la vara CONFIRMA la A por el lado del contenido, no por el de la arista: lo unico que el hijo anade a los pasos 3 y 4 de la madre es UNA LINEA, la pregunta como se entero de nosotros en el formulario. Todo lo demas que trae, la direccion web por campana, el codigo de descuento por canal y la decision de donde invertir mas, ya esta en la madre. REPITE. LA CLASE A SE SOSTIENE, ahora citando la vara y no la ausencia de arista.
```

**PUESTO 586**, clase `A`, `brainstorming_efectivo` contra `construir_sobre_ideas_ajenas`. Su razon entera, sin cortar (los bytes de cada una van contados en la salida sellada de la tarea, y no aqui: un campo de una fila no es un fichero y no tiene dos convenciones):

```
EL HIJO CON CASA PROPIA. Dato del grafo: SIN ARISTA entre los dos, verificado resolviendo a nodo vivo. REESCRITA EL 13 ago 2026 POR EL BARRIDO DE RAZONES: la apertura original citaba la PARAFRASIS ABOLIDA por el banco 9.5.0 como si fuera el argumento. La arista es DATO DEL GRAFO y no argumento, y corta en los dos sentidos: no acusa cuando falta ni exculpa cuando esta. La clase la decide LA VARA del banco 9.6.1, la linea o el procedimiento, como se lee mas abajo, y NO CAMBIA. construir_sobre_ideas_ajenas es el paso 2 de brainstorming_efectivo desarrollado, priorizar la regla de construir sobre las ideas de otros por encima de generar las propias, convertido en nodo entero con sus tres movimientos: compartir abiertamente en vez de guardarlas como propiedad individual, hacer sesiones de construccion colectiva del tipo si, y ademas, y no atribuir las ideas a una sola persona para que puedan evolucionar. Lo unico que se perderia es esa tercera, la no atribucion. NO APLICO aqui la figura del puesto 581, hermanos enlazados menos uno, y digo por que: brainstorming_efectivo enlaza a seis nodos pero ninguno de los seis es el desarrollo de un paso suyo, son vecinos de la sesion, o sea que no hay una familia de radios en la que falte uno. LIMITE DE LA REGLA FAMILIA DECLARADA por quinta vez: solo brainstorming_efectivo esta en la nomina del racimo Las reglas del brainstorming. MEDICION DEL 12 ago 2026, LA MEDICION DE LOS VEINTE, con la regla LA MAYORIA MANDA del banco 9.6.1: FORMA medida: RADIOS. Hijos de paso vivos de brainstorming_efectivo: construir_sobre_ideas_ajenas por el paso 2 y reglas_brainstorming por el paso 1. PROPORCION: CERO enlazados, que es exactamente lo que la razon ya argumentaba: los seis nodos que la madre enlaza son vecinos de la sesion y ninguno desarrolla un paso suyo, incluido brainstorming, que es hermano de racimo y no hijo. La figura NO APLICA. LA CLASE A SE SOSTIENE. RATIFICADO EL 12 ago 2026: el fundador incorporo el limite del cero-enlazados DENTRO de la regla del banco 9.6.1, como caso extremo del mitad-o-menos. La redaccion queda asi: si no hay ni un hermano enlazado no hay mayoria de la que tirar, la silueta no dice nada y manda el contenido. Este veredicto deja de colgar de una nota mia y pasa a citar la regla. CHOQUE DECLARADO EL 12 ago 2026, Y LO TRAIGO EN VEZ DE RESOLVERLO: la razon de arriba dice dos cosas que no encajan. La parte vieja dice que con cero enlazados LA FIGURA NO APLICA y manda la regla original, sin arista igual a duplicacion, que es lo que sostiene la A. La ratificacion dice que cero enlazados es el caso extremo del mitad-o-menos y que entonces MANDA EL CONTENIDO. No son lo mismo: si manda el contenido, este par hay que juzgarlo por continua-o-repite y no por la ausencia de arista. NO CAMBIO LA CLASE por mi cuenta porque el encargo dice que estos diez quedan citando la regla, pero dejo el choque escrito aqui y en la seccion 19 del informe, con la cuenta de cuales aguantarian el test de contenido y cuales no. Sin el visto del auditor este veredicto queda con las dos lecturas encima. EJECUCION DEL 12 ago 2026 CON LA VARA NOMBRADA, LA LINEA O EL PROCEDIMIENTO del banco 9.6.1, que resuelve el choque de la seccion 19 en la rama contenido-manda. Par verificado otra vez contra el grafo al escribir el cambio: la madre brainstorming_efectivo NO enlaza a construir_sobre_ideas_ajenas, verificado resolviendo a nodo vivo. Y la vara CONFIRMA la A por contenido: lo unico que el hijo anade al paso 2 de la madre es UNA LINEA, no atribuir las ideas a una sola persona para que puedan evolucionar. Compartir abiertamente y construir sobre lo del otro es lo que la madre ya manda. REPITE. LA CLASE A SE SOSTIENE, ahora citando la vara y no la ausencia de arista.
```

**RAZONES PEGADAS ENTERAS: 3; RAZONES QUE DEBERIA HABER: 3.**

### `474`: POR QUE LO MARCO COMO DISCUTIBLE AUNQUE NO LO MUEVO

**LO MARCO ANTES DE SABER SI ACIERTO, QUE ES LO QUE VALE LA MARCA.** El `474` es el unico de los tres que **no tiene el bloque de EJECUCION con la vara nombrada** que el `568` y el `586` si tienen. Lo que tiene es la lectura vieja escrita en presente, *PROPORCION: CERO enlazados, o sea que no hay hermanos enlazados y la figura NO APLICA: manda la regla original*, **y encima una confirmacion de contenido que llega despues y por su cuenta**.

**POR QUE AUN ASI NO SE MUEVE, Y NO ES MI OPINION:** el propio banco lo ratifica por contenido. La linea **1742** de `docs/BANCO_DE_TEXTOS.md`, leida hoy, dice: | **474** | el hijo **repite además dos pasos más** de la madre |. Y la linea **1735** dice: **EJECUTADA sobre los veintitrés veredictos de esa silueta: DIECINUEVE cayeron a **Un veredicto que la ratificacion del fundador nombra entre los que se sostienen no lo mueve un ejecutor.**

**LA DIFERENCIA CON EL 730, DICHA PARA QUE NO SE CONFUNDAN:** el 730 **decia de si mismo** que su clase colgaba de la lectura vieja y **que por contenido seria D**, y por eso su propia razon lo dejaba sin resolver. **El 474 dice lo contrario**: dice que por contenido REPITE. **Uno pedia que lo resolvieran y el otro ya estaba resuelto.**

### LO QUE ESTA TAREA NO HIZO, DICHO COMO CIFRA

**LA TAREA 2 NO TOCA EL ARCHIVO, Y SE MIDE.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_T2_COLA_RELECTURA.txt`: 4; FILAS QUE DEBERIA HABER: 4.**

| que | lo que dice el instrumento |
|---|---|
| clases cambiadas por la TAREA 2 | 0 |
| el `sha256` del archivo al cerrar la TAREA 2 | 758edf1f5c313c18 en disco y 758edf1f5c313c18 normalizado a LF (el mismo que arriba: SI) |
| filas del archivo | 3388 |
| puestos que dependen de la silueta y habria que traer | 0 (ninguno) |

**NO ABRO NINGUNA COLA DE RE-CRIBADO.** El encargo lo dice con estas palabras: *una cosa es corregir el par que su propia razon deja sin resolver y otra es abrir una cola de re-cribado por mi cuenta. Yo no la abro y tu tampoco.* **No la abro.** Lo unico que sube es la marca del `474`, y sube como discutible, no como encargo.

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: LA VUELTA 212 ENTREGA SUS DOS TAREAS: el puesto 730 verificado contra el grafo, confirmado por la vara y corregido por el carril del banco 9.10 con el marcador RECOMPUTADO de A 551 a A 550, la P.2 de OP-F-04-HOR declarada sin tocar nodos ni estado, y la cola de relectura midiendo que NINGUNO de los tres que quedan en A cuelga de la silueta. UNA caida propia declarada, CUATRO discutibles marcados y UN hallazgo: el instrumento de rutas de la casa se cae con un directorio, y eso tumba tambien al reporte de la 210 y al de la 211.**

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE ESTA SECCION CITA EL FICHERO DEL QUE SALE** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO). Las de las dos tareas van en su anexo, talladas por `scripts/loop/_v212_t1_seccion.py` y `scripts/loop/_v212_t2_seccion.py`, y **aqui no se repiten**.

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, NUNCA `run_phase1.py` A SECAS

Corrido con `scripts/loop/_v212_ciclo_gate0.py`, que **IMPORTA** los ocho comandos de `scripts/loop/_v205_ciclo_gate0.py` y solo le corrige el numero de vuelta, computado de su propio nombre y no tecleado. **PEOR EXITCODE DE LOS OCHO: 0 en APERTURA y 0 en CIERRE.**

**EL CICLO DE GATE 0, LOS DOS LADOS.** **FILAS ARMADAS LEYENDO las DIECIOCHO salidas `docs/loop/SALIDA_V212_*_APERTURA.txt` y `_CIERRE.txt`: 9; FILAS QUE DEBERIA HABER: 9.**

| # | comando | APERTURA | CIERRE |
|---|---|---|---|
| 1 | `run_phase1.py --reaplico-curaduria` | EXITCODE 0, 4790 bytes | EXITCODE 0, 4790 bytes |
| 2 | `etiquetas_de_cara.py --aplicar` | EXITCODE 0, 7928 bytes | EXITCODE 0, 7928 bytes |
| 3 | `sync_assets_web.py` | EXITCODE 0, 574 bytes | EXITCODE 0, 574 bytes |
| 4 | `git diff HEAD --numstat` | EXITCODE 0, **0 filas**, 140 bytes | EXITCODE 0, **0 filas**, 140 bytes |
| 5 | `vuelta83_conteo_aristas.py WORK` | EXITCODE 0, 168 bytes | EXITCODE 0, 168 bytes |
| 6 | `vuelta85_medir_desfase_calibrado` | EXITCODE 0, 498 bytes | EXITCODE 0, 498 bytes |
| 7 | `engine/run_all_tests.py` | EXITCODE 0, 1131 bytes | EXITCODE 0, 1131 bytes |
| 8a | `npx tsc --noEmit` | EXITCODE 0, 7 bytes | EXITCODE 0, 7 bytes |
| 8b | `pnpm test` | EXITCODE 0, 336 bytes | EXITCODE 0, 336 bytes |

**LAS DIECIOCHO CELDAS SE CUENTAN DE SUS DIECIOCHO FICHEROS**, una a una, y el `EXITCODE` sale de la ultima linea de cada uno. **`git diff HEAD --numstat` da CERO FILAS en los dos lados: el grafo no se movio ni al abrir ni al cerrar.**

### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES

**LAS SEDES, AL ENTRAR Y AL CERRAR.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_APERTURA.txt` para la apertura y una medicion de AHORA para el cierre: 7; FILAS QUE DEBERIA HABER: 7.**

| sede | al entrar (disco / LF) | al cerrar (disco / LF) | `sha256` de cierre (disco / LF) | la movio esta vuelta |
|---|---|---|---|---|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 4054129 / 4054129 | 4057130 / 4057130 | `758edf1f5c313c18` / `758edf1f5c313c18` | **SI**, la `TAREA 1.b`: el puesto 730 |
| `docs/plan/OPERACIONES.jsonl` | 513043 / 513043 | 514452 / 514452 | `ca1d95b5b3d19e9e` / `ca1d95b5b3d19e9e` | **SI**, la `TAREA 1.c`: la `adjudicacion` de `OP-F-04-HOR` |
| `dataset/metadata/master_graph.json` | 8375817 / 8375817 | 8375817 / 8375817 | `627cc662296f7f00` / `627cc662296f7f00` | NO, solo se leyo para resolver aristas |
| `docs/plan/01_FUENTES.md` | 128187 / 126666 | 128187 / 126666 | `73168452929b3d42` / `f965abf6c3ca95c3` | NO, solo se leyeron sus lineas 1168 y 1453 |
| `docs/plan/08_VERIFICACION.md` | 69068 / 69068 | 69068 / 69068 | `76bfebb6b2d8ef72` / `76bfebb6b2d8ef72` | NO, solo se leyo su linea 9 |
| `docs/BANCO_DE_TEXTOS.md` | 186490 / 186490 | 186490 / 186490 | `8adbd60239509bb4` / `8adbd60239509bb4` | NO, solo se leyeron sus `9.6.1`, `9.6.2`, `9.6.3` y `9.10` |
| `docs/loop/ACTA_AUDITOR.md` | 4936249 / 4936249 | 4936249 / 4936249 | `a977aa91e8b9f86c` / `a977aa91e8b9f86c` | NO, solo se leyo |

**LAS DOS QUE SE MOVIERON SE MOVIERON UNA SOLA VEZ CADA UNA, Y LAS DOS LO PRUEBAN CON `sha256` DISTINTO AL SALIR** (`SI (se exige SI)` en la `1.b` y `SI (se exige SI)` en la `1.c`). **`docs/plan/01_FUENTES.md` es la unica sede cuyas dos convenciones NO COINCIDEN**, y no es cosa de esta vuelta: entra y sale igual, y ni se abrio para escribir.

### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, MEDIDAS CON EL INSTRUMENTO DE LA CASA

**LA CIFRA NO SE PUBLICA AQUI, Y NO ES OMISION: ES LA REGLA.** El instrumento que las cuenta es `scripts/loop/vuelta186_rutas_del_reporte.py` y **necesita el reporte YA CERRADO** para contar las rutas que el propio cierre anade. Publicar aqui la cifra de antes del cierre seria medir temprano y publicar tarde, que es la caida de la vuelta 28 (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE). **Su salida sellada es `docs/loop/SALIDA_V186_RUTAS_DEL_REPORTE.txt` y ahi vive la cifra**, corrida sobre el reporte cerrado.

**Y LA CORRIDA QUE SE COMMITEA ES LA DE DESPUES DEL CIERRE, no una de antes.** Su veredicto y su cifra de rutas que no existen o miden cero se leen en ese fichero sellado, y no se copian aqui: copiarlas seria volver a publicar una medicion de apertura como si fuera de cierre.

## 4. LO QUE SE TOCO, Y LO QUE NO

**SE TOCARON DOS SEDES Y TRES CAMPOS EN TOTAL:** la `clase` y la `razon` del puesto 730 en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y la `adjudicacion` de `OP-F-04-HOR` en `docs/plan/OPERACIONES.jsonl`. **NI UN NODO DEL GRAFO**, que es lo que la regla 4 de `EJECUTOR.md` manda en modo de cierre, y lo prueban las dos celdas de `git diff HEAD --numstat` de la `3.1`, las dos en cero filas.

**LO QUE MI APERTURA SELLADA DICE, COTEJADO Y NO TECLEADO** (`docs/loop/SALIDA_V212_APERTURA.txt`): **`git status --porcelain` AL ENTRAR daba 2 lineas**, y las dos eran mis propios computos `_v212_` sin seguir todavia, no trabajo ajeno colgando; y **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0**, o sea que la vuelta empezo con el grafo limpio.

### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO

**TODO LO QUE ESTA VUELTA ESCRIBIO EN scripts/loop, LISTADO CON `os.listdir` EN ESTA CORRIDA.** **FILAS ARMADAS LEYENDO un `os.listdir` del arbol scripts/loop (otra vez sin comillas inversas, por lo mismo que la 7 bis) filtrado por el prefijo: 14; FILAS QUE DEBERIA HABER: 14.**

| fichero | que es |
|---|---|
| `scripts/loop/_v212_apertura.py` | computo de la vuelta |
| `scripts/loop/_v212_ciclo_gate0.py` | computo de la vuelta |
| `scripts/loop/_v212_cierre_texto.md` | cuerpo compuesto, no fuente |
| `scripts/loop/_v212_cierre_texto.py` | computo de la vuelta |
| `scripts/loop/_v212_esqueleto.py` | computo de la vuelta |
| `scripts/loop/_v212_hallazgo_rutas.py` | computo de la vuelta |
| `scripts/loop/_v212_t1_seccion.md` | cuerpo compuesto, no fuente |
| `scripts/loop/_v212_t1_seccion.py` | computo de la vuelta |
| `scripts/loop/_v212_t1b_escribir.py` | computo de la vuelta |
| `scripts/loop/_v212_t1b_puesto_730.py` | computo de la vuelta |
| `scripts/loop/_v212_t1c_op_f_04_hor.py` | computo de la vuelta |
| `scripts/loop/_v212_t2_cola_relectura.py` | computo de la vuelta |
| `scripts/loop/_v212_t2_seccion.md` | cuerpo compuesto, no fuente |
| `scripts/loop/_v212_t2_seccion.py` | computo de la vuelta |

**CIFRA ficheros con prefijo `_v212_`: 14, de ellos 11 con extension `.py` y 3 con extension `.md`.** **LA CIFRA Y LA LISTA SALEN DEL MISMO `os.listdir`, en la misma linea de codigo**, que es el remedio de la `C.3` que el ejecutor de la 211 se cazo a si mismo: alli la cifra estaba tecleada y la lista no la miraba nadie.

**LOS 14 LLEVAN LOS 14 EL PREFIJO DE GUION BAJO**, o sea que estan **fuera del censo y fuera de la nomina**, y mueren con la vuelta. **NINGUNO ES ARNES, GUARDA NI LECTOR NUEVO:** los cuatro que miden importan sus funciones de la sede que ya existe (`scripts/loop/apertura_del_auditor.py` para el marcador, `scripts/loop/verificar_aristas_vivas.py` para el resolutor, `scripts/loop/vuelta186_rutas_del_reporte.py` para las dos convenciones y para el patron de rutas), y los tres compositores solo leen salidas y arman texto. **LA NOMINA DE LA BATERIA SIGUE CONGELADA EN 135 Y NADIE LA PODO.**

### 4.2. LA `1.d` DEL ENCARGO, CUMPLIDA POR OMISION Y DICHA EN VOZ ALTA

**NO TOQUE `OP-I-01`** (sigue en `LISTA`, contado en la `1.c` al medir por `estado` antes y despues), **NO MARQUE LAS 95 ENTRADAS DEL INVENTARIO**, y **NO ESCRIBI NI UNA FILA NUEVA EN `docs/plan/08_VERIFICACION.md`**. Las tres son prohibiciones expresas del encargo y las tres se cumplen. La `1.d` las registra con su cita en el anexo de la TAREA 1.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` NO BARRI LAS DOS CITAS VIVAS DEL 730 FUERA DEL ARCHIVO, Y EL BANCO `9.10` DICE QUE UN VOLTEO BARRE SUS TABLAS DERIVADAS EN EL MISMO ACTO.** Las medi y las publico en la TAREA 1: `docs/INTRA_DOMINIO_INFORME.md` linea 6941 y `docs/plan/03_FUSIONES.md` linea 5424, mas una tercera en un reporte archivado que no se toca. **Mi lectura es que no envejecen como frase**, porque las dos dicen que el 730 *declara* la `A` por la lectura vieja y la fila **sigue diciendo eso**, con el texto viejo entero encima; lo que envejece es la clase que el lector infiere. **Y mi motivo para no editarlas es que es prosa sellada del informe y del plan**, que es forma, y la forma del plan el propio auditor la manda al fundador en su `6.2`. **Puedo estar equivocado en las dos mitades y por eso lo marco.**

**`D.2` EL PUESTO `474`.** Es el unico de los tres que quedan en `A` que **no tiene bloque de EJECUCION con la vara nombrada**, y lleva la lectura vieja escrita en presente (*la figura NO APLICA: manda la regla original*). **No lo muevo**, porque la ratificacion del banco lo nombra entre los que se sostienen y su razon cierra por contenido. **Pero es el que mas se parece al 730 de los que quedan**, y si alguien va a discutir uno, va a ser ese.

**`D.3` DIGO QUE DOS CIFRAS DEL ACTA 211 NO REPRODUCEN.** Su **13** y su **9** no salen de ningun patron que yo haya probado: el guion literal da 11 y 8, el patron holgado da 14 y 10. **Puede que el auditor usara un tercer patron que no se me ocurrio**, y por eso publico LOS DOS MIOS con su expresion regular al lado en vez de decir solo que el suyo esta mal. **Lo que no es discutible es que la lista de los cuatro en `A` y los once del choque reproducen al digito.**

**`D.4` PEGUE LAS TRES RAZONES ENTERAS DENTRO DE CERCA.** El encargo pide la razon entera; las cercas son donde esta casa pone el verbatim, y la guarda de las dos convenciones **no mira dentro de una cerca** (es lo que el acta 211 mide en su `7.2`). **O sea que las cifras que esas razones llevan dentro entran al reporte sin que ninguna guarda las mire.** Son del autor que las escribio y no mias, y lo digo, pero alguien puede sostener que un verbatim con cifras deberia ir de otra manera.

## 6. LAS PREGUNTAS

**`P.1` EL BARRIDO DEL `9.10`: QUIEN LO HACE.** Cuando una relectura conjunta voltea UN veredicto, las citas vivas de ese numero en el informe y en el plan quedan describiendo la clase vieja. **El `9.10` manda barrerlas y el encargo no me lo ordena, y editar prosa sellada tampoco me toca.** No es contradiccion suficiente para parar (la `D.1` explica por que), pero la casa no tiene escrito quien lo hace en un volteo de UNA sola fila. **Traigo las dos lineas nombradas para que se adjudique.**

**`P.2` EL INSTRUMENTO DE RUTAS SE CAE CON UN DIRECTORIO, Y ESO TOCA A TRES REPORTES.** Va entera en la `7`, con su medicion. La pregunta es de gobierno: **la moratoria prohibe reparar lectores**, y este no da una cifra mala, da una excepcion. **No lo toque. Pregunto si el arreglo entra por la puerta de la caida de dato o si espera a que se levante la moratoria.**

## 7. PENDIENTES DE DOCTRINA

**`PD.1` UNA CORRECCION QUE CONSERVA EL TEXTO VIEJO ENTERO DEJA LAS CITAS DERIVADAS EN UN ESTADO QUE LA DOCTRINA NO NOMBRA.** El banco `9.10` habla de tablas que **citan un veredicto por numero** y de volteos **en bloque**. Aqui hay un volteo de UNA fila y dos citas que **no son tablas**: son prosa narrativa que describe lo que la fila decia, y que **sigue siendo cierta como descripcion del texto**. **No hay regla que diga si eso hay que barrerlo, matizarlo o dejarlo.** Registro lo mejor sostenido (no barrer, declarar) y sigo, que es lo que manda la regla 5 de `EJECUTOR.md`.

**`PD.2` UN VERBATIM CON CIFRAS AJENAS DENTRO DE UNA CERCA NO TIENE REGLA.** Va ligado a la `D.4`. La casa exige que toda cifra lleve su corte y su atribucion, y una razon del archivo pegada entera trae docenas de cifras del que la escribio. **La cerca las saca del alcance de la guarda, que es lo que las hace publicables; lo que no esta escrito es si eso es lo correcto o solo lo que funciona.**

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**`C.1`. ESCRIBI Y COMMITEE UN FICHERO LLAMADO `SALIDA_V212_TALLADOR_CABECERA.txt` QUE NO LLEVABA UNA CABECERA: LLEVABA UN RECHAZO.** En la apertura corri el tallador sabiendo que la mitad del cierre no existe todavia, y **redirigi su salida al mismo nombre que usa el fichero bueno**. Durante un commit entero, una ruta que promete una cabecera tallada apuntaba a veinte celdas que no se pudieron leer. **Es la especie de LA RUTA QUE PROMETE PRUEBA ES CIFRA** (`EJECUTOR.md` 1): la ruta existia y no media cero, asi que ninguna guarda la habria cazado, y el contenido no era el que el nombre promete. **REMEDIO, y es una linea: el tallador de apertura, si se corre, escribe en un nombre con `_RECHAZO` y no en el del cierre.** El fichero bueno existe desde el cierre y es el que la cabecera cita.

**LO QUE NO CUENTO COMO CAIDA, Y DIGO POR QUE.** Primero: **el heredoc de comillas simples se me cayo** al escribir el primer computo, igual que a la 209, la 210, la 211 y al propio auditor. **No es caida porque el remedio ya estaba escrito y lo cumpli:** use la herramienta de fichero y lo digo, que es lo que el acta 210 dejo dicho. Segundo: **el compositor de la TAREA 1 cayo en ROJO en su primera corrida**, porque le pedi la tercera aparicion de una linea que solo tiene dos. **Eso no es una caida: es la guarda haciendo su trabajo**, y cayo **antes** de escribir nada. Tercero: **parche una celda del reporte ya anexado** para quitarle unas comillas inversas a un directorio; **no lo cuento como caida porque el parche se verifico contra el `.md` regenerado byte a byte** y porque el motivo esta publicado entero en la `7`, pero **lo digo en vez de callarlo** porque un reporte parcheado a mano es exactamente lo que la 211 decidio no volver a hacer.

## 7 BIS. EL HALLAZGO DE LA VUELTA, MEDIDO Y NO REPARADO

**EL INSTRUMENTO QUE HACE CUMPLIR *LA RUTA QUE PROMETE PRUEBA ES CIFRA* SE CAE CON EXCEPCION SI EL REPORTE CITA UN DIRECTORIO.** `scripts/loop/vuelta186_rutas_del_reporte.py` casa la cadena docs/plan seguida de barra (la escribo aqui SIN comillas inversas a proposito, porque escribirla con ellas reproduce el fallo dentro de este mismo reporte, y eso me paso), `os.path.exists` dice que si porque el directorio existe, y el `read()` revienta. **Lo medi importando SU funcion, para que el patron fuera el suyo y no uno mio.**

**LOS DOS REPORTES ARCHIVADOS, MEDIDOS.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_HALLAZGO_RUTAS.txt`: 6; FILAS QUE DEBERIA HABER: 6.**

| lo que midio el instrumento |
|---|
| docs/loop/reportes/REPORTE_V211.md: 29 rutas distintas, medidas con SU patron |
| rutas de docs/loop/reportes/REPORTE_V211.md que no existen en disco: 1 ['docs/loop/SALIDA_V211_BATERIA.txt'] |
| ese texto TUMBA el instrumento: SI (basta UNA fila de la tabla de arriba) |
| docs/loop/reportes/REPORTE_V210.md: 19 rutas distintas, medidas con SU patron |
| rutas de docs/loop/reportes/REPORTE_V210.md que no existen en disco: 0 |
| ese texto TUMBA el instrumento: SI (basta UNA fila de la tabla de arriba) |

**CIFRA directorios citados en los DOS sujetos archivados, sumados: 4.** **LOS SUJETOS SON LOS DOS REPORTES YA ARCHIVADOS Y NO EL DE ESTA VUELTA, A PROPOSITO:** este reporte todavia va a crecer con su cierre, y publicar aqui sus bytes seria medir temprano y publicar tarde. **A este lo mide el propio instrumento de la casa DESPUES del cierre, y si citara un directorio se caeria.** **NO ES UN DEFECTO QUE TRAIGA ESTA VUELTA:** el reporte de la 210 y el de la 211 citan dos directorios cada uno y los dos tumban el instrumento igual. **Y esto prueba una cosa que importa mas que el crash: la cifra de rutas que el reporte de la 211 publica no puede haber salido de este instrumento, porque sobre ese texto el instrumento no llega a imprimir.**

**NO LO REPARO, Y ES LETRA:** la moratoria de `AUDITOR.md` 6.3 prohibe arreglar lectores. **Lo que si hice, porque no cuesta codigo, es sacar de mi reporte los DOS sitios donde citaba un directorio entre comillas inversas**, uno en la TAREA 1 y otro en esta misma seccion, **y por eso el instrumento SI corre sobre este reporte**. El segundo es el que mas dice: **describir el fallo con su ejemplo entrecomillado lo reproducia**, y lo cace corriendo el instrumento sobre el reporte ya cerrado en vez de darlo por bueno. Su caso rojo por mutacion esta corrido: EL CASO ROJO CAE COMO TIENE QUE CAER: sin mutar da 0 y mutado da 1..

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

1. **ADJUDICAR LA `P.1`**: quien barre las citas vivas de un veredicto volteado cuando el volteo es de una sola fila. Las dos lineas estan nombradas y medidas, y el trabajo, si se adjudica, son dos ediciones de prosa.
2. **ADJUDICAR LA `P.2`**: si el crash del instrumento de rutas entra por la puerta de la caida de dato (y entonces se arregla ya) o espera a que se levante la moratoria. **Mientras no se decida, todo reporte que cite un directorio entre comillas inversas se queda sin medir sus rutas, y eso no deja sintoma.**
3. **NO ABRIR COLA DE RE-CRIBADO.** La TAREA 2 midio que **ninguno** de los tres que quedan en `A` cuelga de la silueta. **El cerco del cero-enlazados esta cerrado**, y la unica marca que queda es la `D.2` del `474`, que es marca y no encargo.
4. **LA 215 ES LA VUELTA DE BATERIA**, por la cadencia de cinco de `AUDITOR.md` 6.1. La 212 no lo es y su seccion 9 lo declara con su hueco medido.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 212 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V212_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: NADIE la corrio, y no por olvido: la 212 NO ES VUELTA DE BATERIA. La cadencia de cinco de AUDITOR.md 6.1 pone la siguiente en la 215, la 210 corrio la ultima con sus once tramos, y el encargo de esta vuelta lo escribe con todas las letras.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
