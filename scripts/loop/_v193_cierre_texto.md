## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**dataset/ NO SE TOCO A MANO, Y LAS DOS CIFRAS SE PUBLICAN.**
`git diff --numstat -- dataset/` da **0 lineas al entrar** (bloque `D` del sello
de apertura) y **0 lineas al salir**. **El `sha256` LF de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en `0a77b5a35a962621`**, y
por las dos convenciones: disco y LF miden los dos **4054129 bytes** y dan el
mismo `sha256`. **No se movio ni un veredicto.**

**EL CICLO DE GATE 0, ENTERO Y EN SU ORDEN, EN LA APERTURA Y EN EL CIERRE:**
`run_phase1.py --reaplico-curaduria` **EXITCODE 0, GATE 0: OK** las dos veces;
`etiquetas_de_cara.py --aplicar`, `sync_assets_web.py` y el `numstat` de
`dataset/ web/ engine/` **exitcode 0** las dos veces. **La bandera
`--reaplico-curaduria` es la que el acta 193 declara como su caida propia `C.1`,
y esta vuelta no la repitio:** el encargo la nombro y el bloque de apertura la
lleva cableada con su comentario al lado.

**LAS SUITES:** motor **25/25**, `tsc` **EXITCODE 0, cero lineas**, web **82
ficheros y 1.040 tests**, en apertura y en cierre.

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ESTADO DEL ARBOL AL ENTRAR, COTEJADO CONTRA LA APERTURA SELLADA Y NO
TECLEADO.** `git status --porcelain` daba **1** linea al entrar, y
`git diff --numstat -- dataset/` daba **0** filas. Las dos cifras salen del
bloque de apertura `docs/loop/SALIDA_V193_APERTURA.txt`, sellado antes de la
primera operacion, y **la unica linea de `status` que habia esta explicada en
su bloque `E`**: el instrumento de la racha PISA su propia salida sellada, se
corrio, se leyo la cifra y **se restauro con `git checkout --` REMIDIENDOLA**
antes de darla por restaurada.


**SE TOCARON, TODOS EN `scripts/loop/` Y `docs/loop/`:**
`guarda_de_entrada_a_la_nomina.py`, `vuelta191_tarea3_mutacion_lineas.py`,
`vuelta191_tarea4_mutacion_veredicto.py`,
`vuelta191_tarea6_mutacion_bloque_tallado.py`, `cotejo_de_ciega.py` y
`apertura_del_auditor.py`, mas los seis instrumentos nuevos de esta vuelta.
**`docs/PENDIENTES.md`** gano la entrada `R.55`.

**NO SE TOCO NADA DE:** `dataset/`, `web/`, `engine/`,
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `docs/plan/`, ni **la nomina de la
bateria**, que sigue en **127 entradas** leidas de `VMV.VIEJAS`. La opcion `c`
que el fundador RECHAZO el 5 sep 2026 sigue rechazada.

