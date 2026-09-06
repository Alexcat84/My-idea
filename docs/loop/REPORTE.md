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
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 188 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus SEIS adjudicaciones `5.1` a `5.6` todas a favor, los TRES numerales de la seccion 6 (`PD.1` ABIERTA con sus cinco puestos leidos del acta, `PD.8` ABIERTA, y el `6.3` como ANOTACION), las TRES preguntas de la seccion 7 las tres CONTESTADAS, CERO caidas propias del auditor registradas COMO CERO Y NO OMITIDAS, y CUATRO caidas del ejecutor todas DE METODO y NINGUNA DE RACHA: `C.1` y `C.2` declaradas por el ejecutor y `C.3` y `C.4` levantadas por el auditor, LAS CUATRO ATRIBUIDAS AL EJECUTOR porque la atribucion la hace la cabecera de la seccion y no quien las encontro. Mas la deuda de la serie REMEDIDA en esta vuelta. Con caso positivo por mutacion sobre un acta FABRICADA y el esperado mutado cayendo, y con la PARADA conservada entera: un estado que el registrador no sepa leer sigue siendo PARADA | **CERRADA** | `SALIDA_V188_T1A_REGISTRO_R50.txt`, `SALIDA_V188_T1A_MUTACION_REGISTRO_188.txt` |
| **TAREA 2** | EL PLAN: LAS CUATRO FICHAS QUE LA VARA NOMBRA, RESUELTAS CONTRA SU EVIDENCIA. `scripts/loop/vuelta150_3_relectura_expediente.py --corte <HEAD de apertura>` corrida con corte propio y no copiada del acta; las cuatro fichas `OP-L-01`, `OP-L-02`, `OP-L-03` y `OP-I-01` LEIDAS ENTERAS Y CITADAS de `docs/plan/OPERACIONES.jsonl`; el producto de cada una MEDIDO contra la `evidencia` que la propia ficha nombra, con bytes por las dos convenciones y la cuenta prometida contra la cuenta que hay; LA VARA GANA SU PATA DOCUMENTAL EN CODIGO para las fichas de tipo `MESA`, con la cifra vieja publicada entera y al lado; el estado de cada una declarado en una de las tres formas (su producto la cubre, esta pero no la cubre, o no hay evidencia y es PARADA); y el desfase de sus cortes medido y publicado. NO se toca el campo `estado`, NO se reescriben las fichas y NINGUN VEREDICTO SE MUEVE | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | EL CASO E: EL INVENTARIO DE EXENCIONES EN VEZ DE UNA CUENTA TECLEADA. BLOQUEANTE PORQUE LA BATERIA ES LA 189. El caso E de `scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py` deja de contar un texto y pasa a COMPUTAR EL INVENTARIO de guardas eximidas en el carril tardio CON SUS NOMBRES, leido del fuente, y a cotejarlo contra una LISTA AUTORIZADA Y ESCRITA que hoy tiene DOS entradas con su vuelta y su decision al lado. Cae en rojo en TRES casos y los tres se prueban: una exencion fuera de la lista, una de la lista que desaparece, y una eximida que NO exige su declaracion. Los otros diecisiete casos no se tocan. Mas (b) el `sha256` del sujeto al lado de todo numero de linea que un arnes publique, y (c) la doble corrida de la nomina EXCLUYENDO explicitamente cualquier arnes que ya haya salido en rojo en esa misma vuelta, DICIENDOLO en su salida | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LA ESCALADA: LA GUARDA QUE VE LA MITAD, Y LA SECCION QUE SE DUPLICA. `AUDITOR.md` 1.2, mandatorio con la racha de reporte en dos. (a) `parejas_publicadas()` ensancha sus formas para cubrir las TRES que hoy se le escapan, leidas de reportes reales; LA REGLA DE LA AMBIGUEDAD NO SE TOCA; y la guarda PUBLICA SU COBERTURA, cuantas parejas ve contra cuantas rutas con cifra de bytes hay y cuantas quedan sin atribuir POR AMBIGUAS nombradas una a una. (b) `piezas_que_faltan()` exige que las secciones sean UNICAS Y ESTEN EN ORDEN, no solo que existan, que es la `C.4`. Con arnes obligatorio que incluye un caso por cada forma nueva con su mutacion cayendo, un caso de ambiguedad que exija NO atribuir, un caso sobre el texto real de `git show 9a06b7c8` exigiendo SEIS parejas vistas y SEIS que calzan, y un caso sobre ese mismo texto que ACUSE las dos secciones 9 nombrando sus dos lineas | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LA RELECTURA AL DOBLE, LOS DOS REMEDIOS PEQUENOS Y EL CIERRE. (a) La relectura al doble del tramo de la ciega del acta 188, encargada por `AUDITOR.md` 1.2 porque la discrepancia del auditor (el puesto 1202) cayo FUERA del discutible de clase marcado: cotejo de `sha256` contra el sello `V189` ANTES de leer un solo puesto, 30 puestos mas 30 vecinos deterministas con `vecinos()` IMPORTADA y no copiada, 60 releidos que es el doble exacto, NINGUNA CLASE SE VUELVE A DECIDIR; mas el remedio del `D.2`, que es un conjunto `evitar` OPCIONAL para `vecinos()` que deja su conducta de hoy intacta sin el, y los TRES solapes del UNIVERSO publicados; mas el puesto 1202 mirado con la misma vara; mas la cuenta de cuantos de los 60 llevan en su razon evidencia DE FAMILIA y no del par. (b) `docs/loop/DISCUTIBLES_DE_CLASE_V188.txt` con los puestos de los discutibles DE CLASE y nada mas. (c) El esqueleto tallado en la apertura y en su propio commit, que es la `C.1`. (d) El reporte se abre, se llena por anexion y se cierra con `cerrar_reporte.py --vuelta 188` y `archivar_reporte.py --vuelta 188`, con UNA SOLA SECCION 9 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS. CERRADA

