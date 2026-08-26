# REPORTE DE LA VUELTA 68: EL LOTE D DEL TRAMO UNICO DE `OP-U-02`, DOS FUSIONES, CUATRO DECLARADOS Y EL ESTRENO DEL `ABIERTO EN TRANSITO`

**Fase III, ejecucion continua. Rama `pasada-unica`. 26 ago 2026.**

**FECHA POR DOS RELOJES, CORRIDOS POR MI, Y ESTA VEZ CALZAN:** el reloj del sistema da **2026-08-26**
y `git log -1 --date=format` sobre el ultimo commit da **2026-08-26**. **Toda cifra de este reporte
tiene ese corte.** La vuelta abrio con el arbol limpio en `bd1529b3` y sin cruzar medianoche.

---

## 1. LA CABECERA, TALLADA Y NO TECLEADA

**Generada entera con** `python scripts/loop/tallar_cabecera_reporte.py --vuelta 68` y **pegada sin
tocar una celda** ([`SALIDA_V68_CABECERA.txt`](SALIDA_V68_CABECERA.txt)). **La celda que no salga de
un instrumento no se escribe.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.243 / 610 / 17.555 | **3.853 / 3.237 / 616 / 17.562** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 319 / 232 | **551 / 325 / 226** |
| actos (componentes) | 74 | **72** |
| actos `CERRADOS` / `ABIERTOS` | 26 / 48 | **26 / 46** |
| nodos en `CERRADOS` / `ABIERTOS` | 61 / 207 | **61 / 199** |
| cola de costuras | 1.448 | **1.447** |
| colisiones de clase vigentes | 4 | **4** |
| auto-pares (los dos lados al mismo vivo) | 261 | **263** |
| duplicadas historicas: grupos / nodos | 914 / 724 | **913 / 723** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (268 igual a 268; 232 igual a 232) | **TODAS OK (260 igual a 260; 226 igual a 226)** |

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION** (regla 1): los seis instrumentos de apertura
corrieron con el arbol limpio en `bd1529b3`, **antes de escribir nada**, y `git status --porcelain`
tras correrlos dio **CERO ficheros rastreados movidos** (solo las siete salidas nuevas, sin
trackear). **EL CIERRE SE RECOMPUTO AL CIERRE**, despues de que las dos fusiones y `run_phase1`
movieran el arbol.

**LA APERTURA DE HOY CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 67 PUBLICO**, y lo digo porque es la
prueba de que entre las dos vueltas nadie movio dato. **Comparado por maquina, fichero a fichero y
con los saltos de linea normalizados:** el marcador, la cola y las duplicadas salen **IDENTICOS
byte a byte** a las salidas de cierre de la 67; el estado sale identico **salvo la etiqueta**
(`CIERRE` contra `APERTURA`, que es el argumento del propio instrumento); el censo de colisiones
sale identico **salvo la linea de `CUENTA ESPERADA`**, que la corrida de la 67 pidio con
`--esperadas` y la de apertura no; y el recomputo sale identico **salvo la ruta del `jsonl` que
escribe**. **Las cuatro diferencias son de argumento, no de dato, y van dichas una a una en vez de
resumidas en un calza.**

---

## 2. TAREA 1: EL REGISTRO DEL ACTA 67, LA CORRECCION DE LA CITA Y EL ENSANCHE DE LA GUARDA

`python scripts/loop/vuelta68_registrar_acta67.py`
([`SALIDA_V68_REGISTRO_ACTA67.txt`](SALIDA_V68_REGISTRO_ACTA67.txt)), adosado al final de
[`../plan/03_FUSIONES.md`](../plan/03_FUSIONES.md) **sin reescribir ni una linea de arriba**
(`git diff --numstat`: **`187 0`**).

### 2.1 **LO QUE QUEDA REGISTRADO** (apartados a) a h) de la seccion nueva)

- **LA CAIDA DE CIFRA PUBLICADA DEL EJECUTOR CON SU NOMBRE Y SU MEDICION**, la racha de clase o
  cifra **ROTA en la duodecima** y **EL CONTADOR DE PARADA EN UNO**, escrito con esas letras porque
  manda sobre esta vuelta.
- **LOS QUINCE DISCUTIBLES `A FAVOR`** con su vara citada y su linea, con el **`D1` marcado por
  extension citable**.
- **EL CUARTO MOTIVO SELLADO** del `DECLARADO Y NO FUNDIDO` (un veredicto `D` directo interno que la
  fusion entera desmentiria), **con sus CUATRO letras copiadas de sus lineas**, y **la respuesta a
  la pregunta del ejecutor**: la lista de motivos **no es cerrada**, es la enumeracion de lo
  adjudicado hasta su fecha.
- **EL TRANSITO DEL `EMPATE SIN VARA`** en **cinco pasos numerados**, con `DECLARADO Y NO FUNDIDO`
  **reservado a motivos sellados**.
- **LA NOTA DE DICTADO DEL PUESTO 1030**: la sustancia **medida** (los seis pares del puro, los seis
  en `A`), la atribucion literal **suelta y dicha**, **sin contarse como caida**.
- **LOS PENDIENTES 3 A 6 CON SU DESTINO**, el cierre de la fase 03 donde la parada de `AUDITOR.md`
  espera al fundador; y **los pendientes 1 y 2 dichos como YA ADJUDICADOS** para que su ausencia de
  la tabla no parezca omision.

### 2.2 **LA CORRECCION DECLARADA DE LA CITA** (banco 9.10, dentro del mismo registro)

| | lo que la correccion dice, y como se midio |
|---|---|
| **lo que se declara** | la **linea 4563** de `03_FUSIONES.md` dice que la frase envejecida *cuya linea base sigue en `2`* vive en la **4055** |
| **el texto viejo** | **citado VERBATIM y NO tecleado**: el registrador **copia las tres lineas del parrafo desde el fichero** con la marca `[[VERBATIM:CLAVE:3]]` y las pega como cita en bloque |
| **lo que NO se hace** | **no se tacha ni una letra**, y el parrafo viejo se queda donde esta |
| **lo medido** | la frase vive en las **lineas 4073 a 4075**, y el fragmento *linea base sigue* esta en la **4074** |
| **lo que hay de verdad en la 4055** | **la cabecera del apartado e)** del registro del acta 65 |
| **como se prueba la parte negativa** | con una **AGUJA NEGATIVA**: el instrumento comprueba, antes de escribir, que la linea 4055 **NO contiene** *linea base sigue*. **Las dos negativas dieron `OK`** |
| **lo que la correccion NO toca** | **la aritmetica del censo**: las colisiones siguen en **4** con su duena, y la declaracion de ENVEJECIDA sigue en pie |

### 2.3 **EL ENSANCHE DE LA GUARDA DE CITAS DEL REGISTRADOR** (TAREA 1.c)

**EL TEXTO VIEJO DE LA GUARDA QUEDA VERBATIM Y SIN TACHAR EN EL DOCSTRING**, y debajo va **por que
no alcanzaba, medido**: la guarda de la vuelta 67 cotejaba **las citas de una LISTA**, no las citas
del **TEXTO**. Tenia la 4055 en su lista con la aguja *LOS PENDIENTES 2 Y 4* y dijo `OK`, porque ahi
esta; **lo que nadie miro es que la PROSA usaba ese mismo numero para otra afirmacion**.

**LAS DOS CONDICIONES DEL ACTA 61 ESTAN CUMPLIDAS: enumeradas en el docstring y marcada discutible
en este reporte (`D1`).** Lo que la guarda hace ahora:

