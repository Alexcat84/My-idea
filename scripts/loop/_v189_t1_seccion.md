### TAREA 1. LOS REGISTROS. CERRADA EN VERDE, Y EL REGISTRADOR NACE IDEMPOTENTE

**EL INSTRUMENTO:** `scripts/loop/vuelta189_tarea1a_registrar_acta189.py`, 1.318
lineas. **LA MAQUINA NO SE CLONA, SE IMPORTA** (`6.6` del acta 172): de la cadena
de registradores se importan `titulo_de_la_negrita`, `claves_de_adjudicacion`,
`claves_entrecomilladas`, `cuenta_por_patron`, `actas_sin_entrada`,
`PALABRA_CON_CERO`, `lineas_que_declaran_cero_caidas`, `seccion_que_contiene`,
`bloque_de_la_caida`, `acumulan` y los cinco patrones de caida.

**TODAS LAS CIFRAS DE ABAJO SE CUENTAN DEL FICHERO DE SALIDA QUE SE NOMBRA AL
LADO** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO). Las cuatro salidas de
esta tarea, medidas en disco:

| fichero de salida | bytes en disco |
|---|---:|
| `docs/loop/SALIDA_V189_T1A_MUTACION_REGISTRADOR.txt` | 5068 |
| `docs/loop/SALIDA_V189_T1A_REGISTRO_R51.txt` | 7740 |
| `docs/loop/SALIDA_V189_T1A_RECORRIDO_SIN_ESCRIBIR.txt` | 8026 |
| `docs/loop/SALIDA_V189_T1A_SIMULACION.txt` | 26904 |

**LA ENTRADA:** `R.51` en `docs/PENDIENTES.md`, **17971 bytes y 207 lineas**, con
**0 guiones largos o medios**. El numero **no esta tecleado**: lo devuelve
`scripts/loop/serie_de_registros.py`, que recompone la serie de sus **dos** sedes
y da **42 entradas, 0 colisiones, 0 huecos, siguiente libre R.51**. Despues de
escribir, remedido: **43 entradas, 0 colisiones, 0 huecos, siguiente libre R.52**.
La sede pasa de **943276 a 961248 bytes**.

**LO QUE LA ENTRADA REGISTRA, CONTADO Y NO TECLEADO** (bloques C a J de
`SALIDA_V189_T1A_REGISTRO_R51.txt`):

| lo que se cuenta | cifra | de donde sale |
|---|---:|---|
| adjudicaciones numeradas, patron SIN comillas inversas | **10** (`4.1` a `4.10`) | bloque C |
| adjudicaciones numeradas, patron CON comillas inversas (el del acta 188) | **0** | bloque C |
| de ellas, DISCUTIBLES (su titulo nombra un `D.n`) | **6** | bloque D |
| de esas seis, las que llevan `A FAVOR` en su titulo literal | **6 de 6** | bloque D |
| de ellas, PREGUNTAS (su titulo nombra un `P.n`) | **3** (`4.7`, `4.8`, `4.9`) | bloque D |
| de ellas, ni una cosa ni la otra | **1** (`4.10`) | bloque D |
| adjudicacion suelta de la seccion 5, por su negrita `ADJUDICO: ` | **1**, linea 67010 | bloque E |
| caidas `C.n`, patron de la 187 / patron de la 188 | **2 / 2** | bloque F |
| caidas propias del auditor | **2** (`C.1` linea 67027, `C.2` linea 67039) | bloque F |
| especie de cada una, leida de su bloque | **C.1 DE METODO, C.2 DE METODO** | bloque F |
| caidas del ejecutor | **0** | bloque F |
| patron `A.n` / patron `R.n` / patron `E.n` | **0 / 0 / 0** | bloque F |

**LA SECCION DE LAS ADJUDICACIONES CAMBIO DE NUMERO Y DE FORMA, Y LAS DOS CIFRAS
VAN PUBLICADAS.** En el acta 188 eran la seccion **5** y se escribian
``**`5.1` ...`` (numeral entre comillas inversas); en el acta 189 son la seccion
**4** y se escriben ``**4.1 ...`` (numeral suelto). El patron entrecomillado da
**0** sobre esta acta y el suelto da **10**. **Ninguno se ensancha: se corren los
dos y se dice lo que dan.**

#### 1.a. LA CAIDA QUE ESTE REGISTRADOR EVITA, Y ESTA VEZ EL VOCABULARIO HEREDADO NO ES QUE NO MUERDA: ES QUE SE EQUIVOCA

