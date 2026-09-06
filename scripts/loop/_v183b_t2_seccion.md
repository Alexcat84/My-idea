### TAREA 2. LA BATERIA POR TRAMOS: 5 DE 9 SELLADOS, Y EL TRAMO 5 EN ROJO PARA LA VUELTA

> **ESTA TAREA NO CIERRA, Y LA FILA LO DICE.** El encargo de la continuacion la
> manda hasta los nueve y con el cierre del reporte detras, y termina en el
> **TRAMO 5 DE 9** porque el propio encargo lo ordena con estas palabras: *"Si
> un arnes cae en rojo, te detienes ahi y lo traes con su salida entera"*. Es
> ademas el precedente de la casa: el TRAMO 6 de la bateria de la 176 paro
> igual, y su commit lo escribio asi, *"la guarda que muerde es informacion, no
> un estorbo"*.

**LA TABLA SE TALLA DE LOS FICHEROS Y NO SE TECLEA** (`EJECUTOR.md` 1, LA TABLA
SE CUENTA DE SU FICHERO). Instrumento
`scripts/loop/_v183b_tallar_tabla_tramos.py`, salida
`docs/loop/SALIDA_V183_T2_TABLA_TRAMOS.txt`, pegada entera:

| tramo | fichero | bytes disco | bytes LF | lineas | sha256 LF | exit | minutos | se atribuye a | lineas con 176 | entradas |
|---:|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| **1** | `SALIDA_V183_BATERIA_TRAMO_1.txt` | **9116** | 9116 | 120 | `96bec3628ebc63c6` | **0** | 2.1 | **183** | 1 | 13 |
| **2** | `SALIDA_V183_BATERIA_TRAMO_2.txt` | **7352** | 7352 | 114 | `eb9f0fc446152400` | **0** | 3.8 | **183** | 1 | 13 |
| **3** | `SALIDA_V183_BATERIA_TRAMO_3.txt` | **7406** | 7406 | 114 | `cc356b7e22ccb987` | **0** | 3.7 | **183** | 1 | 13 |
| **4** | `SALIDA_V183_BATERIA_TRAMO_4.txt` | **7421** | 7421 | 114 | `2c606409febaed94` | **0** | 1.0 | **183** | 1 | 13 |
| **5** | `SALIDA_V183_BATERIA_TRAMO_5.txt` | **6975** | 6975 | 115 | `687884431e56820d` | **1** | 0.6 | **183** | 1 | 13 |
| **6** | `SALIDA_V183_BATERIA_TRAMO_6.txt` | **NO EXISTE** | | | | | | | | |
| **7** | `SALIDA_V183_BATERIA_TRAMO_7.txt` | **NO EXISTE** | | | | | | | | |
| **8** | `SALIDA_V183_BATERIA_TRAMO_8.txt` | **NO EXISTE** | | | | | | | | |
| **9** | `SALIDA_V183_BATERIA_TRAMO_9.txt` | **NO EXISTE** | | | | | | | | |

**CIFRA tramos con salida sellada no vacia: 5 de 9.** Los veredictos de cada
tramo, contados del mismo fichero: **ancla perdida 0 en los cinco**, **no
reproducible 0 en los cinco**, **no mordio 0, 0, 0, 0 y 1**. Las cinco
transcripciones de lanzador miden **3.064, 3.118, 3.167, 3.177 y 3.276 bytes** y
ninguna esta vacia.

**LA ATRIBUCION, QUE ERA LA CAIDA `E.1`, QUEDA REPARADA Y REMEDIDA SOBRE LAS
SALIDAS NUEVAS.** Los cinco tramos se atribuyen a la vuelta **183** en su primera
linea. Las menciones de `176` pasan de **3 por fichero** a **1 en cada salida de
bateria** y **0 en cuatro de las cinco de lanzador**. **Las que quedan son citas
historicas y estan nombradas una a una:** en las de bateria, la linea del reparto
en tramos, que vive en `verificar_mutaciones_viejas.py:1872` y no en el lanzador;
en la del lanzador del tramo 5, la linea *"(encargo de la vuelta 176, TAREA
1.f)"*, que **solo se imprime cuando un tramo sale en rojo** y por eso no aparece
en los otros cuatro. **La cuenta no baja a cero y se dice por que, en vez de
publicar un cero limpio que no seria verdad.**

