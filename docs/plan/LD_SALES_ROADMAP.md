# LAS CINCO DEL SALES ROADMAP . `LD-66` a `LD-70`

**Encargadas el 14 ago 2026 en la vuelta 18 del bucle**, por la adjudicacion del
pendiente de doctrina 4 de la vuelta 17 (`docs/loop/ACTA_AUDITOR.md` VUELTA 17,
seccion 4): *"la pregunta de P.5 (UNA familia o DOS) la gobierna P.5, y sus cinco pares
ya estan cuantificados como deuda de P.5. Se leen como dirigidas antes de cualquier
fusion del acto."*

> **LECTURA DIRIGIDA: no entran en la cola y NO MUEVEN SU MARCADOR.** El cribado sigue
> **CERRADO en 3.388 de 3.388**, y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` **no se toca**.

**LOS CINCO SON PARES FUERA DE COLA**, nombrados por primera vez en la vuelta 17
(`RECOMPUTO_3388.md`, seccion "TAREA (vuelta 17)", punto 4). **No hay razon previa que
tapar**, asi que la lectura a ciegas no aplica. Se leyeron con la vara del banco
**9.6.1** y sus dos precisiones, **9.6.2 la vara tiene direccion** y **9.6.3 el tamano
del solape no decide**, mas las quince reglas del banco del plan.

**Instrumento de esta vuelta, de solo lectura:**
`scripts/loop/vuelta18_sales_roadmap.py`, sobre `dataset/metadata/master_graph.json`,
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y `docs/plan/OPERACIONES.jsonl`. **El script no
pone ninguna clase: las clases son de la lectura.** Lo que el script mide es lo que la
lectura no puede medir a ojo: el cableado, las componentes conexas y la prueba de corte.

---

## EL SALDO, primero

| | |
|---|---:|
| lecturas | **5** |
| **A** | **1** |
| **D** | **4** |
| B o C | **0** |

**Y CON ELLAS LA COBERTURA DEL ACTO CIERRA: de los quince pares posibles entre sus seis
nodos, los quince estan leidos.** Diez estaban en el archivo (6 A y 4 D, remedidos en
esta vuelta con instrumento propio) y **estos cinco los cierran**. El acto pasa de
**10 de 15** a **15 de 15**, y **su deuda de P.5 queda en CERO**.

| | antes de estas cinco | despues |
|---|---:|---:|
| pares leidos | 10 de 15 | **15 de 15** |
| A del acto | 6 | **7** |
| D del acto | 4 | **8** |

---

## `LD-66` . `customer_validation_sales_roadmap` contra `estrategia_de_ventas` . **D**

> **LA ECONOMIA DE LA VENTA CONTRA EL MAPA DE ACCESO, y es exactamente el mismo par que
> el puesto 872 ya resolvio con el otro nodo de mapa.**
>
> `customer_validation_sales_roadmap` mide **si la venta funciona**: definir quien
> influye, recomienda y decide la compra; identificar **donde esta el presupuesto
> disponible**; determinar **cuantas llamadas de venta y cuanto tiempo toma cerrar una
> venta**; y probar el proceso de venta completo **con ordenes reales a precio completo
> antes de escalar**.
>
> `estrategia_de_ventas` decide **como se entra**: en que nivel de la organizacion
> entrar, ejecutivo o staff operativo; cuantas personas del mapa organizacional deben
> decir que si; el orden de contacto y **el guion para cada persona**; y que paso podria
> hacer fracasar toda la venta y **quienes son los posibles saboteadores**.

**Lo compartido es UNA linea**, quien decide la compra, que el primero enuncia en su
paso 1 y el segundo cuenta en su paso 2. **Por 9.6.3, lo que se pesa es el resto, y en
los dos lados el resto es procedimiento:** en el primero, el presupuesto, el ciclo de
cierre y la prueba con ordenes reales, que es una secuencia con su propia logica y su
propio entregable; en el segundo, el nivel de entrada, el orden, el guion y los
saboteadores, que es otra. **CONTINUA.**

> **Y CAE BAJO EL PRECEDENTE ESCRITO DEL PUESTO 872**, que separo a este mismo nodo de
> `hoja_de_ruta_de_ventas` con estas palabras: *"la ECONOMIA de la venta contra el MAPA
> de acceso"*. **`estrategia_de_ventas` es el tercer nodo de mapa del acto**, y la
> relacion es la misma. **La vara aguanta el caso nuevo sin retocarse.**

---

## `LD-67` . `customer_validation_sales_roadmap` contra `sales_roadmap` . **D**

> **La misma figura del `LD-66`, contra el mas corto de los nodos de mapa.**
>
> `sales_roadmap` dice tres cosas y nada mas: identificar **los roles clave** dentro de
> la empresa a la que se le vende, quien usa el producto, quien lo compra y quien decide
> el gasto; definir **el orden de contacto y el mensaje especifico para cada rol**; y
> **escribir el proceso paso a paso para poder repetirlo**.
>
> `customer_validation_sales_roadmap` comparte con el **su paso 1 y solo ese**.

**Lo que queda fuera del solape, y en que lado:** del lado de `sales_roadmap`, el orden
de contacto, el mensaje por rol y **la escritura del proceso repetible**, que es el
entregable del nodo; del lado del otro, el presupuesto, el conteo de llamadas, el tiempo
de cierre y **la prueba con ordenes reales a precio completo antes de escalar**.
**Procedimiento en los dos lados: por 9.6.3 el par es SANO. CONTINUA.**

**LO QUE ESTA LECTURA CIERRA, y hay que decirlo porque cambia la forma del acto:** con
esta, **`customer_validation_sales_roadmap` queda leido contra los CUATRO nodos de mapa
del acto y los cuatro salen D** (872 contra `hoja_de_ruta_de_ventas`, 1023 contra
`refinar_sales_roadmap`, `LD-66` contra `estrategia_de_ventas` y esta contra
`sales_roadmap`). **Su unica A en todo el acto es el puesto 319**, contra
`sales_roadmap_vs_sales_force`.

---

## `LD-68` . `estrategia_de_ventas` contra `hoja_de_ruta_de_ventas` . **A**

**Es la unica A de la tanda, y es la que contesta la mitad de la pregunta de P.5.**

> **DOS PASOS IDENTICOS, no parecidos.** El paso 2 de `estrategia_de_ventas`,
> *determina cuantas personas del mapa organizacional deben decir si*, es el paso 2 de
> `hoja_de_ruta_de_ventas`, *identifica cuantas personas deben decir si para cerrar una
> venta*. Y el paso 3 del primero, *establece el orden de contacto y el guion para cada
> persona*, es el paso 3 del segundo, *determina el orden correcto de contacto con los
> distintos stakeholders*.

**Aplicada la vara en la direccion que manda 9.6.2, y el reconocimiento previo primero:
NO es un par madre e hijo**, porque ninguno de los dos cabe entero dentro de un paso del
otro: los pasos compartidos son **el mismo material dicho dos veces**, no un
procedimiento que uno nombra y el otro despliega. **Asi que decide 9.6.3: que queda
fuera del solape, y en que lado.**

| lo que queda fuera | en que lado | que es |
|---|---|---|
| el **nivel de entrada** (ejecutivo o staff) y **quienes son los saboteadores** | `estrategia_de_ventas` | **dos lineas**, dos decisiones sueltas sin secuencia propia |
| actualizar los mapas de organizacion e influencia **con hallazgos reales**, crear **el mapa de acceso** a la primera reunion, y disenar **el plan de implementacion** desde el si verbal hasta el cobro | `hoja_de_ruta_de_ventas` | **procedimiento**, y esta medido abajo |

> **Lineas de un lado y procedimiento del otro: REPITE.** `estrategia_de_ventas` es
> **el contenido del mapa de acceso** que `hoja_de_ruta_de_ventas` nombra en su paso 4.

### LA MEDICION QUE SOSTIENE QUE EL RESTO DE `hoja_de_ruta_de_ventas` ES PROCEDIMIENTO

**Por 9.6.2, la prueba de que un paso es un procedimiento nombrado en una linea es que
existe el hijo que lo ejecuta.** Medido con el instrumento de esta vuelta sobre el
grafo, **los cuatro hijos existen los cuatro**:

| el paso de `hoja_de_ruta_de_ventas` | el hijo que lo ejecuta | existe | la madre lo enlaza |
|---|---|:--:|:--:|
| 1, actualizar los mapas de influencia | `mapa_de_influencia` | **si** | **si** |
| 2 y 3, cuantos firman y en que orden | `estrategia_de_ventas` | **si** | no |
| 4, el mapa de acceso al cliente | `mapa_de_acceso_al_cliente` | **si** | no |
| 5, el plan de implementacion | `plan_de_implementacion_de_venta` | **si** | no |

**LA SILUETA DE 9.6.1 SE MIDE Y NO SE SUPONE: la madre enlaza a UNO de sus CUATRO hijos
con casa propia**, o sea **la mitad o menos**. Por la regla, *la silueta ni exculpa ni
acusa y manda el contenido*, que es lo que se acaba de leer arriba. **La arista que
falta no se cobra como acusacion.**

> **Y HAY UN DATO DE GRAFO QUE HAY QUE DECIR, porque apunta al mismo sitio que la
> lectura:** `estrategia_de_ventas` tiene a **`mapa_de_acceso_al_cliente` entre sus
> `nodos_previos`** y a **`plan_de_implementacion_de_venta` como su unico
> `nodos_siguientes`**. **El nodo esta cableado exactamente en el hueco que la lectura le
> asigna: entre el paso 4 y el paso 5 de la madre.** El cableado no decide (banco 9.8:
> desempata, no decide), pero **aqui no desempata nada: coincide con lo que ya dijo el
> contenido.**

---

## `LD-69` . `estrategia_de_ventas` contra `refinar_sales_roadmap` . **D**

> **El contenido del mapa contra el procedimiento de construirlo, validarlo y usarlo.**
>
> `refinar_sales_roadmap` trae seis pasos: identificar **el tipo de organizacion del
> cliente** (por producto, funcion, matriz o franquicia); construir un **mapa de
> estrategia de acceso** determinando por donde entrar; detectar **patrones de peligro**
> como los concursos formales, las exigencias de demostracion o la negativa a comprarle a
> una startup; **documentar cada paso del proceso de venta en un diagrama de flujo**;
> **validar el mapa repitiendolo con exito en varias cuentas**; y **usarlo como prueba de
> competencia al contratar un director de ventas**.

**Lo compartido son dos lineas y no mas:** el paso 2 de
`refinar_sales_roadmap`, *por donde entrar*, es el paso 1 de `estrategia_de_ventas`, *en
que nivel de la organizacion entraras*; y su paso 3, *los patrones de peligro*, roza el
paso 4 del otro, *que paso podria hacer fracasar la venta*. **Y el roce es parcial: los
peligros del primero son del proceso de compra, los del segundo son personas dentro de
la cuenta.**

| lo que queda fuera | en que lado | que es |
|---|---|---|
| cuantas personas deben decir si, el orden de contacto y **el guion para cada una** | `estrategia_de_ventas` | **procedimiento**: es la secuencia que produce el mapa de acceso, con su propio entregable |
| el tipo de organizacion, **el diagrama de flujo**, la validacion repitiendo en varias cuentas y **el uso como prueba al contratar** | `refinar_sales_roadmap` | **procedimiento**: construir, documentar, validar y usar |

> **Procedimiento en los dos lados: por 9.6.3 el par es SANO. CONTINUA.** Uno acaba
> **en la puerta del cliente** y el otro **en la contratacion del director de ventas.**

**LA DIFERENCIA CONTRA EL PUESTO 200, que hay que declarar porque parece contradecirla y
no la contradice.** El 200 dio **A** entre `refinar_sales_roadmap` y
`hoja_de_ruta_de_ventas` citando como comun *"construir el mapa de acceso y DOCUMENTAR EL
PROCESO PARA REPETIRLO"*, y el 192 dio **A** contra `sales_roadmap` por lo mismo:
*"escribir el proceso paso a paso para poder repetirlo"*. **Los dos comparten con
`refinar_sales_roadmap` el paso de DOCUMENTAR. `estrategia_de_ventas` NO TIENE ningun
paso de documentar**, medido sobre sus cuatro pasos. **Le falta justo la mitad del acto
que hacia repetir a los otros dos.**

---

## `LD-70` . `estrategia_de_ventas` contra `sales_roadmap_vs_sales_force` . **D**

> **El contenido del mapa contra la condicion de contratacion, que es la misma relacion
> que el archivo ya resolvio DOS VECES y las dos en D.**
>
> `sales_roadmap_vs_sales_force` dice en su paso 1, **en UNA LINEA**, escribir paso a
> paso el camino que lleva a una venta que se repite; y **su asunto propio es una
> condicion de contratacion**: probar ese mapa con clientes reales antes de crecer el
> equipo, no contratar vendedores en cantidad hasta validar el modelo, y armar el equipo
> recien cuando el mapa este validado.
>
> `estrategia_de_ventas` no dice ni una palabra de contratar ni de escalar. **Trae el
> contenido de esa linea**: el nivel de entrada, cuantos firman, el orden, el guion y los
> saboteadores.

**Por la vara: procedimiento de un lado (la secuencia de acceso) y procedimiento del
otro (la condicion de escalado, con su umbral y su orden). CONTINUA.**

> **ES EL TERCER EJEMPLAR DE LA MISMA RELACION, y los tres calzan:** el puesto **1306**
> (`sales_roadmap` contra este, D) y el **1330** (`hoja_de_ruta_de_ventas` contra este,
> D) la escribieron con estas palabras: *"el contenido del mapa contra la condicion de
> contratacion"*. **Los tres nodos de contenido del mapa que se han leido contra el salen
> D. El unico A que este nodo tiene con un nodo de mapa es el 918, con
> `refinar_sales_roadmap`**, y ese es el que se mira abajo.

---

# LA PREGUNTA DE P.5, CONTESTADA POR ESCRITO

**La pregunta que estas cinco lecturas tenian que dejar contestada, en las palabras del
encargo: el acto `customer_validation_sales_roadmap` es UNA familia o DOS, y
`estrategia_de_ventas` pertenece o es forastero.**

## 1. POR LA LETRA DEL CRITERIO, EL ACTO ES UNO. Y ya lo era antes de estas lecturas

**El acto es una COMPONENTE CONEXA de la relacion gemelo (banco 9.24).** Medido con el
instrumento de esta vuelta, **con las seis A del archivo solas, los seis nodos ya
formaban UNA sola componente.** Las cinco lecturas de hoy **anaden una A y no cambian
eso**: sigue siendo **una componente de seis**.

> **Asi que la respuesta corta a "una familia o dos" por el criterio escrito es: UNA. Y
> las cinco lecturas no la movieron.** Lo que las cinco lecturas cambian **no es el
> conteo: es la FORMA**, y la forma es lo que P.5 existe para mirar.

## 2. POR LA FORMA, SON DOS FAMILIAS PEGADAS, y la union es UNA SOLA ARISTA

**El grafo de A del acto, con los quince pares leidos, medido y no supuesto:**

| nodo | A | contra quien |
|---|---:|---|
| `sales_roadmap` | **3** | `refinar_sales_roadmap`, `hoja_de_ruta_de_ventas`, `estrategia_de_ventas` |
| `hoja_de_ruta_de_ventas` | **3** | `refinar_sales_roadmap`, `sales_roadmap`, `estrategia_de_ventas` |
| `refinar_sales_roadmap` | **3** | `sales_roadmap`, `hoja_de_ruta_de_ventas`, `sales_roadmap_vs_sales_force` |
| `estrategia_de_ventas` | **2** | `sales_roadmap`, `hoja_de_ruta_de_ventas` |
| `sales_roadmap_vs_sales_force` | **2** | `customer_validation_sales_roadmap`, `refinar_sales_roadmap` |
| `customer_validation_sales_roadmap` | **1** | `sales_roadmap_vs_sales_force` |

**LA PRUEBA DE CORTE, corrida sobre los seis: se quita un nodo y se cuentan las
componentes de lo que queda.**

| se quita | componentes que quedan |
|---|---|
| `customer_validation_sales_roadmap` | **1** de 5 |
| `estrategia_de_ventas` | **1** de 5 |
| `sales_roadmap` | **1** de 5 |
| `hoja_de_ruta_de_ventas` | **1** de 5 |
| **`refinar_sales_roadmap`** | **2**, de 3 y de 2 |
| **`sales_roadmap_vs_sales_force`** | **2**, de 4 y de 1: **`customer_validation_sales_roadmap` queda SUELTO** |

**Y LA MISMA PRUEBA CORRIDA POR ARISTA, quitando una A cada vez, que es la que nombra la
costura:**

| se quita la A | componentes que quedan |
|---|---|
| **918**, `refinar_sales_roadmap` contra `sales_roadmap_vs_sales_force` | **2**, de **4** y de **2** |
| **319**, `customer_validation_sales_roadmap` contra `sales_roadmap_vs_sales_force` | **2**, de **5** y de **1** |
| las otras cinco A, una por una (966, `LD-68`, 200, 255, 192) | **1** de 6, ninguna corta |

> **DOS NODOS DE CORTE, Y LA COSTURA ES LA CADENA DE DOS ARISTAS 918 y 319: son las UNICAS
> dos A del acto cuya perdida lo parte**, y **las dos pasan por el mismo nodo**,
> `sales_roadmap_vs_sales_force`. **Quita la 918 y el acto se parte en cuatro mas dos.**
> Las otras cinco A viven dentro del nucleo y ninguna sostiene la union.

**LAS DOS PIEZAS, con lo que cada una es:**

| | los nodos | los pares | que es |
|---|---|---|---|
| **EL NUCLEO** | `sales_roadmap`, `hoja_de_ruta_de_ventas`, `refinar_sales_roadmap`, `estrategia_de_ventas` | **6 posibles, 5 en A**, y la unica D es `LD-69` | **el mapa de acceso al cliente**: quien decide, cuantos firman, en que orden, y como se documenta |
| **LA COLA** | `customer_validation_sales_roadmap`, `sales_roadmap_vs_sales_force` | **1 posible, 1 en A** (puesto 319) | **la condicion de escalado**: no armes el equipo de ventas hasta que el mapa este validado con ordenes reales |

**Y LA INTRANSITIVIDAD QUE LO DELATA, que es la senal que P.5 busca:**

> **`customer_validation_sales_roadmap` es A con `sales_roadmap_vs_sales_force` (319), que
> es A con `refinar_sales_roadmap` (918), y sin embargo
> `customer_validation_sales_roadmap` es D con `refinar_sales_roadmap` (1023).** Y
> tambien D con los otros tres del nucleo. **Cuatro D contra el nucleo y una sola A hacia
> fuera de el: eso no es un miembro del nucleo, es un vecino cosido por un nodo.**

## 3. `estrategia_de_ventas` PERTENECE. No es forastero, y la medida lo dice de dos formas

**La figura del forastero esta escrita con dos ejemplares** (`tacticas_cierre_ventas` e
`incentivos_no_monetarios_advocacy`, verificados en la vuelta 17), **y su perfil es:
esta en la nomina POR EL NOMBRE, sus lecturas contra el grupo son D, y su cableado apunta
fuera.** `estrategia_de_ventas` **no cumple ninguna de las tres**:

| la senal del forastero | `estrategia_de_ventas` |
|---|---|
| lecturas contra el grupo **todas D** | **NO: tiene DOS A**, el 966 con `sales_roadmap` y `LD-68` con `hoja_de_ruta_de_ventas` |
| cableado apuntando **fuera** del grupo | **NO: `refinar_sales_roadmap`, miembro del acto, esta entre sus `nodos_previos`** |
| en la nomina **por el nombre** | **NO: su nombre ni siquiera dice roadmap.** Entro por una A leida, la del 966 |

> **`estrategia_de_ventas` es miembro pleno del nucleo**, y ademas es **el unico de los
> cuatro que trae el guion por persona y los saboteadores**. **La pregunta del encargo
> tenia la sospecha apuntando al nodo equivocado.**

## 4. EL QUE SI CUMPLE EL PERFIL DEL FORASTERO ES EL NODO QUE LE DA NOMBRE AL ACTO

**Y esto no se pidio, sale de la medicion, y por eso se declara y no se ejecuta.**

| la senal del forastero | `customer_validation_sales_roadmap` |
|---|---|
| lecturas contra el grupo **todas D** | **CUATRO DE CINCO**: 872, 1023, `LD-66` y `LD-67`. Su unica A es el 319, con el otro nodo de la cola |
| cableado apuntando **fuera** | **SI, entero**: sus previos son `producto_minimo_viable` y `customer_discovery_cuatro_fases`; sus siguientes son `sintesis_hipotesis_modelo_negocio`, `vision_estrategia_producto_pivote`, `tipos_de_pivote` y `catalogo_pivotes`. **NINGUNO de los seis es miembro del acto** |
| en la nomina por el nombre | **el acto se llama COMO EL**, porque el nombre del acto es el de un miembro y no una decision de contenido |

> **LA FRASE QUE RESUME LO QUE ESTAS CINCO LECTURAS ENSENAN: el acto del sales roadmap
> se llama por el unico de sus seis nodos que casi no pertenece a el.**

---

# LO QUE ESTO LE DEJA AL PLAN: TRES PROPUESTAS, DECLARADAS Y NO EJECUTADAS

**MODO DE CIERRE: aqui no se ejecuta ninguna. Van al reporte de la vuelta 18 con su
evidencia, para que el auditor las adjudique.** Medido con el instrumento de esta vuelta:
**de las 71 operaciones LISTAS, NINGUNA funde este acto**; la unica que nombra a alguno
de los seis nodos es `OP-M-02-PROG`, y lo nombra **como arista entrante que su simulacion
redirige**, no como miembro de su fusion. **Ninguna operacion LISTA queda contradicha por
estas lecturas.**

| # | la propuesta | su evidencia |
|---:|---|---|
| **1** | **la cobertura del acto pasa de 10 de 15 a 15 de 15, y su deuda de P.5 baja a CERO.** La entrada de tipo `acto` vigente (corte 2026-08-13) dice *"10 de 15 pares leidos; 0 en cola; 5 fuera de cola"* y su nota dice *"Puede crecer: 0 en cola y 5 fuera de cola"* | los cinco `LD-66` a `LD-70` de este documento |
| **2** | **el acto es candidato a PARTIRSE en dos**, un nucleo de cuatro y una cola de dos, cosidos por la sola arista del puesto **918** | la prueba de corte de la seccion 2, corrida con instrumento |
| **3** | **`customer_validation_sales_roadmap` es candidato a TERCER EJEMPLAR de la figura del forastero**, con cuatro D contra el nucleo, una sola A hacia fuera y **cero aristas** hacia ningun miembro del acto | la seccion 4 |

> **LAS TRES SON PARA EL RECOMPUTO Y PARA `OP-U-02`, no para hoy.** Y **la 2 y la 3 no
> son independientes**: si el acto se parte, el forastero deja de serlo, porque pasa a ser
> **la mitad de su propia familia de dos**. **Se dicen las dos y se deja que las adjudique
> quien pueda.**

**LO QUE ESTAS CINCO LECTURAS NO CAMBIAN, y se dice para que nadie lo lea de mas:** la
clase del racimo. La entrada de tipo `racimo` "el sales roadmap" dice **MEZCLADO** desde
el puesto 872, **y sigue MEZCLADO**: cuatro D nuevas y una A nueva no vuelven puro a un
racimo mezclado. **El motivo escrito para no leerlos** (*"leerlos cierra cobertura, no
cambia forma"*) **era cierto para la clase del racimo y era falso para la forma del
acto**, que es lo que la vuelta 17 dejo dicho y estas lecturas confirman.
