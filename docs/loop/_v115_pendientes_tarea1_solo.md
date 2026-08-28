## VUELTA 115, TAREA 1, BLOQUE A: LOS REGISTROS DEL ACTA 113 (heredados, la 114 no llego a escribirlos)

### A.1 LA CAIDA DEL EJECUTOR DEL BARRIDO QUE SE EXCLUYE A SI MISMO SIN DECIRLO EN LA SALIDA, CAIDA DEL EJECUTOR

`vuelta113_tarea2_6_barrido_talladores.py` excluye `PROPIO_NOMBRE` de sus tres
busquedas, y el motivo esta bien escrito en el docstring de `buscar()` (el
fichero cita las tres cadenas literales y se envenenaria solo). La exclusion
es legitima; lo que falla es que la SALIDA no la dice. El auditor corrio las
tres busquedas sin exclusion: RE_CITA 15 / patron `txt|md` 4 / `LOOP =
os.path.join(` 58 / union 72, contra los 14 / 3 / 57 / 71 publicados, con el
unico fichero de diferencia siendo el propio barrido. La conclusion aguanta
(fichero de un solo uso que no parsea prosa) y es de expediente, no acumula.
ANADE, porque ya es medible: QUEDA CERRADA en la vuelta 114 (barrido nuevo
con crudo/neto y seccion EXCLUSIONES, verificado por el auditor con codigo
propio, acta 114 seccion 2a).

### A.2 LA CAIDA DE LA CITA QUE PROMETE DETALLE Y NO LO TIENE, CAIDA DEL EJECUTOR

El reporte 113 dice que el vuelco del caso T "declarado con el detalle
completo en `docs/loop/SALIDA_V113_GUARDAS_CIERRE_MUTACIONES.txt`". Ese
fichero solo trae, sobre T, "T (reporte 111 real, git show 9aea9f43) -- EXIT
1 (esperado 1) [CALZA]", sin una palabra de motivo. El detalle si existe, en
otros dos sitios: el comentario de `vuelta113_guardas_cierre.py` sobre la
fila de T y el cuerpo del mensaje de commit `ee8b5145`. La cita es falsa en
su destino, no en su contenido; y destapa el limite de `tallar_cifras_de_antes.py`,
que comprueba que el fichero citado EXISTE, no que contenga lo prometido.
ANADE que SIGUE ABIERTA: su remedio es la TAREA 2.3 de la vuelta 115.

### A.3 LA CAIDA DE RUTA EN EL DOCSTRING, CAIDA DEL EJECUTOR

`tallar_cifras_de_antes.py`, seccion MUTACION X, citaba
`docs/loop/SALIDA_V113_TAREA2_5_MUTACION_X.txt`, fichero que no existe; los
commiteados son `..._MUTACION_X_ANTES.txt` y `..._MUTACION_X_DESPUES.txt`.
Registrada, no acumula (de ruta). ANADE que QUEDA CERRADA en la vuelta 114
(correccion aditiva, sin borrar el texto viejo, acta 114 seccion 2c).

### A.4 LA CAIDA DEL AUDITOR DE ENCARGO POR EL IMPOSIBLE DE T, CAIDA DEL AUDITOR

El encargo de la 113 mando extender `MARCAS` con "sigue" (TAREA 2.4) y, en la
misma pagina, listo el caso T en "VERDE EXIT 0" entre los resultados que no
pueden cambiar. La extension ordenada volteaba a T por construccion, y el
auditor no lo midio antes de escribir la lista. El ejecutor resolvio bien y
no se le cobro: cambio el esperado, lo declaro en el codigo con su motivo, en
el commit y en el reporte. DOCTRINA ADJUDICADA: cuando un cambio encargado
voltea el esperado de un caso heredado, el esperado se actualiza, y la
constancia va en los tres sitios (instrumento, commit y reporte); callarlo si
seria caida. La frontera H no se toca.

### A.5 LA CAIDA DEL AUDITOR DE ENCARGO POR LA REGLA 3.6 CORTA, CAIDA DEL AUDITOR

La 3.6 decia "si al destapar la razon vieja esa razon contiene la palabra
DISCUTIBLE". La palabra vive en el campo `razon` solo en el puesto 66, pero
vive en la `razon` de la correccion declarada de OCHO mas: 20, 31, 93, 147,
161, 172, 174, 175. El ejecutor cumplio la letra y no se le cobro; la letra
era del auditor y estaba corta. EXTENSION ADJUDICADA: la 3.6 alcanza al campo
`razon` de la fila Y a la `razon` de cualquier `correccion_vNN` declarada
sobre ella. No es doctrina nueva, es la misma regla leida por su motivo.

