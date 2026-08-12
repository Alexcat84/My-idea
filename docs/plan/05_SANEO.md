# FASE 05: EL SANEO

**Nombres, versiones, direcciones y claves.** Casi nada de esta fase toca la
doctrina de un nodo, y por eso es la mas barata de todos los frentes abiertos.
**La excepcion es la primera operacion, que es una fusion.**

**Operaciones: `OP-S-01` a `OP-S-10`. SIETE LISTAS y TRES pendientes**, tras las
adjudicaciones del 11 ago 2026.

| operacion | la adjudicacion, en una linea |
|---|---|
| **`OP-S-01`** | **sobrevive el nodo generico de tratados**; `nafta_free_trade_agreements` se deprecia CON ALIAS |
| **`OP-S-02`** | la reparacion **pasa de doce a tres**: enlazar no es citar |
| **`OP-S-04`** | rige el **remedio espejo**: ejemplo se vuelve generico con ejemplos vivos; objeto lleva ficha de vigencia |
| **`OP-S-05`** | **solo se verifica lo que es objeto o URL cableada**; lo que es ejemplo se genericaliza y no se verifica |
| **`OP-S-06`** | `fuentes_adicionales` **se trata como fuente**, misma tabla de mapeo |
| **`OP-S-09`** | nomina recomputada: **53 familias, 125 nodos vivos** |
| **`OP-S-07`** | **VUELVE al plan**: mi medicion de cero estaba mal, son 27 |
| **`OP-S-08`** | deja de ser construir un resolutor y pasa a ser **medir por donde pasa** |
| **`OP-S-10`** | **condicional**: entra si la medicion muestra ley con alcance real |

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

## `OP-S-01`: EL PAR DE NAFTA . **LISTA**

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

**ADJUDICADO: SOBREVIVE EL NODO GENERICO DE TRATADOS**,
`certificado_de_origen_tratados_libre_comercio`, y `nafta_free_trade_agreements`
**se deprecia CON ALIAS**. Es la direccion que cierra los tres encargos en un solo
acto.

> **Y la dependencia que esta operacion tenia queda CORREGIDA: ya no espera a
> nadie.** Se escribio que dependia de un resolutor inexistente. **El resolutor
> existe** (`graph.ts`, linea 131), asi que **el alias funciona el mismo dia que se
> escribe.**

---

## `OP-S-02`: INCOTERMS SIN VERSION . **LISTA**

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

**ADJUDICADO: LA REPARACION PASA DE DOCE A TRES.** Solo tres nodos lo citan en su
texto, y **de esos, DOS lo llevan tambien en el id**
(`incoterms_reglas_comerciales_internacionales` y `terminos_de_venta_incoterms`).
**El resto lo apunta por arista, y enlazar no es citar.**

> **La version que se escribe es la vigente al corte.** Si el fundador quiere otra
> edicion lo dice; no es una decision que este plan tenga que tomar.

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

## `OP-S-04`: LAS SEIS HERRAMIENTAS MUERTAS . **LISTA**

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

**ADJUDICADO: RIGE EL REMEDIO ESPEJO.**

| si el nombre propio es | que se hace |
|---|---|
| un **EJEMPLO** | la linea se vuelve **generica** y se le ponen **ejemplos vivos** |
| el **OBJETO** del nodo | el nodo se queda y lleva **ficha de vigencia** |

> **El espejo resuelve los cinco nodos sin excepcion: en los cinco la herramienta
> es EJEMPLO, no objeto.** Ninguno de los cinco trata SOBRE una herramienta, asi
> que **no hace falta abrir ficha de vigencia a ninguno: se generalizan los cinco.**

---

## `OP-S-05`: LO QUE SIGUE SIN VERIFICAR . **LISTA**

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

**ADJUDICADO, y cierra el problema por REDUCCION: solo se verifican los nombres
que son OBJETO del nodo o URL CABLEADA. Los que son ejemplo se genericalizan y no
se verifican.**

> **Los dieciocho pendientes dejan de ser una deuda de verificacion.** `Quantcast`
> es **ejemplo** en el paso 6 de `analisis_trafico_competitivo`: **no se verifica,
> se genericaliza** con `OP-S-04`. Lo que si entra a verificacion son las **URL
> cableadas**, y las dos que habia, `stopfakes.gov` y `uspto.gov`, **ya estan
> verificadas y vivas**.

