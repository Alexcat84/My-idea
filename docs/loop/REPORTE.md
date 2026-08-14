# REPORTE de la vuelta 24 del ejecutor (Opus 5). FASE III, EJECUCION, rama `pasada-unica`

**Fecha de corte de TODO lo que va aqui: 14 ago 2026.** Cada cifra y cada nombre propio
salio de un instrumento corrido EN ESTA VUELTA. Donde cito un acta o un reporte anterior
lo digo y lo pongo como CONTRASTE, nunca como fuente (regla 1 de `EJECUTOR.md`).

---

## 0. EL TITULAR

**LA FASE 0 ESTA CERRADA.** `OP-S-07` se ejecuto por su letra nueva y `OP-C-04` se
desbloqueo y se ejecuto detras. Las dos con Gate 0 verde por el ciclo escrito y las tres
suites en verde.

| operacion | estado al cerrar esta vuelta |
|---|---|
| `OP-C-01`, `OP-C-02`, `OP-C-03`, `OP-S-06` | ya estaban en `HEAD` (vueltas anteriores) |
| **`OP-S-07`** | **EJECUTADA**: 66 enlaces retirados en 59 ficheros, commit `82ee608a` |
| **`OP-C-04`** | **EJECUTADA**: las dos guardas en Gate 0, commit `96c14726` |
| `OP-C-05` | **DIFERIDA** por su `depende_de` (`['OP-S-12']`), como el encargo manda |

**LA PRUEBA DE QUE EL CAMINO A ERA EL BUENO, y es una cifra, no un argumento:**
`dataset/metadata/phase1_run_log.json` traia **33 entradas** en `symmetrize_added` cuando
la vuelta 23 retiro solo las 33 vivas, y **hoy trae CERO**. El paso 5 del validador ya no
tiene nada que refabricar porque lo que proyectaba la sombra se retiro con ella.

**Y EL MODO CONTINUO SE DETIENE EN LA FASE 01.** Segui a `01_FUENTES` como el encargo
manda. **`OP-F-01` verifica en verde hoy** (seccion 6). **`OP-F-02` y `OP-F-04-HOR` NO
alcanzan para ejecutarse sin decidir**, y ademas **chocan entre si sobre un nodo**. Es la
condicion de parada que el propio encargo nombra. **No elegi ninguna salida.** Seccion 7.

---

## 1. HASH, RUTAS Y ESTADO DE PARTIDA

**HEAD al empezar: `ba109e5ea483f32df1b1763a2930ef204343f347` (`ba109e5e`)**, rama
`pasada-unica`, arbol **limpio** y **ya empujado** (`git log origin/pasada-unica..HEAD`
salio vacio). **No habia nada pendiente que commitear antes de tocar nada** (regla 2).

**HEAD al cerrar: `96c14726`**, empujado a `origin/pasada-unica`, mas el commit de este
reporte.

**LOS DOS COMMITS DE TRABAJO DE ESTA VUELTA:**

| commit | que trae |
|---|---|
| `82ee608a` | `OP-S-07` ejecutada, mas la TAREA 1 en `docs/plan/08_VERIFICACION.md` |
| `96c14726` | `OP-C-04` ejecutada, con su caso positivo corrido en los dos sentidos |

**RUTAS TOCADAS**, y ninguna otra:

| ruta | que se toco |
|---|---|
| `dataset/nodos/` | **59 ficheros**, solo `nodos_previos` y `nodos_siguientes`, solo `OP-S-07` |
| `dataset/metadata/master_graph.json` | recompilado por el ciclo de Gate 0 |
| `web/lib/assets/` | `master_graph.json` y `manifest.json`, por `sync_assets_web.py` |
| `scripts/run_phase1.py` | las dos guardas de `OP-C-04`, dentro de `step7_validate` |
| `docs/plan/08_VERIFICACION.md` | el registro de la TAREA 1 |
| `scripts/loop/` | dos instrumentos nuevos de esta vuelta |
| `docs/loop/` | este reporte y las salidas de instrumento |

**CERO cambios en `docs/plan/OPERACIONES.jsonl`**: la TAREA 1 punto 2 pedia LEER las notas
corregidas, no escribirlas, y no escribi nada ahi.

---

## 2. TAREA 1: los dos registros

### 2.1. El registro nuevo en `docs/plan/08_VERIFICACION.md`

