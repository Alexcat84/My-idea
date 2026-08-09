# PLAN DE LA CIRUGIA 2: `nucleo/gestion_inventario`

**ESTE DOCUMENTO NO EJECUTA NADA.** Es el plan exacto, y **para** aqui esperando
el visto final del fundador con el auditor. **Ni un nodo tocado al escribirlo.**

**Primera aplicacion de la palanca reservada** (reencuadrar un nodo del NUCLEO a
version base) y **primera aplicacion de la doctrina del exceso**
(`docs/GRADIENTE_NUCLEO_MUNDO.md`): el nucleo baja a base solida **y el exceso se
trasplanta al mundo**, las dos mitades o ninguna.

---

# 1. EL DIAGNOSTICO

De los veredictos **23** y **37** de `docs/GRADIENTE_VEREDICTOS.md`.

## El nodo tiene dos temas pegados

| pasos | tema |
|---|---|
| **1 a 5** | **el DIAGNOSTICO de por que se acumula inventario**: dias de inventario, personalizaciones que ofrece ventas, proliferacion de versiones de ingenieria, tiempos de maquina y cambios de produccion, y no producir por producir |
| **6 a 9** | **la MECANICA de cuanto pedir**: lote optimo entre costo de ordenar y de mantener, inventario de seguridad segun variabilidad, estacionalidad, y puntos de reorden |

## Y pisa a dos mundos

| puesto | nodo del mundo | lo que quedo dicho |
|---:|---|---|
| **23** | `compras/clasifica_tu_inventario` | el nodo del mundo es **correcto y de voz impecable**; el del nucleo tiene **profundidad de curso de operaciones en el plan gratuito** |
| **37** | `quality/inventory_analysis_lean` | el solape es **PARCIAL**: el mundo conserva **flujo de valor** y **estrategico contra desperdicio** como material propio |

> **No es base: es un curso de operaciones en el plan gratuito.**

## Lo que ademas se ve leyendo, y pesa en el arreglo

**Los pasos 2, 3 y 4 asumen departamentos**: *ventas* que ofrece
personalizaciones, *ingenieria* que prolifera versiones, *maquinas* con tiempos de
cambio. Es **voz y valvula**, no solo profundidad, y el reencuadre lo arrastra en
el mismo movimiento.

---

# 2. LA VERSION BASE PROPUESTA

**Solo cambian `resumen_teorico`, `pasos_accionables` y `entregable_esperado`.**
El `node_id`, el titulo, la fuente, la fase, el dominio, las
`condiciones_activacion` y la `etiqueta_arbol` **se conservan**, salvo lo que se
indica.

### `titulo_concepto`

**Se conserva**: *Gestión Eficiente de Inventario*.

### `etiqueta_arbol`

**Se conserva**: *Libera Efectivo de tu Inventario*. **Sigue siendo verdad de la
version base**, que es justo lo que la etiqueta tiene que prometer.

### `resumen_teorico` propuesto

> El inventario es efectivo congelado: dinero tuyo que ya gastaste y que no puedes
> usar para nada mas hasta que ese producto salga. Guardar de menos te deja sin
> que vender; guardar de mas te deja sin caja. Antes de afinar cuanto pedir y cada
> cuanto, necesitas dos cosas simples: saber cuanto tiempo se queda contigo lo que
> compras, y tener claro para que sirve cada cosa que guardas. Con eso puedes
> ponerte una meta y ver si te acercas o te alejas de ella.

### `pasos_accionables` propuestos

> 1. Calcula cuantos dias se queda contigo, en promedio, lo que compras antes de
>    venderlo o usarlo.
> 2. Recorre lo que tienes guardado y anota para que sirve cada cosa: para vender,
>    para producir, para reponer o para cubrirte de un imprevisto.
> 3. Marca lo que lleva meses sin moverse y no sabrias explicar por que sigue ahi.
> 4. Ponte una meta concreta y numerica para el proximo trimestre: menos dias de
>    inventario, o menos dinero guardado en lo que no se mueve.
> 5. Vuelve a medir al cierre del trimestre y compara contra la meta que te
>    pusiste.

