# REPORTE DE LA VUELTA 67: EL LOTE C DEL TRAMO UNICO DE `OP-U-02`, UNA FUSION Y CINCO DECLARADOS, Y UN MOTIVO DE CIERRE QUE NINGUNA LETRA CUBRE

**Fase III, ejecucion continua. Rama `pasada-unica`. 25 ago 2026, y la vuelta cruza la
medianoche.**

**FECHA POR DOS RELOJES, CORRIDOS POR MI, Y NO CALZAN AL CERRAR: SE DICE EN VEZ DE ELEGIR UNA.** Al
ABRIR, los dos daban **2026-08-25** (reloj del sistema **23:20** y `git log -1 --date=short` sobre
`cc366861`). **Al CERRAR, el reloj del sistema da 2026-08-26 (00:03) y `git log -1 --date=short` da
2026-08-25**, porque **los TRES commits de trabajo de esta vuelta se escribieron el 25** (23:28,
23:49 y 23:56, leidos hoy con `git log --date=format`). **LA VUELTA SE FECHA EL 25 ago 2026**, que
es la fecha de sus commits y la de todas sus mediciones, **y el cruce de medianoche queda declarado
aqui** en vez de publicar una fecha unica que uno de los dos relojes desmiente.

---

## 1. LA CABECERA, TALLADA Y NO TECLEADA

**Generada entera con** `python scripts/loop/tallar_cabecera_reporte.py --vuelta 67` y **pegada sin
tocar una celda** ([`SALIDA_V67_CABECERA.txt`](SALIDA_V67_CABECERA.txt)). **La celda que no salga de
un instrumento no se escribe.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.247 / 606 / 17.540 | **3.853 / 3.243 / 610 / 17.555** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 315 / 236 | **551 / 319 / 232** |
| actos (componentes) | 75 | **74** |
| actos `CERRADOS` / `ABIERTOS` | 26 / 49 | **26 / 48** |
| nodos en `CERRADOS` / `ABIERTOS` | 61 / 212 | **61 / 207** |
| cola de costuras | 1.447 | **1.448** |
| colisiones de clase vigentes | 4 | **4** |
| auto-pares (los dos lados al mismo vivo) | 260 | **261** |
| duplicadas historicas: grupos / nodos | 915 / 725 | **914 / 724** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (273 igual a 273; 236 igual a 236) | **TODAS OK (268 igual a 268; 232 igual a 232)** |

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION** (regla 1): los seis instrumentos de apertura
corrieron con el arbol limpio en `cc366861`, **antes de escribir nada**, y **ninguno movio un fichero
rastreado** (`git status --porcelain` tras correrlos: solo las seis salidas nuevas, sin trackear).
**EL CIERRE SE RECOMPUTO AL CIERRE**, despues de que la fusion y `run_phase1` movieran el arbol.

**LA APERTURA DE HOY CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 66 PUBLICO**, y se dice porque es la
prueba de que entre las dos vueltas nadie movio dato: marcador, grafo, retrato, actos, cola,
colisiones, duplicadas y estado salen identicos a las cifras del acta (leidas hoy en
[`ACTA_AUDITOR.md`](ACTA_AUDITOR.md), seccion 1, lineas 17396 en adelante). **Los dos commits de
fundador que hay entre medias** (`eb91d502` y `51501552`) **tocan `orquestador.sh` y `AUDITOR.md`,
no el dataset.**

---

## 2. TAREA 1: EL REGISTRO DEL ACTA 66 (`+143` lineas, `0` borradas)

`python scripts/loop/vuelta67_registrar_acta66.py`
([`SALIDA_V67_REGISTRO_ACTA66.txt`](SALIDA_V67_REGISTRO_ACTA66.txt)), adosado al final de
[`../plan/03_FUSIONES.md`](../plan/03_FUSIONES.md) **sin reescribir ni una linea de arriba**
(`git diff --numstat`: **`143 0`**).

| guarda | resultado |
|---|---|
| **citas cotejadas antes de escribir** | **55** (39 del acta, 16 de la propia pagina), **MALAS 0** |
| **re-cotejo TRAS adosar** | **OK, 16 de 16**: las sedes de arriba siguen en su linea |
| **idempotencia** | **MUERDE**: la segunda corrida dice `YA ADOSADA` y no escribe |
| **guiones largos / medios** | **0 / 0** |

**Lo que queda registrado**, y es lo que el encargo pedia:

- **LOS DOCE DISCUTIBLES `A FAVOR`** con su vara citable y su linea, con **`D1` y `D4` marcados
  `POR EXTENSION`**.
- **LA ADJUDICACION DE `P.5` COMO TERCER MOTIVO SELLADO**, con **sus CUATRO letras copiadas** de sus
  lineas (17637, 17641, 17645 y 17648), y **LOS TRES MOTIVOS SELLABLES ESCRITOS JUNTOS** para que
  nadie tenga que reconstruirlos: el triangulo de `P.10`, la guarda `1B` y la respuesta *DOS
  FAMILIAS* de `P.5`.
- **LA ADJUDICACION DE LA COLISION CON DUENA**, con **la linea base del censo en `4`** y **las cuatro
  nombradas una a una**; y **la frase de la linea 4055 de esa pagina que decia *cuya linea base sigue
  en 2* queda declarada ENVEJECIDA y NO se tacha**, que es el carril del banco 9.10.
- **LA CAIDA DE PROCEDIMIENTO DEL ROL AUDITOR CON SU NOMBRE**: la sesion del 20 de agosto de 23:31 a
  23:39 que corrio ocho minutos de instrumentos y **termino sin escribir acta, encargo ni parada**,
  con **sus cinco dias de bucle parado** contados.
- **LAS DOS RACHAS** (reporte en cero por segunda tanda, clase o cifra en cero por undecima) y **los
  pendientes 3 y 4 con su destino**, el cierre de la fase 03.

**ESTA VUELTA NO TRAE CORRECCION DE FICHA Y SE DICE EN VEZ DE DEJARLO EN BLANCO:** el acta 66 **no
encargo ninguna**, y la unica que estaba encargada se escribio en la vuelta 66 y el auditor la leyo y
la dio por buena.

---

## 3. TAREA 2: EL LOTE C, DECLARADO AL ABRIRLO Y ENTREGADO ENTERO

**EL LOTE ES PREFIJO SIN SALTOS** del `orden_universo` de lo que quedaba del tramo fijado en
[`TRAMO_UNICO_OPU02_V64.jsonl`](TRAMO_UNICO_OPU02_V64.jsonl) (el lote A cerro los actos **1** y
**3**; el lote B cerro el **5**, **7**, **8**, **9**, **10** y **11**): **los actos 12, 13, 14, 15, 16
y 17. SEIS actos y 30 nodos**, **los seis cerrados ENTEROS**.

