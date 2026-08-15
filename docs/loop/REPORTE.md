# REPORTE DE LA VUELTA 34 (ejecutor Opus 5). FASE III, rama `pasada-unica`

**LAS TRES DECISIONES DEL FUNDADOR ESTAN APLICADAS, LA CAIDA `6.1` DE LA VUELTA 33 ESTA CERRADA
CON `23 DE 23` ESTABLE, Y `OP-D-03` DEJO DE ESTAR PARADA. Pero no la desbloqueo el instrumento
recalibrado, que sigue sin pasar su propia puerta: la desbloqueo UNA CAIDA DE REPORTE DE LA VUELTA
33 que este reporte corrige. Dos de las tres costuras que la operacion declara ya estaban
consumidas por la fase 01, la tercera se destejio, los quince pares del acto estan leidos y el
acto resulto no ser una familia de seis sino DOS familias cerradas.**

- **Hash de partida:** `270ef4ea` (el commit del fundador con la decision).
- **Hash final:** `801c59f9`. **CINCO commits**, el primero de ellos la **APERTURA** medida antes
  de tocar nada y commiteada antes de tocar nada (`a25d21f5`). **Cinco contando la apertura, y se
  dice asi a proposito: el acta 33 conto una caida de reporte del ejecutor por esa misma cuenta.**
- **Rutas tocadas** (`git diff --stat a25d21f5..HEAD`, corrido hoy): **83 ficheros, 6.016
  insertadas, 154 borradas**. Por carpeta: `docs/loop` **49**, `scripts/loop` **14**, `docs/plan`
  **6**, `dataset/nodos` **4**, `web/lib` **2**, `dataset/metadata` **2**, y **seis ficheros
  sueltos** (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `docs/INTRA_DOMINIO_INFORME.md`,
  `docs/PENDIENTES.md`, `scripts/run_phase1.py`, `scripts/costuras_internas.py`,
  `engine/test_gate_deprecado_reciproco.py`). **Cero merges.** El hook corrio verde en los cinco.
- **`dataset/nodos` son CUATRO ficheros y ninguno mas:** `ab_testing_optimizacion` (el destejido) y
  `homework_frontend_loading`, `procesamiento_paralelo_con_espirales`, `ventaja_competitiva_producto`
  (la redireccion rehecha). **Ningun nodo nacio, ninguno murio, ninguno se borro.**

---

## 1. EL ESTADO, APERTURA CONTRA CIERRE

**Las dos columnas son de dos corridas del MISMO instrumento** (`scripts/loop/vuelta31_estado.py`,
el que abrio y cerro la vuelta 33, **sin tocarlo**): la de **APERTURA** corrida **antes de la
primera operacion** y commiteada antes de tocar nada (`a25d21f5`, salida
`SALIDA_V34_APERTURA.txt`), y la de **CIERRE** corrida **al cerrar** (`SALIDA_V34_CIERRE.txt`).
Ninguna cifra viene de un acta ni de un reporte anterior.

| | **APERTURA** | **CIERRE** |
|---|---:|---:|
| marcador: n / A / B / C / D | 3.388 / 582 / 84 / 8 / 2.714 | **3.388 / 581 / 83 / 8 / 2.716** |
| huecos / duplicados / clases fuera de ABCD | 0 / 0 / 0 | **0 / 0 / 0** |
| grafo: ficheros / ids / vivos / deprecados | 3.853 / 3.853 / 3.538 / 315 | **identicos** |
| enlaces / claves distintas | 16.852 / 15 | **16.849 / 15** |
| familias Weinberg / Horowitz / Hugos / Coleman / Rackham (vivos) | 72 / 93 / 111 / 75 / 47 | **identicas** |
| operaciones / estados / dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| inventario | 672 | **672** |
| indice rojo declarado | 18 lineas, 0 ausentes | **18 lineas, 0 ausentes** |
| fronteras de `OP-F-04-COL` | 14 de 15 | **14 de 15** |
| **congelados de `OP-D-03`** | **2** (738, 1061) | **0** |

