### TAREA 2 (BLOQUEANTE PARA LA 3). SE DESENVENENA EL CONTADOR Y SE CORRIGE EL `R.40`

**2.a `docs/loop/reportes/REPORTE_V<N>.md` ENTRA EN LOS NARRATIVOS DEL BUCLE, Y
ENTRA POR PATRON.** El cambio vive en `scripts/loop/vuelta48_contar_ld.py` como
**correccion declarada 4** en su docstring, al lado de las tres viejas y sin
borrar ninguna, y lo aplica `scripts/loop/_v172_parche_contador.py` con sus
`assert`.

**Y HUBO QUE HACER ANTES UNA COSA QUE EL ENCARGO NO NOMBRA, ASI QUE LA DIGO:
SACAR EL CRITERIO A UNA FUNCION PURA.** La decision de excluir vivia **dentro
del bucle de `main()`**, y ahi **no hay nada que un arnes pueda llamar**: una
guarda que no se puede llamar no se puede probar por mutacion. Nace
`motivo_de_exclusion(rel)`, que devuelve `SALIDA`, `NARRATIVO`, `ARNES` o
`None`, y **`main()` pasa a llamarla**. Una sola fuente del criterio, no dos
copias. Va como `D.4`.

| celda | de donde sale | valor |
|---|---|---:|
| patron nuevo | del codigo | `^docs/loop/reportes/REPORTE_V\d+\.md$` |
| es un patron, no una lista de nombres | del codigo | **SI**, cubre la carpeta de archivo entera |
| ficheros que excluye HOY | contador corrido en esta vuelta | **4** (`REPORTE_V168`, `V169`, `V170`, `V171`) |
| narrativos del bucle, antes | `SALIDA_V172_T2_CONTAR_LD_ANTES.txt` | **3** |
| narrativos del bucle, hoy | `SALIDA_V172_T2C_ATRIBUCION.txt` | **7** |

**EL CASO POSITIVO POR MUTACION, Y CAE POR LOS DOS LADOS QUE EL ENCARGO PIDE:**
`scripts/loop/vuelta172_tarea2a_mutacion_exclusion.py`, salida
`docs/loop/SALIDA_V172_T2A_MUTACION_EXCLUSION.txt`, **exit 0**: **27 casos, 27
pasan, 27 caen al mutar el esperado**. Lo que prueba, y son tres frentes:

- **que el archivo no cuenta**, para vueltas que existen y para una que no
  (`REPORTE_V9999.md`);
- **que la regla NO se ensancha**: `notas.md`, `REPORTE_VX.md`,
  `REPORTE_V12.txt`, `REPORTE_V12.md.bak`, un subdirectorio y
  `docs/loop/REPORTE_V12.md` **siguen contando**. Una exclusion que se comiera
  la carpeta entera seria un agujero;
- **que estrecharla la tumba**: se fabrica la version estrecha (la que nombra
  `REPORTE_V171.md`) y con ella **0 de 4** archivos quedan excluidos, contra
  **4 de 4** con el patron. Y **si el patron se desactiva, tambien cae**.

**SUJETO CONGELADO:** los sujetos son cadenas literales del proceso, no se lee
el disco, y el resultado no depende de que ficheros existan hoy.

**2.b EL `R.40` TRAIA UNA AFIRMACION FALSA Y QUEDA CORREGIDA POR EL CARRIL DEL
`9.10`.** Instrumento `scripts/loop/vuelta172_tarea2b_corregir_r40.py`, salida
`docs/loop/SALIDA_V172_T2B_CORREGIR_R40.txt`, **exit 0**.

| celda | de donde sale | valor |
|---|---|---:|
| `R.40` acotado | cabecera y siguiente `## R.n.` | `docs/PENDIENTES.md`, lineas 12.289 a 12.391 |
| la via falsa de la 6.1 | barrido | **1** dentro, **1** en el fichero entero |
| la clausula falsa | barrido | **1** dentro, **1** en el fichero entero |
| la frase de las 16 filas en pasado | barrido | **1** dentro, **1** en el fichero entero |
| veces que el reporte archivado de la 171 dice *"NO SE CORRE"* | barrido de `REPORTE_V171.md` | **3** |
| commits de la 171 que tocan `docs/plan/LECTURAS_DIRIGIDAS.md` | `git log 0caca89f..cae2731d --` | **0** |
| lineas `VIA:` halladas en el `R.40` | barrido de la propia entrada | **12** |
| reparto VIEJO, contado de la entrada | del barrido | EJECUTADA **8**; SIN TOCAR NADA **4** |
| reparto CORREGIDO | recomputado | EJECUTADA **7**; NO SE CORRIO **1**; SIN TOCAR NADA **4** |

