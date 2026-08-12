# EXPEDIENTE DE MESA: `OP-M-02`, LA SERIE DE COLEMAN

**LA SEGUNDA MESA, Y TAMBIEN ADJUDICADA.** Se preparo el 11 ago 2026 con el mismo
estandar que el de la junta asesora, sin recomendacion nueva donde no la habia, y
**el auditor la adjudico el 12 ago 2026**. **La adjudicacion esta al final**, y
`OP-M-02` es **LISTA**.

> **Lo que sigue hasta la seccion 6 es el expediente TAL COMO SE ENTREGO**, para que
> la decision se pueda auditar contra lo que habia sobre la mesa.

> **MODO DE CIERRE VIGENTE: este expediente no toca ni un nodo. Es papel.**

**FECHA DE CORTE: 11 ago 2026, archivo al puesto 2.117 de 3.388.**

---

## CORRECCION DECLARADA DE ENTRADA: **LA SERIE SON 28, NO 27**

**La nomina que se publico ayer decia 27.** Al preparar este expediente aparecio que
faltaba **`seis_medios_comunicacion_cliente`**, que no es un miembro cualquiera: **es
LA CABEZA de la serie de medios**, la doctrina general de los seis medios.

**Por que se escapo, y la causa es del instrumento y no del archivo:** la lista de
palabras del contador tenia *correo*, *video*, *regalo* y *herramienta*, **pero no
tenia *medio* ni *canal***. `seis_canales_comunicacion_assess` habia entrado por otra
puerta, por la palabra *assess*.

> **Lo levanto el ARCHIVO, no el contador: el veredicto 948 lo nombra.** Es
> exactamente para lo que el banco 9.20 manda usar los dos instrumentos, **y aqui el
> segundo salvo al primero.**

| | antes | **hoy** |
|---|---:|---:|
| miembros de la serie | 27 | **28** |
| de programa | 19 | 19 |
| **de medios** | 8 | **9** |
| pares posibles | 351 | **378** |
| **leidos** | 38 | **41** *(28 D, 10 A, 3 B)* |
| en cola | 0 | 0 |
| **fuera de cola** | 313 | **337** |
| forma | MEZCLADO | **MEZCLADO, cobertura 41 de 378** |

---

## LO QUE ESTA MESA DECIDE

**La pregunta de la apertura sigue siendo la misma**: si las ocho fases reciben el
tratamiento de **SERIE DECLARADA**, un nodo programa unico y un nodo por paso
colgando de el. **Lo que este expediente anade es que la decision tiene CUATRO
piezas y no una**, y tres de ellas ya estan medidas:

| | decision | estado de la evidencia |
|---:|---|---|
| **1** | **el programa unico**: cual de las dos cabezas sobrevive | **medido**, puesto 326 mas cableado |
| **2** | **las fases dobles**: que hacer con las cinco fases que tienen gemelos dentro | **medido**, cinco A |
| **3** | **la serie de medios**: su cabeza esta duplicada y sus instancias tambien | **medido**, puestos 948, 1012 y 1068 |
| **4** | **el orden entre 2 y 3** | **ya adjudicado**: medios antes que fases, y con evidencia |

---

## 1. EL BLOQUE DE APERTURA, tal como esta hoy

### **LO PRIMERO: LA FASE 3 YA ESTA FUNDIDA, Y AGUANTA**

> **Esta mesa no debate una propuesta. Debate REPETIR ALGO QUE EL GRAFO YA HIZO Y
> SOSTUVO.**

`fase_affirm_buyers_remorse` **es hoy la fase 3 entera** y carga **TRES ids dentro**
como alias: `fase_affirm`, `fase_affirm_reduccion_incertidumbre` y
`fase_affirm_reducir_remordimiento`, **los tres deprecados**. La fusion se hizo con
el patron completo: superviviente, alias y baja.

**VERIFICADO** con `scripts/plan/aristas_por_alias_affirm.py`:

| | |
|---|---:|
| ids fundidos en uno | **4** |
| aristas vivas que apuntan a un alias | **10** |
| de ellas, **con su gemela literal al destino en el MISMO campo** | **10 de 10** |
| nodos que apuntan al destino **por su nombre propio** | **16** |

**LAS DIEZ ARISTAS, nombradas:**

