# REPORTE DE LA VUELTA 44 DEL EJECUTOR (19 ago 2026)

**LO PRIMERO, porque es lo que la vuelta hizo: `OP-D-06` QUEDA CERRADA.** Los tres actos que faltaban (**392**, **711** y **969**) se ejecutaron enteros con sus tres commits cada uno, y la operacion se cerro con su recomputo, sus nueve pares releidos, su verificacion punto por punto, su estado recomputado al cierre y su **REGISTRO DE OPERACION HECHA** escrito en la nota.

**Y LO SEGUNDO, porque es una parada y no se esconde al final:** la vuelta **NO abre la operacion siguiente**. El encargo lo autoriza expresamente (*si su texto no alcanza para ejecutarse sin decidir, PARAS y la traes*), y las tres candidatas se leyeron enteras antes de tocar nada. **Va en la seccion 9 con las tres medidas al lado.**

**Este reporte cubre la vuelta entera.** El anterior, el de la vuelta 43, fue **el primero que salio limpio contra la corrida completa del auditor** y rompio la racha de caidas de reporte.

---

## 0. EL HASH FINAL Y LAS RUTAS

| | |
|---|---|
| rama | `pasada-unica` |
| **ultimo commit antes de este reporte** | **`9a09e8d7`** (el cierre de `OP-D-06`) |
| commit de partida | **`ea44b928`** (el acta de la vuelta 43 del auditor) |
| commits de la vuelta | **DOCE**, sin contar el de este reporte |
| arbol | limpio y todo pusheado a `origin/pasada-unica` antes de escribir esto |

**`git diff --shortstat ea44b928..9a09e8d7`: 101 ficheros, 6.596 anadidas, 183 borradas.** El conteo por carpeta, entero:

| carpeta | ficheros |
|---|---:|
| `docs/loop` | 68 |
| `dataset/nodos` | 19 |
| `scripts/loop/v41_actos` | 3 |
| `docs` raiz | 3 |
| `web/lib/assets` | 2 |
| `scripts/loop` | 2 |
| `docs/plan` | 2 |
| `dataset/metadata` | 2 |
| **total** | **101** |

**LOS DOCE COMMITS, en orden:**

| # | hash | que hizo |
|---:|---|---|
| 1 | `62973381` | **TAREA 1**: los registros de la auditoria de la 43 y **la correccion encargada de la glosa de la senal** |
| 2 | `ecc39804` | **la apertura**, medida antes del primer acto nuevo y **commiteada sola** |
| 3 | `d809eaac` | acto **392**, primer commit: lectura, plan sellado, simulacion y verificador, **antes de fundir** |
| 4 | `9a80b59b` | acto **392**, segundo commit: **la fusion**, trece guardas y ciclo de cuatro comandos |
| 5 | `f9595ae0` | acto **392**, tercer commit: **el cierre** |
| 6 | `07f3a258` | acto **711**, primer commit |
| 7 | `6f905ca3` | acto **711**, segundo commit: **la fusion**, la primera de la operacion que cruza **dos libros** |
| 8 | `55837096` | acto **711**, tercer commit: **el cierre** |
| 9 | `15b3fc54` | acto **969**, primer commit |
| 10 | `a0276079` | acto **969**, segundo commit: **la fusion, la ultima de `OP-D-06`** |
| 11 | `15d42eef` | acto **969**, tercer commit: **el cierre**, con la relectura del **233** |
| 12 | `9a09e8d7` | **`OP-D-06` CERRADA**: recomputo, pares releidos, verificacion punto por punto, estado al cierre y **la nota de OPERACION HECHA** |

---

## 1. EL MARCADOR RECOMPUTADO AL CIERRE (regla 1)

**Recontado del archivo AL CERRAR, no citado de la apertura**, con un barrido propio sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:

| | apertura de la vuelta 44 | **al cierre** | lo que lo movio |
|---|---:|---:|---|
| `n` | 3.388 | **3.388** | nada: **cero altas y cero bajas** |
| **A** | 575 | **575** | nada |
| **B** | 81 | **80** | **la relectura del par 233** al cierre del acto 969 |
| **C** | 8 | **8** | nada |
| **D** | 2.724 | **2.725** | la misma relectura |
| tasa de A | 17,0 | **17,0** | nada (16,97 al centesimo) |

