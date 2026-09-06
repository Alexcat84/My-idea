## 3. LO QUE ESTA VUELTA SOSTIENE, Y NI UNA PALABRA MAS

1. **LA TAREA BLOQUEANTE ESTA HECHA Y LA 189 PUEDE SER UNA VUELTA DE BATERIA
   LIMPIA.** `scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py` abrio la
   vuelta en **ROJO** con `CIFRA fallos: 2` y cierra en **`CIFRA fallos: 0`,
   `VEREDICTO: VERDE`, exitcode 0**. Su caso E **dejo de contar un texto**: ahora
   computa el **inventario de guardas eximidas con sus nombres**, cotejado contra
   una **lista autorizada y escrita** de **dos** entradas, y cae en rojo en **tres**
   casos que van los tres probados.
2. **EL PLAN NO SE MOVIO EN CIFRA Y SI EN EVIDENCIA, Y HAY QUE DECIR LAS DOS
   COSAS JUNTAS.** El `sha256` LF de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y
   cierra en **`0a77b5a35a962621`**: **ninguna clase se decidio y ningun veredicto
   se movio**, y eso era lo mandado. Lo que si se movio es **el estado de las
   cuatro fichas que la vara nombra**, resueltas contra su evidencia documental:
   **dos cubiertas, una cubierta a medias y una PARADA**.
3. **LA VARA DEL PLAN GANO SU PATA DOCUMENTAL EN CODIGO, Y LA CIFRA VIEJA SALE
   IDENTICA.** `CIFRA fichas en LISTA sin ninguna prueba: 6`, de las cuales **4
   son TRABAJO REAL** y **2 estan CONSUMIDAS**, exactamente como antes. **La cifra
   nueva va A SU LADO**: de esas 4, **3 tienen su producto documental en disco y 1
   no**.
4. **LA ESCALADA DE `AUDITOR.md` 1.2 ESTA PUESTA Y CAZA LOS DOS CASOS QUE LA
   TRAJERON.** La guarda de las dos convenciones pasa de ver **3** parejas a ver
   **6** sobre el texto real de `git show 9a06b7c8:docs/loop/REPORTE.md`, publica
   **su cobertura** con las **2** no atribuidas **nombradas una a una**, y la regla
   de la ambiguedad **no se toco**. Y `piezas_que_faltan()` **acusa** las **dos
   secciones `## 9.`** del reporte de la 187, nombrando las lineas **870** y
   **920**, y su desorden contra la `## 10.` de la **877**.
5. **SESENTA PUESTOS RELEIDOS, QUE ES EL DOBLE EXACTO, CON LOS TRES SOLAPES DEL
   UNIVERSO EN CERO POR CONSTRUCCION.** El `sha256` de la ciega se cotejo **antes
   de leer un solo puesto** y calzo. **Y el cero no salio por suerte:** sin el
   parametro `evitar`, el solape con la exclusion **es 30**.
6. **LA NOMINA CRECE DE 121 A 125 Y `arneses_que_faltan()` DEVUELVE 0**, con los
   **seis** de la doble corrida dando **el mismo `sha256` las dos veces**. **No se
   poda nada.**
7. **HAY DOS COSAS EN ROJO Y LAS DOS SE DECLARAN ENTERAS**, y ninguna se arregla
   a la fuerza: **la `guarda_del_sujeto_congelado()` con 3 entradas** (dos
   heredadas de la 187 y una mia deliberada) y **una PARADA de verdad que esta
   vuelta se caza a si misma** en su propio arnes nuevo. Las dos van en la
   seccion 8.
