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

> **REGLA FAMILIA DECLARADA, generalizada el 11 ago 2026 a TODO racimo declarado**
> (los de este informe y los 32 de `RACIMOS_MIEMBROS.jsonl`):
>
> **Un par cuyos DOS nodos pertenecen a un racimo ya declarado lleva razon
> `familia declarada` y NO pelea la clase.** Se registra con la clase que la
> silueta indique, sin argumentarla, **porque la decision ya esta tomada en otro
> sitio y discutirla aqui es trabajo que se tira.**
>
> **Lo que SI se anota de esos pares es cualquier cosa NUEVA**: un miembro que no
> estuviera en la nomina, una arista que cambie la forma, o un choque con la
> lectura de la familia. **La regla ahorra discusion, no observacion.**
>
> **Nacio para el racimo del cierre en venta grande (seccion 9) y se extiende
> aqui** porque el razonamiento no depende de esa familia: **vale para cualquiera
> que ya haya subido.**

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

---

## 5. FIGURA NUEVA: CENTRO SANO CON GEMELO SIN CASA

**Nace de reordenar el racimo del puesto 360, y el reordenamiento cambia el
arreglo, no solo la descripcion.**

### Como se leyo primero, y por que estaba incompleto

**En el puesto 360 la familia del lienzo de propuesta de valor se registro como
RACIMO NUEVO con la silueta de dos mitades mas un nodo conjunto**, la misma del
racimo de capital de trabajo: `customer_profile` y `value_map` como mitades, y
`customer_profile_value_map` como el nodo que las cuenta juntas.

**Estaba bien descrito y mal encuadrado, y el motivo es el de siempre: no habia
mirado las aristas.** Con la regla ya escrita, el puesto 459 obligo a mirarlas.

### Lo que dice el grafo, verificado

| nodo | papel |
|---|---|
| **`value_proposition_canvas`** | **EL CENTRO.** Sus cuatro pasos son descargar la plantilla, dibujar el perfil, dibujar el mapa y trabajar los dos lados hasta el encaje |
| `customer_profile` | pieza, **enlazada** desde el centro |
| `value_map` | pieza, **enlazada** desde el centro |
| `fit_value_proposition` | pieza, **enlazada** desde el centro y con arista de vuelta |
| **`customer_profile_value_map`** | **EL GEMELO: NO esta entre los enlazados del centro** |

> **El centro enlaza con las TRES piezas que nombra en sus propios pasos.** Es la
> jerarquia sana en su mejor forma vista hasta ahora: un nodo que enumera partes y
> el grafo llevando a cada una.
>
> **Y `customer_profile_value_map` cuenta las dos primeras juntas sin estar
> enlazado con el centro ni con ninguna de ellas.** No es una pieza mas: **es una
> segunda version del centro, sin casa.**

### La figura, y su anatomia

> **CENTRO SANO CON GEMELO SIN CASA**: un nodo hace de centro y enlaza con las
> piezas que enumera; **y existe ademas otro nodo que cuenta lo mismo que el
> centro, o parte de ello, sin arista con nadie de la familia.**
>
> **La familia no esta rota. Lo que sobra es uno.**

**No es la primera vez: es la segunda, y la primera se leyo mal por el mismo
motivo.** En el puesto 279 se registro `wallas_etapa_iluminacion` como madre sin
arista con `intimation_illumination`. **Y era cierto pero incompleto**: la madre
**si** tiene arista con `wallas_intimacion_fringe_consciousness`, que desarrolla
la misma sub-etapa. **Tambien alli habia un centro sano y un gemelo sin casa**,
y el par de los dos gemelos es el puesto 403, ya leido como A.

| ejemplar | el centro | la pieza enlazada | **el gemelo sin casa** |
|---|---|---|---|
| lienzo de propuesta de valor | `value_proposition_canvas` | `customer_profile`, `value_map`, `fit_value_proposition` | **`customer_profile_value_map`** |
| iluminacion de Wallas | `wallas_etapa_iluminacion` | `wallas_intimacion_fringe_consciousness` | **`intimation_illumination`** |

### LO QUE CAMBIA EN EL ARREGLO, que es el motivo de nombrarla

> **Un racimo desordenado se resuelve DESMONTANDO la familia: hay que decidir
> cuantos nodos quiere el catalogo y repartir el material, que es lo que la mesa
> hace con los seis del Stage-Gate.**
>
> **Un centro sano con gemelo sin casa NO se desmonta: se resuelve el gemelo.** El
> centro y sus piezas se quedan como estan, con sus aristas, y **la unica decision
> es que hacer con el que sobra**: absorberlo en el centro, o enlazarlo si resulta
> que aporta algo que el centro no dice.
>
> **Es una decision de un nodo en vez de una decision de familia, y por eso es
> mucho mas barata.** Nombrarla sirve exactamente para no llevar a la mesa lo que
> no hace falta llevar.

**Consecuencia para el racimo del 360**: **deja de ser un racimo nuevo que pide
mesa** y pasa a ser **un centro sano con un gemelo que resolver**. La familia
entera son **siete nodos** (`value_proposition_canvas`, `customer_profile`,
`value_map`, `fit_value_proposition`, `customer_profile_value_map`,
`value_proposition_startup` y `desarrollo_value_proposition_usp`), pero **solo uno
esta en cuestion.**

> **Y queda la pregunta de metodo, que apunto sin contestar**: **cuantos de los
> racimos ya declarados son en realidad centros sanos con un gemelo.** Los dos
> primeros ejemplares aparecieron los dos por mirar la arista despues de haber
> escrito el veredicto. **La comprobacion es barata y hay que hacerla antes de
> llevar nada a la mesa.**

---

## 6. BARRIDO DE ARISTAS DE LOS RACIMOS

**Mecanico y de solo lectura. Es un MAPA, no una adjudicacion:** dice que forma
tiene cada racimo en el grafo, y la lectura de racimos lo usara para saber a que
se enfrenta antes de abrir ninguno.

**Poblacion**: los **32 racimos con nomina** de `docs/RACIMOS_MIEMBROS.jsonl` mas
los **4 nuevos que ya tienen miembros escritos** en este informe. **36 racimos.**

### Como se midio, dicho entero para que se pueda discutir

1. **Cada arista se resuelve a NODO VIVO caminando `ids_alias`**, que es la
   enmienda vigente de la seccion 3. **Hizo falta 101 veces**: sin resolver, esas
   101 aristas se habrian contado como inexistentes.
2. Solo cuentan las aristas **entre miembros del mismo racimo**. Se ignoran las
   que salen fuera.
3. La arista se cuenta **sin direccion**: si A apunta a B o B apunta a A, es una.
4. **Formas**, y los umbrales van escritos porque son elegidos por mi, no
   derivados de nada:
   - **SUELTO**: cero aristas internas.
   - **CENTRO ENLAZADO**: hay **un solo** miembro de grado maximo, y ese grado es
     **al menos 2** y **al menos la mitad** de los demas miembros.
   - **CADENA**: ningun miembro pasa de grado 2, no hay aislados y las aristas no
     superan n menos 1.
   - **MIXTO**: todo lo demas.
5. **Candidato a CENTRO SANO CON GEMELO SIN CASA**: hay un unico miembro de grado
   maximo con grado 2 o mas, **y uno o dos miembros con cero aristas internas.**
   Esos son los gemelos.

> **VERIFICACION DE NOMINA, y salio limpia: CERO incidencias.** Los **171
> miembros** de las 32 nominas y los de los cuatro nuevos **resuelven todos a un
> nodo vivo**, ninguno hay que buscarlo por alias y ninguno ha desaparecido.

### EL RESULTADO, y no es el que esperaba

| forma | racimos |
|---|---:|
| **CENTRO ENLAZADO** | **3** |
| **MIXTO** | **18** |
| **SUELTO** | **15** |
| | **36** |

> **QUINCE de los treinta y seis racimos no tienen NI UNA arista entre sus
> miembros.** Y si se cuenta a los que tienen **una sola**, que a efectos de
> navegacion es lo mismo, **son VEINTICUATRO de treinta y seis: dos tercios.**
>
> **Eso es un hallazgo sobre el catalogo, no sobre los racimos.** Un racimo es
> un grupo de nodos que dicen lo mismo o casi. **Que dos tercios de esos grupos
> no esten conectados por el grafo significa que el lector que cae en uno de sus
> miembros no tiene por donde llegar a los otros.** La duplicacion no solo
> repite: **repite sin avisar.**

