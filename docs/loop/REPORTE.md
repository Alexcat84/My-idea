# REPORTE DE LA VUELTA 66: EL LOTE B DEL TRAMO UNICO DE `OP-U-02`, TRES FUSIONES Y TRES DECLARADOS, Y EL PRIMER ACTO DE LA CAMPANA CERRADO POR LA PREGUNTA DE `P.5`

**Fase III, ejecucion continua. Rama `pasada-unica`. 20 ago 2026.**

**Fecha por dos relojes, corridos por mi:** `git log -1 --date=short` y el reloj del sistema dan los
dos **2026-08-20**.

---

## 1. LA CABECERA, TALLADA Y NO TECLEADA

**Generada entera con** `python scripts/loop/tallar_cabecera_reporte.py --vuelta 66` y **pegada sin
tocar una celda** ([`SALIDA_V66_CABECERA.txt`](SALIDA_V66_CABECERA.txt)). **La celda que no salga de
un instrumento no se escribe.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.262 / 591 / 17.511 | **3.853 / 3.247 / 606 / 17.540** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 292 / 259 | **551 / 315 / 236** |
| actos (componentes) | 78 | **75** |
| actos `CERRADOS` / `ABIERTOS` | 26 / 52 | **26 / 49** |
| nodos en `CERRADOS` / `ABIERTOS` | 61 / 230 | **61 / 212** |
| cola de costuras | 1.453 | **1.447** |
| colisiones de clase vigentes | 2 | **4** |
| auto-pares (los dos lados al mismo vivo) | 257 | **260** |
| duplicadas historicas: grupos / nodos | 921 / 730 | **915 / 725** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (291 igual a 291; 259 igual a 259) | **TODAS OK (273 igual a 273; 236 igual a 236)** |

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION** (regla 1): los seis instrumentos de apertura
corrieron con el arbol limpio en `eaa33c77`, **antes** de escribir nada. **EL CIERRE SE RECOMPUTO AL
CIERRE**, despues de que la fusion y `run_phase1` movieran el arbol.

> **UNA NOTA DE HONESTIDAD SOBRE EL FICHERO DE APERTURA, dicha en vez de callada:**
> [`SALIDA_V66_APERTURA.txt`](SALIDA_V66_APERTURA.txt) se corrio **sin el argumento de la etiqueta**,
> asi que su titulo dice `SIN ETIQUETA` donde el de cierre dice `CIERRE`. **Las cifras son las de la
> apertura** y el tallador las lee igual; **lo unico que no calza es el rotulo**, y se dice aqui
> porque un fichero llamado `APERTURA` cuyo titulo no lo dice es justo la clase de cosa que esta
> campana persigue.

### 1.1 **LA DIFERENCIA CON EL ACTA 65, EXPLICADA Y NO SUPUESTA**

**El acta 65 publica el barrido con `429 ficheros` y `CENSO 220`; mi corrida de apertura da `430` y
`221`.** **La diferencia esta medida:** el fichero 430 es
[`_auditor_v65_cuenta.py`](_auditor_v65_cuenta.py), **que el propio auditor committeo en `eaa33c77`
DESPUES de correr su barrido** (`git log --name-only` sobre ese commit, corrido por mi). **`ROJO 32`,
`AMBAR 0` y `ROTULADO 38` salen identicos.** No hay discrepancia que resolver: hay un fichero mas.

---

## 2. TAREA 1: EL REGISTRO DEL ACTA 65 Y LA CORRECCION DECLARADA DE LA FICHA

### 2.1 **EL REGISTRO DE LAS ADJUDICACIONES DEL ACTA 65** (`+118` lineas, `0` borradas)

`python scripts/loop/vuelta66_registrar_acta65.py`
([`SALIDA_V66_REGISTRO_ACTA65.txt`](SALIDA_V66_REGISTRO_ACTA65.txt)), adosado al final de
[`../plan/03_FUSIONES.md`](../plan/03_FUSIONES.md) **sin reescribir ni una linea de arriba**
(`git diff --numstat`: **`118 0`**).

| guarda | resultado |
|---|---|
| **citas cotejadas antes de escribir** | **47** (35 del acta, 12 de la propia pagina), **MALAS 0** |
| **re-cotejo TRAS adosar** | **OK, 12 de 12**: las sedes de arriba siguen en su linea |
| **idempotencia** | **MUERDE**: la segunda corrida dice `YA ADOSADA` y no escribe |
| **guiones largos / medios** | **0 / 0** |

**Lo que queda registrado**, y es lo que el encargo pedia: **los DOCE discutibles `A FAVOR`** con su
vara y su linea; **la adjudicacion del veredicto ausente con sus CUATRO letras copiadas** y **la
letra en divergencia sin callar**; **el carril del acto con dos o mas puertas** (y el caso de UNA
puerta separado a proposito, porque no es el mismo); **la caida de ACTA del auditor con su nombre, el
`NUEVE` por `OCHO`**, y **la racha de reporte de vuelta a CERO**; y **los pendientes 2 y 4 nombrados
con su destino, el cierre de la fase 03**.

### 2.2 **LA CORRECCION DECLARADA DE LA CLAUSULA DE LA ERA DEL PAR** (`1` linea cambiada)

`python scripts/loop/vuelta66_correccion_ficha_opu02.py --escribir`
([`SALIDA_V66_CORRECCION_FICHA_OPU02.txt`](SALIDA_V66_CORRECCION_FICHA_OPU02.txt)).

**El texto viejo se cita VERBATIM y NO se tacha.** La clausula corregida, que sigue en su sitio como
elemento **4** de la lista `verificacion`, dice: *el acto se leyo ENTERO antes de fundirse: cero pares
internos sin veredicto*. **Se escribio en la era en que la componente era el par** y **leida a la
letra hoy anularia los 47 actos del tramo**.

**LA VARA NUEVA, EN SUS TRES MITADES Y TODAS CITABLES:**