8. **LO QUE ESTA VUELTA NO ABRIO NI TOCO:** las tres mesas anotadas del `6.3`
   (la del `PMF` con los puestos **338**, **297** y **670**, la del **603** y la de
   figuras del **226**); el campo `estado` de `docs/plan/OPERACIONES.jsonl`, que
   sigue en `LISTA` en las cuatro fichas; ningun campo nuevo en
   `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, que es la `PD.8`;
   `docs/loop/reportes/REPORTE_V184.md`; y `dataset/`.

## 4. EL ESTADO DEL ARBOL, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO

**LAS DOS CIFRAS DE ESTA SECCION SALEN DE `docs/loop/SALIDA_V188_APERTURA.txt`**,
que se escribio **antes de la primera operacion**, y no de lo que yo recuerde. Es
la guarda de la `2.d` la que las lee de ahi y las coteja contra lo que este
apartado afirma.

- El arbol abrio con **`git status --porcelain`** en **1** linea, y esa linea era
  **`?? scripts/loop/vuelta188_apertura.py`**: el propio bloque de apertura,
  todavia sin seguir por git cuando su bloque C corrio.
- Y con **`git diff --numstat -- dataset/`** en **0** filas **AL ENTRAR**.
- **AL SALIR**, medido de nuevo por el instrumento de la TAREA 5:
  **`CIFRA filas de git diff --numstat -- dataset/`: 0**. **Las dos cifras se
  publican, que es lo que el encargo pide, y el `numstat` es la vara, no el
  `git status`.**

**EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA**, dentro del bloque de
apertura y antes de la primera operacion: **4 filas**, las mismas cuatro que al
cierre. **Una columna de apertura medida al cierre es caida que ACUMULA, y esta
no lo esta.**

**Y EL CICLO DE GATE 0 CORRIO ENTERO Y EN SU ORDEN, LAS DOS VECES**, con
`run_phase1.py --reaplico-curaduria` (`GATE 0: OK`), `etiquetas_de_cara.py
--aplicar`, `sync_assets_web.py` y el `numstat`. **Motor 25/25, `tsc` exitcode 0,
web 82 ficheros y 1.040 tests**, al abrir y al cerrar.

## 5. LAS CORRECCIONES DECLARADAS DE ESTA VUELTA

**NINGUNA SOBRE UN VEREDICTO, Y ESO ES UNA MEDICION Y NO UN HUECO:** el `sha256`
LF del archivo abre y cierra en **`0a77b5a35a962621`**, con **3388 filas, 551 `A`,
72 `B`, 5 `C`, 2760 `D`, 0 huecos y 0 duplicados**.

**LAS QUE SI HAY SON DE INSTRUMENTO, Y VAN LAS TRES CON SU TEXTO VIEJO INTACTO:**

1. **EL CASO E DEL ARNES DE LA 186**, reescrito dentro de su propio fichero por
   la adjudicacion `7.1` del acta 188, **con quien lo autoriza escrito en su
   docstring** y **con la cuenta vieja de `not tardio` publicada al lado**.
2. **EL PARAMETRO `evitar` DE `vecinos()`**, aditivo, **con la version anterior
   congelada dentro de su arnes** para poder exigir que sin el la conducta sea
   identica.
3. **EL PATRON `C.n` Y EL VOCABULARIO DE ESTADOS DEL REGISTRADOR**, donde **se
   anaden** patrones y marcas y **ninguno de los viejos se ensancha ni se borra**:
   sus cifras se publican al lado (el patron viejo ve **2 de las 4** caidas, y el
   vocabulario viejo saca **2 `SIN DECIR`** de tres numerales).

## 6. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Los que hay siguen donde estaban y esta vuelta no los mueve:

- **`PD.1`**, septima vuelta abierta, con sus cinco puestos leidos del acta y no
  copiados del encargo: **1778, 2530, 2540, 3141, 3232**.
- **`PD.8`**, nacida en el acta 188 y abierta: la forma de una correccion
  declarada dentro de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`. **Es del fundador
  porque toca el esquema del archivo maestro**, y esta vuelta **no anade ningun
  campo**.

## 7. LAS PREGUNTAS QUE TRAIGO

**`P.1` ¿LA `guarda_del_sujeto_congelado()` DEBERIA ADMITIR UNA TERCERA CATEGORIA
PARA LOS ARNESES QUE LEEN EL DISCO VIVO A PROPOSITO?** Hoy tiene cuatro
veredictos: `CASO DECLARADO` (exento por lista), `CONGELADO`, `SUJETO VIVO` y `NO
DECIDIBLE`. Mi arnes de la escalada
(`vuelta188_tarea4_mutacion_cobertura_parejas.py`) sale **`NO DECIDIBLE`** y **es
correcto que salga asi**: lee `docs/loop/REPORTE.md` por `git show` (blob
congelado) **y ademas** mide el disco vivo, porque **esa es la fuente que la
guarda usa en produccion y medir contra otra cosa seria medir otra cosa**. **No le
pongo la marca `SUJETO CONGELADO` porque seria falsa.** La pregunta es si un
arnes cuyo caso decisivo TIENE que tocar el disco vivo debe entrar en
`CASOS_DECLARADOS` con su motivo escrito, o si debe seguir contando como deuda
visible. **No lo decido yo**: la lista de exentos es una puerta, y abrirla es
doctrina.

