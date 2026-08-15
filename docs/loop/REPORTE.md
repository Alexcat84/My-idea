# REPORTE DE LA VUELTA 28. Ejecutor: Opus 5. FASE III, EJECUCION. Rama `pasada-unica`

**14 ago 2026.** Encargo: `docs/loop/PROMPT_SIGUIENTE.md` de la vuelta 27 del auditor.
**Toda cifra de este reporte sale de un instrumento corrido EN ESTA VUELTA** (`EJECUTOR.md`
regla 2). Las cifras de actas y reportes anteriores aparecen **solo como contraste**, y
cuando discrepan de la medicion de hoy la discrepancia se declara en vez de resolverse
copiando.

---

## 0. LA CABECERA

| | |
|---|---|
| **HEAD de partida** | `7563c85e` (el commit de la decision del fundador), arbol limpio, cero pendiente que pushear al empezar |
| **commits de la vuelta** | `4e6349ea` (TAREA 1) y `f69f4819` (`OP-F-04-WEI` en parte), **los dos en `origin/pasada-unica`**, mas el commit de este reporte |
| **rutas tocadas** | `docs/loop/` **52 ficheros**, `dataset/nodos/` **11**, `scripts/loop/` **6**, `docs/plan/` **3**, `web/lib/assets/` **2**, `dataset/metadata/` **1** |
| **diff sobre `dataset/nodos/`** | `git diff --stat 7563c85e..HEAD`: **11 ficheros, 37 insertadas, 37 borradas.** La simetria es la firma del reparto: nada se creo ni se perdio, todo se movio |
| **salidas de instrumento** | **51 ficheros `docs/loop/SALIDA_V28_*`**, y la cuenta va partida para que cuadre al digito: **50 ya commiteadas** en `4e6349ea` y `f69f4819` (`git diff --name-only 7563c85e..HEAD`, contado hoy) **mas 1 que entra con este reporte**, `SALIDA_V28_ESTADO_FINAL.txt`. **Se cuenta asi a proposito:** las dos vueltas anteriores cayeron por contar el registro sin contarlo |
| **nodos creados** | **CERO en el historial.** Uno se creo, se probo entero y se deshizo: ver la seccion 3 |

---

## 1. LA PARADA, y va primero porque manda sobre todo lo demas

> **HAY UNA TERCERA HILADA DEL MURO, y no es la misma de las dos anteriores.**

**Como se encontro, y se dice el orden porque importa:** la relectura conjunta de la TAREA 1
mando crear un nodo propio. Se creo, con sus guardas en verde, su caso positivo en las dos
direcciones y su linea en `docs/plan/INDICE_ROJO_DECLARADO.jsonl`. **`GATE 0` cerro en OK e
imprimio el rojo declarado uno a uno**, tal como la decision del fundador del 14 ago 2026
manda, y la **suite del motor paso 24 de 24**: las dos hiladas que el fundador abrio ese dia
quedaron abiertas y funcionando. **La que se cayo fue la suite WEB**, que el guardian de
commit corre igual que las otras (`.githooks/pre-commit`, verificado hoy leyendo el fichero).

**Y se cayo por DOS causas distintas, separadas corriendo el instrumento y no razonando:**

| # | prueba que cae | que es realmente | remedio |
|---|---|---|---|
| **a** | `web/lib/readiness.test.ts`, *paridad exacta contra `node_families.json`*: `expected 3836 to be 3835` | **un artefacto DERIVADO que se quedo viejo.** `engine/node_families.json` lo genera `engine/plan_readiness.py` desde el grafo, y el ciclo escrito de `GATE 0` (los tres comandos de `08_VERIFICACION.md`) **no lo regenera** | **MECANICO Y ESCRITO EN LA PROPIA HERRAMIENTA** (*Uso: python engine/plan_readiness.py, regenera engine/node_families.json*). Corrido mas `sync`: **cura esta y solo esta** |
| **b** | `web/lib/engine/graph.test.ts`, *carga los 3835 nodos reales*: `expected 3836 to be 3835` | **una CIFRA DE CENSO CLAVADA en una prueba.** No es un artefacto que se regenere: es un numero escrito a mano | **NO LO HAY SIN DECIDIR.** Ver abajo |