### LOS CINCO CANDIDATOS A CENTRO SANO CON GEMELO SIN CASA

**Son los racimos que la figura de la seccion 5 resuelve barato**, sin desmontar
la familia:

| racimo | n | el centro | grado | **el gemelo o los gemelos** |
|---|---:|---|---:|---|
| NUEVO: el lienzo de propuesta de valor | 7 | `value_proposition_canvas` | 4 | **`customer_profile_value_map`, `desarrollo_value_proposition_usp`** |
| Auditoria de calidad | 6 | `principios_auditoria_calidad` | 3 | **`auditoria_calidad`, `reporte_auditoria`** |
| Mapeo del flujo de valor | 5 | `ocho_desperdicios_lean` | 2 | **`analisis_flujo_de_valor`, `value_stream_mapping_ambiental`** |
| La estructura de cinturones de Six Sigma | 9 | `rol_black_belt` | 2 | **`desarrollo_expertos_capaces`, `rol_facilitador_black_belt`** |
| Los puntos de Deming en el titulo | 7 | `adopcion_liderazgo` | 2 | **`eliminar_slogans_metas`, `mejora_continua_del_sistema`** |

> **El del lienzo de propuesta de valor tiene DOS gemelos, no uno.** La seccion 5
> nombro a `customer_profile_value_map`; el barrido anade
> **`desarrollo_value_proposition_usp`**, que tampoco esta enlazado con nadie de
> la familia. **Es una correccion a lo que escribi ayer**, y sale de medir en vez
> de mirar.

### LA TABLA ENTERA, racimo por racimo

**`n`** son los miembros, **`ar`** las aristas internas y **`ais`** los miembros
sin ninguna arista dentro del racimo.

| racimo | origen | n | ar | ais | forma | miembro mas enlazado |
|---|---|---:|---:|---:|---|---|
| NUEVO: el lienzo de propuesta de valor | informe | 7 | 7 | 2 | **CENTRO ENLAZADO** | `value_proposition_canvas` (4) |
| Auditoria de calidad | nomina | 6 | 4 | 2 | **CENTRO ENLAZADO** | `principios_auditoria_calidad` (3) |
| Mapeo del flujo de valor | nomina | 5 | 2 | 2 | **CENTRO ENLAZADO** | `ocho_desperdicios_lean` (2) |
| No culpar a la persona, arreglar el sistema | nomina | 20 | 14 | 4 | **MIXTO** | `ciclo_de_culpa` (3) |
| Causas comunes y responsabilidad del sistema | nomina | 12 | 7 | 4 | **MIXTO** | `causas_comunes_vs_especiales` (3) |
| Cradle to cradle | nomina | 11 | 8 | 3 | **MIXTO** | `desperdicio_es_alimento` (4) |
| La estructura de cinturones de Six Sigma | nomina | 9 | 4 | 2 | **MIXTO** | `rol_black_belt` (2) |
| Portafolio: revisar, podar, reasignar | nomina | 7 | 1 | 5 | **MIXTO** | `gestion_portafolio_formal` (1) |
| Customer discovery: salir a hablar con el cliente | nomina | 7 | 3 | 1 | **MIXTO** | `customer_development_modelo` (1) |
| Los puntos de Deming en el titulo | nomina | 7 | 3 | 2 | **MIXTO** | `adopcion_liderazgo` (2) |
| NUEVO: las puertas del Stage-Gate | informe | 6 | 2 | 2 | **MIXTO** | `asignacion_recursos_en_gates` (1) |
| Benchmarking | nomina | 5 | 1 | 3 | **MIXTO** | `monitoreo_continuo_benchmarking` (1) |
| Los cinco porques | nomina | 5 | 5 | 0 | **MIXTO** | `cinco_porques_master` (3) |
| Pivotar o proceder | nomina | 5 | 1 | 3 | **MIXTO** | `decision_pivotar_o_proceder` (1) |
| El avance y el compromiso en la venta | nomina | 5 | 1 | 3 | **MIXTO** | `advances_vs_continuations` (1) |
| Encuadre del problema (How Might We) | nomina | 5 | 2 | 1 | **MIXTO** | `how_might_we_brief_social` (1) |
| Analisis de causa raiz | nomina | 4 | 1 | 2 | **MIXTO** | `analisis_diagnostico_causa` (1) |
| Las reglas del brainstorming | nomina | 4 | 1 | 2 | **MIXTO** | `brainstorming` (1) |
| Metas de calidad | nomina | 3 | 1 | 1 | **MIXTO** | `establecer_estandares_desempeno` (1) |
| El efectivo contra la ganancia | nomina | 3 | 1 | 1 | **MIXTO** | `cash_is_king` (1) |
| NUEVO: la apertura de Customer Validation | informe | 3 | 1 | 1 | **MIXTO** | `filosofia_validacion_clientes` (1) |
| Accion correctiva | nomina | 7 | 0 | 7 | **SUELTO** | ninguno |
| Ciclo de mejora PDCA / PDSA | nomina | 4 | 0 | 4 | **SUELTO** | ninguno |
| Clasificacion de defectos | nomina | 4 | 0 | 4 | **SUELTO** | ninguno |
| NUEVO: la puerta del ajuste | informe | 4 | 0 | 4 | **SUELTO** | ninguno |
| Fitness for purpose | nomina | 3 | 0 | 3 | **SUELTO** | ninguno |
| Costo de calidad | nomina | 3 | 0 | 3 | **SUELTO** | ninguno |
| Consejo de calidad | nomina | 3 | 0 | 3 | **SUELTO** | ninguno |
| Eliminacion de causas de error | nomina | 3 | 0 | 3 | **SUELTO** | ninguno |
| Plan y matriz de control | nomina | 3 | 0 | 3 | **SUELTO** | ninguno |
| Diversidad en el diseno | nomina | 3 | 0 | 3 | **SUELTO** | ninguno |
| La etapa de investigacion en la venta | nomina | 3 | 0 | 3 | **SUELTO** | ninguno |
| Estrategia de innovacion de producto | nomina | 3 | 0 | 3 | **SUELTO** | ninguno |
| Programa de catorce pasos de Crosby | nomina | 3 | 0 | 3 | **SUELTO** | ninguno |
| Poka yoke | nomina | 3 | 0 | 3 | **SUELTO** | ninguno |
| Obtencion de compromiso | nomina | 3 | 0 | 3 | **SUELTO** | ninguno |

### Lo que la tabla dice, en tres lecturas

> **1. Los racimos grandes estan mejor conectados que los pequenos.** Los tres de
> mas de diez miembros (*No culpar a la persona* con 20, *Causas comunes* con 12,
> *Cradle to cradle* con 11) son todos MIXTO con varias aristas. **Los de tres
> miembros son casi todos SUELTOS.** Tiene sentido: un tema grande se escribio
> como recorrido y se enlazo; un trio de gemelos se escribio tres veces y nadie
> los presento.
>
> **2. `NUEVO: la puerta del ajuste` es SUELTO con cuatro miembros y cero
> aristas**, y eso refuerza lo que ya decia su ficha: cuatro nodos juzgando la
> misma puerta **sin que ninguno sepa de los otros.**
>
> **3. `Portafolio: revisar, podar, reasignar` tiene siete miembros y UNA arista,
> con cinco aislados.** Es el racimo censado peor conectado de todos, y es
> ademas el que toca al racimo nuevo de las puertas del Stage-Gate por el puesto
> 488. **La mesa de las puertas se va a encontrar con eso.**

**NO SE ADJUDICA NADA AQUI.** La tabla es el mapa; las decisiones son de la mesa.

---

## 7. RACIMO NUEVO: LAS METRICAS DE COHORTE

**Sube a racimo el 11 ago 2026 por la firma que este informe ya tiene descrita:
el mismo nodo sale de tres maneras distintas segun con que hermano se compare.**

### Los tres pares que lo obligan