**`P.2` ¿QUE SE HACE CON UN CLON DECLARADO QUE ANADE CODIGO NUEVO?** El cotejo de
`vuelta187_tarea5a_nomina.py` contra `vuelta188_tarea3c_nomina.py` sale con
**exitcode 0** y a la vez con **`CIFRA SENTENCIAS DE CODIGO: 94`**, porque el
clon **anade** la exclusion por rojo que el original no tenia. **Lo declaro en vez
de esconderlo**, pero el instrumento no distingue hoy entre *"un clon que cambio
codigo"* y *"un clon que ANADIO una funcion nueva y no toco el resto"*, y **esas
dos cosas no son la misma**. ¿Debe el cotejo separarlas, o basta con declararlo
en prosa como hago aqui?

**`P.3` ¿CUAL ES LA CUENTA BUENA DE LAS ETIQUETAS `LD-nn`?** El acta 188 dice que
`docs/plan/LECTURAS_DIRIGIDAS.md` lleva etiquetas *"de `LD-01` hasta `LD-98`"*.
**Mi medicion da como maximo `LD-154`**, y **las dos son ciertas**: `LD-98` esta
en la linea **1953** y `LD-154` en la **662**, o sea que **el documento no numera
en orden de posicion**. Publico las dos. La pregunta es si esa numeracion no
monotona es intencional o es una costura, **y no la resuelvo tocando el
documento**.

## 8. LAS CAIDAS PROPIAS DE ESTA VUELTA, LO QUE QUEDA EN ROJO, Y LOS DISCUTIBLES

**`C.1`, DECLARADA POR MI: MI PROPIO ARNES NUEVO CAMBIABA SOLO ENTRE DOS
CORRIDAS DEL MISMO DIA SOBRE EL MISMO SUJETO.**

**LA CAIDA, CON SU CIFRA.** La primera doble corrida de la nomina saco **`CIFRA
paradas: 1`**: `scripts/loop/vuelta188_tarea2_mutacion_pata_documental.py` daba
su `sha256` normalizado a LF fue **`6e056e2b9d049861`** en la primera corrida y
**`edd65316f5312cd4`** en la segunda, **el mismo dia y sobre el mismo sujeto**.
**Eso es PARADA por la respuesta del acta 188 a la `P.2`**, con esas palabras.

**LA CAUSA, MEDIDA Y NO SUPUESTA:** imprimia **el nombre del directorio
temporal**, que `mkdtemp` fabrica distinto cada vez. **Es la misma enfermedad que
tumbo a `vuelta182_tarea2_mutacion_apertura_auditor.py` en la vuelta 184**, y la
escribo con su nombre para que se vea que no es nueva.

**POR QUE LA REPARO EN VEZ DE TRAERLA SIN TOCAR:** porque **es un arnes que NACE
en esta vuelta y no habia sellado ninguna salida**, y la adjudicacion `5.2` del
acta 186 dice que en ese caso *"su rojo es parte de escribirlo, lo reparas, y
pegas la corrida en rojo entera en el reporte con el motivo dentro del propio
fichero"*. **Las dos corridas en rojo se conservan enteras** en
`docs/loop/SALIDA_V188_T3C_NOMINA_EN_ROJO.txt` y en
`docs/loop/SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL_EN_ROJO_CAMBIA_SOLA.txt`, y el
motivo esta escrito dentro del propio arnes. **Tras la reparacion, las dos
corridas dan `ae804ea4e2894cce` las dos.**

**NO ACUMULA POR CIFRA PUBLICADA** (no publico ninguna cifra falsa: la cace antes
de escribirla) **y no es caida de reporte** (no afirme nada equivocado). **Es de
metodo.**

**`C.2`, DECLARADA POR MI: MI ARNES DE LA ESCALADA NACIO EN ROJO CON TRES
FALLOS, Y LOS TRES ERAN HALLAZGOS DE VERDAD.**

**LA CIFRA:** la primera corrida de
`scripts/loop/vuelta188_tarea4_mutacion_cobertura_parejas.py` dio **`CIFRA fallos:
3`** y **`VEREDICTO: ROJO`**. **Los tres eran hallazgos de verdad y ninguno se
reparo aflojando el sujeto:** (1) cotejar contra el arbol del commit acusaba en
falso al tallador, porque **git guarda con LF y la convencion DISCO de un fichero
con CRLF no se puede recuperar de git**; (2) el denominador de la cobertura
dejaba fuera la pareja de la linea 398, que es justo la forma que esta vuelta
venia a cubrir; y (3) el caso decisivo arrastraba a los dos. **Es un arnes que
nace en esta vuelta**, asi que por la `5.2` del acta 186 su rojo es parte de
escribirlo. **Se levanta solo y no acumula.**

#### LO QUE QUEDA EN ROJO Y NO ARREGLO, DECLARADO CON SUS TRES NOMBRES

