# -*- coding: utf-8 -*-
"""Pega el registro de cierre de OP-D-08 en 02_DESTEJIDOS.md con el bloque de la
salida sellada IMPRESO y no retecleado (EJECUTOR.md regla 1)."""
import io

salida = io.open('docs/loop/SALIDA_V45_CIERRE_OPD08.txt', encoding='utf-8').read().rstrip('\n')

CAB = u"""

## `OP-D-08`: **EL LIENZO DE MODELO DE NEGOCIO, DESTEJIDO SOLO** (19 ago 2026, vuelta 45)

**Va PRIMERA de las tres candidatas y no por el campo `orden`, que dice 8.** El criterio de esta
fase es **CONGELADOS LIBERADOS** (aviso de la vuelta 17, lineas **35** y **36**; titulo de la tabla,
linea **81**), y por ese criterio esta operacion **libera UNO** (el par **784**) y **le tocaria ir
entre `OP-D-03` y `OP-D-04`**, o sea que **estaba atrasada**. Lo adjudico el acta de la vuelta 44
(seccion 4 punto 1, linea **9661**), y **los numeros 8 y 9 son el artefacto declarado de no
renumerar**, escrito en la propia nota de la operacion.

**DESTEJIDO SOLO: un solo nodo, sin fusion acoplada, sin superviviente que elegir y con
`aristas_nuevas` VACIO.** El nodo cambia; **el censo no**, y por eso el ciclo de Gate 0 va de
**TRES** comandos y no de cuatro.

### LA PREGUNTA PENDIENTE, RESUELTA EN LA LECTURA Y NO ADIVINADA

**El acta de la vuelta 44 adjudico que esta operacion es EJECUTABLE SIN DECIDIR NADA NUEVO** (linea
**9672**): su `pregunta_pendiente` es **un condicional con LAS DOS RAMAS YA LEGISLADAS**, y su propio
texto dice que decidirla **exige leer el nodo con el ojo puesto en esa frase**. Esa lectura se hizo
hoy, **de cero y entera** (`scripts/loop/vuelta45_lectura_opd08.py`, sellada en
`docs/loop/SALIDA_V45_OPD08_LECTURA.txt`).

**LA CITA, literal del paso 5 de hoy:** *Completar cada uno de los 9 bloques del canvas **para la
solucion disenada***.

**LA RESOLUCION: ES UN MARCO PROPIO**, y por tanto **material propio del bloque 2 que SE REPARTE
COMO EL RESTO**, no se va con su bloque.

| la prueba | y sale del propio texto del nodo, medido hoy |
|---|---|
| **A FAVOR, y es la que decide** | la **`condicion_activacion` 3** del nodo dice, con sus palabras, *Cuando una **solucion de diseno** necesita convertirse en un modelo de negocio viable*, y la **4** dice *Al pasar de idea a implementacion*. **El nodo YA LEGISLA ese momento como una de sus SIETE puertas**, y la frase del paso 5 **nombra exactamente esa puerta** |
| **LA CONTRAPRUEBA** | **NINGUNA de las otras tres narraciones trae acotacion de momento**: la 1 es una sesion colaborativa generica, la 3 es una sesion de equipo que acepta vacios y la 4 es el recorrido bloque por bloque. **La del paso 5 es la UNICA que dice PARA QUE estado del proyecto se completa el lienzo** |
| **LA VARA, que es de la propia operacion** | *aplicar el lienzo a una solucion ya disenada, **QUE ES UN MOMENTO DISTINTO DEL PROYECTO***. El nodo lo declara distinto por su cuenta, asi que la rama que aplica es la primera |
| **DONDE ATERRIZA, tambien por regla** | su bloque desaparece entero, asi que la pieza **NO TIENE BLOQUE** y por la regla de reparto va **AL SUPERVIVIENTE**. Dentro de el se adosa al **paso 4**, el **unico** cuyo objeto es **PARA QUE SE USA EL LIENZO**, asi que **no le cambia el objeto a nada**, que es la condicion que `OP-D-02` dejo escrita (linea **514**) para adosar en vez de abrir paso nuevo. **El vocabulario del anadido no se inventa: sale de la `condicion_activacion` 3 del propio nodo** |

> **VA COMO DISCUTIBLE MARCADO**, y se marca **antes** de saber si acierta: es la unica pieza del
> reparto que la operacion dejo abierta, y la resuelve una lectura del ejecutor.

### EL PLAN SELLADO Y LA SIMULACION, ANTES DE TOCAR NADA

**Plan en `docs/loop/PLAN_V45_OPD08.json`**, construido **contra el grafo** por
`scripts/loop/vuelta45_plan_opd08.py` (lo unico tecleado son los grupos, su texto y su motivo;
**prefijos, conteos, fuente y cobertura se miden**). **17 pasos a DOCE**, que es **exactamente la
cifra que la nota de la operacion predijo** (*deja **DOCE** portadores de linea, no cinco*).

**Ejecutado con `scripts/loop/vuelta32_podar.py`**, el destejedor de la casa para una costura
interna de fuente unica. **Simulacion previa sobre copia en memoria, verde** (`--simular`, exit 0,
`SALIDA_V45_OPD08_SIM.txt`): **guarda de texto 17 de 17 prefijos calzan**, **cero perdida con 17
origenes cubiertos de 17** (cero huecos, cero repetidos, cero sobrantes), **procedencia completa**
sobre los 12 pasos y **fuente SIN CAMBIO**.

> **DOS CORRECCIONES DECLARADAS DE MI PROPIO CONSTRUCTOR, vistas antes de sellar nada.** Mi primera
> version dejaba el destino 1 **verbatim del paso 1** (lo que habria **perdido** el formato de *un
> canvas por miembro*, que `preservar` manda salvar) y el destino 2 **verbatim del paso 10** (lo que
> habria dejado viva **la tercera copia sobrante de la orden**). Las dos pasaron a llevar remedio y
> la salida vieja no se tapa: el commit del primer acto la deja escrita.

> **Y UNA MARCA DE LA SALIDA QUE PODRIA LEERSE MAL, dicha para que no se lea mal:** los destinos
> **6, 7 y 8** salen rotulados *(con remedio)* y **su texto SI es verbatim**, de los pasos **15**,
> **16** y **17**. La marca compara contra el **primer origen del grupo**, que en esos tres es el
> paso del bloque 2 que viaja con ellos (**7**, **6** y **8**), no el de la columna.

### EL CASO POSITIVO, QUE SE DA LA VUELTA ENTERO

**`scripts/loop/vuelta45_guardas_opd08.py`, corrido con la MISMA invocacion antes y despues**
(`SALIDA_V45_OPD08_CASO_ANTES.txt` contra `SALIDA_V45_OPD08_CASO_DESPUES.txt`). **Un caso positivo
sirve si CAE antes y PASA despues; si pasa las dos veces no estaba midiendo la cirugia.**

| | ANTES | DESPUES |
|---|---|---|
| **A1** una sola orden de completar los nueve bloques (**el recuento que cierra la cirugia**) | **CAE**: son **4** narraciones | **PASA**: **UNA**, y es la enumeracion |
| **A2** el literal *cada uno de los 9 bloques* sin repetir | **CAE**: en los pasos **2 y 5** | **PASA**: **CERO** |
| **A3** el lienzo mandado imprimir una sola vez | **CAE**: en los pasos **1 y 9** | **PASA**: **UNA**, con **sus dos formatos dentro** |
| **A4** cero junturas entre narraciones, **que es la causa que el propio 784 declara** | **CAE**: son **3** | **PASA**: **CERO** |
| | **0 PASAN y 4 CAEN** | **4 PASAN y 0 CAEN** |

**Y LAS NUEVE INVARIANTES EN `OK` LAS DOS VECES**, que es lo que una invariante tiene que hacer:
los **91** vecinos del nodo, las **16.898** entradas de arista del grafo, el ancla del veredicto
**1434** viva (*definir la propuesta de valor para cada segmento*, **el paso intocable, verbatim**),
el ancla del **1136** viva (las notas post-it), las **tres** aristas paso a nodo en las que este nodo
es **hijo**, los **9 de 9** bloques del Canvas nombrados, la linea de coherencia, la fuente y las
**7** condiciones.

> **CORRECCION DECLARADA SOBRE UNA CIFRA DE LA PROPIA OPERACION, y el texto viejo no se reescribe.**
> Su `verificacion` dice *el grafo entero tiene **16.866** entradas de arista antes y tiene que tener
> 16.866 despues*, cifra **del corte de la vuelta 17** (14 ago 2026), **antes de las ocho fusiones de
> `OP-D-06`**. **Medido hoy: son 16.898 antes y 16.898 despues.** Lo que la guarda exige es **CERO
> MOVIMIENTO**, y eso se comprueba con la cifra de **hoy** (regla 2: una nota vieja nunca es fuente de
> una cifra nueva). **La otra cifra de la operacion, los 91 vecinos, CALZA AL DIGITO.**

### EL BLOQUE DE CIERRE, PEGADO ENTERO Y SIN RETECLEAR

**Salida verbatim de `python scripts/loop/vuelta45_cierre_opd08.py`** (solo lectura, exit 0),
sellada en `docs/loop/SALIDA_V45_CIERRE_OPD08.txt`:

```
"""