**Y las tres comprobaciones de forma, corridas al cierre:** rango **1 a 3.388**, **CERO huecos**, **CERO duplicados**, **CERO clases fuera de ABCD**.

> **LA TASA POR DOMINIO NO SE PUBLICA EN ESTA VUELTA, y se dice por que en vez de dejar la casilla vacia:** es una metrica del **cribado**, y esta vuelta **no cribo un solo par**. Lo unico que toco el archivo fue **una relectura obligatoria post fusion**, que mueve el marcador global en una unidad y no reparte nada por dominio. Igual que en la vuelta 43.

---

## 2. EL ESTADO DEL GRAFO AL CIERRE (regla 1: se mide al cierre)

| | apertura | **al cierre** | la cuenta |
|---|---:|---:|---|
| ficheros | 3.853 | **3.853** | nada: los deprecados **siguen en el grafo** |
| vivos | 3.527 | **3.524** | **menos 3**, una por fusion |
| deprecados | 326 | **329** | **mas 3**, los mismos |
| enlaces | 16.887 | **16.898** | **mas 11 NETOS y sin resto** |
| cola de costuras | 1.493 sobre 3.527 (42,3 %) | **1.494 sobre 3.524 (42,4 %)** | **mas 1** |
| `node_families` | 151 / 3.584 / 118 | **151 / 3.584 / 118** | **nada** |

**EL DESGLOSE DE LOS ONCE ENLACES, acto por acto y sin resto:**

| acto | duplicadas fabricadas | simetrizacion | neto |
|---|---:|---:|---:|
| **392** | **menos 1** (`mvp_alta_fidelidad`, deduplicada por el propio ejecutor) | **mas 5** | **mas 4** |
| **711** | 0 | **mas 3** | **mas 3** |
| **969** | 0 | **mas 4** | **mas 4** |
| | | | **mas 11** |

**LA COLA, explicada acto por acto en vez de dejada como saldo:** en el **392** subio **mas 1** (el absorbido ya estaba fuera, asi que deprecarlo no saco a nadie, y el superviviente entro); en el **711** y en el **969** la cuenta **se compenso exacta** (entro el superviviente, salio el absorbido, que si estaba dentro).

**LA DERIVA DE FAMILIA, medida TRES veces con respaldo antes y comparacion despues: CERO nodos cambian de familia en los tres actos**, y `engine/node_families.json` sale con el **mismo `sha256 7a98d1852fd0`** las tres veces, que es ademas el del acto 344 de la vuelta 43. **El comando 4 se corrio igual las tres veces**, porque la regla es condicional **al censo** y no al resultado: **correrlo y que no cambie nada es la prueba de que el derivado estaba al dia**, no la excusa para saltarselo.

---

## 3. LA VARA POR TRAMO: LOS TRES ACTOS, UNO A UNO

| | **392** | **711** | **969** |
|---|---|---|---|
| par | `metricas_de_adquisicion_activacion` con `build_metrics_toolset` | `future_scenarios_planning` con `escenarios_futuros` | `retention_metrics` con `customer_retention_metrics_webmobile` |
| superviviente | **el primero** | **el primero** | **el primero** |
| las trece guardas | **13 en verde** | **13 en verde** | **13 en verde** |
| verbatim (guarda 3) | **14 de 14**, 0 sobrantes | **16 de 16**, 0 sobrantes | **14 de 14**, 0 sobrantes |
| cobertura (guarda 4) | **10 de 10** y **4 de 4** | **12 de 12** y **4 de 4** | **11 de 11** y **3 de 3** |
| `preservar_literal` / `rastros` | **10 de 10** / **6 de 6** | **10 de 10** / **6 de 6** | **10 de 10** / **6 de 6** |
| `P.13` | **14 VIAJAN, 0 se pierden** | **16 VIAJAN, 0 se pierden** | **14 VIAJAN, 0 se pierden** |
| pasos y condiciones del resultado | **6** y **4** | **6** y **3** | **6** y **3** |
| redirecciones | **6** | **3** | **4** |
| `P.16` | **1** duplicada fabricada, en un tercero; **guarda 11 OK (0)** | **0** y **0** | **0** y **0** |
| simetrizacion exacta | **5 de 5**, 0 de otros, 0 faltan, 0 sobran | **3 de 3** | **4 de 4** |
| caso positivo antes / despues | 16 pasan y **20 caen** / **37 pasan y 0 caen** | 12 pasan y **21 caen** / **34 pasan y 0 caen** | 13 pasan y **21 caen** / **35 pasan y 0 caen** |
| Gate 0 | **OK**, 20 renglones en `[OK]` | **OK**, 20 en `[OK]` | **OK**, 20 en `[OK]` |
| suites | motor 25/25, web 1.030, `tsc` 0 | idem | idem |
| cableado (`P.8`, solo desempate) | **7 contra 6** | **10 contra 3** | **4 contra 4, EMPATE** |
| fuente | MIXTA **por forma** (mismo libro) | **MIXTA DE VERDAD: dos libros** | **UNICA** |
| terceros del acto | **8, los ocho `D`** | **CERO** | **5: un `B` y cuatro `D`** |
| relecturas post fusion | **0** | **0** | **1: el 233, de `B` a `D`** |
| senal | 41,9 (corte 2) a **46,0** (corte 3): **mas 4,1, ENCENDIO** | 0,0 (**corte 0**) a **48,9** (corte 4): **mas 48,9, ENCENDIO** | 42,1 (corte 3) a **50,6** (corte 2): **mas 8,5, ENCENDIO** |
| costura leida | **NO hay** | **NO hay**, y con el agravante declarado | **NO hay** |

