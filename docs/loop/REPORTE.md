# REPORTE de la vuelta 22 del ejecutor (Opus 5). FASE III, EJECUCION, rama `pasada-unica`

**Fecha de corte de TODO lo que va aqui: 14 ago 2026.** Toda cifra y todo nombre
propio de este reporte salio de un instrumento corrido EN ESTA VUELTA. Donde cito
un acta o una nota vieja, lo digo y lo pongo como CONTRASTE, nunca como fuente.

---

## 0. EL TITULAR

**TAREA 1 entregada entera. De la TAREA 2, CUATRO operaciones ejecutadas y verdes:
`OP-C-01`, `OP-C-02`, `OP-C-03` y `OP-S-06`. LA QUINTA, `OP-S-07`, ES UNA PARADA
MEDIDA: su texto no alcanza para ejecutarse sin decidir, y lo demuestra el
instrumento, no un argumento.** `OP-C-04` no se toca porque su `depende_de` escrito
es `['OP-S-06', 'OP-S-07']` y una de las dos no esta hecha. `OP-C-05` sigue diferida
por su propio `depende_de`, como el encargo manda.

**`dataset/` termina esta vuelta IDENTICO a HEAD.** Lo que `OP-S-07` inyecto se
restauro con `git checkout` y quedo verificado por hash de blob.

---

## 1. HASH FINAL Y RUTAS TOCADAS

**HEAD al cerrar: `9707a67df5ee1e62c68482aed9f83cec12cba50a`** (`9707a67d`), rama
`pasada-unica`, empujada a `origin/pasada-unica` tras cada tramo.

| # | hash | que trae |
|---|---|---|
| 1 | `557695a7` | TAREA 1: los dos registros |
| 2 | `8b2ba536` | `OP-C-01` ejecutada |
| 3 | `41a9c570` | `OP-C-02` ejecutada |
| 4 | `1578e641` | `OP-C-03` ejecutada |
| 5 | `a1c39585` | `OP-S-06` ejecutada (primera que toca `dataset/`) |
| 6 | `9707a67d` | `OP-S-06`: el ciclo del Gate 0 verificado como PUNTO FIJO |

**RUTAS TOCADAS**

*Registros del plan (TAREA 1):*
`docs/plan/08_VERIFICACION.md`, `docs/plan/OPERACIONES.jsonl`.

*Codigo (TAREA 2):*
`web/lib/engine/graph.ts`, `web/lib/engine/planRedactor.ts`,
`web/lib/engine/recorrido.ts`, `web/lib/compass.ts`,
`web/lib/engine/accesosResueltos.test.ts` (NUEVO),
`web/app/api/organizer/route.ts`, `web/app/api/organizer/stream/route.ts`,
`web/app/api/session/start/route.ts`, `web/app/api/session/[id]/plan/route.ts`,
`web/app/api/project/[id]/world/[pack]/start/route.ts`.

*Grafo (solo `OP-S-06`):* los seis ficheros de `dataset/nodos/` de su nomina, mas
los artefactos que el ciclo recompila (`dataset/metadata/master_graph.json`,
`web/lib/assets/master_graph.json`, `web/lib/assets/manifest.json`).

