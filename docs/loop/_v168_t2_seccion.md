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
