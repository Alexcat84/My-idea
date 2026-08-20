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
| **B, dudosas** | ~~**89**~~ **72** | **no entran**: su clase se decide DESPUES de los destejidos, porque un destejido puede cambiarla |
| **C, sanas con figura** | ~~**7**~~ **5** | **no se funden NUNCA**: son **ENLACE MUTUO**, o sea **dos aristas**. Puestos 201, ~~203~~, 215, ~~246~~, ~~360~~, **494**, 1077 y 1240 |

> **Fundir una C seria el error caro que el banco 9.22 nombra**: borraria los dos
> procedimientos para dejar un nodo con dos lineas sueltas. **Van a la fase 04, no
> a esta.**

> **CORRECCION DECLARADA (20 ago 2026, vuelta 57, TAREA 1.2, por el carril del banco `9.10`). LA LISTA DE LAS SANAS CON FIGURA ESTABA ENVEJECIDA POR LOS DOS LADOS, y las dos direcciones se dicen porque son especies distintas.**
>
> **SALEN TRES.** El **`203`** lo volteo la vuelta 56 en la relectura del filo del acto 15 del tramo 3 de `OP-U-01`. El **`246`** y el **`360`** dejaron de serlo cuando sus actos se fundieron en las vueltas 52 y 53 y sus dos lados pasaron a resolver al mismo nodo vivo: **nadie los tecleo mal, envejecieron solos**, y por eso ningun barrido que dependa de que alguien NOMBRE el puesto los iba a cazar.
>
> **ENTRA UNO, y este no lo habia notado nadie.** El **`494`** lo es desde el **15 ago 2026**, medido con `git` sobre las versiones del archivo de veredictos: el commit `7cec9ecc` lo volteo desde `A` por el **tercer ejemplar del banco `9.22`**, y esta lista no lo recogio nunca. **Una lista publicada envejece por no soltar y tambien por no tomar.**
>
> **LA CUENTA VIGENTE, RECOMPUTADA HOY del archivo y no heredada de ningun texto: 201, 215, 494, 1077 y 1240, CINCO.** Medido HOY sobre `../INTRA_DOMINIO_VEREDICTOS.jsonl` con `python scripts/loop/vuelta57_puestos_volteados.py --base c0e8041a --tambien 203,246,360` y con `python scripts/recomputar_marcador.py 3388`: [`../loop/SALIDA_V57_PUESTOS_VOLTEADOS_ANTES.txt`](../loop/SALIDA_V57_PUESTOS_VOLTEADOS_ANTES.txt) da estas celdas ROJAS, [`../loop/SALIDA_V57_PUESTOS_VOLTEADOS_DESPUES.txt`](../loop/SALIDA_V57_PUESTOS_VOLTEADOS_DESPUES.txt) las da VERDES, y [`../loop/SALIDA_V57_MARCADOR_APERTURA.txt`](../loop/SALIDA_V57_MARCADOR_APERTURA.txt) es la corrida del marcador de la que salen el 5 y el 72.
>
> **Y LA FILA DE ARRIBA VA EN EL MISMO ACTO, aunque el encargo no la nombraba:** publicaba **89** dudosas, que es la cifra de una medicion vieja; la de hoy es **72**. Corregir una celda y publicar la de al lado sin mirarla es la caida que la regla 1 castiga, asi que se corrige aqui y **se marca como discutible en el reporte de la vuelta**.

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
| ~~**lo que mido HOY** contra el grafo de hoy, 19 ago 2026~~ **AL ABRIR EL TRAMO 1** (vuelta 48) | **324** | **822** | **270** | **579** | **54** |

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
| ~~**actos CERRADOS a fundir**~~ **al ABRIR el tramo 1** | ~~**270**~~ |
| ~~nodos implicados~~ **al ABRIR el tramo 1** | ~~**579**~~ |
| ~~**nodos que MORIRIAN** si se funden los 270 (tamano menos 1 por acto)~~ **al ABRIR el tramo 1** | ~~**309**~~ |
| ~~por tamano~~ **al ABRIR el tramo 1** | ~~**235** de dos, **31** de tres, **4** de cuatro~~ |
| **CORRECCION DECLARADA, barrido 9.10 del 19 ago 2026 (vuelta 48), y las cuatro cifras viejas se quedan delante porque describen el lote QUE ESTA VUELTA ENCONTRO. Recomputado AL CERRAR el tramo 1 con `python scripts/plan/recomputo_3388.py --salida docs/loop/RECOMPUTO_V48_CIERRE.jsonl`. actos CERRADOS a fundir** | **254** |
| **nodos implicados** | **543** |
| **nodos que MORIRIAN si se funden los 254** | **289** |
| **por tamano** | **223** de dos, **27** de tres, **4** de cuatro |

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
re-medido y su guarda de ajenos en verde. ~~CERO fusiones ejecutadas.~~** **CORRECCION DECLARADA, barrido 9.10 del 19 ago 2026 (vuelta 48): la frase era exacta el dia que se escribio y hoy no lo es. El tramo 1 fundio DIECISEIS actos, y su registro esta al final de esta pagina.** El lote de hoy
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

---

## `OP-U-01`, TRAMO 1: **DIECISEIS ACTOS FUNDIDOS Y CINCO DECLARADOS** (19 ago 2026, vuelta 48)

**El tramo son los CINCUENTA primeros actos `CERRADOS` de la nomina re-medida al abrirlo**,
en el orden en que el instrumento los imprime, que es la vara que el auditor adjudico. Se
leyeron los cincuenta (`P.5`, acto leido entero) con
`python scripts/loop/vuelta48_dossier_actos.py`
([`../loop/SALIDA_V48_DOSSIER_1_50.txt`](../loop/SALIDA_V48_DOSSIER_1_50.txt), 369 KB, de solo
lectura), **se fundieron dieciseis y se declararon los demas con su motivo citado.**

### LA CIFRA DEL TRAMO, impresa por el instrumento

| | |
|---|---:|
| actos **leidos** del tramo | **50** |
| actos **FUNDIDOS** | **16** |
| actos **DECLARADOS y no fundidos** | **5** |
| actos **MIXTOS** que quedan a la espera de la lectura de `P.12` | **27** |
| nodos implicados en lo fundido | **36** |
| **nodos DEPRECADOS CON ALIAS** | **20** |
| piezas repartidas (pasos y condiciones de los que mueren) | **123**: **39** viajan enteras al superviviente y **84** ya las decia |

**Y las cifras del censo, del propio instrumento** (`vuelta48_fundir_tramo.py --ejecutar`,
[`../loop/SALIDA_V48_EJECUCION_TRAMO1.txt`](../loop/SALIDA_V48_EJECUCION_TRAMO1.txt), exit 0):

> `censo ANTES  : 3853 ficheros, 3524 vivos, 329 deprecados`
>
> `censo DESPUES: 3853 ficheros, 3504 vivos, 349 deprecados`
>
> `delta deprecados: +20 (esperado +20): OK`

### LO QUE QUEDA DEL LOTE, medido antes y despues

| | al **ABRIR** el tramo | al **CERRAR** el tramo |
|---|---:|---:|
| actos (componentes) | **324** | **308** |
| nodos dentro de actos | **822** | **786** |
| **`CERRADOS`, que es el lote de esta operacion** | **270** | **254** |
| nodos en `CERRADOS` | **579** | **543** |
| `ABIERTOS` | **54** | **54** |
| nodos en `ABIERTOS` | **243** | **243** |

**Los `ABIERTOS` no se mueven ni un digito**, que es exactamente lo que cabe esperar de una
operacion que solo toca `CERRADOS`. **Y los `CERRADOS` bajan en 16, uno por acto fundido.**
Las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) salen **TODAS OK** en
la corrida de cierre ([`../loop/SALIDA_V48_RECOMPUTO_CIERRE.txt`](../loop/SALIDA_V48_RECOMPUTO_CIERRE.txt)).

### LOS DIECISEIS ACTOS, uno por uno, con su superviviente y su motivo

