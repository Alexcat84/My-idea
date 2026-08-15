# REPORTE DE LA VUELTA 35 (ejecutor Opus 5). FASE III, rama `pasada-unica`

**`P.5` PARO LA FUSION DE `OP-D-03`, Y NO POR UNA DUDA: POR UNA MEDICION. De los SEIS pares `A`
del acto, CINCO se leyeron contra texto que ya no existe. La vuelta 34 conto DOS. Las cinco
relecturas estan HECHAS, escritas enteras y SELLADAS con seis guardas verdes, y NO VOLCADAS,
porque lo que contradice una cifra publicada se declara como PARADA y no lo arregla el ejecutor
(`EJECUTOR.md` regla 5). Cero nodos tocados, cero veredictos volcados.**

**Y ANTES DE NADA, EL HECHO QUE CONDICIONA TODA ESTA VUELTA: LA VUELTA 34 NUNCA FUE AUDITADA, y
esta vuelta arranco con el encargo de la 34 ya ejecutado.**

- **Hash de partida:** `ae7f3272` (el reporte de la vuelta 34).
- **Hash final:** `48306f01`. **TRES commits contando la apertura** (`f1e50fda`, `e7eb703a`,
  `48306f01`), **y el de este reporte hace CUATRO.** Se dice asi a proposito: la vuelta 33 recibio
  una caida de reporte por esta cuenta exacta y la 34 la repitio para no repetirla.
- **Rutas tocadas** (`git diff --stat f1e50fda..HEAD`, corrido hoy): **22 ficheros, 1.665
  insertadas, CERO borradas**. Por carpeta: `docs/loop` **15**, `scripts/loop` **6**, `docs/plan`
  **1**. **Cero merges.** El hook corrio verde en los tres.
- **`dataset/` y el archivo de veredictos: CERO ficheros tocados**, medido con
  `git diff --name-only f1e50fda..HEAD` filtrado. **Ningun nodo nacio, murio, se movio ni se
  reescribio. Ningun veredicto se volco.**

---

## 0. EL ENCARGO QUE RECIBI YA ESTABA EJECUTADO, y lo que hice con eso

**`PROMPT_SIGUIENTE.md` no traia el encargo de esta vuelta: traia el de la 34.** Medido, no
supuesto:

| medicion de hoy | resultado |
|---|---|
| `docs/loop/loop.log`, ultimas lineas | el auditor corrio **de las 13:12:43 a las 13:30:52** del 15 ago 2026 (`USD 12.429116`, 1.089 s) y **la linea siguiente ya es `VUELTA 2 : EJECUTOR`**, que soy yo |
| fecha de fichero de `ACTA_AUDITOR.md` | **10:35:08**, y su ultima cabecera es **`ACTA DE LA VUELTA 33`** (`Select-String` sobre las cabeceras) |
| `git log -1 -- docs/loop/ACTA_AUDITOR.md` | **`4d33534c`, 2026-08-15 10:35:28**, que es el acta de la **33** |
| fecha de fichero de `PROMPT_SIGUIENTE.md` | **12:13:41**, y `git log -1` sobre el fichero da **`270ef4ea`**, el commit de la decision del fundador que abrio la vuelta **34** |
| `docs/loop/PARA_ALEXIS.md` al abrir | **no existia** (`Test-Path` dio `False`), asi que el auditor **no paro**: termino sin escribir |

> **EL AUDITOR DE LA VUELTA 34 CORRIO 1.089 SEGUNDOS, GASTO 12,43 DOLARES Y NO ESCRIBIO NADA.**
> Ni acta, ni encargo nuevo, ni parada. **La vuelta 34 esta sin auditar y su relectura ciega no
> existe.**

**QUE HICE CON UN ENCARGO YA EJECUTADO, y por que no lo re ejecute.** Verificado contra el
repositorio, punto por punto, en vez de contra el reporte:

