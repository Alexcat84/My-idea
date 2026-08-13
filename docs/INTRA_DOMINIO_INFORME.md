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

> **SEGUNDA EJEMPLAR, 13 ago 2026, y lo encontro el EJE NUEVO**: en la muestra
> pineada del barrido paso-contra-nodo, el candidato numero 4 resulto ser esto y
> no una jerarquia.
>
> | nodo | que manda para el MISMO gesto, centrar el proceso |
> |---|---|
> | `pre_control_estadistico` | centrar el proceso **entre los limites de ESPECIFICACION** al iniciar |
> | `limites_de_especificacion_vs_limites_de_control` | **NUNCA** ajustar el proceso segun si un punto cae dentro o fuera de **especificacion**; ajustar solo cuando el grafico de control senale causa especial |
>
> **Los dos de `quality`.** El pre-control usa la especificacion a proposito,
> porque es una tecnica de arranque rapido; el otro nodo lo prohibe como doctrina
> general. **No es contradiccion: es una excepcion que ninguno de los dos
> declara.**
>
> **Y confirma algo del instrumento nuevo**: un eje que busca jerarquias tambien
> destapa fronteras, porque las dos figuras se parecen por fuera (dos nodos que
> hablan del mismo gesto) y se distinguen solo leyendo.

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

### TANDA R27, VIGESIMOTERCERA CIEGA: seis de seis

**Acumulado: 162 releidas, de las cuales 138 a ciegas. Discrepancias: UNA**, el
395. **Dos perdidas dictadas no resistieron la verificacion y se corrigen abajo.**

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **475** | `customer_profile` contra `customer_profile_value_map` | **priorizar jobs, pains y gains** por importancia, severidad y relevancia, y **los tres tipos de jobs**, funcionales, sociales y emocionales; del otro lado, **comunicar los dos documentos a toda la organizacion** y **usarlos como marcador** en las conversaciones con clientes | de **lector** |
| **476** | `diseno_organizacional_equipos_innovacion` contra `equipo_multifuncional_real` | **liberar tiempo real** de las tareas habituales y las **recompensas por desempeno del equipo** y no solo individual; del otro lado, **elegir la forma de organizar segun la complejidad** y buscar que el equipo este **fisicamente junto** | de **lector** |
| **477** | `customer_profile_value_map` contra `value_proposition_canvas` | **dibujar los dos lados**, el circulo del perfil a la derecha y el cuadrado del mapa a la izquierda, e **iterar hasta encontrar el encaje** | de **lector** |
| **479** | `contratar_ambicion_correcta` contra `screening_ambicion_organizacional` | **el rigor extra en los roles de ventas**, porque ahi los incentivos locales son mas fuertes; del otro lado, **si pregunta por la estrategia antes que por la compensacion** | de **lector** |
| **482** | `advances_vs_continuations` contra `marco_avances_continuaciones` | **evitar objetivos vagos** como recopilar informacion o construir relacion; del otro lado, **la clasificacion del resultado en CUATRO categorias** | de **lector** |
| **483** | `clasificacion_mercados_cadena_suministro` contra `marco_analisis_mercado_cadena_suministro` | **decidir si en cada area hay que liderar, igualar o superar** a la competencia; del otro lado, **revisar el cuadrante periodicamente porque cambia** y **ajustar inventario y precios** segun el cuadrante | de **lector** |

#### DOS CORRECCIONES DEL DICTADO, en el mismo puesto

**Las dos en el 482, y las dos verificadas contra el grafo:**

> **1. *Identifica que falto* NO es perdida: esta en LOS DOS.** Es el paso 4 de
> `advances_vs_continuations` (*si el resultado fue una continuacion, identifica
> que falto para lograr un avance real*) y el paso 2 de
> `marco_avances_continuaciones` (*si el resultado fue una Continuacion,
> identifica que accion concreta falto para convertirla en Avance*). **Es la misma
> frase.**
>
> **2. La clasificacion es en CUATRO, no en tres.** El dictado decia
> *clasifica-en-tres*; el nodo clasifica en **Orden, Avance, Continuacion y
> No-venta**. **La perdida existe y es mas grande de lo dictado**: la cuarta
> categoria, la no-venta, es la que obliga a mirar de frente lo que no funciono.

#### 475 y 477: el CASO FUNDACIONAL de la figura, releido a ciegas

**`customer_profile_value_map` es el UNICO gemelo de la figura CENTRO SANO CON
GEMELO SIN CASA que esta probado por partida doble**, y estos son los dos pares
que lo prueban. **Los dos se releyeron sin mirar el veredicto y los dos
sostienen su A.**

| puesto | contra quien | que repite |
|---:|---|---|
| **477** | **el CENTRO**, `value_proposition_canvas` | los dos lados del lienzo y su trabajo conjunto |
| **475** | **una PIEZA**, `customer_profile` | la especificacion de jobs, pains y gains |

> **Repite con el centro Y con una de sus piezas, y no tiene arista con ninguno de
> los siete miembros de la familia.** Eso es exactamente la figura, y es la unica
> vez que se cumple con las dos mitades probadas: **la forma la da el grafo, el
> gemelo lo dan estas dos lecturas.**
>
> **Lo que la relectura asegura**: despues de que las nueve lecturas dirigidas
> tumbaran nueve candidatos y de que la del racimo de cohortes cayera por un
> veredicto volteado, **la figura se quedo con tres ejemplares. El mas fuerte de
> los tres acaba de pasar la prueba ciega dos veces.** Ya no descansa en una
> lectura vieja.

#### 483: la familia de los CUADRANTES es de SEIS, y yo la conte en cinco

**Correccion declarada de mi propia nomina.** En la tanda R18 reporte esta familia
con **cinco miembros y diez pares posibles**. **Son SEIS.**

| | lo que reporte | lo que es |
|---|---:|---:|
| miembros | 5 | **6** |
| pares posibles | 10 | **15** |
| en la cola | 5 | **7** |
| **leidos** | 4 | **7** |
| **en A** | 4 | **SIETE de siete** |
| nunca en cola | 5 | **8** |

> **El sexto es `marco_analisis_mercado_cadena_suministro`**, y **su A con un
> miembro ya estaba en el archivo cuando conte**: el puesto **704**. **No lo vi
> porque corri el contador sobre el nombre de la familia y este nodo no lo lleva**,
> exactamente el modo de fallo que el banco 9.15 nombra.
>
> **Tercera vez que el BARRIDO DE LAS A habria evitado un error de nomina**, con
> el quinto puro (394) y con la ecuacion de valor (950). **La regla existe desde
> hace un dia y este es su tercer ejemplar retroactivo.**

> **Y con la cifra corregida, esta familia es la mas cargada del inventario**:
> **siete pares leidos y los SIETE en A**, sin un solo sano. **Le faltan ocho
> lecturas y ninguna esta en la cola.**

### TANDA R28, VIGESIMOCUARTA CIEGA: seis de seis

**Acumulado: 168 releidas, de las cuales 144 a ciegas. Discrepancias: UNA**, el
395.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **486** | `build_measure_learn` contra `ciclo_construir_medir_aprender` | **partir de la hipotesis sacada de los dos Canvas** (el paso 0 del primero) y **repetir el ciclo cada vez mas rapido** | de **lector** |
| **487** | `cash_is_king` contra `diferencia_ganancia_flujo_caja` | **revisar el saldo cada semana**, o cada dia en momento critico, y **aprender a leer el estado de flujo** aunque el lenguaje parezca tecnico; del otro lado, **proyectar a doce o dieciocho meses**, **identificar el momento en que crecer deja sin liquidez**, y **conseguir lineas de credito ANTES** de que falte el efectivo | de **lector** |
| **488** | `gestion_de_portafolio_gates_go_kill` contra `sistema_gates_go_kill` | **los seis criterios** de evaluacion y **matar en vez de reducir recursos**; del otro lado, el **scorecard por gate** y **anotar la decision y el motivo** | de **lector** |
| **489** | `periodo_incubacion_mental` contra `wallas_etapa_incubacion` | **alternar entre varios problemas** en vez de agotar cada uno, y **confiar en que la inactividad aparente es productiva**; del otro lado, **registrar en que momentos surgen las ideas** para hallar el patron propio | de **lector** |
| **492** | `asignacion_de_titulos_ejecutivos` contra `seleccion_ceo_fundador` | **mapear el capital humano, social y financiero** que aporta cada fundador, y **documentar por que se asigno cada titulo**, que es mas fino que el *documenta el acuerdo* del otro | de **lector** |
| **494** | `principio_calidad_mvp` contra `producto_minimo_viable` | **repartida por bloques y con una advertencia**, ver abajo | de **lector** |

#### 494: CURA ACOPLADA MAYOR, y es la primera de COSTURADA CONTRA COSTURADA

**Consultada la ficha antes de registrar. Los DOS son costuras confirmadas**, y
eso cambia la forma del arreglo:

| nodo | veredicto de la ficha |
|---|---|
| **`producto_minimo_viable`** | **CONFIRMADA**, bloque **80,2**, el mas alto del archivo. **VEINTIDOS pasos, CINCO narraciones del MVP en fila.** Es **el emblema de la averia** |
| **`principio_calidad_mvp`** | **CONFIRMADA**, bloque **49,2**, catorce pasos, **TRES NARRACIONES del mismo MVP**, y la ficha ya lo llamaba *pariente directo del emblema* |

> **Las curas acopladas anteriores eran COSTURADA contra GEMELO SANO**: se destejia
> uno y se fundia con el otro, en un acto. **Esta es COSTURADA contra COSTURADA**,
> y por eso son TRES movimientos y no dos: **destejer el emblema, destejer al
> pariente, y solo entonces decidir si lo que queda se funde.**
>
> **Tiene precedente exacto**: el puesto **341**, `blueprint_de_experiencia`
> contra `customer_journey_mapping`, donde los dos estaban costurados y el solape
> era mapa contra mapa. **Es la segunda vez que aparece esta forma, y esta cae
> sobre el primer destejido del plan.**

**CONGELADO, y por el motivo mas limpio que ha dado la regla de la dependencia:**

> **El veredicto DEPENDE de que sobreviva, y de forma directa.** Los catorce pasos
> de `principio_calidad_mvp` son tres narraciones: **la calidad en el MVP** (1 a
> 5), **lanzar rapido y aceptar el fallo** (6 a 10) y **el conjunto minimo de
> caracteristicas** (11 a 14). **El solape con el emblema esta casi todo en la
> TERCERA.**
>
> **Si el destejido conserva la narracion de la CALIDAD, el par deja de repetir y
> seria D. Si conserva la del CONJUNTO MINIMO, sigue repitiendo y es A.** No hay
> forma de saberlo antes de la cirugia. **CONGELADO.**

**LA PERDIDA, repartida y verificada como pedia el dictado:**

| sobrevive al destejido y hay que salvarlo | se va con el destejido |
|---|---|
| de `principio_calidad_mvp`, **bloque 1 a 5**: preguntarse si pulir una caracteristica contribuye al aprendizaje, lanzar versiones simplificadas y medir la reaccion real, **no dar por hecho que el estandar de calidad de la industria es lo que el cliente valora**, y **distinguir los defectos que impiden aprender de la baja fidelidad estetica** | del **bloque 11 a 14**, que es el que repite: identificar las funcionalidades criticas, excluir las secundarias, lanzar la minima y monitorear, iterar con el uso real |
| del emblema: **lo que quede tras colapsar sus cinco narraciones**, que hoy no se puede nombrar | |

> **La distincion entre defecto que impide aprender y fealdad aceptable es lo mas
> valioso del par**, y es lo unico que ninguna de las dos cirugias amenaza.

#### 487: EL PRIMER PURO pasa los DOS instrumentos, y sigue en pie

**`cash_is_king` YA estaba dentro**, y esta es la cifra:

| | |
|---|---:|
| miembros | **3**: `cash_is_king`, `diferencia_ganancia_flujo_caja`, `profit_vs_cash` |
| pares posibles | **3** |
| en la cola | **3** |
| **leidos** | **3** (300, **487**, 544) |
| **en A** | **3** |
| **candidatos levantados por el BARRIDO DE LAS A** | **NINGUNO** |

> **Es el primer racimo del archivo que pasa los DOS instrumentos**: el contador
> por nombre no levanta un cuarto miembro que la lectura acepte, **y el barrido de
> las A no levanta ni un candidato.** Ningun nodo del catalogo tiene una A contra
> ninguno de los tres.
>
> **El primer puro se queda como esta, y ahora con la prueba que a los otros les
> falto.**

#### 486: la familia de BUILD-MEASURE-LEARN es de CINCO, y el barrido levanta dos

**El encargo daba tres nodos. Con el contador y el barrido de las A corriendo
juntos salen CINCO.**

| como entro | nodo | evidencia |
|---|---|---|
| dictado | `build_measure_learn` | |
| dictado | `ciclo_construir_medir_aprender` | |
| dictado | `ciclo_crear_medir_aprender` | |
| **barrido de las A** | **`design_test_repeat`** | **723 A** contra `ciclo_construir_medir_aprender` |
| **barrido de las A** | **`testing_process_completo`** | **796 A** contra `design_test_repeat` |

**LA NOMINA:**

| | |
|---|---:|
| miembros | **5** |
| pares posibles | **10** |
| en la cola | **6** |
| **leidos** | **5**, y **los CINCO en A** (213, 376, 486, 723, 796) |
| pendiente de cola | **1** (puesto **1449**) |
| **nunca en cola** | **4** |
| aristas internas | **1** entre cinco |

> **SUB-PURO de cinco miembros, y es el mas grande declarado hasta hoy.** Cinco
> pares leidos, cinco A, cero sanos.
>
> **Y la forma es la peor**: **una sola arista entre cinco nodos** que dicen el
> mismo bucle de cuatro tiempos. **Dos libros lo cuentan cuatro veces y el grafo
> conoce una sola de esas relaciones.**

> **LA LECTURA QUE DECIDE LOS DOS CANDIDATOS, dicha entera**: `design_test_repeat`
> es el bucle desnudo con vocabulario de Value Proposition Design, prototipar,
> testear, aprender y repetir. **Entra.** `testing_process_completo` es el mismo
> bucle **con el instrumental encima**, los dos lienzos, la tarjeta de test, la de
> aprendizaje y el termometro; **entra tambien**, porque su paso 4 es el bucle y
> el resto es la caja de herramientas alrededor, no otro objeto.

#### 492: `seleccion_ceo_fundador` es el DUODECIMO ejemplar de la cura acoplada

| eje | veredicto |
|---|---|
| **la ficha** | **CONFIRMADA**, bloque 46,8, doce pasos, corte **5**, **DOBLE DE LA DECISION DE CEO**: Founder's Dilemmas en 1 a 5 y Horowitz en 6 a 12 |
| **el intra** | **A** en este puesto 492, y **otra A en el 673** contra `errores_comunes_asignacion_roles` |

> **Costurada confirmada con DOS gemelos declarados: cura acoplada.** **Y el
> primero de los dos, el 673, se leyo hace mucho.** El ejemplar se podia declarar
> desde entonces y no se declaro, porque los ejemplares se han ido encontrando
> **uno a uno, cuando una relectura los cruza**, en vez de barriendo.
>
> **Lo que esto pide, y lo dejo propuesto**: un barrido que cruce **las costuras
> confirmadas contra todas las A del archivo**, de una vez. **Van doce ejemplares
> encontrados de uno en uno; el barrido diria cuantos hay.**

**Por el banco 9.9 el par se juzga HOY**: el solape, discutir y negociar quien
sera director general sin dar por hecho que es la persona de la idea, **cae entero
en el bloque 1 a 5** y la juntura esta en el 5. **En cola sin congelar.**

### TANDA R29, VIGESIMOQUINTA CIEGA: seis de seis

**Acumulado: 174 releidas, de las cuales 150 a ciegas. Discrepancias: UNA**, el
395, resuelta.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **498** | `riesgo_cofundadores_relacion_previa` contra `seleccion_relaciones_cofundadores` | **los tres circulos** (cercanos, indirectos, desconocidos) y los **acuerdos explicitos sobre roles y conflictos** si el cofundador es cercano; del otro lado, **revisar si ya trabajaste de verdad con esa persona** y no solo si se conocen socialmente | de **lector** |
| **502** | `split_igual_vs_desigual` contra `teoria_equidad_split_equity` | la **logica social contra la de negocio** y el **riesgo de asimetria** si se elige la equivocada; del otro lado, **no cerrar con un apreton de manos rapido** y **dejar por escrito por que** se eligio igual o desigual | de **lector** |
| **505** | `evaluacion_tecnologias_disruptivas` contra `tecnologias_disruptivas_oportunidad` | **mapear el desempeno de la tecnologia dominante** en el tiempo y **evaluar si esa dominante ya excede las necesidades reales** de los usuarios; del otro lado, la pregunta **y entonces que hago**, la accion concreta | de **lector** |
| **507** | `fase_diseno_prototipado_modelos` contra `proceso_ideacion_modelo_negocio` | la **narrativa por modelo** con retroalimentacion externa, y **no descartar ideas porque un experto diga que no funcionara** | de **lector** |
| **508** | `analisis_trafico_competitivo` contra `capturar_conocimiento_de_mercado` | **los foros y sitios de preguntas** tipo Quora y **disenar tests A/B a partir de los anuncios observados** de la competencia; del otro lado, **los pares de mercados adyacentes, analistas y periodistas** y **los eventos con demos** | de **lector** |
| **510** | `customer_discovery_get_out_of_building` contra `manifiesto_regla1_hechos_fuera_del_edificio` | **no delegar** la investigacion de clientes en empleados o consultores, y **prepararse para feedback impredecible y a veces doloroso** | de **lector** |

#### 507: aqui es donde la duplicacion del 395 se cobra bien, y aguanta la ciega

**El 395 paso de A a D porque cobraba una duplicacion que no era suya. ESTE es el
par al que pertenecia**, y releido sin mirar el veredicto **vuelve a salir A**.

> **Los dos desarrollan la fase 3 de la misma madre** y coinciden en lo esencial:
> generar multiples variantes de modelo de negocio, prototipar cada una con el
> lienzo, y quedarse con la de mas potencial tras explorar.
>
> **Lo que confirma la conjunta**: la duplicacion existe, **esta cobrada una sola
> vez y en el par correcto.** Con la relectura firme, la unica discrepancia del
> ejercicio queda cerrada por los dos lados: el par que sobraba paso a D y el par
> que la sostiene aguanta a ciegas.

#### 508: EL PAR DE ALEXA, y el toque unico ahorra CINCO verificaciones, no cuatro

**Correccion declarada del dictado, verificada contra el grafo.** El nodo que
muere en la fusion, `analisis_trafico_competitivo`, **no nombra cuatro
herramientas: nombra CINCO.**

| paso | herramientas nombradas | estado en el censo |
|---:|---|---|
| **1** | **Alexa** o **Compete** | **las DOS muertas** |
| **5** | **MixRank** o **Adbeat** | las dos **vivas** |
| **6** | **Alexa** o **Quantcast** | Alexa muerta; **Quantcast SIN VERIFICAR** |

**Y el superviviente, `capturar_conocimiento_de_mercado`, dice en su paso 3
*herramientas de medicion de trafico web y rankings de app stores*: cero nombres
propios.**

> **LO QUE ESTO LE HACE AL PLAN, y es el argumento mas limpio que ha dado el TOQUE
> UNICO del banco 9.4**: fundir hacia el superviviente generico **borra cinco
> nombres propios de una sola vez, y con ellos cinco verificaciones de vigencia
> que alguien tendria que hacer y rehacer con los anos.** Dos de los cinco **ya
> estan muertos hoy**.
>
> **No es que el nodo generico sea mejor por ser vago: es que el especifico
> caduca.** Aqui la fusion **no pierde informacion util: pierde mantenimiento.**

**Y QUEDA UN NOMBRE NUEVO PARA EL CENSO**: **`Quantcast`**, citada en el paso 6 de
`analisis_trafico_competitivo`. **Estado: SIN VERIFICAR**, y se registra asi y no
como viva: **no la he comprobado.** Es el nombre propio numero catorce del censo,
detras de AngelList.

#### 510: la familia de SALIR DEL EDIFICIO sigue creciendo

Con los puestos **840** (el genchi gembutsu por duplicado), **849** y **439**,
**este es el cuarto par de la misma zona y el cuarto en A.**

> **Seis nodos del nucleo mandan salir a hablar con clientes**, dos con la palabra
> japonesa y cuatro con la inglesa, **y de los cuatro pares leidos ninguno tiene
> arista.** Es la zona con mas repeticion confirmada y menos cableado del archivo.

---

### TANDA R30, VIGESIMOSEXTA CIEGA: seis de seis

**Acumulado: 180 releidas, de las cuales 156 a ciegas. Discrepancias: UNA**, el
395, cerrada por los dos lados.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **511** | `disenar_tests_pass_fail` contra `diseno_experimentos_pass_fail` | **NADA. Es un subconjunto estricto** y la direccion de la fusion esta forzada; ver abajo | **de catalogo, nula** |
| **513** | `explotacion_tecnologias_disruptivas` contra `tecnologias_disruptivas_oportunidad` | **el analisis IOTA** de impacto de oportunidades y amenazas, el **trabajo de campo con adoptantes tempranos** y **monitorear industrias relacionadas** que trabajan en problemas similares; del otro lado, **mapear el desempeno de la dominante en el tiempo** y **si la dominante ya excede las necesidades reales** | de **catalogo** |
| **514** | `asignacion_persona_ia` contra `ingenieria_de_prompts_efectiva` | **probar multiples personas para la misma tarea y comparar** e **iterar en modo conversacion** paso a paso; del otro lado, las **restricciones de formato, extension y publico objetivo** | de **lector** |
| **518** | `cuatro_capacidades_mercado` contra `estrategia_cuatro_capacidades_mercado` | **invertir en la fortaleza y no en debilidades menores** y **definir metricas por capacidad** como tasa de surtido o tiempo de entrega; del otro lado, **diagnosticar la etapa de madurez del mercado** y la regla de **no invertir en eficiencia interna si compites en mercado de crecimiento** | de **catalogo** |
| **525** | `encuadre_desafio_diseno` contra `how_might_we_framing` | **verificar que la pregunta no sea demasiado general ni demasiado especifica** y **usarla como brujula** durante todo el proceso; del otro lado **TRES cosas y no una**: ver abajo | de **lector** |
| **526** | `homework_frontend_loading` contra `voice_of_customer_homework` | **los clientes de los clientes** de la cadena de valor y el **business case con datos duros**; del otro lado **TRES y no dos**: ver abajo | de **catalogo** |

#### 511: LA FAMILIA PASS/FAIL son CUATRO, no tres, y la evidencia ya estaba escrita

**Los dos instrumentos corridos, como manda el estandar de certificacion.**

| instrumento | que dio |
|---|---|
| **contador** (`contar_nombre.py "pass/fail" "pass fail"`) | **14 nodos vivos** mencionan el termino, 27 menciones |
| **barrido de las A** | **TRES A vigentes** dentro de la familia: **467**, **511** y **639** |

> **CORRECCION DECLARADA del dictado.** El encargo daba la familia como **tres
> nodos vistos**. **Son CUATRO**, y el cuarto no hubo que leerlo: **su A ya
> estaba en el archivo**. Es el puesto **639**,
> `diseno_experimentos_pass_fail` contra `realizar_pruebas_pasa_no_pasa`. **Es
> exactamente el modo de fallo del 9.20**: el miembro que falta se llama por otro
> idioma, *pasa o no pasa* en vez de *pass/fail*, y el ojo lo salta.

**LA NOMINA VIGENTE AL PUESTO 1100: CUATRO miembros**, los cuatro de `core` y los
cuatro del mismo libro.

| nodo | pasos |
|---|---:|
| `diseno_experimentos_pass_fail` | **6** |
| `disenar_tests_pass_fail` | 5 |
| `diseno_experimentos_hipotesis` | 4 |
| `realizar_pruebas_pasa_no_pasa` | 4 |

**Y LA FORMA NO ES UN RACIMO: ES UNA ESTRELLA.** Seis pares posibles, **cinco en
la cola**, cuatro leidos.

| par | puesto | clase |
|---|---:|:---:|
| `diseno_experimentos_pass_fail` contra `diseno_experimentos_hipotesis` | 467 | **A** |
| `diseno_experimentos_pass_fail` contra `disenar_tests_pass_fail` | 511 | **A** |
| `diseno_experimentos_pass_fail` contra `realizar_pruebas_pasa_no_pasa` | 639 | **A** |
| `diseno_experimentos_hipotesis` contra `realizar_pruebas_pasa_no_pasa` | 636 | **D** |
| `disenar_tests_pass_fail` contra `realizar_pruebas_pasa_no_pasa` | 1346 | pendiente |
| `disenar_tests_pass_fail` contra `diseno_experimentos_hipotesis` | **nunca entro a la cola** | |

> **Las tres A tocan al MISMO nodo.** `diseno_experimentos_pass_fail`, el de seis
> pasos, repite con los otros tres; **y los dos perifericos leidos entre si dan
> D** (636: uno disena la prueba, el otro fija el umbral que la decide). **Es un
> centro con radios, no un racimo cerrado**, y por eso la familia queda
> **MEZCLADA** decida lo que decida el 1346.
>
> **Y la unica arista interna de los cuatro une justo al par que nunca entro a la
> cola**, `disenar_tests_pass_fail` con `diseno_experimentos_hipotesis`. **El
> cableado esta puesto donde la cola no mira, y falta en los tres pares que si
> repiten.**

**POR QUE EL 511 NO PIERDE NADA, y es el A mas barato leido hasta aqui.** Los
**cinco** pasos de `disenar_tests_pass_fail` estan **todos** dentro de los seis
del otro:

| paso del que muere | donde vive |
|---|---|
| que se quiere aprender | paso 1 |
| el test mas simple posible | paso 2, **que ademas dice con que**: paginas de aterrizaje, presentaciones o maquetas |
| criterios numericos claros | paso 3, **que ademas da la cifra**: nueve de treinta pedidos |
| ejecutar y no detenerlo antes de tiempo | pasos 4 y 5, **que ademas dan el tamano**, diez a treinta prospectos, y **el motivo**, no confundir un maximo local con el global |
| registrar aprendizajes, no solo datos | paso 6 |

> **CORRECCION DECLARADA, la segunda de este puesto.** Las tres perdidas que
> proponia el encargo, paginas de aterrizaje, duracion suficiente y grupo de diez
> a treinta, **son material del SUPERVIVIENTE, no del que muere**. Aqui **la
> direccion de la fusion no se elige: esta forzada**, y por eso **la perdida es
> cero**. Es el unico A del archivo hasta ahora que no necesita reparto por
> bloques.
>
> **Y una precision de vocabulario, verificada**: la palabra **preventas** no
> aparece en ninguno de los dos nodos. Lo que el paso 2 dice es **paginas de
> aterrizaje, presentaciones o maquetas**.

#### 513: y de paso, un racimo de tres que la cola NO PUEDE cerrar

**Barrido de las A sobre los tres nodos de tecnologias disruptivas de Cooper:**

| puesto | el par | clase |
|---:|---|:---:|
| **505** | `evaluacion_tecnologias_disruptivas` contra `tecnologias_disruptivas_oportunidad` | **A** (R29) |
| **513** | `explotacion_tecnologias_disruptivas` contra `tecnologias_disruptivas_oportunidad` | **A** (esta tanda) |
| | `evaluacion_` contra `explotacion_` | **NO EXISTE EN LA COLA** |

> **`tecnologias_disruptivas_oportunidad` tiene DOS A vigentes**, o sea que por el
> 9.20 los otros dos son **candidatos a miembro** de una misma familia. **Otra
> estrella, y esta con el centro leido por los dos lados.**
>
> **Lo que hay que decir y no adivinar**: el par que probaria o rompería la
> familia, evaluacion contra explotacion, **no esta en la cola**. **El cribado no
> lo va a decidir nunca**, por mucho que avance. Queda anotado como lo que es:
> **un racimo candidato que este ejercicio no puede cerrar solo**, y que necesita
> una lectura dirigida si alguien quiere la nomina firme.

#### 514: NO es del racimo IA-supervision, y no es una pareja adyacente: es OTRA FAMILIA

**Verificado contra la nomina de OCHO de la seccion 11, antes de escribir esto.**

| pregunta | respuesta medida |
|---|---|
| estan los dos nodos en la nomina de ocho | **NO. Ninguno de los dos.** |
| pares en la cola entre este par y los ocho | **CERO** |

> **Y ahi esta la diferencia con los dos casos anteriores.** La pareja de las
> **alucinaciones** (363) y la del **invitar a la IA a todo** (456) son parejas
> **adyacentes con condicion viva**: cada una tiene **UN puesto de la cola** que
> decide si entra al racimo, el **1478** y el **1517**. **Esta no tiene ninguno.**
> No es adyacente al racimo: **esta en otro sitio del mismo libro.**

**LO QUE SI ES: la cabeza de la FAMILIA DEL PROMPTING**, tambien de Mollick.
**Contador** (`contar_nombre.py "prompt"`): **13 nodos vivos**, 33 menciones. **De
ellos, siete con pares en la cola entre si:**

| puesto | el par | clase |
|---:|---|:---:|
| **514** | `asignacion_persona_ia` contra `ingenieria_de_prompts_efectiva` | **A** |
| **955** | `asignacion_persona_ia` contra `prompting_alta_variacion` | **D** |
| **1125** | `ingenieria_de_prompts_efectiva` contra `prompting_cadena_de_pensamiento` | pendiente |
| **1144** | `ingenieria_de_prompts_efectiva` contra `prompting_por_persona_ia` | pendiente |
| **1175** | `asignacion_persona_ia` contra `prompting_por_persona_ia` | pendiente |
| **1191** | `ingenieria_de_prompts_efectiva` contra `prompting_alta_variacion` | pendiente |
| **1220** | `disenar_prompts_efectivos_para_ia` contra `ingenieria_de_prompts_efectiva` | pendiente |

> **CUATRO de los cinco pendientes caen en el tramo 1101-1200**, o sea en el
> checkpoint que viene. **No adelanto nada**: lo anoto para que cuando salgan se
> lean como lo que son, la evidencia de una familia, y no como pares sueltos.
>
> **Una sola arista interna entre los siete**, `ingenieria_de_prompts_efectiva`
> con `prompting_cadena_de_pensamiento`, y esta puesta en los dos sentidos.
>
> **Y queda una sospecha anotada, no adjudicada**: el titulo de
> `ingenieria_de_prompts_efectiva` es *Ingenieria de Prompts como Habilidad
> Practica* y existe un nodo llamado **`habilidad_prompting_como_experticia`**.
> **No hay par entre ellos en la cola.** Lo digo porque se ve, no porque lo haya
> leido.

#### 525: el par que da nombre al racimo HMW, y el lado de IDEO pierde TRES cosas

**CORRECCION DECLARADA.** El encargo daba una sola perdida del lado de IDEO,
documentar contexto y restricciones. **Son tres**, verificadas contra los dos
nodos:

| lo que solo tiene `encuadre_desafio_diseno` | |
|---|---|
| **definir el impacto ultimo que se busca lograr** | HMW no lo pide en ningun paso |
| **listar posibles soluciones pensando ampliamente**, permitiendo resultados sorprendentes | HMW no lo pide |
| **documentar contexto y restricciones** geograficas, tecnologicas, de tiempo y de poblacion | HMW no lo pide |

> **Y el encuadre de IDEO al lado le da al racimo una lectura que no tenia.** HMW
> es **puro trabajo sobre la pregunta**: redactarla, calibrar su altura, iterarla
> con el equipo, usarla de brujula. IDEO **envuelve la pregunta en su mundo**: el
> impacto que persigue, las soluciones que ya se imaginan y las restricciones
> reales.
>
> **El corazon repetido es el mismo en los dos**, formular el problema como
> pregunta abierta y ajustarla segun lo aprendido, **y por eso el par es A**.
> **Pero la fusion aqui no es simetrica**: el superviviente tiene que quedarse
> con la calibracion de altura de HMW **y** con el contexto y las restricciones de
> IDEO, o la pregunta queda bien formulada y flotando.

#### 526: y el lado del homework pierde TRES, no dos

**CORRECCION DECLARADA, y una precision.** El encargo daba dos perdidas del lado
de `homework_frontend_loading`. **Son tres:**

| lo que solo tiene `homework_frontend_loading` | |
|---|---|
| **el screening inicial** antes de comprometer recursos | ya listado en el encargo |
| **evaluar fuentes de suministro y aspectos de operaciones o manufactura** | **no estaba listado**, y no aparece en el otro nodo en ninguna forma |
| **el business case con analisis financiero Y PLAN DE ACCION** | ya listado |

> **Y la precision sobre la evaluacion tecnica**, que el encargo daba como perdida
> del lado de la voz del cliente: **no es una ausencia, es una diferencia de
> profundidad.** `homework_frontend_loading` **si tiene** evaluacion tecnica, en
> su paso 2, pero **preliminar** y en paralelo con la de mercado;
> `voice_of_customer_homework` la pone **antes de aprobar el proyecto**, o sea
> como puerta. **No se pierde el gesto: se perderia el momento en que se hace.**
>
> **Y la version profunda de esa misma evaluacion vive en un tercer nodo**,
> `etapa_build_business_case`, leido en el puesto **1099**: *evaluacion tecnica y
> operativa detallada de viabilidad*. **Tres nodos del mismo libro tienen la misma
> evaluacion a tres profundidades distintas**, y solo una de las tres parejas ha
> pasado por la cola.

### TANDA R31, VIGESIMOSEPTIMA CIEGA: seis de seis

**Acumulado: 186 releidas, de las cuales 162 a ciegas. Discrepancias: UNA**, el
395, cerrada por los dos lados.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **531** | `diferencia_ventaja_beneficio` contra `framework_caracteristicas_ventajas_beneficios` | **clasificar cada afirmacion** en caracteristica, ventaja o beneficio y **revisar transcripciones propias midiendo la proporcion**; del otro lado, **el remedio**, ver abajo | de **lector** |
| **536** | `fit_problema_solucion` contra `problem_solution_fit` | **familia declarada**: el reparto NO se cierra en el par | ver abajo |
| **537** | `channels_hypothesis_web_mobile` contra `seleccion_canal_distribucion` | **probar varios canales con presupuesto parecido** para comparar el costo por cliente; del otro lado, los **habitos de compra establecidos** de la categoria y la **complejidad y precio** del producto frente al canal | de **catalogo** |
| **541** | `encuesta_satisfaccion_postproyecto` contra `reunion_conclusion_proyecto` | el **monitoreo de tres meses** contra el remordimiento posterior, **el contenido** de la encuesta interna y **pedir testimonios solo despues de dar valor** | de **catalogo** |
| **544** | `cash_is_king` contra `profit_vs_cash` | **familia declarada**: es el PRIMER PURO, el reparto no se cierra en el par | ver abajo |
| **547** | `customer_segments_hypothesis` contra `segmentos_de_clientes_problema_necesidad` | **el dia en la vida**, el **mapa de influencia** y **salir del edificio a observar**; del otro lado, los **mercados de varios lados**. Y **DOS ROLES que el encargo no listaba**, ver abajo | de **catalogo** |

#### 536 y 544: la regla operativa de las familias declaradas, sin pelear la clase

**Los dos pares son A y los dos siguen siendo A.** Lo que NO se decide aqui es la
direccion de la fusion, por el **banco 9.3**: *una direccion de fusion decidida
sobre un par no sobrevive a su familia.*

| par | su familia | que decide la mesa y no el par |
|---:|---|---|
| **536** | **la puerta del ajuste** | no cual de los dos sobra, sino **si el catalogo quiere uno, dos o tres hitos** en esta zona |
| **544** | **el primer puro**, el efectivo contra la ganancia | cual de los **tres** miembros sobrevive, no cual de estos dos |

**PRECISION MEDIDA sobre el 536, con el barrido de las A corrido antes de
escribir**: el barrido levanta **CERO candidatos** fuera de la pareja. **La
familia del ajuste es hoy una PREGUNTA DECLARADA, no una nomina medida**: lo que
esta escrito es que dos nodos llevan nombres de dos hitos distintos, no que haya
mas miembros. **Conviene decirlo asi y no llamarla racimo.**

> **Y un hecho del 536 que la mesa necesita**: `fit_problema_solucion` tiene
> **fuente doble** (*Value Proposition Design* y *Traction*) y sus pasos 4 a 6 son
> del segundo libro, las fases I, II y III del embudo de traccion. **Fusionar aqui
> mueve material de un libro que el otro nodo no toca.**

**Y el 544 SI es nomina medida**: tres miembros, tres pares posibles, los tres
leidos (**300, 487, 544**) y los tres en A, **y el barrido no levanta ni un
candidato**. Es el puro numero 1 de la tabla viva.

#### 537: la familia del canal suma su TERCERA especializacion, y hay que recomputar su ficha

**Es el tercer par en A contra el mismo nodo general**,
`seleccion_canal_distribucion`, y esta vez con la especializacion **digital**.

> **TERCER VOTO A FAVOR DE LA LECTURA MADRE-HIJAS**, y queda anotado en la
> candidatura del racimo: el general no repite con hermanos cualquiera, **repite
> con sus propias especializaciones**, la fisica (165), la del lienzo (400) y la
> digital (537). **Lo que se pierde en cada fusion no es una concrecion suelta:
> es un canal entero que el general no puede llevar sin dejar de ser general.**

**RECOMPUTO DEL ARCHIVO, por el banco 9.10, y la ficha del racimo estaba vieja.**
La seccion 10 decia *cuatro veredictos A de quince pares posibles, con cuatro
pendientes en la cola: 609, 762, 945 y 1488.* **Tres de esos cuatro ya estan
leidos.**

| medida | lo que decia la ficha | **lo que dice el archivo hoy** |
|---|---|---|
| pares leidos | 4 | **7** |
| en A | 4 | **7** |
| pendientes en cola | 4 (609, 762, 945, 1488) | **1** (solo el 1488) |

> **Los tres nuevos son 609, 762 y 945, y los TRES en A.** Y dos de ellos, el 762
> y el 945, **no tocan al nodo general**: son especializaciones que repiten
> **entre si**.
>
> **Lo que eso cambia, y es lo importante**: la familia del canal **NO es un
> racimo en estrella** (banco 9.23). **Es un SUB-PURO de seis miembros con siete
> pares leidos y los siete en A, sin un solo sano en toda la familia.** Empata con
> los cuadrantes de mercado como **el sub-puro mas cargado del inventario**, y no
> estaba en la tabla viva. Se anade.

#### 531: la perdida es de dos lados, no de uno

**CORRECCION DECLARADA.** El encargo listaba las dos perdidas del lado del marco.
**Verificadas y correctas.** Pero el otro lado tambien pierde, y no estaba
listado:

| lo que solo tiene `diferencia_ventaja_beneficio` | |
|---|---|
| **EL REMEDIO** | el marco dice *evita presentar caracteristicas antes de desarrollar necesidades explicitas*, o sea **la prohibicion**. Este dice ademas **que hacer en su lugar**: *vuelve a preguntas de implicacion o de necesidad y beneficio*. **La prohibicion sin el remedio deja al lector parado** |
| la regla de la **apertura** | *evita ABRIR la conversacion con ventajas genericas*. El marco lo cubre por implicacion, pero **no nombra el momento** |

#### 541: la encuesta interna no se pierde, se pierde SU CONTENIDO

**PRECISION DECLARADA.** El encargo listaba *encuesta interna al equipo* como
perdida. **Las dos la tienen**: `encuesta_satisfaccion_postproyecto` dice en su
paso 5, en una linea, *aplica la encuesta tanto a tu equipo como a tu cliente*.

> **Lo que se perderia es lo que hay que PREGUNTARLE al equipo**, que solo esta en
> `reunion_conclusion_proyecto`: **satisfaccion de trabajar con ese cliente y
> disposicion a repetir**. Sin eso queda la instruccion de encuestar al equipo y
> ninguna pregunta que hacerle. **Las otras dos perdidas del encargo, el monitoreo
> de tres meses y pedir testimonios solo despues de dar valor, se verifican
> enteras.**

#### 547: la escala esta en los dos, y se pierden DOS ROLES que no estaban listados

**DOS CORRECCIONES DECLARADAS, las dos verificadas contra los dos nodos.**

**PRIMERA: la escala de consciencia NO se pierde.** El encargo la listaba como
perdida de `customer_segments_hypothesis`. **Los dos nodos la tienen, con
etiquetas distintas para los mismos cuatro niveles:**

| `customer_segments_hypothesis` | `segmentos_de_clientes_problema_necesidad` |
|---|---|
| no lo nota / lo nota pero no actua / busca solucion / ya la improviso | latente / pasivo / activo / con solucion casera |

> **Es la misma escala en dos vocabularios.** Lo unico que de verdad solo tiene el
> primero es **el mercado de varios lados**.

**SEGUNDA, y es la que importa: cada nodo nombra TRES roles de compra y solo
comparten UNO.**

| nodo | los roles que nombra |
|---|---|
| `customer_segments_hypothesis` | quien **usa**, quien **paga**, quien **decide** |
| `segmentos_de_clientes_problema_necesidad` | quien **usa**, quien **influye**, quien **recomienda** |

> **La union son CINCO roles y la interseccion es UNO.** Una fusion que se quede
> con cualquiera de los dos **pierde dos roles del mapa de compra**, y son
> justamente los que deciden a quien hay que entrevistar. **No estaba en la lista
> de perdidas y es la mas cara del par.**

### TANDA R32, VIGESIMOCTAVA CIEGA: seis de seis

**Acumulado: 192 releidas, de las cuales 168 a ciegas. Discrepancias: UNA**, el
395, cerrada por los dos lados.

**Esta tanda se releyo con una regla nueva de trabajo: cada perdida propuesta se
BUSCA EN EL GRAFO antes de clasificarla.** Cuatro de las seis cambiaron de lista.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **549** | `filosofia_customer_validation` contra `introduccion_validacion_clientes` | **familia declarada**: el reparto no se cierra en el par | ver abajo |
| **550** | `preservar_efectivo_buscar_modelo` contra `restriccion_gasto_validacion` | **la reserva de caja para varios pivotes**, las **cifras** del presupuesto por prueba, y del otro lado **invertir tras el encaje** y **el criterio propio de validado**. **La tasa de consumo NO se pierde** | de **catalogo** |
| **558** | `diseno_de_experiencias_participativas` contra `economia_de_la_experiencia` | **los ejemplos de marcas**; del otro lado **TRES cosas y no dos** | de **lector** |
| **559** | `warrants_deuda_convertible` contra `warrants_financiamiento` | el **plazo de cinco a diez anos**, el **pago separado**, el **porcentaje de cobertura**; del otro lado **negociar valoracion en vez de warrant**. **La contabilidad esta en los dos** | de **catalogo** |
| **561** | `evaluacion_vp_ventas` contra `framework_evaluacion_director_ventas` | **las referencias del propio equipo** y **como contrata talento**; del otro lado el **modelo de evaluacion de representantes** y **los procesos tecnicos de venta**. **Las referencias de clientes estan en los dos** | de **catalogo** |
| **562** | `plan_a_b_c_soft_landing` contra `restructuracion_deuda_soft_landing` | **avisar apenas se detecte la desviacion** y **como te califica el prestamista**; del otro lado el **cierre ordenado que minimiza danos** | de **catalogo** |

#### 549: familia declarada, la apertura de Customer Validation

**El par es A y sigue siendo A.** Lo que no se decide aqui es la direccion de la
fusion, por el **banco 9.3**.

> `filosofia_customer_validation` tiene **DOS A vigentes**: esta y la del puesto
> **1096** contra `earlyvangelists_ventas_tempranas`. **Es el centro de la
> apertura de la etapa**, y en el tramo 1101-1200 salio sano contra cinco nodos
> mas. **Repite con quien abre la etapa y jerarquiza con quien la ejecuta.**
>
> **Lo que la mesa decide y el par no**: si el catalogo quiere **una** puerta de
> entrada a Customer Validation o **dos**. Aqui solo esta medido que estas dos
> dicen lo mismo.

#### 550: la tasa de consumo NO se pierde, y hay que quitarla de la lista

**CORRECCION DECLARADA, con la busqueda hecha en el grafo antes de clasificar.**

| perdida propuesta | verificacion | veredicto |
|---|---|---|
| **reserva para multiples pivotes** | el termino aparece en **UN SOLO nodo vivo**, este | **perdida real** |
| **presupuesto maximo por prueba** | el gesto sobrevive en `plan_de_adquisicion_acquire` (*limita el gasto por prueba a una cifra que puedas permitirte*), **pero las cifras 2.000 a 10.000 dolares estan solo aqui** | **perdida PARCIAL: se pierde la cifra, no el gesto** |
| **mide la tasa de consumo de caja** | vive en `cash_is_king`, `burn_rate_por_etapa`, `metricas_de_startup`, `metrics_that_matter_framework` y varios mas | **NO ES PERDIDA** |
| **invertir agresivamente tras el encaje** | *llenar el canal de ventas* aparece **solo aqui** | **perdida real** |
| **documenta tu criterio de validado** | *que constituye un modelo validado* aparece **solo aqui** | **perdida real** |

> **De cinco perdidas propuestas, una se cae entera y otra se reduce a una cifra.**
> **La busqueda en el grafo cuesta una consulta y cambio el 40% de la lista.**
> Queda como practica de las tandas que vienen.

#### 558: el lado de la economia pierde TRES, y aparece un nombre propio para el censo

**CORRECCION DECLARADA.** El encargo daba dos perdidas del lado de
`economia_de_la_experiencia`. **Son tres:**

| lo que solo tiene `economia_de_la_experiencia` | |
|---|---|
| **disenar elementos que generen conexion emocional** | **no estaba listado.** El otro nodo solo IDENTIFICA si la propuesta es emocional; este manda DISENAR lo emocional |
| **evaluar la ejecucion del detalle** (calidad, distribucion, precio, diseno fisico) | ya listado |
| **iterar con el mismo rigor que la ingenieria de un producto** | ya listado |

> **Y el otro lado es casi un subconjunto**: los tres pasos de
> `diseno_de_experiencias_participativas` estan dentro de los cinco del otro salvo
> uno, **y ese uno son DOS NOMBRES PROPIOS**: *Whole Foods* y *Virgin America*,
> los unicos del grafo entero segun la busqueda.
>
> **AVISO PARA LA FICHA DE VIGENCIA, y lo digo como aviso y no como hallazgo**:
> **Virgin America** es un nombre que conviene verificar antes de conservarlo en
> una fusion. **NO lo he comprobado en esta sesion** y por eso no lo registro
> como muerto: lo registro como **PENDIENTE DE VERIFICAR**, igual que Quantcast.

#### 559: la contabilidad esta en los dos, con movimientos opuestos

**PRECISION DECLARADA.** El encargo listaba *complica la contabilidad* como
perdida de `warrants_financiamiento`. **Los dos la nombran, y hacen cosas
distintas con ella:**

| nodo | que dice de la contabilidad |
|---|---|
| `warrants_deuda_convertible` | **la REMEDIA**: pedir que el pago de los warrants quede separado del resto para evitar el descuento de emision original |
| `warrants_financiamiento` | **la usa para DECLINAR**: evaluar si el warrant complica innecesariamente la contabilidad **y la estructura legal a largo plazo** antes de aceptarlo |

> **No se pierde el tema: se perderia uno de los dos movimientos.** Y lo que si es
> exclusivo del segundo es **la estructura legal a largo plazo** y **la
> alternativa de negociar una valoracion previa mas baja** cuando el warrant solo
> se propone por precio.
>
> **Las tres perdidas del primero se verifican enteras**: el plazo de cinco a
> diez anos, el pago separado, y el porcentaje de cobertura de la nota. **Ojo con
> este ultimo**: los dos nodos dicen *20%*, pero uno lo usa como **cobertura del
> monto de la nota** y el otro como **tope de descuento en un prestamo puente**.
> **Misma cifra, dos magnitudes distintas.**

#### 561: las referencias de clientes estan en los dos, y falta un tercer exclusivo

**DOS CORRECCIONES DECLARADAS.**

**PRIMERA: las referencias de clientes NO se pierden.** El encargo las listaba
como exclusivas de `evaluacion_vp_ventas`. **Los dos las piden**, uno en su paso 5
y el otro en su paso 6, y los dos para lo mismo, confirmar que cerro negocios
grandes.

**SEGUNDA: lo que si es exclusivo de `evaluacion_vp_ventas` son DOS cosas y una
no estaba listada:**

| exclusivo de `evaluacion_vp_ventas` | |
|---|---|
| el **modelo de evaluacion de representantes**, con la distincion entre transaccionales y de venta a empresas grandes | ya listado |
| los **procesos tecnicos de venta**: comparativas, pruebas de concepto, demostraciones y documentos de bloqueo | **no estaba listado**, y es lo unico del par que baja al detalle de como se vende |

**Y las dos del otro lado se verifican enteras**: las referencias **del propio
equipo** para confirmar si la gente lo seguiria, y **como identifica y contrata
talento** con ejemplos de contrataciones fallidas.

#### 562: verificado entero, con una nota

**Las tres perdidas propuestas se verifican.** Y queda anotado que **el trato
profesional con prestamista e inversionistas esta en los dos**, en el paso 3 de
uno y el 4 del otro: **lo que se perderia del lado del plan A B C no es la
profesionalidad sino el CIERRE ORDENADO como paso propio**, el que minimiza
perdidas para todos los involucrados cuando ya no hay venta posible.

### TANDA R33, VIGESIMONOVENA CIEGA: seis de seis

**Acumulado: 198 releidas, de las cuales 174 a ciegas. Discrepancias: UNA**, el
395, cerrada por los dos lados.

**Cada perdida propuesta se busco en el grafo antes de clasificarla**, como en la
R32. **Cinco de las seis cambiaron de lista.**

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **568** | `publicidad_offline_pruebas_locales` contra `tracking_publicidad_offline` | **las pruebas locales en paralelo** y **revisar el rendimiento cada tanto**; del otro lado **la pregunta de como se entero** y **el codigo por canal**. **Los espacios sobrantes NO se pierden** | de **catalogo** |
| **570** | `desarrollo_presentacion_problema` contra `presentacion_problema_tres_columnas` | **el costo estimado del problema**, **que deberia haberte preguntado**, **las referencias** y **el formato de una diapositiva**; del otro lado **dos preguntas**. **Las tres columnas estan en los dos** | de **lector** |
| **571** | `gamificacion_onboarding_visual` contra `visualizacion_progreso_onboarding` | **entregar el elemento entero en el arranque** contra **enviar solo lo del paso actual** y **anticipar el siguiente**. **Y las dos instrucciones se contradicen** | de **lector** |
| **573** | `colaboracion_cadena_suministro` contra `compartir_datos_cadena_suministro` | **medir el efecto latigo y graficarlo** y **la posicion en la cadena**; del otro lado **evaluar cuantitativamente beneficios contra riesgos** y **compartir decisiones internas** | de **catalogo** |
| **574** | `gestion_portafolio_formal` contra `portfolio_management` | **familia declarada**, y ahora dentro de la MESA UNIDA | ver abajo |
| **586** | `brainstorming_efectivo` contra `construir_sobre_ideas_ajenas` | **la prioridad de construir por encima de generar**; del otro lado **no atribuir la idea a una sola persona** | de **lector** |

#### 570: LA ARISTA EXISTE Y AUN ASI ES DUPLICACION

**Es el ejemplar que faltaba, y hay que decir de que regla.** El banco 9.5.0
registro que **la arista no exculpa**, y que la parafrasis abolida solo conservaba
la mitad que acusa. **Esta es la otra mitad, y hasta hoy nunca habia disparado en
el archivo.**

| | |
|---|---|
| **la arista** | existe **en los dos sentidos**, verificada resolviendo a nodo vivo |
| **el veredicto** | **A**, sostenido a ciegas |

> **Los dos nodos son la misma reunion, paso por paso**: presentar solo los
> problemas y pausar, preguntar como lo resuelve hoy, presentar la solucion
> propia al final, y observar la reaccion. **El cableado esta bien puesto y el
> contenido esta duplicado de todos modos.**
>
> **Lo que esto le hace a la regla**: durante el ejercicio, la falta de arista se
> uso muchas veces como sintoma. **Aqui la arista esta y no salva nada.** Queda
> como ejemplar de la mitad que exculpa, junto al de la mitad que acusa.

**CORRECCION DECLARADA de las perdidas.** El encargo listaba *las tres columnas*
como perdida del segundo nodo. **Estan en los dos**: el paso 1 de
`desarrollo_presentacion_problema` dice literalmente *una presentacion simple de
una diapositiva con tres columnas*.

| lo que si es exclusivo de cada uno | |
|---|---|
| `presentacion_problema_tres_columnas` | **DOS preguntas y no una**: como RANKEA el cliente las soluciones actuales, y como se compara la solucion propuesta con ellas |
| `desarrollo_presentacion_problema` | el **costo estimado del problema** en tiempo, dinero o frustracion, verificado como unico en el grafo; **que deberia haberte preguntado**; **pedir referencias**; y **el formato de UNA DIAPOSITIVA**, que no estaba listado |

#### 568: los espacios sobrantes NO se pierden, y hay un nodo entero de eso

**CORRECCION DECLARADA, con la busqueda hecha.**

| perdida propuesta | verificacion | veredicto |
|---|---|---|
| **espacios sobrantes con descuento** | existe **`publicidad_remanente_remnant_ads`**, un nodo dedicado entero al tema | **NO ES PERDIDA** |
| revisar el rendimiento cada tanto porque el anuncio decae | no aparece en esa forma en ningun otro nodo de la zona | **perdida real** |
| la pregunta *como se entero de nosotros* | **NINGUN** otro nodo vivo la trae | **perdida real** |
| un codigo de descuento por canal | **NINGUN** otro nodo vivo lo trae | **perdida real** |

> **Y una perdida que no estaba listada**: `publicidad_offline_pruebas_locales`
> es el unico que manda **disenar varias pruebas pequenas EN PARALELO en distintos
> mercados locales**. El otro nodo mide una campana; este disena un experimento
> con varias plazas a la vez.

#### 571: la fase ACCLIMATE sube a CINCO nodos, no a cuatro, y los dos nuevos se contradicen

**CORRECCION DECLARADA.** El encargo daba este par como el **cuarto** nodo de la
fase. **Son dos nodos, y los dos son nuevos para la cuenta: la fase pasa de tres a
CINCO.**

| nodo | como llega a la fase |
|---|---|
| `fase_acclimate` | por nombre |
| `fase_acclimate_experiencia_cliente` | por nombre |
| `fase_acclimate_mapa_de_proceso` | por nombre |
| **`gamificacion_onboarding_visual`** | **por contenido**: su resumen y sus condiciones hablan de la implementacion larga y tecnica, que es esta fase. **No la nombra** |
| **`visualizacion_progreso_onboarding`** | **por contenido**, igual |

**LOS CUATRO PARES LEIDOS: dos A y dos B.**

| puesto | el par | clase |
|---:|---|:---:|
| 447 | experiencia_cliente contra mapa_de_proceso | **A** |
| **571** | gamificacion contra visualizacion | **A** |
| 253 | fase_acclimate contra experiencia_cliente | B |
| 196 | fase_acclimate contra mapa_de_proceso | B |

> **DOS PARES DE GEMELOS SEPARADOS DENTRO DE LA MISMA FASE**, y ningun par leido
> entre los dos grupos. **Los de nombre repiten entre si y los de contenido
> repiten entre si**, y nadie ha cruzado los dos.

**Y LA CONTRADICCION, que es lo que la mesa va a tener que resolver:** los dos
nodos del 571 dicen lo contrario sobre el mismo gesto.

| `gamificacion_onboarding_visual` | `visualizacion_progreso_onboarding` |
|---|---|
| **entregar el elemento fisico o digital AL INICIO, junto con el arranque** | **enviar SOLO la informacion necesaria del paso actual**, evitando saturar al cliente con todo el proceso de una vez |

> **Es la CUARTA tension declarada del ejercicio**, con los puestos 1120, 1155 y
> 1229. **El superviviente no puede llevar las dos**, y no lo adjudico.

#### 573: duplicacion cruzada, y falta un exclusivo del segundo lado

**Verificado por lectura y no por parecido de titulo.** `colaboracion_cadena_suministro`
dedica sus pasos **4 y 5** a establecer acuerdos de intercambio de datos y montar
un sistema barato de visibilidad; y **eso es el asunto entero** de
`compartir_datos_cadena_suministro`. **El cruce es real y va en un solo sentido.**

**CORRECCION DECLARADA**: del lado de `compartir_datos_cadena_suministro` se
pierden **DOS y no una**. La listada, evaluar cuantitativamente los beneficios de
colaborar frente a los riesgos de exposicion; **y una que no estaba: compartir
DECISIONES internas con impacto en la demanda, como las promociones, con los
proveedores clave.** El otro nodo comparte **datos** de inventario y de punto de
venta; **solo este comparte decisiones**, que es otra cosa y llega antes.

**Las dos del primer lado se verifican enteras**: medir el efecto latigo comparando
pedidos entrantes contra salientes y graficar la divergencia, y determinar la
posicion de la empresa en la cadena.

#### 574: familia declarada, y ahora la familia es la MESA UNIDA

**El par es A y sigue siendo A.** Lo que no se decide aqui es la direccion de la
fusion, por el **banco 9.3**. **Y la novedad es de tamano**: cuando este par se
leyo, su familia era el racimo del portafolio. **Hoy los dos son miembros de la
mesa unida de DIECISEIS nodos**, adjudicada el 14 ago 2026.

> **Lo propio de `gestion_portafolio_formal` son los STRATEGIC BUCKETS** con
> asignacion de recursos por cubeta y ranking dentro de cada una hasta el limite,
> y la cadencia de dos a cuatro revisiones al ano. **Lo propio de
> `portfolio_management` es la cifra**, que alrededor de un tercio de los proyectos
> suele sobrar. **La mesa decide con dieciseis nodos delante, no con dos.**

#### 586: el racimo del brainstorming es de CINCO, y eso agranda la cura mas cara del plan

**El par es A y sigue siendo A.** `construir_sobre_ideas_ajenas` no trae
procedimiento: comparte ideas abiertamente, fomenta sesiones de construccion
colectiva y evita atribuir. **Eso es la regla que `brainstorming_efectivo` enuncia
en su paso 2 y practica en su paso 1**, diferir el juicio.

**LO QUE ESTE PAR DESTAPA, y es lo importante de la tanda.** El barrido de
confirmadas conto los gemelos DIRECTOS de `brainstorming_divergente` y dio tres:
`brainstorming_efectivo` (823), `reglas_brainstorming` (834) y
`generar_multiples_opciones` (844). **De ahi salio la ficha del NODO DE MAS
FRENTES con una cura acoplada de CUATRO nodos en un solo acto.**

> **Medido hoy con la nomina cerrada por el 9.20, la familia es de CINCO**, porque
> `construir_sobre_ideas_ajenas` repite con uno de los tres gemelos. **CINCO pares
> en la cola, los CINCO leidos y los CINCO en A: es un SUB-PURO de cinco miembros**
> con una sola arista interna.
>
> **Y arrastra un sexto candidato**: `pensamiento_convergente_divergente`, por la
> A del puesto 943 con `generar_multiples_opciones`.

**LA LECCION DE METODO, y no es que el barrido fallara:** el barrido de las A
contesta **quien es gemelo de un nodo**. Una **cura acoplada fusiona una
familia**, y una familia es el cierre transitivo de esa relacion. **Son dos
preguntas distintas, y la ficha del plan uso la respuesta de la primera para la
segunda.** La cura de `brainstorming_divergente` no es de cuatro nodos: **es de
cinco, y puede ser de seis.**

### TANDA R34, TRIGESIMA CIEGA: seis de seis

**Acumulado: 204 releidas, de las cuales 180 a ciegas. Discrepancias: UNA**, el
395, cerrada por los dos lados.

| puesto | el par | que se pierde | tipo |
|---:|---|---|---|
| **590** | `five_whys_inversion_proporcional` contra `tecnica_cinco_porques` | **reunir a los involucrados** y **si la causa es tecnica o humana**; del otro lado, dos cosas que **viven en el bloque injertado**, ver abajo | de **lector** |
| **595** | `fase_accomplish` contra `fase_accomplish_experiencia_cliente` | **los tres escenarios** y **el 5% de las ganancias**; del otro lado, **recoger evidencia para usos futuros** | de **catalogo** |
| **596** | `acquisicion_viral_engineering` contra `herramientas_adquisicion_viral` | **los tipos de efecto de red** y **las recompensas por referir**; del otro lado, **animar a los primeros clientes a promoverlo** | de **catalogo** |
| **601** | `cierre_segun_complejidad_venta` contra `ineficacia_cierre_ventas_grandes` | **el permiso para la venta pequena**, **revisar el proceso completo** y **capacitar diferenciando**; del otro lado, **auditar por observacion** y **comparar tasas**. **La clasificacion esta en los dos** | de **catalogo** |
| **602** | `ficcion_especulativa_como_metodo` contra `historia_del_futuro_escenarios_especulativos` | **los principios de diseno**; del otro lado **TRES y no una** | de **lector** |
| **605** | `analisis_disrupciones_mercado` contra `evaluacion_industria_cliente` | **la voz del cliente cara a cara** y **los usuarios lideres**; del otro lado **TRES y no una** | de **catalogo** |

#### 595 y el tratamiento de Coleman: no son ocho fases con dos programas

**El encargo pide reformular el tratamiento y medir cuantas fases tienen doble
casa. Medido, y la respuesta es peor de lo que decia el marco anterior.**

**Criterio: se cuenta un nodo en una fase si la nombra en su IDENTIFICADOR o en su
TITULO.** Los dos nodos indice se cuentan aparte, porque pertenecen a las ocho.

| fase | nodos que la nombran | pares internos leidos | tiene A interna |
|---|---:|---|:---:|
| **ASSESS** | **4** | 224 B, **373 A** | **SI** |
| **ADMIT** | **2** | **421 A** | **SI** |
| AFFIRM | **1** | sin pares | no |
| **ACTIVATE** | **3** | **183 A** | **SI** |
| **ACCLIMATE** | **3** | 253 B, 196 B, **447 A** | **SI** |
| **ACCOMPLISH** | **2** | **595 A** | **SI** |
| **ADOPT** | **2** | 965 D | no |
| ADVOCATE | **1** | sin pares | no |

**Mas los DOS INDICES**, `ocho_fases_experiencia_cliente` y
`fases_de_retencion_de_clientes`, **que son gemelos entre si** (A del puesto 326).

> **LA REFORMULACION, con la cifra: SEIS de las OCHO fases tienen DOBLE CASA, y
> CINCO de esas seis ya tienen la repeticion PROBADA con una A interna.** Solo
> AFFIRM y ADVOCATE tienen un nodo cada una, y ADOPT tiene dos que no repiten
> (965 D).
>
> **No son ocho fases con dos programas encima.** Son **veinte nodos para ocho
> fases**: dieciocho de fase mas dos indices que tambien repiten entre si. **La
> mesa no tiene que decidir entre dos programas: tiene que decidir fase por fase**,
> y en cinco de ellas la decision ya esta forzada por una A.

**Y una nota que la tabla deja a la vista**: dos nodos mas llegan a ACCLIMATE **por
contenido y no por nombre**, `gamificacion_onboarding_visual` y
`visualizacion_progreso_onboarding`, gemelos entre si por el puesto **571**. **Si
se cuentan, ACCLIMATE tiene CINCO** y es la fase mas poblada del libro.

**LAS PERDIDAS DEL 595, verificadas**: `fase_accomplish_experiencia_cliente` es el
unico que **clasifica en los tres escenarios** y el unico que **reserva el 5% de
las ganancias**; `fase_accomplish` es el unico que manda **recoger evidencia,
testimonios y datos, del resultado logrado para usos futuros**. **Las tres se
verifican enteras.**

#### 590: dos de las perdidas viven en el bloque injertado, y eso cambia su fecha

**HALLAZGO DE ANATOMIA**: `five_whys_inversion_proporcional` declara **fuente
doble**, *The Lean Startup* y **SPIN Selling**, y sus **nueve pasos** se parten en
el metodo general (1 a 5) y **un bloque de ventas (6 a 9)**. Es la **SEXTA costura
entre libros** del ejercicio y **la primera cuyo segundo libro es Rackham**.

> **PRECISION DECLARADA, por el banco 9.11**: las dos perdidas que el encargo pone
> de este lado, **revisar grabaciones y patrones** y **medir tras el cambio
> estructural**, estan **las dos en los pasos 7 y 9**, o sea **dentro del bloque
> injertado**. **No las pierde esta fusion: su destino lo decide la decision de
> fuente**, que va antes. **Sexto ejemplar de la figura del reparto por bloques.**

**Las dos del otro lado se verifican enteras y son de metodo puro**: **reunir a
todas las personas involucradas** en el descubrimiento, el diagnostico y la
reparacion, y **identificar en cada nivel si la causa es tecnica o humana**.

#### 601: la clasificacion esta en los dos, y el permiso no estaba listado

**CORRECCION DECLARADA.** El encargo listaba *clasificar por valor y relacion* como
exclusivo de `cierre_segun_complejidad_venta`. **Los dos clasifican**: el paso 1 de
uno y el paso 1 del otro, con palabras distintas y el mismo corte.

| lo exclusivo de `cierre_segun_complejidad_venta` | |
|---|---|
| **el PERMISO para la venta pequena**: *aplicar tecnicas de cierre tradicionales sin restriccion* | **no estaba listado**, y es el unico sitio del racimo donde el cierre duro queda **autorizado** en vez de solo desaconsejado |
| revisar el proceso de venta completo y no solo el cierre | no estaba listado |
| capacitar al equipo diferenciando por tipo de venta | ya listado |

**Y las dos del otro lado se verifican, y son lo mas valioso del par**: **auditar
el uso de tecnicas de cierre observando llamadas reales** y **comparar tasas de
exito entre vendedores que usan muchas y pocas**. **Es la unica verificacion
EMPIRICA de todo el racimo del cierre**: los demas miembros afirman la tesis, este
dice como comprobarla en la propia empresa.

#### 602 y 605: dos listas de perdidas cortas, y las dos del mismo lado

**CORRECCION DECLARADA en los dos casos.**

| puesto | lo listado | lo que falta, verificado |
|---:|---|---|
| **602** | *compartir con el equipo antes de requisitos* | **el horizonte de 10 a 15 anos**, que es la unica cifra del par; y **los tres tipos de actor** que hay que meter en la historia, usuarios, empresas y reguladores |
| **605** | *evaluar el futuro de cada actor* | **los impulsores de rentabilidad de la industria y como estan cambiando**; y **definir escenarios futuros** para detectar arenas |

> **En los dos casos el lado corto de la lista era el mismo lado**, el del nodo mas
> largo. **Buscar en el grafo antes de clasificar sirve para las perdidas que se
> caen; releer el par entero sirve para las que faltan.** Son dos disciplinas
> distintas y hacen falta las dos.

#### 596: verificado entero

**Las tres perdidas se verifican.** `acquisicion_viral_engineering` es el unico que
manda **identificar QUE TIPO de efecto de red aplica**, boca a boca, compartir o
red directa, y el unico que propone **recompensas por referir**;
`herramientas_adquisicion_viral` es el unico que manda **animar activamente a los
primeros clientes a promoverlo**, que es pedir en vez de incentivar.

### TANDA R35, TRIGESIMOPRIMERA CIEGA: seis de seis

**Acumulado: 210 releidas, de las cuales 186 a ciegas. Discrepancias: UNA**, el
395, cerrada por los dos lados.

> **PRECEDENTE DE PARADA, y se anota aqui para que quede.** Una primera version de
> esta tanda se encargo con seis puestos que **no eran los que el encargo
> describia**: dos estaban mal caracterizados y **cuatro de los seis eran D**,
> cuando las seis tandas anteriores fueron **A pura**. **La tanda se paro sin
> escribir nada y se trajo la medicion.** Queda como precedente: **cuando los
> puestos no calzan con lo que el encargo dice de ellos, se para antes de
> redactar, no despues.**

**En esta tanda las perdidas NO vienen dictadas: se derivaron leyendo los doce
nodos y verificando contra el grafo.**

| puesto | el par | que se pierde |
|---:|---|---|
| **609** | `channels_hypothesis_physical` contra `seleccion_canal_distribucion` | **casi nada, y ese es el hallazgo**: ver abajo |
| **611** | `customer_discovery` contra `customer_discovery_introduccion` | **las cuatro preguntas clave** y **no delegues**; del otro lado, **construir el producto minimo** y **confirmar que compraria** |
| **614** | `alineacion_cadena_estrategia_negocio` contra `definicion_alineacion_cadena_suministro` | **las seis preguntas de Chopra y Meindl**, **el quinto control** y la coherencia con la propuesta de valor; del otro lado, **mapear la cadena entera** y **nombrar los roles** |
| **616** | `gestion_de_portafolio_gates_go_kill` contra `gestion_portafolio_formal` | **los seis criterios** y **matar en firme en vez de estrangular**; del otro lado, **las cubetas estrategicas**, la cadencia y el ranking hasta el limite |
| **627** | `definir_meta_de_traccion` contra `traction_goal` | **el filtro de actividades** contra la meta; del otro lado, **los subobjetivos con fecha en el calendario** y la reevaluacion por fase |
| **630** | `creacion_data_warehouse` contra `data_warehouse_como_fundamento` | **automatizar la captura** y **empezar pequeno**; del otro lado, **la cadencia de refresco** y **la regla de prioridad** |

**NINGUNO de los doce nodos es costura confirmada**, asi que en esta tanda no hay
acto del cierre transitivo que citar. **Se comprobo antes de escribirlo.**

#### 614: SEGUNDO EJEMPLAR de la arista que existe y aun asi duplica

**Con el 570, ya son dos.** Arista **en los dos sentidos**, verificada resolviendo
a nodo vivo, **y el par repite igual.**

> **Lo comun es la tesis entera**: identificar el rol propio dentro de la cadena,
> decidir si se compite por eficiencia o por capacidad de respuesta, y alinear las
> decisiones de produccion, inventario, ubicacion y transporte con esa eleccion.
>
> **Y aqui la perdida tiene una pieza que hay que mirar dos veces**:
> `alineacion_cadena_estrategia_negocio` habla de **CINCO controles** e incluye la
> **INFORMACION**; `definicion_alineacion_cadena_suministro` lista solo **CUATRO**
> y la deja fuera. **Una fusion hacia el segundo pierde un control entero**, no un
> matiz.
>
> **Lo demas de ese lado**: las **seis preguntas de Chopra y Meindl** sobre el
> mercado, con sus autores nombrados, y validar que la estrategia sea coherente
> con la propuesta de valor. **Del otro lado**: mapear todas las empresas y
> actividades de la cadena, y nombrar los roles posibles, proveedor, fabricante,
> distribuidor.

**LA MITAD DE LA REGLA QUEDA CON DOS EJEMPLARES.** El banco 9.5.0 registro que
**la arista no exculpa** y que la parafrasis abolida solo conservaba la mitad que
acusa. **Van dos casos donde la arista esta puesta, en los dos sentidos, y el
contenido esta duplicado de todos modos.** Ya no es una rareza de un par.

#### 616: segundo par interno de la MESA UNIDA, y NO estan enlazados

**CORRECCION DECLARADA.** El encargo dice que el grafo los enlaza. **Verificado:
NO hay arista entre ellos, en ninguno de los dos sentidos.** La mesa unida tiene
doce aristas internas y **ninguna es esta**.

> **Con el 574, van dos pares internos de la mesa releidos y los dos sostienen A.**
> Lo comun es el embudo que descarta lo debil, las puertas con criterios visibles
> y la revision del conjunto.
>
> **Lo propio de `gestion_de_portafolio_gates_go_kill`**: los **SEIS CRITERIOS**
> nombrados, estrategico, ventaja competitiva, atractivo de mercado,
> apalancamiento y factibilidad; y **matar en firme en vez de reducir recursos
> gradualmente**, que es la unica regla del grupo contra los proyectos zombis.
> **Lo propio de `gestion_portafolio_formal`**: las **cubetas estrategicas**, la
> cadencia de dos a cuatro revisiones al ano, y el ranking dentro de cada cubeta
> hasta agotar el limite.

#### 609: es contra el GENERAL, y el hijo no especializa nada

**CORRECCION DECLARADA.** El encargo lo da como par entre dos hijos. **Es un hijo
contra el general**: `seleccion_canal_distribucion` es el nodo general del racimo,
segun su propia ficha de la seccion 10.

**LA EVIDENCIA SEPARADA, que es lo que la mesa necesita y aqui esta medida:**

| tipo de par | cuantos | puestos |
|---|---:|---|
| **contra el GENERAL** | **CUATRO, todos A** | 165, 400, 537, **609** |
| **entre HIJOS** | **CUATRO, tres leidos y los tres A** | 214, 762, 945, y el **1488 pendiente** |

> **La mesa tiene que ver las dos columnas juntas.** Que el general repita con sus
> hijos sostiene la lectura madre-hijas; **que los hijos repitan ENTRE ELLOS la
> debilita**, porque dos especializaciones distintas no deberian decir lo mismo.

**Y EL HALLAZGO DEL PAR, que apunta en la misma direccion**: leidos paso por paso,
`channels_hypothesis_physical` y el general **dicen lo mismo cinco veces**. Los
habitos de compra, el costo del canal, la complejidad y el precio, un solo canal, y
el recalculo de ingresos: **estan en los dos y en el mismo orden.**

> **El hijo FISICO no tiene ni un paso que sea fisico.** Es el general con otro
> titulo. **Lo unico suyo** es que fija el limite del canal unico **hasta completar
> la validacion**, donde el general lo fija **durante el descubrimiento**: dos
> etapas distintas. **Y lo unico del general** son los tres componentes del costo
> de canal, distribucion, promocion y devoluciones.
>
> **Comparelo con el hijo DIGITAL** (puesto 537), que si trajo algo propio, probar
> varios canales con presupuesto parecido para comparar el costo por cliente.
> **Las especializaciones de esta familia no son uniformes: una especializa y la
> otra solo se llama distinto.**

#### 611: y la familia queda MEDIDA ENTERA, la primera del ejercicio

**CORRECCION DECLARADA**: el encargo la llama sub-puro. **No lo es: es MEZCLADA.**
Y lo que si es, es mucho mas util.

| medida | resultado |
|---|---:|
| miembros | **5** |
| pares posibles | **10** |
| **en la cola** | **10** |
| **leidos** | **10** |
| clases | **6 A, 3 D, 1 B** |
| aristas internas | **1** |

> **ES LA PRIMERA FAMILIA DEL EJERCICIO CON COBERTURA COMPLETA: diez de diez.** No
> hay ni un par sin encolar ni uno sin leer. **De todas las nominas medidas hasta
> aqui, de esta se sabe todo.**
>
> **Y la forma que se ve con todo leido**: `customer_discovery` es el centro con
> **cuatro A**; los tres sanos son **415**, **424** y **1255**, y los tres
> enfrentan a un nodo de PROCESO con uno de FASES. **La familia repite en el eje
> del proceso y jerarquiza en el de las fases**, y eso solo se puede afirmar
> porque estan los diez.

**Y arrastra DOS candidatos fuera de la nomina**: `customer_discovery_get_out_of_building`
(849) y `desarrollo_de_clientes_customer_development` (1052), **los dos por A con
`customer_development_modelo`**.

**Las perdidas del 611**: de `customer_discovery_introduccion` se pierden **las
cuatro preguntas clave como lista** y **no delegues esta tarea en otra persona**;
esa segunda **sobrevive** en `customer_discovery_get_out_of_building`, como quedo
registrado en el puesto 510. De `customer_discovery` se pierden **construir un
producto minimo para probar la solucion** y **confirmar que el problema importa lo
suficiente como para comprar**.

#### 627 y 630: dos pares de nodo repetido con la misma forma

**Los dos son el mismo caso: dos nodos del mismo libro para el mismo concepto,
donde uno anade el CUANDO y el otro anade el FILTRO.**

| puesto | lo que anade uno | lo que anade el otro |
|---:|---|---|
| **627** | `traction_goal`: **subobjetivos con fecha en el calendario**, junto a los hitos de producto, y **reevaluar al cambiar de fase** | `definir_meta_de_traccion`: **evaluar cada actividad de mercadeo** contra la meta y **descartar las de resultado marginal** |
| **630** | `data_warehouse_como_fundamento`: la **cadencia de refresco**, diaria u horaria, y **priorizarlo ANTES de construir modulos analiticos** | `creacion_data_warehouse`: **automatizar la captura** para no teclear a mano, y **empezar por una version pequena** antes de ampliarla |

> **En los dos casos la fusion es asimetrica y conviene decirlo**: el superviviente
> tiene que quedarse con **el calendario y el filtro** en un caso, y con **la
> prioridad y el arranque pequeno** en el otro. **Quedarse con uno solo de los dos
> nodos pierde la mitad util en las dos parejas.**

### TANDA R36, TRIGESIMOSEGUNDA CIEGA: seis de seis

**Acumulado: 216 releidas, de las cuales 192 a ciegas. Discrepancias: UNA**, el
395, cerrada por los dos lados.

**Las perdidas se derivaron leyendo los doce nodos y BUSCANDO CADA UNA en el grafo
antes de listarla.** Tres se cayeron por esa busqueda.

| puesto | el par | que se pierde de verdad |
|---:|---|---|
| **635** | `customer_development_modelo` contra `customer_discovery` | **el canal y el precio** en la respuesta recogida; del otro lado, **probar la percepcion del problema antes de mostrar nada** |
| **639** | `diseno_experimentos_pass_fail` contra `realizar_pruebas_pasa_no_pasa` | las **cifras** y los **artefactos**; del otro lado, **el costo de adquisicion contra el precio** y **la clasificacion de reacciones** |
| **641** | `fase_diseno_prototipado_modelos` contra `prototipado_modelos_negocio` | **no descartar porque un experto diga que no**; del otro lado, **la escalera de fidelidad**, **la manipulacion de escenarios** y **los tres prototipos minimos** |
| **643** | `split_testing` contra `test_ab_precio` | **el reparto equitativo del trafico** y **el 95% de significancia**; del otro lado, **las rondas multiples** |
| **651** | `cuatro_capacidades_mercado` contra `cuatro_categorias_desempeno_cadena_suministro` | **invertir en la fortaleza y no en la debilidad**; del otro lado, **la cadencia diaria del dato** |
| **653** | `ciclo_de_conversion_de_efectivo` contra `dso_dpo_gestion_capital_trabajo` | **la formula del ciclo** y **el capital de trabajo requerido**; del otro lado, **las causas de un DSO alto** |

#### 643: par INTERNO del acto de A/B, el mas caro del inventario

**Los dos nodos son miembros del ACTO 2 del cierre transitivo**, y por la nota de
la seccion 54.7 se cita entero:

| el acto 2 | |
|---|---|
| **tamano** | **SEIS nodos** |
| **costuras dentro** | **TRES**: `ab_testing_optimizacion`, `optimizacion_embudo_get_customers`, `split_testing_experimentos_ab` |
| **sanos dentro** | `split_testing`, `test_ab_precio`, `funnel_get_customers_optimizacion` |
| **pares A que lo sostienen** | 277, 374, 452, **643**, 1061 |
| **lo que cuesta** | **TRES destejidos** y despues **una decision sobre seis nodos**. Es la **tercera cirugia del orden de la pasada**, y la unica que son tres |

> **Este par es entre los dos SANOS del acto**, y aun asi repite. **Que dos nodos
> limpios de un acto digan lo mismo confirma que el problema del acto no es solo
> el destejido: es que sobran nodos aunque se destejan todos.**

**LAS PERDIDAS, verificadas**: de `split_testing` se pierden **dividir el trafico
equitativamente entre control y desafiante** y **exigir significancia estadistica
superior al 95% antes de concluir**, que es el unico umbral estadistico de toda la
familia. De `test_ab_precio` se pierde **ejecutar rondas multiples para afinar el
precio optimo**, que es lo unico que trata la prueba como un barrido y no como una
comparacion de dos.

#### 641: DOS CASAS PARA LA MISMA FASE, ahora entre las dos casas

**Es la figura que resolvio la discrepancia del 395**, y aqui aparece **entre las
dos casas directamente** en vez de entre una casa y un tercero.

> **Los dos desarrollan la misma fase de diseno del modelo de negocio** y coinciden
> en el nucleo: generar varias variantes, prototiparlas con el lienzo y quedarse
> con la de mas potencial tras explorar.

**LAS PERDIDAS, y la busqueda cambio la lista.** De `fase_diseno_prototipado_modelos`
se pierde **una sola cosa y no aparece en ningun otro nodo vivo**: **no descartar
ideas solo porque un experto diga que no funcionara.** Su otra pieza, la narrativa
por modelo con respuesta externa, **si tiene equivalente** en el otro lado, la
prueba de campo con clientes reales.

De `prototipado_modelos_negocio` se pierden **tres**, y las tres son suyas:

| lo exclusivo | |
|---|---|
| **la escalera de fidelidad** | boceto rapido, luego lienzo elaborado, luego caso de negocio en hoja de calculo. **Ningun otro nodo de la zona escalona el prototipo** |
| **la manipulacion de escenarios** | quitar un segmento, quitar un recurso costoso, cambiar una pieza y ver que pasa |
| **los TRES prototipos minimos** | construir al menos tres distintos antes de elegir, **evitando apegarse emocionalmente**. Verificado: la cifra no aparece en ningun otro nodo |

#### 639: tercer par de la ESTRELLA de pass/fail

**El centro contra su cuarto miembro.** Con el 467 y el 511, **las tres A de la
estrella tocan al mismo nodo**, `diseno_experimentos_pass_fail`.

> **Y la forma se sostiene**: el unico par periferico leido, el **636**, sigue
> sano. **Tres radios en A y el unico par entre radios en D**: es la estrella del
> banco 9.23 con la segunda cuenta hecha.

**LAS PERDIDAS, y una se cayo al buscarla.** De `realizar_pruebas_pasa_no_pasa` se
pierden **dos y las dos son unicas en el grafo**: **comparar cuanto cuesta
conseguir un cliente contra el precio del producto**, y **clasificar las reacciones
en categorias**, los que aman el producto, los que piden funciones nuevas, los
indiferentes. **Ninguna de las dos aparece en ningun otro nodo vivo.**

De `diseno_experimentos_pass_fail` se pierden **las cifras y los artefactos**:
nueve de treinta pedidos, diez a treinta prospectos, y las paginas de aterrizaje,
presentaciones y maquetas. **Pero NO se pierde la regla del maximo local**: vive en
`global_vs_local_maximum` y en `disenar_tests_pass_fail`, verificado.

#### 651: la misma taxonomia con dos nombres, y el racimo ya la tenia contada

**Las cuatro capacidades y las cuatro categorias son LAS MISMAS CUATRO**: servicio
al cliente, eficiencia interna, flexibilidad de demanda y desarrollo de producto.
Un nodo las llama capacidades y el otro categorias de desempeno.

> **NO es un miembro nuevo.** Medido antes de escribirlo: el racimo de los
> **CUADRANTES DE MERCADO**, el numero 8 de la tabla viva, ya cuenta a
> `cuatro_categorias_desempeno_cadena_suministro` entre sus **seis** miembros.
> **Siete pares leidos de quince posibles y los SIETE en A**, cero candidatos
> fuera. **Este par es uno de esos siete y la ficha estaba al dia.**

**LAS PERDIDAS**: de `cuatro_capacidades_mercado` se pierde **invertir en reforzar
la fortaleza en vez de corregir debilidades menores**, verificado como unico en el
grafo, y es la unica regla de asignacion de toda la familia. De
`cuatro_categorias_desempeno_cadena_suministro` se pierde **recolectar los datos de
forma diaria o continua**, que es la unica cadencia que alguien da.

#### 653: el racimo declarado en el 203 no se confirma, y el gemelo estaba en otro sitio

**El puesto 203 declaro una figura: un RACIMO NUEVO de tres nodos del capital de
trabajo**, el conjunto `dso_dpo_gestion_capital_trabajo` mas uno por cada mitad,
`gestion_dso` y `gestion_cuentas_por_pagar_dpo`.

**Remedido hoy, esa candidatura no se confirma:**

| par | puesto | clase |
|---|---:|:---:|
| el conjunto contra la mitad del cobro | 191 | **D** |
| el conjunto contra la mitad del pago | 203 | **C** |
| **el conjunto contra el CICLO** | **653** | **A** |

> **Los tres nodos de la figura del 203 no repiten entre si: el conjunto jerarquiza
> con sus dos mitades.** Y la unica A de `dso_dpo_gestion_capital_trabajo`, en
> cinco lecturas, **es con `ciclo_de_conversion_de_efectivo`**, que no estaba en
> aquella figura.
>
> **La lectura confirma la remedicion**: lo que parecia un racimo de tres por
> cercania de tema **era una jerarquia de tres**, y la repeticion real estaba con
> el nodo del ciclo. **Los dos forman una PAREJA CERRADA**: ninguno de los dos
> tiene otra A.

**LAS PERDIDAS, verificadas como unicas en el grafo**: de
`ciclo_de_conversion_de_efectivo` se pierden **la formula del ciclo**, dias de
cobro mas dias de inventario menos dias de pago, y **multiplicarla por las ventas
diarias para estimar el capital de trabajo requerido**. De
`dso_dpo_gestion_capital_trabajo` se pierden **las CAUSAS de un dia de cobro
elevado**: quejas de clientes, terminos de venta laxos y facturacion lenta.

#### 635: la busqueda tumbo una perdida y precisó otra

**CORRECCION DE MI PROPIA LISTA.** Antes de escribir, busque las dos piezas de
`customer_development_modelo` en el grafo:

| pieza | verificacion | veredicto |
|---|---|---|
| **combinar con desarrollo agil en paralelo** | vive en `customer_development_agile_pairing`, `etapa_development` y dos mas | **NO ES PERDIDA** |
| **recoger respuesta sobre el CANAL y el PRECIO**, no solo sobre el producto | ningun otro nodo de la zona pide las tres dimensiones juntas | **perdida real** |

**Y del otro lado**: `customer_discovery` es el unico de la zona que manda **probar
como percibe el cliente el problema ANTES de mostrarle nada del producto**. La
frase equivalente solo aparece en `desarrollo_presentacion_problema`, que es un
nodo de reunion y no de etapa: **la instruccion sobrevive, pero cambia de sitio y
de momento**, y eso conviene decirlo en vez de darla por salvada.

### TANDA R37, TRIGESIMOTERCERA CIEGA: seis de seis

**Acumulado: 222 releidas, de las cuales 198 a ciegas. Discrepancias: UNA**, el
395, cerrada por los dos lados.

**Las perdidas se derivaron leyendo los doce nodos y buscando cada una en el
grafo.** Y la tanda deja **una correccion mia** que no es de perdidas sino de una
cifra publicada.

| puesto | el par | que se pierde |
|---:|---|---|
| **655** | `filosofia_customer_validation` contra `filosofia_validacion_clientes` | **la version del producto y los materiales** y **las tres preguntas**; del otro lado, **no montar equipo de ventas todavia** y **que las reglas corporativas no aplican** |
| **672** | `equipo_multifuncional` contra `equipo_multifuncional_real` | **incluir a cada area desde el inicio** y **evitar el modelo de relevos**; del otro lado, **liberar tiempo real** y **premiar por desempeno del equipo** |
| **673** | `errores_comunes_asignacion_roles` contra `seleccion_ceo_fundador` | **no poner cofundadores en la junta por lealtad** y **cautela con los titulos tempranos**; del otro lado, **las brechas propias y los mentores** |
| **674** | `fase_mobilizacion_equipo_multifuncional` contra `fase_mobilizar_modelo_negocio` | **educar a quien decide con historias y no con teoria**; del otro lado, **el ejercicio de matar o entusiasmar** y **el respaldo visible** |
| **686** | `hipotesis_tipo_mercado` contra `tipo_de_mercado_estrategia_competitiva` | **el costo de entrada** y **la base de competencia**; del otro lado, **los umbrales de cuota** y **actualizar el lienzo** |
| **692** | `alineacion_etica_ia_negocio` contra `principio_humano_en_el_loop` | **avisar al cliente** y **detectar sesgos**; del otro lado, **reconocer la invencion** |

#### 674: la familia del diseno de modelo de negocio REPITE POR FASE

**Con el 641, que mostro lo mismo en la fase de DISENO, este puesto lo muestra en
la fase de MOVILIZACION.** Medido sobre las cinco fases del proceso de
Osterwalder:

| fase | nodos que la nombran | pares internos | tiene A |
|---|---:|---|:---:|
| **MOVILIZAR** | **2** | **674 A** | **SI** |
| COMPRENDER | 1 | sin pares | no |
| **DISENAR** | **3** mas el indice | **641 A**, **507 A**, 572 D | **SI** |
| IMPLEMENTAR | 1 | sin pares | no |
| GESTIONAR | 1 | sin pares | no |

> **DOS de las CINCO fases tienen doble casa, y las dos con la repeticion probada.**
> **Queda registrada como CANDIDATA A TRATAMIENTO DE SERIE**, como el de Coleman,
> **y sin adjudicar**. Y con la comparacion honesta al lado: **Coleman tiene seis
> de ocho fases con doble casa; este tiene dos de cinco.** Es la misma figura, mas
> chica.

**Y LA FASE DE DISENO RESULTA SER UNA ESTRELLA, medida al pasar:**

| cuenta | resultado |
|---|---|
| pares con el centro `fase_diseno_prototipado_modelos` | **DOS y los dos A**: 641 y 507 |
| par entre perifericos | **UNO leido y SANO**: 572 |
| **cobertura** | **3 de 3** |

> **Es la CUARTA estrella del ejercicio**, y la tercera con cobertura completa. Y
> ademas el nodo indice de las cinco fases, `proceso_diseno_modelo_negocio_5_fases`,
> sale **sano contra los tres** (633, 395): **el indice no repite con sus fases**,
> igual que en Coleman.

#### 673: par del acto de la SELECCION DE CEO

**Los dos nodos son miembros del ACTO 4 del cierre transitivo**, citado entero como
manda la nota de la seccion 54.7:

| el acto 4 | |
|---|---|
| **tamano** | **TRES nodos** |
| **la costura** | **`seleccion_ceo_fundador`**, doce pasos y **fuente doble** |
| **los sanos** | `errores_comunes_asignacion_roles` y `asignacion_de_titulos_ejecutivos` |
| **lo que cuesta** | **un destejido** y despues **una decision sobre tres nodos** |

**LAS PERDIDAS, verificadas.** De `errores_comunes_asignacion_roles` se pierden dos
que no estan en el nodo grande: **no colocar automaticamente a los cofundadores en
la junta directiva solo por lealtad**, y **ser cauteloso al asignar titulos de alto
nivel temprano pensando en el crecimiento futuro**. De `seleccion_ceo_fundador` se
pierden **identificar las brechas propias de habilidad** y **buscar mentores con
experiencia real fundando**, que estan en su primer bloque. **Y como su destejido
va antes que la fusion, el reparto de esas dos se decide despues de la cirugia**,
no ahora.

#### 692: par interno del racimo de la IA, y suma cohesion

**Verificado contra la nomina de ocho de la seccion 11: los dos son miembros.**
`alineacion_etica_ia_negocio` y `principio_humano_en_el_loop`.

> **Es un par INTERNO de los que suman cohesion, no uno de los cuatro cruzadores.**
> **Las condiciones vivas no se tocan**: siguen siendo el 1211, el 1239, el 1339 y
> el 1451, **y de esas van tres en D**.
>
> **Lo que este par anade** es que la mitad humana del racimo esta bien trabada por
> dentro: con el 166 y el 792, **`principio_humano_en_el_loop` y
> `human_in_the_loop_ia` repiten con la alineacion etica y entre si.** La cuenta
> interna queda en **nueve pares leidos, seis A y tres D**.

**LAS PERDIDAS**: de `alineacion_etica_ia_negocio` se pierden **avisar con
transparencia al cliente cuando habla con una maquina**, que no aparece en ningun
otro nodo del racimo, y **crear una forma simple de detectar y corregir sesgos**.
De `principio_humano_en_el_loop` se pierde **aprender a reconocer cuando la maquina
inventa**, citas que no existen y datos que no se pueden comprobar.

#### 655: y aqui va una CORRECCION MIA de una cifra publicada

**El par es A y sigue siendo A.** `filosofia_validacion_clientes` es la postura y
`filosofia_customer_validation` es la misma etapa contada con pasos: los dos dicen
que se sale a pedir pedidos reales y no opiniones, y que eso es la prueba.

> **CORRECCION DECLARADA, por el banco 9.10.** En la seccion 56.4 escribi que
> `filosofia_customer_validation` llevaba **ocho lecturas, dos A y seis sanas**, y
> que el reparto era limpio porque **las dos A eran contra nodos que abren la
> etapa**.
>
> **Recomputado del archivo: son DIECIOCHO lecturas, CINCO A y TRECE D.** Conte
> solo las que habia leido yo en este tramo y las di por el total. **Y con las
> cinco A delante, el reparto limpio que afirme NO se sostiene**: repite tambien
> con `customer_validation` (247) y con `customer_validation_sell_phase` (245), que
> no son nodos de apertura sino la etapa y su fase de venta.
>
> **Lo que si se sostiene, y ahora medido**: es el nodo con mas lecturas del
> archivo y **su componente de gemelos es de SIETE nodos**, con 21 pares posibles,
> 15 en la cola, 14 leidos y **ocho de ellos en A**. **La mesa de la apertura de
> Customer Validation es mucho mas grande que el par que la levanto.**

#### 672 y 686: dos pares que no mueven nada, y conviene decirlo

**El 672** confirma la nomina del racimo de los equipos que cruzan areas:
`equipo_multifuncional_real` es el centro con dos A, la 476 y esta. **Lo perdido**:
de `equipo_multifuncional`, incluir a cada area **desde el inicio** y **evitar el
modelo de pasar el proyecto de area en area**; del otro, **liberar tiempo real** de
las tareas habituales y **premiar por desempeno del equipo y no individual**.

**El 686** es uno de los tres pares del **PURO DE TRES del tipo de mercado**, y
sostenerlo lo mantiene puro. **Lo perdido**: de `hipotesis_tipo_mercado`, el
**costo de entrada** con la regla de 1,7 o 3 veces el presupuesto del lider, y la
**base de competencia**; del otro, los **umbrales de cuota** del 74% y el 26%, y
**actualizar el lienzo** con la hipotesis.

> **La cobertura de ese puro, como manda el 9.26: TRES de TRES.** Es una forma sin
> reserva.


### TANDA R38, TRIGESIMOCUARTA CIEGA: seis de seis

**Acumulado: 228 releidas, de las cuales 204 a ciegas. Discrepancias: UNA**, el
395, cerrada por los dos lados.

**Las perdidas se derivaron leyendo los doce nodos y buscando cada una en el
grafo**, y **dos de las nueve candidatas se cayeron porque existen en otro nodo
vivo**: se dicen abajo con nombre. **Y la tanda trae DOS CHOQUES DE MEDICION**
contra cifras publicadas en la tabla viva.

| puesto | el par | que se pierde de verdad |
|---:|---|---|
| **704** | `cuatro_capacidades_mercado` contra `marco_analisis_mercado_cadena_suministro` | **reforzar la fortaleza en vez de corregir debilidades menores** y las **metricas por capacidad**; del otro lado, **quienes participan en el mercado** y **el tipo de mercado a dos anos** |
| **709** | `customer_validation` contra `introduccion_validacion_clientes` | **la razon de dos a uno** en ventas y marketing; del otro lado, **posicionar el producto y la empresa** |
| **711** | `escenarios_futuros` contra `future_scenarios_planning` | **la probabilidad pequena a los escenarios alternativos**; del otro lado, **el bloque entero de IA**, nueve pasos |
| **712** | `formalizar_junta_asesora` contra `identificar_junta_asesores` | **el asesor tipo CEO**, la **compensacion con vesting** y **documentar la operacion**; del otro lado, **el almuerzo informal** |
| **713** | `community_building_estrategia` contra `construccion_de_comunidad_como_canal_traccion` | los **espacios de meta discusion** y las **guias de calidad**; del otro lado, la **pregunta de entrada** y la **conexion cruzada entre miembros** |
| **723** | `ciclo_construir_medir_aprender` contra `design_test_repeat` | **repetir el ciclo cada vez mas rapido**; del otro lado, **anclar el prototipo a la propuesta de valor** |

**LAS DOS QUE SE CAYERON AL BUSCARLAS**, y conviene decirlo porque el que no las
busca las escribe: de `introduccion_validacion_clientes`, *probar canales de venta
y distribucion* **no se pierde**, esta en `mapa_de_canal_de_ventas` y en otros
cinco nodos vivos; de `community_building_estrategia`, *delegar la moderacion con
karma o votacion* **tampoco**, esta entera en `gestion_calidad_comunidad_a_escala`.

#### 712: CUARTO ejemplar de arista en los dos sentidos que aun asi duplica, y cabecera de LA ESCALERA QUE NO SUBE

**Van cuatro**, con el 570, el 614 y el 635. **Y este trae algo que los otros tres
no tenian: es el par de cabecera de una escalera de las del 9.12.**

**LA MESA DE LA JUNTA ASESORA, remedida hoy contra el archivo:**

| medida | cifra |
|---|---:|
| nomina | **CUATRO** nodos |
| pares posibles | 6 |
| en la cola | 5 |
| **leidos** | **5** |
| **en A** | **4** (328, 367, 712, 976) |
| **en D** | **1**, el **1190** |
| pendientes en cola | **cero** |
| **nunca encolado** | **1**: `formalizar_junta_asesora` contra `identificar_consejo_asesores` |

**LA FAMILIA ES UN CUADRO DE DOS POR DOS**, y por eso se ve la escalera:

| | `identificar_junta_asesores` | `identificar_consejo_asesores` |
|---|---|---|
| **`formalizar_junta_asesora`** | **712 A** | **nunca encolado** |
| **`formalize_advisory_board`** | **976 A** | **1190 D** |

> **Las columnas son el mismo momento contado dos veces y las filas tambien**: el
> 328 empareja los dos *formalizar* y el 367 los dos *identificar*, **los dos en
> A**. O sea que **los cuatro nodos son dos nodos escritos cuatro veces**, y las
> celdas del cuadro son **el escalon**: identificar contra formalizar.
>
> **Tres de las cuatro celdas cruzadas estan leidas y NO dicen lo mismo**: dos en
> A y una en D. **Ese es exactamente el 9.12**: la escalera esta anunciada, el
> paso de identificar a formalizar existe como secuencia declarada en el propio
> paso 6 de `identificar_consejo_asesores`, **y aun asi tres de sus cuatro cruces
> duplican contenido en vez de continuarlo.**

**CHOQUE DE MEDICION NUMERO UNO, declarado por el 9.10.** La **tabla viva de los
puros** trae esta familia como su **numero 7**, *SUB-PURO, 4 leidos, 4 en A*.
**Ya no lo es.** El puesto **1190**, posterior a la fecha de corte de la tabla,
metio un **D** dentro de la nomina.

> **La familia de la junta asesora pasa de SUB-PURO a MEZCLADO**, por la misma
> regla que rompio al numero 3 con el 872. **Y su cobertura, como manda el 9.26:
> 5 de 6.** Con un solo par ausente, y ese par ausente es **una de las cuatro
> celdas del cruce**: si sale A, la escalera duplica en tres de cuatro y la
> excepcion es el 1190; si sale D, duplica en dos de cuatro y **la figura queda
> partida por la mitad.** Un par mueve la forma en las dos direcciones, tal cual
> lo dice el 9.26.

**LA ANOTACION QUE PIDE EL ENCARGO, en el registro de dependencias**: el **1190
depende de esta mesa**, y la mesa **no puede sentarse pensando que decide sobre un
sub-puro**. Decide sobre una familia **mezclada de cuatro nodos con un cruce sin
leer**, y con la escalera de cabecera puesta por el 712.

#### 711: el par del acto de `future_scenarios_planning`, y el acto es de DOS

**Citado como manda la nota de la seccion 54.7:**

| el acto | |
|---|---|
| **tamano** | **DOS** nodos: `escenarios_futuros` y `future_scenarios_planning` |
| **la costura** | ninguno de los dos: **el acto entero es este par** |
| **cobertura** | **1 de 1**, completa, **y aun asi es la forma minima** |
| **lo que cuesta** | **una decision de par**, de las 121 del retrato |

> **Y aqui la perdida NO es simetrica, ni de lejos.** `escenarios_futuros` tiene
> siete pasos de Cooper y `future_scenarios_planning` tiene **trece**, de los
> cuales **nueve son un bloque de IA entero**: que tareas se automatizarian con
> crecimiento lineal, que pasa si la capacidad se multiplica por cien, el plan de
> contingencia entre lineal y exponencial, la revision trimestral, y las senales
> de alerta regulatorias y tecnologicas.
>
> **Si la fusion elige mal el superviviente, se pierde la mitad del catalogo de
> escenarios de IA.** Queda dicho aqui para que la decision no se tome por
> antiguedad ni por nombre.

**Y una precision de nomina que evita un error futuro**: `future_scenarios_planning`
**NO es miembro del racimo de la supervision de la IA** de la seccion 11. Ese
racimo tiene ocho nombrados y este no esta entre ellos. **Un nodo con pasos de IA
no es un nodo del racimo de la IA**: el racimo se definio por la supervision, no
por la mencion.

#### 723: par interno del sub-puro de BUILD-MEASURE-LEARN, y el sub-puro CRECIO

**CHOQUE DE MEDICION NUMERO DOS, declarado por el 9.10.** El encargo lo cita como
**sub-puro de cinco miembros**, que es lo que dice la tabla viva en su numero 9.
**Medido hoy contra el archivo, son SIETE.**

| medida | tabla viva (vigente al 1157) | **medido al puesto 1400** |
|---|---:|---:|
| miembros | 5 | **7** |
| pares posibles | 10 | **21** |
| en la cola | no anotado | **8** |
| **leidos** | 5 | **7** |
| **en A** | 5 | **7** |
| estado | SUB-PURO | **SUB-PURO**, y por mas margen |

**LA NOMINA DE SIETE**: `build_measure_learn`, `ciclo_construir_medir_aprender`,
`ciclo_crear_medir_aprender`, `design_test_repeat`, `desarrollo_en_espiral`,
`startup_como_experimento_cientifico` y `testing_process_completo`. **Los pares:**
213, 376, 486, **723**, 796, 1182 y 1208, **los siete en A**.

> **La tabla no mintio: dijo su fecha de corte.** Los dos miembros que faltaban
> entraron **despues** del puesto 1157, por el **1182** y el **1208**, los dos
> levantados por el barrido de las A y no por el contador. **Esto es exactamente
> el patron de la nota del inventario: remedir cambio el tamano otra vez, y otra
> vez hacia arriba.** Van tres remediciones y **ninguna dejo la cifra igual.**

> **Su cobertura, como manda el 9.26: SIETE de VEINTIUNO.** Es el sub-puro **con
> mas miembros y con la reserva mas grande del inventario**: catorce pares
> posibles sin leer, de los cuales **trece no entraron nunca a la cola**. **Un
> solo sano lo tumba**, y por el 9.16 esto sigue siendo una promesa.
>
> **Y le queda UN pendiente en cola, el puesto 1449, que cae en el tramo que se
> lee ahora mismo.** Sale en esta pasada.

#### 704 y 709: dos pares que no mueven nomina, y por que

**El 704** es interno del racimo de **los cuadrantes de mercado**, el numero 8 de
la tabla viva, y los dos nodos ya estaban dentro de su acto de seis. **No lo
agranda: lo densifica.** **La perdida verificada** de `cuatro_capacidades_mercado`
es la unica linea del inventario que manda **invertir en la fortaleza en vez de
corregir la debilidad**, y no aparece en ningun otro nodo vivo.

**El 709** es interno del acto de **siete de la apertura de Customer Validation**,
la mesa que el 655 midio. **La perdida verificada** de
`introduccion_validacion_clientes` es **posicionar correctamente el producto y la
empresa**, que **no esta en ningun otro nodo del catalogo con esas palabras**; y
de `customer_validation`, **la razon de dos a uno** entre lo invertido en ventas y
marketing y lo que vuelve, que es **el unico umbral numerico de la etapa**.

> **Los dos van a bloques distintos**: el 704 al reparto de la mesa de los
> cuadrantes y el 709 al de la mesa de Customer Validation. **Ninguno de los dos
> se decide ahora**, por la regla del reparto por bloques del 9.11.

### TANDA R42: ocho puestos, SEIS COINCIDEN Y DOS DISCREPAN, y las dos discrepancias caen donde el reporte las habia marcado

**Relectura ciega del auditor, 17 ago 2026, sobre ocho puestos de la tanda 2.118 a
2.300:** 2.137, 2.166, 2.195, 2.215, 2.242, 2.261, 2.277 y 2.292.

| resultado | puestos | |
|---|---|---:|
| **coinciden** | 2.137, 2.166, 2.242, 2.261, 2.277, 2.292 | **6 de 8** |
| **discrepan** | **2.195 y 2.215** | **2 de 8** |

> **LO QUE ESTA TANDA MIDE NO ES LA TASA DE ACIERTO. ES SI EL MARCADO SIRVE.**
> El reporte consolidado de la tanda (seccion 73.7) marco **cinco puestos como los mas
> discutibles** de cuarenta. **Las dos discrepancias del auditor son dos de esos cinco**,
> y ninguna cayo fuera de la lista.

**Por que eso importa mas que el 6 de 8.** Una relectura ciega que discrepa en puestos
**no marcados** diria que el lector **no sabe donde esta flojo**, y entonces **ninguna de
sus cuarenta lecturas tendria mas credito que otra**. Aqui pasa lo contrario: **el lector
senalo por adelantado donde iba a fallar y fallo exactamente ahi.** El marcado de
discutibles **deja de ser una cortesia y pasa a ser un instrumento de triaje**: al
auditor le basta con leer los marcados para encontrar lo que se cae.

**Y hay una prediccion cumplida al pie de la letra.** La seccion 73.7 escribio sobre el
2.195: *si el auditor sostiene que una pregunta distinta merece nodo aunque se conteste
en una linea, este veredicto se voltea, **y con el el 2.215***. **Se voltearon los dos, y
en ese orden de dependencia.** El motivo real resulto ser distinto y mejor que el
previsto, y esta en la seccion 74.

> **REGLA DE USO QUE DEJA ESTA TANDA:** **toda tanda que se publique lleva su lista de
> discutibles marcados**, y **la relectura ciega empieza por ellos**. Si una discrepancia
> aparece **fuera** de la lista, eso **si** es una senal sobre el lector, y se anota como
> tal.

### LA REGLA DEL MARCADO, adoptada el 17 ago 2026

> **TODA TANDA QUE SE PUBLIQUE LLEVA SU LISTA DE DISCUTIBLES MARCADOS, Y LA RELECTURA
> CIEGA EMPIEZA POR ELLOS.**

**Los tres usos que tiene, y el tercero no es obvio:**

1. **TRIAJE.** Al auditor le basta con leer los marcados para encontrar lo que se cae.
   **En la R42, las dos discrepancias de ocho fueron dos de los cinco marcados.**
2. **MEDIDA DEL LECTOR.** Si una discrepancia aparece **fuera** de la lista, eso **si**
   es una senal sobre el lector: **no sabe donde esta flojo**, y entonces **ninguna de
   sus lecturas tiene mas credito que otra.** Mientras las discrepancias caigan dentro,
   el resto de la tanda se sostiene.
3. **EL MARCADO SE ESCRIBE ANTES DE SABER SI ACIERTA**, y por eso vale. Un marcado puesto
   despues de la relectura no mide nada.

**Y la prueba de que no es autocomplacencia: el marcado tambien predice el arrastre.**
La seccion 73.7 escribio sobre el 2.195 *si el auditor sostiene X, este veredicto se
voltea, y con el el 2.215*. **Se voltearon los dos, y en ese orden de dependencia.** El
barrido de direccion de la seccion 76 anadio un tercero, el **2.338**, y tambien estaba
marcado.

### TANDA R43: cuatro puestos, TRES COINCIDEN Y UNA DISCREPA, y la relectura empezo por los marcados

**18 ago 2026.** La R43 aplico por primera vez **la regla del marcado como protocolo**:
el auditor releyo **solo los discutibles** de la seccion 77.6, **2.335, 2.368, 2.310 y
2.371**.

| puesto | resultado |
|---:|---|
| **2.335** | **coincide en la clase**, y corrige el superviviente: la doctrina es la casa y el caso viaja como ejemplo (seccion 78.2) |
| 2.368 | **coincide**: fusion mutua sin superviviente |
| 2.310 | **coincide** |
| **2.371** | **DISCREPA. A pasa a D** (seccion 78.1) |

> **TERCERA EVIDENCIA DE QUE EL MARCADO SIRVE, y esta es la mas fuerte de las tres.**
> En la R42 las dos discrepancias de ocho cayeron dentro de los cinco marcados. El
> barrido de direccion tumbo el **2.338**, **tambien marcado**. Y la R43, **leyendo
> unicamente marcados**, encontro **una caida en cuatro**.
>
> **Las cuatro caidas que ha tenido el archivo (2.195, 2.215, 2.338 y 2.371) estaban las
> cuatro marcadas como discutibles antes de que nadie las releyera.** Ninguna
> discrepancia ha aparecido fuera de la lista todavia, y **ese es el numero que hay que
> vigilar**: el dia que aparezca una fuera, lo que se mueve no es un veredicto, es el
> credito de toda la tanda.

### TANDA R44: tres puestos, TRES DE TRES COINCIDEN

**18 ago 2026.** Segunda relectura ciega hecha **solo sobre marcados**: los tres
discutibles de la seccion 79.6, **2.396, 2.389 y 2.335**.

| puesto | resultado | lo que deja escrito |
|---:|---|---|
| **2.396** | **coincide** | **tres perdidas nombradas para viajar**, abajo |
| **2.389** | **coincide** | queda como **ejemplar vivo del 3% lexico** |
| **2.335** | **coincide** | **confirmado en su estado corregido**: la doctrina es la casa |

**LAS TRES PERDIDAS DEL 2.396, nombradas para que la fusion no las deje caer.** Muere
`seduccion_modelo_persona` y con el se van:

| la perdida | que es |
|---|---|
| **revisar como hablas de los errores** en el negocio para ver si siempre se termina culpando a una persona | **el test de entrada** del nodo, y el unico paso suyo que se ejecuta sin saber doctrina |
| **el castigo no reemplaza el analisis de la causa de fondo** | **una advertencia con destinatario**: va a las reglas internas, no al investigador |
| **entender las limitaciones del modelo de persona frente a los problemas de fondo** | **el POR QUE SEDUCE**, que es el titulo del nodo y **va entero al superviviente** |

> **La tercera es la que importa y por eso se escribe aparte.** `enfoque_situacional_vs_personal`
> dice **cuando** mirar a la persona y **cuando** al sistema; **no dice por que la
> primera opcion resulta tan comoda.** Sin esa explicacion, el criterio queda como una
> regla arbitraria que la gente incumple sin saber que la incumple.

**EL 2.389 COMO EJEMPLAR VIVO DEL 3% LEXICO** (informe §76.3 y PENDIENTES, advertencia
de aduana). `cultura_de_aprendizaje` e `ingenieria_cultura_aprendizaje` son **el mismo
ciclo de cuatro casillas** escrito con **dos vocabularios que casi no se tocan**:
*mecanismos formales de analisis de datos* contra *forma sistematica de observar*;
*procesos de decision para implementar reformas* contra *disenar e imaginar soluciones*.
**Y estan SIN ARISTA.** Ninguna maquina que compare palabras los junta; la lectura si.

### LA METRICA DE CREDITO, y es el numero que hay que vigilar

> **TODA CAIDA DEBE CAER DENTRO DEL MARCADO. EL DIA QUE APAREZCA UNA FUERA, LO QUE SE
> MUEVE NO ES UN VEREDICTO: ES EL CREDITO DE TODA LA TANDA.**

**Por que es una metrica y no una frase.** Si el lector **sabe donde esta flojo**, sus
lecturas no marcadas valen mas que las marcadas, **y esa diferencia es lo que se esta
midiendo**. Una discrepancia fuera de la lista dice que **el lector no sabe donde falla**,
y entonces **ninguna de sus lecturas tiene mas credito que otra.**

**LA CUENTA AL DIA, corte 2.400:**

| | |
|---|---:|
| caidas del archivo | **4** (2.195, 2.215, 2.338, 2.371) |
| **caidas DENTRO del marcado** | **4** |
| **caidas FUERA del marcado** | **0** |
| relecturas ciegas corridas | **3** (R42, R43, R44) |
| puestos releidos | **15** |

**CUATRO DE CUATRO DENTRO.** La R44 ademas **no encontro ninguna caida en tres**, que es
el otro resultado posible de una relectura sana: **los marcados tambien se sostienen a
veces, y eso no debilita la metrica, la completa.**

### TANDA R45: un puesto, el 2.414, COINCIDE

**18 ago 2026.** Tercera relectura ciega hecha solo sobre marcados. **Coincide.**
`programa_mejora_calidad_14_pasos` repite contra `programa_de_mejora_de_calidad`, los dos
de Crosby. **La cuenta de la metrica de credito sube a cinco relecturas y dieciseis
puestos, y sigue en cuatro caidas, cuatro dentro, cero fuera.**

#### TERCERA CABEZA DUPLICADA DE SERIE: la figura ya tiene patron

**Crosby se suma a Coleman y a los medios.** Con tres ejemplares, esto deja de ser una
coincidencia y pasa a ser **una forma que hay que buscar en cada serie del catalogo**.

| puesto | la serie | las dos cabezas |
|---:|---|---|
| **326** | Coleman | los dos programas generales de la serie, **A** |
| **948** | los medios de Coleman | **los dos nodos generales de la serie repiten entre si** |
| **2.414** | **los catorce pasos de Crosby** | `programa_de_mejora_de_calidad` (6 pasos) y `programa_mejora_calidad_14_pasos` (7 pasos), **A** |

> **EL PATRON, y por eso conviene tenerlo escrito antes de leer el resto de `quality`:**
> cuando un libro trae **una serie numerada** (catorce pasos, siete medios, cinco fases),
> el catalogo tiende a guardar **la serie desplegada en nodos** *y ademas* **una o dos
> cabezas que la resumen entera**. **Las cabezas repiten entre si**; los pasos de la serie
> no. La cabeza duplicada **no se detecta por el titulo** (aqui son *Programa de Mejora de
> Calidad* contra *Programa de Mejora de Calidad, 14 pasos*), **se detecta porque las dos
> comprimen la misma numeracion.**

#### LA PERDIDA QUE VIAJA, con su motivo de producto

**Muere `programa_mejora_calidad_14_pasos` y se lleva una linea que la vara considera
menor y el producto no:** *reunir a un pequeno equipo que impulse la mejora, **aunque sea
de dos o tres personas***.

> **El superviviente pide un equipo con representantes de CADA AREA del negocio.** Para el
> publico de la app, **un negocio pequeno**, esa frase **descarta el paso 2 entero**: quien
> tiene tres empleados lee *representantes de cada area* y cierra la ficha. **La linea que
> muere es lo unico del par que hace el programa ejecutable a esa escala.**
>
> **No cambia la clase** (por la vara es linea, y lo es), **cambia lo que la fusion tiene
> obligacion de reponer.**

#### EL COSTO DE LA NO CALIDAD: ARISTA, NO PERDIDA, y la verificacion la cierra

El hijo pide *definir como vas a medir la calidad **y el costo de la no calidad***. **Eso
no se copia al superviviente: se cablea**, porque el catalogo tiene el nodo que lo hace,
`costo_de_mala_calidad_copq`.

> **VERIFICADO CONTRA EL GRAFO, y el resultado corrige el encargo: la arista YA EXISTE.**
> `costo_de_mala_calidad_copq` figura en los `nodos_previos` **de los dos nodos del par**,
> del que muere y del que sobrevive. **No es arista candidata: es arista puesta.**
>
> **Por eso la perdida aqui es CERO.** El paso del hijo **ya esta servido por el grafo en
> el superviviente**, y la fusion no tiene que anadir nada por este lado. **Queda escrito
> porque el caso contrario habria sido trabajo, y porque comprobarlo costo una consulta.**

**Y la fusion alimenta la D1 de Crosby**: es la cabeza de esa serie la que queda de pie,
asi que el nodo que sobreviva **es el que la D1 tiene que nombrar.**

### TANDA R46: dos puestos, DOS DE DOS COINCIDEN

**18 ago 2026.** Cuarta relectura ciega hecha solo sobre marcados: **2.417 y 2.421**.
**Las dos coinciden.**

**LA METRICA DE CREDITO AL DIA:**

| | |
|---|---:|
| relecturas ciegas corridas | **6** (R42, R43, R44, R45, R46) mas el barrido de direccion |
| puestos releidos | **18** |
| caidas del archivo | **4** |
| **dentro del marcado** | **4** |
| **fuera del marcado** | **0** |

#### a. EL 2.417, y una fusion mutua NO HEREDA POR DEFECTO

**Es la diferencia entre una A con superviviente y una A mutua.** Cuando hay
superviviente, lo que muere **se absorbe en un nodo que ya existe**. **Aqui no hay
superviviente**, asi que **nada se hereda solo**: las tres lineas hay que **escribirlas en
el encargo de fusion o se pierden las tres.**

| la linea | de que nodo | que es |
|---|---|---|
| **asignar responsables de supervision** que verifiquen el cumplimiento del control | `mantener_las_ganancias` | **una asignacion**: sin dueno, el control es un documento |
| **revisar el sistema tras rotacion de personal** | `mantener_las_ganancias` | **un disparador**, no un calendario. Es la unica condicion del par que se activa por un hecho y no por una fecha |
| **aplicar tecnicas de a prueba de errores donde sea posible** | `sostener_las_ganancias` | **otra clase de control**: disenar el error fuera en vez de auditarlo despues |

**LA TERCERA SE CLASIFICO CON EL GRAFO ANTES DE ESCRIBIRLA, no por criterio.**

> **RESULTADO: ES ARISTA CANDIDATA, NO PERDIDA.** El catalogo **si tiene** donde cablearla.

| medicion | cifra |
|---|---:|
| nodos con **poka yoke o mistake proofing EN EL ID** | **6** |
| nodos que lo **mencionan en pasos, titulo o entregable** | **13** |
| de los seis, **presentes en la cola de `quality`** | **3** |
| **aristas actuales entre los dos nodos del 2.417 y cualquiera de los seis** | **0** |

**Los seis:** `errores_a_prueba_poka_yoke`, `mistake_proofing_poka_yoke`,
`mistake_proofing_poka_yoke_2`, `poka_yoke_a_prueba_de_errores`,
`error_proofing_servicio`, `error_proofing_six_sigma_lean`.

> **Y aqui el resultado sale al reves que en el 2.414, que es justo lo que hace util
> comprobarlo:** alli el COPQ **ya estaba cableado** y la perdida era cero; **aqui el
> poka yoke existe y NO esta cableado con ninguno de los dos nodos del par.** Misma
> doctrina, *el paso se cablea y no se copia*, y **dos resultados opuestos.** **Sin la
> comprobacion, uno de los dos se habria escrito mal.**

#### b. EL 2.421: la evidencia estadistica viaja con nombre

**Muere `relaciones_largo_plazo_con_proveedores` y se lleva un criterio que el
superviviente no reemplaza:** *definir criterios de evaluacion que incluyan **evidencia
estadistica de calidad**, no solo el precio*.

> **`relacion_largo_plazo_proveedor_unico` evalua por *evidencia de mejora continua*.** No
> es lo mismo: **la mejora continua no sustituye a la evidencia estadistica, la diluye.**
> Una es **una tendencia que se afirma**; la otra es **un dato que se exige**. **Viaja con
> nombre propio al encargo de fusion.**

**Y la segunda linea del mismo nodo, *revisar cuantos proveedores tienes hoy para cada
articulo clave*, viaja tambien**: es el **paso cero** que el superviviente da por hecho, y
sin el la instruccion *reducir progresivamente* no tiene desde donde empezar.

### LAS DOS VIAS, Y UNA SOLA CONCLUSION

**El cribado ha medido dos veces si la forma del nombre o del texto puede decidir un
veredicto, y las dos veces la respuesta es la misma.**

| via | medicion | resultado |
|---|---|---|
| **el vocabulario** (§76.3) | prueba de cobertura lexica sobre 46 A con direccion | **34 marcadas, 1 lo era: 3% de precision** |
| **el identificador** (§82.2) | 5 pares del mismo id de familia en `quality` | **3 repitieron, 2 no: 60%** |

> **NI EL NOMBRE NI EL VOCABULARIO DECIDEN. ORDENAN.**
>
> El identificador acierta mucho mas que el vocabulario, **y aun asi se equivoca dos de
> cada cinco**: `sistema_responsabilidad_gerencial` contra su `_2` **es D**, porque uno
> **acota** la responsabilidad y el otro **la mide**.
>
> **Lo que las dos vias sirven para hacer es lo mismo: PONER DELANTE lo que hay que
> mirar.** Es exactamente lo que la cola ya hace con la similitud, y **el limite es el
> mismo: el veredicto se lee.**

### TANDA R47: dos puestos, DOS DE DOS COINCIDEN

**18 ago 2026.** Quinta relectura ciega sobre marcados: **2.432 y 2.431. Las dos
coinciden.**

| | |
|---|---:|
| relecturas ciegas | **7** (R42 a R47) mas el barrido de direccion |
| puestos releidos | **20** |
| caidas | **4** |
| **dentro del marcado** | **4** |
| **fuera** | **0** |

#### a. NACE UNA CLASE DE PERDIDA: LA PERDIDA DE NOMBRE

**Del 2.432 sale una clase que el banco no tenia** y que queda escrita en **9.28**: hay
fusiones donde **lo que muere no es un paso ni una linea, es la palabra por la que el
lector llega**. El alias del grafo **cubre el id y no cubre la busqueda**; el remedio es
que **el nombre viaje como DENOMINACION**, una linea en el texto del superviviente.

**BARRIDO CORRIDO SOBRE LAS 58 A QUE ELIGEN DIRECCION: SON DOS.**

| puesto | muere | sobrevive | el nombre |
|---:|---|---|---|
| **2.250** | `niveles_de_madurez_de_seguridad` | `clasificacion_sistemas_por_nivel_seguridad` | **Amalberti** |
| **2.432** | `funcion_perdida_taguchi` | `funcion_perdida_limites_especificacion` | **Taguchi** |

**Sin adjudicar: son dos denominaciones a reponer, y las dos clases A se sostienen.**
**Esa es la carga futura de esta clase**, y se recomputa con el script cada vez que crezcan
las A con direccion.

#### b. `accion_correctiva` QUEDA REGISTRADA COMO ACTO EN COLAPSO

**No es una cadena de pares: es una familia de cinco decidiendose de a dos**, y la
doctrina vigente dice exactamente que hacer.

| lo leido | resultado |
|---:|---|
| 2.418 | muere `accion_correctiva_6`, sobrevive `accion_correctiva_5` |
| 2.426 | muere `accion_correctiva_6`, sobrevive `accion_correctiva_crosby` |
| 2.431 | **muere `accion_correctiva_5`**, sobrevive `accion_correctiva_sistematica` |

> **POR 9.3, UNA DIRECCION DE FUSION DECIDIDA SOBRE UN PAR NO SOBREVIVE A SU FAMILIA.** El
> superviviente del 2.418 murio trece pares despues. **Los supervivientes por par quedan
> MARCADOS PROVISIONALES.**
>
> **POR P.13, EL SUPERVIVIENTE FINAL SE ELIGE UNA SOLA VEZ Y SOBRE LA NOMINA COMPLETA**,
> no heredando el de la operacion pequena.
>
> **POR P.5, EL ACTO SE LEE ENTERO ANTES DE FUNDIRSE**, y aqui eso tiene nombre y numero:
> **los tres pares sin leer de la familia** (`accion_correctiva`, `accion_correctiva_2`,
> `accion_correctiva_4` contra los demas) **son su lectura de acto**, no una curiosidad.

**Las clases A de los tres pares no se tocan: lo provisional es la DIRECCION, no el
veredicto.**

#### c. REGLA MENOR: CUANDO NO HAY SUPERVIVIENTE, LA PERDIDA SE ADHIERE AL ACTO

> **En una A por FUSION MUTUA no hay nodo al que absorber la linea perdida.** La perdida
> **no queda huerfana ni se asigna a ojo: SE ADHIERE AL ACTO**, y **la hereda quien gane
> P.8 sobre la nomina final.**

**Aplicado al 2.417**, cuyas tres lineas quedan asi:

| la linea | destino |
|---|---|
| **responsables de supervision** | **adherida al acto** |
| **revisar tras rotacion de personal** | **adherida al acto** |
| aplicar tecnicas de a prueba de errores | **ARISTA CANDIDATA**, ya resuelta: hay 6 nodos de poka yoke y cero aristas con el par |

**Con esto el archivo tiene cuatro fusiones mutuas** (2.127, 2.368, 2.417, 2.436) **y una
regla que dice donde va lo que sobra en las cuatro.**

### TANDA R48: un puesto, el 2.440, COINCIDE. Y la comprobacion tumba la premisa

**18 ago 2026. La A se sostiene.** `moral_y_sistema_no_individuo` repite contra
`identificacion_causa_raiz_no_culpa_individual`.

| | |
|---|---:|
| relecturas ciegas | **8** (R42 a R48) mas el barrido de direccion |
| puestos releidos | **21** |
| caidas | **4** . dentro del marcado **4** . fuera **0** |

#### LA PERDIDA SE VERIFICO ANTES DE CLASIFICARLA, Y NO ES DE CATALOGO

**La hipotesis a comprobar era esta:** *dar seguimiento y **apoyo** a quienes caen fuera de
las tolerancias del grupo* **seria el unico lugar del catalogo donde se dice que se hace
CON LA PERSONA despues de absolverla**, y sin ella *enfocate en el sistema* se leeria como
*abandona al que esta fuera*.

> **LA COMPROBACION CONTRA EL GRAFO DICE QUE NO. HAY DOS NODOS QUE LA CUBREN, Y LOS DOS LA
> DESARROLLAN MEJOR QUE EL NODO QUE MUERE.** Los dos son de Deming, la misma fuente.

| nodo | el paso que la cubre | que anade sobre la linea que muere |
|---|---|---|
| **`deteccion_de_lideres_y_rezagados`** | paso 4: *investigar causas especificas para los de bajo desempeno* | **nombra las tres causas a revisar: equipo, entrenamiento y SALUD** |
| **`liderazgo_para_mejora_continua`** | paso 2: *disenar mecanismos de **ayuda individual** o reconocimiento segun corresponda* | su **entregable** es literalmente *apoyo individualizado basado en datos*, y anade **el reconocimiento al que esta fuera POR ARRIBA** |

**`deteccion_de_lideres_y_rezagados` ademas hace la mitad que faltaba:** su paso 5 manda
**estudiar y documentar los metodos de los de ALTO desempeno para replicarlos.** El nodo
que muere solo miraba hacia abajo.

**ENTONCES LA CLASIFICACION CORRECTA ES OTRA:**

| lo propuesto | lo verificado |
|---|---|
| perdida **de CATALOGO** | **perdida DE PAR** |
| **prioridad de rescate** en el reparto | **ARISTA CANDIDATA**: el contenido tiene dos casas, lo que falta es el cable |

**LA COMPROBACION DEL CABLE, hecha tambien:**

| | |
|---|---:|
| aristas entre el superviviente y los dos cubridores | **0** |
| aristas entre el nodo que muere y los dos cubridores | **0** |
| `deteccion_de_lideres_y_rezagados` en la cola | **si**, puestos **2.919** y **3.170** |
| `liderazgo_para_mejora_continua` en la cola | **NO ESTA** |

> **TERCER CASO DE LA MISMA FORMA, y los tres con resultado distinto**: en el **2.414** el
> COPQ **ya estaba cableado** y la perdida era cero; en el **2.417** el poka yoke **existe
> y no esta cableado**; aqui **el apoyo al que queda fuera existe, esta mejor desarrollado
> que en el nodo que muere, y tampoco esta cableado.**
>
> **Y este es el primero donde la comprobacion VOLTEA LA PREMISA.** La linea parecia unica
> y no lo era. **Sin comprobar, se habria escrito una prioridad de rescate para algo que el
> catalogo ya tiene dos veces.**

**LO QUE SI QUEDA ANOTADO PARA EL REPARTO:** `liderazgo_para_mejora_continua` **no esta en
la cola**, asi que **el cribado no lo va a emparejar nunca**. Es carga de las rutas de
enlace, como los 242 de `quality` y los 120 de los racimos de `health_safety`.

### LAS TRES CARAS DE LA MISMA FAMILIA, con su antidoto

**El cribado ha medido tres veces si una senal de forma puede decidir un veredicto. Las
tres fallan, cada una a su modo, y las tres tienen antidoto escrito.**

| la senal | la medicion | como falla | **el antidoto** |
|---|---|---|---|
| **el vocabulario** (§76.3) | 34 marcadas de 46, **1 lo era: 3%** | **no ve el parecido**: dos nodos dicen el mismo paso sin compartir una palabra | **leer el par**. La cobertura lexica no se usa como filtro, solo como orden |
| **el identificador** (§82.2, §84.3) | 5 pares de familia, **3 repitieron: 60%** | **ve parecido donde no lo hay**: un `_2` puede marcar destinatario (2.439) u objeto (2.433) distinto | **mirar el destinatario y el objeto**, no el sufijo |
| **la subcadena** (§9.28 del banco) | 3 nombres propios detectados, **1 falso** | **inventa la senal**: `ries` dentro de *riesgo* | **coincidencia por PALABRA COMPLETA**, ya corregida en el script |

> **LAS TRES SIRVEN PARA LO MISMO Y NINGUNA PARA MAS: PONER DELANTE LO QUE HAY QUE MIRAR.**
> El vocabulario **se queda corto**, el identificador **se pasa de largo**, y la subcadena
> **se inventa lo que mide**. **Ninguna decide. El veredicto se lee.**

### TANDA R49: dos puestos, DOS DE DOS COINCIDEN

**18 ago 2026. 2.445 y 2.447, las dos coinciden.**

| | |
|---|---:|
| relecturas ciegas | **9** (R42 a R49) mas el barrido de direccion |
| puestos releidos | **23** |
| caidas | **4** . dentro del marcado **4** . fuera **0** |

#### a. CLASE REGISTRADA: PERDIDA DE LINEA CON MOTIVO DE ALCANCE

> **Lo que muere no es un paso, ni una denominacion: es UNA LISTA DE EJEMPLOS que abria
> el nodo a lectores de otro rubro.**

**COMO SE DISTINGUE DE LA PERDIDA DE NOMBRE (9.28), que es su vecina:**

| | **perdida de NOMBRE** (9.28) | **perdida de ALCANCE** |
|---|---|---|
| que se pierde | **la denominacion del instrumento** | **los ejemplos que lo aterrizan en otros sectores** |
| el sintoma | el superviviente **no dice la palabra** por la que se busca | el superviviente **dice la palabra**, pero **solo con un ejemplo** |
| el remedio | el nombre viaja como **denominacion**, una linea | **los ejemplos viajan a la lista del superviviente** |

**EL EJEMPLAR: puesto 2.445.** Muere `estandares_especificos_industria` y sobrevive
`adaptaciones_sectoriales_iso`, **que si nombra ISO y cGMP** y por eso **no entra en 9.28**.
Lo que se va son **AS9100 e ISO 14000**.

> **EL REMEDIO, escrito: AS9100 e ISO 14000 ENTRAN A LA MENCION DEL QUE QUEDA.** Su paso 4
> ya dice *certifica bajo la norma sectorial correspondiente*: basta con que **la
> enumeracion incluya los tres**, cGMP, AS9100 e ISO 14000. **Es una linea, no un nodo.**

**LA REGLA ESPEJO QUE YA EXISTE ES EL 9.18**, *una regla abolida se busca tambien en su
espejo*. **La relacion es la misma y conviene tenerla dicha: cuando se funde por contenido,
hay que mirar tambien lo que el nodo servia de PUERTA**, no solo lo que mandaba hacer.
**Un nodo puede no aportar ni un paso y seguir siendo por donde entra un lector.**

#### b. EL 2.447, y el titulo espejo como CUARTA CARA

**Perdidas nombradas de `estilo_gerencial_hockey_vs_ballet`:**

| la linea | por que se anota |
|---|---|
| **capacitar a los supervisores en tecnicas de comunicacion y coordinacion** | **es la unica accion de FORMACION del par.** El superviviente trae un protocolo de reunion completo **escrito para alguien que ya sabe conducir una reunion** |
| **fomentar la comunicacion clara y coordinada entre los niveles** | el protocolo del superviviente actua **dentro** de una reunion; esta linea es **entre niveles y fuera de ella** |

**EL TITULO ESPEJO ENTRA A LA FAMILIA DE SENALES DE SUPERFICIE, con su historial:**

| puesto | el par | lectura |
|---:|---|:---:|
| **2.221** | `new_view_vs_old_view` contra `old_view_vs_new_view_human_error` | **A** |
| **2.412** | `capacidad_de_proceso` contra `capacidad_del_proceso` | **D** |
| **2.447** | `estilo_gerencial_ballet_vs_hockey` contra `estilo_gerencial_hockey_vs_ballet` | **A** |

> **Tres apariciones, dos A y una D: el titulo espejo acierta dos de cada tres.** Queda
> como **cuarta cara** junto al vocabulario (3%), el identificador (60%) y la subcadena
> (falso de tres). **Y con la misma conclusion: ordena, no decide.**

### TANDA R50: un puesto, el 2.451, COINCIDE

**18 ago 2026.** **La A se sostiene.**

| | |
|---|---:|
| relecturas ciegas | **10** (R42 a R50) mas el barrido de direccion |
| puestos releidos | **24** |
| caidas | **4** . dentro del marcado **4** . fuera **0** |

### REGLA NUEVA AL REPARTO DE PERDIDAS: LA PERSUASION ES CONTENIDO

> **LOS BENCHMARKS, LOS CASOS DE EXITO Y EL DESTINO DEL ENTREGABLE ENTRAN AL REPARTO CON
> NOMBRE PROPIO.**

**EL MOTIVO, y es de producto y no de doctrina.** **P.8 pesa PROCEDIMIENTO**: cuenta pasos
con decisiones dentro y deja fuera, por construccion, **el material con el que el lector
convence a un tercero**. Y este catalogo **no es para auditores de calidad: es para
emprendedores que tienen que convencer** a un socio, a un banco, a un proveedor o a si
mismos.

> **Un ROI bien calculado y sin un caso al lado no mueve un presupuesto. Una norma
> nombrada sin sus hermanas no la encuentra el lector de otro rubro. Un numero exacto que
> nadie manda hacia arriba no cambia una decision.**

**LOS DOS EJEMPLARES, y los dos son del mismo tramo de siete pares:**

| puesto | muere | sobrevive | lo que se lleva |
|---:|---|---|---|
| **2.445** | `estandares_especificos_industria` | `adaptaciones_sectoriales_iso` | **AS9100 e ISO 14000**, las dos puertas por las que entra un lector de aeronautica o de ambiental |
| **2.451** | `roi_breakthrough` | `roi_proyectos_calidad` | **el Six Sigma de Samsung** como caso que respalda, **y el mandato de reportar el ROI a la direccion** |

> **En los dos, el superviviente GANA POR PRECISION Y PIERDE POR PERSUASION**: uno trae el
> requisito sustantivo de la norma, el otro trae la formula del ROI. **Ninguno de los dos
> trae con que convencer.**

### LOS SEIS MOTIVOS DE PERDIDA DE LINEA, con su remedio

**Adjudicado el 18 ago 2026: de tres a CUATRO tras la R51, a CINCO tras la R52, y a SEIS
tras la R53.**

| motivo | que muere | como se reconoce | **el remedio** | ejemplares |
|---|---|---|---|---|
| **NOMBRE** (banco 9.28) | **la denominacion del instrumento** | el superviviente **no dice la palabra** por la que se busca | el nombre viaja como **DENOMINACION**: una linea en el titulo o la primera frase | **2.250** (Amalberti), **2.432** (Taguchi) |
| **ALCANCE** | **los ejemplos que abrian el nodo a otros sectores** | el superviviente **si dice la palabra**, pero **con un solo ejemplo** | los ejemplos **entran a la enumeracion** que el superviviente ya tiene | **2.445** (AS9100, ISO 14000), y el caso Samsung del **2.451** |
| **DESTINO** | **a donde va el entregable y a quien hay que convencer** | el superviviente **produce el resultado y no dice que hacer con el** | la linea de destino entra **como paso final** del superviviente | **2.451** (*documentar el ROI para reportarlo a la direccion*) |
| **METODO ALTERNATIVO** | **la otra forma de hacer el mismo paso, la que sirve a otra escala** | el superviviente manda **un solo camino**, y el que muere traia **uno mas barato o mas lento** | el paso del superviviente pasa a **VARIANTE CONDICIONAL**: **la condicion del lector elige el camino** | **2.453**: *recolectar datos diarios durante varias semanas* **o por muestreos periodicos si no puedes medir a diario* |
| **DIRECCION** | **el SENTIDO en que corre cada flujo del paso** | el superviviente **manda hacer la cosa y no dice de quien a quien** | **EL SENTIDO ENTRA DENTRO DEL PASO**: una especificacion en el paso de requisitos y otra en el de retroalimentacion | **2.458**: *los requisitos bajan del proveedor al procesador; la retroalimentacion sube del cliente al procesador* |
| **SALVAGUARDA** | **la advertencia que impide que un paso se resuelva solo por el sesgo por defecto** | el superviviente **manda decidir y no dice contra que sesgo**. **FIRMA DE LA CLASE, medida con sus dos ejemplares: los dos protegen un paso de DECISION, no de ejecucion** | **SE ADOSA AL PASO QUE PROTEGE**: el inciso entero entra al paso que sin el se resolveria solo | **2.461**: *priorizar sin asumir jerarquias automaticas por tipo de cliente*. **2.467**: *seguir revisando con cartas que la fraccion se mantenga estable* |

**EL REMEDIO DEL CUARTO, con su forma exacta.** No es anadir un paso ni partir el nodo: es
**abrir el paso que ya existe.**

| como esta | como queda |
|---|---|
| *Recolectar datos diarios de defectos o errores durante varias semanas.* | *Recolectar datos diarios de defectos o errores durante varias semanas, **o por conteos puntuales y muestreos periodicos si no puedes medir a diario**.* |

> **La condicion la evalua el lector, no el catalogo.** Por eso la variante va **dentro del
> paso** y no como nodo hermano: **un negocio de tres personas no necesita elegir entre dos
> fichas, necesita que la ficha contemple su caso.**

**EL REMEDIO DEL QUINTO, con su forma exacta.** Tampoco es un paso nuevo: es **una
especificacion de quien a quien dentro de dos pasos que ya existen.**

| como esta | como queda |
|---|---|
| *Identificar expectativas mutuas explicitas entre cada par de roles.* | *Identificar expectativas mutuas explicitas entre cada par de roles, **con los requisitos bajando del proveedor al procesador**.* |
| *Establecer bucles de retroalimentacion claros para medir cumplimiento.* | *Establecer bucles de retroalimentacion claros para medir cumplimiento, **subiendo del cliente al procesador**.* |

> **Un mapa sin sentidos no es medio mapa: es un mapa que no se puede recorrer.** El
> superviviente sabe **que pares hay que conectar y que hay que medir**; sin el sentido,
> **no sabe cual de los dos extremos escribe la especificacion y cual la recibe.**

**EL REMEDIO DEL SEXTO, y esta anclado a P.11.** El banco del plan ya dice que **una
advertencia es LINEA, no procedimiento**: por eso la salvaguarda **nunca es un paso propio**.

| como esta | como queda |
|---|---|
| *Analizar y priorizar las necesidades identificadas.* | *Analizar y priorizar las necesidades identificadas, **de forma consensuada y sin asumir jerarquias automaticas por tipo de cliente**.* |

> **La salvaguarda se adosa AL PASO QUE PROTEGE, no al nodo.** Suelta al final no protege
> nada: **el sesgo actua dentro del paso de priorizar, y ahi tiene que estar el freno.**
>
> **Y la prueba de que hacia falta la sexta entrada: sin ella, esta perdida se habria
> metido a la fuerza en ALCANCE**, que es la mas parecida y la equivocada. **Una
> advertencia no abre puertas a otro rubro: cierra una salida facil.**

### LA PRUEBA COMUN DE LOS CUATRO

> **VALOR SIN PROCEDIMIENTO NUEVO: INVISIBLES PARA LA VARA, OBLIGATORIOS EN EL REPARTO.**

**Los cuatro tienen la misma anatomia y por eso forman una clase:**

| | |
|---|---|
| **que son** | linea que **no anade un paso con decisiones dentro** |
| **que hace la vara con ellos** | **nada**: por 9.6.1 son LINEA, y el veredicto A **esta bien** |
| **que se pierde si nadie los anota** | el **nombre** por el que se llega, las **puertas** por las que entra otro rubro, la **salida** hacia quien decide, o la **escala** a la que el lector puede ejecutarlo |
| **el remedio de los cuatro** | **una linea en el superviviente. Nunca un nodo.** |

> **Y la consecuencia que ordena el trabajo: EL VEREDICTO NO ES EL RIESGO, LA FUSION LO
> ES.** Las 471 A del archivo estan bien clasificadas; **lo que puede empobrecer el
> catalogo es fundir sin leer estas cuatro columnas.** Por eso se anotan **con nombre
> propio, puesto por puesto**, y no como una advertencia general al final.

### TANDA R55: cuatro puestos, CUATRO DE CUATRO COINCIDEN

**18 ago 2026. 2.492, 2.493, 2.498 y 2.500, ciega, y las cuatro coinciden.** Son
**los cuatro que el checkpoint 2.500 habia marcado como discutibles**, asi que la tanda
entra entera dentro del marcado.

| | |
|---|---:|
| relecturas ciegas | **15** (R42 a R55) mas el barrido de direccion |
| puestos releidos | **35** |
| caidas | **4** . dentro del marcado **4** . fuera **0** |

> **La metrica de credito se sostiene: cero caidas fuera del marcado en quince
> relecturas.** Cada una de las cuatro caidas historicas cayo donde el cribado habia
> avisado que podia caer.

#### LO QUE LA R55 ANADE SOBRE LOS VEREDICTOS, sin moverlos

**1. EL 2.498: LOS 250.000 DOLARES VIAJAN CON ATRIBUCION DE AUTOR.**

**No basta el corte del 9.21.** El umbral de retorno minimo por proyecto de un Black Belt
**es una cifra de Juran**, y en la fusion **viaja diciendo de quien es**, no como si fuera
un criterio del catalogo.

| como NO se escribe | como se escribe |
|---|---|
| *asignale proyectos con retorno minimo de 250.000 dolares* | *Juran fija el umbral en 250.000 dolares de retorno por proyecto* |

> **El motivo es el mismo del 2.473:** una cifra sin dueno **se lee como recomendacion del
> catalogo**, y este catalogo **no ha medido eso**. La atribucion es la que hace la
> afirmacion verificable.

**2. EL 2.498: LA VOZ DE NEGOCIO PEQUENO DEL QUE MUERE, al patron.**

`rol_black_belt_six_sigma` es el que habla **al dueno directamente**: *elige a alguien con
potencial de liderazgo*, *dale una capacitacion*, *acuerda con esa persona como te va a
asesorar*. **El que sobrevive en la lectura de nombre habla de certificaciones y de
organismos.** En una fusion mutua **no muere ninguno de los dos, pero se elige una voz**, y
la que se elige es la del que se dirige al lector.

> **AL PATRON DEL NEGOCIO PEQUENO, como ejemplar nuevo: cuando dos nodos dicen lo mismo y
> uno lo dice en segunda persona al dueno, ESA es la redaccion que sobrevive.** No es
> preferencia de estilo: **es la unica de las dos que un lector sin departamento de calidad
> puede ejecutar.**

**3. EL 2.500: PRIORIZAR COMO PROYECTOS ES PERDIDA DE DESTINO.**

La linea que muere, **priorizar los problemas detectados como proyectos de mejora**, se
habia anotado suelta. **Queda clasificada: motivo DESTINO**, el tercero de la tabla de
seis.

| | |
|---|---|
| **por que DESTINO y no ALCANCE** | no amplia lo que se mapea: **dice adonde va el resultado del mapa**. Sin ella el VSM termina en un dibujo del estado futuro y **no entra en la cartera de mejora** |
| **el remedio** | una linea en `mapeo_flujo_valor`: **los desperdicios priorizados salen como proyectos** |

#### ADJUDICACION MENOR AL 2.488: EL ACRONIMO ES DENOMINACION BUSCABLE

**El checkpoint 2.500 dijo que la perdida quedaba reducida al acronimo MBO y que con eso
bastaba.** Adjudicado: **no basta por si solo, y el remedio es de una linea.**

> **QUIEN BUSCA MBO NO ESCRIBE GESTION POR OBJETIVOS.** Un acronimo **no es una abreviatura
> del nombre: es OTRA denominacion**, y es la que usa quien viene de un libro de gestion en
> ingles.

**EN LA OPERACION DE ESA FUSION: MBO VIAJA ENTRE PARENTESIS**, dentro del titulo o de la
primera frase de `eliminacion_gestion_por_objetivos_y_numeros`.

**REGISTRO DE DENOMINACIONES A REPONER, al dia:**

| puesto | la denominacion | donde se repone |
|---:|---|---|
| **2.250** | **Amalberti** | superviviente del par |
| **2.432** | **Taguchi** | superviviente del par |
| **2.488** | **MBO**, entre parentesis | `eliminacion_gestion_por_objetivos_y_numeros` |

> **Y la regla que sale de las tres: EL ACRONIMO CUENTA COMO DENOMINACION APARTE.** El
> control de denominacion dentro de cada fusion (banco 9.28) **busca tambien las siglas**,
> no solo los nombres propios y los instrumentos.

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

> **ADJUDICADO EL 14 ago 2026: LAS ESPECIALIZACIONES NO SON UNIFORMES.** La
> jerarquia madre-hijas **no se aplica en bloque a esta familia**. Con la evidencia
> medida, **la digital SE ENLAZA** (aporta probar varios canales con presupuesto
> parecido, puesto 537) **y la fisica SE FUNDE** (no tiene ni un paso fisico y
> repite al general cinco veces, puesto 609). **La mesa de esta familia queda con
> DOS decisiones distintas, no una.** La figura general queda en el banco, 9.25.

> **LA EVIDENCIA, PARTIDA EN DOS, para la candidatura madre-hijas (R35, 14 ago
> 2026).** No es lo mismo que el general repita con un hijo que dos hijos repitan
> entre si, **y la mesa tiene que ver las dos columnas.**
>
> | tipo de par | cuantos | puestos |
> |---|---:|---|
> | **contra el GENERAL** | **CUATRO, todos A** | 165, 400, 537, 609 |
> | **entre HIJOS** | **CUATRO, tres leidos y los tres A** | 214, 762, 945, y el 1488 pendiente |
>
> **Que el general repita con sus hijos sostiene la lectura madre-hijas; que los
> hijos repitan ENTRE ELLOS la debilita**, porque dos especializaciones distintas
> no deberian decir lo mismo. **Y el 609 anade el dato mas duro**: el hijo FISICO
> no tiene ni un paso que sea fisico, dice lo mismo que el general cinco veces
> seguidas. **El hijo DIGITAL si trae algo propio.** Las especializaciones de esta
> familia **no son uniformes**.

> **RECOMPUTO DEL ARCHIVO, 14 ago 2026 (relectura R31), por el banco 9.10.** La
> cifra de arriba quedo vieja: **609, 762 y 945 ya estan leidos y los TRES en A.**
> **Hoy la familia lleva SIETE pares leidos de quince posibles, LOS SIETE EN A**,
> un solo pendiente en cola (**1488**) y **siete que nunca entraron**. Y **el 762
> y el 945 no tocan al nodo general**: las especializaciones repiten tambien entre
> si, o sea que **NO es un racimo en estrella (banco 9.23): es un SUB-PURO de seis
> miembros sin un solo par sano.** Entra a la tabla viva del banco.

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

> **RECOMPUTO DEL ARCHIVO, 14 ago 2026, por el banco 9.10. La cifra de arriba
> quedo vieja: son NUEVE los pares internos leidos, no cuatro.**
>
> | clase | pares |
> |---|---|
> | **A** | **SEIS**: 166, 177, 293, 692, **792**, **1041** |
> | **D** | **TRES**: **993**, **1211**, **1239** |
>
> **Y las tres D importan de forma distinta.** El **993** ya estaba anotado como el
> primer par interno sano, el que paso el racimo a MEZCLADO. **Los otros dos, el
> 1211 y el 1239, son DOS DE LAS CUATRO CONDICIONES VIVAS**, las que deciden si las
> dos mitades originales son una sola familia. **Van dos de cuatro y las dos en D.**
> Quedan el **1339** y el **1451**. **Las condiciones no se tocan aqui**: se
> recomputa la cuenta, que es lo que el 9.10 obliga.

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


---

## 11.bis LA PARTICION, ESCRITA Y SIN EJECUTAR (16 ago 2026, vigente al puesto 1517)

**LAS CUATRO CONDICIONES SALIERON D. Las cuatro.** Este texto las cierra y deja
escrito lo que la seccion 11 anticipaba, **medido del archivo y sin adjudicar
nada**.

| puesto | el par cruzado | clase |
|---:|---|:---:|
| **1211** | `comprension_capacidades_limitaciones_ia` contra `principio_humano_en_el_loop` | **D** |
| **1239** | `comprension_capacidades_limitaciones_ia` contra `human_in_the_loop_ia` | **D** |
| **1339** | `human_in_the_loop_ia` contra `jagged_frontier_ia` | **D** |
| **1451** | `jagged_frontier_ia` contra `principio_humano_en_el_loop` | **D** |

> **Las cuatro parejas que cruzarian las dos mitades originales estan leidas y
> ninguna repite.** El texto de la seccion 11 decia: *si los cuatro salieran D,
> este racimo se parte en dos y hay que decirlo.* **Se dice.**

### 11.bis.1 Y NO SE PARTE EN DOS: SE PARTE EN TRES

**Medido sobre las A internas de la nomina, con cierre transitivo.**

| bloque | tamano | miembros |
|---|---:|---|
| **EL BLOQUE HUMANO** | **5** | `principio_humano_en_el_loop`, `human_in_the_loop_ia`, `alineacion_etica_ia_negocio`, `mitigar_falling_asleep_wheel`, `riesgo_sobredependencia_ia` |
| **EL BLOQUE DEL MAPA** | **2** | `comprension_capacidades_limitaciones_ia`, `jagged_frontier_ia` |
| **SUELTO** | **1** | `comprender_alineacion_etica_ia` |

> **La sorpresa no es la particion: es el tercer pedazo.**
> `comprender_alineacion_etica_ia` **no pertenece a ninguna de las dos mitades**.
> Su unico par interno leido es el **993**, contra `alineacion_etica_ia_negocio`,
> **y salio D**. Estaba en la nomina por tema, no por evidencia.

**Y el bloque humano crecio por un camino que nadie predijo**: la pareja del
*falling asleep at the wheel*, `mitigar_falling_asleep_wheel` y
`riesgo_sobredependencia_ia`, **entro entera por el puesto 1041**, que engancho
`human_in_the_loop_ia` con `mitigar_falling_asleep_wheel`. **Las dos mitades
originales no se unieron; una de ellas absorbio a una tercera pareja.**

### 11.bis.2 LAS DOS ABSORCIONES, y salen al reves una de la otra

**El encargo pedia registrar que pasa con cada una de las dos parejas adyacentes.
Pasan cosas distintas y el motivo es medible.**

| puesto | la pareja adyacente | resultado | por que |
|---:|---|---|---|
| **1478** | las **alucinaciones**: `deteccion_alucinaciones_ia` y `gestion_alucinaciones_ia` | **NO ENTRA** | el par sale **D**: `principio_humano_en_el_loop` nombra *reconocer cuando la IA inventa* **en una linea** y el otro trae el **procedimiento** de esa linea. Vara del 9.6.1, CONTINUA |
| **1517** | **invitar a la IA a todo**: `invitar_ia_a_todo` y `principio_invitar_ia_siempre` | **ENTRA** | el par sale **A**: `invitar_ia_a_todo` y `jagged_frontier_ia` **hacen el mismo barrido de tareas**, probar la maquina en cada una y anotar donde rinde |
| **363** | (interno de las alucinaciones) | **se fusionan entre si** | releido a ciegas en R19 y sostenido. **Decida lo que decida el 1478** |

> **La leccion, y sirve para las demas parejas adyacentes del inventario: una
> pareja vecina se absorbe cuando HACE LO MISMO que un miembro del racimo, y no
> cuando DESARROLLA UNA LINEA suya.** El detalle de una linea es jerarquia y se
> arregla con una arista; el mismo acto escrito dos veces es gemelo y se arregla
> con una fusion.

### 11.bis.3 LA NOMINA VIGENTE, recomputada al puesto 1517

| medida | antes (al 1400) | **ahora** |
|---|---:|---:|
| miembros | 8 | **10** |
| pares posibles | 28 | **45** |
| en la cola | 13 | **15** |
| **leidos** | 10 | **14** |
| **A / D** | 6 / 4 | **8 / 6** |
| pendientes en cola | 3 | **1**, el **1541** |
| nunca encolados | 15 | **30** |

**La particion final, sobre los DIEZ:**

| bloque | tamano | que es |
|---|---:|---|
| **EL BLOQUE HUMANO** | **5** | quien decide y quien revisa |
| **EL BLOQUE DEL MAPA** | **4** | probar la maquina tarea por tarea y anotar donde rinde |
| **SUELTO** | **1** | `comprender_alineacion_etica_ia` |

> **Cobertura, como manda el 9.26: 14 de 45.** La particion es **PROVISIONAL** y
> queda dicho con que la puede mover: **un par pendiente en cola, el 1541**, y
> **treinta que no entraron nunca**. Basta una A entre un miembro del bloque
> humano y uno del bloque del mapa para que los dos vuelvan a ser uno, y **hay
> treinta pares donde eso podria estar escondido**.

> **SIN EJECUTAR.** Esto es una medicion, no una adjudicacion. **Ningun nodo se
> toca**, ninguna mesa se sienta, y la decision de si el catalogo quiere dos
> racimos, tres o uno **es del fundador**.

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

### ADJUDICADO EL 14 ago 2026: EL CRUCE 2 DESAPARECE. Son UNA sola mesa

**El fundador adjudica: PUERTAS y PORTAFOLIO dejan de ser dos mesas.** Motivo
escrito: **dos mesas que comparten franja deciden dos veces lo mismo o se
contradicen.**

> **La medicion respalda la adjudicacion, y con una cifra que no estaba tomada.**
> La nomina unida tiene **DOCE aristas internas**, y **OCHO de las doce CRUZAN la
> frontera vieja** entre puertas y portafolio. **El grafo ya las trata como una
> sola familia**; las dos mesas eran una division del papel, no del catalogo.

**LO QUE ESTO DEROGA, y conviene decirlo entero**: el orden recomendado que este
cruce fijaba, *primero se cierra la familia de las puertas y con el superviviente
en la mano se mira el portafolio*, **ya no aplica**. No hay dos mesas que ordenar:
**hay una que se sienta con dieciseis nodos delante.**

**LA NOMINA UNIDA, cerrada: DIECISEIS miembros y CERO candidatos fuera.**

| procedencia | nodos |
|---|---|
| **las puertas** (6) | `sistema_stage_gate`, `stage_gate_system`, `estructura_gates`, `sistema_gates_go_kill`, `asignacion_recursos_en_gates`, `sistema_gestion_recursos_en_gates` |
| **el portafolio** (7) | `portfolio_management`, `gestion_portafolio_formal`, `revision_portafolio_periodica`, `gestion_portafolio_dos_niveles`, `gestion_de_portafolio_gates_go_kill`, `gestion_portafolio_foco`, `equipos_dedicados_de_proyecto` |
| **los TRES que arrastra `sistema_gates_go_kill`** | `requisitos_gates_con_dientes` (801), `gates_go_kill_decision_points` (1038), **`estructura_de_gates`** (765) |

> **El tercer arrastrado aparecio al correr el barrido sobre la union**, no antes:
> `estructura_de_gates` entra por su A con `requisitos_gates_con_dientes`. **Y es
> la CUARTA trampa de identificador del ejercicio**: existe tambien
> `estructura_gates`, sin la particula, y es otro nodo vivo. **Su par SI esta en
> la cola**, el puesto **1524**, asi que este si se va a poder cerrar.

**LA FORMA DE LA MESA UNIDA, vigente al puesto 1200:**

| medida | cuantas |
|---|---:|
| pares posibles | **120** |
| en la cola | 21 |
| **leidos** | **18** |
| **en A** | **15** |
| B / D | 1 (600) / 2 (1014, 1151) |
| pendientes en cola | 3 (1366, 1399, **1524**) |
| **NUNCA ENCOLADOS** | **99** |
| aristas internas | 12, **ocho cruzando la frontera vieja** |

> **QUINCE pares en A entre dieciseis nodos.** Es, con diferencia, **el bloque de
> repeticion mas grande medido en el ejercicio**, y su consolidacion seria la
> mayor del plan.
>
> **Y la reserva se escribe con la cifra**: **99 de los 120 pares nunca entraron a
> la cola.** Lo que se sabe de esta familia sale de **18 lecturas**, o sea del
> **15%** de sus pares. **La mesa se sienta con eso, no con mas.**

---

### REGISTRO DE DEPENDENCIAS ENTRE MESAS

**Abierto el 14 ago 2026, por encargo.** La regla que lo gobierna:

> ## NINGUNA MESA SE SIENTA ANTES QUE LA MESA DE LA QUE DEPENDE.

**Y hay dos formas de depender**, porque no todo lo que va delante es una mesa:

| forma | que significa |
|---|---|
| **MESA depende de MESA** | el veredicto de un par de la primera cambia segun lo que decida la segunda |
| **MESA depende de CIRUGIA** | el veredicto depende de que sobreviva a un destejido, y el destejido no es una mesa: es un acto |

**PRIMER EJEMPLAR, y el que produjo el registro: el 1190.**

| pieza | |
|---|---|
| **la mesa que espera** | la que decida el par **1190**, `formalize_advisory_board` contra `identificar_consejo_asesores` |
| **la mesa de la que depende** | la **junta asesora**, que tiene que decidir el **367**, los dos nodos de identificar |
| **por que** | los dos gemelos **difieren justo en la linea que decide**: uno difiere la formalizacion en su paso 6 y el otro no. Si el superviviente conserva ese paso, formalizar es su hijo (D); si conserva la version de cuatro pasos, formalizar repite (A) |
| **por que NO contradice al 976** | porque el 976 se leyo contra el gemelo que **no** difiere. **Las dos lecturas son correctas sobre nodos distintos** |

**LAS OTRAS DEPENDENCIAS, que ya estaban implicitas en los congelados y aqui se
hacen explicitas.** Salen de una medicion simple: **cuantos congelados cuelgan del
mismo nodo.**

| el nodo | congelados que dependen de su cirugia | nota |
|---|---|---|
| **`producto_minimo_viable`** | **TRES**: 494, 592, 830 | y el **494 es la CURA ACOPLADA MAYOR**, un acto de tres. **El orden interno es: destejer, luego 494, luego 592 y 830** |
| **`voz_del_cliente_voc`** | **TRES**: 724, 755, 827 | tres pares distintos esperando un solo destejido |
| **`ab_testing_optimizacion`** | **DOS**: 738, 1061 | y el **1061 es una costurada contra costurada**, el tercer acto de tres del archivo |

> **OCHO de los quince congelados cuelgan de TRES nodos.** No estan repartidos por
> el catalogo: **estan amontonados.** Y eso cambia la forma del trabajo: **tres
> cirugias desbloquean mas de la mitad de los congelados**, y hacerlas en otro
> orden no rompe nada, pero hacerlas TARDE bloquea ocho pares a la vez.
>
> **La regla, aplicada a esto**: las mesas que tocan esos tres nodos **no se
> sientan hasta que la cirugia este hecha**. No es una recomendacion de eficiencia:
> es que **antes de la cirugia esas mesas no tienen el veredicto que necesitan
> para decidir.**

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

---

## 42. CHECKPOINT DE LOS 1.000

**Cincuenta y ocho pares leidos de una vez, del 943 al 1.000, los cincuenta y ocho
del nucleo.**

### 42.1 EL MARCADOR, recomputado del archivo

| | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **GLOBAL** | **1.000** | **289** | 88 | 5 | 618 | **28,9%** |
| **NUCLEO** | **845** | **288** | 86 | 5 | 466 | **34,1%** |
| compras | 155 | 1 | 2 | 0 | 152 | 0,6% |

**La cola entera son 3.388 pares. Van 1.000: el 29,5%.**

### 42.2 LA CURVA POR CENTENAS: la meseta se rompe hacia abajo

| centena | tasa de A |
|---|---:|
| 201 a 300 | 54,0% |
| 301 a 400 | 51,0% |
| 401 a 500 | 39,0% |
| 501 a 600 | 32,0% |
| 601 a 700 | 21,0% |
| 701 a 800 | 24,0% |
| 801 a 900 | 25,0% |
| **901 a 1.000** | **18,0%** |

> **La centena mas sana de todo el cribado**, y la primera que baja de veinte.
> **La meseta del 21 al 25 que el checkpoint de los 900 describio no era una
> meseta: era el tramo medio de una bajada que sigue.**
>
> **Y el cierre lo dice mas fuerte que el promedio: los ultimos VEINTIDOS pares,
> del 979 al 1.000, dieron CERO A.** Es la racha de sanos mas larga del ejercicio.

**LA PROYECCION SE REVISA, como se prometio.** En el checkpoint de los 900 estimé
entre 550 y 620 duplicados mas en lo que falta, con la meseta del 25%. **Con la
centena nueva en 18%, esa cifra baja**: si el ritmo de las dos ultimas centenas
(21,5% de media) se sostiene sobre los 2.388 pares que faltan, salen **unos 510**;
si sigue bajando, menos.

> **Sigue siendo proyeccion.** Lo que si es medicion es la direccion, y ya lleva
> **siete centenas seguidas** apuntando al mismo lado.

### 42.3 POR QUE ESTA CENTENA ES DISTINTA, y no es azar

**Trece de los veintidos pares finales se resolvieron con LA VARA, y los trece con
la misma forma**: una madre que nombra un paso en una linea y un hijo que trae el
procedimiento entero.

> **Es exactamente la figura que el barrido `paso_contra_nodo.py` salio a contar
> el mismo dia**, y que la muestra pineada midio en **79% de jerarquia sana**.
>
> **Los dos ejes se confirman entre si sin haberse coordinado**: el cribado la
> encuentra par por par y el barrido la cuenta de golpe. **Cuando el cribado entra
> en una zona donde esta figura abunda, la tasa de A se desploma**, porque esta
> figura **no es duplicacion: es jerarquia sin cablear.**

**Y la lectura de fondo del checkpoint es esa:**

> **La cola se ordeno por similitud, y la similitud alta caza duplicados. La
> similitud media caza JERARQUIAS.** Por eso la tasa de A baja: **no es que quede
> menos por arreglar, es que lo que queda es de otra clase**, y la clase que queda
> es la barata.

### 42.4 LO QUE ESTOS CINCUENTA Y OCHO PARES MOVIERON

| que | donde |
|---|---|
| **el SEGUNDO PURO degrada a sub-puro** | puesto **950**: `construccion_de_valor_percibido` entra como cuarto miembro de la ecuacion de valor por el barrido de las A |
| **el racimo de la SUPERVISION DE LA IA pasa a MEZCLADO** | puesto **993**: primer par interno sano, y no es de los cuatro cruzadores |
| **la familia de los CUADRANTES DE MERCADO cierra su cola** | puesto **963**: cinco pares leidos y los cinco en A; le quedan cinco que nunca entraron |
| **el sub-puro de la JUNTA ASESORA avanza a 4 de 6** | puesto **976**, los cuatro en A |
| **`retention_metrics` VUELVE a cura acoplada** | puesto **969**: el gemelo que le faltaba, con correccion declarada sobre mi propia nota del 848 |
| **la fase ADOPT no esta doblada: esta invadida** | puesto **965**: sus dos nodos son sanos entre si, y la duplicacion corre hacia la familia de la tribu |
| **cuarto par cruzado del pivote, y el primero que separa los dos criterios** | puesto **968**: con un nodo por PUERTA sobrevive entero, con un nodo por LIBRO no |
| **octava de las veinte fuera de cola, leida** | puesto **974**, `gestion_cuentas_por_cobrar` |

### 42.5 LA REGLA ADJUDICADA, trabajando dos veces en el cierre

**Los puestos 998 y 999 enfrentan el mismo emblema**, `lienzo_modelo_negocio`, el
nodo de **diecisiete pasos** que repite *completar los nueve bloques* en siete de
ellos.

> **Por POSICION, cualquier solape con ese nodo toca alguna juntura.** Si la
> posicion siguiera siendo test, **los dos pares estarian congelados.**
>
> **Por DEPENDENCIA, los dos son invariantes**: sobreviva la copia que sobreviva,
> el lienzo de modelo de negocio seguira siendo un lienzo distinto del de
> propuesta de valor (998) y seguira siendo el insumo del plan de tecnologia
> (999). **Los dos se emiten y se encolan.**
>
> **La adjudicacion del 13 ago 2026 se paga sola en el mismo dia en que se
> escribio**: dos veredictos que estarian bloqueados estan emitidos, con su
> relectura anotada y sin haber juzgado nada que dependa de la cirugia.

---

## 43. EL TRAMO 1001 a 1036: nace el PRIMER PURO DE CUATRO, y la vara resuelve un tercio

**Treinta y seis pares leidos, los treinta y seis del nucleo.** Acumulado **1.036
de 3.388**, global **28,5%** de A y **nucleo 33,4%**. **El tramo dio 16,7%** (30
D, 6 A).

**Y la cifra nueva que el banco 9.19 manda reportar: TRECE de los treinta y seis
se resolvieron con LA VARA, el 36%.**

> **Las dos juntas dicen lo que ninguna dice sola.** Una tasa de A del 16,7% con
> **un tercio de los pares resueltos por jerarquia** no describe un catalogo
> limpio: describe **un catalogo mal cableado**. La cola sigue en la zona que la
> doctrina nueva nombro.

### 43.1 EL PRIMER PURO DE CUATRO MIEMBROS

**Puesto 1030**, y era la unica lectura que le faltaba a la familia.

| | |
|---|---:|
| racimo | **la competencia entre inversores** |
| miembros | **4**: `construccion_de_leverage`, `estrategia_competencia_vcs`, `leverage_en_negociacion_con_vcs`, `gestion_multiples_term_sheets` |
| pares posibles | **6** |
| **leidos** | **6** |
| **en A** | **SEIS de SEIS** |

> **PURO por la condicion dura, y el primero de CUATRO miembros del archivo**,
> despues de tres puros de tres. **La prediccion de la tanda R23 se cumple**: alli
> quedo escrito que si el 1030 salia A, esta familia seria el primer puro de ese
> tamano.
>
> **Y su historia es la del banco 9.15**: se declaro puro con **tres** miembros
> (contador por nombre), se degrado a sub-puro cuando el **barrido de las A**
> destapo el cuarto, **y ahora vuelve a puro con el tamano correcto.** El puro no
> era falso: **estaba mal contado.**

### 43.2 LA COLA EN ZONA DE JERARQUIAS, con nombres

**Los trece resueltos con la vara, y la madre que nombra en cada uno:**

| puesto | la madre nombra en una linea | el hijo trae el procedimiento |
|---:|---|---|
| 1001 | *mapea los tipos de cliente* | el retrato con entorno, rutina y decisor aparte |
| 1002 | *clasifica el pivote segun el catalogo* | el reempaquetado sin redisenar el producto |
| 1007 | *pon el esfuerzo en la calidad de tus preguntas* | la tesis de investigar con su medicion |
| 1009 | *prueba la importancia del problema* | la deteccion de fuga con trafico frio |
| 1012 | *selecciona el medio segun la fase* | los seis canales aplicados a Assess con su piloto |
| 1013 | *elige la forma segun la complejidad* | pequeno en inspiracion, grande en implementacion |
| 1020 | *disena acciones para cada una de las ocho fases* | la fase Acclimate entera |
| 1021 | *disena las preguntas en orden SPIN* | las preguntas de implicacion con su mapeo |
| 1022 | *identifica el rol de tu contacto* | la jerarquia real de la firma |
| 1023 | *define quien influye y decide* | el mapa de acceso, los patrones de peligro, el flujo |
| 1024 | *responde las seis preguntas de Chopra y Meindl* | entrevistar, comparar y clasificar el segmento |
| 1025 | *organiza tus metricas por cohortes* | el analisis de cohortes entero |
| 1029 | *prueba con experimentos si le importa* | el guion de la prueba de solucion |

> **Trece madres que nombran y trece hijos que ejecutan.** **De los trece, once no
> tienen arista.** Es la bolsa del barrido `paso_contra_nodo.py` apareciendo par
> por par en la cola, exactamente como la doctrina 9.19 predice.

### 43.3 Lo demas del tramo

> **1. TRES ARISTAS QUE FALTAN ENTRE ARTEFACTOS QUE SE CONSUMEN** (puestos
> **1016**, **1036** y **1002**): `validar_modelo_negocio_hechos` **empieza
> reuniendo** las capturas que otros dos nodos producen, y no enlaza con ninguno
> de los dos. **El catalogo describe una cadena de trabajo y el grafo no la
> conoce.**
>
> **2. El CRUCE portafolio-puertas se acota** (puesto **1014**): `sistema_gates_go_kill`
> contra `gestion_portafolio_formal` sale **sano y con arista**. **El cruce no es
> entre las dos familias: es de un nodo concreto**, `gestion_de_portafolio_gates_go_kill`.
> **La mesa 1 tiene ahora el problema mas chico de lo que parecia.**
>
> **3. Decima de las VEINTE fuera de cola, leida** (puesto **1025**,
> `keep_customers_strategy`), y **no bloquea**: el solape cae en su segundo bloque
> y el veredicto es invariante.
>
> **4. `realizar_pruebas_pasa_no_pasa` llega a CATORCE pares leidos y TRECE
> sanos.** Sigue siendo el nodo mas leido sin duplicarse de todo el cribado.

---

## 44. EL TRAMO 1037 a 1050: la vara no viene repartida

**Catorce pares leidos, los catorce del nucleo.** Acumulado **1.050 de 3.388**,
global **28,3%** de A y **nucleo 33,1%**. **El tramo dio 14,3%**, y **DOS de los
catorce se resolvieron con la vara, el 14%.**

### 44.1 LA CIFRA DE LA VARA NO ES ESTABLE, Y ESO ES INFORMACION

**Los dos tramos desde el checkpoint de los 1.000, uno al lado del otro:**

| tramo | pares | tasa de A | resueltos con la vara |
|---|---:|---:|---:|
| 1001 a 1036 | 36 | 16,7% | **13 (36%)** |
| **1037 a 1050** | 14 | 14,3% | **2 (14%)** |
| **acumulado 1001 a 1050** | **50** | **16,0%** | **15 (30%)** |

> **La tasa de A se mantuvo y la de la vara se desplomo a la mitad.** Si las dos
> midieran lo mismo, se moverian juntas. **No lo hacen.**

> **LO QUE ESTO PRECISA DE LA DOCTRINA 9.19, y hay que decirlo porque la matiza**:
> la figura de la jerarquia **no viene repartida por la cola: viene en racimos**.
> El tramo anterior cayo en una zona de madres con hijos (customer development,
> Coleman, SPIN, cadena de suministro); este cayo en una zona de **pares
> hermanos**, dos etapas del mismo proceso o dos instrumentos del mismo libro.
>
> **La cifra de la vara sirve, pero por TRAMO y no por par.** Un tramo con 36% de
> vara dice *estamos en zona de jerarquias*; uno con 14% dice *volvimos a zona de
> hermanos*. **Es un indicador de POSICION en la cola, no una propiedad del
> catalogo.**

### 44.2 EL DIAGNOSTICO QUE NO ENLAZA CON NINGUNO DE SUS DOS REMEDIOS

**Puesto 1046, y con el 994 son dos.** `efecto_bullwhip` termina su ultimo paso
diciendo **usa estos numeros para decidir si vale la pena invertir en compartir
datos o coordinarte mejor con tus proveedores**.

| el remedio | puesto | arista |
|---|---:|:---:|
| `compartir_datos_cadena_suministro` | 994 | **NO** |
| `mitigacion_efecto_latigo` | **1046** | **NO** |

> **El nodo nombra la decision y el catalogo tiene DOS nodos que la ejecutan, y no
> hay arista con ninguno.** Es la forma del barrido `paso_contra_nodo.py` con una
> vuelta de tuerca: **no falta una arista, faltan dos**, y las dos salen del mismo
> paso.

### 44.3 DOS PAREJAS QUE EL REDACTOR DEBERIA ENLAZAR, NO FUNDIR

> **1. Los dos extremos de la misma transicion** (puesto **1043**):
> `equipo_customer_development` manda **quitar** los titulos de ventas y marketing
> y liderar uno mismo; `company_building` manda **formarlos** y contratar a quien
> tenga experiencia de escala. **Uno deshace lo que el otro monta**, y esa es
> exactamente la frontera del metodo dicha desde los dos lados. **Sin arista.**
>
> **2. Cuando hay reunion contra que pasa dentro** (puesto **1042**):
> `aceleracion_de_gates` dice cuando saltarse la reunion de decision;
> `protocolo_reuniones_gate` dice como hacerla bien cuando toca. **Complementarios
> perfectos, y esta vez SI hay arista.**

### 44.4 Lo demas del tramo

> **1. El frente del Stage-Gate suma otra A puertas adentro** (puesto **1038**),
> y con ella **doce nodos leidos**. La mesa 1 sigue creciendo sin convocarse. **Lo
> unico que este par anade de contenido es una quinta salida del gate**, *seguir
> pero con condiciones*, que el otro nodo no lista.
>
> **2. El racimo de la SUPERVISION DE LA IA suma su quinto par interno** (puesto
> **1041**, **A**), y sigue **MEZCLADO** con cuatro A y un sano. **Lo mas duro del
> par y lo que hay que salvar**: hacer pruebas periodicas con casos **disenados
> para que la IA falle** y medir si el equipo detecta el error.
>
> **3. Tercera lectura del nodo de preguntas de implicacion contra un nodo de
> secuencia** (puesto **1049**), y las tres sanas. **Pero la arista solo existe en
> una de las tres** (la del 1021). **El mismo hijo, tres madres, un cable.**

---

## 45. EL BARRIDO DE CONFIRMADAS CONTRA LAS A: la cifra, de una vez

**Encargo aprobado el 13 ago 2026. Solo lectura, sin adjudicar.** Cruza las
**46 costuras CONFIRMADAS** del cierre del instrumento contra **todos los
veredictos A vigentes** del archivo, mas las **tres fuera de cola con anatomia
escrita**.

### 45.1 EL METODO, y por que la cifra es fiable

**Las confirmadas se extrajeron de las tablas de veredicto de la ficha con un
patron unico**, y el conteo cuadra con su propio marcador: **46 confirmadas y 82
falsas, 128 en total.** No es una lista escrita a mano: **es la ficha leida.**

**Las tres fuera de cola que entran**: `retention_metrics`,
`procesamiento_paralelo_con_espirales` y `metricas_de_adquisicion_activacion`,
que son las unicas de los veinte con anatomia verificada. **Total mirado: 49.**

### 45.2 LA CIFRA

| clase de cura | costuras | que significa |
|---|---:|---|
| **SIN GEMELO** | **32** | no tienen ni una A. **Su arreglo es solo destejido**: un acto |
| **CONTRA GEMELO SANO** | **13** | destejer y fundir **en el mismo acto**: dos movimientos |
| **CONTRA COSTURADA** | **4** nodos en **2 pares** | destejer los dos **y solo entonces decidir la fusion**: tres movimientos |
| **TOTAL con gemelo** | **17** | |

> **DIECISIETE costuras necesitan cura acoplada, no doce.** El goteo llevaba
> **catorce** encontradas de una en una, cuando una relectura las cruzaba. **El
> barrido encuentra tres mas y las encuentra todas juntas.**

### 45.3 LAS TRES QUE EL GOTEO NO HABIA ENCONTRADO

| costura | sus gemelos | por que no aparecio antes |
|---|---|---|
| **`brainstorming_divergente`** | **TRES**: `brainstorming_efectivo` (823), `reglas_brainstorming` (834), `generar_multiples_opciones` (844) | los tres pares se leyeron **como pares del racimo del brainstorming**, no como pruebas de gemelo |
| **`future_scenarios_planning`** | `escenarios_futuros` (711) | su par se leyo antes de que la cura acoplada existiera como figura |
| **`plan_de_adquisicion_acquire`** | `plan_acquire_activate` (344) | el puesto 344 **cito su clase de costura** y **no dio el paso** de declarar el ejemplar |

> **La primera es la mas cara del archivo y nadie la habia contado.**
> `brainstorming_divergente` tiene **TRES gemelos**: su cura acoplada no es de dos
> nodos, **es de CUATRO en un solo acto**. Y ademas **es el injerto de Mollick**,
> o sea que la decision de fuente tambien la toca. **Es el nodo con mas frentes
> encima de todo el catalogo.**

### 45.4 LOS DOS ACTOS DE TRES, y los dos ya estaban nombrados

| par | los dos nodos | puesto |
|---|---|---:|
| **el mapa contado dos veces** | `blueprint_de_experiencia` y `customer_journey_mapping` | **341** |
| **la cura acoplada mayor** | `producto_minimo_viable` y `principio_calidad_mvp` | **494** |

> **El barrido confirma que son exactamente dos y no mas.** Los dos ya estaban
> registrados, **y el barrido prueba que no hay un tercero escondido.** Es la clase
> mas cara y el catalogo solo la tiene dos veces.

### 45.5 LOS CONGELADOS DE ESTE GRUPO, y su motivo

| puesto | por que congela |
|---:|---|
| **494** | **la dependencia es directa**: si el destejido conserva la narracion de la calidad el par deja de repetir; si conserva la del conjunto minimo, sigue |
| **738** | los **dos** nodos de A/B estan averiados y **el solape cruza las dos junturas** |

> **Los demas pares de este grupo estan EN COLA SIN CONGELAR** (361, 374, 386,
> 392, 452, 492, 969): en todos ellos **el solape cae en el bloque que sobrevive**
> y el veredicto es invariante. **La regla de la dependencia deja congelados solo
> dos de diecisiete.**

### 45.6 LO QUE EL BARRIDO NO HACE, y hay que decirlo

> **No adjudica.** Las diecisiete siguen necesitando que alguien decida el orden y
> el destino de cada material. **Lo unico que cambia es que ahora se sabe cuantas
> son antes de empezar**, en vez de irlas descubriendo mientras se trabaja.
>
> **Y deja una leccion de metodo para el resto del plan**: **doce de las
> diecisiete se encontraron de una en una a lo largo de veinte relecturas.** El
> barrido tardo una consulta. **Cuando una figura se puede cruzar mecanicamente,
> cruzarla es mas barato que esperarla.**

---

## 46. CHECKPOINT DE LOS 1.100: el tramo 1051-1100 completo

### 46.1 EL MARCADOR

| medida | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **GLOBAL** | **1.100** de 3.388 | 304 | 88 | 6 | 702 | **27,6%** |
| **NUCLEO por separado** | **945** | 303 | 86 | 6 | 550 | **32,1%** |
| **el tramo 1051-1100** | **50** | **7** | 0 | **1** | 42 | **14,0%** |

**Sin huecos: 1 a 1.100 registrados uno por uno.** Ningun nodo se toco.

### 46.2 LAS DOS SERIES QUE PIDE EL ENCARGO, y van en direcciones contrarias

| tramo | leidos | tasa de A | **pares resueltos con LA VARA** |
|---|---:|---:|---:|
| **901-1000** | 100 | **18,0%** | 31 (**31%**) |
| **1001-1050** | 50 | **16,0%** | 15 (**30%**) |
| **1051-1100** | 50 | **14,0%** | **19 (38%)** |

> **La tasa de A baja por tercer tramo seguido y la de la vara sube.** Es
> exactamente lo que anuncio el 9.19 y por eso la cifra de la vara se lee por
> tramo: **casi cuatro de cada diez pares de este tramo se resolvieron citando la
> linea contra el procedimiento.** No es que el catalogo repita menos: es que la
> cola dejo de traer duplicados y empezo a traer jerarquias, que se resuelven con
> una regla y no con una fusion.
>
> **Y la cifra NO SE PROYECTA.** Vale para donde va la cola hoy.

**Solo 8 de los 50 pares tenian arista.** El resto son jerarquias sanas sin cable:
la bolsa del 9.19 sigue engordando por su lado.

### 46.3 LO QUE ESTE TRAMO CORRIGE DEL BARRIDO, el mismo dia

> **El puesto 1061 es la TERCERA costurada contra costurada del archivo**:
> `ab_testing_optimizacion` contra `optimizacion_embudo_get_customers`, **las dos
> confirmadas**. El barrido de la seccion 45 conto **exactamente dos** actos de
> tres, el 341 y el 494, **y ese negativo queda corregido: son tres.**
>
> **Por que el barrido no lo vio, dicho sin adornos**: el barrido cruza las
> confirmadas contra las **A vigentes en el momento de correrlo**, y esta A no
> existia todavia; se registro horas despues, en este mismo tramo. **El
> instrumento no fallo, se quedo viejo.** La leccion no es que el barrido sea
> malo: es que **un barrido contra un archivo que sigue creciendo caduca**, y hay
> que volver a correrlo cuando la cola avance. Queda anotado como recordatorio de
> la seccion 45, no como enmienda a su metodo.

Con el 1061, la cifra viva es **DIECISIETE costuras con gemelo (corregido el 14 ago 2026 por el cierre transitivo, seccion 54 del informe: el 1061 unio dos costuras que YA estaban dentro de las diecisiete, asi que cambio la clase del acto y no la cuenta)** y **tres actos de tres**.

### 46.4 LA FIGURA NUEVA: LA VARA EN LOS DOS SENTIDOS (puesto 1077, clase C)

`herramientas_de_activacion_web` contra `diseno_landing_page`, del mismo libro y
**con arista**. **Cada uno es hijo del otro, y ninguno repite al otro.**

| sentido | la linea | el procedimiento |
|---|---|---|
| **A hacia B** | herramientas paso 5: *crear paginas de aterrizaje segun la fuente del trafico* | **todo** `diseno_landing_page`: contenido segun origen, tono del anuncio que trajo al visitante, una sola llamada a la accion, diseno limpio, navegacion corta |
| **B hacia A** | landing paso 4: *incluir demos de menos de un minuto, pruebas gratuitas o calculadoras* | **todo** `herramientas_de_activacion_web`: el demo funcional, las pruebas limitadas con correos de seguimiento, el contacto directo, los videos de bienvenida con moderacion |

> **Lo que la figura ensena: la vara es una relacion entre LINEAS, no entre
> NODOS.** Dos nodos pueden ser cada uno hijo del otro sin que ninguno repita al
> otro, porque **la linea que uno expande no es la linea que el otro expande.**
> Es la primera vez en 1.100 pares que aparece, y por eso el par es **C, sano con
> figura**, y no D. **Queda propuesta al banco; no la adjudico.**

### 46.5 LO QUE CIERRA DEL TRATAMIENTO DE COLEMAN (puesto 1068)

**La serie de los seis medios esta instanciada por fase, y las instancias se
repiten entre ellas.** Con lo que ya se sabia, el cuadro queda completo:

| puesto | que probo |
|---:|---|
| **948** | los **dos nodos generales** de la serie repiten entre si |
| **1012** | la instancia de **Assess** es **hija** del general: sana |
| **1068** | dos instancias, **Celebracion** y **Activate**, **repiten entre si**: A |

> **La serie no esta duplicada solo arriba: esta duplicada tantas veces como fases
> la instancien.** Lo unico propio de cada instancia son uno o dos gestos de
> diagnostico, la nota del uno al diez en Activate y el mensaje atado al hito en
> Celebracion. El procedimiento, elegir dos o tres canales, preparar contenido y
> medir, es el mismo texto en las dos.

### 46.6 LA ZONA DE BLANK: cuatro madres y casi ningun cable

**El tramo cayo casi entero en el metodo de Blank**, y deja una medicion de
cableado que vale mas que cualquier veredicto suelto.

| madre | hijos leidos en este tramo | veredictos | aristas |
|---|---|---|---:|
| **`filosofia_customer_validation`** | 1079, 1084, 1086, **1096** | tres sanos y **una A** | **cero** |
| **`customer_discovery_cuatro_fases`** | 1083 (fase 1), 1094 (fase 4) | dos sanos | **cero** |
| **`customer_discovery_phase2_problem_test`** | 1092 | sano | **cero con su hijo** |

> **`filosofia_customer_validation` es una madre con cuatro hijos verificados y
> ni un solo cable**, y el mas visible es el 1086: `decision_pivotar_o_proceder`
> es literalmente el paso siguiente de la filosofia y no hay arista entre ellos.
>
> **Y el 1092 deja el caso mas fino de la bolsa.** El nodo indice **si tiene
> cableado**, cuatro previos y cuatro siguientes distintos, **pero ninguno de
> ellos es uno de los tres nodos cuyos titulos son sus propios pasos.** No es un
> nodo aislado: **es un nodo cableado hacia los lados y no hacia sus hijos.** Es
> una forma de falta de arista que el conteo de grado nunca hubiera encontrado,
> porque el grado sale bien.

### 46.7 EL OTRO LADO: los libros que si jerarquizan

| libro | hijos leidos | resultado |
|---|---:|---|
| **Rackham, SPIN** | 5 (899, 1021, 1049, 1067, **1081**) | **cinco sanos, cinco de cinco** |
| **Cooper, Winning at New Products** | 1099 | **sano y con arista** |

> **Rackham es el libro mejor jerarquizado del archivo hasta aqui.**
>
> **Y el 1099 es la prueba del 9.12 al derecho**: la escalera de Cooper **si
> sube**, y se ve en la misma cifra medida con dos profundidades a proposito,
> **plazo de recuperacion en la puerta** y **valor presente neto con
> sensibilidad** en la etapa. El gasto crece solo despues de que la puerta lo
> autorice, que es para lo que sirve una puerta.

### 46.8 UN MARCO COMPARTIDO NO ES UN MARCO DUPLICADO (puesto 1097)

`customer_development_process` (Osterwalder) contra `modelo_customer_development`
(Blank): **el mismo modelo de cuatro pasos en dos libros**, y aun asi **D**.

> Uno dice **que son** las cuatro etapas y las describe; el otro dice **como se
> recorren**, con la senal de alto, la velocidad de escape y el permiso de
> retroceder, **y nunca dice cuales son.**
>
> **La prueba que decide: fundirlos no borraria material, lo SUMARIA.** El
> contenido de cada uno es exactamente el hueco del otro. **Ahi esta la frontera
> entre un marco compartido por dos fuentes y un marco duplicado**, y conviene
> tenerla escrita porque la cola va a traer mas casos de dos libros contando lo
> mismo.

### 46.9 SOSPECHA REGISTRADA, no adjudicada

> En el puesto **1074** se leyo un nodo llamado **`fase_assess`** y en el **1087**
> otro llamado **`fase_assess_experiencia_cliente`**, **del mismo libro y de la
> misma fase**. Los dos pares salieron sanos contra terceros, pero **son dos nodos
> para la misma fase de Coleman** y quedan marcados como **candidatos fuertes a
> repetir entre si** cuando su propio par salga en la cola. No lo adelanto: lo
> anoto para que no se pase.

### 46.10 EL SALDO DEL CHECKPOINT

> **Mil cien pares leidos uno por uno, sin huecos y sin tocar un nodo.** La tasa
> del nucleo bajo de **54%** en la centena 3 a **32,1%** acumulada, **y el tramo
> suelto marca 14,0%**. La doctrina hizo ese trabajo sola: **cada punto que baja
> es un par que antes se hubiera cobrado como fusion y hoy se resuelve citando una
> regla.**
>
> **Y este tramo deja el aviso mas util del checkpoint**: el barrido de la seccion
> 45, corrido el mismo dia, **ya estaba viejo cuando se escribio.** Los
> instrumentos que cruzan contra el archivo hay que volver a correrlos, porque el
> archivo sigue creciendo debajo de ellos.

---

## 47. TRAMO 1101-1157: dos familias medidas, un puro nuevo y una trampa de identificador

### 47.1 EL MARCADOR

| medida | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **GLOBAL** | **1.157** de 3.388 | 311 | 88 | 6 | 752 | **26,9%** |
| **NUCLEO por separado** | **1.002** | 310 | 86 | 6 | 600 | **30,9%** |
| **el tramo 1101-1157** | **57** | **7** | 0 | 0 | 50 | **12,3%** |

**Sin huecos. Ningun nodo se toco.** El nucleo cruza los **mil pares leidos**.

### 47.2 LAS DOS SERIES, cuarto tramo seguido

| tramo | leidos | tasa de A | **pares resueltos con LA VARA** | con arista |
|---|---:|---:|---:|---:|
| 1001-1050 | 50 | 16,0% | 15 (30%) | 11 |
| 1051-1100 | 50 | 14,0% | 19 (38%) | 8 |
| **1101-1157** | **57** | **12,3%** | **21 (37%)** | **17** |

> **La tasa de A baja por cuarto tramo y la vara se sostiene arriba del tercio.**
> Y aparece un dato nuevo: **17 de 57 pares tenian arista**, el doble de
> proporcion que el tramo anterior. La cola entro en zonas mejor cableadas
> (Rackham, Venture Deals, los formularios de proyecto) y eso se ve en la cifra.

### 47.3 PURO NUEVO, y certificado por los dos instrumentos: EL COMPROMISO CONTADO TRES VECES

**Racimo de Rackham. Los tres nodos dicen como conseguir que el cliente se
comprometa, y los tres repiten entre si.**

| nodo | pasos |
|---|---:|
| `obtencion_compromiso` | 4 |
| `obtencion_de_compromiso` | 5 |
| `obtencion_compromiso_venta` | 4 |

**LOS DOS INSTRUMENTOS, como manda el estandar de certificacion:**

| instrumento | resultado |
|---|---|
| **contador** (`contar_nombre.py "obtencion de compromiso" "obtener compromiso" "compromiso del cliente"`) | 10 nodos vivos, de los que **solo DOS son miembros**; los otros ocho **mencionan** el compromiso sin serlo. **Y se le escapa el tercero** |
| **barrido de las A** | **TRES A vigentes** (197, 222, 463) y **CERO candidatos fuera de la nomina** |

> **TRES pares posibles, TRES en la cola, TRES leidos y los TRES en A.** No es un
> sub-puro: **todos los pares estan leidos**, asi que no es una promesa (banco
> 9.16), es un resultado.
>
> **Y el contador vuelve a fallar por el mismo motivo del 9.20**: el miembro que
> se le escapa es **`obtencion_compromiso`**, que no lleva la particula *de* y por
> eso no casa con el termino buscado. **Es justo el nodo que cierra el triangulo.**
> Con el contador solo, este puro se habria declarado de dos miembros y con un
> par: la mitad de lo que es.
>
> **CERO aristas internas entre tres nodos que repiten entre si.** El caso mas
> limpio del archivo de lo que el 9.6 llama la arista que falta.

### 47.4 EL RACIMO MAS GRANDE DEL TRAMO: LA GESTION DEL PORTAFOLIO

**Cooper otra vez, y es grande.** Nomina levantada por el **barrido de las A**,
que es lo unico que la levanta entera: el contador de *portafolio* y *portfolio*
da **43 nodos vivos**, casi todos meros mencionadores.

| nodo | pasos | por que es miembro |
|---|---:|---|
| `portfolio_management` | 6 | **el centro: CUATRO A** (574, 853, 967, 1119) |
| `gestion_portafolio_formal` | 6 | tres A (468, 574, 616) |
| `gestion_de_portafolio_gates_go_kill` | 5 | tres A (616, 967, 488) |
| `revision_portafolio_periodica` | 5 | A 468 |
| `gestion_portafolio_dos_niveles` | 4 | A 853 |
| `gestion_portafolio_foco` | 5 | A 802, A 1119 |
| `equipos_dedicados_de_proyecto` | 6 | **A 802**, y ver abajo |

**LA FORMA, vigente al puesto 1157: 21 pares posibles, 10 en la cola, 9 leidos.**

| clase | pares |
|---|---|
| **A** | **SIETE**: 468, 574, 616, 802, 853, 967, 1119 |
| **B** | uno: 600 |
| **D** | uno: **1151**, leido en este tramo |
| pendiente | 1366 |

> **Siete A entre siete nodos y CERO aristas internas.** Es el bloque de
> repeticion mas grande medido en el ejercicio y no tiene ni un cable.
>
> **Y es MEZCLADO, no puro**, y lo prueba justo el par de este tramo: el **1151**,
> `gestion_portafolio_dos_niveles` contra `revision_portafolio_periodica`, sale
> **D** porque el segundo es el procedimiento de una linea del primero. **Dos
> miembros de un racimo pueden ser madre e hijo entre si**, y eso es exactamente
> lo que hace que el racimo no sea puro.

**EL MIEMBRO QUE NO PARECE MIEMBRO, y es el hallazgo del puesto 1156.**

> `equipos_dedicados_de_proyecto` se llama por el EQUIPO y repite con
> `gestion_portafolio_foco` (puesto 802). **Su asunto real es elegir pocos
> proyectos y cortar el resto: es podar el portafolio con titulo de equipo.**
>
> Por eso el **1156** sale D: leido contra `equipo_multifuncional`, que **tambien
> tiene A vigente** (672, contra `equipo_multifuncional_real`), resulta que **los
> dos son gemelos de familias distintas.** **Dos nodos que por el titulo parecen
> hermanos y por la evidencia son de casas distintas**, y eso solo lo dice el
> barrido de las A.

**DONDE SE DESDIBUJA LA FRONTERA, y lo digo sin cerrarlo.** Admitir
`sistema_gates_go_kill` como octavo miembro **arrastra tres candidatos mas** por
sus propias A: `estructura_gates` (356), `requisitos_gates_con_dientes` (801) y
`gates_go_kill_decision_points` (1038).

> **Ahi el portafolio se toca con una familia de COMPUERTAS.** Decidir si son una
> familia o dos **es trabajo de lectura, no de conteo**, y por eso la nomina
> queda declarada en **SIETE** con la puerta anotada. El 9.20 lo dice: el script
> dice donde mirar, la pertenencia se decide leyendo.

### 47.5 LA TRAMPA DEL IDENTIFICADOR, y aparece TRES veces en 57 pares

**Tres parejas de nodos vivos cuyos identificadores se diferencian en una
particula o una letra.**

| los dos identificadores | que son | como se supo |
|---|---|---|
| `estrategia_innovacion_producto` (5 pasos) y **`estrategia_de_innovacion_producto`** (7 pasos) | **NODOS DISTINTOS**: uno es la estrategia de arenas y recursos, el otro una doctrina de valentia. Contra el mismo tercero dan **A** (1121) y **D** (1129) | leyendo los dos, tras el choque de veredictos |
| `obtencion_compromiso` y `obtencion_de_compromiso` | **GEMELOS PROBADOS**: A en el puesto 463, y son dos tercios del puro de la seccion 47.3 | barrido de las A |
| `usuarios_extremos_edge_cases` y `usuarios_extremos_insights` | **GEMELOS PROBADOS**: A en el puesto 426 | barrido de las A |

> **La particula no dice nada por si sola.** En un caso separa dos nodos que de
> verdad son distintos; en los otros dos separa dos copias del mismo. **Por eso
> no se puede juzgar por el nombre**, ni para unir ni para separar.
>
> **Y el primer caso deja un pendiente que la cola no puede resolver**: entre
> `estrategia_innovacion_producto` y `estrategia_de_innovacion_producto` **no hay
> par en la cola.** Es el segundo caso del ejercicio, con el racimo de las
> disruptivas del R30, de una pareja que el cribado no va a decidir nunca.

### 47.6 EL INDICE CON DOS HIJOS PARA LA MISMA FASE, y una correccion de mi metodo

**Coleman.** `ocho_fases_experiencia_cliente` es el indice de las ocho fases. En
este tramo salieron **dos hijos suyos para la MISMA fase, la cuarta**:

| puesto | el hijo | arista con el indice |
|---:|---|---|
| **1139** | `fase_activate_primera_impresion` | **NO** |
| **1141** | `fase_activate` | **SI** |

> **Los dos ya estaban probados como gemelos**: el puesto **183** registro **A**
> entre ellos. Y hay un tercero que instancia la misma fase por la serie de
> medios, `seis_herramientas_comunicacion_fase_activate` (puesto 1068). **El
> indice esta cableado a uno de sus dos hijos gemelos y suelto del otro.**

**CORRECCION DECLARADA, y es de metodo, no de veredicto.** En el puesto **1087**
de la sesion anterior anote como **sospecha** que `fase_assess` y
`fase_assess_experiencia_cliente` podian repetir entre si.

> **El barrido de las A lo contesta en una consulta**: el puesto **373** ya tenia
> **A** entre `fase_assess_experiencia_cliente` y un tercer nodo,
> `fase_assess_ciclo_cliente`. **Debi correr el barrido en vez de anotar una
> sospecha.** El 9.20 dice que corre **siempre**, no solo cuando toca declarar una
> nomina, y esta es la prueba de por que: **una sospecha escrita es trabajo
> aplazado; un barrido es trabajo hecho.**

### 47.7 LA FAMILIA DEL PROMPTING avanza dos pares, y los dos sanos

Levantada en la tanda R30 a partir del 514. **Dos de los cinco pendientes salieron
en este tramo:**

| puesto | el par | clase | por que |
|---:|---|:---:|---|
| **1125** | `ingenieria_de_prompts_efectiva` contra `prompting_cadena_de_pensamiento` | **D** | tecnicas distintas; la madre **no nombra** la cadena de pensamiento |
| **1144** | `ingenieria_de_prompts_efectiva` contra `prompting_por_persona_ia` | **D** | el hijo trae el procedimiento de la **linea 1** de la madre |

> **La forma que va saliendo**: `ingenieria_de_prompts_efectiva` es la madre,
> `asignacion_persona_ia` **la repite** (A del 514) y `prompting_por_persona_ia`
> **la continua**. **El puesto que decide si los dos ultimos son ademas gemelos
> entre si es el 1175**, que sigue en la cola. No lo adelanto.

### 47.8 LO QUE SE SOSTIENE DE TRAMOS ANTERIORES

| medicion | como queda |
|---|---|
| **`filosofia_customer_validation`** | **QUINTO** par (1137). Cuatro hijos sanos, un repetidor, **cinco pares y CERO aristas** |
| **Rackham, madres e hijos** | **siete de siete sanos** (899, 1021, 1049, 1067, 1081, 1130, 1133) mas dos mas en este tramo (1149, 1150). El **1146 es A**, pero **no es par de madre e hijo**: son dos nodos laterales |
| **la mesa del PIVOTE** | **NO gana miembro.** El puesto **1140** salio **D**, no A: `actualizar_modelo_de_negocio_pivot_o_proceed` lleva **cinco veredictos y los cinco D**. **La nomina de siete queda intacta** |
| **`lienzo_modelo_negocio`** | leido dos veces (1123, 1136), las dos sanas por la vara y las dos **invariantes** pese a ser la costura mas averiada del archivo, **17 pasos** con los nueve bloques mandados completar **cuatro** veces |

### 47.9 EL SALDO

> **Mil ciento cincuenta y siete pares, y el nucleo pasa de los mil.** Lo que este
> tramo deja no son veredictos sueltos: **son dos familias que nadie habia
> contado**, una de tres que resulta ser **PURO** y otra de siete que es el
> **bloque de repeticion mas grande medido**, y las dos con **cero aristas
> internas**.
>
> **Las dos las levanto el mismo instrumento, y no fue el contador.** En el puro,
> el contador se comio al miembro que cierra el triangulo; en el racimo grande,
> el contador devolvia 43 nodos casi todos falsos. **El barrido de las A no fallo
> en ninguno de los dos.**

---

## 48. LA NOMINA DEL PORTAFOLIO, contada con los dos instrumentos

**Encargo del 14 ago 2026. Vigente al puesto 1157**, por el banco 9.21.

### 48.1 LOS DOS INSTRUMENTOS

| instrumento | resultado |
|---|---|
| **contador** (`contar_nombre.py "portafolio" "portfolio"`) | **43 nodos vivos**, 115 menciones. **Casi todos son mencionadores**: nodos de precios, de redes profesionales, de clausulas de riesgo y hasta uno de `environmental` que dicen la palabra sin ser de la familia |
| **barrido de las A** | **SIETE miembros** y **UN candidato fuera de nomina**: `sistema_gates_go_kill`, por el puesto 488 |

> **El contador solo habria dado una lista de 43 para leer a mano.** El barrido da
> siete con su evidencia. **Es el mismo reparto de trabajo del 9.20**: el contador
> dice donde mirar, el barrido dice quien es.

### 48.2 LA NOMINA: siete miembros, y quien los levanta

| nodo | pasos | sus A |
|---|---:|---|
| **`portfolio_management`** | 6 | **CUATRO**: 574, 853, 967, 1119 |
| `gestion_portafolio_formal` | 6 | tres: 468, 574, 616 |
| `gestion_de_portafolio_gates_go_kill` | 5 | tres: 488, 616, 967 |
| `gestion_portafolio_foco` | 5 | dos: 802, 1119 |
| `gestion_portafolio_dos_niveles` | 4 | una: 853 |
| `revision_portafolio_periodica` | 5 | una: 468 |
| `equipos_dedicados_de_proyecto` | 6 | una: 802, **y se llama por el equipo, no por el portafolio** |

### 48.3 LA CUENTA DE PARES, completa

| medida | cuantos |
|---|---:|
| **pares posibles** | **21** |
| **en la cola** | **10** |
| **leidos** | **9** |
| **pendientes en cola** | **1** (el 1366) |
| **NUNCA ENCOLADOS** | **11** |

| clase | pares |
|---|---|
| **A** | **SIETE**: 468, 574, 616, 802, 853, 967, 1119 |
| **B** | uno: 600 |
| **D** | uno: 1151 |

**ARISTAS INTERNAS: CERO.** Siete nodos del mismo libro sobre el mismo asunto,
siete pares que repiten, **y ni un cable entre ninguno**.

### 48.4 NO ES SUB-PURO, Y TAMPOCO ES ESTRELLA. Es MEZCLADO

**El encargo preguntaba si sale sub-puro. No sale, y conviene decir exactamente
por que**, porque las dos cosas que lo impiden son distintas.

| lo que lo impide | cual |
|---|---|
| **un D leido dentro de la familia** | el **1151**: `gestion_portafolio_dos_niveles` contra `revision_portafolio_periodica` es **madre e hija**, no un duplicado |
| **un B sin resolver** | el **600** |

**Y tampoco es una ESTRELLA** (banco 9.23), aunque desde el centro lo parezca:

| cuenta | resultado |
|---|---|
| pares con el centro `portfolio_management` | **4, todos A** |
| pares **entre perifericos** | **5 leidos: TRES en A** (468, 616, 802), un B y un D |

> **Los perifericos SI repiten entre ellos.** No es un centro que repite con cada
> uno: **es una familia que repite de verdad, con una jerarquia sana metida
> dentro.** Es la forma **mas cara** de la tabla de costes del 9.23: pide mesa, y
> la mesa tiene ademas que separar lo que repite de lo que jerarquiza.

### 48.5 LO QUE SI ES, y con esto queda dicho el tamano

> **Once de los veintiun pares NUNCA ENTRARON A LA COLA.** La familia tiene siete
> A sobre **nueve** lecturas, y **la mitad de sus pares no se va a leer nunca en
> este ejercicio.** Cualquier cifra que se le ponga vale sobre lo leido, no sobre
> la familia.
>
> **Aun asi, y con esa reserva escrita: SIETE PARES EN A entre siete nodos es el
> bloque de repeticion mas grande medido hasta el puesto 1157**, y su consolidacion
> seria la mayor del plan. **Lo que no se puede decir es que sea sub-puro**, y
> decirlo cambiaria el tipo de mesa que necesita.

### 48.6 EL CRUCE CON LA MESA DE LAS PUERTAS, por el 488

**Ya estaba escrito en la seccion 13, CRUCE 2. Aqui va solo lo que cambia**, para
no tener el cruce en dos sitios.

| pieza | estado |
|---|---|
| **el par que une los dos racimos** | **488**: `gestion_de_portafolio_gates_go_kill` (portafolio) contra `sistema_gates_go_kill` (puertas). **A** |
| **el nodo que une** | `sistema_gates_go_kill`, **y esta duplicado dentro de su propio racimo**: puesto **356** contra `estructura_gates` |
| **el orden ya recomendado** | **primero se cierra la familia de las puertas**, y con el superviviente en la mano se mira el cruce |

> **LO QUE ESTA MEDICION ANADE AL CRUCE**: la nomina del portafolio **no es de
> seis, es de siete**, y el par que une los dos racimos **no es el unico hilo**.
> Admitir `sistema_gates_go_kill` como octavo miembro arrastra **tres candidatos
> mas** por sus propias A: `estructura_gates` (356),
> `requisitos_gates_con_dientes` (801) y `gates_go_kill_decision_points` (1038).
>
> **O sea que las dos mesas no se tocan en un punto: se tocan en una franja.**
> Decidir si portafolio y puertas son una familia o dos **es trabajo de lectura**,
> y el barrido no lo va a contestar: solo dice que la frontera esta ahi.

---

## 49. CHECKPOINT DE LOS 1.200: el nucleo baja del 30 por ciento

### 49.1 EL MARCADOR

| medida | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **GLOBAL** | **1.200** de 3.388 | 313 | 88 | 6 | 793 | **26,1%** |
| **NUCLEO por separado** | **1.045** | 312 | 86 | 6 | 641 | **29,9%** |
| **el tramo 1158-1200** | **43** | **2** | 0 | 0 | 41 | **4,7%** |

**Sin huecos: 1 a 1.200 registrados uno por uno. Ningun nodo se toco.**

> **El nucleo baja del 30 por ciento por primera vez.** Empezo en **54%** en la
> centena 3.

### 49.2 LAS DOS SERIES QUE PIDE EL ENCARGO

| tramo | leidos | tasa de A | **pares resueltos con LA VARA** | con arista |
|---|---:|---:|---:|---:|
| 901-1000 | 100 | 18,0% | 31 (31%) | 6 |
| 1001-1050 | 50 | 16,0% | 15 (30%) | 11 |
| 1051-1100 | 50 | 14,0% | 19 (38%) | 8 |
| 1101-1157 | 57 | 12,3% | 21 (37%) | 17 |
| **1158-1200** | **43** | **4,7%** | **21 (49%)** | 4 |

**Y por centenas, que es como se ve el movimiento de verdad:**

| centena | tasa de A | vara |
|---|---:|---:|
| 901-1000 | **18,0%** | 31% |
| 1001-1100 | **15,0%** | 34% |
| **1101-1200** | **9,0%** | **42%** |

> **La tasa de A cae a la mitad en dos centenas y la vara sube diez puntos.** En el
> ultimo tramo **casi uno de cada dos pares se resolvio citando la linea contra el
> procedimiento**, y solo dos de cuarenta y tres repitieron.
>
> **Y hay que decir lo que esto NO significa**, por el banco 9.19: no significa
> que quede menos trabajo. **Significa que la cola dejo de traer duplicados y trae
> jerarquias**, que se arreglan con una arista y no con una fusion. La cifra es un
> indicador de POSICION EN LA COLA. **No se proyecta.**

### 49.3 EL HALLAZGO DEL TRAMO: el 1190 se congela, y traigo el choque entero

**`formalize_advisory_board` contra `identificar_consejo_asesores` sale D por la
vara, y eso CHOCA con una A ya registrada: el puesto 976 leyo el mismo nodo de
formalizar contra el OTRO nodo de identificar y salio A.** Y los dos nodos de
identificar **son gemelos entre si** (A del puesto 367).

**La diferencia esta medida, y es exactamente la que decide:**

| nodo | pasos | que hace con la formalizacion |
|---|---:|---|
| `identificar_junta_asesores` (el del 976) | **4** | **NO la difiere**. Hace parte del trabajo de formalizar: evaluar el interes de cada uno en **convertirse en asesor formal** y para que areas |
| `identificar_consejo_asesores` (el del 1190) | **6** | **la difiere explicitamente**: su paso 6 dice *formaliza el consejo mas adelante, durante la validacion de clientes* |

> **Uno se solapa con formalizar; el otro le cede el turno.** Por eso el 976 es A y
> el 1190 es D, y **no es una contradiccion: es que los dos nodos de identificar
> difieren justo en la linea que decide.**
>
> **POR ESO SE CONGELA (banco 9.9).** El veredicto del 1190 **depende de lo que
> sobreviva a la fusion del 367**: si el superviviente conserva el paso 6,
> formalizar sigue siendo su hijo y esto es D; si conserva la version de cuatro
> pasos, formalizar pasa a repetir y esto seria A.
>
> **La mesa de la junta asesora tiene que decidir el 367 ANTES de tocar este par**,
> y ese orden no estaba escrito en ninguna parte.

### 49.4 SEGUNDO SUBCONJUNTO ESTRICTO, y el primero que cruza libros (1182)

**Los cuatro pasos de `design_test_repeat` (Osterwalder) estan enteros dentro de
los seis de `desarrollo_en_espiral` (Cooper).** Perdida **cero** y direccion de
fusion **forzada**, igual que el 511.

> **Y lo que le hace a una nomina, medido con el barrido antes de escribir**:
> `design_test_repeat` es miembro del racimo **BUILD-MEASURE-LEARN**, el numero 9
> de la tabla viva, con cinco miembros. **`desarrollo_en_espiral` no tenia NINGUNA
> A hasta este par.** Con esta pasa a **candidato a miembro** por el 9.20, y seria
> **el primero de otro libro** en ese racimo: Cooper entrando en una familia de
> Ries y Osterwalder. **Queda como candidato levantado con su evidencia, no como
> miembro.**

### 49.5 TRES COSTURAS ENTRE LIBROS, y las tres lo declaran en su propio campo

**El tramo destapa un patron que no estaba nombrado**: nodos con **fuente doble**
cuyos pasos se parten en dos bloques, uno por libro.

| nodo | pasos | los dos bloques |
|---|---:|---|
| `fit_problema_solucion` (536) | 6 | 1-3 los tres tipos de encaje (Osterwalder) / 4-6 **las fases del embudo de traccion** (Traction) |
| `project_close_out` (1165) | 11 | 1-5 el cierre formal (PM Book of Forms) / 6-11 **objetivos del arranque, testimonios y monitoreo de tres meses** (Coleman) |
| `co_creation_session` (1196) | 9 | 1-4 la sesion de codiseno con usuarios (IDEO) / 5-9 **socios de la cadena de suministro, simulaciones y contratos** (Hugos) |

> **En los tres casos el campo de fuente lo dice**, o sea que **no hay que
> deducirlo: hay que leerlo.** Y en los tres el segundo bloque **repite material
> que ya vive en nodos del libro donante**: el de `project_close_out` duplica casi
> palabra por palabra el monitoreo de tres meses de `reunion_conclusion_proyecto`,
> que la tanda R31 acababa de releer.

**PRECISION AL 541 DE LA R31, y sale de aqui.** Aquella tanda listo *el monitoreo
de tres meses* como perdida del par. **No es perdida de catalogo: ese material
tambien vive en `project_close_out`.** Una perdida se declara contra el par y
**se verifica contra el catalogo**, y esta vez la verificacion llego sesenta
puestos despues.

### 49.6 PAREJAS QUE LA COLA NO PUEDE CERRAR: ya van CUATRO

| la pareja | por que importa |
|---|---|
| `evaluacion_` contra `explotacion_tecnologias_disruptivas` (R30) | decidiria si son un racimo de tres |
| `estrategia_innovacion_producto` contra `estrategia_de_innovacion_producto` (1129) | dos identificadores que difieren en una particula, y **son nodos distintos** |
| `project_close_out` contra los dos nodos de Coleman que duplica (1165) | el bloque injertado no se puede leer contra su origen |
| `disenar_tests_pass_fail` contra `diseno_experimentos_hipotesis` (banco 9.23) | es **un par periferico de la estrella**, y de el depende la figura |

> **Cuatro parejas que este ejercicio no va a decidir por mucho que avance.** No es
> un defecto del cribado: es el limite de la cola que se eligio. **Conviene tenerlas
> juntas y contadas**, porque cada una necesita una lectura dirigida y ninguna la
> va a pedir sola.

### 49.7 LA FAMILIA DEL PROMPTING QUEDA CERRADA (1175)

**El puesto que el R30 dejo anotado salio, y sale A.** `asignacion_persona_ia`
contra `prompting_por_persona_ia`.

> **Lo que decide el par**: los dos pasos que `asignacion_persona_ia` no comparte
> con este **no son sobre personas**, son la anatomia generica del prompt, **y son
> exactamente el material por el que ya salio A contra la madre en el 514.** O sea
> que **no tiene nada que sea suyo y ademas sea sobre personas**.
>
> **Es la union de una madre y de su hija**, y el 1144 ya habia probado que esas
> dos son madre e hija y no gemelas. Con este par, `asignacion_persona_ia` lleva
> **dos A** y la forma de la familia queda dicha: **una madre, una hija, y un
> tercer nodo que las duplica a las dos a la vez.**

### 49.8 LO QUE SE SOSTIENE, medido

| medicion | como queda |
|---|---|
| `actualizar_modelo_de_negocio_pivot_o_proceed` | **OCHO veredictos y los OCHO D** (294, 733, 846, 912, 954, 1140, 1161, 1170). Confirma el 1140: **no es miembro de la mesa del pivote** |
| `customer_discovery_cuatro_fases` | **TRES hijos leidos** (1083, 1094, 1170) y **los tres sin arista** |
| `earlyvangelists_ventas_tempranas` | **cuatro lecturas**: una A (1096, contra la filosofia entera) y **tres sanas** (1128, 1164, 1185). Su unico gemelo es la filosofia |
| Rackham | dos pares laterales mas (1188, 1159) y los dos sanos. **El puro del compromiso y el racimo del metodo SPIN siguen separados**, ahora con dos de tres miembros probados contra `modelo_spin` |
| los gemelos que el barrido contesto antes de leer | `gestion_sindicato_inversores` con `manejo_syndicate_inversion` (160), `usuarios_extremos` (426), `fase_activate` (183), `fase_assess_ciclo` (373). **Ninguno se anoto como sospecha: todos se consultaron** |

### 49.9 EL SALDO

> **Mil doscientos pares leidos uno por uno, sin huecos, sin tocar un nodo.** El
> nucleo baja del 30% por primera vez y el ultimo tramo marca **4,7%**.
>
> **Lo que este checkpoint deja no son los veredictos: son los ordenes.** El 1190
> descubre que **la mesa de la junta asesora tiene que decidir un par antes que
> otro**; las tres costuras entre libros dicen que **hay nodos cuyo arreglo empieza
> por elegir de que libro son**; y las cuatro parejas que la cola no puede cerrar
> dicen **cuanto de este trabajo no va a terminar aqui**.
>
> **Y una nota de metodo que este tramo gano**: cuatro veces el barrido de las A
> contesto, antes de leer, una pregunta que en el tramo anterior se habria anotado
> como sospecha. **La disciplina del 9.5.0 esta funcionando.**

---

## 50. DOS NOMINAS DE LA R32, contadas con los dos instrumentos

**Vigentes al puesto 1200**, por el banco 9.21.

### 50.1 LOS WARRANTS: sub-puro de tres, y a UNA lectura de cerrarse

| instrumento | resultado |
|---|---|
| **contador** (`contar_nombre.py "warrant"`) | **19 nodos vivos**, 69 menciones. Los cuatro de arriba concentran 40; **el resto son mencionadores**, incluida `cumplimiento_magnuson_moss`, que usa la palabra en su sentido legal de garantia y **no tiene nada que ver** |
| **barrido de las A** | **TRES miembros** y **CERO candidatos fuera** |

| nodo | pasos | sus A |
|---|---:|---|
| **`warrants_deuda_convertible`** | 5 | **DOS**: 559 y 1028. **El centro** |
| `warrants_financiamiento` | 4 | 559 |
| `warrant_pricing_venture_debt` | 4 | 1028 |

**LA FORMA: tres pares posibles, LOS TRES EN LA COLA, dos leidos y los dos en A.**

> **Ninguno se quedo fuera de la cola**, que es raro: de las familias medidas hasta
> aqui es **la primera con cobertura completa**. **El puesto 1448 cierra la
> figura**: si sale A es un **PURO de tres**, y si sale D es una estrella.
>
> **Y es la familia mejor cableada del ejercicio**: **DOS aristas internas de tres
> posibles**, cuando el portafolio tiene cero de veintiuna y el compromiso cero de
> tres.
>
> **Nota de campo sucio, ya conocida**: dos miembros declaran *Venture Deals -
> Brad Feld* y el tercero declara solo *Venture Deals*. **La misma obra en dos
> grafias**, el defecto medido en la ficha `campos-sucios-dataset`.

### 50.2 LA EVALUACION DEL LIDER DE VENTAS: pareja cerrada, y NO es Blank contra Horowitz

**CORRECCION DECLARADA del encargo, verificada en el campo de fuente.**

| nodo | fuente declarada |
|---|---|
| `evaluacion_vp_ventas` | **The Hard Thing About Hard Things, Ben Horowitz** |
| `framework_evaluacion_director_ventas` | **The Hard Thing About Hard Things, Ben Horowitz** |

> **Los dos son de Horowitz. No hay ningun nodo de Blank en la nomina.**

| instrumento | resultado |
|---|---|
| **contador** (cinco terminos: *vp de ventas*, *lider de ventas*, *director de ventas*, *head of sales*, *vp ventas*) | **9 nodos vivos**. Siete son mencionadores |
| **barrido de las A** | **DOS miembros** y **CERO candidatos fuera** |

**LA FORMA: un par posible, en la cola, leido, en A. Cero aristas.**

> **Es una PAREJA CERRADA**, la familia mas pequena que puede existir: **todo lo
> que hay esta leido y no hay nada que anadir.** No es un puro, porque un puro se
> declara sobre tres o mas; **es el caso donde el barrido y el contador coinciden
> en que no hay mas que mirar.**

**PERO LA INTUICION DEL ENCARGO APUNTABA A ALGO REAL, y aqui esta medido.** El
contador levanta un nodo de **Blank** que menciona el puesto tres veces:
**`refinar_sales_roadmap`**, leido en el puesto **1088**.

> **Su paso 6 dice, en UNA LINEA**: *usar el roadmap como prueba de competencia al
> contratar un VP de ventas.* **Blank nombra la contratacion; Horowitz trae los
> dos nodos que dicen como evaluarla.** Es una relacion de madre y de hijos
> **entre libros**.
>
> **Y NO HAY NINGUN PAR EN LA COLA entre el nodo de Blank y ninguno de los dos de
> Horowitz.** Es la **QUINTA pareja** que este ejercicio no puede cerrar, y la
> primera que se encuentra **contando una nomina** en vez de leyendo un par.

---

## 51. TRAMO 1201-1235: la tasa de A SUBE, y hay que decirlo

### 51.1 EL MARCADOR

| medida | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **GLOBAL** | **1.235** de 3.388 | 319 | 88 | 6 | 822 | **25,8%** |
| **NUCLEO por separado** | **1.080** | 318 | 86 | 6 | 670 | **29,4%** |
| **el tramo 1201-1235** | **35** | **6** | 0 | 0 | 29 | **17,1%** |

**Sin huecos. Ningun nodo se toco.**

### 51.2 LA SERIE SE ROMPE, y es un dato del 9.19, no un fallo

| tramo | leidos | tasa de A | vara |
|---|---:|---:|---:|
| 1051-1100 | 50 | 14,0% | 38% |
| 1101-1157 | 57 | 12,3% | 37% |
| 1158-1200 | 43 | **4,7%** | 49% |
| **1201-1235** | **35** | **17,1%** | 34% |

> **Cuatro tramos bajando y este sube a mas del triple del anterior.** No es ruido
> y no lo suavizo: **la cola entro en una zona densa de familias**, Rackham con el
> racimo del cierre, Coleman con las ocho fases, Founder's Dilemmas con la junta y
> los cofundadores, y ahi los hermanos salen de a dos.
>
> **Y eso es exactamente lo que dice el 9.19**: la cifra es **un indicador de
> POSICION EN LA COLA**, no una propiedad del catalogo. **Si vale para explicar que
> baje, vale para explicar que suba.** Una serie que solo se cita cuando baja seria
> la mitad comoda de la regla, que es lo que el 9.5.0 llama la senal de alarma.

### 51.3 SEGUNDO EJEMPLAR DE LA ESTRELLA, y el primero con la cuenta completa

**El puesto 1201 cierra la familia del SCORECARD como racimo en estrella (banco
9.23), y esta vez con las dos cuentas terminadas:**

| cuenta | resultado |
|---|---|
| pares con el centro `scoring_model_scorecard` | **DOS y los dos A**: 184 y 820 |
| pares entre perifericos | **UNO, y es el unico posible: SANO** (1201) |

> **Aqui no queda ningun par sin leer.** A diferencia del ejemplar de pass/fail,
> que se sostiene sobre un periferico leido con otros dos sin decidir, **esta
> estrella esta cerrada**: tres nodos, tres pares, todos leidos.
>
> **Y la lectura es limpia**: el centro es el instrumento; los perifericos son
> **el momento en que se usa**, ordenar la cartera contra decidir en una puerta.
> **Comparten herramienta y no comparten acto.**

### 51.4 EL RACIMO DEL CIERRE SUBE A DIEZ, y su vecino queda fuera con tres lecturas

**Dos A en este tramo, y las dos por la misma tesis**: clasificar la venta por su
tamano y no presionar el cierre si es grande.

| puesto | el par | que anade |
|---:|---|---|
| **1202** | `diferencias_venta_pequena_venta_grande` contra el centro | mete al nodo en la nomina |
| **1205** | `cierre_segun_complejidad_venta` contra el mismo nodo | confirma que los dos miembros comparten la tesis |

> **RECOMPUTO, por el 9.10**: la ficha de la seccion 9 se escribio con **ocho**
> miembros. Con el **1004**, que no estaba, y con el **1202**, **la nomina medida
> hoy es de DIEZ.**

**Y el contraste vale mas que la suma**: `relacion_continua_con_cliente` lleva
**TRES lecturas y las tres sanas** (520, 1206, 1217).

> **No enuncia la tesis del racimo en ninguna de las tres.** Dice otra cosa, que la
> relacion pesa en la decision. **Es adyacente y no miembro, y ahora esta medido
> por tres lados** en vez de supuesto por el titulo.

### 51.5 PRIMERA DE LAS CUATRO CONDICIONES DEL RACIMO DE LA IA, Y SALE D

**El puesto 1211 es uno de los cinco puestos que la seccion 11 dejo escritos como
condiciones vivas, y de los cuatro que deciden si las dos mitades del racimo son
una sola familia.**

> `comprension_capacidades_limitaciones_ia` **MAPEA LA MAQUINA** (disena tus
> propias pruebas, prueba los casos limite de tu negocio, anota los patrones de
> error) y despacha la revision humana en **una linea**.
> `principio_humano_en_el_loop` **es esa linea entera**: revisar sin excepcion,
> reconocer cuando la maquina inventa, no tomarla como unica verdad, y decidir de
> antemano donde puede actuar sola.
>
> **Por la vara, CONTINUA.** Y la seccion 11 escribio que **si los cuatro cruces
> salieran D, el racimo se parte en dos.** Este es el primero y sale D.
>
> **Es UN voto de cuatro, no una conclusion.** Quedan el **1239**, el **1339** y el
> **1451**. Lo registro como el primer voto a favor de partirlo, y no adelanto
> nada mas.

### 51.6 LA FAMILIA DEL PROMPTING, LEIDA ENTERA (1220)

**El ultimo par pendiente salio. La forma completa, medida:**

| pieza | nodos |
|---|---|
| **la madre** | `ingenieria_de_prompts_efectiva` |
| **cuatro hijas SANAS** | por persona (1144), cadena de pensamiento (1125), alta variacion (1191), simulaciones (1220) |
| **un repetidor** | `asignacion_persona_ia`: repite con la madre (514) **y con una de las hijas** (1175) |

> **Es una familia madre-hijas como la del canal**, con un solo nodo de sobra. **De
> seis nodos y siete pares, cinco son jerarquia sana y dos son el mismo repetidor.**
> **El arreglo es barato**: cuatro aristas y una fusion.

### 51.7 UNA REGLA QUE ESTE TRAMO DEJA: MARCO COMPARTIDO contra ACTO COMPARTIDO

**Dos pares casi iguales de forma salieron con clases distintas, y el criterio que
los separa queda escrito porque va a hacer falta otra vez.**

| puesto | que comparten | clase | por que |
|---:|---|:---:|---|
| **1222** | los **dos primeros pasos enteros**: definir que informacion guardar y meterla en el sistema de clientes. **Es el acto que los dos titulos nombran** | **A** | lo compartido **es el acto** |
| **1224** | **un solo paso**: limitar cuantos directores ponen los inversionistas. Todo lo que cuelga de el es distinto en cada uno | **D** | lo compartido **es por donde se entra** |

> **CUANDO LO COMPARTIDO ES EL ACTO, ES A. CUANDO ES SOLO EL MARCO DE ENTRADA, ES
> SANO.** Y la misma regla explica el **1214**: los cuatro tipos de mercado son un
> marco, y por eso **los tres nodos que DECIDEN el tipo repiten entre si** (228,
> 345, 686) **y los que lo CONSUMEN salen sanos**, el posicionamiento (1145) y la
> proyeccion de ingresos (1214).
>
> **El 1224 ademas cambio de clase al correr el barrido**: la familia de la junta
> lleva **cinco lecturas y CERO A**, y con esa base volvi a contar. **Sin el
> barrido habria entrado una A que la familia no sostiene.**

### 51.8 CUARTA COSTURA ENTRE LIBROS, y ya son cuatro con el campo declarandolo

| nodo | pasos | los dos bloques |
|---|---:|---|
| `fit_problema_solucion` (536) | 6 | Osterwalder / **Traction** |
| `project_close_out` (1165) | 11 | PM Book of Forms / **Coleman** |
| `co_creation_session` (1196) | 9 | IDEO / **cadena de suministro** |
| **`propuesta_gasto_capital`** (1225) | **12** | Financial Intelligence / **Essentials of Supply Chain** |

> **En los cuatro, el campo `fuente` lo declara.** No hay que deducirlo: hay que
> leerlo. **Y en los cuatro el solape del par cae en el PRIMER bloque**, o sea que
> los cuatro veredictos son invariantes.

### 51.9 DOS CANDIDATOS NUEVOS PARA EL MISMO RACIMO, en cien puestos

**`build-measure-learn`, el numero 9 de la tabla viva, gana dos candidatos y
ninguno es del libro de la familia:**

| puesto | el candidato | su libro |
|---:|---|---|
| **1182** | `desarrollo_en_espiral` | **Cooper** |
| **1208** | `startup_como_experimento_cientifico` | Ries |

> **El 1208 es el caso limpio**: los cuatro pasos del bucle son los mismos y lo
> unico que anade son **tres condiciones de rigor**, que la hipotesis sea falsable,
> que el experimento pueda fallar y que se corra a pequena escala. **No es otro
> ciclo: es el mismo con requisitos.**
>
> **Candidatos, no miembros.** Los declaro con su evidencia y sin subir la nomina.

### 51.10 EL SALDO

> **Mil doscientos treinta y cinco pares. La tasa sube por primera vez en cinco
> tramos y la explicacion no es un fallo del cribado: es la cola.**
>
> Lo que el tramo deja escrito son **criterios** mas que veredictos: **acto contra
> marco** (1222 y 1224), **quien decide contra quien consume** una taxonomia
> (1214), y **la segunda estrella cerrada** (1201). Los tres sirven para leer lo
> que viene, no solo para explicar lo leido.
>
> **Y una nota de disciplina que este tramo confirma**: el **1224** iba a salir A y
> salio D despues de correr el barrido. **Es la segunda vez en cien puestos que el
> barrido corrige mi lectura antes de escribirla**, con el 1140. La regla de
> correrlo siempre no esta pagando en nominas: esta pagando en clases.

---

## 52. LAS PAREJAS QUE EL EJERCICIO NO PUEDE CERRAR

**Lista propia, abierta el 14 ago 2026 por encargo.** Son pares de nodos vivos
que **NO ESTAN EN LA COLA**: por mucho que el cribado avance, **no los va a
decidir nunca.** Cada uno necesita una lectura dirigida, como las nueve del
gemelo.

**Verificado uno por uno contra `INTRA_DOMINIO_PARES.jsonl` antes de escribir la
lista: los dos nodos vivos y el par ausente en los siete casos.**

### 52.1 LA LISTA: CINCO parejas, SIETE lecturas

| # | los nodos | por que hace falta cerrarla | de donde salio |
|---:|---|---|---|
| **1** | `evaluacion_tecnologias_disruptivas` contra `explotacion_tecnologias_disruptivas` | los dos repiten con `tecnologias_disruptivas_oportunidad` (505 y 513), o sea que **son candidatos a una familia de tres**. Este par decide si la familia existe o si son dos pares sueltos alrededor de un centro | **R30** |
| **2** | `estrategia_innovacion_producto` contra `estrategia_de_innovacion_producto` | **dos identificadores que difieren en una particula y son nodos distintos**, de 5 y 7 pasos. Contra el mismo tercero dieron **A** (1121) y **D** (1129). Sin este par no hay forma de saber si el catalogo tiene uno o dos | **1129** |
| **3a** | `project_close_out` contra `reunion_conclusion_proyecto` | `project_close_out` declara **fuente doble** y sus pasos 6 a 11 son de Coleman, **casi palabra por palabra** el monitoreo de tres meses del otro. **El bloque injertado no se puede leer contra su origen** | **1165** |
| **3b** | `project_close_out` contra `encuesta_satisfaccion_postproyecto` | el mismo bloque injertado contra el otro nodo de Coleman que duplica | **1165** |
| **4** | `disenar_tests_pass_fail` contra `diseno_experimentos_hipotesis` | es **un par periferico del racimo en estrella de pass/fail**, y de los pares perifericos depende la figura del **banco 9.23**. Ademas es **el unico par de esa familia que tiene arista** | **banco 9.23** |
| **5a** | `refinar_sales_roadmap` contra `evaluacion_vp_ventas` | Blank dice en **una linea** *usar el roadmap como prueba de competencia al contratar un VP de ventas*, y Horowitz trae los dos nodos que dicen como evaluarlo. **Relacion de madre e hijos entre libros** | **seccion 50.2** |
| **5b** | `refinar_sales_roadmap` contra `framework_evaluacion_director_ventas` | el mismo nodo de Blank contra el segundo de Horowitz | **seccion 50.2** |

| **6** | `pensamiento_visual` (Brown) contra `pensamiento_visual_modelos_negocio` (Osterwalder) | el primero **ya es gemelo de `get_visual`** (A del puesto **325**) y el segundo lleva casi el mismo nombre. **Tres nodos de pensamiento visual en tres libros y solo DOS de los tres pares se pueden leer** | **1281** |

> **ANADIDA el 14 ago 2026.** Con ella van **SEIS parejas y OCHO lecturas**.

### 52.2 QUE TIENEN EN COMUN, y por que aparecen ahora y no antes

**Ninguna se encontro leyendo su propio par**, porque su par no existe. **Las
cinco salieron de mirar alrededor:**

| como aparecio | cuantas |
|---|---:|
| midiendo una **nomina** (contador mas barrido) | 3 (la 1, la 4 y la 5) |
| leyendo **otro** par y chocando con un identificador o una fuente | 2 (la 2 y la 3) |

> **Es una clase de hueco que el cribado no puede ver desde dentro.** La cola se
> construyo por similitud; **estos pares quedaron por debajo del corte** y por eso
> ninguna lectura los va a traer. **Solo aparecen cuando se cuenta una familia o
> cuando dos nodos casi homonimos se cruzan por casualidad.**

### 52.3 LO QUE PIDE LA LISTA

> **Una tanda de lecturas dirigidas al cierre, siete pares**, con el mismo formato
> de las nueve del gemelo: leer el par, clasificarlo, y **anotar el efecto sobre la
> nomina o la ficha que lo levanto.**
>
> **Tres de las siete cambian el tamano de una familia** (la 1, la 4 y las dos de
> la 5). **Dos deciden si un nodo sobra** (la 2 y las dos de la 3). **Ninguna es
> una curiosidad: todas estan colgando de algo que ya esta escrito en el plan.**
>
> **Y la lista queda ABIERTA.** Van cinco parejas en 1.235 pares leidos; **el
> ritmo es de una cada doscientos cincuenta**, asi que conviene volver a esta
> seccion en cada checkpoint en vez de esperar al cierre.

---

## 53. TRAMO 1236-1256: el primer tramo del ejercicio SIN UNA SOLA A

### 53.1 EL MARCADOR

| medida | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **GLOBAL** | **1.256** de 3.388 | 319 | 88 | 7 | 842 | **25,4%** |
| **NUCLEO por separado** | **1.101** | 318 | 86 | 7 | 690 | **28,9%** |
| **el tramo 1236-1256** | **21** | **0** | 0 | **1** | 20 | **0,0%** |

**Sin huecos. Ningun nodo se toco.**

> **Es el primer tramo del ejercicio sin una sola A**, y llega justo despues del
> unico tramo que subio. **La serie no baja ni sube: se mueve con la cola**, que es
> lo que dice el 9.19.

| tramo | leidos | tasa de A | vara |
|---|---:|---:|---:|
| 1158-1200 | 43 | 4,7% | 49% |
| 1201-1235 | 35 | **17,1%** | 34% |
| **1236-1256** | **21** | **0,0%** | **43%** |

**Y el tramo largo 1201-1256, que es lo que se puede comparar con una centena:**
**56 leidos, 6 A, 10,7%, vara 38%.**

### 53.2 SEGUNDO EJEMPLAR DE LA VARA EN LOS DOS SENTIDOS, y el grafo ya lo habia resuelto

**El puesto 1240 es el segundo caso del banco 9.22 en 1.256 pares**, y trae algo
que el primero no tenia.

| sentido | la linea | el procedimiento que la expande |
|---|---|---|
| **A hacia B** | `diversidad_vs_homogeneidad_equipo` paso 3: *hablar con quien consideres sumar y poner sobre la mesa si comparten valores* | **todo** `prueba_antes_de_comprometerse`: el proyecto pequeno de prueba, la discusion de aspiraciones y riesgo, las preguntas de fortalezas y de que haria abandonar |
| **B hacia A** | `prueba_antes_de_comprometerse` paso 4: *evaluar si habria disposicion a contratar diversidad de habilidades* | **todo** `diversidad_vs_homogeneidad_equipo`: que habilidades faltan, salir a buscar contactos distintos, no elegir por comodidad |

> **Y LAS DOS ARISTAS YA ESTAN PUESTAS, en los dos sentidos, verificado
> resolviendo a nodo vivo.** El 9.22 prescribe **enlace mutuo** como arreglo, y
> aqui **el grafo ya lo hizo.**
>
> **Eso cambia el estatus de la figura**: no describe solo un par raro que hubo
> que nombrar. **Describe un cableado que alguien ya considero correcto**, y que
> sin la figura se habria leido como duplicacion mutua y se habria fusionado.

**QUINTA TRAMPA DE IDENTIFICADOR, y la mas literal del ejercicio**:
`diversidad_vs_homogeneidad_equipo` tiene una A vigente (782) contra
**`homogeneidad_vs_diversidad_equipo`**. **Las mismas dos palabras en orden
inverso, y son dos nodos vivos distintos.**

### 53.3 SEGUNDA CONDICION DEL RACIMO DE LA IA, Y TAMBIEN D

**El puesto 1239 es el segundo de los cuatro cruces que la seccion 11 dejo
escritos.** `comprension_capacidades_limitaciones_ia` contra
`human_in_the_loop_ia`: **la misma forma del 1211 con el otro nodo de la mitad
humana**, y el mismo resultado.

| condicion | puesto | clase |
|---|---:|:---:|
| contra `principio_humano_en_el_loop` | **1211** | **D** |
| contra `human_in_the_loop_ia` | **1239** | **D** |
| contra `jagged_frontier_ia` | 1339 | pendiente |
| `jagged_frontier_ia` contra `principio_humano_en_el_loop` | 1451 | pendiente |

> **Van DOS de cuatro y las dos en D.** La seccion 11 escribio que **si los cuatro
> salieran D el racimo se parte en dos.** Ya no es un voto suelto: **es la mitad.**
>
> **Y la lectura es la misma las dos veces**: `comprension_capacidades_limitaciones_ia`
> **mapea la maquina** (disena tus propias pruebas, casos limite, patrones de error)
> y despacha la revision humana **en una linea**; los dos nodos de la mitad humana
> **son esa linea entera**. **No lo adelanto**, pero conviene que la mesa sepa que
> llega con dos votos puestos.

### 53.4 EL VECINO DEL RACIMO DEL CIERRE QUEDA CERRADO, con cuatro lecturas

`relacion_continua_con_cliente` sale **sano por cuarta vez** (1249).

| puesto | contra que | que prueba |
|---:|---|---|
| 520 | `diferencias_venta_pequena_venta_grande` | contra un miembro |
| **1206** | `riesgo_tecnicas_cierre_venta_compleja` | **contra el CENTRO** |
| 1217 | `venta_interna_cliente` | contra un lateral |
| **1249** | `cierre_segun_complejidad_venta` | contra otro miembro |

> **Cuatro lecturas, cuatro sanas, ninguna A.** No enuncia la tesis del racimo en
> ninguna de las cuatro. **Es adyacente y no miembro, y ahora esta medido por
> cuatro lados en vez de supuesto por el titulo.**

### 53.5 EL MISMO DEFECTO DE INDICE, RESUELTO DE LAS DOS FORMAS POSIBLES

| puesto | el indice | nombra a sus hijos | tiene arista con ellos |
|---:|---|---|---|
| **1092** | `customer_discovery_phase2_problem_test` | **si**, sus pasos son titulos de otros nodos | **NO**, esta cableado hacia los lados |
| **1250** | `rapid_prototyping` | **si, y entre parentesis**: *(usar Determine What to Prototype)*, *(Get Feedback)* | **SI** |

> **Es el mismo defecto potencial resuelto de las dos maneras dentro del mismo
> archivo.** Y prueba algo util para la bolsa de aristas faltantes: **cablear un
> indice a sus hijos no es una imposibilidad tecnica ni una convencion ausente.**
> **Es una tarea que en unos sitios se hizo y en otros no.**

### 53.6 QUINTA COSTURA ENTRE LIBROS

`decision_pivote_perseverar` declara **fuente doble**, *The Lean Startup* y
*Traction*, y sus **nueve pasos** se parten en dos bloques: la decision con
metricas, y la busqueda del punto brillante entre los clientes leales.

> Con `fit_problema_solucion`, `project_close_out`, `co_creation_session` y
> `propuesta_gasto_capital`, **ya son CINCO**, y en las cinco **el campo lo
> declara**. **Es un patron del catalogo, no un accidente**: hay una clase de nodo
> que nacio pegando dos libros, y se reconoce leyendo un campo.

### 53.7 EL SALDO

> **Mil doscientos cincuenta y seis pares. Veintiuno seguidos sin una sola A**, y
> el tramo anterior habia sido el mas alto en cinco. **La cifra no tiene tendencia:
> tiene cola.**
>
> Lo que el tramo deja es sobre todo **cierres**: el vecino del racimo del cierre
> queda fuera con cuatro lecturas, la segunda condicion de la IA cae del mismo
> lado que la primera, y la figura del 9.22 **gana un ejemplar que el grafo ya
> habia cableado bien**. **Tres cosas que no se sabian y ahora estan medidas.**

---

## 54. EL CIERRE TRANSITIVO DE LA RELACION GEMELO: trece actos, no diecisiete

**Encargo del 14 ago 2026. Solo lectura, sin adjudicar. VIGENTE AL PUESTO 1256**,
por el banco 9.21.

### 54.1 EL METODO, y por que la cifra es reproducible

**Las 46 confirmadas se volvieron a extraer de la ficha**, no se copiaron de la
salida anterior: patron de una linea con un identificador y un veredicto, y
**vuelve a dar exactamente 46**. Mas las **tres fuera de cola con anatomia
escrita**. **Total mirado: 49.**

**Sobre ellas se construyo el grafo de la relacion gemelo** usando **las 319 A
vigentes del archivo**, y se calcularon sus **componentes conexas**: si A repite
con B y B con C, los tres son el mismo acto (banco 9.24).

### 54.2 LA CIFRA

| medida | resultado |
|---|---:|
| costuras miradas | **49** |
| **sin ninguna A** (componente de una) | **32** |
| **con gemelo** | **17** |
| **ACTOS** en que se reparten esas 17 | **13** |
| **nodos totales que entran en esos 13 actos** | **38** |

> **CORRECCION DECLARADA, y es mia.** El 13 ago escribi que la cifra viva era de
> **DIECIOCHO** costuras con gemelo tras el hallazgo del 1061. **Son DIECISIETE.**
> El 1061 unio a dos costuras que **ya estaban las dos dentro de las diecisiete**:
> no anadio una costura al conjunto, **cambio la CLASE del acto**, de dos actos
> sueltos a uno solo. **La cuenta de costuras y la cuenta de actos son distintas y
> yo sume en la equivocada.**

### 54.3 LOS TRECE ACTOS, por tamano

| # | tamano | costurados | sanos | pares A que lo sostienen | aristas internas |
|---:|---:|---:|---:|---|---:|
| **1** | **7** | 1 | 6 | 234, 586, 823, 834, 844, 885, 943 | 2 |
| **2** | **6** | **3** | 3 | 277, 374, 452, 643, **1061** | 1 |
| **3** | **4** | 1 | 3 | 386, 526, 788 | 2 |
| **4** | 3 | 1 | 2 | 492, 673, 833 | 0 |
| 5 a 13 | **2** cada uno | 1 o 2 | | un par cada uno | 0 salvo el 361 |

**LOS CUATRO GRANDES, con nombre:**

| # | la costura que lo ancla | los demas miembros |
|---:|---|---|
| **1** | `brainstorming_divergente` | `brainstorming_efectivo`, `reglas_brainstorming`, `generar_multiples_opciones`, `construir_sobre_ideas_ajenas`, `pensamiento_convergente_divergente`, `design_attitude_vs_decision_attitude` |
| **2** | **TRES costuras**: `ab_testing_optimizacion`, `optimizacion_embudo_get_customers`, `split_testing_experimentos_ab` | `funnel_get_customers_optimizacion`, `split_testing`, `test_ab_precio` |
| **3** | `voz_del_cliente_voc` | `enfoque_mercado_voc`, `homework_frontend_loading`, `voice_of_customer_homework` |
| **4** | `seleccion_ceo_fundador` | `asignacion_de_titulos_ejecutivos`, `errores_comunes_asignacion_roles` |

**Y los nueve de dos**: `producto_unico_superior`, `propuesta_gasto_capital`,
`blueprint_de_experiencia` con `customer_journey_mapping`,
`plan_de_adquisicion_acquire`, `key_partners_hypothesis`,
`metricas_de_adquisicion_activacion`, `principio_calidad_mvp` con
`producto_minimo_viable`, `future_scenarios_planning`, `retention_metrics`.

### 54.4 CUANTOS ACTOS CRECIERON: TRES de trece

| acto | vecinos directos | cierre transitivo | crece |
|---|---:|---:|---:|
| **1, el brainstorming** | 4 | **7** | **+3** |
| **3, la voz del cliente** | 2 | **4** | **+2** |
| **2, las pruebas A/B** | 5 | **6** | **+1** |
| los otros diez | igual | igual | **=** |

> **Tres de trece crecen, y los tres son de los cuatro mas grandes.** **En total,
> los actos pasan de 32 nodos a 38**: seis nodos que nadie habia contado y que
> **hay que tener delante el dia de la fusion**, porque estan pegados por una A a
> alguien que si estaba contado.
>
> **El acto 3 es el aviso mas util**: `voz_del_cliente_voc` parecia una costura con
> **un** gemelo sano y son **tres**, y dos de ellos, `homework_frontend_loading` y
> `voice_of_customer_homework`, **se leyeron en la relectura R31** sin que nadie
> notara que colgaban de la misma costura.

### 54.5 LO QUE CAMBIA EN EL ORDEN DE LA PASADA

**El acto 2 es el mas caro por cirugias y no estaba dicho.** El orden escrito en el
plan pone `ab_testing_optimizacion` como **tercera cirugia**; medido por
componentes, **ese acto contiene TRES costuras**, o sea **tres destejidos y luego
una decision sobre seis nodos.**

| acto | costuras que hay que destejer | nodos en la decision final |
|---|---:|---:|
| **2, pruebas A/B** | **3** | 6 |
| 11, el MVP (cura acoplada mayor) | 2 | 2 |
| 1, brainstorming | 1, mas la decision de fuente | **7** |
| 3, voz del cliente | 1 | 4 |

> **La tercera cirugia del plan no es una cirugia: son tres.** Queda anotado aqui
> y no se reordena nada: **el criterio del plan sigue siendo congelados liberados**,
> y esto es informacion para quien se siente, no una adjudicacion.

### 54.6 LO QUE ESTE CALCULO NO HACE

> **No adjudica.** No dice si los siete nodos del brainstorming deben quedar en
> uno, en dos o en cuatro. **Dice cuantos hay que tener delante para poder
> decidirlo**, que es exactamente lo que faltaba.
>
> **Y caduca.** Cada A nueva puede unir dos componentes y volver un acto de dos en
> un acto de cinco. **Vigente al puesto 1256**; se vuelve a correr al cierre del
> cribado, junto al barrido de confirmadas, como manda el 9.21.

### 54.7 LA LECCION DE METODO: la relectura ve PARES, no componentes

**Adoptado el 14 ago 2026.** El calculo de la seccion 54 dejo a la vista un fallo
de mirada que no es del instrumento sino de la costumbre.

> **El ejemplar**: `homework_frontend_loading` y `voice_of_customer_homework`
> **se leyeron en la relectura R31, en el puesto 526**, y ninguno de los dos se
> anoto como lo que era: **dos miembros del acto de `voz_del_cliente_voc`**, la
> costura que carga **tres congelados**. Se leyo el par y se escribio el par.
> **El acto al que pertenecian no aparecia por ningun lado.**

**LA REGLA QUE SALE DE AHI:**

> **Cuando un par de la relectura toque una costura CONFIRMADA, se cita su ACTO y
> su TAMANO, no solo el par.** Un par dice que dos nodos repiten; **el acto dice
> cuantos nodos van a estar en la mesa el dia que eso se arregle**, y esa es la
> cifra que le sirve a quien planifica.

**Por que la relectura no lo veia sola**: la relectura verifica **una clase**, y
una clase se decide entre dos nodos. **El alcance no se decide entre dos**: se
decide sobre la componente (banco 9.24). **Son dos preguntas y la tanda solo hacia
una.**

### 54.8 LO QUE ESTO LE ANADE AL ORDEN DE LA PASADA

**El tercer puesto del orden escrito en el plan no es una cirugia.**

| puesto en el orden | la cirugia | lo que cuesta de verdad |
|---:|---|---|
| 1 | `producto_minimo_viable` | **2 destejidos** (con `principio_calidad_mvp`) y una decision sobre **2 nodos** |
| 2 | `voz_del_cliente_voc` | **1 destejido** y una decision sobre **4 nodos** |
| **3** | **`ab_testing_optimizacion`** | **TRES destejidos** (`ab_testing_optimizacion`, `optimizacion_embudo_get_customers` y `split_testing_experimentos_ab`) **y una decision sobre SEIS nodos** |

> **El acto 2 del cierre transitivo contiene TRES costuras confirmadas.** El plan
> lo escribio como una cirugia que libera dos congelados; **medido por
> componentes, es la mas cara de las tres en cirugias y la segunda en nodos.**
>
> **No se reordena nada**: el criterio del plan sigue siendo **congelados
> liberados**, y por esa cuenta el orden es correcto. **Esto es informacion de
> coste para quien se siente, no una adjudicacion.**

### 54.9 RECOMPUTO AL PUESTO 1277: sin cambios

**Corrido de nuevo sobre el archivo tras el tramo 1257-1277**, como manda el 9.21.

| medida | al puesto 1256 | **al puesto 1277** |
|---|---:|---:|
| actos | 13 | **13** |
| nodos en actos | 38 | **38** |
| tamanos | 7, 6, 4, 3 y nueve de 2 | **iguales** |

> **La unica A del tramo es el puesto 1257**, `arquitectura_flexible_soa` contra
> `arquitectura_tecnica_modular`, **y ninguno de los dos es costura**: crea una
> componente nueva que no toca a las cuarenta y nueve. **La tabla de actos queda
> vigente al puesto 1277 sin tocar una cifra.**

---

## 55. TRAMO 1257-1277: las fronteras de los actos aguantan su primera prueba

### 55.1 EL MARCADOR

| medida | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **GLOBAL** | **1.277** de 3.388 | 320 | 88 | 7 | 862 | **25,1%** |
| **NUCLEO por separado** | **1.122** | 319 | 86 | 7 | 710 | **28,4%** |
| **el tramo 1257-1277** | **21** | **1** | 0 | 0 | 20 | **4,8%** |

**Sin huecos. Ningun nodo se toco.**

| tramo | leidos | tasa de A | vara |
|---|---:|---:|---:|
| 1201-1235 | 35 | 17,1% | 34% |
| 1236-1256 | 21 | 0,0% | 43% |
| **1257-1277** | **21** | **4,8%** | **33%** |
| **1201-1277 junto** | **77** | **9,1%** | **36%** |

### 55.2 LO QUE EL TRAMO PRUEBA: las fronteras medidas en la seccion 54 aguantan

**El cierre transitivo se calculo ayer sobre el archivo. Este tramo es el primero
que enfrenta a miembros de esos actos con nodos de FUERA, y los tres salen sanos.**

| puesto | el miembro | su acto | contra | resultado |
|---:|---|---|---|:---:|
| **1270** | `generar_multiples_opciones` | **acto 1**, el brainstorming, **7 nodos** | `deadlines_como_herramienta_convergencia` | **D** |
| **1276** | `plan_acquire_activate` | acto 8, **2 nodos** | `plan_de_activacion` | **D** |
| **1261** | `voz_del_cliente_voc` | **acto 3**, **4 nodos** | `customer_development_modelo` | **D** |

> **Tres actos puestos a prueba por su borde y ninguno crece.** No prueba que las
> fronteras sean definitivas, **pero si que la medicion no era casual**: los nodos
> que estan dentro estan dentro por una A, y los que quedaron fuera siguen fuera
> cuando se les lee de verdad.

**Y el mismo tramo prueba el borde de un racimo de la tabla viva**: el **1273**
enfrenta a `ciclo_construir_medir_aprender`, miembro de **build-measure-learn**,
con `establecer_linea_base_mvp`. **Sale D.** Ese racimo gano **dos candidatos** en
cien puestos (1182 y 1208) y **aqui no gana un tercero.**

### 55.3 LA ZONA MEJOR REPARTIDA DEL ARCHIVO: la junta directiva

**Con el 1258, la familia de la junta llega a SIETE lecturas y sigue con CERO A.**

| puesto | el par |
|---:|---|
| 242 | control tardio contra perdida de control |
| 1053 | perdida de control contra tamano |
| 1091 | gestion contra tamano |
| 1204 | bloqueo contra perdida de control |
| 1224 | control tardio contra tamano |
| 1238 | fundadores en la junta contra gestion |
| **1258** | bloqueo contra tamano |

> **Siete pares distintos entre seis nodos y ninguno repite.** Es lo contrario del
> portafolio, que con dieciocho lecturas lleva quince A. **Dos zonas del mismo
> tamano y de calidad opuesta**, y conviene tenerlo escrito: **cuando la mesa del
> portafolio se siente, la de la junta no tiene nada que decidir.**

### 55.4 SEPTIMA COSTURA ENTRE LIBROS, y es una confirmada

`revisiones_regulares_desempeno_ceo` (puesto **1263**) declara **fuente doble**,
*The Founder's Dilemmas* y *The Hard Thing About Hard Things*, y sus **diez pasos**
se parten en el ritual de revision (1 a 4) y **un bloque de Horowitz** (5 a 10) con
la historia de la empresa, la auditoria de velocidad de decision y los objetivos
calibrados.

> **Es la SEPTIMA del ejercicio y la primera que ademas es COSTURA CONFIRMADA**, o
> sea que su destejido y su decision de fuente **son el mismo trabajo**. En las
> siete el campo `fuente` lo declara.

### 55.5 SEGUNDA ESCALERA DE COOPER, y tambien sube

**El 1274**, `gate1_idea_screen` contra `etapa_scoping`: la puerta pide **una
pagina** y una lista de si o no; la etapa que autoriza pide busqueda secundaria,
contacto con ventas, prueba de concepto, evaluacion tecnica y un caso de negocio
preliminar.

> Con el **1099**, **van dos escaleras de este libro leidas y las dos suben** (banco
> 9.12 al derecho). **El gasto crece solo despues de que la puerta lo autorice.**

### 55.6 TERCERA CONFIRMACION DE LA REGLA DEL TIPO DE MERCADO

**El 1260** anade el tercer caso a la regla que este ejercicio fijo para esa
familia:

| los que **DECIDEN** el tipo | repiten entre si: **puro de tres** (228, 345, 686) |
|---|---|
| los que **CONSUMEN** el tipo | **sanos**: el posicionamiento (1145), la proyeccion de ingresos (1214) y **la rama de resegmentacion (1260)** |

> **La taxonomia compartida no crea repeticion. Lo que la crea es decidirla dos
> veces.**

### 55.7 EL SALDO

> **Mil doscientos setenta y siete pares.** El tramo trae **una sola A**, la de las
> dos arquitecturas modulares, y **veinte sanos**.
>
> **Su valor no esta en los veredictos sino en que pone a prueba lo medido el dia
> anterior.** Tres actos del cierre transitivo y un racimo de la tabla viva salen
> a leerse contra vecinos de fuera, **y los cuatro se quedan del tamano que
> tenian.** Una medicion que aguanta su primera prueba no es una medicion probada,
> **pero es mejor que una que no se ha probado nunca.**

---

## 56. CHECKPOINT DE LOS 1.300

### 56.1 EL MARCADOR

| medida | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **GLOBAL** | **1.300** de 3.388 | 320 | 89 | 7 | 884 | **24,6%** |
| **NUCLEO por separado** | **1.145** | 319 | 87 | 7 | 732 | **27,9%** |
| **el tramo 1278-1300** | **23** | **0** | 1 | 0 | 22 | **0,0%** |

**Sin huecos: 1 a 1.300 registrados uno por uno. Ningun nodo se toco.**

### 56.2 LAS DOS SERIES, por centenas

| centena | leidos | tasa de A | **vara** | con arista |
|---|---:|---:|---:|---:|
| 1001-1100 | 100 | 15,0% | 34% | 19 |
| 1101-1200 | 100 | **9,0%** | **42%** | 21 |
| **1201-1300** | 100 | **7,0%** | **38%** | 21 |

**Y por tramos, que es donde se ve el movimiento fino:**

| tramo | leidos | tasa de A | vara |
|---|---:|---:|---:|
| 1201-1235 | 35 | **17,1%** | 34% |
| 1236-1256 | 21 | 0,0% | 43% |
| 1257-1277 | 21 | 4,8% | 33% |
| **1278-1300** | **23** | **0,0%** | **43%** |

> **Dos de los cuatro tramos de esta centena no dieron ni una A.** Y la centena
> entera cae a **7,0%**, la mas baja del ejercicio, **con la vara en 38%**: cuatro
> de cada diez pares se resuelven citando la linea contra el procedimiento.
>
> **Y el aviso del 9.19 sigue en pie**: dentro de la misma centena hubo un tramo
> al **17,1%** y dos al **0,0%**. **La cifra se mueve con la cola, no con el
> catalogo**, y por eso se lee por tramo y no se proyecta.

### 56.3 EL UNICO B DE LA CENTENA, y es la pregunta abierta de una mesa

**El puesto 1298**, `decision_pivote_perseverar` contra `pivote_startup`, es **el
unico B en cien pares**, y no es un empate por pereza: **es la pregunta que la
mesa del pivote dejo escrita y sin decidir.**

| nodo | su disposicion sobre la MISMA decision |
|---|---|
| `decision_pivote_perseverar` (Ries y Traction) | **buscar el punto brillante**: clientes comprometidos aunque sean pocos, que tienen en comun, si el problema es el momento del mercado; **y pivotar SOLO si no aparece ninguno** |
| `pivote_startup` (Blank) | **decidir con rapidez y sin miedo al fracaso** |

> **No son dos entradas distintas a la misma puerta, que es lo que la mesa
> sospechaba: son dos disposiciones OPUESTAS sobre la misma decision.** Una empuja
> a quedarse hasta agotar la busqueda; la otra a moverse sin miedo.
>
> **Si eso cuenta como que los libros discrepan de verdad, la mesa declara
> FRONTERA y quedan los dos nodos. Si cuenta como matiz, es A y sobra uno.** No lo
> adjudico: lo que anado es que **la familia lleva SEIS B sobre la misma pregunta**
> (668, 737, 753, 843, 957 y este) **y la mesa no se ha sentado.**

### 56.4 EL NODO MAS LEIDO SIN UNA SOLA A

**`actualizar_modelo_de_negocio_pivot_o_proceed` llega a NUEVE lecturas y las
nueve en D**: 294, 733, 846, 912, 954, 1140, 1161, 1170 y **1300**.

> **Se roza con nueve vecinos distintos y no repite con ninguno.** Es la prueba
> por acumulacion de lo que el 1140 dijo por lectura: **no es miembro de la mesa
> del pivote.** Y es, medido, **el nodo mejor delimitado del catalogo**.

**Y su espejo, en la misma centena**: `filosofia_customer_validation` es el otro
extremo, el nodo con mas lecturas del archivo.

> **CORRECCION DECLARADA del 14 ago 2026 (relectura R37), por el banco 9.10.**
> Aqui se escribio que llevaba **ocho lecturas, dos A y seis sanas**, y que el
> reparto era limpio porque las dos A eran contra nodos de apertura. **Recomputado
> del archivo: son DIECIOCHO lecturas, CINCO A y TRECE D**, y con las cinco
> delante **el reparto limpio no se sostiene**: repite tambien con
> `customer_validation` (247) y con `customer_validation_sell_phase` (245), que no
> abren la etapa. **Se contaron solo las lecturas de este tramo y se dieron por el
> total.** Lo que si esta medido: **su componente de gemelos es de SIETE nodos**,
> 21 pares posibles, 15 en cola, 14 leidos y **ocho en A**.

### 56.5 LA SEXTA PAREJA QUE LA COLA NO PUEDE CERRAR

**Encontrada en el puesto 1281**, y por el mismo camino que las cinco anteriores:
contando alrededor de un par, no leyendolo.

| los nodos | por que hace falta |
|---|---|
| `pensamiento_visual` (Brown) contra `pensamiento_visual_modelos_negocio` (Osterwalder) | el primero **ya es gemelo** de `get_visual` (A del puesto **325**); el segundo lleva casi el mismo nombre y **su par con el primero no esta en la cola**. Tres nodos de pensamiento visual en tres libros y **solo dos de los tres pares se pueden leer** |

> **Van SEIS parejas en 1.300 pares.** El ritmo se sostiene en **una cada
> doscientos y pico**, y **cinco de las seis salieron midiendo, no leyendo.**

### 56.6 LA REGLA NUEVA YA ESTA PAGANDO

**La seccion 54.7 pide que, cuando un par toque una costura confirmada, se cite su
ACTO y su tamano.** En este tramo se aplico **tres veces**:

| puesto | la costura | su acto |
|---:|---|---|
| **1282** | `metricas_de_adquisicion_activacion` | **acto 10**, de 2 nodos |
| **1287** | `plan_de_adquisicion_acquire` | **acto 8**, de 2 nodos |
| **1293** | `producto_minimo_viable` | **acto 11**, de 2 nodos, **y su destejido es la primera cirugia del orden de la pasada** |

> **Ninguno de los tres actos crece con estos pares.** El valor no esta en que
> cambien: **esta en que ahora se sabe, en el momento de leer, cuanto pesa el nodo
> que se acaba de tocar.** Antes eso habia que ir a buscarlo, y por eso no se
> buscaba.

### 56.7 EL SALDO DEL CHECKPOINT

> **Mil trescientos pares leidos uno por uno, sin huecos, sin tocar un nodo.** El
> nucleo va en **27,9%** y la centena en **7,0%**, la mas baja del ejercicio.
>
> **Lo que esta centena deja no son racimos nuevos: son cierres.** El nodo mejor
> delimitado del catalogo queda probado por acumulacion; la familia de la junta
> directiva queda medida con **siete lecturas y cero A**; el vecino del racimo del
> cierre queda fuera con **cuatro**; y la pregunta de la mesa del pivote queda
> **afilada**, con las dos disposiciones opuestas puestas una al lado de la otra.
>
> **Y una cifra para el que planifique**: de los 1.300 pares leidos, **320 repiten
> y 884 estan sanos.** Por cada par que hay que fusionar hay casi tres que solo
> habia que leer para descartar. **El cribado no esta encontrando averias: esta
> midiendo cuantas NO hay.**

---

## 57. TRAMO 1301-1340: la tercera condicion de la IA cae del mismo lado

### 57.1 EL MARCADOR

| medida | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **GLOBAL** | **1.340** de 3.388 | 322 | 89 | 7 | 922 | **24,0%** |
| **NUCLEO por separado** | **1.185** | 321 | 87 | 7 | 770 | **27,1%** |
| **el tramo 1301-1340** | **40** | **2** | 0 | 0 | 38 | **5,0%** |

**Sin huecos. Ningun nodo se toco.** La vara resuelve **14 de 40, el 35%**.

### 57.2 LA TERCERA CONDICION DEL RACIMO DE LA IA, Y TAMBIEN SANA

**El puesto 1339**, `human_in_the_loop_ia` contra `jagged_frontier_ia`, es **el
tercero de los cuatro cruces** que la seccion 11 dejo escritos.

| condicion | puesto | clase |
|---|---:|:---:|
| `comprension_capacidades` contra `principio_humano_en_el_loop` | 1211 | **D** |
| `comprension_capacidades` contra `human_in_the_loop_ia` | 1239 | **D** |
| **`jagged_frontier_ia` contra `human_in_the_loop_ia`** | **1339** | **D** |
| `jagged_frontier_ia` contra `principio_humano_en_el_loop` | **1451** | **pendiente** |

> **Y las tres tienen la MISMA forma, que es lo que hace fuerte al conjunto.** En
> las tres, **un nodo MAPEA la maquina** (lista las tareas, prueba con casos
> variados, anota donde rinde bien y donde mal) **y despacha la supervision humana
> en UNA LINEA**; y el otro nodo **es esa linea entera** (define la frontera de
> autonomia, revisa cada respuesta, registra las alucinaciones, dobla la revision
> en lo critico).
>
> **No son tres lecturas independientes que casualmente coinciden: son la misma
> relacion leida tres veces entre cuatro nodos distintos.**
>
> **La seccion 11 escribio que si los cuatro cruces salieran D, el racimo se parte
> en dos.** Van **tres de cuatro**. **Queda el 1451 y de el depende.** No lo
> adelanto, pero la mesa debe saber que llega con tres votos puestos y una sola
> lectura por delante.

### 57.3 TERCER SUBCONJUNTO ESTRICTO DEL EJERCICIO

**El puesto 1332**, `valor_presente` dentro de `metodo_valor_presente_neto`: los
**cuatro** pasos del primero estan enteros en los **seis** del segundo y en el
mismo orden.

| los tres subconjuntos estrictos | puesto | perdida |
|---|---:|---|
| `disenar_tests_pass_fail` en `diseno_experimentos_pass_fail` | 511 | **cero** |
| `design_test_repeat` en `desarrollo_en_espiral` | 1182 | **cero**, y cruza libros |
| **`valor_presente` en `metodo_valor_presente_neto`** | **1332** | **cero** |

> **En los tres la direccion de la fusion esta FORZADA y no hay reparto por bloques
> que hacer.** Son los A mas baratos del archivo: **el nodo que muere no tiene ni
> una linea propia.**

### 57.4 EL OCTAVO MIEMBRO DEL RACIMO DEL CIERRE SE SEPARA POR TERCERA VEZ

**El puesto 1333**, `riesgo_tecnicas_cierre_venta_compleja` contra
`tacticas_cierre_ventas`, **y los dos dicen lo contrario:**

| nodo | que manda |
|---|---|
| `riesgo_tecnicas_cierre_venta_compleja` (Rackham) | **no presiones el cierre** si la venta es compleja o el comprador es profesional |
| `tacticas_cierre_ventas` (**Weinberg**) | **pide un si o un no explicito** al final y **no dejes la decision abierta** |

> **La ficha del racimo ya habia anotado que dos de sus tres D eran contra este
> nodo** (408 y 504). **Con este son TRES sanos, contra tres miembros distintos de
> Rackham.** El unico miembro que no es de Rackham **se separa de todos los que se
> le leen.** Queda anotado, sin adjudicar.

### 57.5 LA TRAMPA DE IDENTIFICADOR MAS AFILADA, y esta vez cambia un acto

**TRES nodos vivos cuyos identificadores se diferencian en particulas**, todos de
Cooper y todos sobre la estrategia de innovacion de producto:

| nodo | pasos | como se comporta |
|---|---:|---|
| `estrategia_innovacion_producto` | 5 | **repite** con los otros dos vecinos (357, 1121) |
| `estrategia_de_innovacion_de_producto` | 6 | **repite** con los mismos (357, 460) |
| **`estrategia_de_innovacion_producto`** | **7** | **COSTURA CONFIRMADA**, y sale **SANO** contra los dos (1129 y **1325**) |

> **El que esta averiado es justo el que NO repite.** Su acto del cierre transitivo
> es de **UNO**: no tiene gemelo, asi que **su arreglo es un destejido solo, sin
> fusion detras.**
>
> **Y si el 1325 hubiera salido A, ese acto habria pasado de uno a cuatro.** Es la
> primera vez en el ejercicio que **una sola lectura decidia el tamano de un acto**,
> y por eso se leyo dos veces antes de escribirla.

### 57.6 LA REGLA DEL ACTO, aplicada seis veces mas

**La seccion 54.7 pide citar el ACTO cuando un par toca una costura confirmada.**
En este tramo se aplico **seis veces**, y **cuatro de los seis actos son de UNO**:

| puesto | la costura | su acto |
|---:|---|---|
| 1302 | `coeficiente_viral` | **1**, sin gemelo |
| 1304 y **1340** | `seleccion_ceo_fundador` | **3** |
| 1318 | `procesamiento_paralelo_con_espirales` | **1**, sin gemelo |
| 1322 | `ganar_comprension_del_cliente` | **1**, sin gemelo |
| 1324 | `voz_del_cliente_voc` | **4**, y su cirugia es la **segunda del orden de la pasada** |
| 1338 | `revisiones_regulares_desempeno_ceo` | **1**, sin gemelo |

> **Cuatro de las seis costuras tocadas en este tramo son de las TREINTA Y DOS sin
> gemelo.** Su arreglo es un destejido y se acabo. **La regla esta cumpliendo
> exactamente lo que se le pidio**: decir, en el momento de leer, cuanto pesa el
> nodo que se acaba de tocar.

### 57.7 EL SALDO

> **Mil trescientos cuarenta pares.** El tramo trae **dos A en cuarenta**: un
> subconjunto estricto y una fusion de arquitecturas modulares.
>
> **Lo que deja son tres cierres y una espera.** El racimo del cierre confirma por
> tercera vez que su octavo miembro no encaja; la familia de la estrategia de
> innovacion queda ordenada, con el nodo averiado solo y los dos sanos repitiendo
> entre si; los tres subconjuntos estrictos quedan juntos y contados. **Y el racimo
> de la IA queda a UNA lectura de partirse en dos.**

---

## 58. LA PRIMERA FAMILIA CON COBERTURA COMPLETA, y lo que solo se ve con todo leido

**Registrado el 14 ago 2026, a partir del puesto 611 (relectura R35).**

### 58.1 LA MEDICION

**`customer_discovery` y sus cuatro vecinos** son la **primera familia del
ejercicio de la que se sabe todo.**

| medida | resultado |
|---|---:|
| miembros | **5** |
| pares posibles | **10** |
| **en la cola** | **10** |
| **leidos** | **10** |
| clases | **6 A, 3 D, 1 B** |
| aristas internas | **1** |
| candidatos fuera de nomina | **2** |

**Los cinco**: `customer_discovery`, `customer_discovery_overview`,
`customer_discovery_cuatro_fases`, `customer_discovery_introduccion` y
`customer_development_modelo`.

> **Ni un par sin encolar ni uno sin leer.** De todas las nominas medidas hasta
> aqui, esta es la unica sin reserva: **cuando se dice que es MEZCLADA, no es una
> conjetura sobre pares pendientes, es el resultado.**

### 58.2 LA LECTURA DE FORMA: una familia puede tener DOS formas segun el eje

**Con los diez pares delante, los tres sanos NO estan repartidos al azar.**

| par sano | puesto | que enfrenta |
|---|---:|---|
| `cuatro_fases` contra `introduccion` | 415 | un nodo de **FASES** contra uno de **PROCESO** |
| `introduccion` contra `overview` | 424 | un nodo de **PROCESO** contra uno de **FASES** |
| `customer_development_modelo` contra `cuatro_fases` | 1255 | un nodo de **PROCESO** contra uno de **FASES** |

**Y las seis A caen todas dentro de un mismo eje**: `customer_discovery` con
`overview` (206), con `cuatro_fases` (276), con `introduccion` (611) y con
`customer_development_modelo` (635); mas `cuatro_fases` con `overview` (156) y
`modelo` con `introduccion` (1082).

> **LA FAMILIA REPITE EN EL EJE DEL PROCESO Y JERARQUIZA EN EL DE LAS FASES.** No
> es una familia con forma unica: **es una familia con dos formas, y cual toca
> depende de que eje se cruce.**
>
> **La mesa no tiene que decidir cuantos nodos quiere: tiene que decidir cuantos
> quiere POR EJE.**

### 58.3 POR QUE ESTA LECTURA EXIGE COBERTURA TOTAL

> **Con nueve de diez pares, esta lectura no se puede hacer.** Bastaria que el par
> que falta fuera uno de los tres sanos para que la familia pareciera un racimo
> uniforme, o uno de las seis A para que pareciera mas jerarquica de lo que es.
>
> **La forma de una familia no es una propiedad de sus pares leidos: es una
> propiedad del conjunto.** Y por eso, de las familias medidas en este ejercicio,
> **esta es la unica de la que se puede afirmar la forma sin reserva.**
>
> **Lo que esto obliga hacia adelante**: cuando una nomina tenga pares sin leer,
> **su forma se escribe como provisional y con la cifra de cobertura al lado.** No
> es lo mismo decir *mezclado con siete de quince leidos* que decir *mezclado con
> diez de diez*.

### 58.4 LOS DOS CANDIDATOS QUE ARRASTRA

**Fuera de la nomina de cinco, el barrido levanta dos mas**, los dos por A con
`customer_development_modelo`: **`customer_discovery_get_out_of_building`** (849) y
**`desarrollo_de_clientes_customer_development`** (1052).

> **Con ellos la familia seria de siete y la cobertura completa se perderia.** Se
> anotan como candidatos y **la cifra de cobertura total se declara sobre los
> cinco**, que es sobre lo que esta medida.

---

## 59. TRAMO 1341-1359: dos estrellas, una confirmada y otra nacida

### 59.1 EL MARCADOR

| medida | leidos | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **GLOBAL** | **1.359** de 3.388 | 322 | 89 | 7 | 941 | **23,7%** |
| **NUCLEO por separado** | **1.204** | 321 | 87 | 7 | 789 | **26,7%** |
| **el tramo 1341-1359** | **19** | **0** | 0 | 0 | 19 | **0,0%** |

**Sin huecos. Ningun nodo se toco.** La vara resuelve **7 de 19, el 37%**.

> **Tercer tramo del ejercicio sin una sola A**, con el 1236-1256 y el 1278-1300.
> **Y aun asi es de los que mas cierran**, porque lo que trajo no fueron
> veredictos: fueron **dos resoluciones de la figura del banco 9.23**.

### 59.2 LA CONDICION VIVA DE LA ESTRELLA SE RESUELVE A SU FAVOR (1346)

**El banco 9.23 declaro la figura del RACIMO EN ESTRELLA con un ejemplar que
cojeaba**, y lo dijo asi: la familia PASS/FAIL se sostenia sobre **UN SOLO par
periferico leido**, y **el puesto 1346, si salia A, rompia la estrella.**

**Salio D.**

| la cuenta | resultado |
|---|---|
| **pares con el centro** `diseno_experimentos_pass_fail` | **TRES y los tres A**: 467, 511, 639 |
| **pares entre perifericos** | **DOS leidos y los DOS sanos**: 636 y **1346** |
| lo que queda | **UN par que NUNCA entro a la cola**, y es una de las seis parejas de la seccion 52 |

> **El ejemplar pasa de tener condicion viva a tener las dos cuentas hechas.** Y la
> razon del sano es la misma que el puesto 636 escribio para esta familia: **uno
> disena la prueba y el otro fija el umbral que la decide.** Dos lecturas
> independientes, separadas por setecientos puestos, dieron la misma frontera.

### 59.3 TERCERA ESTRELLA DEL EJERCICIO, y nace completa (1348)

**Los dos nodos del puesto 1348 ya estaban en la misma componente** del cierre
transitivo: los dos son gemelos de `regalos_estrategicos_sorpresa`, por las A de
los puestos **799** y **251**. **Este par era el unico que faltaba leer entre
ellos.**

| la cuenta | resultado |
|---|---|
| pares con el centro `regalos_estrategicos_sorpresa` | **DOS y los dos A** |
| pares entre perifericos | **UNO, el unico posible: SANO** |
| **cobertura** | **3 de 3** |

> **Es la primera estrella del archivo que nace con cobertura completa el mismo dia
> en que se declara.** Y la prueba del 1097 la respalda: **fundir los dos
> perifericos SUMARIA nueve reglas distintas en vez de borrar ninguna.**

**LAS TRES ESTRELLAS MEDIDAS, para tenerlas juntas:**

| familia | centro | pares con el centro | pares perifericos | cobertura |
|---|---|---|---|---|
| **pass/fail** | `diseno_experimentos_pass_fail` | 3 A | **2 sanos** | 5 de 6 |
| **scorecard** | `scoring_model_scorecard` | 2 A | 1 sano | **3 de 3** |
| **los regalos** | `regalos_estrategicos_sorpresa` | 2 A | 1 sano | **3 de 3** |

> **Tres familias, tres centros, y en las tres los perifericos no se tocan entre
> ellos.** La figura ya no descansa en un ejemplar: **descansa en tres, y dos de
> ellos con todos sus pares leidos.**

### 59.4 LA REGLA DEL ACTO, aplicada otras seis veces

| puesto | la costura | su acto |
|---:|---|---|
| 1347 | `funnel_get_customers_optimizacion` (miembro **sano**) | **6**, el de las pruebas A/B |
| **1354** | `seleccion_ceo_fundador` | **3** |
| **1357** | `posicionamiento_de_empresa` | **1**, sin gemelo |
| **1358** | `ganar_comprension_del_cliente` | **1**, sin gemelo |
| 1358 | `dia_en_la_vida_del_cliente` | **congelado 755**, de la segunda cirugia |
| **1359** | `producto_minimo_viable` | **2**, la cura acoplada mayor, **primera cirugia** |

> **La regla ya se aplica sin esfuerzo y esta cambiando lo que se sabe al leer**:
> en este tramo, **dos de las costuras tocadas resultaron ser de las treinta y dos
> sin gemelo**, o sea que su arreglo es un destejido y nada mas. **Eso antes no se
> sabia hasta que alguien fuera a buscarlo.**

### 59.5 LOS CUATRO HIJOS SIN CABLE

**Con el puesto 1345, `customer_discovery_cuatro_fases` llega a CUATRO hijos
leidos** (1083, 1094, 1170, 1345) **y los cuatro SIN ARISTA.**

> **Una madre con cuatro hijos verificados por lectura y ni un solo cable.** Es la
> entrada mas grande de la bolsa del 9.19 encontrada en una sola familia, y **las
> cuatro son de la clase barata**: una arista cada una.

### 59.6 EL SALDO

> **Mil trescientos cincuenta y nueve pares.** El tramo no trae ni una A, y aun asi
> **cierra dos figuras**: la estrella de pass/fail deja de tener condicion viva, y
> nace una tercera estrella con todos sus pares leidos.
>
> **Lo que esto le hace al banco**: el 9.23 se escribio con **un ejemplar que
> cojeaba y dos contraejemplos**. Hoy tiene **tres ejemplares**, dos de ellos
> completos. **Una figura con tres casos medidos ya no es una observacion: es una
> forma del catalogo.**

## 60. CHECKPOINT DE LOS 1.400: la vara deja de producir A

**Tramo 1360-1400, cuarenta y un pares leidos. CUATRO A: los puestos 1366, 1371,
1386 y 1387. Tasa del tramo, 9,8 por ciento.**

**EL MARCADOR, recomputado del archivo como manda el 9.10:**

| medida | cifra |
|---|---:|
| **registrados** | **1.400 de 3.388** |
| huecos | **cero** |
| global | **A 326, B 89, C 7, D 978** |
| **tasa global de A** | **23,3%** |
| nucleo (core) | **1.245 pares** |
| **tasa del nucleo** | **26,1%** |
| compras | 155 pares, **1 A** |

### 60.1 LA TASA DE A POR CENTENA, la serie entera

| centena | pares | A | tasa | nucleo | A del nucleo | tasa del nucleo |
|---|---:|---:|---:|---:|---:|---:|
| 1-100 | 100 | 1 | 1,0% | 0 | 0 | sin nucleo |
| 101-200 | 100 | 24 | 24,0% | 45 | 24 | **53,3%** |
| 201-300 | 100 | 54 | 54,0% | 100 | 54 | **54,0%** |
| 301-400 | 100 | 51 | 51,0% | 100 | 51 | 51,0% |
| 401-500 | 100 | 39 | 39,0% | 100 | 39 | 39,0% |
| 501-600 | 100 | 32 | 32,0% | 100 | 32 | 32,0% |
| 601-700 | 100 | 21 | 21,0% | 100 | 21 | 21,0% |
| 701-800 | 100 | 24 | 24,0% | 100 | 24 | 24,0% |
| 801-900 | 100 | 25 | 25,0% | 100 | 25 | 25,0% |
| 901-1000 | 100 | 18 | 18,0% | 100 | 18 | 18,0% |
| 1001-1100 | 100 | 15 | 15,0% | 100 | 15 | 15,0% |
| 1101-1200 | 100 | 9 | 9,0% | 100 | 9 | 9,0% |
| 1201-1300 | 100 | 7 | 7,0% | 100 | 7 | 7,0% |
| **1301-1400** | 100 | **6** | **6,0%** | 100 | **6** | **6,0%** |

> **La centena que se cierra hoy es la mas limpia del ejercicio con nucleo dentro:
> SEIS A en cien pares.** De 54 por ciento a 6 por ciento en once centenas, **sin
> tocar un solo nodo**. Y con la advertencia del 9.19 puesta donde toca: **esto es
> una posicion en la cola, no una prediccion.** La cola se ordeno por sospecha, y
> lo sospechoso se leyo primero.

### 60.2 LOS PARES RESUELTOS CON LA VARA, y el hallazgo del checkpoint

**Se cuenta lo que se puede contar: los pares cuya razon cita el 9.6.1.**

| centena | con la vara | de cien | **de esos, A** |
|---|---:|---:|---:|
| 1-300 | 0 | 0,0% | 0 |
| 301-400 | 3 | 3,0% | 0 |
| 401-500 | 12 | 12,0% | **1** |
| 501-600 | 15 | 15,0% | **2** |
| 601-700 | 12 | 12,0% | **2** |
| 701-800 | 9 | 9,0% | **2** |
| 801-900 | 23 | 23,0% | **4** |
| 901-1000 | 31 | 31,0% | **5** |
| 1001-1100 | 34 | 34,0% | **0** |
| 1101-1200 | 42 | 42,0% | **0** |
| 1201-1300 | 38 | 38,0% | **0** |
| **1301-1400** | **34** | **34,0%** | **0** |

> **LA VARA DEJO DE PRODUCIR A, y lleva CUATROCIENTOS PARES sin producir una.**
> La ultima A resuelta citando el 9.6.1 esta en la centena 901-1000. Desde el
> puesto 1001, la vara ha decidido **148 pares y los 148 salieron CONTINUA.**

**Que significa, dicho sin adorno.** La vara nacio como un cuchillo de dos filos:
*si lo que el hijo anade cabe en una linea, repite; si trae un procedimiento que
la madre no tiene, continua*. **En la primera mitad del ejercicio corto por los
dos lados.** Hoy corta por uno solo.

> **La lectura honesta es que la cola cambio de presa, como dice el 9.19.** Los
> pares madre-hijo que REPETIAN estaban arriba en la cola y ya se leyeron; los que
> quedan son madres que nombran a un hijo en una linea y el hijo trae su
> procedimiento. **La vara sigue siendo el instrumento mas usado del tramo, un
> par de cada tres, pero hoy es un instrumento de ABSOLUCION.**
>
> **Lo que NO significa**: que la vara este gastada. **Un cuchillo que solo corta
> por un lado sigue cortando**, y sin el estos 148 pares habrian sido discusiones
> de parecido. La cifra es una descripcion de la cola, no una critica del banco.

### 60.3 LO QUE EL TRAMO CAMBIA EN EL INVENTARIO

**Cuatro A, y las cuatro tocan una nomina ya escrita. Ninguna abre un frente nuevo
salvo una, y esa nace de cero.**

| puesto | el par | que le hace al inventario |
|---:|---|---|
| **1366** | `gestion_de_portafolio_gates_go_kill` contra `gestion_portafolio_foco` | **el par pendiente de LA MESA UNIDA**: la lleva a **dieciseis A** |
| **1371** | `employee_pool_esop` contra `pool_opciones_empleados` | **la familia de la reserva de opciones pasa a CUATRO nodos** por cierre transitivo |
| **1386** | `customer_discovery_get_out_of_building` contra `customer_discovery_introduccion` | **cierra la cola del acto de CUSTOMER DISCOVERY**, sin agrandarlo |
| **1387** | `entrenamiento_empleados_startup` contra `entrenamiento_funcional_empleados` | **acto NUEVO de dos nodos**, y **quinta trampa de identificador** |

**DOS COLAS CERRADAS EN EL MISMO TRAMO, y es la primera vez que pasa.**

| familia | nomina | posibles | en cola | leidos | A | resto | pendientes |
|---|---:|---:|---:|---:|---:|---|---:|
| **acto de Customer Discovery** | 9 | 36 | 16 | **16** | **12** | 3 D, 1 B | **cero** |
| **la mesa unida** | 16 | 120 | 21 | **20** | **16** | 1 B, 3 D | **uno**, el 1524 |

> **Cobertura al lado de las dos formas, como manda el 9.26**: la de Customer
> Discovery es **16 de 36** y la de la mesa unida es **20 de 120**. **Las dos
> formas siguen siendo PROVISIONALES**, y la segunda con una reserva enorme:
> **noventa y nueve de sus pares no se encolaron nunca.** Cerrar la cola no es
> tener cobertura; es agotar lo que el ejercicio se propuso mirar.

### 60.4 UNA CORRECCION MIA, declarada por el 9.10

**En la razon del puesto 1377 escribi que la mesa unida cerraba su cola y que solo
le quedaba un pendiente, el 1399. Es falso por dos lados.**

| lo que escribi | lo medido |
|---|---|
| el 1377 es par interno de la mesa unida | **`pruning_portafolio` NO figura en la nomina de dieciseis.** El par no era interno |
| queda **un** pendiente en cola | quedaban **DOS**: el 1399 y el **1524** |

> **De donde salio el error**: lei el nodo `portfolio_management` como si su
> compania en el par heredara la pertenencia. **Un miembro de la mesa en un par no
> hace del par un asunto de la mesa**, exactamente igual que el 9.24 dice que el
> gemelo no es la familia. **La correccion esta escrita dentro de la propia razon
> del 1377 en el archivo**, no solo aqui, para que quien lea la linea vea las dos
> cosas.

### 60.5 EL RETRATO DE LAS A A LOS 1.400

**Recomputado entero del archivo.**

| medida | cifra |
|---|---:|
| pares en A | **326** |
| **nodos tocados por alguna A** | **466** |
| componentes conexas de la relacion gemelo | **175** |
| de dos nodos | 121 |
| de tres | 29 |
| de cuatro | 9 |
| de cinco | 7 |
| de seis | 4 |
| de siete | 3 |
| **de nueve** | **1**, Customer Discovery |
| **de doce** | **1**, la mesa unida |

> **Ciento veintiuna de las 175 componentes son parejas sueltas.** El grueso de la
> repeticion del catalogo **no son racimos: son gemelos de dos**. Y las dos
> componentes grandes, la de doce y la de nueve, **son las dos mesas que el
> ejercicio ya tiene escritas**, o sea que el mapa grande no esconde una tercera.
>
> **Vigente al puesto 1400**, como manda el 9.21.

### 60.6 EL SALDO DEL CHECKPOINT

> **Mil cuatrocientos pares. Mil novecientos ochenta y ocho por delante.** El
> ejercicio llega al 41,3 por ciento de la cola con **cero huecos**, la tasa del
> nucleo en **26,1 por ciento** y la centena que se cierra en **6 por ciento**.
>
> **Lo que este checkpoint aporta que los otros no**: por primera vez se mide **un
> instrumento del banco contra su propio rendimiento**, y sale que **la vara lleva
> cuatrocientos pares absolviendo y ninguno condenando**. Eso no cambia ninguna
> clase ya escrita, pero **cambia lo que hay que esperar del resto de la cola**:
> las A que queden no van a venir de madres e hijos. **Van a venir de gemelos que
> se llaman distinto**, como el 1387, que aparecio de la nada entre dos nodos sin
> una sola lectura previa.

## 61. CHECKPOINT DE LOS 1.500: tres condiciones resueltas y una mesa que crece

**Tramo 1401-1517, ciento diecisiete pares leidos. DIEZ A, 8,5 por ciento.**

**EL MARCADOR, recomputado del archivo como manda el 9.10:**

| medida | cifra |
|---|---:|
| **registrados** | **1.517 de 3.388**, el 44,8 por ciento |
| huecos | **cero** |
| global | **A 336, B 89, C 7, D 1.085** |
| **tasa global de A** | **22,1%** |
| nucleo (core) | **1.362 pares** |
| **tasa del nucleo** | **24,6%** |

### 61.1 LAS DOS SERIES DEL TRAMO

| tramo | pares | A | tasa de A | **con la vara** | **de esos, A** |
|---|---:|---:|---:|---:|---:|
| **1401-1500** (la centena) | 100 | **7** | **7,0%** | **28** (28,0%) | **0** |
| 1501-1517 (el resto) | 17 | 3 | 17,6% | 8 (47,1%) | 0 |
| **1401-1517** (el tramo) | 117 | **10** | **8,5%** | **36** (30,8%) | **0** |

> **LA VARA SIGUE SIN PRODUCIR NI UNA A, y ya van QUINIENTOS DIECISIETE pares.**
> Desde el puesto 1001 ha decidido **184 pares y los 184 salieron CONTINUA**. La
> adjudicacion del 16 ago 2026 al banco 9.19 se cumple tramo a tramo: **la cifra
> mide jerarquia sin cablear, no duplicacion pendiente.**

**Y el ultimo tramo trae la cifra de vara mas alta del ejercicio, 47,1 por
ciento**: casi la mitad de sus pares son una madre que enuncia y un hijo que
detalla. En ese tramo estan los dos casos mas literales que se han visto: el
**1506**, donde `teoria_de_restricciones` **cita el titulo del otro nodo dentro de
su paso 3**; y el **1503**, donde la madre dedica media linea a coordinar aprender
con construir y el hijo entero es sobre esa coordinacion.

### 61.2 LAS TRES CONDICIONES QUE EL ENCARGO PEDIA

| puesto | que decidia | **resultado** |
|---:|---|---|
| **1451** | cuarta y ultima condicion cruzada del racimo de la IA | **D**. Las cuatro salieron D: **el racimo se parte**, y en TRES, no en dos |
| **1478** | absorcion de la pareja de las **alucinaciones** | **D**. **NO entra**: es jerarquia, no gemelo |
| **1517** | absorcion de la pareja de **invitar a la IA a todo** | **A**. **SI entra**: la nomina pasa de OCHO a DIEZ |

**La particion queda escrita entera y sin ejecutar en la seccion 11.bis**, con su
fecha de corte y su cobertura: **bloque humano de CINCO, bloque del mapa de
CUATRO, y `comprender_alineacion_etica_ia` SUELTO**, porque su unico par interno
leido, el 993, salio D.

> **Lo que las dos absorciones ensenan juntas, y sirve para el resto del
> inventario**: una pareja vecina **se absorbe cuando hace lo mismo que un
> miembro**, y **no se absorbe cuando desarrolla una linea suya.** El 1517 hace el
> mismo barrido de tareas que `jagged_frontier_ia`; el 1478 detalla una linea de
> `principio_humano_en_el_loop`. **Mismo racimo, misma distancia aparente, y
> resultados opuestos por un motivo medible.**

### 61.3 LA MESA UNIDA CRECE A DIECISIETE

**Y era la que se habia cerrado con la frase *cero candidatos fuera*.** El puesto
**1499**, `decision_factory_mentality` contra `gestion_portafolio_foco`, sale **A**
y mete un miembro nuevo por el barrido de las A.

| medida | al 1400 | **al 1517** |
|---|---:|---:|
| **nomina** | 16 | **17** |
| pares posibles | 120 | **136** |
| en la cola | 21 | **23** |
| **leidos** | 20 | **22** |
| **en A** | 16 | **17** |
| B / D | 1 / 3 | **2 / 3** |
| pendientes en cola | 1 | **1**, el **1524** |

> **Cobertura, por el 9.26: 22 de 136.** La forma sigue **PROVISIONAL** y con la
> reserva mayor del inventario: **113 pares que nunca entraron a la cola.**
>
> **Y la leccion del 9.16 se cobra otra vez**: una nomina se declaro cerrada con
> el barrido corrido, y **el barrido volvio a hablar cien puestos despues**. No
> porque estuviera mal corrido, sino porque **el barrido solo ve las A que ya
> existen**, y la cola sigue fabricando A. **Ninguna nomina esta cerrada mientras
> queden pares suyos sin leer.**

**Y QUEDA ANOTADO EL CASO QUE NO LA HIZO CRECER**, porque la comparacion es util:
el puesto **1459**, `cinco_artefactos_stage_gate` contra `estructura_de_gates`,
**es la D mas ajustada del tramo**, con tres de cuatro pasos correspondidos. Lo
que la inclina a CONTINUA es que la madre gobierna ademas **las etapas y los
roles**, que el otro no toca. **Si el fundador la leyera como A, la mesa iria a
dieciocho.** Queda escrito para que la decision sea suya y no un descuido mio.

### 61.4 LAS OTRAS SIETE A DEL TRAMO

| puesto | el par | que le hace al inventario |
|---:|---|---|
| **1431** | `convertir_necesidad_en_demanda` contra `insight_observacion_empatia` | acto NUEVO de dos. **Octava trampa de identificador**: mismo libro y **mismo subtitulo** |
| **1436** | `creacion_option_pool` contra `pool_opciones_empleados` | densifica la familia de la reserva de opciones: **5 de 6 pares leidos, los cinco en A** |
| **1438** | `framework_flujos_de_datos_ppp` contra `framework_ppph_flujos` | acto NUEVO de dos, **cinco pasos correspondidos uno a uno**. **Novena trampa** |
| **1449** | `build_measure_learn` contra `design_test_repeat` | **cierra la cola del sub-puro de build-measure-learn**: 8 de 8 encolados leidos, **los ocho en A** |
| **1468** | `business_model_canvas_scorecard` contra `business_model_canvas_vs_plan` | acto NUEVO de dos. **Decima trampa** |
| **1488** | `hipotesis_de_canales` contra `seleccion_canal_fisico` | confirma el **9.25** por tercera vez: la especializacion **fisica funde**. Racimo del canal a **8 de 15, los ocho en A** |
| **1507** | `atacar_mercados_establecidos_con_problema` contra `encontrar_grandes_problemas_mercados_emergentes` | el **mismo metodo con el mercado cambiado de parametro**. Familia a **tres nodos** |
| **1510** | `atencion_focal_y_periferica` contra `wallas_intimacion_fringe_consciousness` | familia de la conciencia periferica a **tres nodos** |

> **TRES TRAMPAS DE IDENTIFICADOR NUEVAS EN CIEN PARES**, la octava, la novena y
> la decima, **mas dos que se leyeron y NO repiten** (el 1402, *ways to grow*
> framework contra matrix; y el 1398 de la centena anterior). **La trampa ya no es
> una rareza: es la fuente principal de A que le queda a la cola**, tal como
> anticipo el checkpoint de los 1.400.

### 61.5 CUATRO CANDIDATOS NATURALES LEIDOS Y DESCARTADOS

**Y esto es lo que el 9.16 pedia: la lectura que admite o descarta al candidato,
escrita.**

| puesto | el candidato | la familia | resultado |
|---:|---|---|---|
| **1426** | `posicionamiento_por_tipo_de_mercado` | el **puro de tres** del tipo de mercado | **descartado**, sigue en 3 con cobertura **3 de 3** |
| **1433** | `encontrar_lead_vc` | el **puro de cuatro** de la competencia entre inversores | **descartado**, sigue en 4 con cobertura **6 de 6** |
| **1465** | `venture_debt_terminos_economicos` | la familia de los **warrants** | **descartado**, sigue en 3 |
| **1489** | `modelo_spin` | el **puro numero 10**, el compromiso contado tres veces | **descartado**, sigue en 3 con cobertura **3 de 3** |

> **Los dos puros con cobertura completa de la tabla viva aguantaron su prueba
> mas dura**: el candidato natural, del mismo libro y del mismo tema, se leyo y
> salio sano. **Un puro que sobrevive a su candidato vale mas que un puro que
> nunca lo tuvo delante.**

### 61.6 UNA FAMILIA QUE CIERRA COBERTURA Y RESULTA MEZCLADA

**El puesto 1448 cierra los tres pares posibles de la familia de los warrants:
`warrants_deuda_convertible`, `warrant_pricing_venture_debt` y
`warrants_financiamiento`. Cobertura 3 de 3, sin reserva.**

> **Y el resultado es que NO es un sub-puro: dos A y una D.** Con dos pares leidos
> parecia uniforme; con el tercero deja de serlo. **Es el 9.26 en su forma mas
> corta: la cobertura completa no confirmo la forma, la corrigio.**

### 61.7 LAS CINCO FRONTERAS QUE AGUANTAN

**El retrato de las A dijo que no hay una tercera mesa escondida. El tramo lo puso
a prueba cinco veces y las cinco veces aguanto.**

| puesto | que se probaba | resultado |
|---:|---|---|
| **1414** | la estrella de pasa o no pasa (4) contra build-measure-learn (7) | **D**, no nacen once |
| **1422** | los dos racimos de Rackham de cuatro | **D**, no nacen ocho |
| **1453** | Customer Discovery (9) contra Customer Validation (7) | **D**, no nacen dieciseis |
| **1467** | el mapa de ventas (6) contra preservar efectivo (3) | **D**, no nacen nueve |
| **1477** | Customer Discovery contra Customer Validation, **por sus dos costuras mayores** | **D**, y la frontera esta **escrita dentro del nodo**: empieza donde el otro termina |

> **El retrato de las A queda confirmado por lectura, no solo por conteo.** Las dos
> componentes grandes siguen separadas, **y la mayor crecio de doce a TRECE por el
> 1499**, no por fusionarse con nadie.

### 61.8 UN CONTRAEJEMPLO DECLARADO, por el 9.10

**En los puestos 1388, 1463 y 1474 quedo escrito que los indices del inventario
salen sanos contra las fases que enumeran. La figura tiene una excepcion medida.**

> **El indice de Wallas SI repite con una de sus etapas.** El puesto **1109**,
> `cuatro_etapas_del_pensamiento_creativo` contra `wallas_etapa_iluminacion`, es
> **A**; y el **1494**, contra `wallas_etapa_incubacion`, es **D**.
>
> **La figura no es una ley: es una tendencia con al menos un contraejemplo.** El
> mismo indice repite con una etapa y no con otra, **asi que la forma se decide
> por fase y no por indice.** Queda escrito antes de que alguien la cite como
> regla.

### 61.9 EL SALDO

> **Mil quinientos diecisiete pares. Mil ochocientos setenta y uno por delante.**
> El nucleo baja a **24,6 por ciento** y la centena 1401-1500 cierra en **siete A**,
> la segunda mas limpia del ejercicio.
>
> **Lo que este checkpoint cierra**: tres condiciones vivas que llevaban cientos
> de puestos abiertas, un racimo partido y medido, y **una mesa que crece despues
> de haberse declarado cerrada**. Lo que abre: **el 1524 y el 1541**, los dos
> ultimos pendientes de las dos familias grandes, **caen los dos en el proximo
> tramo.**

## 62. CHECKPOINT DE LOS 1.600: cinco colas cerradas y el sub-puro mas cargado del archivo

**Tramo 1518-1600, ochenta y tres pares. NUEVE A, 10,8 por ciento.**

| medida | cifra |
|---|---:|
| **registrados** | **1.600 de 3.388**, el 47,2 por ciento |
| huecos | **cero** |
| global | **A 345, B 89, C 7, D 1.159** |
| **tasa global de A** | **21,6%** |
| **nucleo** | **1.445 pares, A 344, tasa 23,8%** |

### 62.1 LAS DOS SERIES

| tramo | pares | A | tasa de A | nucleo | tasa del nucleo | **vara** | **vara-A** |
|---|---:|---:|---:|---:|---:|---:|---:|
| **1501-1600** (la centena) | 100 | **12** | **12,0%** | 100 | **12,0%** | **31** (31,0%) | **0** |
| 1518-1600 (el tramo) | 83 | 9 | 10,8% | 83 | 10,8% | 23 (27,7%) | 0 |

> **La vara llega a SEISCIENTOS pares sin producir una A.** Desde el puesto 1001
> ha decidido **215 pares y los 215 salieron CONTINUA.** La adjudicacion del 9.19
> se sostiene tramo a tramo.

**Y la centena SUBE de 7 a 12 A**, la primera subida desde la centena 801-900. El
motivo esta medido y no es una vuelta de la duplicacion antigua: **de las doce, la
mitad son pares internos de racimos ya escritos** (el cierre, las pruebas A/B, el
reparto de tareas con IA), o sea **densidad dentro de familias conocidas, no
familias nuevas**.

### 62.2 CINCO COLAS CERRADAS, y hay que decirlo con sus cifras

**En este tramo terminan su cola CINCO nominas**, tres de ellas por pares de este
mismo tramo.

| familia | nomina | posibles | en cola | leidos | resultado | cobertura |
|---|---:|---:|---:|---:|---|---:|
| **la mesa unida** (1524) | **17** | 136 | 23 | **23** | **18 A**, 2 B, 3 D | **23 de 136** |
| **el racimo de la IA** (1541) | **10** | 45 | 15 | **15** | **8 A**, 7 D | **15 de 45** |
| **el racimo del cierre** | **6** | 15 | 9 | **9** | **NUEVE A, cero sanos** | **9 de 15** |
| **el sub-puro de build-measure-learn** | **8** | 28 | 9 | **9** | **NUEVE A, cero sanos** | **9 de 28** |
| **el reparto de tareas con IA** (1597) | **4** | 6 | 3 | **3** | **TRES A** | **3 de 6** |

> **EL RACIMO DEL CIERRE ES HOY EL SUB-PURO MAS CARGADO DEL INVENTARIO: nueve
> pares leidos y los nueve en A**, por delante de los cuadrantes de mercado (7) y
> de la seleccion de canal (8). **Y su cola esta cerrada**, o sea que el ejercicio
> ya no le va a traer un sano por la via ordinaria: **solo pueden tumbarlo los
> seis pares que nunca entraron a la cola.**

**EL SUB-PURO DE BUILD-MEASURE-LEARN CRECIO OTRA VEZ, de SIETE a OCHO**, por el
puesto **1573**, y con el entra `design_thinking_proceso`, de Cooper. **Su cola
tambien cierra: nueve pares leidos y los nueve en A, cobertura 9 de 28.** Van
**cuatro remediciones de esta misma nomina** (5, luego 7, luego 8) y **ninguna la
dejo igual**, tal como advierte la nota del inventario.

### 62.3 LO QUE CRECIO Y LO QUE NO

| nomina | antes | **ahora** | por que |
|---|---:|---:|---|
| **build-measure-learn** | 7 | **8** | el **1573**, subconjunto estricto |
| **reparto de tareas con IA** | 2 | **4** | el **1582** y el **1597**, y con miembros de **dos libros** |
| la mesa unida | 17 | 17 | el **1537** no la hace crecer: `diamante_decision_tres_partes` sigue sin una sola A |
| el racimo del cierre | 6 | 6 | el **1564** y el **1585** son **internos**: densifican, no agrandan |
| las pruebas A/B | 6 | 6 | el **1571** y el **1575** son **internos** |
| **el puro numero 10** | 3 | **3** | **TRES candidatos naturales leidos y descartados**: 1489, 1523 y 1598 |

> **El puro numero 10 es hoy la forma mas probada del inventario.** Cobertura
> completa, 3 de 3, certificado por los dos instrumentos, **y tres candidatos del
> mismo libro y del mismo tema leidos uno por uno y descartados.** Ninguna otra
> forma del archivo ha resistido tres.

### 62.4 UNA FAMILIA CON COBERTURA COMPLETA Y CERO A

**El puesto 1558 cierra los tres pares posibles de la familia de los MERCADOS DE
VARIOS LADOS**: `mercados_multilaterales`, `multi_sided_market_channel` y
`optimizacion_mercado_multilado`. **Cobertura 3 de 3, y LAS TRES SANAS.**

> **Es lo contrario de un puro y merece nombre propio**: una familia de tres del
> mismo libro y del mismo asunto, con **todos sus pares leidos y ninguno repite.**
> Los tres nodos son **un mapa, un calculo y una ejecucion**, y ninguno sobra.
> **Con la cobertura entera se puede afirmar; con dos pares habria sido una
> sospecha.**

### 62.5 EL RETRATO DE LAS A, recomputado al 1600

| medida | al 1400 | al 1517 | **al 1600** |
|---|---:|---:|---:|
| nodos tocados por alguna A | 466 | 475 | **480** |
| componentes | 175 | 177 | **178** |
| **parejas sueltas** | 121 | 120 | **120** |
| de tres | 29 | 31 | **31** |
| de cuatro | 9 | 10 | **11** |
| de siete | 3 | 3 | **2** |
| **de ocho** | 0 | 0 | **1** |
| de nueve | 1 | 1 | **1** |
| de trece | 0 | 1 | **1** |

> **La lectura del plan no cambia: siguen siendo DOS mesas y ciento veinte
> decisiones de par.** Lo que se movio es el escalon de arriba: **una componente
> de siete paso a ocho** (build-measure-learn) **y ninguna se fusiono con otra**.
> **Sigue sin haber una tercera mesa escondida**, y en este tramo la frontera
> entre las dos grandes se probo **cuatro veces mas** (1557, 1576, y antes 1453 y
> 1477) **y aguanto las cuatro.**

### 62.6 EL SALDO

> **Mil seiscientos pares. Mil setecientos ochenta y ocho por delante.** El nucleo
> queda en **23,8 por ciento**.
>
> **Lo que este tramo cambia**: cinco nominas dejan de tener cola, o sea que
> **cinco familias del inventario ya no pueden cambiar de forma por el camino
> ordinario**. De aqui en adelante, lo que las mueva tendra que venir de los pares
> que nunca se encolaron, **y esos hay que ir a buscarlos, no esperarlos.**

## 63. LA TANDA LARGA 1518-1817: tres dominios, tres tasas, y la duplicacion cambia de casa

**Trescientos pares en una sola tanda. VEINTICINCO A, 8,3 por ciento.** Los
checkpoints de los 1.700 y los 1.800 caen dentro y van con sus cifras.

| medida | cifra |
|---|---:|
| **registrados** | **1.817 de 3.388**, el 53,6 por ciento |
| huecos | **cero** |
| global | **A 361, B 89, C 7, D 1.360** |
| **tasa global de A** | **19,9%**, y baja del 20 por primera vez |
| **nucleo (core)** | **1.445 pares, A 344, 23,8%** |

> **EL NUCLEO NO SE MOVIO NI UN PAR EN ESTA TANDA.** El ultimo par de `core` fue
> el **1600**. De los trescientos, **83 son core** (los del tramo 1518-1600) y
> **217 no lo son**. La tasa del nucleo queda congelada en 23,8 por ciento hasta
> que la cola vuelva a traer pares del catalogo central.

### 63.1 LAS TRES SERIES, y la tasa por dominio es la cifra que importa

| tramo | pares | A | tasa | **con la vara** | **vara-A** | dominios |
|---|---:|---:|---:|---:|---:|---|
| 1518-1600 | 83 | 9 | 10,8% | 23 (27,7%) | 0 | core |
| **1601-1700** | 100 | **2** | **2,0%** | 21 (21,0%) | 0 | entrega |
| **1701-1800** | 100 | **10** | **10,0%** | 8 (8,0%) | 0 | entrega + environmental |
| 1801-1817 | 17 | 4 | 23,5% | 1 (5,9%) | 0 | environmental |
| **TOTAL** | **300** | **25** | **8,3%** | **53 (17,7%)** | **0** | |

**Y POR DOMINIO, que es donde la cifra se vuelve legible:**

| dominio | pares leidos | A | **tasa de A** |
|---|---:|---:|---:|
| `core` | 1.445 | 344 | **23,8%** |
| `compras` | 155 | 1 | **0,6%** |
| **`entrega`** | **171** | **2** | **1,2%** |
| **`environmental`** | **46** | **14** | **30,4%** |

> **La tasa media del tramo, 8,3 por ciento, no describe ningun dominio.** Es el
> promedio de un dominio que casi no repite, entrega con **1,2 por ciento**, y de
> otro que repite mas que el nucleo, environmental con **30,4 por ciento**. **La
> centena 1601-1700 es la mas limpia del ejercicio entero, con DOS A**, y la que
> viene detras multiplica esa cifra por cinco.
>
> **Leccion para el marcador: a partir de aqui la tasa global deja de ser una
> medida del catalogo y pasa a ser una medida de que dominio esta pasando por la
> cola.** Se reporta, pero se lee **por dominio**.

**LA VARA SIGUE SIN PRODUCIR UNA SOLA A, Y YA VAN OCHOCIENTOS DIECISIETE PARES.**
Desde el puesto 1001 ha decidido **268 pares y los 268 salieron CONTINUA**. Y su
frecuencia **cae con el dominio**: 27,7 por ciento en core, 21 por ciento en
entrega, **5,9 por ciento en environmental**. En un dominio de nodos gemelos casi
no hay madres ni hijos que separar.

### 63.2 EL DOMINIO DE ENTREGA: una malla, no un catalogo con duplicados

**171 pares leidos y solo DOS A**, las dos en los primeros doce puestos del
dominio. Despues, **CIENTO CINCUENTA Y NUEVE pares seguidos sin una sola A.**

> **El retrato del dominio**: unos veinticinco nodos de empaque, medicion y
> servicio que **se cruzan en dependencias reales y no en repeticiones**. La
> anatomia dominante es la de la vara: **una regla general de empaque nombra un
> caso en una linea y otro nodo trae el procedimiento de ese caso** (liquidos,
> fragiles, pesados, mercancia peligrosa, teletrabajo, alucinaciones del carton).
>
> **Y la QUINTA ESTRELLA del ejercicio nacio aqui**, en el puesto 1609: centro
> `calcular_peso_dimensional_antes_cotizar`, dos A con los perifericos y el par
> periferico sano. **Cobertura 3 de 3, completa, y la primera estrella fuera del
> nucleo.**

**TRES TENSIONES DEL DOMINIO que ningun nodo resuelve**, anotadas para su mesa:

| puestos | la tension |
|---|---|
| **1714, 1741, 1765** | el **piso de cinco centimetros de relleno** contra la orden de **reducir el relleno excesivo**, sin que nadie defina la proteccion minima |
| **1726** | el **patron de cinta en H** recorre la misma cara grande y plana donde la etiqueta debe quedar **sin cinta encima** |
| **1733, 1679** | la **copia interior de la etiqueta** y la **regla del contenedor rigido** suponen una caja, y el nodo del umbral admite **sobre o bolsa** |

### 63.3 EL DOMINIO AMBIENTAL: entra duplicando

**46 pares leidos y CATORCE A, 30,4 por ciento**, la tasa mas alta de cualquier
dominio del archivo y por encima del nucleo en su mejor momento reciente.

> **Y la forma de esa duplicacion es distinta a todo lo visto.** De las catorce A,
> **once son entre identificadores casi iguales**: el mismo concepto escrito dos
> veces con el sustantivo cambiado, con las palabras invertidas, con un dos al
> final, o con una preposicion de diferencia.
>
> **La trampa de identificador deja de ser una rareza y pasa a ser LA FORMA
> PRINCIPAL de este dominio.** En el nucleo se contaron doce trampas en mil
> seiscientos pares; aqui hay once confirmadas en cuarenta y seis.

**Y no todas confirman, que es lo que hace util la lectura:** el **1780**
(`issue_spotting_ambiental` contra `issue_spotting_sostenibilidad`) y el **1813**
(`eco_efectividad` contra `eco_efectividad_2`) **son identificadores gemelos que
salen SANOS**, porque debajo hay dos instrumentos distintos. **La trampa se
confirma leyendo los pasos, nunca leyendo el nombre.**

### 63.4 CINCO SUBCONJUNTOS ESTRICTOS EN UNA SOLA TANDA

**La figura del subconjunto estricto, que en mil quinientos pares habia dado tres
ejemplares (511, 1182, 1332), da CINCO en esta tanda:**

| puesto | el nodo contenido | dentro de |
|---:|---|---|
| **1573** | `design_test_repeat` | `design_thinking_proceso` |
| **1601** | `calcular_peso_dimensional_antes_cotizar` | `medir_paquete_redondeando_hacia_arriba` |
| **1776** | `evitar_greenwashing_2` | `evitar_greenwashing` |
| **1794** | `critica_al_pib_como_metrica` | `critica_del_pib_como_metrica_de_progreso` |
| **1811** | `liderazgo_ceo_sostenibilidad` | `vision_alineacion_sostenibilidad` |

> **Con estos cinco la figura llega a OCHO ejemplares y deja de ser una
> curiosidad.** Y su anatomia es siempre la misma: **un nodo corto cuyos pasos
> estan todos dentro de uno largo, al mismo grano y sin aportar procedimiento.**
> **No es jerarquia**, porque el corto no detalla nada; **es el mismo texto
> podado.**

### 63.5 EL RETRATO DE LAS A, recomputado al 1817

| medida | al 1600 | **al 1817** |
|---|---:|---:|
| nodos tocados por alguna A | 480 | **510** |
| componentes | 178 | **192** |
| **parejas sueltas** | 120 | **132** |
| de tres | 31 | **33** |
| de cuatro | 11 | **11** |
| de ocho / nueve / trece | 1 / 1 / 1 | **1 / 1 / 1** |

> **La lectura del plan se refuerza en vez de cambiar: DOS mesas y ahora CIENTO
> TREINTA Y DOS decisiones de par.** Las catorce componentes nuevas de la tanda
> **son todas de dos o de tres nodos**, y **ninguna de las tres componentes
> grandes se movio ni se fusiono con otra**. **Sigue sin haber una tercera mesa
> escondida**, y los dominios nuevos no traen mesas: traen parejas.

## 64. EL NUCLEO QUEDA CERRADO, R40, Y LA RECONCILIACION DEL RACIMO DEL CIERRE

### 64.1 HITO: EL NUCLEO ESTA CERRADO

**Fecha de corte: puesto 1.600. El ultimo par de `core` de toda la cola.**

| medida | **cifra final del nucleo** |
|---|---:|
| **pares leidos de `core`** | **1.445** |
| **en A** | **344** |
| **tasa de A del nucleo** | **23,8%** |
| B / C / D | 87 / 7 / 1.007 |

> **Esta cifra ya no se mueve.** De aqui al puesto 3.388 la cola no trae un solo
> par mas del catalogo central: los 1.771 que quedan son de `compras`, `entrega`,
> `environmental`, `exportacion` y `franquicias`. **El 23,8 por ciento es el numero
> definitivo del nucleo**, y toda comparacion futura de tasas se hace contra el,
> no contra la global, por el banco 9.27.

**LA CURVA COMPLETA DEL NUCLEO, para que quede en un solo lugar:**

| centena | tasa del nucleo |
|---|---:|
| 101-200 | 53,3% |
| 201-300 | **54,0%**, el maximo |
| 401-500 | 39,0% |
| 601-700 | 21,0% |
| 901-1000 | 18,0% |
| 1201-1300 | 7,0% |
| **1501-1600** | **12,0%** |

> **De 54 a 23,8 de media, y con la ultima centena del nucleo en 12 por ciento.
> Sin tocar un solo nodo.**

### 64.2 TANDA R40, DEL AUDITOR: DIEZ DE DIEZ SOSTENIDAS

**Acumulado: 250 releidas, de las cuales 226 a ciegas. Discrepancias: UNA**, el
395, cerrada por los dos lados.

| puesto | el par | dominio |
|---:|---|---|
| 1524 | `estructura_de_gates` contra `estructura_gates` | core |
| 1552 | `bucle_retroalimentacion_autoajustable` contra `ciclos_retroalimentacion_autoajuste` | core |
| 1564 | `cierre_segun_tamano_decision` contra `ineficacia_cierre_ventas_grandes` | core |
| 1571 | `split_testing_experimentos_ab` contra `test_ab_precio` | core |
| 1573 | `design_test_repeat` contra `design_thinking_proceso` | core |
| 1575 | `ab_testing_optimizacion` contra `test_ab_precio` | core |
| 1582 | `descomposicion_tareas_trabajo` contra `division_trabajo_humano_ia` | core |
| 1585 | `cierre_segun_complejidad_venta` contra `cierre_segun_tamano_decision` | core |
| 1597 | `automatizacion_tareas_aburridas` contra `descomposicion_tareas_trabajo` | core |
| 1601 | `calcular_peso_dimensional_antes_cotizar` contra `medir_paquete_redondeando_hacia_arriba` | entrega |

#### 64.2.1 EL ACTO DE A/B, recomputado, y una precision de tamano

**Vigente al puesto 1817**, por el banco 9.21.

| medida | cifra |
|---|---:|
| **nomina** | **SEIS** |
| pares posibles | 15 |
| en la cola | 8 |
| **leidos** | **8**, cola cerrada |
| **A / B** | **7 / 1** (el 738) |
| **cobertura** | **8 de 15** |

**LOS SEIS**: `split_testing`, `split_testing_experimentos_ab`,
`ab_testing_optimizacion`, `optimizacion_embudo_get_customers`,
`funnel_get_customers_optimizacion` y `test_ab_precio`.

> **PRECISION, y va con la medicion delante como manda el 9.17: el acto NO gana un
> miembro en esta tanda.** `test_ab_precio` **ya era miembro desde el puesto 643**,
> y el acto ya estaba en seis. **Lo que cambia es la DENSIDAD, no el tamano.**
>
> **Y el cambio es real y vale anotarlo**: `test_ab_precio` pasa de UNA A a TRES
> (643, 1571, 1575), **contra tres nodos generales distintos**. Es el segundo nodo
> mas conectado del acto y **la unica aplicacion concreta** entre cinco manuales
> generales: **la prueba A/B aplicada al precio repite con todos los manuales que
> se le leen.**
>
> **Esto refuerza lo que el 643 mostro y la nota del plan recogio**: la repeticion
> de este acto **no esta solo dentro de las costuras**, y por eso su cirugia
> termina en una **FUSION** y no en tres destejidos.

#### 64.2.2 EL TRIO DE LAS ESTRUCTURAS DE GATES, confirmado por lectura triple

**Los tres pares posibles leidos y los TRES en A. Cobertura 3 de 3, completa.**

| puesto | el par |
|---:|---|
| **745** | `estructura_gates` contra `requisitos_gates_con_dientes` |
| **765** | `estructura_de_gates` contra `requisitos_gates_con_dientes` |
| **1524** | `estructura_de_gates` contra `estructura_gates` |

> **Es un TRIANGULO CERRADO dentro de la mesa unida**: tres nodos, tres pares, tres
> A, sin un solo sano y sin un par pendiente. **La cuarta trampa de identificador
> del ejercicio queda confirmada por los tres lados**, y no por deduccion: el
> 1524 se leyo aparte y dio lo mismo que la transitividad predecia.
>
> **Lo que le hace a la mesa unida**: no cambia su nomina de diecisiete, pero
> **identifica dentro de ella un nucleo de tres que se funde sin discusion**. Es el
> primer movimiento evidente cuando esa mesa se siente.

### 64.3 RECONCILIACION DEL RACIMO DEL CIERRE, con correccion declarada

**El encargo pregunta por una nomina de OCHO. La seccion 51.4 publico DIEZ. El
barrido de las A mide SEIS. Se cuentan las tres y se declara cual es la buena.**

| instrumento | resultado | de donde salio |
|---|---:|---|
| **el contador por nombre y tema** | 8 a 10 | la ficha de la seccion 9, ampliada en la 51.4 |
| **el barrido de las A** | **SEIS** | cierre transitivo sobre las A del archivo |

**LA NOMINA BUENA ES LA DE SEIS**, por el banco 9.17 y el 9.20: entre dos nominas
manda la medicion, y el barrido corre siempre junto al contador.

| medida | cifra |
|---|---:|
| **nomina** | **SEIS** |
| pares posibles | 15 |
| en la cola | 9 |
| **leidos** | **9**, cola cerrada |
| **en A** | **NUEVE, cero sanos** |
| cobertura | **9 de 15** |

**LOS SEIS**: `riesgo_tecnicas_cierre_venta_compleja` (el centro, cinco A),
`cierre_segun_complejidad_venta`, `cierre_segun_tamano_decision`,
`cierre_sofisticacion_comprador`, `ineficacia_cierre_ventas_grandes` y
`diferencias_venta_pequena_venta_grande`.

**CORRECCION DECLARADA, por el banco 9.10.** La seccion **51.4** dice *la nomina
medida hoy es de DIEZ*. **No lo era.** Lo que se midio ese dia fueron las A
nuevas; **la cifra de diez arrastraba a cuatro candidatos que el contador habia
metido por titulo y que el archivo desmintio uno por uno:**

| candidato del contador | como quedo medido | veredicto |
|---|---|---|
| `relacion_continua_con_cliente` | **cuatro lecturas, cuatro sanas** (520, 1206, 1217, 1249) | **FUERA**, ya declarado adyacente en la 53.4 |
| `cierre_satisfaccion_postventa` | **tres lecturas, cero A** (337 B, 1280 D, 1427 D) | **FUERA** |
| `tacticas_cierre_ventas` (Weinberg) | **seis lecturas, una sola A y NO es con el cierre** | **FUERA**, y ver abajo |
| `escala_actitud_cierre` | **CERO lecturas y CERO pares en la cola** | **NO MEDIBLE** por la via ordinaria |

> **La cuarta fila es la que hay que decir sin adorno**: `escala_actitud_cierre` es
> un nodo vivo de Rackham sobre el cierre **que nunca entro a la cola**. No esta
> fuera por medicion: **esta fuera por ausencia**. Es un pendiente de los que solo
> se resuelven yendo a buscarlo, y queda anotado como tal.

#### 64.3.1 LA FRONTERA DE MOMENTO: el forastero quedo FUERA, y ahora esta medido

**`tacticas_cierre_ventas`, de *Traction*, se llamo durante mucho tiempo el octavo
miembro del racimo. No lo es.**

| medida | resultado |
|---|---|
| lecturas totales | **SEIS**, y la cola no le deja ninguna pendiente |
| contra miembros del cierre | **una sola, el 1333, y sale D** |
| contra la familia del compromiso | **tres, y las tres D** (408, 437, 504) |
| contra las senales de compra | una, D (1365) |
| **su unica A** | el **221**, con `compromiso_linea_tiempo_cliente`, **que no es del cierre** |
| **su acto real** | **DOS nodos**: el y `compromiso_linea_tiempo_cliente` |

> **La frontera de momento se sostiene y ahora esta probada por seis lados.**
> Rackham manda **no presionar el cierre en la venta grande** y Weinberg manda
> **pedir un si o un no explicito y no dejar la decision abierta**. Son dos
> doctrinas legitimas, y por la adjudicacion de hoy eso es una **FRONTERA
> CANDIDATA inter-fuente**, no un defecto: **queda anotada en la lista de
> contradicciones internas y no cambia ninguna clase.**
>
> **Y el forastero no queda huerfano: tiene su propio acto de dos**, del lado del
> compromiso con linea de tiempo. **Estaba en la familia equivocada, no en
> ninguna.**

## 65. CHECKPOINT DE LOS 1.900: la curva propia del dominio ambiental

**Tramo 1818-1900, ochenta y tres pares. DOCE A, 14,5 por ciento.** Todos del
dominio `environmental`.

| medida | cifra |
|---|---:|
| **registrados** | **1.904 de 3.388**, el 56,2 por ciento |
| huecos | **cero** |
| global | **A 374, B 89, C 7, D 1.434** |
| **tasa global de A** | **19,6%** |

**LA TASA POR DOMINIO, como manda el banco 9.27:**

| dominio | pares | A | **tasa** |
|---|---:|---:|---:|
| `core` | 1.445 | 344 | **23,8%**, cerrado |
| `compras` | 155 | 1 | 0,6% |
| `entrega` | 171 | 2 | 1,2% |
| **`environmental`** | **133** | **27** | **20,3%** |

| tramo | pares | A | tasa | **vara** | **vara-A** |
|---|---:|---:|---:|---:|---:|
| **1801-1900** (la centena) | 100 | **16** | **16,0%** | 22 (22,0%) | **0** |
| 1818-1900 (el tramo) | 83 | 12 | 14,5% | 21 (25,3%) | 0 |

### 65.1 EL DOMINIO TIENE SU PROPIA CURVA, Y BAJA

**La tasa de `environmental` medida en dos momentos:**

| corte | pares leidos | A | tasa |
|---|---:|---:|---:|
| al puesto **1817** | 46 | 14 | **30,4%** |
| al puesto **1904** | 133 | 27 | **20,3%** |

> **El dominio entrega primero sus nodos escritos dos veces y despues su malla de
> nodos complementarios.** Es la misma forma que hizo `entrega`, que abrio con dos
> A en doce puestos y despues encadeno ciento cincuenta y nueve sanos, **pero con
> la meseta mucho mas alta.**
>
> **Consecuencia para el 9.27**: la tasa por dominio **tampoco es un numero fijo,
> es una curva**, y hay que decir en que punto de la cola se midio. **El 30,4 por
> ciento del checkpoint anterior no era el dominio: era su primera centena.**

### 65.2 LO QUE CRECIO

**Cinco familias del dominio crecieron o cerraron cobertura en este tramo**, todas
por cierre transitivo y todas de `The Green to Gold` o de `Cradle to Cradle`:

| familia | tamano | cobertura | nota |
|---|---:|---|---|
| **la critica a la eco eficiencia** | **3** | **3 de 3, completa** | **TRIANGULO CERRADO** (1783, 1832, 1836) |
| **el respeto a la diversidad** | **3** | **3 de 3, completa** | **TRIANGULO CERRADO** (1779, 1792, 1857), y su cuarto candidato **descartado** en el 1901 |
| **la alianza sectorial** | **4** | 3 de 6 | crecio dos veces, 1871 y 1903 |
| **el riesgo ambiental extendido** | **3** | 2 de 3 | 1788 y 1822 |
| **la huella de carbono** | **3** | 2 de 3 | 1805 y 1865, con discriminacion medida |

> **DOS TRIANGULOS CERRADOS EN UN SOLO TRAMO**, y con el de las estructuras de
> gates ya son tres en el archivo. **La figura del triangulo cerrado, tres nodos y
> tres pares en A, es hoy la unica forma que se puede afirmar sin reserva** en un
> dominio donde casi ninguna familia tiene la cola completa.

### 65.3 LA DISCRIMINACION MEDIDA, y vale como ejemplar

**El mismo nodo, `definir_limites_huella_carbono`, leido contra los dos nodos de
huella de carbono, da resultados opuestos y por un motivo verificable:**

| puesto | contra | clase | por que |
|---:|---|:---:|---|
| **1855** | `medir_huella_carbono_corporativa` | **D** | ese nodo **no tiene** ni la frontera organizacional ni el ano base |
| **1865** | `huella_carbono_empresarial` | **A** | ese nodo **si los tiene**, con las mismas palabras |

> **No es una inconsistencia: es la vara funcionando.** Dos nodos que parecen
> hermanos difieren en dos pasos, y esos dos pasos deciden la clase de un tercero
> contra cada uno. **Es el mejor ejemplo del tramo de por que la clase se decide
> leyendo los pasos y no el titulo.**

### 65.4 LAS TRAMPAS DE IDENTIFICADOR DEL DOMINIO, con su tasa de acierto

**Van CUATRO leidas que NO confirman**, y conviene tenerlas contadas:

| puesto | el par de identificadores gemelos | resultado |
|---:|---|---|
| 1780 | `issue_spotting_ambiental` / `issue_spotting_sostenibilidad` | **D** |
| 1813 | `eco_efectividad` / `eco_efectividad_2` | **D** |
| **1867** | `dialogo_con_stakeholders` / `dialogo_stakeholders` | **D** |
| **1886** | `triple_bottom_line` / `triple_bottom_line_2` | **D** |

> **En este dominio el identificador gemelo acierta la mayoria de las veces, pero
> falla lo bastante como para que nunca se pueda dar por hecho.** La regla
> practica queda escrita: **la trampa se confirma leyendo los pasos, y cuatro de
> las lecturas de este dominio existen solo porque no se dio por supuesto.**

---

## 66. EL CHECKPOINT DE LOS 2.000, y la correccion que obliga a precisar el 9.27

**Corte: puesto 2.012.** Marcador recomputado del archivo, no de tabla anterior
(banco 9.10).

### 66.1 EL MARCADOR, con la tasa POR DOMINIO al lado de la global (banco 9.27)

| dominio | puestos | pares leidos | A | B | C | D | **tasa de A** |
|---|---|---:|---:|---:|---:|---:|---:|
| `compras` | 1-155 | 155 | 1 | 2 | 0 | 152 | **0,6%** |
| `core` | 156-1600 | **1.445** | **344** | 87 | 7 | 1.007 | **23,8%** (CERRADO) |
| `entrega` | 1601-1771 | 171 | 2 | 0 | 0 | 169 | **1,2%** (CERRADO) |
| `environmental` | 1772-1941 | **170** | **29** | 0 | 0 | 141 | **17,1%** (CERRADO) |
| `exportacion` | 1942-2012 | 71 | 13 | 0 | 0 | 58 | **18,3%** (abierto) |
| **GLOBAL** | 1-2012 | **2.012** | **389** | **89** | **7** | **1.527** | **19,3%** |

**Faltan 1.376 pares para el final.** Van 2.012 de 3.388, sin huecos.

### 66.2 LA CORRECCION DECLARADA: environmental NO repite mas que el nucleo

**El 9.27 se escribio el 17 ago 2026 con environmental a 46 pares leidos y 30,4%
de A**, y su texto corrido decia que era *"otro que repite mas que el nucleo"*.

> **Medido hoy con el dominio CERRADO: environmental repite MENOS que el nucleo.
> 170 pares, 29 A, 17,1% contra el 23,8% del nucleo.**

**La cifra de la tabla no era falsa: llevaba su corte escrito al lado, "46 pares
leidos", tal como manda el 9.21.** Lo que fallo fue **la glosa en prosa**, que
leyo esa foto como una propiedad del dominio. Es exactamente el error que el 9.21
nombra: *"un numero sin corte se lee como propiedad del catalogo, y no lo es: es
una foto"*. **La regla funciono; la frase que la acompanaba no.**

**Por eso NO se para el cribado:** no hay contradiccion con una regla vigente ni
con una cifra publicada con su corte. Hay una **lectura corregida**, y se corrige
en su sitio (banco 9.17: entre dos nominas manda la MEDICION).

### 66.3 LO QUE LA CORRECCION ENSENA, y es una figura nueva: LA COLA DEL DOMINIO SE AGOTA POR DENTRO

**No es que environmental bajara por azar. Es que un dominio a medio leer no
describe al dominio**, y ahora esta medido **dos veces, en dos dominios
distintos, con la misma forma.**

| `environmental` (cerrado) | pares | A | tasa |
|---|---:|---:|---:|
| primeros 29 (1772-1800) | 29 | 10 | **34,5%** |
| siguientes 50 (1801-1850) | 50 | 12 | **24,0%** |
| siguientes 50 (1851-1900) | 50 | 4 | **8,0%** |
| ultimos 41 (1901-1941) | 41 | 3 | **7,3%** |

| `exportacion` (abierto) | pares | A | tasa |
|---|---:|---:|---:|
| primeros 25 (1942-1966) | 25 | 9 | **36,0%** |
| siguientes 25 (1967-1991) | 25 | 4 | **16,0%** |
| ultimos 21 (1992-2012) | 21 | **0** | **0,0%** |

> **Las dos curvas caen igual: el primer tercio del dominio concentra la
> duplicacion y el ultimo tercio esta limpio.** No es una coincidencia de dos
> dominios: es la consecuencia de como esta ordenada la cola. **La cola esta
> ordenada por parecido descendente**, asi que dentro de cada dominio los pares
> mas parecidos entran primero. La tasa de un dominio **no se puede leer hasta que
> el dominio cierra.**

**Lo que obliga, y es corto:** toda tasa por dominio se escribe **con su cobertura
al lado** (banco 9.26) y con la marca de **abierto o cerrado**. Un dominio abierto
al 18,3% no dice 18,3%: dice **"18,3% hasta aqui, y va bajando"**.

### 66.4 EL TRAMO 1989-2012: VEINTICUATRO PARES, CERO A

**El tramo mas limpio de todo el ejercicio en su tamano.** Veinticuatro D
seguidas, y ninguna forzada. Contadas por como se resolvieron: **diez** donde los
dos nodos no comparten ni un paso, **ocho** que se resolvieron por la vara, y
**seis** donde lo compartido es letra generica de dos a cinco lineas y toda la
sustancia esta en lo propio de cada uno (1989, 1990, 1997, 2001, 2010 y 2011).

**LA VARA DEL TRAMO (banco 9.6.1): 8 de 24, un 33,3%** de pares donde uno de los
dos nodos nombra en UNA LINEA lo que el otro trae como procedimiento. Son los
puestos 1991, 1992, 1993, 1995, 2005, 2006, 2009 y la mitad del 2012.

> **Y aqui la vara alta NO significa cola pendiente** (banco 9.19): significa que
> este dominio esta hecho de **un indice y sus fichas**. `seleccion_de_metodo_de_pago`
> nombra los cinco metodos de pago en una linea y hay **un nodo por metodo**;
> `documentacion_exportacion` nombra "que documentos necesitas" y hay un nodo por
> documento. **Es una enciclopedia, y una enciclopedia con indice no es una
> enciclopedia que se repite.**

### 66.5 LA FIGURA DEL TRAMO: EL ESQUELETO COMPARTIDO

**Dos veces en veinticuatro pares**, y las dos con la misma forma: dos nodos con
**el mismo esqueleto de pasos** y **contenido distinto en cada paso**.

| puesto | los dos hermanos | el esqueleto comun | lo que los separa |
|---:|---|---|---|
| **2001** | `customs_bonded_warehouses` / `foreign_trade_zones` | evaluar si conviene, contactar la oficina | en el almacen la mercancia **solo espera**; en la zona **se le puede trabajar encima** |
| **2011** | `financiamiento_sba_exportacion` / `programas_ex_im_bank` | capital de trabajo, consultar al servicio comercial | uno pasa por un **prestamista privado**, el otro **es el banco** |

> **El esqueleto compartido es lo contrario del subconjunto estricto.** En el
> subconjunto los pasos del corto viven dentro del largo y la clase es **A**. Aqui
> **la forma coincide y el contenido no comparte nada**, y la clase es **D**. Son
> las dos caras de la misma pregunta, y la unica manera de distinguirlas es la
> que ya esta escrita: **leer los pasos, no la forma.**

### 66.6 LA COLA ABIERTA DEL TRAMO, anotada para cuando salga

**Puesto 2006**, `clausula_antidesviacion` contra `documentacion_exportacion`,
salio **D**: la clausula es una linea dentro de un documento, no un documento.
**Pero `licencia_exportacion_regulaciones` (leido en el puesto 2008) trae en su
paso 6 la MISMA orden**: incluir la declaracion de control de destino en todas
las facturas comerciales.

> **Ese par no ha salido todavia.** Queda anotado aqui para leerlo cuando aparezca,
> y para que no se cierre el dominio sin haberlo mirado.

---

## 67. EL CHECKPOINT DE LOS 2.100, y la curva del dominio medida por tercera vez

**Corte: puesto 2.103.** Marcador recomputado del archivo (banco 9.10).

### 67.1 EL MARCADOR, con la tasa POR DOMINIO y su estado (banco 9.27)

| dominio | puestos | pares | A | B | C | D | **tasa de A** | estado |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `compras` | 1-155 | 155 | 1 | 2 | 0 | 152 | **0,6%** | CERRADO |
| `core` | 156-1600 | **1.445** | **344** | 87 | 7 | 1.007 | **23,8%** | CERRADO |
| `entrega` | 1601-1771 | 171 | 2 | 0 | 0 | 169 | **1,2%** | CERRADO |
| `environmental` | 1772-1941 | 170 | 29 | 0 | 0 | 141 | **17,1%** | CERRADO |
| `exportacion` | 1942-2071 | 130 | 15 | 0 | 0 | 115 | **11,5%** | CERRADO |
| `franquicias` | 2072- | 32 | 8 | 0 | 0 | 24 | **25,0%** | **abierto, y va bajando** |
| **GLOBAL** | 1-2103 | **2.103** | **399** | **89** | **7** | **1.608** | **19,0%** | abierto |

**Van 2.103 de 3.388, sin huecos. Faltan 1.285.**

### 67.2 LA PREDICCION DEL CHECKPOINT ANTERIOR SE CUMPLIO

En el checkpoint de los 2.000 se escribio, sobre `exportacion`: *"un dominio
abierto al 18,3% no dice 18,3%: dice **18,3% hasta aqui, y va bajando**"*.

> **`exportacion` cerro en 11,5%.** La prediccion no era una corazonada: era la
> consecuencia de que la cola esta ordenada por parecido descendente.

**Y la curva se ha medido ya en TRES dominios, con la misma forma:**

| dominio | primer tercio | segundo tercio | ultimo tercio | cierre |
|---|---:|---:|---:|---:|
| `environmental` | **34,5%** | 24,0% | **7,3%** | 17,1% |
| `exportacion` | **36,0%** | 16,0% | **0,0%** | 11,5% |
| `franquicias` (abierto) | **66,7%** (4/6) | 30,8% (4/13) | **0,0%** (0/13) | por medir |

> **Tres dominios, tres curvas, la misma caida.** `franquicias` abrio con la tasa
> mas alta medida en todo el ejercicio, **cuatro A en sus primeros seis pares**, y
> a los treinta y dos pares ya lleva **trece D seguidas**. La tasa del 25,0% que
> figura hoy en la tabla **no describe al dominio**: describe que se lleva un
> tercio leido.

### 67.3 EL DOMINIO DE FRANQUICIAS: OCHO A, Y TODAS DE LA MISMA FAMILIA

**Las ocho A del dominio son SUBCONJUNTO ESTRICTO o su caso espejo.** Ninguna es
un empate de contenido: en siete de ellas un nodo cabe dentro del otro.

| puesto | el nodo que cabe dentro | dentro de | lo unico que anade |
|---:|---|---|---|
| 2072 | `terminacion_franquiciado_causas` | `gestion_terminacion_franquiciado` | que los plazos se graduen por gravedad |
| 2074 | `estimacion_inversion_inicial_franquiciador` | `cinco_categorias_costos_franquicia` | los materiales de entrenamiento |
| 2075 | `costos_preparacion_franquicia` | `cinco_categorias_costos_franquicia` | mobiliario, y "adicionales" en las marcas |
| 2076 | `contratar_abogado_especializado_franquicias` | `eleccion_abogado_franquicias` | pedir referencias |
| 2079 | `estrategia_multicanal_expansion` | `franquicia_mas_crecimiento_corporativo_hibrido` | nada: su paso 4 resume sus pasos 1 y 2 |
| 2087 | `sitio_web_captura_leads` | `sitio_web_franquicia` | la oferta de valor a cambio del contacto |
| 2090 | `contratar_abogado_especializado_franquicias` | `contratar_abogado_franquicias` | completar la planificacion antes |
| **2080** | **ninguno contiene al otro** | `proceso_llamada_inicial_venta` / `proceso_primera_llamada` | **una linea por cada lado** |

**El 2080 es el unico distinto y por eso importa** (ver 67.5).

### 67.4 DOS ESTRELLAS EN EL MISMO DOMINIO, CON ORIENTACIONES OPUESTAS

**Es la primera vez que el ejercicio da las dos formas juntas**, y verlas al lado
deja clara la unica cosa que las distingue: **quien contiene a quien.**

| | **OCTAVA, clasica** (puesto 2092) | **SEPTIMA, invertida** (puesto 2090) |
|---|---|---|
| **centro** | `cinco_categorias_costos_franquicia`, el **largo** | `contratar_abogado_especializado_franquicias`, el **corto** |
| **periferios** | `estimacion_inversion_inicial_franquiciador`, `costos_preparacion_franquicia` | `eleccion_abogado_franquicias`, `contratar_abogado_franquicias` |
| **las A** | 2074 y 2075: el centro **contiene** a los dos | 2076 y 2090: el centro **esta contenido** en los dos |
| **la D entre periferios** | 2092: dos categorias distintas del mismo presupuesto | 2086: cada largo trae lo suyo |

> **En la clasica, un nodo grande fue troceado y cada trozo quedo como nodo.** En
> la invertida, **un nodo pequeno fue escrito dos veces con dos ampliaciones
> distintas.** Son dos averias de catalogo distintas y las dos se detectan igual:
> leyendo los pasos y contando lo que queda fuera.

### 67.5 NOTA DE DOCTRINA PARA EL AUDITOR: la vara vuelve LINEA por los dos lados

**Puesto 2080**, `proceso_llamada_inicial_venta` contra `proceso_primera_llamada`.
Es la misma agenda de la misma llamada: **seis pasos coinciden, paso por paso y en
el mismo orden**, con el mismo formulario nombrado igual al final. **Ninguno
contiene al otro**: cada uno anade UNA linea, una criba mas por experiencia y
territorio en uno, el rechazo amable del que no califica en el otro.

> **Hasta hoy el 9.22, la vara en los dos sentidos, se habia usado siempre para
> confirmar D**: la vara volvia PROCEDIMIENTO por los dos lados y el par
> continuaba. **Este es el primer par donde vuelve LINEA por los dos lados**, que
> es el caso espejo y da **A**.

**No es regla nueva. Es el 9.6.1 y el 9.22 aplicados juntos**, y queda anotado
aqui para que el auditor lo mire en la relectura.

**Y viene con su contraste medido, el puesto 2091**, que se leyo D con la misma
pregunta: alli el solape es de **dos pasos de cuatro** y cada nodo sigue hacia un
sitio distinto, la calidad del contacto uno y el control del gasto el otro. **Lo
que separa un caso del otro es cuanto coincide y en que orden**, no el parecido
de los titulos.

### 67.6 LA REGLA PRACTICA QUE ESTE TRAMO OBLIGO A ESCRIBIR

Con tantas llamadas ajustadas seguidas, quedo hecha explicita la manera de contar
lo que un nodo anade, y se aplico igual en las veintiseis lecturas del tramo:

> **Es LINEA** un puntero a una fuente, una advertencia, un criterio suelto o una
> accion unica. **Es PROCEDIMIENTO** un paso que obliga a tomar varias decisiones
> dentro de si, o que se repite en el tiempo.

**Ejemplos de las dos columnas, todos de este tramo:** linea fue *consultar dos
sitios oficiales* (2022), *pedir referencias* (2076 y 2090), *definir la oferta de
valor* (2087). Procedimiento fue *auditar cada cierto tiempo si la relacion
evoluciono* (2073), *verificar los umbrales de tarifa estado por estado* (2073),
*establecer la logistica del entrenamiento con sus asistentes obligatorios* (2100).

> **La regla no cambia la vara: la hace contable.** Y como toda vara, se reporta y
> no se interpreta sola: en un dominio hecho de indice y fichas, como
> `exportacion`, la vara alta no significo cola pendiente (banco 9.19 y seccion 66.4).

---

## 68. LA TANDA LARGA 2: reporte consolidado de los puestos 1818 a 2117

**300 pares leidos de corrido.** Se aplicaron las doctrinas escritas sin inventar
ninguna. **No hubo que parar**: nada de lo leido contradice una regla vigente ni
una cifra publicada con su corte.

### 68.1 CIFRAS

**EL TRAMO, 1818-2117:**

| | pares | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **total del tramo** | **300** | **39** | **0** | **0** | **261** | **13,0%** |
| `environmental` (cola del dominio) | 124 | 15 | 0 | 0 | 109 | 12,1% |
| `exportacion` (dominio entero) | 130 | 15 | 0 | 0 | 115 | **11,5%** |
| `franquicias` (apertura) | 46 | 9 | 0 | 0 | 37 | 19,6% |

> **Ni una B ni una C en trescientos pares.** Todas las lecturas se resolvieron con
> las doctrinas escritas; ninguna quedo en duda.

**EL MARCADOR GLOBAL AL CORTE, recomputado del archivo (banco 9.10):**

| dominio | puestos | pares | A | tasa | estado |
|---|---|---:|---:|---:|---|
| `compras` | 1-155 | 155 | 1 | 0,6% | CERRADO |
| `core` | 156-1600 | 1.445 | 344 | **23,8%** | CERRADO |
| `entrega` | 1601-1771 | 171 | 2 | 1,2% | CERRADO |
| `environmental` | 1772-1941 | 170 | 29 | 17,1% | CERRADO |
| `exportacion` | 1942-2071 | 130 | 15 | 11,5% | CERRADO |
| `franquicias` | 2072- | 46 | 9 | 19,6% | **abierto, y va bajando** |
| **GLOBAL** | 1-2117 | **2.117** | **400** | **18,9%** | abierto |

**Van 2.117 de 3.388, sin huecos. Faltan 1.271.**

**LA VARA (banco 9.6.1) POR TRAMO**, reportada y no interpretada sola:

| tramo | pares | resueltos por la vara | % |
|---|---:|---:|---:|
| `environmental` 1818-1941 | 124 | 27 | **21,8%** |
| `exportacion` 1942-2071 | 130 | 37 | **28,5%** |
| `franquicias` 2072-2117 | 46 | 12 | **26,1%** |
| **tramo completo** | **300** | **76** | **25,3%** |

> **Y la vara alta de `exportacion` NO significo cola pendiente** (banco 9.19):
> ese dominio esta hecho de **un indice y sus fichas**, un nodo que nombra los
> cinco metodos de pago y un nodo por metodo, un nodo que nombra los documentos y
> un nodo por documento. Una enciclopedia con indice no es una enciclopedia que se
> repite.

**LA VARA EN LOS DOS SENTIDOS (banco 9.22): 37 usos**, y su reparto dice algo:
**27 de los 37 caen en `franquicias`**, que es donde los nodos son mas parecidos
entre si y donde hubo que medir en las dos direcciones para separarlos.

### 68.2 FIGURAS

**NUEVAS EN ESTA TANDA:**

1. **LA COLA DEL DOMINIO SE AGOTA POR DENTRO.** *(precision adoptada al 9.27)*
   Un dominio a medio leer no describe al dominio, por la misma razon por la que
   la global no describe al dominio: la cola esta ordenada por parecido
   descendente, asi que los pares mas parecidos de cada dominio entran primero.
   **Medida en tres dominios:** `environmental` 34,5% a 7,3%; `exportacion` 36,0%
   a 0,0%; `franquicias` 66,7% a 0,0% y sigue abierto.

2. **EL ESQUELETO COMPARTIDO** *(puestos 2001 y 2011)*. Dos nodos con la **misma
   forma de pasos** y **contenido distinto en cada paso**: el almacen aduanero
   contra la zona franca, la agencia de pequenos negocios contra el banco de
   exportacion. **Es lo contrario del subconjunto estricto**: alli los pasos del
   corto viven dentro del largo y la clase es A; aqui la forma coincide, el
   contenido no comparte nada y la clase es D.

3. **LAS DOS ADUANAS** *(2008, 2013, 2037, 2054, 2070; cinco veces)*. Lo que el
   pais destino exige para dejar entrar contra lo que el pais propio prohibe
   sacar. **Con una asimetria que se repitio en las cinco:** contra la regla ajena
   hay recurso, una queja formal; contra la propia no.

4. **LOS DOS PARES QUE NO SE CRUZAN** *(1942 y 1969 en A; 2034 y 2059 en D)*.
   Cuatro nodos de cobro bancario formando dos parejas gemelas. Las dos parejas
   repiten por dentro; **los dos cruces entre parejas salen D**. Es la forma de un
   catalogo sano con dos instrumentos distintos.

5. **EL PASO DE OFICIO** *(todo `exportacion`)*. "Consulta con la oficina de
   comercio exterior" abre media docena de nodos del dominio. **Por si solo no
   decide ninguna clase** y hubo que descontarlo en cada lectura.

6. **LA BIFURCACION** *(2030 y 2050)*. `certificados_genericos_de_origen` **empieza
   declarando que no es el otro**: su paso 1 es confirmar que el producto NO
   califica para ningun tratado. Es la frontera mas limpia que dio el ejercicio:
   escrita dentro del propio nodo.

7. **EL CASO ESPEJO DE LA VARA** *(2080 y 2105)*. Ver 68.5.

**CRECIDAS EN ESTA TANDA:**

8. **SUBCONJUNTO ESTRICTO: de 12 ejemplares a 23.** Once nuevos en el tramo (1966,
   1967, 2022, 2043, 2072, 2074, 2075, 2076, 2079, 2087, 2090). **Es la figura
   dominante de `franquicias`**: ocho de sus nueve A son un nodo que cabe dentro
   de otro.

9. **ESTRELLAS (banco 9.23): de 6 a 8**, y las dos nuevas caen en el mismo dominio
   con **orientaciones opuestas**, la primera vez que salen juntas.

| | **OCTAVA, clasica** (2092) | **SEPTIMA, invertida** (2090) |
|---|---|---|
| centro | `cinco_categorias_costos_franquicia`, el **largo** | `contratar_abogado_especializado_franquicias`, el **corto** |
| periferios | `estimacion_inversion_inicial_franquiciador`, `costos_preparacion_franquicia` | `eleccion_abogado_franquicias`, `contratar_abogado_franquicias` |
| las A | 2074 y 2075: el centro **contiene** a los dos | 2076 y 2090: el centro **esta contenido** en los dos |
| la D | 2092 | 2086 |

> **En la clasica, un nodo grande fue troceado y cada trozo quedo como nodo. En la
> invertida, un nodo pequeno fue escrito dos veces con dos ampliaciones
> distintas.** Dos averias de catalogo distintas, y las dos se detectan igual:
> contando lo que queda fuera.

### 68.3 NOMINAS Y RACIMOS, con su cobertura al lado (banco 9.26)

**`exportacion` cerro con TRECE actos y ninguna familia mayor.** Doce son ACTO 2 y
uno es ACTO 3:

| acto | miembros | puestos |
|---|---|---|
| **investigacion de mercados** (ACTO 3, **SEXTA ESTRELLA**) | `enfoque_paso_a_paso_investigacion_mercado` centro, `screening_mercados_potenciales`, `evaluacion_mercados_objetivo` | 1966, 1967; la D entre periferios en 1972 |
| carta de credito | `carta_de_credito_letter_of_credit`, `letters_of_credit` | 1942 |
| reglamento de exportacion | `export_administration_regulations`, `regulaciones_exportacion_ear` | 1943 |
| seguro de carga | `seguro_de_carga_transporte`, `seguro_exportacion` | 1947 |
| terminos de venta | `incoterms_reglas_comerciales_internacionales`, `terminos_de_venta_incoterms` | 1952 |
| certificado de origen | `certificado_de_origen_tratados_libre_comercio`, `nafta_free_trade_agreements` | 1955 |
| intermediarios | `intermediarios_exportacion`, `uso_intermediarios_exportacion` | 1957 |
| canales | `seleccion_canales_distribucion`, `seleccion_canales_exportacion` | 1961 |
| apoyo a pymes | `ecosistema_global_emprendimiento_gee`, `recursos_apoyo_pymes_sba` | 1963 |
| cobranza documentaria | `documentary_collections`, `letra_de_cambio_bill_of_exchange` | 1969 |
| metodo de pago | `prevencion_problemas_de_pago`, `seleccion_de_metodo_de_pago` | 1981 |
| barreras comerciales | `barreras_comerciales_no_arancelarias`, `cumplimiento_acuerdos_comerciales_tanc` | 1984 |
| propiedad intelectual | `licenciamiento_tecnologico`, `proteccion_propiedad_intelectual_internacional` | 2022 |
| apoyo del servicio comercial | `consejos_distrito_exportacion_dec`, `uso_del_us_commercial_service` | 2043 |

> **Ningun acto de `exportacion` paso de tres miembros, y el unico de tres es una
> estrella.** El dominio no tiene familias: tiene parejas de gemelos con nombre
> distinto, casi todas por duplicacion de terminologia, `letters_of_credit` contra
> `carta_de_credito_letter_of_credit`.

**`franquicias`, con 46 de sus pares leidos, lleva SEIS actos**, dos de ellos de
tres miembros y los dos son estrellas *(ver 68.2)*. Los otros cuatro son ACTO 2:
terminacion (2072), estrategia hibrida (2079), la primera llamada de ventas
(2080), el sitio web (2087) y la definicion legal (2105).

> **Ninguna nomina se declaro con el contador solo** (banco 9.20): el barrido de
> las A corrio en cada caso, y por eso el racimo del abogado se vio entero, tres
> nodos y tres pares, antes de nombrarlo estrella.

### 68.4 CONDICIONES VIVAS

**CUATRO COLAS ANOTADAS Y ABIERTAS**, escritas en la razon del puesto donde
aparecieron para que no se pierdan:

| anotada en | la cola | por que importa |
|---:|---|---|
| **2006** y **2058** | `clausula_antidesviacion` contra `licencia_exportacion_regulaciones` | ese nodo **si ordena** incluir la declaracion de control de destino en todas las facturas; el par no ha salido |
| **2027** y **2061** | el racimo de **cuatro nodos del plan de exportacion** | `estructura_`, `plan_accion_`, `elementos_..._ejemplo` y `desarrollo_plan_exportacion`; varios pares sin salir |
| **2114** | la advertencia de **no financiarse con las cuotas iniciales** | sale ya en tres nodos de `franquicias`; faltan pares cruzados |
| **67.2** | **`franquicias` esta abierto al 19,6% y bajando** | su tasa **no se puede leer hasta que cierre** |

**UNA CONTRADICCION INTERNA NUEVA, INTRA-FUENTE** *(puesto 2094)*: un nodo manda
dar **recursos dedicados a los dos canales**, propio y franquiciado, y otro manda
darlos **exclusivamente a la franquicia** hasta que haya caja excedente. **Puede
leerse como dos momentos, pero como instruccion chocan.** Va a la lista de
`PENDIENTES.md`, columna INTRA-FUENTE, y **no decide la clase**: decide
continua-o-repite, y la D se queda, igual que se adjudico en el 1632.

### 68.5 PENDIENTES DE DOCTRINA

> **NINGUNO.** En trescientos pares no hubo que registrar ni una razon marcada
> como pendiente de doctrina: **las reglas escritas alcanzaron para todos**.

**Pero SI hay una nota de doctrina para el auditor**, que no es regla nueva sino
dos reglas aplicadas juntas por primera vez:

> **EL CASO ESPEJO DEL 9.22: la vara vuelve LINEA por los DOS lados.**
>
> Hasta hoy el 9.22 se habia usado siempre para **confirmar D**: la vara volvia
> PROCEDIMIENTO por los dos lados y el par continuaba. **En dos pares de esta
> tanda volvio LINEA por los dos lados**, que es el caso espejo y da **A**.
>
> - **2080**, `proceso_llamada_inicial_venta` contra `proceso_primera_llamada`:
>   la misma agenda de la misma llamada, **seis pasos coincidentes paso por paso y
>   en el mismo orden**, con el mismo formulario nombrado igual al final. Cada uno
>   anade una linea.
> - **2105**, `comprender_definicion_legal_franquicia` contra
>   `marco_name_system_fee`: **el mismo test de tres elementos** en el mismo orden
>   y con el mismo cierre, el abogado. Cada uno anade una linea, el umbral de los
>   quinientos dolares uno y separar soporte de control el otro.
>
> **Ninguno de los dos es subconjunto estricto: ninguno contiene al otro.** Por eso
> se anota. Y viene con su contraste medido, **2091**, que se leyo **D** con la
> misma pregunta porque alli el solape es de dos pasos de cuatro y cada nodo sigue
> hacia un sitio distinto.

**Y con la regla practica que este tramo obligo a escribir** *(seccion 67.6)*: es
**LINEA** un puntero, una advertencia, un criterio suelto o una accion unica; es
**PROCEDIMIENTO** un paso que obliga a varias decisiones dentro de si o que se
repite en el tiempo. **No cambia la vara: la hace contable.**

### 68.6 CORRECCIONES DECLARADAS

**UNA, y toca una regla del banco.**

> **El 9.27 decia que `environmental` "repite mas que el nucleo".** Se escribio el
> 17 ago 2026 con el dominio a **46 pares leidos y 30,4%**. **Con el dominio
> CERRADO, repite MENOS: 17,1% contra el 23,8% del nucleo.**

**La cifra de la tabla no era falsa: llevaba su corte escrito al lado**, "46 pares
leidos", tal como manda el 9.21. **Lo que fallo fue la glosa en prosa**, que leyo
esa foto como propiedad del dominio: el error exacto que el 9.21 nombra.

**Que se hizo:** la tabla del 9.27 se recomputo del archivo al corte, la glosa se
corrigio en su sitio con la correccion declarada al lado, y se anadio la
**PRECISION** que la explica *(la cola del dominio se agota por dentro)*.

**Por que NO se paro el cribado:** no hay contradiccion con una regla vigente ni
con una cifra publicada con su corte. **Hay una lectura corregida por una
medicion**, que es exactamente lo que manda el 9.17.

### 68.7 LOS PUESTOS NUEVOS EN A, en orden, para la relectura del auditor

**TREINTA Y NUEVE.**

**`environmental`, cola del dominio (15):**
`1818, 1822, 1824, 1826, 1828, 1829, 1832, 1836, 1857, 1865, 1871, 1884, 1903, 1905, 1917`

**`exportacion`, dominio completo (15):**
`1942, 1943, 1947, 1952, 1955, 1957, 1961, 1963, 1966, 1967, 1969, 1981, 1984, 2022, 2043`

**`franquicias`, apertura (9):**
`2072, 2074, 2075, 2076, 2079, 2080, 2087, 2090, 2105`

**Las cuatro que mas conviene mirar primero**, por si la relectura quiere empezar
por lo discutible:

| puesto | por que |
|---:|---|
| **2080** | primer caso espejo del 9.22; **ninguno contiene al otro** |
| **2105** | segundo caso espejo, y con su contraste D inmediato en el 2106 |
| **2022** | la clase se decidio porque lo unico propio del hijo era **un puntero a dos sitios web**; su hermano salio D en el 2012 contra la misma madre |
| **2043** | el nodo corto **reconoce en su propio paso 1** que la puerta es la misma oficina del nodo largo |

---

## 69. REGISTROS PREVIOS DE LA TANDA LARGA 3, y una PARADA por cifra publicada

### 69.1 RELECTURA R41 del auditor: OCHO DE OCHO SOSTENIDAS

**Puestos 2080, 2105, 2022, 2043, 1832, 1955, 2074, 2090.** Ocho de ocho.

| | |
|---|---:|
| **acumulado de relecturas** | **258 leidas** |
| **de ellas ciegas** | **234** |
| **discrepancias en todo el ejercicio** | **una** |

> **El auditor eligio bien el lote.** Seis de los ocho son los que yo mismo habia
> marcado como los mas discutibles del tramo, incluidos **los dos casos espejo**
> (2080 y 2105) y **las dos A que se decidieron por un puntero o una linea**
> (2022 y 2043). **Las cuatro se sostienen.**

### 69.2 EL PAR DE NAFTA (puesto 1955): ejemplar mayor del TOQUE UNICO

**Nota del auditor sobre el 1955, y es la mas util de las dos.**
`certificado_de_origen_tratados_libre_comercio` contra
`nafta_free_trade_agreements` salio **A**: los cinco pasos se corresponden.

**Lo que el auditor vio y yo no habia juntado:** esos dos nodos **no son solo un
par del cribado**. Son tambien **los dos primeros de la lista del barrido de
vigencia** *(`PENDIENTES.md`, adjudicacion del 11 ago 2026)* y **el ejemplar
escrito de la DECISION 4 de la mesa**, la del alias.

**TRES ENCARGOS DISTINTOS CAEN SOBRE LOS MISMOS DOS NODOS:**

| encargo | de donde viene | que manda hacer |
|---|---|---|
| **fusion** | el cribado intra, puesto 1955 | fundirlos, reponiendo las cinco perdidas ya listadas |
| **reparacion de vigencia** | el barrido de marco, orden 1 y 2 de la lista | quitar de id y titulo un tratado extinto desde el 1 de julio de 2020 |
| **alias** | DECISION 4 de la mesa, aprobada el 9 ago 2026 | el id que muera lleva alias, o rompe lo que apuntaba a el |

> **Por el TOQUE UNICO del banco 9.4, los tres van en UN SOLO ACTO.** Hacerlos por
> separado significa abrir los mismos dos nodos tres veces, y **reparar la
> vigencia de un nodo que la fusion va a borrar despues.**

**Y hay una alineacion medida que conviene dejar escrita, porque no es casualidad
y ahorra una decision:** el id que el barrido de vigencia manda matar,
`nafta_free_trade_agreements`, **es tambien el que la fusion puede matar**. Si la
fusion va **hacia** `certificado_de_origen_tratados_libre_comercio`, el mismo acto
resuelve las tres cosas. **Con dos condiciones verificadas contra el grafo:**

1. **El alias es obligatorio**, y ya tiene dos aristas con nombre que lo prueban:
   `foreign_trade_zones` lo lleva en `nodos_previos` e
   `import_regulations_foreign_governments` en `nodos_siguientes`. **Hoy ninguno de
   los dos nodos tiene `ids_alias`.**
2. **Las cinco perdidas se reponen o el acto pierde material**: la regla de
   *obtenido en su totalidad*, la conservacion por el periodo que exija la aduana,
   las cuatro reglas del articulo 401, los dos porcentajes (60 por transaccion y
   50 por costo neto) y **los nombres de los formularios**, sin los cuales el paso
   de completar el certificado no dice que papel llenar.

> **No se adjudica aqui la direccion de la fusion**: se deja medido que **una de
> las dos direcciones cierra los tres encargos y la otra no.** Va a la mesa.

### 69.3 EL CENSO DE HERRAMIENTAS suma dos, y las dos VIVAS

**Del puesto 2022**, `proteccion_propiedad_intelectual_internacional`, cuyo paso 3
cablea dos portales de agencias de un solo pais.

| nombre propio | verificado el | estado | quien lo opera |
|---|---|---|---|
| **`stopfakes.gov`** | 11 ago 2026 | **VIVO** | International Trade Administration, Departamento de Comercio de EE.UU. |
| **`uspto.gov`** | 11 ago 2026 | **VIVO** | United States Patent and Trademark Office |

**Ninguno de los dos anuncia mudanza, retiro ni redireccion.** `stopfakes.gov`
sigue ofreciendo sus guias por pais.

> **Y deja un dato que le sirve al barrido de vigencia**: `stopfakes.gov` lo opera
> **la misma International Trade Administration** que opera `trade.gov`, o sea el
> organismo que absorbio `export.gov`. **Los tres portales de la lista cuelgan del
> mismo sitio**, y eso hace probable que se muevan juntos la proxima vez.

**Son los nombres propios numero quince y dieciseis del censo.** La cuenta de
vivacidad queda: **6 muertas, 7 vivas, 1 no verificable, 14 verificadas**, con
**otros dieciocho nombres anotados sin verificar**.

### 69.4 TAREA PREVIA: el barrido de marco medido en `franquicias`

**Medido, no leido, y sin adjudicar.** Detalle completo con ids en `PENDIENTES.md`.

| | `franquicias` | `exportacion` |
|---|---:|---:|
| nodos vivos | 195 | 141 |
| **(a) cablean marco legal de UN SOLO PAIS** | **31** (15,9%) | **42** (29,8%) |
| **(b) nombran organismo o portal** | **12** (6,2%) | **34** (24,1%) |
| **(c) citan norma con version o fecha** | **10** (5,1%) | **3** (2,1%) |

**Y AHORA LA COLUMNA QUE DECIDE, la del banco *donde se actua*:**

| donde esta la condicion de pais | `franquicias` | `exportacion` |
|---|---:|---:|
| **EN LA PUERTA** (`condiciones_activacion`, con el pais nombrado) | **2** de 31 | **5** de 42 |
| **EN LA DESPEDIDA** (solo en `resumen_teorico`) | **4** | **23** |
| **EN NINGUN SITIO** | **25** | **14** |
| **ejecutan el marco en pasos o entregable sin condicion en la puerta** | **25** | **36** |

> **`franquicias` tiene un problema MAS PEQUENO y MUCHO MAS CALLADO.** Cablea
> marco de un solo pais en la mitad de proporcion que `exportacion`, pero **el
> 80,6% de sus nodos de marco no nombra el pais en ningun sitio**, contra el
> **33,3%** de `exportacion`. Alli casi siempre esta dicho, aunque tarde; **aqui
> casi nunca esta dicho.**

**LOS DOS QUE SI CONDICIONAN EN LA PUERTA, y son el contramodelo del dominio:**
`comprender_definicion_legal_franquicia` y `cumplimiento_ftc_rule_436`, los dos
con la misma primera linea: *solo aplica si vendes o piensas vender franquicias en
Estados Unidos*.

**EL PEOR CASO MEDIDO, y merece nombre propio: `obtencion_marca_registrada`.** Su
puerta dice *"aun no se posee un trademark **federal**"*. **Nombra la federacion
como si hubiera una sola en el mundo.** Y sus pasos mandan buscar en la base
**TESS del gobierno de EE.UU.** y presentar la solicitud **ante la USPTO**, sin
condicion de ninguna clase. **Es el unico del dominio que condiciona con un
adjetivo en vez de con un pais.**

**Que dice la medicion sobre la pregunta del encargo, sin adjudicar:** el volumen
de `franquicias` es menor, pero **la fraccion muda es mas del doble**, y **25 de
sus 31 nodos de marco ejecutan el marco sin condicion en ningun sitio**. La
doctrina escrita mide **donde se actua**, no cuanto se cita.

### 69.5 PARADA: una cifra publicada no reconcilia con el grafo

**Lo encontre al medir `franquicias` con el mismo instrumento que se uso para
`exportacion`. No lo toco, no lo corrijo y no adivino: lo traigo.**

**LA CIFRA PUBLICADA** esta en `PENDIENTES.md`, seccion *ADJUDICADO PARA EL PLAN
(11 ago 2026)*, en la tabla que dice **"Recontado del grafo, sobre nodos VIVOS"**:

| averia | publicado | **medido hoy** |
|---|---:|---:|
| citan **NAFTA** en su texto | 6 | **6** OK |
| cablean **`export.gov`** | 3 | **3** OK |
| citan **Incoterms** sin ninguna version | **12** | **3** |
| **UNION de las tres** | **21** | **12** |

**DOS DE LAS TRES FILAS CUADRAN EXACTAMENTE.** La de Incoterms no, y por un
factor de cuatro.

**EL DIAGNOSTICO, medido fichero por fichero en `dataset/nodos/`:**

| donde aparece la palabra Incoterms | nodos |
|---|---:|
| **en el TEXTO** (las cinco casas), **vivos** | **3** |
| en el texto, pero **deprecados** | 2 |
| **solo en el id, en un alias, en una ARISTA o en `merged_originals`** | **11** (9 de ellos vivos) |
| total de ficheros tocados | **16** |

> **3 vivos que lo citan + 9 vivos que solo lo llevan en una arista o en el id = 12.**
> **Ese es el 12 publicado.**

**Y es exactamente el error que la propia adjudicacion habia corregido para
NAFTA**, tres parrafos mas arriba en el mismo documento:

> *"otros 2 solo lo llevan en una ARISTA que apunta al id
> `nafta_free_trade_agreements`. **Apuntar al nodo no es citar el tratado**, y
> mezclarlos infla la cifra."*

**La correccion se aplico a la fila de NAFTA y no a la de Incoterms.** Por eso las
otras dos filas cuadran y esa no.

**LO QUE NO HAGO:** no toco la tabla publicada, no cambio el numero, no reordeno
la lista del barrido. **Lo que la medicion deja listo por si el fundador
adjudica:**

- **Incoterms sin version, nodos vivos que lo CITAN: 3** y los tres son de
  `exportacion`: `incoterms_reglas_comerciales_internacionales`,
  `seguro_de_carga_transporte`, `terminos_de_venta_incoterms`.
- **UNION real de las tres averias: 12 nodos, con solape CERO entre las tres**, y
  **los 12 de 12 siguen siendo de `exportacion`**, que es lo que la adjudicacion
  usaba como argumento. **El argumento sobrevive entero: solo cambia el tamano.**
- **La decision de fondo no se mueve**: `exportacion` sigue siendo el unico
  dominio tocado por las tres averias, y sigue yendo primero.

> **Se para por la cifra, no por la decision.** La adjudicacion aguanta; el numero
> que la acompana no. Y por el 9.21 recien ampliado, **una cifra que no cuadra con
> el grafo se corrige donde esta escrita, no se hereda.**

---

## 70. LAS OCHO CORRECCIONES APLICADAS, y un volteo decidido

**12 ago 2026, antes de reanudar el cribado.** La otra sesion dejo ocho correcciones
escritas y verificadas en su encargo, **todas sobre ficheros de esta sesion**. Se
aplican aqui, **cada una con su correccion declarada donde vive la cifra**, y sin
borrar el texto original: **una correccion que tapa lo que corrige no se puede
auditar.**

### LAS SIETE DE CIFRA, y las siete comprobadas contra el grafo antes de escribirlas

| # | que cambia | donde | comprobada |
|---:|---|---|---|
| **1** | **self-alias, de 7 a CERO** | `AUDITORIA_MOTOR.md` B.3 | **si**: cero nodos, vivos o deprecados, se listan a si mismos |
| **2** | **Incoterms sin version, de 12 a 3**; la **union, de 21 a 12** | `PENDIENTES.md` | **si**: tres nodos vivos lo citan en su texto, y son los tres nombrados |
| **3** | **el resolutor SI existe** | `AUDITORIA_MOTOR.md` B.3 | **si**: `mapaDeAlias` y `resolverId` en `graph.ts` |
| **4** | la cuenta de **18** nodos de fuente, **31 con la clase entera** | `COSTURAS_INTERNAS_RESUMEN.md` 6 y 7 | se acepta con su corte |
| **5** | **el CAVEAT DEL PREDICTOR** | `COSTURAS_INTERNAS_RESUMEN.md` 2 | **si**, con un ajuste: ver abajo |
| **6** | **el quinto puro degrada a SUB-PURO**, 7 de 10 | `BANCO_DE_TEXTOS.md`, tabla de racimos | **si**: la componente mide cinco miembros |
| **7** | **muere *cero podas en veinticuatro lecturas*** | `PENDIENTES.md`, ficha del barrido | se acepta con su banda |

**DOS AJUSTES QUE ESTA SESION LE HACE AL ENCARGO, y los dos son de una unidad:**

| | el encargo decia | **medido hoy** |
|---|---|---|
| **grafias del campo `fuente`** | 129 | **128** en primera posicion, **140** contando todas |
| **`mapaDeAlias` en `graph.ts`** | linea 107 | **linea 100** |

> **Ninguno mueve un argumento, y los dos se escriben igual.** Es el banco 9.21
> llevado un paso mas alla: **toda cifra lleva su corte, y ademas su CRITERIO.** *128
> grafias* y *140 grafias* son la misma medida con dos criterios, y sin decir cual se
> uso, las dos parecen contradecirse.

### LA OCTAVA: **EL VOLTEO DEL PUESTO 2.078, DECIDIDO. DE D A A**

**`elaboracion_fdd` contra `preparar_fdd`**, franquicias. **Llegaba propuesto y se
decide aqui**, porque el veredicto es de esta sesion.

**LA RAZON VIEJA CONTABA PASOS PROPIOS, dos contra dos, e invocaba el 9.22. LA VARA
LOS PESA:**

| nodo | lo propio | que es |
|---|---|---|
| `elaboracion_fdd` | que ninguna cuota quede sin divulgar; documentar la entrega con la pagina de recibo | **DOS LINEAS**: un criterio de completitud y una accion unica |
| `preparar_fdd` | incluir el contrato y los anexos; **preparar o crear una entidad corporativa nueva con estados financieros auditados si no se tienen** | una linea **y un PROCEDIMIENTO** |

> **Por la vara del banco 9.6.1, lo que `elaboracion_fdd` anade CABE EN LINEAS:
> REPITE.**

**Y EL 9.22 NO APLICA, que es lo que la razon vieja invocaba.** El enlace mutuo pide
que **cada uno EXPANDA UNA LINEA DISTINTA del otro**. Aqui **ninguno expande una linea
del otro: cada uno anade cosas suyas**. **Anadir no es expandir**, y confundirlos
convierte **cualquier par con material propio** en un enlace mutuo.

**DOS SENALES QUE REFUERZAN, y ninguna decide sola:** los ids son **la misma cosa en
dos verbos**, con titulos y etiquetas sinonimos, *Elabora tu Documento de Divulgacion*
contra *Redacta tu Documento de Divulgacion*; y **el grafo ya los trata como
intercambiables** en un punto, porque **los dos desembocan en `decision_fpr`**.

**SUPERVIVIENTE MEDIDO: `preparar_fdd`.** Por contenido, es el unico con procedimiento
propio; el cableado confirma sin contradecir, **6 contra 5** en quien los nombra.

**PERDIDAS QUE VIAJAN, y la segunda importa mas de lo que parece:** que **todas las
cuotas y fuentes de ingreso esten completamente divulgadas**, que es la falta clasica
de este documento; y **documentar la entrega con la pagina de recibo, Item 23**, que es
**lo unico del par que sirve para probar el cumplimiento despues**, cuando ya nadie
recuerda la fecha. **Si la fusion se lleva esa linea por delante, el catalogo pierde la
prueba y se queda con la obligacion.**

**Y NO ES UN ERROR DEL CRIBADO: ES DERIVA DE DOCTRINA.** La precision que lo decide,
**una advertencia o un criterio suelto es LINEA y no procedimiento**, se escribio
**despues** de este veredicto. **El lector de entonces conto bien con la doctrina de
entonces.**

### EL MARCADOR, RECOMPUTADO DEL ARCHIVO TRAS EL VOLTEO

| clase | antes | **despues** |
|---|---:|---:|
| **A** | 400 | **401** |
| B | 89 | 89 |
| C | 7 | 7 |
| **D** | 1.621 | **1.620** |
| **TOTAL** | **2.117** | **2.117** |

**Tasa global de A: 18,9% antes y despues** (400 y 401 sobre 2.117 redondean igual).
**Lo que si se mueve es `franquicias`: de 9 A sobre 46 a 10 sobre 46, del 19,6% al
21,7%.**

> **Y una nota de metodo que este volteo deja: UN VOLTEO NO SE APLICA PORQUE VENGA
> PROPUESTO. Se aplica porque, releido el par con la doctrina de hoy, la vara dice lo
> mismo que dice la propuesta.** Aqui coinciden. **Si no hubieran coincidido, se habria
> escrito la discrepancia y el veredicto se habria quedado como estaba.**

---

## 71. CHECKPOINT 2200 (TANDA DE 500), y el cierre de `franquicias`

**Corte de todas las cifras de esta seccion: puesto 2.219 del archivo.** El checkpoint
encargado era el del 2.200; se escribe al 2.219 **porque ahi cierra el dominio y
partirlo en el 2.200 habria dado una cifra de dominio incompleta**. Banco 9.21: toda
cifra lleva su corte.

### 71.1 EL MARCADOR, RECOMPUTADO DEL ARCHIVO

| clase | corte 2.117 | **corte 2.219** | delta |
|---|---:|---:|---:|
| **A** | 401 | **411** | +10 |
| B | 89 | **89** | 0 |
| C | 7 | **7** | 0 |
| **D** | 1.620 | **1.712** | +92 |
| **TOTAL** | **2.117** | **2.219** | +102 |

**Tasa global de A: 18,5%** (411 sobre 2.219). Venia del 18,9%.

### 71.2 LA TASA POR DOMINIO, que es como se lee (banco 9.27)

| dominio | pares leidos | A | B | C | D | **tasa de A** |
|---|---:|---:|---:|---:|---:|---:|
| `compras` | 155 | 1 | 2 | 0 | 152 | **0,6%** |
| `core` | 1.445 | 344 | 87 | 7 | 1.007 | **23,8%** |
| `entrega` | 171 | 2 | 0 | 0 | 169 | **1,2%** |
| `environmental` | 170 | 29 | 0 | 0 | 141 | **17,1%** |
| `exportacion` | 130 | 15 | 0 | 0 | 115 | **11,5%** |
| **`franquicias`** | **148** | **18** | **0** | **0** | **130** | **12,2%** |

> **La global no describe a nadie.** Entre `compras` al 0,6% y `core` al 23,8% hay
> cuarenta veces de diferencia, y el 18,5% del total no es la tasa de ningun dominio:
> es el peso de `core`, que aporta 1.445 de los 2.219 pares leidos.

### 71.3 CIERRE DE DOMINIO: `franquicias`

**Del puesto 2.072 al 2.219, 148 pares, cerrado.**

| | |
|---|---:|
| pares | **148** |
| A | **18** |
| B | **0** |
| C | **0** |
| D | **130** |
| **tasa de A** | **12,2%** |

> **CIFRA CORREGIDA EL 17 AGO 2026, y es la segunda correccion sobre este mismo
> numero.** Cerro primero en **13,5%** con 20 A. **La relectura conjunta con el auditor
> volteo los puestos 2.195 y 2.215 de A a D** (la vara aplicada al reves: se peso lo que
> la madre anade al hijo en vez de lo que el hijo anade a la madre). **Con los dos
> volteos, 18 A sobre 148 y la cifra final del dominio es 12,2%.** El detalle vive en
> la seccion 74.

**Correccion declarada sobre la cifra publicada en la seccion 70.** Alli se escribio
*franquicias del 19,6% al 21,7%*, y era correcto **a su corte**: 10 A sobre 46 pares,
que eran los unicos leidos del dominio al 2.117. **Con el dominio entero leido y los dos
volteos de la relectura aplicados, la cifra final es 12,2%**, no porque la de entonces
estuviera mal contada, sino porque **una tasa sobre 46 pares de 148 no es la tasa del
dominio: es la tasa de su cabecera**. Las tres conviven con su corte al lado.

**Fuente unica del dominio:** los 148 pares salen del mismo libro,
*Franchise Your Business* de Mark Siebert. **La homogeneidad de fuente no bajo la tasa
por si sola** (`environmental` esta al 17,1%), pero explica la forma de las A: **ninguna
es un choque entre dos libros, todas son un autor diciendo dos veces lo mismo en dos
sitios de su propio indice.**

### 71.4 LA VARA POR TRAMO (banco 9.6.1)

**Tramo 2.118 a 2.219: 102 pares, 8 A y 94 D. Tasa del tramo: 7,8%** (corregida el
17 ago 2026 por el volteo de 2.195 y 2.215; la cifra de la primera escritura fue 10 A y
9,8%).

| la vara dijo | pares | como se lee |
|---|---:|---|
| **CONTINUA** (trae procedimiento) | **35** | el hijo no cabia en una linea de la madre |
| **REPITE** (cabe en una linea) | **8** | los 8 A del tramo |
| no se invoco | 59 | objetos distintos, la vara no hacia falta |

**43 de 102 pares se decidieron con la vara**, y **en los 8 que dieron A el patron es
el mismo**: el nodo que muere trae **advertencias, criterios sueltos o acciones unicas**,
nunca un paso con decisiones dentro ni uno que se repita en el tiempo. **La precision
del 9.6.1 hizo todo el trabajo del tramo**: sin ella, cinco de esos ocho habrian pasado
por D.

> **Y la vara tiene una direccion, que este tramo aprendio a la mala.** Los dos pares
> volteados eran los dos unicos del tramo donde la pregunta se hizo al reves: **que
> anade la madre al hijo**. La pregunta correcta es **que anade el hijo a la madre**, y
> con la direccion invertida **cualquier nodo que enuncie sus pasos en forma compacta
> muere contra el que despliega uno de ellos**.

**Cero PENDIENTE DE DOCTRINA en el tramo.** Ninguna pareja pidio una regla que no
existiera. **Las escritas alcanzaron**, que es exactamente lo que decia el encargo.

### 71.5 LO QUE EL TRAMO DEJA ANOTADO

| figura | pares | nota |
|---|---:|---|
| **ARISTA QUE FALTA** | **24** | madre e hijo sin cable, o hermanas de una misma decision |
| **RACIMO CANDIDATO** | 8 menciones, **4 racimos** | ver abajo |
| **Falso hermano** | 4 | 2.184, 2.194, 2.201, 2.219 |
| **FIGURA DE PERSPECTIVA** | 2 | 2.121 y 2.187 |
| **SOLAPE DECLARADO** | 2 | 2.178 y 2.193 |
| **GEMELO por vigilar** | 2 | 2.207 y 2.217 |
| **PROCEDIMIENTO COMPARTIDO** | 2 | 2.139 y 2.175 |
| **TENSION DECLARADA** | 1 | 2.193 |
| **ADVERTENCIA DUPLICADA** | 1 | 2.186 |
| **LAS DOS RAMAS DE LA BIFURCACION** | 1 | 2.198 |

**LOS CUATRO RACIMOS DE `franquicias`:**

1. **LA FRANQUICIA INADVERTIDA**, el mas cargado: `comprender_definicion_legal_franquicia`,
   `deteccion_franquicia_inadvertida`, `prevenir_franquicias_inadvertidas` y
   `estructuras_combinadas_franquicia`. **Cuatro nodos sobre la misma prueba de tres
   elementos y ni una arista entre ellos.** El cuarto **repitio dos veces** (2.181 y
   2.207) y los dos del medio son **candidatos a gemelo**.
2. **EL DINERO DEL FRANQUICIADOR**, cinco miembros con cabeza clara:
   `cinco_categorias_costos_franquicia` contiene a `estimacion_inversion_inicial_franquiciador`
   en su paso 2 y a `costos_preparacion_franquicia` en su paso 6, y es **el hijo que
   despliega el paso 1 de `capitalizacion_adecuada_del_franquiciador`** (2.215, leido D
   tras la relectura); `principio_apalancamiento_numero_magico` es el unico con doctrina
   propia. **Cero aristas entre los cinco, y la del 2.215 es candidata de fase 04.**
3. **EL CANAL CORPORATIVO**, cuatro miembros: `mix_ubicaciones_corporativas_franquicia`,
   `franquicia_mas_crecimiento_corporativo_hibrido`, `estrategia_multicanal_expansion`
   y `combinar_crecimiento_corporativo_y_franquicia`, que **repitio** en el 2.204.
4. **EL MENSAJE**: `mensaje_marketing_franquicia`, `multiples_compradores_influyentes`
   (que es su paso 1 entero) y `motivaciones_reales_franquiciado`.

**Y una silueta medida que sigue creciendo (banco 9.6.1, la mayoria manda):**
`evaluacion_necesidad_franquiciar` nombra en su paso 6 **tres ventajas** de franquiciar,
**cada una tiene nodo propio y ninguna tiene arista con la madre**; en el 2.205 aparecio
**una cuarta ventaja con nodo propio, `rentabilidad_incrementada_franquicia`, que la
madre ni siquiera nombra**. **Cero de cuatro: la silueta ni acusa ni exculpa, y manda el
contenido**, que es lo que se hizo en los cinco pares.

---

## 72. CHECKPOINT 2300, y el dominio que dobla a todos los demas

**Corte de todas las cifras de esta seccion: puesto 2.300 del archivo.** `health_safety`
NO esta cerrado: llega hasta el 2.411 y aqui van leidos 81 de sus 192 pares. **Toda
tasa de este dominio es provisional y lleva su corte al lado** (banco 9.21).

### 72.1 EL MARCADOR, RECOMPUTADO DEL ARCHIVO

| clase | corte 2.219 | **corte 2.300** | delta |
|---|---:|---:|---:|
| **A** | 409 | **439** | +30 |
| B | 89 | **89** | 0 |
| C | 7 | **7** | 0 |
| **D** | 1.714 | **1.765** | +51 |
| **TOTAL** | **2.219** | **2.300** | +81 |

**Tasa global de A: 19,1%.** Subio del 18,4%, **y la subida entera la produce un solo
dominio**.

> **Cifras corregidas el 17 ago 2026.** La primera escritura de esta tabla decia 411 y
> 441, con el corte 2.219 al 18,5% y el 2.300 al 19,2%. **El volteo de los puestos 2.195
> y 2.215 de A a D resta dos A a los dos cortes por igual**, asi que **el delta de +30 no
> cambia**: lo que cambia es el punto de partida y el de llegada. Detalle en la seccion 74.

### 72.2 LA TASA POR DOMINIO (banco 9.27)

| dominio | pares leidos | A | B | C | D | **tasa de A** | estado |
|---|---:|---:|---:|---:|---:|---:|---|
| `compras` | 155 | 1 | 2 | 0 | 152 | **0,6%** | cerrado |
| `core` | 1.445 | 344 | 87 | 7 | 1.007 | **23,8%** | cerrado |
| `entrega` | 171 | 2 | 0 | 0 | 169 | **1,2%** | cerrado |
| `environmental` | 170 | 29 | 0 | 0 | 141 | **17,1%** | cerrado |
| `exportacion` | 130 | 15 | 0 | 0 | 115 | **11,5%** | cerrado |
| `franquicias` | 148 | 18 | 0 | 0 | 130 | **12,2%** | cerrado |
| **`health_safety`** | **81 de 192** | **30** | 0 | 0 | 51 | **37,0%** | **abierto, 42% leido** |

> **`health_safety` esta al 37,0% con 81 pares leidos: es la tasa mas alta del archivo
> entero, mas de la mitad por encima de `core`, que era el techo hasta hoy.** Con 111
> pares sin leer la cifra puede moverse, y no en cualquier direccion: **la cola del
> dominio baja de similitud semantica, y en todos los dominios anteriores la tasa cae
> conforme baja la similitud.** La cifra de cierre sera mas baja que 37,0%. **Cuanto,
> no se sabe hasta leerla, y por eso queda escrita como provisional y no como final.**

### 72.3 POR QUE ESTE DOMINIO REPITE TANTO, y no es lo que parece

**La repeticion de `health_safety` NO viene de dos autores que coinciden. Viene de UN
MISMO CONCEPTO EXTRAIDO VARIAS VECES DEL MISMO LIBRO.** La prueba esta en los propios
ids:

| senal en el id o el titulo | ejemplo | pares |
|---|---|---|
| **sufijo numerico** | `drift_hacia_el_fallo_2`, `ciclo_de_culpa_2`, `defensas_en_profundidad_2` y `_3`, `cultura_justa_3` | 2.222, 2.226, 2.272, 2.283 |
| **titulo espejo** | `new_view_vs_old_view` contra `old_view_vs_new_view_human_error` | 2.221 |
| **una preposicion de diferencia** | `confusion_de_modos_automatizacion` contra `confusion_modos_automatizacion` | 2.235 |
| **mismo titulo, distinto oficio** | `construccion_linea_tiempo` contra `construccion_timeline_resolucion` | 2.249, y ese dio **D** |

**De las 30 A del tramo, 24 son entre nodos de la MISMA fuente.** Las 6 restantes cruzan
fuentes, y ahi aparece **una figura nueva del tramo, LA MISMA NORMA EN DOS FOLLETOS**
(2.232): OSHA3885 y OSHA3886 cubren el mismo requisito de capacitacion con distinto
detalle. **No son dos escuelas discrepando: es un organismo publicando dos veces.**

**Y el contraste importa: `franquicias`, tambien de fuente unica, cerro en 12,2%.** La
fuente unica no basta para explicar el 37,0%. **Lo que lo explica es que el mismo
concepto tiene tres y cuatro nodos, no que el autor sea uno solo.**

### 72.4 LA VARA POR TRAMO (banco 9.6.1)

**Tanda completa hasta aqui, 2.118 a 2.300: 183 pares, 38 A y 145 D. Tasa 20,8%**
(corregida el 17 ago 2026: la primera escritura decia 40 A y 21,9%).

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **43** |
| **REPITE** | **38** |
| no se invoco | 102 |

**81 de 183 pares se decidieron con la vara, y en el tramo de `health_safety` casi todos.**
El patron de las 30 A es siempre el mismo: **lo que el nodo que muere anade son
advertencias, criterios sueltos, acciones unicas, prohibiciones o principios enunciados**,
y lo que el superviviente conserva es **una taxonomia nombrada, un test que se puede
hacer, o un mecanismo que actua en el tiempo**.

**Cero PENDIENTE DE DOCTRINA en 183 pares.** Ninguna pareja pidio una regla que no
existiera.

### 72.5 LOS RACIMOS ABIERTOS EN `health_safety`

| racimo | miembros | repetidores |
|---|---:|---|
| **la vieja y la nueva vision** | **6** | `old_view_vs_new_view_human_error`, `vieja_vision_vs_nueva_vision_seguridad`, `new_view_vs_old_view_de_error_humano` (×2) |
| **el sesgo retrospectivo** | **6** | `evitar_sesgo_retrospectivo_hindsight` (×2), `sesgo_retrospectivo_hindsight` |
| **las defensas** | **5** | `defensas_en_profundidad_2` (×2) |
| **las condiciones latentes** | **5** | ninguno todavia |
| **el error como sintoma** | **5** | `errores_como_consecuencia` (×3), `human_error_como_sintoma` (×2), `falla_sistemica_vs_error_individual` |
| **la deriva** | 3 | `drift_hacia_el_fallo_2` (×3) |
| **la cultura justa** | 3 | `cultura_justa` |
| **el error de mantenimiento** | 3 | `omisiones_en_mantenimiento` |
| **la gestion del error** | 3 | ninguno todavia |

**Ninguno de estos racimos tiene UNA SOLA arista entre sus miembros.**

### 72.6 DOS CONDICIONES VIVAS, y por que no se resuelven par a par

**`drift_hacia_el_fallo_2` repitio TRES veces contra TRES supervivientes distintos**
(`deriva_hacia_el_fallo`, `drift_hacia_el_fallo` y `normalizacion_de_la_desviacion`), y
**`errores_como_consecuencia` tambien tres** (`falla_sistemica_vs_error_individual`,
`human_error_como_sintoma` y `riesgos_del_enfoque_en_error_humano`).

> **Un nodo que repite contra tres madres distintas no elige superviviente en ninguna de
> las tres lecturas: lo elige el racimo.** El veredicto del par dice *este no aporta*, y
> eso es firme. **Quien se queda con su contenido es una decision de la fusion, no del
> cribado**, y queda anotada como condicion viva.

**Y hay una CADENA DE ABSORCION medida:** `errores_como_consecuencia` repite contra
`falla_sistemica_vs_error_individual` (2.242), y `falla_sistemica_vs_error_individual`
repite contra `fallas_activas_condiciones_latentes` (2.273). **Tres nodos, una cadena, y
solo el ultimo queda en pie.** El del medio **sobrevive en un par y muere en otro**, que
es exactamente lo que la doctrina permite: **la clase es del par, no del nodo.**

### 72.7 UNA FIGURA NUEVA: EL HERMANO QUE CORRIGE AL HERMANO

En el puesto **2.283**, `defensas_en_profundidad_3` pide **evaluar si hay dependencias
ocultas entre capas que se asumen independientes**. `defensas_en_profundidad_2` pide,
literalmente, **evaluar la integridad de cada capa de forma independiente**. **El segundo
desmiente el supuesto del primero, y los dos son del mismo autor y del mismo libro.**

**No es contradiccion con una regla vigente ni con una cifra publicada**, asi que no
detuvo el cribado: **queda declarada**. Lo mismo pasa con el principio de redundancia
del `_2` y la advertencia de complacencia por exceso de defensas del `_3`.

---

## 73. REPORTE CONSOLIDADO DE LA TANDA, del puesto 2.118 al 2.300

**Corte: puesto 2.300.** La tanda encargada iba del 2.118 al 2.617. **Van 183 pares de
500.** Lo que sigue reporta **lo leido**, y la seccion 73.8 nombra **lo que falta y donde
retomarlo**, para que ninguna cifra de aqui se lea como cifra de la tanda entera.

### 73.1 CIFRAS

| | |
|---|---:|
| pares leidos en la tanda | **183** |
| A | **38** |
| B | **0** |
| C | **0** |
| D | **145** |
| **tasa de A de la tanda** | **20,8%** |

**Y esa cifra sola no dice nada, porque los dos tramos no se parecen** (banco 9.27):

| tramo | dominio | pares | A | **tasa** |
|---|---|---:|---:|---:|
| 2.118 a 2.219 | `franquicias` | 102 | 8 | **7,8%** |
| 2.220 a 2.300 | `health_safety` | 81 | 30 | **37,0%** |

**Casi cuatro veces de diferencia entre dos tramos consecutivos del mismo cribado, con
la misma vara y el mismo lector.** El archivo global queda en **A 439, B 89, C 7, D
1.765 sobre 2.300, tasa 19,1%**.

**Un dominio cerrado: `franquicias`, 148 pares, 18 A, 12,2%.**
**Un dominio abierto: `health_safety`, 81 de 192 leidos, 30 A, 37,0% PROVISIONAL.**

### 73.2 FIGURAS NUEVAS Y CRECIDAS

**Nuevas de esta tanda:**

| figura | puesto | que es |
|---|---|---|
| **LA MISMA NORMA EN DOS FOLLETOS** | 2.232 | la repeticion cruza fuentes del **mismo organismo**: OSHA3885 y OSHA3886 cubren el mismo requisito con distinto detalle. No son dos escuelas, es una entidad publicando dos veces |
| **EL HERMANO QUE CORRIGE AL HERMANO** | 2.283 | `defensas_en_profundidad_3` pide buscar **dependencias ocultas entre capas que se asumen independientes**; `defensas_en_profundidad_2` pide evaluar cada capa **de forma independiente**. Un nodo del catalogo desmiente el supuesto de otro, del mismo autor |
| **MISMO TITULO, DISTINTO OFICIO** | 2.249 | `construccion_linea_tiempo` y `construccion_timeline_resolucion` se llaman igual y hacen cosas distintas: uno reune datos del sistema, el otro **analiza el habla segundo a segundo, con silencios, solapes y cambios de ritmo**. Dio **D** |
| **ADVERTENCIA DUPLICADA** | 2.186 | la misma advertencia literal en dos nodos, y ninguno repite porque cada uno trae ademas materia propia |
| **CADENA DE ABSORCION** | 2.242 y 2.273 | tres nodos, dos veredictos A encadenados, **solo el ultimo queda en pie**; el del medio sobrevive en un par y muere en otro |
| **EL TITULO PROMETE LO QUE LOS PASOS NO DAN** | 2.247 | `hoist_auxiliary_equipment_safety` nombra montacargas en su titulo y ninguno de sus cinco pasos habla de montacargas. No cambia el veredicto, queda anotado |

**Crecidas, que ya existian:**

- **ARISTA QUE FALTA: 48 pares** de 183, el hallazgo mas frecuente con diferencia.
- **FIGURA DE PERSPECTIVA: 3.** El 2.121 (desventaja por unidad, ventaja en agregado),
  el 2.187 (el mismo mensaje calibrado al reves segun el segmento) y el **2.287, el
  mejor de los tres: el mismo autor sostiene que el perfil de riesgo es propio de cada
  dominio y que las condiciones latentes son iguales en todos. No se contradice,
  delimita.**
- **Falso hermano: 5.** Por el titulo (2.184, entrenar), por la palabra (2.194
  inversionista, 2.245 escalera), por el numero (2.201, los tres), por el verbo (2.219,
  comparar).
- **SOLAPE DECLARADO: 19.** **TENSION DECLARADA: 1** (2.193, un nodo pide siete
  contactos en siete dias y el otro se titula *evitar el acoso*).
- **GEMELOS POR VIGILAR: 5 parejas**, todas en `health_safety`.
- **PROCEDIMIENTO COMPARTIDO: 2** (2.139 y 2.175, un hijo que sirve a dos madres).

### 73.3 NOMINAS Y RACIMOS

**En `franquicias`, cuatro racimos, todos sin una sola arista entre miembros:**

| racimo | miembros | forma |
|---|---:|---|
| **la franquicia inadvertida** | **4** | el mas cargado del dominio; `estructuras_combinadas_franquicia` **repitio dos veces** y los dos del medio son candidatos a gemelo |
| **el dinero del franquiciador** | **5** | **cerro cobertura**: `cinco_categorias_costos_franquicia` contiene a `estimacion_inversion_inicial_franquiciador` en su paso 2 y a `costos_preparacion_franquicia` en su paso 6, y es **el hijo que despliega el paso 1 de `capitalizacion_adecuada_del_franquiciador`**, leido D tras la relectura |
| **el canal corporativo** | 4 | `combinar_crecimiento_corporativo_y_franquicia` repitio |
| **el mensaje** | 3 | `multiples_compradores_influyentes` es el paso 1 entero de `mensaje_marketing_franquicia` |

**En `health_safety`, nueve racimos, tambien sin una sola arista:**
la vieja y la nueva vision (**6**), el sesgo retrospectivo (**6**), las defensas (**5**),
las condiciones latentes (**5**), el error como sintoma (**5**), la deriva (3), la
cultura justa (3), el error de mantenimiento (3) y la gestion del error (3).

**Cambiaron de forma:** dos racimos dejaron de ser listas de parecidos y quedaron con
**cabeza medida**. En **el dinero del franquiciador**, la cabeza es
`cinco_categorias_costos_franquicia` porque **contiene a dos miembros por dentro**. En
**las defensas**, `defensas_en_profundidad_3` no solo contiene al `_2`: **lo corrige**.

**Una silueta medida que crecio** (banco 9.6.1): `evaluacion_necesidad_franquiciar`
nombra **tres ventajas** de franquiciar, **cada una tiene nodo propio y ninguna tiene
arista con la madre**; en el 2.205 aparecio **una cuarta ventaja con nodo propio que la
madre ni nombra**. **Cero de cuatro: la silueta ni acusa ni exculpa, y mando el
contenido.**

**Y una silueta que si mando** (2.274): `hoist_auxiliary_equipment_safety` enlaza con
`materials_handling_safety` y `machinery_equipment_safety` **y no** con
`powered_industrial_trucks_safety`. **Dos de tres es mayoria estricta: la jerarquia esta
establecida y el suelto es arista que falta.**

### 73.4 CONDICIONES VIVAS

1. **`drift_hacia_el_fallo_2` repitio TRES veces**, contra `deriva_hacia_el_fallo`,
   `drift_hacia_el_fallo` y `normalizacion_de_la_desviacion`.
2. **`errores_como_consecuencia` repitio TRES veces**, contra
   `falla_sistemica_vs_error_individual`, `human_error_como_sintoma` y
   `riesgos_del_enfoque_en_error_humano`.
3. **`human_error_como_sintoma`, `new_view_vs_old_view_de_error_humano`,
   `evitar_sesgo_retrospectivo_hindsight`, `ciclo_de_culpa`, `defensas_en_profundidad_2`
   y `estructuras_combinadas_franquicia` repitieron DOS veces cada uno.**
   `capitalizacion_adecuada_del_franquiciador` estaba en esta lista y **salio el 17 ago
   2026**: sus dos supuestas repeticiones eran la vara aplicada al reves, y **ya no repite
   ninguna vez**.

> **El veredicto del par es firme en los tres casos: ese nodo no aporta.** Lo que queda
> abierto es **quien se queda con su contenido**, y eso **no se decide par a par: lo
> decide el racimo**. Ninguna de estas condiciones bloquea el cribado.

4. **`health_safety` sigue abierto en 37,0% con 111 pares sin leer.** La cifra **bajara**
   (la cola pierde similitud y en todos los dominios anteriores la tasa cae con ella),
   pero **cuanto no se sabe hasta leerla**.

5. **PERDIDA QUE VIAJA Y HAY QUE VIGILAR (2.293):** la instruccion explicita de
   **redisenar la herramienta en vez de entrenar a la persona** es la unica accion
   correctiva directa del racimo del error como sintoma. Es LINEA para la clase, **y una
   perdida real si la fusion la deja caer**: el catalogo se quedaria con el diagnostico y
   sin el remedio.

### 73.5 PENDIENTES DE DOCTRINA

**Cero.** En 183 pares **ninguna pareja pidio una regla que no existiera**. Las escritas
alcanzaron, que es exactamente lo que decia el encargo.

**Lo que si hubo, y no es lo mismo, son tres tensiones declaradas sin regla que las
resuelva y sin que ninguna contradiga regla vigente ni cifra publicada:** la del 2.193
(siete contactos contra evitar el acoso), la del 2.283 (el hermano que corrige al
hermano) y la del 2.287 (riesgo local contra condicion latente universal). **Las tres
quedan escritas en su veredicto, no como pendiente.**

### 73.6 CORRECCIONES DECLARADAS

1. **`franquicias` no esta en 21,7% ni en 13,5%, esta en 12,2%, y se corrigio dos veces
   por dos motivos distintos.** La seccion 70 publico *del 19,6% al 21,7%* y **era
   correcto a su corte**: 10 A sobre **46** pares, los unicos leidos del dominio al
   2.117; **una tasa sobre 46 pares de 148 es la tasa de una cabecera, no la de un
   dominio**, y con el dominio entero fueron 20 A sobre 148, el 13,5%. **La segunda
   correccion si es un error de lectura y no de corte**: la relectura conjunta con el
   auditor volteo los puestos 2.195 y 2.215, y el cierre real es **18 A sobre 148, 12,2%**
   (seccion 74). Las tres cifras conviven con su corte al lado (banco 9.21).
2. **La tasa global bajo y despues subio, y ninguna de las dos cosas dice lo que
   parece.** Del 18,9% al 18,5% al 2.219 (por 102 pares de un dominio tranquilo) y al
   19,2% al 2.300 (por 81 pares de uno que repite el triple). **La global se mueve por
   composicion, no por criterio.**
3. **DOS volteos sobre veredictos ya registrados**, 2.195 y 2.215, ambos de A a D,
   ambos con correccion declarada dentro de su propia razon. **Es lo unico de este
   reporte que cambio de clase**, y salio de la relectura del auditor, no de una
   relectura propia (seccion 74).

### 73.7 LAS 38 A NUEVAS, con las mas discutibles marcadas

> **Encabezado corregido el 17 ago 2026.** Eran 40. **Los puestos 2.195 y 2.215 salieron
> de esta lista** porque la relectura conjunta con el auditor los volteo a D, y **eran dos
> de los cinco que esta misma seccion habia marcado como discutibles**. Quedan tachados
> abajo, no borrados: **una lista de A que oculta las que se cayeron no sirve para medir
> nada.**

**`franquicias`, 8:**

| puesto | muere | sobrevive |
|---|---|---|
| 2.127 | `referidos_franquiciados_existentes` | **fusion mutua**, ninguno domina |
| 2.145 | `mito_control_calidad_corporativo` | `motivated_management_franquiciado` |
| 2.181 | `estructuras_combinadas_franquicia` | `deteccion_franquicia_inadvertida` |
| 2.190 | `perdida_control_operativo` | `gestion_terminacion_franquiciado` |
| ~~2.195~~ | ~~`capitalizacion_adecuada_del_franquiciador`~~ | **VOLTEADA A D** el 17 ago 2026 |
| 2.196 | `confidencialidad_manual_operaciones` | `desarrollar_manual_operaciones` |
| 2.202 | `marketing_en_ferias_comerciales_de_franquicias` | `ferias_comerciales_franquicia` |
| 2.204 | `combinar_crecimiento_corporativo_y_franquicia` | `mix_ubicaciones_corporativas_franquicia` |
| 2.207 | `estructuras_combinadas_franquicia` | `prevenir_franquicias_inadvertidas` |
| ~~2.215~~ | ~~`capitalizacion_adecuada_del_franquiciador`~~ | **VOLTEADA A D** el 17 ago 2026 |

**`health_safety`, 30:**

| puesto | muere | sobrevive |
|---|---|---|
| 2.221 | `old_view_vs_new_view_human_error` | `new_view_vs_old_view` |
| 2.222 | `drift_hacia_el_fallo_2` | `deriva_hacia_el_fallo` |
| 2.223 | `rutas_de_salida_y_puertas_de_emergencia` | `rutas_salida_planificacion_emergencias` |
| 2.226 | `drift_hacia_el_fallo_2` | `drift_hacia_el_fallo` |
| 2.230 | `responsabilidad_prospectiva` | `rendicion_cuentas_prospectiva` |
| 2.232 | `capacitacion_conciencia_programa` | `capacitacion_educacion_seguridad` |
| 2.233 | `ciclo_de_culpa` | `dysfunctional_organizational_culture_patterns` |
| 2.235 | `confusion_modos_automatizacion` | `confusion_de_modos_automatizacion` |
| 2.236 | `defensas_en_profundidad_2` | `defensas_en_profundidad` |
| 2.237 | `drift_hacia_el_fallo_2` | `normalizacion_de_la_desviacion` |
| 2.242 | `errores_como_consecuencia` | `falla_sistemica_vs_error_individual` |
| 2.244 | `evitar_sesgo_retrospectivo_hindsight` | `reconstruccion_contexto_situacional` |
| 2.250 | `niveles_de_madurez_de_seguridad` | `clasificacion_sistemas_por_nivel_seguridad` |
| 2.252 | `declive_teoria_manzana_podrida` | `accident_proneness_fallacy` |
| 2.253 | `vieja_vision_vs_nueva_vision_seguridad` | `nueva_vision_organizacion_linea_seguridad` |
| **2.255** | `cultura_justa` | `cultura_justa_organizacional` |
| 2.261 | `errores_como_consecuencia` | `human_error_como_sintoma` |
| **2.264** | `omisiones_en_mantenimiento` | `vulnerabilidad_instalacion` |
| 2.265 | `areas_riesgo_primario` | `clasificacion_riesgos_por_dominio` |
| 2.267 | `errores_como_consecuencia` | `riesgos_del_enfoque_en_error_humano` |
| 2.268 | `critica_perdida_de_conciencia_situacional` | `evitar_perdida_situacion_awareness` |
| 2.272 | `ciclo_de_culpa` | `ciclo_de_culpa_2` |
| 2.273 | `falla_sistemica_vs_error_individual` | `fallas_activas_condiciones_latentes` |
| **2.280** | `human_error_como_sintoma` | `enfoque_situacional_vs_personal` |
| 2.281 | `sesgo_retrospectivo_hindsight` | `sesgo_retrospectivo_hindsight_2` |
| 2.283 | `defensas_en_profundidad_2` | `defensas_en_profundidad_3` |
| 2.290 | `new_view_vs_old_view_de_error_humano` | `investigacion_new_view` |
| 2.292 | `new_view_vs_old_view_de_error_humano` | `perspectiva_dentro_del_tunel` |
| **2.293** | `human_error_como_sintoma` | `error_humano_vs_falla_mecanica` |
| 2.294 | `evitar_sesgo_retrospectivo_hindsight` | `evitar_shopping_bag` |

**LAS CINCO MAS DISCUTIBLES, y por que cada una lo es:**

1. **2.195 y 2.215: SE VOLTEARON, y la prediccion escrita aqui se cumplio literal.**
   Esta seccion decia *si el auditor sostiene que una pregunta distinta merece nodo aunque
   se conteste en una linea, este veredicto se voltea, y con el el 2.215*. **El auditor lo
   sostuvo, los dos se voltearon, y el motivo real resulto ser mejor que el previsto**: no
   era que una pregunta distinta merezca nodo, era que **la vara se habia aplicado al
   reves**, pesando lo que la madre anade al hijo. Detalle en la seccion 74.
2. **2.255.** Muere el nodo de **cinco** pasos contra el de **cuatro**, y lo que se va
   como linea absorbida es **la garantia de que los supervisores apliquen los criterios
   igual**. Es la unica linea del par que impide que una cultura justa se vuelva
   arbitraria segun quien juzgue.
3. **2.264.** Lo que muere aporta **firma paso a paso** e **inspeccion independiente
   antes de la puesta en servicio**. Son calificativos por la vara, **y son controles
   reales por el oficio.**
4. **2.280 y 2.293 juntas.** `human_error_como_sintoma` **sobrevivio en el 2.261 y murio
   en los dos siguientes**, y en las tres lecturas la bisagra fue la misma linea:
   **redisenar la herramienta en vez de entrenar a la persona**. Sobrevivio donde era el
   unico que la decia, y murio donde el otro tambien redisena o donde el otro trae tres
   blancos de analisis. **Es doctrinalmente correcto y practicamente incomodo: la unica
   accion correctiva del racimo viaja como linea absorbida en dos fusiones distintas.**
5. **2.221.** Los titulos son el mismo contraste dicho al derecho y al reves, y lo que
   muere aporta **el Bad Apple en las politicas de cultura justa** y **la tabla
   comparativa como herramienta de dialogo con la direccion**. Son puntero y accion
   unica, **pero la tabla es el unico instrumento de conversacion con directivos del
   racimo entero.**

### 73.8 LO QUE FALTA DE LA TANDA, y donde se retoma

**Van 183 de 500. Faltan 317 pares, del 2.301 al 2.617.**

| tramo | dominio | pares | estado |
|---|---|---:|---|
| 2.301 a 2.411 | `health_safety` | **111** | pendiente; **cierra el dominio** y fija su cifra final |
| 2.412 a 2.617 | `quality` | **206** | pendiente; **abre el dominio**, que no cierra en esta tanda |

**Checkpoints pendientes: 2.400, 2.500 y 2.600.** El del 2.300 esta escrito en la
seccion 72 y el del 2.200 en la 71.

**El archivo esta en 2.300 sin huecos y sin duplicados.** El cribado se retoma en el
**2.301** con `python scripts/volcar_pares.py 2301 2312` y se registra con
`python scripts/registrar_veredictos.py`, que **toma dominio y nodos de la cola** para
que no se pueda registrar un veredicto contra un par que no existe.

**Cero nodos tocados en toda la tanda. El modo de cierre se respeto entero: se leyo y se
documento.**


---

## 74. LA RELECTURA CONJUNTA DEL 2.195 Y EL 2.215, y la direccion de la vara

**17 ago 2026, con el caso del auditor delante. Los dos puestos estaban en A y los dos
pasan a D.** Es el unico cambio de clase de toda la tanda 2.118 a 2.300.

### 74.1 EL CASO DEL AUDITOR, y la verificacion contra el grafo

**Lo que sostuvo el auditor:** que `cinco_categorias_costos_franquicia` **es el
procedimiento del paso 1** de `capitalizacion_adecuada_del_franquiciador`, la linea
*estimar el presupuesto* desplegada en siete pasos, y que por la vara eso es **madre e
hijo, D**; y que en el 2.195 hay **una linea compartida** y **procedimiento propio de
cada lado**, y eso tambien es **D**.

**Verificado contra `master_graph.json`, y los entregables son la prueba mas limpia:**

| nodo | pasos | **entregable verificado** |
|---|---:|---|
| `capitalizacion_adecuada_del_franquiciador` | 4 | **Presupuesto de capitalizacion del programa con fuente de fondos definida** . **DOS productos** |
| `cinco_categorias_costos_franquicia` | 7 | **Un presupuesto detallado y sumado, dividido en las cinco categorias** . **UNO, y es el primero de los dos de la madre** |
| `franquicia_como_capital_alternativo` | 4 | **Analisis comparativo de capital requerido, expansion propia contra expansion via franquicia** . una **comparacion**, no un presupuesto |

**El paso 1 de la madre dice** *estimar el presupuesto necesario para desarrollar el
sistema de franquicia (documentos legales, manuales, marketing)*. **El hijo lo despliega
en las cinco categorias nombradas** (desarrollo, legal, marketing, personal y
preparacion), **mas la decision que dimensiona todo lo demas**, *cuantas franquicias
quieres vender en tu primer ano*, **mas el cierre de sumarlo en un solo presupuesto**.

### 74.2 EL ERROR, nombrado: LA VARA TIENE DIRECCION

**El banco 9.6.1 pregunta QUE ANADE EL HIJO A LA MADRE.** La razon vieja del 2.215
pregunto lo contrario: **que anade la madre al hijo**. Encontro tres lineas sobre la
fuente de fondos y mato a la madre.

> **CON LA DIRECCION INVERTIDA, CUALQUIER NODO QUE ENUNCIE SUS PASOS EN FORMA COMPACTA
> MUERE CONTRA EL QUE DESPLIEGA UNO DE ELLOS.** Y eso liquidaria a **todas las madres del
> catalogo**: `decision_franquiciar_vs_expansion_propia`, `evaluacion_necesidad_franquiciar`,
> `seleccion_estructura_franquicia`, `preparar_fdd`, `programa_entrenamiento_franquiciados`.
> **Todas enuncian pasos que otros nodos despliegan. Ninguna repite por eso.**

**Y la formulacion util, que es la que se lleva al banco como precision de uso:**

> **UNA LINEA QUE TARDA SIETE PASOS EN EJECUTARSE NO ES UNA LINEA: ES UN PROCEDIMIENTO
> NOMBRADO EN UNA LINEA.** La prueba de que el paso 1 de la madre es un procedimiento
> **es que existe el hijo que lo ejecuta**. Una madre puede ser un enunciado compacto de
> sus propios pasos: **eso es lo que es una madre, y no se la mata por serlo.**

**Por que el resto del tramo no esta contaminado:** los otros 24 pares de madre e hijo
del tramo (2.167, 2.168, 2.175, 2.179, 2.182, 2.185, 2.192, 2.206, 2.210, 2.211, 2.212,
2.213, 2.216, 2.217 y los del primer lote) **se leyeron en la direccion correcta y todos
dieron D**. Los dos volteados **son los dos unicos donde la pregunta se hizo al reves**,
y son **los dos que el propio reporte marco como discutibles**.

### 74.3 EL 2.195, que no es madre e hijo

**Aqui no hay despliegue: hay una linea compartida y dos procedimientos ajenos.**

| | `capitalizacion_adecuada_del_franquiciador` | `franquicia_como_capital_alternativo` |
|---|---|---|
| **la linea compartida** | paso 1, el capital del sistema | paso 3, el capital del sistema |
| lo suyo | **presupuestar** (que el 2.215 demuestra que es procedimiento) y **financiar**: elegir entre ahorros, caja o cuotas, no depender de las cuotas iniciales, validar la estructura | **comparar rutas de capital**: propio o deuda contra franquicia, cuanto haria falta para 10, 50 o 100 unidades, y el riesgo contingente aceptado |
| pregunta que contesta | **con que dinero se paga el programa** | **si franquiciar es la ruta de capital** |

**Por la vara, CONTINUA. Sano.**

### 74.4 EL RECOMPUTO, del archivo

| | antes | **despues** |
|---|---:|---:|
| A del archivo | 441 | **439** |
| D del archivo | 1.763 | **1.765** |
| **tasa global** (corte 2.300) | 19,2% | **19,1%** |
| A de `franquicias` | 20 | **18** |
| **tasa de `franquicias`** (cierre) | 13,5% | **12,2%** |
| A del tramo 2.118 a 2.219 | 10 | **8** |
| **tasa del tramo** | 9,8% | **7,8%** |
| A de la tanda 2.118 a 2.300 | 40 | **38** |
| **tasa de la tanda** | 21,9% | **20,8%** |
| la vara: CONTINUA | 41 | **43** |
| la vara: REPITE | 40 | **38** |

**Secciones actualizadas con la cifra nueva:** 71.2, 71.3, 71.4, 71.5, 72.1, 72.2, 72.3,
72.4, 73.1, 73.3, 73.4, 73.6 y 73.7. **Ninguna cifra vieja se borro: todas quedan con su
corte al lado** (banco 9.21).

### 74.5 LO QUE ARRASTRA, y no es solo aritmetica

1. **`capitalizacion_adecuada_del_franquiciador` deja de ser un repetidor.** Estaba en la
   lista de nodos que repitieron dos veces (seccion 73.4) y **sale de ella: ya no repite
   ninguna vez.**
2. **El racimo del dinero del franquiciador cambia de forma.** Seguia con cinco miembros,
   pero **la cabeza no es la que se dijo**: `cinco_categorias_costos_franquicia` no
   absorbe a `capitalizacion_adecuada_del_franquiciador`, **es su hijo**.
3. **ARISTA QUE FALTA, candidata de fase 04.** Verificada contra el grafo: la madre viene
   de `riesgo_concepto_vs_amenaza_competitiva`, `evaluacion_riesgo_mercado_dinero_gestion`
   y `decision_intensidad_capital`, y va a `evaluacion_temperamento_franquiciador`. **No
   toca a su hijo por ningun lado.** Queda anotada aqui para que el recomputo del plan la
   recoja.


---

## 75. REPORTE CONSOLIDADO DEL TRAMO 2.301 A 2.376, y la prediccion del 2.300 cumplida

**Corte: puesto 2.376.** El encargo pedia del 2.301 al 2.617, 317 pares. **Van 76.** La
seccion 75.8 nombra lo que falta. **Ninguna cifra de aqui se lee como cifra del encargo
entero.**

### 75.1 CIFRAS

| | |
|---|---:|
| pares leidos en el tramo | **76** |
| A | **10** |
| B | **0** |
| C | **0** |
| D | **66** |
| **tasa de A del tramo** | **13,2%** |

**Archivo global al corte 2.376: A 449, B 89, C 7, D 1.831 sobre 2.376. Tasa 18,9%.**

> **Cifras corregidas el 17 ago 2026 por el barrido de direccion**, que volteo el puesto
> 2.338 de A a D. La primera escritura decia 12 A, 15,8% del tramo y 19,0% global.
> Detalle en la seccion 76.

### 75.2 LA PREDICCION DEL CHECKPOINT 2.300, CUMPLIDA Y MEDIDA

La seccion 72.2 escribio, con `health_safety` al **37,0%** y 111 pares sin leer:

> *La cifra puede moverse, y no en cualquier direccion: la cola del dominio baja de
> similitud semantica, y en todos los dominios anteriores la tasa cae conforme baja la
> similitud. **La cifra de cierre sera mas baja que 37,0%.** Cuanto, no se sabe hasta
> leerla.*

**Se leyeron 76 pares mas. Esto es lo que paso:**

| corte | pares leidos de `health_safety` | A | **tasa** |
|---|---:|---:|---:|
| 2.300 | 81 de 192 | 30 | **37,0%** |
| **2.376** | **157 de 192** | **40** | **25,5%** |
| el tramo nuevo solo (2.301 a 2.376) | 76 | 10 | **13,2%** |

> **La direccion acerto y la magnitud es grande: el tramo nuevo entrega menos de la mitad
> de la tasa del anterior, 13,2% contra 37,0%, y arrastra el acumulado del dominio del
> 37,0% al 25,5%.** Con 35 pares por leer, la cifra de cierre **seguira bajando**.
>
> **Y esto vuelve a decir lo mismo que la seccion 71 y la 72: una tasa parcial no es la
> tasa de un dominio.** El 37,0% publicado al 2.300 era correcto **a su corte** y hoy
> sobreestima el dominio en mas de diez puntos. **La regla ya no es una advertencia: esta
> medida dos veces, en `franquicias` y en `health_safety`.**

**Por que baja.** En la cabecera del dominio los pares eran **el mismo concepto extraido
dos veces** (ids con sufijo `_2`, titulos espejo, preposiciones de diferencia). En la
cola los pares son **objetos distintos que comparten vocabulario**: el fuego contra la
intoxicacion (2.370), el escalon contra el agujero (2.373), entender contra cumplir
(2.361), el deber del que organiza contra el derecho del que ejecuta (2.358).

### 75.3 LA VARA POR TRAMO (banco 9.6.1)

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **8** |
| **REPITE** | **12** |
| no se invoco | **56** |

**Solo 20 de 76 pares necesitaron la vara**, contra 81 de 183 en la tanda anterior. **Es
el mismo hecho contado de otro modo: en la cola del dominio la mayoria de los pares no
son madre e hijo ni gemelos, son cosas distintas que comparten palabras**, y para eso la
vara no hace falta.

**Cero PENDIENTE DE DOCTRINA en 76 pares.** Ninguna pareja pidio una regla que no
existiera. **En los 259 pares leidos desde el 2.118, cero.**

### 75.4 FIGURAS

**Nuevas de este tramo:**

| figura | puesto | que es |
|---|---|---|
| **LOS DOS SENTIDOS DEL MISMO INSTRUMENTO** | 2.323 | Tripod-Beta va **hacia atras** desde un accidente y Tripod-Delta va **hacia adelante** sin que haya pasado nada, con el mismo vocabulario de GFT. Un checklist de **220 items, 20 por GFT, trimestral** |
| **HERMANOS DE UNA MISMA MADRE** | 2.316 | dos hijos que abren **lineas distintas** de la misma madre, y por eso no se pisan |
| **LAS DOS CARAS DE LA MISMA DECISION** | 2.327 | `abandonar_arreglos_rapidos` dice **que no es un arreglo** y `hard_fixes_organizacionales` dice **que si lo es** |
| **A POR FUSION MUTUA** | 2.368 | los dos repiten y **ninguno domina**; el superviviente lo decide el racimo. Segundo caso del archivo tras el 2.127 |

**Crecidas:** **ARISTA QUE FALTA en 34 de 76 pares**, casi la mitad; **SOLAPE DECLARADO
en 15**; **FIGURA DE PERSPECTIVA 1** (2.329, el desajuste entre autoridad y
responsabilidad **escrito en primera persona del que ejecuta y en primera persona del que
organiza**); **dos siluetas medidas** (75.5).

### 75.5 NOMINAS, RACIMOS Y SILUETAS

**Racimos que crecieron:** la medicion que corrompe lo medido pasa a **5** miembros
(`cuestionar_vision_zero`, `responsabilidad_hacia_abajo_vs_rendicion_de_cuentas`,
`limitaciones_ltif_indicador`, `medidas_proceso_vs_resultado`,
`metas_de_seguridad_correctas`); las defensas a **6** con `trayectoria_del_accidente`;
las condiciones latentes a **5**; la cultura coordinadora a **3**.

**Dos siluetas medidas (banco 9.6.1, la mayoria manda):**

1. **`identificacion_evaluacion_peligros` tiene CUATRO hermanos leidos** que abren sus
   lineas: recopilacion (paso 1, **con arista**), inspeccion (paso 2, sin), investigacion
   (paso 4, sin) y emergencias y no rutinarias (sin). **Uno de cuatro es mitad o menos:
   la silueta ni acusa ni exculpa y mando el contenido**, que es lo que se hizo en los
   cuatro.
2. **`prevencion_control_peligros` dice en una linea *desarrollar un plan de
   implementacion*, tiene DOS hijos leidos** (`plan_control_peligros` e
   `implementacion_controles`) **y no enlaza con ninguno.**

**Precision sobre una silueta ya publicada (2.341):** la seccion 73.3 dijo que
`hoist_auxiliary_equipment_safety` enlaza con dos de sus tres hermanos y no con
`powered_industrial_trucks_safety`. **Sigue siendo cierto, y ahora se sabe por que: el
montacargas cuelga de `materials_handling_safety`, no del hoist.** La familia tiene **dos
centros y no uno**.

### 75.6 CONDICIONES VIVAS

1. **`errores_como_consecuencia` cae en A por NOVENA vez** (2.242, 2.261, 2.267, 2.303,
   2.311, 2.347, 2.362, 2.368 y 2.371). **Es la marca del archivo, y la lectura que deja
   es precisa: no es duplicado de nadie, es EL ENUNCIADO DE LA DOCTRINA SIN NINGUN
   INSTRUMENTO**, y por eso pierde contra cualquiera que traiga uno.
2. **Y la serie NO es mecanica, y hay prueba: el puesto 2.345 la rompe.** Contra
   `atribucion_retrospectiva_del_error`, que trabaja **la etiqueta** y no **la busqueda**,
   este mismo nodo **si aporta** (buscar sistematicamente los factores del lugar de
   trabajo y organizacionales) **y quedo en D**. Nueve A y una D, decididas cada una por
   lo que el otro nodo traia.
3. **`vieja_vision_vs_nueva_vision_seguridad` cae en A por TERCERA vez** (2.253, 2.309,
   2.352). Cuatro verbos sin contenido: diagnosticar, migrar, comunicar, redisenar.
4. **`human_error_como_sintoma` llega a TRES**, y con el **la perdida que viaja ya se
   anoto tres veces**: la instruccion de **redisenar la herramienta en vez de entrenar a
   la persona** es la unica accion correctiva directa del racimo, y en el 2.310 viaja
   hacia un nodo que es **analisis puro, sin un solo paso de remedio**.
5. **`health_safety` sigue abierto**, 157 de 192, **25,5% y bajando**.

### 75.7 LAS 10 A NUEVAS, con las discutibles marcadas

> **Eran 12. El 2.338 salio el 17 ago 2026**, volteado por el barrido de direccion, y
> **era uno de los tres que esta misma seccion habia marcado como discutibles.** Queda
> tachado abajo, no borrado.

| puesto | muere | sobrevive |
|---|---|---|
| 2.303 | `errores_como_consecuencia` | `enfoque_situacional_vs_personal` |
| 2.309 | `vieja_vision_vs_nueva_vision_seguridad` | `cultura_de_seguridad_interpretivista_funcionalista` |
| 2.310 | `human_error_como_sintoma` | `new_view_human_error` |
| 2.311 | `errores_como_consecuencia` | `error_humano_vs_falla_mecanica` |
| 2.328 | `reglas_parada_investigacion_accidentes` | `limite_busqueda_causas_pendulo` |
| **2.335** | `caso_descarrilamiento_nakina` | `condiciones_latentes_largo_plazo` **(superviviente corregido el 18 ago 2026)** |
| ~~2.338~~ | ~~`cuestionar_vision_zero`~~ | **VOLTEADA A D** el 17 ago 2026 |
| 2.347 | `errores_como_consecuencia` | `seduccion_modelo_persona` |
| 2.352 | `vieja_vision_vs_nueva_vision_seguridad` | `new_view_vs_old_view` |
| 2.362 | `errores_como_consecuencia` | `new_view_human_error` |
| **2.368** | **fusion mutua** | ninguno domina |
| ~~2.371~~ | ~~`errores_como_consecuencia`~~ | **VOLTEADA A D** el 18 ago 2026 |

**LAS TRES MAS DISCUTIBLES:**

1. **2.335.** Sobrevive **un estudio de caso** (`caso_descarrilamiento_nakina`, un
   descarrilamiento con una falla latente de 76 anos) y muere **la doctrina general** que
   sale de el. Por contenido la vara manda: el caso trae **el analisis geotecnico
   profundo frente a la inspeccion visual**, que es lo unico del par que dice como se
   encuentra una condicion latente enterrada. **Pero la fusion tiene que conservar el
   titulo generico**, o la regla queda colgada de un descarrilamiento concreto.
2. **2.338: SE VOLTEO, y por la razon que esta misma seccion adelanto.** Aqui se escribio
   que el que muere es **el unico nodo del catalogo que nombra la Vision Cero** y que su
   linea de **no usar el cero como excusa retroactiva** es el unico puente con la familia
   del sesgo retrospectivo. **Eso no era una perdida a vigilar: era la prueba de que la
   madre conservaba materia propia**, y por tanto de que la vara se habia aplicado al
   reves. **El par es madre e hijo y quedo en D** (seccion 76).
3. **2.368.** **Fusion mutua sin superviviente**: cada uno anade dos lineas y ninguno
   trae procedimiento. **Lo que se pierde si nadie lo mira: el nivel organizacional
   explicito, el entrenamiento contra el sesgo de atribucion, y la instruccion de usar el
   hallazgo para cambiar el sistema y no para senalar.**

### 75.8 LO QUE FALTA, y donde se retoma

**Van 76 de 317. Faltan 241 pares, del 2.377 al 2.617.**

| tramo | dominio | pares | estado |
|---|---|---:|---|
| 2.377 a 2.411 | `health_safety` | **35** | pendiente; **cierra el dominio y fija su cifra final** |
| 2.412 a 2.617 | `quality` | **206** | pendiente; **abre el dominio**, que no cierra aqui |

**Checkpoints pendientes: 2.400, 2.500 y 2.600.**

**LA PREDICCION SOBRE `quality`, escrita antes de leer un solo par.** El barrido paso
contra nodo dejo **742 candidatos** en `docs/PASO_NODO_CANDIDATOS.jsonl`, y asi se
reparten:

| dominio | candidatos | **sin arista** |
|---|---:|---:|
| **`quality`** | **323** | **296** |
| `core` | 298 | 229 |
| `environmental` | 32 | 32 |
| `franquicias` | 29 | 27 |
| `health_safety` | 27 | 16 |
| resto | 33 | 24 |

> **`quality` tiene mas candidatos que `core`, y `core` tiene diez veces mas pares en la
> cola.** Si el barrido acierta, **la cola de `quality` deberia entregar madre e hijo, no
> gemelos**: muchos **CONTINUA** por linea desplegada y muchas **ARISTA QUE FALTA**, con
> una tasa de A mas parecida a la cola de `health_safety` (13,2%) que a su cabecera
> (37,0%). **Queda escrito antes de leer para que se pueda comprobar despues.**

**El archivo esta en 2.376 sin huecos ni duplicados.** Se retoma en el **2.377** con
`python scripts/volcar_pares.py 2377 2385` y se registra con
`python scripts/registrar_veredictos.py`.

**Cero nodos tocados en todo el tramo. Modo de cierre respetado entero.**


---

## 76. EL BARRIDO DE DIRECCION sobre todas las A del archivo

**17 ago 2026. Corte: puesto 2.376.** Levantado por `scripts/barrido_direccion.py`, que
es **de solo lectura** sobre el archivo y sobre el grafo y **no cambia ni una clase**.

### 76.1 EL UNIVERSO, y por que se parte en dos

| | |
|---|---:|
| veredictos en el archivo | **2.376** |
| clase A | **451** |
| **A cuya razon invoca la vara** (la formula y sus variantes) | **295** (65,4% de las A) |
| de esas, **ELIGEN DIRECCION**, es decir nombran superviviente | **46** |
| de esas, **NO eligen direccion**: *REPITE con X* y nada mas | **249** |

> **LA PARTICION NO ES UN DETALLE DE FILTRADO: ES EL RESULTADO.** Una A que **no elige
> superviviente no puede estar al reves**, porque **nunca eligio un sentido.** Dice *sobra
> uno* y deja abierto cual, que es exactamente lo que la seccion 8 estableció desde el
> principio: **la A dice que sobra uno; no dice cual.**
>
> **El error de direccion solo existe donde la razon PESO una cosa contra la otra para
> decidir quien vive.** Y eso son **46 pares de 451 A: el 10,2%.**

**Las 249 sin direccion no quedan absueltas de todo: quedan absueltas de ESTE error.**
Su direccion sigue **sin decidir**, y decidirla es trabajo de la fusion (fase 04), no del
cribado. **Las 46 son las unicas que ya comprometieron una respuesta.**

**Reparto de las 46:** `franquicias` **6**, `health_safety` **40**. **Ninguna en `core`,
`compras`, `entrega`, `environmental` ni `exportacion`**, porque las razones de esos
dominios cierran con *REPITE con X. Candidato a fusion* y no nombran superviviente.

### 76.2 LA VERIFICACION, una a una, con criterio escrito

**EL CRITERIO, fijado antes de mirar:** una A esta al reves **si y solo si el nodo que
SOBREVIVE es el desarrollo de UNA SOLA LINEA del que MUERE**, es decir si el superviviente
**cabe entero dentro de un paso del muerto** y el muerto **conserva materia propia que el
superviviente no toca en ningun paso.**

**RESULTADO: 46 verificadas, 1 cayo, 45 sostenidas.**

| puesto | dominio | forma del par | veredicto de la verificacion |
|---:|---|---|---|
| **2.338** | `health_safety` | **MADRE E HIJO leidos al reves** | **CAE. A pasa a D** |
| 2.181, 2.190, 2.196, 2.202, 2.204, 2.207 | `franquicias` | gemelos o hijo que muere correctamente | **6 sostenidas** |
| las 39 restantes | `health_safety` | gemelos, o el hijo muriendo en el sentido correcto | **39 sostenidas** |

**EL CASO QUE CAE, 2.338.** `cuestionar_vision_zero` es **la madre** y dice en sus pasos 1
y 4, en una linea cada uno, traducir el compromiso de cero en acciones controlables y
disenar indicadores de proceso. `metas_de_seguridad_correctas` es **el hijo** y despliega
esas dos lineas en seis pasos. **Y la madre conserva lo que el hijo no toca en ningun
paso: que la meta de cero no se use como excusa retroactiva para decir que todo era
evitable, y hablar con claridad de sus limites reales.** El hijo mejora los indicadores;
**la madre discute si la meta misma es honesta.**

**EL CONTRASTE QUE SOSTIENE LAS 45.** El caso corriente de estas A **no es madre e hijo:
son gemelos**, dos nodos al mismo nivel que dicen lo mismo con otras palabras
(`drift_hacia_el_fallo_2` contra `drift_hacia_el_fallo`, `ciclo_de_culpa` contra
`ciclo_de_culpa_2`, `defensas_en_profundidad_2` contra `defensas_en_profundidad_3`). **En
un par de gemelos la vara no tiene direccion que equivocar**, porque ninguno es la madre.

**Y el segundo grupo son hijos que mueren BIEN**, que es lo que confunde y por eso se
escribe: en el **2.196**, `confidencialidad_manual_operaciones` desarrolla la palabra
*confidencial* del paso 5 de `desarrollar_manual_operaciones`. **Es madre e hijo, y el que
muere es EL HIJO.** Esa es la direccion correcta, y el 2.215 es su espejo exacto con el
error dentro.

### 76.3 LO QUE EL BARRIDO PROBO QUE NO SIRVE

Se implemento tambien **una prueba de cobertura lexica**: para cada par, que fraccion de
los pasos del nodo que muere aparece, por vocabulario, dentro del superviviente. La idea
era que **una A correcta exige que el muerto este contenido en el que vive.**

| | |
|---|---:|
| pares con direccion elegida | 46 |
| marcados **SOSPECHOSO** por la prueba lexica | **34** |
| de esos, **realmente al reves** | **1** |
| **precision de la prueba** | **3%** |

> **La prueba no discrimina, y la razon es del corpus: estos nodos REPITEN IDEAS CON
> PALABRAS DISTINTAS.** *Historial de pequenos cambios acumulados* y *brecha entre
> procedimiento escrito y practica real* son el mismo paso y no comparten una palabra.
>
> **LA CONSECUENCIA, y va mas alla de este barrido: cualquier deduplicacion mecanica por
> vocabulario que se plantee sobre este catalogo va a fallar del mismo modo.** La
> direccion se verifica **leyendo**, y el instrumento util no fue el contador de palabras
> sino **los entregables**, que en el 2.215 dijeron en una linea lo que la comparacion de
> pasos tardo un parrafo en decir.

**El script queda igual, con la prueba dentro y con su tasa de acierto escrita en la
cabecera**, para que nadie la use como si midiera algo.

### 76.4 EL RECOMPUTO

| | antes | **despues** |
|---|---:|---:|
| A del archivo | 451 | **450** |
| D del archivo | 1.829 | **1.830** |
| **tasa global** (corte 2.376) | 19,0% | **18,9%** |
| A de `health_safety` | 42 | **41** |
| **tasa de `health_safety`** (157 de 192) | 26,8% | **26,1%** |
| A del tramo 2.301 a 2.376 | 12 | **11** |
| **tasa del tramo** | 15,8% | **14,5%** |

**`franquicias` no se mueve: 18 A sobre 148, 12,2%.** Sus 6 A con direccion elegida se
sostuvieron todas.

### 76.5 LA CIFRA QUE SE REPORTA

> **295 A invocaban la vara. 46 elegian direccion. 1 cayo.**
>
> **Y contando los dos que el auditor ya habia tumbado, el archivo entero tiene TRES A
> escritas con la vara al reves, las tres del mismo lector y las tres en la misma tanda.**
> Dos las encontro la relectura ciega del auditor; **la tercera la encontro el barrido, y
> no habria salido sin la regla escrita primero.**


---

## 77. REPORTE CONSOLIDADO DEL TRAMO 2.301 A 2.388

**Corte: puesto 2.388.** El encargo pedia del 2.377 al 2.617, 241 pares; **van 12 de esa
tanda y 88 desde el 2.301.** La seccion 77.7 nombra lo que falta. **La R43 empieza por
los discutibles de la 77.6.**

### 77.1 CIFRAS

| | pares | A | D | **tasa** |
|---|---:|---:|---:|---:|
| **tramo 2.301 a 2.388** | **88** | **11** | **77** | **12,5%** |
| `health_safety` acumulado | **169 de 192** | 41 | 128 | **24,3%** |
| archivo global (corte 2.388) | 2.388 | **450** | **1.842** | **18,8%** (B 89, C 7) |

> **Cifras corregidas el 18 ago 2026 por la R43**, que volteo el puesto 2.371 de A a D.
> La primera escritura decia 12 A, 13,6% del tramo, 24,9% del dominio y 18,9% global.

### 77.2 LA PREDICCION DEL 2.300, MEDIDA POR TERCERA VEZ

| corte | pares leidos de `health_safety` | **tasa** |
|---|---:|---:|
| 2.300 | 81 de 192 | **37,0%** |
| 2.376 | 157 de 192 | **25,5%** |
| **2.388** | **169 de 192** | **24,3%** |

> **Tres cortes, tres bajadas, ninguna sorpresa.** Lo que se escribio en la seccion 72.2
> se cumple en direccion y en magnitud: **la cabecera de un dominio no predice su cierre**,
> y con 23 pares por leer **la cifra final seguira por debajo de 24,3%**.

### 77.3 LA VARA POR TRAMO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **10** |
| **REPITE** | **12** |
| no se invoco | **66** |

**22 de 88.** En la cabecera del dominio fue casi siempre; aqui, una vez de cada cuatro.
**La cola no pide vara porque no trae gemelos: trae objetos distintos que comparten
vocabulario.**

**Cero PENDIENTE DE DOCTRINA en 88 pares. En los 271 leidos desde el 2.118, cero.**

### 77.4 FIGURAS

| figura | puesto | que es |
|---|---|---|
| **LOS DOS EXTREMOS DEL MISMO SISTEMA** | 2.388 | `analisis_del_extremo_organizacional` trabaja el **extremo romo** y `perspectiva_dentro_del_tunel` el **afilado**; uno empieza donde el otro termina. La pareja canonica de Dekker, **sin arista** |
| **LA BRECHA CONTRA SU CAUSA** | 2.380 | uno **describe** la brecha entre trabajo prescrito y real; el otro **la explica** por la acumulacion de reglas en el manual, y es el unico que la **redisena** |
| **LA VENTANA QUE SE ABRE** | 2.386 | el queso suizo es un mapa permanente; `ventana_oportunidad_accidente` es el instante de la alineacion **y la unica accion del par: romperla** |

**Crecidas: ARISTA QUE FALTA en 40 de 88 pares** (45%); **SOLAPE DECLARADO en 20**; el
**racimo de las defensas llega a SIETE** miembros.

### 77.5 CONDICIONES VIVAS

1. **`errores_como_consecuencia` queda en NUEVE A** tras el volteo del 2.371, y la mas
   limpia de las nueve es el **2.387**: el superviviente nombra con sus cuatro casillas
   (presupuesto, capacitacion, dotacion, diseno) **la busqueda organizacional que en los
   puestos 2.345 y 2.382 lo habia salvado.**
2. **Y sigue sin ser mecanica: TRES D lo prueban.** En el **2.345**, el **2.371** y el
   **2.382**, contra nodos que trabajan **la etiqueta**, **la politica** o **la escena** y
   no **la busqueda**, este mismo nodo **si aporta**. **Nueve A y tres D, decididas cada
   una por lo que el otro traia.**
3. **`health_safety` abierto**, 169 de 192, **24,3% y bajando**.
4. **CUATRO A del archivo han caido, y las cuatro estaban marcadas** (2.195, 2.215,
   2.338 y 2.371). Las tres primeras por **la vara al reves**, y el barrido de la seccion
   76 cerro esa busqueda: **no hay una quinta de ese tipo.** La cuarta es de otra especie:
   **una postura mapeada sobre una busqueda** (seccion 78.1).

### 77.6 LAS 11 A DEL TRAMO, con las discutibles marcadas

> **Eran 12. El 2.371 salio el 18 ago 2026**, volteado por la R43, y **era uno de los
> tres marcados como discutibles.** Queda tachado abajo, no borrado.

| puesto | muere | sobrevive |
|---|---|---|
| 2.303 | `errores_como_consecuencia` | `enfoque_situacional_vs_personal` |
| 2.309 | `vieja_vision_vs_nueva_vision_seguridad` | `cultura_de_seguridad_interpretivista_funcionalista` |
| 2.310 | `human_error_como_sintoma` | `new_view_human_error` |
| 2.311 | `errores_como_consecuencia` | `error_humano_vs_falla_mecanica` |
| 2.328 | `reglas_parada_investigacion_accidentes` | `limite_busqueda_causas_pendulo` |
| **2.335** | `caso_descarrilamiento_nakina` | `condiciones_latentes_largo_plazo` **(superviviente corregido el 18 ago 2026)** |
| 2.347 | `errores_como_consecuencia` | `seduccion_modelo_persona` |
| 2.352 | `vieja_vision_vs_nueva_vision_seguridad` | `new_view_vs_old_view` |
| 2.362 | `errores_como_consecuencia` | `new_view_human_error` |
| **2.368** | **fusion mutua** | ninguno domina |
| ~~2.371~~ | ~~`errores_como_consecuencia`~~ | **VOLTEADA A D** el 18 ago 2026 |
| 2.387 | `errores_como_consecuencia` | `fallas_activas_condiciones_latentes` |

**LAS TRES MAS DISCUTIBLES, y la R43 empieza aqui:**

1. **2.335: RESUELTO, y la clase se sostuvo.** Se marco aqui que *la fusion tiene que
   conservar el titulo generico o la regla queda colgada de un descarrilamiento
   concreto*. **La R43 lo confirmo y el superviviente se corrigio**: manda
   `condiciones_latentes_largo_plazo`, el analisis geotecnico se repone en ella y Nakina
   viaja como ejemplo nombrado. **De ahi sale la figura EL CASO NO ES LA CASA**
   (seccion 78.3).
2. **2.368.** **Fusion mutua sin superviviente.** Cada uno anade dos lineas y ninguno
   trae procedimiento. **Se pierde, si nadie lo mira: el nivel organizacional explicito,
   el entrenamiento contra el sesgo de atribucion, y usar el hallazgo para cambiar el
   sistema y no para senalar.**
3. **2.310, y el 2.371 ya no la acompana.** En el 2.310 muere el nodo que trae **la
   unica accion correctiva directa del racimo**, redisenar la herramienta en vez de
   entrenar a la persona, y **la perdida ya se anoto cuatro veces en el archivo**. El
   2.371 se marco por la misma inquietud y **la R43 le dio la razon: no era una perdida a
   vigilar, era un veredicto mal puesto**, y las mejoras informativas se quedan donde
   estaban porque el par ni siquiera repetia.

### 77.7 LO QUE FALTA, y donde se retoma

**Faltan 229 pares, del 2.389 al 2.617.**

| tramo | dominio | pares | estado |
|---|---|---:|---|
| 2.389 a 2.411 | `health_safety` | **23** | pendiente; **cierra el dominio y fija su cifra final** |
| 2.412 a 2.617 | `quality` | **206** | pendiente; **abre el dominio** |

**Checkpoints pendientes: 2.400, 2.500 y 2.600.** **Pendiente tambien el resumen de
racimos de ids de `health_safety` para el plan**, que solo se puede escribir con el
dominio cerrado.

**LA PREDICCION SOBRE `quality` sigue en pie y sin tocar**, escrita en la seccion 75.8
antes de leer un solo par: **323 candidatos del barrido paso contra nodo, 296 sin arista**,
mas que `core` teniendo `core` diez veces mas pares. **Si acierta, `quality` entrega madre
e hijo y no gemelos.** La comprobacion pedida (tasa, proporcion de vara, y cuantos pares
confirman candidatos que el barrido ya tenia) **se hace al leerlo, y no antes.**

**El archivo esta en 2.388 sin huecos ni duplicados.** Se retoma en el **2.389**.
**Cero nodos tocados. Modo de cierre respetado entero.**


---

## 78. LA R43, LA CONJUNTA DEL 2.371 Y LA FIGURA EL CASO NO ES LA CASA

**18 ago 2026. Corte de esta seccion: puesto 2.388.**

### 78.1 LA CONJUNTA DEL 2.371, y el 2.335 no cae con ella

**EL CASO DEL AUDITOR:** `principios_gestion_error` **trae OTRO MOMENTO con procedimiento
propio**, la **gestion** del error y no su **investigacion**.

**VERIFICADO CONTRA EL GRAFO, y los entregables lo cierran en una linea:**

| nodo | entregable verificado | que momento es |
|---|---|---|
| `errores_como_consecuencia` | **Protocolo de investigacion de incidentes** que exija identificar causas raiz mas alla del error senalado | **el dia del incidente** |
| `principios_gestion_error` | **Documento de politica organizacional de gestion de errores** integrado a la cultura de seguridad | **la politica que existe antes y despues** |

**Un protocolo de caso y una politica permanente no son el mismo producto.**

**EL CABLEADO CONFIRMA SIN DECIDIR (P.8): no comparten ni un vecino.**
`errores_como_consecuencia` viene de `gestion_de_errores` y va a `ciclo_de_culpa`,
`enfoque_situacional_vs_personal` y `ciclo_de_culpa_2`. `principios_gestion_error` viene
de `tripod_beta_analisis_incidentes` y `vpc_condiciones_productoras_violacion` y va a
`regulador_fallas_sistemicas` y `normalizacion_de_la_desviacion`. **Cero solape.**

**EL 2.371 CAE: A pasa a D.**

> **LA LECCION, y es del mismo linaje que la del 9.6.2: UNA POSTURA NO EJECUTA UNA
> BUSQUEDA.** *Aceptar que el error es inevitable y enfocar la gestion en las condiciones*
> es una **posicion**; *ir a buscar que decidio la empresa antes del incidente* es un
> **paso de trabajo**. La lectura vieja los mapeo uno sobre otro **porque comparten el
> sentimiento**, y eso mato al que trabaja.

**EL IMAN QUEDA EN NUEVE.** `errores_como_consecuencia` baja de diez A a **nueve**, y sus
**tres D** (2.345, 2.371, 2.382) son las tres por el mismo motivo: **contra nodos que
trabajan la escena, la etiqueta o la politica, y no la busqueda, este nodo si aporta.**

### 78.2 EL SUPERVIVIENTE DEL 2.335, verificado con P.8

**La clase se sostiene: los tres pasos de uno y de otro van uno a uno.** Lo que cambia es
**quien se queda de pie.**

**P.8 dice que el cableado desempata pero NO decide, y que EL ALCANCE DEL ROL ES
CONTENIDO.** Su ejemplar propio lo formula asi: *una cabeza que vale para las ocho fases
no puede llamarse como una sola*. **Aqui: una casa que vale para toda infraestructura
critica no puede llamarse como un descarrilamiento concreto.**

**Y los entregables lo prueban sin necesidad de interpretar nada:**

| nodo | entregable verificado |
|---|---|
| `condiciones_latentes_largo_plazo` | **Informe de auditoria historica de infraestructura critica** identificando condiciones latentes de origen antiguo . **generico** |
| `caso_descarrilamiento_nakina` | Informe de **caso de estudio** que manda buscar **posibles FALLAS DE 1916 equivalentes** . **lleva la fecha de un terraplen dentro de su propio producto** |

**EL CABLEADO APUNTA AL OTRO LADO Y NO ALCANZA, y hay que decirlo:** Nakina tiene **tres
vecinos** y la doctrina **uno**. **P.8 resuelve el choque: una arista de margen no vence
al alcance del rol.** Y ese margen **no es un argumento a favor de Nakina: es el sintoma
del problema**, un estudio de caso cableado como si fuera doctrina.

> **SOBREVIVE `condiciones_latentes_largo_plazo`.** El requisito propio de Nakina, **el
> analisis geotecnico o de ingenieria profundo frente a la inspeccion visual externa**,
> **se repone en la doctrina**; y **el caso viaja dentro de ella como EJEMPLO NOMBRADO**,
> con su falla latente de setenta y seis anos, **que es lo que hace creible la regla**.

### 78.3 FIGURA NUEVA: EL CASO NO ES LA CASA

> **LA DOCTRINA SOBREVIVE; EL CASO VIAJA COMO EJEMPLO NOMBRADO, NUNCA AL REVES.**
>
> **Como se reconoce, sin discutir de gustos:** el entregable del caso **lleva dentro un
> dato del caso** (una fecha, un lugar, una empresa). El de la doctrina **vale sin
> cambiar una palabra para cualquier organizacion.**
>
> **Por que importa y no es cosmetica:** un catalogo cuya regla se llama *Descarrilamiento
> de Nakina* **obliga al lector a saber que fue Nakina antes de poder usar la regla**. El
> ejemplo se lee **despues** de la regla, no en lugar de ella.
>
> **Y el margen de aristas no la voltea** (P.8): si un caso esta mejor cableado que su
> doctrina, **eso se corrige moviendo las aristas, no coronando al caso.**

**EJEMPLAR: puesto 2.335**, `caso_descarrilamiento_nakina` contra
`condiciones_latentes_largo_plazo`.

### 78.4 EL BARRIDO DE CASOS, sin adjudicar

Levantado por script sobre los ids que empiezan por `caso_`, `estudio_`, `case_` o
`ejemplo_`.

| | |
|---|---:|
| nodos de caso o estudio **en el grafo** | **10** |
| pares del archivo leidos que tocan uno | **2** (2.279 y 2.335) |
| **pares con un caso como SUPERVIVIENTE declarado** | **1** (el 2.335, ya corregido) |
| nodos de caso **todavia sin cribar** | **8** |

**Los diez:** `case_study_sistema_servicio_completo`, `caso_definicion_arruga`,
`caso_descarrilamiento_nakina`, `caso_estudio_benchmarking_terminal`,
`caso_grietas_pequenas_mantenimiento_aeronaves`, `caso_taobao_evolucion_modelo`,
`estudio_desempeno_run_charts_servicios`, `estudio_lealtad_cliente`,
`estudio_mercado_calidad`, `estudio_mezclas_multiples_fuentes`.

> **SIN ADJUDICAR, y con un aviso de calendario: varios de los ocho sin cribar tienen
> pinta de `quality`**, el dominio que abre ahora. **La figura llega justo a tiempo**, y
> conviene aplicarla al leerlos y no despues.

### 78.5 EL RECOMPUTO

| | antes | **despues** |
|---|---:|---:|
| A del archivo | 451 | **450** |
| D del archivo | 1.841 | **1.842** |
| **tasa global** (corte 2.388) | 18,9% | **18,8%** |
| A de `health_safety` | 42 | **41** |
| **tasa de `health_safety`** (169 de 192) | 24,9% | **24,3%** |
| A del tramo 2.301 a 2.388 | 12 | **11** |
| **tasa del tramo** | 13,6% | **12,5%** |

**El 2.335 no mueve ninguna cifra: cambia el superviviente, no la clase.**


---

## 79. CHECKPOINT 2.400 y reporte del tramo 2.301 a 2.400

**Corte: puesto 2.400.** El tramo cierra en **100 pares redondos**. `health_safety` sigue
abierto: **181 de 192**.

### 79.1 CIFRAS

| | pares | A | D | **tasa** |
|---|---:|---:|---:|---:|
| **tramo 2.301 a 2.400** | **100** | **15** | **85** | **15,0%** |
| `health_safety` acumulado | **181 de 192** | **45** | 136 | **24,9%** |
| archivo global (corte 2.400) | 2.400 | **454** | **1.850** | **18,9%** (B 89, C 7) |

**TASA POR DOMINIO (banco 9.27):**

| dominio | pares | A | **tasa** | estado |
|---|---:|---:|---:|---|
| `compras` | 155 | 1 | **0,6%** | cerrado |
| `core` | 1.445 | 344 | **23,8%** | cerrado |
| `entrega` | 171 | 2 | **1,2%** | cerrado |
| `environmental` | 170 | 29 | **17,1%** | cerrado |
| `exportacion` | 130 | 15 | **11,5%** | cerrado |
| `franquicias` | 148 | 18 | **12,2%** | cerrado |
| **`health_safety`** | **181 de 192** | **45** | **24,9%** | **abierto, 94% leido** |

### 79.2 CORRECCION DECLARADA: mi prediccion sobre la cola se rompio en el cuarto corte

La seccion 77.2 escribio, con el dominio al 24,3%: **la cifra final seguira por debajo de
24,3%**. **No se cumplio.**

| corte | pares leidos | **tasa del dominio** | el tramo nuevo solo |
|---|---:|---:|---|
| 2.300 | 81 | **37,0%** | . |
| 2.376 | 157 | **25,5%** | 13,2% |
| 2.388 | 169 | **24,3%** | 12,5% |
| **2.400** | **181** | **24,9%** | **33,3%** (4 A en 12) |

> **La direccion acerto tres cortes seguidos y fallo al cuarto.** Los ultimos doce pares
> devolvieron **33,3%**, mas del doble que los ochenta y ocho anteriores, y **subieron el
> acumulado del dominio en seis decimas.**
>
> **POR QUE, y es lo que hay que aprender de la falla:** la cola **no baja de forma
> monotona**. Baja **en promedio**, porque va perdiendo gemelos, pero **quedan bolsas**:
> los puestos 2.389 a 2.400 juntaron cuatro pares de doctrina repetida seguidos
> (`ingenieria_cultura_aprendizaje`, `seduccion_modelo_persona`,
> `human_error_como_sintoma`, `vieja_vision_vs_nueva_vision_seguridad`).
>
> **LA REGLA SE CORRIGE, no se abandona:** *la tasa de una cola tiende a la baja y no
> desciende paso a paso*. **Una prediccion sobre la tendencia es legitima; una prediccion
> sobre cada corte siguiente no lo era, y esta lo era.**

### 79.3 LA VARA POR TRAMO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **12** |
| **REPITE** | **15** |
| no se invoco | **73** |

**27 de 100**, contra 81 de 183 en la cabecera. **Cero PENDIENTE DE DOCTRINA en 100
pares. En los 283 leidos desde el 2.118, cero.**

### 79.4 FIGURAS Y NOMINAS

**Nueva del tramo: EL CASO NO ES LA CASA** (informe §78.3), nacida del 2.335.

**Crecidas:** **ARISTA QUE FALTA en 44 de 100 pares**; el racimo de las defensas en
**siete**; y **una TENSION DECLARADA INTER FUENTE nueva en el 2.393**, que va a la mesa
del dominio: `limitaciones_ltif_indicador` manda seguir los casi accidentes **como
precursores** del grave, y `no_usar_triangulo_heinrich` sostiene que **el menor y el
grave pueden no compartir causa**. **Dos doctrinas legitimas: frontera candidata, no
defecto de instruccion**, y la contradiccion no decide la clase (banco 1632).

**Un hijo leido en la direccion correcta, y conviene tenerlo escrito junto al 9.6.2:** el
**2.392**, donde `reacciones_al_fallo` nombra **las cuatro caracteristicas** de una
reaccion mala y `foco_proximal_reacciones_falla` **desarrolla la cuarta** trayendo la
busqueda de senales previas. **Madre e hijo, D, y el hijo vivo.**

### 79.5 CONDICIONES VIVAS

1. **`errores_como_consecuencia`: NUEVE A y TRES D.** Las tres D contra nodos que trabajan
   **la etiqueta**, **la politica** o **la escena** y no **la busqueda**.
2. **`vieja_vision_vs_nueva_vision_seguridad`: CUATRO A** (2.253, 2.309, 2.352, 2.400),
   contra cuatro supervivientes distintos. **Un plan de migracion sin doctrina.**
3. **`human_error_como_sintoma`: CUATRO A**, y con el **la perdida que viaja se anota por
   quinta vez**: redisenar la herramienta en vez de entrenar a la persona **sigue siendo
   la unica accion correctiva directa del racimo** y sigue viajando como linea absorbida.
4. **Cuatro A del archivo han caido** (2.195, 2.215, 2.338, 2.371) **y las cuatro estaban
   marcadas.** Ninguna discrepancia fuera de la lista todavia.

### 79.6 LAS 15 A DEL TRAMO, con las discutibles marcadas

`2.303`, `2.309`, `2.310`, `2.311`, `2.328`, **`2.335`**, `2.347`, `2.352`, `2.362`,
**`2.368`**, `2.387`, `2.389`, **`2.396`**, `2.397`, `2.400`.

**LAS TRES MAS DISCUTIBLES, y la R44 empieza aqui:**

1. **2.396.** Muere `seduccion_modelo_persona`, que **sobrevivio cuatro veces antes**
   (2.228, 2.331, 2.347, 2.385) **por tener el criterio persona contra sistema**. Aqui el
   otro lo tiene y la ventaja desaparece. **Lo que se pierde es la explicacion de POR QUE
   el modelo de persona seduce**, que ningun superviviente conserva.
2. **2.335.** Resuelto por la R43 en cuanto al superviviente, **pero la clase sigue siendo
   la mas fina del tramo**: los dos nodos dicen lo mismo en tres pasos y lo que los separa
   es un requisito de metodo.
3. **2.389.** Muere `ingenieria_cultura_aprendizaje`, cuyo unico aporte propio es **un
   enfasis**, comprometer tiempo y recursos a implementar y no solo a hablar. **Es linea
   por la vara y es lo que mas se incumple en la practica**: si la fusion la deja caer, el
   ciclo queda escrito y sin dueno.

### 79.7 LO QUE FALTA

**Faltan 217 pares, del 2.401 al 2.617.**

| tramo | dominio | pares | estado |
|---|---|---:|---|
| 2.401 a 2.411 | `health_safety` | **11** | pendiente; **cierra el dominio** |
| 2.412 a 2.617 | `quality` | **206** | pendiente; **abre el dominio** |

**Pendientes con ellos:** los checkpoints **2.500 y 2.600**; **el resumen de los trece
racimos de ids de `health_safety` para el plan**, que solo se puede escribir con el
dominio cerrado; y **la comprobacion de la prediccion sobre `quality`** de la seccion
75.8 (tasa, proporcion de vara y solape con los 296 candidatos sin arista del barrido
paso contra nodo).

**El archivo esta en 2.400 sin huecos ni duplicados. Cero nodos tocados.**


---

## 80. CIERRE DE `health_safety`, y sus trece racimos de ids para el plan

**Corte: puesto 2.411. El dominio queda CERRADO.**

### 80.1 LA CIFRA FINAL

**Del puesto 2.220 al 2.411, 192 pares.**

| | |
|---|---:|
| pares | **192** |
| A | **45** |
| B | **0** |
| C | **0** |
| D | **147** |
| **tasa de A** | **23,4%** |

**Archivo global al corte 2.411: A 454, B 89, C 7, D 1.861 sobre 2.411. Tasa 18,8%.**

| dominio | pares | A | **tasa** |
|---|---:|---:|---:|
| `compras` | 155 | 1 | **0,6%** |
| `entrega` | 171 | 2 | **1,2%** |
| `exportacion` | 130 | 15 | **11,5%** |
| `franquicias` | 148 | 18 | **12,2%** |
| `environmental` | 170 | 29 | **17,1%** |
| **`health_safety`** | **192** | **45** | **23,4%** |
| `core` | 1.445 | 344 | **23,8%** |

> **`health_safety` cierra en 23,4%, a cuatro decimas de `core`, y es el segundo dominio
> mas repetido del archivo.**

### 80.2 LA PREDICCION, resuelta: acerto al cierre y su defensa era mala

| corte | pares | tasa | tramo nuevo |
|---|---:|---:|---|
| 2.300 | 81 | **37,0%** | . |
| 2.376 | 157 | **25,5%** | 13,2% |
| 2.388 | 169 | **24,3%** | 12,5% |
| 2.400 | 181 | **24,9%** | **33,3%** |
| **2.411, cierre** | **192** | **23,4%** | **0,0%** (0 A en 11) |

> **Los ultimos once pares dieron CERO A, y el dominio cerro en 23,4%, por debajo del
> 24,3% que la seccion 77.2 habia predicho.**
>
> **La prediccion acerto al cierre. La defensa que le puse era mala igual**, y la
> precision del 9.19 se queda como esta: **la tasa de una cola tiende a la baja y no
> desciende paso a paso**. Que el resultado final coincida **no rehabilita el
> razonamiento**: entre el 2.388 y el 2.400 la cifra subio, y quien hubiera parado ahi
> habria publicado una cifra peor que la de partida.

### 80.3 LA VARA EN EL DOMINIO ENTERO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **22** |
| **REPITE** | **45** |
| no se invoco | **125** |

**67 de 192.** **Cero PENDIENTE DE DOCTRINA en los 192.** **74 ARISTA QUE FALTA** (39% de
los pares del dominio) y **42 SOLAPE DECLARADO**.

### 80.4 LOS TRECE RACIMOS DE IDS, medidos para el plan

**Medidos por `scripts/racimos_health_safety.py`, de solo lectura.** Cada forma va con su
cobertura al lado (banco 9.26).

| racimo | miembros | pares posibles | leidos | A | D | **cobertura** | aristas |
|---|---:|---:|---:|---:|---:|---:|---:|
| **LA VIEJA Y LA NUEVA VISION** | 6 | 15 | 9 | 4 | 5 | **60%** | **0** |
| **EL SESGO RETROSPECTIVO** | 7 | 21 | 11 | 3 | 8 | **52%** | 2 |
| **LAS DEFENSAS** | 7 | 21 | 5 | 2 | 3 | **24%** | 4 |
| **LAS CONDICIONES LATENTES** | 5 | 10 | 4 | 1 | 3 | **40%** | 3 |
| **EL ERROR COMO SINTOMA** | 9 | 36 | 14 | **11** | 3 | **39%** | 2 |
| **LA DERIVA** | 4 | 6 | **6** | 3 | 3 | **100%** | **0** |
| **LA CULTURA JUSTA** | 4 | 6 | 3 | 1 | 2 | **50%** | 2 |
| **EL ERROR DE MANTENIMIENTO** | 7 | 21 | 4 | 1 | 3 | **19%** | 6 |
| **LA GESTION DEL ERROR** | 3 | 3 | **3** | 0 | 3 | **100%** | **0** |
| **LA MEDICION QUE CORROMPE** | 7 | 21 | 4 | 0 | 4 | **19%** | **0** |
| **LA CULTURA COORDINADORA** | 3 | 3 | 2 | 0 | 2 | **67%** | **0** |
| **EL APRENDIZAJE ORGANIZACIONAL** | 5 | 10 | 3 | 1 | 2 | **30%** | **0** |
| **LA REACCION AL FALLO** | 7 | 21 | 6 | 2 | 4 | **29%** | 1 |
| **TOTAL** | **74** | **194** | **74** | **29** | **45** | **38%** | **20** |

**COMO SE LEE ESTA TABLA, y son cuatro cosas:**

1. **DOS RACIMOS ESTAN CERRADOS Y LOS DOS SON PEQUENOS:** **la deriva** (4 miembros, 6 de
   6 leidos, **3 A y 3 D**) y **la gestion del error** (3 miembros, 3 de 3, **cero A**).
   **El primero se funde en parte y el segundo no se toca**: son los dos unicos del
   dominio donde **la lectura ya no puede cambiar nada.**
2. **EL ERROR COMO SINTOMA es el racimo grande y el mas caro:** **9 miembros, 11 A sobre
   14 pares leidos**, y solo el 39% de cobertura. **Es el que contiene al iman**,
   `errores_como_consecuencia` con nueve A y tres D. **Con 22 pares sin leer, su forma
   final no esta fijada.**
3. **CUATRO RACIMOS TIENEN CERO ARISTAS ENTRE MIEMBROS** (la vieja y la nueva vision, la
   gestion del error, la medicion que corrompe, la cultura coordinadora) **mas el
   aprendizaje organizacional**: **cinco de trece sin un solo cable interno.** Es la
   cosecha de enlace mas barata del dominio.
4. **COBERTURA BAJA DONDE HAY MAS ARISTAS.** El error de mantenimiento tiene **19% leido y
   6 aristas**; la medicion que corrompe tiene **19% y 0**. **La cola no ordeno estos
   racimos por igual**, y eso decide cuanto trabajo queda: donde hay aristas, el racimo ya
   esta parcialmente resuelto por el grafo.

**LOS RACIMOS QUE CAEN EN FIGURAS CONOCIDAS:**

| figura | racimos donde aparece |
|---|---|
| **gemelos de extraccion** (ids `_2`, `_3`, titulos espejo, una preposicion) | la deriva, las defensas, la reaccion al fallo, la cultura justa, la vieja y la nueva vision, el sesgo retrospectivo |
| **EL CASO NO ES LA CASA** (§78.3) | **las condiciones latentes**, con `caso_descarrilamiento_nakina` |
| **el iman**: un nodo que repite contra muchos | **el error como sintoma** (9 A, 3 D) y **la vieja y la nueva vision** (`vieja_vision_vs_nueva_vision_seguridad`, 4 A) |
| **frontera candidata INTER fuente** | **la medicion que corrompe**, puesto 2.393, LTIF contra Heinrich (PENDIENTES) |
| **A por fusion mutua** | **el error como sintoma**, puesto 2.368 |
| **advertencia de aduana, el 3% lexico** | **el aprendizaje organizacional**, puesto 2.389 |

> **LA CUENTA QUE EL PLAN NECESITA: 74 miembros nominales en trece racimos, con 68 nodos
> distintos** (`enfoque_situacional_vs_personal` aparece en dos). **194 pares posibles, 74
> leidos, 120 sin leer.** **La cola no volvera a ofrecerlos**: el dominio esta cerrado, y
> los 120 pares restantes **solo se leen si el plan los encarga como lectura dirigida.**


---

## 81. `quality` ABIERTO, y la prediccion de la 75.8 medida (a medias, y por que)

**Corte: puesto 2.416. Van 5 pares de `quality` de los 844 que tiene en la cola.**

### 81.1 CIFRAS, con su banda

| | |
|---|---:|
| pares de `quality` leidos | **5** |
| A | **1** (2.414) |
| D | **4** |
| tasa | **20,0%** |

> **CINCO PARES NO SON UNA TASA.** Se escribe porque el encargo la pide, **y no se puede
> usar para nada**: con 5 lecturas, un solo veredicto distinto la mueve veinte puntos.
> **El dominio tiene 844 pares en la cola y aqui va el 0,6%.**

**Archivo global al corte 2.416: A 455, B 89, C 7, D 1.865 sobre 2.416. Tasa 18,8%.**

### 81.2 LA PREDICCION DE LA 75.8, y lo que la medicion le hace

**Lo que se escribio antes de leer un solo par:** el barrido paso contra nodo le da a
`quality` **323 candidatos, 296 sin arista**, mas que a `core` teniendo `core` diez veces
mas pares; **si acierta, `quality` entrega madre e hijo y no gemelos.**

**LO QUE LA MEDICION DICE, y hay que partirlo en dos porque las dos mitades no coinciden:**

**PRIMERA MITAD: la cabecera de `quality` entrega GEMELOS, no madre e hijo.** Los cinco
primeros pares tienen similitud de titulo **97,6, 97,3, 94,7, 93,0 y 92,3**, y sus ids se
diferencian en **una preposicion o un sufijo**:

| puesto | los dos ids | que los separa |
|---:|---|---|
| 2.412 | `capacidad_de_proceso` / `capacidad_del_proceso` | **una preposicion** |
| 2.413 | `control_estadistico_de_procesos` / `control_estadistico_del_proceso` | **una preposicion** |
| 2.414 | `programa_de_mejora_de_calidad` / `programa_mejora_calidad_14_pasos` | dos formas del mismo catorce pasos |
| 2.415 | `planificacion_de_la_inspeccion` / `planificacion_inspeccion` | **un articulo** |
| 2.416 | `eliminacion_causas_error` / `eliminacion_causas_error_2` | **un sufijo** |

**Y eso NO contradice el barrido: confirma el 9.19.** La cola esta ordenada por similitud,
y **la similitud alta caza duplicados**. Los madre e hijo del barrido **viven mas abajo**.
La media de similitud de titulo lo dice sola: **70,0 en los veinte primeros pares del
dominio contra 46,1 en los veinte ultimos.**

**SEGUNDA MITAD, y esta si corrige la prediccion: el solape medido es del 5,8%.**

| | |
|---|---:|
| candidatos paso contra nodo de `quality`, **parejas unicas sin arista** | **291** |
| de esos, **presentes en la cola** de `quality` | **49** |
| **fuera de la cola** | **242 (83%)** |
| **pares de la cola de `quality` que son candidato del barrido** | **49 de 844 = 5,8%** |

> **LA PREDICCION ERA OPTIMISTA SOBRE EL CANAL, NO SOBRE EL HALLAZGO.** El barrido si
> encontro 291 madre e hijo en `quality`. **Lo que no vio es que 242 de ellos NO ESTAN EN
> LA COLA**, porque una madre y su hijo **no se parecen**: la madre enuncia y el hijo
> despliega, y la similitud que los emparejaria esta por debajo del corte.
>
> **CONSECUENCIA PARA EL PLAN, y es la parte util: leer `quality` entero NO cosecha los
> 291.** Cosecha, como mucho, **49**. **Los otros 242 son trabajo que la cola no va a
> ofrecer nunca**, exactamente igual que los 120 pares sin leer de los racimos de
> `health_safety` (§80.4). **Se leen si se encargan, o no se leen.**

**Y una nota de honestidad sobre la propia prediccion:** decia *si el barrido acerto,
`quality` entrega madre e hijo y no gemelos*. **La cabecera entrega gemelos.** La
prediccion no era falsa, **estaba mal formulada**: mezclaba lo que el barrido ve
(el catalogo entero) con lo que la cola ofrece (los pares parecidos). **Son dos universos
distintos y ahora estan medidos por separado.**

### 81.3 LO QUE FALTA

**Faltan 201 pares del encargo, del 2.417 al 2.617**, todos de `quality`. **Y el dominio
completo son 844**, asi que ni siquiera este tramo lo cierra: `quality` llega hasta el
puesto 3.255.

| pendiente | |
|---|---|
| cribado | **2.417 a 2.617**, 201 pares |
| checkpoints | **2.500 y 2.600** |
| comprobacion | la tasa de `quality` con banda utilizable, la proporcion de vara, y **cuantos de los 49 candidatos del barrido caen dentro del tramo leido** |



### 81.4 LA SEPARACION CANAL CONTRA CATALOGO, y con esto la 75.8 queda cerrada

> **LA PREDICCION MEZCLABA LO QUE EL BARRIDO VE CON LO QUE LA COLA OFRECE. AHORA ESTAN
> MEDIDOS POR SEPARADO.**

| | que universo mide | cifra de `quality` |
|---|---|---:|
| **el barrido paso contra nodo** | **el catalogo entero**: toda madre cuyo paso tiene hijo con casa propia | **291 parejas sin arista** |
| **la cola del cribado** | **los pares que se parecen**: similitud de titulo y semantica por encima del corte | **844 pares** |
| **la interseccion** | lo que el cribado puede cosechar leyendo | **49, el 5,8%** |

**LA CONSECUENCIA OPERATIVA, escrita, y SIN RUTA NUEVA:**

1. **Leer `quality` cosecha GEMELOS.** Es lo que la cabecera ya entrego y lo que el 9.19
   predice: similitud alta, duplicados.
2. **Sus JERARQUIAS no llegan por la cola: llegan por las rutas que el plan ya tiene.**
   `OP-E-06` escribe **los que tienen direccion**; `OP-E-07` son **lecturas de frase, no de
   par**, con la clase ya decidida; y `OP-E-03` computa **la diferencia contra la cola el
   dia que cada dominio cierre**.
3. **Los 242 de `quality` que quedan fuera de la cola no son un hueco del cribado: son la
   carga de esas tres operaciones.** El cribado **no los va a ver**, y no tiene por que.

**Con esto la prediccion de la seccion 75.8 queda cerrada:** no era falsa **y no era
util**, porque hablaba de un canal con las cifras de otro.

**El archivo esta en 2.416 sin huecos ni duplicados. Cero nodos tocados.**


---

## 82. REPORTE DEL TRAMO 2.412 A 2.428: `quality` abre en 41,2%

**Corte: puesto 2.428.** Van **17 pares de `quality`** de los 844 que tiene en la cola.

### 82.1 CIFRAS

| | pares | A | D | **tasa** |
|---|---:|---:|---:|---:|
| **`quality`** | **17** | **7** | **10** | **41,2%** |
| archivo global (corte 2.428) | 2.428 | **461** | **1.871** | **19,0%** (B 89, C 7) |

> **41,2% es la apertura mas alta del archivo**, por encima del 37,0% con que abrio
> `health_safety`. **Y con 17 pares sigue sin ser una tasa utilizable**: la banda es
> enorme y un solo veredicto la mueve seis puntos. **Lo que si es solido es la forma**, y
> esa se ve con 17.

### 82.2 LA TRAMPA DEL IDENTIFICADOR, con su cuenta

**La cabecera de `quality` esta hecha de nodos que se llaman casi igual.**

| medicion | cifra |
|---|---:|
| pares leidos cuyos dos ids son **de la misma familia** (sufijo numerico, preposicion o articulo de diferencia) | **5 de 17** |
| **familias por sufijo numerico** en la cola de `quality` | **24 familias, 57 nodos** |
| nodos distintos de `quality` que aparecen en la cola | **573** |

**Las familias mas cargadas, medidas:** `accion_correctiva` **(5)**,
`definiciones_operacionales` **(4)**, `programa_make_certain` **(3)**,
`consejo_de_calidad` **(3)**, `dia_cero_defectos` **(3)**,
`eliminacion_causas_error` **(3)**.

> **LA TRAMPA, y por eso se registra con la cuenta:** un id con sufijo **parece** un
> duplicado y **no siempre lo es**. En este tramo, de los cinco pares de misma familia,
> **tres repitieron** (2.417, 2.418, 2.426) **y dos no** (2.422, 2.428). El
> **sistema_responsabilidad_gerencial** contra su `_2` **es D**: uno acota la
> responsabilidad y el otro la mide.
>
> **El identificador ordena la sospecha; no la resuelve.** Es la misma leccion del 3%
> lexico por otra via: **la forma del nombre no decide.**

### 82.3 LA VARA POR TRAMO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **2** |
| **REPITE** | **7** |
| no se invoco | **8** |

**9 de 17, el 53%**, contra 27 de 100 en la cola de `health_safety`. **La cabecera pide
vara casi siempre**, que es exactamente lo que el 9.19 dice de la similitud alta.

**Cero PENDIENTE DE DOCTRINA. 9 ARISTA QUE FALTA en 17 pares (53%), 6 SOLAPE DECLARADO.**

### 82.4 FIGURAS

| figura | puesto | nota |
|---|---|---|
| **TERCERA CABEZA DUPLICADA DE SERIE** | 2.414 | los catorce pasos de Crosby, tras Coleman (326) y los medios (948). **Con tres ejemplares la figura tiene patron** (§8) |
| **A POR FUSION MUTUA** | **2.417** | **tercer caso del archivo** tras 2.127 y 2.368. `mantener_las_ganancias` contra `sostener_las_ganancias`, **ids que se diferencian en un verbo sinonimo**, linea en los dos sentidos |
| **EL TITULO PROMETE LO QUE LOS PASOS NO DAN** | 2.420 | `tipos_innovacion_i_ii` se llama *Dos Tipos de Innovacion, Tipo I y Tipo II* y **sus seis pasos son solo el ejercicio del Tipo II**. La ausencia **refuerza** el veredicto |
| **diferencia doctrinal INTER fuente** | 2.412 | Deming exige **control estadistico ANTES** de calcular capacidad; Juran calcula sobre historicos **sin nombrar esa condicion**. No es contradiccion frontal: es una precondicion que uno pone y el otro omite |

**Ningun nodo de CASO o ESTUDIO entro a par todavia.** El censo del 2.335 dejo **8 sin
cribar** y varios con pinta de este dominio (`caso_estudio_benchmarking_terminal`,
`estudio_mercado_calidad`, `estudio_desempeno_run_charts_servicios`,
`estudio_mezclas_multiples_fuentes`). **La figura EL CASO NO ES LA CASA queda armada y sin
usar; se cita el dia que aparezcan.**

### 82.5 LAS 7 A DEL TRAMO, con las discutibles marcadas

| puesto | muere | sobrevive |
|---|---|---|
| **2.414** | `programa_mejora_calidad_14_pasos` | `programa_de_mejora_de_calidad` |
| **2.417** | **fusion mutua** | ninguno domina |
| 2.418 | `accion_correctiva_6` | `accion_correctiva_5` |
| 2.420 | `tipos_innovacion_i_ii` | `innovacion_tipo_ii` |
| **2.421** | `relaciones_largo_plazo_con_proveedores` | `relacion_largo_plazo_proveedor_unico` |
| 2.424 | `compra_por_precio_mas_bajo_como_error` | `fin_precio_como_criterio_unico` |
| 2.426 | `accion_correctiva_6` | `accion_correctiva_crosby` |

**LAS TRES MAS DISCUTIBLES, y la R46 empieza aqui:**

1. **2.417.** **Fusion mutua sin superviviente**, y con **tres perdidas** que nadie hereda
   por defecto: **el mistake proofing** (una clase de control distinta, disenar el error
   fuera en vez de auditarlo), **el disparador de la rotacion de personal**, y **los
   responsables de supervision.** Si la fusion elige a ojo, se pierde la primera.
2. **2.421.** Muere el nodo que trae **la evidencia estadistica de calidad** como criterio
   de evaluacion y **el recuento de proveedores actuales** como primer paso. El
   superviviente evalua por *evidencia de mejora continua*, que es mas vago. **Es linea
   por la vara y es el arranque practico por el oficio.**
3. **2.414.** Ya releida y confirmada (R45), **queda marcada por su perdida**: *aunque sea
   de dos o tres personas* es lo unico del par que hace el programa ejecutable en un
   negocio pequeno, **que es el publico de la app**.

**Y `accion_correctiva_6` repitio DOS veces en cinco pares** (2.418 y 2.426), contra dos
supervivientes distintos. **Es la version generica de una familia de cinco**, y **la
familia entera no esta leida**: quedan pares con `accion_correctiva`,
`accion_correctiva_2` y `accion_correctiva_4` sin tocar.

### 82.6 LO QUE FALTA

**Faltan 189 pares del encargo, del 2.429 al 2.617**, todos de `quality`. **Checkpoints
2.500 y 2.600 pendientes.** El dominio completo son **844 pares** y llega al puesto
**3.255**: este tramo no lo cierra ni de lejos.

**El archivo esta en 2.428 sin huecos ni duplicados. Cero nodos tocados.**


---

## 83. REPORTE DEL TRAMO 2.429 A 2.438: `quality` sube a 44,4%

**Corte: puesto 2.438. Van 27 pares de `quality`** de sus 844.

### 83.1 CIFRAS

| | pares | A | D | **tasa** |
|---|---:|---:|---:|---:|
| **`quality`** | **27** | **12** | **15** | **44,4%** |
| archivo global (corte 2.438) | 2.438 | **466** | **1.876** | **19,1%** (B 89, C 7) |

**Subio del 41,2% al 44,4% con diez pares mas.** Sigue **sin banda utilizable**, y sigue
siendo **la apertura mas alta del archivo**.

### 83.2 LA VARA POR TRAMO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **3** |
| **REPITE** | **12** |
| no se invoco | **12** |

**15 de 27, el 56%.** **Cero PENDIENTE DE DOCTRINA. 14 ARISTA QUE FALTA (52%), 9 SOLAPE
DECLARADO.**

### 83.3 LO QUE ESTE TRAMO ANADE

**CUARTO CASO DE A POR FUSION MUTUA (2.436)**, y el archivo ya lleva cuatro: 2.127, 2.368,
2.417 y este. **`enfermedades_mortales_gestion` contra `las_siete_enfermedades_mortales`**
son los mismos cuatro pasos, y **cada lado aporta dos lineas y ninguno domina**: uno mide
el impacto **en los numeros** y nombra al responsable; el otro mide **en la cultura** y da
el criterio de prioridad, **empezar por la que genera mayor dano de fondo**.

> **Dos de las cuatro fusiones mutuas del archivo han salido en `quality`, y en diez
> pares.** Es la firma de un dominio escrito dos veces.

**LA CADENA DE ABSORCION DE `accion_correctiva`, la familia mas grande del dominio.**

| puesto | muere | sobrevive |
|---:|---|---|
| 2.418 | `accion_correctiva_6` | `accion_correctiva_5` |
| 2.426 | `accion_correctiva_6` | `accion_correctiva_crosby` |
| **2.431** | **`accion_correctiva_5`** | `accion_correctiva_sistematica` |

> **El superviviente del 2.418 muere en el 2.431.** La familia tiene **cinco miembros en
> la cola** y va colapsando hacia `accion_correctiva_sistematica` y
> `accion_correctiva_crosby`. **Quedan sin leer los pares con `accion_correctiva`,
> `accion_correctiva_2` y `accion_correctiva_4`.**

**EL MEJOR EJEMPLAR DE LA TRAMPA DEL IDENTIFICADOR (2.433).**
`auditoria_de_producto` contra `auditoria_de_producto_2`: **un sufijo de diferencia y
auditan cosas distintas.** El primero mide **el producto contra la necesidad del usuario**;
el segundo **reinspecciona productos ya clasificados para verificar si la decision del
inspector fue correcta**. **Uno mide el producto y el otro mide al que mide. D.**

**UNA PERDIDA QUE NO ES DE PASOS SINO DE NOMBRE (2.432).** Muere `funcion_perdida_taguchi`
y el superviviente no dice **Taguchi** en ningun lado. **Es el nombre por el que este
instrumento se busca en cualquier manual.** La fusion **tiene que reponerlo en el titulo o
en la primera linea**, o el catalogo pierde la entrada por la que el lector llega.

**Y UNA OBSERVACION DE PRODUCTO (2.434).** La linea de negocio pequeno que se perdio en el
2.414 (*aunque sea de dos o tres personas*) **vive en otro nodo**: `zero_defects_concepto`
dice *marca un dia concreto para lanzar el compromiso, **aunque sea contigo mismo o con
quien te ayude en el negocio***. **El registro de negocio pequeno no esta repartido por el
catalogo: esta concentrado en nodos concretos**, y conviene saber cuales antes de fundir.

**Ningun nodo de CASO o ESTUDIO ha entrado a par todavia.** La figura **EL CASO NO ES LA
CASA sigue armada y sin usar**.

### 83.4 LAS 12 A DE `quality`, con las discutibles marcadas

`2.414`, **`2.417`**, `2.418`, `2.420`, `2.421`, `2.424`, `2.426`, **`2.431`**,
**`2.432`**, `2.436`, `2.437`, `2.438`.

**LAS TRES MAS DISCUTIBLES, y la R47 empieza aqui:**

1. **2.432.** La clase es solida (la misma cuenta paso por paso), **pero el superviviente
   pierde el nombre canonico del instrumento.** Es el primer caso del archivo donde **lo
   que se pierde no es un paso ni una linea: es la palabra por la que se busca.**
2. **2.431.** Mata al superviviente de una A anterior (2.418). **La clase se sostiene por
   la cadencia de tres niveles del superviviente nuevo**, pero **es la tercera lectura de
   la misma familia en trece pares**, y la familia no esta leida entera: **el orden en que
   la cola las va emparejando esta decidiendo quien queda de pie.**
3. **2.417.** Fusion mutua ya releida (R46) y **con su tercera linea reclasificada a arista
   candidata**; queda marcada porque **las otras dos siguen sin heredero por defecto.**

### 83.5 LO QUE FALTA

**Faltan 179 pares del encargo, del 2.439 al 2.617**, todos de `quality`. **Checkpoints
2.500 y 2.600 pendientes.** El dominio completo son **844 pares** y llega al **3.255**.

**El archivo esta en 2.438 sin huecos ni duplicados. Cero nodos tocados.**


---

## 84. REPORTE DEL TRAMO 2.439 A 2.443

**Corte: puesto 2.443. Van 32 pares de `quality`** de sus 844.

### 84.1 CIFRAS

| | pares | A | D | **tasa** |
|---|---:|---:|---:|---:|
| **`quality`** | **32** | **13** | **19** | **40,6%** |
| archivo global (corte 2.443) | 2.443 | **467** | **1.880** | **19,1%** (B 89, C 7) |

**La tasa del dominio bajo del 44,4% al 40,6%** con cinco pares mas: cuatro D y una A.
**Sigue sin banda utilizable**, y **el movimiento de casi cuatro puntos con cinco lecturas
es justamente lo que hace que no lo sea.**

### 84.2 LA VARA POR TRAMO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **4** |
| **REPITE** | **13** |
| no se invoco | **15** |

**17 de 32, el 53%.** **Cero PENDIENTE DE DOCTRINA. 17 ARISTA QUE FALTA (53%), 11 SOLAPE
DECLARADO.**

### 84.3 LO QUE ANADE ESTE TRAMO

**SEGUNDO EJEMPLAR DE LA TRAMPA DEL IDENTIFICADOR EN CINCO PARES (2.439).**
`clasificacion_de_seriedad_de_defectos_2` **no es un duplicado**: el sufijo marca **la
variante para el proveedor**. Uno mira hacia adentro (categorias acordadas entre areas,
validacion con pilotos) y el otro **hacia afuera** (comunicar la clasificacion al
proveedor, vincularla a los planes de muestreo). **D.**

> **Con el 2.433 son dos ejemplares en cinco pares** donde un sufijo `_2` **marca un
> destinatario o un objeto distinto, no una repeticion.** La cuenta de la trampa sube:
> **de los pares de familia leidos en `quality`, tres repitieron y ahora cuatro no.**

**DOS PARES QUE SE ENTREGAN EL TRABAJO Y NO ESTAN CABLEADOS.**

| puesto | quien construye | quien lee o continua |
|---:|---|---|
| **2.442** | `histograma`, la receta en siete pasos | `histograma_calidad`, que **agrega los limites de especificacion al grafico** y evalua centrado, ancho y forma **para determinar capacidad** |
| **2.441** | `control_estadistico_proceso` | `innovacion_tras_control_estadistico`, **CON ARISTA ya puesta** |

> **Un histograma sin los limites dibujados encima no dice si el proceso sirve.** El 2.442
> es una **arista que falta con direccion**, y de las mas baratas del dominio.

**UNA PERDIDA QUE CONVIENE MIRAR (2.440).** Muere `moral_y_sistema_no_individuo` y se
lleva *dar seguimiento y **apoyo** a quienes caen fuera de las tolerancias del grupo*.
**Es la unica linea del par que dice que hacer con la persona que si queda fuera**, y sin
ella **la doctrina del sistema se lee como que nunca hay nada que hacer con nadie.**

### 84.4 LAS 13 A DE `quality`, con las discutibles marcadas

`2.414`, `2.417`, `2.418`, `2.420`, `2.421`, `2.424`, `2.426`, `2.431`, `2.432`, `2.436`,
`2.437`, `2.438`, **`2.440`**.

**LAS TRES MAS DISCUTIBLES, y la R48 empieza aqui:**

1. **2.440.** Es la mas fina del tramo: el que muere aporta **dos lineas** y una de ellas,
   el apoyo al que queda fuera de tolerancias, **no la cubre nadie en el superviviente**.
   **Si el auditor lee que eso es un paso y no una linea, el par se voltea.**
2. **2.431**, ya releida y confirmada (R47), **queda marcada mientras el acto de
   `accion_correctiva` siga en colapso**: su superviviente es **provisional por 9.3** hasta
   que se lea la familia entera.
3. **2.432**, ya releida y confirmada, **queda marcada como el ejemplar de la clase 9.28**:
   la denominacion **Taguchi** tiene que reponerse en el texto del superviviente.

### 84.5 LO QUE FALTA

**Faltan 174 pares del encargo, del 2.444 al 2.617.** **Checkpoints 2.500 y 2.600
pendientes.** El dominio son **844 pares** y llega al **3.255**.

**El archivo esta en 2.443 sin huecos ni duplicados. Cero nodos tocados.**


---

## 85. REPORTE DEL TRAMO 2.444 A 2.448

**Corte: puesto 2.448. Van 37 pares de `quality`** de sus 844.

### 85.1 CIFRAS

| | pares | A | D | **tasa** |
|---|---:|---:|---:|---:|
| **`quality`** | **37** | **15** | **22** | **40,5%** |
| archivo global (corte 2.448) | 2.448 | **469** | **1.883** | **19,2%** (B 89, C 7) |

**La tasa del dominio se estabiliza: 44,4% al 2.438, 40,6% al 2.443, 40,5% al 2.448.**
Tres cortes seguidos y el ultimo movimiento es de **una decima**. **Sigue sin ser una banda
publicable**, pero **por primera vez el dominio deja de saltar.**

### 85.2 LA VARA POR TRAMO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **4** |
| **REPITE** | **15** |
| no se invoco | **18** |

**19 de 37, el 51%.** **Cero PENDIENTE DE DOCTRINA. 19 ARISTA QUE FALTA (51%), 14 SOLAPE
DECLARADO.**

### 85.3 LO QUE ANADE ESTE TRAMO

**TERCERA APARICION DEL TITULO ESPEJO (2.447).** `estilo_gerencial_ballet_vs_hockey` contra
`estilo_gerencial_hockey_vs_ballet`: **el mismo contraste dicho al derecho y al reves**,
como el 2.221 (`new_view_vs_old_view` contra `old_view_vs_new_view_human_error`) y el
2.412 (`capacidad_de_proceso` contra `capacidad_del_proceso`).

> **Y las tres veces la lectura fue distinta: A, D y A.** El titulo espejo **es una senal
> de sospecha, no un veredicto**, exactamente igual que el sufijo `_2`. **Cuarta cara de la
> misma familia.**

**DOS PARES QUE SE REPARTEN UNA DOCTRINA POR MITADES, y ninguno esta cableado.**

| puesto | una mitad | la otra |
|---:|---|---|
| **2.444** | **Deming**: como se RECONOCE una causa especial (datos cronologicos, cartas, reglas, investigar antes de perder la evidencia) | **Juran**: por que PUERTA sale cada una, PDCA para la especial y **DMAIC para la comun**, mas la advertencia del **tampering** |
| **2.448** | la **curva de aprendizaje** para saber cuando parar de entrenar | **el tercer caso**: en control **pero** desempeno insatisfactorio, que pide **reasignacion con nueva capacitacion** |

**UNA PERDIDA DE NOMBRE QUE NO LO ES (2.445).** Muere `estandares_especificos_industria` y
se lleva **AS9100 e ISO 14000**, que son las dos normas por las que un lector de otro rubro
llegaria. **No entra en la clase 9.28** porque **el superviviente si nombra ISO y cGMP**:
lo que se pierde **no es la denominacion del instrumento, es la lista de ejemplos**. **Se
anota como perdida de linea con motivo de alcance.**

**Y el superviviente de ese par trae la unica precision del catalogo sobre la c de cGMP:**
*actualizar procesos y tecnologia para cumplir con el caracter **actualizado** que exigen
regulaciones como cGMP*. **Es lo que distingue esa norma de una certificacion que se saca
una vez.**

### 85.4 LAS 15 A DE `quality`, con las discutibles marcadas

`2.414`, `2.417`, `2.418`, `2.420`, `2.421`, `2.424`, `2.426`, `2.431`, `2.432`, `2.436`,
`2.437`, `2.438`, `2.440`, **`2.445`**, **`2.447`**.

**LAS TRES MAS DISCUTIBLES, y la R49 empieza aqui:**

1. **2.445.** Muere el nodo con **la lista de ejemplos mas ancha** (AS9100, ISO 14000) y
   sobrevive el que trae **un requisito sustantivo** (mantener la tecnologia actualizada).
   **La vara manda por contenido**, pero **la puerta de entrada del lector de aeronautica o
   de ambiental se va con el que muere.**
2. **2.447.** El superviviente gana por **un protocolo de reunion completo**, y lo que
   muere aporta **capacitar a los supervisores en comunicacion**. **Es linea por la vara y
   es la unica accion de formacion del par**: sin ella el protocolo queda escrito para
   alguien que ya sabe conducir una reunion.
3. **2.440**, ya releida y confirmada (R48), **queda marcada con su clasificacion
   corregida**: no es perdida de catalogo sino **arista candidata**, y los dos nodos que la
   cubren estan sin cablear.

### 85.5 LO QUE FALTA

**Faltan 169 pares del encargo, del 2.449 al 2.617.** **Checkpoints 2.500 y 2.600
pendientes.** El dominio son **844 pares** y llega al **3.255**.

**El archivo esta en 2.448 sin huecos ni duplicados. Cero nodos tocados.**


---

## 86. REPORTE DEL TRAMO 2.449 A 2.452

**Corte: puesto 2.452. Van 41 pares de `quality`** de sus 844.

### 86.1 CIFRAS

| | pares | A | D | **tasa** |
|---|---:|---:|---:|---:|
| **`quality`** | **41** | **16** | **25** | **39,0%** |
| archivo global (corte 2.452) | 2.452 | **470** | **1.886** | **19,2%** (B 89, C 7) |

**Cuatro cortes seguidos:** 44,4% . 40,6% . 40,5% . **39,0%**. **La cifra se asienta y baja
despacio**, que es la forma que el 9.19 predice para una cola que empieza a perder gemelos.
**Sigue sin banda publicable.**

### 86.2 LA VARA POR TRAMO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **5** |
| **REPITE** | **16** |
| no se invoco | **20** |

**21 de 41, el 51%.** **Cero PENDIENTE DE DOCTRINA. 22 ARISTA QUE FALTA (54%), 17 SOLAPE
DECLARADO.**

### 86.3 LO QUE ANADE ESTE TRAMO

**SEGUNDO EJEMPLAR DE LA CLASE PERDIDA DE ALCANCE (2.451)**, y confirma que la clase hacia
falta. Muere `roi_breakthrough` y se lleva **el caso de exito nombrado, el Six Sigma de
Samsung**. El superviviente **calcula el ROI mejor** (trae la formula explicita) **y no
menciona ningun benchmark**.

> **La clase se distingue de la perdida de nombre (9.28) por lo mismo que en el 2.445: no
> falta la denominacion del instrumento, falta EL EJEMPLO CON EL QUE SE CONVENCE.** Aqui el
> destinatario esta nombrado en el propio paso que muere: *justificar la inversion continua*
> **ante la direccion**. **Un ROI bien calculado y sin un caso al lado no mueve un
> presupuesto.**

**Y se va con el una segunda linea que no es de alcance sino de destino:** *documentar el
ROI **para reportarlo a la direccion***. **Calcularlo bien y reportarlo hacia arriba son dos
cosas**, y el superviviente solo hace la primera.

**TRES PARES QUE SE REPARTEN UNA DOCTRINA Y NINGUNO CABLEADO.**

| puesto | una mitad | la otra |
|---:|---|---|
| **2.449** | los **factores de complejidad** para normalizar, y el septimo paso, **institucionalizar con capacitacion continua** | **el cronograma acordado con los participantes** y **el instrumento de recoleccion con validaciones incorporadas** |
| **2.450** | **clasificar las barreras por origen** y **poner dueno a cada una** | las tres barreras que no se van clasificando: **las evaluaciones que dan miedo**, **el supervisor que no conoce el trabajo tecnico**, y **actuar visiblemente sobre las sugerencias** |
| **2.452** | **estar donde se hace el trabajo** y **escribir tu mismo los reportes** | **sostener el compromiso durante anos** y **no dejar la calidad en un area aislada** |

> **El 2.452 tiene la forma mas limpia de las tres: uno dice que hace el dueno el lunes y
> el otro que tiene que seguir siendo cierto en tres anos.**

### 86.4 LAS 16 A DE `quality`, con las discutibles marcadas

`2.414`, `2.417`, `2.418`, `2.420`, `2.421`, `2.424`, `2.426`, `2.431`, `2.432`, `2.436`,
`2.437`, `2.438`, `2.440`, `2.445`, `2.447`, **`2.451`**.

**LAS TRES MAS DISCUTIBLES, y la R50 empieza aqui:**

1. **2.451.** La clase se sostiene por la formula, **pero lo que muere es lo unico del par
   que se ocupa de que el numero LLEGUE a quien decide**: el reporte hacia arriba y el caso
   de exito que lo respalda. **Es la segunda vez en siete pares que el superviviente gana
   por precision de calculo y pierde por capacidad de persuasion.**
2. **2.445**, ya releida y confirmada (R49), **queda marcada como el ejemplar que da nombre
   a la clase**, con su remedio ya escrito.
3. **2.447**, ya releida y confirmada, **queda marcada por la unica accion de formacion del
   par**, que sigue sin heredero.

### 86.5 LO QUE FALTA

**Faltan 165 pares del encargo, del 2.453 al 2.617.** **Checkpoints 2.500 y 2.600
pendientes.** El dominio son **844 pares** y llega al **3.255**.

**El archivo esta en 2.452 sin huecos ni duplicados. Cero nodos tocados.**


---

## 87. REPORTE DEL TRAMO 2.453 A 2.456

**Corte: puesto 2.456. Van 45 pares de `quality`** de sus 844.

### 87.1 CIFRAS

| | pares | A | D | **tasa** |
|---|---:|---:|---:|---:|
| **`quality`** | **45** | **17** | **28** | **37,8%** |
| archivo global (corte 2.456) | 2.456 | **471** | **1.889** | **19,2%** (B 89, C 7) |

**Cinco cortes:** 44,4% . 40,6% . 40,5% . 39,0% . **37,8%**. **Baja monotona desde el
segundo corte**, y **la caida se desacelera**: 3,8 puntos, 0,1, 1,5, 1,2. **Sigue sin banda
publicable**, pero **la forma es ya la del 9.19**: la cola pierde gemelos poco a poco.

### 87.2 LA VARA POR TRAMO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **6** |
| **REPITE** | **17** |
| no se invoco | **22** |

**23 de 45, el 51%.** **Cero PENDIENTE DE DOCTRINA. 23 ARISTA QUE FALTA (51%), 19 SOLAPE
DECLARADO.**

### 87.3 LO QUE ANADE ESTE TRAMO

**UN PAR DONDE EL SOLAPE ES DE CUATRO PASOS Y AUN ASI ES SANO (2.456).**
`diseno_experimentos_doe_mejora` y `dmaic_fase_improve` comparten **planificar los
experimentos, el cribado factorial fraccionado, los factoriales 2k y RSM o EVOP**, y **cada
uno sigue por su lado despues del solape**: uno termina **en el modelo matematico con los
ajustes optimos**, el otro **en la mejora disenada e implementada**.

> **Es el solape mas grande del dominio que no da A**, y por eso conviene tenerlo escrito:
> **el tamano del solape no decide.** Lo que decide es **si lo que queda fuera del solape
> es procedimiento en los dos lados**, y aqui lo es. **Uno acaba en la ecuacion y el otro
> en el taller.**

**DOS PARES DE IDS GEMELOS CON CONTRAPARTES DISTINTAS.**

| puesto | uno | el otro |
|---:|---|---|
| **2.455** | `definiciones_operacionales` pone de acuerdo **a los de dentro**, con supervisores e inspectores y **ejemplos fisicos de conforme y no conforme** | `definiciones_operacionales_de_calidad` pone de acuerdo **al cliente**, traduciendo requisitos subjetivos y **compartiendole las cartas de control** |
| **2.454** | `analisis_capacidad_proceso` **audita la cuenta**: Cpk, Cpm y **los cinco supuestos** que dicen cuando el numero NO vale | `capacidad_proceso_concepto` **acota el proceso** (maquina, metodo, material, personas) y **dice para que sirve el resultado** |

**UNA PERDIDA DE METODO (2.453).** Muere `sistema_estable_responsabilidad_gerencial` y se
lleva **la recoleccion por observacion planificada, con conteos puntuales y muestreos
periodicos**. El superviviente pide **datos diarios durante varias semanas**.

> **No es perdida de nombre, ni de alcance, ni de destino: es de METODO ALTERNATIVO.** Y
> tiene el mismo peso de producto que las otras tres: **es lo unico del par que sirve a
> quien no puede tomar datos todos los dias**, que es la mayoria de los negocios pequenos.
> **Se anota en el reparto con nombre propio.**

### 87.4 LAS 17 A DE `quality`, con las discutibles marcadas

`2.414`, `2.417`, `2.418`, `2.420`, `2.421`, `2.424`, `2.426`, `2.431`, `2.432`, `2.436`,
`2.437`, `2.438`, `2.440`, `2.445`, `2.447`, `2.451`, **`2.453`**.

**LAS TRES MAS DISCUTIBLES, y la R51 empieza aqui:**

1. **2.453.** La clase se sostiene: el que muere **se salta la clasificacion comun contra
   especial**, que es el paso que decide el camino. **Pero lo que se lleva es un metodo de
   recoleccion mas barato**, y este catalogo es para negocios que no miden a diario. **Es
   el cuarto motivo de perdida de linea, y el primero que no estaba en la tabla.**
2. **2.451**, ya releida y confirmada (R50), **queda marcada como el ejemplar que dio
   nombre a la regla de la persuasion.**
3. **2.447**, ya releida y confirmada, **sigue sin heredero para la unica accion de
   formacion del par.**

### 87.5 LO QUE FALTA

**Faltan 161 pares del encargo, del 2.457 al 2.617.** **Checkpoints 2.500 y 2.600
pendientes.** El dominio son **844 pares** y llega al **3.255**.

### TANDA R51: un puesto, el 2.453, COINCIDE

**18 ago 2026. La A se sostiene**, y con ella **la tabla de perdidas pasa a cuatro
motivos** (seccion 8).

| | |
|---|---:|
| relecturas ciegas | **11** (R42 a R51) mas el barrido de direccion |
| puestos releidos | **25** |
| caidas | **4** . dentro del marcado **4** . fuera **0** |

> **Once relecturas y ninguna discrepancia fuera de la lista de marcados.** La metrica de
> credito sigue entera.

### TANDA R52: dos puestos, DOS DE DOS COINCIDEN, y se resuelve el riesgo marcado

**18 ago 2026. 2.458 y 2.460, las dos coinciden.**

| | |
|---|---:|
| relecturas ciegas | **12** (R42 a R52) mas el barrido de direccion |
| puestos releidos | **27** |
| caidas | **4** . dentro del marcado **4** . fuera **0** |

#### EL RIESGO DEL 2.458, RESUELTO: la particion por direccion es LINEA

**Lo que se habia marcado:** *si el auditor lee que la particion por direccion es un paso y
no una linea, el par se voltea a fusion mutua*. **No procede.**

> **La particion CABE COMO ESPECIFICACION DE QUIEN A QUIEN DENTRO DE LOS PASOS DEL
> SUPERVIVIENTE**, y por eso es linea: no pide un paso propio, **pide dos incisos**. El
> remedio escrito en la tabla de perdidas lo demuestra: *con los requisitos bajando del
> proveedor al procesador* y *subiendo del cliente al procesador* **son dos frases dentro
> de pasos que ya existen.**
>
> **La A se sostiene, y la perdida entra al reparto como QUINTO MOTIVO: DIRECCION.**

#### OTRO EJEMPLAR DE ARISTA QUE NO EXCULPA, y ya son 55

**El 2.458 tenia ARISTA PUESTA entre los dos nodos y aun asi repitio.**

| | |
|---|---:|
| A del archivo | **472** |
| **A con la arista YA PUESTA entre los dos nodos** | **55 (11,7%)** |
| en `core` | 42 . `exportacion` 4 . `environmental` 3 . `health_safety` 3 . **`quality` 3** |
| los tres de `quality` | **2.420**, **2.432**, **2.458** |

> **UNA DE CADA NUEVE A ESTABA CABLEADA.** El cable **dice que alguien vio la relacion**;
> **no dice que los dos nodos hagan cosas distintas.** Es la simetrica de la ARISTA QUE
> FALTA: alli el grafo **no vio** una jerarquia real; aqui **vio** un parentesco y lo
> cableo **en vez de** fundirlo.
>
> **Para la fusion importa, y la adjudicacion de la R53 corrige como se dijo aqui:** ver
> abajo.

### TANDA R53: dos puestos, DOS DE DOS COINCIDEN

**18 ago 2026. 2.461 y 2.464, las dos coinciden.**

| | |
|---|---:|
| relecturas ciegas | **13** (R42 a R53) mas el barrido de direccion |
| puestos releidos | **29** |
| caidas | **4** . dentro del marcado **4** . fuera **0** |

#### LOS 55 PARES CON ARISTA PUESTA: no es trabajo manual

**CORRECCION DECLARADA a lo escrito en la R52.** Alli se dijo que *fundir obliga ademas a
rehacer la arista*. **No es asi, y el mecanismo ya esta medido en este mismo informe.**

> **AL FUNDIR, LA ARISTA INTERNA RESUELVE AL SUPERVIVIENTE POR ALIAS, Y LO QUE NACE ES UNA
> AUTO-ARISTA.** Es el mismo mecanismo de **las 27 auto-aristas del grafo vivo** (§31.3):
> el id muerto queda en `ids_alias`, la arista sigue resolviendo, **y acaba apuntando al
> nodo consigo mismo.**

| | |
|---|---|
| **lo que NO es** | rehacer aristas a mano, par por par |
| **lo que SI es** | **carga de `OP-S-12`**, saneo mecanico, **con su guarda `OP-C-05`** |
| **quien lo reporta antes** | **la simulacion P.7**, que toda operacion de mesa exige antes de escribirse lista |

**LOS 55, por dominio:** `core` **42**, `exportacion` **4**, `environmental` **3**,
`health_safety` **3**, `quality` **3**. **El anexo con los 55 puestos queda en PENDIENTES**,
enlazado para el recomputo.

#### EL PATRON DEL NEGOCIO PEQUENO, con su regla y sus dos salidas

> **EN CADA FUSION SE MIRA QUIEN CONSERVA LA ESCALA.**

**Y las dos salidas no son la misma cosa ni piden lo mismo:**

| salida | que es | ejemplar | que se hace |
|---|---|---|---|
| **LINEA QUE VIAJA** | la escala esta **en una frase** dentro de un nodo que por lo demas repite | **2.414**: *aunque sea de dos o tres personas* | **entra al reparto** como perdida de linea |
| **MOMENTO CON PROCEDIMIENTO PROPIO** | la escala **tiene pasos propios** y por eso el par es **D** | **2.464**: `zero_defects_concepto`, con *marcar el dia aunque sea contigo mismo* y *el compromiso por escrito entre dos* | **no se fusiona**: se cablea |

> **La diferencia decide si el nodo muere o vive**, y por eso la regla no es *conservar la
> escala*, es **mirar quien la conserva antes de decidir la direccion.**

#### LA TRAMPA DEL IDENTIFICADOR, RE-MEDIDA: no es 60%, es 25%

**CORRECCION DECLARADA de una cifra publicada** (§82.2 y §84.3, banco 9.21).

| | cifra publicada | **re-medida** |
|---|---:|---:|
| pares de `quality` con ids **de la misma familia** | 5 | **8** |
| de esos, **repiten** (A) | 3 | **2** |
| **acierto del identificador** | **60%** | **25%** |

**Por que cambia:** la cuenta vieja **solo miraba el sufijo numerico**. La definicion
completa de familia incluye tambien **preposicion y articulo**, y al abrirla entran tres
pares mas, **los tres D**: 2.412 (`capacidad_de_proceso` / `capacidad_del_proceso`), 2.415
(`planificacion_de_la_inspeccion` / `planificacion_inspeccion`) y 2.439.

> **La conclusion no cambia, se refuerza: el identificador ORDENA Y NO DECIDE.** Y ahora
> **acierta uno de cada cuatro**, no dos de cada tres. **Los seis D son las seis derrotas
> del identificador ante la lectura.**

**Y UNA PRECISION SOBRE EL 2.464, que NO es una de ellas.** `cero_defectos` contra
`zero_defects_concepto` **no comparten raiz de id**: uno esta en castellano y el otro en
ingles. **No es el identificador el que falla ahi, es otra senal: EL SINONIMO TRADUCIDO.**
Queda anotada como **quinta cara** de la familia de senales de superficie, **sin cifra
todavia** porque un solo caso no la tiene.

#### EL CATCHBALL DEL 2.463: ARISTA CANDIDATA

`desplegar_metas_organizacion` **reparte** (subdividir, asignar, cronogramas, diagrama de
arbol, dueno del proceso al terminar) y `despliegue_metas` **pacta** (que los niveles de
accion elijan los proyectos, y negociar recursos entre niveles hasta el acuerdo).

> **El hoshin necesita los dos y no estan cableados. ARISTA CANDIDATA**, y de las mas
> claras del dominio: **sin el pacto, el reparto es una orden; sin el reparto, el pacto no
> tiene sobre que.**

### TANDA R54: dos puestos, DOS DE DOS COINCIDEN

**18 ago 2026. 2.465 y 2.467, las dos coinciden.**

| | |
|---|---:|
| relecturas ciegas | **14** (R42 a R54) mas el barrido de direccion |
| puestos releidos | **31** |
| caidas | **4** . dentro del marcado **4** . fuera **0** |

#### EL 2.465: LA COMPROBACION TAMBIEN ABSUELVE, y es la tercera vez

**Se marco por sospecha de perdida de nombre** (el metodo se busca por **DMADV**) **y por
la duda del id**. **Las dos partes se comprueban y las dos absuelven.**

| lo sospechado | lo verificado |
|---|---|
| el superviviente **no dice DMADV** | su titulo es **DFSS y Metodologia DMADV**: la denominacion **vive en el texto** |
| **muere el id** `design_for_six_sigma_dmadv`, que es por donde entra el grafo | **esa es la funcion medida del alias**: el id muerto queda en `ids_alias` y **las aristas siguen resolviendo** (§31.3, las 27 auto-aristas) |

> **PERDIDA DE NOMBRE: CERO.** El alias **no cubre la busqueda del lector** (banco 9.28) **y
> si cubre la entrada del grafo**, que es exactamente lo que se necesitaba aqui. **Las dos
> mitades del problema tienen cada una su mecanismo, y en este par los dos estan cubiertos.**

**TERCERA VEZ QUE UNA COMPROBACION BARATA EVITA UN REGISTRO FALSO, y las tres en `quality`
o su vispera:**

| puesto | lo que se iba a escribir | lo que dijo el grafo |
|---:|---|---|
| **2.414** | arista candidata al COPQ | **la arista ya estaba puesta** |
| **2.440** | perdida de catalogo con prioridad de rescate | **el catalogo lo tiene dos veces y mejor** |
| **2.465** | perdida de nombre, DMADV | **la denominacion esta en el titulo y el alias cubre el grafo** |

> **Las tres absoluciones costaron una consulta cada una.** Es la misma economia que la
> disciplina del dictado ya tenia escrita: **el error muere en la consulta y no en el
> registro.**

#### EL 2.467: SEGUNDO EJEMPLAR DE SALVAGUARDA

Muere `regla_todo_o_nada_inspeccion` y se lleva *anota tu decision y **sigue revisando con
cartas de control que la fraccion de defectos se mantenga estable***.

> **Se adosa AL PASO DE DECISION**, el de comparar p contra k1 partido k2. Sin el freno,
> **ese paso se resuelve una vez y queda fijo**: el superviviente **supone que p sigue donde
> estaba y no manda comprobarlo.**
>
> **Dos ejemplares en seis pares** (2.461 y 2.467) **y los dos protegen un paso de
> DECISION**, no uno de ejecucion. **Es la firma de la clase.**

### LA QUINTA CARA DE LAS SENALES DE SUPERFICIE: EL SINONIMO TRADUCIDO

**Registrada el 18 ago 2026, SIN CIFRA, y esperando su segundo caso.**

| la senal | la medicion | como falla |
|---|---|---|
| **el vocabulario** | 34 de 46, **1 lo era: 3%** | **no ve el parecido** |
| **el identificador** | 8 pares, **2 A: 25%** (re-medido) | **ve parecido donde no lo hay** |
| **la subcadena** | 3 detectados, **1 falso** | **inventa la senal** |
| **el titulo espejo** | 3 apariciones, **2 A: 67%** | **acierta dos de cada tres** |
| **EL SINONIMO TRADUCIDO** | **1 caso: el 2.464** | **invisible para las cuatro anteriores** |

> **`cero_defectos` contra `zero_defects_concepto` son el mismo concepto y NO comparten
> raiz de id, ni vocabulario suficiente, ni titulo espejo.** Ninguna de las cuatro senales
> lo empareja: **lo emparejo la similitud semantica de la cola, y lo resolvio la lectura.**
>
> **Un caso no es una cifra**, asi que la quinta cara **queda anotada y sin porcentaje.**
> **Lo que si se puede decir ya: el catalogo mezcla castellano e ingles en los ids del
> mismo concepto**, y **eso es un riesgo para cualquier deduplicacion que se apoye en la
> forma del nombre**, que es justo lo que la advertencia de aduana de PENDIENTES pide
> evitar.

**El archivo esta en 2.456 sin huecos ni duplicados. Cero nodos tocados.**


---

## 88. REPORTE DEL TRAMO 2.457 A 2.460

**Corte: puesto 2.460. Van 49 pares de `quality`** de sus 844.

### 88.1 CIFRAS

| | pares | A | D | **tasa** |
|---|---:|---:|---:|---:|
| **`quality`** | **49** | **18** | **31** | **36,7%** |
| archivo global (corte 2.460) | 2.460 | **472** | **1.892** | **19,2%** (B 89, C 7) |

**Seis cortes:** 44,4% . 40,6% . 40,5% . 39,0% . 37,8% . **36,7%**. **Cinco bajadas
seguidas y cada una menor que la anterior.** Sigue sin banda publicable, **y la forma ya no
deja duda: es la cola del 9.19 perdiendo gemelos.**

### 88.2 LA VARA POR TRAMO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **6** |
| **REPITE** | **18** |
| no se invoco | **25** |

**24 de 49, el 49%.** **Primera vez que la vara baja del 50% en `quality`.**
**Cero PENDIENTE DE DOCTRINA. 25 ARISTA QUE FALTA (51%), 22 SOLAPE DECLARADO.**

### 88.3 LO QUE ANADE ESTE TRAMO

**TERCERA FAMILIA QUE SE DECIDE DE A DOS (2.460), y conviene tenerlas contadas.**

| familia | miembros vistos | lo que pasa |
|---|---:|---|
| `accion_correctiva` | **5 en la cola** | `_6` murio dos veces, y **su superviviente `_5` murio despues** (2.431). Registrada como **ACTO EN COLAPSO** |
| los **ROI** | 3 | `roi_breakthrough` murio contra `roi_proyectos_calidad` (2.451), que a su vez fue **D** contra `calculo_roi_calidad` (2.427) |
| las **adopciones ISO sectoriales** | 3 | `estandares_especificos_industria` **murio** en el 2.445 y **sobrevive** en el 2.460 |

> **Las tres son correctas par a par y las tres piden lo mismo: por 9.3, la direccion
> decidida sobre un par no sobrevive a su familia.** El superviviente final **se elige una
> vez, sobre la nomina completa**, y hasta entonces **los supervivientes por par son
> provisionales.**

**DOS FASES CONSECUTIVAS QUE SI ESTAN CABLEADAS (2.457).** `prepare_phase_roadmap` crea los
charters y `launch_phase_roadmap` los asigna, **y su paso 1 nombra a la fase anterior**.
**Es el par mas limpio del tramo**: solape de una bisagra, arista puesta, nada que arreglar.

**UNA PERDIDA DE DIRECCION (2.458).** Muere `pensamiento_sistemico_rol_triple` y se lleva
**la particion por direccion**: *canales de requisitos del proveedor al procesador* contra
*loops de control del cliente al procesador*.

> **Es lo unico del par que dice que LOS REQUISITOS BAJAN Y LA RETROALIMENTACION SUBE.** El
> superviviente exige expectativas explicitas entre cada par de roles y bucles que midan
> cumplimiento, **pero no dice en que sentido corre cada cosa.** **Entra al reparto como
> perdida de linea, motivo ALCANCE**: no falta el nombre ni el destino, **falta la mitad
> del mapa.**

**Y UNA CIFRA PUBLICADA QUE SOBREVIVE (2.459):** el estandar de referencia del **2,5% al
4% de las ventas** para el costo de calidad **queda del lado del superviviente**. Se anota
porque **es la unica cifra de contraste externo del dominio leida hasta ahora**, y porque
banco 9.21 obliga a que toda cifra viaje con su corte: **es de Crosby, no una medicion de
este catalogo.**

### 88.4 LAS 18 A DE `quality`, con las discutibles marcadas

`2.414`, `2.417`, `2.418`, `2.420`, `2.421`, `2.424`, `2.426`, `2.431`, `2.432`, `2.436`,
`2.437`, `2.438`, `2.440`, `2.445`, `2.447`, `2.451`, `2.453`, **`2.458`**.

**LAS TRES MAS DISCUTIBLES, y la R52 empieza aqui:**

1. **2.458.** El superviviente gana **en los cuatro pasos por afinado**, no por traer nada
   nuevo. **Es la A mas ajustada del dominio**: si el auditor lee que la particion por
   direccion es un paso y no una linea, el par se voltea a **fusion mutua**.
2. **2.460**, aunque quedo **D**: se marca porque **es el par que destapa la tercera
   familia decidiendose de a dos**, y porque el mismo nodo que aqui sobrevive **murio
   quince pares antes**.
3. **2.453**, ya releida y confirmada (R51), **queda marcada como el ejemplar que hizo
   pasar la tabla de perdidas de tres motivos a cuatro.**

### 88.5 LO QUE FALTA

**Faltan 157 pares del encargo, del 2.461 al 2.617.** **Checkpoints 2.500 y 2.600
pendientes.** El dominio son **844 pares** y llega al **3.255**.

**El archivo esta en 2.460 sin huecos ni duplicados. Cero nodos tocados.**


---

## 89. REPORTE DEL TRAMO 2.461 A 2.464

**Corte: puesto 2.464. Van 53 pares de `quality`** de sus 844.

### 89.1 CIFRAS

| | pares | A | D | **tasa** |
|---|---:|---:|---:|---:|
| **`quality`** | **53** | **19** | **34** | **35,8%** |
| archivo global (corte 2.464) | 2.464 | **473** | **1.895** | **19,2%** (B 89, C 7) |

**Siete cortes:** 44,4% . 40,6% . 40,5% . 39,0% . 37,8% . 36,7% . **35,8%**. **Seis bajadas
seguidas**, ninguna mayor que la anterior. **La curva ya no informa nada nuevo: informa que
es una curva.**

### 89.2 LA VARA POR TRAMO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **7** |
| **REPITE** | **19** |
| no se invoco | **27** |

**26 de 53, el 49%.** **Cero PENDIENTE DE DOCTRINA. 28 ARISTA QUE FALTA (53%), 24 SOLAPE
DECLARADO.**

### 89.3 LO QUE ANADE ESTE TRAMO

**UNA PERDIDA QUE NO ENTRA EN NINGUNO DE LOS CINCO MOTIVOS (2.461), y no se fuerza.**
Muere `descubrir_necesidades_cliente` y se lleva: *priorizar de forma consensuada, **sin
asumir jerarquias automaticas por tipo de cliente***.

> **El superviviente prioriza y NO DICE CON QUE CRITERIO.** La linea que muere es **lo unico
> del par que impide que la priorizacion se resuelva sola por tamano de factura.**
>
> **No es NOMBRE, ni ALCANCE, ni DESTINO, ni METODO, ni DIRECCION: es una ADVERTENCIA
> CONTRA UN SESGO POR DEFECTO.** Se anota en el reparto **con nombre propio y sin motivo
> asignado**: la tabla tiene cinco entradas porque cinco fueron adjudicadas, **y esta
> espera adjudicacion en vez de meterse a la fuerza en la mas parecida.**

**EL CATCHBALL DEL HOSHIN, partido en dos nodos y sin cable (2.463).**

| `desplegar_metas_organizacion` | `despliegue_metas` |
|---|---|
| **la mecanica de arriba abajo**: subdividir, asignar, cronogramas, **diagrama de arbol**, y **designar dueno del proceso al terminar** | **la conversacion en los dos sentidos**: que **los niveles de accion elijan los proyectos**, y **negociar los recursos entre niveles hasta el acuerdo** |

> **Uno reparte y el otro pacta**, y el hoshin **necesita los dos**. **ARISTA QUE FALTA.**

**Y SE CONFIRMA POR SEGUNDA VEZ (2.464) LO ANOTADO EN EL 2.434:** el **registro de negocio
pequeno esta concentrado en nodos concretos**, no repartido. `zero_defects_concepto` vuelve
a ser el que dice *aunque sea contigo mismo* y *por escrito entre tu y la persona que te
ayuda*, frente a un `cero_defectos` que despliega el programa **por areas**.

> **Para el reparto esto ya es un patron, no una anecdota: hay nodos que son la version
> ejecutable a escala minima**, y **fundirlos contra su hermano grande sin mirar quien
> conserva la escala es como se pierde el publico de la app.**

### 89.4 LAS 19 A DE `quality`, con las discutibles marcadas

`2.414`, `2.417`, `2.418`, `2.420`, `2.421`, `2.424`, `2.426`, `2.431`, `2.432`, `2.436`,
`2.437`, `2.438`, `2.440`, `2.445`, `2.447`, `2.451`, `2.453`, `2.458`, **`2.461`**.

**LAS TRES MAS DISCUTIBLES, y la R53 empieza aqui:**

1. **2.461.** La clase se sostiene con holgura (el superviviente trae tres cosas propias,
   entre ellas **los usos no previstos y sus riesgos de seguridad**). **Lo que se marca es
   la perdida sin motivo asignado**: la advertencia contra priorizar por tamano de cliente.
   **Si el auditor la clasifica, la tabla pasa a seis.**
2. **2.464**, aunque quedo **D**: se marca porque **es el segundo par donde la escala minima
   vive en un nodo y no en el otro**, y porque la familia de Cero Defectos **tiene al menos
   tres miembros** (`cero_defectos`, `zero_defects_concepto`, `filosofia_zero_defectos`)
   **decidiendose de a dos**, como las otras tres familias ya contadas.
3. **2.458**, ya releida y confirmada (R52), **queda marcada como el ejemplar del quinto
   motivo**, DIRECCION.

### 89.5 LO QUE FALTA

**Faltan 153 pares del encargo, del 2.465 al 2.617.** **Checkpoints 2.500 y 2.600
pendientes.** El dominio son **844 pares** y llega al **3.255**.

**El archivo esta en 2.464 sin huecos ni duplicados. Cero nodos tocados.**


---

## 90. REPORTE DEL TRAMO 2.465 A 2.467

**Corte: puesto 2.467. Van 56 pares de `quality`** de sus 844.

### 90.1 CIFRAS

| | pares | A | D | **tasa** |
|---|---:|---:|---:|---:|
| **`quality`** | **56** | **21** | **35** | **37,5%** |
| archivo global (corte 2.467) | 2.467 | **475** | **1.896** | **19,3%** (B 89, C 7) |

**Ocho cortes:** 44,4% . 40,6% . 40,5% . 39,0% . 37,8% . 36,7% . 35,8% . **37,5%**.

> **La curva se rompe: sube 1,7 puntos tras seis bajadas.** Y **no es una sorpresa ni un
> problema: es la bolsa del 9.19 otra vez**, tres pares con **dos A** seguidas. **El
> precedente esta escrito y medido**: en `health_safety` paso lo mismo entre el 2.388 y el
> 2.400, y el dominio **cerro igual por debajo**. **Con 56 pares de 844, la tasa sigue sin
> ser publicable, y esta subida lo demuestra mejor que las seis bajadas.**

### 90.2 LA VARA POR TRAMO

| la vara dijo | pares |
|---|---:|
| **CONTINUA** | **7** |
| **REPITE** | **21** |
| no se invoco | **28** |

**28 de 56, exactamente la mitad.** **Cero PENDIENTE DE DOCTRINA. 29 ARISTA QUE FALTA
(52%), 25 SOLAPE DECLARADO.**

### 90.3 LO QUE ANADE ESTE TRAMO

**SEGUNDO EJEMPLAR DE LA SEXTA ENTRADA, SALVAGUARDA (2.467), y llega solo seis pares
despues del primero.** Muere `regla_todo_o_nada_inspeccion` y se lleva: *anota tu decision
y **sigue revisando con cartas de control que la fraccion de defectos se mantenga
estable***.

> **Es lo unico del par que impide que una decision de todo o nada se tome una vez y quede
> fija para siempre.** El superviviente **supone que p sigue donde estaba y no manda
> comprobarlo**. **Se adosa al paso de comparar**, que es el que sin el freno se resuelve
> solo.
>
> **Dos ejemplares en seis pares confirman que la sexta entrada no era un caso raro:** el
> 2.461 protege contra **decidir por tamano de cliente**, este contra **decidir una vez y
> no volver a mirar.** **Las dos son advertencias contra la salida facil de un paso
> concreto.**

**UNA PERDIDA DE NOMBRE QUE SE COMPROBO Y NO EXISTIA (2.465).** Muere
`design_for_six_sigma_dmadv` y **la sospecha era inmediata**: el metodo se busca por
**DMADV**. **Comprobado contra el texto del superviviente: su titulo dice *DFSS y
Metodologia DMADV*.** **La denominacion sobrevive y la clase 9.28 no aplica.**

> **Es la tercera vez en el dominio que una comprobacion barata evita un registro falso**,
> despues del COPQ del 2.414 (la arista ya estaba) y del apoyo al que queda fuera del 2.440
> (el catalogo lo tenia dos veces). **La regla de la disciplina del dictado esta pagando
> sola.**

**EL EVENTO KAIZEN, PARTIDO EN CALENDARIO Y ENGANCHE (2.466).**

| `eventos_kaizen_rie` | `kaizen_mejora_continua` |
|---|---|
| **lo que pasa ANTES**: datos de una a tres semanas antes, **formacion de los participantes una semana antes** | **de donde sale el area y como se mide**: el desperdicio **identificado en el VSM**, y el impacto **en velocidad y desperdicio antes y despues** |

> **Sin el calendario, la semana del evento se gasta preparandose. Sin el VSM, el area se
> elige por corazonada.** **ARISTA QUE FALTA.**

### 90.4 LAS 21 A DE `quality`, con las discutibles marcadas

`2.414`, `2.417`, `2.418`, `2.420`, `2.421`, `2.424`, `2.426`, `2.431`, `2.432`, `2.436`,
`2.437`, `2.438`, `2.440`, `2.445`, `2.447`, `2.451`, `2.453`, `2.458`, `2.461`, **`2.465`**,
**`2.467`**.

**LAS TRES MAS DISCUTIBLES, y la R54 empieza aqui:**

1. **2.467.** La clase se sostiene con holgura (el superviviente trae la precondicion de
   control, la prohibicion de muestreos intermedios y la extension a varios proveedores).
   **Lo que se marca es si la salvaguarda es linea o paso**: *seguir revisando con cartas
   de control* **se parece a un paso mas que la del 2.461**, y si el auditor la lee asi, el
   par se voltea.
2. **2.465.** Muere el nodo cuyo id es **el nombre canonico del metodo** (`dmadv`) y
   sobrevive el que lo lleva **solo en el titulo**. **La comprobacion dice que la
   denominacion se conserva**, pero **el id muere**, y el id es por donde entra el grafo,
   no el lector. **Se marca para que la fusion verifique que el alias queda registrado.**
3. **2.461**, ya releida y confirmada (R53), **queda marcada como el ejemplar que hizo
   pasar la tabla a seis motivos.**

### 90.5 LO QUE FALTA

**Faltan 150 pares del encargo, del 2.468 al 2.617.** **Checkpoints 2.500 y 2.600
pendientes.** El dominio son **844 pares** y llega al **3.255**.

### LA FAMILIA kp: PRIMERA DE `quality` CON SUPERVIVIENTE FINAL POR DERECHO

**Registrada el 18 ago 2026.** Tres nodos, **tres pares posibles y los tres leidos**, que es
**la lectura de acto completa que P.5 exige**.

| puesto | el par | resultado |
|---:|---|---|
| **2.467** | `regla_todo_o_nada_inspeccion` contra `punto_equilibrio_calidad_inspeccion` | **A**, muere el primero |
| **2.473** | `economia_de_la_inspeccion` contra `punto_equilibrio_calidad_inspeccion` | **A**, muere el primero |
| **2.480** | `economia_de_la_inspeccion` contra `regla_todo_o_nada_inspeccion` | **A por fusion mutua** |

> **`punto_equilibrio_calidad_inspeccion` GANA LOS DOS PARES DIRECTOS.** No queda ninguna
> lectura pendiente que pueda cambiar al ganador: **el tercer par no lo toca**, y es
> justamente el que se resolvio en fusion mutua entre los dos perdedores.
>
> **ES SUPERVIVIENTE FINAL POR DERECHO, no provisional.**

**Y ESA ES LA DIFERENCIA CON LAS CUATRO DEL 9.3, que siguen provisionales:**

| familia | nodos | pares leidos | estado |
|---|---:|---|---|
| **la regla kp** | 3 | **3 de 3** | **FINAL por derecho** |
| la **ISO sectorial** | 3 | **3 de 3** | **acto completo**, pero reparte A y D entre pares distintos: **el ganador se elige, no se hereda** |
| `accion_correctiva` | **5 en la cola** | 3 | **provisional** |
| los **ROI** | 3 | 2 | **provisional** |
| el **QFD** | 3 | 2 | **provisional** |
| la **auditoria de producto** | 3 | 2 | **provisional** |

> **La leccion que separa a las dos primeras de las otras cuatro no es cuantos pares se
> leyeron: es SI EL GANADOR PUEDE CAMBIAR.** En la kp **no puede**, porque el unico par que
> falta por decidir direccion no incluye al ganador. **En la ISO si**, aunque este leida
> entera, porque el ganador de un par murio en otro.

#### CORREGIDO EL MISMO DIA: LA FILA DE LA ISO Y LA TABLA ENTERA

**La fila de la ISO de la tabla de arriba esta MAL y se deja escrita, tachada por esta
correccion.** La prueba contaba **todos** los pares; **debe contar solo los pares A**,
porque **una D no es sobrevivir a un duelo: es que no hubo duelo**. El acto es **el cierre
transitivo de las A**. Adjudicado y escrito en el banco **9.3.1**.

**EL ERROR FUE COMPARTIDO:** CC lo propuso y **el auditor lo ratifico sin recontar**.

**LA TABLA CORREGIDA, al dia del puesto 2.500:**

| familia | nodos | pares A leidos | especie |
|---|---:|---|---|
| **la regla kp** | 3 | **3 de 3, todas A** | **POR DERECHO**, final |
| **la ISO sectorial** | 3 | **1 A** (2.445); las otras dos D | **POR DERECHO**, final. **Corregido** |
| **`accion_correctiva`** | 6 o mas | **3 A** y 1 D | **POR ELEGIR**, y provisional: faltan pares |
| los **ROI** | 3 | **1 A** (2.451) y 1 D | **provisional** |
| el **QFD** | 3 | **1 A** (2.469) | **provisional** |
| la **auditoria de producto** | 3 | **0 A**, dos D | **FAMILIA SIN ACTO** |
| el **histograma** | 3 | **0 A**, dos D | **FAMILIA SIN ACTO** |

> **La auditoria de producto y el histograma NO son familias provisionales: no son
> familias.** Comparten raiz de id **y no comparten ni una fusion**. Eso es lo que la
> prueba vieja no sabia decir.

### ADJUDICACION DEL 2.473: la atribucion es una afirmacion de fuente y se verifica

**Registrada el 18 ago 2026 junto a su entrada en CONTRADICCIONES INTERNAS.**

`economia_de_la_inspeccion`, de Juran, **se titula Regla de Deming kp** y en su paso 5
**admite el muestreo**. `punto_equilibrio_calidad_inspeccion`, de Deming, **lo prohibe** en
su paso 5.

> **SI ESOS DOS NODOS SE FUNDEN ALGUN DIA, EL ANADIDO DEL MUESTREO SE MARCA COMO AJENO AL
> AUTOR.**
>
> **El motivo, y no es de estilo: una atribucion es una afirmacion de fuente, y las
> afirmaciones de fuente se verifican.** Decir *regla de Deming* **no es un titulo
> decorativo: es una cita**, y una cita que admite lo que el citado prohibe **es una cita
> falsa**.
>
> **Un lector no puede salir de este catalogo creyendo que Deming admite el muestreo.**
> Si la fusion conserva la opcion, **la conserva con su etiqueta**: *variante no atribuible
> a Deming*.

**Y la regla general que deja, del mismo linaje que la disciplina del dictado:** cuando un
nodo **lleva un nombre propio en el titulo**, ese nombre **es una afirmacion comprobable
sobre el contenido**, no una denominacion suelta. **Se comprueba contra el nodo del autor
citado cuando existe en el catalogo**, que es exactamente lo que este par permitio hacer.

**El archivo esta en 2.467 sin huecos ni duplicados. Cero nodos tocados.**

## 91. CHECKPOINT 2.500: el archivo llega a dos mil quinientos veredictos

**Escrito el 18 ago 2026, al cerrar el puesto 2.500.** Tramo `2.488` a `2.500`, trece pares
de `quality`, sin reporte intermedio por encargo.

### 91.1 MARCADOR RECOMPUTADO DESDE EL ARCHIVO

| | |
|---|---:|
| **veredictos** | **2.500**, sin huecos, hasta el puesto 2.500 |
| **A** (REPITE) | **487** |
| **B** (DUDOSO) | 89 |
| **C** (SANO CON FIGURA) | 7 |
| **D** (SANO LIMPIO) | **1.917** |
| **tasa global de A** | **19,5 %** |

**Quedan 888 pares en la cola:** `quality` **755**, `risk_management` **106**,
`seguridad_digital` **27**.

### 91.2 TASA POR DOMINIO

| dominio | pares | A | tasa | B | C | D |
|---|---:|---:|---:|---:|---:|---:|
| `core` | 1.445 | 344 | **23,8 %** | 87 | 7 | 1.007 |
| `health_safety` | 192 | 45 | **23,4 %** | 0 | 0 | 147 |
| `entrega` | 171 | 2 | **1,2 %** | 0 | 0 | 169 |
| `environmental` | 170 | 29 | **17,1 %** | 0 | 0 | 141 |
| `compras` | 155 | 1 | **0,6 %** | 2 | 0 | 152 |
| `franquicias` | 148 | 18 | **12,2 %** | 0 | 0 | 130 |
| `exportacion` | 130 | 15 | **11,5 %** | 0 | 0 | 115 |
| **`quality`** | **89** | **33** | **37,1 %** | 0 | 0 | 56 |

> **`quality` es, con diferencia, el dominio mas repetido del catalogo.** 37,1 % contra el
> 23,8 % de `core`, que era el techo anterior. Y **le faltan 755 pares**, asi que la cifra
> aun se puede mover mucho.

### 91.3 LA VARA POR TRAMO, dentro de `quality`

| tramo | pares | A | tasa |
|---|---:|---:|---:|
| 2.400 a 2.424 | 13 | 6 | **46,2 %** |
| 2.425 a 2.449 | 25 | 9 | 36,0 % |
| 2.450 a 2.474 | 25 | 8 | **32,0 %** |
| 2.475 a 2.499 | 25 | 9 | 36,0 % |

> **La cabeza entrega gemelos y despues la banda se asienta:** 46,2 % en la entrada y
> **32 a 36 % en los tres tramos siguientes**, sin tendencia a la baja. **Es la confirmacion
> del 9.19 y, a la vez, su limite:** el descenso de cabeza a cuerpo existe, pero **el cuerpo
> de `quality` no baja al 20 % como en los dominios anteriores.** Se sostiene.

### 91.4 LA TRAMPA DEL IDENTIFICADOR, RE MEDIDA SOBRE EL ARCHIVO ENTERO

**Sustituye a la cifra anterior, que estaba medida solo sobre `quality` y sobre pocos
pares.** Definicion de familia: **los dos ids comparten raiz**, sea por sufijo numerico o
porque uno extiende al otro.

| alcance | pares | A | tasa |
|---|---:|---:|---:|
| **archivo entero** | **59** | **30** | **50,8 %** |
| solo `quality` | 17 | 5 | **29,4 %** |

> **Un par cuyos ids comparten raiz repite el doble de veces que un par cualquiera:
> 50,8 % contra 19,5 %.** Sigue sin ser un veredicto, pero **es la senal de superficie mas
> fuerte de las cinco caras**, muy por encima del vocabulario (3 %) y del titulo espejo.
>
> **Y sigue sin decidir:** **26 de esos 59 pares salieron D**. Ordena la cola; no la falla.

**HIPOTESIS NO MEDIDA, anotada como tal:** en `quality` la tasa es **la mitad** de la
global, y el 2.499 sugiere por que: **`analisis_flujo_proceso_servicio` no es una serie,
es un alcance nombrado.** *El sufijo vacio (`_2`, `_3`) y el sufijo que dice algo
(`_servicio`) podrian no ser la misma trampa.* **No esta contado. No se publica como cifra.**

### 91.5 FIGURAS NUEVAS Y CRECIDAS EN EL TRAMO

| figura | que paso |
|---|---|
| **EL SUFIJO QUE SI DISTINGUE** (2.499) | **nueva**, y **como hipotesis sin contar**, no como cifra |
| **fusion mutua** (2.498) | **crece de 6 a 7 casos** en el archivo |
| **SALVAGUARDA**, sexto motivo de perdida (2.497) | **tercer ejemplar** |
| **titulo espejo que NO es duplicado** (2.494) | otro ejemplar: dos titulos que dicen *fitness for purpose* y **cero solape de procedimiento** |
| **9.6.3, el tamano no decide** (2.493) | ejemplar limpio: **siete pasos contra cuatro, y el de cuatro trae la unica medicion del par** |
| **9.21, cifra publicada con su corte** (2.498) | los **250.000 dolares** de retorno minimo y las **seis semanas** son de Juran |
| **la comprobacion tambien absuelve** (2.488 y 2.500) | **dos veces mas**, y las dos sobre perdida de nombre |

**LAS DOS ABSOLUCIONES, porque son las que valen:**

- **2.488 acota el aviso del 2.477.** El superviviente **si dice GESTION POR OBJETIVOS en su
  titulo**: la denominacion en castellano **no se pierde**. Lo unico que muere es **el
  acronimo MBO**.
- **2.500 lo hace del otro lado.** Muere el nodo con el id ingles, `value_stream_mapping`,
  **pero el superviviente escribe VALUE STREAM MAPPING en su paso 1**: la denominacion
  **sigue siendo buscable**. **Cero perdida de nombre.**

### 91.6 LAS FAMILIAS DEL 9.3, AL DIA, CON SU ESPECIE DE GANADOR

| familia | nodos | pares leidos | especie |
|---|---:|---|---|
| **la regla kp** | 3 | 3 de 3 | **POR DERECHO**, final |
| **la ISO sectorial** | 3 | 3 de 3 | **PARA ADJUDICAR, ver 91.7** |
| `accion_correctiva` | 6 o mas | 4 | **POR ELEGIR**, y provisional |
| **MBO y metas numericas** | 3 o mas | 2, **las dos A** | **provisional y abierta**, ver abajo |
| los **ROI** | 3 | 2 | provisional |
| el **QFD** | 3 | 1 | provisional |
| **dia de cero defectos** | 3 | 1 | provisional |
| **make certain** | 3 o mas | 1 | provisional |
| la **auditoria de producto** | 3 | 2, **las dos D** | **sin acto**: no hay fusion que decidir |
| el **histograma** | 3 | 2, **las dos D** | **sin acto**: no hay fusion que decidir |

**`accion_correctiva` ES EL EJEMPLAR LIMPIO DE POR ELEGIR:**

| puesto | resultado |
|---:|---|
| 2.418 | **`accion_correctiva_5` GANA** a `accion_correctiva_6` |
| 2.426 | `accion_correctiva_crosby` gana a `accion_correctiva_6` |
| 2.431 | **`accion_correctiva_5` PIERDE** contra `accion_correctiva_sistematica` |
| 2.496 | `accion_correctiva_5` contra `accion_correctiva_crosby`: **D** |

> **Un mismo nodo gana un par y pierde otro.** Eso es lo que obliga a elegir con P.8 y la
> nomina entera delante, y **es exactamente la forma que 9.3.1 describe**.

**LA FAMILIA MBO DEJA UN HUECO QUE P.13 TIENE QUE CERRAR:**
`critica_gestion_por_objetivos` **muere dos veces**, en el 2.477 y en el 2.488, **contra dos
supervivientes distintos**, `eliminar_metas_numericas_gerencia` y
`eliminacion_gestion_por_objetivos_y_numeros`, **que nunca se han leido entre si**. La cola
no trae ese par. **Queda anotado para la mesa.**

### 91.7 PARA ADJUDICAR: EL EJEMPLAR DE 9.3.1 QUE NO SE SOSTIENE

**Lo traigo en vez de arreglarlo, porque contradice una regla escrita hoy mismo.**

**9.3.1 usa la familia ISO sectorial como su ejemplar de GANADOR POR ELEGIR**, con este
argumento: *`estandares_especificos_industria` murio en el 2.445 y sobrevivio en el 2.460*.
**Al recontar la familia con los tres pares delante, el argumento no aguanta:**

| puesto | par | clase |
|---:|---|---|
| 2.445 | `adaptaciones_sectoriales_iso` contra `estandares_especificos_industria` | **A** |
| 2.460 | `adopciones_industria_especifica_iso9000` contra `estandares_especificos_industria` | **D** |
| 2.479 | `adaptaciones_sectoriales_iso` contra `adopciones_industria_especifica_iso9000` | **D** |

> **EL FALLO: una D no es sobrevivir a un duelo, es que no hubo duelo.** Un par sano
> **saca al nodo del acto**; no anade un contendiente. Contadas asi, **la unica fusion de
> la familia es el 2.445**, su ganador `adaptaciones_sectoriales_iso` **no perdio nunca**, y
> `adopciones_industria_especifica_iso9000` **no esta en ese acto**. **La ISO seria POR
> DERECHO, no por elegir.**

**QUE PIDE ESTO, y son dos cosas distintas:**

1. **La distincion en si NO se cae.** Sigue siendo verdad que *lo que decide no es cuantos
   pares se leyeron, es si el ganador puede cambiar*. **Y ahora tiene un ejemplar real de
   POR ELEGIR: `accion_correctiva`.**
2. **Lo que hay que cambiar es la prueba operativa**, que hoy dice *ninguno gano todos los
   pares que lo tocan*. **Deberia contar SOLO LOS PARES A.** Con esa precision, las dos
   familias de dos D, la auditoria de producto y el histograma, **se leen bien de una vez:
   no tienen acto, no tienen ganador que elegir.**

**NO TOCO 9.3.1 NI LA SECCION 90 HASTA QUE ESTO SE ADJUDIQUE.** Cero reparaciones.

### 91.8 LOS DISCUTIBLES MARCADOS PARA LA R55

**Cuatro, y los cuatro del tramo nuevo.** Por la metrica de credito: **si una discrepancia
cae fuera de esta lista, se mueve el credito de toda la tanda, no el de un veredicto.**

| puesto | veredicto | por donde puede caer |
|---:|---|---|
| **2.492** | **D** | `decision_aptitud_uso` cabe entero dentro del paso 2 del otro. Quien mire solo el solape de la aptitud **dira REPITE**. Mi defensa: el otro trae **la medicion contra especificacion**, sin la cual el corto no puede ni empezar |
| **2.498** | **A por fusion mutua** | los cuatro anadidos podrian leerse como procedimiento y no como linea, sobre todo **las cuatro sesiones con intervalos**, que es un diseno de practica espaciada. Si eso es procedimiento, **el par es D** |
| **2.500** | **A** | `value_stream_mapping` trae **flujo de informacion, costo por etapa y priorizacion como cartera**. Tres lineas, dije. **Si la priorizacion cuenta como procedimiento, es D** |
| **2.493** | **D** | el corto solo anade **tres lineas**; el largo tiene siete pasos. Quien aplique la vara sin 9.6.3 delante **dira REPITE del corto** |

---

## 92. CHECKPOINT 2.600: la fuente del informe no queda trunca en el 2.500

**Apendice compacto, adjudicado por el auditor del bucle (acta vuelta 1, 12 ago 2026).** El
reporte en prosa de este checkpoint vive en `docs/loop/REPORTE.md` en git (commit `5834d869`);
esta seccion NO lo re-narra, solo fija las cifras y los commits para que la fuente de
checkpoints del informe no quede cortada en la seccion 91. **Cifras ya verificadas por el
auditor contra el archivo y el grafo, corte 2.600.**

### 92.1 MARCADOR RECOMPUTADO (corte 2.600, sin huecos, sin duplicados)

| | |
|---|---:|
| **veredictos** | **2.600**, hasta el puesto 2.600 |
| **A** (REPITE) | **522** |
| **B** (DUDOSO) | 89 |
| **C** (SANO CON FIGURA) | 7 |
| **D** (SANO LIMPIO) | **1.982** |
| **tasa global de A** | **20,1 %** |

Contra el 2.554 (arranque del bucle): **+14 A y +32 D**. **Quedan 788 pares:** `quality` **655**,
`risk_management` **106**, `seguridad_digital` **27**.

### 92.2 `quality`, EL DOMINIO MAS REPETIDO, Y SU VARA POR TRAMO

`quality` **189 pares, 68 A, 36,0 %**, sigue al frente del catalogo (contra 23,8 % de `core`).
Bajo del 37,1 % del corte 2.500 porque el cuerpo entrega menos que la cabeza, no por caida.

| tramo | pares | A | tasa |
|---|---:|---:|---:|
| 2.501 a 2.525 | 25 | 11 | **44,0 %** |
| 2.526 a 2.550 | 25 | 8 | 32,0 % |
| 2.551 a 2.575 | 25 | 9 | 36,0 % |
| 2.576 a 2.600 | 25 | 7 | **28,0 %** |

> **El cuerpo de `quality` se sostiene entre 28 y 44 %**, sin tendencia a la baja al 20 % de
> los dominios anteriores. El 28,0 % del ultimo tramo es tramo cargado de cumulos todo D
> (benchmarking, cartas de control, seriedad), no descenso. Confirma el 9.19 y su limite.

### 92.3 FAMILIAS DEL 9.3 AL DIA, CON SU ESPECIE (corte 2.600)

| familia | pares leidos | especie |
|---|---|---|
| el **histograma** | 3 de 3 (2.442 D, 2.486 D, 2.517 A) | **POR DERECHO, final** |
| la **auditoria de producto** | 3 de 3, las tres D (2.433, 2.478, 2.594) | **SIN ACTO, cerrada** |
| **causas comunes vs especiales** | gana 2.497, 2.501, 2.577; el 2.532 es fusion mutua entre perdedores | **candidata a POR DERECHO**, falta cola |
| **sistema estable / resp. gerencial** | 2.453 A, 2.537 A, 2.572 A; un nodo gano una y perdio otra | **POR ELEGIR**, provisional (cumulo de 17 nodos sin leer entero) |
| la **capacidad** | 5 de 6, las cinco D | **SIN ACTO A LA FECHA** (falta un par) |
| la **seriedad** | 5 de 6, las cinco D | **SIN ACTO A LA FECHA** (falta un par) |
| **dia de cero defectos** | 2.491 A, 2.525 A mutua | **POR ELEGIR** (9.3.1 visto segundo) |

### 92.4 FIGURAS AL DIA

- **Fusion mutua:** dos casos nuevos, el **decimotercero (2.575)** y el **decimocuarto
  (2.597)**; el duodecimo era el 2.552. Conteo verificado contra el archivo por el auditor.
- **La senal del idioma (quinta cara, 9.28.1):** **cinco apariciones al corte 2.600**, una de
  emparejamiento (2.464) y cuatro de perdida de denominacion (MBO, box plot, VOC, COC 2.593).
  Su TASA se midio en el bucle vuelta 2, ver la nota de medicion del 9.28.1.

### 92.5 CORRECCION DECLARADA Y COMMITS

El tramo trajo una **correccion declarada del propio ejecutor** (la fila de la responsabilidad
gerencial estaba mal medida por saltarse el resolutor; el 2.453 A la parte en dos actos y la
vuelve POR ELEGIR). El texto viejo quedo **tachado sin borrar**, porque el error es la leccion.
Detalle en `docs/loop/REPORTE.md` y en `docs/BANCO_DE_TEXTOS.md` 9.3.1.

| commit | que fija |
|---|---|
| **`f3c3750c`** | el archivo del cribado en 2.600 lineas (el estado que el auditor recomputa) |
| **`5834d869`** | reporte, correccion declarada de 9.3.1 y `.gitignore` del bucle |

---

## 93. CHECKPOINT 2.700: el cuerpo de `quality` entrega familias que se separan

**Apendice compacto (bucle vuelta 2, 12 ago 2026, corte 2.700).** La prosa vive en
`docs/loop/REPORTE.md` en git; esta seccion fija cifras y commits. Cifras recomputadas del
archivo, sin huecos ni duplicados.

### 93.1 MARCADOR (corte 2.700)

| | |
|---|---:|
| **veredictos** | **2.700**, hasta el puesto 2.700 |
| **A** | **~~544~~ 543** (~~20,1~~ 20,1 %) |
| **B** | 89 |
| **C** | 7 |
| **D** | **~~2.060~~ 2.061** (76,3 %) |

Tramo 2.601-2.700: **~~22~~ 21 A y ~~78~~ 79 D (~~22,0~~ 21,0 %)**. Quedan **688 pares**: `quality`
**555**, `risk_management` **106**, `seguridad_digital` **27**. **CORRECCION DECLARADA (bucle
vuelta 8, relectura conjunta acta vuelta 7, TAREA 1.2 del PROMPT_SIGUIENTE.md): el 2.630 pasa
de A a D**, ver 98.2 para el caso completo. Cifras de esta seccion ya recomputadas con la
correccion aplicada (`python scripts/recomputar_marcador.py 2700`).

### 93.2 `quality` y su vara por tramo (2.601-2.700)

`quality` **289 pares, ~~90~~ 89 A, ~~31,1~~ 30,8 %** (baja de 36,0 % porque el tramo entrego
21,0 %; corregido por el 2.630, ver 98.2).

| tramo | pares | A | tasa |
|---|---:|---:|---:|
| 2.601-2.625 | 25 | 6 | 24,0 % |
| 2.626-2.650 | 25 | ~~7~~ 6 | ~~28,0~~ 24,0 % |
| 2.651-2.675 | 25 | 7 | 28,0 % |
| 2.676-2.700 | 25 | 2 | **8,0 %** |

> El ultimo cuarto toca **8,0 %**, el mas bajo del dominio, por cumulos todo D (consejos,
> benchmarking, roadmap, definiciones operacionales, capacidad, costo de calidad, make_certain,
> QFD, responsabilidad gerencial). No es caida de la tasa del inventario: es el cuerpo de
> `quality` separando familias en caras distintas, el limite del 9.19.

### 93.3 FAMILIAS Y FIGURAS AL DIA

| que | estado (corte 2.700) |
|---|---|
| la **capacidad** | **SIN ACTO, cerrada**: 7 de 7 D (cierra el 2.636, extiende el 2.697) |
| el **Consejo de Calidad** | **POR ELEGIR** nuevo, hub `consejo_calidad`, 5 pares A (2.523, 2.631, 2.662, 2.663, 2.670); el nodo del rol del director queda fuera |
| la **regla kp** | **POR DERECHO** se sostiene; `regla_todo_o_nada_2` queda fuera (2.646, 2.690 D) |
| **fusion mutua** | ~~tres nuevas: 15.a (2.630), 16.a (2.638), 17.a (2.666), todas superviviente POR ELEGIR~~ **CORREGIDO (bucle vuelta 8): el 2.630 NO es fusion mutua, pasa a D (98.2); el 2.673 (identificar_clientes_diseno =A= identificar_clientes_externos_e_internos) SI es un caso valido que el checkpoint original no conto. El recuento completo y renumerado del contador vive en 98.1** |
| **senal del idioma** | sin aparicion nueva; cinco al corte 2.700; su tasa medida en 9.28.1 (TAREA 1.3) |

### 93.4 COMMIT

`a5d16eee` (Cribado 2697-2700) fija el archivo en 2.700 lineas, el estado que el auditor
recomputa.

---

## 94. CHECKPOINT 2.800: cien pares casi todo D del cuerpo de `quality`

**Apendice compacto (bucle vuelta 3, 12 ago 2026, corte 2.800).** La prosa vive en
`docs/loop/REPORTE.md` en git; esta seccion fija cifras y commits. Cifras recomputadas del
archivo, sin huecos ni duplicados.

### 94.1 MARCADOR (corte 2.800)

| | |
|---|---:|
| **veredictos** | **2.800**, hasta el puesto 2.800 |
| **A** | **~~563~~ 562** (20,1 %) |
| **B** | 89 |
| **C** | 7 |
| **D** | **~~2.141~~ 2.142** (76,5 %) |

Tramo 2.701-2.800: **19 A y 81 D (19,0 %)**, sin cambio (el 2.630 no cae en este tramo). Los
100 pares fueron `quality`. Quedan **588 pares**: `quality` **455**, `risk_management` **106**,
`seguridad_digital` **27**. **CORRECCION DECLARADA (bucle vuelta 8, TAREA 1.2): el marcador
global baja por el 2.630 (98.2), aunque el tramo 2.701-2.800 no lo contiene.**

### 94.2 `quality` y su vara por tramo (2.701-2.800)

`quality` **389 pares, ~~109~~ 108 A, ~~28,0~~ 27,8 %** (baja de 30,8 % porque el tramo entrego
19,0 %; el 108 arrastra la correccion del 2.630, que es anterior a este tramo).

| tramo | pares | A | tasa |
|---|---:|---:|---:|
| 2.701-2.725 | 25 | 3 | 12,0 % |
| 2.726-2.750 | 25 | 6 | 24,0 % |
| 2.751-2.775 | 25 | 6 | 24,0 % |
| 2.776-2.800 | 25 | 4 | 16,0 % |

> El cuerpo de `quality` sigue por debajo de su banda historica: ficha contra mapa (2.707,
> 2.735, 2.758, 2.769, 2.772, 2.778, 2.782, 2.790), metodo contra encuadre (2.765, 2.767) y
> fase contra fase del roadmap (2.798), cumulos todo D del mismo autor. Es el limite del 9.19.

### 94.3 LA PRECISION DE LA CAPACIDAD (adjudicacion del auditor, acta vuelta 2)

**Contada por raiz la familia de la capacidad lleva 8 pares, los 8 D** (el 2.423, establecer
contra establecimiento, tambien junta dos nodos de la raiz); el 7 de 7 del checkpoint 2.700
contaba la cobertura completa del nucleo de cuatro nodos, 6 pares, mas el 2.697. **SIN ACTO se
sostiene sobre los 8.** Precision del tramo 2.701-2.800, declarada sin retocar lo anterior: la
cola trajo **dos pares mas de la raiz via el nodo nuevo `capacidad_de_proceso_2`** (2.751 contra
`capacidad_del_proceso`, 2.779 contra `capacidad_de_proceso`), **ambos D**. La familia queda en
**10 pares, los 10 D**; no reabre el acto (SIN ACTO), extiende la cobertura, igual que el 2.697
extendio los seis.

### 94.4 FAMILIAS Y FIGURAS AL DIA

| que | estado (corte 2.800) |
|---|---|
| la **capacidad** | **SIN ACTO, sigue cerrada**: 10 de 10 D (extiende con 2.751 y 2.779) |
| la **distincion comun/especial** | **POR DERECHO**, absorbedor `causas_comunes_vs_especiales`: fusiona 2.736, 2.740, 2.752, 2.766, 2.800 (el cumulo del no culpar cae aqui) |
| la **responsabilidad gerencial** | **POR ELEGIR provisional, sigue abierto**: la postura gerencial (remover barreras, comunicar responsabilidad) sale D contra el procedimiento (2.741) y contra los lemas (2.732, 2.793) |
| el **breakthrough / DMAIC** | **POR ELEGIR**: breakthrough_desempeno_actual =A= DMAIC otra vez (2.759, via 2.618 y 2.548) |
| **make_certain, auditorias, costo de calidad, benchmarking, roadmap** | **D pesada por facetas**: familias que separan cada nodo en cara distinta (2.739, 2.768, 2.778, 2.784, 2.798) |
| **fusion mutua** | ~~sin caso nuevo en 2.701-2.800~~ **CORREGIDO (bucle vuelta 8, 98.1): CINCO casos validos que este checkpoint no conto, todos quality: 2.760 (gobierno_corporativo_juntas_directivas =A= planificacion_gobierno_organizaciones_familiares), 2.762 (falacia_recompensa_loteria =A= sistemas_recompensa_aleatorios), 2.773 (comparacion_inspectores_independientes =A= riesgos_consenso_inspeccion), 2.780 (revision_progreso =A= revision_progreso_breakthrough), 2.787 (gestion_estrategica_de_calidad_sqm =A= rol_tactico_estrategico_oficina). El recuento completo y renumerado vive en 98.1** |
| **senal del idioma (quinta cara)** | **sin aparicion nueva**; cinco denominaciones al corte 2.800; su cota se remidio con el barrido del CUERPO (BANCO 9.28.1): recall pleno del numerador, denominador saturado, 6 de 234 = 2,6 % (piso) |

### 94.5 COMMIT

El archivo llega a 2.800 lineas en los commits del tramo (`Cribado 2701-2725` en adelante); el
commit del checkpoint fija el estado que el auditor recomputa.

---

## 95. CHECKPOINT 2.900: diez A del cuerpo de `quality`, la distincion y el breakthrough=DMAIC

**Apendice compacto (bucle vuelta 4, 12 ago 2026, corte 2.900).** La prosa vive en
`docs/loop/REPORTE.md` en git; esta seccion fija cifras y commits. Cifras recomputadas del
archivo, sin huecos ni duplicados.

### 95.1 MARCADOR (corte 2.900)

| | |
|---|---:|
| **veredictos** | **2.900**, hasta el puesto 2.900 |
| **A** | **~~573~~ ~~572~~ 571** (~~19,8~~ ~~19,7~~ 19,7 %) |
| **B** | 89 |
| **C** | 7 |
| **D** | **~~2.231~~ ~~2.232~~ 2.233** (~~76,9~~ ~~77,0~~ 77,0 %) |

Tramo 2.801-2.900: **~~10~~ 9 A y ~~90~~ 91 D (~~10,0~~ 9,0 %)**, sin cambio adicional (el 2.630
no cae en este tramo). Los 100 pares fueron `quality`. Quedan **488 pares**: `quality` **355**,
`risk_management` **106**, `seguridad_digital` **27**. **CORRECCION DECLARADA (bucle vuelta 5,
relectura conjunta acta vuelta 4, 95.3.1):** el 2.805 pasa de A a D. **SEGUNDA CORRECCION
DECLARADA (bucle vuelta 8, relectura conjunta acta vuelta 7, TAREA 1.2):** el 2.630 pasa de A a
D (98.2), y baja el marcador global un escalon mas (el 2.630 es anterior a este corte). Cifras
de esta seccion ya recomputadas con las dos correcciones aplicadas.

### 95.2 `quality` y su vara por tramo (2.801-2.900)

`quality` **489 pares, ~~119~~ ~~118~~ 117 A, ~~24,3~~ ~~24,1~~ 23,9 %** (baja de 27,8 % [corte
2.800 corregido] porque el tramo entrego 9,0 %; corregido por el 2.805 en 95.3.1 y por el 2.630
en 98.2).

| tramo | pares | A | tasa |
|---|---:|---:|---:|
| 2.801-2.825 | 25 | ~~4~~ 3 | ~~16,0~~ 12,0 % |
| 2.826-2.850 | 25 | 1 | 4,0 % |
| 2.851-2.875 | 25 | 1 | 4,0 % |
| 2.876-2.900 | 25 | 4 | 16,0 % |

> El cuerpo de `quality` toca su piso mas bajo (4,0 % en los dos tramos centrales): stretch de
> cumulos cronicos que separan cada nodo (benchmarking, cartas de control, cero defectos,
> programas de 14 pasos, muestreo, cascadeo de diseno, auditorias, capacidad). Las ~~diez~~
> nueve A se concentran en los bordes, donde asoman los cumulos POR DERECHO (la distincion) y
> las identidades ya doctrina (breakthrough=DMAIC, gemelos del Dia ZD). Es el limite del 9.19.
> El 2.805 (borde del primer tramo) sale del conteo de A por la correccion de 95.3.1.

### 95.3 CORRECCION DECLARADA DEL 9.28.1 (TAREA 1, acta vuelta 3)

Dos cifras secundarias del barrido del cuerpo no reproducian con instrumento independiente y se
corrigieron con tachado sin borrar (BANCO 9.28.1, bloque de correccion declarada): **204 a 209**
(pares del universo fuerte cuya senal no se reduce a los fragmentos multipalabra *total*, *of*,
*value*; 25 pares removidos) y **benchmarking 59 a 20** (pares fuertes con el token al corte
2.800). Comando declarado al lado: `python scripts/barrido_quinta_cara_cuerpo.py 2800 --dominio
quality` mas recomputo directo sobre el grafo. **La cota titular (6 de 234 = 2,6 %), la tasa
secundaria (6 de 209 = 2,9 %, identica) y la leccion de las dos cotas quedaron intactas.**

### 95.3.1 CORRECCION DECLARADA DEL 2.805 (relectura conjunta, encargada en el acta vuelta 4)

**El par 2.805 (`accion_correctiva_crosby` contra `accion_correctiva_sistematica`) pasa de**
**~~A~~ a D.** El ejecutor lo habia dictaminado A por transitividad del cumulo (crosby =A=
generico _6 en 2.426, sistematica =A= el mismo _6 en 2.701), pero el auditor senalo la grieta:
el generico _6 tambien cabe en _5 (2.418) y sin embargo _5 =D= crosby (2.496, "sano, arista que
falta"), asi que la contencion compartida de un mismo generico no basta para fundir dos nodos
entre si. Verificado contra el grafo (nodos enteros, no titulos): **crosby trae cuatro pasos
enteros que sistematica no tiene** (consultar directamente al personal operativo, auditorias
independientes periodicas por departamento, reportes formales de ingenieria de calidad, planes
de accion por departamento) y **sistematica trae los suyos que crosby no tiene** (la escalada
diaria a semanal y de ahi a una revision mensual que decide esfuerzo dedicado, el grupo de
trabajo puntual con regla de disolucion para los complejos, ordenar por gravedad). Ninguno cabe
entero en el otro. Ademas, **sistematica es el superviviente de _5** (2.431, pasos uno a uno con
sistematica), y _5 no fundio con crosby (2.496); por la misma vara, sistematica tampoco funde
con crosby. **La regla que queda escrita: la transitividad del cumulo solo compone entre
gemelos (identidad, como el Dia ZD 2.853); con CONTENCION (dos nodos que contienen al mismo
generico) no compone.** Razon del 2.805 corregida en el jsonl con tachado sin borrar (la razon
vieja se conserva completa, la correccion se agrega al final). Efecto en el marcador: A 573 a
572, D 2.231 a 2.232 al corte 2.900; tramo 2.801-2.900 de 10 A a 9 A; tramo 2.801-2.825 de 4 A a
3 A; `quality` de 119 A (24,3 %) a 118 A (24,1 %). Ver 95.1 y 95.2 para las cifras ya
recomputadas.

### 95.4 FAMILIAS Y FIGURAS AL DIA

| que | estado (corte 2.900) |
|---|---|
| la **capacidad** | **SIN ACTO, sigue cerrada**: extiende con 2.827, 2.884, 2.890, todas D; la familia no reabre acto |
| la **distincion comun/especial** | **POR DERECHO**, absorbedor `causas_comunes_vs_especiales`: suma 2.888 (variacion del sistema vs individuo) y 2.897 (distincion en accidentes y Teorema de Nelson) |
| la **responsabilidad gerencial** | **POR ELEGIR provisional, sigue abierto**: la postura gerencial sale D contra la distincion en 2.881 (misma frontera que 2.850) |
| el **breakthrough / DMAIC** | **POR ELEGIR**: 2.887 secuencia_universal_para_el_breakthrough =A= six_sigma_dmaic, la identidad breakthrough=DMAIC de nuevo (via 2.618, 2.759) |
| los **roadmaps** | **DMAIC no es DPLES** (2.862): lean_six_sigma_roadmap es el ciclo de proyecto DMAIC, roadmap_despliegue es el despliegue DPLES; juran_transformation_roadmap =A= roadmap_despliegue (2.811, ambos DPLES) |
| **fusion mutua** | ~~UN caso nuevo: 2.891..., el contador pasa a DIECIOCHO~~ **CORREGIDO (bucle vuelta 8, 98.1): este tramo (2.801-2.900) trae en realidad DOS casos validos mas, ademas del 2.891, que el checkpoint original no conto: 2.816 (eliminacion_barreras_orgullo_del_trabajo =A= orgullo_por_el_trabajo, Punto 12 de Deming) y 2.825 (cinco_suposiciones_erroneas_calidad =A= concepto_supuestos_erroneos_sobre_calidad, Crosby). El recuento completo y renumerado (con el 2.891 en su nueva posicion) vive en 98.1** |
| **senal del idioma (quinta cara)** | **sin aparicion nueva**; cinco denominaciones al corte 2.900; la cota del cuerpo quedo corregida (9.28.1: 6 de 234 = 2,6 %, o 6 de 209 = 2,9 %) |

### 95.5 COMMIT

El archivo llega a 2.900 lineas en los commits del tramo (`Cribado 2801-2825` en adelante); el
commit del checkpoint fija el estado que el auditor recomputa.

---

## 96. CHECKPOINT 3.000: la grieta del 2.916 cerrada, la ficha nombrada dentro del paso, piso de 0,0 %

**Apendice compacto (bucle vuelta 6, 13 ago 2026, corte 3.000).** La prosa vive en
`docs/loop/REPORTE.md` en git; esta seccion fija cifras y commits.

### 96.1 MARCADOR (corte 3.000)

| | |
|---|---:|
| **veredictos** | **3.000**, hasta el puesto 3.000, cero huecos ni duplicados |
| **A** | **~~578~~ ~~577~~ 576** (~~19,3~~ ~~19,2~~ 19,2 %) |
| **B** | 89 |
| **C** | 7 |
| **D** | **~~2.326~~ ~~2.327~~ 2.328** (~~77,5~~ ~~77,6~~ 77,6 %) |

**CORRECCION DECLARADA (bucle vuelta 7, TAREA 1 del PROMPT_SIGUIENTE.md de esa vuelta, seccion
97.2): esta seccion 96.1 NO habia arrastrado la correccion del 2.931 (A a D) cuando se publico.
Corregido ahora: 578 a 577, 2.326 a 2.327.** **SEGUNDA CORRECCION DECLARADA (bucle vuelta 8,
TAREA 1.2, ver 98.2): el 2.630 pasa de A a D, y baja el marcador un escalon mas, 577 a 576 y
2.327 a 2.328.** Cifras ya recomputadas con las dos correcciones aplicadas
(`python scripts/recomputar_marcador.py 3000`). Contra el checkpoint 2.900 corregido (95.1: A
571, D 2.233): +5 A y +95 D en el tramo 2.901-3.000 (el conteo bruto de A nuevas es 7; las
correcciones del 2.916 y el 2.931 restan una cada una).

### 96.2 CORRECCION DECLARADA DEL 2.916 (relectura conjunta, encargada en el acta vuelta 5)

**El par 2.916 (`consejo_de_calidad` contra `consejo_de_calidad_3`) pasa de `~~A~~` a D.** Los
dos eslabones citados como gemelos (2.523, 2.662) son contencion asimetrica (el 2.523 registra
PERDIDA NOMBRADA motivo DESTINO; el 2.662 se resolvio el mismo por transitividad), no identidad;
con un eslabon de contencion la transitividad no compone (regla del 2.805, extendida a su forma
espejo). Lectura directa: `consejo_de_calidad_3` trae dos pasos enteros propios (coordinar la
repeticion del ciclo, institucionalizar el consejo) y `consejo_de_calidad` trae tres (capacitarse
en el metodo, Pareto, asignar recursos) que el otro no tiene. Tachado sin borrar en el jsonl.
Efecto: A 574 a 573 y D 2.255 a 2.256 al corte 2.925 (previo a los tramos nuevos); tramo
2.901-2.925 de 2 A a 1 A.

### 96.3 `quality` y su vara por tramo (2.901-3.000)

`quality` **589 pares, ~~124~~ ~~123~~ 122 A, ~~21,1~~ ~~20,9~~ 20,7 %** (baja desde 23,9 % al
corte 2.900 corregido). **CORRECCION DECLARADA (bucle vuelta 7, seccion 97.2): 124 a 123 A
(21,1 % a 20,9 %) por el 2.931. SEGUNDA CORRECCION (bucle vuelta 8, 98.2): 123 a 122 A (20,9 %
a 20,7 %) por el 2.630, anterior a este corte.**

| tramo | pares | A | tasa |
|---|---:|---:|---:|
| 2.901-2.925 | 25 | 1 | 4,0 % |
| 2.926-2.950 | 25 | ~~3~~ 2 | ~~12,0~~ 8,0 % |
| 2.951-2.975 | 25 | 2 | 8,0 % |
| 2.976-3.000 | 25 | 0 | 0,0 % |

> El tramo 2.976-3.000 entrega el piso mas bajo del cuerpo hasta ahora (0,0 %, el anterior minimo
> fue 4,0 %). Filo dominante: dos cumulos separados de siempre (distincion comun/especial contra
> responsabilidad gerencial) y una figura nueva, la ficha nombrada literalmente dentro del paso
> de otro nodo (seis casos: 2.956, 2.961, 2.963, 2.980, 2.986, y la familia del 2.975/2.991), que
> sigue dando D porque el nodo menor desarrolla mecanica propia que el paso generico no despliega.

### 96.4 FAMILIAS Y FIGURAS AL DIA

| que | estado (corte 3.000) |
|---|---|
| la **capacidad** | **SIN ACTO, sigue cerrada**: extiende con 2.984, 2.996, ambas D pese a sim_tit muy alto (68,0 y 64,9) |
| la **distincion comun/especial** contra **responsabilidad gerencial** | **dos cumulos separados, confirmado tres veces mas** (2.977, 2.985, 2.990), todas D; misma frontera de 2.677, 2.766, 2.800, 2.850, 2.881, 2.906 |
| **fusion mutua** | El 2.952 (cultura de integridad/objetividad contra manejo de problemas, resumenes Crosby casi verbatim) SI es un caso valido nuevo de este tramo. ~~El contador pasa a DIECINUEVE (el anterior fue el 2.891)~~ **CORREGIDO (bucle vuelta 8, 98.1): el ordinal viejo (diecinueve) no calzaba con el archivo (faltaban ocho casos y sobraba el 2.630). El recuento completo y renumerado vive en 98.1** |
| el **breakthrough / DMAIC** | dos identidades nuevas por transitividad hacia el hub ya contado: 2.935 (secuencia universal = breakthrough) y 2.962 (DMAIC en servicios) |
| el **Consejo de Calidad** | grieta del 2.916 cerrada a D (96.2); el hub sigue absorbiendo a `consejo_de_calidad_3` por los eslabones de contencion 2.523 y 2.662, no tocados |
| **ficha nombrada dentro del paso de otro nodo** | figura reconocida esta vuelta, seis casos en 2.901-3.000; siempre D, la vara del paso entero ya la cubre |
| **senal del idioma (quinta cara)** | sin aparicion nueva; cinco denominaciones al corte 3.000 |

### 96.5 DISCUTIBLES MARCADOS (100 de 100, 28 fuertes)

Los 100 pares de 2.901 a 3.000 llevan DISCUTIBLE MARCADO inline en el jsonl, corrigiendo la
densidad baja senalada por el auditor en la vuelta 5 (5 de 25 en el tramo trunco). Las seis A del
tramo nuevo (2.931, 2.935, 2.942, 2.952, 2.962) mas el 2.917 relecturado y el 2.916 corregido son
el riesgo primario. Detalle completo con el filo de cada discutible fuerte en
`docs/loop/REPORTE.md`.

### 96.6 COMMITS

`9e5dc156` (TAREA 1: correccion 2.916, relectura al doble 2.901-2.925, marcado), `facd7b68`
(cribado 2.926-2.950), `20ec558b` (cribado 2.951-2.975), `544c021b` (cribado 2.976-3.000,
checkpoint 3.000, hash final de la vuelta).

---

## 97. CHECKPOINT 3.100: el 2.931 corregido, la disciplina de la cita, cuatro tramos en el piso

**Apendice compacto (bucle vuelta 7, 13 ago 2026, corte 3.100).** La prosa vive en
`docs/loop/REPORTE.md` en git; esta seccion fija cifras y commits.

### 97.1 MARCADOR (corte 3.100)

| | |
|---|---:|
| **veredictos** | **3.100**, hasta el puesto 3.100, cero huecos ni duplicados |
| **A** | **~~579~~ 578** (~~18,7~~ 18,6 %) |
| **B** | 89 |
| **C** | 7 |
| **D** | **~~2.425~~ 2.426** (~~78,2~~ 78,3 %) |

**CORRECCION DECLARADA (bucle vuelta 8, TAREA 1.2, ver 98.2): el 2.630 pasa de A a D**, baja el
marcador un escalon en todos los cortes posteriores, incluido este. Cifras ya recomputadas
(`python scripts/recomputar_marcador.py 3100`). Contra el checkpoint 3.000 corregido (96.1: A
576, D 2.328): +2 A y +98 D en el tramo 3.001-3.100, sin cambio (el 2.630 es anterior a este
tramo).

### 97.2 CORRECCION DECLARADA DEL 2.931 (relectura conjunta, encargada en el acta vuelta 6)

**El par 2.931 (`error_proofing_servicio` contra `poka_yoke_a_prueba_de_errores`) pasa de
`~~A~~` a D.** Los dos eslabones citados como identidad (2.737, 2.613) se cierran con firma de
contencion ("A por contencion"; "trae de mas"), la misma frase que el propio cribado trata como
contencion en el 2.933; la transitividad no compone. Lectura directa: conjuntos de pasos
disjuntos entre los dos nodos. Tachado sin borrar. Efecto: A 578 a 577, D 2.326 a 2.327 al corte
3.000; tramo 2.926-2.950 de 3 A a 2 A (12,0 % a 8,0 %). Ademas, cita reescrita sin cambio de
clase en el 2.935 y el 2.962 (los eslabones de contencion se retiran de la cadena, queda el
fundamento en eslabones de identidad simetrica o en el argumento directo), y marca fuerte
agregada en el 2.942.

### 97.3 `quality` y su vara por tramo (2.901-3.100, ocho tramos)

`quality` **689 pares, ~~125~~ 124 A, ~~18,1~~ 18,0 %** (baja desde ~~21,1~~ 20,7 % al corte
3.000 corregido). **CORRECCION DECLARADA (bucle vuelta 8, TAREA 1.3b/1.2): el "21,1 %" comparaba
contra una cifra muerta (el corte 3.000 sin la correccion del 2.931 arrastrada); el corte 3.000
correcto es 20,7 % (98.2/96.3). Ademas 125 a 124 A por el 2.630 (98.2), anterior a este corte.**

| tramo | pares | A | tasa |
|---|---:|---:|---:|
| 2.901-2.925 | 25 | 1 | 4,0 % |
| 2.926-2.950 | 25 | 2 | 8,0 % |
| 2.951-2.975 | 25 | 2 | 8,0 % |
| 2.976-3.000 | 25 | 0 | 0,0 % |
| 3.001-3.025 | 25 | 1 | 4,0 % |
| 3.026-3.050 | 25 | 0 | 0,0 % |
| 3.051-3.075 | 25 | 1 | 4,0 % |
| 3.076-3.100 | 25 | 0 | 0,0 % |

> El cuerpo se asento en un piso bajo y estable, cuatro tramos entre 0,0 % y 4,0 %, dos en 0,0 %
> exacto. ~~Los tres A del tramo nuevo son casos aislados de lectura directa (contencion o
> REPITE sin cadena), no cumulos nuevos~~ **CORREGIDO (bucle vuelta 8, TAREA 1.3c): son DOS, no
> tres, los A del tramo nuevo (3.001-3.100): 3.012 y 3.064; el 2.917 es de la tanda anterior
> (2.901-3.000) y ya estaba contado ahi. Los dos son casos aislados de lectura directa
> (contencion o REPITE sin cadena), no cumulos nuevos.** No se forzo A para compensar el piso
> ni D para sostener la tendencia.

### 97.4 FAMILIAS Y FIGURAS AL DIA

| que | estado (corte 3.100) |
|---|---|
| la **distincion comun/especial POR DERECHO** | un miembro nuevo por contencion directa (3.012, `trampa_del_promedio_como_estandar`); dos D verificados contra el mismo hub (3.057, 3.094) |
| **fusion mutua** | sin caso nuevo en 3.001-3.100. ~~contador sigue en DIECINUEVE~~ **CORREGIDO (bucle vuelta 8, 98.1): el contador DIECINUEVE no calzaba (el 2.630 no es mutua y faltaban ocho casos entre el 2.673 y el 2.891). El recuento completo y renumerado (VEINTISEIS) vive en 98.1** |
| **ficha nombrada dentro del paso de otro nodo** | **seis casos nuevos** (3.003, 3.029, 3.053, 3.060, 3.088, 3.099); doce acumulados desde el 2.956 |
| **planificar contra ejecutar** | figura nueva reconocida (3.080, con precedente en el 2.815 de la vuelta 5): disenar el evento no es realizar el evento, entregables de distinta naturaleza |
| **especializaciones del mismo hub no fusionan entre si** | confirmada con un caso nuevo (3.087, `analisis_pareto_de_proveedores` contra `principio_pareto`), forma espejo del 2.916/2.931 |
| **programa contra proyecto/etapa** | dos casos nuevos (3.098, y ya contados 3.003, 3.009); tres acumulados |
| **hallazgo de metodo** | la mayoria de los veredictos "REPITE" del archivo usan lenguaje de contencion ("trae de mas", "esta(n) dentro de"), no de identidad simetrica, y por la regla de la cita (TAREA 1.2) no son citables para transitividad nueva; traido como pregunta al acta, no como doctrina nueva |

### 97.5 DISCUTIBLES MARCADOS (conjunto fuerte de la tanda: 10 de 100, 10 %)

El conjunto fuerte del archivo y la tabla de discutibles del reporte son el mismo conjunto,
como manda la TAREA 1.4c. Las siete A de 2.901-3.100 llevan las siete marca fuerte. Detalle
completo con el filo de cada discutible en `docs/loop/REPORTE.md`.

### 97.6 COMMITS

`f040633d` (TAREA 1: correccion 2.931, citas 2.935/2.962, marca fuerte 2.942), `fa26c8cf`
(cribado 3.001-3.025), `0e387021` (cribado 3.026-3.050), `4317c067` (cribado 3.051-3.075),
`f0c54577` (cribado 3.076-3.100, checkpoint 3.100, hash final de la vuelta).

---

## 98. CHECKPOINT 3.200: el recuento del contador de fusiones mutuas, el 2.630 a D, tres cifras corregidas

**Apendice compacto (bucle vuelta 8, 13 ago 2026, corte 3.200).** La prosa vive en
`docs/loop/REPORTE.md` en git; esta seccion fija cifras y commits.

### 98.1 RECUENTO DEL CONTADOR DE FUSIONES MUTUAS (TAREA 1.1, acta vuelta 7)

**El contador publicado (DIECINUEVE) no calzaba con el archivo. Recontado entero sobre las
3.100 razones, con el criterio adjudicado en el acta vuelta 7: cuenta como caso nuevo de la
figura el par que (a) es A y declara por sus propias palabras el mismo acto SIN DOMINANCIA
(cada uno anade lineas, ninguno domina), y (b) no es reformulacion transitiva de una fusion ya
contada (al menos uno de sus dos nodos no habia sido fundido todavia hacia el mismo cumulo).**

**METODO.** Barrido con `grep` de "mutua" (57 apariciones, cualquier clase) y de "ninguno
domina"/"dos sentidos"/"sin dominancia" (33 apariciones en clase A) sobre el archivo entero;
cada hit en clase A se leyo entero y se resolvio con el criterio, citando la frase; los hits en
clase D o los que citan una fusion AJENA como antecedente (no la propia) se descartaron sin
contarlos. **Limite declarado de este metodo, para que no se lea como censo:** el propio 2.127
(primer caso de la serie, ya verificado en vueltas anteriores) no contiene ni "mutua" ni
"ninguno domina" en su razon, así que un barrido por palabra clave no es prueba exhaustiva de
ausencia; una re-derivación completa leyendo los 579 veredictos A uno por uno no se hizo esta
vuelta, por proporcion con el resto del encargo. Esta vuelta corrige el delta especifico que el
acta trajo (el 2.630 y los ocho candidatos entre el 2.673 y el 2.891) mas una verificacion
amplia de palabra clave que no encontro ningun otro caso perdido; no es una garantia de que no
quede alguno sin la palabra clave en algun punto del archivo anterior al 2.127. Se deja como
PENDIENTE DE MEDICION, no de doctrina, para quien retome el barrido con mas presupuesto.

**LOS OCHO CANDIDATOS DEL ACTA, verificados uno por uno con cita y con barrido de toques
previos (ninguno de los ocho toca un nodo ya fundido en un cumulo contado: los unicos toques
previos de sus nodos, cuando los hay, son D):**

| puesto | par | cita que prueba (a) sin dominancia |
|---:|---|---|
| 2.673 | `identificar_clientes_diseno` =A= `identificar_clientes_externos_e_internos` | "Cada uno trae una linea propia" (el propio cuerpo de la razon, antes de nombrar superviviente por elegir) |
| 2.760 | `gobierno_corporativo_juntas_directivas` =A= `planificacion_gobierno_organizaciones_familiares` | "Los pasos calzan uno a uno. A por fusion mutua, superviviente POR ELEGIR" |
| 2.762 | `falacia_recompensa_loteria` =A= `sistemas_recompensa_aleatorios` | "Los actos calzan. A por fusion mutua, superviviente POR ELEGIR" |
| 2.773 | `comparacion_inspectores_independientes` =A= `riesgos_consenso_inspeccion` | "Los pasos calzan. A por fusion mutua, superviviente POR ELEGIR" |
| 2.780 | `revision_progreso` =A= `revision_progreso_breakthrough` | "A por fusion mutua, superviviente POR ELEGIR" |
| 2.787 | `gestion_estrategica_de_calidad_sqm` =A= `rol_tactico_estrategico_oficina` | "Los pasos calzan... A por fusion mutua, superviviente POR ELEGIR" |
| 2.816 | `eliminacion_barreras_orgullo_del_trabajo` =A= `orgullo_por_el_trabajo` | "es el mismo acto, no dos caras. A por fusion mutua" (Punto 12 de Deming, sin superviviente nombrado) |
| 2.825 | `cinco_suposiciones_erroneas_calidad` =A= `concepto_supuestos_erroneos_sobre_calidad` | "es el acto entero compartido... A por fusion mutua, superviviente POR ELEGIR" |

**LAS TRES EXCLUSIONES DEL ACTA, reverificadas y correctas** (2.736, 2.766, 2.800:
reformulaciones transitivas del cumulo del no culpar, ya fundidas por un caso contado antes de
llegar a ellas: fallan la condicion (b)).

**ONCE HITS MAS DEL BARRIDO AMPLIO, verificados y CORRECTAMENTE FUERA los once** (no se cuentan
como fusion mutua; la palabra "mutua" o "dos sentidos" aparece en su razon por otro motivo: un
survivor con dominancia declarada, o la palabra dentro de un paso del propio nodo, no como
figura): 2.253 (REPITE con survivor claro, "mutua" es contenido de un paso del nodo), 2.458
(REPITE con survivor claro, "mutuas" es contenido de un paso), 2.571 (el propio veredicto
declara dominancia y se defiende explicitamente de leerse como mutua: "mi defensa es que
comunicar_politicas cubre mas dimensiones"), 2.577 (survivor claro, "FUSION MUTUA" ahi cita a
OTRO par, el 2.532, como antecedente, no a si mismo), 2.579 (survivor claro, "REPITE. Sobrevive
ciclo_shewhart_pdsa"), 2.601 (survivor claro con dos herramientas contra una), 2.627 (survivor
claro, "el mas completo"), 2.631 (survivor claro, "el de seis pasos"), 2.639 (survivor claro,
"el bucle completo de ocho pasos"), 2.699 (survivor claro, "el mas completo"), 2.853 (A por
transitividad de cumulo hacia el 2.525, ya contado; el propio veredicto dice "no mueve el
contador de mutuas, convencion de la vuelta 3").

**EL 2.630 SALE DE LA SERIE**, corregido a D esta misma vuelta (98.2): declaraba fusion mutua
pero, verificado, es contencion con supervivencia declarada sobre el mismo contenido que su
par gemelo 3.067 (mismo nodo `quality_awareness_crosby`) lee como paso entero propio para dar D.

### LA SERIE COMPLETA, renumerada, VEINTISEIS casos (era diecinueve, con un caso retirado y ocho anadidos)

| # | puesto | par |
|---:|---:|---|
| 1 | 2.127 | `programa_de_referidos_de_franquiciados` =A= `referidos_franquiciados_existentes` (franquicias) |
| 2 | 2.368 | `errores_como_consecuencia` =A= `preguntar_que_no_quien` (health_safety) |
| 3 | 2.417 | `mantener_las_ganancias` =A= `sostener_las_ganancias` |
| 4 | 2.436 | `enfermedades_mortales_gestion` =A= `las_siete_enfermedades_mortales` |
| 5 | 2.480 | `economia_de_la_inspeccion` =A= `regla_todo_o_nada_inspeccion` |
| 6 | 2.484 | `eliminar_slogans_metas` =A= `eliminar_slogans_y_exhortaciones` |
| 7 | 2.498 | `rol_black_belt` =A= `rol_black_belt_six_sigma` |
| 8 | 2.512 | `rol_facilitador_black_belt` =A= `rol_facilitador_equipos_mejora` |
| 9 | 2.516 | `barreras_orgullo_trabajo` =A= `remover_barreras_orgullo_trabajo` |
| 10 | 2.525 | `dia_cero_defectos_2` =A= `dia_cero_defectos_3` |
| 11 | 2.532 | `distincion_causas_comunes_especiales_2` =A= `distincion_causas_especiales_comunes` |
| 12 | 2.552 | `conciencia_calidad` =A= `conciencia_de_calidad_2` |
| 13 | 2.575 | `pocos_vitales_muchos_utiles` =A= `proyectos_vitales_pocos` |
| 14 | 2.597 | `enfasis_en_ganancias_corto_plazo` =A= `enfasis_en_utilidades_corto_plazo` |
| ~~15~~ | ~~2.630~~ | ~~`conciencia_calidad` =A= `quality_awareness_crosby`~~ **RETIRADO, pasa a D (98.2)** |
| 15 | 2.638 | `medicion_calidad` =A= `medicion_calidad_2` |
| 16 | 2.666 | `consumidor_como_eje_de_produccion` =A= `consumidor_parte_linea_produccion` |
| 17 | 2.673 | `identificar_clientes_diseno` =A= `identificar_clientes_externos_e_internos` **(nuevo)** |
| 18 | 2.760 | `gobierno_corporativo_juntas_directivas` =A= `planificacion_gobierno_organizaciones_familiares` **(nuevo)** |
| 19 | 2.762 | `falacia_recompensa_loteria` =A= `sistemas_recompensa_aleatorios` **(nuevo)** |
| 20 | 2.773 | `comparacion_inspectores_independientes` =A= `riesgos_consenso_inspeccion` **(nuevo)** |
| 21 | 2.780 | `revision_progreso` =A= `revision_progreso_breakthrough` **(nuevo)** |
| 22 | 2.787 | `gestion_estrategica_de_calidad_sqm` =A= `rol_tactico_estrategico_oficina` **(nuevo)** |
| 23 | 2.816 | `eliminacion_barreras_orgullo_del_trabajo` =A= `orgullo_por_el_trabajo` **(nuevo)** |
| 24 | 2.825 | `cinco_suposiciones_erroneas_calidad` =A= `concepto_supuestos_erroneos_sobre_calidad` **(nuevo)** |
| 25 | 2.891 | `estadistico_competente_organizacion` =A= `organizacion_liderazgo_estadistico` |
| 26 | 2.952 | `cultura_integridad_objetividad_resolucion_problemas` =A= `manejo_problemas` |
| 27 | 3.182 | `control_del_proceso_del_proveedor` =A= `planificacion_tecnologica_conjunta` **(nuevo, bucle vuelta 8, TAREA 2 del cribado 3.101-3.200)** |

**EL CONTADOR AL CORTE 3.100 ERA VEINTISEIS. AL CORTE 3.200 ES VEINTISIETE**, con el caso nuevo
del 3.182 (tres pasos casi verbatim compartidos entre las dos fichas de plan de control de
proceso del proveedor con SPC, ver el registro del 3.182 en el jsonl). Sin otro caso nuevo entre
el 3.101 y el 3.200. Comando de verificacion: barrido `grep -i "mutua"` mas lectura citada de
cada hit en clase A, reproducible sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.

### 98.2 CORRECCION DECLARADA DEL 2.630 (relectura conjunta, encargada en el acta vuelta 7, TAREA 1.2)

**El par 2.630 (`conciencia_calidad` contra `quality_awareness_crosby`) pasa de `~~A~~` a D.**
El caso del auditor se sostiene, verificado contra el grafo (nodos enteros, no titulos). El
3.067 (`conciencia_de_calidad_2` contra el MISMO `quality_awareness_crosby`) lee los mismos dos
pasos de `quality_awareness_crosby` (registrar y mostrar las mediciones desde el inicio; evitar
amenazas o castigos) como "pasos enteros propios que la campana de reuniones no tiene"; el 2.630
leia esos mismos pasos como "tactica propia del mismo paso" para declarar identidad. No se
puede leer el mismo contenido como paso entero propio en un par y como tactica compartida en el
de al lado. Verificado ademas que `quality_awareness_crosby` es D contra TODOS los demas nodos
que lo tocan en el archivo (2.648, 2.696, 2.789, 2.939, 3.040, 3.067, 3.089, 3.097); el 2.630 es
su UNICA A, sin respaldo estructural. El `entregable_esperado` desempata tambien (TAREA 1.4d):
`conciencia_calidad` entrega un "Programa de comunicacion interna sobre calidad implementado en
todos los niveles, con supervisores capacitados"; `quality_awareness_crosby` entrega un
"Registro inicial de mediciones de calidad que compartes con todo tu equipo como punto de
partida". Artefactos distintos. Leido directo: `conciencia_calidad` trae CUATRO pasos enteros
propios que el otro no tiene (capacitar supervisores sobre el costo real, producir material
visible, incluir a personal administrativo y de servicio, fomentar el habito de hablar de
calidad) y `quality_awareness_crosby` trae los suyos (registrar y mostrar mediciones desde el
inicio, evitar amenazas o castigos, dejar participar activamente). Conjuntos disjuntos.
**CONTRAPESO ESCRITO por el auditor, para que la relectura sea justa:** los dos nodos son el
mismo Paso del programa de Crosby, y el 2.552 (`conciencia_calidad` =A= `conciencia_de_calidad_2`)
NO esta en discusion y no se reabre; la D en el 2.630 no rompe ese cumulo, le quita un miembro
(`quality_awareness_crosby`) y resta una unidad al contador de fusiones mutuas (ver 98.1: la
serie ya se recompuso sin el). Tachado sin borrar en el jsonl; la razon vieja se conserva
entera. **Efecto en el marcador, arrastrado a TODAS las secciones donde aparecia (93, 94, 95, 96,
97), ver cada una:** corte 2.700 de A 544 a 543; corte 2.800 de A 563 a 562; corte 2.900 de A
572 a 571 (segunda correccion sobre la ya aplicada del 2.805); corte 3.000 de A 577 a 576
(segunda correccion sobre la ya aplicada del 2.931); corte 3.100 de A 579 a 578.

### 98.3 MARCADOR (corte 3.200)

| | |
|---|---:|
| **veredictos** | **3.200**, hasta el puesto 3.200, cero huecos ni duplicados |
| **A** | **580** (18,1 %) |
| **B** | 89 |
| **C** | 7 |
| **D** | **2.524** (78,9 %) |

Contra el checkpoint 3.100 corregido (98.2: A 578, D 2.426): **+2 A y +98 D** en el tramo
3.101-3.200 (comando `python scripts/recomputar_marcador.py 3200`).

### 98.4 `quality` y su vara por tramo (3.101-3.200, cuatro tramos)

`quality` **789 pares, 126 A, 16,0 %** (baja desde 18,0 % al corte 3.100 corregido, ver 97.3).

| tramo | pares | A | tasa |
|---|---:|---:|---:|
| 3.101-3.125 | 25 | 0 | 0,0 % |
| 3.126-3.150 | 25 | 0 | 0,0 % |
| 3.151-3.175 | 25 | 1 | 4,0 % |
| 3.176-3.200 | 25 | 1 | 4,0 % |

> El cuerpo sigue en el piso: dos tramos en 0,0 % exacto (el primero desde el 2.976-3.000) y dos
> en 4,0 %. Las dos A del tramo (3.165 contencion, 3.182 fusion mutua nueva) son casos aislados
> de lectura directa, no cumulos nuevos. No se forzo A para compensar el piso ni D para sostener
> la tendencia; cada D trae su comparacion de pasos enteros escrita en la razon.

### 98.5 FAMILIAS Y FIGURAS AL DIA (corte 3.200)

| que | estado (corte 3.200) |
|---|---|
| **fusion mutua** | **UN caso nuevo**, el 3.182 (control_del_proceso_del_proveedor =A= planificacion_tecnologica_conjunta, tres pasos casi verbatim compartidos). El contador pasa de **VEINTISEIS a VEINTISIETE** (ver 98.1 para la serie completa renumerada) |
| **contencion por procedimiento mas completo** | figura nueva reconocida (3.165, evaluacion_organizacional_calidad =A= evaluacion_riesgo_calidad_organizacional): un nodo cabe entero dentro de un procedimiento mas formal del mismo acto, que ademas trae equipo/roles, objetivos, plan de comunicacion y puntaje |
| **la capacidad del proceso, SIN ACTO** | sigue cerrada, extiende con seis pares mas de esta tanda (3.130, 3.141, 3.149, 3.152, 3.200 via indice_cpk, mas la ficha 3.156/3.169/3.197 del patron general), sim_tit hasta 67,4 sin fundir |
| **ficha nombrada dentro del paso de otro nodo** | la figura mas frecuente del checkpoint: nueve casos nuevos (3.103, 3.107, 3.114, 3.118, 3.156, 3.169, 3.175, 3.186, 3.197, 3.200); veintiuno acumulados desde el 2.956 |
| **distincion comun/especial POR DERECHO contra responsabilidad gerencial** | frontera confirmada de nuevo (3.113), PREGUNTA 3 sigue abierta sin resolverse en este tramo |
| **hubs que no funden con sus vecinos pese al sim_tit alto** | tres casos marcados: concepto_haciendo_la_calidad_cierta (D contra siete vecinos distintos en la sesion), gestion_estrategica_de_calidad_sqm (D contra cuatro vecinos), planificacion_calidad_crosby (D contra tres vecinos) |
| **trampa del identificador con sim_tit muy alto** | 3.176 (facilitador contra lider de equipo, sim_tit 76,7, roles distintos del mismo equipo) y 3.165 (sim_tit 75,9, resuelto A por contencion) |
| **breakthrough/RCCA/DMAIC** | frontera confirmada de nuevo (3.139, RCCA carece de Measure independiente) |

### 98.6 DISCUTIBLES MARCADOS (conjunto fuerte de la tanda)

El conjunto fuerte de esta tanda son los pares con marca fuerte inline: **3.121** (estructura de
reporte dual contra organizacion de liderazgo estadistico, D pese al nucleo compartido con el
cumulo del 2.891), **3.147** (concepto_haciendo_la_calidad_cierta contra concepto_quality_is_free,
con arista), **3.148** (dia_cero_defectos contra zero_defects_concepto, entregables parecidos),
**3.165** (A por contencion, sim_tit 75,9, el mas alto del checkpoint), **3.173** (los dos
autocontrol de Juran, checklist parecido pero especializaciones distintas), **3.176** (facilitador
contra lider, sim_tit 76,7, trampa del identificador), **3.182** (A por fusion mutua nueva, tres
pasos casi verbatim). Detalle completo de cada uno en `docs/loop/REPORTE.md`.

### 98.7 COMMITS

`9c7eab96` (TAREA 1: recuento del contador de fusiones mutuas, correccion del 2.630, tres cifras
publicadas corregidas, cribado 3.101-3.125), `5603ee40` (cribado 3.126-3.155), `b703adcc`
(cribado 3.156-3.170), `53782609` (cribado 3.171-3.185), `18f1d09b` (cribado 3.186-3.200,
checkpoint 3.200, hash final de la vuelta antes del reporte).

---

