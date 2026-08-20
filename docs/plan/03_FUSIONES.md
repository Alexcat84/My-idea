# FASE 03: LAS FUSIONES

**Aqui se ejecuta lo que el cribado adjudico par a par.** Una A dice *estos dos
repiten*; **una fusion decide cual sobrevive y que se rescata del que muere.**

**Operaciones: `OP-U-01` LISTA y `OP-U-02` pendiente del cierre del cribado.**

> **ADJUDICADO el 11 ago 2026: se escriben HOY las fusiones de los actos QUE YA NO
> PUEDEN CRECER.** El resto queda con su fecha de corte y **una sola
> recomputacion** al cerrar el cribado.

---

## LA CIFRA, con su corte y su caducidad

**MEDIDA EL 11 ago 2026, VIGENTE AL PUESTO 2117. MARCADA PARA RECOMPUTO AL
CIERRE DEL CRIBADO.**

| | |
|---|---:|
| **A vigentes** | **400** |
| **ACTOS DE FUSION** (componentes conexas) | **221** |
| **nodos implicados** | **576** |

**POR TAMANO:**

| tamano | actos |
|---:|---:|
| 2 | **154** |
| 3 | 39 |
| 4 | 12 |
| 5 | 7 |
| 6 | 4 |
| 7 | 2 |
| 8 | 1 |
| 9 | 1 |
| **13** | **1** |

> **Un acto no es un par: es una COMPONENTE** (banco 9.24). Si A repite con B y B
> con C, **los tres se deciden juntos o no se deciden.**

---

## LOS SEIS MAYORES, y cuatro de ellos NO se resuelven aqui

| tamano | el acto | donde se resuelve |
|---:|---|---|
| **13** | puertas y portafolio | **`OP-M-01`**: trece nodos no se funden mirando pares. **Es una MESA** |
| **9** | customer discovery | **`OP-M-05`** |
| **8** | build, measure, learn | aqui |
| **7** | customer validation | **`OP-M-05`** |
| **7** | el brainstorming | **`OP-D-04`**, porque va con destejido y decision de fuente |
| **6** | cuatro empatados: la hoja de ruta de ventas, los cuadrantes de mercado, el cierre en venta grande, y las pruebas A/B | las pruebas A/B en **`OP-D-03`**; los otros tres aqui |

> **La regla que esto deja escrita: cuando un acto es grande, casi nunca es una
> fusion limpia.** Los actos de 13, 9 y 7 **llegaron a ser grandes porque el
> catalogo trato el mismo programa de varias maneras**, y eso es una decision de
> forma, no una de pares.

---

## EL ORDEN DE ESTA FASE, y el criterio que lo fija . **adjudicado el 19 ago 2026 (vuelta 47)**

**Lo pidio el fundador** en su decision del 19 ago 2026 (*el orden de la fase 03 lo
adjudica el auditor al reanudar por el precedente de CONGELADOS LIBERADOS; **si no hay
criterio citable, parada***). **Aqui esta el criterio, citado, y la medicion que lo
aplica**, corrida con `python scripts/loop/vuelta47_orden_fase03.py`
([`../loop/SALIDA_V47_ORDEN_FASE03.txt`](../loop/SALIDA_V47_ORDEN_FASE03.txt), exit 0,
instrumento de solo lectura).

### 1. EL EMPATE ES REAL, y esta contado

**El campo `orden` deja TRES operaciones empatadas en el puesto 1**: `OP-M-02-PROG`,
`OP-M-03-I` y `OP-U-01`. **El campo no basta**, igual que no basto en la fase 02.

### 2. LA VARA DE LA FASE 02, APLICADA LITERAL, NO ROMPE EL EMPATE. Y se dice

> **`02_DESTEJIDOS.md` linea 81: *El criterio es CONGELADOS LIBERADOS. No es tamano, no
> es coste.*** Adjudicado para aquella fase por el **acta de la vuelta 44** (seccion 4
> punto 1: *EL ORDEN DE LA FASE 02 NO ES EL CAMPO `orden`: ES CONGELADOS LIBERADOS*).

