## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE AQUI CITA EL FICHERO DEL QUE SALE Y SE RECONSTRUYO CONTANDO ESE
FICHERO** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO). El cierre corrio
**el ciclo entero de Gate 0 otra vez**, nunca `run_phase1.py` a secas, con sus
**8 comandos en su orden y los 8 en `EXITCODE 0`**.

| cifra | valor | de que fichero se cuenta |
|---|---|---|
| marcador, en su forma canonica | `A 551`, `B 72`, `C 5`, `D 2760`, `n = 3388`, `huecos: 0`, `dups(puesto): 0`, y **0** lineas que no son JSON | `docs/loop/SALIDA_V203_CIERRE_MEDICIONES.txt`, bloque C |
| veredictos, por las dos convenciones | `0a77b5a35a962621` **al entrar y al salir** | bloque `D` de la apertura y bloque `B` del cierre |
| serie `R.n` | **56, 0, 0, `R.65`** al abrir y **58, 0, 0, `R.67`** al cerrar | `SALIDA_V203_SERIE_APERTURA.txt` y `_CIERRE.txt` |
| nomina de la bateria | **135**, que calza con el congelado de `AUDITOR.md` 6.3 | bloques `F` de apertura y `E` de cierre |
| censo de arneses | **197**, con **2** fuera de la nomina con la vara **148** y **62** sin vara | los mismos bloques |
| ficheros que esta vuelta anade a `scripts/loop/` | **13**, y **0 de los 13** entra en el censo | bloque `E` del cierre, comprobado uno a uno |
| deuda del `4.9` del acta 201 | eran **8**, quedaban **6** y quedan **4**: las **177, 178, 179 y 180** | `SALIDA_V203_T4_REGISTROS.txt` |
| inventario de salidas de la vuelta | **32** al cierre, **0** de cero bytes | bloque `H` del cierre |
| rutas que este reporte publica como prueba | **28** distintas, **27 vivas**, **1 ausente** y **0** de cero bytes | bloque `J` del cierre |
| cabecera tallada | **11 filas de tabla** | `SALIDA_V203_TALLADOR_CABECERA.txt` |
| `docs/PENDIENTES.md` al cierre | **1131953** bytes en disco y **1131953** normalizado a LF | bloque `G` del cierre |
| `docs/plan/OPERACIONES.jsonl` al cierre | **513043** bytes en disco y **513043** normalizado a LF | bloque `G` del cierre |

**LA UNICA RUTA AUSENTE ES `docs/loop/SALIDA_V203_BATERIA.txt`, Y NO ES UNA CAIDA
DE CIFRA:** es **el hueco declarado y medido** de la seccion 9, con su nombre,
sus bytes y su atribucion. **No se publica como prueba de nada:** se publica como
la ausencia que es.

**LAS PRUEBAS POR MUTACION DE ESTA VUELTA, CONTADAS DE SUS DOS FICHEROS.**
`docs/loop/SALIDA_V203_T1_CORRECCION_REGISTROS.txt` dice **9 casos, 9 verdes, 0
rojos**, con **4 casos donde la plantilla ancha y la heredada discrepan** y **9
de 9 que caen** con el esperado mutado.
`docs/loop/SALIDA_V203_T4_REGISTROS.txt` **vuelve a correr la misma prueba en vez
de heredar su verde**, y dice lo mismo: **9 casos, 9 verdes, 0 rojos**.

## 4. LO QUE SE TOCO, Y LO QUE NO

**AL ENTRAR**, medido en el bloque `C` de `docs/loop/SALIDA_V203_APERTURA.txt`
**antes de la primera operacion**: `git status --porcelain` daba **1** linea, que
era el propio fichero del sello; y `git diff --numstat -- dataset/` daba **0**
filas.

**LO QUE ESTA VUELTA ESCRIBIO, Y NADA MAS:**

- `docs/PENDIENTES.md`, en **cuatro** sitios y **solo por adicion**: la
  correccion declarada dentro de `R.63` y de `R.64`, y las entradas nuevas `R.65`
  y `R.66`. Mide hoy **1131953** bytes en disco y **1131953** normalizado a LF.
