# Auditoría del motor — PASO 1: el inventario

**Solo lectura. Cero cambios de código.** Ni un arreglo de paso, ni siquiera los
obvios. De aquí sale el plan de arreglos que adjudican el auditor y el fundador.

Fecha: 2026-08-08. Rama `staging`, `0fc0ca1`. Estado de partida: motor 19/19, web
992/992, Gate 0 OK, rumbos sin deriva. **Todo lo que sigue está roto o flojo
*debajo* de esas cuatro capas verdes**, que es exactamente el punto.

**Veredicto de arranque: no hay ROJO.** Nada de lo encontrado es tan grave que
no deba esperar la adjudicación. Lo digo explícitamente porque los seis paros
anteriores fueron correctos y no voy a fabricar un séptimo: el producto está
pre-beta, sin usuarios vivos, y ninguna de las averías está hiriendo a nadie hoy.
Varias herirían el día que entre el primer tester. Esa es la diferencia entre
esta lista y una alarma.

---

# (A) EL MAPA

## A.1 — `web/lib/engine/` (23 módulos, 8.134 líneas con sus tests)

El motor de producción. Todo lo que la web ejecuta de verdad.

| módulo | responsabilidad | lo llaman | llama a |
|---|---|---|---|
| **`graph.ts`** (162) | acceso al grafo: cargar, sucesores, semillas, **`esOfrecible`** | **31 sitios** | assets |
| **`recorrido.ts`** (660) | el bucle de entrevista, versión resumible (el CLI bloquea, la web no) | 8 | compass, interprete, reeleccionPuerta, graph |
| **`planRedactor.ts`** (625) | cosecha del vecindario + ensamblado del plan + autodeclaración | 4 | interprete, graph, readiness, verificadorHuerfanos, detectorAcentos |
| **`interprete.ts`** (540) | interpretar multi-salto (capa 2), reparación de camino, respaldo tier-2 | 6 | compass, graph, tokens |
| **`reporteFlow.ts`** (298) | mini-entrevista de Tus Números, resumible | 3 | reporte, calculadora |
| **`reporte.ts`** (219) | piezas deterministas y de IA del reporte numérico | 4 | calculadora, constants |
| **`enlazador.ts`** (215) | mundos de protección: enlazar el plan del mundo con las actividades reales | 2 | snapshotProyecto |
| **`estimacion.ts`** (175) | scheduler: la banda de duración nace con el plan (mayoría de 3) | 3 | — |
| **`bloqueRealidad.ts`** (173) | el espejo de lo real **para el motor** (lo que el Análisis muestra al humano) | 2 | analytics |
| **`reformuladorProteccion.ts`** (170) | ancla la pregunta del mundo de protección a lo que ya existe | 3 | interprete |
| **`snapshotProyecto.ts`** (144) | la foto del plan vigente que consumen los mundos de protección | 8 | dbContract |
| **`seguimientoComposer.ts`** (135) | el ritual de 3 tarjetas → mensaje "qué ha pasado" | 2 | dbContract |
| **`reeleccionPuerta.ts`** (121) | **el mundo nunca abandona**: reelige puerta si el intérprete descarta | 2 | evaluacionBrecha, graph, tokens |
| **`puertaAvanzada.ts`** (121) | candidatos y elección de puerta en seguimiento | 3 | graph, tokens |
| **`checklist.ts`** (97) | deriva el checklist de un plan finalizado (determinístico, cero LLM) | 3 | dbContract |
| **`constants.ts`** (100) | constantes del bucle que no son grafo ni brújula | 6 | — |
| **`evaluacionBrecha.ts`** (88) | elige la semilla de entrada de un pack (determinística) | 4 | assets, tokens |
| **`diagnosticoMundo.ts`** (83) | el redactor del diagnóstico del preview | 1 | graph, recorrido |
| **`organizador.ts`** (78) | lo compartido entre el organizador JSON y el SSE | 4 | voz |
| **`juezSesion.ts`** (77) | juez de sesión muestreado (Haiku) | 2 | graph, interprete |
| **`previewMundos.ts`** (72) | lógica pura del preview (cero LLM, cero DB) | 6 | — |
| **`clasificar.ts`** (56) | texto libre → (puerta, perfil de sesión) | 1 | graph |
| **`tokens.ts`** (22) | tokenizador de cosecha, compartido | 5 | — |

## A.2 — `engine/` (Python, 6.901 líneas)

