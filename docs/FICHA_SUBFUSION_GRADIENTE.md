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

# LADO NUCLEO, cuatro casos con nombre

Estos cuatro **corrigen la cuenta sin nombre** que quedo en el marcador del lote 5
de `docs/GRADIENTE_VEREDICTOS.md`.

**Estado: el caso 1 esta CERRADO** (no se funden, ver su razon). **Los casos 2, 3
y 4 siguen abiertos.**

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

# LADO MUNDO, dos casos

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
> caso **mas maduro para fusion** de los cinco.

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
| **4.º** | **caso 6**, el racimo de auditoria | **el mas grande**, pero ya **RACIMO COMPLETO**: 16 de 16 leidos, membresia cerrada en tres grupos. **Se puede ejecutar sin reabrirse** |

**El caso 1 salio del orden: esta CERRADO y no se ejecuta.**

**El caso 4 puede ejecutarse junto con el reencuadre a base de
`gestion_inventario`** si el fundador aprueba esa palanca: **es el mismo nodo
abierto una sola vez.**