**MEDIDO, no supuesto:** tras correr el remedio (a), la suite web paso de **2 ficheros y 2
pruebas en rojo** a **1 y 1** (`SALIDA_V28_SUITE_WEB_RELECTURA.txt` contra
`SALIDA_V28_MURO_SUITE_WEB.txt`).

### POR QUE (b) ES PARADA Y NO LA ARREGLO YO

**No es una prueba envejecida cualquiera: es la que vigila el censo del grafo**, y la pasada
entera existe para moverlo. **Arreglarla exige decidir**, y ninguna pagina lo dice:

1. **si la cifra se actualiza a mano en cada operacion** (y entonces quien la actualiza, y
   con que evidencia), **o si la prueba deja de clavar un numero** (y entonces la guarda
   deja de vigilar lo que vino a vigilar);
2. **cuantas veces va a moverse**: hoy la mueve un nodo creado; la fase 03 depreca por
   fusion en dieciseis operaciones, y **cada una la mueve otra vez**;
3. **si el mecanismo del rojo declarado le sirve o no**, que es la pregunta que el fundador
   ya contesto para el indice semantico y que aqui **no esta contestada**.

> **Es la misma especie que el auditor se nego a adjudicar en el acta de la vuelta 27,
> seccion 5, y por las mismas tres razones que escribio alli** (*la letra*, *el precedente*,
> *el remedio no se ejecuta sin decidir*). La correccion del fundador del 14 ago nombra
> **el chequeo del indice semantico** y sus tres sedes; **esta prueba no mide el indice: mide
> el censo.** Leerle una guarda mas seria leerle intencion, no letra. Y `AUDITOR.md` seccion
> 3 es explicita: *una operacion cuyo texto no alcance para ejecutarse sin decidir es PARADA,
> no una improvisacion*.

### QUE BLOQUEA EXACTAMENTE, medido operacion por operacion

| bloqueado | por que |
|---|---|
| **`OP-F-02` entera** | sus **tres** cortes son nodo propio (plan sellado `PLAN_V27_OPF02.json`) |
| **`OP-F-03`, los CINCO bloques que le faltan** | los cinco tienen destino NODO PROPIO leido |
| **la correccion 1 de la relectura conjunta** | nodo propio |
| **`OP-F-04-HOR`, previsiblemente** | su texto dice *va a familia propia*, o sea nodo propio |
| **la fase 01 entera, por tanto** | no se puede declarar cerrada |
| **el punto 4 del encargo (modo continuo a las fases siguientes)** | depende de la fase 01 cerrada |

**LO QUE NO BLOQUEA, y por eso esta vuelta no se paro en seco:** todo bloque cuyo destino es
un **miembro**. Eso es lo que se ejecuto (seccion 4), con la letra del modo continuo y con el
precedente que el acta de la vuelta 27 adjudico CORRECTO en su discutible 9.

**Nada se salto, nada se rodeo:** el hook corrio en los dos commits y los dos lo pasaron en
verde; el guardian no se toco; el `.env` no volvio al repo; ningun verde se falseo.

---

## 2. EL ESTADO, RECOMPUTADO DEL ARCHIVO HOY

`python scripts/loop/vuelta26_estado.py`, salidas `SALIDA_V28_ESTADO.txt` (al abrir) y
`SALIDA_V28_ESTADO_FINAL.txt` (al cerrar). **Las dos dan lo mismo: esta vuelta no toco un
solo veredicto.**

**EL MARCADOR:** n **3.388**, puestos **1 a 3.388**, **cero huecos, cero duplicados, cero
clases fuera de ABCD**.

| clase | n | por ciento |
|---|---:|---:|
| **A** | **583** | **17,2** |
| **B** | **89** | **2,6** |
| **C** | **7** | **0,2** |
| **D** | **2.709** | **80,0** |

**LA TASA DE A POR DOMINIO, corte 14 ago 2026:**