| acto | miembros | cierra | motivo sellado | superviviente |
|---:|---:|---|---|---|
| **12** | 5 | **`DECLARADO Y NO FUNDIDO`** | **un `D` DIRECTO sin triangulo**, y **no es ninguno de los tres**: PENDIENTE DE DOCTRINA | ninguno se elige |
| **13** | 5 | **`DECLARADO Y NO FUNDIDO`** | **guarda `1B`**, DOS puertas dentro | ninguno se elige |
| **14** | 5 | **`DECLARADO Y NO FUNDIDO`** | **`P.5`**, que contesta **NO ES UNA** | ninguno se elige |
| **15** | 5 | **`DECLARADO Y NO FUNDIDO`** | **guarda `1B`**, DOS puertas dentro | ninguno se elige |
| **16** | 5 | **FUNDIDO** | | `encuadre_desafio_diseno` |
| **17** | 5 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`** con su triangulo medido, **mas la `1B`** | ninguno se elige |

> **UN LOTE CON UNA SOLA FUSION SOBRE SEIS ACTOS, Y LA CIFRA VA PUBLICADA EN VEZ DE MAQUILLADA.** El
> contrato del lote es **PREFIJO CON TOPE, NO MINIMO** (acta 61, `D1`), y **lo que la lectura da es lo
> que se entrega**. **Va marcado discutible en la seccion 6** (`D5`).

### 3.1 **`P.5` CONTESTADA ACTO POR ACTO, SOBRE EL TEXTO ESTABLE**

**El acto se leyo ENTERO** con `python scripts/loop/dossier_del_tramo.py --tramo
docs/loop/TRAMO_UNICO_OPU02_V64.jsonl --actos 12,13,14,15,16,17`
([`SALIDA_V67_DOSSIER_LOTE_C.txt`](SALIDA_V67_DOSSIER_LOTE_C.txt), **705 lineas**), con **todos sus
pares internos y su razon entera**.

| acto | libro | pares `A` | pares `D` | puentes | triangulos | puertas | **una familia o dos** |
|---:|---|---:|---:|---:|---:|---:|---|
| **12** | Blank (los 5) | 5 | **1** | 0 | 0 | 0 | **UNA**, y el puesto **451** la nombra entera; **pero es MEZCLADA** y el `D` la detiene |
| **13** | Blank (los 5) | 8 | 0 | 0 | 0 | **2** | **UNA**, declarada por el archivo (racimo de SEIS); la detiene la guarda |
| **14** | Feld, Wasserman | 7 | 0 | 0 | 0 | 0 | **NO ES UNA. Hay un PURO DE CUATRO y un quinto que la lectura deja FUERA** |
| **15** | Rackham (los 5) | 5 | 0 | 0 | 0 | **2** | **NO SE CONTESTA HOY y se dice**: la guarda detiene antes y la pregunta no hace falta |
| **16** | IDEO y Brown | 4 | 0 | 0 | 0 | 0 | **UNA**, con las cuatro `A` encadenando a los cinco |
| **17** | Cooper (los 5) | 6 | **2** | **1** | **2** | **1** | `P.10` la detiene |

**MEDIDO** con `python scripts/loop/vuelta65_puentes_del_tramo.py --tramo ... --detalle`
([`SALIDA_V67_PUENTES_LOTE_C.txt`](SALIDA_V67_PUENTES_LOTE_C.txt)), **con los ids pasados por el
resolutor (`P.1`)**, y las puertas con `varas_n_arias_del_tramo.py` contra el universo protegido de
**256 ids**.

**Y EL TRAMO ENTERO SE MIDIO HOY, no se heredo del acta**
([`SALIDA_V67_PUENTES_TRAMO.txt`](SALIDA_V67_PUENTES_TRAMO.txt)): **47 actos mirados, 9 con al menos
un nodo puente**, y **de los 39 que quedaban al abrir esta vuelta, SEIS traian puente: los actos 17,
20, 21, 23, 24 y 27**, exactamente los que el acta 66 conto. **Cerrado el 17, quedan CINCO.**

### 3.2 **LAS VARAS POR FORMA, CON SU LETRA Y MEDIDAS POR INSTRUMENTO**

`python scripts/loop/varas_n_arias_del_tramo.py --tramo ... --actos 12,13,14,15,16,17`
([`SALIDA_V67_VARAS_N_ARIAS.txt`](SALIDA_V67_VARAS_N_ARIAS.txt)).

| acto | **FORMA medida** | a que lado apunta | **la letra que decide** |
|---:|---|---|---|
| **12** | `UNA SOLA VARA` | `metrics_that_matter_framework` (condiciones 4 contra 3; el cableado coincide, 14 contra 8) | **no llega a aplicarse: el `D` del puesto 1374 detiene ANTES** |
| **13** | `CONTENIDO EMPATA` | el cableado apuntaria a `hipotesis_de_canales` (8 contra 7), **que es puerta** | **no llega a aplicarse: la guarda `1B` prohibe absorber la SEGUNDA puerta** |
| **14** | `CONTENIDO EMPATA` | el cableado apunta a `tecnica_anclaje_negociacion` (7 contra 6), **que es el nodo que la lectura deja FUERA** | **no llega a aplicarse: `P.5` contesta NO ES UNA** |
| **15** | `TODAS DE ACUERDO` | `prevencion_objeciones_vs_manejo` (6 pasos contra 4, 3 condiciones contra 2, cableado 9 contra 4), **que es puerta** | **NO es choque de puerta**, porque las tres varas apuntan A LA PUERTA; la detiene la SEGUNDA puerta |
| **16** | `UNA SOLA VARA` | `encuadre_desafio_diseno` (pasos 5 contra 4; condiciones empatan en 2) | **funde a su lado**. **El cableado apunta al OTRO** (`how_might_we_briefs`, 8 contra 3) **y NO HABLA**, porque `P.8` es regla de PRELACION |
| **17** | `UNA SOLA VARA` | `seleccion_arenas_estrategicas` (condiciones 4 contra 3) | **no llega a aplicarse: `P.10` detiene, y la `1B` tambien** |

**EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN**, y **ninguna vara se teclea**: las tres cuentas por
miembro salen del instrumento.

### 3.3 **LA FUSION DEL `ACTO 16`, EN CIFRAS DEL INSTRUMENTO**

`python scripts/loop/fundir_por_plan.py --plan docs/loop/PLAN_V67_OPU02_LOTE_C.json --ejecutar`
([`SALIDA_V67_FUSION_LOTE_C.txt`](SALIDA_V67_FUSION_LOTE_C.txt)).

| | acto 16 |
|---|---:|
| absorbidos | 4 |
| pasos del superviviente | 5 a **10** |
| condiciones | 2 a **3** |
| piezas repartidas | 23 |
| de ellas `APPEND` / `CUBIERTO` / `INCISO` | 6 / 15 / **2** |
| perdidas selladas en campo propio | 9 |
| ficheros tocados | 21 |

**TOTAL: 4 nodos mueren (3.247 vivos a 3.243).**

**LAS GUARDAS DE LA OPERACION, LAS CUATRO Y TODAS VERDES:** guarda 1 (miembros vivos y nomina
completa), guarda **1B** (ningun absorbido es semilla ni extremo de puente), guarda 2 (cobertura
exacta de indices, cero olvidos) y guarda 3 (cero repetidos literales). **Los DOS `INCISO` se
EXTRAJERON del nodo y se comprobaron VERBATIM**, y sus dos pasos resultantes estan impresos en la
salida:

- al paso 1: *Formular el problema como una pregunta de diseño abierta, utilizando la fórmula
  '¿Cómo podríamos...?'*
- al paso 5: *Revisar y ajustar la pregunta original según lo aprendido, iterando la formulación con
  el equipo hasta encontrar el nivel de abstracción correcto*

**`P.16`, QUIEN FABRICA LIMPIA, EN EL MISMO COMMIT:** la fusion fabrico **2** duplicadas y **las
limpio en la misma corrida**; **guarda A** (cero auto-aristas nuevas) **OK**, **guarda B** (cero
duplicadas nuevas tras resolver) **OK**, **guarda C** (los campos que esta operacion no redacta,
intactos: **5 de 5**) y **guarda D** (los 4 absorbidos conservan su texto **INTACTO**) **OK**. El
pasivo del censo propio de la guarda **baja 1** (892 a 891) y **ni una duplicada ajena se toca de
mas**.

**`reanclar_por_resolutor.py` corrido ENTRE la fusion y `run_phase1`**
([`SALIDA_V67_REANCLAJE.txt`](SALIDA_V67_REANCLAJE.txt)): **1 referencia re-anclada, y esta vez NO
por vacio**. El rumbo `nucleo_quiero_algo_propio_sin_idea` apuntaba a `how_might_we_hmw` y pasa a
apuntar al superviviente. **En la vuelta 66 este instrumento no tuvo nada que hacer y se corrio
igual; hoy mordio.**

### 3.4 **EL DIFF DE DUPLICADAS, POR INSTRUMENTO Y CON LA APERTURA SACADA DE `git`**

`python scripts/loop/diff_duplicadas_por_resolutor.py --antes <git show d25ab668:...> --despues
docs/plan/ARISTAS_DUPLICADAS.jsonl`
([`SALIDA_V67_DIFF_DUPLICADAS.txt`](SALIDA_V67_DIFF_DUPLICADAS.txt)).

> **GRUPOS FABRICADOS DE VERDAD: `0`.** **RENOMBRADOS: `0`.** Hay **1 que DESAPARECE**
> (`encuadre_desafio_diseno` en `nodos_previos` hacia `search_for_business_model`), y **esta
> explicado**: era un grupo del absorbido `how_might_we_briefs` que la fusion deduplico al unir los
> `nodos_previos`. **915 grupos a 914.**

**LA AVERIA 7.3 DE LA VUELTA 66 NO SE REPITE:** el corte de *antes* se saco de **`git show`** sobre el
commit de la TAREA 1 (`d25ab668`), **anterior a la fusion**, y el de *despues* es el fichero **tras
recompilar**. **No se comparan dos cortes del mismo lado.**

### 3.5 **EL CENSO DE COLISIONES: ESPERADAS MEDIDAS ANTES DE FUNDIR SOBRE LA BASE `4`, Y CALZA**

**La cuenta esperada se midio ANTES, sobre el arbol de antes y simulando en memoria**, contra la
**linea base `4`** que el acta 66 adjudico (adjudicacion 2 del encargo):
`python scripts/loop/vuelta65_colisiones_esperadas.py --plan docs/loop/PLAN_V67_OPU02_LOTE_C.json
--base 4` ([`SALIDA_V67_COLISIONES_ESPERADAS.txt`](SALIDA_V67_COLISIONES_ESPERADAS.txt)).

| | |
|---|---:|
| linea base declarada **y MEDIDA sobre el arbol de antes** | **4** |
| **colisiones NUEVAS que la fusion fabricaria** | **0** |
| colisiones que desaparecerian | 0 |
| **ESPERADAS TRAS FUNDIR** | **4** |
| **MEDIDAS al cierre por el censo** | **4** |
| **`CALZA`** | **`SI`**, y son **LAS MISMAS CUATRO** |

**Las dos de la mesa `OP-M-03` no se tocan y las dos de `OP-U-02` siguen vigentes con su duena.**
**La guarda de la base MORDIO donde tenia que morder**: el instrumento **midio** la base sobre el
arbol antes de simular nada, y **si no hubiera calzado con la declarada habria caido en `ROJO` sin
escribir**.

**CORRECCION DECLARADA DE INSTRUMENTO** (banco 9.10, y va marcada discutible en el `D12`): el valor
por defecto de `--base` en `vuelta65_colisiones_esperadas.py` **pasa de `2` a `4`**, con **el texto
viejo verbatim y sin tachar** en el docstring y la nueva cita del acta 66. **La aritmetica no se
toca**: la guarda sigue **midiendo** la base y cayendo en `ROJO` si no calza.

### 3.6 **GATE 0 CON SU CICLO DE TRES, Y NO DE CUATRO**

| paso | resultado |
|---|---|
| `python scripts/run_phase1.py --reaplico-curaduria` | **`GATE 0: OK`**, todos los chequeos en `[OK]`; universo **3.243 activos / 610 deprecados**; alcanzabilidad **100,0 por ciento** |
| `python scripts/etiquetas_de_cara.py --aplicar` | **71 etiquetas** re-aplicadas |
| `python scripts/sync_assets_web.py` | **6 assets** mas `manifest.json` |
| **una cuarta corrida** | **NO SE HIZO** |

**LAS TRES SUITES, CORRIDAS POR MI:** motor **25/25**
([`SALIDA_V67_SUITE_MOTOR.txt`](SALIDA_V67_SUITE_MOTOR.txt)); web **80 ficheros, 1.030 pasadas, 3
saltadas** ([`SALIDA_V67_SUITE_WEB.txt`](SALIDA_V67_SUITE_WEB.txt)); `tsc --noEmit` **CERO lineas**
([`SALIDA_V67_TSC.txt`](SALIDA_V67_TSC.txt)). **Y el guardian de commit las volvio a correr en verde
en los tres commits de trabajo de esta vuelta.**

### 3.7 **EL REGISTRO EN `03_FUSIONES.md`** (`+410` lineas, `0` borradas)

`python scripts/loop/vuelta67_registro_lote_c.py`
([`SALIDA_V67_REGISTRO_LOTE_C.txt`](SALIDA_V67_REGISTRO_LOTE_C.txt)), **bajo la cabecera de tramo que
la vuelta 65 adoso** (linea **3732**, cotejada hoy) y **sin reescribir ni una linea de arriba**
(`git diff --numstat`: **`410 0`**).

**NINGUNA TABLA TECLEADA:** la del reparto pieza a pieza y la de piezas por absorbido **se generan
del plan sellado**; **las CINCO fichas de los declarados se generan del mismo plan**; la de perdidas
**se recorta de la salida del tallador leyendo la columna `acto` por su sitio en la cabecera**; y
**las 23 celdas** de guardas, colisiones, duplicadas y censos **se extraen por aguja**, con `ROJO` y
cero escrituras si una sola no se puede leer. **Citas cotejadas 11, MALAS 0** antes de escribir y
**11 de 11** despues. **Idempotencia MUERDE.**

**EL UNICO CAMBIO SOBRE LA MAQUINA COPIADA LITERAL DEL REGISTRADOR DE LA VUELTA 66, Y VA DICHO EN SU
DOCSTRING:** `tabla_declarado` **imprime ademas EL MOTIVO SELLADO** de cada cierre. Con **cinco**
declarados y **tres** motivos distintos, una tabla que no lo diga **obliga a leer la prosa para saber
por que cerro cada uno**.

---

## 4. LOS CINCO DECLARADOS, Y EL QUE NO TIENE LETRA

### 4.1 **EL `ACTO 12`: EL PRIMERO DE LA CAMPANA CERRADO POR UN `D` DIRECTO SIN TRIANGULO**

**`P.10` NO SE DISPARA AQUI, y se dice primero:** **cero nodos puente, cero triangulos**, medido. **Y
ningun miembro es puerta.** **Con `P.10` sola y con la guarda `1B` sola, este acto se fundiria** en
`metrics_that_matter_framework`.

**LO QUE LO DETIENE ES EL PUESTO 1374**, un veredicto `D` **DIRECTO** entre `cash_burn_calculation` y
`validacion_hipotesis_ingresos`, cuya razon dice que los dos parten del mismo dato, el ingreso neto
de canal, y **salen por puertas distintas**: *uno responde cuanto tiempo queda, el otro cuanto se
puede gastar en traer al siguiente cliente*. **Fundir los cinco a un superviviente unico deprecaria a
los dos contra el mismo vivo y sellaria que REPITEN ENTRE SI**, que es lo que ese veredicto niega.

**LA FAMILIA ES UNA Y AUN ASI NO SE FUNDE, Y LAS DOS COSAS SE DICEN JUNTAS:** el puesto **451**
enumera **los CINCO** por su nombre *sobre el mismo modelo financiero del fin de la validacion*, y el
**404** y el **807** la ven crecer. **Pero una familia con un `D` dentro es una familia MEZCLADA**,
que es el mismo nombre que el archivo usa en el puesto **863** cuando a la familia de la estrategia
de innovacion le entra su primer `D`. **FAMILIA NO ES FUSION.**

**LAS CUATRO LETRAS, cada una citable:** **1)** `P.10` cierra con que *LO QUE NUNCA ES SALIDA es
fundir la componente entera porque el cierre transitivo la junta*, y aqui los dos nodos del `D` solo
coinciden por el camino `cash_burn`, `metrics`, `verificar`, `validacion`: **la unica lectura DIRECTA
entre ellos es el `D`**. **2)** `P.12`: *el cierre transitivo convoca, la lectura decide*. **3)** el
**acto 5 de la vuelta 66** se declaro porque fundir sellaria identidades **que NADIE leyo**, y **aqui
alguien las leyo y dijo que no**. **4)** las alternativas estan prohibidas por letra: leer los **4**
pares que faltan es cribado que esta fase no tiene (banco 9.21), y **la fusion parcial la prohibe el
encargo con todas sus letras**.

**NO PARO, POR LA REGLA 5:** nada se toca, es reversible entero y no desmiente ninguna lectura
escrita. **Registro lo mejor sostenido, lo marco `PENDIENTE DE DOCTRINA` y lo subo como el `D1` de
esta vuelta.**

### 4.2 **LOS `ACTOS 13` Y `15`: LA GUARDA `1B` COMO MOTIVO UNICO, Y ES SU ESTRENO**

**El carril lo escribio el acta 65 y esta pagina lo registro** (linea **4023** de `03_FUSIONES.md`,
cotejada hoy). **Hasta hoy existia y nadie lo habia estrenado como motivo UNICO**: el acto 1 de la
vuelta 65 tenia dos puertas, **pero su motivo sellado fue `P.10`** y las puertas eran la segunda
razon.

| acto | las DOS puertas | por que no hay salida de fusion |
|---:|---|---|
| **13** | `hipotesis_de_canales` y `seleccion_canal_distribucion` | cualquier eleccion de superviviente **absorbe a la otra**, y la `1B` lo prohibe. **`P.10` no se dispara**: cero `D`, cero puentes, cero triangulos, **la razon del declarado es UNA y no dos** |
| **15** | `ecuacion_de_valor` y `prevencion_objeciones_vs_manejo` | **las tres varas apuntan A LA PUERTA**, asi que **NO es un choque de puerta**; lo que detiene es **la SEGUNDA puerta**, que habria que absorber |

> **EL `ACTO 15` SE PARECE A UN CHOQUE DE PUERTA Y NO LO ES, Y SE DICE PARA QUE NADIE LOS CONFUNDA.**
> En el choque **la vara apunta a un miembro y la puerta es OTRO**, y el carril manda **fundir a la
> puerta y registrar el choque** (acta 54, pregunta 1; el acto 9 de la vuelta 66 es el precedente
> nuevo). **Aqui la vara y la puerta son el mismo nodo.**

### 4.3 **EL `ACTO 14`: `P.5` CONTESTA `NO ES UNA`, Y ES EL SEGUNDO USO DEL CARRIL DEL ACTA 66**

**`P.10` no se dispara** (cero `D`, cero puentes) y **ningun miembro es puerta**. **Lo que lo detiene
es la respuesta de `P.5`, y esta escrita en el archivo por dos puestos:**

| | lo que el archivo dice, leido del dossier |
|---|---|
| **el PURO de CUATRO** | el puesto **1030**: *CON ESTE PAR NACE EL PRIMER PURO DE CUATRO*, y **enumera la familia**: `construccion_de_leverage`, `leverage_en_negociacion_con_vcs`, `gestion_multiples_term_sheets` y `estrategia_competencia_vcs`. **CUATRO miembros, SEIS pares posibles, LOS SEIS LEIDOS Y LOS SEIS EN `A`** |
| **el quinto, y no esta fuera por olvido** | el puesto **878** lo levanta por el **barrido de las `A`** del banco 9.15, lo mira y decide: **LA LECTURA LO DEJA FUERA PORQUE SU OBJETO ES COMO NEGOCIAR TERMINOS Y NO COMO GENERAR COMPETENCIA ENTRE INVERSORES** |

**Y LA VARA APUNTA AL NODO EXCLUIDO**, que no es un detalle: el cableado eligiria
`tecnica_anclaje_negociacion`, o sea que **fundir el acto entero pondria de superviviente al mismo
nodo que la lectura saco de la familia**, y **sellaria que el PURO DE CUATRO repite a un nodo que el
archivo declara de otro objeto**.

### 4.4 **EL `ACTO 17`: `P.10` CON SU TRIANGULO MEDIDO, Y UNA SEGUNDA RAZON INDEPENDIENTE**

**Es el primero de los seis actos con puente que el acta 66 dejo contados.** El puente es
`estrategia_de_innovacion_arenas`, con **2 triangulos** medidos y **2 `D` internos** (puestos **530**
y **863**), que **hablan del mismo nodo** y que **una fusion entera desmentiria**. El **530** es
ademas una **correccion declarada del 13 ago 2026 por relectura conjunta encargada por el auditor**:
era `A`, se midio paso por paso, **la afirmacion resulto FALSA** y paso a `D`.

**SEGUNDA RAZON INDEPENDIENTE:** `estrategia_de_innovacion_y_tecnologia` **es puerta y no es el
miembro al que apunta la vara**, asi que la `1B` tambien lo detendria. **Dos motivos independientes,
como el acto 1 de la vuelta 65.**

> **UNA CITA QUE SE TRAE COMO CONTRASTE Y NO COMO FUENTE** (regla 2): el puesto **460** dice que *esta
> familia ya esta declarada como racimo nuevo de SEIS nodos y se decide en mesa, no aqui*. **Medido
> hoy contra el fichero del tramo**, este acto **NO tiene dueno en mesa ni en destejido**
> (`duenos_mesa_o_destejido` vacio), que es el criterio con el que `OP-U-02` abrio su universo.
> **La discrepancia se declara y no se resuelve copiando**, y **ninguna de las dos lecturas mueve un
> nodo**.

---

## 5. CORRECCIONES DECLARADAS DE INSTRUMENTO

**Va por el carril del banco 9.10 y de la regla de la ficha envejecida** (linea **3338** de
`03_FUSIONES.md`, cotejada hoy), **con el texto viejo VERBATIM en el sitio donde muerde y sin tachar
nada**.

### 5.1 **`vuelta65_colisiones_esperadas.py`: EL DEFECTO DE `--base` PASA DE `2` A `4`**

**El docstring afirmaba `LA LINEA BASE ES 2 Y ESTA DECLARADA (acta 64, pregunta 3)`**, y **el acta 66
adjudico que queda en `4`**. Dejar un instrumento afirmando una cifra superada, **sabiendolo**, es la
especie que esta campana persigue. **El texto viejo queda entero debajo de la correccion**, el
defecto pasa a `4`, y **el eco de la corrida dice las dos cosas**: la cita nueva y que el texto viejo
decia 2.

**LA ARITMETICA NO SE TOCA Y ESO ES LA MITAD DEL PUNTO:** la guarda sigue **MIDIENDO** la base sobre
el arbol y **cayendo en `ROJO` si no calza con la declarada**. Es la guarda que **mordio en la
corrida del auditor de la vuelta 66**, y **sigue viva**. **Va marcado discutible (`D12`).**

### 5.2 **`comprobar_promesas_de_marcado.py`: LA AGUJA SE ENSANCHA POR SEGUNDA VEZ, Y EL ROTULO QUE MENTIA SE CORRIGE**

**Es un hallazgo de esta vuelta y no estaba encargado**, y **lo destapo la propia guarda de cierre
corriendo en verde sobre nada** (averia 7.3). El plan sellado del lote C dice **`VA MARCADO
DISCUTIBLE`**, sin la palabra `COMO`, y **el comprobador solo conocia `VA MARCADO COMO DISCUTIBLE` y
`VAN MARCADAS COMO DISCUTIBLES`**: imprimio *NINGUN PLAN DE LOS PASADOS PROMETE MARCADO* **sobre un
plan que promete**. **Es LA MISMA especie que el acta 64 adjudico en su pregunta 6: *una promesa
invisible es peor que una incumplida porque no sale en rojo*.**

**LO QUE SE MIDIO ANTES DE ENSANCHAR**, con el mismo barrido que la vuelta 65 corrio antes de su
propio ensanche: **barridos los 65 `PLAN_*.json` de `docs/loop`, la forma sin `COMO` aparece en UNO
solo** (el de esta vuelta, acto 16, `nota_del_reparto`) **y en ningun otro plan**; ese campo **no
trae ninguna de las dos formas viejas**, asi que el ensanche **destapa UNA promesa nueva** y **la
seccion 6 la CUMPLE**. **CERO promesas incumplidas destapadas: el ensanche no es regresion.**

**Y EN EL MISMO SITIO SE CORRIGE UN ROTULO QUE MENTIA, aunque no mueva ninguna cifra:** el eco decia
`"SINGULAR" if f == PROMESA else "PLURAL"`, verbatim, y **con TRES formas rotulaba `PLURAL` a una
forma que es singular**. **El texto viejo queda citado en el sitio.** Re-corrido, dice `SINGULAR SIN
COMO`.

**ES UNA GUARDA QUE CRECE**, y por eso va **enumerada en el docstring** y **marcada discutible**
(`D15`), que son las dos condiciones del acta 61 (`D2` y pregunta 2).

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D1`. DECLARAR EL `ACTO 12` POR UN `D` DIRECTO SIN TRIANGULO, CON UN MOTIVO QUE NO ESTA ENTRE LOS
TRES SELLADOS. ES EL MAS FUERTE DE LA VUELTA Y LO SE.** El encargo enumera **TRES** motivos sellables
(el triangulo de `P.10`, la guarda `1B` y la respuesta *DOS FAMILIAS* de `P.5`) y **esa lista se
puede leer como CERRADA**; **leida asi, este acto tenia que fundirse**. Mi lectura es que **fundir
desmentiria un veredicto DIRECTO y escrito**, y que **el acto 5 de la vuelta 66 se declaro por un
caso mas debil** (identidades que nadie leyo). **No paro porque nada se toca y es reversible entero**;
**lo subo como pendiente de doctrina 1**.

