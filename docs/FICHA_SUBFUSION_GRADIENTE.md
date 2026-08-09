# FICHA DE SUB-FUSION iluminada por la campaña del gradiente

Abierta desde `docs/audits/AUD-08-Gradiente_Nucleo_Mundo.md`. Los casos salieron
**de rebote** leyendo la cola de pares: ninguno se buscaba.

**Estado: ABIERTA, pendiente de visto del fundador para ejecutar.**

La ejecucion sera **lectura de fusion clasica**, con **la valvula de pasos
accionables como ultima palabra**, por lotes, y con la **maquinaria de
deprecacion existente**: alias, `merged_originals`, **nada se borra**.

> **Cada caso se ADJUDICA leyendo. Esta ficha registra sospechas fundadas, no
> veredictos.**

---

# LADO NUCLEO, cinco casos con nombre

Estos cuatro **corrigen la cuenta sin nombre** que quedo en el marcador del lote 5
de `docs/GRADIENTE_VEREDICTOS.md`.

**Estado: el caso 1 esta CERRADO** (no se funden, ver su razon). **Los casos 2, 3
y 4 siguen abiertos**, y el **caso 9** se sumo en el lote 9.

## 1. GOLDRATT, dos nodos. **CERRADO: NO SE FUNDEN**

> **CERRADO el 9 ago 2026**, adjudicado por el auditor con los datos de grafo que
> trajo el ejecutor al abrir esta ficha. **La entrada no se borra: se marca
> cerrada con su razon**, que es como se cierra todo en esta casa.
>
> **La razon**: los dos nodos son **una escalera tejida con delegacion
> explicita**. Estan encadenados **en los dos sentidos**, y **el paso 3 del
> primero delega literalmente en el segundo** (*"Aplicar los cinco pasos de
> enfoque para gestionar las restricciones identificadas"*). Eso no es un
> concepto partido por accidente: **es un peldano que apunta al siguiente a
> proposito.**
>
> **Lo unico vivo de Goldratt** es la **violacion de gradiente del nodo del
> mundo**, `quality/constraint_management`, **que ya tiene veredicto propio**
> (puestos 9 y 10) y se arregla profundizando el mundo, no tocando el nucleo.

**Lo que sigue es el registro original de la sospecha, conservado.**

`nucleo/teoria_de_restricciones` (3 pasos) y
`nucleo/cinco_pasos_enfoque_restricciones` (5 pasos).

Vistos en el **lote 3, puestos 9 y 10**: **tres nodos para un tema y medio**
contando el del mundo (`quality/constraint_management`).

**Pregunta de lectura**: la teoria con metricas y los cinco pasos, ¿son **dos
conceptos de verdad**, o **un concepto partido**?

> **EVIDENCIA VERIFICADA CONTRA EL GRAFO, que juega EN CONTRA de la sospecha y se
> registra por eso mismo.** Los dos nodos **ya estan encadenados**:
> `teoria_de_restricciones` declara a `cinco_pasos_enfoque_restricciones` en sus
> `nodos_siguientes` y este lo declara en sus `nodos_previos`. Y hay mas: **el
> paso 3 del primero es literalmente** *"Aplicar los cinco pasos de enfoque para
> gestionar las restricciones identificadas"*, es decir, **delega de forma
> explicita en el segundo**.
>
> Eso es exactamente lo que hace una **escalera de dos peldaños bien tejida**, no
> un nodo partido por accidente. **La lectura arranca con la carga de la prueba
> del lado de la fusion**, y bien puede terminar en *"no se funden"*.

## 2. BRAINSTORMING, trio confirmado

`nucleo/brainstorming_efectivo` (4 pasos), `nucleo/brainstorming_divergente`
(8 pasos) y `nucleo/reglas_brainstorming` (5 pasos). **Los tres del nucleo, los
tres activos.**

Vistos en los **lotes 3 y 5, puestos 13, 18 y 24**. La sospecha subio de par a
**trio confirmado** cuando el puesto 24 destapo el tercero.

**Tres nodos del nucleo sobre el mismo tema**, y uno de ellos con **voz de
manual y anglicismos**: *Post-it notes* y el ejercicio *Silly Cow* estan en los
pasos 4 y 5 de `reglas_brainstorming`.

**Pregunta de lectura**: los tres declaran **las mismas reglas base** (diferir el
juicio, cantidad sobre calidad, construir sobre ideas de otros). Lo que los
podria separar es lo que cada uno tiene **encima** de esa base: el ritual de
inmersion previa, la **capa de IA como participante** (pasos 5 a 8 de
`brainstorming_divergente`) y la separacion divergencia-convergencia. **La
valvula dira si eso sostiene tres nodos, dos o uno.**

## 3. `criterios_seleccion_proveedores`, costura visible

Visto en el **lote 5, puesto 27**. **Diez pasos que son dos nodos pegados:**

| pasos | de que hablan |
|---|---|
| **1 a 6** | **la matriz ponderada**: que evaluar, repartir importancia hasta 100%, como calificar, evaluar, multiplicar, sumar y elegir |
| **7 a 10** | **la gestion de la base de proveedores**: que necesitas comprar, mirar mas alla del precio, reducir el numero de proveedores para ganar poder, y anotar la lista de preferidos |

**Los pasos 1 a 6 cierran una secuencia completa** (terminan eligiendo al
proveedor con el puntaje mas alto) **y el paso 7 abre otra**.

> **PRECISION VERIFICADA Y TRAIDA POR EL EJECUTOR, sin decidirla.** El encargo
> describe el paso 7 como el *"define que necesitas comprar"* **repetido al
> final**, y el veredicto del puesto 27 dice que **reaparece**. Leidos los diez
> pasos, **la frase no aparece dos veces**: el paso 1 es *"Decide que vas a
> evaluar en cada proveedor"*, que es fijar criterios, no definir la compra. **El
> paso 7 aparece una sola vez, y en el puesto 7 de 10, no al final.**
>
> **El hallazgo se sostiene entero y el defecto es el mismo**, solo que su nombre
> exacto es otro: no es una repeticion, es **un arranque de secuencia colocado a
> mitad de lista**, despues de que la lista ya cerro su decision. **Un nodo no
> vuelve a empezar en su paso 7.**

## 4. `gestion_inventario`, costura mas exceso

Visto en los **lotes 5 y 6, puestos 23 y 37**. **Nueve pasos, dos temas pegados:**

| pasos | de que hablan |
|---|---|
| **1 a 5** | **el DIAGNOSTICO de por que se acumula inventario**: dias de inventario, personalizaciones que ofrece ventas, proliferacion de versiones de ingenieria, tiempos de maquina, y no producir por producir |
| **6 a 9** | **la MECANICA de cuanto pedir**: lote optimo entre costo de ordenar y de mantener, inventario de seguridad, estacionalidad, y puntos de reorden |

**Y ademas pisa a dos mundos**: `compras/clasifica_tu_inventario` (puesto 23) y
`quality/inventory_analysis_lean` (puesto 37).

### Nota de alcance, corregida por el ejecutor y aceptada por el auditor

**El solape con `quality/inventory_analysis_lean` es PARCIAL, no casi total.** De
los cuatro elementos del nodo lean, **uno solo esta dentro del nucleo** (los
minimos y maximos por demanda y variacion, que cubren el inventario de seguridad
y los puntos de reorden).

**El mundo lean tiene material propio**: el **flujo de valor** y el **estrategico
contra desperdicio**. Y su **conteo ciclico** es exactitud de registros, mientras
el paso 6 del nucleo es **lote optimo**: son cosas distintas.

> **Cualquier arreglo debe PRESERVAR ese material propio como la profundizacion
> natural del mundo.** Es lo que el nodo de pago tiene de verdad y lo que
> sobrevive a la cirugia.

### Marca adicional

Este caso esta **ademas** marcado como **primer y segundo caso legitimo de la
palanca reservada** (reencuadrar el nodo del **NUCLEO** a version base, clausula
(c) de la doctrina). **PENDIENTE DEL VISTO DEL FUNDADOR.**

> **Dato de grafo verificado, util para la ejecucion**: `gestion_inventario` ya
> declara a `clasifica_tu_inventario` (el nodo de `compras` del puesto 23) en sus
> `nodos_siguientes`. **El puente al mundo ya existe**, asi que un reencuadre a
> base **no deja al lector sin salida**: la escalera esta tendida.

---

## 9. ACRECION SIN TEJER. **CLASE del nucleo**

> **LA CLASE CAMBIA DE NOMBRE Y DE TAMAÑO** al leer el top del instrumento.
> Nacio como *"costuras de pegado doble"*, con dos ejemplares de **dos** bloques.
> El top tiene nodos de **cinco, siete y mas** bloques apilados.
>
> **El defecto no es que algo se pego dos veces: es que las fusiones historicas
> del nucleo APILARON NARRACIONES SIN TEJERLAS.** Cada fuente entro entera,
> detras de la anterior, y nadie escribio la version unica.
>
> **ACRECION SIN TEJER** es el nombre que describe lo que se ve.

### El tamaño, medido

| | |
|---|---:|
| nodos citados por `scripts/costuras_internas.py` | **110** |
| de `core` | **66** |
| de `quality` | **24** |
| resto (`exportacion`, `seguridad_digital`, `health_safety`, `franquicias`, `environmental`) | **20** |

**La señal de bloques marca el corte**, asi que cada cita llega con **donde
mirar**, no solo con que mirar.

---

## LOTE C1: los tres primeros del top, leidos

**Veredicto del auditor: COSTURA CONFIRMADA en los tres.** Las repeticiones que
siguen **se verificaron contra el grafo antes de escribirlas**.

### a) `core/producto_minimo_viable`, 22 pasos: CINCO narraciones del MVP en fila

**Los bloques**: 1 a 5, 6 a 9, 10 a 14, 15 a 18, 19 a 22.

**Y la misma instruccion servida una y otra vez**, con las palabras cambiadas:

| la instruccion | en los pasos |
|---|---|
| *"define el conjunto minimo de caracteristicas a partir de tu vision"* | **6, 15 y 19** |
| *"itera o cambia de rumbo si nadie lo encuentra interesante o suficiente"* | **8, 17 y 22** |
| *"muestra tu primera version solo a los earlyvangelists, no al mercado masivo"* | **7, 12 y 20** |

> **Es el nodo de bandera del catalogo sirviendo la misma instruccion TRES veces,
> tres veces, y tres veces.** Un lector que llegue aqui recibe veintidos pasos
> para aprender lo que caben en cinco.

### b) `core/coeficiente_viral`, 16 pasos: TRES narraciones del calculo de K

| bloque | que es |
|---|---|
| **1 a 5** | la version **simple**: contar usuarios y referidos, porcentaje que se activa, coeficiente, incentivos, monitoreo |
| **6 a 11** | la version **descompuesta**, en **tu**: invitaciones por usuario, conversion, `K = i * conversion`, tiempo de ciclo viral, eslabon mas debil |
| **12 a 16** | **la descompuesta OTRA VEZ**, en **infinitivo**: invitaciones, conversion en clics, clics en registros, `K = invitaciones x click-through x signup`, variable mas debil |

> **DOS CORTES, NO UNO.** Y el tercer bloque **repite al segundo cambiando solo la
> voz**, que es la firma de esta clase: el mismo contenido entro dos veces desde
> dos extracciones distintas.

### c) `core/viral_loop_marketing`, 30 pasos: SIETE bloques apilados

Todo lo que las fuentes dijeron sobre referidos, en fila: mecanismos y coeficiente
(1 a 3), la peticion de referido (4 a 8), los promotores espontaneos (9 a 13), el
programa de referidos (14 a 17), **el mismo programa otra vez en tu** (18 a 21),
las recompensas mas alla del dinero (22 a 25), y los tipos de viralidad (26 a 30).

> **Contra el estandar de 3 a 6 pasos, treinta pasos son CINCO VECES el techo.**
>
> **Eso no es un nodo: es un vertedero ordenado.**

---

## LA CORRELACION CON EL ESTANDAR DE PASOS

**El estandar de `docs/SOP_EXTRACCION_PACKS.md` ya hacia ilegales estos nodos**:
*"pasos_accionables: 3-6 pasos imperativos concretos, hacibles esta semana"*.

**Nadie lo medía.**

| | |
|---|---:|
| activos por encima de 6 pasos | **177** (5,0% del catalogo) |
| de las **110 citas**, cuantas estan fuera del estandar | **72** (65%) |
| de las **106 que disparan por bloque**, cuantas estan fuera | **72** (68%) |
| de los **10 nodos con mas pasos** del catalogo, cuantos cito el instrumento | **10 de 10** |

> **El 5% del catalogo incumple el estandar, pero es el 65% de las citas.** Las dos
> señales miden cosas distintas y apuntan al mismo sitio: **un nodo largo lo es
> casi siempre porque le apilaron narraciones.**

**Consecuencia para la lectura**: el instrumento **ya reporta el conteo de pasos
de cada cita**, y **la cola del auditor se ordena por disparo de bloque y conteo
de pasos JUNTOS**. Ninguna de las dos sola pone arriba lo que mas duele.

---

## EL ARREGLO DE LA CLASE: DESTEJIDO POR REESCRITURA

**Para cuando el fundador dispare. No se ejecuta desde este documento.**

**No es una fusion**: no hay supervivientes que elegir ni alias que escribir.
**Es un solo nodo al que le sobran narraciones.**

| | que se hace |
|---|---|
| **1** | **UNA narracion canonica de 3 a 6 pasos**, la del estandar |
| **2** | **los aportes UNICOS de cada bloque, tejidos dentro**: la descomposicion de K, el tiempo de ciclo viral, los tipos de viralidad, y sus equivalentes en cada nodo |
| **3** | clausula **"quitar no es inventar"**, con **la lista explicita de lo que se quita** |
| **4** | **re-voz** del resultado |
| **5** | **cierre completo de catalogo tocado**: Gate 0, reindex, sync, trinquete con puestos antes y despues |

**Por LOTES, con plan previo por lote**, como la cirugia 2.

> **Lo que hace este arreglo posible sin perder nada**: **las fuentes ya viajan en
> `merged_originals`**. El destejido **no toca la doctrina de fuentes**: quita
> texto repetido, y la autoria de cada absorbido sigue registrada donde siempre.

---

## El registro original de la clase, conservado

> **PASO DE CASO A CLASE en el lote 10.** El puesto 97 destapo **el segundo
> ejemplar**, `nucleo/economia_circular_como_modelo_de_negocio`, con la figura
> identica y en un tema **sin ninguna relacion** con el primero.
>
> **Dos figuras identicas en temas sin relacion no son coincidencia: significan
> que la tanda que pego sin tejer dejo mas huellas.** Y esas **no se cazan
> esperando el tercer golpe de suerte**: se cazan con un instrumento.
>
> **Instrumento construido**: `scripts/costuras_internas.py`, con sus salidas en
> `docs/COSTURAS_INTERNAS.jsonl` y `docs/COSTURAS_INTERNAS_RESUMEN.md`. **Cita,
> no juzga**, como su hermano mayor. **110 nodos citados** de 3.521 activos.

### Los dos ejemplares leidos

**Ninguno de los dos lo destapo su par**: los dos aparecieron **leyendo el nodo
del nucleo mientras se leia otra cosa**.

| ejemplar | pasos | el corte | la marca de voz |
|---|---:|---|---|
| `plan_mejora_procesos` (lote 9, puesto 83) | 15 | **tras el 10** | **fuerte**: 1 a 10 en infinitivo, 11 a 15 en tu |
| `economia_circular_como_modelo_de_negocio` (lote 10, puesto 97) | 9 | **tras el 5** | **debil**: los dos bloques en infinitivo, pero el segundo se dirige al lector (*"tu producto"*) |

**El instrumento acierta los dos cortes**, y los pone en los puestos 24 y 61 de su
cola de 110.

### El primer ejemplar, en detalle

**Quince pasos, y dos secuencias casi identicas pegadas dentro del MISMO nodo:**

| el primer bloque | el segundo, otra vez |
|---|---|
| 8. Definir el **output esperado** antes de disenar los pasos | 11. Define el **resultado final** que el proceso debe producir |
| 9. Establecer **metricas de exito en cada etapa** | 13. Establece **metricas para cada etapa** |
| 10. **Asignar responsabilidad clara** por cada paso | 14. **Asigna responsabilidad clara** por cada paso |

**Los pasos 12 y 15 no tienen pareja**: son anadidos del segundo bloque.

**Y el ejemplo de contratacion aparece dos veces**, en el paso 6 y en el 11.

> **LA MARCA QUE CIERRA EL CASO, verificada y que el conteo no ve**: los pasos **1
> a 10 estan en INFINITIVO** (*Documentar, Identificar, Definir, Establecer,
> Asignar*) y los **11 a 15 estan en TU** (*Define, Diseña, Establece, Asigna,
> Aumenta*).
>
> **La costura se ve en la gramatica.** Son **dos extracciones distintas pegadas**,
> y **ni siquiera hablan igual**.

### Es la mas visible de la campaña, y la de forma distinta

**Los otros ocho casos son varios nodos que deberian ser menos.** Este es **UN
SOLO NODO con el texto duplicado dentro.**

> **Por eso su lectura es de FUSION INTERNA: se DESTEJE, no se depreca.** No hay
> superviviente que elegir ni alias que escribir: **hay un nodo al que le sobran
> pasos, y una decision sobre que voz se queda.**

**Y esa decision no es cosmetica**: el bloque en tu es el que ya habla como la
casa, y el bloque en infinitivo es el que trae el arranque del metodo (documentar
el as-is, limites de control, objetivos to-be). **Quedarse con uno entero
perderia algo; la lectura tiene que tejer, no cortar.**

**PENDIENTE. Sin ejecutar.**

---

# LADO MUNDO, cuatro casos

## 5. `quality`, el metodo COC escrito dos veces

Visto en el **lote 6, puesto 31**. `quality/evaluacion_gestion_riesgos` (6 pasos)
y `quality/plan_de_gestion_de_riesgos` (5 pasos), **los dos del mismo mundo**.

**Pasos casi identicos:**

| el metodo | en `evaluacion_gestion_riesgos` | en `plan_de_gestion_de_riesgos` |
|---|---|---|
| lluvia exhaustiva sin restricciones | paso 1 | pasos 1 y 2 |
| actuar contra no actuar, con efectos secundarios inesperados | paso 2 | paso 3 |
| costo-beneficio de cada opcion | paso 4 | paso 4 |
| acciones concretas, responsables y fechas | paso 5 | paso 5 |

**Lo unico que no se solapa**: `evaluacion_gestion_riesgos` añade el **impacto
sobre la flexibilidad futura del negocio** (paso 3) y la **reevaluacion anual**
(paso 6).

**Pregunta de lectura**: ¿**absorcion con alias**, o hay **un matiz real que los
titulos no muestran**?

> **Dato de grafo verificado**: los dos nodos **no estan conectados** entre si, ni
> por `nodos_previos` ni por `nodos_siguientes`. **Nadie los puso en escalera a
> proposito**, a diferencia del caso 1. Ese es el contraste que hace a este el
> caso **mas maduro para fusion**.

### AÑADIDO EN EL LOTE 8 (puesto 76): la fusion tiene que arreglar el ID

El puesto 76 emparejo a `quality/plan_de_gestion_de_riesgos` contra
`nucleo/plan_gestion_riesgos`. **El veredicto fue falso par funcional** (el metodo
COC no es el plan de gobierno), **pero destapo un problema de nombres que esta
fusion debe resolver de paso.**

**Los TITULOS no son el problema** (similitud 44,6). **Los IDS si son gemelos**:
`plan_de_gestion_de_riesgos` contra `plan_gestion_riesgos`. Y **el parentesico del
titulo del NUCLEO es, letra por letra, el nombre del nodo del MUNDO**: *"Como vas a
manejar los riesgos del proyecto **(Plan de Gestion de Riesgos)**"*.

> **Quien lea ese nombre en el nucleo y lo busque, encuentra el nodo del mundo.**
>
> **Al fusionar el duo COC, el superviviente NO puede conservar el id
> `plan_de_gestion_de_riesgos`.** El renombre entra en la misma operacion, con su
> alias, o el problema sobrevive a la fusion.

## 6. `quality`, EL RACIMO DE AUDITORIA

Abierto en el **lote 7**. **Nodos del mundo `quality` que emparejan contra el
MISMO `nucleo/quality_audit`**, un nodo de cuatro pasos.

**Cada par individual cumple el gradiente.** Ninguno es una violacion. **El
hallazgo es el solape INTERNO del racimo.**

### Los primeros siete leidos, con su puesto (lotes 6 y 7)

| puesto | nodo del mundo | pasos |
|---:|---|---:|
| 16 | `auditoria_calidad` | 4 |
| **33** | `auditoria_de_producto` | 7 |
| 47 | `auditoria_de_producto_2` | 4 |
| 50 | `programa_auditoria_calidad` | 4 |
| 55 | `auditoria_producto` | 4 |
| 56 | `auditoria_negocio` | 5 |
| 58 | `concepto_de_auditoria_de_calidad` | 4 |

> **CORRECCION DE ALCANCE, medida y traida por el ejecutor sin decidirla.** El
> encargo abrio este caso con **seis** miembros y la lista de puestos **16, 47,
> 50, 55, 56, 58**. **Son siete**: falta el **puesto 33**,
> `quality/auditoria_de_producto`, que el propio encargo **nombra en el cuerpo**
> del hallazgo (*"auditoria_de_producto y auditoria_producto son casi el mismo
> nodo"*) pero **omite en la lista**. Verificado contra la cola.

### El solape interno, leido

**a) `auditoria_de_producto` (7 pasos) y `auditoria_producto` (4 pasos): casi el
mismo nodo con casi el mismo nombre.**

> **Precision verificada**: **no es un parecido, es una contencion.** Los cuatro
> pasos del corto viven dentro de los siete del largo: elegir la etapa de
> evaluacion, tomar muestras representativas, y validar que lo auditado sea lo
> que le importa al cliente. **El nodo de cuatro pasos no tiene nada que el de
> siete no tenga**, y el de siete ademas clasifica fallas por gravedad, calcula
> indice por unidad y compara en el tiempo.

**b) `auditoria_calidad` y `programa_auditoria_calidad`: los dos son "el
programa".** Ambos se ocupan de montar la auditoria antes de hacerla (alcance,
criterios, quien audita).

