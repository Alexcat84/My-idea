# -*- coding: utf-8 -*-
"""vuelta37_escribir_ld.py - ESCRIBE LA DECIMA TANDA DE LECTURAS DIRIGIDAS, LD-83 a LD-95.

Las trece lecturas del acto de OP-D-04 que la cola nunca va a traer. El texto de
cada una lo escribe el lector; este instrumento SOLO lo pega al final de
docs/plan/LECTURAS_DIRIGIDAS.md y aborta si la tanda ya estuviera escrita, para
no duplicarla si la vuelta se reintenta.

Uso: python scripts/loop/vuelta37_escribir_ld.py
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")

TEXTO = u"""

---

# DECIMA TANDA: **LAS TRECE QUE LEEN ENTERO EL ACTO DE `OP-D-04`** . `LD-83` a `LD-95`

**Escritas el 19 ago 2026, vuelta 37, dentro de `OP-D-04` y por `P.5`**, cuyo alcance quedo
adjudicado el 15 ago 2026: **solo dentro del acto en operacion, nunca fuera.**

**POR QUE SE PUEDEN LEER HOY, y la guarda corrio antes de escribir una sola linea.** `P.5` manda
leer el acto **despues** de su destejido. El destejido de `OP-D-04` **esta consumado**, y no por
renuncia: su unica costura y el injerto de fuente de `OP-F-02` eran **el mismo bloque**, y un solo
corte sirvio a los dos frentes. Medido hoy en `scripts/loop/vuelta37_destejido_opd04.py` (salida
`docs/loop/SALIDA_V37_OPD04_DESTEJIDO.txt`): de los siete nodos del acto **UNO estaba costurado y
SEIS sanos** sobre los 128 registros de `docs/COSTURAS_INTERNAS.jsonl`; el corte registrado de esa
costura es el **5** y la frontera que `OP-F-02` publico es **1 a 4 / 5 a 8**, el mismo sitio; y los
ocho pasos viejos, leidos por `git` del padre del commit de `OP-F-02`, se reparten **4 y 4 sin
perder nada**. **Leer antes seria leer texto que iba a cambiar.**

**POR QUE EMPIEZAN EN EL 83, medido y no supuesto.** Barrido hoy `docs/` entero por la cadena
`LD-` seguida de digitos (`scripts/loop/vuelta37_ld_opd04.py`, salida
`docs/loop/SALIDA_V37_LD_OPD04.txt`): **el numero mas alto escrito es el 82**, en
`docs/INTRA_DOMINIO_INFORME.md`.

**POR QUE SON LECTURA DIRIGIDA Y NO PARES SALTADOS, y esta medido:** los trece se buscaron hoy en
`docs/INTRA_DOMINIO_PARES.jsonl`, **3.388 filas leidas**, y **ninguno de los trece esta en la
cola**. **No entran en la cola y NO mueven `n`, que sigue en 3.388.**

**EL ACTO ESTABA A 8 DE 21.** Siete nodos dan **21 pares internos posibles**; el archivo traia
**ocho** (234, 585, 586, 823, 834, 844, 885 y 943) y faltaban **trece**. Es la misma figura que
`OP-D-02` resolvio con `LD-72` a `LD-74` y `OP-D-03` con `LD-75` a `LD-81`.

**LOS SIETE NODOS SE IMPRIMIERON ENTEROS ANTES DE DECIDIR NADA**
(`docs/loop/SALIDA_V37_OPD04_NODOS.txt`) y **las ocho razones ya escritas tambien**
(`docs/loop/SALIDA_V37_OPD04_RAZONES.txt`). **Las 21 aristas internas se buscaron en los dos
sentidos contra el grafo compilado, resueltas por el resolutor de alias antes de comparar (`P.1`):
de 21 pares, solo DOS tienen arista**, y las dos la tienen **en los dos sentidos**.