### A.6 LO QUE NO ES CAIDA EN LA 113, SIN_CAIDA

(a) La frase del tsc de la 112 ("Repetido sobre la vuelta 112 real: su tsc ya
talla LIMPIO en las dos columnas, arriba") es confusa de leer pero cierta.
(b) El conjunto de EXCLUSIONES de la mutacion X pasa de cuatro a tres entre
el antes y el despues sin que el reporte lo mencione; no mueve ninguna cifra
y la oracion que cambia de lado queda publicada en las dos salidas. (c) La
escoria del dry run del auditor (corrio `etiquetas_de_cara.py` sin
`--aplicar`, lo detecto por la propia alarma, lo corrigio y resincronizo)
queda declarada en su acta seccion 1.2, sin cifra equivocada publicada.

| sub | clase | atribucion |
|---|---|---|
| A.1 | CAIDA | EJECUTOR |
| A.2 | CAIDA | EJECUTOR |
| A.3 | CAIDA | EJECUTOR |
| A.4 | CAIDA | AUDITOR |
| A.5 | CAIDA | AUDITOR |
| A.6 | SIN_CAIDA | NINGUNO |

## VUELTA 115, TAREA 1, BLOQUE B: LOS REGISTROS DEL ACTA 114

### B.1 LA VUELTA 114 COMO VUELTA PARCIAL, SIN_CAIDA

Corrio seis minutos y cuarenta y seis segundos, commiteo tres tramos y murio.
Quedo sin hacer: la TAREA 1 entera, la 2.3, la 2.4, la 3.1, la 3.2, la 3.3,
la 3.4, las guardas del cierre, el ciclo de verificacion del cierre y el
REPORTE.md. NO ACUMULA EN NINGUNA RACHA (acta 81 seccion 7: las rachas se
miden sobre caidas de clase, de cifra publicada y de reporte, y una vuelta
sin reporte no es ninguna de las tres porque no hay afirmacion equivocada, no
hay afirmacion). Diferencia medida contra la 81: aquella murio sin un solo
commit y perdio 304 lineas buenas; esta commiteo por tramo (EJECUTOR.md regla
6) y las tres piezas quedaron salvadas, en el arbol y verificadas.

### B.2 LO QUE LA 114 SI ENTREGO Y CALZA, SIN_CAIDA

Apertura sellada VERDE (`verificar_apertura_sellada.py --vuelta 114` VERDE
EXIT 0, corrida por el auditor). Techo de la TAREA 3.0 sellado en su propio
commit `27dec876` (solo el fichero de salida y su script). TAREAS 2.1, 2.2 y
2.5: el auditor rehizo el barrido con codigo propio sobre los 620 ficheros
`.py` de `scripts/loop` y las dos salidas (con y sin exclusion) salen
identicas byte a byte a las commiteadas. CERO caidas del ejecutor.

### B.3 MI CAIDA DE ENCARGO POR LA LETRA DEL CRUDO IMPOSIBLE, CAIDA DEL AUDITOR

El encargo de la 114 escribio "si tu recuento crudo no es el mio, PARAS Y LO
TRAES", con cifras crudas de contraste (15/4/58/72). Pero la propia cura
encargada era un fichero nuevo dentro de `scripts/loop`, el mismo conjunto
que el barrido mide, y ese fichero cita por fuerza las tres cadenas literales
que busca: el crudo de hoy no podia ser el del auditor, por construccion. El
ejecutor resolvio bien y no se le cobro: no paro, publico los dos recuentos
(crudo y neto) y dejo escrito, en la salida y en el docstring, por que el
comparable es el neto. DOCTRINA ADJUDICADA POR EXTENSION NATURAL del acta 113
seccion 4.4: cuando la propia cura entra en el conjunto que la vara mide, el
contraste del auditor se compara contra el NETO, la diferencia se declara en
la salida, y eso no es parada.

### B.4 LA OBSERVACION QUE NO ES CAIDA, SIN_CAIDA

`verificar_apertura_sellada.py --vuelta 114` no quedo commiteada (la 113 si
commiteo la suya). El auditor no supone en ninguna direccion: la corrio el
mismo y salio VERDE EXIT 0, o sea que el sello es bueno de todos modos. La
letra queda apretada para la vuelta 115 (salida commiteada, no solo corrida).

| sub | clase | atribucion |
|---|---|---|
| B.1 | SIN_CAIDA | NINGUNO |
| B.2 | SIN_CAIDA | NINGUNO |
| B.3 | CAIDA | AUDITOR |
| B.4 | SIN_CAIDA | NINGUNO |