Añadida, **a continuacion de la tabla de los dos comandos** del GATE 0 EN VERDE, la
subseccion **`REGISTRO: git status NO ES LA VARA DE ESTE FICHERO`**, con lo que el encargo
dicta: en Windows tocar `master_graph.json` reemplaza LF por CRLF y `git status` lo marca
como modificado sin que haya cambiado un dato; **eso no es la vara**; la vara es **el hash
de blob byte identico a HEAD**, que es el comando 2 del ciclo; y quien lea un movimiento en
`git status` sobre ese fichero sin diferencia de contenido real **no esta viendo una
regresion**. Añadi ademas la comprobacion barata que lo separa (`git diff --quiet` en exit
0 y `git hash-object` contra `git rev-parse HEAD:...`).

> **Y EL REGISTRO SE VERIFICO SOLO EN ESTA MISMA VUELTA.** Al commitear `OP-C-04`,
> `git status` listaba `dataset/metadata/master_graph.json` como modificado mientras
> `git diff --name-only HEAD -- dataset/` daba **CERO ficheros** y el blob del disco era
> `8d47ff32`, el mismo de HEAD. **El artefacto que el registro describe se reprodujo en el
> mismo dia en que se registro.**

### 2.2. Las notas corregidas, leidas antes de ejecutar

Lei enteras las notas de `OP-S-07` y `OP-C-04` en `docs/plan/OPERACIONES.jsonl` (lineas
**17** y **23**), con sus correcciones declaradas del 14 ago 2026. **No escribi nada ahi**,
que es lo que el encargo pide. Lo que gobernó mi ejecucion, citado de la letra vigente:

- `OP-S-07` `eliminar`: **66 enlaces** (33 vivos mas 33 reciprocas literales del gemelo
  deprecado), en **59 ficheros**; las **48 alias contra alias NO se tocan**.
- `OP-S-07` `verificacion`: **baja en 66 exactamente**, **Gate 0 verde por el ciclo
  escrito**, **cero auto aristas tras resolver sobre vivos**.
- `OP-C-04`: la guarda **mide sobre vivos**, los deprecados **fuera** con motivo escrito;
  `merged_originals` **dentro** de la lista blanca; el caso positivo **en arbol de trabajo
  temporal, nunca commiteado**.

---

## 3. LA LINEA BASE, medida antes de tocar nada

| # | comando | resultado de hoy |
|---:|---|---|
| **1** | `python scripts/run_phase1.py --reaplico-curaduria` | **EXITCODE 0**, `GATE 0: OK` |
| **2** | `python scripts/etiquetas_de_cara.py --aplicar` | **71 etiquetas**, blob `6007c1da864ef625796a47cab126a1d717610ffd`, **identico a HEAD** |

**EL CONTEO DE ETIQUETAS NO ENCOGIO EN NINGUNA DE LAS CINCO CORRIDAS DEL CICLO** de esta
vuelta: **71, 71, 71, 71, 71**. La definicion registrada obliga a declararlo, y lo declaro
aunque no haya pasado nada.

> **DISCREPANCIA DECLARADA, y no la resuelvo copiando** (regla 1). `08_VERIFICACION.md`
> registra su linea base con el blob **`bb423c066f5a961f082b3b70aaff4f98d35d7a1d`**. El
> blob de HEAD al empezar hoy era **`6007c1da...`** y al cerrar es **`8d47ff32...`**. **No
> es una regresion: la vara escrita es *byte identico a HEAD*, no *igual a un blob
> concreto*, y esa vara se cumplio en las cinco corridas.** El blob del registro es de un
> HEAD anterior y **queda desfasado cada vez que una operacion toca el grafo, que es justo
> lo que la fase III hace**. Lo traigo como pregunta 1 en vez de reescribirlo yo.

El validador reporto, las cinco veces: **1 componente conexo**, **3.835 nodos** en el
principal, **cobertura 100,0 por ciento**, **2 nodos sin enlaces entrantes**, **0 enlaces
rotos**, y **13 pares de titulo con similitud igual o mayor que 95** como warning
informativo.

---

## 4. `OP-S-07`, ejecutada por su letra nueva

### 4.1. La simulacion previa (P.7), copia en memoria y cero escrituras

Reimplemente el resolutor del motor (`mapaDeAlias` y `resolverId` de
`web/lib/engine/graph.ts`) en `scripts/loop/vuelta24_ops07.py` y barri el catalogo entero.

