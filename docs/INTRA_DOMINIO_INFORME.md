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

> **LO QUE ESTE RACIMO PIDE, nombrado el 12 ago 2026 desde la relectura R11: un
> PROGRAMA UNICO**, la misma figura que la serie de Coleman. **Una sola decision
> de cuantos nodos quiere el catalogo para las puertas, y despues una redaccion
> que la ejecute entera.** Los tres A de este racimo **no son tres encargos**: son
> sintomas de un encargo solo. **Si se ejecutan por separado, el segundo redacta
> sobre lo que el primero acaba de mover.**

### Racimo nuevo C: LA APERTURA DE CUSTOMER VALIDATION (3 nodos)

| nodo | pasos | fuente declarada |
|---|---:|---|
| `customer_validation` | 5 | *The Startup Owner's Manual - Steve Blank* |
| `filosofia_validacion_clientes` | 4 | *The Startup Owner's Manual - **Blank, Steve*** |
| `introduccion_validacion_clientes` | 5 | *The Startup Owner's Manual - Steve Blank* |

**Pares ya leidos**: puestos **332** y **349**, **los dos marcados D**, sanos.

> **ACTUALIZADO EL 12 ago 2026: este racimo esta CERRADO y es un MEZCLADO
> COMPLETO.** Sus **tres** pares posibles estan leidos, **cero pendientes**, con
> clases **D, D y A**: el tercero es el puesto **709**, `customer_validation`
> contra `introduccion_validacion_clientes`, en **A**.
>
> **Lo estaba desde el 709 y nadie lo habia declarado.** Salio al contar el jsonl
> para corregir una cifra puesta de memoria en el puesto 781. **Registrado como
> CUARTO MEZCLADO COMPLETO en el banco 9.5.**

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

> **CORRECCION DEL 13 ago 2026, y cae casi toda esta tabla.** Estos cinco
> candidatos se declararon **midiendo la forma**, cero aristas dentro del racimo,
> **sin leer ni uno de los pares**. Leidos por encargo, **los NUEVE gemelos de
> esta tabla y el del racimo de cohortes CAEN**: ninguno repite a su centro. Ver
> **seccion 33**.
>
> **`desarrollo_value_proposition_usp` es el caso mas claro de por que**: no solo
> no repite al centro, **es de otro dominio**, `franquicias`. La medicion de
> aristas no lo podia ver y una sola lectura lo resuelve.

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

### REGLA DE METODO: LA NOMINA QUE CRECE RE-MIDE SU FORMA

**Anadida el 12 ago 2026, y sale del defecto de origen que destapo la remedicion
de la seccion 14.**

> **La forma de un racimo se mide sobre su nomina. Si la nomina cambia, la forma
> medida caduca.** Un racimo declarado con cuatro miembros y medido con seis **no
> da la misma forma**, no da los mismos aislados y no da el mismo centro.

**LOS DOS EJEMPLARES, y los dos son de esta misma casa:**

| racimo | se declaro con | resulto tener | que cambio al re-medir |
|---|---:|---:|---|
| **el reparto de equity** (puesto 246) | **4** | **6** | de forma supuesta a **CENTRO ENLAZADO sin ningun aislado**, o sea la unica de las remedidas **sin gemelo que resolver** |
| **el lienzo de propuesta de valor** (puesto 360) | **3** | **7** | de tres nodos a **CENTRO ENLAZADO con DOS gemelos sin casa** |

> **En los dos casos los miembros que faltaban aparecieron DESPUES, en veredictos
> posteriores, y nadie volvio a la declaracion a sumarlos.** No es que se midiera
> mal: es que se midio bien **una nomina que despues crecio y nadie volvio.**

**LO QUE LA REGLA OBLIGA, y son tres movimientos baratos:**

> **1. Todo veredicto que suma un miembro a un racimo ya declarado lo dice en su
> razon**, con el nombre del racimo. Sin eso el crecimiento no deja rastro.
>
> **2. Antes de usar la forma de un racimo para cualquier cosa, se RE-CUENTA la
> nomina.** La forma vieja no se hereda: se vuelve a medir.
>
> **3. La forma medida se guarda SIEMPRE con el tamano de nomina con el que se
> midio.** Una forma sin su n al lado **no se puede saber si esta vigente**, y una
> forma que no se sabe si esta vigente **es peor que no tenerla**, porque se usa
> igual.

---


## 7. RACIMO NUEVO: LAS METRICAS DE COHORTE

**Sube a racimo el 11 ago 2026 por la firma que este informe ya tiene descrita:
el mismo nodo sale de tres maneras distintas segun con que hermano se compare.**

### Los tres pares que lo obligan

| puesto | el par | clase | por que |
|---:|---|:---:|---|
| **353** | `metricas_cohortes` contra `analisis_de_cohortes` | **A** | mismo instrumento, mismo uso |
| **478** | `metricas_cohortes` contra `metricas_accionables` | **D** | hijo con casa propia **CON arista**: jerarquia sana |
| **522** | `metricas_cohortes` contra `retention_metrics` | **D** | **CORREGIDO el 13 ago 2026**: decia A; la ratificacion lo volteo a D y esta tabla no se barrio. Ver seccion 30.1 |

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
> **ADJUDICADO el 13 ago 2026: esta candidatura CAE.** `retention_metrics` pasa de
> **gemelo sin casa** a **MIEMBRO SIN ARISTA**, y su arreglo es la arista que
> falta del banco 9.6, no una fusion. **Ver seccion 31.** Lo que sigue queda como
> historia de lo que se penso antes de la adjudicacion.
>
> **La marca original**: esta candidatura
> **descansaba en el puesto 522 en A**, y el 522 **es D** desde la ratificacion.
> **Sin esa A, `retention_metrics` no es gemelo de nadie en esta familia**: lo que
> le queda es un **B** (233) y un **D** (522). **La figura puede seguir siendo
> util por la forma** (un nodo sin ninguna arista al centro) **pero ya no por el
> contenido**, y quien decida eso no soy yo. **Ver seccion 30.1.**
>
> **Con esto son SEIS los candidatos a esa figura**, los cinco de la tabla de la
> seccion 6 mas este.

### Lo que esto le hace al arreglo

> **La familia no se desmonta.** Cuatro de los cinco cuelgan de un centro que los
> enlaza, y esa parte esta sana. **Lo que hay que resolver son dos cosas y no
> cinco:**
>
> 1. **`retention_metrics`**, que es la primera **COSTURA FUERA DE COLA** de la
>    ficha de costuras: **lleva dos temas pegados** y su cirugia es partirlo.
>    **Partirlo puede resolver de paso lo que quede pendiente con el racimo**,
>    porque su mitad de retencion es lo que se solapa y la de adquisicion no.
>    **CORREGIDO el 13 ago 2026**: este texto lo llamaba *el gemelo*, y no lo es;
>    esa palabra venia del puesto 522 en A, **que la ratificacion volteo a D**.
>    **La cirugia no cambia; el motivo si.** Ver seccion 30.1.
> 2. **El par del puesto 353**, `metricas_cohortes` contra `analisis_de_cohortes`,
>    que repite y **cuelga del mismo centro**: ahi si hay fusion que hacer.
>
> **Las dos decisiones son de nodo, no de familia. El centro se queda como esta.**

> **CONFIRMADO A CIEGAS el 13 ago 2026, relectura R19.** La segunda de las dos
> decisiones, el par del puesto 353, **volvio a leerse sin mirar el veredicto y
> volvio a salir A.** Es el pilar del arreglo: **si se cayera, el centro
> `metricas_accionables` se quedaria con dos hijos que repiten entre si** y esto
> dejaria de ser un problema de dos nodos para volver a ser uno de cinco.

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

#### FIGURA NUEVA (13 ago 2026): LA FRONTERA INTRA-LIBRO

**Hasta hoy todas las fronteras registradas eran ENTRE LIBROS**: Rackham contra
Weinberg en el cierre, Blank contra Ries en el pivote. **El puesto 877 trae la
primera de un libro consigo mismo.**

| nodo | que manda para el MISMO caso, cofundar con amigos o familia |
|---|---|
| `cofundar_con_amigos_familia_riesgos` | **estructuras de autoridad CLARAS aunque resulten socialmente incomodas** |
| `relacion_previa_y_estructura_roles` | **estructura de decision mas COLEGIADA E IGUALITARIA** |

**Los dos son de *The Founder's Dilemmas*.**

> **No es duplicacion y no es error del catalogo: es que el libro dice las dos
> cosas**, una desde el riesgo de la relacion y otra desde el diseno de roles.
> **Y no es un empate que se resuelva fusionando**, porque fundir deja al lector
> con una sola de las dos y sin saber que la otra existia.

> **LO QUE LA FIGURA OBLIGA**: escribir la frontera **dentro de los dos nodos**,
> nombrando la condicion que decide. **Una frontera intra-libro es mas peligrosa
> que una entre libros**, porque el lector no tiene la senal de *son autores
> distintos* para sospechar que hay dos escuelas. **Parece contradiccion y es
> matiz, y solo el texto puede decirlo.**

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

### TANDA R7, TERCERA CIEGA: seis de seis

**Acumulado: 42 de 42, de los cuales 18 a ciegas.** Perdidas verificadas contra el
grafo.

| puesto | el par | que se pierde si no viaja |
|---:|---|---|
| **222** | `obtencion_compromiso` contra `obtencion_compromiso_venta` | **mide-por-avances** del primero; **revisa-las-preocupaciones-en-voz-alta** del segundo |
| **227** | `balance_eficiencia_responsividad` contra `trade_off_responsividad_eficiencia` | **el monitoreo de factores** del primero (demanda, precios, tasas de produccion, frecuencia de entregas); **los cinco drivers nombrados** del segundo (produccion, inventario, ubicacion, transporte, informacion) |
| **228** | `determinar_tipo_de_mercado` contra `hipotesis_tipo_mercado` | **la cifra doctrinal de Blank** del segundo, *1,7x o 3x el presupuesto de marketing del lider*; **clonar-de-otro-pais** y **documentar-como-hipotesis** del primero |
| **230** | `etnografia_investigacion_usuario` contra `investigacion_etnografica_ideacion` | **dia-en-la-vida** del segundo; **problemas fisicos, emocionales y contextuales** del primero |
| **232** | `customer_validation_sell_phase` contra `get_out_building_test_sell` | **evita-exclusividades** y **personalizaciones-reales** del segundo; **proceso-de-aprobacion dentro del negocio del cliente** del primero |
| **234** | `brainstorming_efectivo` contra `reglas_brainstorming` | **Silly Cow** y **la inmersion previa** del segundo; **grupos-con-confianza** y **separar-divergencia-de-seleccion** del primero |

> **DIRECCIONES PROVISIONALES DE PAR**, por la 9.3: el **222** es de la familia de
> obtencion de compromiso, que vive dentro del racimo censado del avance; el
> **232** es de la apertura de Customer Validation; y el **234** es del racimo
> censado de las reglas del brainstorming, **que ademas cruza con una decision de
> fuente y por eso tiene entrada propia en la seccion 13.**

> **UNA CIFRA QUE MERECE SU PROPIA LINEA**: el 228 es el unico par de las siete
> tandas donde lo que se pierde es **un numero**. *1,7x o 3x el presupuesto de
> marketing del lider* no se puede reconstruir leyendo el nodo superviviente. Las
> demas perdidas son gestos que otro redactor podria volver a escribir; **esta
> no.**
>
> **CORREGIDO EL MISMO DIA, y la correccion vale mas que la frase.** Aqui escribi
> que la cifra *o viaja o desaparece del catalogo*. **Es falso**: vive tambien en
> `analisis_costo_entrada_mercado`, que es **hijo con casa propia CON arista** del
> mismo nodo y la trae **con mas precision**, con los umbrales del 74, el 41 y el
> 26 por ciento. **Es una PERDIDA DE LECTOR, no de catalogo**, y de ahi salio la
> distincion del banco 9.7.

### TANDA R8, CUARTA CIEGA: seis de seis

**Acumulado: 48 de 48, de los cuales 24 a ciegas.** Perdidas verificadas contra el
grafo **y clasificadas por tipo**, segun la doctrina del banco 9.7 que esta tanda
estrena.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **235** | `estrategia_de_innovacion_y_tecnologia` contra `seleccion_arenas_estrategicas` | **la mecanica de la sesion**: generar doce arenas o mas y priorizar de dos a cuatro; y **declarar que queda FUERA del alcance de busqueda** | de **lector** |
| **236** | `how_might_we_brief_social` contra `how_might_we_briefs` | **el conocimiento-local**: validar el brief con ONGs o actores en terreno antes de prototipar | de **lector** |
| **237** | `desafios_de_diseno_competitivos` contra `diseno_de_desafios_de_innovacion` | **equipos-independientes** (no gubernamentales) e **impacto-en-inversion** del primero; **aprendizaje-colectivo mas alla del ganador** del segundo | de **lector** |
| **241** | `shadow_ai_use_organizacional` contra `shadow_ia_organizacional` | **encuestas-anonimas** del primero; **power-users** (estan en cualquier nivel jerarquico) y **recompensar en vez de amenazar** del segundo | de **lector** |
| **244** | `innovacion_abierta` contra `open_innovation_ideacion` | **sindrome NIH** y **metodos-segun-complejidad** del primero; **Stage-Gate-para-IP** del segundo | de **lector** |
| **245** | `customer_validation_sell_phase` contra `filosofia_customer_validation` | **las tres preguntas de escala** de la filosofia (puede crecer, se repite la venta, se puede pagar la adquisicion) y el **proceso-de-aprobacion** del primero | de **lector** |

> **LAS SEIS SON PERDIDAS DE LECTOR, ninguna de catalogo.** Es la primera tanda
> clasificada con la distincion nueva, y **sale entera del lado barato**: lo que
> se perderia en estas seis fusiones **sigue existiendo en el catalogo por otra
> via o es reconstruible**, asi que **el arreglo es traslado o arista, no rescate
> previo.**

> **DIRECCIONES PROVISIONALES DE PAR**, por la 9.3: el **235** es del racimo de
> las arenas y la estrategia de innovacion (seis miembros), el **236** del racimo
> censado del encuadre del problema, y el **245** de la apertura de Customer
> Validation.

#### 244: es tambien el par de INNOVACION ABIERTA de la ficha, y SE SOSTIENE

**El par de los puestos 187 y 233 de la numeracion del gradiente**, registrado en
`docs/FICHA_SUBFUSION_GRADIENTE.md` como **el mas pegado de aquella tanda**: los
dos del nucleo y los dos de *Winning at New Products* (Cooper), con el scouting,
la pagina web, la transferencia universitaria, las sesiones con proveedores y la
co-creacion tipo LEGO **coincidiendo uno a uno**.

> **Tres ejes lo han mirado y los tres coinciden**: el gradiente lo llamo el mas
> pegado, el cribado intra le dio **A** en el puesto 244, y la relectura **a
> ciegas** lo sostiene. **Anotado tambien en la ficha.**

### TANDA R9, QUINTA CIEGA: seis de seis

**Acumulado: 54 de 54, de los cuales 30 a ciegas.** Perdidas verificadas contra el
grafo y clasificadas por tipo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **247** | `customer_validation` contra `filosofia_customer_validation` | **la metrica peso-invertido-peso-devuelto** (si por cada peso en ventas y marketing vuelven dos) y **las tres preguntas de escala** | de **lector** |
| **248** | `framework_spin_selling` contra `modelo_spin_preguntas` | **calificar-rapido-sin-abusar** de las de situacion; **ajusta-al-flujo** sin forzar el orden rigido y **presenta-recien-cuando-articule** la necesidad explicita | de **lector** |
| **249** | `hr_calidad_gestion` contra `hr_como_control_de_calidad_gerencial` | **compensacion-contra-mercado**, **tiempo-a-productivo** de un empleado nuevo, **contratar a un disenador de procesos** y **el giro de HR como control de calidad DE LOS GERENTES** | de **lector** |
| **251** | `regalos_estrategicos_sorpresa` contra `sorprender_cliente_estrategico` | **el 2 a 10 por ciento de utilidades**, **la nota a mano**, **evitar-festivos** y **la familia del cliente** en la investigacion previa | de **lector** |
| **252** | `clasificacion_mercados_cadena_suministro` contra `modelo_cuadrantes_mercado` | **oportunidades-por-cuadrante** y **capacidades-a-reforzar** | de **lector** |
| **255** | `hoja_de_ruta_de_ventas` contra `sales_roadmap` | ya anotadas en los puestos **192** y **200** | de **lector** |

> **Nota del 248, y es de frontera**: esta fusion es **intra-Rackham**, los dos
> nodos son del mismo libro y del mismo lado. **No toca la frontera de momento
> con el forastero de Weinberg**, que sigue vigente.

#### EL TRIO DEL SALES ROADMAP: TERCER PURO, verificado contando el jsonl

| | |
|---|---:|
| miembros | **3**: `sales_roadmap`, `refinar_sales_roadmap`, `hoja_de_ruta_de_ventas` |
| pares posibles | **3** |
| **leidos** | **3**: puestos **192**, **200** y **255** |
| **que repiten** | **3** |
| pendientes | **0** |

> **Cumple la condicion dura. Declarado TERCER PURO en el banco 9.5.** Y ya tiene
> superviviente propuesto de la tanda R4: **`refinar_sales_roadmap`**, seis pasos
> contra tres y cinco, superconjunto claro.
>
> **DETALLE DE CAMPO, otra vez el mismo**: dos de los tres declaran *Blank, Steve*
> y el tercero *Steve Blank*. **La misma obra en dos grafias dentro de un racimo de
> tres nodos.**

#### SANO POR DENTRO, GEMELO POR FUERA: el patron, con ejemplar doble

**Dos de los pares de esta tanda enfrentan nodos que el instrumento de costuras ya
habia leido y declarado FALSOS**, o sea sanos por dentro. **Y aqui salen A**, o
sea gemelos por fuera.

| nodo | el instrumento de costuras dijo | el cribado intra dice |
|---|---|---|
| los dos de **SPIN** del puesto 248 | **falsos**: secuencia legitima, sin repeticion interna | **A**: repiten entre si |
| los dos de **regalos** del puesto 251 | **falsos** | **A**: repiten entre si |

> **UN NODO PUEDE ESTAR LIMPIO POR DENTRO Y TENER UN GEMELO FUERA.** No son
> preguntas que se contesten la una con la otra: **son dos preguntas distintas
> sobre el mismo nodo.**
>
> **Es el ejemplar doble de lo que el informe de cierre declaro como punto ciego,
> visto desde el otro lado**: alli el eje intra tapaba el agujero del de costuras
> (la forma que parte pura). **Aqui el de costuras acierta al decir que estan
> limpios y el intra encuentra lo que el otro no podia ver por diseno.**
>
> **Los dos instrumentos no se corrigen: se completan.** Ninguna de las dos
> lecturas es un error de la otra.

> **La familia de los regalos queda con tres nodos y dos relaciones distintas**:
> `regalos_estrategicos_sorpresa` y `sorprender_cliente_estrategico` **repiten**
> (puesto 251), y `shock_and_awe_kit_bienvenida` es **sano frente al primero**
> (puesto 564), **porque se contradicen sobre la marca**: uno manda regalar **sin
> logos** y el otro **con identidad de marca**. **La contradiccion es lo que lo
> salva.**

### TANDA R10, SEXTA CIEGA: seis de seis

**Acumulado: 60 de 60, de los cuales 36 a ciegas.** Perdidas verificadas contra el
grafo y clasificadas por tipo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **256** | `founder_ceo_succession_process` contra `identificacion_necesidad_sucesion_ceo` | **deja-que-quien-dirige-opere**: el proceso de dejar operar a quien dirige, identificar los problemas y trabajar junto a esa persona | de **lector** |
| **257** | `estrategia_competencia_vcs` contra `leverage_en_negociacion_con_vcs` | **no-reveles** con que otros inversores hablas salvo que sean colaboradores conocidos; **ofertas-de-compra-como-palanca**; y **traccion-antes**, producto, ingresos o contratos antes de acercarte | de **lector** |
| **258** | `ecuacion_de_valor` contra `ecuacion_de_valor_venta` | ya anotadas en los puestos **185** y **217** | de **lector** |
| **261** | `formacion_de_habitos_de_pensamiento` contra `gestion_de_habitos_mentales_para_pensar` | **fringe-thoughts**, registrar los pensamientos espontaneos que aparecen fuera del horario, y **rupturas-deliberadas** de rutina cuando el pensamiento se estanca | de **lector** |
| **262** | `customer_appreciation_pr` contra `customer_appreciation_soporte` | **contests** y sorteos de bajo costo y alto valor emocional; y **satisfaccion-sobre-eficiencia** como politica explicita | de **lector** |
| **264** | `how_might_we_framing` contra `how_might_we_hmw` | casi nada: el **ni-amplio-ni-estrecho** esta en los dos. Solo cambia el uso final, **brujula** de todo el proceso contra **titular** de la sesion de brainstorming | de **lector** |

#### 256: TERCER EJEMPLAR de SANO POR DENTRO, GEMELO POR FUERA

**Y es el mas claro de los tres, porque la ficha de costuras dice exactamente por
que lo declaro falso.**

> `founder_ceo_succession_process` esta en la cola de las 128 con bloque **51,5**,
> y se leyo **FALSO** con una razon nombrada: **falso positivo de secuencia
> legitima por pasos tematicamente ESPEJADOS**. Su paso 2 dice *evalua si TUS
> habilidades encajan con la siguiente etapa* y su paso 6 dice *evalua si el
> perfil de QUIEN TE SUCEDERIA encaja con la etapa*. **Espejo, no repeticion.**
>
> **Y aqui sale A**: repite por fuera con `identificacion_necesidad_sucesion_ceo`.
>
> **Los dos instrumentos aciertan.** El de costuras midio si el nodo se repite a
> si mismo y dijo que no, con el motivo escrito; el intra midio si tiene gemelo
> fuera y dijo que si. **Anotado en la ficha junto a los otros dos.**

#### 258: el SEGUNDO PURO se sostiene, y ya con sus tres pares releidos

**El puro de la ecuacion de valor**, del banco 9.5, tiene tres miembros y tres
pares, los puestos **185, 217 y 258**. **Este es el tercero y ultimo**, y la
relectura a ciegas lo sostiene.

> **Un puro cuyos tres pares han pasado por la relectura no vuelve a la mesa: va
> directo al redactor.** Es el unico de los tres puros declarados que tiene
> **todos** sus pares releidos.

#### Cuatro familias que este tanda deja PROVISIONALES

**Ninguna se declara racimo aqui: se anotan con su nombre para que la mesa las
cuente antes de tocarlas.**

| familia | por que queda provisional |
|---|---|
| **la sucesion** | ya medida en el puesto 618: **once nodos vivos**, diez de *The Founder's Dilemmas* y uno forastero. El 256 es un par mas de esa familia |
| **la competencia entre inversores** | `estrategia_competencia_vcs` y `leverage_en_negociacion_con_vcs` son de **libros distintos**, *Venture Deals* y *The Founder's Dilemmas*, y mandan la misma jugada: varios term sheets a la vez |
| **los habitos de pensamiento** | el 261 es **vecino** de la familia de Wallas ya tocada en los puestos 473, 689 y 693: `esfuerzo_y_energia_intelectual` y sus hijos. **Cinco nodos del mismo libro sobre como se trabaja la cabeza** |
| **el HMW** | el 264 se suma a los puestos 236 y 237, ya leidos, sobre encuadre del problema y desafios de diseno |

> **CRUCE ANOTADO, del 262 a la seccion 13**: `customer_appreciation_pr` manda
> notas escritas a mano y regalos pequenos a clientes tempranos, que es
> **exactamente el material de la familia de los regalos** del puesto 251 y del
> 564. **Dos frentes tocan los mismos gestos desde libros distintos**, Weinberg
> por el lado de traccion y Coleman por el de experiencia. Quien redacte uno tiene
> que mirar el otro.

### TANDA R11, SEPTIMA CIEGA: seis de seis

**Acumulado: 66 de 66, de los cuales 42 a ciegas.** Perdidas verificadas contra
el grafo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **265** | `influence_map_organizacional` contra `mapa_de_influencia` | **comprador-economico**, determinar quien es el que finalmente paga; **palanca-entre-grupos**, usar el apoyo de un grupo para convencer al siguiente; y **no-te-saltes-etapas** aunque parezca mas rapido | de **lector** |
| **268** | `pivotar_o_proceder` contra `pivote_o_proceder` | **dibuja-el-flujo-real** del cliente tipico con datos recogidos, para compararlo contra lo que suponias; y **reduce-a-un-parrafo**, dejar la lista de funciones en algo que se cuente en un parrafo y se venda a miles | de **lector** |
| **273** | `analisis_de_variancia` contra `analisis_varianza_financiera` | **favorable-desfavorable**, decidir a mano el signo de cada varianza; **parentesis-contables**, verificar como presenta el sistema los negativos; y **antes-de-tomar-decisiones**, investigar la causa **antes** de decidir nada | de **lector** |
| **274** | `cierre_segun_complejidad_venta` contra `riesgo_tecnicas_cierre_venta_compleja` | la mitad permisiva del primero, que en la venta pequena las tecnicas de cierre **si** se aplican; y **satisfaccion-postventa** como medida de si el cierre esta danando la relacion | de **lector** |
| **275** | `sistema_stage_gate` contra `stage_gate_system` | **logica-de-opciones**, que cada etapa cueste progresivamente mas siguiendo la logica de comprar opciones; **playbook-replicable** como sistema operativo de toda la organizacion; y **agil-context-based**, ajustar el rigor al riesgo y tipo de proyecto | de **lector** |
| **276** | `customer_discovery` contra `customer_discovery_cuatro_fases` | ya anotadas en los puestos **156** y **206** | de **lector** |

#### 274: la fusion es INTRA-RACKHAM y no toca la frontera

**Los dos nodos son de *SPIN Selling*, los dos del racimo del cierre en venta
grande de la seccion 9.**

> **Fusionarlos no mueve la frontera de doctrina de ese racimo**, que es la que
> enfrenta a los siete de Rackham con el forastero `tacticas_cierre_ventas` de
> *Traction*. **Es una poda interna, y de las baratas.** Igual que el 248.

#### 275: los DOS programas del Stage-Gate, y el racimo pide PROGRAMA UNICO

**`sistema_stage_gate` y `stage_gate_system` son los dos nodos que el racimo B de
la seccion 1 describe como el sistema entero, dos veces.**

> **Este par no se arregla solo, y no porque sea dificil sino porque no es un
> par.** El racimo de las puertas tiene **seis miembros y tres pares leidos, los
> tres en A**, y esos tres A son **tres fusiones distintas que no se pueden
> ejecutar a la vez.**
>
> **Lo que este racimo necesita es la misma figura que la serie de Coleman: un
> PROGRAMA UNICO.** No tres podas sucesivas, sino **una sola decision de cuantos
> nodos quiere el catalogo para las puertas** y despues una redaccion que la
> ejecute entera. **Registrado junto a la candidatura del racimo B.**

#### 276: SUB-PURO, figura nueva, y va al banco

**El trio `customer_discovery_overview`, `customer_discovery_cuatro_fases` y
`customer_discovery` tiene sus TRES pares posibles leidos y los tres son A.**

| | |
|---|---:|
| miembros del trio | **3** |
| pares posibles **del trio** | **3** |
| leidos | **3** (puestos 156, 206 y 276) |
| que repiten | **3** |
| pendientes | **0** |

> **Y sin embargo NO es un racimo puro**, porque **el trio no es una familia: es
> un pedazo de una.** La familia censada de customer discovery tiene **siete
> miembros y 21 pares posibles**, de los cuales **11 estan en la cola y 9 leidos**.
>
> **PRECISION QUE HAY QUE HACER Y NO ESTABA EN EL ENCARGO**: uno de los tres del
> trio, `customer_discovery_overview`, **NO esta en esa nomina de siete** (es uno
> de los nueve que el puesto 615 midio fuera). **Asi que el conjunto que de verdad
> contiene al trio son OCHO nodos y 28 pares posibles**, no siete y 21. La cifra
> del encargo es la de la nomina censada; la del grafo es una mas.

**Declarado en el banco 9.5 como figura nueva: EL SUB-PURO.**

> **Lo que compra**: el redactor puede consolidar el trio **mientras la familia se
> sigue leyendo**, sin esperar a la mesa. **Lo que NO compra**: decidir cuantos
> nodos quiere el catalogo para el descubrimiento de clientes, que sigue siendo
> decision de familia.

### TANDA R12, OCTAVA CIEGA: seis de seis

**Acumulado: 72 de 72, de los cuales 48 a ciegas.** Perdidas verificadas contra
el grafo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **277** | `funnel_get_customers_optimizacion` contra `optimizacion_embudo_get_customers` | **data-chief**, revisar a diario las diez o doce metricas clave con esa figura; **escala-el-mas-productivo** primero; y **no-demasiados-a-la-vez** para no confundir resultados. **Todas TRAS el destejido**, ver abajo | de **lector** |
| **278** | `enfoque_etapa_investigacion` contra `etapa_de_investigacion` | **entrena-primero-S-y-P**: entrenar en preguntas de Situacion y Problema antes de pasar a Implicacion y Necesidad-beneficio | de **lector** |
| **280** | `estrategia_de_innovacion_arenas` contra `seleccion_arenas_estrategicas` | ya anotadas en los puestos **207** y **235** | de **lector** |
| **281** | `formacion_de_habitos_de_pensamiento` contra `formacion_de_habitos_de_trabajo_creativo` | casi nada: uno anade el **estimulo sensorial** asociado al habito y el otro **perseverar hasta el segundo aire** | de **lector** |
| **282** | `antigoals_framework` contra `definir_antigoals` | **revisita-periodica** de las cuatro listas conforme el proyecto evoluciona; y **comparte-con-equipo** para que el equipo se agrupe tambien alrededor de lo que NO se hara | de **lector** |
| **284** | `influence_map_organizacional` contra `mapa_organizacional_influencia` | **impacto-en-vida-diaria**, representar como el producto cambia el dia de cada persona del mapa; y **actualiza-el-lienzo** con esos hallazgos | de **lector** |

#### 277: CUARTO NODO DONDE LOS DOS EJES SE CRUZAN, y es el primero al reves

**`optimizacion_embudo_get_customers` es la doble de la TANDA 14 de la ficha de
costuras**, diez pasos, Blank y Weinberg, con la anatomia escrita: **EL TESTEO
DICHO DOS VECES.**

> **Y aqui hay que decir en que se parece a los otros tres y en que NO.**
>
> Los tres anteriores, SPIN (248), regalos (251) y `founder_ceo_succession_process`
> (256), eran **FALSAS** de costuras: **sanos por dentro y gemelos por fuera.**
>
> **Este es CONFIRMADA: averiado por dentro Y gemelo por fuera.** Es la cuarta vez
> que los dos ejes caen sobre el mismo nodo, **y la primera vez que los dos
> encuentran algo.**

**LA CURA ACOPLADA, que es lo que este caso obliga a nombrar:**

> **No se puede destejer primero y fusionar despues, ni al reves.** Si se desteje
> la costura interna, el nodo queda mas corto y el gemelo pasa a cubrir mas de el;
> si se fusiona con el gemelo primero, se fusiona **arrastrando la mitad ajena**
> que la cirugia iba a quitar.
>
> **Destejido y fusion van en el MISMO acto, por el TOQUE UNICO del banco 9.4.**
> Y por eso las perdidas del 277 se anotan **tras el destejido**: lo que hay que
> salvar es lo que sobreviva a las dos operaciones juntas.
>
> **Anotado en las fichas de los dos ejes.**

#### 280: EL TRIO DE LAS ARENAS es SUB-PURO, y la familia es de SEIS

**El encargo ofrecia dos respuestas, tres o cinco. Contado con
`scripts/contar_nombre.py` y el jsonl, la respuesta es OTRA y hay que traerla.**

**EL TRIO, y cumple la condicion dura puertas adentro:**

| | |
|---|---:|
| miembros | **3**: `estrategia_de_innovacion_arenas`, `estrategia_de_innovacion_y_tecnologia`, `seleccion_arenas_estrategicas` |
| pares **posibles del trio** | **3** |
| leidos | **3** (puestos **207**, **235** y **280**) |
| que repiten | **3** |
| pendientes | **0** |

**PERO NO ES UNA FAMILIA CERRADA, y por dos motivos medidos:**

> **1. Uno de los tres ya esta censado en OTRO racimo.**
> `estrategia_de_innovacion_y_tecnologia` es miembro del racimo
> `Estrategia de innovacion de producto` de `RACIMOS_MIEMBROS.jsonl`, junto a
> `estrategia_innovacion_producto` y `estrategia_de_innovacion_de_producto`.
>
> **2. El contador destapa un cuarto nodo de arenas que no estaba en ninguna
> lista**: **`strat_map_arenas_estrategicas`**, con **trece menciones**, y leido es
> el instrumento con el que se eligen las arenas: definir la base actual,
> identificar candidatas, seis a ocho criterios de atractivo y seis a ocho de
> fortaleza, calificar de cero a diez, graficar las burbujas y quedarse con el
> cuadrante superior derecho.

**LA FAMILIA MEDIDA, uniendo las tres listas:**

| | |
|---|---:|
| miembros | **6** |
| pares **posibles** | **15** |
| en la cola intra | **9** |
| **leidos** | **6** |
| **de esos, en A** | **SEIS DE SEIS** (207, 235, 280, 357, 460, 530) |
| pendientes **de la cola** | 3 (puestos 863, 1121, 1290) |
| **pares que NUNCA entraron a la cola** | **6** |

> **Seis pares leidos y los seis repiten.** No hay un solo sano en esta familia.
>
> **Por eso el trio NO se declara puro: se declara SUB-PURO**, como el del puesto
> 276, y por el mismo motivo. **Y la familia de seis se convierte en el mejor
> candidato que hay a COMPLETAR LOS PARES DEL PURO** del banco 9.5: **nueve
> lecturas dirigidas** y esta familia queda cerrada en un sentido o en el otro.
>
> **Si las nueve salen A, son seis nodos que dicen una sola cosa.** Con seis de
> seis ya en A, **es la apuesta mas cargada del inventario.**

**SATELITES ANOTADOS, no miembros**: `desarrollo_attack_plans` desarrolla el paso
de los planes de ataque y `product_roadmap_estrategico` el del roadmap. **No
entran a la cuenta**: el script los trae, la lectura los deja fuera.

#### Las dos familias que el encargo daba en 2 de 3, y estan en 3 de 3

**Las dos se midieron contra el jsonl antes de escribir esto, y las dos estaban
mas adelantadas de lo que el encargo suponia. Lo traigo porque una de ellas es un
PURO y hay que declararlo.**

##### CUARTO PURO: `la etapa de investigacion en la venta`

**Y este no es sub-puro: la nomina es CENSADA y esta cerrada por definicion.**

| | |
|---|---:|
| miembros, de `RACIMOS_MIEMBROS.jsonl` | **3**: `etapa_investigacion_ventas`, `etapa_de_investigacion`, `enfoque_etapa_investigacion` |
| pares **posibles** | **3** |
| **leidos** | **3** (puestos **209**, **278** y **303**) |
| que repiten | **3** |
| pendientes | **0** |

> **El par que el encargo daba por faltar, enfoque contra ventas, es el puesto
> 303 y esta leido desde hace tiempo, en A.** La cuenta salio de contar el
> archivo, no de suponerla.
>
> **Cumple la condicion dura con pares posibles y no con pares de cola**, que es
> la precision del banco 9.5. **Declarado CUARTO PURO.** **CON CONDICION, puesta ocho
> puestos despues por el propio cribado: ver seccion 22.1.**
>
> **DEGRADADO A SUB-PURO EL MISMO DIA, en el puesto 800**: la condicion se
> cumplio, la familia es de CUATRO y le faltan dos pares. **Correccion declarada
> en el banco 9.5 y medida en la seccion 24.1.** Lo que sigue en pie es el trio:
> **puro puertas adentro, sub-puro hacia afuera.** Le falta lo unico que a
> un puro le puede faltar: **un superviviente propuesto**, que aqui no lo da
> ninguna relectura todavia.

##### TERCER MEZCLADO COMPLETO: `los habitos de pensamiento`

| | |
|---|---:|
| miembros | **3**: `formacion_de_habitos_de_pensamiento`, `formacion_de_habitos_de_trabajo_creativo`, `gestion_de_habitos_mentales_para_pensar` |
| pares posibles | **3** |
| **leidos** | **3** (puestos **261**, **281** y **333**) |
| clases | **A, A y D** |
| pendientes | **0** |

> **Los dos nodos de FORMACION del habito repiten entre si y con el de GESTION uno
> repite y el otro no.** El 333 lo dejo escrito: formar el habito, hora fija y
> repeticion durante semanas, no es lo mismo que administrarlo y hasta romperlo a
> proposito.
>
> **Es el tercer mezclado completo del archivo**, con el racimo del control de la
> junta (seccion 14) y la familia del encaje (seccion 15.6). **Y es el mas barato
> de los tres**: dos nodos que se funden y un tercero que se queda, con la arista
> entre ellos como unico trabajo pendiente.

> **LO QUE ESTAS DOS DEJAN COMO AVISO**: el encargo las daba en 2 de 3 y estaban
> en 3 de 3. **Ninguna de las dos cuentas era mia ni del auditor: eran del
> recuerdo.** Es el mismo error que el contador vino a matar, en su otra forma.
> **Antes de decir que a una familia le falta un par, se cuenta el jsonl.**

### TANDA R13, NOVENA CIEGA: seis de seis

