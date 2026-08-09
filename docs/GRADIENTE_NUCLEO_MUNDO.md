# LA VARA DEL GRADIENTE: núcleo suficiente, mundo exponencial

Requisito de calidad del fundador: **leída textual en los nodos**, la información
del núcleo debe ser verdaderamente superficial frente a la del mundo específico,
contrastada uno a uno. El núcleo **jamás** más profundo y concreto que el mundo
aplicable, y la diferencia debe **crecer**, no empatarse.

---

## Las dos caras, inseparables

### a) El núcleo es SUFICIENTE

Entrega **la base completa** de cada tema que toca. *"Ya está la base"* tiene que
ser verdad: quien se quede solo con el núcleo tiene algo entero en la mano, no un
teaser.

### b) El mundo es EXPONENCIAL respecto de esa base

Todo nodo de mundo que **comparta tema** con uno del núcleo debe ser
**estrictamente más profundo y concreto** que su base:

- pasos más específicos,
- entregable más avanzado,
- supuestos que **ya asumen la base hecha**.

### c) PROHIBIDO el arreglo por empobrecimiento

Una violación **nunca** se corrige recortando el núcleo hasta dejarlo mudo.

**El arreglo por defecto es profundizar el nodo del mundo**, o reencuadrar el del
núcleo hacia su versión de base. **El núcleo es la puerta de entrada gratuita y
no se degrada.**

### d) La profundidad se adjudica por LECTURA TEXTUAL

De `pasos_accionables` y `entregable_esperado`. **Jamás por conteos ni por
largos.** Los conteos solo ordenan la cola de lectura.

### e) Vigencia

Aplica como **deuda a medir** sobre los nueve mundos existentes, y como **REGLA
DE NACIMIENTO** para todo mundo futuro, **empezando por el 11**.

---

## Cómo se instrumenta

`scripts/gradiente_pares.py` **empareja, no juzga**: encuentra pares candidato
(nodo de mundo, nodo base del núcleo) por dos señales independientes y los pone
en cola. **Un par en la cola es una cita para leer, no una violación.** El
veredicto de cada par es lectura textual del auditor con visto del fundador.

La regla de nacimiento vive además donde se mina: `docs/SOP_EXTRACCION_PACKS.md`,
en las reglas de extracción.
