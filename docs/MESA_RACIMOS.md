# La mesa de racimos

**Documento de decision, no de hallazgo.** Todo lo que aqui se cita ya esta
medido y escrito en `docs/FRANJA_INFORME.md` (apartado 4) y en
`docs/FICHA_SUBFUSION_GRADIENTE.md`. Esta mesa no aporta hallazgos nuevos: los
ordena para que el fundador pueda decidir **cuatro veces** en vez de treinta y
dos.

**Ningun nodo se toca desde este documento.**

---

## 1. Que es esta mesa

Es la **adjudicacion de los 32 racimos**, y es el **insumo del plan de la pasada
unica**. Sin estas cuatro decisiones, la pasada unica tendria que decidir nodo
por nodo mientras edita, que es exactamente como se produjo el problema que viene
a arreglar.

**De donde salen los 32:**

| origen | cuantos | donde esta medido |
|---|---:|---|
| **Censo del cribado de la franja** | **30** | `FRANJA_INFORME.md`, apartado 4.1 |
| **Destapados por la muestra D** | **2** | `FRANJA_INFORME.md`, apartado 10.1, verificaciones 1 y 2 |
| | **32** | |

Los dos de la muestra **no estan en la tabla del apartado 4.1 y no se van a
meter ahi**: ese censo es el cierre de lo que vio el cribado, y el cribado no
podia verlos porque son de un mundo contra si mismo mientras la franja solo
miraba mundo contra nucleo. Se suman aqui, que es donde se decide.

**Las NOMINAS de los 32 estan escritas** en `docs/RACIMOS_MIEMBROS.jsonl`, una
linea por racimo, con el id de cada miembro y **el veredicto del cribado de donde
salio**. Se reconstruyeron de las razones de `docs/FRANJA_VEREDICTOS.jsonl`, y
**las 32 cuadran con su tamano censado**: 171 miembros en total.

> **Un hallazgo del censo de nominas, y toca a la cuenta de 32.** Dos racimos se
> solapan y uno **contiene** al otro: **Obtencion de compromiso** (3) es un
> subconjunto exacto de **El avance y el compromiso en la venta** (5). Los tres
> nodos `obtencion_de_compromiso`, `obtencion_compromiso_venta` y
> `obtencion_compromiso` estan en los dos.
>
> **Por eso los 32 racimos tienen 171 miembros pero solo 168 nodos distintos.**
> No cambio la cuenta de 32 por mi cuenta: **la decision 2 los va a leer par a
> par de todos modos**, y con la nomina delante el solape se resuelve en la
> lectura. Queda anotado para que nadie lo cuente dos veces al planificar.

**La forma de la mesa.** Los 32 se reparten en **cuatro grupos, y cada grupo
cuelga de UNA decision estructural.** Cada racimo esta en exactamente un grupo.
Los tres primeros grupos consumen los 32; **el cuarto no consume racimos: cruza
por encima de todos**, porque es una familia de ids, no de doctrina.

| grupo | de que va | racimos | la decision |
|---|---|---:|---|
| **1** | Los programas desmontados en piezas | **6** | serie declarada contra disolucion tematica |
| **2** | La doctrina-columna de un mundo | **13** | sin cuota contra cuota por doctrina |
| **3** | Los racimos del nucleo | **13** | entran enteros contra tolerarlos |
| **4** | La familia de ids | **cruza todos** | familia unica contra caso por caso |

---

## 2. GRUPO 1: los programas desmontados

**El patron.** Un programa de un autor entro al catalogo **dos veces a la vez**:
como nodo que lo describe entero, **y** como una coleccion de nodos sueltos, uno
por paso, con el numero puesto en el titulo. Y en el camino, varios pasos
entraron dos veces.

**Los racimos de este grupo:**

| racimo | mundo | nodos | de que programa |
|---|---|---:|---|
| Accion correctiva | quality | **7** | Crosby |
| Los puntos de Deming en el titulo | quality | **7** | Deming |
| Eliminacion de causas de error | quality | **3** | Crosby |
| Consejo de calidad | quality | **3** | Crosby |
| Metas de calidad | quality | **3** | Crosby |
| Programa de catorce pasos de Crosby | quality | **3** | Crosby, los que lo describen entero |

