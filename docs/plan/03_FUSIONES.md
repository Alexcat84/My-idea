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
| `founder_ceo_succession_process`, `identificacion_necesidad_sucesion_ceo`, `sucesion_iniciada_por_fundador` | **EL CONTENIDO NO ALCANZA A ELEGIR Y LA RECETA NO TIENE CARRIL PARA LO QUE LA LECTURA ENCUENTRA** | SE DECLARA POR DOS MOTIVOS Y LOS DOS SE ESCRIBEN, porque cada uno por separado ya bastaria | LA MESA y el PARA_ALEXIS del cierre |
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