| dominio | n | A | tasa | B | C | D |
|---|---:|---:|---:|---:|---:|---:|
| core | 1.445 | 344 | 23,8% | 87 | 7 | 1.007 |
| quality | 844 | 126 | 14,9% | 0 | 0 | 718 |
| health_safety | 192 | 45 | 23,4% | 0 | 0 | 147 |
| entrega | 171 | 2 | 1,2% | 0 | 0 | 169 |
| environmental | 170 | 29 | 17,1% | 0 | 0 | 141 |
| compras | 155 | 1 | 0,6% | 2 | 0 | 152 |
| franquicias | 148 | 18 | 12,2% | 0 | 0 | 130 |
| exportacion | 130 | 15 | 11,5% | 0 | 0 | 115 |
| risk_management | 106 | 0 | 0,0% | 0 | 0 | 106 |
| seguridad_digital | 27 | 3 | 11,1% | 0 | 0 | 24 |

> **LA BANDA QUE `P.15` OBLIGA A LLEVAR AL LADO, citada con su corte y no recomputada:**
> el error de dejar pasar medido el 12 ago 2026 sobre el archivo al puesto 2.117 es de
> **4,2 por ciento, banda de 0,7 a 20,2** (`08_VERIFICACION.md`). **No se remide aqui: esta
> vuelta no leyo ni un par.**

**LA VARA POR TRAMO NO APLICA EN ESTA VUELTA, y se dice en vez de callarlo:** cero pares
leidos, cero puestos movidos. **La unidad de esta vuelta fue el bloque injertado y el
registro.**

**EL GRAFO, al cerrar:** **3.835 ficheros de nodo**, **3.521 vivos**, **314 deprecados**,
**16.800 enlaces** (previos mas siguientes), **15 claves distintas**. **Identico al de
apertura: esta vuelta no creo ni deprecio ningun nodo en el historial.**

**LAS OPERACIONES:** **71**, 71 ids unicos, **cero dependencias rotas**, las **71 en
`LISTA`**. `OPERACIONES.jsonl` **no se toco**.

**EL INVENTARIO:** **671 entradas al abrir, 672 al cerrar** (dominio 10, acto 556, racimo 13,
**familia_de_ids 53 a 54**, figura 20, defecto 19). **La entrada nueva es `HUGOS-SISTEMAS`.**

**LAS FAMILIAS AL DIA, medidas hoy** (`scripts/loop/vuelta27_medir.py familia`):

| familia | vivos | con fuente UNICA |
|---|---:|---:|
| Hugos | **111** | **107** |
| Rackham (`SPIN`) | **47** | **47** |
| Weinberg (`Traction`) | **80** | **67** |
| Coleman (`Never Lose a Customer`) | **83** | **68** |
| Horowitz (trozo `Hard Thing`) | **102** | **88** |

> **CONTRASTE DECLARADO con el acta de la vuelta 27, que las midio al HEAD de partida de
> aquella vuelta:** Hugos 126 y 107 entonces, **111 y 107 hoy**; Rackham 51 y 47 entonces,
> **47 y 47 hoy**. **No es discrepancia: es la resta exacta de los donantes cuya fuente
> aquella vuelta corrigio**, y el acta ya la habia reproducido al HEAD de cierre con esos
> mismos numeros.

**LAS CINCO CITAS DEL FUNDADOR, comprobadas hoy contra el repo** (`vuelta27_medir.py
citas`, `SALIDA_V28_CITAS.txt`): **5 de 5 PRESENTES, FALLOS 0**, y `P.18` citada en las
**cuatro** `OP-F-04` una por una.

---

## 3. TAREA 1: LOS REGISTROS

### 3.1 `HUGOS-SISTEMAS` horneada al inventario

**Adjudicacion 7 del acta de la vuelta 27** (`ACTA_AUDITOR.md`, seccion 4, punto 7, leida
hoy: *SI, POR EXTENSION CITADA*). Entrada `familia_de_ids` escrita con
`scripts/loop/vuelta28_registros.py --ejecutar` (`SALIDA_V28_REGISTROS_INVENTARIO.txt`).

**LA NOMINA SE MIDIO, NO SE COPIO:** los **nueve** ids (los ocho de la salida de sistemas
mas `tecnologia_como_medio_no_fin`) salieron **vivos** y con **fuente UNICA** *Essentials of
Supply Chain Management - Michael H. Hugos*, **9 de 9**. El instrumento **para y no escribe**
si uno falla. Contraste medido en la misma corrida: **111 vivos declaran a Hugos, 107 con
fuente unica**; la nomina es **9 de esos 107**.