| módulo | responsabilidad | estado |
|---|---|---|
| **`prototipo_motor.py`** (3.383) | el motor original de CLI **y la fuente de los 12 prompts** | vivo como fuente, fósil como producto |
| **`calculadora.py`** (502) | la aritmética de Tus Números | vivo; gemelo TS en `web/lib/calculadora.ts` |
| **`db.py`** (300) | persistencia del CLI | fósil |
| **`build_question_cache.py`** (221) | genera `preguntas_cache.json` | vivo, de línea de ensamblaje |
| **`verificador_huerfanos.py`** (160) | caza ids citados que no existen | vivo; gemelo TS |
| **`plan_readiness.py`** (111) | mide si un nodo está listo para plan | vivo, de línea de ensamblaje |
| **`build_semantic_index.py`** | índice semántico (versión vieja, sin Voyage) | fósil |
| 19 × `test_*.py` | la capa "motor 19/19" | viva |

## A.3 — LAS PUERTAS ÚNICAS

Piezas por las que **debe** pasar todo el que quiera hacer esa cosa. Su valor
está en que no haya una segunda entrada.

| puerta | qué controla | quién la respeta | vigilante |
|---|---|---|---|
| **`esOfrecible(nid, graph, dominios)`** en `graph.ts` | si un nodo puede ofrecerse (existe + no deprecado + dominio abierto) | los **tres** caminos de oferta: recorrido, semillas, índice semántico | `puertaUnica.test.ts` (verificado no-vacuo por sabotaje) |
| **`PRECIOS`** en `precios.ts` | el precio de un mundo | la ruta de unlock, la de plan, la tarjeta | comentario explícito en unlock (`el catálogo decía 3 cuando se cobraban 5`) |
| **`catalogoMundos.ts`** | qué mundos existen y cuáles son visibles | UI + rutas | `catalogoMundos.test.ts` |
| **`consumir_creditos` / `reembolsar_creditos`** (RPC de Postgres) | el dinero | `creditos.ts`, único llamador | atomicidad de Postgres + clave de idempotencia `plan:{sessionId}` |
| **`dominiosDesbloqueados()`** en `db.ts` | el muro de mundos | todo el motor | — |
| **`espacios.ts`** | un proyecto = núcleo + mundos | toda la UI de espacios | `espacios.test.ts` |

## A.4 — REGLAS ESCRITAS EN DOS SITIOS

Aquí hay que corregir la premisa del encargo, porque el reparto real es otro.

### El corredor de rumbos NO está duplicado
`scripts/rumbos/prueba_rumbos.py` es **Python y solamente Python**. No existe
gemelo TS. Busqué `banco_rumbos`/`prueba_rumbos` en todo `web/` y no hay nada.
La duplicación de verdad está en otro sitio y es mucho más grande.

### LA COPIA GRANDE: el motor entero existe dos veces
`web/lib/engine/*.ts` es, módulo por módulo y por declaración propia en cada
docstring, **el port de `engine/prototipo_motor.py`**. Doce de los veintitrés
módulos dicen "port de …" en su primera línea.

- **Declarada**: sí, en cada archivo.
- **Con vigilante**: **solo para los prompts**, no para la lógica.

### El reparto exacto, pieza por pieza

| pieza duplicada | tipo | vigilante | veredicto |
|---|---|---|---|
| **los 12 `SYSTEM_*`** | copia declarada | `sync_assets_web.py` los exporta **desde el módulo Python** (`getattr`, no retipeados) + `checksums.test.ts` verifica sha256 contra el manifest | **declarada, con vigilante — pero con un hueco, ver abajo** |
| **`calculadora.py` ↔ `calculadora.ts`** | copia declarada | dos suites en paralelo (`test_calculadora.py` 381 l, `calculadora.test.ts`) sobre los mismos casos | **declarada, con vigilante** |
| **`verificador_huerfanos.py` ↔ `verificadorHuerfanos.ts`** | copia declarada | test a cada lado | **declarada, con vigilante** |
| **`buscar_afines` (py) ↔ `compass.ts`** | copia declarada | `compass.test.ts` + fixture generado (`gen_compass_fixture.mjs`) | **declarada, con vigilante** |
| **la lógica del recorrido, el intérprete, el redactor** | **copia silenciosa** | **ninguno**: cada lado tiene sus propios tests, nadie compara los dos | **DEFECTO** |
| **3 prompts nuevos** (`REFORMULADOR_PROTECCION`, `ENLACE_PROTECCION`, `ESTIMACION_BANDA`) | solo TS | n/a | **correcto**, son funciones que nunca existieron en Python |

### El hueco del vigilante de prompts
`checksums.test.ts` verifica que **`prompts.json` no haya sido tocado a mano**
(hash contra el manifest). No verifica que **`prompts.json` esté al día respecto
de `prototipo_motor.py`**: si alguien edita un `SYSTEM_*` en Python y no corre
`sync_assets_web.py`, el JSON y el manifest siguen coincidiendo entre sí y el
test pasa **con la copia vieja en producción**.