| # | sobrevive | absorbe | por que sobrevive, en una linea |
|---:|---|---|---|
| **9** | `determinar_tipo_de_mercado` | `hipotesis_tipo_mercado`, `tipo_de_mercado_estrategia_competitiva` | CONTENIDO |
| **15** | `diferencia_ganancia_flujo_caja` | `cash_is_king`, `profit_vs_cash` | CONTENIDO |
| **23** | `critica_eco_eficiencia` | `eco_eficiencia_critica`, `limites_de_la_eco_eficiencia` | CONTENIDO |
| **30** | `punto_equilibrio_calidad_inspeccion` | `economia_de_la_inspeccion`, `regla_todo_o_nada_inspeccion` | CONTENIDO, y lo escribe el archivo: los veredictos 2473 y 2467 dicen los dos, con esas palabras, Sobrevive punto_equilibrio_calidad_inspeccion, y el 2480 lo llama GANADOR LIMPIO porque se llevo los dos pares directos |
| **37** | `gestion_sindicato_inversores` | `manejo_syndicate_inversion` | CONTENIDO |
| **38** | `asignacion_agil_de_recursos` | `presupuesto_agil_innovacion` | CONTENIDO, y por margen corto que se declara: mismo numero de pasos (cuatro y cuatro) y el cableado empatado a 3, asi que por P |
| **39** | `estrategia_plataformas_existentes` | `existing_platforms_leverage` | CONTENIDO |
| **41** | `targeting_blogs_traccion` | `targeting_blogs_channel` | CONTENIDO EMPATADO Y EL VEREDICTO LO DICE: el puesto 176 escribe que los cinco pasos son los mismos reordenados |
| **43** | `comunicacion_transparente_en_crisis` | `liderazgo_frente_crisis_competitiva` | CONTENIDO EMPATADO Y EL VEREDICTO LO DICE: el puesto 182 escribe que los cuatro pasos coinciden |
| **44** | `fase_activate_primera_impresion` | `fase_activate` | CONTENIDO |
| **45** | `proceso_decision_vc` | `proceso_diligencia_vc` | CONTENIDO, y contra el cableado, que es exactamente lo que P |
| **46** | `business_model_environment_mapping` | `analisis_entorno_modelo_negocio` | CONTENIDO CASI EMPATADO Y EL CABLEADO DESEMPATA (P |
| **47** | `three_rs_equilibrium` | `sistema_tres_rs_alineacion` | CONTENIDO |
| **48** | `framework_excelencia_operacional` | `preguntas_excelencia_operacional` | CONTENIDO, y por el margen mas ancho del tramo: diez pasos contra cuatro |
| **49** | `storytelling_como_herramienta_de_diseno` | `storytelling_para_el_cambio` | CONTENIDO |
| **50** | `compromiso_linea_tiempo_cliente` | `tacticas_cierre_ventas` | CONTENIDO |

**El plan sellado, con la marca de CADA paso y CADA condicion de CADA nodo que muere, vive en**
[`../loop/PLAN_V48_OPU01_TRAMO1.json`](../loop/PLAN_V48_OPU01_TRAMO1.json). **No trae texto: trae
INDICES**, y el instrumento lee cada pieza verbatim del fichero del nodo. La guarda de cobertura
comprueba que **cada indice aparezca exactamente una vez y que no sobre ninguno**: una perdida sin
destino no es una perdida, es un olvido.

### CORRECCION DECLARADA SOBRE EL ACTO 49: **LA PIEZA QUE NO VIAJABA, ADOSADA** (19 ago 2026, vuelta 49)

> **El texto viejo NO se borra, y va delante:** el plan sellado del tramo
> ([`../loop/PLAN_V48_OPU01_TRAMO1.json`](../loop/PLAN_V48_OPU01_TRAMO1.json), acto 49) marco el
> **paso 3** de `storytelling_para_el_cambio` como **`CUBIERTO:3`**, y su campo
> `perdidas_declaradas` lo decia asi: *"NO se anade como paso propio: el veredicto 212 agrupa ese
> paso con las demostraciones tangibles, que sobreviven enteras en el paso 3 del superviviente. Lo
> que NO sobrevive es el matiz de QUIEN demuestra."* **El reporte de la vuelta 48 lo marco el mismo
> como discutible `D9`.**

**Y NO ERA VERDAD COMPLETA.** El auditor lo verifico y lo adjudico
([`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), acta de la vuelta 48, seccion 4, leida hoy):
el paso 3 del superviviente **dice las demostraciones y NO dice QUIEN modela**. Los dos textos,
leidos hoy del fichero del nodo:

| | el paso 3, verbatim |
|---|---|
| superviviente, **antes** | `Crear momentos memorables (eventos, demostraciones) en lugar de solo publicidad` |
| absorbido (`storytelling_para_el_cambio`, **texto INTACTO**) | `Usar demostraciones tangibles y figuras de autoridad para modelar el nuevo comportamiento` |

**LA FIGURA APLICADA ES EL `INCISO ADOSADO`**, que es el remedio escrito de `SALVAGUARDA` en la
**TABLA DE LOS SEIS MOTIVOS DE PERDIDA DE LINEA** (*el inciso se adosa al paso que protege*), con
el precedente vivo de `OP-D-02` paso 1 en [`02_DESTEJIDOS.md`](02_DESTEJIDOS.md) **linea 220**,
leida hoy. **No es `APPEND`**: anadir el paso entero duplicaria *usar demostraciones tangibles*,
que es exactamente lo que el superviviente ya manda. **Y no es `CUBIERTO`**, que es lo que estaba
mal escrito.

| | el paso 3 del superviviente, **HOY** |
|---|---|
| **resultado** | `Crear momentos memorables (eventos, demostraciones) en lugar de solo publicidad, con figuras de autoridad para modelar el nuevo comportamiento` |

**El instrumento es `scripts/loop/vuelta49_inciso_adosado.py`** con el plan sellado
[`../loop/PLAN_V49_INCISO_ACTO49.json`](../loop/PLAN_V49_INCISO_ACTO49.json)
([`../loop/SALIDA_V49_INCISO_SIM.txt`](../loop/SALIDA_V49_INCISO_SIM.txt) y
[`../loop/SALIDA_V49_INCISO_EJEC.txt`](../loop/SALIDA_V49_INCISO_EJEC.txt), los dos exit 0).
**El plan no redacta el inciso: lo nombra como TROZO VERBATIM** del paso del que muere, y la
guarda 2 comprueba que ese trozo esta literal dentro de ese paso. **Lo unico que el instrumento
aporta de su cosecha es el NEXO**, `", con "`, **y va impreso aparte para que se pueda discutir
por separado del contenido.**

| guarda | resultado |
|---|---|
| **0**, los dos nodos en el estado que el plan dice (vivo, deprecado, y el alias los une) | **OK** |
| **1**, `P.5` sobre el texto: el paso es HOY byte a byte el que el plan leyo | **OK** |
| **2**, el inciso es trozo **VERBATIM** del paso 3 del absorbido | **OK** |
| **3**, idempotencia: correr dos veces no apila | **OK** (la 1.ª corrida `--ejecutar` se revirtio con `git checkout` para tomar la base de la guarda de defectos, y la 2.ª volvio a escribir el mismo byte) |
| **4**, **SOLO** cambia `pasos_accionables`; ni titulo, ni fuente, ni resumen, ni entregable, ni una arista | **OK** |
| **duplicadas tras resolver y auto-aristas NUEVAS**, re-corridas sobre el resultado | **CERO y CERO**: **1.004** y **0** en la base y **1.004** y **0** despues ([`../loop/SALIDA_V49_DEFECTOS_INCISO.txt`](../loop/SALIDA_V49_DEFECTOS_INCISO.txt), exit 0) |

**El nodo absorbido no se toca: su texto sigue INTACTO**, que es lo que hace que un recorrido viejo
siga contando algo.

### LOS CINCO DECLARADOS Y NO FUNDIDOS, con su motivo citado

| # | el acto | por que NO se funde |
|---:|---|---|
| **36** | `domina_lo_que_compras`, `investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor` | LA PUERTA DE UN MUNDO NO SE ABSORBE. El absorbido que este plan traia, investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor, es SEMILLA DE ENTRADA del mundo compras y ademas DESTINO DE UN PUENTE APROBADO. La primera corrida --ejecutar de esta vuelta lo depreco y GATE 0 SALIO EN ROJO por dos chequeos a la vez (Ninguna semilla de entrada esta deprecada, y Ningun puente aprobado apunta a un nodo deprecado). El dataset se restauro con git checkout, el acto sale del lote, y la guarda que faltaba (1B) queda escrita en el instrumento para que ningun tramo futuro pueda deprecar una puerta en silencio. La lectura y el superviviente del acto siguen siendo validos y quedan escritos aqui para cuando alguien decida que hacer con la semilla: sobrevive domina_lo_que_compras. |
| **22** | `diversidad_como_fortaleza_ecosistemica`, `respetar_la_diversidad`, `respeto_a_la_diversidad` | CONTENIDO EMPATADO Y EL CABLEADO TAMBIEN. Los tres veredictos (1857, 1792, 1779) dicen lo mismo de los tres pares: TRES de los cuatro pasos se corresponden y a cada nodo le queda EXACTAMENTE UNA linea propia. Cuatro pasos y dos condiciones cada uno. El cableado empata a 3 entre diversidad_como_fortaleza_ecosistemica y respeto_a_la_diversidad. P.8, fila tres de su tabla: empatado el contenido y empatado el cableado, SE TRAE AL AUDITOR. No se fuerza. |
| **29** | `mejora_del_sistema_responsabilidad_gerencial`, `sistema_estable_causas_comunes`, `sistema_estable_responsabilidad_gerencial` | EL PROPIO VEREDICTO MARCA AL GANADOR COMO PROVISIONAL. El puesto 2572 escribe una NOTA GRAVE DE FAMILIA: mejora_del_sistema queda arriba y sin perder, ganador PROVISIONAL, pero el cumulo pasa de diez nodos por raiz y no esta leido entero, y sistema_estable_causas_comunes gano el 2453 y perdio el 2537, que es la firma de POR ELEGIR. Fundir sobre un ganador que el archivo llama provisional es decidir lo que el archivo dejo sin decidir. Se declara. |
| **32** | `dia_cero_defectos`, `dia_cero_defectos_2`, `dia_cero_defectos_3` | EL VEREDICTO 2525 DEJA UN AVISO EXPRESO PARA ESTA OPERACION: los dos dan CADENAS DE FIRMA DISTINTAS, firmar contigo uno a uno contra firmar con su supervisor, y dice con esas palabras que la fusion TIENE QUE DECIDIRLO, NO APILARLO. Decidirlo es quedarse con una y borrar la otra, y borrar contenido que ninguna regla ordena esta reservado al fundador (AUDITOR.md seccion 4). Apilarlas dejaria el nodo mandando dos cosas incompatibles. Se declara y no se funde. |
| **42** | `storyboard`, `storyboard_prototipado` | CONTENIDO EMPATADO Y EL CABLEADO TAMBIEN. El veredicto 179 lee los dos como la misma cosa en tres gestos. Cuatro pasos cada uno, y el cableado empata a 4. P.8, fila tres: SE TRAE AL AUDITOR. |

### LOS VEINTISIETE MIXTOS, y por que esta vuelta NO los funde

**De los 270 actos `CERRADOS` del lote, VEINTISIETE tienen dentro un par que NO es `A`** (4 de
tamano cuatro y 23 de tamano tres), **y los veintisiete caen dentro de estos primeros 50**: el
orden impreso pone los duros por delante. Medido en
[`../loop/SALIDA_V48_COLISION_1_50.txt`](../loop/SALIDA_V48_COLISION_1_50.txt).

> **`P.12` prohibe fundirlos por transitividad**: *el cierre transitivo CONVOCA, la lectura
> DECIDE*, y *NI TRANSITIVIDAD AUTOMATICA NI MAYORIA*. El nodo mixto **se lee CONTRA EL
> SUPERVIVIENTE** y se decide `ENTRA` (comparte procedimiento) o `CONTINUA` (comparte la idea
> en lineas: enlace mas poda del solape).

**Esa lectura se hizo ENTERA para UNO, el acto 1**, y se deja escrita como ejemplar: el mixto es
`metodologia_spin_selling`, cuyos dos veredictos `D` (puestos **625** y **764**) dicen los dos, con
esa palabra, **CONTINUA**, porque su paso 3 es *una linea que ademas remite fuera* mientras los
otros traen *el PROCEDIMIENTO entero*. **`CONTINUA` no es fusion: es enlace**, y el enlace es de la
fase 04. **Los otros veintiseis NO se leyeron en esta vuelta, y se dice en vez de callarse.**

### LA GUARDA QUE FALTABA, y el `GATE 0` en rojo que la trajo

> **Se cuenta con nombre porque un fallo que no deja sintoma es la especie del canon 9.**

**La primera corrida `--ejecutar` de este tramo llevaba el acto 36**, que absorbia
`investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor`. Ese nodo es **SEMILLA DE ENTRADA**
del mundo `compras` **y ademas DESTINO DE UN PUENTE APROBADO**, asi que `run_phase1.py` dio
**`GATE 0: FALLIDO`** por **dos** chequeos a la vez. **El dataset se restauro entero con
`git checkout` y el acto salio del lote.**

**Y la pregunta no era del acto 36: era de la operacion entera.** Medido con
`python scripts/loop/vuelta48_puertas_en_el_lote.py`
([`../loop/SALIDA_V48_PUERTAS_EN_EL_LOTE.txt`](../loop/SALIDA_V48_PUERTAS_EN_EL_LOTE.txt), exit 0):

| | |
|---|---:|
| semillas de entrada (20 del core mas las de los mundos) | **85** |
| nodos que son extremo de un puente aprobado | **185** |
| **el universo PROTEGIDO, la union** | **256** |
| actos `CERRADOS` con **al menos una puerta dentro** | **31** de 270 |
| de esos, **SALVABLES** (una sola puerta: el acto se funde **si la puerta sobrevive**) | **29** |
| de esos, **IMPOSIBLES** (todos sus miembros son puerta: alguien tendria que morir) | **2**, los actos **36** y **174** |

> **LO QUE ESTO DEJA ABIERTO, y va como PREGUNTA y no como decision: en esos 29 actos la eleccion
> de superviviente YA NO ES LIBRE.** La regla de esta pagina dice que **sobrevive por CONTENIDO**;
> si el contenido apunta al que **no** es puerta, **hay choque entre la vara de la fase y el
> `GATE 0`**, y **ninguna regla escrita hoy lo resuelve.**

**La guarda `1B` queda escrita en `scripts/loop/vuelta48_fundir_tramo.py`** y lee las mismas
fuentes que el `GATE 0`: **ningun absorbido puede ser semilla ni extremo de puente**. Con ella el
tramo **aborta antes de escribir** en vez de romper.

### GATE 0 Y SUITES TRAS EL TRAMO

| que | como salio |
|---|---|
| `run_phase1.py --reaplico-curaduria` | **`GATE 0: OK`**, exit 0 |
| `etiquetas_de_cara.py --aplicar` | **71** etiquetas, exit 0 |
| `sync_assets_web.py` | **6** assets, exit 0 |
| suite del motor | **25 de 25**, exit 0 |
| suite web | **80** ficheros, **1.030** pasadas y **3** saltadas, exit 0 |
| `tsc --noEmit` | **CERO** lineas, exit 0 |
| marcador del archivo | **575 / 79 / 8 / 2.726**, `n` **3.388**, cero huecos y cero duplicados: **SIN MOVER** |
| duplicadas tras resolver | **1.010** antes y **1.004** despues: **CERO nuevas**, y el tramo **baja el pasivo historico en 6** por `P.16` |
| auto-aristas | **CERO** nuevas; **3** que la fusion habria creado, retiradas en el acto |

---

## `OP-U-01`, TRAMO 1, CIERRE PARCIAL: **LOS DOS EMPATES ADJUDICADOS, LA PRIMERA LECTURA `P.12` EJECUTADA, Y UNA COLISION QUE FABRICO ESTA MISMA VUELTA** (19 ago 2026, vuelta 49)

**Esta seccion NO cierra el tramo 1: cierra TRES de sus treinta y cuatro actos pendientes.** Lo
que queda sin hacer va escrito abajo con su cifra, en vez de callado.

### LOS DOS EMPATES DE `P.8` FILA TRES, ADJUDICADOS Y EJECUTADOS

**Los dos venian declarados en el registro del tramo de la vuelta 48 con la frase `SE TRAE AL
AUDITOR`.** El auditor los re-midio, verifico el empate en los dos y escribio el caso del
superviviente ([`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), acta de la vuelta 48,
seccion 5). **El ejecutor verifico cada caso CONTRA EL GRAFO antes de fundir**, con los
veredictos reproducidos verbatim en el dossier de hoy
([`../loop/SALIDA_V49_DOSSIER_20.txt`](../loop/SALIDA_V49_DOSSIER_20.txt) y
[`../loop/SALIDA_V49_DOSSIER_34.txt`](../loop/SALIDA_V49_DOSSIER_34.txt)), **y las tres patas de
cada caso calzan.**

| era el acto | hoy | sobrevive | absorbe | las tres patas del caso, VERIFICADAS hoy |
|---:|---:|---|---|---|
| **22** | **20** | `respeto_a_la_diversidad` | `diversidad_como_fortaleza_ecosistemica`, `respetar_la_diversidad` | **(a)** el puesto **1792** lo escribe **DE CENTRO** de la familia con esas palabras; **(b)** el puesto **1779** llama a su *evaluar la resiliencia* **la unica que pone una PRUEBA al diseno en vez de una regla**; **(c)** el nombre es el principio **sin calificar**, contra *Diversidad como Fortaleza (Fitting)*, que es el angulo del encaje, y contra *Respetar la Diversidad (Biologica, Cultural y de Lugar)*, que es el principio con tres calificativos |
| **42** | **34** | `storyboard` | `storyboard_prototipado` | **(a)** el nombre del concepto **sin calificar**, y el propio veredicto **179** dice que el otro es *el base mas un sufijo tematico*; **(b)** su **mecanica de sesion** es lo que hace ejecutable la practica (el time-box de 30 a 45 minutos, no preocuparse por la calidad del dibujo, actuar o presentar al equipo) y **ninguna de las tres esta en el otro**; **(c)** la anatomia del otro **viaja limpia** |

**EL EMPATE, RE-MEDIDO HOY Y NO HEREDADO:** el acto 20 da **cuatro pasos y dos condiciones cada
uno** y **cableado 3 a 3** entre los dos punteros; el acto 34 da **cuatro pasos cada uno**,
**cableado 4 a 4** y **cero aristas internas**. **El empate era real y sigue siendolo**, que es
lo que hace que la eleccion la decidan las tres patas y no el conteo.

**LA VARA DE LAS PUERTAS, APLICADA ANTES DE TOCAR** (adjudicacion del acta 48, seccion 6, punto
1): medida hoy sobre la nomina de hoy
([`../loop/SALIDA_V49_PUERTAS_EN_EL_LOTE.txt`](../loop/SALIDA_V49_PUERTAS_EN_EL_LOTE.txt)),
**ninguno de los cinco miembros de los dos actos es semilla de entrada ni extremo de puente
aprobado**, y ni el 20 ni el 34 estan entre los **30 SALVABLES** ni entre los **2 IMPOSIBLES**.
**La vara no muerde aqui y la guarda `1B` pasa por vacio: se dice en vez de darla por buena.**

### EL TERCER DESTINO QUE LE FALTABA AL INSTRUMENTO DE FUNDIR: `INCISO`

> **Nace de la correccion que el auditor encargo sobre el acto 49, dos secciones mas arriba, y
> no de un capricho.** El instrumento de la vuelta 48 solo sabia **DOS** destinos para una pieza
> del que muere: `APPEND` (viaja entera) y `CUBIERTO:n` (ya lo dice el paso n). **El caso de en
> medio no tenia marca**, y esa carencia es exactamente lo que produjo la pieza mal marcada del
> acto 49.

**`scripts/loop/vuelta49_fundir_tramo.py`**, sucesor declarado del de la vuelta 48, anade la
marca **`INCISO:n|<inciso VERBATIM>|<nexo>`** con sus dos guardas propias: **el inciso tiene que
ser trozo LITERAL** del paso del absorbido, y **si ya esta dentro no se apila**.

**El acto 34 lo estrena, y es LA MISMA FORMA del acto 49.** El paso 4 de `storyboard_prototipado`
(*Compartir el storyboard con usuarios o el equipo para retroalimentacion*) contra el paso 4 del
superviviente (*Actuar o presentar el storyboard al equipo para recibir feedback*): **`APPEND`
entero habria dejado dos pasos mandando lo mismo, y `CUBIERTO` habria perdido la palabra
`usuarios`, que es lo unico que el otro anade.**

| | el paso 4 del superviviente |
|---|---|
| **antes** | `Actuar o presentar el storyboard al equipo para recibir feedback` |
| **HOY** | `Actuar o presentar el storyboard al equipo para recibir feedback, y compartirlo con usuarios o el equipo para retroalimentacion` |

> **SE MARCA COMO DISCUTIBLE, y va tambien al reporte de la vuelta:** el auditor escribio que esa
> pieza *viaja limpia como pieza*, y **el ejecutor la hace viajar como INCISO**. No se pierde ni
> una palabra de lo que el auditor mando viajar, pero **no es literalmente lo que dijo**.

### LA PRIMERA LECTURA `P.12`, REGISTRADA EN TABLA PROPIA (el carril adjudicado)

**El carril lo adjudico el auditor** (acta de la vuelta 48, seccion 6, punto 2): el veredicto de
cada lectura `P.12` se registra **AQUI**, en tabla propia, y **los `CONTINUA` declaran AHI su
arista a la fase 04**, con id **RESUELTO** (`P.9`) y **SIN ejecutarla**, que es la figura de
[`02_DESTEJIDOS.md`](02_DESTEJIDOS.md) **linea 3521**.

| el mixto | leido CONTRA | veredicto | las citas |
|---|---|---|---|
| `metodologia_spin_selling` | `modelo_spin_preguntas` | **`CONTINUA`** | **Los DOS veredictos `D` del acto lo dicen con esa palabra.** El puesto **764**: *el paso 3 de la madre es UNA LINEA QUE ADEMAS REMITE FUERA* (*prepararse para usar las preguntas de Situacion, Problema, Implicacion y Necesidad-Beneficio, que se detallan en capitulos posteriores*) y `modelo_spin_preguntas` *trae el PROCEDIMIENTO entero*; **No cabe en una linea: CONTINUA**. El puesto **625** dice lo mismo con el otro miembro de la parte A: *CONTINUA, no repite* |

**LA ARISTA QUE FALTA, DECLARADA AQUI Y NO EJECUTADA:**

| de | a | sentido | medida hoy | quien la ejecuta | la poda del solape |
|---|---|---|---|---|---|
| `metodologia_spin_selling` | `modelo_spin_preguntas` | de la **madre** al **hijo**: la madre nombra en su paso 3 lo que el hijo desarrolla | **CERO arista en los dos sentidos**, buscada hoy resolviendo por alias | **la fase 04**. Los dos ids van **RESUELTOS** (`P.9`): `modelo_spin_preguntas` es el superviviente de la parte A de este mismo acto | **PENDIENTE de la fase que ejecute el enlace.** Esta operacion **NO la tiene autorizada**. El solape a podar es **el paso 3 de `metodologia_spin_selling`**, que es la linea que remite fuera |

### LA PARTE A DEL ACTO 1, FUNDIDA

| sobrevive | absorbe | por que, y no esta empatado |
|---|---|---|
| `modelo_spin_preguntas` | `framework_spin_selling`, `modelo_spin` | **CONTENIDO, y el cableado no habla porque no hay empate (`P.8`).** SEIS pasos contra CUATRO y CUATRO, TRES condiciones contra UNA y DOS, y el resumen mas largo del acto. **Es el unico que trae las dos piezas que cierran el metodo**: ajustar la secuencia al flujo natural **sin forzar el orden rigido**, y **NO presentar la solucion hasta que el cliente haya articulado la Necesidad Explicita**. **Y lo escribe el veredicto 401**: *el segundo detalla que hace cada tipo de pregunta*. Cableado **15** contra 9 y 7 |

**Pasos 6 a 9, condiciones 3 a 5. Once piezas repartidas: CINCO viajan enteras y SEIS ya las
decia.** Plan sellado en
[`../loop/PLAN_V49_OPU01_ACTO1.json`](../loop/PLAN_V49_OPU01_ACTO1.json).

### **LA COLISION DE CLASE QUE FABRICO ESTA MISMA VUELTA**, y se cuenta con nombre

> **Se dice asi, y no como hallazgo, porque la fabrico mi propia operacion.** Es el canon 9: un
> fallo que no deja sintoma es la especie que hay que contar.

**Al deprecar `modelo_spin` con alias a `modelo_spin_preguntas`, el puesto 305**
(`metodologia_spin_selling` contra `modelo_spin`, clase **`A`**) **paso a RESOLVER sobre el mismo
par que el 764** (clase **`D`**) **y que el 625** (clase **`D`**). **Tres veredictos, un solo par
resuelto, dos clases.**

**`P.16` DEL BANCO DEL PLAN, QUIEN FABRICA LIMPIA**, y el carril es el que el auditor adjudico
para las tres colisiones preexistentes: **relectura conjunta con los textos vivos delante,
correccion declarada, y marcador recomputado.** **El 305 pasa de `A` a `D`**, y la relectura no
necesita doctrina nueva porque **la lectura `P.12` de arriba YA ES esa relectura**: el `305` leyo
`modelo_spin`, un nodo cuyo cuerpo eran **tres gestos de entrenamiento** mas el orden enunciado;
**el nodo vivo de hoy tiene NUEVE pasos** y trae el procedimiento entero. **Contra ese, el paso 3
de `metodologia_spin_selling` sigue siendo una linea.**

### **LA MEDICION QUE ESTO OBLIGA A HACER, Y ES LO MAS GRANDE QUE DEJA ESTA VUELTA**

**No es un caso suelto.** Medido hoy sobre **todos** los mixtos pendientes
([`../loop/SALIDA_V49_MIXTOS_FORMA.txt`](../loop/SALIDA_V49_MIXTOS_FORMA.txt)):

| | |
|---|---:|
| mixtos pendientes con **la forma** (algun miembro carga a la vez un par `A` y un par NO-`A` dentro del acto) | **26** |
| mixtos pendientes **sin** la forma | **1** |

> **QUE SIGNIFICA, dicho con su limite:** la forma **solo fabrica colision cuando el veredicto es
> `CONTINUA`**. Si el mixto `ENTRA`, el acto se funde entero y todos sus pares colapsan a
> auto-par sin chocar. **Asi que la cifra de 26 es el TECHO, no la prediccion**: cuantas
> colisiones nazcan de verdad depende de cuantas lecturas digan `CONTINUA`, y eso no se sabe
> hasta leerlas.
>
> **Y LA BUENA NOTICIA VA CON ELLA:** cuando nace, **la colision se resuelve con la MISMA lectura
> que la produjo**, sin doctrina nueva, porque `CONTINUA` es precisamente el hallazgo de que el
> mixto **no repite** al superviviente. **El `A` viejo se emitio contra un nodo que hoy no existe
> solo.**

### LO QUE ESTA SECCION **NO** HIZO

| | |
|---|---:|
| lecturas `P.12` **hechas y registradas** | **1** (el acto 1, que ya la tenia hecha) |
| lecturas `P.12` **encargadas y NO hechas** | ~~**25**~~ **26** **[CORREGIDA UNA VEZ, el 20 ago 2026 (vuelta 51, TAREA 1.1). NO ES UNA CIFRA QUE ENVEJECIO: NACIO MAL. La cuenta buena al cierre de la vuelta 49 era 26, medida por miembros sobre la nomina de aquel estado (`../loop/SALIDA_V50_TRAMO1_POR_MIEMBROS.txt`, corrida al abrir la vuelta 50 sobre el hash `b8d1083a`, que es el cierre de la 49) y re-derivada por el auditor en el acta de la vuelta 50, seccion 3.3, que es su relectura conjunta: 25 mixtos al cierre de la vuelta 50 mas el acto 1 que esa vuelta resolvio. LA FILA HERMANA del registro de la vuelta 50, que dice 25 al cierre, esta bien medida y NO se toca. El 25 de aqui convivia en esta misma pagina con el 26 de la medicion de la forma, dos parrafos mas arriba]** |
| actos **fundidos** en esta seccion | **3** (los dos empates y la parte A del acto 1) |
| **tramo 2** de 50 actos | **NO ABIERTO**: no hubo cuerda |
| los declarados **29**, **32** y **36** (~~hoy~~ **26**, **28** y **32** AL ABRIR LA VUELTA 49) **[ROTULO FECHADO, 20 ago 2026 (vuelta 52, TAREA 1.3), CIFRAS INTACTAS: el 26/28/32 es exacto para la corrida de la APERTURA de la vuelta 49 y lo que envejecio es la palabra *hoy*. Re-medido esta vuelta con `python scripts/loop/vuelta50_tramo_por_miembros.py` contra las tres nominas selladas: al ABRIR la vuelta 49 son 26, 28 y 32 (`../loop/SALIDA_V52_TRAMO1_EN_APERTURA_V49.txt`, sobre `RECOMPUTO_V48_CIERRE.jsonl`, 254 CERRADOS); al CERRARLA ya eran 24, 26 y 30 (`../loop/SALIDA_V52_TRAMO1_EN_CIERRE_V49.txt`, sobre `RECOMPUTO_V49_CIERRE.jsonl`, 252 CERRADOS); y al ABRIR la vuelta 51 eran 23, 25 y 29 (`../loop/SALIDA_V52_TRAMO1_EN_APERTURA_V51.txt`, sobre `RECOMPUTO_V51_APERTURA.jsonl`, 251 CERRADOS). Es la misma especie que la TAREA 1.2 de la vuelta 51 corrigio en el registro de la vuelta 50, y el acta de la vuelta 51 la adjudico en su `D10`. Los tres son numeros del TRAMO (29, 32 y 36), que no bailan; lo que baila es el ordinal de la nomina del dia]** | **siguen declarados**, ninguno se toca |
| los dos actos que la vuelta 48 dejo fuera **por colision de clase medida** (hoy los **8** y **33**) | **siguen fuera**, y esta vuelta no los mira |

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 49 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 575 / 79 / 8 / 2.726 | **573 / 77 / 8 / 2.730** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.504 / 349 / 16.962 | **3.853 / 3.499 / 354 / 16.984** |
| actos `CERRADOS` / `ABIERTOS` | 254 / 54 | **252 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 543 / 243 | **536 / 240** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |

---

## `OP-U-01`, TRAMO 1, LA VUELTA 50: **EL BARRIDO QUE LA VUELTA 49 NO CORRIO AL CERRAR, Y UN ALIAS QUE NO SE IZO** (19 ago 2026, vuelta 50)

### LO PRIMERO DE LA VUELTA, PORQUE ES UNA CAIDA DE CIFRA PUBLICADA Y NO UN TRAMITE

**La vuelta 49 movio el marcador y el retrato DESPUES de correr su barrido `9.10`** (el volteo
del puesto **305** por `P.16` y las tres fusiones de su TAREA 2) **y no volvio a barrer al
cerrar.** El acta de la vuelta 49, seccion 3, lo nombra como caida de cifra publicada del
ejecutor, FUERA de sus discutibles marcados. **Las cinco celdas quedan corregidas hoy con
tachado, fecha y motivo**, y las cifras salen de dos instrumentos corridos EN ESTA VUELTA y de
ningun acta:

| la celda | decia | **al corregirla en la TAREA 1.1** | el instrumento |
|---|---:|---:|---|
| [`../INTRA_DOMINIO_INFORME.md`](../INTRA_DOMINIO_INFORME.md) apendice **100.1**, fila `A` | 574 | **573** | `scripts/recomputar_marcador.py 3388` |
| el mismo apendice, fila `D` | 2.729 | **2.730** | el mismo |
| [`RECOMPUTO_3388.md`](RECOMPUTO_3388.md) fila **246**, `A` crudas | 574 | **573** | `scripts/plan/recomputo_3388.py` |
| la fila **247**, colapsos a auto-arista | 41 | **48** | el mismo |
| la fila **248**, pares distintos del retrato | 533 | **525** | el mismo |
| la fila **1079**, total de `A` de la tabla por dominio | 574 | **573** | `recomputar_marcador.py` |
| el checkpoint **ii** de la fila **528** | 533 igual a 533 | **525 igual a 525, sigue OK** | `recomputo_3388.py`, seccion final |

**Y LA CIFRA 41 NO ERA UN ERROR DE LECTURA, QUE ES LO QUE LA HACE INTERESANTE:** era el corte de
la TAREA 1.3 de la vuelta 49, tomado ANTES de las tres fusiones de su propia TAREA 2. **Los
siete que faltaban son la huella de esas tres fusiones**, que es exactamente lo que la propia
fila ya explicaba de las 41. Una fila puede explicar bien su cifra y traer la cifra vieja.

> **LA REGLA QUE ESTO DEJA, y ya esta adjudicada** (acta de la vuelta 49, seccion 5, pregunta 5,
> por extension del banco `9.10`): **quien mueve una clase o funde un acto corre el barrido ANTES
> DE CERRAR LA VUELTA**, sobre toda tabla vigente que cite la clase, el marcador o el retrato.
> Barrer al destapar y barrer al mover son la misma regla vista de los dos lados.

### EL INSTRUMENTO DEL BARRIDO TENIA LA MISMA AVERIA QUE PERSEGUIA, Y SE DICE

**Medido antes de escribir una linea del sucesor:** `scripts/loop/vuelta49_barrido_910.py` acepta
`--viejo` **pero no lo usa para buscar**. Sus dos expresiones regulares estan clavadas a `583` y
`2709`, las cifras del marcador de la vuelta 14, y `--viejo` solo cambia la cabecera que imprime.
Corrido hoy con `--viejo 574,77,8,2729` devuelve 22 candidatos, **y los devuelve porque esas
celdas arrastran el 583 en su cadena de tachados, no porque sepa buscar el 574**
([`../loop/SALIDA_V50_BARRIDO_910_INSTRUMENTO_VIEJO.txt`](../loop/SALIDA_V50_BARRIDO_910_INSTRUMENTO_VIEJO.txt)).
**Una celda nueva escrita hoy con la cifra vigente y sin cadena de tachados le seria invisible.**
El sucesor `scripts/loop/vuelta50_barrido_910.py` busca de verdad lo que se le pide, conserva la
familia legado del 583 y anade la familia del RETRATO, que ningun barrido anterior miraba: **con
el, las siete celdas de arriba salen solas**
([`../loop/SALIDA_V50_BARRIDO_910_A.txt`](../loop/SALIDA_V50_BARRIDO_910_A.txt)).

### EL ALIAS QUE NO SE IZO AL SUPERVIVIENTE (`modelo_spin_2`)

**Una linea de registro y ningun dato tocado**, que es lo que el encargo manda. Al fundir la
parte A del acto 1 en la vuelta 49, el absorbido `modelo_spin` cargaba a su vez el alias
`modelo_spin_2` y **ese alias NO se izo a `modelo_spin_preguntas`**. Medido hoy con
`scripts/loop/vuelta50_alias_durmiente.py`
([`../loop/SALIDA_V50_ALIAS_DURMIENTE.txt`](../loop/SALIDA_V50_ALIAS_DURMIENTE.txt)), y con un
filo mas que la observacion del acta: **por el resolutor de la casa (`P.1`, que construye el mapa
de alias SOLO con nodos vivos) `modelo_spin_2` NO RESUELVE EN ABSOLUTO**; solo llega por la
cadena ancha `modelo_spin_2` a `modelo_spin` **[DEPRECADO]** a `modelo_spin_preguntas`. **CERO
referencias en aristas y CERO en veredictos**: nadie lo pisa hoy. **Es pasivo de la especie
`OP-S-12` y queda nombrado para esa operacion**, no se repara aqui.

### LA RECETA DE `P.12` NO ESTABA DEFINIDA PARA LA FORMA QUE TIENEN 24 DE LOS 26 MIXTOS, Y ESO ES LO PRIMERO QUE HUBO QUE MEDIR

**El encargo manda, por cada acto mixto, elegir el superviviente de la PARTE A y leer el MIXTO
contra el.** Esa receta presupone una forma concreta, que es la del UNICO acto ya resuelto (el
del SPIN, vuelta 49): **una clique de pares `A` mas UN nodo colgando** que entra a la componente
por una sola arista `A` y tiene `D` con el resto. **El primer acto que se abrio en esta vuelta no
tiene esa forma**, y por eso antes de fundir nada se midio la de los veintiseis
([`../loop/SALIDA_V50_FORMA_MIXTOS.txt`](../loop/SALIDA_V50_FORMA_MIXTOS.txt)):

| forma del subgrafo `A` | actos |
|---|---:|
| **CLIQUE MAS COLGANTE**, la del SPIN, donde la receta se aplica sola | **2** |
| **ESTRELLA**, un centro que repite contra cada punta y puntas que no se parecen entre si | **24** |

**La ESTRELLA no es una rareza: es la figura `9.23` del banco**, escrita con su ejemplar y su
tabla de costes, y **el propio archivo la nombra** (el puesto **1201** dice, con esa palabra,
*este par cierra una ESTRELLA*). Lo que el banco `9.23` NO dice es quien sobrevive cuando el
centro repite contra varios nodos que son `D` entre si.

### LA DEFINICION OPERATIVA, SACADA DEL ACTO YA RESUELTO Y NO INVENTADA

**En el acto del SPIN la parte A fueron los nodos con arista `A` CONTRA EL SUPERVIVIENTE, y el
mixto fue el unico miembro SIN arista `A` contra el.** Generalizado, y es lo unico que esta
vuelta anade:

> **dado un superviviente `S`: PARTE A = `S` mas los miembros con arista `A` contra `S`;
> MIXTOS = los miembros SIN arista `A` contra `S`.**

**Y de ahi sale una comprobacion que no es criterio sino aritmetica**, corrida sobre los 26
([`../loop/SALIDA_V50_SUPERVIVIENTES_VIABLES.txt`](../loop/SALIDA_V50_SUPERVIVIENTES_VIABLES.txt)):
un superviviente es **VIABLE** si su parte A es una clique `A` (si no, fundirla juntaria dos nodos
que el archivo declaro `D`, que es lo que `P.12` prohibe) y si deja al menos un mixto fuera.

| resultado | actos |
|---|---:|
| **VARIOS VIABLES**, y el CONTENIDO decide, que es la regla de esta pagina | **26 de 26** |
| NINGUNO VIABLE, que habria sido parada | **CERO** |

> **NINGUN ACTO SE QUEDA SIN SUPERVIVIENTE POSIBLE, asi que no hay condicion de parada.** Lo que
> hay es que **en la estrella el CENTRO casi nunca es viable**: absorberlo todo juntaria las
> puntas, que son `D` entre si.

**Y UN CHOQUE MEDIDO QUE SE DEJA NOMBRADO: CINCO veredictos en CUATRO actos** (los de hoy **3**,
que trae dos, **27**, **28** y **29**): **un veredicto `A` cierra con la formula *Sobrevive X* y
ese `X` NO es viable** por la estructura del acto. La letra del veredicto y la aritmetica del acto
apuntan a sitios distintos. **No se resuelve aqui**: se mide, se nombra y se trae.

### EL ACTO 1 DE LA NOMINA DE HOY, EJECUTADO ENTERO: EL RACIMO DE LA DERIVA

| | |
|---|---|
| miembros | `deriva_hacia_el_fallo`, `drift_hacia_el_fallo`, `drift_hacia_el_fallo_2`, `normalizacion_de_la_desviacion` |
| forma | **ESTRELLA**, centro `drift_hacia_el_fallo_2`, que repite contra los otros tres (puestos **2222**, **2226**, **2237**) |
| supervivientes viables | **TRES**; el centro **NO** es viable |
| **superviviente elegido** | **`normalizacion_de_la_desviacion`**, por **CONTENIDO** y sin empate: **SEIS** pasos contra cuatro, **CUATRO** condiciones contra dos, y el resumen mas largo de los cuatro (**711** caracteres contra 574, 466 y 458). Es el mismo margen y el mismo criterio con que la vuelta 49 eligio a `modelo_spin_preguntas`. **Y lo escribe el propio veredicto `A` del par**: el **2237** cierra con *Sobrevive normalizacion_de_la_desviacion* |
| parte A fundida | `normalizacion_de_la_desviacion` absorbe `drift_hacia_el_fallo_2` |
| **vara de las puertas** | medida hoy sobre la nomina de hoy ([`../loop/SALIDA_V50_PUERTAS_EN_EL_LOTE.txt`](../loop/SALIDA_V50_PUERTAS_EN_EL_LOTE.txt)): el acto **no** esta entre los **30 SALVABLES** ni entre los **2 IMPOSIBLES**, ningun miembro es semilla ni extremo de puente. **La guarda `1B` pasa por vacio y se dice asi en vez de darla por buena** |

**NOTA DE FUENTE, que no decide pero se dice**, igual que en el acto del SPIN: los otros tres
miembros son de **Dekker** y el superviviente es de **Reason**; el que muere es de Dekker. **La
regla de la pagina pesa CONTENIDO, no procedencia**, y las piezas de Dekker viajan enteras o
adosadas: **ninguna se pierde.**

#### LAS DOS LECTURAS `P.12`, con sus citas

| el mixto | contra | veredicto | lo que lo decide |
|---|---|---|---|
| `deriva_hacia_el_fallo` | `normalizacion_de_la_desviacion` | **`CONTINUA`** | El puesto **2275**: *LA ESTRUCTURA CONTRA EL CALENDARIO*. Uno explica **por que pasa** (acoplamiento fuerte de Perrow, exploracion organizacional contra los limites de seguridad) y el otro dice **como se para**. Lo propio del mixto es **un marco analitico entero** que el superviviente no menciona, no un paso de su procedimiento |
| `drift_hacia_el_fallo` | `normalizacion_de_la_desviacion` | **`CONTINUA`** | El puesto **2394** reparte los dos con dos verbos y esas palabras: **drift VIGILA** (monitorear la brecha entre procedimiento escrito y practica real de forma sistematica, y cuestionar si el exito reciente es seguridad real) y **normalizacion FRENA**. Dos procedimientos distintos sobre la misma idea |

**LAS DOS ARISTAS QUEDAN DECLARADAS AQUI CON ID RESUELTO (`P.9`) Y SIN EJECUTARSE**, que es la
figura de [`02_DESTEJIDOS.md`](02_DESTEJIDOS.md) linea 3521, y **la poda del solape queda anotada
como pendiente de la fase 04**:

| de | a | sentido | el solape a podar |
|---|---|---|---|
| `deriva_hacia_el_fallo` | `normalizacion_de_la_desviacion` | del que explica al que remedia | la auditoria del historial, **declarada como solape por el propio 2275** |
| `drift_hacia_el_fallo` | `normalizacion_de_la_desviacion` | del que vigila al que frena | la auditoria del historial y la relajacion de criterios, **declaradas por el propio 2394** |

#### EL REPARTO DE LAS SEIS PIEZAS, impreso por el instrumento

**Ninguna se teclea: el plan trae INDICES y el instrumento lee cada pieza verbatim del fichero**
([`../loop/PLAN_V50_OPU01_ACTO1.json`](../loop/PLAN_V50_OPU01_ACTO1.json),
[`../loop/SALIDA_V50_ACTO1_EJEC.txt`](../loop/SALIDA_V50_ACTO1_EJEC.txt), exit 0).

| pieza de `drift_hacia_el_fallo_2` | destino |
|---|---|
| paso **1**, el historial de pequenos cambios acumulados | **ya lo dice el paso 1** del superviviente, **y lo escribe el 2237** |
| paso **2**, las senales descartadas o no reportadas como *malas noticias* | **viaja entero**, paso **7** |
| paso **3**, la puntualidad vuelta norma a costa de los margenes | **INCISO ADOSADO al paso 3** |
| paso **4**, la cultura donde las desviaciones son visibles | **viaja entero**, paso **8** |
| condiciones **1** y **2** | **viajan enteras**, condiciones **5** y **6** |

> **POR QUE EL PASO 3 VA DE INCISO Y NO DE `APPEND` NI DE `CUBIERTO`, que es la unica pieza fina
> del reparto:** el **2237** dice que ese paso es **un EJEMPLO** del paso 3 del superviviente.
> **`APPEND` dejaria dos pasos mandando revisar lo mismo; `CUBIERTO` perderia el ejemplar
> concreto**, que es lo unico que vuelve palpable la relajacion de criterios. Es la forma exacta
> para la que la vuelta 49 incorporo el INCISO al instrumento. **El nexo, lo unico de cosecha
> propia, va impreso aparte**: `, por ejemplo si `.

#### LAS DOS COLISIONES QUE LA FUSION FABRICO, LIMPIADAS EN EL MISMO ACTO (`P.16`)

**LA CUENTA CALZA CON LA QUE EL ENCARGO EXIGE: una colision por cada `CONTINUA`, cero por cada
`ENTRA`. Dos `CONTINUA`, DOS colisiones**, medidas con resolutor propio
([`../loop/SALIDA_V50_CENSO_COLISIONES_ACTO1.txt`](../loop/SALIDA_V50_CENSO_COLISIONES_ACTO1.txt)).

| el par resuelto | los dos veredictos | el volteo |
|---|---|---|
| `deriva_hacia_el_fallo` contra `normalizacion_de_la_desviacion` | **2222** `A` (emitido contra `drift_hacia_el_fallo_2`) y **2275** `D` | **2222: `A` a `D`** |
| `drift_hacia_el_fallo` contra `normalizacion_de_la_desviacion` | **2226** `A` (emitido contra `drift_hacia_el_fallo_2`) y **2394** `D` | **2226: `A` a `D`** |

**Las dos correcciones llevan la razon vieja ENTERA dentro, pegada POR MAQUINA y no transcrita**
([`../loop/SALIDA_V50_CORREGIR_ACTO1.txt`](../loop/SALIDA_V50_CORREGIR_ACTO1.txt)), con el carril
adjudicado en el acta de la vuelta 49, pregunta 1: **la lectura `P.12` ES la relectura conjunta
de ese `A`**, porque ese `A` se emitio contra un nodo que hoy no existe solo. **Censo tras la
limpieza: CERO colisiones vigentes.**

### LO QUE ESTA VUELTA NO HIZO DEL TRAMO 1, CON SU CIFRA

| | |
|---|---:|
| lecturas `P.12` **hechas y ejecutadas** en esta vuelta | **2** (las dos del acto 1) |
| actos **fundidos** | **1** |
| actos **MIXTOS que siguen pendientes** de `P.12`, re-medidos al cierre | **25** |
| **tramo 2** de 50 actos | **NO ABIERTO** |

> **Y LA CIFRA DEL ENCARGO NO CUADRA CON LA MEDICION, ASI QUE SE DECLARA EN VEZ DE COPIARSE**
> (regla 2 del `EJECUTOR.md`): **el encargo pide *las veinticinco lecturas `P.12` pendientes*, y
> al abrir esta vuelta eran VEINTISEIS**, medidas por miembros sobre la nomina re-corrida
> ([`../loop/SALIDA_V50_TRAMO1_POR_MIEMBROS.txt`](../loop/SALIDA_V50_TRAMO1_POR_MIEMBROS.txt)).
> **El 25 viene de la fila *lecturas `P.12` encargadas y NO hechas* del registro de la vuelta 49**,
> que en la misma pagina convive con un **26 de 26** en su medicion de la forma. **La cuenta buena
> es 26**: la vuelta 48 dejo **27** mixtos y la 49 resolvio **uno**. Con el acto 1 de esta vuelta
> hecho, **quedan 25**, que ahora si es la cifra medida y no la heredada.

### LOS DECLARADOS, IDENTIFICADOS POR SUS MIEMBROS Y NO POR SU NUMERO

**El numero baila con cada fusion y por eso no se usa** (lo manda el encargo). Los cinco del tramo
1 siguen declarados y **ninguno se toca**:

| los miembros | por que sigue declarado | numero en la vuelta 48 / ~~**hoy**~~ **AL ABRIR LA VUELTA 50** |
|---|---|---|
| `obtencion_compromiso`, `obtencion_compromiso_venta`, `obtencion_de_compromiso` | **colision de clase medida**: fundirlo fabrica una colision **aunque se funda solo el nucleo `A`**, medido hoy | 8 / **7** |
| `mejora_del_sistema_responsabilidad_gerencial`, `sistema_estable_causas_comunes`, `sistema_estable_responsabilidad_gerencial` | el puesto **2572** llama **PROVISIONAL** a su propio ganador | 29 / **24** |
| `dia_cero_defectos`, `dia_cero_defectos_2`, `dia_cero_defectos_3` | el puesto **2525** deja aviso expreso: las cadenas de firma son **incompatibles** y hay que **decidirlo, no apilarlo** | 32 / **26** |
| `domina_lo_que_compras`, `investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor` | **IMPOSIBLE POR PUERTA**: los dos miembros son puerta, alguien tendria que morir | 36 / **30** |
| `cultura_climatica_innovacion`, `cultura_de_innovacion` | **colision de clase medida**, igual que el primero | 40 / **31** |

> **CORRECCION DECLARADA DE ROTULO (20 ago 2026, vuelta 51, TAREA 1.2), adjudicada en el acta de
> la vuelta 50, seccion 3.1, con la figura del discutible D6 de la propia vuelta 50.** La columna
> de arriba se titulaba **`hoy`** y traia los numeros de la corrida de APERTURA de la vuelta 50
> (**7, 24, 26, 30, 31**,
> [`../loop/SALIDA_V50_TRAMO1_POR_MIEMBROS.txt`](../loop/SALIDA_V50_TRAMO1_POR_MIEMBROS.txt)).
> **El cierre de esa MISMA vuelta los re-midio distintos: 6, 23, 25, 29 y 30**
> ([`../loop/SALIDA_V50_TRAMO1_CIERRE.txt`](../loop/SALIDA_V50_TRAMO1_CIERRE.txt)), porque la
> fusion del acto 1 borro un acto de la nomina y corrio todos los numeros de detras. **Las cifras
> NO se reescriben: fueron exactas para la corrida que la celda cita, y reescribirlas fabricaria
> una corrida que nunca existio.** Lo que se corrige es el ROTULO, fechado a su corrida. **Los
> mismos cinco actos re-medidos al abrir la vuelta 51 siguen en 6, 23, 25, 29 y 30**
> ([`../loop/SALIDA_V51_TRAMO1_APERTURA.txt`](../loop/SALIDA_V51_TRAMO1_APERTURA.txt)). **Y la
> propia tabla ya avisaba de que el numero no se usa: la llave son los miembros.**

**Los dos IMPOSIBLES por puerta re-medidos sobre la nomina de la APERTURA DE LA VUELTA 50 son el
`domina_lo_que_compras` y `licenciamiento_tecnologico` contra
`proteccion_propiedad_intelectual_internacional`** (~~hoy el acto **156**~~ **el acto 156 en
aquella corrida**, [`../loop/SALIDA_V50_PUERTAS_EN_EL_LOTE.txt`](../loop/SALIDA_V50_PUERTAS_EN_EL_LOTE.txt);
**al abrir la vuelta 51 es el acto 155**,
[`../loop/SALIDA_V51_PUERTAS_APERTURA.txt`](../loop/SALIDA_V51_PUERTAS_APERTURA.txt)), **y el
segundo cae FUERA del tramo 1**, que es exactamente lo que decia el registro de la vuelta 48 con
la numeracion de aquel dia. **Rotulo corregido con la misma vara el 20 ago 2026 (vuelta 51,
TAREA 1.2): el ordinal era el de la apertura de la vuelta 50 y se presentaba como el de hoy. Los
DOS imposibles siguen siendo los mismos DOS por miembros, que es la llave que no baila.**

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 50 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 573 / 77 / 8 / 2.730 | **571 / 77 / 8 / 2.732** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.499 / 354 / 16.984 | **3.853 / 3.498 / 355 / 16.986** |
| retrato: `A` crudas / colapsos / pares distintos | 573 / 48 / 525 | **571 / 49 / 522** |
| actos `CERRADOS` / `ABIERTOS` | 252 / 53 | **251 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 536 / 240 | **532 / 240** |
| cola de costuras | 1.491 | **1.491**, sin cambio |
| colisiones de clase vigentes | 0 | **0** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |
| **el barrido `9.10` DEL CIERRE**, la regla del aviso | | **CORRIDO despues del ultimo movimiento**, con **diez** celdas corregidas |

---

## `OP-U-01`, TRAMO 1, LA VUELTA 51: **CUATRO ACTOS, CUATRO LECTURAS `P.12`, Y UN INSTRUMENTO QUE SE DIO EL VISTO BUENO A SI MISMO MIRANDO DONDE NO ERA** (20 ago 2026, vuelta 51)

### EL HALLAZGO DE LA VUELTA, Y ME LO HIZO A MI MISMO MI PROPIO INSTRUMENTO

**El encargo pone una guarda de cuenta:** *una colision por cada `CONTINUA` sobre mixto CON
forma y CERO por cada `ENTRA`; una colision que no calce con esa cuenta te detiene*. Para
poder cumplirla ANTES de mover un nodo, esta vuelta escribio
`scripts/loop/vuelta51_colisiones_esperadas.py`. **Y la primera version del instrumento
contaba las colisiones mirando SOLO LOS VEREDICTOS INTERNOS DEL ACTO.**

**Con esa cuenta dio el visto bueno al acto del reparto de equity**, la fusion se ejecuto, y
**el censo del archivo entero devolvio CINCO colisiones donde el instrumento habia prometido
TRES** ([`../loop/SALIDA_V51_CENSO_COLISIONES_LOTE_A.txt`](../loop/SALIDA_V51_CENSO_COLISIONES_LOTE_A.txt),
en su primera corrida). Las dos de mas eran veredictos del absorbido `split_igual_vs_desigual`
contra nodos de **FUERA del acto**: el puesto **266** contra `reparto_inicial_equity` y el
puesto **246** contra `timing_equity_split`, que al resolver caian sobre pares que el
superviviente ya tenia leidos, los puestos **754** y **688**.

> **LA LECCION, escrita donde no se pierde: UNA FUSION NO SOLO CHOCA CONSIGO MISMA.** Absorber
> un nodo arrastra **TODOS** sus veredictos, tambien los que apuntan fuera del acto, y cada uno
> puede caer sobre un par que el superviviente ya tenia leido. **Una guarda que solo mira dentro
> del acto tranquiliza sin mirar**, que es exactamente la especie de la averia que la vuelta 50
> encontro en el barrido `9.10`.

**QUE SE HIZO CON ESO, y no fue seguir:** el dataset se revirtio entero con `git checkout`, el
censo confirmo la vuelta a **CERO** colisiones, el instrumento se reescribio para **simular el
mapa de alias y re-resolver LOS 3.388 VEREDICTOS**, y las ~~25~~ **51** combinaciones de acto y
superviviente viable **de los 25 actos mixtos** se re-midieron con la aritmetica buena
([`../loop/SALIDA_V51_COLISIONES_ESPERADAS.txt`](../loop/SALIDA_V51_COLISIONES_ESPERADAS.txt)).
**De 51 combinaciones, CINCO no calzan con la cuenta del encargo.**

> **CORRECCION DE ROTULO DECLARADA (20 ago 2026, vuelta 52, TAREA 1.2; acta de la vuelta 51, seccion 3.4), y el 25 se queda tachado delante:** lo que se re-midio fueron **51 combinaciones de acto y superviviente viable**, no 25. **El 25 es la cuenta de los ACTOS MIXTOS** que habia entonces, y la frase de al lado ya publicaba el 51, asi que la pagina se contradecia consigo misma a dos lineas de distancia. La cifra buena la imprime el propio instrumento citado ([`../loop/SALIDA_V51_COLISIONES_ESPERADAS.txt`](../loop/SALIDA_V51_COLISIONES_ESPERADAS.txt)). **No es una cifra mal medida: es un nombre mal puesto a una cifra bien medida**, y por eso el tratamiento es el del rotulo y no el de la cifra.

### Y UNA FORMA DE CONTAR QUE ESTA VUELTA TUVO QUE FIJAR: **LA COLISION SE CUENTA POR PAR RESUELTO**

**El acto del consejo de calidad lo prueba:** el par resuelto `consejo_de_calidad` contra
`consejo_de_calidad_3` lleva **TRES** veredictos dentro (**2523** `A`, **2662** `A` y **2916**
`D`) y es **UNA sola colision**: los dos `A` se voltean, el `D` se queda. **Con esa forma de
contar la cuenta del encargo calza; contando veredictos, no.** Se dice porque es una decision
de lectura y no un dato.

### LAS CINCO LECTURAS `P.12`, con sus citas: **CUATRO EJECUTADAS Y UNA DETENIDA**

**Tabla generada desde los dos planes sellados**, no tecleada
(`python scripts/loop/vuelta51_registro_tramo.py`):

| el mixto | leido contra | veredicto | estado | lo que lo decide, con su puesto |
|---|---|---|---|---|
| `accion_correctiva_crosby` | `accion_correctiva_sistematica` | **`CONTINUA`** | EJECUTADA | lote A. El puesto 2805 es el veredicto DIRECTO del par y ya trae su relectura conjunta escrita (bucle vuelta 5): dice, con estas palabras, que NINGUNO DE LOS DOS CABE ENTERO EN EL OTRO. Puestos citados: 2496, 2805 |
| `scorecards_criterios_gate` | `scorecard_de_seleccion_de_proyectos` | **`CONTINUA`** | EJECUTADA | lote A. El puesto 1201 es el veredicto DIRECTO del par y lo escribe entero: EL INSTRUMENTO ES EL MISMO Y EL MOMENTO Y EL RITUAL NO SE TOCAN. Puestos citados: 1201 |
| `teoria_equidad_split_equity` | `criterios_equity_split` | **`CONTINUA`** | **HECHA, NO EJECUTADA** (el acto lo detuvo la guarda de la cuenta de colisiones) | lote A. El puesto 871 es el veredicto DIRECTO del par y lo dice sin rodeos: EL SEGUNDO ES LA PREGUNTA PREVIA DEL PRIMERO Y NO ESTA CONTENIDO EN EL, porque el checklist SUPONE YA ELEGIDA la logica de negocio. Puestos citados: 871 |
| `consejo_de_calidad_3` | `consejo_de_calidad` | **`CONTINUA`** | EJECUTADA | lote B. El puesto 2916 es el veredicto DIRECTO del par y trae su relectura conjunta entera ya escrita (bucle vuelta 5, acta del auditor de la vuelta 5): dice, verificado contra el grafo y con los nodos enteros delante, que consejo_de_calidad_3 TRAE DOS PASOS ENTEROS QUE consejo_de_calidad NO TIENE, coordinar la repeticion d.... Puestos citados: 2549, 2916 |
| `seleccion_relaciones_cofundadores` | `cofundar_con_amigos_familia_riesgos` | **`CONTINUA`** | EJECUTADA | lote B. EL VEREDICTO DIRECTO DEL PAR ESCRIBE LA PALABRA. Puestos citados: 1058 |

**LAS CINCO SALIERON `CONTINUA`, y ninguna por descarte:** en las cinco el veredicto DIRECTO
del par mixto ya era `D` y ya traia escrito por que. **En la del acto de los cofundadores el
propio veredicto escribe la palabra** (el **1058**: *por la vara del banco `9.6.1`, CONTINUA*),
y en la del consejo el **2916** cierra con *son conjuntos disjuntos de pasos propios, no
gemelos*. **Las aristas de las CUATRO ejecutadas quedan DECLARADAS con id resuelto (`P.9`) y SIN ejecutarse**, y
la poda de sus solapes queda anotada para la fase 04.

### LOS CUATRO ACTOS FUNDIDOS, con su reparto contado por el instrumento

| lote | superviviente | absorbe | piezas del reparto |
|---|---|---|---|
| **A** | `accion_correctiva_sistematica` | `accion_correctiva_5`, `accion_correctiva_6` | **15**: 5 enteras, 0 de INCISO, 10 ya dichas |
| **A** | `scorecard_de_seleccion_de_proyectos` | `scoring_model_scorecard` | **9**: 4 enteras, 2 de INCISO, 3 ya dichas |
| **B** | `consejo_de_calidad` | `consejo_calidad`, `consejo_calidad_2` | **15**: 8 enteras, 4 de INCISO, 3 ya dichas |
| **B** | `cofundar_con_amigos_familia_riesgos` | `riesgo_cofundadores_relacion_previa` | **6**: 3 enteras, 1 de INCISO, 2 ya dichas |

### EL CHOQUE DE LETRA CONTRA ARITMETICA, registrado con sus puestos

**El acta de la vuelta 50, pregunta 3, lo adjudico: MANDA LA ARITMETICA**, y manda registrar
cada choque con sus puestos. **En el acto del consejo hay CINCO**: los puestos **2631**,
**2663** y **2523** cierran con *Sobrevive `consejo_calidad`*, y los **2670** y **2662** con
*Sobrevive `consejo_calidad_2`*, **y ninguno de los dos es VIABLE**, porque su parte `A` se
lleva a los cuatro miembros y no deja ningun mixto fuera: elegirlos seria fundir entero un acto
con una `D` dentro, que es lo que `P.12` prohibe. **La letra se honra en lo que puede: los dos
nombrados mueren aqui, que es lo que sus veredictos pedian de ellos dentro de sus pares, pero
ninguno absorbe el racimo.** En los otros tres actos **ningun veredicto `A` escribe la formula
*Sobrevive X***, y se dice en vez de darlo por supuesto.

### LOS ACTOS QUE ESTA VUELTA NO FUNDE, Y POR QUE

| el acto | superviviente que el CONTENIDO elige | por que NO se funde |
|---|---|---|
| `criterios_equity_split`, `split_igual_vs_desigual`, `teoria_equidad_split_equity` | `criterios_equity_split` | DETENIDO POR LA GUARDA DE LA CUENTA DE COLISIONES DEL ENCARGO, y el acto estaba escrito entero. Con criterios_equity_split de superviviente la fusion fabrica UNA colision DENTRO del acto (la que el encargo predice, el puesto 502 contra el 871) y DOS FUERA de el, contra nodos que no son miembros: el puesto 266 (reparto_inicial_equity contra split_igual_vs_desigual, clase B) cae sobre el par del puesto 754 (criterios_equity_split contra reparto_inicial_equity, clase D), y el puesto 246 (split_igual_vs_desigual contra timing_equity_split, clase C) cae sobre el par del puesto 688 (criterios_equity_split contra timing_equity_split, clase D). Tres colisiones para una CONTINUA: la cuenta NO calza y el encargo manda detener. El superviviente alternativo teoria_equidad_split_equity SI calza, pero el CONTENIDO lo descarta por el margen mas ancho del tramo (ocho pasos contra cuatro, tres condiciones contra dos, 1.134 caracteres de resumen contra 586 y cableado de 20 contra 4), y elegirlo para hacer calzar la guarda seria dejar que la aritmetica de las colisiones decida el superviviente, que ninguna regla escrita permite. Va al auditor con la lectura P.12 hecha y las cuatro razones leidas. |

**Y DOS MAS QUE BLOQUEA LA VARA DE LAS PUERTAS, con un hallazgo sobre el instrumento que las
mide:** los actos **9** y **17** de la nomina re-medida tras el lote A tienen **DOS puertas
dentro cada uno** (`decision_cuando_fundar` mas `evaluacion_capacidades_fundador`; y
`enfoque_paso_a_paso_investigacion_mercado` mas `evaluacion_mercados_objetivo`) **y en los dos
la puerta que hace de CENTRO de la estrella tiene que morir con cualquiera de los supervivientes
viables**, asi que la guarda `1B` los rechaza
([`../loop/SALIDA_V51_PUERTAS_TRAS_LOTE_A.txt`](../loop/SALIDA_V51_PUERTAS_TRAS_LOTE_A.txt)).

> **EL HALLAZGO: `vuelta48_puertas_en_el_lote.py` LOS LLAMA SALVABLES.** Su dicotomia es
> SALVABLE (una sola puerta, el acto se funde si la puerta sobrevive) contra IMPOSIBLE (todos
> los miembros son puerta). **Falta el tercer caso: MAS DE UNA PUERTA, con alguna obligada a
> morir por la estructura del acto.** No se repara aqui, que seria alcance: se declara y se
> trae.

### LOS CINCO DECLARADOS DEL TRAMO SIGUEN DECLARADOS

**Ninguno se toca y se identifican por sus MIEMBROS**, no por su numero, que baila con cada
fusion: `obtencion_compromiso` y hermanos; `mejora_del_sistema_responsabilidad_gerencial` y
hermanos; `dia_cero_defectos` y hermanos; `domina_lo_que_compras` con
`investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor`; y `cultura_climatica_innovacion`
con `cultura_de_innovacion`. **Al cerrar la vuelta 51 son los actos ~~4, 21, 23, 27 y 28~~ 3, 19, 21, 25 y 26**
([`../loop/SALIDA_V51_TRAMO1_CIERRE.txt`](../loop/SALIDA_V51_TRAMO1_CIERRE.txt), y el rotulo va
fechado a su corrida desde el principio, que es lo que el acta 50 adjudico en su pregunta 5).

> **CORRECCION DECLARADA (20 ago 2026, vuelta 52, TAREA 1.2), y el texto viejo se queda tachado delante: LOS CINCO ORDINALES NACIERON MAL, no envejecieron.** El rotulo de la celda estaba bien fechado y la salida citada era la correcta; **las cifras venian de OTRA corrida**, la de TRAS EL LOTE A ([`../loop/SALIDA_V51_TRAMO1_TRAS_LOTE_A.txt`](../loop/SALIDA_V51_TRAMO1_TRAS_LOTE_A.txt), que imprime 4, 21, 23, 27 y 28 porque el lote B todavia no habia consumido dos actos mas). **La salida que la propia celda cita imprime 3, 19, 21, 25 y 26** ([`../loop/SALIDA_V51_TRAMO1_CIERRE.txt`](../loop/SALIDA_V51_TRAMO1_CIERRE.txt), bloque *actos de FUSION PURA vivos*). Es la caida de cifra publicada que el acta de la vuelta 51 nombra en su seccion 3.2. **Al abrir la vuelta 52 los cinco siguen en 3, 19, 21, 25 y 26**, re-medidos hoy ([`../loop/SALIDA_V52_TRAMO1_APERTURA.txt`](../loop/SALIDA_V52_TRAMO1_APERTURA.txt)), y la coincidencia no es la fuente de la correccion sino su contraste: entre el cierre de la 51 y la apertura de la 52 no se fundio ningun acto.

### LO QUE ESTA VUELTA NO HIZO DEL TRAMO 1, CON SU CIFRA MEDIDA AL CIERRE

| | |
|---|---:|
| lecturas `P.12` **hechas y ejecutadas** | **4** |
| lecturas `P.12` **hechas y NO ejecutadas** (el acto detenido por la guarda) | **1** |
| actos **fundidos** | **4** |
| actos MIXTOS que **siguen pendientes** de `P.12`, re-medidos al cierre | **21** |
| **tramo 2** de 50 actos | **NO ABIERTO** |

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 51 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 571 / 77 / 8 / 2732 | **566 / 77 / 8 / 2737** |
| grafo: ficheros / vivos / deprecados / enlaces | 3853 / 3498 / 355 / 16986 | **3853 / 3492 / 361 / 17011** |
| retrato: `A` crudas / colapsos / pares distintos | 571 / 49 / 522 | **566 / 57 / 509** |
| actos `CERRADOS` / `ABIERTOS` | 251 / 53 | **247 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 532 / 240 | **518 / 240** |
| cola de costuras | 1491 | **1489** |
| colisiones de clase vigentes | 0 | ****0**, censo propio sobre el archivo entero** |
| mixtos del tramo 1 pendientes de `P.12` | 25 | ****21**** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |

---

## `OP-U-01`, TRAMO 1, LA VUELTA 52: **TRES ACTOS FUNDIDOS, EL CARRIL DEL FILO ESTRENADO, Y CINCO ACTOS DECLARADOS CON SU ESPECIE** (20 ago 2026, vuelta 52)

### LA GUARDA DE COLISIONES YA NO ES UNA CUENTA FIJA: ES LA QUE LA SIMULACION IMPRIME

**El acta de la vuelta 51, pregunta 2c, retiro la cuenta fija del encargo viejo** (*una colision
por cada `CONTINUA` sobre mixto CON forma y CERO por cada `ENTRA`*), que era exacta para la forma
de la estrella con centro absorbido y no en general. **En su lugar: antes de cada lote se corre
`scripts/loop/vuelta51_colisiones_esperadas.py` sobre la nomina re-medida del dia, EL CENSO
ESPERADO ES EL QUE LA SIMULACION IMPRIME, por PAR RESUELTO, y una colision real FUERA de la
prediccion detiene.**

**Los dos lotes de esta vuelta cumplieron la guarda AL DIGITO.** El lote A predijo **TRES** (una
dentro del acto y dos fuera) y el censo del archivo entero devolvio **exactamente esas tres**
([`../loop/SALIDA_V52_CENSO_COLISIONES_LOTE_A.txt`](../loop/SALIDA_V52_CENSO_COLISIONES_LOTE_A.txt)).
El lote B predijo **TRES** (dos dentro y una fuera) y devolvio **exactamente esas tres**
([`../loop/SALIDA_V52_CENSO_COLISIONES_LOTE_B.txt`](../loop/SALIDA_V52_CENSO_COLISIONES_LOTE_B.txt)).
**Tras cada limpieza `P.16` el censo vuelve a CERO.**

### LAS TRES LECTURAS `P.12` EJECUTADAS, con sus citas

**Tabla generada desde los dos planes sellados**, no tecleada
(`python scripts/loop/vuelta52_registro_tramo.py`):

| el mixto | leido contra | veredicto | estado | lo que lo decide, con su puesto |
|---|---|---|---|---|
| `teoria_equidad_split_equity` | `criterios_equity_split` | **`CONTINUA`** | EJECUTADA | lote A. El puesto 871 es el veredicto DIRECTO del par y lo dice sin rodeos: EL SEGUNDO ES LA PREGUNTA PREVIA DEL PRIMERO Y NO ESTA CONTENIDO EN EL, porque el checklist SUPONE YA ELEGIDA la logica de negocio. Puestos citados: 871 |
| `sorprender_cliente_estrategico` | `regalos_estrategicos_personalizados` | **`CONTINUA`** | EJECUTADA | lote B. El puesto 1348 es el veredicto DIRECTO del par y es D, y no lo dice de pasada: lo llama TERCERA ESTRELLA DEL EJERCICIO y la primera del archivo con cobertura completa desde el dia en que se declara. Puestos citados: 251, 799, 1097, 1348 |
| `formacion_de_habitos_de_trabajo_creativo` | `gestion_de_habitos_mentales_para_pensar` | **`CONTINUA`** | EJECUTADA | lote B. El puesto 333 es el veredicto DIRECTO del par y es D, y lo escribe entero: LA FORMACION DEL HABITO CONTRA SU GESTION. Puestos citados: 261, 281, 333 |

**LAS TRES SALIERON `CONTINUA`, y en las tres el veredicto DIRECTO del par mixto ya era `D`.**
**Las aristas de las tres quedan DECLARADAS con id resuelto (`P.9`) y SIN ejecutarse**, y la
poda de sus solapes queda anotada para la fase 04. **En el acto del equity no hay arista que
declarar**: ya existe en los dos sentidos, y lo que queda es solo la poda.

### LOS TRES ACTOS FUNDIDOS, con su reparto contado por el instrumento

| lote | superviviente | absorbe | el mixto que queda vivo | piezas del reparto |
|---|---|---|---|---|
| **A** | `criterios_equity_split` | `split_igual_vs_desigual` | `teoria_equidad_split_equity` | **5**: 1 enteras, 0 de INCISO, 4 ya dichas |
| **B** | `regalos_estrategicos_personalizados` | `regalos_estrategicos_sorpresa` | `sorprender_cliente_estrategico` | **10**: 7 enteras, 2 de INCISO, 1 ya dichas |
| **B** | `gestion_de_habitos_mentales_para_pensar` | `formacion_de_habitos_de_pensamiento` | `formacion_de_habitos_de_trabajo_creativo` | **6**: 2 enteras, 1 de INCISO, 3 ya dichas |

**EN LOS TRES MUERE EL CENTRO DE LA ESTRELLA Y SOBREVIVE UN PERIFERICO**, que es la figura que
la vuelta 51 ya habia ejecutado dos veces: el centro es el que tiene arista `A` con los dos
demas, y absorberlo entero juntaria a los dos perifericos, que el archivo declara `D`.

**Y EN LOS TRES EL SUPERVIVIENTE LO ELIGIO EL CONTENIDO, NUNCA EL CONTEO DE CARACTERES**, que es
lo que el encargo de esta vuelta retiro como vara: en el del equity el contenido gana por el
margen mas ancho del tramo; **en el de los regalos las tres varas de conteo EMPATAN y decide el
MATERIAL PROPIO declarado en el puesto 799** (*resistir la tentacion de comercializar
masivamente el artefacto exclusivo, que no esta en ningun otro nodo*) contra el otro viable, al
que el puesto 251 declara repetido; **y en el de los habitos empatan pasos y condiciones, el
resumen apunta al otro y NO desempata, y decide el PADRE DECLARADO en el puesto 261**, que llama
al elegido *la version larga* del centro que muere.

### EL CARRIL DEL FILO, ESTRENADO: **TRES RELECTURAS EN EL MISMO ACTO**

**El acta de la vuelta 51, pregunta 2, lo adjudico:** una colision cuyo veredicto arrastrado es
del FILO (`B` o `C`) **NO se voltea por maquina**, porque su nodo muere o cambia de texto y eso
es la COLA DE RELECTURA POST FUSION de [`08_VERIFICACION.md`](08_VERIFICACION.md): **se RELEE el
par resuelto EN EL MISMO ACTO con el veredicto directo como contraste, y la correccion cita ESA
relectura.** Y si la relectura encuentra que lo congelado es una pregunta de POLITICA de
catalogo, **el acto NO se funde**.

| par resuelto | veredicto del FILO arrastrado o directo | contraste | que decide la relectura |
|---|---|---|---|
| `criterios_equity_split contra reparto_inicial_equity` | puesto 266, clase B, emitido contra reparto_inicial_equity mas split_igual_vs_desigual | puesto 754, clase D | **CONDICION DE TEXTO.** CONDICION DE TEXTO, y se resuelve |
| `criterios_equity_split contra timing_equity_split` | puesto 246, clase C, emitido contra split_igual_vs_desigual mas timing_equity_split | puesto 688, clase D | **CONDICION DE TEXTO.** CONDICION DE TEXTO, y se resuelve |
| `gestion_de_habitos_mentales_para_pensar contra ruptura_de_habitos_para_estimulo` | puesto 563, clase D, emitido contra formacion_de_habitos_de_pensamiento mas ruptura_de_habitos_para_estimulo | puesto 243, clase B | **CONDICION DE TEXTO.** CONDICION DE TEXTO, y se resuelve a D |

**LAS TRES SALIERON CONDICION DE TEXTO Y NINGUNA PREGUNTA DE POLITICA**, y de eso dependia que
los actos se pudieran fundir. **Las tres relecturas estan escritas en los planes ANTES de
sellarlos**, no despues de ejecutar.

> **UNA FORMA QUE NINGUN CARRIL ESCRITO CUBRE, dicha antes de resolverla y no despues:** en el
> par `gestion_de_habitos_mentales_para_pensar` contra `ruptura_de_habitos_para_estimulo` el
> veredicto **ARRASTRADO es una `D`** (el 563) y el **DIRECTO es una `B`** (el 243), que es al
> reves de los dos carriles: el del `A` arrastrado (acta 49, pregunta 1) y el del filo (acta 51,
> pregunta 2). **Lo que si es mecanico es el disparador de `08_VERIFICACION.md`: un par vuelve a
> la cola cuando uno de sus dos nodos MUERE O CAMBIA DE TEXTO, y aqui pasan las dos cosas.** Se
> relee y **se mueve el `B` directo y no la `D` arrastrada**, porque la relectura sostiene la `D`
> por su cuenta: `ruptura_de_habitos_para_estimulo` tiene CINCO pasos y solo DOS caben en el paso
> 3 del superviviente. **Mover el `B` y no la `D` es lectura del ejecutor y va marcada.**

### EL CHOQUE DE LETRA CONTRA ARITMETICA

**Ningun veredicto `A` de los tres actos fundidos escribe la formula *Sobrevive X***, medido hoy
([`../loop/SALIDA_V52_VIABLES.txt`](../loop/SALIDA_V52_VIABLES.txt)), asi que **esta vuelta no
registra ningun choque nuevo**. Se dice en vez de darlo por supuesto. **Los TRES choques que el
instrumento sigue midiendo estan en actos que esta vuelta NO toca** (los del `analisis_pareto`,
del `mistake_proofing_poka_yoke_2` y del `proceso_nominacion_seleccion`), y quedan para su
lectura.

### LOS ACTOS QUE ESTA VUELTA NO FUNDE, CADA UNO CON SU ESPECIE

| el acto, por sus MIEMBROS | especie | por que NO se funde | se acumula para |
|---|---|---|---|
| `mission_and_operations_planning`, `proceso_sop_mop`, `sop_colaborativo` | **PREGUNTA DE POLITICA DE CATALOGO CONGELADA EN UNA B** | EL PROPIO VEREDICTO DEL PAR MIXTO ESCRIBE LA PREGUNTA Y LA MANDA A LA MESA | LA MESA |
| `founder_ceo_succession_process`, `identificacion_necesidad_sucesion_ceo`, `sucesion_iniciada_por_fundador` | **EL CONTENIDO NO ALCANZA A ELEGIR Y LA RECETA NO TIENE CARRIL PARA LO QUE LA LECTURA ENCUENTRA** **[ESPECIE ADJUDICADA Y REGISTRADA, 20 ago 2026 (vuelta 53, TAREA 1.4.a): el acto queda DECLARADO POR EMPATE SIN VARA, que es el carril del encargo 2.4 de la vuelta 52; el `ENTRA` que la lectura ademas destapo es real y REFUERZA la declaracion, pero NO hace falta para sostenerla. Ver el registro entero mas abajo]** | SE DECLARA POR DOS MOTIVOS Y LOS DOS SE ESCRIBEN, porque cada uno por separado ya bastaria | LA MESA y el PARA_ALEXIS del cierre |
| `decision_cuando_fundar`, `evaluacion_capacidades_fundador`, `tres_preguntas_carrera` | **IMPOSIBLE POR PUERTA (por estructura)** | DOS PUERTAS DENTRO Y UNA OBLIGADA A MORIR | el PARA_ALEXIS del cierre |
| `enfoque_paso_a_paso_investigacion_mercado`, `evaluacion_mercados_objetivo`, `screening_mercados_potenciales` | **IMPOSIBLE POR PUERTA (por estructura)** | MISMA FIGURA EXACTA QUE EL ACTO 8 | el PARA_ALEXIS del cierre |
| `calcular_peso_dimensional_antes_cotizar`, `conocer_limites_peso_tamano_courier`, `medir_paquete_redondeando_hacia_arriba` | **IMPOSIBLE POR PUERTA (por estructura), Y EL ENCARGO NO LO NOMBRABA** | EL TERCERO QUE LA VARA REPARADA ENCUENTRA Y QUE NADIE HABIA CONTADO, y se dice asi en vez de colarlo con los otros dos | el PARA_ALEXIS del cierre |

> **EL TERCER IMPOSIBLE POR PUERTA QUE EL ENCARGO NO NOMBRABA, y es el hallazgo de la TAREA
> 1.5:** el encargo mandaba reparar `vuelta48_puertas_en_el_lote.py` con el caso *MAS DE UNA
> PUERTA con alguna obligada a morir*, y nombraba DOS actos. **La vara reparada encuentra TRES**,
> y el tercero tiene **UNA SOLA puerta**. **Lo que eso desmiente es el caso `a` del instrumento
> viejo**, escrito con estas palabras: *UN SOLO miembro protegido, el acto SE SALVA si la lectura
> elige a ese nodo como superviviente*. **Cuando esa unica puerta es el CENTRO de la estrella, la
> lectura NO PUEDE elegirlo**, porque no deja ningun mixto fuera. **La cuenta de puertas no es lo
> que decide: lo que decide es si alguna puerta esta OBLIGADA A MORIR por la estructura del
> acto**, y asi quedan las cuatro categorias del instrumento de hoy: SALVABLE, IMPOSIBLE POR
> NOMINA, IMPOSIBLE POR ESTRUCTURA y SIN RECETA
> ([`../loop/SALIDA_V52_PUERTAS_REPARADO.txt`](../loop/SALIDA_V52_PUERTAS_REPARADO.txt)).

### LOS CINCO DECLARADOS DEL TRAMO SIGUEN DECLARADOS

**Ninguno se toca y se identifican por sus MIEMBROS**, no por su numero, que baila con cada
fusion: `obtencion_compromiso` y hermanos; `mejora_del_sistema_responsabilidad_gerencial` y
hermanos; `dia_cero_defectos` y hermanos; `domina_lo_que_compras` con
`investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor`; y `cultura_climatica_innovacion`
con `cultura_de_innovacion`. **Al cerrar la vuelta 52 son los actos 2, 16, 18, 22 y 23**, leidos
de la salida que esta misma celda cita
([`../loop/SALIDA_V52_TRAMO1_CIERRE.txt`](../loop/SALIDA_V52_TRAMO1_CIERRE.txt), bloque *actos de
FUSION PURA vivos*, corrida DESPUES del ultimo movimiento de la vuelta).

### LO QUE ESTA VUELTA NO HIZO DEL TRAMO 1, CON SU CIFRA MEDIDA AL CIERRE

| | |
|---|---:|
| lecturas `P.12` **hechas y ejecutadas** | **3** |
| actos **fundidos** | **3** |
| actos **DECLARADOS** y no fundidos, con su especie escrita | **5** |
| actos MIXTOS que **siguen pendientes** de `P.12`, re-medidos al cierre | **18** |
| de esos, **bloqueados por la vara de las puertas** y que ninguna lectura salva | **3** |
| **tramo 2** de 50 actos | **NO ABIERTO**: no hubo cuerda |

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 52 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 566 / 77 / 8 / 2737 | **563 / 75 / 7 / 2743** |
| grafo: ficheros / vivos / deprecados / enlaces | 3853 / 3492 / 361 / 17011 | **3853 / 3489 / 364 / 17011** |
| retrato: `A` crudas / colapsos / pares distintos | 566 / 57 / 509 | **563 / 60 / 503** |
| actos `CERRADOS` / `ABIERTOS` | 247 / 53 | **244 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 518 / 240 | **509 / 240** |
| cola de costuras | 1489 | **1488** |
| colisiones de clase vigentes | 0 | **0**, censo propio sobre el archivo entero |
| mixtos del tramo 1 pendientes de `P.12` | 21 | **18** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |

### LAS TRES ADJUDICACIONES DEL ACTA DE LA VUELTA 52, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (20 ago 2026, vuelta 53, TAREA 1.4 del encargo)

**Las tres se adjudicaron DESPUES de que esta seccion quedara escrita**, y por eso se adosan al
final de ella en vez de reescribirla. **Ninguna cifra de arriba se toca.**

**a) EL ACTO DE LA SUCESION DEL CEO QUEDA DECLARADO POR EMPATE SIN VARA** (acta de la vuelta
52, `D2` y pregunta 2; el carril es el del encargo 2.4 de aquella vuelta, cumplido al pie).
**El contenido NO ELIGE y hay una vara para cada lado**: las condiciones apuntan a
`identificacion_necesidad_sucesion_ceo` (2 contra 1) y el **PADRE DECLARADO** del puesto 612
apunta a `sucesion_iniciada_por_fundador`. **El cableado EMPATA 3 contra 3.** Cuando el
contenido no elige y el cableado tampoco, **el acto se DECLARA como empate sin vara y se
acumula para la mesa con los demas declarados**, y eso basta por si solo. **EL `ENTRA` QUE LA
LECTURA DESTAPO ES REAL Y VA DICHO, pero no es lo que sostiene la declaracion**: los dos
veredictos `A` del acto (puestos **256** y **354**) declaran a los dos viables contenidos
ENTEROS en el centro que moriria. **Y la frontera de parada queda trazada** (acta 52, pregunta
2): si algun dia un acto NO se puede ni fundir ni declarar sin resolver un `ENTRA`, ese dia es
PARADA por doctrina nueva. **Hoy ninguno lo necesita.**