PIE = u"""```

### LOS NUEVE PUNTOS DE LA `verificacion`, CONTESTADOS UNO POR UNO

| # | el punto, copiado de `OPERACIONES.jsonl` (abreviado) | como quedo, MEDIDO |
|---:|---|---|
| **1** | *CASO POSITIVO: **el par 784 se descongela y se juzga*** | **CUMPLIDO Y ES EL CORAZON DEL ACTO.** El **784** pasa de **`B`** a **`D`** con `scripts/corregir_veredicto.py`, **correccion declarada** y **la razon vieja copiada por maquina y conservada entera**. Su razon **ya no ABRE con marca de congelado**, y **la lista de congelados abiertos del archivo entero baja de DOS a UNO** (queda solo el **1190**) |
| **2** | *y se comprueba que el **analisis cruzado** NO esta en el nodo largo* | **COMPROBADO Y SIGUE SIN ESTAR**, medido palabra por palabra: en los **doce** pasos del destejido **no aparece ni una vez** fortaleza, debilidad, oportunidad, amenaza, SWOT, impacta ni prioriza. **Lo unico que se le parece es el paso 10** (*coherencia entre los bloques*) **y no es lo mismo**: la coherencia pide que los bloques no se contradigan, el analisis cruzado pide rastrear como una **debilidad** de uno se propaga a los otros. **La operacion escribio que si resultara que SI esta, el par cambiaria de clase: NO esta** |
| **3** | *el veredicto **1434** se relee y tiene que seguir dando `D`: su ancla tiene que seguir viva* | **CUMPLIDO**: *definir la propuesta de valor para cada segmento* esta **VERBATIM** en el paso **5** del resultado, sin tocar una palabra. Es el **paso intocable** que la operacion nombra |
| **4** | *el veredicto **1136** se relee: la clausula de las **notas adhesivas** tiene que seguir viva* | **CUMPLIDO**: la clausula del post-it vive en el paso **3** del resultado. **Lo que se le quito fue la orden repetida que arrastraba**, no la clausula |
| **5** | *CERO MOVIMIENTO DE GRAFO: 91 vecinos antes y despues, y las entradas de arista del grafo entero* | **CUMPLIDO Y RE-MEDIDO AL CIERRE**: **91 = 91** (25 previos mas 66 siguientes) y **16.898 = 16.898**. **CERO `ids_alias` creados**, el nodo **sigue vivo**, ningun id se movio. La cifra escrita de 16.866 queda declarada arriba como de otro corte |
| **6** | *las **tres** aristas paso a nodo en las que este nodo es HIJO siguen resolviendo* | **CUMPLIDO**: `tipo_de_mercado_estrategia_competitiva` paso 5, `customer_discovery_overview` paso 1 y `unbundling_business_models` paso 4. Las tres madres **existen, tienen ese paso y siguen citando al nodo**. **No dependen de los pasos de este nodo sino de los de su madre**, que es lo que la simulacion de la vuelta 17 ya habia verificado |
| **7** | *EL RECUENTO QUE CIERRA LA CIRUGIA: **una sola** orden de completar los nueve bloques* | **CUMPLIDO**: **UNA**, la enumeracion. **El literal *cada uno de los 9 bloques* aparece CERO veces** y las **cuatro** narraciones son **una** |
| **8** | *el `entregable_esperado` se relee contra el texto que quede* | **CUMPLIDO Y SIGUE SIENDO CIERTO**. Dice *Lienzo de Modelo de Negocio completo con los **9 bloques definidos y coherentes entre si***: los **nueve** bloques estan nombrados **dentro de la columna que sobrevive** (segmentos, propuesta de valor, canales, relaciones, ingresos, recursos, actividades, asociaciones y costos, **9 de 9**) y la **coherencia** la produce el paso 10 |
| **9** | *GATE 0 verde, y recomputo del cierre transitivo (banco `9.21`)* | **CUMPLIDO LAS DOS VECES**, tras la cirugia y otra vez al cierre: **`GATE 0: OK`** con sus **VEINTE** renglones en `[OK]` y cero rojos, **71** etiquetas, **seis** assets, y las **dos copias del grafo byte iguales** (md5 `92cccd790f239e302b03e4a385d56a85`). **El recomputo sobre las 575 `A` vigentes deja al nodo en componente de UNO**, que es justo lo que la propia guarda pedia comprobar (*si el 784 saliera `A` este nodo dejaria de ser componente de uno*): **salio `D`** |

**EL COMANDO 4 NO CORRE, y se dice por que en vez de callarlo:** la regla es **condicional AL CENSO**
y **el censo no se movio**, cosa que **imprime el propio Gate** (**3.524 activos y 329 deprecados**,
los mismos de la apertura). **Un destejido cambia el grafo pero no el censo.**

### LA RELECTURA DEL 784, CON EL DATO QUE INCOMODA PUBLICADO

**El veredicto nuevo es `D`, con la vara ordinaria** (banco `9.6.1`, la linea o el procedimiento, con
la direccion del `9.6.2`). **Los dos procedimientos son DISJUNTOS**, medido y no impresionado: **cero
vocabulario de SWOT** en los doce pasos del lienzo y **cero acciones de construir el lienzo** en los
cinco del SWOT. **Los entregables no son intercambiables**: uno produce **el lienzo**, el otro produce
**una evaluacion DEL lienzo**. **La prueba de madre e hijo del `9.6.2` falla en los dos sentidos.**
**Lo unico compartido es la enumeracion de los nueve bloques, y en el donante es un PUNTERO** (su paso
1 manda **TOMAR** cada uno de los 9 bloques, no construirlos).

**LA RELACION ES DE ALIMENTACION Y NO DE GEMELOS**, la misma figura que el acta de la vuelta 44
adjudico para el **233** y la 43 para el **599**. **Y AQUI HAY UNA DIFERENCIA CON AQUELLOS DOS, que se
dice porque MEJORA el caso: LA ARISTA YA EXISTE Y ESTA BIEN PUESTA**, buscada hoy en los dos sentidos
contra el grafo (regla 9): `lienzo_modelo_negocio` nombra a `swot_business_model_canvas` en sus
`nodos_siguientes` **y** este lo nombra en sus `nodos_previos`, o sea **arista dirigida CON su
espejo**. **Este par NO deja ninguna arista que falte para la fase 04.** **Misma fuente los dos**
(Osterwalder con dos grafias), lo que descarta el argumento de libro.

> **Y SE DICE LO QUE INCOMODA EN VEZ DE ELEGIR EL DATO QUE CONVIENE: EL DESTEJIDO ACERCO LOS DOS
> TEXTOS.** Al quitar del nodo largo tres de sus cuatro narraciones, **lo dejo mas parecido a un
> recorrido de los nueve bloques, que es justo la forma del paso 1 del donante**. **Aun asi el
> veredicto es `D`**, y por la misma frontera del 344 y del 233: **recorrer los bloques para
> CONSTRUIRLOS no es recorrerlos para EVALUARLOS**, y **ningun paso del nodo largo pregunta nada**.
> **VA COMO DISCUTIBLE MARCADO.**

> **UNA PRECISION SOBRE UNA CIFRA QUE PODRIA CONFUNDIR, medida y declarada:** el archivo **sigue
> teniendo UNA fila con la frase *NO SE JUZGA HOY***, y es **la misma 784**, porque **la razon vieja
> se conserva entera dentro de la nueva**. **Lo que la distingue no es la frase sino la APERTURA**: su
> razon **ya no abre** con marca de congelado, y **la lista de razones que SI abren asi baja de DOS a
> UNA**. Quien cuente por la frase contara uno; quien cuente por la apertura contara cero. **Se dice
> asi para que nadie lea la cifra sin su vara.**

### LA SENAL DE COSTURA, RE-MEDIDA DESPUES DE LA CIRUGIA

**Re-corrido `scripts/costuras_internas.py` tras el acto**: `lienzo_modelo_negocio` pasa de **bloque
65,6 con corte tras el 13** a **bloque 46,0 con corte tras el 8**, o sea **menos 19,6**, con **12
pasos en vez de 17**. **La senal SIGUE disparando por bloque y eso se publica en vez de omitirse**, y
**queda como CITA y no como veredicto**, por el limite declarado del propio instrumento (*la cola
global no es base de lectura*, acta de la vuelta 40 seccion 5 pregunta 2). **La cola global se queda
en 1.494 sobre 3.524**: el nodo ya estaba dentro y sigue dentro, asi que **no entra ni sale nadie**.

### EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE (regla 1)

**Las dos columnas con el mismo instrumento en dos momentos**: la apertura antes del primer acto
(`SALIDA_V45_APERTURA.txt` y `SALIDA_V45_APERTURA_COLA.txt`, commiteadas solas) y el cierre **despues**
de la relectura del 784.

| | apertura de la vuelta 45 | **al cierre, recomputado** | lo que lo movio |
|---|---:|---:|---|
| ficheros | 3.853 | **3.853** | nada |
| vivos | 3.524 | **3.524** | **nada: un destejido no deprecia a nadie** |
| deprecados | 329 | **329** | nada |
| enlaces | 16.898 | **16.898** | **nada, y es una GUARDA de la operacion, no una casualidad** |
| cola de costuras | 1.494 sobre 3.524 (42,4 por ciento) | **1.494 sobre 3.524 (42,4 por ciento)** | nada: el nodo ya estaba dentro y sigue dentro |
| marcador `n` | 3.388 | **3.388** | nada: sin altas ni bajas |
| marcador A | 575 | **575** | nada |
| marcador B | 80 | **79** | **la relectura del 784**, el caso positivo de la operacion |
| marcador C | 8 | **8** | nada |
| marcador D | 2.725 | **2.726** | la misma relectura |
| tasa de A | 17,0 | **17,0** | nada |

**UN SOLO MOVIMIENTO EN TODA LA VUELTA, y es el que la operacion mandaba producir.**

### EL REGISTRO DE OPERACION HECHA, con el patron de la vuelta 30

**Los NUEVE puntos de la `verificacion` estan cumplidos y medidos**, asi que el registro se escribe
**en la nota**, con el campo `estado` **quieto en `LISTA`** (el esquema no tiene el valor `HECHA`,
**adjudicado NO en el punto 7 del acta de la vuelta 30**).

> **VA COMO DISCUTIBLE MARCADO, y se marca antes de saber si acierta:** el encargo de esta vuelta pide
> para `OP-D-08` un *registro de cierre* y **no dice literalmente** *registro de OPERACION HECHA*, que
> si lo decia para `OP-D-01` y `OP-D-02`. **Se escribe igual** porque la vara que el propio encargo
> fija para el registro es *si y solo si todo lo material cumple*, y aqui cumple **9 de 9** con su
> medicion al lado; **no escribirlo dejaria la operacion sin registro y se lo cargaria a la vuelta
> siguiente**, que es justo lo que esta vuelta acaba de tener que hacer con `OP-D-01` y `OP-D-02`.
> **Si el auditor lee que el encargo no lo cubria, la correccion es quitar el parrafo de la nota, y el
> texto viejo queda entero delante para que se pueda hacer.**
"""

with io.open('docs/plan/02_DESTEJIDOS.md', 'a', encoding='utf-8', newline='') as fh:
    fh.write(CAB + salida + u"\n" + PIE)
print("OK, seccion de cierre de OP-D-08 pegada")