| puesto | el par | clase | por que |
|---:|---|:---:|---|
| **353** | `metricas_cohortes` contra `analisis_de_cohortes` | **A** | mismo instrumento, mismo uso |
| **478** | `metricas_cohortes` contra `metricas_accionables` | **D** | hijo con casa propia **CON arista**: jerarquia sana |
| **522** | `metricas_cohortes` contra `retention_metrics` | **A** | hijo con casa propia **SIN arista**: duplicacion |

> **`metricas_cohortes` es a la vez un duplicado, un hijo legitimo y un
> duplicado otra vez, segun a quien se le ponga al lado.** Las tres lecturas son
> correctas por separado y **ninguna se puede ejecutar sin las otras dos
> delante**, que es la definicion de familia que este informe usa desde la
> seccion 1.

### Los miembros, verificados contra el grafo

**Cinco nodos vivos, los cinco de `core`:**

| nodo | pasos | fuente |
|---|---:|---|
| **`metricas_accionables`** | 6 | *The Lean Startup* (Ries) |
| `metricas_cohortes` | 4 | *The Lean Startup* (Ries) |
| `analisis_de_cohortes` | 5 | *The Startup Owner's Manual* (Blank) |
| `tres_as_de_metricas` | 5 | *The Lean Startup* (Ries) |
| `retention_metrics` | 9 | *The Startup Owner's Manual* (Blank) y *Never Lose a Customer Again* (Coleman) |

> **Y hay un sexto que ya esta resuelto**: `cohort_analysis_retencion`, **5 pasos,
> DEPRECADO**. **Esta familia ya tuvo un duplicado retirado en su dia**, lo que
> dice que alguien la miro antes y no la termino.

### La forma, medida con el metodo de la seccion 6

**Aristas internas resueltas a nodo vivo:**

| nodo | toca dentro del racimo | grado |
|---|---|---:|
| **`metricas_accionables`** | `analisis_de_cohortes`, `metricas_cohortes`, `tres_as_de_metricas` | **3** |
| `metricas_cohortes` | `metricas_accionables`, `tres_as_de_metricas` | 2 |
| `tres_as_de_metricas` | `metricas_accionables`, `metricas_cohortes` | 2 |
| `analisis_de_cohortes` | `metricas_accionables` | 1 |
| **`retention_metrics`** | **ninguno** | **0** |

> **FORMA: CENTRO ENLAZADO.** `metricas_accionables` toca a tres de los otros
> cuatro y es el unico de grado maximo.
>
> **Y CANDIDATO A CENTRO SANO CON GEMELO SIN CASA**, la figura de la seccion 5:
> **centro `metricas_accionables`, gemelo `retention_metrics`**, que no enlaza con
> ninguno de los otros cuatro.
>
> **Con esto son SEIS los candidatos a esa figura**, los cinco de la tabla de la
> seccion 6 mas este.

### Lo que esto le hace al arreglo

> **La familia no se desmonta.** Cuatro de los cinco cuelgan de un centro que los
> enlaza, y esa parte esta sana. **Lo que hay que resolver son dos cosas y no
> cinco:**
>
> 1. **El gemelo `retention_metrics`**, que ademas es la primera **COSTURA FUERA
>    DE COLA** de la ficha de costuras: **lleva dos temas pegados** y su cirugia
>    es partirlo. **Partirlo puede resolver el gemelo de paso**, porque su mitad
>    de retencion es lo que se solapa con el racimo y la de adquisicion no.
> 2. **El par del puesto 353**, `metricas_cohortes` contra `analisis_de_cohortes`,
>    que repite y **cuelga del mismo centro**: ahi si hay fusion que hacer.
>
> **Las dos decisiones son de nodo, no de familia. El centro se queda como esta.**

---

## 8. LA RELECTURA DE LAS A, y su metodo

**Frente nuevo, abierto por el auditor el 11 ago 2026 y en paralelo al cribado.**
La cola del cribado **no cambia por esto**: sigue en orden y sin saltos.

> **QUE ES.** El cribado emite un veredicto por par leyendo los dos nodos. **La
> relectura vuelve sobre las A ya registradas** y pregunta otra cosa: **si la
> fusion se sostiene al mirarla como operacion**, no como juicio.
>
> **Por que hace falta.** Un par puede repetir de verdad y aun asi **no tener
> superviviente claro**, o tener uno que pierde material al fusionar. **La A dice
> que sobra uno; no dice cual.**

### TANDA R1: seis puestos, SEIS DE SEIS SOSTENIDAS

| puesto | el par | sostiene |
|---:|---|:---:|
| **3** | `domina_lo_que_compras` contra `investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor` | **si** |
| **156** | `customer_discovery_cuatro_fases` contra `customer_discovery_overview` | **si** |
| **160** | `gestion_sindicato_inversores` contra `manejo_syndicate_inversion` | **si** |
| **161** | `asignacion_agil_de_recursos` contra `presupuesto_agil_innovacion` | **si** |
| **165** | `seleccion_canal_distribucion` contra `seleccion_canal_fisico` | **si** |
| **166** | `human_in_the_loop_ia` contra `principio_humano_en_el_loop` | **si** |

**Ninguna se cae.** Es la primera medida de fiabilidad que tiene el cribado sobre
si mismo, y con seis casos **no prueba nada todavia**; lo que hace es **abrir la
serie**.

### LA NOTA DE DIRECCION DE FUSION DEL PUESTO 165, verificada contra el grafo

**Es lo que la relectura anade y el cribado no daba: quien sobrevive.**

| | `seleccion_canal_distribucion` (5 pasos) | `seleccion_canal_fisico` (4 pasos) |
|---|---|---|
| habitos de compra de la categoria | paso 1 | paso 3 |
| evaluar el canal por costo y control | paso 2 | paso 2 |
| complejidad y precio del producto contra el canal | paso 3 | paso 1, como listado de opciones |
| **recalcular la hipotesis de INGRESOS NETOS con los costos del canal** | **paso 4** | **NO LO TIENE** |
| quedarse con UN canal y no lanzar por varios | paso 5 | paso 4 |

> **`seleccion_canal_distribucion` es SUPERCONJUNTO de `seleccion_canal_fisico`.**
> Cubre sus cuatro pasos y **trae uno que el otro no tiene**, el que devuelve el
> costo del canal al modelo de ingresos. **Superviviente natural.**

> **UNA PRECISION QUE LA FUSION TIENE QUE LLEVARSE, y no contradice la
> direccion**: lo unico propio del nodo que muere es **el encuadre fisico**, su
> paso 1 lista *opciones de canal fisico relevantes para la industria*. **El
> superviviente habla de canal en general.** **Al fusionar hay que conservar el
> ejemplo fisico**, o la fusion gana un paso y pierde una concrecion.

### LA REGLA QUE ESTA TANDA DEJA

> **La relectura no revisa el veredicto: revisa la OPERACION.** Sus tres
> preguntas, en este orden:
>
> 1. **Se sostiene la A?** Si no, vuelve al cribado con su razon.
> 2. **Quien sobrevive?** Y la respuesta se justifica **por contenido**, no por
>    antiguedad ni por longitud: **sobrevive el superconjunto**.
> 3. **Que se pierde al fusionar?** Lo que solo tenga el que muere **se anota
>    para que viaje**, como el encuadre fisico del 165.
>
> **La tercera pregunta es la que evita que una fusion correcta empobrezca el
> catalogo.**

### TANDA R2: seis puestos mas, SEIS DE SEIS SOSTENIDAS

**Acumulado de la relectura: 12 de 12.**

| puesto | el par | sostiene |
|---:|---|:---:|
| **169** | `estrategia_plataformas_existentes` contra `existing_platforms_leverage` | **si** |
| **173** | `mission_and_operations_planning` contra `proceso_sop_mop` | **si** |
| **174** | `cultura_climatica_innovacion` contra `cultura_de_innovacion` | **si** |
| **175** | `customer_discovery_get_out_of_building` contra `get_out_of_the_building` | **si** |
| **176** | `targeting_blogs_channel` contra `targeting_blogs_traccion` | **si** |
| **177** | `comprension_capacidades_limitaciones_ia` contra `jagged_frontier_ia` | **si** |

**Y esta tanda trae lo que R1 no habia necesitado: TRES casos donde la tercera
pregunta, que se pierde al fusionar, tiene respuesta larga.** Verificados contra
el grafo paso por paso.

#### 175: la fusion tiene que llevarse TRES cosas, y ninguna esta en los dos

