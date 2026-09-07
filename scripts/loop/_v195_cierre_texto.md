## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE AQUI SE CUENTA DEL FICHERO QUE LA LLEVA, Y EL FICHERO VA NOMBRADO
AL LADO** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO). Corte de todas:
**2026-09-06**.

| cifra | valor | fichero del que se cuenta |
|---|---:|---|
| racha de cierres, del inventario ENTERO | **9** (vueltas 185 a 193) | `SALIDA_V195_APERTURA.txt` bloque `E` |
| siguiente libre de la serie | **`R.57`** | `SALIDA_V195_APERTURA.txt` bloque `G` |
| entradas de la serie, antes de escribir | **48** | idem |
| entradas de la serie, despues de escribir | **49** | `SALIDA_V195_T1A_REGISTRO_R57.txt` |
| colisiones y huecos de la serie | **0 y 0** | idem |
| casos del arnes del registrador | **27 pasan de 27, 0 fallan** | `SALIDA_V195_T1A_MUTACION_REGISTRADOR.txt` |
| universo consumido de las ciegas, de sus DOCE ficheros | **591** (561 sin el tramo) | `SALIDA_V195_T2_SUJETO.txt` bloque `C` |
| pares aislados a ciegas | **60**, con **0 fugas** del destape | `SALIDA_V195_T2_SUJETO.txt` bloque `E` |
| cotejo de la ciega, sobre los 60 | **54 coinciden, 6 discrepan** | `SALIDA_V195_T2E_COTEJO.txt` bloque `D` |
| cotejo de la ciega, sobre los 58 limpios | **52 coinciden, 6 discrepan** | idem, bloque `F` |
| discrepancias DENTRO de mi marcado | **4** | idem, bloque `E` |
| discrepancias FUERA de mi marcado | **2** (`2428`, `2662`) | idem |
| mi reparto de clases | **A 9, B 4, C 0, D 47** | idem, bloque `C` |
| reparto del archivo en esos 60 | **A 8, B 1, C 0, D 51** | idem |
| entradas de la nomina, apertura y cierre | **127** y **135** | `SALIDA_V195_APERTURA.txt` bloque `F` y `SALIDA_V195_T3F_BATERIA_DE_LO_TOCADO.txt` bloque `C` |
| arneses del censo, apertura y cierre | **193** y **195** | idem |
| arneses del censo FUERA de la nomina | **6** al abrir, **0** al cerrar | idem |
| entradas SIN SUJETO CONGELADO | **3** al abrir, **0** al cerrar | idem |
| entradas que el censo NO VE | **0** al abrir, **0** al cerrar | idem |
| arneses corridos en la corrida acotada, cada uno DOS veces | **12** | `SALIDA_V195_T3F_BATERIA_DE_LO_TOCADO.txt` bloque `E` |
| de esos 12: ancla perdida, no mordio, sin reproducir | **0, 0, 0** | idem |
| casos del arnes de la nomina enchufada | **15 pasan de 15, 15 caen al mutar** | `SALIDA_V195_T3G_MUTACION_NOMINA_ENCHUFADA.txt` |
| casos del arnes de `--componer` | **15 pasan de 15, 15 caen al mutar** | `SALIDA_V195_T4C_MUTACION_COMPONER_ROJO.txt` |
| casos del arnes que no mordia, ya reparado | **17 pasan de 17, 17 caen al mutar** | su propia salida por consola, corrida en esta vuelta |

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO EN ESTA PROSA.**
`docs/loop/SALIDA_V195_APERTURA.txt`, bloque `C`, publica las dos cifras del estado
del arbol con la redaccion exacta que la guarda coteja, y aqui se repiten LEIDAS de
ella:

`git status --porcelain` 1 linea al entrar, que era el propio bloque de apertura
todavia sin commitear.

`git diff --numstat -- dataset/` 0 filas al entrar.

**Y ESTA VUELTA ESAS DOS CIFRAS LAS ESCRIBIO EL PROPIO BLOQUE DE APERTURA, con la
redaccion exacta que la guarda `D.1` busca.** La 194 tuvo que anadirle a su
apertura sellada un bloque de restatement al cierre y lo conto como su caida `C.2`.
**Aqui la apertura no se toco al cierre ni una vez.**

