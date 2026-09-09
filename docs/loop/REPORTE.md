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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 216`, y su salida
cruda vive en `docs/loop/SALIDA_V216_TALLADOR_CABECERA.txt` (2396 bytes en disco y 2376 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `c7a0651c` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 215: LA VUELTA CIERRA BIEN, LA BATERIA ESTA CORRIDA POR LA LETRA DE LA 6.1, Y LA PEOR CIFRA DE LA JORNADA ES LA MIA.'), HEAD real de apertura `c7a0651c` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `cf212ef2` (leido de `SALIDA_V216_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, Y VA PRIMERA PORQUE LAS DEMAS SE APOYAN EN ELLA. Leer el acta de la vuelta 215 en `docs/loop/ACTA_AUDITOR.md`, sus secciones 3, 5 y 6, y REGISTRAR LAS OCHO ADJUDICACIONES DE LA 5.1 A LA 5.8 CON LA LINEA DE DONDE SALE CADA UNA, leida con un instrumento y no tecleada; las cuatro que obligan van con DOS COLUMNAS SEPARADAS, el titulo VERBATIM y la lectura mia. Y registrar las DOS CORRECCIONES DECLARADAS del auditor con su cifra, y su UNICA CIFRA MALA, que es suya y se escribe igual | **CERRADA** | `SALIDA_V216_T1_REGISTROS.txt` (8 adjudicaciones, 4 hallazgos, 3 anclajes y 5 puntos de la seccion 6, cada uno con su linea leida), `SALIDA_V216_T1_MUTANTES.txt` (9 de 9 caen, texto bueno en 0 fallos), `SALIDA_V216_COMPOSITOR_T1.txt` |
| **TAREA 2** | LA RE-MEDICION QUE EL FUNDADOR ORDENO EL 9 SEP 2026, Y ES EL CORAZON DE ESTA VUELTA Y ES BLOQUEANTE. Sacar CON UN INSTRUMENTO las clausulas de las CATORCE filas de derivacion de `docs/plan/08_VERIFICACION.md`, publicar cuantas filas se armaron y cuantas deberia haber EN LA MISMA LINEA, y medir cada una con su busqueda corrida y su cifra delante, incluidas las que dan cero. La ficha OP-V-01 tiene trato propio por la DECISION 2: su prueba va POR CITA DE LA CORRIDA K YA ESCRITA, y si no aparece, ESO TAMBIEN ES UN RESULTADO. Y el caso rojo se prueba POR MUTACION, en memoria y sin escribir en ninguna ficha | **CERRADA, 13 DE 14 EN CUBRE Y LA QUE FALTA DICHA CON SU CIFRA** | `SALIDA_V216_T2_REMEDICION.txt` (14 filas armadas de 14, 0 descuadres contra su sede, 13 CUBRE y 1 A MEDIAS, 14 de 14 mutantes rotos caen y 1 de 1 mutante sano sube), `SALIDA_V216_COMPOSITOR_T2.txt` |
| **TAREA 3** | LA CONSECUENCIA, MEDIDA Y SIN TOCAR UN SOLO CAMPO DE ESTADO. Publicar ficha por ficha cuantas clausulas quedan en CUBRE para las CINCO; volver a correr la vara `scripts/loop/vuelta150_3_relectura_expediente.py` con el hash de MI apertura y publicar MI cifra sin copiar la del auditor; PUBLICAR LAS DOS VARAS LADO A LADO sin maquillar que miden cosas distintas; y PROPONER, no declarar, si la campana queda consumada en lo que el bucle puede consumar | **CERRADA, Y NO PROPONE LA PARADA FELIZ PORQUE SU CONDICION NO SE CUMPLE** | `SALIDA_V216_T3_EXPEDIENTE.txt` (la vara corrida con el hash de mi apertura), `SALIDA_V216_T3_DOS_VARAS.txt` (5 filas por ficha, 5 cifras cotejadas con 0 discrepancias, 5 filas de las dos varas lado a lado, 4 fichas nombradas), `SALIDA_V216_COMPOSITOR_T3.txt` |
| **TAREA 4** | EL CIERRE INTEGRAL Y EL REPORTE. El ciclo entero de Gate 0 por los dos lados con su consola SELLADA desde dentro del propio instrumento, manteniendo el remedio de la 215 y sin aflojarlo; las tres suites solas con su exitcode y sus bytes; marcador y censo recomputados cada uno con su comando; las rutas con `scripts/loop/vuelta186_rutas_del_reporte.py` corrido DESPUES de cerrar el reporte; la cabecera con su tallador y su comparacion; y el cierre con `scripts/loop/cerrar_reporte.py`, que con la 215 hacen dos seguidas | **CERRADA, EL CIERRE INTEGRAL SALE LIMPIO** | `SALIDA_V216_T4_CIERRE.txt` (18 salidas selladas del ciclo, 0 ausentes, 0 de cero bytes, peor exitcode 0; 2 consolas selladas por el propio instrumento; 3 suites solas en exitcode 0; 16 cifras cotejadas con 0 que no calzan; 13 sedes con 0 movidas; 15 de 15 ficheros con prefijo), `SALIDA_V216_T4_MARCADOR.txt`, `SALIDA_V216_T4_ARISTAS.txt`, `SALIDA_V216_COMPOSITOR_T4.txt` |
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