**Los siete pasos duplicados de Crosby**, con sus pares (apartado 4.2 del
informe):

| Paso | Los dos nodos |
|---|---|
| Paso 3 | `medicion_calidad` y `medicion_calidad_2` |
| Paso 4 | `costo_de_calidad_2` y `costo_de_calidad_3` |
| Paso 6 | `accion_correctiva_4` y `accion_correctiva_sistematica` |
| Paso 10 | `establecimiento_metas` y `fijacion_de_metas` |
| Paso 11 | `eliminacion_causas_error` y `eliminacion_causas_error_2` |
| Paso 12 | `reconocimiento` y `reconocimiento_al_desempeno` |
| Paso 14 | `reinicio_programa_calidad` y `repeticion_programa` |

> **Aviso de cifra**, para que la mesa no decida sobre un numero viejo: **hasta
> la preparacion de esta mesa el informe decia CINCO.** Al volver a medir los
> titulos contra el grafo salieron **siete**: el Paso 4 y el Paso 12 no estaban
> contados. Los dos van verificados en el apartado 4.2, y la correccion esta
> declarada en la seccion 6 del informe. **Si el auditor quiere el conteo
> anterior, la evidencia esta escrita para discutirla; no la escondi ni la
> cambie en silencio.**

**Y un caso que mide igual sin serlo**: el **Paso 7** tambien tiene dos nodos
(`comite_cero_defectos` y `planificacion_cero_defectos`) **pero dicen cosas
distintas**, uno arma el grupo de apoyo y el otro planifica el lanzamiento.
**Mismo numero, distinto contenido.** No entra como duplicado.

**Los siete puntos de Deming en el titulo** (apartado 10.1, verificacion 1):
puntos **5, 6, 7, 8, 10, 13 y 14**, en `mejora_continua_del_sistema`,
`institucionalizar_capacitacion`, `adopcion_liderazgo`, `eliminar_miedo`,
`eliminar_slogans_metas`, `fomento_educacion_autoeducacion` y
`plan_de_accion_transformacion`.

### DECISION 1

**La pregunta:** cuando un programa de un autor entra al catalogo, entra **como
serie o como temas sueltos**?

| opcion | que significa | que cuesta |
|---|---|---|
| **A. Serie declarada** *(recomendacion del auditor)* | **Un nodo-programa unico** que presenta la serie entera, **un nodo por paso** colgando de el, y **el numero en el titulo pasa a ser legitimo** porque el nodo-programa lo explica | hay que escribir el nodo-programa y fusionar los duplicados de cada paso |
| **B. Disolucion tematica** | Los pasos se reparten por tema y **el numero desaparece de todos los titulos** | se pierde la secuencia del autor, que en Crosby es parte del metodo |

**Por que la recomendacion es A.** El numero en el titulo hoy es ruido **porque
no hay donde consultarlo**: un lector que recibe *Paso 11* no tiene el mapa. Con
el nodo-programa delante, el numero deja de ser ruido y pasa a ser una
coordenada. **La opcion B arregla el sintoma quitando informacion que el autor si
tenia.**

**Lo que la decision 1 arrastra:** los siete duplicados se fusionan como parte de
la ejecucion, sea cual sea la opcion. **Esa parte no esta en discusion**, solo el
marco.

**Adjudicaciones parciales que ya existen dentro de este grupo:**

- **El trio ECR** (`eliminacion_causas_error`, `eliminacion_causas_error_2` y su
  hermano): **LEIDO Y ADJUDICADO** en la ficha, fusion doble, **pendiente solo
  del disparo del fundador**.
- **El caso 5, el metodo COC escrito dos veces** en `quality`: leido en la ficha.
- **Los gemelos del Paso 3**: leidos en la ficha, apartado de pares calcados
  dentro de un mundo.