**Medido hoy sobre el archivo entero: queda UN solo congelado abierto, el puesto
1190** (`formalize_advisory_board` contra `identificar_consejo_asesores`), **y no lo
libera ninguna operacion de esta fase**: lo nombra `OP-M-04`, que es de **06 MESAS**, y
esta pagina ya tenia escrito desde el 11 ago 2026 que **se libera sin cirugia**.

| operacion empatada | congelados que libera |
|---|---:|
| `OP-M-02-PROG` | **0** |
| `OP-M-03-I` | **0** |
| `OP-U-01` | **0** |

**Cero, cero y cero. La vara literal empata a las tres**, y eso no es un fallo de la
vara: **es que en la fase 03 no quedan congelados que liberar.**

### 3. LA MISMA VARA EN SU FORMA GENERAL, QUE ES LA QUE ROMPE EL EMPATE

> **`docs/PENDIENTES.md`, seccion ORDEN DE LA PASADA, adjudicado el 14 ago 2026: *El
> criterio de orden no es el tamano del nodo ni lo averiado que este: es CUANTOS PARES
> DESBLOQUEA su destejido.***

**CONGELADOS LIBERADOS es esa regla leida sobre lo que una cirugia desbloquea.** En una
fase sin congelados, **lo que una operacion desbloquea sigue estando escrito, y lo
escribe el propio plan en el campo `depende_de`**: no es una lectura mia, es texto
sellado. **Aplicada a las tres empatadas:**

| operacion empatada | **desbloquea** | a quien |
|---|---:|---|
| **`OP-U-01`** | **2** | `OP-U-02` y `OP-S-12` |
| `OP-M-03-I` | 1 | `OP-M-03-ENLACES` |
| `OP-M-02-PROG` | **0** | a nadie |

> **EL EMPATE SE ROMPE, Y NO POR PREFERENCIA: `OP-U-01` VA PRIMERA.**

### 4. Y UN SEGUNDO CRITERIO CITABLE, DE ESTA MISMA PAGINA, QUE APUNTA A LO MISMO

**No hace falta para decidir, y por eso va detras y no delante**; pero converge, y una
adjudicacion con dos citas independientes es mas facil de auditar que una con una:

| donde | que dice | a quien senala |
|---|---|---|
| esta pagina, **cabecera**, adjudicado el **11 ago 2026** | *se escriben HOY las fusiones de los actos **QUE YA NO PUEDEN CRECER**. El resto queda con su fecha de corte y una sola recomputacion al cerrar el cribado* | **es `OP-U-01` literalmente**, y `OP-U-02` es el resto |
| [`00_INDICE.md`](00_INDICE.md), **atadura 2** | *`OP-S-12` va **AL FINAL**, despues de la **ultima fusion*** | `OP-S-12` **espera a `OP-U-01`**, que es una de las dos que desbloquea |

### 5. LAS TRES ESTAN DESBLOQUEADAS, comprobado dependencia por dependencia

**No se adjudica un orden sin comprobar que la primera se puede correr.** Las 13
dependencias de `OP-U-01` viven en fases con **cierre declarado y citable**: 4 en
**00 CODIGO** (acta de la vuelta 21, seccion 4 punto 5: la fase 0 cierra con `OP-C-05`
diferida y declarada), 3 en **01 FUENTES** ([`01_FUENTES.md`](01_FUENTES.md) linea
1139, *LA FASE 01 QUEDA CERRADA*, 14 ago 2026) y 6 en **02 DESTEJIDOS**
([`02_DESTEJIDOS.md`](02_DESTEJIDOS.md), el cierre declarado midiendo, hoy **9 de 9**
con registro escrito). `OP-M-03-I` y `OP-M-02-PROG` tambien lo estan.

### LO QUE ESTE CRITERIO NO ES

- **NO es el campo `orden`**, igual que en la fase 02. El campo se cita y no decide.
- **NO es el tamano.** `OP-U-01` es con diferencia la mas grande de las tres, y eso
  **no** es lo que la pone primera: la pone primera lo que desbloquea. Si el tamano
  contara, contaria en contra.
- **NO renumera nada.** El campo `orden` de las 16 operaciones se queda como esta, por
  el mismo motivo que `OP-D-08` y `OP-D-09` se quedaron en 8 y 9: **renumerar
  operaciones ya adjudicadas no es algo que esta vuelta tenga autorizado**, y el
  artefacto queda declarado aqui en vez de tapado.