> **EL MARCADOR SE MOVIO UNA VEZ, y con la cifra esperada escrita ANTES de correr el
> instrumento**, con orden de PARAR si daba otra cosa (`SALIDA_V34_LOTE.txt`). **Dio exactamente
> lo escrito.** `n` **no se movio**: las siete lecturas dirigidas nuevas **no entran en la cola**.

> **LOS TRES ENLACES DE MENOS SON LA REDIRECCION REHECHA, y nada mas.** 16.852 a **16.849**: los
> tres sitios vivos de los que se quito el id del absorbido de `OP-D-02`. **Ninguna arista se
> escribio a mano en esta vuelta**, y el paso 5 del `Gate 0` reporta **0 nodos actualizados**
> despues, que es la prueba de que ya no las devuelve.

> **La tasa por dominio se movio SOLO en `core`**, porque los dos veredictos volteados son los dos
> de `core`: de `A 343, B 82, C 8, D 1.012` a **`A 342, B 81, C 8, D 1.014`**. **Los otros nueve
> dominios, identicos al digito** (`SALIDA_V34_TASA_DOMINIO.txt`). **La tasa redondeada NO se
> mueve (23,7 % las dos veces) y la cifra SI**, y va dicho para que nadie lea el 23,7 como *no
> paso nada*: 343 de 1.445 es 23,74 y 342 es 23,67. **La vara por tramo es cifra del cribado y
> esta vuelta no leyo ningun par de la cola: no se mueve, y no se copia de ningun lado.**

---

## 2. DECISION 1 APLICADA: **el deprecado es archivo tambien en el reciprocado**

**El cambio es UNA regla en DOS funciones.** Nace `aristas_a_simetrizar(nodes)` en
`scripts/run_phase1.py`, **funcion pura** como las tres barandas del alias: **entra la arista que
declara un nodo VIVO**, en cualquiera de sus dos vistas. `step5_symmetrize` y
`count_asymmetric_edges` **leen las dos la misma funcion**, porque un Gate que exigiera simetria
en aristas que el paso 5 ya no simetriza **se pondria rojo por su propia politica**, y la salida
barata seria aflojar la comprobacion.

**LA LECTURA ES POR DECLARACION, NO POR ORIGEN TOPOLOGICO**, y la diferencia decide: por origen,
una arista declarada por un vivo **hacia** un deprecado seguiria escribiendo el id del muerto
dentro del vivo, que es el sintoma exacto que la decision manda cerrar.

**MEDIDO ANTES DE TOCAR CODIGO** (`vuelta34_reciprocado.py`, sobre `dataset/nodos`): **110**
aristas con su unica declaracion en un deprecado, **las 110 de deprecado a deprecado**, **0**
tocando a un vivo. **Eso ultimo no es que no hubiera problema: es que el Gate ya se las habia
devuelto**, y por eso el censo se corre y se publica en vez de suponerse.

| medicion | resultado |
|---|---|
| **caso positivo EN ROJO y EN VERDE** (`engine/test_gate_deprecado_reciproco.py`, cinco pruebas) | la **regla vieja** (copiada literal dentro de la prueba) devuelve **2 aristas** del muerto a los vivos; la **nueva**, **ninguna**. **La prueba EXIGE que la vieja falle** |
| redireccion rehecha (`vuelta34_redirigir.py`, seis guardas) | **3 sitios vivos**, **0** que sigan nombrando al absorbido; cableado del archivo **intacto** y sus **5 pasos** sin tocar |
| **caso positivo de `OP-D-02` ANTES** | **22 PASAN, 1 CAE** (el mismo rojo que la vuelta 33 publico) |
| `Gate 0`, **paso 5** | **0 nodos actualizados, 0 vistas completadas** |
| **caso positivo DESPUES del ciclo entero de `Gate 0`** | **23 PASAN, 0 CAEN**. **Es la cifra que prueba estabilidad, porque se mide donde la otra caia** |

**Ciclo de `Gate 0` entero:** comando 1 **exit 0**, `GATE 0: OK`, **20 `[OK]` y 0 `[FALLO]`**;
comando 2, **71 etiquetas**; comando 3, verde, las dos copias con **0 divergentes**. **Suites:
motor 25 de 25** (el fixture nuevo es el 25), **web 80 ficheros con 1.030 pasadas y 3 saltadas**,
**`tsc` cero lineas**. Correccion declarada **dentro del plan sellado**, con la cifra vieja de
22 de 23 escrita dentro.