**Los dos nodos dicen salir a hablar con clientes. Ninguno es superconjunto del
otro: cada uno trae lo suyo.**

| lo que hay que conservar | de que nodo sale |
|---|---|
| **hipotesis-primero**: *identifica tus hipotesis clave sobre el problema, el cliente y la solucion* antes de salir | `customer_discovery_get_out_of_building`, paso 1 |
| **lidera-tu-mismo**: *lidera tu mismo estas conversaciones, no las delegues en personal junior* | `get_out_of_the_building`, paso 2 |
| **documenta-al-momento**: *documenta lo que aprendes de cada conversacion EN EL MOMENTO (blog, CRM)* | `get_out_of_the_building`, paso 4 |

> **Aqui no hay superviviente natural: hay una fusion que se escribe.** Y las tres
> instrucciones **viajan las tres**, porque cada una tapa un fallo distinto: salir
> sin hipotesis, delegar la salida, y salir y no anotar.

#### 174: sobrevive el largo, pero el corto tiene el TONO

**`cultura_de_innovacion` (6 pasos) contra `cultura_climatica_innovacion` (3).**
El largo trae la mecanica entera, reconocimiento, politica de no castigar el error
honesto, comunicacion abierta y recursos para proyectos audaces.

> **Sobrevive el largo. Pero lo que el corto tiene y el largo no es EL TONO
> INTROSPECTIVO**, y es literal: *revisa si de verdad le dedicas tiempo a apoyar
> los proyectos, **no solo dinero***; *abre espacios para que las ideas puedan
> venir de cualquiera, **no solo de ti***.
>
> **El corto le habla al fundador de sus propios actos; el largo describe un
> sistema.** **La fusion conserva el tono o el nodo pierde a quien lo lee.**

#### 173: superconjunto LEVE, y el que muere tiene sabor propio

**`proceso_sop_mop` es superconjunto de `mission_and_operations_planning`, pero
por poco**: los cinco pasos corren en paralelo y **lo unico que el primero anade
es el cierre del ciclo**, *implementar el plan y monitorear con datos
actualizados, ajustando en tiempo real*, donde el segundo se detiene en *simular
antes de ejecutarlo*.

> **Superviviente: `proceso_sop_mop`.** Y lo que hay que conservar del otro es
> **el sabor de mision**: su vocabulario es humanitario o militar, *poblacion
> afectada*, *suministros*, *vehiculos disponibles*. **El superviviente habla de
> negocio; el que muere habla de operacion de emergencia**, y ese encuadre es un
> caso de uso real que no se puede tirar con el nodo.

> **LOS TRES CASOS ENSEÑAN LO MISMO Y POR ESO VAN JUNTOS**: en 175 no hay
> superviviente, en 174 lo hay pero pierde el tono, en 173 lo hay pero pierde el
> encuadre. **Ninguna de las tres perdidas se ve mirando cual nodo tiene mas
> pasos**, que es lo que una fusion apresurada mira.

### TANDAS R3 y R4: doce puestos mas, DOCE DE DOCE SOSTENIDAS

**Acumulado de la relectura: 24 de 24.** Todos los pares verificados contra el
grafo paso por paso al escribir su perdida.

> **NOTA GENERAL QUE GOBIERNA LA MITAD DE ESTAS DIRECCIONES**: los pares que
> pertenecen a una **familia declarada** llevan su direccion de fusion como
> **PROVISIONAL DE PAR**. Se fija **al leer la familia entera**, por la doctrina
> del banco 9.3: **una direccion decidida sobre un par no sobrevive a su
> familia.** Van marcados abajo.

#### R3, seis puestos

| puesto | el par | que se pierde si no viaja |
|---:|---|---|
| **178** | `comunidad_tribu_marca` contra `construccion_tribu_de_marca` | **celebrar-historias** del primero; **transformacion-de-identidad** y **simbolos** (merchandising, insignias) del segundo |
| **179** | `storyboard` contra `storyboard_prototipado` | **time-box de 30 a 45 minutos** y **actuar-el-storyboard** del primero; **titular-escenas** del segundo |
| **182** | `comunicacion_transparente_en_crisis` contra `liderazgo_frente_crisis_competitiva` | **contacto-proactivo con medios** del primero; **practica-bajo-presion** del segundo |
| **183** | `fase_activate` contra `fase_activate_primera_impresion` | **expectativas claras y momentum temprano** del primero; **momento-exacto del primer contacto**, **eliminar barreras** y **reaccion emocional** del segundo |
| **184** | `scorecard_de_seleccion_de_proyectos` contra `scoring_model_scorecard` | **scorecard-por-tipo de proyecto** e **indicador-de-productividad** del segundo |
| **185** | `ecuacion_de_valor_cliente` contra `ecuacion_de_valor_venta` | **las preguntas SPIN nombradas** (Implicacion y Necesidad-Beneficio) del primero; **agrandar-el-problema** del segundo |

> **El 183 es de familia declarada** (la de la experiencia de Coleman) y **el 178
> tambien**: sus direcciones quedan **provisionales de par**.
>
> **Y el 184 confirma algo que ya estaba escrito en otra ficha**: es el **cuarto
> par calcado del nucleo** registrado en `docs/FICHA_SUBFUSION_GRADIENTE.md`,
> puestos 174 y 322 de aquella numeracion. **La relectura lo sostiene**, y eso
> queda anotado alli.

#### R4, seis puestos

| puesto | el par | que se pierde si no viaja |
|---:|---|---|
| **188** | `criterios_equity_split` contra `split_igual_vs_desigual` | **el anti-apreton-de-manos** del corto: *no cierres el acuerdo con un simple apreton de manos rapido* |
| **189** | `proceso_decision_vc` contra `proceso_diligencia_vc` | **rol-del-contacto** (asociado contra socio) y **senales-de-alerta** del primero; **pregunta-el-proceso y los proximos pasos** del segundo |
| **192** | `refinar_sales_roadmap` contra `sales_roadmap` | **sobrevive `refinar_sales_roadmap`**, que es superconjunto claro, 6 pasos contra 3 |
| **194** | `analisis_entorno_modelo_negocio` contra `business_model_environment_mapping` | **preguntas-estrategicas-por-bloque del Canvas** del segundo; **stakeholders y su influencia** del primero |
| **195** | `sistema_tres_rs_alineacion` contra `three_rs_equilibrium` | **los elefantes en la habitacion** y **documenta-por-escrito** del segundo |
| **197** | `obtencion_compromiso_venta` contra `obtencion_de_compromiso` | **evita-presion** del primero; **el compromiso mas alto que el cliente pueda dar de verdad** del segundo |

> **CUATRO DE LOS SEIS SON DE FAMILIA DECLARADA y sus direcciones quedan
> PROVISIONALES DE PAR**: el **188** de la familia del reparto de equity (seis
> nodos), el **192** de la del sales roadmap, el **195** de la de las tres Rs, y
> el **197** de la de obtencion de compromiso, que vive dentro del racimo censado
> del avance en la venta.

### LO QUE VEINTICUATRO DE VEINTICUATRO SIGNIFICAN, y lo que no

> **Lo que significan**: en veinticuatro relecturas **el cribado no ha emitido una
> sola A que no se sostenga**. Sobre 194 A registradas, eso es una muestra del
> 12%, y es la primera cifra de fiabilidad que la campana tiene sobre si misma.
>
> **Lo que NO significan**: la relectura **no vuelve a leer los nodos desde cero**,
> los mira con la razon del cribado delante. **Una A mal puesta por haber leido
> mal los dos nodos pasaria las dos veces.** Lo que esta serie prueba es que **la
> clase es coherente con la razon escrita**, no que la razon fuera correcta.
>
> **Donde si esta mordiendo**: **en las perdidas.** De los doce pares de R3 y R4,
> **todos menos uno** tienen material que se perderia en una fusion apresurada, y
> el unico que no, el 192, es superconjunto limpio. **Once de doce fusiones
> necesitan que alguien escriba que se lleva del que muere.**

### TANDA R5, EN MODO CIEGO: el control de la observacion de 24 de 24

**El auditor adjudico seis puestos CON LAS RAZONES TAPADAS, y al destapar
coincidio SEIS DE SEIS.** Acumulado de la relectura: **30 de 30**.