**c) `auditoria_de_producto_2` SI es tema propio** (reinspeccion de decisiones de
inspeccion ya tomadas), **pero carga el sufijo numerico conocido**, que es la
marca de nacimiento de la extraccion por chunks.

> **HALLAZGO ADICIONAL, verificado al leer y traido sin decidirlo**: el solape de
> (b) **no es una pareja, es un trio**. `concepto_de_auditoria_de_calidad`
> comparte **paso por paso** con los otros dos: su *"definir si la auditoria sera
> orientada a cumplimiento, a efectividad o ambas"* es **el paso 1 de
> `programa_auditoria_calidad`**, y su *"seleccionar auditores independientes de
> la actividad evaluada"* es **el paso 2 de `auditoria_calidad`**. **Tres nodos
> reparten cuatro decisiones de montaje.**

### RACIMO COMPLETO: los dieciseis leidos

**El fundador decidio atacar el arbol completo**, y los nueve pares que faltaban
(puestos 63, 66, 98, 105, 106, 160, 176, 228 y 279) se **adelantaron fuera del
orden de la cola**. Sus veredictos estan en la seccion ADELANTO DEL RACIMO DE
AUDITORIA de `docs/GRADIENTE_VEREDICTOS.md`.

> **16 de 16 pares de `nucleo/quality_audit` leidos. Ningun par futuro queda
> pendiente: la fusion puede ejecutarse SIN REABRIRSE.**

