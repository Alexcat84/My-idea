# REPORTE DE LA VUELTA 216 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v216_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 215.**
> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **CUATRO TAREAS, Y LA 216 NO ES VUELTA DE BATERIA Y NO LA CORRE.** La 215 la
> corrio entera y el auditor la declaro CORRIDA en su adjudicacion 5.1; la
> cadencia de cinco de `AUDITOR.md` 6.1 pone la siguiente en la **220**. La
> seccion 9 de este reporte cierra por tanto con el **HUECO DECLARADO Y MEDIDO**
> por el carril de la TAREA 1.b de la vuelta 173, que es lo que la 6.1 manda en
> las vueltas intermedias. **El tope de sub-tareas es CINCO** (acta 212,
> adjudicacion 6.8, **linea 75168** de `docs/loop/ACTA_AUDITOR.md`, leida en esta
> vuelta), y **estas cuatro no lo agotan porque el encargo dice que no hacen
> falta mas**.
>
> **ESTA VUELTA CORRE LA UNICA COSA QUE LE QUEDA AL PLAN, Y NO ES DEL AUDITOR: LA
> ORDENO EL FUNDADOR.** Su sede es
> `docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, DECISION 2, y su letra
> verbatim es *"las cinco fichas SIN EJECUTAR se re-miden contra esas filas
> (OP-V-01 con su prueba por cita de la corrida K ya escrita)"*. **La re-medicion
> es la TAREA 2 y es bloqueante.**
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado: **las cuatro tareas son MEDICION y
> VERIFICACION**, que es lo que la moratoria protege. Todo lo que esta vuelta
> escribe en el arbol scripts/loop (**sin comillas inversas, por la obligacion del
> 6.2 del acta 212**) son ficheros `_v216_*` **con prefijo de guion bajo, fuera
> del censo y fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se
> poda.
>
> **Y RIGE LA PROHIBICION QUE NO SE NEGOCIA: NINGUNA TAREA DE ESTA VUELTA MUEVE EL
> CAMPO DE ESTADO DE NINGUNA FICHA.** La vara del trabajo pendiente es el
> instrumento y nunca ese campo (recuadro de `AUDITOR.md` 0, decision del fundador
> del 4 sep 2026). Se mide, se publica y se dice. **No se escribe.**
>
> **RIGE LA OBLIGACION DE DICTADO DEL 6.6 DEL ACTA 210:** toda cita de un acta
> anterior lleva **LA LINEA** de `docs/loop/ACTA_AUDITOR.md` donde vive el texto
> citado, **y la linea se LEE, no se recuerda**.
>
> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado
> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.
>
> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO DEL ACTA 212, LAS TRES SIN CODIGO:**
> ningun reporte cita un directorio a secas como ruta entre comillas inversas
> (adjudicacion 6.2); una seccion suplementaria va detras de la que amplia y nunca
> detras de una mayor (hallazgo 7.1); y el tallador de cabecera corrido en la
> apertura escribe en un nombre con `_RECHAZO`, no en el del cierre.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V216_APERTURA.txt`,
> `docs/loop/SALIDA_V216_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre. **Y el remedio de la
> 215 se mantiene y no se afloja: el ciclo SELLA SU PROPIA CONSOLA en
> `docs/loop/SALIDA_V216_CICLO_GATE0_APERTURA_CONSOLA.txt`, que es el nombre
> exacto que el compositor busca, y cae en rojo por sus dos puertas, la del
> fichero ausente y la del fichero de cero bytes.**

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 216`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, Y VA PRIMERA PORQUE LAS DEMAS SE APOYAN EN ELLA. Leer el acta de la vuelta 215 en `docs/loop/ACTA_AUDITOR.md`, sus secciones 3, 5 y 6, y REGISTRAR LAS OCHO ADJUDICACIONES DE LA 5.1 A LA 5.8 CON LA LINEA DE DONDE SALE CADA UNA, leida con un instrumento y no tecleada; las cuatro que obligan van con DOS COLUMNAS SEPARADAS, el titulo VERBATIM y la lectura mia. Y registrar las DOS CORRECCIONES DECLARADAS del auditor con su cifra, y su UNICA CIFRA MALA, que es suya y se escribe igual | **CERRADA** | `SALIDA_V216_T1_REGISTROS.txt` (8 adjudicaciones, 4 hallazgos, 3 anclajes y 5 puntos de la seccion 6, cada uno con su linea leida), `SALIDA_V216_T1_MUTANTES.txt` (9 de 9 caen, texto bueno en 0 fallos), `SALIDA_V216_COMPOSITOR_T1.txt` |
| **TAREA 2** | LA RE-MEDICION QUE EL FUNDADOR ORDENO EL 9 SEP 2026, Y ES EL CORAZON DE ESTA VUELTA Y ES BLOQUEANTE. Sacar CON UN INSTRUMENTO las clausulas de las CATORCE filas de derivacion de `docs/plan/08_VERIFICACION.md`, publicar cuantas filas se armaron y cuantas deberia haber EN LA MISMA LINEA, y medir cada una con su busqueda corrida y su cifra delante, incluidas las que dan cero. La ficha OP-V-01 tiene trato propio por la DECISION 2: su prueba va POR CITA DE LA CORRIDA K YA ESCRITA, y si no aparece, ESO TAMBIEN ES UN RESULTADO. Y el caso rojo se prueba POR MUTACION, en memoria y sin escribir en ninguna ficha | **CERRADA, 13 DE 14 EN CUBRE Y LA QUE FALTA DICHA CON SU CIFRA** | `SALIDA_V216_T2_REMEDICION.txt` (14 filas armadas de 14, 0 descuadres contra su sede, 13 CUBRE y 1 A MEDIAS, 14 de 14 mutantes rotos caen y 1 de 1 mutante sano sube), `SALIDA_V216_COMPOSITOR_T2.txt` |
| **TAREA 3** | LA CONSECUENCIA, MEDIDA Y SIN TOCAR UN SOLO CAMPO DE ESTADO. Publicar ficha por ficha cuantas clausulas quedan en CUBRE para las CINCO; volver a correr la vara `scripts/loop/vuelta150_3_relectura_expediente.py` con el hash de MI apertura y publicar MI cifra sin copiar la del auditor; PUBLICAR LAS DOS VARAS LADO A LADO sin maquillar que miden cosas distintas; y PROPONER, no declarar, si la campana queda consumada en lo que el bucle puede consumar | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 4** | EL CIERRE INTEGRAL Y EL REPORTE. El ciclo entero de Gate 0 por los dos lados con su consola SELLADA desde dentro del propio instrumento, manteniendo el remedio de la 215 y sin aflojarlo; las tres suites solas con su exitcode y sus bytes; marcador y censo recomputados cada uno con su comando; las rutas con `scripts/loop/vuelta186_rutas_del_reporte.py` corrido DESPUES de cerrar el reporte; la cabecera con su tallador y su comparacion; y el cierre con `scripts/loop/cerrar_reporte.py`, que con la 215 hacen dos seguidas | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS, Y LA LINEA DE CADA UNO LEIDA HOY

