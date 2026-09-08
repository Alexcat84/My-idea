# REPORTE DE LA VUELTA 209 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v209_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se
> hicieron.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO EN LA 208, Y ESO
> SIGUE SIENDO MI `C.1` DE LA 207 REMEDIADA.** No se teclean: se **IMPORTAN de
> `anexar_tarea_al_reporte.py`**, que es el instrumento que las lee, y se comprueba
> ANTES de tallar que es lo que ese instrumento exige. **Las cuatro no se citan
> literalmente en esta prosa a proposito**: la guarda las cuenta sobre el fichero
> entero y una cita en prosa las duplicaria. **Y el texto se COMPONE EN MEMORIA,
> SE JUZGA ENTERO Y SOLO SE ESCRIBE SI EL JUICIO DA CERO FALLOS**, que es la otra
> mitad del mismo remedio: escribir primero y validar despues es lo que dejo el
> `REPORTE.md` pisado en la 207 y en la 208.
>
> **EL REPORTE DE LA 208 TAMPOCO ESTABA ARCHIVADO AL ENTRAR, Y ESO SE DECLARA EN
> VEZ DE COPIARSE** (`EJECUTOR.md` 2, EL INSTRUMENTO MANDA). Mi sello de apertura,
> `docs/loop/SALIDA_V209_APERTURA.txt`, escrito **antes de la primera operacion**,
> publica `CIFRA docs/loop/reportes/REPORTE_V208.md existe al entrar: NO`. Lo
> archiva el PASO 0, que es su sitio, y su salida va sellada en
> `docs/loop/SALIDA_V209_PASO0_ARCHIVAR.txt`.
>
> **TRES SUB-TAREAS.** El tope esta en CINCO (`AUDITOR.md` 6.2, adjudicacion `6.8`
> del acta 208: la 207 y la 208 cerraron las dos su propio reporte con
> `cerrar_reporte.py`), y el encargo pone TRES y no cinco porque la TAREA 2 toca
> una sede de `docs/plan/`.
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA**
> (`AUDITOR.md` 6.1, adjudicacion `6.10` del acta 208). La ultima fue la **205** y
> la siguiente es la **210**. La **seccion 9 cierra igual**, con el **HUECO
> DECLARADO Y MEDIDO** y sus **tres piezas juntas**: el nombre del fichero, los
> bytes medidos **distinguiendo el cero de ausencia del cero de fichero vacio**, y
> la atribucion.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Todo lo que esta vuelta
> escribe son ficheros `_v209_*` **con prefijo de guion bajo, fuera del censo y
> fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda. **EL
> TRABAJO ES EL PLAN**, y por eso las TAREAS 2 y 3 son las dos mesas que quedan.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 209`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TRES TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS DE LA VUELTA 208. Leer el acta 208 entera y REMEDIR sus cifras de crecimiento; escribir `R.73` en `docs/PENDIENTES.md` **por adicion pura y en su sede**, con el numero COMPUTADO por `scripts/loop/serie_de_registros.py` corrido a la entrada y a la salida y las dos puntas publicadas; y registrar **las diez adjudicaciones** `6.1` a `6.10` por su numero y su linea medida, diciendo cuales cierran pendiente, con la vara del `4.1` del acta 202 corrida con el lector IMPORTADO y sin tocarle una linea | **CERRADA** | `SALIDA_V209_T1_REGISTROS.txt`, `SALIDA_V209_T1_REGISTROS_2.txt` |
| **TAREA 2** | LAS DOS CIFRAS DE `OP-L-01` QUE SIGUEN MAL EN `docs/plan/LECTURAS_DIRIGIDAS.md`. **Primero el DENOMINADOR** recomputado con el resolutor puesto (`P.1`) y leyendo la nomina de miembros de `docs/INTRA_DOMINIO_INFORME.md`, no de la tabla; despues las dos correcciones escritas por el carril del banco `9.10`, con CORRECCION DECLARADA, el texto viejo entero encima y **la marca en la celda de nombre** (adjudicacion `6.5`). Y **SE CIERRA `OP-L-01`** tocando SOLO su campo `estado`, con las tres guardas del encargo | **CERRADA. `OP-L-01` queda `HECHA`** | `SALIDA_V209_T2A_DENOMINADOR.txt`, `SALIDA_V209_T2B_CORRECCIONES.txt`, `SALIDA_V209_T2C_CERRAR_OPL01.txt` |
| **TAREA 3** | LA MESA `OP-L-02`, MEDIDA POR EL MISMO METODO QUE LA `OP-L-01` DE LA 207 Y LA `OP-L-03` DE LA 208. La vara SELLADA EN SU PROPIO COMMIT antes de cotejar nada, con cada cita comprobada VERBATIM, el reparto documental sellado antes de mirar y la busqueda POSITIVA con literales de control; el cotejo punto por punto con CUBRE, A MEDIAS o NO CUBRE **y su cita de fichero y linea en cada fila**; las DOS cuentas separadas. **NO SE CIERRA LA FICHA Y NO SE TOCA SU CAMPO `estado`** | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS DE LA VUELTA 208

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN de
`docs/loop/SALIDA_V209_T1_REGISTROS.txt` y de
`docs/loop/SALIDA_V209_T1_REGISTROS_2.txt` con
`scripts/loop/_v209_t1_seccion.py`, que **cae en rojo si no puede leer una**
o si encuentra mas de una coincidencia. Es la letra de `EJECUTOR.md` 1, LA
TABLA SE CUENTA DE SU FICHERO.

#### 1.a. EL CRECIMIENTO DEL ACTA 208, REMEDIDO CON MIS COMANDOS

El commit del acta se leyo de `git log` y no se tecleo (`EJECUTOR.md` 1, LA
IDENTIDAD SE LEE DE GIT): **`32fc034831256806d0749547efb0e8869d6f44ad`**, con padre **`174717b809400c7d766c298bd79790956238a917`**.
**EL PADRE SE PIDIO CON `~1` Y NUNCA CON EL CIRCUNFLEJO**, y ademas se
comprobo ANTES DE RESTAR que los dos blobs son DISTINTOS: restar dos valores
iguales daria un cero que no es una medicion. La salida lo dice literal:
`los dos blobs son IDENTICOS: NO`.

| que se mide | medido en esta vuelta | contraste del encargo | calza |
|---|---:|---:|---|
| acta ANTES, bytes en disco y bytes normalizado a LF | **4820516** y **4820516** | 4820516 | SI |
| acta DESPUES, bytes en disco y bytes normalizado a LF | **4849108** y **4849108** | 4849108 | SI |
| `sha256` disco y `sha256` LF del acta | **`2abc86822340d1bd`** y **`2abc86822340d1bd`** | `2abc86822340d1bd` | SI |
| linea en que abre la seccion del acta 208 | **73083** | 73083 | SI |

**CIFRA crecimiento del acta: 28592 bytes en disco y 28592 bytes normalizado a LF**,
con **443** lineas anadidas y **0** borradas por `git diff --numstat`. **El
acta solo crece por anexion y su cero de borradas lo prueba.**

**CIFRA discrepancias con el contraste del encargo en el 1.a: 0.** Las seis
celdas cotejadas calzan al digito, asi que **no hay ninguna discrepancia que
declarar en este apartado**, y eso se dice midiendolo y no suponiendolo.

**LO QUE SI DECLARO, PORQUE NO ES DISCREPANCIA PERO LO PARECE:** el acotado
del cuerpo que hace la vara publica `lineas 73083 a 73525, 443 lineas`, y el
fichero mide **73525** lineas por `split` y **73524** por `wc -l`. **Son las
dos convenciones de siempre, no dos mediciones que peleen**, y lo digo en vez
de dejar que parezca un desajuste de una linea.

#### 1.b. `R.73`, ESCRITA POR ADICION PURA Y EN SU SEDE

**EL NUMERO NO ESTA TECLEADO:** lo computa `scripts/loop/serie_de_registros.py`
recomputando la serie de sus DOS sedes, **corrido a la entrada y a la
salida**, y **las dos puntas se publican**.

| la serie `R.N` | punta de ENTRADA | punta de SALIDA | contraste del encargo |
|---|---:|---:|---:|
| entradas | **64** | **65** | 64 |
| de ellas en `docs/PENDIENTES.md` | **63** | **64** | 63 |
| de ellas en `docs/plan/CORRECCIONES_A_APLICAR.md` | **1** | **1** | 1 |
| colisiones | **0** | **0** | 0 |
| huecos | **0** | **0** | 0 |
| mayor escrita | **R.72** | **R.73** | R.72 |
| siguiente libre | **R.73** | **R.74** | R.73 |

**LA SEDE, POR LAS DOS CONVENCIONES Y EN SUS DOS PUNTAS.** Al entrar,
`docs/PENDIENTES.md` mide **1180091** bytes en disco y **1180091** bytes normalizado a
LF, con `sha256` LF **`9cf019a1c9a856f0`**, que calza al digito con el contraste del
encargo (1180091 por las dos y `9cf019a1c9a856f0`) y con mi propio sello de
apertura. Al salir mide **1190145** bytes en disco y **1190145** bytes normalizado a LF,
con `sha256` LF **`772f6167da46fba8`**.

**CIFRA crecimiento de la sede: 10054 bytes en disco y 10054 bytes normalizado a
LF.** La entrada compuesta mide **10053** bytes y trae **166** lineas, con **0**
guiones largos y **0** guiones medios.

**LAS DOS GUARDAS DE LA ADICION PURA, LAS DOS EN CERO:**

- `git diff --numstat -- docs/PENDIENTES.md` da **167** anadidas y **0**
  borradas. **CERO BORRADAS**, que es lo que el encargo exige.
- La guarda de texto viejo corrio entera encima: **CIFRA lineas del texto de
  ENTRADA que NO estan, en orden, en el de SALIDA: 0**.

**SEGUNDA CORRIDA IDEMPOTENTE:** crece **0** bytes en disco y **0** bytes
normalizado a LF, con **0** entradas escritas. Su salida entera va sellada en
`docs/loop/SALIDA_V209_T1_REGISTROS_2.txt`.

#### 1.c. LAS DIEZ ADJUDICACIONES, POR SU NUMERO Y SU LINEA MEDIDA

**LA VARA DEL `4.1` DEL ACTA 202 CORRIO CON EL LECTOR IMPORTADO Y SIN TOCARLE
UNA LINEA.** `vara_sobre()` viene de `scripts/loop/_v208_t1_registros.py` y
`medir_acta()` de `scripts/loop/_v203_reparto_de_actas_viejas.py`. **IMPORTAR
NO ES CLONAR** (acta 206 `6.5`), y la moratoria de `AUDITOR.md` 6.3 queda
intacta: **ningun lector se ensancho**.

**SU PRUEBA POR MUTACION CORRIO ANTES DE ESCRIBIR NADA Y NO SE HEREDO DE OTRA
CORRIDA** (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): sobre
`docs/loop/SALIDA_V209_T1_REGISTROS.txt`, **9 casos, 9 verdes y 0 rojos**,
y la segunda pasada muta el esperado y exige que cada caso CAIGA: **9 de 9
caen**. Un caso que no puede fallar no probaria nada.

**LOS CUATRO NUMERALES SALEN COMPUTABLES SOBRE LAS DOS ACTAS: 4 de 4 sobre la
208 y 4 de 4 sobre la 207.** No hubo que declarar ninguno NO COMPUTABLE, y
por eso no se ensancho nada.

| clave | linea medida | que pendiente cierra | titulo, literal del acta |
|---|---:|---|---|
| `6.1` | 73309 | el CHOQUE DE NUEVE ACTAS entre el remedio del acta 205 y `AUDITOR.md` 1 | `6.1` EL REMEDIO DEL ACTA 205 SE AFINA, Y NO ES DOCTRINA NUEVA NI TOCA |
| `6.2` | 73329 | `P.1` del reporte de la 208 | `6.2` LA `P.1` SE ADJUDICA: LA `V.3` DE `OP-L-01` CUBRE, Y NO POR GENEROSIDAD. |
| `6.3` | 73336 | (ninguno) | `6.3` `OP-L-01` NO SE CIERRA AUN, Y EL MOTIVO ES OTRO Y ESTA MEDIDO EN LA `5.2 |
| `6.4` | 73344 | `P.2` del reporte de la 208 | `6.4` LA `P.2` SE ADJUDICA: `OP-L-03` SE CIERRA, Y LAS DOS CUENTAS VAN JUNTAS. |
| `6.5` | 73359 | `P.3` del reporte de la 208 | `6.5` LA `P.3` SE CONTESTA SIN TOCAR NINGUN LECTOR.** El instrumento sellado d |
| `6.6` | 73371 | `PD.1` del reporte de la 208 | `6.6` LA `PD.1` SE ADJUDICA SIN DOCTRINA NUEVA: MANDA LA CONVENCION DEL CORTE |
| `6.7` | 73381 | los TRES DISCUTIBLES del reporte de la 208, los tres ADMITIDOS | `6.7` LOS TRES DISCUTIBLES QUEDAN ADMITIDOS, Y EL MARCADO FUNCIONO EN LOS TRES |
| `6.8` | 73400 | (ninguno) | `6.8` EL TOPE SIGUE EN CINCO Y LE PONGO TRES.** El disparador de `AUDITOR.md` |
| `6.9` | 73408 | (ninguno) | `6.9` LA MORATORIA SE RESPETO Y LO MIDO YO: 19 de 19 CON PREFIJO, 0 SIN EL**, |
| `6.10` | 73412 | (ninguno) | `6.10` LA BATERIA NO CORRE EN LA 209.** Cadencia de cinco (`AUDITOR.md` 6.1): |