> El vigilante custodia que nadie toque la copia. No custodia que la copia esté
> al día. Es la mitad del trabajo, y la mitad que falta es la que se degrada sola.

### La consecuencia estructural de la copia silenciosa
El prototipo Python ya **no puede correr el producto**: le faltan los mundos de
protección, el scheduler, el preview, los espacios. Los 19 tests del motor
verifican reglas de un motor que ya no es el que atiende al usuario. **Siguen
siendo válidos como especificación del núcleo original; ya no son evidencia de
que producción funcione.** La capa "motor 19/19" hay que leerla así.

---

# (B) LA DEUDA VIVA

## B.1 — Los tests fijados al estado real (esperando mejora)

### **B1.1 — La reelección de puerta está inoperante en `quality`**
- **Qué es**: `reeleccionPuerta.ts` implementa *"el mundo nunca abandona"*: si el
  intérprete descarta la puerta, se reelige otra semilla del pack. En `quality`,
  la rama de **cualquiera** de las 7 semillas se traga a las otras 6, así que no
  queda ninguna semilla fuera y la reelección **siempre** cae al respaldo de
  "vecinos del dominio".
- **Qué pasa hoy**: el test (`reeleccionPuerta.test.ts:171-198`) **fija el estado
  real** y afirma `esSemilla === false`. Verde, y describiendo una avería.
- **Si nadie lo arregla**: en Calidad —el mundo más grande y el más vendido— un
  usuario que rechace la puerta recibe un nodo vecino cualquiera en vez de una
  puerta pensada. La entrevista sigue, la calidad del arranque baja, y **nadie se
  entera** porque el test es verde.
- **No lo causó la fusión**: antes ya era 6 de 7; la fusión se comió el último
  margen y lo hizo visible. Está en la ficha `densidad-de-quality`.
- **Recomendación**: **ficha, post-beta.** Arreglarlo es podar aristas del pack
  más denso, y eso mueve el vecindario justo antes de medir. El tercer argumento
  de espera del núcleo aplica igual aquí.

### **B1.2 — El fixture de reelección migró y el margen es de 3**
- **Qué es**: `SEMILLA_RECHAZADA` era `medicion_calidad`; al fusionar, su rama se
  tragó la séptima semilla y el test pasaba por **una** de margen. Se movió a
  `mejora_continua_del_proceso`, que deja 3 fuera.
- **Si nadie lo arregla**: la próxima fusión en `quality` se come esos 3 y el
  test cae de golpe, sin nadie que sepa por qué.
- **Recomendación**: **arreglar ahora, barato.** El test debe elegir su fixture
  **calculándolo** (la semilla con más nodos fuera de su rama) en vez de tenerlo
  escrito a mano. Deja de envejecer.

## B.2 — Los campos sucios del dataset (confirmados, siguen ahí)

Recuento sobre los 3.835 nodos en disco:

| campo | nodos | qué es |
|---|---|---|
| `fuentes_adicionales` | **4** | `arquetipos_de_cliente`, `composicion_board_directors`, `definicion_startup`, `preferencia_de_liquidacion` |
| **`fase_проekto`** | **1** | `crosby_habilidad_transmision` — **gemelo cirílico**: las letras `р`, `о`, `е` son cirílicas |
| `fase_project` | **1** | `mapa_flujo_trabajo_cliente` — gemelo en inglés |

- **Qué pasa hoy**: **nada visible**, y ese es el problema. Los dos gemelos
  conviven con un `fase_proyecto` correcto en el mismo nodo, así que el motor lee
  el bueno y el sucio viaja de polizón. El validador no los caza porque solo
  exige que los obligatorios estén, no que no sobre nada.
- **Si nadie lo arregla**: el día que alguien escriba `nodo["fase_проekto"]` por
  copiar-pegar de un editor, tendrá una clave que *parece* la correcta y no lo
  es. Es la avería más difícil de diagnosticar que existe: **dos strings que se
  ven idénticos en pantalla.**
- **Recomendación**: **arreglar ahora.** Es barato y es de higiene: borrar los 2
  gemelos, decidir si `fuentes_adicionales` se fusiona en `fuente` o se borra, y
  **añadir al Gate 0 un chequeo de claves desconocidas** (lista blanca), que es
  lo que impide que vuelva.

## B.3 — **`ids_alias`: una promesa que nadie cumple** ← el hallazgo más grande de esta sección

- **Qué es**: el consolidador escribe `ids_alias` en el superviviente de cada
  fusión (219 nodos, 293 alias) y `graph.ts` lo declara en el tipo `NodoGrafo`.
  Su propósito declarado es que una referencia vieja siga resolviendo.