**`D2`. DECLARAR EL `ACTO 14` POR `P.5` CUANDO EL QUINTO TIENE UNA `A` CON UN MIEMBRO DEL PURO.** El
puesto **878** es de clase `A` y aun asi **su propio texto deja al nodo FUERA de la familia**. Leo
que **el veredicto de clase y la pertenencia a la familia son dos cosas** y que la lectura manda;
**se puede leer al reves**, y leido al reves el acto tenia cinco miembros de una familia y se fundia
al que el cableado eligiera.

**`D3`. ESTRENAR LA GUARDA `1B` COMO MOTIVO UNICO EN DOS ACTOS EL MISMO DIA.** El carril esta escrito
y registrado (linea 4023), **pero nadie lo habia usado solo**, y **lo uso dos veces seguidas**. **La
alternativa era fundir absorbiendo una puerta**, que la guarda prohibe con todas sus letras, asi que
no la tome; **pero estrenar un carril por partida doble merece que se diga**.

**`D4`. EN EL `ACTO 15` LAS TRES VARAS APUNTAN A UNA PUERTA Y AUN ASI DECLARO.** Alguien puede leer
que **si la vara apunta a la puerta, la puerta sobrevive y se funde** (que es el carril del acta 54).
**Mi lectura es que ese carril resuelve el CHOQUE, no la existencia de una SEGUNDA puerta**, y que
absorber `ecuacion_de_valor` rompe la `1B` igual. **El bulto es que un acto con `TODAS DE ACUERDO` se
queda sin fundir.**

