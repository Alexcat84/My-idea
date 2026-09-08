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
| **TAREA 3** | LA MESA `OP-L-02`, MEDIDA POR EL MISMO METODO QUE LA `OP-L-01` DE LA 207 Y LA `OP-L-03` DE LA 208. La vara SELLADA EN SU PROPIO COMMIT antes de cotejar nada, con cada cita comprobada VERBATIM, el reparto documental sellado antes de mirar y la busqueda POSITIVA con literales de control; el cotejo punto por punto con CUBRE, A MEDIAS o NO CUBRE **y su cita de fichero y linea en cada fila**; las DOS cuentas separadas. **NO SE CIERRA LA FICHA Y NO SE TOCA SU CAMPO `estado`** | **CERRADA. NO se cierra `OP-L-02`** | `SALIDA_V209_T3A_VARA.txt`, `SALIDA_V209_T3_COTEJO.txt` |
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
LF, con `sha256` disco **`9cf019a1c9a856f0`** y `sha256` LF **`9cf019a1c9a856f0`**, que calzan al digito con el contraste del
encargo (1180091 por las dos y `9cf019a1c9a856f0`) y con mi propio sello de
apertura. Al salir mide **1190145** bytes en disco y **1190145** bytes normalizado a LF,
con `sha256` disco **`772f6167da46fba8`** y `sha256` LF **`772f6167da46fba8`**.

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
`sha256` disco **`dda1cdd67042c733`** y `sha256` LF **`dda1cdd67042c733`**, que calzan al digito con el contraste del encargo.
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

### TAREA 3. LA MESA `OP-L-02`, MEDIDA POR EL MISMO METODO QUE LAS DOS ANTERIORES

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN de
`docs/loop/SALIDA_V209_T3A_VARA.txt` y `docs/loop/SALIDA_V209_T3_COTEJO.txt`
con `scripts/loop/_v209_t3_seccion.py`, que **cae en rojo si no puede leer
una**; y **la tabla del cotejo se reconstruye barriendo el fichero**, no se
copia a mano.

#### 3.a. LA VARA, SELLADA EN SU PROPIO COMMIT ANTES DE COTEJAR NADA

La vara vive en `scripts/loop/_v209_t3_vara.py` y quedo **committeada antes
de abrir ningun documento del cotejo**. El cotejo la **IMPORTA** y no puede
cambiarla: si pudiera, el sello no valdria para nada. Es el metodo que la 207
uso con `OP-L-01` y la 208 con `OP-L-03`, las dos veces bien.

**LA SEDE FINA ES `campo[indice]` Y NO UN NUMERO DE LINEA**, porque la ficha
entera vive en UNA sola linea de `docs/plan/OPERACIONES.jsonl`, la **42**, que
mide **7989** bytes en disco y **7989** bytes normalizado a LF. Decir *linea 42*
dieciocho veces no localiza nada.

| que se sella | cifra |
|---|---:|
| puntos de la vara | **18** |
| de ellos DOCUMENTALES | **13** |
| de ellos NO DOCUMENTALES | **5** |
| citas que NO aparecen VERBATIM en su campo | **0** |
| controles positivos que FALLAN | **0** |
| candidatos a NO DOCUMENTAL cuyo literal SI aparece en el corpus | **0** |
| discrepancias con el contraste del encargo | **0** |

**EL ESCARMIENTO, APLICADO Y NO SOLO CITADO.** Antes de sellar un punto como
NO DOCUMENTAL se busca su literal en el corpus y **la vara CAE EN ROJO si
aparece**: da **0**. Los tres primeros (`V.1`, `V.2` y `V.3`) **no se buscan
a proposito y se dice por que**: son campos de la propia ficha (`tipo`,
`orden`, `fecha_corte`) y su unica sede posible es ella. Y **la sede de la
propia ficha queda FUERA de esa busqueda**, porque encontrar ahi el literal de
su propio campo probaria que la ficha existe, no que tenga sede documental.

**LA BUSQUEDA VA TAMBIEN POSITIVA** (`EJECUTOR.md` 9, una busqueda negativa no
se puede citar sola), con un literal de control por cada uno de los **11**
documentos del corpus: **0 fallan**.