- **Qué pasa hoy**: **ningún código lo lee.** Busqué `ids_alias` en todo
  `web/lib`, `web/app`, `scripts/` y `engine/`: solo aparece en la declaración del
  tipo y en el consolidador que lo escribe. **No existe resolutor.**
  > **CORRECCION DECLARADA, 12 ago 2026: LA PROMESA SI SE CUMPLIO, y esta verificada
  > contra el codigo.** El resolutor **existe**: `web/lib/engine/graph.ts` construye el
  > mapa en **`mapaDeAlias` (linea 100)** y exporta **`resolverId` (linea 131)**, que
  > **camina cadenas de alias** hasta un nodo activo y, si la cadena entera fue
  > retirada, devuelve el eslabon mas reciente que exista. **Lo invocan `etiquetaArbol`
  > (164) y `tituloDeNodo` (172)**, hay un espejo en Python en
  > `scripts/reanclar_por_resolutor.py`, y lo ejercitan `resolutorHistoria.test.ts` y
  > `compass.test.ts`.
  >
  > **AJUSTE DE UNA LINEA sobre el encargo que trajo esta correccion**: aquel citaba
  > `mapaDeAlias` en la **107**; **medido hoy esta en la 100**. La funcion es la misma y
  > el resto de las lineas coincide.
  >
  > **LO QUE QUEDA NO ES CONSTRUIRLO: ES MEDIR POR DONDE PASA.** En produccion,
  > `web/lib` y `web/app` sin tests, hay **42 accesos directos al grafo por id, en 12
  > ficheros, y 9 de esos ficheros manejan ids de origen externo**. Esa es la lista que
  > hay que revisar.
  >
  > **Y LA TABLA DE ALIAS, medida el mismo dia:** **391 alias totales**, **314 a nodo
  > deprecado** (que es su funcion), **CERO colisiones vivas** y **77 huerfanos** a ids
  > inexistentes. **Con cero colisiones vivas, borrar los 77 no puede romper ninguna
  > resolucion buena.**
- **Y hay 77 alias que apuntan a ids que ya no son nodos** (renombres de la era
  de integración de packs: `carta_de_credito` → `carta_de_credito_letter_of_credit`,
  `ceo_guerra_vs_paz` → `ceo_de_guerra_vs_paz`, …). Esos ids **no están en
  `master_graph.json`**. Los 217 deprecados **sí** están (la historia se conservó
  como se ordenó); los renombrados, no.
- **Si nadie lo arregla**: un `project_nodes.node_id` histórico que apunte a un id
  renombrado no resuelve. Cae en `graph[nid]?.titulo_concepto ?? nid` y el usuario
  ve **el id crudo** en su Expediente o su plan. La avería `?? nid` ya cazada
  tiene, entonces, un proveedor de casos que sigue vivo.
- **Además, 7 nodos se listan a sí mismos como su propio alias** (`trilogia_de_juran`,
  `recomendaciones_smart`, …): ruido inofensivo, pero ruido.
  > **CORRECCION DECLARADA, 12 ago 2026: HOY SON CERO.** Remedido sobre
  > `dataset/metadata/master_graph.json`: **ningun nodo, vivo ni deprecado, se lista a
  > si mismo en `ids_alias`**. `trilogia_de_juran`, el ejemplar citado arriba, lleva
  > hoy tres alias y **ninguno es el suyo**.
  >
  > **LA GUARDA DEL CODIGO SE QUEDA Y HACE BIEN**: `mapaDeAlias` filtra `if (a !== nid)`
  > con el comentario *el auto-alias (7 nodos) no dice nada*. **La guarda sigue en pie;
  > la cifra que la motivaba ya no.** Es la diferencia entre una defensa y su
  > ocasion: la ocasion se fue y la defensa se queda.
  >
  > **Y NO CONFUNDIR CON LAS 27 AUTO-ARISTAS**, que son otra cosa y **siguen siendo
  > 27**: aquello son nodos que se apuntan a si mismos por `nodos_previos` o
  > `nodos_siguientes` **via alias propio**, no el auto-alias de este parrafo. El motivo
  > del banco 9.14 queda confirmado, no corregido.
- **Recomendación**: **arreglar ahora.** Dos piezas: (1) un resolutor
  `resolverId(nid, graph)` que consulte los alias, dentro de `graph.ts` para que
  sea puerta única; (2) un chequeo del Gate 0 que exija que todo alias apunte a
  algo resoluble. Los 7 auto-alias se limpian de paso.

## B.4 — El `insert` de `project_nodes` sin `ON CONFLICT`

- **Qué es**: `db.ts:554`. `project_nodes` tiene `UNIQUE(project_id, node_id)` y
  el insert no declara conflicto: un re-insert **lanza**.
- **Qué pasa hoy**: no revienta porque `registrarNodos` filtra por
  `nodosCubiertos()` justo antes. **La protección vive en el código que llama, no
  en el esquema.**