**LA VARA ES LA DEL CRIBADO, sin cambios:** el banco `9.6.1` (la linea o el procedimiento) con la
direccion del `9.6.2`, la precision del `9.6.3` (el tamano del solape no decide) y los dos polos
del `9.22`. **Y el criterio de la arista que falta es el escrito el 15 ago 2026** en
`docs/plan/02_DESTEJIDOS.md`: se declara donde lo compartido es un **BLOQUE** que uno expande de
una **LINEA** del otro; no se declara donde el solape es **LINEA contra LINEA** y los dos ya tienen
cableado propio.

## `LD-83` . `brainstorming_divergente` contra `construir_sobre_ideas_ajenas` . **D. MADRE E HIJO. ARISTA QUE FALTA**

**LA PRUEBA DE RECONOCIMIENTO DEL `9.6.2` SE CUMPLE EN UN SOLO SENTIDO.**
`brainstorming_divergente` dice, dentro de su **paso 2**, en cinco palabras, *construir sobre ideas
de otros*, como uno de los items de su lista de reglas. **`construir_sobre_ideas_ajenas` es el
metodo entero de esa linea**: compartir las ideas abiertamente en vez de guardarlas como propiedad
individual, hacer sesiones de construccion colectiva del tipo *si, y ademas*, y no atribuir las
ideas a una sola persona para que puedan evolucionar.

**Y LA MADRE CONSERVA MATERIA PROPIA QUE EL HIJO NO TOCA EN NINGUN PASO**, que es la otra mitad de
la prueba: la sala dedicada sin distracciones, la regla de cantidad sobre calidad y de diferir el
juicio, generar el mayor numero de ideas sin filtrar, y el registro visual en post-its.

**LO QUE EL HIJO ANADE NO CABE EN UNA LINEA, y aqui esta la cuenta.** Quitandole a
`construir_sobre_ideas_ajenas` lo que la madre ya dice, queda **su doctrina de propiedad de la
idea**: no acapararla y no firmarla. **Dos gestos con una sola logica y con su propio entregable**,
que es lo que lo decide: la madre entrega *una coleccion amplia de ideas divergentes documentadas
visualmente, lista para ser filtrada*, o sea **el producto de UNA sesion**; el hijo entrega *un
repositorio de ideas compartido y en evolucion continua accesible a todo el equipo*, o sea **una
practica que se repite en el tiempo**. Por la regla practica del informe 67.6, algo que se repite
en el tiempo es **PROCEDIMIENTO**, no linea. **CONTINUA: `D`, los dos sanos.**

**LA ARISTA, buscada hoy en los dos sentidos y resuelta por alias: NO HAY NINGUNA. `D`, sano, con
ARISTA QUE FALTA**, de madre a hijo, declarada para la **fase 04**.

> **DISCUTIBLE MARCADO, y es de los fuertes de la tanda, marcado antes de saber si acierto.** El
> puesto **586** lee ESTE MISMO HIJO contra `brainstorming_efectivo` y da **`A`**, y lo hace
> citando el `9.6.1` con estas palabras: *lo unico que el hijo anade al paso 2 de la madre es UNA
> LINEA, no atribuir las ideas a una sola persona*. **Lo que separa las dos lecturas es medible y
> esta en el texto de las dos madres:** el paso 2 de `brainstorming_efectivo` dice *priorizar la
> regla de construir sobre las ideas de otros **por encima de generar ideas propias de forma
> aislada***, y ese *por encima de las propias aisladas* **ya cubre el no acaparar**; el paso 2 de
> `brainstorming_divergente` **no lo dice**: solo nombra la regla. **Con una madre queda una linea
> fuera y con la otra quedan dos.** Quien sostenga que dos lineas siguen siendo lineas dira que
> este par tambien es `A`.

> **Y LO QUE ESTO DEJA A LA VISTA PARA LA FUSION, que no es de esta lectura:** si el **586** funde
> a `construir_sobre_ideas_ajenas` dentro de `brainstorming_efectivo`, y el **823** funde a
> `brainstorming_efectivo` con `brainstorming_divergente`, **los tres acaban en el mismo nodo pese
> a que este par lee `D`.** Es exactamente la tension que `P.5` existe para sacar a la luz, y se
> deja escrita, no resuelta.

