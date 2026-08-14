# REPORTE de la vuelta 23 del ejecutor (Opus 5). FASE III, EJECUCION, rama `pasada-unica`

**Fecha de corte de TODO lo que va aqui: 14 ago 2026.** Cada cifra y cada nombre propio
de este reporte salio de un instrumento corrido EN ESTA VUELTA. Donde cito el reporte
de la vuelta 22 o un acta, lo digo y lo pongo como CONTRASTE, nunca como fuente.

---

## 0. EL TITULAR

**EL ENCARGO QUE RECIBI YA ESTABA EJECUTADO. `docs/loop/PROMPT_SIGUIENTE.md` es BYTE
IDENTICO al encargo de la vuelta 22, y lo demuestra el hash de blob, no una impresion:
`362492c3b145e2d1643a3db9b0659fdd03364b7b` en el commit `bd782052`, en `HEAD` y en el
disco, con CERO commits que lo hayan tocado desde entonces.** La causa esta medida en la
seccion 1: **la sesion del auditor de la vuelta 22 murio con un error de API antes de
escribir su acta y antes de escribir el encargo nuevo.**

**Lo que hice, y por que no es rellenar:** por la regla 1 de `EJECUTOR.md` (EL
INSTRUMENTO MANDA) nada de la vuelta 22 es fuente de una cifra mia. Asi que **corri el
encargo entero otra vez contra el HEAD de hoy**, midiendo todo desde cero. Resultado:

- **TAREA 1: los dos registros estan puestos y verificados hoy.** No los duplique.
- **`OP-C-01`, `OP-C-02`, `OP-C-03`, `OP-S-06`: verificadas vivas en el codigo de hoy**,
  con Gate 0 verde por el ciclo escrito y las tres suites en verde.
- **`OP-S-07`: LA PARADA SE REPRODUCE, y la reproduje ejecutandola, no leyendola.**
  Retire los 33 enlaces, corri Gate 0, y **los 33 volvieron**. La causa quedo medida
  contra el log del propio validador.
- **`OP-C-04`: BLOQUEADA por su `depende_de` medido hoy** (`['OP-S-06', 'OP-S-07']`).
- **`OP-C-05`: DIFERIDA por el suyo** (`['OP-S-12']`), como el encargo manda.

**`dataset/` termina esta vuelta IDENTICO a HEAD**, verificado por hash de blob tras
restaurar. **Nada de `OP-S-07` quedo commiteado.**

**Y traigo material NUEVO Y MEDIDO que corrige una lectura del reporte anterior:** la
cifra de 81 auto aristas del lado deprecado **no existe bajo el criterio que la
verificacion de `OP-S-07` tiene escrito**. Existe bajo otro criterio, que nadie ha
escrito todavia. Seccion 5.

---

## 1. POR QUE EL ENCARGO LLEGO REPETIDO, MEDIDO

| que mire | comando | resultado de hoy |
|---|---|---|
| el encargo en `HEAD` | `git rev-parse HEAD:docs/loop/PROMPT_SIGUIENTE.md` | `362492c3b145e2d1643a3db9b0659fdd03364b7b` |
| el encargo en `bd782052` (el de la vuelta 22) | `git rev-parse bd782052:...` | **el mismo blob** |
| el encargo en el disco | `git hash-object ...` | **el mismo blob** |
| quien lo toco desde `bd782052` | `git log bd782052..HEAD -- ...` | **nadie, cero commits** |
| el acta de la vuelta 22 | `grep -cin "vuelta 22" docs/loop/ACTA_AUDITOR.md` | **0** |
| la ultima cabecera del acta | `grep -n "^## "` | **`VUELTA 21`**, linea 4.579 |

**LA CAUSA, leida de `docs/loop/ultimo_auditor.json`:** `"is_error": true`,
`"terminal_reason": "api_error"`, `"result": "API Error: Connection lost mid-response.
The response above may be incomplete."`, modelo `claude-fable-5`, `duration_ms` 851.409.
**El auditor de la vuelta 22 se corto a mitad de respuesta.** Por eso no hay acta 22 y
por eso `PROMPT_SIGUIENTE.md` sigue siendo el de la 22.

`docs/loop/ultimo_ejecutor.json` esta **vacio, cero bytes**, asi que no da informacion.

> **ESTO NO ES UNA PARADA POR CONTRADICCION.** Un encargo repetido no contradice ninguna
> regla vigente ni ninguna cifra publicada. Lo trato por la regla 1: **vuelvo a medirlo
> todo**, y lo declaro aqui arriba para que nadie lea esta vuelta como una vuelta nueva
> de trabajo nuevo. **La decision de que hacer con el bucle es de quien tiene esa pluma,
> no mia** (seccion 8, pregunta 1).

