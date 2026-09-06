# REPORTE DE LA VUELTA 183 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta183_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA SI ES DE BATERIA, Y ESO MANDA SOBRE TODO LO DEMAS.**
> `AUDITOR.md` 6.1: la bateria corre CADA CINCO, en **VUELTA PROPIA**, y esa
> vuelta **no lleva trabajo de plan al lado**. **La 181 era la suya y se corto
> antes de lanzarla.** La decision del fundador del **5 sep 2026** (PREGUNTA 4 de
> `docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md`) la manda **por
> tramos resumibles**, y su lanzador,
> `scripts/loop/vuelta183_bateria_por_tramos.py`, esta escrito desde la 182 y sin
> correr. **La seccion 9 de este reporte lleva la bateria entera dentro, no un
> hueco: esta vez si es su vuelta.**
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y NO ES INERCIA: ESTA MEDIDO.** El
> regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas seguidas
> cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. El acta 182,
> punto 8, lo midio: **la 181 NO cerro el suyo** y **la 182 SI**, asi que la
> cuenta va por **UNA**. **Si la 183 cierra el suyo, seran dos seguidas y el tope
> vuelve a cinco en la 184.**
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee
> ningun par de los 543 ni se toca la cola de `docs/plan/08_VERIFICACION.md` (su
> TRAMO 1 es el par **2.464** y se relee cuando haya vuelta de trabajo, no en la
> de bateria); no se cablea el instrumento de vigencia de las ocho `A` rancias por
> `P.5`; no se toca el marcador, ni un veredicto, ni `dataset/`; y **no se poda la
> nomina de la bateria**, que es la opcion `c` que el fundador RECHAZO el 5 sep.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno, la 179 y la 180 lo repitieron y aqui
> vuelve a correr en su sitio. **Desde la 178, una columna de apertura medida al
> cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Las dos preguntas vuelven a coincidir en el numero, pero
> **no en el estado**: la 182 **cerro su reporte con `cerrar_reporte.py` y NO
> lo archivo en su misma vuelta**, cosa que el bloque de apertura de hoy midio
> (`docs/loop/SALIDA_V183_APERTURA.txt`, bloque H.4: `REPORTE_V182.md
> archivado: NO`). **Lo archiva el PASO 0 de este esqueleto, antes de escribir
> una sola linea encima**, y su salida se pega abajo con lo que salga.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta183_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 182: `0ef74748`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 182: LA APERTURA SELLADA CUMPLIO EN SU ESTRENO, Y EL VEREDICTO DE UNA LINEA SE CONTRADICE CON SU PROPIA SECCION 8.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V183_HEAD_APERTURA.txt`: `0ef74748`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `f3593671`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **182**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 183`. **Esta
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
| **TAREA 1** | LOS REGISTROS Y LA ESCALADA, BLOQUEANTE Y ANTES DE LA BATERIA. (a) El acta 182 entra en la serie de registros con el numero que devuelve `scripts/loop/serie_de_registros.py` y no tecleado, con sus adjudicaciones `5.D.1` a `5.D.7` y `7.1` a `7.5`, su caida propia del auditor y las dos del ejecutor, y su caso por mutacion. (b) LA DEUDA DE OCHO REGISTROS SE DOCUMENTA COMO SALTO Y NO SE RELLENA: una sola linea de constancia en la serie, en su sitio, con la cifra contada por el instrumento. (c) LA ESCALADA DE `AUDITOR.md` 1.2, que es la operacion de codigo de esta vuelta: `scripts/loop/cerrar_reporte.py` gana una funcion PURA con arnes propio que coteja los numerales del veredicto de una linea contra lo que el cuerpo permite contar (caidas propias `C.n` de la seccion 8 y filas de la tabla de tareas), lee los numerales TAMBIEN escritos con letra, y CAE EN ROJO sin escribir nada si no calzan. Con caso positivo POR MUTACION SOBRE VARIABLE COMPUTADA. (d) EL HUECO DE LA SECCION 9 TIENE QUE DECIR SI EL FICHERO NO EXISTE O SI MIDE CERO, que hoy los confunde en un `max(tam, 0)`, sin tocar las tres piezas que el hueco ya exige. (e) LA RELECTURA AL DOBLE del tramo de la ciega: los 30 puestos de la seccion 9 del acta 182 y sus 30 vecinos deterministas, mecanica y con la vara, sin volver a decidir la clase de ningun par | **CERRADA** | `docs/loop/SALIDA_V183_T1A_REGISTRO_R44.txt`, `docs/loop/SALIDA_V183_T1A_MUTACION_REGISTRO.txt`, `docs/loop/SALIDA_V183_T1C_MUTACION_VEREDICTO.txt`, `docs/loop/SALIDA_V183_T1E_RELECTURA_AL_DOBLE.txt`, `docs/PENDIENTES.md` (`R.44`) y `scripts/loop/cerrar_reporte.py` |
| **TAREA 2** | LA BATERIA DE MUTACIONES, ENTERA Y POR TRAMOS. `scripts/loop/vuelta183_bateria_por_tramos.py`, escrito y medido en la 182 y sin correr. Cada tramo se commitea CON SU SALIDA SELLADA al terminar, antes de seguir; una vuelta cortada RETOMA EN EL TRAMO SIGUIENTE y cual toca lo dice `--siguiente`; la bateria se declara corrida cuando LOS NUEVE tienen salida sellada DEL MISMO CALIBRE; una salida sellada que mide CERO BYTES no cuenta como hecha; la doble corrida y todas las demas guardas siguen enteras, y lo unico que cambio es la cadencia. El reloj de cada tramo se mide al cerrarlo y se publica medido: la estimacion del `--plan` es estimacion y se dice como tal. Si un arnes cae en rojo, el ejecutor se detiene ahi y lo trae con su salida entera | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | LOS REGISTROS Y LA CORRECCION DE LA ATRIBUCION, BLOQUEANTE Y ANTES DE TOCAR LA BATERIA. **Es la TAREA 1 del encargo de la CONTINUACION de esta vuelta**, y entra como TAREA 3 porque la tabla ya tiene una TAREA 1 cerrada y una TAREA 2 abierta que es la bateria. (a) El acta 183 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, con sus siete adjudicaciones `5.1` a `5.7`, la caida del ejecutor `E.1`, las CERO caidas propias del auditor y su caso por mutacion. (b) LA CORRECCION DEL `E.1`, que es la operacion de codigo: el numero de vuelta y el nombre del lanzador de la bateria se COMPUTAN de `os.path.basename` y no se clavan, con caso positivo por mutacion sobre variable computada que CAE si alguien vuelve a clavarlos. (c) Los tramos 1 y 2 se vuelven a correr despues de (b), con el coste medido al lado. (d) Las tres rutas de la celda de prueba de la TAREA 1 se escriben enteras. (e) `scripts/loop/_v183_tallar_cierre.py` se commitea y no se borra. (f) La relectura al doble del tramo de la ciega del acta 183, cotejando su `sha256` contra el sello antes de leer un solo puesto | **CERRADA** | `docs/loop/SALIDA_V183_T1A_REGISTRO_R45.txt`, `docs/loop/SALIDA_V183_T1A_MUTACION_REGISTRO_183.txt`, `docs/loop/SALIDA_V183_T1B_MUTACION_ATRIBUCION.txt`, `docs/loop/SALIDA_V183_T1F_RELECTURA_AL_DOBLE.txt`, `docs/loop/SALIDA_V183_T1B_COTEJO_CLON_APERTURA.txt`, `docs/loop/SALIDA_V183_T1F_COTEJO_CLON.txt`, `docs/PENDIENTES.md` (`R.45`) y `scripts/loop/vuelta183_bateria_por_tramos.py` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS Y LA ESCALADA

