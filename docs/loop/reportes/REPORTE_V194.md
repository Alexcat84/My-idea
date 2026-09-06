# REPORTE DE LA VUELTA 194 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta194_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA ES VUELTA DE BATERIA.** `AUDITOR.md` 6.1, decision del fundador del 5 sep
> 2026: la bateria corre **CADA CINCO VUELTAS** en una vuelta propia **que no lleva
> nada mas**, y **la 189 la corrio entera**. Por esa cadencia toca aqui. **La
> seccion 9 de este reporte NO cierra con hueco declarado: cierra con la bateria
> corrida**, por tramos, con su doble corrida, su reloj y su salida sellada.
>
> **VAN TRES SUB-TAREAS Y DOS SON BLOQUEANTES.** El tope de cinco sigue vigente y
> esta ganado, y **la cifra se conto del instrumento en esta vuelta**, no se heredo:
> el bloque `E` del sello de apertura corrio
> `scripts/loop/vuelta192_racha_de_cierres.py` sobre el inventario ENTERO. **Y
> la TAREA 2 no es trabajo de al lado: es la PRECONDICION de la bateria**, porque
> dos entradas de la nomina estan rotas de una forma que la bateria misma va a
> pisar, y por `AUDITOR.md` 6.1 unas salidas selladas no valen si una es de otra
> hondura que las demas.
>
> **EL DESFASE DE CALIBRADO SE MIDIO EN LA APERTURA**, dentro del bloque de
> apertura y **antes de la primera operacion**. Una columna de apertura medida al
> cierre es caida que ACUMULA, y esa fue la `C.1` que el acta 194 le puso al reporte
> de la 193.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina** (la opcion `c` que el fundador RECHAZO el
> 5 sep 2026: **la nomina sigue creciendo y nadie la poda sin el fundador**), ni
> ciegas nuevas: **es vuelta de bateria y no lleva trabajo de plan al lado**. **Y
> siguen fuera, nombradas para que la 195 no las redescubra:** la relectura al doble
> del tramo de la tanda del auditor, que es SU deuda de credito y la encarga el, y
> **va a la 195 con su tramo y su doble ya cerrados hoy**; el remedio del hallazgo
> `5.3` (los mensajes de commit del bucle **no publican clases por puesto ni el
> reparto de una ciega**, y eso empieza HOY aunque su guarda de codigo se encargue
> en la 195); el desfase de `PATRONES_ACTA`, **que el acta 193 dejo DESPUES de esta
> bateria y que la 195 recoge**; `acumulan()` que lea la tabla o declare que no es
> la sede; el cotejo de clon declarado que separa sentencia de codigo de cambio de
> texto; la excepcion que publica siempre su lista; la medicion del censo de arneses
> con carril de mutacion sin fichero propio; las ocho actas sin entrada propia en la
> serie (173 a 180); el exitcode 2 propagado a `--componer`; que el campo
> `evidencia` de `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE
> MUEVE: sigue en `LISTA`**; y **QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO**, que
> el acta 194 deja NOMBRADO y medido en su `4.8` y **no resuelto, porque mover una
> clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: LA VUELTA 194 CIERRA CON SUS TRES TAREAS Y CON LA BATERIA CORRIDA ENTERA POR SUS DIEZ TRAMOS, Y LA CORRIDA SALE EN ROJO EN LOS DIEZ POR SEIS ARNESES QUE LA NOMINA NO TIENE Y QUE NADIE PUEDE METER SIN EL FUNDADOR: los tres escenarios que el acta 194 midio rotos quedan invertidos y medidos, y el fallo de verdad no era el que el hallazgo nombraba.**
## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta194_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 193: `5b921750`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 193: LA 192 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA NI UNA RUTA VACIA (97 rutas barridas, 0 de cero bytes). SOY EL SEGUNDO LECTOR QUE SU REPORTE DECLARA IMPOSIBLE: mis 5 discrepancias son subconjunto exacto de sus 10, y el 1804 y el 2833 cayeron fuera del marcado de LOS DOS con el MISMO error. Adjudico los siete discutibles y las tres preguntas; la vara de las ciegas pasa a ser 9.6.1 por extension citable. TRES ARNESES NO REPRODUCEN Y ROMPEN LA BATERIA DE LA 194 SI NADIE LOS TOCA EN LA 193.'
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA, Y LLEVA SU FECHA DE CORTE.** La
  linea de arriba nombra el acta **193** porque `PATRONES_ACTA` pide la de
  `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la 194**. Es el `D.2` del
  reporte de la 184, adjudicado a favor con reparacion encargada por la `5.2` del
  acta 185, **y el acta 193 lo dejo expresamente DESPUES de la bateria de la 194:
  la 195 es el sitio, y el encargo de esta vuelta lo repite**. Lo que si se puede
  contar: **5 reportes archivados traen el literal `DESFASE DECLARADO`**
  (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`), contados por `reportes_con_el_literal()` de este mismo fichero,
  **con FECHA DE CORTE 2026-09-06** (banco `9.21`, TODA CIFRA DE CRUCE LLEVA SU
  FECHA DE CORTE). **Un inventario que crece cada vuelta sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V194_HEAD_APERTURA.txt`: `edff6568`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `d3e2c8f6`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **193**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 194`, y su salida
cruda vive en `docs/loop/SALIDA_V194_TALLADOR_CABECERA.txt` (2774 bytes en disco y 2754 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `5b921750` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 193: LA 192 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA NI UNA RUTA VACIA (97 rutas barridas, 0 de cero bytes). SOY EL SEGUNDO LECTOR QUE SU REPORTE DECLARA IMPOSIBLE: mis 5 discrepancias son subconjunto exacto de sus 10, y el 1804 y el 2833 cayeron fuera del marcado de LOS DOS con el MISMO error. Adjudico los siete discutibles y las tres preguntas; la vara de las ciegas pasa a ser 9.6.1 por extension citable. TRES ARNESES NO REPRODUCEN Y ROMPEN LA BATERIA DE LA 194 SI NADIE LOS TOCA EN LA 193.'), HEAD real de apertura `edff6568` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `56c2d085` (leido de `SALIDA_V194_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS TRES TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 194 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. Registra LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, las diez A FAVOR (siete son los discutibles `D.1` a `D.7` del reporte de la 193 y las tres restantes son las preguntas `P.1`, `P.2` y `P.3` contestadas por extension citable), CERO EN CONTRA y es la CUARTA acta seguida; LOS TRES HALLAZGOS DE LA SECCION 5 que no salen de ningun discutible (`5.1` los dos arneses de la cuarta puerta que se contradicen en la sede de verdad, `5.2` la seccion 8 que dice cuatro donde el instrumento dice cinco, `5.3` los mensajes de commit del bucle que queman la ciega del auditor antes de su primer comando); UNA CAIDA DEL EJECUTOR, DE REPORTE, QUE **SI ACUMULA** (el hallazgo `5.2`: vive solo en `REPORTE.md`, no mueve ningun dato y vive en una CONCLUSION, luego cuenta para la racha por la letra del 27 ago 2026; **RACHA DE REPORTE 1**, y no hay escalada que encargar porque se dispara a DOS); TRES CAIDAS DEL EJECUTOR DE METODO `C.1` a `C.3`, declaradas por el propio ejecutor en su seccion 8.1, que se registran y NO abren racha; DOS CAIDAS PROPIAS DEL AUDITOR, la primera grave (`C.1`, ROMPER UN REMEDIO ESCRITO, que CUENTA PARA LA PARADA por la letra del 5 sep 2026: el sello de la vuelta 194 SALIO ROJO y no existe) y la segunda de metodo (`C.2`, haber commiteado `docs/loop/_TURNO_DEL_AUDITOR.json`, que es estado de turno y no contenido de campana); y LA METRICA DE CREDITO de la seccion 7 con su fila de puestos y su nota: 30 aislados, 30 cotejados, ONCE QUEMADOS por el contexto de sesion y no por comando del auditor, y el cotejo publicado dos veces, sobre los 30 y sobre los 19 limpios. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues | **CERRADA, y con una discrepancia DENTRO del acta publicada y no resuelta copiando** | `SALIDA_V194_T1A_REGISTRO_R56.txt`, `SALIDA_V194_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, `SALIDA_V194_T1A_MUTACION_REGISTRADOR.txt`, `SALIDA_V194_T1A_SIMULACION.txt` |
| **TAREA 2** | LOS DOS ARNESES DE LA CUARTA PUERTA QUE SE CONTRADICEN. BLOQUEANTE, Y ES LA PRECONDICION DE LA BATERIA. Es el hallazgo `5.1` del acta 194, corrido y no deducido en `docs/loop/_auditor_v194_cuarta_puerta_rota.txt` con sus tres casos: `vuelta192_tarea4_mutacion_cuarta_puerta.py` llama a `AP.olvidar_todo()` OCHO veces contra el modulo REAL y nunca redirige `AP.RUTA_DEL_TURNO` a un temporal, asi que BORRA EL TURNO VIVO DEL AUDITOR en su sede de verdad y sale VERDE mientras lo hace; y el caso `H` de `vuelta193_tarea4e_mutacion_sello_entre_procesos.py` exige `os.path.exists(turno_real) == False`, o sea pide que NO haya auditor. En el orden alfabetico en que la bateria los corre, EL VERDE DEL SEGUNDO NO ES SUYO: se lo debe al primero. (a) QUE EL ARNES DE LA 192 NO TOQUE LA SEDE DE VERDAD, redirigiendo `AP.RUTA_DEL_TURNO` a un temporal antes de su primer `olvidar_todo()`. (b) QUE EL ARNES DE LA 193 DEJE DE EXIGIR QUE EL FICHERO NO EXISTA: que mida existencia, bytes y `sha256` ANTES y DESPUES y caiga si CAMBIA. (c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un arnes de la nomina modifica o borra `_TURNO_DEL_AUDITOR.json` en su sede de verdad, LANZANDO PROCESOS DE VERDAD. (d) QUE EL FICHERO DEL TURNO NO SE PUEDA VOLVER A COMMITEAR. (e) NO SE CLONA NINGUNO DE LOS DOS FICHEROS: se les anade. (f) NO SE TOCA LA NOMINA. (g) AL CERRAR, LOS DOS ARNESES EN LOS TRES ESCENARIOS DEL FICHERO DEL AUDITOR, CON LAS TRES SALIDAS PUBLICADAS; si el verde de alguno sigue dependiendo del orden, SE PARA Y SE TRAE | **CERRADA. Los TRES escenarios del auditor invertidos, y una premisa suya desmentida y publicada** | `SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt`, `SALIDA_V194_T2G_TRES_ESCENARIOS.txt`, y las dos selladas re selladas |
| **TAREA 3** | LA BATERIA, ENTERA Y POR TRAMOS. `AUDITOR.md` 6.1, literal: LA BATERIA CORRE POR TRAMOS OBLIGATORIOS, CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR, UNA VUELTA CORTADA RETOMA EN EL TRAMO SIGUIENTE, y LA BATERIA SE DECLARA CORRIDA CUANDO LOS TRAMOS TIENEN SALIDA SELLADA DEL MISMO CALIBRE. (a) CLONAR EL LANZADOR COMO `scripts/loop/vuelta194_bateria_por_tramos.py`, CLON DECLARADO del de la 189, cotejado con `scripts/loop/cotejar_clon_declarado.py` y con su salida pegada. (b) EL NUMERO DE TRAMOS SE COMPUTA CON `--plan`, NO SE TECLEA NI SE HEREDA, y se publica con su FECHA DE CORTE (banco `9.21`): el NUEVE de `AUDITOR.md` 6.1 es la cuenta de la nomina del 5 sep 2026 y no un objetivo. (c) CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR. (d) LA DOBLE CORRIDA NO SE AFLOJA: cada entrada se corre DOS VECES por el cotejo de reproducibilidad de la vuelta 141. (e) AL FINAL `--componer`, que es quien coteja EL CALIBRE, y UNA SALIDA SELLADA QUE MIDE CERO BYTES NO CUENTA COMO HECHA. (f) PUBLICAR EL RELOJ de la corrida. (g) SI UN TRAMO CAE EN ROJO, NI SE ESCONDE NI SE REPITE HASTA QUE SALGA VERDE: se publica con su tramo, su entrada y su motivo. Y LA TRAMPA MEDIDA POR EL AUDITOR: las NUEVE selladas que `vuelta183_bateria_por_tramos.py --siguiente` encuentra son de las vueltas 183 y 184 y NO de esta, asi que correr ese fichero declararia la bateria corrida sobre la corrida de otra vuelta | **CORRIDA: los DIEZ tramos con salida sellada del mismo calibre y cobertura 127 de 127. Y los diez en ROJO, publicados en rojo** | `SALIDA_V194_BATERIA_TRAMO_1.txt` a `_10.txt`, `SALIDA_V194_BATERIA.txt`, `SALIDA_V194_BATERIA_COMPUESTA.txt`, `SALIDA_V194_T3A_COTEJO_CLON.txt`, `SALIDA_V194_T3B_PLAN.txt`, `SALIDA_V194_T3_DATASET_RESTAURADO.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS. **CERRADA, Y CON UNA DISCREPANCIA DENTRO DEL ACTA QUE SE PUBLICA EN VEZ DE RESOLVERSE COPIANDO.**

**EL NUMERO DE LA ENTRADA NO SE TECLEA.** `scripts/loop/serie_de_registros.py`,
corrido en el bloque `G` de la apertura y otra vez dentro del registrador, da
**`R.56`** como siguiente libre sobre **47 entradas**, con **0 colisiones** y **0
huecos**. El encargo adelantaba `R.56` y **CALZA**, y esa palabra la escribe el
instrumento y no yo.

**LA ENTRADA ESCRITA:** `R.56` en `docs/PENDIENTES.md`. Contada de
`docs/loop/SALIDA_V194_T1A_REGISTRO_R56.txt`:
**12060 bytes en disco y 12060 bytes normalizado a LF**, **181 lineas** por
`count(NL)` y **182** por `split`, **0 guiones largos o medios**. La sede
`docs/PENDIENTES.md` pasa de **1029096 bytes** a **1039583 bytes**, y la entrada
se releyo del disco byte a byte.

**LA IDEMPOTENCIA NO SE AFIRMA: SE PROBO RE CORRIENDOLO**, con la sede medida en
bytes antes y despues. Segunda corrida:
`docs/loop/SALIDA_V194_T1A_RECORRIDO_SIN_ESCRIBIR.txt`
(12207 bytes en disco y 12207 bytes normalizado a LF), *"el acta
194 YA TIENE ENTRADA en la serie: 2 linea(s) la nombran. NO se escribe una entrada
nueva y NO se consume el numero R.57."* **docs/PENDIENTES.md sigue en 1039583
bytes**, la misma cifra por las dos medidas.

**LO QUE LA ENTRADA REGISTRA, TODO CONTADO DEL CUERPO ACOTADO DEL ACTA (lineas
68284 a 68708, 425 lineas) Y NADA DEL ENCARGO:**

| lo que se cuenta | del acta | cotejo |
|---|---:|---|
| adjudicaciones `4.1` a `4.10`, patron entrecomillado | 10 | el patron suelto da **0**, y las dos cifras se publican |
| discutibles `D.1` a `D.7`, todos A FAVOR | 7 | reparto por familia leido del titulo |
| preguntas `P.1`, `P.2` y `P.3`, contestadas por extension citable | 3 | |
| **`EN CONTRA`** | **0** | **CUARTA acta seguida**, y la guarda vieja de la 190 PARARIA aqui |
| hallazgos de la seccion 5 | 3 | los DOS lectores heredados dan **0** cada uno |
| discrepancias fuera del marcado, POR RESTA de la fila (5) menos los hallazgos (3) | 2 | la fila los cuenta juntos y su celda lo escribe |
| caidas propias del auditor, del CUERPO de la seccion 8 | **2** | **su fila de la tabla dice 1. NO CALZA** |
| caidas del ejecutor, de reporte | 1 | la fila nombra el hallazgo `5.2`, no una `C.n` |
| caidas del ejecutor, de metodo, con el rango expandido | 3 | `C.1` a `C.3`, y **CALZA** con su fila |
| actas sin entrada propia en la serie, tramo 173 a 193 | 8 | 173 a 180, y el encargo dice ocho: **CALZA** |

**LA DISCREPANCIA, DICHA ENTERA Y CON SUS DOS LINEAS.** El cuerpo de la seccion 8
del acta 194 (`## 8. MIS CAIDAS PROPIAS`, lineas 68646 a 68662) declara **DOS**
caidas propias del auditor, `C.1` en la linea 68648 y `C.2` en la 68654. **Su fila
de la tabla de credito, en la linea 68629, dice UNO** y solo nombra la `C.1`. **Las
dos lecturas son correctas: es el acta la que se contradice consigo misma.** Se
registra la del cuerpo, porque el encargo de esta vuelta dice literal *"cada cifra
se cuenta del cuerpo acotado del acta y no de aqui"* y ademas nombra **DOS**; y
**las dos cifras quedan publicadas en la entrada con su linea y su atribucion**.
**Es la misma especie que el propio hallazgo `5.2` del acta**, que levanta contra
el reporte de la 193 una seccion que dice cuatro donde el instrumento dice cinco.
**Lo registro y no lo adjudico: registrar no es adjudicar, y quien clasifica las
caidas del auditor es el auditor.** Va marcado como discutible abajo.

**Y NINGUNA GUARDA SE AFLOJO PARA PODER DECIRLO.** El registrador de la 193 PARABA
cuando el cuerpo y la fila no calzaban, y esa parada existia para cazar **un error
de lectura del propio registrador**. Aqui no hay error de lectura, asi que:

- **la parada por descuadre SIGUE ENTERA** para la fila del ejecutor de metodo,
  que es donde la lectura si podria fallar (3 claves del rango contra 3 de la
  fila, y CALZA);
- **la parada por especie no declarada SIGUE ENTERA**: la `C.1` sale **SIN
  ESPECIE** con el vocabulario de la 193 y el registrador PARARIA, asi que el
  vocabulario CRECE en una marca literal del acta, `ROMPER UN REMEDIO ESCRITO`, y
  **una caida muda sigue haciendo PARAR**;
- **y SE ANADE UNA GUARDA NUEVA**, `entrada_publica_las_dos()`: si hay descuadre y
  la entrada armada no lleva **las dos** cifras en su tabla de cotejo Y la frase
  que declara el descuadre, el registrador **cae en rojo y no escribe nada**. Una
  discrepancia callada seria peor que la parada que sustituye.

**LO QUE ESTE REGISTRADOR ESTRENA, Y POR QUE NO ERA OPCIONAL.** El acta 194 cambia
de forma en tres sitios y **los tres estaban medidos antes de escribir una linea
de la entrada**:

1. **los hallazgos son titulares `###` y no negritas**: `claves_de_adjudicacion` da
   **0** y `claves_entrecomilladas` da **0** sobre esta acta, y con cero el
   registrador PARARIA por no encontrar hallazgos que el acta si tiene. Se anade
   `hallazgos_en_titular()`, **lector ANADIDO y no ensanche**: los dos viejos
   siguen intactos y sus cifras se publican al lado;
2. **las caidas propias viven en la seccion 8 y no en la 6**, porque en el acta 194
   la 6 es PENDIENTES DE DOCTRINA. Se anade
   `caidas_propias_entrecomilladas()`, con **el rango por parametro**, para que el
   lector no suponga la seccion;
3. **la fila de puestos ya no dice `SOLAPE TOTAL`: dice `ONCE QUEMADOS`.** La nota
   heredada **no aparece** en esta acta (buscada y medida), y el registrador de la
   193 PARARIA por eso. **La vieja se conserva y se sigue buscando**: retirarla
   estrecharia el vocabulario a lo que el acta de hoy usa.

**LA FILA DE PUESTOS, REGISTRADA CON SU NOTA Y SUS TRES CIFRAS**, leidas de la
celda y no parafraseadas: **30 aislados**, **30 cotejados**, **once quemados por el
contexto de sesion y no por comando del auditor**, y **el cotejo limpio va sobre
19**. **El cotejo se publica dos veces**, sobre los 30 y sobre los 19. Un quemado
no es un solape: **el solape mide si dos lectores leen lo mismo; el quemado dice
que uno de los dos ya sabia lo que el otro habia dicho antes de leer.**

**EL CASO POSITIVO POR MUTACION, CORRIDO Y NO PROMETIDO:**
`docs/loop/SALIDA_V194_T1A_MUTACION_REGISTRADOR.txt`
(4074 bytes en disco y 4074 bytes normalizado a LF), **VEREDICTO:
VERDE**, con **27 casos, 27 pasan y 0 fallan**, cifra que ese mismo fichero
publica de si mismo en su linea `CIFRA casos` y que por eso `cerrar_reporte.py`
puede cotejar contra esta prosa. Cada trozo
nuevo es PURO y se corre sobre texto **fabricado**, con el valor esperado sacado de
como se fabrico y no de una constante igual a la obtenida. Las mutaciones que
importan, nombradas: **la misma entrada sin la frase que declara el descuadre CAE**;
**una entrada que publica una sola cifra CAE**; **una caida sin especie sigue
saliendo SIN ESPECIE con el vocabulario nuevo**; y **los dos lectores heredados
sobre el texto fabricado dan cero**, que es lo que prueba que el nuevo es un
anadido y no un ensanche.

### TAREA 2. LOS DOS ARNESES DE LA CUARTA PUERTA. **CERRADA, LOS TRES ESCENARIOS DEL AUDITOR INVERTIDOS, Y CON UNA PREMISA SUYA QUE NO SE SOSTIENE Y QUE PUBLICO IGUAL.**

**LA TABLA DEL AUDITOR Y LA DE HOY, UNA DEBAJO DE OTRA.** La suya vive en
`docs/loop/_auditor_v194_cuarta_puerta_rota.txt`; la de hoy sale contada de
`docs/loop/SALIDA_V194_T2G_TRES_ESCENARIOS.txt`
(3671 bytes en disco y 3671 bytes normalizado a LF; `sha256` de disco `56481dd977310ceb` y `sha256` LF `56481dd977310ceb`), **13
casos, 13 pasan, 0 fallan, VEREDICTO VERDE**, cifra que ese fichero publica de si
mismo en su linea `CIFRA casos`:

| escenario, con el fichero del turno PUESTO | lo que medio el auditor | lo que mide hoy |
|---|---|---|
| solo el arnes de la **192** | exit 0, verde, y el turno **BORRADO** | exit 0, y el turno **EXACTAMENTE como estaba** |
| solo el arnes de la **193** | exit 1, **ROJO**, turno EXISTE | **exit 0, VEREDICTO VERDE**, turno como estaba |
| los dos, en el orden alfabetico de la bateria | 192 verde, 193 verde, turno **BORRADO** | los dos verdes, turno como estaba |

**Y EL COTEJO QUE DE VERDAD DECIDE, PORQUE UN VEREDICTO SE PUEDE CREER Y UN
`sha256` NO:** la salida sellada de cada arnes es **la misma corrido solo y
corrido en compania**. El de la 192 da `ee605b4b8450c484` en los dos escenarios;
el de la 193 da `1cb7f216c650b06f` en los dos. **Si el verde de uno siguiera
prestado del otro, la diferencia estaria dentro de su salida.**

**LO QUE SE ARREGLO, PIEZA POR PIEZA.**

**(a) EL ARNES DE LA 192 YA NO TOCA LA SEDE DE VERDAD.** Se le anade, antes de su
primer `olvidar_todo()`, la redireccion de `AP.RUTA_DEL_TURNO` a su temporal, que
es exactamente para lo que esa variable es de modulo, con el mecanismo que el
arnes de la 193 ya usaba. **Y no basta con redirigir:** el arnes mide ahora la
sede de verdad **al entrar y al salir**, con existencia, bytes y `sha256`, y
**CAE EN ROJO si cambia**. Un arnes que promete no tocar algo y no lo comprueba es
lo que dejo pasar este agujero.

**(b) EL ARNES DE LA 193 YA NO EXIGE QUE EL FICHERO NO EXISTA.** Su caso `H`
comprobaba `os.path.exists(turno_real) == False`, o sea **pedia que no hubiera
auditor**. Ahora mide la sede **antes** (bloque `0`, nuevo) y **despues** (caso
`H`) y **cae si CAMBIA**. La funcion `medir_turno_real()` devuelve **las tres
cosas a proposito**: un fichero borrado y reescrito con el mismo tamano tiene el
mismo `existe` y los mismos `bytes`, y **solo el `sha256` lo delata**.

**Y AQUI APARECIO UN SEGUNDO FALLO, QUE NO ESTABA EN EL ENCARGO Y QUE ERA LA
CAUSA DE VERDAD.** Con `(a)` y `(b)` puestos, el arnes de la 193 **seguia saliendo
en rojo** con el turno puesto, y no por su caso `H`: por sus casos `A`, `B` y `E`.
La causa, medida y no supuesta: `apertura_del_auditor.py` carga el turno **AL
IMPORTAR**, y `_cargar_turno()` **se iba dejando la memoria como estuviera cuando
el fichero no existia**. Eso la convertia en un MEZCLADOR y no en un cargador, y
rompia lo unico para lo que `RUTA_DEL_TURNO` es de modulo: **un proceso hijo que
redirige la ruta a un temporal y vuelve a cargar seguia viendo el turno de la sede
de verdad**. Medido: sus hijos entraban con `['x']` en la bitacora en vez de
vacios. **Arreglado con la vara escrita entera y con sus dos lados:** si el fichero
**no existe**, el disco dice que no hay turno y la memoria se reinicia; si el
fichero **existe pero no se puede leer**, eso no es "no hay turno" sino un fichero
roto, y **la memoria NO se toca**, porque tirar el estado vivo por un JSON corrupto
seria perder la prueba en silencio.

**(c) EL CASO POSITIVO POR MUTACION, Y LANZA PROCESOS DE VERDAD.**
`scripts/loop/vuelta194_tarea2c_mutacion_sede_del_turno.py`, salida en
`docs/loop/SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt`
(3687 bytes en disco y 3687 bytes normalizado a LF; `sha256` de disco `b014e233a5e7512d` y `sha256` LF `b014e233a5e7512d`), **14 casos, 14
pasan, 0 fallan, VEREDICTO VERDE**, contados de su propia linea `CIFRA casos`.
**Su caso rojo no es una constante comparada consigo misma:** escribe en un
temporal un **culpable fabricado** de cuatro lineas que reproduce el fallo exacto
de antes de esta vuelta (importa el modulo y llama a `olvidar_todo()` sin redirigir
nada), lo lanza **como proceso**, y **el detector lo caza: `LA BORRO`, con
exitcode 0**. Si el detector no lo cazara, el arnes cae. **Lanzar procesos de
verdad es la mitad que importa:** la sede se resuelve al IMPORTAR el modulo, asi
que un arnes importado desde el mismo proceso heredaria la redireccion de otro y
el agujero no se veria.

**(d) LA SEDE DEL TURNO NO SE PUEDE VOLVER A COMMITEAR.** La via es `.gitignore`,
que es lo natural, **porque lo que hay que impedir es que ENTRE EN EL INDICE y eso
lo decide git**. Y la comprobacion tambien la hace git y no una lectura del fichero
de reglas: `git check-ignore -v` sale con exitcode 0 y nombra la regla
`.gitignore:43`, y `git ls-files` devuelve vacio. Las dos son casos del arnes `c`.

**(e) NO SE CLONO NINGUNO DE LOS DOS FICHEROS: SE LES ANADIO**, con el bloque
nuevo delimitado y comentado con la fecha y el hallazgo que lo motiva, y **el
texto viejo del caso `H` se dice en el comentario en vez de borrarse sin rastro**.

**(f) LA NOMINA NO SE TOCO.** Sigue en **127 entradas**, medidas con
`len(VMV.VIEJAS)` en el bloque `H` de la apertura y otra vez al escribir esto.

**LAS DOS SALIDAS SELLADAS SE RE SELLAN, Y EL CORTE VIEJO SE GUARDA AL LADO**, que
es la forma que la `4.9` del acta 194 declara correcta:

| salida sellada | corte VIEJO (blob de `edff6568`) | corte NUEVO |
|---|---|---|
| `SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt` | 4282 bytes, `sha256` `4779fcd04bc5b2da` | 5153 bytes en disco y 5153 por LF, `sha256` `ee605b4b8450c484` por las dos convenciones |
| `SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt` | 4613 bytes, `sha256` `10c2d2d1e9eb06ce` | 5023 bytes en disco y 5023 por LF, `sha256` `1cb7f216c650b06f` por las dos convenciones |

**Y COMO TOQUE `apertura_del_auditor.py`, RE CORRI LOS TRES ARNESES DE LA NOMINA
QUE LO VIGILAN**, antes de la bateria y no confiando en que ella los pille:
`vuelta182_tarea2_mutacion_apertura_auditor.py`,
`vuelta160_tarea6b_mutacion_puerta.py` y `vuelta162_tarea2a_mutacion_puerta.py`.
**Los tres con exitcode 0 y ninguna de sus salidas selladas cambio**, medido con
`git status --porcelain -- docs/loop/`, que solo lista las dos que esta tarea re
sella a proposito.

**LA PREMISA DEL ENCARGO QUE NO SE SOSTIENE, PUBLICADA SALGA LO QUE SALGA.** El
hallazgo `5.1` del acta 194 dice, literal, que los dos arneses *"son entradas
suyas"* de la nomina y que por eso *"uno de sus nueve tramos publicaria un verde
prestado"*. **Corrido hoy sobre `VMV.VIEJAS`, ninguno de los dos esta en la
nomina:** `vuelta192_tarea4_mutacion_cuarta_puerta.py` da `False` y
`vuelta193_tarea4e_mutacion_sello_entre_procesos.py` da `False`, y **la vuelta mas
alta nombrada en las 127 entradas es la 190**. O sea que **la bateria de esta
vuelta no los habria corrido**, y el verde prestado no habria llegado a ningun
tramo. **La reparacion se hizo igual y no me arrepiento de haberla hecho**, porque
la mitad de abajo del hallazgo si estaba: **el arnes de la 192 borraba de verdad el
turno vivo del auditor en su sede de verdad, con exitcode 0 y sin avisar**, y eso
es cierto lo corra quien lo corra. **Lo que no es cierto es el camino por el que
llegaba.** No lo adjudico ni lo clasifico: lo mido, lo publico y lo marco abajo.
**Y no toco la nomina para hacerlo calzar**, que era la otra salida y esta
expresamente prohibida.

### TAREA 3. LA BATERIA, ENTERA Y POR TRAMOS. **CORRIDA: LOS DIEZ TRAMOS CON SALIDA SELLADA DEL MISMO CALIBRE. Y LOS DIEZ EN ROJO, PUBLICADOS EN ROJO.**

**(a) EL LANZADOR, CLONADO Y COTEJADO.**
`scripts/loop/vuelta194_bateria_por_tramos.py`, **clon declarado del de la 189**,
que es el ultimo que corrio de verdad. Cotejo con
`scripts/loop/cotejar_clon_declarado.py --exigir-codigo-identico`, salida en
`docs/loop/SALIDA_V194_T3A_COTEJO_CLON.txt`: **SOLO LA MAQUINA: IDENTICO**,
**CIFRA lineas de maquina que difieren: 0**, y **el AST sin el docstring:
IDENTICO**, con **4070 nodos en los dos**. Lo unico que difiere es el docstring
(43 lineas en el original y 37 en el clon). **Su numero no se teclea:** sale de
`os.path.basename(__file__)`, y la guarda `literales_de_vuelta_clavados()`,
corrida sobre el propio fuente en cada invocacion, publica **CIFRA literales de
vuelta clavados en lineas que escriben: 0**.

**(b) EL REPARTO, COMPUTADO Y CON SU FECHA DE CORTE.**
`--plan`, salida en `docs/loop/SALIDA_V194_T3B_PLAN.txt`: **CIFRA entradas de la
nomina: 127**, **CIFRA tamano de tramo: 13**, **CIFRA tramos: 10**, **CIFRA suma
de las entradas de todos los tramos: 127**, con **corte `HEAD e6f46677ab23`,
nomina contada en esa corrida** (banco `9.21`). **Da DIEZ y no nueve**, y el
NUEVE de `AUDITOR.md` 6.1 es la cuenta de la nomina del 5 sep 2026, no un
objetivo: la cifra sale de `len(tramos)` y no de ninguna tecla.

**Y LA TRAMPA DEL ENCARGO, EVITADA Y MEDIDA POR MI.** El bloque `I` del sello de
apertura fecho **una a una** con `git log --diff-filter=A` las nueve salidas que
`vuelta183_bateria_por_tramos.py --siguiente` cuenta: **nacen en las vueltas 183 y
184**, y el asunto del commit que da de alta cada una lo dice en su propia linea.
`--siguiente` de **mi** lanzador contesta **CIFRA tramos CON salida sellada no
vacia: 0** y **EL SIGUIENTE ES EL TRAMO 1**, que es la verdad.

**(c) Y (f) LOS DIEZ TRAMOS, CADA UNO COMMITEADO CON SU SALIDA SELLADA AL
TERMINAR, Y EL RELOJ.** La tabla sale de `--componer`
(`docs/loop/SALIDA_V194_BATERIA_COMPUESTA.txt`) y el reloj de la linea
`DURACION DEL TRAMO (monotona, minutos)` de cada salida sellada:

| tramo | bytes disco | bytes LF | lineas | `sha256` | entradas | minutos | exitcode |
|---:|---:|---:|---:|---|---:|---:|---:|
| 1 | 11284 | 11284 | 143 | `a4db8c7b420a` | 13 | 1.1 | 1 |
| 2 | 9528 | 9528 | 137 | `0a08458bafc6` | 13 | 2.9 | 1 |
| 3 | 9582 | 9582 | 137 | `b5f1b65a553e` | 13 | 7.6 | 1 |
| 4 | 9596 | 9596 | 137 | `984584039c88` | 13 | 1.4 | 1 |
| 5 | 9559 | 9559 | 137 | `614226f68f13` | 13 | 0.6 | 1 |
| 6 | 9605 | 9605 | 137 | `6ace42fc6b5a` | 13 | 1.1 | 1 |
| 7 | 9815 | 9815 | 139 | `2a40104d3fbf` | 13 | 0.6 | 1 |
| 8 | 9581 | 9581 | 137 | `5fb1efd65e77` | 13 | 0.8 | 1 |
| 9 | 10058 | 10058 | 137 | `64042ebd6bfe` | 13 | 0.7 | 1 |
| 10 | 9492 | 9492 | 128 | `36e2d04ffc83` | 10 | 0.4 | 1 |

**EL RELOJ, LAS DOS MEDIDAS Y NO UNA:** la **suma de las duraciones monotonas de
los diez tramos da 17.2 minutos**, y la **ventana de reloj de pared del primer
inicio al ultimo fin es de 30.1 minutos** (inicio del tramo 1
`2026-09-06T22:01:57Z`, fin del tramo 10 `2026-09-06T22:32:03Z`), leidas de las
lineas `INICIO` y `FIN (reloj de pared, UTC)` de las dos salidas selladas. **La
diferencia entre las dos no es un misterio y no se disimula:** entre tramo y tramo
van el commit y su hook, y ademas el primer intento del tramo 3 se corto.

**EL TRAMO 3 SE CORTO A MITAD EN SU PRIMER INTENTO**, por tope de tiempo del turno
y no por fallo de la bateria, y **dejo `dataset/metadata/master_graph.json`
tocado** porque el PASO 5 del lanzador no llego a correr. Medido con **las dos
varas y sin elegir la comoda**: `git status --porcelain` lo daba por modificado y
`git diff --numstat` decia **CERO filas**, o sea que la diferencia era de finales
de linea y no de contenido. Restaurado con `git checkout -- dataset/` **sin tocar
ningun final de linea a mano**, y **remedido**: cero y cero. Entero en
`docs/loop/SALIDA_V194_T3_DATASET_RESTAURADO.txt`
(1154 bytes en disco y 1154 bytes normalizado a LF). El tramo NO se dio
por corrido: no dejo salida sellada y `--siguiente` volvio a decir TRAMO 3, que es
lo que la 6.1 llama retomar en el tramo siguiente.

**(d) LA DOBLE CORRIDA NO SE AFLOJO.** Cada entrada se corre DOS VECES por el
cotejo de reproducibilidad de la vuelta 141, y el resultado esta en la celda que
lo mide: **`0 sin reproducir` en los diez tramos**.

**(e) `--componer`, QUE ES QUIEN COTEJA EL CALIBRE.** Exitcode 0 y **VERDE**:
**CIFRA entradas que los tramos dicen haber corrido: 127**, **CIFRA entradas de la
nomina que NINGUN tramo corrio: 0**, **CIFRA entradas corridas que NO estan en la
nomina: 0**, **CIFRA entradas corridas MAS DE UNA VEZ: 0**. La cobertura se lee
**de las salidas y no se recalcula del reparto**, que es la mitad que impide el
atajo. La salida unica es `docs/loop/SALIDA_V194_BATERIA.txt`:
**102495 bytes en disco y 102495 bytes normalizado a LF**, 1454 lineas, `sha256` LF
`f2d927fa66cdc40a3f157294eaee1c86d1ffb4633a7afbd731befc1cd094b263`**. **Ninguna
salida sellada mide cero bytes**, y esa es la condicion que la 6.1 pone para que
un tramo cuente como hecho.

**(g) LOS ROJOS, PUBLICADOS CON SU TRAMO, SU ENTRADA Y SU MOTIVO, Y NO REPETIDOS
HASTA QUE SALGAN VERDES.** **LOS DIEZ TRAMOS SALEN `ROJO POR FALLO` con exitcode
1**, contados uno a uno de su linea `CLASE DEL VEREDICTO`. **Y la especie del
veredicto dice lo que de verdad paso**, leida de la linea `CIFRA de FALLO` de cada
salida:

| especie | cuantos | en cuantos tramos |
|---|---:|---|
| con ancla perdida | 0 | los diez |
| **que no mordieron** | **1** | **solo el tramo 7** |
| sin reproducir | 0 | los diez |
| **fuera de la nomina** | **6** | **los diez** |
| invisibles al censo | 0 | los diez |
| `SUJETO VIVO` | 0 | los diez |
| `NO DECIDIBLE` con motivo escrito (deuda declarada) | 3 | los diez |

**NINGUN ARNES FALLO POR SU PROPIA MAQUINA SALVO UNO.** Las 127 entradas corrieron
y reprodujeron. Los dos motivos del rojo son **censales y globales**, o sea que
salen en los diez tramos por igual y no dependen de que entradas lleve cada uno:

1. **SEIS ARNESES QUE EL CENSO VE Y LA NOMINA NO TIENE**, nacidos despues de la
   vara de la vuelta 148: `vuelta191_tarea3_mutacion_lineas.py`,
   `vuelta191_tarea4_mutacion_veredicto.py`,
   `vuelta191_tarea6_mutacion_bloque_tallado.py`,
   `vuelta192_tarea4_mutacion_cuarta_puerta.py`,
   `vuelta193_tarea4e_mutacion_sello_entre_procesos.py` y
   `vuelta194_tarea2c_mutacion_sede_del_turno.py`, que es el que esta vuelta
   escribio. **ES NUEVO EN ESTA BATERIA:** la de la 189 publica **0** en esa misma
   celda, medido en su tramo 1. **NO SE ARREGLA AQUI**, y por dos razones escritas
   antes de mirar: el encargo dice **NO TOQUES LA NOMINA**, y podarla o adelantarla
   es la opcion que el fundador RECHAZO el 5 sep 2026. **Y ES LA CORROBORACION
   INDEPENDIENTE DE LO QUE LA TAREA 2 MIDIO**: el censo de la bateria, por su
   cuenta y con otro instrumento, dice que los dos arneses de la cuarta puerta
   **no estan en la nomina**.
2. **TRES ENTRADAS SIN SUJETO CONGELADO**, las tres con motivo escrito:
   `vuelta186_tarea2c_mutacion_cierre_tardio.py`,
   `vuelta187_tarea4_mutacion_dos_convenciones.py` y
   `vuelta188_tarea4_mutacion_cobertura_parejas.py`. **NO ES NUEVO:** la bateria de
   la 189 publica **la misma lista y el mismo rojo en sus diez tramos**, medido en
   sus salidas selladas.

**Y EL UNICO ARNES QUE FALLO POR SU MAQUINA, NOMBRADO CON SU TRAMO Y SU MOTIVO:**
**tramo 7**, `vuelta172_tarea5_mutacion_cierre.py`, **exit 1, `NO MORDIO`, 2.4s**.
Corrido a mano aparte, publica **CIFRA casos: 17 | pasan: 15 | fallan: 2** y
**CIFRA casos que caen al mutar el esperado: 16 de 17**. Los dos que fallan son
`A_con_las_cuatro_no_falta_ninguna` (real 1, esperado 0) y
`A_y_no_nombra_ningun_codigo` (real `['(3)']`, esperado `[]`), y el que no cae al
mutar es el primero de esos dos. **TAMPOCO ES NUEVO:** la bateria de la 189 lo
publica igual, `exit 1 NO MORDIO`, en su propia salida sellada. **No lo re corri
hasta que saliera verde y no lo arreglo**: esta vuelta es de bateria y su encargo
no lo incluye.

**LO QUE ESTO DEJA DICHO, SIN ADORNARLO:** la bateria **esta corrida** por la vara
de la 6.1, porque **los diez tramos tienen salida sellada no vacia y del mismo
calibre** y `--componer` lo coteja leyendo las salidas. **Y su contenido sale en
rojo**, por dos cuentas censales y un arnes que no muerde, **ninguno de los tres
arreglable dentro de este encargo**. Las dos cosas son ciertas a la vez y se
publican juntas: **una bateria corrida no es una bateria verde.**

<!-- FIN ANEXO DE TAREAS -->

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**LA CABECERA DE ARRIBA ES LA TABLA TALLADA ENTERA**, pegada de
`docs/loop/SALIDA_V194_TALLADOR_CABECERA.txt`, que salio de
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 194` con **exitcode 0
y sin una sola celda ilegible**. **LA CELDA QUE NO SALE DE UN INSTRUMENTO NO SE
ESCRIBE**, y por eso aqui abajo no se repite ninguna de sus cifras: se anaden las
que el tallador no cubre, cada una con el fichero del que sale.

| lo que se mide | cifra | de que fichero sale |
|---|---|---|
| entradas de la nomina de la bateria | 127 | `len(VMV.VIEJAS)`, corrido en la apertura y otra vez al cierre |
| tramos del reparto | 10 | `SALIDA_V194_T3B_PLAN.txt`, computado y no tecleado |
| entradas que los tramos dicen haber corrido | 127 | `SALIDA_V194_BATERIA_COMPUESTA.txt` |
| entradas sin correr, de mas, o repetidas | 0, 0 y 0 | `SALIDA_V194_BATERIA_COMPUESTA.txt` |
| tramos con salida sellada no vacia | 10 de 10 | las diez `SALIDA_V194_BATERIA_TRAMO_n.txt` |
| tramos cuya `CLASE DEL VEREDICTO` es `ROJO POR FALLO` | 10 de 10 | la linea `CLASE DEL VEREDICTO` de cada sellada |
| arneses que no mordieron | 1 (tramo 7) | la linea `CIFRA de FALLO` de cada sellada |
| arneses sin reproducir | 0 | la misma linea, en los diez |
| arneses fuera de la nomina | 6 | la misma linea, en los diez |
| entradas sin sujeto congelado | 3, con motivo escrito | la misma linea, en los diez |
| entradas de la serie `R.n` | 48, siguiente libre `R.57`, 0 colisiones y 0 huecos | `serie_de_registros.py`, corrido al cierre |
| actas sin entrada propia en la serie, tramo 173 a 193 | 8 | `SALIDA_V194_T1A_REGISTRO_R56.txt` |
| casos del arnes del registrador | 27, 27 pasan, 0 fallan | `SALIDA_V194_T1A_MUTACION_REGISTRADOR.txt` |
| casos del arnes de la sede del turno | 14, 14 pasan, 0 fallan | `SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt` |
| casos del cotejo de los tres escenarios | 13, 13 pasan, 0 fallan | `SALIDA_V194_T2G_TRES_ESCENARIOS.txt` |

**LA SALIDA UNICA DE LA BATERIA:** `docs/loop/SALIDA_V194_BATERIA.txt`, **102495
bytes en disco y 102495 normalizado a LF**, **1454 lineas**, `sha256` LF
`f2d927fa66cdc40a3f157294eaee1c86d1ffb4633a7afbd731befc1cd094b263`. **El hueco
que la 193 declaro con su nombre y sus cero bytes ya no es un hueco.**

**EL RELOJ DE LA BATERIA, CON SUS DOS MEDIDAS:** **17.2 minutos** sumando las
duraciones monotonas de los diez tramos, y **30.1 minutos** de ventana de reloj de
pared entre el inicio del tramo 1 (`2026-09-06T22:01:57Z`) y el fin del tramo 10
(`2026-09-06T22:32:03Z`).

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ESTADO DEL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO.**
`git status --porcelain` daba **1** linea al entrar.
`git diff --numstat -- dataset/` daba **0** filas. Las dos salen de
`docs/loop/SALIDA_V194_APERTURA.txt`, sellado antes de la primera operacion. **La
unica linea de `status` que habia era el propio fichero del bloque de apertura,
todavia sin commitear**, y esta escrita dentro de su bloque `B`.

**SE TOCARON, TODOS EN `scripts/loop/`, `docs/loop/` y `.gitignore`:**
`apertura_del_auditor.py` (su `_cargar_turno()`),
`vuelta192_tarea4_mutacion_cuarta_puerta.py`,
`vuelta193_tarea4e_mutacion_sello_entre_procesos.py`, `.gitignore`, mas los
instrumentos nuevos de esta vuelta. **`docs/PENDIENTES.md`** gano la entrada
`R.56`. **Y `docs/loop/SALIDA_V194_APERTURA.txt` recibio al cierre un bloque `Z`
marcado como RESTATEMENT DECLARADO**, que es mi caida `C.2` y va contada abajo.

**NO SE TOCO NADA DE:** `dataset/`, `web/`, `engine/`,
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `docs/plan/`, ni **la nomina de la
bateria**, que sigue en **127 entradas** leidas de `VMV.VIEJAS` al entrar y al
salir. La opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada. **Y
esta vuelta tuvo el motivo mas grande que ha habido para tocarla y no la toco:**
seis arneses fuera de la nomina son lo que pone los diez tramos en rojo.

**LOS VEREDICTOS NO SE MOVIERON:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y
cierra en **4054129 bytes en disco y 4054129 bytes normalizado a LF**, con
`sha256` de disco **`0a77b5a35a962621`** y `sha256` LF **`0a77b5a35a962621`**, medido en el
bloque `C` de la apertura y otra vez al cierre.

**`dataset/` SE MIDIO AL ENTRAR Y AL SALIR Y LAS DOS CIFRAS SE PUBLICAN: CERO Y
CERO.** El ciclo de Gate 0 corrio ENTERO las dos veces, con
`--reaplico-curaduria` y despues `etiquetas_de_cara.py --aplicar`, que es lo que
el encargo trajo medido y lo que evita las 72 lineas.

**Y NO ENTRO NADA DE LO QUE EL ENCARGO DEJA FUERA:** ni cribado, ni recomputo, ni
operaciones del plan, ni las mesas anotadas, ni ciegas nuevas, ni la relectura al
doble del tramo del auditor, que va a la 195 con su tramo ya cerrado.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` REGISTRE LA CIFRA DEL CUERPO Y NO LA DE LA TABLA DE CREDITO.** El acta 194
declara **dos** caidas propias del auditor en su seccion 8 y **una** en su fila de
la tabla. Elegi el cuerpo porque el encargo dice literal *"cada cifra se cuenta
del cuerpo acotado del acta y no de aqui"*. **Un lector puede sostener lo
contrario con la misma fuerza:** la tabla de credito es la sede de las cifras de
credito, y la fila es la que lleva la racha. **Las dos quedan publicadas con su
linea; lo discutible es cual manda.**

**`D.2` CAMBIE UNA PARADA POR UNA GUARDA DE PUBLICACION, Y ESO SE PUEDE LEER COMO
AFLOJAR.** El registrador de la 193 PARABA cuando el cuerpo y la fila no calzaban;
el mio publica las dos y **cae en rojo si la entrada no las lleva las dos**.
Sostengo que la parada vieja cazaba **un error de lectura del registrador** y que
aqui no lo hay, pero **un lector puede decir que una parada sustituida es una
parada menos**. La parada sigue entera en la fila del ejecutor.

**`D.3` TOQUE UN TERCER FICHERO QUE EL ENCARGO NO NOMBRA.** La pieza `e` dice *"NO
SE CLONA NINGUNO DE LOS DOS FICHEROS: se les anade"*, y yo ademas arregle
`_cargar_turno()` en `apertura_del_auditor.py`. **Sin eso el arnes de la 193 sigue
en rojo con el turno puesto**, o sea que la tarea no se podia cerrar sin tocarlo;
pero **el encargo no me lo pidio y lo marco**.

**`D.4` ELEGI UN LADO EN `_cargar_turno()` Y EL OTRO ERA DEFENDIBLE.** Cuando el
fichero **no existe** reinicio la memoria; cuando **existe y no se puede leer** NO
la toco. **Un lector puede sostener que un JSON roto tambien debe reiniciar**, por
simetria y para que no quede estado fantasma. Elegi no perder el estado vivo en
silencio, y lo digo.

**`D.5` PUSE UN CENTINELA EN LA SEDE DE VERDAD DEL TURNO PARA PROBAR QUE NADIE LA
BORRA.** Para demostrar que un arnes no borra ese fichero, hace falta que el
fichero exista mientras corre la prueba. **O sea que toco la sede que digo
proteger.** La respaldo byte a byte si hay una viva, pongo un centinela fabricado,
y al terminar restauro y **REMIDO** existencia, bytes y `sha256`. **Un lector
puede decir que la sede de verdad no se toca nunca y que la prueba debia montarse
en otro sitio.**

**`D.6` CORRI LA BATERIA SABIENDO QUE SALDRIA EN ROJO POR ALGO QUE NO PUEDO
ARREGLAR.** Los seis arneses fuera de la nomina ponen los diez tramos en rojo, y
la unica reparacion es tocar la nomina, que esta prohibida. **Podia haber parado
antes de correrla y traer la contradiccion**; corri, porque `AUDITOR.md` 6.1
manda correrla y porque un rojo medido dice mas que una parada. **Lo marco por si
la eleccion correcta era la otra.**

**`D.7` LE ANADI A MIS TRES ARNESES NUEVOS LA LINEA `CIFRA casos`, QUE ES LA QUE
`cerrar_reporte.py` USA PARA COTEJAR MI PROSA.** Sin ella, mis citas de casos
salen `SIN COTEJO`, o sea que la cifra se teclea y nadie la mira. **Un lector
puede decir que anadir la linea que me va a medir es escoger mi propia vara.** La
anadi solo a los arneses nuevos y **no toque la de ninguno viejo**.

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` LAS DOS CIFRAS DE CAIDAS PROPIAS DEL ACTA 194, CUAL ES LA SEDE?** Su
seccion 8 dice dos y su fila de credito dice una. **Registre la del cuerpo y
publique las dos.** No lo adjudico yo: es una cifra de credito del auditor.

**`P.2` LOS SEIS ARNESES FUERA DE LA NOMINA, QUIEN LOS METE Y CUANDO?** La regla
del propio fichero dice que un arnes entra en la nomina, y el acta 176 acepto que
entre en su misma vuelta; pero **las vueltas 191, 192, 193 y 194 escribieron
arneses y ninguno entro**, y cada encargo repite *"NO TOQUES LA NOMINA"*. **Tal
como esta, la bateria de la 199 saldra en rojo por lo mismo y con la lista mas
larga.** No lo resuelvo porque tocar la nomina esta expresamente prohibido.

**`P.3` UNA BATERIA CON LOS DIEZ TRAMOS EN ROJO Y `--componer` EN VERDE, ESTA
CORRIDA?** Por la letra de la 6.1 si: los diez tienen salida sellada no vacia y
del mismo calibre, y la cobertura se lee de las salidas. **Pero `--componer` sale
con exitcode 0 sin mirar el veredicto de los tramos**, y eso es exactamente el
punto que la lista de lo que sigue fuera nombra como *"el exitcode 2 propagado a
`--componer`"*. **Lo dejo dicho con las dos mitades: corrida por la letra, roja
por dentro.**

## 7. PENDIENTES DE DOCTRINA

**NINGUNO ABIERTO POR MI.** Las tres preguntas de arriba no piden regla nueva:
piden que alguien con autoridad diga cual de dos reglas ya escritas manda.

## 8. LO QUE LA 195 RECIBE

**LA BATERIA ESTA CORRIDA Y SU HUECO CERRADO**, asi que la 195 vuelve al regimen
de vuelta normal, con la seccion 9 en hueco declarado y medido. **La siguiente
bateria cae en la 199.**

**LO QUE SIGUE FUERA Y VA NOMBRADO PARA QUE NO SE REDESCUBRA:** la relectura al
doble del tramo de la tanda del auditor, con su tramo y su doble ya cerrados por
el acta 194; el remedio de codigo del hallazgo `5.3`, que desde hoy aplico a mano
en mis mensajes de commit; el desfase de `PATRONES_ACTA`; `acumulan()` que lea la
tabla; el cotejo de clon declarado que separa sentencia de codigo de cambio de
texto; la excepcion que publica siempre su lista; el censo de arneses con carril
de mutacion sin fichero propio; las **8** actas sin entrada propia en la serie
(173 a 180); el exitcode 2 propagado a `--componer`; el campo `evidencia` de
`OP-L-02`, **cuyo ESTADO NO SE MUEVE: sigue en `LISTA`**; y **las 72 filas `B` del
archivo**, nombradas y no resueltas.

**Y DOS COSAS QUE LA 195 RECIBE ROTAS Y QUE YO NO PODIA ARREGLAR HOY:** los
**seis** arneses fuera de la nomina, que ponen en rojo los diez tramos de
cualquier bateria mientras nadie los meta; y `vuelta172_tarea5_mutacion_cierre.py`,
que **no muerde** y que la bateria de la 189 ya publicaba igual.

### 8.1 MIS CAIDAS PROPIAS DE ESTA VUELTA, DECLARADAS Y NO OMITIDAS

**`C.1` (Y ACUMULA). MI BLOQUE DE APERTURA NO CORRIO `tsc` NI `pnpm test`, Y ESAS
DOS CELDAS DE APERTURA SE MIDIERON AL CIERRE.** Corri los dos comandos en el
momento del cierre y **lo declare en su fichero propio**,
`docs/loop/SALIDA_V194_APERTURA_INCOMPLETA_DECLARADA.txt`, que es el carril que la
`4.7` del acta 194 adjudico A FAVOR. **La cifra es cierta; su MOMENTO no es el que
su nombre dice.** Por `EJECUTOR.md` 1, una columna de apertura medida al cierre es
caida que ACUMULA, y **la cuento como tal en vez de discutirla**. **Es la SEGUNDA
vuelta seguida con esta misma caida**, porque el reporte de la 193 se la declaro a
si mismo en su `C.1` y yo clone su bloque de apertura.

**`C.2` (DE METODO). TOQUE LA APERTURA SELLADA AL CIERRE.** La guarda `D.1` de
`cerrar_reporte.py` coteja la seccion 4 contra la apertura sellada buscando **dos
literales exactos**, y mi bloque de apertura escribio esas mismas cifras **con
otras palabras**. Anadi al final de `docs/loop/SALIDA_V194_APERTURA.txt` un bloque
`Z` **marcado como RESTATEMENT DECLARADO**, que **lee las dos cifras del propio
fichero con una expresion regular** y no cambia ni un digito, y que dice dentro
que no es una medicion nueva. La version sin ese bloque se puede cotejar contra el
commit `d3e2c8f6`, leido con `git log --diff-filter=A`. **Tocar una apertura
sellada al cierre es exactamente la especie que esta casa vigila**, y **tambien es
la segunda vuelta seguida**: la 193 lo conto como su `C.3`.

**`C.3` (DE METODO, Y ES LA CAUSA DE LAS DOS DE ARRIBA). CLONE EL BLOQUE DE
APERTURA DE LA 193 SIN LEER LA SECCION 8.1 DE SU PROPIO REPORTE**, que declaraba
esas dos caidas con su nombre y su remedio. **Un clon declarado hereda tambien los
defectos declarados de su fuente**, y el sitio donde estan escritos es el reporte
de esa vuelta. **El remedio durable, nombrado y no hecho aqui:** que el bloque de
apertura corra el ciclo completo, incluidos `tsc` y `pnpm test`, y que escriba el
los dos literales que la guarda `D.1` busca. Mientras las dos redacciones no se
toquen, **estas dos caidas se heredan de vuelta en vuelta**, que es justo lo que
acaba de pasar dos veces.

## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE

**CORRIDA ENTERA Y SOLA, Y SU SALIDA VA AQUI COMPLETA Y SIN RECORTAR.**
Fichero: `docs/loop/SALIDA_V194_BATERIA.txt` (**102495 bytes en disco y 102495 normalizado a LF**, **1352 lineas
no vacias**, contadas
por `scripts/loop/cerrar_reporte.py`). **Este instrumento CAE EN ROJO si esta
seccion se queda sin ella**, que es la cuarta de sus cuatro piezas.

```
LA BATERIA DE MUTACIONES DE LA VUELTA 194, CORRIDA ENTERA Y EN TRAMOS
compuesta por scripts/loop/vuelta194_bateria_por_tramos.py --componer

LO QUE SE PARTIO ES EL BOCADO, NO LA BATERIA. Las cuatro cosas que la
letra del fundador del 5 sep 2026 fija siguen enteras: la cadencia (cada
cinco vueltas), la soledad (vuelta propia sin nada al lado), la
integridad (cada entrada corrida, y corrida DOS VECES) y la prohibicion
de podar la nomina.

CIFRA entradas de la nomina: 127
CIFRA tramos: 10
CIFRA entradas que los tramos dicen haber corrido: 127
CIFRA entradas sin correr: 0 | repetidas: 0 | ajenas: 0
LA COBERTURA SE LEYO DE LAS SALIDAS, no se recalculo del reparto.

  tramo 1 -> SALIDA_V194_BATERIA_TRAMO_1.txt: 11284 bytes disco, 11284 bytes LF, 143 lineas, sha256 a4db8c7b420a78d6
  tramo 2 -> SALIDA_V194_BATERIA_TRAMO_2.txt: 9528 bytes disco, 9528 bytes LF, 137 lineas, sha256 0a08458bafc60207
  tramo 3 -> SALIDA_V194_BATERIA_TRAMO_3.txt: 9582 bytes disco, 9582 bytes LF, 137 lineas, sha256 b5f1b65a553e7789
  tramo 4 -> SALIDA_V194_BATERIA_TRAMO_4.txt: 9596 bytes disco, 9596 bytes LF, 137 lineas, sha256 984584039c88a377
  tramo 5 -> SALIDA_V194_BATERIA_TRAMO_5.txt: 9559 bytes disco, 9559 bytes LF, 137 lineas, sha256 614226f68f138778
  tramo 6 -> SALIDA_V194_BATERIA_TRAMO_6.txt: 9605 bytes disco, 9605 bytes LF, 137 lineas, sha256 6ace42fc6b5a7d88
  tramo 7 -> SALIDA_V194_BATERIA_TRAMO_7.txt: 9815 bytes disco, 9815 bytes LF, 139 lineas, sha256 2a40104d3fbf6f00
  tramo 8 -> SALIDA_V194_BATERIA_TRAMO_8.txt: 9581 bytes disco, 9581 bytes LF, 137 lineas, sha256 5fb1efd65e7795b9
  tramo 9 -> SALIDA_V194_BATERIA_TRAMO_9.txt: 10058 bytes disco, 10058 bytes LF, 137 lineas, sha256 64042ebd6bfe3271
  tramo 10 -> SALIDA_V194_BATERIA_TRAMO_10.txt: 9492 bytes disco, 9492 bytes LF, 128 lineas, sha256 36e2d04ffc835786
==============================================================================

==============================================================================
TRAMO 1 DE 10. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V194_BATERIA_TRAMO_1.txt
==============================================================================

CORRIDA DEL TRAMO 1 DE 10, BATERIA DE LA VUELTA 194
lanzada por scripts/loop/vuelta194_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-06T22:01:57Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 127 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 127 (corte: HEAD e6f46677ab23, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 193
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 127 (corte: HEAD e6f46677ab23, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 190 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 127 (corte: HEAD e6f46677ab23, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 10
  CIFRA TRAMO QUE SE CORRE: 1 de 10
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 127
      ENTRADA DEL TRAMO: vuelta133_tarea2e_mutacion_cifras.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_1.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_2.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_3.py
      ENTRADA DEL TRAMO: vuelta139_2b_mutaciones.py
      ENTRADA DEL TRAMO: vuelta140_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta141_2_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2b_mutacion_bateria.py
      ENTRADA DEL TRAMO: vuelta143_2c_mutacion_positivo.py
      ENTRADA DEL TRAMO: vuelta144_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_2b_mutacion_giro.py
      ENTRADA DEL TRAMO: vuelta144_2d_mutacion_cobertura.py


  vuelta133_tarea2e_mutacion_cifras.py   exit 0  OK                  14.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta135_2e_mutacion_1.py             exit 0  OK                   3.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_1.txt
  vuelta135_2e_mutacion_2.py             exit 0  OK                   3.2s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_2.txt
  vuelta135_2e_mutacion_3.py             exit 1  CASO DECLARADO       3.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_3.txt
      SUJETO FIJO VERIFICADO: SUJETO_FIJO_V135_2E_REPORTE_134.md calza con el blob e12e4c36 (sha256 d1f97a510f17e35046eeec4975e1e0a1adabcfdda5a4646a250aa6db
  vuelta139_2b_mutaciones.py             exit 0  OK                   5.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta140_2a_mutaciones.py             exit 2  CASO DECLARADO       4.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta141_2_mutaciones.py              exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2a_mutaciones.py             exit 0  OK                   5.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2b_mutacion_bateria.py       exit 0  OK                   4.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2c_mutacion_positivo.py      exit 0  OK                   4.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2a_mutaciones.py             exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2b_mutacion_giro.py          exit 0  OK                   7.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2d_mutacion_cobertura.py     exit 0  OK                   4.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 65.8
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.1
  CIFRA arnes MAS LENTO: vuelta133_tarea2e_mutacion_cifras.py con 14.8s
  CIFRA arnes MAS RAPIDO: vuelta144_2a_mutaciones.py con 2.4s
  CIFRA mediana por arnes, en segundos: 4.3
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta133_tarea2e_mutacion_cifras.py          14.8s
      vuelta144_2b_mutacion_giro.py                  7.0s
      vuelta143_2a_mutaciones.py                     5.2s
      vuelta139_2b_mutaciones.py                     5.1s
      vuelta140_2a_mutaciones.py                     4.9s
      vuelta144_2d_mutacion_cobertura.py             4.5s
      vuelta143_2b_mutacion_bateria.py               4.3s
      vuelta143_2c_mutacion_positivo.py              4.3s
      vuelta135_2e_mutacion_1.py                     3.8s
      vuelta135_2e_mutacion_3.py                     3.4s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 2 (vuelta135_2e_mutacion_3.py, vuelta140_2a_mutaciones.py)
      vuelta135_2e_mutacion_3.py, exit declarado 1, marca obligatoria 'NO TIENE CONVENCION MECANICA DE CONTEO':
         su SUJETO FIJO es el REPORTE.md de la vuelta 134, congelado por banco 9.10, y ES ANTERIOR A LOS DELIMITADORES DE CABECERA TALLADA. Medido en esta vuelta: grep -c 'CABECERA TALLADA' docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md da 0, y sobre docs/loop/REPORTE.md da 3. La ampliacion del vocabulario de la TAREA 2.a (vuelta 142) hace que la guarda vea ahora la celda '3 fila(s)' del desfase del calibrado, que EN UN REPORTE MODERNO vive DENTRO de la cabecera delimitada y queda recortada antes de parsear, y en este sujeto no, porque las marcas no existian aun. LAS DOS CIFRAS QUE ESTA MUTACION PRUEBA SI COTEJAN (la salida publica '2 POR ETIQUETA'): lo que cae es una tercera, ajena al caso. El sujeto NO se retoca, porque su valor es estar congelado.
      vuelta140_2a_mutaciones.py, exit declarado 2, marca obligatoria 'VEREDICTO (iii): NO CALZA':
         su bloque (iii), el caso positivo sobre la fase 05, sale NO CALZA y esta DECLARADO desde la vuelta 140: el auditor lo reconocio como caida SUYA de encargo (acta 140, 4.5, 'EL AUDITOR ELIGIO MAL EL SUJETO CONGELADO'). OP-S-05, OP-S-08, OP-S-11 y OP-S-12 tienen HUELLA DE GRAFO IDENTICA (los cuatro campos vacios) y lo unico que las separa es `estado`, que el encargo prohibe mirar: NINGUNA VARA DE GRAFO PUEDE SEPARARLAS. Los bloques (i) y (ii) SI muerden y son los que esta bateria vigila.
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 127 (corte: HEAD e6f46677ab23, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 3, de 127 (corte: HEAD e6f46677ab23, nomina contada en esta corrida)
      SUJETO SIN CONGELAR: vuelta186_tarea2c_mutacion_cierre_tardio.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta187_tarea4_mutacion_dos_convenciones.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta188_tarea4_mutacion_cobertura_parejas.py NO DECIDIBLE   abre REPORTE.md
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 6 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 3 NO DECIDIBLE con motivo escrito, 0 sin
         CON MOTIVO ESCRITO     vuelta186_tarea2c_mutacion_cierre_tardio.py
         CON MOTIVO ESCRITO     vuelta187_tarea4_mutacion_dos_convenciones.py
         CON MOTIVO ESCRITO     vuelta188_tarea4_mutacion_cobertura_parejas.py
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 6 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta191_tarea3_mutacion_lineas.py, vuelta191_tarea4_mutacion_veredicto.py, vuelta191_tarea6_mutacion_bloque_tallado.py, vuelta192_tarea4_mutacion_cuarta_puerta.py, vuelta193_tarea4e_mutacion_sello_entre_procesos.py, vuelta194_tarea2c_mutacion_sede_del_turno.py
ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado. La regla es de la vuelta 145 y su condicion la fijo la 148: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y la que no pueda tenerlo entra como CASO DECLARADO. Un arnes anclado a un fichero que la campana mueve cada vuelta no mide su maquina, mide el dia. La lista entera: vuelta186_tarea2c_mutacion_cierre_tardio.py, vuelta187_tarea4_mutacion_dos_convenciones.py, vuelta188_tarea4_mutacion_cobertura_parejas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 1: 1
FIN (reloj de pared, UTC): 2026-09-06T22:03:05Z
DURACION DEL TRAMO (monotona, segundos): 68.0
DURACION DEL TRAMO (monotona, minutos): 1.1


==============================================================================
TRAMO 2 DE 10. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V194_BATERIA_TRAMO_2.txt
==============================================================================

CORRIDA DEL TRAMO 2 DE 10, BATERIA DE LA VUELTA 194
lanzada por scripts/loop/vuelta194_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-06T22:04:28Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 127 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 127 (corte: HEAD 6a508ca56b42, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 193
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 127 (corte: HEAD 6a508ca56b42, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 190 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 127 (corte: HEAD 6a508ca56b42, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 10
  CIFRA TRAMO QUE SE CORRE: 2 de 10
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 127
      ENTRADA DEL TRAMO: vuelta144_3a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_3b_mutacion_negativa.py
      ENTRADA DEL TRAMO: vuelta144_3c_caso_positivo_1190.py
      ENTRADA DEL TRAMO: vuelta145_2a_mutacion_ancla_unica.py
      ENTRADA DEL TRAMO: vuelta145_2b_mutacion_arneses.py
      ENTRADA DEL TRAMO: vuelta145_2c_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta146_2b_mutacion_ausencias.py
      ENTRADA DEL TRAMO: vuelta147_2c_mutacion_vitalidad.py
      ENTRADA DEL TRAMO: vuelta147_3d_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta147_3e_simular_a26.py
      ENTRADA DEL TRAMO: vuelta148_0d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta148_1a_mutacion_embebido.py
      ENTRADA DEL TRAMO: vuelta148_2a_mutacion_nomina_commiteada.py


  vuelta144_3a_mutaciones.py             exit 0  OK                   4.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3b_mutacion_negativa.py      exit 0  OK                  12.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3c_caso_positivo_1190.py     exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2a_mutacion_ancla_unica.py   exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2b_mutacion_arneses.py       exit 0  OK                  18.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2c_mutacion_censo.py         exit 0  OK                  11.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta146_2b_mutacion_ausencias.py     exit 0  OK                   3.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_2c_mutacion_vitalidad.py     exit 0  OK                  91.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3d_mutacion_nomina.py        exit 0  OK                   4.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3e_simular_a26.py            exit 0  OK                   4.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_0d_mutacion_corredor.py      exit 0  OK                   5.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_1a_mutacion_embebido.py      exit 0  OK                   5.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2a_mutacion_nomina_commiteada.py exit 0  OK                   3.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 170.6
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.8
  CIFRA arnes MAS LENTO: vuelta147_2c_mutacion_vitalidad.py con 91.2s
  CIFRA arnes MAS RAPIDO: vuelta145_2a_mutacion_ancla_unica.py con 2.5s
  CIFRA mediana por arnes, en segundos: 4.7
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta147_2c_mutacion_vitalidad.py            91.2s
      vuelta145_2b_mutacion_arneses.py              18.1s
      vuelta144_3b_mutacion_negativa.py             12.2s
      vuelta145_2c_mutacion_censo.py                11.8s
      vuelta148_1a_mutacion_embebido.py              5.9s
      vuelta148_0d_mutacion_corredor.py              5.4s
      vuelta147_3d_mutacion_nomina.py                4.7s
      vuelta147_3e_simular_a26.py                    4.7s
      vuelta144_3a_mutaciones.py                     4.4s
      vuelta148_2a_mutacion_nomina_commiteada.py     3.7s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 127 (corte: HEAD 6a508ca56b42, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 3, de 127 (corte: HEAD 6a508ca56b42, nomina contada en esta corrida)
      SUJETO SIN CONGELAR: vuelta186_tarea2c_mutacion_cierre_tardio.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta187_tarea4_mutacion_dos_convenciones.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta188_tarea4_mutacion_cobertura_parejas.py NO DECIDIBLE   abre REPORTE.md
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 6 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 3 NO DECIDIBLE con motivo escrito, 0 sin
         CON MOTIVO ESCRITO     vuelta186_tarea2c_mutacion_cierre_tardio.py
         CON MOTIVO ESCRITO     vuelta187_tarea4_mutacion_dos_convenciones.py
         CON MOTIVO ESCRITO     vuelta188_tarea4_mutacion_cobertura_parejas.py
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 6 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta191_tarea3_mutacion_lineas.py, vuelta191_tarea4_mutacion_veredicto.py, vuelta191_tarea6_mutacion_bloque_tallado.py, vuelta192_tarea4_mutacion_cuarta_puerta.py, vuelta193_tarea4e_mutacion_sello_entre_procesos.py, vuelta194_tarea2c_mutacion_sede_del_turno.py
ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado. La regla es de la vuelta 145 y su condicion la fijo la 148: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y la que no pueda tenerlo entra como CASO DECLARADO. Un arnes anclado a un fichero que la campana mueve cada vuelta no mide su maquina, mide el dia. La lista entera: vuelta186_tarea2c_mutacion_cierre_tardio.py, vuelta187_tarea4_mutacion_dos_convenciones.py, vuelta188_tarea4_mutacion_cobertura_parejas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 2: 1
FIN (reloj de pared, UTC): 2026-09-06T22:07:20Z
DURACION DEL TRAMO (monotona, segundos): 171.9
DURACION DEL TRAMO (monotona, minutos): 2.9


==============================================================================
TRAMO 3 DE 10. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V194_BATERIA_TRAMO_3.txt
==============================================================================

CORRIDA DEL TRAMO 3 DE 10, BATERIA DE LA VUELTA 194
lanzada por scripts/loop/vuelta194_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-06T22:15:06Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 127 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 127 (corte: HEAD 2d51cc92cc80, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 193
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 127 (corte: HEAD 2d51cc92cc80, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 190 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 127 (corte: HEAD 2d51cc92cc80, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 10
  CIFRA TRAMO QUE SE CORRE: 3 de 10
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 127
      ENTRADA DEL TRAMO: vuelta148_2b_mutacion_cifras_conjunto.py
      ENTRADA DEL TRAMO: vuelta148_2c_mutacion_vara_parada.py
      ENTRADA DEL TRAMO: vuelta148_2d_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta150_5c_mutacion_ciclo.py
      ENTRADA DEL TRAMO: vuelta154_tarea2d_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta154_tarea6_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta156_tarea4b_mutacion_tallador.py
      ENTRADA DEL TRAMO: vuelta156_tarea5d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta157_tarea4b_mutacion_tachado.py
      ENTRADA DEL TRAMO: vuelta157_tarea5c_mutacion_ruido.py
      ENTRADA DEL TRAMO: vuelta157_tarea6b_mutacion_re_sellado.py
      ENTRADA DEL TRAMO: vuelta159_tarea6c_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta160_tarea6b_mutacion_puerta.py


  vuelta148_2b_mutacion_cifras_conjunto.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2c_mutacion_vara_parada.py   exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2d_mutacion_exencion.py      exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta150_5c_mutacion_ciclo.py         exit 0  OK                   3.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta154_tarea2d_mutacion_guarda.py   exit 0  OK                 105.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta154_tarea6_mutacion_corredor.py  exit 0  OK                   4.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea4b_mutacion_tallador.py exit 0  OK                   3.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea5d_mutacion_corredor.py exit 0  OK                  29.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea4b_mutacion_tachado.py  exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea5c_mutacion_ruido.py    exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea6b_mutacion_re_sellado.py exit 0  OK                   4.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta159_tarea6c_mutacion_exencion.py exit 0  OK                 235.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea6b_mutacion_puerta.py   exit 0  OK                  52.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 452.2
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 7.5
  CIFRA arnes MAS LENTO: vuelta159_tarea6c_mutacion_exencion.py con 235.4s
  CIFRA arnes MAS RAPIDO: vuelta148_2c_mutacion_vara_parada.py con 2.4s
  CIFRA mediana por arnes, en segundos: 3.4
  CIFRA arneses que pasan de 30 segundos: 3
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta159_tarea6c_mutacion_exencion.py       235.4s
      vuelta154_tarea2d_mutacion_guarda.py         105.4s
      vuelta160_tarea6b_mutacion_puerta.py          52.2s
      vuelta156_tarea5d_mutacion_corredor.py        29.9s
      vuelta157_tarea6b_mutacion_re_sellado.py       4.9s
      vuelta154_tarea6_mutacion_corredor.py          4.7s
      vuelta150_5c_mutacion_ciclo.py                 3.4s
      vuelta156_tarea4b_mutacion_tallador.py         3.4s
      vuelta157_tarea5c_mutacion_ruido.py            3.0s
      vuelta157_tarea4b_mutacion_tachado.py          2.7s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 127 (corte: HEAD 2d51cc92cc80, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 3, de 127 (corte: HEAD 2d51cc92cc80, nomina contada en esta corrida)
      SUJETO SIN CONGELAR: vuelta186_tarea2c_mutacion_cierre_tardio.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta187_tarea4_mutacion_dos_convenciones.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta188_tarea4_mutacion_cobertura_parejas.py NO DECIDIBLE   abre REPORTE.md
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 6 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 3 NO DECIDIBLE con motivo escrito, 0 sin
         CON MOTIVO ESCRITO     vuelta186_tarea2c_mutacion_cierre_tardio.py
         CON MOTIVO ESCRITO     vuelta187_tarea4_mutacion_dos_convenciones.py
         CON MOTIVO ESCRITO     vuelta188_tarea4_mutacion_cobertura_parejas.py
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 6 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta191_tarea3_mutacion_lineas.py, vuelta191_tarea4_mutacion_veredicto.py, vuelta191_tarea6_mutacion_bloque_tallado.py, vuelta192_tarea4_mutacion_cuarta_puerta.py, vuelta193_tarea4e_mutacion_sello_entre_procesos.py, vuelta194_tarea2c_mutacion_sede_del_turno.py
ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado. La regla es de la vuelta 145 y su condicion la fijo la 148: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y la que no pueda tenerlo entra como CASO DECLARADO. Un arnes anclado a un fichero que la campana mueve cada vuelta no mide su maquina, mide el dia. La lista entera: vuelta186_tarea2c_mutacion_cierre_tardio.py, vuelta187_tarea4_mutacion_dos_convenciones.py, vuelta188_tarea4_mutacion_cobertura_parejas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 3: 1
FIN (reloj de pared, UTC): 2026-09-06T22:22:40Z
DURACION DEL TRAMO (monotona, segundos): 453.6
DURACION DEL TRAMO (monotona, minutos): 7.6


==============================================================================
TRAMO 4 DE 10. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V194_BATERIA_TRAMO_4.txt
==============================================================================

CORRIDA DEL TRAMO 4 DE 10, BATERIA DE LA VUELTA 194
lanzada por scripts/loop/vuelta194_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-06T22:23:24Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 127 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 127 (corte: HEAD cd0a5cd098f7, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 193
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 127 (corte: HEAD cd0a5cd098f7, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 190 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 127 (corte: HEAD cd0a5cd098f7, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 10
  CIFRA TRAMO QUE SE CORRE: 4 de 10
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 127
      ENTRADA DEL TRAMO: vuelta160_tarea7c_mutacion_guarda_cita.py
      ENTRADA DEL TRAMO: vuelta161_tarea1a_mutacion_alcance.py
      ENTRADA DEL TRAMO: vuelta162_tarea1a_mutacion_serie.py
      ENTRADA DEL TRAMO: vuelta162_tarea2a_mutacion_puerta.py
      ENTRADA DEL TRAMO: vuelta162_tarea2b_mutacion_excepcion.py
      ENTRADA DEL TRAMO: vuelta162_tarea3_mutacion_fila.py
      ENTRADA DEL TRAMO: vuelta163_tarea1b_mutacion_relectura.py
      ENTRADA DEL TRAMO: vuelta163_tarea1c_mutacion_tramo.py
      ENTRADA DEL TRAMO: vuelta163_tarea2_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta163_tarea4a_mutacion_cobertura.py
      ENTRADA DEL TRAMO: vuelta163_tarea4b_mutacion_re_sellado.py
      ENTRADA DEL TRAMO: vuelta163_tarea5a_mutacion_contador.py
      ENTRADA DEL TRAMO: vuelta164_tarea1_mutacion_registro.py


  vuelta160_tarea7c_mutacion_guarda_cita.py exit 0  OK                   8.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta161_tarea1a_mutacion_alcance.py  exit 0  OK                  11.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea1a_mutacion_serie.py    exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2a_mutacion_puerta.py   exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2b_mutacion_excepcion.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea3_mutacion_fila.py      exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1b_mutacion_relectura.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1c_mutacion_tramo.py    exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea2_mutacion_nomina.py    exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4a_mutacion_cobertura.py exit 0  OK                   4.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4b_mutacion_re_sellado.py exit 0  OK                  35.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea5a_mutacion_contador.py exit 0  OK                   4.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta164_tarea1_mutacion_registro.py  exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 84.6
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.4
  CIFRA arnes MAS LENTO: vuelta163_tarea4b_mutacion_re_sellado.py con 35.6s
  CIFRA arnes MAS RAPIDO: vuelta164_tarea1_mutacion_registro.py con 2.3s
  CIFRA mediana por arnes, en segundos: 2.5
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta163_tarea4b_mutacion_re_sellado.py      35.6s
      vuelta161_tarea1a_mutacion_alcance.py         11.8s
      vuelta160_tarea7c_mutacion_guarda_cita.py      8.0s
      vuelta163_tarea4a_mutacion_cobertura.py        4.8s
      vuelta163_tarea5a_mutacion_contador.py         4.5s
      vuelta162_tarea3_mutacion_fila.py              3.0s
      vuelta162_tarea2b_mutacion_excepcion.py        2.5s
      vuelta163_tarea2_mutacion_nomina.py            2.5s
      vuelta162_tarea1a_mutacion_serie.py            2.4s
      vuelta163_tarea1b_mutacion_relectura.py        2.4s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 127 (corte: HEAD cd0a5cd098f7, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 3, de 127 (corte: HEAD cd0a5cd098f7, nomina contada en esta corrida)
      SUJETO SIN CONGELAR: vuelta186_tarea2c_mutacion_cierre_tardio.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta187_tarea4_mutacion_dos_convenciones.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta188_tarea4_mutacion_cobertura_parejas.py NO DECIDIBLE   abre REPORTE.md
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 6 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 3 NO DECIDIBLE con motivo escrito, 0 sin
         CON MOTIVO ESCRITO     vuelta186_tarea2c_mutacion_cierre_tardio.py
         CON MOTIVO ESCRITO     vuelta187_tarea4_mutacion_dos_convenciones.py
         CON MOTIVO ESCRITO     vuelta188_tarea4_mutacion_cobertura_parejas.py
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 6 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta191_tarea3_mutacion_lineas.py, vuelta191_tarea4_mutacion_veredicto.py, vuelta191_tarea6_mutacion_bloque_tallado.py, vuelta192_tarea4_mutacion_cuarta_puerta.py, vuelta193_tarea4e_mutacion_sello_entre_procesos.py, vuelta194_tarea2c_mutacion_sede_del_turno.py
ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado. La regla es de la vuelta 145 y su condicion la fijo la 148: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y la que no pueda tenerlo entra como CASO DECLARADO. Un arnes anclado a un fichero que la campana mueve cada vuelta no mide su maquina, mide el dia. La lista entera: vuelta186_tarea2c_mutacion_cierre_tardio.py, vuelta187_tarea4_mutacion_dos_convenciones.py, vuelta188_tarea4_mutacion_cobertura_parejas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 4: 1
FIN (reloj de pared, UTC): 2026-09-06T22:24:50Z
DURACION DEL TRAMO (monotona, segundos): 85.9
DURACION DEL TRAMO (monotona, minutos): 1.4


==============================================================================
TRAMO 5 DE 10. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V194_BATERIA_TRAMO_5.txt
==============================================================================

CORRIDA DEL TRAMO 5 DE 10, BATERIA DE LA VUELTA 194
lanzada por scripts/loop/vuelta194_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-06T22:25:18Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 127 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 127 (corte: HEAD daf4241f1dd4, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 193
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 127 (corte: HEAD daf4241f1dd4, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 190 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 127 (corte: HEAD daf4241f1dd4, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 10
  CIFRA TRAMO QUE SE CORRE: 5 de 10
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 127
      ENTRADA DEL TRAMO: vuelta164_tarea4_mutacion_005.py
      ENTRADA DEL TRAMO: vuelta165_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta165_tarea2_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta165_tarea4_mutacion_sujeto.py
      ENTRADA DEL TRAMO: vuelta165_tarea6_mutacion_op_l_01.py
      ENTRADA DEL TRAMO: vuelta166_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta166_tarea2_mutacion_correccion.py
      ENTRADA DEL TRAMO: vuelta166_tarea3_mutacion_retrato.py
      ENTRADA DEL TRAMO: vuelta166_tarea6_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta167_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta167_tarea3_mutacion_ii.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_nota.py


  vuelta164_tarea4_mutacion_005.py       exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea1_mutacion_registro.py  exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea2_mutacion_censo.py     exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea4_mutacion_sujeto.py    exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea6_mutacion_op_l_01.py   exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea1_mutacion_registro.py  exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea2_mutacion_correccion.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea3_mutacion_retrato.py   exit 0  OK                   6.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea6_mutacion_guarda.py    exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta167_tarea1_mutacion_registro.py  exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta167_tarea3_mutacion_ii.py        exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_registro.py  exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_nota.py      exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 37.2
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.6
  CIFRA arnes MAS LENTO: vuelta166_tarea3_mutacion_retrato.py con 6.5s
  CIFRA arnes MAS RAPIDO: vuelta168_tarea1_mutacion_registro.py con 2.3s
  CIFRA mediana por arnes, en segundos: 2.5
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta166_tarea3_mutacion_retrato.py           6.5s
      vuelta166_tarea2_mutacion_correccion.py        3.1s
      vuelta167_tarea3_mutacion_ii.py                3.0s
      vuelta165_tarea4_mutacion_sujeto.py            2.7s
      vuelta168_tarea1_mutacion_nota.py              2.5s
      vuelta166_tarea6_mutacion_guarda.py            2.5s
      vuelta165_tarea2_mutacion_censo.py             2.5s
      vuelta164_tarea4_mutacion_005.py               2.5s
      vuelta165_tarea6_mutacion_op_l_01.py           2.5s
      vuelta165_tarea1_mutacion_registro.py          2.4s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 127 (corte: HEAD daf4241f1dd4, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 3, de 127 (corte: HEAD daf4241f1dd4, nomina contada en esta corrida)
      SUJETO SIN CONGELAR: vuelta186_tarea2c_mutacion_cierre_tardio.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta187_tarea4_mutacion_dos_convenciones.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta188_tarea4_mutacion_cobertura_parejas.py NO DECIDIBLE   abre REPORTE.md
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 6 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 3 NO DECIDIBLE con motivo escrito, 0 sin
         CON MOTIVO ESCRITO     vuelta186_tarea2c_mutacion_cierre_tardio.py
         CON MOTIVO ESCRITO     vuelta187_tarea4_mutacion_dos_convenciones.py
         CON MOTIVO ESCRITO     vuelta188_tarea4_mutacion_cobertura_parejas.py
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 6 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta191_tarea3_mutacion_lineas.py, vuelta191_tarea4_mutacion_veredicto.py, vuelta191_tarea6_mutacion_bloque_tallado.py, vuelta192_tarea4_mutacion_cuarta_puerta.py, vuelta193_tarea4e_mutacion_sello_entre_procesos.py, vuelta194_tarea2c_mutacion_sede_del_turno.py
ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado. La regla es de la vuelta 145 y su condicion la fijo la 148: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y la que no pueda tenerlo entra como CASO DECLARADO. Un arnes anclado a un fichero que la campana mueve cada vuelta no mide su maquina, mide el dia. La lista entera: vuelta186_tarea2c_mutacion_cierre_tardio.py, vuelta187_tarea4_mutacion_dos_convenciones.py, vuelta188_tarea4_mutacion_cobertura_parejas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 5: 1
FIN (reloj de pared, UTC): 2026-09-06T22:25:57Z
DURACION DEL TRAMO (monotona, segundos): 38.4
DURACION DEL TRAMO (monotona, minutos): 0.6


==============================================================================
TRAMO 6 DE 10. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V194_BATERIA_TRAMO_6.txt
==============================================================================

CORRIDA DEL TRAMO 6 DE 10, BATERIA DE LA VUELTA 194
lanzada por scripts/loop/vuelta194_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-06T22:26:26Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 127 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 127 (corte: HEAD 14b340a5f128, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 193
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 127 (corte: HEAD 14b340a5f128, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 190 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 127 (corte: HEAD 14b340a5f128, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 10
  CIFRA TRAMO QUE SE CORRE: 6 de 10
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 127
      ENTRADA DEL TRAMO: vuelta168_tarea2_mutacion_reconstructor.py
      ENTRADA DEL TRAMO: vuelta168_tarea4_mutacion_op_v_01.py
      ENTRADA DEL TRAMO: vuelta169_tarea2_mutacion_reanclaje.py
      ENTRADA DEL TRAMO: vuelta170_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta170_tarea2a_mutacion_aislador.py
      ENTRADA DEL TRAMO: vuelta98_tarea4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta99_tarea3_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta109_tarea2_4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py
      ENTRADA DEL TRAMO: vuelta113_tarea2_mutacion_tsc.py
      ENTRADA DEL TRAMO: vuelta171_mutacion_busqueda_acta.py
      ENTRADA DEL TRAMO: vuelta171_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta171_tarea5a_mutacion_enchufe.py


  vuelta168_tarea2_mutacion_reconstructor.py exit 0  OK                   4.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea4_mutacion_op_v_01.py   exit 0  OK                  16.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta169_tarea2_mutacion_reanclaje.py exit 0  OK                   2.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea1a_mutacion_registro.py exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea2a_mutacion_aislador.py exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta98_tarea4_prueba_mutacion.py     exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta99_tarea3_prueba_mutacion.py     exit 0  OK                   2.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta109_tarea2_4_prueba_mutacion.py  exit 0  OK                  16.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta113_tarea2_mutacion_tsc.py       exit 0  OK                   2.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_mutacion_busqueda_acta.py    exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_tarea1a_mutacion_registro.py exit 0  OK                   3.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_tarea5a_mutacion_enchufe.py  exit 0  OK                   3.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 62.3
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.0
  CIFRA arnes MAS LENTO: vuelta168_tarea4_mutacion_op_v_01.py con 16.9s
  CIFRA arnes MAS RAPIDO: vuelta113_tarea2_mutacion_tsc.py con 2.2s
  CIFRA mediana por arnes, en segundos: 2.3
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta168_tarea4_mutacion_op_v_01.py          16.9s
      vuelta109_tarea2_4_prueba_mutacion.py         16.1s
      vuelta168_tarea2_mutacion_reconstructor.py     4.1s
      vuelta171_tarea5a_mutacion_enchufe.py          3.6s
      vuelta171_tarea1a_mutacion_registro.py         3.2s
      vuelta171_mutacion_busqueda_acta.py            2.6s
      vuelta170_tarea1a_mutacion_registro.py         2.3s
      vuelta98_tarea4_prueba_mutacion.py             2.3s
      vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py     2.3s
      vuelta170_tarea2a_mutacion_aislador.py         2.3s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 127 (corte: HEAD 14b340a5f128, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 3, de 127 (corte: HEAD 14b340a5f128, nomina contada en esta corrida)
      SUJETO SIN CONGELAR: vuelta186_tarea2c_mutacion_cierre_tardio.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta187_tarea4_mutacion_dos_convenciones.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta188_tarea4_mutacion_cobertura_parejas.py NO DECIDIBLE   abre REPORTE.md
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 6 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 3 NO DECIDIBLE con motivo escrito, 0 sin
         CON MOTIVO ESCRITO     vuelta186_tarea2c_mutacion_cierre_tardio.py
         CON MOTIVO ESCRITO     vuelta187_tarea4_mutacion_dos_convenciones.py
         CON MOTIVO ESCRITO     vuelta188_tarea4_mutacion_cobertura_parejas.py
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 6 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta191_tarea3_mutacion_lineas.py, vuelta191_tarea4_mutacion_veredicto.py, vuelta191_tarea6_mutacion_bloque_tallado.py, vuelta192_tarea4_mutacion_cuarta_puerta.py, vuelta193_tarea4e_mutacion_sello_entre_procesos.py, vuelta194_tarea2c_mutacion_sede_del_turno.py
ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado. La regla es de la vuelta 145 y su condicion la fijo la 148: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y la que no pueda tenerlo entra como CASO DECLARADO. Un arnes anclado a un fichero que la campana mueve cada vuelta no mide su maquina, mide el dia. La lista entera: vuelta186_tarea2c_mutacion_cierre_tardio.py, vuelta187_tarea4_mutacion_dos_convenciones.py, vuelta188_tarea4_mutacion_cobertura_parejas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 6: 1
FIN (reloj de pared, UTC): 2026-09-06T22:27:29Z
DURACION DEL TRAMO (monotona, segundos): 63.7
DURACION DEL TRAMO (monotona, minutos): 1.1


==============================================================================
TRAMO 7 DE 10. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V194_BATERIA_TRAMO_7.txt
==============================================================================

CORRIDA DEL TRAMO 7 DE 10, BATERIA DE LA VUELTA 194
lanzada por scripts/loop/vuelta194_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-06T22:28:01Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 127 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 127 (corte: HEAD aa2351091907, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 193
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 127 (corte: HEAD aa2351091907, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 190 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 127 (corte: HEAD aa2351091907, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 10
  CIFRA TRAMO QUE SE CORRE: 7 de 10
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 127
      ENTRADA DEL TRAMO: vuelta172_tarea1b_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta172_tarea2a_mutacion_exclusion.py
      ENTRADA DEL TRAMO: vuelta172_tarea3_mutacion_numeracion.py
      ENTRADA DEL TRAMO: vuelta172_tarea5_mutacion_cierre.py
      ENTRADA DEL TRAMO: vuelta173_tarea1b_mutacion_hueco.py
      ENTRADA DEL TRAMO: vuelta174_tarea1a_mutacion_44.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_esqueleto.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_sellar.py
      ENTRADA DEL TRAMO: vuelta174_tarea2b_mutacion_confirmar.py
      ENTRADA DEL TRAMO: vuelta176_tarea1c_mutacion_tramos.py
      ENTRADA DEL TRAMO: vuelta177_tarea1b_mutacion_esperado_vivo.py
      ENTRADA DEL TRAMO: vuelta177_tarea1d_mutacion_cotejo.py
      ENTRADA DEL TRAMO: vuelta177_tarea1e_mutacion_correcciones_chicas.py


  vuelta172_tarea1b_mutacion_registro.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea2a_mutacion_exclusion.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea3_mutacion_numeracion.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea5_mutacion_cierre.py    exit 1  NO MORDIO            2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta173_tarea1b_mutacion_hueco.py    exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1a_mutacion_44.py       exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_esqueleto.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_sellar.py   exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea2b_mutacion_confirmar.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta176_tarea1c_mutacion_tramos.py   exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1b_mutacion_esperado_vivo.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1d_mutacion_cotejo.py   exit 0  OK                   3.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1e_mutacion_correcciones_chicas.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 33.0
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.6
  CIFRA arnes MAS LENTO: vuelta177_tarea1d_mutacion_cotejo.py con 3.3s
  CIFRA arnes MAS RAPIDO: vuelta174_tarea1b_mutacion_sellar.py con 2.3s
  CIFRA mediana por arnes, en segundos: 2.4
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta177_tarea1d_mutacion_cotejo.py           3.3s
      vuelta177_tarea1b_mutacion_esperado_vivo.py     3.1s
      vuelta174_tarea1b_mutacion_esqueleto.py        2.5s
      vuelta173_tarea1b_mutacion_hueco.py            2.5s
      vuelta174_tarea1a_mutacion_44.py               2.5s
      vuelta172_tarea1b_mutacion_registro.py         2.5s
      vuelta172_tarea2a_mutacion_exclusion.py        2.4s
      vuelta176_tarea1c_mutacion_tramos.py           2.4s
      vuelta172_tarea5_mutacion_cierre.py            2.4s
      vuelta174_tarea2b_mutacion_confirmar.py        2.4s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 1 (vuelta172_tarea5_mutacion_cierre.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 127 (corte: HEAD aa2351091907, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 3, de 127 (corte: HEAD aa2351091907, nomina contada en esta corrida)
      SUJETO SIN CONGELAR: vuelta186_tarea2c_mutacion_cierre_tardio.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta187_tarea4_mutacion_dos_convenciones.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta188_tarea4_mutacion_cobertura_parejas.py NO DECIDIBLE   abre REPORTE.md
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 1 que no mordieron, 0 sin reproducir, 6 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 3 NO DECIDIBLE con motivo escrito, 0 sin
         CON MOTIVO ESCRITO     vuelta186_tarea2c_mutacion_cierre_tardio.py
         CON MOTIVO ESCRITO     vuelta187_tarea4_mutacion_dos_convenciones.py
         CON MOTIVO ESCRITO     vuelta188_tarea4_mutacion_cobertura_parejas.py
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 6 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta191_tarea3_mutacion_lineas.py, vuelta191_tarea4_mutacion_veredicto.py, vuelta191_tarea6_mutacion_bloque_tallado.py, vuelta192_tarea4_mutacion_cuarta_puerta.py, vuelta193_tarea4e_mutacion_sello_entre_procesos.py, vuelta194_tarea2c_mutacion_sede_del_turno.py
ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado. La regla es de la vuelta 145 y su condicion la fijo la 148: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y la que no pueda tenerlo entra como CASO DECLARADO. Un arnes anclado a un fichero que la campana mueve cada vuelta no mide su maquina, mide el dia. La lista entera: vuelta186_tarea2c_mutacion_cierre_tardio.py, vuelta187_tarea4_mutacion_dos_convenciones.py, vuelta188_tarea4_mutacion_cobertura_parejas.py
ROJO: 0 con el ancla perdida, 1 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 7: 1
FIN (reloj de pared, UTC): 2026-09-06T22:28:35Z
DURACION DEL TRAMO (monotona, segundos): 34.3
DURACION DEL TRAMO (monotona, minutos): 0.6


==============================================================================
TRAMO 8 DE 10. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V194_BATERIA_TRAMO_8.txt
==============================================================================

CORRIDA DEL TRAMO 8 DE 10, BATERIA DE LA VUELTA 194
lanzada por scripts/loop/vuelta194_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-06T22:29:04Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 127 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 127 (corte: HEAD 845b5d13965a, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 193
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 127 (corte: HEAD 845b5d13965a, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 190 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 127 (corte: HEAD 845b5d13965a, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 10
  CIFRA TRAMO QUE SE CORRE: 8 de 10
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 127
      ENTRADA DEL TRAMO: vuelta177_tarea1f_mutacion_tope_minutos.py
      ENTRADA DEL TRAMO: vuelta178_tarea1b_mutacion_hermano.py
      ENTRADA DEL TRAMO: vuelta178_tarea1c_mutacion_ast.py
      ENTRADA DEL TRAMO: vuelta178_tarea1d_mutacion_puestos.py
      ENTRADA DEL TRAMO: vuelta178_tarea1e_mutacion_higiene.py
      ENTRADA DEL TRAMO: vuelta178_tarea2_mutacion_resolutor.py
      ENTRADA DEL TRAMO: vuelta178_tarea4_mutacion_consumidas.py
      ENTRADA DEL TRAMO: vuelta150_2d_simular_op_c_05.py
      ENTRADA DEL TRAMO: vuelta160_tarea3b_caso_positivo.py
      ENTRADA DEL TRAMO: vuelta179_tarea1b_mutacion_citas.py
      ENTRADA DEL TRAMO: vuelta179_tarea3_mutacion_triangulos.py
      ENTRADA DEL TRAMO: vuelta179_tarea1d_mutacion_corte.py
      ENTRADA DEL TRAMO: vuelta180_tarea1b_mutacion_etiqueta.py


  vuelta177_tarea1f_mutacion_tope_minutos.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1b_mutacion_hermano.py  exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1c_mutacion_ast.py      exit 0  OK                   3.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1d_mutacion_puestos.py  exit 0  OK                   5.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1e_mutacion_higiene.py  exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea2_mutacion_resolutor.py exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea4_mutacion_consumidas.py exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta150_2d_simular_op_c_05.py        exit 0  OK                   3.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea3b_caso_positivo.py     exit 0  OK                  12.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea1b_mutacion_citas.py    exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea3_mutacion_triangulos.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea1d_mutacion_corte.py    exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea1b_mutacion_etiqueta.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 46.9
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.8
  CIFRA arnes MAS LENTO: vuelta160_tarea3b_caso_positivo.py con 12.3s
  CIFRA arnes MAS RAPIDO: vuelta178_tarea4_mutacion_consumidas.py con 2.3s
  CIFRA mediana por arnes, en segundos: 2.6
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta160_tarea3b_caso_positivo.py            12.3s
      vuelta178_tarea1d_mutacion_puestos.py          5.3s
      vuelta150_2d_simular_op_c_05.py                3.8s
      vuelta178_tarea1c_mutacion_ast.py              3.3s
      vuelta180_tarea1b_mutacion_etiqueta.py         2.7s
      vuelta179_tarea3_mutacion_triangulos.py        2.7s
      vuelta179_tarea1d_mutacion_corte.py            2.6s
      vuelta178_tarea1b_mutacion_hermano.py          2.5s
      vuelta177_tarea1f_mutacion_tope_minutos.py     2.4s
      vuelta178_tarea1e_mutacion_higiene.py          2.4s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 127 (corte: HEAD 845b5d13965a, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 3, de 127 (corte: HEAD 845b5d13965a, nomina contada en esta corrida)
      SUJETO SIN CONGELAR: vuelta186_tarea2c_mutacion_cierre_tardio.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta187_tarea4_mutacion_dos_convenciones.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta188_tarea4_mutacion_cobertura_parejas.py NO DECIDIBLE   abre REPORTE.md
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 6 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 3 NO DECIDIBLE con motivo escrito, 0 sin
         CON MOTIVO ESCRITO     vuelta186_tarea2c_mutacion_cierre_tardio.py
         CON MOTIVO ESCRITO     vuelta187_tarea4_mutacion_dos_convenciones.py
         CON MOTIVO ESCRITO     vuelta188_tarea4_mutacion_cobertura_parejas.py
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 6 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta191_tarea3_mutacion_lineas.py, vuelta191_tarea4_mutacion_veredicto.py, vuelta191_tarea6_mutacion_bloque_tallado.py, vuelta192_tarea4_mutacion_cuarta_puerta.py, vuelta193_tarea4e_mutacion_sello_entre_procesos.py, vuelta194_tarea2c_mutacion_sede_del_turno.py
ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado. La regla es de la vuelta 145 y su condicion la fijo la 148: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y la que no pueda tenerlo entra como CASO DECLARADO. Un arnes anclado a un fichero que la campana mueve cada vuelta no mide su maquina, mide el dia. La lista entera: vuelta186_tarea2c_mutacion_cierre_tardio.py, vuelta187_tarea4_mutacion_dos_convenciones.py, vuelta188_tarea4_mutacion_cobertura_parejas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 8: 1
FIN (reloj de pared, UTC): 2026-09-06T22:29:53Z
DURACION DEL TRAMO (monotona, segundos): 48.3
DURACION DEL TRAMO (monotona, minutos): 0.8


==============================================================================
TRAMO 9 DE 10. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V194_BATERIA_TRAMO_9.txt
==============================================================================

CORRIDA DEL TRAMO 9 DE 10, BATERIA DE LA VUELTA 194
lanzada por scripts/loop/vuelta194_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-06T22:30:22Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 127 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 127 (corte: HEAD 4021f12f1efe, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 193
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 127 (corte: HEAD 4021f12f1efe, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 190 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 127 (corte: HEAD 4021f12f1efe, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 10
  CIFRA TRAMO QUE SE CORRE: 9 de 10
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 127
      ENTRADA DEL TRAMO: vuelta180_tarea2c_mutacion_cableado.py
      ENTRADA DEL TRAMO: vuelta180_tarea3_mutacion_corte_de_tramos.py
      ENTRADA DEL TRAMO: vuelta180_tarea4_mutacion_texto_y_clon.py
      ENTRADA DEL TRAMO: vuelta180_tarea5_mutacion_backlog_l02.py
      ENTRADA DEL TRAMO: vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py
      ENTRADA DEL TRAMO: vuelta182_tarea2_mutacion_apertura_auditor.py
      ENTRADA DEL TRAMO: vuelta183_tarea1c_mutacion_veredicto.py
      ENTRADA DEL TRAMO: vuelta183_tarea1b_mutacion_atribucion.py
      ENTRADA DEL TRAMO: vuelta184_tarea1c_mutacion_estimacion.py
      ENTRADA DEL TRAMO: vuelta185_tarea1b_mutacion_sin_temporal.py
      ENTRADA DEL TRAMO: vuelta185_tarea1c_mutacion_bateria_continuada.py
      ENTRADA DEL TRAMO: vuelta186_tarea2a_mutacion_pieza4.py
      ENTRADA DEL TRAMO: vuelta186_tarea2b_mutacion_pieza2_cercas.py


  vuelta180_tarea2c_mutacion_cableado.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea3_mutacion_corte_de_tramos.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea4_mutacion_texto_y_clon.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea5_mutacion_backlog_l02.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta182_tarea2_mutacion_apertura_auditor.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt
  vuelta183_tarea1c_mutacion_veredicto.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V183_T1C_MUTACION_VEREDICTO.txt
  vuelta183_tarea1b_mutacion_atribucion.py exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V183_T1B_MUTACION_ATRIBUCION.txt
  vuelta184_tarea1c_mutacion_estimacion.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V184_T1C_MUTACION_ESTIMACION.txt
  vuelta185_tarea1b_mutacion_sin_temporal.py exit 0  OK                   4.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt, SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt
  vuelta185_tarea1c_mutacion_bateria_continuada.py exit 0  OK                  11.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt
  vuelta186_tarea2a_mutacion_pieza4.py   exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2A_MUTACION_PIEZA4.txt
  vuelta186_tarea2b_mutacion_pieza2_cercas.py exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 43.6
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.7
  CIFRA arnes MAS LENTO: vuelta185_tarea1c_mutacion_bateria_continuada.py con 11.0s
  CIFRA arnes MAS RAPIDO: vuelta186_tarea2b_mutacion_pieza2_cercas.py con 2.3s
  CIFRA mediana por arnes, en segundos: 2.5
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta185_tarea1c_mutacion_bateria_continuada.py    11.0s
      vuelta185_tarea1b_mutacion_sin_temporal.py     4.0s
      vuelta182_tarea2_mutacion_apertura_auditor.py     3.1s
      vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py     3.0s
      vuelta183_tarea1b_mutacion_atribucion.py       2.9s
      vuelta184_tarea1c_mutacion_estimacion.py       2.7s
      vuelta180_tarea4_mutacion_texto_y_clon.py      2.5s
      vuelta180_tarea2c_mutacion_cableado.py         2.5s
      vuelta183_tarea1c_mutacion_veredicto.py        2.4s
      vuelta180_tarea3_mutacion_corte_de_tramos.py     2.4s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 127 (corte: HEAD 4021f12f1efe, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 3, de 127 (corte: HEAD 4021f12f1efe, nomina contada en esta corrida)
      SUJETO SIN CONGELAR: vuelta186_tarea2c_mutacion_cierre_tardio.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta187_tarea4_mutacion_dos_convenciones.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta188_tarea4_mutacion_cobertura_parejas.py NO DECIDIBLE   abre REPORTE.md
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 6 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 3 NO DECIDIBLE con motivo escrito, 0 sin
         CON MOTIVO ESCRITO     vuelta186_tarea2c_mutacion_cierre_tardio.py
         CON MOTIVO ESCRITO     vuelta187_tarea4_mutacion_dos_convenciones.py
         CON MOTIVO ESCRITO     vuelta188_tarea4_mutacion_cobertura_parejas.py
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 6 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta191_tarea3_mutacion_lineas.py, vuelta191_tarea4_mutacion_veredicto.py, vuelta191_tarea6_mutacion_bloque_tallado.py, vuelta192_tarea4_mutacion_cuarta_puerta.py, vuelta193_tarea4e_mutacion_sello_entre_procesos.py, vuelta194_tarea2c_mutacion_sede_del_turno.py
ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado. La regla es de la vuelta 145 y su condicion la fijo la 148: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y la que no pueda tenerlo entra como CASO DECLARADO. Un arnes anclado a un fichero que la campana mueve cada vuelta no mide su maquina, mide el dia. La lista entera: vuelta186_tarea2c_mutacion_cierre_tardio.py, vuelta187_tarea4_mutacion_dos_convenciones.py, vuelta188_tarea4_mutacion_cobertura_parejas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 9: 1
FIN (reloj de pared, UTC): 2026-09-06T22:31:07Z
DURACION DEL TRAMO (monotona, segundos): 44.9
DURACION DEL TRAMO (monotona, minutos): 0.7


==============================================================================
TRAMO 10 DE 10. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V194_BATERIA_TRAMO_10.txt
==============================================================================

CORRIDA DEL TRAMO 10 DE 10, BATERIA DE LA VUELTA 194
lanzada por scripts/loop/vuelta194_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-06T22:31:36Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 127 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 127 (corte: HEAD 201468a2694d, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 193
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 127 (corte: HEAD 201468a2694d, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 190 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 127 (corte: HEAD 201468a2694d, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 10
  CIFRA TRAMO QUE SE CORRE: 10 de 10
  CIFRA entradas de ESTE tramo: 10
  CIFRA suma de las entradas de TODOS los tramos: 127
      ENTRADA DEL TRAMO: vuelta186_tarea2c_mutacion_cierre_tardio.py
      ENTRADA DEL TRAMO: vuelta186_tarea2d_mutacion_seccion4.py
      ENTRADA DEL TRAMO: vuelta187_tarea4_mutacion_dos_convenciones.py
      ENTRADA DEL TRAMO: vuelta187_tarea5b_mutacion_seccion4_tardio.py
      ENTRADA DEL TRAMO: vuelta188_tarea2_mutacion_pata_documental.py
      ENTRADA DEL TRAMO: vuelta188_tarea3c_mutacion_exclusion_por_rojo.py
      ENTRADA DEL TRAMO: vuelta188_tarea4_mutacion_cobertura_parejas.py
      ENTRADA DEL TRAMO: vuelta188_tarea5a_mutacion_vecinos_evitar.py
      ENTRADA DEL TRAMO: vuelta190_tarea2b_mutacion_deuda_y_fallo.py
      ENTRADA DEL TRAMO: vuelta190_tarea3b_mutacion_selladas_ajenas.py


  vuelta186_tarea2c_mutacion_cierre_tardio.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt
  vuelta186_tarea2d_mutacion_seccion4.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2D_MUTACION_SECCION4.txt
  vuelta187_tarea4_mutacion_dos_convenciones.py exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt
  vuelta187_tarea5b_mutacion_seccion4_tardio.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V187_T5B_MUTACION_SECCION4_TARDIO.txt
  vuelta188_tarea2_mutacion_pata_documental.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL.txt
  vuelta188_tarea3c_mutacion_exclusion_por_rojo.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt
  vuelta188_tarea4_mutacion_cobertura_parejas.py exit 0  OK                   3.3s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt
  vuelta188_tarea5a_mutacion_vecinos_evitar.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T5A_MUTACION_VECINOS_EVITAR.txt
  vuelta190_tarea2b_mutacion_deuda_y_fallo.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt
  vuelta190_tarea3b_mutacion_selladas_ajenas.py exit 0  OK                   2.3s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 10
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 25.7
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.4
  CIFRA arnes MAS LENTO: vuelta188_tarea4_mutacion_cobertura_parejas.py con 3.3s
  CIFRA arnes MAS RAPIDO: vuelta190_tarea3b_mutacion_selladas_ajenas.py con 2.3s
  CIFRA mediana por arnes, en segundos: 2.5
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta188_tarea4_mutacion_cobertura_parejas.py     3.3s
      vuelta187_tarea4_mutacion_dos_convenciones.py     2.9s
      vuelta186_tarea2c_mutacion_cierre_tardio.py     2.6s
      vuelta188_tarea3c_mutacion_exclusion_por_rojo.py     2.5s
      vuelta188_tarea2_mutacion_pata_documental.py     2.5s
      vuelta187_tarea5b_mutacion_seccion4_tardio.py     2.5s
      vuelta186_tarea2d_mutacion_seccion4.py         2.4s
      vuelta190_tarea2b_mutacion_deuda_y_fallo.py     2.4s
      vuelta188_tarea5a_mutacion_vecinos_evitar.py     2.4s
      vuelta190_tarea3b_mutacion_selladas_ajenas.py     2.3s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 6
      FUERA DE LA NOMINA: vuelta191_tarea3_mutacion_lineas.py
      FUERA DE LA NOMINA: vuelta191_tarea4_mutacion_veredicto.py
      FUERA DE LA NOMINA: vuelta191_tarea6_mutacion_bloque_tallado.py
      FUERA DE LA NOMINA: vuelta192_tarea4_mutacion_cuarta_puerta.py
      FUERA DE LA NOMINA: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      FUERA DE LA NOMINA: vuelta194_tarea2c_mutacion_sede_del_turno.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 127 (corte: HEAD 201468a2694d, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 3, de 127 (corte: HEAD 201468a2694d, nomina contada en esta corrida)
      SUJETO SIN CONGELAR: vuelta186_tarea2c_mutacion_cierre_tardio.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta187_tarea4_mutacion_dos_convenciones.py NO DECIDIBLE   abre REPORTE.md
      SUJETO SIN CONGELAR: vuelta188_tarea4_mutacion_cobertura_parejas.py NO DECIDIBLE   abre REPORTE.md
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 6 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 3 NO DECIDIBLE con motivo escrito, 0 sin
         CON MOTIVO ESCRITO     vuelta186_tarea2c_mutacion_cierre_tardio.py
         CON MOTIVO ESCRITO     vuelta187_tarea4_mutacion_dos_convenciones.py
         CON MOTIVO ESCRITO     vuelta188_tarea4_mutacion_cobertura_parejas.py
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 6 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta191_tarea3_mutacion_lineas.py, vuelta191_tarea4_mutacion_veredicto.py, vuelta191_tarea6_mutacion_bloque_tallado.py, vuelta192_tarea4_mutacion_cuarta_puerta.py, vuelta193_tarea4e_mutacion_sello_entre_procesos.py, vuelta194_tarea2c_mutacion_sede_del_turno.py
ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado. La regla es de la vuelta 145 y su condicion la fijo la 148: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y la que no pueda tenerlo entra como CASO DECLARADO. Un arnes anclado a un fichero que la campana mueve cada vuelta no mide su maquina, mide el dia. La lista entera: vuelta186_tarea2c_mutacion_cierre_tardio.py, vuelta187_tarea4_mutacion_dos_convenciones.py, vuelta188_tarea4_mutacion_cobertura_parejas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 10: 1
FIN (reloj de pared, UTC): 2026-09-06T22:32:03Z
DURACION DEL TRAMO (monotona, segundos): 27.0
DURACION DEL TRAMO (monotona, minutos): 0.4
```
