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

## LOTE C2: cinco confirmaciones nuevas

**Veredicto del auditor: COSTURA CONFIRMADA en las cinco.** Repeticiones
verificadas contra el grafo antes de escribirlas.

### 1. `core/decision_de_vender_startup`, 34 pasos: EL PEOR NODO MEDIDO DEL CATALOGO

**Pareja 79,2 y bloque 69,3. Unas seis narraciones apiladas.**

**Seis parejas duplicadas a simple vista, las seis verificadas:**

| la instruccion, dicha dos veces | pasos |
|---|---|
| define un precio minimo firme basado en el valor real | **14 y 18** |
| comunica ese precio con firmeza a todos los compradores | **15 y 19** |
| corre un proceso corto de sondeo de M&A | **8 y 26** |
| compara la oferta contra tu proyeccion a 3 o 5 anos | **9 y 25** |
| ajusta tu salario de CEO a valores de mercado | **27 y 32** |
| separa la decision de tu situacion financiera personal | **30 y 33** |

> **Y hay mas de las seis citadas**: *"pregunta a tu equipo si esta dispuesto a
> seguir"* aparece en **11, 13 y 17**, y **evaluar el mercado real** en **16, 22 y
> 24**. **Treinta y cuatro pasos para vender una empresa, y el nodo se repite a si
> mismo al menos ocho veces.**

### 2. `core/lienzo_modelo_negocio`, 17 pasos: CUATRO narraciones del Canvas

| bloque | como completa los nueve bloques |
|---|---|
| **1 a 4** | **con post-its**, en grande, iterando en grupo |
| **5 a 8** | **para la solucion disenada**: socios, canales, costos e ingresos |
| **9 a 12** | **con el equipo y publicacion**: imprimir para cada miembro, reunirse, pausar donde falte, publicar en la pared |
| **13 a 17** | **bloque por bloque**: segmentos, propuesta, canales, recursos, costos |

**El literal *"completar cada uno de los 9 bloques"* esta en los pasos 2 y 5.**

> **Nodo insignia, como el MVP del C1.**

### 3. `core/ab_testing_optimizacion`, 15 pasos: TRES narraciones

**Corte en el 10.** Landing page (1 a 5), metrica unica (6 a 10), canal nucleo
(11 a 15).

> **Y el tercer bloque esta en TU** (*Define, Disena, Mide, Itera, Documenta*)
> mientras los dos primeros van en infinitivo. **La misma firma de siempre.**

### 4. `core/transicion_producto_a_experiencia`, 12 pasos: COSTURA DOBLE

**Corte en el 7**, y dos instrucciones dichas dos veces:

| | pasos |
|---|---|
| *"tu producto podria transformarse en un modelo de acceso o servicio"* | **5 y 9** |
| *"identificar barreras de adopcion"* (confianza, disponibilidad, propiedad contra renta) | **6 y 10** |

### 5. `quality/planificacion_recoleccion_datos`, 16 pasos: COSTURA LEVE

**Corte en el 11**, pero la figura es mas simple: **los cuatro primeros pasos son
un RESUMEN** (objetivos, que medir, como medir, recolectar) **pegado delante del
metodo completo** que empieza en el 5 y llega hasta el 16.

> **Destejido facil**: no hay que elegir entre narraciones, **hay que quitar un
> indice que se colo como pasos.**

### 6. `nucleo/plan_mejora_procesos`

**Ya confirmado como calibracion. Sin cambio.**

## LOTE C3: dos confirmadas, cuatro citas falsas, y dos clases de veredicto nuevas

**Es el primer lote que trae CITAS FALSAS, y por eso es el que mas enseña sobre el
instrumento.** Cada anatomia verificada contra el grafo.

### CONFIRMADAS

#### 1. `core/key_partners_hypothesis`, 14 pasos, corte 9: TRIPLE

| bloque | de que fuente viene |
|---|---|
| **1 a 5** | **el Canvas**: listar socios, que provee cada uno, flexibilidad de proveedores, y **actualizar el Business Model Canvas** |
| **6 a 10** | **el libro de traccion**: objetivo de traccion y metricas, tipo de partnership, evaluar por capacidad de mover la metrica, negociar alineado con el **Critical Path** |
| **11 a 14** | **alianzas por cuello de botella**: que alianza resuelve tu cuello de botella, licensing, distribucion, supply |

> **Tres fuentes, cero tejido.**

#### 2. `core/split_testing_experimentos_ab`, 9 pasos, corte 6: DOBLE

**El A/B de producto** (1 a 5: hipotesis, dividir en A y B, lanzar solo a B, medir,
comparar) y **la narracion de grupo de control** (6 a 9: seleccionar control con
desempeno similar, medir en el mismo periodo, comparar cambio porcentual, reportar
diferencia neta).

> **CITA INTRA-DOMINIO DEL NUCLEO, y es de las que ahorran trabajo**: el nucleo
> tiene **DOS nodos de A/B testing**, este y `ab_testing_optimizacion` (confirmado
> en el C2, con tres narraciones). **Los dos con costura.**
>
> **Su destejido probablemente converge en uno**, asi que **en la pasada unica se
> leen JUNTOS.** Registrado tambien en las citas intra-dominio.

### CITAS FALSAS, y las dos clases nuevas que las nombran

#### LARGO LEGITIMO

**Supera el estandar de 3 a 6 pasos, pero NO hay narracion repetida dentro.**

| nodo | pasos | bloque | corte | que es |
|---|---:|---:|---:|---|
| `quality/principios_medicion_efectiva` | 10 | 51,9 | 6 | **la lista canonica de diez principios**, cada uno distinto |
| `quality/seleccion_representante_extranjero` | 9 | **50,9** | **5** | **checklist de nueve criterios distintos** para evaluar a un candidato: tamano de la fuerza de ventas, historial de cinco anos, territorio, compatibilidad de lineas, instalaciones, politicas de compensacion, perfil de clientes, cuantos principales representa, enfoque promocional. **Ninguno repite a otro.** |
| `quality/fmea_analisis_de_modos_de_falla` | 8 | 51,4 | 4 | **el metodo FMEA canonico en secuencia unica**: hoja de nueve columnas, modos, causas, efectos, frecuencia por severidad por detectabilidad, RPN, acciones, validar |

> **Su arreglo NO es destejido: es una decision de ESTANDAR**, y le toca a la
> pasada unica. Un metodo canonico de ocho pasos **no se puede partir sin
> romperlo**, y la pregunta honesta es si el estandar admite excepciones nombradas.

> **Con la tercera, la clase queda caracterizada** y ya no es una bolsa de casos
> sueltos: **es la clase de los FORMATOS LISTA que el estandar de 3 a 6 pasos no
> contempla.** Una lista canonica de principios, un metodo canonico en secuencia
> unica y un checklist de criterios de evaluacion **no son narraciones apiladas: son
> formatos donde el numero de pasos lo fija el contenido, no el autor.**
>
> **Y tienen firma medible**: los tres pasan de ocho pasos (10, 9 y 8) y sus cortes
> de bloque son **6, 5 y 4**, o sea la evidencia mas ancha que el instrumento
> produce. **El largo legitimo se parece al doble por arriba y se distingue por
> abajo**: mucho material, cero repeticion.
>
> **Lo que le toca decidir a la pasada unica ya no es caso por caso**: es si el
> estandar admite una excepcion nombrada para los formatos lista, y con que
> criterio se reconoce uno.

> **Verificado contra el grafo antes de registrar**: `seleccion_representante_extranjero`
> existe en `exportacion`, tiene exactamente **nueve pasos**, y su pareja disparada
> (3 contra 7) son *"analizar el territorio actual cubierto"* contra *"analizar el
> perfil de clientes actuales"*, **dos criterios distintos que comparten el verbo**.

#### FALSO POSITIVO DE SECUENCIA LEGITIMA

**Pasos tematicamente ESPEJADOS que la señal de bloque roza sin que haya narracion
repetida.**

| nodo | pasos | bloque | corte | el espejo |
|---|---:|---:|---:|---|
| `core/founder_ceo_succession_process` | 8 | 51,5 | 5 | paso 2 *"evalua si TUS habilidades encajan con la siguiente etapa"* contra paso 6 *"evalua si el perfil de QUIEN TE SUCEDERIA encaja con la etapa"* |
| `franquicias/mix_ubicaciones_corporativas_franquicia` | 6 | 51,4 | **3** | secuencia unica de decision, sin espejo ni repeticion |
| `core/plan_gestion_riesgos` | 6 | **50,3** | **3** | pasos **5 y 6**: *"define que tan probable y que tan grave puede ser cada riesgo"* y *"decide tu propia forma de comparar que riesgos son mas probables o mas graves"*. **Son los dos vecinos legitimos del PMI**: primero se definen las escalas, despues el metodo para comparar con ellas. **Uno no puede existir sin el otro.** |

> **Mismo verbo y misma estructura, sujeto distinto.** Es exactamente lo que engana
> a un emparejador monotono, y **no es un defecto: es como se escribe una sucesion.**

> **Nota del ejecutor sobre el segundo**: `mix_ubicaciones_corporativas_franquicia`
> tiene **seis pasos**, o sea **esta DENTRO del estandar**. Su bloque se evaluo con
> **tres contra tres**, que es el minimo que el instrumento admite y **la evidencia
> mas delgada que puede producir**. **Los nodos cortos dan la señal de bloque mas
> ruidosa**, y conviene saberlo al leer la parte baja de la cola.

> **Con el tercero, esa nota deja de ser una observacion suelta y se vuelve el
> retrato de la clase.** `plan_gestion_riesgos` tambien tiene **seis pasos** y
> tambien se evaluo **tres contra tres**. **Los dos falsos positivos que estan
> DENTRO del estandar son los dos que el instrumento juzgo con la evidencia mas
> delgada que sabe producir.**
>
> **La regla practica que sale de ahi**: cuando la cita tenga **corte 3**, la señal
> de bloque no alcanza por si sola y hay que mirar los pasos. El tercero de la
> clase la confirma dos veces seguidas.

> **Verificado contra el grafo antes de registrar**: `plan_gestion_riesgos` existe
> en `core`, tiene exactamente **seis pasos**, y los pasos 5 y 6 son literalmente
> los que el instrumento emparejo. **La cita entro por bloque (50,3 sobre el umbral
> de 44), no por pareja**: su 61,9 de pareja esta muy por debajo del umbral de 80.
> **Es una cita de bloque, y el bloque es de tres contra tres.**

## CONFIRMADA DE REBOTE desde el gradiente (lote 13)

### `core/ratios_eficiencia_inventario`, 8 pasos: DOBLE

**El puesto 4 del top del instrumento**, confirmado **sin leer la cola**: salio en
el puesto **154** del gradiente, leyendo otra cosa.

| bloque | de que habla |
|---|---|
| **1 a 4** | DII, **rotacion**, comparar con competidores, liberar efectivo atado |
| **5 a 8** | **la rotacion OTRA VEZ**, retorno sobre ventas, ciclo de conversion de efectivo, cuentas por cobrar y pagar |

**El literal**: paso 2 *"calcular COGS anual dividido entre inventario promedio
para obtener **rotacion**"* contra paso 5 *"calcular la **rotacion** de inventario
actual de la empresa"*.

