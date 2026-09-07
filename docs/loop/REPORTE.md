# REPORTE DE LA VUELTA 200 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta200_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA ES LA VUELTA DE BATERIA, Y NO LLEVA NADA MAS.** `AUDITOR.md` 6.1 lo dice
> con estas palabras: la bateria corre **cada cinco vueltas**, en una **vuelta
> propia** con **su doble corrida, su reloj y su salida sellada**, y **nada de
> trabajo de plan al lado**. Por eso este encargo trae **DOS** tareas y la segunda
> es la bateria; y por eso **la correccion declarada de `OP-I-01` y la medicion de
> `OP-L-02`, que el acta 199 ya adjudico en su `4.1` y su `4.2`, VAN A LA 201** y
> no se pierden.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026): **no se fabrican arneses, guardas ni lectores nuevos**, y **esta
> vuelta NO TIENE NINGUNA EXCEPCION**, porque las dos de la 199 se consumieron.
> **La nomina queda CONGELADA EN 135**, y el bloque `F` del sello de apertura la
> midio contra ese congelado.
>
> **EL TOPE SIGUE SIENDO DE DOS SUB-TAREAS, Y LA CIFRA QUE LO MANDA NO SE
> TECLEA.** El bloque `E` del sello de apertura de esta vuelta corrio el
> instrumento de la racha sobre el inventario ENTERO y **la racha de cierres vale
> 1**, con las vueltas **199**. `AUDITOR.md` 6.2 apaga el regimen
> temporal de dos sub-tareas cuando **DOS vueltas seguidas** cierran su propio
> reporte con `cerrar_reporte.py`, y con **1** no se apaga. **Este encargo
> trae DOS, y cabe.**
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y su bloque `F`
> **es la medicion de la caida `C.1` del acta 199, tomada antes de mirar nada**: la
> cifra de arneses del censo fuera de la nomina **viaja con su vara y se miden las
> dos**, con vara **148** salen **2** y sin vara salen **62**.
> **Esas son las cifras de HOY, y la TAREA 1.a las publica con sus nombres.**
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina** (la poda se
> decide en la auditoria integral, no aqui), ni **el trabajo de plan**, que la
> cadencia de 6.1 manda dejar fuera de una vuelta de bateria. **Y siguen fuera,
> nombradas para que la 201 no las redescubra:** la guarda de codigo del hallazgo
> `5.3` del acta 194; `acumulan()` que lea la tabla; el cotejo de clon declarado;
> las actas sin entrada propia en la serie; **QUE HACER CON LAS FILAS `B` DEL
> ARCHIVO**, que el hallazgo `5.1` del acta 199 vuelve a poner encima de la mesa; y
> **los puestos que dos o tres lectores independientes fallaron**, nombrados y
> medidos y **no resueltos, porque mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**. **La bateria lo mide ella sola once veces mas**,
> al entrar y al salir de cada tramo, con `guarda_y_restauracion()`.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta200_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 199: `69a16e29`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 199, SIN PARADA: LA VUELTA REPRODUCE ENTERA SALVO UN NUMERO QUE SU PROPIA VUELTA VOLVIO FALSO, Y MIS ONCE DISCREPANCIAS SALEN DE UNA DEFINICION QUE HEREDE SIN COMPROBAR.'
```
- **EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y SE MIDE EN VEZ DE
  SUPONERSE.** `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la **199**,
  y **el acta que ORDENA esta vuelta ES la 199**: el bloque `H` del sello de
  apertura conto **1 acierto para la cabecera de la 199 y 0 para la 200**. El
  `D.2` del reporte de la 184 sigue vivo como especie, y aqui **no muerde**. Lo
  que si se sigue contando, porque es cifra de inventario y envejece sola: **10 reportes archivados traen el literal
  `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`, `REPORTE_V194.md`, `REPORTE_V195.md`, `REPORTE_V196.md`, `REPORTE_V197.md`, `REPORTE_V199.md`), contados por `reportes_con_el_literal()`
  de este mismo fichero, **con FECHA DE CORTE 2026-09-07** (banco `9.21`, TODA
  CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Un inventario que crece cada vuelta
  sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V200_HEAD_APERTURA.txt`: `69a16e29`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `5b9604ac`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **199**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 200`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 19 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **0 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 199 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, y su cuerpo se acota con `grep -n` EN ESTA VUELTA. Y con la entrada van LAS TRES CORRECCIONES DE CIFRA que la seccion 3 del acta 199 levanta, cada una EN SU SEDE, por el carril del banco `9.10` mas `EJECUTOR.md` 8, CON EL TEXTO VIEJO ENTERO Y SIN TACHAR: (1.a) la `C.1`, LA QUE ACUMULA, el reporte de la 199 dice UN arnes del censo fuera de la nomina con la vara 148 y al commit de cierre son DOS, y NO SE CORRIGE TECLEANDO EL DOS sino volviendo a correr `V.arneses_que_faltan(vara=148)` y pegando su salida con su corte, mas la cifra SIN VARA que el reporte dio en 61; (1.b) la `C.2`, el literal `HUECO` en `docs/plan/10_INVENTARIO.md` sale 3 y no 4, y hay que decir si se corrige la cifra o la etiqueta; (1.c) la `C.3`, ese fichero tiene 413 lineas y no 414 | **CERRADA** | `SALIDA_V200_T1A_REGISTRO_R60.txt` (serie de 51 a 52, 0 colisiones, 0 huecos), `SALIDA_V200_T1A_REGISTRO_IDEM.txt` (7/7 en la mutacion, sede identica al re correr), `SALIDA_V200_T1B_CORRECCIONES_EN_SU_SEDE.txt` (104 lineas anadidas y 0 borradas en la sede) |
| **TAREA 2** | LA BATERIA ENTERA, POR TRAMOS, Y CON LA TRAMPA MEDIDA DELANTE. Es la TAREA de la cadencia de `AUDITOR.md` 6.1 y la vuelta NO LLEVA NADA MAS. El lanzador es `scripts/loop/vuelta183_bateria_por_tramos.py` y NO SE CLONA. Sus dos mitades, las dos medidas por el auditor corriendolas: `--siguiente` dice que faltan el 10 y el 11 sobre NUEVE SALIDAS AJENAS de la corrida de la 183, y correr el tramo 1 PISA la sellada del 183. Por eso: LAS NUEVE SE PRESERVAN POR COPIA con sus bytes y su `sha256` medidos antes y despues; SE CORREN LOS ONCE TRAMOS, no los dos que `--siguiente` dice, porque `--plan` da ONCE hoy y el NUEVE de 6.1 se escribio con una nomina menor; CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR; una salida sellada de CERO BYTES no cuenta como hecha; y la bateria se declara corrida cuando los once tienen salida sellada del mismo calibre, y el calibre lo coteja `--componer` y no el criterio del ejecutor | **CERRADA** | `SALIDA_V183_BATERIA.txt` (92570 bytes, 1424 lineas, sha256 LF aac5f56abac9e758, 135 de 135 entradas y 0 sin correr), las ONCE `SALIDA_V183_BATERIA_TRAMO_1..11.txt` (ninguna de cero bytes), `SALIDA_V200_T2_PRESERVAR_LAS_NUEVE.txt` (9 copias identicas, 9 originales intactas), `SALIDA_V200_T2_PLAN_APERTURA.txt` y `SALIDA_V200_T2_SIGUIENTE_APERTURA.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

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

### TAREA 2, LA BATERIA ENTERA. CERRADA. LOS ONCE TRAMOS CORRIDOS, SELLADOS Y COMMITEADOS, Y DOS ROJOS QUE NO SON LO MISMO

**Instrumento:** `scripts/loop/vuelta183_bateria_por_tramos.py`, **NO CLONADO**,
que es lo que el encargo manda por defecto. **Salida unica:**
`docs/loop/SALIDA_V183_BATERIA.txt`, **disco 92570 bytes y LF 92570 bytes**,
`sha256` LF `aac5f56abac9e758`, **1424 lineas**. Preservacion previa en
`docs/loop/SALIDA_V200_T2_PRESERVAR_LAS_NUEVE.txt`.

**LAS DOS MITADES DE LA TRAMPA, MEDIDAS ANTES DE TOCAR NADA Y NO CREIDAS.** El
bloque `H.1` del sello de apertura corrio `--plan` y `--siguiente`: **`--plan` da
ONCE tramos sobre 135 entradas**, y **`--siguiente` dijo que habia NUEVE hechos y
que el siguiente era el TRAMO 10**, sobre **nueve salidas selladas de la corrida
de la vuelta 183**. **No se le hizo caso**: se corrieron **los once**.

**LAS NUEVE SE PRESERVARON POR COPIA ANTES DE QUE EL TRAMO 1 LAS PISARA**, en
`docs/loop/preservadas/v183/` y **con el nombre exacto del original**, que es lo
que las hace citables como la misma prueba. **9 copias identicas, 0 distintas, 0
ausentes**, y **las 9 originales INTACTAS tras copiar**, remedidas una a una:
copiar no es borrar y se comprueba en vez de prometerse.

#### LOS ONCE TRAMOS, CONTADOS DE `--componer` Y NO TECLEADOS

| tramo | bytes disco | bytes LF | lineas | `sha256` LF | entradas | exitcode | minutos |
|---:|---:|---:|---:|---|---:|---:|---:|
| 1 | 9558 | 9558 | 129 | `413cf381cac3` | 13 | 1 | 2.5 |
| 2 | 7804 | 7804 | 123 | `553e56b775af` | 13 | 1 | 6.4 |
| 3 | 7857 | 7857 | 123 | `5156e936d005` | 13 | 1 | 12.9 |
| 4 | 7867 | 7867 | 123 | `75acd39e3b70` | 13 | 1 | 3.0 |
| 5 | 7827 | 7827 | 123 | `2f4ba7df5015` | 13 | 1 | 0.7 |
| 6 | 7887 | 7887 | 123 | `98498ba8f979` | 13 | 1 | 2.2 |
| 7 | 7893 | 7893 | 123 | `c09960750d7c` | 13 | 1 | 0.6 |
| 8 | 7848 | 7848 | 123 | `b07f055c9e20` | 13 | 1 | 0.8 |
| 9 | 8523 | 8523 | 125 | `c323573fb6b3` | 13 | 1 | 2.3 |
| 10 | 8475 | 8475 | 123 | `a91d4a64007f` | 13 | 1 | 2.5 |
| 11 | 6273 | 6273 | 94 | `f50d0fbbd554` | 5 | 1 | 0.3 |

**Las once primeras columnas salen de la salida de `--componer`; el `exitcode` y
los minutos, de la linea `EXITCODE DEL TRAMO` y `DURACION DEL TRAMO (monotona,
minutos)` de cada sellada.** **NINGUNA MIDE CERO BYTES.** **El reloj de la
corrida entera, sumado de las once celdas: 34.2 minutos**, contra la estimacion
que `--plan` publico con su corte, **entre 44.6 y 58.0**.

**EL CALIBRE LO COTEJA `--componer` Y NO MI CRITERIO, Y SALE VERDE:** **135**
entradas de la nomina, **135** que los tramos dicen haber corrido, **0** sin
correr, **0** ajenas, **0** repetidas, y **la cobertura se leyo de las salidas,
no se recalculo del reparto**. **Cada entrada se corre DOS VECES**, que es la
integridad que la letra del fundador del 5 sep 2026 fija y que el propio
encabezado de cada tramo escribe.

**CADA TRAMO SE COMMITEO CON SU SALIDA SELLADA AL TERMINAR, ANTES DE SEGUIR**, en
once commits distintos, mas el de la preservacion y el de la composicion.

#### EL PRIMER ROJO: LOS DOS ARNESES DEL CENSO, Y ES EL CONGELADO

**LOS ONCE TRAMOS SALEN CON EXITCODE 1, Y LOS ONCE POR EL MISMO MOTIVO, QUE NO ES
NINGUNA MUTACION:**

```
ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta
148 o despues, se quedan FUERA. La lista entera:
vuelta197_tarea2_mutacion_orden_del_turno.py,
vuelta199_tarea1_mutacion_guardas_revividas.py
```

**ES EXACTAMENTE LA CONSECUENCIA DEL CONGELADO EN 135 DE `AUDITOR.md` 6.3**, y el
encargo manda nombrarla en la seccion 9 en vez de callarla. **No se arregla, y se
dice por que:** meter esos dos en la nomina seria saltarse una decision escrita
del fundador, y la moratoria lo prohibe.

**EL PRECEDENTE ESTA MEDIDO Y NO RECORDADO:** la bateria de la vuelta 194 corrio
sus **DIEZ** tramos con **exitcode 1 en los diez**, por **6** arneses fuera de la
nomina **mas 3** entradas sin sujeto congelado. **La de hoy tiene 2 fuera, 0
invisibles al censo y 0 sin sujeto congelado**, o sea que es **estrictamente
mejor** en las tres varas. Y las nueve selladas de la 183, contadas de las copias
preservadas, **traen exitcode 0 en ocho y 1 en la novena**.

#### EL SEGUNDO ROJO, QUE NO ES EL MISMO Y VA MARCADO COMO PARADA

**UNA SOLA ENTRADA DE LAS 135 SALE `NO MORDIO`, Y ES DEL TRAMO 9:**
`vuelta185_tarea1c_mutacion_bateria_continuada.py`, **exit 1, 13.0 segundos**.
Las otras **134** corren limpias: **0 ancla perdida, 0 sin reproducir, 0
invisibles al censo, 0 sin sujeto congelado, 0 ruido de concurrencia en los once
tramos**, y **2 casos declarados con su marca obligatoria**, los dos del tramo 1
(`vuelta135_2e_mutacion_3.py` y `vuelta140_2a_mutaciones.py`).

**Y NO ES UNA GUARDA MUERTA. Lo mido en su propia salida sellada,**
`docs/loop/SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt`: sus bloques `A` a
`E` y `G` **calzan enteros**. Los **6** casos de `rama_de_la_seccion9()` calzan y
**los 6 CAEN al mutar su esperado**; los cuatro del cuarto parametro por defecto
calzan y caen; `vuelta_que_sello()` calza en sus tres casos y cae en los tres.
**`CIFRA fallos: 1`, y el fallo es SOLO su bloque `F`.**

**LO QUE FALLA ES UN BLOQUE CUYO SUJETO ESTA VIVO.** El bloque `F` afirma que
`tramos_por_vuelta(183)` reparte **4 y 5**: *"los tramos 1 a 4 los sello la vuelta
183 y los tramos 5 a 9 la vuelta 184"*, leyendo **el asunto del ultimo commit de
cada una de las nueve selladas**. **Esta vuelta 200 RE SELLA esas nueve con sus
propios commits**, asi que el mismo lector, corrido hoy, dice:

```
   CIFRA sellados por la vuelta 183: 0 []
   CIFRA sellados por la vuelta 184: 1 [9]
   CIFRA sellados por otra vuelta o sin asunto: 8 [1, 2, 3, 4, 5, 6, 7, 8]
   EL REPARTO ES 4 Y 5 SOBRE NUEVE: NO
```

**ES CONSECUENCIA MEDIDA DE NO CLONAR EL LANZADOR**, que es lo que el encargo
manda por defecto y lo que se hizo. **No lo arreglo**: la moratoria `6.3` lo
prohibe, el sujeto no es mio, y **su esperado no ha dejado de ser correcto: lo
que ha dejado de ser cierto es su premisa**, que es la misma especie que el acta
199 nombro en la TAREA 1 de esa vuelta. **VA COMO PARADA AL REPORTE.**

#### LO QUE LA CORRIDA DEJO EN EL ARBOL, DICHO Y NO ESCONDIDO

**LOS FICHEROS QUE LA BATERIA RE ESCRIBE SON SUYOS Y ESTABAN YA RASTREADOS.** Al
correr, cada arnes vuelve a sellar su propia salida (`SALIDA_V182_T2_*`,
`SALIDA_V184_T1C_*`, `SALIDA_V185_*`, `SALIDA_V186_*`, `SALIDA_V187_*`,
`SALIDA_V188_*`, `SALIDA_V190_*`, `SALIDA_V191_*`, `SALIDA_V192_*`,
`SALIDA_V193_*`, `SALIDA_V194_*`, `SALIDA_V195_*`) y algunos regeneran su
fixture (`docs/loop/_v167_t3_mut_componentes_*.jsonl` y
`scripts/loop/_v167_recomputo_ultimo_gana_copia.py`, **los tres ya rastreados
desde `12053ade`, medido con `git log --diff-filter=A`**). **Van dentro de los
commits de su tramo**, y **`RUIDO DE CONCURRENCIA` sale 0 en los once**, porque
no son ficheros ajenos apareciendo: son las selladas de los propios arneses que
la bateria acaba de correr.

**UNA NOTA DE METODO QUE VA CON SU NOMBRE:** el tramo 3 tardo **12.9 minutos** y
su primer lanzamiento **se corto a los 10 por el tope de la sesion**, dejando
`dataset/metadata/master_graph.json` tocado y **sin escribir su sellada**. Se
restauro con `git checkout --`, el `numstat` volvio a **cero filas**, y **el
tramo se re corrio ENTERO desde el principio**, no desde donde se corto. **Esa
corrida cortada no dejo ninguna sellada, asi que no hay ninguna prueba a medias
publicada.** Los tramos siguientes se lanzaron en segundo plano por eso.

**Y LO QUE EL ENCARGO PIDE MEDIR AL ABRIR Y AL CERRAR, CON LAS DOS MEDIDAS:**

| que | al abrir | al cerrar |
|---|---:|---:|
| entradas de la nomina | **135** | **135** |
| casos declarados | **2** | **2** |
| arneses que el censo reconoce | **197** | **197** |
| fuera de la nomina CON la vara 148 | **2** | **2** |
| fuera de la nomina SIN vara | **62** | **62** |
| entradas invisibles al censo | **0** | **0** |
| entradas sin sujeto congelado | **0** | **0** |
| `sha256` LF de `INTRA_DOMINIO_VEREDICTOS.jsonl` | `0a77b5a35a962621` | `0a77b5a35a962621` |

<!-- FIN ANEXO DE TAREAS -->