---

## `OP-S-06`: LOS CAMPOS SUCIOS . **LISTA**

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

**ADJUDICADO: `fuentes_adicionales` SE TRATA COMO FUENTE**, con la misma tabla de
mapeo. **No se borra: su contenido entra al campo `fuente`.**

> **Los dos gemelos de fase si se borran**, y eso sigue siendo mecanico y sin
> criterio. **Lo que cambia es el cuarto campo: deja de ser una duda y pasa a ser
> una migracion de contenido.**

---

## `OP-S-07`: LAS AUTO-ARISTAS . **LISTA**

**Vuelve al plan como operacion LISTA. El auditor la remidio con la semantica de
`resolverId` y coincide con la cifra remedida: la publicada estaba bien.**

**REMEDIDO y CONFIRMADO por dos instrumentos independientes:**

| | publicado | **remedido el 11 ago 2026** |
|---|---:|---:|
| nodos vivos con auto-arista | **27** | **27** |
| enlaces implicados | | **33** |
| de ellos **directos** | | **0** |
| de ellos **via alias** | | **33** |
| nodos con **self-alias** | 7 | **0** |

> **La cifra de 27 es EXACTA. La de 7 si encogio a cero.**

**POR QUE NINGUNA ERA VISIBLE: ninguna es directa.** El nodo no se cita a si mismo
por su id; **cita un id que es su propio alias**. El ejemplar que el informe ya
nombraba lo prueba: `analisis_flujo_de_valor` lleva `value_stream_analysis_lean` en
sus `nodos_previos`, **y ese id es su propio alias**.

**EL PEOR**: `costo_de_mala_calidad_copq`, con **siete** enlaces a si mismo, dos en
previos y cinco en siguientes.

**LOS VEINTISIETE**: `analisis_de_cohortes`, `analisis_flujo_de_valor`,
`buyin_customer_development`, `costo_de_mala_calidad_copq`, `cronograma_proyecto`,
`cuatro_etapas_del_pensamiento_creativo`, `cumplimiento_inversionistas_acreditados`,
`customer_needs_spreadsheet`, `customer_retention_tactics`,
`decision_pivotar_o_proceder`, `definicion_sprint_terminado_fisico`,
`diseno_experimentos_pass_fail`, `diseno_landing_page`,
`diseno_para_el_ciclo_completo`, `eleccion_abogado_franquicias`,
`elevated_surfaces_fall_protection`, `gestion_portafolio_formal`,
`lockout_tagout_procedures`, `medir_comportamiento_cliente_mvp`,
`medir_huella_carbono_corporativa`, `metodo_strategic_buckets`,
`metricas_accionables`, `multi_sided_platforms`, `redundancia_en_diseno`,
`reglas_gestion_riesgo_gambling`, `reporte_estado_miembro_equipo`,
`search_for_business_model`.

**EL ARREGLO**: de cada uno de los 27, **retirar el enlace de `nodos_previos` o
`nodos_siguientes` que RESUELVE al propio nodo**. Son **33 enlaces**. No se toca
ningun otro campo, **y los `ids_alias` NO se tocan**: el alias es correcto y util;
**lo que sobra es la arista que lo usa para volver a casa.**

**VERIFICACION:**

- ningun nodo vivo se cita a si mismo **ni directamente ni tras resolver alias**
- **el conteo de aristas del grafo baja en 33 exactamente**, ni una mas
- la guarda se prueba **con un caso positivo**: si se reinyecta el enlace de
  `analisis_flujo_de_valor` a `value_stream_analysis_lean`, **Gate 0 tiene que
  caerse**

### LA CONSECUENCIA DE MAQUINARIA: LA GUARDA DE GATE 0 DEBE RESOLVER, NO COMPARAR

> **Un chequeo literal, id contra id, da CERO sobre un grafo con VEINTISIETE.**
> Ninguna de las 33 es directa.
>
> **Una guarda que compare literalmente pasaria verde el dia de la reparacion y
> seguiria pasando verde si manana vuelve a entrar una. Es una guarda que no
> guarda.**