> **Es la TERCERA vez que una costura aparece de rebote leyendo el gradiente**,
> despues de `plan_mejora_procesos` y `economia_circular`. **El instrumento no fue
> una idea: fue la respuesta a un patron que ya se estaba repitiendo.**

### `core/propuesta_gasto_capital`, 12 pasos: DOBLE, y el PRIMER FALSO NEGATIVO

**La cuarta confirmada de rebote** (lote 15, puesto 189). **Dos narraciones del
mismo analisis de gasto de capital:**

| bloque | de que habla |
|---|---|
| **1 a 5** | **la generica**: costos, beneficios, **NPV** con hurdle rate, payback e IRR, **redactar la propuesta** |
| **6 a 12** | **la de sabor IT**: hardware y software por trimestre, beneficios directos, incrementales, de evitacion e intangibles, flujo trimestral con **VPN**, y **presentar el analisis** |

**Duplicados verificados**: el valor presente en el paso **3** (*NPV*) y en el
**11** (*VPN*); la propuesta **redactada** en el 5 y **presentada** en el 12.

> ## ESTE NODO NO ESTA EN LA COLA DEL INSTRUMENTO
>
> **Es el primer falso negativo medido, y quedo fuera por 0,9 puntos**: bloque
> **44,1** contra el umbral **45**.
>
> **Y lo que lo hace instructivo es que el instrumento SI vio la costura**: su
> corte propuesto es **tras el paso 5**, exactamente donde la lectura la encontro.
> **Lo que fallo no fue la señal: fue el umbral.**

### Por que se le escapo: la parafrasis con vocabulario distinto

| los dos pasos duplicados | similitud |
|---|---:|
| *"Calcular NPV usando el hurdle rate"* contra *"calcular el flujo de caja neto trimestral y el valor presente neto (VPN)"* | **46,2** |
| *"Redactar la propuesta"* contra *"Presentar el analisis a los ejecutivos"* | **50,6** |

> **Es la parafrasis un escalon mas alla de lo que el C3 ya habia visto: no es que
> cambie la cola de la frase, es que la SIGLA esta en dos idiomas.** `NPV` y `VPN`
> son la misma cosa y **para un comparador de tokens no se parecen en nada.**

### El costo de recuperarlo, medido y sin adjudicar

**Bajar el umbral de bloque de 45 a 44 recupera este nodo**, y cuesta:

| umbral de bloque | nodos que entran por esa señal |
|---:|---:|
| 46 | 82 |
| **45** (el actual) | **106** |
| **44** | **124** |
| 43 | 142 |

> **Dieciocho citas mas para recuperar una costura confirmada**, y
> `propuesta_gasto_capital` entra **penultimo** de esas dieciocho.

### ADJUDICADO: el umbral baja a 44

**El auditor lo adjudico con el mandato del fundador como argumento**: *dieciocho
citas mas es barato, y hay un falso negativo conocido viviendo en esa franja.*

| | antes | ahora |
|---|---:|---:|
| umbral de bloque | 45 | **44** |
| **citas en la cola** | 110 | **128** |
| citas nuevas | | **18** |

> **Nota de cifra, para que nadie la lea mal**: el **124** que se midio era el
> conteo **por señal de bloque**. **La cola es la UNION de las dos señales**, y
> lleva ademas **4 citas que entran solo por la señal de pareja**. De ahi 128.
> **Las dieciocho nuevas, que es lo que se adjudico, son exactas.**

**Las 18 van marcadas como `franja_44_45` en la salida y agrupadas en su propia
seccion del resumen**, para que la lectura las encuentre juntas y no repartidas
por la cola.

### Y EL LIMITE, que este cambio NO cierra

**Bajar el umbral recupera a ESE falso negativo. No cierra el mecanismo que lo
produjo.**

> **Un comparador de tokens no ve equivalencias semanticas a ningun umbral.**
> `NPV` y `VPN` son la misma cosa y para este instrumento se parecen un **46,2**.
> **No hay numero que arregle eso.**

**Las tres redes que quedan debajo** estan escritas en
`docs/COSTURAS_INTERNAS_RESUMEN.md`: los **rebotes del gradiente** (que ya cazaron
cuatro costuras sin buscarlas), el **barrido semantico intra-dominio** del final
(donde los embeddings si ven que NPV y VPN viven juntos), y **la pasada unica**,
que relee entero cada nodo antes de destejerlo.

> **El limite queda declarado, no tapado. Ninguna cola sustituye a leer el nodo.**

## CONFIRMADAS DE REBOTE, quinta y sexta (lote 17)

**Las dos YA estaban citadas en la cola.** No son falsos negativos: **son citas que
el gradiente leyo antes de que les tocara su turno.**

### `core/voz_del_cliente_voc`, 10 pasos: DOBLE de la observacion

**En la cola con pareja 57,1 y bloque 50,2.**

| bloque | de que habla |
|---|---|
| **1 a 5** | preparate para observar, **observa en su entorno**, complementa la entrevista, usa lo observado desde el inicio, manten contacto |
| **6 a 10** | **observa una vez al mes**, ponte en su lugar, atiende los detalles pequenos, anota y revisa, busca patrones |

**El duplicado literal**: paso **2** contra paso **6**, los dos mandando observar
al cliente en su contexto real. **La segunda tanda repite el ciclo entero.**

> **Nota honesta sobre el instrumento**: su corte propuesto fue **tras el paso 4**,
> y la lectura pone la frontera **tras el 5**. **Se quedo a un paso.** En los cinco
> casos anteriores habia acertado el corte exacto; **aqui lo aproxima.** Sigue
> siendo util (el corte orienta), pero **no es una coordenada, es una pista.**

### `core/future_scenarios_planning`, 13 pasos: CUATRO bloques

**En la cola con pareja 53,7 y bloque 50,1.**

| bloque | de que habla |
|---|---|
| **1 a 3** | el generico: drivers, matriz, narrar escenarios |
| **4 a 5** | el del **Canvas**: workshop y preguntas por bloque |
| **6 a 9** | **IA, tanda 1**: lineal contra exponencial, contingencia, revision trimestral |
| **10 a 13** | **IA, tanda 2**: definir escenarios de IA, evaluar impacto, senales de alerta, revision periodica |

> **Las dos tandas de IA se repiten ENTRE SI**: las dos definen escenarios, evaluan
> el impacto en el modelo de negocio y mandan revisar con periodicidad.
>
> **Es el primer ejemplar con CUATRO bloques de tres fuentes distintas**, y el
> primero donde **la repeticion no es entre el bloque viejo y el nuevo, sino entre
> dos bloques NUEVOS del mismo tema.**

---

## MARCADOR DE LA CLASE

| | |
|---|---:|
| **CITAS del instrumento leidas** | **22** de **128** |
| de esas, costura **confirmada** | **16** |
| de esas, **citas falsas** | **6** |
| **precision de la cola** | **73%** |
| **costuras confirmadas que la cola NO citaba** | **0** |
| **TOTAL de costuras confirmadas** | **16** |

> **DISCREPANCIA RESUELTA: el auditor elige la segunda lectura.** El marcador
> anterior contaba 21 leidas, 15 confirmadas y una decimosexta aparte, en una
> fila de *confirmadas que la cola NO citaba*. **Esa fila baja a cero y su
> ejemplar entra a la cola.**
>
> **La razon:** tras la regeneracion `propuesta_gasto_capital` **si esta citado**
> (bloque 44,1). La categoria *fuera de cola* **describe la historia, no el
> presente**, y la historia ya tiene su sitio propio en esta ficha: el apartado
> **`core/propuesta_gasto_capital`, 12 pasos: DOBLE, y el PRIMER FALSO NEGATIVO**,
> con **El costo de recuperarlo, medido y sin adjudicar** a continuacion. Ahi
> queda contado lo que de verdad importa de ese caso, que es **que el umbral 44
> existe porque este nodo se escapo**. En el marcador no hace falta una fila para
> recordarlo.
>
> **Las dos lecturas siempre dieron el mismo TOTAL de 16.** Lo unico que cambia es
> donde se cuenta el decimosexto, y ahora se cuenta donde esta: dentro.

### DOCTRINA DEL MARCADOR: los totales se recomputan del archivo

**Registrada aqui porque este marcador ya se descuadro dos veces por la misma
causa.**

> **Los totales del marcador se recomputan SIEMPRE del archivo. El auditor dicta
> el delta, nunca el total.**

Un total dictado de memoria no se puede verificar contra nada: llega como cifra
y se copia como cifra. Un delta si (*esta cita salio falsa*, *esta se confirmo*),
porque el total sale despues de contar, y contar es reproducible. **Las dos veces
que este marcador no cerro fue por sumar deltas sobre un total recordado en vez
de recontar.**

La cuenta de esta entrada salio de cruzar los veredictos escritos en esta ficha
con `docs/COSTURAS_INTERNAS.jsonl`, cita por cita: **22 leidas, 16 confirmadas,
6 falsas, y cada una en exactamente una fila de la tabla de franjas de abajo.**

**De las 22 citas leidas, buena parte llego por el gradiente y no por orden de
cola**: los dos calibradores, `ratios_eficiencia_inventario`,
`propuesta_gasto_capital` y el hermano del caso 7. **La lectura de la clase no ha
avanzado sola: la ha empujado el otro frente.**

> **Nota de la recomputacion, para no inventar**: la version anterior de esta
> linea decia *7 de 19 llegaron por el gradiente* y enumeraba cinco. El total de
> leidas si se recomputa del archivo; **la procedencia de cada cita no esta
> registrada por cita en ningun sitio**, asi que el 7 no lo puedo reconstruir ni
> lo repito como cifra. Queda la enumeracion, que si esta verificada.

> **El denominador si cambio con la regeneracion de la cola.** Las **18 nuevas**
> entraron como **PENDIENTES**, no como leidas: suman al denominador (110 a 128)
> y nada mas. La unica que ademas movio el numerador fue
> `propuesta_gasto_capital`, que ya estaba confirmada y **ahora ademas esta
> citada**, que es exactamente lo que esta entrada viene a asentar.

**Las seis falsas se reparten en dos clases**: LARGO LEGITIMO (3) y FALSO POSITIVO
DE SECUENCIA LEGITIMA (3). **Las dos clases quedaron empatadas y las dos quedaron
caracterizadas**, cada una con su firma medible: la primera son formatos lista de
ocho pasos o mas con cortes anchos; la segunda tiene sus dos miembros de seis pasos
juzgados con corte 3.

### LA FRANJA, medida, y la lectura NO es la que parecia

**El dato que se propuso**: *las cuatro falsas viven entre 51 y 52 de señal de
bloque; por encima de 52, doce de doce confirmadas.*

**La primera mitad es exacta.** La segunda no cuadra, y la diferencia cambia lo que
se puede hacer con ella:

**La tabla esta RECONCILIADA: cada una de las 22 citas leidas vive en
exactamente una fila, y las filas suman 22 clavado.**

| franja de señal de bloque | confirmadas | falsas | leidas |
|---|---:|---:|---:|
| **por encima de 52,0** | **9** | **0** | 9 |
| **entre 51,0 y 52,0** | **2** | **4** | 6 |
| **por debajo de 51,0** | **5** | **2** | **7** |
| **sin señal de bloque** (solo pareja) | 0 | 0 | **0** |
| | **16** | **6** | **22** |

