# REPORTE de la vuelta 26 del ejecutor (Opus 5). FASE III, EJECUCION, rama `pasada-unica`

**Fecha de corte de TODO lo que va aqui: 14 ago 2026.** Cada cifra y cada nombre propio
salio de un instrumento corrido EN ESTA VUELTA. Donde cito un acta, un reporte o una nota
anterior lo digo y va como CONTRASTE, nunca como fuente (regla 1 de `EJECUTOR.md`).

---

## 0. EL TITULAR

**LA FASE 01 AVANZA HASTA DONDE EL REPO LA DEJA, Y DONDE PARA NO ES POR DOCTRINA: ES POR
UN MURO TECNICO QUE NADIE HABIA MEDIDO.**

| operacion | estado al cerrar esta vuelta |
|---|---|
| **`OP-F-01`** | **EJECUTADA Y HECHA.** Sus cuatro lineas de verificacion en verde, commit `204be669` |
| **`OP-F-02`** | **A MEDIAS, y la mitad hecha es la que la operacion manda hacer PRIMERO**: frontera de los tres publicada y destino decidido por lectura. **El corte NO se hizo**, commit `e7b751b8` |
| **`OP-F-03`** | **A MEDIAS**: los 21 leidos uno a uno con veredicto y frontera, y la fuente corregida en los dos que la tenian mal. **La separacion del bloque NO se hizo**, commit `4430e461` |
| **`OP-F-04-HOR`** | **NO EJECUTADA.** Sus 13 fronteras publicadas verifican 13 de 13 contra el grafo de hoy, pero la separacion **no alcanza para ejecutarse sin decidir** |
| `OP-F-04-COL`, `OP-F-04-WEI`, `OP-F-04-RAC` | **NO EJECUTADAS**, por el mismo muro y la misma falta de metodo de destino |

> **EL MURO, dicho en una linea y medido dos veces: CREAR UN NODO PONE `Gate 0` EN ROJO, Y
> SU REMEDIO ESCRITO NECESITA CREDENCIALES QUE ESTAN FUERA DEL REPO MIENTRAS EL BUCLE
> CORRA.** El chequeo *Todo nodo ACTIVO tiene vector en el indice semantico* es de **cero
> tolerancia**, y el unico instrumento que fabrica vectores es
> `scripts/build_semantic_index_voyage.py`, que pide `VOYAGE_API_KEY`. **Siete de las 71
> operaciones piden crear nodo**, y **cinco de las siete son de la fase 01**.

**ESO ES UNA PARADA DE LA ESPECIE QUE `AUDITOR.md` SECCION 4 NOMBRA ENTERA** (*credenciales
ausentes: si una suite del Gate 0 las necesita, que falle visible: eso es PARADA legitima, y
NO es motivo para devolverlas al repo*). **No devolvi ningun `.env` al repo y no falsee
ningun verde.**

---

## 1. HASH, RUTAS Y ESTADO DE PARTIDA

**HEAD al empezar: `1758706b`**, rama `pasada-unica`, arbol **limpio** y ya empujado.
**No habia nada pendiente que commitear antes de tocar nada** (regla 2).

**HEAD al cerrar: `4430e461`**, mas el commit de este reporte. **Los cuatro commits de
trabajo estan en `origin/pasada-unica`.**

| commit | que trae |
|---|---|
| `79a0bfc7` | TAREA 1: el tercer comando condicional del ciclo de Gate 0 y el calificador de corte del blob |
| `204be669` | **`OP-F-01` ejecutada** |
| `e7b751b8` | **`OP-F-02`**: frontera y destino publicados; el corte no se hizo |
| `4430e461` | **`OP-F-03`**: los 21 leidos y la fuente corregida en dos |

**RUTAS TOCADAS**, y ninguna otra:

| ruta | que se toco |
|---|---|
| `docs/plan/08_VERIFICACION.md` | los dos registros de la TAREA 1 |
| `docs/plan/01_FUENTES.md` | las correcciones declaradas de `OP-F-01`, la frontera y el destino de `OP-F-02`, y la lectura de los 21 de `OP-F-03` |
| `docs/COSTURAS_INTERNAS_RESUMEN.md` | la segunda sede de la cifra de 18, por correccion declarada aditiva |
| `dataset/nodos/` | **DOS ficheros**, y solo el campo `fuente`: `gestion_libro_abierto_obm` y `seleccion_estrategia_pricing` |
| `dataset/metadata/master_graph.json` y `web/lib/assets/` | recompilados y sincronizados por el ciclo de Gate 0 |
| `scripts/loop/` | tres instrumentos nuevos de esta vuelta |
| `docs/loop/` | este reporte y nueve salidas de instrumento |

