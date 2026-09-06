# REPORTE DE LA VUELTA 186 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta186_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que no lleva nada
> mas. **Cerro entera en la 184**, con sus nueve tramos sellados, asi que **la
> siguiente vuelta de bateria es la 189**. En las vueltas intermedias la seccion 9
> se cierra igual, con el **nombre del fichero, sus bytes medidos y su
> atribucion**, las tres juntas o no vale.
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, PERO LA CUENTA YA NO ESTA EN CERO.**
> El regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas
> seguidas cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. **La
> 185 cerro el suyo** y es la **PRIMERA de las dos**. **Si esta vuelta cierra el
> suyo, es la SEGUNDA y la 187 recupera el tope de CINCO.** Van dos tareas y no hay
> una tercera.
>
> **EL TRABAJO DE ESTA VUELTA ES APLICAR LAS DOS ADJUDICACIONES DEL ACTA 186 QUE
> DEJAN UN INSTRUMENTO DICIENDO DOS COSAS DEL MISMO CASO**, meter en la nomina los
> dos arneses que si no dejarian la bateria de la 189 abriendo en rojo, y cerrar el
> reporte de la 184, que lleva dos vueltas sin conseguirse.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee el
> par **2.464** ni ningun otro de la cola post fusion (**encabeza el encargo de la
> 187**, y el acta 186 explica en su seccion 12 que el tope de dos sub-tareas es
> aritmetica y no preferencia); **no se vuelve a decidir ninguna clase** en la
> relectura al doble; no se toca el marcador, ni un veredicto, ni `dataset/`; **no
> se poda la nomina de la bateria**, que es la opcion `c` que el fundador RECHAZO
> el 5 sep, y aqui se hace lo contrario, que es completarla; y **no se abre la mesa
> de los tres nodos de la puerta del `PMF`** que el acta 186 anota en su `6.4`, que
> es trabajo de plan y no de esta vuelta.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py` y desde la 178 vuelve a correr en su sitio. **Una
> columna de apertura medida al cierre es caida que ACUMULA.**
>
> **Y EL ESQUELETO VUELVE A SU SITIO DE SIEMPRE, LA APERTURA, AL REVES QUE EN LA
> 185.** Alli tuvo que esperar porque su PASO 0 habria archivado el reporte de la
> 184 sin cerrar. Aqui no hay nada de eso: el reporte del arbol es el de la 185, ya
> cerrado y ya archivado, y el de la 184 tambien esta archivado desde la TAREA 2.a
> de la 185. **El PASO 0 se corre igual y su salida se pega con lo que salga**,
> diga lo que diga, en vez de dejar la fila muda.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta186_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 185: `5834632b`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 185: LA 184 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA, ADJUDICO LOS SIETE DISCUTIBLES A FAVOR, CIERRO PD.2, PD.3 Y PD.4 POR CITA, Y EL ROJO QUE IMPIDE CERRAR EL REPORTE QUEDA DECLARADO FALSO ROJO CON SU REPARACION ENCARGADA.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V186_HEAD_APERTURA.txt`: `620dc837`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `793ad9a1`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **185**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 186`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LAS DOS CUENTAS QUE VENCEN. BLOQUEANTE. (a) El acta 186 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus SIETE adjudicaciones `5.1` a `5.7` todas a favor, los CUATRO pendientes de doctrina de la seccion 6 (`PD.5` y `PD.6` CERRADAS por cita, `PD.1` ABIERTA con sus cinco puestos leidos del acta, y el `6.4` como ANOTACION y no como pendiente propio), las TRES preguntas de la seccion 7 las tres CONTESTADAS, CERO caidas propias del auditor registradas COMO CERO Y NO OMITIDAS, UNA caida de reporte del ejecutor (`R.1`, la del `git status` en cero lineas) que NO acumula por vivir en prosa, y la deuda de la serie REMEDIDA en esta vuelta y no heredada del `R.47`, mas su caso positivo por mutacion sobre un acta FABRICADA con el esperado mutado cayendo. (b) LOS DOS ARNESES DE LA 185 ENTRAN EN LA NOMINA, que es la respuesta a la `P.3`: `arneses_que_faltan()` tiene que devolver 0 despues, con el tamano de la nomina antes y despues, y los dos arneses corridos DOS VECES CADA UNO EN PROCESOS APARTE exigiendo el mismo `sha256`. NO SE PODA NADA. (c) LA RELECTURA AL DOBLE del tramo de la ciega del acta 186, con el cotejo de `sha256` contra el sello `V187` ANTES de leer un solo puesto, 30 puestos mas 30 vecinos deterministas con `vecinos()` IMPORTADA, solape 0 por los dos lados MEDIDO, las cuatro discrepancias del auditor miradas con la misma vara, y la cuenta de clases `B` del universo releido | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LAS TRES REPARACIONES DE `cerrar_reporte.py`, LA ESCALADA Y EL CIERRE DE DOS REPORTES. (a) La pieza (4) deja de llevar su propia copia de `ajena != vuelta` y LLAMA a la unica sede, con parametro nuevo cuyo valor por defecto conserva EXACTAMENTE la conducta de hoy y computado en `main()` sin bandera, con arnes propio. (b) La pieza (2) busca el hueco de cabecera FUERA de los bloques cercados REUSANDO el desbloqueador que `cifras_sin_pareja()` ya tenia, separado a una sede y llamado por las dos, con arnes propio. (c) El carril de CIERRE TARDIO, computado y no pasado por bandera, donde las cifras sin pareja NO bloquean pero SE DECLARAN una a una dentro del propio reporte cerrado, con arnes propio; y DESPUES, y no antes, el reporte de la 184 se cierra y se archiva tras cotejar sus tres piezas por `sha256` y por bytes. (d) LA ESCALADA de `AUDITOR.md` 1.2: una guarda que extrae de `SALIDA_V<N>_APERTURA.txt` las dos cifras del estado del arbol y las coteja contra lo que la seccion 4 del reporte afirma, cayendo en ROJO si discrepan o si el reporte no las afirma, con arnes propio que exige que HUBIERA CAZADO LA `R.1`. (e) El reporte de la 186 se abre en su esqueleto, cada tarea anexa su fila al cerrarse, la cabecera se talla y `--comparar` tiene que dar CABECERA IDENTICA AL TALLADOR, y su SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
