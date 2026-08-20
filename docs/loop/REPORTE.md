# REPORTE DE LA VUELTA 47 (19 ago 2026, ejecutor Opus 5)

**LA PARADA SE LEVANTA. La decision del fundador esta registrada con sus cuatro
correcciones, la frontera del 1298 re-declarada, `OP-D-07` SELLADA, el marcador del
`00_INDICE` impreso con instrumento nuevo, el orden de la fase 03 adjudicado por
criterio citable y `OP-U-01` ABIERTA con su lectura de cero. CERO NODOS TOCADOS.**

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash final** | **`d5c4d64b`**, pusheado a `origin/pasada-unica` |
| **hash de apertura** | `a47edcc9` (la decision del fundador), arbol limpio |
| **commits de la vuelta** | **3**, uno por tarea: `62c10658`, `c63be8aa`, `d5c4d64b` |
| **nodos tocados** | **CERO.** `git status` sobre `dataset/` da **0** ficheros en toda la vuelta |
| **ficheros tocados** | **31**: 21 altas en `docs/loop`, 5 altas en `scripts/loop`, 5 modificados en `docs/plan`. **CERO borrados** |

---

## 0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (regla 1)

**Corrida ANTES de tocar nada**, con `python scripts/loop/vuelta31_estado.py APERTURA_V47`
(`SALIDA_V47_APERTURA.txt`). El arbol estaba **limpio** y **todo pusheado** en
`a47edcc9`, asi que la regla 3 (commitear lo pendiente antes de tocar nada) **se cumplio
por vacio, y se dice asi en vez de darla por cumplida**.

| | apertura | **cierre, recomputado** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 575 / 79 / 8 / 2.726 | **575 / 79 / 8 / 2.726** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.524 / 329 / 16.898 | **3.853 / 3.524 / 329 / 16.898** |
| cola de costuras | (no medida en apertura) | **1.494 sobre 3.524** |

**El cierre esta RECOMPUTADO al cierre** (`SALIDA_V47_CIERRE.txt`,
`SALIDA_V47_COLA.txt`), no copiado de la apertura: es la regla que la vuelta 28 estreno.
**Ni una cifra se movio, y el motivo es que esta vuelta no tenia por que moverlas: no
ejecuto ninguna cirugia.**

---

## 1. TAREA 1: LA DECISION DEL FUNDADOR, REGISTRADA . commit `62c10658`

**LA RAMA ES LA (a)** y **EL CRITERIO SE CITA EN LAS CUATRO CORRECCIONES**, con las
palabras del fundador: *cuando dos textos sellados chocan, GANA EL QUE APLICO LA REGLA
MAS RECIENTE DEL FUNDADOR, y el perdedor se corrige*. **Gana la fase 01 del 14 ago 2026**
(`P.18` punto 3, nodo propio); **pierden los cuatro textos del 12 ago 2026.**

### 1.1 LOS CUATRO TEXTOS, CORREGIDOS CON TACHADO, FECHA Y CITA

**Tres de los cuatro se escribieron con instrumento** y no a mano:
`python scripts/loop/vuelta47_correcciones_p18.py --escribir`
(`SALIDA_V47_CORRECCIONES_P18.txt`, exit 0).

| # | texto del 12 ago | donde | como quedo |
|---:|---|---|---|
| **1** | `verificacion` punto 2 de `OP-D-07` | `OPERACIONES.jsonl` | tachado + correccion declarada citando `P.18` punto 3 y `01_FUENTES` linea 982 |
| **2** | campo `preservar` de `OP-M-03-I` | `OPERACIONES.jsonl` | tachado + lo que la fusion SI tiene que hacer: **no tocar el bloque y no perder su arista** |
| **3** | `verificacion` punto 3 de `OP-M-03-I` | `OPERACIONES.jsonl` | tachado + las **tres** comprobaciones medibles que la sustituyen |
| **4** | la fila del bloque, linea 82 | `FRONTERAS_DECLARADAS.md` | tachada + *no llega por ahi porque ya no sale de ahi* |