### Membresia final, para la lectura de fusion

| grupo | nodos | que se leyo |
|---|---|---|
| **el par de producto** | `auditoria_de_producto` (7 pasos) y `auditoria_producto` (4) | **el largo contiene por completo al corto** |
| **el trio del programa** | `concepto_de_auditoria_de_calidad`, `programa_auditoria_calidad`, `auditoria_calidad` | **tres nodos reparten cuatro decisiones de montaje** |
| **el duo de proceso** | `auditorias_calidad_proceso` y `auditoria_de_proceso` | el checklist y los hallazgos del proceso, **dos veces** |

**Nombrado en el grupo de producto pero FUERA de la fusion**:
`auditoria_de_producto_2`, que es **tema propio** (reinspeccion de decisiones de
inspeccion ya tomadas).

**Fuera del racimo, con tema propio verificado**: `auditoria_negocio`,
`definicion_y_concepto_de_aseguramiento_de_calidad`,
`auditoria_sistema_control_calidad_2`, `ingenieria_calidad`,
`auditoria_presidente` y `funciones_del_departamento_de_calidad`.

### LA CUENTA DE NUEVE, fijada

**Adjudicada con la lectura del ejecutor. El nueve no se borra: se explica.**

| | cuantos | quienes |
|---|---:|---|
| **nodos del MUNDO que entran a lectura de fusion** | **8** | el **par de producto** (`auditoria_de_producto`, `auditoria_producto`) **con `auditoria_de_producto_2` leido aparte** dentro del mismo grupo, el **trio del programa** y el **duo de proceso** |
| **el NOVENO implicado** | **1** | **`nucleo/quality_audit`** |
| **total implicado** | **9** | |