**Las 22, con su fila y su veredicto**, recontadas cruzando los veredictos de
esta ficha con `docs/COSTURAS_INTERNAS.jsonl`:

| fila | cita | bloque | veredicto |
|---|---|---:|:--:|
| por encima de 52,0 | `producto_minimo_viable` | 80,2 | confirmada |
| por encima de 52,0 | `coeficiente_viral` | 74,7 | confirmada |
| por encima de 52,0 | `decision_de_vender_startup` | 69,3 | confirmada |
| por encima de 52,0 | `viral_loop_marketing` | 65,9 | confirmada |
| por encima de 52,0 | `transicion_producto_a_experiencia` | 60,1 | confirmada |
| por encima de 52,0 | `lienzo_modelo_negocio` | 59,2 | confirmada |
| por encima de 52,0 | `plan_mejora_procesos` | 56,7 | confirmada |
| por encima de 52,0 | `ab_testing_optimizacion` | 52,6 | confirmada |
| por encima de 52,0 | `planificacion_recoleccion_datos` | 52,3 | confirmada |
| entre 51,0 y 52,0 | `principios_medicion_efectiva` | 51,9 | **falsa** |
| entre 51,0 y 52,0 | `key_partners_hypothesis` | 51,7 | confirmada |
| entre 51,0 y 52,0 | `split_testing_experimentos_ab` | 51,5 | confirmada |
| entre 51,0 y 52,0 | `founder_ceo_succession_process` | 51,5 | **falsa** |
| entre 51,0 y 52,0 | `mix_ubicaciones_corporativas_franquicia` | 51,4 | **falsa** |
| entre 51,0 y 52,0 | `fmea_analisis_de_modos_de_falla` | 51,4 | **falsa** |
| por debajo de 51,0 | `seleccion_representante_extranjero` | 50,9 | **falsa** |
| por debajo de 51,0 | `plan_gestion_riesgos` | 50,3 | **falsa** |
| por debajo de 51,0 | `voz_del_cliente_voc` | 50,2 | confirmada |
| por debajo de 51,0 | `future_scenarios_planning` | 50,1 | confirmada |
| por debajo de 51,0 | `economia_circular_como_modelo_de_negocio` | 49,7 | confirmada |
| por debajo de 51,0 | `ratios_eficiencia_inventario` | 48,3 | confirmada |
| por debajo de 51,0 | `propuesta_gasto_capital` | 44,1 | confirmada |

> **Las dos nuevas cayeron las dos en la fila de abajo**:
> `seleccion_representante_extranjero` con **50,9** y `plan_gestion_riesgos` con
> **50,3**, y **las dos salieron falsas.**
>
> **La nota de contabilidad que estaba abierta queda CERRADA.** Las filas sumaban
> 19 contra 21 leidas por dos motivos, los dos identificados al recontar:
> **`voz_del_cliente_voc` (50,2) y `future_scenarios_planning` (50,1), las dos
> confirmadas de rebote del lote 17, nunca se habian metido en ninguna fila.** Y
> el vigesimo segundo es `propuesta_gasto_capital` (44,1), que entra con la
> decision del auditor de arriba. Las tres van a la fila de abajo, y las tres son
> confirmadas: por eso esa fila pasa de **2 y 2** a **5 confirmadas y 2 falsas**.
>
> **La fila de las citas sin señal de bloque queda creada y en cero.** El
> instrumento tiene **cuatro** citas que disparan solo por pareja (bloque 0,0) y
> **ninguna esta leida todavia**. La fila existe para que la primera que se lea
> tenga sitio y no vuelva a caerse de la cuenta.

**Por encima de 52 son NUEVE de nueve.** Y ahora que la cuenta esta completa, el
reparto de las **16 confirmadas** es: **9 por encima de 52 y SIETE por debajo**
(`key_partners` 51,7, `split_testing` 51,5, `voz_del_cliente_voc` 50,2,
`future_scenarios_planning` 50,1, `economia_circular` 49,7,
`ratios_eficiencia_inventario` 48,3 y `propuesta_gasto_capital` 44,1).

> **Esto es una correccion de fondo, no de forma.** La version anterior decia
> *tres de ellas viven por debajo de 52*, sobre un total de doce confirmadas. Con
> la tabla cuadrada son **siete de dieciseis**: **casi la mitad de todas las
> costuras confirmadas del catalogo viven por debajo de la franja**, es decir en
> el terreno donde la señal de bloque es debil. **Es el argumento mas fuerte que
> hay contra acelerar la lectura ahi abajo**, y estaba escondido en el descuadre.

> **LA FRANJA 51 a 52 NO ES UN PISO DE FALSOS: ES UNA ZONA MEZCLADA**, con dos
> confirmadas y cuatro falsas. Y **por debajo de 51 viven CINCO costuras
> confirmadas**, que con la tabla cuadrada son la mayoria de esa fila:
> `voz_del_cliente_voc` (50,2) y `future_scenarios_planning` (50,1), las dos
> confirmadas de rebote del lote 17; `economia_circular` (49,7), que es uno de los
> dos calibradores del instrumento; `ratios_eficiencia_inventario` (48,3),
> confirmada de rebote en el lote 13; y `propuesta_gasto_capital` (44,1), el
> primer falso negativo, que es la razon de que el umbral sea 44 y no mas alto.

> **Y el segundo trae ademas la prueba de que las dos señales se ganan el
> sueldo**: `ratios_eficiencia_inventario` tiene **bloque 48,3** (de los mas bajos
> de la cola) **y pareja 85,1** (de los mas altos). **La señal que casi lo deja
> fuera es la que la otra compenso.** Quitar una de las dos habria costado esta
> costura.

### Consecuencia para el paso de lectura, y va en sentido contrario

**Por encima de 52 la señal es limpia y ahi si se puede leer rapido. Pero eso son
solo NUEVE de las 128 citas** (cifras recontadas del instrumento tras la
regeneracion; la version anterior decia 13 de 110, sobre la cola vieja).

> **119 de las 128 viven por debajo de 52**, es decir **en la zona mezclada o mas
> abajo**, donde la muestra leida da **7 confirmadas contra 6 falsas**: una moneda
> al aire, no un piso de ruido.
>
> **Acelerar ahi seria pasar de largo justamente donde esta casi toda la cola, y
> donde ya se sabe que hay costuras reales.** El compromiso de leer la cola entera
> no cambia, **y el paso tampoco deberia aflojarse por debajo de la franja.**

### La prediccion de la zona mezclada se sigue cumpliendo

**Las dos citas nuevas son la comprobacion, y salio la que se esperaba**: las dos
viven **por debajo de bloque 52** (50,9 y 50,3) y **las dos resultaron falsas.**

> **Bajo 52 la señal de bloque no se sostiene sola.** La muestra leida en esa
> mitad de la cola queda, con la tabla ya cuadrada, en **7 confirmadas contra 6
> falsas**. Ni piso de ruido ni terreno donde se pueda leer de corrido: una
> moneda al aire, y con casi la mitad del tesoro dentro.
>
> **Correccion, y va en la direccion que menos convenia.** Esta subseccion decia
> que la muestra pasaba de *3 contra 4* a *3 contra 6*, con lo que la mitad de
> abajo parecia irse volviendo esteril y el argumento se apoyaba en resistir la
> tentacion de acelerar. **Al reconciliar la tabla aparecieron tres confirmadas
> que nunca se habian contado en ninguna fila** (`voz_del_cliente_voc`,
> `future_scenarios_planning` y `propuesta_gasto_capital`), **las tres por debajo
> de 51**. El reparto real nunca fue 3 contra 6.
>
> **Lo que si se cumplio de la prediccion**: las dos citas nuevas viven bajo 52
> (50,9 y 50,3) y **las dos salieron falsas**, que es lo que se esperaba de esa
> banda.
>
> **Y la consecuencia operativa no solo no cambia: se refuerza.** **El paso de
> lectura NO se acelera**, y ahora por un motivo mejor que la prudencia: **siete
> de las dieciseis costuras confirmadas del catalogo estan ahi abajo.** No es una
> zona que haya que peinar por disciplina, es donde esta casi la mitad de lo que
> se busca. Cada cita se sigue leyendo entera contra el grafo: las dos de esta
> entrada **parecian costura por su bloque y ninguna lo era**, y eso solo se supo
> abriendo los pasos.

### Nota de orden: la zona 51 a 52 esta cosechada entera

**De los seis puestos siguientes de la cola, cuatro ya estaban leidos bajo sus ids
completos**: `key_partners_hypothesis`, `split_testing_experimentos_ab`,
`mix_ubicaciones_corporativas_franquicia` y `fmea_analisis_de_modos_de_falla`.

> **Comprobado contra el instrumento**: la banda de bloque **51,0 a 52,0 tiene
> exactamente SEIS citas** en `docs/COSTURAS_INTERNAS.jsonl`, y **las seis estan
> leidas y registradas en esta ficha**: `principios_medicion_efectiva` (51,9),
> `key_partners_hypothesis` (51,7), `founder_ceo_succession_process` (51,5),
> `split_testing_experimentos_ab` (51,5), `mix_ubicaciones_corporativas_franquicia`
> (51,4) y `fmea_analisis_de_modos_de_falla` (51,4).
>
> **La zona mezclada no queda a medias: queda cerrada**, con su reparto final de
> **dos confirmadas contra cuatro falsas**. Lo que sigue por leer vive todo **por
> debajo de 51**, que es justo donde la evidencia es mas delgada y donde ya hay dos
> costuras reales esperando.

---

## EL PATRON DE CENTRALIDAD

**La acrecion golpea PROPORCIONAL A LA CENTRALIDAD.**

Los nodos mas acrecionados son los **insignia**: el MVP, el Canvas, vender la
empresa, el A/B testing, el coeficiente viral. **Y no es casualidad**: son **los
que todas las fuentes tocan**, y por tanto **los que mas fusiones recibieron**.
Cada libro traia su version, y cada version entro entera detras de la anterior.

> **Los nodos que mas se sirven al usuario son los peores servidos.**

> **Y el contrario tambien existe, para no leer el patron como una condena**:
> `nucleo/decision_intensidad_capital` lleva **NUEVE especializaciones sanas** de
> `franquicias` (puestos 22, 79, 82, 136, 146, 188, 236, 286 y 293) **sin una sola costura ni
> pisada**. **Un nodo base muy citado NO tiene por que acabar acrecionado**: el
> defecto es de como se fusiono, no de cuanto se usa.

> **Y el hub ha seguido sumando en la otra cola, sin una sola mala.** El cribado
> de la franja le emparejo **CATORCE especializaciones mas** (trece D y una C con
> hallazgo lateral, ninguna A y ninguna B), y la ultima la trajo la muestra D:
> **F1096, `franquicias/mito_control_calidad_corporativo`**, otra pareja sana.
> **Son dos colas distintas y por eso no se suman en una sola cifra**: nueve en
> la cola de 346 y catorce en la franja. **Veintitres emparejamientos contra el
> mismo nodo base y ni uno solo problematico.**

**Consecuencia para la mesa del fundador**, y es la que cambia el orden de las
prioridades:

> **La primera tanda de destejidos, el top-10, toca MAS EXPERIENCIA DE USUARIO
> REAL que cualquier otra cirugia pendiente.** Un lector que pide su MVP, su
> Canvas o su prueba A/B recibe hoy veintidos, diecisiete o quince pasos donde
> caben cinco. **No es deuda de catalogo: es lo que la gente lee.**

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

### ECO DE LA ADJUDICACION DE LA FRANJA: la clase tapa al pago

**Viene del cribado de la franja bajo el umbral** (`docs/FRANJA_INFORME.md`,
seccion 9). El detalle completo esta alli; aqui queda lo que le toca a esta
clase, que es mucho.

**El cribado leyo 1.606 pares y encontro exactamente DOS violaciones de la
vara. Las dos son sombras de DOS nodos de esta clase:**

| franja | el nodo del mundo (de pago) | el nodo del nucleo (gratis) |
|---:|---|---|
| **15** | `quality/breakthrough_desempeno_actual`, 5 pasos | **`plan_mejora_procesos`**, 15 pasos, tres bloques apilados |
| **124** | `environmental/eco_efectividad`, 3 pasos | **`economia_circular_como_modelo_de_negocio`**, 9 pasos, dos bloques apilados |

Son **los dos ejemplares con nombre de esta ficha**: el primero y el segundo,
los mismos que hicieron pasar el hallazgo de caso a clase.

> **La frase de la adjudicacion, y es un cargo nuevo contra la clase:** *las
> violaciones de la franja no son enfermedad nueva, son la acrecion del gratis
> tapando al pago.*
>
> El nodo del nucleo no gana la comparacion porque sepa mas: **gana porque
> abulta**. Llega a la mesa con quince pasos contra cinco, o nueve contra tres,
> y son la misma doctrina contada dos o tres veces. **La vara del gradiente
> estaba midiendo una costura y llamandola profundidad.**

**Consecuencia practica para el arreglo de arriba: la cura es ACOPLADA, y las
dos manos van en la pasada unica.**

1. **Destejer el costurado del nucleo** con la tabla de cinco pasos de arriba,
   sin cambiarle nada. Reduce la sombra sin quitarle una sola decision al
   lector.
2. **Profundizar el nodo del mundo con su propio libro**, que es **el patron de
   la cirugia 1**: ni copiarle al nucleo ni recortarle al nucleo, sino darle al
   nodo de pago la voz y el metodo de su propia fuente.

**Las dos juntas o ninguna.** Destejer solo el nucleo deja el par igual de plano
por el otro lado; profundizar solo el mundo deja la costura viva.

**Las 6 dudosas del cribado quedaron OK las seis**, sin ninguna accion de vara.
La unica que deja tarea es `quality/optimizacion_de_procesos` (franja 28), flaco
y autorreferente: **candidato a engorde, no caso de vara.**

**Y la validacion del cribado esta CERRADA**: el auditor sorteo la muestra del 5%
de las D (61 pares, semilla `81febf5c`, procedimiento fijado, reproducido y
pineado al commit del sorteo) y la leyo entera en tres tandas de 20, 21 y 20.
**Sesenta y uno de sesenta y uno se sostienen en la vara: cero violaciones y cero
dudosos escondidos.** **Veredicto: CRIBADO VALIDADO**, y el metodo de tres piezas
que lo consiguio queda registrado en el informe como metodo reutilizable de la
casa.

**Lo que la muestra si ha movido son figuras, no la vara**, y en tres entradas:

1. **Tanda 1, F303**: una **FRONTERA CANDIDATA** nueva, registrada mas abajo en
   esta ficha. Hueco de la lista de figuras del encargo, no error del cribado.
2. **Tanda 2, F822**: **el primer C-como-D**, y el unico veredicto corregido en
   41 pares. La figura de *numero de paso en el titulo* estaba en la lista y se
   habia aplicado a los *Paso N* de Crosby pero **nunca a los *Punto N* de los
   catorce puntos de Deming**: son **siete nodos de `quality`** con el numero
   puesto en el titulo (puntos 5, 6, 7, 8, 10, 13 y 14). Censo entero en
   `docs/FRANJA_INFORME.md`, apartado 10.1.
3. **Tanda 2, F947**: una candidatura a par calcado transdominio que **el texto
   completo desarmo**. Ver la nota de los cinturones aqui abajo.

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

### EL PRIMER MIEMBRO CONCRETO, y lo dio el ultimo lote de la cola

**`quality/descubrir_necesidades_cliente` (3 pasos) y
`quality/descubrir_necesidades_del_cliente` (6 pasos).** Puesto **320**.

| | |
|---|---|
| titulos | *Descubrir las Necesidades del Cliente* contra *Descubrimiento de las Necesidades del Cliente* |
| fuente | **la misma**, Juran |
| estado | **los dos activos, ninguno con marca, NO conectados** |
| contenido | el de 3 pasos es **la version comprimida**; el de 6 es **el metodo completo** (planificar metodos, recopilar en el lenguaje del cliente, distinguir declaradas de reales de percibidas de culturales, usos no previstos, priorizar, traducir a lenguaje tecnico) |

> **Sus nombres se diferencian en UNA PALABRA, y esa palabra basta para que ninguna
> consulta de sufijo los vea**: ni la de `_2`, ni la general, ni la de cadenas.
>
> **La clase deja de ser una hipotesis.** Y lo entrego **la cola, en su ultimo
> lote, por accidente**, que es exactamente como aparecieron casi todos los
> hallazgos laterales de esta campana.

| clase | estado |
|---|---|
| huerfanos por **familia de sufijo** | **CERRADA**: seis bases, nueve rutas, todas en `quality` |
| huerfanos por **nombre libre** | **NO MEDIDA**, pero **YA NO SIN MIEMBROS**: ver abajo |

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

# LAS DOS CIRUGIAS DEL CICLO, VERIFICADAS POR LA PROPIA COLA

**No es sub-fusion. Se registra aqui porque es el unico sitio donde el trabajo de
la campana se mira entero**, y porque es la evidencia mas barata que esta casa ha
conseguido de que una reparacion funciono.

**Las dos cirugias se arreglaron mirando un par. Y las dos volvieron a la cola por
su cuenta, en OTRO par, mucho mas abajo, y pasaron.**

| cirugia | que arreglo | donde volvio | veredicto de la relectura |
|---|---|---:|---|
| **1** (`08988ad`) | cinco peldanos de `risk_management` por via 1 | **puesto 59**, `haz_tu_lista_de_lo_que_puede_fallar` contra el mismo nodo del nucleo | **GRADIENTE OK**: donde el puesto 5 encontro empate blando, la cola encuentra **momento propio con voz propia** |
| **1B** (`1260581`) | `cradle_to_cradle_concepto` reencuadrado a **puerta** del tema | **puesto 173**, contra `economia_circular_como_modelo_de_negocio` | **GRADIENTE OK**: sus cuatro pasos son **decisiones de marco** y nada mas |
| **1**, otra vez | la cadencia de `revisa_tus_riesgos_con_un_ritmo` | **puesto 217**, contra `matriz_probabilidad_impacto` | **GRADIENTE OK** |
| **1**, y una cuarta | el Censo de `haz_tu_lista_de_lo_que_puede_fallar` | **puesto 268**, contra `plan_gestion_riesgos` | **GRADIENTE OK**, y **la frontera la hace un paso que escribio la cirugia**: *"marcalos como observados, no como activos"* |
| **1**, y una QUINTA | `manten_viva_tu_lista_de_riesgos`, otro de los cinco peldanos | **franja 1604** (otra cola: el cribado bajo el umbral, y ademas un par de borde), contra `matriz_probabilidad_impacto` | **GRADIENTE OK**: mantener vivo el registro contra priorizar por probabilidad e impacto son **momentos propios** |

> **Ninguna de las CINCO relecturas se hizo para verificar nada.** Salieron en el
> orden de la cola, con el auditor leyendo otro par, meses de trabajo despues.
>
> **Eso es lo que las hace valer**: una verificacion que se busca es un examen que
> uno mismo escribe. **Esta llego sola.**

**La quinta merece una linea aparte por como llego**: salio del **agujero de
borde** del cribado de la franja, es decir, de un par que la regla de corte
habia dejado fuera y que se anexo despues. Ni siquiera estaba en la cola que se
leyo. **La cirugia 1 lleva cinco verificaciones y ninguna se fue a buscar.**

**Y hay un tercer dato en el mismo puesto 173**: el nodo del NUCLEO de ese par
**vuelve a exhibir la costura que el lote 10 ya le habia confirmado**. **Dos
lecturas independientes, el mismo defecto**, que es la otra cara de la misma
moneda: la cola confirma tanto lo curado como lo pendiente.

---

# FRONTERAS CON CHOQUE DE FUENTES: CUATRO formuladas, DOS candidatas, y hay patron

**No son violaciones de gradiente. Son doctrinas que se contradicen dentro del
catalogo**, y un lector que reciba las dos sale con instrucciones opuestas.

| # | puesto | el mundo dice | el nucleo dice |
|---:|---:|---|---|
| **1** | 6 | `franquicias`: **las objeciones indican interes**, prepara respuestas | **SPIN**: los mejores reciben MENOS objeciones porque **las previenen** |
| **2** | 38, **y 159** | `compras`: **REVELA tu fecha limite real** al proveedor | **DOS nodos del nucleo**, ver abajo |
| **3** | 138 | `quality` (**Deming**): los sistemas de evaluacion de desempeno son una **BARRERA** al orgullo del trabajo | **instituye revisiones formales y periodicas** |
| **4** | 150 | `quality` (**Deming**): **proveedor unico y relacion de largo plazo** | **matriz ponderada** para elegir entre varios por puntaje |

## La frontera 2 gana un SEGUNDO nodo del nucleo (lote 14)

El puesto **159** emparejo `compras/revela_tu_propio_plazo_limite_al_negociar`
contra `nucleo/no_shop_extension_negotiation`. **El par en si es FALSO PAR
FUNCIONAL**, pero **el nodo del nucleo cae del mismo lado doctrinal**: trata el
plazo como **palanca que se administra**, no como informacion que se comparte
(*"mantener presion sobre el comprador"*).

> **Y las fuentes, verificadas, agrandan el hallazgo**: los dos nodos del nucleo
> **NO salen del mismo libro**. `negociacion_con_plazos_artificiales` es de *The
> Hard Thing About Hard Things*; `no_shop_extension_negotiation` es de *Venture
> Deals*.
>
> **No es un autor: son DOS libros distintos de la literatura de TRATOS cayendo
> del mismo lado**, contra `compras`, que viene de la literatura de **relacion con
> proveedores**. **La frontera no es entre dos nodos: es entre dos oficios.**

## La frontera 2 queda FORMULADA ENTERA (lote 18)

**El puesto 249 le encontro su espejo**, y con el la frontera deja de ser un par
suelto para ser **un mapa completo**:

