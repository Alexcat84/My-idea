### TAREA 4. LA DEUDA. `R.65` Y `R.66`, LAS ACTAS 175 Y 176

**VA DETRAS DEL TRABAJO DE PLAN Y NUNCA DELANTE**, que es lo que la moratoria
manda: **las TAREAS 1, 2 y 3 cerraron y se commitearon antes de que esta
empezara**. Por el `4.9` del acta 201 la deuda son las **175 a 180**, **DOS POR
VUELTA**, de la mas vieja a la mas nueva.

**4.a EL COMPUTO NO SE ESCRIBIO DOS VECES.** Se importa
`scripts/loop/_v203_reparto_de_actas_viejas.py`, **el mismo que uso la TAREA 1**,
que es lo que el encargo manda con estas palabras: *reutiliza el computo de la
TAREA 1, no escribas un segundo*. **Y su prueba por mutacion se vuelve a correr
aqui en vez de heredar su verde de otra corrida:** contado de
`docs/loop/SALIDA_V203_T4_REGISTROS.txt`, **9 casos, 9 verdes, 0 rojos**, **4
discrepancias entre la plantilla ancha y la heredada** y **9 de 9 caen** con el
esperado mutado.

**4.b EL NUMERO NO SE TECLEA, Y EL SEGUNDO MENOS QUE EL PRIMERO.** Lo computa
`serie_de_registros.siguiente_libre()` recomputando la serie de sus **dos** sedes,
y el de la segunda entrada se computa **despues** de escribirse la primera. Al
abrir la tarea la serie daba **56 entradas, 0 colisiones, 0 huecos y siguiente
libre `R.65`**; **coincide con lo que el encargo dice**, y se corrio en vez de
copiarse.

**4.c LAS DOS ACTAS, ACOTADAS EN ESTA VUELTA.** Acta **175** en las lineas
**59995 a 60401** (**407** lineas, **11** secciones) y acta **176** en las
**60402 a 60865** (**464** lineas, **10** secciones), sobre un
`docs/loop/ACTA_AUDITOR.md` de **4706383** bytes en disco y **4706383**
normalizado a LF.

**4.d EL REPARTO ENTERO, POR LA VARA DEL `4.1` DEL ACTA 202, QUE CADA ENTRADA
DECLARA HABER USADO.**

| numeral | acta 175 | acta 176 |
|---|---|---|
| adjudicaciones | **6** (`5.1` a `5.6`), seccion **5** LAS ADJUDICACIONES, linea 60169 | **10** (`7.1` a `7.10`), seccion **7** LAS ADJUDICACIONES, linea 60633 |
| hallazgos | **no computable**: ninguna seccion la titula | **no computable**: ninguna seccion la titula |
| preguntas contestadas | **0** | **2** (`P.1`, `P.2`) |
| caidas propias del auditor | **1** (`CAIDA 1`), seccion **4**, linea 60152 | **no computable por una sola forma**, seccion **6** MIS PROPIAS CAIDAS Y MIS AMAGOS, linea 60606 |
| caidas del ejecutor | **no computable**: ninguna seccion la titula | **no computable por una sola forma**, seccion **5** LA CAIDA DEL EJECUTOR, CON SU NOMBRE, linea 60559 |

**4.e Y AQUI ESTA LA PIEZA QUE ESTA TAREA ANADE, PORQUE HABRIA PUBLICADO DOS
CEROS FALSOS.** El acta 176 **titula** una seccion `LA CAIDA DEL EJECUTOR, CON SU
NOMBRE`, y sobre ella la forma ``**`CAIDA n`.`` **da 0**. Publicar ese 0 se
leeria como que **no hubo caida del ejecutor**, y es falso: esa acta escribe su
caida como ``**CAIDA DE REPORTE 1:``, sin comillas inversas y sin numeral `N.M`.
**La regla quedo escrita dentro del codigo y no en la cabeza de nadie:** el
numeral de caidas es la cifra de `CAIDA n` **solo si ningun encabezado en negrita
se le escapa**; si alguno se escapa, se declara **no computable por una sola
forma** y la entrada publica **las tres lecturas**. **Eso es medir y decir lo que
cada forma da, no decidir cual gana.**