**GUARDAS DEL INSTRUMENTO, todas en verde:** 72 lineas antes y 72 despues; **4 campos
escritos en 2 operaciones**; **69 de 71 lineas intactas byte a byte**; el texto viejo
**sigue dentro del nuevo en los tres casos**, comprobado por el propio instrumento; y
**cero guiones largos y cero medios** en el fichero entero.

### 1.2 LA FRONTERA DEL 1298, RE-DECLARADA CON SUS DOS LADOS MEDIDOS HOY

**Medida con `python scripts/loop/vuelta47_frontera_1298.py`**
(`SALIDA_V47_FRONTERA_1298.txt`, exit 0, **solo lectura**). **No se copio nada de la
pagina del 12 ago.**

| | medido el 19 ago 2026 |
|---|---|
| **lado del punto brillante** | **`puntos_brillantes_antes_del_pivote`**: **5 de 5** huellas del bloque, contra **0 de 5** en `pivotar_o_perseverar` y **0 de 5** en `decision_pivote_perseverar`. Fuente `Traction - Gabriel Weinberg` **sola** |
| **lado de decidir rapido** | **SIN CAMBIO**: paso **3** de `pivote_startup`, *Decide con rapidez y sin miedo al fracaso si toca pivotar*. Fuente `The Startup Owner's Manual - Steve Blank`. Viaja al acto por `OP-M-03-III`, **no ejecutada** |
| **entre libros** | **SIN CAMBIO**: Ries mas Traction contra Blank, **medido en las dos fuentes** |
| **la arista** | el nodo propio cuelga **HOY del sujeto**, medido en los dos sentidos; **`pivotar_o_perseverar` todavia no lo nombra en ningun campo**. Al morir el sujeto en `OP-M-03-I` la arista **se redirige a la puerta** |

**Y queda escrito lo que la re-declaracion PROHIBE: el bloque no se mete dentro de la
puerta.** Absorberlo en la fusion del acto I seria deshacer `P.18` punto 3.

### 1.3 `OP-D-07` SELLADA

**Por la via de `OP-D-05` SELLADA, citada por su nombre** y por sus dos lineas (1765 y
1773 de `02_DESTEJIDOS.md`). Las tres verificaciones al cierre: **1 y 3 CUMPLEN**
medidas en la vuelta 46, y **la 2 CUMPLE ENTERA** porque su mitad de ruta dejo de estar
en PARADA. **El campo `estado` no se toca: sigue `LISTA`**, por el motivo escrito en las
notas de `OP-F-02` y `OP-D-04`, que el encargo cita.

### 1.4 LO QUE SE MOVIO, RECOMPUTADO POR EL CARRIL DEL BANCO 9.10

**Se movio UNA cifra, y se barrio su tabla derivada en el mismo acto**, con el mismo
instrumento de la vuelta 46 (`SALIDA_V47_CIERRE_FASE02_REMEDIDO.txt`, exit 0):

| | vuelta 46 | **vuelta 47** |
|---|---:|---:|
| operaciones de la fase 02 con registro de cierre | 8 de 9 | **9 de 9** |
| con la frase de la vuelta 30 | 5 de 9 | **5 de 9** |
| con encabezado `CERRADA` o `SELLADA` | 4 de 9 | **5 de 9** |

**El marcador NO se movio** (tabla de la seccion 0). **La cifra vieja se queda delante y
no se borra.**

---

## 2. TAREA 2: EL MARCADOR DEL `00_INDICE`, IMPRESO . commit `c63be8aa`

**INSTRUMENTO NUEVO: `scripts/loop/vuelta47_marcador_indice.py`** (solo lectura).
Cuenta `OPERACIONES.jsonl` fase por fase y estado por estado y **escupe la tabla en
markdown, lista para pegar entera**. Salida en `SALIDA_V47_MARCADOR_INDICE.txt`, exit 0.

