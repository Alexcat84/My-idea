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

#### MEDICION COMPLETA (10 ago 2026, de rebote en el puesto 362 del cribado intra): PRIMER DESTEJIDO DEL PLAN

**El cribado intra-dominio volvio a caer sobre este nodo por otro camino, y al
recontarlo salieron dos cosas que esta entrada no tenia. Queda medido entero.**

**Primero, la cuenta de los pasos se queda corta en una fila.** La instruccion de
mostrarlo solo a los primeros usuarios **no aparece tres veces sino CUATRO**:

| la instruccion | en los pasos | como se dijo la cuarta vez |
|---|---|---|
| *"muestra tu primera version solo a los earlyvangelists, no al mercado masivo"* | 7, 12, 20 **y 4** | el paso **4** dice **early adopters** en vez de **earlyvangelists**; es la misma orden con otra etiqueta, y por eso se habia escapado |

**Segundo, y esto no se habia mirado nunca: la costura tambien esta en las
`condiciones_activacion`, y ahi es peor.** **El nodo declara DIEZ condiciones de
activacion**, y al agruparlas por lo que dicen **quedan CINCO**:

| lo que la condicion dice de verdad | en cuantas condiciones | cuales |
|---|---:|---|
| alguien quiere construir el producto completo con todas las funciones antes de validar | **4** | 3, 5, 7, 9 |
| no hay evidencia todavia de que el problema sea real | **2** | 6, 10 |
| no se sabe cuando dejar de analizar y empezar a construir | **2** | 1, 2 |
| ya hay earlyvangelists listos para probar | 1 | 4 |
| no esta claro que caracteristicas priorizar | 1 | 8 |

> **Diez condiciones para decir cinco cosas, y una de ellas dicha cuatro veces.**
> **La costura no es solo de pasos: el nodo se repite tambien en la puerta por la
> que se entra a el.** Ninguna otra entrada de esta ficha habia medido ese campo,
> y este caso obliga a mirarlo en los demas emblemas.

> **POR ESO ES EL PRIMER DESTEJIDO DEL PLAN, y no por ser el mas grande**, que no
> lo es: `decision_de_vender_startup` tiene 34 pasos. **Lo es porque es el mas
> barato de arreglar y el que mas ensena.**
>
> - **El material sobrante ya esta identificado paso por paso**, con posiciones,
>   asi que el destejido **no exige releer y decidir**: exige **borrar**.
> - **Las cinco narraciones dicen lo mismo**, o sea que **no hay reparto que
>   negociar**: no se parte en dos nodos, se poda a uno.
> - **De veintidos pasos a cinco y de diez condiciones a cinco** deja el nodo
>   dentro del estandar de 3 a 6 sin escribir una sola frase nueva.
> - **Y es el nodo de bandera del catalogo**: si el destejido se ensaya aqui, el
>   antes y el despues se puede ensenar sin explicar nada.
>
> **Lo que este caso deja probado para los demas**: cuando la medicion trae las
> posiciones exactas de cada repeticion, el destejido deja de ser un juicio y
> pasa a ser una lista de borrados. **Medir bien es la mitad del arreglo.**

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
| `exportacion/internacionalizacion_sitio_web_exportacion` | 9 | **50,1** | **3** | **checklist de nueve mejoras del sitio** para vender fuera: texto de bienvenida, conversor de moneda, quien paga aranceles, testimonios internacionales, opciones de envio, politica de devoluciones, invitacion a distribuidores, anuncios por pais, beneficios de tratado. **Ninguna repite a otra.** |
| `exportacion/elaboracion_pro_forma_invoice` | 8 | 49,7 | 4 | **checklist de los campos de un documento**: partes, referencia y fecha, productos y precio, volumen y peso, descuentos y terminos, seguro y flete, declaracion de veracidad y origen, y marcarlo como Pro Forma. **Ocho campos distintos, cero narracion.** |
| `exportacion/elementos_plan_exportacion_ejemplo` | 13 | 48,6 | **10** | **trece elementos de un plan de exportacion**: introduccion, metas medibles, recursos financieros y no financieros, capacidad, mercados, politica de riesgo, agente de carga, idioma del etiquetado, codigo arancelario, propiedad intelectual, precios y sitio web. |
| `core/background_startup_vs_corporativo` | 9 | 48,8 | 4 | **nueve criterios de entrevista** para decidir entre experiencia de startup y de corporativo. Lista de criterios, no narracion. **Es el PRIMER largo legitimo que no sale de los dos manuales.** |

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

> **La CUARTA de la clase la confirma, y ademas rompe la firma por abajo.** Los
> tres primeros tenian cortes anchos (6, 5 y 4);
> `internacionalizacion_sitio_web_exportacion` tiene **corte 3**, la evidencia mas
> delgada del instrumento, **y sigue siendo formato lista**. **La firma de la
> clase es el CONTENIDO (nueve items sin repeticion), no el ancho del corte.** El
> corte ancho la delata a menudo; no la define.

> **Con la QUINTA, la clase deja ver de donde sale, y es un dato de origen que
> ninguna lectura caso por caso habria dado.** Las cinco vienen de **DOS libros y
> solo dos**:
>
> | fuente | miembros |
> |---|---|
> | *A Basic Guide to Exporting* (U.S. Commercial Service) | **4**: `seleccion_representante_extranjero`, `internacionalizacion_sitio_web_exportacion`, `elaboracion_pro_forma_invoice`, `elementos_plan_exportacion_ejemplo` |
> | *Juran's Quality Handbook* | **2**: `principios_medicion_efectiva`, `fmea_analisis_de_modos_de_falla` |
> | *The Founder's Dilemmas* con *The Hard Thing About Hard Things* | **1**: `background_startup_vs_corporativo` |
>
> **El largo legitimo esta MUY concentrado, pero ya no solo en dos manuales.**
> **Seis de siete siguen saliendo de los dos de referencia**, y el manual de
> exportacion solo aporta cuatro. **El septimo rompe la exclusividad**:
> `background_startup_vs_corporativo` sale de dos libros de fundadores y no de un
> manual, lo que dice que **el formato lista no es propiedad de los manuales,
> solo su casa mas frecuente.** El resto del razonamiento se mantiene: el grueso
> de la clase esta concentrado en dos manuales de referencia, y los dos son de los que enumeran criterios, campos y
> principios. **Eso convierte la decision de la pasada unica en una decision de
> FUENTE**: no es si este nodo merece nueve pasos, es si el estandar de 3 a 6
> admite los formatos de estos dos libros. **Una decision en vez de cinco.**

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
| `quality/auditoria_calidad_proveedores` | 7 | 50,2 | 4 | **secuencia unica de UNA visita**: reunirse con el gerente de calidad, luego con el general, ejecutar la auditoria, redactar el informe, anotar los desacuerdos y distribuirlo desde la planta. **No hay dos narraciones: hay una cronologia.** |
| `quality/matriz_de_seleccion` | 7 | 50,2 | **3** | **el metodo de los cien puntos, en secuencia unica**: acordar criterios, repartir 100 puntos, promediar pesos, listar alternativas, calificar de 1 a 5, promediar y consensuar. **Cada paso necesita al anterior.** |
| `core/decision_de_salir_a_bolsa` | 10 | 50,0 | 7 | **decidir y luego preparar**: los pasos 1 a 5 evaluan si salir a bolsa (capital, exposicion personal, bloqueo, junta, accionistas dispersos) y los 6 a 10 preparan la salida (minimos para ser publico, ventajas y desventajas, hablar con quien ya lo hizo, preparar al equipo, precio de la oferta). **Continua, no repite.** |
| `franquicias/programa_cumplimiento_legal` | 6 | 49,8 | **3** | **secuencia unica de cumplimiento**: capacitar cada ano, designar punto de contacto legal, registrar comunicaciones, entrevista de cierre, compras de prueba, cero tolerancia. |
| `core/contratacion_experiencia_vs_potencial` | 10 | 49,2 | 5 | **elegir el perfil y luego afinarlo**: los pasos 1 a 4 deciden entre rock star y rising star con el burn rate delante, y los 5 a 10 afinan con la pregunta de conocimiento interno contra externo y sus dos ramas. |
| `quality/identificacion_practicas_lideres` | 6 | 49,0 | **3** | **DOS foros distintos en secuencia**, no dos narraciones: el paso 1 es el foro interno de hallazgos y el 4 es el foro de intercambio de practicas lideres, con presentaciones y preguntas recogidas antes. |
| `core/verificar_modelo_ingresos` | 6 | 48,8 | **3** | **secuencia unica de calculo**: recopilar datos, ingreso bruto, ingreso neto de canal, restar costos, tres escenarios y evaluar el cash burn. Cada paso necesita al anterior. |
| `seguridad_digital/csf_funcion_govern` | 7 | 48,5 | **3** | **secuencia unica de la funcion Govern del NIST CSF 2.0**: mision y riesgos, requisitos aplicables, responsable, impacto de perder activos, seguro, terceros y comunicar politicas. |
| `quality/desarrollo_caracteristicas_producto` | 6 | 48,3 | **3** | el **Paso 4 del Quality by Design de Juran** en secuencia unica: agrupar necesidades, elegir metodos, tecnicas creativas, verificar regulaciones, seleccionar y detallar. |
| `quality/abolir_inspeccion_masiva` | 6 | 48,3 | **3** | **secuencia de Deming**: medir el costo de la inspeccion actual, causa raiz, muestreo aleatorio, redisenar el proceso, reducir gradualmente, reservar el 100% para lo critico. |
| `core/criterios_equity_split` | 8 | 48,3 | 5 | **secuencia de criterios de Wasserman** que continua sin calcarse: aportes pasados, capital, costo de oportunidad, aportes futuros, prima de idea, motivaciones, ajuste por dedicacion y registro escrito. |
| `quality/estratificacion_datos` | 7 | 48,2 | 4 | **secuencia del metodo**, y el *repetir para otras variables* del paso 6 es **iteracion, no re-narracion**. |
| `quality/distorsion_muestreo_mecanico` | 6 | 48,1 | **3** | **secuencia de Deming** sobre el sesgo del instrumento de muestreo, de evaluar el metodo a documentar sus cambios. |
| `core/medir_comportamiento_cliente_mvp` | 6 | 48,1 | **3** | secuencia de metricas de comportamiento sobre el MVP. |
| `core/fase_affirm_buyers_remorse` | 6 | 48,0 | **3** | secuencia unica de la fase Affirm: mapear el periodo de silencio, contacto proactivo, reafirmar la decision, anticipar obstaculos, abrir espacio para dudas y medir cancelaciones. |
| `core/etapa_testing_validation` | 6 | 47,5 | **3** | secuencia de la **Etapa 4** de Cooper. |
| `core/wizard_of_oz_testing` | 6 | 47,4 | **3** | secuencia del metodo Wizard of Oz. |

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

#### LA REGLA DEL CORTE 3 SE ENDURECE, y ahora con cifra

**Era una regla practica sacada de dos casos. Con la tanda nueva ya es un dato
del archivo, y el dato es rotundo:**

> **De las citas leidas con corte 3, van DOS confirmadas de DIECINUEVE.**

| cita | pasos | bloque | pareja | veredicto |
|---|---:|---:|---:|:--:|
| `franquicias/mix_ubicaciones_corporativas_franquicia` | 6 | 51,4 | 58,8 | **falsa** |
| `core/plan_gestion_riesgos` | 6 | 50,3 | **61,9** | **falsa** |
| `quality/matriz_de_seleccion` | 7 | 50,2 | 56,9 | **falsa** |
| `exportacion/internacionalizacion_sitio_web_exportacion` | 9 | 50,1 | 59,9 | **falsa** |
| **`core/empoderamiento_de_participantes`** | **8** | **50,1** | **59,7** | **CONFIRMADA** |
| `franquicias/programa_cumplimiento_legal` | 6 | 49,8 | 54,6 | **falsa** |
| `quality/identificacion_practicas_lideres` | 6 | 49,0 | 54,4 | **falsa** |
| `core/verificar_modelo_ingresos` | 6 | 48,8 | 57,8 | **falsa** |
| `seguridad_digital/csf_funcion_govern` | 7 | 48,5 | 62,0 | **falsa** |
| `quality/desarrollo_caracteristicas_producto` | 6 | 48,3 | 58,1 | **falsa** |
| `quality/abolir_inspeccion_masiva` | 6 | 48,3 | 53,2 | **falsa** |
| `quality/distorsion_muestreo_mecanico` | 6 | 48,1 | 59,1 | **falsa** |
| `core/medir_comportamiento_cliente_mvp` | 6 | 48,1 | 52,6 | **falsa** |
| `core/fase_affirm_buyers_remorse` | 6 | 48,0 | 54,7 | **falsa** |
| `core/etapa_testing_validation` | 6 | 47,5 | 48,9 | **falsa** |
| `core/wizard_of_oz_testing` | 6 | 47,4 | 61,4 | **falsa** |
| `core/metricas_accionables` | 6 | 47,0 | 50,0 | **falsa** |
| `core/ceo_de_guerra_vs_paz` | 6 | 46,7 | 50,5 | **falsa** |
| **`core/cliente_disena_producto`** | **8** | **46,6** | **55,2** | **CONFIRMADA** |
| `core/modelo_spin_preguntas` | 6 | 46,5 | 55,7 | **falsa** |
| `core/publicidad_garantia_conforme` | 6 | 46,0 | 52,6 | **falsa** |
| **`core/estrategia_de_innovacion_producto`** | **7** | **45,7** | **49,6** | **CONFIRMADA** |
| **`core/producto_unico_superior`** | **8** | **44,2** | **55,0** | **CONFIRMADA** |
| `core/definicion_gatekeepers` | 6 | 45,7 | 60,6 | **falsa** |
| `core/plan_gestion_adquisiciones` | 6 | 45,7 | 52,0 | **falsa** |
| `core/retargeting_display` | 6 | 45,6 | 48,6 | **falsa** |
| `core/validar_canal_distribucion` | 6 | 45,4 | 50,0 | **falsa** |
| `core/prototipar_con_medios_no_convencionales` | 6 | 45,3 | 51,4 | **falsa** |
| `core/eventos_offline_como_canal_traccion` | 7 | 45,1 | 52,6 | **falsa** |
| `core/preferencia_de_liquidacion` | 8 | 45,0 | 50,9 | **falsa** |
| `core/portfolio_management` | 6 | 44,7 | 62,1 | **falsa** |
| `core/lectura_balance_general` | 6 | 44,6 | 51,0 | **falsa** |
| `core/product_market_fit` | 6 | 44,2 | 55,8 | **falsa** |

**Los cincuenta y tres cortes y las cincuenta y tres parejas verificados uno por
uno en `docs/COSTURAS_INTERNAS.jsonl` antes de escribir estas cifras.**

> **La regla se mantiene y gana su segunda excepcion:** **una cita de corte 3 no
> es evidencia de costura por si sola.** Cuarenta y nueve de cincuenta y tres han
> caido al abrir los pasos, pero **CUATRO eran costura de verdad**, asi que el corte 3 tampoco
> es un descarte. **Es exactamente lo que la regla decia: hay que abrir los pasos.**
>
> **Y no se puede usar para filtrar la cola**, que sigue siendo la tentacion:
> **53 de las 128 citas tienen corte 3**, el 41% de la cola entera. Las **dos**
> confirmadas leidas son la prueba de que ahi dentro hay costuras reales. **La
> regla es para leer, no para podar.**

#### LA LECTURA FINA POR LONGITUD, y esta vez el archivo SI la sostiene

**La lectura por PAREJA (mas abajo) no separo nada. La lectura por LONGITUD si.**
Con una sola confirmada no habia con que leer fino; con dos, y las dos recontadas
del archivo, aparece una figura que antes no se podia ver: las **dos confirmadas
de corte 3 tienen las dos EXACTAMENTE 8 pasos** (`empoderamiento_de_participantes`
y `cliente_disena_producto`), mientras las falsas se apilan abajo.

| pasos del nodo (con corte 3) | citas | confirmadas |
|---|---:|---:|
| **6 pasos** | 14 | **0** |
| **7 pasos** | 2 | **0** |
| **8 pasos** | **2** | **2** |
| **9 pasos** | 1 | **0** |

> **La lectura que el dato aguanta, y solo la que aguanta**: con corte 3, **en los
> nodos de 6 y 7 pasos la señal es ruido puro (dieciseis falsas de dieciseis)**, y
> **las dos costuras reales viven las dos en nodos de 8 pasos.** El corte 3 dice
> que hay poco material que comparar; **en un nodo corto ese poco no alcanza para
> nada, en uno de 8 pasos ya hay bastante para que una costura asome.** Es la misma
> forma del retrato inverso, vista desde el otro extremo de la escala.

> **La excepcion que impide escribir un *8 o mas* limpio, y se dice**: el unico
> nodo de corte 3 con 9 pasos es `internacionalizacion_sitio_web_exportacion`, y
> es **falsa**, porque es un **formato lista** (nueve mejoras de sitio web, cero
> repeticion). **La regla no es *8 pasos o mas confirma*: es que a corte 3 la
> longitud es el desempate que la señal de bloque no da, y el formato lista sigue
> siendo la excepcion que se reconoce por fuente y titulo antes de abrir los
> pasos.** Con esa salvedad, la regla del corte 3 queda: **nodo corto, ruido; nodo
> de 8 pasos, abre con cuidado que ahi han aparecido las dos presas.**

#### LA LECTURA FINA DEL CORTE 3, y NO sale como se esperaba

**La propuesta era que en la confirmada la senal que la sostiene es la PAREJA de
59,7 y no el bloque, y que la regla pasara a ser *con corte 3, mira la pareja*.**
**Fui a medirlo antes de escribirlo y el archivo no lo sostiene.**

| | |
|---|---|
| pareja **mas alta** de las cincuenta y tres citas de corte 3 | **62,0**, y es de `csf_funcion_govern`, que es **falsa** |
| segunda mas alta | **59,9**, `internacionalizacion_sitio_web_exportacion`, tambien **falsa** |
| la de la primera confirmada | **59,7** (`empoderamiento_de_participantes`), o sea **la tercera**, por debajo de dos falsas |
| la de la segunda confirmada | **55,2** (`cliente_disena_producto`), **mas abajo todavia**, por debajo de varias falsas |

> **La pareja no separa las confirmadas de las falsas en el corte 3, y con la
> segunda confirmada lo deja aun mas claro.** Escrita como regla, *mira la pareja*
> habria mandado leer primero dos falsas y dejar la primera confirmada en tercer
> lugar y la segunda mas abajo. **La longitud si separo (arriba); la pareja no.**
>
> **Ademas, ninguna de las cincuenta y tres dispara por pareja**: el umbral de pareja
> es **80** y la mas alta de este grupo es 62,0. **Todas entraron por bloque.** La
> pareja aqui no es una senal que sostenga nada, es un numero que acompana.
>
> **Lo que si se puede escribir, porque sale del archivo**: **con corte 3 ninguna
> de las dos senales alcanza, y el veredicto lo pone la lectura de los pasos.**
> Es una regla mas pobre que la propuesta, y es la que el dato aguanta.

> **Traigo la discrepancia en vez de escribir la regla dictada.** Si el auditor
> tiene otra medicion de la pareja que yo no vea, la cambio; con esta, no.

#### EL RETRATO INVERSO, y es todavia mas limpio

**Si el corte 3 no distingue nada, el corte ancho distingue casi todo.** Del
archivo, contando las leidas:

> **De las citas leidas con corte 8 o mas, van DIECISIETE confirmadas de
> DIECIOCHO.**
>
> **La racha se rompio en esta tanda, y con un caso que la explica.**

| corte | pasos | cita |
|---:|---:|---|
| **30** | 34 | `core/decision_de_vender_startup` |
| **18** | 22 | `core/producto_minimo_viable` |
| **17** | 30 | `core/viral_loop_marketing` |
| **13** | 17 | `core/lienzo_modelo_negocio` |
| **13** | 17 | `core/blueprint_de_experiencia` |
| **11** | 16 | `quality/planificacion_recoleccion_datos` |
| **11** | 16 | `core/coeficiente_viral` |
| **11** | 14 | `core/metas_vs_proposito` |
| **10** | 19 | `core/actualizacion_posiciones_existentes` |
| **10** | 15 | `core/plan_mejora_procesos` |
| **10** | 15 | `core/ab_testing_optimizacion` |
| **10** | 14 | `core/principio_calidad_mvp` |
| **10** | 13 | `exportacion/elementos_plan_exportacion_ejemplo` **FALSA** |
| **9** | 12 | `core/plan_de_adquisicion_acquire` |
| **8** | 11 | `core/ganar_comprension_del_cliente` |
| **9** | 14 | `core/key_partners_hypothesis` |
| **8** | 13 | `core/future_scenarios_planning` |

**La entrada nueva es una sola, y es la que rompe la racha**:
`elementos_plan_exportacion_ejemplo`, corte 10 en 13 pasos, **falsa**, y en la
tanda siguiente `plan_de_adquisicion_acquire` con corte 9 volvio a confirmar.
**Los cortes altos en nodos largos siguen prediciendo costura quince veces de
dieciseis**, y la unica excepcion es un formato lista.

> **Y la primera falsa por encima de la linea ya llego**:
> `exportacion/elementos_plan_exportacion_ejemplo`, **corte 10 en un nodo de 13
> pasos**, y **falsa**. Antes de ella la falsa de corte mas alto era
> `core/decision_de_salir_a_bolsa` con corte 7.
>
> **La excepcion no rompe el retrato: lo precisa, y el caso dice como.** El nodo
> que la rompe es un **LARGO LEGITIMO**, un checklist de trece elementos de un
> plan de exportacion. **Un checklist largo da muchisimo material que comparar y
> por eso saca corte ancho, sin repetir una sola linea.** Es la misma firma que
> la clase ya tenia descrita.
>
> **La regla queda con su condicion, y es una condicion util porque se puede
> comprobar antes de leer**: **corte 8 o mas predice costura SALVO si el nodo es
> un formato lista.** El formato lista se reconoce por su fuente y su titulo
> antes de abrir los pasos: cuatro de los siete de esa clase salen del mismo
> manual de exportacion.

> **Las dos puntas juntas dan la forma de la señal, y es la que ya se sospechaba
> en la correlacion con el estandar de pasos**: el corte no mide costura, **mide
> cuanto material hay para comparar**. Con tres pasos contra tres no hay material
> y la señal es ruido; con trece contra trece hay tanto que si el nodo repite, se
> ve. **El corte es un termometro de cuanto se puede confiar en el bloque, no de
> cuanta costura hay.**

> **Recomputado tras la banda 46,6 a 47,4, y el retrato NO se movio.** Las seis
> citas de esa tanda tienen cortes 3, 3, 3, 4, 5 y 5: **ninguna llega a corte 8**,
> asi que **el retrato inverso sigue en DIECISEIS confirmadas de DIECISIETE**, sin
> entrada nueva por arriba. Lo que la tanda movio fue el otro extremo de la escala,
> el corte 3, donde por fin aparecieron dos confirmadas y la lectura fina por
> longitud (arriba). **Las dos puntas se leyeron el mismo dia y solo una cambio.**

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

## TANDA DE LA BANDA 50,1 a 50,3: tres confirmadas y tres falsas

**Seis citas leidas de corrido en una banda estrecha de bloque**, y el reparto
sale mitad y mitad. **Las tres confirmadas son las tres del nucleo.**

### `core/project_close_out`, 11 pasos: DOS CIERRES APILADOS

**Bloque 50,3, corte 5.** Y el nodo declara sus dos fuentes: *A Project Manager's
Book of Forms* y *Never Lose a Customer Again*.

| bloque | de que habla |
|---|---|
| **1 a 5** | **el cierre formal PMI**: revisar los objetivos del acta de constitucion, documentar criterios de finalizacion, registrar variaciones, incorporar el cierre de contrato, **obtener las aprobaciones formales** |
| **6 a 11** | **el cierre de metricas y relacion**: revisar los objetivos y metricas del kickoff, evaluacion honesta de cada metrica, feedback del cliente, **atender deficiencias pendientes antes de cerrar**, testimonios mutuos, plan de monitoreo post entrega |

**Lo que se dice dos veces, verificado contra el grafo:**

- **revisar objetivos**: paso 1 (*los objetivos del proyecto definidos en el
  Acta*) y paso 6 (*los objetivos organizacionales y metricas de exito del
  kickoff*).
- **evaluar desviaciones**: paso 3 (*registrar cualquier variacion respecto a los
  objetivos originales*) y paso 7 (*evaluacion honesta del nivel de exito en cada
  metrica*).
- **aprobar antes de cerrar**: paso 5 (*obtener las aprobaciones formales de
  cierre*) y paso 9 (*atender cualquier deficiencia pendiente antes de cerrar*).

> **El corte del instrumento clavo la frontera.** El corte es **5**, y la costura
> esta exactamente entre el paso 5 y el 6. **No es que la señal apuntara cerca:
> apunto al sitio.**

### `core/blueprint_de_experiencia`, 17 pasos: CUATRO PROGRAMAS APILADOS

**Bloque 50,3, corte 13**, y es **la costura mas larga registrada en esta ficha**.

| bloque | de que habla |
|---|---|
| **1 a 4** | **el mapa**: los momentos de la experiencia y su carga emocional |
| **5 a 8** | **la postventa proactiva**: el proceso de despues de la venta y los momentos de ansiedad |
| **9 a 13** | **el ritual del momento de conversion**: la celebracion de cuando el prospecto se vuelve cliente |
| **14 a 17** | **los cien dias**: puntos de contacto, rediseno del traspaso entre vender y dar soporte, responsable por punto |

**El segundo y el cuarto narran el mismo seguimiento proactivo**, con distinta
letra.

> **NOTA PARA EL DESTEJIDO, y cambia el plan de este nodo**: aqui **probablemente
> no sale un nodo, salen DOS**. El blueprint de experiencia es una cosa y **el
> ritual de bienvenida es otra**, con su propio momento y su propio lector. **El
> arreglo de la clase dice una narracion canonica de 3 a 6 pasos**, y aplicado
> aqui a ciegas obligaria a tirar material que no sobra: **lo que sobra es la
> repeticion del seguimiento, no el ritual.**
>
> **Es el primer caso de la clase donde el destejido PARTE en vez de podar.**
>
> **Y ya son CUATRO**: `metas_vs_proposito` (tercer bloque de Coleman pegado a dos
> narraciones de Goodhart), `analisis_tco_roi_b2b` (giro de audiencia de vendedor
> a comprador) y `enfoque_motor_unico_crecimiento` (la misma doctrina con dos
> objetos de dos libros). **Con cuatro ejemplares la forma tiene regla propia en
> el arreglo de la clase, escrita mas abajo.**

### `core/cultura_de_experiencia`, 12 pasos: EL EMPODERAMIENTO DOS VECES

**Bloque 50,2, corte 5.** Dos fuentes otra vez: *Change by Design* y *Never Lose
a Customer Again*.

| tanda | de que habla |
|---|---|
| **1 a 4** | inmersion en el servicio, herramientas inspiracionales, **empoderar a los equipos locales para adaptar la experiencia**, fomentar la improvisacion |
| **5 a 8** | talleres con empleados de distintas areas, **dar autonomia para que propongan sus propias iniciativas**, recoger y priorizar ideas, comunicar el rol de cada uno |
| **9 a 12** | **lo operativo**: diagnosticar si saben que la experiencia es parte de su trabajo, capacitacion peer to peer, unificar las herramientas internas, un simbolo del cliente en las reuniones |