La cabecera de la seccion 6 del acta 189 es
`## 6. LAS CAIDAS. DOS SON MIAS Y CERO SON DEL EJECUTOR`, y **contiene la palabra
`EJECUTOR`**. Corrido sobre esta misma acta con el vocabulario de la vuelta 188
(`EJECUTOR` y `LAS SUYAS` para el ejecutor, con precedencia del ejecutor), el
reparto sale **ejecutor 2, auditor 0, huerfanas 0**: **las dos caidas propias del
auditor habrian quedado atribuidas al ejecutor**, que es exactamente la especie
de cifra falsa que el `4.3` del acta acaba de elogiar por haberse evitado en el
sentido contrario.

**EL REMEDIO SON DOS MARCAS, LAS DOS LITERALES DEL ACTA Y NINGUNA ENSANCHADA:**
`SON MIAS` como marca de AUDITOR, y `CERO SON DEL EJECUTOR` como marca de **CERO
DECLARADO**. Una cabecera que declara **cero** caidas del ejecutor **no le esta
atribuyendo ninguna**: la mencion de la palabra es una declaracion de cero, no un
reparto. Con el vocabulario de esta vuelta: **ejecutor 0, auditor 2, huerfanas
0**.

**LA PARADA SE CONSERVA ENTERA.** El bloque C del arnes corre los TRES casos
sobre actas fabricadas: cabecera al modo 189 da `(0, 2, 0)`, cabecera al modo 188
da `(2, 0, 0)`, y **cabecera que no dice de quien son da `(0, 0, 2)`**, o sea dos
huerfanas, y una caida huerfana **hace PARADA** y no se reparte a ojo.

#### 1.b. EL CERO DEL EJECUTOR, REGISTRADO COMO CERO Y NO OMITIDO

**CIFRA caidas del ejecutor: 0.** Y **un cero que sale de un patron que no muerde
no es evidencia de nada**, asi que va con la declaracion literal del acta al
lado: la frase `DEL EJECUTOR: CERO` aparece en **1 linea**,
`docs/loop/ACTA_AUDITOR.md:67056`. **Si el patron diera cero y el acta no lo
declarara por ninguna frase, este instrumento haria PARADA** en vez de publicar
un cero desnudo, y el bloque D del arnes lo prueba con un acta fabricada sin esa
declaracion, que da **0**.

#### 1.c. LA CORRECCION DECLARADA DE LA `4.9`, REMEDIDA HOY Y NO COPIADA DEL ACTA

El acta 188 escribio *"de `LD-01` hasta `LD-98`"*. **Esa cifra no se corrige
copiando la del acta 189: se vuelve a medir aqui** sobre
`docs/plan/LECTURAS_DIRIGIDAS.md` (**214916 bytes en disco, 2231 lineas**):

- **CIFRA etiquetas `LD-nn` distintas: 68.**
- **minima `LD-01`, maxima `LD-154`.**
- `LD-154` aparece en la linea **662**; `LD-98` en las lineas **1812, 1953, 2012
  y 2017**.
- **Lo que el acta 189 publica y lo que yo mido: CALZAN.**

**EL TEXTO VIEJO NO SE BORRA** y queda escrito en la entrada al lado del bueno, y
**el documento no se toca**: la numeracion no monotona se anota y no se arregla.

#### 1.d. LA RACHA DE REPORTE, CON LAS DOS CIFRAS LEIDAS DE LAS DOS ACTAS

Las dos filas salen de `grep` sobre el propio fichero, no de la memoria:

- **acta 188** (`docs/loop/ACTA_AUDITOR.md:66694`):
  `| caidas del ejecutor de reporte | **0** | **racha de reporte: SE MANTIENE EN 2**, y la escalada va ENCARGADA |`
- **acta 189** (`docs/loop/ACTA_AUDITOR.md:67071`):
  `| caidas del ejecutor de reporte | **0** | **racha de reporte: CORTADA, vuelve a 0** (adjudicacion 4.10) |`

**Si alguna de las dos actas no dijera nada de la racha, este instrumento haria
PARADA**, porque la `4.10` exige publicar LAS DOS cifras.

#### 1.e. LAS DOS CUENTAS DE RACHA DE LAS CAIDAS PROPIAS, QUE SON DE ALCANCE DISTINTO

**DISCUTIBLE MARCADO.** `acumulan()`, que mira el BLOQUE de cada caida, da
**acumulan 1 (`C.2`) y no acumulan 1 (`C.1`)**, porque el bloque de la `C.2` no
repite la formula literal que la `C.1` si escribe, y **una caida cuyo bloque no
diga nada se cuenta como QUE ACUMULA**, que es el lado seguro. La **tabla de
credito** del acta (`docs/loop/ACTA_AUDITOR.md:67069`) dice
`| caidas propias del auditor | **2** ... | **ninguna repetida: no abren racha** |`.
**Son dos mediciones de alcance distinto y las dos se publican; ninguna se
resuelve copiando la otra.** El encargo dice "ninguna de racha" y la tabla del
acta lo respalda; el computo por bloque no lo respalda para la `C.2`, y **eso se
declara aqui en vez de taparse**.

