# Informe del cribado intra-dominio

**ESTE INFORME ESTA ABIERTO.** El cribado va por **370 de 3388 pares** y el
informe de cierre se escribe al llegar al 100%, como manda el encargo largo.
Lo que vive aqui son **los hallazgos que ya no caben en la razon de un
veredicto**: figuras, familias y siluetas que valen para muchos pares a la vez.

**La cola, el metodo y la calibracion estan en `INTRA_DOMINIO_RESUMEN.md`. Los
veredictos par por par estan en `INTRA_DOMINIO_VEREDICTOS.jsonl`. Aqui no se
repite nada de eso.**

---

## 1. RACIMOS NUEVOS FUERA DE NOMINAS

**Las tres familias que el tramo 268 a 370 destapo no estan en
`docs/RACIMOS_MIEMBROS.jsonl`.** Ese censo tiene 32 nominas reconstruidas de los
veredictos de la franja; estas tres salieron del otro eje y por eso faltan.

> **LA REGLA QUE LAS CREA, y es la leccion del tramo**: **una familia juzgada de
> a pares da incoherencia, porque la pregunta no es de pares.** El mismo nodo
> sale sano contra uno de sus hermanos y repetido contra otro, y las dos lecturas
> son correctas por separado. **Se leen enteras en la relectura, con la mesa como
> marco**, igual que los 32 racimos: una decision por familia, no una por pareja.

**Miembros verificados contra el grafo uno por uno.** Los tres racimos son
**enteramente de `core`**.

### Racimo nuevo A: LA PUERTA DEL AJUSTE (3 nodos)

| nodo | pasos | fuente |
|---|---:|---|
| `problem_solution_fit` | 4 | *The Startup Owner's Manual* (Blank) |
| `verificar_product_market_fit` | 5 | *The Startup Owner's Manual* (Blank) |
| `product_market_fit` | 6 | *The Startup Owner's Manual* (Blank) |

**Pares ya leidos**: puesto **297** (`problem_solution_fit` contra
`verificar_product_market_fit`) y puesto **338** (`problem_solution_fit` contra
`product_market_fit`), **los dos marcados B a proposito**.

> **Por que es familia y no dos parejas**: los tres **declaran el mismo momento en
> sus propias `condiciones_activacion`**, antes de entrar en Customer Validation,
> y los tres miden lo mismo, que el problema duela, que la solucion convenza a un
> precio pagable y que haya mercado suficiente. **Pero llevan nombres de dos hitos
> distintos de Blank**, ajuste problema-solucion y ajuste producto-mercado.
>
> **La pregunta real no es cual de dos sobra: es si el catalogo quiere uno, dos o
> tres hitos aqui.** Esa pregunta no se puede contestar mirando una pareja.

### Racimo nuevo B: LAS PUERTAS DEL STAGE-GATE (6 nodos)

| nodo | pasos | de que trata |
|---|---:|---|
| `sistema_stage_gate` | 4 | el sistema entero, etapas y gates |
| `stage_gate_system` | 5 | el sistema entero otra vez, con Go/Kill y playbook |
| `estructura_gates` | 4 | como se arma una puerta: entregables, criterios, responsable |
| `sistema_gates_go_kill` | 6 | la decision de la puerta: Go, Kill, Hold, Recycle |
| `asignacion_recursos_en_gates` | 4 | los recursos que se comprometen en la puerta |
| `sistema_gestion_recursos_en_gates` | 4 | los recursos otra vez, con el metodo de seguimiento |

**Los seis son de `core` y los seis declaran la misma fuente**, *Winning at New
Products* (Cooper). **Pares ya leidos**: puestos **275**, **302** y **356**, los
tres marcados **A**.

