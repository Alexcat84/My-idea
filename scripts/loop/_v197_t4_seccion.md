### TAREA 4, LAS DOS CIFRAS QUE VIAJAN SIN SU VARA. CERRADA.

**Ficheros de salida, y toda cifra de abajo se cuenta de ellos:**
`docs/loop/SALIDA_V197_APERTURA.txt` bloque `F`,
`docs/loop/SALIDA_V197_T4_TRES_VARAS.txt` y
`docs/loop/SALIDA_V197_T4_MUTACION_TRES_VARAS.txt`.

**(a) LA CIFRA DE FUERA DE LA NOMINA YA NO PUEDE VIAJAR SOLA.** El remedio va
**dentro del bloque `F` del sello de apertura**, que es donde nace la cifra, y de
ahi lo lee la cabecera del reporte por `varas_de_la_nomina()` del esqueleto, que
**CAE EN ROJO si el sello no trae las dos**. Medido en esta vuelta: censo **195**,
nomina **135**, invisibles al censo **0**, sin sujeto congelado **0**, y **fuera de
la nomina CON la vara 148: 0**, **SIN vara: 60**. Las dos van impresas **con el
numero de la vara al lado**, y el sello lista los diez primeros de los 60 para que
la cifra no viaje sola. **No era caida** y la `4.7` lo dice; lo que se arregla es
que un `0` junto a un 195 y un 135 **se lee como cobertura total del censo, y es
cobertura desde la vara para arriba**.

**(b) EL TOPE DE 80 LINEAS, MEDIDO POR LAS TRES VARAS.** Instrumento:
`scripts/loop/vuelta197_tarea4_tres_varas.py`, con **8 casos de mutacion, 8
verdes, 0 rojos**.

| vara | que cuenta | este reporte | el de la 196 |
|---|---|---:|---:|
| **V1 total** | `count(NL)` | **395** | **588** |
| **V1 total** | `len(split(NL))` | **396** | **589** |
| **V2 escrita a mano** | total menos las piezas TALLADAS | **380** | **562** |
| **V3 estrecha** | V2 menos lo que otra regla obliga | **344** | **267** |

*(Las dos columnas se midieron al anexarse esta tarea; el reporte sigue creciendo
hasta el cierre y sus cifras finales las remide el instrumento al cerrar.)*

**LA TERCERA VARA SIGUE MUY POR ENCIMA DE 80, Y LO DIGO CON ESAS PALABRAS**, que
es lo que el encargo manda: **344 lineas contra un tope de 80, 4.3 veces el tope**,
y en el reporte de la 196 **267, 3.3 veces**. **El tope no se afloja y no invento
ninguna excepcion.**

**CADA RESTA LLEVA AL LADO LA GUARDA QUE LA OBLIGA**, y **una seccion sin guarda NO
se resta**: eso es lo unico que impide que la vara estrecha sea una excusa, y va
probado con su mutacion (una seccion `## 99.` fabricada sin guarda NO baja la V3).
**Una marca de pieza tallada que aparezca dos veces tampoco se resta.**

**DISCREPANCIA DECLARADA Y NO RESUELTA COPIANDO.** La `4.6` del acta 197 dice que
el reporte de la 196 mide **318 por la vara estrecha del acta 196**. Mi V2 sobre
ese mismo fichero da **562**. La causa que sostengo, medida: **318 es el numero de
saltos de linea del reporte de la 196 ANTES de cerrarlo**, y sale literal de
`docs/loop/SALIDA_V196_CERRAR_REPORTE.txt` (*"CIFRA bytes: 22804 | saltos de linea:
318"*). **No es la vara estrecha: es el conteo total de un reporte a medio
escribir.** Publico las dos y no elijo.

**LA PREGUNTA QUE DEJO ESCRITA, Y NO LA CONTESTO YO.** El austero dice que
**recorta tinta, no control**. Las tres cifras muestran que lo que empuja el
reporte por encima del tope **no es prosa de acompanamiento sino piezas que una
guarda exige**: la seccion 9, la seccion 4, la tabla de tareas, la cabecera
tallada. **Las tres respuestas posibles son del fundador y ninguna mia:** subir el
tope, medirlo por la vara estrecha, o recortar de verdad lo que hoy es
obligatorio.

**`D.11` DISCUTIBLE MARCADO. LA V3 LA DEFINI YO.** El encargo dice *"escrita a mano
menos lo que otra regla obliga a escribir"* y nombra cuatro piezas entre
parentesis. Yo reste **ocho secciones**, cada una con la guarda que la busca por su
literal. **Lo discutible es que ampliar la lista de restas hace la V3 mas pequena y
me favorece**, aunque el criterio (tener guarda que la busque) sea comprobable.
