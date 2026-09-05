### TAREA 3. LA NUMERACION `LD`, QUE AHORA SI SE ESCRIBE

**LAS 16 LECTURAS DE LA SEGUNDA TANDA GANAN `LD-139` A `LD-154`.** Instrumento
`scripts/loop/vuelta172_tarea3_numerar_ld.py`, salida
`docs/loop/SALIDA_V172_T3_NUMERAR_LD.txt`, **exit 0**.

| celda | de donde sale | valor |
|---|---|---:|
| hechas antes de escribir | funciones del propio contador | **82** |
| mayor de las HECHAS, computado | `siguiente_libre` sobre ese mapa | **LD-138** |
| siguiente libre, computado y no tecleado | mayor mas uno | **LD-139** |
| numeros con seccion propia por encima de `LD-138` | guarda (ii) | **0** |
| filas de par leidas de la tabla | barrido de los tres bloques | **8 + 5 + 3 = 16** |
| clases leidas de la tabla | del mismo barrido | **A 2, D 14** |
| numeros asignados | computados | **`LD-139` a `LD-154`** |
| el fichero antes | contado | 205.820 bytes, 2.078 saltos de linea |
| el fichero despues | contado | 214.916 bytes, 2.230 saltos de linea |

**QUE SIGNIFICA "POR ADICION PURA" AQUI, DICHO EXACTO PARA QUE SE PUEDA
DISCUTIR.** Las tres tablas **no se han tocado, ni una palabra ni un byte**: el
instrumento lo comprueba al releer, buscando cada una de las 16 filas de par tal
como estaba (`(nodo_a, nodo_b, clase)`) y contando **16 de 16 intactas**. Lo que
se anade es un **bloque nuevo al final de la segunda tanda**, con las 16
secciones en la forma de la casa
(``### `LD-nn` . `a` contra `b` . **CLASE**``), **y el par y la clase de cada una
se LEEN de la tabla**, no se teclean.

**Y DIGO LO QUE ESTE INSTRUMENTO NO HACE, PORQUE ES LO QUE MAS PODRIA
MALINTERPRETARSE: NO VUELVE A LEER NINGUN PAR.** Las 16 lecturas estan hechas y
sus veredictos escritos **desde el 11 ago 2026**; lo unico que les faltaba era el
numero. **Ninguna clase se mueve, ningun nodo se toca y `master_graph.json` no se
abre siquiera.** Cada seccion nueva remite a la tabla y **no copia su razon**,
porque una copia seria una segunda version de lo mismo.

**EL CONTRASTE CON EL SALDO QUE LA PROPIA PAGINA PUBLICA, Y ES CONTRASTE Y NO
FUENTE:** la pagina dice **leidas 16, REPITEN (A) 2, SANAS (D) 14** desde el 11
ago 2026, y mi conteo de hoy da **16, A 2, D 14**. Calzan al digito. **Manda mi
conteo**, que es el que se corrio hoy.

**LAS DOS GUARDAS, Y LAS DOS CAEN POR MUTACION.** Arnes
`scripts/loop/vuelta172_tarea3_mutacion_numeracion.py`, salida
`docs/loop/SALIDA_V172_T3_MUTACION_NUMERACION.txt`, **exit 0**: **24 casos, 24
pasan, 24 caen al mutar el esperado**. Y **para poder probarlas hubo que sacarlas
a funciones puras**, `siguiente_libre(hechas)` y `asignacion_ajena(hechas,
corte)`, porque dentro de `main()` no hay nada que un arnes pueda llamar.

- **La (i), que el numero se compute y no se teclee**, se prueba por donde
  importa: la funcion **devuelve cuatro valores distintos para cuatro mapas
  distintos**, y con mayor 90 el rango sale **`LD-91` a `LD-106`**. **Si el
  `LD-139` estuviera tecleado, ese caso no se moveria.**
- **La (ii), la asignacion ajena**, se prueba con mapas limpios, de un intruso y
  de dos, y **el arnes exige que los NOMBRE**, no solo que los cuente.
- Y el lector de filas se prueba contra una pagina fabricada: **no se traga el
  ruido de otra tabla, no cruza a la tercera tanda, no se traga la tabla de
  oficios, y lee las clases LITERALES** (`DDADAD` sobre un caso fabricado).

**SUJETO CONGELADO:** paginas y mapas son literales del proceso, **cero lecturas
de disco y cero escrituras**, asi que el arnes seguira verde dentro de diez
vueltas.

**EL CIERRE DE LA VARA, MEDIDO DESPUES** (`docs/loop/SALIDA_V172_T3_ATRIBUCION_DESPUES.txt`,
exit 0, y `docs/loop/SALIDA_V172_T3_CONTAR_LD.txt`):

| vara | antes de la 2.a | tras la 2.a | **al cerrar la TAREA 3** |
|---|---:|---:|---:|
| **hechas** | 82 | 82 | **98** |
| mayor de las **HECHAS** | LD-138 | LD-138 | **LD-154** |
| mayor del **UNIVERSO** | LD-155 | LD-154 | **LD-154** |
| nombrados sin seccion propia | 9 | 6 | **4** |

**LAS DOS VARAS CONVERGEN EN `LD-154`, QUE ES LO QUE EL ENCARGO PEDIA**, y las
**98** hechas tambien salen. **Los 4 que quedan estan nombrados uno a uno**:
`LD-12` y `LD-27` (las menciones de la serie `R.n` al glosar un encargo, o sea el
`PD.1` abierto) y `LD-71` y `LD-99`, que **la vuelta 48 ya declaraba como no
pendientes** con su linea de acta.

**Y UNA NOTA SOBRE EL INSTRUMENTO DE LA 2.c QUE NO ME AHORRO:** su corte estaba
**clavado en 138**, asi que al correrlo DESPUES de la TAREA 3 salia ROJO **por
diseno**, diciendo que hay asignacion ajena cuando lo que hay es el trabajo
recien hecho. **Un rojo que solo dice "hiciste tu tarea" es un rojo que no se
puede leer**, asi que el corte paso a ser parametro (`--corte`). Va como `D.6`.

**Y UNA CAIDA MIA AL HACERLO** (va como `CAIDA 3` de la seccion 8): al anadir el
parametro **volvi a correr el instrumento con `--corte 138` y pise su salida
vieja**, que era la evidencia de la guarda previa. **No se perdio nada porque
estaba commiteada**, y la restaure con `git checkout 96940490 --`. La salida que
hoy vive en `docs/loop/SALIDA_V172_T2C_ATRIBUCION.txt` es **la corrida original,
la de antes de la TAREA 3**, y la de despues vive aparte.

**LA SEGUNDA MITAD: LAS DOS FILAS DE `docs/plan/00_INDICE.md`, POR `9.21`.**
Instrumento `scripts/loop/vuelta172_tarea3b_indice.py`, salida
`docs/loop/SALIDA_V172_T3B_INDICE.txt`, **exit 0, 10 comprobaciones y 0 fallos**.

**LA FILA QUE EL ENCARGO NOMBRA** es *"lecturas dirigidas encargadas y sin
hacer"*, que publicaba **CERO** con corte 19 ago 2026 y hoy mide **4**. El `D.4`
de la vuelta 171 se nego a adosarla y **tenia razon**: entonces el barrido daba
**8** y seis salian del archivo de reportes. **Hoy ya se puede**, y los cuatro
van nombrados uno a uno dentro de la celda.

**Y TOQUE UNA SEGUNDA FILA QUE EL ENCARGO NO NOMBRA, ASI QUE LO DIGO EN VEZ DE
COLARLO.** La fila de arriba, *"lecturas dirigidas hechas"*, llevaba adosada
desde la vuelta 171 la cifra **82 con corte 5 sep 2026**, y **mi TAREA 3, del
mismo 5 sep 2026, la ha movido a 98**. Dejarla asi habria puesto **dos cifras
distintas con la misma fecha para la misma vara en la misma celda**, que no es
una cifra con su corte sino una contradiccion, **y la habria creado yo**. Se
adosa por el mismo `9.21`, diciendo en palabras el antes y el despues (*"82 antes
de la TAREA 3 de la vuelta 172, 98 despues"*, diferencia exacta **16**), y **sin
tocar el 82, ni el 81, ni el 65**. Va como `D.7`.