---

## 4. LAS CUATRO COSAS QUE ESTA VUELTA APRENDIO

### 4.1 LA SENAL SE ENCENDIO EN LOS TRES ACTOS, Y LA GLOSA CORREGIDA LO CUBRE SIN TOCARSE OTRA VEZ

**Antes de esta vuelta, `OP-D-06` no habia encendido la senal ni una sola vez** (el 331 quedo quieto en `+0,0`, el 341 bajo `0,7`, el 344 subio `1,7` sin cruzar y el 361 la **apago**). **En esta vuelta la encendio en los tres actos.** La glosa que la TAREA 1 corrigio decia que la senal **SUBE** con la fusion; la corregida dice que **puede subir o bajar y que NO HAY LEY que diga cual**, y que lo que la mueve es **si las piezas que entran REPARTEN vocabulario entre los dos bloques o lo CONCENTRAN en uno**. **Las tres subidas de hoy son del primer caso, y la glosa nueva las cubre sin tener que corregirse otra vez**, que es la prueba de que la correccion se hizo por la razon correcta y no para tapar el caso que la disparo.

### 4.2 EL `+48,9` DEL 711 SE DESINFLA EN VEZ DE LUCIRSE

Es **el movimiento de senal mas grande de toda la campana**, y **la mitad de la cifra es un artefacto**. El propio instrumento distingue **dos ceros** en su codigo (`_mejor_bloque`): `NO_APLICA` si la lista no llega al minimo de pasos, y `(0.0, 0)` si llega **pero ningun corte puntua**. El *antes* era el segundo caso, **con corte 0**. **Comparar un 0,0 sin corte contra un 48,9 con corte tras 4 no es medir la misma particion dos veces: es pasar de no tener particion a tenerla.** La cifra se publica **con esa linea al lado**, que es lo contrario de publicarla sola.

### 4.3 `P.16` NO DISPARO NI UNA VEZ, Y SE DIJO POR QUE EN VEZ DE CALLARLO

La regla nombra **la arista interna DEL PAR**. En el **392** la simulacion predijo **una duplicada fabricada**, pero **en un tercero** (`mvp_alta_fidelidad`, que nombraba a los dos), y **el propio ejecutor la deduplica** con la guarda 11 en `OK (0)`. **Es el mismo caso del 361**, donde las **dos** duplicadas fabricadas vivian en terceros y `P.16` se aplico **solo a la auto-arista del par**. En el **711** y el **969** no hubo ni duplicadas ni auto-aristas. **Precedente citado, no inventado.**

### 4.4 LOS INSTRUMENTOS DE REGISTRO CLASIFICAN COMO `VIVO` COSAS QUE SON `ARCHIVO`, y salio CINCO veces