**`D5`. EL LOTE ENTREGA UNA SOLA FUSION SOBRE SEIS ACTOS.** Es el rendimiento mas bajo del tramo (el
lote A: 1 de 2; el lote B: 3 de 6). **No hay ninguna fusion que yo haya evitado por comodidad**, y
cada declarado trae su medicion, **pero una vuelta que mueve cuatro nodos es una vuelta que mueve
cuatro nodos**, y eso va publicado.

**`D6`. DECLARAR EL LOTE EN SEIS ACTOS TENIENDO CINCO DECLARADOS BARATOS.** Al abrirlo no sabia
cuantos iban a declararse; **declare SEIS por el tamano que la vuelta 66 entrego**, y al final cinco
salieron sin fusion. **Se puede sostener que, visto el resultado, el lote debio ser mas largo.** **No
lo alargue sobre la marcha a proposito**: el lote se declara al abrirlo y se entrega lo declarado, y
cambiar el tope cuando ya sabes que sale barato es justo lo que el contrato del prefijo evita.

**`D7`. EL SUPERVIVIENTE DEL `ACTO 16` ES EL QUE EL CABLEADO NO ELIGE, Y POR MARGEN GRANDE.** 8 contra
3. **`P.8` dice que el cableado solo habla a contenido empatado y aqui el contenido dice algo (5
pasos contra 4)**, y el propio banco trae el ejemplar de **10 contra 5 perdiendo**. **Pero un margen
de cableado de casi tres a uno es un dato**, y queda dicho.

