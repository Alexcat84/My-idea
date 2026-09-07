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

**EL VEREDICTO DE UNA LINEA: LA VUELTA 200 CIERRA CON SUS DOS TAREAS Y CON DOS PARADAS QUE NO SE ARREGLAN AQUI: la bateria corrio ENTERA en sus ONCE tramos y no en los dos que --siguiente decia, con las nueve selladas de la 183 preservadas identicas antes de que el tramo 1 las pisara, 135 de 135 entradas corridas exactamente una vez y 34.2 minutos de reloj; el acta 199 entro en la serie como R.60 sin escribir un solo lector nuevo y sus tres correcciones de cifra estan en su sede con 104 lineas anadidas y CERO borradas; y los dos rojos que quedan no son lo mismo, uno es el congelado de la nomina convertido en exitcode y el otro es un bloque de arnes cuyo sujeto esta vivo porque esta misma vuelta lo re sella.**
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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 200`, y su salida
cruda vive en `docs/loop/SALIDA_V200_TALLADOR_CABECERA.txt` (2449 bytes en disco y 2429 normalizado a LF, 11 filas de
tabla,
contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN
INSTRUMENTO NO SE ESCRIBE.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 82 passed (82) / 1.040 passed (1.040) | **82 passed (82) / 1.040 passed (1.040)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `69a16e29` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 199, SIN PARADA: LA VUELTA REPRODUCE ENTERA SALVO UN NUMERO QUE SU PROPIA VUELTA VOLVIO FALSO, Y MIS ONCE DISCREPANCIAS SALEN DE UNA DEFINICION QUE HEREDE SIN COMPROBAR.'), HEAD real de apertura `69a16e29` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `118bf6e3` (leido de `SALIDA_V200_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 199 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, y su cuerpo se acota con `grep -n` EN ESTA VUELTA. Y con la entrada van LAS TRES CORRECCIONES DE CIFRA que la seccion 3 del acta 199 levanta, cada una EN SU SEDE, por el carril del banco `9.10` mas `EJECUTOR.md` 8, CON EL TEXTO VIEJO ENTERO Y SIN TACHAR: (1.a) la `C.1`, LA QUE ACUMULA, el reporte de la 199 dice UN arnes del censo fuera de la nomina con la vara 148 y al commit de cierre son DOS, y NO SE CORRIGE TECLEANDO EL DOS sino volviendo a correr `V.arneses_que_faltan(vara=148)` y pegando su salida con su corte, mas la cifra SIN VARA que el reporte dio en 61; (1.b) la `C.2`, el literal `HUECO` en `docs/plan/10_INVENTARIO.md` sale 3 y no 4, y hay que decir si se corrige la cifra o la etiqueta; (1.c) la `C.3`, ese fichero tiene 413 lineas y no 414 | **CERRADA** | `SALIDA_V200_T1A_REGISTRO_R60.txt` (serie de 51 a 52, 0 colisiones, 0 huecos), `SALIDA_V200_T1A_REGISTRO_IDEM.txt` (7/7 en la mutacion, sede identica al re correr), `SALIDA_V200_T1B_CORRECCIONES_EN_SU_SEDE.txt` (104 lineas anadidas y 0 borradas en la sede) |
| **TAREA 2** | LA BATERIA ENTERA, POR TRAMOS, Y CON LA TRAMPA MEDIDA DELANTE. Es la TAREA de la cadencia de `AUDITOR.md` 6.1 y la vuelta NO LLEVA NADA MAS. El lanzador es `scripts/loop/vuelta183_bateria_por_tramos.py` y NO SE CLONA. Sus dos mitades, las dos medidas por el auditor corriendolas: `--siguiente` dice que faltan el 10 y el 11 sobre NUEVE SALIDAS AJENAS de la corrida de la 183, y correr el tramo 1 PISA la sellada del 183. Por eso: LAS NUEVE SE PRESERVAN POR COPIA con sus bytes y su `sha256` medidos antes y despues; SE CORREN LOS ONCE TRAMOS, no los dos que `--siguiente` dice, porque `--plan` da ONCE hoy y el NUEVE de 6.1 se escribio con una nomina menor; CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR; una salida sellada de CERO BYTES no cuenta como hecha; y la bateria se declara corrida cuando los once tienen salida sellada del mismo calibre, y el calibre lo coteja `--componer` y no el criterio del ejecutor | **CERRADA** | `SALIDA_V183_BATERIA.txt` (disco 92570 bytes y LF 92570 bytes, 1424 lineas, sha256 aac5f56abac9e758 por disco y aac5f56abac9e758 por LF, 135 de 135 entradas y 0 sin correr), las ONCE `SALIDA_V183_BATERIA_TRAMO_1..11.txt` (ninguna de cero bytes), `SALIDA_V200_T2_PRESERVAR_LAS_NUEVE.txt` (9 copias identicas, 9 originales intactas), `SALIDA_V200_T2_PLAN_APERTURA.txt` y `SALIDA_V200_T2_SIGUIENTE_APERTURA.txt` |
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
`sha256` `24d55cd02d626c4f` por disco y `24d55cd02d626c4f` por LF),
`docs/loop/SALIDA_V200_T1A_REGISTRO_IDEM.txt` (disco 9100 bytes y LF 8962 bytes,
`sha256` `90d22b9de53d33cd` por disco y `81fa613af871114b` por LF, y **las cuatro
cifras difieren entre convenciones porque este se sello por redireccion de
consola y llego con CRLF**),
`docs/loop/SALIDA_V200_T1B_CORRECCIONES_EN_SU_SEDE.txt` (disco 3292 bytes y LF
3292 bytes, `sha256` `a805477c03bd134f` por disco y `a805477c03bd134f` por LF).

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

**MEDIDO Y NO NARRADO:** `docs/PENDIENTES.md` paso de **1079444** a **1086030**
bytes en disco y la serie de **52** a **53** entradas; su `sha256` **por LF** paso
de `1c56ba86ffe292f9` a `24c0ecd7425c2418`, y **el `sha256` de disco de esos dos
estados NO SE MIDIO en su momento, asi que no se publica ninguno**: un sha que no
se midio no se deduce. **La duplicada se retiro con `git checkout --`** y la sede
volvio a su estado del commit, **1088345 bytes en disco y 1072852 normalizados a
LF**, con `sha256` **por LF** `6d4ff7222b4e77b7` y **sin cifra de disco por el
mismo motivo**. **Nunca se commiteo.**

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
`docs/PENDIENTES.md` mide **1079444 bytes en disco y 1079444 normalizados a LF**
con `sha256` `1c56ba86ffe292f9` por disco y `1c56ba86ffe292f9` por LF, **antes y
despues**; la serie sigue en **52** entradas y el
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
`sha256` `aac5f56abac9e758` por disco y `aac5f56abac9e758` por LF, **1424 lineas**. Preservacion previa en
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

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA FILA DE ESTA TABLA CITA EL FICHERO DEL QUE SE CUENTA** (`EJECUTOR.md` 1,
LA TABLA SE CUENTA DE SU FICHERO). Ninguna celda esta tecleada de memoria.