| punto del encargo | estado medido hoy | donde se ve |
|---|---|---|
| **1.1** registrar acta y decision por su fecha | **HECHO** | `02_DESTEJIDOS.md:559`, `08_VERIFICACION.md:281`, `LECTURAS_DIRIGIDAS.md:837` citan el fichero de la parada |
| **1.2** decision 1, el reciprocado del deprecado | **HECHO** | commit `05734a97` |
| **1.3** decision 2, `MIN_BLOQUE` y la puerta | **HECHO** | commit `72d7e6ab` |
| **1.4** el criterio de la arista que falta, UNA vez | **HECHO** | `LECTURAS_DIRIGIDAS.md:861` |
| **2.1** destejer las costuras de `OP-D-03` | **HECHO** | commit `2a45f346` |
| **2.2** los pares internos como dirigidas | **HECHO** | commit `801c59f9`, **15** apariciones de `LD-75` a `LD-81` |
| **2.3** seguir el modo continuo | **ES LO UNICO VIVO, y es lo que esta vuelta tomo** | este reporte |

> **RE EJECUTAR 2.1 HABRIA SIDO DESTRUCTIVO: destejer lo ya destejido.** Por eso esta vuelta tomo
> **solo la parte viva** del encargo y **lo dice en vez de fingir que ejecuto siete puntos.**

---

## 1. EL ESTADO, APERTURA CONTRA CIERRE

**Las dos columnas son de dos corridas propias del MISMO instrumento**
(`scripts/loop/vuelta31_estado.py`, **sin tocarlo**): la de **APERTURA** corrida **antes de la
primera operacion** y commiteada antes de tocar nada (`f1e50fda`, salida
`SALIDA_V35_APERTURA.txt`), y la de **CIERRE** corrida **al cerrar**
(`SALIDA_V35_CIERRE.txt`). **Ninguna cifra viene de un acta ni de un reporte anterior.**

| | **APERTURA** | **CIERRE** |
|---|---:|---:|
| marcador: n / A / B / C / D | 3.388 / 581 / 83 / 8 / 2.716 | **3.388 / 581 / 83 / 8 / 2.716** |
| huecos / duplicados / clases fuera de ABCD | 0 / 0 / 0 | **0 / 0 / 0** |
| grafo: ficheros / ids / vivos / deprecados | 3.853 / 3.853 / 3.538 / 315 | **identicos** |
| enlaces / claves distintas | 16.849 / 15 | **16.849 / 15** |
| familias Weinberg / Horowitz / Hugos / Coleman / Rackham (vivos) | 72 / 93 / 111 / 75 / 47 | **identicas** |
| operaciones / estados / dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| inventario (de el, **20 figuras**) | 672 | **672** |
| indice rojo declarado | 18 lineas, 0 ausentes | **18 lineas, 0 ausentes** |
| fronteras de `OP-F-04-COL` | 14 de 15 | **14 de 15** |

> **Y LA IDENTIDAD SE COMPROBO POR MAQUINA, no a ojo:** `Compare-Object` sobre las dos salidas
> enteras da **cero diferencias sobre 84 lineas cada una**. **Que salga identica es tambien una
> medicion, y por eso el instrumento se volvio a correr en vez de copiarse el cierre de ayer.**

**LA TASA POR DOMINIO, recomputada del archivo en esta vuelta** (`vuelta35_tasa_dominio.py`,
sucesor declarado del que produjo `SALIDA_V34_TASA_DOMINIO.txt`, salida
`SALIDA_V35_TASA_DOMINIO.txt`): `core` **1.445 / 342 / 23,7 %**, `quality` 844 / 126 / 14,9 %,
`health_safety` 192 / 45 / 23,4 %, `entrega` 171 / 2 / 1,2 %, `environmental` 170 / 29 / 17,1 %,
`compras` 155 / 1 / 0,6 %, `franquicias` 148 / 18 / 12,2 %, `exportacion` 130 / 15 / 11,5 %,
`risk_management` 106 / 0 / 0,0 %, `seguridad_digital` 27 / 3 / 11,1 %. **Diez dominios, y ninguno
se movio: esta vuelta no volco un solo veredicto.**