**LA LECTURA QUE LOS JUNTA**, escrita en la entrada: los nueve son **el mismo capitulo de
Hugos, el de como se construye un sistema**. Cuatro dicen el **ciclo de diseno**
(`diseno_conceptual_sistema` esboza, `guias_diseno_sistemas_estrategicos` compara disenos con
siete criterios, `definicion_objetivos_proyecto_sistema` parte el diseno en componentes
cohesivos, `complejidad_acorde_capacidad_organizacional` mide el alcance contra la capacidad
real). Tres dicen **como se ejecuta** (`ejecucion_incremental_transicion_tecnologica`,
`rediseno_tras_fracaso_proyecto`, `arquitectura_flexible_soa`). Dos dicen **para que**
(`tecnologia_como_medio_no_fin`, `requisitos_sistema_retroalimentacion`).

**Y LA NOTA DE ALCANCE VA DENTRO DE LA ENTRADA, para que nadie la lea de mas:** los nueve son
**la nomina LEIDA**, no un barrido exhaustivo del capitulo sobre los 107. **Si la familia
crece, `P.18` manda releerla al dia de la operacion que la use.**

### 3.2 LA RELECTURA CONJUNTA: LAS DOS DISCREPANCIAS VUELCAN

**Las dos que el auditor marco en el acta 27, seccion 2, verificadas hoy contra el grafo con
la vara de `P.18`** (`SALIDA_V28_RELECTURA_CONJUNTA.txt`). **Las dos vuelcan: el auditor
tenia razon en las dos y mi lectura de la vuelta 27 cae en las dos.** El texto de la lectura
anterior **queda entero** en `01_FUENTES.md` con la correccion escrita encima.

**d2, `economia_circular_como_modelo_de_negocio` 6 a 9: NO va al miembro, VA A NODO PROPIO.**

- **El miembro SIMULA y COMPARA** (definir entidades, centro de gravedad, correr
  simulaciones de 14 dias, reportes de P y L, comparar disenos). **El bloque ELIGE la
  estrategia y DISENA el mecanismo** (mapear el ciclo de vida de hoy, identificar en cual de
  las cinco estrategias circulares hay mas potencial, disenar el retorno o la remanufactura,
  calcular el impacto). **Ningun paso del miembro elige ni disena; ningun paso del bloque
  simula.**
- **Y LA FRASE QUE YO PUBLIQUE EN LA VUELTA 27 NO SE SOSTIENE MEDIDA HOY:** dije que *el
  ultimo paso del bloque es su propio entregable*. **El entregable del miembro, leido hoy, es
  un modelo de simulacion con reporte de P y L y KPIs para al menos dos escenarios**, no el
  impacto en costos de materiales y logistica. **Yo nombre una clausula del `resumen_teorico`
  y la llame entregable.**
- **Ningun otro miembro coincide**, y no es una busqueda negativa citada: barrido corrido hoy
  sobre los **111 vivos de Hugos**, con **tres aciertos** de los cuales dos son incidentales
  (`estrategia_captura_mercado_crecimiento` cita *productos verdes* como ejemplo de mercado
  emergente; `gestion_beneficios_alianza_sostenible` usa *sostenible* en el sentido de alianza
  duradera). **Queda uno, y es el que no coincide.**
- **`P.18` punto 3: NODO PROPIO.** `estrategia_circular_y_mecanismo_de_retorno`, con
  `economia_circular_como_modelo_de_negocio` de procedencia y previo.

**d4, `superioridad_producto_beneficios` 7 a 10: se MUDA de `diferencia_ventaja_beneficio` a
`framework_caracteristicas_ventajas_beneficios`. APLICADA Y EN EL ARBOL.**

- **El bloque no nombra la Ventaja ni una sola vez** y **no decide ningun momento de
  conversacion**: opone CARACTERISTICAS y BENEFICIOS y decide el estilo global del discurso
  segun el posicionamiento de precio.
- El miembro que lo recibio decide **el momento** (su entregable lo dice con esas palabras:
  *el momento exacto de la conversacion en que debes usar cada uno*) y sus cuatro pasos
  propios son todos de momento. **El objeto no coincide alli.**
- El miembro nuevo tiene por entregable **la guia de clasificacion de mensajes de venta
  aplicada a la propuesta de valor propia**, y su paso 3 pide que el Beneficio responda a una
  Necesidad Explicita, **que es el paso premium del bloque**. **Coincide aqui.**