**Por que `quality_audit` cuenta aunque no se funda**: es **la referencia contra la
que se lee todo el racimo**. Los dieciseis pares emparejan **contra el**, y lo que
sobreviva a la fusion **volvera a medirse contra el**. Una lectura de fusion que
lo deje fuera **no sabria contra que altura esta fusionando**.

> **`auditoria_de_producto_2` esta dentro de los ocho porque se LEE con el grupo,
> aunque su veredicto sea tema propio y no se funda.** Esa es la diferencia entre
> **implicado en la lectura** y **absorbido en la fusion**, y conviene no
> mezclarlas al contar.

### Observacion suelta, sin caso abierto

`quality/revision_progreso` (puesto 105) **roza** a
`quality/revision_progreso_breakthrough` (puesto 36). **Una linea, no un caso**:
los dos son revision periodica, pero el segundo la aplica a proyectos de mejora
con costo, inversion y ahorro neto. **Si el racimo se abre alguna vez a una
segunda vuelta, mirarlos juntos cuesta poco.**

## 7. `quality`, EL DUO DE VSM

Abierto en el **lote 8**. **Nace de una revision de veredicto**: el puesto 49 era
una VIOLACION con arreglo por via 2 (re-minado), y el lote 8 **cambio el
diagnostico a FUSION**.

| nodo | pasos | papel |
|---|---:|---|
| `quality/value_stream_mapping` | 4 | **el DEBIL**. Sus cuatro pasos **viven dentro** del fuerte |
| `quality/mapeo_flujo_valor` | 5 | **el FUERTE**. Estado actual con tiempos, VA/NVA de tres niveles, estado futuro y mecanismos de control |
| `quality/value_non_value_added_analysis` | 4 | **ESPECIALIZACION LEGITIMA**: se queda **fuera de la fusion** |

**Los tres comparten fuente**: *Juran's Quality Handbook*. Y el nodo del nucleo
contra el que emparejan, `analisis_flujo_de_valor`, viene de **otro libro**
(*Winning at New Products*), **asi que no hay riesgo de tocar el nucleo aqui.**

## LO QUE EL GRAFO DICE, y es mas de lo que la sospecha esperaba

**Verificado antes de escribirlo, como en el caso 5.**

### a) Los dos hermanos NO estan conectados entre si

`value_stream_mapping` y `mapeo_flujo_valor` **no se declaran** ni en
`nodos_previos` ni en `nodos_siguientes`. **Nadie los puso nunca en escalera.**

**Los dos apuntan al mismo hijo**: los dos declaran
`value_non_value_added_analysis` en sus `nodos_siguientes`, y este declara **a los
dos** en sus `nodos_previos`. **Dos padres separados para un hijo compartido.**

### b) LA FUSION DE ESTE RACIMO YA SE HIZO UNA VEZ, Y DEJO A UNO FUERA

**Este es el hallazgo, y no estaba en la sospecha.**

`mapeo_flujo_valor` **ya es el superviviente de una fusion**:

| absorbido | titulo |
|---|---|
| `mapeo_flujo_valor_2` | *Mapeo de Flujo de Valor (Valor Agregado y No Agregado)* |
| `value_stream_mapping_2` | *Value Stream Mapping (Distinguir Valor de Desperdicio)* |

**Los dos estan en sus `ids_alias` y en sus `merged_originals`, con su fuente.**
Es decir: **`quality` tenia CUATRO nodos de VSM, tres se fundieron en uno, y
`value_stream_mapping` se quedo fuera.**

Y se quedo fuera **sin marca**: no tiene `ids_alias`, no tiene
`merged_originals`. **Nadie decidio conservarlo aparte; simplemente no entro.**

> **Este caso no pregunta si hay que fusionar. Pregunta por que este no entro la
> primera vez.**
>
> Y sugiere una comprobacion que **excede este caso**: si el dedup de los packs
> fusiono por pares de sufijo (`X` con `X_2`), **`value_stream_mapping` quedaria
> fuera por llamarse distinto de `mapeo_flujo_valor`** aunque su `_2` si entrara.
> **Eso seria una CLASE, no un caso.** No se investiga desde aqui.

### RESOLUCION DE LA HIPOTESIS: INVESTIGADA Y CONFIRMADA COMO CLASE

**El auditor la investigo. Es una clase, y `value_stream_mapping` es un miembro,
no una rareza.**

**La consulta**: nodos base **activos**, **sin `ids_alias` ni
`merged_originals`**, cuyo hermano `_2` **fue absorbido por un TERCER nodo**.
**Cuatro huerfanos, los cuatro en `quality`:**

| huerfano | su hermano fue absorbido por |
|---|---|
| `value_stream_mapping` | `mapeo_flujo_valor` |
| `consejos_de_calidad` | `consejo_de_calidad_3` |
| `costo_de_calidad` | `costo_de_calidad_3` |
| `entrenamiento_supervisores` | `entrenamiento_supervisores_calidad` |

**El mecanismo**: el dedup **caso por parentesco de nombre**, y **el hermano que
se llamaba distinto quedo fuera sin decision**. Nadie lo conservo a proposito:
**simplemente no entro.**