> **Aqui la incoherencia de pares ya se produjo**: los tres pares dieron A, o sea
> tres fusiones distintas, y **las tres no pueden ejecutarse a la vez sin decidir
> antes cuantos nodos quiere el catalogo para las puertas**. Uno que lo cuente
> todo, dos que separen sistema y puerta, o tres que separen sistema, puerta y
> recursos. **Es una decision de arquitectura, no tres podas.**

### Racimo nuevo C: LA APERTURA DE CUSTOMER VALIDATION (3 nodos)

| nodo | pasos | fuente declarada |
|---|---:|---|
| `customer_validation` | 5 | *The Startup Owner's Manual - Steve Blank* |
| `filosofia_validacion_clientes` | 4 | *The Startup Owner's Manual - **Blank, Steve*** |
| `introduccion_validacion_clientes` | 5 | *The Startup Owner's Manual - Steve Blank* |

**Pares ya leidos**: puestos **332** y **349**, **los dos marcados D**, sanos.

> **Este racimo se abre aunque sus dos pares salieran sanos**, y ese es
> justamente el motivo: **tres nodos abren la misma etapa** y cada pareja se
> defiende sola, uno con los actos, otro con la postura y otro con el temario.
> **Tres puertas de entrada a una sola sala pueden ser correctas y aun asi ser
> demasiadas.** Eso lo decide la mesa mirando las tres, no yo mirando dos.
>
> **DETALLE DE FUENTE, verificado y anotado porque sirve al barrido de fuentes**:
> **el mismo libro esta escrito de dos maneras** en el campo `fuente`, *Steve
> Blank* en dos nodos y *Blank, Steve* en el tercero. El campo `fuente` no esta
> normalizado, y cualquier conteo por libro que se haga con igualdad de cadena
> **contara ese libro como dos**.

### Las familias menores anotadas al paso, sin racimo todavia

**No suben a racimo porque el encargo nombra tres, pero quedan escritas para que
no haya que volver a encontrarlas.** Todas de `core` y ninguna en las nominas:

| familia | nodos | donde se vio |
|---|---:|---|
| el mapa de influencia | **3** | puestos 265 y 284 |
| las tecnicas de cierre en venta grande | **4** | puestos 274, 321 y 337 |
| el consejo asesor | **4** | puestos 328 y 367 |
| la senal de compra en venta grande | **3** | puestos 286 y 346 |
| el momento de fundar | **3** | puestos 290 y 347 |
| el habito de trabajo creativo | **3** | puestos 281 y 333 |
| el perfil del cliente y el mapa de valor | **3** | puestos 309 y 360, con figura de dos mitades mas nodo conjunto |

---

## 2. SILUETA BAUTIZADA: EL HIJO CON CASA PROPIA

**Definicion**: **un paso de un nodo vive ademas desarrollado como nodo propio.**
El nodo grande lo despacha en una linea; el chico lo convierte en cuatro o cinco
pasos con su propio titulo, sus propias condiciones y su propio entregable.

**Ocho casos en cien pares**, del 268 al 370. **Es la silueta mas frecuente del
tramo despues del calco simple**, y hasta ahora se venia marcando B por no saber
como leerla.

### La regla de lectura

> **arista madre a hijo, mas paso-resumen en la madre = JERARQUIA SANA.** El
> catalogo dice en un sitio que hay que hacer algo y en otro como se hace, y el
> lector llega del uno al otro porque **el grafo lo lleva**.
>
> **Sin arista = DUPLICACION.** El material esta dos veces y nada conecta las dos
> copias: quien lee la madre no se entera de que existe el hijo, y quien lee el
> hijo no sabe de donde sale.
>
> **Madre que RE-DESARROLLA = DUPLICACION**, aunque haya arista. Si la madre no
> se limita a resumir en un paso sino que vuelve a contar lo que el hijo cuenta,
> la jerarquia se rompe por arriba.

**Por eso la arista de HOY se registra ahora**: no cambia el veredicto del par,
**decide su lectura despues**, y el grafo se puede tocar en la pasada unica.

### Los ocho casos, con su arista verificada contra el grafo

