### TAREA 1. LA CORRECCION DECLARADA DE `R.63` Y `R.64`, Y SU REPARTO REAL

**VA PRIMERA PORQUE `AUDITOR.md` 1.4 PONE LOS REGISTROS EN LA TAREA 1**, y es el
remedio de la `C.E1` de la 202.

**1.a LA FRASE FALSA, MEDIDA AQUI Y NO COPIADA DEL ENCARGO.** El encargo dice que
`R.63` y `R.64` afirman que las adjudicaciones de esas actas viven en la
**seccion 6 sin clave numerada**, y manda medirlo. Medido en esta vuelta por
`scripts/loop/_v203_t1_correccion_registros.py`, ese literal vive en
**2 lineas** de `docs/PENDIENTES.md`, la **15813** y la **15902**, y las dos
calzan con lo que el encargo dice. El bloque `H.1` del sello de apertura lo
midio antes por separado y da lo mismo. **Las cabeceras `## R.63.` y `## R.64.`
aparecen 1 vez cada una, en las lineas 15766 y 15865.**

**1.b LA PRUEBA POR MUTACION VA DELANTE DE ESCRIBIR NADA.** Lo unico propio de
esta vuelta es **la plantilla de clave**, y es lo que se prueba, sobre textos
FABRICADOS dentro de la funcion y sin tocar el repo. Contado de
`docs/loop/SALIDA_V203_T1_CORRECCION_REGISTROS.txt`: **9 casos, los 9 verdes y
0 rojos**; **4 casos donde la plantilla ancha y la heredada DISCREPAN**; y la
segunda pasada muta el esperado y **caen los 9 de 9**. **NINGUN VEREDICTO ES UNA
CONSTANTE LITERAL:** los tres valores de cada caso salen de correr
`R84.claves_entrecomilladas()` tres veces sobre el mismo texto.

**Y LA TERCERA COLUMNA DE ESA TABLA ES LA QUE PRUEBA QUE NINGUN LLAMANTE VIEJO
SE MUEVE:** la funcion llamada **SIN el parametro nuevo** da, en los **9** casos,
exactamente lo mismo que la plantilla heredada. **Ese es el unico ensanche de
esta vuelta**, y va como el acta 173 adjudico en su `6.2`: **parametro opcional,
sin tocar a ninguno de los catorce llamantes**.

**1.c LAS TRES FORMAS DE CLAVE NO SE INVENTARON: SE MIDIERON** sobre las cuatro
actas antes de escribir el patron. Son la negrita **con** comillas inversas (la
forma de la 184 en adelante), la negrita **sin** comillas inversas (las
ADJUDICACIONES de las actas 173 a 176) y el **titular markdown** `### 4.1` (los
HALLAZGOS de las actas 173 y 174). **Y LA TRAMPA QUE EL PATRON ESQUIVA TAMBIEN
ESTA MEDIDA:** en el cuerpo de estas actas hay lineas como
``**3.388 filas, A 551, B 72**`` y ``**32.568 bytes**``, que son **cifras con
separador de millar y no claves**; no se cuelan porque la clave se busca por su
prefijo exacto, que es **el numero de la seccion**, y `3.` y `32.` no son el
numero de ninguna seccion mirada. **Los dos casos estan en la tabla de mutacion.**

**1.d EL REPARTO REAL, POR LA VARA ADJUDICADA, CONTADO DEL FICHERO DE SALIDA.**
Acta **173** acotada en las lineas **58941 a 59447** (**507** lineas) y acta
**174** en las **59448 a 59994** (**547** lineas), sobre un
`docs/loop/ACTA_AUDITOR.md` de **4706383** bytes en disco y **4706383**
normalizado a LF.