**CIFRA adjudicaciones medidas por la vara: 10. CIFRA de ellas que cierran
pendiente: 6. CIFRA de esas que el acta NO trae: 0.** Las cuatro restantes
(`6.3`, `6.8`, `6.9` y `6.10`) **no cierran ningun pendiente numerado**, y eso
se dice en vez de inflar la cuenta.

**EL CERO FALSO QUE NO SE PUBLICA, Y YA NO ES ELECCION MIA.** `titulo_de()`
cuenta las caidas por la forma antigua `CAIDA n`, y el acta 208 escribe las
suyas como `9.1` a `9.4` y `4.1`. Corrido tal cual, el titulo diria **las 0
caidas propias del auditor** sobre un acta que trae **4**. Se le pasa el dato
contado por la forma vigente, **con las dos cuentas y el titulo crudo escritos**,
que es exactamente la letra general que el acta 208 adjudico en su `6.7` al
ADMITIR mi `D.1`. **Se cambia el dato, no la maquina.**

#### 1.d. LA CORRECCION RECIBIDA, SIN CORRECCION QUE APLICAR

El acta 208 levanta **una sola caida contra el ejecutor de esa vuelta**, su
`4.1`: la glosa de la moratoria publicaba `16` ficheros **sin su corte** cuando
el corte de cierre daba `19`. **La recibo y la escribo aqui**, y el encargo ya
dice que **no mueve ningun dato**: el propio auditor midio **19 de 19 con
prefijo de guion bajo y 0 sin el**, asi que la conclusion aguanta y la
moratoria se respeto. **No hay correccion que aplicar en esta tarea.**