### EL CENSO FINAL: SEIS bases huerfanas por NUEVE rutas

**Primero se corrio la consulta fijada al sufijo `_2` y dio cuatro.** El ejecutor
la extendio a `_3` y `_4` y aparecieron dos mas. **El auditor la corrio en su
forma general (`_N`, cualquier sufijo) y confirmo el resultado del ejecutor:**

| consulta | bases | rutas |
|---|---:|---:|
| hermano **`_2`** | 4 | 4 |
| hermano **`_2`, `_3` o `_4`** (extension del ejecutor) | **6** | 6 |
| hermano **`_N`**, **un salto** de alias (general, del auditor) | **6** | 8 |
| hermano **`_N`**, **resolviendo CADENAS** (censo final) | **6** | **9** |

**La novena ruta es una CADENA**: `costo_de_calidad_5` fue absorbido por
`costo_de_calidad_6`, **y el `_6` viajo entero despues a
`costo_de_mala_calidad_copq`** en un segundo salto. **Una consulta de un solo
salto no la ve.**

**Las seis, todas en `quality`.** A los cuatro del caso 8 se suman **tres
CANDIDATOS A LECTURA, sin adjudicar**:

#### a) `costo_de_calidad`: huerfano MULTIPLE

**Sus hermanos emigraron y el base quedo fuera de todas las fusiones.** Ya estaba
en el caso 8 por la ruta `_2`; **la novedad es que su maraña no es simple.**

| miembro | estado | se fue a |
|---|---|---|
| `costo_de_calidad` | **ACTIVO, sin marca** | **se quedo** |
| `costo_de_calidad_2` | deprecado | `costo_de_calidad_3` |
| `costo_de_calidad_3` | **ACTIVO** | **superviviente** |
| `costo_de_calidad_4` | deprecado | `costo_de_calidad_3` |
| `costo_de_calidad_5` | deprecado | `costo_de_calidad_6` |
| `costo_de_calidad_6` | deprecado | `costo_de_mala_calidad_copq` |

> **CENSO FINAL, adjudicado**: **CUADRUPLE huerfano**. Familia de **seis
> miembros**, **cuatro emigrados** (`_2`, `_4`, `_5`, `_6`) **repartidos entre DOS
> supervivientes finales** (`costo_de_calidad_3` y `costo_de_mala_calidad_copq`),
> **y el base quedo fuera de ambas fusiones.**

#### b) `distincion_causas_comunes_especiales`

**Familia de tres: dos vivos y uno emigrado.** El base y su `_2` **siguen los dos
ACTIVOS y sin marca**; el `_3` se fue a **`causas_comunes_vs_especiales`**, un
superviviente **que se llama distinto**. **Es la forma identica al caso 7.**

#### c) `eliminacion_causas_error`

**Familia de cuatro**, y aqui el superviviente **es de la misma familia de
nombre**: `eliminacion_causas_error_4` absorbio al `_3` y **quedo con la
historia**, mientras el base sigue activo **sin marca**.

> **TRES HERMANOS ACTIVOS**: el base, el `_2` y el `_4`, **y solo el `_4` lleva
> historia.** De cuatro hermanos sobre el mismo tema, **tres siguen ofreciendose y
> nada los relaciona.**

> ## PRIMERO EN LA COLA DE LECTURA DEL CASO 8 AMPLIADO
>
> **Es el unico de los tres donde la maraña esta VIVA EN LA OFERTA**, no solo en
> el registro. Los demas son huecos de historia: se leen cuando toque. **Aqui hay
> tres nodos que un lector puede recibir hoy, sobre el mismo tema, sin que nada
> le diga que son parientes.**

### LAS DOS MARAÑAS, LEIDAS (lote 9)

**Se leyeron con los puestos 81 a 85, fuera de cola.** `costo_de_calidad` sigue
sin leer.

#### EL TRIO ECR: LEIDO Y ADJUDICADO, pendiente solo del disparo del fundador

**Los tres vivos son el mismo concepto**: el **paso 11 de Crosby**.

| nodo | pasos | quien es |
|---|---:|---|
| `eliminacion_causas_error` | 4 | **el base, corporativo**: *"asignar grupos funcionales responsables"*, voz en infinitivo, y **"Paso 11" en el titulo** |
| `eliminacion_causas_error_2` | 6 | voz de tu, y **el sorteo semanal** como incentivo (paso 6). **Tambien lleva "Paso 11" en el titulo** |
| `eliminacion_causas_error_4` | 6 | **curado a la voz del taller** (*"quien te ayuda"*), titulo sin numero de paso, **y el unico con historia** (`ids_alias`) |

> **VEREDICTO DE LECTURA: FUSION DOBLE hacia `eliminacion_causas_error_4`**, con
> **alias de los dos absorbidos**.
>
> **Los titulos con numero de paso se curan solos en la fusion**: los dos que lo
> llevan son los dos que se absorben. **El colateral C2 se cierra en parte por
> esta via.**

**PENDIENTE DEL DISPARO DEL FUNDADOR. No se ejecuta desde este documento.**

#### LA MARAÑA DE CAUSAS COMUNES: mitad clara y mitad fina

**La mitad clara**: `distincion_causas_comunes_especiales_2` **cabe en el
superviviente** `causas_comunes_vs_especiales`, que trae el metodo completo (datos
en orden cronologico, grafico con limites, reglas de deteccion, investigar la
senal, listar las causas comunes y actuar distinto segun el tipo). **FUSION
CLARA.**

> **Precision verificada al leer los dos, y la traigo porque la fusion tendra que
> decidirlo**: lo unico del `_2` que el superviviente **no dice como tal** es su
> **aviso en forma de prohibicion**, *"evita investigar cada caso como si fuera
> una causa especial cuando el proceso es estable"*. El superviviente **manda
> investigar la senal** y **manda asumir las causas comunes**, pero **no advierte
> del error de perseguir cada caso**. **La lectura decide si ese aviso sobrevive
> como paso.**

**La mitad fina**: el **BASE** es otra cosa. Sus cuatro pasos son **angulo de
gestion de personas**: no informar defectos individuales con el proceso en
control, **ayudar** al trabajador ante una causa especial, y **no sancionarlo por
fallas del sistema**.

> **Es Deming aplicado a DIRIGIR GENTE, no a leer una carta de control.**

**DUDOSO, con la lectura anotada**: **sobrevive con titulo diferenciado**, o **se
funde**. **Lo decide la fusion fina con el fundador.**

> ## EL CRUCE DEL PUESTO 86 CIERRA EL DUDOSO
>
> **Lo que hacia dudoso al base era su angulo de personas. Ese angulo ya tiene
> casa, y mejor.**
>
> `quality/politica_no_culpar_trabajador` hace lo mismo **con metodo**: analiza la
> **distribucion de errores entre todas las personas usando limites de control**,
> identifica a quien excede el limite superior **como posible causa especial e
> investiga el contexto antes de actuar**, y **disena respuestas diferenciadas
> segun lo que muestren los datos**. El base solo dice *"no sancionar"*.
>
> **LA LECTURA DEL AUDITOR PASA DE DUDOSO A FUSION CON REPARTO:**
>
> | que parte del base | a donde va |
> |---|---|
> | el contenido de **proceso** (carta de control, causa comun contra especial) | `causas_comunes_vs_especiales` |
> | el contenido de **personas** (no sancionar, ayudar al trabajador) | `politica_no_culpar_trabajador` |
>
> > **El base queda sin territorio propio.** No es que se parezca a dos nodos: es
> > que **sus dos mitades ya viven mejor en dos sitios distintos.**
>
> **Decision final del fundador, como todas.**