| numeral | acta 173 | acta 174 |
|---|---|---|
| adjudicaciones | **5** (`6.1` a `6.5`), seccion **6** LAS ADJUDICACIONES, linea 59294 | **10** (`6.1` a `6.10`), seccion **6** LAS ADJUDICACIONES, linea 59802 |
| hallazgos | **5** (`4.1` a `4.5`), seccion **4** LOS HALLAZGOS, linea 59157 | **5** (`4.1` a `4.5`), seccion **4** LOS HALLAZGOS, linea 59635 |
| caidas propias del auditor | **3** (`CAIDA 1` a `CAIDA 3`), seccion **3**, linea 59124 | **2** (`CAIDA 1` y `CAIDA 2`), seccion **3**, linea 59612 |
| caidas del ejecutor | **no computable**: ninguna seccion de esa acta titula ese numeral | **no computable**: ninguna seccion de esa acta titula ese numeral |
| preguntas contestadas | **0** | **2** (`P.1`, `P.2`) |

**LO QUE ESA TABLA REPRODUCE, Y NO ES POCO:** el acta 202 midio en su `4.1` que
la 173 trae `6.1` a `6.5` y la 174 `6.1` a `6.10`. **Medido hoy con un
instrumento distinto, sale lo mismo.**

**1.e EL COTEJO QUE NADIE PIDIO Y QUE ES LA MEJOR PRUEBA DE QUE EL COMPUTO NO SE
INVENTA NADA.** La propia **fila de metrica de credito** de cada acta publica
cuantas caidas propias tuvo el auditor, y esa fila **la escribio el auditor de
aquella vuelta, no yo**. Cotejada contra mi computo por la forma `CAIDA n`:

| acta | lo que la fila de metrica del acta publica | lo que este computo cuenta | calza |
|---|---:|---:|---|
| 173 (linea 59360) | **3** | **3** | SI |
| 174 (linea 59909) | **2** | **2** | SI |

**1.f LAS DOS LECTURAS, PUBLICADAS JUNTAS, Y LA DISCREPANCIA DECLARADA.** El
lector heredado con su plantilla de siempre da **0, 0 y 0** sobre las dos actas,
y **ese cero es CIERTO**: esa plantilla exige comillas inversas y estas actas no
las escriben. La vara adjudicada da **5, 5 y 3** en la 173 y **10, 5 y 2** en la
174. **La discrepancia se declara, no se resuelve copiando** (`EJECUTOR.md` 2), y
las dos cifras quedan escritas dentro de cada entrada.

**1.g LO QUE SE ESCRIBIO, Y SOLO POR ADICION.** Contado del fichero de salida:
el bloque de `R.63` mide **7911** bytes y **127** lineas, y el de `R.64` mide
**8260** bytes y **129** lineas. `docs/PENDIENTES.md` pasa de **1101602** bytes
en disco y **1101602** normalizado a LF, con `sha256` LF `04228d4c0fcea65c`, a
**1117775** bytes en disco y **1117775** normalizado a LF, con `sha256` LF
`e6419a188db4334b`: **crecimiento 16173 bytes** por las dos convenciones y
**256 lineas**. Las entradas pasan a vivir en las lineas **15766 a 15991** y
**15992 a 16209**.

**1.h LA GUARDA, Y LA SEGUNDA CORRIDA SELLA CRECIMIENTO 0.** La guarda del texto
viejo cuenta **0 lineas del texto de entrada que no esten, EN ORDEN, en el de
salida**: una adicion solo puede anadir, y si esa cifra no fuera 0 seria ROJO.
Las dos entradas, releidas del disco, **traen la marca de la correccion** y
**siguen trayendo el texto viejo con el literal falso**, sin tachar y sin borrar.
La segunda corrida, en
`docs/loop/SALIDA_V203_T1_CORRECCION_REGISTROS_IDEM.txt`, sella **crecimiento 0
por las dos convenciones, 0 lineas de crecimiento y 0 entradas escritas**, con
el `sha256` LF de la sede **identico** a la salida de la primera.

**1.i LO QUE NO SE TOCO:** ningun campo `estado`, ninguna clase, ningun
veredicto, y **cero lineas de `numstat`** en `dataset/`, `web/` y `engine/`.
