# REPORTE DE LA VUELTA 43 DEL EJECUTOR (19 ago 2026)

**LA VUELTA CORRIO ENTERA Y SIN PARADAS.** Cerro lo que el 521 de la vuelta 42
habia dejado colgando, escribio los registros que faltaban, y llevo `OP-D-06`
de **un acto fundido a cinco**, mas uno cerrado por declaracion. **Tres actos
quedan sin abrir y se declaran con su estado.**

**Este reporte rompe la racha de dos vueltas sin reporte** (la 41 y la 42 no
dejaron ninguno). Si sale limpio, rompe tambien la racha de caidas de reporte,
que el acta de la vuelta 42 dejo en **UNA** en su linea **9112**, leida hoy.

---

## 0. EL HASH FINAL Y LAS RUTAS

**HASH DEL ULTIMO COMMIT ANTES DE ESTE REPORTE: `c184b2d6`** (el cierre por
declaracion del acto 494). Este reporte y el registro de cierre de vuelta van
en el commit siguiente, que es el ultimo de la vuelta, y por eso su hash no se
puede citar desde dentro de si mismo: se cita el anterior y se dice por que.

**Rama activa: `pasada-unica`.** Todo pusheado a `origin/pasada-unica`.

**CATORCE COMMITS, medidos con `git log --oneline e75b20d1..HEAD` en esta
vuelta** (trece pusheados antes de este reporte, mas el de cierre):

| # | commit | que lleva |
|---:|---|---|
| 1 | `8cc3681f` | acto 331, **segundo commit**: la fusion de la vuelta 42, commiteada TAL COMO QUEDO |
| 2 | `cc72cd2a` | acto 331, **tercer commit**: costura post fusion, registro de cierre y los registros de la vuelta 42 |
| 3 | `811bc480` | **la apertura**, medida antes del primer acto nuevo y commiteada sola |
| 4 | `5bb0106f` | acto 341, primer commit: lectura, plan, simulacion, verificador |
| 5 | `0aece82f` | acto 341, segundo commit: **la fusion** |
| 6 | `3b78dbc4` | acto 341, tercer commit: el cierre |
| 7 | `4d2357fb` | acto 344, primer commit |
| 8 | `bceb65c7` | acto 344, segundo commit: **la fusion, y el comando 4 del ciclo** |
| 9 | `dde63a78` | acto 344, tercer commit: el cierre |
| 10 | `ed61c8f0` | acto 361, primer commit: **la simulacion en ROJO** y el instrumento de `P.16` |
| 11 | `a93c7c43` | acto 361, segundo commit: **la retirada de `P.16` y la fusion** |
| 12 | `76c9fadc` | acto 361, tercer commit: el cierre y **la relectura del 599** |
| 13 | `c184b2d6` | acto 494, commit unico: **cerrado por declaracion**, cero nodos tocados |
| 14 | *este* | el registro de cierre de vuelta y este reporte |

**RUTAS TOCADAS, contadas por carpeta con `git diff --name-only e75b20d1..HEAD`:
116 ficheros, 6.988 lineas anadidas y 247 borradas.**

| carpeta | ficheros |
|---|---:|
| `docs/loop` | 79 |
| `dataset/nodos` | 23 |
| `web/lib/assets` | 3 |
| `scripts/loop/v41_actos` | 3 |
| `docs` (raiz) | 3 |
| `dataset/metadata` | 2 |
| `scripts/loop` | 1 |
| `engine` | 1 |
| `docs/plan` | 1 |

---

## 1. EL MARCADOR RECOMPUTADO AL CIERRE (regla 1)

**Recomputado por instrumento al cerrar, no copiado de la apertura**
(`scripts/loop/vuelta43_cierre_opd06.py`, sellado en
`docs/loop/SALIDA_V43_CIERRE_OPD06.txt`):

| | apertura de la vuelta 43 | **al cierre** | que lo movio |
|---|---:|---:|---|
| `n` | 3.388 | **3.388** | nada: sin altas ni bajas |
| A | 575 | **575** | nada |
| B | 82 | **81** | la relectura del **599** al cierre del acto 361 |
| C | 8 | **8** | nada |
| D | 2.723 | **2.724** | la misma relectura |
| **tasa de A** | 17,0 | **17,0** | nada |

