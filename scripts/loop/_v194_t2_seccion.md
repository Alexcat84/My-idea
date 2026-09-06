### TAREA 2. LOS DOS ARNESES DE LA CUARTA PUERTA. **CERRADA, LOS TRES ESCENARIOS DEL AUDITOR INVERTIDOS, Y CON UNA PREMISA SUYA QUE NO SE SOSTIENE Y QUE PUBLICO IGUAL.**

**LA TABLA DEL AUDITOR Y LA DE HOY, UNA DEBAJO DE OTRA.** La suya vive en
`docs/loop/_auditor_v194_cuarta_puerta_rota.txt`; la de hoy sale contada de
`docs/loop/SALIDA_V194_T2G_TRES_ESCENARIOS.txt` (3671 bytes en disco y 3671
normalizado a LF, `sha256` `56481dd977310ceb` por las dos convenciones), **13
casos, 13 pasan, 0 fallan, VEREDICTO VERDE**, cifra que ese fichero publica de si
mismo en su linea `CIFRA casos`:

| escenario, con el fichero del turno PUESTO | lo que medio el auditor | lo que mide hoy |
|---|---|---|
| solo el arnes de la **192** | exit 0, verde, y el turno **BORRADO** | exit 0, y el turno **EXACTAMENTE como estaba** |
| solo el arnes de la **193** | exit 1, **ROJO**, turno EXISTE | **exit 0, VEREDICTO VERDE**, turno como estaba |
| los dos, en el orden alfabetico de la bateria | 192 verde, 193 verde, turno **BORRADO** | los dos verdes, turno como estaba |

**Y EL COTEJO QUE DE VERDAD DECIDE, PORQUE UN VEREDICTO SE PUEDE CREER Y UN
`sha256` NO:** la salida sellada de cada arnes es **la misma corrido solo y
corrido en compania**. El de la 192 da `ee605b4b8450c484` en los dos escenarios;
el de la 193 da `1cb7f216c650b06f` en los dos. **Si el verde de uno siguiera
prestado del otro, la diferencia estaria dentro de su salida.**

**LO QUE SE ARREGLO, PIEZA POR PIEZA.**

**(a) EL ARNES DE LA 192 YA NO TOCA LA SEDE DE VERDAD.** Se le anade, antes de su
primer `olvidar_todo()`, la redireccion de `AP.RUTA_DEL_TURNO` a su temporal, que
es exactamente para lo que esa variable es de modulo, con el mecanismo que el
arnes de la 193 ya usaba. **Y no basta con redirigir:** el arnes mide ahora la
sede de verdad **al entrar y al salir**, con existencia, bytes y `sha256`, y
**CAE EN ROJO si cambia**. Un arnes que promete no tocar algo y no lo comprueba es
lo que dejo pasar este agujero.

**(b) EL ARNES DE LA 193 YA NO EXIGE QUE EL FICHERO NO EXISTA.** Su caso `H`
comprobaba `os.path.exists(turno_real) == False`, o sea **pedia que no hubiera
auditor**. Ahora mide la sede **antes** (bloque `0`, nuevo) y **despues** (caso
`H`) y **cae si CAMBIA**. La funcion `medir_turno_real()` devuelve **las tres
cosas a proposito**: un fichero borrado y reescrito con el mismo tamano tiene el
mismo `existe` y los mismos `bytes`, y **solo el `sha256` lo delata**.

**Y AQUI APARECIO UN SEGUNDO FALLO, QUE NO ESTABA EN EL ENCARGO Y QUE ERA LA
CAUSA DE VERDAD.** Con `(a)` y `(b)` puestos, el arnes de la 193 **seguia saliendo
en rojo** con el turno puesto, y no por su caso `H`: por sus casos `A`, `B` y `E`.
La causa, medida y no supuesta: `apertura_del_auditor.py` carga el turno **AL
IMPORTAR**, y `_cargar_turno()` **se iba dejando la memoria como estuviera cuando
el fichero no existia**. Eso la convertia en un MEZCLADOR y no en un cargador, y
rompia lo unico para lo que `RUTA_DEL_TURNO` es de modulo: **un proceso hijo que
redirige la ruta a un temporal y vuelve a cargar seguia viendo el turno de la sede
de verdad**. Medido: sus hijos entraban con `['x']` en la bitacora en vez de
vacios. **Arreglado con la vara escrita entera y con sus dos lados:** si el fichero
**no existe**, el disco dice que no hay turno y la memoria se reinicia; si el
fichero **existe pero no se puede leer**, eso no es "no hay turno" sino un fichero
roto, y **la memoria NO se toca**, porque tirar el estado vivo por un JSON corrupto
seria perder la prueba en silencio.

