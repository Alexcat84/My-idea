## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA FILA DE ESTA TABLA CITA EL FICHERO DEL QUE SE CUENTA** (`EJECUTOR.md` 1,
LA TABLA SE CUENTA DE SU FICHERO). Ninguna celda esta tecleada de memoria.

| que | cifra | de que fichero se cuenta |
|---|---|---|
| entradas de la serie `R.N`, antes y despues | **51** y **52**, 0 colisiones y 0 huecos en las dos | `SALIDA_V200_T1A_REGISTRO_R60.txt` |
| numerales del acta 199 | **5** adjudicaciones, **4** hallazgos, **4** preguntas, **2** caidas del auditor, **3** del ejecutor | `SALIDA_V200_T1A_REGISTRO_R60.txt` |
| cuerpo del acta 199, acotado hoy | lineas **69878** a **70229**, **352** lineas | `SALIDA_V200_APERTURA.txt`, bloque `H` |
| prueba de la guarda de idempotencia | **7** casos, **7** verdes, **0** rojos, **7 de 7 CAEN** al mutar el esperado, **1** discrepa contra la guarda vieja | `SALIDA_V200_T1A_REGISTRO_IDEM.txt` |
| sede de las tres correcciones, antes y despues | disco **48688** y LF **48688** con `sha256` `e88a05f2d64c791f`; disco **54251** y LF **54251** con `sha256` `a32272ff36524041` | `SALIDA_V200_T1B_CORRECCIONES_EN_SU_SEDE.txt` |
| lineas anadidas y borradas en esa sede | **104** anadidas, **0** borradas | `git diff --numstat` corrido en esta vuelta |
| las nueve selladas del 183, preservadas | **9** copias identicas, **0** distintas, **0** ausentes, **9** originales intactas | `SALIDA_V200_T2_PRESERVAR_LAS_NUEVE.txt` |
| reparto de la bateria | **11** tramos sobre **135** entradas, tamano **13** | `SALIDA_V200_T2_PLAN_APERTURA.txt` |
| lo que `--siguiente` decia antes de correr | **9** por hechos, **2** que faltan, siguiente el **10** | `SALIDA_V200_T2_SIGUIENTE_APERTURA.txt` |
| cobertura de la bateria | **135** de **135**, **0** sin correr, **0** ajenas, **0** repetidas | `SALIDA_V183_BATERIA.txt` |
| salida unica de la bateria | disco **92570** y LF **92570**, **1424** lineas, `sha256` LF `aac5f56abac9e758` | `SALIDA_V183_BATERIA.txt` |
| reloj de la bateria | **34.2** minutos sumados de las once celdas, contra una estimacion de **44.6** a **58.0** | las once `SALIDA_V183_BATERIA_TRAMO_N.txt` y `SALIDA_V200_T2_PLAN_APERTURA.txt` |
| entradas que no mordieron | **1** de **135**, `vuelta185_tarea1c_mutacion_bateria_continuada.py` | `SALIDA_V183_BATERIA_TRAMO_9.txt` |
| casos declarados en la corrida | **2**, los dos del tramo 1 | `SALIDA_V183_BATERIA_TRAMO_1.txt` |
| ancla perdida, sin reproducir, ruido de concurrencia | **0**, **0** y **0** en los once tramos | las once `SALIDA_V183_BATERIA_TRAMO_N.txt` |
| racha de cierres | **1**, con la vuelta **199** | `SALIDA_V200_APERTURA.txt`, bloque `E` |
| deuda de la serie al cerrar | **9** actas de la 173 a la 199 sin entrada propia | `serie_de_registros.py` recorrido al cerrar la TAREA 1 |

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO EN ESTA PROSA.**
`docs/loop/SALIDA_V200_APERTURA.txt`, bloque `C`, publica las dos cifras del
estado del arbol con la redaccion exacta que la guarda coteja, y aqui se repiten
LEIDAS de ella:

`git status --porcelain` 1 linea al entrar, que era el propio bloque de apertura
todavia sin commitear.

`git diff --numstat -- dataset/` 0 filas al entrar.