**`D8`. CINCO `APPEND` SOBRE UN SUPERVIVIENTE DE CINCO PASOS: EL NODO DUPLICA SU TAMANO.** De 5 a 10.
Elegi **catalogo mas rico con solapes declarados** sobre **`CUBIERTO` que calla texto vivo**, que es
el carril del `D9` del acta 65 y del `D7` del acta 66, **pero el costo esta publicado**, y **el nodo
resultante entro a la cola de costuras por eso** (seccion 9).

**`D9`. DOS `APPEND` QUE SE SOLAPAN: LA BRUJULA Y EL TITULAR.** El paso 4 de `how_might_we_framing`
(*usa la pregunta como brujula durante todo el proceso*) y el paso 4 de `how_might_we_hmw` (*usar
esta pregunta como titular para las sesiones de brainstorming*) dicen **los dos para que sirve la
pregunta despues de escribirla**. **Los meti los dos con el solape DECLARADO**, porque el puesto 1319
llama al segundo *su unico gesto propio*. **Quien lea el solape como identidad dira que sobra uno.**

**`D10`. SELLAR UNA PERDIDA UNA SOLA VEZ CON SUS DOS SITIOS EN EL CAMPO `donde`.** Dos perdidas de
esta vuelta las traen **dos nodos cada una**, y en vez de sellarlas dos veces **puse los dos sitios
en un solo campo**. **Mi razon es que inflar la cuenta duplicando una sola perdida tambien falsea el
campo**; **la lectura contraria es que el contrato pide una fila por pieza que se pierde**, y con esa
lectura la cuenta seria **11** y no **9**.