> **Dato de rebote que pesa en esa decision**: ese base **ya figura como DUDOSO en
> `docs/INVENTARIO_ESCALA.md`**, y por la misma razon exacta (*"el analisis
> estadistico central es solitario, pero los pasos sobre trabajadores asumen que
> hay empleados"*). **Las dos lecturas, hechas por separado y con criterios
> distintos, señalan el mismo nodo por el mismo motivo.**

---

### LA LECCION DEL DETECTOR

**Confesada por el auditor, y vale mas que el hallazgo:**

> **La consulta que cazaba un dedup ciego al parentesco de nombre estaba ella
> misma fijada al sufijo `_2`. El detector del punto ciego heredo el punto
> ciego**, y la frase *"no hay quinta victima"* era falsa.

### Y la SEGUNDA CAPA, confesada tambien por el auditor

**La consulta general arreglo el sufijo pero heredo otra ceguera**: **resolvia UN
SOLO SALTO de alias**, y **la ruta en cadena le era invisible**.

> **Y las cadenas no son una hipotesis: el propio catalogo las declara.**
> `resolverId` en `web/lib/engine/graph.ts` **camina cadenas** precisamente porque
> existen. **Hay ocho** de mas de un salto en el catalogo, y una de ellas es
> justo la novena ruta de esta clase.

**Dos ejemplares del mismo patron, con el mismo remedio.**

### FORMULACION FINAL DE LA REGLA

> **Toda consulta que caza una ceguera se revisa contra ESA MISMA CEGUERA y
> contra LAS ESTRUCTURAS QUE EL CATALOGO YA DECLARO**: sufijos de cualquier
> profundidad, cadenas de cualquier largo.

**La segunda mitad es la que importa**: la casa **ya tenia escrito** que las
cadenas existen, en el codigo que las camina. **La consulta no lo leyo.**

**Credito de las dos cazas**: el ejecutor.

---

### EL LIMITE DE LA CLASE, declarado para que no se vuelva a acotar en falso

**Incluso la consulta general esta atada a FAMILIAS DE NOMBRE.**

**Un huerfano cuyo gemelo se llame distinto desde el origen es INVISIBLE para
ella.** Si dos extracciones del mismo capitulo nacieron con nombres sin parentesco
y una se fundio, **ninguna consulta de sufijo lo vera jamas.**

Ese residuo **solo se caza con semantica**, y **es la misma pregunta mundo contra
mundo** anotada en el tablero de `docs/audits/AUD-08-Gradiente_Nucleo_Mundo.md`.

| clase | estado |
|---|---|
| huerfanos por **familia de sufijo** | **CERRADA**: seis bases, nueve rutas, todas en `quality` |
| huerfanos por **nombre libre** | **NO MEDIDA**, y declarada como tal |

---

## 8. `quality`, LOS TRES HUERFANOS RESTANTES

**Hermanos del caso 7, misma clase, mismo mecanismo.** Leidos por el auditor
contra sus supervivientes. **Cada uno va a lectura de fusion propia, con la
valvula como ultima palabra.**

### a) `consejos_de_calidad` contra `consejo_de_calidad_3`

| | quien es |
|---|---|
| **el huerfano** (5 pasos) | **el intercambio ENTRE talleres**: un espacio con otras personas que evaluan calidad **en su propio negocio**, con agenda propia, participacion abierta, y el intercambio entre sucursales. **Es el paso 13 de Crosby re-vozado** |
| **el superviviente** (4 pasos) | **el consejo INTERNO de areas**: representantes de las distintas areas de mejora, periodicidad, e **institucionalizarlo como estructura permanente** |

> **Parientes, no gemelos.** Uno mira hacia afuera y el otro hacia adentro. **La
> lectura puede terminar en dos nodos con frontera clara, o en fusion.**

### b) `costo_de_calidad` contra `costo_de_calidad_3`

| | quien es |
|---|---|
| **el huerfano** (5 pasos) | **marco financiero mensual**: revision mensual con numeros financieros y operativos juntos, comparados contra lo presupuestado, con dueno por desviacion |
| **el superviviente** (6 pasos) | **el calculo como porcentaje de ventas**, con el desglose por componente, la comparacion contra un estandar de referencia, y **meta de reduccion progresiva** |

> **El solape mas gordo de los tres.** Los dos calculan el costo de la calidad y
> los dos lo vuelven recurrente.

### c) `entrenamiento_supervisores` contra `entrenamiento_supervisores_calidad`

| | quien es |
|---|---|
| **el huerfano** (3 pasos) | **la version taller**: una conversacion clara, comprobar que cada quien pueda explicarlo con sus palabras, y alinear antes de lanzar |
| **el superviviente** (6 pasos) | **el programa completo**: seis horas de estudio, manual de referencia, **test de comprension**, dudas individuales y refuerzo por area |

> **Posible relacion base-profundo DENTRO del mismo mundo**, que es una figura que
> el gradiente no cubre (mide nucleo contra mundo, no mundo contra mundo). **Si la
> lectura la confirma, no se funden: se encadenan.**

---

# CITAS INTRA-DOMINIO ADELANTADAS

**No son casos. Son la cola inicial del barrido intra-dominio** que el fundador
decidio hacer (ver el tablero de `docs/audits/AUD-08-Gradiente_Nucleo_Mundo.md`).

> **La lectura del gradiente las REGALA sin costo**: aparecen mientras se lee otra
> cosa, y guardarlas es gratis. **Aqui se acumulan SIN ADJUDICAR**, para que
> cuando el barrido arranque no empiece de cero.

## a) `quality`, el par de KPI

`sistema_medicion_kpi` (puestos **15** y **84**) y `medicion_kpi` (puesto **114**).

## b) `quality`, el racimo Deming de responsabilidad

`politica_no_culpar_trabajador` (puesto **86**),
`responsabilidad_gerencial_causas_comunes` (puesto **113**), y el **base** de
`distincion_causas_comunes_especiales`.

> **Ojo con este**: la **fusion con reparto del base ya esta adjudicada** (ver la
> maraña de causas comunes), y **puede absorber parte de este racimo antes de que
> el barrido llegue**. Conviene mirarlos juntos, no en dos momentos.

## c) `risk_management`, el trio de actualizacion de la lista

`el_riesgo_cambia_con_el_tiempo` (puesto **107**) contra los **dos reencuadrados
de la cirugia 1**, `manten_viva_tu_lista_de_riesgos` y
`revisa_tus_riesgos_con_un_ritmo`.

> **Este merece cuidado especial**: los dos contra los que roza **acaban de ser
> reescritos**, y el veredicto del puesto 59 confirmo que **el reencuadre les dio
> momento propio**. Leer esto como sub-fusion sin tener eso presente seria
> deshacer una cirugia que la propia cola valido.

---

# VERIFICACIONES DE FAMILIA (lote 11)

**Pedidas por el auditor, hechas contra el grafo. Se reporta lo que hay, sin
adjudicar.**

## `desarrollar_caracteristicas_proceso`: FORMA NUEVA, ni huerfano ni fusion

| nodo | estado | dominio | pasos | alias | merged |
|---|---|---|---:|---|---:|
| `desarrollar_caracteristicas_proceso` | **ACTIVO** | quality | 4 | ninguno | 0 |
| `desarrollar_caracteristicas_proceso_2` | **ACTIVO** | quality | 6 | ninguno | 0 |

**No hay mas variantes de la familia.**

> **NO ES LA CLASE DE LOS HUERFANOS DEL DEDUP.** Alli el hermano **habia sido
> absorbido por un tercero** y el base se quedaba fuera. **Aqui no paso NADA**: los
> dos siguen vivos, ninguno lleva marca, y **el dedup sencillamente nunca miro esta
> familia.**

**Leidos, son el mismo tema a dos voces y dos profundidades**: el base *"Desarrollar
las Caracteristicas del Proceso"* en **cuatro pasos y en infinitivo** (listar,
evaluar, seleccionar, establecer); el `_2` *"Como disenar el proceso para crear y
entregar tu producto"* en **seis pasos y en tu**, con las condiciones de operacion
reales del usuario y los diagramas de flujo.