**CERO cambios en `docs/plan/OPERACIONES.jsonl`.** Ninguna linea del encargo me mandaba
escribir ahi.

---

## 2. TAREA 1: los dos registros y las cinco citas

### 2.1. El tercer comando condicional del ciclo de Gate 0

Añadido en `docs/plan/08_VERIFICACION.md`, **como fila 3 de la tabla del ciclo**:
`python scripts/sync_assets_web.py`, corrido **despues del comando 2** y **solo cuando la
operacion cambia el grafo**. **La vara es doble y por eso se escribe aparte de la del
comando 2: las DOS copias del grafo byte identicas a HEAD**, la del dataset y la de
`web/lib/assets/`. Con su registro: es el remedio escrito del propio validador
(`REMEDIO_SYNC`), no corre en fases que no tocan el grafo, y el motivo por el que el Gate no
puede cazar solo la divergencia recien creada (compara el snapshot de **antes** del paso 6).

> **Y SE USO EN ESTA MISMA VUELTA, en las dos direcciones.** En `OP-F-01`, que no toca el
> grafo, **no lo corri y no fue un rojo**. En `OP-F-03`, que si lo toca, **lo corri**, y las
> dos copias quedaron en el mismo blob `3f5065d3`, que tras el commit **es el de HEAD**.

### 2.2. El calificador de corte del blob de la linea base

En el mismo archivo, **sin borrar el parrafo viejo**: el blob
`bb423c066f5a961f082b3b70aaff4f98d35d7a1d` queda calificado como **REGISTRO HISTORICO**; la
**vara operativa** es *byte identico al HEAD DEL MOMENTO*; y **la cifra que se vigila es el
conteo de 71 etiquetas**, que si es comparable entre vueltas y **si encoge se declara**.
Cierra la pregunta 1 del reporte de la vuelta 24.

> **EL CONTEO NO ENCOGIO EN NINGUNA CORRIDA DE ESTA VUELTA: 71, 71, 71, 71, 71 y 71.** Lo
> declaro aunque no haya pasado nada, porque la definicion registrada obliga a declararlo.

### 2.3. Las cinco correcciones del fundador, citadas y verificadas, no reescritas

**Las cinco existen en el repo y las mire una por una antes de citarlas** (una cita sin
comprobar es una busqueda negativa citada, que la doctrina prohibe):

| # | correccion | donde la verifique hoy |
|---|---|---|
| 1 | la nomina de `OP-F-01` en **SEIS** miembros, sin `background_startup_vs_corporativo` | `OPERACIONES.jsonl`, campo `nodos`, contado hoy: **6** |
| 2 | **`P.17` LA LECTURA VENCE AL METADATO** | `BANCO_DEL_PLAN.md`, seccion propia con su alcance escrito |
| 3 | la correccion declarada sobre la clase LARGO LEGITIMO | `01_FUENTES.md`, dentro de la seccion de `OP-F-01`, con tachado y sin borrar |
| 4 | la **regla de destino por lectura** | `OPERACIONES.jsonl`, nota de `OP-F-02` |
| 5 | el **BACKLOG POST CAMPAÑA** | `docs/PENDIENTES.md`, seccion propia, con las dos preguntas de codigo y la tercera resuelta sin estado nuevo |

> **Y la 5 contesta ademas la pregunta 4 de la vuelta 24**, que llevaba dos vueltas sin
> respuesta: **no se añade estado `ejecutada`**; el commit por operacion es su registro.

---

## 3. LA LINEA BASE, medida antes de tocar nada

| # | comando | resultado de hoy |
|---:|---|---|
| **1** | `python scripts/run_phase1.py --reaplico-curaduria` | **EXITCODE 0** y `GATE 0: OK` |
| **2** | `python scripts/etiquetas_de_cara.py --aplicar` | **71 etiquetas**, blob `8d47ff32d4376f17a5880d7ba56060569856a04a`, **identico a HEAD** en las **dos** copias |

> **CONTRASTE DECLARADO:** el reporte de la vuelta 24 publica ese mismo blob `8d47ff32` como
> el suyo al cerrar. **Mi medicion no lo copia: lo reproduce. Cero discrepancia.**

---

## 4. `OP-F-01`: EJECUTADA Y HECHA

**Es documental**: `eliminar`, `preservar` y `aristas_nuevas` vacios, `superviviente` nulo.
**Su ejecucion es medir, registrar y no tocar un nodo.**