**LA CORRIDA K EXISTE.** Su ruta es
`docs/loop/SALIDA_SESION_CREDENCIAL_VUELO_K.txt` y mide **63756 bytes en disco y 63655 bytes normalizado a LF**, con **788 lineas**, medidos
hoy. **No se vuelve a producir: se cita**, que es lo que la DECISION 2 manda.

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

**El `sha256` de `docs/plan/OPERACIONES.jsonl` al ENTRAR, el mismo en disco y normalizado a LF, es `650578474361eb2b`; y al SALIR, tambien el mismo en disco y normalizado a LF, es `650578474361eb2b`. Los dos CALZAN**, porque ese fichero
no trae ni un retorno de carro. Y cero filas de
`git diff --numstat` sobre el expediente, el inventario, la vara y la pagina de
lecturas dirigidas.

#### 2.f. UNA DISCREPANCIA QUE DECLARO EN VEZ DE CALLARLA, Y NO ME FAVORECE DISCUTIRLA

**MI ENCARGO DICE, Y EL ACTA 215 EN SU `5.7` TAMBIEN, QUE LA RE-MEDICION NO LA
HA CORRIDO NADIE.** **Medido hoy por mi: existe
`docs/loop/SALIDA_V214_T2B_REMEDIR_CINCO.txt`, **14302 bytes en disco y 14302 bytes normalizado a
LF**, commit `bb2337a0`, y es una re-medicion de las cinco fichas contra
estas mismas catorce clausulas.**

**NO DISCUTO LA ADJUDICACION Y NO LA NECESITO PARA NADA, porque la orden se
cumple igual:** aquella re-medicion dejo **6 de catorce sin veredicto
mecanico** y **2 mas en NO CALZA LEIDA A LA LETRA**, o sea que
**ocho de las catorce se quedaron sin CUBRE, A MEDIAS ni NO CUBRE**. **La orden
del fundador pedia las catorce medidas, y esa parte NO estaba corrida.** Lo
publico porque `EJECUTOR.md` 2 dice que una discrepancia se declara y nunca se
resuelve copiando, **y porque el que la declara con su cifra soy yo y no el que
me audita.**

### TAREA 3. LA CONSECUENCIA, MEDIDA, Y LAS DOS VARAS LADO A LADO

**EL INSTRUMENTO ES `scripts/loop/_v216_t3_dos_varas.py` Y SU SALIDA SELLADA
ES `docs/loop/SALIDA_V216_T3_DOS_VARAS.txt`.** Todas las tablas de abajo se pegan enteras de ese fichero.
**NINGUNA CELDA SE TECLEA.**