**`D11`. TRES PERDIDAS CON ATENUANTE DECLARADO.** Las tres dicen que **el contenido llega igual por
el `APPEND` de un hermano**. **Sellar una perdida que quiza no se pierde es sobre-sellar**, y lo hago
por el carril del `D8` del acta 63 y el `D10` del acta 65. **Es la cuenta del pendiente 4, y crece.**

**`D12`. CORREGIR EL DEFECTO DE `--base` SIN ENCARGO EXPLICITO.** El encargo manda medir **sobre 4**
y yo pase `--base 4` a mano, asi que **la correccion del defecto no era necesaria para esta vuelta**.
**La hice porque dejar committeado un instrumento que afirma una cifra superada, sabiendolo, es la
misma especie que el caso positivo que acusaba en falso de la vuelta 66.** **Se puede sostener que
tocar un instrumento fuera de encargo es alcance.**

**`D13`. RE-CODIFICAR DOS SALIDAS DE `cp1252` A `utf-8` EN VEZ DE RE-CORRER LOS INSTRUMENTOS.** Las
salidas del reanclaje y de Gate 0 se escribieron en la codificacion de la consola de Windows y **el
registrador no podia leerlas**. **Las pase a `utf-8` byte a byte, sin re-correr nada y sin cambiar
una cifra**, porque **re-correr el reanclaje habria dado `0` re-anclajes** (ya estaba hecho) y **esa
salida ya no seria la de la operacion**. **Se puede sostener que una salida re-codificada ya no es la
salida cruda.**

**`D14`. NO CONTESTAR LA PREGUNTA DE `P.5` EN EL `ACTO 15`.** Con la guarda `1B` deteniendo la
fusion, **la pregunta de si el quinto miembro es de la misma familia no cambia el destino del acto**,
y **la deje MEDIDA y sin contestar, diciendolo**. **`P.5` manda leer el acto entero antes de
fundirlo**, y este no se funde. **Pero se puede sostener que la pregunta se contesta siempre que el
acto se abre**, y con esa lectura falta una respuesta.

**`D15`. ENSANCHAR LA AGUJA DEL COMPROBADOR DE PROMESAS Y CORREGIR SU ROTULO, SIN ENCARGO.** Nadie
me pidio tocarlo; **lo corri porque el encargo manda comprobar las promesas por maquina y salio
diciendo que no habia ninguna sobre un plan que promete**. **La alternativa era declarar la promesa
como cumplida por mi ojo**, que es exactamente lo que esa guarda existe para no tener que hacer.
**Se puede sostener que tocar un instrumento de nombre estable fuera de encargo es alcance**, y que
lo debido era **re-sellar el plan con la forma que el instrumento ya conocia**. **No lo hice porque
el plan ya estaba sellado, committeado y EJECUTADO**, y **re-sellarlo despues de fundir habria dejado
el plan sellado diciendo algo distinto de lo que se ejecuto**.

---

## 7. LAS AVERIAS PROPIAS, CAZADAS ANTES DE UNA CIFRA PUBLICADA

**CERO de ellas llego a una cifra publicada ni a un dato movido.**

### 7.1 **DOS SALIDAS EN `cp1252` QUE ROMPIERON EL REGISTRADOR, Y LO CAZO SU PROPIA LECTURA**

`reanclar_por_resolutor.py` y `run_phase1.py` imprimen titulos de nodo con acentos, y **la consola de
Windows los redirige en `cp1252`**. **El registrador del lote C murio al leerlas con
`UnicodeDecodeError`**, que es exactamente lo que tenia que hacer: **no escribio nada**. Pasadas a
`utf-8` byte a byte, **sin re-correr y sin cambiar una cifra**, el registrador leyo sus 23 celdas.
**Es la misma especie que el `BOM` de PowerShell que el auditor declaro en la vuelta 66**, y **va
marcada discutible (`D13`)**.

### 7.2 **LLAME AL CASO POSITIVO DE MESA SIN SU ARGUMENTO REQUERIDO**

`caso_positivo_de_fusion_de_mesa.py` **exige `--id-op`** y lo llame sin el: `argparse` **murio con
`exit 2`**. **Lo vi porque miro los codigos de salida**, y **es justo la clase de fallo que la vuelta
66 encontro escondido** en el caso positivo del contrato de perdidas, **que leia un `exit 2` como si
la guarda no mordiera**. Re-corrido con `--id-op OP-M-02-ACCLIMATE`: **LAS NUEVE MUERDEN**. **Ninguna
salida con esa forma se publico.**