| linea de `verificacion` | resultado de hoy |
|---|---|
| los SEIS tratados por la misma regla, sin excepciones caso por caso | **6 de 6 vivos, cero deprecados. VERDE** |
| ningun nodo de la clase con pasos alterados | **6 de 6 con el conteo identico al publicado. VERDE** |
| la cifra de 18 reescrita con su corte alli donde este publicada | **REESCRITA HOY en sus dos sedes. VERDE** |
| Gate 0 verde | **VERDE** |

**LOS SEIS, medidos hoy:** `seleccion_representante_extranjero` 9,
`internacionalizacion_sitio_web_exportacion` 9, `elaboracion_pro_forma_invoice` 8,
`elementos_plan_exportacion_ejemplo` 13, `principios_medicion_efectiva` 10,
`fmea_analisis_de_modos_de_falla` 8. **Los seis calzan con lo publicado.**

**EL CHOQUE DE LA VUELTA 24 ESTA CERRADO, y lo verifique en vez de suponerlo:** barridas hoy
las 71 operaciones, **ninguno de los seis aparece en ninguna otra**, y
`background_startup_vs_corporativo` aparece **solo en `OP-F-04-HOR`**.

> **AHORA SI LA DECLARO HECHA, y digo por que cambio.** La vuelta 24 la dejo *verde pero no
> hecha* porque su segunda linea se caia el dia que `OP-F-04-HOR` corriera sobre un nodo que
> las dos reclamaban. **Ese nodo ya no esta en la clase**, asi que la segunda linea ya no
> depende de la otra operacion. **Lo que la desbloqueo fue `P.17`, no una medicion mia.**

**LA TERCERA LINEA, ejecutada con su aritmetica al lado.** Contado hoy sobre el campo
`nodos` de las operaciones de fuente: **6 mas 3 mas 21 igual a 30 ids distintos, cero
solape**; y **73 distintos en las siete**, con **43 en las cuatro de la tanda** y cero solape
entre los dos grupos.

| sede | que decia | que dice ahora, por correccion declarada aditiva |
|---|---|---|
| `01_FUENTES.md`, la aritmetica de los dieciocho | formatos lista **7**, total **31** | **6** y **30** |
| `01_FUENTES.md`, tabla de cabecera | *sus SIETE miembros* | **SEIS** |
| `01_FUENTES.md`, el alcance de las siete | *de 31 nodos a 74* | **de 30 a 73** |
| `COSTURAS_INTERNAS_RESUMEN.md` 6 y 7 punto 1 | **31** | **30** |

---

## 5. `OP-F-02`: la mitad que va PRIMERO esta hecha; el corte no

### 5.1. La frontera de los tres, publicada ANTES de cortar

| nodo | pasos | frontera leida | el bloque de Mollick |
|---|---:|---|---|
| `future_scenarios_planning` | 13 | **1 a 5 / 6 a 13** | apendice al final, **y entra DOS VECES** (6 a 9 y 10 a 13) |
| `gut_check` | 9 | **1 a 4 / 5 a 9** | apendice al final |
| `brainstorming_divergente` | 8 | **1 a 4 / 5 a 8** | apendice al final |

**Cada corte va publicado con el paso que cierra el bloque 1 y el que abre el 2**, que es el
metodo de la tabla de los 14 de Horowitz. El primero **no es un simple apendice**: su bloque
de IA entra dos veces, igual que `coeficiente_viral`, **y le toca TOQUE UNICO**.

### 5.2. El destino, decidido por lectura

**Los DIEZ miembros del racimo se leyeron enteros hoy.** El resultado es el mismo en los
tres: **NINGUNO coincide en objeto**, asi que **los tres van a NODO PROPIO dentro del
racimo**.

| bloque | por que ninguno coincide |
|---|---|
| `future_scenarios_planning` 6 a 13 | proyecta lo que la IA **hara**; el bloque del mapa solo prueba lo que **hace hoy** |
| `gut_check` 5 a 9 | **la direccion se invierte**: en los diez el humano supervisa a la IA, aqui la IA audita al humano |
| `brainstorming_divergente` 5 a 8 | el mas cercano es `invitar_ia_a_todo`, pero su objeto es **mapear la frontera probando en todas las tareas**, no generar ideas |

> **LA VARA CON QUE DESCARTE AL MAS CERCANO ES DEL PROPIO RACIMO, no mia**: *una pareja
> vecina se absorbe cuando HACE LO MISMO que un miembro, y no cuando DESARROLLA UNA LINEA
> suya* (`INTRA_DOMINIO_INFORME.md` 11.bis.3, seccion 11.bis.2).