**LO QUE SE TOCO:**

- `scripts/loop/`: el bloque de apertura y el de cierre de esta vuelta, el
  esqueleto del reporte, los cuatro instrumentos de las tareas, los dos arneses
  nuevos, los cinco arneses viejos que reciben declaracion o reparacion, la nomina
  de `verificar_mutaciones_viejas.py`, el lanzador de la bateria (por
  `--componer`), y los generadores de un solo uso del clon.
- `docs/loop/`: las salidas de esta vuelta, el reporte, y `REPORTE_V194.md`
  archivado byte a byte antes de pisar nada.
- `docs/PENDIENTES.md`: la entrada `R.57`, y **solo por adicion**.

**LO QUE NO SE TOCO, MEDIDO Y NO PROMETIDO:**

- **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO SE MOVIO.** Abre y cierra igual por
  LAS DOS CONVENCIONES, y las dos van escritas en la misma linea en vez de
  fiarse de que se entienda:
  disco 4054129 bytes y LF 4054129 bytes; y los `sha256` de disco y LF son `0a77b5a35a962621` y `0a77b5a35a962621`.
  Medido en la apertura, en el bloque `A` y el `F` del sujeto de la ciega, en el
  bloque `H` del cotejo y otra vez al cerrar.
- **`dataset/` NO SE TOCO A MANO Y NO SE MOVIO.** `git diff --numstat -- dataset/`
  da **0 filas al entrar y 0 al salir**. Y el ciclo de Gate 0 entero
  (`run_phase1.py --reaplico-curaduria` y despues `etiquetas_de_cara.py --aplicar`)
  deja **0 lineas** en `dataset/`, `web/` y `engine/` por los dos lados, selladas
  en `SALIDA_V195_CICLO_NUMSTAT_APERTURA.txt` y `..._CIERRE.txt`.
- **NINGUNA ENTRADA DE LA NOMINA SE QUITO.** La nomina solo crece, de 127 a 135, y
  `CASOS_DECLARADOS` sigue en **2**.
- **NINGUNA SALIDA SELLADA AJENA QUEDO PISADA.**
  `SALIDA_V192_RACHA_DE_CIERRES.txt` se re corrio en la apertura, se restauro con
  `git checkout --` y se REMIDIO, **identica antes y despues**, y aqui va por LAS
  DOS CONVENCIONES porque en este fichero NO coinciden:
  disco 2443 bytes y LF 2399 bytes; y los `sha256` de disco y LF son `ceb100c9fb83df88` y `4469a54a3417f36b`.
  Y `SALIDA_V194_BATERIA_COMPUESTA.txt` quedo **byte a byte igual** tras correr
  `--componer` sobre las selladas de la 194, comprobado con `cmp`.
- **LA SEDE DEL TURNO DEL AUDITOR NO SE MOVIO**, al entrar y al salir de la
  corrida acotada, y va por LAS DOS CONVENCIONES:
  disco 345 bytes y LF 345 bytes; y los `sha256` de disco y LF son `2e085e88795b9df2` y `2e085e88795b9df2`.