---

## 2. HASH, RUTAS Y ESTADO DE PARTIDA

**HEAD al empezar y al cerrar el trabajo de medicion: `f151051c75ca61ece33cb25b860c0f3e10ea1584`**
(`f151051c`), rama `pasada-unica`, **ya empujada a `origin/pasada-unica`** (los dos hashes
coinciden; `git log origin/pasada-unica..HEAD` sale vacio).

**LO PENDIENTE ANTES DE TOCAR NADA (regla 2):** `git status` marcaba
`dataset/metadata/master_graph.json` como modificado. **No habia nada que commitear:**
`git diff --quiet` salio con **exit 0** y el hash de blob del disco es identico al de
HEAD. Es el artefacto de CRLF que la vuelta 22 ya dejo descrito en su pregunta 3, y hoy
vuelve a medirse igual.

**RUTAS TOCADAS EN ESTA VUELTA:** ninguna de `dataset/`, ninguna de `web/`, ninguna de
`scripts/`, ninguna de `docs/plan/`. **Solo `docs/loop/`**: este reporte y las salidas de
instrumento `SALIDA_V23_GATE0_BASE.txt`, `SALIDA_V23_ETIQUETAS_BASE.txt`,
`SALIDA_V23_OPS07_SIMULACION.txt`, `SALIDA_V23_OPS07_DEPRECADOS.txt`,
`SALIDA_V23_OPS07_EJECUCION.txt`, `SALIDA_V23_GATE0_OPS07.txt`,
`SALIDA_V23_OPS07_VERIFICACION.txt`, `SALIDA_V23_OPS07_CAUSA.txt`,
`SALIDA_V23_GATE0_TRAS_RESTAURAR.txt`, `SALIDA_V23_SUITE_MOTOR.txt`,
`SALIDA_V23_SUITE_WEB.txt`, `SALIDA_V23_TSC.txt`, `SALIDA_V23_SITIOS_FASE0.txt`,
`SALIDA_V23_MARCADOR.txt`.

---

## 3. TAREA 1: los dos registros, verificados hoy y NO duplicados

### 3.1. `docs/plan/08_VERIFICACION.md`

La seccion **QUE ES GATE 0 EN VERDE, y es EL CICLO ESCRITO DE DOS COMANDOS** esta en la
pagina, **linea 42**, con los dos comandos en su tabla (**lineas 52 y 53**), la aclaracion
de que la invocacion a secas sale con **exit 2** por diseño, la cita del comentario
fechado **2026-08-07** en `run_phase1.py` **lineas 941 a 958**, **QUIEN RECOMPILA,
REAPLICA** en la **linea 955**, y la linea base de **71 etiquetas** con su blob.

**No añadi ni una linea: el registro que la TAREA 1 pide ya esta puesto y lo verifique.**

### 3.2. `docs/plan/OPERACIONES.jsonl`

Las dos notas estan puestas, **aditivas**, y las lei enteras hoy:

| operacion | longitud de la nota hoy | lo que trae al final |
|---|---:|---|
| `OP-C-04` | **1.842 caracteres** | `REGISTRO DE LA ADJUDICACION (2026-08-14 ... vuelta 21, seccion 4, punto 4): LA SEDE DEL CASO POSITIVO DE ESTA OPERACION ES EL ARBOL DE TRABAJO TEMPORAL, NUNCA COMMITEADO ... Nada del texto anterior se borra: esta linea se añade.` |
| `OP-C-05` | **1.766 caracteres** | `REGISTRO DE LA ADJUDICACION (2026-08-14 ... vuelta 21, seccion 4, punto 5): SE QUEDA EN LA FASE 0, DIFERIDA POR SU depende_de ESCRITO (OP-S-12), sin bloquear nada y SIN CAMBIO DE FONDO ... Nada del texto anterior se borra: esta linea se añade.` |

**EL FICHERO, remedido hoy:** **71 operaciones, 71 ids unicos, CERO dependencias rotas**,
todas en estado `LISTA`. Reparto por fase: `00_CODIGO` 7, `01_FUENTES` 7, `02_DESTEJIDOS`
9, `03_FUSIONES` 16, `04_ENLACES` 10, `05_SANEO` 10, `06_MESAS` 5, `07_ADUANA` 2,
`08_VERIFICACION` 1, `09_LECTURAS_DIRIGIDAS` 3, `10_INVENTARIO` 1.