| que | cifra | de que fichero se cuenta |
|---|---|---|
| entradas de la serie `R.N`, antes y despues | **51** y **52**, 0 colisiones y 0 huecos en las dos | `SALIDA_V200_T1A_REGISTRO_R60.txt` |
| numerales del acta 199 | **5** adjudicaciones, **4** hallazgos, **4** preguntas, **2** caidas del auditor, **3** del ejecutor | `SALIDA_V200_T1A_REGISTRO_R60.txt` |
| cuerpo del acta 199, acotado hoy | lineas **69878** a **70229**, **352** lineas | `SALIDA_V200_APERTURA.txt`, bloque `H` |
| prueba de la guarda de idempotencia | **7** casos, **7** verdes, **0** rojos, **7 de 7 CAEN** al mutar el esperado, **1** discrepa contra la guarda vieja | `SALIDA_V200_T1A_REGISTRO_IDEM.txt` |
| sede de las tres correcciones, antes y despues | disco **48688** y LF **48688** con `sha256` `e88a05f2d64c791f`; disco **54251** y LF **54251** con `sha256` `a32272ff36524041` | `SALIDA_V200_T1B_CORRECCIONES_EN_SU_SEDE.txt` |
| lineas anadidas y borradas en esa sede | **104** anadidas, **0** borradas | `git diff --numstat` corrido en esta vuelta |
| las nueve selladas del 183, preservadas | **9** copias identicas, **0** distintas, **0** ausentes, **9** originales intactas | `SALIDA_V200_T2_PRESERVAR_LAS_NUEVE.txt` |
| reparto de la bateria | **11** tramos sobre **135** entradas, tamano **13** | `SALIDA_V200_T2_PLAN_APERTURA.txt` |
| lo que `--siguiente` decia antes de correr | **9** por hechos, **2** que faltan, siguiente el **10** | `SALIDA_V200_T2_SIGUIENTE_APERTURA.txt` |
| cobertura de la bateria | **135** de **135**, **0** sin correr, **0** ajenas, **0** repetidas | `SALIDA_V183_BATERIA.txt` |
| salida unica de la bateria | disco **92570** y LF **92570**, **1424** lineas, `sha256` LF `aac5f56abac9e758` | `SALIDA_V183_BATERIA.txt` |
| reloj de la bateria | **34.2** minutos sumados de las once celdas, contra una estimacion de **44.6** a **58.0** | las once `SALIDA_V183_BATERIA_TRAMO_N.txt` y `SALIDA_V200_T2_PLAN_APERTURA.txt` |
| entradas que no mordieron | **1** de **135**, `vuelta185_tarea1c_mutacion_bateria_continuada.py` | `SALIDA_V183_BATERIA_TRAMO_9.txt` |
| casos declarados en la corrida | **2**, los dos del tramo 1 | `SALIDA_V183_BATERIA_TRAMO_1.txt` |
| ancla perdida, sin reproducir, ruido de concurrencia | **0**, **0** y **0** en los once tramos | las once `SALIDA_V183_BATERIA_TRAMO_N.txt` |
| racha de cierres | **1**, con la vuelta **199** | `SALIDA_V200_APERTURA.txt`, bloque `E` |
| deuda de la serie al cerrar | **9** actas de la 173 a la 199 sin entrada propia | `serie_de_registros.py` recorrido al cerrar la TAREA 1 |

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO EN ESTA PROSA.**
`docs/loop/SALIDA_V200_APERTURA.txt`, bloque `C`, publica las dos cifras del
estado del arbol con la redaccion exacta que la guarda coteja, y aqui se repiten
LEIDAS de ella:

`git status --porcelain` 1 linea al entrar, que era el propio bloque de apertura
todavia sin commitear.

`git diff --numstat -- dataset/` 0 filas al entrar.

**La apertura sellada no se toco al cierre ni una vez.**

**LO QUE SE TOCO:**

- `docs/PENDIENTES.md`: la entrada `R.60` del acta 199, anadida al final.
- `docs/loop/reportes/REPORTE_V199.md`: **tres avisos de una linea** y **un bloque
  de correcciones declaradas** al final. **104 lineas anadidas y 0 borradas.**
- `scripts/loop/`: el bloque de apertura, el esqueleto, el bloque de cierre (los
  tres **clones declarados**), los tres computos de un solo uso con prefijo de
  guion bajo y los dos cuerpos de tarea.
- `docs/loop/`: las salidas selladas de esta vuelta, las **once** de la bateria
  con su transcripcion de lanzador, la salida unica, las **nueve copias
  preservadas** en `preservadas/v183/`, y el reporte.
- **Las salidas selladas que los propios arneses de la nomina re escriben al
  correr**, que son suyas y estaban ya rastreadas.

**LO QUE NO SE TOCO, Y SE MIDE EN VEZ DE PROMETERSE:**

- **`dataset/` no se toco a mano.** El `numstat` contra `HEAD` sale con **0
  filas** al entrar y **0 al salir**, medido en `SALIDA_V200_CICLO_NUMSTAT_APERTURA.txt`
  y en `SALIDA_V200_CICLO_NUMSTAT_CIERRE.txt`. **Y la bateria lo remidio ella sola
  veintidos veces mas**, al entrar y al salir de cada uno de los once tramos, con
  `guarda_y_restauracion()`, y las veintidos dan **cero filas**.
- **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se movio.** Disco **4054129** bytes y
  LF **4054129** bytes, `sha256` `0a77b5a35a962621` por disco y por LF, **al
  entrar y al salir**.
- **`web/` y `engine/` en cero filas de `numstat`**, y **`docs/plan/` tampoco se
  movio**: la correccion de la `C.2` y la `C.3` **mide** `docs/plan/10_INVENTARIO.md`
  y **no lo edita**.
- **La nomina no crecio ni se podo**: **135** al entrar y **135** al salir, con
  `CASOS_DECLARADOS` en **2**. **Los dos arneses que quedan fuera siguen fuera.**
- **`AUDITOR.md` no se toco**, aunque su `6.1` diga NUEVE tramos y hoy sean ONCE:
  es del fundador.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` LA SEDE DE LAS TRES CORRECCIONES.** Elegi
`docs/loop/reportes/REPORTE_V199.md`, o sea **el reporte archivado**, porque es
donde viven las tres cifras. **Se puede leer de otra manera**: que la sede sea la
entrada `R.60`, o el reporte de esta vuelta. **Escribi en la que contiene el
texto falso**, que es lo que "cada una EN SU SEDE" dice mas literalmente, y
**anadi ademas el aviso en el propio parrafo** para que nadie lea la cifra vieja
sin ver que hay correccion. **Va marcado.**

**`D.2` CORREGIR LA CIFRA Y NO LA ETIQUETA EN LA `C.2`.** El encargo pide elegir
y decir cual. **Elegi la cifra**, con el motivo escrito en el bloque: la etiqueta
del parrafo dice *el literal* y esa etiqueta es la correcta para la clausula que
mide. **Se podia haber elegido lo contrario** y llamar a la cifra *"lineas que
nombran un hueco"*. **Publico las dos con sus patrones y sus lineas**, asi que
quien discrepe tiene delante las dos. **Va marcado.**

**`D.3` NO CLONAR EL LANZADOR DE LA BATERIA.** El encargo lo deja abierto
(*"NO SE CLONA salvo que decidas lo contrario con su motivo escrito"*) y **segui
el defecto**. **El coste esta medido y no es cero**: las once salidas selladas de
esta corrida se llaman `SALIDA_V183_...` y dicen **BATERIA DE LA VUELTA 183**
dentro, y **eso tumbo el bloque `F` de `vuelta185_tarea1c_mutacion_bateria_continuada.py`**.
**El propio docstring del lanzador nombra `vuelta200_bateria_por_tramos.py` como
el clon que arreglaria eso sin tocar codigo.** No lo hice porque el defecto del
encargo es no clonar y porque la moratoria pesa del mismo lado. **Va marcado, y
es el discutible mas gordo de esta vuelta.**

**`D.4` CORRER LOS ONCE TRAMOS AUNQUE EL PRIMERO SALIERA EN ROJO.** El lanzador
imprime *"AQUI SE PARA"*. **Lo lei como "no se re-corre ESE tramo", no como "la
bateria se abandona"**, y el precedente lo respalda: **la vuelta 194 corrio sus
diez tramos con exitcode 1 en los diez**. Ademas el encargo dice **CORRE LOS ONCE
TRAMOS** con todas sus letras. **Va marcado.**

**`D.5` LA CAIDA PROPIA `C.P1` LA CUENTO COMO MIA Y NO COMO ANECDOTA.** Mi guarda
de idempotencia escribio una entrada duplicada. **Nunca se commiteo** y esta
revertida y medida, pero **la escribo como caida** en vez de contarla como un
tropiezo del camino. **Puede que el auditor la clasifique de otra especie.**

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` LOS DOS ARNESES FUERA DE LA NOMINA CONVIERTEN LA BATERIA ENTERA EN ROJO,
Y ESO NO ESTABA DICHO.** El congelado de `AUDITOR.md` 6.3 y la regla de entrada
de la nomina, escrita en `verificar_mutaciones_viejas.py` desde la vuelta 148 y
aceptada por el acta 176 punto 7.2, **se contradicen**: mientras el congelado
dure, **ningun tramo puede salir verde**. **Va como PARADA en la seccion 8.** Lo
que no se: si el remedio es podar, ensanchar el congelado, o que la bateria
distinga *rojo de mutacion* de *rojo de censo* en su exitcode. **Ninguna de las
tres la decido yo.**