## `LD-84` . `brainstorming_divergente` contra `design_attitude_vs_decision_attitude` . **D. SIN ARISTA DECLARADA**

**LA SESION CONTRA LA ACTITUD, y es la misma figura que el puesto 585 ya fijo en este acto** (*la
sesion contra la disciplina mental, y son niveles distintos*), aqui con el otro libro.

**LO COMPARTIDO ES EL IMPERATIVO DE DIVERGIR, y cabe en una linea por lado:**
`brainstorming_divergente` manda en su paso 3 *generar el mayor numero de ideas posible sin filtrar
prematuramente*; `design_attitude_vs_decision_attitude` manda en su paso 2 *dedicar tiempo y
energia a explorar multiples posibilidades antes de converger* y en su paso 4 *evitar adoptar la
primera solucion razonable*.

**LO PROPIO DE `brainstorming_divergente` ES EL TALLER ENTERO:** la sala sin distracciones, las
reglas explicitas, el registro visual. **LO PROPIO DE
`design_attitude_vs_decision_attitude` ES EL MARCO MENTAL:** aceptar la ambiguedad y la
incertidumbre como parte natural del proceso, y **alternar entre investigacion de mercado,
prototipado y generacion de ideas de forma no lineal**, que nombra dos actividades que el otro nodo
no menciona en ningun paso y que viven fuera de la sesion.

**LOS ENTREGABLES LO DICEN SIN AMBIGUEDAD, leidos hoy:** *una coleccion amplia de ideas divergentes
documentadas visualmente* contra *mentalidad y proceso de trabajo del equipo orientado a
exploracion divergente*. **Uno entrega ideas; el otro entrega una manera de trabajar. CONTINUA:
`D`, los dos sanos.**

**ARISTA: NO HAY, y NO SE DECLARA.** Lo compartido es **linea contra linea** y los dos tienen
cableado propio.

## `LD-85` . `brainstorming_efectivo` contra `generar_multiples_opciones` . **D. SIN ARISTA DECLARADA**

**LO COMPARTIDO ES LA SEPARACION DE FASES, dicha una vez por lado:** el paso 4 de
`brainstorming_efectivo` manda *dedicar sesiones especificas solo para generar opciones,
separadas de las de seleccion*, y el paso 1 de `generar_multiples_opciones` manda *generar
deliberadamente multiples alternativas antes de elegir una*. **Y su paso 3, la polinizacion
cruzada, es el paso 2 de la madre candidata**, construir sobre las ideas de otros, con otro nombre.

**LA PRUEBA DEL `9.6.2` NO SE CUMPLE, y se dice en vez de forzarla:**
`generar_multiples_opciones` **no cabe entero dentro de UN paso** de `brainstorming_efectivo`,
porque cae en dos, el 4 y el 2. **Asi que se aplica el `9.22` en los dos sentidos.**

**LO QUE `generar_multiples_opciones` ANADE ES UNA LINEA:** el plazo claro para la fase de
divergencia. **LO QUE `brainstorming_efectivo` ANADE ES UN PROCEDIMIENTO:** el juego de reglas
visibles (diferir el juicio, ideas descabelladas, foco en el tema) y **la condicion social**,
formar grupos donde la gente se conozca y tenga confianza para que no aparezca el escepticismo que
corta la generacion. **Procedimiento en UN solo sentido: el caso corriente del `9.22`, la vara se
aplica una vez y el par CONTINUA. `D`, los dos sanos.**

**LOS ENTREGABLES LO CONFIRMAN:** *una sesion de brainstorming documentada con un conjunto amplio
de ideas generadas colaborativamente* contra *un set documentado de al menos 3-5 alternativas de
solucion evaluadas antes de la decision final*. **La cosecha de una sesion contra una lista corta
ya evaluada.**

