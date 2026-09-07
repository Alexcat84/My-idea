### TAREA 1, CERRADA. LAS DOS GUARDAS APAGADAS, VUELTAS A ENCENDER Y PROBADAS DONDE SE ESCAPARON

**LA PRUEBA VIVE EN `docs/loop/SALIDA_V199_T1_GUARDAS_REVIVIDAS.txt`, 26 casos,
26 VERDES, 0 ROJOS**, contados de ese fichero con `grep -E "CASOS:"` en esta
vuelta. El arnes es
`scripts/loop/vuelta199_tarea1_mutacion_guardas_revividas.py`, y **parte del que
el auditor dejo escrito**, `scripts/loop/_auditor_v198_guarda_muerta.py`, del que
copia el proceso hijo, el constructor de escenarios y la medicion de la sede.
**Lo que cambia son los esperados:** aquel salia verde probando que las guardas NO
mordian; este sale verde probando que SI muerden.

**LAS DOS EXIGENCIAS DEL ENCARGO SE CUMPLEN Y SE MIDEN:** cada paso corre en un
`subprocess` propio (**cuatro procesos distintos por escenario**), y todos los
escenarios se montan sobre un turno **CERRADO** (`vivo.abierto: false`), que es el
estado exacto en que la 197 dejo la sede.

**`1.a` REABRIR EL TURNO. La marca de cerrado SE CONSUME AL CARGARLA.** El
remedio va en `_cargar_turno()` (linea que reabre tras `_reiniciar_memoria()`) y
en `_apuntar_sello()`. **La memoria SIGUE reiniciandose**, o sea el turno nuevo
sigue empezando limpio, que era el remedio entero de la 197; lo unico que cambia
es que **el turno nuevo queda VIVO en vez de nacer muerto**.

**`1.b` `puede_leer_reporte()` MIRA EL DISCO TAMBIEN SIN `vuelta`**, por
`sello_mas_reciente_en_disco()`, que devuelve el sello de vuelta mas alta que hay
en el directorio. Con `vuelta` manda `vuelta`; sin ella manda el sello del disco;
y la clave del cierre (`_CERRADOS`) **se computa** en vez de exigirse por
parametro, para que la rama nueva no bloquee para siempre el reporte de una vuelta
cuyas clases si se declararon.

**LA MUTACION, QUE ES LO QUE HACE QUE ESTO SEA PRUEBA Y NO AFIRMACION.** Se copia
el modulo a un temporal, se le quitan los remedios por sustitucion de texto, y se
corren LOS MISMOS escenarios contra la copia mutilada. **Cada `viejo` se cuenta
antes: si no aparece exactamente una vez, el arnes cae sin medir nada.**

| mutacion | que quita | que pasa, medido |
|---|---|---|
| **A** | `_cargar_turno()` deja de reabrir | la bitacora ya NO acumula (`['git status', 'REPORTE.md']` en vez de los tres) y un toque anterior al sello ya NO cierra `puede_sellar()` |
| **B** | `_apuntar_sello()` deja de reabrir | con la `A` fuera y la `B` puesta el sello SOBREVIVE; con las dos fuera el sello SE TIRA |
| **C** | `sello_mas_reciente_en_disco()` devuelve vacio | `leer_reporte()` sin `vuelta` vuelve a DEJAR PASAR |
| **TOTAL** | las tres | reproduce las CUATRO medidas del auditor de la 198: sello no sobrevive, bitacora no acumula, cero prohibidos vistos, y la lectura pasa |

**DOS COSAS QUE ESTE ARNES APRENDIO EN ROJO CONTRA SI MISMO, Y VAN ESCRITAS
PORQUE SON LA MITAD QUE LO HACE VALER.** Su primera corrida salio **18 de 23**, y
los cinco rojos eran suyos y no del remedio:

1. **LA `B` NO SE VE SOLA.** Con la `A` puesta, `_cargar_turno()` ya reabre el
   turno antes de que la cola del sello llegue, asi que quitarle su linea no
   cambia nada medible. **Se mide contra la `A` ya quitada** (`mut_A` contra
   `mut_AB`). Un remedio que solo se ve cuando el otro falta sigue siendo un
   remedio, pero **decir que se prueba solo seria falso**.
