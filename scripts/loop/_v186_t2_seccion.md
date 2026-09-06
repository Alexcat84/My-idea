### TAREA 2. LAS TRES REPARACIONES, LA ESCALADA Y EL CIERRE DE DOS REPORTES. CERRADA

**LO QUE ESTA TAREA SOSTIENE, EN UNA LINEA: las dos adjudicaciones del acta 186
que dejaban a `cerrar_reporte.py` diciendo dos cosas del mismo caso quedan
aplicadas, cada una con su arnes propio; el carril de CIERRE TARDIO existe y se
computa de git; el reporte de la 184 CIERRA EN VERDE con sus diez cifras sin
pareja DECLARADAS una a una; y la escalada de la `2.d` esta en codigo y su arnes
prueba que HABRIA CAZADO la `R.1`.**

#### 2.a LA PIEZA (4) DEJA DE LLEVAR SU PROPIA COPIA DE LA REGLA. ES LA `PD.6`

La comparacion `ajena != vuelta` vivia **dos veces** en el fichero, medido en el
bloque de apertura de esta vuelta antes de tocar nada: **lineas 438 y 905**. La
de la linea 438 vive en `rama_de_la_seccion9()`, que la 185 ya reparo; la de la
905 era la copia de la pieza (4), que no recibia la evidencia de los tramos.

**LO QUE SE HIZO, Y ES LA MITAD QUE IMPORTA:** la pieza (4) **NO recibio una
copia sincronizada**. `piezas_que_faltan()` gano un sexto parametro,
`tramos_sellados_en_esta_vuelta`, con valor por defecto `None`, y la pieza (4)
**LLAMA** a `rama_de_la_seccion9()` y cae solo cuando esa rama dice `ROJO`. En
`main()` ese valor **se computa con `tramos_por_vuelta()`** y se le pasa la misma
lista que ya recibia la rama: **no se anadio ninguna opcion de linea de ordenes**,
porque una evidencia que se puede teclear no es una evidencia.

**EL ROJO VIEJO NO SE REESCRIBIO:** la pieza (4) sigue cayendo con su texto de
hoy, palabra por palabra, y el arnes lo exige letra por letra.

Los casos, todos cayendo al mutar su esperado
(`docs/loop/SALIDA_V186_T2A_MUTACION_PIEZA4.txt`, **3601 bytes en disco y 3601 bytes normalizados a LF**):

| caso | que exige | resultado |
|---|---|---|
| A | la bateria de la 183 cerrando la 184 CON tramos sellados: la pieza (4) NO falta | CALZA |
| B | la misma con la lista VACIA: falta, con el motivo LITERAL de hoy | CALZA, letra por letra |
| C | la bateria de la 185 cerrando la 184, con tramos y sin ellos: falta las dos veces | CALZA |
| D | el defecto `None` se comporta igual que la logica vieja, en 8 escenarios | **difieren en 0** |
| E | las apariciones de la comparacion en el fichero: se exige **1** | **2 crudas** (lineas 438 y 917) y **1 en codigo** |

**EL CASO D NO SE AFIRMA, SE MIDE:** el arnes lleva dentro una copia declarada de
la logica vieja de la pieza (4) y compara escenario a escenario. **Difieren en 0
de 8.**

**Y EL CASO E CUENTA APARTE LAS LINEAS DE COMENTARIO, Y SE DICE EN VEZ DE
ESCONDERLO.** La reparacion deja un comentario que NOMBRA la comparacion para
explicar por que la pieza (4) llama en vez de comparar, y un comentario no es una
copia de la regla. Por eso el conteo crudo da **2** y el de codigo da **1**, y
**las dos cifras se publican**. El propio arnes prueba que sabe contar: sobre un
texto fabricado con dos copias en codigo y una en comentario, saca **2 en codigo
y 3 crudo**.

#### 2.b LA PIEZA (2) DEJA DE CAER SOBRE UNA CITA. ES LA `PD.5`