> **CORRECCION DE UN ERROR MIO, declarada:** mi primer barrido del fichero uso la clave
> `id` y **revento con `KeyError`**. La clave es **`id_op`**. Quedo corregido en la
> corrida siguiente y **no alcanzo ninguna cifra publicada**.

---

## 4. TAREA 2: la fase 0, operacion por operacion, medida hoy

### 4.0. LA LINEA BASE: GATE 0 VERDE POR EL CICLO ESCRITO

| # | comando | resultado de hoy |
|---:|---|---|
| **1** | `python scripts/run_phase1.py --reaplico-curaduria` | **EXITCODE 0** y **`GATE 0: OK`** |
| **2** | `python scripts/etiquetas_de_cara.py --aplicar` | **71 etiquetas**, blob `6007c1da864ef625796a47cab126a1d717610ffd`, **identico a HEAD** |

**EL CONTEO DE ETIQUETAS NO ENCOGIO.** El ciclo se corrio **tres veces** en esta vuelta
(linea base, tras `OP-S-07`, y tras restaurar) y **las tres dieron 71**, que es la cifra
de la vara registrada en `08_VERIFICACION.md`. Lo declaro porque la definicion registrada
obliga a declararlo, no porque haya pasado algo.

El validador tambien reporto, las tres veces: **1 componente conexo**, **3.835 nodos** en
el principal, **cobertura 100,0 por ciento**, **2 nodos sin enlaces entrantes**, **0
enlaces rotos**, y **13 pares de titulo con similitud igual o mayor que 95** como warning
informativo.

### 4.1. `OP-C-01`, `OP-C-02`, `OP-C-03` y `OP-S-06`: verificadas vivas en el codigo de hoy

**No las re ejecute: ya estan en `HEAD`. Verifique que siguen puestas, con el
instrumento.**

**LOS SITIOS DE LAS NOMINAS, medidos hoy** (`SALIDA_V23_SITIOS_FASE0.txt`):

| sitio | como resuelve hoy |
|---|---|
| `web/lib/engine/planRedactor.ts` | **2** apariciones de `resolverId` |
| `web/lib/compass.ts` | **3** apariciones de `resolverId` |
| `web/lib/engine/graph.ts` | **6** apariciones de `resolverId` |
| `web/app/api/organizer/route.ts` | `cargarEntrySeeds(graph)` **si** |
| `web/app/api/organizer/stream/route.ts` | `cargarEntrySeeds(graph)` **si** |
| `web/app/api/session/start/route.ts` | `cargarEntrySeeds(graph)` **si** |
| `web/app/api/project/[id]/world/[pack]/start/route.ts` | **2** apariciones de `resolverId` |

**Y AQUI ESTUVE A PUNTO DE PUBLICAR UN FALSO ROJO.** `web/lib/engine/recorrido.ts` y
`web/app/api/session/[id]/plan/route.ts` dan **CERO** apariciones de `resolverId`. **No es
un hueco: la resolucion es INDIRECTA**, por los tres ayudantes que la vuelta 22 extrajo a
`graph.ts` (su discutible 5). Lo segui hasta el fondo antes de decir nada:

- `graph.ts:194` `conceptosDeRuta`, `graph.ts:206` `faseDeNodo`, `graph.ts:279`
  `preguntaDeNodo`.
- `faseDeNodo` y `preguntaDeNodo` llevan **`resolverId(nid, graph) ?? nid` en su primera
  linea de cuerpo**, leido del archivo.
- **Quien los llama, medido:** `recorrido.ts:271` y `recorrido.ts:649` llaman
  `preguntaDeNodo`; `plan/route.ts:265` llama `conceptosDeRuta` y `plan/route.ts:403`
  llama `faseDeNodo`.

> **DISCREPANCIA DECLARADA CONTRA EL REPORTE DE LA VUELTA 22.** Ese reporte publica los
> sitios de `OP-C-02` como **la linea 267 y la 405** de la ruta del plan. **Medido hoy con
> `grep -n`: son la 265 y la 403.** Es un desfase de dos lineas. **No corrijo el texto
> viejo y no lo borro: pongo mi medicion al lado con su corte.** Es una cifra que vive
> solo en `REPORTE.md` y no mueve ningun dato. **Y no afirmo la causa del desfase:** una
> extraccion a ayudantes mueve lineas, pero **no corri el instrumento sobre ese estado
> intermedio**, asi que darlo por causa seria adivinar.

**EL FICHERO DE CASOS POSITIVOS de la fase 0 existe:**
`web/lib/engine/accesosResueltos.test.ts`, 15.956 bytes, **27 lineas `it(`**.

**LAS SUITES, corridas hoy enteras:**

