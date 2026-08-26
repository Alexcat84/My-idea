# REPORTE DE LA VUELTA 72: EL LOTE H DEL TRAMO UNICO DE `OP-U-02`, CUATRO FUSIONES, EL PRIMER `DECLARADO` POR LA GUARDA `1B` Y CERO COLISIONES FABRICADAS

**Fase III, ejecucion continua. Rama `pasada-unica`. 26 ago 2026.**

**FECHA POR DOS RELOJES, CORRIDOS POR MI:** el reloj del sistema da **2026-08-26** y `git log -1
--date=format` sobre el ultimo commit da **2026-08-26 06:35**. **Toda cifra de este reporte tiene ese
corte.** La vuelta abrio con el arbol limpio en `1dd2cccd` y **no cruzo medianoche**.

**EL CONTADOR DE PARADA ENTRO A ESTA VUELTA EN CERO TANDAS** (acta 71, seccion 8, por las dos vias que
esa seccion nombra). **Lo que este reporte trae para ese contador va dicho de frente y no al final:**
cero veredictos movidos, cero colisiones fabricadas, y **el marcador identico al digito entre apertura
y cierre, las catorce filas y las diez tasas**. **Las averias propias de la vuelta son CINCO y ninguna
llego a una cifra publicada** (seccion 7). **Hay DOS cosas que este reporte declara en vez de
esconder, y las dos van marcadas: una celda de tabla copiada que publicaba una afirmacion falsa para
un declarado por la guarda `1B` (`D9`), y una fila de perdida que es de la especie del pendiente 4 en
sustancia pero no lleva la frase sellada, sobre un plan que YA se ejecuto y que por eso NO se re-sella
(`D8`).**

---

## 1. LA CABECERA, TALLADA Y NO TECLEADA

**Generada entera con** `python scripts/loop/tallar_cabecera_reporte.py --vuelta 72` y **pegada sin
tocar una celda** ([`SALIDA_V72_CABECERA.txt`](SALIDA_V72_CABECERA.txt)). **La celda que no salga de
un instrumento no se escribe.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.204 / 649 / 17.639 | **3.853 / 3.196 / 657 / 17.663** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 360 / 191 | **551 / 368 / 183** |
| actos (componentes) | 57 | **53** |
| actos `CERRADOS` / `ABIERTOS` | 26 / 31 | **26 / 27** |
| nodos en `CERRADOS` / `ABIERTOS` | 61 / 151 | **61 / 139** |
| cola de costuras | 1.442 | **1.440** |
| colisiones de clase vigentes | 7 | **7** |
| auto-pares (los dos lados al mismo vivo) | 278 | **282** |
| duplicadas historicas: grupos / nodos | 902 / 714 | **899 / 712** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (212 igual a 212; 191 igual a 191) | **TODAS OK (200 igual a 200; 183 igual a 183)** |

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION** (regla 1): los seis instrumentos de apertura
corrieron con el arbol limpio en `1dd2cccd`, **antes de escribir nada**, y `git status --porcelain`
tras correrlos dio **CERO ficheros rastreados movidos** (solo las salidas nuevas, sin trackear).
**EL CIERRE SE RECOMPUTO AL CIERRE**, despues de que las cuatro fusiones y `run_phase1` movieran el
arbol.

**LA APERTURA DE HOY CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 71 PUBLICO** (marcador 551 / 72 / 5 /
2.760, grafo 3.853 / 3.204 / 649 con 17.639 enlaces, retrato 551 / 360 / 191, 57 componentes, 26 y 31
sobre 61 y 151, cola 1.442, colisiones 7, auto-pares 278, duplicadas 902/714, 71 `LISTA`, 672 entradas
y las cuatro comprobaciones en 212 y 191), **que es el contraste que la regla 2 permite**: entre las
dos vueltas nadie movio dato.

**LA ARITMETICA DEL SALTO ES COHERENTE ENTERA:** cuatro actos fundidos son **menos 4 componentes** (57
a 53), **menos 12 nodos abiertos** (151 a 139), **menos 8 vivos** (3.204 a 3.196) y **mas 8
deprecados** (649 a 657). El retrato sube 8 colapsos y baja 8 pares distintos (191 a 183), que es **un
par interno por acto colapsando a auto-arista**, y los auto-pares suben exactamente esos **4** (278 a
282). Las duplicadas bajan **3** por `P.16`. Los enlaces suben **24**.

> **LA COLA DE COSTURAS BAJA POR PRIMERA VEZ EN TODO EL TRAMO, Y NO SE DEJA COMO UN MENOS DOS MUDO**,
> porque el instrumento la mide nodo a nodo
> ([`SALIDA_V72_COLA_DELTA.txt`](SALIDA_V72_COLA_DELTA.txt)): **ENTRAN CERO y SALEN DOS**. Los dos que
> salen son **absorbidos** (`evitar_sesgo_retrospectivo_hindsight` y `perdida_control_operativo`) que
> dejan de ser vivos, y **NINGUN superviviente de este lote entra a la cola**. **Es la diferencia
> entera con el lote `G`**, donde entraron tres y quedo marcado como su costo mas caro (`D6` del acta
> 71). **El corte de esta medicion es `c4c38956`, el commit del plan, que es PRE fusion.**

---

## 2. TAREA 1: EL REGISTRO DEL ACTA 71 Y LAS TRES CORRECCIONES DECLARADAS

`python scripts/loop/vuelta72_registrar_acta71.py`
([`SALIDA_V72_REGISTRO_ACTA71.txt`](SALIDA_V72_REGISTRO_ACTA71.txt))

**`+246` lineas y CERO borradas** (`git show --numstat` sobre `a3bc1153`: **`246 0`**), **59 agujas
derivadas y NINGUNA tecleada**, **tres agujas NEGATIVAS de sustancia en verde**, **idempotencia
MORDIENDO** (segunda corrida: *YA ADOSADA*, arbol limpio despues).

**LA MAQUINA SE COPIO POR EXTRACCION Y NO SE RETECLEO** (`_v72_construir_registrador_acta.py`): las
dos piezas copiadas (los imports y la maquina entera de la guarda de citas, 9 sub-piezas comprobadas
con `assert`) **aparecen LITERALES en el destino**, comprobado por el propio constructor. **La maquina
NO CRECE**: cero mecanismos nuevos, cero filas, cero columnas (adjudicacion 3 del acta 69).

> **LO UNICO QUE SE ANADE SON TRES CONSTANTES DE RUTA, Y SE DICE POR QUE NO ES MAQUINA NUEVA:** esta
> vuelta cita **la sede de cada una de sus tres correcciones por AGUJA y no por numero tecleado**, y
> dos de esas sedes no viven ni en la pagina ni en el acta (`OPERACIONES.jsonl`,
> `generar_plan_del_lote.py`, `banco_rumbos.json`). **`AGUJAS` siempre fue un mapa `CLAVE ->
> (fichero, aguja)` y el fichero es un DATO**: ni una funcion nueva, ni una condicion nueva.

### 2.1 **CORRECCION DECLARADA, PRIMERA: LA FICHA DE `OP-L-03`** (adjudicacion 3 del acta 71)

`python scripts/loop/vuelta72_correccion_ficha_opl03.py --escribir`
([`SALIDA_V72_CORRECCION_OPL03.txt`](SALIDA_V72_CORRECCION_OPL03.txt))

**Por el carril del banco `9.10`**, el mismo que la ficha gemela de `OP-U-02` uso en la vuelta 66:
**el texto viejo entero arriba sin tacharlo** y **la vara nueva escrita debajo**, con las **cuatro**
mitades que el acta 65 dio para la clausula gemela y con las palabras **NO ES PARADA** citadas del
acta 71. **CERO claves nuevas de esquema**: la correccion entra como **un elemento mas** de la lista
`verificacion` que ya existia, y las **71 fichas siguen con 18 claves cada una**, medido antes y
despues; **cero otras fichas movidas**, medido comparando su `json.dumps` ordenado.

