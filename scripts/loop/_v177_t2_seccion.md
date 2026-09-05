### TAREA 2. `OP-L-03`, DESAPLAZADA DESPUES DE SIETE VUELTAS

#### 2.a. LA FICHA, LEIDA ENTERA ANTES DE TOCAR NADA

`docs/plan/OPERACIONES.jsonl` **linea 43**, `OP-L-03`, fase
`09_LECTURAS_DIRIGIDAS`, tipo **MESA**, estado `LISTA`, `fecha_corte`
**2026-08-11**, con sus **4** clausulas de `verificacion`, su `adjudicacion` y su
`nota`. Mas `docs/plan/LECTURAS_DIRIGIDAS.md` (**2230** lineas).

**Y LA FICHA CONTRADICE AL ENCARGO EN SU PROPIO CUERPO, ASI QUE LO DIGO ANTES DE
EMPEZAR.** El encargo dice *"El universo esta MEDIDO desde el 11 ago 2026: 55
pares en 29 actos, corte puesto 2117"*, y eso es exacto **para la `evidencia` y
la `fecha_corte` de la ficha**. Pero **la `nota` de esa misma ficha declara un
RECOMPUTO POSTERIOR**, al corte **3.388**, **ADJUDICADO EN LA VUELTA 15**: *"EL
BACKLOG QUEDA EN CUARENTA ACTOS Y SETENTA Y TRES PARES, por LECTURA LITERAL de la
regla y no por preferencia"*. **Corrido hoy el instrumento que la propia nota
cita** (`scripts/loop/backlog_l03_vuelta14.py`,
`docs/loop/SALIDA_V177_T2_UNIVERSO.txt`): **40 actos, 73 pares**, con reparto
**24 de tres, 10 de cuatro, 4 de cinco y DOS de seis**.

**DE AHI SALE UNA SEGUNDA DIFERENCIA, Y CAMBIA POR DONDE SE EMPIEZA.** El encargo
manda empezar por `cierre_segun_complejidad_venta`, *"seis miembros, seis pares
por leer de quince, **el mayor del reparto**"*. **En el universo adjudicado NO es
el mayor**: hay **dos** actos de seis, y el otro
(`breakthrough_desempeno_actual...`) tiene **8** pares por leer, no 6. El "mayor"
del encargo es el del corte **2117**. **Sigo el universo adjudicado y no el de la
`evidencia`**, porque `EJECUTOR.md` 2 dice que la cifra la da el instrumento
corrido hoy, y **hago los SEIS actos grandes** (los dos de seis y los cuatro de
cinco) en vez de los cinco que el encargo nombra: es la misma instruccion
(*"LOS ACTOS GRANDES PRIMERO"*) aplicada a lo que hay. **MARCADO COMO
DISCUTIBLE.**

#### 2.b. EL CRITERIO, CITADO Y NO PARAFRASEADO (`P.5`, banco 9.5.0)

La clausula de la ficha, **verbatim**: *"cada acto que vaya a fundirse **SE LEE
ENTERO** despues de su destejido y antes de su fusion"*. **La lectura es del
ACTO, no de la pareja**, y el motivo es la regla de **FAMILIA DECLARADA** del
informe intra-dominio: **una familia juzgada de a pares da incoherencia, porque
la pregunta no es de pares**. Una decision por acto.

#### 2.c. EL HALLAZGO QUE CAMBIA LA TAREA: LA MITAD DEL TRAMO YA NO EXISTE

**TRES DE LOS SEIS ACTOS GRANDES NO TIENEN NADA QUE LEER, Y NO PORQUE SE HAYAN
LEIDO: PORQUE SE FUNDIERON.** Sus miembros escritos son **hoy un solo nodo**, asi
que sus pares no estan pendientes, **estan disueltos**.