| suite | comando | resultado |
|---|---|---|
| motor | `python engine/run_all_tests.py` | **exit 0**, `TODOS LOS TESTS PASARON (24/24)` |
| web | `npx vitest run` | **exit 0**, **80 ficheros**, **1.030 pasadas, 3 saltadas** (1.033) |
| tipos | `npx tsc --noEmit` | **exit 0**, **cero lineas de salida** |

### 4.2. `OP-S-07`: LA PARADA, reproducida ejecutandola

**LA SIMULACION PREVIA (P.7), sobre copia en memoria y cero escrituras.** Reimplemente el
resolutor del motor desde `web/lib/engine/graph.ts` (`mapaDeAlias` **lineas 109 a 129**,
`resolverId` **lineas 140 a 161**, medidas hoy con `grep -n` y `awk` sobre el archivo) y
barri **el catalogo entero**:

| | escrito en `OP-S-07` | **medido hoy** | coincide |
|---|---|---|---|
| enlaces que resuelven al propio nodo, en vivos | 33 | **33** | si |
| nodos | 27 | **27** | si |
| directas (`dest == nid` literal) | 0 | **0** | si |
| via alias | 33 | **33** | si |
| el peor, `costo_de_mala_calidad_copq` | 7 (2 previos, 5 siguientes) | **7 (2 previos, 5 siguientes)** | si |
| la nomina de 27 ids | escrita en el plan | **identica, id por id** | **exacta** |

**EL EJEMPLAR ESCRITO TAMBIEN CALZA, medido:** `analisis_flujo_de_valor` lleva
`value_stream_analysis_lean` en sus `nodos_previos`; ese nodo **existe, esta deprecado, y
resuelve a `analisis_flujo_de_valor`**.

**Y una cosa que la simulacion probo antes de tocar nada:** de las **33**, **las 33
tienen su vista reciproca escrita en el gemelo deprecado**. Cero excepciones.

**LA EJECUCION, tal como `eliminar` esta escrita**, sobre `dataset/nodos` y **solo en el
arbol de trabajo**:

- **33 enlaces retirados** en **27 ficheros**, comprobado despues **contra `HEAD`, campo
  por campo**: `ENLACES RETIRADOS (contra HEAD): 33`.
- **`CAMPOS DISTINTOS DE previos/siguientes QUE SE MOVIERON: 0`**, o sea la letra *"no se
  toca ningun otro campo"* cumplida y medida.
- **`ids_alias` intactos en los 27**, que es lo que `preservar` manda.
- Conteo de enlaces del grafo: **de 16.866 a 16.833**, baja de **33 exacta**.

**Y DESPUES CORRI EL GATE 0, Y LOS 33 VOLVIERON.**

| linea de `verificacion` de `OP-S-07` | resultado de hoy |
|---|---|
| `ningun nodo vivo se cita a si mismo ... NI tras resolver alias` | **ROJO: 33 enlaces en 27 nodos** |
| `el conteo de aristas del grafo baja en 33 exactamente` | **ROJO: vuelve a 16.866, variacion neta CERO** |

El ciclo en si salio **verde** (exit 0, `GATE 0: OK`, 71 etiquetas): **el que sale en rojo
es el texto de la operacion, no el instrumento.**

### 4.3. LA CAUSA, medida contra el log del propio validador

`dataset/metadata/phase1_run_log.json` trae el campo **`symmetrize_added` con exactamente
33 entradas**, cada una con su nodo y su campo. Y la comparacion que lo cierra:

- **`COINCIDEN EXACTAMENTE CON symmetrize_added: True`**. Conjunto contra conjunto:
  **`SOLO EN symmetrize_added: []`**, **`SOLO EN las auto aristas: []`**.
- **De las 33, las 33 son la vista reciproca de un enlace que el GEMELO DEPRECADO tiene
  hacia su propio superviviente.** Medido: **33 de 33**.

El **paso 5 de `scripts/run_phase1.py`** (simetrizar, leido hoy en las lineas 396 a 435)
recorre `succ_needed` y `pred_needed` y **fabrica** la reciproca que falte. Su unica
defensa contra la auto arista es **`dedupe_and_remove_self`**, que compara **literalmente**
y por eso no ve ni una de las 33: **ninguna es directa.**

> **La auto arista no esta escrita a mano en el nodo vivo. Es la sombra que el paso 5
> proyecta desde el nodo deprecado. Retirar la sombra sin tocar lo que la proyecta es
> trabajo que se deshace solo en la siguiente corrida, siempre.**

### 4.4. Por que esto es PARADA y no una decision mia

`OP-S-07` escribe **dos cosas que hoy no pueden ser verdad a la vez**, y lo demuestra el
instrumento, no un argumento:

- **(a)** `eliminar`: *"de cada uno de los 27, el enlace ... 33 enlaces en total. **No se
  toca ningun otro campo**"*. **Ejecutado hoy al pie de la letra y verificado.**
- **(b)** `verificacion`: *"ningun nodo vivo se cita a si mismo ... NI tras resolver
  alias"* mas *"el conteo de aristas del grafo baja en **33 exactamente**"*.

**(a) ejecutado al pie de la letra NO produce (b).** Las salidas que si producirian (b)
reescriben la letra de (a) o tocan lo que ninguna operacion ordena:

| camino | que rompe | cifra medida hoy |
|---|---|---|
| retirar tambien el enlace del gemelo deprecado | rompe *"no se toca ningun otro campo"* | son **81 enlaces mas en 59 nodos deprecados**, bajo el criterio B de la seccion 5 |
| enseñar al paso 5 a no fabricar una reciproca que resuelve al propio nodo | toca `run_phase1.py` sin que ninguna operacion lo ordene: `OP-C-04` ordena **añadir una guarda a Gate 0**, no cambiar el simetrizador | no medida, seria codigo nuevo |
| diferir `OP-S-07` | contradice su `bloquea_a` escrito (`['OP-C-04']`) y deja la fase 0 sin cerrar | |

**Es la especie exacta que el encargo nombra: "cualquier operacion cuyo texto no alcance
para ejecutarse sin decidir, te detiene a ti y convoca al auditor".** No elegi ninguno de
los tres caminos.

### 4.5. Que hice al parar

**Pare `OP-S-07`, no parti la fase.** Restaure con `git checkout -- dataset/
web/lib/assets/` y lo verifique por dos varas: **`git diff --name-only HEAD` sobre
`dataset/` y `web/lib/assets/` da CERO ficheros**, y el blob de `master_graph.json` es
**`6007c1da864ef625796a47cab126a1d717610ffd`, el de HEAD**. Despues volvi a correr el
ciclo entero sobre el arbol restaurado: **EXITCODE 0, `GATE 0: OK`, 71 etiquetas, blob
identico a HEAD**. **Nada de `OP-S-07` quedo commiteado; sus salidas si quedan, como
prueba.**

### 4.6. `OP-C-04` y `OP-C-05`: los dos campos, leidos del plan hoy

| operacion | orden | `depende_de` medido hoy | `bloquea_a` medido hoy | estado en esta vuelta |
|---|---:|---|---|---|
| `OP-C-04` | 6 | **`['OP-S-06', 'OP-S-07']`** | `['OP-S-01', 'OP-S-09', 'OP-F-01']` | **BLOQUEADA**: `OP-S-07` no esta hecha |
| `OP-C-05` | 7 | **`['OP-S-12']`** | **`[]`** | **DIFERIDA**, como el encargo manda |

**`OP-C-04` no se toco, y por eso su caso positivo de arbol temporal (el registro de la
TAREA 1) no se corrio en esta vuelta.** El registro esta puesto y la ejecucion espera a
que la operacion se desbloquee. Lo digo en vez de dejar el hueco callado.

---

## 5. MATERIAL NUEVO: las 81 del lado deprecado solo existen bajo un criterio que nadie ha escrito

El reporte de la vuelta 22, seccion 4.6, publica **81 aristas de la misma especie en 59
nodos deprecados**. **Fui a remedirlo y con el criterio que `OP-S-07` tiene escrito me dio
CERO.** En vez de copiar la cifra o desmentirla, medi **los dos criterios posibles**
(`SALIDA_V23_OPS07_DEPRECADOS.txt`):

| criterio | definicion | en DEPRECADOS | en VIVOS (control) |
|---|---|---:|---:|
| **A**, el que `OP-S-07` escribe | el enlace **resuelve al PROPIO id** del nodo | **0 enlaces, 0 nodos** | **33 enlaces, 27 nodos** |
| **B**, el que hace falta para que la cifra exista | el enlace **resuelve al MISMO destino** al que resuelve el propio nodo | **81 enlaces, 59 nodos** | **33 enlaces, 27 nodos** |

**LO QUE ESTO SIGNIFICA, y es la parte que importa:**

1. **El criterio A da CERO en deprecados POR CONSTRUCCION, no por limpieza.** El resolutor
   lleva siempre al superviviente vivo, nunca de vuelta al deprecado: un nodo deprecado no
   puede resolver a si mismo. **Contar deprecados con el criterio A no mide nada.**