---

## 3. DECISION 2 APLICADA: **el instrumento de costuras, recalibrado a la letra. Y SIGUE SIN PASAR SU PUERTA**

**Se aplico exactamente lo que la letra dice:** `MIN_BLOQUE` de 3 a **2** (senal para todo nodo de
**cuatro** pasos o mas); por debajo, **`NO APLICA` EXPLICITO**, que es un objeto que **revienta si
alguien lo compara con un umbral** en vez de un cero silencioso; **recalibracion declarada en el
docstring con los ids y las cifras de hoy**, con el texto viejo entero al lado; y **la puerta de
calibracion mudada a las senales**.

**LA PUERTA HEREDADA, PROBADA CONTRA EL CULPABLE.** `scripts/loop/vuelta32_costura_opd01.py`, el
script que publico la cifra mala importando por debajo de la puerta vieja, **hoy MUERE al llamar a
la senal**: `CalibracionRota: INSTRUMENTO MAL CALIBRADO: plan_mejora_procesos`
(`SALIDA_V34_PUERTA_HEREDADA.txt`). **El pendiente de doctrina 3 queda cerrado en el codigo, no en
una nota.**

**Y LO QUE LA RECALIBRACION NO ARREGLA, medido ANTES de aplicar nada y publicado sin maquillar**
(`vuelta34_calibrar_costuras.py`, `SALIDA_V34_CALIBRACION.txt`):

| | resultado |
|---|---|
| **la puerta sigue ROJA**, ahora por UNO y no por dos | `plan_mejora_procesos` da **43,1** contra 44. **Se queda fuera por 0,9 puntos**, que es exactamente la distancia del falso negativo que en su dia bajo el umbral de 45 a 44 |
| **el costo** | la cola pasaria de **122 a 1.497** nodos, el **42,3 por ciento** del catalogo |
| **la causa del costo** | `MIN_BLOQUE` **no es un solo dial**: tambien es la K del promedio de las K mejores, asi que promediar DOS en vez de TRES sube el puntaje de todo el catalogo con el umbral quieto. **El p50 de la senal nueva es 45,8: el umbral quedo POR DEBAJO DE LA MEDIANA** |

> **Con 24 por ciento esta casa ya adjudico que una baranda asi esta rota. Con 42,3 tampoco.** Que
> umbral acompana a `MIN_BLOQUE = 2`, o contra que nodos se recalibra la puerta, **es doctrina de
> medicion y NO la invento yo**: va como **pendiente de doctrina 1**.

**RECOMPUTO DEL APOYO DEL MOVIMIENTO 2 DE `OP-D-01`, con el nodo impreso ENTERO delante**
(`vuelta34_mov2.py`):

| pata | vuelta 32 | medido hoy |
|---|---|---|
| senal 1, pareja | **51,2** contra 80 | **51,2. SE REPRODUCE AL DIGITO** y sigue sin disparar |
| senal 2, bloque | **0,0** contra 44 | con la regla nueva, **45,8 con corte tras el 5. DISPARA** |
| **lectura del nodo entero** | (no se publico) | **NO hay costura**: los pasos 6 y 7 son la continuacion, no un reinicio |

**La pata instrumental queda EN SUSPENSO, no volteada**, y el motivo es una cifra: **45,8 es
exactamente la mediana del catalogo con la regla nueva.** Y **la causa del `0,0` no era la que se
dijo**: el reporte de la vuelta 33 la atribuyo al **rango vacio**, que vale para los nodos de
cinco pasos pero **no para este, que tiene siete**; medida hoy corte por corte, **el
emparejamiento monotono lograba UNO donde el promedio exigia TRES**. **Dos averias con el mismo
sintoma.**

---

## 4. **LA CAIDA DE REPORTE DE LA VUELTA 33 QUE DESBLOQUEO `OP-D-03`**

**El MOTIVO 2 de la parada decia:** *la nomina de esas tres no esta escrita en ninguna parte por
su nombre: sale del instrumento*. **ESTA ESCRITA, en el mismo documento y ochenta lineas mas abajo
del propio motivo**, desde la primera entrega del plan (`23f9ac32`, medido hoy con `git log -L`):

