### TAREA 1, LOS REGISTROS. CERRADA. `R.60` ESCRITA, Y LAS TRES CORRECCIONES EN SU SEDE SIN TAPAR NADA

**Instrumentos, los dos con prefijo de guion bajo por la moratoria:**
`scripts/loop/_v200_t1_registrar_acta199.py` y
`scripts/loop/_v200_t1b_correcciones_en_su_sede.py`. La adjudicacion `4.5` del
acta 199 declara que un computo de una vuelta, con prefijo de guion bajo, fuera
del censo y fuera de la nomina y que no vigila a nadie, **no es maquinaria**.
**Ficheros de salida, y toda cifra de abajo se cuenta de ellos:**
`docs/loop/SALIDA_V200_T1A_REGISTRO_R60.txt` (disco 8974 bytes y LF 8974 bytes,
`sha256` LF `24d55cd02d626c4f`),
`docs/loop/SALIDA_V200_T1A_REGISTRO_IDEM.txt` (disco 9100 bytes y LF 8962 bytes,
`sha256` LF `81fa613af871114b`, y **las dos cifras no coinciden porque este se
sello por redireccion de consola y llego con CRLF**),
`docs/loop/SALIDA_V200_T1B_CORRECCIONES_EN_SU_SEDE.txt` (disco 3292 bytes y LF
3292 bytes, `sha256` LF `a805477c03bd134f`).

**NINGUN LECTOR NUEVO, Y ESO ES LA MITAD DEL ENCARGO.** Rige la moratoria
`AUDITOR.md` 6.3 y **esta vuelta no tiene ninguna excepcion**. Los numerales
salen de lectores que ya existen: `R84.claves_entrecomilladas()` lee las `4.n`,
las `5.n` y las `C.An`; `R94.caidas_propias_entrecomilladas()` lee las `C.n` del
ejecutor; `R92.caidas_por_lead_heredado()` corre al lado como contraste; y
`R92.titulo_de_la_entrada()` compone el titulo.

**EL CUERPO SE ACOTO EN ESTA VUELTA Y NO POR LA LINEA DEL ENCARGO:** lineas
**69878 a 70229**, **352 lineas**, sobre un `ACTA_AUDITOR.md` de disco **4635053**
bytes y LF **4635053** bytes. **Calzan con las dos que el encargo cita, y se dice
que calzan porque se remidieron, no porque se heredaran.**

**EL NUMERO NO SE TECLEO:** serie recomputada de sus dos sedes, **51 entradas, 0
colisiones, 0 huecos, siguiente libre `R.60`**. Tras escribir: **52 entradas,
siguiente libre `R.61`, 0 colisiones y 0 huecos**.

**LO QUE LA ENTRADA REGISTRA, CADA CIFRA CONTADA DEL CUERPO ACOTADO:** **5**
adjudicaciones `4.1` a `4.5`; **4** hallazgos `5.1` a `5.4`; **4** preguntas
contestadas; **2** caidas propias del auditor (`C.A1`, `C.A2`); **3** caidas del
ejecutor (`C.1`, `C.2`, `C.3`).

**LOS DOS CONTRASTES QUE NO CALZAN VAN PUBLICADOS, QUE ES LO QUE PIDE LA CASA.**

| que se cuenta | el lector que manda | el contraste | por que difieren |
|---|---:|---:|---|
| caidas del ejecutor | **3** (`R94`, negrita que abre) | **4** (`R92`, por lead) | el heredado cuenta tambien la cita de `C.2` del parrafo del FILO, que el acta declara COMO CITA |
| caidas del auditor | **2** (`R84`, prefijo `C.A`) | **3** (`R92`, por lead) | el heredado las lee de la fila 70189 de la TABLA de la metrica, donde estan citadas las `C.n` DEL EJECUTOR |
| preguntas contestadas | **4** (las que el reporte llama pregunta) | **5** (claves `P.n` en los titulos `4.n`) | la quinta es `P.2`, que el reporte de la 199 marca DISCUTIBLE en su seccion 5, no pregunta en su seccion 6 |