2. **El criterio B coincide con el A exactamente donde el A esta definido:** sobre nodos
   vivos, `resolver(nid) == nid`, y B devuelve **33 y 27**, las mismas cifras que la
   verificacion escrita. **B es la generalizacion honesta, no un criterio rival.**
3. **La cifra de 81 en 59 nodos de la vuelta 22 SE REPRODUCE, pero solo bajo B.** No hay
   discrepancia de medicion: **hay un criterio que nadie escribio.**

**Los ejemplares, medidos:** `categorias_costos_calidad` con 4,
`comunicacion_coordinacion_multiempleador` con 3, `costo_de_mala_calidad_3` con 3,
`costo_de_mala_calidad_copq_3` con 3, `costos_ocultos_calidad` con 3. Y el par
`6s_lugar_trabajo` con `6s_workplace_organization`, que se citan mutuamente y **ambos
resuelven a `metodologia_6s`**.

> **NO TOQUE NI UNA DE LAS 81 Y NO PROPONGO QUE SE TOQUEN. Las declaro con su criterio
> delante**, porque `OP-C-04` va a escribir una guarda de auto arista y **la guarda tiene
> que decir con cual de los dos criterios mide**. Con A, la guarda pasa verde sobre 81
> aristas de esta especie. Va como PENDIENTE DE DOCTRINA en la seccion 8.

---

## 6. LAS CIFRAS DE ESTADO, recomputadas HOY (`SALIDA_V23_MARCADOR.txt`)

**Ninguna sale de un acta ni de un reporte anterior.**