**EL RELOJ SE MIDE AL CERRAR CADA TRAMO Y LA ESTIMACION SE DICE COMO ESTIMACION.**
Medidos: **2,1 + 3,8 + 3,7 + 1,0 + 0,6 = 11,2 minutos** para 65 entradas. El
`--plan` de hoy **estimaba** entre **4,3 y 5,6 minutos por tramo de 13** y entre
**36,6 y 47,7 para la nomina entera; la medicion va por debajo de la horquilla en
cuatro de los cinco tramos**, y el tramo 5 no cuenta para esa comparacion porque
paro en rojo.

**`dataset/` NO SE MUEVE, MEDIDO AL ENTRAR Y AL SALIR DE CADA TRAMO.**
`git diff --numstat -- dataset/` da **CERO filas** en las diez mediciones (cinco
de entrada y cinco de salida), y ademas la guarda del propio lanzador lo remide
por su cuenta en sus pasos 1, 2 y 5 y publica **LIMPIO AL ENTRAR** en los cinco.

---

## PARADA: EL ARNES `vuelta165_tarea2_mutacion_censo.py` NO MUERDE, Y NO LO ARREGLO YO

**EJECUTOR.md 5:** *"Paras SOLO si algo contradice una regla vigente o una cifra
publicada con su corte: en ese caso lo escribes en el reporte como PARADA y no lo
arreglas tu"*. Aqui pasa exactamente eso, y por partida doble: una cifra
**tecleada dentro de una guarda** contradice la medicion de hoy.

**QUE FALLA, EXACTAMENTE UN CASO DE TRECE.** El caso
`A_el_patron_VIEJO_no_ve_dos_de_su_propia_nomina`. El arnes lleva **tecleada** una
lista esperada de **DOS** ficheros:

```
esperadas = ["vuelta144_3c_caso_positivo_1190.py", "vuelta147_3e_simular_a26.py"]
```

y `nomina_invisible_al_censo(patron=PATRON_ARNES_VIEJO)`, corrida hoy, devuelve
**CINCO**: esas dos mas `vuelta150_2d_simular_op_c_05.py`,
`vuelta160_tarea3b_caso_positivo.py` y
`vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py`. **Los otros doce casos
PASAN y los trece CAEN al mutar su esperado**, o sea que el arnes esta sano: lo
que envejecio es su cifra.

**NO LO CAUSA LA ENTRADA QUE ESTA VUELTA ANADIO, Y ESTA MEDIDO EN VEZ DE
SUPUESTO.** Corrida la misma funcion sobre la nomina de hoy (**112 entradas**) y
sobre esa misma nomina **sin** `vuelta183_tarea1b_mutacion_atribucion.py`
(**111**), la lista sale **identica**, las mismas cinco. El arnes de esta vuelta
lleva la palabra `mutacion` en el nombre y el patron viejo **si** lo ve.

**CUANDO SE PUSO EN ROJO, LOCALIZADO EN GIT Y NO RECORDADO.** En la ultima bateria
con cuerpo, la de la vuelta **176**, este arnes salio **exit 0 OK**
(`docs/loop/SALIDA_V176_BATERIA_TRAMO_6.txt`, linea 50). Los dos commits que
metieron las tres entradas nuevas en la nomina, **`d4a1028c`** (las dos primeras)
y **`a462306f`** (la tercera, en la vuelta 182), **NO son ancestros** del commit
que sello aquel tramo, **`cd5aa065`**: corrido `git merge-base --is-ancestor`, los
dos salen **POSTERIORES**. **Y desde entonces ninguna bateria llego hasta aqui:**
cero bytes en la 171, la 172 y la 173, la 181 cortada antes de lanzarla y la 183
cortada en el tramo 2. **Este rojo llevaba esperando desde antes de la 182 y esta
es la primera corrida que lo alcanza.**

**POR QUE NO LO TOCO.** Actualizar la lista esperada para que calce con la
medicion de hoy es **resolver la discrepancia copiando**, que es lo que
`EJECUTOR.md` 2 prohibe con todas las letras; y es ademas la mano que afloja una
guarda en la unica vuelta que existe para correrlas. **Lo que sostengo es la
medicion, no el remedio:** el arnes dice la verdad y su cifra esta vieja, pero
**cual es la reparacion buena no es mia**. Hay al menos dos caminos que no son
equivalentes y no elijo entre ellos: que la lista se **compute** de la nomina en
vez de teclearse, o que el caso deje de mirar la nomina real y mire una
**fabricada**, que es lo que hacen sus otros doce casos.