*Salidas de instrumento, todas en `docs/loop/`:* `SALIDA_V22_GATE0_BASE.txt`,
`SALIDA_V22_ETIQUETAS_BASE.txt`, `SALIDA_V22_OPC01_ROJO.txt`,
`SALIDA_V22_OPC01_VERDE.txt`, `SALIDA_V22_OPC01_MOTOR.txt`,
`SALIDA_V22_GATE0_OPC01.txt`, `SALIDA_V22_OPC02_ROJO.txt`,
`SALIDA_V22_OPC02_VERDE.txt`, `SALIDA_V22_OPC02_MOTOR.txt`,
`SALIDA_V22_GATE0_OPC02.txt`, `SALIDA_V22_OPC03_ROJO.txt`,
`SALIDA_V22_OPC03_VERDE.txt`, `SALIDA_V22_OPC03_MOTOR.txt`,
`SALIDA_V22_GATE0_OPC03.txt`, `SALIDA_V22_OPS06_SIMULACION.txt`,
`SALIDA_V22_OPS06_EJECUCION.txt`, `SALIDA_V22_OPS06_VERIFICACION.txt`,
`SALIDA_V22_OPS06_VERDE.txt`, `SALIDA_V22_GATE0_OPS06.txt`,
`SALIDA_V22_GATE0_OPS06_PUNTOFIJO.txt`, `SALIDA_V22_OPS07_SIMULACION.txt`,
`SALIDA_V22_OPS07_EJECUCION.txt`, `SALIDA_V22_OPS07_VERIFICACION.txt`,
`SALIDA_V22_OPS07_CAUSA.txt`, `SALIDA_V22_GATE0_OPS07.txt`,
`SALIDA_V22_GATE0_TRAS_RESTAURAR.txt`, `SALIDA_V22_MARCADOR.txt`.

---

## 2. TAREA 1: los dos registros (commit `557695a7`)

### 2.1. `08_VERIFICACION.md`: que es GATE 0 EN VERDE

Seccion nueva bajo LA VERIFICACION TRANSVERSAL, **aditiva**: no se borro una linea.
El criterio registrado es **EL CICLO ESCRITO DE DOS COMANDOS**, no la invocacion a
secas:

1. `python scripts/run_phase1.py --reaplico-curaduria` con **EXITCODE 0** y `GATE 0: OK`.
2. `python scripts/etiquetas_de_cara.py --aplicar` justo despues, dejando
   `dataset/metadata/master_graph.json` **byte identico a HEAD**.

**MEDIDO HOY, no copiado del acta:** el comentario fechado 2026-08-07 esta en
`scripts/run_phase1.py` **lineas 941 a 958** y `Quien recompila, reaplica` en la
**linea 955**. Las dos cifras las lei del archivo con `awk` numerando lineas, y
salen identicas a las que el acta de la vuelta 21 adjudico. **Cero discrepancia.**

**La linea base del ciclo, corrida hoy sobre `bd782052`:** EXITCODE 0, `GATE 0: OK`,
**71 etiquetas reaplicadas**, blob `bb423c066f5a961f082b3b70aaff4f98d35d7a1d`,
identico al de HEAD. Esa cifra de 71 quedo escrita en la pagina como la vara contra
la que se mide el encogimiento.

### 2.2. `OPERACIONES.jsonl`: las dos notas

Las dos son **ADITIVAS y verificadas por `assert` dentro del propio script**: el
texto viejo queda entero como prefijo del nuevo.

| operacion | nota antes | nota despues | que dice lo anadido |
|---|---:|---:|---|
| `OP-C-04` | 1.249 car. | 1.842 car. | la sede del caso positivo es EL ARBOL DE TRABAJO TEMPORAL, nunca commiteado, restaurado a HEAD acto seguido con la salida guardada como prueba |
| `OP-C-05` | 1.254 car. | 1.766 car. | se queda en la fase 0, DIFERIDA por su `depende_de` escrito (`OP-S-12`), sin bloquear nada y sin cambio de fondo |

Tras el cambio, remedido: **71 operaciones, 71 ids unicos, cero dependencias rotas.**
El fichero hace round trip byte identico en las 71 lineas, asi que solo cambiaron las
dos tocadas (`git diff --stat`: 2 inserciones, 2 borrados).

---

## 3. TAREA 2, operacion por operacion

**El paquete de cada una fue el mismo:** simulacion o medicion previa, el arreglo tal
como esta escrito, caso positivo con su ROJO guardado ANTES del arreglo, suites
enteras, y GATE 0 VERDE POR EL CICLO ESCRITO tras cada operacion.

### 3.1. `OP-C-01` (commit `8b2ba536`)

**Los tres arreglos escritos, ni uno mas:**