- **Saldo medido:** `diferencia_ventaja_beneficio` **8 pasos a 4**;
  `framework_caracteristicas_ventajas_beneficios` **4 a 8**. **Cero perdida:** la huella *otro
  posicionamiento de precio* vive hoy en **exactamente un nodo vivo**.

**EL RECOMPUTO QUE ESTO OBLIGA, y es una correccion de cifra:** los **quince** repartidos de
`OP-F-03` en la vuelta 27 pasan a **CATORCE en el arbol**, y **los bloques que le faltan a
`OP-F-03` para declararse HECHA suben de CUATRO a CINCO.** El encargo decia *los cuatro nodos
propios que le faltan*; **medido hoy son cinco bloques**, y el encargo mismo lo previo
(*con el ajuste que traiga la relectura conjunta si economia_circular voltea*).

**LA CORRECCION 1 SE EJECUTO ENTERA Y SE DESHIZO, y se dice entero en vez de callarse.** El
nodo se creo, se declaro en la lista del rojo, `GATE 0` cerro en OK imprimiendolo, el motor
paso 24 de 24, y el **caso positivo corrio en las dos direcciones: 4 de 6 pruebas CAEN antes,
6 de 6 PASAN despues**. **Se deshizo porque la suite web lo dejo incommitteable** (seccion 1).
El plan queda **SELLADO** en `docs/loop/PLAN_V28_RELECTURA.json`, con su corte, sus prefijos
de guarda leidos del grafo de hoy y su motivo por `P.18`. **`INDICE_ROJO_DECLARADO.jsonl`
vuelve a quedar VACIA**, porque el nodo que declaraba ya no existe.

### 3.3 LAS TRES ADJUDICACIONES REGISTRADAS

| # | adjudicacion | donde quedo escrita |
|---|---|---|
| **1** | **`OP-F-03` NO se declara HECHA: queda PARCIAL** hasta que existan sus nodos propios y su caso positivo pase | `01_FUENTES.md`, con la cuenta medida hoy: **14 de 19 bloques en el arbol, 5 pendientes** |
| **2** | **la repeticion que un reparto crea entra a la cola de relectura post fusion de la fase 02 y NO se desteje en el acto** | `08_VERIFICACION.md`, que es donde vive la cola, con su **primera costura declarada**: `ejecucion_incremental_transicion_tecnologica`, que recibio tres bloques y **mide 16 pasos hoy** contra los 4 que tenia. Y en `01_FUENTES.md` |
| **3** | **dos bloques que caen en el mismo nodo propio se funden en UNO**, con las dos procedencias declaradas en su fuente, nunca dos gemelos | `01_FUENTES.md`, aplicada al **unico caso medido**: `analisis_tco_roi_b2b` y `criterios_seleccion_proveedores` van a **un** nodo |

---

## 4. TAREA 2: LO QUE SE PUDO EJECUTAR

**Los puntos 1, 2 y 4 del encargo estan BLOQUEADOS ENTEROS por la parada** (seccion 1): los
tres cortes de `OP-F-02` y los cinco bloques que le faltan a `OP-F-03` son **todos** nodo
propio. **Ni un paso de ellos se movio.**

**Lo que se ejecuto es la parte de `OP-F-04-WEI` cuyo destino es un MIEMBRO**, o sea la que
no toca el muro. Plan sellado `docs/loop/PLAN_V28_OPF04_WEI.json`. La nomina de destino se
midio hoy: **80 nodos vivos declaran `Traction`, 67 con fuente UNICA**.

| origen | frontera | miembro receptor | saldo medido |
|---|---|---|---|
| `plan_de_adquisicion_acquire` | **1 a 7 / 8 a 12** | `bullseye_framework` | 12 pasos a **7**; miembro 6 a **11** |
| `earned_vs_paid_media` | **1 a 4 / 5 a 8** | `publicidad_offline_pruebas_locales` | 8 a **4**; miembro 5 a **9** |
| `fit_problema_solucion` | **1 a 3 / 4 a 6** | `fases_traccion_producto` | 6 a **3**; miembro 4 a **7** |
| `sales_funnel_get_keep_grow` | **1 a 4 / 5 a 9** | `clasificacion_leads_abc` | 10 a **4**; miembro 5 a **10** |
| `sales_funnel_get_keep_grow` | **el paso 10, aparte** | `compromiso_linea_tiempo_cliente` | miembro 5 a **6** |