### `entregable_esperado` propuesto

> Tus dias de inventario medidos, la lista de lo que guardas con su para que, y
> una meta numerica escrita para el proximo trimestre.

### Por que esta base es SUFICIENTE y no queda muda

Quien se quede solo con el nucleo **sale con algo entero en la mano**: sabe cuanto
inventario tiene en dias, sabe para que sirve cada cosa, sabe que le sobra, tiene
una meta escrita y una fecha para volver a medir. **Eso es un ciclo completo, no
un teaser.**

## RIESGO DE COLISION, medido y traido sin decidirlo

**El encargo pide que la base sea el diagnostico simple mas la clasificacion y la
meta.** Y `compras/clasifica_tu_inventario` es, literalmente, **clasificar y
definir que meta persigues**. **La base podia nacer colisionando con el nodo del
mundo que el veredicto 23 declaro impecable, y crear una violacion nueva el mismo
dia que se cura otra.**

**El borrador de arriba esta escrito para evitarlo por construccion**, y asi queda
el gradiente:

| | el NUCLEO dice | el MUNDO (`clasifica_tu_inventario`) dice |
|---|---|---|
| clasificar | **anota para que sirve cada cosa** (paso 2), en una lista | **separa por funcion en cinco tipos**, y **distingue reserva de seguridad de exceso sin proposito** |
| la meta | **una meta numerica para el trimestre** (paso 4) | **elige entre tres clases de meta**: dias de stock, rotaciones al ano, o nivel de disponibilidad |
| el ritmo | vuelve a medir **al cierre del trimestre** | revisa **cada pocos meses** contra la meta por categoria |

> **El nucleo nombra; el mundo tipifica y elige entre metas.** El gradiente se
> sostiene, pero **es apretado a proposito y conviene que el auditor lo mire**: es
> la primera vez que se redacta una base sabiendo que hay un nodo de mundo a un
> palmo.

---

# 3. EL DESTINO DEL EXCESO, verificado contra el grafo

**Busqueda hecha sobre `compras`, `quality` y `entrega`**, por titulo y por
vecindad de `clasifica_tu_inventario` y de `inventory_analysis_lean`.

## El hallazgo principal: `compras` YA TIENE la escalera entera

| pieza del exceso | paso del nucleo | destino existente | estado |
|---|---|---|---|
| **lote optimo**: equilibrio entre costo de ordenar y costo de mantener | 6 | `compras/calcula_costo_de_mantener_contra_costo_de_reponer` | **YA ESTA, y mas hondo** |
| **inventario de seguridad** segun variabilidad y costo de quiebre | 7 | `compras/define_punto_maximo_de_stock`, paso 4 | **YA ESTA** |
| **puntos de reorden** revisados con datos reales | 9 | `compras/define_punto_maximo_de_stock`, pasos 5 y 6 | **YA ESTA, y mas hondo** |
| **estacionalidad**: acumular inventario estacional o invertir en flexibilidad | 8 | **ninguno** | **SIN CASA** |

### Lo que esto significa, y es mejor noticia de la que el plan esperaba

**Tres de las cuatro piezas no se trasplantan: ya viven en el mundo, y viven
mejor.**

- `calcula_costo_de_mantener_contra_costo_de_reponer` **calcula de verdad** el
  equilibrio (sumar el gasto anual de guardar, sacar el porcentaje sobre el
  inventario promedio, costear cada pedido, comparar pedir poco y seguido contra
  mucho y espaciado). El paso 6 del nucleo **solo lo enuncia**.
- `define_punto_maximo_de_stock` **desarma el calculo en seis pasos** (consumo
  semanal, plazo del proveedor, reserva de trabajo, colchon, punto de reorden,
  revision). Los pasos 7 y 9 del nucleo **solo lo nombran**.

> **Para esas tres piezas, la mitad de "trasplantar el exceso" ya esta hecha por
> el catalogo. Sacarlas del nucleo no destruye nada: destapa lo que el mundo ya
> hacia mejor.** El arreglo se reduce a **bajar el nucleo y tender la arista**.

