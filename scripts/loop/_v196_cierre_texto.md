## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE AQUI SE CUENTA DEL FICHERO QUE LA LLEVA, Y EL FICHERO VA NOMBRADO
AL LADO** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO). Corte de todas:
**2026-09-06**.

| cifra | valor | fichero del que se cuenta |
|---|---:|---|
| racha de cierres, del inventario ENTERO | **1** (solo la vuelta 195) | `SALIDA_V196_APERTURA.txt` bloque `E` |
| selladas `SALIDA_V*_CERRAR_REPORTE.txt` en disco al entrar | **13**, y faltan **4** en el rango 179 a 195 (181, 182, 183, 194) | idem, bloque `E.1` |
| siguiente libre de la serie | **`R.58`** | idem, bloque `G` |
| entradas de la serie, antes de escribir | **49** | idem |
| entradas de la serie, despues de escribir | **50**, con **0 colisiones y 0 huecos** | `SALIDA_V196_T1A_REGISTRO_R58.txt` |
| bytes de `docs/PENDIENTES.md`, antes y despues | **1050189** y **1063803** | idem |
| bytes de `docs/PENDIENTES.md` tras el RE corrido | **1063803**, sin mover | `SALIDA_V196_T1A_RECORRIDO_SIN_ESCRIBIR.txt` |
| casos del arnes del registrador | **27 pasan de 27, 0 fallan** | `SALIDA_V196_T1A_MUTACION_REGISTRADOR.txt` |
| adjudicaciones del acta 196, por la union de los dos patrones | **14**, con **0 EN CONTRA** | `SALIDA_V196_T1A_REGISTRO_R58.txt` bloque `C` |
| lectores de adjudicacion: lead, suelto, negrita sola | **7, 0 y 7** | idem |
| caidas del cuerpo del acta, por parte | **1 del auditor y 1 del ejecutor** | idem, bloque `F` |
| universo consumido de las ciegas, de sus CATORCE ficheros | **621**, y **561** por diferencia de conjuntos con el tramo | `SALIDA_V196_T2_SUJETO.txt` bloque `C` |
| pares aislados a ciegas | **120**, con **0 fugas** del destape | idem, bloque `E` |
| quemados declarados ANTES de leer | **6**, los seis dentro de los 120 | idem, bloque `D.2` |
| cotejo de la ciega, sobre los 120 | **113 coinciden, 7 discrepan** | `SALIDA_V196_T2_COTEJO.txt` bloque `F` |
| cotejo sobre los 114 sin quemados | **108 coinciden, 6 discrepan** | idem |
| cotejo sobre el DOBLE, la unica mitad ciega de verdad | **55 de 60, 5 discrepan** | idem |
| cotejo sobre el TRAMO, con el reparto filtrado | **58 de 60, 2 discrepan** | idem |
| discutibles marcados ANTES de saber | **15** | idem |
| discrepancias DENTRO de mi marcado | **5** (`207`, `880`, `2429`, `2430`, `2917`) | idem |
| discrepancias FUERA de mi marcado | **2** (`616`, `2662`) | idem |
| de esas, FUERA y NO quemadas | **1** (`616`) | idem |
| mi reparto de clases sobre los 120 | **A 16, B 2, C 0, D 102** | idem, bloque `B` |
| reparto del archivo sobre los mismos 120 | **A 17, B 1, C 0, D 102** | idem, bloque `G` |
| razones de los 120 que citan un RACIMO | **6** | conteo sobre `INTRA_DOMINIO_VEREDICTOS.jsonl`, publicado en la seccion de la TAREA 2 |