**El empoderamiento esta contado dos veces**, entre la primera y la segunda
tanda: *empoderar a los equipos locales para adaptar* (paso 3) y *dar autonomia
para que propongan sus propias iniciativas* (paso 6).

> **La tercera tanda no repite: anade lo operativo.** Es la parte del nodo que
> sobrevive entera a cualquier destejido.

### Las tres falsas de la tanda

Van a sus clases, que quedan las dos ampliadas y estan arriba con su anatomia:

| cita | pasos | corte | clase |
|---|---:|---:|---|
| `quality/auditoria_calidad_proveedores` | 7 | 4 | **SECUENCIA LEGITIMA** (la clase llega a **cinco**) |
| `quality/matriz_de_seleccion` | 7 | **3** | **SECUENCIA LEGITIMA** |
| `exportacion/internacionalizacion_sitio_web_exportacion` | 9 | **3** | **LARGO LEGITIMO** (la clase llega a **cuatro**) |

---

## TANDA DE LA BANDA 49,7 a 50,1: tres confirmadas y tres falsas

**Otra banda estrecha y otra vez mitad y mitad.** Las tres confirmadas son las
tres del nucleo, igual que en la tanda anterior.

### `core/metas_vs_proposito`, 14 pasos: CONFIRMADA DOBLE, y de la forma blueprint

**Bloque 49,7, corte 11.** El nodo declara **tres fuentes**: *Assembling
Tomorrow*, *The Hard Thing About Hard Things* y *Never Lose a Customer Again*, y
se le notan las tres.

| bloque | de que habla |
|---|---|
| **1 a 4** | **Goodhart, primera narracion**: lista tus metricas, pregunta si representan el proposito, identifica cual se puede hackear (el ejemplo del Q*bert), complementa con indicadores cualitativos |
| **5 a 9** | **Goodhart, segunda narracion**: define el objetivo cualitativo antes de la metrica, pregunta que comportamientos genera, complementa lo cuantitativo con lo cualitativo, no sacrifiques el largo plazo, entiende como se producen los numeros |
| **10 a 14** | **OTRO TEMA PEGADO**: el objetivo que el cliente dice buscar contra su deseo real, el punto de seguimiento posterior al logro aparente, mantener el contacto mas alla del contrato |

**Los dos calcos verificados contra el grafo:**

- **paso 4** (*complementa las metricas con indicadores cualitativos que capturen
  mejor el proposito*) vuelve casi literal en el **paso 7** (*complementa
  metricas cuantitativas con evaluaciones cualitativas*).
- **paso 2** (*pregunta si esta metrica representa el valor y el proposito*)
  vuelve en el **paso 5** (*antes de fijar una metrica, define primero el
  objetivo cualitativo real*).

> **SEGUNDO CASO DE LA FORMA BLUEPRINT: aqui el destejido PARTE en vez de
> podar.** El tercer bloque no es una repeticion de los otros dos: **es otro
> nodo metido dentro**. De aqui salen **dos**: el Goodhart canonico, con sus dos
> narraciones tejidas en una, y **el deseo real del cliente detras del objetivo
> declarado**, que es doctrina de Coleman y merece su propio nodo.
>
> **La forma ya tiene dos ejemplares** (`blueprint_de_experiencia` y este), y
> con dos deja de ser una excepcion: **el arreglo de la clase necesita una regla
> para cuando el nodo costurado contiene un tema ajeno**, no solo para cuando
> repite el propio.

> **Precision sobre el corte, para no darle un merito que no tiene.** En
> `project_close_out` el corte 5 caia exactamente en la frontera (5 contra 6).
> **Aqui no**: el corte es 11 y las fronteras reales estan en 4 contra 5 y en 9
> contra 10. **El corte ancho dice que hay mucho material que comparar, no donde
> esta la costura.** La frontera la puso la lectura.

### `core/schedule_management_plan`, 10 pasos: DOS PLANES DE CRONOGRAMA APILADOS

**Bloque 49,8, corte 5.** Dos fuentes: *A Project Manager's Book of Forms* y
*Essentials of Supply Chain Management*.

| bloque | de que habla |
|---|---|
| **1 a 5** | **el plan PMI**: metodologia de programacion, herramientas, nivel de precision y unidades, umbrales de varianza, procesos para identificar y secuenciar actividades |
| **6 a 10** | **el plan por objetivos con time boxes**: una seccion por objetivo, tareas de diseno y construccion, dependencias, time boxes con input del equipo, ajuste iterativo de tiempo y alcance |

> **Es de la familia de `project_close_out`**, y no por parecido sino por
> genealogia: **los dos salen del mismo formulario del PMI con un segundo libro
> pegado detras**. Cuando el destejido llegue a esta familia conviene mirarla
> entera: **el patron no es de nodo, es de tanda de extraccion.**
>
> **Y aqui el corte SI clava la frontera**: corte 5, costura entre el paso 5 y
> el 6.

### `core/empoderamiento_de_participantes`, 8 pasos: EL EMPODERAMIENTO DOS VECES

**Bloque 50,1, corte 3, pareja 59,7.** Dos fuentes: *Change by Design* y
*Essentials of Supply Chain Management*.

| bloque | de que habla |
|---|---|
| **1 a 4** | **el modelo colmena**: puntos de contacto, autonomia a la primera linea, cambiar guiones rigidos por pensamiento critico, un sistema que evoluciona de miles de interacciones y no de un control central |
| **5 a 8** | **la auto-organizacion**: objetivos comunes, informacion en tiempo real, confiar en la auto-organizacion en vez de microgestionar, comunicacion abierta |

**Los calcos, verificados:** el **paso 2** (*da autonomia para tomar decisiones
en el momento*) y el **paso 7** (*confia en la auto-organizacion en lugar de
microgestionar*) mandan lo mismo; y el **paso 4** (*que el sistema evolucione de
miles de pequenas interacciones, no de un control centralizado*) vuelve a decir
el 7 con otras palabras.

> **Es la gemela en forma de `cultura_de_experiencia`**, la confirmada de la
> tanda anterior: **los dos son nodos de Change by Design con un segundo libro
> pegado, y en los dos lo que se repite es el empoderamiento.**

> **Y es la PRIMERA CONFIRMADA CON CORTE 3.** La regla del corte 3 tiene desde
> hoy su excepcion, y esta registrada abajo con la lectura fina, que no salio
> como se esperaba.

### Las tres falsas de la tanda

| cita | pasos | corte | clase | por que |
|---|---:|---:|---|---|
| `core/decision_de_salir_a_bolsa` | 10 | 7 | **SECUENCIA LEGITIMA** | los pasos 1 a 5 **deciden** si salir a bolsa y los 6 a 10 **preparan** la salida. Continua, no repite |
| `franquicias/programa_cumplimiento_legal` | 6 | **3** | **SECUENCIA LEGITIMA** | secuencia unica de un sistema de cumplimiento: capacitar, designar punto de contacto, registrar comunicaciones, entrevista de cierre, compras de prueba, politica de cero tolerancia |
| `exportacion/elaboracion_pro_forma_invoice` | 8 | 4 | **LARGO LEGITIMO** | **checklist de los campos de un documento**: partes, referencia, productos, volumen y peso, terminos, seguro y flete, declaracion de origen, y marcarlo como Pro Forma |

> **Nota al margen sobre `programa_cumplimiento_legal`**, sin abrirle figura
> nueva: es el mismo nodo que el cribado de la franja ya registro como **pais
> cableado** (franja 1568), porque manda capacitar cada ano en la ley de
> franquicias y hacer compras de prueba **sin condicion de pais**. Aqui sale
> falso **como costura**, que es otra pregunta. **Las dos cosas son ciertas a la
> vez.**

---

## TANDA DE LA BANDA 48,9 a 49,5: cuatro confirmadas y dos falsas

**La primera tanda de banda estrecha que rompe el empate**: cuatro y dos en vez
de tres y tres. **Las cuatro confirmadas son las cuatro del nucleo.**

### `core/actualizacion_posiciones_existentes`, 19 pasos: CUATRO TANDAS

**Bloque 49,0, corte 10.** Dos fuentes: *The Founder's Dilemmas* y *The Hard
Thing About Hard Things*.

| tanda | de que habla |
|---|---|
| **1 a 4** | expectativas desde el inicio, no inflar titulos, evaluar si el empleado escala, comunicar antes de contratar por encima |
| **5 a 10** | **la conversacion de degradacion**: evaluar honestamente, decidir antes de entrar, anticipar la verguenza y la traicion, ofrecer otro rol, lenguaje decisivo, compensacion |
| **11 a 15** | **la evaluacion del ejecutivo**: los roles cambian, evaluar por desempeno actual y no por reputacion, apalancamiento del CEO, si sigue haciendo su trabajo viejo, el equipo antes que la lealtad |
| **16 a 19** | **la evaluacion trimestral**: evaluar cada trimestre, no separar la capacidad de escalar del desempeno, preguntarse si hay alguien mejor hoy, no juzgar el futuro sin datos |

**Los tres calcos, verificados contra el grafo:**

- **3 con 5**: *evaluar objetivamente si un empleado clave puede escalar con las
  nuevas demandas del rol* contra *evaluar honestamente si el empleado leal puede
  crecer con el puesto*.
- **4 con 11**: *comunicar de forma transparente y anticipada cuando se preve
  contratar por encima* contra *comunicar desde el inicio que los roles cambiaran
  conforme la empresa crezca*.
- **12 con 19**: *evaluar a cada ejecutivo segun su desempeno actual, no su
  reputacion pasada* contra *evita juicios sobre el desempeno futuro basados en
  teorias sin datos*. **Es la misma doctrina dicha por sus dos extremos**: juzga
  con el dato de hoy, ni con el pasado ni con la teoria.

> **Entra al top de los destejidos por tamano, y es el CUARTO**: 19 pasos, detras
> de `decision_de_vender_startup` (34), `viral_loop_marketing` (30) y
> `producto_minimo_viable` (22). **De los cuatro mas grandes, tres son de
> personas y equipo**, que es donde el catalogo apilo mas.

### `core/analisis_tco_roi_b2b`, 9 pasos: GIRO DE AUDIENCIA A MITAD DE NODO

**Bloque 48,9, pareja 61,9, corte 6.** Dos fuentes: *The Startup Owner's Manual*
y *Essentials of Supply Chain Management*.

**Es una forma NUEVA dentro de la forma que parte, y es la mas incomoda de las
vistas hasta ahora: el nodo cambia de lector a mitad de camino.**

| bloque | quien eres | que te manda |
|---|---|---|
| **1 a 4** | **el VENDEDOR B2B** | calcular el TCO de adopcion, preparar un ROI hipotetico antes de las reuniones, comparar tu ROI contra la solucion actual **del cliente**, usar el analisis como white paper **en tu proceso de venta** |
| **5 a 9** | **el COMPRADOR** | definir criterios cualitativos, asignar pesos entre costo y calidad (75/25), calcular el costo total ponderado **de cada proveedor**, comparar proveedores, ajustar los pesos |

> **No es una repeticion: es un cambio de silla.** El lector que llega buscando
> como vender su producto a una empresa recibe, en el paso 5, instrucciones para
> ponderar a sus proveedores. **Las dos mitades son utiles y ninguna sobra; lo
> que sobra es que vivan en el mismo nodo.**

> **CONSECUENCIA ESCRITA, y no es poda: la mitad compradora es candidata a
> TRASPLANTE del nucleo a `compras`.** Ahi ya vive esa doctrina, medida en el
> cribado intra-dominio: `matriz_de_seleccion` es el metodo de los cien puntos y
> `decide_criterio_eleccion_proveedor` manda anotar de tres a cinco criterios
> ademas del precio. **El material del paso 5 al 9 pertenece a ese mundo, no al
> nucleo.**
>
> **Y el trasplante tiene condicion**, que se escribe aqui para que no se aplique
> a la ligera: **solo si viaja TEXTO**, con su registro de procedencia. Mover una
> idea sin texto no es trasplante, es reescribir de memoria en otro sitio, y eso
> es exactamente como se produjo la duplicacion que esta campana viene a
> deshacer.

### `core/principio_calidad_mvp`, 14 pasos: TRES NARRACIONES DEL MISMO MVP

**Bloque 49,2, corte 10.** **Tres fuentes y tres narraciones**, una por libro:
*The Lean Startup*, *The Hard Thing About Hard Things* y *Essentials of Supply
Chain Management*.

| bloque | de que habla |
|---|---|
| **1 a 5** | **Ries**: si la caracteristica contribuye al aprendizaje, versiones hacky, no asumir el estandar de la industria, distinguir defecto de baja fidelidad estetica, decidir con el feedback |
| **6 a 10** | resistir la presion del equipo tecnico, distinguir requisitos heredados de necesidades reales, **lanzar lo antes posible aceptando que fallara**, capturar el aprendizaje, iterar con el mercado |
| **11 a 14** | identificar las funcionalidades criticas, excluir las secundarias, **lanzar la solucion minima viable**, iterar con el uso real |

> **Las tres dicen lo mismo: lanza temprano, aprende del cliente real, itera.**
> Cambian los ejemplos, no la doctrina.

> **Es pariente directo del emblema de la clase.** `producto_minimo_viable` tiene
> **22 pasos en cinco narraciones** del mismo asunto y es el caso mas citado de
> esta ficha. **Los dos nodos del MVP estan costurados, y hay que mirarlos
> juntos**: destejer uno sin el otro deja al lector con la misma doctrina
> repetida, solo que repartida en dos sitios.

### `core/enfoque_motor_unico_crecimiento`, 9 pasos: CUARTO CASO DE LA FORMA QUE PARTE

**Bloque 49,5, corte 4.** Dos fuentes: *The Lean Startup* y *Traction*.

| bloque | de que habla |
|---|---|
| **1 a 4** | **el motor de crecimiento** (Ries): identifica tu apuesta de fe, sal a hablar con clientes si no lo tienes claro, concentra desarrollo y metricas en **ese unico motor**, evalua a fondo antes de cambiar |
| **5 a 9** | **el canal Bullseye** (Weinberg): identifica el canal que gana en el anillo medio, redirige **todos** tus recursos a **ese canal principal**, no te distraigas con secundarios, tacticas de apoyo solo si refuerzan, repite Bullseye cuando se sature |

> **La doctrina es UNA, concentrate en uno solo, y los objetos son DOS**, motor y
> canal, cada uno de su libro. **Aqui el destejido parte en dos nodos que se
> apuntan entre si**, no en dos temas ajenos: es la variante mas limpia de la
> forma, y por eso conviene tenerla registrada al lado de las otras tres.

### Las dos falsas de la tanda

| cita | pasos | corte | clase | por que |
|---|---:|---:|---|---|
| `core/contratacion_experiencia_vs_potencial` | 10 | 5 | **SECUENCIA LEGITIMA** | los pasos 1 a 4 eligen el perfil (burn rate, rock star contra rising star, la comprobacion en la entrevista) y los 5 a 10 **afinan el criterio** con la pregunta de conocimiento interno contra externo y sus dos ramas. **Continua, no repite.** |
| `quality/identificacion_practicas_lideres` | 6 | **3** | **SECUENCIA LEGITIMA** | **son DOS foros distintos, no dos narraciones**: el paso 1 es el foro interno de hallazgos y el paso 4 es el foro de intercambio de practicas lideres, con sus presentaciones y sus preguntas recogidas antes. Secuencia de benchmarking. |

> **Con esta, el corte 3 queda en UNA confirmada de SIETE**, y la lectura no
> cambia: ni descarta ni confirma, obliga a abrir los pasos.

---

## TANDA DE LA BANDA 48,5 a 48,8: dos confirmadas, cuatro falsas, y el retrato inverso se rompe

**El reparto se invierte respecto de la tanda anterior**: dos y cuatro donde
antes fue cuatro y dos. Las dos confirmadas son las dos del nucleo.

### CURA CONJUNTA: los DOS mapas del racimo de experiencia se reunen en UNO

**Anadido el 12 ago 2026 desde la relectura R18, puesto 341 del cribado intra.**

> **`blueprint_de_experiencia` y `customer_journey_mapping` estan los dos en esta
> cola, los dos confirmados, y ademas REPITEN ENTRE SI** (puesto 341, clase **A**).
>
> **Y el solape no es cualquiera: es el bloque de mapeo de uno contra el bloque de
> mapeo del otro.** Los dos mandan recorrer el viaje etapa por etapa, identificar
> los puntos de contacto y evaluarlos uno a uno.

**LO QUE ESTO OBLIGA, y es mas fuerte que la cura acoplada normal:**

> **No son dos destejidos que ademas hay que fusionar: es UN SOLO acto con tres
> movimientos.** Destejer los dos, **reunir los dos bloques de mapa en uno**, y
> decidir en cual de los dos nodos vive el mapa resultante.
>
> **Si se destejen por separado quedan DOS mapas** y el par vuelve a aparecer
> exactamente igual que hoy. **El destejido por separado no arregla nada aqui: lo
> aplaza.**

---

### `core/customer_journey_mapping`, 10 pasos: EL MAPEO CONTADO DOS VECES

**Bloque 48,6, corte 7.** Dos fuentes: *Change by Design* y *Never Lose a
Customer Again*.

| bloque | de que habla |
|---|---|
| **1 a 5** | observar al cliente durante toda su experiencia, **documentar cada etapa del viaje**, **identificar los touchpoints**, evaluar cada uno como oportunidad, priorizar por impacto |
| **6 a 10** | **identificar y mapear los distintos journeys** (facturacion, soporte, onboarding), diagnosticar donde los departamentos se pasan la responsabilidad, medir el impacto del mal servicio, la silla vacia, consolidar herramientas |

**El calco, con los dos textos delante para que se pueda juzgar**: el paso 6
(*identificar y mapear los distintos journeys del cliente*) vuelve a mandar el
acto de los pasos 2 y 3 (*documentar cada etapa del viaje* e *identificar todos
los touchpoints*). **Lo que el 6 agrega es la pluralidad de journeys, no un acto
nuevo.**

### HALLAZGO TRANSVERSAL: la familia de experiencia esta costurada Y ENTRELAZADA

**Los tres nodos de experiencia del nucleo estan confirmados como costurados, y
los tres salen de las MISMAS DOS FUENTES**, *Change by Design* y *Never Lose a
Customer Again*:

| nodo | pasos | tanda donde se confirmo |
|---|---:|---|
| `blueprint_de_experiencia` | 17 | banda 50,1 a 50,3 |
| `cultura_de_experiencia` | 12 | banda 50,1 a 50,3 |
| `customer_journey_mapping` | 10 | esta |

**Y no solo cada uno repite por dentro: el material CIRCULA entre los tres.**
Los cruces, verificados contra el grafo uno por uno:

| lo que circula | donde | donde tambien |
|---|---|---|
| **la silla vacia del cliente** | `customer_journey_mapping` paso 9: *colocar una silla vacia representando al cliente en cada reunion interna* | `cultura_de_experiencia` paso 12: *incorporar un simbolo o recordatorio del cliente en las reuniones internas de decision* |
| **la consolidacion de herramientas** | `customer_journey_mapping` paso 10: *consolidar herramientas internas dispersas en un sistema unificado* | `cultura_de_experiencia` paso 11: *unificar las herramientas internas de informacion del cliente* |
| **los touchpoints** | `customer_journey_mapping` pasos 3 y 4: identificarlos y evaluarlos uno a uno | `blueprint_de_experiencia` pasos 14 y 17: listarlos entre la compra y el dia 100 y asignarles responsable |
| **el traspaso entre areas** (cruce que no venia en el encargo y sale de la misma lectura) | `customer_journey_mapping` paso 7: *diagnosticar en que punto los departamentos se pasan la responsabilidad* | `blueprint_de_experiencia` paso 15: *redisena el traspaso entre quien vende y quien da soporte* |

> **RACIMO COSTURADO TRANSVERSAL, y es una forma que esta ficha no tenia.** Las
> costuras registradas hasta hoy eran de un nodo consigo mismo. **Aqui hay tres
> nodos costurados por dentro que ademas se pisan entre si**, con el mismo
> material saltando de uno a otro.

> **REGLA PARA LA PASADA UNICA: los tres se destejen JUNTOS, con un solo reparto
> de material.** Destejer `customer_journey_mapping` por su cuenta dejaria la
> silla vacia y la consolidacion de herramientas en `cultura_de_experiencia`, y
> los touchpoints en `blueprint_de_experiencia`, **sin que nadie sepa cual es la
> copia**. **Nodo por nodo, este racimo no se puede arreglar: se arregla como
> bloque o se mueve el problema de sitio.**
>
> **Y se cruza con la regla de la forma que parte**, porque
> `blueprint_de_experiencia` ya tiene dictado que **se parte en dos** (el
> blueprint y el ritual de bienvenida). **El reparto de material de este racimo
> tiene que decidirse con esa particion ya sobre la mesa**, no despues.

### `core/organizacion_adaptativa`, 8 pasos: EL TIMING DE LA ESTRUCTURA, DOS VECES

**Bloque 48,5, corte 4.** Dos fuentes: *The Lean Startup* y *The Hard Thing
About Hard Things*.

**El calco enmarca el nodo entero**, que es una forma que no se habia visto:

- **paso 1**: *no impongas procesos rigidos desde el inicio; dejalos crecer a
  partir de resolver problemas reales*.
- **paso 8**: *no metas estructura demasiado pronto, porque te vuelves lento, ni
  demasiado tarde, porque colapsas bajo presion*.

> **El mismo mandato abre y cierra el nodo**, y los pasos 2 a 7 quedan dentro
> como el desarrollo. **No es una tanda pegada detras de otra: es una narracion
> que se repite a si misma en sus dos extremos.** Para el destejido es el caso
> mas barato de la clase: sobra uno de los dos, y el resto del nodo esta sano.

### Las cuatro falsas de la tanda

| cita | pasos | corte | clase | por que |
|---|---:|---:|---|---|
| `exportacion/elementos_plan_exportacion_ejemplo` | 13 | **10** | **LARGO LEGITIMO** | **trece elementos distintos de un plan de exportacion**: introduccion, metas medibles, recursos financieros y no financieros, capacidad, mercados, politica de riesgo, agente de carga y licencias, idioma del etiquetado, codigo arancelario, propiedad intelectual, precios y sitio web. **Ninguno repite a otro.** |
| `core/background_startup_vs_corporativo` | 9 | 4 | **LARGO LEGITIMO** | **nueve criterios distintos de entrevista** para decidir entre experiencia de startup y de corporativo. Lista de criterios, no narracion. |
| `core/verificar_modelo_ingresos` | 6 | **3** | **SECUENCIA LEGITIMA** | secuencia unica de calculo: recopilar datos, ingreso bruto, ingreso neto de canal, restar costos, tres escenarios, evaluar el cash burn. **Cada paso necesita al anterior.** |
| `seguridad_digital/csf_funcion_govern` | 7 | **3** | **SECUENCIA LEGITIMA** | secuencia unica de la funcion Govern del NIST CSF 2.0: mision y riesgos, requisitos aplicables, responsable, impacto de perder activos, seguro, terceros, comunicar politicas. |

> **Verificado antes de escribirlo, con la leccion de Magnuson-Moss aplicada**:
> `csf_funcion_govern` **no lleva condicion de pais** en sus
> `condiciones_activacion`, asi que su marco NIST **si** es material del caso a
> escala de mundo de `seguridad_digital`, no un contramodelo. No se le abre
> figura aqui porque esa ya esta registrada en su ficha.

> **Nota sobre `background_startup_vs_corporativo`, que no se adjudica aqui**:
> es vecino gemelo de `contratacion_experiencia_vs_potencial`, la falsa de la
> tanda anterior, y los dos salen de las mismas dos fuentes. **El cribado
> intra-dominio lo cazara por su via**, que es donde se juzgan dos nodos entre
> si. Aqui solo se dice que como COSTURA es falso.

---

## TANDA DE LA BANDA 48,1 a 48,3: una confirmada y cinco falsas

**El peor rendimiento de las cinco tandas de banda estrecha**, y con un reparto
por dominio que se explica solo: la unica confirmada es del nucleo y **cuatro de
las cinco falsas son de `quality`**.

### `core/plan_de_adquisicion_acquire`, 12 pasos: QUINTA DE LA FORMA QUE PARTE

**Bloque 48,3, corte 9.** Dos fuentes: *The Startup Owner's Manual* y
*Traction*.

| bloque | de que habla |
|---|---|
| **1 a 7** | **el Acquire Plan de Blank**: revisar las hipotesis del modelo, definir por actividad quien, que tactica, cuanto presupuesto y que metrica, fijar el pasa o falla antes de cada prueba, instrumentar el sitio, lanzar escalonado, limitar el gasto por prueba, y dejar lista la plomeria de activacion |
| **8 a 12** | **el programa Bullseye de Weinberg, entero**: listar los 19 canales de traccion, disenar una prueba barata por canal, correrlas y medir resultados concretos, comparar entre canales y elegir, y anotar lo aprendido incluso de las que fallaron |

> **No es repeticion, es un programa ajeno pegado detras**, que es la firma de
> la forma que parte. **Quinto ejemplar**, detras de `blueprint_de_experiencia`,
> `metas_vs_proposito`, `analisis_tco_roi_b2b` y
> `enfoque_motor_unico_crecimiento`.

### RACIMO COSTURADO TRANSVERSAL NUMERO DOS: el Bullseye pegado en dos sitios

**El cruce, verificado contra el grafo, y sale mas fuerte de lo que el encargo
suponia.** El programa Bullseye de *Traction* esta pegado en **dos** nodos del
nucleo, **y cada uno se quedo con una mitad distinta**:

| nodo | que mitad del Bullseye lleva | pasos |
|---|---|---|
| `plan_de_adquisicion_acquire` | **la mitad de PRUEBA**: listar los 19 canales, disenar una prueba barata por canal, correrlas, comparar y anotar | 8 a 12 |
| `enfoque_motor_unico_crecimiento` | **la mitad de ELECCION**: identificar el canal que gana en el anillo medio, redirigir todos los recursos, no distraerse con secundarios, y repetir Bullseye cuando se sature | 5 a 9 |

> **Ninguno de los dos tiene el Bullseye completo, y entre los dos si.** El
> primero prueba y no dice que hacer con el ganador mas alla de invertirle mas;
> el segundo elige y concentra pero da por hecha la prueba. **Un lector que
> reciba solo uno se queda con medio programa sin saberlo.**

> **REGLA PARA LA PASADA UNICA: los dos se destejen JUNTOS, con un solo reparto,
> y la salida probable es un NODO BULLSEYE PROPIO que los dos citen.** Aqui la
> particion no es una opcion entre otras: **el material extraido de los dos es
> exactamente un programa completo**, asi que el nodo nuevo no hay que
> inventarlo, hay que reunirlo.
>
> **Y hay una diferencia con el racimo transversal numero uno**, el de la
> familia de experiencia: alli el material se repetia entre los tres nodos y el
> reparto era para decidir **cual es la copia**. **Aqui el material NO se repite:
> se complementa**, y el reparto es para decidir **donde vive el original**. Son
> dos problemas distintos con la misma cirugia.

### Las cinco falsas de la tanda