| pieza | nodo | que ensena |
|---|---|---|
| **la tactica** | `nucleo/negociacion_con_plazos_artificiales` (P38) | **pon una fecha limite artificial** para forzar que avancen |
| **la palanca** | `nucleo/no_shop_extension_negotiation` (P159) | administra el plazo **para mantener presion** |
| **la defensa** | `compras/reconoce_las_tacticas_de_presion_y_urgencia_artificial_del_vendedor` (P249) | **reconoce esa tactica y no cedas por prisa fabricada** |
| **la alternativa** | `compras/revela_tu_propio_plazo_limite_al_negociar` (P38) | **revela tu fecha real** y pregunta por la suya |

> **Los cuatro son correctos para su lector.** El nucleo habla a quien vende y
> necesita que el comprador avance; el mundo habla a quien compra.
>
> **No falta ninguna pieza. Lo que falta es decidir si el catalogo lo dice.**

## El contador de objeciones: SIETE apariciones

`franquicias/manejo_objeciones_venta_franquicia` lleva **siete** emparejamientos
leidos (puestos 5, 42, 54, 70, 75, 117 y 167) de **diez** que tiene en la cola.

> **CIERRE DEL CONTADOR**: la cola termino con **DIEZ apariciones** (puestos 5, 42,
> 54, 70, 75, 117, 167, 216, 218 y 336), **las diez leidas**.
>
> **Una sola es doctrinal, la del puesto 5. Las otras NUEVE son falsos pares por
> vecindad de venta.**
>
> **El contador nunca agravo el caso: lo acoto.** Diez emparejamientos y **un solo
> problema real**, que es el que la ficha de fronteras ya tenia.

## EL PATRON, que las dos ultimas dejan a la vista

> **Las fuentes DOCTRINALES de `quality` (Deming) chocan sistematicamente con las
> MEJORES PRACTICAS GERENCIALES del nucleo.**

**Y no es casualidad de tema**: Deming escribio **contra** la evaluacion de
desempeno y **contra** la compra por puntaje comparado. **Son sus catorce puntos,
literalmente.** El nucleo, minado de manuales de gestion, trae justo lo que Deming
combatia.

**De las cuatro fronteras, DOS son Deming.** Las otras dos son de venta y
negociacion, y tambien enfrentan una fuente con doctrina propia contra una practica
generica.

> **Ninguna se resuelve sola.** Quien se queda con que, y **si el contexto se
> escribe dentro de los nodos**, es adjudicacion de la pasada unica.

## LA PIEZA NEUTRAL de la frontera Deming, y ya existia (lote 20, puesto 290)

`quality/seleccion_fuente_unica_multiple` **presenta las dos escuelas como una
DECISION CON CRITERIOS, sin doctrina**: evaluar ventajas de competencia (multiples)
contra profundidad de relacion (unica), analizar reputacion y calificacion, decidir
si se reduce la base, y **documentar la decision segun criticidad del componente**.

> **Y hay un dato que explica por que PUEDE ser neutral: es de JURAN.** La frontera
> 4 enfrenta a **Deming** (*proveedor unico y relacion larga*) con el nodo del
> nucleo (*matriz ponderada entre varios por puntaje*). **Este viene de un tercer
> autor, y por eso no tiene que defender ninguno de los dos lados.**

**Cuando la pasada unica escriba el contexto de esa frontera, el puente natural NO
hay que inventarlo: ya esta en el catalogo.** **Lo que si se
> puede afirmar ya es que no son errores: son dos escuelas, y el catalogo las
> sirve a la vez sin avisar.**

## RACIMO CANDIDATO: los cinturones de Six Sigma en `quality`

**Llega por la muestra D del cribado** (tanda 2, verificacion de la franja
**947**; detalle en `docs/FRANJA_INFORME.md`, apartado 10.1). **El cribado no
podia verlo**: son nodos de `quality` contra `quality`, y la franja solo miraba
mundo contra nucleo.

**Nueve nodos de `quality` sobre la estructura de cinturones**, medidos contra el
grafo:

| que repite | nodos |
|---|---|
| **el rol del Black Belt, tres veces** | `rol_black_belt`, `rol_black_belt_six_sigma`, `rol_facilitador_black_belt` |
| **la estructura de roles entera, dos veces** | `roles_six_sigma`, `estructura_competencias_six_sigma_lean` (las dos listan Green, Black, Master y Lean) |
| **la certificacion y el entrenamiento, tres veces** | `certificacion_belts_six_sigma`, `entrenamiento_para_breakthrough`, `desarrollo_expertos_capaces` |
| el Green Belt | `rol_green_belt_six_sigma` |

> **Seria de los racimos mas grandes de los treinta censados si perteneciera a
> ese censo. No pertenece**: el censo de treinta esta cerrado y este es material
> del barrido intra-dominio. **Queda anotado con su medicion para que el barrido
> lo encuentre hecho.**

> **Y hay un dato de frontera que sale del mismo barrido**: **Green Belt y Black
> Belt aparecen en DOCE nodos del catalogo y los doce son de `quality`. Ninguno
> del nucleo.** El vocabulario de los cinturones **no cruza al catalogo gratis**,
> que es exactamente lo que la vara del gradiente querria ver.

## FRONTERA CANDIDATA: la negacion del riesgo contra el determinismo del CEO

**Llega por la muestra D del cribado de la franja** (tanda 1, franja **303**;
detalle en `docs/FRANJA_INFORME.md`, apartado 10.1). **Entra como candidata, no
como formulada**, junto a las cuatro de arriba.

| | el mundo dice | el nucleo dice |
|---|---|---|
| **nodo** | `risk_management/deja_de_ignorar_el_riesgo` | `nucleo/no_jugar_con_probabilidades` |
| **fuente** | DeMarco y Lister, *Waltzing with Bears*, cap. 1 y 2 | Ben Horowitz, *The Hard Thing About Hard Things* |
| **doctrina** | **date permiso de pensar en negativo un rato cada semana**: dedica quince minutos a proposito a escribir lo que preferirias no pensar, marca los miedos que ignoras porque no sabes resolverlos, y dale una idea al mas feo | **rechaza la paralisis de las probabilidades**: concentra el cien por ciento del esfuerzo en buscar la solucion y **evita construir planes de contingencia que desvien el enfoque de encontrar la salida** |

**Los cuatro pasos de cada lado verificados contra el grafo.** El choque es
literal y esta en el mismo acto: **el mundo manda reservar tiempo semanal para
imaginar lo que puede fallar, y el nucleo manda no gastar foco en el plan de
lo que puede fallar.** Un lector que reciba los dos sale con instrucciones
opuestas, que es la definicion de esta seccion.

> **Parentesco que agranda el lado del mundo, verificado**:
> `risk_management/correr_hacia_el_riesgo` **sale del mismo capitulo del mismo
> libro** (DeMarco y Lister, cap. 1) y **es la otra cara de la misma doctrina**:
> *un proyecto sin riesgo casi siempre es un proyecto sin premio*, y manda
> **decidir a proposito cuanto riesgo estas dispuesto a correr**. No es un nodo
> suelto contra Horowitz: es **una escuela entera** la que esta del lado del
> mundo.

> **Por que entra como CANDIDATA y no numerada.** Ya hay otra candidata en pie,
> el sexto nodo del racimo de la culpa (`responsabilidad_personal_en_gestion`,
> Crosby contra Deming), y **ninguna de las dos esta formulada entera todavia**:
> a esta le falta el barrido de `risk_management` para saber si el mundo tiene
> mas piezas del lado de DeMarco, y si el nucleo tiene alguna pieza neutral como
> la que aparecio en la frontera 4. **No le pongo ordinal a ninguna hasta que se
> formulen.**

> **Y como llego importa**: el cribado **vio esta figura y la anoto en la razon
> del veredicto**, pero la clasifico D porque *frontera de doctrina* **no estaba
> entre las ocho figuras que disparaban C** en el encargo. **Es hueco de la lista
> de figuras, no de la lectura.** Si el barrido intra-dominio va a cazar
> fronteras, la lista de figuras tiene que decirlo antes de empezar.

### La tanda 3 ACOTA esta frontera, y la acota mucho

**Dos pares de la ultima tanda de la muestra D cambian el tamano del choque**, y
los dos estan verificados contra el grafo.

**F1379**: `risk_management/correr_hacia_el_riesgo` contra
`nucleo/fallo_como_aprendizaje_startup` (Steve Blank, *The Startup Owner's
Manual*). **Las dos escuelas CONCUERDAN.** DeMarco y Lister dicen *un proyecto
sin riesgo casi siempre es un proyecto sin premio* y mandan **decidir a proposito
cuanto riesgo correr**; Blank manda **quitarle el peso de la culpa al fallo y
tratarlo como un dato mas**. Distinto metodo, misma postura ante el riesgo y el
fallo.

> **Consecuencia para la frontera candidata, y es de acotacion:** el mundo `risk`
> **no esta enfrentado al nucleo**. Esta enfrentado a **UN autor del nucleo,
> Horowitz, y solo en un punto: los planes de contingencia.** Con el lean del
> nucleo concuerda. **Una frontera de un par contra un autor es un caso de
> contexto; una frontera del mundo contra el catalogo seria otra cosa.** Es la
> primera.

**F1399**: `risk_management/escepticismo_sano_ante_el_riesgo` (Hubbard, *The
Failure of Risk Management*) contra `nucleo/matriz_probabilidad_impacto`. **Es un
meta-nodo: desconfia de las plantillas de riesgo, incluida la del nucleo con la
que lo emparejaron.** Sus pasos, textuales: *de cualquier metodo de riesgo que
uses, preguntate como sabrias si de verdad te esta ayudando*, *desconfia de la
calma*, *antes de adoptar una plantilla ajena busca evidencia de que a alguien le
funciono*, *prefiere una nota simple y honesta a un tablero vistoso que no puedas
comprobar*.

> **El nodo no nombra la matriz de probabilidad e impacto**, y no le hago decir lo
> que no dice. **Pero el nodo del nucleo con el que se empareja es exactamente el
> genero de artefacto del que manda desconfiar**: una plantilla de escalas
> cruzadas.
>
> **Se registra como PIEZA DE CONTEXTO del mundo `risk` para la pasada unica, y
> es sano.** No es frontera ni empate: es un nodo que ensena a usar las
> herramientas con humildad, y el catalogo esta mejor con el dentro que fuera.
> **Es ademas el contrapeso natural de la frontera de arriba**, escrito por el
> propio mundo.

---

# DUDOSOS QUE ESPERAN AL FUNDADOR

## El EMPATE TRANSDOMINIO (lote 16, puesto 202): figura nueva

`risk_management/nombra_tus_suposiciones_fragiles` contra
`nucleo/leap_of_faith_assumptions`. **Cuatro pasos cada uno, dos linajes
distintos, el mismo ejercicio.**

| | el del mundo (**DeMarco y Lister**) | el del nucleo (**Ries**) |
|---|---|---|
| separar lo comprobado de lo supuesto | paso 2 | paso 1 |
| ordenar por peligro | paso 3 | pasos 2 y 4 |
| **lo propio** | definir una **prueba barata** | reescribir las **comparaciones** en terminos verificables |

### Por que es una figura NUEVA y no encaja en las que ya hay

| | por que no |
|---|---|
| **VIOLACION** | el de pago **no queda a la altura del gratis**: quedan a la **misma** altura, por caminos distintos |
| **ESPECIALIZACION** | **ninguno asume al otro hecho** |
| **FALSO PAR** | **es exactamente el mismo ejercicio**, no temas vecinos |

