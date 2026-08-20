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

