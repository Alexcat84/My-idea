# -*- coding: utf-8 -*-
"""_v72_texto_acta71.py . EL TEXTO EDITORIAL DEL REGISTRO DEL ACTA 71.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo coteja y lo adosa es
scripts/loop/vuelta72_registrar_acta71.py, que lo importa. Vive aparte por la
misma razon por la que el contenido de un lote vive aparte del generador: para
que el fichero que MIDE y el fichero que DICE no se confundan. Es el mismo
reparto que las vueltas 66 a 71 usaron con _v66_texto_acta65.py,
_v67_texto_acta66.py, _v68_texto_acta67.py, _v69_texto_acta68.py,
_v70_texto_acta69.py y _v71_texto_acta70.py.

AQUI NO HAY NI UN NUMERO DE LINEA TECLEADO. Cada cita va como marca [[CLAVE]] y
el registrador la sustituye por el numero que le devuelve BUSCAR la aguja de esa
clave en su fichero.

LO QUE ESTE TEXTO REGISTRA, y es lo que el encargo de la vuelta 72 pide: LA
VERIFICACION COMPLETA con la ciega 5 de 5; LA RECLASIFICACION de la caida de la
vuelta 70 con su sede medida y el contador de parada en CERO, mas la caida de
acta del auditor contada; los QUINCE discutibles A FAVOR con su vara citada; las
SIETE adjudicaciones de la seccion 6 con sus letras; los pendientes heredados
con su destino; y LAS TRES CORRECCIONES DECLARADAS que esta vuelta aplica (la
ficha de OP-L-03, el prefijo del generador y el ancla duplicada del rumbo), cada
una con su texto viejo entero y su cita.

LA SEDE DE CADA CORRECCION SE CITA POR AGUJA Y NO POR NUMERO TECLEADO, y eso
estrena TRES ficheros de aguja que las vueltas anteriores no usaban
(docs/plan/OPERACIONES.jsonl, scripts/loop/generar_plan_del_lote.py y
scripts/rumbos/banco_rumbos.json). NO ES MAQUINA NUEVA: la maquina de agujas
sale identica del ancestro y ya buscaba en el fichero que la CLAVE nombrase; lo
unico propio es la ruta, que vive en el bloque PROPIO como el resto de AGUJAS.
"""