- **`costo_de_calidad`**: la ficha lo tiene marcado **sin leer**. Con el Paso 4
  ahora contado como duplicado, **este es el hueco vivo de este grupo**.

**VISTO DEL FUNDADOR: APROBADA, 9 ago 2026.** Se ejecuta la recomendacion del auditor.

#### AMPLIACION (11 ago 2026): el contraejemplo del alias ya no es solo un alias

**Viene del puesto 1955 del cribado intra y de la relectura R41 del auditor.** El
mismo par que esta decision usa como contraejemplo, `nafta_free_trade_agreements`,
**salio A en el cribado contra `certificado_de_origen_tratados_libre_comercio`**:
los cinco pasos se corresponden.

**Eso junta TRES encargos sobre los mismos dos nodos:**

| encargo | de donde viene |
|---|---|
| **fusion**, con cinco perdidas a reponer | cribado intra, puesto 1955 |
| **reparacion de vigencia** del id y el titulo | barrido de marco, ordenes 1 y 2 de su lista |
| **alias** para no romper dos aristas | **esta decision** |

> **Por el TOQUE UNICO del banco 9.4 los tres van en UN SOLO ACTO.** Y hay una
> alineacion medida: **el id que la vigencia manda matar es el que la fusion puede
> matar.** Si la fusion va **hacia** `certificado_de_origen_tratados_libre_comercio`,
> el mismo acto cierra los tres. **La direccion de la fusion deja de ser libre: una
> cierra los tres encargos y la otra deja dos abiertos.**

**Queda para la mesa, sin adjudicar aqui.** Detalle y verificacion en
`PENDIENTES.md`, ficha `vigencia-del-marco-internacional`, y en el informe 69.2.

---

## 3. GRUPO 2: la doctrina-columna de mundo

**El patron.** Un mundo tiene **una doctrina que lo sostiene**, y esa doctrina
esta escrita en muchos nodos a la vez. **No es lo mismo que el grupo 1**: aqui no
hay un programa numerado desmontado, hay una conviccion repetida.

**Los racimos de este grupo, trece:**

| racimo | mundo | nodos |
|---|---|---:|
| **No culpar a la persona, arreglar el sistema** | health_safety | **20** |
| **Causas comunes y responsabilidad del sistema** | quality | **12** |
| **La estructura de cinturones de Six Sigma** | quality | **9** |
| Auditoria de calidad | quality | **6** |
| Benchmarking | quality | **5** |
| Ciclo de mejora PDCA / PDSA | quality | **4** |
| Clasificacion de defectos | quality | **4** |
| Analisis de causa raiz | quality | **4** |
| Fitness for purpose | quality | **3** |
| Costo de calidad | quality | **3** |
| Plan y matriz de control | quality | **3** |
| Poka yoke | quality | **3** |
| Diversidad en el diseno | environmental | **3** |

**Los tres grandes son la columna de su mundo.** Veinte nodos de health_safety
predicando *no culpes a la persona* no son un descuido: **es la doctrina central
de ese mundo dicha veinte veces.** Y esa es justo la razon por la que la decision
no puede ser una cuota.

> **Nota sobre `costo_de_calidad`**, para que la mesa lo sepa antes de decidir:
> este racimo **tiene dentro dos nodos del Paso 4 de Crosby**
> (`costo_de_calidad_2` y `costo_de_calidad_3`), asi que **la decision 1 va a
> meter mano aqui tambien**. Lo dejo en el grupo 2 porque es donde lo pone el
> informe, **y aviso del cruce en vez de moverlo por mi cuenta.**

### DECISION 2

**La pregunta:** como se poda una doctrina sin descabezar el mundo que la
sostiene?