| cita | pasos | corte | por que es SECUENCIA LEGITIMA |
|---|---:|---:|---|
| `quality/desarrollo_caracteristicas_producto` | 6 | **3** | el Paso 4 del Quality by Design de Juran en secuencia unica: agrupar necesidades, elegir metodos de identificacion, aplicar tecnicas creativas, verificar regulaciones, seleccionar caracteristicas de alto nivel y detallarlas |
| `quality/abolir_inspeccion_masiva` | 6 | **3** | secuencia de Deming: medir el costo de la inspeccion actual, analizar causa raiz, pasar a muestreo aleatorio, redisenar el proceso, reducir gradualmente y reservar el 100% para lo critico |
| `quality/estratificacion_datos` | 7 | 4 | secuencia del metodo: elegir variables, establecer categorias, clasificar, calcular, graficar, **repetir para otras variables** y planificar confirmacion. **El repetir del paso 6 es ITERACION del metodo, no una segunda narracion** |
| `quality/distorsion_muestreo_mecanico` | 6 | **3** | secuencia de Deming sobre el sesgo del instrumento de muestreo: evaluar el metodo, calibrar el sesgo, pasar a numeros aleatorios, alternativa si no se puede, registrar las caracteristicas y documentar los cambios |
| `core/criterios_equity_split` | 8 | 5 | secuencia de criterios de Wasserman que **continua sin calcarse**: aportes pasados, capital, costo de oportunidad, aportes futuros, prima de idea, motivaciones, ajuste por dedicacion y registro escrito |

> **Nota sobre `desarrollo_caracteristicas_producto`, que no se adjudica aqui**:
> es el id base de una pareja de sufijo y de la familia D4 de
> `desarrollar_caracteristicas_producto`. **Como COSTURA es falso**, que es la
> pregunta de esta ficha. Lo otro le toca a la familia.

> **Nota sobre `criterios_equity_split`, y es un caso util de las dos preguntas
> a la vez**: como costura es **falso**, y al mismo tiempo el cribado
> intra-dominio ya lo clasifico como **A REPITE** en su puesto 188, porque
> `split_igual_vs_desigual` es su version corta. **Un nodo puede estar limpio
> por dentro y tener un gemelo fuera.** Las dos cosas son ciertas y ninguna
> corrige a la otra.

---

## LA FORMA REPARTIDA, espejo de la forma que parte

**Nace de una correccion.** El encargo de la banda 48,1 daba por hecho que el
Bullseye estaba **repetido** en dos nodos; al verificarlo contra el grafo salio
que estaba **repartido**, cada nodo con una mitad distinta. La diferencia no era
de matiz: **cambia la cirugia**, asi que la forma se nombra aparte.

| | LA FORMA QUE PARTE | LA FORMA REPARTIDA |
|---|---|---|
| **que pasa** | **un nodo lleva dos temas** | **un tema vive partido en dos nodos** |
| **la cirugia** | **separar** | **reunir** |
| **que decide el reparto** | **cual de los dos temas se queda** | **donde vive el original** |
| **el material** | sobra donde esta | **no sobra en ninguno de los dos: falta en los dos** |
| **ejemplares** | **ocho**: `blueprint_de_experiencia`, `metas_vs_proposito`, `analisis_tco_roi_b2b`, `enfoque_motor_unico_crecimiento`, `plan_de_adquisicion_acquire`, `ganar_comprension_del_cliente`, `mapa_de_canal_de_ventas`, `asociaciones_clave` | **uno**: el Bullseye entre `enfoque_motor_unico_crecimiento` y `plan_de_adquisicion_acquire` |

> **El ejemplar medido, para que la forma no quede en abstracto**:
> `plan_de_adquisicion_acquire` tiene la mitad de PRUEBA del Bullseye (listar los
> 19 canales, probar cada uno, comparar) y `enfoque_motor_unico_crecimiento`
> tiene la mitad de ELECCION (identificar el ganador del anillo medio,
> concentrar todo, repetir al saturarse). **Ninguno de los dos sirve solo.**

> **Y hay un nodo que esta en las dos formas a la vez**:
> `enfoque_motor_unico_crecimiento` **parte** (motor de Ries mas canal de
> Weinberg) **y ademas esta repartido** (su mitad de canal es media Bullseye).
> **Eso no es una contradiccion: es lo que pasa cuando el pegado se hizo dos
> veces sobre el mismo nodo.** La pasada unica lo tiene que abrir una sola vez y
> resolver las dos cosas en el mismo acto.

---

## TANDA DE LA BANDA 47,4 a 48,1: dos confirmadas y cuatro falsas, todas del nucleo

**Primera tanda con el orden nuevo aplicado**: las seis citas son del nucleo.

### `core/ganar_comprension_del_cliente`, 11 pasos: SEXTA DE LA FORMA QUE PARTE

**Bloque 48,0, corte 8.** Dos fuentes: *The Startup Owner's Manual* y *Never
Lose a Customer Again*.

| bloque | de que habla |
|---|---|
| **1 a 6** | **investigacion etnografica**: el flujo de trabajo del cliente, que otras soluciones usa, que cambiaria su compra, **pasar un dia haciendo lo que el hace**, que publicaciones lee, documentar con criterio de validado |
| **7 a 11** | **un programa de CRM completo**: elegir la herramienta, definir de 5 a 10 datos prioritarios, completar lo que ya sabes, investigar perfiles publicos, priorizar datos personales y emocionales |

> **Precision sobre el corte, con la misma disciplina de siempre**: el encargo
> dice que el corte clava la frontera y **no la clava**. El corte es **8** y la
> frontera esta en **6 contra 7**. Es el mismo caso de `metas_vs_proposito`: el
> corte ancho dice que hay mucho material que comparar, **no donde esta la
> costura**. Donde el corte si clavo fue en `project_close_out` y en
> `schedule_management_plan`, los dos con corte 5 y frontera en 5 contra 6.

### `core/modelo_hibrido_agile_stage_gate`, 13 pasos: DOBLE DEL CICLO ITERATIVO

**Bloque 48,1, corte 7.** Dos fuentes: *Winning at New Products* y *Essentials
of Supply Chain Management*.

| bloque | de que habla |
|---|---|
| **1 a 9** | **el hibrido Agile-Stage-Gate de Cooper**: mantener las compuertas Go/Kill, insertar sprints de 1 a 4 semanas, reuniones diarias, **entregable tangible al final de cada sprint**, tableros y backlog, revisiones con interesados, equipo dedicado, expandir a etapas tempranas |
| **10 a 13** | **el ciclo generico vision e hitos**: definir la vision de largo plazo, dividir en hitos de 30, 60 y 90 dias, **entregar una version funcional al final de cada ciclo** y ajustar el plan siguiente con lo aprendido |

**El calco, con los dos textos delante**: el paso **4** (*definir un entregable
tangible y demostrable al final de cada sprint*) vuelve en el paso **12**
(*entregar una version funcional al final de cada ciclo, por minima que sea*).
**Es la misma instruccion con el vocabulario del otro libro.**

### Las cuatro falsas, todas corte 3 y todas SECUENCIA LEGITIMA

| cita | pasos | por que |
|---|---:|---|
| `core/fase_affirm_buyers_remorse` | 6 | secuencia unica de la fase Affirm: mapear el periodo de silencio, disenar el contacto proactivo, redactar la reafirmacion, anticipar obstaculos, abrir espacio para dudas y medir cancelaciones |
| `core/etapa_testing_validation` | 6 | secuencia de la Etapa 4 de Cooper |
| `core/medir_comportamiento_cliente_mvp` | 6 | secuencia de metricas de comportamiento sobre el MVP |
| `core/wizard_of_oz_testing` | 6 | secuencia del metodo Wizard of Oz |

> **Nota C2 sobre `etapa_testing_validation`, anotada SIN CENSAR**: su titulo
> lleva **Etapa 4**, y podria ser la primera vista de una serie numerada de
> Cooper dentro del nucleo, como los Paso N de Crosby y los Punto N de Deming en
> `quality`. **Una vista no es un censo**, asi que aqui solo queda la anotacion.
> **El barrido intra-dominio es quien la mira.**

### `fase_affirm_buyers_remorse` es el CUARTO VERTICE del racimo transversal uno

**Sana como costura, y aun asi cambia el plan del racimo de experiencia.** El
solape, verificado contra el grafo:

| `fase_affirm_buyers_remorse` | `blueprint_de_experiencia`, bloque 5 a 8 |
|---|---|
| paso 1: **mapea cuanto dura el periodo de silencio** entre la compra y el primer uso | paso 5: documenta el proceso actual de atencion postventa, paso a paso |
| paso 2: **disena al menos un punto de contacto proactivo durante ese periodo** | paso 6: identifica los momentos de mayor ansiedad **y disena acciones proactivas para esos momentos** |
| paso 5: crea un espacio explicito donde el cliente exprese dudas | paso 7: **establece seguimientos programados sin esperar a que tu cliente se queje** |

> **El bloque 5 a 8 del blueprint es el tema de `fase_affirm`**, escrito otra vez
> y en otro nodo. **La diferencia con los otros tres vertices es importante:
> `fase_affirm` NO esta costurado. Es el nodo sano al que le duplicaron el
> tema.**

> **REGLA QUE ESTO ANADE AL RACIMO TRANSVERSAL NUMERO UNO**: el reparto del
> destejido conjunto **tiene que mirar a `fase_affirm_buyers_remorse` como
> DESTINO EXISTENTE antes de crear nada**. El bloque de postventa proactiva del
> blueprint **no necesita un nodo nuevo: ya tiene casa**. **Crear uno seria
> fabricar el quinto vertice del mismo racimo mientras se destejen los otros
> cuatro.**
>
> Con esto el racimo transversal uno pasa a tener **cuatro vertices**:
> `blueprint_de_experiencia`, `cultura_de_experiencia`, `customer_journey_mapping`
> (los tres costurados) y **`fase_affirm_buyers_remorse`, sano y destino**.

---

## TANDA DE LA BANDA 46,6 a 47,4: tres confirmadas y tres falsas, todas del nucleo

**Segunda tanda con el orden nuevo, y repite la firma de la primera**: las seis
citas son del nucleo, las tres confirmadas de `core` y las tres falsas tambien.
**Es la banda mas baja leida hasta hoy**, pegada al umbral 44, y aun asi el
nucleo pone tres presas.

### `core/cliente_disena_producto`, 8 pasos, corte 3: DOBLE, y SEGUNDA CONFIRMADA DE CORTE 3

**Bloque 46,6, pareja 55,2 sobre [1,5], corte 3.** Dos fuentes: *Winning at New
Products* de Cooper y *Never Lose a Customer Again* de Coleman.

| bloque | de que habla |
|---|---|
| **1 a 4** | **la herramienta de co-diseno de Cooper**: evaluar si el cliente entiende la tecnologia, montar una herramienta digital tipo CAD para que cree sus propios disenos, abrir una galeria o comunidad donde los compartan, revisar esos disenos para sacar ideas de nuevos productos |
| **5 a 8** | **la co-creacion como experiencia de Coleman**: identificar donde el cliente puede personalizar, disenar un proceso guiado que no lo abrume, **entregarle algo tangible o simbolico que represente su decision**, mostrar de forma visible lo que logro |

**El calco verificado contra el grafo**: el **paso 1** (*evalua si tu producto es
apto: tu cliente debe poder entender la tecnologia que hay detras*) y el **paso
5** (*identifica en que partes de tu producto tu cliente puede tomar decisiones
de personalizacion*) hacen la misma pregunta de aptitud para la co-creacion, una
por el lado tecnico y otra por el lado del alcance. Es la pareja [1,5] que el
instrumento disparo.

> **Precision sobre el corte, con la disciplina de siempre**: el corte es **3** y
> la frontera real entre las dos narraciones esta en **4 contra 5** (Cooper cierra
> en el 4, Coleman abre en el 5). **Se queda a un paso**, como
> `ganar_comprension_del_cliente`. El corte 3 dice que hay poco material que
> comparar, no donde esta la costura: la frontera la puso la lectura.

> **EL CRUCE AL RACIMO TRANSVERSAL DE EXPERIENCIA, verificado contra el grafo.**
> El **paso 7** (*entregale algo tangible o simbolico que represente la decision
> que tomo*) es el mismo material del ritual de bienvenida de Coleman que ya vive
> en `blueprint_de_experiencia` **paso 11** (*crea un recuerdo fisico o digital
> que tu cliente pueda conservar de la decision que tomo*). **Las dos frases
> mandan lo mismo**: dar al cliente un objeto que represente la decision que acaba
> de tomar.

> **Nota del ejecutor sobre el conteo, traida en vez de escrita redonda**: el
> encargo llama a este cruce el *quinto avistamiento del material del ritual*. **La
> ficha no lleva una serie numerada de avistamientos de ese material**, asi que el
> ordinal *quinto* no lo puedo reconstruir del archivo ni lo repito como cifra. Lo
> verificado y lo que se registra es el cruce en si: `cliente_disena_producto`
> paso 7 contra `blueprint_de_experiencia` paso 11, la misma instruccion de
> entregar un objeto de la decision. Si el auditor lleva ese conteo aparte, el
> ordinal es suyo; con lo que hay en la ficha, se registra el cruce sin numerarlo.

> **CONSECUENCIA PARA EL RACIMO TRANSVERSAL UNO**: el bloque del ritual de
> `blueprint_de_experiencia` (pasos 9 a 13) ya tiene dictado que **se parte en un
> nodo propio, el ritual de bienvenida**. El material del ritual de
> `cliente_disena_producto` (pasos 7 y 8) **es de esa misma casa**: cuando la
> pasada unica arme el nodo del ritual, este par de pasos es suyo, no de un nodo
> nuevo. Es la misma leccion que dejo `fase_affirm_buyers_remorse`: **mirar el
> destino existente antes de crear nada.**

### `core/mapa_de_canal_de_ventas`, 8 pasos, corte 5: SEPTIMA DE LA FORMA QUE PARTE

**Bloque 47,4, corte 5.** Dos fuentes: *The Startup Owner's Manual* de Blank y
*Essentials of Supply Chain Management* de Hugos.

| bloque | de que habla |
|---|---|
| **1 a 5** | **la food chain de canal de Blank**: validar un solo canal antes de expandir, dibujar la cadena completa entre tu empresa y el cliente final, documentar la responsabilidad de cada eslabon, calcular descuentos y margenes por nivel, disenar un plan de gestion del canal |
| **6 a 8** | **medio mapa SCM de Hugos**: identificar en que categoria participa tu empresa, mapear todos los participantes de la cadena de suministro incluyendo proveedores del proveedor y clientes del cliente, ver que proveedores de servicios mejorarian la eficiencia |

> **No es repeticion, es un programa ajeno pegado detras**, la firma de la forma
> que parte. **Septimo ejemplar**, detras de `blueprint_de_experiencia`,
> `metas_vs_proposito`, `analisis_tco_roi_b2b`, `enfoque_motor_unico_crecimiento`,
> `plan_de_adquisicion_acquire` y `ganar_comprension_del_cliente`. **Y aqui el
> corte SI clava la frontera**: es 5, y la costura esta exactamente entre el paso
> 5 y el 6.

> **NOTA DE REPARTO, verificada contra el grafo**: la mitad de Hugos (pasos 6 a 8)
> no es material suelto. **Sale de *Essentials of Supply Chain Management*, y ese
> libro tiene parientes en el bloque Hugos del nucleo**, la subfamilia Hugos
> registrada mas abajo en esta ficha. Cuando la pasada unica separe este nodo, la
> mitad SCM no se desteje sola: **se reparte con esa subfamilia**, que es donde
> vive su tema. La mitad de Blank se queda como el mapa de canal que el titulo
> promete. **Es medio mapa** porque son tres pasos, un SCM abreviado, no el mapa
> entero.

### `core/seleccion_ceo_fundador`, 12 pasos, corte 5: DOBLE DE LA DECISION DE CEO

**Bloque 46,8, corte 5.** Dos fuentes: *The Founder's Dilemmas* y *The Hard Thing
About Hard Things* de Horowitz.