**EL NUMERO NO SE TECLEO Y LA ENTRADA ES LA `R.50`.**
`scripts/loop/serie_de_registros.py`, corrido en esta vuelta y recomputando la
serie de sus **dos** sedes, devolvio **41 entradas, 0 colisiones, 0 huecos y
siguiente libre `R.50`**. Despues de escribir, la serie recomputada da **42
entradas, siguiente libre `R.51`, 0 colisiones y 0 huecos**. Salida:
`docs/loop/SALIDA_V188_T1A_REGISTRO_R50.txt`.

**EL ACTA ACOTADA ANTES DE CONTAR NADA:** `docs/loop/ACTA_AUDITOR.md`, lineas
**66071 a 66825**, o sea **755 lineas**, con **una sola** cabecera del acta 188.

**LAS CIFRAS DEL TITULO, CONTADAS DEL ACTA Y NO TECLEADAS:** **6** adjudicaciones
numeradas (`5.1` a `5.6`, una aparicion cada una), **3** numerales en la seccion
6, **3** preguntas en la seccion 7, **0** caidas propias del auditor y **4**
caidas de metodo del ejecutor. La sede pasa de **924954 a 943276 bytes**, la
entrada mide **18321 bytes** y **195 lineas**, esta byte a byte tras releerla del
disco, y lleva **0 guiones largos y 0 guiones medios**.

**LAS SEIS ADJUDICACIONES, TODAS A FAVOR**, con su linea leida hoy: `5.1` en la
**66394**, `5.2` en la **66405**, `5.3` en la **66416**, `5.4` en la **66428**,
`5.5` en la **66438** y `5.6` en la **66466**. El patron de adjudicacion **sin**
comillas inversas, el del acta 183, corrido sobre esta acta da **0**, y ese cero
se publica.

#### LO QUE ESTE REGISTRADOR TUVO QUE APRENDER, Y CADA COSA CON SU MEDICION

**(1) DOS MARCAS DE ESTADO NUEVAS PARA LA SECCION 6, LAS DOS LITERALES DEL ACTA
188.** El `6.1` dice `SIGUE ABIERTA` y el vocabulario heredado ya lo leia; el
`6.2` dice *"`PD.8` NACE Y **LA DEJO ABIERTA**"* y el `6.3` dice *"LAS TRES MESAS
ANOTADAS **SIGUEN ANOTADAS** Y NO SE ABREN"*, y **ninguna de las dos formas
estaba en el vocabulario de la 187**. Corrido con el vocabulario viejo sobre esta
misma acta, los estados salen **`6.1` ABIERTA; `6.2` SIN DECIR; `6.3` SIN
DECIR**: **`CIFRA SIN DECIR con el vocabulario viejo: 2`**, y `SIN DECIR` es
PARADA. Con el nuevo salen **`6.1` `PD.1` ABIERTA; `6.2` `PD.8` ABIERTA; `6.3`
ANOTACION**, o sea **CERRADAS 0, ABIERTAS 2, ANOTACIONES 1, CORRECCIONES 0**.
**Se anaden marcas; ninguna de las cuatro viejas se ensancha ni se toca.**