**LA VARA POR TRAMO NO SE MUEVE Y NO SE COPIA DE NINGUN LADO:** es cifra del cribado, y **esta
vuelta no leyo ningun par de la cola**. `n` sigue en **3.388**.

---

## 2. LA MEDICION QUE PARO LA FUSION: `P.5` SOBRE EL ACTO DE `OP-D-03`

**El paso 2 del orden interno de `OP-D-03`** (`02_DESTEJIDOS.md:980`) es *solo entonces decidir
sobre los SEIS nodos*, o sea la fusion. **`P.5`** (`BANCO_DEL_PLAN.md:239`) manda, con estas
palabras: **cada acto se lee ENTERO DESPUES de su destejido y ANTES de su fusion**, y escribe su
motivo en la misma pagina: *leer un par cuyo nodo va a perder la mitad de sus pasos es leer algo
que va a dejar de existir*.

**SE MIDIO CON DOS VARAS INDEPENDIENTES, y la segunda es la que manda.**

| vara | instrumento | que compara |
|---|---|---|
| **FECHA** | `vuelta35_pares_opd03.py` | la fecha de la lectura del par contra la del ultimo cambio de sus dos ficheros, **las dos leidas de `git`** |
| **TEXTO** | `vuelta35_rancios.py` | **los pasos accionables del nodo en el commit de la lectura contra los de hoy**, con `git show` |

> **POR QUE LA SEGUNDA VARA NO ES ADORNO:** un fichero de nodo cambia por cosas que no son su
> texto (una redireccion de enlace, un reciprocado del `Gate`, un campo de fuente). **Contar como
> rancio un par cuyo texto no se movio seria inflar el hallazgo**, y esta casa acaba de pagar dos
> paradas por cifras infladas. **Las dos varas dieron la misma lista, y por eso se publica.**

**LA TABLA NO ESTA TECLEADA: es la salida del instrumento, pegada entera** (`EJECUTOR.md` regla 1,
cuarto renglon). Comando corrido en esta vuelta:

```
python scripts/loop/vuelta35_rancios.py
```

salida entera en `SALIDA_V35_RANCIOS.txt`, cierre pegado sin editar una coma:

```
RANCIOS POR TEXTO: 5
   277   A    optimizacion_embudo_get_customers de 10 a 5 pasos
   374   A    split_testing_experimentos_ab de 9 a 5 pasos
   452   A    ab_testing_optimizacion de 15 a 5 pasos
   1571  A    split_testing_experimentos_ab de 9 a 5 pasos
   1575  A    ab_testing_optimizacion de 15 a 5 pasos
AL DIA: 3 -> [(643, 'A'), (738, 'D'), (1061, 'D')]
```

**CINCO DE LOS SEIS PARES `A` DEL ACTO ESTAN RANCIOS.** El unico `A` al dia es el **643**, y lo
esta porque **ninguno de sus dos nodos cambio de texto**.

> **POR QUE LA VUELTA 34 CONTO DOS Y SON CINCO, y no es un descuido de aritmetica: es de
> alcance.** Los tres que no vio (`277`, `374`, `1571`) **no envejecieron por el destejido de esta
> operacion**, sino por los de la **FASE 01**, que se llevaron el bloque `6 a 10` de
> `optimizacion_embudo_get_customers` (`OP-F-04-WEI`) y el `6 a 9` de
> `split_testing_experimentos_ab` (`OP-F-04-RAC`). **La vuelta 34 miro solo hacia su propia
> cirugia.** `P.5` no dice *despues de TU destejido*: dice **despues de su destejido**.

---

## 3. LAS CINCO RELECTURAS: HECHAS, SELLADAS Y NO VOLCADAS

**Las dos mitades de esa frase son a proposito.**