**LA FUENTE ES EL ACTA Y EL LECTOR ES UN INSTRUMENTO.**
`scripts/loop/_v216_t1_registros.py` abre `docs/loop/ACTA_AUDITOR.md`
(**76686** lineas hoy), localiza el acta de la vuelta 215 por su
cabecera en la **linea 76240**, y saca sus entradas numeradas con
`enumerate()`. **NINGUN NUMERO DE LINEA DE ESTA SECCION SE TECLEA**, que es lo
que manda el 6.6 del acta 210, la letra de `EJECUTOR.md` 1 y la orden literal
del encargo. El instrumento halla **14** entradas numeradas en el acta
entera, de ellas **8** adjudicaciones y **4** hallazgos.

#### 1.a. LAS CUATRO ADJUDICACIONES QUE ME OBLIGAN, CON SU TITULO VERBATIM Y CON MI LECTURA APARTE

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T1_REGISTROS.txt`: 4. FILAS QUE DEBERIA HABER,
CONTADAS POR EL PROPIO INSTRUMENTO SOBRE EL ACTA: 4.** **LAS DOS SE ESCRIBEN
JUNTAS**, por la obligacion de las filas.

**LAS DOS COLUMNAS SON DE AUTORES DISTINTOS Y POR ESO VAN SEPARADAS:** la de
TITULO es del auditor y sale del acta por instrumento, verbatim; la de QUE ME
OBLIGA **es lectura mia del encargo** y no la sostiene ningun instrumento.

| adjudicacion | linea del acta | titulo, VERBATIM del acta (AUTOR: EL AUDITOR) | que me obliga a hacer en esta vuelta (LECTURA MIA) |
|---|---:|---|---|
| **`5.1`** | **76559** | LA BATERIA DE LA VUELTA 215 ESTA CORRIDA. ADJUDICADO, Y RESPONDE SU PREGUNTA 1. | NO CORRO LA BATERIA. Esta declarada CORRIDA por la 215 con sus once tramos y sus 135 entradas contadas por el auditor, y la cadencia de cinco de `AUDITOR.md` 6.1 pone la siguiente en la **220**. Mi seccion 9 cierra con el HUECO DECLARADO Y MEDIDO por el carril de la TAREA 1.b de la vuelta 173, con su medicion, su atribucion y su corrida. |
| **`5.2`** | **76573** | LA PARADA 2 ES UNA CONTRADICCION REAL Y MEDIDA, PERO NO ES PARADA, Y DOY LA REGLA QUE LA RESUELVE. | NO TOCO EL LANZADOR DE LA BATERIA Y NO PROPONGO PODA. El rojo estructural queda COMO ESTA IMPRESO: mide la vara 148, que es una regla escrita dentro de un script, y el fundador la tiene suspendida por la moratoria. La poda se decide en la auditoria integral y no antes, y por tanto la nomina sigue CONGELADA EN 135. |
| **`5.4`** | **76590** | SU PENDIENTE DE DOCTRINA 1 NO ES DOCTRINA NUEVA: EL FUNDADOR YA LO DECIDIO HOY, Y LO CITO POR SU RUTA. | DOY `OP-I-01` POR CERRADA POR LA DECISION 1 DEL FUNDADOR, y su punto 4 sube NOMBRADO sin bloquear. No relleno ese hueco y no muevo su campo de estado: lo mido, lo publico y lo digo. |
| **`5.7`** | **76617** | SU PREGUNTA 2, LAS CUATRO FICHAS EN HECHA SIN NINGUNA PRUEBA: NO BLOQUEAN, PERO TAMPOCO ESTAN CERRADAS, Y EL TRABAJO QUE LAS CIERRA YA ESTA ORDENADO. | CORRO LA RE-MEDICION DE LAS CINCO FICHAS CONTRA LAS CATORCE FILAS, y es mi TAREA 2 y es BLOQUEANTE. La ordeno el fundador el 9 sep 2026 en la DECISION 2 y no la ha corrido nadie. |

#### 1.a.bis. LAS OTRAS CUATRO, REGISTRADAS IGUAL PORQUE EL ENCARGO MANDA REGISTRAR LAS OCHO

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T1_REGISTROS.txt`: 4. FILAS QUE DEBERIA HABER:
4.** **8 filas de adjudicacion leidas en total, contra las
8 que el instrumento cuenta sobre el acta.**