| condicion | como muerde | medido en esta vuelta |
|---|---|---|
| **1. LAS CITAS SE DERIVAN POR AGUJA, NO SE TECLEAN** | el texto lleva marcas `[[CLAVE]]`; cada clave es un par (fichero, **aguja de CONTENIDO**); el instrumento **busca** la aguja, exige que aparezca **EXACTAMENTE UNA VEZ** (en el fichero o en una ventana anclada) y sustituye | **64 agujas** derivadas en el registro del acta, **16** en el del lote, **cero tecleadas** |
| **2. EL TEXTO NUEVO SE COTEJA ANTES DE ESCRIBIR** | ya sustituido, se barre el texto FINAL buscando la forma canonica y se exige que **cada numero salga de una clave derivada** | **24** citas canonicas en el registro del acta y **10** en el del lote, **MALAS 0** |
| **la red ancha** (anadida sobre lo pedido) | **TODO numero de 3 a 5 digitos en negrita**, tambien los de celda de tabla que no llevan la palabra *linea* delante, tiene que salir de una aguja **o estar declarado uno a uno con su motivo** | **64** numeros en negrita en el registro del acta (3 declarados) y **40** en el del lote |
| **las agujas NEGATIVAS** | una lista de pares (clave, aguja que esa linea **NO** debe contener) | **2**, las dos de la correccion, **las dos `OK`** |
| **cero citas muertas** | toda clave derivada tiene que usarse al menos una vez | **64 de 64** y **16 de 16** |

> **LA GUARDA MORDIO DE VERDAD MIENTRAS SE ESCRIBIA ESTE REGISTRO, y por eso la creo:** en su primera
> corrida saco `ROJO` con **14 fallos** (seis agujas que no eran unicas, dos marcas sin derivar y 37
> citas muertas) y **no escribio nada**. En la del lote D saco `ROJO` con **9** (dos agujas
> ambiguas y cuatro numeros en negrita sin procedencia). **Una guarda que nunca ha fallado no se
> sabe si mide.**

**LAS DOS GUARDAS VIEJAS SIGUEN:** guiones largos y medios **0 / 0** en la pagina entera;
**idempotencia MUERDE** en los dos registradores (`YA ADOSADA` y `YA ADOSADO` en la segunda
corrida); y el **re-cotejo tras adosar** dice **`OK (64 de 64)`** y **`OK (16 de 16)`**.

---

## 3. TAREA 2: EL LOTE D, DECLARADO AL ABRIRLO Y ENTREGADO ENTERO

**EL LOTE ES PREFIJO SIN SALTOS** del `orden_universo` de lo que quedaba del tramo fijado en
[`TRAMO_UNICO_OPU02_V64.jsonl`](TRAMO_UNICO_OPU02_V64.jsonl) (el lote A cerro los actos **1** y
**3**; el lote B el **5**, **7**, **8**, **9**, **10** y **11**; el lote C el **12** al **17**):
**EL PREFIJO 18 A 24, SIETE ACTOS Y 28 NODOS**. **SEIS se declararon para cerrar ENTEROS** y **el
acto 18 se procesa entero y se cuenta APARTE**, por el carril del transito.

| acto | miembros | cierra | motivo | superviviente |
|---:|---:|---|---|---|
| **18** | 4 | **`ABIERTO EN TRANSITO`** | **`EMPATE SIN VARA` y NADA lo detiene** | **ninguno se elige, y esa es la regla** |
| **19** | 4 | **FUNDIDO** | `CONTENIDO EMPATA`: decide el cableado solo (`P.8`) | `division_trabajo_humano_ia` |
| **20** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, 1 puente y 1 triangulo | ninguno se elige |
| **21** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, 2 puentes y 2 triangulos | ninguno se elige |
| **22** | 4 | **FUNDIDO** | `UNA SOLA VARA` de pasos; el cableado apunta al otro y **no habla** | `comprension_capacidades_limitaciones_ia` |
| **23** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, 1 puente y 1 triangulo | ninguno se elige |
| **24** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, 2 triangulos, **la figura `ESTRELLA`** y **el dueno `OP-S-07`** | ninguno se elige |

> **LOS CUATRO DECLARADOS CIERRAN LOS CUATRO POR EL MISMO MOTIVO, EL TRIANGULO DE `P.10`**, que es el
> **primero** de los cuatro motivos sellados. **Ni la guarda `1B` ni la respuesta de `P.5` se
> necesitaron en ningun acto de este lote: las dos pasan por vacio y se dice.**

### 3.1 **`P.5` CONTESTADA ACTO POR ACTO, SOBRE EL TEXTO ESTABLE**

**El acto se leyo ENTERO** con `python scripts/loop/dossier_del_tramo.py --tramo
docs/loop/TRAMO_UNICO_OPU02_V64.jsonl --actos 18,19,20,21,22,23,24`
([`SALIDA_V68_DOSSIER_LOTE_D.txt`](SALIDA_V68_DOSSIER_LOTE_D.txt), **600 lineas**), con **todos sus
pares internos y su razon entera**.

| acto | libro o libros | pares `A` | pares `D` | puentes | triangulos | puertas | **una familia o dos** |
|---:|---|---:|---:|---:|---:|---:|---|
| **18** | Esty (los 4) | 3 | 0 | 0 | 0 | 0 | **UNA**, y la declara el archivo: el **1871** la ve pasar de dos a tres y el **1903** de tres a cuatro |
| **19** | Mollick (3) y Hugos | 3 | 0 | 0 | 0 | 0 | **UNA**, y el **1597** la nombra entera con sus cuatro miembros |
| **20** | Hugos (los 4) | 3 | **1** | **1** | **1** | 0 | **UNA, pero MEZCLADA**: el `D` la detiene |
| **21** | Deming (los 4) | 3 | **2** | **2** | **2** | 0 | **UNA, pero MEZCLADA** con DOS `D` |
| **22** | Mollick (los 4) | 3 | 0 | 0 | 0 | 0 | **UNA**, y es **el bloque de CUATRO de una particion escrita** |
| **23** | Feld, Wasserman | 4 | **1** | **1** | **1** | 0 | **UNA, MEZCLADA**; el **1371** y el **1436** la cuentan |
| **24** | Blank (los 4) | 3 | **2** | **1** | **2** | 0 | **UNA, MEZCLADA**, y ademas **una FIGURA con centro y periferia** |

**MEDIDO** con `python scripts/loop/vuelta65_puentes_del_tramo.py --tramo ... --detalle`
([`SALIDA_V68_PUENTES_TRAMO.txt`](SALIDA_V68_PUENTES_TRAMO.txt)), **con los ids pasados por el
resolutor (`P.1`)**, y las puertas con `varas_n_arias_del_tramo.py` contra el universo protegido de
**256 ids**.

**Y EL TRAMO ENTERO SE MIDIO HOY, no se heredo del acta:** **47 actos mirados, 9 con al menos un
nodo puente**, y **de los 33 que quedaban al abrir esta vuelta, CINCO traian puente: los actos 20,
21, 23, 24 y 27**, exactamente los que el acta 67 conto. **Cerrados cuatro de ellos, queda UNO.**

### 3.2 **LAS VARAS POR FORMA, CON SU LETRA Y MEDIDAS POR INSTRUMENTO**

`python scripts/loop/varas_n_arias_del_tramo.py --tramo ... --actos 18,19,20,21,22,23,24`
([`SALIDA_V68_VARAS_N_ARIAS.txt`](SALIDA_V68_VARAS_N_ARIAS.txt)). **Formas del prefijo: 1 `EMPATE SIN
VARA`, 3 `CONTENIDO EMPATA` y 3 `UNA SOLA VARA`.**

