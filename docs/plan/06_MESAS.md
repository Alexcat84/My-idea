# FASE 06: LAS MESAS

**Una MESA es una decision que no se puede tomar mirando un par**: hace falta la
familia entera delante.

> **REGLA QUE LAS GOBIERNA, adjudicada el 14 ago 2026: NINGUNA MESA SE SIENTA
> ANTES QUE LA MESA DE LA QUE DEPENDE.**

**Operaciones: `OP-M-01` a `OP-M-05`. LAS CINCO DECISION PENDIENTE**, porque una
mesa **es** una decision pendiente: lo que el plan puede hacer es dejarla lista
para sentarse.

---

## LO QUE CADA MESA TRAE ESCRITO ANTES DE SENTARSE

**Por la REGLA MADRE, ninguna se sienta sin estas cuatro cosas**: **nomina
medida**, **que decide**, **de que depende**, y **las opciones con su evidencia**.

| mesa | nomina | depende de | cobertura de pares |
|---|---:|---|---|
| **`OP-M-01`** puertas y portafolio | **16** | de las tres primeras cirugias | **18 de 120 leidos**, o sea el **15%** |
| **`OP-M-02`** la serie de Coleman | 83 nodos del libro, **16 de fase** | de la DECISION 1, ya aprobada | por medir |
| **`OP-M-03`** el racimo del pivote | **7** | ninguna | dos pares en B |
| **`OP-M-04`** la junta asesora | **4** | ninguna, **pero tiene una colgando** | el par 367 |
| **`OP-M-05`** customer development | **9 mas 7** | ninguna | dos actos vecinos |

---

# LOS CINCO BLOQUES DE APERTURA

**Esto es lo que se lee en voz alta el dia que cada mesa se siente. Sin releer nada
mas.**

---

## APERTURA . `OP-M-01`, LA MESA UNIDA

> ## **LAS 26 LECTURAS DIRIGIDAS, EJECUTADAS EL 12 ago 2026.**
>
> **La mesa NO se sento con dos de setenta y dos pares cruzados y en empate.** Se
> ejecuto la seleccion minima: **1 A, 2 C, 23 D**. **La frontera existe pero es una
> JERARQUIA, no una linea**; **un solo nodo repite**; y **los tres actos no son uno,
> son madre e hijo**. Cobertura del **17% al 36%**. El **trio de gates** ya esta
> decidido como avanzada: `OP-M-01-TRIO`, LISTA.

> **SU EXPEDIENTE COMPLETO:**
> [`EXPEDIENTE_MESA_UNIDA.md`](EXPEDIENTE_MESA_UNIDA.md), del 12 ago 2026, **sin
> recomendacion nueva donde no la hay**, y **con DOS correcciones de entrada: la nomina
> son 17 y los pares que no llegaran nunca son 113, no 58**. Trae los tres actos, la
> franja con sus tres candidatos, el trio de gates confirmado por lectura triple, las
> ocho aristas que cruzan la frontera vieja, y **la seleccion minima que decide: 24
> lecturas contra 113**. **Para adjudicar se lee el expediente.**

**QUE SE DECIDE.** Cuantos nodos quedan de los **dieciseis**, y **si queda alguna
frontera entre la puerta y el portafolio**.

**CON QUE NOMINA Y COBERTURA.** Dieciseis miembros, **120 pares posibles**. Leidos
**18**, de ellos **15 en A**, 1 B y 2 D. **Quedan 3 en cola y 58 QUE NO LLEGARAN
NUNCA** por estar fuera de ella. **La mesa se sienta sabiendo el 15% de sus pares,
y sabiendo que un 48% no lo va a saber si nadie los lee dirigidos.**

**LA RECOMENDACION DEL AUDITOR, ya adjudicada el 14 ago 2026**: dejan de ser dos
mesas, porque **dos mesas que comparten franja deciden dos veces lo mismo o se
contradicen**. La medicion la respalda: **doce aristas internas y ocho cruzan la
frontera vieja.**