**(c) EL CASO POSITIVO POR MUTACION, Y LANZA PROCESOS DE VERDAD.**
`scripts/loop/vuelta194_tarea2c_mutacion_sede_del_turno.py`, salida en
`docs/loop/SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt` (3687 bytes en disco y
3687 por LF, `sha256` `b014e233a5e7512d` por las dos convenciones), **14 casos, 14
pasan, 0 fallan, VEREDICTO VERDE**, contados de su propia linea `CIFRA casos`.
**Su caso rojo no es una constante comparada consigo misma:** escribe en un
temporal un **culpable fabricado** de cuatro lineas que reproduce el fallo exacto
de antes de esta vuelta (importa el modulo y llama a `olvidar_todo()` sin redirigir
nada), lo lanza **como proceso**, y **el detector lo caza: `LA BORRO`, con
exitcode 0**. Si el detector no lo cazara, el arnes cae. **Lanzar procesos de
verdad es la mitad que importa:** la sede se resuelve al IMPORTAR el modulo, asi
que un arnes importado desde el mismo proceso heredaria la redireccion de otro y
el agujero no se veria.

**(d) LA SEDE DEL TURNO NO SE PUEDE VOLVER A COMMITEAR.** La via es `.gitignore`,
que es lo natural, **porque lo que hay que impedir es que ENTRE EN EL INDICE y eso
lo decide git**. Y la comprobacion tambien la hace git y no una lectura del fichero
de reglas: `git check-ignore -v` sale con exitcode 0 y nombra la regla
`.gitignore:43`, y `git ls-files` devuelve vacio. Las dos son casos del arnes `c`.

**(e) NO SE CLONO NINGUNO DE LOS DOS FICHEROS: SE LES ANADIO**, con el bloque
nuevo delimitado y comentado con la fecha y el hallazgo que lo motiva, y **el
texto viejo del caso `H` se dice en el comentario en vez de borrarse sin rastro**.

**(f) LA NOMINA NO SE TOCO.** Sigue en **127 entradas**, medidas con
`len(VMV.VIEJAS)` en el bloque `H` de la apertura y otra vez al escribir esto.

**LAS DOS SALIDAS SELLADAS SE RE SELLAN, Y EL CORTE VIEJO SE GUARDA AL LADO**, que
es la forma que la `4.9` del acta 194 declara correcta:

| salida sellada | corte VIEJO (blob de `edff6568`) | corte NUEVO |
|---|---|---|
| `SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt` | 4282 bytes, `sha256` `4779fcd04bc5b2da` | 5153 bytes en disco y 5153 por LF, `sha256` `ee605b4b8450c484` por las dos convenciones |
| `SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt` | 4613 bytes, `sha256` `10c2d2d1e9eb06ce` | 5023 bytes en disco y 5023 por LF, `sha256` `1cb7f216c650b06f` por las dos convenciones |

**Y COMO TOQUE `apertura_del_auditor.py`, RE CORRI LOS TRES ARNESES DE LA NOMINA
QUE LO VIGILAN**, antes de la bateria y no confiando en que ella los pille:
`vuelta182_tarea2_mutacion_apertura_auditor.py`,
`vuelta160_tarea6b_mutacion_puerta.py` y `vuelta162_tarea2a_mutacion_puerta.py`.
**Los tres con exitcode 0 y ninguna de sus salidas selladas cambio**, medido con
`git status --porcelain -- docs/loop/`, que solo lista las dos que esta tarea re
sella a proposito.

**LA PREMISA DEL ENCARGO QUE NO SE SOSTIENE, PUBLICADA SALGA LO QUE SALGA.** El
hallazgo `5.1` del acta 194 dice, literal, que los dos arneses *"son entradas
suyas"* de la nomina y que por eso *"uno de sus nueve tramos publicaria un verde
prestado"*. **Corrido hoy sobre `VMV.VIEJAS`, ninguno de los dos esta en la
nomina:** `vuelta192_tarea4_mutacion_cuarta_puerta.py` da `False` y
`vuelta193_tarea4e_mutacion_sello_entre_procesos.py` da `False`, y **la vuelta mas
alta nombrada en las 127 entradas es la 190**. O sea que **la bateria de esta
vuelta no los habria corrido**, y el verde prestado no habria llegado a ningun
tramo. **La reparacion se hizo igual y no me arrepiento de haberla hecho**, porque
la mitad de abajo del hallazgo si estaba: **el arnes de la 192 borraba de verdad el
turno vivo del auditor en su sede de verdad, con exitcode 0 y sin avisar**, y eso
es cierto lo corra quien lo corra. **Lo que no es cierto es el camino por el que
llegaba.** No lo adjudico ni lo clasifico: lo mido, lo publico y lo marco abajo.
**Y no toco la nomina para hacerlo calzar**, que era la otra salida y esta
expresamente prohibida.