**Acumulado: 78 de 78, de los cuales 54 a ciegas.** Perdidas verificadas contra
el grafo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **285** | `producto_unico_superior` contra `superioridad_producto_beneficios` | los **discursos por posicionamiento**, si eliges premium NO enumeres caracteristicas y si eliges precio bajo SI; **desarma-la-competencia**; **imagina-la-evolucion** del producto rival; **necesidades-sin-nombre**, las que el cliente no sabe pedir; y **proveedores-que-innovan** contigo | de **lector** |
| **288** | `arquetipos_de_cliente` contra `customer_archetypes` | **patrones-de-conversaciones**, buscar lo que se repite en las charlas exploratorias; e **hipotesis-provisional**, tratar cada retrato como algo que se revisa al aprender | de **lector** |
| **289** | `assumption_and_constraint_log` contra `assumption_constraint_log` | practicamente nada: **es el mismo formulario con y sin conjuncion en el identificador** | de **lector** |
| **290** | `decision_cuando_fundar` contra `tres_preguntas_carrera` | nada: **calco permutado**, los mismos tres factores en distinto orden y el mismo cierre de reforzar el mas debil | de **lector** |
| **292** | `embudo_get_keep_grow` contra `estrategia_get_keep_grow` | **earned-vs-paid** como tacticas a probar; **CAC-contra-margen** por venta; **adquirir-es-lo-mas-caro** como regla de prioridad; y **actualiza-canvas** con pruebas de pasa o no pasa por etapa | de **lector** |
| **293** | `mitigar_falling_asleep_wheel` contra `riesgo_sobredependencia_ia` | **pruebas-para-que-la-IA-falle**, casos disenados a proposito para medir si el equipo lo detecta; y **medir-con-y-sin-apoyo**, comparar la calidad de las decisiones tomadas con IA y sin ella | de **lector** |

#### 285: QUINTO gemelo-de-costurada, y el segundo del tipo caro

**`producto_unico_superior` es la confirmada LEVE de la tanda 13 de la ficha**, y
aqui repite con `superioridad_producto_beneficios`.

> **Es el segundo caso de AVERIADO POR DENTRO Y GEMELO POR FUERA**, tras
> `optimizacion_embudo_get_customers` del puesto 277. **Los otros tres del grupo
> eran falsas de costuras.**
>
> **Le aplica la CURA ACOPLADA igual que al 277**: destejer el apendice ajeno y
> fusionar con el gemelo **en el mismo acto**, por el TOQUE UNICO del banco 9.4.
> **Anotado en la ficha.**

#### 289: par de familia D4, al monton

**`assumption_and_constraint_log` contra `assumption_constraint_log`: el mismo
formulario con y sin la conjuncion `and` en el identificador.**

> **No es una decision de contenido: es la DECISION 4 ya adjudicada**, la de los
> identificadores que solo se diferencian en una particula. **Va al monton de esa
> decision y no consume mesa.**

#### 293: LA SUPERVISION DE LA IA SUBE A RACIMO, y con una precision

**El candidato de la seccion 11 sube.** Pero hay que decir con exactitud **que se
cumplio y que no**, porque la condicion que yo mismo escribi alli era mas
estrecha.

> **LO QUE ESCRIBI EN LA SECCION 11**: *nadie ha leido todavia un par CRUZADO
> entre las dos mitades*, y sin eso no esta probado que sean una familia y no dos
> parejas vecinas.
>
> **LO QUE HAY HOY**: el **293** es un **TERCER par disjunto**, con dos nodos
> nuevos, y el **692** es el primero que **cruza**, pero cruza un nodo nuevo con la
> mitad 1, no las dos mitades originales entre si.
>
> **Los cuatro pares que cruzarian las mitades 1 y 2 siguen PENDIENTES**: los
> puestos **1211**, **1239**, **1339** y **1451**.

**Sube igual, y el motivo es que la evidencia agregada es de otro tamano:**

| | |
|---|---:|
| miembros | **8** |
| pares posibles | **28** |
| en la cola intra | **13** |
| **leidos** | **4** |
| **de esos, en A** | **CUATRO DE CUATRO** (166, 177, 293, 692) |
| pendientes de la cola | **9** (792, 993, 1041, 1211, 1239, 1339, 1451, 1496, 1541) |
| pares que nunca entraron a la cola | **15** |
| **aristas internas** | **UNA** |
| fuente | **la misma para los ocho**: *Co-Intelligence* (Mollick) |

**LA NOMINA, contada con `scripts/contar_nombre.py` y leida uno por uno:**

| nodo | pasos |
|---|---:|
| `human_in_the_loop_ia` | 4 |
| `principio_humano_en_el_loop` | 4 |
| `comprension_capacidades_limitaciones_ia` | 5 |
| `jagged_frontier_ia` | 4 |
| **`mitigar_falling_asleep_wheel`** | 4 |
| **`riesgo_sobredependencia_ia`** | 4 |
| **`alineacion_etica_ia_negocio`** | 5 |
| **`comprender_alineacion_etica_ia`** | 4 |

> **Cuatro miembros nuevos respecto del candidato**, los tres primeros traidos por
> pares ya leidos y el cuarto por lectura del contador.
>
> **La forma sigue siendo la peor**: **una sola arista interna** entre ocho nodos,
> `jagged_frontier_ia` con `riesgo_sobredependencia_ia`. **Ocho nodos del mismo
> libro sobre el mismo asunto y el grafo conoce una sola pareja.**

**ADYACENTE, anotada y NO incluida**: `deteccion_alucinaciones_ia` y
`gestion_alucinaciones_ia` repiten entre si (puesto **363**, A) y el paso 2 de
`principio_humano_en_el_loop` manda justamente reconocer cuando la IA inventa.

> **El par que decide si se absorben es el 1478 y esta pendiente.** Hasta
> entonces son una pareja vecina, no dos miembros.

**LO QUE ESTE RACIMO PIDE**: es el tercer caso, con las puertas del Stage-Gate y
la serie de Coleman, en que **cuatro fusiones sueltas no valen**. Ocho nodos que
dicen donde acaba la IA y empieza la persona **necesitan una sola decision de
cuantos nodos quiere el catalogo**, no cuatro podas.

### TANDA R14, DECIMA CIEGA: seis de seis

**Acumulado: 84 de 84, de los cuales 60 a ciegas.** Perdidas verificadas contra
el grafo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **300** | `diferencia_ganancia_flujo_caja` contra `profit_vs_cash` | **proyeccion-12-18-meses** del flujo de caja segun lo que esperas crecer; y **lineas-de-credito-antes**, conseguir financiamiento **antes** de que la falta de efectivo sea urgente | de **lector** |
| **301** | `analisis_motivaciones_fundador` contra `influencias_tempranas_motivaciones` | **las-13-motivaciones** de la lista, de la que se eligen cuatro; **perfiles-tipicos** de quien emprende y de quien no, para compararse; y **control-o-riqueza**, saber cual de los dos pesa mas en ti | de **lector** |
| **302** | `asignacion_recursos_en_gates` contra `sistema_gestion_recursos_en_gates` | **lista-priorizada-visible** de proyectos activos en cada puerta; **no-agregar-sin-resolver** las implicaciones de recursos; y **compromiso-explicito** de personas y presupuesto en la reunion | de **lector** |
| **303** | `enfoque_etapa_investigacion` contra `etapa_investigacion_ventas` | ya anotadas en los puestos **209** y **278** | de **lector** |
| **305** | `metodologia_spin_selling` contra `modelo_spin` | **diagnostica-pequena-o-grande** antes de nada; **estudios-de-incremento**, la cifra de mas del veinte por ciento; **deja-abiertas-vs-cerradas**, que esa distincion no es el factor; y **transiciones-invisibles** entre tipos de pregunta | de **lector** |
| **306** | `pivote_startup` contra `pivotes_e_iteraciones` | **distingue-ajuste-de-cambio** entre iteracion y pivote; **versiona-el-lienzo**, documentar cada cambio como version nueva; y **cuentalo-como-normal** a quien trabaja contigo | de **lector** |

> **DOS DE FAMILIA DECLARADA**: el **302** es del racimo de **las puertas del
> Stage-Gate** (ocho miembros tras la remedicion del puesto 765) y el **306** del
> racimo censado **Pivotar o proceder**. **Sus direcciones de fusion quedan
> provisionales de par por la 9.3.**

#### 303: el CUARTO PURO sostiene su tercer par

**Con el 209 y el 278, los tres pares del puro de la etapa de investigacion han
pasado por la relectura a ciegas y los tres se sostienen.**

> **Es el segundo puro con todos sus pares releidos**, tras el de la ecuacion de
> valor. **La condicion del puesto 769 sigue viva** (el cuarto candidato externo,
> con los puestos 800 y 862 pendientes), pero **lo que esta leido, aguanta.**

#### 300: LA NOMINA DEL PRIMER PURO, contada, y NO crecio

**El encargo pedia verificar si la familia del efectivo contra la ganancia habia
crecido, porque el 300 parecia emparejar dos nodos de fuera. Contado con el
script y con `RACIMOS_MIEMBROS.jsonl`, la respuesta es que NO.**

| | |
|---|---:|
| nomina censada | **3**: `diferencia_ganancia_flujo_caja`, `profit_vs_cash`, `cash_is_king` |
| pares posibles | **3** |
| leidos | **3** (puestos **300**, **487** y **544**) |
| que repiten | **3** |
| pendientes | **0** |

> **Los dos nodos del 300 SI estan en la nomina**, y ese par es **uno de los tres
> que hicieron puro al racimo**. **No hay nada que degradar.**
>
> **Y el censo por script lo confirma por el otro lado**: los tres primeros del
> conteo son exactamente los tres de la nomina; los otros cuatro que asoman
> (`burn_rate_por_etapa`, `cash_burn_calculation` y dos mas) **hablan de consumo de
> caja, que es otro objeto**, y **ninguno de los tres tiene un solo par leido con
> un nodo de fuera**.
>
> **EL PRIMER PURO SE SOSTIENE SIN CAMBIOS.**

#### 305: LA FAMILIA SPIN, y la vara le cambio la clase

**Contada con el script y el jsonl. Es FAMILIA PROPIA, no material del racimo del
cierre en venta grande.**

| | |
|---|---:|
| miembros | **4**: `metodologia_spin_selling`, `modelo_spin`, `modelo_spin_preguntas`, `framework_spin_selling` |
| pares posibles | **6** |
| **en la cola** | **6**, o sea **todos** |
| leidos | **5** |
| clases | **A** (248), **A** (305), **A** (401), **D** (625), **D** (764) |
| **pendiente** | **UNO**, el puesto **856** |
| solape con el racimo del cierre | **NINGUNO**, cero miembros compartidos |

> **Lo que la nomina dice y la memoria no decia**: los cuatro pares que conectarian
> SPIN con el racimo del cierre **existen en la cola y estan los cuatro
> pendientes** (1150, 1375, 1489 y 1526). **Hoy son dos familias vecinas sin un
> solo par leido entre ellas.**

**Y AQUI ESTA EL HALLAZGO GORDO, que no es de nomina sino de doctrina:**

> **Antes de la vara del banco 9.6.1, esta familia tenia CINCO pares leidos y los
> CINCO en A.** Con el 856 en A habria sido el **QUINTO PURO** y habria ido
> directo al redactor.
>
> **La vara convirtio el 625 y el 764 en D**, y con eso la familia **paso de
> candidata a pura a MEZCLADA**, y una mezclada necesita mesa.
>
> **La vara no solo movio diecinueve veredictos: cambio la clase de familias
> enteras.** Y el efecto va en la direccion que ya se habia visto en el marcador:
> **menos consolidacion directa y mas enlace**. Es el primer caso donde se puede
> medir sobre una familia concreta.

**LA FORMA DE ESTA FAMILIA, para cuando le toque**: `framework_spin_selling` es
**el forastero declarado**, cita *Traction* de Weinberg y no a Rackham, y es uno
de los tres forasteros de *Traction* en familias de Rackham (con
`tacticas_cierre_ventas` y `compromiso_linea_tiempo_cliente`).

### TANDA R15, UNDECIMA CIEGA: seis de seis

**Acumulado: 90 de 90, de los cuales 66 a ciegas.** Perdidas verificadas contra
el grafo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **307** | `apertura_efectiva_llamada_venta` contra `apertura_llamada_venta_grande` | **veinte-por-ciento-de-preliminares** como tope de tiempo; **retoma-el-control** si el comprador pregunta por producto demasiado pronto; y **el-mito-de-la-primera-impresion**, que en venta grande la apertura pesa poco | de **lector** |
| **308** | `cofundar_con_amigos_familia_riesgos` contra `riesgo_cofundadores_relacion_previa` | **firewalls**, mecanismos formales para separar lo personal de lo profesional; **proyecto-pequeno-de-prueba** antes de comprometerse; y **trabajaste-de-verdad**, revisar si ya trabajaron juntos y no solo si se conocen | de **lector** |
| **312** | `produccion_scheduling_balance_objetivos` contra `programacion_produccion` | casi nada: **calco con reparto menor**, los mismos lote economico, run-out time y balance de los tres objetivos, en distinto orden | de **lector** |
| **317** | `investigar_datos_cliente` contra `seguimiento_informacion_cliente` | **cuenta-tu-algo-primero** para animar al cliente a contar; **escucha-enfocada** para captar lo que sale solo; **razon-declarada-vs-razon-real** de la compra; y **fecha-del-dato**, registrar cuando se obtuvo y cuando se actualizo | de **lector** |
| **319** | `customer_validation_sales_roadmap` contra `sales_roadmap_vs_sales_force` | **calco con reparto menor**: uno pone el detalle de quien decide y donde esta el presupuesto, el otro la regla de no contratar vendedores hasta validar | de **lector** |
| **320** | `estrategia_anuncios_sociales_respuesta_indirecta` contra `social_ads_indirect_response` | **migrar-gradualmente** la audiencia hacia conversion; **ventanas-largas** de medicion frente a la publicidad de busqueda; y **contenido-de-mision**, explicar el proposito de la marca y no solo el producto | de **lector** |

#### 307: LA FAMILIA DE LAS ETAPAS DE RACKHAM, anotada y sin censar

**La apertura entra al inventario, y con ella se ve el conjunto.**

> *SPIN Selling* divide la llamada en **cuatro etapas**: **Preliminares**
> (apertura), **Investigacion**, **Demostracion de capacidad** y **Obtencion de
> compromiso**. **El cribado ya toco las cuatro por separado**:
>
> | etapa | donde aparecio |
> |---|---|
> | **apertura** | puesto **307**, este par |
> | **investigacion** | el sub-puro de cuatro nodos (209, 278, 303, 800) |
> | **demostracion** | dentro del racimo del cierre y en `cuatro_etapas_llamada_de_ventas` |
> | **compromiso** | el racimo censado `El avance y el compromiso en la venta` |

> **Queda anotada como FAMILIA VECINA del racimo del cierre en venta grande, y no
> se amplia ningun censo.** La nomina la dira el contador cuando le toque: **hoy
> solo se sabe que las cuatro etapas tienen nodos y que tres de las cuatro ya
> tienen familia propia medida.**
>
> **El marco que las une, `cuatro_etapas_llamada_de_ventas`, ya salio en el puesto
> 775 y se comporta como marco y no como hermano**: enlaza a dos miembros de la
> familia de investigacion.

#### 319: EL TERCER PURO TAMBIEN CAE, y por el mismo motivo que el cuarto

**Contado con `scripts/contar_nombre.py` y el jsonl.**

> **`customer_validation_sales_roadmap` y `sales_roadmap_vs_sales_force` son de la
> misma familia que el trio**, leidos uno por uno: el primero define quien influye
> y decide, donde esta el presupuesto y cuantas llamadas cuesta cerrar; el segundo
> manda escribir paso a paso el camino a una venta repetible y **no contratar
> vendedores hasta validarlo**. **Los dos son el mapa de ventas.**

| | trio | familia real |
|---|---:|---:|
| miembros | 3 | **5** |
| pares posibles | 3 | **10** |
| leidos | 3 | **4** (192, 200, 255 y **319**) |
| en A | 3 | **4 de 4** |
| pendientes de cola | 0 | **5** (872, 918, 1023, 1306, 1330) |
| nunca en cola | 0 | **1** (`customer_validation_sales_roadmap` contra `sales_roadmap`) |

> **CORRECCION DECLARADA: el TERCER PURO queda degradado a SUB-PURO.** El trio
> sigue siendo puro puertas adentro y **sigue teniendo superviviente propuesto**,
> `refinar_sales_roadmap`, de la relectura R4. **Lo que ya no se puede decir es que
> la familia este cerrada.**
>
> **Le faltan SEIS lecturas**, cinco en cola y una que nunca entro. **Es mas caro
> de cerrar que el sub-puro de la investigacion, que necesita dos.**

**Y el sexto nodo que el contador levanta, `optimizacion_mercado_multilado`, NO
entra**: menciona el roadmap de ventas de pasada y su objeto es otro. **El script
lo trae, la lectura lo deja fuera.**

### TANDA R16, DUODECIMA CIEGA: seis de seis

**Acumulado: 96 de 96, de los cuales 72 a ciegas.** Perdidas verificadas contra
el grafo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **321** | `ineficacia_cierre_ventas_grandes` contra `riesgo_tecnicas_cierre_venta_compleja` | **auditoria-por-observacion**, auditar el uso de tecnicas de cierre escuchando llamadas reales; y **compara-tasas-entre-vendedores**, medir el exito de quien usa muchas tecnicas contra quien usa pocas | de **lector** |
| **322** | `desconexion_ventas_experiencia` contra `traspaso_ventas_cuentas` | **incentivos-de-quien-vende**, que al vendedor tambien le importe que el cliente quede bien; **CRM-automatico** que pase la informacion sin depender de nadie; y **promesa-contra-entrega-periodica**, revisar de vez en cuando si lo prometido coincide con lo entregado | de **lector** |
| **325** | `get_visual` contra `pensamiento_visual` | **si-cuesta-explicarlo-dibujalo** como regla de desatasco; y **libreta-siempre**, llevar encima el cuaderno o su equivalente digital | de **lector** |
| **326** | `fases_de_retencion_de_clientes` contra `ocho_fases_experiencia_cliente` | **prioriza-Affirm-y-Activate** como las dos fases mas descuidadas; y **detecta-atascos-y-plan-de-avance**, ver en que fase se atascan los clientes y armar el plan para moverlos | de **lector** |
| **328** | `formalizar_junta_asesora` contra `formalize_advisory_board` | **CEO-been-there**, buscar un asesor que ya haya dirigido; **mapa-por-area**, decidir que asesores necesitas por tecnico, negocio, cliente e industria; y **solo-impacto-estrategico**, calidad sobre cantidad | de **lector** |
| **329** | `diagnostico_efecto_latigo` contra `efecto_bullwhip` | **beer-game**, simular el juego con el equipo para que vean la dinamica; y **decidir-si-compartir-datos**, usar los numeros del costo para decidir si vale la pena coordinarse | de **lector** |

#### 321: la segunda poda intra-Rackham del racimo del cierre

**Los dos son de *SPIN Selling* y los dos del racimo de la seccion 9.**

> **La fusion respeta la frontera**: no toca al forastero `tacticas_cierre_ventas`
> de *Traction*, que es la linea de doctrina de ese racimo. **Es poda interna,
> como el 248 y el 274.**

#### 326: LOS DOS PROGRAMAS DE COLEMAN, confirmados a ciegas

**Y esto no es un par mas: es el arranque del tratamiento entero de esa serie.**

> La **DECISION 1** pide **un nodo-programa unico** que presente la serie y del que
> cuelguen las fases. **La serie de Coleman tiene DOS**, y el puesto 326 ya los
> habia marcado **A**. **La relectura a ciegas lo sostiene.**
>
> **Sin fundir estos dos primero, las piezas no tienen de donde colgar**, asi que
> este par es **el primer movimiento** de la candidatura de la seccion 12, no uno
> cualquiera.

**LAS DOS PRIORIDADES QUE TIENEN QUE VIAJAR AL SUPERVIVIENTE:**

| de que nodo | que dice |
|---|---|
| `fases_de_retencion_de_clientes` | **priorizar Affirm y Activate**, que son las dos fases mas descuidadas del ciclo |
| `ocho_fases_experiencia_cliente` | **detectar en que fase se atascan** los clientes y **armar el plan** para moverlos a la siguiente |

> **Ninguna de las dos esta en el otro nodo, y las dos son operativas.** Un
> programa unico que las pierda deja la serie sin punto de entrada, porque
> **Affirm y Activate son justamente donde la serie dice que esta el problema.**
>
> **Anotado junto a LA FORMA DEL TRATAMIENTO en la seccion 12.**

### TANDA R17, DECIMOTERCERA CIEGA: seis de seis

**Acumulado: 102 de 102, de los cuales 78 a ciegas.** Perdidas verificadas contra
el grafo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **330** | `proceso_sop_mop` contra `sop_colaborativo` | reparto menor: uno pone el **CONOPS** y la simulacion del sistema completo, el otro la **cadencia mensual** y la validacion con socios | de **lector** |
| **331** | `analisis_de_gastos_de_capital` contra `propuesta_gasto_capital` | **la taxonomia de beneficios** (directos, incrementales, de evitacion de costos e intangibles); el **hurdle rate**; el **analisis de sensibilidad**; **decision-del-analisis-no-al-reves**; **proyeccion-conservadora**; e **involucra-tecnicos** en las proyecciones | de **lector** |
| **334** | `construccion_de_leverage` contra `leverage_en_negociacion_con_vcs` | **sincroniza-tiempos** para que los term sheets lleguen juntos; **ancla-en-2-3** terminos prioritarios; y **nunca-el-primero-en-precio** | de **lector** |
| **335** | `prototipado_de_experiencias` contra `prototipado_experiencial_servicios` | reparto menor: uno dice **maqueta a escala real**, el otro **documentar insights emocionales**; lo demas es calco | de **lector** |
| **339** | `entender_term_sheet` contra `term_sheet_overview` | **clausulas-distraccion**, detectar las que no afectan ni economia ni control; y **asesoria-legal-VC** especializada para revisar el documento completo | de **lector** |
| **340** | `modelo_cascada_desarrollo_producto` contra `modelo_tradicional_introduccion_producto` | **deten-la-ejecucion-ciega** si no hay contacto continuo con el cliente; y **no-contrates-VP-antes** de validar el modelo | de **lector** |

#### 331: SEXTO nodo donde los dos ejes se cruzan, y TERCERO del tipo caro

**Y aqui hay que corregir la clasificacion del encargo, medida contra la ficha.**

> **El encargo lo llama la CUARTA FALSA de costuras reaparecida gemela.**
> **`propuesta_gasto_capital` no es falsa: es CONFIRMADA**, doce pasos, **DOBLE**,
> y ademas **el PRIMER FALSO NEGATIVO del instrumento**, el nodo por el que el
> umbral de bloque bajo de 45 a 44.

**El grupo, recontado de la ficha:**

| nodo | veredicto de costuras | puesto del intra |
|---|---|---:|
| SPIN | falsa | 248 |
| regalos | falsa | 251 |
| `founder_ceo_succession_process` | falsa | 256 |
| `optimizacion_embudo_get_customers` | **confirmada** | 277 |
| `producto_unico_superior` | **confirmada** | 285 |
| **`propuesta_gasto_capital`** | **confirmada** | **331** |

> **TRES falsas con gemelo y TRES confirmadas con gemelo.** Las tres confirmadas
> son las que necesitan **CURA ACOPLADA**; en las falsas no hay nada que destejer.

**Y esta trae una tercera pieza que las otras dos no tenian:**

> **La ficha ya habia medido que `propuesta_gasto_capital` esta ENCADENADO con un
> vecino generico**: `calculo_roi` a `comparacion_metodos_inversion` a
> `propuesta_gasto_capital`, **con el generico primero**, y aun asi la costurada
> vuelve a derivar lo mismo.
>
> **Asi que aqui la cura no es doble sino TRIPLE**: destejer el apendice, fusionar
> con el gemelo `analisis_de_gastos_de_capital`, **y mirar antes al vecino
> generico**, porque parte del material duplicado puede sobrar del todo si
> `calculo_roi` ya lo cubre. **Los tres movimientos, un solo acto.**

**Anotado en la ficha junto a los otros dos del tipo caro.**

#### LAS DOS NOMINAS, contadas con el contador y leidas una por una

##### a) La familia S&OP: CUATRO miembros y CERO aristas

| | |
|---|---:|
| miembros | **4**: `sop_colaborativo`, `sales_operations_planning`, `mission_and_operations_planning`, `proceso_sop_mop` |
| pares posibles | **6** |
| en la cola | 5 |
| **leidos** | **4**: **A** (173), **A** (330), **B** (703), **D** (725) |
| pendientes de cola | **1** (puesto 1218) |
| nunca en cola | **1**: `proceso_sop_mop` contra `sales_operations_planning` |
| **aristas internas** | **CERO**, los cuatro aislados |

> **Va a salir MEZCLADA, no pura**: ya tiene un sano y un dudoso dentro. **Le
> faltan DOS lecturas** para cerrar la cuenta.
>
> **El contador levanta tres nodos mas** (`driver_produccion`,
> `plataforma_colaboracion_masiva`, `roadmap_proyectos_operacionales_12_meses`) y
> **la lectura los deja fuera**: mencionan el S&OP o el plan maestro de pasada y
> su objeto es otro.

##### b) La competencia entre inversores: QUINTO PURO, y este si paso el contador

**El encargo decia que faltaba el par estrategia contra construccion. Ese par es
el puesto 787, se leyo hace cuatro tandas y dio A.** Contado el jsonl, la familia
esta **cerrada**.

| | |
|---|---:|
| miembros | **3**: `construccion_de_leverage`, `estrategia_competencia_vcs`, `leverage_en_negociacion_con_vcs` |
| pares posibles | **3** |
| **leidos** | **3** (puestos **257**, **334** y **787**) |
| **que repiten** | **3** |
| pendientes | **0** |
| aristas internas | **1**, y `estrategia_competencia_vcs` queda aislado |

**EL CONTADOR, hecho antes de declarar, como manda la regla del banco 9.5:** el
censo levanta **once** candidatos y **la lectura deja tres**. Los tres descartados
que mas se acercaban:

| nodo | por que NO entra |
|---|---|
| `gestion_sindicato_inversores` | maneja el sindicato **ya formado**, no crea la competencia |
| `no_shop_extension_negotiation` | negocia la extension del no-shop, otro objeto |
| **`batna_definicion`** | **el mas cercano**: su paso 3 manda mantener conversaciones con varios inversores y su paso 4 usar las alternativas como palanca. **Pero su objeto es el plan B, los limites propios y no farolear.** Queda **anotado como vecino**, y **no tiene ni un par con el trio en la cola**, asi que no hay lectura que pueda desmentirlo por ahora |

> **DECLARADO QUINTO PURO**, y es **el primero declarado con la regla del contador
> ya vigente**: censo primero, lectura despues, condicion dura al final. **Los tres
> son de libros distintos**, *Venture Deals* dos y *The Founder's Dilemmas* uno.
>
> **Superviviente propuesto**: `construccion_de_leverage`, que es el unico que
> trae las dos reglas de negociacion que los otros no tienen, **anclar en dos o
> tres terminos** y **nunca mover primero en precio**.

### TANDA R18, DECIMOCUARTA CIEGA: seis de seis

**Acumulado: 108 de 108, de los cuales 84 a ciegas.** Perdidas verificadas contra
el grafo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **341** | `blueprint_de_experiencia` contra `customer_journey_mapping` | ver abajo: **los dos nodos estan costurados y el solape es mapa contra mapa** | de **lector** |
| **342** | `framework_scor_plan_source_make_deliver` contra `scor_model_operaciones` | **la escalera completa de metricas**: KPI de **nivel 1** por categoria, metricas de **nivel 2**, diagnostico de **nivel 3** cuando hay desviacion, y el **benchmark** contra la industria | de **lector** |
| **343** | `estrategia_cuatro_capacidades_mercado` contra `modelo_cuadrantes_mercado` | **una-o-dos-capacidades**, concentrar la inversion en una o dos y no en todas; y **evita-eficiencia-en-crecimiento**, no invertir en eficiencia interna si compites en mercado de crecimiento | de **lector** |
| **344** | `plan_acquire_activate` contra `plan_de_adquisicion_acquire` | **los-19-canales** y **anota-lo-que-falla** (los dos del bloque Bullseye), **tope-bajo-por-prueba** y **escalonadas** | de **lector** |
| **345** | `determinar_tipo_de_mercado` contra `tipo_de_mercado_estrategia_competitiva` | **umbral-74** y las bandas de cuota; **escribe-el-documento** con las preguntas clave del tipo elegido; y **actualiza-canvas** con la hipotesis | de **lector** |
| **346** | `senales_de_compra_en_venta_grande` contra `senales_de_compra_reales` | **no-celebres-antes** de tiempo cuando el cliente menciona problemas; **clasifica-tras-cada-reunion** lo que dijo; y **planea-otra-conversacion** si solo hubo problemas mencionados | de **lector** |

#### 341: LOS DOS COSTURADOS, y el solape es MAPA CONTRA MAPA

**Los dos estan en la cola de las 128 y los dos con anatomia escrita en la
ficha.**

| nodo | anatomia registrada |
|---|---|
| `blueprint_de_experiencia` | **17 pasos, corte 13**, uno de los ocho ejemplares de **LA FORMA QUE PARTE** |
| `customer_journey_mapping` | **10 pasos, corte 7**, bloque 48,6, **EL MAPEO CONTADO DOS VECES**, dos fuentes: *Change by Design* y *Never Lose a Customer Again* |

> **Y el solape del par no es cualquiera: es el bloque de mapeo de uno contra el
> bloque de mapeo del otro.** Los dos mandan recorrer el viaje del cliente etapa
> por etapa, identificar los puntos de contacto y evaluarlos.

**LO QUE ESTO LE APORTA A LA CURA DEL RACIMO DE EXPERIENCIA, y es lo util:**

> **No son dos cirugias independientes que ademas hay que fusionar: son UNA.** El
> destejido de los dos tiene que **reunir los dos bloques de mapa en uno solo**,
> porque son el mismo mapa contado dos veces en dos nodos distintos.
>
> **Si se destejen por separado quedan dos mapas**, y el par vuelve a aparecer
> igual que ahora. **Anotado junto a la cura acoplada en la ficha.**

#### 344: consultada la ficha, y la clase se cita con su fuente

**`plan_de_adquisicion_acquire` esta registrado en
`docs/FICHA_SUBFUSION_GRADIENTE.md` como CONFIRMADA**, bloque **48,3**, corte
**9**, y nombrado alli **la QUINTA DE LA FORMA QUE PARTE**, con dos fuentes,
*The Startup Owner's Manual* y *Traction*:

| bloque | de que habla |
|---|---|
| **1 a 7** | **el Acquire Plan de Blank**: hipotesis, quien hace que con que presupuesto y que metrica, el pasa o falla antes de cada prueba, instrumentar el sitio, lanzar escalonado, tope de gasto y la plomeria de activacion |
| **8 a 12** | **el programa Bullseye de Weinberg, entero**: los 19 canales, prueba barata por canal, correrlas y medir, comparar y elegir, y anotar lo aprendido |

> **La clase del par es A y se emite hoy**, y el motivo esta en el banco 9.9: **el
> solape con `plan_acquire_activate` cae ENTERO en el bloque 1 a 7**, el de Blank.
> **No toca la juntura.**
>
> **Y eso corrige la lectura de las perdidas**: de las cuatro anotadas, **dos son
> del bloque Bullseye** (los 19 canales y anotar lo que falla) y **por lo tanto no
> se pierden en esta fusion: se van con el destejido**, a donde sea que el
> programa de Weinberg acabe viviendo. **Las que de verdad hay que salvar aqui son
> las otras dos**, el tope bajo por prueba y las pruebas escalonadas.

#### LAS DOS NOMINAS, contadas con el contador y leidas una por una

##### a) Los CUADRANTES DE MERCADO: cinco miembros y casi ningun par en la cola

| | |
|---|---:|
| miembros | **5**: `modelo_cuadrantes_mercado`, `clasificacion_mercados_cadena_suministro`, `cuatro_capacidades_mercado`, `estrategia_cuatro_capacidades_mercado`, `cuatro_categorias_desempeno_cadena_suministro` |
| pares posibles | **10** |
| en la cola | **5** |
| **leidos** | **4**, y **los CUATRO en A** (252, 343, 518, 651) |
| pendiente de cola | **1** (puesto 963) |
| **nunca en cola** | **CINCO** |
| aristas internas | **1**, con tres aislados |

> **Cuatro de cuatro repiten y a la familia le faltan seis lecturas**, cinco de
> ellas fuera de la cola. **Es el mismo perfil de las arenas**: mucha repeticion
> confirmada y la mayoria de los pares sin encolar.
>
> **El contador levanta tres nodos mas** (`ways_to_grow_matrix`,
> `ways_to_grow_framework`, `strat_map_arenas_estrategicas`) y **la lectura los
> deja fuera**: hablan de matrices de crecimiento y de arenas, no de los cuadrantes
> de oferta y demanda.

##### b) El TIPO DE MERCADO: cuatro miembros, y va a salir MEZCLADA

| | |
|---|---:|
| miembros | **4**: `determinar_tipo_de_mercado`, `tipo_de_mercado_estrategia_competitiva`, `hipotesis_tipo_mercado`, `entrada_mercado_nuevo` |
| pares posibles | **6** |
| **leidos** | **4**: **A** (228), **A** (345), **A** (686), **D** (825) |
| pendientes de cola | **0** |
| **nunca en cola** | **2** |
| aristas internas | **2**, con `hipotesis_tipo_mercado` aislado |

> **Ya tiene un sano dentro, asi que va a salir MEZCLADA**, y le faltan **dos
> lecturas**, las dos fuera de la cola. **Es de las mas baratas de cerrar.**

**DOS VECINOS QUE EL CONTADOR LEVANTA Y LA LECTURA DEJA FUERA, con su motivo:**

| nodo | por que no entra |
|---|---|
| `market_type_revenue_growth` | **consume** el tipo de mercado para proyectar curvas de ingresos; su objeto es la proyeccion |
| `posicionamiento_por_tipo_de_mercado` | **consume** el tipo para decidir el posicionamiento; su objeto es el mensaje |

> **Los dos tienen pares con la familia en la cola y los cuatro estan pendientes**
> (1145, 1214, 1323, 1426). **Quedan anotados como vecinos con lectura pendiente**:
> si alguno saliera A, la familia pasaria de cuatro a cinco o seis. **Es la misma
> forma que tumbo dos puros, y esta vez queda dicho antes y no despues.**

### TANDA R19, DECIMOQUINTA CIEGA: seis de seis

**Acumulado: 114 de 114, de los cuales 90 a ciegas.** Perdidas verificadas contra
el grafo, y **dos de las listadas en el dictado no resistieron la verificacion**:
quedan corregidas aqui abajo con su motivo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **353** | `analisis_de_cohortes` contra `metricas_cohortes` | **canal-mas-leal**, que canal de adquisicion trae clientes mas leales; y **curva-por-mejoras**, comparar cohortes en el tiempo para ver si las mejoras del producto cambian algo de verdad | de **lector** |
| **354** | `founder_ceo_succession_process` contra `sucesion_iniciada_por_fundador` | **el encuadre iniciada-por-fundador contra impuesta-por-la-junta**, con el dato de que quien la inicia conserva rol senior y silla | de **lector** |
| **356** | `estructura_gates` contra `sistema_gates_go_kill` | **criterios-eliminatorios** y **quien-con-poder-sobre-recursos** de un lado; **anota-decision-y-motivo** y **recursos-solo-tras-el-gate** del otro | de **lector** |
| **357** | `estrategia_de_innovacion_de_producto` contra `estrategia_innovacion_producto` | **el roadmap a tres o cinco anos** de uno; **los planes de ataque por arena** (innovador, seguidor rapido, proveedor de bajo costo) del otro | de **lector** |
| **361** | `key_partners_hypothesis` contra `partners_hypothesis_physical` | **una sola**: la **validacion posterior con reuniones reales** (ver la correccion) | de **lector** |
| **363** | `deteccion_alucinaciones_ia` contra `gestion_alucinaciones_ia` | **pregunta-de-distintas-formas**, **politica-interna** escrita, y el **patron sonar-creible** como senal de alerta | de **lector** |

#### LAS DOS CORRECCIONES DEL DICTADO, declaradas

**Por la DISCIPLINA DEL AUDITOR del banco 9.5: todo estado pasado va consultado.**
Estas dos salieron de consultarlo.

> **1. En el 361, dos de las tres perdidas dictadas ya estan dentro del nodo
> grande y por lo tanto no se pierden.**
>
> | perdida dictada | donde ya vive |
> |---|---|
> | **tabla-de-tres-columnas** | es el **entregable literal** de `key_partners_hypothesis`: *tabla de socios clave con columnas nombre, que proveen, que ofrece la empresa a cambio* |
> | **suplentes** | es su **paso 1**: *listar socios potenciales primarios y alternativos por tipo* |
> | **validacion-con-reuniones** | **no esta**: esta es la unica perdida real del par |
>
> **El archivo tampoco lo tenia fino**: la razon del 361 daba por cubierta la
> validacion con el *dejarlo anotado* del paso 5, que es **actualizar el Canvas**,
> no reunirse. **Actualizar un lienzo no valida un socio.**
>
> **2. En el 363, la prohibicion en documentos legales y financieros es COMUN, no
> perdida.** Esta en el paso 4 de `deteccion_alucinaciones_ia` y en el paso 1 de
> `gestion_alucinaciones_ia`, que la extiende a pitch decks, reportes y contratos.
> **Lo unico que solo uno nombra es la palabra financieros.** Es un matiz, no una
> perdida entera, y las otras tres del dictado se sostienen.

> **Ninguna de las dos cambia una clase.** Cambian **lo que el redactor tiene que
> salvar**, que es justamente para lo que se escriben estas listas.

#### 353: el par que el arreglo del racimo de cohortes ya habia nombrado

**La seccion 7 cerro con dos decisiones y no cinco**, y **este par es la segunda
de las dos.** La relectura a ciegas lo confirma sin tocarlo.

> **Vale la pena decir por que importa que aguante**: el arreglo entero del racimo
> de las metricas de cohorte **descansa sobre estas dos decisiones**. Si esta se
> cayera, el centro `metricas_accionables` se quedaria con dos hijos que repiten
> entre si y la familia volveria a ser un problema de cinco nodos.

#### 356: el cruce portafolio-puertas, visto DESDE DENTRO

**El cruce 2 de la seccion 13 mide el toque por fuera**:
`sistema_gates_go_kill` repite con `gestion_de_portafolio_gates_go_kill`, que
esta censado en otro racimo, y por eso la mesa de las puertas tiene que mirar
tambien la nomina del portafolio.

> **Este par mide el mismo nodo por dentro**: `sistema_gates_go_kill` **tambien
> repite con `estructura_gates`, que es de su propio racimo.**
>
> **Y eso cambia el orden del arreglo, no solo su tamano.** El nodo que une los
> dos racimos **esta duplicado dentro del suyo**: si la mesa del portafolio lo
> toca primero, decide sobre un nodo que la mesa de las puertas va a fusionar
> despues. **Primero se cierra la familia de las puertas, y con el superviviente
> en la mano se mira el cruce con el portafolio.** Anotado tambien en la seccion
> 13.