| adjudicacion | linea del acta | titulo, VERBATIM del acta (AUTOR: EL AUDITOR) | lo que deja registrado (LECTURA MIA) |
|---|---:|---|---|
| **`5.3`** | **76585** | LA PARADA 1, LOS SIETE ARNESES QUE CAEN: REGISTRADA, NO REPARADA, Y SUBE NOMBRADA. ADJUDICADO A FAVOR DEL EJECUTOR. | REGISTRADA, y no me da orden nueva: confirma que no tocar los siete arneses fue lo correcto y los manda NOMBRADOS a la auditoria integral. Esta vuelta tampoco los toca. |
| **`5.5`** | **76599** | EL PUNTO 3 SE MUEVE A CUBRE. ADJUDICADO A FAVOR DEL EJECUTOR, Y RESPONDE SU DISCUTIBLE `D.d`. | REGISTRADA, y cierra a mi favor el punto 3 y mis discutibles `D.a`, `D.b` y `D.d` de la 215. No me da orden nueva. |
| **`5.6`** | **76610** | SU `D.c`, CORRER LOS ONCE TRAMOS CON EL PRIMERO EN ROJO, VA A SU FAVOR. | REGISTRADA, y cierra a mi favor mi discutible `D.c` de la 215 sobre correr los once tramos con el primero en rojo. No me da orden nueva. |
| **`5.8`** | **76628** | LE ABONO SU DISCREPANCIA DECLARADA DE LA TAREA 3, Y CORRIJO POR DECLARACION UNA CIFRA DE MI ANTECESOR. | REGISTRADA, y es ADEMAS una de las dos correcciones declaradas que la 1.b me manda escribir con su cifra. No me da orden nueva. |