`vuelta40_registros_no_grafo.py` clasifica por **prefijo de ruta**, y su lista de `ARCHIVO` **no cubre** `docs/GRADIENTE_PARES.jsonl`, `dataset/metadata/merged_originals/` ni `packs/*/metadata/bridges_*`. **Los cinco ficheros que salieron marcados `VIVO` por esa via se midieron uno a uno en vez de despacharse:** cero lectores de codigo en todos, y en los dos de `packs/seguridad_digital` **la mencion vive dentro de `rechazados_individuales` con su motivo escrito**. **No se toco el instrumento** (tocar uno sellado sin encargo escrito es peor que no tocarlo) y **queda como `PENDIENTE DE DOCTRINA`**.

---

## 5. CORRECCIONES DECLARADAS (sin borrar el texto viejo)

| # | que se corrigio | donde queda el texto viejo | como se verifico |
|---:|---|---|---|
| **1** | **LA GLOSA DE LA SENAL** de `scripts/loop/vuelta42_senal_antes_despues.py`, por encargo escrito del acta de la vuelta 43 (seccion 4, punto 2, linea **9351**). Decia que la senal **SUBE** con la fusion, y en la salida sellada del 361 esa frase convivia con **LA FUSION APAGO LA SENAL, menos 9,4** | **verbatim en el mensaje del commit `62973381`** | **re-corrida sobre el acto 361 con los MISMOS refs** (antes `ed61c8f0`), sellada en `SALIDA_V44_GLOSA_VERIFICADA.txt`, exit 0. **Las quince lineas de cifras salen BYTE IGUALES, `md5 1160702f399c5875e6c805f630b5ec6d` en las dos.** Solo la glosa cambia. **Ninguna cifra se movio: no hubo que revertir ni parar** |
| **2** | **LA CABECERA TECLEADA** de `scripts/loop/vuelta43_cierre_opd06.py`, que imprimia `MEDIDO EN LA VUELTA 43` y **habria salido mintiendo en cuanto alguien lo corriera en otra vuelta**, que es lo que paso hoy | **verbatim en el mensaje del commit `9a09e8d7`** | **una sola linea tocada**: ni una cifra, ni una medicion, ni un umbral. Las 59 lineas de contenido son las que produce la logica intacta, con **las unicas diferencias que las tres fusiones explican** |
| **3** | **EL VEREDICTO DEL PAR 233**, `analisis_de_cohortes` con `retention_metrics`, **de `B` a `D`** | **entero dentro de la propia razon nueva**, y ademas en el registro y en el commit `15d42eef` | `scripts/corregir_veredicto.py`, que **comprueba que el total no cambie**: **3.388 veredictos, sin altas ni bajas**, y publica el marcador recomputado |

> **Y UNA CUARTA QUE NO ES CORRECCION SINO HALLAZGO, y se declara igual:** la razon del **233** estaba **rancia por partida doble antes de esta fusion**, y la primera mitad **no es culpa de este acto**: el CAC, el payback y el churn temprano que atribuia a `retention_metrics` se habian ido con `OP-F-04-COL` en el commit **`575be1e3`**. **Lo mismo le paso a la razon del 711** (atribuia al superviviente unas senales de alerta que ya viven en `escenarios_de_evolucion_de_la_ia`) **y a la del 392** (nueve pasos cuando el nodo mide cinco). **Tres razones del archivo rancias en el mismo sitio: el detalle que el destejido de la fase 01 se llevo.**

---

## 6. PENDIENTES DE DOCTRINA

1. **EL CAMPO `fuente` TRAS UNA FUSION QUE CRUZA DOS LIBROS DE VERDAD** (el acto **711**, el primero de `OP-D-06`). **`P.19` punto 2** manda que el nodo quede **MULTIFUENTE LEGITIMO con la procedencia declarada por bloque**, pero **`P.19` gobierna la REPETICION INTERNA de un nodo, no la fusion de dos nodos de dos libros**, y **ninguna regla escrita dice hoy que hace ese campo en ese caso**. **Lo mejor sostenido, y es lo que se hizo:** el campo del superviviente **queda intacto por el precedente MEDIDO de `OP-D-04`** (que fundio a traves de libros **en los dos sentidos**, publicado en su TABLA 1), y **la procedencia por bloque queda declarada en el mapa de movimiento del acto**. **Si el fundador quiere legislarlo, es un renglon.**
2. **LA HEURISTICA DE CLASES DE `vuelta40_registros_no_grafo.py`**, seccion 4.4. Cinco ficheros salieron `VIVO` siendo `ARCHIVO` por naturaleza. **No se toco el instrumento** y **ninguno era un rojo**: los cinco se midieron uno a uno.
3. **`MIN_BLOQUE = 2`**: del fundador, **nadie lo toco, sigue igual**, y con el sigue pendiente que umbral lo acompana.
4. **EL ENLACE MUTUO DEL PAR 494**: pendiente vivo de la **fase 04**, re-medido hoy en los dos sentidos y **sigue sin existir**.
5. **DOS ARISTAS QUE FALTAN, declaradas por las dos relecturas de la operacion**: la del par **599** (vuelta 43) y la del par **233** (esta vuelta). **Las dos por el mismo motivo: la relacion es de ALIMENTACION y no de gemelos, y una alimentacion pide arista.** Van a la **fase 04**.
6. **CUAL ES LA OPERACION SIGUIENTE cuando la de menor `orden` no declarada HECHA no es la siguiente por `orden`.** Es la parada de la seccion 9 y **no se resuelve aqui**.