---

## LAS DOS REGLAS DE EJECUCION, y las dos ya estan adjudicadas

> **DIRECCION**: sobrevive **por CONTENIDO**; a contenido empatado, **desempata el
> grafo**.
>
> **PERDIDAS**: **cada perdida al bloque del que proviene**; la que no tenga
> bloque, **al superviviente** (adjudicado el 11 ago 2026).

**Y una tercera que viene del saneo y aplica a todas**: **el que muere queda
DEPRECADO CON ALIAS, nunca borrado.** Es lo que hace que un recorrido viejo siga
contando algo.

---

## LO QUE NO ENTRA AQUI, y por que

| clase | cuantas | donde va |
|---|---:|---|
| **B, dudosas** | **89** | **no entran**: su clase se decide DESPUES de los destejidos, porque un destejido puede cambiarla |
| **C, sanas con figura** | **7** | **no se funden NUNCA**: son **ENLACE MUTUO**, o sea **dos aristas**. Puestos 201, 203, 215, 246, 360, 1077 y 1240 |

> **Fundir una C seria el error caro que el banco 9.22 nombra**: borraria los dos
> procedimientos para dejar un nodo con dos lineas sueltas. **Van a la fase 04, no
> a esta.**

---

## `OP-U-01`: LOS ACTOS CERRADOS . **LISTA**

**EL CRITERIO, y son DOS condiciones a la vez:**

> **1. Todos los pares posibles entre miembros del acto ya estan leidos.**
> **2. Ningun miembro tiene un par PENDIENTE en la cola sin leer.**

**La segunda es la que importa.** Un acto puede tener sus pares internos leidos y
**aun asi crecer**, porque un miembro tiene un par pendiente **con un nodo de
fuera** que podria salir A.

**MEDIDO el 11 ago 2026, corte del puesto 2117, con 1.271 pares aun en cola:**

| | actos | nodos |
|---|---:|---:|
| **CERRADOS: se ejecutan hoy** | **173** | **371** |
| ABIERTOS: esperan al recomputo | 48 | 205 |

**LOS CERRADOS POR TAMANO**: **149 de dos**, **23 de tres** y **uno de cuatro**,
el de SPIN (`framework_spin_selling`, `metodologia_spin_selling`, `modelo_spin`,
`modelo_spin_preguntas`).

**POR QUE ESTAN ABIERTOS LOS 48:**

| motivo | actos |
|---|---:|
| les falta leer un par **INTERNO** | **42** |
| un miembro tiene par **pendiente en la cola** | **6** |
| por las dos cosas | **0** |

> **Y LOS GRANDES ESTAN TODOS ABIERTOS**: los de 13, 9, 8, 7, 6 y 5 estan **los
> veintitres** en la lista de abiertos. **Los cerrados son los pequenos**, y eso
> tiene sentido: **un acto de dos cierra con un solo par leido.**

---

## `OP-U-02`: LOS ACTOS ABIERTOS . **espera al cierre**

**Quedan con su fecha de corte y UNA SOLA recomputacion** al cerrar el cribado
(banco 9.21).

> **EL RECOMPUTO NO ABRE 48 FUSIONES: ABRE 44.** Cuatro de los abiertos **no se
> resuelven aqui nunca**: el de 13 y el de 9 van a mesa (`OP-M-01` y `OP-M-05`), y
> dos de los grandes van a destejido (`OP-D-03` y `OP-D-04`).

**LO UNICO QUE HAY QUE FIJAR**: quien dispara el recomputo y con que instrumento.
**Y por la regla P.1, ese instrumento RESUELVE ANTES DE CONTAR**, o contara los ya
absorbidos como nodos vivos.

---

## EL PRIMER ACTO CON DECISION ESCRITA: **LA JUNTA ASESORA**

**`OP-M-04`, adjudicada el 11 ago 2026, y sale de la lista de actos abiertos.**

> **NO SE FUNDE EN UNO: SE FUNDE EN DOS Y SE ENLAZAN.** Cuatro nodos, cuatro pares
> en A, **y aun asi la decision no es una fusion de cuatro.**