1. `aMaterial` (`planRedactor.ts:52`) resuelve al entrar, con el patron ya escrito
   en la casa: `resolverId(nid, graph) ?? nid`, el de `etiquetaArbol` y
   `tituloDeNodo`.
2. Los DOS organizadores piden `cargarEntrySeeds(graph)`. La funcion **ya** filtraba
   por `esOfrecible` al recibir el grafo y nadie se lo pasaba en el unico camino por
   el que entra un usuario nuevo.
3. `compass.ts` **resuelve antes de puntuar** y descarta lo que resuelve a `null`.
   Ahi muere el unico HUECO AL REVES del inventario: el `opts.graph[id] &&` hacia
   falsa la condicion entera ante un id desconocido, o sea que **pasaba** en vez de
   caer.

**CASO POSITIVO:** 8 pruebas nuevas en rojo antes del arreglo
(`SALIDA_V22_OPC01_ROJO.txt`: 8 failed, 4 passed), verdes despues.
**GATE 0:** EXITCODE 0, `GATE 0: OK`, 71 etiquetas, blob `bb423c06...`, igual a HEAD.
**SUITES:** web 80 archivos, 1.015 verde y 3 saltados; motor 24/24; `tsc --noEmit` limpio.

### 3.2. `OP-C-02` (commit `41a9c570`)

**Los dos arreglos escritos:** la linea 267 de la ruta del plan **resuelve** en vez
de filtrar con `nid in graph`; la 405 **resuelve** antes de leer `fase_proyecto` en
vez de caer al `?? "ideacion"`.

**CASO POSITIVO:** 4 pruebas en rojo (`SALIDA_V22_OPC02_ROJO.txt`: 4 failed, 14 passed),
verdes despues.
**GATE 0:** EXITCODE 0, `GATE 0: OK`, 71 etiquetas, blob igual a HEAD.
**SUITES:** web 1.021 verde y 3 saltados; motor 24/24; `tsc` limpio.

### 3.3. `OP-C-03` (commit `1578e641`)

**Los cuatro arreglos escritos:** `resumenNodo` resuelve al entrar; `recorrido.ts`
resuelve antes de `obtenerPregunta` en **los dos sitios** de la nomina (271 y 649);
`clasificar.ts` recibe los seeds ya pasados por la puerta unica (el arreglo esta en
quien los carga, `session/start/route.ts`); y el arranque de mundo cambia el criterio
de **existir** a **resolver**.

**Hallazgo util:** `preguntaDeNodo` arregla **dos** averias de la misma linea, no una.
`graph[nid]` reventaba con un id de la era en que fusionar borraba, y aunque no
reventara, `cache[nid]` no encontraba la pregunta **curada** del superviviente y
entregaba la plantilla generica.

**CASO POSITIVO:** 6 pruebas en rojo (`SALIDA_V22_OPC03_ROJO.txt`: 6 failed, 21 passed),
verdes despues.
**GATE 0:** EXITCODE 0, `GATE 0: OK`, 71 etiquetas, blob igual a HEAD.
**SUITES:** web 1.030 verde y 3 saltados; motor 24/24; `tsc` limpio.

### 3.4. `OP-S-06` (commits `a1c39585` y `9707a67d`)

**Primera operacion de la pasada que toca `dataset/`, y lo hace porque su texto lo
ordena.**

**SIMULACION PREVIA (P.7), sobre copia en memoria y cero escrituras.** Barrido del
CATALOGO ENTERO, 3.835 nodos, no de la nomina copiada:

| | escrita en `OP-S-06` | **medida hoy** | coincide |
|---|---|---|---|
| claves de fase sucias | 2 | **2** | si |
| nodos con `fuentes_adicionales` | 4 | **4** | si |
| nomina total | 6 nodos | **los mismos 6** | **exacta** |