#### 1.b. LAS DOS CORRECCIONES DECLARADAS DEL AUDITOR, CADA UNA CON SU CIFRA

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T1_REGISTROS.txt`: 3. FILAS QUE DEBERIA HABER:
3** (las dos correcciones de la 1.b **mas** la cifra mala de la 1.c, que el
mismo instrumento ancla). **Las tres se localizan POR SU TEXTO dentro del acta y
se exige que aparezcan UNA sola vez, o el instrumento cae en rojo.**

| lo que ancla | linea del acta | la linea del acta, VERBATIM |
|---|---:|---|
| CORRECCION 1 (su 5.8): las fichas en HECHA SIN NINGUNA PRUEBA son CUATRO | **76630** | prueba, `OP-V-01` y `OP-L-01`. **Medido hoy por mi con la misma vara y con los dos cortes: |
| CORRECCION 2 (su 3.1): mi racha de caida de reporte VUELVE A CERO | **76508** | **CONSECUENCIA REGLADA: SU RACHA DE CAIDA DE REPORTE, QUE LA 214 DEJO EN UNO, VUELVE A |
| SU UNICA CIFRA MALA, QUE ES SUYA (su seccion 7) | **76673** | fundador. Y una cifra mia que no adorno: mi ciega sale 67 de 80.** |

**CORRECCION 1, CON SU CIFRA: LAS FICHAS EN HECHA SIN NINGUNA PRUEBA SON
CUATRO, NO DOS.** Su `5.8` corrige por declaracion una cifra de su antecesor: el
acta 214, en su `5.9`, nombraba **DOS** (`OP-V-01` y `OP-L-01`), y medido hoy
por el con la misma vara y con los dos cortes **son CUATRO**: `OP-V-01`,
`OP-L-01`, `OP-L-02` y `OP-L-03`. **La cifra vieja no se retira y no era falsa:
nombraba dos de las cuatro sin afirmar que fueran solo dos.**

**CORRECCION 2, CON SU CIFRA: MI RACHA DE CAIDA DE REPORTE VUELVE A CERO.** Su
`3.1` mide **0 cifras mias que no calcen con las suyas**, y por la letra que el
acta 203 cita en su linea **71534** (*"sin caida que acumule rompe la racha"*)
**la racha que la 214 dejo en UNO vuelve a CERO**. **No arrastro ninguna**, y
por tanto **no hay escalada del tallador que encargar**, porque la racha no
llego a dos.

#### 1.c. LA UNICA CIFRA MALA DEL ACTA, QUE ES DEL AUDITOR, Y SE ESCRIBE IGUAL

**SU RELECTURA CIEGA SALE 67 DE 80** (acta de la 215, **linea 76673**,
verbatim: *"Y una cifra mia que no adorno: mi ciega sale 67 de 80."*).

**NO ME TOCA HACER NADA CON ELLA Y NO LA DISCUTO**, que es exactamente lo que el
encargo dice. **Me toca que quede escrita**, y queda: **el registro de una vuelta
no es el escaparate de nadie**, y una vuelta que solo publica las cifras malas
del otro es la misma especie de verde que esta casa lleva doscientas vueltas
cazando.

#### 1.d. LA SECCION 6 DEL ACTA, LO QUE SUBE A LA AUDITORIA INTEGRAL

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T1_REGISTROS.txt`: 5. FILAS QUE DEBERIA HABER,
CONTADAS POR EL INSTRUMENTO: 5.** Se registra aqui porque **es la sede a
la que mi TAREA 3 remite lo que el bucle no puede cerrar**, y porque el encargo
manda leer tambien la seccion 6.