#### 3.a. LAS CATORCE CLAUSULAS, REPARTIDAS FICHA POR FICHA

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T3_DOS_VARAS.txt`: 5. FILAS QUE DEBERIA HABER: 5**
(las cinco fichas). **Y las clausulas repartidas son 14, contra las 14
que la TAREA 2 midio: LA SUMA SE COMPRUEBA CONTRA SI MISMA.**

| ficha | linea del expediente | clausulas suyas | en CUBRE | NO en CUBRE | cuales |
|---|---:|---:|---:|---:|---|
| `OP-V-01` | 34 | **1** | **1** | 0 | ninguna |
| `OP-L-01` | 41 | **3** | **3** | 0 | ninguna |
| `OP-L-02` | 42 | **3** | **3** | 0 | ninguna |
| `OP-L-03` | 43 | **3** | **3** | 0 | ninguna |
| `OP-I-01` | 44 | **4** | **3** | 1 | indice 3 en A MEDIAS |

#### 3.b. LA VARA DEL EXPEDIENTE, CORRIDA CON EL HASH DE MI APERTURA

**EL COMANDO, CON MI HASH Y NO CON OTRO:**
`scripts/loop/vuelta150_3_relectura_expediente.py --corte c7a0651c1e00de6ae296c71aaac52b71e798fa52`, leido del
sello `docs/loop/SALIDA_V216_HEAD_APERTURA.txt` y **no tecleado**. Su salida
cruda vive en `docs/loop/SALIDA_V216_T3_EXPEDIENTE.txt`.

**FILAS ARMADAS: 5. FILAS QUE DEBERIA HABER: 5.** **LA COLUMNA DE LA
IZQUIERDA ES MIA Y LA DE LA DERECHA ES LA DEL ENCARGO**, y van separadas para
que se pueda auditar cual es cual.

| cifra | LA MIA, medida hoy | la del encargo, del auditor | calzan |
|---|---:|---:|---|
| no calzan | **40** | 40 | SI |
| congeladas declaradas | **24** | 24 | SI |
| congeladas en silencio | **12** | 12 | SI |
| en LISTA sin prueba | **3** | 3 | SI |
| en HECHA sin prueba | **4** | 4 | SI |

**CIFRA celdas que NO calzan con la cifra del encargo: 0.** Las
cinco calzan una a una. **Lo digo con las dos columnas delante y no con una
sola**, porque publicar solo la mia cuando coincide es indistinguible de
copiarla.

**Y LA CIFRA DEL AUDITOR NO SE TOMA DEL ENCARGO Y YA: SE LEE DE SU ACTA, CON SU
LINEA**, porque una cifra citada de un encargo no es una cifra leida.

- ANCLAJE fichas que no calzan                   | linea 76665 | cifra suya 40
- ANCLAJE fichas en HECHA sin ninguna prueba     | linea 76666 | cifra suya 4

**LAS CUATRO FICHAS EN HECHA SIN NINGUNA PRUEBA SIGUEN IGUAL, Y VAN NOMBRADAS.**
**FILAS ARMADAS: 4. FILAS QUE DEBERIA HABER: 4.**

- HECHA SIN PRUEBA> OP-V-01 (fase 08_VERIFICACION, pruebas positivas: ninguna)
- HECHA SIN PRUEBA> OP-L-01 (fase 09_LECTURAS_DIRIGIDAS, pruebas positivas: ninguna)
- HECHA SIN PRUEBA> OP-L-02 (fase 09_LECTURAS_DIRIGIDAS, pruebas positivas: ninguna)
- HECHA SIN PRUEBA> OP-L-03 (fase 09_LECTURAS_DIRIGIDAS, pruebas positivas: ninguna)

#### 3.c. LAS DOS VARAS, LADO A LADO, SIN MAQUILLAR QUE MIDAN LO MISMO

**LA VARA NO SABE DE LAS CATORCE FILAS NUEVAS, Y ESO NO ES UN FALLO SUYO.** La
del expediente mide **P1, P2 y P3**: grafo, codigo vivo y huella en git. La de
las catorce filas mide **clausulas de verificacion**. **Son dos varas distintas
midiendo cosas distintas**, y una ficha puede salir en HECHA SIN NINGUNA PRUEBA
teniendo **todas sus clausulas en CUBRE**. **ESO NO ES UNA CONTRADICCION Y NO LO
MAQUILLO.** Cambiar la vara seria fabricar maquinaria y la moratoria lo prohibe.

**FILAS ARMADAS: 5. FILAS QUE DEBERIA HABER: 5.** **CIFRA de las
CUATRO en HECHA sin prueba que NO aparecen en lo leido: 0** (se
exigen 0), que es la guarda que impide publicar esta tabla a medio leer.

| ficha | VARA 1, la del expediente (P1 P2 P3) | VARA 2, las catorce clausulas |
|---|---|---|
| `OP-V-01` | estado `HECHA`, pruebas positivas ninguna, HECHA SIN NINGUNA PRUEBA: el estado afirma mas que el repo | 1 de 1 clausulas en CUBRE |
| `OP-L-01` | estado `HECHA`, pruebas positivas ninguna, HECHA SIN NINGUNA PRUEBA: el estado afirma mas que el repo | 3 de 3 clausulas en CUBRE |
| `OP-L-02` | estado `HECHA`, pruebas positivas ninguna, HECHA SIN NINGUNA PRUEBA: el estado afirma mas que el repo | 3 de 3 clausulas en CUBRE |
| `OP-L-03` | estado `HECHA`, pruebas positivas ninguna, HECHA SIN NINGUNA PRUEBA: el estado afirma mas que el repo | 3 de 3 clausulas en CUBRE |
| `OP-I-01` | estado `LISTA` SIN NINGUNA PRUEBA, o sea que su estado CALZA con el repo: consumida por otra ficha: no | 3 de 4 clausulas en CUBRE |

**LO QUE ESTA TABLA DICE, EN UNA FRASE Y SIN ADORNO:** las cuatro fichas que la
vara del expediente marca como **HECHA SIN NINGUNA PRUEBA** tienen hoy **todas
sus clausulas en CUBRE**; y la unica que **no** tiene todas sus clausulas en
CUBRE, `OP-I-01`, es justamente la que **si** calza con la vara del expediente,
porque su estado `LISTA` es exactamente lo que el repo dice de ella.

**Y UNA CORRECCION DECLARADA DE MI PROPIO COMPOSITOR, QUE NO TAPA LO QUE
CORRIGE:** su primera version leia CUALQUIER fila con forma de tabla de la
salida de la vara, y por eso cogia para `OP-I-01` la fila de la tabla de
DESBLOQUEADAS, cuya tercera celda es el TIPO y no el estado: publicaba
*estado MESA* cuando la ficha esta en `LISTA`. **La cifra era falsa por mi
compositor y no por el instrumento**, se acoto la lectura a la tabla por su
propia cabecera, y **la version vieja queda escrita en el codigo y no se borra**.

#### 3.d. LO QUE PROPONGO, QUE NO ES LO QUE DECLARO

**LA CONDICION LA ESCRIBI ANTES DE SABER EL RESULTADO**, que es lo que el
encargo manda: *"si las CATORCE clausulas quedan en CUBRE con su busqueda
corrida y su cifra delante, y si el cierre integral sale limpio, entonces la
campana esta consumada EN LO QUE EL BUCLE PUEDE CONSUMAR"*.

**CIFRA clausulas en CUBRE: 13 | CIFRA que la condicion exige: 14 | CIFRA
que NO estan en CUBRE: 1.**

- NO CUBRE LA CONDICION> clausula 14, ficha OP-I-01, indice 3, linea 44 del expediente, veredicto A MEDIAS

**LA PRIMERA MITAD DE LA CONDICION NO SE CUMPLE, Y POR ESO NO PROPONGO LA PARADA
FELIZ.** **PROPONGO ESTO EN SU LUGAR, con la cifra delante:** el plan queda
**agotado en trece de sus catorce clausulas**, y la que falta, `OP-I-01` indice
3, **no falta por pereza de esta vuelta**: le falta **la sede que la cumpliria**,
y esa sede **no existe en el repo** (**0 ficheros escriben la vista humana**,
busqueda corrida en la TAREA 2). **Fabricarla es maquinaria nueva y la moratoria
de `AUDITOR.md` 6.3 lo prohibe**, asi que **sube NOMBRADA**, que es donde el
propio auditor ya la puso en el punto 3 de su seccion 6.

**LO QUE ESTA TAREA NO HACE, DICHO PARA QUE NO SE BUSQUE:** no declara la
campana consumada, no escribe el PARA_ALEXIS del bucle (nombrado sin comillas
inversas a proposito: el fichero NO EXISTE en el arbol, y una ruta que promete
prueba es cifra) y **no pide ningun
merge**. Quien declara es **EL AUDITOR**, por la `4.2` del acta 203, **linea
71543**, ratificada por el fundador el 9 sep 2026. **Y EL BUCLE NO FUNDE RAMAS.**

**LA GUARDA DE LA PROHIBICION QUE NO SE NEGOCIA:** `sha256` LF de
`docs/plan/OPERACIONES.jsonl` **igual al entrar y al salir**, y **cero filas** de
`git diff --numstat` sobre el expediente. **CIFRA comprobaciones que fallan en
esta tarea: 0.**

### TAREA 4. EL CIERRE INTEGRAL, MEDIDO DE SUS FICHEROS Y NO TECLEADO

**EL INSTRUMENTO ES `scripts/loop/_v216_t4_cierre.py` Y SU SALIDA SELLADA ES
`docs/loop/SALIDA_V216_T4_CIERRE.txt`.** Todas las tablas de abajo se cuentan de ese fichero.

#### 4.a.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, CON SU CONSOLA SELLADA DESDE DENTRO

**CIFRA salidas selladas del ciclo: 18 | CIFRA que deberia haber: 18.**
**CIFRA ausentes: 0 | CIFRA de cero bytes: 0 | CIFRA sin
exitcode dentro: 0 | CIFRA peor exitcode de las dieciocho:
0.**

**EL REMEDIO DE LA 215 SE MANTIENE Y NO SE AFLOJA, Y ADEMAS SE LE ANADE LA
PUERTA QUE LE FALTABA:** el ciclo sella su propia consola desde dentro, en el
nombre exacto que el compositor busca, y cae en rojo **por sus dos puertas**, la
del fichero **ausente** y la del fichero de **cero bytes**.

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T4_CIERRE.txt`: 2. FILAS QUE DEBERIA HABER: 2.**