**`P.2` `vuelta185_tarea1c_mutacion_bateria_continuada.py` TIENE UN BLOQUE CON
SUJETO VIVO.** Su bloque `F` afirma un reparto que lee del `git log` de nueve
ficheros que **cualquier vuelta de bateria que no clone el lanzador vuelve a
sellar**. **Su esperado no ha dejado de ser correcto; su premisa si.** El remedio
puede ser congelar su sujeto o clonar el lanzador, y las dos son decisiones de
codigo que la moratoria me prohibe tomar. **Tambien va como PARADA.**

**`P.3` LA `C.1` NO SE PUEDE CERRAR DEL TODO Y SE DICE.** La correccion queda
escrita y la cifra remedida, pero **el segundo arnes sigue sin correr y seguira
sin correr** mientras el congelado dure. **La correccion arregla el papel, no el
hueco de cobertura.**

**`P.4` LA 198 SIGUE SIN REGISTRO Y SIN REPORTE ARCHIVADO.** Medido hoy:
`docs/loop/reportes/REPORTE_V198.md` **no existe**, y la 198 **no tiene entrada
propia** en la serie. **No lo arreglo por mi cuenta** porque el encargo nombra el
acta 199 y solo esa, y fabricar el archivado de un reporte que nadie guardo seria
inventarme el texto. **Quien la tome, la registra.**

## 7. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Las dos sub-tareas se ejecutaron con reglas escritas y citadas
por numero. Lo que no cabia en una regla vigente salio como **pregunta** en la
seccion 6 o como **PARADA** en la 8, en vez de resolverse por mi cuenta.

## 8. LO QUE LA 201 RECIBE, Y LAS DOS PARADAS

**PARADA `1`: LA BATERIA NO PUEDE SALIR VERDE MIENTRAS DURE EL CONGELADO.** Los
once tramos salen con **exitcode 1** y el motivo es el mismo en los once y **no
sale de ninguna mutacion**: **2 arneses que el censo VE y la nomina NO tiene**,
`vuelta197_tarea2_mutacion_orden_del_turno.py` y
`vuelta199_tarea1_mutacion_guardas_revividas.py`. **La regla de entrada de la
nomina y la moratoria `6.3` se contradicen**, y `AUDITOR.md` 0 dice que cuando
una guarda contradice una decision escrita del fundador, **la que se corrige es
la guarda**. **No la corrijo yo**: es codigo, y la moratoria lo prohibe. **Se
escribe como PARADA y no se arregla.**

**PARADA `2`: UN BLOQUE DE ARNES CON EL SUJETO VIVO.** El bloque `F` de
`vuelta185_tarea1c_mutacion_bateria_continuada.py` sale `NO MORDIO` porque **esta
misma vuelta re sella los nueve ficheros cuyo `git log` el bloque afirma**. Sus
otros seis bloques calzan enteros y sus casos caen al mutar el esperado, **asi
que la guarda esta viva**. **Es la consecuencia medida de no clonar el lanzador**,
que es lo que el encargo manda por defecto.

**LO QUE LA 201 SE VA A ENCONTRAR, Y SE DICE PARA QUE NO LO REDESCUBRA:**

- **la nomina mide 135 y CALZA con el congelado**, con `CASOS_DECLARADOS` en 2, y
  **el censo reconoce 197 arneses**;
- **2 arneses del censo quedan fuera de la nomina con la vara 148**, y son
  `vuelta197_tarea2_mutacion_orden_del_turno.py` y
  `vuelta199_tarea1_mutacion_guardas_revividas.py`; **sin vara son 62**. **Las dos
  cifras van juntas**, porque un numero solo al lado de un censo de 197 y una
  nomina de 135 se lee como cobertura total y es cobertura desde la vara arriba;
- **el siguiente libre de la serie es `R.61`**, con 0 colisiones y 0 huecos;
- **la 198 sigue sin entrada propia y sin reporte archivado**, medido hoy;
- **las nueve selladas de la 183 viven preservadas** en
  `docs/loop/preservadas/v183/`, identicas byte a byte a las de su corrida, **y
  las que llevan ese nombre en `docs/loop/` son ya las de esta vuelta**;
- **el trabajo de plan que la 199 adjudico y la cadencia aparto de aqui sigue
  entero**: la **CORRECCION DECLARADA de la evidencia de `OP-I-01`** (ficha 323
  contra fichero 672, adjudicacion `4.1` del acta 199, **NO ES PARADA**) y la
  **MEDICION DE `OP-L-02` CONTRA SU `verificacion`, no contra su `evidencia`**
  (adjudicacion `4.2`). **Ninguna de las dos se empezo en esta vuelta.**

**Y SIGUEN FUERA, NOMBRADAS:** la guarda de codigo del hallazgo `5.3` del acta
194; `acumulan()` que lea la tabla; el cotejo de clon declarado; **que hacer con
las filas `B` del archivo**, que el hallazgo `5.1` del acta 199 vuelve a poner
encima de la mesa; y **los puestos que dos o tres lectores independientes
fallaron**, nombrados y medidos y no resueltos, porque mover una clase es del
RECOMPUTO.

**UNA COSA MAS QUE VA DICHA PORQUE SE HIZO A MANO.** `cerrar_reporte.py` salio
**VERDE con sus cuatro piezas** y **compone el la seccion 9 el solo**, sin admitir
texto anadido. El punto `2.f` del encargo manda **nombrar los dos arneses EN LA
SECCION 9**, asi que ese parrafo **se escribio despues del cierre**, y **no se
quedo sin comprobar**: `docs/loop/SALIDA_V200_REVERIFICACION_DEL_CIERRE.txt` vuelve
a correr **las mismas guardas puras de `cerrar_reporte.py`, importadas y no
copiadas**, sobre el fichero tal como queda en disco, y da **0 cifras sin pareja,
0 descartes de cobertura, 0 motivos de la seccion 4, 0 citas de arnes que no
calzan, 0 guiones largos y 0 medios**, con **las siete secciones presentes**, **el
cuerpo del cierre byte a byte dentro** y **los dos literales del reporte sin
cerrar ya fuera**. **Ninguna guarda se afloja: se re corren.**

## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE

**CORRIDA ENTERA Y SOLA, Y SU SALIDA VA AQUI COMPLETA Y SIN RECORTAR.**
Fichero: `docs/loop/SALIDA_V183_BATERIA.txt` (**92570 bytes en disco y 92570 normalizado a LF**, **1312 lineas
no vacias**, contadas
por `scripts/loop/cerrar_reporte.py`). **Este instrumento CAE EN ROJO si esta
seccion se queda sin ella**, que es la cuarta de sus cuatro piezas.

**LOS DOS ARNESES DEL CENSO QUE QUEDAN FUERA DE LA NOMINA CON LA VARA 148, NOMBRADOS
AQUI COMO EL ENCARGO MANDA, Y MEDIDOS POR MI AL ABRIR Y AL CERRAR:**
`vuelta197_tarea2_mutacion_orden_del_turno.py` y
`vuelta199_tarea1_mutacion_guardas_revividas.py`. **Con la vara 148 son 2 al abrir
y 2 al cerrar; sin vara son 62 al abrir y 62 al cerrar**, sobre un censo de **197**
arneses y una nomina de **135** con `CASOS_DECLARADOS` en **2**. La medida de
apertura esta en el bloque `F` de `docs/loop/SALIDA_V200_APERTURA.txt`, tomada
antes de la primera operacion, y la de cierre la recomputa la propia bateria al
cerrar cada uno de los once tramos. **NO ES UN DESCUIDO DE NADIE: es consecuencia
del congelado en 135 de `AUDITOR.md` 6.3, y por eso se dice en vez de callarse.**
**LA BATERIA NO LOS CORRIO NI LOS PODIA CORRER**, y el segundo lo escribio la
vuelta 199. **Ese mismo hecho es el que pone los once tramos en exitcode 1**, y va
como PARADA `1` en la seccion 8.