#### 1.f. LA IDEMPOTENCIA, QUE ES LO QUE SALE DE LA `C.2` DEL ACTA Y ES DEL PROPIO REGISTRADOR

**LA CAUSA, LEIDA Y NO SUPUESTA.** El bloque H.3 del sello de apertura de esta
vuelta la cita: `scripts/loop/vuelta188_tarea1a_registrar_acta188.py`, **linea
1348**, dice `ya = ("## R.%d. %s" % (numero, titulo)) in texto_sede`, y `numero`
es **el siguiente libre**, o sea un numero que **por construccion todavia no esta
en la sede**. **Comprobar la idempotencia por el numero que se va a escribir es
no comprobarla:** la respuesta es NO siempre, y por eso re correrlo duplicaba.

**LA COMPROBACION NUEVA ES POR EL ACTA, NO POR EL NUMERO, Y MIRA LAS DOS SEDES.**
Las dos marcas se computan de la vuelta y no se teclean:
`'del acta de la vuelta 189'` y `'(Acta del auditor, vuelta 189,'`.

**Y NO SE AFIRMA QUE FUNCIONE: SE RE CORRIO, QUE ES LO QUE HIZO EL AUDITOR.**
Segunda corrida entera, sellada en
`docs/loop/SALIDA_V189_T1A_RECORRIDO_SIN_ESCRIBIR.txt` (8026 bytes):

> `O) NO SE ESCRIBE NADA, Y ESTA ES LA IDEMPOTENCIA HACIENDO SU TRABAJO.`
> `el acta 189 YA TIENE ENTRADA en la serie: 4 linea(s) la nombran.`
> `NO se escribe una entrada nueva y NO se consume el numero R.52.`

**Y LA SEDE NO SE MOVIO:** `docs/PENDIENTES.md` mide **961248 bytes** antes y
despues del re corrido, con **42** cabeceras `## R.` y **2** lineas que nombran
`del acta de la vuelta 189` (el titulo y la cabecera del cuerpo). La primera
salida, `SALIDA_V189_T1A_REGISTRO_R51.txt`, se comparo byte a byte contra la
copia que se guardo antes del re corrido: **identica**.

**Y EL NOMBRE DE LA SALIDA DICE LO QUE PASO.** En la primera version, el re
corrido escribia su transcripcion en `SALIDA_V189_T1A_REGISTRO_R52.txt`, y ese
nombre **prometia un registro `R.52` que no existe**. Por `EJECUTOR.md` 1 (LA
RUTA QUE PROMETE PRUEBA ES CIFRA) se corrigio: cuando la idempotencia muerde, la
salida se llama `SALIDA_V189_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, y en `--simular`,
`SALIDA_V189_T1A_SIMULACION.txt`. **El fichero con el nombre viejo se borro y se
regenero con el nombre honesto; queda dicho aqui en vez de callarse.**

#### 1.g. EL CASO POSITIVO POR MUTACION, SOBRE ACTAS Y SEDES FABRICADAS

`python scripts/loop/vuelta189_tarea1a_registrar_acta189.py --mutacion`, salida
sellada en `docs/loop/SALIDA_V189_T1A_MUTACION_REGISTRADOR.txt` (5068 bytes):
**`CIFRA casos que CAEN: 0`, `CIFRA mutaciones que NO cayeron (y deberian): 0`,
`VEREDICTO: VERDE`**.

**NINGUN CASO SE PUBLICA SIN HABER CORRIDO SU MUTACION** (`EJECUTOR.md` 1, EL
CASO ROJO SE PRUEBA POR MUTACION). Las cinco mutaciones, con lo que dieron:

| mutacion | tiene que | lo que dio |
|---|---|---|
| pedir una cabecera de acta que el texto fabricado NO trae | PARAR | `PARADA: '# ACTA DEL AUDITOR, VUELTA 999' aparece 0 veces.` |
| cambiar a 4 el esperado del patron suelto sobre 3 fabricadas | CAER | `3 no es 4` |
| quitarle la marca de CERO DECLARADO al vocabulario nuevo | CAER | sale `(2, 0, 0)` en vez de `(0, 2, 0)` |
| intentar escribir dos veces sobre una sede que ya tiene la entrada | CAER | prohibida, con 2 lineas de prueba |
| cambiar a `LD-98` el esperado de la etiqueta maxima | CAER | la maxima es `LD-154` |

**Y EL ARNES NO SE QUEDA EN LO FABRICADO:** su bloque F corre la comprobacion
nueva **sobre el repo de verdad** y mide que el **acta 188 YA tiene entrada**
(`docs/PENDIENTES.md:13583` y `:13585`), o sea que un re corrido del registrador
de la 188, hoy, **volveria a escribir una duplicada**. Ese arnes **no corre** el
registrador de la 188: lo mide, porque correrlo es justamente lo que muta el
repo.