**Y LA CAUSA QUEDA APUNTADA PARA NO REPETIRLA:** `_v208_cierre.py` cuenta los
ficheros que la vuelta anadio a `scripts/loop/` **y va en el mismo commit que
cuenta**, asi que su cifra nace corta en uno por construccion. **No lo arreglo,
que es moratoria**: en esta vuelta la glosa lleva su corte, que es el remedio
barato del banco `9.21` y el que el acta 208 encarga en su `7.2`.

#### 1.e. LA DEUDA DE REGISTROS, REMEDIDA AL CIERRE

**CIFRA actas de la 173 a la 208 sin entrada propia: 5** (201, 202, 203, 204, 205). Bajo de 6 a
**5** con `R.73`, y las que quedan son de vueltas anteriores a la 206.

### TAREA 2. LAS DOS CIFRAS DE `OP-L-01` QUE SEGUIAN MAL EN SU PROPIO DOCUMENTO

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN de
`docs/loop/SALIDA_V209_T2A_DENOMINADOR.txt`,
`docs/loop/SALIDA_V209_T2B_CORRECCIONES.txt` y
`docs/loop/SALIDA_V209_T2C_CERRAR_OPL01.txt` con
`scripts/loop/_v209_t2_seccion.py`, que **cae en rojo si no puede leer una**.

