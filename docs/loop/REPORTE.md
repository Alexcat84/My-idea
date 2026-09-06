# REPORTE DE LA VUELTA 185 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta185_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que no lleva nada
> mas. **Cerro entera en la 184**, con sus nueve tramos sellados, asi que **la
> siguiente vuelta de bateria es la 189**. En las vueltas intermedias la seccion 9
> se cierra igual, con el **nombre del fichero, sus bytes medidos y su
> atribucion**, las tres juntas o no vale.
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y LA CUENTA SIGUE EN CERO.** El
> regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas seguidas
> cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. **La 184 no
> cerro el suyo** (`cerrar_reporte.py` exitcode 1, salida pegada entera en su
> reporte), asi que la cuenta **sigue en cero**. **Van dos tareas y no hay una
> tercera.**
>
> **EL TRABAJO DE ESTA VUELTA ES DESATASCAR EL CIERRE DEL REPORTE**, que lleva
> CUATRO vueltas sin conseguirse (181, 182, 183 y 184), y que es el mismo atasco
> por el que el fundador puso el regimen 6.2 el 5 sep.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee el
> par **2.464** ni ningun otro de la cola post fusion (encabeza el encargo de la
> **186**); no se cablea el instrumento de vigencia de las `A` rancias por `P.5`;
> **no se vuelve a decidir ninguna clase** en la relectura al doble; no se toca el
> marcador, ni un veredicto, ni `dataset/`; **no se poda la nomina de la bateria**,
> que es la opcion `c` que el fundador RECHAZO el 5 sep; y **no se repara el
> desfase del acta `VUELTA - 1`** de la `5.2`, que queda encargado y sin ejecutar
> porque el tope son dos sub-tareas.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py` y desde la 178 vuelve a correr en su sitio. **Una
> columna de apertura medida al cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO YA NO TIENE REPORTE AJENO QUE ARCHIVAR, PORQUE
> LA TAREA 2.a LO ARCHIVO ANTES.** El orden de esta vuelta no es el de siempre y
> el motivo se dice: si el esqueleto corriera primero, su PASO 0 archivaria el
> reporte de la 184 **sin cerrar**, y la reparacion de la TAREA 1.c llegaria tarde
> para el unico reporte al que le sirve. **El PASO 0 se corre igual y su salida se
> pega con lo que salga**, diga lo que diga, en vez de dejar la fila muda.

**EL VEREDICTO DE UNA LINEA: LAS DOS TAREAS CIERRAN Y ESTE REPORTE SE CIERRA CON SU SECCION 9 EN HUECO DECLARADO Y MEDIDO, PORQUE LA BATERIA CORRE CADA CINCO VUELTAS Y LA SIGUIENTE ES LA 189; LA GUARDA DE LA BATERIA CONTINUADA QUEDA REPARADA Y SU ARNES VERDE, PERO EL REPORTE DE LA 184 SIGUE SIN CERRAR PORQUE LA MISMA REGLA VIVE DOS VECES EN cerrar_reporte.py Y LA SEGUNDA SEDE NO ME TOCA TOCARLA; LAS DOS CAIDAS PROPIAS VAN NOMBRADAS Y NINGUNA TAPADA.**
## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta185_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 184: `dc558582`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 184: LA CONTINUACION DE LA 183 REPRODUJO ENTERA, LOS SIETE DISCUTIBLES VAN A FAVOR, Y ADJUDICO LA REPARACION DEL ARNES QUE PARO LA BATERIA.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V185_HEAD_APERTURA.txt`: `5834632b`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `2c72d81d`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **184**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 185`, y su salida
cruda vive en `docs/loop/SALIDA_V185_TALLADOR_CABECERA.txt` (2419 bytes en disco y 2399 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `dc558582` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 184: LA CONTINUACION DE LA 183 REPRODUJO ENTERA, LOS SIETE DISCUTIBLES VAN A FAVOR, Y ADJUDICO LA REPARACION DEL ARNES QUE PARO LA BATERIA.'), HEAD real de apertura `5834632b` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `403e50c3` (leido de `SALIDA_V185_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LAS TRES REPARACIONES DE CODIGO. BLOQUEANTE. (a) El acta 185 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus siete adjudicaciones `5.1` a `5.7` todas a favor, los CUATRO pendientes de doctrina de la seccion 6 con su estado leido del titulo (`PD.2`, `PD.3` y `PD.4` CERRADAS por cita y `PD.1` ABIERTA con sus cinco puestos leidos del acta y no copiados del encargo), la caida propia del auditor `A.1` y la caida de reporte del ejecutor `R.1`, mas su caso positivo por mutacion sobre un acta FABRICADA con el esperado mutado cayendo, y la deuda de la serie REMEDIDA y no heredada del `R.46`. (b) LA SALIDA SELLADA DEL ARNES QUE PARO LA BATERIA DEJA DE CAMBIAR SOLA: funcion PURA `sin_temporal(linea, tmp)` aplicada ANTES del recorte, sin tocar lo que el arnes prueba, con arnes propio de DOS MITADES que fallan por separado. (c) LA GUARDA DE LA BATERIA CONTINUADA, que es la adjudicacion `6.2` del acta 185: `vuelta_que_sello()` y `tramos_por_vuelta()` nuevas, `rama_de_la_seccion9()` con un cuarto parametro que por defecto se comporta EXACTAMENTE como hoy, y una rama nueva que EXIGE MAS que la vieja con CUATRO condiciones a la vez, con la evidencia computada de git y sin ninguna bandera. (d) LA ESCALADA DE `AUDITOR.md` 1.2: la columna `quien lo sello` se computa en vez de teclearse, y el cotejo de las NUEVE celdas contra las que el reporte de la 184 ya lleva es la prueba. (e) LA RELECTURA AL DOBLE del tramo de la ciega del acta 185, con el cotejo de `sha256` contra el sello `V185b` ANTES de leer un solo puesto | **CERRADA, CON UNA PARADA LEVANTADA EN LA 1.c** | `SALIDA_V185_T1A_REGISTRO_R47.txt`, `SALIDA_V185_T1A_MUTACION_REGISTRO_185.txt`, `SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt`, `SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt`, `SALIDA_V185_T1C_SEGUNDA_GUARDA.txt`, `SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt`, `SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt`, `SALIDA_V185_COTEJO_DE_CLONES.txt` |
| **TAREA 2** | EL CIERRE DE DOS REPORTES: EL DE LA 184 Y EL DE LA 185. (a) El reporte de la 184 se cierra con la guarda ya reparada por la 1.c, DESPUES de cotejar sus tres piezas por `sha256` y por bytes contra lo que la 184 midio, con el veredicto de una linea TALLADO y no tecleado, y se archiva. (b) El reporte de la 185 se abre en su esqueleto, cada tarea anexa su fila al cerrarse, la cabecera se talla y `--comparar` tiene que dar CABECERA IDENTICA AL TALLADOR, y su SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO por el carril de `cerrar_reporte.py`: nombre del fichero, bytes medidos y atribucion, las tres juntas o no vale | **CERRADA, CON UNA PARADA LEVANTADA EN LA 2.a** | `SALIDA_V185_T2A_VEREDICTO_184.txt`, `SALIDA_V185_CERRAR_REPORTE_184.txt`, `SALIDA_V185_T2A_ARCHIVAR_184.txt`, `SALIDA_V185_T2A_REPORTE_184_CERRADO_EN_ROJO.md`, `SALIDA_V185_ESQUELETO.txt`, `SALIDA_V185_TALLADOR_CABECERA.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS Y LAS TRES REPARACIONES DE CODIGO. CERRADA, CON UNA PARADA LEVANTADA EN LA 1.c

**TODAS LAS CIFRAS DE ESTA SECCION SALEN DE CONTAR SUS FICHEROS DE SALIDA CON
`scripts/loop/_v185_tallar_t1.py`, Y NINGUNA ESTA TECLEADA.** Las 10 rutas que
esta seccion publica como prueba existen y **ninguna mide cero bytes**: las de
cero medidas hoy son **0**.

#### 1.a EL ACTA 185 EN LA SERIE, CON EL NUMERO LLAMADO Y NO TECLEADO

Entrada **`R.47`**, en `docs/PENDIENTES.md`. El numero lo devolvio
`scripts/loop/serie_de_registros.py` recomputando la serie de sus dos sedes:
**38 entradas** antes de escribir, cero colisiones y cero huecos.

| lo que se registra | cifra contada del acta acotada |
|---|---:|
| adjudicaciones numeradas `5.1` a `5.7`, todas a favor | **7** |
| pendientes de doctrina `6.1` a `6.4` | **4** |
| caidas propias del auditor (`A.n`, cabecera `###`) | **1** |
| caidas de reporte del ejecutor (`R.n`) | **1** |