| | |
|---|---|
| **fusion 367** | sobrevive `identificar_consejo_asesores`, **por el paso 6**, la unica linea de los cuatro que entrega el testigo |
| **fusion 328** | sobrevive `formalizar_junta_asesora`, **por DESEMPATE POR CABLEADO**: contenido empatado, y es el unico nodo conectado con el otro lado |
| **el enlace** | la escalera de identificar hacia formalizar. **Medido: el grafo tenia la cuerda de VUELTA, no la de ida** |
| **el congelado 1190** | **se libera sin cirugia**: el superviviente conserva el paso 6, formalizar sigue siendo hijo, la D se confirma |

> **LA LECCION PARA EL RESTO DE LA FASE 03, y es la que mas caro sale si se ignora:**
> **una componente de cuatro nodos en A no obliga a una fusion de cuatro.** Aqui los
> cuatro A formaban **dos parejas separadas por una etapa del proyecto**, y **una
> regla mecanica las habria fundido borrando la secuencia.**

> **EL DETECTOR, en una linea: ANTES DE FUNDIR, MIRAR SI HAY UNA LINEA QUE ENTREGUE
> EL TESTIGO.** Si un nodo dice *esto se hace mas adelante*, **no es gemelo del que
> lo hace mas adelante: es su madre.**

**El detalle entero esta en**
[`EXPEDIENTE_MESA_JUNTA_ASESORA.md`](EXPEDIENTE_MESA_JUNTA_ASESORA.md).

---

## `OP-U-01` ABIERTA: **LA LECTURA DE CERO Y EL LOTE RE-MEDIDO** (19 ago 2026, vuelta 47)

**Es la primera operacion de la fase 03** por el criterio adjudicado arriba en esta
misma vuelta. **Se abre leyendola ENTERA del fichero y RE-MIDIENDO su nomina contra el
grafo de hoy**, con `python scripts/loop/vuelta47_lectura_opu01.py`
([`../loop/SALIDA_V47_OPU01_LECTURA.txt`](../loop/SALIDA_V47_OPU01_LECTURA.txt), exit 0,
instrumento de solo lectura) sobre la nomina que produce el instrumento de la casa,
`python scripts/plan/recomputo_3388.py --salida docs/loop/RECOMPUTO_V47_COMPONENTES.jsonl`
(que resuelve por alias **antes** de contar, `P.1`).

**CERO NODOS TOCADOS AL ABRIRLA.**

### TRES CIFRAS DEL MISMO OBJETO QUE NO CUADRAN, DECLARADAS Y NO RESUELTAS COPIANDO

**La regla 2 de `EJECUTOR.md` manda declarar la discrepancia en vez de taparla eligiendo
una.** Son tres, y **las tres estan escritas en sitios distintos del repo**:

| de donde sale | actos | nodos | CERRADOS | nodos en CERRADOS | ABIERTOS |
|---|---:|---:|---:|---:|---:|
| **lo que publica `OP-U-01`** en su `nota` y su `evidencia` (corte 3.388, vuelta 12) | **335** | **854** | **280** | **600** | **55** |
| **lo que trae hoy el fichero sellado** [`RECOMPUTO_3388_COMPONENTES.jsonl`](RECOMPUTO_3388_COMPONENTES.jsonl), contado linea a linea | **332** | **838** | **278** | **595** | **54** |
| **lo que mido HOY** contra el grafo de hoy, 19 ago 2026 | **324** | **822** | **270** | **579** | **54** |

**LA SEGUNDA DIFERENCIA ESTA EXPLICADA Y MEDIDA; LA PRIMERA NO.**

- **Del fichero sellado a hoy: OCHO actos**, y el motivo esta contado: **ocho nodos que
  la nomina sellada contaba estan HOY DEPRECADOS**, absorbidos por fusiones de las fases
  01 y 02 que corrieron **despues** de sellarse la nomina. Son
  `blueprint_de_experiencia`, `build_metrics_toolset`,
  `customer_retention_metrics_webmobile`, `escenarios_futuros`,
  `partners_hypothesis_physical`, `plan_acquire_activate`, `propuesta_gasto_capital` y
  `superioridad_producto_beneficios`. **Ocho nodos, ocho actos menos, y las cuentas de
  CERRADOS bajan en ocho: cuadra al digito.**