| | escrito en la letra nueva | **medido hoy** | coincide |
|---|---|---|---|
| enlaces de nodo VIVO que resuelven al propio nodo | 33 | **33** | si |
| nodos vivos | 27 | **27** | si |
| directas (`dest == nid` literal) | 0 | **0** | si |
| via alias | 33 | **33** | si |
| reciprocas literales en el gemelo deprecado | 33 | **33**, en **32** nodos | si |
| reciprocas que faltaban en el gemelo | 0 | **0** | si |
| **total a retirar** | **66** | **66** | si |
| **ficheros** | **59** | **59** | si |
| alias contra alias INERTES | 48, en 33 nodos | **48, en 33 nodos** | si |
| **la particion del lado deprecado** | **81 = 33 + 48**, sin solape | **81 = 33 + 48, solape 0** | **exacta** |
| el peor, `costo_de_mala_calidad_copq` | 7 (2 previos, 5 siguientes) | **7 (2 previos, 5 siguientes)** | si |

**EL EJEMPLAR ESCRITO CALZA:** `analisis_flujo_de_valor` lleva `value_stream_analysis_lean`
en sus `nodos_previos`; ese nodo **existe, esta deprecado y resuelve a
`analisis_flujo_de_valor`**.

**La simulacion sobre la copia dio la baja de 66 y CERO auto aristas de vivos**, con las 48
inertes intactas, **antes de escribir un solo byte**.

### 4.2. La ejecucion y su verificacion

**66 entradas retiradas en 59 ficheros de `dataset/nodos`.** Verificado despues **contra
`HEAD`, campo por campo**:

| linea de `verificacion` de `OP-S-07` | resultado de hoy |
|---|---|
| ningun nodo vivo se cita a si mismo, NI directamente NI tras resolver | **0 en 0 nodos, VERDE** |
| los 66 retirados y ningun otro; el conteo de aristas baja en 66 exactamente | **66 exactos, 16.866 a 16.800, VERDE** |
| no se toca ningun otro campo | **0 campos distintos de previos/siguientes se movieron, VERDE** |
| los `ids_alias` NO se tocan (`preservar`) | **0 movidos, VERDE** |
| las 48 alias contra alias quedan intactas | **48 en 33 nodos deprecados, sin tocar** |
| GATE 0 VERDE POR EL CICLO ESCRITO tras la retirada | **EXITCODE 0, `GATE 0: OK`, 71 etiquetas** |

### 4.3. Lo que esta vuelta prueba y la anterior no pudo

`symmetrize_added` en `dataset/metadata/phase1_run_log.json`: **CERO entradas**. La vuelta
23 documento **33** al retirar solo las vivas. **La sombra no vuelve porque se retiro lo
que la proyectaba.** Es la letra nueva funcionando, medida en el log del propio validador.

### 4.4. El punto fijo contra el HEAD nuevo

Tras commitear, volvi a correr el ciclo entero: **EXITCODE 0**, `GATE 0: OK`, **71
etiquetas**, y el blob del disco **`8d47ff32d4376f17a5880d7ba56060569856a04a`**, **identico
al de HEAD nuevo**, con **cero ficheros con diferencia real**. El ciclo es **punto fijo**
contra el HEAD que la operacion acaba de crear.

---

## 5. `OP-C-04`, ejecutada con su caso positivo en los dos sentidos

### 5.1. Las dos guardas

Escritas en `scripts/run_phase1.py`, dentro de `step7_validate`:

**1. AUTO ARISTA CON RESOLUCION.** Cada id de `nodos_previos` y `nodos_siguientes` pasa por
una copia fiel de `resolverId` y se compara con el id del propio nodo. **Mide sobre
vivos**; los deprecados quedan fuera con el motivo escrito en la correccion declarada.

**2. LISTA BLANCA DE CLAVES.** **No reescribi la lista.** Existe ya, escrita, en
`scripts/expansion/validar_esquema.py` (`CAMPOS_PERMITIDOS`, **15 campos**), y **lleva
dentro la adjudicacion argumentada de `merged_originals`**, que es exactamente lo que la
nota de `OP-C-04` cierra. La importo. **Dos listas blancas divergentes serian el mismo
defecto que el chequeo de los dos `master_graph` vino a curar.**

> **La lista blanca medida contra el catalogo de hoy: 15 claves permitidas, 15 claves
> presentes, cero renegadas.** Coinciden campo a campo.

### 5.2. El caso positivo, corrido en los dos sentidos

El estado malo se inyecto **solo en el arbol de trabajo** y se restauro acto seguido, tal
como la nota de la operacion lo adjudica. **Nada de esto quedo commiteado.**

- **La auto arista:** el enlace de `analisis_flujo_de_valor` a `value_stream_analysis_lean`,
  que es el ejemplar que la propia verificacion nombra.
- **La clave sucia:** `fase_проekto`, con **п, р y о CIRILICAS**, recuperada de su forma
  original en el commit `fa2e6011` con `git show`, **no retipeada a ojo**. Puntos de
  codigo medidos: `0x43f`, `0x440`, `0x43e`.