| puesto | el hijo | la madre | paso | **arista HOY** |
|---:|---|---|---:|:---:|
| 316 | `duration_estimating_worksheet` | `activity_duration_estimates` | 1 | **SI**, en los dos sentidos |
| 336 | `hoja_estimacion_costos` | `estimacion_costos_actividad` | 2 | **SI**, madre a hijo y hijo a madre |
| 369 | `background_startup_vs_corporativo` | `contratacion_experiencia_vs_potencial` | 3 | **SI**, hijo a madre y madre lo tiene de previo |
| 279 | `intimation_illumination` | `wallas_etapa_iluminacion` | 2 | **NO** |
| 299 | `entrenamiento_de_gerentes_para_despidos` | `proceso_despidos_responsables` | 4 | **NO** |
| 318 | `comunicacion_a_toda_la_empresa` | `proceso_despidos_responsables` | 5 | **NO** |
| 337 | `cierre_satisfaccion_postventa` | `riesgo_tecnicas_cierre_venta_compleja` | 4 | **NO** |
| 347 | `decision_momento_fundacion` | `tres_preguntas_carrera` | 1 | **NO** |

**Tres con arista y cinco sin ella.**

> **Y las tres con arista son las tres de fuentes de gestion de proyectos y de
> contratacion, no las de metodo.** Las dos de estimacion, duraciones y costos,
> son ademas **el patron de fuente ya anotado en el puesto 336**: esa fuente
> publica el concepto y su hoja de trabajo como pareja, **y ademas los enlaza**.
> **Cuando la fuente trabaja bien, la silueta sale sana.** Es la mejor evidencia
> que hay de que la regla de lectura mide lo que dice medir.

---

### CHOCA CON EL ENCARGO: `proceso_despidos_responsables` NO es la primera madre de dos

**El encargo la nombra como primera MADRE de dos, pasos 4 y 5. El grafo dice otra
cosa, y la traigo en vez de escribirla como venia dictada.**

**Lo que hay de verdad**, verificado nodo por nodo:

| nodo | prev | sig |
|---|---|---|
| `ejecucion_rapida_de_despidos` (Horowitz) | falta_de_constancia_de_proposito | **`entrenamiento_de_gerentes_para_despidos`, `comunicacion_a_toda_la_empresa`** |
| `entrenamiento_de_gerentes_para_despidos` | **`ejecucion_rapida_de_despidos`** | `comunicacion_a_toda_la_empresa` |
| `comunicacion_a_toda_la_empresa` | **`ejecucion_rapida_de_despidos`, `entrenamiento_de_gerentes_para_despidos`** | confianza_mutua_fundadores |
| `proceso_despidos_responsables` | cultura_transparencia_organizacional | breakthrough_cultural |

> **La MADRE DE DOS existe y es `ejecucion_rapida_de_despidos`**: tiene arista a
> los dos hijos, los dos hijos la tienen a ella, y **los tres forman una cadena
> ordenada**, ejecutar rapido, entrenar a los gerentes, comunicar a la empresa.
> **Es el ejemplar limpio de jerarquia sana, no de duplicacion.**
>
> **`proceso_despidos_responsables` es otra cosa, y peor.** Sus cinco pasos
> incluyen los tres nodos de esa cadena: **su paso 2 es
> `ejecucion_rapida_de_despidos` entero** (minimizar el tiempo entre decision y
> ejecucion para evitar filtraciones), **su paso 4 es
> `entrenamiento_de_gerentes_para_despidos` entero**, y **su paso 5 es
> `comunicacion_a_toda_la_empresa` entero**. **Y no tiene arista con ninguno de
> los tres.**
>
> **Por la regla de lectura recien escrita, esto no es una madre: es
> DUPLICACION**, y de la peor especie, porque **no duplica un nodo sino una
> cadena entera que ya existia bien enlazada**. La regla lo decide sola, sin
> criterio nuevo.

