# FASE 08: LA VERIFICACION

**Operacion: `OP-V-01`. LISTA.**

---

## EL CRITERIO DE HECHO, y es uno solo

> **UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA.**
>
> **No cuando pasa verde: cuando se CAERIA.**

**Es el criterio del CASO POSITIVO de la FASE 0, aplicado a todo el plan.** Y tiene
una comprobacion barata: **correr la prueba ANTES del arreglo. Si pasa, no prueba
nada.**

---

## POR FASE

| fase | que tiene que dar verde |
|---|---|
| **0 CODIGO** | cada caso positivo **se cae antes** del arreglo y pasa despues |
| **01 FUENTES** | ningun nodo de la clase con pasos alterados; **el material del segundo libro reubicado, no borrado** |
| **02 DESTEJIDOS** | los **quince congelados** releidos; **cada perdida en el bloque del que proviene** |
| **03 FUSIONES** | un superviviente por acto, el resto **DEPRECADO CON ALIAS**; `resolverId` devuelve el superviviente |
| **04 ENLACES** | cada arista nueva **confirmada por lectura**, no por el instrumento; ninguna crea auto-arista tras resolver |
| **05 SANEO** | ningun id vivo con tratado extinto; los tres de Incoterms con su version; ningun nodo cablea `export.gov`; ninguna de las seis herramientas muertas; ningun nodo con dos claves de fase; **ningun nodo se cita a si mismo tras resolver** |
| **06 MESAS** | cada decision escrita **con su motivo y su cobertura al lado** (banco 9.26) |
| **07 ADUANA** | los cuatro controles mecanicos **corriendo en Gate 0** |

---

## LA VERIFICACION TRANSVERSAL, y su orden importa

1. **Gate 0 verde**
2. **suite verde**
3. **vuelo completo**
4. **prueba de rumbos** (ya comprueba que ningun ancla este deprecada)
5. **reindexado semantico**

### QUE ES **GATE 0 EN VERDE**, y es EL CICLO ESCRITO DE DOS COMANDOS

**REGISTRADO el 14 ago 2026 por adjudicacion del auditor** (`docs/loop/ACTA_AUDITOR.md`,
vuelta 21, seccion 4, puntos 1 y 2). **No borra nada de esta pagina: fija lo que la
linea 1 de la lista de arriba no decia.**

> **EL CRITERIO ES EL CICLO, NO LA INVOCACION A SECAS DEL VALIDADOR.**

| # | comando | que tiene que dar |
|---:|---|---|
| **1** | `python scripts/run_phase1.py --reaplico-curaduria` | **EXITCODE 0** y `GATE 0: OK` |
| **2** | `python scripts/etiquetas_de_cara.py --aplicar`, corrido **JUSTO DESPUES** | `dataset/metadata/master_graph.json` **BYTE IDENTICO a HEAD**: el mismo hash de blob |
| **3**, **CONDICIONAL** | `python scripts/sync_assets_web.py`, corrido **DESPUES del 2** y **SOLO cuando la operacion cambia el grafo** | **LAS DOS COPIAS byte identicas a HEAD**: `dataset/metadata/master_graph.json` y `web/lib/assets/master_graph.json` con el mismo hash de blob que HEAD |
| **4**, **CONDICIONAL** | `python engine/plan_readiness.py`, corrido **DESPUES del 2 y ANTES del 3**, **SOLO cuando la operacion cambia el CENSO del grafo** | regenera `engine/node_families.json` desde `dataset/metadata/master_graph.json` fresco; la vara es la suite web (`web/lib/readiness.test.ts`, paridad exacta) **en verde despues del 3**, que es lo que sincroniza el derivado al asset que la suite lee |

#### REGISTRO: **EL TERCER COMANDO, CONDICIONAL** (14 ago 2026, vuelta 26)

**Encargado por el acta de la vuelta 25 del auditor, y nace de la pregunta 2 del reporte de
la vuelta 24.** El comando 3 **es el remedio escrito del propio validador** (`REMEDIO_SYNC`
en `scripts/run_phase1.py`: *primero se reaplica, despues se sincroniza*), y sin correrlo
`engine/test_gate_alias.py` cae con los nodos divergentes entre las dos copias del grafo.

> **ES CONDICIONAL Y NO SE CORRE SIEMPRE: solo cuando la operacion CAMBIA EL GRAFO.** En una
> fase que no toca el grafo (una operacion de codigo, un registro documental) **el comando 3
> no aplica y no correrlo no es un rojo**. En una fase que si lo toca, **saltarselo deja las
> dos copias divergentes y la que lo caza es la suite del motor, no el Gate**: el chequeo de
> gemelos del Gate compara el snapshot de **antes** del paso 6 y no puede ver la divergencia
> que la operacion acaba de crear.

**LA VARA DEL COMANDO 3 ES DOBLE**, y por eso se escribe aparte de la del comando 2: no basta
con que el fichero del dataset calce con HEAD, **tienen que calzar LOS DOS**, el del dataset y
el de `web/lib/assets/`.

##### REGISTRO QUE FALTABA: **CONTRA QUE HEAD SE MIDE EL COMANDO 3** (14 ago 2026, vuelta 27)

**Encargado por el acta de la vuelta 26 del auditor, y responde a la pregunta 4 del reporte de
la vuelta 26.** La fila del comando 3 dice *las dos copias byte identicas a HEAD* y no decia
CUAL HEAD, y el dia que una operacion cambia el grafo esa frase sola es incumplible: antes del
commit el HEAD todavia es el de la operacion anterior, asi que las dos copias buenas y recien
sincronizadas **no** calzan con el.

> **LA VARA DEL COMANDO 3 SE MIDE CONTRA EL HEAD QUE TRAE EL COMMIT DE ESTA VUELTA**, no
> contra un blob citado en una pagina vieja ni contra el HEAD anterior a la operacion. Es
> **exactamente el mismo motivo** por el que el comando 2 ya lleva su calificador de corte: un
> blob escrito en una pagina es **registro historico**, y la **vara operativa** es *byte
> identico al HEAD DEL MOMENTO*, medida con `git hash-object` contra
> `git rev-parse HEAD:<ruta>` **despues de commitear la operacion**.

| momento | que dice el comando 3 | como se lee |
|---|---|---|
| **antes del commit** | las dos copias iguales **entre si**, y distintas de HEAD si la operacion toco el grafo | **no es un rojo**: es la operacion todavia sin commitear |
| **despues del commit** | las dos copias **byte identicas a HEAD**, mismo blob | **esta es la vara**, y es la que se publica en el reporte |

**LO QUE SIGUE SIENDO ROJO, y por eso el registro no ablanda nada:** que las dos copias
difieran **ENTRE SI** en cualquier momento, antes o despues del commit. **Esa es la averia que
el comando 3 vino a cazar**, y no depende de contra que HEAD se mire.