- **Si nadie lo arregla**: dos pestañas cerrando el mismo turno a la vez (o un
  reintento del cliente) leen la misma lista de cubiertos, y el segundo insert
  tira una excepción que sube hasta la ruta. El usuario ve un error al final de
  un turno que ya se completó.
- **Recomendación**: **arreglar ahora, una línea.** `.upsert(..., { onConflict:
  "project_id,node_id", ignoreDuplicates: true })`. Es exactamente el patrón que
  el esquema ya declara.

## B.5 — El techo de 1.000 filas, otra vez

- **Qué es**: **no hay una sola llamada a `.range()` en toda la web.**
  `nodosCubiertos()` (`db.ts:505`) lee `project_nodes` sin paginar.
- **Qué pasa hoy**: nada. El proyecto más grande está muy por debajo de 1.000
  nodos cubiertos.
- **Si nadie lo arregla**: al nodo 1.001 la consulta devuelve 1.000 **sin error**
  y el motor vuelve a ofrecer nodos ya recorridos. Es **la misma avería** que en
  este ciclo reportó 66 visitados donde había 172, ahora en el corazón.
- **Recomendación**: **ficha con umbral**, no arreglo ahora. Lo correcto no es
  paginar por si acaso: es **un chequeo que grite si alguna consulta devuelve
  exactamente 1.000 filas**. Barato, y convierte un techo silencioso en un aviso.

## B.6 — `TODO` / `FIXME` / `HACK` en el motor

**Cero.** Busqué `TODO`, `FIXME`, `HACK`, `XXX`, "por ahora", "de momento",
"provisional", "parche", "temporal" en `web/lib/engine/*.ts`, `compass.ts`,
`db.ts` y `prototipo_motor.py`. Los únicos aciertos son `TODO` en mayúsculas
dentro de frases en español ("en TODO el plan") y `error_temporal`, que es un
tipo legítimo del recorrido.

**Esta es la buena noticia del reporte**: la deuda de este motor no está escrita
en comentarios de disculpa. Está en la forma del código, que es más difícil de
ver y por eso existe esta auditoría.

## B.7 — Las barandas rotas y reparadas: ¿dejaron hermanas vivas?

Revisé las tres que se rompieron en el ciclo del censo:

| baranda | lección | ¿hay hermanas vivas? |
|---|---|---|
| guardia de acentos (rechazaba 39 de 40) | solo palabras **siempre** acentuadas | **NO.** `detectorAcentos.ts` es explícitamente conservador y su regex `(?:cion\|sion)(?![a-záéíóúüñ])` ya excluye los plurales (*acciones*) |
| `sabes` marcado como voseo | voseo es `sabés`, no `sabes` | **NO.** La lista de `revoz_pack.py` es de formas voseadas puras |
| banda de longitud 80-150 sobre nodos existentes | medir contra el original | **NO.** `max(45, 0.65×viejo)` … `min(150, 1.35×viejo+10)` |

Ninguna dejó hermana. La familia entera de "detectar por mención en vez de por lo
que el nodo describe" quedó cerrada con ley del auditor.

---

# (C) LOS CAMINOS SIN TEST

Cruce de los módulos contra las cuatro capas. Nombrado por camino de usuario.

**Primero, el marco honesto**: existe una **quinta capa**, los arneses de vuelo
(`vuelo.ts`, `vuelo_beta.ts`, `vuelo_cuenta.ts`, `vuelo_preview.ts`,
`vuelo_numeros.ts` y 8 gates), que **sí** cubre casi todo lo de abajo. Pero
necesita servidor vivo + Supabase real + claves, **no corre en CI**, y por la
memoria del proyecto **no se ha corrido en vivo desde la campaña de Mundos de
Protección**. Las cuatro capas verdes de las que hablamos **no la incluyen**.

## C.1 — La entrevista completa
**Cubierta.** `recorrido.test.ts` (288 l), `interprete.test.ts` (229 l),
`session/start/route.test.ts`, `session/[id]/turn/route.test.ts`.

**El hueco**: `clasificar.ts` **no tiene test propio**, y el comentario de
cabecera de `session/start/route.test.ts` afirma que *"clasificar.ts ya tiene su
propia cobertura vía interprete.test.ts"*. **Eso no es cierto**: `clasificar.ts`
no aparece en ningún test salvo como mock. Es un comentario que reclama una
cobertura que no existe — la clase exacta de test que envejece verde.

> **Si la clasificación de entrada se rompe, el usuario entra por la puerta
> equivocada, la entrevista entera va sobre el tema equivocado, y nadie se
> entera** — porque el `catch` devuelve `entrySeeds[0]`, que siempre es una
> puerta válida.