---

## 7. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Van marcados sin saber como los adjudicara el auditor. Son las decisiones que un lector razonable podria resolver al reves.**

### D1. EL SUPERVIVIENTE DEL 392 Y LA VARA DEL ALCANCE DEL ROL, QUE APRIETA

El titulo del superviviente dice **(adquisicion y activacion)** y el resultado nombra ademas **referidos**. **La vara de `P.8` en la direccion inversa que el acta de la vuelta 43 adjudico en su D3 podria cortar contra mi eleccion.** Mi lectura: **los unicos dos pasos que MIDEN son el de adquisicion y el de activacion**; los referidos entran como **categoria de la seleccion** y las cohortes como **capacidad futura del tablero**, y **preparar no es ejecutar** (el precedente del 344). **Ademas la guarda 12 prohibe tocar titulo y etiqueta en una fusion**, asi que elegir base es elegir nombre definitivo. **Quien lea que un nodo debe nombrar todo lo que su procedimiento menciona, y no solo lo que mide, adjudicara al reves.**

### D2. LAS CUATRO CONDICIONES DEL 392, SIN FUNDIR NINGUNA

Cuatro origenes en **cuatro** condiciones: **dos momentos** (decidir inversion, entrar en validacion) y **dos carencias** (no poder medir, no saber que medir). **Los actos 344 y 711 SI fundieron un par de condiciones cada uno**, asi que **no estoy aplicando la misma mano en los tres**. Mi lectura es que aqui ninguna es caso particular de otra; **quien mida la coherencia entre actos y no dentro de cada uno lo vera como una inconsistencia.**

### D3. EL SUPERVIVIENTE DEL 711 CON EL MARGEN DE CABLEADO MAS ANCHO DE LA OPERACION

**10 contra 3**, y **la lectura NO es ciega respecto del cableado**: lo vi al leer el bloque (e). Sostengo que el nombre, el motor de la matriz y el amarre al Canvas **se sostendrian igual con el cableado al reves**, y cito que la segunda aplicacion escrita de `P.8` es exactamente el caso contrario (**diez contra cinco y aun asi pierde el de diez**). **Es la misma limitacion que la vuelta 43 se declaro y el auditor adjudico sin accion en su D1; se vuelve a declarar porque el margen aqui es el mayor de todos.**

### D4. LA DECLARACION DE **NO HAY COSTURA** EN EL 711, CON EL CORTE EN LA FRONTERA DE LOS DOS LIBROS

**Es el discutible mas duro de la vuelta y va con sus dos agravantes por delante:** (1) el corte cae **exactamente donde empieza el material del donante** (bloque B **entero** de Cooper), asi que un lector puede decir con razon que el nodo se lee como *el metodo de Osterwalder y despues el apendice de Cooper*; y (2) **el verbo repetido `Identifica` en tres pasos es una eleccion de redaccion MIA**, y bajarlo ahora que la senal disparo **seria acomodar la puerta**. Mi lectura: los pasos 5 y 6 **operan sobre el producto de los 1 a 4** y sin ellos no tendrian sobre que trabajar. **La firmo yo, que soy quien fundio, y esa es la razon de que se marque.**

### D5. EL `+48,9` PUBLICADO Y DESINFLADO EN LUGAR DE OMITIDO

Podia haber publicado solo el estado final (**DENTRO por mas 4,9**) y no la diferencia. **Elegi publicar la cifra grande CON su explicacion**, porque omitirla seria elegir el dato que conviene. **Quien piense que una cifra que hay que explicar en cinco lineas no deberia publicarse como movimiento adjudicara al reves.**