> **UNA DISCREPANCIA CON EL ACTA QUE SE DECLARA EN VEZ DE RESOLVERSE COPIANDO** (regla 2): el acta 71
> llama a esta clausula **LA MISMA frase** que el acta 65 adjudico para `OP-U-02`. **EN SUSTANCIA LO
> ES**, y por eso la adjudicacion vale entera y la correccion se aplica sin dudar. **AL BYTE NO LO
> ES**, medido hoy por el propio instrumento: la de `OP-L-03` dice *ningun acto se funde con un par
> interno sin veredicto* y la de `OP-U-02` dice *el acto se leyo ENTERO antes de fundirse: cero pares
> internos sin veredicto*. **Es la misma regla en voz activa sobre la fusion y en voz pasiva sobre la
> lectura.** **Por eso el instrumento cita la letra de ESTA ficha y no la de aquella, y cae en `ROJO`
> si la de `OP-L-03` no esta verbatim.** **Va marcado (`D1`).**
>
> **Y EL PRECEDENTE QUE LA CORRECCION CITA SE COMPRUEBA EN VEZ DE SUPONERSE**, que es la regla 9 (una
> busqueda negativa no se puede citar) aplicada a una POSITIVA: el instrumento **mide** que la
> clausula gemela sigue verbatim en `OP-U-02` **y** que la correccion de la vuelta 66 esta aplicada
> sobre ella. **Si cualquiera de las dos faltara, seria `ROJO` y no escribiria nada.**

### 2.2 **CORRECCION DECLARADA, SEGUNDA: EL PREFIJO DE `generar_plan_del_lote.py`** (adjudicacion 6)

**Instrumento de nombre estable**, asi que va **por el carril declarado**, el mismo que este fichero
ya uso en la vuelta 63 y en la vuelta 65: **el texto viejo se queda entero, citado VERBATIM en el
docstring Y en las DOS sedes donde muerde**, y no se tacha. **`git diff --numstat`: `50 2`.**

| | el texto viejo, VERBATIM | lo que hace ahora |
|---|---|---|
| la declaracion del argumento | `help="prefijo del plan; por defecto PLAN_V<vuelta>_OPU01_LOTE_"` | el `help` describe el prefijo **derivado de `--operacion`** |
| su uso dentro de `main` | `prefijo = a.prefijo or ("PLAN_V%d_OPU01_LOTE_" % a.vuelta)` | `prefijo = a.prefijo or ("PLAN_V%d_%s_LOTE_" % (a.vuelta, a.operacion.replace("-", "")))` |

**LA EVIDENCIA NO ES UNA IMPRESION: ES LA AVERIA 7.3 DE LA VUELTA 71**, donde el generador acepto
`--operacion OP-U-02`, **sello bien el contenido** y aun asi escribio `PLAN_V71_OPU01_LOTE_G.json`.
**LA ARITMETICA NO SE TOCA** y **`--prefijo` sigue existiendo y sigue ganando cuando se pasa.**

> **LA CORRECCION SE COMPROBO MORDIENDO, NO LEYENDO EL DIFF:** el plan de este lote salio como
> **`PLAN_V72_OPU02_LOTE_H.json`**, leido de la linea `plan escrito` de la salida **antes de sellar**
> ([`SALIDA_V72_SELLO_PLAN_1.txt`](SALIDA_V72_SELLO_PLAN_1.txt)). **Es el primer plan del tramo que
> sale con el nombre de su operacion sin pasar `--prefijo` a mano.**
>
> **Y EL CASO POSITIVO DEL GENERADOR SIGUE EN VERDE, Y NO ES CASUALIDAD SINO LO QUE LA PROPIA
> CORRECCION PROMETIO:** `vuelta65_caso_positivo_generador.py` **pasa `--prefijo` EXPLICITO en las dos
> ramas** (ancestro y fichero de hoy), leido hoy en sus lineas 151 a 156, **asi que el cambio del
> defecto no lo alcanza**. **Ninguna llamada vieja que pase `--prefijo` a mano cambia de resultado**,
> y eso queda medido y no prometido.

### 2.3 **CORRECCION DECLARADA, TERCERA: EL ANCLA DUPLICADA DEL RUMBO** (adjudicacion 7)

`python scripts/loop/vuelta72_ancla_duplicada.py --escribir`
([`SALIDA_V72_ANCLA_DUPLICADA.txt`](SALIDA_V72_ANCLA_DUPLICADA.txt))

**QUIEN FABRICA LIMPIA**, por el principio de `P.16` **por extension** (la duplicada la fabrico un
reanclaje y no una fusion, y eso se dice en vez de estirar la letra literal, que habla de aristas del
grafo).

| | medido |
|---|---:|
| rumbos barridos, el fichero **ENTERO** | **49** |
| rumbos con alguna ancla repetida, **ANTES** | **1** |
| rumbos con alguna ancla repetida, **DESPUES** | **0** |
| el nombrado por el acta y el medido por la maquina, **calzan** | **SI** |
| entradas repetidas quitadas | **1** |
| **destinos perdidos** | **0**, el conjunto de ids de cada ancla es identico |
| otros rumbos movidos | **0** |
| `git diff --numstat` | **`0 1`**: **una linea borrada y CERO anadidas** |

> **LA COMPROBACION QUE EL ENCARGO PIDE SE PUBLICA ENTERA Y NO SE RESUME EN UN CERO**, porque una
> busqueda negativa no se puede citar (regla 9): **no basta con depurar el rumbo que el acta nombra**.
> El instrumento **barre los 49 rumbos**, **cuenta**, **los nombra uno a uno** y **coteja** lo medido
> contra lo que el acta dice. **Si el acta hubiera nombrado uno y hubiera dos, se veria aqui.**

---

## 3. TAREA 2: EL LOTE H, DECLARADO AL ABRIRLO Y ENTREGADO ENTERO

**SE DECLARARON CINCO ACTOS Y 15 NODOS AL ABRIR, Y SE ENTREGO EL DESTINO DE LOS CINCO.** **CUATRO
cierran FUNDIDOS y UNO cierra `DECLARADO Y NO FUNDIDO`.**

| acto | cierra | **FORMA medida** | superviviente | quien decide |
|---:|---|---|---|---|
| **43** | **FUNDIDO** | `UNA SOLA VARA` | `preservar_efectivo_buscar_modelo` | la vara de **condiciones**, sola |
| **44** | **`DECLARADO Y NO FUNDIDO`** | `UNA SOLA VARA` | **NINGUNO** | **la guarda `1B`, con DOS puertas** |
| **45** | **FUNDIDO** | `CONTENIDO EMPATA` | `reconstruccion_contexto_situacional` | **el cableado, solo** |
| **46** | **FUNDIDO** | `UNA SOLA VARA` | `mitigacion_riesgos_ambientales` **(LA PUERTA)** | **la puerta, contra la vara** |
| **47** | **FUNDIDO** | `UNA SOLA VARA` | `gestion_terminacion_franquiciado` | la vara de **pasos** |

**LOS DOS SALTOS VAN DECLARADOS CON SU CITA** (adjudicacion 2 del acta 69): el `acto 31` tiene dueno
medido (`OP-F-04-WEI` y `OP-S-04`) y el `acto 37` tambien (`OP-S-07`), **leidos hoy del fichero
fijado**; ninguno de los dos es una fusion de `OP-U-02`, asi que **saltarlos no rompe el prefijo sin
saltos**. **EL TOPE CAE ANTES DEL `49`, y es de lote y no estructural:** el `49` no tiene dueno y no
trae puerta; el tope cae ahi **porque el encargo fija CINCO actos**.

### 3.1 **`P.5`: EL ACTO LEIDO ENTERO, Y LA PREGUNTA CONTESTADA CON EL TEXTO ESTABLE**

**El acto se leyo ENTERO** con `python scripts/loop/dossier_del_tramo.py --tramo
docs/loop/TRAMO_UNICO_OPU02_V64.jsonl --actos 43,44,45,46,47`
([`SALIDA_V72_DOSSIER_LOTE_H.txt`](SALIDA_V72_DOSSIER_LOTE_H.txt), **310 lineas**): los **15** nodos
con sus pasos, condiciones, previos, siguientes y entregable, y **los 10 pares con su razon ENTERA sin
recortar**. **`P.5` contesta UNA FAMILIA en los cinco**, **incluido el `44`**, y eso se dice porque
**lo que detiene al `44` no es la familia, son sus puertas**.