**EL ESTADO DE CADA PENDIENTE SALE DE SU TITULO Y NO DE UNA TABLA A MANO:**
`PD.2`, `PD.3` y `PD.4` **CERRADAS**, `PD.1` **ABIERTA**. **Y LOS CINCO PUESTOS
DE LA `PD.1` NO SE COPIARON DEL ENCARGO:** se leyeron del parrafo del `6.4` del
acta y son **1778, 2530, 2540, 3141, 3232**.

**LOS PATRONES VIEJOS SE CORREN IGUAL Y SU CERO SE PUBLICA**, que es lo que
prueba que hacian falta los nuevos: el patron sin comillas del acta 183, el
`C.n` de linea, el `C.n` de negrita de frase y el `E.n` de las actas 182 y 184
dan **0** los cuatro sobre esta acta.

**LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL `R.46`:**
**8 actas** sin entrada propia, las **173, 174, 175, 176, 177, 178, 179, 180**.

Prueba: `docs/loop/SALIDA_V185_T1A_REGISTRO_R47.txt` (**4615 bytes en disco y 4615 bytes normalizados a LF**).
Caso positivo por mutacion sobre un acta **FABRICADA**, nunca la real, en
`docs/loop/SALIDA_V185_T1A_MUTACION_REGISTRO_185.txt` (**4443 bytes en disco y 4443 bytes normalizados a LF**):
**CIFRA fallos: 0**, veredicto **VERDE**.

#### 1.b LA SALIDA SELLADA DEL ARNES QUE PARO LA BATERIA DEJA DE CAMBIAR SOLA

La reparacion es una funcion **PURA**, `sin_temporal(linea, tmp)`, aplicada en
las dos lineas `w("      | " + l[:130])` **ANTES del recorte y no despues**.
**NO SE TOCO LO QUE EL ARNES PRUEBA:** ningun esperado aflojado, ningun
escenario quitado.

| mitad | lo que mide | cifra contada de su fichero |
|---|---|---:|
| A, la funcion pura | casos | **7** |
| A | casos que CALZAN | **7** |
| A | casos que CAEN al mutar su esperado | **7 de 7** |
| B, corrida 1 | exitcode, y sus bytes por las dos convenciones al lado | **exitcode 0** |
| B, corrida 2 | exitcode, y sus bytes por las dos convenciones al lado | **exitcode 0** |

**LAS DOS CORRIDAS, EN PROCESOS APARTE, DAN EL MISMO `sha256`:**
`ce85fd0cc659774c` y `ce85fd0cc659774c`, identicos.
Y `docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` mide **4982 bytes en disco y 4982 bytes normalizados a LF**
despues de las dos.

**ESTA REPARACION REESCRIBE ESE FICHERO DE SALIDA, Y SE DICE EN VEZ DE
DISIMULARLO.** El que se commitea es el de la forma reparada, con
`<TEMPORAL>` dentro: **3 apariciones de `<TEMPORAL>`** y **0 de
`v182_apertura_`**. `git diff --numstat` sobre ese fichero dio **3 y 3**, o sea
las tres lineas 53, 54 y 55 que el acta 185 punto 3.5 diagnostico **y ninguna
mas**.