Y una cosa que la simulacion probo antes de borrar nada: **las dos claves sucias
llevaban EL MISMO VALOR que su `fase_proyecto`** (`ejecucion` y `validacion`), asi
que el motor leia la buena y la sucia viajaba de polizon. **No se perdio un dato.**

**El separador de `fuente` NO SE INVENTO, SE MIDIO.** Sobre los 3.835: **70 nodos**
separan LIBROS con ` | ` (entre ellos los 21 de `OP-F-03`) y los **235** que llevan
`; ` lo usan para separar COAUTORES dentro de un mismo libro (`Out of the Crisis,
Reissue - Deming, W. Edwards; Cahill, Kev`). El ` | ` es la convencion de la casa.

**LA VERIFICACION ESCRITA, corrida contra LAS TRES SEDES del grafo** (`dataset/nodos`,
`dataset/metadata/master_graph.json` y la copia de la web), en
`SALIDA_V22_OPS06_VERIFICACION.txt`:

| linea escrita en `OP-S-06` | resultado en las tres sedes |
|---|---|
| ningun nodo tiene dos claves de fase | **0** |
| ningun nodo conserva `fuentes_adicionales` | **0** |
| los cuatro declaran en `fuente` lo que tenian repartido | **0 ausencias** |
| el motor sigue leyendo `fase_proyecto` | **3.835 de 3.835** |

**El catalogo pasa de 18 a 15 claves distintas**, y `merged_originals` (269 nodos) se
queda, porque `OP-C-04` lo mete DENTRO de la lista blanca por la letra corregida del
14 ago 2026.

**GATE 0, y aqui hay una lectura que declaro en vez de dar por hecha:** el blob de
`master_graph.json` **SI se movio**, de `bb423c06...` a `6007c1da...`, **y debe
moverse**: la operacion cambia el grafo a proposito. Lo que la definicion registrada
prohibe es que **EL CICLO** mueva el grafo por su cuenta, y eso lo verifique aparte en
el commit `9707a67d`: **corrido el ciclo entero contra el HEAD que ya contiene la
operacion, sale EXITCODE 0, `GATE 0: OK`, 71 etiquetas, y el blob vuelve a ser
`6007c1da864ef625796a47cab126a1d717610ffd`, el de HEAD. EL CICLO ES PUNTO FIJO.**

**El orden del remedio fue el escrito** en `run_phase1.py` lineas 859 a 867:
recompilar, reaplicar la curaduria, y SOLO ENTONCES `sync_assets_web.py`. Sincronizar
a secas habria empujado la copia atrasada sobre la buena y estropeado la voz.

**SUITES:** web 1.030 verde y 3 saltados; motor 24/24.

---

## 4. LA PARADA: `OP-S-07` no se puede ejecutar tal como esta escrita

### 4.1. Lo que la simulacion previa confirmo, numero por numero

La nomina de `OP-S-07` **es correcta y esta viva**. Reimplemente el resolutor del
motor linea a linea desde `web/lib/engine/graph.ts` (`mapaDeAlias` 100 a 120,
`resolverId` 131 a 152) y medi:

| | escrito en `OP-S-07` | **medido hoy** |
|---|---|---|
| enlaces que resuelven al propio nodo, en vivos | 33 | **33** |
| nodos | 27 | **27** |
| directas | 0 | **0** |
| via alias | 33 | **33** |
| el peor, `costo_de_mala_calidad_copq` | 7 (2 previos, 5 siguientes) | **7 (2 y 5)** |
| la nomina de 27 ids | escrita | **identica, id por id** |

El ejemplar escrito tambien calza: `analisis_flujo_de_valor` lleva
`value_stream_analysis_lean` en sus `nodos_previos`, y ese id es su propio alias.

### 4.2. Lo que paso al ejecutarla

Retire los **33** enlaces exactos, ni uno mas: 27 nodos tocados, `ids_alias`
intactos en los 3.835, conteo del grafo de **16.866 a 16.833**, baja de 33 exacta
(`SALIDA_V22_OPS07_EJECUCION.txt`).