**UNA CORRECCION DECLARADA, Y NO SE TAPA LO QUE CORRIGE** (`EJECUTOR.md` 8). **La
seccion de la TAREA 2 de este mismo reporte publica
`docs/loop/SALIDA_V196_T2_SUJETO.txt`, 12038 bytes`, o sea disco 12038 bytes y LF 12038 bytes, Y ESA CIFRA ES VIEJA:
el fichero mide HOY disco 12683 bytes y LF 12683 bytes**, con `sha256` `86f01d42aabdd153` por disco y `86f01d42aabdd153` por LF.
La cifra vieja, la de la primera corrida, era disco 12038 bytes y LF 12038 bytes. **La causa esta medida:** el sujeto se corrio dos veces, y entre
la primera y la segunda su bloque `C` crecio para medir el `561 sin el tramo` por
las dos lecturas. **La cifra vieja se cito despues de la segunda corrida**, que es
justo lo que la regla prohibe. **El texto viejo se queda donde esta y la correccion
va aqui**, y la caida entra en la seccion `8.1` con su nombre.

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO EN ESTA PROSA.**
`docs/loop/SALIDA_V196_APERTURA.txt`, bloque `C`, publica las dos cifras del estado
del arbol con la redaccion exacta que la guarda coteja, y aqui se repiten LEIDAS de
ella:

`git status --porcelain` 1 linea al entrar, que era el propio bloque de apertura
todavia sin commitear.

`git diff --numstat -- dataset/` 0 filas al entrar.

**Y ESAS DOS CIFRAS LAS ESCRIBIO EL PROPIO BLOQUE DE APERTURA**, con la redaccion
exacta que la guarda `D.1` busca. Eso funciono en la 195 y **aqui no se deshizo: la
apertura sellada no se toco al cierre ni una vez.**

**LO QUE SE TOCO:**

- `scripts/loop/`: el bloque de apertura y el de cierre de esta vuelta, el
  esqueleto del reporte, el registrador del acta 196, el sujeto de la relectura al
  doble, el fichero de mis clases y el cotejo, y los dos cuerpos de tarea.
- `docs/loop/`: las salidas de esta vuelta, el reporte, y `REPORTE_V195.md`
  archivado byte a byte antes de pisar nada.
- `docs/PENDIENTES.md`: la entrada `R.58`, y **solo por adicion**.

**LO QUE NO SE TOCO, MEDIDO Y NO PROMETIDO:**

- **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO SE MOVIO.** Abre y cierra igual por
  LAS DOS CONVENCIONES, y las dos van en la misma linea:
  disco 4054129 bytes y LF 4054129 bytes; y los `sha256` de disco y LF son `0a77b5a35a962621` y `0a77b5a35a962621`.
  Medido en la apertura, en el bloque `A` y el `F` del sujeto de la ciega, en el
  bloque `H` del cotejo y otra vez al cerrar.
- **NINGUNA CLASE SE TOCO.** El cribado y el recomputo quedan fuera por encargo, y
  las siete discrepancias se DECLARAN y no se mueven.
- **`dataset/` NO SE TOCO A MANO Y NO SE MOVIO.** `git diff --numstat -- dataset/`
  da **0 filas al entrar y 0 al salir**, y el ciclo de Gate 0 entero
  (`run_phase1.py --reaplico-curaduria` y despues `etiquetas_de_cara.py --aplicar`)
  deja **0 lineas** en `dataset/`, `web/` y `engine/` por los dos lados, sellado en
  `SALIDA_V196_CICLO_NUMSTAT_APERTURA.txt` y `..._CIERRE.txt`.
- **LA NOMINA NI SE PODO NI CRECIO:** **135 entradas** y `CASOS_DECLARADOS` en
  **2** al entrar, y ninguna tarea de esta vuelta la toca.
- **NINGUNA SALIDA SELLADA AJENA QUEDO PISADA.**
  `SALIDA_V192_RACHA_DE_CIERRES.txt` se re corrio en la apertura, se restauro con
  `git checkout --` y se REMIDIO, **identica antes y despues**, y va por LAS DOS
  CONVENCIONES porque en este fichero NO coinciden:
  disco 2443 bytes y LF 2399 bytes; y los `sha256` de disco y LF son `ceb100c9fb83df88` y `4469a54a3417f36b`.
- **LA SEDE DEL TURNO DEL AUDITOR NO SE MOVIO**, y va por LAS DOS CONVENCIONES:
  disco 377 bytes y LF 377 bytes; y los `sha256` de disco y LF son `2759cc614b0b11ae` y `2759cc614b0b11ae`.
- **NI CRIBADO, NI RECOMPUTO, NI OPERACIONES DEL PLAN, NI MESAS ANOTADAS, NI LA
  BATERIA ENTERA**, que no es su vuelta y cae en la 199.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` LOS SEIS QUEMADOS LOS ELEGI YO, Y PODRIA HABER ELEGIDO OTROS SEIS.** El
encargo pide declarar los puestos inalcanzables; lo que hice fue mas ancho: declarar
tambien los que llegan con su clase sabida. **El `976`, el `2428`, el `2662` y el
`3173` son incontestables** porque la seccion 4 del acta publica su clase. **El
`654` y el `719` son mi juicio**: el acta dice que el encargo de la 195 publico su
clase, y yo no lei ese encargo, pero si lei que la leccion era *"la de la `B` que
faltaba"*, y con eso el `654` queda servido. **Quien crea que esos dos no estaban
quemados, que sume dos aciertos mios y lo diga.**

**`D.2` PUBLICO CUATRO CUENTAS Y NO UNA, Y LA QUE MANDA ES LA QUE ME PERJUDICA.**
Las cuatro varas del cotejo se publican enteras, y digo expresamente que **la que
manda es el 55 de 60 del DOBLE**. Se podria sostener que la buena es el 108 de 114,
que es tres puntos mejor. **No la elijo yo: elijo la que sale de leer sin saber
nada.**