| punto | linea del acta | lo que sube, VERBATIM del acta |
|---:|---:|---|
| **1** | **76640** | **LA CONTRADICCION DE LA NOMINA.** Vara 148 contra moratoria `6.3`. **Dos arneses fuera: |
| **2** | **76644** | **LOS SIETE ARNESES QUE NO MUERDEN**, nombrados en mi tabla de la seccion 1, **cayendo |
| **3** | **76646** | **EL PUNTO 4 DE `OP-I-01`**, A MEDIAS, **con su sede medida y no encontrada: 0 ficheros |
| **4** | **76648** | **LA ORDEN QUE NO SE PUEDE CUMPLIR SIN ROMPERLA LA PRIMERA VEZ** (mi `0.2`): *"tu comando |
| **5** | **76652** | **SI UN ROTULO DE COMANDO CUENTA COMO CIFRA PUBLICADA** (mi `3.2`). Hoy no cuenta, y por |

#### 1.e. LA GUARDA DE ESTA TAREA, PROBADA POR MUTACION Y NO PROMETIDA

**`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION.** El juicio vive en una
funcion pura, `juzgar()`, y `scripts/loop/_v216_t1_mutantes.py` **le da de
comer listas rotas sin tocar el acta ni un byte**.

**CIFRA fallos del texto bueno: 0** (se exigen 0). **CIFRA mutantes:
9 | CIFRA mutantes que CAEN: 9.** Contadas de
`docs/loop/SALIDA_V216_T1_MUTANTES.txt`. Los nueve rompen una cosa cada uno: falta una adjudicacion,
falta una de las cuatro que obligan, una etiqueta renumerada, una adjudicacion
de mas, falta un hallazgo, un anclaje que no aparece, un anclaje que aparece dos
veces (que es cita ambigua), la seccion 6 sin puntos, y todo vacio.

### TAREA 2. LA RE-MEDICION QUE EL FUNDADOR ORDENO, CORRIDA Y CON SU CIFRA DELANTE

**QUIEN LA ORDENA, POR SU RUTA Y NO DE MEMORIA:**
`docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, **DECISION 2**,
verbatim: *"las cinco fichas SIN EJECUTAR se re-miden contra esas filas (OP-V-01
con su prueba por cita de la corrida K ya escrita)"*. El instrumento es
`scripts/loop/_v216_t2_remedicion.py` y su salida sellada es
`docs/loop/SALIDA_V216_T2_REMEDICION.txt`.

#### 2.a. LAS CATORCE FILAS, SACADAS CON UN INSTRUMENTO Y COTEJADAS CONTRA SU SEDE

**FILAS ARMADAS LEYENDO LA TABLA DE DERIVACION DE `docs/plan/08_VERIFICACION.md`
(947 lineas hoy): 14. FILAS QUE DEBERIA HABER: 14.** **LAS
DOS SE ESCRIBEN JUNTAS**, y si el instrumento hubiera sacado otro numero
**habria parado**, que es lo que el encargo manda.

**Y NO BASTA CON CONTARLAS: CADA FILA SE COTEJA CONTRA SU SEDE.** El instrumento
abre `docs/plan/OPERACIONES.jsonl`, va a la linea que la fila declara, saca la
clausula del indice que la fila declara y **compara el texto VERBATIM**.
**CIFRA filas que NO calzan con su sede: 0** (se exigen 0).