**Y LA PRIMERA CORRIDA DE LA VARA CAYO EN ROJO, POR MI CONTROL Y NO POR EL
FICHERO.** El control de `SALIDA_V170_T3_DEUDAS_DE_CORTE.txt` era la palabra
`marcador` y aparecia **0** veces: ese fichero habla del marcador **por su
sede y su cifra** (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl: 3388 filas`, en su
linea **48**) y **nunca escribe la palabra**. **Un control positivo que no
aparece no invalida el documento: invalida el control**, y para eso esta la
guarda. Quedo por `OP-L-02`, que aparece en su linea **9**. La correccion va
**declarada dentro del propio sello y con el texto viejo sin borrar**, y **no
toco ni un punto de la vara ni el reparto documental**.

#### 3.b. LOS DOS AVISOS DE ESTA FICHA, LOS DOS MEDIDOS

**LA `evidencia` TIENE UN SOLO ELEMENTO Y ES PROSA QUE NO NOMBRA NINGUN
FICHERO**, y por eso `vuelta150_3_relectura_expediente.py` la lista como la
unica de las tres mesas sin documento que medir. **Eso no la deja sin
cotejar:** se coteja contra lo que su prosa AFIRMA, que es una cifra con su
fecha de corte, y esa aritmetica se remide aqui. **CIFRA aritmeticas de la
ficha comprobadas: 11, de las que cuadran 11 y no cuadran 0.**
Las tres cifras de la `evidencia` cuadran entre si (11 mas 194 dan 205) y con
la particion de la `nota` (126 mas 79 dan 205), y **205 menos las 16 de la
segunda tanda dan los 189 del backlog**.

**Y `adjudicacion` Y `nota` SI TRAEN TEXTO, que es lo que las otras dos mesas
no tenian igual:** **260** y **5578** caracteres. **Ahi es donde vive lo que la
mesa decidio**, y de ahi salen la mayoria de los puntos de la vara.

**LAS DOS CIFRAS DEL MARCADOR, PUBLICADAS JUNTAS Y CADA UNA CON SU CORTE**, que
es lo que el encargo manda y lo que el banco `9.21` pide:

| cifra | corte | de donde sale |
|---:|---|---|
| **2.117** | **2026-08-11**, el `fecha_corte` de la ficha | `verificacion[1]`. **TESTIGO Y NO CONDICION** |
| **3388** | **7 sep 2026** | recomputado por mi de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` linea a linea |

**NO SE ARREGLA TOCANDO LA FICHA.** El instrumento no fallo, **la cifra se
quedo vieja** (banco `9.21`), y la clausula exige que la OPERACION no mueva el
marcador, **no que el marcador valga 2.117 hoy**. La `verificacion[3]` de la
propia ficha ya le puso el corte al lado el 4 sep 2026 por CORRECCION
DECLARADA, sin borrar el numeral viejo.

**MI RECOMPUTO DEL MARCADOR: 3388 filas, repartidas en A 551, B 72, C 5 y D 2760**,
con **3388** puestos distintos y **0** huecos. **Calza con el sello del auditor**
`docs/loop/SALIDA_MARCADOR_AUDITOR_V208.json`: **SI,**.

**UNA CAIDA MIA CAZADA ANTES DE PUBLICAR, Y VA MARCADA COMO `C.2`.** La primera
version del cotejo leia el puesto como `puesto`, y **ese campo no existe en ese
archivo**: se llama `puesto_intra`. `.get()` devolvia vacio en las **3388** filas,
el conjunto se quedaba con un solo valor y la salida publicaba **CIFRA puestos
distintos: 1** sobre un archivo de **3388** puestos. **Ese 1 no era una medicion:
era el uno de un patron roto**, que es justo lo que `EJECUTOR.md` 9 prohibe
publicar como hecho del mundo. Arreglado el campo, **queda ademas una guarda**
que comprueba que el campo se lee en todas las filas **antes** de publicar la
cifra, y que la declara NO COMPUTABLE si no. Va entera en la seccion 8.

#### 3.c. EL COTEJO PUNTO POR PUNTO, CON SU CITA EN CADA FILA

| punto | veredicto | sede citada | por que entra asi |
|---|---|---|---|
| `V.1` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `tipo`, y su criterio de HECHO en `docs/plan/08_VERIFICACION.md:29` | el campo dice 'MESA', y la fila 06 MESAS existe en su linea medida |
| `V.2` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `orden` | vale 2, la segunda de las tres mesas |
| `V.3` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `fecha_corte` | vale '2026-08-11', y es contra ese corte contra el que se juzgan sus cifras |
| `V.4` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `depende_de`, y las tres halladas en ese mismo fichero | las 3 dependencias existen; 0 no se encuentran |
| `V.5` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `evidencia[0]` | sus tres cifras cuadran entre si (11 mas 194 da 205) y con la particion de la nota (126 mas 79 da 205); 11 de 11 aritmeticas de la ficha cuadran |
| `V.6` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campos `verificacion[0]` y `nota` | las tres nominas SI se pueden nombrar desde la propia ficha (3 de 3), asi que NO hay parada por texto insuficiente |
| `V.7` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `verificacion[1]`, con su correccion en `verificacion[3]` | la clausula exige que la OPERACION no mueva el marcador, no que valga 2.117 hoy; las dos cifras van publicadas juntas con su corte (2.117 al 2026-08-11 y 3388 al 7 sep 2026) |
| `V.8` | **A MEDIAS** | `docs/plan/OPERACIONES.jsonl:42` campos `verificacion[2]`, `nota` y `adjudicacion` | 3 de 4 grupos del backlog llevan su motivo escrito y no solo su cuenta |
| `V.9` | **CUBRE** | `docs/INTRA_DOMINIO_VEREDICTOS.jsonl:recomputado entero, 3388 filas` y `docs/loop/SALIDA_MARCADOR_AUDITOR_V208.json:1` | mi recomputo da 3388 filas con A 551, B 72, C 5 y D 2760, identico a lo que la correccion declarada publica y al sello del auditor |
| `V.10` | **CUBRE** | `docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt:9` | la ruta existe y no mide cero bytes; de las 11 rutas del corpus fallan 0 |
| `V.11` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `adjudicacion` | la decision de la mesa esta escrita, y la `nota` le pone al lado su motivo y su cobertura, que es lo que la fila 06 MESAS exige |
| `V.12` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `adjudicacion`, cotejado contra el reparto por nomina de la `nota` | 2 A mas 14 D dan 16, y las tres nominas leidas (8 mas 5 mas 3) tambien dan 16 |
| `V.13` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `nota`, y las tres nominas en `docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt:45` | las tres estan NOMBRADAS y sus tres cuentas suman 16 |
| `V.14` | **CUBRE** | `docs/plan/LD_SALES_ROADMAP.md:48` a `docs/plan/LD_SALES_ROADMAP.md:195` | las 5 cabeceras estan, y su reparto contado de ellas da 1 A y 4 D, que es el `SALDO: 1 A y 4 D` de la ficha |
| `V.15` | **A MEDIAS** | `docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt:35` | la salida sellada trae las 6 nominas y suma 0 pares SIN veredicto de ninguna sede, o sea que la parte de `cero pares sin veredicto` CUBRE; pero `cobertura COMPLETA` solo se sostiene en la convencion LITERAL, porque la NOMINA 2 publica `0 de 0` con 5 de sus 6 miembros colapsados por alias. Las dos convenciones van publicadas y manda la LITERAL |
| `V.16` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `nota` | los cuatro grupos suman 189, y 205 menos las 16 de la segunda tanda tambien dan 189 |
| `V.17` | **CUBRE** | `scripts/vuelta16_generar_actos.mjs:8` y el resolutor de la casa | 6 miembros escritos, 6 vivos tras resolver y 15 pares posibles, recomputado por mi con `mapa_de_alias()` y `resolver()` |
| `V.18` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:las 71 fichas barridas` | el barrido da 0 apariciones, y su CONTROL POSITIVO da 47 fichas con `nodos` no vacio, asi que el cero no es el cero de un patron roto |

**CIFRA filas del cotejo SIN cita de fichero y linea: 0.** Ninguna sin cita,
que es lo que el encargo exige.

**LAS MEDICIONES QUE SOSTIENEN ESAS FILAS, CADA UNA CON SU CIFRA:**

| que se midio | cifra |
|---|---:|
| las tres nominas de `verificacion[0]` que la ficha NOMBRA | **3** de 3 |
| cabeceras `LD-66` a `LD-70` halladas en su documento | **5** de 5 |
| reparto de esas cinco, contado de sus cabeceras | **1** A y **4** D |
| nominas de la ficha en su salida sellada de la 169 | **6** |
| pares SIN veredicto de ninguna sede, sumando las seis | **0** |
| fichas barridas para la busqueda negativa | **71** |
| apariciones de los nodos del acto en `nodos`, `preservar`, `eliminar` y `superviviente` | **0** |
| control positivo del mismo barrido: fichas con `nodos` no vacio | **47** |
| rutas del corpus comprobadas, y de ellas las que fallan | **11** y **0** |
| dependencias de la ficha que NO existen | **0** |
| grupos del backlog, y de ellos los que llevan su motivo escrito | **4** y **3** |

**LA BUSQUEDA NEGATIVA SE RE-VERIFICO EN VEZ DE CITARSE** (`EJECUTOR.md` 9): la
`nota` declara un barrido de las fichas buscando los nodos del acto, y aqui se
repite entero sobre las **71** de hoy. Da **0** apariciones, **y su CONTROL
POSITIVO da 47 fichas con `nodos` no vacio**, asi que ese cero **no es el cero
de un patron roto**.

**LA DISCREPANCIA QUE ENCUENTRO Y QUE NO RESUELVO COPIANDO** (`EJECUTOR.md` 2).
La `nota` dice *cuadrantes 15 de 15 con 8 A y 7 D*, y la **NOMINA 2** de su
propia salida sellada, que es la de los cuadrantes, publica **0 de 0** con 6
miembros escritos, 1 vivo tras resolver y 5 colapsados por alias. **Son las dos
convenciones y la ficha habla en LITERAL:** el **15** son los pares de SEIS
miembros escritos, que es el universo que habia en el `fecha_corte`
**2026-08-11**; el **0 de 0** es la foto RESUELTA de hoy, **7 sep 2026**,
despues de que cinco de esos seis se fundieran. **Manda la LITERAL** por la
adjudicacion `6.6` del acta 208, **y la resuelta va al lado**. Por eso la `V.15`
entra **A MEDIAS** y no CUBRE ni NO CUBRE.

**LAS DOS CUENTAS, SEPARADAS Y JUNTAS, COMO EN LA 208:**

| cuenta | cifra |
|---|---|
| **la del SELLO**, escrita ANTES de mirar | **18** puntos, **13** DOCUMENTALES y **5** NO DOCUMENTALES |
| **la de los VEREDICTOS**, sacada DESPUES de mirar | **18** emitidos: **16** CUBRE, **2** A MEDIAS y **0** NO CUBRE |

**LA COBERTURA, MEDIDA Y NO NARRADA: 16 de 18 CUBREN**, y su lista NOMINAL de
los que no cubren entero es **`V.8`** (**3** de **4** grupos del backlog
llevan su motivo escrito: el de los **126 que esperan destejido** trae la
cuenta pero no un motivo propio) y **`V.15`** (la cobertura COMPLETA solo se
sostiene en la convencion LITERAL). **Ningun `NO CUBRE`.**

#### 3.d. NO SE CIERRA `OP-L-02` Y NO SE TOCA SU CAMPO `estado`

**AQUI SE MIDE, SE PROPONE Y SE PARA.** La autorizacion del 2.c era **SOLO**
para `OP-L-01`, y la adjudicacion de esta mesa es del auditor. **Lo que
propongo, y no lo adjudico yo:** con **16 de 18** puntos cubriendo, **0 NO
CUBRE** y los dos A MEDIAS declarados con su motivo, la ficha esta **a un
juicio de cerrarse**, y el juicio no es mio.

**Y PARA PROBAR QUE NO LA TOQUE, LA SEDE VA PUBLICADA POR LAS DOS CONVENCIONES
AL ENTRAR Y AL SALIR DE ESTA TAREA:**

| `docs/plan/OPERACIONES.jsonl` | bytes en disco y bytes normalizado a LF | `sha256` disco |
|---|---:|---|
| **AL ENTRAR** | **513043** y **513043** | **`e96dbe74485814e9`** |
| **AL SALIR** | **513043** y **513043** | **`e96dbe74485814e9`** |

**Los cuatro valores son identicos y el `estado` sigue en `LISTA`.** Los `sha256`
de esta tabla **no** son los de mi sello de apertura, y eso tambien se dice: la
TAREA 2 movio ese fichero **antes** de esta tarea, con su propia guarda de una
linea. Lo que esta tabla prueba es que **la TAREA 3 no lo movio**, que es lo
que el `3.d` pide.

#### 3.e. LA TAREA CABE ENTERA CON SUS GUARDAS, Y NO HAY PARADA

**NO QUEDA ABIERTA.** Los **18** puntos estan cotejados, las **18** filas llevan
su cita, el reparto documental se sello antes de mirar y las dos cuentas van
publicadas.

**Y EL CASO DE PARADA QUE EL ENCARGO AVISA NO SE CUMPLE, Y LO MIDO EN VEZ DE
SUPONERLO.** `verificacion[0]` habla de *las tres nominas afectadas* y no las
nombra; **la `nota` SI las nombra las tres**, con su literal y su cuenta:
*cuadrantes de mercado (8)*, *ecuacion de valor (5)* y *el bloque humano de la
supervision de la IA (3)*, y las tres cuentas suman 16. **CIFRA de las tres que
la ficha nombra: 3 de 3.** No hay que adivinar ninguna, asi que **la ficha SI
alcanza para cotejarse sin decidir y NO hay PARADA por este motivo**
(`AUDITOR.md` 3).

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