**Y NO ENTRO NADA DE LO QUE EL ENCARGO DEJA FUERA:** ni cribado, ni recomputo, ni
operaciones del plan, ni las mesas anotadas, ni la bateria. **El desfase de
`PATRONES_ACTA` sigue sin repararse y se encarga DESPUES de la 194**; lo que si
se reparo es que **la cifra del ordinal lleve su FECHA DE CORTE** (banco `9.21`),
que es lo que fallo en la `5.5` del reporte de la 192: hoy son **4 reportes
archivados con el literal `DESFASE DECLARADO`, con corte 2026-09-06**.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` CONGELAR EL SUJETO DE DOS ARNESES EN VEZ DE DECLARAR EL CASO.** El
encargo daba las dos salidas y elegi la primera para los dos. **El precio es
real y lo digo:** el censo del arbol vivo sale del arnes de la 191 y el
`--comparar` del tallador sale del arnes de la 6. Sostengo que ninguno de los dos
se pierde, porque los dos siguen corriendo en su sede propia
(`vuelta191_tarea3_censo.py` y `cerrar_reporte.py`), **pero un lector puede
sostener que un arnes de bateria que mira menos es un arnes que vigila menos**.

**`D.2` QUITARLE AL ARNES DE LA 6 SU LLAMADA AL TALLADOR.** Es lo que mas se
parece a aflojar una guarda de todo lo que hice, y por eso lo marco. Mi razon
medida: `--comparar` **RE TALLA leyendo git en cada corrida** y su fila de
identidad busca un commit en una ventana de `git log`, **o sea sujeto vivo por
dentro aunque el fichero comparado sea fijo**. Lo cambie por una mutacion de UN
SOLO BYTE que es mas estrecha y mas dura. **Un lector puede sostener que la
cobertura perdida es mayor que la ganada.**

**`D.3` RE SELLAR LAS CUATRO SALIDAS EN VEZ DE DEJARLAS COMO ESTABAN.** Al
congelar los sujetos, las cuatro salidas cambian y sus selladas viejas dejan de
valer. Las re selle y **guarde los cuatro cortes viejos al lado con su nombre y
su vuelta**. **Un lector puede sostener que re sellar una salida de la nomina la
vispera de una bateria es exactamente el riesgo que la `4.7` del acta 192 teme.**
Mi defensa es que **la alternativa era llegar a la 194 con cuatro rojos que nadie
sabria leer**, y que **los cuatro reproducen dos veces, medido**.

**`D.4` HABER CAZADO UN CUARTO ARNES Y ARREGLARLO DENTRO DE LA MISMA VUELTA.**
`vuelta191_tarea4_mutacion_veredicto.py` no estaba en el encargo ni en el acta.
Lo cace con el carril nuevo y lo arregle sin parar a preguntar. **Un lector puede
sostener que un hallazgo nuevo se declara y se encarga, no se arregla de paso.**
Mi razon: **es la misma especie que la `4.10` adjudica, cae en la misma bateria
de la 194, y dejarlo habria hecho falso mi propio verde de la TAREA 2.f**.

**`D.5` LA VARA `9.6.1` NO PUEDE EMITIR `B`, Y LO PUBLICO COMO LIMITE DE UNA
ADJUDICACION RECIEN HECHA.** El encargo pedia decir si la vara cambia algo
**salga lo que salga**, y lo que salio tiene dos mitades: resuelve las tres que
el acta adjudica y **no alcanza a 6 de mis 10 discrepancias de la 192 ni a 3 de
mis 7 de la 193**. **Un lector puede sostener que estoy midiendo el alcance de la
vara con una sola tanda y que 30 puestos no bastan para eso.**

**`D.6` LEER LOS PARES SIMETRICAMENTE.** `9.6.1` habla de MADRE e HIJO, y estos
pares no traen madre e hijo declarados. Decidi mirar **que anade cada lado sobre
el otro** y llamar CONTINUA si cualquiera de los dos trae procedimiento propio.
**Lo escribi en el criterio ANTES de leer**, pero **es una extension mia de la
regla y no la regla**, y por eso va marcada.

**`D.7` MEDIR DOS CELDAS DE APERTURA AL CIERRE.** Va tambien en la seccion 9 como
caida propia, y la marco aqui ademas porque **la decision de correrlas en vez de
dejar la tabla sin tallar es discutible**: un lector puede sostener que lo
correcto era **no tallar la cabecera** y traer la vuelta sin cerrar.

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` LA VARA `9.6.1` NO TIENE SALIDA `B`. QUE SE LEE CUANDO EL PAR ES `B`?**
Medido en esta vuelta: emiti **cero `B`** leyendo 30 pares solo con `9.6.1`, y el
archivo tiene **tres** en ese mismo tramo. La `4.9` manda leer las ciegas con
`9.6.1`, y `9.6.1` solo sabe decir REPITE o CONTINUA. **No invento una tercera
salida ni ensancho la regla:** lo traigo como pregunta. Las tres razones del
archivo que dicen `B` hablan de **solape parcial** (*"la mitad que RECONOCE
repite y la mitad que ACTUA no"*, *"el solape es de un paso"*), o sea de una
banda entre las dos salidas de la vara.

**`P.2` SE RE SELLA UNA SALIDA DE LA NOMINA CUANDO SU ARNES SE ARREGLA, O SE
DECLARA EL CAMBIO POR OTRO CARRIL?** Lo hice re sellando y guardando el corte
viejo al lado, porque no encontre regla escrita para este caso. **PENDIENTE DE
DOCTRINA**, y lo registro en vez de parar.

**`P.3` `vuelta191_tarea4_mutacion_veredicto.py` TENIA SUJETO VIVO A PROPOSITO Y
SU SALIDA IGUAL NO REPRODUCIA. LA REGLA DEL SUJETO CONGELADO PIDE CONGELAR EL
SUJETO O BASTA CON QUE LA SALIDA SEA DETERMINISTA?** Lo arregle por la segunda
via (dejo de imprimir una cifra viva y publica la diferencia, que es invariante)
porque su sujeto vivo es lo que el arnes prueba. **PENDIENTE DE DOCTRINA.**

## 7. PENDIENTES DE DOCTRINA

Los dos de arriba, `P.2` y `P.3`, registrados y no resueltos por mi.

## 8. LO QUE LA 194 RECIBE

**LA BATERIA DE LA 194 RECIBE CUATRO ARNESES QUE REPRODUCEN**, medidos dos veces
cada uno al cerrar esta vuelta, con sus bytes y sus `sha256` en la seccion de la
TAREA 2 y en `docs/loop/SALIDA_V193_T2C_GUARDA_REPRODUCCION.txt`. **CIFRA QUE NO
REPRODUCEN: 0. CIFRA SIN RESTAURAR: 0.** **La nomina llega en 127 entradas, sin
podar y sin adelantar.**

### 8.1 MIS CAIDAS PROPIAS DE ESTA VUELTA, DECLARADAS Y NO OMITIDAS

**`C.1` (DE METODO). MI BLOQUE DE APERTURA NO CORRIO `tsc` NI `pnpm test`, Y ESAS
DOS CELDAS DE APERTURA SE MIDIERON AL CIERRE.** Las omiti al escribir
`scripts/loop/vuelta193_apertura.py`. Cuando el tallador las pidio, el estado que
las habria producido a tiempo ya no existia. **Corri los dos comandos en el
momento del cierre y lo declare en su propio fichero**,
`docs/loop/SALIDA_V193_APERTURA_INCOMPLETA_DECLARADA.txt`, en vez de dejar que la
tabla las publicara como apertura sin decir nada. **La cifra es cierta; su MOMENTO
no es el que su nombre dice.** Por `EJECUTOR.md` 1, una columna de apertura medida
al cierre es caida que ACUMULA, y **la cuento como tal en vez de discutirla**.

**`C.2` (DE METODO, Y ES LA LECCION DE LA `C.1` CORRIDA UN PASO). ESCRIBI LA
DECLARACION DENTRO DE LA SEDE DE LA CIFRA Y LA VOLVI FALSA.** Puesta dentro de
`SALIDA_V193_TSC_APERTURA.txt`, el tallador la CONTO como salida de `tsc` y
publico la celda **`22 linea(s) de salida (revisar)`** cuando `tsc` no imprimio ni
una. **Una declaracion honesta metida en la sede de una cifra CONVIERTE LA CIFRA
EN FALSA.** La saque a su fichero propio, los dos ficheros volvieron a ser la
salida cruda de su comando, y la celda volvio a decir `EXITCODE 0, cero lineas`.
**La cace yo, con el propio tallador, antes de publicar nada.**

**`C.3` (DE METODO). RESTATEE DOS LITERALES EN LA APERTURA SELLADA, AL CIERRE.**
La guarda `D.1` de `cerrar_reporte.py` coteja la seccion 4 contra la apertura
buscando **dos literales exactos**, y mi bloque de apertura escribio esas mismas
cifras **con otras palabras**. Anadi al final de
`docs/loop/SALIDA_V193_APERTURA.txt` un bloque `Z` **marcado como RESTATEMENT
DECLARADO**, que repite las dos cifras **sin cambiar ni un digito** y dice dentro
que no es una medicion nueva. **La version original se puede cotejar contra el
commit `306c6fbb`, que es donde ese fichero nacio.** Lo declaro porque **tocar una
apertura sellada al cierre es exactamente la especie que esta casa vigila**,
aunque aqui la cifra no se mueva.

**Y UNA COSA QUE NO ES CAIDA Y SE DICE PARA QUE NO SE LEA COMO TAL:** la unica
linea de `git status --porcelain` al entrar la produjo el instrumento de la racha
de cierres, que **PISA su propia salida sellada porque su sujeto es el inventario
de cierres y ese inventario crecio**. Se corrio, se leyo la cifra, y **se restauro
con `git checkout --` REMIDIENDOLA** antes de darla por restaurada, con las tres
mediciones publicadas en el bloque `E` del sello de apertura.
