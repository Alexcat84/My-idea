## VUELTA 112, TAREA 1: LOS REGISTROS DEL ACTA 111

### 1.1 TU CAIDA DE GUARDA QUE NO ALCANZA, CAIDA DEL EJECUTOR

`tallar_cifras_de_antes.py` resolvia toda cita SIEMPRE con
`os.path.join(LOOP, nombre)`, ciego a la forma `carpeta/NOMBRE.md` que su
propio docstring ya prometia y que usan TODAS Y CADA UNA de las citas del
reporte de la vuelta 111 (`docs/loop/SALIDA_V111_...txt`): la ruta se
resolvia a `docs/loop/docs/loop/SALIDA_...`, no existe, y la cita se
descartaba EN SILENCIO. Sonda de tres lineas
(`docs/loop/_auditor_v111_mut/sonda_backticks.md`), la MISMA oracion con el
MISMO fichero: ANTES del arreglo, VERDE con el nombre pelado (linea 3) y
ROJO FALSO con la ruta delante (linea 4, "0/1 citas ()")
(`docs/loop/SALIDA_V112_TAREA2_3_MUTACION_S_ANTES.txt`); DESPUES, las dos
lineas VERDE e IGUALES (1/1 cada una)
(`docs/loop/SALIDA_V112_TAREA2_3_MUTACION_S_DESPUES.txt`). Consecuencia
doble: su VERDE sobre el reporte de la 111 era VACUO (cero oraciones
marcadas), medido hoy sobre el reporte real
(`docs/loop/SALIDA_V112_TAREA2_4_MUTACION_T_ANTES.txt`, VERDE con 0
oraciones que cumplen la vara). Remedio: TAREA 2, BLOQUEANTE, de esta
vuelta.

### 1.2 TU CAIDA DE EXPEDIENTE, EL DOCSTRING INVERTIDO DE `censar_alcance_de_la_vara.py`

El docstring de modulo decia que se toma "el MAS VIEJO si un puesto aparece
en mas de un fichero". El codigo hace lo contrario y hace bien: sobrescribe
recorriendo los seis ficheros en orden, se queda con EL MAS NUEVO, y es lo
unico que produce el 72/2 publicado. Medido por las dos reglas juntas
(`docs/loop/SALIDA_V112_TAREA2_6_MUTACION_U.txt`): MAS NUEVO 72 OBJETO / 2
SATELITE, MAS VIEJO 70 OBJETO / 4 SATELITE. **La cifra PUBLICADA (72/2) es
la CORRECTA**; lo que estaba mal era la cabecera del docstring, ya
corregida esta vuelta para que diga EL MAS NUEVO.

### 1.3 TU CAIDA DE EXPEDIENTE, EL REGISTRO 1.4 DEL BLOQUE DE LA VUELTA 111

Ver la NOTA DE CORRECCION arriba, bajo el bloque de la vuelta 111: la
composicion verdadera de aquel bloque es 2 CAIDA / 3 SIN_CAIDA, no 3
CAIDA / 2 SIN_CAIDA. Corregido de forma ADITIVA, sin borrar una letra del
texto ni de la tabla viejos.

### 1.4 MI CAIDA DE ENCARGO (DEL AUDITOR), LA LISTA CERRADA SIN "PASA DE"

El encargo 2.1 de la vuelta 110 fijo la lista cerrada de marcas con "pasaba
de" y sin "pasa de": la oracion de la TAREA 2.5 del reporte de la vuelta
111 ("la pasa de OK a hallazgo") hablaba de un estado anterior y no fue
marcada por ese solo hueco. **Es caida de ENCARGO DEL AUDITOR**, heredada.
Consecuencia de doctrina, para que no se lea como contradiccion: esa lista
la cerro un encargo del auditor, no una decision del fundador, asi que
ampliarla es del auditor y no necesita parada; el docstring que decia "no
se amplia sin decision del fundador" queda corregido junto con la lista
(TAREA 2.2 de esta vuelta).

### 1.5 LO QUE NO ES CAIDA, LA CITA UNICA DE LA 2.5

La oracion de la TAREA 2.5 del reporte de la vuelta 111 cita solo
`SALIDA_V111_TAREA2_5_MUTACION_DESPUES.txt` para un antes y un despues. NO
es caida: el "antes" SI esta medido y commiteado en
`SALIDA_V111_TAREA2_5_MUTACION_ANTES.txt`, identico byte a byte (md5
`bcbee0ad30b45164e1305a7102e6c516`) al
`SALIDA_V111_TAREA2_4_CASO_POSITIVO.txt` que la oracion inmediatamente
anterior si cita. Lo que este caso prueba de verdad son los dos boquetes de
1.1 y 1.4, no una caida propia.

### 1.6 LA COMPOSICION DEL ANADIDO, TALLADA

DISCUTIBLE DE METODO de la vuelta 111 (seccion 1.6 de aquel bloque),
adjudicado a favor del ejecutor por el auditor en su acta: la extraccion
del bloque de esta TAREA 1 se hace DESPUES de la ultima edicion de
`docs/PENDIENTES.md`, no antes, para que la copia tallada sea fiel al
bloque final. Linea de arranque medida hoy con
`grep -n "^## VUELTA 112, TAREA 1" docs/PENDIENTES.md`, extraccion con
`sed -n '<linea>,$p' docs/PENDIENTES.md > docs/loop/_v112_pendientes_tarea1_solo.md`,
y tallado con
`python scripts/loop/tallar_composicion_salida.py --fichero docs/loop/_v112_pendientes_tarea1_solo.md --patron "^\| (?P<sub>1\.\d) \| (?P<clase>[A-Z_]+) \| (?P<atrib>[A-Z]+) \|$" --clave sub --campo-clase clase --valor-base SIN_CAIDA --etiqueta-base "sin caida" --etiqueta-otra "caida" --clase-cotejo "caida" --lista-citada 1.1,1.2,1.3,1.4`
(salida completa en `docs/loop/SALIDA_V112_TAREA1_6_COMPOSICION.txt`): de
los cinco subapartados de arriba, CUATRO son CAIDA (1.1, 1.2 y 1.3 del
EJECUTOR; 1.4 del AUDITOR) y UNO es SIN_CAIDA (1.5). Cotejo contra la lista
citada arriba: SOBRAN NINGUNO, FALTAN NINGUNO. Demostracion de que la
extraccion es fiel al bloque final: `git diff` sobre el anadido real de
`docs/PENDIENTES.md` contra este mismo fichero tallado, CERO diferencias
salvo la primera linea en blanco
(`docs/loop/SALIDA_V112_TAREA1_DIFF_FIDELIDAD.txt`).

| sub | clase | atribucion |
|---|---|---|
| 1.1 | CAIDA | EJECUTOR |
| 1.2 | CAIDA | EJECUTOR |
| 1.3 | CAIDA | EJECUTOR |
| 1.4 | CAIDA | AUDITOR |
| 1.5 | SIN_CAIDA | NINGUNO |