#### 357: la clase citada, y el nodo costurado NO es ninguno de los dos

**Consultada la ficha, como mandaba el dictado. Lo que hay no es lo que el dictado
suponia**, y por eso queda escrito con nombre y cifra.

**El nucleo tiene CUATRO nodos vivos con casi el mismo nombre**, y el censo por
script los levanta a los cuatro:

| nodo | pasos | que es | en la ficha de costuras |
|---|---:|---|---|
| `estrategia_de_innovacion_de_producto` | 6 | objetivos, arenas, buckets, roadmap | **no aparece** |
| `estrategia_innovacion_producto` | 5 | metas, rol, arenas, recursos, planes de ataque | **no aparece** |
| `estrategia_de_innovacion_y_tecnologia` | 5 | las arenas como filtro de ideas | **no aparece** |
| **`estrategia_de_innovacion_producto`** | **7** | **la apuesta audaz**, Cooper mas Horowitz | **CONFIRMADA**, bloque **45,7**, corte **3** |

> **El costurado es el CUARTO**, el unico sin la segunda preposicion, y **no es
> ninguno de los dos del par 357.** El par **no esta bloqueado por ninguna de las
> tres causas del banco 9.9**: se juzga hoy, y su **A se sostiene**.
>
> **La ficha ya lo habia bautizado**: *LA APUESTA AUDAZ, DOS VECES*, con la
> reinvencion contra el feedback del cliente contada en sus pasos 4 a 7 con
> vocabulario de Horowitz.

**Y el estado de la familia, contado del archivo:**

| par | nodos | clase |
|---:|---|:---:|
| **357** | los dos del racimo censado | **A** |
| **530** | `estrategia_de_innovacion_de_producto` contra `estrategia_de_innovacion_y_tecnologia` | **A** |
| **863** | `estrategia_de_innovacion_y_tecnologia` contra `estrategia_innovacion_producto` | **pendiente, y cae en este mismo tramo** |
| 405 | el costurado contra `estrategia_de_innovacion_y_tecnologia` | **B**, bloqueado por la costura |
| 1325 | el costurado contra `estrategia_de_innovacion_de_producto` | pendiente |

> **El racimo censado de TRES se cierra en el puesto 863**, que esta a menos de
> treinta lecturas. **Si sale A, los tres pares del racimo estan leidos y los tres
> en A: seria un PURO de tres**, con la condicion dura cumplida y el contador ya
> corrido aqui arriba. **Queda como condicion viva, no como prediccion.**

#### 361: `key_partners_hypothesis` es el SEPTIMO EJEMPLAR de la CURA ACOPLADA

**Consultada la ficha, como mandaba el dictado, y la clase real es la peor de las
posibles para el plan:**

| eje | veredicto |
|---|---|
| **la ficha de costuras** | **CONFIRMADA**, bloque **51,7**, catorce pasos, **TRIPLE**: el Canvas en los pasos 1 a 5, el libro de traccion en los 6 a 10, y las alianzas por cuello de botella en los 11 a 14 |
| **el intra** | **A** en este mismo puesto 361, gemelo `partners_hypothesis_physical` |

> **Averiado por dentro y gemelo por fuera: le toca CURA ACOPLADA**, destejer y
> fusionar en el mismo acto. **Es el SEPTIMO ejemplar de la lista y el CUARTO del
> tipo caro**, detras de 277, 285 y 331. **Anotado en la ficha, que es donde la
> cura acoplada exige que viva.**

**Y por la TERCERA CAUSA del banco 9.9, el par entra a la COLA DE RELECTURA
POST-CIRUGIA.** Con una diferencia que hay que decir para que la cuenta no se
tuerza:

> **El 361 entra a la cola SIN quedar congelado, y es el primero asi.** La clase
> se emite hoy porque **la relacion del par es la propia estructura de bloques**:
> el nodo chico **es** el bloque 1 a 5 del grande, y eso lo dice la ficha, no la
> lectura. **Cualquier destejido plausible deja el bloque del Canvas en pie**, asi
> que el superviviente de la cura sigue conteniendo al chico entero.
>
> **Comparalo con el 835**, que si quedo en B: alli los dos nodos son textos
> independientes que **se cruzan en dos instrucciones**, y cuanto se cruzan
> depende de que quede tras la cura. **Ahi la clase si depende de la cirugia.**

> **LO QUE ESTO SEPARA, y va como propuesta al auditor**: **la cola de relectura
> es mas ancha que la cuenta de congelados.** Un par entra a la cola cuando su
> texto va a cambiar; queda **congelado** solo cuando **el veredicto depende de
> que sobreviva**. **Hoy los dos numeros se llevaban juntos y este par los
> separa: once congelados, doce en cola.**

#### 363: la pareja de las alucinaciones, y quien decide si entra al racimo

**Los dos nodos son del mismo libro, Mollick, y repiten la misma politica.** La
fusion entre ellos **no depende de nadie**: se hace.

> **Lo que si depende de otra lectura es si la pareja se absorbe en el racimo LA
> SUPERVISION DE LA IA**, el de la seccion 11. **Y el que lo decide tiene numero:
> el puesto 1478**, `deteccion_alucinaciones_ia` contra
> `principio_humano_en_el_loop`, **el unico par de la cola que toca los dos
> lados.** Anotado en la seccion 11 junto a las otras condiciones vivas.

### TANDA R20, DECIMOSEXTA CIEGA: seis de seis

**Acumulado: 120 de 120, de los cuales 96 a ciegas.** Perdidas **propuestas por el
auditor y verificadas una por una contra los dos nodos** antes de escribirlas.
**El saldo de esa verificacion: una lista entera cae, otra se recorta a un tercio,
y dos crecen.**

| puesto | el par | que se pierde DE VERDAD | tipo |
|---:|---|---|---|
| **364** | `rediseno_procesos_negocio_cliente` contra `rediseno_procesos_negocio_cx` | las cuatro dictadas **mas tres**: ver abajo | de **lector** |
| **366** | `deep_dive_workshop` contra `metodologia_deep_dive` | el formato **Como podriamos**, **simular la situacion** cuando no se puede observar, y la version ligera **Skinny Dip** | de **lector** |
| **367** | `identificar_consejo_asesores` contra `identificar_junta_asesores` | **NADA verificable**: las tres dictadas ya viven en el otro nodo | de **lector** |
| **371** | `metrics_that_matter_framework` contra `validar_modelo_financiero` | **burn rate aceptable y cuantos pivotes quedan**; el **P&L, balance y flujo multianual**; y el **CAC contra el LTV** | de **lector** |
| **373** | `fase_assess_ciclo_cliente` contra `fase_assess_experiencia_cliente` | **algo tangible que de una prueba real** de la experiencia posterior; y **calificar del 1 al 10** la etapa de hoy | de **lector** |
| **374** | `split_testing` contra `split_testing_experimentos_ab` | **una sola**: la **significancia del 95%**. Las otras dos se van con el destejido | de **lector** |

#### 364: las cuatro se sostienen, y hay TRES mas que el dictado no listo

| perdida | de que nodo | verificado |
|---|---|---|
| compensaciones automaticas al incumplir la promesa | `_cliente` | **si**, paso 4, y no esta en el otro |
| presupuesto sostenido durante varios anos | `_cx` | **si**, paso 5 |
| ensenar a TODAS las personas, no solo a quien atiende | `_cx` | **si**, paso 2 |
| reducir la cantidad de herramientas y sistemas | `_cx` | **si**, paso 3 |
| **resolucion en un solo contacto** | `_cliente` | **anadida**, paso 3 |
| **medir el impacto con metricas antes y despues** | `_cliente` | **anadida**, paso 5 |
| **alguien con vision de todo el proceso a cargo** | `_cx` | **anadida**, paso 4 |

> **Siete piezas para salvar en un par de dos nodos de cinco pasos cada uno.** Es
> el par mas caro de fundir del tramo, y **el dictado se quedaba corto por tres**.

#### 366: y el CRUCE con el racimo del HMW queda anotado

> **`deep_dive_workshop` manda plantear la pregunta central en formato COMO
> PODRIAMOS dentro de su paso 2.** Y el nucleo tiene un racimo censado,
> **`Encuadre del problema (How Might We)`, con CINCO miembros.**
>
> **Es la misma figura que los seis canales dentro de una fase de Coleman**: una
> serie instanciada **dentro** de un nodo que pertenece a otra familia. **Y por
> eso lleva el mismo orden**: quien toque el HMW despues de fundir los deep dive
> tiene que volver a entrar en el nodo fundido.

#### 367: las TRES perdidas dictadas ya viven en el otro nodo

**Este es el motivo por el que el dictado se verifica antes de escribirlo.**

| perdida dictada | donde ya vive en `identificar_junta_asesores` |
|---|---|
| **mentor de negocio** | en su **resumen**: *asi como un mentor de negocios con experiencia previa en startups* |
| **pide ayuda concreta** | en su **paso 4**: *asesores para problemas tecnicos, introducciones a clientes clave, conocimiento de dominio y desarrollo de producto* |
| **formaliza mas adelante** | en su **resumen**: *formalizar la junta asesora se hace mas adelante, durante la validacion de clientes* |

> **La fusion de este par no pierde nada verificable en ningun sentido.** Los dos
> nodos dicen lo mismo con las mismas piezas, **uno repartiendolas entre pasos y
> resumen y el otro toda en pasos.** Es la fusion mas barata del tramo y
> probablemente de varios tramos.

#### 373: la ASSESS DOBLADA confirmada, y la evidencia viva del ORDEN

**El par repite y aguanta la ciega.** Lo que aporta a la seccion 12 no es la
clase, es la **prueba de que el paso 2 del tratamiento va donde esta**:

> **`fase_assess_ciclo_cliente` manda, en su paso 5, disenar al menos una mejora
> usando uno de los SEIS CANALES de comunicacion.** O sea que **la serie de los
> medios esta instanciada DENTRO de un nodo de la serie de las fases**, viva y
> operante, no como nota.
>
> **Ese es el motivo del orden medios-antes-que-fases**, y ahora tiene ejemplar
> leido dos veces: **si las fases se consolidan primero, la consolidacion se hace
> sobre un texto que la serie de medios va a reescribir despues.**

#### 374: la clase citada, la cura, y DOS de las tres perdidas no se pierden aqui

**Consultada la ficha antes de registrar, como mandaba el dictado:**

| eje | veredicto |
|---|---|
| **la ficha de costuras** | **CONFIRMADA**, nueve pasos, corte **6**, **DOBLE**: el A/B de producto de Ries en los pasos **1 a 5** y la narracion de **grupo de control de Rackham** en los **6 a 9** |
| **el intra** | **A** en este mismo puesto 374, gemelo `split_testing` |

> **Costurada confirmada con gemelo declarado: CURA ACOPLADA.** Es el **OCTAVO
> ejemplar** de la lista de la ficha y el **QUINTO del tipo caro**. Anotado alli.

**Y la regla nueva del banco 9.9 decide su puesto sin discutir:**

> **EN COLA, NO CONGELADO.** El solape **cae entero en el bloque 1 a 5**, el de
> Ries, y **el destejido se lleva el bloque 6 a 9**, el de Rackham. Lo que
> sobrevive a la cura **es justamente el bloque donde el solape vive**, asi que
> **el veredicto es invariante**: siga la cirugia el camino que siga, el
> superviviente sigue repitiendo con `split_testing`.

**LA CORRECCION DE LAS PERDIDAS, y es la misma del puesto 344:**

| perdida dictada | en que bloque vive | que le pasa |
|---|---|---|
| **significancia del 95%** | en `split_testing`, el nodo chico | **se pierde de verdad** en esta fusion |
| comparar el **cambio porcentual** y no los absolutos | paso 8, **bloque de Rackham** | **no se pierde aqui**: se va con el destejido |
| **grupo de control con desempeno inicial similar** | paso 6, **bloque de Rackham** | **no se pierde aqui**: se va con el destejido |

> **Dos de las tres perdidas dictadas pertenecen al material que la cirugia va a
> sacar del nodo.** Hay que salvarlas, si, **pero en el otro frente y con otro
> destino**, no en este par. **Es la segunda vez que pasa lo mismo** y ya se puede
> decir en general: **cuando un nodo costurado entra a un par, la lista de
> perdidas hay que repartirla por bloques antes de entregarsela al redactor.**

#### LA NOMINA DE LA JUNTA ASESORA: SEPTIMO SUB-PURO

**El contador primero, con `contar_nombre.py` y tres terminos**, *junta asesora*,
*consejo asesor* y *advisory*. **La lectura deja fuera a uno**:
`decision_pivotar_o_proceder`, que **consulta** al consejo asesor en un paso pero
cuyo objeto es la decision de pivotar.

| | |
|---|---:|
| miembros | **4**: `identificar_consejo_asesores`, `identificar_junta_asesores`, `formalizar_junta_asesora`, `formalize_advisory_board` |
| pares posibles | **6** |
| en la cola | **5** |
| **leidos** | **3**, y **los TRES en A** (328, 367, **712**) |
| pendientes de cola | **2** (976 y 1190) |
| **nunca en cola** | **1** |
| aristas internas | **1**, entre `identificar_junta_asesores` y `formalizar_junta_asesora`; **los otros dos aislados** |

> **La familia son DOS momentos, identificar y formalizar, con dos nodos cada
> uno.** Y **el par que cruza los dos momentos ya esta leido: el 712, y es A.**
> O sea que **aqui no repite solo cada momento consigo mismo: repite el momento
> siguiente con el anterior.**
>
> **SUB-PURO por la condicion dura**, y **de los que se cierran solos**: dos de
> las tres lecturas que faltan **ya estan en la cola**. Entra a la tabla viva del
> banco 9.5 como el numero **7**.

### TANDA R21, DECIMOSEPTIMA CIEGA: seis de seis

**Acumulado: 126 de 126, de los cuales 102 a ciegas.** Perdidas propuestas,
verificadas contra los dos nodos **y repartidas por bloques** donde hacia falta,
por la figura nueva del banco 9.11.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **376** | `ciclo_construir_medir_aprender` contra `ciclo_crear_medir_aprender` | **partir del final del ciclo**, definir que se necesita aprender antes de construir; las **metricas de innovation accounting** que lo demuestran; y **una tercera que el dictado no listo**, repetir el ciclo **cada vez mas rapido** | de **lector** |
| **378** | `valor_del_dinero_en_el_tiempo` contra `valor_presente` | **identificar el riesgo** de recibir el dinero mas tarde, y **definir el retorno exigido** segun ese riesgo | de **lector** |
| **380** | `test_socios_de_trafico` contra `traffic_partners_hypothesis` | de uno: el **correo centrado en lo que el socio gana**, la **ficha de resultados** tras cada reunion, y **cerrar acuerdos firmes**; del otro: **ordenar la lista por criticidad** y mirar **tiendas de aplicaciones y marketplaces** | de **lector** |
| **381** | `etnografia_aplicada_en_equipos_multidisciplinarios` contra `etnografia_de_proyecto` | las **situaciones analogas** (el pit stop para entender urgencias) y la **convivencia y estadias** frente a las entrevistas puntuales | de **lector** |
| **386** | `enfoque_mercado_voc` contra `voz_del_cliente_voc` | **repartida por bloques**, ver abajo | de **lector** |
| **387** | `fallo_como_aprendizaje_startup` contra `fracaso_como_aprendizaje_startup` | los **criterios de exito y fracaso** definidos de antemano, **documentar cada fracaso** como aprendizaje valido, y **no penalizar** al equipo por hipotesis fallidas | de **lector** |

#### 386: `voz_del_cliente_voc` es el NOVENO ejemplar de la cura acoplada

**Es el nodo que mas pares congela de todo el archivo**, tres (724, 755, 827), y
ahora se sabe por que le toca la cura mas cara:

| eje | veredicto |
|---|---|
| **la ficha de costuras** | **CONFIRMADA**, bloque **50,2**, diez pasos, **DOBLE DE LA OBSERVACION**: Cooper en los pasos **1 a 5** y Coleman en los **6 a 10**, con el duplicado literal **paso 2 contra paso 6** |
| **el intra** | **A** en este puesto 386, gemelo `enfoque_mercado_voc` |

> **Costurada confirmada con gemelo declarado: CURA ACOPLADA.** **Noveno ejemplar
> y SEXTO del tipo caro.** Y aqui la frase de la ficha se vuelve literal:
> **destejer y fundir son el mismo acto**, porque el gemelo cubre justo la mitad
> que la cirugia deja en pie.

**SU PUESTO EN LA COLA, con la regla del 9.9: EN COLA, NO CONGELADO.**

> El solape con `enfoque_mercado_voc` **cae entero en el bloque 1 a 5**, el de
> Cooper, y **el destejido se lleva el 6 a 10**, el de Coleman. **Lo que sobrevive
> es justo donde el solape vive**, asi que el veredicto es invariante. **Tercer par
> en cola sin congelar**, con el 361 y el 374.

**LA PERDIDA, REPARTIDA por el banco 9.11:**

| se salva en ESTA fusion | viaja con el destejido |
|---|---|
| de `enfoque_mercado_voc`: la **evaluacion preliminar de mercado** antes de comprometer recursos, el **analisis competitivo detallado** de productos, precios y tecnologias, y **probar los conceptos con clientes reales** antes del desarrollo formal | de `voz_del_cliente_voc`, **bloque 6 a 10**: observar **una vez al mes**, ponerse en el lugar del cliente, las **pepitas de oro** de los comentarios casuales, anotar y revisar uno o dos dias despues, y buscar patrones |

> **El dictado listaba el bloque de observacion entero como perdida.** La mitad de
> Cooper (pasos 1 a 5) **no se pierde: sobrevive en el superviviente.** La mitad de
> Coleman **tampoco se pierde aqui: se va con el destejido.** **Tercer ejemplar de
> la figura**, con el 344 y el 374.

#### 381: par interno del sub-puro de la etnografia, y aguanta

**Es uno de los tres pares que sostienen el sub-puro numero 6 del banco 9.5**, con
el 230 y el 839. **Releido a ciegas, sostiene su A.**

> **Lo que esto asegura**: el sub-puro **no descansa en una sola lectura vieja**.
> De sus tres pares, **este es el segundo que se releee** y los dos han aguantado.
> Le siguen faltando **tres lecturas, las tres fuera de la cola.**

#### 376 y 387: dos ids SINONIMOS, al monton de la DECISION 4

| puesto | los dos ids | la diferencia |
|---:|---|---|
| **376** | `ciclo_construir_medir_aprender` contra `ciclo_crear_medir_aprender` | **construir** contra **crear** |
| **387** | `fallo_como_aprendizaje_startup` contra `fracaso_como_aprendizaje_startup` | **fallo** contra **fracaso** |

> **Van al monton de la DECISION 4 y no consumen mesa.** **Una precision de
> redaccion, no de fondo**: la DECISION 4 esta escrita para *identificadores que
> solo se diferencian en una particula* (el ejemplar fue `and` contra nada, puesto
> 289). **Estos dos se diferencian en un SINONIMO**, que es un paso mas alla de una
> particula. **Van al mismo monton por decision del auditor**, y queda dicho para
> que el texto de la decision se ensanche cuando alguien la redacte, o para que
> estos lleven su propia linea.

> **Y los dos traen la misma leccion de fondo**: en los dos casos **el nodo con el
> id mas largo es el que trae el material propio** (partir del final y el
> innovation accounting en el 376; los criterios de exito y fracaso, la
> documentacion y el no penalizar en el 387). **El monton de la DECISION 4 no
> puede fusionar a ciegas por el id: tiene que leer cual de los dos trae mas.**

### TANDA R22, DECIMOCTAVA CIEGA: CINCO de seis, y la PRIMERA DISCREPANCIA

**Acumulado: 132 de 132 releidos, de los cuales 108 a ciegas. Coincidencias: 131
de 132.** El puesto **395** es **la primera discrepancia en todo el ejercicio**, y
se resolvio en relectura conjunta: **la clase cambia**.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **389** | `leap_of_faith_assumptions` contra `leap_of_faith_questions` | **reescribir las comparaciones** con otros negocios en terminos verificables; **disenar el experimento** que valida cada supuesto antes de construir | de **lector** |
| **392** | `build_metrics_toolset` contra `metricas_de_adquisicion_activacion` | **repartida por bloques**, ver abajo | de **lector** |
| **394** | `construccion_de_leverage` contra `gestion_multiples_term_sheets` | **nunca ser el primero en poner precio**; **usar el primer term sheet como palanca**; y **dos que el dictado no listo**: anclar en dos o tres terminos y flexibilidad en el resto, e identificar a todos los VCs objetivo antes de empezar | de **lector** |
| **395** | `proceso_diseno_modelo_negocio_5_fases` contra `proceso_ideacion_modelo_negocio` | **cambia de clase**, ver abajo | **de CATALOGO a de LECTOR** |
| **400** | `hipotesis_de_canales` contra `seleccion_canal_distribucion` | **una sola**: los **habitos de compra** establecidos en la categoria | de **lector** |
| **401** | `modelo_spin` contra `modelo_spin_preguntas` | **dejar de entrenar abiertas contra cerradas**, **revisar tus llamadas** para ver donde te trabas, y **presentar la solucion recien cuando el cliente articule** la necesidad explicita | de **lector** |

#### 395: LA PRIMERA DISCREPANCIA, resuelta en conjunta. **A pasa a D.**

**LAS DOS LECTURAS, dichas enteras antes de decidir:**

| | qué dice |
|---|---|
| **la A vigente** | el hijo es **segunda casa** de la fase 3, que ya tiene la suya (`fase_diseno_prototipado_modelos`). Duplicacion de casa, no de arista |
| **la del auditor** | por **LA LINEA O EL PROCEDIMIENTO**: el hijo trae **criterios de seleccion, reducir a tres o cinco y prototipar**, procedimiento que la madre no tiene. **D** |

**VERIFICADO CONTRA EL ARCHIVO, y es lo que decide:**

| par | nodos | clase |
|---:|---|:---:|
| **507** | `fase_diseno_prototipado_modelos` contra `proceso_ideacion_modelo_negocio` | **A** |
| **633** | `fase_diseno_prototipado_modelos` contra la **madre** | **D** |
| **641** | `fase_diseno_prototipado_modelos` contra `prototipado_modelos_negocio` | **A** |

> **La duplicacion que la razon vieja describia YA ESTA REGISTRADA, y en el par
> que le corresponde: el 507.** El 395 la estaba cobrando **por segunda vez y
> contra el nodo equivocado.**
>
> **Y la inconsistencia se ve sin discutir**: la misma madre contra **las dos
> casas** de su fase 3 daba **D** con una (633) y **A** con la otra (395). **No
> pueden ser las dos.**

> **VEREDICTO: 395 pasa de A a D**, con correccion declarada dentro de su razon.
> **Por la vara**: la fase 3 de la madre es **una linea**, *genera y prueba
> prototipos y selecciona el mejor*; el hijo trae **criterios de seleccion**
> nombrados (tiempo de implementacion, potencial de ingresos, resistencia del
> cliente) y **reducir a tres o cinco y prototiparlas**. **Procedimiento, no
> linea. CONTINUA.**

> **LO QUE SI SE PIERDE Y QUEDA ANOTADO**: los pasos 1 y 2 del hijo, **el equipo
> diverso y la inmersion**, vuelven a contar las fases 1 y 2 de la madre. **Eso es
> material repetido dentro de un nodo sano**, y el redactor tiene que podarlo, no
> fusionarlo.

**Y LA PARAFRASIS ABOLIDA ESTABA VIVA EN SU TEXTO.** La razon empezaba con *la
regla lo resuelve: SIN ARISTA, verificado, o sea DUPLICACION*, que es exactamente
la parafrasis que el banco 9.5.0 abolio. **Reescrita citando la vara.**

#### 394: el QUINTO PURO se degrada a SUB-PURO, y el contador se queda corto

**`gestion_multiples_term_sheets` ES un cuarto miembro**, y no por este par: **ya
tenia DOS A con miembros en el archivo antes de esta lectura.**

| | antes | ahora |
|---|---:|---:|
| miembros | 3 | **4** |
| pares posibles | 3 | **6** |
| leidos | 3 | **5** (257, 334, **394**, **413**, 787) |
| en A | 3 | **5** |
| pendientes | 0 | **1**: el puesto **1030** |

> **Por que el contador no lo vio**: se corrio sobre el nombre de la familia,
> *competencia entre inversores*, y este nodo **se llama por su artefacto**, term
> sheets. **El termino correcto era otro y el nodo estaba a la vista con el
> 413 ya en A.**
>
> **De ahi la precision del banco 9.15: el contador se complementa con EL BARRIDO
> DE LAS A.** Todo nodo con A vigente contra un miembro es candidato a miembro.

> **Le falta UNA lectura y esta en la cola.** Si el **1030** sale A, esta familia
> es **PURO DE CUATRO**, el primero de ese tamano en todo el archivo.

#### 392 y 401: las dos clases citadas de la ficha, y salen distintas

| nodo | clase real en la ficha | efecto en el par |
|---|---|---|
| **`modelo_spin_preguntas`** | **CITA FALSA**, seis pasos, bloque 46,5, nombrada **SECUENCIA LEGITIMA**: la secuencia SPIN entera mas el ajuste de ritmo | **ninguno**: no es costura, el 401 es libre |
| **`metricas_de_adquisicion_activacion`** | **una de las VEINTE fuera de cola**, dos obras, **sin anatomia escrita** hasta hoy | **es costura, y con gemelo: cura acoplada** |

**ANATOMIA DE `metricas_de_adquisicion_activacion`, verificada contra el grafo y
escrita por primera vez** (tercera de las veinte que la recibe):

| bloque | de que habla |
|---|---|
| **1 a 5** | **Blank**: que relacion se quiere con el cliente, menos de doce metricas accionables, metricas de adquisicion, metricas de activacion, y el tablero |
| **6 a 9** | **Weinberg**: definir que es una conversion antes de lanzar campana, calcular CTR, CPC y CPA por campana de prueba, comparar CAC contra LTV, y usar SEM para **aprender** que mensaje funciona |

> **DECIMO EJEMPLAR DE LA CURA ACOPLADA** y septimo del tipo caro: costurada con
> gemelo declarado (este 392 en A). **Anotado en la ficha.**

**SU PUESTO EN LA COLA: EN COLA, NO CONGELADO**, y con un aviso.

> El solape del par es **el montaje del instrumento** (hipotesis de relacion,
> menos de doce metricas, instrumentar, tablero), y **cae entero en el bloque 1 a
> 5**, el que sobrevive al destejido. **Veredicto invariante.**
>
> **EL AVISO, porque estuvo cerca**: este nodo **repite el costo de adquisicion a
> los dos lados de la juntura**, en su paso 3 y otra vez en los pasos 7 y 8. **Si
> el solape de un par futuro cae sobre el CAC, ese par SI bloquea.** Este no,
> porque su solape es el montaje y no el costo.

**LA PERDIDA, REPARTIDA por el banco 9.11:**

| se salva en ESTA fusion | viaja con el destejido |
|---|---|
| de `build_metrics_toolset`: que el sistema **escale luego a retencion y cohortes** | **las tres del dictado**: definir que es una conversion, el CAC contra el LTV, y el SEM para aprender. **Las tres son del bloque de Weinberg** |

> **El dictado listaba las tres como perdidas del par. Ninguna lo es**: las tres
> viven en el bloque que la cirugia se lleva. **Cuarto ejemplar de la figura**,
> con el 344, el 374 y el 386.

#### 400: una de las dos perdidas dictadas no lo es

> **`un-solo-canal` esta en LOS DOS nodos**, y con las mismas mayusculas: paso 4
> de `hipotesis_de_canales` y paso 5 de `seleccion_canal_distribucion`. **La razon
> vieja ya lo decia.** La unica perdida real del par son **los habitos de compra
> establecidos en la categoria.**

### TANDA R23, DECIMONOVENA CIEGA: seis de seis

**Acumulado: 138 releidas, de las cuales 114 a ciegas. Discrepancias acumuladas:
UNA**, el puesto 395, ya resuelta en conjunta. Perdidas propuestas, verificadas
una por una contra los dos nodos.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **404** | `cash_burn_calculation` contra `metrics_that_matter_framework` | **definir que burn rate es aceptable** y **cuantos pivotes mas se pueden costear**. Las dos del nodo grande: **el chico no aporta nada propio** | de **lector** |
| **406** | `key_resources_hypothesis` contra `recursos_clave` | de Blank: **de donde puede venir el dinero** (capital de riesgo, subsidios, factoring, leasing), **que vale la pena proteger** como propiedad intelectual, y **que dependencias quedan fuera de tu control**; de Osterwalder: **calcular los recursos financieros** concretos, efectivo y lineas de credito | de **lector** |
| **410** | `planificacion_preguntas_implicacion` contra `preguntas_implicacion` | **escribir tres problemas potenciales antes de la llamada**, y **practicar y refinar** las preguntas porque son las que mas habilidad piden | de **lector** |
| **413** | `estrategia_competencia_vcs` contra `gestion_multiples_term_sheets` | **la ventana de tres a seis meses**, **pedir feedback concreto si dicen que no**, **nunca compartir el contenido de un term sheet**, y **dos que el dictado no listo**: identificar a todos los VCs objetivo antes de empezar y usar el primer term sheet como palanca | de **lector** |
| **417** | `blogging_como_canal_de_traccion` contra `content_marketing_blog` | **las infografias y el contenido visual**, que se comparten unas veinte veces mas; los **lead magnets** para construir lista de correo; y **los seis meses de publicacion consistente antes de evaluar** | de **lector** |
| **419** | `desirability_feasibility_viability` contra `triada_restricciones_diseno` | **aprovechar los activos existentes** (marca, base de clientes, distribucion) cuando se parte de deseabilidad, e **iterar entre las tres restricciones durante todo el ciclo** y no de forma lineal | de **lector** |

#### 404: EL HIJO CONTENIDO, y la vara dice que no trae nada

**Los cuatro pasos de `cash_burn_calculation` son los pasos 3, 4 y 5 de
`metrics_that_matter_framework`**, verificado uno por uno:

| cash_burn | donde vive en el otro |
|---|---|
| ingresos netos por trimestre | paso **3**, restar descuentos y costos de canal |
| restar costos de ventas, producto y operativos | paso **4** |
| el resultado es lo quemado | paso **4** |
| restar del efectivo inicial para saber cuanto queda | paso **5**, la hoja trimestral con el efectivo en banco |

> **LA VARA, aplicada y con respuesta clara: NO trae procedimiento propio.** No es
> que lo que anade quepa en una linea: **es que no anade nada.** El nodo grande lo
> contiene entero y ademas trae dos pasos previos (tipo de canal, unidades por
> precio de venta validado) y dos posteriores (el burn aceptable, cuantos pivotes
> quedan) que el chico no tiene.
>
> **Es el CONTENIDO SIN RESIDUO**, la fusion mas barata que existe: **se borra el
> chico y no hay que salvar nada de el.** Distinto del caso normal, donde siempre
> queda algo que rescatar.
>
> **Y tiene arista en los dos sentidos**, verificada resolviendo a nodo vivo: **el
> grafo ya sabe que van juntos.**

#### 406: el gemelo VERDADERO de `key_resources_hypothesis`, y lo que le dice a la calibracion

**El molde PLANTILLA DE ID esta registrado en `INTRA_DOMINIO_RESUMEN.md` como
falso positivo conocido**, con su ejemplar: el puesto **427**,
`key_partners_hypothesis` contra `key_resources_hypothesis`, **dos ids de la misma
plantilla sobre contenidos que no se parecen**, que salio **D**.

**Y ahora estan leidos los DOS gemelos verdaderos de esos dos nodos:**

| nodo | su gemelo de verdad | id | puesto | clase |
|---|---|---|---:|:---:|
| `key_partners_hypothesis` | `partners_hypothesis_physical` | **misma plantilla** | 361 | **A** |
| `key_resources_hypothesis` | **`recursos_clave`** | **plantilla distinta**, de otro libro | **406** | **A** |

> **LO QUE ESTO LE ANADE A LA CALIBRACION, y es a favor del instrumento**: el
> molde **engano una vez** (el 427) **y no impidio cazar a ninguno de los dos
> reales.** Uno lo caza **por la plantilla** y el otro **a pesar de ella**, porque
> `recursos_clave` no comparte ni el sufijo ni el idioma.
>
> **El modo de fallo del eje de titulo es de PRECISION, no de RECALL**: mete un
> par de mas, no deja fuera a los buenos. **Eso es exactamente lo que se le
> pide a un eje que va a leerse entero.**

#### 413: el cuarto miembro del sub-puro, confirmado ahora POR LECTURA

**El puesto 394 lo trajo por el conteo; este lo confirma por el contenido.**

| | |
|---|---:|
| miembros | **4** |
| pares posibles | **6** |
| **leidos** | **5**, y **los cinco en A** (257, 334, 394, **413**, 787) |
| falta | **1**: el puesto **1030**, en la cola |

> **`gestion_multiples_term_sheets` repite con DOS miembros distintos**, y en los
> dos casos por el mismo mecanismo: **sincronizar los tiempos para que los term
> sheets lleguen juntos y no revelar con quien mas se habla.** La nomina de cuatro
> **ya no descansa en el contador: descansa en dos lecturas.**

> **Y un detalle que ensena a escribir listas de perdidas**: *nunca compartas el
> term sheet* **fue perdida aqui y NO lo fue en el 394**, porque
> `construccion_de_leverage` si la trae y `estrategia_competencia_vcs` no. **La
> misma instruccion es perdida o no segun el companero del par.** Las listas de
> perdidas no son del nodo: son del par.

### RELECTURA CONJUNTA DEL 530: la medicion, y el veredicto

**Encargada tras el puesto 863.** La pregunta era una sola: **el paso que la razon
del 530 cita, existe en los dos nodos o en uno solo.**

**MEDIDO, paso por paso y contra el grafo:**

| lo que la razon del 530 afirma | `estrategia_de_innovacion_y_tecnologia` | `estrategia_de_innovacion_de_producto` |
|---|---|---|
| identificar los mercados atractivos | **paso 1** | **no aparece** |
| **pesarlos contra las competencias propias** | **paso 2** | **NO APARECE, ni en pasos ni en resumen** |
| seleccionar las arenas donde ambos convergen | **paso 3** | **no**: dice *definir arenas estrategicas*, una linea |
| declarar que queda fuera del alcance | paso 4 | no |
| usar la estrategia como filtro en los gates | paso 5 | no |

> **Cinco de cinco pasos del primero estan ausentes del segundo.** Lo unico que el
> segundo tiene es **la palabra arenas**, en una linea, dentro de una lista de
> seis que va de objetivos a roadmap.

**EL ESQUELETO ES EL MISMO DEL 863**, verificado: madre con las arenas en una
linea, hijo con el metodo de seleccion completo.

> **VEREDICTO: el 530 pasa de A a D**, por la vara del banco 9.6.1, con correccion
> declarada dentro de su razon. **Es la segunda discrepancia del ejercicio y la
> segunda que se resuelve en conjunta.**

**LO QUE ESTO LE HACE A LA FAMILIA, contado del archivo:**

| | antes de hoy | ahora |
|---|---:|---:|
| pares leidos | 6 | **7** |
| en **A** | **6** | **5** |
| en **D** | 0 | **2** (530 y 863) |

> **La familia de la estrategia de innovacion pasa de *seis de seis en A* a
> **cinco y dos**, y el motivo de los dos sanos es el mismo: `y_tecnologia` **no
> es un hermano que repite, es el procedimiento de las arenas.** Con nueve
> lecturas pendientes, **la apuesta mas cargada del inventario se desinfla dos
> veces en un dia.**

---

### TANDA R24, VIGESIMA CIEGA: seis de seis

**Acumulado: 144 releidas, de las cuales 120 a ciegas. Discrepancias: UNA**, el
395. **El 530 no cuenta como discrepancia de tanda**: no salio de una relectura
ciega sino de una inconsistencia que el cribado destapo.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **421** | `fase_admit` contra `fase_admit_celebracion` | el **artefacto que memorializa** el momento, la **co-creacion** del producto con el cliente, y **que la celebracion no venga solo del vendedor**; del otro lado, **evitar el silencio posventa** | de **lector** |
| **426** | `usuarios_extremos_edge_cases` contra `usuarios_extremos_insights` | **documentar los hallazgos como activos creativos** para futuras iteraciones, y **evitar la ortodoxia** de las soluciones estandar cuando los extremos piden otra cosa | de **lector** |
| **432** | `cierre_sofisticacion_comprador` contra `riesgo_tecnicas_cierre_venta_compleja` | **medir la satisfaccion posventa** para detectar si el cierre esta danando la relacion, y **reemplazar el cierre por preguntas** que exploren necesidades reales | de **lector** |
| **434** | `business_intelligence_niveles_datos` contra `jerarquia_datos_scor` | **sumar datos externos** (tamano de mercado, indicadores economicos, comparaciones sectoriales) y **el control de accesos** por funcion; del otro lado, **el almacen de datos** y **automatizar la captura** | de **lector** |
| **439** | `get_out_of_the_building` contra `manifiesto_regla1_hechos_fuera_del_edificio` | **no hacer listas con todas las funciones que piden los clientes** y **documentar en el momento**; del otro lado, **prepararse para feedback impredecible y doloroso** y **experiencia de primera mano de cada parte del modelo** | de **lector** |
| **440** | `alineacion_motivacional_cofundadores` contra `compatibilidad_motivaciones_riqueza_control` | **la matriz de escenarios** para verificar consenso; del otro lado, **si ambos buscan control** anticipar el choque y resolverlo sin liderazgo compartido ambiguo, y **confiar de verdad en la capacidad** del socio antes de cederle autoridad | de **lector** |

#### 421: ADMIT DOBLADA, la SEGUNDA fase confirmada por lectura

**La medicion de la seccion 12 conto dos nodos en Admit. Esta relectura lo
confirma leyendo**, y con eso **son DOS las fases dobles confirmadas por lectura**,
Assess (puesto 373) y Admit.