```
**Acto 2. SEIS nodos y TRES destejidos.** Costuras: `ab_testing_optimizacion`,
`optimizacion_embudo_get_customers`, `split_testing_experimentos_ab`.
```

**Y la cita ya no depende de que alguien la recuerde:** `vuelta34_costuras_opd03.py` **aborta si
esa linea no esta en el documento o si le falta uno de los tres nombres.**

**MEDIDAS LAS TRES, DOS YA ESTABAN CONSUMIDAS POR LA FASE 01**, igual que le paso al paso 1 de
`OP-D-02`, y cada una con su huella medida en el nodo de hoy:

| costura declarada | frontera escrita | pasos hoy | huella del bloque | estado |
|---|---|---:|---|---|
| `optimizacion_embudo_get_customers` | 1 a 5 / 6 a 10 sobre 10 | **5** | *middle ring testing*: **ya no esta** | **CONSUMIDA** por `OP-F-04-WEI` |
| `split_testing_experimentos_ab` | 1 a 5 / 6 a 9 sobre 9 | **5** | *cambio porcentual*: **ya no esta** | **CONSUMIDA** por `OP-F-04-RAC` |
| `ab_testing_optimizacion` | 1 a 10 / 11 a 15 sobre 15 | **10** | *punto de saturacion*: **ya no esta** | **EN PIE** |

**EL `preservar` DE LA OPERACION, COMPROBADO DONDE VIVE HOY y no dado por bueno:** la
significancia del 95 por ciento en `split_testing`; el **cambio porcentual** y el **grupo de
control de desempeno inicial similar** en `metodologia_evaluacion_entrenamiento_ventas`. **Los
tres, en UN solo nodo vivo cada uno.**

---

## 5. EL DESTEJIDO: **`ab_testing_optimizacion`, de DIEZ pasos a CINCO**

**Su frontera tampoco se adivina:** la escribio la tabla de fronteras de `OP-F-04-WEI` en
`01_FUENTES.md` linea 947. **El criterio del superviviente es el de `OP-D-01`, citado y no
inventado** (de cada grupo sobrevive el de indice mas bajo), y cae entero sobre el bloque **1 a
5**, que es **la narracion del unico libro que el nodo declara como fuente**.

| guarda | resultado |
|---|---|
| las **siete** guardas del constructor, escritas para caer | **7 de 7 verdes** |
| simulacion previa sobre copia en memoria (`P.7`) | **verde** |
| guarda de texto sobre TODOS los pasos | **10 de 10** calzan con su prefijo sellado |
| cero perdida, cobertura exacta | **10 de 10** origenes, sin huecos ni repetidos |
| **caso positivo ANTES** | **0 PASAN, 7 CAEN** |
| **caso positivo DESPUES** | **7 PASAN, 0 CAEN** |
| conservacion (aparte) | **17 rastros vivos de 17** |
| fuente / censo | **sin cambio** / **3.853 ficheros** |

**Ciclo de `Gate 0` entero: exit 0, `GATE 0: OK`, 20 `[OK]` y 0 `[FALLO]`; motor 25 de 25, web
1.030 pasadas, `tsc` cero lineas.** El **comando 4 NO se corre y se dice por que: el censo no
cambia**, y su vara (`readiness.test.ts`) queda verde en la suite. **La tabla del mapa esta
IMPRESA desde el plan sellado**, con el comando citado al lado.

> **LO QUE LA SENAL RECALIBRADA DICE DE ESTE NODO, y mide al instrumento y no al destejido:** su
> mejor corte es **tras el paso 8 con 49,5**, y **en el corte de la frontera escrita (tras el 5)
> da 42,1, POR DEBAJO DE SU PROPIO UMBRAL**. El docstring presume de *acertar el corte exacto*;
> **sobre esta costura no lo acierta**. Y dispara en **4 de los 6** nodos del acto, **incluidos
> DOS que el plan declara SANOS**.

---

## 6. **EL VERIFICADOR DE MAPAS ENSENO UN HUECO PROPIO**, y salio porque se probo en rojo