**HECHAS, con la disciplina entera de la casa:** los **seis nodos impresos ENTEROS antes de
decidir** (`SALIDA_V35_NODOS_ENTEROS.txt`, con el instrumento sellado
`vuelta34_leer_opd03.py` **reutilizado y no reescrito**); **las razones viejas leidas enteras**
(`SALIDA_V35_RAZONES.txt`), porque una relectura que no lee la razon vieja no es una relectura;
**las aristas buscadas en los DOS sentidos** contra el grafo; y **el criterio citado y no
inventado**.

**EL CRITERIO ES EL DE ESTA MISMA CASA, DEL MISMO DIA Y SOBRE UNO DE ESTOS MISMOS NODOS:** el que
la vuelta 34 escribio en la razon del **738**, *lo compartido es la mecanica, partir en dos, medir
con las mismas metricas y comparar; uno optimiza una pagina y el otro decide si una funcionalidad
merece existir; CONTINUA, D, los dos sanos*. **La mecanica compartida no basta: el objeto decide.**

| puesto | los dos nodos | lo que la razon vieja daba por compartido y hoy NO esta | veredicto |
|---:|---|---|:---:|
| **452** | `ab_testing_optimizacion` contra `split_testing` | **exigir confianza estadistica antes de concluir**: se fue con el bloque 11 a 15. Y la descripcion *quince pasos en tres narraciones* ya no describe nada | **`A` a `D`** |
| **1575** | `ab_testing_optimizacion` contra `test_ab_precio` | la frase que la sostiene, *dentro de los QUINCE pasos*, **es falsa hoy**; y de las perdidas que proponia, **la confianza estadistica y el punto de saturacion ya no estan en el nodo** | **`A` a `D`** |
| **1571** | `split_testing_experimentos_ab` contra `test_ab_precio` | **el rigor estadistico ENTERO** (grupo de control similar, mismo periodo, cambio porcentual, diferencia neta): **ninguna de las cuatro esta**, las cuatro salieron con `OP-F-04-RAC` | **`A` a `D`** |
| **374** | `split_testing` contra `split_testing_experimentos_ab` | **el cambio porcentual**, que era la mitad de su simetria; y *nueve pasos partidos por la mitad*, que ya se destejio | **`A` a `D`** |
| **277** | `funnel_get_customers_optimizacion` contra `optimizacion_embudo_get_customers` | **los CINCO gestos que listaba, uno por uno**: hoy **ninguno de los cinco esta en los dos nodos**. Y la nota lateral de *Visual Website Optimizer* **tampoco esta ya en el nodo** | **`A` a `D`** |

**LAS SEIS GUARDAS DE LA PROPUESTA, ESCRITAS PARA CAER Y LAS SEIS VERDES**
(`vuelta35_relecturas.py`, salida `SALIDA_V35_RELECTURAS.txt`):

| guarda | resultado |
|---|---|
| 1. los seis nodos tienen HOY los pasos que las razones nuevas afirman | **6 de 6 OK** (5, 7, 5, 4, 5, 5) |
| 2. cada par sigue registrado y en la clase que la propuesta espera | **5 de 5 en `A`** |
| 3. la razon vieja se copia **del archivo por maquina**, nunca se transcribe | **hecha** |
| 4. la razon vieja queda **LITERAL dentro de la nueva**, o aborta | **5 de 5** (573, 664, 569, 1.574 y 1.452 caracteres, dentro de 4.657, 3.721, 4.652, 4.945 y 4.823) |
| 5. las aristas internas, buscadas **en los dos sentidos** contra el grafo | **5 de 5 sin arista**, tal como afirman las razones |
| 6. el marcador esperado, escrito **antes de que nadie vuelque** | de `A 581 / D 2.716` a **`A 576 / D 2.721`**, con `n`, `B` y `C` quietos. **Si el dia del volcado diera otra cosa, SE PARA** |