**b) EL CARRIL GENERAL DE COLISIONES DE CLASE, ADJUDICADO Y REGISTRADO** (acta de la vuelta 52,
pregunta 4). **Piezas: acta 51 pregunta 2b, [`08_VERIFICACION.md`](08_VERIFICACION.md), `P.12`
y `P.16`.**

| la forma del par resuelto | que se hace |
|---|---|
| **`A` ARRASTRADO contra un DIRECTO `D`** | **VOLTEO POR MAQUINA**, citando el directo y pegando la razon vieja entera. Es la figura de la vuelta 51 y **es el UNICO caso mecanico** |
| **un veredicto DEL FILO (`B` o `C`) en CUALQUIERA de los dos lados**, arrastrado O directo | **NADA se voltea por maquina.** El disparador de `08_VERIFICACION` ya mete el par en la cola (nodo muerto o texto cambiado): **se RELEE EN EL MISMO ACTO** con el otro veredicto como contraste, **LA RELECTURA DECIDE CUAL DE LOS DOS SE MUEVE**, y la correccion CITA esa relectura con la razon vieja entera |
| la relectura destapa **POLITICA DE CATALOGO** | **el acto NO se funde: se DECLARA** y se acumula para la mesa |

**LA FIGURA DEL CARRIL ES EL `243` DE LA VUELTA 52**, y por eso se nombra: alli el arrastrado
era una `D` (el 563) y el directo una `B` (el 243), que es al reves de los dos carriles que
habia escritos, **y la relectura movio el `B` DIRECTO porque sostuvo la `D` por su cuenta**.
**El carril general dice que eso no fue una excepcion sino la regla: la LECTURA decide, no la
direccion del arrastre.**

