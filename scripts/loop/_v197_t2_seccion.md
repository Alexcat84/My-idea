### TAREA 2, EL ORDEN DEL TURNO DEL AUDITOR PASA A CODIGO. CERRADA. 49 DE 49 EN VERDE, Y UNA CAIDA MIA QUE CAZO MI PROPIA GUARDA.

**Sobre `scripts/loop/apertura_del_auditor.py`, que NO SE CLONA.** Instrumentos y
ficheros de salida, **y toda cifra de abajo se cuenta de ellos**:
`docs/loop/SALIDA_V197_T2_MUTACION_ORDEN_DEL_TURNO.txt` (6491 bytes),
`docs/loop/SALIDA_V197_T2B_CIERRE_DEL_TURNO_197.txt` (3480 bytes),
`docs/loop/SALIDA_V197_T2C_GUARDA_MARCADOR_ACTA_197.txt` (2364 bytes),
`docs/loop/SALIDA_V197_T2_QUIEN_BORRA_LA_SEDE.txt`,
`docs/loop/SALIDA_MARCADOR_AUDITOR_V197.json` (102 bytes).

**(a) `leer_reporte()` APUNTA SU TOQUE Y CAE EN ROJO.** La decision vive en
`puede_leer_reporte()`, pura y probable sin escribir un fichero, y el orden
obligatorio pasa a ser `sellar()` -> clasificar -> `--declarar-clases` ->
`leer_reporte()`. **Un turno SIN sello sigue pudiendo leer el reporte**, y eso se
prueba en dos casos. Con sello y sin clases, `leer_reporte()` levanta
`ReporteFueraDeOrden`: es excepcion y no valor de vuelta **porque una cadena vacia
devuelta en silencio es la degradacion que el banco `9` prohibe**. La guarda vale
**entre procesos**, con el sello leido de DISCO, que es la unica forma de que no se
esquive arrancando otro.

**(b) EL FICHERO DEL TURNO SE CIERRA, Y CERRAR NO ES BORRAR.** `cerrar_turno()`
escribe en el fichero un registro `cerrados[vuelta]` con el motivo, la ruta de las
clases y **la bitacora tal como quedo**, y marca el bloque vivo como cerrado. Un
turno nuevo lo carga como CERRADO y **empieza limpio sin borrar nada**. Medido en
procesos de verdad: el turno 2 heredaba `git log, git status, REPORTE.md` y **no
podia sellar**; tras el cierre, el turno nuevo entra con la bitacora **vacia**, ya
**puede sellar**, el fichero **sigue en disco** y el **sello en disco no se toco**.
**LA GUARDA NO SE PIERDE AL LIMPIAR:** declarar dos veces la misma vuelta sigue
cayendo, ahora por `cerrados` y **tambien entre procesos**.

**(c) LA GUARDA DE LA `C.A1`, QUE VA POR SU TERCERA ACTA SEGUIDA.**
`sellar_marcador()` sella la salida de `AP.marcador()` de una vuelta, y
`guarda_del_marcador()` exige que la cifra que un acta publica calce con ella.
**Corrida sobre el acta 197 REAL**, no sobre un texto fabricado: cuerpo acotado en
esa corrida, lineas **69341 a 69635**, y `3388 filas; A 551, B 72, C 5, D 2760`
calzan con la salida sellada. **Y las CINCO mutaciones sobre el acta real cayeron
las cinco** (las filas y cada una de las cuatro clases), mas el caso de **no haber
salida sellada**, que es exactamente lo que la `C.A1` es.

**CASO POSITIVO POR MUTACION: 49 casos, 49 verdes, 0 rojos**, con las dos
direcciones corridas en cada pieza (**sin el remedio la guarda deja pasar, con el
no**) y con la sede de verdad del turno medida antes y despues.

**`C.1` CAIDA MIA, DE METODO, DECLARADA Y CAZADA POR MI PROPIA GUARDA.** La primera
version del arnes restauraba `AP.RUTA_DEL_TURNO` a su sede **antes** de llamar a
`AP.olvidar_todo()`, y `olvidar_todo()` **borra el fichero del turno**: el arnes se
llevo por delante `docs/loop/_TURNO_DEL_AUDITOR.json`, que media **329 bytes** con
`sha256` LF `7203f39fd7f5a54f`. **Lo cazo el ultimo caso del propio arnes**, el que
mide la sede antes y despues. El orden ya esta corregido con su motivo al lado, y
la sede se reconstruyo **por el carril** con `vuelta197_tarea2b_cerrar_turno_197.py`,
del contenido que el bloque `D.1` del sello de apertura publico **antes de la
primera operacion**. **El fichero nuevo no se hace pasar por el original: se
escribe CERRADO y lleva el motivo dentro**, y mide **801 bytes**, `sha256` LF
`69dfc4b6c6854d39`.

**HALLAZGO QUE NADIE ENCARGO, MEDIDO Y NO SUPUESTO.** Corridos **5** arneses de la
nomina que tocan este modulo, **1 BORRA la sede del turno**:
`scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py`, que llama a
`AP.olvidar_todo()` contra el modulo real **sin redirigir `AP.RUTA_DEL_TURNO` a un
temporal**. Los otros cuatro la dejan intacta byte a byte. **Es la misma leccion
que la 193 le aplico a `olvidar_todo()` y la 194 al arnes de la 192, y a este no se
le aplico nunca.** **NO LO REPARO**, porque reparar un arnes de la nomina no esta
encargado en esta vuelta. Consecuencia dicha sin adorno: **mientras eso siga asi,
cada corrida de la bateria vuelve a dejar sin sede el turno del auditor**, y el
remedio de la `2.b` no se puede ver en produccion aunque este entero en el codigo.
Los cuatro arneses heredados siguen en VERDE.

**DISCUTIBLES MARCADOS, ESCRITOS ANTES DE SABER SI ACIERTO.**

**`D.4` DISCUTIBLE MARCADO. `leer_reporte()` APUNTA SU TOQUE AUNQUE LUEGO CAIGA.**
Un intento bloqueado deja `REPORTE.md` en la bitacora sin que se haya leido nada.
Lo sostengo porque el modulo dice desde la 182 que `apuntar()` va **antes** de
hacer la cosa, y porque apuntar de mas **solo puede hacer las guardas mas
estrictas**. Lo discutible es que la bitacora deja de ser un registro de lo hecho y
pasa a serlo de lo intentado.

**`D.5` DISCUTIBLE MARCADO. LA CONSTANCIA DEL CIERRE VALE COMO PRUEBA DE QUE LAS
CLASES SE ESCRIBIERON.** Sin esa via, cerrar el turno bloqueaba **para siempre** la
lectura del reporte de esa vuelta, porque el sello sigue en disco y la memoria de
las clases se limpia. **Lo cazo el arnes y no yo**. Lo discutible es que un registro
del propio fichero del turno se acepte como prueba: quien pudiera escribir ese
fichero se auto concederia el permiso. **El sello en disco no tiene ese problema y
la ruta de clases si.**

**`D.6` DISCUTIBLE MARCADO. RECONSTRUI LA SEDE DEL TURNO QUE MI ARNES BORRO.** La
alternativa era dejarla sin existir y declarar la perdida. Reconstrui porque el
contenido estaba medido y sellado antes de la primera operacion, y porque un
auditor sin sede empieza distinto. Lo discutible es que **un fichero reconstruido
por el ejecutor esta en la sede que prueba el turno del auditor**, aunque se escriba
cerrado, con su motivo dentro y sin hacerse pasar por el original.
