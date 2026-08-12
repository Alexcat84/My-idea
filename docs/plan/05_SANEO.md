# FASE 05: EL SANEO

**Nombres, versiones, direcciones y claves.** Casi nada de esta fase toca la
doctrina de un nodo, y por eso es la mas barata de todos los frentes abiertos.
**La excepcion es la primera operacion, que es una fusion.**

**Operaciones: `OP-S-01` a `OP-S-10`. Una LISTA, nueve DECISION PENDIENTE.**

---

## EL TOQUE UNICO, marcado donde toca

> **Banco 9.4: un nodo se abre UNA VEZ.** Donde un nodo tiene encima un saneo **y
> ademas** una fusion o un destejido, **los dos van en el mismo acto**. Hacerlos
> por separado significa **reparar la vigencia de un nodo que la fusion va a
> borrar despues.**

| operacion | toque unico con | por que |
|---|---|---|
| **`OP-S-01`** | **fusion del puesto 1955 + vigencia + alias de la DECISION 4** | **tres encargos sobre los mismos dos nodos** |
| **`OP-S-04`** | **fusion de `analisis_trafico_competitivo` con su gemelo generico** | fundir hacia el generico **borra cinco verificaciones de vigencia de una vez** |

---

## `OP-S-01`: EL PAR DE NAFTA: fusion, vigencia y alias en UN SOLO ACTO

**Nodos**: `nafta_free_trade_agreements` y
`certificado_de_origen_tratados_libre_comercio`.

**TRES ENCARGOS CAEN SOBRE LOS MISMOS DOS NODOS:**

| encargo | de donde viene | que manda |
|---|---|---|
| **fusion** | cribado intra, **puesto 1955**, clase A | los cinco pasos se corresponden: fundir, reponiendo cinco perdidas |
| **vigencia** | barrido de marco, **ordenes 1 y 2** de su lista | quitar de id y titulo un tratado **extinto desde el 1 de julio de 2020** |
| **alias** | **DECISION 4** de la mesa, aprobada el 9 ago 2026 | el id que muera lleva alias, o rompe lo que apuntaba a el |

**SUPERVIVIENTE PROPUESTO** (por medicion, **no adjudicado**):
`certificado_de_origen_tratados_libre_comercio`.

> **La direccion de la fusion deja de ser libre.** El id que la vigencia manda
> matar **es el que la fusion puede matar**. Si la fusion va **hacia**
> `certificado_de_origen_tratados_libre_comercio`, **el mismo acto cierra los tres
> encargos**. Si va al reves, quedan dos abiertos.

**QUE SE PRESERVA, repartido por lado:**

| de | que |
|---|---|
| `certificado_de_origen_tratados_libre_comercio` | la regla de **obtenido en su totalidad**, la tercera via de calificacion |
| `certificado_de_origen_tratados_libre_comercio` | conservar la documentacion **por el periodo que exija la aduana**, la unica linea del par con obligacion **posterior al embarque** |
| `nafta_free_trade_agreements` | las **cuatro reglas del articulo 401** |
| `nafta_free_trade_agreements` | los **dos porcentajes**: 60% por metodo de transaccion y 50% por costo neto |
| `nafta_free_trade_agreements` | los **nombres de los formularios** (CF 434, Form B-232), sin los cuales *completar el certificado* no dice que papel llenar |

**LAS DOS ARISTAS QUE EL ALIAS PROTEGE, verificadas contra el grafo el 11 ago 2026:**

- `foreign_trade_zones` lleva `nafta_free_trade_agreements` en sus `nodos_previos`
- `import_regulations_foreign_governments` lo lleva en sus `nodos_siguientes`
- **hoy NINGUNO de los dos nodos del par tiene `ids_alias`**

**DEPENDE DE `OP-S-08`**: sin resolutor, el alias **no protege esas dos aristas,
solo las documenta**.

**LA PREGUNTA**: se confirma la direccion de la fusion?

---

## `OP-S-02`: INCOTERMS SIN VERSION · **PARADA ABIERTA**

**Nodos que lo CITAN en su texto, medidos el 11 ago 2026**:
`incoterms_reglas_comerciales_internacionales`, `seguro_de_carga_transporte`,
`terminos_de_venta_incoterms`. **Los tres de `exportacion`. Los tres sin ano.**

> **CIFRA PUBLICADA QUE NO RECONCILIA.** La tabla de `PENDIENTES.md`, seccion
> *ADJUDICADO PARA EL PLAN (11 ago 2026)*, que dice **"Recontado del grafo, sobre
> nodos VIVOS"**, publica **12**. Medido hoy: **3**.