#### REGISTRO: **EL CUARTO COMANDO, CONDICIONAL** (14 ago 2026, decision del fundador)

**Encargado por el acta de la vuelta 28 del auditor. Misma forma que el comando 3:
condicional, y con su propio motivo escrito.** `python engine/plan_readiness.py`
**regenera `engine/node_families.json`**, un artefacto DERIVADO que clasifica cada nodo
en familias por palabra clave (el docstring de la herramienta lo dice con esas
palabras: *regenera engine/node_families.json*). `web/lib/readiness.test.ts` exige
**paridad exacta** contra ese derivado, y **el ciclo de dos comandos no lo regeneraba**:
un nodo nuevo o deprecado cambiaba el censo del grafo, el derivado quedaba viejo, y la
suite web caia por el desfase aunque el grafo mismo estuviera perfecto.

> **ES CONDICIONAL Y NO SE CORRE SIEMPRE: solo cuando la operacion CAMBIA EL CENSO** (crea
> o deprecia un nodo). En una operacion que no toca el censo (un reparto de bloque sin
> nodo propio, un registro documental) **el comando 4 no aplica y no correrlo no es un
> rojo**. En una que si lo toca, **saltarselo deja el derivado viejo y la que lo caza es
> `readiness.test.ts`**, no el Gate: ninguna de las guardas de `Gate 0` mide familias.

**EL ORDEN IMPORTA, y por eso el comando 4 corre ANTES del 3 aunque sea el ultimo en
numero:** `plan_readiness.py` lee `dataset/metadata/master_graph.json` (fresco tras el
comando 1) y escribe `engine/node_families.json`; `sync_assets_web.py` (comando 3) es
quien copia ese fichero a `web/lib/assets/node_families.json`, que es lo que la suite
web lee. Correr el 3 antes del 4 sincroniza el derivado VIEJO.

**IMPLEMENTADO Y VERIFICADO (14 ago 2026), con caso positivo en arbol de trabajo
temporal nunca commiteado:** un nodo nuevo en el censo, `readiness.test.ts` en ROJO
(1 fallo, 3835 contra 3836) antes de correr el comando 4; corrido `plan_readiness.py`
seguido de `sync_assets_web.py`, la suite pasa **3 de 3**. Ciclo completo corrido
despues, con el nodo de prueba borrado: `Gate 0` OK, motor 24 de 24, web 80 ficheros con
1.030 pasadas y 3 saltadas, `tsc` limpio, `dataset/` byte identico a HEAD.

#### REGISTRO: **`git status` NO ES LA VARA DE ESTE FICHERO** (14 ago 2026)

**En Windows, el simple hecho de tocar `dataset/metadata/master_graph.json` reemplaza
LF por CRLF, y `git status` lo marca como modificado sin que haya cambiado ni un dato.**

> **ESO NO ES LA VARA. LA VARA ES EL HASH DE BLOB BYTE IDENTICO A HEAD**, que es lo
> que mide el **comando 2** del ciclo de arriba.

**Quien lea un movimiento en `git status` sobre ese fichero, sin diferencia de contenido
real, NO esta viendo una regresion.** La comprobacion barata que lo separa: `git diff
--quiet` sale con **exit 0** y `git hash-object` sobre el fichero del disco devuelve el
mismo blob que `git rev-parse HEAD:dataset/metadata/master_graph.json`. **Si los dos
blobs coinciden, no hay movimiento que reportar por mucho que `git status` lo liste.**

**LA INVOCACION A SECAS NO ES UN ROJO QUE CLASIFICAR.** `python scripts/run_phase1.py`
sin `--reaplico-curaduria` sale con **exit 2 SIEMPRE que haya curaduria viva**, y eso
**es la alarma del propio instrumento funcionando**, no una regresion. Esta escrito en
el comentario fechado **2026-08-07** dentro de `scripts/run_phase1.py`, **lineas 941 a
958** (verificado contra el archivo el 14 ago 2026): la recompilacion borra la
curaduria porque las etiquetas de cara **no viven en los nodos**, viven en
`dataset/metadata/etiquetas_de_cara_v1*.json`, y el script **avisa y falla a proposito
en vez de auto aplicarlas**, porque auto aplicarlas crearia una segunda fuente de
curaduria que el remache de `integrar_packs` prohibe.

> **QUIEN RECOMPILA, REAPLICA** (`scripts/run_phase1.py`, **linea 955**). El ejecutor
> que corra Gate 0 **reaplica la curaduria acto seguido**, y **si el conteo de etiquetas
> aplicadas ENCOGE al reaplicar, lo declara en el reporte en vez de callarlo**: ese
> encogimiento es el sintoma de un nodo curado que una operacion de la pasada depreco,
> renombro o fundio, y callarlo seria exactamente la degradacion silenciosa que el canon
> de fallar ruidoso prohibe.

**LA CIFRA DE LA LINEA BASE, con su corte:** al 14 ago 2026, sobre `HEAD` de
`pasada-unica`, el ciclo cierra con **71 etiquetas reaplicadas** y el blob
`bb423c066f5a961f082b3b70aaff4f98d35d7a1d`, que es el de HEAD. **Esa es la cifra contra
la que se compara el encogimiento.**

#### CALIFICADOR DE CORTE DEL BLOB: **ES REGISTRO HISTORICO, NO LA VARA OPERATIVA** (14 ago 2026, vuelta 26)

**Encargado por el acta de la vuelta 25 del auditor, y responde a la pregunta 1 del reporte
de la vuelta 24. El parrafo de arriba se queda entero: el blob `bb423c06` era el de HEAD el
dia en que se escribio.**

| | |
|---|---|
| **el blob `bb423c06...`** | **REGISTRO HISTORICO** con su corte. Nombra el HEAD de un dia concreto y **queda desfasado en cuanto una operacion de la fase III toca el grafo**, que es exactamente lo que esa fase hace |
| **LA VARA OPERATIVA** | **byte identico al HEAD DEL MOMENTO**, sea cual sea ese HEAD. Se mide con `git hash-object` contra `git rev-parse HEAD:<ruta>`, no contra un blob escrito en esta pagina |
| **LA CIFRA QUE SE VIGILA** | **el conteo de 71 etiquetas**. Esa si es comparable entre vueltas, y **si ENCOGE se declara** en vez de callarse |

> **POR QUE IMPORTA LA DISTINCION: un blob distinto del de esta pagina NO ES UNA REGRESION,
> y un conteo de etiquetas menor que 71 SI LO ES.** Confundirlos hace las dos averias: obliga
> a reescribir esta pagina en cada operacion, y deja pasar el unico sintoma que de verdad
> avisa de un nodo curado que se depreco, se renombro o se fundio.