**1.a. EL ACTA 182 ENTERA, REGISTRADA COMO `R.44`.** Instrumento
`scripts/loop/vuelta183_tarea1a_registrar_acta182.py`, salida
`docs/loop/SALIDA_V183_T1A_REGISTRO_R44.txt` (**4.498 bytes en disco y 4.498
bytes normalizados a LF**). El numero lo devolvio
`serie_de_registros.siguiente_libre()` y **no se tecleo**: la serie recomputada
de sus dos sedes daba **35 entradas, 0 colisiones y 0 huecos**, y el siguiente
libre **R.44**. Tras escribir: **36 entradas, 0 colisiones y 0 huecos**.
`docs/PENDIENTES.md` pasa de **850.711 bytes** a **862.331 bytes en disco y
862.331 bytes normalizados a LF**.

**LOS TRES NUMERALES DEL TITULO SE CONTARON DEL ACTA ACOTADA** (lineas 63250 a
63681, 432 lineas): **12 adjudicaciones** (7 de la seccion 5, `5.D.1` a `5.D.7`,
lineas 63456, 63465, 63472, 63480, 63489, 63495 y 63503; y 5 de la seccion 7,
`7.1` a `7.5`, lineas 63563, 63578, 63583, 63588 y 63607), **1 caida propia del
auditor** (`C.1`, linea 63294) y **2 caidas del ejecutor** (`E.1` en la 63510 y
`E.2` en la 63532).