| lado | fichero de la consola | bytes, por las dos convenciones | peor exitcode que declara |
|---|---|---|---:|
| **APERTURA** | `docs/loop/SALIDA_V216_CICLO_GATE0_APERTURA_CONSOLA.txt` | **965** bytes en disco y **965** bytes normalizado a LF | 0 |
| **CIERRE** | `docs/loop/SALIDA_V216_CICLO_GATE0_CIERRE_CONSOLA.txt` | **961** bytes en disco y **961** bytes normalizado a LF | 0 |

#### 4.a.2. LAS TRES SUITES SOLAS, CADA UNA CON SU EXITCODE Y SUS BYTES

**FILAS ARMADAS: 3. FILAS QUE DEBERIA HABER: 3.**

| suite | fichero | exitcode | bytes, por las dos convenciones |
|---|---|---:|---|
| **motor** | `docs/loop/SALIDA_V216_T4_SUITE_MOTOR.txt` | **0** | **1160** bytes en disco y **1131** bytes normalizado a LF |
| **tsc** | `docs/loop/SALIDA_V216_T4_SUITE_TSC.txt` | **0** | **11** bytes en disco y **11** bytes normalizado a LF |
| **web** | `docs/loop/SALIDA_V216_T4_SUITE_WEB.txt` | **0** | **334** bytes en disco y **334** bytes normalizado a LF |