**LAS LECTURAS QUE SOSTIENEN LOS DESTINOS**, en una linea cada una:

- **`bullseye_framework` y no `middle_ring_testing`**: el bloque **empieza por listar los 19
  canales**, que es el anillo EXTERIOR, y el miembro del anillo medio no tiene ese paso.
- **`publicidad_offline_pruebas_locales`**: pedir a cada medio su prospecto de audiencia,
  comparar alcance contra precio y empezar por radio, prensa y vallas **locales** es su
  objeto. Los otros dos nodos offline no coinciden: uno **mide** lo ya lanzado y el bloque no
  mide, elige; el otro es una tactica de compra, no la eleccion del medio.
- **`fases_traccion_producto`**: el calce mas literal de los cinco, paso por paso. El miembro
  se llama *Las Tres Fases de Traccion* y el bloque nombra las tres.
- **`clasificacion_leads_abc`**: las mismas categorias (A menos de 3 meses, B de 3 a 12, C mas
  de 12) y **las mismas cifras** (66 a 75 por ciento del tiempo a los A).
- **`compromiso_linea_tiempo_cliente`**, y por eso el apendice se **parte en dos**: el paso 10
  no clasifica ni reparte tiempo, **pacta un plazo**, que es palabra por palabra el objeto de
  ese miembro. **Forzarlo dentro de la clasificacion seria el encaje que `P.18` punto 3
  prohibe.**

**LAS GUARDAS DE ESTE REPARTO, corridas todas:** simulacion previa sobre copia en memoria
(**verde**, 5 cortes, **cero nodos nuevos**, 9 ficheros); guarda de texto por paso, de fuente
por nodo, y **guarda de huella nueva de esta vuelta** (cada huella se comprobo **AUSENTE del
destino ANTES de sellar**: una huella que ya vive en el destino no probaria nada); **caso
positivo 15 de 15 CAEN antes y 15 de 15 PASAN despues**.

**LO QUE DE `OP-F-04` NO SE EJECUTO, con su frontera LEIDA HOY y su destino declarado
PENDIENTE en vez de adivinado** (tabla entera en `01_FUENTES.md`): los otros **nueve** bloques
de WEI, de los cuales dos (`coeficiente_viral` y `viral_loop_marketing`) la propia pagina ya
llama *no son un simple apendice* y piden TOQUE UNICO. **`OP-F-04-COL` y `OP-F-04-HOR` no se
tocaron ni un paso**, con sus nominas medidas hoy (**15 nodos vivos** y **13 nodos vivos**) y
sus familias de destino medidas (**Coleman 83 y 68**, **Horowitz 102 y 88**).

---

## 5. LAS GUARDAS TRANSVERSALES, corridas tras cada operacion

**El ciclo de `GATE 0` entero, los tres comandos de `08_VERIFICACION.md`, corrido CUATRO
veces esta vuelta** (base, tras la relectura, tras deshacer, tras WEI):

| | |
|---|---|
| **comando 1** | `run_phase1.py --reaplico-curaduria`: **exit 0 y `GATE 0: OK`** las cuatro veces |
| **comando 2** | `etiquetas_de_cara.py --aplicar` justo despues: **71 etiquetas** las cuatro veces. **NO ENCOGE**, que es la cifra que `08_VERIFICACION.md` manda vigilar |
| **comando 3** | `sync_assets_web.py`: **las dos copias del grafo en el MISMO blob** cada vez, y **byte identicas al HEAD del commit de su tramo**: `05bab97f` en `4e6349ea`, `0c284bc9` en `f69f4819`, medido con `git hash-object` contra `git rev-parse HEAD:<ruta>` **despues de commitear**, que es la vara escrita el 14 ago (vuelta 27) |
| **el rojo declarado** | con el nodo en el arbol, `GATE 0` cerro **OK** e **imprimio el id uno a uno con su operacion y su fecha**. Al cierre la lista esta **VACIA** y `GATE 0` da **0 activos sin vector** sin excepcion ninguna |
| **suites** | motor **24 de 24**; web **80 ficheros, 1.030 pasadas y 3 saltadas**; `tsc --noEmit` **cero lineas** |
| **el hook** | corrio en los dos commits, **verde los dos**, y no se salto ni una vez |