| donde aparece la palabra Incoterms | nodos |
|---|---:|
| **en el TEXTO** (las cinco casas), vivos | **3** |
| en el texto, pero deprecados | 2 |
| **solo en el id, en un alias, en una ARISTA o en `merged_originals`** | **11**, de ellos 9 vivos |

> **3 vivos que lo citan + 9 vivos que solo lo apuntan = 12.** Ese es el 12
> publicado. **Y es el mismo error que esa misma adjudicacion habia corregido para
> NAFTA tres parrafos mas arriba**: *apuntar al nodo no es citar el tratado, y
> mezclarlos infla la cifra.* **Se corrigio la fila de NAFTA y no la de al lado.**

**LAS OTRAS DOS FILAS DE LA MISMA TABLA CUADRAN EXACTAS**: NAFTA da **6** y
`export.gov` da **3**.

**LA CIFRA NO SE HA TOCADO.** Lo que la medicion deja listo por si el auditor
adjudica: la **union real** de las tres averias es de **12 nodos, con solape
CERO**, y **los 12 de 12 siguen siendo de `exportacion`**, que era el argumento de
la adjudicacion. **El argumento sobrevive entero: solo cambia el tamano.**

**LA PREGUNTA**: se confirma que la fila contaba aristas como citas? Y que ano se
escribe, **Incoterms 2020**?

---

## `OP-S-03`: `export.gov` A `trade.gov` · **LISTA**

**Nodos**: `calculo_de_aranceles_importacion`,
`evaluacion_preparacion_empresa_exportar`, `reglas_de_origen_fta_2`.

**Solo pide cambiar el dominio.** No toca la doctrina de ningun nodo: **es la mas
barata de las tres averias de vigencia.**

> **ATENCION AL RECUENTO: son 3 nodos y CUATRO menciones**, porque
> `calculo_de_aranceles_importacion` lo nombra **dos veces**. La correccion 1 de la
> adjudicacion ya lo advertia, y es facil dejarse una.

> **DATO NUEVO del 11 ago 2026, y le sirve a esta operacion**: `stopfakes.gov` lo
> opera **la misma International Trade Administration** que opera `trade.gov`, o
> sea el organismo que absorbio `export.gov`. **Los tres portales de la lista
> cuelgan del mismo sitio**, asi que probablemente se muevan juntos la proxima vez.

---

## `OP-S-04`: LAS SEIS HERRAMIENTAS MUERTAS

**El mapa completo, verificado contra el grafo el 11 ago 2026:**

| herramienta | estado | donde vive |
|---|---|---|
| **Alexa** | MUERTA, Amazon la cerro | `analisis_trafico_competitivo` (pasos 1 y 6), `capturar_conocimiento_de_mercado`, `medicion_resultados_marketing_franquicia` |
| **Compete** | RETIRADA | `analisis_trafico_competitivo` (paso 1), `capturar_conocimiento_de_mercado` |
| **Perfect Audience** | MUERTA, descontinuada tras Marin 2014 y SharpSpring 2019 | `retargeting_display`, **paso 1, entre los pixeles a instalar** |
| **The Deck** | MUERTA, **cerro en marzo de 2017** | `retargeting_display`, **paso 4, entre las redes de nicho a evaluar** |
| **oDesk** | MUERTA | `seo_long_tail` |
| **Elance** | MUERTA | `seo_long_tail` |

> **Un lector que siga `retargeting_display` hoy instalaria un pixel de una
> plataforma descontinuada y evaluaria una red que cerro hace nueve anos.** El nodo
> es **sano como costura** y esta **caducado como consejo**: son dos preguntas
> distintas y las dos hay que contestarlas.

**TOQUE UNICO MARCADO.** `analisis_trafico_competitivo` **nombra cinco
herramientas** y su gemelo dice *herramientas de medicion de trafico web*, **cero
nombres propios**. **Fundir hacia el generico borra cinco verificaciones de
vigencia de una vez, y dos de las cinco ya estan muertas.** La fusion ahi **no
pierde informacion util: pierde mantenimiento.**

**LA PREGUNTA**: una herramienta muerta **se borra**, **se sustituye** por la viva
equivalente, o **se generaliza** la linea perdiendo el nombre propio?

---

## `OP-S-05`: LO QUE SIGUE SIN VERIFICAR

**`Quantcast`**, en el paso 6 de `analisis_trafico_competitivo`, sigue **SIN
VERIFICAR**, y se registra asi **y no como viva**, porque nadie la ha comprobado.