> **EL REINDEXADO VA AL FINAL, DESPUES DE MOVER IDS.** El indice **guarda ids** y
> es **una de las fuentes externas que `OP-S-08` identifico**. Reindexar antes deja
> el indice apuntando a la era anterior, **y el sintoma no aparece en el
> reindexado: aparece semanas despues en el recorrido de una persona.**

#### CORRECCION DECLARADA: **ROJO DECLARADO DEL INDICE SEMANTICO DURANTE LA FASE III, EXCLUSIVO PARA IDS NUEVOS** (14 ago 2026, decision del fundador, opcion B estricta)

**Resuelve la contradiccion medida en el acta de la vuelta 26: el plan mandaba a la vez
Gate 0 verde entre fases Y reindexado al final, despues de mover ids, y el dia que una
operacion crea un nodo las dos reglas no se podian cumplir juntas** (el unico instrumento
que fabrica vectores exige una credencial que esta fuera del repo mientras el bucle
corre, por regla del fundador). El parrafo de arriba sobre el reindexado al final **se
queda entero: sigue siendo la regla.** Lo que se anade es la excepcion que la hace
ejecutable:

> **DURANTE LA FASE III, EL CHEQUEO DEL INDICE SEMANTICO PUEDE ESTAR EN ROJO DECLARADO
> EXCLUSIVAMENTE PARA LOS IDS QUE LA PASADA ACABA DE CREAR.** ~~Cada reporte que corra Gate
> 0 con ese rojo los lista uno a uno, por id, con la operacion que los creo.~~ **CUALQUIER
> OTRO id en rojo en el chequeo del indice es PARADA**: no se declara, se trae.

#### CORRECCION DECLARADA: **LA OPCION B SE EXTIENDE A TODAS LAS SEDES** (14 ago 2026, decision del fundador)

**Resuelve el motivo 1 de la parada del acta de la vuelta 27: el MISMO chequeo (todo
activo tiene vector) vive en TRES sedes, no en una, y la correccion de arriba solo
nombraba `Gate 0`.** El auditor lo leyo en codigo: `engine/test_aviso_curaduria.py`
(fixture `test_todo_activo_tiene_vector_en_el_indice`, que mide `activos - ids` **contra
el repo real**) y `.githooks/pre-commit` (aborta el commit si la suite del motor esta en
rojo, sin excepcion escrita). Con un nodo nuevo en el arbol, **ningun commit entraba al
historial**, ni uno que no lo tocara: la cerradura bloqueaba el fallback entero de `P.18`
(nodo propio), no una operacion.

> ~~Cada reporte que corra Gate 0 con ese rojo los lista uno a uno~~ **CADA SEDE QUE MIDA
> EL INDICE SEMANTICO RESTA LOS IDS DECLARADOS Y LOS IMPRIME UNO A UNO**, en las tres:
> `Gate 0` (`scripts/run_phase1.py`), el fixture del motor
> (`engine/test_aviso_curaduria.py`) y, por herencia, `.githooks/pre-commit` (que solo
> corre las suites y no tiene chequeo propio del indice).

**MECANISMO: lista versionada `docs/plan/INDICE_ROJO_DECLARADO.jsonl`**, una linea por
id declarado, `{"id": ..., "operacion": ..., "fecha": ...}`. **SOLO las operaciones de la
pasada escriben ahi, al crear un nodo.** Las sedes RESTAN exactamente esos ids de los
activos sin vector y los imprimen; **cualquier otro id sin vector sigue siendo rojo que
para**, sin excepcion. Hoy, sin ninguna operacion ejecutada, **la lista esta VACIA**.

**IMPLEMENTADO Y VERIFICADO (14 ago 2026), con caso positivo en arbol de trabajo temporal
nunca commiteado:**

| sede | que se toco | caso positivo |
|---|---|---|
| `scripts/run_phase1.py` | nueva funcion `indice_rojo_declarado()`; el chequeo del indice resta sus ids antes de fallar y los imprime con operacion y fecha | un id nuevo SIN declarar: `GATE 0: FALLIDO`. El MISMO id DECLARADO: `GATE 0: OK`, con la linea impresa |
| `engine/test_aviso_curaduria.py` | `test_todo_activo_tiene_vector_en_el_indice` importa `indice_rojo_declarado` y resta antes del `assert`; nuevas aserciones de forma sobre el codigo de `run_phase1.py` | mismo id, sin declarar: el fixture CAE con `AssertionError` nombrando el id. Declarado: pasa e imprime la linea |
| `.githooks/pre-commit` | **sin cambio de codigo**: solo corre las suites, no tiene chequeo propio del indice; hereda el arreglo de la sede anterior | la suite del motor entera, `engine/run_all_tests.py`, corrida con el id declarado: **24 de 24** |

**Corrido entero tras el arreglo, con el nodo de prueba borrado y la lista vacia de
nuevo:** `Gate 0` OK, blob byte identico a HEAD; motor 24 de 24; web 80 ficheros, 1.030
pasadas y 3 saltadas; `tsc` limpio; `dataset/` byte identico a HEAD. **`docs/plan/` gana
un archivo nuevo, `INDICE_ROJO_DECLARADO.jsonl`, vacio.**

**El reindexado sigue haciendose AL FINAL, tras mover ids, como esta pagina ya manda.**
Esta correccion no cambia CUANDO se reindexa: cambia que Gate 0 puede correr en verde en
todo lo demas mientras existan ids nuevos sin vector, en vez de bloquear cada fase de la
pasada esperando una credencial que la casa reserva.

> **EL CIERRE DE LA FASE III EXIGE REINDEXADO HECHO Y GATE 0 ENTERO EN VERDE, SIN
> EXCEPCIONES, ANTES DE LA AUDITORIA INTEGRAL Y DEL MERGE.** El rojo declarado es un
> permiso para avanzar DURANTE la pasada, no una excepcion permanente: **sin el
> reindexado corrido y el chequeo del indice semantico en verde como todos los demas,
> la campaña no se declara consumada.**

#### CORRECCION DECLARADA: **LA CIFRA DE CENSO DE LA SUITE WEB PASA A PARIDAD CONTRA EL DATO** (14 ago 2026, decision del fundador, camino a)

**Resuelve la tercera hilada del muro, medida en el acta de la vuelta 28: la
correccion del rojo declarado cubre el chequeo del indice semantico, no el censo.**
`web/lib/engine/graph.test.ts` **clavaba `toBe(3835)` a mano** (*carga los 3835 nodos
reales*), y cada nodo propio de la pasada la rompia, dejando el arbol incommitteable
por una cifra que la campaña entera existe para mover.