## C.2 — La reelección
**Cubierta con datos sintéticos** (`reeleccionPuerta.test.ts`, 199 l), pero
**con el grafo real la regla ya no se puede ejercer** (ver B1.1). Es decir: el
test prueba que el código hace lo correcto cuando hay una semilla fuera, y en
producción nunca la hay.

> Si la reelección se rompe en Calidad, **el usuario no ve nada**: recibe un nodo
> vecino en vez de una puerta, la conversación sigue, y el único síntoma es que
> el mundo se siente menos afilado.

## C.3 — El redactor y su autodeclaración
**Bien cubierto**: `planRedactor.test.ts` (395 l), `sensores.test.ts`,
`test_procedencia_etapas.py`.

**El hueco**: el redactor **streamea** desde la ruta del plan; el test cubre el
ensamblado y el parseo, no el streaming. Si el stream se corta a media redacción,
lo que sostiene el plan es la red de reembolso de la ruta (que sí tiene test).

## C.4 — El scheduler
**Cubierto**: `estimacion.test.ts` (191 l) + `empaquetado`, `fechasBase`,
`hitosEspacio`, `palancas`, todos con test.

**El hueco**: `estimacion.ts:142` hace `catch { continue }` sobre cada corrida de
la mayoría-de-3. **Nada prueba el caso de 2 de 3 corridas perdidas.** Con las 3
perdidas no hay votos y la banda no nace; con 1 perdida la mayoría se decide
entre 2, que no es mayoría de 3.

> Si dos corridas fallan a la vez, **el usuario recibe bandas decididas por una
> sola opinión del modelo presentadas como si fueran el consenso de tres.**

## C.5 — La protección
**Cubierto en piezas**: `snapshotProyecto.test.ts` (265 l),
`enlazador.test.ts` (273 l), `reformuladorProteccion.test.ts` (287 l).

**El hueco de camino**: la ruta `world/[pack]/start` **no tiene test de ruta**, y
es donde el snapshot, el reformulador y el candado de secuencia se encuentran.
Y por memoria del proyecto, **la campaña de protección se cerró sin corrida en
vivo**. Es el camino con más código nuevo y menos verificación de extremo a
extremo.

## C.6 — Los créditos y las murallas
**El dinero está bien**: `creditos.test.ts`, RPC atómicas en Postgres,
idempotencia por `plan:{sessionId}`, red de reembolso post-cobro con log. La
ruta que cobra (`session/[id]/plan`) tiene test.

**Los huecos de ruta**: sin test propio quedan `account/saldo`, `cuenta/2fa/*`
(6 rutas), `cuenta/eliminar`, `cuenta/seguridad`, `auth/*` (5 rutas),
`calendar/feed/[token]` **(ruta pública, autenticada por HMAC)**,
`world/[pack]/unlock`, `packs/interes`. **27 de las 40 rutas de la API no tienen
archivo de test**; el vuelo cubre buena parte, y el vuelo no corre en CI.

> Si el HMAC del feed de calendario se rompe hacia el lado permisivo, **cualquiera
> con la URL ve el calendario de cualquiera y nadie se entera**: es una ruta
> pública por diseño, sin sesión que audite.

## C.7 — El cableado de mundos
**Cubierto**: `catalogoMundos.test.ts`, `semillasDePack.test.ts`,
`puertaUnica.test.ts`, `espacios.test.ts`, `previewMundos.test.ts`, y el Gate 0
vigila semillas, puentes, fantasmas y brecha.

**El hueco**: `diagnosticoMundo.ts` **no tiene test**. Es el redactor que produce
lo primero que un usuario lee de un mundo que está evaluando comprar.

> Si el diagnóstico degrada, **el usuario lee un texto plano justo en el momento
> de decidir si paga**, y el único síntoma es que no compra.

## C.8 — Resumen de módulos sin test propio

`clasificar.ts` · `diagnosticoMundo.ts` · `puertaAvanzada.ts` · `constants.ts` ·
`tokens.ts`

Los dos últimos son datos y un tokenizador de 22 líneas usado por 5 módulos que
sí se prueban: su cobertura es indirecta y suficiente. Los tres primeros **toman
decisiones llamando al modelo** y ninguno tiene prueba propia.

---

# (D) LOS PUNTOS DE FALLO SILENCIOSO

## D.1 — Fail-open **DISEÑADO** (correcto, documentado, con aviso)

