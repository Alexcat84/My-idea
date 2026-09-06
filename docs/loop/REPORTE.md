# REPORTE DE LA VUELTA 189 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta189_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA SI ES DE BATERIA, Y POR ESO LLEVA DOS TAREAS Y LA SEGUNDA ES LA
> BATERIA SOLA.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la
> bateria de mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que
> **no lleva nada mas**. **Cerro entera en la 184**, asi que la siguiente es
> esta. Su seccion 9 **no cierra con hueco declarado**: cierra con la bateria
> corrida, sus tramos sellados y su salida compuesta.
>
> **Y LA BATERIA DE ESTA VUELTA NO HEREDA NI UNA SALIDA SELLADA DE LA CORRIDA
> 183/184.** El acta 189, seccion 5, midio que
> `scripts/loop/vuelta183_bateria_por_tramos.py` **ya no reparte en nueve tramos
> sino en DIEZ** (la nomina paso de 121 a 125) y que su `--siguiente` dice hoy
> **"EL SIGUIENTE ES EL TRAMO 10"**: correrlo tal cual habria corrido **un tramo
> de diez** y se habria declarado corrido **habiendo corrido 8 arneses de 125**.
> El bloque **H.4** del sello de apertura de esta vuelta lo **reprodujo entero**
> antes de tocar nada. Por eso la bateria va con un **clon declarado**,
> `scripts/loop/vuelta189_bateria_por_tramos.py`, cuyo `--siguiente` **cuenta
> desde cero**. **Y no se borra nada:** las nueve salidas de la 183 se quedan
> donde estan.
>
> **DONDE SE TALLO ESTE ESQUELETO: EN LA APERTURA Y EN SU PROPIO COMMIT**, como
> hizo la 188. Desde el segundo commit de esta vuelta ya hay reporte parcial en
> el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** ni cribado, ni
> recomputo, ni operaciones del plan, ni las mesas anotadas, ni **podar la
> nomina** (la opcion `c` que el fundador RECHAZO el 5 sep 2026: **la nomina
> sigue creciendo y nadie la poda sin el fundador**). **No entran** la relectura
> al doble del tramo del puesto **2422**, la `P.1` en codigo, la `P.2` en codigo,
> la condicion del `D.4` ni la busqueda de la sede de `OP-L-02`: **las cinco van
> a la vuelta 190** y su encargo ya las lleva escritas. **Y no se mueve ningun
> veredicto**: el `sha256` LF del archivo abre y tiene que cerrar en el mismo
> valor. **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al
> salir y las dos cifras se publican.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** **Una columna de apertura medida
> al cierre es caida que ACUMULA.**

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta189_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 188: `5aa9305d`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 188: LA 187 REPRODUJO ENTERA, EL PLAN SE MOVIO DE VERDAD (UNA FILA DE 3.388, EL PUESTO 2.464), ADJUDICO LOS SEIS DISCUTIBLES A FAVOR, Y LA PARADA QUE EL EJECUTOR DECLARA NO ES PARADA: LA RESUELVE SU PROPIO ENCARGO DE LA 187 Y SU REMEDIO VA BLOQUEANTE PORQUE LA BATERIA ES LA 189.'
- **DESFASE DECLARADO, QUINTA VUELTA:** la linea de arriba nombra el acta
  **188** porque `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que
  ORDENA esta vuelta es la 189**. Es el `D.2` del reporte de la 184, adjudicado a
  favor con reparacion encargada por la `5.2` del acta 185. **Esta vuelta no la
  ejecuta** porque su encargo dice con todas las letras *NADA MAS ENTRA EN ESTA
  VUELTA*. Se declara en vez de colarse.
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V189_HEAD_APERTURA.txt`: `bbeea713`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `b4f8b23c`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **188**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 189`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 189 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus DIEZ adjudicaciones `4.1` a `4.10` mas la adjudicacion de la seccion 5 (la bateria corre entera), las SEIS primeras (`4.1` a `4.6`) que son los seis discutibles del ejecutor y las seis A FAVOR, las TRES preguntas contestadas (`4.7`, `4.8`, `4.9`), DOS caidas propias del auditor (`C.1` y `C.2`) las dos DE METODO y NINGUNA DE RACHA, y CERO caidas del ejecutor REGISTRADAS COMO CERO Y NO OMITIDAS. Mas la correccion declarada del auditor sobre su propia sede (`4.9`: el acta 188 escribio "de `LD-01` hasta `LD-98`" y la cifra buena medida hoy es 68 etiquetas distintas con maximo `LD-154`), SIN BORRAR EL TEXTO VIEJO; y la racha de reporte CORTADA Y DE VUELTA A 0 por la `4.10`, con las DOS cifras, la vieja del acta 188 y la nueva. Con caso positivo por mutacion sobre un acta FABRICADA y su esperado mutado cayendo, y con la PARADA conservada entera. Y EL REGISTRADOR NACE IDEMPOTENTE, que es lo que sale de la `C.2` del acta: comprueba primero si el acta que se le pide YA TIENE ENTRADA, por su cabecera literal y no por el numero, y si la tiene SALE SIN ESCRIBIR Y LO DICE CON SU CIFRA, con su propio caso positivo por mutacion | **CERRADA EN VERDE** | `SALIDA_V189_T1A_REGISTRO_R51.txt` (7740 b), `_T1A_MUTACION_REGISTRADOR.txt` (5068 b), `_T1A_RECORRIDO_SIN_ESCRIBIR.txt` (8026 b), `_T1A_SIMULACION.txt` (26904 b), y la entrada `R.51` en `docs/PENDIENTES.md` |
| **TAREA 2** | LA BATERIA DE MUTACIONES, ENTERA, POR TRAMOS Y SOLA. Primero el CLON, que es bloqueante: `scripts/loop/vuelta189_bateria_por_tramos.py`, clon declarado de `vuelta183_bateria_por_tramos.py`, cotejado con `scripts/loop/cotejar_clon_declarado.py` y con la salida del cotejo pegada, porque el de la 183 ya reparte en DIEZ tramos y su `--siguiente` diria hoy EL SIGUIENTE ES EL TRAMO 10: correrlo tal cual haria UN tramo de diez y declararia la bateria corrida habiendo corrido 8 arneses de 125. La bateria de esta vuelta CORRE ENTERA sobre la nomina de hoy y NO HEREDA NI UNA SALIDA SELLADA de la corrida 183/184, y no se borra ninguna de las nueve. Despues la bateria tramo a tramo: `--plan` con el reparto computado y no tecleado, cada tramo con `--tramo N` sellado y COMMITEADO antes del siguiente, doble corrida con cotejo de reproducibilidad, la exclusion de los arneses ya en rojo DICHA en su salida, el reloj con la estimacion del `--plan` y la medicion de verdad al cerrar cada tramo, y `--componer` al final. LA BATERIA SE DECLARA CORRIDA CUANDO LOS DIEZ TRAMOS TIENEN SALIDA SELLADA DEL MISMO CALIBRE, y una salida sellada de CERO BYTES no cuenta como hecha | **CERRADA, LA BATERIA CORRIDA ENTERA, CON UN ROJO SELLADO TRAIDO SIN RE CORRER** | `SALIDA_V189_BATERIA.txt` (81968 b, 1236 lineas), los DIEZ `SALIDA_V189_BATERIA_TRAMO_n.txt`, `_T2_COTEJO_CLON.txt` (3022 b), `_T2_PLAN.txt`, `_T2_SIGUIENTE_ANTES.txt`, `_T2_SIGUIENTE_DESPUES.txt`, `_T2_NOMINA.txt` (4822 b) y `ROJOS_DE_LA_VUELTA_189.txt` (964 b) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

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

### TAREA 2. LA BATERIA DE MUTACIONES, ENTERA, POR TRAMOS Y SOLA. CORRIDA, Y CON UN ROJO DE VERDAD CAZADO

#### 2.a. PRIMERO EL CLON, QUE ERA BLOQUEANTE, Y SU COTEJO PEGADO SALGA LO QUE SALGA

`scripts/loop/vuelta189_bateria_por_tramos.py`, **clon declarado** de
`vuelta183_bateria_por_tramos.py`. El cotejo lo corrio
`scripts/loop/cotejar_clon_declarado.py --a ... --b ... --num-a 183 --num-b 189`
y su salida entera vive en `docs/loop/SALIDA_V189_T2_COTEJO_CLON.txt` (**3022
bytes en disco**). **Contado de ese fichero**:

| lo que el cotejo dice | cifra |
|---|---|
| FICHERO ENTERO / SOLO DOCSTRING / SOLO LA MAQUINA | **DIFIERE / DIFIERE / DIFIERE** |
| AST del fichero entero / AST sin el docstring | **DIFIERE / DIFIERE** |
| nodos del arbol sin docstring, A contra B | **4074 contra 4070** |
| lineas de maquina que difieren | **13** |
| **SENTENCIAS DE CODIGO** | **3** |
| **LITERALES DE TEXTO** | **10** |

**AQUI NO SE AFIRMA QUE EL DIFF SALGA VACIO, Y ES EL CASO QUE LA `4.8` DEL ACTA
DESCRIBE.** De las 3 SENTENCIAS DE CODIGO, **una sola es del original**:
`A:108 TRAMOS_QUE_MANDA_LA_DECISION = 9`, **retirada en el clon**; las otras dos
que el instrumento lista (`B:98` y `B:99`) son lineas de comentario que su
atribucion por linea arrastra. **Por que se retira, medido y no supuesto:** la
constante **no la usa nadie** (`grep -rn TRAMOS_QUE_MANDA_LA_DECISION scripts/
docs/` da su propia definicion y dos salidas selladas que la citan, y ninguna
lectura), y su valor **9 ya no dice la verdad**: con la nomina de hoy el reparto
da **10**. Dejar en el fuente un numero muerto que miente es la especie de cosa
que esta campana persigue. **Se declara, se publica y no se esconde detras de
"solo cambia texto".**

#### 2.b. LAS DOS COMPROBACIONES ANTES DE LANZAR NADA, QUE ERAN LA MITAD DEL ENCARGO

**`--plan`** (`docs/loop/SALIDA_V189_T2_PLAN.txt`), **computado y no tecleado**:

- **CIFRA entradas de la nomina: 125.** **CIFRA tamano de tramo: 13.**
  **CIFRA tramos: 10.** **CIFRA suma de las entradas de todos los tramos: 125.**
- **Nueve tramos de 13 y uno de 8**, publicados tramo a tramo por el propio
  instrumento.
- **LA ESTIMACION, DICHA COMO ESTIMACION Y CON SU CORTE PEGADO EN LA MISMA
  LINEA:** `entre 4.3 y 5.6` minutos por tramo y `entre 41.2 y 53.8` de la nomina
  entera, `(corte: HEAD d1c2f6d6c51c, nomina de 125 entradas contada en esta
  corrida)`.

**`--siguiente` ANTES DE EMPEZAR** (`docs/loop/SALIDA_V189_T2_SIGUIENTE_ANTES.txt`):
**`CIFRA tramos CON salida sellada no vacia: 0`**, **`CIFRA tramos que FALTAN:
10`**, **`EL SIGUIENTE ES EL TRAMO 1`**. **El clon cuenta desde cero**, que era
exactamente lo que la adjudicacion de la seccion 5 del acta pedia. Y su guarda de
atribucion, corrida sobre el propio fuente: **`CIFRA literales de vuelta clavados
en lineas que escriben: 0`**.

**EL CONTRASTE, QUE ES LO QUE PRUEBA QUE EL CLON HACIA FALTA.** El bloque **H.4**
del sello de apertura de esta vuelta corrio el lanzador **de la 183** y sello su
respuesta: **`CIFRA tramos CON salida sellada no vacia: 9`**, **`CIFRA tramos que
FALTAN: 1`**, **`EL SIGUIENTE ES EL TRAMO 10`**. Correrlo tal cual habria corrido
**8 arneses de 125** y se habria declarado corrido. **Y no se borro nada:** el
bloque **H.5** midio las **nueve** salidas `SALIDA_V183_BATERIA_TRAMO_n.txt` una
a una, y ahi siguen.

#### 2.c. LOS DIEZ TRAMOS, CADA UNO SELLADO Y COMMITEADO ANTES DEL SIGUIENTE

**LA TABLA SALE DE `--componer`, QUE LEE LOS FICHEROS, Y NO DE MI MEMORIA**
(`docs/loop/SALIDA_V189_T2_COMPONER_CONSOLA.txt`). La columna de minutos la
publica cada tramo al cerrarse:

| tramo | fichero | bytes | lineas | sha256 LF | entradas | minutos medidos |
|---:|---|---:|---:|---|---:|---:|
| 1 | `SALIDA_V189_BATERIA_TRAMO_1.txt` | 9296 | 122 | `0e27295e3ea0` | 13 | 2,6 |
| 2 | `SALIDA_V189_BATERIA_TRAMO_2.txt` | 7529 | 116 | `0854947a9b4e` | 13 | 5,8 |
| 3 | `SALIDA_V189_BATERIA_TRAMO_3.txt` | 7594 | 116 | `a85d7c71461b` | 13 | 8,3 |
| 4 | `SALIDA_V189_BATERIA_TRAMO_4.txt` | 7606 | 116 | `9f3a18ee5eae` | 13 | 2,4 |
| 5 | `SALIDA_V189_BATERIA_TRAMO_5.txt` | 7566 | 116 | `87c71accfa34` | 13 | 1,9 |
| 6 | `SALIDA_V189_BATERIA_TRAMO_6.txt` | 7626 | 116 | `0ff009ab23dc` | 13 | 2,3 |
| 7 | `SALIDA_V189_BATERIA_TRAMO_7.txt` | 7843 | 118 | `7f166322f04e` | 13 | 2,0 |
| 8 | `SALIDA_V189_BATERIA_TRAMO_8.txt` | 7595 | 116 | `5156306187dc` | 13 | 2,3 |
| 9 | `SALIDA_V189_BATERIA_TRAMO_9.txt` | 8062 | 116 | `5ce6ccd89c3e` | 13 | 2,1 |
| 10 | `SALIDA_V189_BATERIA_TRAMO_10.txt` | 6861 | 99 | `f7ae02f06cce` | 8 | 1,2 |

**NINGUNA MIDE CERO BYTES**, y esa es la condicion que el encargo pone para que
una salida sellada cuente como hecha.

**EL RELOJ: LA ESTIMACION ERA ESTIMACION Y LA MEDICION MANDA.** Suma de los diez
tramos: **30,9 minutos** contra **41,2 a 53,8** estimados. Pero la estimacion
**por tramo** se quedo corta en dos de los diez: el tramo 3 tardo **8,3** minutos
contra un techo estimado de **5,6**. **Las dos cifras se publican y la de verdad
es la medida.**

#### 2.d. LA COMPOSICION, Y LA COBERTURA LEIDA DE LAS SALIDAS Y NO DEL REPARTO

`--componer` cerro en **VERDE**:

- **CIFRA entradas que los tramos dicen haber corrido: 125.**
- **CIFRA entradas de la nomina que NINGUN tramo corrio: 0.**
- **CIFRA entradas corridas que NO estan en la nomina: 0.**
- **CIFRA entradas corridas MAS DE UNA VEZ: 0.**
- La salida unica `docs/loop/SALIDA_V189_BATERIA.txt`: **81968 bytes, 1236
  lineas, sha256 LF `f6b49dab8d357cb3bf4156d582c7fa88d1d3b3d86ea129cfcc128488d4212743`**.

**`--siguiente` CORRIDO DESPUES** (`docs/loop/SALIDA_V189_T2_SIGUIENTE_DESPUES.txt`):
**`CIFRA tramos CON salida sellada no vacia: 10`**, **`CIFRA tramos que FALTAN:
0`**. **LA BATERIA DE LA 189 QUEDA CORRIDA ENTERA SOBRE LA NOMINA DE HOY.**

#### 2.e. EL ROJO DE VERDAD QUE LA BATERIA CAZO, TRAIDO SIN RE CORRERLO Y SIN ARREGLARLO

**`vuelta172_tarea5_mutacion_cierre.py` sale `exit 1 NO MORDIO` en 10,9s**, en el
**tramo 7**, linea **52** de `docs/loop/SALIDA_V189_BATERIA_TRAMO_7.txt`. Es un
**arnes ya sellado**, o sea el caso que el punto 5 del encargo describe: **se
detiene AL ARNES, no a la vuelta**, y **no se re corre ni se arregla**.

**EL CONTRASTE, LEIDO DE UNA SALIDA SELLADA Y NO RECORDADO:** en
`docs/loop/SALIDA_V183_BATERIA_TRAMO_7.txt`, **linea 52**, el **mismo** arnes
daba **`exit 0 OK` en 2,2s**.

**LO QUE SE PUEDE AFIRMAR Y LO QUE NO, SEPARADO:**

- **MEDIDO:** su sujeto son **cadenas literales en memoria** (su propio docstring
  lo declara y su fuente lo confirma: *"todos los reportes de mentira son CADENAS
  literales de este proceso. NO se lee el disco"*), asi que **no puede haber
  cambiado por el dia**. Lo que prueba es
  `cerrar_reporte.piezas_que_faltan()`, que importa.
- **MEDIDO:** entre las dos corridas, `scripts/loop/cerrar_reporte.py` **si se
  movio**: es el sujeto que la **TAREA 4.b de la vuelta 188** cambio para exigir
  que las secciones sean **unicas y esten en orden**.
- **NO MEDIDO, Y POR ESO NO SE PUBLICA COMO CAUSA:** cual de sus casos concretos
  es el que deja de morder. **La salida sellada de la bateria no conserva el
  stdout del arnes**, solo su veredicto, y **averiguarlo exigiria re correrlo**,
  que es exactamente lo que el encargo prohibe. **Se trae asi, con la causa
  acotada y no afirmada.**

**LA EXCLUSION NO ES MUDA, Y HOY NO ESTA VACIA POR PRIMERA VEZ.**
`docs/loop/ROJOS_DE_LA_VUELTA_189.txt` (**964 bytes, sha256 LF
`aefae0656fe1612f`**) lleva su linea con **nombre, ruta de su salida en rojo y
motivo**, y `scripts/loop/vuelta189_tarea2_nomina.py` la lee con
`rojos_registrados()` y `particion_por_rojo()`, **importadas** del instrumento de
la 188 y no clonadas. Su salida
(`docs/loop/SALIDA_V189_T2_NOMINA.txt`, **4822 bytes**) publica
**`CIFRA arneses EXCLUIDOS de la doble corrida: 1`** con el excluido nombrado y
**`CIFRA arneses que SI se corren dos veces: 1 de 2`**.

#### 2.f. EL exitcode 1 DE LOS DIEZ TRAMOS, QUE NO ES DE NINGUN ARNES

**DISCUTIBLE MARCADO.** Los diez tramos salen con **exitcode 1**, y **en nueve de
los diez no cayo ni un arnes**. La fuente es siempre la misma linea, identica en
los diez:

> `ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado ... La lista
> entera: vuelta186_tarea2c_mutacion_cierre_tardio.py,
> vuelta187_tarea4_mutacion_dos_convenciones.py,
> vuelta188_tarea4_mutacion_cobertura_parejas.py`

**ES LA DEUDA QUE EL ACTA 189 YA MIDIO** en su seccion 2, con estas palabras:
*"el `ROJO` es solo `guarda_del_sujeto_congelado(): 3 entradas`"*, **y que su
`4.7` deja abierta a proposito**: `NO DECIDIBLE` se queda como esta porque deja
la deuda visible, y el remedio (separar en la salida las que traen motivo escrito
de las que no) **va encargado a la vuelta 190**.

**POR QUE SEGUI EN VEZ DE PARAR, Y ES LO DISCUTIBLE:** el punto 5 del encargo
manda detener **AL ARNES**, y aqui **no cayo ningun arnes**: cayo una guarda de
nomina que **cae igual en los diez tramos**. Parar en el tramo 1 habria dejado la
bateria sin correr, y `AUDITOR.md` 6.1 la manda **entera**. **No lo traigo como
PARADA** porque no contradice ninguna regla vigente ni ninguna cifra publicada:
es una deuda declarada, visible y con remedio ya encargado. **Lo marco como
discutible para que se adjudique.**

#### 2.g. LA DOBLE CORRIDA, LA NOMINA AL CERRAR Y EL ARBOL

**LA DOBLE CORRIDA DE LOS 125 LA HACE LA PROPIA BATERIA** (TAREA 2.f de la vuelta
141) y su veredicto esta en los diez tramos: **`NO REPRODUCIBLE: 0 (ninguna)` en
los diez**. Ningun arnes cambia solo entre dos corridas del mismo dia sobre el
mismo sujeto, asi que **no hay PARADA de esa especie**.

**LA NOMINA AL CERRAR** (`docs/loop/SALIDA_V189_T2_NOMINA.txt`, contado de ese
fichero): **censo 185, nomina 125, `VARA_DEL_CENSO` 148**,
**`arneses_que_faltan()` ultima vuelta 188 y FALTAN 0**,
**`nomina_invisible_al_censo()` 0**, **`guarda_del_sujeto_congelado()` 3**.
**LA NOMINA NO SE PODO**: sigue en 125, y la opcion `c` que el fundador rechazo
el 5 sep no se toco.

**LA DOBLE CORRIDA DEL ARNES QUE NACE HOY**, que es el carril `--mutacion` del
registrador: **corrida 1 y corrida 2, exitcode 0 las dos, y el mismo sha256 LF
`ac68abfc3a17628f`** sobre 5068 bytes. Y el registrador **sin argumentos**,
corrido dos veces mas: **exitcode 0 las dos y el mismo sha256 LF
`49cbe8bf0840e5d8`**, que es su idempotencia otra vez.

**Y UNA MEDICION QUE NO ESTABA ENCARGADA Y SALIO AL MEDIR, ANOTADA Y NO
ARREGLADA:** el arnes que nace hoy **el censo NO LO VE**. `PATRON_ARNES` es
`^vuelta(\d+).*(?:mutacion|caso_positivo|simular).*\.py$` y **mira el nombre del
fichero**, y este arnes vive en el carril `--mutacion` de
`vuelta189_tarea1a_registrar_acta189.py`, que no dice `mutacion` en su nombre.
**No lo introduce esta vuelta** (el registrador de la 188 tiene la misma forma, y
tampoco esta en la nomina) y **esta vuelta no lo arregla**, porque su encargo dice
*NADA MAS ENTRA EN ESTA VUELTA*. **Queda anotado con su cifra.**

**EL ARBOL:** `git diff --numstat -- dataset/` da **0 filas** al terminar, medido
por el propio instrumento, y **se midio antes de cada commit de tramo** desde el
tramo 4 en adelante.

<!-- FIN ANEXO DE TAREAS -->