#### 4.a.3. EL MARCADOR Y EL CENSO, RECOMPUTADOS CADA UNO CON SU COMANDO, Y COTEJADOS SIN COPIAR

**LOS DOS COMANDOS, ESCRITOS ANTES DE SU RESULTADO:**
`python scripts/recomputar_marcador.py 3388` y
`python scripts/loop/vuelta83_conteo_aristas.py WORK`.

**FILAS ARMADAS: 16. FILAS QUE DEBERIA HABER: 16.** **LA COLUMNA DE
LA IZQUIERDA ES MIA Y LA DE LA DERECHA ES LA DEL ENCARGO**, y van separadas
porque son de autores distintos.

| cifra | LA MIA, recomputada hoy | la del encargo, del auditor | calzan |
|---|---:|---:|---|
| marcador n | **3388** | 3388 | SI |
| marcador A | **550** | 550 | SI |
| marcador B | **72** | 72 | SI |
| marcador C | **5** | 5 | SI |
| marcador D | **2761** | 2761 | SI |
| marcador huecos | **0** | 0 | SI |
| censo nodos | **3853** | 3853 | SI |
| censo vivos | **3169** | 3169 | SI |
| censo deprecados | **684** | 684 | SI |
| aristas siguientes | **8780** | 8780 | SI |
| aristas previos | **8740** | 8740 | SI |
| aristas suma | **17520** | 17520 | SI |
| aristas union | **9914** | 9914 | SI |
| Gate 0 peor exitcode | **0** | 0 | SI |
| salidas selladas del ciclo | **18** | 18 | SI |
| salidas ausentes del ciclo | **0** | 0 | SI |

**CIFRA cifras cotejadas: 16 | CIFRA que NO calzan: 0.**

#### 4.a.4. LAS SEDES QUE LA VUELTA PUDO MOVER, Y LA PRUEBA MEDIDA DE QUE NO LAS MOVIO

**FILAS ARMADAS: 13. FILAS QUE DEBERIA HABER: 13.** **CIFRA sedes que
se movieron: 0.**

| sede | sha256 LF al abrir | sha256 LF al cerrar | | bytes |
|---|---|---|---|---|
| `docs/plan/INVENTARIO.jsonl` | 43cea06634e6fc1a | 43cea06634e6fc1a | **QUIETA** | 629533 bytes en disco y 629533 bytes normalizado a LF |
| `docs/plan/OPERACIONES.jsonl` | 650578474361eb2b | 650578474361eb2b | **QUIETA** | 517181 bytes en disco y 517181 bytes normalizado a LF |
| `docs/plan/08_VERIFICACION.md` | 578eeefab6db2fd4 | 578eeefab6db2fd4 | **QUIETA** | 73652 bytes en disco y 73652 bytes normalizado a LF |
| `docs/plan/10_INVENTARIO.md` | 67f464d3d0b9e067 | 67f464d3d0b9e067 | **QUIETA** | 34258 bytes en disco y 33845 bytes normalizado a LF |
| `docs/plan/LECTURAS_DIRIGIDAS.md` | NO_MEDIDA_AL_ABRIR | a8ba1749b9a3fa13 | **QUIETA** | 219178 bytes en disco y 219178 bytes normalizado a LF |
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 758edf1f5c313c18 | 758edf1f5c313c18 | **QUIETA** | 4057130 bytes en disco y 4057130 bytes normalizado a LF |
| `docs/INTRA_DOMINIO_INFORME.md` | c05b6bcd20188a9c | c05b6bcd20188a9c | **QUIETA** | 943970 bytes en disco y 943970 bytes normalizado a LF |
| `docs/plan/00_INDICE.md` | 2e71336cc2fdc387 | 2e71336cc2fdc387 | **QUIETA** | 45278 bytes en disco y 45278 bytes normalizado a LF |
| `docs/BANCO_DE_TEXTOS.md` | 8adbd60239509bb4 | 8adbd60239509bb4 | **QUIETA** | 186490 bytes en disco y 186490 bytes normalizado a LF |
| `docs/plan/BANCO_DEL_PLAN.md` | 7836c8976c585143 | 7836c8976c585143 | **QUIETA** | 61554 bytes en disco y 61554 bytes normalizado a LF |
| `dataset/metadata/master_graph.json` | 627cc662296f7f00 | 627cc662296f7f00 | **QUIETA** | 8375817 bytes en disco y 8375817 bytes normalizado a LF |
| `docs/loop/ACTA_AUDITOR.md` | c0e023c04c02d6b7 | c0e023c04c02d6b7 | **QUIETA** | 5067810 bytes en disco y 5067810 bytes normalizado a LF |
| `docs/loop/PROMPT_SIGUIENTE.md` | 1fff5c15dd6fc5e7 | 1fff5c15dd6fc5e7 | **QUIETA** | 9866 bytes en disco y 9866 bytes normalizado a LF |