**HIZO FALTA CODIGO PROPIO, Y ESTA MEDIDO EN VEZ DE SUPUESTO.** El registrador de
la 182 barre un solo prefijo del tipo `**7.n `: corrido sobre esta acta da **5** y
**dejaria las 7 de la seccion 5 fuera**, porque el acta las escribe como
``**`D.1`,``. Y el patron de caida del auditor de la 182 (``**`C.n`.`` al
principio de linea) **cuenta CERO** sobre el acta 182, que escribe la suya dentro
de una frase en negrita, *"**MI CAIDA PROPIA, `C.1`, Y VA IGUAL AUNQUE EL SELLO
AGUANTARA.**"*; el patron mas viejo (`**CAIDA n.`) tambien cuenta **CERO**. **Se
anaden patrones, no se ensancha el viejo hasta que trague**, y las dos cifras de
cero van publicadas al lado de la buena.

**CASO POSITIVO POR MUTACION VERDE**, salida
`docs/loop/SALIDA_V183_T1A_MUTACION_REGISTRO.txt` (**2.310 bytes en disco y 2.310
bytes normalizados a LF**), **0 fallos**: 4 actas fabricadas con cifras distintas,
los contadores calzan con las cuatro; el esperado mutado **CAE**; el patron de
caida del acta 181 sobre un acta en forma 182 da **CERO**; el prefijo `6.` sobre
un acta que numera `7.n` da **CERO**; y `actas_sin_entrada()`, que es pura, se
tumba sobre una serie fabricada y devuelve el salto y **sus dos extremos**
computados.

**1.b. LA DEUDA DE OCHO REGISTROS, DOCUMENTADA COMO SALTO Y NO RELLENADA.** Va
dentro del propio `R.44`, en una **sola linea de constancia**, que es lo que la
adjudicacion `7.4` del acta 182 encarga con estas palabras: *"la deuda se
documenta como salto, no se inventa"*. Contado por el instrumento y no tecleado
(seccion G de su salida): **8 actas sin entrada propia, las 173 a 180**, con sus
dos extremos **`R.42`, que cubre el acta 172**, y **`R.43`, que cubre el acta
181**. **No se escriben ocho registros de memoria.**

**1.c. LA ESCALADA DE `AUDITOR.md` 1.2, QUE ES LA OPERACION DE CODIGO DE ESTA
VUELTA.** `scripts/loop/cerrar_reporte.py` (**54.697 bytes en disco y 54.697
bytes normalizados a LF**) gana su **septima comprobacion**, cuatro funciones
**PURAS** y un carril nuevo en `main()`:

- `numerales_del_veredicto()`, que lee los numerales **en cifra y en letra**
  (`cero` a `quince`), que es como el veredicto de una linea los escribe.
- `caidas_propias_del_cuerpo()`, que cuenta las cabeceras `C.n` **de la seccion 8
  y solo de ahi**: un reporte cita `C.n` ajenas en su prosa y contarlas seria
  fabricar un rojo.
- `tareas_de_la_tabla()`, que cuenta las filas entre las dos marcas de la tabla,
  reconociendo una fila por llevar `TAREA <numero>` dentro y no por su posicion.
- `numerales_del_veredicto_que_no_calzan()`, que las junta y devuelve los motivos.

**SI UN NUMERAL NO CALZA, EL CIERRE CAE EN ROJO Y NO ESCRIBE NADA:** el carril
`B.1)` corre **antes** del bloque que escribe, sobre `texto + cuerpo`, que son las
dos mitades del reporte (la tabla vive en el esqueleto, la seccion 8 en el
borrador del cierre). **Y cae tambien si el veredicto publica una cifra que el
cuerpo no permite contar**, porque una cifra sin fichero que la sostenga no cierra
un reporte.