> **POR QUE ESTA TANDA EXISTE.** Al cerrar R4 escribi una objecion contra mi
> propia serie: *la relectura no vuelve a leer los nodos desde cero, los mira con
> la razon del cribado delante, asi que una A mal puesta por haber leido mal los
> dos nodos pasaria las dos veces.* **La tanda ciega es la respuesta a esa
> objecion**: sin la razon delante, la coincidencia ya no puede venir de haberla
> leido.

| puesto | el par | coincide a ciegas |
|---:|---|:---:|
| **200** | `hoja_de_ruta_de_ventas` contra `refinar_sales_roadmap` | **si** |
| **206** | `customer_discovery` contra `customer_discovery_overview` | **si** |
| **207** | `estrategia_de_innovacion_arenas` contra `estrategia_de_innovacion_y_tecnologia` | **si** |
| **209** | `etapa_de_investigacion` contra `etapa_investigacion_ventas` | **si** |
| **211** | `framework_excelencia_operacional` contra `preguntas_excelencia_operacional` | **si** |
| **212** | `storytelling_como_herramienta_de_diseno` contra `storytelling_para_el_cambio` | **si** |

### EL LIMITE, dicho antes que el resultado

> **Son SEIS pares.** Con seis casos y coincidencia perfecta, **lo unico que queda
> descartado es que la razon escrita estuviera arrastrando al segundo lector en
> estos seis**. **No queda medida la tasa de acuerdo del metodo**: para eso hacen
> falta mas tandas ciegas, y sobre todo **pares donde la clase sea discutible**,
> que es donde un control muerde.
>
> **Y no sustituye al control de fondo.** El control de fondo de esta campana
> sigue siendo **la muestra pineada de las D**, que se sortea con procedimiento
> reproducible y se lee al cierre: **esa mide si el cribado esta DEJANDO PASAR
> duplicados**, que es el error que ninguna relectura de las A puede ver, porque
> las A no son la poblacion donde vive ese error.
>
> **En una frase: la tanda ciega controla que la razon no contamine. La muestra
> pineada controla que la clase no se equivoque en la otra direccion.** Hacen
> falta las dos.

### LO QUE LA CIEGA AÑADIO, y esto si es ganancia neta

**Cuatro matices que la lectura con razon delante no habia producido.** Los cuatro
verificados contra el grafo.

> **211: EL MISMO FRAMEWORK EN DOS DIRECCIONES DE USO.**
> `framework_excelencia_operacional` manda **documentar y disenar tus propios
> procesos**; `preguntas_excelencia_operacional` manda **preguntarle al ejecutivo
> por los suyos**. **Mismo contenido, dos usos: autoauditoria y entrevista.**
> **La fusion conserva las dos direcciones**, o el nodo sirve para la mitad de los
> casos.

> **212: EL MISMO METODO CON DOS OBJETIVOS.**
> `storytelling_como_herramienta_de_diseno` busca **que la audiencia se apropie de
> la historia y la difunda**; `storytelling_para_el_cambio` busca **cambiar
> comportamientos concretos en una poblacion**. **Difusion y cambio de conducta no
> son el mismo objetivo, y el metodo si es el mismo.** **La fusion conserva los
> dos objetivos.**

> **209: UN MATIZ DE AUDIENCIA, y apunta mas lejos que este par.**
> `etapa_de_investigacion` le habla **al vendedor de sus propios actos** (*dedica
> tiempo*, *resiste la tentacion*). `etapa_investigacion_ventas` le habla **a quien
> dirige a otros** (*entrenar al equipo comercial*, *medir la proporcion en las
> llamadas propias*). **Es la voz de dirigir, no la de ejecutar.**
>
> **ANOTADO PARA EL FUTURO MUNDO 11**: si alguna vez existe un mundo de direccion
> de equipos, **esta mitad tiene ahi su casa**, y la fusion de hoy no deberia
> borrarla sino marcarla.

> **200: las perdidas, y son dos por lado.** De `hoja_de_ruta_de_ventas` viajan
> **cuantos-yeses** (cuantas personas tienen que decir que si) y **el
> plan-post-venta** (los pasos que quedan tras el si verbal). De
> `refinar_sales_roadmap` viajan **peligros-RFP** (detectar RFPs y negativas a
> comprar de startups) y **validar-en-cuentas** (que el roadmap se repita con
> exito en varias). **Ninguno de los dos es superconjunto.**

> **Los pares de familia declarada de esta tanda llevan direccion PROVISIONAL DE
> PAR**, por la doctrina del banco 9.3: el **200** es de la familia del sales
> roadmap, el **206** del racimo censado de Customer discovery y el **207** del
> racimo nuevo de la estrategia de innovacion.

### TANDA R6, SEGUNDA CIEGA: seis de seis, y una corrige al encargo

**Seis puestos mas adjudicados con las razones tapadas, SEIS DE SEIS al
destapar.** Acumulado: **36 de 36**, de los cuales **12 a ciegas**.

| puesto | el par | que se pierde, o que nota deja |
|---:|---|---|
| **213** | `build_measure_learn` contra `ciclo_crear_medir_aprender` | viajan **la inversion de Ries** (*partir del final del ciclo*) y el **innovation accounting** del segundo; y **el anclaje a los Canvas** del primero, su paso 0 |
| **214** | `channels_hypothesis_physical` contra `hipotesis_de_canales` | **familia del canal**: direccion **provisional de par**, y trae dos datos nuevos, abajo |
| **217** | `ecuacion_de_valor` contra `ecuacion_de_valor_cliente` | **choca con el encargo**, abajo |
| **219** | `option_pool_negociacion` contra `pool_opciones_empleados` | viajan **el matiz pre-money** (*valuacion pre-money mas alta como alternativa*) y **verifica-si-incluye-otorgadas** (*si el pool incluye opciones ya otorgadas o solo el no emitido*) |
| **220** | `advances_vs_continuations` contra `objetivos_de_llamada_orientados_a_avance` | **familia declarada**: los dos son miembros del racimo censado del avance y el compromiso, que suma par |
| **221** | `compromiso_linea_tiempo_cliente` contra `tacticas_cierre_ventas` | **NOTA DE FRONTERA**, abajo |

#### CHOCA CON EL ENCARGO, y a favor: la ecuacion de valor YA es PURA

**El encargo dice que la ecuacion de valor va dos de tres y que si el tercer par
sale A se declara pura. Verificado en el archivo: el tercer par YA ESTA LEIDO Y
YA ES A.**

| par | puesto | clase |
|---|---:|:---:|
| `ecuacion_de_valor_cliente` contra `ecuacion_de_valor_venta` | **185** | **A** |
| `ecuacion_de_valor` contra `ecuacion_de_valor_cliente` | **217** | **A** |
| `ecuacion_de_valor` contra `ecuacion_de_valor_venta` | **258** | **A** |

> **Tres miembros, tres pares posibles, LOS TRES LEIDOS, LOS TRES A, CERO
> pendientes.** Cumple la condicion dura **hoy**, no cuando llegue un tercer par.
>
> **Sube a racimo nuevo y se declara SEGUNDO PURO** en el banco 9.5. **Los tres
> son de `core` y los tres de *SPIN Selling*.**
>
> **Y su forma es SUELTO**: cero aristas internas entre los tres. **Tres nodos que
> dicen lo mismo y el grafo no conoce a ninguno de los otros dos.**

#### 214: la familia del canal crece a SEIS, y la evidencia va a favor de la jerarquia

**Dos datos nuevos, los dos verificados:**

> **1. `channels_hypothesis_physical` es un SEXTO miembro** que no estaba en la
> seccion 10, donde la familia se declaro con cinco. **Los seis son de `core` y
> los seis de Blank**, con `validar_canal_distribucion` en la grafia *Blank,
> Steve*.
>
> **2. Y la familia ya tiene CUATRO veredictos A** (puestos 165, 214, 400 y 537)
> **de quince pares posibles, con cuatro pendientes en la cola** (609, 762, 945 y
> 1488).