**ARISTA: NO HAY, y NO SE DECLARA:** lo propio de `generar_multiples_opciones` es una linea, no un
bloque que expanda nada.

## `LD-86` . `brainstorming_efectivo` contra `pensamiento_convergente_divergente` . **D. ENLACE YA PUESTO EN LOS DOS SENTIDOS**

**ESTE PAR YA ESTABA ANUNCIADO DENTRO DEL ACTO Y NADIE LO HABIA LEIDO.** La razon del puesto
**585**, escrita el 10 ago 2026, dejo la observacion por escrito: *`pensamiento_convergente_
divergente` enlaza a `brainstorming_efectivo`, o sea que es VECINO del racimo sin ser miembro, y la
mesa del racimo tendra que mirarlo*. **Medido hoy: la arista esta, y esta EN LOS DOS SENTIDOS.**

**LO COMPARTIDO ES LA ALTERNANCIA, una linea por lado:** el paso 4 de `brainstorming_efectivo`
separa las sesiones de divergencia de las de seleccion; el paso 3 de
`pensamiento_convergente_divergente` manda *alternar conscientemente entre fases de generacion de
ideas y fases de seleccion o eliminacion*.

**LO PROPIO DE `brainstorming_efectivo` es el mismo procedimiento del `LD-85`:** las reglas
visibles y la condicion social del grupo. **LO PROPIO DE `pensamiento_convergente_divergente` es
tambien un procedimiento y no una linea:** la metafora del embudo que abre y estrecha, la exigencia
de dedicar tiempo explicito a divergir **antes** de buscar la solucion, la alternancia consciente, y
la aceptacion de que descartar ideas prometedoras (*matar a los hijos favoritos*) es parte
necesaria del proceso. **Es una disciplina que se repite a lo largo del proyecto entero**, y su
entregable lo dice: *un mapa o registro de iteraciones mostrando ciclos de divergencia y
convergencia a lo largo del proyecto*, contra la sesion unica del otro.

**PROCEDIMIENTO EN LOS DOS SENTIDOS. Y NO ES EL PRIMER POLO DEL `9.22`, y se dice por que:** esa
figura exige que **cada uno expanda UNA LINEA DISTINTA del otro**, y aqui no ocurre: la unica linea
que se cruza es la misma, la separacion de fases. **Sin dos lineas distintas no hay enlace mutuo
que declarar; hay dos objetos que se rozan en un punto. CONTINUA: `D`, los dos sanos.**

**LA ARISTA YA ESTA PUESTA EN LOS DOS SENTIDOS**, verificada hoy resolviendo a nodo vivo. **El
grafo ya los tenia modelados como vecinos y el contenido dice lo mismo.**

## `LD-87` . `brainstorming_efectivo` contra `design_attitude_vs_decision_attitude` . **D. SIN ARISTA DECLARADA**

**LA MISMA FIGURA DEL `LD-84` con la otra sesion.** Lo compartido es el imperativo de divergir
antes de converger, una linea por lado: el paso 4 de `brainstorming_efectivo` contra los pasos 2 y
4 de `design_attitude_vs_decision_attitude`.

**LO PROPIO DE `brainstorming_efectivo`** son las reglas visibles y la condicion social del grupo.
**LO PROPIO DE `design_attitude_vs_decision_attitude`** es el marco de las dos actitudes con la
aceptacion de la ambiguedad y **la alternancia no lineal entre investigacion de mercado,
prototipado y generacion de ideas**, que sale de la sala de la sesion.

**Uno regula UNA REUNION; el otro regula EL PROYECTO. CONTINUA: `D`, los dos sanos. ARISTA: NO
HAY, y NO SE DECLARA.**

## `LD-88` . `reglas_brainstorming` contra `generar_multiples_opciones` . **D. SIN ARISTA DECLARADA**