**Ensucie a proposito una celda de la tabla nueva** (meter el origen **4** en el grupo del paso 1)
**y el instrumento siguio imprimiendo `0 discrepancias` y exit 0.** La causa esta en su `main()`:
**la `vara 2` corre SOLO `if args.jsons`**, o sea solo si quien lo invoca se acuerda de pasar
`--json`.

> **Y eso alcanza a un verde ya publicado:** el *2 tablas, 12 filas, 0 discrepancias* de la vuelta
> 33 **se corrio sin `--json`**. **La cifra era cierta y la vara 1 corrio de verdad; lo que no
> corrio fue la vara 2.**

**QUE SE ARREGLA: el silencio.** La salida **nombra las dos varas y dice cual corrio**, y sin
`--json` escribe que *este resultado mide solo la vara 1*. **NO se le pone descubrimiento
automatico de planes**, porque hay planes sellados **sin tabla en el documento** y eso daria un
**rojo falso**, que es peor que un verde parcial anunciado. **Con los tres planes y la celda
sucia: exit 1, 2 discrepancias. Restaurada: exit 0, 3 tablas, 17 filas, LAS DOS VARAS CORRIDAS.**

---

## 7. EL PASO 3 DEL ORDEN INTERNO: **738 y 1061 releidos y volcados**

**Con la cifra esperada escrita ANTES de correr el instrumento y orden de parar si daba otra cosa.
Dio exactamente lo escrito.**

| puesto | antes | ahora | por que |
|---:|:---:|:---:|---|
| **738** | `B` | **`D`** | cayo el TOQUE UNICO: **los dos nodos estaban averiados y hoy ninguno tiene juntura**. Uno optimiza una pagina, el otro decide **si una funcionalidad merece existir** |
| **1061** | `A` | **`D`** | **la prediccion de su propia razon acerto al pie de la letra**: el destejido dejo a la madre con el A/B en UNA linea y al otro como su procedimiento entero |

**La razon vieja se copia del archivo POR MAQUINA en las dos** (1.128 y 1.241 caracteres) **y el
script aborta si no queda literal dentro de la nueva.**

**EL BARRIDO DEL `9.10` EN EL MISMO ACTO**, con instrumento **sucesor declarado** (cambian las
cifras del marcador viejo, no la maquinaria): **65 candidatos listados sin ocultar ninguno**.
Corregidos `INTRA_DOMINIO_INFORME` (marcador con **tres** tachados, tasa por dominio, total de A),
`PENDIENTES` (congelados **7 a 6**, cola **13 a 12**), `RECOMPUTO_3388` (**siete celdas** con su
cifra vieja tachada dentro) y `02_DESTEJIDOS`.

> **Y EL RECOMPUTO SE VOLVIO A CORRER ENTERO. Su cifra pide explicacion y se da:** los actos
> **SUBEN de 334 a 335** y las cerradas **de 279 a 281 QUITANDO una `A`**. **No es
> contradiccion:** el 1061 era la arista que cosia dos mitades, y al caer **la componente se parte
> en dos, las dos CERRADAS**. Retrato 581 a **580**, nodos con A **quietos en 851**, abiertas 55 a
> **54** y de 253 a **247** nodos. **Las cuatro comprobaciones, OK.**

---

## 8. LAS SIETE LECTURAS DIRIGIDAS `LD-75` a `LD-81`, y la respuesta de `P.5`

**EL RELOJ DE `P.5` ES UNA GUARDA DE CODIGO, no una promesa:** el instrumento **aborta antes de
imprimir nada** si el destejido no esta hecho. **Los seis nodos impresos ENTEROS antes de decidir,
las aristas buscadas en los DOS sentidos, y ninguno de los siete pares esta en la cola: `n` no se
movio.** El numero de partida (**75**) **se midio sobre `docs/` entero**, no se recordo.

**Las siete `D`.** Una con el enlace ya puesto (`LD-75`), **tres con `ARISTA QUE FALTA`**
(`LD-76`, `LD-79`, `LD-80`) declaradas para la fase 04, y **tres sin arista con su motivo
escrito** (`LD-77`, `LD-78`, `LD-81`).