| | la vara nueva | su letra |
|---|---|---|
| **que es LEIDO ENTERO** | los **TEXTOS del acto** y la pregunta de si es una familia o dos, **no** todas las combinaciones de pares | `P.5` con su correccion de alcance (15 ago 2026, decision del fundador) |
| **que es UN PAR SIN LEER** | el que esta **EN COLA** y sin veredicto, contado aparte por el recomputo en `en_cola_sin_leer`; los 47 actos traen **CERO** | el propio `recomputo_3388.py`, verificado en el acta 11 |
| **que BLOQUEA una fusion** | el **triangulo `A` mas `A` mas `D` MEDIDO**, y la **guarda `1B`**; en los dos casos el acto cierra `DECLARADO Y NO FUNDIDO` | `P.10` y la guarda `1B`, con la adjudicacion del acta 65 |

| guarda | resultado |
|---|---|
| **la clausula vieja se pudo citar** | **OK**: hallada **una sola vez**, IDENTICA al byte, elemento 4 de 6 |
| **clave nueva de esquema** | **NINGUNA**: es un elemento mas de la lista `verificacion`, el carril que **esta misma ficha uso en su `evidencia` en la vuelta 48** |
| **fichas antes / despues** | **71 / 71**, con **las MISMAS 18 claves en todas** |
| **el texto viejo sigue dentro** | **OK**, verbatim |
| **las otras 70 fichas** | **IDENTICAS al byte** |
| **idempotencia** | **MUERDE**: `YA ESCRITA`, no escribe |

**EL ESTADO Y LAS DEPENDENCIAS DE LAS 71 FICHAS QUEDAN COMO ESTABAN, Y NO ES UNA IMPRESION:**
`vuelta31_estado.py` corrido **antes y despues** de la correccion da **CERO lineas distintas sobre
85** (comparado linea a linea por maquina). **71 operaciones `LISTA`, 0 dependencias rotas, 672
entradas, enlaces 17.511.**

---

## 3. TAREA 2: EL LOTE B, DECLARADO AL ABRIRLO Y ENTREGADO ENTERO

**EL LOTE ES PREFIJO SIN SALTOS** del `orden_universo` de lo que quedaba del tramo fijado en
[`TRAMO_UNICO_OPU02_V64.jsonl`](TRAMO_UNICO_OPU02_V64.jsonl) (el lote A cerro los actos **1** y
**3**): **los actos 5, 7, 8, 9, 10 y 11. SEIS actos y 37 nodos**, **los seis cerrados ENTEROS**.

| acto | miembros | cierra | superviviente |
|---:|---:|---|---|
| **5** | 8 | **`DECLARADO Y NO FUNDIDO` por `P.5`** | ninguno se elige |
| **7** | 6 | **FUNDIDO** | `six_sigma_dmaic` |
| **8** | 6 | **FUNDIDO** | `cierre_segun_complejidad_venta` |
| **9** | 6 | **FUNDIDO** | `marco_analisis_mercado_cadena_suministro` (**PUERTA**) |
| **10** | 6 | **`DECLARADO Y NO FUNDIDO` por `P.10`** | ninguno se elige |
| **11** | 5 | **`DECLARADO Y NO FUNDIDO` por `P.10`** | ninguno se elige |

### 3.1 **`P.5` CONTESTADA ACTO POR ACTO, SOBRE EL TEXTO ESTABLE**

**El acto se leyo ENTERO** con `python scripts/loop/dossier_del_tramo.py --tramo
docs/loop/TRAMO_UNICO_OPU02_V64.jsonl --actos 5,7,8,9,10,11`
([`SALIDA_V66_DOSSIER_LOTE_B.txt`](SALIDA_V66_DOSSIER_LOTE_B.txt), **877 lineas**), con **todos sus
pares internos y su razon entera**.

| acto | libro | pares `A` | pares `D` | puentes | triangulos | **una familia o dos** |
|---:|---|---:|---:|---:|---:|---|
| **5** | CUATRO libros distintos | 9 | **0** | 0 | 0 | **NO ES UNA. Hay un bucle y TRES procesos que lo contienen** |
| **7** | Juran (los 6) | 7 | 0 | 0 | 0 | **UNA** |
| **8** | SPIN Selling (los 6) | 9 | 0 | 0 | 0 | **UNA**, y el puesto 601 ya la declaraba |
| **9** | Hugos (los 6) | 7 | 0 | 0 | 0 | **UNA**, y el puesto 483 ya la anotaba |
| **10** | Blank (los 6) | 6 | **4** | **2** | **3** | `P.10` la detiene |
| **11** | Mollick (los 5) | 5 | **2** | **2** | **2** | `P.10` la detiene |

**MEDIDO** con `python scripts/loop/vuelta65_puentes_del_tramo.py --tramo ... --detalle`
([`SALIDA_V66_PUENTES_LOTE_B.txt`](SALIDA_V66_PUENTES_LOTE_B.txt)), **con los ids pasados por el
resolutor (`P.1`)**.

### 3.2 **LAS VARAS POR FORMA, CON SU LETRA Y MEDIDAS POR INSTRUMENTO**

`python scripts/loop/varas_n_arias_del_tramo.py --tramo ... --actos 5,7,8,9,10,11`
([`SALIDA_V66_VARAS_N_ARIAS.txt`](SALIDA_V66_VARAS_N_ARIAS.txt)).

| acto | **FORMA medida** | a que lado apunta | **la letra que decide** |
|---:|---|---|---|
| **5** | `UNA SOLA VARA` | `desarrollo_en_espiral` | **no llega a aplicarse: `P.5` se contesta ANTES que `P.8`** |
| **7** | `CONTENIDO EMPATA` | pasos empatan en 6 a tres bandas, condiciones en 3 a dos | **decide EL CABLEADO SOLO** (`P.8`): 11 contra un maximo de 5, `six_sigma_dmaic` |
| **8** | `TODAS DE ACUERDO` | `cierre_segun_complejidad_venta` (5 pasos contra 4, 3 condiciones contra 2) | **funde a su lado**; el cableado **no hace falta y no se usa** |
| **9** | `TODAS DE ACUERDO` | `cuatro_categorias_desempeno...` (10 pasos contra 5, 4 condiciones contra 3) | **CHOQUE con la guarda `1B`: LA PUERTA SOBREVIVE** (acta 54, pregunta 1) |
| **10** | `UNA SOLA VARA` | `refinar_sales_roadmap` | **no llega a aplicarse: `P.10` detiene** |
| **11** | `UNA SOLA VARA` | `alineacion_etica_ia_negocio` | **no llega a aplicarse: `P.10` detiene** |

**EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN**, y **ninguna vara se teclea**: las tres cuentas por
miembro salen del instrumento.

### 3.3 **LAS TRES FUSIONES, EN CIFRAS DEL INSTRUMENTO**

`python scripts/loop/fundir_por_plan.py --plan docs/loop/PLAN_V66_OPU02_LOTE_B.json --ejecutar`
([`SALIDA_V66_FUSION_LOTE_B.txt`](SALIDA_V66_FUSION_LOTE_B.txt)).

| | acto 7 | acto 8 | acto 9 |
|---|---:|---:|---:|
| absorbidos | 5 | 5 | 5 |
| pasos del superviviente | 6 a **12** | 5 a **12** | 5 a **21** |
| condiciones | 3 a **8** | 3 a **7** | 2 a **7** |
| piezas repartidas | 38 | 29 | 40 |
| de ellas `APPEND` / `CUBIERTO` / `INCISO` | 11 / 27 / **0** | 11 / 17 / **1** | 21 / 18 / **1** |
| perdidas selladas en campo propio | 11 | 8 | 12 |

**TOTAL: 15 nodos mueren (3.262 vivos a 3.247), 107 piezas repartidas, 31 perdidas selladas, 65
ficheros tocados.**

**LAS GUARDAS DE LA OPERACION, LAS CUATRO POR ACTO Y TODAS VERDES:** guarda 1 (miembros vivos y
nomina completa), guarda **1B** (ningun absorbido es semilla ni extremo de puente), guarda 2
(cobertura exacta de indices, cero olvidos) y guarda 3 (cero repetidos literales). **Los DOS `INCISO`
se EXTRAJERON del nodo y se comprobaron VERBATIM**, y sus dos pasos resultantes estan impresos en la
salida.

**`P.16`, QUIEN FABRICA LIMPIA, EN EL MISMO COMMIT:** la fusion fabrico **10** duplicadas y **las
limpio en la misma corrida**; **guarda A** (cero auto-aristas nuevas) **OK**, **guarda B** (cero
duplicadas nuevas tras resolver) **OK**, **guarda C** (los 15 campos que esta operacion no redacta,
intactos: **15 de 15**) y **guarda D** (los 15 absorbidos conservan su texto **INTACTO**) **OK**. El
pasivo historico **baja 8** y **ni una duplicada ajena se toca de mas**.

**`reanclar_por_resolutor.py` corrido ENTRE la fusion y `run_phase1`**
([`SALIDA_V66_REANCLAJE.txt`](SALIDA_V66_REANCLAJE.txt)): *nada que re-anclar, ninguna referencia
apunta a un absorbido*. **Se corre igual y se dice, en vez de darlo por bueno.**

### 3.4 **EL DIFF DE DUPLICADAS, POR INSTRUMENTO Y NO POR CODIGO SUELTO**

`python scripts/loop/diff_duplicadas_por_resolutor.py --antes <apertura, sacada de git> --despues
docs/plan/ARISTAS_DUPLICADAS.jsonl`
([`SALIDA_V66_DIFF_DUPLICADAS.txt`](SALIDA_V66_DIFF_DUPLICADAS.txt)).

> **GRUPOS FABRICADOS DE VERDAD: `0`.** Hay **3 RENOMBRADOS** (el mismo grupo con el rotulo nuevo del
> superviviente) y **4 que DESAPARECEN**, y los siete estan explicados por el alias nuevo. **921
> grupos a 915.**

### 3.5 **EL CENSO DE COLISIONES: ESPERADAS MEDIDAS ANTES DE FUNDIR, Y CALZA**

**La cuenta esperada se midio ANTES, sobre el arbol de antes y simulando en memoria**, que es la
adjudicacion 3 del encargo y la leccion del `D5` del acta 64:
`python scripts/loop/vuelta65_colisiones_esperadas.py --plan docs/loop/PLAN_V66_OPU02_LOTE_B.json`
([`SALIDA_V66_COLISIONES_ESPERADAS.txt`](SALIDA_V66_COLISIONES_ESPERADAS.txt)).

| | |
|---|---:|
| linea base declarada (las dos de la mesa `OP-M-03`) | **2** |
| **colisiones NUEVAS que la fusion fabricaria** | **2** |
| colisiones que desaparecerian | 0 |
| **ESPERADAS TRAS FUNDIR** | **4** |
| **MEDIDAS al cierre por el censo** | **4** |
| **calzan y son LAS MISMAS CUATRO** | **SI** |

**Las dos nuevas las fabrica el acto 8** y estaban **predichas por su nombre**:
`cierre_satisfaccion_postventa` contra `cierre_segun_complejidad_venta`, y
`cierre_segun_complejidad_venta` contra `obtencion_compromiso`, **las dos `B` contra `D`**. **Las dos
de la mesa `OP-M-03` no se tocan** y siguen siendo suyas.

> **LA LINEA BASE DEL CENSO PASA DE `2` A `4`, DECLARADA Y CON DUENO NOMBRADO.** Las dos nuevas
> **nacen de una fusion de `OP-U-02`** y **no de la mesa**, asi que **no heredan a `OP-M-03`**:
> **quedan REGISTRADAS, VIGENTES y PUBLICADAS EN ROJO**, con **`OP-U-02` como su duena**, y **la
> proxima operacion corre el censo con esperadas medidas sobre `4`**. **Va marcado como discutible en
> la seccion 6.**