**La guarda correcta**: pasar cada id de `nodos_previos` y `nodos_siguientes` **por
el resolutor** y compararlo con el id del propio nodo.

> **EL BANCO 9.14 NO SE MUEVE.** La regla de excluir el propio nodo al contar grado
> sigue en pie, y **su motivo queda confirmado en vez de corregido.** Es el
> ejemplar mayor de la regla **P.1** del banco del plan.

---

## `OP-S-08`: POR DONDE PASA EL RESOLUTOR . **LISTA**

**La dependencia estaba mal escrita y se corrige.** Se escribio que ningun codigo
leia `ids_alias`. **Verificado contra el codigo el 11 ago 2026: si lo lee.**

| pieza | donde |
|---|---|
| el mapa de alias | `web/lib/engine/graph.ts`, `mapaDeAlias`, **linea 107** |
| **`resolverId`** | **linea 131**, y **camina cadenas** hasta un nodo activo |
| lo invocan | `etiquetaArbol` (**164**) y `tituloDeNodo` (**172**) |
| espejo en Python | `scripts/reanclar_por_resolutor.py` |
| lo ejercitan | `resolutorHistoria.test.ts` y `compass.test.ts` |

> **`resolutorHistoria.test.ts` documenta que la promesa estaba a MEDIO cumplir, no
> incumplida.** Incluso guarda contra la regresion: comprueba que el fuente **no
> vuelva a contener** el acceso directo `titulo_concepto ?? nid`.

**ESTA OPERACION YA NO ES CONSTRUIR NADA: ES MEDIR POR DONDE PASA.**

**MEDIDO el 11 ago 2026**, sobre produccion (`web/lib` y `web/app`, sin tests):

| | |
|---|---:|
| accesos **directos** al grafo por id | **42** |
| ficheros que los contienen | **12** |
| de esos, ficheros que **manejan ids de origen externo** | **9** |

**LOS ALIAS, medidos el mismo dia:**

| | |
|---|---:|
| alias totales | **391** |
| a nodo **deprecado**, que es su funcion | **314** |
| **colisiones vivas** | **0** |
| **huerfanos** a ids inexistentes | **77** |

> **Los 77 se limpian en el saneo SIN RIESGO**: con **cero colisiones vivas**, su
> borrado no puede romper una resolucion buena. **Los 314 no se tocan**: apuntar a
> un deprecado ES la funcion del alias, y `resolverId` los camina hasta un activo.

> **Y esta operacion YA NO BLOQUEA A `OP-S-01`.** El resolutor existe, asi que el
> alias que esa operacion crea **funciona el mismo dia que se escribe.**

### CLASIFICADOS POR ORIGEN DEL ID: 22 INTERNOS y 20 EXTERNOS

> **EL CRITERIO, en una linea.** Un id **INTERNO** salio del propio grafo en la
> misma pasada, un `nodos_siguientes` o una clave, y por tanto **esta al dia por
> construccion**. Un id **EXTERNO** entro desde fuera, de una sesion persistida, un
> artefacto en disco o un parametro, y **puede ser de cualquier era**.
>
> **El riesgo esta SOLO en los externos.** Los veintidos internos se dejan como
> estan.

**LOS VEINTE EXTERNOS, con su origen y su blindaje:**