**LAS CORRECCIONES DECLARADAS NO ENTRAN COMO FILAS**, que es lo que el registro
`R.72` del acta 208 adjudico y lo que la propia tabla hace listandolas aparte.
**PERO SI SE LEEN, Y LO DIGO PORQUE ES UNA DECISION MIA:** la tabla trae una
columna que dice, fila por fila, **que correccion corrige que clausula**
(**CIFRA filas que la tabla declara corregidas: 4**), y una
clausula corregida se mide **por su lectura corregida**. Leer la correccion no
es medirla.

#### 2.b. LAS CATORCE, MEDIDAS UNA POR UNA, CON LA BUSQUEDA CORRIDA Y SU CIFRA DELANTE

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T2_REMEDICION.txt`: 14. FILAS QUE DEBERIA HABER:
14.** Ninguna celda de veredicto se teclea: todas se leen de esa salida.

| # | ficha | indice | linea del expediente | la clausula, VERBATIM | veredicto medido hoy |
|---:|---|---:|---:|---|---|
| **1** | `OP-V-01` | 8 | 34 | TRANSVERSAL: Gate 0 verde, suite verde, vuelo completo, prueba de rumbos, y reindexado semantico DESPUES de mover ids | **CUBRE** |
| **2** | `OP-L-01` | 0 | 41 | ninguna de las once aparece en INTRA_DOMINIO_VEREDICTOS.jsonl: viven solo aqui | **CUBRE** |
| **3** | `OP-L-01` | 1 | 41 | el marcador del cribado no se mueve: sigue en 2.117 | **CUBRE** |
| **4** | `OP-L-01` | 2 | 41 | cada nomina afectada se re-mide con su cobertura al lado (banco 9.26) | **CUBRE** |
| **5** | `OP-L-02` | 0 | 42 | las tres nominas afectadas quedan con cobertura COMPLETA y su forma reescrita | **CUBRE** |
| **6** | `OP-L-02` | 1 | 42 | el marcador del cribado no se mueve: sigue en 2.117 | **CUBRE** |
| **7** | `OP-L-02` | 2 | 42 | cada grupo del backlog lleva su motivo escrito, no solo su cuenta | **CUBRE** |
| **8** | `OP-L-03` | 0 | 43 | ningun acto se funde con un par interno sin veredicto | **CUBRE** |
| **9** | `OP-L-03` | 1 | 43 | las 55 lecturas marcadas LECTURA DIRIGIDA: no entran en la cola ni mueven su marcador | **CUBRE** |
| **10** | `OP-L-03` | 2 | 43 | cada acto cuya lectura completa cambie su forma se re-mide con su cobertura al lado | **CUBRE** |
| **11** | `OP-I-01` | 0 | 44 | toda entrada lleva su fecha_corte | **CUBRE** |
| **12** | `OP-I-01` | 1 | 44 | toda forma con cobertura incompleta va marcada PROVISIONAL | **CUBRE** |
| **13** | `OP-I-01` | 2 | 44 | todo hueco va NOMBRADO, nunca rellenado | **CUBRE** |
| **14** | `OP-I-01` | 3 | 44 | el inventario se recomputa entero con el disparador de 08_VERIFICACION | **A MEDIAS** |

**EL REPARTO: CIFRA en CUBRE 13 | CIFRA en A MEDIAS 1 | CIFRA en
NO CUBRE 0 | CIFRA sin sonda 0 | CIFRA medidas 14
de 14.**

**LO QUE ESTA VUELTA ANADE SOBRE LA 214, DICHO CON SU CIFRA Y NO COMO MERITO:**
la 214 dejo **6 de las catorce SIN VEREDICTO MECANICO** y
**2 en NO CALZA LEIDA A LA LETRA**, declaradas documentales o
pendientes de doctrina. **Aqui las catorce llevan sonda corrida, y las que dan
cero publican su cero con el comando delante**, que es lo que la `5.4` del acta
214 autoriza: **lo prohibido es afirmar una busqueda NO corrida, no publicar la
que da cero.**

#### 2.c. `OP-V-01` POR CITA DE LA CORRIDA K, QUE SE BUSCO Y SE ENCONTRO

**LA CORRIDA K EXISTE.** Ruta
`docs/loop/SALIDA_SESION_CREDENCIAL_VUELO_K.txt`, **63756 bytes exactos**
y **788 lineas**, medidos hoy. **No se vuelve a producir: se cita**,
que es lo que la DECISION 2 manda.

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T2_REMEDICION.txt`: 5. FILAS QUE DEBERIA HABER: 5**
(las cinco partes de la clausula transversal). **CIFRA partes sostenidas por
cita: 5 de 5.**