**LO COMPARTIDO ES UNA PALABRA DENTRO DE UNA LISTA:** el paso 2 de `reglas_brainstorming` manda
*ir por cantidad* como uno de sus cinco items, y `generar_multiples_opciones` manda generar muchas
alternativas antes de elegir. **Y ahi se acaba.**

**LO PROPIO DE `reglas_brainstorming` ES EL PROTOCOLO ENTERO DE OSTERWALDER:** definir un enunciado
claro del problema **centrado en la necesidad del cliente**, hacer cumplir las cinco reglas,
**preparar al equipo con una inmersion previa** (visita de campo, entrevistas a clientes), capturar
en post-its para poder mover las ideas, y el calentamiento del *Silly Cow*. **LO PROPIO DE
`generar_multiples_opciones`** son el plazo y la polinizacion cruzada.

**LA INMERSION PREVIA ES LO QUE LO DECIDE, y no es un detalle:** `reglas_brainstorming` exige que
el equipo haya estado con el cliente **antes** de la sesion, y ningun paso de
`generar_multiples_opciones` menciona al cliente. **Uno prepara y conduce una sesion; el otro
impone una cuota de alternativas. CONTINUA: `D`, los dos sanos. ARISTA: NO HAY, y NO SE DECLARA.**

## `LD-89` . `reglas_brainstorming` contra `construir_sobre_ideas_ajenas` . **D. SIN ARISTA DECLARADA, Y ES EL SOLAPE MAS FINO DE LA TANDA**

**HAY QUE EMPEZAR POR LO QUE NO ESTA, porque es lo que decide.** El paso 2 de
`reglas_brainstorming` lista sus cinco reglas y **construir sobre las ideas de otros NO ES NINGUNA
DE ELLAS**: son *diferir juicio, una conversacion a la vez, ir por cantidad, ser visual, fomentar
ideas locas*. **La linea que en `brainstorming_divergente` y en `brainstorming_efectivo` engancha
con este hijo, aqui no existe.**

**Lo unico que se toca es *una conversacion a la vez*, que es una regla de turno de palabra, no de
construccion colectiva.** `construir_sobre_ideas_ajenas` habla de otra cosa: de a quien pertenece
la idea y de como se la deja evolucionar.

**Dos objetos distintos y dos entregables distintos:** *sesion de brainstorming documentada con
ideas capturadas en Post-its y agrupadas por tema* contra *un repositorio de ideas compartido y en
evolucion continua*. **CONTINUA: `D`, los dos sanos. ARISTA: NO HAY, y NO SE DECLARA.**

## `LD-90` . `reglas_brainstorming` contra `pensamiento_convergente_divergente` . **D. SIN ARISTA DECLARADA**

**LA TERCERA VEZ DE LA MISMA FIGURA EN ESTE ACTO** (`585`, `LD-86` y esta): **la sesion contra la
disciplina mental**, ahora con la sesion de Osterwalder.

**LO COMPARTIDO CABE EN UNA LINEA POR LADO:** *diferir juicio* e *ir por cantidad*, dentro del paso
2 de `reglas_brainstorming`, contra *dedicar tiempo explicito a generar multiples opciones sin
juzgarlas* del paso 1 de `pensamiento_convergente_divergente`.

**LO PROPIO DE `reglas_brainstorming`** es el protocolo con su enunciado del problema, su inmersion
previa, sus post-its y su calentamiento. **LO PROPIO DE `pensamiento_convergente_divergente`** es
el embudo, la alternancia consciente y matar a los hijos favoritos, **a lo largo del proyecto
entero y no de una sesion**.

**CONTINUA: `D`, los dos sanos. ARISTA: NO HAY, y NO SE DECLARA.**

## `LD-91` . `reglas_brainstorming` contra `design_attitude_vs_decision_attitude` . **D. SIN ARISTA DECLARADA**