> ~~`expect(Object.keys(graph).length).toBe(3835)`~~ **LA PRUEBA MIDE PARIDAD CONTRA
> `total_nodos`**, el campo que el compilador Python escribe en el mismo asset que
> `cargarGrafo()` ya lee (`web/lib/assets/master_graph.json`). Verifica que el parser de
> TypeScript no pierda un nodo en silencio, **sin pedir una edicion manual por
> operacion**: un censo que se mueve legitimamente en `dataset/` mueve las dos cifras a
> la vez, y la prueba queda verde sin tocarla.

**IMPLEMENTADO Y VERIFICADO (14 ago 2026), con caso positivo en las DOS direcciones,
en arbol de trabajo temporal nunca commiteado:**

| direccion | como se probo | resultado |
|---|---|---|
| **un nodo quitado del grafo cargado la tumba** | se borro un id de `nodos` en `web/lib/assets/master_graph.json`, dejando `total_nodos` intacto en 3835 | **FALLO**, nombrando la diferencia exacta: *cargados 3834 vs total_nodos 3835* |
| **un censo movido legitimamente la deja verde, sin editar la prueba** | se creo un nodo real en `dataset/nodos/` y se corrio el ciclo completo (comandos 1, 2 y 3), que mueve `nodos` y `total_nodos` juntos, a 3836 | **PASO**, sin tocar `graph.test.ts` |

Ciclo completo corrido despues, con el nodo de prueba borrado: `Gate 0` OK, motor 24 de
24, web 80 ficheros con 1.030 pasadas y 3 saltadas, `tsc` limpio, `dataset/` byte
identico a HEAD.

---

## LA COMPROBACION QUE SOLO SE PUEDE HACER AL FINAL

**Recomputar el cierre transitivo** y comprobar dos cosas:

- **los actos ejecutados desaparecieron**
- **ninguno nuevo aparecio por sorpresa**

> **Y por la regla P.1 del banco del plan: ese recomputo, como cualquier conteo que
> toque ids, PASA POR EL RESOLUTOR ANTES DE CONTAR.** Un recomputo literal sobre un
> grafo recien fusionado **contaria los absorbidos como nodos vivos.**

---

## EL DISPARADOR DEL RECOMPUTO

**Se dispara EL DIA QUE EL CRIBADO LLEGUE AL PUESTO 3.388**, y no antes. Es la
**unica** recomputacion general del plan (banco 9.21).

> **Por que una sola vez y no en cada checkpoint: un barrido de cruce cuesta lo
> mismo con 2.117 pares que con 3.388, y solo el ultimo es el bueno.** Los de en
> medio producen cifras que hay que volver a escribir.

### QUE SE RECOMPUTA, Y EN ESTE ORDEN

**El orden no es de comodidad: cada paso usa la salida del anterior.**

| # | que | por que va aqui |
|---:|---|---|
| **1** | **EL RETRATO DE LAS A** | es el insumo de todo lo demas: la lista de A vigentes al cierre |
| **2** | **EL BARRIDO DE CONFIRMADAS contra las A** | cruza las costuras confirmadas contra el retrato del paso 1. **Da las curas acopladas** |
| **3** | **EL CIERRE TRANSITIVO** | las componentes se calculan **sobre el retrato del paso 1**, no sobre el archivo crudo |
| **4** | **LAS NOMINAS Y LOS ACTOS** | cada racimo y cada acto se re-mide **con su cobertura al lado** (banco 9.26), usando las componentes del paso 3 |

> **Y por la regla P.1 del banco del plan, LOS CUATRO RESUELVEN ANTES DE CONTAR.**
> Un recomputo literal sobre un grafo ya fusionado **contaria los absorbidos como
> nodos vivos**, y sobre uno sin fusionar **no veria las auto-aristas via alias**.

### QUE OPERACIONES CAMBIAN DE ESTADO CON EL RESULTADO

| operacion | hoy | despues del recomputo |
|---|---|---|
| **`OP-U-02`** | DECISION PENDIENTE | **pasa a LISTA** con la lista definitiva de actos cerrados. Es la unica que el recomputo desbloquea por si solo |
| **`OP-U-01`** | LISTA con **173 actos** | **la cifra se reescribe**: algunos de los 48 abiertos habran cerrado, y **puede que alguno de los 173 haya crecido y se abra** |
| **`OP-L-02`** | DECISION PENDIENTE | **el universo de 205 se remide**: cada A nueva puede crear pares internos nuevos fuera de cola |
| **`OP-M-01` a `OP-M-05`** | DECISION PENDIENTE | **sus nominas se re-miden con cobertura**. Una mesa puede **crecer**, y la mesa unida es la candidata |
| **`OP-D-01` a `OP-D-06`** | LISTA | **los trece actos del cierre transitivo se recomputan.** Los repartos de perdidas **no cambian**; los tamanos si pueden |

> **LO QUE EL RECOMPUTO NO PUEDE CAMBIAR, y conviene decirlo para que nadie lo
> espere:** el **ORDEN** de la fase 02. Se decide por **congelados liberados**, y
> **una A nueva no mueve un congelado.**

### EL LOTE DE LECTURA QUE VIAJA CON EL RECOMPUTO

**ADJUDICADO el 11 ago 2026: el inventario final NO lleva ninguna nomina con
cobertura incompleta pudiendo cerrarla con cinco lecturas.**

| nomina | cobertura hoy | lecturas que faltan |
|---|---|---:|
| **el sales roadmap** | **10 de 15**, MEZCLADO desde el puesto 872 | **5** |

**LOS CINCO PARES**, nombrados para que el lote no haya que reconstruirlo:

- `customer_validation_sales_roadmap` contra `estrategia_de_ventas`
- `customer_validation_sales_roadmap` contra `sales_roadmap`
- `estrategia_de_ventas` contra `hoja_de_ruta_de_ventas`
- `estrategia_de_ventas` contra `refinar_sales_roadmap`
- `estrategia_de_ventas` contra `sales_roadmap_vs_sales_force`

> **Se leen CON el recomputo y no antes**, por dos razones que se suman: su clase
> ya esta decidida, asi que no urgen; y **el recomputo puede meter miembros nuevos
> en la nomina**, con lo que leer antes obligaria a volver.

> **Y la regla que esto deja escrita, que es mas grande que estos cinco: TODA
> NOMINA QUE SE PUEDA CERRAR CON UNA TANDA CORTA SE CIERRA ANTES DEL INVENTARIO
> FINAL.**

### LO SEGUNDO QUE VIAJA CON EL RECOMPUTO: **`OP-E-03`, LA DIFERENCIA CONTRA LA COLA**

**Enganchada aqui el 11 ago 2026 por adjudicacion del auditor.** El barrido
calibrado **no abre puerta nueva al cribado**: se corre **el dia en que la cola de
un dominio cierra**, y solo aporta **lo que no estaba en la cola**.