| sitio | qué hace | por qué está bien |
|---|---|---|
| `db.ts:542` — el diario `node_visits` | `console.warn` y sigue | *"un sensor que rompe lo que mide deja de ser un sensor"*. Documentado y **testeado** en `sensores.test.ts` |
| `interprete.ts:509` — respaldo tier-2 | cae a afinidad léxica y **registra el evento** | el único de la lista que **deja rastro estructurado** |
| `recorrido.ts:224` — brújula caída en la oferta | cae al nombre humano de la familia | comentado |
| `reporte.ts:216` | cae a `reporteOffline()` | el usuario recibe su reporte |
| `estimacion.ts:142` | pierde una corrida y sigue | *"sin votos, sin romper el plan"* |
| `rateLimit` sin credenciales | desactiva el límite con aviso | *"nunca deben romper el flujo por configuración faltante"* |

## D.2 — Fail-open **ACCIDENTAL** (el catálogo de verdad)

### **D2.1 — `registrarBitacora`: un `catch` decorativo** ← el más limpio de demostrar
```ts
try {
  await supabase.from("project_bitacora").insert({ ... });
} catch { /* la bitácora nunca bloquea la acción del usuario */ }
```
`supabase-js` **no lanza** en error de consulta: resuelve con `{ error }`. Este
`catch` **no se ejecuta nunca** y el `error` **no se lee nunca**. Es el único
punto de `db.ts` que no desestructura `error` — los otros 30 sí.
> La bitácora puede llevar semanas sin escribir una sola fila —RLS mal, columna
> renombrada, tabla llena— y **el comentario diciendo que está protegido**.

### **D2.2 — `obtenerPlanCoreVigente`: "no hay" y "falló" son la misma respuesta**
```ts
const { data: sesiones } = await supabase.from("sessions")...   // sin error
const { data } = await supabase.from("plans")...                // sin error
return ((data ?? [])[0])?.id ?? null;
```
Dos consultas cuyo error se descarta. `null` significa *"este proyecto no tiene
plan de núcleo, no hay nada que proteger"* — y también *"la base falló"*.
> Un hipo de base en el momento de entrar a un mundo de protección hace que el
> producto **crea que el usuario no tiene plan**: el enlace no se hace y el plan
> del mundo sale sobre el vacío, en vez de sobre sus actividades reales. Que es
> justo la cosa que la campaña de protección existió para lograr.

### **D2.3 — La brújula avisa una vez por proceso y nunca más**
```ts
let avisoImpreso = false;
function avisar(motivo) { if (!avisoImpreso) { avisoImpreso = true; console.warn(...); } }
```
`avisoImpreso` es de módulo. En un proceso Node de larga vida, **el primer fallo
imprime y todos los siguientes son mudos**. Y el aviso va a `console`: no hay
telemetría, no hay evento, el usuario no ve nada.
> La navegación semántica —el salto que hace que la entrevista se sienta lista—
> puede estar caída durante horas. Las sesiones se completan, los planes salen,
> y **la única diferencia es que son peores.**

### **D2.4 — El techo de 1.000 filas** (ver B.5): "hay exactamente 1.000" y "hay más" son indistinguibles.

### **D2.5 — `contarEnUpstash`: el código contradice su propio contrato**
El docstring dice *"Upstash caído no debe tumbar el producto: se permite y se
registra"*. El código maneja `!resIncr.ok`, pero **el `fetch` no está en
`try/catch`**: un fallo de DNS o un timeout **lanza**, y ningún llamador lo
atrapa.
> Upstash con problemas de red y **todo arranque de sesión responde 500**. Es el
> reverso de los demás: falla ruidoso donde prometió fallar suave. Lo listo aquí
> porque la avería es la misma —contrato y código no dicen lo mismo— aunque el
> síntoma sea el contrario.

## D.3 — Valores por defecto que enmascaran ausencia

| sitio | el default | qué esconde |
|---|---|---|
| `graph.ts:81` | `?? nid` | id crudo en pantalla (**ya cazado**; B.3 muestra que sigue habiendo proveedores) |
| `recorrido.ts:407` | `?? nidActual` | **hermana viva** del anterior, en el título que va al prompt del turno |
| `juezSesion.ts:56` | `?? nid` | **hermana viva**, en el material que juzga la calidad de la sesión |
| `clasificar.ts:53` | `entrySeeds[0]` | puerta equivocada indistinguible de puerta elegida |
| `puertaAvanzada.ts:116` | `candidatosIds[0]` | ídem, en seguimiento |
| `planRedactor.ts:245` | `autodeclaracion: null` | *"el modelo no autodeclaró"* y *"el JSON venía roto"* son lo mismo |

Las dos hermanas vivas del `?? nid` son hallazgo nuevo de esta auditoría.

## D.4 — Respuestas del modelo que se parsean sin verificar forma

`enlazador.ts:62` y `estimacion.ts:81` hacen `JSON.parse` sobre `texto.match(/\[[\s\S]*\]/)`
y **devuelven `[]` si falla**. Los dos filtran después elemento a elemento, así
que un elemento malformado se descarta en silencio.
> Un lote de estimación donde el modelo cambió el nombre de un campo devuelve
> **cero votos, no un error**. La banda sale de los otros dos lotes y nadie sabe
> que se decidió con un tercio menos de opinión.