**`D.3` DECLARE CONTAMINADA LA MITAD DEL SUJETO POR UNA CIFRA QUE NADIE ME OBLIGO A
MIRAR.** El reparto `A 8, B 1, C 0, D 51` del tramo esta en la seccion 2 del acta,
y la TAREA 1 obliga a leer el acta entera. **Podria haber callado que lo lei**, y el
tramo habria pasado por lectura limpia con un 58 de 60. **Lo declaro porque mi
reparto sobre el tramo salio exactamente ese**, y una coincidencia asi no se puede
publicar como merito.

**`D.4` CAMBIE EL ORDEN DE LAS TAREAS RESPECTO DE LA 195.** Alli la TAREA 2 fue
antes que la 1 para no quemar la ciega; aqui la 1 va primera. **El motivo es
medido:** el acta 196 no publica la clase por puesto de ninguno de los 120 salvo
las cuatro que ya nombre, y esas cuatro estan destapadas desde su propia seccion 4.
**Lo que si me quemo el orden es el REPARTO del tramo**, y por eso lo declaro en el
`D.3` en vez de defenderlo.

**`D.5` LE ANADI AL REGISTRADOR SEIS LECTORES Y AFLOJE UNA GUARDA.** Cinco de los
seis son adiciones puras y su cifra va delante. **El sexto no lo es:** la exigencia
del cotejo de claves en la fila de metodo pasa a ser **condicional a que la fila
nombre alguna clave**. Es la misma forma que la 195 uso con el cotejo limpio y la
adjudicaron a favor, pero **es un aflojamiento y lo llamo por su nombre en vez de
venderlo como estrechamiento del caso.**

**`D.6` ENDURECI OTRA GUARDA SIN QUE ME LO PIDIERAN.** El cotejo limpio ya no basta
con que exista: tiene que **calzar con `cotejados - quemados`**. Nadie lo encargo, y
un endurecimiento no encargado tambien es cambiar el instrumento por mi cuenta.