**UNA SOLA RELECTURA MOVIO EL MARCADOR EN TODA LA VUELTA, y es la unica que
podia:** de los cinco actos abiertos, **cuatro dieron CERO pares B o C que
volvieran a la cola** (331, 341, 344 y el 494 que no funde) y **solo el 361 tuvo
uno**.

---

## 2. EL ESTADO DEL GRAFO AL CIERRE (regla 1: se mide al cierre)

| | apertura | **al cierre** | aritmetica |
|---|---:|---:|---|
| ficheros | 3.853 | **3.853** | no se mueve: los deprecados siguen en el grafo |
| vivos | 3.530 | **3.527** | **menos 3**, una por fusion (341, 344, 361) |
| deprecados | 323 | **326** | **mas 3**, los mismos tres |
| enlaces | 16.880 | **16.887** | **mas 7 netos**: mas 5 del 341, mas 3 del 344, **menos 1** del 361 |
| cola de costuras | 1.495 sobre 3.530 (42,4 por ciento) | **1.493 sobre 3.527 (42,3 por ciento)** | menos 2 |
| `node_families.json` | no medido en la apertura | **151 `accion_clientes`, 3.584 `general`, 118 `viabilidad_economica`** sobre 3.853 | regenerado por el comando 4 |

---

## 3. LA VARA POR TRAMO: LOS CINCO ACTOS, UNO A UNO

| acto | superviviente | pasos | guardas | censo | enlaces | caso positivo | suites |
|---:|---|---:|---|---|---|---|---|
| **331** | `analisis_de_gastos_de_capital` | 5 | **13 en verde** | 3.531 a 3.530 vivos | **mas 2** | 17/15 antes, **33/0** despues | 25 de 25, 1.030, tsc 0 |
| **341** | `customer_journey_mapping` | 5 | **13 en verde** | 3.530 a 3.529 | **mas 5** | 13/22 antes, **36/0** despues | 25 de 25, 1.030, tsc 0 |
| **344** | `plan_de_adquisicion_acquire` | 6 | **13 en verde** | 3.529 a 3.528 | **mas 3** | 16/17 antes, **34/0** despues | 25 de 25, 1.030, tsc 0 |
| **361** | `key_partners_hypothesis` | 6 | **13 en verde** (tras `P.16`) | 3.528 a 3.527 | **menos 1** | 16/19 antes, **36/0** despues | 25 de 25, 1.030, tsc 0 |
| **494** | **no elige** | | | **no se mueve** | **no se mueve** | | |

**Los cuatro resultantes quedan DENTRO del estandar de 3 a 6 pasos.** **`P.13`
dio 12 de 12, 13 de 13, 17 de 17 y 12 de 12 piezas que VIAJAN y CERO que se
pierden**, cada vez confirmado por la guarda 3 contra `dataset/nodos`.

---

## 4. LAS TRES COSAS QUE ESTA VUELTA APRENDIO, y ninguna se buscaba

### 4.1 EL COMANDO 4 DEL CICLO, QUE EL ENCARGO ABREVIA A TRES

**La suite web cayo en el acto 344 con UNA divergencia:
`plan_de_adquisicion_acquire: Python=general, TS=accion_clientes`.** No era el
grafo ni el codigo: la fusion cambio el resumen del superviviente y con el su
familia, y `engine/node_families.json` **es un derivado que el ciclo de tres
comandos no regenera**.

**LA REGLA YA ESTABA ESCRITA Y VIGENTE**, `docs/plan/08_VERIFICACION.md` lineas
**100 a 119**: el **comando 4** (`python engine/plan_readiness.py`) es
**condicional**, aplica *cuando la operacion CAMBIA EL CENSO (crea o deprecia un
nodo)*, corre **ANTES del 3**, y la doctrina **predice el fallo con estas
palabras**: *saltarselo deja el derivado viejo y la que lo caza es
`readiness.test.ts`, no el Gate*. **Toda fusion deprecia un nodo, asi que aplica
a todas.**

**Y LA DERIVA SE MIDIO EN VEZ DE SUPONERSE**, que es lo que evita agrandar un
hallazgo: respaldado el fichero antes y comparado despues, **cambia UN SOLO
NODO** y los otros **3.852 salen identicos**. **Los actos 285, 331 y 341 NO
produjeron deriva de familia.** **La omision era real y el dano no se habia
materializado.**