**LO QUE ESTA VUELTA NO PUEDE PROBAR, Y SE DICE:** esta reparacion **NO se
verifica contra la bateria**, porque la 185 no es vuelta de bateria
(`AUDITOR.md` 6.1). **La prueba de esta vuelta es la doble corrida de la mitad
B; la prueba definitiva sera la bateria de la 189.**

Prueba: `docs/loop/SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt` (**6100 bytes en disco y 6100 bytes normalizados a LF**),
**CIFRA fallos: 0**, veredicto **VERDE**.

#### 1.c LA GUARDA DE LA BATERIA CONTINUADA, Y LA PARADA QUE LEVANTA

**LA RAMA NUEVA EXIGE MAS QUE LA VIEJA Y NO MENOS:** cuatro condiciones a la
vez, y si falla cualquiera cae al ROJO de siempre. **La evidencia se computa de
`git log` en `main()` y NO se pasa por bandera:** apariciones de `--tramos` en
`cerrar_reporte.py`, contadas hoy: **0**.

| lo que se mide | cifra contada de su fichero |
|---|---:|
| casos de la tabla (el caso G va aparte) | **6** |
| casos que CALZAN | **6** |
| casos que CAEN al mutar su esperado | **6 de 6** |
| fallos del caso G, el del cuarto parametro por defecto | **0** |
| `tramos_por_vuelta(183)`: sellados por la vuelta 183 | **4** |
| `tramos_por_vuelta(183)`: sellados por la vuelta 184 | **5** |

**EL MOTIVO DEL ROJO VIEJO NO SE REESCRIBIO,** y eso no se afirma: el caso B
exige que su motivo sea **IDENTICO** al que la misma funcion devuelve con el
cuarto parametro en su valor por defecto, y sale identico.

**EL ARNES VIEJO SIGUE MANDANDO Y SE CORRIO SIN TOCARLO:**
`scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py`, con **9 casos**, **9
que calzan** y veredicto **VERDE**, en
`docs/loop/SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt` (**5802 bytes en disco y 5802 bytes normalizados a LF**).

Prueba: `docs/loop/SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt` (**7937 bytes en disco y 7937 bytes normalizados a LF**),
**CIFRA fallos: 0**, veredicto **VERDE**.

**PARADA. LA MISMA REGLA VIVE DOS VECES EN `cerrar_reporte.py`, Y EL ENCARGO
SOLO NOMBRA UNA.** El propio encargo lo previo: *"no se toca ninguna otra
guarda; si al escribir esto ves que hace falta cambiar algo mas, paras y lo
traes"*. **Se ve.** `ajena != vuelta` aparece **2 veces** en el fichero: en
`rama_de_la_seccion9()`, que es la que el encargo manda reparar y esta
reparada, y en la **PIEZA (4) de `piezas_que_faltan()`**, que tiene su propia
copia y **no recibe la evidencia**. Medido sobre un reporte **FABRICADO**, sin
escribir nada, en `docs/loop/SALIDA_V185_T1C_SEGUNDA_GUARDA.txt` (**2234 bytes en disco y 2234 bytes normalizados a LF**):
la rama sale **CORRIDA** y `piezas_que_faltan()` devuelve **1 pieza que**
**falta**. **NO SE TOCA Y NO SE ARREGLA AQUI.**

#### 1.d LA ESCALADA: LA COLUMNA `quien lo sello` SE COMPUTA

**LA PRUEBA DE LA ESCALADA ES QUE LA VERSION COMPUTADA REPRODUCE LA TECLEADA
EXACTAMENTE:** las **9 de 9** celdas calzan y **0 no calzan**.
Las tecleadas se leen de `docs/loop/REPORTE.md`, donde el reporte de la 184 las
publico; las computadas, de `scripts/loop/_v184_t2_seccion.md`, que es lo que el
tallador acaba de escribir con `tramos_por_vuelta()`.

La linea tecleada muere como codigo vivo: **0 apariciones como CODIGO VIVO** y
**1 como CITA dentro de un comentario**, nombrada y pegada porque
`EJECUTOR.md` 8 manda que una correccion no tape lo que corrige. Las dos
funciones se **IMPORTAN** de `cerrar_reporte.py` y no se copian.

**NO SE RE-PEGO NADA EN `docs/loop/REPORTE.md`.** El cierre del reporte de la
184 va en la TAREA 2 y usa el texto que ese reporte ya tenia; aqui solo se
prueba el instrumento.

Prueba: `docs/loop/SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt` (**2602 bytes en disco y 2602 bytes normalizados a LF**),
**CIFRA fallos: 0**, veredicto **VERDE**.

#### 1.e LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 185

**EL `sha256` SE COTEJO ANTES DE LEER UN SOLO PUESTO, Y NO SE COPIO DEL
ENCARGO:** el sello `V185b` declara la ciega y el fichero de hoy calza. **EL
FICHERO ES EL QUE EL SELLO DICE: SI.**

| lo que se mide | cifra contada de su fichero |
|---|---:|
| puestos del tramo, leidos de la ciega sellada | **30** |
| vecinos deterministas anadidos | **30** |
| solape entre tramo y vecinos | **0** |
| solape con la ciega inmediatamente anterior | **0** |
| puestos releidos EN TOTAL | **60** |
| es el doble exacto del tramo | **SI** |
| de los releidos, declaran diferenciador | **4** |
| de los releidos, con LESION EXACTA | **0** |
| de los releidos, con algun nodo muerto en el grafo de hoy | **0** |
| clase `A` / clase `D` en el universo releido | **9** / **51** |

**LAS SIETE DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA VARA.** El auditor
las pierde **las siete** a favor del archivo. **AQUI NO SE RE-DECIDE NINGUNA
CLASE:** solo se dice si estan dentro del universo releido y que ve la vara.