**NO VOLCADAS, y el motivo es una regla y no una prudencia.** `EJECUTOR.md` regla 5: **se para
cuando algo contradice una regla vigente o una cifra publicada con su corte, y entonces se escribe
como PARADA y no lo arregla el ejecutor.** Aqui pasan **las dos**: fundir con cinco `A` emitidas
contra texto muerto **contradice `P.5`**, y el recuento de dos pares rancios **es una cifra
publicada por la vuelta 34** que hoy no se sostiene. **La propuesta queda sellada en
`docs/loop/PROPUESTA_V35_RELECTURAS.json`, lista para un solo comando el dia que el fundador lo
diga.**

---

## 4. LA CONSECUENCIA, COMPUTADA Y NO DIBUJADA

**`P.6` manda que la nomina de acto se COMPUTA y no admite gusto.** Corrido por el propio
instrumento sobre el archivo de hoy:

| si las cinco se volcaran | |
|---|---|
| pares `A` que quedarian **dentro** del acto | **1**, el `643` (`split_testing` contra `test_ab_precio`) |
| nodos que seguirian en el cierre transitivo | **2**: `split_testing`, `test_ab_precio` |
| nodos que **saldrian** del acto | **4**: `ab_testing_optimizacion`, `funnel_get_customers_optimizacion`, `optimizacion_embudo_get_customers`, `split_testing_experimentos_ab` |

> **EL ACTO DE SEIS SE VOLVERIA UN ACTO DE DOS, y el paso 2 se quedaria sin los seis sobre los que
> decidir.** Y eso **no seria un fracaso de la operacion: seria el destejido haciendo su
> trabajo.** El acto existia **porque los nodos repetian**, y lo que repetia **eran los bloques
> que las cirugias se llevaron.**

---

## 5. LAS GUARDAS OBLIGATORIAS, todas por corrida propia de hoy

| guarda | resultado |
|---|---|
| `run_phase1.py --reaplico-curaduria` | **exit 0**, `GATE 0: OK`, **20 `[OK]` y 0 `[FALLO]`**, 3.853 compilados, 3.538 activos y 315 deprecados |
| `etiquetas_de_cara.py --aplicar` | **71 etiquetas** |
| `sync_assets_web.py` | **verde**, manifiesto escrito, seis assets |
| **el derivado sale BYTE IGUAL** | `git status` **no lista ni `dataset/metadata` ni `web/lib`** despues del ciclo entero |
| suite del motor (`engine/run_all_tests.py`) | **25 de 25** |
| suite web (`npx vitest run`) | **80 ficheros, 1.030 pasadas, 3 saltadas** |
| `npx tsc --noEmit` | **cero lineas** |
| verificador de mapas, **con las DOS varas** | **3 tablas, 17 filas, 0 discrepancias, exit 0** (`SALIDA_V35_VERIFICADOR_MAPAS.txt`) |

> **EL VERIFICADOR SE CORRIO CON LOS TRES PLANES SELLADOS A PROPOSITO.** Con solo dos, **sale en
> rojo con exit 1** y lo dice: la tabla del emblema de `OP-D-01` no calza contra ninguno de los
> dos planes dados. **Esa corrida en rojo esta hecha, guardada y no escondida**
> (`SALIDA_V35_VERIFICADOR_DOS_PLANES.txt`, **exit 1, 1 discrepancia**), y prueba que la vara 2
> del instrumento **si muerde** despues de la correccion que la vuelta 34 le hizo.

> **ESTA VUELTA NO ANADIO NINGUNA TABLA DE PARTICION**, y por eso el verificador sigue contando
> **3 tablas y 17 filas**, las mismas que la 34. Lo que se pego en `02_DESTEJIDOS.md` es un
> **bloque de salida de instrumento**, no una tabla tecleada.

---

## 6. CORRECCIONES DECLARADAS DE ESTA VUELTA

1. **La cifra del pendiente de doctrina 3 de la vuelta 34**: los pares rancios **no son dos, son
   CINCO**, y el motivo es de alcance, no de aritmetica. Texto viejo conservado entero.
2. **La conclusion publicada de las DOS FAMILIAS CERRADAS** queda **en suspenso, no volteada**: se
   dibuja con seis `A` y cinco estan rancias. **Volteada solo lo estaria despues del volcado**, y
   el volcado no es mio.