> **Y trae algo que el otro nodo no tiene y que no es de Coleman-el-programa sino
> de Coleman-el-artesano**: **crear un artefacto fisico o digital que memorialice
> el momento**, certificado, mensaje personalizado o video. **Es EL MATERIAL DEL
> RITUAL.**
>
> **Anotado en el racimo de experiencia como avistamiento con destino ya
> conocido**: cuando la mesa consolide la fase Admit, **este artefacto es lo
> primero que hay que salvar**, porque es lo unico operativo que el nodo base no
> dice. Igual que la inmersion previa del brainstorming (puesto 834).

#### 432: TERCERA poda intra-Rackham, y la frontera sigue en pie

**Es la tercera fusion dentro del racimo del cierre que NO toca la frontera**, con
los puestos **248** y **274**.

> **Los dos nodos son de Rackham y del mismo lado.** La frontera de la seccion 9
> separa **el lado de Rackham** (no cierres, investiga) **del lado de Weinberg**
> (cierra), y **fusionar dentro de un lado no la borra: la limpia.**
>
> **Van tres podas intra-Rackham y cero cruces.** La frontera **no ha tenido que
> defenderse ni una vez**, que es la mejor senal que puede dar una frontera
> declarada.

#### 439: la familia de SALIR DEL EDIFICIO ya son cuatro nodos leidos

Con los puestos **840** (el genchi gembutsu por duplicado) y **849**
(`customer_development_modelo` contra `customer_discovery_get_out_of_building`),
**este es el tercer par de la misma zona y el tercero en A**.

> **Cuatro nodos del nucleo mandan salir a hablar con clientes**, dos con la
> palabra japonesa y dos con la inglesa, **y ninguno enlaza con ninguno.** Es la
> zona con mas repeticion confirmada y menos cableado del tramo.

### TANDA R25, VIGESIMOPRIMERA CIEGA: seis de seis

**Acumulado: 150 releidas, de las cuales 126 a ciegas. Discrepancias: UNA**, el
395. Perdidas propuestas, verificadas contra los dos nodos y repartidas por
bloques donde hacia falta.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **447** | `fase_acclimate_experiencia_cliente` contra `fase_acclimate_mapa_de_proceso` | **medir la aclimatacion** con encuestas rapidas, **celebrar los hitos**, e **identificar los momentos de friccion**; del otro lado, el **mapa visual que muestra en que etapa esta el cliente**, **detectar las senales silenciosas** de desconexion antes de la queja, y **partir lo complejo en pasos digeribles** | de **lector** |
| **450** | `estrategia_de_balas_de_plomo` contra `lead_bullets_no_silver_bullets` | **si el problema es de mercado o de producto**, **resistir la tentacion de buscar mercados alternativos**, y **comunicar al equipo que no hay atajos**; del otro lado, **no buscar asociaciones ni adquisiciones como solucion magica** | de **lector** |
| **451** | `validacion_hipotesis_ingresos` contra `verificar_modelo_ingresos` | el **valor de vida del cliente** para fijar precio y **si la rentabilidad mejora al crecer**; del otro lado, los **tres escenarios** optimista, esperado y pesimista, y el **cash burn contra la caja disponible** | de **lector** |
| **452** | `ab_testing_optimizacion` contra `split_testing` | **una sola**: la **significancia estadistica del 95%**. Lo demas viaja con el destejido, ver abajo | de **lector** |
| **453** | `formalizacion_acuerdo_equity` contra `reparto_inicial_equity` | las **implicaciones fiscales y legales** en tu mercado; del otro lado, **esperar a que la estrategia y el equipo se estabilicen** antes de cerrar el reparto, y usar una **plantilla estructurada** para la conversacion | de **lector** |
| **456** | `invitar_ia_a_todo` contra `principio_invitar_ia_siempre` | **repetir el ejercicio periodicamente porque las capacidades de la IA cambian** y **compartir los hallazgos con el equipo**; del otro lado, **iterar el prompt** hasta encontrar la forma optima para esa tarea | de **lector** |

#### 447: TERCERA fase doble de Coleman confirmada por lectura

**Con Assess (373) y Admit (421), van TRES fases dobles confirmadas leyendo**, y
esta es ademas **la unica de las tres que la medicion contaba como racimo de
TRES** (`fase_acclimate`, `fase_acclimate_experiencia_cliente`,
`fase_acclimate_mapa_de_proceso`).

> **Y las dos mitades se reparten el trabajo de forma limpia**: una mide y
> celebra, la otra dibuja el mapa y vigila el silencio. **No es una copia peor de
> la otra: son dos aportes distintos sobre el mismo hueso**, mapear el recorrido y
> comunicar por hitos.
>
> **Lo que esto le anade al tratamiento de la seccion 12**: de las ocho fases,
> **tres ya tienen su duplicacion confirmada por lectura y no solo por conteo.**
> El paso 3 del tratamiento, consolidar fase por fase, **ya tiene tres fases con
> la evidencia hecha.**

#### 452: `ab_testing_optimizacion` es el UNDECIMO ejemplar de la CURA ACOPLADA

**Consultada la ficha antes de registrar, como manda el dictado:**

| eje | veredicto |
|---|---|
| **la ficha de costuras** | **CONFIRMADA**, quince pasos, corte **10**, **TRES NARRACIONES**: landing page (1 a 5), metrica unica (6 a 10) y canal nucleo (11 a 15), con el tercer bloque en segunda persona mientras los dos primeros van en infinitivo |
| **el intra** | **A** en este puesto 452, gemelo `split_testing` |

> **Costurada confirmada con gemelo declarado: CURA ACOPLADA.** **Undecimo
> ejemplar y OCTAVO del tipo caro.** Anotado en la ficha.
>
> **Y su cura ya estaba emparejada con otra**: la ficha dice que este nodo y
> `split_testing_experimentos_ab` (el octavo ejemplar, puesto 374) **se leen
> juntos porque su destejido probablemente converge en uno.** **Ahora son TRES
> nodos de A/B en el mismo acto**: los dos costurados y `split_testing`, que
> repite con los dos.

**SU PUESTO EN LA COLA, con la regla recien adjudicada: EN COLA, NO CONGELADO.**

> **La POSICION dice bloquea**: el solape (definir variaciones, partir el trafico,
> medir conversion, confianza estadistica) **toca el bloque 1 a 5 Y el bloque 11 a
> 15**, o sea que cruza junturas.
>
> **La DEPENDENCIA dice que se emite, y manda ella**: sobreviva la narracion que
> sobreviva, **lo que quede seguira siendo un nodo de pruebas A/B**, y
> `split_testing` es un nodo de pruebas A/B entero. **El veredicto es
> invariante.**

**LA PERDIDA, REPARTIDA y verificada como pedia el dictado:**

| se salva en ESTA fusion | viaja con el destejido |
|---|---|
| de `split_testing`: la **significancia estadistica superior al 95%**, que el otro solo nombra como *confianza estadistica* sin cifra | **la saturacion** (paso 15) y **el canal nucleo** (paso 11), los dos del **bloque de Weinberg** |
| | |

> **Verificado antes de listarlo**: los dos que el dictado proponia como perdida,
> saturacion y canal nucleo, **estan en el tercer bloque**, el que la cirugia se
> lleva. **No se pierden aqui.** Quinto ejemplar de la figura del banco 9.11.

#### 456: NO es par interno del racimo de la IA, y lo traigo

**El dictado lo daba como par interno del racimo IA-supervision. Verificado contra
la nomina: no lo es.**

| | |
|---|---|
| la nomina del racimo (seccion 11) | **ocho miembros**, y **ninguno de los dos de este par** esta entre ellos |
| pares en la cola entre este par y los ocho | **UNO**: el puesto **1517**, `invitar_ia_a_todo` contra `jagged_frontier_ia`, **pendiente** |

> **Lo que si es**: **la pareja del PRINCIPIO 1 de Mollick**, invitar a la IA a
> todo, **adyacente al racimo pero fuera de su nomina.** Su asunto es *pruebala en
> todo*; el del racimo es *donde tiene que mirar una persona*. **Son la puerta y
> el freno del mismo libro, no el mismo tema.**
>
> **Y su forma es exactamente la de la pareja de las alucinaciones** (puesto 363):
> **un par interno que repite, adyacente al racimo, con UN solo puesto de la cola
> que decide si entra.** Alli era el 1478; aqui es el **1517**. **Quedan los dos
> anotados como condiciones vivas del racimo**, y ninguno de los dos es de los
> cuatro cruzadores que deciden si el racimo se parte.

### TANDA R26, VIGESIMOSEGUNDA CIEGA: seis de seis

**Acumulado: 156 releidas, de las cuales 132 a ciegas. Discrepancias: UNA**, el
395. **Las seis razones de esta tanda pasaron ademas por el barrido de razones**,
y la del 474 era una de las treinta y ocho.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **460** | `estrategia_de_innovacion_arenas` contra `estrategia_de_innovacion_de_producto` | los **buckets estrategicos de recursos**, el **compromiso con la vision de largo plazo** mas alla del ano en curso, y **vincular explicitamente las metas de innovacion con las del negocio** | de **lector** |
| **462** | `crowdfunding_legal_exemptions_jobs_act` contra `equity_crowdfunding` | **determinar si lo que ofreces es un security o no**, y **elegir portal autorizado** con las divulgaciones de la SEC si vas por el Titulo III; del otro lado, **los sindicatos de AngelList** | de **lector** |
| **463** | `obtencion_compromiso` contra `obtencion_de_compromiso` | **preguntar si falta algo por aclarar** antes de cerrar, **resumir los beneficios** discutidos, y **pedir el compromiso mas alto que el cliente pueda dar de verdad**; del otro lado, **medir el exito por avances y no por pedidos** | de **lector** |
| **467** | `diseno_experimentos_hipotesis` contra `diseno_experimentos_pass_fail` | el **criterio numerico de exito fijado de antemano**, **extender la duracion** lo suficiente para no confundir un maximo local con el global, y **registrar los insights cualitativos** y no solo el pasa o no pasa | de **lector** |
| **468** | `gestion_portafolio_formal` contra `revision_portafolio_periodica` | la **poda inicial** de los mas debiles y los **buckets con ranking dentro de cada uno**; del otro lado, el **panorama visual** de todos los proyectos y **anotar las decisiones** | de **lector** |
| **474** | `milk_run_deliveries` contra `programacion_entregas_delivery_scheduling` | **medir el ahorro tras implementar** la ruta consolidada; del otro lado, **decidir entre ubicaciones de producto unico o centros de distribucion** | de **lector** |

#### UNA PERDIDA DICTADA QUE NO LO ES

> **En el 463, el *objetivo de avance realista* esta en LOS DOS.** Es el paso 1 de
> `obtencion_compromiso` (*define para cada llamada un objetivo de avance
> realista*) y el paso 4 de `obtencion_de_compromiso` (*propon el siguiente paso
> concreto y realista*). **No se pierde.** Las otras dos del dictado se sostienen.

#### 474: la A se sostiene POR CONTENIDO, y su razon era una de las treinta y ocho

**Verificado paso por paso**: `milk_run_deliveries` **repite tres de los cinco
pasos de la madre** (el EOQ por ubicacion, la eleccion entre matriz de ahorros y
asignacion generalizada, y el diseno de la ruta consolidada), **y no solo
desarrolla el paso 3.**

> **Por la vara: no trae un procedimiento que la madre no tenga, trae la madre
> otra vez con una rama ampliada. REPITE.** La A se sostiene, y ahora la sostiene
> el contenido y no la ausencia de arista, que era lo que decia su apertura vieja.

#### 463: ids con y sin preposicion, dentro del racimo del avance

`obtencion_compromiso` contra `obtencion_de_compromiso`: **el mismo nombre con y
sin el *de***. **Va al monton de la DECISION 4**, y es el tercero que este cribado
manda alli tras el 883 y el 941.

> **Pero con una diferencia que hay que decir**: los dos son **miembros del racimo
> del cierre**, y este par es **la cuarta poda intra-Rackham** tras 248, 274 y
> 432. **La frontera con el lado de Weinberg sigue sin tocarse.**

#### 468: el cruce portafolio-puertas vuelve, y ahora desde dentro del portafolio

**El cruce 2 de la seccion 13** enfrentaba un nodo de puertas contra uno de
portafolio. **Este par es de dos nodos de portafolio**, y los dos integran los
gates dentro de su procedimiento.

> **Lo que anade al cruce**: la familia del portafolio **tambien repite puertas
> adentro**, asi que la mesa 1 no puede resolver el cruce mirando solo la nomina
> de las puertas. **Son dos familias que repiten cada una por su lado y ademas se
> tocan.**

#### 462: CANDIDATO A MARCO-PAIS, verificado en sus tres casas

**El nodo cablea la regulacion de un solo pais y hay que decir donde condiciona y
donde no**, con el mismo procedimiento que se uso con las EAR:

| casa | que es | condiciona por pais? |
|---|---|---|
| **`titulo_concepto`** | *Crowdfunding y Exenciones Legales (JOBS Act)* | **NO**: nombra la ley estadounidense sin decir que lo es |
| **`resumen_teorico`** | *vender una participacion exige registrarla ante la SEC, salvo que aplique una exencion; la JOBS Act define tres marcos: 506(b), 506(c) y Titulo III* | **NO**: nombra SEC y JOBS Act **sin ninguna clausula de jurisdiccion** |
| **`pasos_accionables`** | los cinco pasos mandan elegir entre 506(b), 506(c) y Titulo III, y **elegir un portal autorizado con las divulgaciones que exige la SEC** | **NO**: cero condicion previa, igual que las EAR |

> **VEREDICTO DE LA FIGURA: es marco-pais CABLEADO, del tipo duro.** A diferencia
> de Magnuson-Moss, que al menos condiciona por **destino**, y de las EAR, que
> condicionan por **origen**, **este nodo no condiciona por nada**: da por supuesto
> que el lector levanta capital bajo la SEC.
>
> **Y su gemelo, `equity_crowdfunding`, hace exactamente lo mismo**: nombra la SEC
> en su titulo y en tres de sus cuatro pasos, sin jurisdiccion. **La pareja entera
> es marco-pais.**
>
> **Lo que esto le anade al remedio**: si los dos se funden, **el superviviente
> hereda el problema completo**. La fusion y el reencuadre **son el mismo acto**,
> como en la cura acoplada, y el contramodelo ya existe:
> `seguridad_trabajadores_jovenes`, que universaliza dentro del paso.

**Y AL CENSO DE HERRAMIENTAS, con evidencia:**

> **`AngelList`** queda registrada, citada en `equity_crowdfunding` **paso 4**
> (*si usas una plataforma como AngelList, entiende como funcionan los grupos de
> inversionistas o syndicates*) **y en su resumen**. **Estado: VIVA**, verificada
> el 13 ago 2026. **Es el nombre propio numero trece del censo**, y el primero que
> entra por el eje intra-dominio en vez de por la franja o las costuras.

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

## 11. RACIMO NUEVO: LA SUPERVISION DE LA IA

> **SUBIO A RACIMO EL 12 ago 2026, en la relectura R13.** Lo que sigue es el texto
> del candidato tal como se escribio, **sin retocar**, y debajo lo que cambio.
>
> **La nomina paso de CUATRO a OCHO miembros** y los pares leidos de dos a cuatro,
> los cuatro en **A**. **La forma no mejoro**: una sola arista interna entre ocho.
>
> **Y la condicion que este mismo texto puso NO se cumplio como estaba escrita**:
> el par que cruzaria las dos mitades originales sigue pendiente. **Lo que subio
> el racimo fue la evidencia agregada, no esa condicion.** Todo medido y
> declarado en la seccion 8, tanda R13.

### LA NOMINA VIGENTE: OCHO miembros

| nodo | pasos |
|---|---:|
| `human_in_the_loop_ia` | 4 |
| `principio_humano_en_el_loop` | 4 |
| `comprension_capacidades_limitaciones_ia` | 5 |
| `jagged_frontier_ia` | 4 |
| `mitigar_falling_asleep_wheel` | 4 |
| `riesgo_sobredependencia_ia` | 4 |
| `alineacion_etica_ia_negocio` | 5 |
| `comprender_alineacion_etica_ia` | 4 |

**28 pares posibles, 13 en la cola, CUATRO leidos y los cuatro en A** (166, 177,
293, 692). **Nueve pendientes de cola y quince que nunca entraron.** **Una sola
arista interna**, entre `jagged_frontier_ia` y `riesgo_sobredependencia_ia`.

### LAS CONDICIONES VIVAS DE ESTE RACIMO

**Escritas aqui dentro para que no vivan solo en una razon de veredicto.** Son
cinco puestos concretos y cada uno decide algo distinto:

| puesto | que decide |
|---:|---|
| **1211** | `comprension_capacidades_limitaciones_ia` contra `principio_humano_en_el_loop`: **cruza las dos mitades originales** |
| **1239** | `comprension_capacidades_limitaciones_ia` contra `human_in_the_loop_ia`: **cruza** |
| **1339** | `human_in_the_loop_ia` contra `jagged_frontier_ia`: **cruza** |
| **1451** | `jagged_frontier_ia` contra `principio_humano_en_el_loop`: **cruza** |
| **1478** | `deteccion_alucinaciones_ia` contra `principio_humano_en_el_loop`: **decide la ABSORCION** de la pareja de alucinaciones, hoy adyacente y no incluida |

> **Los cuatro primeros prueban o desmienten que las dos mitades originales sean
> una sola familia.** El racimo subio por evidencia agregada, no porque eso este
> probado. **Si los cuatro salieran D, este racimo se parte en dos y hay que
> decirlo.**
>
> **El quinto decide el tamano**: con el 1478 en A la nomina pasa de ocho a diez.
>
> **Precision del 13 ago 2026, relectura R19**: el puesto **363**, el par INTERNO
> de esa pareja adyacente, **se releyo a ciegas y sostuvo su A**. La pareja se
> fusiona entre si **decida lo que decida el 1478**; lo unico que ese puesto
> decide es **si el superviviente entra al racimo o se queda al lado**. Son dos
> preguntas distintas y conviene no mezclarlas.

**EL TEXTO ORIGINAL DEL CANDIDATO, del 11 ago 2026:**

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
| nodos de CANAL (la sub-serie de los seis medios de comunicacion) | ~~4~~ **7** |

### Las ocho fases, una por una

| fase | nodos vivos | cuales |
|---|---:|---|
| **Assess** | **3** | `fase_assess`, `fase_assess_ciclo_cliente`, `fase_assess_experiencia_cliente` |
| | | **y ademas ASSESS ESTA DOBLADA POR LA OTRA SERIE**, ver abajo |
| **Admit** | **2** | `fase_admit`, `fase_admit_celebracion` |
| Affirm | **1** | `fase_affirm_buyers_remorse` |
| **Activate** | **2** | `fase_activate`, `fase_activate_primera_impresion` |
| **Acclimate** | **3** | `fase_acclimate`, `fase_acclimate_experiencia_cliente`, `fase_acclimate_mapa_de_proceso` |
| **Accomplish** | **2** | `fase_accomplish`, `fase_accomplish_experiencia_cliente` |
| **Adopt** | **2** | `fase_adopt`, `fase_adopt_ciclo_cliente` |
| Advocate | **1** | `advocacy_customer_journey` |

#### ASSESS DOBLADA: la fase que aparece en las dos series a la vez

**Encontrada el 12 ago 2026 al contar con el script, y a ojo no se veia.**

| nodo | como trata el instrumento de las seis vias |
|---|---|
| `fase_assess_ciclo_cliente` | lo lleva **DENTRO**, en su paso 5: *disena al menos una mejora inmediata usando uno de los seis canales de comunicacion* |
| `seis_canales_comunicacion_assess` | lo tiene con **CASA PROPIA**: es ese mismo uso convertido en nodo entero |

> **Y no hay arista entre los dos**, verificado resolviendo a nodo vivo. **Es la
> DUPLICACION CRUZADA de la seccion 15.3 aplicada a una serie**: el mismo material
> absorbido por un lado y desarrollado por el otro, sin camino entre ellos.
>
> **Adopt tiene la mitad de la figura** (`fase_adopt_ciclo_cliente` lleva los seis
> canales dentro de su paso 2) **pero no tiene nodo de canal propio**, o sea que
> **Assess es la unica fase doblada por las DOS series a la vez**: tres nodos de
> fase y uno de canal, cuatro nodos para un paso.
>
> **Lo que esto le anade a la candidatura**: el tratamiento de serie declarada
> **tiene que decidir las dos series juntas**, porque en Assess se tocan. Si se
> consolidan las fases primero, el nodo de canal de Assess queda colgando de un
> nodo que ya no existe.

> **CONFIRMADO A CIEGAS el 13 ago 2026, relectura R20, puesto 373.** El par
> `fase_assess_ciclo_cliente` contra `fase_assess_experiencia_cliente` **repite y
> aguanta la relectura**, asi que **los tres nodos de fase de Assess siguen en
> pie** y con ellos la cuenta de cuatro nodos para un paso.
>
> **Y de ahi sale la EVIDENCIA VIVA del orden del tratamiento**: el paso 5 de
> `fase_assess_ciclo_cliente` **manda usar uno de los seis canales**, o sea que
> **la serie de los medios esta instanciada DENTRO de la serie de las fases**,
> operante y no como nota. **Ese es el motivo por el que los medios van antes que
> las fases** en la forma del tratamiento: consolidar las fases primero seria
> consolidar sobre un texto que la otra serie va a reescribir.

> **SEIS DE LAS OCHO FASES ESTAN DOBLADAS O TRIPLICADAS.** Solo Affirm y Advocate
> tienen un nodo. **Dieciseis nodos para ocho pasos.**

### TRES HALLAZGOS QUE LA MEDICION DESTAPA

> **CONFIRMADO A CIEGAS EL 12 ago 2026, relectura R16, puesto 326.** Y con las
> dos piezas que tienen que VIAJAR al programa unico, porque ninguna esta en el
> otro nodo y las dos son operativas:
>
> | de que nodo | que dice |
> |---|---|
> | `fases_de_retencion_de_clientes` | **priorizar Affirm y Activate**, las dos fases mas descuidadas |
> | `ocho_fases_experiencia_cliente` | **detectar en que fase se atascan** los clientes y **armar el plan** para moverlos |
>
> **Un programa unico que las pierda deja la serie sin punto de entrada**, porque
> Affirm y Activate son justamente donde la serie dice que esta el problema.
>
> **Y EL SUPERVIVIENTE YA TIENE NOMBRE, por el DESEMPATE POR CABLEADO del banco
> 9.8**: **`ocho_fases_experiencia_cliente`**. Los dos programas dicen
> practicamente lo mismo, asi que el contenido no desempata; **el grafo si**. Ese
> nodo enlaza a **las ocho fases, al otro programa, a la serie de los seis medios
> y a la aplicacion de la bienvenida**, medido en el puesto 815. **Fundir hacia el
> es gratis; fundir hacia el otro obliga a reconstruir doce aristas.**

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
> y `seis_herramientas_comunicacion_celebracion`.
>
> **CORRECCION DECLARADA DEL 12 ago 2026, contada con `scripts/contar_nombre.py`:
> esa cifra de CUATRO era mia y estaba mal. Son SIETE.** La conte a ojo en el
> puesto 669 y dio cuatro, la volvi a contar a ojo en el 719 y dio cinco, y el
> contador dio **siete**. Faltaban `estrategia_multicanal_bienvenida`, que aplica
> las mismas seis vias a la bienvenida posterior a la compra **sin llevar la
> palabra en el identificador**, y los dos nodos de fase que llevan el instrumento
> **metido dentro de un paso**, `fase_assess_ciclo_cliente` y
> `fase_adopt_ciclo_cliente`. **Es una serie de canales
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

---

## 13. LOS CRUCES: donde dos frentes tocan el mismo nodo

**Seccion abierta el 11 ago 2026.** Hasta ahora los cruces se anotaban dentro de
la razon del veredicto que los encontraba, y **eso los esconde**: quien lea el
plan por frentes no los ve.

> **UN CRUCE es un nodo o una familia que dos frentes distintos van a tocar.** Y
> la regla que los gobierna es la misma que la del **toque unico** del banco 9.4,
> subida un nivel: **si dos frentes tocan lo mismo, o se resuelven juntos, o el
> segundo recompone lo que hizo el primero.**

### CRUCE 1: el racimo del brainstorming contra la DECISION DE FUENTE de Mollick

**Verificado contra el grafo.** El racimo censado `Las reglas del brainstorming`
tiene **cuatro miembros, y los cuatro declaran libros distintos**:

| miembro | fuente |
|---|---|
| `brainstorming_efectivo` | *Change by Design* (Tim Brown, IDEO) |
| **`brainstorming_divergente`** | ***Change by Design* (Tim Brown) mas *Co-Intelligence* (Mollick)** |
| `reglas_brainstorming` | *Business Model Generation* (Osterwalder) |
| `brainstorming` | *Juran's Quality Handbook* (Defeo) |

> **Cuatro nodos, cuatro libros.** Y **uno de los cuatro es el injerto de Mollick**
> que la ficha de costuras confirmo: `brainstorming_divergente` lleva **el taller
> de Tim Brown en sus pasos 1 a 4 y la version con IA de Mollick en los 5 a 8**,
> con el paso 3 volviendo calcado en el 7.

**EL CRUCE, y es de los que recomponen:**

> **La decision de fuente de Mollick manda DESTEJER ese nodo**, separando el
> bloque de IA. **Y el destejido cambia la aritmetica del racimo**, porque lo que
> queda despues **ya no es el mismo nodo**.
>
> **Lo que queda es un taller de Tim Brown. Y `brainstorming_efectivo` TAMBIEN es
> un taller de Tim Brown.** O sea que **el destejido puede convertir un racimo de
> cuatro libros en un duplicado limpio de dos nodos del mismo libro**, que es una
> pregunta mucho mas facil que la de ahora.

**El orden importa y va en los dos sentidos:**

| si se hace primero | que pasa |
|---|---|
| **el racimo** | se decide la arquitectura de cuatro nodos **con uno de ellos todavia costurado**, o sea sobre un miembro que va a cambiar |
| **la decision de fuente** | el racimo llega a la mesa **con el nodo ya limpio**, y quiza con un duplicado obvio que antes estaba tapado por el bloque de IA |

> **RECOMENDACION, y no es adjudicacion: la decision de fuente PRIMERO.** Es mas
> barata (es una pasada por libro, no una mesa), y **deja el racimo mejor
> planteado en vez de peor.** Lo contrario obliga a rehacer la mesa.

> **APROBADO COMO ORDEN DEL PLAN, 11 ago 2026.** La recomendacion deja de ser
> recomendacion: **el cruce se ejecuta FUENTE PRIMERO**, con el motivo que ya
> estaba escrito, **el destejido convierte un racimo de cuatro libros en un
> duplicado de dos nodos del mismo libro.**
>
> **Y eso fija un precedente de orden para los cruces que vengan**: cuando un
> frente **cambia lo que un nodo dice** y otro frente **decide cuantos nodos
> hacen falta**, **primero va el que cambia lo que dicen.** Decidir cuantos
> hacen falta sobre un texto que va a cambiar es decidir sobre lo que ya no
> sera.

### CRUCE 2: el racimo del Portafolio contra el racimo de las puertas del Stage-Gate

**Ya estaba encontrado, en el puesto 488, pero vivia dentro de una razon de
veredicto. Se sube aqui.**

`gestion_de_portafolio_gates_go_kill` esta censado en el racimo
`Portafolio: revisar, podar, reasignar`, y `sistema_gates_go_kill` pertenece al
racimo nuevo de **las puertas del Stage-Gate** (seis miembros, seccion 1).
**El par entre los dos REPITE.**

> **Los dos racimos se tocan en ese par**, asi que **la mesa de las puertas tiene
> que mirar tambien la nomina del portafolio antes de decidir cuantos nodos quiere
> el catalogo**. Si no, decide sobre seis cuando en realidad hay siete en juego.

> **AMPLIACION del 13 ago 2026, relectura R19, y cambia el ORDEN del arreglo.**
> El puesto **356** mide el mismo nodo por dentro: **`sistema_gates_go_kill`
> tambien repite con `estructura_gates`, que es de su PROPIO racimo.**
>
> **El nodo que une los dos racimos esta duplicado dentro del suyo.** Si la mesa
> del portafolio lo toca primero, decide sobre un nodo que la mesa de las puertas
> va a fusionar despues. **Orden recomendado: primero se cierra la familia de las
> puertas, y con el superviviente en la mano se mira el cruce con el portafolio.**

### LA REGLA QUE ESTA SECCION FIJA

> **Todo cruce se anota AQUI ademas de en su veredicto.** Un cruce escrito solo
> dentro de una razon **existe para quien lee los veredictos en orden y no existe
> para quien lee el plan por frentes**, que es justamente quien lo necesita.
>
> **Y todo cruce lleva su orden recomendado con el motivo**, porque *resolverlos
> juntos* casi nunca significa a la vez: significa **en el orden que no obliga a
> rehacer nada.**

---

## 14. REMEDICION DE LOS RACIMOS PRE-REGLA

**Aprobada el 11 ago 2026 y ejecutada el mismo dia.** Los racimos declarados en
los puestos **201, 203, 246 y 360** se declararon **antes de que existiera la
regla de la arista** de la seccion 3, asi que **su forma nunca se midio: se
supuso.** Dos de ellos ya habian cambiado de lectura al remedirlos por accidente.

**Metodo: el de la seccion 6**, aristas resueltas a nodo vivo caminando
`ids_alias`, umbrales identicos.

> **Y la remedicion destapo un defecto anterior al de la arista: DOS de los cuatro
> se declararon con la NOMINA INCOMPLETA.** El 246 se declaro con cuatro miembros
> y son **seis**; el 360 con tres y son **siete**. **Los miembros que faltaban
> aparecieron despues, en veredictos posteriores, y nadie volvio a la declaracion
> a sumarlos.**

### El resultado, racimo por racimo

| racimo | n | aristas | forma medida | aislados |
|---|---:|---:|---|---|
| **201** el control de la junta | 3 | 1 | **MIXTO**, grado maximo 1 | `board_control_etapas_tardias` |
| **203** el capital de trabajo | **4** | 2 | **CENTRO ENLAZADO** | `dso_dpo_gestion_capital_trabajo` |
| **246** el reparto de equity | **6** | 7 | **CENTRO ENLAZADO** | **ninguno** |
| **360** el lienzo de propuesta de valor | **7** | 7 | **CENTRO ENLAZADO** | `customer_profile_value_map`, `desarrollo_value_proposition_usp` |

### 203: SEPTIMO GEMELO SIN CASA, y la lectura vieja estaba del reves

**La razon del puesto 203 dice**: *tres nodos, el nodo conjunto mas uno por cada
mitad*, con `dso_dpo_gestion_capital_trabajo` de conjunto.

> **Medido: son CUATRO y el conjunto es OTRO.** `ciclo_de_conversion_de_efectivo`
> **enlaza con las dos mitades**, `gestion_dso` y `gestion_cuentas_por_pagar_dpo`,
> y **`dso_dpo_gestion_capital_trabajo` no toca a ninguno de los tres.**
>
> **CENTRO SANO CON GEMELO SIN CASA, y es el SEPTIMO candidato.** El nodo que yo
> llame conjunto **es el gemelo**.

**Y su lectura de familia cambia de sitio**: no hay que decidir la arquitectura de
tres, **hay que resolver uno**. Es de las baratas.

### 246: la mejor conectada de las cuatro, y sin gemelo

**Con la nomina completa de seis**, `criterios_equity_split` **toca a los otros
CINCO** y **no hay ni un aislado**. Es **la unica de las cuatro remedidas sin
gemelo que resolver**.

> **Eso cambia lo que la mesa tiene que hacer con ella**: la familia **ya esta
> presidida**. Lo que queda es podar de las hijas lo que el centro ya dice, que es
> trabajo de redactor. **Sus seis pares leidos dan A, B, C y A, A**, o sea que es
> **MEZCLADA**, pero **mezclada con centro**, que es la version facil.

### 360: se confirma, y con DOS gemelos

**Con la nomina completa de siete**, `value_proposition_canvas` es el centro con
grado 4, y **hay DOS aislados**: `customer_profile_value_map` y
`desarrollo_value_proposition_usp`. **Coincide con lo que el barrido de la
seccion 6 ya habia medido**, y con la correccion que la seccion 5 recibio en el
puesto 459.

### 201: el PRIMER MEZCLADO COMPLETO, y no tiene centro

**Tres miembros, tres pares posibles, LOS TRES LEIDOS, cero pendientes. Y las
clases son B, C y D: tres pares, tres clases distintas.**

> **Es el espejo exacto del racimo PURO del banco 9.5**: la condicion dura se
> cumple (todo leido, nada pendiente) **y el resultado es el contrario**. **Ni un
> solo par repite.**
>
> **Su forma tampoco ayuda**: grado maximo 1, un aislado, **no hay centro que
> presida.** Dos nodos enlazados entre si y un tercero suelto.
>
> **MEZCLADO COMPLETO SIN CENTRO es la categoria mas cara que hay**: hay que
> decidir la arquitectura **y** no hay ningun nodo que se pueda dejar de pie por
> defecto. **Va entero a la mesa.**

### LO QUE LA REMEDICION DEJA COMO REGLA

> **1. Ningun racimo va a la mesa sin forma medida.** La forma no se supone: se
> cuenta. **Dos de los cuatro tenian la forma mal supuesta y uno la tenia del
> reves.**
>
> **2. La nomina de un racimo declarado se RE-CUENTA antes de usarla.** Dos de los
> cuatro habian crecido en veredictos posteriores **sin que nadie volviera a la
> declaracion**. Un racimo declarado con cuatro y medido con seis **da otra
> forma**.
>
> **3. La etiqueta PURO o MEZCLADO se pone con los pares leidos y los pendientes
> delante**, y **solo dos de los cuatro tienen la cuenta cerrada**: el 201 con tres
> de tres, y ninguno mas. **El 203 tiene dos pares sin leer, el 246 cinco y el 360
> tres**: ninguno de esos puede declararse ni puro ni mezclado-completo todavia.

---

## 15. EL TRAMO 568 a 645: la regla de la arista se parte en dos

**Setenta y ocho pares leidos, los setenta y ocho del nucleo.** Es el tramo que
mas le ha exigido a la regla de la seccion 3, y la regla salio de el **partida en
sus dos mitades, con una de ellas puesta a prueba y todavia sin veredicto.**

### CHECKPOINT DE LOS 600, contado antes de escribir

| | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **global al puesto 600** | **600** | 215 | 44 | 4 | 337 | **35,8%** |
| **nucleo al puesto 600** | **445** | 214 | 42 | 4 | 185 | **48,1%** |

**Y el acumulado al cierre de este tramo, que es la cifra de lectura:**

| | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **global** | **645 de 3.388** | 233 | 48 | 4 | 360 | **36,1%** |
| **nucleo** | **490** | 232 | 46 | 4 | 208 | **47,3%** |
| tramo 568 a 645 | 78 | 28 | 9 | 0 | 41 | 35,9% |

> **La tasa de A del nucleo lleva veinte puestos moviendose menos de un punto**
> (49,5% en el 567, 48,1% en el 600, 47,3% en el 645). **Baja despacio y no rebota.**

### 15.1 LA MITAD QUE NUNCA HABIA DISPARADO: con arista y aun asi duplicacion

**La regla de la seccion 3 tiene dos mitades y hasta este tramo solo se habia
usado una.** La segunda dice que **una madre que RE-DESARROLLA al mismo grano que
su hijo es duplicacion aunque la arista exista.** Nunca habia disparado. En este
tramo disparo **tres veces**:

| puesto | el par | la arista | por que igual repite |
|---:|---|:---:|---|
| **570** | `desarrollo_presentacion_problema` contra `presentacion_problema_tres_columnas` | **en los dos sentidos** | la madre recorre las tres columnas en sus pasos 2, 3 y 4 **con el mismo detalle** que el hijo |
| **614** | `alineacion_cadena_estrategia_negocio` contra `definicion_alineacion_cadena_suministro` | **en los dos sentidos** | ninguno resume al otro: los dos disenan la cadena entera |
| **635** | `customer_development_modelo` contra `customer_discovery` | **en los dos sentidos** | mismo orden, mismo grano, mismas cuatro ordenes |

> **La arista no absuelve.** Lo que absuelve es que **uno de los dos sea un
> resumen**. Cuando los dos textos son del mismo tamano de grano, la arista solo
> documenta la duplicacion en vez de resolverla.

### 15.2 LA MITAD QUE SE PUSO A PRUEBA: HERMANOS ENLAZADOS MENOS UNO

**Figura nueva, y va con una pregunta abierta para el auditor.** Aparecio en el
puesto **581** y se repitio en el **633**.

> **Cuando una madre enlaza a los hijos de sus OTROS pasos y no al de este, la
> arista que falta parece una omision del grafo y no una prueba de duplicacion.**

| puesto | la madre | hijos con arista | el hijo sin arista |
|---:|---|:---:|---|
| **581** | `cumplimiento_magnuson_moss` | **4 de 5** | `prohibicion_tie_in_sales` |
| **633** | `proceso_diseno_modelo_negocio_5_fases` | **2 de 5** | `fase_diseno_prototipado_modelos` |

> **CORRECCION DECLARADA DEL 12 ago 2026, y esta tabla es la que estaba mal.**
> La proporcion del **581** es **3 de 5**, no cuatro de cinco, y la del **633**
> **no se cuenta por radios porque esa familia esta cableada en CADENA**: son
> cinco de cinco. **El 633 paso a D.** Todo medido y explicado en la **seccion 16**.

**Y aqui esta la incoherencia, declarada en vez de escondida:**

> **El 581 quedo en D PROVISIONAL** porque fusionar romperia una familia sana de
> cinco radios. **El 633 quedo en A**, aplicando la regla literal, **porque su
> misma silueta con su misma madre ya habia dado A en el puesto 395** y el archivo
> no puede contradecirse solo.
>
> **Los dos no pueden estar bien.** Si el auditor acepta el refinamiento, se
> releen juntos el **395**, el **581** y el **633**, y hay que fijar **desde que
> proporcion de hermanos enlazados la arista que falta deja de acusar**: el 581
> esta en cuatro de cinco y el 633 en dos de cinco, y no es lo mismo.

### 15.3 DUPLICACION CRUZADA: cada uno absorbe lo que el otro enlaza

**Figura nueva, dos ejemplares en cuatro puestos de distancia.**