> **Es la misma figura del trio ECR**: **una version curada viviendo al lado de su
> hermana sin curar, y ninguna de las dos marcada.**

### La forma, medida en todo el catalogo

**36 parejas** de `base` mas `_N` con **los dos ACTIVOS y NINGUNO con marca**
(ni `ids_alias`, ni `merged_originals`, ni ser alias de nadie):

| dominio | parejas |
|---|---:|
| quality | **25** |
| health_safety | 6 |
| environmental | 3 |
| core | 1 |
| franquicias | 1 |

> **Traido como medicion, no como caso.** Una pareja de sufijo viva **no prueba
> duplicado**: `auditoria_de_producto` y su `_2` estan en esta lista y **ya se
> leyeron como temas propios** en el racimo de auditoria. **Lo que la lista dice es
> donde nadie ha mirado, no donde hay defecto.**

## `trilogia`: FALSA FAMILIA, el parentesco es de apellido

| nodo | estado | pasos | que es de verdad |
|---|---|---:|---|
| `trilogia_de_juran` | **ACTIVO**, con 3 absorbidos | 6 | **la trilogia**: planificar, controlar, mejorar, con esporadico contra cronico |
| `juran_trilogy` | **DEPRECADO**, con archivo | 4 | absorbido por el anterior |
| `trilogia_de_juran_2`, `_3` | **sin archivo**, solo alias | | absorbidos; son **dos de los 27 registros sin archivo** |
| `trilogia_juran_qa_qc` | **ACTIVO**, sin marca | 3 | **la diferencia entre QC y QA**. Su titulo **ni menciona la trilogia** |
| `benchmarking_trilogia_juran` | **ACTIVO**, sin marca | 4 | **benchmarking** alimentando el diseno y la mejora |

> **La sospecha del auditor se confirma leyendo: el parentesco es SOLO DE NOMBRE.**
>
> `trilogia_juran_qa_qc` se titula *"La diferencia entre vigilar la calidad y
> asegurarla"* y sus tres pasos separan el dia a dia de la revision del sistema.
> **No es la trilogia: es otra cosa que comparte apellido.**
>
> `benchmarking_trilogia_juran` es **benchmarking**, y usa la trilogia como destino
> de sus hallazgos. **Tampoco es el mismo nodo.**

**NADA que fusionar aqui.** Lo unico que deja la lectura es **una nota de voz**:
`benchmarking_trilogia_juran` esta **en infinitivo** (*Utilizar, Aplicar,
Incorporar, Usar*), y **al barrido residual va**.

> **Vale la pena escribir la moraleja**: la familia de sufijo dio un hallazgo real
> (36 parejas sin mirar) **y la familia de apellido dio cero**. **El nombre
> compartido no es señal, y conviene no volver a tratarlo como si lo fuera.**

---

# CASOS COLATERALES DE VOZ Y VALVULA

**No son sub-fusion.** Son nodos que la lectura del gradiente encontro rotos por
otra razon y que **no tienen donde ir**. Se registran aqui para que no se pierdan.

## C1. `quality/auditoria_calidad_proveedores`: el titulo miente

Encontrado en el **adelanto del racimo, puesto 160**. **Fuera del racimo y fuera
del gradiente.**

| | |
|---|---|
| **el titulo promete** | auditoria en **recepcion y aceptacion de proveedores** |
| **los pasos entregan** | el **protocolo de visita de un auditor corporativo**: reunirse con el gerente de calidad, reunirse con el gerente general, obtener autorizacion de otros departamentos, distribuir el informe desde la planta auditada |

**Tres defectos a la vez**: **titulo que miente**, **pasos en voz de manual**, y
**la valvula en contra** (nada de eso lo hace el lector del taller esta semana).

**Arreglo probable, y lo decide la lectura**: **reencuadre a la escala del
lector**, o **marca corporativa con reescritura**. **PENDIENTE DE ADJUDICACION.**

> **Dato verificado que ahorra la mitad del trabajo**: el nodo **ya esta
> clasificado CORPORATIVO por la condicion (c)** en `docs/INVENTARIO_ESCALA.md`,
> **con la misma cita**. Lo unico nuevo que aporta el gradiente es **el titulo que
> miente**.

> **Y el contraste que enseña como se arregla**:
> `quality/funciones_del_departamento_de_calidad` (puesto 279) **tenia el mismo
> riesgo de origen** (su titulo dice *departamento*) **y esta resuelto bien**: sus
> pasos hablan de *"alguien capacitado que no sea quien fabrica el producto"*.
> **El camino ya existe en el propio mundo.**

## C2. El numero de paso del libro, cableado en el titulo

Encontrado en el **caso 8**. **Dos titulos llevan el numero de paso de Crosby:**

| nodo | titulo |
|---|---|
| `quality/consejos_de_calidad` | **Paso 13**: Consejos de Calidad |
| `quality/costo_de_calidad_3` | **Paso 4**: Costo de la Calidad |
| `quality/eliminacion_causas_error` | **Paso 11**: Eliminacion de Causas de Error |
| `quality/eliminacion_causas_error_2` | Eliminacion de Causas de Error - ECR (**Paso 11**) |

**Los dos ultimos entraron con la lectura del trio ECR (lote 9), y son los dos que
esa fusion absorbe**: ahi el titulo se cura sin trabajo extra.

**Es la secuencia del libro filtrandose al catalogo como si el usuario lo
estuviera leyendo.** Un titulo que **presupone un orden que la app no muestra**:
nadie que abra la app ve un paso 1, ni sabe que hay catorce.

**No es dato caducado ni voz corporativa: es una referencia a un indice que el
lector no tiene.**

> **Se arregla en la misma lectura de fusion de cada caso, no antes.** Los dos
> nodos ya estan citados a esa lectura, y un titulo que va a cambiar de dueno no
> se toca dos veces.

## C3. AUTO-ALIAS Y ALIAS CON DOS DUEÑOS. **LIMPIADO en `0e5e0c6`**

**Hallazgo del cotejo del "ocho".** No es sub-fusion: es **metadata sucia**, y
salio de que dos cuentas no coincidian.

> **CERRADO el 9 ago 2026 en `0e5e0c6`.** Lo que sigue **se conserva en pasado**,
> porque la clase y su leccion valen mas que el arreglo.

### Como se destapo

**La cifra del ejecutor era CORRECTA: ocho cadenas reales** de mas de un salto,
es decir alias cuyo dueño esta a su vez deprecado.

**La cuenta inicial del auditor (17) estaba contaminada**: su caminador contaba
como cadena los **bucles de auto-alias**, que no llevan a ninguna parte.

### Lo que hay en el dato

**OCHO nodos llevan su propio id dentro de su `ids_alias`**: siete activos
(`trilogia_de_juran`, `concepto_variacion_estadistica`,
`distribucion_normal_probabilidad`, `inspeccion_automatizada`,
`plan_control_peligros`, `deteccion_temprana_regulatoria`,
`recomendaciones_smart`) **mas `jerarquia_controles`, que esta deprecado.**

**El patron es comun y se lee solo**: el auto-alias aparece **junto al `_2`
absorbido**. Es la **huella de una tanda de fusion que escribio la familia
completa incluyendo al sobreviviente**, en vez de solo a los absorbidos.

### UN alias con DOS dueños

**`jerarquia_controles`** esta reclamado por **su propio nodo deprecado** (via
auto-alias) **y por `prevencion_control_peligros`**, que es su absorbedor real.