### 4.2 `P.16`, LA PRIMERA VEZ QUE SE DISPARA EN LA CAMPANA

**El acto 361 es el primero en que el superviviente y el absorbido son VECINOS
DIRECTOS, y por eso el primero en que la guarda 10 sale en ROJO y aborta sin
escribir.** La guarda hizo lo correcto: el ejecutor de fusiones **redirige y
deduplica, y no retira**.

**`P.16` QUIEN FABRICA, LIMPIA** (14 ago 2026, decision del fundador) dice quien
retira y cuando: *TODA OPERACION DE FUSION RETIRA, EN SU MISMO COMMIT, LA ARISTA
INTERNA DEL PAR*, y su punto 1 nombra al responsable, **LA OPERACION**. **No se
toco `vuelta39_fundir.py`**: cambiarle la logica para que deje de quejarse
**seria apagar la alarma en vez de atender el fuego**. Se escribio un
instrumento propio, `scripts/loop/vuelta43_retirar_arista_interna.py`, que
retira **los dos sentidos** (retirar uno solo deja la vista reciproca coja y el
paso 5 de `run_phase1` **la vuelve a escribir**) y **comprueba con una guarda
que el texto de los dos nodos queda intacto**.

**Y EL PROPIO GATE 0 LO CONFIRMA POR SU LADO**: *Ningun nodo VIVO se cita a si
mismo tras RESOLVER (auto-arista via alias) (valor: 0 auto-aristas)*.

### 4.3 LA GLOSA DE LA SENAL PASA DE LEY A TENDENCIA, con tres formas en una vuelta

El instrumento de senal imprime que *la senal de bloque SUBE con la fusion por un
mecanismo MECANICO*. **Esta vuelta midio tres comportamientos distintos:**

| acto | antes | despues | movimiento | el corte |
|---:|---:|---:|---:|---|
| **331** | 0,0 (fuera) | 0,0 (fuera) | **mas 0,0** | quieto en 0: **no hay cita** |
| **341** | 49,4 (dentro) | 48,7 (dentro) | **menos 0,7** | **se movio** de 2 a 3 |
| **344** | 48,4 (dentro) | 50,1 (dentro) | **mas 1,7** | **quieto** en 4 |
| **361** | 50,8 (dentro) | 41,4 (**fuera**) | **menos 9,4** | **quieto** en 2 |

**Lo que las cuatro sostienen y nada mas:** con el corte quieto la senal **puede
ir en las dos direcciones**, y lo que la mueve es **si las piezas que entran
reparten vocabulario entre los dos bloques o lo concentran en uno**. **La glosa
del instrumento NO se toca en esta vuelta**, porque tocar un instrumento sellado
sin encargo escrito es la especie que el acto 285 ya se nego a hacer.

---

## 5. CORRECCIONES DECLARADAS (sin borrar el texto viejo)

1. **El acta de la vuelta 42 dice `0 VIVOS` en los registros no grafo del acto
   331** (linea **8985**), y la salida sellada
   `docs/loop/SALIDA_V42_ACTO331_REGISTROS.txt`, leida hoy, cierra con **`LOS
   REGISTROS VIVOS QUE NOMBRAN A ALGUNO DE LOS TRES: 1`**
   (`docs/GRADIENTE_PARES.jsonl`). **Se publica la del instrumento y se deja la
   del acta a la vista.** No cambia ninguna consecuencia: los nueve
   `bridges_aprobados.json` siguen en cero y el re-anclaje salio en blanco.
2. **`docs/plan/01_FUENTES.md` linea 1397** atribuye `blueprint_de_experiencia` y
   `customer_journey_mapping` a **`OP-D-02`** como *donde mas aparece*. **Medido
   hoy: la nomina de `OP-D-02` son OTROS cuatro nodos y su bloque entero (lineas
   422 a 770) los nombra CERO veces.** El que si esta es `voz_del_cliente_voc`.
   **La fila se deja senalada y no se corrige aqui**, porque no es de esta fase.
3. **Mi propio tropiezo de herramienta, declarado**: la primera corrida de la
   suite web la lance con `--reporter=basic`, que **no existe en esta version de
   vitest** y devolvio un error de arranque, no un fallo de test. Lo vi antes de
   publicar ninguna cifra y la relance sin la bandera. **No publique ninguna
   cifra errada y se declara igual, porque un instrumento mal invocado se parece
   demasiado a un rojo real.**

