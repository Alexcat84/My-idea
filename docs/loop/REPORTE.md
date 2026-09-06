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
| **TAREA 2** | EL PLAN: LAS CUATRO FICHAS QUE LA VARA NOMBRA, RESUELTAS CONTRA SU EVIDENCIA. `scripts/loop/vuelta150_3_relectura_expediente.py --corte <HEAD de apertura>` corrida con corte propio y no copiada del acta; las cuatro fichas `OP-L-01`, `OP-L-02`, `OP-L-03` y `OP-I-01` LEIDAS ENTERAS Y CITADAS de `docs/plan/OPERACIONES.jsonl`; el producto de cada una MEDIDO contra la `evidencia` que la propia ficha nombra, con bytes por las dos convenciones y la cuenta prometida contra la cuenta que hay; LA VARA GANA SU PATA DOCUMENTAL EN CODIGO para las fichas de tipo `MESA`, con la cifra vieja publicada entera y al lado; el estado de cada una declarado en una de las tres formas (su producto la cubre, esta pero no la cubre, o no hay evidencia y es PARADA); y el desfase de sus cortes medido y publicado. NO se toca el campo `estado`, NO se reescriben las fichas y NINGUN VEREDICTO SE MUEVE | **CERRADA CON UNA PARADA DENTRO (la de OP-L-02)** | `SALIDA_V188_T2_VARA_APERTURA.txt`, `SALIDA_V188_T2_VARA_CON_PATA.txt`, `SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL.txt`, `SALIDA_V188_T2_EVIDENCIA_DE_LAS_FICHAS.txt` |
| **TAREA 3** | EL CASO E: EL INVENTARIO DE EXENCIONES EN VEZ DE UNA CUENTA TECLEADA. BLOQUEANTE PORQUE LA BATERIA ES LA 189. El caso E de `scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py` deja de contar un texto y pasa a COMPUTAR EL INVENTARIO de guardas eximidas en el carril tardio CON SUS NOMBRES, leido del fuente, y a cotejarlo contra una LISTA AUTORIZADA Y ESCRITA que hoy tiene DOS entradas con su vuelta y su decision al lado. Cae en rojo en TRES casos y los tres se prueban: una exencion fuera de la lista, una de la lista que desaparece, y una eximida que NO exige su declaracion. Los otros diecisiete casos no se tocan. Mas (b) el `sha256` del sujeto al lado de todo numero de linea que un arnes publique, y (c) la doble corrida de la nomina EXCLUYENDO explicitamente cualquier arnes que ya haya salido en rojo en esa misma vuelta, DICIENDOLO en su salida | **CERRADA EN VERDE** | `SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt`, `SALIDA_V186_T2A_MUTACION_PIEZA4.txt`, `SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt` |
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

### TAREA 2. EL PLAN: LAS CUATRO FICHAS, RESUELTAS CONTRA SU EVIDENCIA. CERRADA CON UNA PARADA DENTRO

**LA VARA CORRIDA CON MI PROPIO CORTE, NO CON EL DEL ACTA.**
`python scripts/loop/vuelta150_3_relectura_expediente.py --corte 5aa9305df3ceb438f92011d1b9e973c58277c6fe`,
que es el HEAD de apertura sellado en `docs/loop/SALIDA_V188_HEAD_APERTURA.txt`.
Salida entera: `docs/loop/SALIDA_V188_T2_VARA_APERTURA.txt`, exitcode **0**. Sus
cifras, contadas de ese fichero:

- `CIFRA fichas del expediente: 71 operaciones`
- `CIFRA fichas que no calzan: 37 operaciones`
- `CIFRA fichas congeladas declaradas: 24 operaciones`
- `CIFRA fichas congeladas en silencio: 12 operaciones`
- `CIFRA fichas HECHA sin ninguna prueba: 1 operaciones`
- **`CIFRA fichas en LISTA sin ninguna prueba: 6 operaciones`**
- **`CIFRA de esas que estan CONSUMIDAS por otra ficha: 2 operaciones`**
- **`CIFRA de esas que son TRABAJO REAL: 4 operaciones`**

