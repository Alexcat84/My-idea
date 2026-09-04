### TAREA 1, LOS REGISTROS: `R.37`, Y LA NOTA ADOSADA AL `R.36`

**Salidas:** `docs/loop/SALIDA_V168_T1_REGISTRO_ACTA_167.txt` (la escritura del
`R.37`), `docs/loop/SALIDA_V168_T1_NOTA_R36.txt` (la nota adosada) y
`docs/loop/SALIDA_V168_T1_MUTACION_NOTA_R36.txt` (su caso positivo).
**Instrumentos:** `scripts/loop/vuelta168_tarea1_registrar_acta167.py`,
`scripts/loop/vuelta168_tarea1_adosar_nota_r36.py` y el arnes
`scripts/loop/vuelta168_tarea1_mutacion_registro.py`.

**LAS CIFRAS, CONTADAS DE SU FICHERO DE SALIDA Y NO TECLEADAS.** Cada una sale
de `docs/loop/SALIDA_V168_T1_REGISTRO_ACTA_167.txt`, en la seccion que se
nombra al lado:

| lo que se midio | cifra | de que seccion de la salida sale |
|---|---:|---|
| adjudicaciones `6.n` del acta 167 | **6** (6.1 a 6.6) | B |
| caidas propias del auditor, seccion 3 del acta | **2** | C |
| cuerpo del acta 167 acotado, `ACTA_AUDITOR.md` | **lineas 55.644 a 56.057** | A |
| entradas de la serie ANTES de escribir | **28** | E |
| colisiones y huecos de la serie | **0 y 0** | E |
| numero libre, computado y no tecleado | **`R.37`** | E |
| entradas de la serie DESPUES de escribir | **29** | K |

**EL REPARTO POR VIA, DE LA SECCION I DE LA MISMA SALIDA:** `SIN TOCAR NADA` 3
(6.1, 6.2, 6.3); `EN MEDICION` 2 (6.4, 6.5); `AL FUNDADOR, YA CONTESTADA` 1
(6.6). **Y LA LINEA DEL FUNDADOR DEJA DE SER UNA FRASE FIJA:** el `R.36` decia
*"Ninguna de las nueve sube al fundador"* porque el acta 166 no subia ninguna;
el acta 167 SI sube su `6.6` con la palabra *"lo subo"*, asi que en este
instrumento esa frase **se computa del reparto**. Si estuviera tecleada, la
herencia la habria arrastrado mintiendo.

**LAS DOS CIFRAS DEL TITULO SE MOVIERON EN SENTIDOS OPUESTOS, Y ES LA MEJOR
PRUEBA DE QUE NO ESTAN TECLEADAS:** el `R.36` registro **nueve** adjudicaciones
y **una** caida; el `R.37` registra **seis** y **dos**. La concordancia del
titulo cambia sola de la rama del singular a la del plural.

**EL CASO POSITIVO POR MUTACION DEL REGISTRADOR:** `34 casos pasan tal cual y
los 34 caen al mutar el esperado`, exit 0, corrido por el arnes de nombre propio
que la bateria ve.

**LA NOTA ADOSADA AL `R.36`, Y LO QUE LA HACE DISTINTA DE UNA GLOSA MAS: LOS
CUATRO VEREDICTOS SE MIDIERON CONTRA GIT, NO SE COPIARON DEL ACTA.** Cifras de
`docs/loop/SALIDA_V168_T1_NOTA_R36.txt`, secciones B, C y E:

| glosa del `R.36` | la medicion de hoy | ocurrio |
|---|---|---|
| `6.1` y `6.3`: el reporte de la 167 cubre las dos vueltas | `git show e3152a9c:docs/loop/REPORTE.md` da primera linea **VUELTA 165** | **NO** |
| `6.4`: la bateria de verdad se corre en esa vuelta | `SALIDA_V167_BATERIA.txt` en ese arbol mide **0 bytes** | **NO** |
| `6.9`: EJECUTADA EN EJECUCION, TAREA 5 | ultimo commit del ejecutor antes del acta: `3d0277d3`, *"TAREA 5: PARADA..."* | **NO** |

**4 de 4 no ocurrieron**, y la cifra sale del conteo de los veredictos, no de la
adjudicacion. **NINGUNA PALABRA VIEJA SE BORRO Y EL INSTRUMENTO LO COMPRUEBA
SOLO:** la seccion E dice `el cuerpo viejo del R.36 sigue ENTERO dentro del
nuevo: SI`, **32 lineas anadidas y 0 borradas**, porque la escritura es una
insercion. **Su caso positivo por mutacion:** `14 casos pasan tal cual y los 14
caen al mutar el esperado`, exit 0, y **el veredicto de cada glosa es una
variable computada**: alimentado con un sujeto fabricado donde el reporte SI es
el de la 167 y la bateria trae 4.000 bytes, el mismo codigo dice que las cuatro
ocurrieron. **Si la medicion hubiera dicho que ocurrieron, el instrumento NO
habria escrito la nota y lo habria declarado**, que es lo contrario de dar por
buena una adjudicacion sin comprobarla.

**LO QUE ESTA TAREA NO HACE:** no reabre el `R.36`, no mueve ninguna clase del
cribado, no toca ningun `estado` y no borra una linea.