**LAS DOS AMPLIACIONES DEL CARRIL, ADJUDICADAS Y REGISTRADAS EL 20 ago 2026** (vuelta 54,
TAREA 1.2 del encargo; acta de la vuelta 53, preguntas 5 y 6). **Se adosan aqui, al carril que
amplian, y NO reescriben la tabla de arriba: la tabla se queda entera.**

| la forma que la tabla de arriba no cubria | que se hace | la figura |
|---|---|---|
| **CONDICION DE CONTEO O DE COBERTURA en un veredicto del filo** (el veredicto no afirma un texto: afirma una CUENTA, o pide contar antes de decidir) | **SE DESCARGA POR MEDICION ANTES DE FUNDIR**, con el instrumento y su salida CITADOS en la correccion. **Es carril de TEXTO EN SENTIDO AMPLIO**: la casilla de texto cubre TODA afirmacion verificable del veredicto, se lea en el nodo o se mida en el grafo, porque **la medicion es la lectura del grafo**. **POLITICA sigue siendo lo que pide decision de mesa, y sigue DECLARANDO el acto** | **EL `811` DE LA VUELTA 53**: su razon pedia contar la familia Coleman antes de decidir (*ya lleva cuatro nodos vistos y los pares se contradicen*). **La cuenta se corrio ANTES de fundir y dio COBERTURA 6 DE 6, CERO pares pendientes**, y contada no habia contradiccion |
| **CUANDO MOVER UN SOLO VEREDICTO DEJA LA COLISION VIVA** | **LA RELECTURA MUEVE LOS DOS**, y **lo dice en LAS DOS correcciones con la razon vieja entera**. **La vara del carril es su proposito escrito: el censo de colisiones en CERO** (`P.16` y la guarda), **no la letra del singular**. El *CUAL se mueve* de la tabla de arriba presupone que mover uno basta; cuando no basta, **la relectura, que es el mismo organo, decide QUE se mueve, uno o los dos** | **EL PAR `811` CONTRA `1222` DE LA VUELTA 53**: los dos veredictos caian sobre el MISMO par resuelto, uno `B` DIRECTO y la otra `A` arrastrada. **Dejar uno en `B` y el otro en `D` deja la colision viva**, porque `B` contra `D` sigue siendo colision de clase. **Se movieron los dos** |

**LAS DOS SON AMPLIACION Y NO EXCEPCION**, y se dice con la vara de cada una: la primera
porque **la casilla de TEXTO ya cubria toda afirmacion verificable** y lo unico que faltaba era
decirlo con esas palabras; la segunda porque **el proposito del carril es el censo en CERO**, y
un carril que dejara la colision viva no cumpliria el suyo. **NINGUNA CREA DOCTRINA NUEVA**
(acta de la vuelta 53, seccion 5, preguntas 5 y 6).

**c) EL CRITERIO DEL MIXTO QUE QUEDA CONTENIDO TRAS LA FUSION, ADJUDICADO Y REGISTRADO** (acta
de la vuelta 52, pregunta 1). **EL VEREDICTO DIRECTO MANDA.**

| el par mixto directo | que se hace |
|---|---|
| **`D`** | **MANTIENE `CONTINUA`.** La aritmetica del solape que una fusion fabrica NO tumba una lectura real del archivo. **El unico carril para moverlo es una relectura declarada**: el par entra a la cola de relectura post fusion de `08_VERIFICACION` cuando el superviviente cambia de texto, y **si ESA relectura encuentra que el mixto quedo sin nada propio, lo mueve POR LECTURA con correccion declarada, nunca por aritmetica** |
| **`B`** | **SE LEE ANTES DE FUNDIR** (acta 51, pregunta 5), y esa lectura decide su carril: si es CONDICION DE TEXTO se resuelve y el acto se funde; si es PREGUNTA DE POLITICA el acto se DECLARA |

**EL CRITERIO ASIMETRICO QUEDA RATIFICADO CON ESA FORMA**, y se dice porque la vuelta 52 lo
aplico a los dos lados en la misma tanda y lo trajo marcado: **ni el acto de los regalos (`D`,
`CONTINUA`) ni el de la sucesion (`B`, declarado) estaban mal.**

---

## `OP-U-01`, TRAMO 1, LA VUELTA 53: **EL TRAMO 1 QUEDA CERRADO. DOCE ACTOS FUNDIDOS, UN ACTO MAS DECLARADO Y CERO LECTURAS `P.12` PENDIENTES** (20 ago 2026, vuelta 53)

**Al abrir esta vuelta el tramo 1 tenia DIECIOCHO actos mixtos vivos: 13 sin mirar, 2 ya
declarados y 3 bloqueados por la vara de las puertas. Al cerrarla NO QUEDA NINGUNA LECTURA
PENDIENTE: doce de los trece se leyeron y se FUNDIERON, y el decimotercero se leyo y se DECLARO
porque su veredicto manda la pregunta a la mesa.** Los seis actos mixtos que siguen vivos son
exactamente los que ninguna lectura puede mover: dos declarados por politica, uno por empate sin
vara y tres imposibles por puerta.

### LAS DOCE LECTURAS `P.12` EJECUTADAS, con el veredicto DIRECTO de cada par leido del archivo

**Tabla generada leyendo los tres planes sellados y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**, no
tecleada (`python scripts/loop/vuelta53_registro_tramo.py`). **LA CLASE QUE SE IMPRIME ES LA DE
HOY, DESPUES de `P.16`**, y por eso las cuatro relecturas del filo aparecen ya en su clase nueva.