| cuando | que se corre | sobre que |
|---|---|---|
| al cerrar la cola de **cada dominio** | `scripts/plan/diferencia_contra_cola.py --dominio <el que cerro>` | sus candidatos del barrido calibrado |
| al cerrar **el catalogo entero**, puesto 3.388 | el mismo, sin `--dominio` | los 477 |

**LO QUE SALE Y QUE SE HACE CON ELLO:** `docs/plan/DIFERENCIA_CONTRA_COLA.jsonl`,
con su cuenta por dominio. **Esa diferencia va a LECTURAS DIRIGIDAS**, se marca como
tal, **no entra en la cola y no mueve el marcador**, y **sus veredictos se cuentan
aparte de la tasa por dominio** para no contaminarla.

> **POR QUE NO SE PUEDE CORRER ANTES.** Mientras la cola del dominio no este
> planificada, **su diferencia es un TECHO y no una cuenta.** El ensayo en vacio del
> 11 ago 2026 dio 387 de diferencia sobre 477, con `quality` aportando 167 **solo
> porque su cola todavia no existe.**

> **Y LA COMPROBACION DE QUE CORRIO BIEN ES ARITMETICA: filas igual a pares
> repetidos mas ya en cola mas diferencia.** Si no cuadra, el resolutor cambio o la
> cola se movio bajo los pies. Una nomina con cobertura incompleta en el inventario **no dice lo que
> hay: dice hasta donde se miro.**

---

### LA COMPROBACION DE QUE EL RECOMPUTO CORRIO BIEN

**Tres cifras que tienen que cuadrar entre si**, y si no cuadran el recomputo esta
mal hecho:

1. **nodos en actos** igual a la suma de los tamanos de las componentes
2. **A vigentes** igual a la suma de aristas internas de todas las componentes
3. **todo acto marcado CERRADO** tiene sus pares internos leidos **y** ningun
   miembro con par pendiente

> **Y una cuarta, que es la que caza el error de P.1**: **ningun nodo deprecado
> aparece dentro de una componente.** Si aparece, el instrumento no resolvio.

---

## LA COLA DE RELECTURA POST FUSION

**Abierta el 12 ago 2026, y nace de un hueco que ninguna fase recogia.** El banco 9.10
manda **recomputar del archivo**, pero **no dice que una fusion pueda obligar a
releer un par YA CERRADO.**

> **EL DISPARADOR, y es mecanico: UN PAR VUELVE A LA COLA CUANDO UNO DE SUS DOS NODOS
> MUERE EN UNA FUSION O CAMBIA DE TEXTO.**

**POR QUE SOLO LOS B Y LOS C, y no todos:** un **D** dice que los dos nodos son sanos,
y fundir uno de ellos con un tercero **no lo vuelve gemelo del otro**. Un **A** ya
esta resuelto por definicion. **Lo que se mueve es lo que estaba en el filo**: el
dudoso, que puede caer a cualquier lado, y el enlace mutuo, que puede dejar de serlo
si uno de sus dos lados cambia.

### LA LISTA, barrida el 12 ago 2026 sobre las diecisiete fusiones del plan

| par | clase | que le pasa | tras que operacion |
|---:|---|---|---|
| **707** | **B** | `customer_discovery_overview` **MUERE** | `OP-M-05-INDICE` |
| **1096** | **A** | su contraparte muere **y su A se volveria contradiccion con su propia D** | `OP-M-05-APERTURA` |
| **196** | **B** | `fase_acclimate_mapa_de_proceso` **MUERE** | `OP-M-02-ACCLIMATE` |
| **253** | **B** | `fase_acclimate_experiencia_cliente` **cambia de texto** | `OP-M-02-ACCLIMATE` |
| **224** | **B** | `fase_assess_ciclo_cliente` **cambia de texto** | `OP-M-02-ASSESS` |
| **591** | **B** | `pivote_estrategico` **cambia de texto** | `OP-M-03-III` |
| **968** | **B** | `pivote_o_proceder` **cambia de texto** | `OP-M-03-II` |

**LOS DOS ESTRENOS SON EL 707 Y EL 1096**; los otros cinco los levanto el barrido.

**Y UNA CAE, y se dice para que nadie la busque:** el puesto **751**,
`customer_validation_sell_phase` contra `verificar_product_market_fit`, **estaba en la
lista y sale**, porque **`LD-59` dejo a ese nodo fuera de la fusion: ya no muere.**

### LOS SIETE DEL PIVOTE NO ENTRAN, y hay que decir por que

**Los puestos 668, 737, 753, 771, 843, 957 y 1298 son B y sus nodos mueren o cambian**,
pero **no se releen: se REESCRIBEN**. `OP-M-03` ya los resolvio **por el criterio**, y
su clase nueva esta adjudicada. **Releerlos seria decidir dos veces lo mismo.**

> **LA DIFERENCIA IMPORTA: un par que una adjudicacion resolvio NO vuelve a la cola.
> Vuelve el que sigue abierto y cuyo texto cambia bajo los pies.**

### QUE PASA CON LO QUE SE RELEA

| si sale | |
|---|---|
| **A** | entra en la fusion que le corresponda, **y su perdida se nombra antes** |
| **D** | se queda, y **si hay jerarquia se enlaza** |
| **B otra vez** | **va a la lista de decisiones del inventario final**, y se dice que quedo dudoso dos veces |

> **Y LA COMPROBACION DE QUE ESTA COLA SE CORRIO: al cerrar, ningun par de la lista
> sigue con su clase vieja apuntando a un nodo que ya no existe.** **Si uno la
> conserva, es que la relectura no se hizo.**

### REGISTRO: **LA COLA TAMBIEN RECIBE LAS COSTURAS QUE UN REPARTO CREA** (14 ago 2026, vuelta 28)

**Adjudicado por el acta de la vuelta 27 del auditor (seccion 4, punto 2), POR EXTENSION
CITADA y sin doctrina nueva:** `P.3` manda repartir y prohibe podar, la fase 02 es la que
desteje, y esta cola existe para las costuras que las reuniones crean. **La lista de siete
de arriba se queda entera: nace de las fusiones y esto no la toca.**

> **UNA REPETICION QUE UN REPARTO DE LA FASE 01 CREA DENTRO DE UN MIEMBRO ENTRA A LA
> NOMINA DE LA FASE 02 COMO COSTURA NUEVA, Y NO SE DESTEJE EN EL ACTO.** Destejer en el
> acto seria una operacion que ninguna pagina escribio, y el verbo de la operacion que la
> creo es **repartir**, no elegir por cual mitad se queda.

**LA PRIMERA COSTURA QUE ENTRA POR ESTA PUERTA, con su medicion de hoy:**