#### 2.a. EL DENOMINADOR, RECOMPUTADO ANTES DE ESCRIBIR NADA

**EL RESOLUTOR VA PUESTO** (`P.1`): **3853** `node_id` distintos en disco y
**761** alias en el mapa, con `mapa_de_alias()` y `resolver()` **importados**
de `vuelta166_tarea2_correccion_op_l_01.py`. **La nomina se leyo de
`docs/INTRA_DOMINIO_INFORME.md`, lineas `5314` a `5319`, y NO de la tabla**,
que es lo que el encargo manda y lo que el hallazgo `7.2` del acta 207
explica: escribir los leidos sobre un denominador sin comprobar seria
arreglar la mitad visible.

| nomina | LITERAL, que es la que MANDA | RESUELTA, publicada AL LADO | fundidos |
|---|---|---|---:|
| junta asesora | **4** miembros y **6** pares | **2** miembros y **1** pares | **2** |
| **seleccion de canal** | **6** miembros y **15** pares | **6** miembros y **15** pares | **0** |

**MANDA LA CONVENCION DEL CORTE DE LA FICHA, O SEA LA LITERAL, Y NO LA VUELVO
A DECIDIR:** es la adjudicacion `6.6` del acta 208, por el banco `9.21` mas
`P.1`. El `fecha_corte` de `OP-L-01` es **2026-08-11** y la resuelta es la
foto de hoy, **7 sep 2026**, que se publica **al lado y nunca en su lugar**.
En la seleccion de canal **las dos convenciones dan lo mismo**, con **0**
miembros fundidos; en la junta asesora **no**, y por eso las cuatro cifras van
las cuatro escritas en vez de elegir una en silencio.