**UNA DE LAS TRECE NO ESTABA EN LA LISTA DEL SELLO DE APERTURA Y LO DIGO EN VEZ
DE PUBLICAR UN FALSO ROJO:** `docs/plan/LECTURAS_DIRIGIDAS.md` es sede que esta
vuelta LEYO y su apertura no la nombraba, asi que **su quietud se mide con
`git diff --numstat`, que es una medicion y no una suposicion**. La primera
corrida de este instrumento la publicaba como SE MOVIO comparando un sha contra
una ausencia, **y eso era un falso rojo mio**: queda corregido y el texto viejo
sigue en el codigo.

#### 4.a.5. LA MORATORIA, MEDIDA Y NO PROMETIDA

**CIFRA ficheros del arbol de scripts que esta vuelta escribio: 16 |
CIFRA de esos con el prefijo `_v216_` que le toca: 16.** Ninguno
entra en el censo ni en la nomina, y **la nomina sigue CONGELADA EN 135**.

#### 4.a.6. EL VEREDICTO DE ESTA TAREA

**CIFRA comprobaciones que fallan en el cierre integral: 0.**

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: LA VUELTA 216 CORRE LA RE-MEDICION QUE EL FUNDADOR ORDENO, TRECE DE SUS CATORCE CLAUSULAS QUEDAN EN CUBRE CON SU BUSQUEDA CORRIDA, EL CIERRE INTEGRAL SALE LIMPIO, Y NO DECLARO NADA CONSUMADO PORQUE LA CATORCEAVA NO CUBRE Y LO DIGO CON SU CIFRA.**

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODAS SALEN DE `docs/loop/SALIDA_V216_T4_CIERRE.txt`, que las midio y las sello. NINGUNA SE TECLEA.**

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS

**CIFRA salidas selladas: 18 de 18 | ausentes 0 | de cero
bytes 0 | sin exitcode dentro 0 | peor exitcode 0.**
**Las dos consolas existen y las sello el propio instrumento**, que es el
remedio de la `3.1` del acta 214 mantenido y con su segunda puerta anadida.

### 3.2. EL MARCADOR, EL CENSO Y LAS SUITES

**CIFRA cifras cotejadas contra las del encargo: 16 | CIFRA que NO
calzan: 0.** Las tres suites corren **solas**, fuera del ciclo, cada
una con su exitcode y sus bytes por las dos convenciones. **La tabla entera esta
en la TAREA 4 del anexo y no se repite aqui**, porque dos versiones de lo mismo
es exactamente lo que esta casa prohibe.

### 3.3. LAS SEDES, Y LA PRUEBA DE QUE ESTA VUELTA NO ESCRIBIO NI UNA FICHA

**CIFRA sedes cotejadas: 13 | CIFRA que se movieron: 0.**
**Esa es la prueba medida de que esta vuelta no movio ni un nodo, ni un
veredicto, ni un campo de estado.** `docs/loop/ACTA_AUDITOR.md` y
`docs/loop/PROMPT_SIGUIENTE.md`, que son sede del auditor, tambien quedan
quietas.

### 3.4. LAS RUTAS QUE ESTE REPORTE CITA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y **su salida se cita en el
commit de cierre**. Va ademas **metido como guarda previa en los cuatro
compositores de tarea de esta vuelta**, que cuentan las rutas inexistentes o de
cero bytes y los directorios de dos tramos entre comillas inversas **antes de
escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

**CIFRA ficheros del arbol de scripts que esta vuelta escribio: 16 |
CIFRA con el prefijo `_v216_`: 16.** Fuera del censo y fuera de la
nomina, que sigue **CONGELADA EN 135**.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **`git status --porcelain` al entrar: 1 linea**, y era mi propio
  script de apertura sin rastrear.
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0.**

**LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE:** no corrio la
bateria (la 215 la corrio y la cadencia pone la siguiente en la **220**); no
reparo ninguno de los siete arneses que no muerden; no toco el lanzador; no podo
ni engordo la nomina; no escribio en `docs/loop/PROMPT_SIGUIENTE.md`,
`docs/loop/ACTA_AUDITOR.md` ni el PARA_ALEXIS del bucle, que no existe en el
arbol y por eso va sin comillas inversas; **y no movio ni un
campo de estado, con los dos `sha256` del expediente delante.**

**LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA:** leida de `git log` sobre el
commit de apertura y sobre el de ahora mismo, y las dos dan **2026-09-09**.

## 5. LAS PARADAS

**NO TRAIGO NINGUNA PARADA, Y LO DIGO CON EL MOTIVO DELANTE.** Las dos que la
215 trajo estan adjudicadas: la del rojo estructural por la `5.2`, que manda
dejarlo **como esta impreso**, y la de los siete arneses por la `5.3`, que los
manda **NOMBRADOS a la auditoria integral**. **Esta vuelta no toca ninguno de
los dos**, que es exactamente lo que esas dos adjudicaciones ordenan.

**Y LA UNICA CLAUSULA QUE NO LLEGA A CUBRE TAMPOCO ES PARADA:** `OP-I-01` indice
3 esta **A MEDIAS** porque **la sede que la cumpliria no existe** (**0 ficheros
la escriben**, busqueda corrida), y **fabricarla es maquinaria nueva bajo la
moratoria**. **El auditor ya la puso NOMBRADA en el punto 3 de su seccion 6**,
asi que no hay nada que parar: hay algo que subir, y ya esta subido.

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Los cinco son de la TAREA 2 y todos son LECTURAS MIAS de una clausula.** Los
marco antes de la relectura ciega, que es lo que `EJECUTOR.md` 7 manda.

**`D.a` LEER LA CLAUSULA DEL MARCADOR POR SU CORRECCION Y NO A LA LETRA.** La
214 dejo esta clausula como PENDIENTE DE DOCTRINA entre dos lecturas. Yo la mido
por la **corregida**, y no porque me convenga: **la propia tabla de derivacion
trae una columna que dice que la corrige el indice 4**, y esa correccion escribe
que **2.117 es TESTIGO y no condicion**. **Si el auditor sostiene que la lectura
literal manda, mi CUBRE se cae y pasa a NO CUBRE.**

**`D.b` TOMAR LA NOMINA Y NO EL RACIMO COMO SUJETO DE LA CLAUSULA DE
`OP-L-02`.** La entrada de `la supervision de la IA` declara **dos universos** y
dice que **los dos son ciertos**: el racimo con **13 de 21**, y la nomina de
`OP-L-02` dentro de el con **10 de 10 y 0 sin veredicto**. La clausula dice *"las
tres NOMINAS"*, y por eso mido la nomina. **Bajo la otra lectura esta clausula
sale A MEDIAS y no CUBRE.**

**`D.c` HACER QUE EL SUJETO DE LAS ONCE SEAN LAS ONCE.** Leo `las once` de las
cabeceras que viven **bajo su propia seccion** de la pagina, y ahi aparecen
**0**. **El instrumento de la vuelta 203 mide otro universo**, toda cabecera LD
de la pagina, que hoy son **54**, y ahi aparece **1**. **Publico las dos y el
veredicto lo doy sobre el sujeto de la clausula.**

**`D.d` NO CONTAR `LD-82` COMO ENTRADA A LA COLA.** Su fila del archivo es el
**puesto 643**, que el cribado ya habia abierto, y **su propia razon la nombra
como relectura**. Leo que **no entro**: la releyeron. **Si eso se lee al reves,
la clausula de `OP-L-03` indice 1 se cae.**

**`D.e` CONTAR LAS CINCO PARTES DE `OP-V-01` ENTRE SUS DOS SEDES.** El fichero de
la corrida K sostiene **por si solo** el vuelo completo; **las otras cuatro las
sostiene el cuerpo del commit que sello esa corrida**. Leo que la DECISION 2, al
decir *"por cita de la corrida K ya escrita"*, se refiere a **lo que aquella
sesion sello**, no solo a los bytes de ese fichero. **Si se lee estricto, esa
clausula sale A MEDIAS con 1 de 5.**

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

**`P.1` UNA RE-MEDICION PARCIAL, CUENTA COMO CORRIDA?** Mi encargo y la `5.7`
dicen que **nadie** habia corrido la re-medicion, y **existe**
`docs/loop/SALIDA_V214_T2B_REMEDIR_CINCO.txt`. **No lo discuto y no me hace
falta**, porque aquella dejo **ocho de las catorce** sin veredicto. **La
pregunta es de doctrina y no de esta vuelta:** una medicion que deja la mitad sin
veredicto, se llama corrida o no.