| miembro | que recibio | medido hoy |
|---|---|---|
| `ejecucion_incremental_transicion_tecnologica` | los bloques de `modelo_hibrido_agile_stage_gate`, `principio_calidad_mvp` y `reduccion_tamano_de_lote_batch_size`, los tres de `OP-F-03` por `P.18` | **16 pasos**, contra los 4 que tenia antes del reparto |
| `fases_traccion_producto` | los pasos 4 a 6 de `fit_problema_solucion`, de `OP-F-04-WEI` por `P.18` | **7 pasos**, contra los 4 que tenia antes del reparto. **Los tres que entraron repiten sus pasos 1, 2 y 4** casi literales: identificar la fase, mandar en Fase I un flujo pequeno y constante para ver por donde se fuga el producto, y escalar marketing solo al confirmar el ajuste. **El unico de los cuatro viejos sin gemelo es su paso 3**, el del feedback de los clientes tempranos |
| `clasificacion_leads_abc` | los pasos 5 a 9 de `sales_funnel_get_keep_grow`, de `OP-F-04-WEI` por `P.18` | **10 pasos**, contra los 5 que tenia antes del reparto. **Tres de los cinco que entraron repiten**: el nuevo 7 dice las mismas tres categorias con las mismas cifras que sus pasos 1 y 2, el nuevo 8 el mismo 66 a 75 por ciento de su paso 3, y el nuevo 9 el mismo pase de los C a marketing de su paso 4. **Los otros dos no tienen gemelo**: generar leads por marketing antes de aplicar ventas, y coordinar el collateral con marketing |
| `bullseye_framework` | los pasos 8 a 12 de `plan_de_adquisicion_acquire`, de `OP-F-04-WEI` por `P.18` | **11 pasos**, contra los 6 que tenia antes del reparto. **Cuatro de los cinco que entraron repiten**: listar los 19 canales (su paso 1), disenar la prueba barata y corta por canal (su paso 3), medir resultados concretos (sus pasos 3 y 4) y comparar entre canales para elegir donde invertir mas (su paso 5). **El quinto no tiene gemelo**: anotar lo aprendido de cada prueba, incluidas las que fallaron |
| `publicidad_offline_pruebas_locales` | los pasos 5 a 8 de `earned_vs_paid_media`, de `OP-F-04-WEI` por `P.18` | **9 pasos**, contra los 5 que tenia antes del reparto, y **el solape es PARCIAL, uno de cuatro**: solo el nuevo 9 (empezar con pruebas pequenas y economicas antes de escalar) repite sus pasos 1 y 4. **Los otros tres traen material que el miembro no tenia**: preguntar que medios se consumen fuera de internet, pedir a cada medio su prospecto de audiencia y comparar alcance contra precio. Es la ELECCION del medio, y el miembro PRUEBA |
| `compromiso_linea_tiempo_cliente` | el paso 10 de `sales_funnel_get_keep_grow`, de `OP-F-04-WEI` por `P.18` | **6 pasos**, contra los 5 que tenia antes del reparto. **El unico que entro repite sus pasos 2 y 3**, comunicar el cronograma y pedir el si o el no explicito, que es la MISMA lectura con la que el acta de la vuelta 28 sostuvo el destino (discutible 9: *palabra por palabra el objeto del miembro*) |
| `producto_como_servicio_de_acceso` **(NODO NUEVO, no miembro)** | los DOS bloques de `transicion_producto_a_experiencia`, pasos 5 a 8 y 9 a 12, de `OP-F-03` por `P.18` punto 3 mas la adjudicacion 3 del acta de la vuelta 27 | **nace con 8 pasos y con la costura dentro**, medida hoy: **su paso 5 repite al 1** (reformular el producto como acceso en vez de venta de propiedad) y **su paso 6 repite al 2** (identificar barreras de adopcion). **No es un error del reparto: los dos bloques ya venian repetidos DENTRO del donante**, que declara a Hugos dos veces con dos grafias, y partirlos en dos nodos habria fabricado el gemelo que la adjudicacion 3 prohibe |
| `anillo_interior_explotar_el_canal_nucleo` **(NODO NUEVO, no miembro)** | los TRES bloques de `enfoque_motor_unico_crecimiento` (5 a 9), `optimizacion_embudo_get_customers` (6 a 10) y `ab_testing_optimizacion` (11 a 15), de `OP-F-04-WEI` por `P.18` punto 3 mas la adjudicacion 3 | **nace con 15 pasos y es la costura mas grande de esta puerta hasta hoy**, medida hoy: **su paso 6 repite al 1** (concentrarse en el canal que gano el anillo medio) y **sus pasos 11 a 14 repiten al 7** (la prueba A/B dentro del canal). **Los tres donantes describian el mismo anillo interior**, que es justamente lo que la lectura de `P.18` afirmo al mandarlos al mismo destino |
| `alineacion_bd_metricas_core` | los pasos 6 a 10 de `key_partners_hypothesis`, de `OP-F-04-WEI` por `P.18` | **9 pasos**, contra los 4 de antes. **Tres de los cinco que entraron repiten**: el nuevo 5 su paso 1 (definir la metrica de traccion antes de buscar socios), el nuevo 7 su paso 2 (evaluar si el socio mueve la aguja) y el nuevo 9 su paso 3 (rechazar el acuerdo atractivo desalineado del Critical Path). **La repeticion es la misma evidencia que sostuvo el destino** |
| `pipeline_alianzas_bd` | los pasos 11 a 14 de `key_partners_hypothesis`, de `OP-F-04-WEI` por `P.18` | **9 pasos**, contra los 5 de antes, y **el solape es PARCIAL, uno de cuatro**: solo el nuevo 6 (que tipo de alianza resuelve tu cuello de botella) toca su paso 3, el de categorizar socios por atributos. Los otros tres (licensing, socios de distribucion, supply partnerships) traen tipos que el miembro no nombraba |
| `sem_estrategia_ejecucion` | los pasos 6 a 9 de `metricas_de_adquisicion_activacion`, de `OP-F-04-WEI` por `P.18` | **12 pasos**, contra los 8 de antes, y **el solape es PARCIAL, uno de cuatro**: solo el nuevo 9 (definir que es una conversion antes de lanzar) toca su paso 6, el del rastreo de conversiones. Los otros tres (CTR, CPC y CPA; el costo de adquisicion contra el valor de vida; el SEM como aprendizaje de mensaje) traen la cuenta economica que el miembro no tenia |

**No es un error del reparto: es la medida de que los tres traian el mismo material de
Hugos**, que es justamente lo que la tercera clase de `OP-F-03` afirmaba. **La lectura que
lo decide es de la fase 02, no de la 01.**