**La apertura sellada no se toco al cierre ni una vez.**

**LO QUE SE TOCO:**

- `docs/PENDIENTES.md`: la entrada `R.60` del acta 199, anadida al final.
- `docs/loop/reportes/REPORTE_V199.md`: **tres avisos de una linea** y **un bloque
  de correcciones declaradas** al final. **104 lineas anadidas y 0 borradas.**
- `scripts/loop/`: el bloque de apertura, el esqueleto, el bloque de cierre (los
  tres **clones declarados**), los tres computos de un solo uso con prefijo de
  guion bajo y los dos cuerpos de tarea.
- `docs/loop/`: las salidas selladas de esta vuelta, las **once** de la bateria
  con su transcripcion de lanzador, la salida unica, las **nueve copias
  preservadas** en `preservadas/v183/`, y el reporte.
- **Las salidas selladas que los propios arneses de la nomina re escriben al
  correr**, que son suyas y estaban ya rastreadas.

**LO QUE NO SE TOCO, Y SE MIDE EN VEZ DE PROMETERSE:**

- **`dataset/` no se toco a mano.** El `numstat` contra `HEAD` sale con **0
  filas** al entrar y **0 al salir**, medido en `SALIDA_V200_CICLO_NUMSTAT_APERTURA.txt`
  y en `SALIDA_V200_CICLO_NUMSTAT_CIERRE.txt`. **Y la bateria lo remidio ella sola
  veintidos veces mas**, al entrar y al salir de cada uno de los once tramos, con
  `guarda_y_restauracion()`, y las veintidos dan **cero filas**.
- **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se movio.** Disco **4054129** bytes y
  LF **4054129** bytes, `sha256` `0a77b5a35a962621` por disco y por LF, **al
  entrar y al salir**.
- **`web/` y `engine/` en cero filas de `numstat`**, y **`docs/plan/` tampoco se
  movio**: la correccion de la `C.2` y la `C.3` **mide** `docs/plan/10_INVENTARIO.md`
  y **no lo edita**.
- **La nomina no crecio ni se podo**: **135** al entrar y **135** al salir, con
  `CASOS_DECLARADOS` en **2**. **Los dos arneses que quedan fuera siguen fuera.**