**LA TABLA PEGADA, tal como el instrumento la imprime:** **71 operaciones, 71 LISTAS, 0
DECISION PENDIENTE**; por fase **7, 7, 9, 16, 10, 10, 5, 2, 1, 3, 1**.

### LAS CUATRO FILAS RANCIAS, RE-MEDIDAS

| fila | publicaba | **medido hoy** | por que se movio |
|---|---:|---:|---|
| operaciones | 69 | **71** | nacieron `OP-D-08` y `OP-D-09` el 14 ago |
| 0 CODIGO | 5 | **7** | `OP-S-06` y `OP-S-07` entraron a la fase 0 |
| 02 DESTEJIDOS | 7 | **9** | las dos operaciones nuevas |
| 05 SANEO | 12 | **10** | las dos que se fueron a la fase 0 |

**Calzan al digito con lo que el auditor midio en la vuelta 46**, y se **re-midieron**
aqui en vez de copiarse.

**Y DOS CELDAS MAS que el conteo de filas no cuenta y se dicen igual:** `03 FUSIONES`
publicaba **15 LISTAS y 1 pendiente** y hoy son **16 y 0**, porque `OP-U-02` paso a
`LISTA` en la vuelta 12; en consecuencia el total de LISTAS va de **68 a 71** y el de
pendientes de **1 a 0**.

### EL BARRIDO DE LAS TABLAS DERIVADAS, EN EL MISMO ACTO

| donde | que decia | **corregido a** |
|---|---|---|
| linea 9, la frase de cierre del plan | 69 operaciones, 68 LISTAS, **quince** reglas | **71, 71, cero pendientes, VEINTE reglas** (`P.1` a `P.20`, contadas por el instrumento) |
| la celda de HECHO de la fase 2 | *las **siete cirugias** hechas* | **las NUEVE operaciones**, y ademas: *cirugias* ya no calza, porque `OP-D-05` y `OP-D-07` quedaron `SELLADA`s con su destejido **consumido por la fase 01** |
| `EL ESTADO EN QUE QUEDA TODO` (cierre de la sesion B) | 69 / 68 / 1 / 15 / 336 / corte 2.117 | marcada con **SU** corte y con la columna de hoy al lado: **71 / 71 / 0 / 20 / 672 / corte 3.388** |

**Las dos filas de lecturas dirigidas (65 hechas, cero encargadas) van marcadas A
VERIFICAR y NO se republican**: ningun instrumento corrido en esta vuelta las cuenta, y
**una cifra sin medicion de hoy no se republica**.

**EL MARCADOR VIEJO SE QUEDA ENTERO, TACHADO Y CON SU FECHA.**

---

## 3. TAREA 3: EL ORDEN DE LA FASE 03, Y `OP-U-01` ABIERTA . commit `d5c4d64b`

### 3.1 EL CRITERIO, ADJUDICADO POR CITA Y NO POR PREFERENCIA

Medido con `python scripts/loop/vuelta47_orden_fase03.py`
(`SALIDA_V47_ORDEN_FASE03.txt`, exit 0). **La adjudicacion entera vive en
`docs/plan/03_FUSIONES.md`, seccion `EL ORDEN DE ESTA FASE`**, que es donde la fase 02
tiene la suya.

1. **EL EMPATE ES REAL Y ESTA CONTADO**: `OP-M-02-PROG`, `OP-M-03-I` y `OP-U-01`, las
   tres en `orden` 1.
2. **LA VARA DE LA FASE 02 APLICADA LITERAL NO LO ROMPE, y se dice.** Queda **UN** solo
   congelado abierto en todo el archivo, el **1190**, **y lo libera `OP-M-04`**, que es
   de la fase 06. **Las tres empatadas liberan CERO.** No es un fallo de la vara: **en
   la fase 03 no quedan congelados que liberar.**