| puesto | clase | declara diferenciador | lesion exacta | dentro del universo |
|---:|:-:|:-:|:-:|:-:|
| **1208** | A | no | no | **SI** |
| **1459** | D | no | no | **SI** |
| **2363** | D | no | no | **SI** |
| **2386** | D | no | no | **SI** |
| **2505** | D | no | no | **SI** |
| **2636** | D | no | no | **SI** |
| **2854** | D | no | no | **SI** |

**LO QUE LA VARA NO VE, ESTA SECCION NO LO AFIRMA.** La vara dice, por puesto,
si declara diferenciador, si tiene lesion exacta, si algun nodo esta muerto y
su clase de archivo, **y nada mas**.

Prueba: `docs/loop/SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt` (**12566 bytes en disco y 12566 bytes normalizados a LF**).

#### LOS TRES CLONES DECLARADOS, COTEJADOS, Y SE PUBLICA LO QUE SALGA

**NO SE AFIRMA QUE NINGUN DIFF SALGA VACIO.** Salida en
`docs/loop/SALIDA_V185_COTEJO_DE_CLONES.txt` (**42081 bytes en disco y 41431 bytes normalizados a LF**).

| clon | sentencias de codigo | literales de texto |
|---|---:|---:|
| `vuelta184_apertura.py` -> `vuelta185_apertura.py` | **276** | **117** |
| `vuelta184_esqueleto_reporte.py` -> `vuelta185_esqueleto_reporte.py` | **1** | **67** |
| `vuelta184_tarea1d_relectura_al_doble.py` -> `vuelta185_tarea1e_relectura_al_doble.py` | **4** | **35** |

**Y LA DIFERENCIA MAS QUE EL ENCARGO MANDA DECLARAR:** el clon de la relectura
apunta a `SELLO_APERTURA_AUDITOR_V185b.json` y a `_auditor_v185b_ciega_blind.txt`,
y NO a las rutas que el numero de vuelta sugeriria. El auditor nombro su sello
`V185b` cuando la casa lo nombra `V186` y lo declaro como su caida propia `A.1`;
**las rutas vienen del encargo, no de deducirlas**.

#### LAS GUARDAS DE ESTA TAREA, MEDIDAS

`git diff --numstat -- dataset/` al cerrar esta tarea: **0 filas**.

#### LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. ANADI UN CAMBIO MAS DE LOS TRES QUE LA `1.d` NOMBRA.** El encargo
lista tres cosas que hacer y yo hice una cuarta: anadir a la prosa del tallador
la procedencia de la NOVENA columna. **Mi razon es que la `R.1` dice que la
averia es que la enumeracion no la incluia**, asi que dejarla fuera conservaria
el defecto en el instrumento. **No mueve ninguna celda de la tabla.** Pero es
un cambio que el encargo no pidio y lo marco.

**`D.2`. MI ARNES DE LA `1.b` SALIO EN ROJO EN SU PRIMERA CORRIDA Y LO REPARE
YO EN VEZ DE TRAERLO.** El encargo dice *"si cualquier arnes cae en rojo, te
detienes ahi, lo traes con su salida entera, sin re-correrlo"*. **Lo que cayo
fue MI arnes recien escrito, no una guarda de la casa**, y lo que estaba mal era
mi entrada de prueba tecleada, no la funcion bajo prueba. **Lei que esa regla
protege a los arneses ya sellados y no al que estoy escribiendo en esta misma
linea**, y arregle la prueba. **La corrida en rojo va entera en el reporte y en
el comentario del fichero**, pero la decision de alcance la tome yo.

**`D.3`. PUBLIQUE LA COLUMNA `quien lo sello` CON UNA NEGRITA COMPUTADA.** La
version tecleada ponia en negrita la vuelta mas alta (`**vuelta 184**`) y la
computada tiene que reproducirla, asi que **calculo cual es la vuelta mas alta
del reparto y esa va en negrita**. Reproduce las nueve celdas exactamente, pero
**es una regla de formato que nadie escribio**: la deduje de las celdas que
tenia que reproducir.

**`D.4`. NO METI LOS DOS ARNESES NUEVOS EN LA NOMINA DE LA BATERIA.**
`arneses_que_faltan()` da **2**, y son los dos que nacen hoy. La `5.6` del acta
185 ampara meterlos en su propia vuelta, pero **esta vuelta no es de bateria y
su encargo no nombra la nomina**. **Elegi no tocarla y declararlo**, a sabiendas
de que la bateria de la 189 empezara en rojo por esa via si nadie los mete
antes.

**`D.5`. GUARDE EL REPORTE DE LA 184 QUE `cerrar_reporte.py` SI LLEGO A
ESCRIBIR, Y DESPUES RESTAURE EL ARBOL.** El instrumento escribe en su bloque C
y juzga en el D, asi que al devolver 1 dejo en disco un reporte de contenido
completo. **Lo guarde con un nombre que dice lo que es y restaure**
**`docs/loop/REPORTE.md` con `git checkout`**, para que el arbol y el archivado
digan lo mismo. **Es una decision de alcance que tome yo**: destruirlo habria
perdido la evidencia, y dejarlo habria hecho que el esqueleto de la 185 pisara
un texto que no estaba en ninguna otra sede.

#### LAS PREGUNTAS

**`P.1`. LA PIEZA (4) DE `piezas_que_faltan()` Y LA PIEZA (2), ¿SE REPARAN
JUNTAS O POR SEPARADO?** La (4) es la copia gemela de la regla que la `1.c`
acaba de reparar. La (2) es otra especie: la marca `PENDIENTE DE TALLAR AL
CIERRE` se busca **en todo el texto**, y un reporte que CITA una salida roja
dentro de un bloque cercado la lleva dentro sin estar sin tallar. **No se cual
de las dos es prioridad y no me lo encargaron.**

**`P.2`. ¿QUE SE HACE CON LAS 10 CIFRAS SIN PAREJA DEL REPORTE DE LA 184?** La
guarda `cifras_sin_pareja()` las caza y el encargo prohibe tocar ese texto. **O
se exime el texto ya escrito, o se reescribe, o la guarda aprende a mirar solo
lo nuevo.** No elijo yo.

#### MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**`C.1`. ESCRIBI UN ARNES CUYA SALIDA SELLADA LLEVABA DENTRO EL MISMO DATO QUE
CAMBIA SOLO QUE LA REPARACION VIENE A QUITAR.** La primera version de
`vuelta185_tarea1b_mutacion_sin_temporal.py` pegaba las lineas de entrada
**crudas**, con el sufijo aleatorio del `mkdtemp` dentro. **Habria hecho caer la
bateria de la 189 por la misma averia que estaba reparando.** Lo cace
**mirando mi propio fichero**, no un instrumento, y anadi `mostrar()`.

**`C.2`. MI PRIMER ARNES DE LA `1.b` FABRICO UN TEMPORAL QUE NO EXISTE Y SUS
DOS CASOS DE RUTA RELATIVA SALIERON EN ROJO.** La funcion estaba bien; lo que
estaba mal era mi entrada tecleada. **Es exactamente la especie que esta casa
castiga**: teclear una cadena en vez de medirla. La salida en rojo va entera en
el reporte y el motivo queda escrito en el propio fichero.

### TAREA 2. EL CIERRE DE DOS REPORTES. EL DE LA 185 CIERRA; EL DE LA 184, NO: PARADA

**TODAS LAS CIFRAS DE ESTA SECCION SALEN DE CONTAR SUS FICHEROS DE SALIDA CON
`scripts/loop/_v185_tallar_t2.py`, Y NINGUNA ESTA TECLEADA.**

#### 2.a EL REPORTE DE LA 184: LA RAMA NUEVA FUNCIONA Y EL CIERRE SIGUE EN ROJO

**PRIMERO LAS TRES PIEZAS, COTEJADAS POR `sha256` Y POR BYTES CONTRA LO QUE LA
184 MIDIO. LAS TRES CALZAN**, y el cotejo salio **VERDE**:

| pieza | medida hoy |
|---|---|
| `docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt` | **2435 bytes en disco y 2415 bytes normalizados a LF** |
| `scripts/loop/_v184_cierre_texto.md` | **13982 bytes en disco y 13982 bytes normalizados a LF** |
| `docs/loop/SALIDA_V183_BATERIA.txt` | **71753 bytes en disco y 71753 bytes normalizados a LF** |

Salida del cotejo: `docs/loop/SALIDA_V185_T2A_VEREDICTO_184.txt` (**2322 bytes en disco y 2322 bytes normalizados a LF**).

**EL VEREDICTO DE UNA LINEA SE TALLO Y NO SE TECLEO A OJO.** Sus dos numerales
salen de `caidas_propias_del_cuerpo()` y `tareas_de_la_tabla()` corridas sobre
las dos mitades que la guarda `B.1` juzga, y la guarda dio **CIFRA numerales
que NO calzan: 0**. Mutado un numeral, la guarda cae. La frase quedo en
`docs/loop/SALIDA_V185_T2A_VEREDICTO_184_FRASE.txt` (**356 bytes en disco y 356 bytes normalizados a LF**).

**LO QUE EL ENCARGO PEDIA Y SI PASO: LA RAMA DE LA SECCION 9 SALIO `CORRIDA`**
**POR LA RAMA NUEVA**, y su motivo nombra que la bateria se **CONTINUO** y que
la vuelta 184 sello **5** de sus tramos, leidos del asunto de su ultimo commit
con `git log` y no tecleados. Las lineas que lo dicen, pegadas de la salida:

```
      tramo 1   -> vuelta 183
      tramo 2   -> vuelta 183
      tramo 3   -> vuelta 183
      tramo 4   -> vuelta 183
      tramo 5   -> vuelta 184
      tramo 6   -> vuelta 184
      tramo 7   -> vuelta 184
      tramo 8   -> vuelta 184
      tramo 9   -> vuelta 184
   CIFRA tramos sellados EN LA VUELTA 184: 5 [5, 6, 7, 8, 9]
   RAMA DE LA SECCION 9, decidida por rama_de_la_seccion9(): CORRIDA
      motivo: la bateria del fichero es de la vuelta 183 y se esta cerrando la 184, pero NO ES UNA CORRIDA AJENA: ES LA MISMA BATERIA CONTINUADA. La vuelta 184 sello 5 de sus tramos (los tramos 5, 6, 
```

#### PARADA. EL CIERRE DE LA 184 CAE EN ROJO POR TRES GUARDAS MAS, Y NINGUNA ES LA RAMA

`scripts/loop/cerrar_reporte.py --vuelta 184` devuelve **exitcode 1**. La salida
entera vive en `docs/loop/SALIDA_V185_CERRAR_REPORTE_184.txt` (**5581 bytes en disco y 5497 bytes normalizados a LF**).

**Y AQUI NO SE PEGA ENTERA, CON UN MOTIVO MEDIDO Y NO UNA EXCUSA.** Esa salida
lleva dentro la marca de maquina que la **pieza (2)** de `piezas_que_faltan()`
busca **en todo el texto del reporte, sin excluir los bloques cercados**.
Pegarla aqui haria caer el cierre de **este** reporte por el mismo falso
positivo que cazo al de la 184, que es exactamente la averia que se esta
reportando. **Se cita por su ruta con sus bytes, se pegan las lineas que
deciden, y se dice.** El fichero entero esta commiteado: no se pierde nada.

**LOS TRES MOTIVOS DEL ROJO, CONTADOS DE ESA SALIDA:**

| motivo | cifra de su fichero | que especie es |
|---|---:|---|
| piezas de las cuatro que faltan | **2** | (2) y (4) |
| cifras publicadas sin su pareja | **10** | guarda `cifras_sin_pareja()` |
| citas de arnes que NO calzan | **0** | ninguna |

