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

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

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
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 194`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 23 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **4 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
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
`docs/loop/SALIDA_V194_T1A_REGISTRO_R56.txt`: **10486 bytes**, **181 lineas** por
`count(NL)` y **182** por `split`, **0 guiones largos o medios**. La sede pasa de
**1029096** a **1039583 bytes**, y la entrada se releyo del disco byte a byte.

**LA IDEMPOTENCIA NO SE AFIRMA: SE PROBO RE CORRIENDOLO**, con la sede medida en
bytes antes y despues. Segunda corrida:
`docs/loop/SALIDA_V194_T1A_RECORRIDO_SIN_ESCRIBIR.txt` (12207 bytes), *"el acta
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
`docs/loop/SALIDA_V194_T1A_MUTACION_REGISTRADOR.txt` (4074 bytes), **VEREDICTO:
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
`docs/loop/SALIDA_V194_T2G_TRES_ESCENARIOS.txt` (3671 bytes en disco y 3671
normalizado a LF, `sha256` `56481dd977310ceb` por las dos convenciones), **13
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
`docs/loop/SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt` (3687 bytes en disco y
3687 por LF, `sha256` `b014e233a5e7512d` por las dos convenciones), **14 casos, 14
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
`docs/loop/SALIDA_V194_T3_DATASET_RESTAURADO.txt` (1154 bytes). El tramo NO se dio
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
atajo. La salida unica es `docs/loop/SALIDA_V194_BATERIA.txt`: **102495 bytes en
disco y 102495 normalizado a LF, 1454 lineas, `sha256` LF
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