- `docs/plan/OPERACIONES.jsonl`, en **1 sola linea**, la **41**, y en **1 sola
  clave**, `verificacion`. Mide hoy **513043** bytes en disco y **513043**
  normalizado a LF.
- `docs/loop/REPORTE.md`, este fichero.
- `docs/loop/reportes/REPORTE_V202.md`, el archivado del reporte anterior, que la
  guarda del PASO 0 exige antes de pisar nada.
- **13** ficheros nuevos en `scripts/loop/`, **todos con prefijo `_v203_`,
  `_gen_v203_` o `vuelta203_`**, y **ninguno de los 13 entra en el censo**,
  comprobado uno a uno en el bloque `E` del cierre.
- Y **un solo fichero permanente**: `scripts/loop/vuelta184_tarea1a_registrar_acta184.py`,
  al que se le anadio **un parametro opcional** cuyo valor por defecto es la
  expresion que ya tenia dentro. **Va marcado como discutible.**

**LO QUE NO SE TOCO, Y SE MIDE EN VEZ DE AFIRMARSE:** **0 filas de `numstat`** en
`dataset/`, `web/`, `engine/` y `docs/plan/` al cerrar, las cuatro; **ningun
campo `estado`** (0 de las 71 fichas); **ninguna clase y ningun veredicto**, con
el `sha256` de su sede identico al entrar y al salir; **ninguna ficha cerrada**;
**la nomina sin podar y sin crecer**; y **ningun arnes, guarda ni lector
permanente nuevo**.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` TOQUE UN FICHERO PERMANENTE BAJO LA MORATORIA, Y ES LO MAS CERCA DE UNA
PARADA QUE ENCONTRE.** El ensanche de `R84.claves_entrecomilladas()` vive en
`scripts/loop/vuelta184_tarea1a_registrar_acta184.py`, que **no es un `_v203_`**.
**A FAVOR:** el encargo lo manda con estas palabras, *lo unico que se ensancha es
el patron de clave, y el ensanche va con parametro opcional para que los
llamantes viejos no se toquen*; el valor por defecto es la expresion que la
funcion ya tenia dentro, la prueba por mutacion mide que **la funcion llamada sin
el parametro da lo mismo en los 9 casos**, y **ninguno de sus catorce llamantes
se toco**. **EN CONTRA:** sigue siendo una linea de codigo permanente escrita
bajo una moratoria que dice *no se fabrican arneses, guardas ni lectores nuevos*.
**Sostengo que un parametro opcional que no cambia ninguna conducta no es un
lector nuevo, pero lo marco antes de saber si acierto.**

**`D.2` LA PLANTILLA ANCHA ACEPTA TRES FORMAS Y LA VARA SOLO NOMBRA DOS.** El
`4.1` del acta 202 dice *lleve o no comillas inversas*, y mi plantilla acepta
ademas **el titular markdown `### 4.1`**. **A FAVOR:** esa es la forma real en
que las actas 173 y 174 escriben sus hallazgos, medida antes de escribir el
patron, y sin ella el numeral de hallazgos habria salido **0** sobre secciones
que el acta titula `LOS HALLAZGOS`. **EN CONTRA:** es un ensanche mio sobre la
letra de la vara.

**`D.3` LA REGLA DE CUANDO UN NUMERAL DE CAIDAS ES COMPUTABLE ES MIA.** Decidi
que la cifra de `CAIDA n` **solo vale si ningun encabezado en negrita se le
escapa**, y que si alguno se escapa el numeral se declara **no computable por una
sola forma** con las tres lecturas publicadas. **A FAVOR:** sin esa regla el acta
176 habria publicado **0 caidas del ejecutor** sobre una seccion que ella misma
titula `LA CAIDA DEL EJECUTOR, CON SU NOMBRE`, que es justo el cero falso que la
201 rechazo. **EN CONTRA:** elegir cuando un numeral es computable **se parece a
decidir**, y lo digo sin adornarlo.