### La pieza que se queda sin casa: LA ESTACIONALIDAD

**No hay ningun peldano en `compras`, `quality` ni `entrega`** que hable de
decidir entre **acumular inventario estacional** o **invertir en flexibilidad de
produccion**.

> **NO SE PROPONE CREAR EL NODO.** La creacion de nodos es **adjudicacion
> aparte**, y esta cirugia no la abre.
>
> **Las opciones, para que el auditor elija y no para que el ejecutor decida:**
>
> **(a)** La estacionalidad **se queda en la base del nucleo**, en forma simple
> (*"si tu venta sube en ciertas epocas, decide con tiempo si vas a acumular
> antes o a arreglartelas cuando llegue"*). **Cuesta un paso mas y no rompe la
> valvula.**
>
> **(b)** La pieza se **declara deuda abierta** con ficha propia, el nodo baja sin
> ella, y **el arreglo queda a medias hasta que se adjudique el nodo nuevo**.
> **La doctrina dice que un arreglo a medias se rechaza**, asi que esta opcion
> **bloquea la cirugia** hasta esa adjudicacion.
>
> **El borrador del punto 2 NO incluye la estacionalidad**, porque incluirla es
> exactamente la decision que no me toca.

## Lo que NO es destino, y conviene dejarlo dicho

- **`quality/inventory_analysis_lean`** conserva **flujo de valor** y
  **estrategico contra desperdicio**. **No recibe nada** de este trasplante: su
  profundizacion natural es su propio material, y el veredicto 37 ya lo dejo
  escrito.
- **`quality/reduccion_inventario_calidad`** habla de **bajar el inventario en
  proceso mejorando la calidad de lo que entra**. Es **otro angulo**, no un
  peldano de la mecanica de pedido.
- **`compras/traduce_stock_muerto_numeros`** es **el costo del stock muerto**, que
  la base del nucleo apunta en su paso 3 y el mundo desarrolla. **Ya es gradiente
  sano; no se toca.**

---

# 4. LAS ARISTAS: lo que hay y lo que faltaria

**Solo se listan. No se crea ninguna desde este documento.**

## Lo que existe hoy

| arista | estado |
|---|---|
| `gestion_inventario` -> `clasifica_tu_inventario` | **EXISTE**, en `nodos_siguientes`, y el mundo lo declara en sus `nodos_previos`. **Bidireccional y sana** |
| `gestion_inventario` -> `ciclo_de_conversion_de_efectivo`, `milk_run_deliveries` | existen, ajenas a esta cirugia |
| `gestion_inventario` <- seis previos del nucleo | existen, ajenas a esta cirugia |

## Lo que el arreglo necesitaria

| arista que faltaria | por que |
|---|---|
| `gestion_inventario` -> `compras/calcula_costo_de_mantener_contra_costo_de_reponer` | **al bajar el nucleo, el lector que quiera el lote optimo tiene que poder llegar.** Hoy **no hay camino** |
| `gestion_inventario` -> `compras/define_punto_maximo_de_stock` | lo mismo para el punto de reorden y el colchon de seguridad |

> **DATO VERIFICADO QUE PESA MAS QUE LAS DOS ARISTAS**: esos dos nodos de
> `compras` **NO TIENEN NINGUN ANCLA EN EL NUCLEO HOY**. Sus previos y siguientes
> son todos de `compras` (`decide_si_lo_compras_o_lo_haces_tu`,
> `ten_un_checklist_de_clausulas_de_contrato`,
> `plantea_oferta_como_rango_o_cifra_precisa`,
> `lleva_scorecard_desempeno_proveedor`).
>
> **La ley del ancla dice que los puentes anclan siempre en el nucleo.** Estas dos
> aristas **no son un adorno de la cirugia: reparan un hueco de anclaje que ya
> existia**, y `gestion_inventario` es **el ancla natural** de las dos.

**Las dos van en la direccion permitida** (nucleo hacia mundo) y **no acoplan
mundo con mundo**, asi que **no chocan con la ley del ancla**. Aun asi, **crearlas
es parte de la ejecucion y necesita el mismo visto que el resto.**

---

# 5. EL CIERRE OBLIGATORIO DE LA EJECUCION

**Lo mismo que cerro la cirugia 1 (`08988ad`) y la 1b (`1260581`). Sin atajos.**

| paso | que se comprueba |
|---|---|
| **Gate 0 ANTES** | completo y verde antes de tocar nada |
| **la edicion** | solo `resumen_teorico`, `pasos_accionables` y `entregable_esperado` del nodo del nucleo, mas las dos aristas si se aprueban |
| **Gate 0 DESPUES** | completo, incluido **0 activos sin vector** y la alcanzabilidad dirigida al 100% |
| **reindex** | `build_semantic_index_voyage.py` completo, porque el texto cambio |
| **sync** | `sync_assets_web.py`, o el indice y el grafo quedan desfasados |
| **rumbos** | el trinquete, con **los puestos de las anclas ANTES y DESPUES** en `scripts/rumbos/`, como en las dos cirugias anteriores |
| **suites** | motor y web verdes; **el hook las corre y aborta si no** |

## La clausula que la orden de edicion va a necesitar

**El reencuadre QUITA cuatro pasos.** El SYSTEM de la re-voz dice *"los HECHOS: ni
uno nuevo, ni uno menos"* y **gana a la orden del editor** cuando se contradicen:
en la cirugia 1 un peldano volvio **identico a como entro** por esto mismo.

> **La orden tiene que decir, con estas palabras, "QUITAR NO ES INVENTAR".** Sin
> esa autorizacion explicita **el nodo volvera sin cambios y el ejecutor perdera
> la pasada.** La clausula esta documentada en `scripts/revoz_pack.py`, junto al
> argumento `--instruccion` y en su `--help`.

**Y la baranda de cifras seguira armada**: la base propuesta **no introduce ni una
cifra** que no estuviera, ni en digitos ni en palabras.

## EL REGISTRO DE TRASPLANTE, requisito de ejecucion

**Regla 4 de la seccion LA FUENTE DE UN NODO FUSIONADO O TRASPLANTADO de
`docs/GRADIENTE_NUCLEO_MUNDO.md`**, y aqui es obligatoria:

> **Cada pieza del exceso que baje a `compras` lleva su REGISTRO DE TRASPLANTE en
> el nodo RECEPTOR**: de que nodo vino (`gestion_inventario`) y con que fuente
> (*Financial Intelligence for Entrepreneurs | Essentials of Supply Chain
> Management - Michael H. Hugos*), **con la misma forma del registro de fusion**.
>
> **Un trasplante sin ese registro no se ejecuta.**

**Aplica a los dos receptores**:
`compras/calcula_costo_de_mantener_contra_costo_de_reponer` y
`compras/define_punto_maximo_de_stock`.

> **Matiz que la ejecucion tendra que resolver y este plan no decide**: en el
> punto 3 quedo medido que **tres de las cuatro piezas ya viven en `compras`, y
> mas hondo**. Si el trasplante resulta ser **cero texto movido** (el nucleo
> simplemente baja y el mundo ya lo tenia), **hay que decidir si el registro de
> trasplante se escribe igual**. **Mi lectura, no vinculante**: si no viaja
> contenido, no hay autoria que acreditar, y el registro **sobra**; lo que si hace
> falta es **la arista**, que es lo que conecta la base con la profundidad. **Que
> lo fije el auditor antes de ejecutar.**

---

# LO QUE ESTE PLAN NO DECIDE, y espera al fundador con el auditor

1. **La estacionalidad**: opcion (a), un paso simple en la base, u opcion (b),
   deuda abierta que **bloquea** la cirugia. **Es la unica decision que impide
   ejecutar.**
2. **Las dos aristas** del nucleo hacia `compras`: si entran en esta cirugia o van
   por su cuenta.
3. **El borrador del punto 2**, palabra por palabra, incluida la colision
   apretada con `clasifica_tu_inventario`.

**PARADO AQUI. La ejecucion la disparan el fundador y el auditor sobre este
documento.**
