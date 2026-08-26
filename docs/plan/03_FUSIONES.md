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

> **RATIFICADA POR CORRIDA PROPIA DEL AUDITOR (20 ago 2026, vuelta 59, TAREA 1.2 del encargo).** El acta 58 **re-derivo el cuadro de varas del tramo con codigo propio y las 50 filas calzan al digito, `DISTINTAS 0`** (`../loop/ACTA_AUDITOR.md` linea **14735**, leida hoy), y **re-midio este acto 32 sobre los ficheros de hoy: pasos 5 contra 5, condiciones 2 contra 2, cableado 3 contra 3, `EMPATE SIN VARA`** (linea **14743**). **Nada de lo sellado se reescribe: la correccion de arriba queda como esta y esta linea solo dice que un segundo instrumento la midio y la sostiene.**

> **CORRECCION DECLARADA DE LA FECHA DE ESTA MISMA LINEA (20 ago 2026, vuelta 60, TAREA 1.1 del encargo; hallazgo del acta 59).** La linea de arriba decia **~~21 ago 2026~~** y la fecha buena es **20 ago 2026**. **EL TEXTO VIEJO NO SE BORRA: queda citado aqui**, que es lo que la regla 8 del `EJECUTOR.md` pide. **EL MOTIVO ESTA MEDIDO, NO SUPUESTO:** los **6 commits** de la vuelta 59 (`c9927b19`, `fd7de724`, `956f9e3d`, `39d495b2`, `6b6607bb`, `02d0bf00`) llevan **todos** fecha **2026-08-20** por `git log --date=format:'%Y-%m-%d'`, y el commit que escribio esta misma linea es **`956f9e3d`, de 2026-08-20 13:48:45**. **LA FECHA DE LA VUELTA SE SUPUSO EN VEZ DE MEDIRSE**, y de aqui en adelante **la fecha de todo reporte y de toda nota fechada SE MIDE** (del reloj del sistema o del commit) **y no se supone**. **EL CAMPO `fecha` DEL PLAN SELLADO DEL LOTE A (`docs/loop/PLAN_V59_OPU01_LOTE_A.json`) NO SE REEDITA:** su error queda declarado en el registro de este tramo cuando el tramo cierre.

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


---

## `OP-U-01`, TRAMO 5: EL REGISTRO DEL CIERRE (20 ago 2026, vuelta 60)

**LA VARA QUE FIJA EL TRAMO ES LA MISMA DESDE LA VUELTA 48**, escrita en la cabecera del registro
del tramo 1: *los CINCUENTA primeros actos CERRADOS de la NOMINA RE-MEDIDA AL ABRIRLO*. **EL INSUMO
DE ESTE TRAMO SE MIDIO Y SE FIJO AL ABRIRLO Y NO SE RE-MIDIO NI UNA VEZ DESPUES**, que es lo que el
encargo mandaba
([`../loop/SALIDA_V58_TRAMO5_NOMINA.txt`](../loop/SALIDA_V58_TRAMO5_NOMINA.txt)).

**GUARDA DEL PREFIJO:** los vivos de los tramos anteriores son **26** y ocupan sus puestos
sin huecos, medido y no tecleado. **El tramo 5 son los puestos 27 a 76 de
hoy.** **Solape con los tramos anteriores: CERO.**

> **EL COTEJO QUE ESTE TRAMO ESTRENA, y nace de que el tramo se repartio entre DOS vueltas:** entre
> la foto fijada del insumo y la ejecucion de los lotes B y C hubo una fusion de por medio (la del
> lote A), y una fusion CAMBIA los pasos del superviviente. Antes de escribir una linea del plan del
> lote B se corrio `scripts/loop/vuelta60_cotejo_insumo.py`, que NO re-mide el insumo sino que lo
> COTEJA contra los nodos de hoy: **50 actos mirados, 34 vivos, 16 ya fundidos, DESCALCES 0**
> ([`../loop/SALIDA_V60_COTEJO_INSUMO.txt`](../loop/SALIDA_V60_COTEJO_INSUMO.txt)).

**LAS COLISIONES ESPERADAS DEL TRAMO ENTERO, medidas ANTES de tocar un nodo** sobre el archivo
entero y por par resuelto
([`../loop/SALIDA_V58_COLISIONES_ESPERADAS_TRAMO5.txt`](../loop/SALIDA_V58_COLISIONES_ESPERADAS_TRAMO5.txt)):
**100 combinaciones simuladas y 0 que fabriquen colision.** Ni una. **Por eso este
tramo NO volteo ningun veredicto y el marcador queda identico al abrir y al cerrar.**

### EL ESTADO, MEDIDO AL ABRIR LA VUELTA QUE CIERRA EL TRAMO Y RECOMPUTADO AL CERRARLA

| | **apertura de la vuelta 60** | **cierre, RECOMPUTADO** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| grafo: vivos / deprecados / enlaces | 3.326 / 527 / 17.396 | **3.295 / 558 / 17.449** |
| retrato: colapsos / pares distintos | 223 / 328 | **254 / 297** |
| actos (componentes) / `CERRADOS` | 134 / 81 | **103 / 50** |
| actos del tramo 5 fundidos / vivos | 0 / 50 | **47 / 3, los 3 DECLARADOS** |

> **LA COLUMNA DE APERTURA ES LA DE LA VUELTA QUE CIERRA EL TRAMO, no la de la que lo abrio, y se
> dice para que nadie lea de ahi el efecto del tramo entero.** El lote A ya estaba fundido cuando se
> tomo. El efecto del TRAMO COMPLETO se lee de los `47` actos fundidos de la ultima fila, que
> es la cifra que si cubre las dos vueltas.

### EL REPARTO, TALLADO DE LOS PLANES SELLADOS DE LAS DOS VUELTAS

**Ninguna de estas tablas esta tecleada:** salen enteras de
`python scripts/loop/tallar_planes_del_tramo.py --vuelta 60 --prefijo PLAN_V59_OPU01_LOTE_ --prefijo PLAN_V60_OPU01_LOTE_`
([`../loop/SALIDA_V60_TALLAR_PLANES.txt`](../loop/SALIDA_V60_TALLAR_PLANES.txt)), que las cuenta de los planes **SELLADOS** y **cae en ROJO
con el acto nombrado si un motivo no encaja en ninguna forma conocida**. **`--prefijo` se hizo
REPETIBLE en esta vuelta justamente para esto**: con un prefijo unico, el registro habria publicado
**31 fusiones donde hay 47**, y las cuatro tablas habrian mentido por omision.

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **A** | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17 | **16** | **16** | **97** | 24 | 59 | **14** | **3** |
| **B** | 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33 | **15** | **15** | **90** | 30 | 55 | **5** | **1** |
| **C** | 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 | **16** | **16** | **101** | 24 | 70 | **7** | **0** |
| **los tres** | | **47** | **47** | **288** | **78** | **184** | **26** | **4** |

| la forma, leida del motivo sellado | cuantos | los actos |
|---|---:|---|
| **UNA SOLA VARA de contenido no empatada, y BASTA** | **18** | 4, 6, 9, 16, 21, 22, 23, 24, 25, 26, 27, 28, 30, 36, 37, 44, 45, 46 |
| **TODAS LAS VARAS de contenido de acuerdo** | **10** | 8, 12, 14, 17, 18, 19, 31, 39, 48, 50 |
| **EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO** | **6** | 2, 5, 10, 15, 20, 38 |
| **CONTEOS QUE CHOCAN CON LA PIEZA DECLARADA, y decide la declarada** | **4** | 11, 35, 42, 47 |
| **LA PIEZA DECLARADA GANA A UN CONTEO de contenido** | **2** | 7, 33 |
| **LA PUERTA SOBREVIVE, con el choque registrado** | **2** | 1, 43 |
| **LOS TRES CONTEOS EMPATAN y decide LA PIEZA DECLARADA, que esta de UN SOLO LADO** | **2** | 32, 40 |
| **EL CONTENIDO EMPATA y LA PIEZA DECLARADA Y EL CABLEADO COINCIDEN** | **1** | 49 |
| **LA PIEZA DECLARADA GANA A LOS DOS CONTEOS de contenido** | **1** | 3 |
| **UNA FIGURA CON NOMBRE del informe vence al conteo (EL CASO NO ES LA CASA)** | **1** | 41 |
| **suma** | **47** | |

| acto | lote | sobrevive | absorbe | piezas | enteras | ya dichas | `INCISO` |
|---:|:---:|---|---|---:|---:|---:|---:|
| **1** | A | `programa_mejora_calidad_14_pasos` | `programa_de_mejora_de_calidad` | 9 | 2 | 6 | 1 |
| **2** | A | `sostener_las_ganancias` | `mantener_las_ganancias` | 7 | 1 | 5 | 1 |
| **3** | A | `innovacion_tipo_ii` | `tipos_innovacion_i_ii` | 9 | 1 | 8 | 0 |
| **4** | A | `funcion_perdida_limites_especificacion` | `funcion_perdida_taguchi` | 6 | 0 | 4 | 2 |
| **5** | A | `enfermedades_mortales_gestion` | `las_siete_enfermedades_mortales` | 6 | 2 | 2 | 2 |
| **6** | A | `eliminar_trabajo_a_destajo` | `eliminacion_pago_destajo` | 5 | 1 | 4 | 0 |
| **7** | A | `adaptaciones_sectoriales_iso` | `estandares_especificos_industria` | 6 | 1 | 4 | 1 |
| **8** | A | `estilo_gerencial_ballet_vs_hockey` | `estilo_gerencial_hockey_vs_ballet` | 6 | 3 | 3 | 0 |
| **9** | A | `roi_proyectos_calidad` | `roi_breakthrough` | 6 | 4 | 2 | 0 |
| **10** | A | `teoria_triple_rol_sistemas_abiertos` | `pensamiento_sistemico_rol_triple` | 6 | 1 | 3 | 2 |
| **11** | A | `descubrir_necesidades_del_cliente` | `descubrir_necesidades_cliente` | 5 | 1 | 2 | 2 |
| **12** | A | `qfd_matriz` | `spreadsheet_diseno_para_la_calidad` | 5 | 0 | 4 | 1 |
| **14** | A | `reinicio_programa_calidad` | `repeticion_programa` | 4 | 0 | 4 | 0 |
| **15** | A | `eliminar_slogans_y_exhortaciones` | `eliminar_slogans_metas` | 6 | 2 | 3 | 1 |
| **16** | A | `rol_black_belt_six_sigma` | `rol_black_belt` | 5 | 3 | 2 | 0 |
| **17** | A | `mapeo_flujo_valor` | `value_stream_mapping` | 6 | 2 | 3 | 1 |
| **18** | B | `cero_defectos` | `filosofia_zero_defectos` | 6 | 2 | 4 | 0 |
| **19** | B | `equipo_mejora_calidad_2` | `equipo_mejora_calidad` | 5 | 1 | 4 | 0 |
| **20** | B | `rol_facilitador_equipos_mejora` | `rol_facilitador_black_belt` | 6 | 3 | 2 | 1 |
| **21** | B | `indice_cpk` | `interpretacion_cpk` | 6 | 4 | 2 | 0 |
| **22** | B | `remover_barreras_orgullo_trabajo` | `barreras_orgullo_trabajo` | 5 | 2 | 3 | 0 |
| **23** | B | `histograma` | `histogramas_distribucion_frecuencias` | 7 | 2 | 5 | 0 |
| **24** | B | `eliminacion_planes_muestreo_estandar` | `criticas_muestreo_aceptacion` | 5 | 0 | 4 | 1 |
| **25** | B | `recoleccion_validacion_datos_benchmarking` | `validacion_datos_benchmarking` | 6 | 3 | 3 | 0 |
| **26** | B | `intercambio_de_roles_para_motivacion` | `rotacion_de_puestos_para_mejora_calidad` | 6 | 1 | 5 | 0 |
| **27** | B | `control_estadistico_del_proceso` | `control_estadistico_no_implica_cero_defectos` | 6 | 4 | 2 | 0 |
| **28** | B | `benchmarking_proceso` | `benchmarking_mejores_practicas` | 6 | 1 | 5 | 0 |
| **30** | B | `eliminacion_causas_error_4` | `eliminacion_causas_error_2` | 8 | 0 | 6 | 2 |
| **31** | B | `circulos_calidad_qc` | `preparacion_gerencial_antes_de_circulos_de_calidad` | 5 | 2 | 3 | 0 |
| **32** | B | `autocontrol_y_controlabilidad` | `concepto_autocontrol` | 7 | 2 | 5 | 0 |
| **33** | B | `comunicar_politicas_organizacionales` | `politica_calidad_organizacional` | 6 | 3 | 2 | 1 |
| **35** | C | `ciclo_shewhart_pdsa` | `pdsa_shewhart_cycle` | 8 | 2 | 6 | 0 |
| **36** | C | `control_estadistico_de_procesos` | `control_estadistico_de_procesos_2` | 7 | 1 | 4 | 2 |
| **37** | C | `evaluacion_gestion_riesgos` | `plan_de_gestion_de_riesgos` | 7 | 1 | 5 | 1 |
| **38** | C | `enfasis_en_utilidades_corto_plazo` | `enfasis_en_ganancias_corto_plazo` | 6 | 5 | 1 | 0 |
| **39** | C | `grafico_de_corrida_run_chart` | `run_chart_datos_temporales` | 5 | 0 | 5 | 0 |
| **40** | C | `evaluacion_alternativas_solucion` | `evaluacion_seleccion_alternativas_mejora` | 5 | 1 | 3 | 1 |
| **41** | C | `definiciones_operacionales` | `caso_definicion_arruga` | 7 | 0 | 7 | 0 |
| **42** | C | `formula_exponencial_confiabilidad` | `distribucion_exponencial` | 6 | 1 | 4 | 1 |
| **43** | C | `medicion_calidad` | `medicion_calidad_2` | 7 | 4 | 2 | 1 |
| **44** | C | `analisis_reporte_benchmarking` | `desarrollo_reporte_benchmarking` | 7 | 2 | 5 | 0 |
| **45** | C | `gestion_efectiva_benchmarking` | `rol_alta_direccion_benchmarking` | 8 | 0 | 8 | 0 |
| **46** | C | `consumidor_como_eje_de_produccion` | `consumidor_parte_linea_produccion` | 5 | 3 | 2 | 0 |
| **47** | C | `identificar_clientes_externos_e_internos` | `identificar_clientes_diseno` | 5 | 2 | 3 | 0 |
| **48** | C | `juran_quality_by_design` | `quality_by_design` | 6 | 1 | 5 | 0 |
| **49** | C | `definiciones_operacionales_3` | `definiciones_operacionales_4` | 8 | 1 | 7 | 0 |
| **50** | C | `fijacion_de_metas` | `establecimiento_metas` | 4 | 0 | 3 | 1 |

| acto | lote | sus miembros | especie | se acumula para |
|---:|:---:|---|---|---|
| **13** | A | `premio_shingo`, `shingo_prize` | **EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN** | LA MESA, dentro del pendiente de doctrina 1. LOS TRES CONTEOS EMPATAN AL DIGITO: pasos 4 contra 4, condiciones 2 contra 2 y cableado 2 contra 2 (cuadro de varas de la vuelta 58, fila 13, re-derivado por el auditor). Por acta 53 pregunta 4, el empate sin vara es cuando TODO empata, y aqui todo empata. LA RAZON DEL PUESTO 2475 DECLARA PROPIO A LOS DOS LADOS, que es la figura exacta del acto 32 del tramo 4 resuelta en esta misma campana: de premio_shingo declara DOS PASOS que el otro no tiene (documentar evidencia de implementacion de principios Lean, y usar el feedback de la evaluacion externa para planificar los proximos pasos); de shingo_prize declara la madurez CULTURAL Y OPERATIVA y la puerta de los criterios minimos. Que la razon llame LINEA a lo del segundo y PASOS a lo del primero es una comparacion de PESO entre dos propios declarados, y pesar dos propios declarados para romper un empate triple es EXACTAMENTE la rama que el acta 58 dejo NO ADOPTADA al deshacer el acto 32. SE DECLARA Y NO SE FUNDE. Y va marcado como DISCUTIBLE en el reporte, porque hay una lectura sostenible en contra: cuando la razon clasifica el propio de un lado como LINEA esta diciendo que no lo cuenta, y entonces el propio declarado seria de UN SOLO LADO y por acta 54 pregunta 4 seria vara. No la aplico porque decidirlo asi es estrenar doctrina sobre un empate, y deshacer una fusion cuesta una vuelta entera, como acaba de costarla el 32. |
| **29** | B | `conciencia_calidad`, `conciencia_de_calidad_2` | **CONTEOS QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA** | LA MESA, dentro del pendiente de doctrina 1. LOS DOS CONTEOS DE CONTENIDO CHOCAN ENTRE SI: pasos 4 contra 5 apunta a conciencia_de_calidad_2 y condiciones 3 contra 2 apunta a conciencia_calidad (cuadro de varas de la vuelta 58, fila 29, cotejado hoy contra los nodos). Por acta 53 pregunta 3 y acta 54 pregunta 2, cuando dos varas de contenido CHOCAN decide LA PIEZA DECLARADA; y aqui LA PIEZA DECLARADA ESTA A LOS DOS LADOS Y NO DESEMPATA: la razon del puesto 2552 escribe REPITE POR FUSION MUTUA, DUODECIMO CASO DEL ARCHIVO, y NINGUNO DOMINA, reconociendo propio a los dos. De conciencia_calidad: EL COSTO REAL DE LA NO CALIDAD como contenido del mensaje, que es lo unico que le da sustancia a la campana, y LA EXTENSION A PERSONAL ADMINISTRATIVO Y DE SERVICIO. De conciencia_de_calidad_2: QUE CADA SUPERVISOR TRANSMITA DIRECTAMENTE Y NUNCA POR UNA SOLA REUNION MASIVA, que es regla de cascada y no de estilo; MANTENER CONSISTENCIA Y CUMPLIR LAS PROMESAS HECHAS EN LAS REUNIONES; y apoyar la logistica con relaciones publicas. CONTAR CUANTOS PROPIOS TIENE CADA LADO, DOS CONTRA TRES, ES LA RAMA DE LA CANTIDAD COMO VARA, QUE EL ACTA 58 DEJO NO ADOPTADA AL DESHACER EL ACTO 32 DEL TRAMO 4 Y QUE EL ENCARGO DE ESTA VUELTA PROHIBE USAR. EL CABLEADO TAMPOCO ENTRA: por P.8 el cableado solo habla a contenido EMPATADO, y aqui el contenido no empata, choca. SE DECLARA Y NO SE FUNDE. Va marcado como DISCUTIBLE en el reporte: es el primer ejemplar del tramo en que LAS DOS VIAS DE DESEMPATE ESCRITAS FALLAN A LA VEZ, los conteos porque chocan y la pieza declarada porque esta a los dos lados. |
| **34** | B | `pocos_vitales_muchos_utiles`, `proyectos_vitales_pocos` | **EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN** | LA MESA, dentro del pendiente de doctrina 1. LOS TRES CONTEOS EMPATAN AL DIGITO: pasos 4 contra 4, condiciones 2 contra 2 y cableado 2 contra 2 (cuadro de varas de la vuelta 58, fila 34, cotejado hoy contra los nodos). Por acta 53 pregunta 4, el empate sin vara es cuando TODO empata, y aqui todo empata. Y LA PIEZA DECLARADA TAMPOCO SEPARA, porque la razon del puesto 2575 escribe REPITE POR FUSION MUTUA, DECIMOTERCER CASO DEL ARCHIVO, NINGUNO DOMINA, y le reconoce a CADA UNO UNA LINEA PROPIA Y SOLO UNA: a pocos_vitales_muchos_utiles LA TERCERA CATEGORIA, el apagado de incendios, con su guarda de no volcar todos los recursos ahi, que es el unico del par que reconoce el trabajo reactivo; a proyectos_vitales_pocos el DELEGAR LOS PROYECTOS DE BAJO IMPACTO A EQUIPOS DEPARTAMENTALES LOCALES, que nombra a quien cae la cola. UNA CONTRA UNA: ni siquiera la rama NO ADOPTADA de la cantidad lo romperia. La propia razon escribe que por el visto de hoy LA FUSION MUTUA NO PRODUCE GANADOR POR DERECHO y que el acto es POR ELEGIR, y marca ella misma su discutible, que se trae sin tocar: quien lea la categoria de incendios como un acto aparte y no como una linea dira que pocos_vitales domina y es A plana; la defensa de la razon es que sigue siendo clasificar proyectos, en tres cubos en vez de dos. SE DECLARA Y NO SE FUNDE. |
| **suma** | | **3 declarados** | | |

### LAS PERDIDAS NOMBRADAS

**Talladas de los planes sellados** con el tallador de perdidas ([`../loop/SALIDA_V60_TALLAR_PERDIDAS.txt`](../loop/SALIDA_V60_TALLAR_PERDIDAS.txt)), que **lee la especie del propio plan y no tiene rama por defecto**.

| acto | lote | el nodo que muere | **ESPECIE** | por que se perdio | la frase del plan sellado que lo dice |
|---:|:---:|---|---|---|---|
| **19** | B | `equipo_mejora_calidad` | **DE PARAMETRO DE PASO** | el inciso MENTIRIA contra la unica restriccion del paso que protege | *PERDIDA NOMBRADA QUE LA RAZON MARCO, motivo ALCANCE, y se NOMBRA en vez de reponerse: no es un gesto suelto sino una MANERA de entender el rol que ya define el paso 5 del superviviente (hasta donde puede llegar este grupo para proponer y ejecutar acciones correctivas), y adosarla de inciso a ese paso convertiria un ...* |
| **suma** | | | **1 DE PARAMETRO DE PASO** | | |

### CORRECCION DECLARADA: **EL CAMPO `fecha` DEL PLAN SELLADO DEL LOTE A ESTA EQUIVOCADO**

**El plan del lote A (`../loop/PLAN_V59_OPU01_LOTE_A.json`) lleva `"fecha": "2026-08-21"` y ES
FALSO: aquella vuelta corrio el 20 de agosto de 2026.** La medicion esta corrida hoy y no supuesta:
los **seis commits del ejecutor de la vuelta 59** (`c9927b19`, `fd7de724`, `956f9e3d`, `39d495b2`,
`6b6607bb`, `02d0bf00`) llevan **todos** fecha `2026-08-20` por
`git log --format=%ad --date=format:'%Y-%m-%d'`, y el commit que sello ese plan es `39d495b2`, del
`2026-08-20 14:08:34`.

**EL PLAN NO SE REEDITA, y el motivo es el de la casa: un plan sellado es el registro de lo que se
decidio aquel dia y reescribirlo taparia lo que se corrige.** El error queda declarado AQUI, que es
el sitio que el encargo de la vuelta 60 senalo, y **la fecha buena es el 20 de agosto de 2026**.

**LO QUE SE ARREGLO PARA QUE NO VUELVA A PASAR, y se arreglo donde de verdad muerde:** el campo
`fecha` de la cabecera del generador de planes estaba **TALLADO A MANO**, asi que cualquier plan
sellado despues heredaba la misma fecha equivocada. Pasa a leerse del reloj
(`datetime.date.today()`), y **los planes de los lotes B y C ya nacieron con `2026-08-20`**,
comprobado leyendo los tres ficheros. **De aqui en adelante, la fecha de toda nota fechada y de todo
reporte SE MIDE, del reloj del sistema o del commit, y no se supone.**

### LO QUE ESTE REGISTRO NO PUEDE PUBLICAR, DICHO CON NOMBRE

**LA TABLA DE PERDIDAS DE ESTE TRAMO NO SALE ENTERA, Y LA CULPA NO ES DEL TRAMO SINO DEL
INSTRUMENTO.** Se declaran las dos mitades del problema, las dos medidas hoy:

1. **CONTABA DE MAS, y esto SI se corrigio.** El tallador contaba una perdida por cada aparicion del
   token `PERDIDA NOMBRADA` en la nota del reparto. Medido sobre los lotes B y C: de **SEIS**
   apariciones, **CINCO** viven dentro de frases que dicen lo contrario de una perdida, porque
   anuncian que la que la razon nombro **esta REPUESTA** por esta fusion (lote B actos 20, 28, 31 y
   32; lote C acto 36). **Sin corregirlo, la TABLA 1 de arriba habria publicado 5 perdidas en el
   lote B y 1 en el C, y las dos cifras son falsas.** La regla nueva es textual y comprobable: una
   aparicion no cuenta si en su misma frase el plan dice `SE REPONE`, `SE REPONEN` o `NO SE PIERDE`.
   **El contraste esta corrido: con la correccion puesta, el lote A de la vuelta 59 sigue dando 3,
   la misma cifra que ya publico.**
2. **SIGUE CONTANDO DE MENOS, y esto NO se corrigio porque corregirlo a ojo seria inventar.** El
   tallador solo ve las perdidas que llevan el token. Las que el plan nombra **con otras palabras**
   no las cuenta, y en estos dos lotes hay al menos cuatro: el matiz *sin recurrir a esquemas
   motivacionales artificiales* (lote B, acto 26), el matiz *o trabajador* de la condicion 1 (lote C,
   acto 36), la mitad de la denominacion `Concerns, Options, Consequences` que solo vive en el titulo
   del absorbido (lote C, acto 37) y la instancia `arruga`, que tambien vive solo en el titulo (lote
   C, acto 41). **Las cuatro estan escritas en su nota de reparto**; lo que falta es que un
   instrumento sepa contarlas.

**Y EL TALLADOR CAYO EN ROJO SOBRE EL UNICO ACTO QUE SI TIENE PERDIDA CON TOKEN, EL 19 DEL LOTE B**,
porque su nota nombra a la vez un paso y una condicion. **Eso es la guarda funcionando**: el
instrumento esta escrito para caer en ROJO antes que clasificar en silencio. Su salida entera esta
en [`../loop/SALIDA_V60_TALLAR_PERDIDAS.txt`](../loop/SALIDA_V60_TALLAR_PERDIDAS.txt).

**HALLAZGO APARTE, MEDIDO Y QUE NO ES DE ESTA VUELTA:** corrido el tallador **sin ningun cambio**
(`git stash`) sobre el lote A de la vuelta 59, **sus tres perdidas salen las tres en ROJO** (*el
trozo no nombra ni condicion ni paso*, actos 1, 4 y 7), y **la vuelta 59 nunca llego a correrlo**,
comprobado porque no existe `SALIDA_V59_TALLAR_PERDIDAS.txt`. La cifra **3** que aquella vuelta
publico en su TABLA 1 **sigue en pie y no la toca nada de esto**; lo que no existe, y no existia, es
la clasificacion por especie de esas tres.

---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 61, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (20 ago 2026, vuelta 62, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso con las tres adjudicaciones del acta 52 (linea **1250**) y con la del
acta 57 sobre el acto 25 (linea **2475**). **Ninguna cifra publicada se toca.** **Cada cita lleva la
linea del acta LEIDA HOY**, no recordada: el acta de la vuelta 61 abre en la linea **15690** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), su seccion de adjudicaciones en la **15822** y
la de las cinco preguntas en la **15879**.

### a) **EL TRAMO ES UN PREFIJO CON TOPE DE CINCUENTA, NO UN MINIMO: UN TRAMO CORTO POR AGOTAMIENTO ES UN TRAMO** (acta 61, `D1`, linea **15824**; pregunta 1, linea **15881**)

**LA VARA NO CAMBIA: SE LEE ENTERA.** La vara vigente es la cabecera del registro del tramo 1 de esta
misma pagina, **linea 360**, leida hoy: *El tramo son los CINCUENTA primeros actos `CERRADOS` de la
nomina re-medida al abrirlo, en el orden en que el instrumento los imprime.* **Eso define un PREFIJO
con TOPE de cincuenta, no un minimo:** fija el orden y corta en cincuenta. **El prefijo de una nomina
de veintiuno son los veintiuno.**

| lo que se pregunto | lo adjudicado | la vara |
|---|---|---|
| un tramo con **menos de cincuenta actos libres**, es un tramo? | **SI** | la linea **360** de esta pagina, leida como prefijo con tope |
| hace falta **doctrina nueva** para decirlo? | **NO.** De las tres salidas posibles, la de prefijo es **la unica que no estrena regla**; declararlo cierre en vez de tramo, o darle otra vara, **si la necesitarian** | acta 61, `D1` |
| **agotarse** es lo mismo que **truncar**? | **NO, y la diferencia es medible: truncar deja actos detras del corte y agotarse no deja ninguno.** En el tramo 6 se tomaron **21 de 21** y **no queda ni un acto fuera**, comprobado por el auditor con cuenta propia e independiente | acta 61, seccion 1, cuenta del tramo 6 por tres caminos |

**Y LA CONSECUENCIA QUE VIENE PEGADA, PORQUE EL ACTA LA DICTA EN LA MISMA RESPUESTA: EL TRAMO 6 ES EL
ULTIMO TRAMO DE `OP-U-01`.** Cuando el tramo 6 quede ejecutado y registrado, **el universo de
`OP-U-01` queda agotado**, y **su registro abre declarandolo con la cifra**: `TRAMO FINAL POR
AGOTAMIENTO: VEINTIUNO, NO CINCUENTA`.

**LO QUE ESTA ADJUDICACION NO AUTORIZA:** cortar un tramo por debajo de cincuenta **habiendo actos
libres detras del corte**. Eso sigue siendo truncar, y truncar no esta adjudicado.

### b) **UNA GUARDA PUEDE CRECER EN UN SUCESOR DECLARADO, CON DOS CONDICIONES** (acta 61, `D2`, linea **15839**; pregunta 2, linea **15887**)

El contrato del sucesor declarado es **copia byte a byte MAS lo declarado** (acta 54, pregunta 3), y
**lo declarado admite una guarda que CRECE** si cumple las dos:

| condicion | por que |
|---|---|
| **va enumerada en el docstring** del sucesor, entre lo que cambia | una guarda que crece **no es copia**, y lo que no es copia se enumera |
| **va marcada DISCUTIBLE** en el reporte de la vuelta que la estrena | es el unico cambio de la lista que **amplia lo comprobado**, y ampliar lo comprobado se somete |

**LA FIGURA ES LA DEL ABRIDOR:** el ancestro miraba `(1, 2, 3)` tallado a mano y **por eso dejo fuera
el tramo 4 al abrir el tramo 5**; la guarda que mira **TODOS los previos medidos** es **la correccion
de esa especie**, no una mutacion callada. **LO QUE ESTA ADJUDICACION NO CUBRE: crecer una guarda sin
declararla.**

### c) **`SELLO_FIJO` NO NECESITA FUENTE EXTERNA: BASTA LA GUARDA** (acta 61, `D3`, linea **15847**; pregunta 3, linea **15890**)

El barrido de titulos **no le cree a la palabra: le cree a la estructura**, que es **la MISMA
distincion que ya separa `ROJO` de `CENSO`** (sujeto repuntable por argumento contra sujeto fijo).

| rotulo | su sujeto vive | que se le exige |
|---|---|---|
| **`PROCEDENCIA`** | **FUERA** del fichero (un acta, un ancestro, otra vuelta) | **fuente externa citada**, porque el sujeto no esta en la pagina |
| **`SELLO_FIJO`** | **DENTRO** del propio fichero | **los tres dientes de la guarda**: sin argumento que repunte el sujeto, numero cotejado por maquina, y `ROTULO HUERFANO` en `ROJO` si no casa. **La fuente de un sujeto fijo es el propio fichero** |

**Exigirle ademas fuente externa seria regla nueva sin necesidad.** Los tres dientes **estan probados
sembrando averia** (acta 61, seccion 1: `sujeto=tramo:9` sembrado, el barrido dio `ROTULO HUERFANO`
en `ROJO`, restaurado y de vuelta a limpio).

### d) **LOS 29 VIVOS DE LOS TRAMOS 1 A 5 SON ACTOS DECLARADOS Y COSA JUZGADA** (acta 61, pregunta 4, linea **15893**)

| lo que son | **actos DECLARADOS**, cada uno con su motivo citado en el registro de su tramo |
|---|---|
| **quince** | siguen **la via de la mesa**, dentro del pendiente de doctrina 1 |
| **catorce** | **no tienen cola pendiente NI la necesitan**: su declaracion **es su estado final** mientras ninguna regla nueva los nombre |

**LO QUE ESTO CIERRA, con las palabras del acta: no se reparten, no se reabren, no entran en ningun
tramo por abrir.** Ocupan los puestos **1 a 29** como **prefijo para las guardas de solape y nada
mas**.

### e) **ENTRE CORRER UN ANCESTRO CUYO TITULO MIENTE Y ESCRIBIR UN SUCESOR DECLARADO QUE NO MIENTE, EL SUCESOR ES LA VIA** (acta 61, `D5`, linea **15861**; pregunta 5, linea **15900**)

**La mentira declarada en el reporte NO repara la salida publicada que la lleva.** Correr el ancestro
habria publicado un titulo que miente (**la especie exacta que la racha de reporte pago en las
vueltas 59 y 60**) o habria pagado un `ROJO` que el encargo prohibia pagar. **Dos ficheros de mas es
el precio de no mentir**, y **los ancestros quedan intactos y citados**, que es la via del acta 54
pregunta 3.

### f) **LOS TRES RESTANTES, ADJUDICADOS `A FAVOR` Y REGISTRADOS SIN DESARROLLO PORQUE NO CREAN CARRIL**

| | que se adjudico | la vara |
|---|---|---|
| **`D4`** | **extender el barrido la misma vuelta que publica su cifra**: `A FAVOR` por la adjudicacion ya escrita (`D7` de la vuelta 60, sus cuatro condiciones), cumplidas y re-verificadas | acta 61, linea **15856** |
| **`D6`** | **la exclusion de los DOS ficheros que hablan la gramatica** (el barrido y el triador), solo para el cotejo de rotulos y con los dos midiendose igual por titulos: **alcance minimo y motivo medido** | acta 61, linea **15867** |
| **`D7`** | **el lote A sin ejecutar en la vuelta 61**: `A FAVOR`, porque el encargo lo permitia expresamente, mandaba decirlo primero y **se dijo primero**; fundir 21 actos bajo una vara aun no adjudicada **habria decidido en silencio** lo que el `D1` traia a la mesa | acta 61, linea **15873** |

**NINGUNA DE LAS SIETE ESTRENA DOCTRINA**, y el acta lo dice en su seccion 8 (linea **15953**, leida
hoy): *Doctrina nueva: NO.*


---

## `OP-U-01`, TRAMO 6: EL REGISTRO DEL CIERRE (20 ago 2026, vuelta 62)

> **TRAMO FINAL POR AGOTAMIENTO: VEINTIUNO, NO CINCUENTA. Y CON EL, EL UNIVERSO DE `OP-U-01` QUEDA AGOTADO.**
> Este tramo no tiene cincuenta actos porque **ya no quedaban cincuenta**: fuera de los tramos 1 a 5
> solo quedaban **VEINTIUNO** actos `CERRADOS`, y el abridor **se los llevo todos**. **Agotarse no es
> truncar, y la diferencia es medible: truncar deja actos detras del corte y aqui no queda ninguno**
> (21 tomados de 21, comprobado por el abridor, por la nomina de la 48 y por la corrida propia del
> auditor, tres caminos).

> **LA VARA NO SE ESTRENO PARA ESTO: SE LEYO ENTERA.** Que un tramo corto por agotamiento SEA un
> tramo esta **adjudicado por el acta de la vuelta 61** (`D1` y pregunta 1, registradas al final de
> esta misma pagina): la vara de la linea **360** define un **PREFIJO CON TOPE de cincuenta, no un
> minimo**, y **el prefijo de una nomina de veintiuno son los veintiuno**. **Ninguna regla nueva se
> estrena aqui.**


**LA VARA QUE FIJA EL TRAMO ES LA MISMA DESDE LA VUELTA 48**, escrita en la cabecera del registro
del tramo 1: *los CINCUENTA primeros actos CERRADOS de la NOMINA RE-MEDIDA AL ABRIRLO*. **EL INSUMO
DE ESTE TRAMO SE MIDIO Y SE FIJO AL ABRIRLO Y NO SE RE-MIDIO NI UNA VEZ DESPUES**, que es lo que el
encargo mandaba
([`../loop/SALIDA_V61_TRAMO6_ABIERTO.txt`](../loop/SALIDA_V61_TRAMO6_ABIERTO.txt)).

**GUARDA DEL PREFIJO:** los vivos de los tramos anteriores son **29** y ocupan sus puestos
sin huecos, medido y no tecleado. **El tramo 6 son los puestos 30 a 50 de
hoy.** **Solape con los tramos anteriores: CERO.**

> **EL COTEJO DEL INSUMO, CORRIDO ANTES DE ESCRIBIR UNA LINEA DE CADA PLAN:** el
> insumo se midio y se FIJO al abrir el tramo y no se re-mide, pero entre aquella
> foto y hoy puede haberse fundido un lote del mismo tramo, y una fusion CAMBIA los
> pasos del superviviente. `scripts/loop/vuelta60_cotejo_insumo.py` NO re-mide:
> COTEJA contra los nodos de hoy y dice en que actos la foto dejo de calzar.
>
> **RESUMEN: actos mirados 21 | VIVOS 21 | ya fundidos 0 | DESCALCES 0**
> ([`../loop/SALIDA_V62_COTEJO_INSUMO.txt`](../loop/SALIDA_V62_COTEJO_INSUMO.txt))
>
> **RESUMEN: actos mirados 10 | VIVOS 10 | ya fundidos 0 | DESCALCES 0**
> ([`../loop/SALIDA_V62_COTEJO_INSUMO_B.txt`](../loop/SALIDA_V62_COTEJO_INSUMO_B.txt))

**LAS COLISIONES ESPERADAS DEL TRAMO ENTERO, medidas ANTES de tocar un nodo** sobre el archivo
entero y por par resuelto
([`../loop/SALIDA_V61_COLISIONES_ESPERADAS_TRAMO6.txt`](../loop/SALIDA_V61_COLISIONES_ESPERADAS_TRAMO6.txt)):
**42 combinaciones simuladas y 0 que fabriquen colision.** Ni una. **Por eso este
tramo NO volteo ningun veredicto y el marcador queda identico al abrir y al cerrar.**

### EL ESTADO, MEDIDO AL ABRIR LA VUELTA QUE CIERRA EL TRAMO Y RECOMPUTADO AL CERRARLA

| | **apertura de la vuelta 62** | **cierre, RECOMPUTADO** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| grafo: vivos / deprecados / enlaces | 3.295 / 558 / 17.449 | **3.274 / 579 / 17.486** |
| retrato: colapsos / pares distintos | 254 / 297 | **275 / 276** |
| actos (componentes) / `CERRADOS` | 103 / 50 | **82 / 29** |
| actos del tramo 6 fundidos / vivos | 0 / 21 | **21 / 0** |

> **EL TRAMO ABRE Y CIERRA DENTRO DE ESTA MISMA VUELTA, medido y no supuesto: los
> 2 planes sellados que el tallador hallo son TODOS de la vuelta 62.** Por eso la
> columna de apertura SI precede al tramo entero: cuando se tomo no habia ni un
> acto de este tramo fundido, y la diferencia entre las dos columnas es el efecto
> del tramo completo.

### EL REPARTO, TALLADO DE LOS PLANES SELLADOS DE ESTA VUELTA

**Ninguna de estas tablas esta tecleada:** salen enteras de
`python scripts/loop/tallar_planes_del_tramo.py --vuelta 62 --prefijo PLAN_V62_OPU01_LOTE_`
([`../loop/SALIDA_V62_TALLAR_PLANES.txt`](../loop/SALIDA_V62_TALLAR_PLANES.txt)), que las cuenta de los planes **SELLADOS** y **cae en ROJO
con el acto nombrado si un motivo no encaja en ninguna forma conocida**. **`--prefijo` se hizo
REPETIBLE en esta vuelta justamente para esto**: con un prefijo unico, el registro habria publicado
**lo mismo que publica, porque los planes de este tramo caben en UN solo prefijo y ahi la repetibilidad no cambia nada**, y las cuatro tablas habrian mentido por omision.

 LOS 2 LOTES, CON SUS PIEZAS ---

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **A** | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | **11** | **11** | **69** | 14 | 45 | **10** | **12** |
| **B** | 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 | **10** | **10** | **65** | 13 | 46 | **6** | **6** |
| **los 2** | | **21** | **21** | **134** | **27** | **91** | **16** | **18** |

| la forma, leida del motivo sellado | cuantos | los actos |
|---|---:|---|
| **UNA SOLA VARA de contenido no empatada, y BASTA** | **11** | 1, 3, 5, 6, 10, 12, 14, 16, 18, 19, 21 |
| **TODAS LAS VARAS de contenido de acuerdo** | **5** | 4, 8, 11, 13, 17 |
| **EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO** | **4** | 2, 7, 9, 15 |
| **LA PUERTA SOBREVIVE, con el choque registrado** | **1** | 20 |
| **suma** | **21** | |

| acto | lote | sobrevive | absorbe | piezas | enteras | ya dichas | `INCISO` |
|---:|:---:|---|---|---:|---:|---:|---:|
| **1** | A | `gestion_miedo_reportes` | `administracion_sin_miedo` | 6 | 0 | 6 | 0 |
| **2** | A | `contacto_con_el_cliente` | `contacto_con_el_cliente_2` | 6 | 2 | 2 | 2 |
| **3** | A | `analisis_de_sistemas_de_medicion_msa` | `errores_de_medicion` | 7 | 0 | 6 | 1 |
| **4** | A | `definicion_problema_moms_2` | `definicion_problema_moms` | 5 | 0 | 5 | 0 |
| **5** | A | `planificacion_gobierno_organizaciones_familiares` | `gobierno_corporativo_juntas_directivas` | 8 | 0 | 7 | 1 |
| **6** | A | `falacia_recompensa_loteria` | `sistemas_recompensa_aleatorios` | 6 | 3 | 3 | 0 |
| **7** | A | `riesgos_consenso_inspeccion` | `comparacion_inspectores_independientes` | 7 | 2 | 5 | 0 |
| **8** | A | `revision_progreso` | `revision_progreso_breakthrough` | 5 | 3 | 1 | 1 |
| **9** | A | `rol_tactico_estrategico_oficina` | `gestion_estrategica_de_calidad_sqm` | 6 | 1 | 5 | 0 |
| **10** | A | `roadmap_despliegue_lean_six_sigma` | `juran_transformation_roadmap` | 7 | 1 | 2 | 4 |
| **11** | A | `orgullo_por_el_trabajo` | `eliminacion_barreras_orgullo_del_trabajo` | 6 | 2 | 3 | 1 |
| **12** | B | `cinco_suposiciones_erroneas_calidad` | `concepto_supuestos_erroneos_sobre_calidad` | 6 | 3 | 1 | 2 |
| **13** | B | `organizacion_liderazgo_estadistico` | `estadistico_competente_organizacion` | 5 | 1 | 3 | 1 |
| **14** | B | `sistema_pull_push` | `kanban_pull_system` | 7 | 1 | 5 | 1 |
| **15** | B | `manejo_problemas` | `cultura_integridad_objetividad_resolucion_problemas` | 6 | 2 | 4 | 0 |
| **16** | B | `seminario_de_exito_para_gerencia` | `cambio_actitud_gerencial` | 7 | 0 | 7 | 0 |
| **17** | B | `evaluacion_riesgo_calidad_organizacional` | `evaluacion_organizacional_calidad` | 7 | 0 | 6 | 1 |
| **18** | B | `control_del_proceso_del_proveedor` | `planificacion_tecnologica_conjunta` | 7 | 3 | 4 | 0 |
| **19** | B | `respuesta_incidentes_cui` | `getting_started_incident_response` | 5 | 1 | 3 | 1 |
| **20** | B | `mantenimiento_sistema_cui` | `getting_started_maintenance` | 7 | 2 | 5 | 0 |
| **21** | B | `funcion_protect_politica_seguridad` | `protect_medidas_tecnicas` | 8 | 0 | 8 | 0 |

| acto | lote | sus miembros | especie | se acumula para |
|---:|:---:|---|---|---|
| **suma** | | **0 declarados** | | |

### LAS PERDIDAS NOMBRADAS

**Talladas de los planes sellados** con el tallador de perdidas ([`../loop/SALIDA_V62_TALLAR_PERDIDAS.txt`](../loop/SALIDA_V62_TALLAR_PERDIDAS.txt)), que **lee la especie del propio plan y no tiene rama por defecto**.

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V62_OPU01_LOTE_A.json | 1 | DE PARAMETRO DE PASO | el escenario del limite DE ESPECIFICACION como sitio donde mirar la concentracion anomala de datos; el superviviente solo nombra el limite regulatorio y el de aceptacion | paso 1 de administracion_sin_miedo | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_A.json | 3 | DE PARAMETRO DE PASO | el LABORATORIO como fuente de variabilidad del sistema de medicion; el superviviente lista material, analistas, aparatos y dias, y no lo incluye | paso 2 de errores_de_medicion | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_A.json | 3 | DE CONDICIONES | el disparador de estar bajo enfoque Six Sigma con niveles de defectos exigidos; el superviviente dispara por validar la precision antes de decidir y por dudas sobre la exactitud, y no nombra el programa | condicion 1 de errores_de_medicion | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V62_OPU01_LOTE_A.json | 4 | DE PARAMETRO DE PASO | MEDIANTE SINTOMAS, que es como se comprueba la O de observable; el superviviente enumera las cuatro letras del criterio y no dice con que se verifica cada una | paso 3 de definicion_problema_moms | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_A.json | 4 | DE PARAMETRO DE PASO | DENTRO DEL ALCANCE DEL EQUIPO, que es la vara con la que se confirma la M de manejable en el paso 4 del absorbido | paso 4 de definicion_problema_moms | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_A.json | 5 | DE CONDICIONES | el disparador de querer PROFESIONALIZAR LA TOMA DE DECISIONES ESTRATEGICAS; el superviviente dispara por el retiro del fundador, por varias generaciones en la gestion y por una junta que solo firma | condicion 3 de gobierno_corporativo_juntas_directivas | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V62_OPU01_LOTE_A.json | 6 | DE PARAMETRO DE PASO | el REEMPLAZO del reconocimiento por desempeno puntual con ANALISIS DE TENDENCIAS EN GRAFICOS DE CONTROL INDIVIDUALES; el superviviente dice evitar el premio individual y mejorar el sistema, y no nombra ese mecanismo | paso 3 de sistemas_recompensa_aleatorios | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_A.json | 7 | DE PARAMETRO DE PASO | el seguimiento A LO LARGO DEL TIEMPO del grafico de los inspectores; el grafico del superviviente organiza acuerdos y desacuerdos POR TIPO DE CASO, que no es lo mismo que la serie longitudinal | paso 4 de comparacion_inspectores_independientes | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_A.json | 7 | DE PARAMETRO DE PASO | la particion diagnostica de la discrepancia, si viene de diferencias ENTRE INSPECTORES o ENTRE MUESTRAS; el superviviente investiga el desacuerdo para pedir mejores definiciones o entrenamiento y no hace esa separacion | paso 5 de comparacion_inspectores_independientes | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_A.json | 7 | DE CONDICIONES | el disparador de la sospecha de sesgo o divergencia sistematica entre evaluadores SIN relacion jerarquica de por medio; la condicion 2 del superviviente exige esa relacion jerarquica | condicion 2 de comparacion_inspectores_independientes | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V62_OPU01_LOTE_A.json | 9 | DE PARAMETRO DE PASO | la mirada sobre QUIEN MANEJA LA CALIDAD, si piensa solo en lo tecnico o tambien tiene vision de conjunto; el superviviente clasifica actividades en tacticas o estrategicas y no evalua a la persona | paso 1 de gestion_estrategica_de_calidad_sqm | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_A.json | 11 | DE PARAMETRO DE PASO | CAMBIAR LOS DISCURSOS MOTIVACIONALES Y LOS CARTELES, o sea la mitad de RETIRAR los lemas; el superviviente hace la mitad de PONER accion visible sobre las sugerencias y no nombra los carteles | paso 4 de eliminacion_barreras_orgullo_del_trabajo | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_B.json | 14 | DE PARAMETRO DE PASO | el AJUSTE DE LOS NIVELES DE KANBAN segun la variacion de demanda; el superviviente monitorea la reduccion del tiempo de entrega y la mejora en confiabilidad, que es otro objeto | paso 5 de kanban_pull_system | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_B.json | 15 | DE CONDICIONES | el encuadre de que sean LOS SUPERVISORES los que evitan reportar problemas por miedo a ser senalados; la condicion que se anade habla del clima de culpa o temor sin nombrar a ese sujeto | condicion 2 de cultura_integridad_objetividad_resolucion_problemas | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V62_OPU01_LOTE_B.json | 16 | DE PARAMETRO DE PASO | las formas concretas del compromiso, FIRMAR o LEVANTAR LA MANO; el superviviente pide compromisos publicos y visibles y no dice con que gesto se dan | paso 4 de cambio_actitud_gerencial | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_B.json | 16 | DE PARAMETRO DE PASO | RECONOCER LOGROS Y DAR SEGUIMIENTO al repetir el proceso; el paso 6 del superviviente repite y EXTIENDE a los espacios de revision, que no es reconocer ni dar seguimiento. ES LA PERDIDA CANDIDATA QUE LA RAZON DEL PUESTO 3064 DEJO MARCADA SIN VERIFICAR, y aqui queda sellada | paso 5 de cambio_actitud_gerencial | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_B.json | 17 | DE PARAMETRO DE PASO | las AREAS CLAVE sobre las que se aplica el criterio de enfoque, despliegue y resultados: alineacion estrategica, sistema de calidad, medicion, procesos, empleados, proveedores y resultados | paso 2 de evaluacion_organizacional_calidad | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V62_OPU01_LOTE_B.json | 17 | DE PARAMETRO DE PASO | la REVISION DE DOCUMENTOS como fuente de la recoleccion; el superviviente recolecta por observacion, entrevistas y revision de resultados operativos | paso 3 de evaluacion_organizacional_calidad | la fase 04, que redacta y afina los pasos del superviviente |

**EL TRAMO CIERRA CON CERO ACTOS DECLARADOS, y es el primero de la campana que lo hace.** **El motivo esta medido y no es merito:** el cuadro de varas del tramo 6 ([`../loop/SALIDA_V61_VARAS_TRAMO6.txt`](../loop/SALIDA_V61_VARAS_TRAMO6.txt)) **no trae ni un `CHOCAN` ni un `EMPATE SIN VARA`** (12 de `UNA SOLA VARA`, 5 de `TODAS DE ACUERDO` y 4 de `CONTENIDO EMPATA`), y esas son **las dos unicas figuras que declaran**. **LA MESA SE QUEDA EN QUINCE ACTOS**, los mismos que el acta 60 conto, y **la rama de LA CANTIDAD COMO VARA sigue NO ADOPTADA y no se uso en ningun acto de estos dos planes.**

**EL UNICO CHOQUE DE PUERTA DEL TRAMO, REGISTRADO EN VEZ DE TAPADO: EL ACTO 20.** `mantenimiento_sistema_cui` es **puerta** (extremo de puente aprobado, leido del dossier y de la columna `puerta` del cuadro de varas), y **las DOS vias apuntaban al otro lado**: la vara de contenido (pasos 6 contra 5) y **la razon del puesto 3364, que NOMBRA superviviente a `getting_started_maintenance` por dominancia**. **La guarda `1B` prohibe absorber una puerta**, asi que **LA PUERTA SOBREVIVE** por acta 54 pregunta 1, y **el choque queda escrito en el motivo sellado del acto**. **Y LA CONSECUENCIA VA DICHA:** el paso con el que la razon daba esa dominancia, *sanitizar o destruir equipos con CUI antes de retirarlos de las instalaciones*, **es justo el que tuvo que viajar de `APPEND`, y viajo**.

**LAS PERDIDAS DE ESTE TRAMO NO VIVEN EN LA PROSA: VIVEN EN UN CAMPO DEL PLAN.** Los dos planes nacen con el contrato **`CAMPO PROPIO v1`** (raiz con `contrato_de_perdidas`, y cada acto con su lista `perdidas`, **siempre, aunque vacia**). **LISTA VACIA es una DECLARACION de cero perdidas; CAMPO AUSENTE es que el plan no lo dice, y eso es `ROJO`.** De los **21** actos, **nueve declaran cero perdidas** y **doce sellan al menos una**. **Es el pendiente de instrumento que el acta 60 dejo escrito**, y con el, la mitad que la correccion de aquella vuelta no pudo arreglar (*sigue contando de menos las que el plan nombra con otras palabras*) **queda cerrada por contrato en vez de por heuristica**.

**CORRECCION DECLARADA SOBRE LOS INSTRUMENTOS QUE ESCRIBEN ESTE REGISTRO (20 ago 2026, vuelta 62), y va aqui porque toca a las cifras de esta misma pagina.** `scripts/loop/tallar_planes_del_tramo.py` contaba las perdidas **SOLO por el token en la prosa**, y con el contrato nuevo eso habria publicado **`perdidas nombradas 0` en la TABLA 1 de arriba cuando el campo sella DIECIOCHO**. Ahora, **si el plan declara el contrato, la cuenta sale del campo**; si no lo declara, se cuenta por token como hasta ahora. **EL CONTRASTE ESTA CORRIDO Y NO AFIRMADO:** sobre los planes del tramo 5, que no declaran el contrato, esta version da **exactamente las mismas cifras que aquel registro publico (A 3, B 1, C 0, los tres 4)**, y la unica diferencia del `diff` es el rotulo de la cabecera ([`../loop/SALIDA_V62_CONTRASTE_TRAMO5.txt`](../loop/SALIDA_V62_CONTRASTE_TRAMO5.txt)). **Y `registrar_cierre_de_tramo.py` llevaba TRES bloques de su plantilla TALLADOS A MANO CON LAS CIFRAS DEL TRAMO 5** (*50 actos mirados, 34 vivos, 16 ya fundidos*, la casilla *0 / 50*, y la nota que afirmaba que el lote A ya estaba fundido al tomar la apertura). **Corrido tal cual, este registro habria publicado esas tres cosas, y las tres son falsas en un tramo de veintiuno que abre y cierra en la misma vuelta.** Las tres pasan a medirse; **el texto viejo queda citado entero dentro del propio instrumento**, que es lo que la regla 8 pide.

**LO QUE QUEDA DE `OP-U-01`, DICHO SIN ADORNO Y CON SU CIFRA:** **el universo esta agotado**. Los **29** actos vivos de los tramos 1 a 5 son **cosa juzgada** de los registros de sus tramos (acta 61, pregunta 4): quince siguen la via de la mesa y catorce **no tienen cola pendiente ni la necesitan**. **No se reparten, no se reabren y no entran en ningun tramo por abrir**, porque **no queda ninguno por abrir**.


---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 62, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (20 ago 2026, vuelta 63, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso tres veces: las tres adjudicaciones del acta 52 (linea **1250**), la
del acta 57 sobre el acto 25 (linea **2475**) y las del acta 61 (linea **2689**), **las tres
cotejadas HOY abriendo el fichero**. **Ninguna cifra publicada se toca.** **Cada cita lleva la linea
del acta LEIDA HOY**, no recordada, y **cada una se imprimio y se comparo antes de escribir esta
seccion** con `python scripts/loop/_v63_registrar_acta62.py --simular`, que cae en `ROJO` sin
escribir si una sola no calza: el acta de la vuelta 62 abre en la linea **15971** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), su seccion de adjudicaciones en la **16115**,
la de las cinco preguntas en la **16169** y la de las caidas en la **16098**.

### a) **LOS NUEVE DISCUTIBLES DE LA VUELTA 62, LOS NUEVE `A FAVOR`, CADA UNO CON LA VARA QUE LO SOSTIENE**

**Es la primera tanda de la campana con los NUEVE a favor y sin una sola caida de clase ni de cifra.**
La columna de la vara **no es una glosa: es la regla citable con la que el auditor lo adjudico**, y
va copiada de su linea.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | **hizo crecer una guarda en un sucesor declarado**: el generador valida las perdidas AL SELLAR, cosa que el ancestro no hacia | **acta 61, `D2` y pregunta 2**: una guarda puede crecer en un sucesor declarado **con dos condiciones**, enumerada en el docstring y marcada discutible. **Las dos se cumplieron**, y es su primera aplicacion | **16117** |
| **`D2`** | **corrigio el mismo dia dos instrumentos que cuentan las cifras de esa misma vuelta** | **la alternativa era publicar dos cifras falsas** (*50 actos mirados* y *perdidas 0*). **El contraste sobre el tramo 5 da IDENTICO al registro viejo**: la correccion **honra el conteo, no lo acomoda**, y el texto viejo queda citado entero en los dos instrumentos | **16122** |
| **`D3`** | **ejecuto el tramo entero en una vuelta** cuando el encargo pedia el lote A | **la letra del encargo lo contemplaba**: decia *entrega lo que cierre entero* y **traia ya escrito que hacer si el tramo cerraba entero**. Cerrar entero estaba DENTRO de la letra | **16128** |
| **`D4`** | **fundio el acto 20 hacia la puerta** contra la vara de contenido y contra una razon que nombraba por DOMINANCIA | **acta 54, pregunta 1**: *LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO*, y **la letra no distingue como hable el contenido**, por elegir o por dominancia. **La dominancia no se pierde: su paso viajo de `APPEND`** | **16133** |
| **`D5`** | **apendio 3 pasos en el acto 8 y 3 en el acto 18**, los dos repartos mas anchos del tramo | **cada pieza viajada es un gesto que el superviviente no hacia en ningun grado**, releido pieza a pieza por el auditor. Los supervivientes quedan en 8 y 9 pasos y **son candidatos legitimos a la poda de la fase 04, ya anotada en los planes** | **16140** |
| **`D6`** | **nombro 18 perdidas** cuando el tramo 5 entero nombro 4 | **la cifra NO es comparable entre tramos**, y por eso la comparacion no pesa. El desarrollo esta en el apartado **c)** de aqui abajo | **16148** |
| **`D7`** | **decidio el acto 1 por la cuenta de CONDICIONES** (2 contra 3) contra un cableado de 7 contra 3 | **`P.8` al pie mas acta 53 pregunta 4**: pasos 4 contra 4 empatados, condiciones la unica vara que separa, y **el cableado solo habla a contenido EMPATADO**. Cotejado por el auditor contra el arbol de apertura | **16150** |
| **`D8`** | **decidio el acto 5 igual**, por pasos 5 contra 6, **hacia un nodo con cero siguientes** | **la cantidad de cableado NO es vara adoptada**, y la objecion del grafo pobre **se disuelve midiendo**: el superviviente HEREDO el cableado del que murio y hoy tiene 2 siguientes | **16155** |
| **`D9`** | **marco `CUBIERTO` con perdida sellada en vez de `INCISO` en once sitios** | **la letra de la politica del reparto**: *de `CUBIERTO` con la perdida NOMBRADA cuando el paso resultante no se lee limpio*. **La legibilidad del paso resultante ES el criterio escrito**, y con el contrato nuevo la perdida sellada **es visible y enrutada, no un silencio** | **16160** |

> **EL LIMITE QUE EL `D9` NO CUBRE, Y VA REGISTRADO PORQUE ES LA MITAD UTIL:** marcar `CUBIERTO` con
> perdida **para ahorrarse un `INCISO` que SI cabria limpio**. En los once sitios releidos el auditor
> **no vio ese abuso**, pero la adjudicacion **no lo autoriza**.

### b) **LAS PLANTILLAS DE LOS INSTRUMENTOS ESTABLES: NO HACE FALTA VARA NUEVA, LA REGLA 1 YA LAS CUBRE POR EXTENSION** (acta 62, pregunta 1, linea **16171**)

**LA LECTURA, ENTERA Y CITABLE.** La regla 1 del ejecutor (`EL INSTRUMENTO MANDA`, en su segundo
renglon) dice que **toda cifra publicada se lee de la salida del instrumento corrido EN ESA VUELTA**
y que **una nota vieja NUNCA es fuente de una cifra nueva**. De ahi sale, sin regla nueva, que:

> **UNA PLANTILLA CON CIFRAS TALLADAS HACE DECIR AL INSTRUMENTO CIFRAS QUE NO MIDIO, o sea VIOLA LA
> REGLA 1 CADA VEZ QUE CORRE.** No es una averia del dia en que se escribio: **es una averia que se
> dispara sola en la corrida siguiente**, y por eso vive en el instrumento y no en el reporte.

**LA FORMA DEBIDA, en una linea: EL BLOQUE SE ARMA DEL INSUMO O DECLARA SU FALTA.** Es la forma que
la correccion de `registrar_cierre_de_tramo.py` ya tiene (vuelta 62) y la que la vuelta 63 le puso a
`generar_plan_del_lote.py`.

**LO QUE SE ENCARGO NO ES DOCTRINA SINO MEDICION, y esa medicion esta hecha:** el censo unico de las
plantillas de salida de los instrumentos de nombre estable, con su instrumento propio
(`scripts/loop/censo_de_plantillas_talladas.py`, de nombre estable el tambien) y su salida publicada
([`../loop/SALIDA_V63_CENSO_PLANTILLAS.txt`](../loop/SALIDA_V63_CENSO_PLANTILLAS.txt)). **Dio UN
solo `TALLADO` en los quince**, y era `generar_plan_del_lote.py`. **Queda corregido en la misma
vuelta, con el texto viejo citado entero dentro del propio fichero y con su caso positivo corrido**
([`../loop/SALIDA_V63_CASO_POSITIVO_CABECERA.txt`](../loop/SALIDA_V63_CASO_POSITIVO_CABECERA.txt)).
**El censo re-corrido despues da CERO `TALLADOS`**
([`../loop/SALIDA_V63_CENSO_PLANTILLAS_TRAS_CORREGIR.txt`](../loop/SALIDA_V63_CENSO_PLANTILLAS_TRAS_CORREGIR.txt)).

### c) **LAS PERDIDAS DE DOS TRAMOS NO SE COMPARAN SI LAS CUENTAN INSTRUMENTOS DISTINTOS** (acta 62, pregunta 3, linea **16186**; `D6`, linea **16148**)

**LA LETRA, tal como el acta la escribe:** las 18 perdidas del tramo 6 y las 4 del tramo 5 **las
cuentan instrumentos distintos**, el campo sellado contra el token en la prosa, y

> **compararlas leeria UNA MEJORA DE INSTRUMENTO COMO UN EMPEORAMIENTO DE FUSION.**

**LO QUE SI ES COMPARABLE, Y ES LA MITAD QUE HACE UTIL LA REGLA: LA SERIE POR ESPECIE, HACIA
ADELANTE.** De este tramo en adelante, **mientras el contrato `CAMPO PROPIO v1` no cambie**, las
cifras de perdidas **si se pueden poner una al lado de otra**, porque las cuenta el mismo
instrumento con la misma vara. **Hacia atras, no.**

### d) **LA CAIDA DE REPORTE DE LA VUELTA 62, REGISTRADA CON SUS SEIS SITIOS** (acta 62, seccion 3, linea **16100**; hallada en la ciega, linea **16085**)

**QUE FUE, dicho sin adorno:** seis motivos sellados de los planes del tramo 6 **prometen `VA MARCADO
COMO DISCUTIBLE`** y **la seccion 6 de aquel reporte no trae ninguno de los seis**. **CERO datos
movidos y el fondo de los seis actos re-verificado limpio** (cotejo mecanico del auditor, 21 de 21),
pero **una promesa de marcado incumplida es caida de la especie de REPORTE**, y **la racha de reporte
pasa de cero a uno**.

**LOS SITIOS, MEDIDOS Y NO RECORDADOS.** La tabla sale entera de
`python scripts/loop/_v63_sitios_promesa.py`
([`../loop/SALIDA_V63_SITIOS_PROMESA.txt`](../loop/SALIDA_V63_SITIOS_PROMESA.txt)), que busca la
frase en los dos planes sellados y la coteja contra la seccion 6 del reporte:

| acto | lote | el motivo sellado dice **en el reporte** | **cumplida** |
|---:|---|---|---|
| **5** | A | **SI** | **SI**, es el `D8` del reporte |
| **7** | A | no | **NO** |
| **9** | A | **SI** | **NO** |
| **10** | A | **SI** | **NO** |
| **12** | B | no | **NO** |
| **15** | B | no | **NO** |
| **19** | B | no | **NO** |

> **UN DATO QUE EL ACTA NO PUBLICO Y LA MEDICION DE HOY ANADE, y va aqui porque afina la caida sin
> disolverla: LAS PROMESAS ERAN SIETE, NO SEIS, Y UNA SE CUMPLIO.** El acto 5 promete con las mismas
> palabras y **si llego al reporte, como `D8`**. **Las incumplidas siguen siendo exactamente las seis
> que el acta nombra** (7, 9, 10, 12, 15 y 19), **y de ellas dos prometian ademas el sitio** (9 y 10,
> con *en el reporte* explicito). La cuenta del acta **no cambia**; lo que cambia es que ahora se
> puede ver **que la promesa a veces si se cumplia**, que es peor y no mejor para el ejecutor: **no
> era un giro de estilo que nadie honraba, era un compromiso que se honro una vez de siete**.

**LA REGLA QUE SALE DE AQUI NO ES NUEVA: ES LA REGLA 2 DEL PROTOCOLO DEL EJECUTOR LEIDA ENTERA.** Lo
que un motivo sellado prometa del reporte, **el reporte lo cumple**; y si al consolidar se decide que
un discutible del plan **no llega a la seccion 6**, el reporte **lo DICE con su motivo en vez de
callarlo**.

### e) **LAS DOS PREGUNTAS RESTANTES, REGISTRADAS SIN DESARROLLO PORQUE NO CREAN CARRIL NUEVO**

| | que contesta | linea |
|---|---|---:|
| **pregunta 2** | **el carril de la puerta BASTA aunque la razon nombre por dominancia**: la guarda **no lee el tono de la razon, restringe**, y el contenido dominante **viaja en vez de perderse**. Es el `D4` por otro lado | **16183** |
| **pregunta 4** | **si se podia cerrar el tramo entero**: la letra del encargo **lo contemplaba con su registro ya prescrito**. Es el `D3` por otro lado | **16191** |

### f) **Y LA QUINTA, QUE SI MANDA SOBRE LO QUE VIENE DESPUES: EL ORDEN NO SE ELIGE** (acta 62, pregunta 5, linea **16193**)

**Agotada `OP-U-01`, la siguiente operacion SALE DEL ORDEN YA ADJUDICADO EN LA VUELTA 47** y esta en
esta misma pagina, en la seccion **EL ORDEN DE ESTA FASE** (linea **62**), cuya tabla de desbloqueos
dejo medido el empate del puesto 1: **`OP-U-01` con 2 desbloqueos, `OP-M-03-I` con 1 y
`OP-M-02-PROG` con 0**. **Siguen, en ese orden, `OP-M-03-I` y despues `OP-M-02-PROG`**, las dos
desbloqueadas. **Despues viene el puesto 2, donde vive `OP-U-02`**, cuya apertura **se puede MEDIR
sin fundir nada**.

---

## `OP-M-03-I`: EL REGISTRO DE LA FUSION (2026-08-20, vuelta 63)

**Cada celda de este registro sale de un instrumento corrido en la vuelta 63 y pegada entera**, con el comando citado al lado. **El registro se adosa al final de la pagina y NO reescribe ni una linea de arriba.**

| | |
|---|---|
| **la ficha** | `docs/plan/OPERACIONES.jsonl`, tipo **FUSION DE MESA**, estado **LISTA**, fecha de corte **2026-08-12** |
| **superviviente** | `pivotar_o_perseverar` |
| **absorbe** | `decision_pivote_perseverar` |
| **plan sellado** | [`../loop/PLAN_V63_OPM03I.json`](../loop/PLAN_V63_OPM03I.json), contrato **`CAMPO PROPIO v1`** |
| **censo del catalogo** | ANTES 3853 ficheros, 3274 vivos, 579 deprecados . DESPUES 3853 ficheros, 3273 vivos, 580 deprecados . **delta de deprecados +1 (esperado +1): OK** |
| **el superviviente** | 5 -> 6 (anadidos 1), condiciones 2 -> 3 (anadidas 1) |
| **piezas repartidas** | **7 (2 viajan enteras, 3 ya estaban dichas)** |

**LA ADJUDICACION, COPIADA VERBATIM DE LA FICHA Y NO REDACTADA AQUI:**

> ACTO I, LA PUERTA DE METRICAS DE RIES. Sobrevive pivotar_o_perseverar por CABLEADO A CONTENIDO EMPATADO, 6 contra 4, que es el supuesto en el que P.8 deja decidir al grafo. CONSERVA EL BLOQUE DEL PUNTO BRILLANTE, que llega por el destejido de OP-D-07 y que es uno de los dos lados de la frontera declarada del 1298.

### EL REPARTO, PIEZA A PIEZA, TALLADO DEL PLAN SELLADO

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `decision_pivote_perseverar` | `CUBIERTO` | ya lo dice el paso **1** del superviviente |
| paso **2** de `decision_pivote_perseverar` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `decision_pivote_perseverar` | `INCISO` | **`INCISO` ADOSADO** al paso 1: *las expectativas cuantitativas definidas al inicio* |
| paso **4** de `decision_pivote_perseverar` | `INCISO` | **`INCISO` ADOSADO** al paso 3: *con datos concretos en la sala, no solo con intuición* |
| condicion **1** de `decision_pivote_perseverar` | `CUBIERTO` | ya lo dice la condicion **1** del superviviente |
| condicion **2** de `decision_pivote_perseverar` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **3** de `decision_pivote_perseverar` | `CUBIERTO` | ya lo dice la condicion **2** del superviviente |

### LAS PERDIDAS, SELLADAS EN CAMPO PROPIO (`CAMPO PROPIO v1`)

| especie | que se pierde | donde vivia | enrutada a |
|---|---|---|---|
| **DE PARAMETRO DE PASO** | el calificativo ACCIONABLES de las metricas que se revisan, y el rotulo de MODELO DE NEGOCIO SOSTENIBLE como destino; el paso 1 del superviviente dice tus metricas actuales y el modelo ideal de tu plan de negocio, que es el mismo gesto sin esos dos rotulos. SE DICE LO QUE NO SE PIERDE: metricas_accionables es HOY uno de los cinco nodos_previos del superviviente, medido en esta vuelta, asi que el concepto sigue a un salto del nodo vivo | paso 1 de decision_pivote_perseverar | la fase 04, que redacta y afina los pasos del superviviente |
| **DE CONDICIONES** | el disparador de que los experimentos de producto muestren efectividad DECRECIENTE; la condicion 1 del superviviente dispara porque las metricas clave NO MEJORAN tras varios ciclos, que es el mismo fenomeno sin la pendiente | condicion 1 de decision_pivote_perseverar | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| **DE CONDICIONES** | la imagen de la startup ATRAPADA EN LA TIERRA DE LOS MUERTOS VIVIENTES, que es el estado de ni crecer ni morir; la condicion 2 del superviviente dispara por haber agotado las mejoras posibles sin ver resultados, que es el mismo callejon dicho sin la imagen | condicion 3 de decision_pivote_perseverar | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |

### LAS REDIRECCIONES Y LAS GUARDAS, LEIDAS DE LA SALIDA DE LA EJECUCION

**Redirecciones sobre nodos VIVOS: 5.** Salen enteras de [`../loop/SALIDA_V63_OPM03I_EJEC.txt`](../loop/SALIDA_V63_OPM03I_EJEC.txt):

| nodo que nombraba al que muere | campo | pasa a nombrar |
|---|---|---|
| `catalogo_pivotes` | `nodos_previos` | `pivotar_o_perseverar` |
| `ciclo_crear_medir_aprender` | `nodos_siguientes` | `pivotar_o_perseverar` |
| `contabilidad_innovacion_pivote` | `nodos_siguientes` | `pivotar_o_perseverar` |
| `puntos_brillantes_antes_del_pivote` | `nodos_previos` | `pivotar_o_perseverar` |
| `reunion_pivotar_o_perseverar` | `nodos_previos` | `pivotar_o_perseverar` |

| guarda | resultado |
|---|---|
| **`P.16`, duplicadas que la propia fusion fabrica** | **0** |
| **auto-aristas que la fusion habria creado** | **0** |
| **guarda A**, cero auto-aristas nuevas | **OK (0)** |
| **guarda B**, cero duplicadas nuevas tras resolver | **OK (0)** |
| **guarda C**, los cinco campos que la operacion NO redacta, intactos | **5 de 5** |
| **guarda D**, el absorbido conserva su texto INTACTO | **OK** |

### LO QUE LA FICHA MANDABA COMPROBAR DESPUES DE FUNDIR, COMPROBADO

Sale de [`../loop/SALIDA_V63_VERIFICAR_OPM03I.txt`](../loop/SALIDA_V63_VERIFICAR_OPM03I.txt), corrida en esta vuelta:

```
1. LAS TRES PIEZAS PROPIAS DEL PAR, EN EL TEXTO FINAL DEL SUPERVIVIENTE
   racionalizacion del fracaso  OK   paso [6]
   linea base nueva             OK   paso [4]
   comprobacion posterior       OK   paso [5]
   el superviviente queda con 6 pasos y 3 condiciones
2. EL BLOQUE DEL PUNTO BRILLANTE, BYTE A BYTE EN SU NODO PROPIO
   pasos hoy: 5 | pasos antes: 5 | IDENTICOS BYTE A BYTE: SI
   fuente: 'Traction - Gabriel Weinberg' (antes 'Traction - Gabriel Weinberg')
   pasos del bloque que estaban en el que MUERE: 0 de 5 (la correccion declarada de la ficha decia 0 de 5)
3. LA ARISTA REDIRIGIDA AL SUPERVIVIENTE, CON SU ESPEJO
   ANTES: el que muere lo nombraba en nodos_siguientes: True | el nodo propio nombraba al que muere en nodos_previos: True
   HOY  : el superviviente lo nombra en nodos_siguientes: True | el nodo propio nombra al superviviente en nodos_previos: True
   el id del muerto ya NO aparece en el nodo propio: True
4. EL NODO PROPIO SIGUE VIVO
   deprecado: None | VIVO: SI
5. EL ALIAS DEL SUPERVIVIENTE CARGA EL ID QUE MUERE
   ids_alias: ['decision_pivote_perseverar']
   merged_originals: ['decision_pivote_perseverar']
6. EL ABSORBIDO, DEPRECADO Y CON SU TEXTO INTACTO
   deprecado: SI | texto y aristas INTACTOS: SI
```

### LAS DOS DIVERGENCIAS ENTRE LA SIMULACION SELLADA Y LA MEDICION DE HOY, DECLARADAS

**LA FICHA SE SELLO EL 12 AGO 2026 Y SU SIMULACION ES DE ESE DIA.** Entre aquel dia y hoy el grafo se movio, y **las dos diferencias se declaran en vez de taparse, porque ninguna cambia el superviviente**:

| | lo que la ficha sellada dice | **lo medido HOY** | por que difiere |
|---|---|---|---|
| **entradas que se redirigen** | **4**: `catalogo_pivotes`, `ciclo_crear_medir_aprender`, `contabilidad_innovacion_pivote` y `reunion_pivotar_o_perseverar` | **5**: las cuatro **mas** `puntos_brillantes_antes_del_pivote` | ese nodo **NACIO EL 14 AGO 2026** por `OP-F-04-WEI`, dos dias DESPUES de la simulacion sellada. **Es exactamente la arista que la correccion declarada de la propia ficha manda redirigir**, y el cotejo de las dos listas es identidad mas ese unico anadido |
| **cableado** | **6 contra 4** | **6 contra 5** | la entrada que el que muere gano es la misma de arriba. **El superviviente sigue ganando** |

**Y UNA TERCERA DIFERENCIA, QUE NO ES DE MEDICION SINO DE LECTURA, Y VA MARCADA DISCUTIBLE EN EL REPORTE DE ESTA VUELTA.** La ficha adjudica *por CABLEADO A CONTENIDO EMPATADO*. **Leido con las varas por forma que los seis tramos de `OP-U-01` usaron, el contenido de hoy NO empata entero:** pasos **5 contra 4** apunta al superviviente y condiciones **2 contra 3** apunta al que muere, o sea **`CHOCAN`**. Y en un `CHOCAN` **decide la pieza DECLARADA** (acta 53, pregunta 3), que aqui es **la adjudicacion sellada de la propia ficha** y nombra a `pivotar_o_perseverar` con todas sus letras. **LAS DOS VIAS CONVERGEN EN EL MISMO NODO**, y por eso esto es una divergencia declarada y no una parada.

### `P.16` CONTRA LA LETRA DE LA FICHA, Y LA DIVERGENCIA YA ESTABA ADJUDICADA

La ficha de esta operacion **no manda nada sobre duplicadas**; la de `OP-M-02-PROG` si, y dice que **las duplicadas que la fusion fabrique quedan para `OP-S-12`**. **`P.16` (adoptada el 14 ago 2026, decision del fundador) dice lo contrario: quien fabrica, limpia, en el mismo commit**, y su punto 3 convierte a `OP-S-12` en **VERIFICACION DE CERO**. **La divergencia la declaro el instrumento de fundir desde la vuelta 48 y con ella se ejecutaron los seis tramos de `OP-U-01`**, auditados vuelta a vuelta. **Aqui no hizo falta**: esta fusion fabrico **CERO** duplicadas y **CERO** auto-aristas, medido antes de limpiar.


---

## `OP-M-02-PROG`: EL REGISTRO DE LA FUSION (2026-08-20, vuelta 63)

**Cada celda de este registro sale de un instrumento corrido en la vuelta 63 y pegada entera**, con el comando citado al lado. **El registro se adosa al final de la pagina y NO reescribe ni una linea de arriba.**

| | |
|---|---|
| **la ficha** | `docs/plan/OPERACIONES.jsonl`, tipo **FUSION DE MESA**, estado **LISTA**, fecha de corte **2026-08-12** |
| **superviviente** | `ocho_fases_experiencia_cliente` |
| **absorbe** | `fases_de_retencion_de_clientes` |
| **plan sellado** | [`../loop/PLAN_V63_OPM02PROG.json`](../loop/PLAN_V63_OPM02PROG.json), contrato **`CAMPO PROPIO v1`** |
| **censo del catalogo** | ANTES 3853 ficheros, 3273 vivos, 580 deprecados . DESPUES 3853 ficheros, 3272 vivos, 581 deprecados . **delta de deprecados +1 (esperado +1): OK** |
| **el superviviente** | 4 -> 5 (anadidos 1), condiciones 1 -> 2 (anadidas 1) |
| **piezas repartidas** | **5 (2 viajan enteras, 3 ya estaban dichas)** |

**LA ADJUDICACION, COPIADA VERBATIM DE LA FICHA Y NO REDACTADA AQUI:**

> EL PROGRAMA UNICO. Sobrevive ocho_fases_experiencia_cliente POR CABLEADO SIN EMPATE. SIMULADO el 12 ago 2026: lo nombran 13 nodos contra 3, y tiene 4 pasos contra 3. LAS DOS PRIORIDADES VIAJAN al superviviente.

### EL REPARTO, PIEZA A PIEZA, TALLADO DEL PLAN SELLADO

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `fases_de_retencion_de_clientes` | `CUBIERTO` | ya lo dice el paso **1** del superviviente |
| paso **2** de `fases_de_retencion_de_clientes` | `CUBIERTO` | ya lo dice el paso **2** del superviviente |
| paso **3** de `fases_de_retencion_de_clientes` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `fases_de_retencion_de_clientes` | `CUBIERTO` | ya lo dice la condicion **1** del superviviente |
| condicion **2** de `fases_de_retencion_de_clientes` | `APPEND` | **viaja ENTERA** al superviviente |

### LAS PERDIDAS, SELLADAS EN CAMPO PROPIO (`CAMPO PROPIO v1`)

| especie | que se pierde | donde vivia | enrutada a |
|---|---|---|---|
| **DE PARAMETRO DE PASO** | el parentesis NO SOLO PARA ASSESS Y ADMIT, que es la advertencia de que el diseno no puede pararse en las dos fases previas a la venta; y el encuadre de ACCIONES ESPECIFICAS DE LA EMPRESA frente al de EXPERIENCIA EMOCIONAL DESEADA del paso 2 del superviviente. SE DICE LO QUE NO SE PIERDE: el gesto de disenar para CADA UNA DE LAS OCHO FASES esta entero en ese paso 2, y el plan de accion concreto es el paso 4 del superviviente. NO SE ADOSA DE INCISO porque el paso 2 del superviviente cierra en punto y la guarda de la juntura lo rechaza | paso 2 de fases_de_retencion_de_clientes | la fase 04, que redacta y afina los pasos del superviviente |

### LAS REDIRECCIONES Y LAS GUARDAS, LEIDAS DE LA SALIDA DE LA EJECUCION

**Redirecciones sobre nodos VIVOS: 3.** Salen enteras de [`../loop/SALIDA_V63_OPM02PROG_EJEC.txt`](../loop/SALIDA_V63_OPM02PROG_EJEC.txt):

| nodo que nombraba al que muere | campo | pasa a nombrar |
|---|---|---|
| `estrategia_de_ventas` | `nodos_previos` | `ocho_fases_experiencia_cliente` |
| `ocho_fases_experiencia_cliente` | `nodos_siguientes` | `ocho_fases_experiencia_cliente` |
| `pensamiento_h2h` | `nodos_siguientes` | `ocho_fases_experiencia_cliente` |

| guarda | resultado |
|---|---|
| **`P.16`, duplicadas que la propia fusion fabrica** | **1** |
| **auto-aristas que la fusion habria creado** | **1** |
| **guarda A**, cero auto-aristas nuevas | **OK (0)** |
| **guarda B**, cero duplicadas nuevas tras resolver | **OK (0)** |
| **guarda C**, los cinco campos que la operacion NO redacta, intactos | **5 de 5** |
| **guarda D**, el absorbido conserva su texto INTACTO | **OK** |

### LO QUE LA FICHA MANDABA COMPROBAR DESPUES DE FUNDIR, COMPROBADO

Sale de [`../loop/SALIDA_V63_VERIFICAR_OPM02PROG.txt`](../loop/SALIDA_V63_VERIFICAR_OPM02PROG.txt), corrida en esta vuelta:

```
1. LAS DOS PRIORIDADES, EN EL TEXTO DEL SUPERVIVIENTE
   Affirm       OK   paso [5]
   Activate     OK   paso [5]
   el superviviente queda con 5 pasos y 2 condiciones (antes 4 y 1)
2. LAS PIEZAS PROPIAS DEL QUE MUERE, UNA POR UNA
   paso 3, la priorizacion de Affirm y Activate   OK   indice [5]
   condicion 2, reducir el abandono temprano      OK   indice [2]
3. LAS DOS PIEZAS QUE VIVEN DENTRO, INTACTAS Y NO TOCADAS
   detectar en que fase se atascan      OK   hoy en el paso [3] (antes [3])
   el plan de avance                    OK   hoy en el paso [4] (antes [4])
4. EL ALIAS DEL SUPERVIVIENTE CARGA EL ID QUE MUERE
   ids_alias: ['fases_de_retencion_de_clientes'] | merged_originals: ['fases_de_retencion_de_clientes']
5. EL ABSORBIDO, DEPRECADO Y CON SU TEXTO INTACTO
   deprecado: SI | texto y aristas INTACTOS: SI
6. LA DUPLICADA QUE LA FUSION FABRICABA, MEDIDA EN EL TESTIGO
   ANTES, pensamiento_h2h en nodos_siguientes nombraba a los DOS miembros: True
   HOY  : lo nombra 1 vez(veces) y al muerto 0
   AUTO-ARISTA: el superviviente se nombra a si mismo: False (tiene que ser False)
```

### LA DIVERGENCIA CON LA LETRA DE LA FICHA, DECLARADA: `P.16` CONTRA *QUEDAN PARA `OP-S-12`*

**LA FICHA DICE, en su campo `verificacion`:** *las duplicadas que la fusion fabrica quedan para `OP-S-12`, que corre despues*. **`P.16`, adoptada el 14 ago 2026 por decision del fundador y por tanto DOS DIAS POSTERIOR a esta ficha, dice lo contrario y con todas sus letras:** *toda operacion de fusion retira, en su mismo commit, la arista interna del par que su propia simulacion reporta*; y **su punto 3 convierte a `OP-S-12` en VERIFICACION DE CERO** en vez de en limpieza.

**QUE SE HIZO, y por que no es una parada:** se siguio **`P.16`**, que es la regla mas reciente. **No es una decision de esta vuelta: es el carril que el instrumento de fundir declara desde la vuelta 48 y con el que se ejecutaron los SEIS tramos de `OP-U-01`**, auditados vuelta a vuelta. Ademas, **`AUDITOR.md` seccion 3 pone como guarda obligatoria de la fase III *cero duplicadas o auto-aristas tras resolver***, que es lo mismo que `P.16` pide. **VA MARCADO COMO DISCUTIBLE EN LA SECCION 6 DEL REPORTE DE ESTA VUELTA.**

**LO QUE SE MIDIO, y es lo que hace verificable la eleccion:**

| | |
|---|---|
| **la duplicada que la fusion fabricaba** | `pensamiento_h2h` en `nodos_siguientes`, que nombraba a los DOS miembros. **Medida ANTES de limpiarla** |
| **la auto-arista que la fusion creaba** | `ocho_fases_experiencia_cliente` en `nodos_siguientes`, que se nombraba a si mismo por alias. **Medida ANTES de retirarla** |
| **las dos, despues** | el testigo nombra al superviviente **UNA sola vez** y al muerto **CERO**; el superviviente **NO** se nombra a si mismo |
| **el pasivo historico ajeno** | **NO SE TOCA**: 927 grupos antes y 927 despues, con el `diff` por resolutor dando **CERO fabricados y CERO renombrados** |

**Y UNA COSA QUE PARECE UNA DISCREPANCIA ENTRE DOS INSTRUMENTOS Y NO LO ES, dicha porque leerla mal cuesta una vuelta:** `simular_fusion.py` reporta **UNA duplicada nueva** y `retirar_duplicada_por_resolutor.py` (el instrumento de `P.16` que corre ANTES de fundir) reporta **NINGUNA**. **No se contradicen: el segundo dice en su propio docstring que SALTA A PROPOSITO el caso que el ejecutor de fusiones deduplica solo**, y persigue unicamente las que llegan por una cadena de alias y sobrevivirian. Esta es de las primeras: `pensamiento_h2h` trae los dos ids **literalmente** en su lista, asi que la sustitucion del ejecutor la funde y la dedupica en el sitio. **El ejecutor la conto y la imprimio antes de limpiarla**, que es lo que `P.16` exige.


---

## `OP-U-02`: **LA APERTURA MEDIDA, SIN FUNDIR NI UN ACTO** (20 ago 2026, vuelta 63)

**Esto NO ejecuta `OP-U-02`: la MIDE.** Ni un acto suyo se funde en esta vuelta. **La nomina queda FIJADA en fichero propio**, [`../loop/NOMINA_OPU02_V63.jsonl`](../loop/NOMINA_OPU02_V63.jsonl), **una fila por acto abierto con sus miembros**, y sale entera de `python scripts/loop/abrir_universo_de_opu02.py` ([`../loop/SALIDA_V63_APERTURA_OPU02.txt`](../loop/SALIDA_V63_APERTURA_OPU02.txt)).

**EL INSUMO ES EL RECOMPUTO CORRIDO EN ESTA MISMA VUELTA**, no un fichero sellado viejo: [`../loop/_v63_componentes_cierre.jsonl`](../loop/_v63_componentes_cierre.jsonl), medido DESPUES de las dos fusiones de mesa. **Y por `P.1`, el instrumento RESUELVE POR ALIAS ANTES DE CONTAR**, o contaria como libre un acto cuyo miembro ya fue absorbido.

| | |
|---|---:|
| **actos abiertos, medidos hoy** | **53** sobre **240** nodos |
| **`OP-U-02` ABRE** (criterio del propio plan: sin dueno en mesa ni destejido) | **47** actos sobre **201** nodos |
| **quedan FUERA, con dueno en otra fase** | **6** actos sobre **39** nodos |
| **los que ABREN, por tamano** | **1** de 15, **1** de 10, **1** de 8, **4** de 6, **7** de 5, **10** de 4, **23** de 3 |

### LOS QUE QUEDAN FUERA, CADA UNO CON SU DUENO NOMBRADO Y SU CITA

| tamano | dueno | miembros |
|---:|---|---|
| **13** | `OP-M-01`, `OP-M-01-FUSION` | `decision_factory_mentality`, `equipos_dedicados_de_proyecto`, `estructura_de_gates`, `estructura_gates`, `gates_go_kill_decision_points`, `gestion_de_portafolio_gates_go_kill`, `gestion_portafolio_dos_niveles`, `gestion_portafolio_foco`, `gestion_portafolio_formal`, `portfolio_management`, `requisitos_gates_con_dientes`, `revision_portafolio_periodica`, `sistema_gates_go_kill` |
| **9** | `OP-M-05`, `OP-M-05-EDIFICIO`, `OP-M-05-INDICE` | `customer_development_modelo`, `customer_discovery`, `customer_discovery_cuatro_fases`, `customer_discovery_get_out_of_building`, `customer_discovery_introduccion`, `customer_discovery_overview`, `desarrollo_de_clientes_customer_development`, `get_out_of_the_building`, `manifiesto_regla1_hechos_fuera_del_edificio` |
| **7** | `OP-M-05-APERTURA` | `customer_validation`, `customer_validation_sell_phase`, `earlyvangelists_ventas_tempranas`, `filosofia_customer_validation`, `filosofia_validacion_clientes`, `get_out_building_test_sell`, `introduccion_validacion_clientes` |
| **4** | `OP-M-04` | `formalizar_junta_asesora`, `formalize_advisory_board`, `identificar_consejo_asesores`, `identificar_junta_asesores` |
| **3** | `OP-D-02` | `homework_frontend_loading`, `voice_of_customer_homework`, `voz_del_cliente_voc` |
| **3** | `OP-M-03-III` | `pivote_estrategico`, `pivote_startup`, `pivotes_e_iteraciones` |

### **LA FRASE DE LA LINEA 226 ESTA ENVEJECIDA, Y SE DICE EN VEZ DE CALLARLO**

**El texto de arriba (lineas 226 a 228, leidas HOY y cotejadas por este mismo instrumento antes de escribir) dice que CUATRO abiertos no se resuelven aqui nunca**: el de 13 y el de 9 a mesa, y **dos grandes a destejido**. **La ficha de `OP-U-02` en [`OPERACIONES.jsonl`](OPERACIONES.jsonl) ya lo habia corregido en la vuelta 13 y dice OCHO.** **Lo medido HOY reconcilia las dos y no elige entre ellas:**

| los OCHO que la ficha nombra | como estan HOY |
|---|---|
| **seis de ellos** (el de 13, el de 9, el de 7 de `customer validation`, el de la junta asesora, el de la voz del cliente y el del pivote) | **siguen ABIERTOS y quedan fuera por su dueno**, y son exactamente los seis de la tabla de arriba |
| **los DOS de destejido** (`OP-D-03` y `OP-D-04`) | **YA NO SON ACTOS: no aparecen en NINGUNA componente del recomputo de hoy, ni abierta ni cerrada** |

**Y LA DESAPARICION DE ESOS DOS NO SE SUPONE: SE MIDE, Y LAS DOS CAUSAS SON DISTINTAS** ([`../loop/SALIDA_V63_DESTEJIDOS_COMPROBADOS.txt`](../loop/SALIDA_V63_DESTEJIDOS_COMPROBADOS.txt)):

| | lo medido | la causa |
|---|---|---|
| **`OP-D-04`** | sus **7** nodos resuelven HOY a **2** supervivientes, los dos vivos | **la componente se consumio POR FUSION** |
| **`OP-D-03`** | sus **6** nodos siguen **VIVOS** y **ninguno resuelve a otro** | **lo que desaparecio no son los nodos: son LAS ARISTAS `A`**. Los **8** pares internos que el archivo tiene entre ellos son **8 de clase `D`**, y una componente de este recomputo se forma **solo con aristas `A`** |

> **UNA CIFRA MAS QUE CAMBIO Y VA DICHA:** la ficha de la vuelta 13 llamaba **de tamano 4** al acto de la voz del cliente; **hoy mide 3**. Es un acto que encogio, no una cuenta mal hecha, y por eso la tabla de arriba publica **3** y esta nota publica la diferencia.

> **LO QUE ESTA APERTURA NO HACE, dicho para que nadie se lo atribuya: NO elige superviviente, NO reparte piezas, NO declara ningun acto y NO funde nada.** Fija quien entra en el universo y quien no, con su motivo citado. **La fusion de esos 47 actos es trabajo de la vuelta que la ejecute.**



---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 63, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (20 ago 2026, vuelta 64, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **CUATRO** veces: las tres adjudicaciones del acta 52 (linea **1250**),
la del acta 57 sobre el acto 25 (**2475**), las del acta 61 (**2689**) y las del acta 62 (**2933**),
**las cuatro cotejadas HOY abriendo el fichero**. **Ninguna cifra publicada se toca.** **Cada cita
lleva la linea LEIDA HOY**, no recordada, y **las treinta y tres se imprimieron y se compararon antes
de escribir esta seccion** con `python scripts/loop/vuelta64_registrar_acta63.py --simular`, que cae
en `ROJO` sin escribir si una sola no calza: el acta de la vuelta 63 abre en la linea **16274** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), su seccion de adjudicaciones en la **16432**,
la de las cinco preguntas en la **16502**, la del hallazgo de las consumidas en la **16547** y la
del orden del puesto 2 en la **16583**.

### a) **LOS NUEVE DISCUTIBLES ADJUDICADOS `A FAVOR`, CADA UNO CON LA VARA QUE LO SOSTIENE**

**Fueron DIEZ los marcados y NUEVE los adjudicados**: el decimo, el `D10`, quedo a **relectura
conjunta** y se resuelve en el apartado **e)** de aqui abajo. La columna de la vara **no es una
glosa: es la regla citable con la que el auditor lo adjudico**, y va copiada de su linea.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | **exigio `--operacion` y declaro los insumos en un generador de nombre estable**, con lo que el comando viejo cae en `ROJO` | **acta 61, `D2`**, con sus dos condiciones comprobadas (docstring enumerado con nota fechada, marcado discutible). Y **que el comando viejo caiga en `ROJO` es fallar ruidoso**, canon de la casa (banco seccion 9): *un generador que sella planes no puede adivinar la operacion* | **16434** |
| **`D2`** | **corrigio el sellador dos vueltas seguidas** | **la prueba 2 del caso positivo lo mide**: la cabecera corregida da **21 y 42 IDENTICOS** a los planes ya sellados, o sea que **la correccion honra el conteo**. El riesgo de tocar el sellador es real **y la mitigacion tambien esta medida**: el censo re-corrido da cero tallados y el texto viejo queda citado entero | **16440** |
| **`D3`** | **estreno DOS instrumentos estables y los uso el mismo dia** | `fundir_por_plan.py` es **sucesor declarado POR EXTRACCION con un `assert` por cambio** (sha1 del ancestro medido por el auditor), y el caso positivo nuevo **aisla NUEVE guardas y las nueve muerden**. **La alternativa real era correr el ancestro con `OP-U-01` TALLADO en el titulo**, que es la especie que la regla 1 prohibe | **16446** |
| **`D4`** | **ejecuto `OP-M-03-I` con una ficha cuya medicion habia envejecido** | **las dos vias convergen medidas hoy**: el `CHOCAN` de las varas por forma lo decide **la pieza declarada** (acta 53, pregunta 3), que es la adjudicacion sellada, y nombra al mismo nodo. **La regla general queda escrita en el apartado b)** | **16452** |
| **`D5`** | **siguio `P.16` contra la letra de la ficha Y del encargo** | **`P.16` es posterior** (14 contra 12 de ago), **es decision del fundador**, su punto 3 hace de `OP-S-12` una verificacion de cero, y `AUDITOR.md` seccion 3 exige cero duplicadas tras resolver como guarda de la fase III. **Una linea de encargo no deroga doctrina del fundador** | **16457** |
| **`D6`** | **ejecuto con las simulaciones selladas descuadradas** | **la regla 1 leida entera**: la simulacion sellada es una nota vieja, se cita como contraste, y la de HOY se corrio y se cotejo **con las tres diferencias medidas y explicadas**, y ninguna cambia superviviente ni reparto. **Re-sellar fichas no es del ejecutor** | **16464** |
| **`D7`** | **sello una perdida que su ficha NIEGA** | el parentesis **no esta en ningun paso del superviviente de hoy**, medido sobre el json vivo, y la pasada de perdidas de la ficha es del **12 ago**, ANTERIOR al contrato `CAMPO PROPIO v1`. **La cifra de perdidas se mide contra el texto de hoy**; la afirmacion vieja se declara como contraste. **Eso no es re-abrir la ficha: es no copiarla** | **16471** |
| **`D8`** | **marco `CUBIERTO` con perdida sellada por el calificativo ACCIONABLES** | `A FAVOR` **con el limite dicho**: la perdida SELLADA es la mitad auditable y esta; el atenuante de grafo (`metricas_accionables` es nodo previo del superviviente) **es contraste medido y NO descuenta el sello**. *Una perdida con atenuante declarado es mas auditable que un silencio, no menos* | **16477** |
| **`D9`** | **cambio la vara del censo despues de ver su resultado** | `A FAVOR` **con la guarda cumplida**: la vara final es mas estrecha, **la lista `DEBIL` publica todo lo que la estrecha deja fuera**, el unico `TALLADO` de la vara nueva tambien estaba entre los once de la vieja, y **es medicion re-corrible, no doctrina**. *Lo que la salva es la publicacion de la lista `DEBIL`: sin ella seria fabricar la vara* | **16483** |

### b) **LA REGLA DE LA FICHA ENVEJECIDA**, escrita entera porque manda sobre todas las mesas que quedan

**No es doctrina nueva y el acta lo dice al adjudicarla** (linea **16504**): sale por extension
citable de **la regla 1 de `EJECUTOR.md`** (*una nota vieja NUNCA es fuente: se cita como contraste y
la discrepancia se declara*) y del **acta 53, pregunta 3** (*el `CHOCAN` lo decide la pieza
declarada*). **Su letra, tal como la vuelta 64 la aplica:**

> **Las mediciones selladas de una ficha se RE-CORREN el dia de la ejecucion.**
>
> - **Si TODAS las vias medidas hoy** (varas por forma, pieza declarada, correccion declarada si la
>   hay) **convergen en el MISMO superviviente y el MISMO reparto: SE EJECUTA**, con la divergencia
>   **declarada en el motivo** del plan.
> - **Si CUALQUIER via cambia el superviviente**, o **la pieza declarada ya no existe medida hoy**, o
>   **el objeto de la ficha ya fue consumado por otra operacion ejecutada y auditada: NO SE EJECUTA.**
>   Se trae al auditor con la medicion.
> - **Y si lo consumado es el caso, la ficha no se ejecuta ni se rehace: se declara CONSUMIDA por
>   correccion declarada** citando el registro que la consumio (carril del banco `9.10`), **porque
>   deshacer una fusion registrada y auditada seria decision de fundador.**

**Vale para las fusiones de mesa restantes con fichas del 12 ago 2026**, que son todas las que
quedan. **La vuelta 64 la aplica dos veces**: en las cinco consumidas del apartado **d)** y en
`OP-M-03-II`, cuya ejecucion re-corrio sus mediciones antes de fundir.

### c) **EL ORDEN DEL PUESTO 2 DE LA FASE 03, ADJUDICADO CON LA VARA DE LA VUELTA 47**

**Le tocaba al auditor por la decision del fundador del 19 ago 2026** (linea **64** de este mismo
documento) **y habia criterio citable**, asi que se adjudico en vez de subir a mesa. **La vara es la
general de la vuelta 47: lo que cada operacion desbloquea, escrito en el `depende_de` de las demas.**
`CONGELADOS LIBERADOS` literal **empata a las tres en cero** y por eso no separa.

**LA TABLA NO ESTA TECLEADA: sale entera de `python scripts/loop/vuelta64_puesto2.py`**
([`../loop/SALIDA_V64_PUESTO2.txt`](../loop/SALIDA_V64_PUESTO2.txt)), **que la mide de
`OPERACIONES.jsonl` en esta vuelta y no la copia del acta**:

| puesto | operacion | **desbloquea** | cuales, leidas de su `depende_de` | estado HOY |
|---:|---|---:|---|---|
| **1.a** | `OP-M-02-MEDIOS` | **5** | `OP-M-02-ASSESS`, `OP-M-02-ADMIT`, `OP-M-02-ACTIVATE`, `OP-M-02-ACCLIMATE`, `OP-M-02-ACCOMPLISH` | **CONSUMIDA**, su par ya resuelve a un solo vivo |
| **2.a** | `OP-M-03-II` | **4** | `OP-M-03-ENLACES`, `OP-M-05-INDICE`, `OP-M-05-EDIFICIO`, `OP-M-05-APERTURA` | ejecutable, 2 miembros a 2 vivos |
| **3.a** | `OP-U-02` | **1** | `OP-E-03` | ejecutable; **SIN nomina de nodos en su ficha**, su universo se abre aparte |

**EL PUESTO 2 QUEDA: `OP-M-02-MEDIOS`, despues `OP-M-03-II`, despues `OP-U-02`.** Y como
`OP-M-02-MEDIOS` **esta CONSUMIDA** (apartado **d**), **su resolucion es la correccion declarada y
LA PRIMERA FUSION EJECUTABLE DEL PUESTO ES `OP-M-03-II`**, que es la que esta vuelta ejecuta.
**Medido por el propio instrumento:** `OP-M-03-II`.

### d) **EL HALLAZGO PROPIO DEL AUDITOR: CINCO FUSIONES DE MESA YA CONSUMIDAS POR LOS TRAMOS DE `OP-U-01`, DOS CON EL SUPERVIVIENTE OPUESTO**

**El auditor lo midio con instrumento propio** (acta 63, seccion 6, linea **16547**) **y el ejecutor
lo volvio a medir por camino propio antes de escribir una sola correccion**, que es lo que el
protocolo de relectura conjunta pide. **LA TABLA SALE ENTERA de
`python scripts/loop/vuelta64_consumidas.py`**
([`../loop/SALIDA_V64_CONSUMIDAS.txt`](../loop/SALIDA_V64_CONSUMIDAS.txt)), **con los alias
resueltos por `P.1` y con las celdas de `acto`, `lote`, `sobrevive` y `absorbe` leidas POR EL NOMBRE
DE SU COLUMNA en la cabecera de cada tabla citada, nunca de la prosa de alrededor**:

| ficha | superviviente de la **ficha** (12 ago) | el que quedo **VIVO** | coinciden | quien la consumio | linea |
|---|---|---|:---:|---|---:|
| `OP-M-02-MEDIOS` | `seis_medios_comunicacion_cliente` | `estrategia_multicanal_bienvenida` | **NO** | `OP-U-01`, TRAMO 3, vuelta 56, acto 32, lote B | **2091** |
| `OP-M-02-ASSESS` | `fase_assess_ciclo_cliente` | `fase_assess_ciclo_cliente` | si | `OP-U-01`, TRAMO 2, vuelta 55, acto 30, lote A | **1832** |
| `OP-M-02-ADMIT` | `fase_admit` | `fase_admit_celebracion` | **NO** | `OP-U-01`, TRAMO 2, vuelta 55, acto 38, lote B | **1840** |
| `OP-M-02-ACTIVATE` | `fase_activate_primera_impresion` | `fase_activate_primera_impresion` | si | `OP-U-01`, TRAMO 1, vuelta 48, acto 44 | **417** |
| `OP-M-02-ACCOMPLISH` | `fase_accomplish_experiencia_cliente` | `fase_accomplish_experiencia_cliente` | si | `OP-U-01`, TRAMO 3, vuelta 56, acto 9, lote A | **2069** |

**LAS DOS MEDICIONES CALZAN.** La del auditor situa `OP-M-02-MEDIOS` en el tramo 3, vuelta 56, lote
B, acto 32, linea **2091**, con su perdida sellada en la **2132**; **la corrida propia da lo mismo al
digito**, y las otras cuatro quedan situadas por el mismo camino.

**LA ADJUDICACION, con las reglas ya escritas y sin estrenar ninguna:** las fusiones de los tramos
son **cosa juzgada** (planes sellados, verificadas por las actas 56 a 62); **deshacerlas seria
decision de fundador y nadie la pide**. **Las cinco fichas NO SE EJECUTAN NI SE REHACEN: se declaran
CONSUMIDAS por correccion declarada** (banco `9.10`) **en el campo `nota` de cada una**, citando el
registro del tramo que la consumio. **Y la divergencia de superviviente de `MEDIOS` y `ADMIT` se
DECLARA como contraste en vez de resolverse copiando** (regla 1): **la adjudicacion del 12 ago queda
entera y sin tachar, y lo que se declara es que NO FUE LA QUE SE EJECUTO.** **NADA DEL GRAFO SE
TOCA**: la correccion es de registro.

> **POR QUE LA CORRECCION VA EN EL CAMPO `nota` Y NO EN UNA CLAVE NUEVA, dicho para que no parezca
> descuido:** el esquema de `OPERACIONES.jsonl` es **un pendiente de doctrina heredado** (acta 55,
> seccion 5, cierre) y **estrenar clave en 5 de las 71 fichas seria decidirlo de tapadillo**. El
> campo `nota` es ademas el sitio que estas mismas fichas ya usan: `OP-F-01`, `OP-D-01`, `OP-D-03`,
> `OP-D-04`, `OP-S-06`, `OP-S-07`, `OP-C-04` y `OP-U-01` traen ahi su correccion declarada.

> **LA PREGUNTA QUE EL AUDITOR DEJO MEDIDA PERO NO CERRADA, y que se registra para que el cierre de
> la fase 03 la tenga delante:** la nomina de la vuelta 48 incluyo **cinco pares con dueno de mesa**,
> y **no hay regla escrita que mandara excluirlos de `OP-U-01`**. No es caida de nadie. Queda dicha.

### e) **`D10`, LA RELECTURA CONJUNTA: SE SELLA**

**El caso del auditor** (linea **16489**): la condicion 1 de `fases_de_retencion_de_clientes` quedo
`CUBIERTO:1` **sin perdida sellada**, y **ese mismo dia `OP-M-03-I` sello DOS perdidas `DE
CONDICIONES` por la misma especie**, el matiz del disparador que muere sin sello. **El auditor no
adjudico: mando verificar contra el grafo y decidir con la vara** del acta 55, pregunta 5.

**MEDIDO HOY sobre el json vivo** con `python scripts/loop/vuelta64_d10.py`
([`../loop/SALIDA_V64_D10.txt`](../loop/SALIDA_V64_D10.txt)):

| | el texto de HOY |
|---|---|
| **muere** (condicion 1 de `fases_de_retencion_de_clientes`) | *Cuando la empresa solo tiene procesos disenados para atraer y cerrar ventas, pero no para despues de la compra* |
| **sobrevive** (condicion 1 de `ocho_fases_experiencia_cliente`) | *Cuando el usuario necesita una estructura sistematica para gestionar la experiencia del cliente despues de la venta* |

**LA BUSQUEDA NEGATIVA SE CORRIO EN VEZ DE CITARSE** (regla 9): las **cinco** agujas del encuadre del
sintoma (*atraer*, *cerrar venta*, *cerrar la venta*, *solo tiene proceso*, *procesos dise*) salen
**AUSENTES sobre el json ENTERO del superviviente**, no solo sobre sus condiciones.

**LA DECISION: SE SELLA.** **Y el `CUBIERTO` se sostiene y no se remarca**, que es la mitad que el
auditor ya daba por buena: el disparador operativo, **el DESPUES DE LA VENTA**, esta en la condicion
1 del superviviente con todas sus letras. **Lo que se anade es el sello de la mitad que muere**, el
**encuadre del sintoma**, que es el diagnostico por el que un lector se reconoce a si mismo.

**LA VARA, leida entera** (acta 55, pregunta 5): *las perdidas de condiciones no van de `APPEND` por
defecto, y la perdida NOMBRADA es el carril mientras el pendiente del `INCISO` de condiciones siga
abierto*. **Esa vara reparte DOS marcas y no una**: `APPEND` cuando el disparador es **distinto**, y
`CUBIERTO` **con la perdida nombrada** cuando es el **mismo** disparador con un matiz que muere.
**Lo que la vara no contempla en ninguna de sus dos ramas es el `CUBIERTO` CON SILENCIO.** Y es **la
misma especie** que las dos hermanas que `OP-M-03-I` sello el mismo dia (*el mismo fenomeno sin la
pendiente*, *el mismo callejon sin la imagen*): **tratar igual lo medido igual dentro de la misma
vuelta** es la regla de trabajo **declarada y uniforme** del acta 55, pregunta 4.

> **CORRECCION DECLARADA (2026-08-20, vuelta 64, TAREA 1.b del encargo, por el carril del banco
> `9.10`; el texto viejo se queda entero y no se tacha).** **La seccion `LAS PERDIDAS, SELLADAS EN
> CAMPO PROPIO` del registro de `OP-M-02-PROG` (linea 3189) publica UNA sola fila, la `DE PARAMETRO
> DE PASO` de la linea 3193. HOY SON DOS.** La segunda es **`DE CONDICIONES`**, vive en la
> **condicion 1 de `fases_de_retencion_de_clientes`** y va **enrutada a la fase 04, mientras el
> `INCISO` de condiciones no exista**. **La fila vieja no se toca y la tabla de arriba no se
> reescribe: esta nota la corrige.** El sello esta ademas en el campo `perdidas` del plan
> ([`../loop/PLAN_V63_OPM02PROG.json`](../loop/PLAN_V63_OPM02PROG.json)), con su correccion declarada
> adosada a `nota_del_reparto` **citando verbatim la frase que decia lo contrario**, y el tallador lo
> confirma por maquina: `python scripts/loop/tallar_perdidas_del_plan.py --plan ...` da **5 perdidas
> nombradas en los dos planes de la vuelta 63** (**3 `DE CONDICIONES`, 2 `DE PARAMETRO DE PASO`**),
> donde antes daba 4 ([`../loop/SALIDA_V64_TALLAR_PERDIDAS_V63.txt`](../loop/SALIDA_V64_TALLAR_PERDIDAS_V63.txt)).

### f) **LA CAIDA DE ACTA DEL AUDITOR, REGISTRADA CON SU NOMBRE**

**No se registra solo lo del ejecutor, y por eso esta aqui** (acta 63, seccion 3, linea **16416**).
**El encargo que el acta 62 dejo escrito decia con todas sus letras que en `OP-M-02-PROG` la
duplicada que la fusion fabrica quedaba para `OP-S-12`**, repitiendo la letra de una ficha del 12 ago
que **`P.16` (decision del fundador, 14 ago) contradice**; y **el MISMO encargo pedia en otra linea
el diff de duplicadas con CERO fabricadas**. **El ejecutor resolvio bien** (es el `D5` del apartado
**a**) **y ningun dato se movio**, pero **la linea era un error del encargo**. **Las caidas de acta
del auditor pasan de 5 a 6.**

**LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya: NO toca ni una cifra publicada
arriba, NO elige ningun superviviente, NO funde nada y NO deshace ninguna fusion.** Registra
adjudicaciones y corrige por declaracion.

---

## `OP-M-03-II`: EL REGISTRO DE LA FUSION (2026-08-20, vuelta 64)

**Cada celda de este registro sale de un instrumento corrido en la vuelta 64 y pegada entera**, con el comando citado al lado. **El registro se adosa al final de la pagina y NO reescribe ni una linea de arriba.**

| | |
|---|---|
| **la ficha** | `docs/plan/OPERACIONES.jsonl`, tipo **FUSION DE MESA**, estado **LISTA**, fecha de corte **2026-08-12** |
| **superviviente** | `pivote_o_proceder` |
| **absorbe** | `pivotar_o_proceder` |
| **plan sellado** | [`../loop/PLAN_V64_OPM03II.json`](../loop/PLAN_V64_OPM03II.json), contrato **`CAMPO PROPIO v1`** |
| **censo del catalogo** | ANTES 3853 ficheros, 3272 vivos, 581 deprecados . DESPUES 3853 ficheros, 3271 vivos, 582 deprecados . **delta de deprecados +1 (esperado +1): OK** |
| **el superviviente** | 7 -> 9 (anadidos 2), condiciones 1 -> 2 (anadidas 1) |
| **piezas repartidas** | **7 (3 viajan enteras, 3 ya estaban dichas)** |

**LA ADJUDICACION, COPIADA VERBATIM DE LA FICHA Y NO REDACTADA AQUI:**

> ACTO II, LA PUERTA DE LA REUNION DEL DESCUBRIMIENTO, DE BLANK. Sobrevive pivote_o_proceder POR CONTENIDO, y es la aplicacion mas dura de P.8 que hay en el plan: EL CABLEADO DICE LO CONTRARIO Y POR MUCHO, 10 contra 5 a favor de pivotar_o_proceder. Gana el contenido porque pivote_o_proceder lleva el material propio, el mapa del cliente y el resumen en un parrafo, y el otro no tiene nada que el superviviente no diga. LOS IDS SON EL MISMO NOMBRE EN DOS FORMAS Y VAN A LA DECISION 4.

### EL REPARTO, PIEZA A PIEZA, TALLADO DEL PLAN SELLADO

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `pivotar_o_proceder` | `CUBIERTO` | ya lo dice el paso **1** del superviviente |
| paso **2** de `pivotar_o_proceder` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `pivotar_o_proceder` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `pivotar_o_proceder` | `INCISO` | **`INCISO` ADOSADO** al paso 7: *hacia la validación con clientes* |
| paso **5** de `pivotar_o_proceder` | `CUBIERTO` | ya lo dice el paso **7** del superviviente |
| condicion **1** de `pivotar_o_proceder` | `CUBIERTO` | ya lo dice la condicion **1** del superviviente |
| condicion **2** de `pivotar_o_proceder` | `APPEND` | **viaja ENTERA** al superviviente |

### LAS PERDIDAS, SELLADAS EN CAMPO PROPIO (`CAMPO PROPIO v1`)

| especie | que se pierde | donde vivia | enrutada a |
|---|---|---|---|
| **DE PARAMETRO DE PASO** | el proposito declarado de la reunion, A EVALUAR CON CALMA EN QUE PUNTO ESTAS, y el rotulo de SOCIO O INVERSOR como quienes se sientan; el paso 1 del superviviente convoca a quien te acompana y suma a los inversores, pero no dice A QUE se sientan ni pide calma. SE DICE LO QUE NO SE PIERDE: el gesto de no decidirlo solo esta entero en ese paso 1, y a que se sientan lo dicen los seis pasos que siguen. NO SE ADOSA DE INCISO porque el paso 1 del superviviente cierra en una subordinada sobre los inversores y el inciso quedaria colgando de ella | paso 1 de pivotar_o_proceder | la fase 04, que redacta y afina los pasos del superviviente |
| **DE PARAMETRO DE PASO** | el destino de la rama que pivota, Y VUELVES AL INICIO; la mitad de PROCEDER si viaja, adosada de INCISO al paso 7, pero la de PIVOTAR muere: el paso 7 del superviviente dice CAMBIAS DE RUMBO (PIVOTAS) y no dice adonde te lleva ese cambio. SE DICE LO QUE NO SE PIERDE: la decision misma y su registro por escrito estan enteros en ese paso 7 | paso 4 de pivotar_o_proceder | la fase 04, que redacta y afina los pasos del superviviente |
| **DE PARAMETRO DE PASO** | LOS CRITERIOS QUE USASTE PARA TOMARLA, que es lo que hace auditable la decision; el paso 7 del superviviente manda anotar la decision final pero no manda anotar con que se decidio. SE DICE LO QUE NO SE PIERDE: el entregable_esperado del superviviente pide el modelo de negocio actualizado y la lista de funciones reducida, que son el rastro de la decision aunque no sean sus criterios. NO SE ADOSA DE INCISO porque el paso 7 ya recibe el del paso 4 y dos incisos sin coordinar dejan el paso diciendo otra cosa | paso 5 de pivotar_o_proceder | la fase 04, que redacta y afina los pasos del superviviente |
| **DE CONDICIONES** | LA CADENCIA y LA PUERTA DE GASTO: que el alto se hace DESPUES DE CADA fase de descubrimiento de clientes, o sea que se repite y no ocurre una sola vez, y que se hace ANTES DE INVERTIR MAS EN DESARROLLO, que es lo que convierte el alto en una puerta de dinero. La condicion 1 del superviviente dispara por HABER TERMINADO de poner a prueba el problema con clientes reales, que es el mismo momento dicho una sola vez y sin la puerta | condicion 1 de pivotar_o_proceder | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |

### LAS REDIRECCIONES Y LAS GUARDAS, LEIDAS DE LA SALIDA DE LA EJECUCION

**Redirecciones sobre nodos VIVOS: 10.** Salen enteras de [`../loop/SALIDA_V64_OPM03II_EJEC.txt`](../loop/SALIDA_V64_OPM03II_EJEC.txt):

| nodo que nombraba al que muere | campo | pasa a nombrar |
|---|---|---|
| `categorias_entusiasmo_cliente` | `nodos_siguientes` | `pivote_o_proceder` |
| `checkpoints_validacion` | `nodos_previos` | `pivote_o_proceder` |
| `decision_pivotar_o_proceder` | `nodos_siguientes` | `pivote_o_proceder` |
| `filosofia_validacion_clientes` | `nodos_previos` | `pivote_o_proceder` |
| `mapa_flujo_trabajo_cliente` | `nodos_siguientes` | `pivote_o_proceder` |
| `presentacion_solucion_producto` | `nodos_previos` | `pivote_o_proceder` |
| `product_market_fit` | `nodos_previos` | `pivote_o_proceder` |
| `scorecard_descubrimiento_cliente` | `nodos_siguientes` | `pivote_o_proceder` |
| `validar_posicionamiento_con_analistas` | `nodos_siguientes` | `pivote_o_proceder` |
| `verificar_modelo_ingresos` | `nodos_siguientes` | `pivote_o_proceder` |

| guarda | resultado |
|---|---|
| **`P.16`, duplicadas que la propia fusion fabrica** | **2** |
| **auto-aristas que la fusion habria creado** | **0** |
| **guarda A**, cero auto-aristas nuevas | **OK (0)** |
| **guarda B**, cero duplicadas nuevas tras resolver | **OK (0)** |
| **guarda C**, los cinco campos que la operacion NO redacta, intactos | **5 de 5** |
| **guarda D**, el absorbido conserva su texto INTACTO | **OK** |

### LO QUE LA FICHA MANDABA COMPROBAR DESPUES DE FUNDIR, COMPROBADO

Sale de [`../loop/SALIDA_V64_VERIFICAR_OPM03II.txt`](../loop/SALIDA_V64_VERIFICAR_OPM03II.txt), corrida en esta vuelta:

```
1. LA CLASIFICACION AMOR TOTAL A INDIFERENCIA, EN EL TEXTO FINAL
   pasos del superviviente HOY: 9 (antes 7)
   la frase vive en el paso: [9]
   texto: Clasifica las respuestas de tus clientes según su nivel de entusiasmo, desde amor total hasta indiferencia
2. EL ALIAS DEL SUPERVIVIENTE CARGA EL ID QUE MUERE
   ids_alias       : ['pivotar_o_proceder']
   merged_originals: forma diccionarios | ids ['pivotar_o_proceder']
   merged_originals en crudo: [{'node_id': 'pivotar_o_proceder', 'titulo': 'La decisión de cambiar de rumbo o seguir adelante (pivot or proceed)', 'fuente': "The Startup Owner's Manual - Steve Blank"}]
3. LAS DOS DUPLICADAS QUE LA FICHA NOMBRA, MEDIDAS HOY (P.16 manda)
   presentacion_solucion_producto     nodos_previos     entradas 4 | resuelven a pivote_o_proceder: 1
      entradas: ['mapa_flujo_trabajo_cliente', 'pivote_o_proceder', 'captura_conocimiento_mercado', 'preguntas_ipo_dolor_cliente']
   scorecard_descubrimiento_cliente   nodos_siguientes  entradas 8 | resuelven a pivote_o_proceder: 1
      entradas: ['identificar_earlyvangelists', 'pivote_o_proceder', 'ganar_comprension_del_cliente', 'identificacion_problema_cliente', 'mapa_de_canal_de_ventas', 'mapa_flujo_trabajo_cliente', 'verificar_product_market_fit', 'voc_temprano_en_agile_stage_gate']
   LAS DOS EN CERO: la duplicada que la fusion fabrico esta LIMPIA, que
   es lo que P.16 manda y lo contrario de lo que la ficha del 12 ago decia.
4. EL ABSORBIDO, DEPRECADO Y CON SU TEXTO INTACTO
   deprecado: SI | texto y aristas INTACTOS: SI
5. LAS DOS PIEZAS QUE LA FICHA RECLASIFICA COMO QUE VIVEN DENTRO
   paso 2, dibujar como trabaja el cliente tipico: INTACTO SI
      Dibuja cómo trabaja realmente tu cliente típico, basándote en datos reales que hayas recogido
   paso 6, reducir la lista de funciones a un parrafo: INTACTO SI
      Reduce tu lista de funciones a algo que puedas contar en un párrafo y vender a miles de personas, no a una lista larguísima pensada para diez clientes
6. EL INCISO ADOSADO, VERBATIM DEL PASO 4 DEL QUE MUERE
   paso 7 ANTES : Anota tu decisión final: cambias de rumbo (pivotas) o sigues adelante
   paso 7 HOY   : Anota tu decisión final: cambias de rumbo (pivotas) o sigues adelante hacia la validación con clientes
   lo anadido   : 'hacia la validación con clientes'
   es subcadena LITERAL del paso 4 del que muere: True
   El diff dice que el censo baja de 927 a 925 y que DESAPARECEN DOS
   grupos, y NO son los dos que P.16 limpio. Se mide de donde salen.
   grupos que desaparecen: 2
      pivotar_o_proceder       nodos_previos     -> decision_pivotar_o_proceder        | vive en el nodo QUE MUERE: SI
         entradas: ['revalidacion_modelo_negocio', 'decision_pivotar_o_proceder']
      pivotar_o_proceder       nodos_previos     -> verificar_modelo_ingresos          | vive en el nodo QUE MUERE: SI
         entradas: ['verificar_modelo_rentable', 'verificar_modelo_ingresos']
   LOS 2 SON DEL NODO QUE MUERE: 2 de 2.
   LA EXPLICACION MEDIDA, y no es que P.16 los limpiara: el censo de
   aristas_duplicadas_tras_resolver.py solo revisa NODOS VIVOS (3272
   antes, 3271 despues), y estos dos eran duplicadas HISTORICAS DENTRO
   de pivotar_o_proceder. Al quedar deprecado, SALEN DEL CENSO. No se
   han reparado: siguen enteras en su nodo, que conserva su texto
   intacto (comprobacion 4). LAS DOS QUE P.16 SI LIMPIO nunca entraron
   en el censo porque nacieron y murieron dentro de la misma corrida,
   y por eso el diff da CERO grupos fabricados.
   contraprueba: las entradas ['revalidacion_modelo_negocio', 'decision_pivotar_o_proceder'] siguen en pivotar_o_proceder.nodos_previos: SI
   contraprueba: las entradas ['verificar_modelo_rentable', 'verificar_modelo_ingresos'] siguen en pivotar_o_proceder.nodos_previos: SI
```

LA CELDA DE PIEZAS REPARTIDAS DICE 7 (3 ENTERAS, 3 YA DICHAS) Y NO SUMA, Y SE DICE EN VEZ DE RETOCARLA: la celda sale literal del resumen del fundidor, que enumera solo las dos marcas viejas; LA SEPTIMA ES EL INCISO, y esta en su fila de la tabla del reparto. El instrumento no la corrige aqui porque la celda es suya y no mia.

DOS COLISIONES DE CLASE FABRICADAS, PREDICHAS Y NO TOCADAS. Medidas con scripts/loop/vuelta64_colisiones_opm03ii.py sobre el arbol de ANTES y sobre el de HOY (../loop/SALIDA_V64_COLISIONES_OPM03II.txt): ESPERADAS 2, MEDIDAS 2, LAS MISMAS, y antes de fundir habia CERO. Son pivote_o_proceder contra pivote_startup (puestos 668 en B y 1312 en D) y pivote_o_proceder contra reunion_pivotar_o_perseverar (968 en B y 1305 en D). NO SE TOCA NI UN VEREDICTO Y SE DICE POR QUE: el 668 es uno de los SIETE dudosos que la ficha de OP-M-03 nombra literalmente y cuyo expediente del 12 ago ya posiciona como PUERTA CONTRA ACTO CON ENLACE, y el 1312 es uno de sus TRES sanos; ademas pivote_startup es miembro de OP-M-03-III, que sigue pendiente. Re-leerlos seria decidir cosa de mesa, que es lo que AUDITOR.md seccion 3 llama improvisacion. Y NO SE RESUELVEN SOLAS: simulada la ejecucion de OP-M-03-III sobre el arbol de hoy, las colisiones pasan de DOS a TRES en vez de a cero. VAN A LA MESA OP-M-03 CON SU MEDICION.

EL CASO POSITIVO DE MESA DE LA VUELTA 63 CADUCO EN ESTA OPERACION, y la caducidad es la que su propia regla predecia: la regla del acta 54 pregunta 7 manda fabricarlo sobre un acto que la vuelta no toque, y el ancestro eligio OP-M-03-II, que es justo lo que esta vuelta ejecuta. Re-corrido hoy da ROJO en cuatro de nueve, no porque las guardas se rompan sino porque el absorbido ya esta deprecado y el generador cae antes en la guarda de miembro vivo. Nace scripts/loop/caso_positivo_de_fusion_de_mesa.py, de nombre estable, con --id-op requerido y una guarda que cae en ROJO si el sujeto esta consumido: LAS NUEVE MUERDEN sobre OP-M-02-ACCLIMATE.



---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 64, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (20 ago 2026, vuelta 65, TAREA 1.a del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **CINCO** veces: las tres adjudicaciones del acta 52 (linea **1250**),
la del acta 57 sobre el acto 25 (**2475**), las del acta 61 (**2689**), las del acta 62 (**2933**) y
las del acta 63 (**3307**), **las cinco cotejadas HOY abriendo el fichero**. **Ninguna cifra
publicada se toca.** **Cada cita lleva la linea LEIDA HOY**, no recordada, y **las treinta y siete se
imprimieron y se compararon antes de escribir esta seccion** con
`python scripts/loop/vuelta65_registrar_acta64.py --simular`, que cae en `ROJO` sin escribir si una
sola no calza: el acta de la vuelta 64 abre en la linea **16655** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), su seccion de adjudicaciones en la **16839**,
la de las siete preguntas en la **16906**, la de las caidas de la tanda en la **16805** y la de las
rachas en la **16989**.

### a) **LOS NUEVE DISCUTIBLES, ADJUDICADOS: OCHO `A FAVOR` Y EL `D5` REGISTRADO COMO CAIDA DE PROCEDIMIENTO AUTODECLARADA**

> **LA DIVERGENCIA SE DECLARA EN VEZ DE RESOLVERSE COPIANDO (regla 1 y regla 2).** El mensaje del
> commit del acta y el encargo de esta vuelta dicen los dos **NUEVE discutibles A FAVOR**, con el
> parentesis *el `D5` registrado como caida de procedimiento autodeclarada*. **El texto del acta, que
> es la vara, no adjudica el `D5` `A FAVOR`**: la linea **16876** lo abre diciendo *caida de
> procedimiento del ejecutor, autodeclarada, registrada en la seccion 3*. **Son OCHO `A FAVOR` y UNO
> registrado como caida**, y el resumen del mensaje del commit **queda entero y sin tachar** como
> contraste. **Ninguna de las dos lecturas cambia una sola cifra ni un solo dato**: el `D5` esta
> registrado en las dos, y solo cambia el rotulo con que se le nombra.

La columna de la vara **no es una glosa: es la regla citable con la que el auditor lo adjudico**, y
va copiada de su linea.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | **sello el `D10` en vez de dejarlo `CUBIERTO` con silencio** | `A FAVOR`, **y no estaba en discusion re-abrir nada: el encargo lo mandaba con todas sus letras**. La vara del **acta 55, pregunta 5** leida entera reparte `APPEND` o `CUBIERTO` **con perdida nombrada** y **no contempla el `CUBIERTO` con silencio**; la misma especie se sello dos veces el mismo dia en `OP-M-03-I`. *Anadir el sello de una mitad que muere no es re-abrir la fusion: es completar su registro por el carril escrito* | **16841** |
| **`D2`** | **marco `CUBIERTO` con perdida nombrada en el paso 1 pudiendo poner `INCISO`** | `A FAVOR`. **El criterio escrito de la politica es la LEGIBILIDAD del paso resultante**, y esta argumentada con el texto delante: el paso 1 del superviviente cierra en la subordinada de los inversores y el inciso quedaria colgando de `SUMALOS` y no de `SIENTATE`. La perdida va **nombrada y enrutada**, que es la mitad auditable que el `D9` del acta 62 exige. *Que lo decida el ojo del ejecutor con el criterio escrito y lo marque discutible es exactamente la forma debida* | **16851** |
| **`D3`** | **no apilo un segundo `INCISO` en el paso 5** | `A FAVOR`, **por el mismo criterio**: el paso 7 ya recibe el inciso del paso 4 y el apilado dejaria el paso diciendo otra cosa. La perdida (**los criterios de la decision**) va nombrada y enrutada, y **el paso se puede rehacer sin tocar el grafo** si la respuesta general fuera otra. **La regla general queda en la pregunta 5** y se registra en el apartado **c)** | **16860** |
| **`D4`** | **ejecuto dejando DOS colisiones de clase vivas** | `A FAVOR`, **con el desarrollo entero en la pregunta 3**. Las guardas obligatorias de `AUDITOR.md` seccion 3 estan TODAS verdes (cero duplicadas y cero auto-aristas tras resolver, **medidas por el auditor**); el censo es la guarda que el encargo anade y **su contrato es esperadas y CALZA, y CALZA**: esperadas 2, medidas 2, las mismas, **predichas por la fusion**. *Re-leer los cuatro puestos seria ejecutar la adjudicacion de la mesa `OP-M-03` fuera de su turno*, que es la improvisacion que la seccion 3 prohibe. **Publicar la celda en rojo en vez de esconderla es el canon de la casa** | **16866** |
| **`D5`** | **midio la cuenta esperada del censo DESPUES de fundir** | **NO es `A FAVOR`: es caida de procedimiento del ejecutor, autodeclarada**, y queda registrada en la seccion 3 del acta. **El manejo posterior fue el debido**: la simulacion se corrio sobre el arbol de ANTES de fundir y calza con la medida, asi que **no hay cifra mala publicada**. **El orden equivocado queda con nombre y no se repite: la cuenta esperada se mide ANTES** | **16876** |
| **`D6`** | **estreno DOS instrumentos de nombre estable y los uso el mismo dia** | `A FAVOR` **por el carril del `D3` del acta 63**, con las guardas comprobadas por el auditor: **las nueve muerden** sobre un sujeto que la vuelta no toco, **la guarda NUEVA de sujeto consumido muerde** sobre `OP-M-03-II`, el ancestro queda entero con su `ROJO` committeado como contraste, el heredado muerde las seis, y **el censo da cero tallados sobre 22**. *Un estreno que HACE CRECER una guarda y nace de una leccion medida es la especie buena de estreno* | **16881** |
| **`D7`** | **no estreno clave nueva en `OPERACIONES.jsonl`** | `A FAVOR`. **El esquema es pendiente de doctrina heredado** (acta 55) y **estrenar clave en 5 de 71 fichas seria decidirlo de tapadillo**; el campo `nota` es el carril que **ocho fichas ya usan**, y **las 18 claves quedaron intactas**, medido por el auditor | **16889** |
| **`D8`** | **dejo las cinco consumidas en estado `LISTA`** | `A FAVOR` **con el limite dicho**. La celda publica lo que el instrumento mide y **la divergencia (cinco de esas 71 no se pueden ejecutar) esta declarada** en el reporte y en las notas de las fichas; cambiar el estado seria **estrenar valor de esquema**, que es el mismo pendiente del `D7`. **La regla de la ficha envejecida** (acta 63, pregunta 1) **protege la ejecucion: lo consumado no se ejecuta, este como este su celda** | **16893** |
| **`D9`** | **publico la vara del instrumento en el cableado** | `A FAVOR`. **Son dos varas y no una discrepancia**, las dos medidas por el auditor (**10 contra 5** y **12 contra 6**, identicas a las publicadas), y **la publicada es la que la ficha uso**, que es el mismo manejo que el acta 63 declaro para los enlaces | **16900** |

### b) **EL CARRIL DE LAS DOS COLISIONES DE CLASE VIGENTES: LA MESA `OP-M-03` ES SU DUENA Y LA LINEA BASE DEL CENSO PASA A `2`**

**No es doctrina nueva y el acta lo dice al adjudicarla** (linea **16916**): es **extension del carril
general de colisiones**, que el acta 52 pregunta 4 adjudico y que **esta misma pagina registro en la
linea 1377** en sus dos especies (**volteo por maquina** y **relectura en el mismo acto**). **La
especie `B` contra `D` ya tiene precedente resuelto por RELECTURA EN EL MISMO ACTO**, el puesto 204.

**Lo que el acta 64 fija, y su letra:**

> **El acto al que pertenecen los puestos es material adjudicado de la mesa `OP-M-03`**: el **668**
> esta LITERAL entre sus siete dudosos y su expediente del 12 ago ya lo posiciona como *puerta contra
> acto con enlace*, el **1312** esta entre sus tres sanos, y el par de la reunion es la misma familia
> del pivote cuya serie la mesa gobierna.
>
> **La relectura en el mismo acto EXISTE como carril; su ejecutor es la operacion que es DUENA del
> acto, y su turno lo fija el `00_INDICE`.** Hasta ese turno **las dos colisiones quedan REGISTRADAS,
> VIGENTES y PUBLICADAS EN ROJO**, con **la mesa `OP-M-03` como duena nombrada**, y **NO SE TOCAN**.
>
> **LA LINEA BASE DEL CENSO DE COLISIONES PASA DE `0` A `2`, DECLARADA** (linea **16929**): **toda
> operacion siguiente corre el censo con esperadas MEDIDAS sobre esa base**, y **un delta no predicho
> por la operacion sigue siendo PARADA de guarda**.
>
> **Que la deuda crezca con `OP-M-03-III` (de 2 a 3, medido) no cambia el carril**: cambia la cuenta
> esperada de esa fusion, **que debera predecirlo en su plan**.

**Y LA CUENTA ESPERADA SE MIDE ANTES DE FUNDIR, sobre el arbol de antes**, que es la leccion del
`D5` del apartado **a)** escrita como procedimiento y no como reproche.

### c) **NO SE APILA MAS DE UN `INCISO` SOBRE EL MISMO PASO**

**Por defecto NO** (acta 64, pregunta 5, linea **16940**), **y tampoco es doctrina nueva**: sale por
**extension del criterio escrito** de la politica del `INCISO`, que es **la legibilidad del paso
resultante**, y *un segundo inciso sin coordinar la rompe*.

> **Si un caso concreto leyera limpio con dos, se ejecuta MARCADO DISCUTIBLE y el auditor lo
> adjudica**, que es el mismo camino del `D2` y el `D3`. **La perdida del paso que no lo recibe queda
> ENRUTADA y re-hacible** si el fundador un dia escribe otra letra.

### d) **LA CAIDA DE REPORTE DEL EJECUTOR, CON SU NOMBRE, Y LA RACHA EN UNO**

**Se registra aqui porque el registro no depende del acta, y porque una caida que solo vive en un
acta se olvida.** **La caida es la `7.1` del reporte de la vuelta 64** (acta, linea **16808**): el
mensaje del commit `6e1784c0` publico **tres celdas del barrido que salieron de la corrida ANTERIOR y
no de la de ese momento**. **El ejecutor la autodeclaro y el auditor la verifico EXACTA en sus dos
mitades**: el mensaje dice 417 ficheros, `ROJO` 32 y cuatro scripts sin hallazgo; **la corrida
committeada EN ESE MISMO COMMIT** dice 415 ficheros, `ROJO` 33 y `AMBAR` 2.

**Es caida de REPORTE**, no de clase ni de cifra: **vive en un mensaje de commit y no movio ningun
dato**. Se registra, **dispara la relectura al doble del tramo** (hecha) y **NO acumula para la
parada**. **LA RACHA DE REPORTE PASA DE CERO A UNO** (linea **16989**), y **tres tandas seguidas de
la misma especie serian patron y parada**. **CLASE O CIFRA sigue EN CERO**, novena tanda limpia
(linea **16825**).

### e) **LAS RESPUESTAS DE LAS PREGUNTAS 4 Y 7, REGISTRADAS Y NO ENCARGADAS**

**Se registran porque son adjudicaciones vivas que mandan sobre lo que viene, aunque no encarguen
trabajo a nadie.**

| pregunta | la respuesta del acta 64, copiada de su linea | linea |
|---|---|---:|
| **4. las fusiones de mesa ANTES que sus mesas** | **el orden es el escrito** (`00_INDICE` y campo `orden`) **y no se cambia por acta**; **el costo** (las colisiones que fabrica ejecutar las hijas antes que la madre) **queda medido y registrado**, y **la pregunta se guarda para el CIERRE DE LA FASE 03**, como la de los cinco pares con dueno del acta 63 | **16935** |
| **7. el sujeto del caso positivo elegido por medicion** | **la guarda nueva ya cae en `ROJO` si el sujeto esta consumido**, que es lo que la vuelta 64 demostro; elegirlo por medicion es **mejora del mismo instrumento por el mismo carril de sucesores, SIN URGENCIA MEDIDA**. **Queda ANOTADO, no encargado** | **16957** |

**Y las otras cinco quedan donde el acta las dejo y aqui se dice para que no parezca omision:** la
**1** (el `INCISO` de condiciones no existe) sigue en su carril escrito del acta 55 pregunta 5, con
**el costo medido y registrado** (linea **16908**); la **2** (el esquema de `OPERACIONES.jsonl`)
sigue pendiente y **el carril de la nota lo cubre** (**16914**); la **3** y la **5** se registran
enteras en los apartados **b)** y **c)** de aqui arriba; y la **6** (la aguja del comprobador de
promesas) **iba encargada** (**16947**) **y es la TAREA 1.b de la vuelta 65**, que la ensancha por
correccion declarada con caso positivo en dos mitades.

### f) **LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya**

**NO toca ni una cifra publicada arriba, NO elige ningun superviviente, NO funde nada, NO deshace
ninguna fusion y NO re-lee ni un veredicto de las dos colisiones vigentes.** Registra adjudicaciones.


---

## `OP-U-02, TRAMO UNICO Y FINAL POR AGOTAMIENTO: EL REGISTRO DEL LOTE A` (2026-08-20, vuelta 65)

**Cada celda y cada tabla de este registro sale del PLAN SELLADO
[`../loop/PLAN_V65_OPU02_LOTE_A.json`](../loop/PLAN_V65_OPU02_LOTE_A.json) o de una salida de esta
vuelta, generada y pegada entera con `python scripts/loop/vuelta65_registro_tramo.py`.** **El
registro se adosa al final de la pagina y NO reescribe ni una linea de arriba.**

**EL LOTE SE DECLARO AL ABRIRLO Y ES PREFIJO SIN SALTOS** del `orden_universo` del tramo fijado en
[`../loop/TRAMO_UNICO_OPU02_V64.jsonl`](../loop/TRAMO_UNICO_OPU02_V64.jsonl): **los actos 1 y 3**,
que son **los dos primeros**. **Los dos CIERRAN ENTEROS en esta vuelta**, uno declarado y el otro
fundido.

### a) **EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`, Y ES LA PRIMERA VEZ QUE LA CAMPANA LO HACE**

`P.10` del banco del plan dice, con todas sus letras, que **un NODO PUENTE es el que tiene `A` con
dos nodos que entre si son `D`**, que **la componente que forma puede ser UNA familia o DOS pegadas
por el**, que **el cierre transitivo no lo distingue porque no lee sino que cuenta**, y que **si
aparece, LA COMPONENTE NO SE FUNDE HASTA QUE ESE TRIANGULO SE CIERRE**. **Lo que `P.10` llama *lo que
nunca es salida* es exactamente fundir la componente entera porque el cierre transitivo la junta.**

**LA MEDICION VA DELANTE DE LA DECISION**, y sale de
`python scripts/loop/vuelta65_puentes_del_tramo.py`, con los ids pasados por el resolutor (`P.1`):

| | |
|---|---|
| **acto** | **1** del `orden_universo`, el PRIMERO del prefijo |
| **miembros** | **15**, y **NINGUNO se toca** |
| **combinaciones internas** | 105 |
| **pares `A` internos** | 20 |
| **pares `D` internos** | **10**, leidos y declarados DISTINTOS |
| **pares sin veredicto escrito** | 75 |
| **NODOS PUENTE** | **3** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **6** |
| **PUERTAS dentro del acto** | **2**: `enfoque_situacional_vs_personal`, `fallas_activas_condiciones_latentes` |
| **instrumento** | [`../loop/SALIDA_V65_PUENTES_TRAMO.txt`](../loop/SALIDA_V65_PUENTES_TRAMO.txt) |

**LOS TRES NODOS PUENTE Y SUS SEIS TRIANGULOS, leidos de la salida:**
`errores_como_consecuencia` hace de puente en **cuatro** (contra `error_humano_vs_falla_mecanica` y
`falla_sistemica_vs_error_individual`, que son `D` en el puesto **2403**; contra
`new_view_human_error` y `riesgos_del_enfoque_en_error_humano`, `D` en el **2299**; contra
`new_view_human_error` y `seduccion_modelo_persona`, `D` en el **2331**; y contra
`riesgos_del_enfoque_en_error_humano` y `seduccion_modelo_persona`, `D` en el **2228**);
`human_error_como_sintoma` en **uno** (el **2403**); y `vieja_vision_vs_nueva_vision_seguridad` en
**uno** (`new_view_human_error` contra `new_view_vs_old_view`, `D` en el **2220**).

**LAS TRES SALIDAS DE `P.10`, RECORRIDAS UNA A UNA en vez de elegir la comoda:** *leer el par que
falta* es la unica que resuelve de verdad, **y quedan 75 combinaciones sin veredicto escrito**, que
es trabajo de cribado y no de esta operacion; *releer contra el superviviente* **no aplica**, porque
aqui no hay superviviente elegido ni nodo que vaya a cambiar; y *fundir solo el subconjunto CERRADO y
enlazar el resto* **pide que TODAS las lecturas esten hechas, y no lo estan**.

> **Y HAY UNA SEGUNDA RAZON INDEPENDIENTE, TAMBIEN MEDIDA, que sola bastaria: DOS de los quince
> miembros son PUERTA** con la marca *TIENE QUE SOBREVIVIR* (`enfoque_situacional_vs_personal` y
> `fallas_activas_condiciones_latentes`, leidas de la salida del dossier). **La GUARDA 1B dice que un
> nodo que es semilla de entrada o extremo de puente aprobado NO SE ABSORBE**, y una fusion a un solo
> superviviente tendria que absorber una de las dos.

**EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se elige
superviviente.** El motivo entero esta sellado en el campo `declarados_y_no_fundidos` del plan.

### b) **EL ACTO 3: LA PRIMERA FUSION DE MAS DE DOS MIEMBROS DE LA CAMPANA**

| | |
|---|---|
| **superviviente** | `causas_comunes_vs_especiales` |
| **absorbidos** | **9** |
| **nodos implicados / nodos que MUEREN** | 10 / 9 |
| **plan sellado** | [`../loop/PLAN_V65_OPU02_LOTE_A.json`](../loop/PLAN_V65_OPU02_LOTE_A.json), contrato **`CAMPO PROPIO v1`** |
| **figura** | ACTO DE 10 MIEMBROS, clases internas {'A': 14} medidas en el fichero del tramo |

**LA PREGUNTA DE `P.5`, UNA FAMILIA O DOS, CONTESTADA CON MEDICION Y NO CON IMPRESION:** los **diez**
miembros salen del **mismo libro** (*Out of the Crisis*, Deming), **los 14 pares internos con
veredicto escrito son TODOS de clase `A`**, hay **CERO pares `D` internos** y **CERO nodos puente**.
**`P.10` solo detiene una componente cuando aparece un triangulo `A` mas `A` mas `D`, y aqui no hay
ninguno.**

**EL SUPERVIVIENTE LO ELIGE EL CONTENIDO, CON LAS TRES VARAS POR FORMA A SU LADO Y NINGUNA EN CONTRA**
(`TODAS DE ACUERDO`, que funde a su lado): **6 pasos contra un maximo de 5**, **3 condiciones contra
2** y **cableado 14 contra un maximo de 9**. **NI EL ROTULO SOLO NI LA CANTIDAD DECIDEN**: decide que
es el unico del acto que trae el procedimiento entero de punta a punta, del dato en orden cronologico
a la accion distinta por tipo de causa. **NINGUN MIEMBRO DE ESTE ACTO ES PUERTA**, medido al sellar.

#### EL REPARTO POR ABSORBIDO, TALLADO DEL PLAN SELLADO

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `distincion_causas_comunes_especiales` | 4 | 2 | 1 | 4 | 1 |
| `distincion_causas_comunes_especiales_2` | 4 | 2 | 1 | 5 | 0 |
| `distincion_causas_comunes_especiales_incidentes` | 5 | 2 | 1 | 4 | 2 |
| `distincion_causas_especiales_comunes` | 4 | 2 | 1 | 5 | 0 |
| `identificacion_causa_raiz_no_culpa_individual` | 5 | 2 | 4 | 3 | 0 |
| `moral_y_sistema_no_individuo` | 4 | 2 | 3 | 3 | 0 |
| `politica_no_culpar_trabajador` | 5 | 2 | 2 | 5 | 0 |
| `trampa_del_promedio_como_estandar` | 4 | 2 | 2 | 4 | 0 |
| `variacion_del_sistema_vs_individuo` | 5 | 2 | 1 | 6 | 0 |
| **los 9 juntos** | **40** | **18** | **16** | **39** | **3** |

#### EL REPARTO, PIEZA A PIEZA, TALLADO DEL PLAN SELLADO

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `distincion_causas_comunes_especiales` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **2** de `distincion_causas_comunes_especiales` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| paso **3** de `distincion_causas_comunes_especiales` | `INCISO` | **`INCISO` ADOSADO** al paso 4: *ayudar al trabajador a identificarla y eliminarla* |
| paso **4** de `distincion_causas_comunes_especiales` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| condicion **1** de `distincion_causas_comunes_especiales` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **2** de `distincion_causas_comunes_especiales` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **1** de `distincion_causas_comunes_especiales_2` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **2** de `distincion_causas_comunes_especiales_2` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| paso **3** de `distincion_causas_comunes_especiales_2` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `distincion_causas_comunes_especiales_2` | `CUBIERTO` | ya lo dice el **paso 6** del superviviente |
| condicion **1** de `distincion_causas_comunes_especiales_2` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| condicion **2** de `distincion_causas_comunes_especiales_2` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `distincion_causas_comunes_especiales_incidentes` | `INCISO` | **`INCISO` ADOSADO** al paso 1: *de incidentes o accidentes* |
| paso **2** de `distincion_causas_comunes_especiales_incidentes` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `distincion_causas_comunes_especiales_incidentes` | `CUBIERTO` | ya lo dice la **condicion 1** del superviviente |
| paso **4** de `distincion_causas_comunes_especiales_incidentes` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **5** de `distincion_causas_comunes_especiales_incidentes` | `INCISO` | **`INCISO` ADOSADO** al paso 6: *la proporción estimada de causas sistémicas vs especiales* |
| condicion **1** de `distincion_causas_comunes_especiales_incidentes` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **2** de `distincion_causas_comunes_especiales_incidentes` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **1** de `distincion_causas_especiales_comunes` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **2** de `distincion_causas_especiales_comunes` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `distincion_causas_especiales_comunes` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `distincion_causas_especiales_comunes` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| condicion **1** de `distincion_causas_especiales_comunes` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| condicion **2** de `distincion_causas_especiales_comunes` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **1** de `identificacion_causa_raiz_no_culpa_individual` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **2** de `identificacion_causa_raiz_no_culpa_individual` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `identificacion_causa_raiz_no_culpa_individual` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `identificacion_causa_raiz_no_culpa_individual` | `CUBIERTO` | ya lo dice el **paso 6** del superviviente |
| paso **5** de `identificacion_causa_raiz_no_culpa_individual` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `identificacion_causa_raiz_no_culpa_individual` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **2** de `identificacion_causa_raiz_no_culpa_individual` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **1** de `moral_y_sistema_no_individuo` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **2** de `moral_y_sistema_no_individuo` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `moral_y_sistema_no_individuo` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `moral_y_sistema_no_individuo` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `moral_y_sistema_no_individuo` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `moral_y_sistema_no_individuo` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **1** de `politica_no_culpar_trabajador` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **2** de `politica_no_culpar_trabajador` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `politica_no_culpar_trabajador` | `CUBIERTO` | ya lo dice el **paso 6** del superviviente |
| paso **4** de `politica_no_culpar_trabajador` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| paso **5** de `politica_no_culpar_trabajador` | `CUBIERTO` | ya lo dice el **paso 6** del superviviente |
| condicion **1** de `politica_no_culpar_trabajador` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `politica_no_culpar_trabajador` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `trampa_del_promedio_como_estandar` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **2** de `trampa_del_promedio_como_estandar` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **3** de `trampa_del_promedio_como_estandar` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `trampa_del_promedio_como_estandar` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| condicion **1** de `trampa_del_promedio_como_estandar` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **2** de `trampa_del_promedio_como_estandar` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `variacion_del_sistema_vs_individuo` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `variacion_del_sistema_vs_individuo` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **3** de `variacion_del_sistema_vs_individuo` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `variacion_del_sistema_vs_individuo` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| paso **5** de `variacion_del_sistema_vs_individuo` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| condicion **1** de `variacion_del_sistema_vs_individuo` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **2** de `variacion_del_sistema_vs_individuo` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |

#### LAS PERDIDAS, SELLADAS EN CAMPO PROPIO (`CAMPO PROPIO v1`)

**Son 13**, y la tabla sale entera de
`python scripts/loop/tallar_perdidas_del_plan.py --plan docs/loop/PLAN_V65_OPU02_LOTE_A.json`
([`../loop/SALIDA_V65_TALLAR_PERDIDAS.txt`](../loop/SALIDA_V65_TALLAR_PERDIDAS.txt)). **Por especie:
{'DE CONDICIONES': 3, 'DE PARAMETRO DE PASO': 10}.**

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE PARAMETRO DE PASO | la instruccion explicita de NO INFORMAR SOBRE DEFECTOS INDIVIDUALES cuando el proceso esta en control estadistico. El paso 5 del superviviente manda listar las causas comunes y asumir la responsabilidad sobre ellas, que es enfocar el esfuerzo en el sistema, pero NO dice que haya que dejar de reportar el defecto de cada uno | paso 2 de distincion_causas_comunes_especiales | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE PARAMETRO DE PASO | la prohibicion explicita de SANCIONAR AL TRABAJADOR por fallas atribuibles al sistema. SE DICE LO QUE NO SE PIERDE: la condicion 1 del superviviente ya dispara cuando estas por culparte a ti o a alguien sin verificar si es del sistema, y el paso de rediseñar el proceso en lugar de sancionar al individuo VIAJA ENTERO de APPEND desde distincion_causas_comunes_especiales_incidentes | paso 4 de distincion_causas_comunes_especiales | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE PARAMETRO DE PASO | que la accion para las causas comunes sea UN CAMBIO ESTRUCTURAL DEL SISTEMA y no el rastreo caso por caso. El paso 6 del superviviente manda definir una accion distinta para cada tipo de causa pero NO dice cual es la de las comunes | paso 4 de distincion_causas_comunes_especiales_2 | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE CONDICIONES | que el disparador incluya ACCIDENTES, FALLAS O RESULTADOS DESFAVORABLES RECURRENTES. La condicion 2 del superviviente nombra indicadores de desempeño, ventas, calidad o quejas, y ninguna de las cuatro es un accidente | condicion 1 de distincion_causas_comunes_especiales_incidentes | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE PARAMETRO DE PASO | la remision al CAPITULO 11 de la fuente como el metodo estadistico con el que se decide si una intervencion es necesaria. El paso 3 del superviviente manda aplicar reglas simples y las nombra, pero no remite a ese capitulo | paso 4 de distincion_causas_especiales_comunes | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE CONDICIONES | el disparador del CONFLICTO INTERNO YA INSTALADO por errores o tasas de rechazo, que no es el momento de culpar sino el estado que deja el haber culpado. ATENUANTE DECLARADO, y se dice para que la perdida se pueda pesar: la condicion 1 de identificacion_causa_raiz_no_culpa_individual viaja ENTERA de APPEND y nombra el conflicto interno y la baja moral | condicion 1 de moral_y_sistema_no_individuo | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE CONDICIONES | que el disparador sea LA MORAL DEL EQUIPO YA AFECTADA por señalamientos de culpa. ATENUANTE DECLARADO: la condicion 1 de identificacion_causa_raiz_no_culpa_individual viaja entera de APPEND y nombra la baja moral por atribucion de culpas | condicion 2 de moral_y_sistema_no_individuo | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE PARAMETRO DE PASO | que el punto que excede el limite superior sea UNA PERSONA y que antes de actuar se investigue SU CONTEXTO. El paso 3 del superviviente detecta posibles causas especiales con reglas sobre los puntos, y el paso 4 manda investigar la señal, pero ninguno de los dos dice que el punto pueda ser alguien ni manda mirar su contexto antes de actuar | paso 2 de politica_no_culpar_trabajador | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE PARAMETRO DE PASO | la prohibicion de las SANCIONES UNIFORMES Y LOS MENSAJES ESTANDAR para todos los niveles de error. El paso 6 del superviviente manda definir una accion distinta para cada tipo de causa, que es la forma positiva de lo mismo, pero no prohibe la respuesta uniforme | paso 3 de politica_no_culpar_trabajador | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE PARAMETRO DE PASO | EL PROMEDIO SIMPLE COMO LINEA DE CORTE, nombrado como el error que se abandona. El paso 2 del superviviente manda construir el grafico con limites calculados estadisticamente, que es lo que sustituye al promedio, pero NO nombra al promedio ni dice que dejarlo es el punto. Es el titulo entero del nodo que muere | paso 1 de trampa_del_promedio_como_estandar | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE PARAMETRO DE PASO | los ejemplos concretos de causa especial, PROBLEMAS DE VISION O DE CAPACITACION, que es lo que convierte la busqueda en algo que se puede hacer. NO SE ADOSA DE INCISO Y SE DICE POR QUE: el paso 4 del superviviente YA recibe el inciso del paso 3 de distincion_causas_comunes_especiales, y no se apila mas de un INCISO sobre el mismo paso (acta 64, pregunta 5) | paso 4 de trampa_del_promedio_como_estandar | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE PARAMETRO DE PASO | que los datos sean DE UN GRUPO DE PERSONAS QUE HACEN UN TRABAJO SIMILAR. El paso 1 del superviviente recopila los datos DEL PROCESO. ATENUANTE DECLARADO: el paso 1 de politica_no_culpar_trabajador viaja ENTERO de APPEND y analiza la distribucion de errores ENTRE TODAS LAS PERSONAS con limites de control | paso 1 de variacion_del_sistema_vs_individuo | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V65_OPU02_LOTE_A.json | 3 | DE PARAMETRO DE PASO | que el caer fuera de los limites cuente TAMBIEN PARA BIEN y no solo para mal, que es lo que impide leer el grafico como una lista de culpables. El paso 3 del superviviente detecta posibles causas especiales sin decir que el punto alto tambien es una señal que se investiga | paso 3 de variacion_del_sistema_vs_individuo | la fase 04, que redacta y afina los pasos del superviviente |

> **LAS TRES COSAS QUE EL REPARTO DICE EN VEZ DE CALLAR, y las tres tienen letra citable.**
> **PRIMERA, POR QUE HAY TRES `INCISO` Y NO SEIS:** el paso **4** del superviviente recibe **UN**
> inciso y **NO** recibe el segundo que pedia `trampa_del_promedio_como_estandar` con sus ejemplos de
> vision y capacitacion, **porque NO SE APILA MAS DE UN `INCISO` SOBRE EL MISMO PASO** (acta 64,
> pregunta 5, registrada en esta misma vuelta unas lineas mas arriba); esa pieza va `CUBIERTO` con la
> perdida **nombrada y enrutada**. **SEGUNDA, LAS ADVERTENCIAS NO SON PASOS** (`P.11`): *evitar
> sanciones*, *evitar conclusiones apresuradas*, *evitar tratar cada defecto como causa especial* y
> *dejar de usar el promedio como linea de corte* **califican el acto y no lo constituyen**, asi que
> van `CUBIERTO` con su perdida nombrada en vez de `APPEND`. **TERCERA, LOS SOLAPES VAN DECLARADOS**
> para la poda de la fase 04: dos piezas de comunicacion viajan enteras diciendo casi lo mismo, y las
> piezas del eje de la persona van `CUBIERTO` **con el atenuante dicho**, porque ese eje llega entero
> en el `APPEND` del paso 1 de `politica_no_culpar_trabajador`.

#### LAS GUARDAS, LEIDAS DE LA SALIDA DE LA EJECUCION

Salen de [`../loop/SALIDA_V65_LOTE_A_EJEC.txt`](../loop/SALIDA_V65_LOTE_A_EJEC.txt):

| guarda | resultado |
|---|---|
| **`P.16`, duplicadas que la propia fusion fabrica** | **6**, limpiadas en el mismo commit |
| **guarda A**, cero auto-aristas nuevas | **OK (0)** |
| **guarda B**, cero duplicadas nuevas tras resolver | **OK (0)** |
| **guarda C**, los cinco campos que la operacion NO redacta, intactos | **5 de 5** |
| **guarda D**, los absorbidos conservan su texto INTACTO | **OK** |
| **`P.16` por instrumento**, grupos FABRICADOS de verdad | **0** (y 4 grupos que DESAPARECEN) |

#### LA CUENTA ESPERADA DE COLISIONES, MEDIDA **ANTES** DE FUNDIR

**Se mide antes y no despues, y esa es la mitad del punto**: es la leccion del `D5` de la vuelta 64,
que el acta 64 registro como caida de procedimiento autodeclarada. **La linea base es `2` y esta
DECLARADA** (acta 64, pregunta 3, registrada en esta pagina unas lineas mas arriba): **las dos
colisiones vigentes son de la mesa `OP-M-03` y NO SE TOCAN.**

**Simulacion en memoria sobre el arbol de ANTES de fundir**
([`../loop/SALIDA_V65_COLISIONES_ESPERADAS.txt`](../loop/SALIDA_V65_COLISIONES_ESPERADAS.txt)):
**colisiones NUEVAS que la fusion fabricaria: 0.** **Censo de cierre con la esperada MEDIDA:
2 | MEDIDA: 2 | CALZA: SI** ([`../loop/SALIDA_V65_CENSO_COLISIONES_LOTE_A.txt`](../loop/SALIDA_V65_CENSO_COLISIONES_LOTE_A.txt)).

### c) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba, NO re-lee ni un veredicto de las dos colisiones vigentes de
la mesa `OP-M-03`, NO ejecuta ningun acto con dueno de otra operacion y NO rehace ninguna de las
cinco fichas `OP-M-02` consumidas.**


---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 65, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (20 ago 2026, vuelta 66, TAREA 1.a del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **SEIS** veces: las tres adjudicaciones del acta 52 (linea **1250**),
la del acta 57 sobre el acto 25 (**2475**), las del acta 61 (**2689**), las del acta 62 (**2933**),
las del acta 63 (**3307**) y las del acta 64 (**3613**), **las seis cotejadas HOY abriendo el
fichero**. **Ninguna cifra publicada se toca.** **Cada cita lleva la linea LEIDA HOY**, no recordada,
y **las cuarenta y siete se imprimieron y se compararon antes de escribir esta seccion** con
`python scripts/loop/vuelta66_registrar_acta65.py --simular`, que cae en `ROJO` sin escribir si una
sola no calza: el acta de la vuelta 65 abre en la linea **17018** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), su seccion de adjudicaciones en la **17185**,
la de los pendientes en la **17253**, la de las caidas de la tanda en la **17160** y la de las
rachas en la **17338**.

### a) **LOS DOCE DISCUTIBLES, ADJUDICADOS: LOS DOCE `A FAVOR`, Y NINGUNA CAIDA DEL EJECUTOR EN LAS TRES ESPECIES**

La columna de la vara **no es una glosa: es la regla citable con la que el auditor lo adjudico**, y
va copiada de su linea. **La cifra de cabecera y el detalle coinciden esta vez** (linea **17185**,
*ADJUDICACION DE LOS DOCE DISCUTIBLES*), que es justo lo que en la tanda anterior no pasaba.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | **registrar OCHO `A FAVOR` y no NUEVE, contra el resumen del commit y contra el encargo** | `A FAVOR`. **La vara es el TEXTO del acta**, cuya seccion 4 adjudica el `D5` de la tanda anterior como caida de procedimiento; **la divergencia con el resumen del commit se declara como contraste sin tachar nada** y **ninguna cifra se mueve**. *Una instruccion que contradice el texto que resume pierde contra ese texto*, que es la regla 2 aplicada al propio resumen del auditor | **17187** |
| **`D2`** | **corregir en el sitio los DOS instrumentos de nombre estable en vez de escribir sucesores** | `A FAVOR`. El encargo nombraba `generar_plan_del_lote.py` **con la operacion `OP-U-02` con todas sus letras** y ese fichero **no podia correr**; el carril de correccion declarada es **el que la vuelta 63 uso sobre EL MISMO fichero**; el texto viejo esta **verbatim** y el caso positivo **ancestro contra corregido AISLA la correccion** (y ya mordio una vez). *Un sucesor habria dejado roto al instrumento que el encargo nombraba* | **17193** |
| **`D3`** | **una guarda N-aria que CRECE y se estrena el mismo dia** | `A FAVOR` **por el carril del `D6` del acta 64**: un estreno que **HACE CRECER** una guarda, con la averia `7.2` como prueba de que muerde de verdad. Y la averia del generador viejo (**sellar quince miembros con UN absorbido y TRECE desaparecidos en silencio**) era **de la especie que MIENTE, la peor**: corregirla no admitia esperar | **17200** |
| **`D3.b`** | **la PRIMERA fusion N-aria de la campana, de diez miembros** | `A FAVOR`, **y es la adjudicacion de mas peso de la tanda**. `P.5` contestada **por medicion** (mismo libro, 14 pares con veredicto TODOS `A`, cero `D`, cero puentes) **y por la relectura ciega de los diez textos**, que da UNA familia sin dudas; el reparto **pieza a pieza verificado contra los textos** (51 comprobaciones); y **el tamano sin precedente esta mitigado por lo unico que puede mitigarlo, que el reparto entero sea legible y auditable, y lo es** | **17206** |
| **`D4`** | **un tramo sin numero no se numera** | `A FAVOR`. **Leer el campo `tramo` del fichero en vez de inventarle un ordinal es el instrumento manda** | **17213** |
| **`D5`** | **declarar el `ACTO 1` por `P.10` en vez de cerrar sus triangulos** | `A FAVOR`. **Las tres salidas de `P.10` estan recorridas con su letra**; leer los 75 pares **seria un cribado que la fase no tiene** (banco 9.21, el barrido corre UNA vez) y el subconjunto cerrado **esta condicionado por `P.10` a que TODAS las lecturas esten hechas**. **La segunda razon independiente es real y el auditor la leyo**: DOS puertas con `TIENE QUE SOBREVIVIR` hacen imposible la fusion a un superviviente por la guarda `1B`. *Declarar sin fundir no desmiente ninguna lectura escrita y es reversible entero* | **17215** |
| **`D6`** | **leer un veredicto ausente como NO CANDIDATO y no como par sin leer** | `A FAVOR` **POR EXTENSION CITABLE**, con la adjudicacion entera en el apartado **b)** de aqui abajo | **17224** |
| **`D7`** | **un lote de DOS actos, y el primero sin fusion** | `A FAVOR`. **El lote es prefijo sin saltos, declarado al abrir y entregado entero**, que es el contrato del acta 61 (**prefijo con tope, no minimo**). *Corto y dicho es la forma debida* | **17226** |
| **`D8`** | **las cuatro advertencias a `CUBIERTO` con perdida, pudiendo ser `APPEND`** | `A FAVOR`. **`P.11` es la vara escrita** (califican el acto, no lo constituyen), **las cuatro perdidas van nombradas y enrutadas**, y **la lectura ciega del auditor llego a lo mismo antes de destapar** | **17229** |
| **`D9`** | **dieciseis `APPEND` y el nodo mas largo de la campana** | `A FAVOR`. **La politica escrita reparte `APPEND` o `CUBIERTO` con perdida nombrada**; ante el empate, **un catalogo mas rico con solapes DECLARADOS para la poda de la fase 04 pierde menos que un `CUBIERTO` que calla texto vivo**. El costo (15 pasos, 10 condiciones) **queda publicado y la fase 04 existe** | **17233** |
| **`D10`** | **tres perdidas selladas con atenuante declarado** | `A FAVOR` **por el carril del `D8` del acta 63**: *una perdida con atenuante declarado es mas auditable que un silencio*, y **las tres nombran al hermano cuyo `APPEND` trae el contenido**, leidas por el auditor | **17238** |
| **`D11`** | **el `INCISO` al paso 6, el de la proporcion estimada** | `A FAVOR`. **El auditor leyo el paso resultante**: cierra en *definir una accion distinta para cada tipo de causa, incluida la proporcion estimada*, **y es legible**. *Es el mas fragil de los tres y esta bien marcado* | **17242** |
| **`D12`** | **ensanchar el dossier sin encargo** | `A FAVOR`. **El docstring del propio dossier ya prometia la razon entera de cada par interno**, sin eso `P.5` **no se puede leer en un acto de quince**, y la correccion va declarada **con no regresion medida**. *Cumplir la promesa escrita de un instrumento no es alcance nuevo* | **17246** |

### b) **UN VEREDICTO AUSENTE NO ES UN PAR SIN LEER A EFECTOS DE `P.10`: ADJUDICADO POR EXTENSION, CON SUS CUATRO LETRAS**

**No es doctrina nueva y el acta lo dice al adjudicarla** (linea **17255**): sale **por extension de
cuatro letras vigentes**, y las cuatro se copian aqui porque **el registro no puede depender del
acta**.

| | la letra, copiada de su linea del acta | linea |
|---|---|---:|
| **PRIMERA** | **`P.10` dice EN LA PRACTICA que se listan sus pares LEIDOS y se busca el triangulo `A` mas `A` mas `D`**: el disparador **esta definido sobre veredictos escritos, y es mecanico** | **17257** |
| **SEGUNDA** | **`P.5` con su correccion de alcance** (15 ago, decision del fundador) fija que **la lectura debida es la del ACTO entero** (sus textos, y la pregunta de una familia o dos), y que **extender deberes de lectura mas alla de lo que la operacion escribio abre un re cribado que ninguna operacion escribio y que nadie adjudico** | **17260** |
| **TERCERA** | **el recomputo de la propia `OP-U-02` cuenta `en_cola_sin_leer` APARTE de `fuera_de_cola`**, y **los 47 actos del tramo tienen CERO pares en cola sin leer**: *lo que falta no es lectura pendiente, es propuesta que la semejanza nunca hizo* | **17265** |
| **CUARTA** | **el tramo unico se fijo en la vuelta 64 con los 47 `ABIERTOS` como universo de fusion**, verificado por acta, **y el encargo mando fundir su prefijo**: la lectura contraria **anularia la operacion entera que el plan sello** | **17269** |

> **Y LA LETRA EN DIVERGENCIA NO SE DEJA CALLADA** (linea **17273**): la **verificacion** de la ficha
> de `OP-U-02` dice *el acto se leyo ENTERO antes de fundirse: cero pares internos sin veredicto*,
> **escrita en la era en que la componente era el par** (en `OP-U-01`, tamano dos y puro `A`, la
> clausula era **trivialmente cierta**). **Leida a la letra hoy anularia los 47 actos del tramo,
> incluida la parte ya ejecutada y verificada.** **Su CORRECCION DECLARADA va encargada** por el
> carril del **banco 9.10**, el mismo que **la propia ficha ya uso en su evidencia (vuelta 48)**:
> **texto viejo verbatim y la vara nueva escrita al lado**, y **es la TAREA 1.b de la vuelta 66**.

**LO QUE ESTO FIJA PARA TODO EL TRAMO, dicho como procedimiento y no como glosa:** **el disparador
que detiene una fusion por `P.10` es el TRIANGULO `A` mas `A` mas `D` MEDIDO**, y **los actos con
puente cierran `DECLARADOS Y NO FUNDIDOS` con motivo sellado, como el acto 1**.

### c) **UN ACTO CON DOS O MAS PUERTAS CIERRA `DECLARADO Y NO FUNDIDO`, CON LA GUARDA `1B` COMO MOTIVO SELLADO**

**Adjudicado POR EXTENSION** (linea **17293**), **y tampoco es doctrina nueva**: **la guarda `1B`
prohibe absorber una puerta** y **el carril del `DECLARADO Y NO FUNDIDO` CON MOTIVO SELLADO ya
existe** desde el acto 1 (linea **3744** de esta pagina).

> **Si aparece un acto que no se pueda fundir sin absorber una puerta, cierra `DECLARADO` con la
> guarda `1B` como motivo, SIN improvisar fusiones parciales que ninguna letra escribe.** **Que
> hacer con el despues comparte destino con el pendiente 2 de aqui abajo.**

**Y EL CASO DE UNA SOLA PUERTA NO ES ESTE Y SE DICE PARA QUE NO SE CONFUNDAN:** con **una** puerta el
acto **si se funde**, **la puerta sobrevive** (acta 54, pregunta 1) **y el choque con la vara de
contenido queda escrito en el motivo sellado**, que es lo que esta misma pagina ya registro en el
**acto 20** de un tramo de `OP-U-01`.

### d) **LA CAIDA DE ACTA DEL AUDITOR, CON SU NOMBRE, Y LA RACHA DE REPORTE DE VUELTA A CERO**

**Se registra aqui porque el registro no depende del acta, y porque una caida que solo vive en un
acta se olvida.** **Esta vez la caida es del AUDITOR y no del ejecutor** (linea **17171**): **el
resumen del commit del acta 64 y el encargo de la vuelta 65 dicen NUEVE discutibles `A FAVOR` cuando
la propia acta adjudico OCHO `A FAVOR` y UNO como caida de procedimiento**. **El NUEVE por OCHO.**

> **Vive en un mensaje de commit y en un encargo, NO movio ningun dato**, y **el ejecutor la cazo y
> declaro la divergencia en vez de copiarla, que es exactamente el manejo debido** (es su `D1`).
> **Cuenta en la metrica del auditor como caida de acta.**

**Y LAS CIFRAS DE LA TANDA, copiadas de su linea:** **EJECUTOR CERO de clase, CERO de cifra publicada
y CERO de reporte** (linea **17163**); **cinco averias propias declaradas y cazadas ANTES de publicar
cifra alguna**, y **averia declarada y cazada antes de publicar no es caida: es el sistema
mordiendo**. **LA RACHA DE REPORTE VUELVE A CERO** y **CLASE O CIFRA sigue EN CERO, decima tanda
limpia** (linea **17338**).

### e) **LOS PENDIENTES 2 Y 4, NOMBRADOS CON SU DESTINO: EL CIERRE DE LA FASE 03**

**Se registran porque mandan sobre lo que viene aunque no encarguen trabajo hoy.**

| pendiente | lo que el acta fija, copiado de su linea | destino | linea |
|---|---|---|---:|
| **2. el subconjunto cerrado de un acto con puente** | **PENDIENTE NOMBRADO, sin urgencia medida.** `P.10` lo condiciona a que **todas** las lecturas esten hechas, y en los actos con puente **no lo estan ni pueden estarlo sin lecturas nuevas que ninguna operacion escribio**. **Los actos con puente cierran `DECLARADOS` cuando les llegue el turno y el carril existe** | **el CIERRE DE LA FASE 03** (mesa, enlace, o lecturas dirigidas autorizadas como la excepcion del racimo mixto de `OP-D-04`), **con el fundador delante si pide lecturas nuevas** | **17284** |
| **4. la marca para *ya lo dice el `APPEND` de un hermano*** | **PENDIENTE NOMBRADO.** El carril vigente (**`APPEND` con solape declarado** o **`CUBIERTO` con atenuante declarado**) **alcanza, y la vuelta 65 lo probo dos veces**; **estrenar una marca nueva en el contrato del plan es doctrina de instrumento que nadie necesita HOY** | **el mismo trato que el `INCISO` de condiciones** (acta 55, pregunta 5): **anotado, no encargado** | **17299** |

**Y los otros dos quedan donde el acta los dejo y aqui se dice para que no parezca omision:** el
**5** (el `INCISO` de condiciones, heredado) **sigue en su carril**, con **tres perdidas `DE
CONDICIONES` mas** en la vuelta 65 enrutadas a la fase 04 (linea **17305**); y el **6** (el esquema de
`OPERACIONES.jsonl`, heredado) **sigue pendiente y el campo `nota` lo cubre**, y **la correccion
encargada en el apartado b) usa el carril de texto que la ficha ya uso, SIN clave nueva** (linea
**17307**).

### f) **LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya**

**NO toca ni una cifra publicada arriba, NO elige ningun superviviente, NO funde nada, NO deshace
ninguna fusion y NO re-lee ni un veredicto de las dos colisiones vigentes**, cuya **linea base sigue
en `2`** y cuya duena sigue siendo la mesa `OP-M-03`. Registra adjudicaciones.


---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE B` (2026-08-20, vuelta 66)

**Va bajo la cabecera de tramo que la vuelta 65 adoso** (linea **3732**, cotejada hoy) y **no
reescribe ni una linea de arriba.** **NINGUNA TABLA DE AQUI SE TECLEA** (regla 1): las del reparto
pieza a pieza y las de piezas por absorbido **se generan del plan sellado**
[`../loop/PLAN_V66_OPU02_LOTE_B.json`](../loop/PLAN_V66_OPU02_LOTE_B.json), las de perdidas **se
recortan de la salida del tallador**, y las celdas de guardas y censos **se extraen por aguja** de
las salidas de esta vuelta con `python scripts/loop/vuelta66_registro_lote_b.py`.

**EL LOTE, DECLARADO AL ABRIRLO Y ENTREGADO ENTERO:** **PREFIJO SIN SALTOS** del `orden_universo` de
lo que quedaba del tramo (el lote A cerro los actos **1** y **3**): **los actos 5, 7, 8, 9, 10 y 11,
SEIS actos y 37 nodos.** **TRES cierran FUNDIDOS** (7, 8 y 9) y **TRES cierran `DECLARADOS Y NO
FUNDIDOS` con motivo sellado** (5, 10 y 11).

| | |
|---|---:|
| nodos VIVOS antes de la operacion | **3262** |
| nodos VIVOS despues | **3247** |
| nodos que MUEREN | **15** |
| piezas repartidas | **107** |
| ficheros tocados | **65** |
| duplicadas que la propia fusion fabrico y `P.16` limpio en el mismo commit | **10** |
| **grupos de duplicadas FABRICADOS de verdad** (diff por instrumento, apertura contra cierre) | **0** |
| colisiones de clase **ESPERADAS**, medidas ANTES de fundir sobre el arbol de antes | **4** |
| colisiones de clase **MEDIDAS** por el censo al cierre | **4** |
| actos del recomputo al cierre | **75** |
| de ellos `ABIERTOS` | **49** sobre **212** nodos |

> **LAS COLISIONES CALZAN Y LA CUENTA SE MIDIO ANTES, QUE ES LA MITAD DEL PUNTO** (adjudicacion 3 del
> encargo de esta vuelta): **esperadas 4** sobre la linea base **2** de la mesa `OP-M-03`,
> con **2 NUEVAS** que la fusion del **acto 8** fabrica
> (`cierre_satisfaccion_postventa` contra `cierre_segun_complejidad_venta`, y
> `cierre_segun_complejidad_venta` contra `obtencion_compromiso`, las dos `B` contra `D`), y
> **medidas 4: LAS MISMAS CUATRO**. **Las dos de la mesa no se tocan**, y su carril sigue
> siendo el de la linea **1377**.

### a) **EL `ACTO 7`: LA FAMILIA DEL `DMAIC` Y LA SECUENCIA UNIVERSAL DE JURAN**

**Sobrevive `six_sigma_dmaic` y absorbe CINCO.** **`P.5` contestada por medicion:** los seis del
**mismo libro** (Juran), **7 pares internos con veredicto y los 7 en `A`**, **cero `D`** y **cero
puentes**. **La vara que elige es EL CABLEADO SOLO, y su letra es `P.8`:** la FORMA medida es
**`CONTENIDO EMPATA`** (pasos empatan en 6 a tres bandas, condiciones en 3 a dos bandas), y entonces
**decide el cableado solo**: **11 contra un maximo de 5**. **El superviviente pasa de 6 a
12 pasos y de 3 a 8 condiciones.**

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `breakthrough_desempeno_actual` | 5 | 2 | 0 | 7 | 0 |
| `secuencia_universal_breakthrough` | 6 | 2 | 6 | 2 | 0 |
| `secuencia_universal_para_el_breakthrough` | 6 | 2 | 3 | 5 | 0 |
| `seis_sigma_servicios` | 5 | 2 | 1 | 6 | 0 |
| `six_sigma_dmaic_2` | 5 | 3 | 1 | 7 | 0 |
| **los 5 juntos** | **27** | **11** | **11** | **27** | **0** |

**El reparto, pieza a pieza:**

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `breakthrough_desempeno_actual` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **2** de `breakthrough_desempeno_actual` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `breakthrough_desempeno_actual` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| paso **4** de `breakthrough_desempeno_actual` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| paso **5** de `breakthrough_desempeno_actual` | `CUBIERTO` | ya lo dice el **paso 6** del superviviente |
| condicion **1** de `breakthrough_desempeno_actual` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `breakthrough_desempeno_actual` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **1** de `secuencia_universal_breakthrough` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **2** de `secuencia_universal_breakthrough` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `secuencia_universal_breakthrough` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `secuencia_universal_breakthrough` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| paso **5** de `secuencia_universal_breakthrough` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **6** de `secuencia_universal_breakthrough` | `CUBIERTO` | ya lo dice el **paso 6** del superviviente |
| condicion **1** de `secuencia_universal_breakthrough` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **2** de `secuencia_universal_breakthrough` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `secuencia_universal_para_el_breakthrough` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `secuencia_universal_para_el_breakthrough` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `secuencia_universal_para_el_breakthrough` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| paso **4** de `secuencia_universal_para_el_breakthrough` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| paso **5** de `secuencia_universal_para_el_breakthrough` | `CUBIERTO` | ya lo dice el **paso 6** del superviviente |
| paso **6** de `secuencia_universal_para_el_breakthrough` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `secuencia_universal_para_el_breakthrough` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **2** de `secuencia_universal_para_el_breakthrough` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `seis_sigma_servicios` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **2** de `seis_sigma_servicios` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `seis_sigma_servicios` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| paso **4** de `seis_sigma_servicios` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| paso **5** de `seis_sigma_servicios` | `CUBIERTO` | ya lo dice el **paso 6** del superviviente |
| condicion **1** de `seis_sigma_servicios` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `seis_sigma_servicios` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `six_sigma_dmaic_2` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **2** de `six_sigma_dmaic_2` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `six_sigma_dmaic_2` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| paso **4** de `six_sigma_dmaic_2` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| paso **5** de `six_sigma_dmaic_2` | `CUBIERTO` | ya lo dice el **paso 6** del superviviente |
| condicion **1** de `six_sigma_dmaic_2` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `six_sigma_dmaic_2` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **3** de `six_sigma_dmaic_2` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |

**Las perdidas selladas en campo propio, recortadas de la salida del tallador:**

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V66_OPU02_LOTE_B.json | 7 | DE PARAMETRO DE PASO | EL APOYO DE QUIEN TE ASESORE al definir el problema, que es lo unico del acto que mete a un tercero en el paso de definir. El paso 2 del superviviente manda definir el problema con claridad y en una frase de diez segundos, pero lo deja como tarea de uno solo | paso 1 de breakthrough_desempeno_actual | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 7 | DE CONDICIONES | que el disparador incluya RETRASOS Y COSTOS CRONICOS y no solo defectos, y que lo que se ve afectado sea LA SATISFACCION DEL CLIENTE. La condicion 1 del superviviente habla de un problema cronico de calidad que ya se intento resolver sin exito duradero, y ninguna de esas tres cosas esta nombrada | condicion 1 de breakthrough_desempeno_actual | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V66_OPU02_LOTE_B.json | 7 | DE PARAMETRO DE PASO | que la nominacion del problema se haga A NIVEL DE GERENCIA, que es quien selecciona y no solo que se seleccione. El paso 1 del superviviente manda seleccionar el problema concreto y darse un plazo, pero no dice a que altura de la organizacion se decide | paso 1 de secuencia_universal_para_el_breakthrough | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 7 | DE PARAMETRO DE PASO | EL VIAJE DIAGNOSTICO con sus cuatro tiempos nombrados, sintomas, teorias, pruebas y causa raiz, que es el metodo con el que se llega a la causa. El paso 4 del superviviente manda analizar hasta encontrar la causa raiz pero no dice por que camino | paso 3 de secuencia_universal_para_el_breakthrough | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 7 | DE PARAMETRO DE PASO | que el remedio se PRUEBE BAJO CONDICIONES OPERATIVAS REALES antes de darlo por bueno, que es el viaje remedial. El paso 5 del superviviente manda implementar un remedio dirigido a la causa raiz, pero no manda probarlo en condiciones reales antes | paso 4 de secuencia_universal_para_el_breakthrough | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 7 | DE CONDICIONES | que el disparador sea buscar UNA MEJORA SIGNIFICATIVA Y NO INCREMENTAL. ATENUANTE DECLARADO, y se dice para que la perdida se pueda pesar: la condicion 1 de secuencia_universal_breakthrough viaja ENTERA de APPEND y dice literalmente cambio radical de desempeno, no solo mejora incremental | condicion 1 de secuencia_universal_para_el_breakthrough | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V66_OPU02_LOTE_B.json | 7 | DE PARAMETRO DE PASO | EL EJEMPLO CONCRETO DE SERVICIOS, reducir el ciclo de emision de credito, que es lo unico del acto que aterriza el metodo fuera de la manufactura. El paso 2 del superviviente manda definir el problema en una frase, sin ejemplo | paso 1 de seis_sigma_servicios | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 7 | DE CONDICIONES | que el proceso con el problema cronico sea UN PROCESO DE SERVICIO y que el problema sea CUANTIFICABLE. La condicion 1 del superviviente nombra el problema cronico de calidad sin decir de que tipo de proceso ni que tenga que poder contarse | condicion 1 de seis_sigma_servicios | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V66_OPU02_LOTE_B.json | 7 | DE PARAMETRO DE PASO | EL CHARTER como instrumento con el que se define el problema, y LOS OBJETIVOS DEL PROYECTO junto al problema. El paso 2 del superviviente manda definir el problema con claridad y en diez segundos, pero no nombra ni el documento ni los objetivos | paso 1 de six_sigma_dmaic_2 | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 7 | DE PARAMETRO DE PASO | RECOPILAR LA VOZ DEL CLIENTE (VOC) dentro del paso de medir, que es lo que evita medir solo hacia dentro. El paso 3 del superviviente manda medir la magnitud real de los sintomas con datos, y el cliente no aparece | paso 2 de six_sigma_dmaic_2 | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 7 | DE CONDICIONES | que el disparador sea buscar una mejora DE TIPO BREAKTHROUGH EN PROCESOS CRITICOS PARA EL CLIENTE. ATENUANTE DECLARADO: la condicion 1 de secuencia_universal_breakthrough viaja ENTERA de APPEND y nombra el cambio radical de desempeno; lo que si se pierde sin atenuante es que el proceso sea CRITICO PARA EL CLIENTE | condicion 3 de six_sigma_dmaic_2 | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |

> **CERO `INCISO` EN ESTE ACTO, Y EL MOTIVO ES MEDIBLE:** el criterio escrito de la politica del
> `INCISO` es **la legibilidad del paso resultante**, y **los SEIS pasos de `six_sigma_dmaic`
> terminan en punto**. Un inciso detras de un punto no se lee limpio, asi que **cada parametro
> concreto va `CUBIERTO` con su perdida nombrada y enrutada**, que es la otra mitad del mismo carril.

### b) **EL `ACTO 8`: LA FAMILIA DEL CIERRE EN LA VENTA GRANDE**

**Sobrevive `cierre_segun_complejidad_venta` y absorbe CINCO.** **`P.5` contestada por medicion:**
los seis de **SPIN Selling**, **9 pares internos con veredicto y los 9 en `A`**, **cero `D`**, **cero
puentes**, y **la familia ya estaba DECLARADA** por la razon del puesto **601**. **FORMA medida
`TODAS DE ACUERDO`:** 5 pasos contra un maximo de 4 y 3 condiciones contra un maximo de 2, **las dos
varas de contenido al mismo lado**; **el cableado no hace falta y no se usa** (`P.8` solo habla a
contenido empatado). **El superviviente pasa de 5 a 12 pasos y de 3 a 7
condiciones.**

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `cierre_segun_tamano_decision` | 4 | 2 | 2 | 4 | 0 |
| `cierre_sofisticacion_comprador` | 4 | 2 | 3 | 3 | 0 |
| `diferencias_venta_pequena_venta_grande` | 4 | 1 | 3 | 1 | 1 |
| `ineficacia_cierre_ventas_grandes` | 4 | 2 | 2 | 4 | 0 |
| `riesgo_tecnicas_cierre_venta_compleja` | 4 | 2 | 1 | 5 | 0 |
| **los 5 juntos** | **20** | **9** | **11** | **17** | **1** |

**El reparto, pieza a pieza:**

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `cierre_segun_tamano_decision` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `cierre_segun_tamano_decision` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **3** de `cierre_segun_tamano_decision` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `cierre_segun_tamano_decision` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `cierre_segun_tamano_decision` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **2** de `cierre_segun_tamano_decision` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **1** de `cierre_sofisticacion_comprador` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `cierre_sofisticacion_comprador` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `cierre_sofisticacion_comprador` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `cierre_sofisticacion_comprador` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `cierre_sofisticacion_comprador` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **2** de `cierre_sofisticacion_comprador` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `diferencias_venta_pequena_venta_grande` | `INCISO` | **`INCISO` ADOSADO** al paso 1: *su ciclo (una llamada vs múltiples), monto y visibilidad de la decisión* |
| paso **2** de `diferencias_venta_pequena_venta_grande` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `diferencias_venta_pequena_venta_grande` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `diferencias_venta_pequena_venta_grande` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `diferencias_venta_pequena_venta_grande` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `ineficacia_cierre_ventas_grandes` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `ineficacia_cierre_ventas_grandes` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `ineficacia_cierre_ventas_grandes` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `ineficacia_cierre_ventas_grandes` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| condicion **1** de `ineficacia_cierre_ventas_grandes` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `ineficacia_cierre_ventas_grandes` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **1** de `riesgo_tecnicas_cierre_venta_compleja` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `riesgo_tecnicas_cierre_venta_compleja` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `riesgo_tecnicas_cierre_venta_compleja` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `riesgo_tecnicas_cierre_venta_compleja` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `riesgo_tecnicas_cierre_venta_compleja` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **2** de `riesgo_tecnicas_cierre_venta_compleja` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |

**Las perdidas selladas en campo propio:**

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V66_OPU02_LOTE_B.json | 8 | DE PARAMETRO DE PASO | LOS TRES CRITERIOS DE CLASIFICACION DEL PORTAFOLIO, precio, riesgo e IMPACTO ORGANIZACIONAL, y el tercero es el que no es una cifra. El paso 1 del superviviente clasifica por valor, sofisticacion del cliente y relacion posventa, y ninguno de los tres es el impacto organizacional. NO SE ADOSA DE INCISO Y SE DICE POR QUE: el paso 1 YA recibe el inciso del paso 1 de diferencias_venta_pequena_venta_grande, y no se apila mas de un INCISO sobre el mismo paso (acta 64, pregunta 5) | paso 1 de cierre_segun_tamano_decision | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 8 | DE CONDICIONES | que el disparador sea querer optimizar la estrategia comercial SEGUN EL TICKET PROMEDIO, que es el unico sitio del acto donde el criterio de entrada es una cifra del negocio y no una caracteristica de la venta. La condicion 1 del superviviente habla de alto valor y ciclos largos, que es otra cosa | condicion 2 de cierre_segun_tamano_decision | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V66_OPU02_LOTE_B.json | 8 | DE PARAMETRO DE PASO | LOS SUJETOS CONCRETOS con los que no se presiona, compradores corporativos, PROCUREMENT y ejecutivos experimentados. El paso 3 del superviviente manda minimizar el cierre en la venta grande y relacional, pero describe la VENTA y no a QUIEN se le vende | paso 2 de cierre_sofisticacion_comprador | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 8 | DE PARAMETRO DE PASO | que la razon de no presionar entre llamadas sea que ESO REDUCE LA PROBABILIDAD DE EXITO FINAL, que es el dato empirico detras de la regla. El paso 3 del superviviente manda minimizar el cierre sin decir que pasa si no se hace | paso 2 de diferencias_venta_pequena_venta_grande | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 8 | DE PARAMETRO DE PASO | que lo que se sustituya al cierre sean PREGUNTAS QUE EXPLOREN LA NECESIDAD REAL, nombradas como enfoque consultivo. El paso 3 del superviviente manda enfocar el esfuerzo en las etapas de indagacion (SPIN), que es el nombre del metodo pero no el gesto de preguntar | paso 3 de cierre_sofisticacion_comprador | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 8 | DE PARAMETRO DE PASO | que el esfuerzo se ponga en las etapas previas DE INVESTIGACION Y DESARROLLO DE NECESIDADES y no en frases de cierre. El paso 3 del superviviente nombra la indagacion (SPIN) pero no la investigacion previa ni el desarrollo de la necesidad como dos tiempos | paso 3 de riesgo_tecnicas_cierre_venta_compleja | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 8 | DE CONDICIONES | que el sintoma que dispara sea LA BAJA SATISFACCION DE CLIENTES junto a los scripts de cierre agresivo. ATENUANTE DECLARADO, y se dice para que la perdida se pueda pesar: el paso 4 de ESTE MISMO nodo viaja ENTERO de APPEND y manda medir la satisfaccion posventa para detectar el dano, o sea que el gesto se salva aunque el disparador no | condicion 2 de riesgo_tecnicas_cierre_venta_compleja | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V66_OPU02_LOTE_B.json | 8 | DE CONDICIONES | que el disparador sea que el equipo usa tecnicas de cierre tradicionales SIN RESULTADOS. La condicion 3 del superviviente dice que los resultados del cierre agresivo no mejoran las ventas COMPLEJAS, que acota a un tipo de venta lo que aqui se dice del equipo entero | condicion 2 de ineficacia_cierre_ventas_grandes | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |

### c) **EL `ACTO 9`: EL PRIMER CHOQUE DE PUERTA DEL TRAMO, REGISTRADO EN VEZ DE TAPADO**

**Sobrevive `marco_analisis_mercado_cadena_suministro` y absorbe CINCO.** **`P.5` contestada por
medicion:** los seis de **Hugos**, **7 pares internos con veredicto y los 7 en `A`**, **cero `D`**,
**cero puentes**.

> **LAS DOS VIAS APUNTABAN A LADOS DISTINTOS Y SE DICE ENTERO.** La **vara de contenido** apunta a
> `cuatro_categorias_desempeno_cadena_suministro` con **las dos varas y ninguna en contra** (FORMA
> `TODAS DE ACUERDO`: **10 pasos contra un maximo de 5** y **4 condiciones contra un maximo de 3**), y
> ademas la razon del puesto **704** dice que **el marco largo se traga al corto**. **PERO
> `marco_analisis_mercado_cadena_suministro` ES PUERTA**, con la marca `TIENE QUE SOBREVIVIR` leida
> del dossier, y **la guarda `1B` prohibe absorber una puerta**. **LA PUERTA SOBREVIVE** por el
> **acta 54, pregunta 1**, que es el mismo carril con el que esta pagina cerro el **acto 20** de un
> tramo de `OP-U-01` (linea **2922**).
>
> **Y LA CONSECUENCIA VA DICHA Y NO ESCONDIDA:** el nodo que la vara elegia es el que **mas piezas
> manda de `APPEND`, OCHO de sus diez pasos**, y **el superviviente pasa de 5 a 21 pasos y
> de 2 a 7 condiciones**, que lo convierte en **el nodo mas largo que la campana ha
> fabricado**, por encima de los 15 del acto 3. **Ese bulto es consecuencia de la guarda y no de
> repartir mal**, y va **MARCADO DISCUTIBLE** en el reporte de esta vuelta.

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `clasificacion_mercados_cadena_suministro` | 5 | 3 | 5 | 2 | 1 |
| `cuatro_capacidades_mercado` | 4 | 2 | 2 | 4 | 0 |
| `cuatro_categorias_desempeno_cadena_suministro` | 10 | 4 | 9 | 5 | 0 |
| `estrategia_cuatro_capacidades_mercado` | 4 | 2 | 4 | 2 | 0 |
| `modelo_cuadrantes_mercado` | 4 | 2 | 1 | 5 | 0 |
| **los 5 juntos** | **27** | **13** | **21** | **18** | **1** |

**El reparto, pieza a pieza:**

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `clasificacion_mercados_cadena_suministro` | `INCISO` | **`INCISO` ADOSADO** al paso 2: *desarrollo, crecimiento, estable o maduro* |
| paso **2** de `clasificacion_mercados_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `clasificacion_mercados_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `clasificacion_mercados_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **5** de `clasificacion_mercados_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `clasificacion_mercados_cadena_suministro` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `clasificacion_mercados_cadena_suministro` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **3** de `clasificacion_mercados_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `cuatro_capacidades_mercado` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **2** de `cuatro_capacidades_mercado` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| paso **3** de `cuatro_capacidades_mercado` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `cuatro_capacidades_mercado` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| condicion **1** de `cuatro_capacidades_mercado` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `cuatro_capacidades_mercado` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `cuatro_categorias_desempeno_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **2** de `cuatro_categorias_desempeno_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `cuatro_categorias_desempeno_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `cuatro_categorias_desempeno_cadena_suministro` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| paso **5** de `cuatro_categorias_desempeno_cadena_suministro` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **6** de `cuatro_categorias_desempeno_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **7** de `cuatro_categorias_desempeno_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **8** de `cuatro_categorias_desempeno_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **9** de `cuatro_categorias_desempeno_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **10** de `cuatro_categorias_desempeno_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `cuatro_categorias_desempeno_cadena_suministro` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `cuatro_categorias_desempeno_cadena_suministro` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **3** de `cuatro_categorias_desempeno_cadena_suministro` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **4** de `cuatro_categorias_desempeno_cadena_suministro` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `estrategia_cuatro_capacidades_mercado` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **2** de `estrategia_cuatro_capacidades_mercado` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `estrategia_cuatro_capacidades_mercado` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `estrategia_cuatro_capacidades_mercado` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `estrategia_cuatro_capacidades_mercado` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **2** de `estrategia_cuatro_capacidades_mercado` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `modelo_cuadrantes_mercado` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **2** de `modelo_cuadrantes_mercado` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| paso **3** de `modelo_cuadrantes_mercado` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `modelo_cuadrantes_mercado` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| condicion **1** de `modelo_cuadrantes_mercado` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **2** de `modelo_cuadrantes_mercado` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |

**Las perdidas selladas en campo propio:**

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE PARAMETRO DE PASO | ANALIZAR LA RELACION ENTRE OFERTA Y DEMANDA DE LA INDUSTRIA como la medicion con la que se decide el cuadrante. SE DICE LO QUE NO SE PIERDE: el paso 2 de clasificacion_mercados_cadena_suministro viaja ENTERO de APPEND y trae ese analisis; lo que se pierde es que sea EL CRITERIO del diagnostico del paso 1 de modelo_cuadrantes_mercado, que va CUBIERTO al paso 2 del superviviente | paso 1 de modelo_cuadrantes_mercado | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE PARAMETRO DE PASO | que la comparacion sea contra LOS ESTANDARES ESPERADOS PARA TU TIPO DE MERCADO y no solo contra la competencia. El paso 3 del superviviente compara con la competencia en las cuatro areas, que es otra vara: un mercado entero puede estar por debajo del estandar y la comparacion con el vecino no lo dice | paso 5 de cuatro_categorias_desempeno_cadena_suministro | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE PARAMETRO DE PASO | LAS METRICAS ESPECIFICAS POR CAPACIDAD con sus ejemplos, fill rate y tiempo de entrega. ATENUANTE DECLARADO: el paso 1 de cuatro_categorias_desempeno_cadena_suministro viaja ENTERO de APPEND y manda definir metricas concretas para cada una de las cuatro categorias; lo que se pierde son los DOS EJEMPLOS, que son lo que hace ejecutable el paso | paso 4 de cuatro_capacidades_mercado | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE PARAMETRO DE PASO | que lo que se identifique sea LA VENTAJA COMPETITIVA YA EXISTENTE, o sea donde ya se es mejor, como insumo de la decision. El paso 4 del superviviente decide si liderar, igualar o superar en cada area, pero no manda antes localizar la fortaleza que ya se tiene | paso 2 de cuatro_capacidades_mercado | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE PARAMETRO DE PASO | que la fortaleza relativa se mida FRENTE A COMPETIDORES y de forma RELATIVA. SE DICE LO QUE NO SE PIERDE: el paso 3 del superviviente ya compara con la competencia en las cuatro areas; lo que se pierde es que esa comparacion sirva para elegir DONDE CONCENTRARSE, que llega igual por el APPEND del paso 3 de estrategia_cuatro_capacidades_mercado | paso 2 de estrategia_cuatro_capacidades_mercado | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE PARAMETRO DE PASO | que las capacidades a reforzar se elijan SEGUN EL CUADRANTE detectado, y que sean esas cuatro nombradas (servicio, eficiencia, flexibilidad o desarrollo de producto). ATENUANTE DECLARADO: el paso 2 de cuatro_categorias_desempeno_cadena_suministro viaja ENTERO de APPEND y manda determinar cual categoria es critica SEGUN EL CUADRANTE de mercado en el que operas, que es ese mismo amarre | paso 2 de modelo_cuadrantes_mercado | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE PARAMETRO DE PASO | AJUSTAR LA MEZCLA de capacidades, o sea que la decision no es por area suelta sino sobre el reparto entre las cuatro. ATENUANTE DECLARADO, el mismo del paso 2: el APPEND del paso 2 de cuatro_categorias_desempeno_cadena_suministro trae la priorizacion por cuadrante | paso 4 de modelo_cuadrantes_mercado | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE CONDICIONES | que el disparador sea NO SABER COMO PRIORIZAR RECURSOS SEGUN EL TIPO DE MERCADO. La condicion 2 del superviviente dice no tener claro en que areas enfocar los recursos para competir, y le falta el amarre al tipo de mercado, que es lo que esta familia aporta | condicion 2 de clasificacion_mercados_cadena_suministro | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE CONDICIONES | que el disparador sea necesitar ESTABLECER KPIs de cadena de suministro, que es una entrada por el instrumento y no por la oportunidad. La condicion 1 del superviviente entra por definir oportunidades para la cadena de suministro | condicion 1 de cuatro_categorias_desempeno_cadena_suministro | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE CONDICIONES | que el disparador sea necesitar EVALUAR OBJETIVAMENTE el desempeno de la cadena, con el acento en lo objetivo. La condicion 2 del superviviente habla de no tener claro en que areas enfocar los recursos, que es una duda de foco y no de metodo | condicion 3 de cuatro_categorias_desempeno_cadena_suministro | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE CONDICIONES | que el disparador sea DEFINIR LA ESTRATEGIA DE INVERSION EN OPERACIONES. La condicion 1 del superviviente entra por definir oportunidades de cadena de suministro, que es el paso anterior y no la decision de inversion | condicion 1 de cuatro_capacidades_mercado | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V66_OPU02_LOTE_B.json | 9 | DE CONDICIONES | que el disparador sea NO TENER CLARO QUE PRIORIZAR entre servicio, eficiencia, flexibilidad o innovacion, con las cuatro nombradas. La condicion 2 del superviviente dice no tener claro en que areas enfocar los recursos sin nombrar ninguna | condicion 2 de modelo_cuadrantes_mercado | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |

> **LOS CUATRO CALCULOS FINANCIEROS SE OBSERVAN Y NO SE ACTUAN.** Los pasos **7 a 10** de
> `cuatro_categorias_desempeno_cadena_suministro` (rotacion de inventario, retorno sobre ventas,
> ciclo de conversion de efectivo, y mirar cuentas por cobrar y pagar antes que el inventario)
> **tienen la firma de un bloque pegado**: los pasos 1 a 6 de ese nodo son el tablero de las cuatro
> categorias y estos cuatro no vuelven a nombrarlas. **La observacion se REGISTRA y no se EJECUTA:**
> decidir si eso es un injerto es materia de **DESTEJIDO** (`P.3` y `P.19`) y **ninguna operacion
> escrita lo nombra**. Los cuatro viajan enteros de `APPEND` y la fase 04 poda. **Fundir no es sitio
> para destejer.**

### d) **EL `ACTO 5`: `DECLARADO Y NO FUNDIDO` POR `P.5`, Y ES LA PRIMERA VEZ QUE LA CAMPANA CIERRA UN ACTO POR LA PREGUNTA DE `P.5` Y NO POR EL TRIANGULO DE `P.10`**

| | |
|---|---|
| **acto** | **5** del `orden_universo` |
| **miembros** | **8**, y **NINGUNO se toca** |
| **combinaciones internas** | 28 |
| **pares `A` internos** | 9 |
| **pares `D` internos** | **0** (por eso `P.10` NO se dispara aqui) |
| **pares sin veredicto escrito** | 19 |
| **NODOS PUENTE** | **0** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **0** |
| **PUERTAS dentro del acto** | **NINGUNA**, la guarda `1B` pasa por vacio y se dice |
| **el nodo que PEGA la componente** | `design_test_repeat`, con sus `A` en los puestos **723**, **796**, **1182**, **1449**, **1573** |
| **lo que solo entra por el** | `design_thinking_proceso`, `testing_process_completo`, `desarrollo_en_espiral` |
| **instrumento** | [`../loop/SALIDA_V66_PUENTES_LOTE_B.txt`](../loop/SALIDA_V66_PUENTES_LOTE_B.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V66_DOSSIER_LOTE_B.txt`](../loop/SALIDA_V66_DOSSIER_LOTE_B.txt) |

> **`P.10` NO SE DISPARA AQUI, Y SE DICE PRIMERO** para que no se confunda con el acto **1** (linea
> **3744**): **cero `D` internos, cero nodos puente y cero triangulos**, medido. Por la adjudicacion
> del acta 65 **un veredicto ausente NO es un par sin leer**, asi que **con `P.10` sola este acto se
> fundiria**.
>
> **LO QUE LO DETIENE ES LA OTRA MITAD: la pregunta que `P.5` obliga a contestar antes de fundir, EL
> ACTO ES UNA FAMILIA O SON DOS.** Contestada sobre el texto estable de los ocho nodos leidos
> enteros, **NO ES UNA FAMILIA**: hay un **bucle de cuatro tiempos** (`build_measure_learn`,
> `ciclo_construir_medir_aprender`, `ciclo_crear_medir_aprender` y
> `startup_como_experimento_cientifico`, cerrados entre si por los puestos 213, 376, 486 y 1208) y
> hay **TRES PROCESOS LARGOS que lo contienen como UNO DE SUS PASOS** y que tienen procedimiento
> propio: `design_thinking_proceso` recorre entender, observar con etnografia, definir un punto de
> vista e idear antes de prototipar; `testing_process_completo` da forma con los dos lienzos, extrae
> hipotesis, disena con la tarjeta de test y mide con el Progress Board; `desarrollo_en_espiral` fija
> **que** se mide, **cuantas** vueltas y la documentacion de cada iteracion.
>
> **Y LOS TRES ENTRAN A LA COMPONENTE POR UN SOLO NODO QUE NO TIENE NADA PROPIO**,
> `design_test_repeat`, cuyas cinco `A` son la unica via. **Sus propias razones lo dicen cuatro
> veces:** el **796** lo llama *el ciclo desnudo contra el proceso que lo contiene* y dice que lo que
> anade *no llega ni a una linea*; el **1182** y el **1573** lo llaman **SUBCONJUNTO ESTRICTO**; y el
> **1573** avisa de que de `design_thinking_proceso` *se perderian CUATRO ETAPAS ENTERAS*.
>
> **`P.12` ES LA LETRA QUE CIERRA ESTO:** *el cierre transitivo convoca, la lectura decide*, y con el
> acto leido entero **mandan los veredictos DIRECTOS**, porque **una `A` que nadie leyo no existe**.
> **Fundir el acto entero sellaria que los tres procesos repiten ENTRE SI**, y **entre ellos no hay
> ni un solo veredicto escrito**.
>
> **LAS ALTERNATIVAS SE RECORREN EN VEZ DE ELEGIR LA COMODA:** leer los 19 pares que faltan es
> cribado que esta fase no tiene (banco 9.21 y regla 4); **fundir solo la sub-familia cerrada es una
> FUSION PARCIAL**, que el encargo de esta vuelta prohibe con todas sus letras; y fundir entero
> desmiente cuatro razones escritas. **ASI QUE NO SE FUNDE NADA Y SE DECLARA.** Es **reversible
> entero** y **no desmiente ninguna lectura escrita**, que es lo que el acta 65 dijo del acto 1 al
> adjudicarlo `A FAVOR`. **VA COMO PENDIENTE DE DOCTRINA** en el reporte, por la regla 5, **sin
> parar**: la letra no dice que hacer cuando `P.5` contesta DOS y `P.10` no se dispara, y **lo mejor
> sostenido es el carril que ya existe**.

### e) **LOS `ACTOS 10` Y `11`: `DECLARADOS Y NO FUNDIDOS` POR `P.10`, CON SU TRIANGULO MEDIDO**

**El `acto 10`, la familia del sales roadmap:**

| | |
|---|---|
| **acto** | **10** del `orden_universo` |
| **miembros** | **6**, y **NINGUNO se toca** |
| **combinaciones internas** | 15 |
| **pares `A` internos** | 6 |
| **pares `D` internos** | **4**, leidos y declarados DISTINTOS |
| **pares sin veredicto escrito** | 5 |
| **NODOS PUENTE** | **2** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **3** |
| **PUERTAS dentro del acto** | **NINGUNA**, la guarda `1B` pasa por vacio y se dice |
| **puestos de los `D` internos** | **872**, **1023**, **1306**, **1330** |
| **instrumento** | [`../loop/SALIDA_V66_PUENTES_LOTE_B.txt`](../loop/SALIDA_V66_PUENTES_LOTE_B.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V66_DOSSIER_LOTE_B.txt`](../loop/SALIDA_V66_DOSSIER_LOTE_B.txt) |

> **Las cuatro lecturas que una fusion entera desmentiria son DE UNA PIEZA y no un accidente:** las
> razones del **1306** y del **1330** dicen las dos **el contenido del mapa contra el uso del mapa**,
> y la del **872** dice **la economia de la venta contra el mapa de acceso** y declara que **el
> sub-puro del sales roadmap SE ROMPE**.

**El `acto 11`, la familia de la supervision de la IA:**

| | |
|---|---|
| **acto** | **11** del `orden_universo` |
| **miembros** | **5**, y **NINGUNO se toca** |
| **combinaciones internas** | 10 |
| **pares `A` internos** | 5 |
| **pares `D` internos** | **2**, leidos y declarados DISTINTOS |
| **pares sin veredicto escrito** | 3 |
| **NODOS PUENTE** | **2** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **2** |
| **PUERTAS dentro del acto** | **NINGUNA**, la guarda `1B` pasa por vacio y se dice |
| **puestos de los `D` internos** | **1496**, **1541** |
| **instrumento** | [`../loop/SALIDA_V66_PUENTES_LOTE_B.txt`](../loop/SALIDA_V66_PUENTES_LOTE_B.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V66_DOSSIER_LOTE_B.txt`](../loop/SALIDA_V66_DOSSIER_LOTE_B.txt) |

> **Las dos lecturas que una fusion entera desmentiria dicen LA MISMA FRONTERA con las mismas
> palabras:** el **1496** dice *uno protege la decision de hoy, el otro protege la capacidad de
> decidir de manana*, y el **1541** lo repite. Ademas el **1541** declara que con ese par **el racimo
> de la IA termina su cola** y que **la particion escrita NO se mueve**: **hay una frontera escrita
> dentro de este acto y una fusion entera la borraria**.

**Los TRES declarados quedan VIVOS Y ENTEROS**, sin un nodo tocado ni un superviviente elegido, y
**su destino comparte carril con el pendiente 2 del acta 65: el cierre de la fase 03.**

### f) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba, NO deshace ninguna fusion, NO re-lee ni un veredicto de las
colisiones vigentes, NO funde ningun acto con dueno, NO toca la mesa `OP-M-03` y NO ejecuta ninguna
de las cinco fichas `OP-M-02` consumidas.**


---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 66, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (25 ago 2026, vuelta 67, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **SIETE** veces: las tres adjudicaciones del acta 52 (linea **1250**),
la del acta 57 sobre el acto 25 (**2475**), las del acta 61 (**2689**), las del acta 62 (**2933**),
las del acta 63 (**3307**), las del acta 64 (**3613**) y las del acta 65 (**3962**), **las siete
cotejadas HOY abriendo el fichero**. **Ninguna cifra publicada se toca.** **Cada cita lleva la linea
LEIDA HOY**, no recordada, y **las CINCUENTA Y CINCO se imprimieron y se compararon antes de escribir
esta seccion** con `python scripts/loop/vuelta67_registrar_acta66.py --simular`, que cae en `ROJO`
sin escribir si una sola no calza: el acta de la vuelta 66 abre en la linea **17368** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), su seccion de adjudicaciones en la **17568**,
la de los pendientes en la **17632**, la de las caidas de la tanda en la **17544** y la de las
rachas en la **17712**.

**ESTA VUELTA NO TRAE CORRECCION DE FICHA, y se dice en vez de dejarlo en blanco:** el acta 66 **no
encargo ninguna**. La unica que estaba encargada, la de la clausula de la era del par de la ficha de
`OP-U-02`, **se escribio en la vuelta 66 y el auditor la leyo y la dio por buena** (la clausula vieja
verbatim como elemento 4 de `verificacion` y la correccion como elemento 7).

### a) **LOS DOCE DISCUTIBLES, ADJUDICADOS: LOS DOCE `A FAVOR`, Y DOS DE ELLOS POR EXTENSION CITABLE**

La columna de la vara **no es una glosa: es la regla citable con la que el auditor lo adjudico**, y
va copiada de su linea. **La cifra de cabecera y el detalle coinciden** (linea **17568**,
*ADJUDICACION DE LOS DOCE DISCUTIBLES*): doce marcados, doce adjudicados, **cero sin contestar**.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | **declarar el `ACTO 5` por la pregunta de `P.5` cuando `P.10` NO se dispara** | `A FAVOR` **POR EXTENSION CITABLE**, y el acta la llama **la adjudicacion de mas peso de la tanda**. La letra entera va en el apartado **b)** de aqui abajo. Lo esencial: **el encargo mismo MANDA contestar la pregunta de una familia o dos**; *una pregunta cuya respuesta negativa no tuviera consecuencia seria teatro*; **la consecuencia con carril escrito es el `DECLARADO Y NO FUNDIDO CON MOTIVO SELLADO`**, que el acta 65 ya extendio a un segundo motivo; y **fundir desmentiria cuatro lecturas escritas**, contra `P.12`, *y contra mi propia ciega, que llego a lo mismo* | **17570** |
| **`D2`** | **haber fundido el `ACTO 9` con el superviviente mas corto y fabricar el nodo mas largo de la campana** | `A FAVOR`. **El carril del choque de puerta esta escrito** (acta 54, pregunta 1, con el acto 20 de precedente): **la puerta sobrevive y el choque se registra**. *Declarar habria inventado un tercer carril sin letra.* **El nodo de 21 pasos es un bulto real, publicado, y la fase 04 existe** | **17579** |
| **`D3`** | **los pasos 7 a 10 de `cuatro_categorias_desempeno_cadena_suministro` de `APPEND` aunque parecen un injerto** | `A FAVOR`. **Fundir no desteje**: `P.3` y `P.19` son materia de destejido y **ninguna operacion escrita lo nombra**; **`APPEND` conserva el texto vivo para la poda de la fase 04**; **los cuatro viajaron VERBATIM** (cuenta del auditor) y **la sospecha quedo publicada con promesa de marcado cumplida por maquina** | **17584** |
| **`D4`** | **la linea base del censo de colisiones de `2` a `4`, con `OP-U-02` de duena** | `A FAVOR` **POR EXTENSION**, adjudicado entero en el apartado **c)** de aqui abajo | **17590** |
| **`D5`** | **cero `INCISO` en el `ACTO 7`, y el motivo es tipografico** | `A FAVOR`. **El criterio escrito es la legibilidad del paso resultante** (el carril de la vuelta 56 sobre puntuacion de incisos); **ocho `CUBIERTO` con perdida nombrada y atenuante es el costo publicado de aplicarlo, no un silencio** | **17592** |
| **`D6`** | **seis pasos de `APPEND` desde la secuencia universal al `DMAIC`** | `A FAVOR`. **La identidad que las razones declaran es del VIAJE** (breakthrough igual `DMAIC` como recorrido); **el andamiaje** (la creencia, el Pareto, los dos brazos, lo cultural, el proyecto formal, el replicar) **no esta en los seis pasos del `DMAIC`, y `CUBIERTO` lo habria callado**. El carril es el del `D9` del acta 65: **catalogo mas rico con solapes declarados** | **17596** |
| **`D7`** | **veintiuna piezas enteras en el `ACTO 9`** | `A FAVOR`, **mismo carril del `D9` del acta 65**, con **el costo publicado** y **la poda de la fase 04 como destino** | **17602** |
| **`D8`** | **las siete perdidas con atenuante declarado** | `A FAVOR`, **carril del `D8` del acta 63 y el `D10` del acta 65**: *sobre-sellar declarando es mas auditable que callar*. **La cuenta crece y esta contada** (pendiente 4) | **17604** |
| **`D9`** | **los dos cambios del cuadro de varas, y estrenar un instrumento de nombre estable el mismo dia** | `A FAVOR`. **Las dos condiciones del acta 61 estan cumplidas** (docstring y discutible); **la segunda averia del ancestro** (publicar una fila de DOS sobre actos de quince con los demas desaparecidos en silencio) **es de la especie que MIENTE, la peor, y no admitia esperar**; **el caso positivo mordio de verdad antes de publicar** (averia 7.1) y **sus tres mitades estan en verde re-corridas por el auditor**, con **el ancestro identico sobre el fixture de dos** | **17607** |
| **`D10`** | **corregir `caso_positivo_del_contrato_de_perdidas.py` sin encargo** | `A FAVOR`. *Un caso positivo que acusa en falso, committeado a sabiendas, es peor que el alcance: la proxima vez que acuse nadie le cree.* **El hallazgo es real** (roto desde la vuelta 63, ausente de las listas de las actas 64 y 65, leido por el auditor), **la correccion va declarada con el texto viejo verbatim**, y **las cuatro pruebas muerden** en su corrida | **17615** |
| **`D11`** | **la cita de linea `3959` que era `3962`, corregida con `grep`** | `A FAVOR` **con nota**. **La guarda existe para eso y mordio sin escribir nada**; **corregir con la medicion delante es legitimo**. *Re-derivar todas las citas por aguja queda como mejora de instrumento, no como deuda: se nombra y no se encarga* | **17621** |
| **`D12`** | **el fichero de apertura lleva `SIN ETIQUETA` en su titulo** | `A FAVOR`. **Copiar la salida real con el rotulo torcido Y DECIRLO vale mas que re-correr con datos de cierre bajo un rotulo de apertura, que seria fabricar.** El titulo dice *MEDICION DE SIN ETIQUETA*, leido por el auditor, **y las cifras son las de apertura, verificadas enteras en su worktree** | **17626** |

### b) **UN ACTO CUYO `P.5` CONTESTA QUE NO ES UNA FAMILIA CIERRA `DECLARADO Y NO FUNDIDO` CON `P.5` COMO MOTIVO SELLADO, AUNQUE `P.10` NO SE DISPARE: ADJUDICADO POR EXTENSION, CON SUS CUATRO LETRAS**

**No es doctrina nueva y el acta lo dice al adjudicarla** (linea **17634**): sale **por extension de
cuatro letras vigentes, la misma via del acta 65 con la guarda `1B`**, y las cuatro se copian aqui
porque **el registro no puede depender del acta**.

| | la letra, copiada de su linea del acta | linea |
|---|---|---:|
| **PRIMERA** | **`P.5` con su correccion de alcance** (15 ago, decision del fundador) **OBLIGA a contestar sobre el texto estable si el acto es UNA familia o DOS**; **el encargo de la vuelta lo repite con todas sus letras**. *Una pregunta obligatoria cuya respuesta negativa no tuviera consecuencia no seria una pregunta: seria un rito* | **17637** |
| **SEGUNDA** | **`P.12`** (*el cierre transitivo convoca, la lectura decide*) **manda que los veredictos DIRECTOS gobiernen**: **fundir el acto entero sellaria que los tres procesos repiten entre si, y entre ellos hay CERO veredictos**, contado por el auditor | **17641** |
| **TERCERA** | **el carril del `DECLARADO Y NO FUNDIDO CON MOTIVO SELLADO` ya existe y ya acepta mas de un motivo** (`P.10` de origen, la guarda `1B` por el acta 65): **anadir `P.5` como tercer motivo es la misma extension, no doctrina nueva** | **17645** |
| **CUARTA** | **las alternativas estan prohibidas por letra vigente**: **leer los 19 pares es cribado que la fase no tiene** (banco 9.21) **y la fusion parcial la prohibe el encargo con todas sus letras**. *La frase del encargo sobre el triangulo contesta a `P.10` y no abole la pregunta de `P.5` que el mismo encargo manda contestar dos parrafos despues* | **17648** |

> **LOS TRES MOTIVOS SELLABLES DEL `DECLARADO Y NO FUNDIDO`, ESCRITOS JUNTOS PARA QUE NADIE TENGA QUE
> RECONSTRUIRLOS:** **1)** el **triangulo `A` mas `A` mas `D` MEDIDO** (`P.10`, con el acto 1 de
> precedente en la linea **3744** de esta pagina); **2)** la **guarda `1B`**, cuando el acto no se
> puede fundir sin absorber una puerta (acta 65, registrada en la linea **4023** de esta pagina);
> **3)** la **respuesta DOS FAMILIAS de `P.5`** (acta 66, esta seccion). **El precedente del tercero
> es el `ACTO 5` de la vuelta 66**, registrado en la linea **4365**.

**Y NO ES PARADA, y el acta lo razona:** **nada se toca, es reversible entero, y la letra que faltaba
queda adjudicada por extension citable** (linea **17653**). **El destino de los declarados sigue
siendo el cierre de la fase 03**, con el pendiente 3 de aqui abajo.

### c) **UNA COLISION QUE FABRICA UNA FUSION TIENE DE DUENA A QUIEN LA FABRICA, Y LA LINEA BASE DEL CENSO QUEDA EN `4`**

**Adjudicado POR EXTENSION** (linea **17658**, *LA DUENA ES QUIEN LA FABRICA*), **y tampoco es
doctrina nueva**: es **el espiritu ya escrito de `P.16`** (*quien fabrica limpia, en el mismo
commit*) **aplicado a lo que no se puede limpiar sino solo gobernar**.

| | lo que el acta fija, copiado de su linea | linea |
|---|---|---:|
| **la razon** | **la colision nace de una sustitucion de `OP-U-02`, esta predicha en su plan, publicada en rojo y con dueno nombrado**; **mandarla a la mesa `OP-M-03` le colgaria a una mesa cerrada en decisiones un pasivo que no fabrico** | **17660** |
| **la linea base** | **LA LINEA BASE OPERATIVA DEL CENSO QUEDA EN `4`** (2 de la mesa mas 2 de `OP-U-02`) **y toda fusion siguiente mide sus esperadas SOBRE `4`** | **17663** |
| **lo que queda abierto** | **que hace la campana con las colisiones vigentes al cierre de la fase** (mesa nueva, enlace o saneo) **comparte destino con el pendiente 3 y lo vera el fundador en la parada del cierre de la fase 03** | **17665** |

> **LAS CUATRO, NOMBRADAS UNA A UNA PARA QUE EL CENSO SE PUEDA COTEJAR SIN ABRIR OTRO FICHERO:** las
> **dos de la mesa `OP-M-03`**, cuyo carril se registro en la linea **3653** de esta pagina y **que
> no se tocan**; y las **dos que la fusion del `ACTO 8` de la vuelta 66 fabrico**,
> `cierre_satisfaccion_postventa` contra `cierre_segun_complejidad_venta` y
> `cierre_segun_complejidad_venta` contra `obtencion_compromiso`, **las dos `B` contra `D`**,
> **REGISTRADAS, VIGENTES, EN ROJO y con `OP-U-02` de duena**.

**LA CONSECUENCIA OPERATIVA, dicha como procedimiento y no como glosa:** **toda fusion mide su cuenta
esperada ANTES de fundir, sobre el arbol de antes y simulando en memoria, CONTRA `4`**, y **un delta
no predicho es PARADA de guarda**. La frase de la linea **4055** de esta pagina que decia *cuya linea
base sigue en `2`* **queda envejecida por esta adjudicacion y NO se tacha**: se lee con su corte del
20 ago 2026 y **manda la de hoy**.

### d) **LA CAIDA DE PROCEDIMIENTO DEL ROL AUDITOR, CON SU NOMBRE, Y LAS DOS RACHAS**

**Se registra aqui porque el registro no depende del acta, y porque una caida que solo vive en un
acta se olvida.** **Esta vez la caida vuelve a ser del AUDITOR y no del ejecutor** (linea **17555**):
**una sesion de auditor corrio el 20 de agosto de 23:31 a 23:39, corrio ocho minutos de instrumentos
y termino SIN escribir acta, encargo ni parada.** Es **la especie de la vuelta 34**.

> **NO FABRICO HUECO DE VUELTA** y el acta lo mide: **ningun encargo se emitio y ninguna vuelta corrio
> sin auditar**. **El costo real existe y esta contado: CINCO dias de bucle parado**, hasta que el
> fundador ajusto el orquestador y `AUDITOR.md` (commits `eb91d502` y `51501552`) y relanzo. **Sus
> salidas quedaron sin trackear**, se committearon **como evidencia del incidente** y **NO se usaron
> como fuente de ninguna cifra**, que es la regla 2 aplicada al propio auditor. **Cuenta en la
> metrica del auditor como caida de procedimiento del rol.**

**Y LAS CIFRAS DE LA TANDA, copiadas de su linea:** **EJECUTOR CERO de clase, CERO de cifra publicada
y CERO de reporte** (linea **17547**); **tres averias propias declaradas y cazadas ANTES de publicar
cifra alguna**, y **averia declarada y cazada antes de publicar no es caida: es el sistema
mordiendo**. **LA RACHA DE REPORTE SIGUE EN CERO** (segunda tanda seguida) y **CLASE O CIFRA sigue EN
CERO, UNDECIMA tanda limpia** (linea **17712**).

### e) **LOS PENDIENTES 3 Y 4, NOMBRADOS CON SU DESTINO: EL CIERRE DE LA FASE 03, DONDE LA PARADA NUEVA ESPERA AL FUNDADOR**

**Se registran porque mandan sobre lo que viene aunque no encarguen trabajo hoy.**

| pendiente | lo que el acta fija, copiado de su linea | destino | linea |
|---|---|---|---:|
| **3. el subconjunto cerrado de un acto con puente** (heredado, acta 65 pendiente 2) | **sigue NOMBRADO y enrutado al cierre de la fase 03**, ahora con **CUATRO actos esperandolo**: el **1**, el **10** y el **11** por puente, y el **5** por la via de `P.5` | **el CIERRE DE LA FASE 03**, y **la parada nueva de `AUDITOR.md`** (`51501552`) **garantiza que el fundador lo ve antes del tramo mecanico** | **17669** |
| **4. la marca para *ya lo dice el `APPEND` de un hermano*** (heredado, acta 65 pendiente 4) | **sigue NOMBRADO**; **el carril vigente alcanza** y **la vuelta 66 lo pago siete veces con atenuante declarado**. *La cuenta crece y se publica; estrenar marca sigue siendo doctrina de instrumento que nadie necesita HOY* | **el mismo trato que el `INCISO` de condiciones** (acta 55, pregunta 5): **anotado, no encargado** | **17674** |

**Y los otros dos quedan donde el acta los dejo y aqui se dice para que no parezca omision:** el
**5** (el `INCISO` de condiciones, heredado) **sigue en su carril**, con **doce perdidas `DE
CONDICIONES` mas** en la vuelta 66 enrutadas a la fase 04 (linea **17679**); y el **6** (el esquema de
`OPERACIONES.jsonl`, heredado) **sigue pendiente y el campo existente lo cubre**, y **la correccion
de la ficha NO estreno clave**, leido por el auditor (**las mismas 18 claves en las 71**, linea
**17681**).

> **LA PARADA DEL CIERRE DE LA FASE 03 NO SE CUMPLE TODAVIA, y el acta lo mide** (linea **17731**):
> **quedan 39 actos y 139 nodos del tramo unico** al cierre de la vuelta 66, **6 de ellos con puente**
> (que cerraran `DECLARADOS`), **la mesa `OP-M-03`**, y **los declarados con su subconjunto sin
> resolver**. **Cuando el ultimo acto del tramo tenga destino y el cierre este verificado, la parada
> se ejecuta tal como esta escrita:** `PARA_ALEXIS.md` con el cierre medido y `PROMPT_SIGUIENTE`
> vacio.

### f) **LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya**

**NO toca ni una cifra publicada arriba, NO elige ningun superviviente, NO funde nada, NO deshace
ninguna fusion, NO re-lee ni un veredicto de las cuatro colisiones vigentes y NO corrige ninguna
ficha** (**ninguna quedo encargada**). **Registra adjudicaciones**, y **la unica cifra que mueve es
la linea base declarada del censo, de `2` a `4`, por la adjudicacion del apartado c)**, con la duena
nombrada y el texto viejo sin tachar.


---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE C` (2026-08-25, vuelta 67)

**Bajo la cabecera de tramo que la vuelta 65 adoso** (linea **3732** de esta pagina, cotejada hoy) y
**adosado al final sin reescribir ni una linea de arriba**. **EL LOTE SE DECLARO AL ABRIRLO Y ES
PREFIJO SIN SALTOS** del `orden_universo` de lo que quedaba (el lote A cerro los actos **1** y **3**,
el lote B cerro los actos **5**, **7**, **8**, **9**, **10** y **11**): **los actos 12, 13, 14, 15,
16 y 17, SEIS actos y 30 nodos, los seis cerrados ENTEROS.**

| acto | miembros | cierra | superviviente |
|---:|---:|---|---|
| **12** | 5 | **`DECLARADO Y NO FUNDIDO`**, y su motivo NO tiene letra: **PENDIENTE DE DOCTRINA** | ninguno se elige |
| **13** | 5 | **`DECLARADO Y NO FUNDIDO` por la guarda `1B`** | ninguno se elige |
| **14** | 5 | **`DECLARADO Y NO FUNDIDO` por `P.5`** | ninguno se elige |
| **15** | 5 | **`DECLARADO Y NO FUNDIDO` por la guarda `1B`** | ninguno se elige |
| **16** | 5 | **FUNDIDO** | `encuadre_desafio_diseno` |
| **17** | 5 | **`DECLARADO Y NO FUNDIDO` por `P.10`** | ninguno se elige |

> **UN LOTE CON UNA SOLA FUSION Y CINCO DECLARADOS, Y LA CIFRA SE PUBLICA EN VEZ DE MAQUILLARSE.** El
> contrato del lote es **PREFIJO CON TOPE, NO MINIMO** (acta 61, `D1` y pregunta 1), y **lo que la
> lectura da es lo que se entrega**. **Ninguno de los cinco declarados se declara por comodidad**:
> **dos por una guarda que prohibe la fusion**, **uno por la respuesta de `P.5`**, **uno por el
> triangulo de `P.10`** y **uno por una situacion que ninguna letra cubre y que va nombrada como
> tal**.

### a) **EL `ACTO 16`: LA FAMILIA DEL ENCUADRE DEL PROBLEMA (`HOW MIGHT WE`), Y LA PRIMERA VEZ QUE EL CABLEADO APUNTA AL OTRO LADO Y NO DECIDE**

| | |
|---|---|
| **superviviente** | `encuadre_desafio_diseno` |
| **absorbidos** | **4** |
| **nodos implicados / nodos que MUEREN** | 5 / 4 |
| **plan sellado** | [`../loop/PLAN_V67_OPU02_LOTE_C.json`](../loop/PLAN_V67_OPU02_LOTE_C.json), contrato **`CAMPO PROPIO v1`** |
| **vivos antes / despues** | 3247 / **3243** |

**LA PREGUNTA DE `P.5`, UNA FAMILIA O DOS, CONTESTADA CON MEDICION Y CON LAS RAZONES DELANTE:** los
**cinco** miembros tienen **CUATRO pares internos con veredicto escrito y los CUATRO son de clase
`A`**, hay **CERO pares `D` internos**, **CERO nodos puente** y **CERO triangulos**. **`P.10` solo
detiene una componente cuando aparece un triangulo `A` mas `A` mas `D`, y aqui no hay ninguno.**

**Y LAS CUATRO `A` ENCADENAN A LOS CINCO SIN UNA SOLA CONTRADICCION**, que es lo que separa una
familia leida de un cierre transitivo que solo cuenta: el puesto **525** encadena
`encuadre_desafio_diseno` con `how_might_we_framing`, el **264** encadena `how_might_we_framing` con
`how_might_we_hmw`, el **1319** encadena `how_might_we_hmw` con `how_might_we_briefs`, y el **236**
encadena `how_might_we_briefs` con `how_might_we_brief_social`.

> **EL PUESTO 1319 DECLARA LA UNION CON TODAS SUS LETRAS Y SE CITA EN VEZ DE RESUMIRSE:** *hasta hoy
> la familia HMW eran DOS componentes separadas*, y esa `A` *las UNE: por el cierre transitivo del
> banco 9.24 son ahora UNA SOLA de CINCO NODOS*. **El mismo veredicto nombra el gesto comun de los
> cinco**: *tomar el problema central, reformularlo con la formula de como podriamos, y CALIBRAR SU
> ALTURA para que no quede ni tan amplio que sea imposible de abordar ni tan estrecho que no deje
> espacio a soluciones*.

**EL SUPERVIVIENTE LO ELIGE EL CONTENIDO, Y AQUI EL CABLEADO APUNTA AL OTRO LADO:** la **FORMA
medida** es **`UNA SOLA VARA`**, la de **PASOS**, y apunta a `encuadre_desafio_diseno` con **5 contra
un maximo de 4**; la de **CONDICIONES empata en 2**. **El cableado apunta a `how_might_we_briefs`
con 8 contra 3, Y NO HABLA**, porque **`P.8` es regla de PRELACION**: *el desempate por cableado solo
habla a contenido empatado*, y **aqui el contenido dice algo**. **UNA SOLA VARA BASTA** (acta 53,
pregunta 4). **NI EL ROTULO SOLO NI LA CANTIDAD DECIDEN**: decide que `encuadre_desafio_diseno` es el
unico del acto que **ademas de formular la pregunta** define el impacto que se busca, documenta
contexto y restricciones, y manda revisar y ajustar la pregunta con lo aprendido. **NINGUN MIEMBRO DE
ESTE ACTO ES PUERTA**, medido al sellar.

#### EL REPARTO POR ABSORBIDO, TALLADO DEL PLAN SELLADO

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `how_might_we_brief_social` | 4 | 2 | 2 | 4 | 0 |
| `how_might_we_briefs` | 4 | 1 | 1 | 4 | 0 |
| `how_might_we_framing` | 4 | 2 | 2 | 3 | 1 |
| `how_might_we_hmw` | 4 | 2 | 1 | 4 | 1 |
| **los 4 juntos** | **16** | **7** | **6** | **15** | **2** |

#### EL REPARTO, PIEZA A PIEZA, TALLADO DEL PLAN SELLADO

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `how_might_we_brief_social` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `how_might_we_brief_social` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| paso **3** de `how_might_we_brief_social` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `how_might_we_brief_social` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `how_might_we_brief_social` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **2** de `how_might_we_brief_social` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `how_might_we_briefs` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **2** de `how_might_we_briefs` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **3** de `how_might_we_briefs` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `how_might_we_briefs` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| condicion **1** de `how_might_we_briefs` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **1** de `how_might_we_framing` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `how_might_we_framing` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `how_might_we_framing` | `INCISO` | **`INCISO` ADOSADO** al paso 5: *con el equipo hasta encontrar el nivel de abstracción correcto* |
| paso **4** de `how_might_we_framing` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `how_might_we_framing` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `how_might_we_framing` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **1** de `how_might_we_hmw` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `how_might_we_hmw` | `INCISO` | **`INCISO` ADOSADO** al paso 1: *utilizando la fórmula '¿Cómo podríamos...?'* |
| paso **3** de `how_might_we_hmw` | `CUBIERTO` | ya lo dice el **paso 5** del superviviente |
| paso **4** de `how_might_we_hmw` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `how_might_we_hmw` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `how_might_we_hmw` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |

> **LOS DOS `INCISO` DEL ACTO, Y POR QUE SON DOS Y NO MAS.** El superviviente viene del *field guide*
> de IDEO y **NO NOMBRA LA FORMULA** que le da nombre a la familia. **La formula viaja de `INCISO`
> adosado al paso 1, EXTRAIDA VERBATIM del paso 2 de `how_might_we_hmw`**, y el paso resultante se
> lee limpio porque **el paso 1 del superviviente no termina en punto**. **El segundo `INCISO` va al
> paso 5**, extraido VERBATIM del paso 3 de `how_might_we_framing`, y mete en el paso de revisar **lo
> unico que le faltaba: con quien se itera y cual es el criterio de parada**. **NO SE APILA MAS DE UN
> `INCISO` SOBRE EL MISMO PASO** (acta 64, registrada en esta pagina): los otros dos pasos que traen
> la formula, **el 1 de `how_might_we_framing` y el 2 de `how_might_we_briefs`**, van **`CUBIERTO`
> por el paso 1 y SIN perdida**, porque **el `INCISO` ya la trae**.

**EL SUPERVIVIENTE PASA DE 5 A 10 PASOS Y DE 2 A 3 CONDICIONES**, leido de
la salida de la ejecucion. **Piezas repartidas: 23 (6 viajan enteras, 15
ya estaban dichas).**

#### LAS PERDIDAS, SELLADAS EN CAMPO PROPIO (`CAMPO PROPIO v1`), RECORTADAS DE LA SALIDA DEL TALLADOR

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V67_OPU02_LOTE_C.json | 16 | DE PARAMETRO DE PASO | que de UN objetivo amplio salgan VARIAS preguntas y no una sola. El paso 1 del superviviente manda formular EL problema como UNA pregunta de diseno abierta, y el entregable de how_might_we_briefs pedia de tres a cinco preguntas | paso 1 de how_might_we_brief_social | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V67_OPU02_LOTE_C.json | 16 | DE PARAMETRO DE PASO | que la ESPECIFICIDAD se VERIFIQUE sobre la pregunta, con contexto, poblacion y restriccion, para que sea accionable. El paso 4 del superviviente documenta el contexto y las restricciones pero no los usa de vara sobre la pregunta. ATENUANTE DECLARADO: el APPEND del paso 2 de how_might_we_framing trae la calibracion de la altura de la pregunta por sus dos lados | paso 2 de how_might_we_brief_social | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V67_OPU02_LOTE_C.json | 16 | DE PARAMETRO DE PASO | que la FLEXIBILIDAD se verifique sobre LA PREGUNTA antes de idear, y no solo al listar soluciones. El paso 3 del superviviente manda listar posibles soluciones pensando ampliamente, que es un gesto posterior y sobre otra cosa. ATENUANTE DECLARADO: el APPEND del paso 2 de how_might_we_framing dice literalmente ni demasiado especifica, que limita soluciones | paso 3 de how_might_we_brief_social y paso 3 de how_might_we_briefs | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V67_OPU02_LOTE_C.json | 16 | DE CONDICIONES | el disparador SOCIAL, un problema social muy amplio, y el gesto de ACOTARLO para poder empezar a disenar. La condicion 2 del superviviente habla de falta de claridad sobre el alcance del problema, que es mas general y no nombra ni lo social ni el acotar | condicion 1 de how_might_we_brief_social | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V67_OPU02_LOTE_C.json | 16 | DE PARAMETRO DE PASO | que la especificidad se exija para CONECTAR CON LA VIDA REAL de los beneficiarios y no solo con el problema abstracto. Es una de las DOS perdidas que el puesto 1319 nombro de este nodo antes de que nadie fundiera nada, y el superviviente no la dice en ninguno de sus cinco pasos | paso 4 de how_might_we_briefs | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V67_OPU02_LOTE_C.json | 16 | DE CONDICIONES | la MISION FILANTROPICA sin punto de partida concreto como disparador. La condicion 2 del superviviente habla de falta de claridad sobre el alcance y no nombra ni la mision ni el objetivo abstracto sin punto de partida | condicion 1 de how_might_we_briefs | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V67_OPU02_LOTE_C.json | 16 | DE CONDICIONES | que el encuadre valga tambien para cualquier proyecto de INNOVACION y no solo para uno de diseno centrado en humanos, que es lo que dice la condicion 1 del superviviente. ES LA MISMA PERDIDA VISTA DESDE DOS NODOS y se sella UNA sola vez con sus dos sitios nombrados, en vez de dos, para no inflar el campo duplicando | condicion 1 de how_might_we_framing y condicion 1 de how_might_we_hmw | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V67_OPU02_LOTE_C.json | 16 | DE PARAMETRO DE PASO | la calibracion de la ALTURA de la pregunta por sus dos lados, ni demasiado amplio que sea imposible de resolver ni demasiado estrecho que limite la innovacion. El paso 5 del superviviente manda revisar y ajustar la pregunta segun lo aprendido pero no dice contra que vara. ATENUANTE DECLARADO: el APPEND del paso 2 de how_might_we_framing trae esa misma calibracion entera y con sus dos puntas | paso 3 de how_might_we_hmw | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V67_OPU02_LOTE_C.json | 16 | DE CONDICIONES | el ESTANCAMIENTO del equipo por los DOS extremos, un problema demasiado abstracto o demasiado restrictivo, como disparador. La condicion 2 del superviviente habla de falta de claridad sobre el alcance y no nombra ni el estancamiento ni los dos extremos | condicion 2 de how_might_we_hmw | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |

> **UNA PERDIDA SE SELLA UNA SOLA VEZ CON SUS DOS SITIOS NOMBRADOS, Y VA MARCADO DISCUTIBLE.** El
> disparador de **PROYECTO DE INNOVACION** lo traen la condicion 1 de `how_might_we_framing` **y** la
> condicion 1 de `how_might_we_hmw`, y **es LA MISMA perdida vista desde dos nodos**. Lo mismo con la
> verificacion de la **FLEXIBILIDAD**, que traen el paso 3 de `how_might_we_brief_social` y el paso 3
> de `how_might_we_briefs`. **Se sellan UNA vez con los DOS sitios escritos en el campo `donde`**, en
> vez de dos, porque **inflar la cuenta de perdidas duplicando una sola tambien falsea el campo**.

#### LAS GUARDAS Y LOS CENSOS, LEIDOS DE LA SALIDA DE LA EJECUCION

| guarda | resultado |
|---|---|
| **guarda 1** (miembros vivos y nomina completa) | **OK** |
| **guarda `1B`** (ningun absorbido es semilla ni extremo de puente) | **OK** |
| **guarda 2** (cobertura exacta de indices, cero olvidos) | **OK** |
| **guarda 3** (cero repetidos literales en el resultado) | **OK** |
| **`P.16`**, duplicadas que la propia fusion fabrica y limpia **en el mismo commit** | **2**, limpiadas en la misma corrida |
| **guarda A** (cero auto-aristas nuevas) y **guarda B** (cero duplicadas nuevas tras resolver) | **OK** las dos |
| **guarda C** (los campos que esta operacion NO redacta, intactos) y **guarda D** (los absorbidos conservan su texto INTACTO) | **OK** las dos |
| **pasivo historico del censo propio de la guarda** | **892 a 891** |
| **ficheros tocados** | **21** |

**EL DIFF DE DUPLICADAS, POR INSTRUMENTO Y CON LA APERTURA SACADA DE `git`**
([`../loop/SALIDA_V67_DIFF_DUPLICADAS.txt`](../loop/SALIDA_V67_DIFF_DUPLICADAS.txt)): **GRUPOS
FABRICADOS DE VERDAD: 0**, renombrados **0**, y el censo de `OP-S-12` pasa de
**915 a 914** grupos.

**EL CENSO DE COLISIONES, CON LAS ESPERADAS MEDIDAS ANTES DE FUNDIR SOBRE LA LINEA BASE QUE EL ACTA
66 ADJUDICO** (registrada en la linea **4542** de esta pagina):

| | |
|---|---:|
| linea base declarada **y MEDIDA sobre el arbol de antes** | **4** |
| colisiones NUEVAS que la fusion fabricaria | **0** |
| **ESPERADAS TRAS FUNDIR** | **4** |
| **MEDIDAS al cierre por el censo** | **4** |
| **CALZA** | **SI** |

**`reanclar_por_resolutor.py` corrido ENTRE la fusion y `run_phase1`**: **1 referencia
re-anclada**, y esta vez **no fue por vacio**: el rumbo `nucleo_quiero_algo_propio_sin_idea` apuntaba
a `how_might_we_hmw` y pasa a apuntar al superviviente. **Se corre siempre y se dice, en vez de darlo
por bueno.**

> **UNA CONSECUENCIA MEDIDA QUE SE DICE EN VEZ DE CALLARSE: LA COLA DE COSTURAS SUBE UNO.** De
> **1.447** a **1.448**, y **el que entra es `encuadre_desafio_diseno`**, el propio superviviente,
> **medido por diff contra la cola de la apertura sacada de `git`** y no supuesto. **Un nodo de 10
> pasos entrando a la cola de costuras internas es la consecuencia esperada de una fusion de cinco
> miembros**, y **queda enrutado a la fase 04 como el resto de la cola**.

### b) **EL `ACTO 12`: `DECLARADO Y NO FUNDIDO` POR ALGO QUE NINGUNA LETRA CUBRE, Y SE DICE ASI EN VEZ DE DISFRAZARLO DE MOTIVO CONOCIDO**

| | |
|---|---|
| **acto** | **12** del `orden_universo` |
| **MOTIVO SELLADO DEL CIERRE** | **un par `D` INTERNO DIRECTO sin triangulo que cerrar**, y NO es ninguno de los tres sellados: **PENDIENTE DE DOCTRINA** (regla 5) y **DISCUTIBLE** |
| **miembros** | **5**, y **NINGUNO se toca** |
| **combinaciones internas** | 10 |
| **pares `A` internos** | 5 |
| **pares `D` internos** | **1**, leidos y declarados DISTINTOS |
| **pares sin veredicto escrito** | 4 |
| **NODOS PUENTE** | **0** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **0** |
| **PUERTAS dentro del acto** | **NINGUNA**, la guarda `1B` pasa por vacio y se dice |
| **puestos de los `D` internos** | **1374** |
| **instrumento** | [`../loop/SALIDA_V67_PUENTES_LOTE_C.txt`](../loop/SALIDA_V67_PUENTES_LOTE_C.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V67_DOSSIER_LOTE_C.txt`](../loop/SALIDA_V67_DOSSIER_LOTE_C.txt) |

**LO PRIMERO QUE SE DICE ES QUE `P.10` NO SE DISPARA, medido y no supuesto:** **CERO nodos puente y
CERO triangulos**. **Y NINGUN MIEMBRO ES PUERTA**: la guarda `1B` pasa por vacio. **Con `P.10` sola y
con la guarda `1B` sola, este acto se fundiria**, y la FORMA habria apuntado a
`metrics_that_matter_framework`.

**LO QUE LO DETIENE ES EL PUESTO 1374, UN VEREDICTO `D` DIRECTO ENTRE DOS MIEMBROS:**
`cash_burn_calculation` contra `validacion_hipotesis_ingresos`, y su razon dice que los dos parten
del mismo dato, el ingreso neto de canal, y **salen por puertas distintas**: *uno responde cuanto
tiempo queda, el otro cuanto se puede gastar en traer al siguiente cliente*. **Una fusion de los
CINCO a un superviviente unico deprecaria a los dos contra el mismo vivo y SELLARIA QUE REPITEN ENTRE
SI**, que es exactamente lo que ese veredicto niega.

**LA FAMILIA ES UNA Y AUN ASI NO SE FUNDE, Y LAS DOS COSAS SE DICEN JUNTAS PORQUE NO SE
CONTRADICEN:** la pregunta de `P.5` se contesta **UNA**, y esta escrita con nombres propios en el
puesto **451**, que enumera **los CINCO** sobre el mismo modelo financiero del fin de la validacion,
sostenida por el **404** y el **807**. **Pero una familia con un `D` dentro es una familia
MEZCLADA**, que es el mismo nombre que el archivo usa en el puesto **863** para la familia de la
estrategia de innovacion cuando le entra su primer `D`. **FAMILIA NO ES FUSION:** la fusion exige
que **todos** los absorbidos REPITAN al superviviente.

**LAS CUATRO LETRAS QUE SOSTIENEN EL DECLARADO, cada una citable:**

| | la letra | |
|---|---|---|
| **PRIMERA** | **`P.10`** cierra con que **LO QUE NUNCA ES SALIDA ES FUNDIR LA COMPONENTE ENTERA PORQUE EL CIERRE TRANSITIVO LA JUNTA** | y aqui los dos nodos del `D` **solo coinciden en la componente por el camino** `cash_burn`, `metrics`, `verificar`, `validacion`: **la unica lectura DIRECTA entre ellos es el `D`** |
| **SEGUNDA** | **`P.12`** manda que el cierre transitivo convoque y **LA LECTURA DECIDA** | y la lectura decide **`D`** |
| **TERCERA** | el **acto 5 de la vuelta 66** (linea **4365** de esta pagina) se declaro porque fundir sellaria identidades **QUE NADIE LEYO** | y **aqui el caso es mas fuerte y no mas debil: alguien las leyo y dijo que no** |
| **CUARTA** | las **alternativas estan prohibidas por letra vigente** | leer los **4** pares que faltan es **cribado que esta fase no tiene** (banco 9.21), y fundir solo el subconjunto cerrado es una **FUSION PARCIAL** que el encargo prohibe con todas sus letras |

> **POR QUE NO ES PARADA Y SI ES PENDIENTE DE DOCTRINA:** **nada se toca, ningun nodo se depreca, es
> reversible entero y no desmiente ninguna lectura escrita**. La **regla 5** manda registrar lo mejor
> sostenido y seguir. **LO DISCUTIBLE, DICHO ANTES DE SABER SI ACIERTA:** el encargo de esta vuelta
> **enumera TRES motivos sellables** (el triangulo de `P.10`, la guarda `1B` y la respuesta *DOS
> FAMILIAS* de `P.5`) **y esa lista se puede leer como CERRADA**, y **leida asi este acto tenia que
> fundirse**.

### c) **LOS `ACTOS 13` Y `15`: LAS DOS PRIMERAS VECES DE LA CAMPANA EN QUE LA GUARDA `1B` ES EL MOTIVO UNICO**

**El carril lo escribio el acta 65 y esta pagina lo registro en la linea 4023:** *si aparece un acto
que no se pueda fundir sin absorber una puerta, cierra `DECLARADO` con la guarda `1B` como motivo,
SIN improvisar fusiones parciales que ninguna letra escribe*. **Hasta hoy ese carril existia y nadie
lo habia estrenado como motivo UNICO**: el acto 1 de la vuelta 65 tenia dos puertas, pero **su
motivo sellado fue `P.10`** y las puertas eran la segunda razon.

**El `acto 13`, la familia de la seleccion de canal de distribucion:**

| | |
|---|---|
| **acto** | **13** del `orden_universo` |
| **MOTIVO SELLADO DEL CIERRE** | **la guarda `1B`**, DOS puertas dentro (acta 65, registrada en la linea **4023**) |
| **miembros** | **5**, y **NINGUNO se toca** |
| **combinaciones internas** | 10 |
| **pares `A` internos** | 8 |
| **pares `D` internos** | **0** (por eso `P.10` NO se dispara aqui) |
| **pares sin veredicto escrito** | 2 |
| **NODOS PUENTE** | **0** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **0** |
| **PUERTAS dentro del acto** | **2**: `hipotesis_de_canales`, `seleccion_canal_distribucion` |
| **instrumento** | [`../loop/SALIDA_V67_PUENTES_LOTE_C.txt`](../loop/SALIDA_V67_PUENTES_LOTE_C.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V67_DOSSIER_LOTE_C.txt`](../loop/SALIDA_V67_DOSSIER_LOTE_C.txt) |

> **LA PREGUNTA DE `P.5` SE CONTESTA IGUAL Y SE DEJA ESCRITA, porque el acto se lee entero aunque no
> se funda: ES UNA FAMILIA, y no es lectura de esta vuelta sino declaracion del archivo.** El puesto
> **609** dice **FAMILIA DECLARADA** y nombra el racimo *LA SELECCION DE CANAL* de seis miembros, el
> **762** lo repite, y el **1488** cierra que el racimo **NO crece**, sigue en **SEIS** miembros, su
> cobertura pasa a **8 de 15** con los ocho en `A`, y **sigue siendo SUB-PURO**.
>
> **Y UNA COSA MAS QUE SE DICE EN VEZ DE CALLARSE:** el puesto **537** declara un **CHOQUE CON LA
> DIRECCION DE FUSION DE LA RELECTURA `R1`** y avisa con todas sus letras de que **la direccion de
> fusion NO se puede cerrar par por par**, porque *fisico y digital son especializaciones que el nodo
> general NO lleva*. **No es el motivo sellado, pero apunta al mismo sitio que la guarda.**

**El `acto 15`, la familia de la ecuacion de valor de Rackham:**

| | |
|---|---|
| **acto** | **15** del `orden_universo` |
| **MOTIVO SELLADO DEL CIERRE** | **la guarda `1B`**, DOS puertas dentro (acta 65, registrada en la linea **4023**) |
| **miembros** | **5**, y **NINGUNO se toca** |
| **combinaciones internas** | 10 |
| **pares `A` internos** | 5 |
| **pares `D` internos** | **0** (por eso `P.10` NO se dispara aqui) |
| **pares sin veredicto escrito** | 5 |
| **NODOS PUENTE** | **0** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **0** |
| **PUERTAS dentro del acto** | **2**: `ecuacion_de_valor`, `prevencion_objeciones_vs_manejo` |
| **instrumento** | [`../loop/SALIDA_V67_PUENTES_LOTE_C.txt`](../loop/SALIDA_V67_PUENTES_LOTE_C.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V67_DOSSIER_LOTE_C.txt`](../loop/SALIDA_V67_DOSSIER_LOTE_C.txt) |

> **Y SE DICE PRIMERO LO QUE ESTE ACTO NO ES, PORQUE SE PARECE Y NO LO ES: NO ES UN CHOQUE DE
> PUERTA.** En el choque, **la vara de contenido apunta a un miembro y la puerta es OTRO**, y el
> carril escrito manda **fundir A LA PUERTA y registrar el choque** (acta 54, pregunta 1, con el acto
> 9 de la vuelta 66 de precedente nuevo). **Aqui LAS TRES VARAS APUNTAN A LA PUERTA**
> (`prevencion_objeciones_vs_manejo`, con 6 pasos contra 4, 3 condiciones contra 2 y cableado 9
> contra 4), **o sea que no hay nada que chocar**. **Lo que hay es una SEGUNDA puerta dentro**,
> `ecuacion_de_valor`, **que cualquier fusion tendria que absorber**.
>
> **LA PREGUNTA DE `P.5` SE DEJA MEDIDA Y SIN CONTESTAR, Y ESO TAMBIEN SE DICE:** hay un nucleo de la
> ecuacion de valor de **cuatro** miembros que el archivo declara (puesto **217**, racimo nuevo de
> tres, y puesto **950**, que lo lleva a cuatro y **lo DEGRADA a SUB-PURO** con dos lecturas por
> hacer), y el quinto entra por el puesto **1146**, cuya razon avisa de que **no es un par de madre e
> hijo sino dos nodos laterales**. **Con la guarda `1B` deteniendo la fusion, la pregunta de si el
> quinto es de la misma familia NO HACE FALTA CONTESTARLA HOY y no se contesta**: se deja medida y
> escrita para quien la necesite.

### d) **EL `ACTO 14`: `DECLARADO Y NO FUNDIDO` POR `P.5`, Y ES EL SEGUNDO USO DEL CARRIL QUE EL ACTA 66 ADJUDICO**

| | |
|---|---|
| **acto** | **14** del `orden_universo` |
| **MOTIVO SELLADO DEL CIERRE** | **`P.5`**, que contesta **NO ES UNA** (acta 66, registrada en la linea **4518**) |
| **miembros** | **5**, y **NINGUNO se toca** |
| **combinaciones internas** | 10 |
| **pares `A` internos** | 7 |
| **pares `D` internos** | **0** (por eso `P.10` NO se dispara aqui) |
| **pares sin veredicto escrito** | 3 |
| **NODOS PUENTE** | **0** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **0** |
| **PUERTAS dentro del acto** | **NINGUNA**, la guarda `1B` pasa por vacio y se dice |
| **instrumento** | [`../loop/SALIDA_V67_PUENTES_LOTE_C.txt`](../loop/SALIDA_V67_PUENTES_LOTE_C.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V67_DOSSIER_LOTE_C.txt`](../loop/SALIDA_V67_DOSSIER_LOTE_C.txt) |

**El precedente es el acto 5 de la vuelta 66** (linea **4365**) y **la letra esta registrada en la
linea 4518 de esta pagina**. **`P.10` NO se dispara** (cero `D`, cero puentes, cero triangulos) y
**ningun miembro es puerta**: con las dos solas, este acto se fundiria.

**LA PREGUNTA DE `P.5` SE CONTESTA SOBRE EL TEXTO ESTABLE Y LA RESPUESTA ES `NO ES UNA`: HAY UN PURO
DE CUATRO Y UN QUINTO QUE LA LECTURA DEJA FUERA CON TODAS SUS LETRAS.**

| | lo que el archivo dice, leido del dossier |
|---|---|
| **el PURO de CUATRO** | el puesto **1030** declara que *CON ESTE PAR NACE EL PRIMER PURO DE CUATRO* y **enumera la familia**: `construccion_de_leverage`, `leverage_en_negociacion_con_vcs`, `gestion_multiples_term_sheets` y `estrategia_competencia_vcs`, **CUATRO miembros, SEIS pares posibles, LOS SEIS LEIDOS Y LOS SEIS EN `A`**, y anade que es el **PRIMER PURO DE CUATRO MIEMBROS del archivo**. **Cuatro, no cinco** |
| **el quinto, y no esta fuera por olvido** | el puesto **878** lo levanta por el **BARRIDO DE LAS `A`** del banco 9.15, **lo mira y decide**, y su razon dice que **LA LECTURA LO DEJA FUERA PORQUE SU OBJETO ES COMO NEGOCIAR TERMINOS Y NO COMO GENERAR COMPETENCIA ENTRE INVERSORES**. El mismo puesto llama a `tecnica_anclaje_negociacion` **el paso cuatro contado como nodo**, sin procedimiento propio |

> **LA VARA APUNTA AL NODO EXCLUIDO, Y ESO NO ES UN DETALLE.** La FORMA medida es `CONTENIDO EMPATA`
> (pasos empatan en 5 a dos bandas y condiciones en 2 a dos bandas), asi que por `P.8` decidiria **el
> cableado solo**, y el cableado apunta a `tecnica_anclaje_negociacion` con **7 contra un maximo de
> 6**. **Fundir el acto entero pondria de superviviente al mismo nodo que la lectura saco de la
> familia**, y **sellaria que el PURO DE CUATRO repite a un nodo que el archivo declara de otro
> objeto**. **`P.12` manda que los veredictos DIRECTOS gobiernen**, y el directo aqui dice que **el
> objeto es otro**.

**LAS ALTERNATIVAS, RECORRIDAS EN VEZ DE ELEGIR LA COMODA:** leer los **3** pares que faltan es
cribado que esta fase no tiene; **fundir solo el PURO DE CUATRO y dejar fuera al quinto es una FUSION
PARCIAL**, que el encargo prohibe con todas sus letras; y **fundir entero desmiente la lectura del
878**. **ASI QUE NO SE FUNDE NADA Y SE DECLARA.**

### e) **EL `ACTO 17`: `DECLARADO Y NO FUNDIDO` POR `P.10`, CON SU TRIANGULO MEDIDO, Y CON UNA SEGUNDA RAZON INDEPENDIENTE**

| | |
|---|---|
| **acto** | **17** del `orden_universo` |
| **MOTIVO SELLADO DEL CIERRE** | **`P.10`**, con su triangulo MEDIDO, **mas la guarda `1B` como segunda razon independiente** |
| **miembros** | **5**, y **NINGUNO se toca** |
| **combinaciones internas** | 10 |
| **pares `A` internos** | 6 |
| **pares `D` internos** | **2**, leidos y declarados DISTINTOS |
| **pares sin veredicto escrito** | 2 |
| **NODOS PUENTE** | **1** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **2** |
| **PUERTAS dentro del acto** | **1**: `estrategia_de_innovacion_y_tecnologia` |
| **puestos de los `D` internos** | **530**, **863** |
| **instrumento** | [`../loop/SALIDA_V67_PUENTES_LOTE_C.txt`](../loop/SALIDA_V67_PUENTES_LOTE_C.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V67_DOSSIER_LOTE_C.txt`](../loop/SALIDA_V67_DOSSIER_LOTE_C.txt) |

**Es el PRIMERO de los seis actos con puente que el acta 66 dejo contados al cierre** (los actos 17,
20, 21, 23, 24 y 27). **El puente es `estrategia_de_innovacion_arenas`**, que tiene `A` con
`estrategia_de_innovacion_de_producto` y `A` con `estrategia_de_innovacion_y_tecnologia` siendo esos
dos `D` entre si (puesto **530**), y `A` con `estrategia_de_innovacion_y_tecnologia` y `A` con
`estrategia_innovacion_producto` siendo esos dos `D` entre si (puesto **863**).

> **LOS DOS `D` SON DE UNA PIEZA Y NO UN ACCIDENTE, Y LOS DOS HABLAN DEL MISMO NODO:** el **863** dice
> *LA MADRE Y SU PIEZA DE ARENAS* y declara que `estrategia_de_innovacion_y_tecnologia` **desarrolla
> con un procedimiento propio la UNA LINEA que la madre despacha**, con el metodo de seleccion, la
> frontera del alcance y el uso como filtro de gate que **no estan en ningun paso de la madre**. El
> **530** es una **CORRECCION DECLARADA del 13 ago 2026 por relectura conjunta encargada por el
> auditor**: era `A`, se midio paso por paso contra el grafo, **la afirmacion resulto FALSA** y paso
> a `D` por la vara del banco 9.6.1. **Una fusion entera desmentiria las dos.**

**Y HAY UNA SEGUNDA RAZON INDEPENDIENTE, QUE SE DICE EN VEZ DE CALLARSE:**
`estrategia_de_innovacion_y_tecnologia` **ES PUERTA**, y **no es el miembro al que apunta la vara**
(que es `seleccion_arenas_estrategicas`), asi que **cualquier fusion tendria que absorberla y la
guarda `1B` lo prohibe**. **Este acto tiene DOS motivos independientes, como el acto 1 de la vuelta
65, y no uno.**

> **UNA CITA QUE SE TRAE COMO CONTRASTE Y NO COMO FUENTE, Y LA DISCREPANCIA SE DECLARA EN VEZ DE
> RESOLVERSE COPIANDO** (regla 2): el puesto **460** dice que *esta familia ya esta declarada como
> racimo nuevo de SEIS nodos y se decide en mesa, no aqui*. **MEDIDO HOY CONTRA EL FICHERO DEL
> TRAMO**, este acto **NO tiene dueno en mesa ni en destejido** (el campo `duenos_mesa_o_destejido`
> esta vacio), que es **el criterio con el que `OP-U-02` abrio su universo en la vuelta 63**. **La
> razon habla de una mesa que ninguna operacion escrita nombra**, y **el acto cierra `DECLARADO`
> igual**, asi que **ninguna de las dos lecturas mueve un nodo**.

### f) **LO QUE QUEDA DEL TRAMO AL CIERRE DE ESTE LOTE, MEDIDO Y NO ARRASTRADO**

| | |
|---|---:|
| actos del tramo unico | **47** |
| cerrados por el lote A (vuelta 65) | **2** |
| cerrados por el lote B (vuelta 66) | **6** |
| **cerrados por el lote C (esta vuelta)** | **6** (1 fundido, 5 declarados) |
| **quedan** | **33 actos** |
| **nodos que quedan** | **109** |
| de los que quedan, con nodo puente | **5** (actos 20, 21, 23, 24 y 27) |
| actos `ABIERTOS` del recomputo al cierre | **48** sobre **207** nodos |

### g) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba, NO deshace ninguna fusion, NO re-lee ni un veredicto de las
cuatro colisiones vigentes, NO funde ningun acto con dueno, NO toca la mesa `OP-M-03` ni sus dos
colisiones, NO toca las dos colisiones de `OP-U-02` (que siguen vigentes y publicadas con su duena) y
NO ejecuta ninguna de las cinco fichas `OP-M-02` consumidas.**


---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 67, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (26 ago 2026, vuelta 68, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **OCHO** veces, la ultima de ellas la del acta 66 en la linea
**4478** y la anterior la del acta 65 en la **3962**, **las dos cotejadas HOY
abriendo el fichero**. **Ninguna cifra publicada de arriba se toca.**

**Y AQUI CAMBIA EL PROCEDIMIENTO DE LA CITA, porque la vuelta pasada lo pago:** **ninguna de las
citas de linea de esta seccion esta TECLEADA**. Cada una es una marca que el registrador sustituye
por el numero que le devuelve **buscar su aguja de contenido** en el fichero, y **antes de escribir
una sola letra el instrumento vuelve a barrer el texto ya sustituido y exige que TODO numero de
linea que aparezca en el salga de una aguja**; si uno solo no sale, cae en `ROJO` y **no escribe
nada**. El ensanche esta enumerado en el docstring de
[`../../scripts/loop/vuelta68_registrar_acta67.py`](../../scripts/loop/vuelta68_registrar_acta67.py)
y **va marcado discutible** en el reporte de esta vuelta. **El acta de la vuelta 67 abre en la linea
**17745** de [`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md)**, su verificacion por
corrida propia en la **17761**, su relectura ciega en la **17865**, sus caidas en la
**17919**, sus quince adjudicaciones en la **17972**, sus pendientes en la
**18074**, su metrica de credito en la **18142** y sus condiciones de parada en la
**18175**.

### a) **LA CAIDA DE CIFRA PUBLICADA DEL EJECUTOR, CON SU NOMBRE Y SU MEDICION: LA RACHA SE ROMPE EN LA DUODECIMA Y EL CONTADOR DE PARADA QUEDA EN UNO**

**Se registra aqui, y no solo en el acta, porque la cifra equivocada vive en ESTA pagina**, y una
caida que solo vive en un acta se olvida.

| | lo que el acta 67 mide, copiado de su linea | linea |
|---|---|---:|
| **la caida** | **el registro del acta 66 de esta pagina dice que la frase envejecida *cuya linea base sigue en `2`* vive en la linea `4055`, y lo medido es que vive en otras tres**; **es una cifra que vive en `docs/plan/`, o sea CAIDA DE CIFRA PUBLICADA**, y **esta FUERA de los quince discutibles marcados** | **17922** |
| **por que la guarda no la cazo** | **la guarda de citas del registrador cotejo esa linea contra OTRA afirmacion** (que ahi esta la cabecera del apartado e, y ahi esta) **y la afirmacion de la PROSA no estaba en su lista de agujas**; una guarda que coteja las citas de una lista y no las citas del TEXTO deja pasar exactamente esta especie | **17933** |
| **lo que NO cae** | **la declaracion de ENVEJECIDA es correcta**: la frase existe, esta envejecida por la adjudicacion de la base `4` y no se tacha; **lo equivocado es el puntero**, y el dato adjudicado no se movio | **17941** |
| **el efecto en el credito** | **la relectura al doble se ejecuto** (47 citas de linea de los dos adosados, **46 calzan, UNA mala**) y **la racha CLASE O CIFRA EN CERO se rompe en la duodecima tanda** | **17946** |
| **la especie reporte** | **CERO**, porque la afirmacion equivocada no vive solo en `REPORTE.md`: **cuenta una sola vez y en la especie mas grave**. **TERCERA tanda seguida con reporte en cero** | **17952** |
| **las rachas al cierre de la 67** | **REPORTE EN CERO** (tercera seguida); **CLASE O CIFRA: ROTA** en la duodecima | **18171** |

> **EL CONTADOR DE PARADA QUEDA EN UNO, y se escribe con estas letras porque manda sobre la vuelta
> siguiente:** **UNA tanda con caida de clase o de cifra publicada**. La regla del credito pide **DOS
> SEGUIDAS** para parar el bucle. **Si la tanda 68 trae otra caida de clase o de cifra publicada, es
> `PARADA`**, y el auditor la ejecuta. La metrica acumulada al cierre de la 67 esta en la linea
> **18166**: **463 relecturas, 786 puestos, 7 caidas de clase, 27 de reporte del
> ejecutor, 14 de cifra publicada del ejecutor, 3 de cifra del auditor, 7 de acta del auditor y 4 de
> procedimiento del auditor**.

### b) **LA CORRECCION DECLARADA DE LA CITA, POR EL CARRIL DEL BANCO 9.10: EL TEXTO VIEJO VERBATIM, SIN TACHAR NADA, Y LA MEDICION AL LADO**

**Va por el mismo carril que la regla de la ficha envejecida de esta pagina** (linea
**3338**): **una correccion que tapa lo que corrige no se puede auditar**, asi
que **el texto viejo se cita entero y se queda donde esta**.

**LO QUE LA LINEA 4563 DE ESTA PAGINA DICE HOY, COPIADO DEL FICHERO Y NO DE MEMORIA**
(las tres lineas del parrafo, leidas por el registrador en la corrida que escribe esta seccion):

> no predicho es PARADA de guarda**. La frase de la linea **4055** de esta pagina que decia *cuya linea
> base sigue en `2`* **queda envejecida por esta adjudicacion y NO se tacha**: se lee con su corte del
> 20 ago 2026 y **manda la de hoy**.

**LO MEDIDO, Y ES LO QUE MANDA:**

| | medicion |
|---|---|
| **donde vive de verdad la frase** | en las lineas **4073** a **4075** de esta pagina, dentro del apartado *LO QUE ESTA SECCION NO HACE* del registro del acta 65; **el fragmento *linea base sigue* esta en la linea 4074** |
| **que hay de verdad en la linea 4055** | **la cabecera del apartado e) del registro del acta 65**, *LOS PENDIENTES 2 Y 4, NOMBRADOS CON SU DESTINO: EL CIERRE DE LA FASE 03*. **NUNCA vivio ahi la frase**, y el registrador lo comprueba con una aguja NEGATIVA antes de escribir |
| **que se corrige** | **solo el puntero**. **La declaracion de ENVEJECIDA sigue en pie**: la frase se lee con su corte del 20 ago 2026 y **manda la linea base `4`** que el acta 66 adjudico y que esta pagina registro en el apartado c) del registro del acta 66 |
| **que NO se corrige** | **nada de la aritmetica del censo**: las colisiones vigentes siguen siendo **4**, las dos de la mesa `OP-M-03` con su carril en la linea **3653** y las dos de `OP-U-02` con su duena |
| **que NO se tacha** | **ni una letra**. El parrafo viejo se queda tal cual, y esta correccion se lee al lado |

### c) **LOS QUINCE DISCUTIBLES, ADJUDICADOS: LOS QUINCE `A FAVOR`, Y EL `D1` POR EXTENSION CITABLE**

La columna de la vara **no es una glosa: es la regla citable con la que el auditor lo adjudico**.
**La cifra de cabecera y el detalle coinciden** (linea **17972**, *ADJUDICACION DE LOS
QUINCE DISCUTIBLES*): **quince marcados, quince adjudicados, cero sin contestar**.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | declarar el `ACTO 12` por un `D` DIRECTO sin triangulo, con un motivo fuera de los tres sellados | **`A FAVOR` POR EXTENSION CITABLE**, y es la adjudicacion de mas peso de la tanda: la lista de motivos es **enumeracion, no estatuto**; `P.12` manda que los veredictos DIRECTOS gobiernen; la ultima linea de `P.10` no esta condicionada al triangulo | **17974** |
| **`D2`** | declarar el `ACTO 14` por `P.5` cuando el quinto tiene una `A` con un miembro del puro | **`A FAVOR`**: el veredicto de clase y la membresia de familia **son dos cosas**, y el propio puesto 878 las separa en su texto; **`P.5` pregunta por familias, no por clases** | **17985** |
| **`D3`** | estrenar la guarda `1B` como motivo unico en dos actos el mismo dia | **`A FAVOR`**: el carril esta escrito y registrado; **un carril escrito no necesita estreno previo para valer**, y usarlo dos veces el mismo dia es frecuencia, no doctrina | **17996** |
| **`D4`** | en el `ACTO 15` las tres varas apuntan a una puerta y aun asi declara | **`A FAVOR`**: el carril del acta 54 resuelve el CHOQUE (vara a un miembro, puerta OTRO); aqui vara y puerta son **el mismo nodo** y lo que detiene es **la SEGUNDA puerta** | **18001** |
| **`D5`** | una sola fusion sobre seis actos | **`A FAVOR`**: el contrato es **prefijo con tope, no minimo** (acta 61, `D1`); la cifra va publicada en vez de maquillada | **18009** |
| **`D6`** | declarar seis teniendo cinco declarados baratos | **`A FAVOR`**: el lote se declara al abrirlo y se entrega lo declarado; **alargarlo al ver que sale barato es justo lo que el contrato del prefijo evita** | **18012** |
| **`D7`** | el superviviente del `ACTO 16` contra el cableado 8 a 3 | **`A FAVOR`**: `P.8` es regla de **PRELACION** y el contenido dice algo (5 pasos contra 4); **el cableado no habla** | **18017** |
| **`D8`** | cinco `APPEND` y el nodo duplica su tamano | **`A FAVOR`**, carril del `D9` del acta 65 y el `D7` del acta 66: **catalogo mas rico con solapes declarados** sobre `CUBIERTO` que calla texto vivo; el nodo entro a la cola de costuras | **18022** |
| **`D9`** | los dos `APPEND` que se solapan (la brujula y el titular) | **`A FAVOR`**: el puesto 1319 llama al titular *su unico gesto propio*; **callar uno con `CUBIERTO` habria perdido texto vivo que el archivo distingue** | **18027** |
| **`D10`** | una perdida con dos sitios en un solo campo `donde` | **`A FAVOR`, y el criterio queda adjudicado para que no oscile: LA FILA DEL CONTRATO ES POR PIEZA QUE SE PIERDE, NO POR SITIO DONDE VIVIA** | **18032** |
| **`D11`** | tres perdidas con atenuante declarado | **`A FAVOR`**, carril del `D8` del acta 63 y el `D10` del acta 65: **sobre-sellar declarando es mas auditable que callar** | **18039** |
| **`D12`** | corregir el defecto de `--base` sin encargo | **`A FAVOR`**: un instrumento committeado afirmando una cifra superada, **a sabiendas**, es la especie que esta campana persigue; la guarda sigue midiendo | **18043** |
| **`D13`** | re-codificar dos salidas en vez de re-correr | **`A FAVOR`**, verificado **al byte** por el auditor: `cp1252` a `utf-8` **sin tocar una letra ni una cifra**; re-correr el reanclaje habria dado cero re-anclajes y esa salida ya no seria la de la operacion | **18050** |
| **`D14`** | no contestar la pregunta de `P.5` en el `ACTO 15` | **`A FAVOR` con la letra delante**: `P.5` existe para decidir ANTES de fundir y **este acto no se funde**; **una pregunta cuya respuesta no tuviera consecuencia seria un rito** | **18056** |
| **`D15`** | ensanchar la aguja del comprobador y corregir su rotulo sin encargo | **`A FAVOR`**: **una guarda que pasa en verde sobre nada es peor que una que falla** (acta 64, pregunta 6); el barrido previo esta medido y **no hay regresion** | **18064** |

### d) **EL CUARTO MOTIVO SELLADO DEL `DECLARADO Y NO FUNDIDO`: UN VEREDICTO `D` DIRECTO INTERNO QUE LA FUSION ENTERA DESMENTIRIA (adjudicado por extension, con sus cuatro letras)**

**LA PREGUNTA CONCRETA DEL EJECUTOR SE CONTESTA PRIMERO, y la respuesta manda sobre todos los lotes
que quedan:** **LA LISTA DE MOTIVOS SELLABLES NO ES CERRADA, ES LA ENUMERACION DE LO ADJUDICADO
HASTA SU FECHA** (linea **18079**). **La prueba esta en su propia historia**:
nacio con uno (`P.10`, registrado en la linea **3744** de esta pagina), **el acta 65
anadio la guarda `1B`** (linea **4023**) y **el acta 66 anadio `P.5`** (linea
**4518**) diciendo con todas sus letras que anadir un motivo por adjudicacion es la
misma extension y **no doctrina nueva**. **Un encargo que enumera el estado del dia no convierte la
enumeracion en frontera.**

**EL CUARTO MOTIVO QUEDA ADJUDICADO** (linea **18076**), **y sus cuatro letras van copiadas de
sus lineas**:

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **PRIMERA** | **`P.12` parte 2 manda que con el acto convocado gobiernen los veredictos DIRECTOS** (una lectura hecha vale por si misma), y el **1374** es un `D` directo leido: **fundir los cinco deprecaria sus dos extremos al mismo vivo y sellaria que repiten entre si**, que es lo que esa lectura niega | **18087** |
| **SEGUNDA** | **la ultima linea de `P.10`** (*lo que NUNCA es salida es fundir la componente entera porque el cierre transitivo la junta*) **no esta condicionada a que exista triangulo**, y aqui **lo unico que junta a los dos nodos del `D` es el camino transitivo**: la unica lectura directa entre ellos es el `D` | **18091** |
| **TERCERA** | **las tres salidas de `P.10` estan cerradas por letra vigente**: leer los pares que faltan es cribado que la fase no tiene (banco 9.21), releer contra el superviviente **presupone la fusion que se esta negando**, y el subconjunto cerrado exige todas las lecturas hechas **y ademas la fusion parcial la prohibe el encargo** | **18096** |
| **CUARTA** | **el precedente del acto 5 de la vuelta 66 cerro `DECLARADO` por identidades que NADIE leyo**; aqui **la identidad esta leida y NEGADA**: el caso es mas fuerte | **18100** |

> **EL CATALOGO DE MOTIVOS SELLADOS QUEDA EN CUATRO** (linea **18106**): **el
> triangulo de `P.10`**, **la guarda `1B`**, **la respuesta de `P.5` (no es una familia)** y **el `D`
> directo interno que la fusion entera desmentiria**. **El `ACTO 12` cierra `DECLARADO Y NO FUNDIDO`
> por ese cuarto motivo**, y su ficha en esta pagina, escrita cuando el motivo aun no tenia letra,
> esta en la linea **4797** del registro del lote C.
>
> **Y LA LISTA SIGUE SIN SER ESTATUTO:** si un acto no cabe en ninguno de los cuatro, **va como
> `PENDIENTE DE DOCTRINA` con lo mejor sostenido registrado**, que es exactamente lo que la vuelta 67
> hizo con el 12.

### e) **EL TRANSITO DEL ACTO CON FORMA `EMPATE SIN VARA`: NI SE DECLARA NI DETIENE EL LOTE**

**Adjudicado en la linea **18109**, y `P.8` ya decia a quien se trae (al auditor); lo que
faltaba era el estado mientras tanto.** **Queda asi, y es carril nuevo de procedimiento sobre letra
vieja:**

1. **EL ACTO NI SE DECLARA NI DETIENE EL LOTE** (linea **18111**). **Se procesa entero
   como cualquier otro**: dossier, `P.5` sobre el texto estable, puertas, puentes y colisiones.
2. **Si una guarda o un motivo sellado lo detiene, cierra `DECLARADO` por ese motivo** y **el empate
   ya no importa**.
3. **Si nada lo detiene, el ejecutor NO elige superviviente** (linea **18116**): **escribe
   el caso entero en el reporte** (la respuesta de `P.5`, las tres cuentas y el cableado, y **las
   piezas propias que el archivo nombra por cada miembro**, que es lo que `P.8` llama contenido:
   piezas propias, rol declarado, alcance) y **lo marca discutible**.
4. **El acto queda `ABIERTO EN TRANSITO` dentro del tramo, FUERA de la cuenta de cerrados del lote**
   (linea **18120**).
5. **El auditor adjudica el superviviente en su acta siguiente**, con el caso delante, y **el lote
   siguiente ejecuta esa fusion adjudicada como su primera operacion**.

> **`DECLARADO Y NO FUNDIDO` QUEDA RESERVADO A MOTIVOS SELLADOS** (linea
> **18123**): **el auditor aun no contesta no es un motivo, es una pregunta en
> viaje**. **El `ACTO 18` del prefijo viene MEDIDO en `EMPATE SIN VARA`** (pasos 4 a cuatro bandas,
> condiciones 2 a cuatro bandas, cableado empatado) **y entra al lote D por este carril**.

### f) **LA NOTA DE DICTADO DEL PUESTO 1030: LA SUSTANCIA MEDIDA, LA ATRIBUCION SUELTA, Y SIN CAIDA**

**Se registra porque una nota que solo vive en un acta se olvida, y porque distingue dos cosas que
conviene no confundir** (linea **17905**).

| | lo que el acta 67 dice |
|---|---|
| **lo que el reporte 67 escribio** | que el puesto **1030** *enumera la familia con sus cuatro nombres* |
| **lo que el auditor midio** | la razon del **1030** nombra **el PAR** y **el rotulo de la familia** (la competencia entre inversores) **con su cuenta de cuatro miembros y seis pares**; **los cuatro nombres juntos los da el conjunto de los seis pares**, no ese puesto solo |
| **la sustancia** | **CALZA y esta medida**: los seis pares entre los cuatro miembros (787, 394, 334, 413, 257 y 1030) **leidos y los SEIS en `A`**, contados por el auditor contra el archivo |
| **el veredicto** | **la atribucion literal es un pelo suelta y queda dicha**, **sin contarse como caida**: el mismo carril del 1306 y el 1330 en el acta 66 |

### g) **LOS PENDIENTES 3 A 6, NOMBRADOS CON SU DESTINO**

**Se registran porque mandan sobre lo que viene aunque no encarguen trabajo hoy**, y **los cuatro
quedan NOMBRADOS, ninguno abierto en doctrina nueva**.

| pendiente | lo que el acta 67 fija, copiado de su linea | destino | linea |
|---|---|---|---:|
| **3. el subconjunto cerrado de un acto con puente** (heredado) | sigue **NOMBRADO**, ahora con **NUEVE actos esperandolo** (el **1**, **5**, **10**, **11**, **12**, **13**, **14**, **15** y **17**) | **el CIERRE DE LA FASE 03**, donde **la parada de `AUDITOR.md` garantiza que el fundador lo ve antes del tramo mecanico** | **18128** |
| **4. la marca para *ya lo dice el `APPEND` de un hermano*** (heredado) | sigue **NOMBRADO**: **el carril vigente alcanza**, y la vuelta 67 **lo pago tres veces con atenuante declarado**; la cuenta crece y se publica | **anotado, no encargado** (el mismo trato que el `INCISO` de condiciones, acta 55 pregunta 5) | **18133** |
| **5. el `INCISO` de condiciones** (heredado) | sigue en su carril, con **cinco piezas `DE CONDICIONES` mas** de la vuelta 67 | **la fase 04** (acta 55, pregunta 5) | **18136** |
| **6. el esquema de `OPERACIONES.jsonl`** (heredado) | sigue **pendiente**; la vuelta 67 **no toco ninguna ficha y no estreno ninguna clave** (`OPERACIONES.jsonl` sin cambios, verificado por `numstat`) | **anotado, sin clave nueva** | **18138** |

> **LOS DOS PRIMEROS PENDIENTES NO ESTAN EN ESTA TABLA PORQUE YA NO SON PENDIENTES:** el **1** quedo
> **ADJUDICADO** como el cuarto motivo sellado del apartado d) y el **2** quedo **ADJUDICADO** como
> el transito del apartado e). **Se dice para que la ausencia no parezca omision.**

### h) **LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya**

**NO toca ni una cifra publicada arriba**, **NO tacha ni una letra del texto que corrige**, **NO
elige ningun superviviente**, **NO funde nada**, **NO deshace ninguna fusion**, **NO re-lee ni un
veredicto de las cuatro colisiones vigentes** (cuya **linea base es `4`** y cuyas duenas son la mesa
`OP-M-03` y `OP-U-02`), **NO toca la mesa `OP-M-03`**, **NO ejecuta ninguna de las cinco fichas
`OP-M-02` consumidas** y **NO reabre el registro del lote C** (linea **4621**), cuyos
apartados sobre los actos **13** y **15** (linea **4851**), el **14** (linea
**4920**) y el **17** (linea **4962**) **quedan tal como se escribieron**.
Registra adjudicaciones y una correccion declarada.


---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE D` (2026-08-26, vuelta 68)

**Se adosa al final del documento, bajo la cabecera de tramo que la vuelta 65 ya puso** (linea
**3732**), **y NO reescribe ni una linea de arriba.** **Ninguna tabla de esta
seccion esta tecleada**: el reparto pieza a pieza, las piezas por absorbido y las fichas de los
declarados **se generan del plan sellado** [`../loop/PLAN_V68_OPU02_LOTE_D.json`](../loop/PLAN_V68_OPU02_LOTE_D.json);
la de perdidas **se recorta de la salida del tallador**; y las celdas de guardas, colisiones y
censos **se extraen por aguja** de las salidas de la vuelta. **Y las citas de linea tampoco se
teclean**: salen de buscar su aguja de contenido, con la guarda ensanchada que esta vuelta estreno
(el ensanche esta registrado arriba, en el apartado del acta 67 que abre en la linea
**5031**).

**EL LOTE ES PREFIJO SIN SALTOS** del `orden_universo` de lo que quedaba: **el prefijo 18 a 24,
SIETE actos y 28 nodos**. **SEIS cierran ENTEROS** y **el acto 18 se procesa entero y se cuenta
APARTE**, por el carril del transito que el acta 67 adjudico y que esta pagina registra en la linea
**5152**.

| acto | miembros | cierra | motivo | superviviente |
|---:|---:|---|---|---|
| **18** | 4 | **`ABIERTO EN TRANSITO`** | **`EMPATE SIN VARA` y nada lo detiene**: ni guarda ni motivo sellado | **ninguno se elige**, y esa es la regla |
| **19** | 4 | **FUNDIDO** | `CONTENIDO EMPATA`, decide el cableado solo (`P.8`) | `division_trabajo_humano_ia` |
| **20** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, triangulo medido | ninguno se elige |
| **21** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, dos triangulos medidos | ninguno se elige |
| **22** | 4 | **FUNDIDO** | `UNA SOLA VARA` de pasos; el cableado apunta al otro y no habla | `comprension_capacidades_limitaciones_ia` |
| **23** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, triangulo medido | ninguno se elige |
| **24** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, dos triangulos, **la figura `ESTRELLA`** y **el dueno `OP-S-07`** | ninguno se elige |

> **LOS CUATRO DECLARADOS DE ESTE LOTE CIERRAN LOS CUATRO POR EL MISMO MOTIVO, EL TRIANGULO DE
> `P.10`**, que es el primero de los CUATRO motivos sellados del catalogo (el cuarto se adjudico en
> el acta 67 y esta registrado arriba, en la linea **5121**). **Ningun acto de este
> lote necesito la guarda `1B`** (linea **4023**) **ni la respuesta de `P.5`** (linea
> **4518**): las dos pasan por vacio y se dice.

**LO QUE LA FUSION MOVIO, LEIDO DE LA SALIDA DE LA EJECUCION:** **3243 vivos a
3237**, **6 nodos mueren**, **34 piezas repartidas**
(**12** viajan enteras y **20** ya estaban dichas), **15 ficheros
tocados** y **11 redirecciones sobre nodos vivos**.

### a) **EL `ACTO 19`: LA FAMILIA DEL REPARTO DE TAREAS ENTRE PERSONA Y MAQUINA, Y LA PRIMERA VEZ DEL TRAMO QUE EL CABLEADO DECIDE SOLO**

**`P.5` CONTESTADA SOBRE EL TEXTO ESTABLE: ES UNA FAMILIA, y no es lectura del ejecutor sino
declaracion del archivo.** El puesto **1597** dice con todas sus letras que **la familia del reparto
de tareas entre persona y maquina pasa a CUATRO nodos por cierre transitivo**, con
`descomposicion_tareas_trabajo` de centro y sus tres `A`, los puestos **972**, **1582** y ese; el
**1582** la habia visto pasar de dos a tres **y con miembros de DOS libros distintos**.

**UNA FRONTERA QUE EL ARCHIVO ESCRIBE Y QUE ESTA FUSION NO CRUZA:** el mismo puesto **1597** declara
que **esta familia NO es el racimo de la supervision de la IA**, y que **ninguno de sus cuatro
miembros figura en aquella nomina de diez**. **Cotejado hoy** contra
[`INVENTARIO.jsonl`](INVENTARIO.jsonl): **los cuatro estan FUERA de esa nomina**. Son dos familias
de IA distintas, una sobre quien hace que y otra sobre quien revisa.

**`P.8` EN ORDEN:** la FORMA medida es **`CONTENIDO EMPATA`** (pasos 4 a tres bandas, condiciones 2
a cuatro bandas), asi que **EL CABLEADO DECIDE SOLO** y apunta a `division_trabajo_humano_ia`.
**No es que el cableado gane a un contenido que dice otra cosa: es que el contenido NO DICE NADA**,
que es el unico supuesto en que `P.8` le da la palabra.

**EL NODO CRECE de 4 pasos a 7 y de 2 condiciones a 5**, y **el costo va
publicado**. **CERO `INCISO` y es POR LA PUNTUACION**: los cuatro pasos del superviviente terminan
en punto y cualquier `INCISO` con nexo de coma cae en la guarda de la juntura rota.

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `automatizacion_tareas_aburridas` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `automatizacion_tareas_aburridas` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **3** de `automatizacion_tareas_aburridas` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `automatizacion_tareas_aburridas` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **2** de `automatizacion_tareas_aburridas` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `descomposicion_tareas_trabajo` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `descomposicion_tareas_trabajo` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **3** de `descomposicion_tareas_trabajo` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `descomposicion_tareas_trabajo` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **1** de `descomposicion_tareas_trabajo` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **2** de `descomposicion_tareas_trabajo` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `framework_tareas_ia_humano` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `framework_tareas_ia_humano` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `framework_tareas_ia_humano` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **4** de `framework_tareas_ia_humano` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `framework_tareas_ia_humano` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `framework_tareas_ia_humano` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `automatizacion_tareas_aburridas` | 3 | 2 | 2 | 3 | 0 |
| `descomposicion_tareas_trabajo` | 4 | 2 | 2 | 4 | 0 |
| `framework_tareas_ia_humano` | 4 | 2 | 2 | 4 | 0 |
| **los 3 juntos** | **11** | **6** | **6** | **11** | **0** |

**LAS PERDIDAS SELLADAS EN CAMPO PROPIO**, recortadas de la salida del tallador:

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V68_OPU02_LOTE_D.json | 19 | DE PARAMETRO DE PASO | LA UNIDAD DE ANALISIS: que el barrido se haga POR PUESTO O ROL y termine en un ROL REDISENADO, y no por proceso operativo. Es la perdida que el propio puesto 1582 nombro antes de que nadie fundiera nada. El superviviente mapea LAS TAREAS DEL PROCESO OPERATIVO y asigna a personas las excepciones, la negociacion y los problemas complejos, pero en ningun paso dice que la unidad sea el puesto ni que el entregable sea un rol redisenado. UNA SOLA PIEZA CON DOS SEDES, sellada una vez con las dos nombradas (acta 67, D10) | paso 1 y paso 3 de descomposicion_tareas_trabajo | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V68_OPU02_LOTE_D.json | 19 | DE PARAMETRO DE PASO | la CREATIVIDAD como destino del tiempo que se libera. El paso 3 del superviviente asigna a las personas la excepcion, la negociacion y la resolucion de problemas complejos, y esas tres cubren dos de las tres que el absorbido nombra, pero la creatividad no esta en ninguna | paso 3 de descomposicion_tareas_trabajo | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V68_OPU02_LOTE_D.json | 19 | DE PARAMETRO DE PASO | que la delegacion a la maquina se evalue CON SUPERVISION HUMANA, dicho en el mismo paso que decide que se delega. ATENUANTE DECLARADO: el paso 4 del superviviente pone el mecanismo entero de escalamiento, que la IA alerte a las personas ante anomalias o excepciones relevantes, asi que la supervision llega por otro sitio aunque no acompane a la decision de delegar | paso 2 de automatizacion_tareas_aburridas | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V68_OPU02_LOTE_D.json | 19 | DE PARAMETRO DE PASO | el ORDEN DE ARRANQUE de la delegacion: empezar por lo TEDIOSO Y FACIL DE VERIFICAR, que es la unica linea del acto que dice por donde se empieza y con que criterio de riesgo. ATENUANTE DECLARADO: el APPEND del paso 2 de framework_tareas_ia_humano trae la taxonomia entera con su criterio de capacidad actual de la IA, que es la mitad de ese arranque | paso 3 de framework_tareas_ia_humano | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V68_OPU02_LOTE_D.json | 19 | DE CONDICIONES | la ROTACION ALTA y la MORAL BAJA por tareas repetitivas como sintoma disparador. La condicion 2 del superviviente habla de tiempo humano valioso perdido en tareas repetitivas, que es el mismo hecho medido por el reloj y no por la gente | condicion 1 de automatizacion_tareas_aburridas | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V68_OPU02_LOTE_D.json | 19 | DE CONDICIONES | la SUBUTILIZACION DE LA IA como disparador simetrico. La condicion 2 del superviviente solo mira el lado humano, el tiempo que se pierde en lo repetitivo, y no el lado de la maquina ociosa que el absorbido pone a su lado | condicion 2 de framework_tareas_ia_humano | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |

### b) **EL `ACTO 22`: EL BLOQUE DE CUATRO DEL RACIMO DE LA SUPERVISION DE LA IA, Y LA PARTICION ESCRITA NO SE MUEVE**

**`P.5` CONTESTADA: ES UNA FAMILIA.** El puesto **177** dice *REPITE* entre
`comprension_capacidades_limitaciones_ia` y `jagged_frontier_ia`; el **456** dice que
`invitar_ia_a_todo` y `principio_invitar_ia_siempre` son **el mismo principio numerado**; y el
**1517** declara que **la absorcion SI ocurre** y que la pareja de invitar a la IA a todo **ENTRA**
al racimo por ese par.

**LA PARTICION `5 MAS 4 MAS 1`, CONTRASTADA HOY CONTRA EL FICHERO DEL TRAMO, Y ESTA FUSION NO CRUZA
NI UNA DE SUS DOS FRONTERAS:**

| bloque de la particion | que es hoy | quien lo dice |
|---|---|---|
| **el CINCO** | **el `acto 11` del tramo**, que ya cerro **`DECLARADO Y NO FUNDIDO` por `P.10`** en la vuelta 66 (registrado en la linea **4443**), y cuyo puesto **1541** dejo escrito que **la particion escrita NO se mueve** | el fichero del tramo mas la ficha de arriba |
| **el CUATRO** | **este `acto 22`**, que es el que se funde | el fichero del tramo |
| **el UNO** | `comprender_alineacion_etica_ia`, **el suelto**, que `04_ENLACES.md` manda a **mesa** por ser el suelto de un racimo **sin centro** | el carril de los sueltos |

> **LA SUMA DA `5 MAS 4 MAS 1` Y CALZA CON EL CAMPO `forma` DEL INVENTARIO**, medido hoy. **Esta
> fusion opera DENTRO de un bloque**: ni toca al bloque de cinco, ni toca al suelto.
>
> **LO QUE SE TRAE COMO CONTRASTE Y NO COMO FUENTE, y por eso va MARCADO DISCUTIBLE:** el campo
> `estado` de esa entrada de inventario dice **`en mesa, particion PROVISIONAL`**, con corte del 13
> ago 2026. **MEDIDO HOY** contra el fichero fijado del tramo, **este acto tiene los DOS campos de
> dueno VACIOS**, y **el campo `operaciones` de la propia entrada del racimo tambien esta vacio**:
> **ninguna operacion lo reclama**. El criterio con el que `OP-U-02` abrio su universo es el dueno
> medido. **La discrepancia se declara en vez de resolverse copiando** (regla 2), que es el mismo
> carril con el que el acto 17 de la vuelta 67 trajo el puesto 460.

**`P.8` EN ORDEN:** la FORMA medida es **`UNA SOLA VARA`**; la de PASOS apunta a
`comprension_capacidades_limitaciones_ia` (5 contra un maximo de 4) y **se funde a su lado**. **El
cableado apunta al OTRO**, `jagged_frontier_ia` (7 contra 3), **y NO HABLA**: `P.8` es regla de
**PRELACION**. **Es la misma forma que el acto 16 de la vuelta 67** (linea **4621**),
cuyo `D7` el acta 67 adjudico `A FAVOR` con esta misma letra. **El margen del cableado se publica
como dato.**

**EL NODO CRECE de 5 pasos a 9 y de 1 condiciones a 3**, y **es el nodo
mas grande que este tramo ha producido**. **DOS `INCISO` y ninguno apilado sobre el mismo paso**,
los dos extraidos del nodo y comprobados VERBATIM.

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `invitar_ia_a_todo` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **2** de `invitar_ia_a_todo` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `invitar_ia_a_todo` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `invitar_ia_a_todo` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `invitar_ia_a_todo` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `jagged_frontier_ia` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `jagged_frontier_ia` | `INCISO` | **`INCISO` ADOSADO** al paso 2: *con casos reales y variados, no solo con ejemplos fáciles* |
| paso **3** de `jagged_frontier_ia` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `jagged_frontier_ia` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `jagged_frontier_ia` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `jagged_frontier_ia` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **1** de `principio_invitar_ia_siempre` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `principio_invitar_ia_siempre` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **3** de `principio_invitar_ia_siempre` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `principio_invitar_ia_siempre` | `INCISO` | **`INCISO` ADOSADO** al paso 5: *hasta encontrar la forma óptima de uso para esa tarea específica* |
| condicion **1** de `principio_invitar_ia_siempre` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `principio_invitar_ia_siempre` | `APPEND` | **viaja ENTERA** al superviviente |

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `invitar_ia_a_todo` | 4 | 1 | 4 | 1 | 0 |
| `jagged_frontier_ia` | 4 | 2 | 1 | 4 | 1 |
| `principio_invitar_ia_siempre` | 4 | 2 | 1 | 4 | 1 |
| **los 3 juntos** | **12** | **5** | **6** | **9** | **2** |

**LAS PERDIDAS SELLADAS EN CAMPO PROPIO:**

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V68_OPU02_LOTE_D.json | 22 | DE PARAMETRO DE PASO | EL INVENTARIO DE TAREAS como paso previo: LISTAR todas las tareas del negocio donde se podria usar la IA, con sus areas nombradas (marketing, ventas, atencion al cliente, analisis), ANTES de probar nada. El superviviente arranca disenando pruebas para su propio caso de uso y en ningun paso manda listar. ATENUANTE DECLARADO: el APPEND del paso 1 de invitar_ia_a_todo manda probar en CADA tarea del flujo de trabajo diario, que recorre el mismo terreno sin escribirlo como lista. UNA SOLA PIEZA CON DOS SEDES, sellada una vez con las dos nombradas (acta 67, D10) | paso 1 de jagged_frontier_ia y paso 1 de principio_invitar_ia_siempre | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V68_OPU02_LOTE_D.json | 22 | DE PARAMETRO DE PASO | el barrido SISTEMATICO SIN DESCARTE PREVIO dicho por segunda vez y con la palabra sistematicamente delante. ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: el contenido llega ENTERO por el APPEND del paso 1 de invitar_ia_a_todo, que es su gemelo declarado en el puesto 456 (el mismo principio numerado). Se sella igual, porque sobre-sellar declarando es mas auditable que callar | paso 2 de principio_invitar_ia_siempre | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V68_OPU02_LOTE_D.json | 22 | DE PARAMETRO DE PASO | el CRITERIO DE PARADA de la iteracion. El paso 5 del superviviente manda ajustar la instruccion segun lo que se vaya descubriendo, pero no dice hasta cuando. ATENUANTE DECLARADO Y MEDIDO: el INCISO al paso 5 de este mismo acto le adosa VERBATIM el criterio del absorbido, asi que la pieza NO se pierde de hecho; se sella porque el sello es del reparto y no del resultado | paso 4 de principio_invitar_ia_siempre | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V68_OPU02_LOTE_D.json | 22 | DE CONDICIONES | el ARRANQUE DE LA EXPLORACION de IA generativa como disparador. ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: llega entero por el APPEND de la condicion 1 de invitar_ia_a_todo, su gemelo del puesto 456 | condicion 1 de principio_invitar_ia_siempre | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V68_OPU02_LOTE_D.json | 22 | DE CONDICIONES | la DESCONFIANZA MEDIDA como disparador: no saber que tan confiable es la IA para una tarea especifica. La condicion 1 del superviviente dispara cuando vas a dejarle una tarea importante, que es la decision y no la duda que la precede | condicion 2 de jagged_frontier_ia | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |

> **UNA PERDIDA CON DOS SEDES EN UN SOLO CAMPO `donde`, en cada uno de los dos actos fundidos**, por
> el criterio que el acta 67 adjudico y que esta pagina registra: **5114**.

### c) **LOS `ACTOS 20`, `21`, `23` Y `24`: `DECLARADOS Y NO FUNDIDOS` POR `P.10`, CON SUS TRIANGULOS MEDIDOS**

**Los cuatro quedan VIVOS Y ENTEROS**, sin un nodo tocado ni un superviviente elegido, y **su destino
comparte carril con el pendiente 3 del acta 67: el cierre de la fase 03**.

**El `acto 20`, la familia del efecto latigo en la cadena de suministro:**

| | |
|---|---|
| **acto** | **20** del `orden_universo` |
| **MOTIVO SELLADO DEL CIERRE** | **`P.10`**, con su triangulo MEDIDO (acta 65, el carril registrado en la linea **3744**) |
| **miembros** | **4**, y **NINGUNO se toca** |
| **combinaciones internas** | 6 |
| **pares `A` internos** | 3 |
| **pares `D` internos** | **1**, leidos y declarados DISTINTOS |
| **pares sin veredicto escrito** | 2 |
| **NODOS PUENTE** | **1** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **1** |
| **PUERTAS dentro del acto** | **NINGUNA**, la guarda `1B` pasa por vacio y se dice |
| **puestos de los `D` internos** | **994** |
| **duenos medidos hoy en el fichero del tramo** | **NINGUNO**, los dos campos vacios |
| **instrumento** | [`../loop/SALIDA_V68_PUENTES_TRAMO.txt`](../loop/SALIDA_V68_PUENTES_TRAMO.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V68_DOSSIER_LOTE_D.txt`](../loop/SALIDA_V68_DOSSIER_LOTE_D.txt) |

> **La lectura que una fusion entera desmentiria:** el **994** dice que `efecto_bullwhip` **mide el
> problema** y `compartir_datos_cadena_suministro` **es la inversion que lo cura**, que **ni un paso
> se solapa**, y que es **arista que falta de las mas claras** porque el diagnostico termina
> apuntando al remedio **por su nombre**. **Y hay un CHOQUE encima**, dicho en vez de callado: el
> puesto **730** declara que la clase queda en `A` **por la lectura vieja del cero-enlazados** y que
> **si mandara el contenido seria `D`**, y lo deja anotado en vez de elegir.

**El `acto 21`, la familia del Punto 4 de Deming:**

| | |
|---|---|
| **acto** | **21** del `orden_universo` |
| **MOTIVO SELLADO DEL CIERRE** | **`P.10`**, con sus DOS triangulos MEDIDOS |
| **miembros** | **4**, y **NINGUNO se toca** |
| **combinaciones internas** | 6 |
| **pares `A` internos** | 3 |
| **pares `D` internos** | **2**, leidos y declarados DISTINTOS |
| **pares sin veredicto escrito** | 1 |
| **NODOS PUENTE** | **2** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **2** |
| **PUERTAS dentro del acto** | **NINGUNA**, la guarda `1B` pasa por vacio y se dice |
| **puestos de los `D` internos** | **2927**, **3102** |
| **duenos medidos hoy en el fichero del tramo** | **NINGUNO**, los dos campos vacios |
| **instrumento** | [`../loop/SALIDA_V68_PUENTES_TRAMO.txt`](../loop/SALIDA_V68_PUENTES_TRAMO.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V68_DOSSIER_LOTE_D.txt`](../loop/SALIDA_V68_DOSSIER_LOTE_D.txt) |

> **Las dos lecturas que una fusion entera desmentiria:** el **2927** avisa con todas sus letras de
> que los dos extremos **fusionan por `A` con el mismo tercer nodo** y de que **quien componga esa
> cadena sin verificar que es CONTENCION en los dos eslabones dira `A`**; el **3102** declara
> **conjuntos disjuntos** y entregables distintos. **El cierre transitivo junta a los cuatro
> justamente por la cadena que el 2927 dice que NO compone.**

**El `acto 23`, la familia de la reserva de opciones para empleados:**

| | |
|---|---|
| **acto** | **23** del `orden_universo` |
| **MOTIVO SELLADO DEL CIERRE** | **`P.10`**, con su triangulo MEDIDO |
| **miembros** | **4**, y **NINGUNO se toca** |
| **combinaciones internas** | 6 |
| **pares `A` internos** | 4 |
| **pares `D` internos** | **1**, leidos y declarados DISTINTOS |
| **pares sin veredicto escrito** | 1 |
| **NODOS PUENTE** | **1** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **1** |
| **PUERTAS dentro del acto** | **NINGUNA**, la guarda `1B` pasa por vacio y se dice |
| **puestos de los `D` internos** | **1193** |
| **duenos medidos hoy en el fichero del tramo** | **NINGUNO**, los dos campos vacios |
| **instrumento** | [`../loop/SALIDA_V68_PUENTES_TRAMO.txt`](../loop/SALIDA_V68_PUENTES_TRAMO.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V68_DOSSIER_LOTE_D.txt`](../loop/SALIDA_V68_DOSSIER_LOTE_D.txt) |

> **La lectura que una fusion entera desmentiria:** el **1193** dice que uno es **NEGOCIACION** y el
> otro **MECANICA**, nombra las dos cuentas que la negociacion no trae, y cierra con que **ese par
> NO anade miembro: sale sano porque trae calculos propios, y no repeticion**. La familia esta
> contada por el archivo en el **1371** (cuatro nodos por cierre transitivo) y en el **1436**
> (cobertura de cinco de seis, forma **PROVISIONAL** por un solo par).

**El `acto 24`, la estrella de pass/fail, con TRES razones independientes:**

| | |
|---|---|
| **acto** | **24** del `orden_universo` |
| **MOTIVO SELLADO DEL CIERRE** | **`P.10`**, con sus DOS triangulos MEDIDOS, **mas el ejemplar de la figura `ESTRELLA (9.23)` que una fusion entera borraria**, **mas el DUENO** |
| **miembros** | **4**, y **NINGUNO se toca** |
| **combinaciones internas** | 6 |
| **pares `A` internos** | 3 |
| **pares `D` internos** | **2**, leidos y declarados DISTINTOS |
| **pares sin veredicto escrito** | 1 |
| **NODOS PUENTE** | **1** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **2** |
| **PUERTAS dentro del acto** | **NINGUNA**, la guarda `1B` pasa por vacio y se dice |
| **puestos de los `D` internos** | **636**, **1346** |
| **duenos medidos hoy en el fichero del tramo** | **OP-S-07** en `duenos_cualquier_operacion` |
| **instrumento** | [`../loop/SALIDA_V68_PUENTES_TRAMO.txt`](../loop/SALIDA_V68_PUENTES_TRAMO.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V68_DOSSIER_LOTE_D.txt`](../loop/SALIDA_V68_DOSSIER_LOTE_D.txt) |

> **PRIMERA, `P.10`:** el **636** dice que **uno construye el experimento y el otro dicta cuando se
> aprueba**, y el **1346** repite la misma frontera entera.
> **SEGUNDA, la figura:** la entrada `figura` **`ESTRELLA (9.23)`** del inventario nombra a este
> acto como **su ejemplar numero UNO**, con el centro `diseno_experimentos_pass_fail`, los radios
> **467**, **511** y **639** y los perifericos **636** y **1346** en `D`, y declara que **las dos
> cuentas que el banco 9.23 exige estan hechas**. El propio **1346** dice que era **el par que
> decidia** y que al salir `D` **la figura queda CONFIRMADA**. Fundir el acto borraria el ejemplar.
> **TERCERA, y es la mas seca: ESTE ACTO TIENE DUENO.** Su campo `duenos_cualquier_operacion` trae
> **`OP-S-07`**, medido hoy. **Es la unica de las tres que habria bastado sola sin leer nada.**

### d) **EL `ACTO 18`, `ABIERTO EN TRANSITO`: EL ESTRENO DEL CARRIL QUE EL ACTA 67 ADJUDICO**

**Se procesa entero y se cuenta APARTE, ni cerrado ni saltado**, que es exactamente lo que el carril
de la linea **5152** manda. **NO se elige superviviente y esa es la regla, no una
omision.**

| | lo medido hoy |
|---|---|
| **miembros** | **4**: `alianzas_cross_industry`, `co_opetition_industria`, `colaboracion_sectorial`, `trabajo_colectivo_estandares_industria` |
| **pares internos con veredicto** | **3 de 6**, y **los TRES en `A`** (puestos **1797**, **1871** y **1903**) |
| **pares `D` internos** | **0** |
| **NODOS PUENTE / TRIANGULOS** | **0 / 0**, o sea **`P.10` NO se dispara** |
| **PUERTAS dentro** | **NINGUNA**: la guarda `1B` pasa por vacio |
| **`P.5`** | **ES UNA FAMILIA**, y la declara el archivo: el **1871** dice *LA MISMA ALIANZA SECTORIAL POR TERCERA VEZ* y que la familia **pasa de DOS a TRES**, y el **1903** dice *POR CUARTA VEZ* y que **pasa de TRES a CUATRO por cierre transitivo**. Los cuatro de la misma fuente |
| **FORMA medida** | **`EMPATE SIN VARA`**: pasos **4 a cuatro bandas**, condiciones **2 a cuatro bandas** y **el cableado tambien empata** |
| **destino** | **`ABIERTO EN TRANSITO`**, fuera de la cuenta de cerrados del lote. **El auditor adjudica el superviviente en su acta y el lote siguiente ejecuta esa fusion como su primera operacion** |

> **NADA LO DETIENE, Y POR ESO NO CIERRA `DECLARADO`.** `P.10` no se dispara, la `1B` pasa por
> vacio y `P.5` contesta que es UNA familia: **no hay motivo sellado que invocar**, y `DECLARADO Y
> NO FUNDIDO` queda reservado a motivos sellados. **El auditor aun no contesta no es un motivo, es
> una pregunta en viaje.**

### e) **LAS GUARDAS DE LA OPERACION, LEIDAS DE LAS SALIDAS Y NO AFIRMADAS**

| guarda | resultado |
|---|---|
| **las cuatro de cada fusion** (1 miembros vivos, **1B** ningun absorbido es puerta, 2 cobertura exacta, 3 cero repetidos) | **VERDES en los dos actos** |
| **`P.16`, quien fabrica limpia, en el mismo commit** | la fusion fabrico **1** duplicada(s) y **las limpio en la misma corrida**; **1 auto-arista(s)** retirada(s); el pasivo propio de la guarda baja de **891** a **890** |
| **colisiones esperadas, MEDIDAS ANTES de fundir sobre la linea base declarada** | base **4**, **NUEVAS 0**, **ESPERADAS 4**; el censo de cierre mide **4** y **`CALZA: SI`** |
| **diff de duplicadas, con la apertura sacada de `git`** | **FABRICADAS 0**, **RENOMBRADAS 0**, grupos **914 a 913** |
| **reanclaje entre la fusion y `run_phase1`** | **NADA QUE RE-ANCLAR**: el fundidor ya habia redirigido las **11** referencias vivas |
| **Gate 0 con su ciclo de TRES** | **`GATE 0: OK`**, universo **3237 activos / 616 deprecados**; sin cuarta corrida |
| **recomputo al cierre** | **72** actos, **46** `ABIERTOS` sobre **199** nodos |

**Las CUATRO colisiones vigentes no se tocan** y siguen con su duena, por el carril general de la
linea **1377** y el que la vuelta 66 fijo en la base `4`.

### f) **LO QUE QUEDA DEL TRAMO AL CIERRE DE ESTE LOTE, MEDIDO Y NO ARRASTRADO**

| | |
|---|---:|
| actos del tramo unico | **47** |
| cerrados por los lotes A, B y C | **14** |
| **cerrados por el lote D (esta vuelta)** | **6** (2 fundidos, 4 declarados) |
| **quedan** | **27 actos** |
| **nodos que quedan** | **85** |
| **el siguiente del prefijo** | el acto **18**, que es el que queda `ABIERTO EN TRANSITO` |
| de los que quedan, con nodo puente | **1** (acto 27) |
| **actos declarados que esperan el cierre de la fase 03** | **13** (actos 1, 5, 10, 11, 12, 13, 14, 15, 17, 20, 21, 23, 24) |

### g) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba**, **NO deshace ninguna fusion**, **NO re-lee ni un veredicto
de las cuatro colisiones vigentes**, **NO funde ningun acto con dueno** (los del tramo con dueno
siguen fuera, y el `acto 24` se declara con el suyo dicho), **NO toca la mesa `OP-M-03` ni sus dos
colisiones**, **NO toca las dos colisiones de `OP-U-02`**, **NO ejecuta ninguna de las cinco fichas
`OP-M-02` consumidas**, **NO elige superviviente para el acto 18** y **NO mueve la particion del
racimo de la supervision de la IA**. El orden de la fase sigue siendo el de la linea
**62**, la regla de la ficha envejecida la de la **3338**, el
carril del lote B el de la **4080**, el del acto 12 sin letra el de la
**4797** y la correccion declarada de la cita de esta vuelta el de la
**5074**.


---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 68, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (26 ago 2026, vuelta 69, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **NUEVE** veces, la ultima de ellas la del acta 67 en la linea
**5031** y la anterior la del acta 66 en la **4478**, **las dos cotejadas HOY
abriendo el fichero**. **Ninguna cifra publicada de arriba se toca.**

**NINGUNA CITA DE LINEA DE ESTA SECCION ESTA TECLEADA**, que es el procedimiento que la vuelta 68
estreno y que esta vuelta hereda entero: cada una es una marca que el registrador sustituye por el
numero que le devuelve **buscar su aguja de contenido** en el fichero, y **antes de escribir una sola
letra el instrumento vuelve a barrer el texto ya sustituido y exige que TODO numero de linea que
aparezca en el salga de una aguja**; si uno solo no sale, cae en `ROJO` y **no escribe nada**.

**El acta de la vuelta 68 abre en la linea **18205** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md)**, su verificacion por corrida propia en la
**18218**, su relectura ciega en la **18364**, sus caidas en la **18389**,
sus dieciseis adjudicaciones en la **18422**, sus adjudicaciones nuevas y sus pendientes
en la **18513**, su metrica de credito en la **18587** y sus condiciones de parada
en la **18620**.

### a) **LA CAIDA DE REPORTE DEL EJECUTOR, CON SU NOMBRE Y SU MEDICION: EL `D9` DIJO CUATRO Y LO MEDIDO ES SEIS**

**Se registra aqui, y no solo en el acta, porque una caida que solo vive en un acta se olvida.** **Y
se dice primero lo que NO cayo**: la cuenta equivocada vivia **solo en `REPORTE.md`**, **esta pagina
publica la tabla entera de perdidas con sus atenuantes verbatim y NO publica esa cuenta agregada**, y
**ninguna cifra de `docs/plan/` ni del banco se movio**.

| | lo que el acta 68 mide, copiado de su linea | linea |
|---|---|---:|
| **lo que el reporte dijo** | **el `D9` del reporte de la vuelta 68 dice CUATRO perdidas con atenuante declarado** | **18393** |
| **lo que el auditor midio** | contadas por el auditor sobre el plan sellado y sobre el registro, **fila a fila: SEIS filas llevan `ATENUANTE DECLARADO` en su campo `que`** | **18395** |
| **las seis filas, nombradas** | **las filas 3, 4, 7, 8, 9 y 10** | **18396** |
| **la mitad que si era exacta** | **DOS de las seis son de la especie del pendiente 4**, las filas 8 y 10 | **18397** |
| **la lectura con la que el cuatro se entiende, y por que no basta** | excluir la fila 9, que el `D10` cuenta aparte, y la fila 7, que el `D8` cuenta aparte; **pero la frase publicada no dice eso: dice cuatro y son seis** | **18398** |
| **la especie** | **CAIDA DE REPORTE**: se registra con nombre, dispara la relectura al doble del tramo y **NO acumula para la parada** | **18401** |
| **la relectura al doble, ejecutada** | el tramo es la tabla de perdidas, **releida ENTERA y DOS VECES** (las 11 filas en el plan sellado y las 11 en el registro), **con la cuenta de atenuantes hecha por dos vias** | **18407** |
| **la cuenta buena, contada fila a fila por el auditor** | **11 filas**, especies **7 `DE PARAMETRO DE PASO`** y **4 `DE CONDICIONES`**; **DOS filas con dos sedes** en el campo `donde`; **SEIS con atenuante declarado**; y las **CUATRO `DE CONDICIONES`** del pendiente son las filas 5, 6, 10 y 11 | **18330** |

> **LA REGLA QUE SALE DE ESTA CAIDA, y vale desde hoy para todo lote:** **toda cuenta agregada que se
> publique sobre una tabla** (cuantas filas cumplen `X`) **se deriva CONTANDO POR MAQUINA en la
> corrida de esa vuelta, no de memoria del reparto**; y **si se excluyen filas de una cuenta porque
> otro discutible las cubre, la frase lo DICE**. **Una cuenta que el autor recuerda no es una cuenta
> medida**, que es la misma familia de la regla 2 del ejecutor (*el instrumento manda*) aplicada al
> agregado y no solo a la celda.

### b) **EL CONTADOR DE PARADA VUELVE A CERO, Y LA RACHA DE REPORTE SE ROMPE EN LA CUARTA**

**Se escribe con estas letras porque manda sobre esta vuelta y sobre la siguiente.**

| | lo medido al cierre de la tanda 68 | linea |
|---|---|---:|
| **caidas de CLASE y de CIFRA PUBLICADA** | **CERO y CERO** | **18389** |
| **caidas de REPORTE** | **UNA**, la cuenta del `D9` | **18389** |
| **el contador de parada** | **VUELVE A CERO**: la 67 lo dejo en UNO, la parada pide **DOS TANDAS SEGUIDAS** con caida de clase o de cifra publicada, y **la segunda no llego** | **18411** |
| **la racha de reporte** | **ROTA en la cuarta tanda**, con **UNA** caida; **TRES seguidas de esta especie si serian `PARADA`** | **18411** |
| **las rachas escritas juntas** | **CLASE O CIFRA EN CERO otra vez**; **REPORTE roto en la cuarta** | **18615** |
| **el acumulado** | **464 relecturas, 794 puestos, 7 caidas de clase, 28 de reporte del ejecutor, 14 de cifra publicada del ejecutor, 3 de cifra del auditor, 7 de acta del auditor y 4 de procedimiento del auditor** | **18610** |

### c) **LOS DIECISEIS DISCUTIBLES, ADJUDICADOS: LOS DIECISEIS `A FAVOR`, CON LA CUENTA DEL `D9` CAIDA APARTE**

**La cifra de cabecera y el detalle coinciden**: **dieciseis marcados, dieciseis adjudicados, cero
sin contestar**, y **la unica discrepancia del dia no esta en la lista sino en una cuenta**, que es
lo que el apartado a) registra.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | el ensanche de la guarda de citas con cuatro mecanismos donde el encargo pedia dos | **`A FAVOR`**: las dos condiciones del acta 61 cumplidas, y **los dos mecanismos de mas son guardas que aprietan**, justificadas por la especie exacta de la caida de la 67 | **18425** |
| **`D2`** | fundir el `acto 22`, bloque de cuatro de un racimo cuyo inventario dice *en mesa* | **`A FAVOR`**, y **la pregunta 5 queda adjudicada** (apartado e): el dueno es **EL MEDIDO**, la particion **calza al digito** y el precedente es doble | **18432** |
| **`D3`** | el superviviente del `acto 22` contra el cableado 7 a 3 | **`A FAVOR`**: **`P.8` es regla de PRELACION** y la vara de pasos hablo; **el cableado solo decide a contenido empatado** | **18442** |
| **`D4`** | el nodo de nueve pasos | **`A FAVOR`** por el carril del `D8` del acta 67; **la redaccion fina es de la fase 04** | **18447** |
| **`D5`** | tres `APPEND` de condicion en el `acto 19` | **`A FAVOR`**: la vara del acta 55 pregunta 5 es **disparador DISTINTO**, y **los tres lo son**; tres de golpe es **volumen, no una regla rota** | **18451** |
| **`D6`** | el `acto 18` en transito sin superviviente elegido | **`A FAVOR`**: es **el carril que el acta 67 adjudico, ejecutado a la letra**; el costo de seis cerrados en vez de siete **es el diseno del carril, no una perdida** | **18457** |
| **`D7`** | declarar el lote en seis | **`A FAVOR`**: el encargo manda **declarar al abrir y entregar lo declarado**, y **ninguna letra fija el tamano** | **18463** |
| **`D8`** | dos perdidas con dos sedes en una fila | **`A FAVOR`**: es la aplicacion consciente del `D10` del acta 67, **la fila es POR PIEZA** | **18468** |
| **`D9`** | sobre-sellar perdidas con atenuante declarado | **LA PRACTICA `A FAVOR`** (declarar es mas auditable que callar), **con LA CUENTA CAIDA aparte**: la buena es **SEIS**, dos del pendiente 4 | **18471** |
| **`D10`** | sellar la perdida que el `INCISO` del mismo acto repara | **`A FAVOR`**: **el sello es del reparto y no del resultado**, y el atenuante medido evita el doble conteo | **18475** |
| **`D11`** | un `CUBIERTO` que apunta al superviviente cuando el contenido llega por el `APPEND` del hermano | **`A FAVOR`** como **la mejor marca DISPONIBLE** mientras el pendiente 4 no tenga marca propia, con la perdida declarandolo | **18480** |
| **`D12`** | los dos `INCISO` con nexo de coma sobre pasos que no terminan en punto | **`A FAVOR`**: la guarda de la **JUNTURA ROTA** cubre la especie del `D5` del acta 66 y **aqui no aplica** | **18485** |
| **`D13`** | la fila de duenos en `tabla_declarado` sin encargo | **`A FAVOR`** con las dos condiciones del acta 61 cumplidas: **una razon de cierre que solo vive en la prosa se pierde** | **18490** |
| **`D14`** | importar la guarda en vez de copiarla | **`A FAVOR` CON LA REGLA DICHA**: el carril de copiar protege a los registradores de **VUELTAS DISTINTAS**; **dentro de LA MISMA vuelta el import garantiza identidad mejor que la copia** | **18494** |
| **`D15`** | el plan sellado dos veces | **`A FAVOR`**: el diff de sellos esta **medido en UNA linea** y **el plan no se habia ejecutado**; **un plan EJECUTADO no se re-sella** | **18501** |
| **`D16`** | leer entero y declarar el acto con dueno en vez de saltarlo | **`A FAVOR`**: **la letra prohibe FUNDIR un acto con dueno, no leerlo**, y la lectura produjo dos razones mas | **18506** |

### d) **EL SUPERVIVIENTE DEL `ACTO 18`, ADJUDICADO POR EL AUDITOR: `alianzas_cross_industry`, CON LAS CINCO PIEZAS QUE EL PLAN TIENE QUE CONSERVAR O SELLAR**

**Es la mitad que le faltaba al carril del `EMPATE SIN VARA`** (registrado en la linea
**5152** de esta pagina, y estrenado sobre este acto en la **5506**):
**el ejecutor escribe el caso y NO elige; el auditor adjudica en su acta con el caso delante; y el
lote siguiente ejecuta esa fusion como su primera operacion.** **El acta lo cerro**, y la
adjudicacion abre en la linea **18515**.

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **el superviviente** | **`alianzas_cross_industry`** | **18518** |
| **PRIMERA, el alcance** | **es el unico de los cuatro que apunta al MERCADO ENTERO** (el poder de compra colectivo para mover el mercado hacia otro tipo de producto); **los otros tres caben dentro de ese marco y el marco no cabe en ninguno de los tres** | **18521** |
| **SEGUNDA, el reparto con menos perdida** | **sus piezas ya alojan lo propio de los otros con la costura mas corta**: su condicion 1 **ES** el test del poder de mercado dicho como condicion, su paso 2 aloja la convocatoria por asociaciones, y su paso 3 son los estandares comunes | **18526** |
| **TERCERA, lo buscable** | **trae los nombres propios** (`EICC`, `AIM-PROGRESS`) **que la razon del puesto 1903 senala como lo que vuelve buscable el paso** | **18533** |
| **CUARTA, el cableado no lo desmiente** | **empata en cabeza** (3 con `co_opetition_industria`), **y entre esos dos deciden el alcance y el reparto** | **18535** |

> **LAS CINCO PIEZAS QUE EL PLAN DEL LOTE E TIENE QUE CONSERVAR O SELLAR, nombradas para que no se
> pierdan en el reparto** (linea **18538**): **1)** publicar y monitorear el
> cumplimiento colectivo (`co_opetition_industria`, paso 4); **2)** aplicar el estandar conjunto a
> los proveedores compartidos (`trabajo_colectivo_estandares_industria`, paso 4); **3)** el test del
> poder de mercado como **arranque explicito** (`colaboracion_sectorial`, paso 1); **4)** el encuadre
> por **riesgo reputacional compartido** (`trabajo_colectivo_estandares_industria`, condicion 1); y
> **5)** el marco nombrado **Responsible Care** (`trabajo_colectivo_estandares_industria`, paso 3).
> **El reparto pieza a pieza es del ejecutor bajo el contrato `CAMPO PROPIO`**, con simulacion previa
> y todas las guardas.

**LAS TRES RAZONES QUE SOSTIENEN LA FAMILIA, y son las que el ejecutor leyo enteras antes de que el
auditor adjudicara:** el puesto **1797** (la misma alianza entre competidores dos veces), el
**1871** (la familia pasa de DOS a TRES por cierre transitivo) y el **1903** (de TRES a CUATRO).
**La ciega del auditor sobre este acto dio 1 de 1 en el fondo**, con los cuatro textos leidos
enteros antes de destapar las razones (linea **18364**).

### e) **LA PREGUNTA 5, ADJUDICADA: UN ESTADO DE INVENTARIO *EN MESA* CON `operaciones` VACIO NO ES DUENO, Y LA FRONTERA QUEDA ESCRITA**

**Adjudicado POR EXTENSION CITABLE** (linea **18548**), **y no es doctrina nueva**: es **el
criterio con el que `OP-U-02` abrio su universo**, mas el precedente del `acto 11` (misma nomina,
mismo estado) y el carril del `acto 17` con el puesto 460.

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **el criterio** | **el dueno a efectos del universo de `OP-U-02` es EL MEDIDO: los dos campos `duenos_*` del tramo fijado y el campo `operaciones` de la entrada del inventario** | **18551** |
| **LA FRONTERA, y se escribe para que no oscile** | **si la entrada del inventario nombra una operacion en su campo `operaciones`, o el tramo trae dueno en cualquiera de los dos campos, ESO es dueno y el acto NO se funde** | **18559** |

> **LA FUSION DEL `ACTO 22` NO SE DESHACE** (linea **18432**), y su registro sigue donde estaba,
> en la linea **5317** de esta pagina.

### f) **LA PREGUNTA 6, ADJUDICADA: LA FUSION DEL TRANSITO ABRE EL LOTE `E` CON PLAN PROPIO Y CUENTA EN SU DECLARACION**

**Adjudicado POR EXTENSION** (linea **18562**), **extension del carril del transito y del patron
de un plan por lote**, que es como esta pagina viene sellando los lotes desde el `A` (linea
**5218** para el ultimo de ellos).

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **con que plan** | **dentro del PLAN PROPIO del lote `E`, sellado por `generar_plan_del_lote.py` como cualquier otro**; **el plan del lote `D` NO se reabre** | **18564** |
| **en que puesto del lote, y si cuenta** | **como PRIMERA operacion del lote `E`**, y **el `acto 18` CUENTA en la declaracion del lote como uno de los que cierran ENTEROS** | **18564** |

### g) **LOS PENDIENTES HEREDADOS, NOMBRADOS CON SU DESTINO**

**Se registran porque mandan sobre lo que viene aunque no encarguen trabajo hoy.**

| | lo que el acta 68 deja escrito | destino | linea |
|---|---|---|---:|
| **el subconjunto cerrado de un acto con puente** | sigue **NOMBRADO**, ahora con **TRECE actos declarados esperandolo** (1, 5, 10, 11, 12, 13, 14, 15, 17, 20, 21, 23 y 24), **contados por el auditor** | **el cierre de la fase 03**, donde la parada de `AUDITOR.md` espera al fundador | **18571** |
| **la marca para *ya lo dice el `APPEND` de un hermano*** | sigue **NOMBRADO**; **el carril vigente alcanza** y la vuelta 68 lo pago **DOS veces** con atenuante declarado | **la cuenta crece y se publica en cada lote** | **18576** |
| **el `INCISO` de condiciones** | sigue en su carril, con **CUATRO piezas `DE CONDICIONES` mas** (filas 5, 6, 10 y 11) | **la fase 04** (acta 55, pregunta 5) | **18580** |
| **el esquema de `OPERACIONES.jsonl`** | sigue **pendiente**; la vuelta 68 **no toco ninguna ficha y no estreno ninguna clave** | **sin fecha, y se dice** | **18583** |
| **el cierre de la fase 03** | **NO SE CUMPLE TODAVIA**: quedan **27 actos y 85 nodos**, la mesa `OP-M-03`, y los trece declarados | **la parada escrita de `AUDITOR.md`, tal como esta** | **18640** |

**LOS CUATRO MOTIVOS SELLADOS DEL `DECLARADO Y NO FUNDIDO` SIGUEN SIENDO CUATRO Y LA LISTA SIGUE SIN
SER CERRADA:** el triangulo de `P.10` (linea **3744**), la guarda `1B` (linea
**4023**), la respuesta *DOS FAMILIAS* de `P.5` (linea **4518**) y el
veredicto `D` directo interno (linea **5121**). **La linea base del censo de
colisiones sigue en `4`** (linea **4542**) y **el carril de las dos de la mesa sigue
donde estaba** (linea **3653**).

### h) **LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya**

**NO toca ni una cifra publicada arriba**, **NO funde ni deshace nada**, **NO elige ningun
superviviente** (el del `acto 18` lo eligio el auditor y aqui solo se transcribe), **NO re-lee ni un
veredicto de las cuatro colisiones vigentes**, **NO toca la mesa `OP-M-03`**, **NO toca ninguna ficha
de `OP-U-02` ni de `OPERACIONES.jsonl`** y **NO abre el lote `E`**: **registra adjudicaciones**. El
lote `E` es la TAREA 2 de esta misma vuelta y se registra en su propia seccion, debajo de esta.


---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE E` (2026-08-26, vuelta 69)

**Se adosa al final del documento, bajo la cabecera de tramo que la vuelta 65 dejo en la linea
**3732**, y NO reescribe ni una linea de las secciones de arriba.** El orden de la
fase sigue siendo el de la linea **62**; el registro del lote `C` esta en la
**4621** y el del lote `D` en la **5218**.

**EL LOTE SE DECLARO AL ABRIRLO Y SE ENTREGO ENTERO: SEIS actos y 22 nodos.** **Abre con LA FUSION
ADJUDICADA DEL `ACTO 18`**, que el acta 68 resolvio y que esta pagina registra en la linea
**5655**, ejecutada **como PRIMERA operacion del lote y dentro de un PLAN PROPIO** (la
adjudicacion esta en la linea **5701**: el plan del lote `D` NO se reabre, y el acto
CUENTA en la declaracion como cierre ENTERO). **Despues sigue el PREFIJO SIN SALTOS desde el `acto
25`.**

| | |
|---|---|
| **actos que cierran ENTEROS** | **6**: el **18**, **25**, **26**, **29** y **30** FUNDIDOS, y el **27** `DECLARADO Y NO FUNDIDO` |
| **nodos del lote** | **22** |
| **nodos que MUEREN** | **13** |
| **vivos del catalogo** | de **3237** a **3224** |
| **ficheros tocados** | **49** |
| **piezas repartidas** | **78** (**14** viajan enteras, **58** ya estaban dichas) |
| **EL TOPE DEL PREFIJO, y es ESTRUCTURAL** | el siguiente es el **acto 31**, que **TIENE DUENO** (`OP-F-04-WEI` y `OP-S-04`, medido hoy sobre el fichero fijado) y que **no trae ninguno de los cuatro motivos sellados** con los que podria cerrar `DECLARADO`: **no podria cerrar ENTERO**, y el contrato del lote es entregar lo declarado |

**LAS FORMAS MEDIDAS DEL LOTE, y `P.8` aplicado en orden sobre cada una:**

| acto | miembros | **FORMA medida** | cierra | **la letra que decide** |
|---:|---:|---|---|---|
| **18** | 4 | `EMPATE SIN VARA` | **FUNDIDO** | **ninguna vara apunta**: lo adjudico el auditor, y este plan EJECUTA esa adjudicacion |
| **25** | 4 | `CONTENIDO EMPATA` | **FUNDIDO** | **el cableado DECIDE SOLO** y apunta a **la MISMA puerta** que la guarda `1B` obliga a conservar |
| **26** | 4 | `CHOCAN` | **FUNDIDO** | **decide LA PIEZA DECLARADA**, y apunta al mismo nodo que la vara de pasos, el cableado y la puerta |
| **27** | 4 | `TODAS DE ACUERDO` | **`DECLARADO Y NO FUNDIDO`** | **no llega a aplicarse: `P.10` detiene ANTES**, y la figura del inventario tambien |
| **29** | 3 | `UNA SOLA VARA` | **FUNDIDO** | **una sola vara BASTA**: la de condiciones, con pasos y cableado empatados |
| **30** | 3 | `CHOCAN` | **FUNDIDO** | **decide LA PIEZA DECLARADA**, y aqui la declaracion es **verbatim** del puesto **2838** |

> **LA GUARDA `1B` MUERDE EN DOS ACTOS DE ESTE LOTE Y NO PARA NINGUNO**, que es la mitad de la letra
> que menos se usa: el `acto 25` y el `acto 26` tienen **UNA** puerta cada uno, y con **UNA** puerta
> el acto **si se funde y la puerta SOBREVIVE** (acta 54, pregunta 1), frente al caso de **DOS o
> mas**, que cierra `DECLARADO` y esta registrado en la linea **4023**.

### a) **EL `ACTO 18`: LA FUSION QUE EL EJECUTOR NO ELIGIO, Y LAS CINCO PIEZAS DEL ACTA CONSERVADAS LAS CINCO**

**Es el cierre del carril del `EMPATE SIN VARA`** (registrado en la linea **5152** y
estrenado sobre este mismo acto en la **5506**). **La vuelta 68 lo dejo `ABIERTO
EN TRANSITO` sin elegir superviviente; el acta 68 adjudico `alianzas_cross_industry`; y esta vuelta
ejecuta esa fusion.** **El ejecutor no re-decidio nada: reparte.**

**`P.5`, contestada sobre el texto estable: ES UNA FAMILIA**, los cuatro del mismo libro (*The Green
to Gold Business Play*, de Esty), con **tres pares internos leidos y los tres en `A`** (puestos
**1797**, **1871** y **1903**), **cero `D`**, **cero nodos puente** y **cero triangulos**.

**LAS CINCO PIEZAS QUE EL ACTA MANDO CONSERVAR O SELLAR QUEDAN LAS CINCO CONSERVADAS**, y ninguna
sellada como perdida:

| pieza nombrada por el acta 68 | de donde sale | **como se conserva** |
|---|---|---|
| publicar y monitorear el cumplimiento colectivo | `co_opetition_industria`, paso 4 | **`APPEND`** |
| aplicar el estandar conjunto a los proveedores compartidos | `trabajo_colectivo_estandares_industria`, paso 4 | **`APPEND`** |
| el marco nombrado *Responsible Care* | `trabajo_colectivo_estandares_industria`, paso 3 | **`APPEND`** |
| el encuadre por riesgo reputacional compartido | `trabajo_colectivo_estandares_industria`, condicion 1 | **`APPEND`** |
| el test del poder de mercado **como arranque explicito** | `colaboracion_sectorial`, paso 1 | **`INCISO` ADOSADO AL PASO 1**, que es **la unica forma de que siga siendo un arranque**: un `APPEND` lo habria puesto al final |

**El nodo crece de 4 pasos a 7 y de 2 condiciones a 4.** **EL REPARTO,
PIEZA POR PIEZA, GENERADO DEL PLAN SELLADO:**

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `co_opetition_industria` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `co_opetition_industria` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **3** de `co_opetition_industria` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `co_opetition_industria` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `co_opetition_industria` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `co_opetition_industria` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **1** de `colaboracion_sectorial` | `INCISO` | **`INCISO` ADOSADO** al paso 1: *si la empresa tiene suficiente poder de mercado para exigir cambios individualmente* |
| paso **2** de `colaboracion_sectorial` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **3** de `colaboracion_sectorial` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `colaboracion_sectorial` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| condicion **1** de `colaboracion_sectorial` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `colaboracion_sectorial` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **1** de `trabajo_colectivo_estandares_industria` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `trabajo_colectivo_estandares_industria` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `trabajo_colectivo_estandares_industria` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `trabajo_colectivo_estandares_industria` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `trabajo_colectivo_estandares_industria` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **2** de `trabajo_colectivo_estandares_industria` | `APPEND` | **viaja ENTERA** al superviviente |

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `co_opetition_industria` | 4 | 2 | 1 | 5 | 0 |
| `colaboracion_sectorial` | 4 | 2 | 0 | 5 | 1 |
| `trabajo_colectivo_estandares_industria` | 4 | 2 | 4 | 2 | 0 |
| **los 3 juntos** | **12** | **6** | **5** | **12** | **1** |

**LAS PERDIDAS SELLADAS EN CAMPO PROPIO, recortadas enteras de la salida del tallador:**

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V69_OPU02_LOTE_E.json | 18 | DE PARAMETRO DE PASO | EL CANAL DE LA CONVOCATORIA: convocar MEDIANTE LAS ASOCIACIONES INDUSTRIALES EXISTENTES, que la razon del puesto 1797 llama la unica linea que dice por donde se convoca sin que parezca acuerdo entre competidores. El paso 2 del superviviente manda BUSCAR COALICIONES EXISTENTES o formar una nueva, que es el mismo terreno visto desde quien se suma y no desde quien convoca. ATENUANTE DECLARADO: ese paso 2 trae ademas los nombres propios de las coaliciones, asi que el sitio donde buscarlas no se pierde. UNA SOLA PIEZA CON DOS SEDES, sellada una vez con las dos nombradas (acta 67, D10) | paso 2 de co_opetition_industria y paso 2 de colaboracion_sectorial | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 18 | DE PARAMETRO DE PASO | las METAS COMPARTIDAS DE DESEMPENO AMBIENTAL, o sea la parte MEDIBLE del pacto. El paso 3 del superviviente define ESTANDARES COMUNES DE CONDUCTA social y ambiental para toda la industria, que es la regla, pero en ningun paso pide metas de desempeno contra las que medirse | paso 3 de co_opetition_industria | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 18 | DE PARAMETRO DE PASO | las METRICAS Y COMPROMISOS CONJUNTOS para los proveedores comunes, dichos como definicion propia. ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: el APPEND del paso 4 de trabajo_colectivo_estandares_industria manda APLICAR EL ESTANDAR CONJUNTO A PROVEEDORES COMPARTIDOS, o sea que la palanca hacia arriba en la cadena llega entera por el hermano; lo que no llega es la palabra METRICAS | paso 4 de colaboracion_sectorial | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 18 | DE PARAMETRO DE PASO | el RIESGO REPUTACIONAL COMPARTIDO dicho como PRIMER PASO, o sea como test de arranque y no como disparador. ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: el encuadre llega entero por el APPEND de la condicion 1 de este mismo nodo, pero cambia de sitio, de paso a condicion | paso 1 de trabajo_colectivo_estandares_industria | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 18 | DE CONDICIONES | la CRISIS REGULATORIA compartida como disparador. La mitad reputacional de esa condicion llega entera por el APPEND de la condicion 1 de trabajo_colectivo_estandares_industria; lo que se pierde es la palabra REGULATORIA, que es el unico sitio del acto donde el disparador es el regulador y no el mercado ni la prensa | condicion 1 de co_opetition_industria | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V69_OPU02_LOTE_E.json | 18 | DE CONDICIONES | las ECONOMIAS DE ESCALA en la colaboracion sectorial como disparador. Las dos condiciones del superviviente miran la DEBILIDAD (el poder de compra individual insuficiente) y el PROBLEMA (el desafio sistemico); ninguna mira el AHORRO de hacerlo juntos | condicion 2 de colaboracion_sectorial | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V69_OPU02_LOTE_E.json | 18 | DE CONDICIONES | el alcance del test sobre los PROVEEDORES: no tener poder individual SOBRE PROVEEDORES. La condicion 1 del superviviente mide el poder de compra sobre EL MERCADO, que es mas ancho y por eso no dice lo mismo. ATENUANTE DECLARADO Y MEDIDO: el INCISO al paso 1 de este mismo acto adosa el test del poder de mercado VERBATIM como arranque, asi que el test no se pierde; lo que se pierde es el objeto proveedores | condicion 1 de colaboracion_sectorial | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |

### b) **EL `ACTO 25`: LA PUERTA SOBREVIVE, Y ESTA FUSION FABRICA DOS COLISIONES DE CLASE**

**`P.5`, contestada: ES UNA FAMILIA, y es el acto MEJOR LEIDO del prefijo**: cuatro miembros del
mismo libro (*SPIN Selling*, de Rackham), **CINCO pares internos leidos de seis y los CINCO en `A`**
(puestos **209**, **278**, **303**, **800** y **862**), cero `D`, cero puentes, cero triangulos. **La
cuarta membresia la declara el archivo y no el ejecutor**: el **800** dice que **la familia no es de
tres sino de CUATRO** y que el cuarto puro queda degradado a sub-puro, y el **862** la deja en cinco
de seis.

**EL RACIMO CENSADO NO SE PARTE, Y ESO SE MIDE:** el racimo *La etapa de investigacion en la venta*
de `docs/RACIMOS_MIEMBROS.jsonl` tiene nomina de **TRES** y **los TRES estan DENTRO de este acto**:
el racimo cabe entero en el acto y esta fusion no lo corta por ningun sitio.

**LA PUERTA:** `enfoque_etapa_investigacion` **es puerta**, medido contra el universo protegido de
**256** ids, **y es UNA sola**, asi que **sobrevive**. **El cableado apunta al MISMO nodo** (6 contra
un maximo de 3), o sea que **no hay choque que resolver**, y se dice para que nadie tenga que
reconstruirlo.

**El nodo crece de 4 pasos a 6 y se queda en 2 condiciones.** **CERO `INCISO` y
es por la puntuacion**: los cuatro pasos del superviviente terminan en punto y la guarda de la
**JUNTURA ROTA** los habria rechazado. **CERO perdidas `DE CONDICIONES`, y se dice en vez de
callarlo.**

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `etapa_de_investigacion` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `etapa_de_investigacion` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **3** de `etapa_de_investigacion` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `etapa_de_investigacion` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| condicion **1** de `etapa_de_investigacion` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **1** de `etapa_investigacion_ventas` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `etapa_investigacion_ventas` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `etapa_investigacion_ventas` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| paso **4** de `etapa_investigacion_ventas` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **1** de `etapa_investigacion_ventas` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **2** de `etapa_investigacion_ventas` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **1** de `investigacion_como_habilidad_clave` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `investigacion_como_habilidad_clave` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **3** de `investigacion_como_habilidad_clave` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `investigacion_como_habilidad_clave` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| condicion **1** de `investigacion_como_habilidad_clave` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `investigacion_como_habilidad_clave` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `etapa_de_investigacion` | 4 | 1 | 1 | 4 | 0 |
| `etapa_investigacion_ventas` | 4 | 2 | 0 | 6 | 0 |
| `investigacion_como_habilidad_clave` | 4 | 2 | 1 | 5 | 0 |
| **los 3 juntos** | **12** | **5** | **2** | **15** | **0** |

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V69_OPU02_LOTE_E.json | 25 | DE PARAMETRO DE PASO | EL NIVEL DE EQUIPO: que la prioridad de las preguntas sobre la presentacion sea una decision de DESARROLLO DE HABILIDADES del equipo comercial y no solo de la planificacion de la llamada propia. El paso 1 del superviviente manda dedicar mas tiempo a disenar preguntas que a preparar el discurso de producto, que es la misma prioridad dicha para una sola cabeza. ATENUANTE DECLARADO: el paso 4 del superviviente si ordena el ENTRENAMIENTO, primero Situacion y Problema y despues Implicacion y Necesidad-beneficio, asi que el nivel de equipo asoma por ahi aunque no acompane a la prioridad | paso 1 de etapa_investigacion_ventas | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 25 | DE PARAMETRO DE PASO | entrenar al equipo en preguntas que revelen NECESIDADES OCULTAS. El paso 4 del superviviente entrena por TIPO de pregunta (Situacion, Problema, Implicacion, Necesidad-beneficio) y no por lo que la pregunta tiene que sacar a la luz. ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: lo de los problemas que el cliente no dice llega entero por el APPEND del paso 3 de investigacion_como_habilidad_clave, que es su hermano en este mismo acto | paso 3 de etapa_investigacion_ventas | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 25 | DE PARAMETRO DE PASO | EL CONOCIMIENTO TECNICO DEL PRODUCTO COMO SUSTITUTO DE INDAGAR, nombrado. El paso 2 del superviviente prohibe MOSTRAR BENEFICIOS O CAPACIDADES antes de desarrollar el problema, que es la conducta, pero no nombra la causa que el absorbido si nombra: apoyarse en lo que uno sabe del producto. La razon del puesto 862 declara este gesto COMUN a los dos nodos; el texto del superviviente no lo dice, y PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3) | paso 2 de investigacion_como_habilidad_clave | la fase 04, que redacta y afina los pasos del superviviente |

> **LO QUE ESTA FUSION CUESTA, Y VA EN SU PROPIO APARTADO PORQUE ES LO MAS CARO DEL LOTE:** **fabrica
> DOS colisiones de clase**, predichas antes de tocar un nodo y publicadas en el apartado g).

### c) **EL `ACTO 26`: EL PRIMER `CHOCAN` DEL TRAMO QUE LLEGA A FUNDIRSE, Y EL NODO MAS GRANDE**

**`P.5`, contestada con la razon que la cerro delante: ES UNA FAMILIA.** Tres pares internos leidos y
los tres en `A` (puestos **230**, **381** y **839**), cero `D`, cero puentes, cero triangulos. **Son
DOS libros distintos** (*Change by Design* de Brown y *Winning at New Products* de Cooper) **y eso NO
parte la familia**: el **839** es justamente **el par que CRUZA las dos parejas ya declaradas** y
dice con todas sus letras que son **CUATRO nodos del mismo instrumento y no dos parejas vecinas**.

**LA FORMA ES `CHOCAN` Y DECIDE LA PIEZA DECLARADA:** la vara de PASOS apunta a
`investigacion_etnografica_ideacion` (6 contra 5) y la de CONDICIONES al otro lado (3 contra 2).
**Las otras dos cuentas apuntan al mismo sitio que los pasos**: el cableado (14 contra 8) **y la
puerta**, que aqui vuelve a ser UNA sola y sobrevive. **Este `CHOCAN` no deja residuo.**

**El nodo crece de 6 pasos a 9 y de 2 condiciones a 3.** **NUEVE PASOS
IGUALA AL NODO MAS GRANDE QUE ESTE TRAMO HA PRODUCIDO** y va dicho en vez de maquillado. **UN solo
`INCISO`, al paso 2**: *deputizar*, que es un **parametro** de la observacion que el superviviente ya
manda hacer, no un gesto aparte.

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `etnografia_aplicada_en_equipos_multidisciplinarios` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **2** de `etnografia_aplicada_en_equipos_multidisciplinarios` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **3** de `etnografia_aplicada_en_equipos_multidisciplinarios` | `INCISO` | **`INCISO` ADOSADO** al paso 2: *a líderes o clientes (deputizar) en la observación de campo para generar empatía directa* |
| paso **4** de `etnografia_aplicada_en_equipos_multidisciplinarios` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **1** de `etnografia_aplicada_en_equipos_multidisciplinarios` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **2** de `etnografia_aplicada_en_equipos_multidisciplinarios` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **1** de `etnografia_de_proyecto` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| paso **2** de `etnografia_de_proyecto` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **3** de `etnografia_de_proyecto` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `etnografia_de_proyecto` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **5** de `etnografia_de_proyecto` | `APPEND` | **viaja ENTERA** al superviviente |
| condicion **1** de `etnografia_de_proyecto` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `etnografia_de_proyecto` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **1** de `etnografia_investigacion_usuario` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `etnografia_investigacion_usuario` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **3** de `etnografia_investigacion_usuario` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `etnografia_investigacion_usuario` | `CUBIERTO` | ya lo dice el **paso 6** del superviviente |
| paso **5** de `etnografia_investigacion_usuario` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| condicion **1** de `etnografia_investigacion_usuario` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `etnografia_investigacion_usuario` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **3** de `etnografia_investigacion_usuario` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `etnografia_aplicada_en_equipos_multidisciplinarios` | 4 | 2 | 2 | 3 | 1 |
| `etnografia_de_proyecto` | 5 | 2 | 2 | 5 | 0 |
| `etnografia_investigacion_usuario` | 5 | 3 | 0 | 8 | 0 |
| **los 3 juntos** | **14** | **7** | **4** | **16** | **1** |

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V69_OPU02_LOTE_E.json | 26 | DE PARAMETRO DE PASO | LA INMERSION PROFUNDA como forma de la observacion: convivencia y estadias EN LUGAR DE entrevistas puntuales. El paso 2 del superviviente manda observar durante un PERIODO EXTENDIDO, que es duracion y no convivencia, y su paso 5 empuja en el sentido contrario, REDUCIR EL TIEMPO POR VISITA si hace falta. ATENUANTE DECLARADO: el periodo extendido del paso 2 conserva la mitad larga de la pieza | paso 2 de etnografia_aplicada_en_equipos_multidisciplinarios | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 26 | DE PARAMETRO DE PASO | CONSTRUIR CONFIANZA CON LAS COMUNIDADES ESTUDIADAS antes de extraer conclusiones de diseno, dicho sobre COMUNIDADES y no sobre sujetos. ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: el gesto llega entero por el APPEND del paso 5 de etnografia_de_proyecto, que lo dice sobre LOS SUJETOS OBSERVADOS; lo que no llega es la palabra COMUNIDADES | paso 4 de etnografia_aplicada_en_equipos_multidisciplinarios | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 26 | DE PARAMETRO DE PASO | ENSAMBLAR UN EQUIPO CROSS-DISCIPLINARIO con perfiles tecnicos y sociales. El paso 4 del superviviente CAPACITA al equipo observador en escucha e inferencia, que es entrenar a quien ya esta, no elegir de que esta hecho. ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: la composicion mixta llega entera y con mas detalle por el APPEND del paso 1 de etnografia_aplicada_en_equipos_multidisciplinarios | paso 1 de etnografia_de_proyecto | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 26 | DE PARAMETRO DE PASO | DEPUTIZAR dicho por segunda vez, con la palabra CONSIDERAR delante y sobre CLIENTES O EJECUTIVOS PROPIOS. ATENUANTE DECLARADO Y MEDIDO: el INCISO al paso 2 de este mismo acto adosa VERBATIM el deputizar del hermano, asi que la pieza NO se pierde de hecho; se sella igual porque el sello es del reparto y no del resultado (acta 68, D10) | paso 4 de etnografia_de_proyecto | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 26 | DE PARAMETRO DE PASO | OBSERVAR SIN INTERFERIR. El paso 2 del superviviente manda observar DIRECTAMENTE a los usuarios usando o mal usando el producto, y recoge por tanto el mal uso, pero en ningun sitio dice que el observador no intervenga. Es la unica linea del acto que pone una regla sobre la conducta DEL OBSERVADOR, y el puesto 839 la nombra como lo propio de etnografia_investigacion_usuario | paso 2 de etnografia_investigacion_usuario | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 26 | DE PARAMETRO DE PASO | LA TIPOLOGIA DE LO QUE SE DOCUMENTA: problemas FISICOS, EMOCIONALES Y CONTEXTUALES. El paso 3 del superviviente documenta problemas, quejas y comportamientos no verbalizados, que es una lista distinta y sin el eje emocional. El puesto 839 la nombra tambien como propia | paso 3 de etnografia_investigacion_usuario | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 26 | DE CONDICIONES | LA NECESIDAD DE CONFIANZA PROFUNDA con los usuarios ANTES de disenar, como disparador. Es el disparador propio del paso de confianza que este mismo acto adosa por APPEND, y ninguna de las dos condiciones del superviviente lo recoge | condicion 2 de etnografia_aplicada_en_equipos_multidisciplinarios | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |
| PLAN_V69_OPU02_LOTE_E.json | 26 | DE CONDICIONES | EL CONTEXTO FISICO COMPLEJO (campo, hospital, fabrica) como disparador. El paso 1 del superviviente nombra esos mismos sitios como EJEMPLO de donde observar, pero como PASO y no como condicion: el acto pierde el CUANDO y conserva el DONDE. ATENUANTE DECLARADO Y MEDIDO: los tres sitios estan escritos verbatim en el paso 1 del superviviente | condicion 3 de etnografia_investigacion_usuario | la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5) |

### d) **LOS `ACTOS 29` Y `30`: EL MAS BARATO DEL LOTE Y EL MAS RARO DEL TRAMO**

**EL `ACTO 29`, la familia del avance contra la continuacion.** `P.5`: **ES UNA FAMILIA**, los tres
del mismo libro, dos pares leidos y los dos en `A` (puestos **220** y **482**). **FORMA `UNA SOLA
VARA`**: pasos y cableado empatan y **la de CONDICIONES apunta**, y **una sola vara BASTA**. El nodo
crece de 4 pasos a 6.

> **EL RACIMO CENSADO SI SE TOCA AQUI, Y SE DECLARA EN VEZ DE CALLARSE.** El racimo *El avance y el
> compromiso en la venta* tiene nomina censada de **CINCO** y este acto contiene **DOS** de ellos.
> **Los otros TRES no se tocan y tienen casa propia MEDIDA**: `INVENTARIO.jsonl` trae la entrada
> racimo *el compromiso contado tres veces*, **forma `PURO`, estado sano y forma cerrada**, con
> nomina de exactamente esos tres. **El censo de cinco del cribado ya estaba PARTIDO en el inventario
> en un `PURO` de tres mas dos sueltos, y esta fusion opera sobre los DOS SUELTOS.**

**EL `ACTO 30`, la familia del viaje diagnostico de Juran.** `P.5`: **ES UNA FAMILIA**, los tres de
la misma fuente, dos pares leidos y los dos en `A` (puestos **2600** y **2838**). **FORMA `CHOCAN`**,
con el cableado **empatado** (o sea que ni podria desempatar si le tocara), **y decide LA PIEZA
DECLARADA**: el **2838** dice `A` **POR CONTENCION** y cierra con la frase *superviviente
viaje_diagnostico_remedial*, verbatim.

> **CUATRO `INCISO` EN UN SOLO ACTO, QUE ES LA CIFRA MAS ALTA DE LA CAMPANA**, y **ninguno apilado
> sobre el mismo paso**. **La razon esta medida y no es de gusto:** el superviviente ya trae ocho
> pasos y las cuatro piezas propias del absorbido **no son gestos nuevos sino PARAMETROS DE RIGOR** de
> gestos que el superviviente ya manda hacer (el Pareto, los diagramas causa-efecto, la recoleccion
> disenada para correlacionar y la validacion estadistica). **Los cuatro pasos que reciben `INCISO`
> no terminan en punto**, asi que la guarda de la **JUNTURA ROTA** no salta en ninguno. El nodo se
> queda en 8 pasos y crece de 1 condicion a 2.

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `advances_vs_continuations` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **2** de `advances_vs_continuations` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **3** de `advances_vs_continuations` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **4** de `advances_vs_continuations` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| condicion **1** de `advances_vs_continuations` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **1** de `objetivos_de_llamada_orientados_a_avance` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **2** de `objetivos_de_llamada_orientados_a_avance` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **3** de `objetivos_de_llamada_orientados_a_avance` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **4** de `objetivos_de_llamada_orientados_a_avance` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **1** de `objetivos_de_llamada_orientados_a_avance` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `advances_vs_continuations` | 4 | 1 | 0 | 5 | 0 |
| `objetivos_de_llamada_orientados_a_avance` | 4 | 1 | 2 | 3 | 0 |
| **los 2 juntos** | **8** | **2** | **2** | **8** | **0** |

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V69_OPU02_LOTE_E.json | 29 | DE PARAMETRO DE PASO | EL DESCARTE DE LOS OBJETIVOS VAGOS dicho por segunda vez, con RECOPILAR INFORMACION y CONSTRUIR RELACION nombrados. El paso 3 del superviviente disena la siguiente interaccion con el objetivo explicito de lograr una accion medible, o sea que manda lo que SI hay que hacer, pero no nombra lo que NO cuenta. ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: el descarte llega entero, con los dos ejemplares nombrados, por el APPEND del paso 2 de objetivos_de_llamada_orientados_a_avance, que es su hermano en este mismo acto | paso 2 de advances_vs_continuations | la fase 04, que redacta y afina los pasos del superviviente |

| pieza del que muere | marca | a donde va |
|---|---|---|
| paso **1** de `analisis_causa_raiz_diagnostico` | `INCISO` | **`INCISO` ADOSADO** al paso 1: *análisis de Pareto para descartar variables no relevantes (ej. turno de trabajo)* |
| paso **2** de `analisis_causa_raiz_diagnostico` | `CUBIERTO` | ya lo dice el **paso 2** del superviviente |
| paso **3** de `analisis_causa_raiz_diagnostico` | `INCISO` | **`INCISO` ADOSADO** al paso 3: *que permita correlacionar cada teoría con el defecto observado* |
| paso **4** de `analisis_causa_raiz_diagnostico` | `INCISO` | **`INCISO` ADOSADO** al paso 4: *estadísticamente cuál teoría explica la mayoría de los casos* |
| paso **5** de `analisis_causa_raiz_diagnostico` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| condicion **1** de `analisis_causa_raiz_diagnostico` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| condicion **2** de `analisis_causa_raiz_diagnostico` | `APPEND` | **viaja ENTERA** al superviviente |
| paso **1** de `analisis_diagnostico_causa` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |
| paso **2** de `analisis_diagnostico_causa` | `INCISO` | **`INCISO` ADOSADO** al paso 2: *usando brainstorming y diagramas causa-efecto* |
| paso **3** de `analisis_diagnostico_causa` | `CUBIERTO` | ya lo dice el **paso 3** del superviviente |
| paso **4** de `analisis_diagnostico_causa` | `CUBIERTO` | ya lo dice el **paso 4** del superviviente |
| condicion **1** de `analisis_diagnostico_causa` | `CUBIERTO` | ya lo dice el **paso 1** del superviviente |

| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |
|---|---:|---:|---:|---:|---:|
| `analisis_causa_raiz_diagnostico` | 5 | 2 | 1 | 3 | 3 |
| `analisis_diagnostico_causa` | 4 | 1 | 0 | 4 | 1 |
| **los 2 juntos** | **9** | **3** | **1** | **7** | **4** |

| plan | acto | especie | que se pierde | donde vive | enrutada a |
|---|---:|---|---|---|---|
| PLAN_V69_OPU02_LOTE_E.json | 30 | DE PARAMETRO DE PASO | LA PARADA EXPLICITA ANTES DEL REMEDIO: confirmar la causa raiz ANTES de disenar el remedio, dicho como orden y no solo como orden de los pasos. Es la frase que el puesto 2838 usa para separar los dos viajes, y el superviviente conserva el ORDEN (su paso 4 establece la causa y su paso 5 disena remedios) pero pierde la PROHIBICION de adelantarse. ATENUANTE DECLARADO: el orden de los ocho pasos del superviviente hace lo mismo de hecho, aunque sin decirlo | paso 5 de analisis_causa_raiz_diagnostico | la fase 04, que redacta y afina los pasos del superviviente |
| PLAN_V69_OPU02_LOTE_E.json | 30 | DE PARAMETRO DE PASO | EL DIAGRAMA CAUSA-EFECTO, el de Ishikawa, que es la perdida que el puesto 2600 nombro por su nombre al declarar aquel par: la herramienta que un dueno sin estadistica puede usar para el mismo paso de generar teorias. ATENUANTE DECLARADO Y MEDIDO: el INCISO al paso 2 de este mismo acto adosa VERBATIM USANDO BRAINSTORMING Y DIAGRAMAS CAUSA-EFECTO, asi que la pieza NO se pierde de hecho; se sella igual porque el sello es del reparto y no del resultado (acta 68, D10), y porque la perdida la nombro una razon publicada y una perdida publicada que desaparece sin decirlo es peor que una sellada de mas | paso 2 de analisis_diagnostico_causa | la fase 04, que redacta y afina los pasos del superviviente |

### e) **EL `ACTO 27`: `DECLARADO Y NO FUNDIDO` POR `P.10`, CON LA `ESTRELLA` ENCIMA**

**Es la forma mas limpia del prefijo y aun asi NO se funde**, que es exactamente lo que `P.10`
existe para hacer: las tres cuentas apuntan al mismo nodo y **`P.10` detiene ANTES**.

**Y ES LA MISMA FORMA DEL `ACTO 24` DE LA VUELTA 68** (registrado en la linea
**5396**): **el nodo puente que `P.10` detecta ES el centro de una figura
declarada del inventario**, y una fusion entera deprecaria a la vez el centro y sus perifericos.

| | |
|---|---|
| **acto** | **27** del `orden_universo` |
| **MOTIVO SELLADO DEL CIERRE** | **`P.10`**, con su triangulo MEDIDO (el carril registrado en la linea **3744**), **mas el ejemplar de la figura `ESTRELLA (9.23)` que una fusion entera borraria**, que es la misma forma del `acto 24` de la vuelta 68 |
| **miembros** | **4**, y **NINGUNO se toca** |
| **combinaciones internas** | 6 |
| **pares `A` internos** | 3 |
| **pares `D` internos** | **1**, leidos y declarados DISTINTOS |
| **pares sin veredicto escrito** | 2 |
| **NODOS PUENTE** | **1** |
| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **1** |
| **PUERTAS dentro del acto** | **NINGUNA**, la guarda `1B` pasa por vacio y se dice |
| **puestos de los `D` internos** | **572** |
| **duenos medidos hoy en el fichero del tramo** | **NINGUNO**, los dos campos vacios |
| **figura del inventario de la que es ejemplar** | **ESTRELLA (9.23), ejemplar 4, la fase de diseno**, y su centro es el MISMO nodo puente que `P.10` detecto |
| **instrumento** | [`../loop/SALIDA_V69_PUENTES_TRAMO.txt`](../loop/SALIDA_V69_PUENTES_TRAMO.txt) |
| **dossier `P.5`** | [`../loop/SALIDA_V69_DOSSIER_LOTE_E.txt`](../loop/SALIDA_V69_DOSSIER_LOTE_E.txt) |

> **LA LECTURA QUE UNA FUSION ENTERA DESMENTIRIA:** el **572** se titula *EL HIJO CON CASA PROPIA* y
> dice que `prototipado_modelos_negocio` **desarrolla el paso 5** de `proceso_ideacion_modelo_negocio`
> y le anade lo suyo entero, mientras **la madre se queda con lo suyo**. **Fundir los cuatro a un
> vivo unico deprecaria los dos extremos de ese `D` contra el mismo superviviente y sellaria que
> repiten entre si**, que es lo que esa lectura niega, y ademas es **una cadena de TRES PISOS** que el
> propio **572** cuenta al cerrar. **Los radios de la estrella son los puestos 507 y 641**, y el
> cuarto miembro, de otro libro, entra por el **1056**.

**El acto queda VIVO Y ENTERO. Su destino comparte carril con el pendiente del subconjunto cerrado:
el cierre de la fase 03.**

### f) **LAS GUARDAS DE LA OPERACION, LEIDAS DE LAS SALIDAS Y NO AFIRMADAS**

| guarda | resultado, extraido por aguja de su salida |
|---|---|
| **guardas 1, 1B, 2 y 3** | **VERDES en las CINCO fusiones**: miembros vivos y nomina completa, ningun absorbido es puerta, cobertura exacta de indices y cero repetidos literales |
| **`P.16`, quien fabrica limpia en el mismo commit** | **5** duplicadas fabricadas y limpiadas en la misma corrida; **1** auto-arista retirada; el pasivo propio de la guarda baja de **890** a **889** |
| **guarda A** (cero auto-aristas nuevas) y **guarda B** (cero duplicadas nuevas tras resolver) | **las dos `OK`** |
| **guarda C** (los campos que esta operacion NO redacta, intactos) | **25 de 25** |
| **guarda D** (los absorbidos conservan su texto INTACTO) | **`OK` sobre los 13** |
| **redirecciones sobre nodos vivos** | **38** |
| **reanclaje**, corrido **ENTRE** la fusion y `run_phase1` | **NADA QUE RE-ANCLAR**, y se corrio igual, que es lo que la guarda pide |
| **diff independiente de duplicadas**, con la apertura sacada de `git` | **FABRICADOS 0**, **RENOMBRADOS 0**, y **913** grupos pasan a **912** |
| **Gate 0 con su ciclo de TRES** | **`OK`**: **3224** activos y **629** deprecados, alcanzabilidad 100,0 por ciento; **SIN cuarta corrida** |
| **las tres suites** | motor **25/25**, web **80 ficheros y 1030 pasadas**, `tsc` **CERO lineas** |

**LAS PERDIDAS DEL LOTE, CONTADAS POR MAQUINA Y NO DE MEMORIA**, que es la regla que sale de la caida
del `D9` de la vuelta 68 y que esta pagina registro en la linea **5610**:

| | contado sobre el plan sellado |
|---|---:|
| **perdidas selladas en campo propio** | **21** |
| de ellas `DE PARAMETRO DE PASO` | **16** |
| de ellas `DE CONDICIONES` | **5** |
| **filas con `ATENUANTE DECLARADO`** | **14** |
| de ellas, de la **especie del pendiente 4** | **6** |
| de ellas, con **`ATENUANTE DECLARADO Y MEDIDO`** | **4** |
| **filas con DOS SEDES en el campo `donde`** | **1** (el carril de la linea **5114**) |
| la aritmetica de **la lectura contraria** (una fila por SITIO y no por PIEZA) | **22** y no **21** |

### g) **LAS DOS COLISIONES DE CLASE QUE ESTA VUELTA FABRICA, PREDICHAS ANTES DE TOCAR UN NODO Y PUBLICADAS EN ROJO CON SU DUENA**

**Es la pieza mas delicada del lote y por eso va en su propio apartado.** **La fusion del `acto 25`
fabrica DOS colisiones**, y **el carril esta escrito** en la linea **4542**: *la duena
es quien la fabrica*, la colision **nace de una sustitucion de `OP-U-02`, esta predicha en su plan y
se publica en rojo con dueno nombrado**.

| | medido |
|---|---:|
| **linea base declarada y MEDIDA sobre el arbol de antes** | **4** |
| **colisiones NUEVAS que la fusion fabricaria** | **2** |
| colisiones que desaparecerian | 0 |
| **ESPERADAS TRAS FUNDIR** | **6** |
| **MEDIDAS al cierre por el censo** | **6** |
| **`CALZA`** | **`SI`** |
| auto-pares al cierre | **268** |

**LAS DOS, NOMBRADAS UNA A UNA CON SUS PUESTOS PARA QUE EL CENSO SE PUEDA COTEJAR SIN ABRIR OTRO
FICHERO:**

| colision nueva | clases | **de donde sale** |
|---|---|---|
| `cuatro_etapas_llamada_de_ventas` contra `enfoque_etapa_investigacion` | **`B`** contra **`D`** | el **775** dice `B` contra el superviviente; el **202** y el **1364** dicen `D` contra dos absorbidos, y al resolver los tres al mismo vivo las lecturas chocan |
| `enfoque_etapa_investigacion` contra `modelo_spin_preguntas` | **`B`** contra **`D`** | el **648** y el **769** dicen `B`; el **1422** dice `D` contra un absorbido |

> **LAS DOS SON LA MISMA ESPECIE, y se dice porque explica el choque**: **el marco entero contra una
> de sus etapas**. Contra el superviviente la lectura dijo `B` (dos caras del mismo asunto) y contra
> los absorbidos dijo `D` (el todo no repite la parte). **La fusion junta las tres lecturas en un
> solo par y el choque se vuelve visible.**
>
> **LA LINEA BASE OPERATIVA DEL CENSO PASA DE 4 A 6**, y **eso NO se adjudica
> aqui**: la base vigente esta escrita en la linea **4542**, la anterior se movio por
> adjudicacion del auditor, y esta se le sube **COMO PREGUNTA** en el reporte de esta vuelta. **Las
> dos de la mesa `OP-M-03` no se tocan y las dos viejas de `OP-U-02` siguen vigentes con su duena.**

### h) **LO QUE QUEDA DEL TRAMO AL CIERRE DE ESTE LOTE, MEDIDO Y NO ARRASTRADO**

| | |
|---|---:|
| actos del tramo unico | **47** |
| cerrados por los lotes `A` a `D` | **20** |
| **cerrados por el lote `E`** | **6** (5 fundidos, 1 declarado) |
| **quedan** | **21 actos** |
| **nodos que quedan** | **63** |
| **el siguiente del prefijo** | el acto **31**, **con dueno** |
| de los que quedan, **con nodo puente** | **0** |
| de los que quedan, **con par `D` interno** | **0** |
| de los que quedan, **con dueno medido** | **2** |
| **actos declarados que esperan el cierre de la fase 03** | **14** |
| actos (componentes) al cierre | **67** |
| actos `ABIERTOS` al cierre | **41** sobre **181** nodos |

> **UN HECHO MEDIDO QUE CAMBIA LO QUE VIENE:** **de los 21 actos que quedan, NINGUNO
> trae nodo puente y NINGUNO trae par `D` interno**. **Todos los actos con puente del tramo estan ya
> cerrados**, y con ellos el motivo sellado de `P.10` (linea **3744**) y el cuarto
> motivo (linea **5121**) **se quedan sin sujeto en lo que resta del tramo**. Lo que
> queda son actos de tres miembros con dos pares `A` leidos y uno sin veredicto.

### i) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba**, **NO deshace ninguna fusion**, **NO re-lee ni un veredicto
de las colisiones vigentes**, **NO adjudica la linea base nueva del censo** (la sube como pregunta),
**NO funde ningun acto con dueno** (el **31** y el resto siguen fuera), **NO toca la mesa
`OP-M-03` ni sus dos colisiones**, **NO ejecuta ninguna de las cinco fichas `OP-M-02` consumidas** y
**NO abre el lote siguiente**. La respuesta *DOS FAMILIAS* de `P.5` sigue siendo motivo sellado en la
linea **4518** y **en este lote no se uso: los seis actos contestaron UNA familia**. El
dueno se sigue midiendo como el acta 68 lo adjudico, en la linea **5687**, y las
adjudicaciones de esa acta estan registradas desde la linea **5572**.


---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 69, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (26 ago 2026, vuelta 70, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **DIEZ** veces, **y la cifra va con su medicion del dia al lado en vez
de heredada**: **OCHO** llevan esta misma cabecera de nivel dos (de la del acta 61 a la del acta 68,
contadas hoy por maquina sobre el fichero) y **DOS** son las mas viejas, que la pagina adoso con
cabecera de nivel tres (la del acta 52 en la linea **1250** y la del acta 57 sobre el
`acto 25` en la **2475**). **La ultima de las diez es la del acta 68 en la linea
**5572** y la anterior la del acta 67 en la **5031**, las cuatro cotejadas HOY
abriendo el fichero.** **Ninguna cifra publicada de arriba se toca.**

**NINGUNA CITA DE LINEA DE ESTA SECCION ESTA TECLEADA:** cada una es una marca que el registrador
sustituye por el numero que le devuelve **buscar su aguja de contenido** en el fichero, y **antes de
escribir una sola letra el instrumento vuelve a barrer el texto ya sustituido y exige que TODO numero
de linea que aparezca en el salga de una aguja**; si uno solo no sale, cae en `ROJO` y **no escribe
nada**.

**El acta de la vuelta 69 abre en la linea **18654** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md)**, su verificacion por corrida propia en la
**18667**, su relectura ciega en la **18779**, sus caidas en la **18805**,
sus catorce adjudicaciones de discutibles en la **18825**, sus cuatro adjudicaciones nuevas
en la **18879**, su metrica de credito en la **18917** y sus condiciones de parada
en la **18946**.

### a) **LA TANDA 69 QUEDO LIMPIA ENTERA, Y ESO SE REGISTRA CON EL MISMO CUIDADO CON EL QUE SE REGISTRA UNA CAIDA**

**Una tanda limpia que solo vive en un acta se olvida igual que una caida que solo vive en un acta**,
y por eso entra aqui con su medicion al lado y no como un elogio.

| | lo que el acta 69 mide, copiado de su linea | linea |
|---|---|---:|
| **caidas del ejecutor: de CLASE, de CIFRA PUBLICADA y de REPORTE** | **CERO, CERO y CERO**; **toda cifra del reporte que el auditor toco calzo al digito con su corrida** | **18807** |
| **el contador de parada** | **SIGUE EN CERO**, con **dos tandas limpias seguidas** (la 68 y la 69) | **18942** |
| **la racha de reporte** | **VUELVE A CERO**: la caida del `D9` de la vuelta 68 **quedo en UNA** | **18942** |
| **la regla que salio de aquella caida, estrenada y funcionando** | la cuenta agregada **por maquina** con **la exclusion DICHA**: el auditor reconto las 21 filas del plan sellado **fila a fila** y **leyo entera la fila 5**, que describe el mecanismo del pendiente 4 en su prosa y **NO lleva la frase sellada**; la cuenta buena es **14** | **18730** |
| **el acumulado del credito** | **469 relecturas**, **799 puestos**, 7 caidas de clase, 28 de reporte del ejecutor, 14 de cifra publicada del ejecutor, 3 de cifra del auditor, 7 de acta del auditor y 4 de procedimiento del auditor | **18937** |
| **las caidas del auditor** | **CERO**, con **TRES manejos propios declarados** y sin cifra publicada de por medio | **18811** |

> **LO QUE LA REGLA NUEVA VALE PARA TODO LOTE, y por eso se copia aqui en vez de dejarla en el
> acta:** **la cuenta agregada se cuenta por maquina en la corrida de la vuelta**, y **si una fila
> queda fuera de la cuenta, la frase lo DICE**. **El lote `F` de esta misma vuelta la aplica igual.**

### b) **LA RELECTURA CIEGA: 5 DE 5 COINCIDEN, CON SUS PUESTOS, MAS LOS DOS SUPERVIVIENTES ADJUDICADOS CIEGOS**

**El auditor leyo PRIMERO los pasos de los nodos en su texto PRE fusion** (por `git show` sobre el
commit de la `TAREA 1` de la vuelta 69), **adjudico su clase, y SOLO DESPUES destapo la razon
escrita.** **Es la mitad del procedimiento que hace creible el resultado**, y por eso los cinco
puestos van nombrados uno a uno.

| puesto | lo que el auditor adjudico ciego | linea |
|---:|---|---:|
| **2838** | `A` **por contencion** con superviviente `viaje_diagnostico_remedial`, **y hasta el mismo residuo**: la lectura contraria del Pareto y la validacion estadistica es defendible. **La razon escrita dice eso mismo** | **18785** |
| **839** | `A`, **el mismo instrumento entero con parametros propios a cada lado**. Escrita `A` | **18789** |
| **775** | `B`, **el marco entero contra una regla de enfasis sobre una de sus etapas**. Escrita `B` | **18792** |
| **220** y **482** | `A` y `A`, **repeticion del gesto de Rackham**; en el segundo el marco anade la taxonomia completa. Escritas `A` y `A` | **18794** |
| **los dos supervivientes, ademas** | `marco_avances_continuaciones` en el `acto 29` y `viaje_diagnostico_remedial` en el `acto 30`, **elegidos ciegos y COINCIDENTES con lo ejecutado** | **18798** |
| **el saldo** | **CERO discrepancias y CERO fuera del marcado**: el credito de la tanda **queda entero** y **no hay tramo al doble** | **18802** |

### c) **LOS CATORCE DISCUTIBLES, ADJUDICADOS: LOS CATORCE `A FAVOR`, CON SU VARA**

**La cifra de cabecera y el detalle coinciden**: **catorce marcados, catorce adjudicados, cero sin
contestar**, y **ninguna discrepancia fuera de la lista**.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | la fusion del `acto 25` fabrica **dos colisiones de clase** | **`A FAVOR`**: predichas **antes de tocar un nodo**, selladas, publicadas en rojo con su duena y **CALZAN al digito** en la re-simulacion del auditor; **ninguna letra manda deshacer una fusion por una colision predicha** | **18827** |
| **`D2`** | la puerta del `acto 26` a nueve pasos | **`A FAVOR`** por el carril del `D8` del acta 67 y del `D4` del acta 68; **la redaccion de un nodo de nueve pasos es asunto de la fase 04** | **18833** |
| **`D3`** | cuatro `INCISO` en el `acto 30` | **`A FAVOR`**: **ninguno apilado**, pasos receptores **sin punto final**, resultantes **impresos y leidos** por el auditor | **18837** |
| **`D4`** | el racimo del `acto 29` tocado a medias | **`A FAVOR`**: **la particion 3 mas 2 esta MEDIDA** y la fusion opera **sobre los dos sueltos** | **18840** |
| **`D5`** | el **2838** con discutible fuerte de su propio autor | **`A FAVOR`**: la ciega independiente dio **la misma clase y el mismo superviviente**, y el reparto conserva por `INCISO` lo que haria valer la lectura contraria | **18843** |
| **`D6`** | una sola vara con margen 2 contra 1 | **`A FAVOR`**: **donde el contenido dice algo el contenido manda**, y la eleccion ciega cayo en el mismo superviviente **por la misma vara** | **18847** |
| **`D7`** | el tope del lote lo eligio un acto con dueno | **`A FAVOR`**: el contrato es **entregar lo declarado**, y **saltarse el 31 romperia el prefijo** | **18850** |
| **`D8`** | la fila de figura en `tabla_declarado` sin encargo | **`A FAVOR`** con las condiciones del acta 61 cumplidas, **y la advertencia del propio ejecutor atendida**: la tabla **queda CONGELADA** | **18854** |
| **`D9`** | cuatro perdidas con `ATENUANTE DECLARADO Y MEDIDO` | **`A FAVOR`** por el carril del `D10` del acta 68 (**el sello es del reparto y no del resultado**), **con la cuenta por maquina al lado para restarlas** | **18857** |
| **`D10`** | la fila 5 sin la frase sellada, **14** y no **15** | **`A FAVOR`**: la cuenta por maquina **mide la frase sellada** y **la exclusion va DICHA**; **un plan ejecutado no se re-sella** | **18860** |
| **`D11`** | el plan sellado dos veces | **`A FAVOR`**, el mismo carril del `D15` de la vuelta 68; **el diff es UNA linea y el auditor lo corrio** | **18864** |
| **`D12`** | los nexos de los `INCISO` son cosecha propia | **`A FAVOR`**: **el trozo es verbatim** (comprobado por el auditor) y **el nexo minimo evita pasos ilegibles** | **18866** |
| **`D13`** | ocho perdidas en el `acto 26` | **`A FAVOR`**: el **839** sostiene la fusion (**la ciega tambien lo dio `A`**) y **las ocho estan selladas con destino** | **18870** |
| **`D14`** | dos puertas crecen el mismo dia | **`A FAVOR`**: **con UNA puerta el acto funde y la puerta sobrevive** (acta 54, pregunta 1), aplicado dos veces con su letra | **18874** |

### d) **ADJUDICACION 1: LA LINEA BASE OPERATIVA DEL CENSO DE COLISIONES PASA DE `4` A `6`, Y LA CORRECCION DECLARADA YA ESTA APLICADA SOBRE EL INSTRUMENTO**

**Es la adjudicacion que MUEVE una cifra, y por eso va primero y con la correccion pegada al lado.**
El carril esta escrito en esta misma pagina, en la linea **4542**: **la duena de una
colision que fabrica una fusion es quien la fabrica**.

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **lo adjudicado** | **la linea base pasa de `4` a `6`** | **18881** |
| **el carril, y no es nuevo** | **el mismo con el que la base paso de 2 a 4** (acta 66, pregunta 2, con la correccion declarada de la vuelta 67) | **18882** |
| **las tres condiciones que una colision cumple para entrar a la base** | **PREDICHA**, **PUBLICADA** y **con DUENA sellada**; **las dos nuevas cumplen las tres** y estan registradas en esta pagina con sus puestos, en la linea **6110** | **18881** |
| **el encargo al ejecutor** | aplicar en `TAREA 1` la **CORRECCION DECLARADA** sobre el defecto de `--base` de `vuelta65_colisiones_esperadas.py` | **18887** |
| **lo que NO se toca, y se dice** | **LA ARITMETICA**: la guarda **sigue midiendo la base sobre el arbol** y **comparando esperadas contra medidas** | **18889** |

> **LA CORRECCION, APLICADA HOY Y DECLARADA COMO LA DE LA VUELTA 67:** el valor por defecto de
> `--base` de `scripts/loop/vuelta65_colisiones_esperadas.py` pasa de `4` a `6`, **con el texto viejo
> entero conservado en el docstring y en el sitio donde muerde, sin tachar nada**, y **con la llamada
> vieja citada verbatim en un comentario encima de la nueva**. **Es el segundo escalon del mismo
> carril**: 2 por el acta 64, 4 por el acta 66 y 6 por el acta 69. **La guarda no cambia**: si el
> censo de ANTES no mide exactamente la base declarada, el instrumento cae en `ROJO` y dice *la base
> se mide, no se supone*.

### e) **ADJUDICACION 2: EL `ACTO 31` NO ES UNA FUSION DE `OP-U-02`, Y EL PREFIJO DEL LOTE `F` ABRE EN EL `32`**

**Adjudicado por el criterio del propio plan escrito en la ficha de `OP-U-02`**, no por doctrina
nueva.

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **lo adjudicado** | **el `acto 31` NO es una fusion de `OP-U-02` y el prefijo del lote `F` ABRE EN EL `32`** | **18892** |
| **la letra que lo sostiene** | **la ficha de `OP-U-02`** (criterio del propio plan, con correccion declarada de la vuelta 48): **los actos que ya tienen dueno en otra operacion NO se cuentan como fusiones que el recomputo abra** | **18893** |
| **el dueno, MEDIDO** | `OP-F-04-WEI` y `OP-S-04`, **y ademas el acto no trae ningun motivo sellado de `DECLARADO`** | **18896** |
| **por que el salto NO rompe el prefijo sin saltos** | **porque el `31` no esta en la cola de fusiones de `OP-U-02`**: su destino queda con sus duenos en sus fases, y **el salto va DECLARADO con esta cita** | **18899** |
| **y lo mismo para el `37`** | **`OP-S-07`**, cuando el prefijo lo alcance | **18901** |

### f) **ADJUDICACION 3: `tabla_declarado` QUEDA CONGELADA, Y NINGUNA TABLA DE REGISTRADOR CRECE SIN ENCARGO**

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **lo que se queda** | **la fila de duenos** (vuelta 68) **y la de figura** (vuelta 69): **las dos entraron con docstring y marcado**, que son las condiciones del acta 61 | **18902** |
| **la regla, desde el acta 69** | **ninguna fila ni columna nueva entra a las tablas de los registradores sin encargo previo del auditor** | **18906** |

> **ESTA SECCION SE ESCRIBE BAJO ESA REGLA Y SE DICE:** el registrador del lote `F` de esta misma
> vuelta **copia la maquina del de la vuelta 69 SIN ANADIRLE NI UNA FILA NI UNA COLUMNA**, y lo unico
> propio son sus agujas, sus anclas y su texto. **Una tabla que crece sola es lo que esta
> adjudicacion viene a parar.**

### g) **ADJUDICACION 4: EL RESTO DEL TRAMO NO TRAE PUENTES NI PARES `D` INTERNOS, ASI QUE `P.10` Y EL CUARTO MOTIVO QUEDAN SIN SUJETO**

**Esta es la adjudicacion que MANDA sobre lo que el lote `F` puede esperar**, y por eso se registra
aunque no encargue trabajo por si sola.

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **lo medido** | **en lo que resta del tramo no hay actos con nodo puente ni con par `D` interno** | **18908** |
| **la medicion del auditor, aparte** | **47 filas, cerrados 26, quedan 21 actos y 63 nodos**, recontados por el | **18753** |
| **cero y cero, recontados sobre el instrumento** | **cero con par `D` interno** (sobre `clases_internas`) y **cero con nodo puente** (instrumento re-corrido sobre los 21) | **18754** |
| **que queda sin sujeto** | **`P.10`** (el triangulo, linea **3744**) y **el cuarto motivo** (el `D` directo interno, linea **5121**) | **18908** |
| **de donde saldran los cierres `DECLARADO` que vengan** | **de la guarda `1B` con DOS o mas puertas** (linea **4023**), **de la respuesta *DOS FAMILIAS* de `P.5`** (linea **4518**) **o del transito de un `EMPATE SIN VARA`** (linea **5152**) | **18911** |
| **el aviso sobre el ritmo** | **los lotes que vienen seran casi todos fusiones y el ritmo de colisiones puede subir**: **cada una sigue exigiendo prediccion, sello y duena, SIN EXCEPCION POR VOLUMEN** | **18914** |

### h) **LOS PENDIENTES HEREDADOS, NOMBRADOS CON SU DESTINO**

**Se registran porque mandan sobre lo que viene aunque no encarguen trabajo hoy.** **Y se dice como
se midieron**: el acta 69 **no los re-enumera en una lista propia** (medido abriendo el acta hoy: su
seccion 5 trae las cuatro adjudicaciones nuevas, y el pendiente 6 va entre ellas), asi que **su
destino se lee de donde SI esta escrito**: la seccion de los pendientes del acta 68 en esta misma
pagina, linea **5712**, y las lineas del acta 69 que los tocan una a una.

| | lo que queda escrito, con su medicion | destino | linea |
|---|---|---|---:|
| **el subconjunto cerrado de un acto con puente** | ahora son **CATORCE** los actos declarados que esperan, con el `acto 27` de la vuelta 69 sumado (linea **6043**) | **el cierre de la fase 03**, donde la parada de `AUDITOR.md` espera al fundador | **18960** |
| **la marca para *ya lo dice el `APPEND` de un hermano*** | sigue **NOMBRADA** y **su cuenta ya no es anecdotica**: la vuelta 69 la pago **SEIS** veces, y el auditor reconto las filas **una a una** leyendo entera la que no lleva la frase sellada | **la cuenta crece y se publica en cada lote**, con la exclusion DICHA | **18730** |
| **el `INCISO` de condiciones** | sigue sin existir; el acta 69 lo toca en su `D3` y en su `D12`, **con los cuatro `INCISO` del `acto 30` leidos y los nexos comprobados** | **la fase 04** (acta 55, pregunta 5) | **18866** |
| **el esquema de `OPERACIONES.jsonl`** | sigue **pendiente**; el barrido del auditor sobre los 18 miembros del lote `E` devolvio **UNA sola mencion** y **una mencion en el campo `evidencia` NO es dueno** | **sin fecha, y se dice** | **18738** |
| **el cierre de la fase 03** | **NO SE CUMPLE TODAVIA**: quedan **21 actos y 63 nodos**, **dos actos con dueno**, la mesa `OP-M-03` y los catorce declarados | **la parada escrita de `AUDITOR.md`, tal como esta** | **18959** |

**LOS CUATRO MOTIVOS SELLADOS DEL `DECLARADO Y NO FUNDIDO` SIGUEN SIENDO CUATRO Y LA LISTA SIGUE SIN
SER CERRADA**, pero **DOS DE ELLOS SE QUEDAN SIN SUJETO EN LO QUE RESTA DEL TRAMO** por la
adjudicacion 4 del apartado g). **La linea base del censo de colisiones YA NO ES `4`: es `6`**, por
la adjudicacion 1 del apartado d), y **el sitio donde la pagina la habia dejado en `4` no se
reescribe**: queda donde estaba, en la linea **4542**, y **esta seccion es la
correccion declarada encima**.

### i) **LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya**

**NO toca ni una cifra publicada arriba**, **NO funde ni deshace nada**, **NO elige ningun
superviviente**, **NO re-lee ni un veredicto de las seis colisiones vigentes**, **NO toca la mesa
`OP-M-03`**, **NO toca ninguna ficha de `OP-U-02` ni de `OPERACIONES.jsonl`**, **NO anade ni una fila
ni una columna a ninguna tabla de registrador** (adjudicacion 3) y **NO abre el lote `F`**:
**registra adjudicaciones y declara una correccion**. El lote `F` es la `TAREA 2` de esta misma
vuelta y se registra en su propia seccion, debajo de esta. **El registro del lote `E` de la vuelta 69
queda intacto donde esta**, en la linea **5742**, **con su cierre de tramo medido en la
6145**.