### 5.3. Por que el corte no se hizo

**Los tres destinos son NODO PROPIO, y crear un nodo es exactamente lo que el muro impide.**
Los tres nodos **estan intactos**: cero pasos movidos, cero campos tocados.

---

## 6. `OP-F-03`: los 21 leidos, dos fuentes corregidas, y una clase que la operacion no tenia

**Los 21 vivos y los 21 declarando Hugos en segunda o posterior posicion, reproducido hoy:
la nomina no se movio.** La lectura entera esta en `01_FUENTES.md` con la frontera por nodo.

| veredicto | nodos |
|---|---:|
| **SI es de cadena de suministro** | **12** |
| **NO: la fuente declara un libro cuyo material no aparece** | **2** |
| **TERCERA CLASE: es material de Hugos, pero de su parte de SISTEMAS** | **7** |

**LOS DOS QUE NO, y su fuente ya esta corregida** (tercera linea de verificacion):
`gestion_libro_abierto_obm`, que era el ejemplar de referencia y **se confirma**, y
`seleccion_estrategia_pricing`, **el caso mas limpio de los 21: no hay bloque, los seis pasos
son de Blank de principio a fin**. Simulacion previa sobre copia en memoria, guarda de fuente
esperada antes de escribir, **y cero pasos tocados en los dos**.

**LOS SIETE DE LA TERCERA CLASE** (`bundle_ideas`, `modelo_hibrido_agile_stage_gate`,
`principio_calidad_mvp`, `procesamiento_paralelo_con_espirales`, `propuesta_gasto_capital`,
`reduccion_tamano_de_lote_batch_size`, `schedule_management_plan`) **traen todos el mismo
material**: hitos de 30, 60 y 90 dias, time boxes, reutilizar infraestructura, y justificar
la inversion por beneficios directos, incrementales, de evitacion e intangibles. **Eso es de
Hugos, pero de como se construye un sistema, no de cadena de suministro.** La prueba cruzada:
`transicion_producto_a_experiencia`, que **si** tiene bloque de cadena de suministro, trae
ademas **las tres interfaces de usuario**, de esa misma parte del libro. **El injerto no vino
de un capitulo: vino de dos.**

**LO QUE NO SE HIZO:** la separacion del bloque en los doce que si. **Ni un paso se movio**,
por las dos razones de la seccion 9.

---

## 7. `OP-F-04-HOR` y las otras tres tandas: verificadas por fuera, no ejecutadas

**Lo que si pude verificar y verifique:** las **13** fronteras publicadas en la tabla de los
14 **calzan 13 de 13** contra el grafo de hoy, y los 13 estan vivos. **La primera linea de
verificacion, *cada bloque apendice separado con su frontera de paso escrita*, tiene su
frontera escrita y comprobada; lo que falta es la separacion.**

**Y la familia de destino EXISTE, medida hoy: 88 nodos vivos declaran a Horowitz como fuente
UNICA**, mas los 14 que lo declaran junto a otro libro.

**POR QUE NO LA EJECUTE, y son dos cosas que se suman:**

1. **NO HAY METODO ESCRITO PARA ELEGIR DESTINO DENTRO DE LA FAMILIA.** `P.3` dice *la familia
   de Horowitz, y donde no exista se crea nodo propio*. **Elegir a cual de los 88 va cada uno
   de los 13 bloques es trece decisiones, no trece lecturas**, y el plan **no** tiene para
   `OP-F-04-HOR` la regla que el fundador tuvo que escribir para `OP-F-02` cuando este mismo
   hueco paro la vuelta 24. **La misma especie, sin la misma regla.**
2. **LA SALIDA POR DEFECTO ESTA TAPIADA.** *Donde no exista, se crea nodo propio* es
   justamente lo que el muro impide.

**LO MISMO VALE PARA `OP-F-04-COL`, `OP-F-04-WEI` y `OP-F-04-RAC`**, que el encargo no
nombraba pero que cierran la fase 01: sus verificaciones son **identicas palabra por palabra**
a la de HOR.

---

## 8. EL MURO, medido y reproducido

**EL CHEQUEO:** `run_phase1.py`, paso 7, *Todo nodo ACTIVO tiene vector en el indice
semantico*, **cero tolerancia por decision escrita en su propio comentario** (*un chequeo
AUSENTE y un chequeo VERDE se ven igual en el resumen*).

