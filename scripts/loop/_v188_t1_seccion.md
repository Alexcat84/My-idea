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