### 3.6 **GATE 0 CON SU CICLO DE TRES, Y NO DE CUATRO**

**La averia 7.3 de la vuelta 65 no se repite.** El orden es el que el propio aviso de `run_phase1`
dice: **recompilar**, `etiquetas_de_cara.py --aplicar`, `sync_assets_web.py`, **y ahi se para**.

| paso | resultado |
|---|---|
| `python scripts/run_phase1.py --reaplico-curaduria` | **`GATE 0: OK`**, todos los chequeos en `[OK]`; universo **3.247 activos / 606 deprecados** |
| `python scripts/etiquetas_de_cara.py --aplicar` | **71 etiquetas** re-aplicadas |
| `python scripts/sync_assets_web.py` | **6 assets** mas `manifest.json` |
| **una cuarta corrida** | **NO SE HIZO** |

**LAS TRES SUITES, CORRIDAS POR MI:** motor **25/25**; web **80 ficheros, 1.030 pasadas, 3
saltadas**; `tsc --noEmit` **CERO lineas**. **Y el guardian de commit las volvio a correr en verde en
los dos commits de esta vuelta.**

### 3.7 **EL REGISTRO EN `03_FUSIONES.md`** (`+398` lineas, `0` borradas)

`python scripts/loop/vuelta66_registro_lote_b.py`
([`SALIDA_V66_REGISTRO_LOTE_B.txt`](SALIDA_V66_REGISTRO_LOTE_B.txt)), **bajo la cabecera de tramo que
la vuelta 65 adoso** y **sin reescribir ni una linea de arriba** (`git diff --numstat`: **`398 0`**).

**NINGUNA TABLA TECLEADA:** las del reparto pieza a pieza y las de piezas por absorbido **se generan
del plan sellado**, las de perdidas **se recortan de la salida del tallador leyendo la columna `acto`
por su sitio en la cabecera**, y las celdas de guardas y censos **se extraen por aguja**. **Citas
cotejadas 8, MALAS 0** antes de escribir y **8 de 8** despues. **Idempotencia MUERDE.**

---

## 4. LOS TRES DECLARADOS, Y EL QUE ESTRENA CARRIL

### 4.1 **EL `ACTO 5`: EL PRIMERO DE LA CAMPANA CERRADO POR LA PREGUNTA DE `P.5`**

**`P.10` NO SE DISPARA AQUI, y se dice primero:** **cero `D` internos, cero nodos puente, cero
triangulos**, medido. **Con `P.10` sola este acto se fundiria**, porque el acta 65 ya adjudico que un
veredicto ausente no es un par sin leer.

**LO QUE LO DETIENE ES LA PREGUNTA QUE `P.5` OBLIGA A CONTESTAR: el acto es UNA familia o son DOS.**
Contestada sobre el texto estable de los ocho nodos, **NO ES UNA**:

| | |
|---|---|
| **la sub-familia del bucle** | `build_measure_learn`, `ciclo_construir_medir_aprender`, `ciclo_crear_medir_aprender` y `startup_como_experimento_cientifico`, cerrados entre si por los puestos **213, 376, 486 y 1208** |
| **TRES procesos largos que lo contienen como UN paso** | `design_thinking_proceso` (entender, observar con etnografia, definir punto de vista, idear); `testing_process_completo` (los dos lienzos, hipotesis criticas, tarjeta de test, Progress Board); `desarrollo_en_espiral` (que se mide, cuantas vueltas, documentar cada iteracion) |
| **el nodo que los PEGA, y no tiene nada propio** | `design_test_repeat`, cuyas cinco `A` (**723, 796, 1182, 1449, 1573**) son **la unica via** por la que los tres entran a la componente |
| **entre los tres procesos** | **CERO veredictos escritos** |

**SUS PROPIAS RAZONES LO DICEN CUATRO VECES**, leidas del dossier: el **796** lo llama *el ciclo
desnudo contra el proceso que lo contiene* y dice que lo que anade *no llega ni a una linea*; el
**1182** y el **1573** lo llaman **SUBCONJUNTO ESTRICTO**; y el **1573** avisa de que de
`design_thinking_proceso` *se perderian CUATRO ETAPAS ENTERAS*.

**`P.12` ES LA LETRA QUE CIERRA ESTO:** *el cierre transitivo convoca, la lectura decide*, y con el
acto leido entero **mandan los veredictos DIRECTOS**, porque **una `A` que nadie leyo no existe**.
Fundir el acto entero **sellaria que los tres procesos repiten entre si**, y eso **nadie lo leyo**.

**LAS ALTERNATIVAS, RECORRIDAS EN VEZ DE ELEGIR LA COMODA:** leer los 19 pares que faltan es cribado
que esta fase no tiene (banco 9.21 y regla 4); **fundir solo la sub-familia cerrada es una FUSION
PARCIAL**, que el encargo prohibe con todas sus letras; y fundir entero desmiente cuatro razones
escritas. **ASI QUE NO SE FUNDE NADA Y SE DECLARA:** el acto queda **vivo y entero**, sin un nodo
tocado, **reversible entero**.

### 4.2 **LOS `ACTOS 10` Y `11`, POR `P.10`, CON SU TRIANGULO MEDIDO**

| acto | nodos puente | triangulos | puestos de los `D` internos | lo que una fusion entera desmentiria |
|---:|---:|---:|---|---|
| **10** | **2** (`refinar_sales_roadmap` en dos, `sales_roadmap_vs_sales_force` en uno) | **3** | **872, 1023, 1306, 1330** | cuatro lecturas **de una pieza**: el **1306** y el **1330** dicen los dos *el contenido del mapa contra el uso del mapa*, y el **872** declara que *el sub-puro del sales roadmap SE ROMPE* |
| **11** | **2** (`human_in_the_loop_ia` y `mitigar_falling_asleep_wheel`, uno cada uno) | **2** | **1496, 1541** | dos lecturas que dicen **la misma frontera con las mismas palabras**: *uno protege la decision de hoy, el otro protege la capacidad de decidir de manana*; y el **1541** declara que **la particion escrita NO se mueve** |