**MEDIDO** con `python scripts/loop/vuelta65_puentes_del_tramo.py --tramo ... --actos 43,44,45,46,47
--detalle` ([`SALIDA_V72_PUENTES_TRAMO.txt`](SALIDA_V72_PUENTES_TRAMO.txt)): **los cinco son de 3
miembros con 2 pares `A`, 0 `D` y 1 sin veredicto, y los cinco traen CERO nodos puente y CERO
triangulos**. **`P.10` no tiene sujeto en ninguno.**

### 3.2 **`P.8` EN ORDEN, Y TODA CIFRA DE CABLEADO DE LA COLUMNA `cab`**

`python scripts/loop/varas_n_arias_del_tramo.py --tramo ... --actos 43,44,45,46,47`
([`SALIDA_V72_VARAS_N_ARIAS.txt`](SALIDA_V72_VARAS_N_ARIAS.txt)). **Ninguna cifra de esta tabla esta
tecleada: las tres columnas salen del instrumento**, que es la unica fuente de cifra de cableado desde
la adjudicacion 3 del acta 70.

| acto | pasos | condiciones | **cableado (`cab`)** | forma | quien decide, por la letra |
|---:|---|---|---|---|---|
| **43** | **EMPATA** en 5 | apunta al superviviente, **4** contra 2 y 2 | **11 contra 7 y 7**, al OTRO lado | `UNA SOLA VARA` | la de condiciones. **El cableado NO habla: el contenido no empata** |
| **44** | apunta a `explotacion_...`, **6** contra 4 y 4 | **EMPATA** en 2 | **6 contra 5 y 2**, al OTRO lado | `UNA SOLA VARA` | **NADIE: la guarda `1B` detiene antes** |
| **45** | **EMPATA** en 5 a tres bandas | **EMPATA** en 2 | **8 contra 3 y 2**, al superviviente | `CONTENIDO EMPATA` | **el cableado, SOLO, y es el unico del lote** |
| **46** | **EMPATA** en 4 a tres bandas | apunta a `gestion_eco_riesgos`, **3** contra 2 y 2 | **EMPATA** en 4 | `UNA SOLA VARA` | **la guarda de la puerta, contra la unica vara que habla** |
| **47** | apunta al superviviente, **5** contra 4 y 4 | **EMPATA** en 2 | **2 contra 1 y 1**, al OTRO lado | `UNA SOLA VARA` | la de pasos. **El cableado NO habla** |

> **LAS FORMAS MEDIDAS HOY CALZAN AL DIGITO CON LAS QUE EL ACTA 71 PUBLICO** para estos cinco (43, 44,
> 46 y 47 `UNA SOLA VARA`; 45 `CONTENIDO EMPATA`), **y con las puertas que nombro** (el `44` con DOS,
> el `46` con UNA). **Es contraste, no fuente**: las cifras de arriba salen de mi corrida de hoy.

### 3.3 **EL `ACTO 44`: EL PRIMER `DECLARADO` POR LA GUARDA `1B` DE TODO EL TRAMO**

**DOS de los tres miembros son PUERTA** (`explotacion_tecnologias_disruptivas` y
`tecnologias_disruptivas_oportunidad`), medidos contra el universo protegido de **256** ids. **La
guarda `1B` prohibe absorber una puerta, y con DOS no existe ningun superviviente posible que no
absorba a la otra.**

**LO QUE NO SE HIZO, ENUMERADO PARA QUE NADIE LO LEA COMO UN OLVIDO:** no se fundio el tercer miembro
contra una de las dos puertas **(seria una fusion parcial y ninguna letra la escribe)**, no se eligio
puerta ganadora **(la guarda no ordena las puertas entre si)**, no se partio el acto en dos **(el acto
es la componente y partirla es re cribar)**, y **no se toco ni un nodo, ni un alias, ni un veredicto**.

**Y SE DICE A QUIEN HABRIAN APUNTADO LAS VARAS**, porque callarlo seria esconder el costo: **los dos
nodos a los que apuntan las varas SON LAS DOS PUERTAS**. **Esa es exactamente la trampa.**

> **SEGUNDA RAZON, INDEPENDIENTE Y MEDIDA, PARA NO FUNDIRLO:** `INVENTARIO.jsonl` trae una entrada de
> tipo **`figura`**, la `ESTRELLA` del banco `9.23`, que nombra **a los TRES miembros de este acto**
> como uno de sus ejemplares. **Es una FIGURA y no una jurisdiccion** (no nombra operacion ninguna),
> asi que **NO es dueno** por la adjudicacion 2 del acta 68; **se declara porque una fusion entera
> habria deprecado a dos de los tres ejemplares de una figura declarada.**
>
> **Y UNA MEDICION QUE SE DEJA ESCRITA PARA EL CIERRE DE LA FASE 03:** la nota de `OP-L-03` declara
> que `evaluacion_tecnologias_disruptivas` es **`LD-04`**, una de las DOS lecturas dirigidas de la
> primera tanda **YA LEIDAS**. **El acto no se toca, asi que esa lectura no se gasta ni se
> contradice.**

### 3.4 **EL `ACTO 46`: LA PUERTA SOBREVIVE AUNQUE LA UNICA VARA QUE HABLA APUNTE AL OTRO LADO**

**Con UNA puerta el acto SI se funde y LA PUERTA SOBREVIVE, gane o pierda en contenido** (acta 54,
pregunta 1, registrado en esta pagina en la seccion del acta 65, apartado c, con estas palabras: *el
choque con la vara de contenido queda escrito en el motivo sellado*). **ESTE ES EXACTAMENTE ESE CASO,
Y EL CHOQUE EXISTE:** la vara de condiciones apunta a `gestion_eco_riesgos` (**3** contra 2 y 2) y el
superviviente es `mitigacion_riesgos_ambientales`. **Va marcado (`D4`).**

> **LA CONSECUENCIA PARA `OP-S-09` SE PUBLICA EN VEZ DE CALLARSE**, que es lo que la adjudicacion 2
> del acta 70 exige: la entrada `familia_de_ids` de `OP-S-09` trae
> `responsabilidad_extendida_productor` y `responsabilidad_extendida_productor_2`, **cubre 1 de los 3
> miembros del acto (PARTE de la nomina, el caso que esa adjudicacion resolvio)**, y este acto
> **absorbe** al primero. **A `OP-S-09` le queda `responsabilidad_extendida_productor_2` VIVO**,
> medido hoy sobre `master_graph` (sin marca de `deprecado`), **mas el otro id resolviendo por alias a
> `mitigacion_riesgos_ambientales`**. **Su sujeto queda SERVIBLE**, y lo que cambia se dice: **su
> resolucion aprobada tendra que ejecutarse sobre un alias que apunta FUERA de la familia.** **Va
> marcado (`D5`).**

### 3.5 **EL BORDE DE LA ADJUDICACION 2 DEL ACTA 71, MEDIDO Y NO SUPUESTO**

El acta 71 dejo escrito que **una `familia_de_ids` de nomina ENTERA sin resolucion aprobada que la
fusion ejecute va como PREGUNTA, no como fusion**. **No basta con no encontrarla: hay que buscarla**
([`SALIDA_V72_INVENTARIO_LOTE_H.txt`](SALIDA_V72_INVENTARIO_LOTE_H.txt)).

| | medido hoy sobre `INVENTARIO.jsonl` |
|---|---:|
| entradas que tocan a alguno de los **15** miembros | **12** |
| de ellas, de tipo `acto` | **9** |
| de ellas, de tipo `figura` | **2** |
| de ellas, de tipo **`familia_de_ids`** | **1** |
| esa `familia_de_ids`, cuantos miembros de su acto cubre | **1 de 3** (el `46`), o sea **PARTE** |
| **`familia_de_ids` que cubren la NOMINA ENTERA de un acto del lote** | **0** |

**EL BORDE NO SE PISA.** **La unica entrada de esa especie es el caso que el acta 70 ya adjudico**, y
ademas trae su resolucion aprobada (`DECISION 4` de la mesa de racimos, 9 ago 2026).

### 3.6 **LOS DUENOS, LOS RACIMOS Y LAS MENCIONES EN `OPERACIONES.jsonl`**