| opcion | consecuencia |
|---|---|
| **UNA sola familia** | el grafo ya la trata asi. **Quince pares en A entre dieciseis nodos es el bloque de repeticion mas grande medido del catalogo** |
| **DOS familias con frontera nueva** | hay que **escribir la frontera**, y hoy no hay evidencia de donde ponerla: los ocho cruces del grafo apuntan a que no existe |
| **decidir con 18 de 120** | **es lo que pasa si no se leen dirigidas.** La decision se toma sobre el 15% |

---

## APERTURA . `OP-M-02`, LA SERIE DE COLEMAN

> ## **ADJUDICADA EL 12 ago 2026. `OP-M-02` ES LISTA.**
>
> **Coleman recibe el tratamiento de SERIE DECLARADA**, repartido en **siete
> operaciones hijas**, cada una con su simulacion por **P.7**. El programa unico se
> decide por cableado **13 contra 3**; las cinco fases con gemelos confirmados van
> **una a una**; **Adopt y Advocate NO se adjudican** y sus pares van a lecturas
> dirigidas; y **la cabeza de medios se trae al auditor**, porque el cableado y el
> archivo **no empatan: se contradicen**.

> **SU EXPEDIENTE COMPLETO:**
> [`EXPEDIENTE_MESA_COLEMAN.md`](EXPEDIENTE_MESA_COLEMAN.md), del 11 ago 2026, **sin
> recomendacion nueva donde no la hay**. Trae la correccion de la nomina a **28**, el
> reparto por fase, **los veredictos en crudo de las cinco fases dobles y los tres
> dudosos**, el desempate del 326 **por cableado, trece contra tres**, y la regla de
> orden **medios antes que fases** con su evidencia. **Para adjudicar se lee el
> expediente.**

### LO PRIMERO QUE ESTA MESA TIENE QUE SABER: **LA FASE 3 YA ESTA FUNDIDA, Y AGUANTA**

> **Esta mesa no debate una propuesta. Debate REPETIR ALGO QUE EL GRAFO YA HIZO Y
> SOSTUVO.**

**`fase_affirm_buyers_remorse` es hoy la fase 3 entera**, y carga **TRES ids dentro**
como alias: `fase_affirm`, `fase_affirm_reduccion_incertidumbre` y
`fase_affirm_reducir_remordimiento`. **Los tres existen como nodos deprecados**, o
sea que la fusion se hizo con el patron completo: superviviente, alias y baja.

**VERIFICADO EL 11 ago 2026** con `scripts/plan/aristas_por_alias_affirm.py`:

| | |
|---|---:|
| ids fundidos en uno | **4** |
| **aristas vivas que apuntan a un alias** y solo llegan por el resolutor | **10** |
| de ellas, **con su gemela literal al destino en el MISMO campo** | **10 de 10** |
| nodos que apuntan al destino **por su nombre propio** | **16** |

**LAS DIEZ ARISTAS QUE ATRAVIESAN EL ALIAS, nombradas:**

| el que apunta | campo | al alias |
|---|---|---|
| `fase_admit` | `nodos_siguientes` | `fase_affirm` |
| `fase_admit_celebracion` | `nodos_siguientes` | `fase_affirm` |
| `ocho_fases_experiencia_cliente` | `nodos_siguientes` | `fase_affirm` |
| `fase_activate` | `nodos_previos` | `fase_affirm` |
| `calibracion_intensidad_celebracion` | `nodos_siguientes` | `fase_affirm_reduccion_incertidumbre` |
| `fase_acclimate_experiencia_cliente` | `nodos_previos` | `fase_affirm_reduccion_incertidumbre` |
| `sistema_manejo_quejas` *(y es de `quality`, no de `core`)* | `nodos_siguientes` | `fase_affirm_reduccion_incertidumbre` |
| `cierre_segun_complejidad_venta` | `nodos_siguientes` | `fase_affirm_reducir_remordimiento` |
| `fase_activate_primera_impresion` | `nodos_previos` | `fase_affirm_reducir_remordimiento` |
| `welcome_call_cliente_veterano` | `nodos_previos` | `fase_affirm_reducir_remordimiento` |