| momento | Gate 0 |
|---|---|
| **ANTES del arreglo**, con el estado malo puesto | **EXITCODE 0**, `GATE 0: OK`. **La prueba NO era vacia** |
| **DESPUES del arreglo**, con el mismo estado malo | **EXITCODE 1**, `GATE 0: FALLIDO` |
| **DESPUES del arreglo**, catalogo limpio | **EXITCODE 0**, las dos guardas en `[OK]` |

Y las dos guardas **nombran la falla exacta**, que es lo que `OP-C-05` exige de una guarda
y lo que hace auditable a esta:

```
[FALLO] Ningun nodo VIVO se cita a si mismo tras RESOLVER (auto-arista via alias)
        (valor: 1 auto-aristas: ['analisis_flujo_de_valor.nodos_previos -> value_stream_analysis_lean'])
[FALLO] Ninguna clave de nodo fuera de la lista blanca del esquema
        (valor: 1 renegadas: ['crosby_habilidad_transmision.fase_проekto'])
```

### 5.3. La medicion que demuestra la nota de `OP-S-07`

**Sobre el MISMO estado malo**, medido: la guarda **LITERAL** (`dest == nid`) da **0** y
**pasaria verde**; la guarda **que resuelve** da **1** y **cae**. **Es la nota de
`OP-S-07` demostrada con instrumento y no repetida de memoria:** una guarda literal no
guarda.

### 5.4. La restauracion, por dos varas

`git checkout -- dataset/ web/lib/assets/` tras cada inyeccion. Verificado con:
**cero ficheros con diferencia real** contra HEAD, y blob **`8d47ff32...`**, el de HEAD.

---

## 6. `OP-F-01`, la primera de la fase 01: verifica en verde hoy

Es una operacion **documental**: `eliminar`, `preservar` y `aristas_nuevas` estan **vacios**
y `superviviente` es `null`. Su ejecucion es medir y registrar, no tocar nodos.

| linea de `verificacion` | resultado de hoy |
|---|---|
| los SIETE tratados por la misma regla, sin excepciones caso por caso | **7 de 7 existen y estan vivos, cero deprecados, VERDE** |
| ningun nodo de la clase queda con pasos alterados | **7 de 7 con el conteo de pasos IDENTICO al publicado, VERDE** |
| la cifra de 18 reescrita con su corte alli donde este publicada | **YA ESTABA, en las dos sedes, VERDE** |
| Gate 0 verde | **VERDE** |

**LOS SIETE, medidos hoy contra lo publicado en `01_FUENTES.md`:**

| nodo | pasos hoy | publicado |
|---|---:|---:|
| `seleccion_representante_extranjero` | 9 | 9 |
| `internacionalizacion_sitio_web_exportacion` | 9 | 9 |
| `elaboracion_pro_forma_invoice` | 8 | 8 |
| `elementos_plan_exportacion_ejemplo` | 13 | 13 |
| `principios_medicion_efectiva` | 10 | 10 |
| `fmea_analisis_de_modos_de_falla` | 8 | 8 |
| `background_startup_vs_corporativo` | 9 | 9 |

**LA TERCERA LINEA, verificada en vez de rehecha.** `CORRECCIONES_A_APLICAR.md` señala la
sede como `docs/COSTURAS_INTERNAS_RESUMEN.md` secciones 6 y 7 punto 1, y la asigna a la
**SESION A**. **Fui a mirar antes de escribir nada: las dos sedes YA llevan la correccion
declarada con su corte**, aditiva y sin borrar el texto viejo (linea **369** para la
seccion 6, lineas **402 a 407** para la 7). **No añadi nada: no habia nada que añadir**, y
no toque un fichero que el plan asigna a otra sesion.

> **NO DECLARO `OP-F-01` HECHA, y digo por que.** Su segunda linea de verificacion es una
> condicion **de fin de fase**, no de hoy: **se pone en rojo el dia que `OP-F-04-HOR`
> corra**, y eso es la parada de la seccion 7. **Verde hoy no es lo mismo que hecha.**

---

## 7. LA PARADA: la fase 01 no alcanza para ejecutarse sin decidir

**Son dos paradas distintas y las dos estan medidas.** No elegi salida en ninguna.

### 7.1. `OP-F-02` no dice lo suficiente para ejecutarse

Su adjudicacion es **REUNIR**: el bloque de IA de tres nodos viaja entero al racimo de la
supervision de la IA. **Para ejecutarla hacen falta dos datos que no estan escritos en
ninguna sede:**