([`SALIDA_V72_DUENOS_Y_RACIMOS.txt`](SALIDA_V72_DUENOS_Y_RACIMOS.txt),
[`SALIDA_V72_MENCIONES_OPS.txt`](SALIDA_V72_MENCIONES_OPS.txt))

**Los dos campos `duenos_*` del fichero fijado estan VACIOS en los cinco actos**, medido hoy, y
**NINGUNO de los 15 miembros esta en ninguna nomina de `RACIMOS_MIEMBROS.jsonl`** (32 lineas
barridas).

> **Y AQUI SI HAY MENCIONES EN `OPERACIONES.jsonl`, A DIFERENCIA DEL LOTE `G`, Y VAN LEIDAS ENTERAS EN
> VEZ DE CONTADAS:** **SIETE** menciones en **CUATRO** fichas (`OP-U-01`, `OP-U-02`, `OP-L-03` y
> `OP-I-01`). **Las siete viven en el campo `nota` y ninguna en un campo `nodos`**, leidas campo a
> campo. **Tres fichas cuentan la MISMA prosa historica**: que el `acto 47` crecio de 2 a 3 entre el
> corte 2.117 y el 3.388 al ganar `perdida_control_operativo`. **La de `OP-L-03` es la del `LD-04`.**
> **NINGUNA es una de las TRES fuentes que la adjudicacion 2 del acta 68 fija como frontera del
> dueno**, y por eso **ninguna hace dueno a nadie**. **Se lee, se declara y no se estira.**

### 3.7 **EL PLAN, SELLADO DOS VECES, CON EL DIFF MEDIDO CAMPO A CAMPO**

`python scripts/loop/generar_plan_del_lote.py --lote H --vuelta 72 --operacion OP-U-02 ...`
([`SALIDA_V72_SELLO_PLAN_1.txt`](SALIDA_V72_SELLO_PLAN_1.txt),
[`SALIDA_V72_SELLO_PLAN_2.txt`](SALIDA_V72_SELLO_PLAN_2.txt)). **El diff de los dos sellos es de UN
SOLO CAMPO** (`colisiones_esperadas`), **comprobado campo a campo y no solo por lineas**
([`SALIDA_V72_DIFF_SELLOS.txt`](SALIDA_V72_DIFF_SELLOS.txt): **2 lineas de diff, 1 campo distinto**).

**LAS GUARDAS DEL GENERADOR, TODAS EN VERDE:** las cuatro fichas del lote; **guarda `1B`: ningun
absorbido es puerta**; **cobertura exacta** con marca UNICA por indice; **los CINCO `INCISO`
EXTRAIDOS del nodo y comprobados VERBATIM**, con su paso resultante impreso y **la tilde comprobada
leyendo los resultantes** (`métrica`, `según`, `qué`, `quedarán`); **la guarda de la JUNTURA ROTA** no
salto en ninguno, porque **ninguno de los cinco pasos receptores termina en punto**.

### 3.8 **LA FUSION, Y SUS GUARDAS**

`python scripts/loop/fundir_por_plan.py --plan docs/loop/PLAN_V72_OPU02_LOTE_H.json --ejecutar`
([`SALIDA_V72_FUSION_LOTE_H.txt`](SALIDA_V72_FUSION_LOTE_H.txt), simulada antes en
[`SALIDA_V72_FUSION_SIMULADA.txt`](SALIDA_V72_FUSION_SIMULADA.txt))

| | |
|---|---:|
| actos fundidos / declarados | **4** / **1** |
| nodos que **MUEREN** | **8** |
| vivos, antes y despues | **3.204** a **3.196** (delta deprecados **+8**, esperado **+8**: `OK`) |
| ficheros tocados | **40** |
| piezas repartidas | **49** (**6** enteras, **38** ya dichas, **5** de `INCISO`) |
| redirecciones sobre nodos vivos | **30** |
| **`P.16`**, duplicadas que la propia fusion fabrica | **1**, **limpiada en la misma corrida** |
| auto-aristas que la fusion habria creado y se retiran | **1** |
| guarda `C`, campos que esta operacion NO redacta | **20 de 20 intactos** |
| pasivo propio de la guarda `B` | **880** a **877** (la operacion lo BAJA en 3) |

**`P.16` RE-COMPROBADO POR SEPARADO:** `retirar_duplicada_por_resolutor.py --plan ...` corrido **tras**
la fusion dice **NINGUNA**, que es la idempotencia de la limpieza que el fundidor ya hizo.

### 3.9 **EL REANCLAJE, Y EL ANCLA DUPLICADA QUE ESTA VEZ NO SE FABRICO**

`python scripts/reanclar_por_resolutor.py`, **corrido ENTRE la fusion y `run_phase1`**
([`SALIDA_V72_REANCLAJE.txt`](SALIDA_V72_REANCLAJE.txt)): **NADA QUE RE-ANCLAR**, y **es un cero
medido y no un cero supuesto**: el fundidor ya habia redirigido **30** referencias vivas y **no quedo
ninguna fuera del grafo**.

> **LA LECCION DEL ACTA 71 SE APLICO AUNQUE EL REANCLAJE NO TOCARA NADA**, que es la unica forma de
> saber que no toco nada: `vuelta72_ancla_duplicada.py` se re-corrio **despues** de la fusion
> ([`SALIDA_V72_ANCLA_TRAS_FUSION.txt`](SALIDA_V72_ANCLA_TRAS_FUSION.txt)) y midio **CERO anclas
> repetidas sobre los 49 rumbos**. **Ninguna se fabrico y por eso ninguna se limpio.**

### 3.10 **EL DIFF DE DUPLICADAS, POR INSTRUMENTO Y CON LA APERTURA SACADA DE `git`**

`python scripts/loop/diff_duplicadas_por_resolutor.py --antes <git show c4c38956:...> --despues
docs/plan/ARISTAS_DUPLICADAS.jsonl`
([`SALIDA_V72_DIFF_DUPLICADAS.txt`](SALIDA_V72_DIFF_DUPLICADAS.txt)).

> **GRUPOS FABRICADOS DE VERDAD: `0`.** **RENOMBRADOS: `0`.** Hay **3 que DESAPARECEN**, y **los tres
> son de la misma especie y estan nombrados uno a uno en la salida**: un vivo que apuntaba a **DOS
> miembros del mismo acto en el mismo campo** y que tras la fusion **hereda el destino una sola vez**.
> **902 grupos resueltos a 899.**

**EL CORTE DE *ANTES* SALE DE `git show` SOBRE EL COMMIT DEL PLAN** (`c4c38956`), **anterior a la
fusion**, y el de *despues* es el fichero **tras recompilar el grafo con `run_phase1`**.

### 3.11 **EL CENSO DE COLISIONES: ESTE LOTE NO FABRICA NINGUNA, Y SE PUBLICA IGUAL**

`python scripts/loop/vuelta65_colisiones_esperadas.py --plan docs/loop/PLAN_V72_OPU02_LOTE_H.json`
([`SALIDA_V72_COLISIONES_ESPERADAS.txt`](SALIDA_V72_COLISIONES_ESPERADAS.txt)), **corrido sobre el
arbol de antes y simulando en memoria, sin tocar un nodo**.

| | |
|---|---:|
| linea base declarada **y MEDIDA sobre el arbol de antes** | **7** |
| **colisiones NUEVAS que la fusion fabricaria** | **0** |
| colisiones que desaparecerian | **0** |
| **ESPERADAS TRAS FUNDIR** | **7** |
| **MEDIDAS al cierre por el censo** | **7** |
| **`CALZA`** | **`SI`** |
| auto-pares: **NUEVOS predichos** y **medidos al cierre** | **4** nuevos predichos (278 a 282) y **282** medidos |

> **LA BASE ENTRO POR EL DEFECTO DEL INSTRUMENTO, QUE ES LO QUE LA VUELTA 71 DEJO EN `7`**: no hizo
> falta pasarla a mano, **y la guarda la MIDIO sobre el arbol antes de usarla**. **SEGUNDO LOTE
> SEGUIDO DEL TRAMO QUE NO FABRICA NINGUNA COLISION.** **Las dos de la mesa `OP-M-03` y las CINCO de
> `OP-U-02` ya publicadas siguen vigentes con su duena y no se tocan.**