> **LAS DIEZ AGUANTAN, y aguantan por la razon fuerte y no por la debil: LAS DIEZ
> TIENEN SU GEMELA LITERAL AL DESTINO EN EL MISMO CAMPO.** No es que el resolutor
> las rescate en el ultimo momento: **es que la fusion las reescribio y ademas dejo
> la referencia vieja.** Si manana se apagara el resolutor, **la fase 3 seguiria
> conectada igual.**

**LA COMPROBACION DE FONDO: ninguna arista quedo colgando.** La unica referencia
del destino que apunta a un nodo no vivo es `gestion_de_quejas_y_fidelizacion`, y
**tampoco es un cabo suelto: resuelve a `sistema_manejo_quejas`.**

> **Y ESO ES LO QUE LA MESA COMPRA O NO COMPRA.** No es un experimento: **es un
> precedente dentro de la misma serie**, con cuatro ids, diez aristas por alias y
> cero perdidas. **La pregunta de la mesa no es si el tratamiento funciona: es si se
> repite en las otras siete fases.**

**LO QUE EL PRECEDENTE NO PRUEBA, dicho aqui para que nadie lo estire:** las diez
referencias por alias **son redundancia**, no conectividad. Un dedup consciente del
resolutor las colapsaria. **La fusion salio limpia; la basura que dejo esta medida y
es la misma que `OP-S-07` trata en su fase.**

---

**QUE SE DECIDE.** Si las **ocho fases** de *Never Lose a Customer Again* reciben el
tratamiento de **SERIE DECLARADA**: un nodo-programa unico, un nodo por paso
colgando de el, y el numero en el titulo legitimado porque el programa lo explica.

**LA NOMINA, MEDIDA CON LOS DOS INSTRUMENTOS. Corte: 11 ago 2026, puesto 2.117.**
Instrumento: `scripts/plan/nomina_coleman.py`.

**CONTADOR, por la fuente declarada: 83 nodos citan el libro.** 68 lo llevan de
primera o unica casa y **15 de SEGUNDA CASA**.

**LA SERIE son 27 de esos 83**, con el criterio escrito dentro del script: es de la
serie el nodo cuyo id o titulo **nombra una de las ocho fases por su nombre propio**
o **enumera las ocho**, mas los nodos de canal del programa. *(La palabra suelta
"fase" no basta: metia `project_close_out`, que es de gestion de proyectos.)*

**EL PROGRAMA, REPARTIDO POR FASE. 19 nodos vivos y 20 ids:**

| fase | nodos vivos | cuales |
|---|---:|---|
| **1 Assess** | **3** | `fase_assess`, `fase_assess_ciclo_cliente`, `fase_assess_experiencia_cliente` |
| **2 Admit** | 2 | `fase_admit`, `fase_admit_celebracion` |
| **3 Affirm** | **1** | `fase_affirm_buyers_remorse` |
| **4 Activate** | 2 | `fase_activate`, `fase_activate_primera_impresion` |
| **5 Acclimate** | **3** | `fase_acclimate`, `fase_acclimate_experiencia_cliente`, `fase_acclimate_mapa_de_proceso` |
| **6 Accomplish** | 2 | `fase_accomplish`, `fase_accomplish_experiencia_cliente` |
| **7 Adopt** | 2 | `fase_adopt`, `fase_adopt_ciclo_cliente` |
| **8 Advocate** | 2 | `advocacy_customer_journey`, `incentivos_no_monetarios_advocacy` |
| **la cabeza, por duplicado** | 2 | `fases_de_retencion_de_clientes`, `ocho_fases_experiencia_cliente` |

**LOS MEDIOS, 8 nodos:** `seis_canales_comunicacion_assess`,
`seis_herramientas_comunicacion_fase_activate`,
`seis_herramientas_comunicacion_celebracion`, `estrategia_multicanal_bienvenida`,
`regalos_estrategicos_personalizados`, `regalos_estrategicos_sorpresa`,
`sorprender_cliente_estrategico`, `welcome_call_cliente_veterano`.

