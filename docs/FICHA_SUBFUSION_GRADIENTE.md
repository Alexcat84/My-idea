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

### PERO LA CLASE NO ESTA ACOTADA EN CUATRO, y esto lo trae el ejecutor

**Reproduje la consulta y da los cuatro exactos.** Y despues la **corri otra vez
extendiendo el sufijo**, porque el catalogo tiene familias que llegan a `_3` y
`_4`:

| consulta | huerfanos |
|---|---:|
| hermano **`_2`** (la que se corrio) | **4** |
| hermano **`_2`, `_3` o `_4`** | **6** |

**Los dos que aparecen al extenderla:**

| candidato | su hermano | absorbido por | ¿misma forma? |
|---|---|---|---|
| `distincion_causas_comunes_especiales` | `_3` | **`causas_comunes_vs_especiales`** | **SI, identica**: el superviviente **se llama distinto** |
| `eliminacion_causas_error` | `_3` | `eliminacion_causas_error_4` | **NO**: el superviviente **es de la misma familia de nombre** |

> **`distincion_causas_comunes_especiales` es el quinto huerfano, y es la misma
> forma exacta que `value_stream_mapping`.** Su `_2` sigue activo (por eso la
> consulta de `_2` no lo vio) y su `_3` se fue a un nodo con otro nombre.
>
> **La ironia vale la pena escribirla**: la consulta que cazaba un dedup ciego al
> sufijo **estaba ella misma fijada al sufijo `_2`.**
>
> **No lo doy por adjudicado**: el quinto y el sexto **quedan como candidatos a la
> espera del auditor**, y por eso **no entran al caso 8**. Lo que si queda dicho es
> que **la frase "no hay quinta victima" no se sostiene con la medicion.**

### Observacion medida de rebote, fuera de alcance

**27 de las 349 entradas de `merged_originals` del catalogo apuntan a ids que ya
no tienen archivo propio** en ningun sitio del repositorio (entre ellas
`consejos_calidad` y `consejos_de_calidad_2`, absorbidos por
`consejo_de_calidad_3`).

De esos 27 **sobrevive el registro** (id, titulo y fuente), que es lo que la
doctrina de las fuentes necesita, **pero no su contenido**. Los otros 322 si
conservan su archivo deprecado entero.

> **No se investiga desde aqui**, y puede tener explicacion (absorciones ocurridas
> **dentro del pack antes de integrarlo**, de modo que solo el superviviente
> viajo al master). **Queda anotado porque nadie lo habia medido.**

### c) Por que la especializacion se queda

`value_non_value_added_analysis` **no repite** a ninguno de los dos: toma **un
paso** (la clasificacion VA/NVA) y le pone **la pregunta que la hace operable**
(*"¿el cliente pagaria por esto?"*). **Es profundizacion, no duplicado**, y
sobrevive a la fusion **con sus dos aristas de entrada reducidas a una.**

**Lectura de fusion PENDIENTE. La valvula de pasos accionables, como siempre,
tiene la ultima palabra.**

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

**Es la secuencia del libro filtrandose al catalogo como si el usuario lo
estuviera leyendo.** Un titulo que **presupone un orden que la app no muestra**:
nadie que abra la app ve un paso 1, ni sabe que hay catorce.

**No es dato caducado ni voz corporativa: es una referencia a un indice que el
lector no tiene.**

> **Se arregla en la misma lectura de fusion de cada caso, no antes.** Los dos
> nodos ya estan citados a esa lectura, y un titulo que va a cambiar de dueno no
> se toca dos veces.

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
| **5.º** | **caso 8**, los tres huerfanos restantes | **tres lecturas independientes**, una por par, y la (c) puede terminar en encadenar en vez de fundir |
| **6.º** | **caso 6**, el racimo de auditoria | **el mas grande**, pero ya **RACIMO COMPLETO**: 16 de 16 leidos, membresia cerrada en tres grupos. **Se puede ejecutar sin reabrirse** |

**El caso 1 salio del orden: esta CERRADO y no se ejecuta.**

**El caso 4 puede ejecutarse junto con el reencuadre a base de
`gestion_inventario`** si el fundador aprueba esa palanca: **es el mismo nodo
abierto una sola vez.**