| el que apunta | campo | al alias |
|---|---|---|
| `fase_admit` | `nodos_siguientes` | `fase_affirm` |
| `fase_admit_celebracion` | `nodos_siguientes` | `fase_affirm` |
| `ocho_fases_experiencia_cliente` | `nodos_siguientes` | `fase_affirm` |
| `fase_activate` | `nodos_previos` | `fase_affirm` |
| `calibracion_intensidad_celebracion` | `nodos_siguientes` | `fase_affirm_reduccion_incertidumbre` |
| `fase_acclimate_experiencia_cliente` | `nodos_previos` | `fase_affirm_reduccion_incertidumbre` |
| `sistema_manejo_quejas` *(de `quality`, no de `core`)* | `nodos_siguientes` | `fase_affirm_reduccion_incertidumbre` |
| `cierre_segun_complejidad_venta` | `nodos_siguientes` | `fase_affirm_reducir_remordimiento` |
| `fase_activate_primera_impresion` | `nodos_previos` | `fase_affirm_reducir_remordimiento` |
| `welcome_call_cliente_veterano` | `nodos_previos` | `fase_affirm_reducir_remordimiento` |

> **LAS DIEZ AGUANTAN POR LA RAZON FUERTE: todas tienen su gemela literal al destino
> en el mismo campo.** No es que el resolutor las rescate: **la fusion las reescribio
> y ademas dejo la referencia vieja.** **Si se apagara el resolutor, la fase 3
> seguiria conectada igual.**

**Ninguna arista quedo colgando.** La unica referencia del destino a un nodo no vivo
es `gestion_de_quejas_y_fidelizacion`, **y resuelve a `sistema_manejo_quejas`**.

**LO QUE EL PRECEDENTE NO PRUEBA:** las diez referencias por alias **son redundancia,
no conectividad**. Y ahora se sabe que **no son una rareza de Affirm**: son diez de
las **1.056** que `OP-S-12` mide en todo el catalogo.

### EL RESTO DE LA APERTURA

> **QUE SE DECIDE.** Si las **ocho fases** reciben el tratamiento de **SERIE
> DECLARADA**: un nodo programa unico, un nodo por paso colgando de el, y el numero
> en el titulo legitimado porque el programa lo explica.
>
> **LA RECOMENDACION, y viene de la DECISION 1 ya aprobada el 9 ago 2026**: el
> tratamiento de serie declarada **ya esta adoptado** para los programas desmontados
> en piezas. Esta mesa decide **si Coleman lo recibe**, no si el tratamiento existe.
>
> | opcion | consecuencia |
> |---|---|
> | **serie declarada** | **la cabeza ya existe por duplicado**: hay DOS nodos programa, asi que la decision **trae dentro una fusion** |
> | no es serie | hay que explicar **que hacen diecinueve nodos de fase y nueve de medios sin cabeza declarada** |
>
> **LO QUE ESTA MESA SABE HOY Y NO SABIA**: Coleman es **el segundo libro que mas
> injertos aporta, QUINCE**, y su material esta pegado **en nodos de otros libros**.
> **La serie no solo esta desmontada: esta ademas repartida fuera de su casa.**

---

## 2. LA SERIE DE 28, REPARTIDA POR FASE

**Los 28 son de PRIMERA CASA. Ninguno de los quince de segunda casa entra a la
serie**, y eso es un dato de la mesa: **el material injertado de Coleman esta en
nodos de otros libros, no en la serie.**

### EL PROGRAMA, 19 nodos vivos y 20 ids

| fase | vivos | los nodos | gemelos dentro |
|---|---:|---|---|
| **1 Assess** | **3** | `fase_assess`, `fase_assess_ciclo_cliente`, `fase_assess_experiencia_cliente` | **A en 373**, B en 224 |
| **2 Admit** | 2 | `fase_admit`, `fase_admit_celebracion` | **A en 421** |
| **3 Affirm** | **1** | `fase_affirm_buyers_remorse` | **ya fundida**: 4 ids en 1 |
| **4 Activate** | 2 | `fase_activate`, `fase_activate_primera_impresion` | **A en 183** |
| **5 Acclimate** | **3** | `fase_acclimate`, `fase_acclimate_experiencia_cliente`, `fase_acclimate_mapa_de_proceso` | **A en 447**, B en 196 y 253 |
| **6 Accomplish** | 2 | `fase_accomplish`, `fase_accomplish_experiencia_cliente` | **A en 595** |
| **7 Adopt** | 2 | `fase_adopt`, `fase_adopt_ciclo_cliente` | D en 965 |
| **8 Advocate** | 2 | `advocacy_customer_journey`, `incentivos_no_monetarios_advocacy` | sin par leido |
| **LA CABEZA** | **2** | `fases_de_retencion_de_clientes`, `ocho_fases_experiencia_cliente` | **A en 326** |

