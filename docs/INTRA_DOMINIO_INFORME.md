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