### D6. EL VEREDICTO DEL 233, DE `B` A `D`, CON UN DATO EN CONTRA QUE PUBLICO

**La fusion de hoy los ACERCO en dos de los tres puntos** (el paso 1 ahora registra la fuente y el 6 mide el resultado de las promociones). Sostengo `D` porque **registrar no es determinar** y **medir no es disenar**, y porque los entregables no son intercambiables. **Es la misma forma del D5 de la vuelta 43 con el 599, y el dato en contra es mio y lo publico.**

### D7. LOS GRUPOS DEL 969: DOS FUSIONES DE PIEZAS QUE SE PODIAN DEJAR SEPARADAS

Fundi **`W1` con `R5`** (registrar la fecha de inicio con agrupar por mes de ingreso) y **`W3` con `R4`** (detectar el abandono con monitorear quejas y tickets). La primera la defiendo fuerte (**la cohorte se construye con esa fecha y con ninguna otra cosa**); **la segunda es mas opinable**: son **el aviso y la confirmacion** de la misma salida, y quien las lea como dos momentos distintos las separaria.

### D8. LA DECLARACION DE **OPERACION HECHA** SIN UN ACTA DETRAS

El patron de la vuelta 30 escribe la declaracion **citando el acta que la respalda**. **Aqui no hay acta**, porque es esta misma vuelta la que cierra. **Lo declare dentro de la propia nota** en vez de omitirlo, y la evidencia que la sostiene es **la medicion propia sellada de hoy y los veinticuatro commits de acto**. **Quien lea que la declaracion debe esperar al acta adjudicara que me adelante.**

### D9. LA PARADA SOBRE LA OPERACION SIGUIENTE

**No abro ninguna.** Es una decision de alcance disfrazada de lectura si me equivoco, y va entera en la seccion 9 con las tres candidatas medidas. **Quien lea que `OP-D-09` era ejecutable hoy (su `pregunta_pendiente` dice NINGUNA para escribir la operacion) adjudicara que me quede corto.**

---

## 8. LO QUE QUEDA DE `OP-D-06`, DECLARADO CON SU ESTADO

| que | estado |
|---|---|
| **los nueve actos** | **CERRADOS: ocho fundidos y uno (el 494) declarado.** Ninguno a medias |
| **el par 494** | va a **`OP-D-01`** como cura acoplada mayor. `OP-D-06` **no lo toco** |
| **el enlace mutuo del 494** | **fase 04**, re-medido hoy y sigue sin existir |
| **las dos aristas que faltan** (599 y 233) | **fase 04** |
| **la duplicada vieja del catalogo** | **`OP-S-12`**, que desde `P.16` es **verificacion de cero**. **Las ocho fusiones de `OP-D-06` no fabricaron ninguna** |
| **el campo `estado` de `OP-D-06`** | **sigue en `LISTA`**, y es correcto: el esquema no tiene el valor `HECHA` y estrenarlo seria doctrina de esquema, **adjudicado NO en la vuelta 30** |

---

## 9. LA PARADA: **LA OPERACION SIGUIENTE NO SE PUEDE ABRIR SIN DECIDIR**

**Las tres candidatas se leyeron ENTERAS de `docs/plan/OPERACIONES.jsonl` antes de tocar nada, y ninguna se toco.** El encargo autoriza exactamente esto: *si su texto no alcanza para ejecutarse sin decidir, PARAS y la traes*.

| candidata | `orden` | lo medido hoy | por que no se abre |
|---|---:|---|---|
| **`OP-D-07`** | **7**, la siguiente por orden | `depende_de: ['OP-M-03']` y `bloquea_a: ['OP-M-03-I']`, leidos hoy | **depende de una operacion de MESA, que es la fase 06.** Abrirla ahora seria saltarse su propia dependencia declarada |
| **`OP-D-08`** | 8 | su campo `pregunta_pendiente` **NO esta vacio**: *si la frase PARA LA SOLUCION DISENADA del paso 5 es un MARCO propio... No se decide aqui* | **su propio texto dice que el reparto tiene una pieza abierta.** Es la letra del modo continuo y el precedente del **d5 del acta de la vuelta 40** |
| **`OP-D-09`** | 9 | `pregunta_pendiente`: *NINGUNA para escribir la operacion* | **ES LA UNICA EJECUTABLE POR SU PROPIO TEXTO, y aun asi no se abre**, porque abrirla **saltandose dos operaciones de orden menor** es una decision de alcance que ninguna regla escrita autoriza |