| lo que falta | como lo comprobe |
|---|---|
| **la frontera de paso** del bloque de Mollick en cada uno de los tres | `01_FUENTES.md` publica los tres con su fuente real y *lo pegado: Mollick*, **sin tramo de pasos**. La tanda de los 43 (que si publica fronteras) **excluye a Mollick por definicion**: es *"declaraciones en segunda posicion, SIN Hugos ni Mollick"* |
| **el nodo del racimo que RECIBE** el bloque | la operacion dice *"el racimo de supervision de la IA, que hoy tiene DIEZ miembros"*. **Diez destinos posibles y ninguno nombrado**; `aristas_nuevas` esta vacio y `superviviente` es `null` |

**Los tres, medidos hoy:** `future_scenarios_planning` 13 pasos,
`gut_check` 9 pasos, `brainstorming_divergente` 8 pasos, los tres con Mollick declarado en
segunda posicion en su campo `fuente`.

> **Cortar por donde yo crea que empieza el bloque, y elegir yo a cual de los diez va, son
> dos decisiones, no dos lecturas.** Y la primera es irreversible sobre el texto de un
> nodo. **Es la especie exacta que el encargo nombra.**

### 7.2. `OP-F-01` y `OP-F-04-HOR` chocan sobre el mismo nodo

**`background_startup_vs_corporativo` esta en el campo `nodos` de las DOS**, medido hoy
barriendo las 71 operaciones. Es el **unico** de los siete que aparece en otra operacion.

| | dice |
|---|---|
| **`OP-F-01`**, verificacion | *"ningun nodo de la clase queda con pasos alterados"* |
| **`OP-F-04-HOR`**, verificacion | *"cada bloque apendice separado con su frontera de paso escrita"*, *"el bloque separado va a su familia o a nodo propio: NO se poda"* |
| **`01_FUENTES.md`**, tabla de los 14 de Horowitz | la frontera de ese nodo es **pasos 1 a 4 / 5 a 9** |
| **`P.3`** del banco del plan | el bloque de Horowitz es **del MISMO tema**: **REPARTO OBLIGATORIO**, la poda **no es opcion** |

**Separar el bloque 5 a 9 deja el nodo en 4 pasos.** Sus pasos quedan alterados, y la
segunda verificacion de `OP-F-01` se pone en **rojo**. **Las dos operaciones estan en
`LISTA`, en la misma fase, y ninguna regla escrita dice cual manda.**

> **Y LA RAIZ ES MAS INCOMODA QUE UN CHOQUE DE ORDEN.** Lo que mete a ese nodo en la clase
> LARGO LEGITIMO es, en la letra de `01_FUENTES.md`, que *"sale de dos libros de
> fundadores"* y por eso *"rompe la exclusividad de los manuales"*. **Pero declarar un
> segundo libro es, por `P.2`, LA FIRMA DEL INJERTO.** O sea que **el mismo hecho** sostiene
> las dos lecturas: para `OP-F-01` sus 9 pasos son una lista legitima sin repeticion; para
> `OP-F-04-HOR` son **4 mas 5**, dos libros apilados. **No es que sobre una operacion: es
> que el nodo esta clasificado dos veces y las dos clasificaciones se excluyen.**
>
> **Eso no lo resuelve un ejecutor.** Lo dejo escrito con su medicion delante.

---

## 8. LAS CIFRAS DE ESTADO, recomputadas HOY

**Ninguna sale de un acta ni de un reporte anterior** (`SALIDA_V24_MARCADOR.txt`).