**Silueta nueva que sale de aqui y que no estaba prevista: EL RESUMEN QUE
DUPLICA UNA CADENA.** No es un hijo con casa propia. Es **un nodo que vuelve a
contar en cinco pasos lo que tres nodos enlazados ya contaban**. Queda anotada
sin bautizar del todo: **si aparece un segundo ejemplar merece nombre; con uno
solo, no.**

### El segundo choque, mas pequeno y del mismo sitio: la madre de la intimacion ya tenia un hijo

**El puesto 279 se leyo como madre `wallas_etapa_iluminacion` e hijo
`intimation_illumination` sin arista. Es cierto, pero incompleto.**

> **`wallas_etapa_iluminacion` SI tiene arista a un hijo de la intimacion:
> `wallas_intimacion_fringe_consciousness`**, que existe, es del mismo libro de
> Wallas y desarrolla la misma sub-etapa en cuatro pasos.
>
> **O sea que la madre ya tiene su hijo con casa propia y bien enlazado, y hay un
> SEGUNDO hijo de la misma sub-etapa sin arista con ella.** No es una jerarquia
> rota: **es un gemelo de mas.**
>
> **La cola ya lo tiene fichado**: el par `intimation_illumination` contra
> `wallas_intimacion_fringe_consciousness` es el **puesto 403**, semantica 0,8499.
> **No lo juzgo aqui**: se lee cuando le toque, en orden.

**Lo que esto le hace a la regla**: la pregunta *hay arista o no* es correcta pero
**no basta con mirar la arista del par que se tiene delante**. Hay que mirar
**si la madre ya tiene otro hijo para ese mismo paso**, porque entonces el
problema no esta entre madre e hijo **sino entre los dos hijos**.

---

## 3. LA REGLA DE LA ARISTA, PUESTA A TRABAJAR (tramo 371 a 422)

**Desde que la silueta tiene regla, la arista se consulta ANTES de escribir la
clase.** En el tramo anterior la silueta se marcaba B por no saber leerla; en
este ya decide sola. **Cinco casos nuevos, y la regla los reparte en los dos
sentidos:**

| puesto | el hijo | la madre | paso | arista | clase que dicta la regla |
|---:|---|---|---:|:---:|---|
| 393 | `evaluacion_capital_para_cofundadores` | `busqueda_cofundador_complementario` | 1 | **NO** | **A**, duplicacion |
| 395 | `proceso_ideacion_modelo_negocio` | `proceso_diseno_modelo_negocio_5_fases` | 3 | **NO** | **A**, duplicacion |
| 396 | `elevator_pitch_inversion` | `preparacion_materiales_fundraising` | 1 | **NO** | **A**, duplicacion |
| 409 | `drag_along_agreement` | `co_sale_drag_along_agreements` | 4 | **SI** | **D**, jerarquia sana |
| 402 | `acuerdo_de_co_venta_y_votacion` | `co_sale_drag_along_agreements` | 6 | **SI** | **D**, jerarquia sana |

> **SEGUNDA MADRE DE DOS CON ARISTAS, y esta si lo es**: `co_sale_drag_along_agreements`
> reparte sus dos mitades en dos hijos y **enlaza a los dos**. El drag-along vive
> en `drag_along_agreement` y el acuerdo de votacion en
> `acuerdo_de_co_venta_y_votacion`. **Con `ejecucion_rapida_de_despidos` van dos
> madres sanas y bien enlazadas.**

### CORRECCION DECLARADA: el puesto 402 pasa de B a D

**El error es mio y su causa tambien.** Escribi el veredicto del 402 **sin
consultar la arista**, teniendo ya escrita la regla que la exige, y lo lei como
media coincidencia sospechosa entre dos nodos que comparten la clausula de
co-venta y difieren en la otra mitad. **Consultada la arista, eran los dos hijos
enlazados de la misma madre.** Corregido en el archivo, con la correccion y su
motivo escritos dentro de la razon del veredicto.