**Reproduce lo que el acta 188 publica en su punto 12 con otro corte**, y las
cuatro son **`OP-L-01`, `OP-L-02`, `OP-L-03`** (09_LECTURAS_DIRIGIDAS) y
**`OP-I-01`** (10_INVENTARIO). **Las cuatro son de tipo `MESA`**, contado del
expediente, y **dos tienen `depende_de` vacio**: `OP-L-01` y `OP-I-01`.

#### 2.a LA VARA GANA SU PATA DOCUMENTAL, Y ES CODIGO

**EL HUECO, QUE ES DE FORMA Y NO DE CIFRA.** Las tres pruebas de la vara son **de
grafo, de codigo y de git**, y las tres preguntan por una huella que una `MESA`
no deja: **una mesa produce documentos**. Preguntarle al grafo si una mesa se hizo
es preguntarle a la fuente equivocada, que es la caida escrita en el recuadro de
`AUDITOR.md` 0.

**QUE SE ANADIO EN `scripts/loop/vuelta150_3_relectura_expediente.py`:** tres
funciones (`rutas_de_la_evidencia()`, pura; `localizar_evidencia()`, el unico
lector de disco; y `p4_vara_documental()`) y **un bloque de salida que va DESPUES
de la cifra vieja y no en su lugar**. Para las fichas que no son `MESA` **no
cambia absolutamente nada**: la P4 no se computa y **la ficha ni siquiera aparece
en el diccionario**.

**LAS DOS CIFRAS, JUNTAS Y CON SU DIFERENCIA NOMBRADA**, contadas de
`docs/loop/SALIDA_V188_T2_VARA_CON_PATA.txt`:

- **CIFRA VIEJA, identica a la de siempre: 6 fichas en LISTA sin ninguna de las
  tres pruebas, de las cuales 4 son TRABAJO REAL.**
- **CIFRA NUEVA: de esas 4, 3 son mesas cuyo producto documental SI existe en
  disco, y 1 no lo tiene.**
- **LA DIFERENCIA SON 3 fichas, y no significa que su mesa se hiciera bien:**
  significa que el documento que su propia evidencia nombra **esta**. Si cubre lo
  que la ficha describe **es lectura, y la vara no la hace**.
- `CIFRA fichas de tipo MESA en el expediente: 6` | `CIFRA de esas que estan en
  LISTA: 5`.

**ARNES OBLIGATORIO, Y NACE EN ESTA VUELTA:**
`scripts/loop/vuelta188_tarea2_mutacion_pata_documental.py`. Salida:
`docs/loop/SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL.txt`, **`CIFRA casos: 11 |
pasan: 11`**, **`CIFRA casos que CAEN al mutar su esperado: 11 de 11`**, **`CIFRA
fallos: 0`**, **`VEREDICTO: VERDE`**, exitcode **0**. Cinco casos: **(A)** la P4
no existe para una ficha que no es `MESA`, y eso es de FORMA; **(B)** una mesa con
fichero que existe sale con su medicion por las dos convenciones, y el fichero se
fabrica **con CRLF a proposito** para que las dos no sean el mismo numero (**disco
23, LF 21**); **(C)** una mesa cuyo fichero no existe sale vacia, o sea **la P4 no
inventa un documento que no esta**; **(D)** una mesa cuya evidencia es prosa
entera sale vacia **pero con 0 menciones**, y esa diferencia con la (C) es medible
sin tocar disco; **(E)** el extractor no traga prosa con puntos, ni versiones, ni
extensiones fuera de la lista. **El temporal se limpia** (`P.16`).

#### 2.b EL PRODUCTO DE CADA UNA, MEDIDO CONTRA LA `evidencia` QUE ELLA NOMBRA