3. **LA MISMA VARA EN SU FORMA GENERAL SI LO ROMPE, y es citable.**
   `docs/PENDIENTES.md`, seccion `ORDEN DE LA PASADA`, adjudicado el **14 ago 2026**:
   *el criterio de orden no es el tamano del nodo ni lo averiado que este: es **CUANTOS
   PARES DESBLOQUEA***. En una fase sin congelados, **lo que cada operacion desbloquea
   lo escribe el propio plan en `depende_de`**:

| operacion empatada | **desbloquea** | a quien |
|---|---:|---|
| **`OP-U-01`** | **2** | `OP-U-02` y `OP-S-12` |
| `OP-M-03-I` | 1 | `OP-M-03-ENLACES` |
| `OP-M-02-PROG` | **0** | a nadie |

4. **UN SEGUNDO CRITERIO CITABLE QUE CONVERGE**, puesto detras y no delante: la cabecera
   de `03_FUSIONES.md` del **11 ago 2026** (*se escriben HOY las fusiones de los actos
   QUE YA NO PUEDEN CRECER*, que **es `OP-U-01` literalmente**) y la **atadura 2** del
   `00_INDICE` (`OP-S-12` al final, despues de la ultima fusion).
5. **LAS TRES ESTAN DESBLOQUEADAS**, comprobado dependencia por dependencia contra fases
   con **cierre declarado y citable**. **No se renumera el campo `orden`**: el artefacto
   queda declarado, como con `OP-D-08` y `OP-D-09`.

> **`OP-U-01` VA PRIMERA. No hubo que parar: habia criterio citable, y dos.**

### 3.2 `OP-U-01` ABIERTA, CON CERO NODOS TOCADOS

`python scripts/loop/vuelta47_lectura_opu01.py` (`SALIDA_V47_OPU01_LECTURA.txt`, exit 0),
sobre la nomina que produce el instrumento de la casa
`scripts/plan/recomputo_3388.py --salida docs/loop/RECOMPUTO_V47_COMPONENTES.jsonl`
(resuelve por alias **antes** de contar, `P.1`; sus **cuatro comprobaciones** de
`08_VERIFICACION` salieron **todas OK**).

**TRES CIFRAS DEL MISMO OBJETO QUE NO CUADRAN, DECLARADAS Y NO RESUELTAS COPIANDO:**

| de donde sale | actos | nodos | CERRADOS | nodos | ABIERTOS |
|---|---:|---:|---:|---:|---:|
| lo que **publica** `OP-U-01` (vuelta 12) | 335 | 854 | 280 | 600 | 55 |
| el **fichero sellado** de hoy, contado linea a linea | 332 | 838 | 278 | 595 | 54 |
| **lo que mido hoy** | **324** | **822** | **270** | **579** | **54** |

- **Del sellado a hoy: EXPLICADA Y CUADRA AL DIGITO.** **Ocho** nodos que la sellada
  contaba estan **hoy deprecados** por fusiones de las fases 01 y 02, **nombrados uno
  por uno** en la pagina; ocho nodos, ocho actos menos, ocho cerrados menos.
- **De lo publicado al sellado: NO la explico**, es **anterior a esta vuelta** y **va
  como pregunta**. Reescribir una de las dos sin saber cual envejecio es lo que la regla
  2 prohibe.

**EL LOTE REAL DE HOY: 270 actos cerrados, 579 nodos, 309 moririan si se funden todos**
(235 de dos, 31 de tres, 4 de cuatro). **GUARDA DE LOS CUATRO AJENOS EN VERDE**:
`ab_testing_optimizacion` y `brainstorming_divergente` ya no estan en ninguna componente,
y los de **13** y **9** aparecen **ABIERTOS**, no cerrados.

