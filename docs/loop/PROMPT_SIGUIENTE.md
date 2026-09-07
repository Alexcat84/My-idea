Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la VUELTA 197 de la campana My Idea. Rama `pasada-unica`.
Lee `docs/loop/EJECUTOR.md` entero antes de la primera operacion y corre tu bloque
de apertura sellado ANTES de tocar nada, como siempre.

**EL TOPE DE CINCO SUB-TAREAS VOLVIO SOLO, Y LA CIFRA NO SE TECLEA.** `AUDITOR.md`
6.2 dice que el regimen temporal de dos sub-tareas se apaga cuando DOS VUELTAS
SEGUIDAS cierren su propio reporte con `cerrar_reporte.py`. El auditor corrio
`scripts/loop/vuelta192_racha_de_cierres.py` en la vuelta 197 y **da la racha en 2,
con las vueltas 195 y 196**. Vuelve a medirlo tu en tu apertura: **manda tu medicion
de hoy, no esta linea.** Van CUATRO sub-tareas, no cinco.

**ESTA NO ES VUELTA DE BATERIA.** Por `AUDITOR.md` 6.1 la bateria corre CADA CINCO
vueltas en vuelta propia: la 194 la corrio entera por sus diez tramos y **la
siguiente cae en la 199**. Tu seccion 9 cierra con el HUECO DECLARADO Y MEDIDO, con
su nombre, sus bytes y su atribucion, las tres juntas.

**NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO.** El `sha256` LF de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en el mismo valor, y
`git diff --numstat -- dataset/` se mide al entrar y al salir y las dos cifras se
publican. El cribado y el recomputo quedan fuera de esta vuelta.

---

## TAREA 1, LOS REGISTROS. BLOQUEANTE.

El acta 197 entra en la serie con el numero que devuelva
`scripts/loop/serie_de_registros.py`, **computado y no tecleado**: el auditor lo
midio en `R.59` con siguiente libre tras el `R.58`, pero **manda tu corrida**. El
cuerpo del acta se acota contando su primera linea con `grep -n` EN ESTA VUELTA: el
auditor la midio empezando en la **69341** sobre un `ACTA_AUDITOR.md` de **4595886
bytes**, y el fichero puede haber crecido.

La entrada registra, y **cada cifra se cuenta del cuerpo acotado, no de esta lista**:
las **SIETE adjudicaciones** `4.1` a `4.7`, con las tres preguntas del reporte de la
196 contestadas **por letra escrita y no por doctrina nueva** (`4.3` la `P.1`, `4.4`
la `P.2`, `4.5` la `P.3`); los **CUATRO hallazgos** de la seccion 5 (`5.1` el reporte
que quema la ciega del auditor por construccion, `5.2` el marcado de discutibles que
no existe por debajo del puesto 2662, `5.3` los tres puestos con tres lectores
independientes contra el archivo, `5.4` el fichero del turno que no se limpia al
cerrar); **CERO caidas del ejecutor de cifra publicada**, con la `C.E1` de la 196
**RE CLASIFICADA A TU FAVOR** como caida de REPORTE en prosa de acompanamiento, que
**NO acumula** (racha de cifra publicada en **1**, racha de reporte en **1**); tus
**DOS caidas de metodo**; y **CINCO caidas propias del auditor**, `C.A1` a `C.A5`,
todas de metodo y todas remediadas dentro de su vuelta, **con la `C.A1` en su TERCERA
acta seguida de la misma especie**. Y la METRICA DE CREDITO de la seccion 7 con sus
cifras: relecturas **332**, puestos **1.306**, dentro **60**, fuera **179**.

El registrador tiene que seguir siendo IDEMPOTENTE: se prueba re corriendolo, con la
sede medida en bytes antes y despues. Si el acta 197 escribe de alguna forma que tus
lectores heredados no leen, **cada lector nuevo lleva su mutacion delante y su cifra
al lado**, como hizo la 196 con sus seis.

## TAREA 2, EL ORDEN DEL TURNO DEL AUDITOR PASA A CODIGO. BLOQUEANTE.

