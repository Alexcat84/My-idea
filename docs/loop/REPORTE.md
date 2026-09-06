# REPORTE DE LA VUELTA 188 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta188_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que no lleva nada
> mas. **Cerro entera en la 184**, con sus nueve tramos sellados, asi que **la
> siguiente vuelta de bateria es la 189, o sea la que viene**. En las vueltas
> intermedias la seccion 9 se cierra igual, con el **nombre del fichero, sus
> bytes medidos y su atribucion**, las tres juntas o no vale.
>
> **Y ESTA VUELTA ESCRIBE UNA SOLA SECCION 9**, que es la `C.4` del acta 188: el
> reporte de la 187 llevaba **dos**, en las lineas 870 y 920, con la `## 10.` en
> medio. Lo que esta vuelta tenga que decir de la bateria va **en la que talla
> `scripts/loop/cerrar_reporte.py`**, no en una segunda escrita a mano.
>
> **EL TOPE SIGUE EN CINCO, Y ESTA MEDIDO EN VEZ DE DARSE POR BUENO.** El regimen
> temporal `AUDITOR.md` 6.2 quedo cumplido y apagado en la 187. El **bloque H.0**
> del sello de apertura de esta vuelta midio **las tres** salidas de cierre,
> `docs/loop/SALIDA_V185_CERRAR_REPORTE.txt`,
> `docs/loop/SALIDA_V186_CERRAR_REPORTE.txt` y
> `docs/loop/SALIDA_V187_CERRAR_REPORTE.txt`, y **las tres dicen `CIFRA piezas que
> faltan: 0`**. Esta vuelta lleva **CINCO tareas**.
>
> **DONDE SE TALLO ESTE ESQUELETO, Y ESTA VEZ LA RESPUESTA ES EN LA APERTURA.**
> Es el remedio de la `C.1` de la 187, escrito en la TAREA 5.c del encargo: la
> vuelta 187 lo tallo **despues de la TAREA 1**, y el acta 188 le corrigio la
> causa midiendola contra la vuelta 186, que hizo lo mismo **en tres commits**
> (`793ad9a1` apertura, `88bd3216` **esqueleto en su propio commit**, `456f0847`
> tarea 1). **Aqui va igual: apertura y su commit, esqueleto y SU PROPIO COMMIT,
> y despues las tareas.** Desde el segundo commit de esta vuelta ya hay reporte
> parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** **no se abren
> las mesas anotadas** (la del `PMF` con los puestos 338, 297 y ahora 670, la del
> **603** y la de figuras del **226**), que el `6.3` del acta 188 deja como
> ANOTACION y no encarga; **no se poda la nomina de la bateria**, que es la opcion
> `c` que el fundador RECHAZO el 5 sep; **no se anade ningun campo a
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**, que es la `PD.8` y es del fundador;
> **no se toca el campo `estado` de `docs/plan/OPERACIONES.jsonl`**, declarado
> HISTORICO el 4 sep 2026; **no se reabre `docs/loop/reportes/REPORTE_V184.md`**;
> y **no se mueve ningun veredicto**: el `sha256` LF del archivo abre y tiene que
> cerrar en el mismo valor. Y **no se toca `dataset/`**: el `numstat` se mide al
> entrar y al salir y las dos cifras se publican.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** **Una columna de apertura medida
> al cierre es caida que ACUMULA.**

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta188_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 187: `2a8cb229`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 187: LA 186 REPRODUJO ENTERA, ADJUDICO LOS SEIS DISCUTIBLES A FAVOR, CORRIJO LA ESPECIE DE LA C.1 (NO ES CIFRA PUBLICADA Y NO ACUMULA) Y EL TOPE VUELVE A CINCO CON EL PAR 2.464 ENCABEZANDO LA 187.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V188_HEAD_APERTURA.txt`: `5aa9305d`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `2b309654`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **187**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 188`. **Esta
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
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 188 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus SEIS adjudicaciones `5.1` a `5.6` todas a favor, los TRES numerales de la seccion 6 (`PD.1` ABIERTA con sus cinco puestos leidos del acta, `PD.8` ABIERTA, y el `6.3` como ANOTACION), las TRES preguntas de la seccion 7 las tres CONTESTADAS, CERO caidas propias del auditor registradas COMO CERO Y NO OMITIDAS, y CUATRO caidas del ejecutor todas DE METODO y NINGUNA DE RACHA: `C.1` y `C.2` declaradas por el ejecutor y `C.3` y `C.4` levantadas por el auditor, LAS CUATRO ATRIBUIDAS AL EJECUTOR porque la atribucion la hace la cabecera de la seccion y no quien las encontro. Mas la deuda de la serie REMEDIDA en esta vuelta. Con caso positivo por mutacion sobre un acta FABRICADA y el esperado mutado cayendo, y con la PARADA conservada entera: un estado que el registrador no sepa leer sigue siendo PARADA | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | EL PLAN: LAS CUATRO FICHAS QUE LA VARA NOMBRA, RESUELTAS CONTRA SU EVIDENCIA. `scripts/loop/vuelta150_3_relectura_expediente.py --corte <HEAD de apertura>` corrida con corte propio y no copiada del acta; las cuatro fichas `OP-L-01`, `OP-L-02`, `OP-L-03` y `OP-I-01` LEIDAS ENTERAS Y CITADAS de `docs/plan/OPERACIONES.jsonl`; el producto de cada una MEDIDO contra la `evidencia` que la propia ficha nombra, con bytes por las dos convenciones y la cuenta prometida contra la cuenta que hay; LA VARA GANA SU PATA DOCUMENTAL EN CODIGO para las fichas de tipo `MESA`, con la cifra vieja publicada entera y al lado; el estado de cada una declarado en una de las tres formas (su producto la cubre, esta pero no la cubre, o no hay evidencia y es PARADA); y el desfase de sus cortes medido y publicado. NO se toca el campo `estado`, NO se reescriben las fichas y NINGUN VEREDICTO SE MUEVE | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | EL CASO E: EL INVENTARIO DE EXENCIONES EN VEZ DE UNA CUENTA TECLEADA. BLOQUEANTE PORQUE LA BATERIA ES LA 189. El caso E de `scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py` deja de contar un texto y pasa a COMPUTAR EL INVENTARIO de guardas eximidas en el carril tardio CON SUS NOMBRES, leido del fuente, y a cotejarlo contra una LISTA AUTORIZADA Y ESCRITA que hoy tiene DOS entradas con su vuelta y su decision al lado. Cae en rojo en TRES casos y los tres se prueban: una exencion fuera de la lista, una de la lista que desaparece, y una eximida que NO exige su declaracion. Los otros diecisiete casos no se tocan. Mas (b) el `sha256` del sujeto al lado de todo numero de linea que un arnes publique, y (c) la doble corrida de la nomina EXCLUYENDO explicitamente cualquier arnes que ya haya salido en rojo en esa misma vuelta, DICIENDOLO en su salida | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LA ESCALADA: LA GUARDA QUE VE LA MITAD, Y LA SECCION QUE SE DUPLICA. `AUDITOR.md` 1.2, mandatorio con la racha de reporte en dos. (a) `parejas_publicadas()` ensancha sus formas para cubrir las TRES que hoy se le escapan, leidas de reportes reales; LA REGLA DE LA AMBIGUEDAD NO SE TOCA; y la guarda PUBLICA SU COBERTURA, cuantas parejas ve contra cuantas rutas con cifra de bytes hay y cuantas quedan sin atribuir POR AMBIGUAS nombradas una a una. (b) `piezas_que_faltan()` exige que las secciones sean UNICAS Y ESTEN EN ORDEN, no solo que existan, que es la `C.4`. Con arnes obligatorio que incluye un caso por cada forma nueva con su mutacion cayendo, un caso de ambiguedad que exija NO atribuir, un caso sobre el texto real de `git show 9a06b7c8` exigiendo SEIS parejas vistas y SEIS que calzan, y un caso sobre ese mismo texto que ACUSE las dos secciones 9 nombrando sus dos lineas | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LA RELECTURA AL DOBLE, LOS DOS REMEDIOS PEQUENOS Y EL CIERRE. (a) La relectura al doble del tramo de la ciega del acta 188, encargada por `AUDITOR.md` 1.2 porque la discrepancia del auditor (el puesto 1202) cayo FUERA del discutible de clase marcado: cotejo de `sha256` contra el sello `V189` ANTES de leer un solo puesto, 30 puestos mas 30 vecinos deterministas con `vecinos()` IMPORTADA y no copiada, 60 releidos que es el doble exacto, NINGUNA CLASE SE VUELVE A DECIDIR; mas el remedio del `D.2`, que es un conjunto `evitar` OPCIONAL para `vecinos()` que deja su conducta de hoy intacta sin el, y los TRES solapes del UNIVERSO publicados; mas el puesto 1202 mirado con la misma vara; mas la cuenta de cuantos de los 60 llevan en su razon evidencia DE FAMILIA y no del par. (b) `docs/loop/DISCUTIBLES_DE_CLASE_V188.txt` con los puestos de los discutibles DE CLASE y nada mas. (c) El esqueleto tallado en la apertura y en su propio commit, que es la `C.1`. (d) El reporte se abre, se llena por anexion y se cierra con `cerrar_reporte.py --vuelta 188` y `archivar_reporte.py --vuelta 188`, con UNA SOLA SECCION 9 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