**EL CENSO, al 11 ago 2026:**

| | |
|---|---:|
| **muertas** | **6**: Alexa, Compete, Perfect Audience, The Deck, oDesk, Elance |
| **vivas** | **7**: AdRoll, MixRank, Adbeat, BuySellAds, InnoCentive, **stopfakes.gov**, **uspto.gov** |
| no verificables | 1: Guide to Greener Electronics |
| sin verificar | 1: Quantcast |
| **verificadas en total** | **14** |
| **anotadas sin verificar** | **18 mas** |

> **Seis muertas de catorce verificadas: la mitad menos una.** No es una prediccion
> sobre los dieciocho: **es la razon para verificarlos.**

**LA PREGUNTA**: se verifica el lote entero antes de la pasada, o se sanea solo lo
verificado?

---

## `OP-S-06`: LOS CAMPOS SUCIOS, con su tabla de mapeo

**Verificado contra el grafo el 11 ago 2026: los seis ids confirmados, 1 mas 1 mas
4, exactamente como los publica la auditoria del motor.**

| clave sucia | nodo | que es |
|---|---|---|
| **`fase_проekto`** | `crosby_habilidad_transmision` | **gemelo cirilico**: las letras `р`, `о`, `е` son cirilicas |
| **`fase_project`** | `mapa_flujo_trabajo_cliente` | gemelo en ingles |
| **`fuentes_adicionales`** | `arquetipos_de_cliente`, `composicion_board_directors`, `definicion_startup`, `preferencia_de_liquidacion` | campo que no esta en el esquema |

> **Que pasa hoy: nada visible, y ese es el problema.** Los dos gemelos conviven
> con un `fase_proyecto` correcto en el mismo nodo, **asi que el motor lee el bueno
> y el sucio viaja de polizon.** El validador no los caza porque **solo exige que
> los obligatorios esten, no que no sobre nada.**

> **Son dos strings que se ven identicos en pantalla: la averia mas dificil de
> diagnosticar que existe.** El dia que alguien escriba `nodo["fase_проekto"]` por
> copiar y pegar de un editor, tendra una clave que **parece** la correcta.

**LA GUARDA**: **lista blanca de claves en Gate 0**. Sin ella, vuelve.

**LA PREGUNTA**: los dos gemelos se borran, y eso es mecanico. Pero
`fuentes_adicionales`: **se fusiona en `fuente` o se borra**? La auditoria lo deja
abierto.

---

## `OP-S-07`: LAS AUTO-ARISTAS · **SEGUNDA CIFRA QUE NO RECONCILIA**

| | publicado | **medido el 11 ago 2026** |
|---|---:|---:|
| nodos vivos con **auto-arista** | **27** | **0** |
| nodos que se listan **a si mismos como alias** | **7** | **0** |

**Medido en las TRES copias del dataset** (`dataset/metadata/master_graph.json`,
`dataset/nodos/*.json` y `web/lib/assets/master_graph.json`), **con y sin resolver
alias: cero en las tres.**

> **Lo que SI reconcilia exacto en la misma auditoria y el mismo dia**: los **77
> alias huerfanos** (medido: 77 clavados) y los campos sucios de B.2 (1 mas 1 mas
> 4). **O sea que el dataset medido es el mismo que se audito, y la discrepancia
> esta solo en estas dos filas.**

> `trilogia_de_juran`, que la auditoria citaba como ejemplo de self-alias, **hoy
> lleva tres alias y ninguno es el suyo.**

**LA PREGUNTA**: la reparacion **ya se hizo fuera de esta campana**, o el
instrumento original **medía sobre otra base**? **No se toca nada hasta saberlo.**

**LA GUARDA SE ANADE IGUAL**, porque es lo que impide que vuelva: Gate 0 rechaza
que un nodo se cite a si mismo como previo o siguiente, y que se liste a si mismo
como su propio alias.

---

## `OP-S-08`: EL RESOLUTOR DE ALIAS, y por que bloquea

**219 nodos escriben 293 alias y NINGUN codigo los lee.** `ids_alias` aparece solo
en la declaracion del tipo y en el consolidador que lo escribe. **No existe
resolutor.**

**Y hay 77 alias que apuntan a ids que ya no son nodos** (medido hoy: **77**,
exactamente lo publicado). Un `project_nodes.node_id` historico que apunte a un id
renombrado **no resuelve**, cae en el `?? nid` y **el usuario ve el id crudo** en
su Expediente o su plan.