**NINGUNO DE LOS TRES DECLARADOS TIENE PUERTA DENTRO**, medido al sellar: **la guarda `1B` pasa por
vacio en los tres y se dice en vez de darla por buena**, o sea que **la razon del `DECLARADO` es UNA
y no dos** (a diferencia del acto 1, que tenia dos razones independientes).

**Su destino comparte carril con el pendiente 2 del acta 65: el cierre de la fase 03.**

---

## 5. CORRECCIONES DECLARADAS DE INSTRUMENTO

**Las tres van por el carril del banco 9.10, con el texto viejo VERBATIM en el sitio donde muerde y
sin tachar nada.**

### 5.1 **`vuelta58_varas_tramo.py`: DOS CAMBIOS, Y LOS DOS MARCADOS DISCUTIBLES**

**Cambio 1, el ordinal.** El descubrimiento conocia **un** prefijo y no dos: corrido sobre el tramo
unico daba **`ROJO: el fichero del tramo tiene 0 claves de ordinal ([]). PARADA`**, **medido antes de
tocar nada** ([`_v66/varas_lote_b.txt`](_v66/varas_lote_b.txt) de la corrida de apertura). **Es la
TERCERA vez que la campana paga esta misma especie** en un instrumento de nombre estable (la vuelta
65 la pago dos veces, en el generador y en el dossier). **La rama `orden_tramo` sale IDENTICA.**

**Cambio 2, y es el que importa: un acto de mas de dos miembros ahora es `ROJO` en vez de recorte
mudo.** Ese cuadro **compara `d[0]` contra `d[1]` de `sorted(miembros)`**: corregido solo el ordinal,
**habria publicado una fila de DOS por acto sobre actos de hasta quince, con los demas desaparecidos
EN SILENCIO**. **Es la especie que el acta 65 llamo la peor**, la que miente. **La aritmetica de las
flechas y de la FORMA no se toca.**

**Nace [`varas_n_arias_del_tramo.py`](../../scripts/loop/varas_n_arias_del_tramo.py)**, de nombre
estable, que **COPIA LITERAL de aquel** el bloque de la FORMA y su `protegidos()`, y **generaliza
solo la FLECHA**: la vara apunta al **UNICO** que alcanza el maximo, y **empata** si lo alcanzan dos
o mas. **Con `N` igual a 2 da exactamente la flecha vieja**, y eso **esta medido**, no razonado.

### 5.2 **EL CASO POSITIVO DE ESA CORRECCION, Y MORDIO**

`python scripts/loop/vuelta66_caso_positivo_varas.py`
([`SALIDA_V66_CASO_POSITIVO_VARAS.txt`](SALIDA_V66_CASO_POSITIVO_VARAS.txt)): **LAS TRES MITADES EN
VERDE**.

| mitad | que exige | resultado |
|---|---|---|
| **1** | ancestro y corregido sobre un tramo de DOS miembros dan **la misma salida linea a linea** | **16 lineas, 0 distintas** |
| **2** | el ancestro cae por el ordinal; el corregido **ya no**, cae por la guarda nueva, **nombra al N-ario** y **no imprime ni una fila de cuadro** | **las cuatro condiciones** |
| **3** | el N-ario da **la MISMA FORMA** que el de pares sobre ese mismo fixture | `TODAS DE ACUERDO` en los dos |

> **MORDIO EN SU PRIMERA CORRIDA, y por eso es creible:** la guarda nueva estaba **DESPUES** del
> `print` de la cabecera, asi que el instrumento publicaba *EL CUADRO DE VARAS DE LOS 47 ACTOS DEL
> TRAMO* y **luego no imprimia ni una fila**. **Una cabecera que promete 47 filas y da cero es media
> mentira**, y la mitad 2 la cazo. Subida la guarda antes de la cabecera, verde.

### 5.3 **`caso_positivo_del_contrato_de_perdidas.py`: UN CASO POSITIVO QUE ACUSABA EN FALSO**

**Es un hallazgo de esta vuelta y no estaba encargado.** Ese caso positivo llamaba al generador
**SIN `--operacion`**, que es **REQUERIDO desde la vuelta 63**: sus tres llamadas **morian en
`argparse` con `exit 2`** y el fichero **leia ese `2` como si la guarda no mordiera**. Daba
**`ROJO: 4 de 4 fallan`** contra unas guardas que estan **sanas**.

> **UN CASO POSITIVO QUE ACUSA EN FALSO ES TAN MALO COMO UNO QUE CALLA**, porque la proxima vez que
> acuse nadie le va a creer. **Ha estado asi desde la vuelta 63 y nadie lo corrio**: las actas 64 y 65
> enumeran los casos positivos re-corridos y **este no esta en ninguna de las dos listas**.