| acto | **FORMA medida** | a que lado apunta | **la letra que decide** |
|---:|---|---|---|
| **18** | **`EMPATE SIN VARA`** | pasos **4 a cuatro bandas**, condiciones **2 a cuatro bandas**, **cableado empatado en 3** | **nadie decide: va al auditor por `P.8`**, y el acto queda `ABIERTO EN TRANSITO` |
| **19** | `CONTENIDO EMPATA` | el cableado apunta a `division_trabajo_humano_ia` (4 contra 3) | **el cableado DECIDE SOLO**, que es el unico supuesto en que `P.8` le da la palabra |
| **20** | `UNA SOLA VARA` | pasos a `efecto_bullwhip` (6 contra 5); el cableado al OTRO | **no llega a aplicarse: `P.10` detiene ANTES** |
| **21** | `CONTENIDO EMPATA` | el cableado a `relacion_largo_plazo_proveedor_unico` (6 contra 3) | **no llega a aplicarse: `P.10` detiene ANTES** |
| **22** | `UNA SOLA VARA` | pasos a `comprension_capacidades_limitaciones_ia` (5 contra 4); condiciones empatan en 2 | **funde a su lado**. **El cableado apunta al OTRO** (`jagged_frontier_ia`, 7 contra 3) **y NO HABLA**, porque `P.8` es regla de PRELACION |
| **23** | `CONTENIDO EMPATA` | el cableado a `employee_pool_esop` (5 contra 4) | **no llega a aplicarse: `P.10` detiene ANTES** |
| **24** | `UNA SOLA VARA` | pasos **y** cableado a `diseno_experimentos_pass_fail` (6 contra 5; 8 contra 5) | **no llega a aplicarse: `P.10` detiene, la figura tambien, y ademas el acto TIENE DUENO** |

**EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN**, y **ninguna vara se teclea**: las tres cuentas por
miembro salen del instrumento.

### 3.3 **LAS DOS FUSIONES, EN CIFRAS DEL INSTRUMENTO**

`python scripts/loop/fundir_por_plan.py --plan docs/loop/PLAN_V68_OPU02_LOTE_D.json --ejecutar`
([`SALIDA_V68_FUSION_LOTE_D.txt`](SALIDA_V68_FUSION_LOTE_D.txt)), **precedida de la simulacion sobre
copia en memoria** ([`SALIDA_V68_FUSION_SIMULADA.txt`](SALIDA_V68_FUSION_SIMULADA.txt)).

| | acto 19 | acto 22 | **el lote** |
|---|---:|---:|---:|
| absorbidos | 3 | 3 | **6** |
| pasos del superviviente | 4 a **7** | 5 a **9** | |
| condiciones | 2 a **5** | 1 a **3** | |
| piezas repartidas | 17 | 17 | **34** |
| de ellas `APPEND` / `CUBIERTO` / `INCISO` | 6 / 11 / **0** | 6 / 9 / **2** | **12 / 20 / 2** |
| perdidas selladas en campo propio | 6 | 5 | **11** |

**TOTAL: 6 nodos mueren (3.243 vivos a 3.237). Ficheros tocados: 15. Redirecciones sobre nodos
vivos: 11.**

**LAS GUARDAS DE CADA FUSION, LAS CUATRO Y TODAS VERDES:** guarda 1 (miembros vivos y nomina
completa), guarda **1B** (ningun absorbido es semilla ni extremo de puente), guarda 2 (cobertura
exacta de indices, cero olvidos) y guarda 3 (cero repetidos literales). **Los DOS `INCISO` del acto
22 se EXTRAJERON del nodo y se comprobaron VERBATIM**, y sus pasos resultantes estan impresos:

- al paso 2: *Prueba la IA en los casos límite (edge cases) que más importan en tu negocio, con casos
  reales y variados, no solo con ejemplos fáciles*
- al paso 5: *Ajusta la instrucción que le das a la IA o la forma de trabajar según lo que vayas
  descubriendo, hasta encontrar la forma óptima de uso para esa tarea específica*

**CERO `INCISO` EN EL ACTO 19, Y ES POR LA PUNTUACION** (carril del `D5` del acta 66): **los cuatro
pasos de su superviviente terminan en punto**, y un `INCISO` con nexo de coma detras de un punto cae
en la guarda de la **JUNTURA ROTA** del generador. **No se forzo ninguno.**

**`P.16`, QUIEN FABRICA LIMPIA, EN EL MISMO COMMIT:** la fusion fabrico **1** duplicada y **la limpio
en la misma corrida**; **1 auto-arista** retirada; **guarda A** (cero auto-aristas nuevas) **OK**,
**guarda B** (cero duplicadas nuevas tras resolver) **OK**, **guarda C** (los campos que esta
operacion no redacta, intactos: **10 de 10**) y **guarda D** (los 6 absorbidos conservan su texto
**INTACTO**) **OK**. El pasivo del censo propio de la guarda **baja 1** (891 a 890).

**`reanclar_por_resolutor.py` corrido ENTRE la fusion y `run_phase1`**
([`SALIDA_V68_REANCLAJE.txt`](SALIDA_V68_REANCLAJE.txt)): **NADA QUE RE-ANCLAR**, y **se dice por que
en vez de dejarlo como un cero mudo**: el propio fundidor ya habia redirigido **las 11 referencias
vivas** a los absorbidos, asi que cuando el reanclador llego no quedaba ninguna. **Se corrio igual,
que es lo que la guarda pide.**

### 3.4 **EL DIFF DE DUPLICADAS, POR INSTRUMENTO Y CON LA APERTURA SACADA DE `git`**

`python scripts/loop/diff_duplicadas_por_resolutor.py --antes <git show 2bd639c7:...> --despues
docs/plan/ARISTAS_DUPLICADAS.jsonl`
([`SALIDA_V68_DIFF_DUPLICADAS.txt`](SALIDA_V68_DIFF_DUPLICADAS.txt)).

> **GRUPOS FABRICADOS DE VERDAD: `0`.** **RENOMBRADOS: `0`.** Hay **1 que DESAPARECE**
> (`division_trabajo_humano_ia` en `nodos_siguientes` hacia `search_for_business_model`), y **esta
> explicado**: era un grupo del absorbido `descomposicion_tareas_trabajo` que la fusion deduplico al
> unir los `nodos_siguientes`. **914 grupos a 913.**

**EL CORTE DE *ANTES* SALE DE `git show` SOBRE EL COMMIT DE LA TAREA 1** (`2bd639c7`), **anterior a
la fusion**, y el de *despues* es el fichero **tras recompilar**. **UNA AVERIA PROPIA QUE ESTA MEDIDA
Y VA DICHA:** mi primera corrida del censo de duplicadas fue **antes** de `run_phase1` y leyo el
grafo viejo (dio 914 sobre 3.243 vivos); **re-corrida despues del Gate 0** da **913 sobre 3.237**,
que es la cifra que se publica. **Ninguna version de la primera corrida entro en este reporte.**

### 3.5 **EL CENSO DE COLISIONES: ESPERADAS MEDIDAS ANTES DE FUNDIR SOBRE LA BASE `4`, Y CALZA**

`python scripts/loop/vuelta65_colisiones_esperadas.py --plan docs/loop/PLAN_V68_OPU02_LOTE_D.json
--base 4` ([`SALIDA_V68_COLISIONES_ESPERADAS.txt`](SALIDA_V68_COLISIONES_ESPERADAS.txt)), **corrido
sobre el arbol de antes y simulando en memoria, sin tocar un nodo**.

| | |
|---|---:|
| linea base declarada **y MEDIDA sobre el arbol de antes** | **4** |
| **colisiones NUEVAS que la fusion fabricaria** | **0** |
| colisiones que desaparecerian | 0 |
| **ESPERADAS TRAS FUNDIR** | **4** |
| **MEDIDAS al cierre por el censo** | **4** |
| **`CALZA`** | **`SI`**, y son **LAS MISMAS CUATRO** |
| auto-pares nuevos, predichos y medidos | **2** predichos (261 a 263) y **263** medidos al cierre |

**Las dos de la mesa `OP-M-03` no se tocan y las dos de `OP-U-02` siguen vigentes con su duena.**
**El defecto de `--base` ya vale `4` desde la correccion declarada de la vuelta 67**, y aun asi
**se paso `--base 4` a mano**: la guarda **mide** la base sobre el arbol y cae en `ROJO` si no calza
con la declarada.