Instrumento: `scripts/loop/vuelta188_tarea2_evidencia_de_las_fichas.py`. Salida:
`docs/loop/SALIDA_V188_T2_EVIDENCIA_DE_LAS_FICHAS.txt`, exitcode **0**. Toda cifra
de esta seccion sale de ese fichero.

| ficha | lo que su `evidencia` nombra | existe | disco | LF |
|---|---|---|---|---|
| `OP-L-01` | `LECTURAS_DIRIGIDAS.md` | SI, en `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 |
| `OP-L-01` | `INTRA_DOMINIO_INFORME.md` | SI, en `docs/INTRA_DOMINIO_INFORME.md` | 943970 | 943970 |
| `OP-L-01` | `BANCO_DE_TEXTOS.md` | SI, en `docs/BANCO_DE_TEXTOS.md` | 182228 | 182228 |
| `OP-L-02` | (su evidencia entera es prosa: 0 menciones de fichero) | NO HAY QUE MEDIR | | |
| `OP-L-03` | `BANCO_DEL_PLAN.md` | SI, en `docs/plan/BANCO_DEL_PLAN.md` | 61554 | 61554 |
| `OP-L-03` | `LECTURAS_DIRIGIDAS.md` | SI, en `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 |
| `OP-I-01` | `INVENTARIO.jsonl` | SI, en `docs/plan/INVENTARIO.jsonl` | 584554 | 584554 |
| `OP-I-01` | `10_INVENTARIO.md` | SI, en `docs/plan/10_INVENTARIO.md` | 34258 | 33845 |

**Y ese ultimo es el unico de los siete cuyas dos convenciones NO son el mismo
numero**, que es exactamente el motivo por el que se miden las dos y no se
suponen.

**LO QUE LA FICHA PROMETE CONTRA LO QUE HAY, RECOMPUTADO Y NO CREIDO AL ACTA:**

- **`OP-L-01` describe once lecturas** (su `adjudicacion` dice literalmente
  *"TANDA DE ONCE LECTURAS DIRIGIDAS"* y su `nota` enumera **11** etiquetas,
  `LD-01` a `LD-11`). `docs/plan/LECTURAS_DIRIGIDAS.md` mide **214916 bytes por
  las dos convenciones**, `sha256` LF `dda1cdd67042c733` y **2230 lineas**. **Las
  once estan en cabecera: 11 de 11.** Y el documento ha crecido muy por encima:
  **68 etiquetas distintas por toda aparicion** y **60 en cabecera**.
- **`OP-I-01` promete 323 entradas**, leido de su propio texto. `INVENTARIO.jsonl`
  tiene **672 entradas no vacias**, las **672 JSON valido**: **+349**. El reparto
  por tipo, contado del fichero: **acto 556, familia_de_ids 54, figura 20, defecto
  19, racimo 13, dominio 10**.

**Y AQUI VA UN CONTRASTE CONTRA EL ACTA QUE SE DECLARA EN VEZ DE RESOLVERSE
COPIANDO** (`EJECUTOR.md` 2). El acta 188 punto 12 dice que el documento lleva
etiquetas *"de `LD-01` hasta `LD-98`"*. **Mi medicion de hoy da como maximo
`LD-154`.** **Ninguna de las dos cifras es falsa, y lo compruebo con su linea:**
`LD-98` esta en cabecera en la **1953** y `LD-154` en la **662**. **El documento
no numera en orden de posicion**, asi que el mayor por numero y el mayor por
posicion no son el mismo. Se dicen los dos.

#### 2.c EL DESFASE DE LOS CORTES, MEDIDO Y NO REPARADO