- **NI CRIBADO, NI RECOMPUTO, NI OPERACIONES DEL PLAN, NI MESAS ANOTADAS, NI LA
  BATERIA ENTERA**, que no es su vuelta y cae en la 199.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` HACER LA TAREA 2 ANTES QUE LA TAREA 1, SIENDO LA 1 LA PRIMERA DEL
ENCARGO.** El encargo numera la 1 primero y las dos son bloqueantes, pero no fija
el orden. **Lo invertí a proposito**: la seccion 2 del acta 195 publica las clases
del auditor sobre los MISMOS 30 puestos que yo tenia que leer a ciegas, y
registrarla antes me habria quemado la ciega. **Las dos estan cerradas.** Lo marco
porque es una desviacion del orden escrito y la decidi yo.

**`D.2` HABER LEIDO EL ACTA ENTERA DESPUES, Y NO SOLO SUS SECCIONES 4, 5, 7 Y 3.**
Una vez selladas mis clases, lei el acta sin restricciones. **No hay ciega viva a
la que eso pueda afectar** y el registrador solo mira las secciones que declara,
pero lo digo por si el auditor prefiere otra disciplina.

**`D.3` HABER DECLARADO `SUJETO CONGELADO` EN CUATRO ARNESES EN VEZ DE PASARLOS A
CASO DECLARADO.** La regla ofrece las dos salidas y **elegi la primera en los
cuatro**. Mi motivo esta escrito arnes por arnes y es el mismo: **en los cuatro la
huella de vivo NO es una apertura del fichero vivo** (una cadena que va a una
bitacora, una linea impresa que dice que no lo toca, y dos blobs de git con su
commit clavado). **El riesgo que veo y no escondo:** la declaracion es un literal
en un docstring, o sea que **cualquiera puede ponerla sin que sea verdad**, y la
guarda no puede distinguir una declaracion honesta de un sello de goma. **Yo mire
los cuatro uno a uno antes de escribir nada, y eso no lo prueba ningun
instrumento.**

**`D.4` HABER TOCADO `vuelta194_bateria_por_tramos.py`, QUE ES DE OTRA VUELTA.** El
encargo dice que `--componer` propague el peor veredicto y no dice donde vive
`--componer`. Vive en el lanzador de la 194, que es del que la 199 clonara el suyo.
**Alternativa que descarte:** clonar un lanzador de la 195 solo para llevar el
arreglo, en una vuelta que no corre bateria. **Me parecio peor**: dejaria el
arreglo en un fichero que nadie clona.

**`D.5` HABER ANADIDO LOS DOS ARNESES NUEVOS A LA NOMINA EN SU MISMA VUELTA.** Es
lo que la regla escrita hace desde la 144 y lo que hicieron la 188 y la 190, pero
**la nomina pasa de 133 a 135 por decision mia** y el encargo solo nombraba seis.
**Si no lo hiciera, la 199 abriria con dos arneses fuera de la nomina** y el rojo
que esta vuelta apago volveria encendido.

**`D.6` HABER PUBLICADO EL COTEJO DE LA CIEGA DOS VECES, SOBRE 60 Y SOBRE 58.** La
segunda cuenta quita el `654` y el `719`, **cuya clase el propio encargo publica en
el cuerpo de su TAREA 2**. **Acerte en los dos**, asi que quitarlos me BAJA el
resultado, no me lo sube. Lo marco igual: **decidi yo cual de las dos cuentas es la
honesta**, y publico las dos para que el auditor elija.

**`D.7` HABER CONTADO COMO CAIDA MIA EL ARNES QUE SALIO `NO REPRODUCIBLE` EN SU
PRIMERA PASADA.** Lo cazo mi propia corrida acotada, dentro de la vuelta, y lo
arregle antes de cerrar. **Podria no haberlo contado**, porque nunca salio de la
vuelta. **Lo cuento y lo publico** porque la vara de esta casa es lo que se mide,
no lo que llega a publicarse, y porque el remedio (no imprimir el nombre de un
temporal en una salida sellada) es una leccion que la 196 puede usar.

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` LA SALIDA DE `cerrar_reporte.py` HAY QUE SELLARLA A MANO, Y NADIE LO DICE
EN NINGUN SITIO.** Medido en esta vuelta, en el bloque `E` de mi apertura: **la
racha de cierres sigue en 9 y NO en 10**, y las vueltas de la racha son 185 a 193.
La causa no es que la 194 no cerrara su reporte, porque lo cerro en exitcode 0 y su
mensaje de commit lo publica: **la causa es que `docs/loop/SALIDA_V194_CERRAR_REPORTE.txt`
NO EXISTE, ni en disco ni en git** (`git log --all --` sobre esa ruta no devuelve
nada). `vuelta192_racha_de_cierres.py` cuenta ficheros `SALIDA_V<n>_CERRAR_REPORTE.txt`,
y **`cerrar_reporte.py` no escribe el suyo**: lo tiene que redirigir el ejecutor a
mano. **La pregunta: ese fichero lo escribe `cerrar_reporte.py` de aqui en
adelante, o la racha se mide de otra cosa?** Un instrumento que mide una racha
contando un fichero que otro tiene que acordarse de crear **mide la memoria del
ejecutor, no la racha**. **Yo si sello el mio en esta vuelta**, pero eso no arregla
el carril y no lo arreglo por mi cuenta.