**LA NOMINA ESTA VERIFICADA CONTRA EL GRAFO** en
`docs/INTRA_DOMINIO_INFORME.md:5314` a `:5319`, y su **CORRECCION DECLARADA
del 11 ago 2026** vive en la `:5321`, literal: *son SEIS y no cinco*. Los seis
existen hoy en el grafo, **0** fuera.

**LOS LEIDOS TAMPOCO SE HEREDAN:** hay **27** cabeceras `LD` en el documento y
**2** lecturas dirigidas cuyos dos extremos, **tras resolver**, caen dentro de
esta nomina: `LD-02` (**D**) y `LD-03` (**A**). Cobertura medida: **10 de 15**.

**CIFRA discrepancias con el contraste del encargo en el 2.a: 0.** Las nueve
celdas cotejadas calzan al digito.

#### 2.b. LAS DOS CORRECCIONES, POR EL CARRIL DEL BANCO `9.10` Y POR ADICION PURA

**NO SE PISO NI UNA LINEA.** Las dos filas viejas siguen enteras y sin tachar,
y las dos nuevas se anaden detras de su tabla con su CORRECCION DECLARADA.

| que | donde queda hoy, remedido sobre el fichero de salida |
|---|---|
| la fila VIEJA de la tabla por nomina | linea **31** (entraba en la 31) |
| la fila VIEJA de que nominas cambian | linea **339** (entraba en la 291) |
| la fila NUEVA de la tabla por nomina | linea **79** |
| la fila NUEVA de que nominas cambian | linea **377** |

**LA VIEJA DE LA 291 SE MUEVE A LA 339 Y LA DE LA 31 SE QUEDA DONDE ESTABA, Y
LO DIGO EN VEZ DE DEJAR QUE PAREZCA UN PISOTON:** la primera adicion va
**debajo** de la fila 31 y **encima** de la 291, asi que la de abajo cambia de
numero. **El numero cambia; el texto, no**, y la guarda lo prueba.

**LA MARCA EN LA CELDA DE NOMBRE NO ES UNA ELECCION MIA:** es la adjudicacion
`6.5` del acta 208, y las dos filas nuevas llevan
**`(FILA CORREGIDA EN LA VUELTA 209)`**. El motivo esta medido en esa misma
adjudicacion: un lector que toma la primera fila que casa no distingue la vieja
de la nueva sin ella.

**LAS CUATRO GUARDAS DEL 2.b, LAS CUATRO CORRIDAS ANTES DE ESCRIBIR:**

- **(a) y (b):** cada ancla y cada fila vieja aparece **exactamente una vez**,
  y las lineas 31 y 291 se cotejaron **VERBATIM** contra su numero antes de
  tocar nada. **CIFRA guardas que fallan: 0.**
- **(c) EL CONTROL POSITIVO DE LA COLUMNA `fuera de cola`**, que es lo que
  impide computar una columna que no significa lo que se cree: sobre la fila
  VIEJA, *posibles menos leidos* tiene que dar *fuera de cola*, y da **CALZA**.
  Solo entonces se computa el **5** de la fila nueva con esa misma regla.
- **(d)** al terminar, **CIFRA lineas del texto de entrada que NO estan, en
  orden, en el de salida: 0**.

**LA SEDE, POR LAS DOS CONVENCIONES Y EN SUS DOS PUNTAS.** Entra en **214916**
bytes en disco y **214916** bytes normalizado a LF, con `sha256` disco **`dda1cdd67042c733`** y
`sha256` LF **`dda1cdd67042c733`**, que calza al digito con el contraste del encargo.
Sale en **219178** bytes en disco y **219178** bytes normalizado a LF, con `sha256`
disco **`a8ba1749b9a3fa13`** y `sha256` LF **`a8ba1749b9a3fa13`**.
**CIFRA crecimiento: 4262 bytes en disco y 4262 bytes normalizado a LF.**
`git diff --numstat` sobre esa sede da **78** anadidas y **0** borradas:
**CERO BORRADAS**, que es lo que el encargo exige.

