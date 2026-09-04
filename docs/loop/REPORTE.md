# REPORTE DE LA VUELTA 168 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION.** Es la
> regla nueva de `EJECUTOR.md` 1 ("EL REPORTE ABRE CON LA VUELTA", decision del
> fundador del 4 sep 2026) estrenandose sobre si misma. El esqueleto lo tallo
> `scripts/loop/vuelta168_esqueleto_reporte.py` antes de la primera tarea;
> cada tarea ANEXA SU FILA AL CERRARSE, no al final; y el cierre talla la
> cabecera. **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se
> hizo, y las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se
> hicieron.** Tope de cinco tareas por vuelta, y el encargo trae exactamente
> cinco.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar. Un veredicto escrito en la apertura seria justo la especie
que esta regla existe para matar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta168_esqueleto_reporte.py`, que la busca con
`git rev-parse --abbrev-ref HEAD` y con `git log` y CAE EN ROJO si no la
encuentra o si es ambigua:

- rama: `pasada-unica`
- commit del acta de la vuelta 167: `e3152a9c`, asunto real leido de git log:
  'ACTA DE LA VUELTA 167 DEL AUDITOR Y PARADA: OP-C-01 NO SE PUEDE EJECUTAR PORQUE ESTA EJECUTADA, Y NO ES UN CASO SUELTO. 37 DE 71 FICHAS NO CALZAN Y LA CAIDA ES MIA'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V168_HEAD_APERTURA.txt`: `edbc1a48`
- commit de nacimiento del bloque de apertura y commit de cierre: se tallan al
  cierre. **Un reporte no puede nombrar el commit que lo lleva**, porque ese
  commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla de