| puesto | uno lo trae DENTRO | el otro lo ENLAZA |
|---:|---|---|
| **573** | `colaboracion_cadena_suministro` trae el diagnostico del efecto latigo en sus pasos 1 y 2 | `compartir_datos_cadena_suministro` apunta a `diagnostico_efecto_latigo` |
| **574** | `gestion_portafolio_formal` trae los Strategic Buckets en su paso 4 | `portfolio_management` apunta a `metodo_strategic_buckets` |

> **El mismo material vive dos veces con dos tratamientos opuestos**: pegado por
> dentro en un nodo y colgado por fuera en el otro. **La mesa tiene que elegir uno
> de los dos tratamientos para el catalogo entero**, porque hoy el lector recibe
> respuestas distintas segun por cual entre.

Y el **568** trae la version extrema: **una madre que no enlaza a NINGUNO de sus
dos hijos, y los dos hijos enlazados entre si.**

### 15.4 UN NODO AVERIADO CONTAMINA TODOS SUS PARES

**Regla de metodo, encontrada en el 592 y confirmada en el 599.**

> **Un veredicto emitido contra un texto que va a cambiar no vale.** Por el
> **TOQUE UNICO del banco 9.4**, cuando uno de los dos nodos es costura
> confirmada, **el par se lee DESPUES del arreglo interno, no antes.**

| puesto | quien esta averiado | que dice la ficha de costuras |
|---:|---|---|
| **592** | `producto_minimo_viable` | **el emblema**: 22 pasos y 10 condiciones para cinco cosas, con la misma orden repetida cuatro veces |
| **599** | **los DOS** | `key_partners_hypothesis` es **triple**; `asociaciones_clave` son **tres bloques de dos libros**, con un libro declarado dos veces en el campo `fuente` |

### 15.5 LAS NOMINAS ESTAN CORTADAS, y se puede medir cuanto

**Tres familias medidas contra su racimo censado, y las tres salen cortas.**

| familia | nodos vivos que la nombran | en la nomina censada | pares en cola | leidos | pendientes |
|---|---:|---:|---:|---:|---:|
| **el pivote** (puesto 591) | **19** | racimo de otra puerta | 28 | 4 | 24 |
| **customer discovery** (puesto 615) | **16** | **7** | 32 | 14 | 18 |
| **la sucesion del CEO** (puesto 618) | **11** | **sin censar** | 21 | 6 | 15 |

**Y el corte no es arbitrario, es peor: corta por el medio de un par que repite.**

> **Puesto 598**: la nomina del racimo `Pivotar o proceder` tiene un nodo de la
> puerta de **validacion** y deja fuera uno de la puerta de **descubrimiento**,
> con el que el puesto 268 ya emparejo en **A**.
>
> **Puesto 611**: `customer_discovery` esta en la nomina y
> `customer_discovery_introduccion` no, **y el par repite**.

**La familia de la sucesion trae ademas la firma del racimo del cierre**: diez de
once son de *The Founder's Dilemmas*, **uno es forastero** de *The Hard Thing
About Hard Things*, y un doceavo declara los dos libros a la vez y es costura
confirmada.

#### La leccion del barrido por nombre, aprendida a la mala

> En el puesto **615** escribi que `equipo_customer_development` y
> `customer_development_team` **son una pareja que se lee sola**. En el puesto
> **637** los lei de verdad y **no son gemelos**: comparten un paso, no cuatro.
> **Corregido en su razon.**
>
> **Un barrido por nombre senala donde mirar, nunca que decir.** Lo habia escrito
> yo mismo en el puesto 591 y aun asi lo hice mal veinticuatro puestos despues.

### 15.6 SEGUNDO MEZCLADO COMPLETO: la familia del ENCAJE, y es SUELTA

**Encontrada en el puesto 638 contando el jsonl. Cumple la condicion dura.**

| | |
|---|---:|
| miembros | **4**: `fit_problema_solucion`, `problem_solution_fit`, `product_market_fit`, `verificar_product_market_fit` |
| pares posibles | **6** |
| **leidos** | **6** (puestos 186, 297, 338, 490, 497, 536) |
| pendientes | **0** |
| clases | **3 A y 3 B** |
| **aristas internas** | **CERO** |

**Pero la forma no es un monton: las clases estan repartidas con sentido.**

> **Los tres A son los tres pares de `fit_problema_solucion`**, o sea que ese nodo
> **repite con los otros tres**. Los tres B son los otros tres pares entre si.
>
> **No es un mezclado sin centro como el 201: es un CENTRO DE REPETICION.** Un
> nodo que absorbe a los tres y tres nodos que entre ellos son dudosos.
>
> **NOTA DEL 12 ago 2026, y condiciona todo lo que sigue de esta seccion**: esta
> lectura descansa en los veredictos **A** de los puestos **490** y **497**, que
> se sostienen porque `fit_problema_solucion` **no enlaza a ninguno de sus hijos
> de paso**. Y esa cuenta descansa a su vez en **dos juicios mios de
> hijo-o-no-hijo**, declarados en la seccion 16.5: que `design_test_repeat` y
> `circulos_busqueda_cofundadores` **no son hijos de paso** de ese nodo.
>
> **Los dos juicios se revisitan cuando la familia del encaje se lea entera como
> FAMILIA DECLARADA**, y no antes: es exactamente el caso que esa regla existe
> para evitar, decidir de a pares lo que es decision de familia. **Si alguno de
> los dos juicios cae, el 490 o el 497 pasan a D y este CENTRO DE REPETICION deja
> de existir.** Referencia cruzada puesta en los dos sitios.
>
> **Y el puesto 723 aporta evidencia a favor del juicio sobre `design_test_repeat`**:
> resulto ser un nodo de ciclo con **dos gemelos propios**,
> `ciclo_construir_medir_aprender` y `ciclo_crear_medir_aprender`, o sea vida
> propia y no desarrollo de un paso ajeno.

> **Y el centro de repeticion es, otra vez, una costura**: `fit_problema_solucion`
> declara *Value Proposition Design* **y** *Traction* en su campo `fuente`, **y es
> uno de los veinte que quedaron fuera de la cola de las 128.**

### 15.7 LA SERIE DE COLEMAN, afinada por dos pares

**La doctrina de la serie por fases quedo con su limite escrito:**

| puesto | el par | clase | por que |
|---:|---|:---:|---|
| **580** | Assess contra Activate | **D** | **fases distintas**: mismo instrumento, dos publicos, dos entregables |
| **595** | Accomplish contra Accomplish | **A** | **la MISMA fase**: no hay nada que los salve |

> **En una serie por fases, dos nodos de fases distintas son sanos y dos nodos de
> la misma fase son gemelos.** La serie legitima la repeticion del instrumento,
> no la del casillero.

### 15.8 TRACTION, forastero recurrente en las familias de Rackham

**Segundo ejemplar, encontrado en el puesto 625.**

| familia de Rackham | el forastero | su fuente |
|---|---|---|
| **el cierre en venta grande** (seccion 9) | `tacticas_cierre_ventas` | ***Traction*** (Weinberg) |
| **SPIN** | **`framework_spin_selling`** | ***Traction*** (Weinberg) |

> **Un nodo que se llama `framework_spin_selling` y cita a Weinberg** es la misma
> anomalia que el octavo miembro del racimo del cierre. **Dos veces no es
> casualidad: hay una extraccion de *Traction* que dejo material de SPIN con la
> procedencia cambiada**, y eso lo tiene que mirar el frente de fuentes, no la
> mesa de racimos.

---

## 16. LA RELECTURA CONJUNTA DE 395, 581 Y 633

**Hecha el 12 ago 2026 con la regla LA MAYORIA MANDA del banco 9.6.1 delante, y
no arrastrando ningun veredicto.** El encargo lo dijo con estas palabras: **la
coherencia sale de la vara comun, no de arrastrar veredictos.** Salio bien que
fuera asi, porque **la vara comun destapo que mi medicion del 11 de agosto media
lo que no era.**

### El resultado, con las proporciones medidas

| puesto | el par | proporcion medida | clase antes | clase ahora |
|---:|---|---|:---:|:---:|
| **395** | `proceso_ideacion_modelo_negocio` contra la madre de 5 fases | **cadena completa, 5 de 5** | A | **A**, razon reescrita |
| **581** | `prohibicion_tie_in_sales` contra `cumplimiento_magnuson_moss` | **3 de 5 radios**, estricta mayoria | D provisional | **D firme** |
| **633** | `fase_diseno_prototipado_modelos` contra la madre de 5 fases | **cadena completa, 5 de 5** | A | **D** |

### 16.1 EL HALLAZGO QUE LA RELECTURA OBLIGO A TRAER: la familia ENCADENADA

**Lo escribi en la seccion 15.2 asi: la madre enlaza a la fase 1 y a la fase 2 y
no enlaza a la fase 3, ni a la 4, ni a la 5, o sea DOS de CINCO. Eso esta MAL, y
el error es de metodo, no de cuenta.**

> **Conte RADIOS en una familia cableada en CADENA.**

**La cadena, verificada contra el grafo resolviendo a nodo vivo:**

| de | a | fase |
|---|---|---|
| `proceso_diseno_modelo_negocio_5_fases` | `fase_mobilizar_modelo_negocio` | **1** |
| `fase_mobilizar_modelo_negocio` | `fase_entendimiento_investigacion_mercado` | **2** |
| `fase_entendimiento_investigacion_mercado` | **`fase_diseno_prototipado_modelos`** | **3** |
| `fase_diseno_prototipado_modelos` | `fase_implementacion_modelo` | **4** |
| `fase_implementacion_modelo` | `fase_gestion_continua_modelo` | **5** |

> **Cinco fases, cinco hijos, cinco enlaces, CERO sueltos.** La madre solo enlaza
> directo a dos porque **no le hace falta enlazar a mas: la cadena lleva sola.**
>
> **Y por eso el 633 pasa a D.** No es un hijo sin camino: es la casa reconocida
> de la fase 3, alcanzable en el orden correcto. **Aqui no falta ninguna arista.**

**LA REGLA DE MEDICION QUE ESTO FIJA, y quedo en el banco 9.6.1: antes de contar,
se mira la FORMA.** Radios y cadena se cuentan distinto, y contar radios en una
cadena **da minoria donde hay cableado completo.**

### 16.2 El 395 no se salva con lo mismo, y ahora se ve por que

**Si la cadena establece la jerarquia, la pregunta del 395 cambia de sitio.**

> La fase 3 **ya tiene su casa**: `fase_diseno_prototipado_modelos`, la que la
> cadena reconoce. **`proceso_ideacion_modelo_negocio` es una SEGUNDA casa para la
> misma fase**, colgada de un nodo de tecnica y no de la cadena.
>
> **Eso no es una arista que falta: es un duplicado de casa.** La clase A se
> sostiene **con una razon mejor que la que tenia**, y concuerda con el puesto
> **641**, que dio A a las otras dos casas de esa misma fase 3.

**La fase 3 de este metodo tiene TRES nodos**: el de la cadena, el del 395 y
`prototipado_modelos_negocio`, que es hijo con arista del segundo (puesto 572) y
hermano sin arista del primero (puesto 641). **Una fase, tres casas, un solo
camino.**

### 16.3 El 581 se confirma, y de paso corrige mi cuenta

**La clase D se sostiene y deja de ser provisional. Pero la cuenta que la
justificaba estaba mal por los dos lados.**

> **Lo que dije**: la madre enlaza a **cuatro** hijos, uno por cada requisito que
> enumera, y falta **un** radio de cinco.
>
> **Lo que hay:**
> **1.** `contratos_de_servicio_garantia` esta enlazado **pero no desarrolla
> ningun requisito enumerado por la madre**. No es hijo de paso y no cuenta.
> **2.** Me falto un hijo. El paso 3 tiene **DOS** prohibiciones, no comprar a
> proveedor unico **y** no usar frases enganosas, y **las dos tienen casa propia**,
> `prohibicion_tie_in_sales` y `evitar_terminos_enganosos_garantia`, **y ninguna
> de las dos esta enlazada desde la madre.**

| hijo de paso enumerado | que paso desarrolla | enlazado desde la madre |
|---|---|:---:|
| `clasificacion_garantia_full_limited` | paso 2, titulo claro | **si** |
| `regla_divulgacion_garantia` | paso 2, terminos divulgados | **si** |
| `regla_disponibilidad_previa_venta` | paso 2, disponibilidad previa | **si** |
| `prohibicion_tie_in_sales` | paso 3, no obligar a comprar | **NO** |
| `evitar_terminos_enganosos_garantia` | paso 3, no enganar | **NO** |

> **TRES de CINCO es estricta mayoria, asi que la jerarquia esta establecida y el
> veredicto D se sostiene. Pero no falta una arista: FALTAN DOS.**

**Y hay un hallazgo extra que la remedicion destapo, y es la figura del puesto
568 otra vez:** el cubo real de esta familia **no es la madre, es un hijo**.
`clasificacion_garantia_full_limited` enlaza a **SIETE** nodos de la familia,
**incluidos los dos que a la madre le faltan.**

> **La madre no enlaza y el hijo si.** Es la tercera vez que aparece esta forma en
> el archivo, con el 568 y el 574. **Cuando el catalogo tiene un cubo desplazado,
> lo barato no siempre es enlazar desde la madre: puede ser reconocer que el cubo
> es el hijo.**

### 16.4 CORRECCION DECLARADA en la seccion 15.2

**La tabla de la seccion 15.2 dice que el 633 esta en dos de cinco y que por eso
su silueta no exculpa. Eso queda corregido aqui**: la proporcion real es cadena
completa, y el 633 paso a D. **La fila del 581 tambien cambia**, de cuatro de
cinco a **tres de cinco**, que sigue siendo estricta mayoria y no altera su
veredicto.

> **Lo que NO cambia de la 15.2**: la pregunta que abria seguia siendo la
> correcta, y la respuesta llego. **Lo que cambia es que la incoherencia entre el
> 581 y el 633 no era de doctrina: era mia, y era de medicion.**

### 16.5 LA MEDICION DE LOS VEINTE: el saldo

**Hecha el 12 ago 2026 por encargo del fundador.** Los veinte veredictos en **A**
con la silueta *hijo con casa propia sin arista* se midieron **madre por madre con
el grafo delante**, en este orden: **forma primero** (cadena o radios),
**proporcion despues**, y encima la regla de la mayoria con el limite del
cero-enlazados.

| | |
|---|---:|
| veredictos medidos | **20** |
| **cambian de clase** | **9** |
| **se sostienen** | **11** |

**Los nueve que cambian, todos de A a D:**

| puesto | madre | forma | proporcion |
|---:|---|---|---|
| **393** | `busqueda_cofundador_complementario` | radios | 1 de 3 |
| **396** | `preparacion_materiales_fundraising` | radios | 1 de 3 |
| **455** | `customer_validation_sell_phase` | radios | 1 de 3 |
| **470** | `modelo_spin_preguntas` | radios | 1 de 4 |
| **473** | `esfuerzo_y_energia_intelectual` | radios | 1 de 2 |
| **552** | `preparacion_materiales_fundraising` | radios | 1 de 3 |
| **625** | `metodologia_spin_selling` | radios | 1 de 2 |
| **633** | `proceso_diseno_modelo_negocio_5_fases` | **cadena** | 5 de 5 |
| **644** | `customer_discovery_overview` | radios | 1 de 4 |

**Los once que se sostienen, y el motivo es casi siempre el mismo:**

| puesto | madre | por que sigue en A |
|---:|---|---|
| **395** | la madre de 5 fases | **cadena completa**: la fase 3 ya tiene su casa, este es un duplicado |
| **474** | `programacion_entregas_delivery_scheduling` | cero enlazados **y** el hijo repite dos pasos mas de la madre |
| **490**, **497** | `fit_problema_solucion` | cero hijos de paso enlazados |
| **522** | `retention_metrics` | cero enlazados |
| **555** | `etapa_pruebas_necesaria` | cero enlazados |
| **557** | `sucesion_iniciada_por_fundador` | cero enlazados |
| **568** | `publicidad_offline_pruebas_locales` | cero enlazados |
| **582** | `customer_development_weekly_lessons_learned` | cero enlazados |
| **586** | `brainstorming_efectivo` | cero enlazados |
| **610** | `acumulacion_capital_previo_fundacion` | cero enlazados |
| **624** | `estrategia_get_keep_grow` | cero enlazados |

> **DIEZ DE LOS ONCE SE SOSTIENEN POR EL LIMITE DEL CERO-ENLAZADOS**, o sea por el
> limite que yo puse en el puesto 658 y que **no esta escrito en la regla**. Si el
> auditor lo tumba, esos diez se releen otra vez. **Es la pieza de doctrina mas
> cara que hay ahora mismo sobre la mesa.**

#### Los cuatro juicios de HIJO O NO HIJO que sostienen el saldo

**La cuenta depende de decidir que enlace es un hijo de paso y cual no.** El
criterio es el del puesto 581: **hijo de paso es el nodo que desarrolla un item
que la madre ENUMERA.** Cuatro casos lo pusieron a prueba y los cuatro los decidi
yo, asi que van declarados:

| madre | el enlace en duda | mi juicio |
|---|---|---|
| `fit_problema_solucion` | `design_test_repeat` | **no es hijo**: es el ciclo entero de prototipar, testear y repetir, que abarca los pasos 1 a 3 y anade el prototipado que la madre no enumera |
| `fit_problema_solucion` | `circulos_busqueda_cofundadores` | **no es hijo**: es de cofundadores, no toca ningun paso. Arista suelta de nodo costurado |
| `sucesion_iniciada_por_fundador` | `framework_tres_rs_sucesion` | **no es hijo**: los tres Rs son acciones del **sucesor** y los pasos de la madre son acciones del **fundador** |
| `estrategia_get_keep_grow` | `embudo_get_keep_grow` | **no es hijo sino GEMELO**: cubre Get, Keep y Grow al mismo grano que la madre |
| `acumulacion_capital_previo_fundacion` | `seleccion_relaciones_cofundadores` | **no es hijo aqui**: mapea la red para ELEGIR cofundador, que es el paso 3 de **otra** madre |

> **Si alguno de esos cinco juicios se cae, la proporcion de su madre pasa a uno o
> mas de N y el veredicto se vuelve a jugar.** El 490 y el 497 son los que mas
> cuelgan de esto, y arrastran la lectura de CENTRO DE REPETICION de la familia
> del encaje de la seccion 15.6.

#### Lo que la medicion deja como dato, mas alla del saldo

> **1. La forma manda sobre la cuenta, y solo una de veinte era cadena.**
> Diecinueve de las veinte madres estan cableadas en radios; **la unica cadena era
> la que yo habia contado mal.**
>
> **2. La avería dominante no es la mayoria, es el CERO.** Once de las veinte
> madres no enlazan **a ninguno** de sus hijos de paso. **No es que falte un radio:
> es que no hay rueda.**
>
> **3. La regla nueva movio la tasa de A del nucleo casi cuatro puntos**, de 47,3%
> antes de escribirla a **42,8%** despues de aplicarla a todo lo medido. **No
> cambio ni un nodo: cambio la vara.**

### 16.6 EL SALDO FINAL DE LA SILUETA, con la vara ejecutada

**Cerrado el 12 ago 2026.** La silueta *hijo con casa propia sin arista* llego a
**VEINTITRES veredictos** en total: los veinte de la medicion mas los tres que ya
habian caido antes de que se hiciera la lista (473, 633 y 644).

| | |
|---|---:|
| veredictos de la silueta | **23** |
| **pasaron a D** | **19** |
| **siguen en A** | **4** |

**Los cuatro que quedan, y cada uno por un motivo distinto:**

| puesto | por que aguanta |
|---:|---|
| **568** | lo que el hijo anade cabe en **una linea**: la pregunta *como se entero de nosotros* |
| **586** | lo que el hijo anade cabe en **una linea**: no atribuir las ideas a una sola persona |
| **474** | el hijo **repite ademas dos pasos mas** de la madre: no es solo desarrollo, es solape |
| **395** | **no es caso de esta rama**: la familia esta en cadena completa y el nodo es una **segunda casa** de una fase que ya tiene la suya |

### 16.7 LA EXTENSION QUE HICE Y HAY QUE PODER VETAR

**El encargo nombro OCHO caidas. Ejecute DIEZ.**

> Los puestos **658** y **678** no estaban en la lista porque mi cuenta de la
> seccion 19 solo cubria los diez colgantes. **Pero los dos se sostenian con la
> misma frase que la ratificacion abolio**, la figura no aplica y manda la regla
> original. **Dejarlos intactos era dejar el archivo contradiciendose otra vez, en
> el mismo sitio y por el mismo motivo.**
>
> **Los pase a D aplicando la vara y lo declare dentro de sus razones**, con la
> palabra EXTENSION DECLARADA delante, **para que se puedan vetar en una linea.**

> **RATIFICADA POR EL AUDITOR EL 12 ago 2026, SIN VETO.** La razon que dio es la
> que cierra el asunto mejor que la mia: **una frase abolida no puede seguir
> sosteniendo veredictos en ninguna parte del archivo.** No era una extension
> discutible, era el alcance real de la abolicion.
>
> **Y eso deja una regla de procedimiento**: cuando una frase de doctrina se
> retira, **se retira de TODAS las razones que la citan**, no solo de las que
> estaban en la lista del encargo. **La lista era mi cuenta; el alcance es de la
> regla.**

**Los dos, medidos:** en el **658** el hijo trae el **calculo del costo de
retraso con sus cinco componentes** y la regla de superponer solo si supera al
riesgo; en el **678** trae la **prevencion minima viable por nivel de causa** y la
escalada si el problema reaparece. **Ninguna de las dos cosas cabe en una linea.**

### 16.8 EL MARCADOR RECOMPUTADO, y lo que la doctrina le movio

| | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **global** | **742 de 3.388** | **231** | 65 | 4 | 442 | **31,1%** |
| **nucleo** | **587** | **230** | 63 | 4 | 290 | **39,2%** |

**La serie de la tasa de A del nucleo, para que se vea que la movio la vara y no
el material:**

| momento | tasa de A del nucleo |
|---|---:|
| puesto 567, antes de la regla de la mayoria | **49,5%** |
| puesto 700, con la regla escrita y aplicada hacia adelante | 43,9% |
| puesto 742, antes de ejecutar la vara | 40,9% |
| **puesto 742, con la vara ejecutada** | **39,2%** |

> **Diez puntos de caida y ni un nodo tocado.** Los mismos 587 pares del nucleo,
> los mismos textos, y **noventa y tantos veredictos menos en A** de los que
> habria con la vara vieja.
>
> **Lo que esto dice del plan es lo importante**: **la fusion es menos frecuente y
> el ENLACE mas** de lo que el archivo creia hasta ayer. La clase de arreglo mas
> barata del banco 9.6, la arista que falta, **acaba de heredar diecinueve casos
> que estaban contados como fusiones.**

---

## 17. EL TRAMO 646 a 700: la regla nueva puesta a trabajar

**Cincuenta y cinco pares leidos, los cincuenta y cinco del nucleo, y es el
primer tramo que se lee con la regla LA MAYORIA MANDA del banco 9.6.1 delante.**

### CHECKPOINT DE LOS 700, contado antes de escribir

| | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **global al puesto 700** | **700 de 3.388** | 240 | 57 | 4 | 399 | **34,3%** |
| **nucleo al puesto 700** | **545** | 239 | 55 | 4 | 247 | **43,9%** |
| tramo 646 a 700 | 55 | 10 | 9 | 0 | 36 | **18,2%** |

> **LA TASA DE A DEL TRAMO SE DERRUMBO A 18,2%, y hay que decir por que, porque no
> es que los nodos hayan mejorado: es que la vara cambio.** Con la regla vieja,
> sin arista igual a duplicacion, varios de estos pares habrian salido A. La tasa
> del nucleo bajo de 47,3% a 43,9% en cincuenta y cinco lecturas, **y el motivo es
> la regla, no el material.**

### 17.1 LA REGLA NUEVA, aplicada cinco veces, con sus proporciones

| puesto | la madre | hijos de paso | enlazados | rama | clase |
|---:|---|---:|---:|---|:---:|
| **656** | `analisis_de_ratios_financieros` | **8** | **1** | mitad o menos | **D** |
| **670** | `customer_discovery_overview` | **4** | **1** | mitad o menos | **D** |
| **676** | `customer_discovery_overview` | **4** | **1** | mitad o menos | **D** |
| **689** | `esfuerzo_y_energia_intelectual` | **2** | **1** | mitad exacta | **D** |
| **658**, **678** | dos madres distintas | 6 y 3 | **0** | **la figura no aplica** | **A** |

#### El limite que puse yo, y lo declaro porque no esta en la regla

> **La figura pide que la madre enlace a unos hijos si y a otros no.** Cuando
> enlaza a **CERO**, no hay hermanos enlazados de los que sacar mayoria: **no es
> la figura, es el caso corriente**, y manda la regla original, **sin arista igual
> a DUPLICACION**.
>
> **Ese limite lo aplique yo en los puestos 658 y 678 para no romper la linea de
> veredictos que ya existe. No esta escrito en la regla y queda para el visto.**

### 17.2 TRES CORRECCIONES DEL MISMO ORIGEN, y quedan veinte por medir

**La regla nueva no solo gobierna lo que viene: alcanza hacia atras.**

| puesto | era | queda | por que |
|---:|:---:|:---:|---|
| **633** | A | **D** | familia en CADENA, cinco de cinco |
| **644** | A | **D** | misma madre que el 670, uno de cuatro, continua |
| **473** | A | **D** | misma madre que el 689, uno de dos, continua |

> **Las tres corregidas en su razon, con el motivo escrito: el veredicto se emitio
> con la regla vieja y la regla que lo gobierna se escribio despues.**

**Y AQUI ESTA LA DECISION QUE NO ME TOCA TOMAR:**

> **Quedan VEINTE veredictos en A con la misma silueta**, hijo con casa propia sin
> arista: los puestos **393, 395, 396, 455, 470, 474, 490, 497, 522, 552, 555,
> 557, 568, 582, 586, 610, 624, 625, 658 y 678.**
>
> **Ninguno esta medido con la regla nueva.** De los cinco que si medi este tramo,
> **tres cayeron del lado de la figura y cambiaron de clase, y dos no.** La
> proporcion no se puede adivinar: hay que medir madre por madre, y **cada uno
> cuesta una lectura con el grafo delante.**
>
> **Lo traigo en vez de barrer**, porque un barrido sin medir seria justo el error
> que la regla vino a corregir.

### 17.3 PRECISION QUE HAY QUE HACERLE A LA CONDICION DURA DEL PURO

**Encontrada en el puesto 690 y verificada contra las tres declaraciones vivas.**

La condicion dura del banco 9.5 dice **todos los pares leidos y cero pendientes**.
**Pendientes de la COLA. Y la cola no contiene todos los pares posibles.**

**EL EJEMPLAR QUE LO DESTAPA: la familia de Get, Keep, Grow.**

| | |
|---|---:|
| nodos vivos que la nombran | **8** |
| pares **posibles** | **28** |
| pares **en la cola intra** | **3** |
| leidos | **3** |
| **clases** | **A, A, A** (puestos 277, 292, 624) |
| pendientes **de la cola** | **0** |

> **Leido con la frase de hoy, este racimo seria PURO: todos sus pares leidos,
> todos repiten, cero pendientes. Y es falso: veinticinco de sus veintiocho pares
> nunca entraron a la cola**, porque cayeron por debajo del umbral de semejanza.
>
> **LA CONDICION DURA TIENE QUE CONTAR PARES POSIBLES, NO PARES DE LA COLA.**

**VERIFICADO CONTRA LO YA DECLARADO, y las tres se sostienen:** el trio del sales
roadmap tiene 3 posibles y 3 leidos; la familia del encaje 6 y 6; el racimo del
control de la junta 3 y 3. **En familias pequenas todos los pares posibles
entraron a la cola, y por eso el hueco no habia asomado.**

### 17.4 EL PASO QUE TIENE TRES CASAS, y coincide con la familia del encaje

**El paso 4 de `customer_discovery_overview`**, evalua los resultados y decide si
tienes validacion suficiente, **tiene TRES nodos que lo desarrollan**:

| casa | puesto | clase |
|---|---:|:---:|
| `pivotar_o_proceder` | 644 | D, corregido |
| `product_market_fit` | 670 | D |
| `verificar_product_market_fit` | 676 | D |

> **La madre no enlaza a ninguna de las tres.** Y **dos de las tres son miembros
> de la FAMILIA DEL ENCAJE** de la seccion 15.6, la del mezclado completo con cero
> aristas internas. **El paso 4 de esta madre y la familia del encaje son el mismo
> nudo visto desde dos lados**, y quien se siente a resolver uno resuelve el otro.

### 17.5 LO QUE EL TRAMO DEJA ADEMAS

> **1. LA TRAMPA DEL NOMBRE, segunda confirmacion.** El puesto **683** leyo
> `customer_development_modelo` contra `modelo_customer_development`, las mismas
> dos palabras al reves, **y no son gemelos**. Con el 637, **dos de dos
> predicciones por nombre han salido falsas.**
>
> **2. UNA FAMILIA QUE NO TIENE PROBLEMA DE DUPLICADOS SINO DE CABLEADO.** Los
> puestos 681, 699 y 700 leyeron los tres pares de `build_metrics_toolset`,
> `checkpoints_validacion` y `medir_comportamiento_cliente_mvp`: **los tres
> sanos**, y **los tres con la arista que falta**. Instalar los sensores, poner la
> vara y leer el resultado son tres nodos que nadie conecto.
>
> **3. EL UNICO LIBRO QUE CABLEA BIEN.** *A Project Manager's Book of Forms* llego
> a **cuatro familias bien enlazadas** en dos tramos, riesgo (579, 613, 659),
> cronograma (578), requisitos (671) y reportes (642). **Es el unico del nucleo
> que enlaza sus formularios de forma consistente.**
>
> **4. LAS NOMINAS SIGUEN CORTADAS.** `inversion_proporcional` repite en A con
> `five_whys_inversion_proporcional` (puesto 678) y **no esta en la nomina** del
> racimo censado de los cinco porques. Es el **tercer** racimo censado al que le
> falta un miembro que ya emparejo en A.
>
> **5. PRIMERA VEZ QUE LOS DOS NODOS ESTAN CENSADOS Y LA REGLA NO CORRE.** En el
> puesto **677** los dos nodos son miembros de racimos censados, **pero de racimos
> DISTINTOS**. La regla FAMILIA DECLARADA pide los dos en la MISMA nomina.

### 17.6 UN REFINAMIENTO DE LA REGLA DEL NODO AVERIADO

**Registrado en el puesto 673 y usado otra vez en el 678.**

> La seccion 15.4 dice que un nodo averiado contamina sus pares. **Este tramo le
> pone el limite: contamina solo cuando el SOLAPE CRUZA LA JUNTURA.**
>
> En el **673**, `seleccion_ceo_fundador` es costura confirmada de doce pasos, y
> el solape con `errores_comunes_asignacion_roles` **cae entero dentro de sus
> pasos 1 a 4**, el bloque que sobrevive a la cirugia. **El veredicto se puede
> emitir hoy.** Lo mismo en el **678** con el bloque de Ries de
> `five_whys_inversion_proporcional`.
>
> **Si el solape vive de un solo lado de la costura, el par se lee. Si la cruza,
> se espera al arreglo.**

---

## 18. EL TRAMO 701 a 724: familias que se cuentan solas

**Veinticuatro pares leidos, los veinticuatro del nucleo. Sin checkpoint: el
proximo es el de los 800.** Acumulado **724 de 3.388**, global **33,1%** de A y
**nucleo 42,0%**; el tramo dio **25,0%**.

### 18.1 LA TRAMPA DEL NOMBRE, tercera vez, y esta vez es mia contra mi

**En el puesto 669 conte la familia de las seis herramientas de comunicacion de
Coleman y dije CUATRO nodos: la madre y tres aplicaciones.** El puesto **719**
trajo una cuarta aplicacion, `estrategia_multicanal_bienvenida`, **que aplica las
mismas seis herramientas y no lleva `seis` en el identificador.**

> **Volvi a contar por nombre.** Es la tercera vez que ese barrido falla, despues
> del **637** y el **683**, **y las dos anteriores las habia escrito yo mismo como
> leccion.** La cuenta de esa familia queda **abierta** hasta que se haga por
> contenido.

#### LA CIFRA CORRECTA, contada con `scripts/contar_nombre.py`

**La cuenta queda CERRADA el 12 ago 2026, y con herramienta en vez de a ojo.**

| conteo | cuando | resultado |
|---|---|---:|
| a mano, puesto **669** | 11 ago | **4** |
| a mano, puesto **719** | 12 ago | **5** |
| **con script** | 12 ago | **7** |

**Los siete nodos vivos del nucleo que nombran el instrumento de las seis vias de
comunicacion de Coleman**, con lo que es cada uno:

| nodo | que es |
|---|---|
| `seis_medios_comunicacion_cliente` | **el instrumento**: define las seis vias y como elegir entre ellas |
| `seis_canales_comunicacion_assess` | aplicacion a la fase **Assess** |
| `seis_herramientas_comunicacion_fase_activate` | aplicacion a la fase **Activate** |
| `seis_herramientas_comunicacion_celebracion` | aplicacion a la **celebracion de hitos** |
| **`estrategia_multicanal_bienvenida`** | aplicacion a la **bienvenida posterior a la compra**, y **no lleva la palabra en el identificador**: es la que se me habia perdido |
| `fase_assess_ciclo_cliente` | **no es aplicacion**: es un nodo de fase que **mete el instrumento dentro de un paso**, el 5 |
| `fase_adopt_ciclo_cliente` | lo mismo, dentro de su paso 2 |

> **Y contar bien destapa una figura que el conteo a mano no podia ver: la fase
> Assess esta DOBLADA.** `fase_assess_ciclo_cliente` **lleva el instrumento
> pegado dentro de un paso** y `seis_canales_comunicacion_assess` **es ese mismo
> uso con casa propia**. Es la **DUPLICACION CRUZADA** de la seccion 15.3, un
> ejemplar mas: **uno lo absorbe, el otro lo desarrolla, y nadie los enlaza.**
>
> **La regla que sale de aqui esta en el banco 9.5.1: EL CENSO POR NOMBRE SE
> CUENTA POR SCRIPT.** Y la segunda mitad importa igual: **el script dice donde
> mirar; la pertenencia se decide leyendo.** Los dos ultimos de la tabla lo
> prueban: el script los trae y la lectura dice que no son aplicaciones.

### 18.2 CUATRO CANDIDATOS A RACIMO, contados y no declarados

| familia | miembros vistos | pares leidos | señal |
|---|---:|---|---|
| **las cuatro areas de desempeno** (651, 704) | **3** | 2, los dos **A** | mismo libro, mismas cuatro areas |
| **los cofundadores** (708, 716) | **3 o mas** | 2, los dos **B** | el mismo nodo dudoso dos veces |
| **el bucle de cuatro tiempos** (376, 723) | **3** | 2, los dos **A** | tres nodos para *construir, medir, aprender* |
| **Wallas** (473, 689, 693, 718, 721) | **6** | 5 | una familia entera de como se trabaja la cabeza |

> **El bucle es el mas barato de los cuatro y el mas claro**: `ciclo_construir_medir_aprender`,
> `ciclo_crear_medir_aprender` y `design_test_repeat` **dicen los mismos cuatro
> pasos**, y los dos primeros se diferencian **en un verbo del identificador**.
>
> **Y de paso confirma un juicio de la medicion de los veinte**: `design_test_repeat`
> no es hijo de paso de `fit_problema_solucion`, **es un nodo de ciclo con vida
> propia, y ahora se sabe que ademas tiene dos gemelos.**

### 18.3 EL OTRO LADO DEL REFINAMIENTO DEL 673

**El puesto 673 fijo que un nodo averiado contamina el par solo cuando el solape
CRUZA la juntura. El puesto 724 es el primero que la cruza.**

> `voz_del_cliente_voc` es costura **confirmada** con la anatomia escrita en la
> ficha: **DOBLE DE LA OBSERVACION**, diez pasos en dos mitades que hablan **las
> dos** de observar al cliente en su contexto.
>
> Y lo que `voice_of_customer_estrategico` solapa con el **es justamente la
> observacion**, o sea **las dos mitades a la vez**. El veredicto se emitiria
> contra un texto que va a perder la mitad de su masa. **Queda en B y se lee
> despues del arreglo interno.**
>
> **Lo que si queda anotado para el redactor**: *buscar necesidades futuras* y
> *que los mantiene despiertos por la noche* **no estan en el nodo largo**.

### 18.4 Lo demas del tramo

> **1. CUARTO EJEMPLAR de con arista y aun asi duplicacion** (puesto **712**,
> las dos juntas asesoras), con el 570, el 614 y el 635. **Ninguno de los cuatro
> tiene madre que resuma: son textos del mismo grano cableados entre si.**
>
> **2. TERCER EJEMPLAR de *Traction* como forastero** (puesto **710**):
> `compromiso_linea_tiempo_cliente` cita a Weinberg y esta parado dentro del tema
> de obtencion de compromiso, que es de Rackham. Con `tacticas_cierre_ventas` y
> `framework_spin_selling` **ya son tres.**
>
> **3. La introduccion a Customer Validation lleva SEIS pares leidos** (245, 247,
> 597, 655, 697 y 709). **Es de las zonas mas repetidas del nucleo** y todavia no
> esta declarada como racimo.
>
> **4. Dos tramos bien cableados, y los dos son excepcion.** El de Wallas entre
> iluminacion, intimacion y verificacion (puesto 721), y el de `customer_profile`
> hacia sus tres hijos, `customer_jobs`, `customer_pains` y `customer_gains`
> (puesto 705). **En un tramo donde la averia dominante es el cero enlazados,
> conviene anotar quien si enlaza.**

---

## 19. EL CHOQUE DE LA RATIFICACION, traido sin resolver

**Encontrado el 12 ago 2026 al aplicar la ratificacion del cero-enlazados, y lo
traigo en vez de resolverlo porque no me toca.**

### Lo que chocan son dos frases que ahora conviven en el mismo veredicto

| la frase vieja, del puesto 658 | la frase nueva, de la ratificacion |
|---|---|
| con **cero enlazados** la **figura NO APLICA**, y manda la regla original: **sin arista igual a DUPLICACION** | **cero enlazados es el caso extremo del mitad-o-menos**: la silueta no dice nada y **manda el CONTENIDO** |