| opcion | que significa | que cuesta |
|---|---|---|
| **A. Sin cuota, par a par** *(recomendacion del auditor)* | Dentro del racimo se lee **par a par** con el criterio **continua o repite**: si el segundo nodo **continua** al primero (otro momento, otro nivel, otro angulo), los dos viven; si **repite**, se fusiona | es lectura, y de la lenta: veinte nodos son diecinueve comparaciones |
| **B. Cuota por doctrina** | Se fija un techo (por ejemplo tres nodos por doctrina) y se poda hasta llegar | rapido, y **arbitrario**: la cuota no sabe cual de los veinte es el que continua |

**Por que la recomendacion es A.** La cuota trata el tamano como el problema, y
**el tamano no es el problema**: veinte nodos que dicen lo mismo son un problema,
veinte nodos que construyen una doctrina desde veinte angulos son un mundo bien
servido. **Solo la lectura par a par distingue una cosa de la otra**, y es la
misma prueba que el gradiente ya usa entre mundo y nucleo.

**Adjudicaciones parciales que ya existen dentro de este grupo:**

- **La maraña de causas comunes**: su nodo base ya tiene **fusion con reparto
  adjudicada** en la ficha, y **puede absorber parte del racimo antes de que el
  barrido llegue**. La ficha avisa de mirarlos juntos, no en dos momentos.
- **El caso 6, el racimo de auditoria** de `quality`: leido en la ficha.
- **El sexto nodo del racimo de la culpa**
  (`responsabilidad_personal_en_gestion`): **candidato a frontera**, no a poda.
  Es de Crosby y los otros cinco de Deming. **La decision 2 no lo puede tratar
  como repeticion.**
- **Los cinturones** llegan sin leer: es el racimo mas nuevo de la mesa.

**VISTO DEL FUNDADOR: APROBADA, 9 ago 2026.** Se ejecuta la recomendacion del auditor.

---

## 4. GRUPO 3: los trece racimos del nucleo

**El patron, y es el que mas usuario toca.** Estos racimos **no estan en un mundo
de pago: estan en el catalogo que se entrega gratis**, que es el que todo lector
recibe.

| racimo | donde | nodos |
|---|---|---:|
| Cradle to cradle | environmental **y nucleo** | **11** |
| Portafolio: revisar, podar, reasignar | **nucleo** | **7** |
| Customer discovery: salir a hablar con el cliente | **nucleo** | **7** |
| Los cinco porques | **nucleo** | **5** |
| Pivotar o proceder | **nucleo** | **5** |
| El avance y el compromiso en la venta | **nucleo** | **5** |
| Encuadre del problema (How Might We) | **nucleo** | **5** |
| Mapeo del flujo de valor | quality, environmental **y nucleo** | **5** |
| Las reglas del brainstorming | **nucleo** (3) y quality (1) | **4** |
| El efectivo contra la ganancia | **nucleo** | **3** |
| La etapa de investigacion en la venta | **nucleo** | **3** |
| Estrategia de innovacion de producto | **nucleo** | **3** |
| Obtencion de compromiso | **nucleo** | **3** |

**Diez son enteramente del nucleo. Tres son mixtos** (cradle to cradle, mapeo del
flujo de valor y las reglas del brainstorming), y por eso su poda tiene que
mirar los dos lados a la vez: **podar el lado del nucleo de un racimo mixto
cambia el gradiente del mundo que lo acompana.**

### DECISION 3

**La pregunta:** los racimos del nucleo entran a la pasada unica o se toleran?

| opcion | que significa | que cuesta |
|---|---|---|
| **A. Entran enteros, con prioridad UX** *(recomendacion del auditor)* | Los trece van a la pasada unica, **y van primero**, antes que los racimos de mundo | es el tramo mas caro de la pasada |
| **B. Tolerarlos** | Se arreglan los mundos y el nucleo se deja para despues | barato ahora, y **el costo lo paga el lector**, no el catalogo |

**Por que la recomendacion es A, y la razon esta medida.** Es **el patron de
centralidad** de la ficha: **los nodos que mas se sirven al usuario son los peores
servidos**, porque son los que todas las fuentes tocan y por tanto los que mas
fusiones recibieron. **Un lector que pide su MVP, su Canvas o su prueba A/B
recibe hoy veintidos, diecisiete o quince pasos donde caben cinco.** No es deuda
de catalogo: **es lo que la gente lee.**