```
LA BATERIA DE MUTACIONES DE LA VUELTA 183, CORRIDA ENTERA Y EN TRAMOS
compuesta por scripts/loop/vuelta183_bateria_por_tramos.py --componer

LO QUE SE PARTIO ES EL BOCADO, NO LA BATERIA. Las cuatro cosas que la
letra del fundador del 5 sep 2026 fija siguen enteras: la cadencia (cada
cinco vueltas), la soledad (vuelta propia sin nada al lado), la
integridad (cada entrada corrida, y corrida DOS VECES) y la prohibicion
de podar la nomina.

CIFRA entradas de la nomina: 135
CIFRA tramos: 11
CIFRA entradas que los tramos dicen haber corrido: 135
CIFRA entradas sin correr: 0 | repetidas: 0 | ajenas: 0
LA COBERTURA SE LEYO DE LAS SALIDAS, no se recalculo del reparto.

  tramo 1 -> SALIDA_V183_BATERIA_TRAMO_1.txt: 9558 bytes disco, 9558 bytes LF, 129 lineas, sha256 413cf381cac38391
  tramo 2 -> SALIDA_V183_BATERIA_TRAMO_2.txt: 7804 bytes disco, 7804 bytes LF, 123 lineas, sha256 553e56b775af0ef4
  tramo 3 -> SALIDA_V183_BATERIA_TRAMO_3.txt: 7857 bytes disco, 7857 bytes LF, 123 lineas, sha256 5156e936d0053599
  tramo 4 -> SALIDA_V183_BATERIA_TRAMO_4.txt: 7867 bytes disco, 7867 bytes LF, 123 lineas, sha256 75acd39e3b709189
  tramo 5 -> SALIDA_V183_BATERIA_TRAMO_5.txt: 7827 bytes disco, 7827 bytes LF, 123 lineas, sha256 2f4ba7df501556c8
  tramo 6 -> SALIDA_V183_BATERIA_TRAMO_6.txt: 7887 bytes disco, 7887 bytes LF, 123 lineas, sha256 98498ba8f979eace
  tramo 7 -> SALIDA_V183_BATERIA_TRAMO_7.txt: 7893 bytes disco, 7893 bytes LF, 123 lineas, sha256 c09960750d7c1ea4
  tramo 8 -> SALIDA_V183_BATERIA_TRAMO_8.txt: 7848 bytes disco, 7848 bytes LF, 123 lineas, sha256 b07f055c9e20934d
  tramo 9 -> SALIDA_V183_BATERIA_TRAMO_9.txt: 8523 bytes disco, 8523 bytes LF, 125 lineas, sha256 c323573fb6b3f9b7
  tramo 10 -> SALIDA_V183_BATERIA_TRAMO_10.txt: 8475 bytes disco, 8475 bytes LF, 123 lineas, sha256 a91d4a64007fcb93
  tramo 11 -> SALIDA_V183_BATERIA_TRAMO_11.txt: 6273 bytes disco, 6273 bytes LF, 94 lineas, sha256 f50d0fbbd5546bb2
==============================================================================

==============================================================================
TRAMO 1 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_1.txt
==============================================================================

CORRIDA DEL TRAMO 1 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T13:28:40Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 8a60182f750f, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 8a60182f750f, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 8a60182f750f, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 1 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta133_tarea2e_mutacion_cifras.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_1.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_2.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_3.py
      ENTRADA DEL TRAMO: vuelta139_2b_mutaciones.py
      ENTRADA DEL TRAMO: vuelta140_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta141_2_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2b_mutacion_bateria.py
      ENTRADA DEL TRAMO: vuelta143_2c_mutacion_positivo.py
      ENTRADA DEL TRAMO: vuelta144_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_2b_mutacion_giro.py
      ENTRADA DEL TRAMO: vuelta144_2d_mutacion_cobertura.py


  vuelta133_tarea2e_mutacion_cifras.py   exit 0  OK                   5.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta135_2e_mutacion_1.py             exit 0  OK                  11.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_1.txt
  vuelta135_2e_mutacion_2.py             exit 0  OK                  11.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_2.txt
  vuelta135_2e_mutacion_3.py             exit 1  CASO DECLARADO      11.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_3.txt
      SUJETO FIJO VERIFICADO: SUJETO_FIJO_V135_2E_REPORTE_134.md calza con el blob e12e4c36 (sha256 d1f97a510f17e35046eeec4975e1e0a1adabcfdda5a4646a250aa6db
  vuelta139_2b_mutaciones.py             exit 0  OK                  11.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta140_2a_mutaciones.py             exit 2  CASO DECLARADO      11.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta141_2_mutaciones.py              exit 0  OK                  10.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2a_mutaciones.py             exit 0  OK                  12.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2b_mutacion_bateria.py       exit 0  OK                  11.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2c_mutacion_positivo.py      exit 0  OK                  12.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2a_mutaciones.py             exit 0  OK                  11.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2b_mutacion_giro.py          exit 0  OK                  15.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2d_mutacion_cobertura.py     exit 0  OK                  11.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 148.1
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.5
  CIFRA arnes MAS LENTO: vuelta144_2b_mutacion_giro.py con 15.3s
  CIFRA arnes MAS RAPIDO: vuelta133_tarea2e_mutacion_cifras.py con 5.2s
  CIFRA mediana por arnes, en segundos: 11.5
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta144_2b_mutacion_giro.py                 15.3s
      vuelta143_2c_mutacion_positivo.py             12.9s
      vuelta143_2a_mutaciones.py                    12.5s
      vuelta143_2b_mutacion_bateria.py              11.9s
      vuelta135_2e_mutacion_1.py                    11.7s
      vuelta135_2e_mutacion_2.py                    11.7s
      vuelta140_2a_mutaciones.py                    11.5s
      vuelta139_2b_mutaciones.py                    11.5s
      vuelta144_2a_mutaciones.py                    11.0s
      vuelta135_2e_mutacion_3.py                    11.0s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 2 (vuelta135_2e_mutacion_3.py, vuelta140_2a_mutaciones.py)
      vuelta135_2e_mutacion_3.py, exit declarado 1, marca obligatoria 'NO TIENE CONVENCION MECANICA DE CONTEO':
         su SUJETO FIJO es el REPORTE.md de la vuelta 134, congelado por banco 9.10, y ES ANTERIOR A LOS DELIMITADORES DE CABECERA TALLADA. Medido en esta vuelta: grep -c 'CABECERA TALLADA' docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md da 0, y sobre docs/loop/REPORTE.md da 3. La ampliacion del vocabulario de la TAREA 2.a (vuelta 142) hace que la guarda vea ahora la celda '3 fila(s)' del desfase del calibrado, que EN UN REPORTE MODERNO vive DENTRO de la cabecera delimitada y queda recortada antes de parsear, y en este sujeto no, porque las marcas no existian aun. LAS DOS CIFRAS QUE ESTA MUTACION PRUEBA SI COTEJAN (la salida publica '2 POR ETIQUETA'): lo que cae es una tercera, ajena al caso. El sujeto NO se retoca, porque su valor es estar congelado.
      vuelta140_2a_mutaciones.py, exit declarado 2, marca obligatoria 'VEREDICTO (iii): NO CALZA':
         su bloque (iii), el caso positivo sobre la fase 05, sale NO CALZA y esta DECLARADO desde la vuelta 140: el auditor lo reconocio como caida SUYA de encargo (acta 140, 4.5, 'EL AUDITOR ELIGIO MAL EL SUJETO CONGELADO'). OP-S-05, OP-S-08, OP-S-11 y OP-S-12 tienen HUELLA DE GRAFO IDENTICA (los cuatro campos vacios) y lo unico que las separa es `estado`, que el encargo prohibe mirar: NINGUNA VARA DE GRAFO PUEDE SEPARARLAS. Los bloques (i) y (ii) SI muerden y son los que esta bateria vigila.
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 8a60182f750f, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 8a60182f750f, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 1: 1
FIN (reloj de pared, UTC): 2026-09-07T13:31:10Z
DURACION DEL TRAMO (monotona, segundos): 150.4
DURACION DEL TRAMO (monotona, minutos): 2.5


==============================================================================
TRAMO 2 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_2.txt
==============================================================================

CORRIDA DEL TRAMO 2 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T13:32:52Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 44fd9bbe650f, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 44fd9bbe650f, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 44fd9bbe650f, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 2 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta144_3a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_3b_mutacion_negativa.py
      ENTRADA DEL TRAMO: vuelta144_3c_caso_positivo_1190.py
      ENTRADA DEL TRAMO: vuelta145_2a_mutacion_ancla_unica.py
      ENTRADA DEL TRAMO: vuelta145_2b_mutacion_arneses.py
      ENTRADA DEL TRAMO: vuelta145_2c_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta146_2b_mutacion_ausencias.py
      ENTRADA DEL TRAMO: vuelta147_2c_mutacion_vitalidad.py
      ENTRADA DEL TRAMO: vuelta147_3d_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta147_3e_simular_a26.py
      ENTRADA DEL TRAMO: vuelta148_0d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta148_1a_mutacion_embebido.py
      ENTRADA DEL TRAMO: vuelta148_2a_mutacion_nomina_commiteada.py


  vuelta144_3a_mutaciones.py             exit 0  OK                   7.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3b_mutacion_negativa.py      exit 0  OK                  24.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3c_caso_positivo_1190.py     exit 0  OK                  11.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2a_mutacion_ancla_unica.py   exit 0  OK                  11.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2b_mutacion_arneses.py       exit 0  OK                  46.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2c_mutacion_censo.py         exit 0  OK                  33.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta146_2b_mutacion_ausencias.py     exit 0  OK                  11.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_2c_mutacion_vitalidad.py     exit 0  OK                 175.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3d_mutacion_nomina.py        exit 0  OK                  13.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3e_simular_a26.py            exit 0  OK                  13.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_0d_mutacion_corredor.py      exit 0  OK                  14.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_1a_mutacion_embebido.py      exit 0  OK                  14.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2a_mutacion_nomina_commiteada.py exit 0  OK                   7.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 384.8
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 6.4
  CIFRA arnes MAS LENTO: vuelta147_2c_mutacion_vitalidad.py con 175.5s
  CIFRA arnes MAS RAPIDO: vuelta148_2a_mutacion_nomina_commiteada.py con 7.3s
  CIFRA mediana por arnes, en segundos: 13.5
  CIFRA arneses que pasan de 30 segundos: 3
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta147_2c_mutacion_vitalidad.py           175.5s
      vuelta145_2b_mutacion_arneses.py              46.0s
      vuelta145_2c_mutacion_censo.py                33.7s
      vuelta144_3b_mutacion_negativa.py             24.4s
      vuelta148_1a_mutacion_embebido.py             14.6s
      vuelta148_0d_mutacion_corredor.py             14.6s
      vuelta147_3d_mutacion_nomina.py               13.5s
      vuelta147_3e_simular_a26.py                   13.4s
      vuelta146_2b_mutacion_ausencias.py            11.7s
      vuelta144_3c_caso_positivo_1190.py            11.4s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 44fd9bbe650f, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 44fd9bbe650f, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 2: 1
FIN (reloj de pared, UTC): 2026-09-07T13:39:18Z
DURACION DEL TRAMO (monotona, segundos): 386.2
DURACION DEL TRAMO (monotona, minutos): 6.4


==============================================================================
TRAMO 3 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_3.txt
==============================================================================

CORRIDA DEL TRAMO 3 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T13:50:26Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD ff6c1d151d64, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD ff6c1d151d64, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD ff6c1d151d64, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 3 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta148_2b_mutacion_cifras_conjunto.py
      ENTRADA DEL TRAMO: vuelta148_2c_mutacion_vara_parada.py
      ENTRADA DEL TRAMO: vuelta148_2d_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta150_5c_mutacion_ciclo.py
      ENTRADA DEL TRAMO: vuelta154_tarea2d_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta154_tarea6_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta156_tarea4b_mutacion_tallador.py
      ENTRADA DEL TRAMO: vuelta156_tarea5d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta157_tarea4b_mutacion_tachado.py
      ENTRADA DEL TRAMO: vuelta157_tarea5c_mutacion_ruido.py
      ENTRADA DEL TRAMO: vuelta157_tarea6b_mutacion_re_sellado.py
      ENTRADA DEL TRAMO: vuelta159_tarea6c_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta160_tarea6b_mutacion_puerta.py


  vuelta148_2b_mutacion_cifras_conjunto.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2c_mutacion_vara_parada.py   exit 0  OK                  10.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2d_mutacion_exencion.py      exit 0  OK                  11.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta150_5c_mutacion_ciclo.py         exit 0  OK                  12.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta154_tarea2d_mutacion_guarda.py   exit 0  OK                 185.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta154_tarea6_mutacion_corredor.py  exit 0  OK                  13.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea4b_mutacion_tallador.py exit 0  OK                  12.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea5d_mutacion_corredor.py exit 0  OK                  46.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea4b_mutacion_tachado.py  exit 0  OK                  11.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea5c_mutacion_ruido.py    exit 0  OK                  11.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea6b_mutacion_re_sellado.py exit 0  OK                  14.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta159_tarea6c_mutacion_exencion.py exit 0  OK                 357.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea6b_mutacion_puerta.py   exit 0  OK                  82.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 769.8
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 12.8
  CIFRA arnes MAS LENTO: vuelta159_tarea6c_mutacion_exencion.py con 357.2s
  CIFRA arnes MAS RAPIDO: vuelta148_2b_mutacion_cifras_conjunto.py con 2.5s
  CIFRA mediana por arnes, en segundos: 12.5
  CIFRA arneses que pasan de 30 segundos: 4
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta159_tarea6c_mutacion_exencion.py       357.2s
      vuelta154_tarea2d_mutacion_guarda.py         185.7s
      vuelta160_tarea6b_mutacion_puerta.py          82.0s
      vuelta156_tarea5d_mutacion_corredor.py        46.1s
      vuelta157_tarea6b_mutacion_re_sellado.py      14.1s
      vuelta154_tarea6_mutacion_corredor.py         13.0s
      vuelta150_5c_mutacion_ciclo.py                12.5s
      vuelta156_tarea4b_mutacion_tallador.py        12.0s
      vuelta148_2d_mutacion_exencion.py             11.6s
      vuelta157_tarea5c_mutacion_ruido.py           11.4s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD ff6c1d151d64, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD ff6c1d151d64, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 3: 1
FIN (reloj de pared, UTC): 2026-09-07T14:03:20Z
DURACION DEL TRAMO (monotona, segundos): 772.2
DURACION DEL TRAMO (monotona, minutos): 12.9


==============================================================================
TRAMO 4 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_4.txt
==============================================================================

CORRIDA DEL TRAMO 4 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T14:04:41Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 36ebfb3d29f8, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 36ebfb3d29f8, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 36ebfb3d29f8, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 4 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta160_tarea7c_mutacion_guarda_cita.py
      ENTRADA DEL TRAMO: vuelta161_tarea1a_mutacion_alcance.py
      ENTRADA DEL TRAMO: vuelta162_tarea1a_mutacion_serie.py
      ENTRADA DEL TRAMO: vuelta162_tarea2a_mutacion_puerta.py
      ENTRADA DEL TRAMO: vuelta162_tarea2b_mutacion_excepcion.py
      ENTRADA DEL TRAMO: vuelta162_tarea3_mutacion_fila.py
      ENTRADA DEL TRAMO: vuelta163_tarea1b_mutacion_relectura.py
      ENTRADA DEL TRAMO: vuelta163_tarea1c_mutacion_tramo.py
      ENTRADA DEL TRAMO: vuelta163_tarea2_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta163_tarea4a_mutacion_cobertura.py
      ENTRADA DEL TRAMO: vuelta163_tarea4b_mutacion_re_sellado.py
      ENTRADA DEL TRAMO: vuelta163_tarea5a_mutacion_contador.py
      ENTRADA DEL TRAMO: vuelta164_tarea1_mutacion_registro.py


  vuelta160_tarea7c_mutacion_guarda_cita.py exit 0  OK                  18.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta161_tarea1a_mutacion_alcance.py  exit 0  OK                  21.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea1a_mutacion_serie.py    exit 0  OK                  12.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2a_mutacion_puerta.py   exit 0  OK                  13.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2b_mutacion_excepcion.py exit 0  OK                  10.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea3_mutacion_fila.py      exit 0  OK                  11.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1b_mutacion_relectura.py exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1c_mutacion_tramo.py    exit 0  OK                  10.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea2_mutacion_nomina.py    exit 0  OK                  11.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4a_mutacion_cobertura.py exit 0  OK                  13.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4b_mutacion_re_sellado.py exit 0  OK                  35.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea5a_mutacion_contador.py exit 0  OK                   5.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta164_tarea1_mutacion_registro.py  exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 178.5
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 3.0
  CIFRA arnes MAS LENTO: vuelta163_tarea4b_mutacion_re_sellado.py con 35.7s
  CIFRA arnes MAS RAPIDO: vuelta164_tarea1_mutacion_registro.py con 2.6s
  CIFRA mediana por arnes, en segundos: 11.6
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta163_tarea4b_mutacion_re_sellado.py      35.7s
      vuelta161_tarea1a_mutacion_alcance.py         21.0s
      vuelta160_tarea7c_mutacion_guarda_cita.py     18.3s
      vuelta163_tarea4a_mutacion_cobertura.py       13.6s
      vuelta162_tarea2a_mutacion_puerta.py          13.3s
      vuelta162_tarea1a_mutacion_serie.py           12.6s
      vuelta162_tarea3_mutacion_fila.py             11.6s
      vuelta163_tarea2_mutacion_nomina.py           11.4s
      vuelta163_tarea1b_mutacion_relectura.py       11.3s
      vuelta162_tarea2b_mutacion_excepcion.py       10.9s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 36ebfb3d29f8, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 36ebfb3d29f8, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 4: 1
FIN (reloj de pared, UTC): 2026-09-07T14:07:41Z
DURACION DEL TRAMO (monotona, segundos): 179.9
DURACION DEL TRAMO (monotona, minutos): 3.0


==============================================================================
TRAMO 5 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_5.txt
==============================================================================

CORRIDA DEL TRAMO 5 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T14:08:20Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 320e4c1caf27, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 320e4c1caf27, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 320e4c1caf27, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 5 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta164_tarea4_mutacion_005.py
      ENTRADA DEL TRAMO: vuelta165_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta165_tarea2_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta165_tarea4_mutacion_sujeto.py
      ENTRADA DEL TRAMO: vuelta165_tarea6_mutacion_op_l_01.py
      ENTRADA DEL TRAMO: vuelta166_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta166_tarea2_mutacion_correccion.py
      ENTRADA DEL TRAMO: vuelta166_tarea3_mutacion_retrato.py
      ENTRADA DEL TRAMO: vuelta166_tarea6_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta167_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta167_tarea3_mutacion_ii.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_nota.py


  vuelta164_tarea4_mutacion_005.py       exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea1_mutacion_registro.py  exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea2_mutacion_censo.py     exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea4_mutacion_sujeto.py    exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea6_mutacion_op_l_01.py   exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea1_mutacion_registro.py  exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea2_mutacion_correccion.py exit 0  OK                   3.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea3_mutacion_retrato.py   exit 0  OK                   7.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea6_mutacion_guarda.py    exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta167_tarea1_mutacion_registro.py  exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta167_tarea3_mutacion_ii.py        exit 0  OK                   3.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_registro.py  exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_nota.py      exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 40.8
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.7
  CIFRA arnes MAS LENTO: vuelta166_tarea3_mutacion_retrato.py con 7.1s
  CIFRA arnes MAS RAPIDO: vuelta166_tarea1_mutacion_registro.py con 2.6s
  CIFRA mediana por arnes, en segundos: 2.8
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta166_tarea3_mutacion_retrato.py           7.1s
      vuelta167_tarea3_mutacion_ii.py                3.3s
      vuelta166_tarea2_mutacion_correccion.py        3.3s
      vuelta165_tarea4_mutacion_sujeto.py            3.0s
      vuelta164_tarea4_mutacion_005.py               2.9s
      vuelta168_tarea1_mutacion_nota.py              2.9s
      vuelta165_tarea2_mutacion_censo.py             2.8s
      vuelta168_tarea1_mutacion_registro.py          2.6s
      vuelta165_tarea6_mutacion_op_l_01.py           2.6s
      vuelta165_tarea1_mutacion_registro.py          2.6s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 320e4c1caf27, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 320e4c1caf27, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 5: 1
FIN (reloj de pared, UTC): 2026-09-07T14:09:02Z
DURACION DEL TRAMO (monotona, segundos): 42.4
DURACION DEL TRAMO (monotona, minutos): 0.7


==============================================================================
TRAMO 6 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_6.txt
==============================================================================

CORRIDA DEL TRAMO 6 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T14:09:35Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 2b5bbf53e744, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 2b5bbf53e744, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 2b5bbf53e744, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 6 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta168_tarea2_mutacion_reconstructor.py
      ENTRADA DEL TRAMO: vuelta168_tarea4_mutacion_op_v_01.py
      ENTRADA DEL TRAMO: vuelta169_tarea2_mutacion_reanclaje.py
      ENTRADA DEL TRAMO: vuelta170_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta170_tarea2a_mutacion_aislador.py
      ENTRADA DEL TRAMO: vuelta98_tarea4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta99_tarea3_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta109_tarea2_4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py
      ENTRADA DEL TRAMO: vuelta113_tarea2_mutacion_tsc.py
      ENTRADA DEL TRAMO: vuelta171_mutacion_busqueda_acta.py
      ENTRADA DEL TRAMO: vuelta171_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta171_tarea5a_mutacion_enchufe.py


  vuelta168_tarea2_mutacion_reconstructor.py exit 0  OK                   5.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea4_mutacion_op_v_01.py   exit 0  OK                  24.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta169_tarea2_mutacion_reanclaje.py exit 0  OK                  12.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea1a_mutacion_registro.py exit 0  OK                  12.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea2a_mutacion_aislador.py exit 0  OK                  13.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta98_tarea4_prueba_mutacion.py     exit 0  OK                  11.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta99_tarea3_prueba_mutacion.py     exit 0  OK                  12.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta109_tarea2_4_prueba_mutacion.py  exit 0  OK                  24.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta113_tarea2_mutacion_tsc.py       exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_mutacion_busqueda_acta.py    exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_tarea1a_mutacion_registro.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_tarea5a_mutacion_enchufe.py  exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 128.9
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.1
  CIFRA arnes MAS LENTO: vuelta109_tarea2_4_prueba_mutacion.py con 24.6s
  CIFRA arnes MAS RAPIDO: vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py con 2.5s
  CIFRA mediana por arnes, en segundos: 11.8
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta109_tarea2_4_prueba_mutacion.py         24.6s
      vuelta168_tarea4_mutacion_op_v_01.py          24.3s
      vuelta170_tarea2a_mutacion_aislador.py        13.8s
      vuelta169_tarea2_mutacion_reanclaje.py        12.4s
      vuelta99_tarea3_prueba_mutacion.py            12.3s
      vuelta170_tarea1a_mutacion_registro.py        12.3s
      vuelta98_tarea4_prueba_mutacion.py            11.8s
      vuelta168_tarea2_mutacion_reconstructor.py     5.0s
      vuelta171_mutacion_busqueda_acta.py            2.5s
      vuelta171_tarea5a_mutacion_enchufe.py          2.5s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 2b5bbf53e744, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 2b5bbf53e744, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 6: 1
FIN (reloj de pared, UTC): 2026-09-07T14:11:45Z
DURACION DEL TRAMO (monotona, segundos): 130.2
DURACION DEL TRAMO (monotona, minutos): 2.2


==============================================================================
TRAMO 7 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_7.txt
==============================================================================

CORRIDA DEL TRAMO 7 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T14:12:37Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 0941c3f07c97, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 0941c3f07c97, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 0941c3f07c97, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 7 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta172_tarea1b_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta172_tarea2a_mutacion_exclusion.py
      ENTRADA DEL TRAMO: vuelta172_tarea3_mutacion_numeracion.py
      ENTRADA DEL TRAMO: vuelta172_tarea5_mutacion_cierre.py
      ENTRADA DEL TRAMO: vuelta173_tarea1b_mutacion_hueco.py
      ENTRADA DEL TRAMO: vuelta174_tarea1a_mutacion_44.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_esqueleto.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_sellar.py
      ENTRADA DEL TRAMO: vuelta174_tarea2b_mutacion_confirmar.py
      ENTRADA DEL TRAMO: vuelta176_tarea1c_mutacion_tramos.py
      ENTRADA DEL TRAMO: vuelta177_tarea1b_mutacion_esperado_vivo.py
      ENTRADA DEL TRAMO: vuelta177_tarea1d_mutacion_cotejo.py
      ENTRADA DEL TRAMO: vuelta177_tarea1e_mutacion_correcciones_chicas.py


  vuelta172_tarea1b_mutacion_registro.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea2a_mutacion_exclusion.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea3_mutacion_numeracion.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea5_mutacion_cierre.py    exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta173_tarea1b_mutacion_hueco.py    exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1a_mutacion_44.py       exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_esqueleto.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_sellar.py   exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea2b_mutacion_confirmar.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta176_tarea1c_mutacion_tramos.py   exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1b_mutacion_esperado_vivo.py exit 0  OK                   3.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1d_mutacion_cotejo.py   exit 0  OK                   3.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1e_mutacion_correcciones_chicas.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 34.3
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.6
  CIFRA arnes MAS LENTO: vuelta177_tarea1d_mutacion_cotejo.py con 3.5s
  CIFRA arnes MAS RAPIDO: vuelta174_tarea2b_mutacion_confirmar.py con 2.5s
  CIFRA mediana por arnes, en segundos: 2.5
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta177_tarea1d_mutacion_cotejo.py           3.5s
      vuelta177_tarea1b_mutacion_esperado_vivo.py     3.2s
      vuelta172_tarea1b_mutacion_registro.py         2.6s
      vuelta172_tarea5_mutacion_cierre.py            2.6s
      vuelta173_tarea1b_mutacion_hueco.py            2.5s
      vuelta172_tarea3_mutacion_numeracion.py        2.5s
      vuelta174_tarea1b_mutacion_sellar.py           2.5s
      vuelta177_tarea1e_mutacion_correcciones_chicas.py     2.5s
      vuelta176_tarea1c_mutacion_tramos.py           2.5s
      vuelta174_tarea1b_mutacion_esqueleto.py        2.5s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 0941c3f07c97, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 0941c3f07c97, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 7: 1
FIN (reloj de pared, UTC): 2026-09-07T14:13:12Z
DURACION DEL TRAMO (monotona, segundos): 35.6
DURACION DEL TRAMO (monotona, minutos): 0.6


==============================================================================
TRAMO 8 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_8.txt
==============================================================================

CORRIDA DEL TRAMO 8 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T14:13:47Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD f582790832f2, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD f582790832f2, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD f582790832f2, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 8 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta177_tarea1f_mutacion_tope_minutos.py
      ENTRADA DEL TRAMO: vuelta178_tarea1b_mutacion_hermano.py
      ENTRADA DEL TRAMO: vuelta178_tarea1c_mutacion_ast.py
      ENTRADA DEL TRAMO: vuelta178_tarea1d_mutacion_puestos.py
      ENTRADA DEL TRAMO: vuelta178_tarea1e_mutacion_higiene.py
      ENTRADA DEL TRAMO: vuelta178_tarea2_mutacion_resolutor.py
      ENTRADA DEL TRAMO: vuelta178_tarea4_mutacion_consumidas.py
      ENTRADA DEL TRAMO: vuelta150_2d_simular_op_c_05.py
      ENTRADA DEL TRAMO: vuelta160_tarea3b_caso_positivo.py
      ENTRADA DEL TRAMO: vuelta179_tarea1b_mutacion_citas.py
      ENTRADA DEL TRAMO: vuelta179_tarea3_mutacion_triangulos.py
      ENTRADA DEL TRAMO: vuelta179_tarea1d_mutacion_corte.py
      ENTRADA DEL TRAMO: vuelta180_tarea1b_mutacion_etiqueta.py


  vuelta177_tarea1f_mutacion_tope_minutos.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1b_mutacion_hermano.py  exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1c_mutacion_ast.py      exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1d_mutacion_puestos.py  exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1e_mutacion_higiene.py  exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea2_mutacion_resolutor.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea4_mutacion_consumidas.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta150_2d_simular_op_c_05.py        exit 0  OK                   4.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea3b_caso_positivo.py     exit 0  OK                  12.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea1b_mutacion_citas.py    exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea3_mutacion_triangulos.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea1d_mutacion_corte.py    exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea1b_mutacion_etiqueta.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 45.2
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.8
  CIFRA arnes MAS LENTO: vuelta160_tarea3b_caso_positivo.py con 12.1s
  CIFRA arnes MAS RAPIDO: vuelta178_tarea2_mutacion_resolutor.py con 2.5s
  CIFRA mediana por arnes, en segundos: 2.5
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta160_tarea3b_caso_positivo.py            12.1s
      vuelta150_2d_simular_op_c_05.py                4.1s
      vuelta178_tarea1d_mutacion_puestos.py          3.1s
      vuelta178_tarea1c_mutacion_ast.py              2.9s
      vuelta180_tarea1b_mutacion_etiqueta.py         2.7s
      vuelta178_tarea1e_mutacion_higiene.py          2.7s
      vuelta177_tarea1f_mutacion_tope_minutos.py     2.5s
      vuelta179_tarea3_mutacion_triangulos.py        2.5s
      vuelta179_tarea1b_mutacion_citas.py            2.5s
      vuelta179_tarea1d_mutacion_corte.py            2.5s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD f582790832f2, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD f582790832f2, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 8: 1
FIN (reloj de pared, UTC): 2026-09-07T14:14:33Z
DURACION DEL TRAMO (monotona, segundos): 46.6
DURACION DEL TRAMO (monotona, minutos): 0.8


==============================================================================
TRAMO 9 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_9.txt
==============================================================================

CORRIDA DEL TRAMO 9 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T14:15:15Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD fe90a62d0115, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD fe90a62d0115, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD fe90a62d0115, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 9 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta180_tarea2c_mutacion_cableado.py
      ENTRADA DEL TRAMO: vuelta180_tarea3_mutacion_corte_de_tramos.py
      ENTRADA DEL TRAMO: vuelta180_tarea4_mutacion_texto_y_clon.py
      ENTRADA DEL TRAMO: vuelta180_tarea5_mutacion_backlog_l02.py
      ENTRADA DEL TRAMO: vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py
      ENTRADA DEL TRAMO: vuelta182_tarea2_mutacion_apertura_auditor.py
      ENTRADA DEL TRAMO: vuelta183_tarea1c_mutacion_veredicto.py
      ENTRADA DEL TRAMO: vuelta183_tarea1b_mutacion_atribucion.py
      ENTRADA DEL TRAMO: vuelta184_tarea1c_mutacion_estimacion.py
      ENTRADA DEL TRAMO: vuelta185_tarea1b_mutacion_sin_temporal.py
      ENTRADA DEL TRAMO: vuelta185_tarea1c_mutacion_bateria_continuada.py
      ENTRADA DEL TRAMO: vuelta186_tarea2a_mutacion_pieza4.py
      ENTRADA DEL TRAMO: vuelta186_tarea2b_mutacion_pieza2_cercas.py


  vuelta180_tarea2c_mutacion_cableado.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea3_mutacion_corte_de_tramos.py exit 0  OK                  10.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea4_mutacion_texto_y_clon.py exit 0  OK                  11.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea5_mutacion_backlog_l02.py exit 0  OK                  10.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py exit 0  OK                  11.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta182_tarea2_mutacion_apertura_auditor.py exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt
  vuelta183_tarea1c_mutacion_veredicto.py exit 0  OK                  11.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V183_T1C_MUTACION_VEREDICTO.txt
  vuelta183_tarea1b_mutacion_atribucion.py exit 0  OK                  11.6s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V183_T1B_MUTACION_ATRIBUCION.txt
  vuelta184_tarea1c_mutacion_estimacion.py exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V184_T1C_MUTACION_ESTIMACION.txt
  vuelta185_tarea1b_mutacion_sin_temporal.py exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt, SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt
  vuelta185_tarea1c_mutacion_bateria_continuada.py exit 1  NO MORDIO           13.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt
      ARNES DE LA RAMA DE LA BATERIA CONTINUADA (vuelta 185, TAREA 1.c)
  vuelta186_tarea2a_mutacion_pieza4.py   exit 0  OK                  10.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2A_MUTACION_PIEZA4.txt
  vuelta186_tarea2b_mutacion_pieza2_cercas.py exit 0  OK                  10.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 138.6
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.3
  CIFRA arnes MAS LENTO: vuelta185_tarea1c_mutacion_bateria_continuada.py con 13.0s
  CIFRA arnes MAS RAPIDO: vuelta180_tarea2c_mutacion_cableado.py con 2.6s
  CIFRA mediana por arnes, en segundos: 11.3
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta185_tarea1c_mutacion_bateria_continuada.py    13.0s
      vuelta183_tarea1b_mutacion_atribucion.py      11.6s
      vuelta180_tarea4_mutacion_texto_y_clon.py     11.5s
      vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py    11.5s
      vuelta182_tarea2_mutacion_apertura_auditor.py    11.3s
      vuelta185_tarea1b_mutacion_sin_temporal.py    11.3s
      vuelta184_tarea1c_mutacion_estimacion.py      11.3s
      vuelta183_tarea1c_mutacion_veredicto.py       11.1s
      vuelta180_tarea5_mutacion_backlog_l02.py      10.9s
      vuelta186_tarea2b_mutacion_pieza2_cercas.py    10.8s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 1 (vuelta185_tarea1c_mutacion_bateria_continuada.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD fe90a62d0115, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD fe90a62d0115, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 1 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 1 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 9: 1
FIN (reloj de pared, UTC): 2026-09-07T14:17:36Z
DURACION DEL TRAMO (monotona, segundos): 141.0
DURACION DEL TRAMO (monotona, minutos): 2.3


==============================================================================
TRAMO 10 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_10.txt
==============================================================================

CORRIDA DEL TRAMO 10 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T14:18:16Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 2620b94be8bb, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 2620b94be8bb, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 2620b94be8bb, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 10 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta186_tarea2c_mutacion_cierre_tardio.py
      ENTRADA DEL TRAMO: vuelta186_tarea2d_mutacion_seccion4.py
      ENTRADA DEL TRAMO: vuelta187_tarea4_mutacion_dos_convenciones.py
      ENTRADA DEL TRAMO: vuelta187_tarea5b_mutacion_seccion4_tardio.py
      ENTRADA DEL TRAMO: vuelta188_tarea2_mutacion_pata_documental.py
      ENTRADA DEL TRAMO: vuelta188_tarea3c_mutacion_exclusion_por_rojo.py
      ENTRADA DEL TRAMO: vuelta188_tarea4_mutacion_cobertura_parejas.py
      ENTRADA DEL TRAMO: vuelta188_tarea5a_mutacion_vecinos_evitar.py
      ENTRADA DEL TRAMO: vuelta190_tarea2b_mutacion_deuda_y_fallo.py
      ENTRADA DEL TRAMO: vuelta190_tarea3b_mutacion_selladas_ajenas.py
      ENTRADA DEL TRAMO: vuelta191_tarea3_mutacion_lineas.py
      ENTRADA DEL TRAMO: vuelta191_tarea4_mutacion_veredicto.py
      ENTRADA DEL TRAMO: vuelta191_tarea6_mutacion_bloque_tallado.py


  vuelta186_tarea2c_mutacion_cierre_tardio.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt
  vuelta186_tarea2d_mutacion_seccion4.py exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2D_MUTACION_SECCION4.txt
  vuelta187_tarea4_mutacion_dos_convenciones.py exit 0  OK                  11.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt
  vuelta187_tarea5b_mutacion_seccion4_tardio.py exit 0  OK                  10.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V187_T5B_MUTACION_SECCION4_TARDIO.txt
  vuelta188_tarea2_mutacion_pata_documental.py exit 0  OK                  11.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL.txt
  vuelta188_tarea3c_mutacion_exclusion_por_rojo.py exit 0  OK                  10.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt
  vuelta188_tarea4_mutacion_cobertura_parejas.py exit 0  OK                   9.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt
  vuelta188_tarea5a_mutacion_vecinos_evitar.py exit 0  OK                   2.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T5A_MUTACION_VECINOS_EVITAR.txt
  vuelta190_tarea2b_mutacion_deuda_y_fallo.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt
  vuelta190_tarea3b_mutacion_selladas_ajenas.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt
  vuelta191_tarea3_mutacion_lineas.py    exit 0  OK                  69.3s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T3_MUTACION_LINEAS.txt
  vuelta191_tarea4_mutacion_veredicto.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T4_MUTACION_VEREDICTO.txt
  vuelta191_tarea6_mutacion_bloque_tallado.py exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T6_MUTACION_BLOQUE_TALLADO.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 150.4
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.5
  CIFRA arnes MAS LENTO: vuelta191_tarea3_mutacion_lineas.py con 69.3s
  CIFRA arnes MAS RAPIDO: vuelta188_tarea5a_mutacion_vecinos_evitar.py con 2.4s
  CIFRA mediana por arnes, en segundos: 9.7
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta191_tarea3_mutacion_lineas.py           69.3s
      vuelta187_tarea4_mutacion_dos_convenciones.py    11.7s
      vuelta186_tarea2d_mutacion_seccion4.py        11.3s
      vuelta188_tarea2_mutacion_pata_documental.py    11.0s
      vuelta187_tarea5b_mutacion_seccion4_tardio.py    10.8s
      vuelta188_tarea3c_mutacion_exclusion_por_rojo.py    10.8s
      vuelta188_tarea4_mutacion_cobertura_parejas.py     9.7s
      vuelta191_tarea6_mutacion_bloque_tallado.py     3.0s
      vuelta186_tarea2c_mutacion_cierre_tardio.py     2.7s
      vuelta191_tarea4_mutacion_veredicto.py         2.6s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 2620b94be8bb, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 2620b94be8bb, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 10: 1
FIN (reloj de pared, UTC): 2026-09-07T14:20:48Z
DURACION DEL TRAMO (monotona, segundos): 151.8
DURACION DEL TRAMO (monotona, minutos): 2.5


==============================================================================
TRAMO 11 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_11.txt
==============================================================================

CORRIDA DEL TRAMO 11 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T14:21:58Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 617741f764f9, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 617741f764f9, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 617741f764f9, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 11 de 11
  CIFRA entradas de ESTE tramo: 5
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta192_tarea4_mutacion_cuarta_puerta.py
      ENTRADA DEL TRAMO: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      ENTRADA DEL TRAMO: vuelta194_tarea2c_mutacion_sede_del_turno.py
      ENTRADA DEL TRAMO: vuelta195_tarea3g_mutacion_nomina_enchufada.py
      ENTRADA DEL TRAMO: vuelta195_tarea4c_mutacion_componer_rojo.py


  vuelta192_tarea4_mutacion_cuarta_puerta.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt
  vuelta193_tarea4e_mutacion_sello_entre_procesos.py exit 0  OK                   3.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt
  vuelta194_tarea2c_mutacion_sede_del_turno.py exit 0  OK                   5.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt, SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt, SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt
  vuelta195_tarea3g_mutacion_nomina_enchufada.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V195_T3G_MUTACION_NOMINA_ENCHUFADA.txt
  vuelta195_tarea4c_mutacion_componer_rojo.py exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V195_T4C_MUTACION_COMPONER_ROJO.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 5
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 17.1
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.3
  CIFRA arnes MAS LENTO: vuelta194_tarea2c_mutacion_sede_del_turno.py con 5.4s
  CIFRA arnes MAS RAPIDO: vuelta195_tarea3g_mutacion_nomina_enchufada.py con 2.6s
  CIFRA mediana por arnes, en segundos: 3.0
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta194_tarea2c_mutacion_sede_del_turno.py     5.4s
      vuelta193_tarea4e_mutacion_sello_entre_procesos.py     3.5s
      vuelta195_tarea4c_mutacion_componer_rojo.py     3.0s
      vuelta192_tarea4_mutacion_cuarta_puerta.py     2.6s
      vuelta195_tarea3g_mutacion_nomina_enchufada.py     2.6s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 617741f764f9, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 617741f764f9, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 11: 1
FIN (reloj de pared, UTC): 2026-09-07T14:22:16Z
DURACION DEL TRAMO (monotona, segundos): 18.4
DURACION DEL TRAMO (monotona, minutos): 0.3
```