**LOS DOS SON DEL MISMO LIBRO**, *Business Model Generation* (Osterwalder), medido hoy en el campo
`fuente` de los dos, **y por eso este par es el que mas empuja hacia la `A`: si un libro dice dos
veces lo mismo, la sospecha es legitima.** Se lee entero y no se resuelve por la fuente.

**LO COMPARTIDO ES EL IMPERATIVO DE NO CERRAR PRONTO:** *diferir juicio* y *fomentar ideas locas*
del paso 2 de `reglas_brainstorming`, contra *evita adoptar la primera solucion razonable* del paso
4 de `design_attitude_vs_decision_attitude`. **Una linea por lado.**

**LO PROPIO DE CADA UNO ES UN PROCEDIMIENTO, y son dos procedimientos que no se tocan.**
`reglas_brainstorming` **conduce una sesion**: enunciado del problema centrado en el cliente,
inmersion previa de campo, post-its, *Silly Cow*. `design_attitude_vs_decision_attitude`
**describe como decide un equipo**: la contraposicion de Collopy y Boland entre la actitud de
decision (generar alternativas es facil, elegir es dificil) y la actitud de diseno (disenar una
alternativa sobresaliente es dificil, y elegirla despues es trivial), con el *Design Squiggle* de
Newman como su figura. **En el mismo libro, uno es el taller y el otro el capitulo de por que el
taller existe. CONTINUA: `D`, los dos sanos.**

**ARISTA: NO HAY, y NO SE DECLARA.**

> **DISCUTIBLE MARCADO.** El paso 2 de `design_attitude_vs_decision_attitude`, *dedica tiempo y
> energia a explorar multiples posibilidades antes de converger*, **se puede leer como una linea
> cuya madre es la actitud y cuyo hijo es la sesion**, y entonces habria `ARISTA QUE FALTA` de
> `design_attitude_vs_decision_attitude` a `reglas_brainstorming`. **Lo que lo impide, y es la
> prueba de reconocimiento del `9.6.2` corrida hoy:** `reglas_brainstorming` **no cabe entero
> dentro de ese paso**, porque su paso 1 (enunciar el problema) y su paso 3 (la inmersion de campo)
> caen mas cerca del paso 3 de la otra, la investigacion de mercado. **El hijo cruza dos pasos de
> la madre candidata, asi que no hay madre e hijo.** Quien lea el paso 2 con manga ancha declarara
> la arista.

## `LD-92` . `generar_multiples_opciones` contra `construir_sobre_ideas_ajenas` . **D. MADRE E HIJO. ENLACE YA PUESTO EN LOS DOS SENTIDOS**

**LA PRUEBA DEL `9.6.2` SE CUMPLE LIMPIA.** `generar_multiples_opciones` dice en su **paso 3**, en
una linea, *permitir la polinizacion cruzada entre ideas distintas antes de converger en una*.
**`construir_sobre_ideas_ajenas` es el metodo entero de esa linea**: compartir abiertamente, el
*si, y ademas* colectivo, y no firmar las ideas para que puedan mutar. **Su propio resumen usa la
misma imagen**, las ideas que migran por la organizacion sufriendo permutaciones y combinaciones
frente a las que se vuelven propiedad privada y se estancan.

**Y LA MADRE CONSERVA MATERIA PROPIA QUE EL HIJO NO TOCA EN NINGUN PASO:** la exigencia de generar
multiples alternativas **antes de elegir** y **el plazo** que cierra la divergencia. **El hijo no
habla de elegir ni de plazos en ningun paso.**

**LO QUE EL HIJO ANADE ES UN PROCEDIMIENTO, con su entregable propio y continuo**, el repositorio
compartido en evolucion, frente al entregable puntual de la madre, *un set documentado de al menos
3-5 alternativas evaluadas antes de la decision final*. **CONTINUA: `D`, los dos sanos.**

**LA ARISTA YA ESTA PUESTA, y en los dos sentidos**, verificada hoy resolviendo a nodo vivo:
`construir_sobre_ideas_ajenas` nombra a `generar_multiples_opciones` en sus siguientes y este lo
nombra en sus previos. **Es el segundo de los dos unicos pares del acto con cableado, y el grafo ya
los tenia modelados como secuencia: primero la cultura de compartir, despues la exigencia de
opciones.**