**LOS 15 DE SEGUNDA CASA: NINGUNO ENTRA A LA SERIE.** Su primera casa es otro
libro: Change by Design (4), The Startup Owner's Manual (5), Winning at New
Products (2), y uno cada uno The Founder's Dilemmas, The Lean Startup, Business
Model Generation y A Project Manager's Book of Forms.

> **LA CIFRA DE VEINTE DEL ENCARGO CALZA, Y CALZA EXACTA: son los ids del
> programa.** Medido hoy hay **19 vivos porque el vigesimo, `fase_affirm`, YA ESTA
> FUNDIDO**: esta deprecado y lo lleva como alias `fase_affirm_buyers_remorse`.

> **Y ESO ES LO MEJOR QUE TRAE ESTA MESA A SU PROPIA DISCUSION: LA FASE 3 YA
> RECIBIO EL TRATAMIENTO QUE SE DEBATE PARA LAS OTRAS SIETE.**
> `fase_affirm_buyers_remorse` lleva **TRES alias** dentro: `fase_affirm`,
> `fase_affirm_reduccion_incertidumbre` y `fase_affirm_reducir_remordimiento`.
> **Cuatro ids en uno.** La mesa no decide si el tratamiento funciona: decide si se
> extiende, **y tiene un precedente propio dentro de la misma serie.**

**COBERTURA DE LECTURA, y es la parte floja:** 351 pares posibles entre los 27,
**38 leidos** (26 D, 9 A, 3 B), **0 en cola** y **313 fuera de cola**. **FORMA
MEZCLADO, cobertura 38 de 351.**

> **Por el banco 9.26, esta forma es PROVISIONAL y no se puede leer como censo.**
> Las nueve A ya dicen algo firme: **cada fase con mas de un nodo tiene A por
> dentro** (assess, admit, activate, acclimate, accomplish), y las dos cabezas
> **estan en A entre si**, puesto 326. **La cabeza duplicada esta medida, no
> supuesta.**

**LA RECOMENDACION**, y viene de la **DECISION 1 ya aprobada el 9 ago 2026**: el
tratamiento de serie declarada **ya esta adoptado** para los programas desmontados
en piezas. Esta mesa decide **si Coleman lo recibe**, no si el tratamiento existe.

| opcion | consecuencia |
|---|---|
| **serie declarada** | **la cabeza ya existe por duplicado**: hay DOS nodos-programa, asi que la decision **trae dentro una fusion** |
| **no es serie** | hay que explicar **que hacen dieciseis nodos de fase y siete de canal sin cabeza declarada** |

**LO QUE ESTA MESA SABE HOY Y NO SABIA**: Coleman es **el segundo libro que mas
injertos aporta, QUINCE**, y su material esta pegado **en nodos de otros libros**.
**La serie no solo esta desmontada: esta ademas repartida fuera de su casa.**

---

## APERTURA . `OP-M-03`, EL RACIMO DEL PIVOTE

> ## **ADJUDICADA EL 12 ago 2026. `OP-M-03` ES LISTA.**
>
> **No hay una puerta en dos libros: hay DOS PUERTAS DISTINTAS DEL PROCESO MAS UN
> ACTO.** Los seis dudosos y el 753 **se resuelven por el criterio**, y el racimo pasa
> de **siete nodos sin ninguna arista** a **tres nodos y dos aristas**. El 1298 queda
> como **TERCERA FRONTERA DE DISPOSICION** del catalogo.

> **SU EXPEDIENTE COMPLETO:**
> [`EXPEDIENTE_MESA_PIVOTE.md`](EXPEDIENTE_MESA_PIVOTE.md), del 12 ago 2026, **sin
> recomendacion nueva donde no la hay**. Trae los siete miembros con sus pasos, **los
> TRES actos que forman las cuatro A**, **los seis dudosos en crudo**, las aristas de
> los siete y dos hallazgos nuevos: **los tres sanos separan la PUERTA del ACTO y los
> seis dudosos son todos entre puertas**, y **en el acto II el cableado no
> desempata**. **Para adjudicar se lee el expediente.**