| ficha | `fecha_corte` | marcador que cita | de que frase sale | hoy | desfase |
|---|---|---|---|---:|---:|
| `OP-L-01` | 2026-08-11 | 2.117 | *"marcador del cribado no se mueve: sigue en 2.117"* | 3388 | +1271 |
| `OP-L-02` | 2026-08-11 | 2.117 | *"marcador del cribado no se mueve: sigue en 2.117"* | 3388 | +1271 |
| `OP-L-03` | 2026-08-11 | 2117 | *"corte puesto 2117"* | 3388 | +1271 |
| `OP-I-01` | 2026-08-11 | 2117 | *"corte del puesto 2117"* | 3388 | +1271 |

**LA FRASE DE LA QUE SALE CADA CIFRA VA PUBLICADA, Y NO ES ADORNO.** El primer
patron que escribi (`sigue en (\d+)` a secas) daba **671** para `OP-I-01`, que
**no es un marcador**: es la frase *"el archivo sigue en 671 lineas"* hablando del
propio inventario. **Contar bien un patron y atribuirlo al sujeto equivocado es la
caida del recuadro de `AUDITOR.md` 0**, y por eso el patron lleva su contexto y la
salida publica la frase.

**EL HUECO MAYOR QUE `OP-I-01` NOMBRA, COTEJADO CONTRA EL ARCHIVO DE HOY.** La
ficha dice *"CUATRO DOMINIOS no han entrado al cribado intra (quality 792,
health_safety 283, risk_management 55 y seguridad_digital 55), o sea 1.185 nodos
vivos, un tercio del catalogo"*. Hoy el archivo tiene **10 dominios distintos** y
esos cuatro traen **quality 844, health_safety 192, risk_management 106 y
seguridad_digital 27** pares. **`CIFRA de los cuatro que HOY siguen sin un solo
par en el archivo: 0`.** **Se mide y se publica. La ficha NO se reescribe: eso es
plan, y si hace falta, se trae.**

#### 2.d EL ESTADO DE CADA UNA, EN UNA DE LAS TRES FORMAS Y EN NINGUNA OTRA

- **`OP-L-01` -> (a) SU PRODUCTO ESTA Y LA CUBRE.**
  `docs/plan/LECTURAS_DIRIGIDAS.md` existe (**214916 bytes por las dos
  convenciones**) y trae **en cabecera las 11 de 11** que la ficha describe.