TEXTO = """

---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 71, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (26 ago 2026, vuelta 72, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **DOCE** veces, **y la cifra va con su medicion del dia al lado en vez
de heredada**: **DIEZ** llevan esta misma cabecera de nivel dos (de la del acta 61 a la del acta 70,
contadas hoy por maquina sobre el fichero) y **DOS** son las mas viejas, que la pagina adoso con
cabecera de nivel tres. **La ultima de las doce es la del acta 70 en la linea **[[PAG_ACTA70]]** y la
anterior la del acta 69 en la **[[PAG_ACTA69]]**, las dos cotejadas HOY abriendo el fichero.**
**Ninguna cifra publicada de arriba se toca.**

**NINGUNA CITA DE LINEA DE ESTA SECCION ESTA TECLEADA:** cada una es una marca que el registrador
sustituye por el numero que le devuelve **buscar su aguja de contenido** en el fichero, y **antes de
escribir una sola letra el instrumento vuelve a barrer el texto ya sustituido y exige que TODO numero
de linea que aparezca en el salga de una aguja**; si uno solo no sale, cae en `ROJO` y **no escribe
nada**.

**El acta de la vuelta 71 abre en la linea **[[A71_ABRE]]** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md)**, su verificacion por corrida propia en la
**[[A71_VERIF]]**, su relectura ciega en la **[[A71_CIEGA]]**, LA RECLASIFICACION DE LA CAIDA DE LA
VUELTA 70 en la **[[A71_RECLAS]]**, el veredicto sobre la tanda del ejecutor en la
**[[A71_LIMPIA]]**, sus quince adjudicaciones de discutibles en la **[[A71_QUINCE]]**, sus siete
adjudicaciones nuevas en la **[[A71_ADJUD]]**, sus averias con nombre en la **[[A71_AVERIAS]]**, su
metrica de credito en la **[[A71_METRICA]]** y sus condiciones de parada en la **[[A71_PARADAS]]**.

### a) **LA NOTICIA DE LA TANDA ES DEL PROPIO AUDITOR, Y VA PRIMERA PORQUE ES LA QUE MUEVE EL CONTADOR DE PARADA**

**La tanda 71 del ejecutor salio LIMPIA ENTERA** (`CERO` caidas de clase, `CERO` de cifra publicada,
`CERO` de reporte, linea **[[A71_LIMPIA_CERO]]**), **y aun asi la noticia de la tanda existe: es una
CAIDA DE ACTA DEL AUDITOR, declarada por el auditor sobre su propia acta anterior.** **Va registrada
aqui con la misma letra con la que se registran las del ejecutor, porque un registro que solo anota
las caidas de una parte no se puede auditar.**

| | lo que el acta 71 mide, copiado de su linea | linea |
|---|---|---:|
| **el hecho, medido con `grep` corrido sobre `2d22e7e6`** | las dos cifras crudas de cableado de la vuelta 70 tienen **`CERO` ocurrencias** en esta misma pagina, con las formas abreviadas tambien barridas y adjudicadas una a una | **[[A71_RECLAS_HECHO]]** |
| **la medicion, con la sede negativa dicha entera** | `CERO` ocurrencias en `docs/plan/03_FUSIONES.md`, medido sobre el arbol **ANTERIOR** a la vuelta 71 | **[[A71_RECLAS_CERO]]** |
| **las sedes reales, que son TRES y van nombradas** | el **plan sellado** del lote `F` en `docs/loop/`, el **modulo de contenido** `_v70_lote_f.py` en `scripts/loop/`, y la **tabla 3.2 del reporte** de la vuelta 70 | **[[A71_RECLAS_SEDES]]** |
| **lo que el acta 70 escribio, y era otra cosa** | que el registro del lote `F` **en esta pagina** publicaba esas celdas, y sobre esa premisa clasifico la caida | **[[A71_RECLAS_ACTA]]** |
| **la especie de la caida del auditor** | **una sede afirmada sin `grep` corrido**, que es exactamente lo que la disciplina del dictado prohibe: **CAIDA DE ACTA DEL AUDITOR**, declarada con nombre y **contada** | **[[A71_RECLAS_CAIDA_ACTA]]** |
| **la reclasificacion, POR LA LETRA Y NO POR CLEMENCIA** | la regla de la parada define la caida de **CIFRA PUBLICADA** como un veredicto, el marcador, o una cifra que vive en `docs/plan/` o en el banco; **ninguna de las tres sedes medidas es eso** | **[[A71_RECLAS_DEFINE]]** |
| **EL CONTADOR DE PARADA** | la caida de la vuelta 70 es **DE REPORTE**, y **EL CONTADOR DE CLASE O CIFRA PUBLICADA VUELVE A CERO TANDAS** | **[[A71_RECLAS_CONTADOR]]** |
| **el manejo del ejecutor en su seccion 2.1** | **fue el debido**: declaro la discrepancia con el acta en vez de resolverla copiando, y la marco | **[[A71_RECLAS_MANEJO]]** |

> **EL CONTADOR VUELVE A CERO POR DOS VIAS Y NO POR UNA, Y EL ACTA LO DICE ASI EN VEZ DE DEJARLO
> IMPLICITO** (linea **[[A71_RECLAS_LETRA]]**): **aun sin la reclasificacion el contador habria vuelto
> a cero, porque la tanda 71 vino limpia.** **La reclasificacion no le perdona nada a nadie: pone la
> caida en su casilla.** **Y LA CORRECCION DECLARADA QUE LA VUELTA 71 ADOSO AL REGISTRO DE LA VUELTA
> 70 SE QUEDA DONDE ESTA**, entera y sin tachar: **el error del ejecutor existio**, la correccion es
> **correcta e inofensiva**, y **su corrijo vive donde el registro vive**. **Reclasificar de que
> ESPECIE es una caida no la borra.**

### b) **LA RELECTURA CIEGA: 5 DE 5 ACTOS CON SUPERVIVIENTE COINCIDENTE, Y CERO DISCREPANCIAS**

**El auditor extrajo los textos ENTEROS de los quince nodos en su version PRE fusion** (por `git show`
sobre el commit de la `TAREA 1` de la vuelta 71), **adjudico familia y superviviente por acto SIN leer
las razones escritas, y SOLO DESPUES destapo el dossier.** **Los cinco actos van uno a uno.**

| acto | la familia y el superviviente que el auditor adjudico CIEGO | linea |
|---:|---|---:|
| **38** | **UNA** familia (la escala del problema y los roles de compra, Blank); ciego `segmentos_de_clientes_problema_necesidad`, **el guion mas completo**. **Coincide** | **[[A71_CIEGA_38]]** |
| **39** | **UNA** familia (defensa en profundidad, Reason); ciego `defensas_en_profundidad_3`, **el UNICO que trata las defensas como falibles** mientras los otros dos son la misma taxonomia con otras palabras. **Coincide** | **[[A71_CIEGA_39]]** |
| **40** | **UNA** familia (la meta de traccion, Weinberg); ciego `traction_goal`, **el mas estructurado y consciente de fase**. **Coincide** | **[[A71_CIEGA_40]]** |
| **41** | **UNA** familia (las cinco letras de `DMADV` dos veces dentro de un proceso de seis pasos, Juran); ciego `design_for_six_sigma_dfss`. **Coincide** | **[[A71_CIEGA_41]]** |
| **42** | **UNA** familia (el equipo multifuncional de Cooper); ciego `equipo_multifuncional_real`, **el que corrige el modo de fallo que los otros dos describen**. **Coincide** | **[[A71_CIEGA_42]]** |

> **`CERO` DISCREPANCIAS EN LA CIEGA** (linea **[[A71_CIEGA_CERO]]**), **y el hecho del `D5` quedo
> confirmado leyendolo**: las dos razones del `acto 39` **coronan sobre SU par cada una** y **las dos
> matan al mismo nodo**. **Es UN solo gesto y no DOS FAMILIAS que declarar.**

### c) **LOS QUINCE DISCUTIBLES, TODOS A FAVOR, CON LA VARA QUE CADA UNO CITA**

**La relectura ciega se hizo sobre los discutibles que el ejecutor habia marcado ANTES de saber si
acertaba**, que es la unica forma en que ese marcado vale algo.

| | el discutible | lo que el acta 71 adjudica, y por que letra | linea |
|---|---|---|---:|
| `D1` | el `acto 39` pese a la `familia_de_ids` con **nomina entera** | **A FAVOR**: bien fundido, adjudicado en la seccion 6.2 | **[[A71_D1]]** |
| `D2` | el `39` contra un cableado de **11 a 2** | **A FAVOR por la letra**: el cableado solo habla a contenido empatado y **la vara de pasos hablo**; la ciega eligio el mismo nodo por el fondo | **[[A71_D2]]** |
| `D3` | el `38` contra un cableado de **12 a 4** | **A FAVOR**, misma letra: las dos razones escritas apuntan al mismo nodo y la ciega tambien | **[[A71_D3]]** |
| `D4` | el `42` elige al mas pequeno **por la sola vara de condiciones** | **A FAVOR**: `UNA SOLA VARA BASTA` es la letra, la de pasos EMPATA en los dos grandes y la de condiciones apunta | **[[A71_D4]]** |
| `D5` | las **dos razones del `39` coronan distinto** | **A FAVOR** por el precedente del `D6` del acta 70: cada corona es sobre SU par y las dos matan al mismo nodo | **[[A71_D5]]** |
| `D6` | tres supervivientes entran a la **cola de costuras** | **A FAVOR**: la cola **CITA, no juzga**; el delta esta medido; la poda es de la fase 04 y el costo quedo publicado | **[[A71_D6]]** |
| `D7` | tres nodos a **siete pasos**, segunda vuelta seguida | **A FAVOR** por el carril del catalogo mas rico; la tendencia queda **ANOTADA para la fase 04 como medida, no como regla** | **[[A71_D7]]** |
| `D8` | nueve `APPEND`, tres en un acto | **A FAVOR**: los nueve son gestos que las razones nombran como propios, y en el `39` son la respuesta al temor que el `D2` describia | **[[A71_D8]]** |
| `D9` | dos `CUBIERTO` contra **una** condicion | **A FAVOR**: la marca existe para eso y un `APPEND` habria duplicado lo que la condicion 1 del superviviente ya nombra | **[[A71_D9]]** |
| `D10` | los **nexos** de los `INCISO` son cosecha propia | **A FAVOR**: la letra del instrumento exige verbatim **el TROZO, no el nexo**, y los cinco trozos calzan contra su fuente | **[[A71_D10]]** |
| `D11` | fundir con `OP-L-03` en la entrada y **su letra vieja** | **A FAVOR**, adjudicado en la seccion 6.3 **con la correccion encargada**, que es la que el apartado e) de aqui abajo aplica | **[[A71_D11]]** |
| `D12` | el `41` sella **siete perdidas** y no repone nada | **A FAVOR**: las diez piezas de paso estan dentro, los seis pasos del superviviente **terminan en punto** (la juntura rota), y la unica perdida de sustancia esta **sellada con su motivo y NOMBRADA** | **[[A71_D12]]** |
| `D13` | una perdida sellada **sobre un supuesto desmentido** | **A FAVOR**: sellarla deja el rastro de que hubo correccion y no olvido; **callarla seria la degradacion muda** | **[[A71_D13]]** |
| `D14` | dos salidas **transcodificadas** de `cp1252` a `UTF-8` | **A FAVOR con regla practica encargada**: desde esta vuelta las salidas se escriben en `UTF-8` **DESDE EL ORIGEN** | **[[A71_D14]]** |
| `D15` | la correccion adosada **al registro y no al modulo** | **A FAVOR**, adjudicado en la seccion 6.4 | **[[A71_D15]]** |

### d) **LAS SIETE ADJUDICACIONES NUEVAS, CON SUS LETRAS Y CON SUS BORDES**

| | lo que el acta 71 adjudica | linea |
|---:|---|---:|
| **1** | **LA RECLASIFICACION** de la caida de la vuelta 70: **caida de REPORTE**, por la letra de la regla de la parada y la sede medida; **el contador de clase o cifra publicada esta en `CERO` tandas** y la caida de acta del auditor **queda contada** | **[[A71_ADJ1]]** |
| **2** | **LA FRONTERA DEL DUENO CUANDO LA `familia_de_ids` CUBRE LA NOMINA ENTERA**: **el `acto 39` ESTA BIEN FUNDIDO**, con **TRES varas** | **[[A71_ADJ2]]** |
| **3** | **LA FICHA DE `OP-L-03`**: **NO ES PARADA**, y su **CORRECCION DECLARADA VA ENCARGADA** por el carril del banco `9.10` | **[[A71_ADJ3]]** |
| **4** | **EL MODULO DE CONTENIDO DE UNA VUELTA PASADA NO SE EDITA**: `_v70_lote_f.py` y el plan sellado del lote `F` quedan como estan, **con su celda mala a la vista**, y la correccion vive en el registro y en las actas | **[[A71_ADJ4]]** |
| **5** | **LAS SALIDAS SE ESCRIBEN EN `UTF-8` DESDE EL ORIGEN**: **regla practica al encargo, no doctrina**, para que la letra de la regla 2 no vuelva a chocar con la pagina de codigos de la consola | **[[A71_ADJ5]]** |
| **6** | **EL PREFIJO DEL GENERADOR DE PLANES**: **CORRECCION DECLARADA ENCARGADA**, el prefijo derivado de `--operacion` en vez del defecto propio | **[[A71_ADJ6]]** |
| **7** | **EL ANCLA DUPLICADA DEL RUMBO**: **quien fabrica limpia**, por el principio de `P.16` por extension | **[[A71_ADJ7]]** |

> **LA ADJUDICACION 2 ES LA DE MAS PESO Y SU BORDE VA ESCRITO, PORQUE UNA ADJUDICACION SIN BORDE SE
> LEE COMO SI CUBRIERA MAS DE LO QUE CUBRE.** **Las tres varas**: la **PRIMERA**, que el dueno MEDIDO
> es una definicion cerrada de **tres fuentes** (acta 68, adjudicacion 2) y **la cobertura de otra
> entrada no es ninguna de las tres**; la **SEGUNDA**, que el principio del acta 70 es de **TIPO y no
> de cobertura**, y una `familia_de_ids` es **jurisdiccion sobre SU familia**, que la fusion dejo
> **servible y publicada** (linea **[[A71_ADJ2_TIPO]]**); y la **TERCERA, que es la que decide el caso
> entero**: **la propia entrada trae su resolucion APROBADA con fecha** (`DECISION 4` de la mesa de
> racimos, 9 ago 2026: *familia unica, fusion con alias*), **y fundir es EJECUTARLA, no usurparla**
> (linea **[[A71_ADJ2_RESOLUCION]]**).
>
> **EL BORDE, VERBATIM DEL ACTA Y EN SUS CUATRO LINEAS, PORQUE ES LO QUE LOS LOTES QUE VIENEN
> TIENEN QUE SABER** (la cita arranca a mitad de la frase de la TERCERA vara, que es donde el
> acta lo escribe, y se copia tal cual en vez de recortarse):
[[VERBATIM:A71_ADJ2_BORDE:4]]
>
> **DICHO EN LA LETRA DE UN LOTE:** una `familia_de_ids` **de nomina entera SIN resolucion aprobada
> que la fusion ejecute NO queda cubierta por esta adjudicacion**, y **si aparece va como PREGUNTA, no
> como fusion**.

### e) **CORRECCION DECLARADA, PRIMERA: LA CLAUSULA DE LA ERA DEL PAR EN LA VERIFICACION DE LA FICHA DE `OP-L-03`**

**Se ADOSA y no se tacha, que es la unica forma en que una correccion se puede auditar** (banco
`9.10`, y es **el mismo carril** que la ficha gemela de `OP-U-02` uso en la vuelta 66 y que aquella
ficha ya habia usado en su `evidencia` en la vuelta 48). **NO se estrena clave nueva de esquema**: la
correccion es **un elemento mas** de la misma lista `verificacion`.

**EL TEXTO VIEJO, ENTERO Y ARRIBA, LEIDO HOY DE LA FICHA:**

> `ningun acto se funde con un par interno sin veredicto`

**LA VARA NUEVA, EN SUS CUATRO MITADES**, que son las mismas cuatro que el acta 65 dio para la
clausula gemela: **PRIMERA**, que la lectura debida es la del **ACTO ENTERO** por `P.5` con su
correccion de alcance del 15 ago 2026, y no la de todas las combinaciones de pares; **SEGUNDA**, que
un **par sin leer** es el que esta **EN COLA Y SIN VEREDICTO**, y el recomputo cuenta `CERO` en
`en_cola_sin_leer` para los 47 actos del tramo; **TERCERA**, que lo que **bloquea** una fusion es el
triangulo `A` mas `A` mas `D` de `P.10` y la **guarda `1B`**, y en los dos casos el acto cierra
`DECLARADO Y NO FUNDIDO` con motivo sellado; **CUARTA**, que el **universo** es el tramo unico fijado
en la vuelta 64 con sus 47 `ABIERTOS`, y la lectura contraria anularia la operacion entera que el plan
sello.

**LA SEDE DE LA CORRECCION, CITADA POR AGUJA Y NO TECLEADA:** vive en la linea
**[[OPS_CORRECCION_OPL03]]** de [`OPERACIONES.jsonl`](OPERACIONES.jsonl), **dentro de la ficha de
`OP-L-03` y detras de la clausula vieja, que sigue en su sitio.**

> **UNA DIFERENCIA MEDIDA Y NO CALLADA, PORQUE LA REGLA 2 MANDA DECLARAR LA DISCREPANCIA EN VEZ DE
> RESOLVERLA COPIANDO:** el acta 71 llama a esta clausula **LA MISMA frase** que el acta 65 adjudico
> para `OP-U-02` (linea **[[A71_ADJ3_MISMA]]**). **EN SUSTANCIA LO ES**, y por eso la adjudicacion
> vale entera; **AL BYTE NO LO ES**, medido hoy por el propio instrumento de la correccion: la de
> `OP-U-02` dice *el acto se leyo ENTERO antes de fundirse: cero pares internos sin veredicto* y la de
> `OP-L-03` dice *ningun acto se funde con un par interno sin veredicto*. **Es la misma regla en voz
> pasiva sobre la lectura y en voz activa sobre la fusion.** **Por eso la correccion cita la letra de
> ESTA ficha y no la de aquella**, y **el instrumento cae en `ROJO` si la de `OP-L-03` no esta
> verbatim**: no se corrige lo que no se pudo leer, y menos citando la letra de otra ficha.
>
> **Y EL PRECEDENTE QUE ESTA CORRECCION CITA SE COMPRUEBA EN VEZ DE SUPONERSE**: el instrumento mide
> que la clausula gemela **sigue verbatim** en `OP-U-02` y que **la correccion de la vuelta 66 esta
> aplicada sobre ella**; si cualquiera de las dos faltara, seria `ROJO` y no escribiria nada.

### f) **CORRECCION DECLARADA, SEGUNDA: EL PREFIJO DEL NOMBRE DEL PLAN SE DERIVA DE `--operacion`**

**El instrumento es de nombre estable** (`generar_plan_del_lote.py`) **y por eso la correccion va por
el carril declarado**, el mismo que este fichero ya uso en la vuelta 63 y en la vuelta 65: **el texto
viejo se queda entero, citado VERBATIM en el docstring y en el sitio donde muerde, y no se tacha.**

**EL TEXTO VIEJO, ENTERO Y ARRIBA, QUE SON DOS LINEAS:**

> `ap.add_argument("--prefijo", default=None,`
> `                help="prefijo del plan; por defecto PLAN_V<vuelta>_OPU01_LOTE_")`

y, dentro de `main`:

> `prefijo = a.prefijo or ("PLAN_V%d_OPU01_LOTE_" % a.vuelta)`

**LA EVIDENCIA NO ES UNA IMPRESION: ES LA AVERIA 7.3 DE LA VUELTA 71.** El ejecutor paso
`--operacion OP-U-02`, **el generador lo acepto y sello BIEN el contenido**, y aun asi escribio el
fichero como `PLAN_V71_OPU01_LOTE_G.json`, **con el nombre de la operacion equivocada dentro del
nombre**. **Un plan cuyo NOMBRE miente sobre su operacion es exactamente la especie de trampa que esta
campana caza, y el instrumento no debe poder fabricarla.** **La vuelta 63 ya hizo `--operacion`
REQUERIDO con estas palabras** (*un generador de nombre estable que da `OP-U-01` por supuesto miente
en cuanto se use para otra operacion*), **y el prefijo quedo fuera de aquella correccion por olvido,
no por decision.**

**LO QUE CAMBIA Y LO QUE NO, Y SE DICE ENTERO:** cambia **UNA expresion**, el defecto del prefijo, que
ahora sale de `--operacion` sin sus guiones. **`--prefijo` SIGUE EXISTIENDO y sigue ganando cuando se
pasa**, asi que **ninguna llamada vieja que lo pase a mano cambia de resultado**. **LA ARITMETICA NO
SE TOCA**: guardas, cobertura, `INCISO`, juntura, validacion de perdidas y el campo `actos` del plan
salen exactamente igual que antes.

**LA SEDE DE LA CORRECCION, CITADA POR AGUJA:** el bloque declarado abre en la linea
**[[GEN_CORRECCION]]** de [`../../scripts/loop/generar_plan_del_lote.py`](../../scripts/loop/generar_plan_del_lote.py).

### g) **CORRECCION DECLARADA, TERCERA: EL ANCLA DUPLICADA QUE EL REANCLAJE DE LA VUELTA 71 FABRICO**

**QUIEN FABRICA LIMPIA**, por el principio de `P.16` **por extension** (la duplicada la fabrico un
**reanclaje** y no una fusion, y por eso va por el principio y no por la letra literal, que habla de
aristas del grafo).

**QUE PASO, MEDIDO:** el reanclaje de la vuelta 71 reescribio **UNA** referencia del rumbo
`nucleo_le_sirve_a_todo_el_mundo` del banco de rumbos. **El ancla vieja y la nueva resolvian AL MISMO
destino vivo**, asi que la lista `ancla` de ese rumbo quedo con
`segmentos_de_clientes_problema_necesidad` **DOS VECES**. **No es un dato malo: es un dato repetido.**

**LO QUE ESTA CORRECCION MIDE Y PUBLICA, PORQUE UNA BUSQUEDA NEGATIVA NO SE PUEDE CITAR** (regla 9):
**no basta con depurar el rumbo que el acta nombra**. El instrumento **barre los 49 rumbos enteros**
del fichero, **cuenta cuantos traen alguna ancla repetida y los nombra uno a uno**, antes y despues.
**Medido hoy: UN solo rumbo antes, `CERO` despues**, y **el nombrado por el acta y el medido por la
maquina son el mismo**. **La depuracion quita UNA entrada repetida y `CERO` destinos**: el conjunto de
ids de cada ancla sale identico, comprobado por maquina, y **el orden no se toca** (gana la primera
aparicion).

**LA SEDE, CITADA POR AGUJA:** el rumbo depurado esta en la linea **[[BANCO_RUMBO]]** de
[`../../scripts/rumbos/banco_rumbos.json`](../../scripts/rumbos/banco_rumbos.json), y **el diff es de
UNA linea borrada y `CERO` anadidas**.

### h) **LOS PENDIENTES HEREDADOS, NOMBRADOS CON SU DESTINO**

| pendiente | su destino, dicho y no supuesto |
|---|---|
| **los `DECLARADOS Y NO FUNDIDOS` que esperan el cierre de la fase 03** | **CATORCE**, y **esperan la PARADA DEL FUNDADOR**: el acta 71 recorre las condiciones de parada y dice que **el cierre de la fase 03 NO SE CUMPLE TODAVIA** (linea **[[A71_CIERRE03]]**), porque **quedan actos sin destino, dos de ellos con dueno, y la mesa `OP-M-03`** (linea **[[A71_CIERRE03_QUEDAN]]**) |
| **el subconjunto cerrado de un acto con puente** | **PENDIENTE NOMBRADO sin urgencia medida**: en lo que resta del tramo unico **no hay ningun acto con nodo puente**, asi que **la lista de los catorce ya no puede crecer por `P.10` en este tramo** |
| **la marca para *ya lo dice el `APPEND` de un hermano*** | **PENDIENTE NOMBRADO, y la especie se ensancho y se dijo**: la vuelta 71 la pago **TRES** veces, y **una de ellas fue dentro del MISMO nodo y no entre hermanos**. **El carril vigente alcanza**; lo que no existe es la marca propia |
| **el `INCISO` de condiciones** | **SIGUE SIN EXISTIR**: solo hay `INCISO` de pasos. Las perdidas `DE CONDICIONES` se **sellan con su motivo** y van **enrutadas a la fase 04** por el carril del acta 55, pregunta 5 |
| **el esquema de `OPERACIONES.jsonl`** | **PENDIENTE HEREDADO** (acta 55 en su cierre, acta 64 en su `D7`), y **por eso la correccion del apartado e) NO estrena ninguna clave**: entra como **un elemento mas** de la lista `verificacion` que ya existia, y **el numero de claves de las 71 fichas sale identico**, medido por el instrumento antes y despues |

### i) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba**, **NO deshace ninguna fusion**, **NO re-lee ni un veredicto
de las siete colisiones vigentes**, **NO toca la mesa `OP-M-03` ni sus dos colisiones**, **NO toca las
CINCO colisiones de `OP-U-02` ya publicadas**, **NO ejecuta ninguna de las cinco fichas `OP-M-02`
consumidas** (lo consumado no se ejecuta ni se rehace), **NO funde ningun acto con dueno** (el `31` y
el `37` quedan con los suyos), **NO edita `_v70_lote_f.py` ni re-sella el plan del lote `F`** (que es
la adjudicacion 4 del acta 71 cumplida a la letra), **NO borra ni tacha ninguno de los tres textos
viejos que las tres correcciones citan**, **NO mueve la linea base del censo de colisiones** (la mueve
el auditor) y **NO anade ni una fila ni una columna a ninguna tabla de registrador**, que es la
adjudicacion 3 del acta 69 aplicada sobre el instrumento que la registra.
"""