**QUE SE DECIDE.** Si **Ries y Blank discrepan** sobre como decidir un pivote, o si
**solo entran por sitios distintos a la misma puerta**.

**LA NOMINA, MEDIDA CON LOS DOS INSTRUMENTOS. Corte: 11 ago 2026, puesto 2.117.**
Instrumento: `scripts/plan/nominas.py`.

**CONTADOR, por el nombre: 22 candidatos brutos.** **BARRIDO DE LAS A, por el
archivo: SIETE.** Los dos instrumentos levantan, y la lectura decide.

| el miembro | su libro |
|---|---|
| `decision_pivote_perseverar` | The Lean Startup, Ries |
| `pivotar_o_perseverar` | The Lean Startup, Ries |
| `pivote_estrategico` | The Lean Startup, Ries |
| `pivotar_o_proceder` | The Startup Owner's Manual, Blank |
| `pivote_o_proceder` | The Startup Owner's Manual, Blank |
| `pivote_startup` | The Startup Owner's Manual, Blank |
| `pivotes_e_iteraciones` | The Startup Owner's Manual, Blank |

**COBERTURA: 21 pares posibles, 13 leidos, 0 en cola, 8 FUERA DE COLA.**
**FORMA MEZCLADO, cobertura 13 de 21.**

**Y LA FORMA POR DENTRO, que es lo que la mesa tiene que mirar: LAS CUATRO A NO
HACEN UN ACTO, HACEN TRES.**

| acto | miembros | por que |
|---|---|---|
| **I** | `decision_pivote_perseverar` mas `pivotar_o_perseverar` | A del puesto 860 |
| **II** | `pivotar_o_proceder` mas `pivote_o_proceder` | A del puesto 268 |
| **III** | `pivote_estrategico`, `pivote_startup`, `pivotes_e_iteraciones` | A de los puestos 857 y 306 |

> **Y LOS TRES ACTOS ESTAN COSIDOS ENTRE SI POR SEIS DUDOSOS**, no por A: puestos
> **668, 737, 771, 843, 957 y 1298**. **Eso es exactamente la pregunta de la mesa
> puesta en numeros: tres nucleos firmes y seis costuras que nadie ha adjudicado.**

**CORRECCION DECLARADA A UNA CIFRA PUBLICADA.** La ficha de esta mesa decia **dos
pares en B, el 771 y el 843**. **Medido hoy hay SEIS.** Los otros cuatro son 668,
737, 957 y 1298. *(La cifra vieja no llevaba corte; por el banco 9.21 toda cifra
lleva el suyo, y el de esta es el puesto 2.117.)*

**LOS QUINCE DEL CONTADOR QUE EL ARCHIVO NO CONFIRMA, y por que no entran:**
ninguno tiene una sola A con el tema. El mas leido es
`actualizar_modelo_de_negocio_pivot_o_proceed`, con **11 veredictos y CERO A**.
*(La ficha decia ocho veredictos: hoy son once, y la conclusion no cambia.)* Le
siguen `catalogo_pivotes`, `decision_pivotar_o_proceder` y `pivot_post_ventas`, con
cinco lecturas cada uno y cero A. **Siete de los quince no tienen ni una lectura**,
entre ellos `coraje_para_pivotar`, `riesgo_no_pivotar_a_tiempo` y
`runway_como_numero_de_pivotes`.

> **Que un nodo lleve *pivote* en el nombre no lo mete en el racimo.** Los quince se
> quedan fuera **por el archivo, no por criterio**, y **los ocho pares fuera de cola
> pueden mover esto**: la nomina es firme hasta donde llega su cobertura.

**LA POSICION DEL AUDITOR, escrita el 11 ago 2026: UN NODO POR PUERTA.** El
criterio de reparto es **lo que el lector hace**, no de que libro salio el texto.

**CON UNA RESERVA, y es la parte que importa:**

