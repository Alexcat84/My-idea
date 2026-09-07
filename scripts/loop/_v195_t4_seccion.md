### TAREA 4. `--componer` DEJA DE PUBLICAR VERDE SOBRE DIEZ ROJOS. **CERRADA, Y LA LINEA QUE LA 194 PUBLICO YA NO SE PUEDE ESCRIBIR SOBRE ESOS MISMOS DIEZ TRAMOS.**

**EL CASO, MEDIDO Y NO CONTADO.** `docs/loop/SALIDA_V194_BATERIA_COMPUESTA.txt`
termina en *"VERDE: los 10 tramos cubren la nomina entera"* con `exitcode 0`,
mientras los diez tramos que compone traen `CLASE DEL VEREDICTO: ROJO POR FALLO` y
`exitcode 1`. **Las dos cosas eran verdaderas midiendo cosas distintas**: la
cobertura estaba completa (127 de 127) y la bateria estaba roja. Lo que estaba mal
era que la salida **se leyera como si la bateria estuviera bien**. Banco `9.1`: el
instrumento debe caerse en vez de mentir.

#### 4.a EL PEOR VEREDICTO SE PROPAGA AL EXITCODE Y A LA LINEA FINAL

Dos funciones nuevas en `scripts/loop/vuelta194_bateria_por_tramos.py`, que es el
lanzador del que la 199 clonara el suyo:

- **`clase_de_la_salida(ruta)`** lee la `CLASE DEL VEREDICTO` que cada tramo
  publica. **Se lee de la salida y no se recalcula**, igual que la cobertura:
  recalcularla seria preguntarle al reparto por el reparto. **Un tramo que no
  publica su clase devuelve `None`, y `None` NO se confunde con VERDE.**
- **`peor_veredicto(clases)`** devuelve la peor clase, su codigo y la lista de
  ilegibles. **Si hay algun ilegible, el peor es `ROJO POR FALLO`**: no se puede
  componer un verde sobre un tramo cuyo estado no se sabe.

**LOS NOMBRES Y LOS CODIGOS NO SE TECLEAN EN EL LANZADOR: se leen de
`verificar_mutaciones_viejas`**, que es su sede, para que no haya dos tablas que
manana digan cosas distintas.

#### 4.b LAS DOS COSAS SE SIGUEN DICIENDO POR SEPARADO

**Que propague el rojo no puede borrar que la cobertura estaba completa**, que es
informacion util y medida. La salida publica ahora **tres bloques distintos**: la
cobertura con su cifra, el veredicto de cada tramo con la suya, y el peor de los
dos. La linea final dice **las dos cosas juntas**: *"LA COBERTURA: los N tramos
cubren la nomina entera..."* y, debajo, el veredicto propagado con su motivo.

**CORRIDO SOBRE LAS DIEZ SELLADAS DE LA 194**, el composor lee los diez veredictos
y publica `EL PEOR VEREDICTO DE LOS TRAMOS: ROJO POR FALLO (codigo 1)`. **Esa
corrida NO llego a componer nada y NO piso ninguna sellada**, porque con la nomina
ya en 135 el reparto pide 11 tramos y solo hay 10: se paro antes de escribir, y
`SALIDA_V194_BATERIA_COMPUESTA.txt` quedo **byte a byte igual**, comprobado con
`cmp`.

#### 4.c EL CASO POSITIVO POR MUTACION, CON EL CASO REAL Y NO CON UNO COMODO

`scripts/loop/vuelta195_tarea4c_mutacion_componer_rojo.py`, salida en
`docs/loop/SALIDA_V195_T4C_MUTACION_COMPONER_ROJO.txt`: **`CIFRA casos: 15 |
pasan: 15 | fallan: 0`**, **`CIFRA casos que caen al mutar el esperado: 15 de 15`**,
**`VEREDICTO: VERDE`**, contado de su propio fichero.

**SUJETO CONGELADO, Y ES EL DE VERDAD:** las diez salidas de la 194 se leen **por
`git show` del commit `56c2d085`**, que es el que cierra su TAREA 3 y ya tiene las
diez en su arbol. **Un blob de git no se mueve**, y no se abre ningun fichero del
arbol de trabajo.

**LO QUE EXIGE, Y ES EXACTAMENTE LO QUE EL ENCARGO PIDE:** los diez tramos dan
`ROJO POR FALLO`, el peor de los diez es `ROJO POR FALLO`, su codigo NO es cero, y
**con estos diez el veredicto ya no puede ser VERDE**. La linea que la 194 publico
va dentro del arnes **como CITA y no como afirmacion suya**.

**Y LOS TRES CASOS QUE LA 194 NO DEJO VAN FABRICADOS EN MEMORIA**, porque una
guarda probada solo con el caso que ya ocurrio no sabe que hacer con el siguiente:
un tramo verde, un tramo en deuda, y **un tramo que no publica su clase**. Ese
tercero pone `ROJO POR FALLO` y sale nombrado en la lista de ilegibles.

**LA ESCALERA DE GRAVEDAD SE PRUEBA EN SUS TRES PELDANOS:** solo verdes da VERDE,
verde mas deuda da `ROJO POR DEUDA DECLARADA`, y deuda mas fallo da `ROJO POR
FALLO`. **Si el orden estuviera al reves, una bateria con un arnes caido se
publicaria como deuda declarada**, que es la degradacion que la `4.4` del acta 190
ya cazo una vez.

#### 4.d UNA CORRECCION DECLARADA DENTRO DE ESTA TAREA

La primera version del arnes apuntaba el sujeto congelado a **`6a508ca5`**, que es
el commit que anadio **el tramo 1** y en cuyo arbol solo existia **UNO de los
diez**. **Lo cazo su propio caso `los_DIEZ_blobs_se_leen`**, midiendo 1 donde tenia
que medir 10, que es para lo que ese caso esta. Corregido a `56c2d085` y **el
commit viejo se nombra en el codigo en vez de borrarse**, con lo que pasaba.

#### 4.e ESTO LLEVABA VUELTAS EN LA LISTA DE LO QUE SIGUE FUERA

Como *"el exitcode 2 propagado a `--componer`"*. **Hoy entra porque tiene su caso
medido delante**, y lo que se hizo es mas que propagar un 2: **se propaga el peor
de los tres veredictos, sea cual sea**, y la cobertura se sigue diciendo aparte.