**Y LA PARADA SE CONSERVA ENTERA, PROBADA POR MUTACION:** sobre un acta fabricada
cuyo `6.1` no dice ninguna de las seis marcas, el instrumento sigue sacando `SIN
DECIR` y sigue parando, y el esperado mutado (exigir que ninguno sea `SIN DECIR`)
**CAE**.

**(2) UN PATRON DE CAIDA NUEVO, Y SU CIFRA VIEJA PUBLICADA.** El patron `C.n` de
la vuelta 187 exige una **coma o un punto pegados** al numeral (`` **`C.3`, ``),
y el acta 188 escribe sus dos primeras con un **espacio** detras
(`` **`C.1` DEL EJECUTOR ``). Corrido sobre esta acta: **el patron de la 187
encuentra 2** (lineas 66597 y 66630) y **el de esta vuelta encuentra 4** (lineas
**66571, 66589, 66597 y 66630**). Las dos cifras se publican y el patron viejo se
conserva intacto.

**(3) LA ATRIBUCION DE UNA SECCION DE CAIDAS MIXTA, Y AQUI VA UNA DISCREPANCIA
MEDIDA QUE SE DECLARA EN VEZ DE RESOLVERSE COPIANDO** (`EJECUTOR.md` 2). El
encargo dice, con estas palabras, que *"la seccion que las contiene lo dice en su
cabecera"*. **Se midio antes de creerlo, y la cabecera literal es**
`## 8. LAS CAIDAS, LAS SUYAS DECLARADAS Y LAS DOS QUE LEVANTO YO`: **NO contiene
la palabra `EJECUTOR`**. Con el vocabulario de cabecera de la 187 (`EJECUTOR` o
`MI CAIDA`) las cuatro salen **HUERFANAS**, y una caida sin dueno es PARADA:
corrido asi sobre esta acta da **ejecutor 0, auditor 0, huerfanas 4**.

**LA CABECERA SI DICE DE QUIEN SON, PERO CON OTRAS PALABRAS:** `LAS SUYAS`, que
en un acta que el auditor escribe **sobre** el ejecutor son las del ejecutor. Esa
marca se **anade**, literal, y la vieja se conserva. Con el vocabulario de esta
vuelta: **DEL EJECUTOR 4, DEL AUDITOR 0, HUERFANAS 0**, y las cuatro bajo esa
misma cabecera. **La precedencia va escrita:** si la cabecera trae una marca de
ejecutor, la caida es del ejecutor **aunque la cabecera diga ademas que la
levanto el auditor**, que es literalmente lo que dice esta. La PARADA se conserva:
una `C.n` bajo una cabecera que no diga ni una cosa ni la otra sigue saliendo
huerfana y sigue parando, y eso se prueba por mutacion con los cuatro escenarios
de cabecera.

**(4) UNA CAIDA QUE NO ACUMULA NO ES UNA CAIDA QUE NO EXISTE, Y LAS DOS CUENTAS
VAN JUNTAS.** Medido del acta y no tecleado: **`CIFRA caidas del ejecutor
registradas: 4`**, **`CIFRA de esas que ACUMULAN para alguna racha: 0`**,
**`CIFRA de esas que NO acumulan: 4 (C.1, C.2, C.3, C.4)`**. **Por que difieren:**
las cuatro son **de METODO**, y las dos rachas que esta casa lleva son otras: la
de **cifra publicada**, que sigue en **0**, y la de **reporte**, que **se mantiene
en 2** sin sumar. Publicar solo el cero diria que no paso nada; publicar solo el
cuatro diria que alguna racha subio; **las dos son falsas por separado**.