**LO QUE ARRASTRA, DICHO ENTERO Y SIN SUAVIZAR.** Con la bateria en **5 de 9**,
`--componer` **no puede** armar `docs/loop/SALIDA_V183_BATERIA.txt`, y sin esa
pieza `scripts/loop/cerrar_reporte.py` **no puede cerrar el reporte de la 183**.
Asi que **este reporte queda partido y sin archivar por segunda vuelta seguida**,
la TAREA 2 **sin cerrar**, y **el disparador del regimen `6.2` sigue sin
cumplirse**. No lo disimulo con un cierre a mano: un cierre tallado sin su pieza
seria justo la especie de verde que esta casa lleva vueltas persiguiendo.

---

## LOS DISCUTIBLES MARCADOS, ANTES DE SABER SI ACIERTO

**El acta 183 midio que el reporte de la 183 no marcaba ninguno** (`grep -c -i
discutible` daba **0**). Estos van marcados **antes** de la relectura ciega.

**`PD.1` LA FILA DE LA TAREA 3 EN VEZ DE UNA TAREA 1 NUEVA.** El encargo de la
continuacion llama TAREA 1 a los registros, y la tabla ya tenia una TAREA 1
cerrada. Entra como **TAREA 3** con su celda diciendolo. **Lo discutible es si
eso es lo correcto o si habria que haber renumerado**; sostengo que no, porque
renumerar pisa una fila ya auditada, pero **es juicio mio y no sale de ninguna
regla escrita**.

**`PD.2` EL SUFIJO `183B` DE LAS SALIDAS DEL BLOQUE DE APERTURA.** Las salidas
del trabajo llevan `SALIDA_V183` porque son de la 183; las del bloque de apertura
de esta sesion llevan **`183B`** para no pisar las de la primera sesion, de las
que el acta 183 ya tiro. **Lo discutible es el nombre**, no la decision de no
pisar. Ninguna regla escrita dice como se nombra la apertura de una continuacion.

**`PD.3` EL PATRON DEL GUARDA SE ENSANCHO UNA VEZ.** `_PATRON_CLAVADO` paso de
pedir `V` mayuscula sin separador a `(?:vuelta|v)[ _]?(\d{3})` con
`re.IGNORECASE`, **porque su propio arnes lo tumbo con dos casos que el defecto
real traia**. Esta declarado en el comentario del patron y medido, pero
**ensanchar un patron es exactamente lo que esta casa desconfia**, y por eso va
marcado: la contrapartida es que las citas legitimas se eximen **nombrandolas**
con `CITA HISTORICA`, y hoy hay **una sola** exencion en todo el fichero.

**`PD.4` LOS DOS PREFIJOS DE `mkdtemp` NO ESTABAN EN EL ENCARGO Y SE CAMBIARON
IGUAL.** El encargo nombra las lineas **181, 217, 218, 359 y 360**. Las lineas
**198 y 516**, los prefijos `v176_tramo` y `v176_lanzador`, **no las nombra**, y
sin embargo **imprimian dos de las tres menciones de `176` de cada salida de
lanzador**. Se cambiaron porque si no, la reparacion no llegaba a lo que la caida
describe. **Va marcado por ir mas alla de la letra del encargo.**

**`PD.5` LA CUARTA RUTA DE LA CELDA DE PRUEBA.** El encargo manda escribir enteras
**tres**; se escribieron **cuatro**, porque la primera tampoco llevaba su carpeta.
Misma especie que el anterior: mas de lo pedido, en la direccion de lo pedido.

**`PD.6` EL ARNES NUEVO ENTRA A LA NOMINA EN SU MISMA VUELTA.** Por la regla del
acta 176 punto 7.2, que la `5.4` del acta 183 acaba de reconfirmar, y con la
medicion delante (`arneses_que_faltan()` daba **1** con el fuera). **Es la tercera
vuelta seguida que se hace esto**, y va marcado por si el auditor considera que la
regla se esta estirando.

**`PD.7` NO ARREGLAR EL ROJO DEL TRAMO 5.** Sostengo que no me toca, por
`EJECUTOR.md` 2 y 5. **Lo discutible es si "no lo arreglas tu" alcanza a una
guarda cuya cifra esta simplemente vieja**, o si eso era reparacion de rutina que
podia hacerse declarandola. **Marcado a mi costa:** si el auditor dice que habia
que arreglarlo, la bateria se quedo a cuatro tramos del final por una decision
mia.