**UNA CAIDA MIA, CAZADA ANTES DE PUBLICAR, Y VA MARCADA COMO `C.1`.** La
primera version del 2.b leia las cifras del fichero de salida **entero** con
una guarda de *exactamente una coincidencia*. **La guarda paso y la cifra salio
mal igual:** el patron de `fundidos` exigia una linea de detalle detras, la
seleccion de canal tiene **0** fundidos y por tanto **ninguna**, y la unica
coincidencia del fichero era **la de la JUNTA ASESORA, que tiene 2**. Iba a
publicar que la seleccion de canal tiene miembros fundidos cuando no tiene
ninguno. **Una guarda de unicidad sobre un fichero con dos nominas no es una
guarda de identidad**, y el arreglo no fue afinar el patron sino **acotar el
trozo** a su nomina, con una comprobacion de que el bloque de la otra queda
fuera. Va entera en la seccion 8.

#### 2.c. `OP-L-01` QUEDA CERRADA, Y SE DICE CON SUS DOS CUENTAS

**SU CRITERIO DE HECHO QUEDA CUMPLIDO.** `docs/plan/08_VERIFICACION.md`, fila
**06 MESAS**, linea **29**, pide *cada decision escrita con su motivo y su
cobertura al lado (banco 9.26)*, y con el 2.b hecho la decision de la mesa lleva
**la cobertura buena al lado**: **10 de 15, INCOMPLETA y por tanto PROVISIONAL**.
**Y SU VARA QUEDA EN 11 DE 11** por la adjudicacion `6.2` del acta 208: el banco
`9.26` **contempla lo PROVISIONAL en vez de prohibirlo** (*mientras falte un par,
la forma es PROVISIONAL y se dice asi*), asi que una cobertura de **10 de 15**
escrita como PROVISIONAL **CUBRE**.

**LAS TRES GUARDAS DEL ENCARGO, LAS TRES EN VERDE. VEREDICTO DEL INSTRUMENTO:
VERDE.**

**(1) EL VALOR VIEJO SE LEYO Y SE PUBLICA AL LADO DEL NUEVO:** el campo `estado`
de `OP-L-01` pasa de **`LISTA`** a **`HECHA`**, leidos los dos del fichero. La ficha
esta en la linea **41**, trae **18** campos, y **17 de 17** campos distintos del
`estado` **no se movieron**.

**EL VALOR NUEVO NO SE INVENTO.** `HECHA` ya es vocabulario del propio fichero:
lo llevaban **29** de las **71** fichas antes de tocar nada. Estrenar un valor
que no existiera en la sede seria doctrina nueva, y eso no lo decide el ejecutor.

**(2) LA SEDE, POR LAS DOS CONVENCIONES, ANTES Y DESPUES, CON SUS DOS `sha256`:**

| `docs/plan/OPERACIONES.jsonl` | bytes en disco y bytes normalizado a LF | `sha256` disco | `sha256` LF |
|---|---:|---|---|
| **ANTES** | **513043** y **513043** | **`829c583eb779cab6`** | **`829c583eb779cab6`** |
| **DESPUES** | **513043** y **513043** | **`e96dbe74485814e9`** | **`e96dbe74485814e9`** |

Los bytes no se mueven porque `LISTA` y `HECHA` miden lo mismo, **y los
`sha256` si cambian**, que es lo que prueba que algo se escribio. Los de ANTES
calzan al digito con el contraste del encargo y con mi sello de apertura.

**(3) UNA LINEA CAMBIADA Y NI UNA MAS, Y NINGUN OTRO `id_op` MOVIDO:**
`git diff --numstat` da **1** fichero tocado, **1** anadida y **1** borrada.
El censo de `id_op` y `estado` se cotejo **entero**, las **71** fichas contra las
**71**: **CIFRA fichas que se movieron: 1**, y es `OP-L-01`. **CIFRA otros
`id_op` cuyo estado cambio: 0.** El reparto pasa de **29** `HECHA` y **42**
`LISTA` a **30** y **41**.

**LA CIRUGIA FUE DE TEXTO, NO DE JSON, Y ESO ES LO QUE HACE POSIBLE LA GUARDA
(3).** Se sustituyo el par `estado` **dentro de su linea y solo ahi**, comprobado
que aparece exactamente una vez en ella. Volver a serializar el JSON reordenaria
claves o cambiaria espaciados y ensuciaria el `numstat` de las demas lineas, que
es justo lo que la guarda mide.

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