> **No dicen lo mismo, y la diferencia decide clases.** La primera sostiene la
> **A** por la ausencia de arista. La segunda manda **juzgar por
> continua-o-repite**, y en la mayoria de estas siluetas el hijo desarrolla un
> paso con material propio, o sea **CONTINUA**, que es **D**.
>
> **Es exactamente la misma logica que hizo caer a nueve veredictos en la medicion
> de los veinte.** Si se aplica a estos diez, varios caen tambien.

### La cuenta, hecha para que la decision se tome con numeros

**De los diez, DOS aguantan el test de contenido y OCHO probablemente no.**

| puesto | que dice el contenido | aguanta la A |
|---:|---|:---:|
| **568** | el hijo desarrolla el paso 3 **y ademas repite el paso 4** de la madre | **si** |
| **586** | lo unico que el hijo anade es una linea, la no atribucion de ideas | **si** |
| **490**, **497** | el hijo trae su checklist propia de encaje, seis evaluaciones que la madre no tiene | probablemente no |
| **522** | el hijo trae el procedimiento entero de cohortes | probablemente no |
| **555** | el hijo trae alfa, campo, piloto, soft launch y la vuelta atras | probablemente no |
| **557** | el hijo trae el procedimiento de participar en la propia sucesion | probablemente no |
| **582** | el hijo trae el ciclo rojo a negro y la serie historica | probablemente no |
| **610** | el hijo trae el mapeo de red y el puente al primer cliente | probablemente no |
| **624** | el hijo trae umbrales, cohortes, CAC contra valor de vida y la simulacion | probablemente no |

> **Y el puesto 474, que no esta en la lista de los diez, aguanta por el mismo
> motivo que el 568**: su hijo repite dos pasos mas de la madre.

### Por que no lo resuelvo yo

> **El encargo dice que los diez quedan citando la regla.** Cambiarlos por mi
> cuenta seria interpretar la ratificacion mas alla de lo que dice, y **la
> ratificacion vino justamente a quitar de en medio un limite que yo habia puesto
> solo.**
>
> **Los diez quedan con las dos lecturas encima y el choque escrito en su razon.**
> Con el visto del auditor son ocho lecturas dirigidas, ni una mas.

### Y hay una tercera salida, que es la que yo propondria

> **La regla podria distinguir DOS preguntas que hoy mete en una.** Cuando el hijo
> desarrolla un paso de la madre, siempre hay repeticion **de la orden** y casi
> siempre hay material **nuevo** en el hijo. Lo que cambia entre casos es cuanto.
>
> **La vara que ya usa el archivo sin nombrarla**: si lo que el hijo anade cabe en
> una linea, **repite**; si el hijo trae un procedimiento que la madre no tiene,
> **continua**. El 586 y el 568 caen del primer lado y los otros ocho del segundo.
>
> **Nombrarla convertiria ocho lecturas dirigidas en cero**, porque la cuenta de
> arriba ya esta hecha con esa vara.

### CERRADA EL MISMO DIA

**El auditor adopto la vara con el nombre propuesto, LA LINEA O EL PROCEDIMIENTO,
y esta en el banco 9.6.1.** La cuenta de arriba se ejecuto entera: **los ocho
cayeron, el 568 y el 586 aguantan citando la vara**, y **extendi la ejecucion a
dos mas, el 658 y el 678**, que se sostenian con la misma frase abolida y no
estaban en la lista. **Esa extension va declarada y se puede vetar**, seccion
16.7.

> **Lo que esta seccion deja como leccion, y va al banco 9.5.0**: el choque no fue
> entre dos reglas. **Fue entre la regla y mi parafrasis de la regla.** La regla
> decia *la arista no exculpa*, que corta en los dos sentidos; mi parafrasis decia
> *sin arista igual a duplicacion*, que solo corta en uno. **Y la parafrasis
> gobernó diecinueve veredictos.**

---

## 20. EL TRAMO 725 a 742: el tramo mas sano del cribado

**Dieciocho pares leidos, los dieciocho del nucleo.** Acumulado **742 de 3.388**,
global **32,5%** de A y **nucleo 40,9%**. **Sin checkpoint: el proximo es el de
los 800.**

### 20.1 La cifra del tramo, y por que no significa lo que parece

| | leidos | A | B | D | tasa de A |
|---|---:|---:|---:|---:|---:|
| tramo 725 a 742 | 18 | **1** | 2 | 15 | **5,6%** |

> **Es la tasa de A mas baja de todo el cribado, y no es que el catalogo haya
> mejorado en dieciocho lecturas.** Es que **la cola llego a una zona de familias
> bien separadas**: la de garantias federales, donde cada nodo es una obligacion
> legal distinta (puestos 727, 736, 739), la serie de fases del lienzo (740), las
> letras de SPIN (741) y los formularios de despido (735).
>
> **Cuando una familia se escribio con un nodo por objeto, el cribado la atraviesa
> sin encontrar nada.** Y eso tambien es un dato: **hay zonas del nucleo que estan
> bien.**

### 20.2 El primer par que NACE con las dos lecturas encima

**El puesto 730** es el primer veredicto nuevo emitido **despues** de que el
choque de la seccion 19 quedara escrito.

> `efecto_bullwhip` desarrolla los pasos 1 y 2 de `colaboracion_cadena_suministro`
> y la madre **no enlaza a ninguno de sus hijos**. Por la lectura vieja es **A**;
> por la ratificacion, el hijo trae **una contabilidad entera** que la madre no
> tiene, o sea **CONTINUA**, y seria **D**.
>
> **Se registro en A y con el choque anotado dentro.** No elijo yo: mientras la
> doctrina tenga dos lecturas, **los veredictos nuevos de esta silueta nacen con
> las dos y lo dicen.**

### 20.3 Dos familias que hay que contar antes de tocar

> **1. LA FAMILIA DE A/B, por lo menos CUATRO nodos** (puesto 738):
> `ab_testing_optimizacion` con **quince** pasos en tres bloques,
> `split_testing_experimentos_ab` con **nueve** en dos y costura **confirmada**,
> mas `split_testing` y `test_ab_precio` del puesto 643. **Ninguno enlaza a otro.**
> El par 738 quedo en **B** porque los dos nodos estan averiados **y el solape
> cruza las dos junturas**: es el segundo caso de doble averia despues del 599.
>
> **2. LA FAMILIA DE S&OP, TRES nodos y una lectura imposible todavia** (puesto
> 725): `sales_operations_planning`, `sop_colaborativo` y
> `mission_and_operations_planning`. **El primer par dio B (703), el segundo D
> (725) y el tercero esta pendiente en el puesto 1218.** La familia no se puede
> leer hasta que caiga ese tercero, y **son solo tres pares: es candidata natural
> a COMPLETAR LOS PARES DEL PURO**, la clase de tarea del banco 9.5.

### 20.4 Y una cuenta mia corregida, otra vez por conteo a ojo

**Puesto 728.** En el **470** conte **cuatro** hijos de paso de
`modelo_spin_preguntas` y son **CINCO**: `preguntas_need_payoff` existe vivo y
desarrolla su paso 4.

> **La proporcion pasa de uno de cuatro a uno de cinco**, sigue siendo mitad o
> menos y **el veredicto D de aquel par no cambia**. Pero el error es el mismo de
> siempre. **Es justo lo que `scripts/contar_nombre.py` viene a impedir**, y esta
> es la primera vez que el error aparece **despues** de tener la herramienta.
>
> **La leccion no es que conte mal: es que segui contando a mano teniendo el
> script.** La regla del banco 9.5.1 no sirve si no se usa.

### 20.5 Lo demas anotado al paso

> **La familia de la sucesion llega a ONCE pares leidos** (256, 354, 423, 435,
> 557, 612, 618, 621, 634, 720 y 732) **sobre DOCE nodos**: el puesto 732 le suma
> `riesgo_beneficio_retener_fundador` a los once medidos en el 618. **Sigue sin
> censar y sigue con su forastero de *The Hard Thing*.**
>
> **Y la cifra la conte mal dos veces antes de escribirla**: puse cinco y liste
> siete. **La correcta salio de contar el archivo, no la memoria**, que es la
> tercera leccion del mismo tipo en dos tramos. **Once de sesenta y seis pares
> posibles: esta familia es la mas leida del nucleo sin estar declarada.**
>
> **La familia de los cofundadores llega a TRES pares** (708, 716, 729), dos de
> ellos dudosos, y tampoco esta censada.
>
> **El racimo del pivote sigue en 19 nodos y 24 pares sin leer**, y este tramo le
> sumo dos lecturas mas (733, 737).

---

## 21. EL TRAMO 743 a 760: la vara trabajando en caliente

**Dieciocho pares leidos, los dieciocho del nucleo.** Acumulado **760 de 3.388**,
global **30,7%** de A y **nucleo 38,3%**. El tramo dio **11,1%**. **Sin
checkpoint: el proximo es el de los 800.**

### 21.1 La vara nombrada, usada ya en veredictos nuevos

**Es el primer tramo leido con `LA LINEA O EL PROCEDIMIENTO` disponible desde el
principio, y se uso dos veces sin necesidad de discutir nada.**

| puesto | el caso | lo que la vara resolvio |
|---:|---|---|
| **744** | `diagnostico_sintoma_vs_causa_ventas` contra `prevencion_objeciones_vs_manejo` | el hijo trae el diagnostico de objeciones **con su procedimiento**: **CONTINUA**, D |
| **756** | `pensamiento_serial_vs_espacial` contra `pensamiento_espacial_mapeo` | el selector **nombra** el instrumento en su paso 4 y el instrumento trae el procedimiento entero: **CONTINUA**, D |

> **En los dos casos la razon se escribio en una linea y sin deliberar.** Eso es
> lo que una vara nombrada compra: **deja de haber caso dificil donde antes habia
> juicio.**

### 21.2 UN NODO QUE SE ROZA CON DIEZ Y NO REPITE CON NINGUNO

**`verificar_product_market_fit`, contado del archivo en el puesto 760.**

| | |
|---|---:|
| pares leidos | **10** (186, 297, 304, 407, 431, 497, 676, 733, 751 y 760) |
| en **A** | **0** |
| en **B** | 3 |
| en **D** | 7 |

> **Es de los nodos mas emparejados del nucleo y no repite con nadie.** La cola lo
> trae una y otra vez porque **su vocabulario toca el de media familia de
> validacion**, y cada vez que se lee de verdad resulta ser otra cosa: una lista
> de comprobacion con umbrales numericos que ningun vecino tiene.
>
> **FIGURA QUE ESTO NOMBRA: EL NODO MUY EMPAREJADO Y NUNCA REPETIDO.** No es un
> problema del nodo: **es un aviso sobre la cola.** Diez lecturas para confirmar
> diez veces que es sano. **Cuando un nodo acumula muchas D seguidas, sus pares
> restantes bajan de prioridad**, y eso se puede usar para ordenar lo que queda.

### 21.3 El nodo que bloquea, y ya van dos

**`voz_del_cliente_voc`**, costura confirmada con anatomia **DOBLE DE LA
OBSERVACION**, **bloquea su segundo par** (puestos 724 y 755).

> **Los dos pares tienen el solape metido justo en la parte que la cirugia va a
> partir**, asi que ninguno se puede juzgar hoy. **Un nodo averiado no cuesta un
> arreglo: cuesta el arreglo mas todas las lecturas que congela.**
>
> **Y lo que hay que salvar ya esta anotado en los dos**: del 724, buscar
> necesidades futuras y *que los mantiene despiertos por la noche*; del 755,
> proyectar como cambia el dia del cliente con el producto, repetir el ejercicio
> por cada figura de la decision, y llevarle al equipo de desarrollo la imagen
> viva del antes y el despues.

### 21.4 El racimo de las puertas llega a CUATRO pares y los cuatro en A

**Puesto 745**, con el 275, el 302 y el 356.

> **Cuatro fusiones distintas sobre los mismos seis nodos.** Es la confirmacion
> mas fuerte que hay de lo que el 275 dejo nombrado: **esto no son cuatro podas,
> es un PROGRAMA UNICO**, y cada par que se lea va a sumar otra fusion
> incompatible con las anteriores.

### 21.5 Dos familias mas que hay que contar, y una que avanza

> **1. LOS TRES CAPITALES** (puestos 393, 610, 757): el inventario de capital
> humano, social y financiero del fundador aparece en varios nodos con
> redacciones distintas. **Sin censar.**
>
> **2. LOS EXPERIMENTOS** (puesto 748): `startup_como_experimento_cientifico` y
> `producto_como_experimento` dicen la misma doctrina con dos granos, y la familia
> toca ademas los nodos de MVP y de pruebas de pasa o no pasa. **Sin censar.**
>
> **3. EL RACIMO DEL EQUITY AVANZA**: el puesto **754** cerro el tercero de sus
> cinco pares pendientes. **Quedan dos, los puestos 871 y 1008**, y cuando caigan
> ese racimo sera de los pocos con la cuenta cerrada.

---

## 22. EL TRAMO 761 a 772: un puro que nace con condicion

**Doce pares leidos, los doce del nucleo.** Acumulado **772 de 3.388**, global
**30,4%** de A y **nucleo 37,9%**. **Sin checkpoint: el de los 800 es el
proximo.**

### 22.1 EL CUARTO PURO NACIO Y EL MISMO TRAMO LE PUSO CONDICION

**Lo declare en la relectura R12 de este mismo turno. Ocho puestos despues, el
cribado encontro al cuarto candidato.**

> **`investigacion_como_habilidad_clave`** es de *SPIN Selling*, no esta en la
> nomina censada, y manda **lo mismo que los tres**: preparar preguntas que
> descubran necesidades reales, no apoyarse en el conocimiento del producto como
> reemplazo de indagar, y **medir que porcentaje de la llamada se usa en preguntar
> y cuanto en presentar**, que es literalmente el paso que los tres comparten.

| par | contra | estado |
|---|---|---|
| **800** | `etapa_investigacion_ventas` | **PENDIENTE** |
| **862** | `enfoque_etapa_investigacion` | **PENDIENTE** |
| el tercero | `etapa_de_investigacion` | **nunca entro a la cola** |

> **El puro se sostiene sobre la nomina censada, que es lo que la condicion dura
> pide.** Pero **basta con que el 800 o el 862 salga A para que la familia sea de
> cuatro y el puro pase a SUB-PURO**, igual que le paso al trio de las arenas
> ocho puestos antes.
>
> **La condicion quedo escrita dentro de la declaracion del banco 9.5, con los dos
> puestos que la resuelven nombrados.** Un puro con fecha de revision.

> **Y esto es la regla de la nomina que crece (seccion 6) mordiendo por tercera
> vez, ahora sobre un racimo CENSADO.** El censo no protege: **una nomina cerrada
> por censo puede estar cortada igual que una reconstruida.**

### 22.2 OTRO PAR DE NOMBRE, y este si es real

**Puesto 765.** Existen **`estructura_gates`** y **`estructura_de_gates`**, dos
nodos vivos separados por un **DE**, y **solo el primero esta en la nomina** del
racimo de las puertas.

> **Su par mutuo es el puesto 1524 y esta pendiente.** Pero el segundo ya repitio
> con `requisitos_gates_con_dientes` en este tramo, igual que el primero habia
> repetido en el puesto 745.
>
> **LA FAMILIA DE LAS PUERTAS, remedida**: **ocho nodos**, 28 pares posibles,
> ocho en la cola, **cuatro leidos y LOS CUATRO EN A**. **El PROGRAMA UNICO que el
> 275 pidio tiene ahora ocho nodos que gobernar, no seis.**
>
> **Y a diferencia de las dos predicciones por nombre que fallaron** (puestos 637
> y 683), **esta salio cierta porque se leyo antes de decirlo.**

### 22.3 Lo demas del tramo

> **1. SEGUNDA VEZ que los dos nodos estan censados en racimos DISTINTOS** (puesto
> 768, tras el 677): la regla FAMILIA DECLARADA no corre porque pide los dos en la
> misma nomina. **Y las dos veces el cruce es el mismo**: la practica de una
> familia termina en la puerta de la otra, sin arista.
>
> **2. El racimo del pivote suma su tercer par dudoso del mismo nodo** (puestos
> 737, 753 y 771). **`pivote_startup` y `pivote_o_proceder` se rozan con todo el
> mundo y no repiten con nadie del todo.**
>
> **3. La vara del banco 9.6.1 volvio a resolver un caso sin deliberar** (puesto
> 764, la misma madre del 625): uno de tres hijos enlazados, contenido manda, y el
> hijo trae la secuencia SPIN entera. **CONTINUA.**
>
> **4. `sintesis_hipotesis_modelo_negocio` llega a cuatro pares leidos y los
> cuatro sanos.** Es el segundo nodo del tramo con esa firma, con
> `verificar_product_market_fit` de la seccion 21.2: **se rozan con muchos y no
> repiten con ninguno.**

---

## 23. EL TRAMO 773 a 784: el cuarto mezclado completo estaba escondido en una cifra mal puesta

**Doce pares leidos, los doce del nucleo.** Acumulado **784 de 3.388**, global
**30,5%** de A y **nucleo 37,8%**. El tramo dio **33,3%**. **El checkpoint de los
800 es el proximo.**

### 23.1 UNA CIFRA DE MEMORIA QUE DESTAPO UN RACIMO CERRADO

**En el puesto 781 escribi que la apertura de Customer Validation llevaba SIETE
pares leidos. Lo escribi de memoria. Al contar el jsonl para corregirlo aparecio
algo mas grande que el numero.**

| lo que conte | resultado |
|---|---|
| el conjunto ampliado de **5 nodos** | **10 pares posibles, 8 leidos**, 2 que nunca entraron a la cola |
| **el racimo C declarado en la seccion 1**, de **3 miembros** | **3 pares posibles, LOS TRES LEIDOS, cero pendientes** |

> **Clases del racimo C: D, D y A.** Es un **MEZCLADO COMPLETO**, el **CUARTO** del
> archivo, con el racimo del control de la junta, la familia del encaje y los
> habitos de pensamiento.
>
> **Y estaba completo desde el puesto 709**, o sea desde hace setenta y cinco
> lecturas, **sin que nadie lo declarara.**

> **Su forma es la peor que puede tener una mesa: dos pares sanos y uno que
> repite.** No se pueden fusionar los tres ni dejar los tres. **Hay que decidir la
> arquitectura con dos de los tres pares diciendo que no hay nada que decidir.**

**LA LECCION, y es de procedimiento**: la correccion de una cifra **no es
mantenimiento, es lectura**. Al contar para arreglar un numero se ve la familia
entera, y ahi estaba el racimo cerrado. **Vale la pena contar aunque el numero no
importe.**

### 23.2 TERCER PAR DE NOMBRE INVERTIDO, y los tres reales se confirmaron leyendo

**Puesto 782**: `diversidad_vs_homogeneidad_equipo` contra
`homogeneidad_vs_diversidad_equipo`. **Las mismas dos palabras al reves, y esta
vez SI son gemelos**, con arista en los dos sentidos.

| par de nombre invertido | como se supo |
|---|---|
| 637 y 683, los de customer development | **prediccion, y salio FALSA las dos veces** |
| **estructura_gates** contra **estructura_de_gates** (765) | **lectura**, y salio cierta |
| **este 782** | **lectura**, y salio cierta |
| las dos etapas de investigacion (209, 278, 303) | **lectura**, y salio cierta |

> **Tres aciertos y dos fallos, y la diferencia es siempre la misma**: los tres
> aciertos se leyeron antes de decirlos y los dos fallos se dijeron antes de
> leerlos. **El script cuenta; la lectura decide.**

### 23.3 EL CUARTO PURO SUMA SU SEGUNDO VECINO

**Puesto 775.** Tras `investigacion_como_habilidad_clave` del 769, se arrima
`cuatro_etapas_llamada_de_ventas`.

> **A este NO lo juzgo miembro, y digo por que**: su objeto son las **cuatro
> etapas** de la llamada y no la investigacion, y **ENLAZA a dos miembros de la
> familia**, `etapa_investigacion_ventas` e `investigacion_como_habilidad_clave`.
> **Se comporta como marco, no como hermano.**
>
> **Pero el aviso queda**: el cuarto puro tiene ya **dos nodos externos rozandolo**
> y **tres pares pendientes** que pueden convertirlo en sub-puro (800, 862 y el
> que nunca entro a la cola).

### 23.4 EL TERCER NODO QUE BLOQUEA UN PAR

**Puesto 784.** `lienzo_modelo_negocio` es costura confirmada con anatomia
escrita: **diecisiete pasos y CUATRO narraciones del Canvas.**

> El solape con `swot_business_model_canvas` **son los nueve bloques**, o sea
> **exactamente el nucleo que el nodo repite cuatro veces**. **Cruza las cuatro
> junturas a la vez**, asi que el par no se juzga hoy.
>
> **Ya son TRES los nodos que bloquean lecturas por costura**: `voz_del_cliente_voc`
> (dos pares), los dos de A/B del puesto 738, y este.
>
> **Lo que si queda salvado**: el analisis cruzado, **como una debilidad de un
> bloque golpea a los otros**, no esta en el nodo largo y es lo unico que el corto
> aporta.

---

## 24. CHECKPOINT DE LOS 800

**Dieciseis pares leidos en el tramo 785 a 800, los dieciseis del nucleo. Sin
huecos: 800 de 800.**

### El marcador completo, recomputado del archivo

| | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **global** | **800 de 3.388** | **248** | 78 | 4 | 470 | **31,0%** |
| **nucleo** | **645** | **247** | 76 | 4 | 318 | **38,3%** |
| tramo 785 a 800 | 16 | 9 | 1 | 0 | 6 | **56,2%** |

**La serie de checkpoints, para que se vea que la curva no la mueve el material:**

| checkpoint | global | nucleo |
|---|---:|---:|
| 600 | 35,8% | 48,1% |
| 700 | 34,3% | 43,9% |
| **800** | **31,0%** | **38,3%** |

> **Diez puntos de caida en el nucleo entre el 600 y el 800, y la mitad no la
> puso la cola: la puso la doctrina.** Entre esos dos checkpoints se escribieron
> la regla de la mayoria, la ratificacion del cero y la vara de la linea o el
> procedimiento, y **diecinueve veredictos pasaron de A a D sin que se tocara un
> nodo.**

> **El tramo del checkpoint, en cambio, dio 56,2%, la tasa mas alta en mucho
> rato**, y por un motivo de cola: **cayeron juntas varias parejas de gemelos
> puros** (el leverage con los VCs, la voz del cliente, el marcador de innovacion,
> los regalos, las metricas que importan). **La cola no reparte parejo, y por eso
> el acumulado es la cifra de lectura y no el tramo.**

### 24.1 EL CUARTO PURO DURO TREINTA Y UN PUESTOS

**Declarado en la relectura R12 con la nomina censada de tres. Condicionado ocho
puestos despues, en el 769. Degradado en el 800.**

> El **800** salio **A**: `etapa_investigacion_ventas` repite con
> `investigacion_como_habilidad_clave`, y **tres de sus cuatro pasos son el
> mismo**.

| la familia real | |
|---|---:|
| miembros | **4** |
| pares posibles | **6** |
| leidos | **4**, y **los cuatro en A** |
| le faltan | **2**: el **862** y uno que **nunca entro a la cola** |

> **Queda como SUB-PURO**, la tercera figura de esa clase con el trio del
> descubrimiento (276) y el de las arenas (280). **Y es el candidato mas barato a
> COMPLETAR LOS PARES DEL PURO que hay hoy: dos lecturas.**
>
> **La leccion, escrita tambien en el banco**: un puro declarado sobre nomina
> **censada** no es mas seguro que uno sobre nomina reconstruida. **El censo
> tambien corta.**

### 24.2 LA LISTA DE LOS VEINTE YA BLOQUEA LECTURAS

**Puesto 798, y es la primera vez.**

> `preguntas_ipo_dolor_cliente` es uno de los **veinte nodos que declaran dos
> obras y nunca entraron a la cola de las 128**. Sus siete pasos se parten a la
> vista: **1 a 4 son las preguntas IPO de Blank** y **5 a 7 son preguntas de
> problema de Rackham**.
>
> Y `preguntas_problema_2` **solapa exactamente con el bloque injertado**. Por el
> TOQUE UNICO, el par se lee despues de la cirugia.
>
> **LO QUE ESTO PRUEBA: la lista de los veinte no era una curiosidad de censo.**
> Bloquea lecturas igual que las 128, y **ninguno de esos veinte tiene todavia
> ficha de anatomia propia.**

### 24.3 Lo demas del tramo

> **1. LA FAMILIA DE GARANTIAS FEDERALES, contada del archivo: ONCE nodos y
> TREINTA Y NUEVE pares leidos, con 38 D y una sola B. CERO A.** Es, con
> diferencia, **la familia mejor escrita del nucleo**: once nodos que se rozan
> todo el tiempo en el vocabulario y no repiten ni una vez.
>
> **2. La vara sale por el lado que menos se usa** (puesto 793): `estimacion_tres_puntos`
> desarrolla el metodo de tres puntos de su madre y **lo que anade cabe en una
> linea**, el nombre de la ponderacion Beta. **REPITE.** Es el primer caso donde la
> vara confirma una A en vez de tumbarla.
>
> **3. La familia de los tres circulos tiene DOS nodos** (puesto 795):
> `circulos_busqueda_cofundadores` y `seleccion_relaciones_cofundadores`, con su
> par ya leido en el 187 en **B**. **La madre no enlaza a ninguno de los dos.**
>
> **4. `design_test_repeat` acumula su segundo gemelo** (puesto 796, con el 723).
> Cuatro pasos, dos gemelos y ninguna arista propia. **Es el nodo que sostuvo dos
> veredictos de la familia del encaje** y cada lectura nueva lo deja mas suelto.

---

## 25. EL TRAMO 801 a 812: las familias grandes empiezan a chocar entre ellas

**Doce pares leidos, los doce del nucleo.** Acumulado **812 de 3.388**, global
**31,0%** de A y **nucleo 38,2%**. El tramo dio **33,3%**. **El proximo
checkpoint es el de los 900.**

### 25.1 EL RACIMO DE LAS PUERTAS LLEGA A CINCO PARES Y LOS CINCO EN A

**Puesto 801**, con el 275, 302, 356 y 745.

> **Cinco fusiones distintas sobre los mismos ocho nodos**, y ninguna se puede
> ejecutar sin deshacer las otras cuatro. **Es el argumento mas fuerte del archivo
> a favor del PROGRAMA UNICO** que el 275 pidio: no son cinco podas, es una sola
> decision de arquitectura.

### 25.2 LA FAMILIA FINANCIERA DE LA VALIDACION, cuatro nodos y tres que se solapan

| nodo | puesto | clase |
|---|---:|:---:|
| `metrics_that_matter_framework` contra `verificar_modelo_ingresos` | 791 | **A** |
| `validar_modelo_financiero` contra `verificar_modelo_ingresos` | **807** | **A** |
| `revenue_pricing_hypothesis` contra `verificar_modelo_ingresos` | 679 | D |

> **Tres nodos dicen casi lo mismo con nombres distintos** y el cuarto,
> `revenue_pricing_hypothesis`, se salva porque es la hipotesis previa y no el
> calculo. **Sin censar todavia**, y cada uno aporta una pieza real: el numero de
> pivotes que quedan, los tres escenarios, y el estado de resultados multianual
> para inversionistas.

### 25.3 EL MARCO DE LAS CUATRO ETAPAS SALE SANO CONTRA DOS DE SUS CUATRO

**Puesto 805, tras el 775.** `cuatro_etapas_llamada_de_ventas` **enfrentado a la
apertura y a la investigacion, y sano las dos veces**, con la vara resolviendolo
sin deliberacion: su paso sobre cada etapa es **una linea** y el nodo de la etapa
trae **el procedimiento**.

> **Eso lo confirma como MARCO y no como hermano**, que es lo que ya se habia
> dicho en el 775 por la via de las aristas. **Dos metodos distintos, misma
> conclusion.**

### 25.4 LA FAMILIA DE LOS REGALOS SE SALVA POR CONTRADECIRSE, otra vez

**Puesto 812.** `celebracion_hitos_cliente` manda un gesto **alineado con la
marca**; `sorprender_cliente_estrategico` prohibe **el logo y los mensajes de
marca** en el regalo.

> **Es la segunda vez que esta familia se salva por la misma contradiccion**, tras
> el puesto 564. **La marca en el regalo es la linea divisoria de esta familia**, y
> ya hay dos pares donde eso es lo unico que separa a los nodos.
>
> **Para la mesa eso es una decision de contenido, no de arquitectura**: alguien
> tiene que decidir si el regalo lleva marca o no, y **la respuesta determina
> cuantos nodos quedan.**

### 25.5 Dos familias mas que piden contador antes que mesa

> **1. LOS DATOS DEL CLIENTE de Coleman, CUATRO nodos vistos** (puestos 657, 687,
> 811 y el de seguimiento del 317): `investigar_datos_cliente`,
> `conexion_personal_emocional`, `personalizacion_investigacion_prospecto` y
> `seguimiento_informacion_cliente`. **Los pares se contradicen segun con quien se
> compare**: sanos unos contra otros y dudoso el 811. **Sin contar la familia no se
> decide nada.**
>
> **2. LA VOZ DEL CLIENTE, CINCO nodos vistos** (puesto 806), y uno de ellos,
> `voz_del_cliente_voc`, **es costura confirmada que bloquea dos pares**. **No se
> puede decidir de a pares mientras el nodo grande siga sin operar.**

---

## 26. EL TRAMO 813 a 824: el nodo mejor cableado del cribado

**Doce pares leidos, los doce del nucleo.** Acumulado **824 de 3.388**, global
**30,9%** de A y **nucleo 38,0%**. El tramo dio **25,0%**. **El checkpoint de los
900 es el proximo.**

### 26.1 EL NODO MEJOR CABLEADO QUE HA SALIDO, y es el superviviente natural

**Puesto 815.** `ocho_fases_experiencia_cliente` **enlaza a las OCHO fases, al
otro programa, a la serie de los seis medios y a la aplicacion de la bienvenida.**

> **En un archivo donde la averia dominante es el cero enlazados**, este nodo es
> la excepcion medida. **Y eso lo convierte en el candidato natural a superviviente
> cuando los dos programas de Coleman se fundan**, decision que el puesto 326 dejo
> confirmada a ciegas en la relectura R16.
>
> **Fundir hacia el nodo bien cableado es gratis; fundir hacia el otro obliga a
> reconstruir doce aristas.** Es la primera vez que el cribado puede recomendar
> una direccion de fusion **por la forma del grafo y no por el contenido.**

### 26.2 LA VARA RESOLVIO CUATRO PARES DEL TRAMO SIN DELIBERAR

| puesto | madre | lo que el hijo anade | clase |
|---:|---|---|:---:|
| **813** | `ciclo_de_conversion_de_efectivo` | politica de pagos y riesgo reputacional | **D** |
| **816** | `get_out_building_test_sell` | umbrales, CAC contra precio, clasificacion de reacciones | **D** |
| **821** | `diez_principios_prototipado` | materiales y escala de tiempo | **D** |
| **822** | `comparacion_metodos_inversion` | para que NO sirve el payback | **D** |

> **Cuatro de doce pares del tramo los resolvio la vara en una linea de razon.**
> Antes de nombrarla, cada uno de esos habria sido una discusion.

### 26.3 UNA TENSION ENTRE LIBROS que no es contradiccion pero decide

**Puesto 817.** `business_model_canvas_vs_plan` de Blank dice que el lienzo
**reemplaza** al plan de negocio. `business_plan_cinco_secciones` de Osterwalder
**escribe el plan** y mete el lienzo dentro como una de sus cinco secciones.

> **No se contradicen en un paso: se contradicen en la recomendacion.** El
> catalogo hoy le dice al lector las dos cosas segun por donde entre.
>
> **Y no se arregla fusionando**, porque los dos textos son correctos en su libro.
> **Se arregla decidiendo que recomienda el catalogo**, que es una decision de voz
> y no de arquitectura. **Anotada para la mesa.**

### 26.4 Familias que avanzan, contadas del archivo

> **1. LOS DESPIDOS: cinco nodos, diez pares posibles, SIETE leidos** (cinco D y
> dos B). **Le faltan tres** y ya tiene dos dudosos dentro: **va a salir mezclada,
> no pura**, pero es barata de cerrar.
>
> **2. LA META DE TRACCION: tres nodos, dos pares leidos y los dos en A** (627 y
> 824). **Tres nodos para una sola idea y ninguno enlaza a otro.**
>
> **3. EL SCORECARD DE PUERTAS: tres nodos vistos** (184, 820), con el 820 en
> **A**.
>
> **4. `verificar_product_market_fit` llega a ONCE pares leidos y sigue en CERO
> A.** Es el ejemplar mas puro de la figura de la seccion 21.2: **se roza con
> todos y no repite con ninguno.**

### 26.5 La costura que NO bloqueo, y por que

**Puesto 823.** `brainstorming_divergente` es costura confirmada, **pero el par
se juzgo igual.**

> **El solape con `brainstorming_efectivo` cae completo en los pasos 1 a 4**, el
> taller de Tim Brown, **y la juntura esta en el paso 5**, donde arranca el bloque
> de Mollick. **Por el refinamiento del puesto 673, un solape que no cruza la
> juntura no bloquea.**
>
> **Es el contraejemplo util**: de los cuatro nodos costurados que han entrado a
> pares, **tres bloquearon y este no**. La diferencia no es el nodo: **es donde
> cae el solape.**

---

## 27. EL TRAMO 825 a 830: los nodos costurados empiezan a costar de verdad

**Seis pares leidos, los seis del nucleo.** Acumulado **830 de 3.388**, global
**30,7%** de A y **nucleo 37,6%**. **El tramo dio CERO A**, y la mitad de sus
pares quedo bloqueada. **El checkpoint de los 900 es el proximo.**

### 27.1 LA CUENTA DE LO QUE LAS COSTURAS ESTAN CONGELANDO

**Contada del archivo con la regla del banco 9.9 delante.**

| nodo costurado | pares que bloquea | puestos |
|---|---:|---|
| `voz_del_cliente_voc` | **3** | 724, 755, **827** |
| `producto_minimo_viable` | **2** | 592, **830** |
| `lienzo_modelo_negocio` | 1 | 784 |
| los dos de A/B | 1 | 738 |
| `preguntas_ipo_dolor_cliente` | 1 | 798 |
| `key_partners_hypothesis` y `asociaciones_clave` | 1 | 599 |

> **Nueve pares congelados por seis nodos.** Y la cuenta va a seguir subiendo,
> porque **estos nodos son grandes y por eso entran a muchos pares.**
>
> **Lo que esto cambia para el plan**: la cirugia de costuras dejo de ser un
> frente paralelo. **Cada nodo que se opera libera lecturas del otro eje**, y
> `voz_del_cliente_voc` solo ya vale tres.

**Y el 827 trae el caso extremo: LOS DOS nodos del par estan costurados.**
`ganar_comprension_del_cliente` es ademas uno de los ocho ejemplares de **LA
FORMA QUE PARTE**, con once pasos partidos entre la comprension del cliente y el
montaje del CRM.

### 27.2 LA VARA Y LA POSICION DEL SOLAPE, trabajando juntas en el mismo tramo

**Las dos reglas nuevas resolvieron cuatro de los seis pares sin deliberar:**

| puesto | regla | resultado |
|---:|---|---|
| **825** | la vara (9.6.1) | el hijo trae el procedimiento de crear mercado: **CONTINUA**, D |
| **827** | la posicion del solape (9.9) | el solape toca juntura **por los dos lados**: **bloquea**, B |
| **830** | la posicion del solape (9.9) | el solape es una orden que el emblema **repite cuatro veces**: **bloquea**, B |
| 829 | ninguna, lectura directa | programa contra pieza: **D** |

> **Antes de que las dos reglas existieran, estos cuatro habrian sido cuatro
> discusiones.** Ahora son cuatro lineas de razon con la anatomia de la ficha
> delante.

### 27.3 UNA ARISTA QUE FALTA DENTRO DEL NODO MEJOR CABLEADO

**Puesto 829.** `ocho_fases_experiencia_cliente` enlaza a **siete** de las ocho
fases y **no enlaza a `fase_adopt_ciclo_cliente`**.

> **Es la arista que falta mas barata del archivo**: un solo enlace, dentro del
> nodo que el puesto 815 midio como el mejor cableado de todo el cribado, **y que
> el banco 9.8 acaba de nombrar superviviente del programa unico de Coleman.**
>
> **Conviene arreglarla antes de la fusion, no despues**: si el superviviente nace
> con siete de ocho, la octava se pierde en el traslado.

### 27.4 Lo demas anotado

> **1. La familia de la cultura de innovacion, DOS nodos de dos libros** (puesto
> 828), sin citarse: uno mira lo que el lider **hace** con su tiempo, el otro mira
> el **clima** de la oficina. **Sin censar.**
>
> **2. Los dos hijos de `preparacion_materiales_fundraising` salen sanos entre
> si** (puesto 826): el resumen ejecutivo y el deck son artefactos distintos, con
> arista en los dos sentidos. **La madre sigue sin enlazar a ninguno de los dos**,
> que es la arista que falta del banco 9.6 ya registrada.
>
> **3. `tipo_de_mercado_estrategia_competitiva` repite con su gemelo y continua
> con su hijo** (puestos 686 y 825). **Es el ejemplo mas limpio de para que sirve
> la vara**: el mismo nodo, dos vecinos, dos clases distintas y ninguna
> discusion.

---

## 28. EL TRAMO 831 a 836: aparece la tercera causa de bloqueo

**Seis pares leidos, los seis del nucleo.** Acumulado **836 de 3.388**, global
**30,7%** de A y **nucleo 37,6%**. El tramo dio **33,3%**. **El checkpoint de los
900 es el proximo.**

### 28.1 LA TERCERA CAUSA DE BLOQUEO: el nodo que va a la CURA ACOPLADA

**Puesto 835.** `producto_unico_superior` es costura **confirmada** y ademas
**tiene gemelo declarado** (puesto 285), o sea que esta en la lista de los que
necesitan **cura acoplada**: destejido y fusion en el mismo acto.

> **El solape de este par NO toca la juntura**, asi que por el banco 9.9 no
> deberia bloquear. **Y aun asi bloquea**, por otro motivo: **la cura acoplada no
> reescribe un bloque, reescribe el nodo entero.** Lo que sobreviva no se parece
> a lo que hay hoy ni en la parte que el solape toca.

**Las tres causas de bloqueo, ya separadas:**