> **Es un ESPEJO DE LINAJES**: dos libros distintos ensenan lo mismo, y el catalogo
> los sirve sin decir que son la misma cosa.

### Las dos salidas, y decide el fundador

1. **DIFERENCIACION FINA**: el del mundo se reencuadra a **riesgo del plan**,
   citando el ejercicio de supuestos **como ya hecho**. Es la via 1 de siempre.
2. **CONVIVENCIA DECLARADA**: los dos se quedan **y se dice que son dos escuelas
   del mismo ejercicio**.

> **Dato de lectura que pesa en la decision**: el paso 4 del nodo de **riesgo**
> (*"define una forma barata de poner a prueba esa suposicion"*) **es logica de
> Lean Startup pura**, y el nodo que **viene** de Lean Startup **no lo tiene**.
>
> **Los linajes ya se cruzaron solos.** Elegir la salida 1 significaria separar lo
> que las fuentes ya mezclaron.

---

# CITAS INTRA-DOMINIO ADELANTADAS

**No son casos. Son la cola inicial del barrido intra-dominio** que el fundador
decidio hacer (ver el tablero de `docs/audits/AUD-08-Gradiente_Nucleo_Mundo.md`).

> **La lectura del gradiente las REGALA sin costo**: aparecen mientras se lee otra
> cosa, y guardarlas es gratis. **Aqui se acumulan SIN ADJUDICAR**, para que
> cuando el barrido arranque no empiece de cero.

## a) `quality`, la miniseccion de riesgos

`identificacion_de_riesgos`, `evaluacion_gestion_riesgos`,
`plan_de_gestion_de_riesgos`, `matriz_riesgo_conocido_desconocido` (puesto **137**)
y, desde el lote 17, `evaluacion_de_factores_de_riesgo` (puesto **232**). **Cinco.**

**Es el racimo que destapo la pregunta mundo contra mundo** (lote 7, puesto 51):
`quality` tiene una seccion de riesgos **paralela al mundo `risk_management`
entero**.

## b) `quality`, el par de KPI

`sistema_medicion_kpi` (puestos **15** y **84**) y `medicion_kpi` (puesto **114**).

## c) `quality`, el racimo Deming de responsabilidad

**Era trio y pasa a CUARTETO con el lote 13.**

**Era quinteto y pasa a SEXTETO con el lote 18.**

`politica_no_culpar_trabajador` (puesto **86**),
`responsabilidad_gerencial_causas_comunes` (puesto **113**),
`moral_y_sistema_no_individuo` (puesto **143**),
`identificacion_causa_raiz_no_culpa_individual` (puesto **235**, que **solapa
fuerte con el primero**), y el **base** de
`distincion_causas_comunes_especiales`.

**Y el sexto llega con el ANGULO AL REVES**: `responsabilidad_personal_en_gestion`
(puesto **248**) manda *"reconoce tu cuota de responsabilidad"* y *"revisa si le
atribuyes la causa a factores externos"*.

> **Seis nodos de `quality` sobre la culpa.** Es el racimo mas numeroso de la
> ficha, **y su base ya tiene fusion con reparto adjudicada**.
>
> **PRECISION VERIFICADA que cambia como se lee el sexto: es de CROSBY, no de
> Deming.** Los otros cinco dicen *"el sistema, no la persona"*; **este dice *"tu
> parte, no los factores externos"***.
>
> **Probable contrapeso legitimo, y por eso entra al racimo. Pero esta a un paso de
> ser la QUINTA frontera con choque de fuentes**, porque son **dos autores dando
> consejos opuestos.**

> **Ojo con este**: la **fusion con reparto del base ya esta adjudicada** (ver la
> maraña de causas comunes), y **puede absorber parte de este racimo antes de que
> el barrido llegue**. Conviene mirarlos juntos, no en dos momentos.

## d) `quality`, el racimo de mejora continua

`principios_mejora_continua` (puesto **129**), `mejora_continua_del_proceso`
(puesto **95**) y `enfoque_en_procesos_no_en_problemas` (puesto **57**).

**Tres linajes lean del mismo mundo rozandose**: Shingo, Deming y el PDCA sobre
problemas recurrentes. **Sin adjudicar.**

## e) `nucleo`, los DOS nodos de alineacion de cadena

`definicion_alineacion_cadena_suministro` (puesto **135**) y
`alineacion_cadena_estrategia_negocio` (puesto **130**).

> **Verificado contra el grafo: los dos son del NUCLEO y los dos son fuente
> Hugos.** Es decir, **son dos de los 128 de la subfamilia**, y dicen casi lo
> mismo: mapear la cadena y tu rol en ella, y alinear los drivers segun si
> compites por eficiencia o por capacidad de respuesta.
>
> **Esto cambia el peso de la subfamilia Hugos**: no es solo un problema de voz.
> **Si dos de los 128 se duplican entre si, puede haber mas**, y el barrido de voz
> tendria que traer tambien ojo de duplicado.

## f) `quality`, el CUARTETO de metas

**Era par y pasa a cuarteto con el lote 14. Los cuatro activos, los cuatro de
`quality`, los cuatro sobre fijar metas:**

| nodo | puesto | pasos |
|---|---:|---:|
| `goal_statement_smart` | 87 | 5 |
| `establecimiento_metas_de_calidad` | 96 | 5 |
| `definir_metas_smart_de_proyecto` | 139 | 4 |
| `establecer_metas_caracteristicas` | 164 | 5 |

> **Dos de ellos llevan SMART en el titulo y los cuatro fijan metas de un proyecto
> de calidad.** Es el racimo mas parejo de los siete: **ninguno destaca sobre los
> otros**, que es justo lo que hace sospechar que son uno.

## g) `nucleo`, el par de ANALISIS COMPETITIVO

`analisis_competitivo` (puesto **193**, 5 pasos) y
`analisis_competitivo_deconstruccion` (puesto **209**, 6 pasos). **Los dos del
nucleo, y los dos del MISMO libro**: *Winning at New Products - Robert G. Cooper*.

> **DATO DE GRAFO, y no es el que se esperaba: NO estan sueltos.** No se declaran
> entre si, **pero comparten vecino en un orden definido**:
>
> `analisis_competitivo_deconstruccion` **->** `iota_analysis` **->**
> `analisis_competitivo`
>
> **Estan a dos saltos, encadenados a traves de un intermedio**, con la
> deconstruccion **antes** del analisis. **No es un par huerfano: es una escalera
> con un peldano en medio.**