**UN PASO DEL CICLO QUE NO ESTA ESCRITO Y QUE HUBO QUE CORRER:** `python
engine/plan_readiness.py` mas `sync`, para regenerar `engine/node_families.json` cuando el
censo cambia. **Va como pendiente de doctrina 1.**

---

## 6. CORRECCIONES DECLARADAS DE ESTA VUELTA

**Ninguna borra el texto que corrige.**

1. **`economia_circular_como_modelo_de_negocio` 6 a 9 va a NODO PROPIO, no al miembro.**
   Vuelca mi propia lectura de la vuelta 27, y con ella **la frase publicada sobre el
   entregable del miembro, que medida hoy no se sostiene**.
2. **`superioridad_producto_beneficios` 7 a 10 se muda de miembro.** Vuelca el motivo por
   `P.18` que quedo sellado en `PLAN_V27_OPF04_RAC.json`, **que se queda entero**.
3. **`OP-F-03` pasa de 15 repartidos a 14 en el arbol, y de 4 bloques pendientes a 5.**
   Es el recomputo aritmetico de la correccion 1.

---

## 7. PENDIENTES DE DOCTRINA (registrados, no resueltos, `EJECUTOR.md` regla 5)

1. **EL CICLO ESCRITO DE `GATE 0` NO REGENERA `engine/node_families.json`.** Es un artefacto
   derivado del grafo, lo genera `engine/plan_readiness.py`, y **el dia que una operacion
   cambia el censo la suite web se cae por ahi**. Es exactamente la misma especie que el
   comando 3 (*saltarselo deja las dos copias divergentes y la que lo caza es la suite, no el
   Gate*). **Lo mejor sostenido que puedo dejar escrito: el remedio es mecanico y esta en el
   docstring de la propia herramienta, y lo corri.** No lo escribo en `08_VERIFICACION.md`
   como cuarto comando porque **esa pagina es la vara y anadirle un comando es escribir
   doctrina**.
2. **QUIEN MUEVE LA CIFRA DE CENSO DE LA SUITE WEB, Y CON QUE REGLA.** Es la parada de la
   seccion 1.
3. **`OP-F-04-HOR` DICE *va a familia propia*, Y NO ESTA ESCRITO SI ESO ES NODO PROPIO**
   (y por tanto bloqueado hoy) **o si es un miembro de una familia que ya existe.** No lo
   adivino: lo traigo.

---

## 8. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Trece, para la relectura ciega del auditor.**

1. **`economia_circular` a nodo propio.** Coincido con el auditor, pero **vuelco mi propia
   lectura publicada**, y el nodo nuevo que propongo (`estrategia_circular_y_mecanismo_de_retorno`)
   lo escribi yo: su titulo, su resumen y su etiqueta son **texto nuevo mio**, no del libro.
2. **`superioridad_producto_beneficios` a `framework_...`.** El bloque decide por
   **posicionamiento de precio** y el miembro clasifica por **tipo de mensaje**; sostengo que
   coinciden en objeto, **pero ninguno de los dos nodos habla de precio**.
3. **Declarar PARADA por la cifra de censo en vez de actualizarla a 3.836.** Es un numero en
   una prueba y cambiarlo cuesta un minuto. **Sostengo que el minuto no es el problema: la
   regla que falta lo es.**
4. **Correr `engine/plan_readiness.py` sin que ninguna pagina lo mande.** Lo cuento como
   remedio mecanico escrito en la herramienta; **se puede leer como improvisacion.**
5. **Deshacer el nodo propio por segunda vuelta consecutiva**, en vez de dejar el arbol
   incommitteable y parar en seco. Me apoyo en el discutible 8 de la vuelta 27, **adjudicado
   CORRECTO**, pero la situacion no es identica: alli el muro era nuevo, aqui **ya se habia
   parado dos veces por muro**.
6. **Ejecutar `OP-F-04-WEI` en parte pese a que el encargo la condiciona a `OP-F-02` y
   `OP-F-03` cerradas.** Me apoyo en el discutible 9 de la vuelta 27; **es una reordenacion
   del encargo y la marco como tal.**