**`P.2` LA DECLARACION DE SUJETO CONGELADO NO TIENE NADA QUE LA VERIFIQUE.** Es el
`D.3` visto desde el otro lado. El literal `SUJETO CONGELADO` en el texto de un
arnes convierte un `NO DECIDIBLE` en `CONGELADO` **sin que nada compruebe que sea
cierto**. Hoy hay **cinco** arneses que dependen de esa declaracion. **La pregunta:
merece la pena una guarda que exija, ademas del literal, que la aparicion de la
huella de vivo NO sea una llamada de apertura de fichero?** Se puede mirar la linea
y pedir que no case con `open(`, `io.open(` ni `read_text`. **No lo hago por mi
cuenta porque ensancharia una guarda que el encargo no nombra**, y porque un
criterio mal calibrado ahi haria PARAR a arneses sanos.

**`P.3` EL TOPE DE 80 LINEAS DEL MODO AUSTERO Y LA PIEZA (4) DE `cerrar_reporte.py`
SIGUEN CHOCANDO, Y ESTA VUELTA LO ROZA POR EL OTRO LADO.** El reporte de la 194 lo
dejo dicho para las vueltas de bateria, donde la seccion 9 pega la bateria entera.
**Esta vuelta no es de bateria y aun asi el reporte pasa de largo las 80 lineas**,
porque cada tarea anexa su seccion al cerrarse y son cuatro. **La pregunta: el tope
de 80 lineas del MODO AUSTERO se mide sobre el reporte ENTERO, o sobre lo que el
ejecutor escribe A MANO fuera de las secciones talladas y anexadas?** **No elijo
cual incumplo en silencio**, que es lo que la 194 pidio expresamente que no se
hiciera.

## 7. PENDIENTES DE DOCTRINA

**NINGUNO.** Las cuatro tareas se resolvieron con reglas escritas y citadas por su
numero: `AUDITOR.md` 1.2 y 6.1, `EJECUTOR.md` 1, banco `9.1`, `9.6.1` con sus
precisiones `9.6.2` y `9.6.3`, `9.21`, `9.22`, la regla del sujeto congelado de la
vuelta 148 y `P.16`. **Las tres preguntas de la seccion 6 son preguntas de carril,
no de doctrina**: ninguna pide una regla que no exista.

## 8. LO QUE LA 196 RECIBE

**LAS CUATRO TAREAS CERRADAS Y ANEXADAS**, cada una con su seccion y sus salidas
selladas, y **el reporte abierto al empezar y crecido por anexion**, no escrito al
final.

**Y TRES COSAS QUE LA 196 RECIBE ARREGLADAS Y NO ROTAS, que es la diferencia con lo
que la 195 recibio:** los seis arneses fuera de la nomina (ahora **0**), las tres
entradas sin sujeto congelado (ahora **0**), y el arnes que no mordia desde la 188
(ahora muerde, **17 de 17**). **La 199 no deberia abrir con el rojo permanente que
la 194 publico en sus diez tramos**, y eso se sabra cuando corra.

**LO QUE SIGUE FUERA, NOMBRADO PARA QUE NO SE REDESCUBRA:**