### 3.12 **GATE 0 CON SU CICLO DE TRES, Y NO DE CUATRO**

| paso | resultado |
|---|---|
| `python scripts/run_phase1.py --reaplico-curaduria` | **`GATE 0: OK`**, todos los chequeos en `[OK]`; universo **3.196 activos / 657 deprecados**; alcanzabilidad **100,0 por ciento** (3.196/3.196, 85 semillas validas) |
| `python scripts/etiquetas_de_cara.py --aplicar` | etiquetas re-aplicadas |
| `python scripts/sync_assets_web.py` | **6 assets** mas `manifest.json` |
| **una cuarta corrida** | **NO SE HIZO** |

**LAS TRES SUITES, CORRIDAS POR MI:** motor **25/25**
([`SALIDA_V72_SUITE_MOTOR.txt`](SALIDA_V72_SUITE_MOTOR.txt)); web **80 ficheros, 1.030 pasadas, 3
saltadas** ([`SALIDA_V72_SUITE_WEB.txt`](SALIDA_V72_SUITE_WEB.txt)); `tsc --noEmit` **CERO lineas**
([`SALIDA_V72_TSC.txt`](SALIDA_V72_TSC.txt)). **Y el guardian de commit las volvio a correr en verde
en los tres commits de trabajo de esta vuelta.**

### 3.13 **EL REGISTRO EN `03_FUSIONES.md`** (`+498` lineas, `0` borradas)

`python scripts/loop/vuelta72_registro_lote_h.py`
([`SALIDA_V72_REGISTRO_LOTE_H.txt`](SALIDA_V72_REGISTRO_LOTE_H.txt)), **bajo la cabecera de tramo que
la vuelta 65 adoso** (derivada hoy por aguja) y **sin reescribir ni una linea de arriba** (`git show
--numstat` sobre `90df5a9f`: **`498 0`**). **19 agujas derivadas, ninguna tecleada**, **idempotencia
MORDIENDO**, y **las 19 sedes de arriba siguen en su linea** tras adosar, re-derivadas sobre las
lineas de antes.

---

## 4. LA CUENTA AGREGADA DE LAS PERDIDAS, POR MAQUINA

`python scripts/loop/cuenta_agregada_de_perdidas.py --plan docs/loop/PLAN_V72_OPU02_LOTE_H.json`
([`SALIDA_V72_CUENTA_ATENUANTES.txt`](SALIDA_V72_CUENTA_ATENUANTES.txt))

| | contado sobre el plan sellado |
|---|---:|
| **perdidas selladas en campo propio** | **12** |
| de ellas `DE PARAMETRO DE PASO` | **5** |
| de ellas `DE CONDICIONES` | **7** |
| **filas con `ATENUANTE DECLARADO`** | **1** |
| de ellas, de la **especie del pendiente 4** | **0**, **y esa cifra lleva glosa** |
| de ellas, con **`ATENUANTE DECLARADO Y MEDIDO`** | **1** |
| **filas con DOS SEDES en el campo `donde`** | **0** |
| **filas que describen un atenuante SIN la frase sellada** | **NINGUNA**, medido: **CERO exclusiones que declarar** |
| la aritmetica de **la lectura contraria** (una fila por SITIO y no por PIEZA) | **12** y no **12** |

> **LA CELDA DE LA ESPECIE DEL PENDIENTE 4 SALE EN `0` Y NO SE DEJA COMO UN CERO QUE PARECE LIMPIO.**
> El instrumento la cuenta buscando la frase sellada `ESPECIE DEL PENDIENTE 4` dentro del campo `que`,
> **y la fila del `acto 43` no la lleva**. **EN SUSTANCIA ESA FILA SI ES DE ESA ESPECIE**: la pieza
> (medir el consumo de caja) **llega entera desde otro absorbido del mismo acto**. **PERO llega por un
> `INCISO` y no por un `APPEND`**, que es el vehiculo que el nombre del pendiente nombra. **Lo vi al
> leer la salida del instrumento, no al escribir la celda**, y **el plan YA estaba ejecutado**: un
> plan ejecutado **no se re-sella** (acta 68, `D15`). **Se declara aqui y en el registro, y la
> pregunta de si la especie la define el VEHICULO o el HECHO va marcada (`D8`).**

---

## 5. LO QUE ESTA VUELTA APRENDIO DE UNA TABLA COPIADA QUE MENTIA

**La tabla del acto `DECLARADO` se viene copiando lote a lote y solo se habia IMPRESO una vez**, en la
vuelta 69 para el `acto 27`. **Dentro de la funcion, TECLEADA, llevaba esta coletilla, citada
VERBATIM:**

> `"**%s**, y su centro es el MISMO nodo puente que `P.10` detecto"`

**Era CIERTA para el `acto 27`**, cuyo motivo sellado **es** el triangulo de `P.10` y cuyo centro de
estrella **es** el nodo puente. **Es FALSA para el `acto 44`**, cuyo motivo sellado es **la guarda
`1B`** y que tiene **CERO nodos puente y CERO triangulos, medido**. **Una tabla que publica una
afirmacion que la vuelta no midio es exactamente la especie que esta campana caza**, y esta habria
publicado una falsa la primera vez que se usara fuera de su caso original.

**LA CORRECCION, POR EL CARRIL DEL ACTA 61 (`D2` y pregunta 2), que pide DOS cosas y las dos se
cumplen:** va **ENUMERADA** en el docstring de `_v72_construir_registro_lote.py` con el texto viejo
verbatim, y va **MARCADA DISCUTIBLE** aqui (`D9`). **LA TABLA NO CRECE NI SE ENCOGE:** misma fila,
misma columna; **lo unico que cambia es que la frase de esa celda la pone el CONTENIDO MEDIDO del lote
en vez de estar tecleada dentro del instrumento**. **Y el registro del `acto 27` que ya esta escrito
en la pagina NO se toca**: una correccion que reescribiera lo de arriba no se podria auditar.