**`D.7` EMITI UNA `B` DE MAS Y LA DEFIENDO.** El `207` lo lei `B` y el archivo dice
`A`. **La razon del archivo cierra con `FIGURA: el racimo de estrategia de
innovacion de producto, censado con TRES miembros, llega a CUATRO`**, o sea que su
clase se apoya en un censo que la ciega no me ensena. **Sigo pensando que a ciegas
ese par es un `B` razonable**, y lo publico como discrepancia mia igual.

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` UNA CIFRA PUBLICADA Y CORREGIDA DENTRO DE LA MISMA VUELTA, ANTES DE SU
CIERRE, ¿MUEVE LA RACHA DE CIFRA PUBLICADA?** El acta 196 deja la racha en **1** con
la `C.E1` y escribe que **dos tandas seguidas serian PARADA**. Esta vuelta trae una
cifra publicada que no calzaba, el `12038` de la seccion de la TAREA 2, **y la cace
yo al cierre y la corregi en la seccion 3 sin borrar la vieja**. La letra que
conozco no distingue entre una cifra que se va con la vuelta y una que se corrige
dentro de ella. **Registro lo mas estrecho: la cuento como caida de cifra publicada
en mi `8.1`**, y dejo la pregunta de si eso pone la racha en 2. **No la resuelvo yo
porque resolverla a mi favor seria exactamente lo que la regla vigila.**

**`P.2` LA CIEGA NO ENTREGA LA PERTENENCIA A UN RACIMO CENSADO, Y TRES DE MIS SIETE
DISCREPANCIAS SE APOYAN AHI.** El `616` dice literalmente *"FAMILIA DECLARADA: los
dos son miembros del racimo censado Portafolio, asi que no se pelea la clase"*.
**Contado sobre los 120: seis razones citan un RACIMO.** ¿Se anade el racimo a la
lista blanca del aislador, o se declara que esos puestos no entran en la metrica de
credito, como se hizo con el `2662`? **No toco el aislador por mi cuenta.**

**`P.3` ¿SE PUEDE SEGUIR LLAMANDO CIEGA A LA RELECTURA DEL TRAMO CUANDO LA TAREA 1
DE LA MISMA VUELTA OBLIGA A LEER EL ACTA QUE PUBLICA SU REPARTO?** El remedio del
`5.1` que el auditor propone (nombrar la FIGURA y no la CLASE) no alcanza a esto:
lo que se filtra aqui no es una clase, es la **distribucion**. **Lo mas barato que
se me ocurre es que la seccion 2 del acta publique el reparto como porcentaje del
acumulado y no del tramo, pero eso es doctrina y no la invento yo.**

## 7. PENDIENTES DE DOCTRINA

**UNO, Y ES EL DE LA `P.1`.** No hay regla escrita que diga si una cifra publicada y
corregida DENTRO de su propia vuelta, con su correccion declarada y sin borrar el
texto viejo, mueve la racha de cifra publicada. **Registro lo mejor sostenido**
(cuenta como caida, y por eso va en la `8.1`) **y lo marco PENDIENTE DE DOCTRINA en
su razon, y sigo**, que es lo que `EJECUTOR.md` 5 manda cuando falta la regla.

## 8. LO QUE LA 197 RECIBE

**LA RACHA DE CIERRES DEBERIA LLEGAR A 2 CON ESTA VUELTA**, y con eso el tope de
`AUDITOR.md` 6.2 vuelve a cinco sub-tareas **sin que nadie tenga que adjudicar
nada**: esta vuelta sella su `docs/loop/SALIDA_V196_CERRAR_REPORTE.txt`, que es la
linea que el encargo puso en mi mano. **La cifra la cuenta el instrumento en la
apertura de la 197, no yo aqui.**

**Y LA COLA, EN EL ORDEN QUE EL ENCARGO DEJO ESCRITO, sin redescubrirla:** que
`cerrar_reporte.py` escriba su propia salida sellada; el tope de 80 lineas del modo
austero, **con su medicion hecha en esta vuelta y publicada en la `8.1`**; la guarda
de la `P.2` del reporte de la 195 con su calibrado antes que sus dientes; el desfase
de `PATRONES_ACTA`, **que ya lleva CINCO encargos en primer lugar de la cola**; la
fila de credito del acta con su rotulo impuesto por el instrumento; la guarda de
codigo del hallazgo `5.3` del acta 194; `acumulan()` que lea la tabla; el cotejo de
clon declarado; la excepcion que publica siempre su lista; el censo de arneses con
carril de mutacion sin fichero propio; las **ocho** actas sin entrada propia en la
serie (173 a 180), remedidas en esta vuelta; que el campo `evidencia` de `OP-L-02`
nombre los ficheros que ya existen, **con su ESTADO SIN MOVER: sigue en `LISTA`**; y
**QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO** mas los cuatro puestos que dos
lectores independientes fallaron.

**Y TRES QUE ENTRAN NUEVAS, LAS TRES CON SU CIFRA:** la pertenencia a un **racimo
censado** fuera de la lista blanca de la ciega (`P.2`, **6 razones de 120**); la
**distribucion del tramo** publicada en la seccion 2 del acta, que quema la mitad del
sujeto siguiente (`P.3`); y la **relectura al doble de MI tanda**, que dispara el
`616` por `AUDITOR.md` 1.2 y que **no adjudico yo**.

**LA BATERIA CAE EN LA 199** por la cadencia de `AUDITOR.md` 6.1, y esta vuelta no la
corre. **Su hueco va declarado y medido en la seccion 9.**

### 8.1 MIS CAIDAS PROPIAS DE ESTA VUELTA, DECLARADAS Y NO OMITIDAS

**`C.1`, Y ES DE CIFRA PUBLICADA, NO DE METODO.** Publique
`docs/loop/SALIDA_V196_T2_SUJETO.txt`, 12038 bytes`, o sea disco 12038 bytes y LF 12038 bytes, en la seccion de la TAREA 2
cuando el fichero ya media disco 12683 bytes y LF 12683 bytes. La cifra era la de la PRIMERA corrida del
sujeto y la escribi despues de la SEGUNDA. **La cace yo al recontar los ficheros
para la seccion 3, y la correccion esta declarada alli sin borrar el texto viejo.**
Su efecto sobre la racha es la `P.1` y **no lo decido yo**.

**`C.2`, DE METODO.** Corri el sujeto de la ciega **antes** de terminar de comprobar
que su bloque `C` media lo que el encargo pedia, y por eso hubo que correrlo dos
veces. **El aislamiento es determinista y la segunda corrida dio la misma ciega**,
pero la primera ya habia escrito ficheros. **Cazada dentro de la vuelta y sin efecto
sobre ninguna clase**, y es la causa directa de la `C.1`.

**`C.3`, DE METODO Y CONTRA EL MODO AUSTERO.** El punto 2 del modo austero pone tope
de **80 lineas** al reporte, y este mide **318 lineas por `count(NL)` y 319 por
`len(split(NL))`** ANTES de pegarle la cabecera y el cierre. **Las dos varas se
publican porque el acta 196 adjudico en su `4.7` que el tope se mide sobre la prosa
escrita a mano y no sobre lo tallado**, y aun descontando lo tallado sigue muy por
encima. **No lo escondo detras de esa adjudicacion: es una caida.**

**LAS TRES SE CAZARON DENTRO DE LA VUELTA. Ninguna toco una clase, un veredicto ni
un byte de `dataset/`.**