Nace `renglones_fuera_de_cerca()`, que **no es codigo nuevo**: es el
desbloqueador que `cifras_sin_pareja()` ya tenia dentro, **separado a una sede**.
Ahora lo llaman `cifras_sin_pareja()` y la pieza (2), y **no se escribio un
tercero**.

**Y SE DECLARA LO QUE NO SE TOCO:** `parrafos_fuera_de_cerca()` conserva su propio
recorrido de cercas porque hace **otro trabajo** (agrupa renglones en parrafos y
corta el parrafo en la frontera). Fundirla habria cambiado de paso la guarda de
las citas de arnes, que no es lo que esta vuelta viene a hacer.

**LO DEMAS DE LA PIEZA (2) NO SE TOCO**, y el arnes lo exige: el tallador sin
filas sigue siendo rojo con su texto de hoy, y una fila sin pegar sigue siendo
rojo.

Los casos (`docs/loop/SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt`, **2607 bytes en disco y 2607 bytes normalizados a LF**), **9 casos y los 9 caen al mutar su
esperado**:

| caso | resultado |
|---|---|
| A. la marca FUERA de toda cerca | **falta** |
| B. la marca SOLO DENTRO de una cerca | **no falta** |
| C. la marca EN LAS DOS | **falta** |
| D. cero marcas | **no falta** |
| E. una cerca SIN CERRAR y la marca detras | **no falta**, y con su valor exacto afirmado: **0 renglones con la marca fuera de cerca**, no un "lo que salga" |
| F. el texto REAL del reporte de la 184 cerrado en rojo | **ya no falta** |
| G. el tallador sin filas | **sigue siendo rojo**, con su texto de hoy |
| H. una fila sin pegar | **sigue siendo rojo** |

**EL CASO F ES EL QUE TRAJO LA ADJUDICACION**, y esta medido sobre el fichero
real de **122030 bytes en disco y 122030 normalizados a LF**: la marca aparece
**1 vez DENTRO de cerca y 0 veces fuera**, exactamente como la `PD.5` decia.

#### 2.c EL CARRIL DE CIERRE TARDIO, Y EL REPORTE DE LA 184 CIERRA. ES LA `P.2`

Nacen tres funciones: `vuelta_en_curso()`, que lee del asunto del ultimo commit
con `git log` y es la unica que toca git; `es_cierre_tardio()`, que es **PURA**;
y `declaracion_de_cifras_sin_pareja()`, que tambien lo es. **La condicion se
computa y no se pasa por bandera**, y **si la vuelta en curso no se puede leer,
el carril NO se abre**: la falta de evidencia lo cierra, no lo abre.

**EN EL CARRIL NORMAL NO CAMBIA NADA**, y eso se comprobo con el arnes y no con
la vista: la comprobacion de las cifras sin pareja lleva una columna `bloquea`
que solo ella pone a `not tardio`, y el arnes **cuenta las apariciones de esa
expresion en el instrumento y exige 1**.

Los casos (`docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt`, **5040 bytes en disco y 5040 bytes normalizados a LF**), **18 casos y los 18 caen al mutar su
esperado**: la condicion del carril en cinco escenarios; las cifras sin pareja
bloqueando en normal y no bloqueando en tardio; **la declaracion cotejada por
contencion renglon a renglon, 3 de 3**; su cuenta total; la prueba de que la
declaracion **va dentro de una cerca y por eso no se acusa a si misma**; el cero
declarado y no omitido; y las cuatro piezas rotas una a una para exigir que
**ninguna se afloje**.

**LA PRUEBA MAS FUERTE DE QUE EL CARRIL NO TOCA LAS CUATRO PIEZAS ES DE FORMA:**
`piezas_que_faltan()` **ni siquiera tiene un parametro de carril**, asi que no
puede saber en cual esta. El arnes lo comprueba leyendo su firma.

**EL CIERRE DEL REPORTE DE LA 184, DESPUES Y NO ANTES.**