> **Y el patron tiene contraejemplo, que es lo que impide leerlo como condena**:
> `nucleo/decision_intensidad_capital` acumula **veintitres emparejamientos entre
> las dos colas sin una sola mala**. **Un nodo base muy citado no tiene por que
> acabar acrecionado**: el defecto es de como se fusiono, no de cuanto se usa.
> **Eso es lo que hace que la decision 3 sea arreglable y no una condena
> estructural.**

**Adjudicaciones parciales que ya existen dentro de este grupo:**

- **Los pares calcados del nucleo** ya leidos en la ficha: el par de scorecards
  (cuarto calcado del nucleo), el par de ROI con su consecuencia para el
  destejido, el racimo de sucesion, el par de innovacion abierta y los dos nodos
  de A/B testing.
- **`brainstorming_divergente`**: el trio de brainstorming esta **confirmado** en
  la ficha como caso 2.
- **Cradle to cradle**: la **cirugia 1B** ya reencuadro
  `cradle_to_cradle_concepto` como puerta del tema, y **la cola lo verifico sola
  despues**. Hay precedente de que este racimo se arregla bien.

**VISTO DEL FUNDADOR: APROBADA, 9 ago 2026.** Se ejecuta la recomendacion del auditor.

---

## 5. GRUPO 4: la familia de ids

**No consume racimos: cruza por encima de los tres grupos anteriores.** Es la
unica parte de la mesa que **no habla de doctrina sino de nombres**, y por eso
puede ejecutarse con un criterio propio.

| figura | cuantos | donde esta medido |
|---|---:|---|
| **Sufijo `_N` vivo en el id** | **30 nodos** | informe, apartado 4.3 |
| **Pares base mas `_2` con contenido calcado** | **9 pares** | informe, apartado 4.3 |
| **Ids casi identicos** (una letra, un articulo, palabras permutadas) | **19 pares** | informe, apartado 4.4 |

**Los nueve pares base mas `_2`:** `sistema_responsabilidad_gerencial`,
`clasificacion_de_seriedad_de_defectos`, `eco_efectividad`,
`equipo_mejora_calidad`, `planificacion_estrategica_despliegue`,
`establecer_vision_organizacional`, `contacto_con_el_cliente`, `ciclo_de_culpa` y
`triple_bottom_line`, cada uno con su `_2`.

**Dos casos especiales que no se pueden tratar como el resto:**

1. **La transdominio (franja 1603)**:
   `exportacion/seleccion_canales_distribucion` contra
   `seleccion_canal_distribucion` **del nucleo**. **El contenido es sano**: el
   mundo especializa a comercio internacional sobre la base lean del nucleo.
   **Lo que hay que arreglar es el nombre, no el nodo**, y por eso es **caso de
   renombre o de alias, no de fusion**: aqui un lector puede cruzar sin darse
   cuenta la linea entre lo gratis y lo pago.
2. **`proteccion_propiedad_intelectual_2`** vive en `exportacion` y
   `proteccion_propiedad_intelectual` vive en el **nucleo**. **El `_2` no
   distingue a dos hermanos del mismo mundo: choca con el id de un nodo del
   catalogo gratis.** Misma clase que el anterior.

### DECISION 4

**La pregunta:** los ids se arreglan como familia o caso por caso?

| opcion | que significa | que cuesta |
|---|---|---|
| **A. Familia unica** *(recomendacion del auditor)* | Las tres figuras se ejecutan **de una vez**, con el criterio **continua o repite** para decidir fusion, y **fusion con alias** para que ningun id viejo quede muerto | hay que hacer el pase de alias completo y verificarlo |
| **B. Caso por caso** | Cada id se arregla cuando su racimo llegue a la pasada | **los ids quedan repartidos entre las tres decisiones anteriores** y nadie ve la familia entera |