| causa | regla | ejemplares |
|---|---|---|
| el solape **toca la juntura** | banco 9.9 | 724, 755, 784, 798, 827, 830, 831, 599, 738 |
| el nodo va a **cura acoplada** | esta seccion | **835** |
| **ninguna**: el solape cae en un bloque que sobrevive | banco 9.9 | 823, 834, **344** |

> **La diferencia practica es de orden**: los del primer grupo se releen **despues
> de la cirugia de su nodo**; el del segundo, **despues de la cirugia Y de la
> fusion**. **Es un puesto mas atras en la cola.**

### 28.2 LA CUENTA DE CONGELADOS SUBE A ONCE

| nodo a operar | pares que libera |
|---|---:|
| `voz_del_cliente_voc` | **3** (724, 755, 827) |
| `producto_minimo_viable` | **2** (592, 830) |
| `lienzo_modelo_negocio` | 1 (784) |
| `ab_testing_optimizacion` + `split_testing_experimentos_ab` | 1 (738) |
| `preguntas_ipo_dolor_cliente` | 1 (798) |
| `key_partners_hypothesis` + `asociaciones_clave` | 1 (599) |
| **`estrategia_crecimiento_clientes`** | **1** (831) |
| **`producto_unico_superior`** (cura acoplada) | **1** (835) |

> **ONCE pares congelados por OCHO nodos.** Eran nueve por seis hace seis
> lecturas. **La cuenta sube porque los nodos costurados son grandes y por eso
> entran a muchos pares**, y va a seguir subiendo mientras la cirugia no arranque.

### 28.3 LA SEGUNDA DE LOS VEINTE ENTRA A UN PAR, y bloquea

**Puesto 831.** `estrategia_crecimiento_clientes` es uno de los **veinte nodos que
declaran dos obras y nunca entraron a la cola de las 128.**

> Sus diez pasos se parten a la vista: **1 a 6 el Grow de Blank**, **7 a 10 el
> programa de referidos de Coleman**. Y el par solapa con **los dos bloques**.
>
> **Van dos de veinte, y las dos bloquearon** (798 y este). **La lista de los
> veinte se comporta exactamente igual que las 128**, con el agravante de que
> **ninguno de esos veinte tiene anatomia escrita**: hay que abrirlos uno por uno
> cuando les toque.

### 28.4 Lo demas del tramo

> **1. La familia de la sucesion llega a DOCE pares leidos** (puesto 832), y el
> nodo nuevo aporta lo que ninguno de los otros once: **el co-CEO o el COO
> complementario como alternativa al reemplazo total.**
>
> **2. `errores_comunes_asignacion_roles` acumula su segundo gemelo** (673 y
> **833**). **La familia de los titulos del equipo fundador pide contador.**
>
> **3. Segundo par del racimo del brainstorming que se juzga pese a la costura**
> (puesto 834, con el 823): **las dos veces el solape cayo en los pasos 1 a 4.**
> Lo que se pierde aqui es la **inmersion previa** antes de la sesion, que no esta
> en ningun otro nodo del racimo.


---

## 29. EL TRAMO 837 a 842: el par que CRUZA dos parejas y funda una familia

**Seis pares leidos, los seis del nucleo.** Acumulado **842 de 3.388**, global
**30,8%** de A y **nucleo 37,6%**. El tramo dio **33,3%**. **El checkpoint de los
900 es el proximo.**

### 29.1 LA ETNOGRAFIA DE CAMPO: SEXTO SUB-PURO, y nace de un cruce

**Puesto 839.** El archivo tenia **dos parejas de etnografia declaradas y
separadas**, cada una dentro de su libro, **y ningun par cruzado leido**:

| puesto | pareja | libro | clase |
|---:|---|---|:---:|
| **381** | `etnografia_aplicada_en_equipos_multidisciplinarios` contra `etnografia_de_proyecto` | *Change by Design* (Brown) | **A** |
| **230** | `etnografia_investigacion_usuario` contra `investigacion_etnografica_ideacion` | *Winning at New Products* (Cooper) | **A** |

> **Este par es el cruce, y sale A.** Los dos libros mandan el mismo instrumento
> con los mismos gestos: elegir un entorno de uso real, observar en contexto en
> vez de preguntar, traducir lo observado en insights, y montar el equipo con las
> habilidades para observar e inferir.
>
> **No son dos parejas vecinas: son CUATRO nodos del mismo instrumento.** Es la
> misma pregunta que el racimo de la seccion 11 tiene abierta con su puesto 1211,
> **y aqui ya esta contestada.**

**EL CONTADOR PRIMERO, como manda el banco 9.5.** `contar_nombre.py` levanta
**siete** vivos con el termino; **la lectura deja fuera a tres, con su motivo**:

| nodo | por que no entra |
|---|---|
| `netnografia_social_media` | **monitorea foros y redes**: no hay campo ni observacion presencial |
| `diseno_mas_alla_del_individuo` | su objeto son las **dinamicas de grupo**; la etnografia en video es un paso suyo, no su asunto |
| `equipos_visita_cliente` | **entrevista con guia estructurada**, y ya salio **D** contra un miembro en el puesto 722 |

**LA NOMINA: CUATRO miembros.**

| | |
|---|---:|
| miembros | **4**: `etnografia_de_proyecto`, `etnografia_aplicada_en_equipos_multidisciplinarios`, `etnografia_investigacion_usuario`, `investigacion_etnografica_ideacion` |
| pares posibles | **6** |
| en la cola | **3** |
| **leidos** | **3**, y **los TRES en A** (230, 381, 839) |
| **nunca en cola** | **3** |
| aristas internas | **1**, la de la pareja de Brown; los dos de Cooper **aislados entre si y del resto** |

> **SUB-PURO por la condicion dura**: todo lo leido repite, pero **la mitad de los
> pares posibles nunca entro a la cola**, asi que la familia no esta cerrada.
> **Entra a la tabla viva de los puros del banco 9.5 como el numero 6.**
>
> **Y es el sub-puro mas barato de cerrar de los tres**: le faltan **tres
> lecturas** y **ninguna esta en la cola**, o sea que son tres lecturas
> encargadas, no tres esperas.

### 29.2 LA FAMILIA DE LOS LOTES QUEDA LEIDA ENTERA, y su B pide relectura

**Puesto 837.** Con este par, **los tres pares posibles de la familia estan
leidos**, que es la primera vez en varios tramos que una familia se cierra sola:

| par | nodos | clase |
|---:|---|:---:|
| **215** | `espiral_mortal_lotes_grandes` contra `espiral_muerte_lotes_grandes` | **B** |
| **680** | `espiral_muerte_lotes_grandes` contra `trabajo_en_lotes_pequenos` | **D** |
| **837** | `espiral_mortal_lotes_grandes` contra `trabajo_en_lotes_pequenos` | **D** |

> **Los dos D dicen lo mismo con el mismo motivo**: cada espiral es un
> **diagnostico** y el nodo de los lotes pequenos es el **tratamiento**. Y los dos
> diagnosticos **miran cosas distintas**: uno las senales de calendario, fechas
> que se posponen y arreglos de ultimo momento; el otro los **traspasos entre
> especialidades** y el retrabajo por lanzamiento.

> **LO QUE ESTO LE HACE AL 215, y va como PROPUESTA, no ejecutado.** Ese B se
> emitio por una figura de nombre, *ids casi identicos dentro del nucleo*, con la
> observacion de que **recetan cosas distintas**. Hoy hay evidencia nueva que
> entonces no existia: **los dos espirales han sido leidos contra el mismo
> tratamiento y los dos dieron D por la misma razon.** Eso dice que son **dos
> diagnosticos complementarios del mismo fenomeno**, no un nodo contado dos veces.
>
> **Recomiendo relectura del 215 con esta evidencia delante.** No lo muevo: es un
> veredicto emitido y la relectura de las A tiene su cauce.

> **EJECUTADA el 13 ago 2026, aprobada por el auditor. El 215 pasa de B a C, SANO
> CON FIGURA, con correccion declarada dentro de su razon.** Verificado paso por
> paso: **ni uno solo se solapa entre los dos espirales.** Uno mira el
> **calendario** y receta un tope de lote; el otro mira los **traspasos** y receta
> juntar diseno e ingenieria.
>
> **La FIGURA se conserva y es la que sostiene la C**: ids casi identicos, mismo
> libro, mismo nombre de concepto. **Un lector los va a tomar por el mismo nodo
> aunque no lo sean**, y eso es problema de NOMBRE: **su arreglo es renombrar para
> que se distingan, no fundir.**
>
> **Efecto en el marcador: una B menos y una C mas**, y la familia de los lotes
> queda cerrada sin ninguna duda dentro. **Es la quinta C del archivo.**

### 29.3 Lo demas del tramo

> **1. UNA ARISTA QUE FALTA de las baratas** (puesto **841**):
> `customer_discovery_cuatro_fases` **invoca la prueba de pasa o no pasa dentro de
> su fase 3** y **no enlaza** a `realizar_pruebas_pasa_no_pasa`, que es el nodo
> que la ejecuta. Del banco 9.6, un solo enlace.
>
> **2. El grafo no sabe que dos nodos son el mismo principio** (puesto **840**):
> `genchi_gembutsu` y `genchi_gembutsu_salir_del_edificio` comparten **la raiz del
> id, el libro y la palabra japonesa**, repiten entero, y **no tienen arista entre
> ellos.** El censo por script no levanta a nadie mas: **dos vivos, cero
> deprecados.** Es la fusion mas limpia del tramo.
>
> **3. El frente del Stage-Gate llega a SIETE nodos leidos** (puesto **838**),
> entre etapas, puertas y sistemas. Este par sale **D** porque es la alternancia
> canonica, la etapa hace y la puerta decide, **pero el frente entero sigue
> pidiendo mesa** y no pareja por pareja, como ya quedo dicho en el 356.


---

## 30. EL TRAMO 843 a 848: dos tablas que envejecieron, y el racimo del pivote pide mesa

**Seis pares leidos, los seis del nucleo.** Acumulado **848 de 3.388**, global
**30,7%** de A y **nucleo 37,4%**. **El tramo dio 16,7%**, el mas sano en varios
tramos. **El checkpoint de los 900 es el proximo.**

### 30.1 CUATRO VEREDICTOS VOLTEADOS QUE DOS TABLAS SEGUIAN MOSTRANDO EN VERDE

**Encontrado al preparar el puesto 848, y es el hallazgo del tramo.** Iba a
declarar `retention_metrics` como **noveno ejemplar de la cura acoplada** apoyado
en la tabla de las veinte costuras fuera de cola, que le atribuye un **522 A**.

> **El archivo dice que el 522 es D.** Y no es un error del archivo: **el 522 fue
> una de las diecinueve que la ejecucion de la ratificacion volteo de A a D**, con
> su motivo escrito, *el hijo trae el procedimiento entero de cohortes*.
>
> **Lo que fallo no fue la lectura: fue que el volteo actualizo los veredictos y
> no las tablas que los citan.**

**LOS CUATRO, verificados uno por uno contra el archivo:**

| puesto | par | la tabla decia | el archivo dice | donde estaba stale |
|---:|---|:---:|:---:|---|
| **490** | `fit_problema_solucion` | **A** | **D** | ficha, tabla de los veinte |
| **497** | `fit_problema_solucion` | **A** | **D** | ficha, tabla de los veinte |
| **522** | `metricas_cohortes` contra `retention_metrics` | **A** | **D** | ficha **y** seccion 7 de este informe |
| **624** | `estrategia_get_keep_grow` contra `keep_customers_strategy` | **A** | **D** | ficha, tabla de los veinte |

> **Los cuatro son del mismo grupo**: el de *cero hijos de paso enlazados* que la
> ratificacion resolvio con la vara. **No es azar: es que un volteo en bloque toca
> muchas filas de una vez y nadie barrio las tablas detras.**

**LO QUE ESTO CAMBIA, y hay que decirlo por separado porque son dos cosas:**

> **1. Un hecho, corregido aqui**: **`retention_metrics` NO va a cura acoplada.**
> Su unica A aparente era el 522. Con el 522 en D, lo que le queda es **un B (233)
> y un D (522)**, y **un nodo sin gemelo declarado no tiene con quien fundirse**:
> su cirugia es partirlo en dos y ya. **Lo mismo vale para
> `keep_customers_strategy`** (210 B, 624 D) **y para `fit_problema_solucion`**,
> que pasa de parecer un triplicador (tres A) a tener **una sola A y dos D**.
>
> **2. Dos interpretaciones que dependian de esas cifras, y NO las re-adjudico**:
> la seccion 7 llamo a `retention_metrics` **el gemelo** del racimo de las
> metricas de cohorte y lo propuso como ejemplar de la figura **CENTRO SANO CON
> GEMELO SIN CASA**. **Las dos descansaban en el 522 en A.** Corrijo la cifra y
> **dejo las dos lecturas marcadas para el auditor**, porque cambiarlas es
> adjudicar, no corregir.

> **LA REGLA QUE ESTO PIDE, propuesta y sin aplicar**: **toda tabla que cite un
> veredicto por numero se recomputa del archivo, no se copia**, y **todo volteo en
> bloque barre las tablas derivadas en el mismo acto.** Una tabla que cita un
> veredicto viejo **no falla: dice que si**, que es la forma peor. **Es
> exactamente el canon de fallar ruidoso aplicado a los papeles.**

### 30.2 EL RACIMO DEL PIVOTE: cinco censados, SIETE por lectura, y cuatro sin decidir

**Puestos 843 y 846.** El censo del racimo `Pivotar o proceder` dice **cinco
miembros**. **La lectura levanta dos mas** y los dos con evidencia dentro del
archivo:

| nodo que la nomina no tiene | por que entra |
|---|---|
| `pivote_o_proceder` | **repite (268 A)** con `pivotar_o_proceder`, que **si** esta en la nomina |
| `decision_pivote_perseverar` | es la misma decision desde *The Lean Startup* mas *Traction*, y **ya tiene dos pares internos en la cola** |

**Dejado FUERA por lectura**: `war_room_pivot_proceed`, cuyo objeto es **montar la
sala** (cubrir una pared con el lienzo, otra con las hipotesis, un pizarron), no
tomar la decision.

| | |
|---|---:|
| miembros | **7** |
| pares posibles | **21** |
| en la cola | **10** |
| **leidos** | **5**: 268 **A**, 594 **D**, 598 **D**, 771 **B**, **843 B** |
| pendientes de cola | **5** (860, 957, 968, 1140, 1305) |
| **nunca en cola** | **11** |
| aristas internas | **2** entre siete |

> **EL SALDO DICE UNA COSA CLARA Y DEJA OTRA ABIERTA.** Dentro de Blank ya esta
> resuelto: **la misma puerta contada dos veces REPITE** (268) y **puertas
> distintas del proceso son SANAS** (594, 598). **Lo que no se resuelve es el
> cruce entre libros**: Ries entra por las metricas, Blank por la reunion, y los
> dos pares que lo miden estan en **B** (771 y 843).
>
> **LO QUE LA MESA TIENE QUE DECIDIR, ahora nombrado**: si el catalogo quiere **un
> nodo de decision por LIBRO** o **un nodo por PUERTA del proceso**. Con la
> segunda respuesta los pares cruzados caen solos; con la primera, tambien, pero
> al reves. **Sin esa respuesta se van a seguir acumulando B en esta zona**, y ya
> van dos.

### 30.3 Lo demas del tramo

> **1. LA RELACION MAS SANA DE VARIOS TRAMOS** (puesto **845**): `metodo_payback`
> **nombra a NPV dentro de sus propios pasos** como el metodo con el que hay que
> complementarlo. **El catalogo no solo los tiene separados: sabe para que sirve
> cada uno y lo dice en el texto.** Es el contraejemplo util de todo lo demas que
> este informe cuenta.
>
> **2. OTRA ARISTA QUE FALTA de las baratas** (puesto **846**), y con una
> condicion: `customer_discovery_overview` invoca la decision de pivotar en su
> fase 4 y no enlaza al nodo que la ejecuta. **Pero esa madre ya tiene gemelo
> declarado** (puesto 156, con `customer_discovery_cuatro_fases`), asi que **la
> arista hay que crearla desde el superviviente de esa fusion, no desde el nodo de
> hoy**. Es la segunda arista que falta del mismo tipo en dos tramos: la del 841
> es la misma madre con otra fase.
>
> **3. TERCERA vez que `brainstorming_divergente` entra a un par y se juzga pese a
> la costura** (puesto **844**, con el 823 y el 834). **Las tres veces el solape
> cayo en sus pasos 1 a 4**, el bloque de Tim Brown que la cirugia deja en pie.
> **Ya no es casualidad: el injerto de Mollick vive en la mitad del nodo que nadie
> toca al compararlo**, y por eso este nodo se puede seguir leyendo sin esperar a
> su cirugia.


---

## 31. ADJUDICACION DEL RACIMO DE COHORTES, y el RECUENTO de la figura entera

**Adjudicado por el auditor el 13 ago 2026**, a raiz de los cuatro veredictos
volteados de la seccion 30.1.

### 31.1 LA ADJUDICACION: de GEMELO SIN CASA a MIEMBRO SIN ARISTA

> **Con el 522 en D, `retention_metrics` deja de ser GEMELO y pasa a ser MIEMBRO
> SIN ARISTA.** No repite al centro: **simplemente nadie lo enlazo.** Y eso lo
> saca de la figura de la seccion 5 y lo mete en **LA ARISTA QUE FALTA**, banco
> 9.6, que es la clase de arreglo mas barata que existe.
>
> **El centro sigue sano.** `metricas_accionables` toca a tres de los otros cuatro
> y nada de eso cambia.

**Y el arreglo del racimo queda en UNA decision, no en dos:**

| antes (con el 522 en A) | ahora |
|---|---|
| **dos** decisiones: resolver el gemelo **y** fundir el par del 353 | **una**: partir `retention_metrics` por su propia costura y **enlazar su mitad de retencion al centro** |
| la fusion venia **pegada** a la cirugia | **no hay fusion pegada**: se parte y se enlaza |

> **La cirugia no cambia: sigue siendo partirlo en dos por el corte del paso 6**,
> que es lo que la ficha ya tenia escrito. **Lo que cambia es lo que pasa despues**:
> antes habia que decidir si absorberlo, ahora solo hay que **enlazar la mitad que
> queda**. **El par del 353 sigue siendo la otra decision del racimo y no se
> toca.**

### 31.2 EL RECUENTO DE LA FIGURA: ocho candidatos, TRECE gemelos, TRES probados

**Recontado contra el grafo y contra el archivo, uno por uno.** La prueba que se
exige a cada gemelo es la que el auditor fijo: **aristas o un par A VIGENTE.**

> **LA DISTINCION QUE EL RECUENTO OBLIGA A NOMBRAR, y no la habia**: **AISLADO no
> es GEMELO.**
>
> **Cero aristas** es un hecho del **grafo** y dice *nadie lo enlazo*. **Gemelo**
> es un hecho de **lectura** y dice *repite al centro*. **La figura necesita las
> dos mitades**, y hasta hoy se estaba declarando con una sola.

| candidato | gemelo declarado | aristas | par A vigente | veredicto |
|---|---|:---:|---|---|
| el lienzo de propuesta de valor | `customer_profile_value_map` | 0 | **475 A y 477 A** | **PROBADO, por partida doble** |
| el capital de trabajo (203) | `dso_dpo_gestion_capital_trabajo` | 0 | **653 A** | **PROBADO** |
| la iluminacion de Wallas | `intimation_illumination` | 0 | **403 A** (con un miembro, no con el centro) | **PROBADO** |
| **las metricas de cohorte** | **`retention_metrics`** | 0 | **522 volteado a D**, y 233 en B | **SALE**, ver 31.1 |
| el lienzo de propuesta de valor | `desarrollo_value_proposition_usp` | 0 | ninguno | **SIN PROBAR** |
| Auditoria de calidad | `auditoria_calidad` | 0 | ninguno | **SIN PROBAR** |
| Auditoria de calidad | `reporte_auditoria` | 0 | ninguno | **SIN PROBAR** |
| Mapeo del flujo de valor | `analisis_flujo_de_valor` | 0 | ninguno | **SIN PROBAR** |
| Mapeo del flujo de valor | `value_stream_mapping_ambiental` | 0 | ninguno | **SIN PROBAR** |
| Cinturones de Six Sigma | `desarrollo_expertos_capaces` | 0 | ninguno | **SIN PROBAR** |
| Cinturones de Six Sigma | `rol_facilitador_black_belt` | 0 | ninguno | **SIN PROBAR** |
| Los puntos de Deming | `eliminar_slogans_metas` | 0 | ninguno | **SIN PROBAR** |
| Los puntos de Deming | `mejora_continua_del_sistema` | 0 | ninguno | **SIN PROBAR** |

> **TRECE gemelos declarados en OCHO candidatos. TRES probados, UNO fuera, y NUEVE
> sin una sola lectura que los respalde.** Los nueve se declararon **por la
> forma**: cero aristas dentro de su racimo, que es verdad y es todo lo que se
> midio.

**Y LO QUE HACE FALTA PARA PROBARLOS NO VA A LLEGAR SOLO:**

| gemelo sin probar | par interno pendiente en la cola |
|---|---|
| `auditoria_calidad` | **2659 y 3229**, los dos muy lejos |
| **los otros OCHO** | **NINGUNO: nunca entraron a la cola** |

> **Ocho de los nueve no tienen ni un par interno en la cola entera de 3.388.** El
> cribado **no los va a contestar nunca**, por muchos tramos que avance. **Si se
> quieren probar, es por encargo**, un par cada uno, nueve lecturas en total.
>
> **Mientras tanto la cifra honesta de la figura es TRES ejemplares probados**, no
> ocho candidatos. **Los nueve siguen siendo candidatos por forma y quedan
> nombrados como tales**, no borrados.

### 31.3 UNA TRAMPA DE MEDICION QUE CASI CUELA: la AUTO-ARISTA

**Al medir las aristas internas, `analisis_flujo_de_valor` aparecio con una y
estuve a punto de registrarlo como correccion al barrido de la seccion 6.**

> **Era el nodo enlazandose a si mismo.** `analisis_flujo_de_valor` se lista
> dentro de sus propios `nodos_previos`, y al resolver alias el enlace vuelve a
> el. **El barrido de la seccion 6 estaba bien y mi medicion estaba mal.**
>
> **Contadas en el grafo vivo: VEINTISIETE nodos tienen auto-arista.** No es un
> caso raro.

> **Lo que esto pide, y va como nota al plan**: **todo conteo de grado o de
> aislados tiene que excluir el propio nodo**, o los aislados dejan de parecerlo.
> Es una linea de codigo y una fuente de falsos negativos que ya me alcanzo una
> vez.

---

## 32. EL TRAMO 849 a 854: la segunda anatomia fuera de cola, escrita aqui

**Seis pares leidos, los seis del nucleo.** Acumulado **854 de 3.388**, global
**30,8%** de A y **nucleo 37,5%**. **El tramo dio 50%**, el mas cargado de A en
varios tramos. **Faltan 46 para el checkpoint de los 900.**

### 32.1 LA SEGUNDA COSTURA FUERA DE COLA CON ANATOMIA ESCRITA

**Puesto 851.** `procesamiento_paralelo_con_espirales` es uno de los **veinte**,
declara *Winning at New Products* mas *Essentials of Supply Chain Management*, y
**la ficha no tenia su anatomia**: hasta hoy la unica fuera de cola con anatomia
escrita era `retention_metrics`.

| bloque | de que habla |
|---|---|
| **1 a 4** | **Cooper**: areas en paralelo como en el rugby y no como en relevos, versiones tempranas y baratas, ciclos rapidos de prueba con clientes, y repetirlos en cada etapa |
| **5 a 9** | **Hugos**: dividir el proyecto en partes independientes, disenar tareas ejecutables en paralelo, asignar por habilidades multiuso, plan B, y disenar para poder recortar funciones |

> **El duplicado que lo delata es el paso 1 contra el paso 6**: los dos mandan
> trabajar en paralelo y no en cascada, uno hablando de **areas** y otro de
> **tareas**.

**Y ESE MISMO DUPLICADO ES EL SOLAPE DEL PAR**, que es lo que lo bloquea:

> `customer_development_agile_pairing` manda **trabajar agil y no en cascada**, y
> eso **toca el paso 1 y el paso 6 a la vez**, o sea **los dos lados de la
> juntura**. Por el banco 9.9, **bloquea**. Es la misma figura del puesto 830 con
> el emblema: **cuando la orden repetida ES el solape, no hay forma de juzgar sin
> saber cual de las dos copias sobrevive.**

**Van CINCO de los veinte leidos desde que la lista se midio**, y el saldo no
mejora:

| puesto | nodo | clase | motivo |
|---:|---|:---:|---|
| 798 | `preguntas_ipo_dolor_cliente` | **B** | costura |
| 831 | `estrategia_crecimiento_clientes` | **B** | costura |
| 843 | `decision_pivote_perseverar` | **B** | familia sin adjudicar |
| 848 | `retention_metrics` | **D** | solape en el bloque que sobrevive |
| **851** | `procesamiento_paralelo_con_espirales` | **B** | costura, solape sobre la juntura |

> **Cuatro de cinco sin resolver.** La lista de los veinte **se comporta peor que
> la cola de las 128**, y el motivo es de forma: **estos nodos son largos y por eso
> su solape casi siempre encuentra una juntura.**

### 32.2 UN CENTRO QUE NO PARA DE DAR DUDAS

**`customer_development_modelo` entra a DOS pares de este tramo** (849 y 854) y
con ellos llega a **siete pares leidos**:

| clase | puestos |
|---|---|
| **A** | 635 (`customer_discovery`), **849** (`customer_discovery_get_out_of_building`) |
| **D** | 377, **854** |
| **B** | **683, 707, 806** |

> **Repite con DOS nodos de descubrimiento distintos** y **acumula tres dudosos**,
> mas que ningun otro nodo del cribado hasta ahora. **Su zona, la del customer
> development, pide mesa igual que la del Stage-Gate y la del pivote**, y por el
> mismo motivo: **son demasiados nodos contando el mismo proceso desde alturas
> distintas**, y pareja por pareja no se decide.

### 32.3 Lo demas del tramo

> **1. EL FRENTE DEL STAGE-GATE LLEGA A NUEVE NODOS LEIDOS** (puestos **852** y
> **853**, los dos **A**). El 852 repite el scorecard distinto para proyectos
> radicales; el 853 es **la arquitectura de dos niveles contra la practica que ya
> la contiene**, donde lo unico propio de la arquitectura, la distincion entre
> decisiones estrategicas y tacticas, **cabe en una linea**. **La mesa del
> Stage-Gate crece cada tramo y sigue sin convocarse.**
>
> **2. LA ZONA DEL GOBIERNO DE LA JUNTA es de las mas sanas del cribado** (puesto
> **850**): **diez pares leidos y solo dos sin resolver**, el B del 168 y la C del
> 201. Armar la junta y manejarla son cosas distintas y el catalogo lo tiene bien.
>
> **3. OTRA ARISTA QUE FALTA de las baratas** (puesto **854**): la madre del
> customer development **enlaza a `customer_discovery` y a
> `decision_pivotar_o_proceder` y no a `customer_validation`**, que es su segundo
> paso. **Es la tercera del mismo tipo en tres tramos** (841, 846, 854) y las tres
> son madres que nombran un paso y no lo enlazan.

---

## 33. LAS NUEVE LECTURAS DIRIGIDAS: nueve de nueve caen

**Encargo aprobado el 13 ago 2026.** No son lecturas de la cola: son **pares
dirigidos**, cada gemelo declarado contra el centro de su racimo, con la misma
vara del cribado. **Se registran aqui y no en el jsonl**, que solo lleva la cola.

### 33.1 EL SALDO

| | |
|---|---:|
| leidos | **9 de 9** |
| **PROBADOS como gemelo** | **CERO** |
| caen | **9** |
| de esos, de **otro dominio** que su racimo | **3** |

> **La forma sola no acerto ni una vez.** Los tres ejemplares que la figura si
> tiene (`customer_profile_value_map`, `dso_dpo_gestion_capital_trabajo`,
> `intimation_illumination`) **tenian su par A antes de que la figura se
> nombrara**. Los nueve declarados **solo por cero aristas** no sobreviven la
> lectura.

### 33.2 LOS NUEVE, uno por uno

| # | gemelo declarado | contra el centro | veredicto y por que |
|---:|---|---|---|
| 1 | `desarrollo_value_proposition_usp` | `value_proposition_canvas` | **CAE, y ni siquiera es del dominio**: es de **franquicias**, de *Franchise Your Business*, y define la USP de un negocio **franquiciable**, validando con consultas no solicitadas de interesados. El centro es una **herramienta de dos lados** con su plantilla. **Cero solape** |
| 2 | `auditoria_calidad` | `principios_auditoria_calidad` | **CAE**: es de **Crosby** y monta la auditoria, que funcion se audita y contra que criterios, auditores imparciales de otras areas, tiempo para el reporte, autoauditorias verificadas por muestreo. El centro son **los cinco principios de Juran**. Se tocan en **un paso**, formar al auditor |
| 3 | `reporte_auditoria` | `principios_auditoria_calidad` | **CAE**: es **el documento**, resumen ejecutivo y alcance, revisar el borrador con el auditado en reunion de cierre, clasificar hallazgos por gravedad, decidir a quien se entrega, y empezar por lo que si funciona. **Cero solape con los principios** |
| 4 | `analisis_flujo_de_valor` | `ocho_desperdicios_lean` | **CAE, con figura**: mismo instrumento en **arenas distintas**. El centro aplica **la taxonomia de los ocho desperdicios** a un proceso productivo; este aplica el mapeo **al proceso de innovacion**, con lo creido contra lo real, cuatro preguntas por actividad y causa raiz de cuellos de botella. **Ninguno cabe en una linea del otro** |
| 5 | `value_stream_mapping_ambiental` | `ocho_desperdicios_lean` | **CAE, y es de otro dominio**: es de **environmental**, registra entradas de materiales, energia y agua y salidas de scrap, emisiones y residuos peligrosos, con iconos y costos de disposicion. **Es el VSM con datos ambientales**, otro objeto |
| 6 | `desarrollo_expertos_capaces` | `rol_black_belt` | **CAE**: el centro es **el ROL**, seleccionar candidatos, encargarle la nominacion de proyectos, coordinar, certificar. Este es **el SISTEMA DE FORMACION**, linea base de competencias, curriculo por rol y nivel, programa interno de certificacion y medir su impacto. Se tocan en **la certificacion** |
| 7 | `rol_facilitador_black_belt` | `rol_black_belt` | **CAE, y es el mas cercano de los nueve**: los dos son del mismo libro y **el propio centro se distingue en su resumen**, el Black Belt *va mas alla de facilitar equipos*. Este manda asignar facilitador a cada equipo, entrenarlo, usarlo para detectar el estancamiento y **retirar el apoyo poco a poco**. **Actos distintos** |
| 8 | `eliminar_slogans_metas` | `adopcion_liderazgo` | **CAE**: son **dos puntos numerados de Deming**, el 10 y el 7, y el catalogo hace bien en tener los dos. **Se tocan en una instruccion**, dejar las metas numericas, **y ese solape es de Deming, no del catalogo** |
| 9 | `mejora_continua_del_sistema` | `adopcion_liderazgo` | **CAE**: punto **5** contra punto **7**. La calidad desde el diseno, reducir la variacion alrededor del nominal, distinguir apagar incendios de mejorar el proceso. **Cero solape** |

### 33.3 LO QUE ESTO DEJA, y no es solo un saldo

> **1. La figura queda con TRES ejemplares y CERO candidatos pendientes.** Ya no
> hay lista abierta: los nueve estan leidos y los nueve caen. **La seccion 6 de
> este informe queda corregida en ese punto.**

> **2. TRES RACIMOS TIENEN MIEMBROS DE OTRO DOMINIO**, y eso es defecto de
> **nomina**, no de lectura:
>
> | racimo | miembro | su dominio real |
> |---|---|---|
> | el lienzo de propuesta de valor (`core`) | `desarrollo_value_proposition_usp` | **franquicias** |
> | Mapeo del flujo de valor (`quality`) | `value_stream_mapping_ambiental` | **environmental** |
> | Mapeo del flujo de valor (`quality`) | `analisis_flujo_de_valor` | **core** |
>
> **Un racimo con miembros de tres dominios no es una familia: es un grupo de
> nombres parecidos.** Anotado al plan.

> **3. La leccion de metodo, que es la cara util del cero de nueve**: cuando una
> figura **se declara por forma y se prueba por lectura, hay que probarla antes de
> contarla.** Ocho candidatos sonaban a ocho problemas y eran **tres**.

---

## 34. LAS TRES MESAS CONVOCADAS

**Abiertas el 13 ago 2026.** Hasta ahora cada tramo decia *esto pide mesa* y la
frase se quedaba dentro de un veredicto. **Aqui viven las tres, con nomina, motivo
y que decide cada una.**

### MESA 1: EL STAGE-GATE Y SUS PUERTAS, con su cruce de portafolio

| | |
|---|---|
| **nomina medida** | **nueve nodos leidos** del nucleo entre etapas, puertas, sistemas y portafolio |
| **motivo** | pares que repiten dentro de la familia (**356**, **852**, **853**) y **dos racimos que se tocan** en un solo nodo |
| **el cruce** | `sistema_gates_go_kill` repite **hacia fuera** con `gestion_de_portafolio_gates_go_kill`, del racimo del portafolio, **y hacia dentro** con `estructura_gates`, del suyo |
| **QUE DECIDE** | **cuantos nodos quiere el catalogo** para el sistema de puertas, y **en que orden se tocan los dos racimos** |
| **orden recomendado** | **primero la familia de las puertas**, y con el superviviente en la mano el cruce con el portafolio. Al reves, el portafolio decide sobre un nodo que despues se funde |

### MESA 2: EL RACIMO DEL PIVOTE

| | |
|---|---|
| **nomina medida** | **siete** por lectura contra **cinco** censados. 21 pares posibles, 10 en cola, **5 leidos**, 11 que nunca entraron, **dos aristas internas** |
| **el saldo** | dentro de Blank ya esta resuelto: la misma puerta **repite** (268 A), puertas distintas son **sanas** (594 D, 598 D). **El cruce entre libros no**: 771 y 843, los dos **B** |
| **QUE DECIDE** | si el catalogo quiere **un nodo por LIBRO** o **un nodo por PUERTA** del proceso |
| **EL CRITERIO, con evidencia** | **si cada libro ya se repite a si mismo, el criterio de reparto no puede ser el libro.** Medido: dentro de Blank la misma puerta repite (**268 A**), dentro de Ries la misma decision repite (**860 A**), y el **acto** de pivotar repite entre los dos libros (**857 A**). **Los unicos pares sin resolver son los cruzados** (771, 843). **La evidencia empuja hacia UN NODO POR PUERTA** |
| **AMPLIADA el 13 ago 2026** | la zona tiene **DOS familias**, la de la **DECISION** (siete nodos) y la del **ACTO de pivotar** (`pivote_estrategico`, `pivote_startup`, `catalogo_pivotes`), y **SEIS dudosos** contados del archivo: 591, 668, 737, 753, 771 y 843. **`pivote_startup` solo carga cuatro de los seis** |
| **recomendacion del auditor, registrada** | **el catalogo se organiza por lo que el lector HACE, no por la biblioteca**: **un nodo por PUERTA** como opcion por defecto, y **nodo por libro solo donde los libros discrepen de verdad**, y entonces se llama **FRONTERA DECLARADA** y se escribe como tal, no como dos nodos que se ignoran |

### MESA 3: `customer_development_modelo` Y SU ZONA

| | |
|---|---|
| **el nodo** | **siete pares leidos**: **A** en 635 y 849, **D** en 377 y 854, **B en 683, 707 y 806** |
| **motivo** | **tres dudosos sobre un solo nodo, mas que ningun otro del cribado.** Y repite con **dos** nodos de descubrimiento distintos |
| **la forma del problema** | demasiados nodos contando **el mismo proceso desde alturas distintas**: el modelo entero, la etapa, la fase y el gesto |
| **QUE DECIDE** | **a que altura vive cada nodo** de customer development, y **cual de las alturas se queda con el material comun** |
| **por que no se decide pareja por pareja** | porque cada par enfrenta **dos alturas** y la respuesta correcta depende de las **cuatro** |

> **LO QUE LAS TRES COMPARTEN, y es el motivo de abrir el registro**: ninguna es
> una duda de clase. **Las tres son dudas de ARQUITECTURA**, y por eso el cribado
> las acumula en B en vez de resolverlas. **Cada B de estas zonas es una mesa que
> no se ha sentado.**

---

## 35. EL TRAMO 855 a 860: una familia cierra y la mesa del pivote se agranda

**Seis pares leidos, los seis del nucleo.** Acumulado **860 de 3.388**, global
**30,8%** de A y **nucleo 37,4%**. **El tramo dio 50%.** **Faltan 40 para el
checkpoint de los 900.**

### 35.1 LA FAMILIA DE SPIN QUEDA LEIDA ENTERA

**Puesto 856.** Con este par, **los seis pares posibles de la familia estan
leidos**, y los seis estaban en la cola.

| | |
|---|---:|
| miembros | **4**: `metodologia_spin_selling`, `framework_spin_selling`, `modelo_spin`, `modelo_spin_preguntas` |
| pares posibles | **6** |
| **leidos** | **6**, todos |
| saldo | **4 A** (248, 305, 401, 856) y **2 D** (625, 764) |

> **MEZCLADA COMPLETA, y por eso NO pide mesa: pide redactor.** La familia esta
> cerrada, se sabe exactamente que repite y que no, y **no hay ninguna pregunta de
> arquitectura pendiente.** Es el contraste util con las tres mesas de la seccion
> 34.
>
> **Y trae un detalle del grafo**: el par que cierra la familia es **Weinberg
> resumiendo a Rackham**, y **no hay arista entre ellos.** El catalogo tiene la
> cita y el grafo no la conoce.

### 35.2 LA MESA DEL PIVOTE ERA MAS GRANDE DE LO MEDIDO

**La seccion 34 la abrio con SIETE nodos, los de la DECISION.** Este tramo
encuentra que **hay una segunda familia en la misma zona: la del ACTO de
pivotar.**

| familia | de que trata | ejemplo |
|---|---|---|
| **la DECISION** | si pivotar o no | `pivote_o_proceder`, `decision_pivote_perseverar` |
| **el ACTO** | como se pivota | `pivote_estrategico`, `pivote_startup`, `catalogo_pivotes` |