> **Donde dos libros discrepan en la DISPOSICION, no hay duplicado: hay FRONTERA
> DECLARADA, y se ESCRIBE en vez de fundirse.**

**EL CASO CONCRETO DE ESTA MESA**: *buscar el punto brillante antes de pivotar*
contra *decidir rapido y sin miedo*. **No son dos maneras de decir lo mismo: son
dos disposiciones frente a la misma decision**, y un lector que reciba solo una de
las dos recibe media biblioteca.

| opcion | consecuencia |
|---|---|
| **un nodo por puerta** *(la posicion del auditor)* | el reparto lo manda **lo que el lector hace**: una puerta por entrada real, y los textos que sirven a la misma entrada se juntan |
| **frontera declarada donde discrepan** | los dos nodos **se quedan**, y **se escribe la discrepancia**: cuando la biblioteca discrepa de verdad, **la discrepancia se declara** |
| entran por sitios distintos sin discrepar | **la recomendacion resuelve los dos pares en B de una vez**, el 771 y el 843 |

> **La reserva no contradice la posicion: la delimita.** *Un nodo por puerta* vale
> para lo que el lector hace igual desde los dos textos. **Donde los dos textos le
> dicen que haga cosas distintas, juntarlos borraria una de las dos.**

> **Los dos pares en B dependen de esta decision, y no al reves.** Por eso la mesa
> va **antes** que su reclasificacion.

---

## APERTURA . `OP-M-04`, LA JUNTA ASESORA

> ## **ADJUDICADA EL 11 ago 2026. `OP-M-04` ES LISTA.**
>
> **DOS FUSIONES MAS UN ENLACE, no una fusion de cuatro.** Sobrevive
> `identificar_consejo_asesores` en el 367, por el paso 6 que entrega el testigo, y
> sobrevive `formalizar_junta_asesora` en el 328, **por desempate por cableado**. **El
> 1190 se libera sin cirugia.** La adjudicacion entera, con sus siete puntos y la
> correccion que la medicion hizo a la premisa del enlace, esta al final del
> expediente.

> **SU EXPEDIENTE COMPLETO:**
> [`EXPEDIENTE_MESA_JUNTA_ASESORA.md`](EXPEDIENTE_MESA_JUNTA_ASESORA.md), del 11 ago
> 2026. **Va sin recomendacion nueva**: trae los pasos de los cuatro nodos, los seis
> veredictos en crudo, las aristas actuales y las tres decisiones que se toman **en
> un solo acto**. Lo que sigue aqui es el resumen; **para adjudicar se lee el
> expediente.**

**QUE SE DECIDE, y CAMBIO el 11 ago 2026.** Ya **no** es *cual de los dos
sobrevive*. Es **como se enlazan y que solape se poda**.

**CON QUE NOMINA Y COBERTURA.** Cuatro miembros, **6 pares posibles, 6 LEIDOS.
COBERTURA COMPLETA**, la unica de las cinco mesas que la tiene.

**LA RECOMENDACION, que sale de `LD-01`**: `identificar_consejo_asesores` y
`formalizar_junta_asesora` **no son gemelos, son madre e hijo**, y **el paso 6 del
primero lo declara**: *formaliza el consejo asesor mas adelante, durante la
validacion de clientes*.

| opcion | consecuencia |
|---|---|
| **enlazar y podar el solape** *(lo que la lectura sugiere)* | los dos nodos **se quedan**, con **arista** de identificar hacia formalizar, y se poda lo que se repite en el medio |
| fundir | **borraria una secuencia real**: identificar y formalizar son **dos momentos distintos del mismo consejo**, separados por una etapa entera |

---

## APERTURA . `OP-M-05`, CUSTOMER DEVELOPMENT