## D.5 — Funciones que devuelven vacío sin distinguir "no hay" de "falló"

`embedQuery` → `null` · `parsearEnlaces` → `[]` · `parsearLote` → `[]` ·
`obtenerPlanCoreVigente` → `null` · `evaluarCalidadSesion` → `calidad: null` ·
`clasificarTipoOferta` → `{tipo: null, unidad: null}`

**Seis funciones del motor** cuyo valor de "todo bien, no había nada" es idéntico
a su valor de "reventó". Ninguna de las seis emite evento.

---

# (E) MI VEREDICTO — las diez primeras, por daño al usuario

| # | pieza | daño si se rompe | costo | ¿toca producción viva? |
|---|---|---|---|---|
| **1** | **`ids_alias` sin resolutor** (B.3) | el usuario ve **ids crudos** en su plan y su Expediente; la historia que se juró conservar no resuelve | **medio** — resolutor en `graph.ts` + chequeo de Gate 0 + test | sí: lectura del grafo |
| **2** | **`obtenerPlanCoreVigente` traga errores** (D2.2) | el plan de un mundo de protección sale **sobre el vacío** en vez de sobre las actividades reales | **bajo** — leer `error` y lanzar; 2 consultas | sí: mundos de protección |
| **3** | **La brújula muda tras el primer aviso** (D2.3) | la navegación semántica cae **horas** sin síntoma; los planes salen peores | **bajo** — evento por fallo, no flag de módulo | sí: cada turno |
| **4** | **`registrarBitacora`, `catch` decorativo** (D2.1) | la bitácora deja de escribir y **el comentario dice que está protegida** | **muy bajo** — 3 líneas + test | sí |
| **5** | **`project_nodes` sin `ON CONFLICT`** (B.4) | excepción al cerrar un turno **ya completado**, con dos pestañas o un reintento | **muy bajo** — una línea | sí: cada turno |
| **6** | **`contarEnUpstash` contradice su contrato** (D2.5) | Upstash con fallo de red → **500 en todo arranque de sesión** | **muy bajo** — envolver el `fetch` | sí: cada arranque |
| **7** | **`clasificar.ts` sin test + comentario que miente** (C.1) | entrevista entera **sobre el tema equivocado**, sin síntoma | **bajo** — un test + corregir el comentario | no: solo tests |
| **8** | **Las dos hermanas del `?? nid`** (D.3) | ids crudos dentro del **prompt del turno** y del **juez de sesión** | **bajo** — canalizar por una sola función de título | sí |
| **9** | **Los gemelos cirílico e inglés del dataset** (B.2) | clave que *se ve* correcta y no lo es; diagnóstico casi imposible | **muy bajo** — borrar 2 claves + lista blanca en Gate 0 | no: solo dataset |
| **10** | **El fixture de reelección escrito a mano** (B1.2) | el test cae de golpe en la próxima fusión y nadie sabe por qué | **muy bajo** — calcular el fixture | no: solo tests |

**Justo debajo del corte, y por qué**: la **reelección inoperante en `quality`**
(B1.1) hace más daño que varias de arriba, pero arreglarla es podar el pack más
denso — mueve el vecindario justo antes de la beta, que es la cosa que los tres
argumentos de espera del núcleo prohíben. **Ficha, post-beta.** Y el techo de
1.000 filas (B.5) no está cerca de morder: lo que corresponde es el chequeo que
grite, no la paginación preventiva.

**Lote sugerido para el primer arreglo** (si el auditor lo aprueba así): las
**#2, #3, #4, #5, #6** son todas de costo muy bajo o bajo, todas de la misma
familia —*el error existe y nadie lo mira*— y ninguna cambia comportamiento
correcto: solo hacen ruido donde hoy hay silencio. Es el lote que mejor encarna
el canon de **fallar ruidoso, no mentir calladito**, y el que deja el terreno
limpio para medir todo lo demás.

---

## Lo que esta auditoría dice del motor, en una línea

**No encontré un motor descuidado: encontré un motor que sabe fallar y no sabe
avisar.** No hay un solo `TODO` de disculpa, el dinero es atómico, las puertas
únicas están puestas y tienen guardián, y las barandas que se rompieron en el
ciclo se repararon sin dejar hermanas. Lo que falta es casi todo del mismo tipo:
**seis funciones que devuelven vacío sin decir por qué, un `catch` que no puede
ejecutarse, un aviso que se calla tras la primera vez, y un mecanismo de alias
que se escribe y no se lee.** Son baratas de arreglar y son justo las que
convierten una beta en una beta medible.