#### REGISTRO: **LAS CINCO COSTURAS DE `OP-F-04-WEI` ENTRAN A LA COLA** (14 ago 2026, vuelta 29)

**Encargado por el acta de la vuelta 28 del auditor (seccion 3, punto 2), que las adjudico
a correccion y no a caida:** el registro de esta misma puerta se escribio en la MISMA vuelta
que ejecuto `OP-F-04-WEI`, y **las costuras que ese reparto creo no entraron**. La primera
fila de la tabla, la de la vuelta 28, se queda tal como se escribio; **las cinco filas
nuevas son de la vuelta 29 y traen su medicion propia**.

**LA MEDICION, con su instrumento y su corte:** `scripts/loop/vuelta29_costuras.py`, salida
completa con los pasos impresos uno a uno en `docs/loop/SALIDA_V29_COSTURAS.txt`, corte
**14 ago 2026**. Los pasos de HOY se leen del arbol de trabajo; **los de ANTES del reparto
se leen del commit `4e6349ea`**, el ultimo anterior a `f69f4819`, que es el que ejecuto los
cinco cortes. **No se desteje ninguna: solo se declaran.**

**DOS COSAS QUE LA MEDICION LEVANTO Y EL ENCARGO NO NOMBRABA, declaradas y NO arregladas:**

> **PRIMERA, `publicidad_offline_pruebas_locales`: el solape es PARCIAL y la cifra lo dice,
> uno de cuatro.** El acta lo sospechaba y la medicion lo confirma: tres de los cuatro pasos
> que entraron traen material nuevo. **Entra igual a la cola**, porque la regla de esta
> puerta habla de *una repeticion*, no de un bloque entero repetido, **y entra con su cifra
> al lado para que la fase 02 no la lea como las otras cuatro.**

> **TERCERA, y es de `OP-F-03` y no de WEI: `producto_como_servicio_de_acceso` NACE con la
> costura dentro, y la fila lo dice.** Es el primer caso de esta puerta en que la repeticion
> no cae dentro de un miembro que ya existia, **sino dentro de un nodo que la propia
> operacion acaba de crear**. La regla escrita habla de *un miembro*; la extension es natural
> y no inventa doctrina (el disparador es la repeticion, no el domicilio), pero **se declara
> como lo que es, y va marcada en el reporte de la vuelta 29 para que el auditor la
> adjudique**. **Y hay un cabo que la fase 02 tendra que mirar aparte: sus pasos 7 y 8 no
> repiten nada y tampoco son del objeto del nodo** (las tres interfaces de usuario son de la
> parte de SISTEMAS de Hugos, como `01_FUENTES.md` ya senalaba en la vuelta 27, y el ultimo
> mira el modelo desde la economia circular). **No se destejen aqui: el verbo de la operacion
> que los movio es repartir.** Queda **PENDIENTE DE DOCTRINA**: la cola tiene disparador para
> la repeticion y no lo tiene para el paso bien copiado que quedo en el nodo equivocado.

> **SEGUNDA, `compromiso_linea_tiempo_cliente` es una QUINTA costura que el acta no nombro.**
> El acta nombro tres y mando revisar una cuarta; el instrumento midio los cinco receptores
> del reparto y este tambien repite. **La regla de esta puerta es mecanica** (*una repeticion
> que un reparto de la fase 01 crea dentro de un miembro entra a la nomina de la fase 02*),
> y el propio acta de la vuelta 28 ya habia leido esa repeticion al sostener el destino.
> **Declararla es aplicar la regla; callarla porque el encargo no la nombraba seria la misma
> omision que esta correccion viene a reparar.**

#### REGISTRO: **LA COSTURA DENTRO DE UN NODO RECIEN CREADO ENTRA POR LA PRIMERA PUERTA** (14 ago 2026, vuelta 30)

**ADOPTADA POR CITA, sin doctrina nueva. Adjudicada por el acta de la vuelta 29 del auditor
(`docs/loop/ACTA_AUDITOR.md`, seccion 4, punto 3), que la concede POR EXTENSION CITABLE.** La
letra de la primera puerta dice *dentro de un miembro*, y los dos casos que la vuelta 29 midio
(`producto_como_servicio_de_acceso` y `anillo_interior_explotar_el_canal_nucleo`, filas de la
tabla de arriba) son nodos que la propia operacion acababa de crear. **La pregunta era si esa
letra los alcanza, y la respuesta esta escrita en el banco, no aqui.**

> **`P.18` PUNTO 3 DICE QUE EL BLOQUE SIN MIEMBRO COINCIDENTE FORMA NODO PROPIO *DENTRO DE LA
> FAMILIA*: EL NODO PROPIO NACE MIEMBRO DE SU FAMILIA.** Y **EL DISPARADOR DE ESTA PUERTA ES LA
> REPETICION, NO EL DOMICILIO.** Un nodo creado hoy es miembro hoy, asi que la costura que nace
> dentro de el entra por la misma puerta que la costura de un miembro viejo, y entra igual.

**LO QUE ESTO CIERRA, dicho con su nombre:** el *PENDIENTE DE DOCTRINA* que la TERCERA nota del
registro de arriba dejo abierto sobre `producto_como_servicio_de_acceso`. **La nota se queda
entera donde esta**, porque una correccion que tapa lo que corrige no se puede auditar; esta
linea le pone al lado la adjudicacion que la resuelve. **Las dos costuras quedan bien declaradas
y no se vuelven a declarar.**

**LO QUE ESTO NO CIERRA, y va aparte a proposito:** el otro cabo de esa misma nota, *el paso bien
copiado que quedo en el nodo equivocado*, **NO se resolvio por extension**: el acta 29 lo mando a
PARADA en su adjudicacion 2 (*extender la cola a material sin gemelo es escribir una puerta
nueva, no citar una*), y **la puerta nueva la escribio el fundador**, y es la seccion siguiente.

### LA COLA GANA SU SEGUNDA PUERTA: **LA COLA DEL OBJETO AJENO** (14 ago 2026, decision del fundador)

**Resuelve el pendiente de doctrina que la vuelta 29 midio tres veces: la primera puerta
dispara con REPETICION** (*una repeticion que un reparto crea dentro de un miembro*), **y
hay un material distinto que ninguna puerta cazaba: sano, sin gemelo, pero AJENO al
objeto del nodo donde quedo.** No es un error del reparto (el paso se copio bien, entero
y textual): es que el paso bien copiado **cayo en el nodo equivocado**, porque la
frontera que lo puso ahi era la unica publicada y no partia donde el objeto cambia.

> **ENTRA A LA COLA DEL OBJETO AJENO todo nodo donde una medicion declare material SANO,
> SIN REPETICION, pero AJENO AL OBJETO del nodo que lo contiene.** El disparador no es la
> repeticion (esa es la primera puerta): es la LECTURA que encuentra un tramo cuyo objeto
> no es el del resto del nodo.