> **SU EXPEDIENTE COMPLETO YA ESTA ESCRITO:**
> [`EXPEDIENTE_MESA_M05.md`](EXPEDIENTE_MESA_M05.md), del 12 ago 2026, **sin
> recomendacion nueva donde no la hay**. Trae la nomina con los dos instrumentos (**dos
> actos, de nueve y de siete**), sus **46 pares leidos** con **el unico dudoso en
> crudo**, las aristas que cruzan con dos mesas ya adjudicadas, y **la pregunta 3 ya
> contestada: quince lecturas entre los dos actos y las quince D**.

**QUE SE DECIDE.** Si el catalogo quiere **UNA puerta de entrada a Customer
Validation o DOS**. Y, con el acto de nueve delante, **si Customer Discovery es una
familia o un programa desmontado**.

**CON QUE NOMINA Y COBERTURA.** **Dos actos vecinos**: nueve nodos en customer
discovery y siete en customer validation. **Dieciseis en la sala.** Customer
discovery: **36 pares posibles, 16 leidos, 20 fuera de cola.**

**LA RECOMENDACION**: no hay adjudicacion, pero **la medicion apunta**:
`filosofia_customer_validation` **repite con quien abre la etapa** (dos A) y
**jerarquiza con quien la ejecuta** (cinco lecturas sanas en el tramo 1101-1200).

| opcion | consecuencia |
|---|---|
| **una puerta** | se funde con quien abre la etapa y **se conserva la jerarquia** hacia quien la ejecuta |
| **dos puertas** | hay que **decir en que se diferencian**, y las dos A dicen que en poco |
| **declarar serie**, como Coleman | **es la misma pregunta que `OP-M-02`**: un programa en piezas. **Conviene decidirlas el mismo dia y la misma cabeza** |

---

## `OP-M-01`: LA MESA UNIDA

**ADJUDICADO el 14 ago 2026: dejan de ser DOS mesas.** Motivo escrito: **dos mesas
que comparten franja deciden dos veces lo mismo o se contradicen.**

> **La medicion respalda la adjudicacion**: la nomina unida tiene **doce aristas
> internas y OCHO cruzan la frontera vieja**. **El grafo ya las trataba como una
> sola familia.**

**Y esto DEROGA** el orden viejo de *primero las puertas y luego el portafolio*.

**LA RESERVA, escrita con su cifra**: 120 pares posibles, 21 en cola, **18 leidos**,
**15 en A**, 1 B, 2 D, **tres pendientes** (1366, 1399, 1524) y **noventa y nueve
nunca encolados**. **La mesa se sienta sabiendo el 15% de sus pares.**

> **Quince pares en A entre dieciseis nodos: el bloque de repeticion mas grande
> medido del catalogo.** Y es tambien **el acto mayor del cierre transitivo**, con
> trece nodos conectados por A.

---

## `OP-M-02`: LA SERIE DE COLEMAN

**Decide si las ocho fases de *Never Lose a Customer Again* reciben el tratamiento
de SERIE DECLARADA**, ya aprobado por la DECISION 1: *un nodo-programa unico que
presenta la serie entera, un nodo por paso colgando de el, y el numero en el
titulo legitimado porque el nodo-programa lo explica.*

**POBLACION MEDIDA sobre nodos vivos:**

| | |
|---|---:|
| declaran el libro | **83** |
| nodos de **FASE** | **16** |
| nodos-**PROGRAMA** | **2** |
| nodos de **CANAL** | **7** |

> **La cabeza ya existe por duplicado: hay DOS nodos-programa.** Eso es un
> argumento a favor de declarar la serie, y a la vez **una fusion que hacer dentro
> de ella.**

**CRUCE CON EL RECORTE POSICIONAL**: Coleman es **el segundo libro que mas
candidatos a injerto aporta, QUINCE**, y dos de ellos (`voz_del_cliente_voc` y
`blueprint_de_experiencia`) **ya tienen operacion de destejido en la fase 02**.

---

## `OP-M-03`: EL RACIMO DEL PIVOTE

**Nomina de SIETE, sin cambios.** `actualizar_modelo_de_negocio_pivot_o_proceed`
**no entra**: ocho veredictos y **los ocho D**, incluido el puesto 1140.