### 3.6 **GATE 0 CON SU CICLO DE TRES, Y NO DE CUATRO**

| paso | resultado |
|---|---|
| `python scripts/run_phase1.py --reaplico-curaduria` | **`GATE 0: OK`**, todos los chequeos en `[OK]`; universo **3.237 activos / 616 deprecados**; alcanzabilidad **100,0 por ciento** |
| `python scripts/etiquetas_de_cara.py --aplicar` | **71 etiquetas** re-aplicadas |
| `python scripts/sync_assets_web.py` | **6 assets** mas `manifest.json` |
| **una cuarta corrida** | **NO SE HIZO** |

**LAS TRES SUITES, CORRIDAS POR MI:** motor **25/25**
([`SALIDA_V68_SUITE_MOTOR.txt`](SALIDA_V68_SUITE_MOTOR.txt)); web **80 ficheros, 1.030 pasadas, 3
saltadas** ([`SALIDA_V68_SUITE_WEB.txt`](SALIDA_V68_SUITE_WEB.txt)); `tsc --noEmit` **CERO lineas**
([`SALIDA_V68_TSC.txt`](SALIDA_V68_TSC.txt)). **Y el guardian de commit las volvio a correr en verde
en los tres commits de trabajo de esta vuelta.**

### 3.7 **EL REGISTRO EN `03_FUSIONES.md`** (`+354` lineas, `0` borradas)

`python scripts/loop/vuelta68_registro_lote_d.py`
([`SALIDA_V68_REGISTRO_LOTE_D.txt`](SALIDA_V68_REGISTRO_LOTE_D.txt)), **bajo la cabecera de tramo que
la vuelta 65 adoso** (derivada hoy por aguja) y **sin reescribir ni una linea de arriba**
(`git diff --numstat`: **`354 0`**).

**NINGUNA TABLA TECLEADA Y NINGUNA CITA TECLEADA:** el reparto pieza a pieza y las piezas por
absorbido **se generan del plan sellado**; **las CUATRO fichas de los declarados** tambien; la de
perdidas **se recorta de la salida del tallador leyendo la columna `acto` por su sitio**; y **las 30
celdas** de guardas, colisiones, Gate 0 y censos **se extraen por aguja**. **Idempotencia MUERDE.**

**EL UNICO CAMBIO SOBRE LA MAQUINA COPIADA DEL REGISTRADOR DE LA VUELTA 67, Y VA DICHO EN SU
DOCSTRING:** `tabla_declarado` **imprime ademas LOS DUENOS MEDIDOS** del acto. El acto 24 trae
`OP-S-07` en `duenos_cualquier_operacion`, y **esa es una razon de cierre que la prosa no deberia
ser la unica en decir**.

### 3.8 **LA PARTICION DEL RACIMO DE LA SUPERVISION DE LA IA, MEDIDA Y NO CRUZADA**

**Es la pieza mas delicada de la vuelta y por eso va en su propio apartado.** El `acto 22` que esta vuelta funde
**pertenece a un racimo del inventario**, y ese racimo **tiene una particion escrita**.

| | medido hoy |
|---|---|
| **la entrada** | `INVENTARIO.jsonl`, `tipo: racimo`, nombre **la supervision de la IA**, **nomina de DIEZ**, `forma: PARTIDO 5 mas 4 mas 1`, `estado: en mesa, particion PROVISIONAL`, corte **2026-08-13**, **`operaciones: []`** |
| **el bloque de CINCO** | **el `acto 11` del tramo**, que **ya cerro `DECLARADO Y NO FUNDIDO` por `P.10`** en la vuelta 66, y cuyo puesto **1541** dejo escrito que **la particion escrita NO se mueve** |
| **el bloque de CUATRO** | **este `acto 22`** |
| **el UNO** | `comprender_alineacion_etica_ia`, **el suelto**, que `04_ENLACES.md` manda a **mesa** por ser suelto de un racimo **sin centro** |
| **la suma** | **5 mas 4 mas 1**, y **CALZA con el campo `forma`** ([`SALIDA_V68_PARTICION_RACIMO.txt`](SALIDA_V68_PARTICION_RACIMO.txt)) |

> **ESTA FUSION OPERA DENTRO DE UN BLOQUE Y NO CRUZA NI UNA DE LAS DOS FRONTERAS.** Ni toca al bloque
> de cinco (que ya esta declarado y vivo entero), ni toca al suelto (que va a mesa).
>
> **LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO** (regla 2): el campo `estado` dice **en
> mesa**, y **medido hoy** el acto tiene **los dos campos de dueno VACIOS** y **el campo
> `operaciones` de la propia entrada del racimo tambien esta vacio**, o sea que **ninguna operacion
> lo reclama**. El criterio con el que `OP-U-02` abrio su universo es **el dueno medido**. **Es el
> mismo carril con el que el acto 17 de la vuelta 67 trajo el puesto 460 como contraste. VA MARCADO
> DISCUTIBLE (`D2`).**

---

---

## 4. EL `ACTO 18`, `ABIERTO EN TRANSITO`: EL CASO ENTERO, COMO EL CARRIL PIDE

**El acta 67 adjudico que un acto con forma `EMPATE SIN VARA` ni se declara ni detiene el lote**, y
que si nada lo detiene el ejecutor **NO elige superviviente**: **escribe el caso entero aqui**, lo
marca discutible, y el acto queda **fuera de la cuenta de cerrados**. **Esto es ese caso.**

### 4.1 **NADA LO DETIENE, Y SE DICE ANTES QUE NADA**

| guarda o motivo | resultado medido |
|---|---|
| **`P.10`** | **NO se dispara**: **cero** pares `D` internos, **cero** nodos puente, **cero** triangulos |
| **guarda `1B`** | **pasa por vacio**: **NINGUN** miembro es puerta |
| **`P.5`** | **contesta UNA familia**, o sea que el motivo sellado del acta 66 tampoco aplica |
| **el `D` directo interno** (cuarto motivo) | **no existe**: cero `D` |
| **duenos** | **los DOS campos VACIOS**, medidos hoy sobre el fichero fijado |
| **colisiones** | ninguna de las cuatro vigentes toca a este acto |

> **Sin motivo sellado que invocar, `DECLARADO Y NO FUNDIDO` esta prohibido**: queda reservado a
> motivos sellados, y *el auditor aun no contesta* **no es un motivo, es una pregunta en viaje**.

### 4.2 **LA RESPUESTA DE `P.5`, CON EL ARCHIVO DELANTE**

**ES UNA FAMILIA, y la declara el archivo, no yo.** Los cuatro miembros son de la misma fuente (*The
Green to Gold Business Play*, Esty) y los tres pares leidos estan en `A`:

| puesto | par | lo que la razon dice, copiado |
|---:|---|---|
| **1797** | `co_opetition_industria` contra `trabajo_colectivo_estandares_industria` | *LA MISMA ALIANZA ENTRE COMPETIDORES DOS VECES, MISMA FUENTE y sin arista entre ellos. LOS CUATRO PASOS SE CORRESPONDEN* |
| **1871** | `colaboracion_sectorial` contra `trabajo_colectivo_estandares_industria` | *LA MISMA ALIANZA SECTORIAL POR TERCERA VEZ*, y *la familia de la alianza sectorial pasa de DOS a TRES nodos por cierre transitivo* |
| **1903** | `alianzas_cross_industry` contra `colaboracion_sectorial` | *LA MISMA ALIANZA DE INDUSTRIA POR CUARTA VEZ*, y *la familia pasa de TRES a CUATRO nodos por cierre transitivo*. **Cobertura 3 de 6, forma PROVISIONAL** |

### 4.3 **LAS TRES CUENTAS Y EL CABLEADO: EMPATE A CUATRO BANDAS**