**LA REPRODUCCION, en arbol de trabajo temporal y NUNCA commiteada:** escribi un nodo de
prueba, corri el ciclo, y el Gate dio

```
[FALLO] Todo nodo ACTIVO tiene vector en el indice semantico
(valor: 1 activos sin vector: ['zzz_prueba_vuelta26_nodo_nuevo'] -> corre el reindex ...)
GATE 0: FALLIDO      EXITCODE 1
```

**Despues borre el nodo, restaure el grafo y volvi a correr el ciclo entero: `GATE 0: OK`,
71 etiquetas, blob identico a HEAD.** La salida esta en `SALIDA_V26_MURO_INDICE.txt`.

**EL REMEDIO Y POR QUE NO PUEDO CORRERLO:** el propio Gate lo escribe,
`python scripts/build_semantic_index_voyage.py && python scripts/sync_assets_web.py`. Ese
script **pide `VOYAGE_API_KEY`**, medido hoy: **no hay `.env` en la raiz y la variable no
esta en el entorno**. **Y no hay segundo instrumento**: el indice vigente es `voyage-4-lite`
de 512 dimensiones con **3.521 ids, exactamente los 3.521 activos**, y mezclar modelos
corromperia el indice.

**EL ALCANCE, barrido sobre las 71 operaciones:** **SIETE piden crear nodo** por su propio
texto: `OP-F-02`, las **cuatro** `OP-F-04`, `OP-D-08` y `OP-D-09`. **Cinco de las siete son
de la fase 01.**

> **Y LA CONTRADICCION QUE ESTO DESTAPA, que es mas grande que la fase 01 y por eso la
> escribo aqui:** `08_VERIFICACION.md` manda **Gate 0 verde entre fases** y a la vez manda
> **el reindexado AL FINAL, despues de mover ids**, con su motivo escrito (*reindexar antes
> deja el indice apuntando a la era anterior*). **Las dos reglas no pueden cumplirse a la vez
> el dia que una operacion cree un nodo**: el Gate lo exige indexado ya, y el plan manda
> indexar al final. **No lo resuelvo yo.**

---

## 9. LAS DOS PARADAS, dichas por separado

**PARADA 1, CREDENCIALES AUSENTES.** Nombrada entera en `AUDITOR.md` seccion 4. Bloquea el
corte de `OP-F-02`, el reparto de las cuatro `OP-F-04`, y el reparto de al menos parte de los
doce de `OP-F-03`. **Que se necesita:** una decision del fundador sobre como se indexan los
nodos que la pasada cree. **No devolvi el `.env` al repo.**

**PARADA 2, TEXTO QUE NO ALCANZA SIN DECIDIR.** Las cuatro `OP-F-04` no tienen metodo escrito
para elegir el destino dentro de la familia, y `OP-F-03` no tiene regla para elegir entre poda
y reparto **ahora que su premisa de *otro tema* falla en cuatro nodos medidos**. Es la misma
especie que el fundador resolvio para `OP-F-02` escribiendo la regla de destino por lectura.

---

## 10. LAS CIFRAS DE ESTADO, recomputadas HOY

**Ninguna sale de un acta ni de un reporte anterior** (`SALIDA_V26_ESTADO.txt`,
`scripts/loop/vuelta26_estado.py`).

**EL MARCADOR**, corte 14 ago 2026: **n 3.388**, **A 583 (17,2 por ciento)**, **B 89 (2,6)**,
**C 7 (0,2)**, **D 2.709 (80,0)**. Puestos **1 a 3.388**, **cero huecos**, **cero
duplicados**, **cero clases fuera de ABCD**.

> **CONTRASTE DECLARADO:** el reporte de la vuelta 24 publica estas mismas cifras. **Mi
> medicion las reproduce, no las copia. Cero discrepancia.**

**TASA DE A POR DOMINIO:**

| dominio | n | A | tasa | B | C | D |
|---|---:|---:|---:|---:|---:|---:|
| core | 1.445 | 344 | **23,8%** | 87 | 7 | 1.007 |
| quality | 844 | 126 | **14,9%** | 0 | 0 | 718 |
| health_safety | 192 | 45 | **23,4%** | 0 | 0 | 147 |
| entrega | 171 | 2 | **1,2%** | 0 | 0 | 169 |
| environmental | 170 | 29 | **17,1%** | 0 | 0 | 141 |
| compras | 155 | 1 | **0,6%** | 2 | 0 | 152 |
| franquicias | 148 | 18 | **12,2%** | 0 | 0 | 130 |
| exportacion | 130 | 15 | **11,5%** | 0 | 0 | 115 |
| risk_management | 106 | 0 | **0,0%** | 0 | 0 | 106 |
| seguridad_digital | 27 | 3 | **11,1%** | 0 | 0 | 24 |