**`D.4` CORRI UN INSTRUMENTO SABIENDO QUE PISA UN FICHERO SELLADO.**
`vuelta169_tarea3_op_i_01.py` escribe sobre `docs/loop/RECOMPUTO_V169.jsonl`,
commiteado en la vuelta 169. **A FAVOR:** lo comprobe **antes**, lo dije, y lo
corri con el protocolo del sello (medir, correr, restaurar con `git checkout --`,
remedir), con el `sha256` LF identico en los tres momentos y `git status` sin una
sola linea nueva. **EN CONTRA:** la alternativa conservadora era **no correrlo** y
declarar la clausula 4 sin medir.

**`D.5` PROPONGO QUE `OP-I-01` NO SE CIERRE SIN QUE NINGUNA CLAUSULA SALGA EN
ROJO.** Las cuatro salen sin contraejemplo hoy. Lo que sostengo es que **2 de las
4 no se caerian si el fallo volviera**. **Es una lectura del criterio, no una
medicion**, y por eso va aqui.

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` EL ENSANCHE DE UN FICHERO PERMANENTE BAJO LA MORATORIA, QUE EL ENCARGO
MANDA:** el encargo de esta vuelta ordena el parametro opcional por su nombre, y
la moratoria `AUDITOR.md` 6.3 prohibe fabricar lectores. **Lo hice como el
encargo dice y lo marco en `D.1`.** La pregunta es si eso basta o si un ensanche
de codigo permanente necesita **subir al fundador** aunque un encargo lo mande.
**No lo decido yo.**

**`P.2` LA LECTURA POR LEAD EN NEGRITA, QUE NACIO DE UNA MEDICION DE ESTA
VUELTA:** vive dentro de `scripts/loop/_v203_reparto_de_actas_viejas.py`, con
prefijo de guion bajo y fuera del censo, o sea que por el `4.5` del acta 199 es
**computo de una vuelta**. Pero **es una forma de leer que no existia**. La
pregunta es si un computo de una vuelta puede traer una lectura nueva, o si eso
ya es un lector.

**`P.3` LAS DOS CLAUSULAS DE `OP-I-01` QUE NO SE CAERIAN NECESITAN UNA VARA
ESCRITA**, porque `cobertura` es texto libre en
`docs/plan/INVENTARIO.jsonl`. **Escribir esa vara seria maquinaria, y la
moratoria la prohibe.** Queda nombrada, no fabricada.

## 7. PENDIENTES DE DOCTRINA

**`PD.1` UN REPORTE ARCHIVADO QUE EXISTE PERO NO TITULA SECCION DE PREGUNTAS.**
Los reportes de las vueltas **175** y **176** existen y miden **5953** y **95231**
bytes, pero **ninguno de los dos** trae una seccion de PREGUNTAS (**0**
apariciones en cada uno). La doctrina escrita solo cubre **que el reporte no
exista** (vara del `4.7` del acta 201). Aqui se aplico **la misma vara**,
declarandolo, porque un filtro que no se puede correr no se puede correr por
ninguna de las dos causas; **pero la doctrina no lo dice, y por eso va aqui**.

**`PD.2` LA CONVENCION DE BYTES SIGUE SIN FIJAR, Y ESTA VUELTA TRAE UN EJEMPLAR
NUEVO.** `docs/loop/RECOMPUTO_V169.jsonl` mide **15369** bytes en disco y
**15322** normalizado a LF, y **esas dos cifras no coinciden entre si** porque
`git checkout` lo devuelve con CRLF y la corrida lo habia escrito con LF. **Su
contenido no cambio** y `git hash-object` sobre el disco devuelve el mismo blob
que `HEAD`. Mientras la convencion no se fije, **las dos cifras se publican**,
que es lo que la quinta comprobacion de `cerrar_reporte.py` manda.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE

**LAS CINCO SE CAZARON ANTES DE PUBLICARSE, Y NINGUNA LLEGO A UNA CIFRA DEL
REPORTE.** Van con su nombre porque *una correccion que tapa lo que corrige no se
puede auditar*.

**`C.1`. MI LECTOR DE LA RACHA PUBLICO 199 DONDE VA 4.** Mi patron era
`racha[^\n]*?:\s*(\d+)`, y el primer renglon que trae la palabra `racha` seguida
de dos puntos y un numero es **la lista de vueltas**, `199, 200, 201, 202`, no la
cifra. **El 199 no era una medicion: era el sintoma de leer el renglon de al
lado.** Arreglado leyendo **la etiqueta propia de la cifra**, con el motivo
escrito dentro del codigo y sin borrar lo viejo, y el sello se volvio a correr
entero.

**`C.2`. MI CUENTA DE FILAS DEL `numstat` DEL CICLO PUBLICO 1 CON LAS TRES SEDES
LIMPIAS.** Contaba como fila **el aviso de `git` sobre LF y CRLF**, que va por
`stderr` y mi funcion junta con `stdout`. Arreglado contando **por la forma de
una fila de `numstat`**, dos cifras y una ruta separadas por tabulador.

**`C.3`. EL ELEMENTO DE `OP-L-01` CAMBIABA DE TAMANO ENTRE CORRIDAS.** Media
**11156** caracteres en la primera y **11161** en la segunda. **No era
inestabilidad del computo:** el texto citaba dentro **el nombre del fichero de
salida de cada corrida**. Arreglado fijando la cita a la ruta canonica.
**Lo escrito no cambia**, porque la escritura ya citaba la canonica.

**`C.4`. TECLEE DE MEMORIA LAS ETIQUETAS DE UN INSTRUMENTO AJENO.** Mi primera
tanda de patrones para leer las cifras de `vuelta169_tarea3_op_i_01.py` sacaba
**`(no legible)` en 3 de 4**. Arreglado **leyendo su salida** y ampliando a
**12 etiquetas mas la del veredicto de reproduccion**; re-corrido, **las 13 salen
legibles**.

**`C.5`. ESCRIBI UNA PAREJA DE BYTES QUE LA GUARDA HABRIA DADO POR FALSA.** En la
seccion de la TAREA 1 puse, pegado a `docs/PENDIENTES.md`, **el tamano de
ANTES**, que es exactamente la caida que tumbo el cierre de la 202 dos veces.
**Cazada antes de correr la guarda**, releyendo lo que la 202 escribio sobre si
misma, y arreglada **poniendo detras de la ruta su tamano de HOY** y el de antes
en su propia frase, **igual en el reporte y en la fuente de la que sale**.

**`C.6`. LA GUARDA DEL CIERRE ME TUMBO EL REPORTE CUATRO VECES ANTES DE
DEJARME CERRAR, Y LAS CUATRO TENIA RAZON.** Van una a una, porque un cierre que
solo cuenta el verde final esconde lo que costo. **La primera**, por el numeral
del veredicto: publicaba `CINCO` caidas y el cuerpo, contado, decia **0**, porque
yo escribia las cabeceras como ``**`C.1` TEXTO`` y la guarda las lee con un punto
detras de la clave. **La segunda**, por **4 cifras de bytes sin su pareja**: dos
crecimientos, **un cero escrito con la palabra bytes al lado** y **una cita del
acta vieja** que la guarda leia como
cifra propia; esa cita se cerco, que es lo que era. **La tercera**, por **2
parejas COMPLETAS Y FALSAS**: la frase de la TAREA 1 ponia pegado a
`docs/PENDIENTES.md` **su tamano de aquel momento**, y la TAREA 4 volvio a mover
esa sede, asi que al cierre el disco decia otra cosa. **La guarda tenia razon y
la frase estaba mal**, no al reves. **La cuarta**, por otra pareja completa y
falsa de la misma especie, esta vez pegando un crecimiento de `0` a la ruta de un
fichero que mide **8644** bytes.

**COMO SE ARREGLARON, Y ES LO QUE IMPORTA:** **nunca quitando una cifra**. Se
juntaron las cifras con su pareja en el mismo renglon, se cerco lo que era cita,
y **detras de cada ruta quedo SU tamano medido**, con el intermedio dicho sin
nombrar la ruta y **el del cierre pegado a ella en la seccion 3**, que es donde
una guarda que recomputa del disco lo puede cotejar. **Los arreglos se aplicaron
IGUAL en el reporte y en las fuentes de las que sale**, y despues se comprobo que
las cuatro secciones de tarea siguen dentro del reporte **byte a byte**.

**LAS SEIS SON DE INSTRUMENTO O DE REDACCION MIA, NINGUNA DE DATO**, y las seis
tienen su arreglo escrito dentro del codigo o del texto que las produjo.