**LA CURA ES DESTEJIDO ORDINARIO POR `P.18`, COMO OPERACION NUEVA DE LA FASE QUE
CORRESPONDA, NUNCA PODA.** El tramo ajeno se separa como cualquier bloque apendice: al
miembro cuyo objeto coincida, o a nodo propio si ninguno coincide. **No se descarta**: es
material sano, solo esta en el sitio equivocado.

**CADA ENTRADA LLEVA NODO, TRAMO Y LA LECTURA QUE LO HALLO.** Los tres ejemplares que la
midieron, entrando ya con esta puerta:

| nodo | tramo ajeno | la lectura que lo hallo |
|---|---|---|
| `producto_como_servicio_de_acceso` | **pasos 7 y 8** | las tres interfaces de usuario son de la parte de SISTEMAS de Hugos (`01_FUENTES.md`, vuelta 27), y el ultimo mira el modelo desde la economia circular: ninguno de los dos es el objeto del nodo, *reformular el producto como acceso en vez de propiedad* |
| `evaluacion_balanceada_de_ejecutivos` | **pasos 5 a 11**, de `actualizacion_posiciones_existentes` | el bloque trae dos actos: la conversacion de la degradacion (5 a 11) y la evaluacion del ejecutivo (12 a 19); solo el segundo calza con el objeto del miembro. La frontera publicada era UNA y no partia ahi (acta de la vuelta 29, discutible d1) |
| `contratar_por_fortaleza` | **pasos 6 a 8**, de `contratacion_experiencia_vs_potencial` | el paso 5 es literal al objeto del miembro; los pasos 6 a 8, promover de adentro contra traer de afuera, son otro objeto que viaja arrimado (acta de la vuelta 29, discutible d11) |
| `decision_de_vender_startup` | **paso 15 del resultado fundido**, *ajusta tu salario como CEO a valores de mercado una vez que tu empresa se convierta en un negocio real y consolidado, y en un objetivo atractivo de adquisicion* | **CUARTA ENTRADA, 14 ago 2026 (vuelta 30), y la primera que entra por una FUSION y no por un reparto.** Los origenes 27 y 32 decian lo mismo dos veces y `P.19` los fundio en un paso; **fundido y sano, su objeto sigue sin ser el del nodo**, que es *decidir si vendes tu empresa* (su entregable, medido hoy: *un analisis de escenarios que compare el valor esperado de vender ahora contra seguir operando, incluyendo tu punto de inflexion de control*). **La compensacion del CEO no es esa decision**: es una consecuencia de que la empresa se volvio un objetivo de adquisicion, y ninguno de los otros catorce pasos del resultado la toca. **Se declara y NO se poda**, que es la letra de esta puerta |

> **Y LA COMPROBACION DE QUE ESTA PUERTA SE USO: al cerrar, ningun tramo declarado como
> ajeno sigue viviendo dentro del nodo que la lectura senalo.** Si uno sigue ahi, es que
> el destejido no se ejecuto.

**ESTADO DE LAS CUATRO ENTRADAS, medido el 14 ago 2026 al cerrar la vuelta 30:** las
**CUATRO siguen dentro de su nodo**, y eso **no es un rojo de esta comprobacion todavia**:
la cura que esta misma pagina escribe es *destejido ordinario por `P.18`, COMO OPERACION
NUEVA DE LA FASE QUE CORRESPONDA*, y esas operaciones son de la **fase 02**, que la vuelta
30 abre y no cierra. **La comprobacion vence cuando la fase 02 cierre, no antes**, y se
escribe aqui para que ese vencimiento tenga fecha en vez de quedar al recuerdo.

**Y UNA DIFERENCIA ENTRE LAS DOS PUERTAS QUE LA VUELTA 30 MIDIO, dicha porque la letra no
la traia:** la primera puerta (repeticion) **la cierra la propia fase 01 cuando `P.19`
aplica**, porque fundir mata la repeticion en el acto; la segunda (objeto ajeno) **no la
puede cerrar la fase 01**, porque separar un tramo sano hacia otro nodo es una operacion de
destejido con destino, y esa es de la fase 02. **Por eso la cuarta entrada nace declarada y
no resuelta, aunque la vuelta que la hallo tuviera el instrumento para cortarla.**

---

## EL ERROR DE DEJAR PASAR, **YA TIENE TASA MEDIDA**

**Era la linea que le faltaba a esta pagina.** Todo lo que se verifica aqui vigila **el
error de fundir de mas**: las A se releen, se simulan, se recomputan y se corrigen.

> **EL ERROR CONTRARIO, cuantas D eran en realidad A o B, NO TENIA CIFRA.** Y sin esa
> cifra, **la tasa de A del cribado no tenia banda por abajo.**

| | |
|---|---|
| **la cifra** | **23 de 24 sostienen su D: 95,8%** |
| **el intervalo** | **Wilson al 95%: entre 79,8% y 99,3%** |
| **el error de dejar pasar** | **4,2%**, banda **de 0,7% a 20,2%** |
| **proyeccion sobre las 1.621 D** | **unas 68**, banda de **14 a 333** |
| **fecha de corte** | **12 ago 2026, archivo al puesto 2.117** |
| **metodo** | **muestra pineada y estratificada, leida A CIEGAS.** Pin en `PIN_MUESTRA_D.txt`, semilla 20260812, instrumento `scripts/plan/muestra_d.py` |
| **el detalle** | [`CONTROL_MUESTRA_D.md`](CONTROL_MUESTRA_D.md) |

**Y LO UNICO QUE CAYO NO CAYO POR ERROR DE LECTURA: cayo por una regla que se escribio
DESPUES.** `P.11` es del 12 ago 2026 y el veredicto es del puesto 2.078. **Eso es
DERIVA MEDIDA DE LA DOCTRINA, y se cuenta aparte.**

### LO QUE ESTA LINEA OBLIGA A PARTIR DE HOY

| | |
|---|---|
| **1** | **toda tasa de A que se publique lleva esta banda al lado**, o se esta publicando media cifra |
| **2** | **el control se repite despues del recomputo**, con la misma semilla y el mismo metodo, para ver si la deriva creció |
| **3** | **si la banda hay que estrecharla, son unas cien lecturas**, y **eso es una decision de alcance del fundador** |

> **Y LA REGLA DE LECTURA QUE ESTE CONTROL DEJA, porque el propio control la aprendio:
> UNA MUESTRA QUE SOLO ENCUENTRA FALLOS AJENOS NO ES UNA MUESTRA.** En una de las
> veinticuatro **el archivo tenia razon y el relector no**, y **eso esta escrito con su
> puesto**.