> **LA RESPUESTA DE `P.5`: el acto NO es una familia de seis. Son DOS FAMILIAS CERRADAS**, una de
> cuatro (`ab_testing_optimizacion`, `split_testing`, `test_ab_precio`,
> `split_testing_experimentos_ab`) y una de dos (`funnel_get_customers_optimizacion`,
> `optimizacion_embudo_get_customers`), **y el 1061 era el unico hilo que las cosia**. **Lo
> confirma el instrumento de la casa, no mi dibujo.**

**LO QUE ESTA VUELTA NO TOMA, y se dice:** el **paso 2** del orden interno (decidir sobre los
seis, o sea la fusion). **El campo `superviviente` sigue en `null` a proposito.**

---

## 9. TAREA 1.4: el criterio de la `ARISTA QUE FALTA`, escrito UNA vez

Va **bajo la tabla que junta a los tres** (724, 755, 827) y **no dentro de cada razon**: escribirlo
tres veces seria escribirlo tres veces distintas. **La vara es el TAMANO de lo compartido: se
declara donde es un BLOQUE que uno expande de una LINEA del otro; no se declara donde es LINEA
contra LINEA y los dos tienen cableado propio denso.**

> **Y UNA PRECISION QUE EL ENUNCIADO DEL ENCARGO NO CUBRE, dicha en vez de forzar el calce:** el
> encargo lo escribio como *madre e hijo del `9.6.2`* contra *linea contra linea*. **Eso nombra
> los dos extremos (el 724 y el 827) y deja fuera al 755**, que **no tiene madre e hijo** y sin
> embargo **lleva arista**. **Madre e hijo es UN CASO de bloque compartido, el mas nitido, no la
> condicion.**

---

## 10. INSTRUMENTOS NUEVOS Y CORREGIDOS, todos con su motivo dentro

| instrumento | que es | el motivo |
|---|---|---|
| `scripts/run_phase1.py` | **CORREGIDO**, funcion pura `aristas_a_simetrizar` | la decision 1, con las dos funciones leyendo la misma regla |
| `engine/test_gate_deprecado_reciproco.py` | **NUEVO**, entra a la suite (24 a **25**) | guarda la regla **en rojo y en verde**, con la regla vieja dentro |
| `scripts/costuras_internas.py` | **RECALIBRADO** | la decision 2 entera: `MIN_BLOQUE`, `NO APLICA` explicito, puerta en las senales |
| `vuelta34_reciprocado.py` | **NUEVO**, solo lectura | el censo del cableado del deprecado **antes** de tocar codigo |
| `vuelta34_redirigir.py` | **NUEVO** | rehace la redireccion con **seis guardas**; no toca texto de nodo |
| `vuelta34_declarar_plan.py` | **NUEVO** | la correccion declarada dentro del plan sellado |
| `vuelta34_calibrar_costuras.py` | **NUEVO**, solo lectura | mide el **costo** de la recalibracion antes de aplicarla |
| `vuelta34_mov2.py` | **NUEVO**, solo lectura | el recomputo del apoyo del acta 32, **corte por corte**, con el nodo entero |
| `vuelta34_leer_opd03.py` / `vuelta34_ld_opd03.py` | **NUEVOS**, solo lectura | los nodos enteros y el **reloj de `P.5`** como guarda |
| `vuelta34_costuras_opd03.py` | **NUEVO**, solo lectura | **aborta** si la nomina de las tres no esta citable en el plan |
| `vuelta34_plan_opd03.py` | **NUEVO**, constructor | **siete guardas**, los textos leidos del grafo |
| `vuelta34_volcado_910.py` / `vuelta34_barrido_910.py` | **NUEVOS**, sucesores declarados | la razon vieja copiada por maquina; el barrido con las cifras de hoy |
| `verificar_mapas_destejido.py` | **CORREGIDO** | **dice que varas corrio**; el verde parcial deja de ser mudo |

---

## 11. CORRECCIONES DECLARADAS DE ESTA VUELTA

1. **La caida `6.1` de la vuelta 33**, cerrada con el instrumento cambiado y **23 de 23 estable**,
   con la cifra vieja de 22 de 23 escrita dentro del plan sellado.