- **De lo que la operacion PUBLICA al fichero sellado: TRES actos y DOS cerrados de
  diferencia, y esa NO la explico.** El fichero sellado **no se ha tocado en esta
  vuelta** (se restauro intacto tras una corrida que lo iba a pisar por defecto, y se
  declara mas abajo). **La diferencia es anterior a hoy y va como pregunta al auditor**,
  no se arregla aqui: reescribir una de las dos sin saber cual envejecio seria
  exactamente lo que la regla 2 prohibe.

### EL LOTE REAL DE `OP-U-01`, HOY

| | |
|---|---:|
| **actos CERRADOS a fundir** | **270** |
| nodos implicados | **579** |
| **nodos que MORIRIAN** si se funden los 270 (tamano menos 1 por acto) | **309** |
| por tamano | **235** de dos, **31** de tres, **4** de cuatro |

**LA GUARDA DE LOS CUATRO AJENOS, EN VERDE.** Esta pagina declara desde el 11 ago 2026
que cuatro actos **no se resuelven aqui nunca**. Medido hoy: `ab_testing_optimizacion`
y `brainstorming_divergente` **ya no aparecen en ninguna componente** (sus operaciones
corrieron y los deprecaron), y `gates_go_kill_decision_points` (13) y
`customer_discovery` (9) aparecen **ABIERTOS**, no cerrados. **Ninguno de los cuatro
entra en el lote.**

### POR QUE ESTA OPERACION SE EJECUTA POR TRAMOS, Y NO EN UNA SENTADA

**El campo `superviviente` de `OP-U-01` es `null` y su campo `nodos` es lista vacia: la
operacion NO trae escrito quien sobrevive en ninguno de los 270 actos.** Lo que si trae
escrito el plan es **la REGLA para elegirlo**, y son las dos de esta pagina (*sobrevive
por CONTENIDO; a contenido empatado, desempata el grafo*) mas `P.8`, **acto por acto y
con la lectura escrita entera**, tal como `OP-D-04` y `OP-D-05` la aplicaron en la fase
02.

> **Eso NO la convierte en PARADA**, y se dice por que para que nadie lo lea al reves:
> **una operacion es PARADA cuando su texto no alcanza para ejecutarse SIN DECIDIR, y
> aqui la decision de cada acto tiene su regla escrita y citable.** Lo que si obliga es
> a **270 lecturas de contenido**, que es trabajo de varias vueltas y **no cabe en la
> que la abre**. Se ejecuta con la forma asentada de la campana: **lectura de cero y
> lote sellado primero, la cirugia por tramos despues, con Gate 0 y las suites en verde
> tras cada tramo.**

**ESTA VUELTA ENTREGA EL PRIMERO DE ESOS PASOS Y LO DICE ASI EN VEZ DE DECLARARLA
ABIERTA Y HECHA:** `OP-U-01` **queda ABIERTA con su lectura de cero publicada, su lote
re-medido y su guarda de ajenos en verde. CERO fusiones ejecutadas.** El lote de hoy
vive en [`../loop/RECOMPUTO_V47_COMPONENTES.jsonl`](../loop/RECOMPUTO_V47_COMPONENTES.jsonl),
**fuera de `docs/plan/`, para no pisar la nomina sellada.**

> **UNA COSA QUE PASO AL ABRIRLA Y SE DECLARA EN VEZ DE CALLARSE:**
> `scripts/plan/recomputo_3388.py` **escribe `RECOMPUTO_3388_COMPONENTES.jsonl` POR
> DEFECTO**, sin pedirselo, pese a anunciarse como estrictamente de solo lectura. La
> primera corrida de esta vuelta **piso la nomina sellada** (332 lineas a 324). **Se
> restauro con `git checkout` y se comprobo que volvio a sus 332 lineas**, y la corrida
> se repitio con `--salida` apuntando fuera de `docs/plan/`. **El fichero sellado no
> aparece en el `git status` de esta vuelta.** Va como **discutible marcado**, y con una
> recomendacion: **ese instrumento deberia exigir `--salida` en vez de traerla puesta.**