**EL MARCADOR** (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`), corte 14 ago 2026: **n 3.388**,
**A 583 (17,2 por ciento)**, **B 89 (2,6)**, **C 7 (0,2)**, **D 2.709 (80,0)**. Puestos
**1 a 3.388**, **cero huecos**, **cero duplicados**, **cero clases fuera de ABCD**.

> **CONTRASTE DECLARADO:** el reporte de la vuelta 23 publica estas mismas cifras. Mi
> medicion **no las copia, las reproduce**. **Cero discrepancia.**

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

> **LA BANDA QUE TODA TASA DE A LLEVA AL LADO (P.15)**, citada **con su corte propio, que es
> anterior al mio** y con su atribucion: `08_VERIFICACION.md`, corte **12 ago 2026**,
> archivo al puesto **2.117**, autoria del control de la muestra D. El error de dejar pasar
> es **4,2 por ciento**, banda de **0,7 a 20,2**. **No la remedi en esta vuelta y por eso no
> la presento como cifra de hoy.**

**EL GRAFO, recomputado hoy:** **3.835 nodos**, **3.521 vivos**, **314 deprecados**,
**16.800 enlaces** (previos mas siguientes), **15 claves distintas**.

> **LOS 16.800 SON LA UNICA CIFRA DE ESTADO QUE CAMBIO EN ESTA VUELTA**, y cambio por
> `OP-S-07`: **16.866 menos 66**. El resto reproduce exacto contra la vuelta 23.

**LAS OPERACIONES: 71, 71 ids unicos, cero dependencias rotas, las 71 en `LISTA`.** Reparto
por fase: `00_CODIGO` 7, `01_FUENTES` 7, `02_DESTEJIDOS` 9, `03_FUSIONES` 16, `04_ENLACES`
10, `05_SANEO` 10, `06_MESAS` 5, `07_ADUANA` 2, `08_VERIFICACION` 1,
`09_LECTURAS_DIRIGIDAS` 3, `10_INVENTARIO` 1.

**VARA POR TRAMO, FIGURAS Y FAMILIAS: no aplican, y lo digo en vez de rellenarlo.** Esta
vuelta **no leyo un solo par**: el cribado sigue cerrado en 3.388 y ningun veredicto se
abrio. La unidad de trabajo fue la operacion.

**LAS SUITES, corridas enteras dos veces (tras `OP-S-07` y tras `OP-C-04`):**

| suite | comando | resultado |
|---|---|---|
| motor | `python engine/run_all_tests.py` | **exit 0**, `TODOS LOS TESTS PASARON (24/24)` |
| web | `npx vitest run` | **exit 0**, **80 ficheros**, **1.030 pasadas, 3 saltadas** |
| tipos | `npx tsc --noEmit` | **exit 0**, cero lineas de salida |

---

## 9. CORRECCIONES DECLARADAS Y ERRORES PROPIOS

**NINGUNA CORRECCION DE UNA CIFRA PUBLICADA.** Todo lo que remedi contra la letra corregida
del plan salio identico: las 33 vivas, los 27 nodos, el 0 de directas, las 33 reciprocas,
los 66, los 59 ficheros, las 48 inertes, la particion 81 igual a 33 mas 48 sin solape, el
peor con 7, el ejemplar, y el marcador entero.

**LO QUE PONGO AL LADO DEL TEXTO VIEJO, sin borrarlo:**

1. **El blob de la linea base de `08_VERIFICACION.md`** (`bb423c06...`) es de un HEAD
   anterior y hoy no coincide con ninguno de los dos blobs de esta vuelta. **La vara
   escrita (*byte identico a HEAD*) si se cumplio siempre.** Pregunta 1.

**ERRORES PROPIOS DE ESTA VUELTA, con nombre:**

1. **Mi primer script de `OP-S-07` escribia un salto de linea al final de cada nodo**, y los
   ficheros del dataset **no lo llevan**. Lo cace **antes de ejecutar** comparando los
   bytes finales de un nodo real contra `save_node` del validador (`run_phase1.py:103`), y
   lo corregi. **De no haberlo cazado, habria ensuciado 59 ficheros con un cambio de
   formato que ninguna operacion ordena.**
2. **Mi script del caso positivo revento con `UnicodeEncodeError`** al imprimir la clave
   cirilica en la consola `cp1252` de Windows. Lo arregle imprimiendo los puntos de codigo
   escapados. **No alcanzo ninguna cifra**, y de hecho la salida quedo mejor: la clave se
   publica como `проekto` y no como algo que parece latino.
3. **Corri la suite del motor antes de sincronizar los assets de la web y salio en rojo**
   con 59 nodos divergentes. **No era una regresion: era el remedio escrito del propio
   validador sin correr.** Lo declaro entero en el discutible 2 en vez de presentar solo la
   corrida verde.

---

## 10. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Nueve. Van en el orden en que los decidi.**

1. **Ejecute `OP-S-07` sobre `dataset/nodos` y no sobre `master_graph.json`.** Razon: el
   grafo compilado es artefacto y el ciclo lo reconstruye desde los nodos; retirar enlaces
   del artefacto seria una limpieza que la primera recompilacion deshace sin dejar rastro.
   Es el mismo criterio que la vuelta 23 declaro, y lo repito por decision, no por inercia.
2. **Corri `python scripts/sync_assets_web.py`, que NO esta en el ciclo de dos comandos de
   `08_VERIFICACION.md`.** Es el discutible mas grande de la vuelta y lo pongo entero.
   **A favor:** es el remedio que el propio validador tiene escrito, con su orden y su
   motivo (`REMEDIO_SYNC` en `run_phase1.py`: *"primero se reaplica, despues se
   sincroniza"*), y sin correrlo `engine/test_gate_alias.py` cae con **59 nodos divergentes
   entre las dos copias del grafo**. **En contra:** el ciclo registrado dice **dos**
   comandos, y yo corri tres. **Lo que creo que esto destapa, y por eso va tambien como
   pregunta 2:** el chequeo de gemelos de Gate 0 compara el snapshot de **antes** del paso
   6, asi que **el dia en que una operacion cambia el grafo, Gate 0 no puede ver la
   divergencia que esa operacion acaba de crear**; la caza la suite, no el Gate. **No toque
   el registro del ciclo.**
3. **Importe la lista blanca de `scripts/expansion/validar_esquema.py` en vez de escribirla
   en Gate 0.** Podia haber escrito los 15 campos ahi mismo, que es mas explicito y no
   añade un import entre carpetas. Preferi la fuente unica: **dos listas blancas que puedan
   divergir son el defecto que el chequeo de los dos `master_graph` vino a curar**, y esa
   lista ya trae dentro la adjudicacion de `merged_originals` que `OP-C-04` confirma.
4. **La guarda de auto arista lleva una copia del resolutor en Python, y ya existe otra en
   `scripts/loop/vuelta24_ops07.py` y la original en TypeScript.** Son **tres**
   implementaciones de la misma semantica. Lo declaro como deuda en vez de callarlo: si un
   dia divergen, la guarda vigila un grafo distinto del que el motor sirve. **No lo arregle
   porque unificarlas no me lo ordena ninguna operacion**, y va como pregunta 3.
5. **Use `crosby_habilidad_transmision` como sede de la clave sucia**, que es el nodo real
   que `OP-S-06` limpio, en vez de crear un nodo de prueba sintetico como dice la letra
   (*"anadir a un nodo de prueba"*). Razon: un nodo nuevo mueve el conteo de ficheros en
   disco y toca otros chequeos del Gate; reinyectar la averia **en su sede historica** es
   mas fiel al fallo que la guarda tiene que cazar. **Es una desviacion de la letra y la
   marco como tal.**
6. **Fui a buscar la clave cirilica a `git show fa2e6011:` en vez de teclearla.** Parece
   celo excesivo para dos caracteres. Lo hice porque **el fallo entero de esa averia es que
   se ve identica a la buena**: una clave retipeada a ojo podia haber salido latina y el
   caso positivo habria pasado verde probando nada.
7. **Corri el caso positivo ANTES del arreglo, gastando una corrida entera de Gate 0 para
   verlo pasar en verde.** Se puede leer como gasto. Razon: `FASE_0_CODIGO.md` dice
   *"correrla ANTES del arreglo. Si pasa, esta mal escrita"*, y **eso solo se sabe
   corriendolo**. Sin esa corrida yo tendria una guarda que cae, pero no la prueba de que
   antes no caia.
8. **Declaro `OP-F-01` VERDE HOY pero NO HECHA.** Podia haberla dado por ejecutada: sus
   cuatro lineas verifican hoy. No lo hice porque su segunda linea **es una condicion de
   fin de fase** y `OP-F-04-HOR` la pone en rojo. **Marco la diferencia entre *verifica* y
   *esta hecha* en vez de aprovechar la ambiguedad a mi favor.**
9. **Pare en la fase 01 sin ejecutar `OP-F-03`**, que quiza si alcance por si sola. Razon:
   `OP-F-03` es la tarea de **verificar por lectura** 21 nodos, o sea leer, y **las dos
   paradas de la seccion 7 son de la misma fase y una de ellas toca la clasificacion de un
   nodo que `OP-F-03` tambien reclama** (`principio_calidad_mvp` esta en `OP-F-03`,
   `OP-D-01` y `OP-D-06`). **Meterme a leer 21 nodos con la fase en disputa me parecio
   trabajo que habria que rehacer.** Es discutible y puede ser exceso de prudencia.

---

## 11. PENDIENTES DE DOCTRINA Y PREGUNTAS

**PENDIENTES DE DOCTRINA (dos).**

1. **CERRADO EL DE LA VUELTA 23, y lo digo para que nadie lo arrastre.** *"Que hace una
   operacion de saneo cuando el propio Gate 0 REPONE lo que ella retira"* quedo resuelto por
   la decision del fundador (camino A) y **verificado hoy con instrumento**:
   `symmetrize_added` pasa de 33 a **0**. **No lo mantengo abierto.**
2. **NUEVO: un nodo puede estar en dos operaciones cuyas verificaciones se excluyen, y
   ninguna regla dice cual manda.** `background_startup_vs_corporativo` en `OP-F-01` y
   `OP-F-04-HOR` (seccion 7.2). El `orden` dice cual corre primero, **no cual verificacion
   gana al cerrar la fase**. **No escribo la regla: la traigo.**

**PREGUNTAS (cinco).**

1. **La linea base de blob de `08_VERIFICACION.md` queda desfasada en cuanto la fase III
   toca el grafo.** Hoy el registro dice `bb423c06...`, HEAD empezo en `6007c1da...` y acabo
   en `8d47ff32...`. **¿Se reescribe ese blob en cada operacion que toca el grafo, se
   sustituye por la regla *byte identico a HEAD* a secas, o se deja como registro
   historico?** No lo toque yo.
2. **¿Entra `sync_assets_web.py` en el ciclo registrado de Gate 0?** Hoy son dos comandos y
   la fase III necesita tres cada vez que una operacion cambia el grafo, porque **el chequeo
   de gemelos del Gate compara el snapshot de antes del paso 6 y no puede ver la divergencia
   recien creada**. La caza la suite del motor. **Corri el remedio escrito y no toque el
   registro** (discutible 2).
3. **Hay tres implementaciones del resolutor** (TypeScript en `graph.ts`, y dos en Python:
   la guarda de Gate 0 y mi instrumento). **¿Se unifican, y bajo que operacion?** Ninguna me
   lo ordena.
4. **El plan sigue sin estado para *ejecutada*.** Las 71 estan en `LISTA` y **seis ya
   corrieron**. ¿Se añade un estado, se marca por commit, o se deja hasta el cierre de fase?
   *(Sin respuesta desde la vuelta 22.)*
5. **`SALIDA_V24_OPC04_ANTES_DEL_ARREGLO.txt` queda commiteado con `GATE 0: OK` sobre un
   grafo averiado.** Es la prueba de que el caso positivo no era vacio, pero leido suelto
   parece un Gate 0 verde sobre basura. **¿Se conserva asi o se marca en el nombre?**
   *(Sin respuesta desde la vuelta 23.)*

---

## 12. ESTADO EN QUE DEJO LA RAMA

- **Rama `pasada-unica`.** HEAD al empezar `ba109e5e`; **dos commits de trabajo**,
  `82ee608a` y `96c14726`, **los dos ya en `origin`**, mas el commit de este reporte.
- **FASE 0 CERRADA:** `OP-C-01`, `OP-C-02`, `OP-C-03`, `OP-S-06`, **`OP-S-07`** y
  **`OP-C-04`** hechas; **`OP-C-05` DIFERIDA** por su `depende_de`, sin bloquear a nadie.
- **GATE 0 VERDE POR EL CICLO ESCRITO**, corrido **cinco veces**, la ultima sobre el arbol
  final: **EXITCODE 0**, `GATE 0: OK`, **71 etiquetas las cinco veces sin encoger**, blob
  **`8d47ff32`** identico al de HEAD, **cero ficheros con diferencia real**.
- **LAS DOS GUARDAS NUEVAS EN VERDE** sobre el catalogo limpio, y **caidas** en su caso
  positivo, con la salida guardada como prueba.
- **SUITES EN VERDE:** motor **24/24**, web **80 ficheros, 1.030 pasadas y 3 saltadas**,
  `tsc --noEmit` limpio.
- **EL GRAFO:** 3.835 nodos, 3.521 vivos, 314 deprecados, **16.800 enlaces**, 15 claves,
  **cero auto aristas de vivos tras resolver**, **cero claves renegadas**.
- **FASE 01 ABIERTA Y DETENIDA:** `OP-F-01` **verifica en verde hoy pero no esta hecha**;
  **`OP-F-02` y `OP-F-04-HOR` no alcanzan para ejecutarse sin decidir**, y **chocan entre si
  sobre `background_startup_vs_corporativo`**. **Ni un nodo de la fase 01 fue tocado.**
- **NINGUNA operacion de las fases 02 a 10 se toco.**

> **CONVOCO AL AUDITOR**, como el encargo manda. La parada es de la especie *el texto no
> alcanza para ejecutarse sin decidir*, y ademas trae una **contradiccion entre dos
> operaciones en `LISTA` de la misma fase**. **No escribi `docs/loop/PARA_ALEXIS.md`: esa
> pluma es del auditor** (`AUDITOR.md` seccion 4), y `EJECUTOR.md` regla 4 me manda escribir
> la parada **en el reporte**, que es lo que acabo de hacer.