> **LA BANDA QUE TODA TASA DE A LLEVA AL LADO (`P.15`)**, citada con **su corte propio, que
> es anterior al mio**, y con su atribucion: `08_VERIFICACION.md`, corte **12 ago 2026**,
> archivo al puesto **2.117**, autoria del control de la muestra D. El error de dejar pasar
> es **4,2 por ciento**, banda de **0,7 a 20,2**. **No la remedi en esta vuelta y por eso no
> la presento como cifra de hoy.**

**EL GRAFO, recomputado hoy:** **3.835 nodos**, **3.521 vivos**, **314 deprecados**,
**16.800 enlaces**, **15 claves distintas**. **Ninguna cifra del grafo cambio en esta
vuelta**: los dos nodos que toque cambiaron un campo de texto, no un enlace.

**LAS OPERACIONES: 71, 71 ids unicos, cero dependencias rotas, las 71 en `LISTA`.**

**VARA POR TRAMO, FIGURAS Y FAMILIAS: no aplican, y lo digo en vez de rellenarlo.** Esta
vuelta **no leyo un solo par del cribado**: sigue cerrado en 3.388. La unidad de trabajo fue
la operacion.

**LAS SUITES, corridas enteras tras la unica operacion que toco el grafo:**

| suite | comando | resultado |
|---|---|---|
| motor | `python engine/run_all_tests.py` | **exit 0**, `TODOS LOS TESTS PASARON (24/24)` |
| web | `npx vitest run` | **exit 0**, **80 ficheros**, **1.030 pasadas, 3 saltadas** |
| tipos | `npx tsc --noEmit` | **exit 0**, cero lineas |

---

## 11. CORRECCIONES DECLARADAS Y ERRORES PROPIOS

**CORRECCIONES DECLARADAS, todas aditivas y ninguna borra el texto que corrige:**

1. **La cifra de 18**, en sus dos sedes: **31 pasa a 30**, y el alcance de las siete **de 74
   pasa a 73**. Es la tercera linea de verificacion de `OP-F-01`.
2. **El bloque de IA de `future_scenarios_planning` es de OCHO pasos, no de nueve.**
   `INTRA_DOMINIO_INFORME.md` publica *nueve* con su corte anterior; leido hoy contra los
   pasos, el paso 5 es el del Canvas y es de Osterwalder. **Los cinco elementos que aquella
   nota enumera caben todos dentro de mis ocho**: la discrepancia es de conteo, no de
   contenido. **La declaro, no la resuelvo copiando.**
3. **Un tercer y un cuarto ejemplar del defecto de `OP-S-11`**, el mismo libro declarado dos
   veces con dos grafias: `asociaciones_clave` y `transicion_producto_a_experiencia` traen
   *Essentials of Supply Chain Management* y *Essentials of Supply Chain Mana* en la misma
   linea. **El texto que nombraba dos ejemplares no se corrige** (no afirmaba ser
   exhaustivo); esta linea le añade los otros dos.

**ERRORES PROPIOS DE ESTA VUELTA, con nombre:**

1. **Mi primera escritura le quito el salto de linea final a
   `gestion_libro_abierto_obm.json`, que si lo llevaba.** Copie el `save_node` del validador
   sin mirar que **el dataset NO es uniforme**: ese nodo acaba en salto y
   `seleccion_estrategia_pricing` no. **Lo cace en el `git diff` antes de commitear**,
   restaure con `git checkout` y el script ahora preserva el final de fichero tal cual. **Es
   el primo hermano del error que la vuelta 24 declaro, y cayo del otro lado.**
2. **Un filtro de consola me oculto dos pasos de `modelo_hibrido_agile_stage_gate`.** Filtre
   la salida con un `Select-String -NotMatch` para acortarla y el filtro se comio dos lineas
   de paso que contenian una de las palabras filtradas. **Lo cace comparando el conteo
   impreso contra el conteo del nodo**, y añadi al instrumento un modo sin filtros. **De no
   haberlo cazado habria dado un veredicto sobre un nodo leido a medias.**
3. **Corri el comando 1 del ciclo sin el 2 y me asuste del blob.** Vi
   `master_graph.json` con un blob distinto de HEAD y tuve que pararme a entender que era
   **el ciclo a medias**, no una regresion: recompilar borra la curaduria por diseño. **Es
   justo lo que el registro del ciclo dice, y aun asi lo lei mal por un minuto.**