| miembro | pasos | condiciones | cableado |
|---|---:|---:|---:|
| `alianzas_cross_industry` | **4** | **2** | **3** |
| `co_opetition_industria` | **4** | **2** | **3** |
| `colaboracion_sectorial` | **4** | **2** | 1 |
| `trabajo_colectivo_estandares_industria` | **4** | **2** | 2 |

**PASOS: empatan los CUATRO en 4. CONDICIONES: empatan los CUATRO en 2. CABLEADO: empatan DOS en 3.**
**Ninguna vara apunta, y el desempate de `P.8` tampoco desempata.** Es la fila de `P.8` que dice
*empatado y el cableado tambien: se trae al auditor*.

### 4.4 **LAS PIEZAS PROPIAS QUE EL ARCHIVO NOMBRA POR CADA MIEMBRO** (lo que `P.8` llama contenido)

| miembro | lo propio, segun las razones leidas | quien lo nombra |
|---|---|---|
| `alianzas_cross_industry` | **los NOMBRES DE LAS COALICIONES EXISTENTES** (*EICC*, *AIM-PROGRESS*), *que es lo que vuelve buscable el paso*; y **el encuadre de PODER DE COMPRA COLECTIVO para mover el mercado hacia otro tipo de producto**, *mas ambicioso que fijar un estandar de conducta* | **1903** |
| `co_opetition_industria` | **convocar MEDIANTE LAS ASOCIACIONES INDUSTRIALES EXISTENTES**, *la unica linea que dice por donde se convoca sin que parezca acuerdo entre competidores*; y **PUBLICAR Y MONITOREAR EL CUMPLIMIENTO COLECTIVO**, *lo unico que le pone consecuencia publica al pacto* | **1797** |
| `colaboracion_sectorial` | **EL TEST DEL PODER DE MERCADO como disparador**, *la unica linea que dice cuando NO hace falta aliarse*; y el apoyo en las asociaciones existentes para convocar | **1871** y **1903** |
| `trabajo_colectivo_estandares_industria` | **el ejemplo con NOMBRE PROPIO del marco de cumplimiento** (*Responsible Care*), *que lo vuelve buscable*; **APLICAR EL ESTANDAR CONJUNTO A LOS PROVEEDORES COMPARTIDOS**, *la unica linea del par que usa la alianza como palanca hacia arriba en la cadena*; y **el encuadre por RIESGO REPUTACIONAL COMPARTIDO** | **1797** y **1871** |

**ROL DECLARADO Y ALCANCE, que es la otra mitad de lo que `P.8` llama contenido:** `colaboracion_sectorial`
es el unico que **empieza preguntandose si hace falta aliarse**; `alianzas_cross_industry` es el
unico que apunta al **mercado entero** y no solo a los proveedores; `co_opetition_industria` es el
unico que **publica y monitorea**; y `trabajo_colectivo_estandares_industria` es el unico que
**baja el estandar a los proveedores compartidos**. **Los cuatro tienen algo que ninguno de los
otros tres tiene, y ninguna vara los ordena.**

> **VA MARCADO DISCUTIBLE (`D6`) Y EL ACTO QUEDA `ABIERTO EN TRANSITO`.** **No elijo superviviente.**
> El auditor lo adjudica en su acta con este caso delante, y **el lote siguiente ejecuta esa fusion
> adjudicada como su primera operacion**.

---

## 5. LOS CUATRO DECLARADOS, EN UNA LINEA CADA UNO

**Los cuatro cierran por `P.10` con su triangulo MEDIDO**, y los cuatro quedan **vivos y enteros**.

- **`ACTO 20`**, el efecto latigo (Hugos). El `D` del puesto **994** dice que uno **mide el problema**
  y el otro **es la inversion que lo cura**, que **ni un paso se solapa** y que es **arista que falta
  de las mas claras**. **Y hay un CHOQUE encima, dicho en vez de callado**: el puesto **730** declara
  que la clase queda en `A` **por la lectura vieja del cero-enlazados** y que **si mandara el
  contenido seria `D`**, y lo deja anotado **en vez de elegir**.
- **`ACTO 21`**, el Punto 4 de Deming. **Es el acto mas mezclado del prefijo** (cinco pares leidos,
  tres `A` y dos `D`). El **2927** avisa con todas sus letras de que los dos extremos **fusionan por
  `A` con el mismo tercer nodo** y de que **quien componga esa cadena sin verificar que es CONTENCION
  en los dos eslabones dira `A`**. **El cierre transitivo junta a los cuatro justamente por la cadena
  que esa lectura dice que NO compone.**
- **`ACTO 23`**, la reserva de opciones. El **1193** separa **NEGOCIACION** de **MECANICA** y cierra
  con que **ese par NO anade miembro: sale sano porque trae calculos propios, y no repeticion**.