> **LA PRUEBA DE QUE LA CORRECCION NO SE LLEVO NADA POR DELANTE, MEDIDA POR EL PROPIO CONSTRUCTOR:**
> `tabla_reparto` y `tabla_por_absorbido` **aparecen LITERALES** en el destino; y de `tabla_declarado`
> se comprueba **una a una** que **las 32 lineas ajenas a la correccion siguen LITERALES**. **El
> `assert` no se quito en silencio: se sustituyo por uno mas estrecho y se dice.**

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D1` . LA CLAUSULA DE `OP-L-03` NO ES LA MISMA AL BYTE QUE LA DE `OP-U-02`, Y LA CORRECCION SE
APLICO IGUAL.** El acta 71 las llama *la misma frase*; medido, **difieren en bytes** (voz activa
contra voz pasiva). **Fundi la adjudicacion sobre la SUSTANCIA y cite la letra de ESTA ficha.** **La
lectura contraria:** que una adjudicacion que se apoya en una identidad literal no cubre una frase
distinta, y que hacia falta pedir adjudicacion nueva. **No pare, porque las cuatro varas del acta 65
no dependen de las palabras exactas sino de la regla, y porque el acta 71 dice `NO ES PARADA` con esas
letras.**

**`D2` . EL `ACTO 43` FUNDE CONTRA UN CABLEADO DE 11 A 7.** La unica vara de contenido que habla es la
de **condiciones** (4 contra 2 y 2) y el cableado apunta al otro lado con el margen mas ancho del lote,
a un nodo con **DIEZ** siguientes. **Es la misma forma que el `D4` del acta 71 (el `acto 42`), que se
adjudico `A FAVOR` con las palabras UNA SOLA VARA BASTA.** **La lectura contraria:** que un cableado de
11 a 7 sobre un nodo con diez siguientes es una senal de centralidad que una sola vara de condiciones
no compensa, y que el costo de redirigir se paga en la fase 04.

**`D3` . EL `ACTO 43` CRECE DE 5 PASOS A 8, Y ES LA CIFRA MAS ALTA DE CRECIMIENTO DEL LOTE.** Tres
`APPEND` en un solo acto. **Los tres estan nombrados por las razones escritas como propios**, y dos de
ellos con las palabras *esas dos son lo que hay que salvar*. **La lectura contraria:** que la tendencia
que el `D7` del acta 71 anoto (nodos grandes) sigue subiendo y que ocho pasos empieza a ser un nodo que
nadie lee entero. **Lo traigo como medida, no como regla.**

**`D4` . EL `ACTO 46` FUNDE CON LA PUERTA COMO SUPERVIVIENTE Y LA UNICA VARA QUE HABLA APUNTA AL OTRO
LADO.** La de condiciones apunta a `gestion_eco_riesgos` (3 contra 2 y 2). **La letra es explicita**
(acta 54, pregunta 1; registrado con el `acto 20` de `OP-U-01` como precedente) y **el encargo la
repite**. **La lectura contraria:** que absorber al nodo que la vara elige, para salvar a la puerta,
paga el contenido por la topologia, que es lo que `P.8` dice que no se hace. **Fundi por la letra de la
puerta, que es anterior a `P.8`, y publique las tres cifras.**

**`D5` . `OP-S-09` SE QUEDA CON UN ALIAS QUE APUNTA FUERA DE SU FAMILIA.** Tras el `acto 46`, la
familia queda con `responsabilidad_extendida_productor_2` vivo y el otro id resolviendo a
`mitigacion_riesgos_ambientales`. **Su resolucion aprobada dice *familia unica, fusion con alias*, y
ahora tendra que ejecutarse sobre un alias externo.** **La lectura contraria:** que eso deja a la mesa
un sujeto distinto del que aprobo. **Fundi porque la cobertura es de PARTE de la nomina, que es el caso
que el acta 70 adjudico, y publique la consecuencia.**

**`D6` . LAS DOS RAZONES DEL `ACTO 45` CORONAN DISTINTO, Y AQUI LOS DOS CORONADOS SI TIENEN ARISTA.**
El precedente (`D6` del acta 70, `D5` del acta 71) se apoyaba en que el par que faltaba no tenia
arista. **Aqui `reconstruccion_contexto_situacional` y `evitar_shopping_bag` se nombran entre sus
previos y siguientes, en los dos sentidos.** **La lectura contraria:** que una arista existente entre
los dos coronados cambia la figura y pedia leer ese par antes de fundir. **Fundi por el cableado, que
es lo que `P.8` deja hablar con el contenido empatado, y lo declaro.**

**`D7` . EL `ACTO 47` FUNDE A FAVOR DEL NODO PEOR CABLEADO DEL ACTO.** El superviviente tiene **UN**
enlace y **CERO** siguientes; el cableado apunta al otro lado por **un solo enlace de diferencia**.
**La vara de pasos habla y el cableado no.** **La lectura contraria:** que elegir un nodo hoja como
superviviente de una familia lo deja sin salida en el grafo. **La letra manda y las dos razones
escritas coronan al mismo nodo.**

**`D8` . UNA FILA DE PERDIDA ES DE LA ESPECIE DEL PENDIENTE 4 EN SUSTANCIA Y NO LA CUENTA EL
INSTRUMENTO.** La del `acto 43`: la pieza llega entera desde otro absorbido del mismo acto, **pero por
un `INCISO` y no por un `APPEND`**, y la frase sellada que el instrumento busca nombra el `APPEND`.
**Lo declaro en vez de corregir el plan, porque un plan ejecutado no se re-sella** (acta 68, `D15`).
**La pregunta concreta va en la seccion 8: la especie la define el VEHICULO o el HECHO?**

**`D9` . CORREGI UNA CELDA DE UNA TABLA COPIADA Y CONGELADA.** La coletilla de la figura del
inventario en `tabla_declarado` (seccion 5). **Va enumerada en el docstring del constructor con el
texto viejo verbatim, la tabla no crece ni se encoge, y el `assert` de literalidad se sustituyo por
uno mas estrecho que comprueba las 32 lineas ajenas.** **La lectura contraria:** que la adjudicacion 3
del acta 69 congelo esas tablas y que corregir una celda **sin encargo previo** es exactamente lo que
prohibio, aunque la celda mienta. **La lectura por la que fui:** que publicar una afirmacion falsa es
peor, y que el acta 61 (`D2` y pregunta 2) da el carril con sus dos condiciones cumplidas.

**`D10` . EL ACTO QUE ENTRA A LA LISTA DE DECLARADOS ES DE UNA ESPECIE NUEVA.** Los catorce anteriores
esperan por `P.10` o por su familia; **el `44` espera por sus DOS PUERTAS**, que es una pregunta
distinta y que el cierre de la fase 03 va a tener que contestar aparte. **Lo digo porque cambia lo que
ese cierre va a encontrar, no porque dude de la guarda.**

**`D11` . ESTRENE TRES FICHEROS DE AGUJA NUEVOS EN EL REGISTRADOR DEL ACTA.** `OPERACIONES.jsonl`,
`generar_plan_del_lote.py` y `banco_rumbos.json`, para citar la sede de cada correccion por aguja.
**Sostengo que no es maquina nueva** (`AGUJAS` siempre fue un mapa `CLAVE -> (fichero, aguja)` y el
fichero es un dato). **La lectura contraria:** que buscar agujas fuera de la pagina y del acta amplia
el alcance del instrumento sin encargo.

**`D12` . LOS CINCO `INCISO` DEL LOTE SON LA CIFRA MAS ALTA DEL TRAMO, Y DOS VAN AL MISMO ACTO.** El
`47` recibe dos, a pasos distintos (la letra del acta 64 pide que no se apilen, y no se apilan).
**La lectura contraria:** que un acto que recibe dos `INCISO` esta reescribiendo dos pasos del
superviviente a la vez y que eso es redaccion, no fusion. **Lo hice porque las dos razones escritas
nombran esas dos lineas como *lo unico propio* de cada absorbido y una de ellas ademas ENRUTA la suya
con las palabras *se absorbe en el*.**

**`D13` . EL `ACTO 45` CIERRA SIN UNA SOLA PERDIDA DE PASO, Y ES LA PRIMERA VEZ EN EL TRAMO.** Diez
piezas de paso de dos absorbidos, todas dentro. **La lectura contraria:** que un reparto sin ninguna
perdida de paso suele ser un reparto que no miro bastante. **La vara: las dos razones escritas cierran
las dos con *no le queda ni una linea propia*, y el `APPEND` y el `INCISO` recogen las dos unicas que
si le quedaban a `evitar_shopping_bag`.**

---

## 7. LAS AVERIAS PROPIAS, CAZADAS ANTES DE UNA CIFRA PUBLICADA

**CERO de ellas llego a una cifra publicada ni a un dato movido**, y **las CINCO las cazo un
instrumento o una lectura.**

### 7.1 **CORRI `recomputar_marcador.py` SIN SU ARGUMENTO OBLIGATORIO**

La primera corrida del marcador de apertura cayo en **`error: the following arguments are required:
corte`** y **no escribio ninguna cifra**. Corregida pasando el corte `3388`. **La cazo el propio
`argparse`**, y **el fichero de salida vacio se borro antes de commitear nada**.

### 7.2 **LOS DOS PRIMEROS `ROTULO` QUE ESCRIBI NO HABLABAN LA GRAMATICA DEL BARRIDO**

Escribi `ROTULO titulo="..." cita=... fuente="..." nota="..."` en los dos instrumentos nuevos de la
`TAREA 1`, **sin el campo `especie=` que el barrido exige**, con lo que **el barrido los ignoro
enteros** y `vuelta72_ancla_duplicada.py` quedo en **`AMBAR`** por decir *VUELTA 71* en su cabecera.
**Lo vi corriendo el barrido, no leyendo el fichero.** Corregido: **el del ancla se reescribio en la
gramatica `PROCEDENCIA`** (y el `AMBAR` bajo a **0**), y **el de la ficha de `OP-L-03` se QUITO**,
porque **no cubria ningun `AMBAR` vivo y un rotulo asi es HUERFANO, que el barrido cuenta en `ROJO`**.

### 7.3 **LA AGUJA DEL BORDE DEL ACTA APUNTABA A UNA LINEA QUE NO EXISTIA**

La clave `A71_ADJ2_BORDE` buscaba `EL BORDE QUEDA DICHO: esta adjudicacion descansa en esa` y **el acta
parte esa frase de otro modo**: la linea real empieza en `EJECUTARLA, no usurparla.`. **El registrador
cayo en `ROJO` con `aparece 0 veces` y NO escribio nada**, que es para lo que esta. Corregida leyendo
la linea real, **y el texto se ajusto para decir que la cita verbatim arranca a mitad de frase en vez
de recortarla.**

### 7.4 **DOS ANCLAS DEL TEXTO DEL LOTE QUEDARON DERIVADAS Y SIN USAR**

`PAG_CORR_OPL03` y `PAG_CORR_PREFIJO`. **La guarda de citas del propio registrador las cazo** (*hay 2
agujas derivadas que el texto no usa*) **y no escribio nada**. Corregido **anadiendo el bloque que
dice cual de las tres correcciones muerde sobre este lote y que cambia cada una**, que es contenido
que faltaba y no relleno para callar una guarda.

### 7.5 **LA AGUJA DE LOS AUTO-PARES ESPERADOS LEIA LA LINEA EQUIVOCADA**

Pedia `AUTO-PARES\s+: (\d+)$` sobre la salida de esperadas, que ahi es **el total** y no el delta, y
la expresion no casaba con ninguna linea. **El registrador cayo en `ROJO` con `no se pudo leer
auto-pares esperados` y no escribio nada.** Corregida apuntando a **`auto-pares NUEVOS (pares internos
del acto)`**, que es la cifra que el texto queria publicar, **y la celda del texto se renombro para
decir NUEVOS y no confundir un delta con un total.**

> **NINGUNA DE LAS CINCO LLEGO A UNA CIFRA PUBLICADA**, y **cuatro de las cinco las cazo un
> instrumento cayendo en `ROJO` sin escribir**, que es la diferencia entre una averia y una caida.
> **La 7.2 la cazo un censo del cierre corrido antes de tiempo a proposito.**

---

## 8. PENDIENTES DE DOCTRINA Y PREGUNTAS

1. **EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE** (heredado): los actos declarados que esperan el
   cierre de la fase 03 pasan de **CATORCE a QUINCE**, **y el que entra no es por `P.10`**. **Ya no
   puede crecer por `P.10` en este tramo**, medido: **cero puentes en los 6 que quedan**.
2. **NUEVA, Y ES DE INSTRUMENTO: LA ESPECIE DEL PENDIENTE 4 LA DEFINE EL VEHICULO O EL HECHO?** La
   fila del `acto 43` cumple el HECHO (la pieza llega entera desde otro absorbido del mismo acto) por
   un vehiculo distinto (`INCISO` y no `APPEND`). **La pregunta concreta: la frase sellada que el
   instrumento busca deberia nombrar el hecho en vez del vehiculo, o son dos especies distintas?** **No
   invente regla, no re-selle el plan ejecutado y lo traigo marcado (`D8`).**
3. **NUEVA: LA ADJUDICACION 3 DEL ACTA 69 CUBRE UNA CELDA QUE MIENTE?** Congelo las tablas de los
   registradores. **La pregunta concreta: cuando una celda copiada publica una afirmacion FALSA para
   el caso nuevo, se corrige por el carril del acta 61 (enumerar mas marcar discutible) o hay que
   parar y pedir encargo?** **Fui por el carril del acta 61 y lo traigo marcado (`D9`).**
4. **NUEVA: EL ACTO DECLARADO POR LA GUARDA `1B` ES UNA ESPECIE DISTINTA EN LA LISTA DE LOS QUE
   ESPERAN.** **La pregunta concreta: el cierre de la fase 03 tiene que tratar al `44` como a los
   catorce de `P.10`, o su motivo pide otra salida?** **Lo traigo marcado (`D10`) y no lo decido.**
5. **LA MARCA PARA *YA LO DICE EL `APPEND` DE UN HERMANO*** (heredado): **esta vuelta la paga UNA
   vez**, y **por `INCISO`**, que es lo que abre la pregunta 2 de arriba.
6. **EL `INCISO` DE CONDICIONES SIGUE SIN EXISTIR** (heredado): **siete perdidas `DE CONDICIONES`** en
   esta vuelta, **la cifra mas alta del lote y mas de la mitad del total**, enrutadas a la fase 04 por
   el carril del acta 55, pregunta 5.
7. **EL ESQUEMA DE `OPERACIONES.jsonl`** (heredado): sigue pendiente, y **esta vuelta SI toco una
   ficha** (`OP-L-03`, `git diff --numstat`: **`1 1`**) **pero NO estreno ninguna clave**: la
   correccion entro como un elemento mas de una lista que ya existia, y **las 71 fichas siguen con 18
   claves cada una**, medido antes y despues.

---

## 9. RUTAS TOCADAS Y CENSOS AL CIERRE

**Del grafo (40 ficheros):** los **cuatro supervivientes** (`preservar_efectivo_buscar_modelo`,
`reconstruccion_contexto_situacional`, `mitigacion_riesgos_ambientales`,
`gestion_terminacion_franquiciado`), sus **ocho absorbidos** (`escalamiento_prematuro`,
`restriccion_gasto_validacion`, `evitar_sesgo_retrospectivo_hindsight`, `evitar_shopping_bag`,
`gestion_eco_riesgos`, `responsabilidad_extendida_productor`, `perdida_control_operativo`,
`terminacion_franquiciado_causas`), los **redirigidos** (30 referencias sobre nodos vivos), mas
`dataset/metadata/master_graph.json` y `dataset/metadata/phase1_run_log.json`. **NI UN NODO DEL `ACTO
44` SE TOCO.**

**Del registro:** `docs/plan/03_FUSIONES.md` (**`+246`** del acta 71 y **`+498`** del lote H, **cero
borradas en los dos**), `docs/plan/OPERACIONES.jsonl` (**`1 1`**, la correccion declarada de
`OP-L-03`), `docs/plan/ARISTAS_DUPLICADAS.jsonl`, `docs/COSTURAS_INTERNAS.jsonl` y su resumen,
`scripts/rumbos/banco_rumbos.json` (**`0 1`**, el ancla depurada) y `web/lib/assets/` por el `sync`.
**`docs/plan/INVENTARIO.jsonl` y `docs/RACIMOS_MIEMBROS.jsonl` NO se tocaron** (`git diff --numstat`
sobre los dos: vacio).

**Instrumentos nuevos (NUEVE, contados por maquina con `git diff --name-status --diff-filter=A
1dd2cccd..HEAD -- scripts/`): NINGUNO de nombre estable**, los nueve son de vuelta:
`_v72_construir_registrador_acta.py`, `_v72_texto_acta71.py`, `vuelta72_registrar_acta71.py`,
`vuelta72_correccion_ficha_opl03.py`, `vuelta72_ancla_duplicada.py`, `_v72_lote_h.py`,
`_v72_construir_registro_lote.py`, `_v72_texto_lote_h.py` y `vuelta72_registro_lote_h.py`. **Y UN SOLO
instrumento de nombre estable se MODIFICO**, contado por la misma via (`--diff-filter=M`):
**`generar_plan_del_lote.py`**, por la **CORRECCION DECLARADA** de la `TAREA 1`. **Esta vuelta NO crea
ningun instrumento de medida nuevo.**

| censo al cierre | valor |
|---|---|
| **barrido de titulos** ([`SALIDA_V72_BARRIDO.txt`](SALIDA_V72_BARRIDO.txt)), **re-corrido AL CIERRE** | **479 ficheros**, `ROJO` **32** (**linea base heredada, EN SU SITIO**), **`AMBAR` 0**, `ROTULADO` **54**, `CENSO` **225**, `ILEGIBLE` **1** |
| **censo de plantillas talladas** ([`SALIDA_V72_CENSO_PLANTILLAS.txt`](SALIDA_V72_CENSO_PLANTILLAS.txt)) | **CERO TALLADOS** sobre **26** instrumentos de nombre estable |
| **estado de las operaciones** ([`SALIDA_V72_CIERRE.txt`](SALIDA_V72_CIERRE.txt)) | **71**, todas `LISTA`, **0** dependencias rotas, **672** entradas, enlaces **17.663** |
| **casos positivos** ([`SALIDA_V72_CASOS_POSITIVOS.txt`](SALIDA_V72_CASOS_POSITIVOS.txt)) | **SEIS, y los seis sobre sujetos que esta vuelta NO toca**: mesa **LAS NUEVE** sobre `OP-M-02-ACCLIMATE`; contrato de perdidas **LAS CUATRO**; varas **LAS TRES mitades**; promesas **LAS DOS mitades**; cuenta agregada **LAS CINCO mitades**; y el del generador, **que esta vuelta mira con mas cuidado porque su `TAREA 1` corrigio ese instrumento** |
| **promesas de marcado** ([`SALIDA_V72_PROMESAS.txt`](SALIDA_V72_PROMESAS.txt)), **cotejadas por maquina ANTES de sellar este reporte** | **3 de 3 CUMPLIDAS**, cero incumplidas: los actos **43** (dos promesas) y **46** prometieron marca en su motivo o en su nota y **la seccion 6 la trae** |
| **cabecera del reporte** ([`SALIDA_V72_CABECERA_COMPARADA.txt`](SALIDA_V72_CABECERA_COMPARADA.txt)) | **`CABECERA: IDENTICA AL TALLADOR`**, **14** filas cotejadas, **DISTINTAS 0**, ausentes **0** |
| **codificacion de las salidas** | **54** ficheros de salida de la vuelta barridos por maquina, **CERO fuera de `UTF-8`**, y **ninguno se toco despues de generarse** (adjudicacion 5 del acta 71 aplicada desde el primer minuto con `PYTHONIOENCODING=utf-8`) |

> **EL `ROTULADO` SUBE DE 51 A 54 Y NO SE DEJA COMO UN NUMERO QUE CAMBIA SOLO:** son **los tres
> rotulos de los tres ficheros nuevos que los llevan** (`vuelta72_registrar_acta71.py`,
> `vuelta72_registro_lote_h.py` y `vuelta72_ancla_duplicada.py`); **los dos primeros EXTRAIDOS del
> ancestro y no tecleados**, y **el tercero escrito a mano y corregido tras la averia 7.2**. **El
> `CENSO` sube de 224 a 225 por el fichero nuevo de la correccion de la ficha**, y **el `ROJO` no se
> mueve de su linea base de 32.**

### 9.1 **LA TASA POR DOMINIO AL CIERRE, IDENTICA A LA DE APERTURA**

**Fundir no volteo ni un veredicto**, y por eso el marcador de cierre sale **identico** al de apertura,
**las diez lineas**, comprobado por `diff` entre las dos salidas del tallador de marcador.

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

([`SALIDA_V72_TRAMO_CIERRE.txt`](SALIDA_V72_TRAMO_CIERRE.txt),
[`SALIDA_V72_PUERTAS_DE_LOS_QUE_QUEDAN.txt`](SALIDA_V72_PUERTAS_DE_LOS_QUE_QUEDAN.txt) y
[`SALIDA_V72_PUENTES_DE_LOS_QUE_QUEDAN.txt`](SALIDA_V72_PUENTES_DE_LOS_QUE_QUEDAN.txt))

| | |
|---|---:|
| actos del tramo unico | **47** |
| actos **FUNDIDOS**, medido sobre el grafo | **26** |
| actos **`DECLARADOS Y NO FUNDIDOS`** | **15** |
| **quedan sin destino** | **6 actos y 18 nodos** |
| **el siguiente del prefijo** | el acto **31**, **con dueno** (`OP-F-04-WEI`, `OP-S-04`) |
| **el primero SIN dueno** | el acto **49** |
| de los que quedan, **con dueno medido** | **2** (los actos **31** y **37**) |
| de los que quedan, **con nodo puente** | **0** |
| de los que quedan, **con par `D` interno** | **0** |
| de los que quedan, **con puerta dentro** | **2** |
| **actos declarados que esperan el cierre de la fase 03** | **15** |

> **LAS PUERTAS DE LOS QUE QUEDAN SE MIDEN CON SU SALIDA COMMITTEADA:** de los **6**, **DOS traen
> puerta**, y van nombradas una a una. El **`31`**: `captura_conocimiento_mercado` (y ademas tiene
> dueno). El **`51`**: `metodo_valor_presente_neto`. **Los dos funden con su puerta sobreviviendo
> cuando les toque** (acta 54, pregunta 1), **y NINGUNO de los dos puede cerrar `DECLARADO` por la
> guarda `1B`, porque esa guarda pide DOS**. **El `44`, que era el unico que traia dos, ya cerro en
> este lote.**
>
> **LAS FORMAS DE LOS 6, MEDIDAS:** **4 `UNA SOLA VARA`** (los `37`, `49`, `50` y `51`), **1 `CHOCAN`**
> (el `31`) y **1 `TODAS DE ACUERDO`** (el `53`). **Los 6 siguen siendo de tres miembros con dos pares
> `A` y uno sin veredicto, cero puentes y cero `D` internos.**

**NO SE FUNDIO NINGUN ACTO CON DUENO** (el `31` y el `37` quedan con los suyos), **no se toco la mesa
`OP-M-03` ni sus dos colisiones**, **las cinco colisiones de `OP-U-02` ya publicadas siguen vigentes
con su duena**, **no se toco ni un nodo del `acto 44` ni sus dos puertas**, y **las cinco fichas
`OP-M-02` consumidas no se ejecutaron**: lo consumado no se ejecuta ni se rehace.

---

## 11. CONDICIONES DE PARADA, RECORRIDAS

| condicion | hoy |
|---|---|
| **doctrina nueva** | **NO**. Todo va por extension citable: la guarda `1B` (acta 65, apartado c), la puerta unica (acta 54, pregunta 1), la frontera del dueno (acta 68 adj. 2, acta 70 adj. 2, acta 71 adj. 2 con su borde), el banco `9.10`, el carril del acta 61 para la celda corregida, y `P.16` por su principio para el ancla |
| **contradiccion sin regla** | **NO**. Las tres preguntas nuevas de la seccion 8 van marcadas y **ninguna bloqueo la operacion** |
| **decision de fundador** | **NINGUNA SE TOMA**. El merge sigue siendo suyo |
| **fallo tecnico repetido** | **NO**. Gate 0 y las tres suites en verde |
| **credito de tanda roto** | **NO**. El contador entro en **CERO** y esta vuelta no publica ninguna cifra movida |
| **campana consumada** | **NO** |
| **CIERRE DE LA FASE 03** (la parada del fundador) | **NO SE CUMPLE TODAVIA**: quedan **6 actos sin destino (18 nodos)**, dos de ellos con dueno (`31` y `37`), la mesa `OP-M-03`, y **los QUINCE declarados esperan** |
| **credenciales** | no hicieron falta |

---

## 12. HASH FINAL Y COMMITS

**Los commits de esta vuelta en `pasada-unica`, en orden:**

| commit | que trae |
|---|---|
| **`a3bc1153`** | **TAREA 1 entera**: el registro del acta 71 (`+246`, `0` borradas, 59 agujas, tres negativas de sustancia) **mas las TRES CORRECCIONES DECLARADAS** (la ficha de `OP-L-03`, el prefijo del generador y el ancla duplicada del rumbo) **y la APERTURA medida antes de la primera operacion**, con toda salida escrita en `UTF-8` desde el origen |
| **`c4c38956`** | **TAREA 2, paso 1**: el lote `H` **declarado al abrirlo** y su **plan sellado dos veces**, con el `P.5`, las varas, el borde del dueno medido y **las colisiones esperadas sobre base 7**, todo **ANTES DE TOCAR UN NODO** |
| **`90df5a9f`** | **TAREA 2 ejecutada**: las cuatro fusiones, el `acto 44` `DECLARADO` por la guarda `1B`, `P.16`, el reanclaje, `Gate 0` con su ciclo de tres, las tres suites y **el registro del lote `H`** (`+498`, `0` borradas) |
| **este** | el reporte |

**El hash final de la vuelta y la cadena entera van escritos en la cabecera de esta seccion por un
commit posterior**, que es lo que la regla 7 pide y lo que el commit del reporte no puede contener: un
commit no puede llevar su propio hash. **Misma via que las vueltas 69, 70 y 71 usaron en sus commits
`a943673c`, `66ef6d38` y `fd46adc3`.**