- **EL DESFASE DE `PATRONES_ACTA`, EN PRIMER LUGAR DE LA COLA.** Lo pasa
  expresamente el encargo de la 195 con su motivo: las cuatro de hoy atacan causas
  y esta es cosmetica de cabecera. **Sigue vivo y declarado**: la cabecera de este
  reporte nombra el acta **194** (`edff6568`) porque el patron pide la de
  `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la 195** (`124a18a8`).
- **LA FILA DE CREDITO DEL ACTA CON SU ROTULO IMPUESTO POR EL INSTRUMENTO.** El
  auditor ya lo aplico a mano a su tabla en el acta 195, partiendo la fila en dos;
  lo que queda es que el instrumento que la talla lo imponga.
- **LA GUARDA DE CODIGO DEL HALLAZGO `5.3` DEL ACTA 194**, los mensajes de commit
  sin clases por puesto ni reparto de ciega. **A mano funciona y esta medido**: el
  acta 195 publica **CERO QUEMADOS** frente a los ONCE de la 194.
- `acumulan()` que lea la tabla, o que declare en su salida que no es la sede.
- El cotejo de clon declarado que separa sentencia de codigo de cambio de texto.
- La excepcion que publica siempre su lista.
- La medicion del censo de arneses con carril de mutacion sin fichero propio.
- **Las OCHO actas sin entrada propia en la serie (173 a 180)**, remedidas en esta
  vuelta y no arregladas.
- Que el campo `evidencia` de `OP-L-02` nombre los ficheros que ya existen. **Su
  ESTADO NO SE MUEVE: sigue en `LISTA`.**
- **QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO**, nombrado y medido y no resuelto,
  porque mover una clase es del RECOMPUTO. **Y un dato nuevo que esta vuelta anade
  en las dos direcciones:** el auditor emitio 0 `B` donde el archivo tenia 1, y yo
  emiti 4 donde el archivo tiene 1. **El sesgo de los lectores contra esa clase
  esta medido en los dos sentidos y ahora tambien el sesgo a favor.**

### 8.1 MIS CAIDAS PROPIAS DE ESTA VUELTA, DECLARADAS Y NO OMITIDAS

**`C.1` (DE METODO, Y NO ACUMULA). UN ARNES QUE YO ESCRIBI SALIO `NO REPRODUCIBLE`
EN SU PRIMERA CORRIDA.** `vuelta195_tarea3g_mutacion_nomina_enchufada.py` escribia
el nombre del directorio de `mkdtemp` en su salida sellada, y ese nombre lleva un
sufijo distinto en cada corrida: **dos corridas seguidas daban salidas distintas**.
Lo cazo **el cotejo de reproducibilidad de la vuelta 141**, corrido por mi propia
TAREA 3.f **dentro de la vuelta**, y esta arreglado y remedido antes de cerrar (0
sin reproducir). **Una salida sellada que cambia sola no se puede cotejar con
nada**, y por eso lo cuento aunque nunca saliera de la vuelta.

**`C.2` (DE METODO, Y NO ACUMULA). MI PRIMER INSTRUMENTO DE COTEJO CONTABA UN
DISCUTIBLE DE MAS.** `mis_discutibles()` partia el fichero ENTERO por sus filas, de
modo que **el bloque de la ultima fila llegaba hasta el fin del fichero** y se
tragaba la seccion titulada `MIS DISCUTIBLES`. Publicaba **OCHO** donde la lista
del final dice **SIETE**. **Lo cazo su propia guarda**, que publica las dos cuentas
y dice si calzan; corregido acotando la tabla, y hoy las dos dan siete. **El codigo
viejo se nombra entero en el docstring en vez de borrarse.**

**`C.3` (DE METODO, Y NO ACUMULA). LA COLUMNA DE REPARTO DE TRES FILAS DE MI
FICHERO DE CLASES SALIO MAL.** Los puestos `11`, `974` y `975` llevaban el rotulo
de la mitad equivocada, y la columna sumaba **31 y 29** donde solo puede sumar
**30 y 30**. **Ninguna clase se toco** y el destape seguia sin abrirse; lo que
estaba mal era el rotulo, no la lectura. **La correccion va anexada al final del
fichero con lo que decia y lo que dice**, sin borrar el texto viejo.

**`C.4` (DE METODO, Y NO ACUMULA). MI ARNES DE `--componer` APUNTABA A UN COMMIT
QUE NO TENIA LAS DIEZ SALIDAS.** `6a508ca5` es el commit que anadio **el tramo 1**,
y en su arbol solo existia uno de los diez. **Lo cazo su propio caso
`los_DIEZ_blobs_se_leen`**, midiendo 1 donde tenia que medir 10. Corregido a
`56c2d085`, y **el commit viejo se nombra en el codigo con lo que pasaba**.

**LAS CUATRO SON DE METODO Y NINGUNA ES DE CIFRA PUBLICADA: las cuatro se cazaron
DENTRO de la vuelta, tres de ellas por guardas que yo mismo habia escrito para eso,
y ninguna llego a publicarse como cifra.** **Y ninguna es la especie que la 194
declaro:** su `C.1` y su `C.2` eran del bloque de apertura, y esta vuelta el bloque
de apertura corrio el ciclo entero y escribio el sus dos literales. **La cadena que
llevaba dos vueltas heredandose queda cortada aqui.**