### 7.3 **UNA PROMESA DE MARCADO INVISIBLE, Y LA GUARDA PASO EN VERDE SOBRE NADA**

`comprobar_promesas_de_marcado.py` dijo **`NINGUN PLAN DE LOS PASADOS PROMETE MARCADO`** sobre el plan
del lote C, **que promete en su `nota_del_reparto`**. **La causa es tipografica y por eso es
peligrosa**: escribi `VA MARCADO DISCUTIBLE` y la aguja pedia `VA MARCADO COMO DISCUTIBLE`. **La cace
mirando la salida en vez de mirar el `exit 0`**, que es la leccion del caso positivo roto de la
vuelta 66. **Corregida por ensanche declarado y medido** (seccion 5.2); re-corrida: **1 promesa, 1
CUMPLIDA, 0 INCUMPLIDAS**. **Ninguna cifra publicada dependia de ella**, pero **una guarda que pasa
en verde sobre nada es peor que una que falla**.

### 7.4 **UN `ROTULO` HUERFANO QUE PUSE YO, Y LO CAZO EL BARRIDO DE CIERRE**

Le puse a `_v67_texto_acta66.py` un `ROTULO ... especie=PROCEDENCIA cita=vuelta:66` **copiando el
patron del registrador que lo importa**, y **el barrido de cierre lo saco en `ROJO` como `ROTULO
HUERFANO`**: *el rotulo no casa con ningun `AMBAR` vivo de este fichero*. **Tenia razon**, y el
antecesor del fichero (`_v66_texto_acta65.py`) **tampoco lleva rotulo**. **Retirado el rotulo
sobrante, `ROJO` vuelve a 32**, la linea base heredada sin mover, **y `AMBAR` sigue en 0**. **Es la
regla 1 aplicada al propio cierre: el estado al cierre se mide al cierre**, y **el barrido se
re-corrio DESPUES de escribir este reporte**, no antes.

---

## 8. PENDIENTES DE DOCTRINA Y PREGUNTAS

1. **QUE HACE UN ACTO CON UN VEREDICTO `D` DIRECTO INTERNO Y SIN TRIANGULO QUE CERRAR?** (nuevo, y es
   el grande de esta vuelta). **La letra no lo dice.** `P.10` define su disparador **sobre el
   triangulo**, que aqui **no existe**; `P.5` contesta **UNA familia**; y la guarda `1B` **pasa por
   vacio**. **Aun asi, fundir el acto entero desmiente un veredicto escrito.** Registro **lo mejor
   sostenido** (el carril del `DECLARADO Y NO FUNDIDO CON MOTIVO SELLADO`, con un **cuarto** motivo)
   y **lo subo**. **La pregunta concreta para el auditor: la lista de TRES motivos sellables es
   CERRADA o es la enumeracion de lo adjudicado hasta hoy?**
2. **UN ACTO CUYA FORMA ES `EMPATE SIN VARA`, QUE DESTINO TIENE MIENTRAS EL AUDITOR NO LO RESUELVA?**
   (nuevo, y **llega en el siguiente lote**). **`P.8` tiene la fila escrita**: *empatado y el cableado
   tambien: se trae al auditor*. **Lo traigo ANTICIPADO y MEDIDO**, para que no llegue de sorpresa:
   el **acto 18** del tramo (`alianzas_cross_industry`, `co_opetition_industria`,
   `colaboracion_sectorial`, `trabajo_colectivo_estandares_industria`) da **`EMPATE SIN VARA`** con
   **pasos 4 a cuatro bandas, condiciones 2 a cuatro bandas y cableado empatado**, medido hoy
   ([`SALIDA_V67_VARAS_SIGUIENTES.txt`](SALIDA_V67_VARAS_SIGUIENTES.txt)). **`P.8` dice a quien se
   trae, pero no dice si el acto queda `DECLARADO` mientras tanto o si espera.**
3. **EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE** (heredado, acta 66 pendiente 3): **ahora son
   NUEVE los actos declarados que esperan el cierre de la fase 03** (el 1, el 5, el 10 y el 11 de las
   vueltas anteriores, mas el 12, 13, 14, 15 y 17 de esta). Sigue enrutado al **cierre de la fase
   03**, donde **la parada de `AUDITOR.md` espera al fundador**.
4. **EN UN ACTO N-ARIO SIGUE SIN HABER MARCA PARA *YA LO DICE EL `APPEND` DE UN HERMANO*** (heredado,
   acta 66 pendiente 4): **esta vuelta lo pago TRES veces** con `CUBIERTO` mas atenuante declarado.
   **El carril alcanza, pero la cuenta crece.**
5. **EL `INCISO` DE CONDICIONES SIGUE SIN EXISTIR** (heredado): **cinco perdidas `DE CONDICIONES`
   mas** en esta vuelta, enrutadas a la fase 04 por el carril del acta 55, pregunta 5.
6. **EL ESQUEMA DE `OPERACIONES.jsonl`** (heredado): sigue pendiente y **esta vuelta no toco ninguna
   ficha**, asi que no estreno ninguna clave.

---

## 9. RUTAS TOCADAS Y CENSOS AL CIERRE

**Del grafo (21 ficheros):** el **superviviente** (`encuadre_desafio_diseno`), sus **cuatro
absorbidos** (`how_might_we_brief_social`, `how_might_we_briefs`, `how_might_we_framing`,
`how_might_we_hmw`), los nodos **redirigidos** por el alias nuevo, mas
`dataset/metadata/master_graph.json` y `dataset/metadata/phase1_run_log.json`.

**Del registro:** `docs/plan/03_FUSIONES.md` (**`+143`** del acta 66 y **`+410`** del lote C, **cero
borradas en los dos**), `docs/plan/ARISTAS_DUPLICADAS.jsonl`, `docs/COSTURAS_INTERNAS.jsonl` y su
resumen, `scripts/rumbos/banco_rumbos.json` (el reanclaje) y `web/lib/assets/` por el `sync`.
**`docs/plan/OPERACIONES.jsonl` NO se toco.**

**Instrumentos nuevos o corregidos:** `scripts/loop/vuelta67_registrar_acta66.py`,
`scripts/loop/_v67_texto_acta66.py`, `scripts/loop/_v67_lote_c.py`,
`scripts/loop/vuelta67_registro_lote_c.py`, `scripts/loop/_v67_texto_lote_c.py` y
`scripts/loop/vuelta65_colisiones_esperadas.py` (corregido, seccion 5.1) y
`scripts/loop/comprobar_promesas_de_marcado.py` (corregido, seccion 5.2).