| bloque | de que habla |
|---|---|
| **1 a 4** | **la decision en grupo (Founder's Dilemmas)**: reunir al equipo fundador para discutir quien debe ser CEO sin dar por hecho que es quien tuvo la idea, evaluar candidatos por ejecucion y no por pasion, considerar roles alternativos para el fundador (Chairman, CTO, CSO), documentar el acuerdo formalmente |
| **5 a 8** | **la decision introspectiva (Horowitz)**: evaluar si tu tienes la vision de producto para seguir liderando, identificar tus brechas de habilidades de CEO, buscar mentores con experiencia real fundando, y si no quieres el puesto encontrar al CEO profesional adecuado e integrarlo |
| **9 a 12** | **la integracion, que CONTINUA sin calcarse**: evaluar si tu equipo directivo conoce el producto, negociar clausulas de control antes de aceptar inversion, transicion gradual si contratas un CEO externo, detectar senales tempranas de desalineacion |

**El doble, verificado contra el grafo**: la tanda grupal (1 a 4) y la
introspectiva (5 a 8) **responden la misma pregunta**, quien debe ser el CEO y
que pasa si no es el fundador, una desde la mesa del equipo y otra desde el
espejo. El **paso 2** (*evalua a los candidatos por su capacidad de ejecucion, no
por pasion*) vuelve en el **paso 6** (*identifica tus brechas de habilidades de
CEO*); el **paso 3** (*considera roles alternativos para la persona con la idea*)
vuelve en el **paso 8** (*si no quieres ser CEO, encuentra al profesional
adecuado e integralo*). **La tercera tanda no repite: gestiona al CEO ya elegido.**

> **Precision sobre el corte**: el corte es **5** (frontera propuesta entre el
> paso 5 y el 6) y la frontera real del doble esta en **4 contra 5**, donde la
> tanda grupal cierra y la introspectiva abre. **Se queda a un paso**, esta vez por
> el lado tardio: mete el primer paso introspectivo en el bloque del grupo.

### Las tres falsas de la tanda, todas SECUENCIA LEGITIMA

| cita | pasos | corte | por que es SECUENCIA LEGITIMA |
|---|---:|---:|---|
| `core/metricas_accionables` | 6 | **3** | secuencia unica de Ries, accionables contra vanidad: evitar numeros brutos acumulativos, exigir que cada metrica trace la accion que la causo, disenar la relacion causal, pasar a cohortes, eliminar lo que no traza y validar que sea comprensible. **Cada paso afina el anterior, ninguno lo repite.** La pareja [3,6] son dos criterios distintos que comparten el sujeto *metrica* |
| `core/cap_table_basico` | 7 | 4 | secuencia unica de *Venture Deals* para armar un cap table: listar acciones de fundador, pre y post money, porcentaje del inversionista, restar el option pool, resolver lo que falta con algebra y verificar los calculos. La pareja [5,6] son **dos vecinos legitimos: resolver y luego verificar** |
| `core/ceo_de_guerra_vs_paz` | 6 | **3** | secuencia unica de Horowitz: evaluar si el negocio esta en modo normal o existencial, actuar segun guerra o paz, delegar la tactica manteniendo la direccion, y **revisar periodicamente si el contexto cambio de modo**. La pareja [1,6] son los dos vecinos del marco, evaluar ahora y reevaluar despues, como en `plan_gestion_riesgos` |

> **Estas tres mueven la regla del corte 3, y la mueven arriba en la ficha**:
> `cliente_disena_producto` es la SEGUNDA confirmada de corte 3, y
> `metricas_accionables` y `ceo_de_guerra_vs_paz` son dos falsas mas de corte 3.
> La cuenta recomputada del archivo pasa a **dos confirmadas de diecinueve**, y la
> tabla de la regla queda actualizada en su seccion, con la lectura fina que la
> nueva pareja de confirmadas permite escribir.

---

## TANDA DE LA BANDA 45,9 a 46,5: cuatro confirmadas y dos falsas

**La mejor tanda desde que empezo la banda estrecha**, y las seis del nucleo.

### `core/asociaciones_clave`, 12 pasos: TRES BLOQUES DE DOS LIBROS

**Bloque 46,5, corte 8.** Y la fuente **declara tres entradas para dos libros**:
*Business Model Generation* y **`Essentials of Supply Chain Management` DOS
VECES**, una con el titulo completo y otra truncada como
*Essentials of Supply Chain Mana*. **El mismo libro entro dos veces en el campo
de fuente**, que es la huella de dos extracciones distintas sobre el mismo nodo.

| bloque | de que habla | de que libro |
|---|---|---|
| **1 a 4** | **el Canvas puro**: que recursos obtener de terceros, clasificar alianzas por tipo, definir la motivacion, formalizar acuerdos | Osterwalder |
| **5 a 8** | **la jugada de retail con fabricantes**: detectar tendencias emergentes, identificar fabricantes alineados, negociar compras anticipadas por suministro preferencial, incentivar a la fuerza de ventas | Hugos |
| **9 a 12** | **las alianzas profundas**: oferta personalizada, KPIs conjuntos, horizonte de 3 a 5 anos, reparto de beneficios | Hugos |

> **Octava de la forma que parte**, con la salvedad de numeracion de abajo.

> **Precision sobre el corte, y esta vez no es un no rotundo.** El encargo dice
> que el corte 8 clava la frontera 4 contra 5. **El corte vale 8 y la frontera
> esta en 4**, asi que por el criterio que esta ficha viene usando (corte igual a
> posicion de la frontera, como en `project_close_out` y
> `schedule_management_plan`, los dos con corte 5 y frontera 5 contra 6) **no
> clava**. **Pero hay una aritmetica que si acierta**: 12 pasos menos corte 8 son
> exactamente 4. **No la registro como regla**, porque esa misma resta falla en
> `project_close_out` (11 menos 5 son 6, y su frontera esta en 5). **Queda la
> coincidencia anotada y sin mecanismo declarado**, que es lo unico que el dato
> aguanta.

### `core/reduccion_tamano_de_lote_batch_size`, 9 pasos: EL MANDATO A DOS VOCES

**Bloque 46,0, corte 5.** *The Lean Startup* y *Essentials of Supply Chain
Management*.

| bloque | voz | que manda |
|---|---|---|
| **1 a 5** | **voz de producto** (Ries) | equipos pequenos multifuncionales, ciclos cortos en vez de plan anual, clientes reales desde el inicio, infraestructura para probar sin riesgo, medir NPS antes y despues |
| **6 a 9** | **voz de transformacion** (Hugos) | dividir la transformacion en proyectos pequenos, reutilizar lo existente antes de reemplazar, **time boxes estrictos**, evaluar y ajustar tras cada paso |

**El mismo mandato dos veces con dos vocabularios**: haz los lotes pequenos y
evalua entre uno y otro.

> **CRUCE VERIFICADO con `schedule_management_plan`**: el paso 8 de este nodo
> (*define entregables cortos con time boxes estrictos de diseno y
> construccion*) y el paso 9 de aquel (*asignar time boxes a cada tarea con input
> del equipo ejecutor*) son **el mismo material del mismo libro**. Los dos nodos
> declaran a Hugos entre sus fuentes.

### `core/sistema_inmune_producto`, 9 pasos: EL MANDATO INMUNE DOBLADO

**Bloque 45,9, corte 4.** *The Lean Startup* y *Never Lose a Customer Again*.

| bloque | de que habla |
|---|---|
| **1 a 5** | **despliegues**: metricas criticas monitoreadas, pruebas automatizadas por despliegue, alertas, reversion automatica, bloquear despliegues hasta la causa raiz |
| **6 a 9** | **soporte**: puntos de friccion que generan llamadas, deteccion proactiva con aviso al cliente, autoservicio y autosanacion, medir lo resuelto sin intervencion humana |

> **Es una RE-CONFIRMACION POR OTRA VIA**: este nodo ya estaba registrado como
> costura en el informe de la franja (franja 803, nueve pasos en dos bloques),
> encontrado leyendo pares mundo contra nucleo. **La cola del instrumento llega
> al mismo nodo por su cuenta y con el mismo veredicto.**

### `core/sales_funnel_get_keep_grow`, 10 pasos: CONFIRMADA, y la condicion no se activo

**Bloque 45,9, corte 6.**

| bloque | de que habla |
|---|---|
| **1 a 4** | **el embudo Get / Keep / Grow**: mapear Get, disenar Keep, disenar Grow, medir conversion por etapa |
| **5 a 10** | **el sistema operativo de leads**: generar leads por marketing antes de vender, calificar en A, B y C por horizonte de cierre, dar el 66 al 75% del tiempo a los A, delegar los C a marketing, coordinar collateral, y pedir compromiso explicito con timeline |

> **La condicion del encargo NO se activo, y se verifico antes de registrar.** El
> encargo mandaba degradarla si **las dos mitades salian del mismo libro de
> Blank**. La fuente declarada del nodo es **`The Startup Owner's Manual` de
> Blank Y `Traction` de Weinberg**: dos libros distintos. **Se registra
> confirmada.**
>
> **El limite de esa verificacion, dicho para que nadie lo estire**: el campo
> `fuente` lista los dos libros **sin decir que mitad viene de cual**. Lo
> verificado es que el nodo declara dos libros, no que el bloque 5 a 10 sea de
> Weinberg. **Si el auditor tiene esa atribucion por otra via, la condicion
> vuelve a estar sobre la mesa.**

### Las dos falsas

| cita | pasos | corte | clase |
|---|---:|---:|---|
| `core/modelo_spin_preguntas` | 6 | **3** | **SECUENCIA LEGITIMA**: la secuencia SPIN entera, situacion, problema, implicacion y necesidad-beneficio, mas el ajuste de ritmo y el momento de presentar |
| `core/publicidad_garantia_conforme` | 6 | **3** | **SECUENCIA LEGITIMA**: la secuencia de la guia de publicidad de garantias, de revisar el material a consultar al abogado |

> **`publicidad_garantia_conforme` SI condiciona por pais**, verificado hoy con
> la leccion de Magnuson aplicada. Su primera `condiciones_activacion` es
> *vendes, o piensas vender, productos a clientes en Estados Unidos*, y ademas
> condiciona por el uso de la palabra *lifetime* y por el umbral de los 15
> dolares. **Es el SEXTO miembro del bloque contramodelo de la familia
> Magnuson-Moss**, y queda registrado en la ficha de marco-pais de
> `docs/PENDIENTES.md`.

---

## EL HALLAZGO QUE REORDENA EL FRENTE: la costura es la juntura entre DOS LIBROS

**Sale de verificar las fuentes de esta tanda y de contarlas despues en todo lo
leido.** Es la explicacion mas simple que ha tenido esta clase, y es
comprobable **sin abrir un solo paso**.

| | con DOS o mas fuentes declaradas | con UNA sola |
|---|---:|---:|
| **las 35 CONFIRMADAS** | **32** (91%) | 3 |
| **las 29 FALSAS** | **3** (10%) | 26 |
| las 128 citas del instrumento | 47 (37%) | 81 |

> **Una costura confirmada declara dos libros nueve veces de cada diez. Una
> falsa, una vez de cada diez.** El numero de fuentes del nodo **separa las dos
> clases mucho mejor que el corte o el bloque**, que son las dos senales con las
> que se construyo la cola.

**Y tiene sentido con todo lo demas que esta ficha ya escribio**: la forma que
parte, la forma repartida y los dos racimos transversales **son todos el mismo
fenomeno visto de cerca**. Cuando una segunda extraccion pego material de otro
libro sobre un nodo que ya existia, quedaron la costura, el tema ajeno, la mitad
huerfana y el material circulando entre vecinos. **La juntura entre libros es el
mecanismo; lo demas son sus formas.**

**El libro que mas junturas dejo, medido**: **Hugos, `Essentials of Supply Chain
Management`, esta entre las fuentes de 11 de las 35 confirmadas.** Es el pegado
mas extendido del nucleo, y en `asociaciones_clave` aparece dos veces en el
mismo campo.

### La consecuencia operativa, y es fuerte

**De las 64 citas que quedan sin leer, solo DOCE declaran dos o mas fuentes**, y
**las doce son de `core`**:

| bloque | corte | pasos | cita |
|---:|---:|---:|---|
| 47,4 | 5 | 8 | `mapa_de_canal_de_ventas` |
| 46,8 | 5 | 12 | `seleccion_ceo_fundador` |
| 46,6 | 3 | 8 | `cliente_disena_producto` |
| 45,7 | 5 | 9 | `manejo_empleados_en_adquisicion` |
| 45,7 | 3 | 7 | `estrategia_de_innovacion_producto` |
| 45,6 | 4 | 9 | `posicionamiento_de_empresa` |
| 45,2 | 5 | 9 | `gut_check` |
| 45,1 | 4 | 10 | `gestion_libro_abierto_obm` |
| 44,8 | 5 | 8 | `brainstorming_divergente` |
| 44,2 | 3 | 8 | `producto_unico_superior` |
| 44,2 | 5 | 10 | `revisiones_regulares_desempeno_ceo` |
| 44,1 | 6 | 10 | `optimizacion_embudo_get_customers` |

> **La corroboracion independiente esta a la vista**: varias de esas doce
> (`seleccion_ceo_fundador`, `posicionamiento_de_empresa`,
> `brainstorming_divergente`, `revisiones_regulares_desempeno_ceo`) **ya estan en
> la tabla de costuras del informe de la franja**, encontradas por el otro eje.
> **El predictor apunta donde el otro frente ya habia dado.**

> **Lo que esto dice de la cola restante, sin adornarlo**: si el predictor se
> sostiene, **la presa confirmada que queda vive casi entera en esas doce**, y
> las otras 52 son en su gran mayoria secuencias limpias de un solo libro. **Eso
> no autoriza a descartarlas**, por la misma razon de siempre: el predictor es
> una probabilidad medida sobre 64 casos, no una ley. **Lo que si autoriza es a
> leer esas doce PRIMERO**, que es la version afinada de la decision de orden
> anterior.
>
> **Y da una prueba barata que el auditor puede pedir**: si al leer las doce
> salen mayoria confirmadas y al leer una muestra de las otras 52 salen mayoria
> falsas, **el predictor queda validado y el resto de la cola se puede planificar
> con el**. Si no, se cae, y se habra perdido nada mas que el orden.

---

## TANDA 13: la primera leida POR LA SEÑAL DE DOS FUENTES

**Es la primera tanda que no se ordena por bloque sino por el numero de fuentes
del nodo.** Cinco confirmadas y una falsa, las seis del nucleo.

> **Reconciliacion de la cuenta de pendientes, pedida en el encargo.** El
> encargo dice que el archivo del auditor dio **8** y el mio da **9**, y **sigue
> dando 9** al recomputarlo hoy. Los nueve eran `manejo_empleados_en_adquisicion`,
> `estrategia_de_innovacion_producto`, `posicionamiento_de_empresa`, `gut_check`,
> `gestion_libro_abierto_obm`, `brainstorming_divergente`,
> `producto_unico_superior`, `revisiones_regulares_desempeno_ceo` y
> `optimizacion_embudo_get_customers`. **Ninguno cayo en la tanda 12**, cuyas
> cuatro confirmadas ya estaban descontadas.
>
> **La explicacion mas probable de la diferencia de uno, y la dejo como
> hipotesis**: `brainstorming_divergente` **ya figura como costura confirmada en
> la tabla del informe de la franja** (8 pasos, 2 bloques), encontrado por el
> otro eje. Quien cuente *pendientes de leer* descontando lo que ya se sabe
> costura por otra via obtiene **8**; quien cuente *citas de esta cola sin
> veredicto propio* obtiene **9**. **Las dos cuentas son correctas y cuentan
> cosas distintas.**

### `core/posicionamiento_de_empresa`, 9 pasos: EL MISMO ENTREGABLE DOS VECES

Blank y Horowitz. **La declaracion (1 a 5) y la historia (6 a 9) son el mismo
entregable escrito dos veces**, y el calco esta a la vista:

| paso 4 | paso 7 |
|---|---|
| *revisa ejemplos de referencia (Amazon, UPS, Zappos) para calibrar tono y enfoque* | *usa como referencia cartas fundacionales como la de Jeff Bezos a los accionistas de Amazon en 1997* |

**Los dos mandan mirar a Amazon como modelo de tono.** Es el mismo consejo con
distinto grado de detalle.

### `core/gut_check`, 9 pasos: LA EVALUACION CRITICA, DOS VECES

*The field guide to human-centered design* (IDEO) y *Co-Intelligence* (Mollick).

| bloque | como se hace la misma critica |
|---|---|
| **1 a 4** | **el taller**: destilar las ideas a su esencia, listar restricciones en post-its, brainstorm dentro de esas restricciones, **estar dispuesto a descartar** |
| **5 a 9** | **la tanda de IA**: describirle el plan, pedir 10 formas en que podria fallar, pedir una vision de exito alternativa, invocar dos o tres personajes que lo critiquen, sintetizar riesgos |

> **Hermana de `future_scenarios_planning`**, tambien confirmada: los dos son
> nodos de metodo critico a los que se les pego una segunda tanda entera.

### `core/estrategia_de_innovacion_producto`, 7 pasos: LA APUESTA AUDAZ, DOS VECES

Cooper y Horowitz. **Corte 3 y confirmada**, que es dato para la regla del corte.

| primera narracion | segunda narracion |
|---|---|
| paso 2: *identifica los mercados o tecnologias emergentes donde quieres enfocar* | paso 5: *decide reinventar el producto aunque contradiga el feedback documentado* |
| paso 3: *comparte con claridad hacia donde vas a enfocar tu desarrollo* | paso 6: *dile con claridad que la vision pesa mas que la lista de pendientes* |

**Los pasos 3 y 6 comunican lo mismo con dos vocabularios.** Los pasos 2 y 5
deciden los dos la apuesta, aunque el 2 la decide eligiendo arena y el 5
decidiendo contra el feedback: **se anotan los dos textos para que el matiz se
pueda juzgar.**

> **Es miembro de la familia de la estrategia de innovacion**, que el cribado
> intra-dominio llevo a **cinco nodos**.

### `core/gestion_libro_abierto_obm`, 10 pasos: EL GREAT GAME DOBLADO

| lo que se repite | donde | donde tambien |
|---|---|---|
| **vincular la recompensa al resultado** | paso 5: *vincular bonos o participacion en utilidades a los resultados financieros compartidos* | paso 10: *vincular recompensas tangibles e intangibles a los resultados alcanzados* |
| **hacer visibles los numeros** | paso 1: *reportes financieros simplificados y frecuentes* y paso 4: *reuniones periodicas donde se discutan los numeros* | paso 9: *tablero de indicadores visible en tiempo real, el marcador del juego* |

> **FIGURA NUEVA PARA EL BARRIDO: FUENTE QUE NO CORRESPONDE.** El nodo declara
> *Financial Intelligence for Entrepreneurs* **y `Essentials of Supply Chain
> Management` de Hugos**. **Ninguno de sus diez pasos es material de cadena de
> suministro**: los diez son Open-Book Management, el Great Game de Jack Stack.
> **Verificado paso por paso.**
>
> **Se registra como posible ARRASTRE DE CAMPO FUENTE**, no como cita de un
> segundo libro. **Y tiene una consecuencia que hay que decir aunque incomode**:
> si algunos `fuente` cargan entradas que no corresponden, **el denominador de
> la señal de dos fuentes tiene ruido**. La señal sigue midiendo lo que mide,
> pero **su base no esta auditada**, y auditarla es trabajo del barrido.

### `core/producto_unico_superior`, 8 pasos: COSTURA LEVE

Cooper y Hugos. **Un apendice de dos pasos** donde el **8** repite al **5**:
*comparar directamente contra la competencia por valor percibido*. El resto del
nodo esta sano. **Corte 3 y confirmada**, la segunda de esta tanda.

### La falsa, y trae CLASE NUEVA

#### `core/manejo_empleados_en_adquisicion`, 9 pasos: DUO LEGITIMO

*Venture Deals* de Feld y *The Hard Thing About Hard Things* de Horowitz.

| bloque | de que habla |
|---|---|
| **1 a 4** | **la mecanica del deal**: posponer la negociacion de compensacion individual hasta despues del LOI, no dejar los contratos para el final, balancear intereses, evaluar el impacto reputacional |
| **5 a 9** | **la comunicacion del anuncio**: informar a los empleados **antes** que a nadie fuera, no edulcorar el estado real, dar la opcion de irse con dignidad, emitir condiciones nuevas a quien se queda, la claridad interna por encima de las relaciones publicas |

> **CLASE NUEVA: DUO LEGITIMO.** Dos fuentes distintas dentro de un mismo nodo
> **en secuencia temporal, que no se pisan**: la primera cubre un momento y la
> segunda el siguiente. **No hay narracion repetida ni tema ajeno: hay una
> cronologia repartida entre dos libros.**
>
> **Como se distingue de la forma que parte**: alli el segundo bloque es **otro
> tema** que merece su propio nodo. **Aqui es el mismo asunto en su momento
> siguiente**, y separarlo dejaria al lector con media instruccion en cada mitad.
> **El duo legitimo no se toca.**

> **Y de aqui sale la CALIBRACION DE LA SEÑAL, que es lo que este ejemplar
> enseña**: **la juntura de dos libros ORDENA la lectura, no dicta el
> veredicto.** `manejo_empleados_en_adquisicion` declara dos libros, entro en la
> cola por eso, y **salio falsa**. La señal acerto al ponerlo arriba en la fila;
> **el veredicto siguio siendo de la lectura**, como en todas las demas.

---

### LA SEÑAL DE DOS FUENTES, recomputada con la tanda 13 dentro

| | con dos o mas fuentes | con una sola |
|---|---:|---:|
| **las 46 confirmadas** | **43 (93%)** | 3 |
| **las 82 falsas** | **4 (5%)** | 78 |

**La señal se refuerza**: subio de 91% a 93% en las confirmadas y sigue en el
entorno del 10% en las falsas. **Cinco de las seis citas de esta tanda, elegidas
solo por tener dos fuentes, salieron confirmadas.**

> **Y aporto algo que la señal del corte no habia dado**: **dos de las cinco
> confirmadas tienen corte 3** (`estrategia_de_innovacion_producto` y
> `producto_unico_superior`). **Las confirmadas de corte 3 pasan de dos a
> cuatro**, y las cuatro las encontro la señal de fuentes, no el corte. **Donde
> el corte no distingue, las fuentes si.**

> **La vena esta casi agotada, y conviene saberlo antes de planificar**: de las
> **52 citas que quedan sin leer, solo TRES declaran dos o mas fuentes**:
> `brainstorming_divergente`, `optimizacion_embudo_get_customers` y
> `revisiones_regulares_desempeno_ceo`. **Y las tres ya figuran como costuras
> confirmadas en la tabla del informe de la franja**, encontradas por el otro
> eje. **Si la señal se sostiene, la presa que queda en esta cola son esas tres
> y poco mas**, y las tres ya se sabian.

---

## TANDA 14: la vena de las dos fuentes se cierra, y dos herramientas caen

Dos confirmadas y cuatro falsas. Las dos confirmadas son **las dos ultimas
citas de dos fuentes** que quedaban por leer con veredicto propio.

### `core/optimizacion_embudo_get_customers`, 10 pasos: EL TESTEO DICHO DOS VECES

Blank y Weinberg. **El mismo testeo del embudo narrado dos veces:**

| primera narracion | segunda narracion |
|---|---|
| paso 3: *pruebas A/B controladas cambiando no mas de dos variables a la vez* | paso 7: *pruebas A/B continuas, minimo una por semana, sobre copy, imagenes y landing pages* |
| paso 5: *iterar continuamente, testear, medir, ajustar y volver a testear* | pasos 7 y 9: la iteracion continua y *buscar nuevas tacticas dentro del canal principal* |

> **Su paso 8 nombra Optimizely, Visual Website Optimizer y Unbounce**, las tres
> ya registradas en el informe de la franja como herramientas con nombre propio
> del nucleo. **No se reabre aqui**: se anota que este nodo es su casa.

### `core/revisiones_regulares_desempeno_ceo`, 10 pasos: LA EVALUACION DOBLADA

Wasserman y Horowitz. **El marco de calendario y el contenido de auditoria se
solapan en objetivos, metricas y revision:**

| paso 4 | pasos 9 y 10 |
|---|---|
| *vincular las revisiones con metricas objetivas de crecimiento y desempeno* | *establecer objetivos calibrados a la oportunidad real de la empresa* y *revisar resultados contra esos objetivos periodicamente* |

**Los pasos 1 a 4 montan el calendario de revision y los 9 y 10 lo vuelven a
montar** con otro vocabulario, con la auditoria de decisiones y equipo (5 a 8)
en medio.

---

### BALANCE FINAL DE LA SEÑAL DE DOS FUENTES COMO VENA DE LECTURA

**Ocho citas leidas eligiendolas solo por tener dos fuentes declaradas:**

| tanda | citas | confirmadas | falsas |
|---|---:|---:|---:|
| 13 | 6 | 5 | 1 (`manejo_empleados_en_adquisicion`, duo legitimo) |
| 14 | 2 | 2 | 0 |
| | **8** | **7** | **1** |

> **Siete de ocho.** Y la unica falsa no fue un fallo de la señal: fue el
> ejemplar que **obligo a abrir la clase DUO LEGITIMO**, o sea que el nodo tenia
> de verdad dos libros dentro y lo que fallo fue suponer que dos libros implican
> costura. **La señal predijo bien la presencia de dos fuentes; el veredicto lo
> siguio poniendo la lectura.**

> **LA VENA QUEDA AGOTADA COMO ORDEN DE LECTURA.** No quedan citas de dos
> fuentes con veredicto propio pendiente: **las tres que faltaban
> (`brainstorming_divergente`, `optimizacion_embudo_get_customers` y
> `revisiones_regulares_desempeno_ceo`) ya constaban como costuras en el informe
> de la franja**, y las dos ultimas acaban de leerse aqui y confirmaron.
>
> **La señal no se archiva: cambia de oficio.** Deja de ordenar la lectura de
> esta cola y **pasa a ser criterio del plan de la pasada unica**: cuando haya
> que decidir por donde entrar a un nodo, el numero de fuentes declaradas dice
> donde mirar primero. **Con la salvedad ya registrada de que el campo `fuente`
> tiene ruido** (ver `gestion_libro_abierto_obm`, que declara un libro cuyo
> material no aparece en ningun paso).

---

### Las cuatro falsas, todas SECUENCIA LEGITIMA

| cita | pasos | corte | fuente |
|---|---:|---:|---|
| `core/definicion_gatekeepers` | 6 | **3** | Cooper |
| `core/plan_gestion_adquisiciones` | 6 | **3** | Book of Forms |
| `core/retargeting_display` | 6 | **3** | Weinberg |
| `core/regalos_estrategicos_sorpresa` | 8 | 5 | Coleman |

> **Nota de doble pregunta sobre `regalos_estrategicos_sorpresa`**, que ya se ha
> visto antes en esta ficha: como **costura es falso**, y al mismo tiempo el
> cribado intra-dominio lo clasifico **A REPITE** en su puesto 251, porque
> `sorprender_cliente_estrategico` dice lo mismo. **Limpio por dentro, con gemelo
> fuera.**

### `regalos_estrategicos_sorpresa` es el QUINTO VERTICE del racimo de experiencia

**Sano, como `fase_affirm_buyers_remorse`, y por la misma razon util: es destino
existente, no material a crear.** El solape, verificado contra el grafo:

| `regalos_estrategicos_sorpresa` | `blueprint_de_experiencia` |
|---|---|
| paso 7: *memorializar experiencias (cenas, eventos) con un objeto fisico que las recuerde* | paso 11: *crea un recuerdo fisico o digital que tu cliente pueda conservar de la decision que tomo* |

**Es el material del RITUAL, el bloque 9 a 13 del blueprint**, y ya tiene casa
propia en un nodo sano de Coleman.

> **El racimo transversal de experiencia queda con CINCO vertices**: tres
> costurados (`blueprint_de_experiencia`, `cultura_de_experiencia`,
> `customer_journey_mapping`) y **dos sanos que son destino**
> (`fase_affirm_buyers_remorse` para la postventa proactiva y
> `regalos_estrategicos_sorpresa` para la memorializacion del ritual).
>
> **Con esto, dos de los cuatro bloques del blueprint ya tienen adonde ir sin
> crear nodo nuevo.** El reparto del destejido conjunto empieza a parecerse menos
> a una particion y mas a una devolucion.

---

### VERIFICACION DE HERRAMIENTAS de `retargeting_display`, con evidencia

**Encargo adjunto cumplido. Seis herramientas nombradas, DOS MUERTAS.**

| herramienta | estado | evidencia |
|---|---|---|
| **AdRoll** | **VIVA** | plataforma de NextRoll, activa y con reviews de 2026 |
| **Perfect Audience** | **MUERTA** | TrustRadius la lista como *(discontinued)*; comprada por Marin en 2014 y por SharpSpring en 2019, y descontinuada despues |
| **MixRank** | **VIVA** | operando en 2026 como plataforma de inteligencia competitiva y datos B2B |
| **Adbeat** | **VIVA** | activa en 2026, con precio publico y cobertura de mas de 90 redes |
| **The Deck** | **MUERTA** | **cerro en marzo de 2017**, anunciado por su fundador Jim Coudal y cubierto por TechCrunch y Daring Fireball |
| **BuySellAds** | **VIVA** | operando en 2026, con equipo y marketplace activos |

> **Son las PRIMERAS HERRAMIENTAS QUE ESTA CAMPANA PUEDE DECLARAR MUERTAS.** El
> informe de la franja registro catorce pares con herramientas de nombre propio y
> las anoto todas **sin asumir que murieran**, porque nadie las habia verificado.
> **Aqui se verificaron seis y cayeron dos.**

> **Y las dos caen en el mismo nodo y en pasos distintos**: `Perfect Audience` en
> el paso 1, entre los pixeles a instalar, y `The Deck` en el paso 4, entre las
> redes de nicho a evaluar. **Un lector que siga ese nodo hoy instalaria un pixel
> de una plataforma descontinuada y evaluaria una red que cerro hace nueve
> anos.** El nodo es **sano como costura y esta caducado como consejo**: son dos
> preguntas distintas y las dos hay que contestarlas.

> **Lo que esto abre, y se dice sin estirarlo**: si de seis herramientas
> verificadas dos estan muertas, **la ficha de herramientas nombradas deja de ser
> una lista de anotaciones y pasa a ser una lista de comprobaciones pendientes**.
> Son **veinticuatro nombres propios** los que el informe de la franja tiene
> anotados sin verificar. **A este ritmo, un tercio podria estar caducado.** No es
> una prediccion: es la razon para verificarlos.

---

## TANDA 15: la primera tanda EN BLANCO, y la señal la predijo

**Seis citas del nucleo por bloque, banda 44,7 a 45,4. Las seis FALSAS.** Es la
primera tanda sin una sola confirmada en quince tandas de lectura.

| cita | pasos | corte | fuente unica |
|---|---:|---:|---|
| `core/vesting_acciones_fundadores` | 7 | 4 | *Venture Deals* (Feld) |
| `core/validar_canal_distribucion` | 6 | **3** | *The Startup Owner's Manual* (Blank) |
| `core/prototipar_con_medios_no_convencionales` | 6 | **3** | *Assembling Tomorrow* |
| `core/eventos_offline_como_canal_traccion` | 7 | **3** | *Traction* (Weinberg) |
| `core/preferencia_de_liquidacion` | 8 | **3** | *Venture Deals* (Feld) |
| `core/portfolio_management` | 6 | **3** | *Winning at New Products* (Cooper) |

**Todas SECUENCIA LEGITIMA.** Y `portfolio_management` es ademas **vecino sano
del racimo de portafolio** censado en la franja: pertenece a la familia y no
esta costurado por dentro.

> **LA CAUSA ESTA MEDIDA Y ES LA MISMA SEÑAL, ahora prediciendo en negativo: las
> seis declaran UNA SOLA FUENTE.** Verificado nodo por nodo contra el grafo.
>
> **La señal de dos fuentes ha predicho en las dos direcciones**: ocho citas
> elegidas por tener dos libros dieron siete confirmadas; **seis citas que solo
> tienen uno dieron cero.** No es que la banda 44 sea esteril: **es que ahi abajo
> ya casi no quedan nodos de dos libros, y sin juntura no hay costura.**

> **Lo que esta tanda anade a la señal, y es lo que le faltaba**: hasta ahora
> solo se habia comprobado que **las citas de dos fuentes rinden**. Esta
> comprueba lo contrario, que es la mitad que hace util a un predictor: **las de
> una sola fuente no rinden.** Con 88 leidas, la tabla queda con las dos caras.

---

### VERIFICACION DE MARCO en `core/vesting_acciones_fundadores`

**El nodo cablea material del IRS**: el paso 2 manda *presentar la eleccion
fiscal 83(b) dentro de los 30 dias siguientes a la emision*, y el
`entregable_esperado` exige *eleccion 83(b) presentada*. La eleccion 83(b) es
del codigo fiscal estadounidense.

**Revisadas las tres casas, como manda la leccion de Magnuson**, el resultado
**no es limpio en ninguna de las dos direcciones** y se registra como sale:

| casa | condiciona por pais? |
|---|---|
| `condiciones_activacion` | **NO**. Sus cinco entradas son de situacion (constituir la empresa, incorporar cofundadores, exigencia del inversor, proteger la salida temprana, negociar una venta). Ninguna menciona pais |
| `pasos_accionables` | **NO**. El paso 2 manda presentar la 83(b) sin condicion alguna |
| `entregable_esperado` | **NO**. Exige la 83(b) presentada como parte del entregable, sin condicion |
| `resumen_teorico` | **SI, pero generico y al final**: cierra con *verifica estos detalles con un profesional en tu pais* |

> **Ni contramodelo limpio ni marco-pais limpio: es un caso intermedio, y merece
> nombre propio porque no es el unico que va a aparecer.**
>
> **La diferencia con la familia Magnuson-Moss es de peso y de sitio.** Alli la
> condicion es **la primera linea de `condiciones_activacion`**, dice **Estados
> Unidos** con todas sus letras y se repite en dos o tres casas. **Aqui hay una
> frase generica en la ultima linea del resumen**, y **lo que el lector ejecuta**,
> que son los pasos y el entregable, **no lleva condicion ninguna**.
>
> **Un lector de otro pais que siga este nodo presenta una eleccion 83(b) que no
> existe en su jurisdiccion**, y solo se entera si lee el resumen entero hasta el
> final. **La frase esta, pero no esta donde se decide.**

> **Se registra como CANDIDATO a la ficha de marco-pais, con su atenuante
> escrito**, y con la observacion que le toca al barrido: **la pregunta util no
> es si el nodo condiciona, sino si condiciona DONDE SE ACTUA.** El contramodelo
> Magnuson-Moss condiciona en la puerta; este condiciona en la despedida.

---

## TANDA 16: segunda tanda en blanco, y el nucleo queda casi agotado

**Seis citas mas del nucleo, LAS SEIS FALSAS.** Segunda tanda consecutiva sin
una sola confirmada, y **las seis declaran una sola fuente**, igual que las seis
de la tanda 15.

| cita | pasos | corte | fuente unica |
|---|---:|---:|---|
| `core/internal_idea_capture` | 7 | 4 | *Winning at New Products* (Cooper) |
| `core/captura_conocimiento_mercado` | 7 | 4 | *The Startup Owner's Manual* (Blank) |
| `core/lectura_balance_general` | 6 | **3** | *Financial Intelligence for Entrepreneurs* |
| `core/sem_estrategia_ejecucion` | 8 | 5 | *Traction* (Weinberg) |
| `core/product_market_fit` | 6 | **3** | *The Startup Owner's Manual* (Blank) |
| `core/dso_dpo_gestion_capital_trabajo` | 4 | **0** | *Financial Intelligence for Entrepreneurs* |

**Todas SECUENCIA LEGITIMA.** Dos de ellas son piezas sanas de racimos que el
cribado intra-dominio ya censo: `lectura_balance_general` es **la mitad que
ensena a leer** de la forma financiera (un nodo ensena a leer el estado, otro lo
usa para juzgar), y `dso_dpo_gestion_capital_trabajo` es **el nodo conjunto** del
racimo de capital de trabajo. **Pertenecer a un racimo no es estar costurado por
dentro**, y estas dos lo dejan claro.

> **LA FILA VACIA SE ESTRENA.** `dso_dpo_gestion_capital_trabajo` tiene **bloque
> 0,0 y no dispara por bloque**: entro por **pareja 81,5**, por encima del umbral
> de 80. **Es la primera de las cuatro citas de solo-pareja que se lee**, y la
> fila que llevaba desde el principio en cero por fin tiene una entrada. **Salio
> falsa**, con lo que la fila queda en 0 confirmadas de 1.
>
> Quedan **tres citas de solo-pareja sin leer**, y las tres son de `quality`:
> `diseno_de_procesos_por_caracteristicas` (86,6), `tipos_innovacion_i_ii` (84,1)
> y `control_estadistico_metodo_medicion` (80,9).

---

### EL HITO, con su excepcion: el nucleo queda agotado SALVO UNA

**Es un hito real y hay que decirlo con su nombre completo.** De las 128 citas
del instrumento, **quedan 34 sin leer, y solo UNA es del nucleo**:

| dominio | citas sin leer |
|---|---:|
| quality | **16** |
| exportacion | 5 |
| health_safety | 4 |
| seguridad_digital | 4 |
| environmental | 2 |
| franquicias | 2 |
| **core** | **1** |

> **CHOCA CON EL ENCARGO, que dice el nucleo agotado, y lo traigo.** La que
> queda es **`brainstorming_divergente`** (8 pasos, corte 5, bloque 44,8, dos
> fuentes: *Change by Design* y *Co-Intelligence*).
>
> **Y es exactamente el mismo nodo que produjo el descuadre de 9 contra 8 en la
> tanda 13.** Vuelve a producir un off-by-one por la misma razon: **ya consta
> como costura confirmada en la tabla del informe de la franja**, encontrada por
> el eje mundo contra nucleo, **pero no tiene veredicto propio en esta cola**.
>
> **Quien cuenta nodos del nucleo con costura ya sabida dice agotado. Quien
> cuenta citas de esta cola sin leer dice una.** Las dos son correctas, y la
> segunda es la que usa esta ficha. **Dos veces seguidas el mismo nodo ha marcado
> la diferencia entre las dos formas de contar**, asi que conviene decidir cual
> manda antes de que aparezca una tercera vez.
>
> **Ademas tiene dos fuentes**, o sea que **es la ultima cita de dos libros que
> queda sin veredicto propio en toda la cola**. Si el predictor se sostiene,
> deberia confirmar.

---

### EL PREDICTOR DE FUENTES CIERRA SUS DOS MITADES

**Con 94 citas leidas, las dos caras estan medidas:**

| | citas leidas | confirmadas | tasa |
|---|---:|---:|---:|
| **nodos de DOS o mas libros** | **46** | **42** | **91%** |
| **nodos de UN solo libro** | **48** | **3** | **6%** |

> **INSTANTANEA CONGELADA de ese momento, NO se actualiza.** La tabla viva esta
> en `MARCADOR DE LA CLASE`.

> **Quince veces mas probable.** Un nodo que declara dos libros confirma nueve de
> cada diez veces; uno que declara uno solo confirma seis de cada cien. **Y el
> reparto de la cola es casi mitad y mitad**, 46 contra 48, asi que no es un
> efecto de tamano de muestra en un lado.

> **Esto es lo que la campana buscaba desde el principio, y llego por un camino
> que no era el previsto.** El instrumento se construyo sobre dos senales de
> TEXTO, el bloque y la pareja, y las dos han resultado ruidosas: el corte 3 da
> cuatro confirmadas de treinta y tres, y la pareja no separo nada. **La senal
> que si separa no estaba en el texto: estaba en el campo `fuente`, que nadie
> habia mirado.**
>
> **Con la salvedad ya registrada**: ese campo tiene ruido (`gestion_libro_abierto_obm`
> declara un libro cuyo material no aparece en ningun paso), asi que **el
> predictor es bueno y su base no esta auditada**. Auditarla es del barrido.

---

### DOCTRINA DEL MARCO: la condicion honesta se copia A LA PUERTA

**Nace del contraste entre dos casos ya verificados en esta ficha**, y se escribe
aqui, junto al remedio, porque es una instruccion de redaccion y no un hallazgo:

| | `cumplimiento_magnuson_moss` y su familia | `vesting_acciones_fundadores` |
|---|---|---|
| **donde esta la condicion** | **primera linea de `condiciones_activacion`** | ultima linea del `resumen_teorico` |
| **como lo dice** | *si vendes, o piensas vender, productos a clientes en **Estados Unidos*** | *verifica estos detalles con un profesional en **tu pais*** |
| **se repite en** | resumen y entregable, dos o tres casas | en ninguna otra |
| **que lee quien ejecuta** | la condicion, antes de empezar | los pasos y el entregable, **sin condicion** |

> **LA REGLA: la condicion de pais se copia A LA PUERTA, donde se actua**, es
> decir a `condiciones_activacion`, y **nombrando el pais**. Dejarla solo en el
> resumen la convierte en una nota al pie de algo que ya se hizo.
>
> **El caso lo demuestra sin necesidad de teoria**: un lector de otro pais que
> siga `vesting_acciones_fundadores` **presenta una eleccion fiscal 83(b) que no
> existe en su jurisdiccion**, porque el paso 2 y el entregable se la piden sin
> condicion alguna. La frase que lo salvaria esta escrita, pero **al final del
> resumen**, que es donde ya no decide nada.
>
> **Y el remedio es barato**: no hay que reescribir el nodo ni quitarle el
> material. **Hay que mover la condicion de sitio**, o mejor, **copiarla**, que es
> lo que la familia Magnuson-Moss hace y por eso es el contramodelo.

---

### CANDIDATO NUEVO A NODO-FRONTERA: `exportacion/export_administration_regulations`

**Verificacion tipo Magnuson hecha sobre sus tres casas, y el veredicto es
limpio: NO condiciona en la puerta.** Sale de la tanda 17, y es el primer
candidato que no es del nucleo.

**El nodo cablea EAR, ECCN, BIS y U.S. Commercial Service. Esto es lo que dice
cada casa, transcrito:**

| casa | que dice sobre el pais |
|---|---|
| **`condiciones_activacion`, LA PUERTA** | **NADA.** Sus tres condiciones son *si vas a exportar un producto por primera vez*, *si tu producto tiene aplicaciones de doble uso* y *si el destino de exportacion es un pais con restricciones*. **Ninguna nombra desde donde se exporta.** |
| `resumen_teorico` | **SI, y con el pais nombrado**: *las EAR regulan... puede que necesites una licencia de exportacion del BIS del Departamento de Comercio de EE.UU.* Y al final: *esta mecanica refleja la normativa de EE.UU. ...; verifica el acuerdo y la regulacion vigente en tu jurisdiccion antes de actuar.* |
| `pasos_accionables` | **NADA.** Los seis pasos mandan clasificar por ECCN, consultar el chart de las EAR, pedir opinion consultiva al BIS, solicitar la licencia y contactar a la oficina local del U.S. Commercial Service, **sin condicion previa de ninguna clase.** |
| `entregable_esperado` | **NADA**: *clasificacion ECCN de tu producto y determinacion documentada de si necesitas licencia*, sin condicion. |

> **CANDIDATO CONFIRMADO, y con la misma anatomia exacta que
> `vesting_acciones_fundadores`:** la condicion honesta **existe y esta escrita**,
> pero vive **al final del `resumen_teorico`**, que es donde ya no decide nada, y
> ademas **esta redactada en generico** (*verifica la regulacion vigente en tu
> jurisdiccion*) en vez de nombrar el pais.
>
> **Lo que le pasa a un lector de fuera de Estados Unidos**: entra por la puerta
> porque va a exportar por primera vez, que es su caso, y el nodo lo manda a
> **clasificar su producto con un ECCN, pedirle una opinion consultiva al BIS y
> solicitar una licencia de exportacion estadounidense**. **Nada de eso existe
> para el.** Y el entregable que se le pide es precisamente esa clasificacion.

**EL REMEDIO BARATO, escrito para que se pueda copiar tal cual:**

> **Copiar a `condiciones_activacion` la condicion honesta con el pais dentro:
> *si exportas DESDE Estados Unidos*.** Una linea. **No hay que reescribir el
> nodo, ni quitarle material, ni tocar la doctrina**: el contenido es correcto
> para quien exporta desde alli.

#### Y aqui la doctrina del marco gana una distincion que no tenia

**Esta condicion no es del mismo tipo que la de Magnuson-Moss, y confundirlas
haria mal el arreglo:**

| | la condicion es sobre | como se redacta |
|---|---|---|
| la familia **Magnuson-Moss** | **el DESTINO**: a quien le vendes | *si vendes, o piensas vender, productos a clientes en Estados Unidos* |
| **las EAR** | **el ORIGEN**: desde donde exportas | *si exportas DESDE Estados Unidos* |

> **Son dos ejes distintos y un nodo puede necesitar uno, el otro o los dos.**
> `export_administration_regulations` es el primer ejemplar del eje de ORIGEN que
> esta campana encuentra. **La regla de la puerta no cambia; lo que cambia es que
> ahora hay que preguntar cual de los dos ejes condiciona, y no solo si hay
> pais.**

**El nodo no se toca desde esta ficha.** Queda **candidato**, con su evidencia
transcrita y su remedio escrito, para que el barrido lo ejecute.

---

## DECISION DE CUENTAS: en esta cola manda SIN VEREDICTO PROPIO

**Registrada aqui, junto al marcador, porque es una regla de contabilidad y este
es su sitio.**

> **En la cola de 128 citas manda la cuenta de SIN VEREDICTO PROPIO. Cada cita
> exige su veredicto EN ESTA COLA. Lo que conste en otros informes es contexto,
> nunca asiento.**

**Nace de un descuadre que aparecio dos veces y siempre por el mismo nodo.**
`brainstorming_divergente` figuraba como costura confirmada en la tabla del
informe de la franja, encontrada por el eje mundo contra nucleo, **pero no tenia
veredicto propio aqui**. Quien lo contaba como leido obtenia 8 pendientes y
nucleo agotado; quien lo contaba como pendiente obtenia 9 y una cita restante.
**Las dos cuentas eran correctas y contaban cosas distintas**, que es
exactamente lo que una regla de contabilidad viene a impedir.

> **Por que manda esta y no la otra**: un veredicto de otro informe se emitio
> **mirando otra cosa**. La tabla de costuras del informe de la franja salio de
> leer pares mundo contra nucleo, no de leer la cita del instrumento con su
> bloque, su corte y su pareja delante. **Contarlo como asiento aqui seria
> importar una conclusion sin importar su prueba.**

---

## `core/brainstorming_divergente`, 8 pasos: CONFIRMADA, y cierra el nucleo

**Bloque 44,8, corte 5.** *Change by Design* (Tim Brown) y *Co-Intelligence*
(Mollick).

| bloque | de que habla |
|---|---|
| **1 a 4** | **el taller IDEO**: reunir al equipo sin distracciones, establecer las reglas (cantidad sobre calidad, diferir el juicio, construir sobre las ideas de otros), **generar el mayor numero de ideas sin filtrar**, registrarlas visualmente |
| **5 a 8** | **la tanda de IA**: usar la IA como un participante mas, pedirle que adopte personas y estilos, **generar un lote grande con IA y filtrar despues con criterio humano**, iterar cruzando conceptos |

**El calco verificado**: el paso **3** (*generar el mayor numero de ideas posible
sin filtrar prematuramente*) vuelve en el paso **7** (*generar un lote grande de
ideas con IA y luego aplicar filtrado humano experto*). **Es la misma
instruccion, generar mucho y filtrar despues, dicha una vez para el taller y otra
para la maquina.**

> **AVISO DE CORTE (19 ago 2026, vuelta 37). ESTA ANATOMIA ES LA DEL 12 ago 2026 Y
> SE CONSERVA ENTERA, porque es la prueba de la que salio el corte.** El nodo **ya
> no tiene ocho pasos: tiene cuatro**. `OP-F-02` ejecuto el corte que esta misma
> ficha dibujo, y el bloque **5 a 8** vive desde el 14 ago 2026 en
> `ideacion_con_ia_en_la_sesion`, con sus cuatro pasos identicos uno a uno (medido
> hoy por `git` contra el padre del commit de `OP-F-02`, salida
> `docs/loop/SALIDA_V37_OPD04_DESTEJIDO.txt`). **El calco verificado que esta ficha
> nombra, el paso 3 volviendo en el paso 7, es exactamente lo que la cirugia
> deshizo.**


> **EL NUCLEO QUEDA AGOTADO DE VERDAD.** Era la ultima cita de `core` en la cola
> de 128. Las 33 que restan son todas de mundos: 16 de `quality`, 5 de
> `exportacion`, 4 de `health_safety`, 4 de `seguridad_digital`, 2 de
> `environmental` y 2 de `franquicias`.

> **Y era tambien la ultima cita de DOS LIBROS sin veredicto propio. Confirmo, y
> el predictor cierra su ultima apuesta a favor:**
>
> | | citas leidas | confirmadas | tasa |
> |---|---:|---:|---:|
> | **nodos de DOS o mas libros** | **47** | **43** | **91%** |
> | **nodos de UN solo libro** | **48** | **3** | **6%** |
>
> **INSTANTANEA CONGELADA de ese momento, NO se actualiza.** La tabla viva esta en
> `MARCADOR DE LA CLASE`.
>
> **Las 47 citas de dos libros de la cola estan todas leidas.** Lo que queda por
> leer, las 33 de mundos, **es de un solo libro sin excepcion**.

---

## PATRON DE FUENTE: LA TANDA DE MOLLICK, y sale mas raro de lo previsto

**Tres nodos de metodo de taller llevan a Mollick pegado como segunda voz**, y
los tres estan confirmados como costura. Verificado contra el grafo:

| nodo | primera voz, el taller | segunda voz |
|---|---|---|
| `future_scenarios_planning` | *Business Model Generation* (Osterwalder) | **Mollick** |
| `gut_check` | *The field guide to human-centered design* (IDEO) | **Mollick** |
| `brainstorming_divergente` | *Change by Design* (Tim Brown) | **Mollick** |

**Los tres tienen la misma anatomia**: el metodo clasico en el primer bloque y
**la misma operacion rehecha con IA** en el segundo.

> **PERO al ir a contarlo salio un dato que cambia como se lee el patron, y no
> estaba en el encargo.** Mollick **no es un libro que se pego a tres nodos
> ajenos: es un libro con territorio propio.** **51 nodos del catalogo lo
> declaran**, y **48 de ellos son nodos de tema IA por su propio id**
> (`prompting_*`, `ia_*`, `jagged_frontier_ia`, `human_in_the_loop_ia`,
> `deteccion_alucinaciones_ia` y asi).
>
> **O sea que la tanda de Mollick entro dos veces y de dos maneras**: como
> **familia propia de 48 nodos**, que es lo correcto, **y ademas como injerto en
> 3 nodos de taller que ya existian**, que es la costura.
>
> **Eso agrava el caso en vez de atenuarlo**: el material de IA **ya tenia
> adonde ir**. Los tres injertos no se hicieron por falta de sitio; se hicieron
> teniendo el sitio hecho.

### Los patrones de fuente que ya van tres, y lo que significan juntos

| patron | como se manifiesta | cuantos nodos |
|---|---|---:|
| **los formatos lista del `Basic Guide`** | checklists largos que el estandar de 3 a 6 pasos no contempla, y que salen **falsos** | 4 de los 7 LARGO LEGITIMO |
| **la tanda de Mollick** | el metodo de taller rehecho con IA como segundo bloque, **confirmado** las tres veces | 3 |
| **el pegado de Hugos** | material de cadena de suministro adosado a nodos de otro tema, **confirmado** | 11 de las 46 confirmadas |

> **Los tres son arreglos de nodo que se convierten en UNA decision de fuente en
> la pasada unica**, y esa es la utilidad de haberlos nombrado. **No se decide
> nodo por nodo si el checklist del Basic Guide se parte, si el bloque de IA se
> separa o si el apendice de Hugos se poda: se decide una vez por libro, y la
> decision se aplica a todos sus nodos.**
>
> **Es la misma economia que la mesa de racimos**: cuatro decisiones en vez de
> treinta y dos. **Aqui son tres decisiones en vez de dieciocho nodos.**

---

## CENSO DE HERRAMIENTAS: reconciliado, y la cuenta sube

**`Alexa` estaba contada dos veces**, y al reconciliarla aparecio que **el censo
tenia una muerta mas de la que yo habia sumado**.

| donde constaba | que decia |
|---|---|
| ficha de herramientas, entrada del lote 22 (via franja) | `nucleo/analisis_trafico_competitivo` la cita en sus pasos 1 y 6, y ya la declaraba **RETIRADA**, junto con **`Compete`** |
| ficha de herramientas, entrada 3 (10 ago 2026, via costuras) | **MUERTA**, con la fecha exacta del cierre de Amazon |

> **Una sola entrada, con las dos procedencias.** Alexa aparece en **dos nodos
> distintos** del catalogo (`analisis_trafico_competitivo` y el nodo de metricas
> de franquicias del informe 4.7), y **es una sola herramienta muerta**, no dos.

> **CORRECCION DE MI PROPIA CIFRA, recomputada del censo entero**: escribi *cuatro
> muertas y cinco vivas de once verificadas*. **No conte `Compete`**, que la
> entrada anterior ya daba por retirada. **El censo real va asi:**
>
> | | |
> |---|---:|
> | **muertas** | **6**: Alexa, Compete, Perfect Audience, The Deck, oDesk, Elance |
> | **vivas** | **5**: AdRoll, MixRank, Adbeat, BuySellAds, InnoCentive |
> | **no verificables** | **1**: Guide to Greener Electronics |
> | **verificadas en total** | **12** |
>
> **AMPLIACION DEL 13 ago 2026, desde el puesto 508 del cribado intra**:
> **`Quantcast`**, citada en el paso 6 de `analisis_trafico_competitivo`.
> **Estado: SIN VERIFICAR**, y se registra asi y no como viva porque **no la he
> comprobado**. Es el nombre propio numero **catorce**, detras de `AngelList`.
>
> **Y el mismo puesto deja el mejor argumento del TOQUE UNICO que ha dado el
> cribado**: `analisis_trafico_competitivo` nombra **CINCO** herramientas (Alexa y
> Compete en su paso 1, MixRank y Adbeat en el 5, Alexa o Quantcast en el 6) y su
> gemelo dice *herramientas de medicion de trafico web*, **cero nombres propios**.
> **Fundir hacia el generico borra cinco verificaciones de vigencia de una vez**, y
> **dos de las cinco ya estan muertas**. La fusion aqui no pierde informacion util:
> **pierde mantenimiento.**

> **AMPLIACION DEL 11 ago 2026, desde el puesto 2022 del cribado intra y la
> relectura R41**: `exportacion/proteccion_propiedad_intelectual_internacional`
> cablea en su paso 3 **dos portales de agencias de un solo pais**, y los dos se
> verificaron el mismo dia.
>
> | nombre propio | estado | quien lo opera |
> |---|---|---|
> | **`stopfakes.gov`** | **VIVO** | International Trade Administration, Departamento de Comercio de EE.UU. |
> | **`uspto.gov`** | **VIVO** | United States Patent and Trademark Office |
>
> **Ninguno anuncia mudanza, retiro ni redireccion**, y `stopfakes.gov` sigue
> ofreciendo sus guias por pais. Son los nombres **quince y dieciseis**.
>
> **Y dejan un dato para el barrido de vigencia**: `stopfakes.gov` lo opera **la
> misma International Trade Administration** que opera `trade.gov`, el organismo
> que absorbio `export.gov`. **Los tres portales de la lista cuelgan del mismo
> sitio**, asi que probablemente se muevan juntos la proxima vez.

> **Seis muertas de CATORCE verificadas.** **Y el catalogo tiene otros dieciocho
> nombres propios anotados sin verificar.**
>
> | | |
> |---|---:|
> | **muertas** | **6** |
> | **vivas** | **7**: AdRoll, MixRank, Adbeat, BuySellAds, InnoCentive, **stopfakes.gov**, **uspto.gov** |
> | **no verificables** | **1** |
> | **sin verificar** | **1**: Quantcast |
> | **verificadas en total** | **14** |

---

## TANDA 17: la primera tanda de MUNDOS, y la tercera en blanco

**Seis citas mas, LAS SEIS FALSAS**, y es la **tercera tanda consecutiva sin una
sola confirmada**. Es tambien **la primera tanda entera de mundos**: ninguna es
de `core`, porque en `core` ya no queda nada que leer.

**Banda de bloque 47,4 a 48,1**, y esa banda **queda agotada con esta tanda**:
el instrumento tiene **catorce citas** ahi dentro, **ocho ya estaban leidas** en
tandas anteriores y **estas seis eran las que faltaban**. Anatomias y fuentes
verificadas contra el grafo antes de escribir la tabla.

| cita | dominio | pasos | bloque | corte | fuente unica |
|---|---|---:|---:|---:|---|
| `respuesta_consultas_internacionales` | exportacion | 7 | 48,1 | **3** | *A Basic Guide to Exporting* (U.S. Commercial Service, 11.ª ed.) |
| `plan_de_accion_de_emergencia` | health_safety | 6 | 48,1 | **3** | `SMALL_BUSINESS` |
| `design_for_six_sigma_dfss` | quality | 6 | 47,6 | **3** | *Juran's Quality Handbook* (Defeo) |
| `make_certain_programa` | quality | 7 | 47,5 | **3** | *Quality is Free* (Philip B. Crosby) |
| `diseno_de_mejoras_para_clientes` | quality | 7 | 47,5 | 4 | *Juran's Quality Handbook* (Defeo) |
| `export_administration_regulations` | exportacion | 6 | 47,4 | **3** | *A Basic Guide to Exporting* (U.S. Commercial Service, 11.ª ed.) |

**Las seis son SECUENCIA LEGITIMA**, y las seis por el mismo motivo: **cada una
recorre un solo procedimiento de principio a fin**. El plan de emergencia
identifica riesgos, nombra a quien ordena evacuar, documenta rutas, atiende a
quien no puede salir solo, cuenta a la gente y capacita; la respuesta a consultas
fija politica, traduce, contesta, informa terminos, adjunta y archiva. **No hay
un segundo bloque en ninguna: hay un procedimiento largo.**

### Dos precisiones que salieron al verificar, y las dos corrigen el encargo

> **1. `make_certain_programa` es de Crosby pero esta FUERA de los catorce
> pasos**, confirmado contra el grafo: la serie declarada vive en otros nodos
> (`concepto_programa_catorce_pasos`, `crosby_programa_14_pasos_introduccion`,
> `mejora_calidad_crosby` y companeros). **Este es un programa aparte del mismo
> libro**, el Make Certain, con su propia mecanica de coordinadores por
> departamento y sesiones donde cada uno declara su mayor problema. **No toca la
> serie de catorce que la mesa de racimos ya tiene declarada**, y por eso su
> veredicto no arrastra nada alli.

> **2. La fuente de `plan_de_accion_de_emergencia` NO dice *OSHA small business*:
> dice `SMALL_BUSINESS`, a secas y en mayusculas.** Y al ir a comprobarlo salio
> un defecto de campo que vale mas que la cita:
>
> | token en el campo `fuente` | nodos | dominio |
> |---|---:|---|
> | `SMALL_BUSINESS` | **51** | health_safety |
> | `OSHA3886` | **27** | health_safety |
> | `OSHA3885` | **24** | health_safety |
> | | **102** | **todos health_safety** |
>
> **Ciento dos nodos llevan un token de archivo donde deberia ir un titulo de
> fuente**, y **ninguno de los 51 de `SMALL_BUSINESS` contiene la cadena OSHA**,
> asi que ni siquiera se pueden agrupar por texto. **Son 102 de los 283 nodos de
> `health_safety`, mas de un tercio del dominio.**
>
> **Es el mismo defecto de campo ya anotado en el informe intra** con *Steve
> Blank* contra *Blank, Steve*, pero peor: alli el libro estaba escrito de dos
> maneras, **aqui no esta escrito**. Cualquier barrido de fuentes que se haga
> contra este dominio tiene que resolver los tokens primero.

### La constelacion Six Sigma: la cita es sana y la familia es grande

**`design_for_six_sigma_dfss` es sano**: recorre el diseno para Six Sigma de
principio a fin, del alcance a los CTQ, de los CTQ al diseno integrado de
producto y proceso, y de ahi a la verificacion y al plan de lanzamiento.

> **Pero al verificarlo aparecio el tamano de la constelacion: DIECINUEVE nodos
> del catalogo llevan `six_sigma` o `seis_sigma` en su propio id**, y **cuatro de
> ellos son del mismo asunto que este**: `design_for_six_sigma_dfss`,
> `design_for_six_sigma_dmadv`, `design_for_six_sigma_dmadv_2` y
> `dmadv_design_for_six_sigma`. **Eso no lo decide esta ficha**: es materia del
> cribado intra-dominio, que lo leera cuando la cola los traiga. **Queda anotado
> para que no haya que encontrarlo dos veces.**

---

### EL PREDICTOR EN NEGATIVO SOSTENIDO: dieciocho seguidas

**La racha, con cifras recontadas del archivo:**

> **DIECIOCHO citas de UNA SOLA FUENTE leidas seguidas, y CERO costuras.** Seis
> en la tanda 15, seis en la tanda 16 y seis en esta.
>
> **Y la unica cosa que interrumpio esa racha confirma el predictor por el otro
> lado**: entre la tanda 16 y esta se leyo `brainstorming_divergente`, **la unica
> de DOS libros que quedaba sin veredicto propio**, y **confirmo**.
>
> **El predictor esta prediciendo en las dos direcciones a la vez y sin fallar en
> dieciocho tiros.**

> **LA TABLA DEL PREDICTOR NO VIVE AQUI.** Vive **una sola vez**, en
> `MARCADOR DE LA CLASE`, y se recomputa del archivo con el resto del marcador.
> Aqui solo se cuenta lo que esta tanda le anadio.

**Las 47 de dos libros estan todas leidas desde la tanda 17 anterior**, y las 81
de un solo libro tambien: **la cola cerro en 128 de 128.**

> **Consecuencia para lo que queda, y hay que decirla sin adornos**: si el
> predictor se sostiene, **de las 27 que faltan cabe esperar una o dos costuras,
> no mas**. La cola ya dio lo que tenia que dar. **Eso no es motivo para dejar de
> leerla**, porque la tasa del 6% no es cero y porque el compromiso es leerla
> entera, **pero si lo es para no esperar de ella lo que ya no tiene.**

### Lo que queda por leer, recontado del instrumento

| dominio | citas sin leer |
|---|---:|
| quality | **13** |
| seguridad_digital | 4 |
| exportacion | 3 |
| health_safety | 3 |
| environmental | 2 |
| franquicias | 2 |
| **core** | **0** |
| | **27** |

---

## TANDA 18: una sola cita, y el corte 7 tampoco basta

**`quality/control_estadistico_de_procesos`, 10 pasos. Bloque 47,2, pareja 53,0,
corte 7.** *Juran's Quality Handbook* (Defeo), **fuente unica**.

**FALSA. SECUENCIA LEGITIMA**, y la prueba esta en el par de pasos que mas se
parecen:

| paso | que dice | que hace |
|---:|---|---|
| **6** | *decidir la linea central y los limites de control (usualmente mas o menos 3 sigma)* | **elige la REGLA**, antes de tener datos |
| **9** | *calcular limites de control y definir instrucciones de interpretacion y accion* | **aplica esa regla A LOS DATOS** ya recogidos |

> **Entre los dos hay tres pasos que son justamente lo que falta para poder
> calcular**: elegir subgrupos racionales (7) y montar el sistema de recoleccion
> (8). **El 9 no repite al 6: lo continua**, porque sin el 7 y el 8 no hay con
> que calcular nada. **Es la doctrina de continua-o-repite en su forma mas
> limpia.**

**Los diez pasos son un solo procedimiento de principio a fin**, del que
caracteristica graficar hasta interpretar el grafico. **No hay segundo bloque: hay
un procedimiento largo**, como las seis de la tanda 17.

> **Y el corte 7 se estrena en falso.** Hasta ahora la ficha tenia medido que el
> corte 3 no predice; **este es el primer corte alto que se lee en la banda baja
> y tambien sale falso**. La lectura que deja: **el corte mide donde cambia el
> vocabulario, no si hay dos narraciones.** Un procedimiento de diez pasos cambia
> de vocabulario varias veces por dentro sin dejar de ser uno solo.

**DECIMONOVENA cita de una sola fuente seguida sin una costura.** La racha sigue
viva: seis de la tanda 15, seis de la 16, seis de la 17 y esta.

---

## TANDA 19: seis mundos, cuarta tanda en blanco, y la racha llega a veinticinco

**Seis citas, LAS SEIS FALSAS.** Cuarta tanda consecutiva sin una sola
confirmada, y **segunda tanda entera de mundos**: cinco dominios distintos y
ninguna de `core`.

**Banda de bloque 46,6 a 46,9, y esa banda tambien queda agotada**: el
instrumento tiene **diez citas** ahi dentro, **cuatro ya estaban leidas** y estas
seis eran las que faltaban. Anatomias y fuentes verificadas contra el grafo.

| cita | dominio | pasos | bloque | corte | fuente unica |
|---|---|---:|---:|---:|---|
| `estrategia_recoleccion_datos_carbono` | environmental | 6 | 46,9 | **3** | *The Green to Gold Business Play* (Esty) |
| `rol_alta_direccion_calidad` | quality | 6 | 46,9 | **3** | *Juran's Quality Handbook* (Defeo) |
| `getting_started_maintenance` | seguridad_digital | 6 | 46,9 | **3** | *NIST SP 1318: Protecting CUI (SP 800-171 r3)* |
| `cultura_de_reporte` | health_safety | 6 | 46,8 | **3** | *Managing the Risks of Organizational Accidents* (Reason) |
| `viaje_diagnostico_remedial` | quality | 8 | 46,7 | 4 | *Juran's Quality Handbook* (Defeo) |
| `evaluacion_riesgo_calidad_organizacional` | quality | 8 | 46,6 | 5 | *Juran's Quality Handbook* (Defeo) |

**Las seis son SECUENCIA LEGITIMA**, y las dos de ocho pasos lo enseñan mejor que
ninguna:

> **`viaje_diagnostico_remedial` es el viaje entero de Juran en su orden
> canonico**: sintomas, teorias, prueba de teorias, causa raiz, remedio, prueba
> del remedio, resistencia al cambio y controles nuevos. **Ocho pasos que no se
> pueden reordenar**, porque cada uno necesita el anterior. **Eso es lo contrario
> de una costura.**
>
> **`evaluacion_riesgo_calidad_organizacional` es lo mismo con otra evaluacion**:
> equipo, objetivos, alcance, plan de comunicacion, pre-evaluacion, recoleccion,
> documentacion con puntaje y FODA final. **Un procedimiento largo, no dos
> narraciones.**

### LA RACHA LLEGA A VEINTICINCO, y las cifras son del archivo

> **VEINTICINCO citas de UNA SOLA FUENTE leidas seguidas, y CERO costuras.** Seis
> en la tanda 15, seis en la 16, seis en la 17, una en la 18 y seis en esta.

> **LA TABLA DEL PREDICTOR NO VIVE AQUI.** Vive **una sola vez**, en
> `MARCADOR DE LA CLASE`, y se recomputa del archivo con el resto del marcador.
> Aqui solo se cuenta lo que esta tanda le anadio.

**Las tres confirmadas de un solo libro son de hace mucho.** La tasa de esa mitad
**ha bajado del 6% al 5% sin que ninguna nueva confirme**, que es lo que pasa
cuando el denominador crece y el numerador no se mueve.

> **Y esto ya no es una prediccion, es una medicion cerrada**: **las 20 citas que
> quedan son de un solo libro sin excepcion**, igual que las 25 anteriores. **Si
> la tasa del 5% se sostiene, de las 20 restantes sale UNA costura, o ninguna.**

### Lo que queda por leer, recontado del instrumento

| dominio | citas sin leer |
|---|---:|
| quality | **9** |
| seguridad_digital | 3 |
| exportacion | 3 |
| health_safety | 2 |
| franquicias | 2 |
| environmental | 1 |
| **core** | **0** |
| | **20** |

---

### NOTA DE RACIMO: `cultura_de_reporte` es VECINA, no miembro

**Verificado contra `docs/RACIMOS_MIEMBROS.jsonl`: `cultura_de_reporte` NO esta
en la nomina de los veinte del racimo *No culpar a la persona, arreglar el
sistema*, ni en ninguna otra de las 32.**

**Pero es pariente tematico directo, y sus propios pasos lo dicen:**

| paso | que instala |
|---:|---|
| **1** | **indemnidad** ante sanciones disciplinarias para quien reporta honestamente |
| **2** | **confidencialidad** o des-identificacion de los reportes |
| **3** | **separacion organizacional** entre quien recibe el reporte y quien sanciona |

> **Eso es la cultura justa de Reason**, que es exactamente la doctrina del racimo
> de los veinte: *preguntar que y no quien*, *el error humano como sintoma*, *la
> teoria de la manzana podrida*, *el ciclo de culpa*. **El racimo dice por que no
> hay que culpar; este nodo monta el mecanismo que hace posible no culpar.**

> **QUEDA ANOTADA COMO VECINA Y NO COMO MIEMBRO, y la distincion importa**: el
> censo de las 32 nominas esta **cerrado** y se reconstruyo de los veredictos de
> la franja. **Meterla dentro cambiaria un conteo ya cuadrado y auditado.**
> **Vecina significa una sola cosa: cuando el racimo se lea entero, este nodo se
> lee con el.** No entra en el censo, entra en la lectura.

---

## TANDA 20: quinta en blanco, y la racha llega a treinta y una

**Seis citas, LAS SEIS FALSAS.** Quinta tanda consecutiva sin una sola
confirmada. **Banda de bloque 45,9 a 46,4, y tambien queda agotada**: el
instrumento tiene **diez citas** ahi dentro, **cuatro ya estaban leidas** y estas
seis eran las que faltaban. Anatomias y fuentes verificadas contra el grafo.

| cita | dominio | pasos | bloque | corte | fuente unica |
|---|---|---:|---:|---:|---|
| `funcion_protect_politica_seguridad` | seguridad_digital | 8 | 46,4 | 5 | *Cybersecurity for Small Business* (FTC/NIST CSF) |
| `diseno_para_factores_criticos_y_error_humano` | quality | 6 | 46,4 | **3** | *Juran's Quality Handbook* (Defeo) |
| `prevencion_violencia_laboral` | health_safety | 7 | 46,2 | **3** | `SMALL_BUSINESS` |
| `desarrollar_caracteristicas_proceso_2` | quality | 6 | 45,9 | **3** | *Juran's Quality Handbook* (Defeo) |
| `planificacion_estudio_capacidad` | quality | 9 | 45,9 | 5 | *Juran's Quality Handbook* (Defeo) |
| `getting_started_planning` | seguridad_digital | 7 | 45,9 | 4 | *NIST SP 1318: Protecting CUI* |

**Las seis son SECUENCIA LEGITIMA**, y la de nueve pasos es la que mejor lo
enseña: **`planificacion_estudio_capacidad` es un estudio de capacidad de proceso
de principio a fin**, y nueve pasos ahi no son dos narraciones sino un
procedimiento que no se puede acortar.

> **NOTA SOBRE `desarrollar_caracteristicas_proceso_2`, y no se adjudica aqui.**
> Su id es **miembro de las 36 parejas de sufijo**, con
> `desarrollar_caracteristicas_proceso` de pareja, y **eso lo gobierna la DECISION
> 4 de la mesa de racimos**, aprobada el 9 ago 2026: la familia de ids se arregla
> **de una vez**, con el criterio continua-o-repite y **fusion con alias** para que
> ningun id viejo quede muerto.
>
> **Como COSTURA es FALSO**, que es la unica pregunta de esta ficha. **Lo del
> nombre le toca a la familia D4**, y las dos cosas son ciertas sin corregirse.
> Es el mismo reparto que ya se escribio para `desarrollo_caracteristicas_producto`.

### LA RACHA LLEGA A TREINTA Y UNA, con cifras del archivo

> **TREINTA Y UNA citas de UNA SOLA FUENTE leidas seguidas, y CERO costuras.**
> Seis en la tanda 15, seis en la 16, seis en la 17, una en la 18, seis en la 19 y
> seis en esta.

> **LA TABLA DEL PREDICTOR NO VIVE AQUI.** Vive **una sola vez**, en
> `MARCADOR DE LA CLASE`. Con esta tanda queda en **47 de dos libros con 43
> confirmadas (91%)** y **67 de un solo libro con 3 (4%)**.

**La tasa de la mitad de un solo libro ha ido del 6% al 5% y ahora al 4%, y
ninguna de esas bajadas viene de un veredicto nuevo en contra**: vienen de que el
denominador crece y **el numerador lleva treinta y una lecturas sin moverse**.

> **Quedan 14 citas y las 14 son de un solo libro.** Al 4%, **lo esperable de las
> 14 es media costura**. La cola se lee entera igual, porque ese es el compromiso
> y porque el 4% no es cero, **pero conviene decir ya que el rendimiento util de
> este instrumento se agoto hace cinco tandas.**

### Lo que queda por leer, recontado del instrumento

| dominio | citas sin leer |
|---|---:|
| quality | **6** |
| exportacion | 3 |
| franquicias | 2 |
| health_safety | 1 |
| environmental | 1 |
| seguridad_digital | 1 |
| **core** | **0** |
| | **14** |

---

## TANDA 21: siete citas, sexta tanda en blanco, y quedan siete

**Siete citas, LAS SIETE FALSAS.** Sexta tanda consecutiva sin una sola
confirmada. **Banda de bloque 45,0 a 45,6**, que tiene dieciseis citas en el
instrumento: **nueve ya estaban leidas** y estas siete eran las que faltaban.
Anatomias y fuentes verificadas contra el grafo.

| cita | dominio | pasos | bloque | corte | fuente unica |
|---|---|---:|---:|---:|---|
| `seguridad_trabajadores_jovenes` | health_safety | 8 | 45,6 | 4 | `SMALL_BUSINESS` |
| `getting_started_supply_chain_risk_management` | seguridad_digital | 6 | 45,6 | **3** | *NIST SP 1318: Protecting CUI* |
| `seleccion_consultor_franquicias` | franquicias | 6 | 45,5 | **3** | *Franchise Your Business* (Siebert) |
| `sistema_manejo_quejas` | quality | 6 | 45,2 | **3** | *Juran's Quality Handbook* (Defeo) |
| `vehiculos_combustibles_alternativos_2` | environmental | 6 | 45,1 | **3** | *The Green to Gold Business Play* (Esty) |
| `certificado_de_origen_coo` | exportacion | 6 | 45,0 | **3** | *A Basic Guide to Exporting* |
| `presentaciones_alta_direccion` | quality | 6 | 45,0 | **3** | *Juran's Quality Handbook* (Defeo) |

**Las siete son SECUENCIA LEGITIMA.** Seis de las siete son de seis pasos y corte
3, que a estas alturas de la cola es el perfil de lo que queda: **procedimientos
cortos de un solo libro donde el corte marca un cambio de vocabulario y no una
segunda narracion.**

> **`vehiculos_combustibles_alternativos_2` se anota sin adjudicar**, igual que
> `desarrollar_caracteristicas_proceso_2` en la tanda 20: **su id es de las 36
> parejas de sufijo y lo gobierna la DECISION 4 de la mesa**, aprobada el 9 ago
> 2026. **Como COSTURA es falso**, que es la unica pregunta de esta ficha.

### LA RACHA LLEGA A TREINTA Y OCHO

> **TREINTA Y OCHO citas de UNA SOLA FUENTE leidas seguidas, y CERO costuras.**

**Con esta tanda el predictor queda en 74 citas de un solo libro y 3 confirmadas,
que sigue siendo el 4%.** La tabla viva esta en `MARCADOR DE LA CLASE`.

> **QUEDAN SIETE CITAS**: cuatro de `quality`, dos de `exportacion` y una de
> `franquicias`. **Las siete de un solo libro.** Al 4%, lo esperable de las siete
> es **cero coma tres costuras**. La cola se termina en la tanda que viene.

---

### NOTA DE CONTRAMODELO: `seguridad_trabajadores_jovenes` y el remedio universal-reencuadrado

**Es el mejor ejemplar que esta campana ha encontrado del eje donde-se-actua, y
lo es porque resuelve el problema SIN nombrar ningun pais.**

**El nodo viene de una fuente estadounidense** (`SMALL_BUSINESS`, la serie de OSHA
para pequena empresa) **y trata de leyes de trabajo infantil, que son de las mas
distintas entre paises que existen.** Y aun asi **es ejecutable en cualquier
jurisdiccion**, porque el reencuadre esta hecho dentro de los pasos:

| paso | como universaliza |
|---:|---|
| **1** | *verificar el cumplimiento de las **leyes locales** de trabajo infantil* |
| **3** | *obtener los permisos que exija la ley **en tu pais o region*** |
| **4** | *aprender las leyes de trabajo infantil **aplicables*** |
| **8** | *capacitaciones formales de seguridad **cuando existan en tu mercado*** |

> **LA FIGURA, y es la tercera del marco-pais**: donde Magnuson-Moss condiciona
> por **DESTINO** y las EAR por **ORIGEN**, este nodo **no condiciona por pais en
> absoluto: reencuadra la instruccion para que la jurisdiccion sea una variable
> del lector.** *Verifica las leyes locales* funciona en los ciento noventa y
> tantos paises a la vez.
>
> **Y por eso su puerta puede estar limpia con razon.** Su unica condicion de
> activacion es *si tu negocio emplea trabajadores menores de 18 anos*, **sin
> pais**, y eso **no es un fallo aqui**: es la consecuencia correcta de haber
> universalizado los pasos. **Cuando el paso no depende de un pais, la puerta no
> tiene que declararlo.**

> **PRECISION SOBRE EL ENCARGO, que decia los pasos 1, 3 y 4 con la formula
> *segun tu pais o region***: verificado contra el grafo, **son CUATRO pasos y
> con CUATRO redacciones distintas**. Solo el paso 3 usa esa formula literal; el
> 1 dice *leyes locales*, el 4 dice *aplicables* y el 8 dice *en tu mercado*.
>
> **La sustancia es correcta y el detalle mejora el hallazgo**: el nodo
> universaliza cuatro veces y **ninguna igual que otra**. Es un contramodelo
> excelente **con una inconsistencia menor de redaccion**, y esa inconsistencia
> es justo lo que una plantilla de reencuadre vendria a arreglar: **si el remedio
> se va a aplicar a muchos nodos, conviene que la formula sea UNA.**

---

## TANDA 22, LA ULTIMA: la cola cierra en 128 de 128

**Siete citas, LAS SIETE FALSAS.** Septima tanda consecutiva en blanco. **Con
esta tanda no queda ni una cita del instrumento sin veredicto propio: 128 de
128.**

| cita | dominio | pasos | bloque | pareja | corte | fuente unica |
|---|---|---:|---:|---:|---:|---|
| `evaluacion_preparacion_empresa_exportar` | exportacion | 6 | 44,6 | 50,2 | **3** | *A Basic Guide to Exporting* |
| `planificacion_cero_defectos` | quality | 7 | 44,5 | 46,2 | 4 | *Quality is Free* (Crosby) |
| `negociacion_acuerdo_representante_extranjero` | exportacion | 8 | 44,4 | 50,8 | 4 | *A Basic Guide to Exporting* |
| `ferias_comerciales_franquicia` | franquicias | 6 | 44,2 | 50,9 | **3** | *Franchise Your Business* (Siebert) |
| `diseno_de_procesos_por_caracteristicas` | quality | 5 | **0,0** | **86,6** | 0 | *Juran's Quality Handbook* |
| `tipos_innovacion_i_ii` | quality | 6 | **0,0** | **84,1** | 0 | *Juran's Quality Handbook* |
| `control_estadistico_metodo_medicion` | quality | 6 | **0,0** | **80,9** | 0 | *Out of the Crisis* (Deming) |

**Las siete son SECUENCIA LEGITIMA.**

> **`planificacion_cero_defectos` es el par sano del Paso 7 de Crosby**, y la
> mesa de racimos ya lo dejo resuelto: **el Paso 7 tiene dos nodos,
> `comite_cero_defectos` y `planificacion_cero_defectos`, y dicen cosas
> distintas con el mismo numero de paso.** Mismo numero, distinto contenido. **Se
> cita la mesa y no se re-adjudica aqui.**

---

### LAS TRES DE SOLO PAREJA, y CHOCA CON EL ENCARGO

**El encargo dice que sus parejas son gemelos intra-quality que el cribado ve por
su via. Verificado contra el instrumento: NO ES ASI, y el motivo es que el campo
`pareja` no significa eso.**

> **`pareja` NO son dos nodos: son DOS PASOS DEL MISMO NODO.** El propio
> `scripts/costuras_internas.py` lo dice en su docstring: *la pareja de pasos mas
> parecida del nodo, en base 1*. **Comprobado en las 128 entradas del archivo:
> las 128 llevan dos enteros, ninguno supera el numero de pasos de su nodo, y el
> rango va de 1 a 25.**
>
> **Las dos senales del instrumento son INTERNAS las dos**, y tiene que ser asi:
> el instrumento se llama costuras INTERNAS. **Ningun gemelo de otro nodo entra
> aqui**, y por eso el cribado intra-dominio es otro eje y no un solapamiento.

**Y al abrir las tres, el hallazgo es mejor que el error: las tres son SIMETRIA
DELIBERADA.**

| cita | los dos pasos que disparan | que son |
|---|---|---|
| `diseno_de_procesos_por_caracteristicas` (86,6) | *verificar que cada meta sea alcanzada por al menos una caracteristica* / *verificar que cada caracteristica sea necesaria para al menos una meta* | **una comprobacion en los dos sentidos**, que es como se verifica una correspondencia |
| `tipos_innovacion_i_ii` (84,1) | *generar ideas bajo el encabezado hacerlo mas grande* / *...hacerlo mas pequeno* | **los dos polos de la misma tecnica**, que no se entienden por separado |
| `control_estadistico_metodo_medicion` (80,9) | *compara entre operadores con el mismo instrumento* / *compara entre instrumentos con el mismo operador* | **el cruce completo de un estudio R&R**, que exige las dos mitades |

> **LAS TRES PAREJAS MAS ALTAS DE LA COLA QUE NO SON UNA COPIA SON, LAS TRES,
> BUENA ESCRITURA.** El eje de pareja, en su extremo superior, **caza la simetria
> del que escribe bien**: quien verifica en los dos sentidos, quien da los dos
> polos, quien cruza las dos variables. **Esa es la ultima leccion del
> instrumento y llega justo al cerrarlo.**

---

### LA COLA CIERRA

> **128 citas del instrumento, 128 veredictos propios.** Ninguna heredada de otro
> informe, ninguna pendiente. **46 confirmadas, 82 falsas, precision 36%.**
>
> **La racha final de un solo libro: CUARENTA Y CINCO citas seguidas sin una sola
> costura.** El predictor cierra en **81 citas de un libro con 3 confirmadas** y
> **47 de dos o mas con 43**.
>
> **El informe de cierre del instrumento esta en `docs/COSTURAS_INTERNAS_RESUMEN.md`,
> detras de la marca `<!-- MANUAL -->`.**

---

## SANO POR DENTRO, GEMELO POR FUERA

**Registrado el 11 ago 2026, con ejemplar doble, desde la relectura R9 del otro
eje.**

**Dos pares del cribado intra-dominio salieron A, o sea que los nodos repiten
entre si, y los cuatro nodos implicados estan declarados FALSOS en esta ficha**,
o sea limpios por dentro:

| par del cribado | veredicto de ESTA ficha | veredicto del intra |
|---|---|---|
| los dos de **SPIN** (puesto 248) | **falsos**, secuencia legitima sin repeticion interna | **A**, repiten entre si |
| los dos de **regalos** (puesto 251) | **falsos** | **A**, repiten entre si |

> **UN NODO PUEDE ESTAR LIMPIO POR DENTRO Y TENER UN GEMELO FUERA.** Las dos
> lecturas son correctas y **ninguna corrige a la otra**: son dos preguntas
> distintas sobre el mismo nodo.
>
> **Y es el ejemplar doble, visto desde este lado, del PUNTO CIEGO que el informe
> de cierre declaro.** Alli el eje intra tapaba el agujero de este instrumento, la
> forma que parte pura. **Aqui este instrumento acierta al declararlos limpios y el
> intra encuentra lo que este no podia ver por diseno.**
>
> **TERCER EJEMPLAR, anadido el 12 ago 2026 desde la relectura R10, y es el mas
> claro de los tres porque esta ficha dejo escrito POR QUE lo declaro falso:**
>
> | par del cribado | veredicto de ESTA ficha | veredicto del intra |
> |---|---|---|
> | **`founder_ceo_succession_process`** (puesto 256 del intra) | **falso**, bloque 51,5: *falso positivo de secuencia legitima por pasos tematicamente ESPEJADOS*, su paso 2 evalua si TUS habilidades encajan y su paso 6 si encaja el perfil de QUIEN TE SUCEDERIA | **A**, repite con `identificacion_necesidad_sucesion_ceo` |
>
> **El espejo interno era real y el gemelo externo tambien.** Un nodo puede tener
> sus propios pasos bien ordenados, sin repetirse a si mismo, y aun asi estar
> contado dos veces en el catalogo.
>
> **CUARTO EJEMPLAR, anadido el 12 ago 2026 desde la relectura R12, Y ES EL
> PRIMERO AL REVES.** Los tres de arriba son nodos que ESTA ficha declaro FALSOS,
> sanos por dentro, y que el intra encontro con gemelo fuera. **Este es
> CONFIRMADA.**
>
> | nodo | veredicto de ESTA ficha | veredicto del intra |
> |---|---|---|
> | **`optimizacion_embudo_get_customers`** (puesto 277 del intra) | **CONFIRMADA**, tanda 14, diez pasos, Blank y Weinberg: **EL TESTEO DICHO DOS VECES** | **A**, repite con `funnel_get_customers_optimizacion` |
>
> **Averiado por dentro Y gemelo por fuera.** Es la cuarta vez que los dos ejes
> caen sobre el mismo nodo y **la primera en que los dos encuentran algo.**
>
> ### LA CURA ACOPLADA
>
> **Este caso obliga a nombrar un tratamiento que no estaba en ninguna ficha.**
>
> > **El destejido y la fusion NO se pueden hacer por separado, en ningun orden.**
> >
> > **Si se desteje primero**, el nodo queda mas corto y el gemelo pasa a cubrir
> > una porcion mayor de lo que queda: la decision de fusion cambia despues de la
> > cirugia. **Si se fusiona primero**, se fusiona arrastrando la mitad ajena que
> > la cirugia iba a quitar, y el superviviente nace con la costura dentro.
> >
> > **Van en el MISMO acto, por el TOQUE UNICO del banco 9.4.** Un solo encargo:
> > destejer la mitad de Weinberg, fusionar lo que queda con el gemelo, y salvar
> > en el superviviente lo que sobreviva a las dos operaciones.
>
> **Lo que hay que salvar, medido en el puesto 277 y anotado alli**: el
> **data-chief** con la revision diaria de las diez o doce metricas clave,
> **escalar primero el programa mas productivo**, y **no optimizar demasiados
> programas a la vez**.
>
> **Anotado en las fichas de los dos ejes**, que es lo que la cura acoplada exige:
> ninguno de los dos frentes puede tocar este nodo sin el otro.

> **QUINTO EJEMPLAR, anadido el 12 ago 2026 desde la relectura R13, y es el
> SEGUNDO del tipo caro:**
>
> | nodo | veredicto de ESTA ficha | veredicto del intra |
> |---|---|---|
> | **`producto_unico_superior`** (puesto 285 del intra) | **CONFIRMADA LEVE**, tanda 13 | **A**, repite con `superioridad_producto_beneficios` |
>
> **Averiado por dentro y gemelo por fuera, igual que el 277.** Le aplica la misma
> **CURA ACOPLADA**: destejer el apendice ajeno y fusionar con el gemelo **en el
> mismo acto**.
>
> **Lo que hay que salvar, medido en el puesto 285**: los **discursos por
> posicionamiento** (si eliges premium NO enumeres caracteristicas, si eliges
> precio bajo SI), **desarmar el producto de la competencia**, **imaginar como
> evolucionara**, las **necesidades que el cliente no sabe nombrar**, y los
> **proveedores que pueden innovar contigo**.
>
> **SEXTO EJEMPLAR, anadido el 12 ago 2026 desde la relectura R17, y es el TERCERO
> del tipo caro. Ademas obliga a corregir una clasificacion del encargo:**
>
> | nodo | veredicto de ESTA ficha | veredicto del intra |
> |---|---|---|
> | **`propuesta_gasto_capital`** (puesto 331 del intra) | **CONFIRMADA**, doce pasos, **DOBLE**, y ademas **el PRIMER FALSO NEGATIVO** del instrumento, el nodo por el que el umbral de bloque bajo de 45 a 44 | **A**, repite con `analisis_de_gastos_de_capital` |
>
> **El encargo lo llamaba una falsa reaparecida. No lo es: es confirmada**, y por
> eso entra en el grupo caro y no en el barato.
>
> **Y su cura no es doble sino TRIPLE.** Esta ficha ya habia medido que este nodo
> **esta encadenado con un vecino generico**, `calculo_roi` a
> `comparacion_metodos_inversion` a `propuesta_gasto_capital`, **con el generico
> primero**, y que aun asi la costurada vuelve a derivar lo mismo. **Los tres
> movimientos van en un solo acto**: destejer el apendice, fusionar con el gemelo,
> y **mirar antes al vecino generico**, porque parte del material duplicado puede
> sobrar del todo si `calculo_roi` ya lo cubre.

> **SEPTIMO EJEMPLAR, anadido el 13 ago 2026 desde la relectura R19, y es el
> CUARTO del tipo caro:**
>
> | nodo | veredicto de ESTA ficha | veredicto del intra |
> |---|---|---|
> | **`key_partners_hypothesis`** (puesto 361 del intra) | **CONFIRMADA**, bloque **51,7**, catorce pasos, **TRIPLE**: el Canvas en 1 a 5, el libro de traccion en 6 a 10, las alianzas por cuello de botella en 11 a 14 | **A**, repite con `partners_hypothesis_physical` |
>
> **Averiado por dentro y gemelo por fuera. Cura acoplada**, destejer y fusionar
> en el mismo acto.
>
> **Lo que hay que salvar, medido en el puesto 361**: una sola cosa, la
> **validacion posterior con reuniones reales** del nodo chico. Las otras dos que
> el encargo daba por perdidas **ya viven dentro del grande**: la tabla de tres
> columnas es su **entregable literal** y los suplentes son su **paso 1**.
>
> **Y este ejemplar es distinto de los tres anteriores en una cosa util**: el nodo
> chico **es** el bloque 1 a 5 del grande, asi que **cualquier destejido plausible
> deja el Canvas en pie** y el superviviente sigue conteniendolo. Por eso su par
> **entra a la cola de relectura post-cirugia SIN quedar congelado**, que es el
> primer caso de esa distincion. **Anotado en PENDIENTES.**

> **OCTAVO EJEMPLAR, anadido el 13 ago 2026 desde la relectura R20, y es el
> QUINTO del tipo caro:**
>
> | nodo | veredicto de ESTA ficha | veredicto del intra |
> |---|---|---|
> | **`split_testing_experimentos_ab`** (puesto 374 del intra) | **CONFIRMADA**, nueve pasos, corte 6, **DOBLE**: el A/B de Ries en 1 a 5 y el grupo de control de Rackham en 6 a 9 | **A**, repite con `split_testing` |
>
> **Cura acoplada**, destejer y fusionar en el mismo acto. **Y este nodo ya tenia
> encargo de leerse JUNTO con `ab_testing_optimizacion`**, la otra costurada de
> A/B del nucleo, cuyo par comun (puesto 738) esta congelado: **la cura de los dos
> y la fusion con `split_testing` son el MISMO acto, no tres.**
>
> **Lo que hay que salvar, medido en el puesto 374**: del nodo chico, la
> **significancia estadistica del 95%**. Las otras dos piezas que el encargo daba
> por perdidas, el **cambio porcentual** y el **grupo de control similar**, **viven
> en el bloque de Rackham** y por tanto **se van con el destejido**, no se pierden
> en la fusion.
>
> **Su par entra a la cola SIN congelar** por la regla del banco 9.9: el solape
> cae entero en el bloque 1 a 5 y el destejido se lleva el 6 a 9, asi que lo que
> sobrevive es justo donde el solape vive.

> **NOVENO EJEMPLAR, anadido el 13 ago 2026 desde la relectura R21, y es el SEXTO
> del tipo caro. Ademas es el nodo que MAS PARES CONGELA de todo el archivo:**
>
> | nodo | veredicto de ESTA ficha | veredicto del intra |
> |---|---|---|
> | **`voz_del_cliente_voc`** (puesto 386 del intra) | **CONFIRMADA**, bloque 50,2, diez pasos, **DOBLE DE LA OBSERVACION**: Cooper en 1 a 5, Coleman en 6 a 10, duplicado literal paso 2 contra paso 6 | **A**, repite con `enfoque_mercado_voc` |
>
> **Aqui la frase de la cura acoplada se vuelve literal: destejer y fundir son el
> MISMO acto**, porque el gemelo cubre **justo la mitad que la cirugia deja en
> pie** (los pasos 1 a 5, los de Cooper).
>
> **Lo que hay que salvar, medido en el puesto 386 y ya REPARTIDO por bloques**
> (banco 9.11): **en la fusion**, la evaluacion preliminar de mercado, el analisis
> competitivo detallado y probar los conceptos con clientes reales antes del
> desarrollo formal, los tres de `enfoque_mercado_voc`. **Con el destejido** viaja
> el bloque 6 a 10 entero: observar una vez al mes, ponerse en el lugar del
> cliente, las pepitas de oro, anotar y revisar a los dos dias, y buscar patrones.
>
> **Su par entra a la cola SIN congelar**: el solape cae entero en el bloque de
> Cooper, que es el que sobrevive. **Pero los TRES pares que este nodo congela
> siguen congelados**, y por eso sigue siendo el primero de la cirugia.

> **DECIMO EJEMPLAR, anadido el 13 ago 2026 desde la relectura R22, y es el
> SEPTIMO del tipo caro. Sale de la lista de las VEINTE FUERA DE COLA:**
>
> | nodo | veredicto de ESTA ficha | veredicto del intra |
> |---|---|---|
> | **`metricas_de_adquisicion_activacion`** (puesto 392 del intra) | **fuera de cola**, nueve pasos, **DOBLE**: Blank en 1 a 5 y Weinberg en 6 a 9 | **A**, repite con `build_metrics_toolset` |
>
> **Lo que hay que salvar, YA REPARTIDO por bloques** (banco 9.11): **en la
> fusion**, que el sistema escale luego a retencion y cohortes, de
> `build_metrics_toolset`. **Con el destejido** viajan las tres del bloque de
> Weinberg: definir que es una conversion, comparar el CAC contra el LTV, y usar
> SEM para aprender que mensaje funciona.
>
> **Su par entra a la cola SIN congelar**, con un aviso: **este nodo repite el
> costo de adquisicion a los dos lados de la juntura**, en su paso 3 y otra vez en
> los 7 y 8. **Si el solape de un par futuro cae sobre el CAC, ese par SI
> bloquea.** El 392 no, porque su solape es el montaje del instrumento.

> **UNDECIMO EJEMPLAR, anadido el 13 ago 2026 desde la relectura R25, y es el
> OCTAVO del tipo caro:**
>
> | nodo | veredicto de ESTA ficha | veredicto del intra |
> |---|---|---|
> | **`ab_testing_optimizacion`** (puesto 452 del intra) | **CONFIRMADA**, quince pasos, corte 10, **TRES NARRACIONES**: landing page 1 a 5, metrica unica 6 a 10, canal nucleo 11 a 15 | **A**, repite con `split_testing` |
>
> **Y su cura ya estaba emparejada**: esta ficha dice que este nodo y
> `split_testing_experimentos_ab` se leen juntos porque su destejido converge en
> uno. **Ahora son TRES nodos en el mismo acto**: los dos costurados mas
> `split_testing`, que repite con los dos (374 y 452).
>
> **Lo que hay que salvar, ya repartido** (banco 9.11): **en la fusion**, la
> **significancia estadistica superior al 95%** de `split_testing`, que el
> costurado solo nombra como confianza estadistica sin cifra. **Con el destejido**
> viajan la **saturacion** (paso 15) y el **canal nucleo** (paso 11), los dos del
> tercer bloque.
>
> **Su par entra a la cola SIN congelar** por la regla adjudicada: el solape cruza
> dos junturas, pero el veredicto es invariante.

> **DUODECIMO EJEMPLAR, anadido el 13 ago 2026 desde la relectura R28:**
>
> | nodo | veredicto de ESTA ficha | veredicto del intra |
> |---|---|---|
> | **`seleccion_ceo_fundador`** (puestos 492 y 673 del intra) | **CONFIRMADA**, bloque 46,8, doce pasos, corte 5, **DOBLE DE LA DECISION DE CEO** | **A** con `asignacion_de_titulos_ejecutivos` (492) **y A** con `errores_comunes_asignacion_roles` (673) |
>
> **Dos gemelos declarados, y el primero se leyo hace mucho.** El ejemplar se
> podia declarar desde el 673 y no se declaro: los doce se han encontrado **uno a
> uno, cuando una relectura los cruza**, en vez de barriendo. **Queda propuesto un
> barrido que cruce las confirmadas contra todas las A del archivo de una vez.**

> **DECIMOTERCERO Y CUARTO, el mismo dia y en el mismo par: LA CURA ACOPLADA
> MAYOR** (puesto 494 del intra).
>
> | nodo | veredicto de ESTA ficha |
> |---|---|
> | **`producto_minimo_viable`** | **CONFIRMADA**, bloque **80,2**, veintidos pasos, **CINCO narraciones**, el emblema de la averia |
> | **`principio_calidad_mvp`** | **CONFIRMADA**, bloque 49,2, catorce pasos, **TRES narraciones del mismo MVP** |
>
> **Es la primera cura acoplada de COSTURADA contra COSTURADA**, y por eso son
> TRES movimientos y no dos: destejer el emblema, destejer al pariente, **y solo
> entonces decidir si lo que queda se funde.** Precedente exacto: el puesto **341**,
> blueprint contra journey.
>
> **Su par queda CONGELADO**, y con el motivo mas limpio que ha dado la regla de la
> dependencia: **si el destejido de `principio_calidad_mvp` conserva su narracion
> de la CALIDAD (pasos 1 a 5) el par deja de repetir; si conserva la del CONJUNTO
> MINIMO (11 a 14) sigue repitiendo.** No se puede saber antes de la cirugia.
>
> **Lo que hay que salvar y ninguna de las dos cirugias amenaza**: la distincion
> entre **defectos que impiden aprender** (inaceptables) y **baja fidelidad
> estetica** (aceptable), y el aviso de **no dar por hecho que el estandar de
> calidad de la industria es lo que el cliente valora**.

> **RECUENTO COMPLETO DEL 13 ago 2026: EL BARRIDO SUSTITUYE AL GOTEO.**
>
> **Los ejemplares de arriba se encontraron de uno en uno a lo largo de veinte
> relecturas. El barrido de confirmadas contra las A los cuenta de una vez**, y
> sobre las **46 confirmadas mas las 3 fuera de cola con anatomia** da:
>
> | clase de cura | costuras |
> |---|---:|
> | **SIN GEMELO**, solo destejido | **32** |
> | **CONTRA GEMELO SANO**, destejer y fundir en un acto | **13** |
> | **CONTRA COSTURADA**, acto de tres | **4** nodos en **2** pares |
> | **TOTAL con gemelo** | **17** |
>
> **TRES que el goteo no habia encontrado:**
>
> | costura | sus gemelos |
> |---|---|
> | **`brainstorming_divergente`** | **TRES**: 823, 834 y 844. **Su cura es de CUATRO nodos en un solo acto**, y ademas es el injerto de Mollick: el nodo con mas frentes encima del catalogo |
> | `future_scenarios_planning` | `escenarios_futuros` (711) |
> | `plan_de_adquisicion_acquire` | `plan_acquire_activate` (344) |
>
> **Y prueba un negativo util: los actos de tres son exactamente DOS**, el 341 y
> el 494, **los dos ya registrados. No hay un tercero escondido.**

> **CORRECCION DEL MISMO DIA, y el negativo de arriba queda anulado.** El puesto
> **1061** registro una **TERCERA costurada contra costurada**:
> `ab_testing_optimizacion` contra `optimizacion_embudo_get_customers`, **las dos
> confirmadas**, y congelado por la regla de la dependencia.
>
> **Por que el barrido no lo vio**: cruza las confirmadas contra las **A vigentes
> en el momento de correrlo**, y esa A se registro horas despues, en el tramo
> 1051-1100. **El instrumento no fallo, se quedo viejo**: un barrido contra un
> archivo que sigue creciendo caduca, y hay que volver a correrlo cuando la cola
> avance.
>
> **Cifra viva: DIECISIETE costuras con gemelo (corregido el 14 ago 2026 por el cierre transitivo, seccion 54 del informe: el 1061 unio dos costuras que YA estaban dentro de las diecisiete, asi que cambio la clase del acto y no la cuenta) y TRES actos de tres** (341, 494 y
> 1061).

> **El grupo queda asi: TRES falsas con gemelo** (248, 251, 256) **y DIECIOCHO
> costuras con gemelo**, contadas por barrido y no por goteo. **Las cuatro confirmadas son
> las unicas que necesitan cura acoplada**: en las falsas no hay nada que
> destejer.

> **Los dos instrumentos no se corrigen: se completan.**

---

## COSTURAS FUERA DE COLA

**Lista abierta el 11 ago 2026, despues del cierre del instrumento.**

**El instrumento cerro en 128 de 128 y su informe de cierre no se reabre.** Pero
la cola del instrumento **no era el catalogo entero**: era lo que sus dos senales
cazaron. **Lo que aparezca despues por otra via se anota aqui**, con su anatomia
verificada, y **viaja al plan de la pasada unica por la razon de su veredicto**,
no por el informe cerrado.

> **POR QUE UNA LISTA APARTE Y NO UN ANEXO AL INFORME.** Reabrir un informe
> cerrado para meterle una fila **convierte el cierre en mentira**: la proxima
> lectura no sabria si las 128 son las 128 o son las que habia el dia que se
> escribio. **El informe dice lo que el instrumento vio. Esta lista dice lo que
> aparecio despues.** Las dos cifras siguen siendo verdad por separado.

### LA POBLACION MEDIDA: 20 nodos, no uno

**Medida el 11 ago 2026, disparada por el puesto 590 del cribado intra.** La
lista dejo de ser una anecdota y paso a tener tamano.

**El predictor de fuentes de este instrumento dice que declarar dos o mas obras
en el campo `fuente` es la senal mas fuerte de costura, 91% de aciertos.**
Contado sobre el grafo:

| | |
|---|---:|
| nodos **vivos** que declaran DOS obras en `fuente` | **67** |
| de esos, **entraron a la cola de las 128** | **47** |
| de esos, **NUNCA entraron a la cola** | **20** |

> **VEINTE nodos llevan puesta la senal mas fuerte del instrumento y el
> instrumento no llego a mirarlos.** No es un fallo del cierre: las 128 son las
> 128 que las dos senales cazaron. **Es el tamano real de lo que quedo afuera, y
> ahora esta contado en vez de sospechado.**

**CORRECCION DECLARADA, 13 ago 2026.** Esta tabla mostraba **cuatro A que ya no
existen**: los puestos **490**, **497**, **522** y **624** fueron volteados de A a
D por la ejecucion de la ratificacion, y **el volteo no barrio esta tabla**. Las
filas de abajo ya estan corregidas contra el archivo.

> **Lo que la correccion cambia**: **ninguno de los tres nodos afectados va a cura
> acoplada.** `retention_metrics` y `keep_customers_strategy` **se quedan sin
> gemelo declarado** (les queda un B y un D cada uno), y `fit_problema_solucion`
> **pasa de tres A a una sola**. Su cirugia sigue siendo partirlos; lo que
> desaparece es la fusion que venia pegada.

**Los veinte, con lo que el otro eje ya sabe de ellos:**

| nodo | pasos | las dos obras declaradas | lectura del cribado intra |
|---|---:|---|---|
| `analisis_trafico_competitivo` | 8 | The Startup Owner's Manual mas Traction | 508 **A** |
| `bundle_ideas` | 9 | The field guide to human-centered design mas Essentials of Supply Chain | **sin par en la cola intra** |
| `co_creation_session` | 9 | The field guide to human-centered design mas Essentials of Supply Chain | sin leer aun |
| `criterios_seleccion_proveedores` | 10 | A Project Manager's Book of Forms mas Essentials of Supply Chain | **sin par en la cola intra** |
| `decision_pivote_perseverar` | 9 | The Lean Startup mas Traction | 464 D |
| `diseno_estructura_recompensas_roles` | 7 | The Founder's Dilemmas mas Never Lose a Customer Again | **sin par en la cola intra** |
| `earned_vs_paid_media` | 8 | The Startup Owner's Manual mas Traction | **sin par en la cola intra** |
| `estrategia_crecimiento_clientes` | 10 | The Startup Owner's Manual mas Never Lose a Customer Again | sin leer aun |
| **`fit_problema_solucion`** | 6 | **Value Proposition Design mas Traction** | **490 D, 497 D, 536 A** |
| **`five_whys_inversion_proporcional`** | 9 | **The Lean Startup mas SPIN Selling** | **590 A**, 620 D |
| `gestion_cuentas_por_cobrar` | 9 | Financial Intelligence for Entrepreneurs mas Essentials of Supply Chain | sin leer aun |
| `gestion_inventario` | 9 | Financial Intelligence for Entrepreneurs mas Essentials of Supply Chain | sin leer aun |
| `keep_customers_strategy` | 6 | The Startup Owner's Manual mas Never Lose a Customer Again | 210 B, **624 D** |
| `metricas_de_adquisicion_activacion` | 9 | The Startup Owner's Manual mas Traction | 392 **A** |
| `preguntas_ipo_dolor_cliente` | 7 | The Startup Owner's Manual mas SPIN Selling | sin leer aun |
| `procesamiento_paralelo_con_espirales` | 9 | Winning at New Products mas Essentials of Supply Chain | sin leer aun |
| `relaciones_con_clientes` | 8 | Business Model Generation mas Never Lose a Customer Again | **sin par en la cola intra** |
| **`retention_metrics`** | 9 | The Startup Owner's Manual mas Never Lose a Customer Again | 233 B, **522 D**, 848 D |
| `seleccion_estrategia_pricing` | 6 | The Startup Owner's Manual mas Essentials of Supply Chain | **sin par en la cola intra** |
| `superioridad_producto_beneficios` | 10 | Winning at New Products mas SPIN Selling | 285 **A**, 461 D |

**Tres cosas que la tabla dice y que no se veian antes:**

> **1. Ocho de los veinte ya tienen lectura del otro eje, y seis de esos ocho
> dieron por lo menos una A.** O sea que **el eje intra ya los estaba encontrando
> de rebote**, uno por uno, sin saber que compartian esta marca.
>
> **2. SEIS de los veinte no tienen ni un par en la cola intra.** A esos **no los
> va a encontrar ningun eje**: ni el de costuras, que cerro sin verlos, ni el
> intra, que no tiene por donde entrarles. **Sin esta lista quedaban invisibles
> para siempre.**
>
> **3. `five_whys_inversion_proporcional` es el ejemplar que abrio la medicion**:
> nueve pasos, del 1 al 5 el analisis de incidentes de Ries y del 6 al 9 un bloque
> de VENTAS de Rackham, la causa raiz de las objeciones, revisar grabaciones de
> llamadas y redisenar el entrenamiento. **La costura la declara el propio campo
> `fuente`** y aun asi el nodo nunca entro a la cola.

> **Y el dato que mas ordena el plan**: **`fit_problema_solucion` es al mismo
> tiempo uno de estos veinte y el CENTRO DE REPETICION de la familia del encaje**
> de la seccion 15.6 del informe intra, la que repite con sus otros tres hermanos.
> **El nodo que mas duplica hacia afuera es tambien el que esta partido por
> dentro.** Ese se arregla una sola vez, por el TOQUE UNICO, y el arreglo tiene
> que hacerse **antes** de decidir la arquitectura de la familia.

---

### LAS SEIS QUE NINGUN EJE VOLVERA A MIRAR

**Nombradas el 12 ago 2026 por encargo del fundador, para que la relectura final
las tenga por escrito.**

De los veinte de la tabla de arriba, **seis no tienen NI UN PAR en la cola del
cribado intra-dominio**, verificado contra `docs/INTRA_DOMINIO_PARES.jsonl`.

> **Eso significa exactamente esto: el instrumento de costuras cerro sin verlos y
> el eje intra no tiene por donde entrarles.** Los otros catorce, tarde o
> temprano, salen por un par. **Estos seis no salen por ningun lado.** Si no
> quedan nombrados aqui, **desaparecen del inventario sin que nadie los haya
> leido nunca.**

**Los seis, con el corte aparente verificado sobre sus propios pasos:**

| nodo | pasos | las dos obras | donde se ve el corte |
|---|---:|---|---|
| **`bundle_ideas`** | 9 | *The field guide to human-centered design* mas *Essentials of Supply Chain Management* | **paso 6**. Del 1 al 5 es taller de ideacion, agrupar por tema lo que salio de la lluvia, combinar lo que se complementa, descartar lo que no encaja. Del 6 al 9 es diseno de sistema, listar lo que el sistema tiene que lograr, buscar UNA combinacion de tecnologia que sirva a varios objetivos, y evaluar riesgo y costo de cada combinacion |
| **`criterios_seleccion_proveedores`** | 10 | *A Project Manager's Book of Forms* mas *Essentials of Supply Chain Management* | **paso 7**. Del 1 al 6 es el formulario de puntaje ponderado entero, repartir la importancia hasta sumar cien, calificar, multiplicar y sumar. Del 7 al 10 es abastecimiento, definir que comprar segun el plan de negocio, mirar mas alla del precio, **reducir el numero de proveedores para concentrar volumen** y anotar la lista de preferidos |
| **`diseno_estructura_recompensas_roles`** | 7 | *The Founder's Dilemmas* mas *Never Lose a Customer Again* | **paso 4**. Del 1 al 3 es compensacion por tipo de rol, contingente para los individuales y estable para los colaborativos. Del 4 al 7 es **experiencia del cliente**, auditar si los incentivos premian solo adquisicion, **dar asiento ejecutivo al lider de experiencia**, bonos ligados a retencion y valor vitalicio, y quitar los incentivos que premian rapidez por encima de calidad de relacion |
| **`earned_vs_paid_media`** | 8 | *The Startup Owner's Manual* mas *Traction* | **paso 5**. Del 1 al 4 son las dos listas y la regla de probar en pequeno. Del 5 al 8 es medios **fuera de internet**, preguntar al cliente que consume, pedir el prospecto de audiencia a cada medio, comparar alcance contra precio, y arrancar con radio local, prensa local o vallas |
| **`relaciones_con_clientes`** | 8 | *Business Model Generation* mas *Never Lose a Customer Again* | **paso 5**. Del 1 al 4 es el bloque del lienzo, motivacion por segmento, tipo de relacion, costo de mantenerla y co-creacion. Del 5 al 8 es **comunidad de marca de Coleman**, rituales y simbolos, un momento de iniciacion publico, un vocabulario compartido para los miembros, y conectar clientes nuevos con veteranos |
| **`seleccion_estrategia_pricing`** | 6 | *The Startup Owner's Manual* mas *Essentials of Supply Chain Management* | **paso 5**, y es el mas corto de los seis. Del 1 al 4 y el 6 son de tipo de mercado, comparacion con la competencia, valor unico contra commodity, ingresos recurrentes y validar con clientes reales. **El 5 es el intruso**: calcular el TCO y el ROI si vendes B2B |

> **CINCO DE LOS SEIS parten en dos bloques limpios y el sexto tiene el injerto en
> un solo paso.** `seleccion_estrategia_pricing` es el mas barato de arreglar de
> toda la lista: **un paso que se saca o se enlaza a `analisis_tco_roi_b2b`**, que
> ya existe y ya esta en esta ficha con dos fuentes tambien.

**Y hay una lectura de conjunto que vale para el plan:**

> **De los seis, CUATRO llevan pegado un bloque de dos libros concretos**:
> *Essentials of Supply Chain Management* en tres (`bundle_ideas`,
> `criterios_seleccion_proveedores`, `seleccion_estrategia_pricing`) y
> *Never Lose a Customer Again* en dos (`diseno_estructura_recompensas_roles`,
> `relaciones_con_clientes`).
>
> **Es la misma firma que el informe de cierre ya midio**: Hugos es el libro que
> mas junturas dejo en el nucleo. **Estas seis no son casos raros: son la cola de
> la misma extraccion.**

---

### 1. `core/retention_metrics`, 9 pasos: PRIMERA FUERA DE COLA

**Hallada el 11 ago 2026 en el puesto 522 del cribado intra-dominio**, o sea
**por el otro eje**, no por el de costuras. Anatomia verificada contra el grafo:

**Dos fuentes**: *The Startup Owner's Manual* (Blank) y *Never Lose a Customer
Again* (Coleman).

| bloque | de que habla |
|---|---|
| **1 a 5** | **las metricas de retencion**: visitas y tiempo en sitio por cohorte, tiempo medio entre visitas, vida media y valor de vida del cliente, quejas y tickets, y agrupar por cohorte de mes de ingreso |
| **6 a 9** | **otro asunto entero**: costo de adquisicion exacto **por canal**, punto de equilibrio para recuperarlo, porcentaje de clientes que se van **antes** de ese punto, y presentar el impacto financiero a la direccion |

> **El corte esta en el paso 6 y se ve en el vocabulario.** Del 1 al 5 se mide
> **lo que el cliente hace**; del 6 al 9 se mide **lo que el cliente cuesta**.
> Retencion y economia de adquisicion son dos preguntas, y la segunda entra con
> su propia jerga, CAC, breakeven, impacto financiero.
>
> **Y encaja con el predictor**: declara **DOS libros**, que es la senal que en
> las 128 acerto el 91% de las veces. **La cola no lo tenia y el predictor lo
> habria puesto arriba.**

**POR QUE EL INSTRUMENTO NO LO CAZO, y conviene decirlo porque mide su alcance**:
sus dos senales miden **repeticion**, y aqui **no hay repeticion**: hay **dos
temas distintos pegados**. Ninguno de los nueve pasos repite a otro. **Es la
FORMA QUE PARTE en estado puro, y esa forma solo dispara el instrumento cuando
ademas se repite algo**, que es lo que pasaba en los ocho ejemplares ya
registrados.

> **Lo que esto le dice al plan**: **el instrumento de costuras tiene un punto
> ciego declarado**, los nodos que llevan dos temas **sin repetir nada**. **El eje
> intra-dominio los encuentra de rebote**, porque el nodo con dos temas se parece
> a los dos vecinos de cada tema.

**Destino**: la pasada unica, con **cirugia de la FORMA QUE PARTE**, separar en
dos. **No se toca desde aqui.**

---

### 2. `core/procesamiento_paralelo_con_espirales`, 9 pasos: SEGUNDA FUERA DE COLA

**Hallada el 13 ago 2026 en el puesto 851 del cribado intra**, otra vez **por el
otro eje**. Anatomia verificada contra el grafo:

**Dos fuentes**: *Winning at New Products* (Cooper) y *Essentials of Supply Chain
Management* (Hugos).

| bloque | de que habla |
|---|---|
| **1 a 4** | **Cooper**: areas en paralelo como en el rugby y no como en relevos, versiones tempranas y baratas (bocetos, prototipos virtuales), ciclos rapidos de prueba con clientes, y repetirlos en cada etapa |
| **5 a 9** | **Hugos**: dividir el proyecto en partes independientes, disenar tareas ejecutables en paralelo, asignar por habilidades multiuso, plan B, y disenar para poder recortar funciones sin perder lo esencial |

> **El duplicado literal es el paso 1 contra el paso 6**, los dos mandando
> trabajar en paralelo y no en cascada: uno hablando de **areas** y otro de
> **tareas**. **A diferencia de `retention_metrics`, aqui SI hay repeticion
> interna**, o sea que **el instrumento lo habria cazado si hubiera estado en la
> cola.** Es la firma de Hugos que el informe de cierre ya midio.

**Destino**: la pasada unica, **separar en dos**. Y su par del puesto **851 queda
CONGELADO**, no solo encolado: **el solape del par es justamente la orden
repetida**, asi que el veredicto depende de cual de las dos copias sobreviva.

---

### 3. `core/metricas_de_adquisicion_activacion`, 9 pasos: TERCERA FUERA DE COLA

**Hallada el 13 ago 2026 en la relectura R22 del puesto 392**, otra vez **por el
otro eje**. Anatomia verificada contra el grafo.

**Dos fuentes**: el manual de Blank y *Traction* de Weinberg.

| bloque | de que habla |
|---|---|
| **1 a 5** | **Blank**: que relacion se quiere con el cliente, menos de doce metricas accionables, metricas de adquisicion, metricas de activacion, y montar el tablero |
| **6 a 9** | **Weinberg**: definir que es una conversion **antes** de lanzar campana, calcular CTR, CPC y CPA por campana de prueba, comparar **CAC contra LTV**, y usar **SEM para aprender** que mensaje funciona, no solo para vender |

> **Hay repeticion interna y cruza la juntura**: el **costo de adquisicion** esta
> en el paso 3, dentro del bloque de Blank, y vuelve en los pasos **7 y 8**,
> dentro del de Weinberg. **El instrumento lo habria cazado si hubiera estado en
> la cola.**

**Destino**: la pasada unica, **separar en dos**, y **cura acoplada** con
`build_metrics_toolset`, que es su gemelo declarado.

---

## MARCADOR DE LA CLASE

| | |
|---|---:|
| **CITAS del instrumento leidas** | **128** de **128**, LA COLA ENTERA |
| de esas, costura **confirmada** | **46** |
| de esas, **citas falsas** | **82** |
| **precision de la cola** | **36%** |
| **costuras confirmadas que la cola NO citaba** | **0** |
| **TOTAL de costuras confirmadas** | **46** |

### EL PREDICTOR DE FUENTES, la tabla viva y unica

**Se recomputa del archivo con el marcador, en la misma pasada.**

| | citas leidas | confirmadas | tasa |
|---|---:|---:|---:|
| **nodos de DOS o mas libros** | **47** | **43** | **91%** |
| **nodos de UN solo libro** | **81** | **3** | **4%** |

> **POR QUE ESTA AQUI Y NO EN LAS TANDAS, y es una correccion de estructura mia.**
> Esta tabla llego a existir **dos veces a la vez**, en la seccion de la tanda 17
> y en la de la tanda 19, y **las dos estaban vivas**: yo actualizaba una y
> escribia la otra. **Dos versiones de lo mismo es la averia, no el sintoma.**
>
> **Las dos copias murieron y redirigen aqui.** La tabla es del MARCADOR y no de
> una tanda: **sale de todas las citas leidas, no de las seis ultimas.** Cada
> tanda cuenta lo que anadio y apunta a este sitio.

**Recomputado del archivo con la doctrina de abajo**, cruzando los veredictos
escritos en esta ficha con `docs/COSTURAS_INTERNAS.jsonl`: **128 leidas, 46
confirmadas, 82 falsas, y cada una en exactamente una fila de la tabla de franjas.**

**La serie completa**: 73% con 22 leidas, 68% con 28, 65% con 34, 65% con 40,
61% con 46, 56% con 52, 53% con 58, 53% con 64, 54% con 70, 57% con 76, 55% con
82, 51% con 88, 48% con 94, 48% con 95, 46% con 101, 45% con 102, 43% con 108, 40% con 114, 38% con 121 y **36% con 128, que es el cierre**.

> **Las dos subidas tuvieron causa y las dos bajadas tambien.** Las tandas 12 y
> 13 se ordenaron por la señal de dos fuentes y subieron la precision; **la 14
> mezclo las dos ultimas citas de esa señal con cuatro de bloque y las cuatro
> salieron falsas; la 15 fue entera de bloque y salio ENTERA EN BLANCO.**
>
> **No es que la cola empeore: es que la vena se agoto y lo que queda es lo que
> siempre rindio poco.** Las seis de la tanda 15 declaran **una sola fuente**, y
> las seis salieron falsas. **La tanda 16 repitio el resultado exacto**: seis de
> una sola fuente, seis falsas. **Doce citas seguidas de un solo libro y cero
> confirmadas.**

> **Correccion de conteo, recomputada del archivo y traida sin redondear**: la
> version anterior decia que las SEIS tandas de banda llevaban *14 confirmadas
> contra 22 falsas*. Al recontar cruzando la tabla de franjas de abajo con
> `docs/COSTURAS_INTERNAS.jsonl` salen **15 confirmadas contra 21 falsas** en esas
> seis (3+3+4+2+1+2 confirmadas, 3+3+2+4+5+4 falsas, 36 citas). **El total de 36
> siempre cuadro; el reparto estaba corrido en uno.** Con la septima tanda dentro
> (3 y 3) queda en **18 contra 24**.

> **La segunda tanda con el orden nuevo dio tres de seis**, mejor que la primera
> (dos de seis) y por encima de la media de banda. **Dos tandas siguen sin probar
> el orden nuevo**, y asi queda dicho: la decision de leer primero el nucleo se
> tomo por donde vive la presa confirmada, no por una promesa de rendimiento. Lo
> que si confirma esta tanda es el *donde*: **las tres presas son de `core`, las
> tres falsas tambien, y la banda es la mas baja leida.**

> **Ahi esta el dato que sostiene la decision de orden de abajo**, y conviene
> verlo antes de leerla: **cuatro de las cinco falsas de la ultima tanda son de
> `quality`**, y las cuatro son secuencias de manual, de Juran y de Deming.

### DECISION DE ORDEN DEL AUDITOR: primero el nucleo

**Las 76 citas que quedan por leer se leen priorizando las del NUCLEO.**

> **La cobertura integra queda intacta. Cambia el ORDEN, no el alcance.** Las
> citas de mundo no se descartan ni se muestrean: se leen despues.

**El motivo, con los numeros de esta misma ficha delante:**

- **La presa confirmada vive casi entera en el nucleo**: **28 de las 29
  confirmadas** son de `core`, y la unica excepcion lleva veinticuatro tandas
  sin encontrar companeros de mundo.
- **La banda baja de `quality` rinde secuencias limpias de manual**: en la
  ultima tanda, **cuatro de cinco falsas** eran de ese mundo, y las cuatro
  resultaron ser el mismo genero, un paso de Juran o una secuencia de Deming
  escritos en orden.

> **Lo que esta decision NO dice**: no dice que las citas de mundo esten sanas.
> Dice que **la evidencia acumulada las pone despues en la fila**, y que si la
> lectura se interrumpiera a mitad, **es mejor haber leido el nucleo entero que
> media cola de cada sitio.** Cuando el nucleo se agote, la cola de mundo se lee
> igual y con el mismo paso.

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

**Las ochenta y dos falsas se reparten en TRES clases**: LARGO LEGITIMO
(**7**), FALSO POSITIVO DE SECUENCIA LEGITIMA (**74**) y **DUO LEGITIMO (1)**.

> **La tercera clase se abrio en la tanda 13, despues de treinta y dos falsas sin
> necesitarla**, y se abrio porque la lectura cambio de orden: **al leer por la
> señal de dos fuentes aparecio la primera falsa que es falsa PRECISAMENTE por
> tener dos fuentes bien puestas.**
>
> **DUO LEGITIMO**: dos fuentes distintas dentro de un mismo nodo **en secuencia
> temporal, que no se pisan**. La primera cubre un momento y la segunda el
> siguiente. **No hay narracion repetida ni tema ajeno: hay una cronologia
> repartida entre dos libros, y separarla dejaria media instruccion en cada
> mitad.** Ejemplar: `core/manejo_empleados_en_adquisicion`, con la mecanica del
> deal de Feld en los pasos 1 a 4 y la comunicacion del anuncio de Horowitz en
> los 5 a 9.
>
> **Se distingue de la forma que parte** en que alli el segundo bloque es **otro
> tema** que merece nodo propio; **aqui es el mismo asunto en su momento
> siguiente**. **El duo legitimo no se toca.**

### LA ASIMETRIA, recomputada del archivo, y NO es 19 de 19

**La tanda nueva la refuerza otra vez**: las tres confirmadas son las tres de
`core`. Pero al recontar del archivo la cifra completa **sigue sin salir
redonda**, y la escribo como sale:

| | |
|---|---:|
| **confirmadas en nodos del NUCLEO** | **45** |
| **confirmadas en nodos de MUNDO** | **1** |
| | **46** |

**La excepcion es `quality/planificacion_recoleccion_datos`**, confirmada en el
lote C2 y registrada en esta misma ficha **con su prefijo `quality/` desde el
primer dia**. No es un hallazgo nuevo ni un error de nadie: **es que la cifra de
la asimetria nunca se habia recomputado.**

> **Choca con lo dictado, y por eso lo traigo en vez de escribirlo redondo**: el
> encargo daba por hecho que *las confirmadas siguen siendo todas del nucleo*.
> **Son 45 de 46**, y la excepcion sigue siendo la misma y unica:
> `quality/planificacion_recoleccion_datos` sigue sin encontrar companeros de
> mundo, tanda tras tanda.

**Y hay que separar dos registros que se estaban leyendo como uno**, porque el
choque nace de ahi:

| registro | cuantas | reparto |
|---|---:|---|
| **Las costuras que vio el CRIBADO de la franja** (`FRANJA_INFORME.md`, apartado 4.5) | **21** | **21 de 21 en el nucleo**, verificado nodo por nodo contra el grafo |
| **Las costuras confirmadas por la COLA del instrumento** (esta ficha) | **46** | **45 en el nucleo, 1 en `quality`** |

**Son dos colas distintas, con dos poblaciones distintas, y las dos cifras son
correctas en su sitio.** El *21 de 21* del informe se sostiene; el *todas* de
esta ficha no.

> **Y la excepcion tiene un dato que vale mas que la excepcion**:
> `planificacion_recoleccion_datos` tiene **16 pasos**. **El unico nodo de mundo
> con costura confirmada es un nodo largo**, que es exactamente lo que predice la
> hipotesis abierta de que la asimetria sea **efecto del tamano de los nodos y no
> de su salud** (`FRANJA_INFORME.md`, apartado 10.3).
>
> **Cuando el barrido normalice la tasa de costura por longitud, este es el caso
> que hay que mirar primero**: un mundo produce costura en cuanto tiene un nodo
> lo bastante largo para esconderla.

### LA FRANJA, medida, y la lectura NO es la que parecia

**El dato que se propuso**: *las cuatro falsas viven entre 51 y 52 de señal de
bloque; por encima de 52, doce de doce confirmadas.*

**La primera mitad es exacta.** La segunda no cuadra, y la diferencia cambia lo que
se puede hacer con ella:

**La tabla esta RECONCILIADA: cada una de las 128 citas leidas vive en
exactamente una fila, y las filas suman 128 clavado.**

| franja de señal de bloque | confirmadas | falsas | leidas |
|---|---:|---:|---:|
| **por encima de 52,0** | **9** | **0** | 9 |
| **entre 51,0 y 52,0** | **2** | **4** | 6 |
| **por debajo de 51,0** | **35** | **74** | **109** |
| **sin señal de bloque** (solo pareja) | 0 | **4** | **4** |
| | **46** | **82** | **128** |

**Las seis nuevas de la banda 46,6 a 47,4 caen las seis en la fila de abajo**
(46,6 a 47,4 esta por debajo de 51,0): tres confirmadas (`cliente_disena_producto`
46,6, `seleccion_ceo_fundador` 46,8, `mapa_de_canal_de_ventas` 47,4) y tres falsas
(`ceo_de_guerra_vs_paz` 46,7, `cap_table_basico` 46,9, `metricas_accionables`
47,0). La fila de abajo pasa de **20 y 23** a **23 confirmadas y 26 falsas**.

**Las 128, con su fila y su veredicto**, recontadas cruzando los veredictos de
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
| por debajo de 51,0 | `project_close_out` | 50,3 | confirmada |
| por debajo de 51,0 | `blueprint_de_experiencia` | 50,3 | confirmada |
| por debajo de 51,0 | `voz_del_cliente_voc` | 50,2 | confirmada |
| por debajo de 51,0 | `cultura_de_experiencia` | 50,2 | confirmada |
| por debajo de 51,0 | `auditoria_calidad_proveedores` | 50,2 | **falsa** |
| por debajo de 51,0 | `matriz_de_seleccion` | 50,2 | **falsa** |
| por debajo de 51,0 | `future_scenarios_planning` | 50,1 | confirmada |
| por debajo de 51,0 | `empoderamiento_de_participantes` | 50,1 | confirmada |
| por debajo de 51,0 | `internacionalizacion_sitio_web_exportacion` | 50,1 | **falsa** |
| por debajo de 51,0 | `decision_de_salir_a_bolsa` | 50,0 | **falsa** |
| por debajo de 51,0 | `schedule_management_plan` | 49,8 | confirmada |
| por debajo de 51,0 | `programa_cumplimiento_legal` | 49,8 | **falsa** |
| por debajo de 51,0 | `economia_circular_como_modelo_de_negocio` | 49,7 | confirmada |
| por debajo de 51,0 | `metas_vs_proposito` | 49,7 | confirmada |
| por debajo de 51,0 | `elaboracion_pro_forma_invoice` | 49,7 | **falsa** |
| por debajo de 51,0 | `enfoque_motor_unico_crecimiento` | 49,5 | confirmada |
| por debajo de 51,0 | `principio_calidad_mvp` | 49,2 | confirmada |
| por debajo de 51,0 | `contratacion_experiencia_vs_potencial` | 49,2 | **falsa** |
| por debajo de 51,0 | `actualizacion_posiciones_existentes` | 49,0 | confirmada |
| por debajo de 51,0 | `identificacion_practicas_lideres` | 49,0 | **falsa** |
| por debajo de 51,0 | `analisis_tco_roi_b2b` | 48,9 | confirmada |
| por debajo de 51,0 | `background_startup_vs_corporativo` | 48,8 | **falsa** |
| por debajo de 51,0 | `verificar_modelo_ingresos` | 48,8 | **falsa** |
| por debajo de 51,0 | `customer_journey_mapping` | 48,6 | confirmada |
| por debajo de 51,0 | `elementos_plan_exportacion_ejemplo` | 48,6 | **falsa** |
| por debajo de 51,0 | `organizacion_adaptativa` | 48,5 | confirmada |
| por debajo de 51,0 | `csf_funcion_govern` | 48,5 | **falsa** |
| por debajo de 51,0 | `plan_de_adquisicion_acquire` | 48,3 | confirmada |
| por debajo de 51,0 | `desarrollo_caracteristicas_producto` | 48,3 | **falsa** |
| por debajo de 51,0 | `abolir_inspeccion_masiva` | 48,3 | **falsa** |
| por debajo de 51,0 | `criterios_equity_split` | 48,3 | **falsa** |
| por debajo de 51,0 | `ratios_eficiencia_inventario` | 48,3 | confirmada |
| por debajo de 51,0 | `estratificacion_datos` | 48,2 | **falsa** |
| por debajo de 51,0 | `modelo_hibrido_agile_stage_gate` | 48,1 | confirmada |
| por debajo de 51,0 | `medir_comportamiento_cliente_mvp` | 48,1 | **falsa** |
| por debajo de 51,0 | `distorsion_muestreo_mecanico` | 48,1 | **falsa** |
| por debajo de 51,0 | `respuesta_consultas_internacionales` | 48,1 | **falsa** |
| por debajo de 51,0 | `plan_de_accion_de_emergencia` | 48,1 | **falsa** |
| por debajo de 51,0 | `ganar_comprension_del_cliente` | 48,0 | confirmada |
| por debajo de 51,0 | `fase_affirm_buyers_remorse` | 48,0 | **falsa** |
| por debajo de 51,0 | `design_for_six_sigma_dfss` | 47,6 | **falsa** |
| por debajo de 51,0 | `etapa_testing_validation` | 47,5 | **falsa** |
| por debajo de 51,0 | `make_certain_programa` | 47,5 | **falsa** |
| por debajo de 51,0 | `diseno_de_mejoras_para_clientes` | 47,5 | **falsa** |
| por debajo de 51,0 | `wizard_of_oz_testing` | 47,4 | **falsa** |
| por debajo de 51,0 | `mapa_de_canal_de_ventas` | 47,4 | confirmada |
| por debajo de 51,0 | `export_administration_regulations` | 47,4 | **falsa** |
| por debajo de 51,0 | `control_estadistico_de_procesos` | 47,2 | **falsa** |
| por debajo de 51,0 | `estrategia_recoleccion_datos_carbono` | 46,9 | **falsa** |
| por debajo de 51,0 | `rol_alta_direccion_calidad` | 46,9 | **falsa** |
| por debajo de 51,0 | `getting_started_maintenance` | 46,9 | **falsa** |
| por debajo de 51,0 | `cultura_de_reporte` | 46,8 | **falsa** |
| por debajo de 51,0 | `viaje_diagnostico_remedial` | 46,7 | **falsa** |
| por debajo de 51,0 | `evaluacion_riesgo_calidad_organizacional` | 46,6 | **falsa** |
| por debajo de 51,0 | `funcion_protect_politica_seguridad` | 46,4 | **falsa** |
| por debajo de 51,0 | `diseno_para_factores_criticos_y_error_humano` | 46,4 | **falsa** |
| por debajo de 51,0 | `prevencion_violencia_laboral` | 46,2 | **falsa** |
| por debajo de 51,0 | `desarrollar_caracteristicas_proceso_2` | 45,9 | **falsa** |
| por debajo de 51,0 | `planificacion_estudio_capacidad` | 45,9 | **falsa** |
| por debajo de 51,0 | `getting_started_planning` | 45,9 | **falsa** |
| por debajo de 51,0 | `seguridad_trabajadores_jovenes` | 45,6 | **falsa** |
| por debajo de 51,0 | `getting_started_supply_chain_risk_management` | 45,6 | **falsa** |
| por debajo de 51,0 | `seleccion_consultor_franquicias` | 45,5 | **falsa** |
| por debajo de 51,0 | `sistema_manejo_quejas` | 45,2 | **falsa** |
| por debajo de 51,0 | `vehiculos_combustibles_alternativos_2` | 45,1 | **falsa** |
| por debajo de 51,0 | `certificado_de_origen_coo` | 45,0 | **falsa** |
| por debajo de 51,0 | `presentaciones_alta_direccion` | 45,0 | **falsa** |
| por debajo de 51,0 | `evaluacion_preparacion_empresa_exportar` | 44,6 | **falsa** |
| por debajo de 51,0 | `planificacion_cero_defectos` | 44,5 | **falsa** |
| por debajo de 51,0 | `negociacion_acuerdo_representante_extranjero` | 44,4 | **falsa** |
| por debajo de 51,0 | `ferias_comerciales_franquicia` | 44,2 | **falsa** |
| por debajo de 51,0 | `metricas_accionables` | 47,0 | **falsa** |
| por debajo de 51,0 | `cap_table_basico` | 46,9 | **falsa** |
| por debajo de 51,0 | `seleccion_ceo_fundador` | 46,8 | confirmada |
| por debajo de 51,0 | `ceo_de_guerra_vs_paz` | 46,7 | **falsa** |
| por debajo de 51,0 | `cliente_disena_producto` | 46,6 | confirmada |
| por debajo de 51,0 | `asociaciones_clave` | 46,5 | confirmada |
| por debajo de 51,0 | `modelo_spin_preguntas` | 46,5 | **falsa** |
| por debajo de 51,0 | `reduccion_tamano_de_lote_batch_size` | 46,0 | confirmada |
| por debajo de 51,0 | `publicidad_garantia_conforme` | 46,0 | **falsa** |
| por debajo de 51,0 | `sistema_inmune_producto` | 45,9 | confirmada |
| por debajo de 51,0 | `sales_funnel_get_keep_grow` | 45,9 | confirmada |
| por debajo de 51,0 | `manejo_empleados_en_adquisicion` | 45,7 | **falsa** |
| por debajo de 51,0 | `estrategia_de_innovacion_producto` | 45,7 | confirmada |
| por debajo de 51,0 | `definicion_gatekeepers` | 45,7 | **falsa** |
| por debajo de 51,0 | `plan_gestion_adquisiciones` | 45,7 | **falsa** |
| por debajo de 51,0 | `regalos_estrategicos_sorpresa` | 45,7 | **falsa** |
| por debajo de 51,0 | `posicionamiento_de_empresa` | 45,6 | confirmada |
| por debajo de 51,0 | `retargeting_display` | 45,6 | **falsa** |
| por debajo de 51,0 | `vesting_acciones_fundadores` | 45,4 | **falsa** |
| por debajo de 51,0 | `validar_canal_distribucion` | 45,4 | **falsa** |
| por debajo de 51,0 | `prototipar_con_medios_no_convencionales` | 45,3 | **falsa** |
| por debajo de 51,0 | `gut_check` | 45,2 | confirmada |
| por debajo de 51,0 | `gestion_libro_abierto_obm` | 45,1 | confirmada |
| por debajo de 51,0 | `eventos_offline_como_canal_traccion` | 45,1 | **falsa** |
| por debajo de 51,0 | `preferencia_de_liquidacion` | 45,0 | **falsa** |
| por debajo de 51,0 | `brainstorming_divergente` | 44,8 | confirmada |
| por debajo de 51,0 | `portfolio_management` | 44,7 | **falsa** |
| por debajo de 51,0 | `internal_idea_capture` | 44,7 | **falsa** |
| por debajo de 51,0 | `captura_conocimiento_mercado` | 44,7 | **falsa** |
| por debajo de 51,0 | `lectura_balance_general` | 44,6 | **falsa** |
| por debajo de 51,0 | `sem_estrategia_ejecucion` | 44,3 | **falsa** |
| por debajo de 51,0 | `product_market_fit` | 44,2 | **falsa** |
| por debajo de 51,0 | `producto_unico_superior` | 44,2 | confirmada |
| por debajo de 51,0 | `revisiones_regulares_desempeno_ceo` | 44,2 | confirmada |
| por debajo de 51,0 | `optimizacion_embudo_get_customers` | 44,1 | confirmada |
| por debajo de 51,0 | `propuesta_gasto_capital` | 44,1 | confirmada |
| sin señal de bloque | `dso_dpo_gestion_capital_trabajo` | 0,0 | **falsa** |
| sin señal de bloque | `diseno_de_procesos_por_caracteristicas` | 0,0 | **falsa** |
| sin señal de bloque | `tipos_innovacion_i_ii` | 0,0 | **falsa** |
| sin señal de bloque | `control_estadistico_metodo_medicion` | 0,0 | **falsa** |

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
> **las cuatro estan leidas y las cuatro salieron FALSAS**:
> `dso_dpo_gestion_capital_trabajo` (pareja 81,5) en la tanda 16, y las tres de
> `quality` en la tanda 22. **La fila cierra en 0 confirmadas de 4**, y el eje de
> pareja como senal unica **no cazo ni una costura en toda la campaña**.

**Por encima de 52 son NUEVE de nueve.** Y con la tanda 14 dentro, el reparto de
las **45 confirmadas** es: **9 por encima de 52 y TREINTA Y SEIS por debajo**
(`key_partners` 51,7, `split_testing` 51,5, `project_close_out` 50,3,
`blueprint_de_experiencia` 50,3, `cultura_de_experiencia` 50,2,
`voz_del_cliente_voc` 50,2, `future_scenarios_planning` 50,1,
`economia_circular` 49,7, `ratios_eficiencia_inventario` 48,3,
`propuesta_gasto_capital` 44,1, y las tres nuevas `empoderamiento_de_participantes`
50,1, `schedule_management_plan` 49,8, `metas_vs_proposito` 49,7,
`enfoque_motor_unico_crecimiento` 49,5, `principio_calidad_mvp` 49,2,
`actualizacion_posiciones_existentes` 49,0, `analisis_tco_roi_b2b` 48,9,
`customer_journey_mapping` 48,6, `organizacion_adaptativa` 48,5 y
`plan_de_adquisicion_acquire` 48,3, `modelo_hibrido_agile_stage_gate` 48,1 y
`ganar_comprension_del_cliente` 48,0, y las de las dos ultimas tandas
`mapa_de_canal_de_ventas` 47,4, `seleccion_ceo_fundador` 46,8,
`cliente_disena_producto` 46,6, `asociaciones_clave` 46,5,
`reduccion_tamano_de_lote_batch_size` 46,0, `sistema_inmune_producto` 45,9 y
`sales_funnel_get_keep_grow` 45,9, y las cinco de la tanda 13
`estrategia_de_innovacion_producto` 45,7, `posicionamiento_de_empresa` 45,6,
`gut_check` 45,2, `gestion_libro_abierto_obm` 45,1 y `producto_unico_superior`
44,2, y las dos de la tanda 14 `revisiones_regulares_desempeno_ceo` 44,2 y
`optimizacion_embudo_get_customers` 44,1). **Cuatro veces mas abajo que arriba.**

> **Esto empezo siendo una correccion y ya es la tendencia.** La version original
> decia *tres de ellas viven por debajo de 52*, sobre doce confirmadas; al cuadrar
> la tabla fueron **siete de dieciseis**; con la tanda de la banda 50 son **DIEZ
> de diecinueve**. **La mayoria de las costuras confirmadas del catalogo vive por
> debajo de la franja**, es decir en el terreno donde la señal de bloque es debil.
> **Es el argumento mas fuerte que hay contra acelerar la lectura ahi abajo**, y
> cada tanda nueva lo hace mas fuerte, no menos. **Con 82 leidas van treinta y
> seis de cuarenta y cinco.**

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
> abajo**, donde la muestra leida da **37 confirmadas contra 82 falsas**: la
> moneda ya no esta en el filo, y el motivo es que se acabaron los nodos de dos
> libros.
>
> **Acelerar ahi seria pasar de largo justamente donde esta casi toda la cola, y
> donde ya se sabe que hay costuras reales.** El compromiso de leer la cola entera
> no cambia, **y el paso tampoco deberia aflojarse por debajo de la franja.**

### La prediccion de la zona mezclada se sigue cumpliendo

**Las dos citas nuevas son la comprobacion, y salio la que se esperaba**: las dos
viven **por debajo de bloque 52** (50,9 y 50,3) y **las dos resultaron falsas.**

> **Bajo 52 la señal de bloque no se sostiene sola.** La muestra leida en esa
> mitad de la cola queda, con la cola ya cerrada, en **37 confirmadas contra 82
> falsas**.
>
> **CUARTO PASAJE DERIVADO QUE SE ENCUENTRA DESCUADRADO, y hay que decirlo aqui
> porque esta justo debajo del aviso**: antes de esta tanda esta frase decia *48
> falsas* y la tabla de franjas daba **49** (4 mas 44 mas 1). **Un off-by-one
> que sobrevivio al recomputo de la tanda 12**, en el mismo parrafo que advierte
> de este fallo exacto. **Recontado del archivo, con la tanda 17 dentro, son 55.**
>
> **Nota de recomputo, y explica por que estas cifras saltaron mas de lo esperado**:
> tres pasajes derivados de esta seccion se habian quedado en el estado de la
> tanda 10 (decian *31 confirmadas*, *58 leidas* y *22 contra 27*) mientras el
> marcador ya iba por 64. **Se recomputaron todos del archivo en esta entrada.**
> Es exactamente el fallo que la doctrina del marcador viene a evitar: **el total
> se actualizo y las frases que colgaban de el, no.** Ni piso de ruido ni terreno donde se pueda leer de corrido: una
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

### REGLA PROPIA: cuando el destejido PARTE en vez de podar

**La tabla de arriba supone que al nodo le sobran narraciones DEL MISMO TEMA.**
Hay una forma en la que eso no se cumple, y ya tiene **cuatro ejemplares
leidos**, asi que deja de ser excepcion:

| ejemplar | que contiene de mas |
|---|---|
| `blueprint_de_experiencia` | 17 pasos: el blueprint **y** el ritual de bienvenida |
| `metas_vs_proposito` | 14 pasos: Goodhart dos veces **y** el deseo real del cliente detras del objetivo declarado |
| `analisis_tco_roi_b2b` | 9 pasos: el vendedor B2B **y** el comprador ponderando proveedores |
| `enfoque_motor_unico_crecimiento` | 9 pasos: el motor de crecimiento **y** el canal Bullseye |

> **REGLA: el nodo costurado que contiene un TEMA AJENO se PARTE, no se poda.**
> Aplicarle la narracion canonica de 3 a 6 pasos obligaria a tirar material que
> no sobra: **lo que sobra es la repeticion, no el segundo tema.**

**Y la regla tiene una segunda mitad, para el caso en que el tema ajeno no sea
solo otro tema sino de otro MUNDO:**

> **Si el tema ajeno pertenece a un mundo, se evalua TRASPLANTE en vez de nodo
> nuevo en el nucleo.** El caso vivo es `analisis_tco_roi_b2b`: sus pasos 5 a 9
> son doctrina de `compras`, donde ya viven `matriz_de_seleccion` y
> `decide_criterio_eleccion_proveedor`.
>
> **Condicion del trasplante, y es dura a proposito: solo si viaja TEXTO, con su
> registro de procedencia.** Mover una idea sin su texto no es trasplantar, es
> **volver a escribirla de memoria en otro sitio**, y eso es exactamente el
> mecanismo que produjo la duplicacion que esta campana viene a deshacer. **Si el
> texto no puede viajar, se parte en el nucleo y se deja anotado el parentesco
> con el mundo.**

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

> **SOSTENIDO EN RELECTURA A CIEGAS (11 ago 2026).** Este par es tambien el
> **puesto 244 del cribado intra-dominio**, donde salio **A**, y la **tanda R8 de
> la relectura lo adjudico con las razones tapadas y coincidio**. **TRES EJES lo
> han mirado y los tres dicen lo mismo**: el gradiente lo llamo el mas pegado, el
> intra le dio A, y la ciega lo sostiene.
>
> **Y la relectura anade lo que ninguno de los tres daba: que se pierde.** De
> `innovacion_abierta` viajan **el sindrome NIH** (evaluar cuanto hay en la
> organizacion) y **los metodos-segun-complejidad** del producto y la industria.
> De `open_innovation_ideacion` viaja **adaptar el Stage-Gate para manejar ideas,
> IP y tecnologias externas**. **Las tres son perdidas de LECTOR**, por la
> distincion del banco 9.7.

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

> **SOSTENIDO EN RELECTURA (11 ago 2026).** Este par es tambien el **puesto 184
> del cribado intra-dominio**, donde salio **A REPITE**, y la **tanda R4 de la
> relectura lo volvio a mirar y lo sostiene**. **Los dos ejes coinciden y la
> segunda lectura no lo tumba.**
>
> **Y la relectura anade lo que ninguno de los dos ejes daba: que se pierde al
> fusionar.** De `scoring_model_scorecard` viajan **dos cosas que el otro no
> tiene**: usar **un scorecard distinto segun el TIPO de proyecto**, y combinar el
> puntaje con **otro indicador de productividad** para ordenar la cartera.
> **Fusionar sin llevarselas convierte un scorecard de dos dimensiones en uno de
> una.**

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
