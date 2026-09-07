### TAREA 2, CERRADA. EL ARNES QUE BORRABA LA SEDE DEL TURNO, Y LAS SEIS LLAMADAS

**LA CIFRA DE LAS SEIS NO SE HEREDO: SE CONTO HOY.** El bloque `H.1` del sello de
apertura de esta vuelta corrio el conteo ANTES de la primera operacion, y dice
**6 llamadas a `AP.olvidar_todo()`**, en las lineas **153, 175, 190, 213, 232 y
262**, y **CERO menciones de `RUTA_DEL_TURNO`** en todo el fichero. Calza con las
seis que el acta 198 nombra. Fuente: `docs/loop/SALIDA_V199_APERTURA.txt`.

**LA REPARACION CUBRE LAS SEIS, Y NO CINCO, PORQUE ES DE MODULO Y VA ANTES DE LA
PRIMERA.** `AP.RUTA_DEL_TURNO` se redirige a un `mkdtemp` justo despues del
`importlib.reload(AP)` y se restaura en el bloque final. Una redireccion por
llamada habria dejado seis sitios donde olvidarse de uno; una de modulo delante de
todas no los tiene. **Y se redirige tambien `AP.LOOP`**, por una razon que el
propio fichero declaraba mal y que va abajo.

**EL CASO ROJO ESTA DENTRO DEL ARNES Y ES SUYO:** mide la sede en bytes y `sha256`
al entrar y al salir, y **suma un fallo si se movio**. Ninguna de las dos cifras es
una constante literal: las dos salen de `sede_medida()`. Corrida de hoy, leida de
`docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt`:
**`789 bytes, sha256 52a780c072700280`** al entrar y **lo mismo** al salir,
**`CIFRA fallos: 0`, VEREDICTO VERDE**. Los catorce casos que ese arnes ya probaba
siguen enteros: ningun esperado se aflojo y ningun escenario se quito.

**LA PRUEBA DE MUTACION DEL CASO ROJO, QUE `EJECUTOR.md` 1 EXIGE**, vive en
`docs/loop/SALIDA_V199_T2_MUTACION_SEDE.txt`, **9 casos, 9 VERDES**, y la corre
`scripts/loop/_v199_t2_mutacion_sede.py`. Va en fichero aparte y con prefijo `_`
por un motivo que se dice: **la mutacion es destructiva por naturaleza**, y la sede
esta en `.gitignore`, o sea que **git no la puede devolver**. Meterla dentro del
arnes de la nomina dejaria un arnes que destruye la sede cada vez que la bateria
pasa, que es exactamente lo que esta tarea repara. **No entra en la nomina**
(congelada en 135) y el censo no lo cuenta por el prefijo.

| paso | que se le quita al arnes | que se mide |
|---|---|---|
| **M1** | solo la REDIRECCION | **la GUARDA muerde**: exitcode 1 y la sede queda intacta, `sha256 52a780c072700280` |
| **M2** | la redireccion **Y** la guarda (el arnes tal como estaba antes de esta vuelta) | **la sede QUEDA PISADA**: `52a780c072700280` al entrar contra `31ddfaad65791b63` despues |
| **restauracion** | (nada) | la sede vuelve **byte a byte** y se **REMIDE**: `52a780c072700280` |

**`C.2` UNA CAIDA MIA EN ESTA MISMA PRUEBA, DECLARADA SIN TAPAR LO QUE CORRIGE.**
Mi primera version media **la EXISTENCIA** del fichero y esperaba que
desapareciera. Salio **ROJO**, y tenia razon: `olvidar_todo()` BORRA el fichero,
pero **el `apuntar()` siguiente LO VUELVE A CREAR** con la bitacora del arnes
dentro. **Medir la existencia daba VERDE sobre una sede PISADA**, que es el fallar
callado que el banco `9` prohibe. **La vara pasa a ser el contenido**, y con ella
el caso muerde. Lo que el acta 198 llama "borra la sede" es, medido de cerca,
**la borra y la reescribe con otro contenido**: el fichero sigue ahi y ya no es el
del auditor. **La diferencia importa** porque una guarda que solo mire si el
fichero existe habria dado verde.

**`D.2` Y UNA SEGUNDA CAPA QUE NO SABIA QUE ESTABA MIDIENDO, PUBLICADA COMO CASO.**
La `M1` se escribio esperando que borrara la sede, y **no la borra**: salta la
guarda que la propia reparacion dejo puesta (*"si la redireccion no se aplico, NO
se sigue: borraria la sede"*). **Eso no es un fallo de la mutacion, es una capa de
mas**, y por eso la mutacion se parte en dos en vez de darse por buena.

**`D.3` LA PROMESA DEL DOCSTRING QUE ERA FALSA, Y AHORA ES CIERTA.** Ese arnes
declara desde la vuelta 183 que **"este fichero NO ABRE `docs/loop/REPORTE.md` en
ninguna linea"**, y su bloque `B` llama a `AP.leer_reporte()`, que **lo abria**.
Con `AP.LOOP` redirigido al temporal, la afirmacion pasa a ser cierta y el bloque
`B` deja de depender de los sellos de la sede real. **Se declara aqui en vez de
corregirse callando**, porque una promesa de docstring que nadie mide es una cifra
sin vara.

**LA FECHA SE CUMPLE:** la bateria corre en la **200** con la nomina congelada en
**135**, y este arnes esta **dentro** de esa nomina (medido: `VMV.VIEJAS` lo nombra
en la linea 847 de `scripts/loop/verificar_mutaciones_viejas.py`). **Cuando la 200
lo corra, ya no se llevara la sede por delante.**