**QUE DECIDE**: si **Ries y Blank discrepan** sobre como decidir un pivote, o si
**solo entran por sitios distintos a la misma puerta**.

| si | entonces |
|---|---|
| **discrepan** | es una **FRONTERA** y se declara, con las dos doctrinas escritas |
| **entran por sitios distintos** | **la recomendacion resuelve los dos pares en B de una vez**, el 771 y el 843 |

> **Los dos pares en B dependen de esta decision, y no al reves.** Por eso la mesa
> va antes que su reclasificacion.

---

## `OP-M-04`: LA JUNTA ASESORA . la mas pequena y la mas urgente

**Cuatro miembros**: `formalize_advisory_board`, `formalizar_junta_asesora`,
`identificar_junta_asesores`, `identificar_consejo_asesores`.

**QUE DECIDE, ACTUALIZADO el 11 ago 2026 por `LD-01`.** Ya no es *cual sobrevive*:
es **como se enlazan y que solape se poda**.

> **`LD-01` cerro la nomina en 6 de 6 y cambio la pregunta.**
> `formalizar_junta_asesora` contra `identificar_consejo_asesores` salio **D**, y no
> por poco: **el paso 6 de `identificar_` dice, con todas las letras, que la
> formalizacion va mas adelante.** **Son dos momentos del mismo consejo, no dos
> versiones del mismo nodo.**

**Y ESO CAMBIA TAMBIEN EL 1190, que cuelga de esta mesa.** La pregunta vieja era
*si el superviviente conserva el paso 6*. **Ya no hay superviviente**: si los dos
nodos se quedan enlazados, **el paso que difiere se queda donde esta**, y el 1190
se lee contra un nodo que **no** va a cambiar.

| escenario | el 1190 |
|---|---|
| **enlazar y podar** *(lo que la lectura sugiere)* | **deja de estar congelado**: sus dos nodos siguen existiendo con sus pasos |
| fundir de todos modos | sigue congelado, y con la misma trampa de antes |

> **La mesa sigue en pie, pero ya no decide lo mismo. Y si decide enlazar, LIBERA
> UN CONGELADO sin cirugia.**

> **TIENE UNA MESA COLGANDO, y es la primera dependencia mesa contra mesa
> registrada del plan: EL PAR 1190 NO SE PUEDE DECIDIR hasta que esta mesa decida
> el 367.**

**POR QUE, y esta bien medido**: los dos gemelos **difieren justo en la linea que
decide**. Uno **difiere la formalizacion en su paso 6** y el otro no.

| si el superviviente conserva | entonces el 1190 es |
|---|---|
| el paso 6 que difiere | **D**: formalizar es su hijo |
| la version de cuatro pasos | **A**: formalizar repite |

> **Y no contradice al 976**: aquel se leyo contra el gemelo que **no** difiere.
> **Las dos lecturas son correctas sobre nodos distintos.**

---

## `OP-M-05`: CUSTOMER DEVELOPMENT

**Levantada en la relectura R32, puesto 549**, sobre
`filosofia_customer_validation` contra `introduccion_validacion_clientes`, con
`earlyvangelists_ventas_tempranas` dentro por la A del puesto 1096.

**QUE DECIDE**: si el catalogo quiere **UNA puerta de entrada a Customer
Validation o DOS**.

| opcion | evidencia |
|---|---|
| **una puerta** | `filosofia_customer_validation` **repite con quien abre la etapa**: dos A |
| **dos puertas** | y **jerarquiza con quien la ejecuta**: cinco lecturas sanas en el tramo 1101-1200 |

> **LO QUE LA MEDICION DEL 11 ago 2026 ANADE Y NO ESTABA:** el cierre transitivo
> da **dos actos vecinos y grandes**, uno de **NUEVE** en customer discovery y otro
> de **SIETE** en customer validation. **La mesa se sienta con dieciseis nodos en
> la sala, no con tres.**

**Y comparte frontera con `OP-M-02`**: las dos deciden **si un programa en piezas
se declara serie**. Conviene que las decida la misma cabeza el mismo dia.