**Y la zona entera acumula SEIS dudosos**, contados del archivo: **591, 668, 737,
753, 771 y 843.**

> **`pivote_startup` solo carga CUATRO de esos seis.** Es, con
> `customer_development_modelo`, uno de los dos nodos que mas dudas produce en
> todo el cribado.
>
> **La mesa 2 queda ampliada**: no decide sobre siete nodos, decide sobre **una
> zona con dos familias y seis dudosos.**

**PERO EL TRAMO TAMBIEN LE DA A ESA MESA SU DATO MAS UTIL** (puesto **860**):

> **Dentro de Blank, la misma puerta ya repetia** (268 A). **Ahora, dentro de
> Ries, la misma decision tambien repite** (860 A). **Y el acto de pivotar repite
> entre los dos libros** (857 A).
>
> **La duplicacion esta DENTRO de cada libro.** Los unicos pares que siguen sin
> resolverse son **los cruzados** (771 y 843). **Eso empuja hacia la
> recomendacion del auditor**: si cada libro ya se repite a si mismo, el criterio
> de reparto no puede ser el libro. **Un nodo por PUERTA.**

### 35.3 LA CUARTA ARISTA QUE FALTA DEL MISMO TIPO, y la mesa 3 se confirma

**Puesto 855.** `customer_development_process` nombra la validacion con clientes
en su etapa 2 y **no enlaza** a `customer_validation`, que la ejecuta.

> **Es la cuarta del mismo tipo en cuatro tramos** (841, 846, 854, 855): **madres
> que nombran un paso y no lo enlazan.**
>
> **Y aqui se ve por que la mesa 3 no es opcional**: `customer_validation` lleva
> **DOS madres distintas leidas contra el**, esta y `customer_development_modelo`
> (854), **las dos en D**, y **las dos madres entre si dieron D** (377). **Tres
> nodos contando el mismo proceso a tres alturas, ninguno enlazado con el hijo, y
> los tres pares sanos.** El problema no es que repitan: **es que nadie sabe cual
> preside.**

### 35.4 Lo demas del tramo

> **1. Dos etapas consecutivas de la misma llamada de Rackham SIN ARISTA entre
> ellas** (puesto **858**): los Preliminares y la Investigacion. Salen **D**, se
> tocan en una sola orden, no hablar del producto antes de tiempo, **y el grafo no
> sabe que van seguidas.** No es duplicacion: **es una serie sin cablear.**
>
> **2. El sub-puro numero 4, la etapa de investigacion en la venta, tiene su
> lectura pendiente a la vuelta**: el puesto **862**, que cae en el tramo
> siguiente. **Con el y con el par que nunca entro a la cola, la familia se
> cierra.**
>
> **3. La contabilidad de caja contra el devengo sale sana** (puesto **859**):
> una es la **decision de migrar** y la otra es la **revision de periodo**. Lo mas
> valioso del segundo, **distinguir la utilidad reportada del flujo de caja real
> disponible**, no esta en el primero.

---

## 36. CHECKPOINT DE LOS 900, y el tramo mas sano del cribado entero

**Cuarenta pares leidos de una vez, del 861 al 900, los cuarenta del nucleo.**

### 36.1 EL MARCADOR COMPLETO, recomputado del archivo

| | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **GLOBAL** | **900** | **272** | 86 | 5 | 537 | **30,2%** |
| **NUCLEO** | **745** | **271** | 84 | 5 | 385 | **36,4%** |
| compras | 155 | 1 | 2 | 0 | 152 | 0,6% |

**La cola entera son 3.388 pares. Van 900: el 26,6%.**

### 36.2 LA CURVA POR CENTENAS, que es el dato del checkpoint

| centena | tasa de A global | nucleo | tasa de A del nucleo |
|---|---:|---:|---:|
| 1 a 100 | 1,0% | 0 | sin nucleo |
| 101 a 200 | 24,0% | 45 | **53,3%** |
| 201 a 300 | 54,0% | 100 | **54,0%** |
| 301 a 400 | 51,0% | 100 | **51,0%** |
| 401 a 500 | 39,0% | 100 | **39,0%** |
| 501 a 600 | 33,0% | 100 | **33,0%** |
| 601 a 700 | 21,0% | 100 | **21,0%** |
| 701 a 800 | 24,0% | 100 | **24,0%** |
| **801 a 900** | **25,0%** | 100 | **25,0%** |

> **LA CURVA BAJA Y SE APLANA.** De 54% en la segunda y tercera centena a **una
> meseta del 21 al 25% en las tres ultimas.** No es que el catalogo mejore: es que
> **la cola esta ordenada por similitud y los pares mas parecidos ya se leyeron.**
>
> **Lo util para planificar**: si la meseta se sostiene, **las 2.488 lecturas que
> faltan aportarian del orden de 550 a 620 duplicados mas**, no 750. **Pero eso es
> una proyeccion, no una medicion**, y se revisa en cada checkpoint.

**Y el tramo 861 a 900 es el mas sano de todo el cribado**: **33 D, 7 A, 17,5%**.
**Ninguna centena habia bajado de 21%.**

### 36.3 LAS DOS CONDICIONES VIVAS, resueltas

#### 862: el sub-puro de la ETAPA DE INVESTIGACION avanza y queda a UNA lectura

**Sale A**, y con eso el sub-puro numero 4 del banco 9.5 pasa de **4 de 6** a
**5 de 6 pares leidos, los cinco en A.**

> **Le queda UNA sola lectura, y no va a llegar por la cola**: el par
> `etapa_de_investigacion` contra `investigacion_como_habilidad_clave` **nunca
> entro**. **Una lectura dirigida lo cierra**, y seria el primer puro de cuatro
> miembros del archivo.

#### 863: el racimo de la estrategia de innovacion sale D, y arrastra DOS correcciones

**Sale D**, y hay que decir las dos cosas que eso rompe.

> **CORRECCION 1, y es mia.** Mi nota de la tanda R19 llamaba a esto *un racimo
> censado de TRES* y anunciaba el 863 como *posible puro de tres*. **Estaba mal**:
> la **seccion 4 de este mismo informe** ya habia medido la familia en **SEIS
> miembros y quince pares posibles**. Yo mire `RACIMOS_MIEMBROS.jsonl` (que dice
> tres) y no la medicion propia del informe (que dice seis). **Es exactamente el
> modo de fallo que la disciplina del dictado nombra, cometido por mi.**
>
> **CORRECCION 2, y es la que cuesta.** La familia tenia **SEIS de SEIS en A** y
> era, en palabras de la seccion 4, *la apuesta mas cargada del inventario*. **Este
> es su primer sano.** Deja de ser sub-puro y pasa a **MEZCLADA**, con nueve
> lecturas todavia pendientes.

**Y traigo sin resolver un choque interno que este par destapa:**

> **El puesto 530 es LA MISMA RELACION contra el otro gemelo de la madre, y esta
> en A.** Su razon dice que los dos nodos mandan *pesar los mercados contra las
> competencias propias*, **y ese paso no esta en los seis de
> `estrategia_de_innovacion_de_producto`**: solo esta en
> `estrategia_de_innovacion_y_tecnologia`.
>
> **Si el 863 es D por la vara, el 530 tiene el mismo esqueleto.** **No lo muevo:
> pido relectura conjunta**, igual que se hizo con el 395.

### 36.4 DOS SUB-PUROS SE ROMPEN EN EL MISMO TRAMO

| # | racimo | estaba | queda |
|---:|---|---|---|
| **3** | el sales roadmap | SUB-PURO, 4 de 4 en A | **MEZCLADO** (872 sale D) |
| la familia de innovacion | seis miembros | SUB-PURO, 6 de 6 en A | **MEZCLADA** (863 sale D) |

> **Los dos se rompen por el mismo mecanismo y conviene nombrarlo**: una familia
> con muchos pares **sin leer** puede tener todos sus pares leidos en A **y no ser
> pura**. **Cuantos mas pares le falten, mas facil es que el siguiente sea el
> sano.** El sub-puro es una promesa, no un resultado, y estos dos lo demuestran.

### 36.5 LAS ESCALERAS QUE SI SUBEN: cuatro ejemplares en un solo tramo

**El banco 9.12 nombro LA ESCALERA QUE NO SUBE con la junta asesora.** Este tramo
trae **cuatro ejemplares del lado bueno**, y los cuatro pasan el test:

| puesto | los dos peldanos | que exige el segundo que el primero no |
|---:|---|---|
| **876** | etapa 1 Scoping contra etapa 2 Business Case de Cooper | investigacion de mercado detallada, voz del cliente profunda, NPV con sensibilidad |
| **888** | la tesis de investigar contra las preguntas de Implicacion | mapear consecuencias financieras y operativas de cada problema |
| **892** | fase Assess contra fase Admit de Coleman | la celebracion inmediata y el rescate del silencio posventa |
| **895** | fase Mobilizar contra fase Entendimiento de Osterwalder | mapa de empatia, expertos del dominio, intentos previos fallidos |

> **Los cuatro salen D y ninguno pide arreglo.** Sirven para lo contrario de lo
> habitual: **para saber cuando NO hay problema.** Y dejan una lectura de fondo:
> **en las tres series (Cooper, Coleman, Osterwalder) las FASES estan sanas; lo
> que repite son las SEGUNDAS CASAS de cada fase.**

### 36.6 Lo demas del tramo

> **1. `customer_validation` es el nodo mas mirado del archivo y NO repite con
> casi nadie**: **catorce pares leidos, once D y tres A.** En este tramo entro a
> **cinco** y los cinco salieron sanos. **Eso le da a la MESA 3 su dato mas
> importante**: el problema de la zona del customer development **no es este
> nodo**, es que **tres madres distintas lo nombran y ninguna lo enlaza.**
>
> **2. PRIMER USO DEL BARRIDO DE LAS A** (puesto **878**, banco 9.15):
> `tecnica_anclaje_negociacion` aparece con un A contra un miembro del sub-puro de
> inversores, entra como **candidato** y **la lectura lo deja fuera** con su
> motivo, su objeto es como negociar terminos y no como generar competencia. **La
> regla funciono exactamente como se escribio: el archivo levanta, la lectura
> decide.**
>
> **3. UNA FRONTERA QUE HAY QUE DECLARAR, y es dentro del MISMO libro** (puesto
> **877**): para el mismo caso, cofundar con amigos o familia,
> `cofundar_con_amigos_familia_riesgos` manda **autoridad clara aunque incomode** y
> `relacion_previa_y_estructura_roles` manda **estructura colegiada e igualitaria**.
> **Los dos son de *The Founder's Dilemmas*.** No es duplicacion: es una **FRONTERA
> DECLARADA** en el sentido que el auditor dio al termino en la mesa del pivote, y
> hay que escribirla como tal en vez de dejar que el lector encuentre los dos
> consejos y elija al azar.
>
> **4. `realizar_pruebas_pasa_no_pasa` queda confirmado como instrumento y no
> como copia**: **once pares leidos, diez D.** Tres de ellos en esta tanda, contra
> tres nodos de etapa distintos, y los tres sanos.

---

## 37. EL TRAMO 901 a 928: la vara resuelve siete de veintiocho, y un choque de criterios

**Veintiocho pares leidos, los veintiocho del nucleo.** Acumulado **928 de
3.388**, global **29,7%** de A y **nucleo 35,6%**. **El tramo dio 17,9%** (23 D, 5
A), sosteniendo la meseta baja del checkpoint anterior. **El proximo checkpoint es
el de los 1.000.**

### 37.1 EL CHOQUE DE CRITERIOS DEL 915, y lo traigo antes de que se repita

**Es la primera vez que los DOS tests del banco 9.9 se contradicen.**

| test | que dice del puesto 915 |
|---|---|
| **la POSICION del solape** (9.9 original) | el solape son las **pruebas A/B**, y `optimizacion_embudo_get_customers` las tiene **en su paso 3 (Blank) y otra vez en su paso 7 (Weinberg)**. **Toca la juntura: bloquea** |
| **la DEPENDENCIA** (regla adoptada el 13 ago) | el veredicto **no depende** de cual copia sobreviva: la clase se decide por **la fase del embudo**, Get contra Grow, no por el A/B. **Invariante: se emite** |

> **Aplique el de DEPENDENCIA**, porque es el criterio que el auditor adopto como
> definicion (*se congela el par cuyo veredicto DEPENDE de que quede tras la
> cirugia*) **y el de posicion es su proxy.** El par queda **D y en cola sin
> congelar.**
>
> **LO QUE TRAIGO**: hasta hoy los dos tests decian siempre lo mismo y por eso
> convivian sin jerarquia. **Ahora hay un caso donde no**, y conviene dejar escrito
> cual manda antes de que aparezca el segundo. **Mi lectura es que manda la
> dependencia y la posicion queda como atajo**, pero eso lo decide el auditor.

### 37.2 LA VARA RESUELVE SIETE PARES DE VEINTIOCHO, y todos con la misma forma

**Siete pares del tramo se resolvieron por LA LINEA O EL PROCEDIMIENTO**, y los
siete tienen la misma anatomia: **una madre que nombra un paso en una linea y un
hijo que trae el procedimiento entero.**

| puesto | la madre y su linea | el hijo y su procedimiento |
|---:|---|---|
| **901** | los tres capitales, *listar el capital humano* | educacion formal contra experiencia tacita, modelos mentales, y **hacia afuera contra hacia adentro** |
| **902** | los tres circulos, *evaluar que falta en el equipo* | las tres brechas y el aviso de **no fichar redundantes** |
| **903** | las cuatro etapas de Wallas, *define e investiga* | barrer la habitacion, hipotesis que se contradicen, y **aceptar que la etapa se sienta infructuosa** |
| **904** | la cultura financiera, *sesiones regulares* | tres sesiones de 30 a 60 minutos, mensuales, reunion semanal de numeros, mapas de dinero |
| **909** | la estrategia de ventas, *cuantos deben decir si* | el organigrama, el earlyvangelist, el comprador economico, y **repetir para hallar patrones** |
| **910** | la evaluacion de industria, *investigacion VoC cara a cara* | el porque detras de cada peticion, las necesidades futuras, y los hallazgos inesperados |
| **912** | el customer development, *ajusta el modelo* | la reunion, el mapa del cliente, el recorte de funciones y el plan a 18 meses |

> **Siete de veintiocho, y en los siete falta la arista.** No es coincidencia:
> **es la forma dominante del catalogo en esta zona.** Una madre enumera y un hijo
> ejecuta, **y el grafo no los une**.
>
> **Lo que esto le dice al plan**: la clase de arreglo mas barata del banco 9.6
> **no es un caso suelto, es un patron con volumen.** Vale la pena un barrido
> dirigido que busque exactamente esta figura en vez de esperar a que la cola la
> traiga par por par.

### 37.3 LA FRONTERA DEL CIERRE SE CRUZA, y aguanta

**Puesto 917.** `compromiso_linea_tiempo_cliente` (Weinberg) contra
`obtencion_compromiso` (Rackham): **un par que cruza la frontera del racimo del
cierre**, la que separa *pide el si con fecha* de *no pidas el cierre, busca el
avance*.

> **Sale D, y no por poco: ni un paso se solapa.** Uno manda **solicitar un
> compromiso de respuesta si o no al finalizar el plazo y descartar a quien no
> confirme**; el otro manda **medir el exito por avances y no por pedidos** y dice
> que presionar por el si es la tecnica equivocada en venta compleja.
>
> **La frontera no solo aguanta: se ve mejor desde aqui.** Los dos lados **no se
> duplican, se contradicen en el metodo**, y por eso el catalogo tiene que
> conservar los dos **con su condicion escrita**. Es el mismo tratamiento que la
> FRONTERA INTRA-LIBRO del puesto 877, ahora entre libros.

### 37.4 Lo demas del tramo

> **1. `customer_development_modelo` llega a NUEVE pares leidos** (912 y 922, los
> dos D). **Cuatro sanos seguidos.** La mesa 3 acumula evidencia de que su
> problema es de **alturas** y no de contenido.
>
> **2. DOS PARES DE FORMULARIOS HERMANOS Y BIEN CABLEADOS** (puestos **921** y
> **927**): el cierre de contrato dentro del cierre de proyecto, y el registro de
> cambios junto al de decisiones. **Misma forma, objetos distintos, arista en los
> dos sentidos.** Son el contraejemplo limpio de todo lo anterior: **cuando el
> catalogo hace bien las cosas, se ve.**
>
> **3. DOS PRIMAS DE EQUITY QUE NO SE PUEDEN FUNDIR** (puesto **913**): la **prima
> de idea**, de 10 a 15 puntos para quien origino el concepto, y la **prima de
> rol**, de 14 a 20 para el director general y de 5 a 8 para el de tecnologia.
> **Rangos distintos y motivos distintos.** Fundirlas perderia una de las dos.
>
> **4. Y una pareja que el redactor deberia ENLAZAR en vez de fundir** (puesto
> **906**): decidir el ritmo de crecimiento **contando el efectivo** contra
> decidirlo **contando a los competidores**. Ninguno mira lo que mira el otro.

---

## 38. EL BARRIDO DEL PASO CONTRA EL NODO: el tercer eje

**Instrumento nuevo, aprobado el 13 ago 2026: `scripts/paso_contra_nodo.py`.
Estrictamente de solo lectura.** Su salida es `docs/PASO_NODO_CANDIDATOS.jsonl`.

### 38.1 POR QUE HACIA FALTA

**Los dos instrumentos existentes miden lo mismo desde dos sitios, y ninguno mira
este eje:**

| instrumento | que compara |
|---|---|
| `intra_dominio.py` | **nodo contra nodo** del mismo dominio |
| `costuras_internas.py` | **paso contra paso DENTRO del mismo nodo** |
| **`paso_contra_nodo.py`** | **un PASO de la madre contra un NODO ENTERO que lo desarrolla** |

> **La figura la encontro el cribado a mano, una y otra vez.** En el tramo 901 a
> 928 fueron **siete de veintiocho pares**: una madre enumera un paso en una linea
> y otro nodo trae el procedimiento entero de esa linea, **sin arista entre
> ellos**.
>
> **El instrumento no adjudica cual de los dos destinos toca.** La lista alimenta
> las dos clases que el plan ya tiene: **ARISTA QUE FALTA** (banco 9.6) cuando la
> jerarquia es sana, y **PODA** cuando la madre re-desarrolla lo que el hijo ya
> cuenta.

### 38.2 EL METODO, con sus umbrales declarados

**DOS SENALES, y tienen que disparar LAS DOS:**

| senal | que mide | umbral |
|---|---|---:|
| **TITULO** | `token_set_ratio` del paso contra el **titulo** del hijo candidato. Se usa `set` y no `sort` porque los largos son muy distintos: un titulo de cinco palabras dentro de un paso de veinte | **72** |
| **CONTENCION** | que proporcion de las palabras de contenido del paso vive dentro de la **identidad** del hijo (titulo mas resumen mas entregable) | **0,45** |

**Y un piso**: pasos de menos de **cuatro** palabras de contenido no se miden.
*Iterar rapido* se parece a demasiadas cosas.

> **POR QUE LAS DOS Y NO CUALQUIERA.** Es la leccion del umbral 0,80 del intra:
> **dentro de un dominio la vecindad tematica es la norma, no la senal.**
> Cualquiera de las dos sola llena la lista de vecinos legitimos. **La conjuncion
> pide que el paso NOMBRE al hijo y ademas que su vocabulario VIVA dentro de el.**

**Excluye**: deprecados de los dos lados, el propio nodo, y los pares de distinto
dominio. **El nucleo cuenta como un dominio mas**, igual que en el intra.

### 38.3 EL VOLUMEN

**3.521 nodos vivos mirados. 742 candidatos, sobre 507 madres distintas.**

| dominio | nodos | candidatos | con arista | **sin arista** |
|---|---:|---:|---:|---:|
| **quality** | 792 | **323** | 27 | **296** |
| **core** | 1.618 | **298** | 69 | **229** |
| environmental | 289 | 32 | 0 | 32 |
| franquicias | 195 | 29 | 2 | 27 |
| health_safety | 283 | 27 | 11 | 16 |
| exportacion | 141 | 23 | 6 | 17 |
| entrega | 47 | 4 | 0 | 4 |
| seguridad_digital | 55 | 4 | 2 | 2 |
| risk_management | 55 | 1 | 0 | 1 |
| compras | 46 | 1 | 1 | 0 |
| **TOTAL** | **3.521** | **742** | **118** | **624** |

> **SEISCIENTOS VEINTICUATRO candidatos sin arista.** Si aunque sea la mitad
> resultara jerarquia sana, **son mas de trescientas aristas que faltan**, cada
> una un solo enlace. **Es, de lejos, la bolsa de trabajo barato mas grande que
> ningun instrumento haya destapado.**
>
> **Y la sorpresa es `quality`**: 323 candidatos con **la mitad de nodos** que el
> nucleo. **Es el dominio donde esta figura mas abunda**, y hasta hoy nadie lo
> habia mirado por este eje.

### 38.4 LOS DIEZ CANDIDATOS MAS FUERTES

| puntaje | madre y paso | hijo candidato | arista |
|---:|---|---|:---:|
| **1,000** | `verificar_clientes_y_canales`, paso 2 de 6: *crear un dia en la vida del cliente antes y despues del producto* | `dia_en_la_vida_del_cliente` (5 pasos) | **NO** |
| **1,000** | `planificacion_estrategica_despliegue`, paso 1 de 7 | `definir_mision_organizacional` (4 pasos) | **NO** |
| **1,000** | `plan_cambio_climatico`, paso 3 de 5 | `implementar_estrategias_reduccion_emisiones` (5 pasos) | **NO** |
| 0,962 | `estrategias_de_crecimiento_empresarial`, paso 5 de 6 | `due_diligence_adquisiciones` (6 pasos) | SI |
| 0,943 | `seguimiento_cumplimiento_cadena_suministro`, paso 1 de 4 | `identificacion_proveedores_criticos` (4 pasos) | **NO** |
| 0,929 | `genchi_gembutsu_salir_del_edificio`, paso 1 de 5: *identificar las preguntas de fe mas criticas* | `leap_of_faith_questions` (4 pasos) | SI |
| 0,921 | `lectura_balance_general`, paso 3 de 6 | `tipos_de_pasivos` (4 pasos) | SI |
| 0,884 | `rapid_prototyping`, paso 1 de 5 | `determine_what_to_prototype` (4 pasos) | SI |
| 0,875 | `tasa_de_retorno_requerida`, paso 3 de 4 | `costo_de_capital` (4 pasos) | SI |
| 0,857 | `tasa_interna_retorno_irr`, paso 3 de 4 | `tasa_de_retorno_requerida` (4 pasos) | SI |

> **El primero es la figura en estado puro y ya estaba a la vista del cribado**:
> el puesto **926** leyo `verificar_clientes_y_canales` y su paso 2 dice
> literalmente *crear un dia en la vida del cliente*. **Existe un nodo que se
> llama asi y hace eso, y no hay arista.**
>
> **Los que SI tienen arista tambien sirven, y para lo contrario**: son la
> jerarquia sana ya cableada, **el patron de referencia contra el que se lee todo
> lo demas.**

### 38.5 LO QUE ESTE INSTRUMENTO NO HACE

> **No adjudica, no ordena la cola, y no toca un nodo.** Cada fila es **una cita
> para leer**, igual que la del intra. **Y no reemplaza a los otros dos ejes: los
> completa.** Un nodo puede estar sano en los tres ejes y aun asi tener mal el
> cableado, que es justamente lo que este barrido destapa.

---

## 39. EL TRAMO 929 a 942: el barrido nuevo encuentra su primer caso de manual

**Catorce pares leidos, los catorce del nucleo.** Acumulado **942 de 3.388**,
global **29,5%** de A y **nucleo 35,2%**. **El tramo dio 14,3%.** **Faltan 58 para
el checkpoint de los 1.000.**

### 39.1 EL CASO DE MANUAL DEL TERCER EJE, y salio en el mismo dia

**Puesto 932.** `cumplimiento_magnuson_moss` es la madre de la familia de
garantias, y **nombra a CUATRO nodos hermanos en dos de sus cuatro pasos:**

| lo que dice la madre | el nodo que lo desarrolla |
|---|---|
| *titulo claro* | el nodo del titulo de la garantia |
| *terminos divulgados con claridad* | el nodo de la divulgacion |
| *disponibilidad antes de la venta* | **`regla_disponibilidad_previa_venta`**, leido en el 929 |
| *que no obligue a comprarte algo mas* | **`prohibicion_tie_in_sales`**, leido en el 929 |

> **Y no enlaza con ninguno.** Cuatro hijos nombrados en dos lineas, cero
> aristas. **Es exactamente lo que el barrido de la seccion 38 sale a buscar**, y
> aparecio a mano en el mismo tramo en que el instrumento se escribio.
>
> **Lo util es que confirma el diseno del barrido por otra via**: la figura no es
> una impresion del cribador, **es una forma que el catalogo repite**, y ahora hay
> un instrumento que la cuenta en vez de esperarla.

### 39.2 LA SEGUNDA CASA VUELVE A APARECER, y en la misma cadena

**Puesto 933.** `fase_mobilizacion_equipo_multifuncional` desarrolla la **fase 1**
de `proceso_diseno_modelo_negocio_5_fases`. **Pero esa fase ya tenia casa**:
`fase_mobilizar_modelo_negocio`, leido en los puestos 865 y 895.

| fase de Osterwalder | casas que tiene |
|---|---|
| **1, Movilizar** | **DOS**: `fase_mobilizar_modelo_negocio` y `fase_mobilizacion_equipo_multifuncional` |
| **3, Disenar** | **DOS**: `fase_diseno_prototipado_modelos` y `proceso_ideacion_modelo_negocio` (puestos 395, 507, 641) |

> **Es la misma figura que rompio el 395**, y confirma lo que la seccion 36 dejo
> escrito: **en las series de fases, las FASES estan sanas y lo que sobra son las
> segundas casas.** Dos de las cinco fases de Osterwalder ya tienen dos casas cada
> una.

### 39.3 CUATRO PARES DE ARTEFACTOS HERMANOS, y solo dos cableados

**El tramo trae cuatro pares de la misma forma: un artefacto que define y otro que
obedece.** Y el saldo del cableado es la mitad:

| puesto | el par | arista |
|---:|---|:---:|
| **937** | el cronograma y su diagrama de red | **SI** |
| **939** | el plan de requisitos y su registro | **SI** |
| **934** | el informe del contratista y el del proyecto | **NO**, y el texto lo nombra |
| **931** | las disposiciones vinculantes y el acuerdo de exclusividad | **NO** |

> **Los dos cableados son de la misma coleccion de formularios que los dos que no
> lo estan.** No es que una fuente cablee bien y otra mal: **es que el cableado se
> hizo a mano y por eso es irregular.** Con los puestos 881 y 927, esta coleccion
> lleva **seis pares hermanos leidos, todos sanos, y cuatro con arista.**

### 39.4 Lo demas del tramo

> **1. El frente del Stage-Gate llega a ONCE nodos leidos** (puesto **942**, la
> puerta 5 contra la etapa 5, sano). **La mesa 1 crece cada tramo y sigue sin
> convocarse.**
>
> **2. El nucleo tiene DOS nodos de encaje producto-mercado** (puesto **930**):
> este `product_market_fit` y el `verificar_product_market_fit` del puesto 922.
> **Su par pide contador**, y ninguno de los dos se ha leido contra el otro.
>
> **3. Los dos principios de Mollick quedan separados** (puesto **940**): probarlo
> todo (principio 1) contra asumir que la IA mejora (principio 4). **El paso 3 del
> primero es una linea y el segundo es su procedimiento entero.** Y con el puesto
> 456 queda dicho: **la pareja del principio 1 repite entre si, pero es sana
> contra los otros principios.**
>
> **4. `realizar_pruebas_pasa_no_pasa` llega a DOCE pares leidos y ONCE sanos**
> (puesto **938**). **Ningun otro nodo del cribado ha sostenido tantas lecturas
> sin duplicarse.** Es un instrumento propio, y a estas alturas eso ya no es una
> lectura: es una medicion.

---

## 40. LA MUESTRA PINEADA DEL BARRIDO PASO-CONTRA-NODO

**Encargo aprobado el 13 ago 2026. El pin se escribio ANTES de correr el sorteo** y
se transcribe aqui completo para que el orden se pueda auditar.

### 40.1 EL PIN, tal como se escribio

> **UNIVERSO**: las filas de `docs/PASO_NODO_CANDIDATOS.jsonl` con `arista=false`.
> **Son 624.**
>
> **ESTRATOS**: `quality` (296), `core` (229), y una **franja** con todos los
> demas dominios juntos (99).
>
> **TAMANO**: **24**. Diez de quality, ocho de core, seis de la franja.
>
> **POR QUE NO ES PROPORCIONAL**: la franja **se sobre-muestrea a proposito**
> (seis de veinticuatro, 25%, cuando le tocaria 16%) para que los dominios chicos
> tengan senal propia. **Se declara aqui para que la proyeccion se lea con ese
> sesgo puesto.**
>
> **ORDEN DETERMINISTA**: cada estrato se ordena por la terna (madre, paso, hijo)
> antes de sortear. **SEMILLA: 20260813.** Procedimiento:
> `random.Random(20260813).sample(lista_ordenada, n)`, estrato por estrato, en el
> orden quality, core, franja.
>
> **CLASIFICACION**: cada candidato se lee con **LA VARA** del banco 9.6.1 y cae
> en una de tres: **JERARQUIA SANA** (el hijo trae procedimiento; falta la
> arista), **MADRE QUE REPITE** (toca poda), **FALSO POSITIVO** (vecino
> legitimo).
>
> **LA SALIDA ES PROYECCION, NO MEDICION. No se adjudica ningun arreglo.**

### 40.2 EL SALDO

| clase | quality (10) | core (8) | franja (6) | **total (24)** |
|---|---:|---:|---:|---:|
| **JERARQUIA SANA** | **7** | **7** | **5** | **19** |
| **MADRE QUE REPITE** | 0 | 0 | 0 | **0** |
| **FALSO POSITIVO** | 3 | 1 | 1 | **5** |
| tasa de acierto | 70% | 87,5% | 83% | **79,2%** |

> **CERO PODAS en veinticuatro.** Es el hallazgo que no esperaba: **cuando esta
> figura dispara, la madre SIEMPRE dice su paso en una linea.** No aparecio ni una
> madre que re-desarrollara lo que el hijo ya cuenta.
>
> **Si se sostiene, simplifica el plan entero**: esta bolsa **no es una mezcla de
> dos clases de arreglo. Es una sola**, y es la barata.

### 40.3 LOS CINCO FALSOS POSITIVOS, y por que fallo el instrumento

| # | el candidato | por que no es |
|---:|---|---|
| 3 | `seleccion_plan_muestreo_ansi_z14` p3 contra `planes_de_muestreo_de_aceptacion` | el paso manda **LEER la tabla** del estandar; el hijo ensena a **DISENAR** un plan por economia. **Actos distintos sobre el mismo objeto** |
| 4 | `pre_control_estadistico` p1 contra `limites_de_especificacion_vs_limites_de_control` | **estan en TENSION, no en jerarquia**: el paso manda centrar el proceso **entre los limites de especificacion** y el hijo advierte de que **nunca** se ajuste el proceso por la especificacion. **Frontera, no madre e hijo** |
| 10 | `sistema_pull_push` p5 contra `reduccion_tiempo_ciclo` | el paso manda **MONITOREAR** la reduccion; el hijo ensena a **LOGRARLA**. El instrumento engancho el sustantivo compartido |
| 13 | `medir_lo_que_importa_no_solo_lo_facil` p1 contra `metricas_calidad` | el paso manda **listar** las metricas que ya usas; el hijo **define** metricas de calidad con su formato. Inventario contra definicion |
| 24 | `compra_equipos_verdes` p1 contra `certificacion_leed_energy_star` | el paso pide el sello **en cada equipo que compras**; el hijo certifica **el local o el proyecto**. Mismo sello, objeto distinto |

> **El modo de fallo tiene nombre y es uno solo: el VERBO.** En cuatro de los
> cinco, el paso y el hijo comparten el sustantivo y **cambian el verbo**: leer
> contra disenar, monitorear contra lograr, listar contra definir, comprar contra
> certificar. **El instrumento mide vocabulario y no accion**, y ahi es donde
> falla.
>
> **Y el quinto, el numero 4, no es un fallo del instrumento sino un HALLAZGO que
> no cabia en las tres clases**: dos nodos de `quality` que dan instrucciones
> opuestas sobre el mismo gesto. **Es una FRONTERA INTRA-LIBRO como la del puesto
> 877**, encontrada por el eje nuevo. Queda anotada.

### 40.4 LA PROYECCION, declarada como proyeccion

**Aplicando la tasa de cada estrato a su tamano** (que es lo que corrige el
sobre-muestreo de la franja):

| estrato | sin arista | tasa medida | proyeccion de jerarquias sanas |
|---|---:|---:|---:|
| quality | 296 | 70% | **207** |
| core | 229 | 87,5% | **200** |
| franja | 99 | 83% | **82** |
| **TOTAL** | **624** | **79,2%** | **489** |

**EL INTERVALO, y es ancho porque veinticuatro son veinticuatro.** Sobre 19 de 24,
el intervalo de Wilson al 95% va de **60% a 94%**.

> **Traducido a la bolsa entera: entre 376 y 586 aristas que faltan.** El punto
> central esta cerca de **490**.
>
> **NO ES UNA MEDICION.** Es una proyeccion de una muestra de veinticuatro sobre
> seiscientos veinticuatro, con un sesgo de estrato declarado y un intervalo de
> mas de doscientos casos de ancho. **Lo unico que la muestra prueba con firmeza
> es el signo: la mayoria de esta bolsa es jerarquia sana sin cablear**, y **la
> clase de poda, que era la mitad esperada del plan, no aparecio ni una vez.**

### 40.5 DOS CANDIDATOS QUE EL CRIBADO YA CONOCIA

**Dos de los diecinueve caen sobre nodos que el cribado lleva tramos mirando:**

| candidato | lo que el cribado ya sabia |
|---|---|
| `customer_validation` paso 1 contra `mvp_alta_fidelidad` | `customer_validation` es **el nodo mas mirado del archivo**, catorce pares leidos y once sanos. **Y le falta el enlace con el nodo que ejecuta su primer paso** |
| `customer_development_modelo` paso 1 contra `customer_segments_hypothesis` | es el nodo de la **MESA 3**, nueve pares leidos y tres dudosos. **Su problema de alturas tiene aqui una de sus causas: no enlaza al hijo que desarrolla su paso 1** |

> **Los dos son de la zona del customer development.** El eje nuevo **no encontro
> una zona nueva: encontro por que la vieja se comporta como se comporta.**

---

## 41. EL BARRIDO DE RAZONES: treinta y ocho aperturas reescritas

**Encargo aprobado el 13 ago 2026.** Se busco en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` toda razon que citara la **PARAFRASIS
ABOLIDA** por el banco 9.5.0 y se reescribio citando **LA VARA**.

### 41.1 EL VOLUMEN, y es mayor de lo que la primera busqueda dijo

| busqueda | resultado |
|---|---:|
| primera pasada, solo la forma *sin arista igual a duplicacion* | 27 |
| **pasada completa, incluyendo LA FORMA ESPEJO** *con arista igual a jerarquia sana* | **38** |

> **La forma espejo era el error mas facil de pasar por alto**, y es exactamente
> la mitad que la ratificacion abolio con la frase *la arista no exculpa, y eso
> corta en los dos sentidos*. **Once razones exculpaban por la arista** y ninguna
> busqueda anterior las habia mirado, porque el defecto se buscaba solo del lado
> que acusa.

**LAS APERTURAS QUE SE ENCONTRARON, contadas por forma:**

| veces | la formula |
|---:|---|
| 17 | *y la regla lo resuelve: SIN ARISTA, verificado, o sea DUPLICACION* |
| 13 | *con ARISTA en los dos sentidos, verificada: JERARQUIA SANA* |
| 8 | variantes de las dos anteriores con otro encabezado |

### 41.2 QUE SE CAMBIO, exactamente

**Solo la APERTURA.** El cuerpo de cada razon, con su medicion, su forma medida y
su correccion si la tenia, **queda intacto**.

> **La apertura nueva dice tres cosas:** que la version original citaba la
> parafrasis abolida; que **la arista es DATO DEL GRAFO y no argumento**, y que
> **corta en los dos sentidos, no acusa cuando falta ni exculpa cuando esta**; y
> que la clase la decide la vara, **como se lee mas abajo**.

**LO QUE NO SE TOCO, y hay que decirlo**: varias razones citan la parafrasis
**como historia**, del tipo *el veredicto se emitio con la regla vieja y la regla
que lo gobierna se escribio despues*. **Esas citas son correctas y se conservan**:
son el registro de por que hubo una correccion.

### 41.3 NINGUNA CLASE CAMBIA, y por que

**Verificado una por una: las treinta y ocho sostienen su clase con la vara.**

| grupo | cuantas | por que sobrevive |
|---|---:|---|
| las que ya habian sido corregidas por la ratificacion | 19 | su cuerpo **ya aplicaba la vara**; solo la apertura estaba vieja |
| las de la forma espejo, *con arista* | 13 | su cuerpo **ya decia el contenido**: *el hijo le anade lo suyo*, *ninguno sobra*. La arista era adorno, no argumento |
| las cuatro en **A** (474, 568, 586, 611) | 4 | las cuatro dicen ya, en su cuerpo, que **lo que el hijo anade cabe en una linea**. REPITE por contenido |
| las dos con figura propia (641, 671) | 2 | dos casas de la misma fase y un plan con su matriz: la clase venia del contenido |

> **El marcador no se movio ni un punto**: A 278, B 86, C 5, D 573.
>
> **Y eso es exactamente lo que se esperaba de un barrido de redaccion**: si
> arreglar el texto hubiera movido clases, el problema no habria sido de texto.
> **Lo que el barrido arregla es el ARCHIVO como documento**, no el archivo como
> juicio: cualquiera que lea una de esas treinta y ocho razones a partir de hoy
> **lee la regla vigente y no la abolida.**

> **LA LECCION DE METODO, que es la que vale para el proximo barrido**: **una
> regla abolida no se busca solo en la forma que la nombra.** Se busca tambien en
> **su espejo**, y en este caso el espejo era el 34% del defecto.