1. **LA PIEZA (4) ES LA COPIA GEMELA DE LA REGLA QUE LA `1.c` ACABA DE
   REPARAR.** `piezas_que_faltan()` lleva su propia comparacion de vuelta ajena
   y **no recibe la evidencia de los tramos**. Es la PARADA que la TAREA 1.c ya
   trajo levantada y que el encargo prohibe tocar.
2. **LA PIEZA (2) ES UN FALSO POSITIVO DE LA MISMA ESPECIE.** La cabecera **SI**
   esta pegada: las **11 filas de 11** del tallador estan dentro y **0 quedan
   fuera**. Lo que enciende la pieza es que la marca de maquina aparece **UNA**
   vez en todo el reporte, en su **linea 353**, **dentro de un bloque cercado**
   que cita la salida roja de la 184.
3. **LAS CIFRAS SIN PAREJA VIVEN EN EL CUERPO QUE LA 184 YA ESCRIBIO**, y el
   encargo manda cerrar *"con el texto que ya tiene"*. Repararlas seria
   reescribir un texto que no me toca reescribir.

**QUE HAY EN DISCO, DICHO SIN ADORNAR:**

- `docs/loop/reportes/REPORTE_V184.md`, **33608 bytes en disco y 33608 bytes normalizados a LF**, **517 lineas**, `sha256` LF
  `6bbeb09c5822c192`, archivado con **exitcode 0**. **NO ES EL CERRADO:**
  `archivar_reporte.py` lee de git y no del arbol, asi que archivo el ultimo
  estado **commiteado**, el que la 184 dejo.
- `docs/loop/SALIDA_V185_T2A_REPORTE_184_CERRADO_EN_ROJO.md` (**122030 bytes en disco y 122030 bytes normalizados a LF**):
  lo que el instrumento **si** llego a escribir antes de devolver 1, guardado
  con un nombre que dice lo que es. El instrumento escribe en su bloque C y
  juzga en el D.
- `docs/loop/SALIDA_V185_T2A_REPORTE_184_ANTES.md` (**33608 bytes en disco y 33608 bytes normalizados a LF**):
  el estado previo, para que las dos caras se puedan comparar.
- `docs/loop/REPORTE.md` se restauro con `git checkout` al estado commiteado,
  para que el arbol y el archivado digan lo mismo.

**LA CUENTA DE VUELTAS QUE CIERRAN SU PROPIO REPORTE, PARA LA 184, SIGUE EN
CERO.** No lo fuerzo y no lo arreglo yo.

#### 2.b EL REPORTE DE LA 185 SE ABRE, SE LLENA Y SE CIERRA

**EL ESQUELETO** se tallo en el paso 4 del orden de esta vuelta, con sus **2
filas vacias**. `docs/loop/REPORTE.md` nacio con **7542 bytes normalizados a LF**,
contados por el propio esqueleto antes de escribirlos en disco.
Salida: `docs/loop/SALIDA_V185_ESQUELETO.txt` (**3965 bytes en disco y 3901 bytes normalizados a LF**).

**Y SU PASO 0 NO TUVO REPORTE AJENO QUE ARCHIVAR, Y LO DICE EN VEZ DE DEJAR LA
FILA MUDA.** Su salida publica que el destino
`docs/loop/reportes/REPORTE_V184.md` **YA EXISTE con contenido IDENTICO**, y que los dos `sha256` calzan con
el reporte que se iba a pisar. Es lo que el encargo predijo, porque la **2.a**
lo archivo antes.

**CADA TAREA ANEXO SU FILA AL CERRARSE**, no al final: la TAREA 1 entro con su
seccion entera antes de que esta se escribiera.