3. **Un fallo propio, declarado y no borrado:** la primera version de `vuelta35_pares_opd03.py`
   busco los ids del par en los campos `id_a` e `id_b` y **encontro cero de quince pares**. Los
   campos son `nodo_a` y `nodo_b`. **La cura fue mirar el fichero** (`vuelta35_claves.py`), no
   adivinar, y **el fallo quedo escrito dentro del propio instrumento** en vez de limpiarse.
4. **Un segundo fallo propio, cazado en la misma vuelta:** la primera corrida del cierre se
   escribio con `Tee-Object` seguido de `Select-Object -First 32`, **y ese `Select` corta la
   tuberia y trunca el fichero**. La comparacion apertura contra cierre salio falsamente
   distinta. **Se re corrio redirigiendo entero y las dos salidas son identicas linea a linea.**
   **Va escrito porque una tuberia truncada es exactamente la especie de fallo silencioso que este
   banco persigue.**

---

## 7. PENDIENTES DE DOCTRINA

1. **NUEVO Y ES EL DE ESTA VUELTA: hasta donde llega `P.5` hacia atras.** La regla dice *despues
   de su destejido*, y esta vuelta la leyo como **cualquier destejido que toque a los dos nodos
   del par**, no solo el de la operacion en curso. **Esa lectura es la que hace que sean cinco y
   no dos.** Ninguna pagina la escribe con esas palabras.
2. **NUEVO: dos nodos vivos con el mismo nombre en dos idiomas y sin repeticion de texto.** Es el
   caso del `277`, y **va marcado dentro de su propia razon** por la regla 5. Si el catalogo no
   quiere dos nodos que se llaman igual, **eso es una decision de nomenclatura y no un veredicto
   de repeticion**. Ninguna pagina dice que el nombre solo funda.
3. **NUEVO: que hace una operacion cuyo acto se disuelve.** Si las cinco se vuelcan, `OP-D-03`
   se queda sin los seis de su paso 2. **Ninguna pagina dice si la operacion se cierra, se
   replantea o se archiva.**
4. **SIGUE VIVO (era el 1 de la vuelta 34): que umbral acompana a `MIN_BLOQUE = 2`.** No se toco
   en esta vuelta y sigue dejando la puerta de costuras roja por 0,9 puntos.
5. **SIGUE VIVO (era el 2 de la vuelta 34): contra que nodos se recalibra esa puerta**, si los dos
   historicos ya no son reproducibles porque esta campana los destejio.
6. **SIGUE VIVO (era el 4 de la vuelta 34): un verificador que mide media vara si no le pasan un
   argumento.** **Esta vuelta lo comprobo en carne propia:** la primera corrida, con dos planes en
   vez de tres, salio en rojo por un plan que faltaba y no por un dato malo. **El silencio esta
   arreglado; el diseno no.**
7. **SIGUE VIVO (era el 6 de la vuelta 34): hasta donde atras alcanza el barrido del `9.10`.**
8. **SIGUE VIVO (era el 7 de la vuelta 34): los nodos propios de esta pasada escritos sin
   acentos**, con cura escrita en `05_SANEO.md:660` y sin numero de operacion.

---

## 8. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