---

## 12. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Diez. Van en el orden en que los decidi. Los tres primeros son los que mas peso tienen.**

1. **Dije que NINGUNO de los diez miembros del racimo coincide con el bloque de
   `brainstorming_divergente`.** Es el mas discutible de la vuelta. **En contra de mi
   lectura:** el bloque dice *usar la IA como un participante mas* y el miembro se llama
   *Invitar Siempre a la IA a la Mesa*; el eco verbal es fuerte. **A favor:** el miembro
   manda **probar la IA en todas las tareas para mapear donde rinde**, y el bloque **genera
   ideas**; por la vara del propio racimo eso es desarrollar una linea, no hacer lo mismo.
   **Si el auditor lo voltea, ese bloque deja de necesitar nodo nuevo y el muro no lo toca.**
2. **Clasifique `gestion_cuentas_por_cobrar` como SI de cadena de suministro**, cuando su
   bloque habla de politica de credito y cobranza. Lo lei como el proceso de credito y
   cobranza de la entrega, y me apoye en que trae **EFT y cartas de credito
   internacionales**, que son instrumentos de comercio y no de finanzas de emprendedor.
   **Si me equivoco, este nodo pasa a los que NO y su fuente habria que corregirla**, igual
   que los otros dos.
3. **Invente una TERCERA CLASE que la operacion no tiene** (siete nodos con material de Hugos
   pero de su parte de sistemas) **en vez de repartirlos a la fuerza entre los dos desenlaces
   escritos**. Podia haber dicho *si* en los siete y dejar el matiz en una nota. No lo hice
   porque los dos remedios escritos **hacen daño**: corregir la fuente borraria una
   atribucion cierta, y repartirlos a la subfamilia Hugos del nucleo los metaria donde no
   son. **Es la desviacion mas grande respecto de la letra de `OP-F-03`.**
4. **Ejecute la tercera linea de `OP-F-03` (corregir la fuente) pero no la segunda (separar
   el bloque).** Se puede leer como ejecutar una operacion a medias. Razon: la tercera es
   completa por si sola y reversible en un campo de texto; la segunda no se sostiene con la
   premisa de `P.3` contradicha por la medicion.
5. **Toque `docs/COSTURAS_INTERNAS_RESUMEN.md`, que `CORRECCIONES_A_APLICAR.md` asigna a la
   SESION A.** La vuelta 24 no lo toco por esa misma razon. Lo hice porque **lo que escribi
   no es la correccion 4 de aquel documento** (esa ya esta aplicada desde el 12 ago): es la
   tercera linea de verificacion de `OP-F-01`, que manda reescribir la cifra **alli donde
   este publicada**, y esa es una de las dos sedes. **Es discutible y lo marco.**
6. **Declare `OP-F-01` HECHA.** La vuelta 24 la dejo *verde pero no hecha* por un choque que
   `P.17` ya cerro. Podia haber esperado al cierre de fase para declararla. **Preferi decir
   que esta hecha y decir exactamente que la desbloqueo.**
7. **Fui a `OP-F-04-COL`, `WEI` y `RAC` sin que el encargo las nombrara.** El encargo nombra
   `OP-F-01`, `02`, `03` y `04-HOR`, y despues dice *con la fase 01 cerrada, sigue*. **La
   fase 01 tiene SIETE operaciones**, asi que las mire para poder decir si la fase cierra o
   no. **No ejecute ninguna.**
8. **Corri la simulacion del muro escribiendo un nodo de verdad en `dataset/nodos/` en vez de
   simularla en memoria.** Es la desviacion mas fea de la vuelta: toque la carpeta de nodos
   con un fichero de mentira. Lo hice porque **una prediccion no es una guarda en rojo**: el
   valor de la parada esta en que el Gate lo dijera el mismo. **Lo borre, restaure y volvi a
   dejar el ciclo en verde con el blob de HEAD, y nada de eso se commiteo.**
9. **Publique la frontera de los tres de Mollick sabiendo que el corte no se iba a hacer.**
   Se puede leer como escribir una frontera que nadie va a usar. La escribi porque la
   operacion manda publicarla **ANTES** de cortar, y porque **si el corte lo hace otra vuelta,
   la lectura ya no hay que rehacerla**.
10. **No escribi `docs/loop/PARA_ALEXIS.md`.** Hay dos paradas y una de ellas necesita al
    fundador. **Esa pluma es del auditor** (`AUDITOR.md` seccion 4) y `EJECUTOR.md` regla 4
    me manda escribir la parada **en el reporte**. Si el criterio es otro, se corrige rapido.

