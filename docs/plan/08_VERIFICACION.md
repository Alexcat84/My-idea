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