**Y despues corri el Gate 0, y los 33 VOLVIERON.** La verificacion escrita de la
propia operacion (`ningun nodo vivo se cita a si mismo... NI tras resolver alias`)
salio **en rojo con 33** en las tres sedes, y el conteo de enlaces volvio a 16.866.

### 4.3. La causa, MEDIDA y no supuesta

`dataset/metadata/phase1_run_log.json` de esa corrida trae el campo
`symmetrize_added` con **exactamente los 33 enlaces**, uno a uno, con su nodo y su
campo. El **paso 5 de `run_phase1.py`** (simetrizar, lineas 396 a 435) exige que toda
arista tenga su vista reciproca, y **la fabrica** si falta.

**Y de las 33, las 33 son la vista reciproca de un enlace que el GEMELO DEPRECADO
tiene hacia su propio superviviente.** Medido: `value_stream_analysis_lean` esta
deprecado, su `nodos_siguientes` contiene `analisis_flujo_de_valor`, y por eso el
paso 5 repone `value_stream_analysis_lean` en los `nodos_previos` del vivo.
**33 de 33, cero excepciones.**

> **La auto-arista no esta escrita a mano en el nodo vivo. Es la sombra que el paso 5
> proyecta desde el nodo deprecado. Borrar la sombra sin tocar lo que la proyecta es
> trabajo que se deshace solo en la siguiente corrida, siempre.**

### 4.4. Por que esto es PARADA y no una decision mia

`OP-S-07` escribe **dos cosas que hoy no pueden ser verdad a la vez**:

- **(a)** `eliminar`: *"de cada uno de los 27, el enlace ... 33 enlaces en total.
  **No se toca ningun otro campo**"*.
- **(b)** `verificacion`: *"ningun nodo vivo se cita a si mismo como previo o
  siguiente, NI directamente NI tras resolver alias"* mas *"el conteo de aristas del
  grafo baja en **33 exactamente**"*, con **Gate 0 verde**.

Medido hoy: **(a) ejecutado al pie de la letra NO produce (b)**, porque el paso 5 lo
revierte. Y las dos salidas que si producirian (b) **reescriben la letra de (a) o una
cifra publicada**:

| camino | que rompe | cifra medida hoy |
|---|---|---|
| retirar tambien el enlace del gemelo deprecado | rompe *"no se toca ningun otro campo"* | el grafo bajaria en **114**, no en 33 (33 en vivos mas **81 en deprecados**, sobre **59 nodos** deprecados) |
| ensenar al paso 5 a no fabricar una reciproca que resuelve al propio nodo | toca `run_phase1.py` sin que ninguna operacion lo ordene; `OP-C-04` ordena **anadir una guarda** a Gate 0, no cambiar el simetrizador | no medida: es codigo nuevo |
| diferir `OP-S-07` | contradice su `bloquea_a` escrito (`['OP-C-04']`) y deja la fase 0 sin cerrar | |

**Es la especie exacta que el encargo nombra: "cualquier operacion cuyo texto no
alcance para ejecutarse sin decidir, te detiene a ti y convoca al auditor".** No
elegi ninguno de los tres caminos.

### 4.5. Que hice al parar

**Pare `OP-S-07`, no parti la fase** (`OP-C-04` depende de ella y no se toco;
`OP-C-05` sigue diferida). **Restaure `dataset/` con `git checkout -- dataset/
web/lib/assets`** y lo verifique por hash: blob `6007c1da864ef625796a47cab126a1d
717610ffd`, el de HEAD. Despues volvi a correr el ciclo entero del Gate 0 sobre el
arbol restaurado: **EXITCODE 0, `GATE 0: OK`, 71 etiquetas, blob identico a HEAD**
(`SALIDA_V22_GATE0_TRAS_RESTAURAR.txt`). **Nada de `OP-S-07` quedo commiteado.** Sus
salidas si quedan, como prueba.

### 4.6. Una nota que el auditor querra tener delante