**Y HAY UN CUARTO HECHO QUE COMPLICA EL ORDEN, medido hoy y no supuesto:** `OP-D-01` (orden **1**) y `OP-D-02` (orden **2**) **NO declaran HECHA en su nota**, mientras que `OP-D-03`, `OP-D-04`, `OP-D-05` y ahora `OP-D-06` **si**. **Sus notas dicen que su trabajo material esta hecho y que lo que falta esta deferido a otro sitio** (`OP-D-01`: *las tres clases nuevas NO se vuelcan... porque un par nuevo entra POR EL RECOMPUTO, y las tres aristas son la fase 04*), **pero ninguna de las dos trae el registro de operacion hecha**. **Si ese registro es trabajo de esta fase o de la vuelta que haga el recomputo, no esta escrito en ninguna parte, y no lo decido yo.**

**LA PREGUNTA, concreta:** despues de `OP-D-06`, la fase 02 sigue por **`OP-D-09`** (la unica ejecutable), o primero hay que **cerrar el registro de `OP-D-01` y `OP-D-02`**, o hay que **contestar la pregunta abierta de `OP-D-08`**? **Las tres son de una linea de respuesta y ninguna se puede adivinar.**

---

## 10. CONDICIONES DE PARADA, RECORRIDAS

| condicion | se cumple? |
|---|---|
| **doctrina nueva** | **NO.** El campo `fuente` cruzando libros va como `PENDIENTE DE DOCTRINA` **con precedente medido**, no como regla nueva |
| **contradiccion sin regla de correccion** | **NO.** Las tres correcciones de la seccion 5 se hicieron con reglas existentes |
| **decision de fundador** | **NO.** `MIN_BLOQUE` intacto, cero contenido borrado fuera de regla, el bucle no fundio ramas |
| **fallo tecnico repetido** | **NO.** **Cero rojos en toda la vuelta**: las trece guardas verdes en los tres actos a la primera, Gate 0 verde las tres veces, y **la suite web paso a la primera las tres veces** porque el comando 4 fue en su sitio |
| **credito roto** | **NO.** La vuelta 43 cerro con **cero caidas de clase o cifra** y **la racha de reporte en CERO** |
| **campana consumada** | **NO.** `OP-D-06` cerrada, pero la fase 02 tiene tres operaciones detras y el `00_INDICE` tiene el resto |
| **credenciales** | no hicieron falta |
| **UNA PARADA SI, Y ES DE ALCANCE, no de tecnica** | **SI: la operacion siguiente, seccion 9.** No es una condicion de parada del bucle: es el ejecutor haciendo lo que el modo continuo manda cuando el texto no alcanza |

---

## 11. LO QUE EL AUDITOR PUEDE RE-CORRER ENTERO

| que | como |
|---|---|
| el marcador y sus huecos | barrido propio sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` |
| el grafo, los enlaces y la cola | `dataset/nodos` y `scripts/costuras_internas.py` |
| el cierre de la operacion | `python scripts/loop/vuelta43_cierre_opd06.py`, y **el bloque pegado en el registro es su salida verbatim** |
| las tres fusiones | `git show` de los tres commits segundos, mas las salidas `SALIDA_V44_ACTO*_EJEC.txt` |
| la glosa corregida | `python scripts/loop/vuelta42_senal_antes_despues.py --nodo key_partners_hypothesis --commit ed61c8f0 --nombre "OP-D-06 acto 361"` y `diff` contra `SALIDA_V43_ACTO361_SENAL.txt` |
| el ciclo Gate 0 | los cuatro comandos, con el 4 antes del 3, respaldando `phase1_run_log.json` antes |
| las suites | `python engine/run_all_tests.py`, `pnpm test` en `web/`, `npx tsc --noEmit` |
| el verificador de mapas | `verificar_mapas_destejido.py` con los **catorce** planes: **14 tablas, 83 filas, 0 discrepancias** |
| la relectura del 233 | `python scripts/loop/vuelta32_relectura_opd01.py 233` y la razon nueva en el archivo |