2. **La cifra de bloque del movimiento 2 de `OP-D-01`** (0,0 contra 44), **recomputada**: hoy da
   45,8 y **dispara**, y por eso la pata instrumental queda **en suspenso, no volteada**.
3. **La causa que la vuelta 33 le atribuyo a ese 0,0**: no era el rango vacio, era el
   emparejamiento monotono. **Dos averias con el mismo sintoma.**
4. **El MOTIVO 2 de la parada de la vuelta 33**: la nomina de las tres costuras **si estaba
   escrita**, y en el mismo documento.
5. **El verde del verificador de mapas de la vuelta 33**: midio **una** de sus dos varas.
6. **La cifra del recuadro *lo que queda medido y aprovechable*** de `OP-D-03` (siete `A` y un
   congelado): hoy son **seis `A` y cero congelados**.
7. **El marcador y sus tablas derivadas**, con el recomputo re corrido entero.
8. **El enunciado del criterio de la arista que falta**, que nombraba dos extremos y dejaba fuera
   el caso de en medio.

---

## 12. PENDIENTES DE DOCTRINA

1. **NUEVO Y ES EL MAS CARO: que umbral acompana a `MIN_BLOQUE = 2`.** La recalibracion aplicada a
   la letra **deja la puerta roja por 0,9 puntos** y **llevaria la cola al 42,3 por ciento del
   catalogo**. El propio instrumento tiene escrito que **una baranda que caza lo correcto esta
   rota**. **No lo decido yo.**
2. **NUEVO: contra que nodos se recalibra la puerta.** Los dos de la calibracion **fueron
   destejidos por esta misma campana**, asi que la calibracion historica **ya no es reproducible
   por construccion**. Ninguna pagina dice como se elige una calibracion nueva.
3. **NUEVO: la cola de relectura tras un DESTEJIDO.** El **452** y el **1575** se emitieron contra
   los **quince** pasos de `ab_testing_optimizacion` y hoy ese texto tiene **cinco**. Por el `9.4`
   deberian releerse; **el orden interno de la operacion solo nombraba al 738 y al 1061**. Van
   **declarados** aqui y **no releidos**, porque extender el alcance de un orden interno escrito
   es del fundador.
4. **NUEVO: un verificador que mide media vara si no le pasan un argumento.** Se arreglo el
   silencio, **no el diseno**: sigue siendo el operador quien tiene que acordarse del `--json`.
   Ninguna pagina dice que una guarda opcional sea guarda.
5. **CERRADO EN EL CODIGO (era el 3 de la vuelta 33):** la guarda que se salteaba importando por
   debajo. **La puerta vive ahora en las senales y el script culpable muere al llamarlas.**
6. **SIGUE VIVO (era el 4 de la vuelta 33):** hasta donde atras alcanza el barrido del `9.10`. Las
   filas de checkpoints cerrados **no se tocan** (adjudicado por el acta 33), y esta vuelta anadio
   **tres tachados** a las mismas celdas: **una celda con tres tachados es legible hoy y sera
   ilegible a los seis.**
7. **SIGUE VIVO:** los nodos propios de esta pasada **escritos sin acentos**, con cura escrita en
   `05_SANEO.md` linea 660 y sin numero de operacion.

---

## 13. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