**Y ESA CUENTA OBLIGO A LEER EL BLOQUE ENTERO Y NO EL PRIMER PARRAFO, Y SE MIDIO
ANTES DE DECIDIRLO.** `parrafo_de()` se para en la primera linea vacia, y en el
acta 188 la declaracion de que una caida no acumula vive **dos parrafos mas
abajo** de su titulo (la `C.3` la escribe bajo *"LA ESPECIE Y SI ACUMULA"*).
Leyendo solo el primer parrafo las cuatro salian **como que acumulan**, que es
exactamente la cifra falsa que este instrumento existe para no publicar. El arnes
lo prueba con un acta fabricada en esa forma: **4 de 4 saldrian acumulando con el
lector viejo**. **Y el silencio se cuenta como QUE ACUMULA**, que es el lado
seguro.

#### LOS TRES NUMERALES DE LA SECCION 6, LAS TRES PREGUNTAS Y LOS CINCO PUESTOS

- **`6.1` nombra `PD.1`, estado ABIERTA** (linea **66478**). **SEPTIMA vuelta
  abierta**, y esta vuelta no la cierra ni la encarga.
- **`6.2` nombra `PD.8`, estado ABIERTA** (linea **66485**). Nace en esta acta.
  **Esta vuelta no anade ningun campo a `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**, y
  el encargo se lo prohibe con esas palabras.
- **`6.3`, estado ANOTACION** (linea **66493**), y no nombra ninguna `PD` en su
  titulo, cosa que la entrada dice en vez de inventarle una. **Las tres mesas no
  se abren.**

**LAS TRES PREGUNTAS, LAS TRES CONTESTADAS**, y el estado sale de la cabecera
literal de la seccion 7 (linea **66502**): *"LAS TRES PREGUNTAS, QUE **LAS
CONTESTO**, Y LA PRIMERA ES LA QUE IMPORTA"*. `7.1` en la **66504**, `7.2` en la
**66541** y `7.3` en la **66558**. Si esa cabecera no dijera `LAS CONTESTO`, el
instrumento haria PARADA en vez de registrarlas como contestadas, y eso se prueba
por mutacion.

**LOS CINCO PUESTOS DE LA `PD.1`, LEIDOS DEL ACTA Y NO COPIADOS DEL ENCARGO:
1778, 2530, 2540, 3141, 3232.** Y aqui hubo un tercer arreglo pequeno: el acta
188 tiene **DOS** numerales abiertos y **solo el primero nombra puestos**, asi que
el recorrido **ya no se para en el primer abierto**; si se parara y ese no los
trajera, publicaria una lista vacia sobre un acta que si los nombra.

#### CERO CAIDAS PROPIAS DEL AUDITOR, CONTADAS Y DECLARADAS

El patron `A.n` de cabecera de tercer nivel da **0** sobre esta acta. **Un cero
que sale de un patron que no muerde no es evidencia de nada**, asi que va con la
declaracion del acta al lado: la frase `CERO CAIDAS PROPIAS` aparece en **1
linea** (`docs/loop/ACTA_AUDITOR.md:66093`) y la frase `NINGUNA CAIDA PROPIA`, la
del acta 185, en **0**. El patron `R.n` de caida de reporte da **0** y el `E.n` de
las actas 182 y 184 da **0**: **esta acta no registra ninguna caida de reporte del
ejecutor**, y eso es una medicion, no una omision.

#### LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL `R.49`

Tramo mirado: actas **173 a 187**. **`CIFRA actas SIN entrada propia en la serie:
8`**, y son las **173, 174, 175, 176, 177, 178, 179 y 180**. Extremo bajo: **`R.42`
cubre el acta 172**. Extremo alto: **`R.43` cubre el acta 181**. **No se rellenan
aqui.**

#### EL CASO POSITIVO POR MUTACION, SOBRE UN ACTA FABRICADA Y NUNCA SOBRE LA REAL

`docs/loop/SALIDA_V188_T1A_MUTACION_REGISTRO_188.txt`, **`CIFRA fallos: 0`**,
**`VEREDICTO: VERDE`**, exitcode **0**. Nueve mutaciones, y en todas el esperado
mutado **CAE**: los contadores sobre cuatro actas fabricadas; los dos
vocabularios de estado con sus dos cifras y la PARADA conservada; los puestos
leidos de tres listas distintas; los cuatro escenarios de cabecera de la
atribucion mas el vocabulario viejo dando cuatro huerfanas; los dos patrones de
`C.n`; las tres formas de declarar (o no) que una caida acumula; el `A.n` y las
dos frases del cero; el estado de las preguntas; el salto; y el titulo con su
concordancia, incluido el cero en plural.

<!-- FIN ANEXO DE TAREAS -->