**LA FUENTE SE ELIGIO ANTES DE CONTARLA** (regla del fundador del 4 sep 2026):
quien decide si una `P.n` es pregunta o discutible **es el reporte que la
escribio**, no el acta que la cita. La seccion `## 6. PREGUNTAS, QUE NO ADIVINO`
del reporte de la 199 vive en sus lineas **599 a 625** y nombra **`P.1`, `P.3`,
`P.4`, `P.8`**. Con esa vara el numeral es **4**, y **calza con la cifra que el
acta publica en su apertura y en su seccion 6**. Las dos lecturas quedan
escritas.

**EL TITULO HEREDADO CLAVA SU PROPIA VUELTA, Y SE DECLARA EN VEZ DE ESCONDERSE:**
`R92.titulo_de_la_entrada()` cierra con `del acta de la vuelta 192`, porque es el
registrador de la 192 y ese numero vive en su constante. **La sustitucion se
mide**: si el literal no apareciera exactamente una vez, el instrumento no
escribe nada. Aparece **1** vez.

#### LA CAIDA PROPIA DE ESTA TAREA, MEDIDA, REVERTIDA Y ARREGLADA (`C.P1`)

**MI GUARDA DE IDEMPOTENCIA MIRABA EL NUMERO Y NO EL SUJETO, Y ESCRIBIO UNA
ENTRADA DUPLICADA.** La primera version de `ya_escrita()` preguntaba si
`R.<siguiente_libre>` ya estaba en la sede. Pero **el siguiente libre avanza en
cuanto la entrada se escribe**: al re-correr el registrador para probar la
idempotencia, el siguiente libre ya era `R.61`, la guarda respondio que `R.61` no
estaba (**y era cierto**) y escribio **una segunda entrada del mismo acta**.

**MEDIDO Y NO NARRADO:** la sede paso de **1079444** a **1086030** bytes en disco
y la serie de **52** a **53** entradas; el `sha256` LF paso de `1c56ba86ffe292f9`
a `24c0ecd7425c2418`. **La duplicada se retiro con `git checkout --`** y la sede
volvio a su estado del commit, **disco 1088345 bytes y LF 1072852 bytes**, con
`sha256` LF `6d4ff7222b4e77b7`. **Nunca se commiteo.**

**EL ARREGLO ES LA VARA CORRECTA, NO UN PARCHE:** la idempotencia es **por
sujeto**, una entrada por acta, y se busca el literal `del acta de la vuelta N`
que el propio titulo escribe, que es el mismo que `actas_sin_entrada()` ya usa.
El numero se sigue mirando ademas, porque una colision de numero tambien es
motivo para no escribir. **La guarda vieja se conserva entera en el fichero, como
`ya_escrita_vieja()`, y CORRE AL LADO de la nueva en la prueba**, que es lo unico
que convierte "hacia falta arreglarla" en una medicion.

**LA PRUEBA POR MUTACION, CORRIDA: 7 casos, 7 verdes, 0 rojos, y los 7 CAEN con
el esperado mutado.** **En 1 de los 7 la vieja y la nueva discrepan**, y es
justo el caso que la tumbo: *el acta ya registrada con OTRO numero*, donde la
vieja dice `False` y la nueva dice `True`. Los otros dos casos nuevos son de no
ensanche: *otra acta con el mismo numero libre* sigue dando `False`, y *el acta
citada en prosa y no en titular* sigue dando `False`.

**Y LA IDEMPOTENCIA SE PROBO DESPUES DEL ARREGLO, RE CORRIENDO CON `--escribir`:**
la sede mide **1079444 bytes en disco y 1079444 LF** con `sha256` LF
`1c56ba86ffe292f9` **antes y despues**, la serie sigue en **52** entradas y el
instrumento imprime *"NO SE ESCRIBE: la entrada ya estaba. IDEMPOTENTE."*

#### LAS TRES CORRECCIONES DE CIFRA, CADA UNA EN SU SEDE

**LA SEDE ES `docs/loop/reportes/REPORTE_V199.md`**, que es donde viven las tres
cifras. Al abrir la vuelta ese texto estaba todavia en `docs/loop/REPORTE.md`; el
esqueleto de la 200 lo archivo byte a byte con los dos `sha256` cotejados, y a
partir de ahi el archivo ES la sede. **La sede medida al entrar: disco 48688
bytes y LF 48688 bytes, `sha256` `e88a05f2d64c791f` por disco y por LF. Al salir:
disco 54251 y LF 54251, `sha256` `a32272ff36524041` por las dos.**