> **LA EVIDENCIA DE ESTA TANDA VA A FAVOR DE LA JERARQUIA, no de la mega-fusion.**
> El par del 214 enfrenta **la hipotesis de canal FISICO contra la hipotesis de
> canal GENERAL**, y repite. **Es el mismo reparto que el 537 con el digital y que
> el 165 con el fisico de la otra rama.**
>
> **Tres especializaciones distintas repitiendo contra el mismo general es
> exactamente lo que una madre con hijas produce cuando a las hijas no se les ha
> podado lo que la madre ya dice.** **No prueba que sobren: prueba que no se
> podaron.**
>
> **Direccion provisional de par**, por la 9.3.

#### 221: NOTA DE FRONTERA, y limita una fusion antes de que se haga

**`compromiso_linea_tiempo_cliente` y `tacticas_cierre_ventas` repiten**: los dos
mandan poner fecha al piloto, pedir un si o un no explicito al vencer el plazo, no
dejar la decision abierta y documentarla.

> **PERO LOS DOS SON DEL LADO DE WEINBERG DE LA FRONTERA.** `tacticas_cierre_ventas`
> es **el forastero** del racimo del cierre en venta grande, el nodo de *Traction*
> que convive con los siete de Rackham sin contradecirlos.
>
> **LA FUSION DE ESTOS DOS NO DEBE ABSORBER LOS NODOS DE RACKHAM.** El superviviente
> hereda **la doctrina de pedir la decision con fecha**, que es de Weinberg y que
> aplica **cuando el prospecto ya esta calificado**. **Los siete de Rackham dicen
> otra cosa sobre otro momento y su frontera sigue vigente.**
>
> **Fundir a los dos que si cierran es correcto. Dejar que ese superviviente se
> coma a los que no cierran seria borrar la frontera por via de fusion**, que es
> justo lo que la candidata a frontera de la seccion 9 viene a impedir.

---

## 9. RACIMO NUEVO: EL CIERRE EN VENTA GRANDE, el mayor encontrado

**Sube a racimo el 11 ago 2026. Ocho miembros, NUEVE pares ya leidos, y las
lecturas incoherentes entre si segun el hermano: es la firma de familia de la
seccion 1 en su forma mas clara.**

### Los ocho miembros, verificados contra el grafo

**Los ocho de `core`. Y aqui esta el dato que reordena la familia entera:**

| nodo | pasos | fuente |
|---|---:|---|
| `riesgo_tecnicas_cierre_venta_compleja` | 4 | *SPIN Selling* (Rackham) |
| `cierre_segun_complejidad_venta` | 5 | *SPIN Selling* (Rackham) |
| `ineficacia_cierre_ventas_grandes` | 4 | *SPIN Selling* (Rackham) |
| `cierre_satisfaccion_postventa` | 4 | *SPIN Selling* (Rackham) |
| `cierre_sofisticacion_comprador` | 4 | *SPIN Selling* (Rackham) |
| `obtencion_compromiso` | 4 | *SPIN Selling* (Rackham) |
| `obtencion_de_compromiso` | 5 | *SPIN Selling* (Rackham) |
| **`tacticas_cierre_ventas`** | 4 | **_Traction_ (Weinberg)** |

> **SIETE DE OCHO SON DEL MISMO LIBRO. EL OCTAVO ES DE OTRO.** Y eso **no es un
> detalle de procedencia: explica la incoherencia que motivo el racimo.**

### Los nueve pares leidos, y lo que dicen juntos

| puesto | el par | clase |
|---:|---|:---:|
| 274 | `cierre_segun_complejidad_venta` contra `riesgo_tecnicas` | **A** |
| 321 | `ineficacia_cierre_ventas_grandes` contra `riesgo_tecnicas` | **A** |
| 432 | `cierre_sofisticacion_comprador` contra `riesgo_tecnicas` | **A** |
| 463 | `obtencion_compromiso` contra `obtencion_de_compromiso` | **A** |
| 337 | `cierre_satisfaccion_postventa` contra `riesgo_tecnicas` | **B** |
| 527 | `obtencion_compromiso` contra `riesgo_tecnicas` | **B** |
| 499 | `ineficacia_cierre_ventas_grandes` contra `obtencion_compromiso` | **D** |
| **408** | `obtencion_compromiso` contra **`tacticas_cierre_ventas`** | **D** |
| **504** | `obtencion_de_compromiso` contra **`tacticas_cierre_ventas`** | **D** |

> **DOS DE LOS TRES VEREDICTOS D SON CONTRA EL NODO DE WEINBERG**, y el tercero
> (499) enfrenta las dos mitades entre si. **Ningun par de Rackham contra Rackham
> dentro de la misma mitad salio D.**

### LA LECTURA, y no es "ocho nodos incoherentes"

**Medido, el racimo se ordena en TRES piezas y no en una:**

| pieza | miembros | de que trata |
|---|---:|---|
| **A. las tecnicas de cierre no funcionan en venta grande** | **5** | `riesgo_tecnicas` de centro, con `cierre_segun_complejidad`, `ineficacia`, `cierre_sofisticacion` y `cierre_satisfaccion` |
| **B. el avance y el compromiso** | **2** | `obtencion_compromiso` y `obtencion_de_compromiso`, ya censados en su propio racimo |
| **C. el forastero** | **1** | **`tacticas_cierre_ventas`**, de Weinberg, sobre pedir la decision a un prospecto ya calificado |

> **La pieza A repite hacia dentro** (tres A contra el mismo centro). **La pieza B
> repite hacia dentro** (una A). **Y las dos piezas contra el forastero dan D las
> dos veces**, porque el forastero **no dice lo que Rackham dice**: no sostiene
> que el cierre dane la venta grande, sino que **la decision hay que pedirla con
> fecha y por escrito cuando el prospecto ya esta calificado**.
>
> **Las lecturas nunca fueron incoherentes: median cosas distintas y yo no lo
> habia separado.** La incoherencia era mia por tratar como una familia lo que
> son dos mitades de un libro **mas un nodo de otro libro que legitimamente
> discrepa.**

### La forma en el grafo

| | |
|---|---|
| aristas internas | **2**: `cierre_segun_complejidad` con `tacticas_cierre_ventas`, y `cierre_satisfaccion` con `cierre_sofisticacion` |
| aislados | **4**: `ineficacia`, `riesgo_tecnicas`, `obtencion_compromiso`, `obtencion_de_compromiso` |
| **forma** | **MIXTO**, y muy flojo: **grado maximo 1** |

> **El centro doctrinal de la pieza A, `riesgo_tecnicas_cierre_venta_compleja`,
> es uno de los cuatro AISLADOS.** El nodo con el que tres hermanos repiten **no
> esta enlazado con ninguno de ellos.** No hay centro sano que preservar: **aqui
> el grafo no ayuda nada.**

### LA REGLA OPERATIVA, registrada

> **LA FAMILIA SE LEE ENTERA EN LA RELECTURA.** No se decide pieza por pieza ni
> par por par.
>
> **Y los pares que queden de esta familia en la cola del cribado llevan razon
> `familia declarada` y NO pelean la clase.** Quedan **cuatro** por leer, en los
> puestos **601, 971, 1280 y 1333**. Emitir un veredicto propio para cada uno
> **anadiria ruido a una decision que ya esta tomada en otro sitio**: seguir
> discutiendo la clase de un par cuya familia ya subio a mesa es trabajo que se
> tira.
>
> **Lo que si se anota de esos cuatro** es cualquier cosa **nueva** que aparezca
> al abrirlos, un nodo que no estuviera en los ocho o un choque con esta lectura.

### EL FORASTERO: CANDIDATA A FRONTERA DE DOCTRINA INTRA-NUCLEO

**`tacticas_cierre_ventas`, de *Traction* (Weinberg), no es un duplicado mal
puesto: es una doctrina distinta conviviendo con la de Rackham dentro del mismo
nucleo.** Y eso **no tiene ficha todavia**.

| | **Rackham**, los siete | **Weinberg**, el forastero |
|---|---|---|
| **la tesis** | las tecnicas de cierre **danan** la venta grande | la decision **hay que pedirla**, con fecha y por escrito |
| **cuando** | durante toda la venta compleja | cuando el prospecto **ya esta calificado** y en la etapa final |
| **que prohibe** | presionar, cerrar de forma asumida o alternativa | **dejar la decision abierta o ambigua** |