> **La resolucion dependia del ORDEN de construccion del mapa. Averia silenciosa
> en potencia.**

**Medido entonces**: ganaba `prevencion_control_peligros`, que es **el correcto**,
por estar en el **indice 2877** del master contra el **2217** del nodo deprecado.
**Ganaba por orden, no por regla, y un dato que esta bien de suerte es un dato que
esta mal.**

**AHORA gana porque es el UNICO que lo reclama.**

### TERCERA aparicion de la leccion del detector

Van tres formas del mismo tropiezo: **el sufijo fijo**, **el salto unico**, y
ahora **el dato sucio que inflaba la cuenta**.

> ## FORMA FINAL DE LA REGLA
>
> **Toda consulta que caza una ceguera se revisa contra TRES cosas: su propia
> ceguera, las estructuras que el catalogo ya declaro, y la posibilidad de que el
> DATO MISMO este sucio.**

### La limpieza, HECHA en `0e5e0c6`

**Se hizo como higiene, no como incendio**, y el reporte de los resolutores es lo
que permitio tratarla asi: **ningun resolutor de la casa se colgaba**. Los dos que
caminan cadenas **filtran el auto-alias al construir el mapa Y llevan guarda de
ciclo**, dos defensas independientes.

**Alcance**: el propio id fuera del `ids_alias` de los ocho. Todo lo demas
intacto, **por edicion de linea y no por re-serializado**, porque los archivos
estan en CRLF y volcarlos habria reescrito cada linea y enterrado el cambio real.

**Verificacion sobre los dos masters recompilados** (el del dataset y el de la
web):

| consulta | resultado |
|---|---:|
| nodos con auto-alias | **0** |
| alias con dos dueños | **0** |
| **cadenas de mas de un salto** | **8**, las mismas |

**Las ocho cadenas se conservan porque son HISTORIA y no se tocan.** Cierre:
Gate 0 OK, sync hecho, **sin reindex** (ningun texto ni id activo cambio),
trinquete **42/1/0 sin deriva** y **las cinco anclas inmoviles**.

> **Lo que NO se toco, y conviene saberlo**: los ocho nodos viven **tambien en sus
> packs** (`quality`, `health_safety`, `environmental`), y **ahi la huella sigue**.
> Son la entrada pre-integracion, y limpiarlos es otra decision. **Re-integrar un
> pack re-sembraria el defecto.**

### EL CIERRE COMPLETO: las tres capas

**La limpieza del catalogo era solo la primera.** Un defecto que se limpia sin
cerrar su origen vuelve.

#### 1. Las SEMILLAS de los packs, limpiadas

Los ocho nodos vivian **tambien** en `packs/quality`, `packs/health_safety` y
`packs/environmental`, con la misma huella. **Ocho archivos, ocho lineas, mismo
metodo de linea.** Los packs son **entrada, no catalogo**: sin Gate, sin reindex,
sin rumbos. **Re-integrar un pack ya no re-siembra el defecto.**

#### 2. La BARANDA en el Gate 0, tres chequeos nuevos

| chequeo | que impide |
|---|---|
| **auto-alias** | ningun nodo lleva su propio id en su `ids_alias` |
| **alias con dos duenos** | ninguna cadena es reclamada por dos nodos |
| **gemelos del master** | el master del dataset y el de la web **no pueden divergir en contenido de nodos** |

**El tercero nacio de este mismo trabajo**: la divergencia de **71
`etiqueta_arbol`** vivio en HEAD sin que nadie la viera **porque ningun guardian
comparaba los dos artefactos**. Cada copia era valida por su cuenta.

**Fixtures de los dos lados** en `engine/test_gate_alias.py`: uno que viola cada
regla, uno limpio que pasa las tres, uno que prueba que se comparan **campos y no
bytes**, y una pasada sobre el catalogo real.

#### 3. El ESCRITOR, cazado con su linea

**`scripts/hseq/_renombrar_cosmetico.py`**, en el bucle de renombre.

> **El mecanismo**: el nodo llega con **la BASE ya en su `ids_alias`** (la absorbio
> en el dedup) **y acto seguido se guarda CON ESE MISMO NOMBRE**. La entrada vieja
> se vuelve un alias a si mismo. **No fue una tanda descuidada: fue el renombre
> cosmetico.**
>
> **La prueba**: su tabla `RENOMBRES` tiene **exactamente los ocho**.

**El filtro se aplico ahi y en los otros cuatro puntos de escritura de
`ids_alias`** (`paso1_ascii`, `consolidar_pack`, `paso2_dedup`, `tejer_ola1`),
porque **una regla escrita en un solo sitio falla en el que alguien olvido**. Un
test de contrato custodia los cinco.

---

# FICHA DORMIDA: los 27 REGISTROS SIN ARCHIVO

**Medicion del ejecutor, reproducida por el auditor.** No es sub-fusion ni voz:
es un hueco de historia que nadie habia medido.

**27 exactos de las 349 entradas de `merged_originals`** del catalogo apuntan a
ids que **ya no tienen archivo propio en ninguna parte del repositorio**. Entre
ellas, `consejos_de_calidad_2`, del caso 8.

| que sobrevive | que no |
|---|---|
| **el registro**: id, titulo y **fuente** | **el TEXTO** del absorbido |

> **La union de fuentes esta a salvo**, que es lo que la doctrina de las fuentes
> necesita. **Lo que no se puede consultar es que decia.** Los otros 322 si
> conservan su archivo deprecado entero.

**Hipotesis inocente, sin investigar**: absorciones ocurridas **dentro del pack
antes de integrarlo**, de modo que **solo el superviviente viajo al master**.

> **Se investiga cuando alguna lectura de fusion necesite consultar que decia un
> absorbido de esa lista. No antes.**

---

# RELACION CON EL GRADIENTE

**Estos casos NO son violaciones de gradiente.** Son **deuda estructural del
catalogo** que el instrumento ilumino **de rebote**.

Su arreglo es **independiente de la cola de pares** y usa la **doctrina de fusion
de siempre**:

- **fusion primero, voz despues**;
- **la valvula manda**;
- **nada se borra.**

---

# ORDEN PROPUESTO DE EJECUCION, cuando el fundador de el visto

| # | caso | por que va aqui |
|---|---|---|
| **1.º** | **caso 5**, `quality` COC | dos nodos, un solo mundo, **lectura corta** |
| **2.º** | **casos 3 y 4**, las costuras | **un solo nodo cada uno**: se abre, se parte o se recorta, y se cierra |
| **3.º** | **caso 2**, brainstorming | **requiere decidir el reparto** entre nodos que sobreviven |
| **4.º** | **caso 7**, el duo de VSM | **dos nodos y una especializacion que no se toca**, pero antes hay que entender **por que el debil no entro en la fusion anterior** |
| **5.º** | **caso 8**, los huerfanos | **el trio ECR ya esta LEIDO Y ADJUDICADO** (fusion doble); quedan la mitad fina de causas comunes y `costo_de_calidad`, sin leer |
| **6.º** | **caso 9**, `plan_mejora_procesos` | **forma distinta**: no se elige superviviente, se **desteje** un solo nodo. Puede ir en cualquier momento, no depende de los demas |
| **7.º** | **caso 6**, el racimo de auditoria | **el mas grande**, pero ya **RACIMO COMPLETO**: 16 de 16 leidos, membresia cerrada en tres grupos. **Se puede ejecutar sin reabrirse** |

**El caso 1 salio del orden: esta CERRADO y no se ejecuta.**

**El caso 4 puede ejecutarse junto con el reencuadre a base de
`gestion_inventario`** si el fundador aprueba esa palanca: **es el mismo nodo
abierto una sola vez.**