**POR QUE NO SE FUNDE NI UN ACTO EN LA VUELTA QUE LA ABRE, dicho en vez de declararla
hecha:** el campo `superviviente` de `OP-U-01` es `null` y su campo `nodos` es lista
vacia: **la operacion no trae escrito quien sobrevive en ninguno de los 270 actos**.
**NO es PARADA**, porque la regla para elegirlo si esta escrita y es citable (las dos
reglas de ejecucion de la pagina mas `P.8`); pero **obliga a 270 lecturas de contenido**,
que es trabajo de varias vueltas y **no cabe en la que la abre**. Se entrega **el primer
paso de la forma asentada de la campana** (lectura de cero y lote sellado), y **el resto
queda nombrado, no insinuado**.

---

## 4. GATE 0 Y LAS SUITES

**Ciclo corrido DOS veces, tras la TAREA 2 y de cierre. Los seis comandos exit 0.**

| que | como salio |
|---|---|
| **Gate 0**, ciclo de **TRES** comandos | `run_phase1 --reaplico-curaduria` con **`GATE 0: OK`**; `etiquetas_de_cara --aplicar` con **71** etiquetas; `sync_assets_web` con **6** assets |
| **el comando 4** | **NO corre, y es correcto**: el censo no se movio (dataset en cero) |
| `phase1_run_log.json` | respaldado antes y **restaurado byte igual** las dos veces, md5 `dfa6fc2d3e9ce275729047f65fefe446` |
| **suite del motor** | **25 de 25**, exit 0 |
| **suite web** | **80** ficheros, **1.030** pasadas y **3** saltadas, exit 0 |
| **`tsc --noEmit`** | **CERO** lineas, exit 0 |
| **hook guardian** | **verde en los tres commits** |

---

## 5. CORRECCIONES DECLARADAS SOBRE MI PROPIO TRABAJO

**Tres, las tres vistas ANTES de publicar y las tres con el texto viejo delante:**

1. **EL SELLO DE `OP-D-07` ESCRIBIA LA FRASE DE LA VUELTA 30 PARA NEGARLA.** El
   localizador de `vuelta46_cierre_fase02.py` la busca **como texto plano**, asi que la
   seccion se contaba **en las dos formas** (6 de 9 y 5 de 9) y la tabla del cierre
   habria mentido. Reescrita sin la frase: hoy **5 y 5**. **El motivo queda escrito
   dentro de la propia seccion** para que nadie lo repita.
2. **EL LECTOR DE CONTRASTE DEL INSTRUMENTO DEL MARCADOR SE TRAGABA MIS PROPIAS TABLAS.**
   Leia todo lo que seguia a `## EL MARCADOR`, incluidas la tabla vieja tachada y la de
   correcciones, que **traen las cifras rancias a proposito**: daba **4 filas sin
   calzar DESPUES de pegar la buena**. Acotado al bloque del marcador **VIGENTE**, hoy
   da **12 de 12 SI y CERO filas sin calzar**. **El limite queda escrito en el codigo.**
3. **EL GUARDA DE GUIONES DE MI PROPIO INSTRUMENTO LLEVABA LOS DOS CARACTERES
   LITERALES.** Pasan a escape; el fichero queda con **cero guiones largos y cero
   medios**, que es lo que la regla 10 pide de **todo** lo que se escribe.

---

## 6. UN HALLAZGO QUE NO ES MIO Y SE DECLARA

**`scripts/plan/recomputo_3388.py` se anuncia como *estrictamente de solo lectura* y
ESCRIBE `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` POR DEFECTO.** La primera corrida
de esta vuelta **piso la nomina sellada** (332 lineas a 324). **Restaurada con
`git checkout`, comprobada de vuelta en sus 332 lineas, y la corrida repetida con
`--salida` apuntando fuera de `docs/plan/`.** **El fichero sellado NO aparece en el
`git status` de esta vuelta.**

> **Recomendacion: que ese instrumento EXIJA `--salida` en vez de traerla puesta.** Un
> instrumento que dice no escribir y escribe es la especie del canon 9 (fallar ruidoso):
> **no deja sintoma.**

---