| sitio | de donde viene el id | como esta hoy | blindaje |
|---|---|---|---|
| `compass.ts:153` | indice semantico **persistido** | **HUECO REAL**: si `graph[id]` es `undefined` la condicion entera es falsa y **el id PASA el filtro** | resolver **antes** de puntuar, y descartar el que resuelva a `null` |
| `clasificar.ts:34, 35, 36` | `entrySeeds` por parametro | sin guarda: rompe con un seed historico | una sola resolucion arriba del `map` cubre las tres |
| `graph.ts:244` | `resumenNodo(nid)`, con ids de sesion | sin guarda: `n.titulo_concepto` rompe | resolver al entrar, **como ya hacen `etiquetaArbol` y `tituloDeNodo` dos funciones mas arriba** |
| `interprete.ts:331, 332, 333` | `saltoCandidatos`, del indice semantico | sin guarda | heredan el arreglo de `compass.ts:153` |
| `planRedactor.ts:53` | `aMaterial(nid)`, llamado con `recorrido.ruta` y `cosechaIds` | sin guarda: rompe | resolver dentro de `aMaterial`: **una linea cubre sus dos llamadas** |
| `recorrido.ts:271` | `nid` del estado persistido | sin guarda | resolver antes de `obtenerPregunta` |
| `recorrido.ts:649` | `nuevoActualId`, del camino de sesion | sin guarda | resolver antes de `obtenerPregunta` |
| `organizer/route.ts:66, 67, 68` | `cargarEntrySeeds()` **sin pasarle el grafo** | sin guarda | **llamar `cargarEntrySeeds(graph)`**: la funcion ya filtra por `esOfrecible` cuando lo recibe |
| `organizer/stream/route.ts:87, 88, 89` | igual | sin guarda | igual |
| `start/route.ts:255` | `brecha.semillaId`, de `packs_entry_seeds` | **ya guardado** en la linea 149, con aviso | cambiar *esta en el grafo* por *resuelve*: hoy una semilla renombrada aborta cuando podria resolver |
| `session/plan:267` | `recorrido.ruta` (**sesion persistida**) | guardado con `filter(nid in graph)`: **no rompe, OMITE EN SILENCIO** | **resolver en vez de filtrar** |
| `session/plan:405` | `recorrido.ruta`, ultimo | `?.` con fallback a `ideacion` | **resolver**: hoy degrada la fase del proyecto en silencio |

**TRES ARREGLOS CUBREN CATORCE DE LOS VEINTE:**

| arreglo | cubre |
|---|---:|
| resolver dentro de `aMaterial` | **3** (la 53 y sus dos llamadas) |
| llamar `cargarEntrySeeds(graph)` en los dos organizer | **6** |
| resolver en `compass.ts:153` | **4** (la suya y las tres de `interprete`) |

> **LOS DOS MAS CAROS NO ROMPEN: CALLAN.** `session/plan:267` filtra, y **un
> concepto historico se cae de la lista sin que nadie se entere**.
> `session/plan:405` degrada la fase del proyecto a `ideacion` con un `??`
> silencioso. **Los dos son exactamente el modo de fallo que el canon de fallar
> ruidoso prohibe**, y ninguno de los dos se ve en una prueba verde.

---

## `OP-S-09`: LOS IDS DE LA DECISION 4 . **LISTA**

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

**ADJUDICADO Y RECOMPUTADO.** Con el criterio de la propia decision (sufijo
numerico, particulas, orden de palabras y sinonimo), medido el 11 ago 2026 sobre
nodos VIVOS:

| | |
|---|---:|
| **familias** | **53** |
| **nodos vivos implicados** | **125** |

**POR CAUSA:** 35 familias por **sufijo numerico**, 12 por **particulas** (de, del,
la, el), 6 por **orden de palabras**, y **0** por sinonimo puro.

**LAS CUATRO MAYORES:**

| familia | miembros |
|---|---|
| `accion_correctiva` | `accion_correctiva`, `_2`, `_4`, `_5`, `_6` |
| el consejo de calidad | `consejo_calidad`, `consejo_calidad_2`, `consejo_de_calidad`, `consejo_de_calidad_2`, `consejo_de_calidad_3` |
| el programa Make Certain | `make_certain_programa`, `programa_make_certain`, `_2`, `_3` |
| definiciones operacionales | `definiciones_operacionales`, `_2`, `_3`, `_4` |

> **DELTA DECLARADO: el auditor dio 123 nodos y mi recomputo da 125, con las 53
> familias clavadas.** La diferencia es de dos nodos y no de familias. **Se declara
> en vez de forzarse.**

**LA EXCEPCION YA ESCRITA SE MANTIENE**: la transdominio y el `_2` de propiedad
intelectual **van por renombre o alias y NO por fusion**, porque en los dos el
contenido esta sano.

---