## `LD-93` . `generar_multiples_opciones` contra `design_attitude_vs_decision_attitude` . **A. REPITEN. CIERRA EL TRIANGULO DE LA ALTERNANCIA**

**ES LA UNICA `A` DE LA TANDA, y por eso lleva la cuenta mas larga.**

**LO COMPARTIDO NO ES UN PARECIDO: ES LA MISMA INSTRUCCION DICHA DOS VECES.** El paso 1 de
`generar_multiples_opciones` manda *generar deliberadamente multiples alternativas de solucion
antes de elegir una*; el paso 2 de `design_attitude_vs_decision_attitude` manda *dedicar tiempo y
energia a explorar multiples posibilidades antes de converger* y su paso 4 *evitar adoptar la
primera solucion razonable, priorizando la exploracion divergente*. **Y el resumen del primero lo
repite palabra por palabra: no conformarse con la primera buena idea o solucion prometedora.**

**LO QUE CADA UNO ANADE ALREDEDOR CABE EN UNA LINEA, medido uno por uno:**

| nodo | lo que anade | linea o procedimiento |
|---|---|---|
| `generar_multiples_opciones` | fijar un **plazo** para la fase de divergencia | **linea**: accion unica |
| `generar_multiples_opciones` | permitir la **polinizacion cruzada** | **linea**, y ademas tiene su propio hijo que la ejecuta (`LD-92`) |
| `design_attitude_vs_decision_attitude` | **aceptar la ambiguedad** como parte natural del proceso | **linea**: criterio suelto |
| `design_attitude_vs_decision_attitude` | **alternar de forma no lineal** entre investigacion, prototipado e ideacion | **linea**: un orden de trabajo, sin decisiones dentro de si |

**LINEA EN LOS DOS SENTIDOS es el segundo polo del `9.22`: REPITEN, clase `A`, y el arreglo es
FUSION con las dos lineas repuestas en el nodo que sobreviva.**

**Y NO ES UNA LECTURA SUELTA: CIERRA UN TRIANGULO QUE EL ARCHIVO YA TENIA ABIERTO.** El **885**
(`design_attitude_vs_decision_attitude` contra `pensamiento_convergente_divergente`) es `A`, el
**943** (`generar_multiples_opciones` contra `pensamiento_convergente_divergente`) es `A`, **y
este era el lado que faltaba.** La razon del **885**, escrita el 11 ago 2026, lo habia anunciado:
*el catalogo cuenta la misma alternancia al menos cuatro veces*. **Los tres nodos de la alternancia
forman ahora un triangulo cerrado de tres `A`.**

**ARISTA: NO HAY NINGUNA, buscada hoy en los dos sentidos, y no se declara: una `A` manda fusion,
no enlace.**

> **DISCUTIBLE MARCADO, Y ES EL MAS FUERTE DE LA TANDA, marcado antes de saber si acierto.** Los
> **entregables no coinciden**: `generar_multiples_opciones` entrega *un set documentado de al
> menos 3-5 alternativas de solucion evaluadas*, un artefacto contable, y
> `design_attitude_vs_decision_attitude` entrega *mentalidad y proceso de trabajo del equipo*, que
> no es un artefacto. **El `9.6.2` dice que los entregables deciden mas rapido que los pasos**, y
> por ese lado esto seria `D`. **Lo que sostengo es que esa senal del `9.6.2` esta escrita para
> detectar la DIRECCION de un par madre e hijo, y aqui no hay madre e hijo**: ninguno cabe dentro
> de un paso del otro, y la figura que aplica es la del `9.22`, que pesa lineas y no productos.
> **Quien de mas peso al entregable que a los pasos leera `D`.**