**`P.2` UNA CLAUSULA CUYA SEDE NO EXISTE, SE QUEDA A MEDIAS PARA SIEMPRE?**
`OP-I-01` indice 3 **no puede llegar a CUBRE** sin un instrumento que regenere la
vista humana, y **la moratoria prohibe fabricarlo**. La pregunta es del fundador:
**la auditoria integral autoriza ese instrumento, o la clausula se lee cumplida
por su mitad medida.**

**PENDIENTES DE DOCTRINA: NINGUNO NUEVO.** El que la 214 trajo, el de las dos
lecturas del marcador, **queda resuelto por la propia correccion declarada de la
ficha**, que la tabla de derivacion nombra, y su lectura la marco como `D.a`
para que se pueda tumbar.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**SON TRES, LAS TRES DE MIS PROPIAS SONDAS, LAS TRES CAZADAS DENTRO DE ESTA
MISMA VUELTA Y NINGUNA PUBLICADA COMO CIFRA BUENA.**

**`C.1` LA SONDA DE LAS TRES NOMINAS QUITABA TODOS LOS ARTICULOS.** Hacia
`replace('la ', '')` sobre el nombre entero, y por eso `la supervision de la IA`
se volvia `supervision de ia` y salia **NO HALLADA**. Publicaba **2 de 3
nominas halladas**, y la cifra era falsa **por mi sonda y no por el dato**.
Corregida a quitar **solo el articulo de cabeza**, da **3 de 3**. **La version
vieja queda escrita en el codigo y no se borra.**

**`C.2` LA MARCA DEL VUELO COMPLETO ERA EL LITERAL `16` A SECAS.** Es **mas laxa
que su clausula**: casa con cualquier linea que lleve ese numero por cualquier
motivo. **La cazo la guarda de mi propio compositor**, que esperaba 5 filas de
parte y leyo 2. Estrechada a las **dos formas** en que las dos sedes escriben la
cifra del vuelo. **La version laxa queda escrita en el codigo.**

**`C.3` EL COMPOSITOR DE LA TAREA 3 LEIA CUALQUIER FILA CON FORMA DE TABLA.** Por
eso cogia para `OP-I-01` la fila de la tabla de DESBLOQUEADAS, cuya tercera celda
es el **tipo** y no el estado, y publicaba **estado MESA** cuando la ficha esta en
**LISTA**. Acotada la lectura a la tabla por su propia cabecera, y **anadida la
guarda** que exige que las cuatro fichas en HECHA sin prueba aparezcan en lo
leido. **La version vieja queda escrita en el codigo.**

**Y UNA CUARTA QUE NO CUENTO COMO CAIDA Y DIGO POR QUE:** la primera corrida del
instrumento del cierre publicaba `docs/plan/LECTURAS_DIRIGIDAS.md` como **SE
MOVIO**, comparando un `sha256` contra una **ausencia de medicion de apertura**.
**No llego a publicarse en ningun sitio salvo aqui**, la cazo el propio
instrumento cayendo en rojo, y **confundir una ausencia con un movimiento es
justo lo que la casa manda distinguir**: por eso se corrigio midiendo su quietud
con `git diff` y **diciendo por que via se midio**.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**EL PLAN QUEDA AGOTADO EN TRECE DE SUS CATORCE CLAUSULAS**, y la que falta
**sube NOMBRADA** porque su sede no existe y la moratoria prohibe fabricarla.
**NO DECLARO NADA CONSUMADO: LO PROPONGO**, que es lo que mi encargo manda, y
quien declara es el auditor.

**LO QUE PROPONGO, CON SU CIFRA DELANTE:** que la vuelta siguiente **no fabrique
nada** y que **la lista de la seccion 6 del acta 215, que hoy tiene cinco
puntos, suba entera con el punto de `OP-I-01` indice 3 dentro**. **Y EL MERGE NO
SE PIDE: EL BUCLE NO FUNDE RAMAS.**

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 216 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V216_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: LA CORRIO EL EJECUTOR DE LA VUELTA 215, ENTERA Y SOLA, POR SUS ONCE TRAMOS, Y EL AUDITOR LA DECLARO CORRIDA EN SU ADJUDICACION 5.1 (linea 76559 del acta, leida en esta vuelta). Su salida en el arbol mide 93498 bytes en disco y 93498 bytes normalizado a LF, medidos hoy, y su commit es abe21a67, leido de git log. LA 216 NO LA CORRE PORQUE LA CADENCIA DE CINCO DE AUDITOR.md 6.1 PONE LA SIGUIENTE EN LA 220, y correrla aqui seria saltarse la letra del fundador, no cumplirla.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