- **`OP-L-02` -> (c) NO HAY EVIDENCIA QUE LA DECIDA. ES PARADA Y SE TRAE.** Su
  `evidencia` entera es una sola linea de prosa (*"MEDIDO el 11 ago 2026: 205
  pares fuera de cola, 11 leidos, 194 pendientes"*) y **no nombra ningun
  fichero**, asi que **no hay documento que medir**. Su `verificacion` habla de
  *"las tres nominas afectadas"* y de *"cada grupo del backlog"*, y **ninguna de
  las dos cosas tiene sede declarada en la ficha**. **No se inventa una.**
- **`OP-L-03` -> (b) SU PRODUCTO ESTA PERO NO LA CUBRE.** Sus dos ficheros existen
  (`docs/plan/BANCO_DEL_PLAN.md`, **61554 bytes**, y
  `docs/plan/LECTURAS_DIRIGIDAS.md`, **214916 bytes**), pero **lo que falta
  exactamente** es esto: la ficha describe **55 lecturas repartidas en 29 actos** y
  su `evidencia` dice *"LECTURAS_DIRIGIDAS.md, el reparto por acto"*, y **contar
  "el reparto por acto" no es contar un fichero**: no hay cifra que cotejar contra
  las 55.
- **`OP-I-01` -> (a) SU PRODUCTO ESTA Y LA CUBRE.** `INVENTARIO.jsonl` existe
  (**584554 bytes por las dos convenciones**) con **672 entradas, las 672 JSON
  valido**, contra las **323** que promete: **+349**. Y `10_INVENTARIO.md`, la
  vista humana, tambien esta (**34258 en disco y 33845 normalizados a LF**).

**CIFRA en la forma (a): 2 | en la forma (b): 1 | en la forma (c), o sea PARADA:
1.**

#### 2.e LO QUE ESTA TAREA NO HA TOCADO, MEDIDO AL TERMINAR

**El campo `estado` de las cuatro sigue como estaba**: `OP-L-01=LISTA`,
`OP-L-02=LISTA`, `OP-L-03=LISTA`, `OP-I-01=LISTA`. `docs/plan/OPERACIONES.jsonl`
mide al terminar **498085 bytes en disco y 498085 normalizados a LF**, `sha256` LF
`bbdde43a00bdc35c`, **identico al de la apertura de la tarea**.
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` cierra la tarea en `sha256` LF
`0a77b5a35a962621`, **el mismo con el que abrio la vuelta**. **Ninguna clase se ha
decidido y ningun veredicto se ha movido.**

### TAREA 3. EL CASO E: EL INVENTARIO DE EXENCIONES. CERRADA EN VERDE

**LA PARADA DE LA 187 NO ERA PARADA, Y EL REMEDIO ESTA PUESTO.** El acta 188,
punto `7.1`, lo adjudica con regla escrita: no habia dos reglas vigentes
peleandose, habia **un esperado tecleado en la vuelta 186** y **una orden escrita
en el encargo de la 187** que lo dejo viejo. **Y el `1` no se ha cambiado por un
`2`**, porque eso deja otra cifra tecleada que la proxima exencion volveria a
dejar vieja.

#### 3.a EL CASO E DEJA DE CONTAR UN TEXTO Y PASA A NOMBRAR

**EL CAMBIO VA DENTRO DEL PROPIO FICHERO**,
`scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py`, **sin clonarlo y sin
escribir un arnes nuevo para esquivarlo**, y **quien lo autoriza queda escrito en
su docstring**: acta 188, punto `7.1`.

**LA LISTA AUTORIZADA VIVE EN EL ARNES Y HOY TIENE DOS ENTRADAS**, cada una con la
vuelta y la decision que la autorizo, y con la **marca literal** que prueba que
esa exencion exige su declaracion:

| guarda eximida | vuelta | decision que la autoriza | marca de que exige su declaracion |
|---|---:|---|---|
| `toda cifra de bytes y todo sha con su pareja` | 178 | acta 186 punto 7.2, contestando la `P.2`: las cifras sin pareja de un reporte viejo NI SE EXIMEN NI SE REESCRIBEN, SE DECLARAN | `declaracion_de_cifras_sin_pareja` |
| `seccion4_que_no_calza` | 187 | encargo de la vuelta 187, TAREA 5.b, respuesta del acta 187 a la `P.2`: en el carril de cierre tardio la guarda de la `2.d` NO bloquea pero SE DECLARA | `if not dentro or sin_declarar:` |

**Anadir una tercera es ahora un acto visible y no un descuido.**

**EL INVENTARIO, LEIDO DEL FUENTE Y NO TECLEADO**, con el sello del sujeto al lado
(`scripts/loop/cerrar_reporte.py`, **97163 bytes normalizados a LF, 1844 lineas**,
`sha256` LF `2e37089d0389e67e`):

- **linea 1748**, forma `columna`, nombre `toda cifra de bytes y todo sha con su
  pareja`
- **linea 1813**, forma `if`, nombre `seccion4_que_no_calza`
- **`CIFRA exenciones halladas en el fuente: 2`**

**Y LA CUENTA VIEJA SE SIGUE PUBLICANDO Y YA NO ES EL VEREDICTO:** `not tardio`
aparece **2** veces. **Una cuenta de dos no distingue si las dos son las de la
lista o si una se cambio por otra**, y por eso el caso E queda **mas apretado**,
no mas flojo: exige tres cosas donde antes exigia una.

- **`(1) EXENCIONES QUE NO ESTAN EN LA LISTA AUTORIZADA: 0`**
- **`(2) DE LA LISTA QUE HAN DESAPARECIDO DEL FUENTE: 0`**
- **`(3) EXIMIDAS QUE NO EXIGEN SU DECLARACION: 0`**
- **`ANONIMAS (que es peor que las tres): 0`**

**LOS TRES ROJOS SE PRUEBAN, SOBRE FUENTES FABRICADOS EN MEMORIA Y NUNCA SOBRE EL
FICHERO VIVO**, y los tres CAEN:

- **(1) aparece una tercera exencion que nadie autorizo** -> `intrusas 1
  ['(sin nombre)']`, ROJO **SI**.
- **(2) desaparece del fuente una de las dos de la lista** -> `ausentes 1 ['toda
  cifra de bytes y todo sha con su pareja']`, ROJO **SI**.
- **(3) una eximida deja de exigir su declaracion** -> `mudas 1
  ['seccion4_que_no_calza']`, ROJO **SI**.

**Y LA MUTACION SOBRE EL FUENTE DE VERDAD, QUE ES LA QUE PRUEBA QUE EL VEREDICTO
NO ES UNA CONSTANTE:** con la lista autorizada mutada a **una** entrada, el cotejo
saca `intrusas 1 ['seccion4_que_no_calza']` y **CAE**.

**LA CORRIDA ENTERA, PEGADA POR SUS CIFRAS.**
`docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt` (**7544 bytes por las dos
convenciones**, `sha256` LF `be4edc90f2889552`): **`CIFRA casos: 22 | pasan:
22`**, **`CIFRA casos que CAEN al mutar su esperado: 21 de 21`**, **`CIFRA fallos:
0`**, **`VEREDICTO: VERDE`**, **exitcode 0**.

**LOS OTROS CASOS NO SE TOCARON, Y LA PRUEBA ES SU CUENTA:** el arnes pasa de
**18 casos con 17 que caen** a **22 casos con 21 que caen**. **Son los mismos mas
cuatro**, y los cuatro nuevos son las tres pruebas de rojo mas la mutacion de la
lista autorizada.

#### 3.b LA SALIDA QUE ENVEJECE SOLA, Y SU REMEDIO DE UNA LINEA

**QUE SE HIZO:** toda salida de arnes que publique numeros de linea de un fichero
vivo publica al lado el **`sha256` de ese fichero**, para que un diff futuro diga
**si se movio el sujeto o se movio el arnes** en vez de dejarlo a que alguien lo
deduzca.

**Y AQUI VA UNA MEDICION QUE ACOTA EL ENCARGO EN VEZ DE DARLO POR HECHO.** El
encargo dice *"hazlo en los arneses que ya lo publican (los cuatro de la 186
juzgan `cerrar_reporte.py`)"*. **Se midio antes de tocarlos, y de los cuatro solo
DOS publican numeros de linea del fichero vivo:**

| arnes de la 186 | publica numeros de linea de `cerrar_reporte.py` | sello anadido |
|---|---|---|
| `vuelta186_tarea2a_mutacion_pieza4.py` | **SI** (lineas 770 y 1446 en su salida) | **SI** |
| `vuelta186_tarea2b_mutacion_pieza2_cercas.py` | no (su salida no publica ninguna) | no |
| `vuelta186_tarea2c_mutacion_cierre_tardio.py` | **SI** (1748 y 1813, desde hoy) | **SI** |
| `vuelta186_tarea2d_mutacion_seccion4.py` | no (sus lineas son de reportes FABRICADOS) | no |

**Ponerselo a los que no lo necesitan habria movido dos salidas selladas para
nada**, y eso se dice en vez de hacerse callando.

**EL `numstat` DE LO QUE SE MOVIO AL HACERLO, PUBLICADO SALGA LO QUE SALGA:**

```
4	0	docs/loop/SALIDA_V186_T2A_MUTACION_PIEZA4.txt
50	11	docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt
23	0	scripts/loop/vuelta186_tarea2a_mutacion_pieza4.py
223	12	scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py
```

**Y LOS OTROS DOS DE LA 186 SALEN EN CERO FILAS**, medido y no supuesto:
`git diff --numstat` sobre `vuelta186_tarea2b_mutacion_pieza2_cercas.py`,
`vuelta186_tarea2d_mutacion_seccion4.py` y sus dos salidas devuelve **0 filas**.
`SALIDA_V186_T2A_MUTACION_PIEZA4.txt` cierra en **3906 bytes por las dos
convenciones**, `sha256` LF `2b444ffe193d27f9`, y su arnes sigue en
**`CIFRA fallos: 0`, `VEREDICTO: VERDE`**, exitcode **0**.

#### 3.c LA DOBLE CORRIDA NO RE CORRE UN ARNES QUE YA SALIO EN ROJO. ES LA `C.3`

**LA CAIDA, QUE LEVANTO EL AUDITOR Y QUE NO TRAJE.** La letra dice, sobre un arnes
ya sellado que cae en rojo: *"te detienes ahi, lo traes con su salida entera, **sin
re-correrlo** y sin arreglarlo"*. En la 187 ese arnes se corrio **dos veces mas**
dentro de la doble corrida de la 5.a, y **no hubo choque de ordenes**: la 5.a pide
*"corre cada arnes NUEVO dos veces"*, y ese no era nuevo.

**EL REMEDIO, EN `scripts/loop/vuelta188_tarea3c_nomina.py`** (clon declarado del
`vuelta187_tarea5a_nomina.py`): la doble corrida **excluye explicitamente
cualquier arnes que ya haya salido en rojo en esa misma vuelta**, y **lo dice en
su salida** con **el nombre del excluido, la ruta de su salida en rojo y el
motivo**. **Una exclusion muda seria peor que el problema.**

**LOS ROJOS NO SE TECLEAN:** salen de un registro en disco,
`docs/loop/ROJOS_DE_LA_VUELTA_188.txt`, una linea por arnes con la forma
`script | ruta de su salida en rojo | motivo`. **Si el fichero no existe, la
exclusion es vacia Y ESO TAMBIEN SE DECLARA**, con esas palabras: un cero que no
se publica no se puede auditar.

**Y QUEDA ESCRITA LA LETRA QUE EL ACTA 188 ADJUDICA EN SU `5.3`, para que no se
re-litigue: un arnes sellado en rojo detiene AL ARNES, no a la vuelta**; la vuelta
se cierra con la parada declarada.

**ARNES OBLIGATORIO, Y NACE EN ESTA VUELTA:**
`scripts/loop/vuelta188_tarea3c_mutacion_exclusion_por_rojo.py`. Salida:
`docs/loop/SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt` (**3565 bytes por las
dos convenciones**, `sha256` LF `622b67673e6d75f4`), **`CIFRA casos: 11 | pasan:
11`**, **`CIFRA casos que CAEN al mutar su esperado: 11 de 11`**, **`CIFRA fallos:
0`**, **`VEREDICTO: VERDE`**, exitcode **0**. Cinco casos: **(A)** un registro
vacio no excluye a nadie, probado con tres formas de vacio; **(B)** un registro
que nombra un arnes lo excluye y **el excluido desaparece de la lista que se
corre**; **(C)** la exclusion **no es muda**: nombre, ruta del rojo y motivo, los
tres; **(D)** la comparacion es **por nombre de fichero y no por ruta completa**,
probado con barras invertidas, sin directorio y con directorio de mas, y con un
nombre ajeno que **no excluye a nadie**; **(E)** una linea sin motivo **excluye
igual pero lo dice**, `(sin motivo declarado)`, **sin inventarle uno**.

**LA DOBLE CORRIDA DE VERDAD NO CORRE AQUI:** corre al cerrar la vuelta, cuando ya
existan todos los arneses que nacen hoy, y su salida es
`docs/loop/SALIDA_V188_T3C_NOMINA.txt`. **Se dice para que nadie la busque en esta
seccion.**

<!-- FIN ANEXO DE TAREAS -->