## `LD-94` . `construir_sobre_ideas_ajenas` contra `pensamiento_convergente_divergente` . **D. SIN ARISTA DECLARADA**

**NO HAY SOLAPE DE PROCEDIMIENTO Y HAY QUE DECIRLO ASI, sin buscarle uno.** Lo unico que
comparten es el terreno: los dos viven en la fase divergente.

**`construir_sobre_ideas_ajenas` responde A QUIEN PERTENECE UNA IDEA**: compartirla, construir
encima, no firmarla. **`pensamiento_convergente_divergente` responde CUANDO SE ABRE Y CUANDO SE
CIERRA**: el embudo, la alternancia, y el descarte de las ideas prometedoras.

**Y el descarte es justamente donde se ve que no son lo mismo:** uno pide que las ideas circulen y
evolucionen, el otro pide que se maten a tiempo. **No se contradicen, pero tampoco se repiten:
gobiernan cosas distintas. CONTINUA: `D`, los dos sanos. ARISTA: NO HAY, y NO SE DECLARA.**

## `LD-95` . `construir_sobre_ideas_ajenas` contra `design_attitude_vs_decision_attitude` . **D. SIN ARISTA DECLARADA**

**LOS DOS ENTREGAN UNA MANERA DE TRABAJAR Y NO UN ARTEFACTO, y por eso el par se lee entero antes
de decidir:** *un repositorio de ideas compartido y en evolucion continua* contra *mentalidad y
proceso de trabajo del equipo orientado a exploracion divergente*. **Es el par de la tanda donde
los entregables mas se parecen en su forma.**

**Y AUN ASI SON DOS OBJETOS DISTINTOS, medido sobre los pasos.**
`construir_sobre_ideas_ajenas` gobierna **la propiedad de la idea dentro del equipo**: no
acapararla, construir encima de la ajena, no atribuirla a una persona. **Ni uno solo de sus tres
pasos habla de converger, de decidir ni de ambiguedad.**
`design_attitude_vs_decision_attitude` gobierna **como el equipo se planta ante la decision**:
tolerar la incertidumbre, explorar antes de converger, alternar de forma no lineal, no quedarse con
la primera solucion razonable. **Ni uno solo de sus cuatro pasos habla de quien es duena de la
idea.**

**Cero pasos compartidos, medido. CONTINUA: `D`, los dos sanos. ARISTA: NO HAY, y NO SE DECLARA.**

---

## SALDO DE LA TANDA, contado y no narrado

**TRECE lecturas: DOCE `D` y UNA `A`** (`LD-93`). **Dos con el enlace ya puesto en los dos
sentidos** (`LD-86` y `LD-92`), **una con `ARISTA QUE FALTA` declarada para la fase 04**
(`LD-83`), **diez sin arista y sin declararla**. **Ninguna mueve `n`: los trece estaban fuera de
cola, medido hoy sobre las 3.388 filas de `docs/INTRA_DOMINIO_PARES.jsonl`.**

**TRES DISCUTIBLES MARCADOS, todos antes de saber si acierto:** el `LD-83` (dos lineas contra la
una del `586`), el `LD-91` (el paso 2 de la actitud leido como linea madre) y el `LD-93` (los
entregables contra los pasos), **y el ultimo es el mas fuerte porque es la unica `A`.**
"""


def main():
    s = io.open(LD, encoding="utf-8").read()
    if "LD-95" in s:
        print("YA ESTABA ESCRITA: la tanda no se pisa.")
        return 1
    io.open(LD, "w", encoding="utf-8", newline="\n").write(s.rstrip("\n") + "\n" + TEXTO)
    nuevo = io.open(LD, encoding="utf-8").read()
    faltan = [n for n in range(83, 96) if ("`LD-%d`" % n) not in nuevo]
    print("ESCRITA la decima tanda en %s" % os.path.relpath(LD, RAIZ))
    print("cabeceras LD-83 a LD-95 presentes: %s" % ("las trece" if not faltan else faltan))
    return 0 if not faltan else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