**DE DONDE SALE, Y NO ES UNA IDEA MIA:** adjudicacion `4.5` del acta 197, que contesta
la `P.3` del reporte de la 196 **por extension de `AUDITOR.md` 1.2** (*"imprime
PRIMERO los pasos, adjudica tu clase, y SOLO DESPUES destapa la razon escrita"*).
**La tabla de discrepancias de un reporte ES un destape**, y esta medido: el reporte
de la 196 publico **la clase de archivo de 8 de los 120 puestos** que el auditor de
la 197 acababa de sellar, **y ademas el reparto entero del archivo sobre esos mismos
120**. El auditor lo sufrio siguiendo el orden escrito, no saltandoselo.

Sobre `scripts/loop/apertura_del_auditor.py`, **que NO SE CLONA**:

(a) **`leer_reporte()` APUNTA SU TOQUE Y CAE EN ROJO** si el turno tiene sello y
**no ha declarado sus clases todavia**. El orden obligatorio pasa a ser
`sellar()` -> clasificar -> `--declarar-clases` -> `leer_reporte()`. Un turno sin
sello sigue pudiendo leer el reporte, porque ahi no hay sujeto que quemar: **lo que
se prohibe es leerlo con el sujeto ya elegido y las clases sin escribir.**

(b) **EL FICHERO DEL TURNO SE CIERRA**, que es el hallazgo `5.4`. Hoy
`_TURNO_DEL_AUDITOR.json` sobrevive al turno y el auditor siguiente lo hereda sucio,
con lo que **tiene que borrarlo para poder sellar, y una guarda que ensena a borrar
su propia bitacora no es una guarda**. Anade un carril que lo CIERRE al declarar las
clases (o al escribir el acta) dejando constancia de que se cerro, de forma que un
turno nuevo empiece limpio **sin tener que borrar nada**. **El sello en disco no se
toca y la guarda `b` de `sellar()` sigue mirando el disco.**

(c) **EL REMEDIO DE LA `C.A1` DEL AUDITOR, QUE VA POR SU TERCERA ACTA SEGUIDA.**
Tres actas seguidas (195, 196, 197) recontando el marcador a mano con `json` en vez
de por `AP.marcador()`. El remedio de memoria ya fallo: la 196 lo declaro, lo
remedio dentro de su vuelta, y la 197 volvio a caer. **Escribe la guarda de codigo
que lo cace:** un carril que compruebe que la cifra del marcador que un acta publica
**calza con una salida de `AP.marcador()` de esa misma vuelta**, y que caiga en ROJO
si esa salida no existe o no calza.

**CADA UNA DE LAS TRES LLEVA SU CASO POSITIVO POR MUTACION DELANTE**, con nombre
estable y salida sellada, y **el caso rojo tiene que morder de verdad**: se prueba
que sin el remedio la guarda deja pasar y con el no. Ninguna guarda vieja se afloja.

## TAREA 3, LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR.

Es deuda del auditor y la paga el ejecutor con el instrumento, como en la 196.
`AUDITOR.md` 1.2: **CINCO discrepancias del auditor cayeron FUERA del marcado del
archivo** (`655`, `719`, `976`, `1809`, `1810`), asi que el credito de su tanda baja
y el tramo se relee al doble.

**EL TRAMO Y EL DOBLE ESTAN CERRADOS DESDE ANTES**, computados y no tecleados, en
`docs/loop/_auditor_v197_doble_para_la_198.txt`, **para que no se elijan despues de
mirar**. Son **240 pares**: 120 del tramo y 120 del doble. La serie medida va 30, 60,
120 y ahora 240.

(a) `vecinos()` **SE IMPORTA** de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`
y NO se copia, y `puestos_de()`, `numeros_de()` y `UNIVERSO_CONSUMIDO` se importan de
`scripts/loop/vuelta196_tarea2_relectura_al_doble.py`. **Recomputa el doble y
comprueba que calza con el sellado.** OJO CON UNA TRAMPA QUE EL AUDITOR PISO Y
DECLARO en su `C.A5`: **los dos `_exclusion.txt` guardan enteros sueltos y se leen
con `numeros_de()`, no con el patron de `puesto_intra`**; con un solo patron para
todos el universo sale 300 en vez de **681**, y el "solape 0 por construccion" seria
falso. El universo son **681** de **16** ficheros, y **561** por diferencia de
conjuntos con el tramo.

(b) **LEER LOS 240 A CIEGAS** con `aislador_de_ciega.py`, y **escribir las clases
ANTES de abrir el destape**.

(c) LA VARA es `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por numero y no
parafraseada, con sus precisiones `9.6.2` y `9.6.3` y la tabla de LOS DOS POLOS del
`9.22`. **Y CON LOS DOS ERRORES DEL AUDITOR PUESTOS DELANTE, que son los que su
cotejo midio y no una sospecha:**
  . **LA VARA ES EL SUELO Y NO EL TECHO.** Antes de aplicarla se pregunta si el par
    pertenece a una familia con REGLA PROPIA ya fijada, porque entonces manda la
    especifica. **Es la especie del `719` (la regla del puesto 595: el mismo
    instrumento en dos ocasiones distintas es sano) y la del `976` (la familia del
    sub-puro 7, cuatro pares leidos y los cuatro en A).**
  . **LA CONTENCION SE MIDE SOBRE EL CONTENIDO, NO SOBRE EL CONTENEDOR.** Si el nodo
    corto cabe ENTERO en el largo y **no trae ni un paso propio**, es `A` por
    contencion, **por mucho que el largo traiga ademas un procedimiento entero**.
    Preguntarse "el hijo trae procedimiento, luego CONTINUA" mirando el residuo del
    contenedor es la especie del `2838`.

(d) **NO SALTARSE LA `B` NI SOBRE EMITIRLA.** El sesgo esta medido en las dos
direcciones y las dos son perdida.

(e) **PUBLICAR EL COTEJO** con sus cifras: cuantos coinciden, cuantos discrepan, y
cuales caen dentro y fuera del marcado, **con los discutibles marcados ANTES de saber
si aciertas**. Y publica ademas, **porque el hallazgo `5.2` lo obliga**, cuantos de
los 240 llevan el literal `DISCUTIBLE MARCADO` en su razon y **como se reparten por
puesto**: sobre el sujeto de la 197 salieron **14 de 120, y los 14 del 2662 para
arriba**, con **0 en los 89 puestos por debajo**. Si tu reparto sale igual, **la
metrica de dentro-o-fuera no es comparable entre tramos y esa cifra tiene que estar
publicada**, no deducida.

(f) **LOS PUESTOS QUE LA CIEGA NO PUEDE ALCANZAR SE DECLARAN ANTES DE LEER, CON SU
NUMERO Y SU MEDICION, Y SALEN DEL CREDITO**, por la adjudicacion `4.4`: los que se
apoyan en un racimo censado o en una correccion declarada sobre una fusion no
aplicada. **No se ensancha la lista blanca del aislador**, que entregaria la
respuesta. Sobre los 120 de la 197 fueron **6 razones citando un racimo y 3 una
correccion declarada**.

(g) **Y LOS QUE LLEGUEN CON SU CLASE YA SABIDA POR HABER LEIDO EL ACTA O EL REPORTE
SE DECLARAN TAMBIEN, ANTES DE LEER.** El acta 197 publica la clase de archivo de
`655`, `719`, `976`, `1809`, `1810`, `2838`, `2916`, `3072` y `3173` en su seccion
`4.1` y en su `5.3`, y **los nueve estan dentro de estos 240**. **Quemados: se
publican y no entran al credito.**

## TAREA 4, LAS DOS CIFRAS QUE VIAJAN SIN SU VARA.

(a) **LA SECCION 9 PUBLICA "0 ARNESES DEL CENSO FUERA DE LA NOMINA" SIN NOMBRAR LA
VARA.** Medido por el auditor en la vuelta 197: censo **195**, nomina **135**,
entradas invisibles al censo **0**, y fuera de la nomina **60 SIN la vara** y **0 CON
la vara 148**. **No es caida** (la frase nombra su fuente y esa fuente si lleva la
vara, adjudicacion `4.7`), pero un `0` al lado de un 195 y un 135 **se lee como que
la nomina cubre el censo entero, y no lo cubre**. Haz que esa cifra viaje SIEMPRE con
su vara, en el sello de apertura y en el reporte, y **mide las dos** (con vara y sin
vara) en vez de una.

(b) **EL TOPE DE 80 LINEAS DEL MODO AUSTERO SE MIDE POR TRES VARAS Y LAS TRES SE
PUBLICAN**, por la adjudicacion `4.6`: **total**, **escrita a mano** (la vara que el
acta 196 fijo en su `4.7`), y **escrita a mano menos lo que otra regla obliga a
escribir** (cabecera tallada, tabla de tareas, seccion 9 y las demas piezas que una
guarda busca). El reporte de la 196 midio **588 lineas por `count(NL)` y 589 por
`split`**, y **318 por la vara estrecha**, cuatro veces el tope. **El tope no se
afloja y la excepcion no se inventa:** se publican las tres cifras para que el
fundador decida sobre numeros. Si la tercera vara sigue por encima de 80, **dilo con
esas palabras en el reporte** y deja la pregunta escrita.

---

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice
una regla vigente, paras y lo traes. No adivines.