Las tres piezas se cotejaron **recomputandolas hoy**, y las tres **CALZAN** con
lo que la 184 midio y la 185 confirmo
(`docs/loop/SALIDA_V186_T2C_VEREDICTO_184.txt`, **2322 bytes en disco y 2322 bytes normalizados a LF**):

| pieza | lo medido hoy | lo que midio la 184 |
|---|---|---|
| `docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt` | **2435 bytes en disco y 2415 normalizados a LF** | lo mismo |
| `scripts/loop/_v184_cierre_texto.md` | **13982 bytes en disco y 13982 en LF**, `sha256` de LF `050cdbb4ea99e11c` | lo mismo |
| `docs/loop/SALIDA_V183_BATERIA.txt` | **71753 bytes en disco y 71753 en LF**, `sha256` de LF `422a909ad6ffb167` | lo mismo |

El veredicto de una linea fue **TALLADO y no tecleado**, con sus dos numerales en
palabra computados del cuerpo, y la guarda `B.1` dio **`CIFRA numerales que NO
calzan: 0`**. El tallador corre ademas su propia mutacion: al cambiar un numeral
por otro, la guarda **CAE**.

`scripts/loop/cerrar_reporte.py --vuelta 184` salio con **`EXITCODE 0`** y
**VERDE con sus cuatro piezas**
(`docs/loop/SALIDA_V186_T2C_CERRAR_REPORTE_184.txt`, **6128 bytes en disco y 6128 bytes normalizados a LF**). El carril salio **CIERRE TARDIO**, con la vuelta en curso
leida de git en **186** y la del reporte en **184**. Las **10** cifras sin pareja
quedaron **declaradas una a una con su linea y su cuenta total** en una seccion
10 nueva.

**EL ARCHIVADO SE CORRIO DOS VECES Y LAS DOS SALIDAS SE PUBLICAN**, porque
esconder la decision seria peor que tomarla:

| corrida | exitcode | que dijo |
|---|---:|---|
| sin `--forzar` (`docs/loop/SALIDA_V186_T2C_ARCHIVAR_184_SIN_FORZAR.txt`, **790 bytes en disco y 790 en LF**) | **1** | el destino ya existia con contenido DISTINTO, el reporte de la 184 **sin cerrar** |
| con `--forzar` (`docs/loop/SALIDA_V186_T2C_ARCHIVAR_184.txt`, **965 bytes en disco y 965 en LF**) | **0** | VERDE |

**NADA SE PIERDE AL PISARLO, Y SE COMPROBO ANTES DE PISARLO:** el texto viejo de
**33608 bytes en disco y 33608 normalizados a LF** sigue entero en
`docs/loop/SALIDA_V185_T2A_REPORTE_184_ANTES.md`, **byte a byte identico** al que
se piso, con los dos `sha256`, el de disco y el de LF, en `6bbeb09c5822c192`.

**Y SI, EL ARCHIVADO ES EL CERRADO.** `docs/loop/reportes/REPORTE_V184.md` mide
ahora **124249 bytes en disco y 124249 normalizados a LF**, en **1902 lineas**,
con `sha256` de disco y de LF iguales en `6e1a55a3d33be771`. Lleva la seccion 10
del carril tardio y **ya no lleva** el veredicto `SIN ESCRIBIR TODAVIA`. La marca
del hueco de cabecera sigue apareciendo **una vez, en la linea 353, DENTRO de una
cerca**: es la cita de la salida roja de la 185, o sea el falso positivo que la
`2.b` acaba de cerrar, y por eso este cierre pudo hacerse.

#### 2.d LA ESCALADA: LA SECCION 4 CONTRA LA APERTURA SELLADA. `AUDITOR.md` 1.2

**ESTO ES LA OPERACION DE CODIGO DE UNA ESCALADA CON LA RACHA EN DOS, NO UNA
MEJORA.** Nacen cuatro funciones **PURAS** (`cifras_de_la_apertura()`,
`primer_numero()`, `cifras_que_afirma_la_seccion4()` y
`seccion4_que_no_calza()`) y un lector que es la unica pieza que toca disco. La
que lee la seccion 4 **REUSA `renglones_fuera_de_cerca()`**, la sede que nacio en
la `2.b`: **una cita pegada no es una afirmacion del reporte**.

