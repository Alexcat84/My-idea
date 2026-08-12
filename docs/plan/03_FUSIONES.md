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
