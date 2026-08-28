## VUELTA 113, TAREA 1: LOS REGISTROS DEL ACTA 112

### 1.1 TU CAIDA DE GUARDA CEGADA, CAIDA DEL EJECUTOR

`tallar_cabecera_reporte.py` decia en su codigo (linea 600 de la vuelta 112)
"El tsc vacio ES la senal de exito (tsc sin salida igual a exitcode 0)":
fichero vacio da la celda "EXITCODE 0, cero lineas", fichero con lineas da "N
linea(s) de salida (revisar)". La vuelta 112 empezo a apendar `EXIT=0` a
TODOS sus ficheros de salida, tsc incluido. Para Gate 0, motor y web es
inocuo (el tallador los parsea con expresiones regulares que ignoran esa
linea); para el tsc mato la guarda entera: `SALIDA_V112_TSC_APERTURA.txt` y
`_CIERRE.txt` pesan 7 bytes y son solo ese marcador (medido contra la
historia: las vueltas 110 y 111 pesan 0 bytes, `git show 27ecfe43:` y
`git show 9aea9f43:`), y la cabecera de la vuelta 112 publico en sus DOS
columnas "1 linea(s) de salida (revisar)" con el tsc real en exit 0 y cero
lineas (corrido por el auditor). Remedio: TAREA 2.1/2.2/2.3 de esta vuelta,
`interpretar_tsc()` descuenta la linea `EXIT=<n>` antes de contar, probado
con mutacion V (verde, solo el marcador) y mutacion W (rojo, una linea de
error real mas `EXIT=1`), `docs/loop/SALIDA_V113_TAREA2_2_3_MUTACION_V_W.txt`.
Repetido sobre la vuelta 112 real: su tsc ya talla "EXITCODE 0, cero lineas"
en las dos columnas.

### 1.2 TU CAIDA DE EXPEDIENTE, EL BARRIDO 2.7 QUE PROMETE "NINGUNO OMITIDO" Y OMITE

El barrido 2.7 de la vuelta 112 declaraba tres busquedas (RE_CITA, el patron
de extension entre backticks, y `LOOP = os.path.join(` en `scripts/loop/*.py`)
y encabezaba "Ninguno omitido de la lista", pero la tercera busqueda,
corrida de verdad, devuelve 57 ficheros (71 en la union de las tres) y la
lista de la vuelta 112 solo nombraba nueve instrumentos vivos mas dos fuera
de alcance: `abrir_tramo_de_opu01.py`, `caso_positivo_del_contrato_de_perdidas.py`
y `registrar_cierre_de_tramo.py` no aparecian ni nombrados ni descartados en
ningun sitio. La CONCLUSION del barrido viejo aguantaba (el unico boquete de
la especie vivia en el instrumento ya corregido: los tres omitidos no
parsean citas de prosa, son rutas fijas), pero la promesa de completitud era
falsa. Remedio: TAREA 2.6 de esta vuelta, barrido rehecho entero con las tres
busquedas corridas por codigo y la union clasificada sin excepcion
(`docs/loop/SALIDA_V113_TAREA2_6_BARRIDO_TALLADORES.txt`).

### 1.3 MI CAIDA DE ENCARGO (DEL AUDITOR), LA LISTA DE MARCAS PARCHEADA POR ENUMERACION POR TERCERA VEZ

La 110 cerro la lista sin "pasa de"; la 111 la amplio enumerando ("pasa de",
"queda en", "quedo en", "daba", "dio"); el reporte de la vuelta 112 escribio
dos afirmaciones de estado anterior con el verbo "sigue"
("`contar_cierre_efectivo.py` sigue 74/109 (59,6%)" y
"`verificar_cobertura_bolsa_tres_vias.py` sigue 74/74/0") y las dos pasaron
invisibles porque "sigue" no estaba en la lista. Es la MISMA especie de
caida, la tercera vez, y el remedio ya no podia ser otra palabra suelta.
Remedio: TAREA 2.4 de esta vuelta, la lista se documenta como REGLA (toda
construccion que afirme un estado anterior o su permanencia) con la
obligacion escrita de que el EJECUTOR sume, en la misma vuelta en que la
escribe, cualquier verbo de permanencia que su propio reporte use y la lista
todavia no traiga. Mutacion X sobre el reporte 112 real
(`git show 87397be1:docs/loop/REPORTE.md`): antes no marca ninguna de las
dos oraciones, despues marca las dos y las evalua con sus citas
(`docs/loop/SALIDA_V113_TAREA2_5_MUTACION_X_ANTES.txt` y `_DESPUES.txt`).

### 1.4 LO QUE NO ES CAIDA

(a) El 3.5 de la vuelta 112 pedia la cifra vieja y la nueva cada una con SU
fichero, y cito uno por vara: no es caida porque el propio 3.5 dice "si no
se mueve ninguno, DILO CON LA CIFRA" y eso es lo que hizo, con `docs/plan/`
intacto como prueba. (b) El doble sello de `HEAD_CIERRE` de la vuelta 112
(`1d8deba4`, el renombre en `03827ad0`, el re-sello en `961fb18c`) es escoria
declarada en los mensajes de commit y corregida DENTRO de la vuelta: no se
publico nada equivocado. (c) La correccion silenciosa del desliz heredado
del acta 97 ("entre los pasos 1 Y 2 de su madre" en vez de "1, 2 y 4"),
anotada A FAVOR del ejecutor por el auditor: coincide con la razon del acta
97 3.2(b) y con la propia madre de tres pasos.

### 1.5 LA COMPOSICION DEL ANADIDO, TALLADA

Extraccion del bloque hecha DESPUES de la ultima edicion de
`docs/PENDIENTES.md` (metodo fijado en la vuelta 112, seccion 1.6 de aquel
bloque). Linea de arranque medida con
`grep -n "^## VUELTA 113, TAREA 1" docs/PENDIENTES.md`, extraccion con
`sed -n '<linea>,$p' docs/PENDIENTES.md > docs/loop/_v113_pendientes_tarea1_solo.md`,
y tallado con
`python scripts/loop/tallar_composicion_salida.py --fichero docs/loop/_v113_pendientes_tarea1_solo.md --patron "^\| (?P<sub>1\.\d) \| (?P<clase>[A-Z_]+) \| (?P<atrib>[A-Z]+) \|$" --clave sub --campo-clase clase --valor-base SIN_CAIDA --etiqueta-base "sin caida" --etiqueta-otra "caida" --clase-cotejo "caida" --lista-citada 1.1,1.2,1.3`
(salida completa en `docs/loop/SALIDA_V113_TAREA1_COMPOSICION.txt`): de los
cuatro subapartados de arriba, TRES son CAIDA (1.1 y 1.2 del EJECUTOR; 1.3
del AUDITOR) y UNO es SIN_CAIDA (1.4). Cotejo contra la lista citada arriba:
SOBRAN NINGUNO, FALTAN NINGUNO. Fidelidad de la extraccion: `git diff` sobre
el anadido real de `docs/PENDIENTES.md` contra este mismo fichero tallado,
en `docs/loop/SALIDA_V113_TAREA1_DIFF_FIDELIDAD.txt`.

| sub | clase | atribucion |
|---|---|---|
| 1.1 | CAIDA | EJECUTOR |
| 1.2 | CAIDA | EJECUTOR |
| 1.3 | CAIDA | AUDITOR |
| 1.4 | SIN_CAIDA | NINGUNO |