| # | que | por que es discutible |
|---:|---|---|
| **d1** | **Leer `P.5` como *cualquier destejido*, no *el destejido de esta operacion*** | **es la decision de la que cuelga todo el hallazgo.** Con la lectura estrecha son dos pares y la vuelta 34 tenia razon; con la ancha son cinco. Lo sostengo con que la regla escribe *su destejido*, del acto, y con que su motivo (*leer algo que va a dejar de existir*) no distingue quien lo destejio. **Pero es una lectura mia de la letra** |
| **d2** | **No volcar las cinco, teniendolas hechas y con las guardas verdes** | un auditor puede decir que la regla 5 manda registrar lo mejor sostenido **y seguir**, y que dejar cinco `A` que hoy no se sostienen es el *verde y mal* del banco 9. **Lo sostengo con la otra mitad de la regla 5**, la que dice que lo que contradice una cifra publicada no lo arregla el ejecutor. **Las dos mitades apuntan a lados distintos y elegi una** |
| **d3** | **Aplicar a los cinco pares el criterio del `738`** | ese criterio lo escribio la vuelta 34, **que nadie audito**. Estoy apoyandome en una vara que todavia no paso por el auditor. **Lo digo yo antes de que lo diga el** |
| **d4** | **El `277` leido `D`** | **es el mas fuerte de la tanda, y lo marco como tal.** Es el **unico** par donde el objeto SI coincide (los dos optimizan el embudo *get customers*) y donde lo que separa es el procedimiento. **En los otros cuatro pasa al reves.** Quien sostenga que el objeto manda sobre el procedimiento dira que sigue siendo `A` **sin tener que forzar nada** |
| **d5** | **El `452` leido `D`** | los dos titulos dicen *A/B testing* y el catalogo quedaria con dos nodos que lo ensenan. Lo separo por el objeto, pagina contra propuesta de valor, **pero un lector del catalogo no ve objetos: ve dos fichas parecidas** |
| **d6** | **El `374` leido `D`** | es el par de **titulos mas parecidos del acto**, *Split Testing* contra *Split-Testing (Pruebas A/B)*. Sostengo que el nombre no es la vara. **Es el mismo argumento del d4 y del d5, y que se repita tres veces es en si un motivo de sospecha** |
| **d7** | **Dejar el `643` sin releer** | por el criterio de objeto **tambien seria `D`**, y lo dejo en `A`. Lo sostengo con que `P.5` no lo alcanza porque su texto no cambio, y con que releerlo es **re cribar**, otro frente. **Pero deja el archivo con un `A` que mi propio criterio no sostendria** |
| **d8** | **No re ejecutar los puntos 1.1 a 2.2 del encargo** | el encargo dice *al pie de la letra*, y no los ejecute. Lo sostengo con que **estaban hechos y medidos uno por uno**, y con que re destejer habria sido destructivo. **Pero es una decision mia sobre un encargo escrito** |
| **d9** | **Escribir `PARA_ALEXIS.md` y con eso detener el bucle** | el bucle no arranca solo despues de esto. Lo sostengo con que hay parada de verdad. **Un auditor puede decir que con la propuesta sellada el bucle podia seguir por `OP-D-04` sin esperar al fundador** |
| **d10** | **Reutilizar `vuelta34_leer_opd03.py` en vez de escribir uno nuevo** | es un instrumento de la vuelta que nadie audito. **Lo sostengo con que duplicarlo habria sido peor**, pero hereda lo que aquel tenga mal |
| **d11** | **Contar TRES commits y decir que el reporte hace cuatro** | la vuelta 33 cayo por esta cuenta y la 34 la escribio de otra forma. **Escribo las dos cifras a proposito**, pero si el auditor cuenta *commits de trabajo* dira que son dos |

---

## 9. PREGUNTAS

1. **Se vuelcan las cinco relecturas?** Estan selladas y con seis guardas verdes. **Recomiendo
   si, las cinco**, con el aviso de que **disuelve el acto de seis**.
2. **El `643` se relee?** **Recomiendo no**, y que quede declarado: `P.5` no lo alcanza y releerlo
   abre un re cribado que nadie abrio.
3. **Que pasa con `OP-D-03` si el acto se disuelve?** **Recomiendo cerrarla con su destejido hecho
   y sin fusion**, y mandar el `643` al frente que corresponda a un acto de dos.
4. **Y una que no es de plan sino de bucle: por que el auditor de la vuelta 34 corrio 1.089
   segundos y no escribio nada?** **La vuelta 34 sigue sin auditar y sin relectura ciega**, y esta
   vuelta se apoyo en varias de sus conclusiones para trabajar. **No lo puedo medir desde aqui.**