**LOS TRES ANCLAJES SE BUSCAN, NO SE TECLEAN**, porque un numero de linea
tecleado caduca en cuanto algo se inserta encima, que es justo lo que esta tarea
hace: **1 acierto cada uno**, en las lineas **646**, **677** y **489** del
fichero sin corregir.

| caida | que decia la sede | que mide la 200 | instrumento |
|---|---|---|---|
| `C.1` | fuera de la nomina con vara 148: **1** | **2** | `V.arneses_que_faltan(vara=148)` |
| `C.1` | fuera de la nomina sin vara: **61** | **62** | `V.arneses_que_faltan(vara=0)` |
| `C.1` | arneses que el censo reconoce: **196** | **197** | `V.arneses_del_directorio()` |
| `C.2` | el literal `HUECO`: **4** | **3** lineas (8, 105, 213) y **3** apariciones | conteo sensible a mayusculas |
| `C.3` | lineas del inventario: **414** | **413** por `count`, **414** por `split` | el fichero acaba en salto de linea |

**LA `C.1` NO SE CORRIGIO TECLEANDO EL DOS:** el bloque pega **la salida de
`V.arneses_que_faltan()` corrida en esta vuelta**, con los dos nombres dentro. El
segundo es **`vuelta199_tarea1_mutacion_guardas_revividas.py`, escrito por la
propia vuelta 199**. **El `1` no era falso cuando se midio**: sale del bloque `F`
del sello de apertura de la 199, tomado antes de que esa vuelta escribiera nada.
Lo que fallo es publicarlo **sin su corte en la seccion que traspasa el estado**.

**LA `C.2` PEDIA ELEGIR ENTRE CORREGIR LA CIFRA O CORREGIR LA ETIQUETA, Y SE DICE
CUAL SE ELIGIO: SE CORRIGE LA CIFRA.** El parrafo escribe *el literal* `HUECO`,
en singular y en mayusculas, y esa etiqueta describe bien la clausula de la
`verificacion` que se estaba midiendo; **la cifra que no calzaba con ella era la
del patron insensible**. Las dos se publican en el bloque, cada una con su
etiqueta y sus lineas, y **la cuarta linea, la que sobraba, es la 45**, que dice
*hueco* en minusculas. El `PROVISIONAL` **2** si calzaba y no se toco.

**EL TEXTO VIEJO SIGUE ENTERO Y ESO SE COMPRUEBA EN VEZ DE PROMETERSE:**
`git diff --numstat` sobre la sede da **104 lineas anadidas y 0 borradas**. Cada
parrafo afectado lleva detras **un aviso de una linea** que apunta al bloque, y
el bloque **cita el texto viejo**, de modo que cada literal aparece dos veces: la
original y la citada. **Exigir una sola aparicion seria exigir que la correccion
no citara lo que corrige**, que es lo contrario de lo que `EJECUTOR.md` 8 manda.

**EL FILO DEL ACTA QUE NO COBRO, LEIDO Y NO IGNORADO:** los tres grupos de la
seccion `4.c` del reporte de la 199 son la misma especie que la `C.2`, la
etiqueta nombra el tema y la cifra sale del patron. **No los corrijo en esta
tarea porque el encargo manda TRES correcciones y nombra cuales son**, y anadir
una cuarta por mi cuenta seria ensanchar el encargo. **Queda escrito aqui con su
cita** para que la 201 lo tenga delante.

**LA DEUDA DE LA SERIE, REMEDIDA Y NO HEREDADA, Y LAS DOS MEDICIONES CON SU
MOMENTO:** al abrir la tarea, actas de la **173** a la **199** sin entrada
propia: **10** (`173`, `174`, `175`, `176`, `177`, `178`, `179`, `180`, `198`,
`199`). **Recontado AL CERRAR la tarea, ya con `R.60` dentro: 9** (`173`, `174`,
`175`, `176`, `177`, `178`, `179`, `180`, `198`). **La 198 sigue sin registrar, y
ademas su reporte NO esta archivado**: `docs/loop/reportes/REPORTE_V198.md` **no
existe**, medido hoy. Eso se dice en vez de callarse.