## `OP-S-10`: EL REENCUADRE DE MARCO . **CONDICIONAL**

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
| **auto-referencia** | Gate 0 rechaza que un nodo se cite a si mismo como previo o siguiente **con la semantica de `resolverId`**, no por comparacion de id crudo |
| **alias** | ningun alias apunta a un id que no sea nodo; **existe `resolverId`** y lo usa toda lectura de `node_id` historico |
| **vigencia** | ningun nodo vivo lleva NAFTA en id ni titulo; los tres de Incoterms llevan su ano; ningun nodo cablea `export.gov` |
| **herramientas** | ningun nodo vivo nombra las seis muertas |
| **marco** | todo nodo con marco de un solo pais **nombra el pais en `condiciones_activacion`** |
| **general** | Gate 0 verde, y ningun Expediente ni plan muestra un id crudo |

---

## `OP-S-11`: EL CAMPO `fuente` CANONICO . **LISTA**

**Una sola operacion que sirve a TRES cosas**, y por eso no se deja repartida:

| a quien sirve | por que |
|---|---|
| **al CENSO** | hoy **el mismo libro se cuenta dos y tres veces** |
| **al PREDICTOR** | la senal que mejor separa costuras (**91% en nodos de dos o mas libros contra 4% en los de uno**) **se calcula sobre este campo**, y la propia campana declaro que **su base no esta auditada** |
| **a la ADUANA** | **sin lista canonica, el control posicional de P.2 cuenta mal**. Es prerrequisito de `OP-A-01` |

**LA TABLA DE MAPEO, medida el 11 ago 2026, y va DENTRO de esta operacion:**

> **129 grafias distintas en primera posicion se reducen a 55 LIBROS CANONICOS.**

| caso probado | grafias | sin normalizar | canonico |
|---|---:|---:|---:|
| Hugos | **2** | 23 | **21** |
| Horowitz | **3** | 16 | **14** |