`docs/loop/SALIDA_V188_T3C_NOMINA.txt` cierra en **`VEREDICTO: ROJO`** por **una
sola cosa**: **`guarda_del_sujeto_congelado(): 3 entradas sin congelar`**, y son
`vuelta186_tarea2c_mutacion_cierre_tardio.py`,
`vuelta187_tarea4_mutacion_dos_convenciones.py` y
`vuelta188_tarea4_mutacion_cobertura_parejas.py`, **las tres `NO DECIDIBLE` por
nombrar `REPORTE.md`**.

**DOS DE LAS TRES SON HEREDADAS Y NO SON NUEVAS, Y LO MIDO EN VEZ DE DECIRLO:**
`docs/loop/SALIDA_V187_T5A_NOMINA.txt` cierra en `VEREDICTO: ROJO` en su linea
**87** y lista **esas mismas dos** en sus lineas **10** y **11**. **La tercera es
mia y es deliberada**, y su motivo va entero en la `P.1` de la seccion 7. **Todo
lo demas de esa corrida esta en verde**: `arneses_que_faltan()` **0**,
`nomina_invisible_al_censo()` **0**, **6 de 6** dentro de la nomina y **`CIFRA
paradas: 0`**.

#### LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**LOS SEIS SON DE METODO. NINGUNO ES DE CLASE, Y POR ESO
`docs/loop/DISCUTIBLES_DE_CLASE_V188.txt` DICE `(ninguno)`:** esta vuelta **no
decidio ninguna clase y no movio ningun veredicto**. **Ese `(ninguno)` es una
medicion, no un hueco.**

- **`D.1` (DE METODO). DECLARE `OP-L-02` COMO PARADA EN VEZ DE COMO `(b)`.** Su
  `evidencia` es una sola linea de prosa que **no nombra ningun fichero**, asi que
  **no hay documento que medir**. Se podria argumentar que eso ES la respuesta
  (*"su producto no existe"*) y que corresponde `(b)`. **Elegi `(c)` porque la
  ficha no promete un fichero que falte: no promete ninguno**, y decir que su
  producto no la cubre seria afirmar algo sobre un producto que la ficha nunca
  nombro. **Discutible.**
- **`D.2` (DE METODO). DECLARE `OP-I-01` COMO `(a)` CON 672 ENTRADAS CONTRA LAS
  323 QUE PROMETE.** Un producto que ha crecido **+349** por encima de lo que su
  ficha describe **cubre** lo prometido, pero **tambien significa que la ficha ya
  no describe lo que hay**. Elegi `(a)` porque la pregunta era si el producto
  existe y la cubre, no si la ficha esta al dia. **Discutible.**
- **`D.3` (DE METODO). ANADI `LAS SUYAS` COMO MARCA DE ATRIBUCION DE CABECERA.**
  El encargo afirma que la cabecera de la seccion 8 nombra al ejecutor; **la medi
  y no contiene la palabra `EJECUTOR`**. Podria haber parado. **Elegi anadir la
  marca literal y DECLARAR la discrepancia**, porque la atribucion sigue siendo
  legible del texto (`LAS SUYAS`, en un acta que el auditor escribe sobre el
  ejecutor) y porque parar habria dejado sin registrar un acta entera.
  **Discutible.**
- **`D.4` (DE METODO). EL CASO DECISIVO DE LA ESCALADA COTEJA CONTRA EL DISCO DE
  HOY, NO CONTRA EL ARBOL DEL COMMIT**, con una excepcion mecanica para las rutas
  que esta vuelta movio. **Es lo que hace la guarda en produccion**, y el cotejo
  contra el arbol acusaba en falso. Pero **es una excepcion**, y una excepcion es
  una puerta. **Discutible.**
- **`D.5` (DE METODO). EL DENOMINADOR DE LA COBERTURA SON LAS LINEAS CON CIFRA DE
  BYTES, NO LAS RUTAS.** Con el otro denominador, la pareja de la linea 398
  quedaba fuera de su propio universo. **Pero un universo de lineas no es un
  universo de sujetos**, y la cifra se lee distinto. **Discutible.**
- **`D.6` (DE METODO). ACOTE LA `3.b` A DOS DE LOS CUATRO ARNESES DE LA 186.** El
  encargo dice *"hazlo en los arneses que ya lo publican (los cuatro de la 186
  juzgan `cerrar_reporte.py`)"*; **medi cuales publican numeros de linea del
  fichero vivo y son DOS**, y ponerselo a los otros dos habria movido dos salidas
  selladas para nada. **Discutible: la frase del encargo se puede leer como los
  cuatro.**