- **`AUDITOR.md` no se toco**, aunque su `6.1` diga NUEVE tramos y hoy sean ONCE:
  es del fundador.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` LA SEDE DE LAS TRES CORRECCIONES.** Elegi
`docs/loop/reportes/REPORTE_V199.md`, o sea **el reporte archivado**, porque es
donde viven las tres cifras. **Se puede leer de otra manera**: que la sede sea la
entrada `R.60`, o el reporte de esta vuelta. **Escribi en la que contiene el
texto falso**, que es lo que "cada una EN SU SEDE" dice mas literalmente, y
**anadi ademas el aviso en el propio parrafo** para que nadie lea la cifra vieja
sin ver que hay correccion. **Va marcado.**

**`D.2` CORREGIR LA CIFRA Y NO LA ETIQUETA EN LA `C.2`.** El encargo pide elegir
y decir cual. **Elegi la cifra**, con el motivo escrito en el bloque: la etiqueta
del parrafo dice *el literal* y esa etiqueta es la correcta para la clausula que
mide. **Se podia haber elegido lo contrario** y llamar a la cifra *"lineas que
nombran un hueco"*. **Publico las dos con sus patrones y sus lineas**, asi que
quien discrepe tiene delante las dos. **Va marcado.**

**`D.3` NO CLONAR EL LANZADOR DE LA BATERIA.** El encargo lo deja abierto
(*"NO SE CLONA salvo que decidas lo contrario con su motivo escrito"*) y **segui
el defecto**. **El coste esta medido y no es cero**: las once salidas selladas de
esta corrida se llaman `SALIDA_V183_...` y dicen **BATERIA DE LA VUELTA 183**
dentro, y **eso tumbo el bloque `F` de `vuelta185_tarea1c_mutacion_bateria_continuada.py`**.
**El propio docstring del lanzador nombra `vuelta200_bateria_por_tramos.py` como
el clon que arreglaria eso sin tocar codigo.** No lo hice porque el defecto del
encargo es no clonar y porque la moratoria pesa del mismo lado. **Va marcado, y
es el discutible mas gordo de esta vuelta.**

**`D.4` CORRER LOS ONCE TRAMOS AUNQUE EL PRIMERO SALIERA EN ROJO.** El lanzador
imprime *"AQUI SE PARA"*. **Lo lei como "no se re-corre ESE tramo", no como "la
bateria se abandona"**, y el precedente lo respalda: **la vuelta 194 corrio sus
diez tramos con exitcode 1 en los diez**. Ademas el encargo dice **CORRE LOS ONCE
TRAMOS** con todas sus letras. **Va marcado.**

**`D.5` LA CAIDA PROPIA `C.P1` LA CUENTO COMO MIA Y NO COMO ANECDOTA.** Mi guarda
de idempotencia escribio una entrada duplicada. **Nunca se commiteo** y esta
revertida y medida, pero **la escribo como caida** en vez de contarla como un
tropiezo del camino. **Puede que el auditor la clasifique de otra especie.**

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` LOS DOS ARNESES FUERA DE LA NOMINA CONVIERTEN LA BATERIA ENTERA EN ROJO,
Y ESO NO ESTABA DICHO.** El congelado de `AUDITOR.md` 6.3 y la regla de entrada
de la nomina, escrita en `verificar_mutaciones_viejas.py` desde la vuelta 148 y
aceptada por el acta 176 punto 7.2, **se contradicen**: mientras el congelado
dure, **ningun tramo puede salir verde**. **Va como PARADA en la seccion 8.** Lo
que no se: si el remedio es podar, ensanchar el congelado, o que la bateria
distinga *rojo de mutacion* de *rojo de censo* en su exitcode. **Ninguna de las
tres la decido yo.**

**`P.2` `vuelta185_tarea1c_mutacion_bateria_continuada.py` TIENE UN BLOQUE CON
SUJETO VIVO.** Su bloque `F` afirma un reparto que lee del `git log` de nueve
ficheros que **cualquier vuelta de bateria que no clone el lanzador vuelve a
sellar**. **Su esperado no ha dejado de ser correcto; su premisa si.** El remedio
puede ser congelar su sujeto o clonar el lanzador, y las dos son decisiones de
codigo que la moratoria me prohibe tomar. **Tambien va como PARADA.**

**`P.3` LA `C.1` NO SE PUEDE CERRAR DEL TODO Y SE DICE.** La correccion queda
escrita y la cifra remedida, pero **el segundo arnes sigue sin correr y seguira
sin correr** mientras el congelado dure. **La correccion arregla el papel, no el
hueco de cobertura.**

**`P.4` LA 198 SIGUE SIN REGISTRO Y SIN REPORTE ARCHIVADO.** Medido hoy:
`docs/loop/reportes/REPORTE_V198.md` **no existe**, y la 198 **no tiene entrada
propia** en la serie. **No lo arreglo por mi cuenta** porque el encargo nombra el
acta 199 y solo esa, y fabricar el archivado de un reporte que nadie guardo seria
inventarme el texto. **Quien la tome, la registra.**

## 7. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Las dos sub-tareas se ejecutaron con reglas escritas y citadas
por numero. Lo que no cabia en una regla vigente salio como **pregunta** en la
seccion 6 o como **PARADA** en la 8, en vez de resolverse por mi cuenta.

## 8. LO QUE LA 201 RECIBE, Y LAS DOS PARADAS

**PARADA `1`: LA BATERIA NO PUEDE SALIR VERDE MIENTRAS DURE EL CONGELADO.** Los
once tramos salen con **exitcode 1** y el motivo es el mismo en los once y **no
sale de ninguna mutacion**: **2 arneses que el censo VE y la nomina NO tiene**,
`vuelta197_tarea2_mutacion_orden_del_turno.py` y
`vuelta199_tarea1_mutacion_guardas_revividas.py`. **La regla de entrada de la
nomina y la moratoria `6.3` se contradicen**, y `AUDITOR.md` 0 dice que cuando
una guarda contradice una decision escrita del fundador, **la que se corrige es
la guarda**. **No la corrijo yo**: es codigo, y la moratoria lo prohibe. **Se
escribe como PARADA y no se arregla.**