> **Y una precision de contenido**: el **desarme fisico** de productos esta **solo
> en uno** (*"comprar y desarmar fisicamente los productos competidores en
> laboratorio"*). El otro dice *"analizar fortalezas y debilidades de los productos
> de los competidores lideres"*, que es **vecino pero no el mismo acto**.

**Sin adjudicar.** La escalera existente **juega en contra** de la sospecha, igual
que en el caso 1 de Goldratt.

## h) `nucleo`, el par de INNOVACION ABIERTA: el mas pegado hasta la fecha

`open_innovation_ideacion` (puesto **187**, 6 pasos) y `innovacion_abierta`
(puesto **233**, 7 pasos). **Los dos del nucleo y los dos del mismo libro**
(*Winning at New Products - Robert G. Cooper*).

| lo que dicen los dos | en el primero | en el segundo |
|---|---:|---:|
| equipos de **scouting** | 1 | 2 |
| **pagina web** para recibir ideas del publico | 2 | 3 |
| **transferencia tecnologica universitaria** | 3 | 4 |
| sesiones con **proveedores** tecnicos | 4 | 5 |
| **el mismo ejemplo de LEGO Digital Designer** | 5 | 6 |

**Lo propio de cada uno es UN paso**: adaptar Stage-Gate en el primero; el sindrome
NIH y la seleccion de metodo por complejidad en el segundo.

> **DATO DE GRAFO, y esta vez NO exculpa.** Estan **conectados directamente y en
> los dos sentidos**.
>
> **Pero la conexion no significa lo mismo que en Goldratt.** Alli el primero
> **DELEGABA** en el segundo (*"aplicar los cinco pasos de enfoque"*), y por eso el
> caso 1 se cerro. **Aqui el segundo REPITE al primero**, cinco pasos de siete, con
> el mismo ejemplo.
>
> > **Una escalera cuyo segundo peldano vuelve a decir el primero no es una
> > escalera.**
>
> **La leccion, para no repetir el error del caso 1 al reves**: la pregunta no es
> *"¿estan conectados?"*, es *"¿el segundo CONTINUA o REPITE?"*. **La arista sola
> no responde nada.**

**Sin adjudicar.**

## i) `nucleo`, los DOS nodos de A/B testing

`split_testing_experimentos_ab` (C3) y `ab_testing_optimizacion` (C2). **Los dos
del nucleo y los dos con costura confirmada.**

> **Su destejido probablemente converge en uno.** En la pasada unica **se leen
> JUNTOS**: destejer uno sin mirar al otro seria escribir dos veces la misma
> narracion canonica.

## j) `risk_management`, el CUARTETO de actualizacion de la lista

**Era trio y pasa a CUARTETO con el lote 12.**

`el_riesgo_cambia_con_el_tiempo` (puesto **107**) y
`que_hacer_con_un_riesgo_nuevo` (puesto **133**) contra los **dos reencuadrados de
la cirugia 1**, `manten_viva_tu_lista_de_riesgos` y
`revisa_tus_riesgos_con_un_ritmo`.

> **El cuarto llega con veredicto propio**: el 133 es **DUDOSO con via 1 suave**
> (repite el registro del nucleo en sus pasos 2 a 4, y su unico aporte es *"no lo
> ignores por no estar en el plan"*). **Su arreglo por gradiente y su lectura
> intra-dominio son el mismo trabajo**, y conviene no hacerlo dos veces.

> **Este merece cuidado especial**: los dos contra los que roza **acaban de ser
> reescritos**, y el veredicto del puesto 59 confirmo que **el reencuadre les dio
> momento propio**. Leer esto como sub-fusion sin tener eso presente seria
> deshacer una cirugia que la propia cola valido.

---

# NOTA DE VOZ CON NOMBRE DE GRUPO: LA SUBFAMILIA HUGOS

**Para el barrido de voz residual. No es sub-fusion.**

Tres nodos del **nucleo** aparecieron en tres lotes distintos con la misma
enfermedad de voz: **cadena de suministro a escala de multinacional, en voz de
manual.**

| nodo | puesto | pasos |
|---|---:|---:|
| `driver_transporte` | 110 | 4 |
| `gestion_riesgo_cadena_suministro` | 120 | 8 |
| `alineacion_cadena_estrategia_negocio` | 130 | 4 |

**La politica de escala ampara el contenido** (nada se esconde por estructura).
**La voz se cura EN GRUPO, con el mismo criterio, cuando la pasada unica llegue.**

## CORRECCION DEL NOMBRE, verificada contra el grafo

**El encargo llamaba al grupo "subfamilia Chopra". Los tres comparten fuente, pero
NO es esa.**

> **Los tres citan *Essentials of Supply Chain Management - Michael H. Hugos*.**
>
> **Chopra aparece DENTRO de un paso**, no como fuente: el primer paso de
> `alineacion_cadena_estrategia_negocio` dice *"responder las 6 preguntas de
> **Chopra y Meindl** sobre tu mercado"*. Es **un autor citado por el libro**, no
> el libro.

**El grupo se llama SUBFAMILIA HUGOS.**

## Y el grupo es MUCHO mas grande que tres

**Medido sobre los activos:**

| cadena de fuente | nodos |
|---|---:|
| `Essentials of Supply Chain Management - Michael H. Hugos` | **93** |
| `Essentials of Supply Chain Mana - Michael H. Hugos` (la variante truncada) | **14** |
| cadenas combinadas que la incluyen | **21** |

> **No son tres nodos: son 128 nodos del nucleo salidos de UN SOLO libro de cadena
> de suministro escrito para multinacionales.**

> **CIFRA CONFIRMADA POR DOS VIAS INDEPENDIENTES.** El ejecutor la sumo por cadena
> de fuente (93 exactas, 14 truncadas, 21 combinadas) y el auditor conto los
> activos con Hugos en el campo. **Las dos dan 128, y los 128 son del nucleo, sin
> uno solo en los mundos.**
>
> **Los tres que el gradiente cazo son una MUESTRA, no el grupo.** Cuando la
> pasada unica llegue a esta nota, **lo primero no es curar tres: es medir cuantos
> de los 128 tienen la misma voz.**

**Y de paso confirma la ficha dormida de normalizacion de fuentes**: la variante
truncada de 14 nodos es exactamente el ruido de puntuacion que aquella anoto.

## k) `nucleo`, el par de PROGRAMACION DE PRODUCCION

`programacion_produccion` (puesto **208**) y
`produccion_scheduling_balance_objetivos` (puesto **251**). **Cuatro pasos cada
uno, los dos del nucleo, los dos de Hugos.**

| lo que dicen los dos | uno | el otro |
|---|---:|---:|
| **lote economico** | 1 | 2 |
| **run-out time** para secuenciar | 2 y 3 | 3 |
| balancear utilizacion, inventario y servicio | 4 | 1 |

> **CONTINUA O REPITE: repite.** Los cuatro pasos de uno son los cuatro del otro en
> otro orden. **Y NO estan conectados**, ni en un sentido ni en el otro: **aqui no
> hay ni siquiera una arista que discutir.**

> **Es el SEGUNDO par duplicado dentro de la subfamilia HUGOS**, tras el de
> alineacion de cadena (lote 13). **La sospecha sobre los 128 deja de ser teorica:
> dos pares, encontrados los dos por accidente, en un bloque que nadie ha barrido.**

## l) `nucleo`, el par de ROI, y la CONSECUENCIA para el destejido

`calculo_roi` (puesto **297**, 5 pasos genericos y sanos) y
`propuesta_gasto_capital` (puesto **189**, 12 pasos, **la costurada**).

> **DATO DE GRAFO: NO estan sueltos. Estan encadenados en ORDEN a traves de un
> intermedio.**
>
> `calculo_roi` **->** `comparacion_metodos_inversion` **->**
> `propuesta_gasto_capital`
>
> **El generico va PRIMERO.** Y sin embargo la costurada **vuelve a derivar lo
> mismo**: costo total de la inversion, beneficios esperados y el calculo del
> retorno estan **en los dos**.

### CONSECUENCIA PARA LA PASADA UNICA, y es operativa

> **El destejido de `propuesta_gasto_capital` debe mirar PRIMERO a este vecino.**
>
> **Parte del material duplicado puede sobrar del todo si el generico ya lo
> cubre**, y la escalera dice que deberia cubrirlo. **Destejer sin mirar al vecino
> arriesga conservar como "aporte unico" algo que el peldano anterior ya dijo
> mejor.**

**Es la primera vez que un destejido tiene una precondicion escrita.**

## m) `nucleo`, las ferias: escalera SANA, y dos nodos en `franquicias`

**Verificado, y sale a favor del catalogo**: `estrategia_ferias_comerciales`
declara a `tacticas_de_ferias_comerciales` en sus siguientes, y este a aquel en sus
previos. **Del mismo libro (*Traction*), estrategia primero y tacticas despues.**

> **No es duplicado: es como se debe hacer, y sirve de contraejemplo** para los
> pares de este apartado.

**Lo que si queda anotado es del lado del mundo**: `franquicias` tiene **dos nodos
propios de ferias**, `marketing_en_ferias_comerciales_de_franquicias` (P180) y
`ferias_comerciales_franquicia` (P255). **Sin adjudicar.**

---

## PARES CALCADOS DENTRO DE UN MUNDO (lote 19)

> **LA ACRECION ENTRE NODOS NO ERA MONOPOLIO DEL NUCLEO.** Es la primera vez que
> aparecen pares calcados **dentro de un mundo** con esta claridad, y aparecieron
> **dos en el mismo lote**.

### n) `quality`, el par de INNOVACION TIPO II

`tipos_innovacion_i_ii` (6 pasos, puesto **267**) y `innovacion_tipo_ii` (5 pasos,
puesto **233**). **Los dos de `quality`, los dos de Juran.**

**Mismo metodo**: las mismas **tres columnas** (*hacerlo mas grande*, *hacerlo mas
pequeno*, *combinarlo con*), el mismo **diferir la critica**, el mismo refinar.

> **CONTINUA O REPITE: repite, y ademas comprime.** Lo unico propio del segundo es
> *"seleccionar las ideas con mayor potencial"*.
>
> **Y SI estan conectados**, en los dos sentidos, con `tipos_innovacion_i_ii`
> primero. **Es la misma figura del par de innovacion abierta del nucleo**: una
> arista que ordena, pero un segundo peldano que vuelve a decir el primero.

### o) `quality`, el par de CONTROL DE PROCESO (tercer calcado del mundo)

`plan_de_control` (8 pasos, puesto **122**) y `matriz_de_control_de_proceso`
(6 pasos, puesto **316**). **Los dos de `quality`, los dos de Juran.**

| el metodo | en el plan | en la matriz |
|---|---:|---:|
| identificar variables que afectan al remedio y al cliente | 1 | 1 |
| el estandar que dispara la accion, con limite de control | 2 | 2 |
| como, donde y cuando se mide | 3 y 4 | 3 |
| quien analiza y quien actua | 5 y 6 | 4 |
| pasos para regresar el proceso a control | 7 | 5 |
| **revisar la matriz** | 8 | 6 |

> **La prueba mas limpia esta dentro del propio `plan_de_control`: su paso 8 dice
> *"revisar LA MATRIZ"*.** **El nodo llamado plan se refiere a si mismo como
> matriz.** Son el mismo artefacto con dos nombres.

**CONTINUA O REPITE: repite, comprimido. Y NO estan conectados.**

## p) `quality`, los GEMELOS DEL PASO 3, y una figura nueva

`medicion_calidad` (5 pasos, puesto **307**) y `medicion_calidad_2` (5 pasos,
puesto **289**). **Los dos de Crosby, y los dos con el numero de paso en el
titulo**: *"Medicion de la Calidad (Paso 3)"* y *"Paso 3: Medicion de la Calidad"*.

> **NO es una de las 36 parejas, y conviene que quede claro.** Aquella medicion
> exige que **ninguno de los dos** lleve marca. **`medicion_calidad` tiene
> `ids_alias` y un `merged_originals`: ya estuvo en una fusion.**
>
> **Es una figura distinta, y algo peor: el base fue TRATADO en una fusion, y su
> propio `_2` quedo fuera de ella.** **Nadie miro al hermano mientras se fusionaba
> al hermano.**

**Y no estan calcados**: el base define metricas por area e involucra a los
responsables; el `_2` recolecta datos de inspeccion, **clasifica defectos por
gravedad** y pone al **ingeniero de calidad** a revisarlos a diario.

> **Dos alturas del mismo paso, y el `_2` en voz de fabrica.** **La lectura de
> fusion decide, y el superviviente no se adjudica aqui.**

## q) `nucleo`, el par de SCORECARDS (cuarto calcado del nucleo)

`scoring_model_scorecard` (puesto **174**) y `scorecard_de_seleccion_de_proyectos`
(puesto **322**). **Cinco pasos cada uno, los dos del nucleo, los dos de Cooper.**

| lo que dicen los dos | uno | el otro |
|---|---:|---:|
| **los MISMOS seis criterios**: encaje con la estrategia, ventaja del producto, atractivo del mercado, aprovechar lo que ya sabes hacer, viabilidad tecnica, riesgo contra retorno | 1 | 1 |
| escala o pesos | 2 | 2 |
| puntuar y priorizar | 3 y 4 | 3 y 4 |

**Lo propio de cada uno es UN paso**: *"usa un scorecard distinto segun el tipo de
proyecto"* contra *"revisa y actualiza tu lista"*.

> **CONTINUA O REPITE: repite. Y NO estan conectados.**

## r) `franquicias`, el par de la PRIMERA LLAMADA

`proceso_primera_llamada` (7 pasos, puesto **270**) y
`proceso_llamada_inicial_venta` (8 pasos, puestos **74** y **274**). **Los dos de
`franquicias`, los dos de Siebert.**

**Misma agenda**: contacto y fuente del lead, calificar financieramente, urgencia y
motivos, **hot buttons**, que otras franquicias considera, overview breve, y pedir
el avance con **el CIRF**.

> **Y aqui NO estan conectados**: ninguno declara al otro.
>
> **Ademas la voz los separa**: `proceso_primera_llamada` esta en **tu** (*obten,
> calificalo, detecta, preguntale*) y `proceso_llamada_inicial_venta` en
> **infinitivo** (*obtener, calificar, determinar, identificar*).
>
> **Es la figura del trio ECR y de `desarrollar_caracteristicas_proceso`: una
> version curada viviendo al lado de su hermana sin curar, y ninguna marcada.**

**Sin adjudicar los dos.**

---

## s) `nucleo`, el racimo de SUCESION

`founder_ceo_succession_process` (leido **sano** en el lote C3),
`framework_tres_rs_sucesion` (puesto **305**) e
`identificacion_necesidad_sucesion_ceo` (puesto **315**).

> **Dato de grafo**: `identificacion_necesidad_sucesion_ceo` **declara a**
> `framework_tres_rs_sucesion` **en sus siguientes**: **dos de los tres son
> escalera.** El tercero **esta aparte**, sin arista con ninguno.

**Y uno de los tres carga el colateral de AUDIENCIA INVERTIDA** (ver abajo), asi
que **la lectura de este racimo no es solo de duplicado: es tambien de a quien le
habla cada uno.**

## t) `nucleo`, la RETENCION: un trio donde la cura YA se aplico

| nodo | pasos | estado |
|---|---:|---|
| `customer_retention_strategy` | **17** | **DEPRECADO** |
| `customer_retention_tactics` | 6 | **ACTIVO**, y lo tiene en sus `ids_alias` |
| `keep_customers_strategy` | 6 | ACTIVO |

**El deprecado de 17 pasos era una ACRECION de manual**, con el duplicado a la
vista (paso 7 contra paso 11, las dos midiendo el abandono en los primeros 100
dias, **79,7 de similitud**).

> **Y alguien ya lo destejio.** `customer_retention_tactics`, seis pasos, **es su
> version destejida, y lo absorbio con alias.**
>
> **Es el DESTEJIDO POR REESCRITURA que la clase 9 propone, ya aplicado una vez en
> este catalogo, antes de que la clase tuviera nombre.** **El arreglo no es una
> idea nueva: es una practica que esta casa ya ejecuto y funciono.**

**Lo que queda vivo es un par**: `keep_customers_strategy` (estrategia) y
`customer_retention_tactics` (tacticas), **NO conectados entre si**. **Sin
adjudicar.**

---

## CITAS MUNDO CONTRA MUNDO

**Subseccion nueva (lote 15).** Las de arriba son **dentro de un dominio**. Estas
cruzan dos mundos, y por eso **no las adjudica el mismo barrido**: van al
**inter-mundos del final**, que es la tercera cara del instrumento pendiente.

### 1. La calificacion de proveedores vive en DOS mundos

| nodo | mundo | puesto | que es |
|---|---|---:|---|
| `calificacion_de_calidad_de_proveedores` | `quality` | 163 | **el plan compuesto con pesos**: metricas de no conformidad y DPM, pesos para calidad, entrega, costo y respuesta, y la calificacion decide **participacion de mercado entre proveedores** |
| `lleva_scorecard_desempeno_proveedor` | `compras` | 194 | **el registro simple del taller**: una lista corta de lo que te importa, anotar **en palabras** si cumplio, guardar un comentario de que paso, y mirarlo antes de renegociar |

> **Los dos angulos son legitimos y la diferencia es de escala, no de tema**: uno
> reparte volumen de compra entre proveedores con una formula ponderada, el otro te
> deja renegociar sabiendo que paso.
>
> **Lo que no existe es un puente entre ellos**, ni nada que le diga al lector que
> el mismo trabajo tiene dos alturas segun su tamano.

**Sin adjudicar. La decision es del barrido inter-mundos.**

### 2. El DFE vive en DOS mundos

| nodo | mundo | puesto | fuente y angulo |
|---|---|---:|---|
| `design_for_environment` | `quality` | 288 | **Juran**, angulo de **materiales** |
| `diseno_para_el_medio_ambiente` | `environmental` | 81 | **Esty**, *Green to Gold*, angulo de **marco** |

**El mismo tema con casi el mismo nombre, de dos libros distintos, y NO
conectados.**

> **A diferencia de la calificacion de proveedores, aqui no hay diferencia de
> escala: hay diferencia de ANGULO.** Los dos hablan al mismo lector.

**Sin adjudicar.**

---

## La colision de nombre, LEIDA COMPLETA (lote 17)

`exportacion/proteccion_propiedad_intelectual_2` **paso por sus dos parejas de la
cola y las dos salieron sanas**: contra `nucleo/marcas_registradas` (puesto 161) y
contra `nucleo/intellectual_property_strategy` (puesto 221), **las dos OK POR
ESPECIALIZACION**.

> **El nodo esta bien. Lo unico raro era su nombre.**
>
> Con esto, la entrada de las 36 parejas queda cerrada por el lado de la unica que
> cruzaba dominios: **no habia duplicado que fusionar, habia un sufijo que
> significaba otra cosa.**

---

# FIGURA NUEVA: EL BASE FUE FUSIONADO Y SU HERMANO QUEDO FUERA

**Medida por el auditor y reproducida por el ejecutor.** Es **la inversa de los
huerfanos del caso 8**, y es peor.

| | los huerfanos (caso 8) | esta figura |
|---|---|---|
| el **base** | **sin marcas**: se quedo fuera de la fusion | **CON marcas** (`ids_alias` o `merged_originals`): **estuvo EN la fusion** |
| el **hermano `_N`** | fue absorbido por un tercero | **activo y sin marcas**: **nadie lo miro** |

> **Alli la fusion no vio al base. Aqui la fusion TRATO al base y dejo fuera a su
> propio hermano.** **Alguien tuvo el nodo en la mano y no miro al lado.**

## La consulta, reproducida: SEIS rutas sobre CUATRO bases

| base (con marcas) | dominio | hermanos que quedaron fuera |
|---|---|---|
| **`accion_correctiva`** | quality | **`_2`, `_4` y `_6`**: **TRES** |
| `medicion_calidad` | quality | `_2` |
| `six_sigma_dmaic` | quality | `_2` |
| `ciclo_ventas_calidad_franquicia` | franquicias | `_2` |

**Seis rutas, cuatro bases, cinco de las seis en `quality`.**

## Y la secuencia de Crosby otra vez

**Cuatro de los seis hermanos que quedaron fuera son de Crosby** (*Quality is
free*): los tres de `accion_correctiva` y el de `medicion_calidad`. **Dos de ellos
llevan el numero de paso en el titulo**: *Accion Correctiva (**Paso 6**)* y *Paso
3: Medicion de la Calidad*.

> **Y un detalle que agrava el de `accion_correctiva`: el base es de JURAN y los
> tres hermanos que quedaron fuera son de CROSBY.** La fusion conservo el nodo de
> un autor **y dejo sueltos tres del otro**, sobre el mismo tema.

**Sin adjudicar. Lectura de fusion en la pasada unica.**

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
| franquicias | 1 |
| **la pareja que CRUZA dominios** | **1** |

### La pareja que cruza, identificada

**Las dos cuentas del total coincidian en 36 y discrepaban en una etiqueta**: una
tabla decia `core 1` y la otra `exportacion 1`. **Las dos eran correctas**, porque
contaban dominios distintos de la misma pareja:

| miembro | dominio |
|---|---|
| `proteccion_propiedad_intelectual` | **core** |
| `proteccion_propiedad_intelectual_2` | **exportacion** |

**Es la UNICA de las 36 que cruza dominios.**

### Y leida, no es un duplicado: es una COLISION DE NOMBRE

| nodo | fuente | de que habla |
|---|---|---|
| el de `core` | *Venture Deals* | **quien es dueno de lo que se crea**: acuerdo de work for hire, a quien le cuentas informacion sensible |
| el de `exportacion` | *A Basic Guide to Exporting* | **registrar patente y marca en cada mercado extranjero** antes de exportar |

> **Fuentes distintas, temas distintos. El sufijo `_2` aqui no significa "segunda
> version de aquello": significa "el id ya estaba ocupado".**

**Y no esta en la cola del gradiente** (titulo 46,3 y semantica por debajo del
umbral), asi que **tampoco es un par nucleo-mundo**. El `_2` si empareja contra
**otros dos** nodos del nucleo, en los puestos **161 y 221**, ambos sin leer.

> **LA MORALEJA, que afila la medicion de las 36**: el sufijo `_N` de este catalogo
> **carga DOS significados distintos**, y confundirlos es la trampa. Casi siempre
> es *"segunda extraccion del mismo concepto"*; **aqui es *"el nombre estaba
> tomado"***.
>
> **Razon de mas para leer las 36 antes de tratarlas como duplicados.**

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
| `quality/medicion_calidad_2` | **Paso 3**: Medicion de la Calidad |
| `quality/medicion_calidad` | Medicion de la Calidad **(Paso 3)** |

**Los dos de ECR entraron con la lectura del trio (lote 9), y son los dos que esa
fusion absorbe**: ahi el titulo se cura sin trabajo extra. **El quinto llego en el
lote 20 (puesto 289) y NO tiene fusion que lo cure**: hay que tratarlo aparte.

> **SEIS titulos con el numero de paso de Crosby**, y **los seis son pasos de la
> MISMA secuencia** (3, 3, 4, 11, 11 y 13). **No es un descuido suelto: es una
> tanda de extraccion que copio los encabezados del libro.**
>
> **Y el Paso 3 esta DOS veces**, en los dos gemelos de `medicion_calidad`: **el
> mismo encabezado copiado dos veces desde el mismo libro.**

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

## C4. EL ID FOSIL: el nombre sobrevivio a su contenido

Encontrado en el **lote 15, puesto 190**. **No es sub-fusion, ni voz, ni valvula:
es un id que dejo de decir la verdad.**

### `nucleo/convertir_unknown_unknowns_en_known_unknowns`

| | |
|---|---|
| **su id promete** | epistemologia de riesgos: convertir lo que no sabes que no sabes |
| **su titulo dice** | *"Anticipar Escenarios de Riesgo entre Cofundadores"* |
| **sus tres pasos hacen** | listar eventos disruptivos personales (visa, salud, mudanza), discutir como cambia la equidad o los roles, documentar acuerdos de contingencia |
| **su fuente es** | *The Founder's Dilemmas* |

**Verificado**: **no tiene `ids_alias` ni `merged_originals`**. La mudanza del tema
**no dejo rastro**: solo el id fosil.

> **Inofensivo para el usuario, que ve el titulo. Venenoso para toda consulta por
> id**, que es como se trabaja aqui: los rumbos, los puentes, las fichas y esta
> misma campana citan nodos **por su id**.
>
> **Un id que miente hace que la busqueda correcta devuelva el nodo equivocado, y
> el lector humano no tiene forma de notarlo.**

### Clase con UN miembro medido, y sin barrido adjudicado

**Puede no ser el unico.** Un barrido seria comparar el id contra el titulo y el
contenido de cada nodo, y **no se ha corrido**.

> **Y ese unico miembro CERRO LA COLA.** Se re-exhibio en los puestos **324** y
> **346**, o sea **el ultimo par leido de los 346 es el id fosil**. **Tres
> apariciones en total** (190, 324 y 346), **las tres falsos pares**: el id **atrae
> emparejamientos por lo que PROMETE, no por lo que dice**. Es la demostracion
> practica de por que un id que miente envenena las consultas.

> **Queda declarada como clase con un solo miembro conocido.** Es lo unico honesto
> que se puede decir hoy: **no que sea un caso aislado, sino que solo se ha medido
> uno.**

## C5. LA AUDIENCIA INVERTIDA: el contenido acierta, el destinatario no

Encontrado en el **lote 21, puesto 305**. **Un miembro medido.**

### `nucleo/framework_tres_rs_sucesion`

Sus cuatro pasos, verificados: *"invertir tiempo en construir una relacion de
confianza **con el fundador** antes de asumir el rol de CEO"*, *"educar
gradualmente **al fundador** sobre su nuevo rol"*, *"negociar incentivos... para
**el fundador saliente**"*, *"asignar **al fundador** un area donde su experiencia
siga siendo valiosa"*.

> **La segunda persona implicita apunta al CEO entrante o al inversor que gestiona
> la sucesion. Y el lector de la app es el fundador.**

### Por que es una clase propia y no cabe en las que ya hay

| clase | por que no es esa |
|---|---|
| **voz corporativa** | no es que hable a escala grande: **habla a OTRA PERSONA** |
| **id fosil** (C4) | alli **el nombre miente y el contenido esta bien**; aqui el contenido esta bien **y apunta al actor equivocado** |
| **valvula** | no es que el lector no pueda hacerlo: **es que el nodo no le habla a el** |

> **El nodo esta bien escrito. Simplemente no es para quien lo va a leer.**

**Clase con UN miembro medido y sin barrido adjudicado.** Un barrido seria buscar
la segunda persona implicita de cada nodo del nucleo, **y no se ha corrido**.

> **Es lo unico honesto que se puede decir hoy: no que sea un caso aislado, sino
> que solo se ha medido uno.**

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
