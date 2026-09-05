### TAREA 4. LAS DOS DEUDAS DE REGISTRO (adjudicaciones 6.4 y 6.11)

Instrumento `scripts/loop/vuelta171_tarea4_deudas_de_registro.py`, salida
`docs/loop/SALIDA_V171_T4_DEUDAS_DE_REGISTRO.txt`, **exit 0**. **La fecha de
corte tampoco se teclea:** la lee del reloj del sistema y da **5 sep 2026**.

**4.a EL AGUJERO DEL `R.38`, PAGADO POR EL CARRIL DEL BANCO `9.10`.**

| celda | de donde sale | valor |
|---|---|---:|
| `R.38` acotado | cabecera y siguiente `## R.n.` | `docs/PENDIENTES.md`, lineas 12.081 a 12.166 |
| veces que la clausula falsa aparece DENTRO de `R.38` | barrido | **1** |
| veces que aparece en el fichero ENTERO | barrido | **1** |
| arneses de mutacion de registro que existen hoy | `ls scripts/loop/ \| grep mutacion_registro` | **7** |
| vueltas representadas | del nombre de cada fichero | 164, 165, 166, 167, 168, 170, **171** |
| ¿existe el de la vuelta 169? | del mismo barrido | **NO** |

**QUE SE TACHA Y QUE NO, Y ES UNA DECISION QUE DECLARO.** La oracion empieza
diciendo *"Lo que lo impide es el espacio final del patron"*, **y eso es
CIERTO**. Lo falso es la clausula que viene detras. **Tache la clausula falsa
entera y deje en pie la parte cierta**: enterrar una afirmacion buena para tapar
una mala no es corregir. Va como `D.3`.

La correccion adosada dice las tres cosas que hacen falta: que **cuando esa
entrada se escribio el arnes no existia** (el registrador de la 169 se quedo sin
`prueba_de_mutacion`), **la nomina medida hoy pegada entera**, y **quien lo trajo
y quien lo corrige**, porque las dos cosas cuentan: lo hallo el ejecutor de la
170 como su `D.8` y no lo corrigio; la `6.4` dice que *"no es mio"* no vale para
una afirmacion falsa en la serie. **Y dice lo que la correccion NO hace:** no
toca el `R.39` ni el `R.40`, donde la misma frase **si** es cierta.

**4.b EL `81` DE `docs/plan/00_INDICE.md:644`, ADOSADO POR `9.21`.**

| celda | de donde sale | valor |
|---|---|---:|
| filas que casan con el ancla de la celda | barrido del fichero | **1**, la 644 |
| la cifra vieja que la celda publica | leida de la propia celda | **81** |
| el corte que la celda declara | leido de la propia celda | **19 ago 2026** |
| lecturas dirigidas HECHAS hoy | `vuelta48_contar_ld.py` corrido en esta vuelta, exit 0 | **82** |
| la diferencia | computada | **1** |

**LA LETRA VIEJA NO SE TOCA** y la comprobacion lo mide: `exit 0): 81**` sigue
entero en el fichero despues de escribir.

**Y LA FILA DE AL LADO NO RECIBE SU CIFRA DE HOY, Y ESO ES UNA DECISION MIA QUE
DECLARO.** *"Lecturas dirigidas encargadas y sin hacer"* publica **CERO** con su
corte, y el barrido de hoy da **8**. **Ese 8 esta contaminado**: la TAREA 2 midio
que seis de esos ocho salen de dos ficheros que ha escrito esta misma vuelta.
**Adosarlo seria meter una cifra envenenada en una pagina del plan**, que es peor
que dejar la celda vieja con su corte escrito. El instrumento tiene una guarda
que comprueba que esa fila no se toco y que el 8 no se colo. Va como `D.4`.

**LAS DIEZ COMPROBACIONES DE RELECTURA DEL DISCO PASAN, 0 FALLAN**, incluidas
*"la frase falsa sigue ENTERA en el fichero"*, *"y ahora esta TACHADA"* y *"y no
se le colo la cifra contaminada"*.