**PARADA `2`: UN BLOQUE DE ARNES CON EL SUJETO VIVO.** El bloque `F` de
`vuelta185_tarea1c_mutacion_bateria_continuada.py` sale `NO MORDIO` porque **esta
misma vuelta re sella los nueve ficheros cuyo `git log` el bloque afirma**. Sus
otros seis bloques calzan enteros y sus casos caen al mutar el esperado, **asi
que la guarda esta viva**. **Es la consecuencia medida de no clonar el lanzador**,
que es lo que el encargo manda por defecto.

**LO QUE LA 201 SE VA A ENCONTRAR, Y SE DICE PARA QUE NO LO REDESCUBRA:**

- **la nomina mide 135 y CALZA con el congelado**, con `CASOS_DECLARADOS` en 2, y
  **el censo reconoce 197 arneses**;
- **2 arneses del censo quedan fuera de la nomina con la vara 148**, y son
  `vuelta197_tarea2_mutacion_orden_del_turno.py` y
  `vuelta199_tarea1_mutacion_guardas_revividas.py`; **sin vara son 62**. **Las dos
  cifras van juntas**, porque un numero solo al lado de un censo de 197 y una
  nomina de 135 se lee como cobertura total y es cobertura desde la vara arriba;
- **el siguiente libre de la serie es `R.61`**, con 0 colisiones y 0 huecos;
- **la 198 sigue sin entrada propia y sin reporte archivado**, medido hoy;
- **las nueve selladas de la 183 viven preservadas** en
  `docs/loop/preservadas/v183/`, identicas byte a byte a las de su corrida, **y
  las que llevan ese nombre en `docs/loop/` son ya las de esta vuelta**;
- **el trabajo de plan que la 199 adjudico y la cadencia aparto de aqui sigue
  entero**: la **CORRECCION DECLARADA de la evidencia de `OP-I-01`** (ficha 323
  contra fichero 672, adjudicacion `4.1` del acta 199, **NO ES PARADA**) y la
  **MEDICION DE `OP-L-02` CONTRA SU `verificacion`, no contra su `evidencia`**
  (adjudicacion `4.2`). **Ninguna de las dos se empezo en esta vuelta.**

**Y SIGUEN FUERA, NOMBRADAS:** la guarda de codigo del hallazgo `5.3` del acta
194; `acumulan()` que lea la tabla; el cotejo de clon declarado; **que hacer con
las filas `B` del archivo**, que el hallazgo `5.1` del acta 199 vuelve a poner
encima de la mesa; y **los puestos que dos o tres lectores independientes
fallaron**, nombrados y medidos y no resueltos, porque mover una clase es del
RECOMPUTO.

**UNA COSA MAS QUE VA DICHA PORQUE SE HIZO A MANO.** `cerrar_reporte.py` salio
**VERDE con sus cuatro piezas** y **compone el la seccion 9 el solo**, sin admitir
texto anadido. El punto `2.f` del encargo manda **nombrar los dos arneses EN LA
SECCION 9**, asi que ese parrafo **se escribio despues del cierre**, y **no se
quedo sin comprobar**: `docs/loop/SALIDA_V200_REVERIFICACION_DEL_CIERRE.txt` vuelve
a correr **las mismas guardas puras de `cerrar_reporte.py`, importadas y no
copiadas**, sobre el fichero tal como queda en disco, y da **0 cifras sin pareja,
0 descartes de cobertura, 0 motivos de la seccion 4, 0 citas de arnes que no
calzan, 0 guiones largos y 0 medios**, con **las siete secciones presentes**, **el
cuerpo del cierre byte a byte dentro** y **los dos literales del reporte sin
cerrar ya fuera**. **Ninguna guarda se afloja: se re corren.**