| # | parte de la clausula | marca con la que se busca | linea(s) en la corrida K | linea(s) en el commit `e966d896` | sostenida |
|---:|---|---|---|---|---|
| 1 | Gate 0 verde | `GATE 0 VERDE` | ninguna | [8] | **SI** |
| 2 | suite verde | `motor 25/25` | ninguna | [12] | **SI** |
| 3 | vuelo completo | `16 de 16 o 16/16` | [7, 784] | [1, 13] | **SI** |
| 4 | prueba de rumbos | `PRUEBA DE RUMBOS` | ninguna | [15] | **SI** |
| 5 | reindexado semantico DESPUES de mover ids | `d70adc1d` | ninguna | [18] | **SI** |

**Y AQUI VA UNA PRECISION QUE NO ME FAVORECE Y LA ESCRIBO IGUAL:** el fichero de
la corrida K sostiene **por si solo** la parte del vuelo completo; **las otras
cuatro las sostiene el cuerpo del commit `e966d896`**, que es el que movio el
estado de la ficha y el que sello la corrida K. **Son dos sedes y no una, y
decir "la corrida K las sostiene todas" seria mentir por omision.**

#### 2.d. EL CASO ROJO NO SE PROMETE, SE PRUEBA POR MUTACION

**El mutante se fabrica EN MEMORIA, sobre una copia profunda de los datos, y no
se escribe en ninguna ficha.** **CIFRA mutantes rotos: 14 | CIFRA que
CAEN, o sea que dejan de decir CUBRE: 14.**

**Y EL REVERSO, PORQUE UNA SONDA QUE NUNCA PUEDE DECIR CUBRE TAMPOCO MIDE:** la
clausula que hoy no da CUBRE se prueba ademas con un mutante **SANO**, y tiene
que SUBIR. **CIFRA mutantes sanos: 1 | CIFRA que SUBEN a CUBRE:
1.**

#### 2.e. LA GUARDA: ESTA TAREA NO MOVIO NI UN CAMPO DE ESTADO

**`sha256` LF de `docs/plan/OPERACIONES.jsonl` al ENTRAR: `650578474361eb2b`. Al
SALIR: `650578474361eb2b`. Los dos CALZAN.** Y cero filas de
`git diff --numstat` sobre el expediente, el inventario, la vara y la pagina de
lecturas dirigidas.

#### 2.f. UNA DISCREPANCIA QUE DECLARO EN VEZ DE CALLARLA, Y NO ME FAVORECE DISCUTIRLA

**MI ENCARGO DICE, Y EL ACTA 215 EN SU `5.7` TAMBIEN, QUE LA RE-MEDICION NO LA
HA CORRIDO NADIE.** **Medido hoy por mi: existe
`docs/loop/SALIDA_V214_T2B_REMEDIR_CINCO.txt`, 14302 bytes, commit `bb2337a0`, y es una re-medicion
de las cinco fichas contra estas mismas catorce clausulas.**

**NO DISCUTO LA ADJUDICACION Y NO LA NECESITO PARA NADA, porque la orden se
cumple igual:** aquella re-medicion dejo **6 de catorce sin veredicto
mecanico** y **2 mas en NO CALZA LEIDA A LA LETRA**, o sea que
**ocho de las catorce se quedaron sin CUBRE, A MEDIAS ni NO CUBRE**. **La orden
del fundador pedia las catorce medidas, y esa parte NO estaba corrida.** Lo
publico porque `EJECUTOR.md` 2 dice que una discrepancia se declara y nunca se
resuelve copiando, **y porque el que la declara con su cifra soy yo y no el que
me audita.**

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