**EL CASO ROJO ES REAL Y NO FABRICADO, Y SE PROBO POR MUTACION.** Arnes
`scripts/loop/vuelta183_tarea1c_mutacion_veredicto.py`, salida
`docs/loop/SALIDA_V183_T1C_MUTACION_VEREDICTO.txt` (**7.681 bytes en disco y
7.681 bytes normalizados a LF**), **0 fallos**. El veredicto de la 182 se lee de
`docs/loop/reportes/REPORTE_V182.md:46` y no se teclea; sus contadores, corridos
sobre ese mismo fichero, dan **7 caidas propias** (`C.1` a `C.7`, lineas 509, 518,
524, 531, 538, 545 y 549) y **5 filas de tarea**. La guarda lee `'CINCO'` como 5
tareas y `'SEIS'` como 6 caidas, y **CAE con 1 motivo**: *"el veredicto publica
'SEIS' (6 caidas) y el cuerpo, CONTADO, dice 7"*. El mismo veredicto con el
numeral bueno **PASA con 0 motivos**, y la palabra buena se computa de la cuenta,
no se teclea. **Todos los casos del arnes se corrieron con su esperado mutado y
CAEN**, que es lo unico que prueba que podian fallar.

**1.d. EL HUECO DE LA SECCION 9 YA DICE CUAL DE LOS DOS CASOS ES.** Adjudicacion
`7.1` del acta 182. **Lo que pasaba antes no se borra, se cuenta:** `main()` hacia
`tam = os.path.getsize(ruta_bat) if existe else -1` y la seccion publicaba
`max(tam, 0)`, o sea **el mismo cero en los dos casos**, y el arnes lo mide:
`max(-1, 0) = 0` y `max(0, 0) = 0`. Ahora lo arma `frase_del_caso_del_hueco()`,
**pura y con arnes propio**, que devuelve tres textos distintos: **EL FICHERO NO
EXISTE** (y dice que `getsize` *"no llego a correr sobre el"*), **EL FICHERO
EXISTE Y MIDE CERO** (y dice que *"el cero es una medicion, no el resultado de un
`max`"*) y el tercero para el fichero con cuerpo. **Las tres siguen trayendo su
cifra de bytes y ninguna deja una cifra sin su pareja**, comprobado en el mismo
arnes con `PATRON_BYTES` y con `cifras_sin_pareja()`: **las tres piezas que el
hueco ya exige quedan intactas.**

**LOS TRES ARNESES VIEJOS DEL CIERRE SIGUEN VERDES Y NO SE TOCARON:**
`vuelta172_tarea5_mutacion_cierre.py` **17 de 17**,
`vuelta173_tarea1b_mutacion_hueco.py` **24 de 24** y
`vuelta182_tarea1b_arnes_rama_seccion9.py` **0 fallos**.

**1.e. LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA.** Instrumento
`scripts/loop/vuelta183_tarea1e_relectura_al_doble.py`, salida
`docs/loop/SALIDA_V183_T1E_RELECTURA_AL_DOBLE.txt` (**12.375 bytes en disco y
12.375 bytes normalizados a LF**). **30 puestos del tramo + 30 vecinos
deterministas = 60**, solape entre tramo y vecinos **0**, solape con el tramo de
la 181 **0**. **60 releidos: 2 declaran diferenciador, 1 tiene LESION EXACTA (el
puesto 978) y 0 tienen un nodo muerto.** Reparto por clase de los 60: **A 16, B 1,
D 43**. Los seis puestos que el auditor discrepa (375, 393, 1280, 1815, 2416 y
2470) estan **los seis** dentro del universo releido. **Ninguna clase se vuelve a
decidir:** `vecinos()` se importa del instrumento de la 182 y la vara se importa
de `vuelta182_tarea3_diferenciador_movido.py`; lo que la vara no ve, la salida no
lo afirma.

> **CORRECCION DECLARADA, Y NO TAPA LO QUE CORRIGE.** El encargo dice que el tramo
> son *"los 30 puestos de la seccion 9 de mi acta 182"*. **Medido en la apertura,
> antes de escribir ninguna linea de la tarea** (bloque H.8 de
> `docs/loop/SALIDA_V183_APERTURA.txt`): la seccion 9 del acta 182 son las lineas
> **63644 a 63658** y es **LA METRICA DE CREDITO**, una tabla que dice *"puestos |
> 30 aislados, 30 limpios | 736"* **y no lista ningun puesto**; el parseo devolvio
> **CERO**. La ciega del acta 182 es su **seccion 4**, y ahi solo estan **los 6
> puestos que discrepan**. Los 30 viven en el fichero que el propio auditor sello,
> `docs/loop/_auditor_v183_ciega_blind.txt`, y el instrumento **lo coteja contra
> `SELLO_APERTURA_AUDITOR_V183.json` antes de leer un solo puesto**: **41.200
> bytes** declarados y **41.200 bytes** en disco, `sha256` `226f577c7f5a2885` en el
> sello y `226f577c7f5a2885` hoy. **Si no calzaran, no releeria nada.**

**Y UNA COSA QUE ESTA TAREA ENCONTRO Y NO ESTABA ENCARGADA, PORQUE HABRIA PUESTO
LA BATERIA ENTERA EN ROJO.** Al abrir la vuelta, **antes de tocar nada**, el
bloque H.9 de la apertura midio `arneses_que_faltan() HOY: ultima vuelta 180,
faltan 1`, y ese uno es **`vuelta182_tarea2_mutacion_apertura_auditor.py`**: la
vuelta 182 escribio ese arnes en su TAREA 2 y **no lo metio en la nomina**. Con el
fuera, **`hay_rojo_al_cierre()` habria cerrado en ROJO los nueve tramos** de esta
bateria, y un rojo que no senala ninguna guarda rota es justo lo que la `D.4` del
acta 182 llama *"entrenar a mirar los rojos con desgana"*. Entra por la regla de
siempre, que el acta 176 punto 7.2 fijo y la `D.4` del acta 182 reconfirmo: **un
arnes entra en la nomina, y puede entrar en su misma vuelta**. Su clasificacion
era **NO DECIDIBLE** porque trae las dos huellas; la guarda no adivina y pide que
el arnes lo declare, y se declaro **con la medicion delante**: su unica aparicion
de `REPORTE.md` fuera del docstring es **un dato dentro de una tabla de
escenarios** y el fichero fabrica todo lo suyo en un `mkdtemp`. Entra con el, por
la misma regla, **el arnes de la 1.c de esta vuelta**. **La nomina crece de 109 a
111 y no se poda nada.** Remedido despues: `arneses_que_faltan()` **0**,
`nomina_invisible_al_censo()` **0**, `guarda_del_sujeto_congelado()` **0**, y el
reparto sigue dando **NUEVE tramos** con **suma 111**.

### TAREA 3 (TAREA 1 DEL ENCARGO DE LA CONTINUACION). LOS REGISTROS Y LA CORRECCION DE LA ATRIBUCION

> **LA FILA ENTRA COMO TAREA 3 Y SE DICE POR QUE.** El encargo de la
> continuacion la llama TAREA 1, pero la tabla de este reporte YA tiene una
> TAREA 1 cerrada (la de la primera sesion) y una TAREA 2 abierta que es la
> misma bateria que la TAREA 2 de hoy. Renumerar la tabla o reusar la fila de la
> TAREA 1 seria pisar trabajo ya cerrado y ya auditado. La fila se abrio VACIA
> con `scripts/loop/_v183b_abrir_fila_tarea3.py` **antes** de anexar nada, que
> es lo que `EJECUTOR.md` 1 pide, y su salida cuenta **3 filas de tarea en la
> tabla**.

**3.a. EL ACTA 183 ENTERA, REGISTRADA COMO `R.45`.** Instrumento
`scripts/loop/vuelta183b_tarea1a_registrar_acta183.py`, salida
`docs/loop/SALIDA_V183_T1A_REGISTRO_R45.txt` (**3.487 bytes en disco y 3.487
bytes normalizados a LF, 68 lineas**). El numero lo devolvio
`serie_de_registros.siguiente_libre()` y **no se tecleo**: la serie recomputada
de sus dos sedes daba **36 entradas, 0 colisiones y 0 huecos**, y el siguiente
libre **R.45**. Tras escribir: **37 entradas, 0 colisiones y 0 huecos**, y el
siguiente libre pasa a **R.46**. `docs/PENDIENTES.md` pasa de **862.331 bytes** a
**871.284 bytes**. La entrada mide **8.952 bytes y 98 lineas**, se releyo del
disco byte a byte y trae **0 guiones largos o medios**.

**LOS TRES NUMERALES DEL TITULO SE CONTARON DEL ACTA ACOTADA** (lineas 63.682 a
64.048, 367 lineas): **7 adjudicaciones** (`5.1` a `5.7`, lineas 63883, 63924,
63933, 63944, 63956, 63964 y 63971), **0 caidas propias del auditor** y **1 caida
del ejecutor** (`E.1`, linea 63883).

**HIZO FALTA CODIGO PROPIO OTRA VEZ, Y ESTA MEDIDO EN VEZ DE SUPUESTO**, por tres
cosas distintas y las tres con su cifra de contraste al lado. **UNA:** el acta 182
numeraba `7.n` y **el acta 183 numera `5.n`**; corrido el prefijo `7.` de la
vuelta pasada sobre esta acta, da **0**, porque su seccion 7 es la metrica de
credito. **DOS:** el acta 182 escribia la caida del ejecutor como ``**`E.1`.`` al
principio de linea y **el acta 183 la escribe DENTRO DEL TITULO de su primera
adjudicacion**; el patron viejo, corrido sobre esta acta, cuenta **0**. **TRES, y
es la que importa:** las caidas propias del auditor son **CERO**, y un cero que
sale de un patron que no muerde no es evidencia de nada. El instrumento **exige
ademas que el acta lo declare con todas las letras** y publica la linea:
**63726**, *"NINGUNA CAIDA PROPIA ESTA VUELTA, Y DECLARO EL METODO QUE LA EVITO
PORQUE ESTUVE A UN PASO DE UNA"*. **Si el patron diera cero y el acta no lo
declarara, el instrumento haria PARADA en vez de escribir la entrada**, y ese
caso esta probado en el arnes.

**LA DEUDA DE LA SERIE SE REMIDE EN ESTA VUELTA Y NO SE HEREDA DEL `R.44`:** **8
actas sin entrada propia, las 173 a 180**, con sus dos extremos **`R.42`, que
cubre el acta 172**, y **`R.43`, que cubre el acta 181**. **Sigue documentada como
salto y sin rellenar.**

**CASO POSITIVO POR MUTACION VERDE**, salida
`docs/loop/SALIDA_V183_T1A_MUTACION_REGISTRO_183.txt` (**3.181 bytes en disco y
3.181 bytes normalizados a LF, 55 lineas**), **0 fallos**: 4 actas fabricadas con
cifras distintas y los contadores calzan con las cuatro; el esperado mutado
**CAE**; el patron de caida del ejecutor del acta 182 sobre un acta en forma 183
da **CERO**; el prefijo `7.` sobre un acta que numera `5.n` da **CERO**; el
instrumento **distingue el cero declarado del cero sin declarar** (1 linea de
declaracion contra 0); y el numeral **cero** entra en el titulo con su
concordancia y no esta clavado.

**3.b. LA CORRECCION DEL `E.1`, QUE ES LA OPERACION DE CODIGO DE ESTA VUELTA.**
Adjudicacion 5.1 del acta 183. **LO QUE PASABA ANTES NO SE BORRA, SE CUENTA, Y SE
CONTO ANTES DE TOCAR NADA:** el bloque **H.2** de
`docs/loop/SALIDA_V183B_APERTURA.txt` (**30.531 bytes, 474 lineas**) conto **3
lineas con `176` en cada una de las cuatro salidas selladas, 12 en total**, con
sus numeros de linea y su texto.

**LAS TRES ESPECIES DE MENCION, SEPARADAS, PORQUE NO TODAS SON FALSAS.** De las
tres de cada fichero: en las dos salidas de bateria, **dos son atribucion falsa**
(las lineas 1 y 2, *"BATERIA DE LA VUELTA 176"* y *"lanzada por
scripts/loop/vuelta176_bateria_por_tramos.py"*) y **una es CITA HISTORICA
legitima** (la linea 21, *"EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c)"*, que
nombra de donde salio la regla y **vive en `verificar_mutaciones_viejas.py:1872`,
que no es el lanzador**). En las dos salidas de lanzador, **las tres son falsas**:
la linea 4 y los dos prefijos de `mkdtemp` que salen impresos en la ruta del
fichero temporal. **La cuenta de despues no baja a cero y se dice por que.**

**LA REPARACION NO ES TECLEAR UN 183 ENCIMA DEL 176.** Un 183 tecleado se hereda
igual que se heredo el 176. En `scripts/loop/vuelta183_bateria_por_tramos.py`
(**23.847 bytes en git al abrir, 539 lineas**), `LANZADOR` sale de
`os.path.basename(os.path.abspath(__file__))` y `VUELTA` de un `re.match` sobre
ese nombre, **y el modulo se niega a cargarse si el nombre no dice su vuelta**. De
ahi salen ahora, por **cuatro funciones PURAS** (`titulo_de_corrida`,
`linea_de_lanzador`, `titulo_de_composicion`, `linea_de_composicion`) y tres de
nombre (`nombre_tramo`, `nombre_transcripcion`, `nombre_de_la_compuesta`): las dos
primeras lineas de cada salida sellada (lineas 217 y 218 del encargo), la cabecera
de la composicion (359 y 360), la linea del titulo del tramo (181), **los dos
prefijos de `mkdtemp` que el encargo no nombraba** (198 y 516) y las dos rutas que
`--siguiente` y `--componer` imprimen. **El numero de tramos tampoco se teclea:
sale de `len(tramos)`.**

**Y EL GUARDA, QUE ES LA MITAD QUE IMPIDE QUE VUELVA A PASAR:**
`literales_de_vuelta_clavados()`, **pura**, corre en `main()` **sobre el fuente de
su propio modulo** y **el lanzador NO ARRANCA** si encuentra uno. Las citas
historicas se eximen **NOMBRANDOLAS** con la marca `CITA HISTORICA`, no
ensanchando el patron. Corrido hoy sobre el fuente real: **0 literales clavados**,
y esa linea sale impresa en la transcripcion sellada de cada tramo.

**EL CASO POSITIVO ES POR MUTACION SOBRE VARIABLE COMPUTADA, QUE ES LO QUE EL
ENCARGO PIDE.** Arnes `scripts/loop/vuelta183_tarea1b_mutacion_atribucion.py`,
salida `docs/loop/SALIDA_V183_T1B_MUTACION_ATRIBUCION.txt` (**6.782 bytes en disco
y 6.782 bytes normalizados a LF, 116 lineas**), **0 fallos**, y **las dos corridas
seguidas salen identicas byte a byte**, que es lo que la doble corrida de la
bateria va a exigirle. El clon: el fuente REAL copiado a un
`vuelta777_bateria_por_tramos.py`, importado, y **todo lo que ese clon sellaria
dice 777**. La mutacion: el mismo clon con `VUELTA` clavado a mano, y **el arnes
CAE en los tres casos** (no computa su numero, sella con el numero de otra vuelta
y su primera linea miente). Y el remate: **el clon con un literal clavado en un
`print` corrido como PROCESO devuelve exitcode 1** y dice en rojo cual linea lo
clava, contra **exitcode 0** del clon sano.

**EL ARNES TUMBO AL GUARDA DOS VECES ANTES DE QUE NADIE LO DIERA POR BUENO, Y ESO
NO SE ESCONDE.** La primera version del patron pedia `V` mayuscula sin separador,
y el arnes la caza con **dos casos que el defecto REAL de esta vuelta traia**: el
prefijo `v176_tramo` de los `mkdtemp`, que va en minuscula, y la frase *"de la
vuelta 176"*, que lleva espacio. **Las dos salieron impresas en las salidas
selladas y el patron no las veia.** Se ensancho **una vez**, con la medicion
delante y escrita en el comentario del propio patron.

**LA NOMINA CRECE DE 111 A 112 Y NO SE PODA NADA.** El arnes entra por la regla
del acta 176 punto 7.2, que la `D.4` del acta 182 reconfirmo y la `5.4` del acta
183 volvio a conceder. **Medido antes de anadirlo:** `arneses_que_faltan()` daba
**ultima vuelta 183, faltan 1**, y ese uno era este arnes; **con el fuera,
`hay_rojo_al_cierre()` habria cerrado en ROJO los siete tramos que quedan**.
Remedido despues: `arneses_que_faltan()` **0**, `nomina_invisible_al_censo()`
**0**, `guarda_del_sujeto_congelado()` **0**, y el reparto sigue dando **NUEVE
tramos** con **suma 112** y tamanos **13, 13, 13, 13, 13, 13, 13, 13, 8**. **Los
ocho primeros tramos no se mueven: el que crece es el noveno**, de 7 a 8 entradas.

**3.c. LOS TRAMOS 1 Y 2 SE VUELVEN A CORRER, Y VA EN LA TAREA 2.** El regimen
`6.1` pide que los nueve tengan salida sellada **DEL MISMO CALIBRE**, y dos
salidas que se atribuyen otra vuelta no son del mismo calibre que siete que se
atribuyen bien. **El coste esta medido y no estimado:** los dos tramos costaron
**2,1 y 5,6 minutos** en su primera corrida (commits `ede210b2` y `34f7ef7f`),
o sea **7,7 minutos**, sobre una bateria que el `--plan` de hoy estima entre
**36,6 y 47,7 minutos** para la nomina entera. **No contradice "lo corrido queda
corrido":** esa regla protege el trabajo cuando la vuelta se corta, no una salida
sellada que dice de que vuelta es y se equivoca.

**3.d. LAS RUTAS DE LA CELDA DE PRUEBA DE LA TAREA 1, ESCRITAS ENTERAS.**
Adjudicacion 5.2 del acta 183, que las adjudica **a favor del ejecutor** y aun asi
encarga escribirlas enteras, por el motivo que ella misma da: una ruta que hay que
reconstruir mentalmente no se puede cotejar pegandola en un comando. **El encargo
nombra tres y se corrigen CUATRO:** la primera, `SALIDA_V183_T1A_REGISTRO_R44.txt`,
tampoco llevaba su carpeta. Las cuatro se comprobaron una a una antes de
escribirlas, que es lo que la regla del 5 sep manda: **4.498, 2.310, 7.681 y
12.375 bytes**, ninguna ausente y ninguna en cero.

**3.e. EL TALLADOR DEL CIERRE ENTRA A GIT Y NO SE BORRA.** Adjudicacion 5.6.
`scripts/loop/_v183_tallar_cierre.py`, **18.855 bytes**, medido en el bloque F del
bloque de apertura cuando todavia estaba sin seguir, commiteado con el bloque de
apertura en `da1ad513`.

**3.f. LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 183.** Instrumento
`scripts/loop/vuelta183b_tarea1f_relectura_al_doble.py`, clon declarado del de la
TAREA 1.e, salida `docs/loop/SALIDA_V183_T1F_RELECTURA_AL_DOBLE.txt` (**12.050
bytes en disco y 12.050 bytes normalizados a LF, 144 lineas**). **EL COTEJO VA
ANTES DE LEER UN SOLO PUESTO Y CALZA:** `SELLO_APERTURA_AUDITOR_V184.json` (658
bytes) declara **43.593 bytes** y `sha256`
`217077af6ea96a1862a692f81abae6393bd87b7587e14d8bd6e21003408ba9f9`, y el fichero
de hoy mide **43.593 bytes** con **ese mismo `sha256`**. **Si no calzaran, no se
releeria nada y la salida lo diria.**

**30 puestos del tramo + 30 vecinos deterministas = 60**, solape entre tramo y
vecinos **0**, solape con la ciega inmediatamente anterior
(`_auditor_v183_ciega_blind.txt`, 30 puestos) **0**. **60 releidos: 4 declaran
diferenciador, 0 tienen LESION EXACTA y 0 tienen un nodo muerto.** Reparto por
clase de los 60: **A 7, B 1, D 52**. El puesto **660**, que es la unica
discrepancia del auditor, esta **dentro** del universo releido: clase **B**,
declara diferenciador **SI**, lesion **no**. **Ninguna clase se vuelve a decidir:**
`vecinos()` se importa del instrumento de la 182 y la vara de
`vuelta182_tarea3_diferenciador_movido.py`; lo que la vara no ve, la salida no lo
afirma.

> **UNA COSA QUE EL ENCARGO NO DICE Y SE DECLARA EN VEZ DE CALLARLA.** El encargo
> manda leer los 30 de `_auditor_v184_ciega_blind.txt`, y ahi estan; pero la
> **seccion 4 del acta 183**, que es la de la ciega, **no lista ninguno de los
> 30** (parseada, devuelve **0**): publica el reparto por clase y la unica
> discrepancia. Se dice para que nadie busque los 30 en el acta y crea que
> faltan.

**LOS DOS COTEJOS DE CLON DECLARADO, PEGADOS CON LO QUE SALGA Y SIN PROMETER QUE
SALDRIAN VACIOS.** El bloque de apertura de esta continuacion contra el de la
primera sesion (`docs/loop/SALIDA_V183_T1B_COTEJO_CLON_APERTURA.txt`, **37.617
bytes en disco y 37.004 normalizados a LF**): **DIFIERE en los cuatro veredictos**,
con **5.535 nodos de arbol contra 4.852** y **42 tipos de nodo que no empatan**. El
instrumento de la relectura contra el de la TAREA 1.e
(`docs/loop/SALIDA_V183_T1F_COTEJO_CLON.txt`, **7.878 bytes en disco y 7.755
normalizados a LF**): **DIFIERE en los cuatro**, con **2.089 nodos contra 2.104** y
**17 tipos que no empatan**. Los dos docstrings anunciaron que no saldrian
identicos y ninguno de los dos lo prometio.

<!-- FIN ANEXO DE TAREAS -->