> **LA EVIDENCIA DE QUE CONVIVEN Y NO SE CONTRADICEN SON SUS PROPIOS VEREDICTOS**:
> los dos pares que lo enfrentan a la doctrina de Rackham, los puestos **408 y
> 504**, salieron **D los dos**. **El cribado ya dictamino que no se pisan.**
>
> **Y la frontera es real y es de momento**: Rackham habla de **antes**, cuando el
> cliente todavia no ha articulado su necesidad; Weinberg habla de **despues**,
> cuando ya la articulo y solo falta cerrar la fecha. **Pedir claridad no es
> presionar.**

> **POR QUE ES CANDIDATA A FICHA Y NO SE RESUELVE AQUI**: las fronteras de
> doctrina que esta campana ha visto eran **entre el nucleo y un mundo**. **Esta
> es INTRA-NUCLEO**, dos libros dentro de `core` que dicen cosas distintas sobre
> el mismo momento de venta, **y el lector no tiene como saber cual le toca.**
>
> **El riesgo no es la duplicacion: es la contradiccion aparente.** Un lector que
> caiga en los dos sin el matiz del momento **lee que no hay que cerrar y que hay
> que cerrar.** **Eso pide una linea de frontera escrita, no una fusion.**

> **Y LA FRONTERA YA TIENE QUE DEFENDERSE DE UNA FUSION, antes de estar escrita
> (puesto 221, relectura R6).** `tacticas_cierre_ventas` **repite con
> `compromiso_linea_tiempo_cliente`**, y los dos son del lado de Weinberg: poner
> fecha al piloto, pedir un si o un no al vencer el plazo, documentarlo.
>
> **Esa fusion es correcta y hay que acotarla en el mismo acto**: el superviviente
> hereda **la doctrina de pedir la decision con fecha**, y **NO absorbe a los siete
> de Rackham.** **Borrar la frontera por via de fusion es la forma en que una
> frontera no escrita se pierde**: nadie decide quitarla, simplemente un nodo
> crece y se la traga.


---

## 10. RACIMO NUEVO: LA SELECCION DE CANAL, y choca con la relectura R1

**Sube a racimo el 11 ago 2026, en el puesto 537, y lo hace CHOCANDO con una
direccion de fusion que la relectura R1 acababa de fijar. Por eso se registra
aqui y no en una razon de veredicto.**

### Los cinco miembros, verificados contra el grafo

**Los cinco de `core` y los cinco del mismo libro**, *The Startup Owner's Manual*
de Blank:

| nodo | pasos | de que trata |
|---|---:|---|
| **`seleccion_canal_distribucion`** | 5 | el canal **en general** |
| `seleccion_canal_fisico` | 4 | el canal **fisico** |
| `channels_hypothesis_web_mobile` | 5 | el canal **digital** |
| `hipotesis_de_canales` | 5 | la hipotesis de canal del lienzo |
| **`channels_hypothesis_physical`** | 5 | **la hipotesis de canal FISICO** |
| `validar_canal_distribucion` | 6 | validar el canal elegido |

> **CORRECCION DEL 11 ago 2026, de la relectura R6 (puesto 214): son SEIS y no
> cinco.** `channels_hypothesis_physical` no estaba en esta lista cuando se
> declaro el racimo. **La familia tiene ahora CUATRO veredictos A de quince pares
> posibles, con cuatro pendientes en la cola**, los puestos 609, 762, 945 y 1488.

> **DETALLE DE CAMPO, ya conocido y aqui otra vez**: cuatro declaran *Steve
> Blank* y `validar_canal_distribucion` declara *Blank, Steve*. **La misma obra en
> dos grafias**, que es el defecto medido en la ficha `campos-sucios-dataset`.

### Tres veredictos A ya emitidos

| puesto | el par | clase |
|---:|---|:---:|
| **165** | `seleccion_canal_distribucion` contra `seleccion_canal_fisico` | **A** |
| **400** | `hipotesis_de_canales` contra `seleccion_canal_distribucion` | **A** |
| **537** | `channels_hypothesis_web_mobile` contra `seleccion_canal_distribucion` | **A** |

**Los tres contra el mismo nodo general.** Es el patron del centro doctrinal:
`seleccion_canal_distribucion` **repite con todos sus hermanos**.

### EL CHOQUE, dicho entero

**La relectura R1 declaro, y verificado paso por paso sigue siendo cierto**, que
`seleccion_canal_distribucion` es **superconjunto** de `seleccion_canal_fisico` y
por tanto **su superviviente natural**.

> **Eso vale PARA ESE PAR. No vale para la familia.**
>
> **La tercera pregunta de la relectura, que se pierde al fusionar, cambia de
> respuesta al mirar los cinco.** Contra `seleccion_canal_fisico` se perdia **una
> concrecion**, el ejemplo de canal fisico. **Contra los cinco se pierden DOS
> ESPECIALIZACIONES ENTERAS**, la fisica y la digital, que el nodo general **no
> lleva y no puede llevar sin dejar de ser general.**
>
> **Fusionar los cinco en el general dejaria al catalogo con un solo nodo de canal
> que no sabe si el producto se vende en una tienda o en una tienda de
> aplicaciones.** Y ese es justo el reparto que el catalogo hace bien en otros
> sitios.

### LA REGLA QUE ESTE CHOQUE DEJA, y es de metodo

> **UNA DIRECCION DE FUSION DECIDIDA SOBRE UN PAR NO SOBREVIVE A SU FAMILIA.**
>
> **La relectura tiene que preguntar, antes de fijar superviviente, si el par
> pertenece a una familia declarada o declarable.** Si pertenece, **la direccion
> se decide con la familia entera delante**, porque el superconjunto de dos puede
> ser el empobrecedor de cinco.
>
> **Esto NO invalida la tanda R1**: cinco de sus seis pares no tienen familia
> conocida, y el sexto, el 165, sostiene su veredicto de A. **Lo que se corrige es
> el alcance de su nota de direccion, no la lectura.**

### CANDIDATURA DE FORMA: JERARQUIA MADRE-HIJAS CON ARISTAS

**Alternativa a la mega-fusion, y se registra como candidata porque se decide al
leer la familia entera, no ahora.**

| | la mega-fusion | **la jerarquia madre-hijas** |
|---|---|---|
| **que hace** | funde los cinco en `seleccion_canal_distribucion` | **conserva el general como MADRE y las especializaciones como HIJAS, enlazadas** |
| **que gana** | un solo nodo, cero repeticion | el metodo general **una sola vez**, y cada canal con lo suyo |
| **que pierde** | **el canal fisico y el digital como casos propios** | nada de contenido; **exige podar de las hijas lo que la madre ya dice** |

> **Es la forma que el catalogo ya usa bien en otros sitios**: es exactamente lo
> que hace `value_proposition_canvas` con sus tres piezas, y
> `patron_free_business_model` con `patron_freemium` y `patron_bait_hook`. **Las
> dos son MADRES SANAS medidas en este informe.**
>
> **Y el trabajo que exige esta medido**: hoy la familia tiene **DOS aristas
> internas** y ninguna sale del nodo general. **Para que la jerarquia exista hay
> que crear las aristas que faltan**, que es barato, **y podar de cada hija los
> pasos que repiten a la madre**, que es donde esta el trabajo de verdad.

> **LO QUE DECIDE ENTRE LAS DOS, y no lo decido yo**: si el canal fisico y el
> digital **cambian el procedimiento** o solo lo ilustran. Si lo cambian, hijas.
> **Si solo lo ilustran, la madre se los come como ejemplos y la fusion gana.**

**Los pares que queden de esta familia en la cola llevan razon `familia
declarada`**, igual que la del cierre en venta grande.

---

## 11. CANDIDATO a racimo: LA SUPERVISION DE LA IA

**CANDIDATO, no censo.** Se registra aqui para que la relectura lo encuentre
hecho; **no sube a racimo hasta que un tercer par lo confirme o lo desmienta.**

### Los cuatro nodos, verificados contra el grafo

**Los cuatro de `core` y los cuatro del mismo libro**, *Co-Intelligence* de
Mollick:

| nodo | pasos |
|---|---:|
| `human_in_the_loop_ia` | 4 |
| `principio_humano_en_el_loop` | 4 |
| `comprension_capacidades_limitaciones_ia` | 5 |
| `jagged_frontier_ia` | 4 |