El fenomeno tiene **hermano medido**: hay **81 aristas mas** de la misma especie
escritas en **59 nodos DEPRECADOS**. La verificacion de `OP-S-07` habla solo de nodos
**VIVOS**, asi que esas 81 no estan cubiertas por su texto. **No las toque y no las
propongo: las declaro**, porque cualquier salida que el auditor elija para las 33
tiene que decir tambien que hace con las 81.

---

## 5. LAS CIFRAS DE ESTADO, recomputadas HOY (`SALIDA_V22_MARCADOR.txt`)

**Ninguna sale de un acta ni de un reporte anterior.**

**EL MARCADOR** (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`), corte 14 ago 2026:
**n 3.388**, **A 583 (17,2 por ciento)**, **B 89 (2,6)**, **C 7 (0,2)**,
**D 2.709 (80,0)**. Puestos 1 a 3.388, **cero huecos y cero duplicados**, y ninguna
clase fuera de ABCD.

> **Contraste declarado:** el acta de la vuelta 21 publica exactamente estas mismas
> cifras. Mi medicion de hoy no las copia, las reproduce. **Cero discrepancia.**

**TASA DE A POR DOMINIO**, recomputada del archivo:

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

> **Y la banda que toda tasa de A tiene que llevar al lado** (`08_VERIFICACION.md`,
> corte 12 ago 2026, archivo al puesto 2.117, autoria del control de la muestra D):
> el error de dejar pasar es **4,2 por ciento**, banda de **0,7 a 20,2**. La cito con
> su corte propio, que es anterior al mio: **no la remedi en esta vuelta.**

**EL GRAFO**, recomputado: **3.835 nodos**, **3.521 vivos**, **314 deprecados**,
3.835 ficheros en `dataset/nodos`, **16.866 enlaces**, **15 claves distintas** (eran
18 antes de `OP-S-06`).

**LAS OPERACIONES**: **71, 71 ids unicos, cero dependencias rotas**, y **las 71 en
estado `LISTA`** (ver la pregunta 1 de la seccion 8).

**VARA POR TRAMO, FIGURAS Y FAMILIAS:** no aplican a esta vuelta y lo digo en vez de
rellenarlo. **Esta tanda no leyo un solo par**: el cribado sigue cerrado en 3.388 y
los veredictos no se abrieron. La unidad de trabajo de esta vuelta fueron
operaciones de la fase 0, no puestos.

---

## 6. CORRECCIONES DECLARADAS

**Ninguna correccion de una cifra publicada.** Cada cifra que remedi contra su acta o
su nota (las lineas 941 a 958 y 955 de `run_phase1.py`, las 33 auto-aristas, los 27
nodos, las 6 claves sucias, el marcador entero) **salio identica**. Lo unico que este
reporte anade sobre lo publicado es material NUEVO y medido: la causa del rebote de
las 33 y las 81 del lado deprecado.

**Errores propios de esta vuelta, con nombre:**

1. **Mi primer barrido de claves dio "sin claves de fase sucias" donde hay dos.**
   Reviento con `UnicodeEncodeError` de cp1252 al imprimir un valor con acentos, y
   la salida se corto **despues** de la tabla de claves y **antes** de la lista de
   sospechosos. Leerla como completa habria sido publicar una busqueda negativa que
   nunca termino. **No se publico**: quedo cazado en la corrida siguiente con
   `sys.stdout.reconfigure(encoding="utf-8")`, y el barrido bueno encontro las dos.
   Es exactamente la trampa que el acta de la vuelta 20 ya dejo escrita.
2. **Mi primer intento de leer el marcador uso el campo `puesto`, que no existe.**
   El campo es `puesto_intra`. Reviento con `IndexError` y quedo corregido en la
   misma corrida. No alcanzo una cifra publicada.
3. **Un reemplazo de texto sobre `start/route.ts` fallo por fin de linea:** busque
   un patron de dos lineas con `\n` sobre un archivo CRLF y el `assert` lo paro sin
   escribir nada. Corregido detectando el fin de linea del archivo.

---

## 7. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Once. Van en el orden en que los decidi.**

1. **`aMaterial` devuelve el `id` DE LA RUTA y no el resuelto.** Resolvi solo para
   LEER el nodo. Razon: `verificarProcedenciaEtapas` y `nodosPorEtapaValidados`
   validan lo que el redactor autodeclara contra `ruta + cosecha` **crudas**;
   devolver el resuelto habria marcado como alucinacion una procedencia legitima, o
   sea habria arreglado el concepto rompiendo el sensor. **Puse una prueba que fija
   esa identidad**, para que la decision quede custodiada y no dependa de que alguien
   la recuerde.
2. **Lo mismo en `resumenNodo`**: el `id` que sale es el que se pidio.
3. **Anadi dedupe por id resuelto en `compass.ts`.** El absorbido y su superviviente
   estan los dos indexados; sin dedupe, tras resolver se ofrecerian dos veces. No lo
   pide el texto de la operacion, pero es consecuencia directa de resolver.
4. **Separe la decision de la brujula en `seleccionarAfines`, exportada.** Sin eso el
   caso positivo de `compass.ts` habria sido solo un `grep` sobre el fuente:
   `buscarAfines` entera necesita clave y red, y una prueba contra ella pasaria verde
   SIN PROBAR NADA. El precedente esta escrito en `puertaUnica.test.ts`, CAMINO 3.
5. **Extraje `conceptosDeRuta`, `faseDeNodo` y `preguntaDeNodo` a `graph.ts`**, y las
   rutas las llaman. Las expresiones vivian EN LINEA dentro de manejadores de API que
   no se pueden probar sin levantar Supabase, la API y la sesion. **Es cambio de
   sede, no de alcance**, y las deje hermanas de `etiquetaArbol` y `tituloDeNodo`,
   que es donde la casa ya pone esta clase de funcion.
6. **Ensanche el tipo del parametro de `resolverId` a `GrafoResoluble`** (la forma
   minima que mira). Es el mismo movimiento que `esOfrecible` ya tiene escrito y
   razonado en su propio comentario. `Grafo` la satisface entera y **ningun caller
   cambia**.
7. **En el arranque de mundo, el mundo arranca EN EL NODO QUE RESUELVE**, no en el id
   viejo: `puerta_entrada`, `actualId` y la puerta usan el resuelto. Si dejara el
   viejo, cambiaria un 503 ruidoso por un recorrido MUDO: `sucesoresNivel` usa
   `graph[nid]?.` y devolveria lista vacia. **Cambiar un fallo ruidoso por uno mudo
   es justo lo que el canon prohibe.**
8. **NO toque `recorrido.ts:549`** (`obtenerPregunta(reeleccion.puertaId, ...)`), que
   tiene la misma forma que los dos que si arregle. Razon: **no esta en la nomina de
   `OP-C-03`**, y su id no viene de fuera sino de la reeleccion calculada en proceso,
   que es el criterio con el que `OP-S-08` clasifico los 42 accesos. Lo declaro en
   vez de arreglarlo callado. **Lo mismo con `follow/route.ts:232`**, que tambien pide
   `cargarEntrySeeds()` sin grafo y no esta en ninguna de las tres nominas.
9. **Cuatro pruebas de `OP-C-01`, una de `OP-C-02` y tres de `OP-C-03` PASAN antes y
   despues del arreglo.** No son casos positivos y no las presento como tales: son
   guardas del contrato que el arreglo NO debe romper (la identidad del material y
   del resumen, la convencion de que sin grafo no se filtra, el defecto legitimo de
   `ideacion` para el id que jamas existio). **Borrarlas para que la cuenta quedara
   limpia habria sido peor que declararlas.**
10. **Interprete "byte identico a HEAD" como PUNTO FIJO DEL CICLO** cuando la
    operacion cambia el grafo a proposito, y lo verifique en un commit aparte contra
    el HEAD que ya contiene la operacion. La lectura literal (identico al HEAD
    ANTERIOR) haria imposible ejecutar cualquier operacion de las fases 01 a 07.
11. **Anadi `python scripts/sync_assets_web.py` al cierre de `OP-S-06`**, que no esta
    en los dos comandos de la definicion de Gate 0 verde. Lo trato como parte de
    ESCRIBIR el grafo, no del criterio: sin el, las dos copias divergen y el propio
    Gate 0 lo canta. El orden que segui es el que `run_phase1.py` deja escrito en sus
    lineas 859 a 867.

---

## 8. PENDIENTES DE DOCTRINA Y PREGUNTAS

**PENDIENTE DE DOCTRINA (uno).**

- **Que hace una operacion de saneo cuando el propio Gate 0 REPONE lo que ella
  retira.** Ninguna regla escrita lo cubre. `P.16` ("quien fabrica, limpia") gobierna
  las fusiones QUE VIENEN y dice expresamente que las 33 de hoy **siguen siendo
  trabajo de `OP-S-07`**. La nota de `OP-S-07` anticipo que la guarda debe RESOLVER y
  no comparar, pero **no anticipo el simetrizador**. Registro el pendiente y **no
  invento la regla**.

**PREGUNTAS (cuatro).**

1. **El plan no tiene estado para "ejecutada".** Las 71 operaciones siguen en `LISTA`
   y cuatro ya corrieron. Ninguna instruccion me manda moverlas y **no las movi**.
   ¿Se anade un estado, se marca por commit, o se deja asi hasta el cierre de fase?
2. **Las 81 del lado deprecado** (seccion 4.6): ¿entran en `OP-S-07` cuando se
   adjudique su salida, o son operacion aparte?
3. **`git status` marca `dataset/metadata/master_graph.json` como modificado tras
   correr el ciclo, mientras `git diff` y `git hash-object` dicen que es identico a
   HEAD.** Es artefacto del filtro CRLF y del cache de `stat`, no contenido: lo
   comprobe con `git diff --quiet` (exit 0) y con el hash de blob. **La vara buena es
   el hash de blob, que es lo que la definicion registrada pide.** ¿Se deja escrito
   asi, para que nadie lea un falso movimiento del grafo en una vuelta futura?
4. **`SALIDA_V22_OPS07_VERIFICACION.txt` quedo commiteado con su resultado en ROJO**,
   porque es la prueba de la parada. ¿Se conserva asi o se renombra para que nadie lo
   confunda con una verificacion fallida sin explicar?

---

## 9. ESTADO EN QUE DEJO LA RAMA

- **HEAD `9707a67d`**, `pasada-unica`, empujado a `origin`.
- **Arbol limpio salvo las salidas de instrumento de esta vuelta**, que se commitean
  con este reporte.
- **`dataset/` IDENTICO a HEAD**, verificado por hash de blob
  (`6007c1da864ef625796a47cab126a1d717610ffd`) tras restaurar.
- **GATE 0 VERDE POR EL CICLO ESCRITO**, corrido por ultima vez sobre el arbol
  restaurado: EXITCODE 0, `GATE 0: OK`, **71 etiquetas reaplicadas, sin encoger en
  ninguna de las seis corridas de la vuelta**.
- **SUITES EN VERDE**: web 1.030 pasadas y 3 saltadas, motor 24/24, y el guardian de
  `.githooks/pre-commit` corrio las dos en cada uno de los seis commits.
- **FASE 0: cuatro de siete hechas** (`OP-C-01`, `OP-C-02`, `OP-C-03`, `OP-S-06`),
  **`OP-S-07` PARADA**, **`OP-C-04` bloqueada por su `depende_de`**, **`OP-C-05`
  diferida por el suyo**. La fase 0 **no** esta cerrada, y ninguna operacion de las
  fases 01 a 07 se toco.