---

## 13. PENDIENTES DE DOCTRINA Y PREGUNTAS

**PENDIENTES DE DOCTRINA (tres, y el de la vuelta 24 se cierra).**

1. **CERRADO el de la vuelta 24**: *un nodo en dos operaciones cuyas verificaciones se
   excluyen*. Lo cerro `P.17` y **lo verifique hoy contra el repo**, no contra el acta.
2. **NUEVO: material del libro declarado, pero de un capitulo que no es el del injerto.** Los
   siete de la tercera clase de `OP-F-03`. **Ni corregir la fuente ni repartir a la
   subfamilia encajan.** No escribo la regla: dejo la lectura con su frontera por nodo.
3. **NUEVO: como se elige el destino dentro de una familia de 88.** `P.3` nombra la familia,
   no el miembro. `OP-F-02` tiene su regla escrita por el fundador; las cuatro `OP-F-04`, no.

**PREGUNTAS (cinco).**

1. **¿Como se indexan los nodos que la pasada cree?** Es la pregunta que desatasca cinco
   operaciones de la fase 01 y dos de la 02. Las salidas que se me ocurren, **y no elijo
   ninguna**: dar la credencial al bucle para reindexar dentro de la pasada; permitir un Gate
   0 con ese unico chequeo en rojo **declarado** mientras dure la fase III, con el reindexado
   al final como ya manda el plan; o partir la pasada en dos, la parte que no crea nodos
   ahora y la que si cuando haya credencial.
2. **¿`P.3` se re mide nodo por nodo para el caso Hugos?** Su tabla dice *otro tema, la poda
   era segura*, y medido hoy **cuatro de los doce son del MISMO tema que el nodo**. Por su
   propia regla, a esos les toca reparto obligatorio.
3. **¿Se escribe para las cuatro `OP-F-04` la misma regla de destino por lectura que
   `OP-F-02` ya tiene?** Si la respuesta es si, la pregunta 1 sigue siendo la que manda,
   porque el fallback de esa regla es crear nodo.
4. **¿La vara del comando 3 se lee contra el HEAD de antes o el de despues del commit?** Tal
   como la escribi dice *las dos copias byte identicas a HEAD*, y el dia que una operacion
   cambia el grafo **eso solo se cumple contra el HEAD que ya trae la operacion**. Hoy lo
   verifique en los dos momentos y lo dejo dicho; el texto no lo distingue.
5. **`SALIDA_V26_MURO_INDICE.txt` queda commiteado con un `GATE 0: FALLIDO`.** Es la prueba de
   la parada, pero leido suelto parece un Gate en rojo sin explicar. **¿Se conserva asi o se
   marca en el nombre?** *(Es la misma especie de la pregunta 5 de la vuelta 24, que sigue sin
   respuesta.)*

---

## 14. ESTADO EN QUE DEJO LA RAMA

- **Rama `pasada-unica`.** HEAD al empezar `1758706b`; **cuatro commits de trabajo**, todos
  en `origin`, mas el commit de este reporte.
- **FASE 0 CERRADA** (sin cambios desde la vuelta 24). **`OP-C-05` sigue DIFERIDA** por su
  `depende_de`.
- **FASE 01: `OP-F-01` HECHA; `OP-F-02` y `OP-F-03` a medias con su mitad documental hecha y
  su corte pendiente; las cuatro `OP-F-04` sin ejecutar.**
- **DOS NODOS TOCADOS EN TODA LA VUELTA**, y solo en su campo `fuente`. **Cero pasos movidos
  en todo el dataset.**
- **GATE 0 VERDE POR EL CICLO ESCRITO**, con el tercer comando corrido donde tocaba: exitcode
  0, `GATE 0: OK`, **71 etiquetas sin encoger en las seis corridas**, y las dos copias del
  grafo en el blob `3f5065d3`, **identico a HEAD**.
- **SUITES EN VERDE:** motor 24 de 24, web 80 ficheros con 1.030 pasadas y 3 saltadas, `tsc`
  limpio.
- **NINGUNA operacion de las fases 02 a 10 se toco.**

> **CONVOCO AL AUDITOR.** Las dos paradas de la seccion 9 son de las que el protocolo reserva:
> una necesita al fundador (credenciales) y la otra necesita doctrina escrita (metodo de
> destino). **Ninguna la resuelvo yo, y no falsee un verde para seguir.**