### La evidencia: dos pares, los dos A, y los dos SOSTENIDOS en relectura

| puesto | el par | clase | relectura |
|---:|---|:---:|:---:|
| **166** | `human_in_the_loop_ia` contra `principio_humano_en_el_loop` | **A** | **sostenida en R1** |
| **177** | `comprension_capacidades_limitaciones_ia` contra `jagged_frontier_ia` | **A** | **sostenida en R2** |

> **Dos parejas independientes, las dos repiten, y las dos aguantan la relectura.**
> Lo que las une es el asunto: **donde termina lo que la IA hace sola y donde
> empieza lo que tiene que mirar una persona.**

### La forma: SUELTO, cero aristas

> **Ninguno de los cuatro enlaza con ninguno de los otros tres.** Es la forma peor
> del barrido de la seccion 6, y aqui con un agravante: **son cuatro nodos del
> mismo libro sobre el mismo asunto y el grafo no los conoce.**

> **POR QUE QUEDA EN CANDIDATO Y NO SUBE**: los dos pares leidos son **disjuntos**,
> `human_in_the_loop` con `principio_humano` por un lado y `comprension` con
> `jagged_frontier` por otro. **Nadie ha leido todavia un par CRUZADO entre las
> dos mitades**, y sin eso no esta probado que sean una familia y no dos parejas
> vecinas. **La cola decidira: cuando traiga un par cruzado, sube o se parte.**

---

## 12. MEDICION: LA SERIE DE COLEMAN, candidata a TERCERA SERIE DECLARADA

**Medicion, no adjudicacion.** La DECISION 1 de la mesa, aprobada el 9 ago 2026,
resuelve los programas desmontados en piezas con el tratamiento **SERIE
DECLARADA**: *un nodo-programa unico que presenta la serie entera, un nodo por
paso colgando de el, y el numero en el titulo pasa a ser legitimo porque el
nodo-programa lo explica.*

**Esta es la candidatura de las ocho fases de Coleman a ese mismo tratamiento.
Todas las cifras recontadas del grafo, sobre nodos VIVOS.**

### La poblacion

| | |
|---|---:|
| nodos vivos que declaran *Never Lose a Customer Again* | **83** |
| de esos, **nodos de FASE** (llevan una de las ocho en id o titulo) | **16** |
| **nodos-PROGRAMA** (presentan la serie entera) | **2** |
| nodos de CANAL (la sub-serie de los seis medios de comunicacion) | **4** |

### Las ocho fases, una por una

| fase | nodos vivos | cuales |
|---|---:|---|
| **Assess** | **3** | `fase_assess`, `fase_assess_ciclo_cliente`, `fase_assess_experiencia_cliente` |
| **Admit** | **2** | `fase_admit`, `fase_admit_celebracion` |
| Affirm | **1** | `fase_affirm_buyers_remorse` |
| **Activate** | **2** | `fase_activate`, `fase_activate_primera_impresion` |
| **Acclimate** | **3** | `fase_acclimate`, `fase_acclimate_experiencia_cliente`, `fase_acclimate_mapa_de_proceso` |
| **Accomplish** | **2** | `fase_accomplish`, `fase_accomplish_experiencia_cliente` |
| **Adopt** | **2** | `fase_adopt`, `fase_adopt_ciclo_cliente` |
| Advocate | **1** | `advocacy_customer_journey` |

> **SEIS DE LAS OCHO FASES ESTAN DOBLADAS O TRIPLICADAS.** Solo Affirm y Advocate
> tienen un nodo. **Dieciseis nodos para ocho pasos.**

### TRES HALLAZGOS QUE LA MEDICION DESTAPA

> **1. LA SERIE YA TIENE DOS NODOS-PROGRAMA, y la DECISION 1 pide UNO.**
> `fases_de_retencion_de_clientes` y `ocho_fases_experiencia_cliente` **presentan
> los dos la serie entera**, y el cribado ya los juzgo: **puesto 326, A REPITE.**
> **El tratamiento de serie declarada empieza aqui, fundiendo los dos programas**,
> porque sin un programa unico las piezas no tienen de donde colgar.

> **2. AFFIRM YA FUE CONSOLIDADA UNA VEZ, y quedan las cicatrices.** Es la unica
> fase con **TRES nodos DEPRECADOS**: `fase_affirm`,
> `fase_affirm_reduccion_incertidumbre` y `fase_affirm_reducir_remordimiento`.
> **Alguien hizo con Affirm exactamente lo que esta candidatura propone para las
> otras siete**, y por eso Affirm es hoy la fase mas limpia. **El precedente
> existe y funciono.**

> **3. HAY UNA SEGUNDA SERIE CRUZADA, la de los SEIS MEDIOS DE COMUNICACION**:
> `seis_medios_comunicacion_cliente` es su programa, y cuelgan de el
> `seis_canales_comunicacion_assess`, `seis_herramientas_comunicacion_fase_activate`
> y `seis_herramientas_comunicacion_celebracion`. **Es una serie de canales
> instanciada POR FASE**, o sea **una serie dentro de otra**. **El tratamiento de
> la de fases tiene que decidir que hace con esta antes de tocarla**, o multiplica
> el problema en vez de resolverlo.

### La evidencia del cribado

**Dieciseis pares de Coleman ya leidos**: **doce A**, **tres B** y **una D**.

| dentro de la MISMA fase | puestos | clase |
|---|---|:---:|
| Activate | 183 | **A** |
| Admit | 421 | **A** |
| Assess | 373 | **A**, y 224 **B** |
| Acclimate | 447 | **A**, y 196 y 253 **B** |

> **Ninguna comparacion dentro de una fase salio D.** Las tres B son las tres de
> Assess y Acclimate contra el nodo base de su fase, que es justo la duda que el
> tratamiento resuelve: **si el nodo base es el programa de esa fase, no repite:
> preside.**

### LA CANDIDATURA, sin adjudicar

> **La serie de Coleman cumple los tres requisitos que la DECISION 1 pide:** es un
> **programa desmontado en piezas**, las piezas **llevan el nombre del paso en el
> id**, y **el numero de la serie es real** (son ocho fases y hay nodos para las
> ocho).
>
> **Y trae dos cosas que las dos series ya declaradas no tenian**: **dos programas
> en vez de uno**, y **una serie anidada dentro**. **Las dos hay que resolverlas
> antes, no despues.**
>
> **NO SE ADJUDICA AQUI.** Esta tabla es la candidatura; la decision es de la mesa.

### LA FORMA DEL TRATAMIENTO, preparada y sin adjudicar

**El marco lo da la DECISION 1 de la mesa. Lo que sigue es el ORDEN que la
medicion obliga, no una decision nueva.**

| paso | que se hace | por que va en ese lugar |
|---:|---|---|
| **1** | **fundir los DOS nodos-programa en uno** (el par del puesto **326**, ya juzgado A) | **sin programa unico las piezas no tienen de donde colgar**, y la DECISION 1 pide uno |
| **2** | **resolver la serie de los SEIS MEDIOS de comunicacion** | esta **instanciada por fase**, o sea que es **una serie dentro de otra**: tocarla despues obliga a rehacer lo de las fases |
| **3** | **consolidar fase por fase**, con **Affirm de patron** | **Affirm ya se hizo**, y sus **tres nodos deprecados** son la prueba de que el procedimiento funciona y de como quedo el resultado |
| **4** | **el nodo base de cada fase PRESIDE, no repite** | resuelve las **tres B** de Assess y Acclimate: no eran duda de clase, **eran duda de jerarquia** |

> **EL PASO 4 ES EL QUE CAMBIA VEREDICTOS YA ESCRITOS, y por eso se declara
> aqui.** Las tres B del cribado (puestos **196**, **224** y **253**) enfrentaban
> el nodo base de una fase contra un hermano suyo, y quedaron en duda **porque no
> habia forma de decidir si el base repetia o mandaba.**
>
> **Con el tratamiento declarado, el base MANDA**, y esas tres dejan de ser duda
> sin necesidad de releerlas: **la jerarquia las contesta.**
>
> **NO SE TOCAN AHORA.** Se contestan **cuando la mesa apruebe el tratamiento**, y
> no antes: cambiar tres veredictos por una forma que todavia no esta aprobada
> seria adjudicar por adelantado.