## 7. LOS DISCUTIBLES MARCADOS, para la relectura ciega

**Marcados ANTES de saber si acierto.** Son **doce**.

| # | el discutible | por que lo marco |
|---:|---|---|
| **D1** | **La lectura de *entre ese nodo y la puerta*.** La decision del fundador y el encargo dicen esas palabras; yo escribi la re-declaracion como **cambio de SEDE del lado del punto brillante**, dejando intactos el lado de Blank y la linea *entre libros* | **Es el discutible mayor de la vuelta.** La lectura literal pondria la frontera entre `puntos_brillantes_antes_del_pivote` (Traction) y `pivotar_o_perseverar` (Ries), y eso **contradice la linea sellada del 12 ago** *Entre libros: Ries mas Traction contra Blank*, ademas de dejar sin lado a `pivote_estrategico`. Elegi la lectura que **no contradice ninguna linea sellada** y que **cubre igual el fondo** de la frase (el bloque no se mete dentro de la puerta; la puerta lo sostiene tras la redireccion). **Si el auditor lee que la frontera debia quedar literalmente entre esos dos nodos, la correccion es esa tabla y esta escrita para poder cambiarla** |
| **D2** | **Tache tambien la celda de la fila 75** (la sede vieja en la tabla de los dos lados), que el encargo **no** nombraba entre los cuatro textos | Dejarla sin tachar habria dejado la pagina diciendo **dos sedes distintas** para el mismo lado. Lo meti en la **1.2** (la re-declaracion), no en la 1.1, y lo digo |
| **D3** | El registro de `OP-D-07` dice **`SELLADA`** y **no** estrena `HECHA` | El encargo dice *sella por la via de `OP-D-05` SELLADA*, y esa via usa esa palabra. **No estrenar `HECHA` es lo que tres actas han adjudicado**, pero la palabra exacta del registro es eleccion mia |
| **D4** | Corregi la tabla del cierre de la fase 02 de **8 de 9 a 9 de 9 en la misma vuelta** que escribio el registro que faltaba | La 1.4 manda recomputar lo que se mueva. Podria leerse como que me doy el punto a mi mismo; por eso **la cifra vieja se queda delante** y **el recomputo lo firma el instrumento de la vuelta 46, no uno mio** |
| **D5** | **No escribi la frase de la vuelta 30 dentro del sello, a proposito**, y explique el motivo **dentro de la propia seccion del plan** | Es meter una nota sobre el instrumento en una pagina de plan. Lo hice porque **el siguiente que escriba un sello pisara la misma piedra** |
| **D6** | En la TAREA 2 barri **tres tablas derivadas que el encargo no nombraba**: la linea 9, la celda de HECHO de la fase 2 y la tabla de cierre de la sesion B | El encargo dice *el marcador*. La regla 1 dice *el barrido de toda tabla derivada en el mismo acto*. **Elegi la regla**, y puede leerse como alcance tomado |
| **D7** | Marque **A VERIFICAR** las dos filas de lecturas dirigidas en vez de republicarlas | Deja la tabla con dos huecos declarados. La alternativa era **copiar una cifra sin medirla**, que es exactamente la regla 2 |
| **D8** | **Adjudique el criterio de orden de la fase 03** leyendo CONGELADOS LIBERADOS **en su forma general** (`PENDIENTES.md` linea 2596) y aplicandola sobre `depende_de` | Es lo mas cerca de doctrina nueva que hay en la vuelta. **Lo defiendo asi**: la cita general existe, es del fundador, es del 14 ago, y **no invento el dato que la aplica** (`depende_de` es texto sellado del plan). Aun asi, **el auditor podria leer que esto es una vara nueva y que tocaba PARAR por la 3.3** |
| **D9** | **Restaure la nomina sellada** que `recomputo_3388.py` piso, y saque la de hoy a `docs/loop/` | Restaurar es tocar un fichero que no era mio tocar. Lo hice porque **la alternativa era publicar la vuelta con un artefacto sellado sobrescrito sin encargo** |
| **D10** | **Declare TRES cifras de `OP-U-01` sin elegir ninguna**, y explique solo una de las dos diferencias | Un lector rapido lo leera como *no cuadra y no lo arreglo*. **Es deliberado**: la regla 2 manda declarar |
| **D11** | **Abri `OP-U-01` sin fundir ni un acto**, y lo escribi asi en el plan | El encargo dice *abre la primera operacion y sigue en MODO CONTINUO*. **Cumplo la apertura y no la cirugia**, y digo por que con la cifra delante (270 actos, ninguno con superviviente escrito). **Si el auditor lee que abrir obligaba a fundir el primer tramo, esto es una caida de alcance y la marco yo** |
| **D12** | Corregi **el guarda de guiones de mi propio instrumento** despues de que el hook lo dejara pasar | El hook lo permitio, asi que podria haberlo dejado. La regla 10 dice *todo lo que escribas* |