comprobaciones sale de
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 168`, cuya columna
derecha se lee de las salidas `SALIDA_V168_*_CIERRE.txt`. En la apertura esas
salidas no existen, y el tallador, corrido hoy, lo dice sin adorno: **"ROJO, 19
celdas no se pudieron leer y NO se talla nada"**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS: el acta 167 en `R.37`, y la nota adosada al `R.36` | **CERRADA** | `SALIDA_V168_T1_REGISTRO_ACTA_167.txt`, `SALIDA_V168_T1_NOTA_R36.txt`, `SALIDA_V168_T1_MUTACION_NOTA_R36.txt` |
| **TAREA 2** | EL REPORTE QUE CUBRE LAS VUELTAS 166 Y 167 | **CERRADA** | `SALIDA_V168_T2_RECONSTRUCCION_166_167.txt`, `SALIDA_V168_T2_MUTACION_RECONSTRUCTOR.txt` |
| **TAREA 3** | EL MANTENIMIENTO DE LA BATERIA (3.a nomina, 3.b re anclaje, 3.c corrida entera) | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | `OP-V-01` POR LA DECISION 5, VERIFICADA CONTRA GIT | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | ABRIR LAS SEIS POR LA VARA DEL INSTRUMENTO (5.a, 5.b valvula, 5.c depende_de) | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
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

### TAREA 2, EL REPORTE QUE CUBRE LAS VUELTAS 166 Y 167

**Salidas:** `docs/loop/SALIDA_V168_T2_RECONSTRUCCION_166_167.txt` (la
reconstruccion) y `docs/loop/SALIDA_V168_T2_MUTACION_RECONSTRUCTOR.txt` (su caso
positivo). **Instrumento:**
`scripts/loop/vuelta168_tarea2_reconstruir_166_167.py`.

**LA DEUDA, MEDIDA Y NO RECORDADA.** Las dos vueltas terminaron sin escribir su
reporte, y esta tarea lo comprueba en vez de creerlo: la seccion F de la salida
dice, para el arbol del acta 166 Y para el del acta 167, que la primera linea de
`docs/loop/REPORTE.md` era *"# REPORTE DE LA VUELTA 165"*. **Dos vueltas
seguidas, y la misma cabecera heredada en las dos.**

**LAS DOS VUELTAS, CONTADAS DE SU FICHERO DE SALIDA.** Cada celda sale de
`docs/loop/SALIDA_V168_T2_RECONSTRUCCION_166_167.txt`, secciones A, C y D:

| | **vuelta 166** | **vuelta 167** |
|---|---:|---:|
| commit que la abre (acta anterior, leido de git) | `00cfe6e0` | `7028a76a` |
| commit que la cierra (su propia acta) | `7028a76a` | `e3152a9c` |
| commits del corredor, acta incluida | **9** | **6** |
| de ellos, commits del ejecutor | **8** | **5** |
| tareas con commit propio | **6** | **4** |
| lineas anadidas | **8.886** | **7.754** |
| lineas quitadas | **181** | **199** |
| rutas distintas tocadas | **83** | **71** |
| rutas bajo `dataset/` | **0** | **0** |
| rutas bajo `web/` | **0** | **0** |
| rutas bajo `docs/plan/` | **3** | **1** |
| escribio su `REPORTE.md` | **NO** | **NO** |

**LAS CERO RUTAS BAJO `dataset/` Y BAJO `web/` SON LA CIFRA QUE MAS DICE:** en
las dos vueltas **no se toco ni un nodo ni una arista ni una linea de la web**.
Todo lo que se movio fue documentacion, instrumentos y salidas.

**LAS TAREAS, UNA POR UNA, CON SU COMMIT (seccion C de la salida).** Vuelta 166:
`TAREA 1` `2ee2592a`, `TAREA 2` `a23509cf`, `TAREA 3` `33fe1380`, `TAREA 4`
`6c38fb39`, `TAREA 5` `9363c1ba`, `TAREA 6` `0a0e658f`, mas su bloque de
apertura `8472d645` y su bloque de cierre `0f7d5bb2`. Vuelta 167: `TAREA 1`
`a6b318ca`, `TAREA 3` `12053ade`, `TAREA 4` `c6ac70f6`, `TAREA 5` `3d0277d3`
(parada), mas su bloque de apertura `b08543eb`. **LA 167 NO TIENE `TAREA 2` NI
BLOQUE DE CIERRE, y el hueco se ve en la propia lista de commits**: su TAREA 2
era el reporte.

**EL VEREDICTO DEL AUDITOR SOBRE CADA UNA, LEIDO DE SU ACTA Y MARCADO COMO
SUYO** (seccion E; es de otra sede y por eso no se mezcla con lo de arriba):

- **166** (`docs/loop/ACTA_AUDITOR.md:55297`): *"LAS SEIS TAREAS DE LA 166 ESTAN
  ENTREGADAS Y REPRODUCEN TODAS BAJO MIS INSTRUMENTOS, PERO LA VUELTA SE CORTO
  ANTES DE ESCRIBIR SU REPORTE Y ANTES DE QUE LA BATERIA TERMINARA."*
- **167** (`docs/loop/ACTA_AUDITOR.md:55653`): *"LAS CUATRO TAREAS QUE LA 167
  ENTREGO REPRODUCEN TODAS AL DIGITO BAJO MIS INSTRUMENTOS, SU QUINTA ENTREGA
  UNA PARADA QUE ES CORRECTA, Y LA SEGUNDA NO SE ENTREGO."*

**LAS CIFRAS DE TAREAS DE ESTA TABLA Y LAS DE LOS DOS VEREDICTOS COINCIDEN, Y SE
DICE PORQUE PODRIAN NO HABERLO HECHO:** 6 y 4, medidas por mi de los asuntos de
los commits, contra "las seis tareas" y "las cuatro tareas" del auditor, medidas
por el en su vuelta. **Dos manos y dos metodos dan lo mismo.**

**LO QUE NO SE PUEDE RECONSTRUIR, DECLARADO Y NO RELLENADO (seccion G, 4 cosas).**
Ninguna de estas cuatro vive en un commit ni en un acta, asi que **no se
escriben**:

1. **LOS DISCUTIBLES MARCADOS de cada vuelta.** Un discutible se marca ANTES de
   saber si se acierta. Hoy las dos actas ya publicaron su veredicto, asi que
   cualquier lista escrita ahora seria una copia con la respuesta delante.
2. **LAS PREGUNTAS de cada vuelta.** Fabricarlas hoy seria inventar el estado
   mental de una sesion cerrada.
3. **LOS PENDIENTES DE DOCTRINA que las dos vueltas hubieran levantado.** Solo
   se conocen los que llegaron a una sede escrita.
4. **EL VEREDICTO DE UNA LINEA del ejecutor de cada vuelta.** Escribirlo hoy
   seria escribir el del auditor con otra letra.

**UNA CIFRA MIA QUE ESTUVO MAL Y LA CAZO MI PROPIO ARNES ANTES DE PUBLICARSE, y
se declara en vez de taparse:** al escribir los casos puse **8 y 5 commits** de
memoria, de un `git log --oneline -8` truncado. El arnes midio **9 y 6**, porque
el corredor que este instrumento define llega hasta el acta INCLUSIVE. **No
llego a ninguna salida sellada ni a ninguna tabla**; la correccion vive escrita
en el comentario del propio instrumento, junto al caso, sin borrar el motivo.
**Caso positivo por mutacion: 17 casos pasan tal cual y los 17 caen al mutar el
esperado, exit 0.** El contador de tareas se probo ademas sobre corredores
fabricados en memoria, incluido uno cuyo asunto NOMBRA una tarea sin abrirla
(*"ACTA: la TAREA 5 quedo en parada"*), que el instrumento no cuenta.

<!-- FIN ANEXO DE TAREAS -->