| # | que | por que es discutible |
|---:|---|---|
| **d1** | **Leer *aristas que nacen en deprecados* como DECLARACION y no como origen topologico** | el fundador escribio *nacen en*, y **nacer en un nodo** se puede leer como *el nodo es el extremo `antes`*. **Lo sostengo con que la otra lectura no cierra el sintoma**, pero es una interpretacion mia de la letra |
| **d2** | **Que el chequeo de simetria del `Gate` deje de exigir 110 aristas** | es una guarda que se AFLOJA, y esta casa desconfia de eso con razon. Lo sostengo con que **exigir lo que el paso 5 ya no hace es un rojo por construccion**, pero un auditor puede decir que la simetria del archivo tambien importa |
| **d3** | **Aplicar `MIN_BLOQUE = 2` a los TRES sitios**, incluida la K del promedio | la letra dice *`MIN_BLOQUE` pasa a 2* y el constante vive en tres sitios. **Si la K se queda en 3, un nodo de cinco pasos NUNCA puntua**, asi que la senal para `n >= 4` no existiria. Es la unica lectura coherente que encontre, **pero es una lectura** |
| **d4** | **Ejecutar el destejido con la puerta del instrumento ROJA** | la nomina viene del plan sellado y no del instrumento, y eso lo sostengo. **Pero un auditor puede decir que destejer con el medidor descalibrado es exactamente lo que la parada queria impedir** |
| **d5** | **El grupo 1 del mapa: meter el paso 6 (la metrica) con el 1 y el 9** | la metrica **no es un elemento de la pagina**. Los junte porque el paso 1 ya nombra la metrica (*impulsan la activacion*) y el 6 la vuelve elegible. **La lectura contraria hace del 6 un paso propio y deja SEIS** |
| **d6** | **Llamar `DESTINO` al motivo del grupo 5** | *documentar los resultados* encaja en *que hacer con el resultado* y entra en el paso final, **pero tambien se puede leer como `ALCANCE`**, y ademas el inciso trae dos cosas y no una |
| **d7** | **El `738` leido `D` y no `A`** | **es el mas fuerte de la tanda.** El archivo llama `A` al 452 y al 374; **quien encadene esas dos dira que esta tambien lo es**. Lo separo por el objeto (la funcionalidad nueva no es un elemento de la pagina), pero es una cadena que no cierro |
| **d8** | **El `1061` leido `D`** | lo sostengo con la prediccion literal de su propia razon vieja, **que es el apoyo mas fuerte que se puede tener**. Pero **la prediccion la escribio la misma casa**, y un auditor puede decir que cumplir tu propia profecia no es medir |
| **d9** | **`LD-78` sin arista y `LD-76` con arista, desde el MISMO paso 5** | separo *el metodo de probar la variacion* de *otro objeto que usa el mismo metodo*. **Es el arreglo mas debil de la tanda** |
| **d10** | **Declarar TRES aristas que faltan en una sola tanda** | tres enlaces nuevos hacia dos hijos de la misma madre **puede ser exactamente el inflado que el propio criterio dice evitar** |
| **d11** | **Volcar el `738` y el `1061` en esta vuelta** | mueve una cifra publicada por la vuelta 33 el mismo dia. Lo sostengo con que **el orden interno de la operacion lo manda como su paso 3**, pero es la segunda vez en dos vueltas que el marcador se mueve |
| **d12** | **Dejar el `452` y el `1575` SIN releer** | los dos se emitieron contra un texto que hoy tiene la mitad de pasos. **Lo sostengo con que el orden interno nombra dos y no cuatro**, pero es una decision mia sobre el alcance de un plan escrito |
| **d13** | **Tocar TRES instrumentos en la misma vuelta** (`run_phase1`, `costuras_internas`, el verificador) | los tres por encargo o por hallazgo, y los tres declarados. **Pero es el patron que la vuelta 33 se marco a si misma en su `d15`, y aqui son tres y no dos** |
| **d14** | **Publicar la medicion de contraste de costuras con las senales REIMPLEMENTADAS** | es literalmente *importar por debajo de la puerta*, que es lo que el pendiente 3 castigaba. **Lo sostengo con que medir la propia descalibracion es lo unico que no se puede hacer con la puerta puesta**, y va dicho en cada linea de salida |
| **d15** | **Contar CINCO commits incluyendo la apertura** | la vuelta 33 recibio una caida de reporte por esta cuenta exacta. **Lo escribo como *cinco contando la apertura* a proposito**, pero si el auditor cuenta *commits de trabajo* dira que son cuatro |

---

## 14. PREGUNTAS

1. **Que umbral de bloque acompana a `MIN_BLOQUE = 2`?** Con 44, la puerta sigue roja por 0,9
   puntos y la cola se va al 42,3 por ciento. **Sin esa decision, el instrumento de costuras no
   vuelve a entregar.**
2. **Contra que nodos se recalibra la puerta**, si los dos historicos ya no son reproducibles
   porque esta campana los destejio?
3. **El `452` y el `1575` se releen?** Se emitieron contra los quince pasos de
   `ab_testing_optimizacion`. **Si la respuesta es si, el nucleo cerrado de cuatro puede dejar de
   serlo antes de la fusion.**