- **`ACTO 24`**, la estrella de pass/fail, **con TRES razones independientes**: `P.10` con sus dos
  triangulos; **el ejemplar numero UNO de la figura `ESTRELLA (9.23)` del inventario**, cuyo centro y
  perifericos una fusion entera deprecaria a la vez (y el propio **1346** dice que era **el par que
  decidia** y que al salir `D` **la figura queda CONFIRMADA**); y **el DUENO**, `OP-S-07` en
  `duenos_cualquier_operacion`, medido hoy. **La tercera habria bastado sola sin leer nada, y aun asi
  el acto se leyo entero: un acto con dueno no se salta, se declara con el dueno dicho.**

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D1`. EL ENSANCHE DE LA GUARDA DE CITAS, QUE ES UNA GUARDA QUE CRECE Y ADEMAS CAMBIA EL FORMATO DEL
TEXTO.** El encargo pedia **dos** condiciones y yo puse **cuatro** mecanismos: las dos pedidas, mas
la **red ancha** sobre todo numero en negrita, mas las **agujas NEGATIVAS**, mas **cero citas
muertas**. **Se puede sostener que las dos de mas son alcance**; mi razon es que la caida de la 67
vivia en una celda de tabla **sin la palabra *linea* delante**, que la condicion 2 literal no habria
mirado. **Y el costo es real: el texto editorial ya no se puede leer suelto, porque lleva marcas en
vez de numeros.**

**`D2`. FUNDIR EL `ACTO 22`, QUE ES EL BLOQUE DE CUATRO DE UN RACIMO CUYO INVENTARIO DICE *EN MESA*.**
**Es el mas fuerte de la vuelta y lo se.** Mi lectura es que **el dueno se mide** (los dos campos
vacios, y el propio racimo con `operaciones: []`), que **la particion no se cruza** y que el bloque
de cinco ya cerro declarado. **Leido al reves**, *en mesa* significa que el racimo entero es de la
mesa y este acto no se toca hasta que la mesa hable. **No paro porque nada contradice una regla
vigente ni una cifra publicada**, y porque la particion **calza al digito**; pero **si el auditor lo
lee al reves, esta fusion habria que deshacerla**.

**`D3`. EL SUPERVIVIENTE DEL `ACTO 22` ES EL QUE EL CABLEADO NO ELIGE, Y POR MARGEN GRANDE.** 7 contra
3. **`P.8` dice que el cableado solo habla a contenido empatado y aqui el contenido dice algo (5
pasos contra 4)**, que es exactamente el carril del `D7` del acta 67. **Pero `jagged_frontier_ia` es
un nodo con 3 previos y 4 siguientes, y el que sobrevive tiene 1 y 1**: el grafo pierde el hub y lo
gana por redireccion. **Queda publicado.**

**`D4`. EL NODO DEL `ACTO 22` PASA DE 5 PASOS A 9: ES EL NODO MAS GRANDE QUE ESTE TRAMO HA
PRODUCIDO.** Cuatro `APPEND` de paso. Elegi **catalogo mas rico con solapes declarados** sobre
`CUBIERTO` que calla texto vivo, que es el carril del `D8` del acta 67, **pero un nodo de nueve pasos
es un nodo de nueve pasos** y va dicho.

**`D5`. EL NODO DEL `ACTO 19` PASA DE 2 CONDICIONES A 5, Y LAS TRES NUEVAS SON `APPEND` DE
CONDICION.** El acta 55 (pregunta 5) solo deja pasar una condicion de `APPEND` cuando es **disparador
DISTINTO** y no matiz. **Leo que las tres lo son** (el arranque de la adopcion, armar el equipo y
definir roles, y el miedo a que la IA quite tareas), **pero tres de golpe en un solo acto es la
primera vez del tramo** y se puede leer como que abri la mano.

**`D6`. EL `ACTO 18` QUEDA `ABIERTO EN TRANSITO` Y NO ELIJO SUPERVIVIENTE.** Es lo que el carril
manda, **y aun asi lo marco**, porque el carril **se estrena hoy** y porque **el lote entrega SEIS
cerrados en vez de SIETE**. Si el auditor prefiere que el ejecutor proponga un superviviente aunque
sea revocable, **este es el sitio donde se ve el costo**.

**`D7`. DECLARAR EL LOTE EN SEIS ACTOS QUE CIERRAN MAS UNO EN TRANSITO.** Al abrirlo **no sabia
cuantos iban a fundirse**; declare **seis** por el tamano de los lotes B y C. **Salieron dos
fusiones**, que es mas que la unica del lote C pero menos que las tres del B. **Se puede sostener
que, visto que cuatro de los seis traian puente y estaban condenados a `P.10`, el lote debio ser mas
largo.** No lo alargue sobre la marcha a proposito.

**`D8`. DOS PERDIDAS CON DOS SEDES EN UN SOLO CAMPO `donde`, UNA EN CADA FUSION.** Es el criterio que
el acta 67 adjudico en su `D10` (**la fila es POR PIEZA, no por sitio**), **y lo aplico por primera
vez sabiendolo**. Con la lectura contraria la cuenta de perdidas seria **13** y no **11**.

**`D9`. CUATRO PERDIDAS CON ATENUANTE DECLARADO, Y DOS DE ELLAS SON DE LA ESPECIE DEL PENDIENTE 4.**
Las dos dicen que **el contenido llega igual por el `APPEND` de un hermano** (`invitar_ia_a_todo` y
`principio_invitar_ia_siempre` son *el mismo principio numerado* por el puesto 456). **Sobre-sellar
declarando es mas auditable que callar**, carril del `D11` del acta 67, **pero la cuenta del
pendiente 4 crece otra vez**.

**`D10`. SELLO UNA PERDIDA QUE EL `INCISO` DEL MISMO ACTO REPARA.** El criterio de parada de la
iteracion se pierde del paso 4 de `principio_invitar_ia_siempre` **y a la vez entra VERBATIM por el
`INCISO` al paso 5**. **La selle igual**, con el atenuante dicho, porque **el sello es del reparto y
no del resultado**. **Se puede sostener que eso infla la cuenta con una perdida que no se pierde.**

**`D11`. UN `CUBIERTO` QUE APUNTA A UN PASO DEL SUPERVIVIENTE CUANDO EL CONTENIDO REAL LLEGA POR UN
`APPEND` DEL HERMANO.** El paso 2 y la condicion 1 de `principio_invitar_ia_siempre` van `CUBIERTO`
al paso 1 y a la condicion 1 del superviviente, **que es donde el archivo dice que estan**, pero **lo
que de verdad los conserva es el `APPEND` de `invitar_ia_a_todo`**. **La marca no existe** (pendiente
4), asi que use la que hay **y lo dije en el campo de la perdida**; **quien lea el reparto sin la
perdida al lado vera un `CUBIERTO` que no cubre.**

**`D12`. LOS DOS `INCISO` DEL `ACTO 22` ENTRAN CON NEXO DE COMA SOBRE PASOS QUE NO TERMINAN EN
PUNTO.** La guarda de la juntura solo salta cuando el paso acaba en punto, y estos no acaban.
**Leidos enteros los dos pasos resultantes, se leen limpios** y estan impresos arriba; **pero un paso
de dos oraciones cosidas por una coma es una decision de redaccion que la fase 04 puede querer al
reves.**

**`D13`. `tabla_declarado` CRECE CON UNA FILA DE DUENOS, SIN ENCARGO.** Nadie me pidio tocar la tabla.
**Lo hice porque el `acto 24` tiene dueno y esa razon de cierre solo vivia en la prosa**, y una razon
que solo vive en la prosa se pierde. **Va enumerada en el docstring** y marcada aqui, que son las dos
condiciones del acta 61. **Se puede sostener que es alcance.**

**`D14`. EL REGISTRADOR DEL LOTE *IMPORTA* LA GUARDA EN VEZ DE COPIARLA, Y ESO ROMPE UN CARRIL DE LA
CASA.** Esta pagina viene copiando literal la maquina de un registrador al siguiente, con el
argumento de que **dos registros no pueden dibujar lo mismo distinto en silencio**. Yo hice lo
contrario con la guarda de citas: **la importo y le pongo mis agujas**, precisamente para que no
puedan separarse. **Se puede sostener que importar acopla dos ficheros de una vuelta** y que si
manana alguien toca el del acta, rompe el del lote sin saberlo.

**`D15`. EL PLAN SE SELLO DOS VECES.** El primer sello no podia citar el fichero de colisiones
esperadas **porque ese fichero se genera A PARTIR del plan**; medidas las colisiones, **volvi a
sellar** para que la cabecera lo citara. **Los dos sellos estan comparados por maquina y difieren en
UNA sola linea, la del campo `colisiones_esperadas`**
([`SALIDA_V68_DIFF_SELLOS.txt`](SALIDA_V68_DIFF_SELLOS.txt)). **Se puede sostener que un plan
sellado no se re-sella**; mi razon es que **el plan no se habia ejecutado todavia** y que la
alternativa era dejar la cabecera diciendo *NO ENTRO NINGUN FICHERO*, que es menos cierto.

**`D16`. LEER ENTERO Y DECLARAR UN ACTO QUE TENIA DUENO, EN VEZ DE SALTARLO.** El `acto 24` trae
`OP-S-07`. **El encargo prohibe FUNDIR un acto con dueno, no leerlo**, y leerlo produjo dos razones
mas y una figura del inventario preservada. **Se puede sostener que un acto con dueno no es de este
lote y que gaste lectura en el.**

---

## 7. LAS AVERIAS PROPIAS, CAZADAS ANTES DE UNA CIFRA PUBLICADA

**CERO de ellas llego a una cifra publicada ni a un dato movido.**

### 7.1 **LLAME A `vitest` CON UN REPORTER QUE NO EXISTE**

Corri `npx vitest run --reporter=basic` y `vitest` 4 **no conoce ese reporter**: `Startup Error`,
`exit 1`, **cero tests corridos**. **Lo vi porque miro los codigos de salida**, que es la leccion de
la averia 7.2 de la vuelta 67. Re-corrido con el comando que la vuelta 67 uso (`npx vitest run`):
**80 ficheros, 1.030 pasadas, 3 saltadas**. **Ninguna salida con la forma rota se publico.**

### 7.2 **EL REGISTRADOR DEL ACTA MURIO EN `ROJO` EN SU SEGUNDA CORRIDA EN VEZ DE DECIR `YA ADOSADA`**

**Y la causa es el propio bloque `VERBATIM`**: al copiar el texto viejo dentro de la seccion nueva,
**la aguja de ese texto pasa a aparecer DOS veces en la pagina**, y la derivacion (que exige
unicidad) caia en `ROJO` antes de llegar a la idempotencia. **Rojo tambien es seguro**, porque no
escribe; **pero la respuesta correcta a una pagina ya registrada es decirlo, no fallar**. Corregido:
**la idempotencia se mira PRIMERO**, y la correccion va dicha en el sitio.

### 7.3 **EL RE-COTEJO DE DESPUES CONTABA LA COPIA `VERBATIM` COMO UNA SEDE MOVIDA**

Misma causa, otro sitio: el re-cotejo tras adosar media sobre **la pagina entera**, incluida la
seccion recien escrita. Corregido: **se mide sobre las lineas de arriba solas**, las que habia antes
de adosar, **y se dice por que**. Con eso da **`OK (64 de 64)`**.

### 7.4 **CORRI `recomputo_3388.py` SIN SU ARGUMENTO REQUERIDO**

`argparse` murio con **`exit 2`** y **cero salida util**. Lo vi por el codigo de salida y lo re-corri
con `--salida`. **Es la misma especie que la 8.1 y la misma que la 7.2 de la vuelta 67**: un
instrumento que exige argumento y una llamada que no lo lleva.

### 7.5 **CONTE LAS DUPLICADAS ANTES DE RECOMPILAR EL GRAFO**

Mi primera corrida de `aristas_duplicadas_tras_resolver.py` fue **entre la fusion y `run_phase1`**, y
leyo el `master_graph` viejo: dijo **914 grupos sobre 3.243 vivos**, que es el censo de antes con
etiqueta de despues. **Re-corrida despues del Gate 0** da **913 sobre 3.237**. **La cifra publicada
es la segunda**, y la primera queda dicha aqui **porque una medicion descartada en silencio es una
medicion que nadie puede auditar**.

### 7.6 **LOS DOS TITULOS DE PROCEDENCIA DE ESTA VUELTA SALIERON `AMBAR` Y LOS ROTULE**

El barrido de cierre saco **`AMBAR` 2**: mis dos instrumentos nuevos declaran vuelta 68 y sus
titulos nombran la 67 y la 65. **Los dos casos son PROCEDENCIA legitima** (uno transcribe el acta 67,
el otro cuelga de la cabecera de tramo de la 65), asi que **les puse el `ROTULO` con su prueba y su
motivo**, y **`AMBAR` vuelve a 0** con `ROTULADO` de 42 a **44**. **Y no repito la averia 7.4 de la
vuelta 67**: los dos rotulos **tienen `AMBAR` vivo que triar**, no son huerfanos, y el barrido
re-corrido lo confirma.

---

### 7.7 **ESCRIBI LOS DISCUTIBLES EN LA SECCION 7 Y LA GUARDA DE PROMESAS CAYO EN `ROJO`**

**La guarda mide contra LA SECCION 6 del reporte**, que es donde la casa pone los discutibles desde
la vuelta 61. Yo abri una seccion propia para la particion del racimo y **empuje los discutibles a la
7**: la guarda leyo como *seccion 6* la de la particion y dio **3 promesas medidas, 2 cumplidas, 1
INCUMPLIDA** (la del acto 19). **La cace corriendo la guarda, no leyendo el `exit`**, que es la
leccion de la vuelta 67. **Corregido moviendo el texto, no la guarda**: la particion pasa a ser el
apartado **3.8** dentro de la TAREA 2, que es donde le toca, y **los discutibles vuelven a la seccion
6**. Re-corrida: **3 de 3 CUMPLIDAS**. **Ninguna cifra dependia de esto, pero un reporte cuya
numeracion se sale del sitio deja ciega a una guarda que si mide.**

## 8. PENDIENTES DE DOCTRINA Y PREGUNTAS

1. **EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE** (heredado, acta 67 pendiente 3): **ahora son
   TRECE los actos declarados que esperan el cierre de la fase 03** (los 9 anteriores mas el 20, 21,
   23 y 24 de esta vuelta). Sigue enrutado al **cierre de la fase 03**, donde **la parada de
   `AUDITOR.md` espera al fundador**.
2. **LA MARCA PARA *YA LO DICE EL `APPEND` DE UN HERMANO*** (heredado, acta 67 pendiente 4): **esta
   vuelta lo paga DOS veces** con `CUBIERTO` mas atenuante declarado, **y por primera vez sobre un
   par que el archivo declara *el mismo principio numerado***. **El carril alcanza, pero la cuenta
   crece y el caso es mas puro que los anteriores** (ver `D11`).
3. **EL `INCISO` DE CONDICIONES SIGUE SIN EXISTIR** (heredado): **cuatro perdidas `DE CONDICIONES`
   mas** en esta vuelta, enrutadas a la fase 04 por el carril del acta 55, pregunta 5.
4. **EL ESQUEMA DE `OPERACIONES.jsonl`** (heredado): sigue pendiente y **esta vuelta no toco ninguna
   ficha**, asi que no estreno ninguna clave.
5. **NUEVO, Y ES UNA PREGUNTA, NO UNA PARADA: QUE HACE UN ACTO CUYO RACIMO DEL INVENTARIO DICE *EN
   MESA* PERO CUYOS DOS CAMPOS DE DUENO ESTAN VACIOS?** Lo resolvi por el dueno medido y **la
   particion no cruzada** (seccion 3.8), **pero la letra no dice cual de los dos campos manda cuando
   discrepan**: el `estado` de una entrada de inventario o el `duenos_*` del fichero del tramo. **La
   pregunta concreta para el auditor: un `estado` de inventario que dice *en mesa* con
   `operaciones: []` es dueno a efectos del universo de `OP-U-02`, o no lo es?**
6. **NUEVO, Y LO TRAIGO ANTICIPADO: EL LOTE SIGUIENTE ABRE CON UNA FUSION QUE NO ELIGIO EL
   EJECUTOR.** El carril del transito dice que **el lote siguiente ejecuta la fusion adjudicada como
   su primera operacion**, pero **no dice si esa fusion cuenta para el tope del lote nuevo ni con
   que plan se sella** (uno propio, o el del lote D reabierto). **Lo dejo dicho para que no llegue de
   sorpresa.**

---

## 9. RUTAS TOCADAS Y CENSOS AL CIERRE

**Del grafo (15 ficheros):** los **dos supervivientes** (`division_trabajo_humano_ia` y
`comprension_capacidades_limitaciones_ia`), sus **seis absorbidos**
(`automatizacion_tareas_aburridas`, `descomposicion_tareas_trabajo`, `framework_tareas_ia_humano`,
`invitar_ia_a_todo`, `jagged_frontier_ia`, `principio_invitar_ia_siempre`), los **siete redirigidos**
(`centaur_cyborg_ia`, `colaboracion_creador_consumidor`, `desafios_implementacion_ia`,
`principio_humano_en_el_loop`, `riesgo_sobredependencia_ia`, `search_for_business_model`,
`sistemas_organizacionales_ia`), mas `dataset/metadata/master_graph.json` y
`dataset/metadata/phase1_run_log.json`.

**Del registro:** `docs/plan/03_FUSIONES.md` (**`+187`** del acta 67 y **`+354`** del lote D, **cero
borradas en los dos**), `docs/plan/ARISTAS_DUPLICADAS.jsonl`, `docs/COSTURAS_INTERNAS.jsonl` y su
resumen, y `web/lib/assets/` por el `sync`. **`docs/plan/OPERACIONES.jsonl` NO se toco**, y
**`scripts/rumbos/banco_rumbos.json` tampoco**, porque el reanclaje no tuvo nada que hacer.

**Instrumentos nuevos:** `scripts/loop/vuelta68_registrar_acta67.py`,
`scripts/loop/_v68_texto_acta67.py`, `scripts/loop/_v68_lote_d.py`,
`scripts/loop/vuelta68_registro_lote_d.py` y `scripts/loop/_v68_texto_lote_d.py`. **Ningun
instrumento de nombre estable se toco en esta vuelta.**

| censo al cierre | valor |
|---|---|
| **barrido de titulos** ([`SALIDA_V68_BARRIDO.txt`](SALIDA_V68_BARRIDO.txt)), **re-corrido AL CIERRE** | **448 ficheros**, `ROJO` **32** (linea base heredada, **sin mover**), **`AMBAR` 0**, `ROTULADO` **44**, `CENSO` **224**, `ILEGIBLE` **1**. **Los 448 son los 443 del acta 67 mas los CINCO instrumentos nuevos de esta vuelta**, contados uno a uno |
| **censo de plantillas talladas** ([`SALIDA_V68_CENSO_PLANTILLAS.txt`](SALIDA_V68_CENSO_PLANTILLAS.txt)) | **CERO TALLADOS** sobre **23** instrumentos de nombre estable |
| **estado de las operaciones** ([`SALIDA_V68_CIERRE.txt`](SALIDA_V68_CIERRE.txt)) | **71**, todas `LISTA`, **0** dependencias rotas, **672** entradas, enlaces **17.562** |
| **casos positivos sobre sujetos que esta vuelta NO toca** | mesa: **LAS NUEVE MUERDEN** sobre `OP-M-02-ACCLIMATE`; contrato de perdidas: **LAS CUATRO**; varas: **LAS TRES mitades**; promesas: **LAS DOS mitades** |

### 9.1 **LA TASA POR DOMINIO AL CIERRE, IDENTICA A LA DE APERTURA**

**Fundir no volteo ni un veredicto**, y por eso el marcador de cierre sale **identico linea a linea**
al de apertura (comparado por maquina sobre las 20 lineas del fichero: **cero diferencias**).

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

**Corte de todas estas cifras: 26 ago 2026, puesto 3.388.**

---

## 10. LO QUE QUEDA DEL TRAMO, MEDIDO AL CIERRE

([`SALIDA_V68_TRAMO_CIERRE.txt`](SALIDA_V68_TRAMO_CIERRE.txt))

| | |
|---|---:|
| actos del tramo unico | **47** |
| cerrados por los lotes A, B y C | **14** |
| **cerrados por el lote D (esta vuelta)** | **6** (2 fundidos, 4 declarados) |
| **quedan** | **27 actos** |
| **nodos que quedan** | **85** |
| **el siguiente del prefijo** | el acto **18**, que queda `ABIERTO EN TRANSITO` |
| de los que quedan, con nodo puente al cierre | **1** (el acto **27**) |
| **actos declarados que esperan el cierre de la fase 03** | **13** |

**NO SE FUNDIO NINGUN ACTO CON DUENO** (el acto 24 lo tiene y se declaro con el dueno dicho), **no se
toco la mesa `OP-M-03` ni sus dos colisiones**, **no se tocaron las dos colisiones de `OP-U-02`**
(siguen vigentes y publicadas con su duena), y **las cinco fichas `OP-M-02` consumidas no se
ejecutaron**: lo consumado no se ejecuta ni se rehace.

---

## 11. CONDICIONES DE PARADA, RECORRIDAS

| condicion | se cumple? |
|---|---|
| doctrina nueva inventada | **NO**: los dieciseis discutibles y los seis pendientes quedan bajo letra citable (`P.1`, `P.5`, `P.8`, `P.10`, `P.12`, `P.16`, guarda `1B`, banco 9.10, 9.21 y 9.23, y actas 53, 54, 55, 61, 63, 64, 65, 66 y 67). **Lo que no tiene letra va como PENDIENTE, no como regla**: la pregunta del racimo *en mesa* con `operaciones: []` se sube **como pregunta**, no se disfraza de carril |
| contradiccion sin regla de correccion | **NO**: la unica del dia (la cita 4055) tenia carril y se corrigio por el banco 9.10 |
| decision de fundador | **NINGUNA SE TOMA**: el merge sigue siendo suyo y no se autoriza ninguna lectura nueva |
| fallo tecnico repetido | **NO**: Gate 0 y las tres suites en verde |
| campana consumada | **NO**: quedan **27 actos y 85 nodos** del tramo, la mesa `OP-M-03` y las fases 04 en adelante |
| **cierre de la fase 03** (la parada de `AUDITOR.md`) | **NO SE CUMPLE TODAVIA**: quedan 27 actos, uno de ellos `ABIERTO EN TRANSITO`, y los **13** declarados siguen sin destino resuelto |
| credenciales | no hicieron falta |

---

## 12. HASH FINAL Y COMMITS

**Los tres commits de trabajo de esta vuelta, escritos en la rama `pasada-unica` y leidos hoy con
`git log --oneline`:**

| commit | que lleva |
|---|---|
| **`2bd639c7`** | **TAREA 1 entera**: el registro del acta 67 (`+187`, `0` borradas), **la correccion declarada de la cita** y **la guarda de citas ensanchada**, mas **la APERTURA medida antes de la primera operacion** |
| **`0c946b7d`** | **TAREA 2**: el lote D ejecutado (2 fusiones, 4 declarados, 1 en transito, 6 nodos muertos, `P.16` limpio, colisiones que calzan sobre la base 4, Gate 0 con su ciclo de tres y las tres suites en verde) |
| **`e5402157`** | **el registro del lote D** (`+354`, `0` borradas, 16 agujas derivadas, idempotencia mordiendo, barrido con `AMBAR` de vuelta a 0) |
| **`9cf749f5`** | **el reporte entero**, leido hoy con `git log --oneline` |

**EL HASH FINAL DE LA VUELTA ES EL DEL QUINTO COMMIT**, el que escribe esta misma linea, **y por eso
no se puede escribir dentro de si mismo**: **un commit no puede contener su propio hash**. **Los
CUATRO anteriores estan arriba y en esta linea, ninguno de memoria.** Es la misma via que las vueltas
65, 66 y 67 usaron, y la regla 7 pide exactamente esto: el hash final y los commits anteriores en la
cabecera de la seccion 12.

**LAS TRES GUARDAS DE CIERRE, RE-CORRIDAS TRAS ESTA EDICION** (regla 1: lo que la propia vuelta
mueve, se remide antes de publicar):

| guarda | comando | resultado |
|---|---|---|
| **la cabecera se talla, no se teclea** | `tallar_cabecera_reporte.py --vuelta 68 --comparar docs/loop/REPORTE.md` | **`CABECERA: IDENTICA AL TALLADOR`**, 14 filas cotejadas, DISTINTAS 0, ausentes 0 ([`SALIDA_V68_CABECERA_COMPARADA.txt`](SALIDA_V68_CABECERA_COMPARADA.txt)) |
| **las promesas de marcado, por maquina** | `comprobar_promesas_de_marcado.py --reporte docs/loop/REPORTE.md --plan docs/loop/PLAN_V68_OPU02_LOTE_D.json` | **3 promesas, 3 CUMPLIDAS, 0 INCUMPLIDAS**, **tras la correccion de la averia 7.7** ([`SALIDA_V68_PROMESAS.txt`](SALIDA_V68_PROMESAS.txt)) |
| **el barrido de titulos, re-corrido AL CIERRE** | `barrido_titulos_tallados.py` | **448 ficheros, `ROJO` 32** (linea base sin mover), **`AMBAR` 0**, `ROTULADO` 44, `CENSO` 224 ([`SALIDA_V68_BARRIDO.txt`](SALIDA_V68_BARRIDO.txt)) |
| **LAS CITAS DE LINEA DEL PROPIO REPORTE, COTEJADAS UNA A UNA** (guarda nueva de esta vuelta, por el aviso del credito) | un cotejo por maquina de **cada afirmacion del reporte sobre una linea de `03_FUSIONES.md`**, con su aguja de contenido y **una negativa** | **6 afirmaciones, 1 negativa, MALAS 0**, y **CERO citas sin cotejar** ([`SALIDA_V68_COTEJO_CITAS_REPORTE.txt`](SALIDA_V68_COTEJO_CITAS_REPORTE.txt)) |

**Cero guiones largos y cero guiones medios**, contados por maquina sobre el fichero entero.