> **DEPENDENCIA DURA, y es la unica de esta fase que no es de orden sino tecnica:**
> **`OP-S-01` CREA un alias nuevo.** Sin resolutor, **ese alias no protege las dos
> aristas que dice proteger: solo las documenta.**

**LA PREGUNTA**: los 77 huerfanos **se borran o se registran como deprecados** para
que resuelvan? Y el resolutor, **entra en esta pasada** o es trabajo de motor
aparte?

---

## `OP-S-09`: LOS IDS DE LA DECISION 4

**La politica esta APROBADA el 9 ago 2026**: familia unica, criterio **continua o
repite**, y **fusion con alias**. *Un id no pertenece a una doctrina: pertenece al
catalogo.*

**Y la excepcion tambien esta escrita**: la transdominio y el `_2` de propiedad
intelectual **van por renombre o alias y NO por fusion**, porque en los dos **el
contenido esta sano**. *Fusionar ahi seria arreglar un nombre borrando un nodo
bueno de pago.*

> **LA UNICA PIEZA LISTA Y VERIFICADA ES LA DE NAFTA, y va DENTRO de `OP-S-01`**
> por el toque unico. **El resto de la familia carece de nomina**, y por eso esta
> operacion no se puede cerrar.

**LA PREGUNTA**: **cuales son TODOS los ids de la familia?** La politica esta
aprobada; **la lista sobre la que se decidio no existe escrita.**

---

## `OP-S-10`: EL REENCUADRE DE MARCO

**La doctrina, ya escrita**: *la condicion de pais se copia **A LA PUERTA**, donde
se actua*, es decir a `condiciones_activacion`, **y nombrando el pais**. Dejarla
solo en el resumen **la convierte en una nota al pie de algo que ya se hizo**.

**LA MEDICION DE LOS DOS DOMINIOS, 11 ago 2026:**

| | `franquicias` | `exportacion` |
|---|---:|---:|
| nodos vivos | 195 | 141 |
| **cablean marco de UN SOLO PAIS** | **31** (15,9%) | **42** (29,8%) |
| **condicionan EN LA PUERTA** | **2** | 5 |
| condicionan **en la despedida** | 4 | 23 |
| **NO condicionan en ningun sitio** | **25** (80,6%) | 14 (33,3%) |

> **`franquicias` tiene un problema MAS PEQUENO y MUCHO MAS CALLADO.** Cablea
> marco de un solo pais en **la mitad de proporcion**, pero **el 80,6% de sus nodos
> de marco no nombra el pais en ningun sitio**, contra el **33,3%** de
> `exportacion`. Alli casi siempre esta dicho, aunque tarde; **aqui casi nunca.**

**EL CONTRAMODELO DEL DOMINIO, y son los dos nodos de esta operacion:**
`comprender_definicion_legal_franquicia` y `cumplimiento_ftc_rule_436`, los dos con
la misma primera linea: *solo aplica si vendes o piensas vender franquicias en
Estados Unidos*.

**EL PEOR CASO MEDIDO: `obtencion_marca_registrada`.** Su puerta dice *"aun no se
posee un trademark **federal**"*: **nombra la federacion como si hubiera una sola
en el mundo.** Y sus pasos mandan buscar en la base **TESS del gobierno de EE.UU.**
y presentar ante la **USPTO**, sin condicion de ninguna clase. **Es el unico del
dominio que condiciona con un adjetivo en vez de con un pais.**

**LOS 29 RESTANTES** estan en la tabla de `PENDIENTES.md`, ficha
`vigencia-del-marco-internacional`, con su columna de donde condiciona.

**LA PREGUNTA**: entra `franquicias` al barrido de marco junto a `exportacion`?
**La doctrina mide donde se actua, no cuanto se cita. Sin adjudicar.**

---

## VERIFICACION DE LA FASE

| que | como |
|---|---|
| **claves** | Gate 0 con **lista blanca** rechaza cualquier clave desconocida |
| **auto-referencia** | Gate 0 rechaza que un nodo se cite a si mismo como previo, siguiente o alias |
| **alias** | ningun alias apunta a un id que no sea nodo; **existe `resolverId`** y lo usa toda lectura de `node_id` historico |
| **vigencia** | ningun nodo vivo lleva NAFTA en id ni titulo; los tres de Incoterms llevan su ano; ningun nodo cablea `export.gov` |
| **herramientas** | ningun nodo vivo nombra las seis muertas |
| **marco** | todo nodo con marco de un solo pais **nombra el pais en `condiciones_activacion`** |
| **general** | Gate 0 verde, y ningun Expediente ni plan muestra un id crudo |