**EL MARCADOR** (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`), corte 14 ago 2026:
**n 3.388**, **A 583 (17,2 por ciento)**, **B 89 (2,6)**, **C 7 (0,2)**, **D 2.709
(80,0)**. Puestos **de 1 a 3.388**, **cero huecos**, **cero duplicados**, **cero clases
fuera de ABCD**.

> **CONTRASTE DECLARADO:** el acta de la vuelta 21 y el reporte de la vuelta 22 publican
> estas mismas cifras. Mi medicion de hoy **no las copia, las reproduce**. **Cero
> discrepancia.**

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

> **LA BANDA QUE TODA TASA DE A TIENE QUE LLEVAR AL LADO**, citada con **su corte propio,
> que es anterior al mio** (`08_VERIFICACION.md`, corte 12 ago 2026, archivo al puesto
> 2.117, autoria del control de la muestra D): el error de dejar pasar es **4,2 por
> ciento**, banda de **0,7 a 20,2**. **No la remedi en esta vuelta y por eso no la
> presento como cifra de hoy.**

**EL GRAFO**, recomputado hoy: **3.835 nodos**, **3.521 vivos**, **314 deprecados**,
**16.866 enlaces** (previos mas siguientes), **15 claves distintas** en el catalogo:
`condiciones_activacion`, `deprecado`, `dominio`, `entregable_esperado`, `etiqueta_arbol`,
`fase_proyecto`, `fuente`, `ids_alias`, `merged_originals`, `node_id`, `nodos_previos`,
`nodos_siguientes`, `pasos_accionables`, `resumen_teorico`, `titulo_concepto`.

**LAS OPERACIONES: 71, 71 ids unicos, cero dependencias rotas, las 71 en `LISTA`.**

**VARA POR TRAMO, FIGURAS Y FAMILIAS: no aplican, y lo digo en vez de rellenarlo.** Esta
vuelta **no leyo un solo par**: el cribado sigue cerrado en 3.388 y ningun veredicto se
abrio. La unidad de trabajo fue la operacion, no el puesto.

---

## 7. CORRECCIONES DECLARADAS

**NINGUNA CORRECCION DE UNA CIFRA PUBLICADA.** Todo lo que remedi contra el plan o contra
el reporte de la vuelta 22 salio identico: las 33 auto aristas, los 27 nodos, el 0 de
directas, el 33 de via alias, el peor con 7, la nomina id por id, el ejemplar, las 33
entradas de `symmetrize_added`, el marcador entero, el grafo entero, las 71 operaciones y
las 71 etiquetas.

**LAS DOS COSAS QUE SI PONGO AL LADO DEL TEXTO VIEJO, sin borrarlo:**

1. **Las lineas de los sitios de `OP-C-02`:** la vuelta 22 publica **267 y 405**; medido
   hoy son **265 y 403**. Cifra de `REPORTE.md`, no mueve datos.
2. **Las 81 del lado deprecado** solo existen bajo el criterio B (seccion 5). La vuelta 22
   las publico sin nombrar criterio. **No es un error de medicion suyo: es un criterio sin
   escribir.**

**ERRORES PROPIOS DE ESTA VUELTA, con nombre:**

1. **Barri `OPERACIONES.jsonl` con la clave `id`, que no existe;** la clave es **`id_op`**.
   Revento con `KeyError` y quedo corregido en la corrida siguiente. **No alcanzo una
   cifra publicada.**
2. **Mi primer lector del grafo busco la clave `nodes` y el fichero la llama `nodos`.**
   Revento con `AttributeError` tras imprimir **`NODOS: 6`**, que era el numero de claves
   de la raiz. **Es exactamente la especie de falso positivo que la regla del instrumento
   persigue:** un `6` que parecia un conteo de nodos. **No se publico**, quedo cazado y la
   corrida buena dio 3.835.
3. **Mi verificacion de "ningun otro campo se movio" comparaba el fichero del nodo contra
   `master_graph.json` y marco `etiqueta_arbol` en `decision_pivotar_o_proceder`.** **El
   equivocado era mi chequeo, no el dato:** la curaduria de cara **no vive en los nodos**,
   vive en `dataset/metadata/etiquetas_de_cara_v1*.json` y se aplica sobre el grafo
   compilado, tal como el propio registro de Gate 0 deja escrito. Rehice la comprobacion
   **contra `git show HEAD:<fichero>`**, que es la vara correcta, y dio **0 campos
   movidos**.
4. **Estuve a punto de publicar `resolverId: 0` en `recorrido.ts` y en `plan/route.ts`
   como un hueco.** No lo es: la resolucion es indirecta por los tres ayudantes de
   `graph.ts`. Lo segui hasta el cuerpo de las funciones antes de escribir nada
   (seccion 4.1).

---

## 8. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Ocho. Van en el orden en que los decidi.**

1. **Trate el encargo repetido como "volver a medirlo todo" en vez de parar en seco sin
   entregar nada.** Razon: la regla 1 dice que nada de una vuelta anterior es fuente, y la
   regla 4 dice que se para **solo** si algo contradice una regla vigente o una cifra
   publicada. **Un encargo repetido no contradice nada**, y ejecutarlo de nuevo es
   justamente lo que la regla 1 pide. **Lo declaro arriba del todo para que nadie lea esta
   vuelta como trabajo nuevo.**
2. **Re ejecute `OP-S-07` sabiendo que la vuelta 22 ya habia documentado la parada.**
   Se puede leer como gasto repetido. Razon: **una parada heredada no es una parada
   medida**, y la regla 1 me prohibe citar la de la vuelta 22 como fuente. **Y valio la
   pena: al remedir aparecio lo de las 81** (seccion 5), que sin ejecutar no sale.
3. **Puse la ejecucion de `OP-S-07` sobre `dataset/nodos` (los 3.835 ficheros) y no sobre
   `master_graph.json`.** Razon: el grafo compilado es artefacto, y el propio ciclo de
   Gate 0 lo reconstruye desde los nodos; retirar enlaces del artefacto habria sido una
   limpieza que la primera recompilacion deshace sin que quede rastro de por que.
4. **Cuando mi chequeo de campos choco con `etiqueta_arbol`, decidi que el equivocado era
   mi chequeo y no el dato.** Es la clase de decision que un ejecutor puede tomar para
   taparse. **La declaro con su prueba:** el registro de Gate 0 dice que las etiquetas no
   viven en los nodos, y rehice la comprobacion contra `git show HEAD:`, que es una vara
   independiente de mi criterio.
5. **Nombre los dos criterios A y B para el lado deprecado, y esos nombres son mios: no
   estan en el plan.** Podia haber escrito solo "el criterio de la operacion da 0" y
   dejarlo ahi. Preferi medir los dos y **poner el control sobre vivos** (B da 33 y 27,
   igual que la verificacion escrita), porque sin ese control mi criterio B seria una
   invencion mia sin ancla.
6. **NO escribi `docs/loop/PARA_ALEXIS.md`, aunque el bucle esta detenido de hecho.**
   Razon: `AUDITOR.md` seccion 4 pone esa pluma **en el auditor**, y `EJECUTOR.md` regla 4
   me dice que la parada la escribo **en el reporte**. **Que el auditor haya muerto no me
   traspasa su autoridad.** Va como pregunta 1.
7. **No movi ninguna operacion de `LISTA`**, igual que la vuelta 22, aunque cuatro ya
   corrieron y estan en `HEAD`. Ninguna instruccion me manda moverlas.
8. **Conte los casos positivos de la fase 0 como "27 lineas `it(`" y no como "27
   pruebas".** Es un `grep`, no una corrida: la cifra que **si** es corrida son las 1.030
   pasadas de la suite web. Lo separo en vez de presentar el `grep` como resultado de
   prueba.

---

## 9. PENDIENTES DE DOCTRINA Y PREGUNTAS

**PENDIENTES DE DOCTRINA (dos).**

1. **Que hace una operacion de saneo cuando el propio Gate 0 REPONE lo que ella retira.**
   Ninguna regla escrita lo cubre. `P.16` ("quien fabrica, limpia") gobierna las fusiones
   **que vienen** y dice expresamente que las 33 de hoy **siguen siendo trabajo de
   `OP-S-07`**. La nota de `OP-S-07` anticipo que la guarda debe **resolver y no
   comparar**, pero **no anticipo el simetrizador**. Registro el pendiente y **no invento
   la regla**. *(Ya levantado por la vuelta 22; lo mantengo abierto porque sigue sin acta
   que lo adjudique.)*
2. **NUEVO, y sale de la medicion de hoy: con que criterio mide la guarda de auto arista
   de `OP-C-04` sobre un nodo DEPRECADO.** `OP-S-07` escribe el criterio A ("resuelve al
   propio id"), que sobre deprecados da **0 por construccion**. El criterio B ("resuelve al
   mismo destino que el propio nodo") da **81 en 59 nodos** y coincide con A sobre vivos
   (33 y 27). **Una guarda que use A pasara verde sobre 81 aristas de esta especie, y eso
   es precisamente lo que la nota de `OP-S-07` llama "una guarda que no guarda".** No
   escribo la regla: la traigo.

**PREGUNTAS (cinco).**

1. **El bucle esta detenido de hecho y nadie lo ha declarado.** El auditor de la vuelta 22
   murio con error de API, no hay acta 22 y `PROMPT_SIGUIENTE.md` sigue siendo el encargo
   de la 22. **¿Se relanza al auditor sobre el reporte de la vuelta 22, se relanza sobre
   este, o se escribe `PARA_ALEXIS.md`?** Yo no toque esa pluma (discutible 6).
2. **Las 81 del lado deprecado:** ¿entran en `OP-S-07` cuando se adjudique su salida, o
   son operacion aparte? Y sobre todo: **¿bajo que criterio?** (pendiente de doctrina 2).
3. **El plan no tiene estado para "ejecutada".** Las 71 siguen en `LISTA` y cuatro ya
   corrieron. ¿Se añade un estado, se marca por commit, o se deja asi hasta el cierre de
   fase? *(Sin respuesta desde la vuelta 22.)*
4. **`git status` marca `dataset/metadata/master_graph.json` como modificado mientras
   `git diff --quiet` sale con exit 0 y el hash de blob es el de HEAD.** Vuelve a pasar
   hoy. Es artefacto de CRLF y del cache de `stat`, no contenido. **¿Se deja escrito que la
   vara buena es el hash de blob**, para que nadie lea un falso movimiento del grafo en una
   vuelta futura? *(Sin respuesta desde la vuelta 22.)*
5. **`SALIDA_V23_OPS07_VERIFICACION.txt` queda commiteado con su resultado en ROJO**,
   porque es la prueba de la parada. ¿Se conserva asi o se marca en el nombre? *(Sin
   respuesta desde la vuelta 22.)*

---

## 10. ESTADO EN QUE DEJO LA RAMA

- **Rama `pasada-unica`.** HEAD al empezar: **`f151051c`**, ya en `origin`. Esta vuelta
  añade **un commit**: este reporte mas las salidas de instrumento.
- **`dataset/` IDENTICO a HEAD**, verificado por dos varas: **cero ficheros con diferencia
  real** y blob **`6007c1da864ef625796a47cab126a1d717610ffd`**.
- **CERO cambios en `web/`, `scripts/` y `docs/plan/` en esta vuelta.**
- **GATE 0 VERDE POR EL CICLO ESCRITO**, corrido **tres veces** hoy, la ultima sobre el
  arbol restaurado: **EXITCODE 0, `GATE 0: OK`, 71 etiquetas las tres veces, sin
  encoger**, blob identico a HEAD.
- **SUITES EN VERDE:** motor **24/24**, web **80 ficheros, 1.030 pasadas y 3 saltadas**,
  `tsc --noEmit` **limpio**.
- **FASE 0: cuatro de siete hechas y verificadas hoy** (`OP-C-01`, `OP-C-02`, `OP-C-03`,
  `OP-S-06`), **`OP-S-07` PARADA y reproducida**, **`OP-C-04` BLOQUEADA por su
  `depende_de`**, **`OP-C-05` DIFERIDA por el suyo**. **La fase 0 no esta cerrada** y
  ninguna operacion de las fases 01 a 07 se toco.