7. **`plan_de_adquisicion_acquire` 8 a 12 a `bullseye_framework` y no a
   `middle_ring_testing`.** Los dos calzan mucho; decido por el paso 8 (listar los 19), que
   es del anillo exterior.
8. **`earned_vs_paid_media` 5 a 8 a `publicidad_offline_pruebas_locales`.** Los pasos 5 a 7
   son **seleccion de medio** (audiencia, alcance, precio) y solo el 8 es prueba local. **El
   miembro es de prueba local.**
9. **Partir el apendice de `sales_funnel_get_keep_grow` en dos cortes** (5 a 9 y el 10 solo).
   Es el primer apendice de `OP-F-04` que se parte, y **la particion la decido yo leyendo**,
   no la trae escrita ninguna pagina.
10. **La frontera 1 a 10 / 11 a 15 de `ab_testing_optimizacion`** (declarada, no ejecutada):
    la decido por la **firma posicional y de persona** (los pasos 11 a 15 tutean y los 1 a 10
    van en infinitivo), y **los pasos 6 a 10 podrian ser un tercer bloque**.
11. **La frontera 1 a 5 / 6 a 14 de `key_partners_hypothesis` con dos sub bloques sin
    resolver.** Digo que no se si son uno o dos **en vez de elegir**, y eso deja la operacion
    a medias a proposito.
12. **La nota de alcance de `HUGOS-SISTEMAS`**: declaro los nueve como **nomina leida** y no
    como barrido del capitulo sobre los 107. **Alguien puede leer la entrada del inventario
    como si fuera exhaustiva**, y por eso la nota va DENTRO de la entrada.
13. **No escribir `PARA_ALEXIS.md`.** Esa pluma es del auditor (`AUDITOR.md` seccion 4) y la
    regla 4 del `EJECUTOR.md` me manda escribir la parada en el reporte y no arreglarla.

---

## 9. PREGUNTAS (`EJECUTOR.md` regla 11: lo que no puedo medir, lo traigo)

1. **La cifra de censo de `web/lib/engine/graph.test.ts`: se actualiza, se deriva del dato, o
   entra en un mecanismo como el del rojo declarado?** Es la parada. **La casa decide.**
2. **`engine/node_families.json` debe entrar al ciclo escrito de `GATE 0` como cuarto
   comando condicional**, con la misma forma que el comando 3 (*solo cuando la operacion
   cambia el censo*)? Lo corri; **no lo escribi en la pagina de la vara.**
3. **`OP-F-04-HOR`: *familia propia* es nodo propio?** De la respuesta depende si esa tanda
   esta bloqueada o no.
4. **`OP-F-04-WEI` puede quedarse PARCIAL como `OP-F-03`**, o una tanda de `OP-F-04` se
   ejecuta entera o nada? Hoy quedo en **cinco cortes sobre 4 de sus 13 nodos**, con los
   otros nueve nodos con su frontera leida y su destino pendiente. **No escribo cuantos
   cortes son esos nueve porque no lo se:** dos de ellos traen el bloque repetido y uno tiene
   dos sub bloques sin resolver.

---

## 10. LO QUE LA VUELTA DEJA LISTO PARA LA SIGUIENTE

- **Dos planes sellados esperando a que el muro se abra:** `PLAN_V28_RELECTURA.json` (el nodo
  propio de `economia_circular`, con su caso positivo ya probado en las dos direcciones) y
  `PLAN_V27_OPF02.json` (los tres de Mollick, sellado en la vuelta 27 y **verificado por el
  auditor**).
- **Tres instrumentos nuevos**, todos con simulacion por defecto y parada en rojo:
  `vuelta28_mudanza.py` (saca un bloque YA repartido y lo lleva a su destino nuevo, que es lo
  que el recomputo de una relectura conjunta necesita y no existia),
  `vuelta28_declarar.py` (escribe la lista del rojo declarado con sus tres guardas) y
  `vuelta28_caso_positivo.py` (lee los dos esquemas de plan).
- **Las fronteras de nueve bloques de WEI leidas y publicadas**, para que la vuelta que las
  ejecute solo tenga que leer la nomina de destino.
- **`INDICE_ROJO_DECLARADO.jsonl` vacia y `GATE 0` en verde sin excepciones**, que es el
  estado en que la fase III tiene que cerrar segun `08_VERIFICACION.md`.