| seccion | por la vara `N.M` | por `CAIDA n` | por lead en negrita |
|---|---:|---:|---:|
| acta 175, caidas del auditor (seccion 4) | 0 | **1** | 1 |
| acta 176, caidas del auditor (seccion 6) | 0 | 0 | **3** |
| acta 176, caida del ejecutor (seccion 5) | 0 | 0 | **1** |

**4.f EL COTEJO CONTRA LA PROPIA FILA DE METRICA DE CADA ACTA**, que la escribio
el auditor de aquella vuelta y no esta vuelta:

| acta | lo que su fila de metrica publica | lo que este computo cuenta por `CAIDA n` | |
|---|---|---:|---|
| 175 (linea 60324) | `1` | **1** | CALZA |
| 176 (linea 60766) | `0 (dos amagos declarados)` | **0** | CALZA, **y la entrada declara ademas los 3 leads que ve** |

**4.g LOS REPORTES ARCHIVADOS NO SE FABRICAN, Y LOS DOS EXISTEN.**
`docs/loop/reportes/REPORTE_V175.md` mide **5953** bytes y
`docs/loop/reportes/REPORTE_V176.md` mide **95231** bytes, medidos en esta vuelta
con `os.path.isfile` y `os.path.getsize`. **Pero ninguno de los dos titula una
seccion de PREGUNTAS** (**0 apariciones** en cada uno), asi que el filtro de
siempre **no se puede correr** y las dos entradas usan **la vara del `4.7` del
acta 201**, **declarandolo**. **Un reporte que existe pero no tiene la seccion
deja el filtro tan inservible como uno que no existe**, y eso se dice en vez de
publicar un 0.

**4.h EL TITULO HEREDADO SE PUBLICA COMO CONTRASTE Y NO SE USA, CON SU MOTIVO
MEDIDO.** `R92.titulo_de_la_entrada()` escribe los **cinco** numerales como
cifras, y sobre estas actas **2 de los 5 no son computables** en la 175 y **3 de
los 5** en la 176. Un titulo que dijera *los cero hallazgos* se leeria como que
el acta no hallo nada. **Mismo precedente que la vuelta 201 sento en su entrada
de la 198.**

**4.i LO QUE SE ESCRIBIO.** `R.65` para el acta 175 y `R.66` para el acta 176,
las dos en `docs/PENDIENTES.md`, **por adicion al final y sin tocar una linea de
lo anterior**: la guarda cuenta **0 lineas del texto de entrada que no esten, EN
ORDEN, en el de salida**. La sede mide hoy, al salir de esta tarea, **1131953**
bytes en disco y **1131953** normalizado a LF. Antes de esta tarea median
**1117775** y **1117775** por esas mismas dos convenciones, o sea un
**crecimiento de 14178 bytes en disco y 14178 normalizado a LF**, y de
**219 lineas**. Su `sha256`,
identico en disco y normalizado a LF, pasa de `e6419a188db4334b` a
`725b85e12050a0ae`. **La segunda corrida sella crecimiento 0 por las dos
convenciones y 0 entradas escritas**, en
`docs/loop/SALIDA_V203_T4_REGISTROS_IDEM.txt`.

**4.j LA SERIE AL CIERRE, RECOMPUTADA Y NO HEREDADA: 58 entradas, 0 colisiones,
0 huecos y siguiente libre `R.67`**, contra **56, 0, 0 y `R.65`** al abrir.

**4.k LA DEUDA, REMEDIDA AL CIERRE: eran 8, quedaban 6 y quedan 4**, las **177,
178, 179 y 180**, contadas del propio fichero de salida y no heredadas.