**Por que la recomendacion es A.** Un id no pertenece a una doctrina: pertenece
al catalogo. **Repartir la familia entre los otros tres grupos es la forma segura
de que dos racimos distintos resuelvan el mismo choque de nombres de dos maneras
distintas.** Y el alias no es opcional: **un id que muere sin alias rompe todo lo
que apuntaba a el.**

> **La transdominio y el `_2` de propiedad intelectual salen del criterio general
> y van por renombre o alias**, porque en los dos el contenido esta sano. **Fusionar
> ahi seria arreglar un nombre borrando un nodo bueno de pago.**

> **CONTRAEJEMPLO CONCRETO DEL ALIAS, medido el 11 ago 2026 y anotado aqui porque
> es la prueba de la frase de arriba.** La decision dice que *un id que muere sin
> alias rompe todo lo que apuntaba a el*. **Eso ya no es una advertencia teorica:
> tiene dos aristas con nombre.**
>
> **`nafta_free_trade_agreements` es candidato a renombre** porque lleva en el id
> un tratado extinto desde el 1 de julio de 2020. **Y DOS nodos vivos apuntan a
> ese id por arista**: `foreign_trade_zones` lo tiene en sus `nodos_previos` e
> `import_regulations_foreign_governments` en sus `nodos_siguientes`.
>
> **Si ese renombre se hace sin alias, esas dos aristas quedan apuntando a un id
> que ya no existe.** Verificado contra el grafo. **Es el ejemplar mas barato de
> ensenar por que la clausula del alias no era opcional.**

**VISTO DEL FUNDADOR: APROBADA, 9 ago 2026.** Se ejecuta la recomendacion del auditor.

---

## 6. El visto del fundador, y la clausula que lo acompana

**Las cuatro decisiones quedan APROBADAS el 9 de agosto de 2026**, las cuatro por
la recomendacion del auditor:

| decision | que queda aprobado |
|---:|---|
| **1** | **serie declarada**: nodo-programa unico, un nodo por paso, y el numero en el titulo pasa a ser legitimo |
| **2** | **sin cuota**: continua o repite, par a par dentro del racimo |
| **3** | **entran enteros** a la pasada unica, con **prioridad UX** |
| **4** | **familia unica** de ids, con continua o repite y **fusion con alias** |

### La clausula general

> **Lo demas pendiente se ejecuta DESPUES de solventar esto**, salvo lo que haga
> falta **adelantar para sellar un hueco**.

**Lo que la clausula permite y lo que no**, escrito para que no se estire:

- **Permite adelantar** un trabajo pendiente cuando **sin el quedaria un hueco
  abierto** en lo que se esta ejecutando. Sellar un hueco es la unica excusa.
- **No permite** empezar un frente nuevo porque venga a mano ni porque sea
  barato. El orden es el orden.
- **Cuando algo se adelante, se escribe que hueco venia a sellar.** Sin esa
  linea, un adelanto es indistinguible de un desvio.

### Estado de la mesa

**CERRADA como insumo del plan de la pasada unica.** Las cuatro decisiones
estructurales estan tomadas; **lo que sigue no es decidir, es planificar la
ejecucion** con estas cuatro como marco.

---

## 7. Lo que esta mesa NO decide

Para que quede claro que sigue abierto y por que no esta aqui:

- **Las 106 citas de costura que quedan por leer.** Frente paralelo, en tandas
  del auditor. **No se bloquea con esta mesa y esta mesa no se bloquea con el.**
- **La hipotesis de la asimetria de las costuras** (21 de 21 en el nucleo, y si
  es efecto del tamano de los nodos). Se comprueba en el barrido, no aqui.
- **Las dos fronteras candidatas** (F303 y el sexto de la culpa). **No son poda:
  son contexto que hay que escribir**, y por eso no cuelgan de ninguna de las
  cuatro decisiones.
- **El caso a escala de mundo de `seguridad_digital`** (20 de 55 nodos con marco
  federal estadounidense). Vive en su propia ficha de `docs/PENDIENTES.md`, con
  su remedio candidato **provisional**.