**LAS TRES FORMAS DE CAER, Y LA TERCERA ES LA QUE MAS IMPORTA:** la apertura no
publica la cifra; las cifras **discrepan**, y el motivo **nombra las dos cifras y
sus dos sedes**; o **la seccion 4 no la afirma**, que **NO es verde: es su propio
rojo**. Una cifra ausente y una cifra que calza no son lo mismo.

La guarda lee **digitos y numerales en palabra**, y **cruza el salto de renglon**
que el markdown mete, porque la `R.1` esta escrita con el marcador al final de una
linea y el `cero` al principio de la siguiente. **Una guarda que no cruzara ese
salto se comeria la mitad del caso que la trajo.**

Los casos (`docs/loop/SALIDA_V186_T2D_MUTACION_SECCION4.txt`, **5007 bytes en disco y 5007 bytes normalizados a LF**), **11 casos y los 11 caen al mutar su
esperado**: las dos calzando; la de status mutada; la de numstat mutada; la
seccion 4 muda; la apertura incompleta; la frase partida en dos renglones; la
cifra citada dentro de una cerca, que **no cuenta**; y las dos sedes nombradas.

**Y EL CASO QUE PRUEBA LA ESCALADA, SOBRE LOS FICHEROS REALES DE LA 185:**

- la apertura sellada de la 185 publica **`CIFRA lineas de status: 2`** y
  **`CIFRA filas de numstat AL ENTRAR: 0`**
- la seccion 4 de `docs/loop/reportes/REPORTE_V185.md` afirma **15** en su linea
  **574** y **cero** en su linea **581**, y **0** para el numstat en la **575**
- la guarda saca **2 motivos en rojo**, los dos nombrando las dos sedes

**LA GUARDA HUBIERA CAZADO LA `R.1`: SI.** Y **la de numstat de ese mismo reporte
SI calza**, con **0 motivos**, que es lo que hace que no sea un rojo
indiscriminado.

**ESTA GUARDA NO SE AFLOJA EN NINGUN CARRIL, NI SIQUIERA EN EL TARDIO**, y por eso
va cableada fuera de la columna que el carril tardio toca.

#### EL ARNES VIEJO, CORRIDO SIN TOCARLO AL TERMINAR LAS TRES REPARACIONES

`scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py`, **sin tocarlo**, sale
**VERDE con sus 9 casos** y **`CIFRA fallos: 0`**
(`docs/loop/SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt`, **5802 bytes en disco y 5802 bytes normalizados a LF**). **No cambio de color.** Y los dos arneses sellados de
la 185 tambien siguen verdes despues de las tres reparaciones, con su `sha256`
intacto.

#### LAS RUTAS DE PRUEBA DE ESTA TAREA, TODAS COMPROBADAS Y NINGUNA DE CERO BYTES

| ruta | bytes en disco, iguales normalizados a LF |
|---|---:|
| `docs/loop/SALIDA_V186_T2A_MUTACION_PIEZA4.txt` | **3601** |
| `docs/loop/SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt` | **2607** |
| `docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt` | **5040** |
| `docs/loop/SALIDA_V186_T2C_VEREDICTO_184.txt` | **2322** |
| `docs/loop/SALIDA_V186_T2C_VEREDICTO_184_FRASE.txt` | **356** |
| `docs/loop/SALIDA_V186_T2C_CERRAR_REPORTE_184.txt` | **6128** |
| `docs/loop/SALIDA_V186_T2C_ARCHIVAR_184_SIN_FORZAR.txt` | **790** |
| `docs/loop/SALIDA_V186_T2C_ARCHIVAR_184.txt` | **965** |
| `docs/loop/SALIDA_V186_T2D_MUTACION_SECCION4.txt` | **5007** |
| `docs/loop/SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt` | **5802** |
| `docs/loop/reportes/REPORTE_V184.md` | **124249** |