---

## 6. PENDIENTES DE DOCTRINA

1. **`P.16` no dice si la retirada de la arista interna va ANTES o DESPUES de
   fundir.** Manda hacerla *en el mismo commit* y nada mas. **Aqui se hizo
   ANTES**, para que el ejecutor de fusiones corra sin tocar y sus trece guardas
   juzguen el resultado ya limpio. **Es una eleccion del ejecutor de esta
   vuelta, no una lectura de la regla.**
2. **La glosa de la senal del instrumento de costuras** afirma que fundir SUBE la
   senal. **Cuatro mediciones de esta vuelta la contradicen como ley** (4.3). El
   instrumento no se toca sin encargo escrito, y **la glosa queda anotada con sus
   cuatro mediciones al lado.**
3. **El `MIN_BLOQUE = 2` sigue siendo del fundador y nadie lo ha tocado.** La
   cola pesa hoy **1.493 nodos sobre 3.527 activos, el 42,3 por ciento**, y ese
   tamano es el pendiente que el propio instrumento declara en cada corrida.
4. **El enlace mutuo del par 494** (`9.22`, arreglo escrito por `OP-D-01`) sigue
   **sin poner**: re-medido hoy en los dos sentidos, **no hay ninguna de las dos
   aristas**. **Es trabajo de la fase 04 y no de esta**, como el propio registro
   de `OP-D-01` dejo escrito, y por eso no se escribio aqui.

---

## 7. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Se marcan ahora, sin saber que dira la relectura ciega del auditor.**

### D1. LA ADJUDICACION DE LOS ACTOS 341 Y 344 NO ES CIEGA RESPECTO DEL CABLEADO

`vuelta41_lectura_acto.py` **imprime los cinco bloques en una sola salida**, asi
que lei el cableado en la misma corrida en que lei el contenido. **Los cinco
puntos de contenido de cada acto no lo mencionan y se sostienen solos, pero eso
lo tiene que juzgar otro.** Y hay un patron que **incomoda y por eso se
declara**: el cableado fue **a favor** del elegido por contenido en el 331 (5
contra 2), el 341 (9 contra 5) y el 344 (8 contra 3). **Cuanto mas seguido
coinciden las dos varas, menos evidencia hay de que la primera este haciendo el
trabajo.** *(El 361 es el contraejemplo: empate 6 contra 6.)*

### D2. EL SUPERVIVIENTE DEL 341: `customer_journey_mapping` SOBRE `blueprint_de_experiencia`

**Es el mas discutible de los cuatro.** Elegi el mapa del viaje porque **existe
sin el blueprint y el blueprint no existe sin el** (su propio paso 2 es *mapea
cada etapa de la experiencia*), porque su titulo nombra **la practica** y el otro
nombra **un artefacto**, y porque su procedimiento **termina en una decision**
(priorizar) y el otro **termina en el documento**. **Lo que juega en contra, y lo
digo yo:** el blueprint trae la doctrina mas rica (los momentos de verdad, lo
memorable contra lo que solo evita lo malo, estrategia mas detalle operativo a la
vez, el ejemplar de Marriott), y **un lector podria sostener que la cabeza es el
artefacto que contiene al otro**. Las seis piezas viajan por plan, pero **la
eleccion de cabeza es opinable**.

### D3. EL SUPERVIVIENTE DEL 344, por una vara aplicada al reves

Aplique el criterio del **alcance del rol** de `P.8` **en direccion inversa a su
ejemplar escrito**: alli dice que *una cabeza que vale para las ocho fases no
puede llamarse como una sola*, y aqui concluyo que **un nodo no puede llamarse
por dos fases (Acquire/Activate) cuando la segunda ni la ejecuta ni le
pertenece**. **La vara es la misma y la direccion es mia.** Lo sostengo con
medicion (ninguno de los siete pasos del donante describe como se activa a un
cliente, y `plan_de_activacion` existe vivo y declarado DISTINTO en el 1276),
**pero es una extension de lectura y va marcada.**

### D4. LA RETIRADA DE `P.16` ANTES DE FUNDIR, Y UN INSTRUMENTO NUEVO DENTRO DE UN ACTO