**La regla de metodo que deja**: la arista se consulta **antes** de escribir la
clase, no despues de escribirla.

### UNA COMPROBACION QUE SALIO VERDE, y se registra por eso

**Salieron dos nodos de MVP concierge que la cola no habia emparejado nunca**, y
lo persegui como posible fallo de recall del instrumento. **No lo era.**

| | |
|---|---:|
| nodos del grafo | **3835** |
| **deprecados** | **314** |
| activos | **3521** |
| en el indice semantico | **3521** |
| **activos sin vector** | **0** |
| aristas a ids inexistentes | **0** |

**`mvp_concierge` y `mvp_tipo_concierge` estan DEPRECADOS**; el unico vivo de los
tres es `concierge_mvp`. **El catalogo ya habia resuelto ese trio y el
instrumento hizo bien en no emparejarlos.** La cifra de 3521 del resumen es
correcta y la cobertura del cribado no tiene hueco.

### PERO LA COMPROBACION DESTAPO UNA ENMIENDA A LA REGLA DE LA ARISTA

**Las aristas hacia nodos deprecados existen, y son muchas:**

| | |
|---|---:|
| aristas salientes de nodos activos | **15 499** |
| de esas, **apuntan a un nodo DEPRECADO** | **1 149**, el **7,4%** |
| nodos activos con al menos una | **824** de 3521, el **23%** |

> **ENMIENDA: donde la regla dice *hay arista*, hay que leer *hay arista a un
> nodo VIVO*.** Una de cada trece aristas del catalogo apunta a un nodo retirado,
> y casi un cuarto de los nodos vivos tiene alguna. **Un hijo enlazado solo a
> traves de un nodo deprecado no esta enlazado.**
>
> **Ejemplo verificado, del puesto 395**: `proceso_diseno_modelo_negocio_5_fases`
> tiene arista con `fase_entender_modelo_negocio`, **que esta deprecado**. Y en el
> puesto 384, `mvp_catalogo_tecnicas` tiene entre sus previos a **dos** nodos
> deprecados de MVP concierge.
>
> **Ninguno de los nodos de los casos ya juzgados esta deprecado**, asi que **los
> ocho veredictos del tramo anterior y los cinco de este no cambian.** Verificado
> uno por uno.

---

## 4. FAMILIAS NUEVAS DEL TRAMO 371 a 422

**Todas de `core` y ninguna en `RACIMOS_MIEMBROS.jsonl`.** Se anotan aqui para
que la relectura las encuentre hechas.

| familia | nodos | puestos donde salio |
|---|---:|---|
| **la estrategia de innovacion y sus arenas** | **6** | 280, 357, 405, 422 |
| la palanca frente a los inversionistas | **4** | 334, 394, 413 |
| las cabezas de Customer Discovery | **4** | 269, 276, 291, 415 |
| el modelo financiero del fin de la validacion | 3 | 371, 404 |
| SPIN | 3 | 305, 401 |

> **La de innovacion es la mas grave despues de la del Stage-Gate**: **seis
> nodos**, y **tres de sus ids son el mismo nombre con y sin preposiciones**
> (`estrategia_de_innovacion_de_producto`, `estrategia_innovacion_producto`,
> `estrategia_de_innovacion_producto`). **Dos pares distintos del mismo nodo
> cayeron en DUDOSO por el mismo motivo**, los puestos 405 y 422, que es
> exactamente la firma de familia ya descrita: **el mismo nodo sale de una manera
> contra un hermano y de otra contra el siguiente.**

> **Y las cabezas de Customer Discovery tienen un detalle propio**:
> `customer_discovery_overview` y `customer_discovery_cuatro_fases` **llevan el
> mismo titulo exacto**, *Las cuatro fases para descubrir a tu cliente*. El racimo
> censado cubre solo parte de esta familia.