2. **LA `C` NO SE VE EN EL ESCENARIO LARGO**, por el motivo simetrico: con la `A`
   puesta el sello sobrevive EN MEMORIA y la guarda cae por la memoria antes de
   mirar el disco. **Se mide en su escenario propio**, que es ademas el estado
   exacto del auditor de la 198: turno cerrado, memoria en blanco, y el sello en
   el disco al lado.

**Y UNA CAIDA MIA, `C.1`, DECLARADA SIN TAPAR LO QUE CORRIGE.** Mi primera version
del proceso hijo **COPIABA** dentro de si las cuatro lineas de la cola de
`sellar()`, igual que hacia el arnes del auditor. **Una copia no se entera de las
mutaciones que se le hacen al original**, asi que la MUTACION `B` salia ROJA
midiendo mi hijo y no el modulo. La salida honesta no era aflojar el caso: fue
sacar esas cuatro lineas a `_apuntar_sello()` en el modulo y **llamarla**. El
comportamiento de `sellar()` no cambia; lo que cambia es que ahora se puede probar.

**LO QUE NO SE AFLOJA, Y ES LA MITAD QUE IMPIDE QUE LA GUARDA SEA UNA PARED:** dos
casos propios miden que un turno cerrado **CON su constancia** (`cerrados[199]` con
su `ruta_clases`) **SI puede leer**, y que un turno **sin sello en ningun sitio**
tambien.

**LA SEDE DE VERDAD NO SE MOVIO**, y va con su ruta delante y con las dos convenciones, porque la de bytes no esta fijada:
`docs/loop/_TURNO_DEL_AUDITOR.json` mide 789 bytes en disco y 789 normalizado a LF, con `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir del arnes.

**LOS CUATRO ARNESES HEREDADOS QUE MIRAN ESTE MODULO SE CORRIERON DESPUES DEL
CAMBIO**, y sus veredictos se leen de sus ficheros: `vuelta192_tarea4` VERDE,
`vuelta193_tarea4e` VERDE, `vuelta194_tarea2c` VERDE (14 de 14) y
`vuelta197_tarea2c` VERDE. El quinto, `vuelta197_tarea2_mutacion_orden_del_turno.py`,
**salio ROJO 48 de 49 y se resolvio sin aflojar nada**: va en su propio apartado
de abajo.

**`D.1` EL ROJO DEL ARNES DE LA 197, Y POR QUE NO ES UNA REGRESION.** Su caso
*"SIN sello: SI puede leer el reporte"* llamaba a `puede_leer_reporte()` a secas.
Ese arnes prometia en su docstring **"TODO SOBRE UN TEMPORAL"** y era **verdad a
medias**: redirigia `AP.RUTA_DEL_TURNO` pero **no `AP.LOOP`**. Mientras la guarda
solo mirara el disco CON `vuelta`, eso no se notaba; desde la `1.b` una llamada a
secas dentro de ese arnes leia **los sellos REALES de `docs/loop/`**. **La premisa
del caso, no su esperado, era lo que habia dejado de ser cierto.** Se arreglo
completando el sandbox y **anadiendo un caso en vez de sustituir ninguno**: el
original se mide ahora contra un directorio SIN sellos y sigue esperando `True`, y
al lado entra el que la `1.b` hace nacer, *"sin sello en memoria pero CON sello en
disco: ya NO puede"*, que espera `False`. **Ese arnes pasa de 49 a 52 casos, 52 en
verde, y ningun esperado se aflojo.**

**`P.1` UNA PREGUNTA QUE NO CONTESTO YO, Y VA MARCADA.** No corri
`_auditor_v198_guarda_muerta.py` despues del remedio, **a proposito**: sus diez
casos estan escritos para salir verdes sobre el agujero, asi que ahora saldrian
rojos, y correrlo **pisaria `docs/loop/SALIDA_V198_GUARDA_MUERTA.txt`, que es la
prueba sellada del auditor**. Su bloque `MUTACION TOTAL` de mi arnes reproduce sus
cuatro medidas una a una. **No esta en la nomina de la bateria** (medido: la nomina
no lo nombra), asi que la 200 no lo va a correr. **Si el auditor quiere que su
arnes quede invertido en vez de citado, eso lo decide el, no yo.**