| el mixto | leido contra | veredicto `P.12` | estado | el veredicto DIRECTO del par, que es el que manda |
|---|---|---|---|---|
| `customer_profile` | `value_proposition_canvas` | **`CONTINUA`** | EJECUTADA | lote A. Puesto **705**, clase **D** hoy. FAMILIA DECLARADA: los dos son miembros del racimo del lienzo de propuesta de valor, remedido a SIETE miembros en la seccion 14, asi que no se pelea la clase |
| `prompting_por_persona_ia` | `ingenieria_de_prompts_efectiva` | **`CONTINUA`** | EJECUTADA | lote A. Puesto **1144**, clase **D** hoy. La anatomia del prompt contra el procedimiento de su primera linea, del mismo libro y sin arista entre ellos, y es el segundo par de la familia del prompting |
| `warrants_financiamiento` | `warrant_pricing_venture_debt` | **`CONTINUA`** | EJECUTADA | lote A. Puesto **1448**, clase **D** hoy. Como se pone el precio contra si conviene aceptarlo, del mismo libro y sin arista entre ellos, y este par CIERRA la cobertura de su familia |
| `definir_limites_huella_carbono` | `medir_huella_carbono_corporativa` | **`CONTINUA`** | EJECUTADA | lote A. Puesto **1855**, clase **D** hoy. La medicion de la huella contra la definicion de sus limites, MISMA FUENTE y sin arista entre ellos, y aqui la lectura depende de CON CUAL de los dos nodos de huella se compara |
| `costos_preparacion_franquicia` | `estimacion_inversion_inicial_franquiciador` | **`CONTINUA`** | EJECUTADA | lote B. Puesto **2092**, clase **D** hoy. Dos categorias distintas del mismo presupuesto, MISMA FUENTE y sin arista entre ellas, Y CIERRA UNA ESTRELLA |
| `contratar_abogado_franquicias` | `eleccion_abogado_franquicias` | **`CONTINUA`** | EJECUTADA | lote B. Puesto **2086**, clase **D** hoy. Dos maneras de elegir abogado que no se contienen, MISMA FUENTE y sin arista entre ellos |
| `deteccion_franquicia_inadvertida` | `prevenir_franquicias_inadvertidas` | **`CONTINUA`** | EJECUTADA | lote B. Puesto **2073**, clase **D** hoy. Prevenir la franquicia sin querer contra detectarla, MISMA FUENTE y sin arista entre ellos, y es la PRIMERA TRAMPA DE IDENTIFICADOR del dominio: dos nombres casi gemelos, deteccion_franquicia_inadvertida y prevenir_franquicias_inadvertidas, que leidos por los pasos NO se repiten |
| `eliminacion_gestion_por_objetivos_y_numeros` | `eliminar_metas_numericas_gerencia` | **`CONTINUA`** | EJECUTADA | lote B. Puesto **2534**, clase **D** hoy. Y ESTE PAR CIERRA EL HUECO QUE EL CHECKPOINT 2.500 DEJO ABIERTO PARA P.13: son los dos supervivientes del 2477 y del 2488, que nunca se habian leido entre si, y la cola si los trae |
| `principio_pareto` | `analisis_pareto_de_proveedores` | **`CONTINUA`** | EJECUTADA | lote C. Puesto **3087**, clase **D** hoy. analisis_pareto_de_proveedores (Juran: recopilar datos de defectos y rechazos por proveedor/parte/proceso, clasificar perdidas con el principio 80/20, identificar los pocos proveedores que concentran los problemas, enfocar recursos en los elementos vitales, repetir el analisis por distintas dimen... |
| `poka_yoke_a_prueba_de_errores` | `error_proofing_servicio` | **`CONTINUA`** | EJECUTADA | lote C. Puesto **2931**, clase **D** hoy. error_proofing_servicio (Juran: identificar actividades propensas a error, evaluar si se elimina, buscar sustitutos mas confiables, simplificar el trabajo, implementar deteccion temprana, disenar mecanismos para minimizar el impacto) contra poka_yoke_a_prueba_de_errores (Juran: identificar los pu... |
| `dmaic_fase_select` | `criterios_seleccion_proyectos_calidad` | **`CONTINUA`** | EJECUTADA | lote C. Puesto **2933**, clase **D** hoy. criterios_seleccion_proyectos_calidad (Juran: listar las nominaciones, evaluar por ROI/potencial de breakthrough/urgencia/viabilidad/salud del producto/resistencia, construir una matriz de evaluacion compuesta, presentar el listado priorizado al consejo de calidad) contra dmaic_fase_select (Juran... |
| `personalizacion_investigacion_prospecto` | `investigar_datos_cliente` | **`CONTINUA`** | EJECUTADA | lote C. Puesto **811**, clase **D** hoy. CORRECCION DECLARADA EL 20 ago 2026 (vuelta 53), Y LA COLISION QUE LA OBLIGA LA FABRICO ESTA MISMA VUELTA: SE DICE ASI EN VEZ DE PRESENTARLA COMO HALLAZGO |

**LAS DOCE SALIERON `CONTINUA`, y el criterio es el adjudicado en el acta de la vuelta 52,
pregunta 1, registrado en esta misma pagina por la TAREA 1.4.c de esta vuelta: EL VEREDICTO
DIRECTO MANDA.** **Las aristas de las doce quedan DECLARADAS con id resuelto (`P.9`) y SIN
ejecutarse**, y la poda de sus solapes queda anotada para la fase 04.

### LOS DOCE ACTOS FUNDIDOS, con su reparto contado por el instrumento

| lote | superviviente | absorbe | el mixto que queda vivo | piezas del reparto |
|---|---|---|---|---|
| **A** | `value_proposition_canvas` | `customer_profile_value_map` | `customer_profile` | **6**: 3 enteras, 2 de INCISO, 1 ya dichas |
| **A** | `ingenieria_de_prompts_efectiva` | `asignacion_persona_ia` | `prompting_por_persona_ia` | **6**: 0 enteras, 2 de INCISO, 4 ya dichas |
| **A** | `warrant_pricing_venture_debt` | `warrants_deuda_convertible` | `warrants_financiamiento` | **7**: 5 enteras, 0 de INCISO, 2 ya dichas |
| **A** | `medir_huella_carbono_corporativa` | `huella_carbono_empresarial` | `definir_limites_huella_carbono` | **9**: 4 enteras, 1 de INCISO, 4 ya dichas |
| **B** | `estimacion_inversion_inicial_franquiciador` | `cinco_categorias_costos_franquicia` | `costos_preparacion_franquicia` | **8**: 3 enteras, 0 de INCISO, 5 ya dichas |
| **B** | `eleccion_abogado_franquicias` | `contratar_abogado_especializado_franquicias` | `contratar_abogado_franquicias` | **6**: 1 enteras, 0 de INCISO, 5 ya dichas |
| **B** | `prevenir_franquicias_inadvertidas` | `estructuras_combinadas_franquicia` | `deteccion_franquicia_inadvertida` | **5**: 2 enteras, 1 de INCISO, 2 ya dichas |
| **B** | `eliminar_metas_numericas_gerencia` | `critica_gestion_por_objetivos` | `eliminacion_gestion_por_objetivos_y_numeros` | **5**: 1 enteras, 0 de INCISO, 4 ya dichas |
| **C** | `analisis_pareto_de_proveedores` | `analisis_pareto` | `principio_pareto` | **9**: 5 enteras, 2 de INCISO, 2 ya dichas |
| **C** | `error_proofing_servicio` | `mistake_proofing_poka_yoke_2` | `poka_yoke_a_prueba_de_errores` | **8**: 6 enteras, 1 de INCISO, 1 ya dichas |
| **C** | `criterios_seleccion_proyectos_calidad` | `proceso_nominacion_seleccion` | `dmaic_fase_select` | **7**: 3 enteras, 2 de INCISO, 2 ya dichas |
| **C** | `investigar_datos_cliente` | `seguimiento_informacion_cliente` | `personalizacion_investigacion_prospecto` | **9**: 5 enteras, 1 de INCISO, 3 ya dichas |

**EN LOS DOCE MUERE EL CENTRO DE LA ESTRELLA Y SOBREVIVE UN PERIFERICO**, que es la figura que
las vueltas 51 y 52 ya habian ejecutado cinco veces. **Y EN LOS DOCE EL SUPERVIVIENTE LO ELIGIO EL
CONTENIDO**, con el motivo escrito entero en el plan de cada acto: **en SEIS** lo decide el
ALCANCE DEL ROL o el PADRE DECLARADO que `P.8` nombra como contenido (el lienzo, los prompts, los
warrants, los costos de franquicia, el abogado y el dmaic select), **en CINCO** el conteo de pasos
y condiciones apuntando al mismo lado que el material propio (la huella, la franquicia
inadvertida, el pareto, el poka yoke y la investigacion del cliente) y **en UNO** la UNICA vara que
no empata (la gestion por objetivos). **En SIETE de los doce alguna vara apunta al otro lado, y en
los siete va dicho en el motivo del plan y marcado en el reporte:** el conteo en el lienzo, el
cableado en los prompts, en los costos de franquicia y en el pareto, las condiciones en los
warrants, el material propio en el abogado y los pasos en el dmaic select.

### EL CARRIL GENERAL DE COLISIONES, ESTRENADO EN SUS DOS FORMAS

**El carril quedo adjudicado en el acta de la vuelta 52, pregunta 4, y esta vuelta lo REGISTRO en
esta pagina (TAREA 1.4.b) para que no dependa del acta.** Las 15 correcciones de esta
vuelta se reparten en sus dos especies: **11 VOLTEOS POR MAQUINA** (`A` arrastrada contra un
directo `D`, el unico caso mecanico) y **4 RELECTURAS EN EL MISMO ACTO** (un veredicto del
filo en alguno de los dos lados). **Todas llevan la razon vieja pegada ENTERA.**

| lote | puesto | de | a | el par CRUDO | especie del carril |
|---|---:|:---:|:---:|---|---|
| **A** | **475** | A | D | `customer_profile` contra `customer_profile_value_map` | **VOLTEO POR MAQUINA** |
| **A** | **1175** | A | D | `asignacion_persona_ia` contra `prompting_por_persona_ia` | **VOLTEO POR MAQUINA** |
| **A** | **559** | A | D | `warrants_deuda_convertible` contra `warrants_financiamiento` | **VOLTEO POR MAQUINA** |
| **A** | **1865** | A | D | `definir_limites_huella_carbono` contra `huella_carbono_empresarial` | **VOLTEO POR MAQUINA** |
| **A** | **360** | C | D | `customer_profile_value_map` contra `value_map` | **RELECTURA EN EL MISMO ACTO** |
| **A** | **204** | B | D | `venture_debt_terminos_economicos` contra `warrant_pricing_venture_debt` | **RELECTURA EN EL MISMO ACTO** |
| **B** | **2075** | A | D | `cinco_categorias_costos_franquicia` contra `costos_preparacion_franquicia` | **VOLTEO POR MAQUINA** |
| **B** | **2090** | A | D | `contratar_abogado_especializado_franquicias` contra `contratar_abogado_franquicias` | **VOLTEO POR MAQUINA** |
| **B** | **2181** | A | D | `deteccion_franquicia_inadvertida` contra `estructuras_combinadas_franquicia` | **VOLTEO POR MAQUINA** |
| **B** | **2488** | A | D | `critica_gestion_por_objetivos` contra `eliminacion_gestion_por_objetivos_y_numeros` | **VOLTEO POR MAQUINA** |
| **C** | **2551** | A | D | `analisis_pareto` contra `principio_pareto` | **VOLTEO POR MAQUINA** |
| **C** | **2613** | A | D | `mistake_proofing_poka_yoke_2` contra `poka_yoke_a_prueba_de_errores` | **VOLTEO POR MAQUINA** |
| **C** | **2742** | A | D | `dmaic_fase_select` contra `proceso_nominacion_seleccion` | **VOLTEO POR MAQUINA** |
| **C** | **811** | B | D | `investigar_datos_cliente` contra `personalizacion_investigacion_prospecto` | **RELECTURA EN EL MISMO ACTO** |
| **C** | **1222** | A | D | `personalizacion_investigacion_prospecto` contra `seguimiento_informacion_cliente` | **RELECTURA EN EL MISMO ACTO** |

**LA GUARDA DE COLISIONES CUMPLIO AL DIGITO EN LOS TRES LOTES**: el lote A predijo SEIS y midio
SEIS, el B predijo CUATRO y midio CUATRO, y el C predijo CUATRO y midio CUATRO, **siempre las
mismas**. **Tras cada limpieza `P.16` el censo vuelve a CERO.**

### EL CHOQUE DE LETRA CONTRA ARITMETICA: LOS TRES CONOCIDOS, EJECUTADOS

**Los TRES choques que el instrumento venia midiendo desde la vuelta 50 caen en actos de esta
tanda, y esta vuelta los ejecuta y los registra con sus puestos**
([`../loop/SALIDA_V53_VIABLES.txt`](../loop/SALIDA_V53_VIABLES.txt)):

| el acto | el nodo que la letra nombra | los puestos que lo escriben | que paso con el |
|---|---|---|---|
| acto **19** de la nomina de apertura | `analisis_pareto` | **2546,2551** | **NO ES VIABLE por la estructura del acto y MUERE ABSORBIDO**: manda la aritmetica (acta de la vuelta 50, adjudicacion 3) |
| acto **20** de la nomina de apertura | `mistake_proofing_poka_yoke_2` | **2613** | **NO ES VIABLE por la estructura del acto y MUERE ABSORBIDO**: manda la aritmetica (acta de la vuelta 50, adjudicacion 3) |
| acto **21** de la nomina de apertura | `proceso_nominacion_seleccion` | **2627** | **NO ES VIABLE por la estructura del acto y MUERE ABSORBIDO**: manda la aritmetica (acta de la vuelta 50, adjudicacion 3) |

> **LO QUE ESTOS TRES TIENEN DE NUEVO, y va dicho en vez de colado con los cinco anteriores.** El
> acta de la vuelta 50 adjudico que manda la aritmetica y escribio que *la letra se honra en lo
> que puede: X sigue VIVO en los cinco casos*. **En estos tres NO sigue vivo: MUERE, porque el
> nodo que la letra nombra es el CENTRO de la estrella y el centro es justamente el que la receta
> no deja sobrevivir.** La adjudicacion se cumple igual en lo que si dice (nadie funde a X en
> contra de su par: los pares que lo absorben son sus dos `A`), **pero el consuelo que la
> adjudicacion escribia no aplica aqui, y por eso se marca.**

### LOS ACTOS QUE ESTA VUELTA NO FUNDE

| el acto, por sus MIEMBROS | especie | por que NO se funde | se acumula para |
|---|---|---|---|
| `influence_map_organizacional`, `mapa_de_influencia`, `mapa_organizacional_influencia` | **PREGUNTA DE POLITICA DE CATALOGO CONGELADA EN UNA B** | ES UNO DE LOS DOS ACTOS CON PAR MIXTO EN B Y SU RAZON SE LEYO ANTES DE FUNDIR, que es lo que el acta 51, pregunta 5, manda | LA MESA |

**Y LOS CINCO DECLARADOS DE SIEMPRE SIGUEN DECLARADOS, ninguno se toca**, identificados por sus
MIEMBROS y no por su numero: `obtencion_compromiso` y hermanos;
`mejora_del_sistema_responsabilidad_gerencial` y hermanos; `dia_cero_defectos` y hermanos;
`domina_lo_que_compras` con `investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor`; y
`cultura_climatica_innovacion` con `cultura_de_innovacion`. **Al cerrar la vuelta 53 son los actos
2, 8, 9, 10 y 11**, leidos del bloque *actos de FUSION PURA vivos* de
[`../loop/SALIDA_V53_TRAMO1_CIERRE.txt`](../loop/SALIDA_V53_TRAMO1_CIERRE.txt), corrida DESPUES
del ultimo movimiento de la vuelta. **Y los CINCO que no son de fusion pura tambien siguen
declarados**: el del S&OP (politica del 703), el de la sucesion del CEO (empate sin vara), el del
mapa de influencia (politica del 604, declarado ESTA vuelta) y los TRES imposibles por puerta, que
al cerrar son los actos 5, 6 y 7 de la nomina de hoy.

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 53 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 563 / 75 / 7 / 2743 | **551 / 73 / 6 / 2758** |
| grafo: ficheros / vivos / deprecados / enlaces | 3853 / 3489 / 364 / 17011 | **3853 / 3477 / 376 / 17052** |
| retrato: `A` crudas / colapsos / pares distintos | 563 / 60 / 503 | **551 / 72 / 479** |
| actos `CERRADOS` / `ABIERTOS` | 244 / 53 | **232 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 509 / 240 | **473 / 240** |
| cola de costuras | 1488 | **1483** |
| colisiones de clase vigentes | 0 | **0**, censo propio sobre el archivo entero |
| mixtos del tramo 1 pendientes de `P.12` | 18 | **6**, y los 6 DECLARADOS o BLOQUEADOS |
| actos de FUSION PURA vivos del tramo 1 (los cinco declarados de siempre) | 5 | **5** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |

> **DE DONDE SALE CADA COLUMNA, dicho para que se pueda auditar.** La columna de APERTURA del
> marcador y del grafo sale de las dos corridas propias de esta vuelta hechas ANTES de la primera
> operacion ([`../loop/SALIDA_V53_MARCADOR_APERTURA.txt`](../loop/SALIDA_V53_MARCADOR_APERTURA.txt)
> y [`../loop/SALIDA_V53_APERTURA.txt`](../loop/SALIDA_V53_APERTURA.txt)). **Las filas de retrato,
> cola y tramo 1 de esa columna NO se re-corrieron antes de la primera operacion y se dice en vez
> de callarse: son las del CIERRE de la vuelta 52**
> ([`../loop/SALIDA_V52_RECOMPUTO_CIERRE.txt`](../loop/SALIDA_V52_RECOMPUTO_CIERRE.txt),
> [`../loop/SALIDA_V52_COLA_CIERRE.txt`](../loop/SALIDA_V52_COLA_CIERRE.txt) y
> [`../loop/SALIDA_V52_TRAMO1_CIERRE.txt`](../loop/SALIDA_V52_TRAMO1_CIERRE.txt)), y valen como
> apertura porque entre el cierre de aquella vuelta y la primera operacion de esta NO se movio
> ningun nodo ni ningun veredicto, comprobado por las dos corridas propias que SI se hicieron y que
> reproducen el cierre de la 52 al digito. **La columna de CIERRE esta RECOMPUTADA AL CIERRE**,
> despues del ultimo movimiento.

### LA NOTA DE LOS 41 ENLACES, ADOSADA AL CIERRE DE ESTA SECCION (20 ago 2026, vuelta 54, TAREA 1.4 del encargo)

**El reporte de la vuelta 53 publico que el grafo GANA 41 enlaces y escribio que la resta exacta
entre las 45 vistas y los 41 no la habia derivado y no la inventaba. El acta de la vuelta 53
(seccion 3, punto 2) la derivo commit a commit. ESTA NOTA NO COPIA ESA DERIVACION: LA VUELVE A
MEDIR**, con `python scripts/loop/vuelta54_41_enlaces.py`
([`../loop/SALIDA_V54_41_ENLACES.txt`](../loop/SALIDA_V54_41_ENLACES.txt)), corrido el 20 ago
2026 en la vuelta 54, **porque la regla 2 del `EJECUTOR` dice que un acta previa nunca es fuente
de una cifra nueva: se cita como contraste. Las dos coinciden al digito.**

| commit de la vuelta 53 | enlaces MEDIDOS | delta | vistas de la simetrizacion | instancias retiradas |
|---|---:|---:|---:|---:|
| `d88c42bb`, cierre de la vuelta 52 | **17.011** | | | |
| `49ae6eef`, TAREA 1 | **17.011** | **+0** | 0 | 0 |
| `cadc9977`, LOTE A | **17.023** | **+12** | **13** | **1** |
| `04bd56de`, LOTE B | **17.030** | **+7** | **9** | **2** |
| `90bb930c`, LOTE C | **17.052** | **+22** | **23** | **1** |
| `be5d152b`, el cierre | **17.052** | **+0** | 0 | 0 |
| **la vuelta entera** | | **+41** | **45** | **4** |

**LOS TRES LOTES CALZAN UNO A UNO** (vistas menos retiros igual al delta medido: 13 menos 1 son
12; 9 menos 2 son 7; 23 menos 1 son 22), **y eso es mas fino que la resta global**: no solo 45
menos 4 son 41, sino que **cada lote cuadra por separado**. Las vistas se leen del
`symmetrize_added` horneado en `dataset/metadata/phase1_run_log.json` de cada commit; los
enlaces, con la vara de `vuelta31_estado.py` (nodos previos mas nodos siguientes sobre los 3.853
ficheros, deprecados incluidos).

**LAS CUATRO INSTANCIAS RETIRADAS, NOMBRADAS Y VERIFICADAS UNA A UNA** (el id absorbido estaba
en el campo ANTES del lote y ya no esta DESPUES):

| lote | el campo | el id absorbido que desaparece | especie | por que se retira |
|---|---|---|---|---|
| **A** | `warrant_pricing_venture_debt.nodos_previos` | `warrants_deuda_convertible` | **AUTO-ARISTA** | el absorbido redirige AL PROPIO NODO, y una arista a si mismo no se escribe |
| **C** | `criterios_seleccion_proyectos_calidad.nodos_previos` | `proceso_nominacion_seleccion` | **AUTO-ARISTA** | igual: el absorbido redirige al propio nodo |
| **B** | `elaboracion_fdd.nodos_previos` | `contratar_abogado_especializado_franquicias` | **COLAPSO DE DUPLICADA** | el superviviente `eleccion_abogado_franquicias` **YA ESTABA en el campo**, verificado, y las dos instancias colapsan en una |
| **B** | `sistema_estable_causas_comunes.nodos_siguientes` | `critica_gestion_por_objetivos` | **COLAPSO DE DUPLICADA** | el superviviente `eliminar_metas_numericas_gerencia` **YA ESTABA en el campo**, verificado |

**45 MENOS 4 SON 41, medido commit a commit y lote a lote.** **La frase del reporte de la vuelta
53 (*`P.16` retiro por su lado duplicadas y dos auto-aristas*) queda CONFIRMADA y ahora con los
cuatro nombres.**

---

## `OP-U-01`, TRAMO 2: **ABIERTO Y CON VEINTIUN ACTOS FUNDIDOS. LOS CINCUENTA SON DE FUSION PURA Y NINGUNO PIDE `P.12`** (20 ago 2026, vuelta 54)

> ### ADJUDICACION REGISTRADA: **LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO** (20 ago 2026, vuelta 55, TAREA 1.2 del encargo; adjudicada por el acta de la vuelta 54, pregunta 1)
>
> **La pregunta que esta nota cierra:** cuando el CONTENIDO elige al miembro que **no** es puerta,
> quien manda, `P.8` o la guarda `1B`. **El instrumento de las puertas la traia sin resolver desde
> la vuelta 48** y el tramo 2 la hizo caer dos veces (actos **1** y **15**).
>
> **LA RESPUESTA, POR EXTENSION CITABLE Y SIN DOCTRINA NUEVA: LA GUARDA RESTRINGE Y EL CONTENIDO
> ELIGE ENTRE LO PERMITIDO.** Sus piezas, cada una con su sede:
>
> | la pieza | que aporta | donde vive |
> |---|---|---|
> | **la receta ratificada** | ya tiene esa arquitectura: primero se computan los **VIABLES** por estructura, y entre los viables **elige el contenido** | banco `9.3.1`, ratificada en el acta de la vuelta 50 |
> | **la vara del acta 51, pregunta 3** | la guarda `1B` es obligatoria y define al candidato **LIMPIO**: imposible por puerta es **solo** el acto donde NINGUNA fusion la respeta | acta de la vuelta 51 |
> | **la PRECISION DE LA ESTRELLA** | dice la figura entera: **el preferido que no es viable muere absorbido por el viable** | banco `9.3.1`, adosada en la vuelta 54 |
> | **el acta 50, adjudicacion 3** | en el choque entre la letra y la aritmetica **MANDA LA ARITMETICA**, y el choque **se registra con sus puestos** | acta de la vuelta 50 |
>
> **LA CONSECUENCIA, ESCRITA PARA QUE NO HAYA QUE DEDUCIRLA:** en un acto de dos donde el unico
> candidato limpio es la puerta, **el contenido no tiene entre quien elegir**. **LA PUERTA
> SOBREVIVE**, el choque de conteos **se registra en el motivo** con las cifras impresas, y **las
> piezas propias del absorbido viajan enteras por el reparto**, que es lo que protege el contenido
> que el conteo prefirio. **EJECUTADA EN LA VUELTA 55** sobre los actos **1** y **15**, los dos con
> sus conteos escritos en el motivo del plan sellado.
>
> **LO QUE ESTA ADJUDICACION NO DICE, y se dice para que no se estire:** no toca los **IMPOSIBLES
> POR ESTRUCTURA**, que no son un choque sino un cierre y se siguen DECLARANDO.

> ### ADJUDICACION REGISTRADA: **EL `entregable_esperado` NO ES RAZON, Y LOS ACTOS 4, 20 Y 42 QUEDAN DECLARADOS Y ACUMULAN PARA LA MESA** (20 ago 2026, vuelta 55, TAREA 1.3 del encargo; adjudicada por el acta de la vuelta 54, pregunta 2)
>
> **La pregunta que esta nota cierra:** en un acto de UN SOLO PAR cuyos conteos de contenido chocan,
> el `entregable_esperado` de los nodos vale como PIEZA DECLARADA (alcance del rol), o solo valen
> las razones.
>
> **LA RESPUESTA ES NO, Y POR LA LETRA:** la receta dice *pasos y condiciones, material propio y
> padre declarado **EN LAS RAZONES***, y el `entregable_esperado` es **campo del nodo, no razon**.
> Leerlo como pieza declarada seria **doctrina nueva**, y el bucle no escribe doctrina nueva: la
> decide el fundador si quiere.
>
> **EL CARRIL QUE SI APLICA, Y YA ESTABA ESCRITO:** con conteos que chocan y **CERO** piezas
> declaradas, el acto se **DECLARA** y **ACUMULA PARA LA MESA**, que es el mismo carril del acto que
> las reglas vigentes no pueden fundir (la politica del `703` y la del `604`, el empate sin vara del
> CEO, los imposibles por puerta). **Se declara, se acumula, el bucle sigue.**
>
> | el acto | sus miembros | el choque medido |
> |---|---|---|
> | **4** | `hr_calidad_gestion`, `hr_como_control_de_calidad_gerencial` | pasos **6 contra 4** a un lado, condiciones **1 contra 2** al otro |
> | **20** | `fases_de_retencion_de_clientes`, `ocho_fases_experiencia_cliente` | pasos **3 contra 4** a un lado, condiciones **2 contra 1** al otro |
> | **42** | `fase_acclimate_experiencia_cliente`, `fase_acclimate_mapa_de_proceso` | pasos **5 contra 8** a un lado, condiciones **2 contra 1** al otro |
>
> **NINGUNO DE LOS TRES SE TOCA**, y los tres siguen vivos al cerrar la vuelta 55.
>
> **EL PENDIENTE DE DOCTRINA QUEDA ABIERTO PARA LA MESA, CON NOMBRE PROPIO:** o una **prelacion
> entre conteos de contenido** (que vara manda cuando los pasos y las condiciones apuntan a lados
> distintos), o una **ampliacion de donde vive la pieza declarada** (que campos del nodo, ademas de
> la razon, pueden declarar padre, contencion o alcance del rol). **Las dos son decision de
> fundador.**


**LA DEFINICION DEL TRAMO NO SE DECIDIO: SE MIDIO.** La definicion vigente es la de la cabecera
del registro del tramo 1 (*los CINCUENTA primeros actos `CERRADOS` de la nomina re-medida al
abrirlo, en el orden en que el instrumento los imprime*), y **los CINCUENTA SIGUIENTES admitian
dos lecturas.** `python scripts/loop/vuelta54_tramo2_nomina.py`
([`../loop/SALIDA_V54_TRAMO2_NOMINA.txt`](../loop/SALIDA_V54_TRAMO2_NOMINA.txt)) **computa LAS
DOS y las compara**:

| lectura | que dice | resultado |
|---|---|---|
| **A, por el orden de HOY** | se re-mide la nomina hoy, se marcan los actos del tramo 1 que siguen vivos **identificados POR SUS MIEMBROS** (que es la doctrina de esta pagina) y el tramo 2 son los 50 `CERRADOS` siguientes | los once del tramo 1 ocupan los puestos **1 a 11** y el tramo 2 es del **12 al 61** |
| **B, por el orden del dia en que se abrio el tramo 1** | el tramo 2 son los que ocupaban los puestos **51 a 100** de [`../loop/RECOMPUTO_V48_COMPONENTES.jsonl`](../loop/RECOMPUTO_V48_COMPONENTES.jsonl) | **50 actos, los mismos** |

> **LAS DOS DAN EL MISMO TRAMO EN EL MISMO ORDEN**, comprobado acto por acto, **y el instrumento
> cae en ROJO con PARADA si algun dia no calzan.** Una operacion cuyo texto no alcanza para
> ejecutarse sin decidir detiene; esta alcanza, y la prueba esta impresa.

### LA FORMA DEL TRAMO 2, Y ES LO CONTRARIO DEL TRAMO 1

| | |
|---|---:|
| actos del tramo | **50** |
| por tamano | **los 50 de tamano 2** |
| por figura | **{'PURO A': 50, 'MIXTO': 0}** |
| nodos implicados | **100** |
| **lecturas `P.12` que este tramo pide** | **CERO** |

**NO HAY NI UNA SOLA LECTURA `P.12` EN ESTE TRAMO, y se dice porque es la diferencia entera con
el tramo 1**, que dejo veintisiete mixtos esperando cinco vueltas: **un acto de dos miembros con
UN par `A` directo no deja ningun mixto fuera**, asi que la receta de la estrella no tiene nada
que decidir. **Lo que este tramo pide es la otra mitad de `P.8`: quien sobrevive por CONTENIDO.**

**LAS DOS GUARDAS DE ENTRADA, LAS DOS EN VERDE:** la **guarda de los cuatro ajenos** (ninguno de
los cuatro que esta pagina declara fuera de `OP-U-01` desde el 11 ago 2026 entra en el tramo, y
**ninguno esta ya en el lote `CERRADO` entero**) y la **guarda de solape con el tramo 1** (cero
actos del tramo 2 tocan un miembro de un acto del tramo 1).

### LA GUARDA DE COLISIONES NO CUBRIA ESTA FORMA, Y SE DICE EN VEZ DE APAGARLA

**Corrido `scripts/loop/vuelta51_colisiones_esperadas.py` sobre la nomina del dia como manda el
encargo, NO IMPRIME NI UNO de los cincuenta actos**
([`../loop/SALIDA_V54_COLISIONES_ESPERADAS.txt`](../loop/SALIDA_V54_COLISIONES_ESPERADAS.txt)).
**El motivo esta escrito en su propio codigo**, la linea 130: `continue  # fusion pura, no pide
P.12`. **Y es correcto para lo que aquel instrumento mide:** nacio para la guarda de cuenta de la
vuelta 51, que cuenta una colision por cada mixto en `CONTINUA`.

**La guarda no se apaga y el instrumento viejo no se falsea: se escribe un SUCESOR DECLARADO**,
`scripts/loop/vuelta54_colisiones_esperadas.py`, con **la misma aritmetica copiada de aquel** y
la rama que faltaba ([`../loop/SALIDA_V54_COLISIONES_ESPERADAS_TRAMO2.txt`](../loop/SALIDA_V54_COLISIONES_ESPERADAS_TRAMO2.txt)).
**Lo que predice, sobre el archivo entero y antes de tocar un nodo:**

| | |
|---|---:|
| combinaciones simuladas (cada acto por cada eleccion posible) | **100** |
| combinaciones que fabrican alguna colision | **6** |
| **actos del tramo que fabrican colision** | **TRES**: el **6** con dos, el **44** con una y el **49** con dos |
| **actos del tramo que no fabrican ninguna** | **47** |

**LAS CINCO COLISIONES PREVISTAS SON TODAS `B` DIRECTO CONTRA `D` Y TODAS FUERA DEL ACTO**, o
sea del carril del filo: **relectura EN EL MISMO ACTO.** **Los tres actos NO se tocan en esta
vuelta y quedan nombrados abajo.**

### LOS VEINTIUN ACTOS FUNDIDOS, en dos lotes

| lote | actos | fundidos | nodos que mueren | piezas repartidas | enteras | ya dichas | de `INCISO` |
|---|---|---:|---:|---:|---:|---:|---:|
| **A** | 2, 3, 5, 7, 8, 9, 10, 11, 12, 13 y 14 | **11** | **11** | **70** | **19** | **38** | **13** |
| **B** | 16, 17, 19, 21, 22, 23, 24, 25, 26 y 27 | **10** | **10** | **57** | **16** | **35** | **6** |
| **los dos** | | **21** | **21** | | | | |

**LAS CUATRO FORMAS DEL VEREDICTO QUE EL TRAMO 2 TRAE, contadas por maquina sobre los cincuenta**
([`../loop/SALIDA_V54_VARAS_TRAMO2.txt`](../loop/SALIDA_V54_VARAS_TRAMO2.txt)) **y aplicadas en
los veintiuno:**

| la forma | cuantos de los 50 | que decide |
|---|---:|---|
| **TODAS DE ACUERDO** | **13** | las varas de contenido que no empatan apuntan al mismo lado |
| **UNA SOLA VARA** | **22** | solo una vara de contenido no empata, **y BASTA** (acta de la vuelta 53, pregunta 4) |
| **CHOCAN** | **5** | decide **LA PIEZA DECLARADA** de mayor peso en las razones; **si no hay ninguna, es PARADA** (acta 53, pregunta 3) |
| **CONTENIDO EMPATA** | **9** | **EL CABLEADO DECIDE SOLO** |
| **EMPATE SIN VARA** | **1** | tampoco el cableado separa: **se DECLARA** |

### LOS ACTOS QUE ESTA VUELTA NO FUNDE, CADA UNO CON SU ESPECIE

| acto | especie | por que no se funde |
|---|---|---|
| **1** (`balance_eficiencia_responsividad`, `trade_off_responsividad_eficiencia`) y **15** (`apertura_efectiva_llamada_venta`, `apertura_llamada_venta_grande`) | **EL CONTENIDO APUNTA AL QUE NO ES PUERTA** | La guarda `1B` exige que la puerta sobreviva y el contenido elige al otro (pasos 6 contra 4 y condiciones 3 contra 2 en el 1; pasos 5 contra 4 en el 15). **Ese choque entre la vara de la fase y el Gate 0 no lo resuelve ninguna regla escrita hoy**, y el propio instrumento de las puertas lo dice desde la vuelta 48: *va como pregunta al auditor, no como decision.* **SE DECLARAN** |
| **4** (`hr_calidad_gestion`, `hr_como_control_de_calidad_gerencial`), **20** (`fases_de_retencion_de_clientes`, `ocho_fases_experiencia_cliente`) y **42** (`fase_acclimate_experiencia_cliente`, `fase_acclimate_mapa_de_proceso`) | **CONTEOS DE CONTENIDO QUE CHOCAN SIN PIEZA DECLARADA** | Los pasos apuntan a un lado y las condiciones al otro, y la razon **no declara ni padre, ni contencion, ni alcance del rol** en ninguna direccion: la del 326 llega a escribir que los dos anadidos son *la misma deteccion por dos caminos*. **El acta de la vuelta 53, pregunta 3, manda PARAR y traerlo como pregunta antes de fundir**, y eso es lo que se hace |
| **18** (`desconexion_ventas_experiencia`, `traspaso_ventas_cuentas`) | **EMPATE SIN VARA** | pasos 4 contra 4, condiciones 3 contra 3 **y cableado 2 contra 2**. Es el unico del tramo donde TODO empata, que es lo que la receta reserva para declarar |
| **6**, **44** y **49** | **COLISION PREVISTA, PENDIENTE DE RELECTURA** | los tres fabrican colision de clase con un `B` DIRECTO contra una `D`, y el carril del filo pide **relectura EN EL MISMO ACTO**. **No hubo cuerda en esta vuelta y quedan nombrados** |
| los **veinte** restantes (28 a 41, 43, 45 a 48 y 50) | **SIN TOCAR POR FALTA DE CUERDA** | ninguna guarda los frena: quedan para el siguiente tramo de trabajo |

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 54 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 73 / 6 / 2758 | **551 / 73 / 6 / 2758**, sin mover |
| grafo: vivos / deprecados / enlaces | 3477 / 376 / 17052 | **3456 / 397 / 17118** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 72 / 479 | **551 / 93 / 458** |
| actos `CERRADOS` / `ABIERTOS` | 232 / 53 | **211 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 473 / 240 | **431 / 240** |
| cola de costuras | 1483 | **1489** |
| colisiones de clase vigentes | 0 | **0**, censo propio sobre el archivo entero |
| actos del tramo 2 fundidos / pendientes | 0 / 50 | **21 / 29** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |

> **DE DONDE SALE CADA COLUMNA.** **LAS DOS COLUMNAS SON CORRIDAS PROPIAS DE ESTA VUELTA, y
> ninguna fila de la apertura se hereda del cierre anterior**, que es lo que la regla de la
> apertura pide desde el `D1` de la vuelta 53: marcador
> ([`../loop/SALIDA_V54_MARCADOR_APERTURA.txt`](../loop/SALIDA_V54_MARCADOR_APERTURA.txt)),
> estado ([`../loop/SALIDA_V54_APERTURA.txt`](../loop/SALIDA_V54_APERTURA.txt)), retrato y actos
> ([`../loop/SALIDA_V54_RECOMPUTO_APERTURA.txt`](../loop/SALIDA_V54_RECOMPUTO_APERTURA.txt)),
> cola ([`../loop/SALIDA_V54_COLA_APERTURA.txt`](../loop/SALIDA_V54_COLA_APERTURA.txt)),
> colisiones ([`../loop/SALIDA_V54_COLISIONES_APERTURA.txt`](../loop/SALIDA_V54_COLISIONES_APERTURA.txt))
> y duplicadas ([`../loop/SALIDA_V54_DUPLICADAS_APERTURA.txt`](../loop/SALIDA_V54_DUPLICADAS_APERTURA.txt)),
> **todas corridas ANTES de la primera operacion.** La columna de cierre esta **RECOMPUTADA AL
> CIERRE**, despues del ultimo movimiento.

> **EL MARCADOR NO SE MUEVE Y NO ES UN OLVIDO DEL BARRIDO.** Esta vuelta **no volteo ni un
> veredicto**: los veintiun actos fundidos son de fusion pura y **ninguno fabrico colision**, asi
> que `P.16` no tuvo nada que limpiar. **Por eso las DOS tablas por dominio hermanas tampoco se
> mueven: la `A` de cada uno de los diez dominios es la misma al digito.** La hermandad escrita
> en la TAREA 1.1 de la vuelta 53 **se cumple POR VACIO, y se dice asi en vez de darla por
> cumplida.** **Lo que si se movio son las tres celdas del retrato** (`RECOMPUTO_3388.md` 247,
> 248 y 528), corregidas con tachado, contador cuadrado y nota fechada por el barrido `9.10` del
> cierre: **21 colapsos mas, UNO POR CADA ACTO FUNDIDO.**

---

## `OP-U-01`, TRAMO 2 **CERRADO: 45 ACTOS FUNDIDOS DE 50 Y CINCO DECLARADOS** (20 ago 2026, vuelta 55)

**EL TRAMO 2 QUEDA CERRADO EN CODIGO**: de sus **50** actos, **45 estan fundidos** y **CINCO
quedan DECLARADOS**, cada uno con su especie escrita y su carril. La vuelta 55 ejecuto
**VEINTICINCO fusiones** en tres lotes, y **una de ellas es una fusion REHECHA**: el acto **23**,
que la vuelta 54 habia fundido al reves y que esta vuelta deshizo y volvio a hacer con correccion
declarada.

### EL INSTRUMENTO DEL TRAMO CAYO EN ROJO AL CONTINUAR, Y EL ROJO NO DECIA LO QUE DECIA

**Corrido `scripts/loop/vuelta54_tramo2_nomina.py` sobre la nomina del dia como el encargo manda,
CAE EN ROJO CON PARADA** ([`../loop/SALIDA_V55_TRAMO2_NOMINA.txt`](../loop/SALIDA_V55_TRAMO2_NOMINA.txt)).
**El motivo se fue a mirar antes de tocar nada, y es estructural y no del tramo:** aquel
instrumento nacio para **ABRIR** un tramo y compara los 50 `CERRADOS` siguientes de HOY contra los
puestos 51 a 100 de la nomina de la vuelta 48. **En cuanto se funde un acto del tramo, el acto sale
de la nomina de `CERRADOS`, la lectura B encoge y la lectura A rellena hasta 50 con actos del tramo
SIGUIENTE.** El rojo dice *el tramo ya se toco*, no *el tramo no esta determinado*.

**SUCESOR DECLARADO, por la vara del acta 54, pregunta 3** (sus cifras ya las cita la tabla de las
dos lecturas de esta misma pagina, asi que la logica del ancestro NO se toca):
`scripts/loop/vuelta55_tramo2_nomina.py`, **con la aritmetica copiada**, la identidad del tramo
**POR MIEMBROS** de los puestos 51 a 100 de la 48, **el ordinal derivado del fichero y no tecleado**,
y el calzar de la continuacion en **dos formas**
([`../loop/SALIDA_V55_TRAMO2_NOMINA_SUCESOR.txt`](../loop/SALIDA_V55_TRAMO2_NOMINA_SUCESOR.txt)):

| lo que el sucesor comprueba | resultado al abrir la vuelta 55 |
|---|---|
| los 50 del tramo, repartidos entre VIVOS y FUNDIDOS | **29 vivos y 21 fundidos**, suma 50 de 50 |
| los FUNDIDOS, comprobados uno a uno contra el grafo | **21 de 21**: los dos ids resuelven a UNO y el superviviente lleva el alias izado |
| **lectura A** (orden impreso de hoy) contra **lectura B** (orden de la vuelta 48), sobre los vivos | **CALZAN**, mismo conjunto y mismo orden |
| los supervivientes son **PREFIJO** de la lectura A de hoy | **SI**, ningun acto ajeno se cuela por delante |
| guarda de los cuatro ajenos | **VERDE**, ninguno de los cuatro entra |
| guarda de solape con el tramo 1 | **VERDE**, cero |

> **Y LOS 29 ORDINALES QUE IMPRIME REPRODUCEN AL DIGITO LOS QUE LA VUELTA 54 PUBLICO**, porque el
> ordinal se deriva del puesto de la vuelta 48 menos 50 y no de un contador nuevo.

### LOS TRES LOTES, TALLADOS DE LOS PLANES SELLADOS

**Estas tres tablas NO estan tecleadas: salen enteras de
`python scripts/loop/vuelta55_tallar_planes.py`**
([`../loop/SALIDA_V55_TALLAR_PLANES.txt`](../loop/SALIDA_V55_TALLAR_PLANES.txt)), **que las cuenta
de los `PLAN_V55_*.json` sellados**. Es el remedio mecanico de la caida de reporte que el acta de
la vuelta 54 nombra: una tabla que resume decisiones se talla de los planes, no de memoria.

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **T1** | 18, 23 | **2** | **2** | **13** | 5 | 4 | **4** | **1** |
| **A** | 1, 15, 28, 29, 30, 31, 32, 33, 34, 35, 36 | **11** | **11** | **75** | 28 | 32 | **15** | **2** |
| **B** | 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 50 | **12** | **12** | **68** | 20 | 39 | **9** | **1** |
| **los tres** | | **25** | **25** | **156** | **53** | **75** | **28** | **4** |

> ### CORRECCION DECLARADA: **LAS CUATRO PERDIDAS NO SON TODAS DE CONDICIONES. SON TRES Y UNA** (20 ago 2026, vuelta 56, TAREA 1.2 del encargo; caida de reporte nombrada por el acta de la vuelta 55, seccion 3)
>
> **LA CELDA DE ARRIBA DICE `4` PERDIDAS NOMBRADAS Y ESA CIFRA ES CORRECTA: son cuatro.** Lo que
> estaba mal era **SU ESPECIE**, y la correccion se escribe **aqui** porque esta es la celda desde
> la que la cifra se podria heredar.
>
> **ESTA TABLA NO ESTA TECLEADA: sale entera de
> `python scripts/loop/vuelta56_tallar_perdidas_v55.py`**
> ([`../loop/SALIDA_V56_TALLAR_PERDIDAS_V55.txt`](../loop/SALIDA_V56_TALLAR_PERDIDAS_V55.txt)),
> **que la talla de los `PLAN_V55_*.json` SELLADOS y lee la especie del propio plan**, sin rama por
> defecto: si el trozo sellado no nombra ni condicion ni paso, o nombra los dos, el tallador sale
> **ROJO con el acto nombrado** y no emite tabla. **La ultima columna trae la frase sellada
> VERBATIM**, recortada por maquina, para que la etiqueta no haya que creersela.
>
> | acto | lote | el nodo que muere | **ESPECIE** | por que se perdio | la frase del plan sellado que lo dice |
> |---:|:---:|---|---|---|---|
> | **18** | T1 | `traspaso_ventas_cuentas` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 habla de quejas de CLIENTES y la condicion 1 del superviviente dice CLIENTES NUEVOS, que es mas estrecho; el INCISO para condiciones no existe en el instrumento (pendiente de doctrina heredado) y por eso la perdida se nombra en vez de repararse* |
> | **31** | A | `traffic_partners_hypothesis` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA, UNA: su condicion 1 acota el disparador a los negocios WEB O MOVIL y la del superviviente no lo acota; el INCISO para condiciones no existe en el instrumento y la perdida se nombra* |
> | **33** | A | `leap_of_faith_questions` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA, UNA: su condicion 2 acota el disparador a los SUPUESTOS FINANCIEROS sin validar y la condicion 1 del superviviente habla de suposiciones sin acotar; el INCISO para condiciones no existe en el instrumento y la perdida se nombra* |
> | **45** | B | `milk_run_deliveries` | **DE PARAMETRO DE PASO** | el inciso MENTIRIA contra la unica restriccion del paso que protege | *PERDIDA NOMBRADA, UNA, Y LA ELECCION SE DECLARA: el paso 3 del que muere nombra las VENTANAS DE TIEMPO junto a la capacidad de vehiculo como restricciones que deciden la tecnica de ruteo, y el paso 4 de la madre dice que la asignacion generalizada es para cuando LA UNICA restriccion es la capacidad del vehiculo* |
> | **suma** | | | **3 DE CONDICIONES, 1 DE PARAMETRO DE PASO** | | |
>
> **TRES DE CONDICIONES Y UNA DE PARAMETRO DE PASO.** **El `D8` del reporte de la vuelta 55 las
> llamo a las CUATRO de condiciones, y esa es la caida de reporte que el acta de la vuelta 55
> nombra en su seccion 3.** **EL REPORTE VIEJO NO SE EDITA** (una correccion que tapa lo que
> corrige no se puede auditar, banco `9.10`): **la correccion vive aqui**. Y se deja dicho que
> **aquel mismo reporte describia BIEN el caso del 45 en su `D5` y lo generalizaba MAL en su
> `D8`**: la caida no fue de medicion, fue de dictado.

> ### EL PENDIENTE DE DOCTRINA DEL `INCISO` DE CONDICIONES, NOMBRADO EN EL REGISTRO CON SU CUENTA MEDIDA (20 ago 2026, vuelta 56, TAREA 1.3 del encargo)
>
> **UNA MEDICION DEL DIA QUE SE DECLARA EN VEZ DE CALLARSE, porque cambia donde va esta nota:** la
> TAREA 1.3 pedia dejar la cuenta *donde ese pendiente este nombrado en el registro*, y **medido hoy
> por `grep` sobre `docs/plan/`, EL PENDIENTE NO ESTABA NOMBRADO EN NINGUNA PAGINA DEL PLAN**.
> Vivia solo en `docs/loop/REPORTE.md` y en `docs/loop/ACTA_AUDITOR.md`. **Asi que se nombra aqui
> por primera vez, pegado a la cuenta que lo mide**, que es el unico sitio del registro donde tiene
> con que sostenerse.
>
> **EL PENDIENTE, dicho entero:** el instrumento de fundir conoce el destino `INCISO` para los
> **PASOS** y **no para las CONDICIONES**. Mientras no exista, una condicion del que muere que dice
> **casi** lo mismo que una del superviviente solo tiene dos destinos: **`APPEND`**, que fabrica
> condiciones casi gemelas, o **`CUBIERTO` con perdida nombrada**.
>
> **SU COSTO, MEDIDO Y NO ESTIMADO: TRES perdidas de condicion en UNA SOLA VUELTA** (los actos
> **18**, **31** y **33** de la vuelta 55, contados por el tallador de arriba) **son el costo de
> que el `INCISO` de condiciones no exista.**
>
> **LA RAMA DE MANDARLAS DE `APPEND` QUEDO CONTESTADA** (acta de la vuelta 55, pregunta 5): **NO
> por defecto.** Fabricar condiciones casi gemelas para no nombrar una perdida **esconde el sintoma
> que mantiene visible este pendiente**, y **la perdida NOMBRADA es el carril mientras siga
> abierto**.
>
> **LA DECISION DE CREAR EL `INCISO` DE CONDICIONES SIGUE SIENDO DE LA MESA.** Este registro no la
> toma: la nombra, la mide y la deja acumulada.


| la forma, leida del motivo sellado | cuantos | los actos |
|---|---:|---|
| **UNA SOLA VARA de contenido no empatada, y BASTA** | **11** | 18, 29, 30, 31, 34, 36, 37, 39, 46, 47, 48 |
| **TODAS LAS VARAS de contenido de acuerdo** | **7** | 32, 35, 38, 41, 43, 44, 50 |
| **EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO** | **3** | 28, 33, 40 |
| **LA PUERTA SOBREVIVE, con el choque de conteos registrado** | **2** | 1, 15 |
| **CORRECCION DECLARADA, la fusion rehecha al reves** | **1** | 23 |
| **LA PIEZA DECLARADA decide, y la puerta apunta al mismo lado** | **1** | 45 |
| **suma** | **25** | |

| acto | lote | sobrevive | absorbe | piezas | enteras | ya dichas | `INCISO` |
|---:|:---:|---|---|---:|---:|---:|---:|
| **1** | A | `trade_off_responsividad_eficiencia` | `balance_eficiencia_responsividad` | 9 | 6 | 3 | 0 |
| **15** | A | `apertura_llamada_venta_grande` | `apertura_efectiva_llamada_venta` | 7 | 4 | 1 | 2 |
| **18** | T1 | `desconexion_ventas_experiencia` | `traspaso_ventas_cuentas` | 7 | 2 | 3 | 2 |
| **23** | T1 | `modelo_tradicional_introduccion_producto` | `modelo_cascada_desarrollo_producto` | 6 | 3 | 1 | 2 |
| **28** | A | `rediseno_procesos_negocio_cx` | `rediseno_procesos_negocio_cliente` | 11 | 8 | 3 | 0 |
| **29** | A | `deep_dive_workshop` | `metodologia_deep_dive` | 6 | 1 | 3 | 2 |
| **30** | A | `fase_assess_ciclo_cliente` | `fase_assess_experiencia_cliente` | 7 | 3 | 3 | 1 |
| **31** | A | `test_socios_de_trafico` | `traffic_partners_hypothesis` | 6 | 1 | 3 | 2 |
| **32** | A | `fracaso_como_aprendizaje_startup` | `fallo_como_aprendizaje_startup` | 6 | 0 | 6 | 0 |
| **33** | A | `leap_of_faith_assumptions` | `leap_of_faith_questions` | 6 | 1 | 4 | 1 |
| **34** | A | `key_resources_hypothesis` | `recursos_clave` | 5 | 0 | 2 | 3 |
| **35** | A | `planificacion_preguntas_implicacion` | `preguntas_implicacion` | 4 | 1 | 2 | 1 |
| **36** | A | `content_marketing_blog` | `blogging_como_canal_de_traccion` | 8 | 3 | 2 | 3 |
| **37** | B | `desirability_feasibility_viability` | `triada_restricciones_diseno` | 6 | 2 | 3 | 1 |
| **38** | B | `fase_admit_celebracion` | `fase_admit` | 5 | 2 | 3 | 0 |
| **39** | B | `usuarios_extremos_edge_cases` | `usuarios_extremos_insights` | 5 | 1 | 2 | 2 |
| **40** | B | `jerarquia_datos_scor` | `business_intelligence_niveles_datos` | 6 | 4 | 2 | 0 |
| **41** | B | `compatibilidad_motivaciones_riqueza_control` | `alineacion_motivacional_cofundadores` | 5 | 2 | 2 | 1 |
| **43** | B | `lead_bullets_no_silver_bullets` | `estrategia_de_balas_de_plomo` | 5 | 0 | 3 | 2 |
| **44** | B | `reparto_inicial_equity` | `formalizacion_acuerdo_equity` | 4 | 2 | 1 | 1 |
| **45** | B | `programacion_entregas_delivery_scheduling` | `milk_run_deliveries` | 7 | 2 | 5 | 0 |
| **46** | B | `contratar_ambicion_correcta` | `screening_ambicion_organizacional` | 6 | 0 | 5 | 1 |
| **47** | B | `wallas_etapa_incubacion` | `periodo_incubacion_mental` | 6 | 1 | 5 | 0 |
| **48** | B | `framework_caracteristicas_ventajas_beneficios` | `diferencia_ventaja_beneficio` | 6 | 3 | 3 | 0 |
| **50** | B | `reunion_conclusion_proyecto` | `encuesta_satisfaccion_postproyecto` | 7 | 1 | 5 | 1 |

### LAS TRES ADJUDICACIONES QUE ESTA VUELTA EJECUTA, CON SU SEDE

| la adjudicacion | de donde viene | donde se ejecuta |
|---|---|---|
| **LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO** | acta de la vuelta 54, pregunta 1 | actos **1** y **15**, con el choque de conteos escrito en el motivo de cada plan |
| **EL MATERIAL PROPIO DECLARADO DE UN SOLO LADO ES UNA VARA NO EMPATADA** | acta de la vuelta 54, pregunta 4, y relectura conjunta de la vuelta 55 | actos **18** (fundido) y **23** (correccion declarada y fusion rehecha) |
| **EL `entregable_esperado` NO ES RAZON: se declara y acumula para la mesa** | acta de la vuelta 54, pregunta 2 | actos **4**, **20** y **42**, que **no se tocan** |

### LAS CINCO RELECTURAS DEL FILO: **UNA SE RESUELVE Y CUATRO DESTAPAN PREGUNTA DE POLITICA**

**Las cinco estaban predichas y nombradas con sus puestos antes de tocar un nodo**
([`../loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAMO2.txt`](../loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAMO2.txt)),
y las cinco se releyeron por el carril general de colisiones **con sus dos ampliaciones**:

| acto | los dos puestos | que decide la relectura | consecuencia |
|---:|---|---|---|
| **44** | **218** `B` contra **1008** `D` | **CONDICION DE TEXTO, y se resuelve.** La condicion de CONTEO Y COBERTURA se descargo MIDIENDO ANTES: la madre despacha el momento en **UNA LINEA** (su paso 1) y el hijo trae un **PROCEDIMIENTO de cuatro decisiones**, tres de ellas ausentes de la madre. La vara del banco `9.6.1` devuelve **CONTINUA**, no repite | **el 218 pasa de `B` a `D`** con correccion declarada y la razon vieja entera pegada por maquina, y **el acto SE FUNDE** |
| **6** | **668** `B` contra **1312** `D` | **PREGUNTA DE POLITICA DE CATALOGO.** La propia razon del 668 escribe que *esa diferencia de alcance la tiene que resolver **la mesa del racimo del pivote**, no yo* | **el acto NO se funde** |
| **6** | **968** `B` contra **1305** `D` | **PREGUNTA DE POLITICA DE CATALOGO.** La razon del 968 dice que *si el criterio adoptado fuera un nodo por PUERTA, este par sobrevive entero*, y que es **el unico de los cuatro cruzados donde los dos criterios de la mesa dan respuestas distintas** | **el acto NO se funde** |
| **49** | **338** `B` contra **490** `D` | **PREGUNTA DE POLITICA DE CATALOGO.** La razon del 338 escribe que juzgar de dos en dos *da respuestas incoherentes* y que **esto pide mesa de los tres a la vez** | **el acto NO se funde** |
| **49** | **297** `B` contra **497** `D` | **PREGUNTA DE POLITICA DE CATALOGO.** La razon del 297 dice *no lo decido*, y deja las dos lecturas abiertas | **el acto NO se funde** |

> **EL CARRIL DEL FILO SE CUMPLE EN SU LETRA:** el acta de la vuelta 51, pregunta 2, dice que si la
> relectura encuentra que lo congelado es **una pregunta de POLITICA de catalogo, el acto NO se
> funde**. **Cuatro de las cinco lo son, y los actos 6 y 49 quedan DECLARADOS.** El propio par `A`
> del acto 49 (puesto **536**) ya lo escribia: *este par vive entero dentro del racimo nuevo de la
> puerta del ajuste, y por la regla operativa registrada en la seccion 9 no se pelea la clase aqui*.

> **LA AMPLIACION DE MOVER LOS DOS NO HIZO FALTA, Y SE COMPROBO EN VEZ DE SUPONERSE:** en el acto
> 44 mover UN solo veredicto cierra la colision, porque el 1008 ya era `D`. **El censo esperado se
> RE-CORRIO despues de la correccion** y baja de UNA colision a **CERO** para ese acto
> ([`../loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAS_FILO.txt`](../loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAS_FILO.txt)).

> ### ADJUDICACION REGISTRADA: **UNA RAZON QUE REMITE A UNA MESA, O QUE SE ABSTIENE, ES PREGUNTA DE POLITICA Y BLOQUEA EL ACTO** (20 ago 2026, vuelta 56, TAREA 1.1 del encargo; adjudicada por el acta de la vuelta 55, pregunta 1)
>
> **La pregunta que esta nota cierra**, y que la tabla de arriba hizo caer cinco veces: cuando una
> razon del filo dice *esto lo decide la mesa* o *no lo decido*, eso cuenta como **PREGUNTA DE
> POLITICA que BLOQUEA el acto**, o como **MATIZ que no lo bloquea**. De ella dependian los actos
> **6** y **49**, que la vuelta 55 declaro en vez de fundir.
>
> **LA RESPUESTA, POR EXTENSION CITABLE Y SIN DOCTRINA NUEVA: ES PREGUNTA DE POLITICA, Y BLOQUEA.**
> Y con ella va **LA MARCA OPERATIVA**, para que la lectura no dependa del gusto de quien lee:
>
> | la forma de la razon | que es | que se hace con el acto |
> |---|---|---|
> | **REMITE** la decision a una **INSTANCIA NOMBRADA** (una mesa, un criterio por adoptar) | **PREGUNTA DE POLITICA** | **NO se funde**: se **DECLARA** y acumula para esa mesa |
> | **SE ABSTIENE** con sus palabras (*no lo decido*) | **PREGUNTA DE POLITICA** | **NO se funde**: se **DECLARA** y acumula |
> | **RESERVA que la propia razon resuelve, o que una VARA ESCRITA resuelve** | **MATIZ** | **se resuelve y el acto SE FUNDE** |
>
> **LAS DOS SEDES, citadas y no resumidas:** el **acta de la vuelta 51, pregunta 2**, que fija el
> carril del filo (*si la relectura encuentra que lo congelado es una pregunta de POLITICA de
> catalogo, el acto NO se funde*) y de la que esta adjudicacion es **extension citable**; y el
> **acta de la vuelta 55, pregunta 1**, que fija la **marca operativa** de arriba.
>
> **LAS FIGURAS ESTAN EN ESTA MISMA TABLA, y por eso la nota va aqui y no en otra pagina:** los
> cuatro pares de los actos **6** y **49** (**668**, **968**, **338** y **297**) escriben la
> remision o la abstencion **con sus palabras**, y los dos actos quedan **DECLARADOS**; el **218**
> del acto **44** era una **RESERVA que una vara escrita resuelve**, la del banco `9.6.1` (la linea
> contra el procedimiento), **y por eso ese acto SI se fundio**. **Cuatro y uno, en la misma
> tanda**: es el contraste el que hace legible la marca.
>
> **LO QUE ESTA ADJUDICACION NO DICE, para que no se estire:** **no contesta ninguna** de las
> preguntas de politica que las cuatro razones destapan. **Quien las contesta sigue siendo la mesa**
> del `PARA_ALEXIS` del cierre, y ese pendiente de doctrina **sigue abierto y engordado** con los
> actos 6 y 49.


### LOS CINCO ACTOS QUE EL TRAMO 2 DEJA DECLARADOS, CADA UNO CON SU CARRIL

| acto | sus miembros | especie | se acumula para |
|---:|---|---|---|
| **4** | `hr_calidad_gestion`, `hr_como_control_de_calidad_gerencial` | **CONTEOS DE CONTENIDO QUE CHOCAN SIN PIEZA DECLARADA** | **LA MESA**, con el pendiente de doctrina nombrado |
| **20** | `fases_de_retencion_de_clientes`, `ocho_fases_experiencia_cliente` | **CONTEOS DE CONTENIDO QUE CHOCAN SIN PIEZA DECLARADA** | **LA MESA** |
| **42** | `fase_acclimate_experiencia_cliente`, `fase_acclimate_mapa_de_proceso` | **CONTEOS DE CONTENIDO QUE CHOCAN SIN PIEZA DECLARADA** | **LA MESA** |
| **6** | `pivotar_o_proceder`, `pivote_o_proceder` | **PREGUNTA DE POLITICA DE CATALOGO CONGELADA EN DOS `B` DEL FILO** | **LA MESA DEL RACIMO DEL PIVOTE**, que las dos razones nombran |
| **49** | `fit_problema_solucion`, `problem_solution_fit` | **PREGUNTA DE POLITICA DE CATALOGO: LA FAMILIA PIDE MESA DE LOS TRES A LA VEZ** | **LA MESA DEL RACIMO DE LA PUERTA DEL AJUSTE** |

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 55 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 73 / 6 / 2758 | **551 / 72 / 6 / 2759** |
| grafo: vivos / deprecados / enlaces | 3456 / 397 / 17118 | **3432 / 421 / 17168** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 93 / 458 | **551 / 117 / 434** |
| actos `CERRADOS` / `ABIERTOS` | 211 / 53 | **187 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 431 / 240 | **383 / 240** |
| cola de costuras | 1489 | **1482** |
| colisiones de clase vigentes | 0 | **0**, censo propio sobre el archivo entero |
| auto-pares (los dos lados al mismo vivo) | 72 | **96** |
| duplicadas historicas: grupos / nodos | 988 / 779 | **983 / 774** |
| actos del tramo 2 fundidos / pendientes | 21 / 29 | **45 / 5, los cinco DECLARADOS** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** en los tres lotes |

> **DE DONDE SALE CADA COLUMNA.** **LAS DOS SON CORRIDAS PROPIAS DE ESTA VUELTA**: marcador
> ([`../loop/SALIDA_V55_MARCADOR_APERTURA.txt`](../loop/SALIDA_V55_MARCADOR_APERTURA.txt) y
> [`../loop/SALIDA_V55_MARCADOR_CIERRE.txt`](../loop/SALIDA_V55_MARCADOR_CIERRE.txt)),
> estado ([`../loop/SALIDA_V55_APERTURA.txt`](../loop/SALIDA_V55_APERTURA.txt) y
> [`../loop/SALIDA_V55_CIERRE.txt`](../loop/SALIDA_V55_CIERRE.txt)),
> retrato y actos ([`../loop/SALIDA_V55_RECOMPUTO_APERTURA.txt`](../loop/SALIDA_V55_RECOMPUTO_APERTURA.txt)
> y [`../loop/SALIDA_V55_RECOMPUTO_CIERRE.txt`](../loop/SALIDA_V55_RECOMPUTO_CIERRE.txt)),
> cola, colisiones y duplicadas en sus ficheros `_APERTURA` y `_CIERRE` hermanos.
> **La columna de apertura se corrio ANTES de la primera operacion y la de cierre DESPUES del
> ultimo movimiento**, y **ninguna celda de esta tabla esta tecleada**: las extrae
> `python scripts/loop/vuelta55_registro_tramo.py` de esas mismas salidas.

> **EL MARCADOR SI SE MUEVE ESTA VEZ, Y ES LA DIFERENCIA CON LA VUELTA 54.** La relectura del filo
> del acto 44 corrigio el puesto **218** de `B` a `D`, asi que **`B` baja de 73 a 72 y `D` sube de
> 2.758 a 2.759**. **`A` y `C` no se mueven**, y por eso **las DOS tablas por dominio hermanas
> tampoco**: publican la `A` de cada dominio y la `A` de los diez es la misma al digito en las dos
> corridas. **La hermandad se cumple POR VACIO y se dice, en vez de darse por cumplida.** **Las
> veinticinco fusiones NO movieron el marcador por si solas:** son de fusion pura y ninguna fabrico
> colision, asi que `P.16` no tuvo nada que limpiar.

> **EL RETRATO SE MUEVE VEINTICUATRO, NO VEINTICINCO, Y LA CUENTA SE DEJA ESCRITA:** esta vuelta
> ejecuto **25** fusiones, pero el acto 23 es una fusion **REHECHA** sobre un acto que ya estaba
> colapsado en la apertura, y su deshacer resto uno antes de sumar los veinticinco. **93 menos 1
> mas 25 son 117**, y **458 menos 24 son 434**, que vuelve a ser la resta exacta (551 crudas menos
> 117 colapsos). Las celdas 247, 248 y 528 de `RECOMPUTO_3388.md` y las filas `B` y `D` del
> marcador publicado en `INTRA_DOMINIO_INFORME.md` quedan corregidas con tachado, contador cuadrado
> y nota fechada por el barrido `9.10` del cierre.

---

## `OP-U-01`, TRAMO 3 **ABIERTO Y CERRADO EN LA MISMA VUELTA: 47 ACTOS FUNDIDOS DE 50 Y TRES DECLARADOS** (20 ago 2026, vuelta 56)

**EL TRAMO 3 SE ABRE Y SE CIERRA EN LA MISMA VUELTA**: de sus **50** actos, **47 estan fundidos**
y **TRES quedan DECLARADOS**, cada uno con su especie escrita y su carril. Es el primer tramo de
`OP-U-01` que no necesita una segunda vuelta.

### LA FRONTERA DEL TRAMO: **LAS DOS LECTURAS NO CALZAN, Y LA DIVERGENCIA QUEDA EXPLICADA ENTERA**

**El abridor es `scripts/loop/vuelta56_tramo3_nomina.py`**
([`../loop/SALIDA_V56_TRAMO3_NOMINA.txt`](../loop/SALIDA_V56_TRAMO3_NOMINA.txt)), con la
**identidad POR MIEMBROS** copiada del sucesor de la vuelta 55 y el **ORDINAL** copiado del
ABRIDOR de la vuelta 54 (la posicion en el orden impreso de hoy). **Se dice de cual se copia cada
pieza porque no son la misma**: el sucesor derivaba el ordinal del puesto de la nomina de la 48
porque aquel tramo ya estaba abierto y sus ordinales ya estaban publicados; este tramo se ABRE hoy
y no tiene ordinal publicado que respetar.

| lo que el abridor comprueba | resultado al abrir la vuelta 56 |
|---|---|
| **guarda del prefijo**: los vivos de los tramos 1 y 2 ocupan los puestos 1 a N **sin huecos** | **SI**, y son **16**, medido y no tecleado (11 del tramo 1 y 5 del tramo 2) |
| **LECTURA A**: los 50 `CERRADOS` siguientes en el orden impreso de HOY | los puestos **17 a 66** |
| **LECTURA B**: los que ocupaban los puestos **101 a 150** de la nomina de la vuelta 48 | **50 actos**, los 50 vivos hoy |
| las dos lecturas, en conjunto y en orden | **NO CALZAN**: uno solo en A, uno solo en B |
| guarda de los cuatro ajenos, **camino literal** | **VERDE**, ninguno de los cuatro entra |
| guarda de los cuatro ajenos, **POR EL RESOLUTOR** | **MUERDE** donde el literal pasaba por vacio |
| guarda de solape con los tramos 1 y 2 | **VERDE**, CERO |
| figura de los 50 | **FUSION PURA los 50**, tamano 2 y `PURO A` |

> **LA DIVERGENCIA, DIAGNOSTICADA CON EL FICHERO DELANTE Y CON LA CADENA MEDIDA COMMIT A COMMIT.**
> **Solo en A**: `construir_sobre_ideas_ajenas` mas `reglas_brainstorming`, hoy en el puesto **23**,
> que **en la nomina de la 48 NO EXISTIA como `CERRADO`**: alli era la componente **62**, **ABIERTA
> y de tamano 3**, con `pensamiento_convergente_divergente` dentro. **Se partio cuando la vuelta 49
> corrigio el veredicto del puesto 844** (`brainstorming_divergente` contra
> `generar_multiples_opciones`) **de `A` a `D`**, por una de las tres colisiones de clase que el
> acta de la vuelta 48 mando releer: ese par resuelve a `pensamiento_convergente_divergente` contra
> `reglas_brainstorming` y **era la unica arista `A` que ataba al tercero a la componente**.
> **Solo en B**: `crecimiento_ingresos_verdes` mas `generacion_ingresos_verdes`, que ocupaba el
> puesto **150** de la 48 y hoy cae en el **67**, **UNO por detras del corte: DESPLAZADO al tramo
> siguiente, no perdido.**

> **EL TRAMO SE TOMA POR LA VARA VIGENTE Y NO SE ELIGE A OJO.** La cabecera del registro del tramo
> 1 de esta misma pagina dice desde la vuelta 48 que el tramo son *los CINCUENTA primeros actos
> CERRADOS de la NOMINA RE-MEDIDA AL ABRIRLO, en el orden en que el instrumento los imprime*, que
> es **la LECTURA A**. La lectura B no es una vara rival: es la comprobacion de que entre una
> apertura y la siguiente no ha pasado nada que el ejecutor no haya medido. **El abridor no elige:
> DIAGNOSTICA, y solo continua si toda divergencia cae en una de las dos formas explicadas** (un
> `CERRADO` nacido despues en el lado A, un acto desplazado detras del corte en el lado B).
> **Cualquier otra es ROJO y PARADA.**

> **Y LA GUARDA DE LOS CUATRO AJENOS SE LEE AHORA POR DOS CAMINOS** (regla 9 del `EJECUTOR.md`,
> `P.1`): el ajeno **`brainstorming_divergente`** esta **DEPRECADO** y vive hoy dentro del
> `ids_alias` de **`reglas_brainstorming`**, que es miembro del **acto 7**. **Por el camino LITERAL,
> que es el que corrian los abridores de los tramos 1 y 2, la guarda pasa POR VACIO y nadie se
> entera.** **EL ACTO SE FUNDIO IGUAL, Y LA VARA VA ESCRITA**: esta misma pagina midio esa guarda
> **SOBRE LAS COMPONENTES** el 19 ago 2026 y escribio que `ab_testing_optimizacion` y
> `brainstorming_divergente` *ya no aparecen en ninguna componente* porque sus operaciones
> corrieron y los deprecaron; **por esa vara escrita la guarda esta VERDE hoy tambien**. Y **la
> fusion NO TOCA AL AJENO por ningun lado**: el nodo que lleva su alias es **el que SOBREVIVE**, el
> que muere es `construir_sobre_ideas_ajenas`, y ni el id ni el alias ni la clase del ajeno cambian.

### LOS TRES LOTES, TALLADOS DE LOS PLANES SELLADOS

**Estas tablas NO estan tecleadas: salen enteras de
`python scripts/loop/vuelta56_tallar_planes.py`**
([`../loop/SALIDA_V56_TALLAR_PLANES.txt`](../loop/SALIDA_V56_TALLAR_PLANES.txt)), **que las cuenta
de los `PLAN_V56_*.json` sellados** y **cae en ROJO con el acto nombrado si un motivo no encaja en
ninguna forma conocida**.

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **A** | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 | **17** | **17** | **100** | 30 | 52 | **18** | **5** |
| **B** | 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34 | **16** | **16** | **101** | 49 | 36 | **16** | **1** |
| **C** | 35, 36, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50 | **14** | **14** | **82** | 31 | 31 | **20** | **5** |
| **los tres** | | **47** | **47** | **283** | **110** | **119** | **54** | **11** |

| la forma, leida del motivo sellado | cuantos | los actos |
|---|---:|---|
| **TODAS LAS VARAS de contenido de acuerdo** | **19** | 3, 4, 7, 9, 10, 13, 14, 15, 17, 19, 20, 21, 28, 30, 32, 34, 38, 39, 40 |
| **UNA SOLA VARA de contenido no empatada, y BASTA** | **15** | 1, 5, 11, 12, 16, 24, 25, 29, 31, 33, 36, 41, 42, 48, 50 |
| **EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO** | **10** | 2, 6, 18, 22, 26, 43, 44, 46, 47, 49 |
| **LA PUERTA SOBREVIVE, con el choque registrado** | **2** | 8, 35 |
| **CONTEOS QUE CHOCAN CON LA PIEZA DECLARADA, y decide la declarada** | **1** | 23 |
| **suma** | **47** | |

| acto | lote | sobrevive | absorbe | piezas | enteras | ya dichas | `INCISO` |
|---:|:---:|---|---|---:|---:|---:|---:|
| **1** | A | `economia_de_la_experiencia` | `diseno_de_experiencias_participativas` | 5 | 1 | 4 | 0 |
| **2** | A | `evaluacion_vp_ventas` | `framework_evaluacion_director_ventas` | 8 | 4 | 3 | 1 |
| **3** | A | `plan_a_b_c_soft_landing` | `restructuracion_deuda_soft_landing` | 5 | 2 | 3 | 0 |
| **4** | A | `publicidad_offline_pruebas_locales` | `tracking_publicidad_offline` | 5 | 2 | 2 | 1 |
| **5** | A | `desarrollo_presentacion_problema` | `presentacion_problema_tres_columnas` | 6 | 1 | 3 | 2 |
| **6** | A | `gamificacion_onboarding_visual` | `visualizacion_progreso_onboarding` | 6 | 2 | 4 | 0 |
| **7** | A | `reglas_brainstorming` | `construir_sobre_ideas_ajenas` | 4 | 1 | 2 | 1 |
| **8** | A | `five_whys_inversion_proporcional` | `tecnica_cinco_porques` | 8 | 3 | 5 | 0 |
| **9** | A | `fase_accomplish_experiencia_cliente` | `fase_accomplish` | 5 | 1 | 3 | 1 |
| **10** | A | `acquisicion_viral_engineering` | `herramientas_adquisicion_viral` | 6 | 1 | 4 | 1 |
| **11** | A | `ficcion_especulativa_como_metodo` | `historia_del_futuro_escenarios_especulativos` | 7 | 0 | 4 | 3 |
| **12** | A | `evaluacion_industria_cliente` | `analisis_disrupciones_mercado` | 7 | 4 | 2 | 1 |
| **13** | A | `definicion_alineacion_cadena_suministro` | `alineacion_cadena_estrategia_negocio` | 5 | 2 | 1 | 2 |
| **14** | A | `creacion_data_warehouse` | `data_warehouse_como_fundamento` | 5 | 1 | 3 | 1 |
| **15** | A | `ciclo_de_conversion_de_efectivo` | `dso_dpo_gestion_capital_trabajo` | 6 | 1 | 3 | 2 |
| **16** | A | `fase_mobilizar_modelo_negocio` | `fase_mobilizacion_equipo_multifuncional` | 5 | 1 | 3 | 1 |
| **17** | A | `community_building_estrategia` | `construccion_de_comunidad_como_canal_traccion` | 7 | 3 | 3 | 1 |
| **18** | B | `embudo_secuencial_de_inversores` | `seleccion_etapa_fondo_vc` | 6 | 2 | 4 | 0 |
| **19** | B | `vesting_acciones_fundadores` | `eleccion_estructura_vesting_founder` | 9 | 4 | 4 | 1 |
| **20** | B | `homogeneidad_vs_diversidad_equipo` | `diversidad_vs_homogeneidad_equipo` | 6 | 3 | 2 | 1 |
| **21** | B | `ia_como_nivelador_habilidades` | `ia_colaborador_productividad` | 6 | 2 | 3 | 1 |
| **22** | B | `mantener_puntaje_innovacion` | `auditoria_desempeno_new_products` | 6 | 4 | 2 | 0 |
| **23** | B | `duration_estimating_worksheet` | `estimacion_tres_puntos` | 7 | 2 | 4 | 1 |
| **24** | B | `eventos_offline_como_canal_traccion` | `eventos_offline_propios` | 8 | 6 | 0 | 2 |
| **25** | B | `genchi_gembutsu_salir_del_edificio` | `genchi_gembutsu` | 6 | 2 | 3 | 1 |
| **26** | B | `technology_platform_evaluation` | `flexible_go_kill_criteria` | 6 | 2 | 3 | 1 |
| **28** | B | `simulacion_de_operaciones_supply_chain` | `simulacion_diseno_cadena_suministro` | 7 | 5 | 1 | 1 |
| **29** | B | `colaboracion_transporte_ctm` | `collaborative_transportation_management` | 6 | 3 | 2 | 1 |
| **30** | B | `search_for_business_model` | `customer_development_vs_business_plan` | 6 | 2 | 4 | 0 |
| **31** | B | `planificacion_consecuencias_no_intencionadas` | `anticipar_consecuencias_negativas` | 6 | 4 | 1 | 1 |
| **32** | B | `estrategia_multicanal_bienvenida` | `seis_medios_comunicacion_cliente` | 5 | 1 | 2 | 2 |
| **33** | B | `intellectual_property_strategy` | `proteccion_propiedad_intelectual` | 5 | 2 | 1 | 2 |
| **34** | B | `metricas_accionables` | `aprendizaje_validado_vs_metricas_vanidad` | 6 | 5 | 0 | 1 |
| **35** | C | `alineacion_de_objetivos_en_sistemas` | `diseno_de_sistemas_a_escala` | 6 | 2 | 2 | 2 |
| **36** | C | `esfuerzo_voluntario_vs_urge_espontaneo` | `control_voluntario_del_pensamiento` | 5 | 3 | 2 | 0 |
| **38** | C | `cuatro_etapas_del_pensamiento_creativo` | `wallas_etapa_iluminacion` | 5 | 1 | 2 | 2 |
| **39** | C | `practica_de_observacion_atenta` | `observar_lo_ordinario` | 4 | 0 | 3 | 1 |
| **40** | C | `bullseye_framework` | `middle_ring_testing` | 7 | 2 | 3 | 2 |
| **41** | C | `diseno_consecuencias_no_intencionadas` | `diseno_fugitivo_runaway_design` | 7 | 3 | 2 | 2 |
| **42** | C | `arquitectura_tecnica_modular` | `arquitectura_flexible_soa` | 6 | 2 | 3 | 1 |
| **43** | C | `entrenamiento_funcional_empleados` | `entrenamiento_empleados_startup` | 6 | 2 | 2 | 2 |
| **44** | C | `convertir_necesidad_en_demanda` | `insight_observacion_empatia` | 6 | 4 | 1 | 1 |
| **46** | C | `business_model_canvas_scorecard` | `business_model_canvas_vs_plan` | 8 | 6 | 1 | 1 |
| **47** | C | `bucle_retroalimentacion_autoajustable` | `ciclos_retroalimentacion_autoajuste` | 6 | 2 | 2 | 2 |
| **48** | C | `evitar_greenwashing` | `evitar_greenwashing_2` | 5 | 1 | 3 | 1 |
| **49** | C | `contabilidad_ambiental` | `herramientas_contabilidad_ambiental` | 6 | 2 | 2 | 2 |
| **50** | C | `reduccion_cargas_regulatorias` | `reduccion_cargas_cumplimiento` | 5 | 1 | 3 | 1 |

| acto | lote | sus miembros | especie | se acumula para |
|---:|:---:|---|---|---|
| **27** | B | `decision_pivote_perseverar`, `pivotar_o_perseverar` | **CONTEOS DE CONTENIDO QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA** | LA MESA, con el pendiente de doctrina 1 de la vuelta 55, ahora con CUATRO actos y no tres |
| **37** | C | `seis_herramientas_comunicacion_celebracion`, `seis_herramientas_comunicacion_fase_activate` | **EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN** | LA MESA. Y con un dato de familia que la propia razon aporta y conviene que la mesa tenga delante: este par cierra el tratamiento de la serie de los seis medios de Coleman, porque prueba que LAS INSTANCIAS POR FASE TAMBIEN SE REPITEN ENTRE ELLAS, no solo los dos nodos generales. La serie esta duplicada tantas veces como fases la instancien, y eso es una decision de catalogo, no de par. |
| **45** | C | `framework_flujos_de_datos_ppp`, `framework_ppph_flujos` | **EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN** | LA MESA. La propia razon lo llama la trampa de identificador MAS LIMPIA de todas: son el mismo marco, uno nombrado por las tres primeras letras y el otro por las cuatro, con LOS CINCO PASOS CORRESPONDIENDOSE UNO A UNO en el mismo orden y con los mismos nombres. Que un par tan limpio no se pueda fundir por falta de vara es exactamente el caso que hace visible el pendiente de doctrina 1. |
| **suma** | | **3 declarados** | | |

### LAS PERDIDAS NOMBRADAS, CON SU ESPECIE SEPARADA Y LA FRASE SELLADA AL LADO

**Tampoco esta tecleada: sale entera de
`python scripts/loop/vuelta56_tallar_perdidas_v55.py --vuelta 56 --lotes A,B,C`**
([`../loop/SALIDA_V56_TALLAR_PERDIDAS.txt`](../loop/SALIDA_V56_TALLAR_PERDIDAS.txt)), **que lee la
especie del propio plan sin rama por defecto**. **Son ONCE: DIEZ de condiciones y UNA de un paso**,
y se cuentan separadas a proposito, porque mezclarlas fue la caida de reporte que el acta de la
vuelta 55 nombro.

| acto | lote | el nodo que muere | **ESPECIE** | por que se perdio | la frase del plan sellado que lo dice |
|---:|:---:|---|---|---|---|
| **5** | A | `presentacion_problema_tres_columnas` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 pide validar el problema Y la reaccion inicial a la solucion EN UNA MISMA SESION DE ENTREVISTA, y la condicion 1 del superviviente solo habla de validar si el problema es real y urgente antes de mostrar el producto; el INCISO para condiciones no existe en el instrumento (pendiente de...* |
| **6** | A | `visualizacion_progreso_onboarding` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 anade que el proceso PUEDE GENERAR ANSIEDAD EN EL CLIENTE y la condicion 1 del superviviente habla de proceso tecnico, largo o con usuarios sin experiencia previa, que no es lo mismo; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra* |
| **8** | A | `tecnica_cinco_porques` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 incluye UN RESULTADO DE NEGOCIO INESPERADO junto al fallo tecnico o de proceso, y la condicion 1 del superviviente solo habla de error o falla tecnica u operativa repetible; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra* |
| **14** | A | `data_warehouse_como_fundamento` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 nombra el OBJETIVO que dispara el proyecto (querer mejorar pronostico, inventario o gestion de pedidos) y la condicion 1 del superviviente solo habla de manejar varios sistemas de informacion dispersos; el INCISO para condiciones no existe en el instrumento y por eso la perdida se no...* |
| **15** | A | `dso_dpo_gestion_capital_trabajo` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 dice PESE A VENTAS SALUDABLES, que es lo que hace del sintoma un problema de ciclo y no de demanda, y la condicion 2 del superviviente solo dice problemas de liquidez; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra* |
| **32** | B | `seis_medios_comunicacion_cliente` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 pide diversificar y personalizar la comunicacion EN CADA ETAPA DEL CICLO DE VIDA, y la condicion 1 del superviviente acota el disparador a la confirmacion de compra generica y automatizada, que es solo la bienvenida; el INCISO para condiciones no existe en el instrumento (pendiente d...* |
| **35** | C | `diseno_de_sistemas_a_escala` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 acota el disparador a que el problema involucre VARIAS ORGANIZACIONES O ENTIDADES DEL GOBIERNO, y la condicion 1 del superviviente habla de un sistema grande con distintos tipos de usuarios en conflicto, que no lo dice; el INCISO para condiciones no existe en el instrumento (pendient...* |
| **36** | C | `control_voluntario_del_pensamiento` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 dispara al ESTAR APRENDIENDO una habilidad nueva de pensamiento o creacion, y la condicion 1 del superviviente dispara al DEPENDER SOLO DE LA INSPIRACION ESPONTANEA, que es otro estado; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra* |
| **39** | C | `observar_lo_ordinario` | **DE PARAMETRO DE PASO** | el inciso MENTIRIA contra la unica restriccion del paso que protege | *PERDIDA NOMBRADA, Y NO ES DE CONDICIONES SINO DE MOMENTO DE UN PASO, que es la especie del acto 45 de la vuelta 55 y se dice para no mezclarlas: el paso 2 del que muere manda PREGUNTARSE EL PORQUE detras de objetos y comportamientos triviales MIENTRAS se observa, y el paso 2 del superviviente manda SUSPENDER EL JUIC...* |
| **41** | C | `diseno_fugitivo_runaway_design` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 2 incluye los SISTEMAS QUE APRENDEN Y SE RETROALIMENTAN junto a los datos y la IA, y la condicion 1 del superviviente enumera IA, datos personales y biotecnologia sin nombrarlos; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra* |
| **43** | C | `entrenamiento_empleados_startup` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 2 dispara al detectar que los empleados nuevos NO COMPRENDEN EL CONTEXTO COMPLETO de su trabajo, y la condicion 2 del superviviente habla de alta rotacion o baja productividad, que es otro sintoma; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra* |
| **suma** | | | **10 DE CONDICIONES, 1 DE PARAMETRO DE PASO** | | |

> **UN MATIZ DE LA COLUMNA DE LA CAUSA, declarado en vez de callado**: el tallador escribe una
> causa GENERICA para la especie de paso (*el inciso mentiria contra la unica restriccion del paso
> que protege*), que es la del acto 45 de la vuelta 55. **La del acto 39 de esta vuelta es de la
> misma familia pero no identica**: alli el inciso mentiria porque **contradiria el paso 2 del
> superviviente**, que manda suspender el juicio, y no porque el paso hable de *la unica*
> restriccion. **La razon exacta esta en la ultima columna, VERBATIM del plan sellado**, que es
> donde se lee sin tener que creerle a la etiqueta.

### LA UNICA COLISION PREVISTA DEL TRAMO, RESUELTA ANTES DE FUNDIR

**Las colisiones esperadas se midieron sobre EL ARCHIVO ENTERO y por PAR RESUELTO ANTES de tocar un
nodo** ([`../loop/SALIDA_V56_COLISIONES_ESPERADAS_TRAMO3.txt`](../loop/SALIDA_V56_COLISIONES_ESPERADAS_TRAMO3.txt)):
**100 combinaciones simuladas y UNA SOLA que fabrica colision.**

| acto | los dos puestos | que decide la relectura | consecuencia |
|---:|---|---|---|
| **15** | **203** `C` contra **813** `D` | **CONDICION DE TEXTO, y se resuelve.** El **203** es del FILO, asi que por el carril general NO se voltea por maquina: se relee en el mismo acto. **LA RELECTURA MUEVE EL 203 Y NO EL 813**, con tres razones medidas: su propia sustancia ya decia *niveles distintos, sano*; la FIGURA que lo hizo `C` (racimo de tres con `dso_dpo_gestion_capital_trabajo` de conjunto) **ya estaba medida del reves en el registro**, por el puesto **566** bajo el rotulo *hallazgo que corrige la lectura del puesto 203* y por la **seccion 14** del informe, que remidio el racimo a **CUATRO** miembros con `ciclo_de_conversion_de_efectivo` de **centro**; y la vara del banco `9.6.1` devuelve `D` en **los DOS hermanos** del racimo con la misma forma | **el 203 pasa de `C` a `D`** con correccion declarada y la razon vieja entera pegada por maquina, y **el acto SE FUNDE** |

> **Y NO ES PREGUNTA DE POLITICA, medido contra la marca operativa que esta misma vuelta registro**
> (acta de la vuelta 55, pregunta 1, adosada mas arriba en esta pagina): la razon del **203** **ni
> REMITE la decision a una instancia nombrada ni SE ABSTIENE**. Es una **RESERVA que una vara
> escrita resuelve**, o sea **MATIZ**, y el acto no queda bloqueado.

> **LA AMPLIACION DE MOVER LOS DOS NO HIZO FALTA, Y SE COMPROBO EN VEZ DE SUPONERSE:** mover UN
> solo veredicto cierra la colision, porque el 813 ya era `D`. **El censo esperado se RE-CORRIO
> despues de la correccion** y baja de UNA colision a **CERO**
> ([`../loop/SALIDA_V56_COLISIONES_ESPERADAS_TRAS_FILO.txt`](../loop/SALIDA_V56_COLISIONES_ESPERADAS_TRAS_FILO.txt)).

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 56 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 6 / 2759 | **551 / 72 / 5 / 2760** |
| grafo: vivos / deprecados / enlaces | 3432 / 421 / 17168 | **3385 / 468 / 17290** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 117 / 434 | **551 / 164 / 387** |
| actos `CERRADOS` / `ABIERTOS` | 187 / 53 | **140 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 383 / 240 | **289 / 240** |
| cola de costuras | 1482 | **1473** |
| colisiones de clase vigentes | 0 | **0**, censo propio sobre el archivo entero |
| auto-pares (los dos lados al mismo vivo) | 96 | **142** |
| duplicadas historicas: grupos / nodos | 983 / 774 | **972 / 764** |
| actos del tramo 3 fundidos / pendientes | 0 / 50 | **47 / 3, los tres DECLARADOS** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** en los tres lotes |

> **DE DONDE SALE CADA COLUMNA. LAS DOS SON CORRIDAS PROPIAS DE ESTA VUELTA**, la de apertura
> **ANTES de la primera operacion** y la de cierre **DESPUES del ultimo movimiento**, y **ninguna
> celda esta tecleada**: las extrae `python scripts/loop/vuelta56_registro_tramo.py` de las
> salidas `_APERTURA` y `_CIERRE` hermanas que cada celda cita.

> **EL MARCADOR SE MUEVE EN `C` Y EN `D`, Y NO EN `A` NI EN `B`:** la relectura del filo del acto
> 15 corrigio el puesto **203** de `C` a `D`. **Las CUARENTA Y SIETE fusiones NO movieron el
> marcador por si solas**: son de fusion pura y ninguna fabrico colision, asi que `P.16` no tuvo
> nada que limpiar. **La `A` sigue en 551 y por eso las dos tablas por dominio hermanas tampoco se
> mueven**, medido y no supuesto.

> **EL RETRATO SE MUEVE CUARENTA Y SIETE, UNO POR ACTO, Y AQUI LA CUENTA SI ES EXACTA**, a
> diferencia de la vuelta 55: esta vuelta no deshizo ninguna fusion previa, asi que **117 mas 47
> son 164**, y **551 crudas menos 164 colapsos son 387**, que es la resta exacta.

> **Y UNA CIFRA QUE NO CUADRA A LA PRIMERA Y SE EXPLICA EN VEZ DE DEJARSE PASAR:** los auto-pares
> suben de **96** a **142**, o sea **46** y no 47. **Medido**: el censo cuenta **auto-pares
> DISTINTOS**, y el del **acto 7** cae sobre uno que YA EXISTIA, el de `reglas_brainstorming`, que
> hoy recoge **CUATRO** veredictos crudos distintos resueltos al mismo nodo. **Es el mismo acto 7
> del ajeno bajo el resolutor**, y por eso la cuenta baja en uno.


---

## `OP-U-01`, TRAMO 4: EL REGISTRO DEL CIERRE (20 ago 2026, vuelta 57)

**LA VARA QUE FIJA EL TRAMO ES LA MISMA DESDE LA VUELTA 48**, escrita en la cabecera del registro
del tramo 1: *los CINCUENTA primeros actos CERRADOS de la NOMINA RE-MEDIDA AL ABRIRLO*. Aqui, por
primera vez desde el tramo 2, **LAS DOS LECTURAS CALZAN**, mismo conjunto y mismo orden, sin
ninguna divergencia que diagnosticar
([`../loop/SALIDA_V57_TRAMO4_NOMINA.txt`](../loop/SALIDA_V57_TRAMO4_NOMINA.txt)).

> **LA LECTURA B DE ESTE TRAMO YA NO ES UN BLOQUE FIJO DE LA NOMINA DE LA 48, y el motivo esta
> MEDIDO por el propio abridor:** el tramo 3 realmente abierto NO es el bloque 101 a 150, porque un
> `CERRADO` nacido despues se colo y el acto del puesto 150 quedo desplazado. Tomar el bloque 151 a
> 200 dejaria ese acto **fuera de las DOS lecturas**, y la comprobacion se volveria ciega justo
> donde la vuelta anterior encontro algo. La lectura B es **la nomina de la 48 EN SU ORDEN,
> saltando los tramos FIJADOS**.

**GUARDA DEL PREFIJO:** los vivos de los tramos 1, 2 y 3 son **19** y ocupan los puestos
**1 a 19 sin huecos**, medido y no tecleado. **El tramo 4 son los puestos 20 a
69 de hoy.** **Guarda de los CUATRO AJENOS: VERDE POR LOS DOS CAMINOS**, el literal y el del
resolutor. **Solape con los tramos anteriores: CERO.**

**LAS COLISIONES ESPERADAS DEL TRAMO ENTERO, medidas ANTES de tocar un nodo** sobre el archivo
entero y por par resuelto
([`../loop/SALIDA_V57_COLISIONES_ESPERADAS_TRAMO4.txt`](../loop/SALIDA_V57_COLISIONES_ESPERADAS_TRAMO4.txt)):
**100 combinaciones simuladas y 0 que fabriquen colision.** Ni una. **Por eso esta
vuelta NO volteo ningun veredicto y el marcador queda identico al abrir y al cerrar.**

### EL ESTADO, MEDIDO AL ABRIR Y RECOMPUTADO AL CERRAR

| | **apertura** | **cierre, RECOMPUTADO** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2760 | **551 / 72 / 5 / 2760** |
| grafo: vivos / deprecados / enlaces | 3385 / 468 / 17290 | ~~**3341 / 512 / 17369**~~ **3342 / 511 / 17366** |
| retrato: colapsos / pares distintos | 164 / 387 | ~~**208 / 343**~~ **207 / 344** |
| actos (componentes) / `CERRADOS` | 193 / 140 | ~~**149 / 96**~~ **150 / 97** |
| actos del tramo 4 fundidos / vivos | 0 / 50 | ~~**44 / 6, los 6 DECLARADOS**~~ **43 / 7, los 7 DECLARADOS** |

### EL REPARTO, TALLADO DE LOS PLANES SELLADOS

**Ninguna de estas tablas esta tecleada:** salen enteras de
`python scripts/loop/vuelta57_tallar_planes.py`
([`../loop/SALIDA_V57_TALLAR_PLANES.txt`](../loop/SALIDA_V57_TALLAR_PLANES.txt)), que las cuenta de
los `PLAN_V57_*.json` **SELLADOS** y **cae en ROJO con el acto nombrado si un motivo no encaja en
ninguna forma conocida**.

> **TABLA SUPERADA (20 ago 2026, vuelta 58).** Esta tabla es la del dia del sellado y **se queda entera porque el texto viejo no se borra**. La VIGENTE, con el acto **32** fuera, esta en la **CORRECCION DECLARADA** del final de este registro.

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **A** | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 17 | **14** | **14** | **74** | 16 | 36 | **22** | **2** |
| **B** | 18, 19, 20, 21, 22, 23, 26, 27, 28, 29, 30, 32, 33, 34 | **14** | **14** | **78** | 25 | 28 | **25** | **1** |
| **C** | 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 | **16** | **16** | **93** | 27 | 41 | **25** | **0** |
| **los tres** | | **44** | **44** | **245** | **68** | **105** | **72** | **3** |

> **TABLA SUPERADA (20 ago 2026, vuelta 58).** Esta tabla es la del dia del sellado y **se queda entera porque el texto viejo no se borra**. La VIGENTE, con el acto **32** fuera, esta en la **CORRECCION DECLARADA** del final de este registro.

| la forma, leida del motivo sellado | cuantos | los actos |
|---|---:|---|
| **UNA SOLA VARA de contenido no empatada, y BASTA** | **18** | 3, 6, 8, 10, 16, 18, 21, 23, 29, 30, 33, 35, 37, 40, 44, 46, 48, 49 |
| **TODAS LAS VARAS de contenido de acuerdo** | **15** | 2, 4, 5, 7, 9, 12, 15, 17, 19, 22, 26, 27, 34, 36, 39 |
| **LA PIEZA DECLARADA GANA A UN CONTEO de contenido** | **4** | 41, 45, 47, 50 |
| **LA PUERTA SOBREVIVE, con el choque registrado** | **2** | 20, 38 |
| **LOS CONTEOS EMPATAN y la PIEZA DECLARADA decide** | **2** | 28, 42 |
| **EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO** | **1** | 1 |
| **LA PUERTA SOBREVIVE y los conteos concuerdan, contra la razon declarada** | **1** | 43 |
| **LOS TRES CONTEOS EMPATAN y decide la pieza declarada POR CANTIDAD** | **1** | 32 |
| **suma** | **44** | |

> **TABLA SUPERADA (20 ago 2026, vuelta 58).** Esta tabla es la del dia del sellado y **se queda entera porque el texto viejo no se borra**. La VIGENTE, con el acto **32** fuera, esta en la **CORRECCION DECLARADA** del final de este registro.

| acto | lote | sobrevive | absorbe | piezas | enteras | ya dichas | `INCISO` |
|---:|:---:|---|---|---:|---:|---:|---:|
| **1** | A | `crecimiento_ingresos_verdes` | `generacion_ingresos_verdes` | 6 | 1 | 2 | 3 |
| **2** | A | `critica_del_pib_como_metrica_de_progreso` | `critica_al_pib_como_metrica` | 4 | 0 | 4 | 0 |
| **3** | A | `manejo_de_hibridos_monstruosos` | `hibridos_monstruosos` | 5 | 2 | 2 | 1 |
| **4** | A | `vision_alineacion_sostenibilidad` | `liderazgo_ceo_sostenibilidad` | 5 | 1 | 3 | 1 |
| **5** | A | `incentivos_reconocimiento_sostenibilidad` | `accountability_incentivos` | 6 | 2 | 1 | 3 |
| **6** | A | `menos_malo_vs_bueno` | `ser_menos_malo_vs_ser_bueno` | 5 | 2 | 2 | 1 |
| **7** | A | `diseno_mensaje_verde` | `mensajeria_creativa_positiva` | 4 | 1 | 0 | 3 |
| **8** | A | `unirse_organizacion_rsc_ambiental` | `unirse_grupo_lideres_climaticos` | 5 | 0 | 2 | 3 |
| **9** | A | `compra_offsets_carbono` | `neutralidad_carbono` | 5 | 1 | 2 | 2 |
| **10** | A | `eco_efectividad_2` | `eco_efectividad_re_evolucion_industrial` | 6 | 2 | 2 | 2 |
| **12** | A | `eco_eficiencia` | `eco_eficiencia_costos` | 6 | 1 | 3 | 2 |
| **15** | A | `export_administration_regulations` | `regulaciones_exportacion_ear` | 6 | 1 | 5 | 0 |
| **16** | A | `seguro_exportacion` | `seguro_de_carga_transporte` | 6 | 2 | 3 | 1 |
| **17** | A | `incoterms_reglas_comerciales_internacionales` | `terminos_de_venta_incoterms` | 5 | 0 | 5 | 0 |
| **18** | B | `certificado_de_origen_tratados_libre_comercio` | `nafta_free_trade_agreements` | 6 | 0 | 2 | 4 |
| **19** | B | `uso_intermediarios_exportacion` | `intermediarios_exportacion` | 5 | 1 | 1 | 3 |
| **20** | B | `seleccion_canales_distribucion` | `seleccion_canales_exportacion` | 6 | 3 | 1 | 2 |
| **21** | B | `ecosistema_global_emprendimiento_gee` | `recursos_apoyo_pymes_sba` | 6 | 2 | 4 | 0 |
| **22** | B | `letra_de_cambio_bill_of_exchange` | `documentary_collections` | 6 | 3 | 3 | 0 |
| **23** | B | `seleccion_de_metodo_de_pago` | `prevencion_problemas_de_pago` | 6 | 2 | 1 | 3 |
| **26** | B | `uso_del_us_commercial_service` | `consejos_distrito_exportacion_dec` | 4 | 0 | 2 | 2 |
| **27** | B | `preparar_fdd` | `elaboracion_fdd` | 5 | 3 | 1 | 1 |
| **28** | B | `franquicia_mas_crecimiento_corporativo_hibrido` | `estrategia_multicanal_expansion` | 6 | 2 | 3 | 1 |
| **29** | B | `proceso_llamada_inicial_venta` | `proceso_primera_llamada` | 8 | 1 | 5 | 2 |
| **30** | B | `sitio_web_franquicia` | `sitio_web_captura_leads` | 4 | 2 | 0 | 2 |
| **32** | B | `referidos_franquiciados_existentes` | `programa_de_referidos_de_franquiciados` | 7 | 2 | 3 | 2 |
| **33** | B | `motivated_management_franquiciado` | `mito_control_calidad_corporativo` | 5 | 3 | 1 | 1 |
| **34** | B | `desarrollar_manual_operaciones` | `confidencialidad_manual_operaciones` | 4 | 1 | 1 | 2 |
| **35** | C | `ferias_comerciales_franquicia` | `marketing_en_ferias_comerciales_de_franquicias` | 7 | 2 | 1 | 4 |
| **36** | C | `mix_ubicaciones_corporativas_franquicia` | `combinar_crecimiento_corporativo_y_franquicia` | 6 | 1 | 1 | 4 |
| **37** | C | `rutas_salida_planificacion_emergencias` | `rutas_de_salida_y_puertas_de_emergencia` | 7 | 2 | 3 | 2 |
| **38** | C | `responsabilidad_prospectiva` | `rendicion_cuentas_prospectiva` | 6 | 4 | 2 | 0 |
| **39** | C | `capacitacion_educacion_seguridad` | `capacitacion_conciencia_programa` | 6 | 1 | 4 | 1 |
| **40** | C | `confusion_de_modos_automatizacion` | `confusion_modos_automatizacion` | 5 | 0 | 3 | 2 |
| **41** | C | `clasificacion_sistemas_por_nivel_seguridad` | `niveles_de_madurez_de_seguridad` | 6 | 2 | 3 | 1 |
| **42** | C | `accident_proneness_fallacy` | `declive_teoria_manzana_podrida` | 5 | 1 | 2 | 2 |
| **43** | C | `cultura_justa` | `cultura_justa_organizacional` | 6 | 2 | 3 | 1 |
| **44** | C | `vulnerabilidad_instalacion` | `omisiones_en_mantenimiento` | 5 | 0 | 2 | 3 |
| **45** | C | `clasificacion_riesgos_por_dominio` | `areas_riesgo_primario` | 7 | 2 | 5 | 0 |
| **46** | C | `evitar_perdida_situacion_awareness` | `critica_perdida_de_conciencia_situacional` | 6 | 1 | 5 | 0 |
| **47** | C | `sesgo_retrospectivo_hindsight_2` | `sesgo_retrospectivo_hindsight` | 5 | 3 | 1 | 1 |
| **48** | C | `limite_busqueda_causas_pendulo` | `reglas_parada_investigacion_accidentes` | 5 | 2 | 3 | 0 |
| **49** | C | `condiciones_latentes_largo_plazo` | `caso_descarrilamiento_nakina` | 4 | 2 | 1 | 1 |
| **50** | C | `cultura_de_aprendizaje` | `ingenieria_cultura_aprendizaje` | 7 | 2 | 2 | 3 |

> **TABLA SUPERADA (20 ago 2026, vuelta 58).** Esta tabla es la del dia del sellado y **se queda entera porque el texto viejo no se borra**. La VIGENTE, con el acto **32** fuera, esta en la **CORRECCION DECLARADA** del final de este registro.

| acto | lote | sus miembros | especie | se acumula para |
|---:|:---:|---|---|---|
| **11** | A | `disruptores_endocrinos_y_salud_industrial`, `quimicos_toxicos_en_diseno` | **EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN** | LA MESA. Y con un dato que la propia razon aporta y que conviene que la mesa tenga delante: la pieza de disruptores_endocrinos_y_salud_industrial que la razon llama LA UNICA REGLA PRECAUTORIA DEL CATALOGO (no basta con quitar lo que se sabe malo, hay que desconfiar de lo que nadie ha mirado) no tiene equivalente en ningun otro nodo del par. Un empate de conteos que pone en riesgo una regla unica del catalogo es el caso que hace visible el pendiente de doctrina 1 desde otro angulo que el del acto 45 de la vuelta 56. |
| **13** | A | `desperdicio_es_alimento`, `metabolismo_biologico_y_tecnico` | **CONTEOS QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA** | LA MESA. Con un dato de familia: los dos nodos son el eje del que cuelga media seccion del libro (el paso 5 de metabolismo_biologico_y_tecnico nombra el upcycling sobre el downcycling y el paso 6 de desperdicio_es_alimento cambia el MODELO DE NEGOCIO en vez del producto), y ninguno de los dos es la madre del otro. Es el segundo ejemplar de conteos que chocan sin pieza que desempate, y el primero fuera del dominio core. |
| **14** | A | `carta_de_credito_letter_of_credit`, `letters_of_credit` | **CONTEOS QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA** | LA MESA. Y con una observacion medida que la mesa deberia tener delante porque no es de conteo: los dos nodos cubren ETAPAS DISTINTAS del mismo tramite, uno la negociacion previa a que la carta exista y el otro la revision de la carta ya recibida, y la razon lo dice con esas palabras. Es el PRIMER PAR DEL DOMINIO DE EXPORTACION que entra a la mesa, y entra por la misma puerta por la que entro el ambiental. |
| **24** | B | `barreras_comerciales_no_arancelarias`, `cumplimiento_acuerdos_comerciales_tanc` | **EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN** | LA MESA. Y con el dato que la propia razon subraya y que hace este empate distinto de los demas: LAS DOS PIEZAS PROPIAS SON LAS DOS RESPUESTAS OPUESTAS AL MISMO PROBLEMA. Un nodo termina CEDIENDO ante la barrera (ajustar el producto) y el otro INSISTIENDO (dar seguimiento hasta que se resuelva), y la razon escribe que la fusion tiene que conservar las dos porque son las dos salidas legitimas. Un empate cuyas dos mitades son opuestas no se rompe eligiendo la mas larga, y por eso este ejemplar merece llegar a la mesa con esa frase delante. |
| **25** | B | `licenciamiento_tecnologico`, `proteccion_propiedad_intelectual_internacional` | **LOS DOS MIEMBROS SON PUERTA: NO HAY ABSORBIDO POSIBLE** | LA MESA, Y CON UNA PREGUNTA QUE NO ES DE PAR SINO DE CATALOGO: que se hace con un acto CERRADO cuyos DOS miembros son puertas. La vara del acta 54 pregunta 1 esta escrita para el acto con UNA puerta y no dice nada de este caso. Hay al menos dos salidas imaginables y ninguna esta escrita, asi que NO se elige aqui: fundir moviendo antes el puente o la semilla al superviviente, o dejar el par como enlace permanente. Va marcado como PENDIENTE DE DOCTRINA en el reporte, con el aviso de que el tramo 4 lo destapa pero no lo inventa: la figura estaba esperando desde que existen las puertas. |
| **31** | B | `comprender_definicion_legal_franquicia`, `marco_name_system_fee` | **CONTEOS QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA** | LA MESA. Con un dato que la razon aporta y que a la mesa le sirve para no leer este empate como los otros: la unica diferencia real entre los dos nodos ES EL MODO, uno pregunta si YA se es franquicia y el otro si se QUIERE serlo, y la razon deja escrito que la clase se decide leyendo los pasos y no el modo. Es el TERCER ejemplar de conteos que chocan de este tramo, y el primero en el que lo que chocan son cuatro contra cinco pasos y tres contra dos condiciones sobre un test de tres elementos identico. |
| **suma** | | **6 declarados** | | |

### LAS PERDIDAS NOMBRADAS

**Talladas de los planes sellados** con
`python scripts/loop/vuelta56_tallar_perdidas_v55.py --vuelta 57 --lotes A,B,C`
([`../loop/SALIDA_V57_TALLAR_PERDIDAS.txt`](../loop/SALIDA_V57_TALLAR_PERDIDAS.txt)), que **lee la
especie del propio plan y no tiene rama por defecto**. Son **3, LAS TRES DE CONDICIONES**, y
las tres por la misma causa heredada: **el `INCISO` de condiciones no existe en el instrumento**.

| acto | lote | el nodo que muere | **ESPECIE** | por que se perdio | la frase del plan sellado que lo dice |
|---:|:---:|---|---|---|---|
| **12** | A | `eco_eficiencia_costos` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 acota el disparador a UN CONTEXTO DE RECESION ECONOMICA y la condicion 1 del superviviente solo dice buscar reducir costos operativos; el INCISO para condiciones no existe en el instrumento (pendiente de doctrina heredado) y por eso la perdida se nombra en vez de repararse* |
| **16** | A | `seguro_de_carga_transporte` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 dispara ante CUALQUIER envio internacional que necesite definir cobertura de riesgos de transporte, y la condicion 1 del superviviente acota a MERCANCIA DE ALTO VALOR; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra* |
| **23** | B | `prevencion_problemas_de_pago` | **DE CONDICIONES** | el `INCISO` de condiciones no existe en el instrumento | *PERDIDA NOMBRADA: su condicion 1 dispara con compradores nuevos O RECURRENTES, y la condicion 2 del superviviente solo habla del comprador DESCONOCIDO O CON POCO HISTORIAL; el recurrente que ya tiene historial se queda fuera* |
| **suma** | | | **3 DE CONDICIONES** | | |

> **UNA CIFRA QUE CONVIENE DEJAR DICHA PORQUE ES LA QUE MIDE EL REPARTO:** de las **245**
> piezas repartidas en los tres lotes, **3** se pierden. El resto viaja entera, esta ya dicha
> en el superviviente, o se salva de `INCISO` adosado.


---

### CORRECCION DECLARADA: **EL ACTO 32 SE DESHACE Y QUEDA DECLARADO, SEPTIMO DEL TRAMO** (20 ago 2026, vuelta 58, TAREA 1.1 del encargo)

**LA RELECTURA CONJUNTA QUE EL ACTA 57 ENCARGO SE RESOLVIO A FAVOR DEL CASO DEL AUDITOR**
(su seccion 2 y su discutible `D4`), **y se verifico contra el grafo ANTES de tocar nada**, que es
lo que el encargo pedia. **Instrumento de solo lectura**
`python scripts/loop/vuelta58_relectura_acto32.py --raiz <worktree en 75863aee>`
([`../loop/SALIDA_V58_RELECTURA_ACTO32_PREFUSION.txt`](../loop/SALIDA_V58_RELECTURA_ACTO32_PREFUSION.txt)),
con la aritmetica de varas copiada entera del cuadro de varas y medida sobre el arbol **PRE
FUSION**: `programa_de_referidos_de_franquiciados` contra `referidos_franquiciados_existentes` da
**pasos 5 contra 5, condiciones 2 contra 2 y cableado 3 contra 3**, y la forma que la receta le da
es **EMPATE SIN VARA**.

**LA LETRA VIGENTE, LEIDA HOY Y CON SU LINEA AL LADO:** el acta 53, pregunta 4 (linea **13015** de
`../loop/ACTA_AUDITOR.md`) *reserva el empate sin vara para cuando TODO empata*; el acta 54,
pregunta 4 (linea **13389**) dice que *el conteo de caracteres no desempata*, y su linea **13391**
que *el propio declarado de UN SOLO LADO es una vara no empatada*. **En este acto el propio
declarado esta A LOS DOS LADOS**: la razon del puesto **2127**, leida hoy entera, mide **UNA
LINEA** propia de uno y **DOS LINEAS** propias del otro. **Contar esas lineas es un conteo sobre la
letra, y ninguna acta lo ha adjudicado como vara.** La razon del 2127 **no declara superviviente,
ni contencion, ni padre**: pesa una pieza como *la que mas cuesta reponer*, que no es ninguna de
las tres formas que el acta 53, pregunta 3, enumera.

> **EL CONTRASTE INTERNO, MEDIDO EN LA MISMA SALIDA Y NO CITADO DE MEMORIA:** el **acto 11** de
> este mismo tramo da **4 contra 4, 2 contra 2 y 2 contra 2**, tambien **EMPATE SIN VARA**, y su
> razon (puesto **1884**) declara material propio **UNA linea contra TRES**. **La vuelta 57 lo
> DECLARO.** Dos actos con la misma forma y el mismo tipo de desempate no pueden acabar uno fundido
> y otro declarado, y esa inconsistencia es la que esta correccion cierra.

**NINGUNA EVIDENCIA NUEVA CONTRA EL CASO**, asi que no hubo que parar antes de tocar el grafo.
**LA RAMA DE LA CANTIDAD COMO VARA NO SE APLICA MAS** mientras la mesa no la adopte: queda dentro
del **pendiente de doctrina 1**, tal como el acta 57 (pregunta 2) la dejo.

**EL DESHACER, Y LO QUE OBLIGO A HACERLO DISTINTO DEL ACTO 23 DE LA VUELTA 55.**
`python scripts/loop/vuelta58_deshacer_acto32.py --ejecutar`
([`../loop/SALIDA_V58_DESHACER_ACTO32.txt`](../loop/SALIDA_V58_DESHACER_ACTO32.txt)). De los
**CINCO** ficheros que el acto 32 toco en el lote B (`a1d7269d`), **CUATRO** no se habian vuelto a
tocar y se restauran al blob del lote A (`0481113f`); **el quinto,
`principio_apalancamiento_numero_magico.json`, SI se toco despues**, en el lote C (`706397c7`) y
**por OTRO acto, el 35**. **Restaurarle el blob habria borrado el acto 35**, asi que ese fichero
recibe el **DIFF INVERSO** del acto 32, probado con `--check` antes de aplicarse. **El acto 35
queda en pie, verificado por conteo.** Las guardas de despues: **los dos miembros VIVOS, sin alias
cruzado y CAMPO A CAMPO IDENTICOS al blob pre fusion**, y **el cableado de vuelta al absorbido en
los tres vecinos**.

#### EL ESTADO DEL TRAMO 4, RECOMPUTADO TRAS DESHACER EL ACTO 32

**Ninguna celda esta tecleada:** las extrae `python scripts/loop/vuelta58_registro_acto32.py` de
[`../loop/SALIDA_V58_ESTADO_TRAS_ACTO32.txt`](../loop/SALIDA_V58_ESTADO_TRAS_ACTO32.txt),
[`../loop/SALIDA_V58_RECOMPUTO_TRAS_ACTO32.txt`](../loop/SALIDA_V58_RECOMPUTO_TRAS_ACTO32.txt) y
[`../loop/SALIDA_V58_CENSO_TRAS_ACTO32.txt`](../loop/SALIDA_V58_CENSO_TRAS_ACTO32.txt).

| | **cierre de la vuelta 57** | **tras deshacer el acto 32** |
|---|---:|---:|
| grafo: vivos / deprecados / enlaces | 3341 / 512 / 17369 | **3342 / 511 / 17366** |
| retrato: colapsos / pares distintos | 208 / 343 | **207 / 344** |
| actos (componentes) / `CERRADOS` | 149 / 96 | **150 / 97** |
| auto-pares / colisiones de clase vigentes | 186 / 0 | **185 / 0** |
| actos del tramo 4 fundidos / vivos | 44 / 6 | **43 / 7, los 7 DECLARADOS** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (441 igual a 441; 343 igual a 343) | **TODAS OK (443 igual a 443; 344 igual a 344)** |

> **CADA CELDA QUE SE MOVIO LO HIZO EN UNO, Y ESO ERA LO QUE EL ENCARGO PREDECIA:** los colapsos
> bajan uno, los pares distintos suben uno, los actos suben uno, los `CERRADOS` suben uno, los
> auto-pares bajan uno, los vivos suben uno y los deprecados bajan uno. **Los enlaces bajan TRES y
> el motivo esta medido, no supuesto:** el conteo incluye los deprecados, la fusion habia sumado
> **tres** `nodos_previos` al superviviente, y esos tres son los que se van. **El marcador NO se
> mueve y tampoco es un olvido**: deshacer una fusion pura no voltea ningun veredicto, y el censo
> de colisiones sale en **0** con `CALZA: SI`.

#### LAS TABLAS VIGENTES, TALLADAS DE LOS PLANES SELLADOS CON EL 32 RETIRADO

**Salen enteras de** `python scripts/loop/vuelta58_tallar_planes.py --vuelta 58 --retirado "32|..."`
([`../loop/SALIDA_V58_TALLAR_PLANES.txt`](../loop/SALIDA_V58_TALLAR_PLANES.txt)), **sucesor
declarado del tallador de la vuelta 57 copiado byte a byte**, cuyo unico anadido es el argumento
`--retirado`. **EL PLAN SELLADO NO SE TOCA:** los `PLAN_V57_*.json` se quedan con el acto 32 dentro
y su motivo entero, porque reescribir un plan sellado taparia lo que se corrige. **Corrido sin
`--retirado`, este sucesor imprime lo mismo que su ancestro al digito, y se comprobo.**

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **A** | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 17 | **14** | **14** | **74** | 16 | 36 | **22** | **2** |
| **B** | 18, 19, 20, 21, 22, 23, 26, 27, 28, 29, 30, 33, 34 | **13** | **13** | **71** | 23 | 25 | **23** | **1** |
| **C** | 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 | **16** | **16** | **93** | 27 | 41 | **25** | **0** |
| **los tres** | | **43** | **43** | **238** | **66** | **102** | **70** | **3** |

| la forma, leida del motivo sellado | cuantos | los actos |
|---|---:|---|
| **UNA SOLA VARA de contenido no empatada, y BASTA** | **18** | 3, 6, 8, 10, 16, 18, 21, 23, 29, 30, 33, 35, 37, 40, 44, 46, 48, 49 |
| **TODAS LAS VARAS de contenido de acuerdo** | **15** | 2, 4, 5, 7, 9, 12, 15, 17, 19, 22, 26, 27, 34, 36, 39 |
| **LA PIEZA DECLARADA GANA A UN CONTEO de contenido** | **4** | 41, 45, 47, 50 |
| **LA PUERTA SOBREVIVE, con el choque registrado** | **2** | 20, 38 |
| **LOS CONTEOS EMPATAN y la PIEZA DECLARADA decide** | **2** | 28, 42 |
| **EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO** | **1** | 1 |
| **LA PUERTA SOBREVIVE y los conteos concuerdan, contra la razon declarada** | **1** | 43 |
| **suma** | **43** | |

| acto | lote | sus miembros | especie | se acumula para |
|---:|:---:|---|---|---|
| **11** | A | `disruptores_endocrinos_y_salud_industrial`, `quimicos_toxicos_en_diseno` | **EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN** | LA MESA. Y con un dato que la propia razon aporta y que conviene que la mesa tenga delante: la pieza de disruptores_endocrinos_y_salud_industrial que la razon llama LA UNICA REGLA PRECAUTORIA DEL CATALOGO (no basta con quitar lo que se sabe malo, hay que desconfiar de lo que nadie ha mirado) no tiene equivalente en ningun otro nodo del par. Un empate de conteos que pone en riesgo una regla unica del catalogo es el caso que hace visible el pendiente de doctrina 1 desde otro angulo que el del acto 45 de la vuelta 56. |
| **13** | A | `desperdicio_es_alimento`, `metabolismo_biologico_y_tecnico` | **CONTEOS QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA** | LA MESA. Con un dato de familia: los dos nodos son el eje del que cuelga media seccion del libro (el paso 5 de metabolismo_biologico_y_tecnico nombra el upcycling sobre el downcycling y el paso 6 de desperdicio_es_alimento cambia el MODELO DE NEGOCIO en vez del producto), y ninguno de los dos es la madre del otro. Es el segundo ejemplar de conteos que chocan sin pieza que desempate, y el primero fuera del dominio core. |
| **14** | A | `carta_de_credito_letter_of_credit`, `letters_of_credit` | **CONTEOS QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA** | LA MESA. Y con una observacion medida que la mesa deberia tener delante porque no es de conteo: los dos nodos cubren ETAPAS DISTINTAS del mismo tramite, uno la negociacion previa a que la carta exista y el otro la revision de la carta ya recibida, y la razon lo dice con esas palabras. Es el PRIMER PAR DEL DOMINIO DE EXPORTACION que entra a la mesa, y entra por la misma puerta por la que entro el ambiental. |
| **24** | B | `barreras_comerciales_no_arancelarias`, `cumplimiento_acuerdos_comerciales_tanc` | **EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN** | LA MESA. Y con el dato que la propia razon subraya y que hace este empate distinto de los demas: LAS DOS PIEZAS PROPIAS SON LAS DOS RESPUESTAS OPUESTAS AL MISMO PROBLEMA. Un nodo termina CEDIENDO ante la barrera (ajustar el producto) y el otro INSISTIENDO (dar seguimiento hasta que se resuelva), y la razon escribe que la fusion tiene que conservar las dos porque son las dos salidas legitimas. Un empate cuyas dos mitades son opuestas no se rompe eligiendo la mas larga, y por eso este ejemplar merece llegar a la mesa con esa frase delante. |
| **25** | B | `licenciamiento_tecnologico`, `proteccion_propiedad_intelectual_internacional` | **LOS DOS MIEMBROS SON PUERTA: NO HAY ABSORBIDO POSIBLE** | LA MESA, Y CON UNA PREGUNTA QUE NO ES DE PAR SINO DE CATALOGO: que se hace con un acto CERRADO cuyos DOS miembros son puertas. La vara del acta 54 pregunta 1 esta escrita para el acto con UNA puerta y no dice nada de este caso. Hay al menos dos salidas imaginables y ninguna esta escrita, asi que NO se elige aqui: fundir moviendo antes el puente o la semilla al superviviente, o dejar el par como enlace permanente. Va marcado como PENDIENTE DE DOCTRINA en el reporte, con el aviso de que el tramo 4 lo destapa pero no lo inventa: la figura estaba esperando desde que existen las puertas. |
| **31** | B | `comprender_definicion_legal_franquicia`, `marco_name_system_fee` | **CONTEOS QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA** | LA MESA. Con un dato que la razon aporta y que a la mesa le sirve para no leer este empate como los otros: la unica diferencia real entre los dos nodos ES EL MODO, uno pregunta si YA se es franquicia y el otro si se QUIERE serlo, y la razon deja escrito que la clase se decide leyendo los pasos y no el modo. Es el TERCER ejemplar de conteos que chocan de este tramo, y el primero en el que lo que chocan son cuatro contra cinco pasos y tres contra dos condiciones sobre un test de tres elementos identico. |
| **32** | B | `programa_de_referidos_de_franquiciados`, `referidos_franquiciados_existentes` | **EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN** | LA MESA, dentro del pendiente de doctrina 1. RETIRADO EN LA VUELTA 58 por la relectura conjunta que el acta 57 encargo (discutible D4): la fusion de la vuelta 57 rompio el empate triple con la CANTIDAD de lineas propias declaradas, una contra dos, y eso es un conteo sobre la letra que ninguna acta adjudica como vara. Por acta 53 pregunta 4 el empate sin vara es cuando TODO empata, y aqui empatan pasos 5 contra 5, condiciones 2 contra 2 y cableado 3 contra 3; por acta 54 pregunta 4 el propio declarado solo es vara no empatada DE UN SOLO LADO, y aqui esta a los dos. La rama de la CANTIDAD como vara queda ABIERTA PARA LA MESA y NO se aplica mientras tanto. |
| **suma** | | **7 declarados** | | |

| acto | lote | la forma que el motivo SELLADO le dio | donde queda ahora |
|---:|:---:|---|---|
| **32** | B | LOS TRES CONTEOS EMPATAN y decide la pieza declarada POR CANTIDAD | **EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN** |

---

### LA ADJUDICACION DEL ACTA 57 SOBRE EL **ACTO 25**: **EL CARRIL YA ESTABA ESCRITO** (20 ago 2026, vuelta 58, TAREA 1.4 del encargo)

**El registro del tramo 4 dejo el acto 25 con la pregunta abierta** (*que se hace con un acto
`CERRADO` cuyos DOS miembros son puertas*). **El acta 57 la contesta en su pregunta 3 y SIN
DOCTRINA NUEVA, y se anota aqui con fecha porque es este registro el que la pedia:**

> **DECLARARLO FUE CORRECTO, y el carril es el IMPOSIBLE POR PUERTA.** La vara del acta 51,
> pregunta 3, define el imposible por puerta como **el acto donde NINGUNA fusion respeta la
> guarda**; el acta 54, pregunta 1, la cita; y el acta 54, pregunta 2, **lo lista con todas sus
> letras en el carril de DECLARAR Y ACUMULAR**. **Con las DOS puertas, ninguna direccion respeta la
> guarda `1B`: se declara, se acumula, el bucle sigue.** **No hacia falta doctrina nueva para
> declararlo y no se escribio ninguna.**

**LO QUE SI QUEDA PARA LA MESA ES LA SALIDA DE FONDO, Y SOLO ESA:** mover el puente o la semilla al
superviviente, o dejar el par como enlace permanente. **Eso es politica de catalogo y la casa lo
reserva**, en el **pendiente de doctrina 5**. **El acto 25 no vuelve a la cola de fusion mientras
tanto**, y sigue en la tabla de declarados de arriba con su especie escrita.