| censo al cierre | valor |
|---|---|
| **barrido de titulos** ([`SALIDA_V67_BARRIDO.txt`](SALIDA_V67_BARRIDO.txt)), **re-corrido AL CIERRE** | **443 ficheros**, `ROJO` **32** (linea base heredada, **sin mover**), **`AMBAR` 0**, `ROTULADO` **42**, `CENSO` **223**, `ILEGIBLE` **1**. **Los 443 son los 438 del acta 66 mas los CINCO instrumentos nuevos de esta vuelta**, contados uno a uno |
| **censo de plantillas talladas** ([`SALIDA_V67_CENSO_PLANTILLAS.txt`](SALIDA_V67_CENSO_PLANTILLAS.txt)) | **CERO TALLADOS** sobre **23** instrumentos de nombre estable |
| **estado de las operaciones** ([`SALIDA_V67_CIERRE.txt`](SALIDA_V67_CIERRE.txt)) | **71**, todas `LISTA`, **0** dependencias rotas, **672** entradas, enlaces **17.555** |
| **casos positivos sobre sujetos que esta vuelta NO toca** | mesa: **LAS NUEVE MUERDEN** sobre `OP-M-02-ACCLIMATE`; promesas: **VERDE en sus dos mitades**; contrato de perdidas: **LAS CUATRO**; varas: **LAS TRES mitades** |

### 9.1 **LA TASA POR DOMINIO AL CIERRE, IDENTICA A LA DE APERTURA**

**Fundir no volteo ni un veredicto**, y por eso el marcador de cierre sale **identico linea a linea**
al de apertura (comparado por maquina: **0 lineas distintas sobre 21**).

| dominio | pares | `A` | tasa |
|---|---:|---:|---:|
| compras | 155 | 1 | 0,6 |
| core | 1.445 | 325 | 22,5 |
| entrega | 171 | 2 | 1,2 |
| environmental | 170 | 28 | 16,5 |
| exportacion | 130 | 15 | 11,5 |
| franquicias | 148 | 15 | 10,1 |
| health_safety | 192 | 43 | 22,4 |
| quality | 844 | 119 | 14,1 |
| risk_management | 106 | 0 | 0,0 |
| seguridad_digital | 27 | 3 | 11,1 |

**Corte de todas estas cifras: 25 ago 2026, puesto 3.388** (la fecha de los commits que las llevan; ver la nota de los dos relojes en la cabecera).

---

## 10. LO QUE QUEDA DEL TRAMO, MEDIDO

| | |
|---|---:|
| actos del tramo unico | **47** |
| cerrados por el lote A (vuelta 65) | **2** |
| cerrados por el lote B (vuelta 66) | **6** |
| **cerrados por el lote C (esta vuelta)** | **6** (1 fundido, 5 declarados) |
| **quedan** | **33 actos** |
| **nodos que quedan** | **109** |
| **el siguiente del prefijo** | el acto **18** |
| de los que quedan, con nodo puente al cierre | **5** (actos 20, 21, 23, 24 y 27) |
| **actos declarados que esperan el cierre de la fase 03** | **9** |

**NO SE FUNDIO NINGUN ACTO CON DUENO** (los 6 de fuera siguen fuera), **no se toco la mesa `OP-M-03`
ni sus dos colisiones**, **no se tocaron las dos colisiones de `OP-U-02`** (siguen vigentes y
publicadas con su duena), y **las cinco fichas `OP-M-02` consumidas no se ejecutaron**: lo consumado
no se ejecuta ni se rehace.

---

## 11. CONDICIONES DE PARADA, RECORRIDAS

| condicion | se cumple? |
|---|---|
| doctrina nueva inventada | **NO**: los quince discutibles y los seis pendientes quedan bajo letra citable (`P.1`, `P.5`, `P.8`, `P.10`, `P.11`, `P.12`, `P.16`, guarda `1B`, banco 9.6.1, 9.10, 9.15, 9.21 y 9.24, actas 53, 54, 55, 61, 63, 64, 65 y 66). **Lo que no tiene letra va como PENDIENTE, no como regla**: el motivo del acto 12 se declara **como sin letra**, no se disfraza de motivo conocido |
| contradiccion sin regla de correccion | **NO** |
| decision de fundador | **NINGUNA SE TOMA**: el merge sigue siendo suyo y no se autoriza ninguna lectura nueva |
| fallo tecnico repetido | **NO**: Gate 0 y las tres suites en verde |
| campana consumada | **NO**: quedan **33 actos y 109 nodos** del tramo, la mesa `OP-M-03` y las fases 04 en adelante |
| **cierre de la fase 03** (la parada de `AUDITOR.md`) | **NO SE CUMPLE TODAVIA**: quedan 33 actos, y los **9** declarados siguen sin destino resuelto |
| credenciales | no hicieron falta |

---

## 12. HASH FINAL Y COMMITS

**Los tres commits de trabajo de esta vuelta, escritos en la rama `pasada-unica`:**

| commit | que lleva |
|---|---|
| **`d25ab668`** | **TAREA 1 entera**: el registro del acta 66 (`+143`, `0` borradas, 55 citas y 0 malas) **y la APERTURA medida antes de la primera operacion** |
| **`c50cf7e4`** | **TAREA 2**: el lote C ejecutado (1 fusion, 5 declarados, 4 nodos muertos, `P.16` limpio, colisiones que calzan sobre la base 4, Gate 0 con su ciclo de tres y las tres suites en verde) |
| **`944747aa`** | **el registro del lote C** (`+410`, `0` borradas, citas 11 de 11, idempotencia mordiendo) |

**EL HASH FINAL DE LA VUELTA ES ESTE FICHERO ESCRITO POR SU CUARTO COMMIT**, y por eso se escribe
aqui **en una edicion posterior**: **un commit no puede contener su propio hash**. **Los TRES
anteriores estan arriba, leidos hoy con `git log --oneline`**, y el cuarto **es el que escribe esta
misma linea**. Es la misma via que las vueltas 65 y 66 usaron.

**LAS TRES GUARDAS DE CIERRE, RE-CORRIDAS TRAS ESTA EDICION** (regla 1: lo que la propia vuelta
mueve, se remide antes de publicar):

| guarda | comando | resultado |
|---|---|---|
| **la cabecera se talla, no se teclea** | `tallar_cabecera_reporte.py --vuelta 67 --comparar docs/loop/REPORTE.md` | **`CABECERA: IDENTICA AL TALLADOR`** ([`SALIDA_V67_CABECERA_COMPARADA.txt`](SALIDA_V67_CABECERA_COMPARADA.txt)) |
| **las promesas de marcado, por maquina** | `comprobar_promesas_de_marcado.py --reporte docs/loop/REPORTE.md --plan docs/loop/PLAN_V67_OPU02_LOTE_C.json` | **1 promesa, 1 CUMPLIDA, 0 INCUMPLIDAS**, **tras el ensanche declarado de la seccion 5.2** ([`SALIDA_V67_PROMESAS.txt`](SALIDA_V67_PROMESAS.txt)) |
| **el barrido de titulos, re-corrido AL CIERRE** | `barrido_titulos_tallados.py` | **443 ficheros, `ROJO` 32** (linea base sin mover), **`AMBAR` 0**, `ROTULADO` 42, `CENSO` 223 ([`SALIDA_V67_BARRIDO.txt`](SALIDA_V67_BARRIDO.txt)) |

**Cero guiones largos y cero guiones medios**, contados por maquina sobre el fichero entero.