**EL PATRON DE LA AVERIA, y no es de tecleo**: varias grafias estan **TRUNCADAS a
unos treinta caracteres** (*Essentials of Supply Chain Mana*, *Co-Intelligence_
Living and Wor*, *Juran's Quality Handbook_ The C*). **Apunta a un recorte de campo
en alguna importacion.**

**Y HAY UN NODO QUE DECLARA EL MISMO LIBRO DOS VECES**:
`decision_de_vender_startup` lleva *The Hard Thing About Hard Thing* y *The Hard
Thing About Hard Things* **en la misma linea**.

> **La nomina de Hugos del auditor, los 21, SOLO CUADRA CON EL NOMBRE CANONICO.**
> Es la prueba de que **sin esta operacion las cifras del recorte no son
> reproducibles.**

**LA CONSECUENCIA QUE MAS IMPORTA, y no es del censo**: **un libro con dos grafias
puede convertir un nodo de UN libro en uno de DOS**, y el predictor de costuras
separa justamente por ahi. **Mientras el campo no este limpio, el 91% contra 4% no
se puede usar para nada que no sea ordenar una cola.**

---

## `OP-S-12`: **LAS ARISTAS DUPLICADAS TRAS RESOLUCION** . **LISTA**

**MEDIDO EL 11 ago 2026** con `scripts/plan/aristas_duplicadas_tras_resolver.py`,
sobre los **3.521 nodos vivos**. **Salio de tirar del hilo de las diez de Affirm.**

**QUE ES LA CLASE.** Un campo de aristas que **lista el id viejo y el nuevo**, y los
dos **resuelven al mismo destino**. No es un fallo del resolutor: **es basura que
dejo cada fusion**, que reescribio la referencia **y ademas conservo la vieja.**

| | |
|---|---:|
| nodos vivos revisados | 3.521 |
| **nodos con al menos una duplicada** | **802** *(22,8% del catalogo vivo)* |
| **entradas que SOBRAN** | **1.056** |
| grupos afectados (nodo mas campo mas destino) | 1.015 |

> **LAS DIEZ DE AFFIRM ERAN LA PUNTA: hay CIENTO CINCO VECES MAS.** Y no estaban
> escondidas: **nunca se habian contado**, porque el resolutor las tapa y el grafo
> se ve bien desde fuera.

**POR MOTIVO, y el reparto es casi total:**

| motivo | entradas |
|---|---:|
| **el id nuevo mas su alias** en la misma lista | **1.053** |
| dos alias del mismo destino, sin el literal | **3** |

**Los tres del segundo motivo, nombrados**, porque son los unicos donde el id bueno
**no esta**: `cero_defectos` lista dos grafias de `definicion_calidad_conformidad`;
`definicion_calidad_conformidad` lista dos de `rejilla_madurez_gestion_calidad`; y
`market_type_revenue_growth` lista `revalidar_modelo_negocio` y
`revalidacion_modelo_negocio`, **las dos del mismo destino y ninguna es el destino.**

**POR CAMPO, y esta repartido por igual**: `nodos_previos` **531**,
`nodos_siguientes` **525**. **No es un defecto de un lado del grafo.**

**POR DOMINIO:**

| dominio | nodos tocados | duplicadas |
|---|---:|---:|
| `core` | 370 | **461** |
| `quality` | 214 | **306** |
| `health_safety` | 79 | 121 |
| `environmental` | 53 | 59 |
| `franquicias` | 48 | 55 |
| `exportacion` | 32 | 48 |
| `risk_management` | 3 | 3 |
| `entrega` | 2 | 2 |
| `seguridad_digital` | 1 | 1 |

**POR TAMANO DEL GRUPO**: 981 grupos con **una** entrada de mas, 29 con dos, 4 con
tres y **uno con cinco**. **La cola larga es de a una**, lo que confirma el
mecanismo: **cada fusion deja una.**

**EL PEOR EJEMPLAR, y merece leerse entero.** `doble_significado_calidad` tiene en
`nodos_siguientes` **SEIS entradas que van todas a `definicion_calidad_conformidad`**:
`definicion_calidad_conformidad_requisitos_2`, `definicion_calidad_como_conformidad`,
`definicion_calidad_conformidad_requisitos_3`,
`definicion_calidad_conformidad_requisitos`, `conformance_to_requirements` y el
propio `definicion_calidad_conformidad`. **Seis nombres del mismo nodo en la misma
lista.**

**Y LA BASURA SE CONCENTRA EN POCOS DESTINOS**, que son los que mas fusiones han
recibido: `costo_de_mala_calidad_copq` aparece duplicado **en 46 nodos distintos**,
`search_for_business_model` en 35 y `decision_pivotar_o_proceder` en 18.

### LA OPERACION, y es **MECANICA**

> **Por cada nodo vivo y por cada uno de sus dos campos: resolver todas las entradas
> con la semantica de `resolverId`, quedarse con los destinos DISTINTOS, y escribir
> el ID RESUELTO.** Nada mas.

**NO HAY NADA QUE DECIDIR AQUI, y por eso es LISTA y no mesa:** las entradas que se
borran **apuntan al mismo sitio que la que se queda**. **El grafo despues del
arreglo tiene exactamente los mismos vecinos.**

**LO QUE NO TOCA, a proposito:**

| no toca | por que |
|---|---|
| el mismo destino en `nodos_previos` **y** en `nodos_siguientes` | **no es duplicado: es ida y vuelta**, y decidir eso es otra operacion |
| la **auto-arista** (destino igual al propio nodo) | es **`OP-S-07`**, y contarla aqui inflaria las dos cifras. **Medido: cero solape** |

### **EL ORDEN IMPORTA, y es lo unico delicado de esta operacion**

> **`OP-S-12` SE CORRE AL FINAL DE LA PASADA, DESPUES DE TODAS LAS FUSIONES Y
> RENOMBRES.** Si se corriera antes, **cada fusion posterior volveria a generar su
> duplicada** y habria que correrla dos veces.

**Es la misma logica que ya tiene el plan para el recomputo:** lo que depende del
estado final **se hace cuando el estado es final.**

### VERIFICACION

| | |
|---|---|
| **el conteo despues del arreglo da CERO** | mismo script, misma semantica |
| **el vecindario resuelto de cada nodo NO CAMBIA** | conjunto de destinos distintos antes igual a despues, nodo por nodo. **Es la prueba de que la operacion no perdio ninguna arista** |
| **cero solape con `OP-S-07`** | ningun grupo con destino igual al propio nodo |
| **el numero de entradas baja en exactamente 1.056** | si baja mas, se borro algo que no era duplicado |