> **CINCO DE LAS OCHO FASES TIENEN GEMELOS CONFIRMADOS DENTRO, y la sexta, Affirm,
> YA SE FUNDIO.** Quedan **Adopt**, cuyo unico par leido es D, y **Advocate**, que no
> tiene ningun par leido.

### LOS MEDIOS, 9 nodos

| papel | nodos |
|---|---|
| **la cabeza, y esta duplicada** | `seis_medios_comunicacion_cliente`, `estrategia_multicanal_bienvenida` . **A en 948** |
| **instancias por fase** | `seis_canales_comunicacion_assess`, `seis_herramientas_comunicacion_fase_activate`, `seis_herramientas_comunicacion_celebracion` |
| **la familia de los regalos** | `regalos_estrategicos_personalizados`, `regalos_estrategicos_sorpresa`, `sorprender_cliente_estrategico` . **A en 251 y 799** |
| **el medio suelto** | `welcome_call_cliente_veterano` |

### LOS 15 DE SEGUNDA CASA, y su primera casa

`blueprint_de_experiencia`, `cultura_de_experiencia`, `customer_journey_mapping` y
`metas_vs_proposito` **(Change by Design y Assembling Tomorrow)**;
`estrategia_crecimiento_clientes`, `ganar_comprension_del_cliente`,
`keep_customers_strategy`, `retention_metrics` y `viral_loop_marketing` **(The
Startup Owner's Manual)**; `cliente_disena_producto` y `voz_del_cliente_voc`
**(Winning at New Products)**; `diseno_estructura_recompensas_roles` **(The Founder's
Dilemmas)**; `relaciones_con_clientes` **(Business Model Generation)**;
`sistema_inmune_producto` **(The Lean Startup)**; `project_close_out` **(A Project
Manager's Book of Forms)**.

> **Y `project_close_out` es el ejemplar de por que el criterio tuvo que
> estrecharse**: entraba a la serie por la palabra suelta *fase*, **y es de gestion
> de proyectos.**

---

## 3. LOS VEREDICTOS EN CRUDO: **LAS FASES DOBLES CONFIRMADAS**

### PUESTO 373 . `fase_assess_ciclo_cliente` contra `fase_assess_experiencia_cliente` . **A**

> REPITE. Los dos trabajan la misma fase Assess y mandan lo mismo: medir cuanto dura
> el momento en que el prospecto te evalua, revisar si lo que dices para vender
> comunica como se va a sentir en vez de beneficios genericos, y disenar al menos una
> mejora concreta de esa etapa. El segundo anade **crear algo tangible, muestra,
> historia o testimonio, que de un anticipo**; el primero anade calificar del 1 al 10
> y los seis canales de comunicacion. Esta familia es la del **racimo costurado
> transversal numero 1**.

### PUESTO 421 . `fase_admit` contra `fase_admit_celebracion` . **A**

> REPITE. Los dos trabajan la misma fase Admit y mandan lo mismo: disenar un momento
> de celebracion o reconocimiento inmediato al cerrar la compra, dejar un artefacto o
> mensaje personalizado que lo memorialice, y **no caer en el silencio post venta**.
> El segundo anade **la co creacion cuando se pueda** y el cuidado de que la
> celebracion no venga solo del vendedor.

### PUESTO 183 . `fase_activate` contra `fase_activate_primera_impresion` . **A**

> REPITE. Los dos disenan el mismo kickoff de la fase Activate como experiencia
> memorable, cuidando la primera impresion y la reaccion del cliente en ese momento.
> **FIGURA: ids casi identicos, uno es el base y el otro le anade sufijo tematico.**
> Candidato a fusion.

### PUESTO 447 . `fase_acclimate_experiencia_cliente` contra `fase_acclimate_mapa_de_proceso` . **A**

> REPITE. Los dos trabajan la misma fase Acclimate y mandan lo mismo: mapear todo el
> recorrido desde la compra hasta que el cliente logra su objetivo, y **desde la
> perspectiva del cliente**.

### PUESTO 595 . `fase_accomplish` contra `fase_accomplish_experiencia_cliente` . **A**

> GEMELOS DE LA MISMA FASE, **y esto afina la doctrina de LA SERIE DE COLEMAN**. En
> el puesto 580 dos nodos aplicaban el mismo instrumento a DOS FASES distintas y eso
> los salvaba. Aqui los dos son de la MISMA fase, Accomplish, **y no hay nada que los
> salve**. Mandan lo mismo en el mismo orden: definir cual es el resultado que el
> cliente busca de verdad y no la entrega del producto, montar como saber cuando lo
> alcanzo, y celebrarlo con el cliente. Lo propio de cada uno es una linea: el
> primero manda recoger evidencia para usos futuros; el segundo clasifica cada
> relacion en tres escenarios y **reserva al menos el cinco por ciento de las
> ganancias del proyecto para mejorar la experiencia. Ese cinco por ciento es lo mas
> concreto del par y es lo que se perderia.** Sin arista entre ellos.
>
> **REGLA QUE ESTE PAR FIJA: en una serie por fases, dos nodos de fases distintas son
> sanos y dos nodos de la MISMA fase son gemelos.**

### LOS TRES DUDOSOS, que son de la misma familia y hay que decidirlos juntos

**PUESTO 224 . `fase_assess` contra `fase_assess_ciclo_cliente` . B**

> DUDOSO. La misma fase Assess **pero con actos distintos**: uno da **la doctrina de
> la etapa** y el otro **una auditoria de lo que ya haces**, con medicion de tiempos
> y calificacion del 1 al 10. FIGURA: ids casi identicos con sufijo tematico.

**PUESTO 196 . `fase_acclimate` contra `fase_acclimate_mapa_de_proceso` . B**

> DUDOSO. La misma fase Acclimate y comparten la instruccion de simplificar la
> friccion, **pero los artefactos difieren**: uno hace materiales de onboarding y el
> otro un mapa visual del proceso.

**PUESTO 253 . `fase_acclimate` contra `fase_acclimate_experiencia_cliente` . B**

> DUDOSO. La misma fase y comparten la instruccion de identificar los puntos de
> friccion, **pero los artefactos difieren**: uno hace materiales de onboarding y el
> otro mapea los puntos de contacto y mide con encuestas. **FIGURA: RACIMO NUEVO**,
> con el 196 la familia de la fase Acclimate llega a TRES nodos.

> **LOS TRES B TIENEN LA MISMA FORMA, y por eso se deciden en un solo acto: EL NODO
> BASE DE LA FASE CONTRA SUS INSTANCIAS.** `fase_assess` contra su auditoria,
> `fase_acclimate` contra su mapa y contra su experiencia. **La pregunta es una sola:
> el nodo base de una fase es la madre de sus instancias, o es un gemelo mas.**

---

## 4. EL PROGRAMA UNICO DEL 326, con su superviviente **por cableado**

### PUESTO 326 . `fases_de_retencion_de_clientes` contra `ocho_fases_experiencia_cliente` . **A**

> REPITE. Los dos mandan lo mismo sobre **el mismo mapa de ocho fases**: ubicar en
> que fase esta hoy cada segmento, disenar la experiencia de **cada una de las ocho** y
> no solo de las de captacion, y armar el plan que empuja al cliente de una fase a la
> siguiente. El primero senala **Affirm y Activate como las mas descuidadas** y el
> segundo manda **detectar donde se atascan**, que es la misma deteccion por dos
> caminos.

**EL DESEMPATE, medido el 11 ago 2026** con
`scripts/plan/mesa_coleman_verificacion.py`:

| | `fases_de_retencion_de_clientes` | `ocho_fases_experiencia_cliente` |
|---|---:|---:|
| pasos | 3 | **4** |
| destinos resueltos que nombra | 3 | **13** |
| **nodos que lo nombran** | **3** | **13** |
| alias que ya carga | ninguno | ninguno |

> **EL CABLEADO NO EMPATA: ES CUATRO A UNO.** `ocho_fases_experiencia_cliente` es el
> nodo del que cuelga la serie, **y ademas es el unico que nombra a la cabeza de los
> medios** (`estrategia_multicanal_bienvenida`) y **el que apunta a la fase 3 por
> alias**.

> **ES EL MISMO DESEMPATE POR CABLEADO QUE `OP-M-04` acaba de usar en la fusion 328**,
> y aqui llega **con mucho mas margen**: alli el contenido empataba y decidia una
> sola arista; **aqui decide una diferencia de trece contra tres.**

**LA PERDIDA QUE VIAJARIA**, nombrada porque toda fusion la lleva: de
`fases_de_retencion_de_clientes`, **el senalamiento de Affirm y Activate como las dos
fases mas descuidadas**. Es la unica linea suya que el otro no tiene.

---

## 5. LA REGLA DE ORDEN: **LOS MEDIOS ANTES QUE LAS FASES**

**NO ES NUEVA, y por eso se cita en vez de proponerse.** Es **el paso 2 de la forma
del tratamiento de Coleman**, y el archivo la nombra explicitamente en el veredicto
948: *el paso 2 de la forma del tratamiento manda resolver la serie de los seis
medios ANTES que las fases*.

### LA EVIDENCIA DEL ARCHIVO, y son tres lecturas que se encadenan

**PUESTO 948 . `estrategia_multicanal_bienvenida` contra `seis_medios_comunicacion_cliente` . A**

> LOS SEIS MEDIOS DE COLEMAN, **CONTADOS DOS VECES**. Lo comun es el instrumento
> entero: auditar que medios se usan hoy, incorporar los subutilizados (correo
> fisico, video personalizado, regalos con sentido) y evitar los gestos genericos.
> Lo propio del primero: personalizar cada punto de contacto y **MEDIR** las tasas
> antes y despues. Lo propio del segundo: **elegir el medio segun la FASE en que esta
> el cliente**. **Sale A: la serie de los medios tambien esta duplicada, no solo
> instanciada dentro de las fases.**

**PUESTO 1012 . `seis_canales_comunicacion_assess` contra `seis_medios_comunicacion_cliente` . D**

> La serie general contra **su instancia en la fase Assess**. La general dice en UNA
> LINEA *seleccionar deliberadamente que medio usar segun la fase*; la instancia trae
> **el procedimiento de esa linea** para una fase concreta. **Por la vara del banco
> 9.6.1, CONTINUA.** **Su relacion con la doctrina general es de HIJO y no de copia.
> La serie de los medios se duplica entre si, pero sus instancias por fase son
> sanas.**

**PUESTO 1068 . `seis_herramientas_comunicacion_celebracion` contra `seis_herramientas_comunicacion_fase_activate` . A**

> LOS SEIS MEDIOS INSTANCIADOS EN DOS FASES, **y las dos instancias se repiten entre
> si**. Lo comun es el procedimiento entero. Lo propio de la primera es atarlo al
> logro; lo propio de la segunda son dos gestos de diagnostico. **LO QUE ESTO CIERRA:
> las INSTANCIAS TAMBIEN SE REPITEN ENTRE ELLAS. La serie de los medios no solo esta
> duplicada arriba: esta duplicada tantas veces como fases la instancien.**

### LA EVIDENCIA DEL CABLEADO, medida hoy y nueva

**Un medio no pertenece a una fase: cuelga de varias.**

| el medio | cuantos lo nombran | desde que nodos de la serie |
|---|---:|---|
| **`welcome_call_cliente_veterano`** | **9** | **SIETE nodos de programa, de SEIS fases distintas**: Assess, Admit, Affirm, Activate, Acclimate, Accomplish y Advocate |
| `seis_canales_comunicacion_assess` | 2 | `fase_assess_ciclo_cliente` **y `fase_admit`** |
| `seis_herramientas_comunicacion_celebracion` | 2 | `fase_accomplish` **y `fase_adopt`** |
| `estrategia_multicanal_bienvenida` | 3 | `ocho_fases_experiencia_cliente`, o sea **la cabeza** |
| `seis_herramientas_comunicacion_fase_activate` | 2 | **`fase_acclimate_mapa_de_proceso`**, y no una fase Activate |

> **POR QUE EL ORDEN IMPORTA, dicho con el ejemplar exacto:**
> `seis_herramientas_comunicacion_celebracion` y
> `seis_herramientas_comunicacion_fase_activate` **estan en A** (1068). El primero
> cuelga de Accomplish y de Adopt; el segundo, de Acclimate. **Si se funden las fases
> primero, la fase que pierda su nodo hereda una cuerda que no era suya, o pierde la
> que si lo era.** **Resolver el medio primero deja una sola cuerda y todas las fases
> apuntan a ella.**

> **LO QUE PARECIA UN DESAJUSTE Y SE MIDIO EL 12 ago 2026: NO LO ES.**
> `seis_herramientas_comunicacion_fase_activate` lleva *fase_activate* en el nombre y
> quien lo nombra es `fase_acclimate_mapa_de_proceso`. **Se midio contenido y cableado,
> que es lo que manda, y los tres coinciden.**

| | |
|---|---|
| **el nombre** | dice **Activate** |
| **el contenido** | dice **Activate sin ninguna duda**: *identifica cual es el primer contacto real que tienes con tu cliente DESPUES DE QUE COMPRA*, y su etiqueta del arbol es *Recibe Bien al Nuevo Cliente* |
| **el cableado** | dice **Activate**: sus previos son el kit de bienvenida, y su siguiente es **Acclimate**, que es exactamente el orden de la serie |

> **LA CONFUSION FUE MIA Y SE DEJA ESCRITA PORQUE ES REPETIBLE: en un grafo de
> secuencia, quien te nombra en `nodos_previos` es tu SIGUIENTE, no tu dueno.** Que
> Acclimate lo liste entre sus previos **no dice que el nodo sea de Acclimate: dice
> que va antes.**

---

## 6. LO QUE EL EXPEDIENTE NO TRAE

| no esta | por que |
|---|---|
| **recomendacion sobre las cinco fases dobles** | **no existe ninguna escrita.** Los cinco pares estan en A y **ninguno tiene adjudicacion**. Es lo primero que la mesa tiene que decidir |
| **recomendacion sobre los tres B** | tampoco existe. **Se nombran juntos porque tienen la misma forma**, no porque haya una lectura que los resuelva |
| **el destino de los quince de segunda casa** | es de la fase 01, no de esta mesa. **Aqui solo se registra que ninguno entra a la serie** |
| **la cobertura completa** | **41 de 378, y 337 pares FUERA DE COLA.** Por el banco 9.26 **toda forma de esta mesa es PROVISIONAL**, y hay que decirlo al adjudicar |

> **LA ADVERTENCIA QUE GOBIERNA ESTE EXPEDIENTE: la mesa de Coleman se sienta con
> UNA DECIMA PARTE de su nomina leida.** La de la junta asesora se sento con 6 de 6.
> **No son mesas comparables**, y **lo que aqui se decida sobre las fases con gemelos
> confirmados es firme; lo que se decida sobre las fases sin par leido no lo es.**

**LAS DOS FASES SIN EVIDENCIA, nombradas:** **Adopt**, cuyo unico par leido es **D**
(puesto 965), y **Advocate**, que **no tiene ningun par leido entre sus dos nodos**.

---

# LA ADJUDICACION DEL AUDITOR . **12 ago 2026**

> **COLEMAN RECIBE EL TRATAMIENTO DE SERIE DECLARADA. `OP-M-02` PASA A LISTA**, y se
> reparte en **siete operaciones hijas**, cada una con su simulacion por el estandar
> **P.7**.

## a. EL PROGRAMA UNICO . `OP-M-02-PROG` . **LISTA**

**Sobrevive `ocho_fases_experiencia_cliente` por cableado SIN EMPATE: 13 contra 3**,
y 4 pasos contra 3.

**LAS DOS PRIORIDADES VIAJAN**, y son lo unico propio del que muere:

| | |
|---|---|
| **1** | **priorizar Affirm y Activate** como las dos fases mas descuidadas de la serie |
| **2** | **detectar donde se atascan** los clientes, con su plan de avance de una fase a la siguiente |

> **El superviviente es ademas el nodo del que cuelga la serie**: el unico que nombra
> a la cabeza de los medios y el que apunta a la fase 3 por alias. **No es solo el mas
> cableado: es el que sostiene el mapa.**

**LA SIMULACION LEVANTO UNA AUTO ARISTA** que la fusion crearia, y **esta operacion
no la arregla**: es de `OP-S-07`, que ya la tiene contada.

## b. LA CABEZA DE MEDIOS . `OP-M-02-MEDIOS` . **SE TRAE AL AUDITOR**

**El auditor mando desempatar por cableado y traerle el caso si el contenido y el
grafo empatan. MEDIDO: no empatan. SE CONTRADICEN**, que es un caso mas fuerte que el
previsto, y por eso se trae.

| dice | quien gana | con que |
|---|---|---|
| **el cableado** | `estrategia_multicanal_bienvenida` | **3 contra 2**, y 5 pasos contra 4. **Margen de UNA arista** |
| **el archivo** | `seis_medios_comunicacion_cliente` | el veredicto **1012** lo llama **LA DOCTRINA GENERAL** y declara que `seis_canales_comunicacion_assess` es **su HIJO**. **Es el padre declarado de las instancias** |

**Y HAY UNA TERCERA COSA, de nombre**: el id que gana por cableado dice
**BIENVENIDA**, que es **una** fase, mientras la doctrina vale para **las ocho**. **Si
sobrevive, la cabeza general de los medios se llama como una sola fase.**

**LAS TRES OPCIONES, con su consecuencia:**

| | opcion | consecuencia |
|---:|---|---|
| **1** | manda el cableado | sobrevive `estrategia_multicanal_bienvenida`, **y hay que renombrar en la misma operacion** para que la cabeza no se llame como una fase |
| **2** | manda el rol declarado por el archivo | sobrevive `seis_medios_comunicacion_cliente`, y se acepta que **el desempate por cableado no es universal: es subsidiario del rol** cuando el archivo ya declaro uno |
| **3** | no son cabeza y sub cabeza | son **dos cabezas de temas distintos** y **no se funden** |

> **POR QUE ESTO NO LO RESUELVE LA REGLA DEL CABLEADO SOLA: la regla nacio en
> `OP-M-04` para desempatar CONTENIDO EMPATADO.** Aqui el contenido **no empata**,
> porque **el archivo ya asigno un ROL a uno de los dos**. **Un margen de una arista
> no deberia poder revocar un rol declarado por lectura**, y esa es la pregunta.

> **Es la primera vez que el desempate por cableado choca con el archivo, asi que lo
> que se decida aqui FIJA DOCTRINA para las mesas que vienen.**

## c. EL ORDEN: **LOS MEDIOS ANTES QUE LAS FASES**

**Citado del veredicto 948**: *el paso 2 de la forma del tratamiento manda resolver
la serie de los seis medios ANTES que las fases*. **Y con la evidencia de las cuerdas
cruzadas ya escrita en la seccion 5 de este expediente**: un medio no pertenece a una
fase, **cuelga de varias**, y `welcome_call_cliente_veterano` cuelga de **siete nodos
de programa de seis fases distintas**.

**En la practica**: las cinco operaciones de fase **dependen de `OP-M-02-MEDIOS`**, y
ninguna se ejecuta antes.

## d. LAS CINCO FASES CON GEMELOS CONFIRMADOS

**Tratamiento de Affirm fase por fase: un nodo por fase, y los alias cargan los ids
que mueren. UNA OPERACION POR FASE, cada una con su simulacion.**

| fase | operacion | sobrevive | cableado | duplicadas que fabrica |
|---|---|---|---:|---:|
| **1 Assess** | `OP-M-02-ASSESS` | `fase_assess_ciclo_cliente` | **6 a 4** | 2 |
| **2 Admit** | `OP-M-02-ADMIT` | **`fase_admit`** | **7 a 4** | 3 |
| **4 Activate** | `OP-M-02-ACTIVATE` | `fase_activate_primera_impresion` | **4 a 3** | 1 |
| **5 Acclimate** | `OP-M-02-ACCLIMATE` | `fase_acclimate_experiencia_cliente` | **10 a 3** | 0 |
| **6 Accomplish** | `OP-M-02-ACCOMPLISH` | `fase_accomplish_experiencia_cliente` | **9 a 8** | 0 |

**LO QUE HAY QUE DECIR DE CADA UNA, y no es lo mismo:**

**ASSESS Y ACCLIMATE QUEDAN CON DOS NODOS, NO CON UNO.** El nodo base de cada una,
`fase_assess` y `fase_acclimate`, **no entra en la fusion**, porque **sus pares con el
superviviente son DUDOSOS y no A**: los puestos **224**, **196** y **253**. **Fundir
sobre un B seria fundir sin veredicto.** **Un nodo por fase queda como CONDICION en
esas dos.**

**ADMIT es la unica donde gana el nodo base**, y gana con margen: 7 a 4.

**ACTIVATE es el desempate mas flojo, 4 a 3**, y **el veredicto 183 no nombra ninguna
pieza propia de ninguno de los dos**. **Por eso la lectura de acto de P.5 no es
opcional ahi**: si al leer los dos textos enteros aparece una pieza propia en el que
muere, **se registra como perdida antes de fundir**. **Y el precedente de Affirm
apunta igual: alli tambien murio el nodo base y sobrevivio la instancia tematica.**

**ACCOMPLISH es 9 a 8, y es la mejor comprobacion que ha tenido la regla del
cableado.** El veredicto 595 dice que la pieza mas concreta del par, **reservar al
menos el cinco por ciento de las ganancias del proyecto para mejorar la
experiencia**, es **lo que se perderia**. **Esa pieza esta en el nodo que sobrevive.**
**El desempate por cableado salvo justo lo que el veredicto temia perder.**

**LAS PERDIDAS QUE VIAJAN, nombradas una por una:**

| fase | del que muere, viaja |
|---|---|
| Assess | **crear algo tangible**, muestra, historia o testimonio, que de un anticipo |
| Admit | **la co creacion** de la celebracion con el cliente, y **el cuidado de que no venga solo del vendedor** |
| Activate | **ninguna nombrada por el veredicto**. La lectura de acto tiene que buscarlas |
| Acclimate | **el mapa visual del proceso**, que es el artefacto propio del que muere |
| Accomplish | **recoger evidencia, testimonios y datos** del logro, para usos futuros |

> **Y LA REGLA DE ORDEN QUE LAS CINCO LLEVAN DENTRO: CADA FASE ES SU PROPIO ACTO, y
> por P.5 sus pares se leen ENTEROS despues de los destejidos y ANTES de su fusion.**

## e. ADOPT Y ADVOCATE: **NO SE ADJUDICAN**

**Sus pares van a lecturas dirigidas**, `LD-28` a `LD-31`, **y las dos fases quedan
como CONDICION ESCRITA**. Estan en
[`LECTURAS_DIRIGIDAS.md`](LECTURAS_DIRIGIDAS.md), tercera tanda.

> **Y no es lo mismo en las dos.** En **Adopt** la mesa no puede adjudicar **porque
> el archivo ya dijo que no repiten** (puesto 965, D): adjudicar seria contradecir una
> lectura. En **Advocate** no puede adjudicar **porque no sabe**: su par interno no se
> ha leido nunca.

## f. EL DESAJUSTE `activate` CONTRA `acclimate`: **MEDIDO, Y NO EXISTE**

**Escrito como paso previo de la etapa de medios, y ejecutado el 12 ago 2026.**
**Mandan el contenido y el cableado, no el nombre**, y los tres coinciden: es de
**Activate**. **El detalle esta en la seccion 5 de este expediente.**

> **Lo que queda escrito no es el desajuste, es la leccion: en un grafo de secuencia,
> quien te nombra en `nodos_previos` es tu SIGUIENTE, no tu dueno.**

## g. LA ADVERTENCIA DE COBERTURA, **dentro de la operacion**

> **LA MESA ADJUDICA ESTRUCTURA. LA COBERTURA SE PAGA FASE POR FASE EN LAS LECTURAS
> DE ACTO.**

**41 de 378, y 337 pares fuera de cola.** Lo que esta mesa decide **es la forma del
tratamiento**, y esa decision **se sostiene con lo leido**: hay cabeza duplicada
medida, cinco fases con gemelos confirmados y una serie de medios duplicada arriba y
en sus instancias.

> **Lo que NO se sostiene con lo leido es el contenido de cada fusion**, y por eso
> **ninguna de las siete operaciones hijas se ejecuta sin su lectura de acto.** **La
> mesa dice COMO; el acto dice QUE se pierde.**
