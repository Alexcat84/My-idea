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

---

# QUE SIGNIFICA PROFUNDIZAR: tres vias, por orden de costo

## Via 1, REENCUADRE

La profundidad **ya existe** en la escalera del propio mundo, y el peldano de
entrada repitio la base del nucleo en vez de asumirla hecha.

**Arreglo**: reescribir ese peldano para que sus pasos **empiecen donde los del
nucleo terminan**. Cero fuentes nuevas, cero nodos nuevos.

**Evidencia de que esta via suele alcanzar**, tomada del par violado del lote 1:
`la_matriz_de_colores_te_engana` **ya supera al nucleo** con estimaciones en
dinero y tiempo y rangos declarados (*"probabilidad y cuanto en dinero o
tiempo"*, *"cuando digas probabilidad media, aclara que rango quieres decir"*).
**La profundidad existe en la escalera; lo que fallo fue el peldano de entrada.**

> **Precision verificada contra el grafo antes de escribirla**: ese nodo es
> **sucesor DIRECTO** de `cuan_probable_y_cuanto_doleria`, que lo declara en sus
> `nodos_previos`. Es **un peldano, no dos**. El argumento se sostiene entero y
> de hecho se refuerza: la profundidad estaba a un solo paso.

## Via 2, RE-MINADO

La extraccion original se quedo en la superficie del capitulo. Se vuelve al
**texto real de la seccion fuente** (regla 8 del SOP) y se destila el nivel
siguiente. **Cuesta lectura, no bibliografia.**

## Via 3, LITERATURA NUEVA

**Solo con la fuente genuinamente exprimida**, y pasa por adjudicacion de
bibliografia con visto del fundador. **Es la excepcion.**

---

# EL TECHO DE LA PROFUNDIDAD: tres paredes

**a) LA FUENTE.** Jamas se inventa profundidad que el libro no da.

**b) LA VALVULA.** Los pasos siguen siendo **hacibles esta semana** por el lector
del taller. Donde la accion del emprendedor se detiene, el nodo dice *"esto
existe y a esta escala no lo necesitas todavia"*, y ahi termina.

**c) LA VOZ.** Profundo **no es tecnico ni corporativo**: se le pide al lector
**mas precision, no mas empresa**.

> **EXPONENCIAL significa relativo a la base del nucleo, no enciclopedico.**

---

# PROHIBICION COMPLEMENTARIA DEL EMPOBRECIMIENTO: tampoco se DESPLAZA

**Desplazar nodos base del nucleo hacia los mundos tambien queda prohibido como
arreglo.** Deja al **plan gratuito cojo** en ese tema (*"ya esta la base"* se
vuelve mentira) y **serrucha puntos de anclaje de la ley del ancla**, cuyos
puentes anclan **siempre** en el nucleo.

**Los pares nucleo-mundo no son duplicados: son el mismo tema a dos alturas, que
es el diseno querido.**

> **El defecto de una violacion no es que existan dos nodos: es que el de pago
> quedo a la altura del gratis.**

---

# LA PROHIBICION PROTEGE LA BASE, NO EL EXCESO

**Decision del fundador (ago 2026), nacida de la clase VIOLACION INVERTIDA.**

Cuando el nucleo **profundiza de mas**, el arreglo tiene **DOS MITADES
INSEPARABLES**:

1. **El nodo del nucleo baja a BASE SOLIDA**: suficiente, **jamas mudo**.
2. **El EXCESO no se tira: se TRASPLANTA al mundo aplicable y lo robustece.**

**Desplazar el nodo base sigue prohibido. Trasplantar el exceso es el arreglo.**
No son la misma operacion y conviene no confundirlas: la primera deja al plan
gratuito cojo en un tema; la segunda le devuelve al plan gratuito su base honesta
y le da al de pago la profundidad que el nucleo estaba reteniendo de mas.

> **Un reencuadre a base que borre el exceso sin darle destino en el mundo es un
> arreglo A MEDIAS, y se rechaza.**

**Consecuencia practica para quien ejecute**: el plan de la cirugia **no esta
completo** hasta que cada pieza del exceso tenga escrito **a que peldano del
mundo va y como**. Si alguna pieza **no tiene peldano donde vivir**, eso se
**declara**, y crear el nodo que falte es **adjudicacion aparte**, no un tramite
de la cirugia.

---

# LA FUENTE DE UN NODO FUSIONADO O TRASPLANTADO

## 1. En FUSION, el mecanismo actual es correcto y NO se cambia

- **El sobreviviente conserva su campo `fuente`.**
- **Cada absorbido queda en `merged_originals`** con su **id**, su **titulo** y
  **SU fuente**.
- **El archivo deprecado conserva la suya.**

> **Nada se pierde.** Verificado: los **314 deprecados** del catalogo conservan
> su campo `fuente`, sin excepcion.

## 2. LA REGLA DE LECTURA, que faltaba

> **La fuente completa de un nodo es la UNION de su campo `fuente` mas las
> fuentes de sus `merged_originals`.**

**Cualquier superficie que muestre fuentes al usuario deriva esa union.** Leer
solo la portada **subdeclara la autoria**.

**Medido sobre el catalogo:**

| | |
|---|---:|
| activos con absorciones | **264** |
| de esos, con **fuentes mezcladas** | **41** |

**El ejemplar**: `costo_de_mala_calidad_copq` lleva contenido de **Juran, Deming
y Crosby**, con **portada de Juran**. Diecinueve absorbidos, y su union de
fuentes son tres libros distintos. **Mostrar solo la portada le quita el credito
a dos autores.**

## 3. NO se reescriben las portadas

**Duplicar en el campo `fuente` lo que `merged_originals` ya guarda es crear
divergencia futura**: dos sitios que dicen lo mismo hoy y dejan de decirlo el dia
que alguien actualiza uno.

> **El dato se lee, no se copia.**

## 4. En TRASPLANTE, la regla es OBLIGATORIA ANTES de ejecutar

**El trasplante es la operacion nueva de la doctrina de las dos mitades, y no es
una fusion**: **nadie se depreca**, asi que **`merged_originals` no aplica por si
solo**.

> **Todo contenido trasplantado viaja con su fuente, registrada en el nodo
> RECEPTOR con la misma forma del registro de fusion**: de que nodo vino, con que
> fuente.
>
> **Un trasplante sin ese registro NO SE EJECUTA.**

## 5. Nota de higiene, sin tarea

**Parte de los 41 mezclados no son autorias distintas: son variantes de escritura
de la misma cadena.** Verificado:

- **Dekker con y sin punto y coma** (`... - Dekker, Sidney` y `... - Dekker,
  Sidney;`)
- **folletos hermanos** `OSHA3885` y `OSHA3886`
- y algunas mas del mismo tipo: **Berman/Knight** con y sin autores,
  **Osterwalder** con parentesis y con guion, **Blank** en dos ordenes.

> **La normalizacion de cadenas de fuente es FICHA DORMIDA, no urgencia.** Se
> anota para que nadie confunda ruido de puntuacion con coautoria real al leer la
> cifra de 41.