**LOS CERO COMMITS SON LA PRUEBA DURA**, y no la palabra del reporte: la vuelta
171 **no toco el fichero donde esas 16 filas viven**, asi que no pudo darles
ningun numero.

**QUE SE TACHA Y QUE NO, Y ES LA MISMA DECISION QUE EL `D.3` DE LA 171 QUE LA
`6.9` DIO POR BUENA.** La glosa abria diciendo que **la regla estaba escrita en
el codigo de `serie_de_registros.py`**, con su cita de lineas, **y eso es
cierto**: se queda en pie y sin tachar. Lo tachado es el tiempo verbal de la
ejecucion, ni una palabra mas. **Y la glosa de la `6.2` no se toca**, por letra
de la adjudicacion 6.3, que dice que describe bien lo que paso.

**Y ESTRENO UNA ETIQUETA DE VIA, ASI QUE LO DIGO EN VEZ DE COLARLA.** El
vocabulario de vias de la casa trae `EJECUTADA`, `SIN TOCAR NADA` y
`AL FUNDADOR`; para la 6.1 escribi **`NO SE CORRIO`**, que no estaba. Describe
un hecho medido y ninguna regla escrita la prohibe, pero **estrenar una palabra
es exactamente lo que hizo el `D.5` de la vuelta 170 y se le pidio cuenta**. Va
como `D.5`.

**UNA CAIDA MIA EN ESTA TAREA, DECLARADA CON SU NOMBRE** (va como `CAIDA 2` de
la seccion 8): **mi primera guarda anti guiones miraba el fichero ENTERO** y
salio ROJA despues de escribir, porque `docs/PENDIENTES.md` **ya traia 54
guiones largos de antiguo**, ninguno mio. Revertí con `git checkout`, cambié la
guarda **a lo que importa, el DELTA** (que yo no anada ninguno) mas una segunda
que mira **mi propio bloque**, y volvi a correr. **La guarda no se aflojo: se
reapunto**, que es lo mismo que la vuelta 170 hizo con su `CAIDA 2`.

**2.c EL CONTADOR OTRA VEZ, CON LA ATRIBUCION DELANTE.** Instrumento
`scripts/loop/vuelta172_tarea2c_atribucion.py`, salida
`docs/loop/SALIDA_V172_T2C_ATRIBUCION.txt`, **exit 0**. **No copia ninguna regla
del contador: las importa** (`RE_ID`, `RE_CAB`, `PAGINAS`,
`motivo_de_exclusion`), y por eso puede dar la LINEA que el contador no imprime.

| vara | antes de la 2.a, mismo arbol | hoy |
|---|---:|---:|
| mayor de las **HECHAS** | LD-138 | **LD-138** |
| mayor del **UNIVERSO** | LD-155 | **LD-154** |
| nombrados sin seccion propia | 9 | **6** |
| ficheros excluidos por NARRATIVO | 3 | **7** |

**LA CIFRA VIEJA NO SALE DE UN ACTA NI DE UN REPORTE:** sale de
`docs/loop/SALIDA_V172_T2_CONTAR_LD_ANTES.txt`, **corrida en esta misma vuelta**
sobre este mismo arbol antes de tocar el instrumento.

**LA ATRIBUCION, QUE ES LA GUARDA DE LA TAREA 3: SOLO QUEDAN DOS NUMEROS POR
ENCIMA DE `LD-138`, Y NINGUNO TIENE SECCION PROPIA.**

| numero | seccion propia | donde esta nombrado, con fichero y linea |
|---|---|---|
| `LD-139` | **NO** | `docs/PENDIENTES.md:12323`, `:12446`, `:12488` |
| `LD-154` | **NO** | `docs/PENDIENTES.md:12323`, `:12447`, `:12488` |

**Las tres lineas de cada uno son las tres glosas del registro**: la del `R.40`
(la corregida hoy), y las del `R.41` que esta vuelta escribio al citar la
adjudicacion `6.2`. **Ninguna es un encargo: las tres son un registro fiel que
cita un encargo**, que es exactamente el `PD.1` que la 171 dejo abierto.

**LAS CUATRO GUARDAS PASAN, 0 FALLAN**, incluida *"ningun numero por encima de
`LD-138` tiene seccion propia"* y *"el archivo de reportes ya no cuenta"*
(comprobado barriendo todos los sitios del universo). **LA TAREA 3 SE PUEDE
CORRER, y el siguiente libre por la vara que asigna es `LD-139`.**