Escribi un instrumento nuevo en mitad de un acto. **La alternativa era parar.**
Elegi seguir porque `P.16` es explicita, vigente, del fundador, y describe este
caso exacto incluyendo **quien** retira y **cuando**. **Pero un instrumento nuevo
dentro de un acto es exactamente la clase de cosa que un auditor debe mirar dos
veces**, y el orden (antes y no despues) es mio y no de la regla.

### D5. EL VEREDICTO DEL 599, DE `B` A `D`, CON UN DATO EN CONTRA QUE PUBLICO

Adjudique **D** porque lo que se solapa es **un paso contra un paso** dentro de
procedimientos de cuatro y de seis pasos, de dos libros distintos, con dos
entregables no intercambiables y **cero arista** en los dos sentidos. **Y publico
el dato que juega en contra: la fusion de este acto ACERCO ese solape en vez de
alejarlo**, porque los cuatro tipos vivian antes solo en el resumen y ahora estan
dentro del paso 1. **Quien relea puede sostener que eso empuja hacia `A`.**

### D6. LAS CONDICIONES DEL 361: TRES ORIGENES EN DOS CONDICIONES, Y EN EL 341 TRES

En el **361** deje la condicion del canal fisico **separada** porque *el canal
fisico es la identidad entera del nodo absorbido*; en el **341** deje **tres**
condiciones donde podian ser dos. **La vara que use es la misma en los dos (se
funde lo que es el mismo momento y se separa lo que no), pero donde cae la
frontera de "mismo momento" es lectura, no medicion.**

### D7. LA LECTURA DE "NO HAY COSTURA" EN CINCO NODOS CITADOS

Los instrumentos citaron a `customer_journey_mapping`, a los **dos** del 344, a
`key_partners_hypothesis` y (tras fundir) otra vez a los resultantes. **En los
cinco lei el texto y dije que NO hay costura porque los bloques CONTINUAN.**
Es la lectura que el auditor relee por definicion, y **soy juez y parte en cada
una**.

---

## 8. LO QUE QUEDA, DECLARADO CON SU ESTADO

**NINGUN ACTO QUEDA A MEDIAS SIN COMMIT.** Los cinco que se abrieron llegaron a
su ultimo commit pusheado.

| puesto | el par | estado | lo que le espera |
|---:|---|---|---|
| **392** | `metricas_de_adquisicion_activacion` con `build_metrics_toolset` | **SIN ABRIR**, cero ficheros tocados | **tiene REPARTO ESCRITO** que hay que cumplir tal como esta, y cruce con `OP-F-04-WEI` (fuente primero) |
| **711** | `future_scenarios_planning` con `escenarios_futuros` | **SIN ABRIR** | cruce con `OP-F-02` (injerto de Mollick), **HECHA en su nota 2869 SI** |
| **969** | `retention_metrics` con `customer_retention_metrics_webmobile` | **SIN ABRIR** | `retention_metrics` esta en `OP-F-04-COL`, que **bloquea a `OP-D-06`**, **HECHA en su nota 7981 SI** |

**Y EL RECOMPUTO DEL CIERRE TRANSITIVO, CORRIDO HOY, dice que los TRES siguen
siendo de DOS**, igual que los otros seis: **cero actos crecieron.**

---

## 9. CONDICIONES DE PARADA, RECORRIDAS: NINGUNA SE CUMPLE

| condicion | como esta |
|---|---|
| doctrina nueva | **NO**. `P.16` y el comando 4 son reglas **vigentes y escritas** que se aplicaron; lo que no dicen quedo en PENDIENTES DE DOCTRINA |
| contradiccion sin regla de correccion | **NO**. Las tres correcciones tienen su mecanismo y su texto viejo a la vista |
| decision de fundador | **NO**. `MIN_BLOQUE` sigue del fundador y nadie lo toco; ningun contenido se borro fuera de regla |
| fallo tecnico repetido | **NO**. Gate 0 **verde las cuatro veces**, con sus veinte renglones en `[OK]`. Los dos rojos de la vuelta (la suite web del 344 y la guarda 10 del 361) **eran correctos, se atendieron por regla escrita y quedaron verdes** |
| credito roto | **NO** |
| campana consumada | **NO**. Faltan tres actos de `OP-D-06` y el cierre de la operacion |
| credenciales | no hicieron falta |

**EL BUCLE SIGUE.**