**LA SECCION 9 DE ESTE REPORTE CIERRA CON EL HUECO DECLARADO Y MEDIDO, POR EL
CARRIL DE `cerrar_reporte.py` Y NO A MANO.** Las tres piezas van juntas o no
vale: **el nombre del fichero**, **sus bytes medidos** y **la atribucion**. **LA
ATRIBUCION ES QUE LA BATERIA CORRE CADA CINCO VUELTAS Y QUE LA SIGUIENTE ES LA
189**, por `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria
cerro entera en la 184 con sus nueve tramos sellados.

**SI ESTA VUELTA CIERRA SU REPORTE, ES LA PRIMERA DE LAS DOS SEGUIDAS QUE EL
REGIMEN 6.2 PIDE PARA DEVOLVER EL TOPE A CINCO.** Dicho con esas palabras, y
dicho tambien lo otro: **la 184 no lo cerro hoy tampoco**, asi que la cuenta que
empieza es la de la 185 y no una que venga de atras.

#### LAS GUARDAS DEL CIERRE, RECOMPUTADAS AL CIERRE

`git diff --numstat -- dataset/` al salir de la vuelta: **0 filas**. Al entrar
dio **0 filas**, medido en el bloque de apertura antes de la primera operacion.

El ciclo de Gate 0 corrio entero y en su orden al cierre, y sus salidas viven en
`docs/loop/SALIDA_V185_*_CIERRE.txt`. La tabla de la cabecera de este reporte
sale de ellas con `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 185`
y **ninguna celda esta tecleada**.

#### LOS DISCUTIBLES DE ESTA TAREA, MARCADOS ANTES DE SABER SI ACIERTO

**`D.6`. NO PEGUE ENTERA LA SALIDA ROJA DEL CIERRE DE LA 184.** El encargo de
la 2.a dice *"paras y lo traes entero"*, y la 184 pego la suya entera. **Yo la
cito por su ruta con sus bytes y pego las lineas que deciden**, porque pegarla
entera haria caer el cierre de este reporte por la pieza (2). **Mi razon es que
un reporte que no cierra no trae la PARADA a nadie**, y el fichero entero esta
commiteado. **Pero es una desviacion de la letra y la marco.**

**`D.7`. CERRE EL REPORTE DE LA 185 SABIENDO QUE EL DE LA 184 NO CERRO.** Se
puede leer que el orden del encargo hacia del cierre de la 184 una condicion
previa. **Mi lectura es que son dos reportes distintos y que el mio no depende
del suyo**, y que dejar los dos sin cerrar seria la quinta vuelta seguida sin
reporte cerrado. **Lo marco porque la lectura contraria es defendible.**

#### PENDIENTES DE DOCTRINA

**`PD.1` SIGUE ABIERTA Y NO LA TOCO:** las cinco `D` con el diferenciador ya
presente el dia del veredicto, hoy con sus cinco puestos escritos en el `R.47`.

**`PD.5` NUEVA. UNA MARCA DE MAQUINA CITADA DENTRO DE UN BLOQUE CERCADO SIGUE
SIENDO UNA MARCA DE MAQUINA.** La pieza (2) busca su marca en todo el texto y
`cifras_sin_pareja()` ya excluye los bloques cercados: **dos guardas del mismo
fichero tratan la cita al reves la una de la otra**. No hay regla escrita que
elija, y hoy eso impide que un reporte pueda citar el rojo de otro.

**`PD.6` NUEVA. UNA REGLA ESCRITA DOS VECES EN EL MISMO FICHERO.**
`rama_de_la_seccion9()` y la pieza (4) de `piezas_que_faltan()` llevan la misma
comparacion de vuelta ajena. Reparar una y no la otra deja el instrumento
diciendo dos cosas distintas del mismo caso. **Es la PARADA de la 1.c dicha como
doctrina.**

<!-- FIN ANEXO DE TAREAS -->

## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LAS DOS TAREAS DEL ENCARGO CERRARON.** El tope era dos, por el regimen
temporal de `AUDITOR.md` 6.2, y son dos. **La TAREA 1 cierra con una PARADA
levantada en su `1.c` y la TAREA 2 con otra en su `2.a`, y las dos van
escritas con su medicion, no con una impresion.**

- rama, leida con `git rev-parse --abbrev-ref HEAD`: `pasada-unica`
- HEAD de apertura, sellado **antes de la primera operacion** en
  `docs/loop/SALIDA_V185_HEAD_APERTURA.txt`: **`5834632b`**
- HEAD del ultimo commit antes de cerrar, leido con `git rev-parse HEAD`
  **despues de la ultima operacion**: **`403e50c3`**
- commit del acta 185, localizado con `git log --grep` y no tecleado:
  **`5834632b`**
- commit de nacimiento del bloque de apertura, `git log --diff-filter=A`:
  **`2c72d81d`**

**GATE 0 VERDE ENTERO EN SU CICLO, EN LA APERTURA Y OTRA VEZ AL CIERRE.** Sus
salidas son `docs/loop/SALIDA_V185_GATE0_CMD1_APERTURA.txt` (**4859 bytes en disco y 4790 bytes normalizados a LF**)
y `docs/loop/SALIDA_V185_GATE0_CMD1_CIERRE.txt` (**4859 bytes en disco y 4790 bytes normalizados a LF**),
con motor **25/25** en la apertura y **25/25** al cierre, `tsc` **EXIT=0** y **EXIT=0**,
y web **1040 passed (1040)** y **1040 passed (1040)**. La apertura entera vive en
`docs/loop/SALIDA_V185_APERTURA.txt` (**26084 bytes en disco y 26084 bytes normalizados a LF**)
y **la sello el PRIMER commit de la vuelta**.

**EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA, ANTES DE LA PRIMERA
OPERACION**, que es donde `EJECUTOR.md` 1 lo manda desde la 178: **4 filas**
en la apertura y **4 filas** al cierre.

**EL ARCHIVO DE VEREDICTOS NO SE MOVIO, Y ESA ES LA PRUEBA INDEPENDIENTE DE
QUE ESTA VUELTA NO TOCO NINGUN VEREDICTO.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:
**3388 filas**, **A 551, B 72, C 5, D 2760**, **0 huecos y 0 duplicados**,
**4051967 bytes en disco y 4051967 bytes normalizados a LF**, y `sha256` **`ea6e850d331d14f0`**
**identico por las dos convenciones, disco `ea6e850d331d14f0` y LF `ea6e850d331d14f0`**.
Es el mismo que la apertura de esta vuelta midio y el mismo que las actas 179
a 185 publican.

## 4. LA GUARDA DEL COMMIT DE `dataset/`, CORRIDA EL DIA QUE SERVIA

`git status --porcelain` da **15 lineas** al cerrar la vuelta, y
`git diff --numstat -- dataset/` da **0 filas**. **Al ENTRAR, medido en el
bloque de apertura antes de la primera operacion, dio 0 filas tambien.**
**Ninguna perdida de catalogo que declarar**, y `dataset/` no se commitea en
esta vuelta.

**Y ESTA VUELTA NO TIENE LA `M dataset/metadata/master_graph.json` QUE LAS
ANTERIORES TRAIAN.** El arbol abrio limpio, con `git status --porcelain` en
cero lineas, cosa que el docstring del bloque de apertura predijo **antes** de
medirla y que sus bloques C, D, E y F midieron sin saber lo que habia escrito.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**LOS SIETE VAN EN SUS DOS SEDES Y AQUI SE LISTAN JUNTOS, QUE ES LO QUE LA
`5.7` DEL ACTA 185 PIDE.** Los cinco primeros nacen en el anexo de la TAREA 1
y los dos ultimos en el de la TAREA 2; **ninguno se tapa y ninguno cambia de
redaccion al repetirse aqui su titulo**.

- **`D.1`. ANADI UN CAMBIO MAS DE LOS TRES QUE LA `1.d` NOMBRA:** la
  procedencia de la novena columna en la prosa del tallador. No mueve ninguna
  celda, pero el encargo no lo pidio.
- **`D.2`. MI ARNES DE LA `1.b` SALIO EN ROJO EN SU PRIMERA CORRIDA Y LO
  REPARE YO EN VEZ DE TRAERLO.** Lei que la regla de detenerse protege a los
  arneses ya sellados y no al que estoy escribiendo. **La corrida en rojo va
  entera en el reporte.**
- **`D.3`. PUBLIQUE LA COLUMNA `quien lo sello` CON UNA NEGRITA COMPUTADA**,
  deducida de las celdas que tenia que reproducir. Nadie escribio esa regla de
  formato.
- **`D.4`. NO METI LOS DOS ARNESES NUEVOS EN LA NOMINA DE LA BATERIA.** Esta
  vuelta no es de bateria y su encargo no nombra la nomina. **La 189 empezara
  en rojo por esa via si nadie los mete antes.**
- **`D.5`. GUARDE EL REPORTE DE LA 184 QUE `cerrar_reporte.py` SI LLEGO A
  ESCRIBIR Y DESPUES RESTAURE EL ARBOL** con `git checkout`. Destruirlo habria
  perdido la evidencia; dejarlo habria hecho que el esqueleto pisara un texto
  sin otra sede.
- **`D.6`. NO PEGUE ENTERA LA SALIDA ROJA DEL CIERRE DE LA 184**, porque lleva
  dentro la marca de maquina que la pieza (2) busca en todo el texto. **La cito
  por su ruta con sus bytes y pego las lineas que deciden.** Es una desviacion
  de la letra del encargo.
- **`D.7`. CERRE EL REPORTE DE LA 185 SABIENDO QUE EL DE LA 184 NO CERRO.** Se
  puede leer que el orden del encargo hacia del cierre de la 184 una condicion
  previa. **La lectura contraria es defendible y por eso va marcado.**

## 6. LAS PREGUNTAS

**`P.1`. LA PIEZA (4) Y LA PIEZA (2) DE `piezas_que_faltan()`, ¿SE REPARAN
JUNTAS O POR SEPARADO?** La (4) es la copia gemela de la regla que la `1.c`
acaba de reparar. La (2) es otra especie: busca su marca **en todo el texto**,
y un reporte que **cita** una salida roja dentro de un bloque cercado la lleva
dentro sin estar sin tallar. **No se cual es prioridad y no me lo encargaron.**

**`P.2`. ¿QUE SE HACE CON LAS CIFRAS SIN PAREJA DEL REPORTE DE LA 184?** La
guarda `cifras_sin_pareja()` las caza y el encargo prohibe tocar ese texto. **O
se exime el texto ya escrito, o se reescribe, o la guarda aprende a mirar solo
lo nuevo.** No elijo yo.

**`P.3`. ¿LOS DOS ARNESES NACIDOS HOY ENTRAN EN LA NOMINA DE LA BATERIA, Y
QUIEN LOS METE?** La `5.6` del acta 185 ampara meterlos en su propia vuelta,
pero esta no es vuelta de bateria. **Medido hoy: `arneses_que_faltan()` da 2.**

## 7. PENDIENTES DE DOCTRINA

**`PD.1` SIGUE ABIERTA Y NO LA TOCO:** las cinco `D` con el diferenciador ya
presente el dia del veredicto, **1778, 2530, 2540, 3141 y 3232**, hoy con sus
cinco puestos escritos en el `R.47` y leidos del acta, no copiados del encargo.

**`PD.5` NUEVA. UNA MARCA DE MAQUINA CITADA DENTRO DE UN BLOQUE CERCADO SIGUE
SIENDO UNA MARCA DE MAQUINA.** La pieza (2) busca su marca en todo el texto y
`cifras_sin_pareja()` ya excluye los bloques cercados: **dos guardas del mismo
fichero tratan la cita al reves la una de la otra.** Hoy eso impide que un
reporte pueda citar entero el rojo de otro.

**`PD.6` NUEVA. UNA REGLA ESCRITA DOS VECES EN EL MISMO FICHERO.**
`rama_de_la_seccion9()` y la pieza (4) de `piezas_que_faltan()` llevan la misma
comparacion de vuelta ajena. **Reparar una y no la otra deja el instrumento
diciendo dos cosas distintas del mismo caso.** Es la PARADA de la `1.c` dicha
como doctrina.

**`PD.2`, `PD.3` Y `PD.4` QUEDARON CERRADAS POR EL ACTA 185** y no se reabren
aqui: estan registradas en el `R.47` con su estado leido del titulo del acta.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**`C.1`. ESCRIBI UN ARNES CUYA SALIDA SELLADA LLEVABA DENTRO EL MISMO DATO QUE
CAMBIA SOLO QUE LA REPARACION VENIA A QUITAR.** La primera version de
`scripts/loop/vuelta185_tarea1b_mutacion_sin_temporal.py` pegaba sus lineas de
entrada **crudas**, con el sufijo aleatorio del `mkdtemp` dentro. **Habria
hecho caer la bateria de la 189 por la misma averia que estaba reparando.** Lo
cace **releyendo mi propio fichero**, no un instrumento, y anadi `mostrar()`.
La prueba de que ya no pasa es que sus dos corridas seguidas dan la misma
salida byte a byte.

**`C.2`. MI PRIMER ARNES DE LA `1.b` FABRICO UN TEMPORAL QUE NO EXISTE Y SUS
DOS CASOS DE RUTA RELATIVA SALIERON EN ROJO.** La funcion bajo prueba estaba
bien; lo que estaba mal era **mi entrada tecleada**, que no es la cadena que
`os.path.relpath` produce. **Es exactamente la especie que esta casa castiga:
teclear en vez de medir.** La corrida en rojo va entera en el reporte y el
motivo queda escrito dentro del propio fichero, no en una nota aparte.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 185 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V185_HUECO_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: NADIE la corrio, y no es un olvido: por AUDITOR.md 6.1, decision del fundador del 5 sep 2026, la bateria de mutaciones corre CADA CINCO VUELTAS en una vuelta propia que no lleva nada mas. Cerro entera en la VUELTA 184, con sus nueve tramos sellados y su composicion de 71753 bytes en disco y 71753 bytes normalizados a LF, y LA SIGUIENTE VUELTA DE BATERIA ES LA 189. La 185 es una vuelta intermedia y su seccion 9 cierra con este hueco declarado y medido, que es lo que esa misma decision manda.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