**Corregido con el texto viejo verbatim en el sitio**, re-corrido da **LAS CUATRO PRUEBAS EN VERDE**
([`SALIDA_V66_CASO_POSITIVO_PERDIDAS.txt`](SALIDA_V66_CASO_POSITIVO_PERDIDAS.txt)): las tres guardas
**muerden** y **la buena pasa**, o sea que **no es un sello de goma**.

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D1`. DECLARAR EL `ACTO 5` POR LA PREGUNTA DE `P.5` CUANDO `P.10` NO SE DISPARA. ES EL MAS FUERTE
DE LA VUELTA Y LO SE.** El encargo de esta vuelta dice, con todas sus letras, que **el disparador que
detiene una fusion es el TRIANGULO `A` mas `A` mas `D` medido**. **Aqui no hay triangulo y aun asi no
fundo.** Mi lectura es que esa frase contesta a `P.10` y **no abole la pregunta de `P.5`**, que el
propio encargo manda contestar dos parrafos mas abajo, y que **la adjudicacion 2 del encargo ya
reconoce un segundo disparador que no es el triangulo** (la guarda `1B` sobre un acto de dos
puertas). **Pero se puede leer al reves, y si se lee al reves este acto tenia que fundirse.** No paro
porque **nada se toca, nada se desmiente y es reversible entero**; **lo subo como pendiente de
doctrina** en la seccion 8.

**`D2`. HABER FUNDIDO EL `ACTO 9` CON EL SUPERVIVIENTE MAS CORTO, Y FABRICAR EL NODO MAS LARGO DE LA
CAMPANA.** La guarda `1B` obliga a que la puerta sobreviva, **pero el resultado es un nodo de 21
pasos y 7 condiciones**, por encima de los 15 del acto 3. **La alternativa era declarar el acto**, y
la descarte porque **el carril escrito para el choque de puerta es fundir con la puerta y registrar
el choque** (acta 54, pregunta 1, con el acto 20 de precedente). **El bulto es real y va publicado en
vez de escondido.**

**`D3`. LOS PASOS 7 A 10 DE `cuatro_categorias_desempeno_cadena_suministro` VIAJARON DE `APPEND`
AUNQUE PARECEN UN INJERTO.** Los cuatro son razones financieras (rotacion, retorno sobre ventas,
ciclo de conversion de efectivo, cuentas por cobrar) **que no vuelven a nombrar las cuatro
categorias**. **Lo dije y no lo toque**, porque decidir si es injerto es materia de destejido (`P.3`
y `P.19`) **y ninguna operacion escrita lo nombra**. **Fundir no es sitio para destejer**, pero
**meter cuatro pasos sospechosos dentro de un superviviente tambien tiene su costo.**

**`D4`. LA LINEA BASE DEL CENSO DE COLISIONES PASA DE `2` A `4` Y LE PONGO DUENA A `OP-U-02`.** Las
dos nuevas **las fabrica mi fusion**, no la mesa, asi que **no las heredo a `OP-M-03`**. **Es una
decision de carril que nadie ha escrito** y la tomo con la medicion delante: quedan **vigentes,
publicadas en rojo y con dueno nombrado**. Se puede sostener lo contrario (que toda colision viva vaya
a la mesa que gobierna la serie).

**`D5`. NO PUSE NI UN `INCISO` EN EL `ACTO 7`, Y EL MOTIVO ES TIPOGRAFICO.** Los seis pasos de
`six_sigma_dmaic` **terminan en punto**, y un inciso adosado detras de un punto no se lee limpio.
**Ocho parametros concretos fueron a `CUBIERTO` con perdida nombrada por eso.** Es el criterio escrito
(la legibilidad del paso resultante) aplicado a rajatabla, **pero ocho perdidas por un punto final
son ocho perdidas.**

**`D6`. `SEIS` PASOS DE `APPEND` DESDE LA SECUENCIA UNIVERSAL AL `DMAIC`.** Las razones declaran que
**breakthrough IGUAL DMAIC**, y aun asi meti seis pasos enteros (la creencia, el Pareto, los dos
brazos, el impacto cultural, el proyecto formal, el replicar). **Mi lectura es que la identidad que
las razones declaran es de VIAJE y no de ANDAMIAJE**, y el andamiaje no esta en el `DMAIC`. **Quien
lea la identidad como total dira que sobran seis pasos.**

**`D7`. VEINTIUNA PIEZAS ENTERAS EN EL `ACTO 9`.** Es el reparto con mas `APPEND` de la campana.
Elegi **catalogo mas rico con solapes declarados** sobre **`CUBIERTO` que calla texto vivo**, que es
el carril del `D9` del acta 65, **pero el costo esta publicado**: 21 pasos.

**`D8`. LAS SIETE PERDIDAS CON ATENUANTE DECLARADO.** Cuatro en el acto 9, dos en el 7 y una en el 8.
**Sellar una perdida que quiza no se pierde es sobre-sellar**, y lo hago por el carril del `D8` del
acta 63 y el `D10` del acta 65. **Inflar la cuenta de perdidas tiene su propio costo.**

**`D9`. LOS DOS CAMBIOS DEL CUADRO DE VARAS, Y ESTRENAR UN INSTRUMENTO DE NOMBRE ESTABLE EL MISMO
DIA.** Van los dos aqui por **las dos condiciones del acta 61** (`D2` y pregunta 2): **enumerados en
el docstring** y **marcados discutibles**. El segundo cambio **es una guarda que CRECE** y el
instrumento nuevo **se estrena y se usa el mismo dia**; lo sostengo por el carril del `D2` y el `D3`
del acta 65, **y porque el caso positivo mordio de verdad antes de publicar nada**.

**`D10`. CORREGIR `caso_positivo_del_contrato_de_perdidas.py` SIN ENCARGO.** Nadie me pidio tocarlo;
**lo corri porque el encargo manda casos positivos y salio en rojo**. Corregirlo **no estaba en el
alcance**, pero **dejar un instrumento que acusa en falso committeado, sabiendolo, es peor**.

**`D11`. LA CITA DE LINEA `3959` QUE ERA `3962`.** La escribi mal en el registrador del lote B **y la
guarda de citas la cazo sin escribir nada**. **No es discutible que estuviera mal**; lo discutible es
que **la corregi con la medicion (`grep`) en vez de re-derivar todas las citas por aguja**, que seria
el remedio mecanico de verdad. **Queda anotado.**

**`D12`. EL FICHERO DE APERTURA LLEVA `SIN ETIQUETA` EN SU TITULO.** Corri `vuelta31_estado.py` de
apertura **sin el argumento**, y cuando quise darle el rotulo el arbol ya se habia movido. **Elegi
copiar la salida real con su titulo torcido y decirlo** antes que re-correrlo con datos de cierre
bajo un rotulo de apertura. **Se puede sostener que un fichero asi no deberia llamarse `APERTURA`.**

---

## 7. LAS AVERIAS PROPIAS, CAZADAS ANTES DE UNA CIFRA PUBLICADA

**CERO de ellas llego a una cifra publicada ni a un dato movido.** Se cuentan enteras porque callarlas
seria la especie que la casa persigue.

### 7.1 **LA GUARDA NUEVA DEL CUADRO DE VARAS ESTABA DEBAJO DE SU PROPIA CABECERA**

La puse **despues** del `print` del titulo, asi que el instrumento **anunciaba 47 filas y no imprimia
ninguna**. **Lo cazo la mitad 2 de mi propio caso positivo**, no mi ojo. Subida antes de la cabecera,
las tres mitades en verde. **Ninguna salida con esa forma se publico.**

### 7.2 **LA CITA `3959` POR `3962`**

En `vuelta66_registro_lote_b.py` cite la seccion del acta 65 en la linea **3959** cuando esta en la
**3962**. **La guarda de citas la caza y NO escribio nada.** Es exactamente para lo que la guarda
existe, y es la **misma especie** que la averia 7.5 de la vuelta 65.

### 7.3 **CORRI EL CENSO DE DUPLICADAS ANTES DE RECOMPILAR Y EL DIFF SALIO VACIO**

Mi primer diff de duplicadas comparo **dos cortes tomados los dos DESPUES de fundir pero ANTES de
`run_phase1`**, cuando `master_graph.json` todavia decia **3.262 vivos**: dio *cero fabricados* **por
vacuidad**, no por merito. **La cace mirando que el censo seguia diciendo 3.262 vivos con 15 nodos ya
muertos.** Rehecho con **la apertura sacada de `git show`** contra el cierre **posterior a la
recompilacion**, da **cero fabricados de verdad, con 3 renombrados y 4 idos explicados**.

---

## 8. PENDIENTES DE DOCTRINA Y PREGUNTAS

1. **QUE HACE UN ACTO CUANDO `P.5` CONTESTA *DOS FAMILIAS* Y `P.10` NO SE DISPARA?** (nuevo, y es el
   grande de esta vuelta). **La letra no lo dice.** `P.10` define un disparador **mecanico** que aqui
   **no se cumple** (cero `D` internos), y `P.5` define una **pregunta** cuya respuesta negativa
   **no tiene consecuencia escrita**. Registro **lo mejor sostenido** (el carril del `DECLARADO Y NO
   FUNDIDO CON MOTIVO SELLADO`, que ya existe para `P.10` y que el acta 65 extendio a la guarda `1B`)
   y **lo subo**. **No paro**, por la regla 5: nada se toca y es reversible entero.
2. **UNA COLISION QUE FABRICA UNA FUSION DE `OP-U-02`, QUIEN LA HEREDA?** (nuevo). Se la asigno a
   `OP-U-02` porque **la fabrico ella**, pero el carril escrito solo habla de **la operacion DUENA
   DEL ACTO** al que pertenecen los puestos, y esos puestos son de `core`. **Pendiente nombrado.**
3. **EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE** (heredado, acta 65 pendiente 2): **tres actos mas
   de este lote lo esperan** (el 5 por otra via, y el 10 y el 11 por puente). Sigue enrutado al
   **cierre de la fase 03**.
4. **EN UN ACTO N-ARIO SIGUE SIN HABER MARCA PARA *YA LO DICE EL `APPEND` DE UN HERMANO*** (heredado,
   acta 65 pendiente 4): **esta vuelta lo pago SIETE veces** con `CUBIERTO` mas atenuante declarado.
   **El carril alcanza, pero la cuenta crece.**
5. **EL `INCISO` DE CONDICIONES SIGUE SIN EXISTIR** (heredado): **doce perdidas `DE CONDICIONES` mas**
   en esta vuelta, enrutadas a la fase 04 por el carril del acta 55, pregunta 5.
6. **EL ESQUEMA DE `OPERACIONES.jsonl`** (heredado): sigue pendiente y el campo existente lo cubre. La
   correccion de la TAREA 1.b **no estreno ninguna clave**.

---

## 9. RUTAS TOCADAS Y CENSOS AL CIERRE

**Del grafo (65 ficheros):** los **tres supervivientes** (`six_sigma_dmaic`,
`cierre_segun_complejidad_venta`, `marco_analisis_mercado_cadena_suministro`), sus **quince
absorbidos**, los nodos **redirigidos** por el alias nuevo, mas `dataset/metadata/master_graph.json`
y `dataset/metadata/phase1_run_log.json`.

**Del registro:** `docs/plan/03_FUSIONES.md` (**`+118`** del acta 65 y **`+398`** del lote B, **cero
borradas en los dos**), `docs/plan/OPERACIONES.jsonl` (**una linea**), `docs/plan/ARISTAS_DUPLICADAS.jsonl`,
`docs/COSTURAS_INTERNAS.jsonl` y su resumen, y `web/lib/assets/` por el `sync`.

**Instrumentos nuevos o corregidos:** `scripts/loop/vuelta66_registrar_acta65.py`,
`scripts/loop/_v66_texto_acta65.py`, `scripts/loop/vuelta66_correccion_ficha_opu02.py`,
`scripts/loop/_v66_lote_b.py`, `scripts/loop/vuelta66_registro_lote_b.py`,
`scripts/loop/varas_n_arias_del_tramo.py`, `scripts/loop/vuelta66_caso_positivo_varas.py`,
`scripts/loop/vuelta58_varas_tramo.py` (corregido) y
`scripts/loop/caso_positivo_del_contrato_de_perdidas.py` (corregido).

| censo al cierre | valor |
|---|---|
| **barrido de titulos** ([`SALIDA_V66_BARRIDO.txt`](SALIDA_V66_BARRIDO.txt)), **re-corrido al cierre** | **437 ficheros, `ROJO` 32** (linea base heredada, **sin mover**), **`AMBAR` 0**, `ROTULADO` 40, `CENSO` 222, `ILEGIBLE` 1 |
> **EL BARRIDO DE CIERRE SACO UN `AMBAR` NUEVO Y NO SE DEJO PASAR** (regla 1: el estado al cierre se
> mide al cierre). `vuelta66_registro_lote_b.py` **declara vuelta 66 y su cabecera dice VUELTA 65**, y
> el barrido dice con todas sus letras que **el no decide si eso es procedencia o cita envejecida**.
> **ES PROCEDENCIA**: la cabecera nombra la vuelta 65 porque **es la vuelta que adoso la cabecera de
> tramo bajo la que este registro se cuelga**, cotejada hoy en la **linea 3732**. Se rotula por el
> carril que la casa ya usa (`ROTULO titulo especie=PROCEDENCIA cita=vuelta:65` con su fuente y su
> literal de prueba, igual que `vuelta66_registrar_acta65.py`): **re-corrido, `AMBAR` vuelve a 0** y
> **`ROTULADO` pasa de 39 a 40**, con la procedencia **COTEJADA POR MAQUINA**. **`ROJO` sigue en 32,
> la linea base heredada sin mover.**

| **censo de plantillas talladas** ([`SALIDA_V66_CENSO_PLANTILLAS.txt`](SALIDA_V66_CENSO_PLANTILLAS.txt)) | **CERO TALLADOS** sobre **23** instrumentos de nombre estable |
| **estado de las operaciones** ([`SALIDA_V66_CIERRE.txt`](SALIDA_V66_CIERRE.txt)) | **71**, todas `LISTA`, **0** dependencias rotas, **672** entradas, enlaces **17.540** |
| **casos positivos sobre sujetos que esta vuelta NO toca** | mesa: **LAS NUEVE MUERDEN** sobre `OP-M-02-ACCLIMATE`; promesas: **VERDE en sus dos mitades**; contrato de perdidas: **LAS CUATRO** tras su correccion |

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

**Corte de todas estas cifras: 20 ago 2026, puesto 3.388.**

---

## 10. LO QUE QUEDA DEL TRAMO, MEDIDO

| | |
|---|---:|
| actos del tramo unico | **47** |
| cerrados por el lote A (vuelta 65) | **2** (el 1 declarado, el 3 fundido) |
| **cerrados por el lote B (esta vuelta)** | **6** (3 fundidos, 3 declarados) |
| **quedan** | **39 actos** |
| nodos que quedan | **139** (176 menos los 37 de este lote) |
| de los que quedan, con nodo puente al cierre | **6** (actos 17, 20, 21, 23, 24 y 27) |

**NO SE FUNDIO NINGUN ACTO CON DUENO** (los 6 de fuera siguen fuera), **no se toco la mesa `OP-M-03`
ni sus dos colisiones**, y **las cinco fichas `OP-M-02` consumidas no se ejecutaron**: lo consumado no
se ejecuta ni se rehace.

---

## 11. CONDICIONES DE PARADA, RECORRIDAS

| condicion | se cumple? |
|---|---|
| doctrina nueva inventada | **NO**: los doce discutibles y los seis pendientes quedan bajo letra citable (`P.5`, `P.8`, `P.10`, `P.11`, `P.12`, `P.16`, guarda `1B`, banco 9.10 y 9.21, actas 53, 54, 55, 61, 63, 64 y 65). **Lo que no tiene letra va como PENDIENTE, no como regla** |
| contradiccion sin regla de correccion | **NO** |
| decision de fundador | **NINGUNA SE TOMA**: el merge sigue siendo suyo y no se autoriza ninguna lectura nueva |
| fallo tecnico repetido | **NO**: Gate 0 y las tres suites en verde |
| campana consumada | **NO**: quedan **39 actos y 139 nodos** del tramo, la mesa `OP-M-03` y las fases 04 en adelante |
| credenciales | no hicieron falta |

---

## 12. HASH FINAL Y COMMITS

**Los dos commits de trabajo de esta vuelta, escritos en la rama `pasada-unica`:**

| commit | que lleva |
|---|---|
| **`fa1c3226`** | **TAREA 1 entera**: el registro del acta 65 (`+118`, `0` borradas, 47 citas y 0 malas) y la correccion declarada de la ficha de `OP-U-02` (una linea, cero claves nuevas, estado sin mover) |
| **`eedd7fa1`** | **TAREA 2**: el lote B ejecutado (3 fusiones, 3 declarados, 15 nodos muertos, `P.16` limpio, colisiones que calzan, Gate 0 con su ciclo de tres y las tres suites en verde) |

| **`24ca8ca3`** | **el reporte y el registro del lote B** (`+398`, `0` borradas, citas 8 de 8, idempotencia mordiendo) |

**EL HASH FINAL DE LA VUELTA ES ESTE FICHERO ESCRITO POR SU CUARTO COMMIT**, y por eso se escribe
aqui **en una edicion posterior**: **un commit no puede contener su propio hash**. **Los TRES
anteriores estan arriba, leidos hoy con `git log --oneline`**, y el cuarto **es el que escribe esta
misma linea**. Es la misma via que la vuelta 65 uso.

**LAS DOS GUARDAS DE CIERRE, RE-CORRIDAS TRAS ESTA EDICION** (regla 1: lo que la propia vuelta mueve,
se remide antes de publicar):

| guarda | comando | resultado |
|---|---|---|
| **la cabecera se talla, no se teclea** | `tallar_cabecera_reporte.py --vuelta 66 --comparar docs/loop/REPORTE.md` | **`CABECERA: IDENTICA AL TALLADOR`**, 14 filas cotejadas, **DISTINTAS 0**, ausentes 0 ([`SALIDA_V66_CABECERA_COMPARADA.txt`](SALIDA_V66_CABECERA_COMPARADA.txt)) |
| **las promesas de marcado, por maquina** | `comprobar_promesas_de_marcado.py --reporte docs/loop/REPORTE.md --plan docs/loop/PLAN_V66_OPU02_LOTE_B.json` | **1 promesa, 1 CUMPLIDA, 0 INCUMPLIDAS** ([`SALIDA_V66_PROMESAS.txt`](SALIDA_V66_PROMESAS.txt)) |

**Cero guiones largos y cero guiones medios**, contados por maquina sobre el fichero entero.