**VERIFICADO POR DOS CAMINOS INDEPENDIENTES QUE DAN LO MISMO**, que es lo que
`EJECUTOR.md` 9 manda (*"toda perdida de catalogo declarada se re-verifica contra
el grafo"*): el **resolutor de `P.1`** sobre `ids_alias`, y el campo
**`deprecado` del `master_graph.json`**.

| acto | miembros | vivos (resolutor) | vivos (grafo) | pares que el instrumento da por leer | **pares reales** |
|---|---:|---:|---:|---:|---:|
| `breakthrough_desempeno_actual...` | 6 | **1** | **1** | 8 | **0** |
| `cierre_segun_complejidad_venta...` | 6 | **1** | **1** | 6 | **0** |
| `cash_burn_calculation...` | 5 | 5 | 5 | 4 | **4** |
| `construccion_de_leverage...` | 5 | 5 | 5 | 3 | **3** |
| `encuadre_desafio_diseno...` | 5 | **1** | **1** | 6 | **0** |
| `estrategia_de_innovacion_arenas...` | 5 | **4** | **4** | 2 | **2** |
| **TOTAL** | | | | **29** | **9** |

**LOS DOS CAMINOS CALZAN EN LOS SEIS ACTOS.** Y el acto por el que el encargo me
manda empezar, `cierre_segun_complejidad_venta`, **es uno de los tres disueltos**:
sus seis miembros son hoy un solo nodo vivo, que lleva su mismo nombre.

**QUE SIGNIFICA, DICHO SIN ADORNO:** el backlog de `OP-L-03` **esta medido sobre
el archivo de componentes del corte 3.388 y la campana ha fundido nodos desde
entonces**, asi que **cuenta como pendientes pares que ya no existen**. En el
tramo grande, **de 29 pares solo 9 son reales: sobran 20**. No extrapolo al resto
del backlog porque no lo he medido, y **decir cuanto sobra en los 34 actos que no
mire seria adivinar**.

#### 2.d. LAS LECTURAS, EN JSONL Y NO EN PROSA (letra (d))

`docs/plan/OP_L_03_LECTURAS.jsonl`, **6 filas, 24.158 bytes**, releido del disco y
**calza byte a byte con lo escrito**. Cada fila lleva el acto, los miembros con su
fuente, los nodos vivos por los dos caminos, los pares en sus **tres** cajones,
la **forma** del acto, **si esa forma cambia** respecto de lo que el par decia por
separado, y la **cobertura** al lado (banco 9.26, cuarta clausula de la ficha).

| cuenta de la tarea, sumada de las filas | |
|---|---:|
| actos del tramo | **6** |
| actos LEIDOS | **3** |
| actos sin nada que leer (ya fundidos) | **3** |
| pares que el instrumento daba por leer | **29** |
| **pares por leer reales** | **9** |
| **pares LEIDOS en esta vuelta** | **9** |
| pares del tramo sin lectura | **0** |
| reparto de clases de lo leido | **A 3, D 6** |
| actos donde la forma **CAMBIA** respecto del par | **3 de 3** |
| **veredictos movidos** | **0** |

**LAS TRES FORMAS, EN UNA LINEA CADA UNA** (enteras en el JSONL):

- **`cash_burn_calculation`**: **una familia y un vecino, no una familia de
  cinco.** La familia es el modelo financiero del fin de la validacion, y **la
  nombra la razon del puesto 404**, no yo. `cash_burn_calculation` no es un
  hermano: **es el paso de caja que los otros tres llevan dentro** (paso 4 de
  metrics, 5 de validar, 6 de verificar). `validacion_hipotesis_ingresos` es
  vecino: **sale por otra puerta**, el LTV.
- **`construccion_de_leverage`**: **una familia pura de cuatro y una tecnica que
  no es de la familia.** El puro de cuatro lo declara la razon del puesto 1030.
  `tecnica_anclaje_negociacion` es **el anclaje**, tecnica de mesa, no maniobra de
  calendario.
- **`estrategia_de_innovacion_arenas`**: **la madre y sus piezas**, y la vara **ya
  esta escrita en el propio acto**: es la de la **correccion declarada del 13 ago
  2026** (puestos 530 y 863), *"LA MADRE Y SU PIEZA DE ARENAS, y la vara las
  separa"*. Lo que hago es aplicarla al acto entero en vez de a un par.

#### 2.e. NINGUN VEREDICTO SE MOVIO, Y ESTA COMPROBADO Y NO PROMETIDO

**`veredictos_movidos: 0` en las seis filas.** Y el sha256 de los dos ficheros que
podrian haberse movido, tomado **antes y despues** de correr el registrador:

| fichero | antes | despues |
|---|---|---|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | `ea6e850d331d14f0` | **`ea6e850d331d14f0`** |
| `docs/plan/OPERACIONES.jsonl` | `bbdde43a00bdc35c` | **`bbdde43a00bdc35c`** |

`git diff --numstat -- dataset/ docs/plan/` da **0 filas**, y lo unico nuevo en
`docs/plan/` es mi registro. **El marcador no se toco: sigue en 3.388.**

**Y LA LECTURA NO ME OBLIGO A MOVER NINGUNO**, que es distinto de que me haya
callado. Relei entera la razon del puesto **1374** antes de decidir y **se
sostiene sola**. Los puestos **530 y 863** son ya una **correccion declarada
encargada por el auditor**, y mover encima de una correccion declarada sin que
nadie me lo encargue **seria legislar**.

#### 2.f. LO QUE LA LECTURA POR ACTO VE Y LA DE A PARES NO PUEDE VER

**LAS TRES FORMAS DEJAN TRIANGULOS `A` MAS `A` MAS `D` MEDIDOS**, que por **`P.10`
BLOQUEAN LA FUSION** del acto. **No los fabrico: salen de cruzar mi lectura con
los veredictos que ya estaban**, y son la razon entera por la que `P.5` manda leer
el acto y no la pareja.

| acto | el triangulo | de donde sale cada lado |
|---|---|---|
| `cash_burn_calculation` | **1** | `cash_burn`+`verificar` **A** (mi lectura), `verificar`+`validacion_hipotesis` **A** (puesto 451), `cash_burn`+`validacion_hipotesis` **D** (puesto 1374) |
| `construccion_de_leverage` | **3** | `anclaje` es **A** con `construccion_de_leverage` (puesto 878) y **D** con los otros tres (mi lectura), que son **A** con `construccion_de_leverage` (puestos 787, 394, 334) |
| `estrategia_de_innovacion_arenas` | **1** | la madre es **A** con `estrategia_de_innovacion_arenas` (puestos 460 y 1121) y **D** con `y_tecnologia` (puestos 530 y 863) y con `seleccion_arenas` (mi lectura) |

**Y HAY UN PATRON EN LOS TRES, QUE ES EL HALLAZGO DE FONDO DE ESTA TAREA:** en los
tres actos, **el par que rompe la coherencia es siempre el mismo tipo de par**, el
que junta **UN NODO ENTERO CON UNA PIEZA DE SI MISMO** y lo llama `A`. La
contencion (`cash_burn` dentro de los tres modelos, el anclaje dentro del paso 4
de `construccion_de_leverage`, la pieza de arenas dentro de la estrategia madre)
**se leyo como repeticion cuando se miro de a dos**. Leida el acto entero, no lo
es. **Lo traigo medido y no lo adjudico yo.**

#### 2.g. LO QUE NO TOQUE, PORQUE LA FICHA Y EL ENCARGO LO PROHIBEN

**Las 55 lecturas marcadas LECTURA DIRIGIDA no entraron en la cola ni movieron su
marcador** (segunda clausula de la `verificacion`): mi registro vive en un fichero
propio, `docs/plan/OP_L_03_LECTURAS.jsonl`, y **no escribe en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**. **`LD-04` y `LD-08` no se releyeron ni se
les acuno numero nuevo** (adjudicacion 4.1 del acta 19): ninguno de los seis actos
del tramo los contiene.

**Y EL `estado` DE LA FICHA NO SE TOCO** (letra (g), decision del fundador del 4
sep 2026): sigue en `LISTA`, y el sha256 de `OPERACIONES.jsonl` de la tabla de
arriba lo prueba. **La vara es `vuelta150_3_relectura_expediente.py` y la corri en
el bloque de apertura**: sigue dando `OP-L-03` en LISTA sin prueba de ejecucion, y
asi se queda. Quien lea despues, que corra la vara.

#### 2.h. LO QUE QUEDA, CON LA CUENTA EXACTA (letra (c))

**El tramo encargado esta ENTERO: 6 de 6 actos grandes, 9 de 9 pares reales.** No
hubo que parar a media tarea.

**Lo que queda de `OP-L-03`: 34 actos** (los 40 del backlog menos los 6 grandes),
con **44 pares** segun el instrumento (73 menos los 29 del tramo). **Ese 44 es la
cifra del instrumento y casi seguro esta inflada por la misma causa que inflaba el
29**, pero **no lo mido aqui y no lo estimo**: los 34 actos son de tres y cuatro
miembros y hay que resolverlos uno a uno. **Van a la 178.**