---

## 8. PENDIENTES DE DOCTRINA

1. **EL ESQUEMA DE `OPERACIONES.jsonl` NO DISTINGUE UNA OPERACION EJECUTADA DE UNA
   PENDIENTE.** Heredado desde la vuelta 30 y **sin cambio hoy**: las **71** estan en
   `LISTA`, medido. Hoy eso solo se lee en el campo `nota` y en la pagina de la fase.
2. **EL CAMPO `orden` DE LA FASE 03 NO ES SU CRITERIO DE ORDEN**, igual que en la fase
   02, y **sigue sin renumerarse**. El artefacto queda **declarado** en la pagina de la
   fase, no tapado.
3. **`MIN_BLOQUE = 2` de la cola de costuras** sigue pendiente del fundador, tal como el
   propio instrumento lo imprime. **Sin cambio en esta vuelta.**

---

## 9. LAS PREGUNTAS, que es lo que no adivino

1. **LA DISCREPANCIA DE `OP-U-01`: 335 contra 332.** El fichero sellado
   `RECOMPUTO_3388_COMPONENTES.jsonl` trae **332** actos y **278** cerrados; la `nota` y
   la `evidencia` de `OP-U-01` y `OP-U-02` publican **335** y **280 sobre 600**. **Las
   dos son anteriores a esta vuelta y no se cual envejecio.** Verificado que **el
   fichero no lo toco yo**. **Quien corrige a quien es adjudicacion, no medicion.**
2. **LA LECTURA DE *Y LA PUERTA*** (el discutible D1). **Si el fundador quiso decir
   literalmente que los dos lados de la frontera pasan a ser el nodo propio y la puerta,
   mi re-declaracion esta mal y hay que rehacerla**, y ademas habria que decidir que
   pasa con la linea *entre libros* y con el lado de `pivote_estrategico`, que hoy nadie
   ha mandado mover.
3. **`OP-U-01` SON 270 LECTURAS DE CONTENIDO. ¿DE QUE TAMANO ES UN TRAMO?** La regla 6
   dice *~50 a 100 pares, o por operacion en ejecucion*, y aqui la unidad no es el par
   ni la operacion, **es el acto**. **No lo adivino: lo pregunto.**
4. **¿SE CAMBIA `recomputo_3388.py` PARA QUE EXIJA `--salida`?** Es codigo de
   `scripts/plan/`, no del bucle, y **tocarlo no me lo encargo nadie.**

---

## 10. LO QUE ESTA VUELTA NO HIZO, dicho en vez de callado

- **NO fundio ni un acto.** `OP-U-01` queda **abierta**, no ejecutada.
- **NO toco un solo nodo.** `dataset/` en **cero** ficheros, comprobado con
  `git status` al cierre.
- **NO renumero el campo `orden`** de ninguna operacion.
- **NO resolvio la discrepancia 335 contra 332**: la declaro.
- **NO republico las dos cifras de lecturas dirigidas**: las marco a verificar.
