# REPORTE DE LA VUELTA 171 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta171_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre talla la cabecera. **Si esta vuelta se corta,
> lo que quede aqui es lo que de verdad se hizo, y las filas que sigan diciendo
> ABIERTA, SIN CERRAR son las que no se hicieron.** Tope de cinco tareas, y el
> encargo trae exactamente cinco.
>
> **Y EL ESQUELETO YA NO PUEDE PISAR UN REPORTE SIN ARCHIVAR** (TAREA 5.a de esta
> misma vuelta): su paso 0 corre el archivador y **se niega a escribir** si el
> reporte anterior no esta guardado byte a byte. Esta corrida lo paso en verde
> contra `docs/loop/reportes/REPORTE_V170.md`.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta171_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 170: `d7b18370`, asunto real leido de git log:
  '@ ACTA DE LA VUELTA 170 DEL AUDITOR: LAS CINCO TAREAS REPRODUCEN AL DIGITO, PERO LA VUELTA NO CERRO SU REPORTE Y SU PROPIO BORRADOR ENVENENO AL INSTRUMENTO QUE SOSTIENE SU PARADA. NO HAY PARADA: LA REGLA QUE EL EJECUTOR BUSCABA ESTABA ESCRITA EN EL CODIGO @'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V171_HEAD_APERTURA.txt`: `0caca89f`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `ce1e3aa3`
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 171`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Son todas del lado CIERRE, que al abrir todavia no existe.
Este hueco se rellena con la tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | BLOQUEANTE. LOS REGISTROS Y EL CIERRE QUE FALTO (1.a el acta 170 al `R.40` con su arnes de mutacion del registro, 1.b el reporte de la 170 CERRADO con la cabecera tallada pegada y sus ocho discutibles y cinco caidas sin suavizar, 1.c la seccion 9 dice que la bateria NO corrio y no se rellena con una corrida de hoy, 1.d el archivador para la 170 y este esqueleto) | **CERRADA** | `SALIDA_V171_T1A_REGISTRO_ACTA_170.txt`, `_T1A_MUTACION_REGISTRO`, `_T1B_CERRAR_REPORTE_170`, `_T1B_COMPARAR_CABECERA_170`, `_T1B_RELECTURA_DESDE_GIT`, `_T1D_ARCHIVADOR_170`, `_T1D_ESQUELETO` |
| **TAREA 2** | BLOQUEANTE PARA LA 3. EL BORRADOR QUE ENVENENO UN INSTRUMENTO (adjudicacion 6.3): los cinco `docs/loop/_v170_t*_seccion.md` salen de `docs/` con `git mv`, sin borrar ni editar ninguno, y las dos varas del contador `LD` tienen que converger en `LD-138` o se para | **CERRADA, Y TRAE UNA PARADA** | `SALIDA_V171_T2_SACAR_BORRADORES.txt`, `_T2_ATRIBUCION`, `_T2_LAS_DOS_FUENTES`, `_T2_CONTAR_LD_222ca6a7`, `_T2_CONTAR_LD_0caca89f`, `_T2_CONTAR_LD_ANTES`, `_T2_CONTAR_LD_DESPUES` |
| **TAREA 3** | LA NUMERACION `LD`, QUE YA NO ES PARADA (adjudicacion 6.1): las 16 filas de la segunda tanda de `docs/plan/LECTURAS_DIRIGIDAS.md` ganan `LD-139` a `LD-154` POR ADICION PURA, con los numeros COMPUTADOS POR INSTRUMENTO y sin tocar una palabra de su texto | **NO SE CORRE: PARADA DECLARADA EN LA TAREA 2** | (la 2 es bloqueante para la 3 y su guarda cayo: `SALIDA_V171_T2_SACAR_BORRADORES.txt` bloque H) |
| **TAREA 4** | LAS DOS DEUDAS DE REGISTRO (adjudicaciones 6.4 y 6.11): 4.a el agujero del `R.38` corregido por el carril del `9.10` con la frase vieja entera y tachada, 4.b el `81` de `docs/plan/00_INDICE.md:644` con la cifra de hoy adosada por `9.21` y sin tocar la letra vieja | **CERRADA** | `SALIDA_V171_T4_DEUDAS_DE_REGISTRO.txt`, `_T4B_CONTAR_LD` |
| **TAREA 5** | LOS TRES INSTRUMENTOS QUE FALTAN (adjudicaciones 6.6, 6.9 y 6.12): 5.a el archivador ENCHUFADO como paso 0 del esqueleto, 5.b el CENSO del campo `forma` sobre las 672 entradas del inventario, 5.c el barrido MEDIDO de los 8 pares sin leer de `la supervision de la IA` sobre las 71 fichas | **CERRADA**: 5.a enchufada con su mutacion, 5.b y 5.c MEDIDAS | `SALIDA_V171_T5A_MUTACION_ENCHUFE.txt`, `_T5BC_CENSO_Y_BARRIDO`, `_T5C_CONTRAPRUEBA`, `_T5C_BARRIDO_CORREGIDO` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
### TAREA 1 (BLOQUEANTE). LOS REGISTROS Y EL CIERRE QUE FALTO

**EL ORDEN DE LA APERTURA SE INVIRTIO COMO EL ENCARGO MANDA, CON UNA SOLA
DESVIACION Y VA DECLARADA.** El encargo ordena (1) cerrar el reporte de la 170,
(2) archivarlo, (3) tallar el esqueleto y correr el bloque de apertura. **La
MEDICION de apertura la corri ANTES de todo**, porque `EJECUTOR.md` 1 dice *"LA
APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION"* y esa regla es permanente; el
motivo del encargo (que el esqueleto pisa `REPORTE.md`) vale para el ESQUELETO y
no para la medicion, cuyas salidas son `SALIDA_V171_*_APERTURA.txt` y ninguna es
`REPORTE.md`. **El TALLADO del esqueleto si va donde el encargo lo pone.** Va
como `D.1`.

**1.b EL REPORTE DE LA VUELTA 170 QUEDA CERRADO** (`ca55afd8`), instrumento
`scripts/loop/vuelta171_tarea1b_cerrar_reporte_170.py`, salida
`docs/loop/SALIDA_V171_T1B_CERRAR_REPORTE_170.txt`, **exit 0**. Las tres cosas
que hace son PEGAR y no escribir:

| celda | de donde sale | valor |
|---|---|---:|
| el reporte antes | `git show HEAD:docs/loop/REPORTE.md`, bloque H de la apertura | 530 lineas, 32.473 bytes |
| ficheros que toca `29f04e86` | `git show --stat` | **12** |
| `docs/loop/REPORTE.md` entre ellos | del mismo `--stat` | **NO** |
| la tabla de la cabecera | `SALIDA_V170_TALLADOR_CABECERA.txt`, pegada entera | 2.443 bytes, **11** filas |
| el cuerpo | `scripts/loop/_v170_cierre_texto.md`, anexado tal cual | 9.010 bytes, 150 lineas |
| discutibles contados del borrador | barrido `^- \*\*`D.n`` | **8** |
| caidas contadas del borrador | 4 numeradas mas la quinta sin numero | **5** |
| commits de la tabla del borrador | `git log 46208790..29f04e86` | **8 de 8 en el rango, 0 fuera** |
| el reporte despues | del fichero escrito | 729 lineas, 45.706 bytes |

**LA CABECERA CALZA, Y NO LO DIGO YO:**
`tallar_cabecera_reporte.py --fase04 --vuelta 170 --comparar docs/loop/REPORTE.md`
da **exit 0** y *"filas cotejadas: 9 | DISTINTAS: 0 | ausentes: 0. CABECERA:
IDENTICA AL TALLADOR"* (`docs/loop/SALIDA_V171_T1B_COMPARAR_CABECERA_170.txt`).

**1.c LA SECCION 9 DICE QUE LA BATERIA NO CORRIO, Y NO SE RELLENA.**
`docs/loop/SALIDA_V170_BATERIA.txt` existe y mide **0 bytes**, medido hoy con
`os.path.getsize` por el propio instrumento antes de escribir. **Ahi no se pega
una corrida de la 171**, y el instrumento tiene una guarda que lo comprueba
(*"la seccion 9 no cuela ninguna corrida de la 171"*). Se remite a la seccion 5
del acta 170, `docs/loop/ACTA_AUDITOR.md:57574` (linea localizada por el
instrumento, no tecleada), **con la atribucion del auditor delante**.

**LA RELECTURA AL DOBLE, PIEZA 1, HECHA DESPUES DE COMMITEAR Y LEYENDO DE GIT**
(`docs/loop/SALIDA_V171_T1B_RELECTURA_DESDE_GIT.txt`): `git show --stat` dice que
`docs/loop/REPORTE.md` **si** esta entre los ficheros de `ca55afd8`, y
`git show ca55afd8:docs/loop/REPORTE.md` pasa las **11** comprobaciones con **0
fallos**, incluida *"el borrador entero, byte a byte dentro del commiteado"*.

**1.d EL ARCHIVADOR Y EL ESQUELETO.** `archivar_reporte.py --vuelta 170` sale
**VERDE** (`docs/loop/SALIDA_V171_T1D_ARCHIVADOR_170.txt`): destino
`docs/loop/reportes/REPORTE_V170.md`, 45.706 bytes, 729 lineas, sha256
`0b85f30e9c78e2b4...`, commit de origen `ca55afd8`. Y el esqueleto de la 171
(`docs/loop/SALIDA_V171_T1D_ESQUELETO.txt`, exit 0) **ya no puede pisar un
reporte sin archivar**: su paso 0 es la TAREA 5.a y se cuenta alli.

**1.a EL ACTA 170 ENTERA QUEDA EN EL `R.40`.** Instrumento
`scripts/loop/vuelta171_tarea1_registrar_acta170.py`, salida
`docs/loop/SALIDA_V171_T1A_REGISTRO_ACTA_170.txt`, **exit 0**:

| celda | de donde sale | valor |
|---|---|---:|
| cuerpo del acta 170 acotado | cabecera y final del fichero | lineas 57.288 a 57.846 |
| adjudicaciones `6.n` | barrido del acta, para en el primer hueco | **12** (6.1 a 6.12) |
| caidas, patron VIEJO (el de la 170) | barrido del cuerpo acotado | **0** |
| caidas, patron NUEVO (las dos formas) | barrido del cuerpo acotado | **4** |
| serie antes de escribir | `serie_de_registros.py`, sus DOS sedes | 31 entradas, 0 colisiones, 0 huecos |
| siguiente libre, computado | mayor mas uno | **R.40** |
| sede, leida de la regla | `docs/loop/ACTA_AUDITOR.md:53933` | `docs/PENDIENTES.md` |
| reparto por via, computado | del mapa `VIA` | **EJECUTADA 8** (6.1, 6.2, 6.3, 6.4, 6.6, 6.9, 6.11, 6.12); **SIN TOCAR NADA 4** (6.5, 6.7, 6.8, 6.10) |
| que suben al fundador | del reparto | **0** |
| serie despues de escribir | recomputada | 32 entradas, 0 colisiones, 0 huecos |
| donde vive | recomputado | `R.40` en `docs/PENDIENTES.md:12262` |

**Y AQUI HAY UNA ADAPTACION DE PATRON QUE DECLARO EN VEZ DE PASAR CALLANDO.** El
acta 169 escribia sus caidas como `**CAIDA 1. ...**` al principio de linea; el
acta 170 las escribe **como vineta y con comillas inversas**. El patron de la
vuelta 170, corrido sobre el acta 170, cuenta **0**. Si lo hubiera heredado tal
cual, la entrada `R.40` habria salido **sin ninguna caida y sin que nada lo
cazara**, porque el registrador solo para cuando el conteo es cero y aqui habria
parado por el motivo equivocado. **El patron nuevo acepta la vineta y las
comillas como OPCIONALES**, casa con las dos formas, y sigue exigiendo la
negrita, el numero y el signo detras. Va como `D.2`.

**EL ARNES DE MUTACION DEL REGISTRO, QUE LA 169 PROMETIO Y NO ESCRIBIO Y LA 170
SI:** `scripts/loop/vuelta171_tarea1a_mutacion_registro.py`, salida
`docs/loop/SALIDA_V171_T1A_MUTACION_REGISTRO.txt`, **exit 0**: **43 casos, 43
pasan, 43 caen al mutar el esperado**. Sus cinco casos nuevos son los del patron:
que el nuevo ve las dos formas (4 y 4), que **el viejo no ve ninguna vineta (0)**,
que no casa con negritas que no son de caida (0 de 4 senuelos), y que el titulo
de una caida con vineta sale **sin el guion de lista pegado**.

### TAREA 2 (BLOQUEANTE PARA LA 3). EL BORRADOR QUE ENVENENO UN INSTRUMENTO

**LOS CINCO SALIERON, Y NO SIRVIO DE NADA: LAS DOS VARAS NO CONVERGEN. PARO Y LO
TRAIGO, QUE ES LO QUE EL ENCARGO MANDA CON ESAS PALABRAS.** Instrumentos
`scripts/loop/vuelta171_tarea2_sacar_borradores.py` (**exit 1**, y sale en 1 a
proposito: su guarda es la que cae) y
`scripts/loop/vuelta171_tarea2_atribuir_universo.py` (**exit 0**).

**EL MOVIMIENTO SI SE HIZO, ENTERO Y SIN PERDER NADA:** `git mv` de los cinco
`docs/loop/_v170_t*_seccion.md` a `scripts/loop/`, **5 de 5 con sha256 identico
en el destino y 0 de 5 quedando en `docs/loop/`**, comprobado fichero a fichero
(`docs/loop/SALIDA_V171_T2_SACAR_BORRADORES.txt`, bloque E). **Nada se borro y
nada se edito.**

**LAS TRES LECTURAS QUE EL ENCARGO PIDE, MAS UNA CUARTA QUE HIZO FALTA**, todas
del contador `scripts/loop/vuelta48_contar_ld.py` corrido por mi en esta vuelta,
las de corte viejo sobre WORKTREE LIMPIO y no sobre el arbol de hoy:

| lectura | hechas | mayor de las hechas | mayor del universo | huecos | sin seccion |
|---|---:|---:|---:|---:|---:|
| `222ca6a7`, worktree limpio | 82 | **LD-138** | **LD-138** | 54 | 2 |
| `0caca89f` (HEAD de apertura), worktree limpio | 82 | LD-138 | **LD-154** | 64 | 8 |
| HEAD, ANTES de mover | 82 | LD-138 | **LD-154** | 64 | 8 |
| HEAD, DESPUES de mover | 82 | **LD-138** | **LD-154** | 64 | 8 |

**TU CIFRA DE 54 ERA CIERTA Y LA REPRODUJE EXACTA**, y tambien reproduje exacta
la de 64 con sus 8. **Pero mover los cinco no movio ni una cifra**, y eso es lo
que hay que explicar.

**LA CAUSA, MEDIDA Y NO SUPUESTA** (`docs/loop/SALIDA_V171_T2_ATRIBUCION.txt`,
bloque B, y `docs/loop/SALIDA_V171_T2_LAS_DOS_FUENTES.txt`). **Los ocho numeros
son los mismos ocho; lo que cambio por completo es DE DONDE SALEN.** En
`0caca89f` los seis de mas venian TODOS de `docs/loop/_v170_t4_seccion.md`, que
es lo que el acta 170 midio. Hoy, con ese fichero ya fuera de `docs/`, los mismos
seis vienen de **dos ficheros que en `0caca89f` no los nombraban, y los dos los
ha escrito ESTA VUELTA**:

| fuente de hoy | que numeros trae | de donde sale |
|---|---|---|
| `docs/loop/reportes/REPORTE_V170.md` | `LD-12`, `LD-27`, `LD-100`, `LD-137`, `LD-139`, `LD-154` | **NO EXISTIA en `0caca89f`**; lo crea la TAREA 1.d de esta vuelta (`git log --diff-filter=A` lo ancla en `dd34047a`) |
| `docs/PENDIENTES.md` | `LD-12`, `LD-27`, `LD-139`, `LD-154` | **cero apariciones en `0caca89f`, una hoy**, y esta en UNA sola linea, `docs/PENDIENTES.md:12296`, que es la glosa de la adjudicacion `6.1` dentro del `R.40` que escribio la TAREA 1.a de esta vuelta |

**Y LA PRIMERA DE LAS DOS TIENE UNA PRUEBA QUE NO ADMITE DISCUSION:** el sha256
(LF) de `docs/loop/reportes/REPORTE_V170.md` es
`0b85f30e9c78e2b4d59e19deb9aa30d61d3724800bd54e7309246fb405bd1e16`, **y el
sha256 de `docs/loop/REPORTE.md` en `ca55afd8` es exactamente el mismo**. O sea
que el contador esta contando, como si fuera un encargo, **un fichero que es
BYTE A BYTE el mismo que el contador ya excluye por NARRATIVO DEL BUCLE**.

**LO QUE ESTO ES, DICHO SIN ADORNO: LA VUELTA 170 ENVENENO EL CONTADOR CON UN
BORRADOR, Y ESTA VUELTA LO HA ENVENENADO CON DOS COSAS SUYAS AL SACAR EL
BORRADOR.** Y la segunda es peor que la primera por una razon que hay que decir:
el borrador de la 170 era un fichero suelto que alguien podia mover. **El
archivado nace de un automatismo que esta misma vuelta acaba de enchufar** (la
TAREA 5.a), asi que **a partir de ahora cada vuelta deja un
`docs/loop/reportes/REPORTE_V<N>.md` bajo `docs/` sin que nadie tenga que
acordarse**. Es exactamente la especie ancha que el acta 170 subio al fundador en
su seccion 7.3: *"cualquier fichero nuevo bajo `docs/` puede mover la lectura de
un instrumento que barra `docs/`"*.

**NO ACUSO DE MAS:** los otros dos reportes archivados no nombran ningun `LD` sin
seccion (`REPORTE_V168.md` no nombra ninguno; `REPORTE_V169.md` nombra `LD-66` a
`LD-70`, que **si** tienen seccion propia y por eso no entran en la cuenta).

**LA GUARDA, Y CAE:** el mayor de las HECHAS da `LD-138` y el mayor del UNIVERSO
da `LD-154`. **No convergen. LA TAREA 3 NO SE CORRE**, y no por prudencia: si se
corriera, *"el siguiente libre es el mayor mas uno"* sobre este universo daria
**`LD-155`** y no `LD-139`, que es justo la cifra falsa que la guarda existe para
impedir.

**Y NO ARREGLO NINGUNA DE LAS DOS FUENTES, Y DIGO POR QUE.** Para la primera hay
un remedio de una linea (excluir `docs/loop/reportes/REPORTE_V<N>.md` con la
misma vara y por el mismo motivo que los tres narrativos del bucle) y creo que
cabe entero dentro de la adjudicacion `6.3`, que dice que la exclusion **ya
esta** en el instrumento y solo hay que leerla *"sin hacerse el tonto con el
nombre del fichero"*. **Pero el acta 170 reservo al fundador la guarda general
sobre ficheros nuevos bajo `docs/`**, y tocar la lista de exclusiones del
contador es tocar esa guarda. Para la segunda no hay remedio de instrumento
ninguno: `docs/PENDIENTES.md` **si** es un sitio donde cabe un encargo, por el
criterio escrito del propio contador, asi que excluirlo seria doctrina nueva y
ademas mala. **Las dos suben en `PD.1` y en `P.1`, con mi propuesta escrita y
sin ejecutarla.**

### TAREA 3. LA NUMERACION `LD`. NO SE CORRE, Y LA PARADA ES DE LA TAREA 2

**LA REGLA SI QUEDA CERRADA, Y NO ERA DOCTRINA NUEVA.** La adjudicacion `6.1` del
acta 170 tiene razon y lo verifique en el fichero: `serie_de_registros.py`, lineas
97 a 102, `def siguiente_libre(halladas):` con docstring *"EL NUMERO QUE NO SE
TECLEA. Uno mas que el mayor escrito en CUALQUIERA de las sedes"* y
`return (max(nums) + 1) if nums else 1`, **sin condicional de huecos y sin
excepcion**. **EL SIGUIENTE LIBRE ES EL MAYOR MAS UNO, y el camino es el 1.**
Leido hoy, no recordado. El `D.6` de la vuelta 170 (que el tramo `LD-12` a
`LD-27` mida exactamente 16) queda **como contraste medido y no como fundamento**:
el propio contador dice que esos numeros nunca fueron nombrados hasta esta vuelta,
o sea que nadie los asigno, y **una adyacencia no es una asignacion**.

**LO QUE NO SE PUEDE HACER HOY ES APLICARLA, Y EL MOTIVO NO ES LA REGLA SINO EL
UNIVERSO SOBRE EL QUE SE APLICARIA.** La adjudicacion `6.2` es explicita y el
encargo la repite: *"las dos lecturas (hechas y universo) tienen que converger en
`LD-138`; solo entonces se escriben `LD-139` a `LD-154`. Si no convergen, se para
y se trae."* Medido en esta vuelta tras mover los cinco borradores: **hechas hasta
`LD-138`, universo hasta `LD-154`. NO CONVERGEN.**

**Y LA CONSECUENCIA DE SALTARSELO SERIA UNA CIFRA FALSA, NO UNA MOLESTIA:** *"el
mayor mas uno"* sobre el universo de hoy da **`LD-155`**, no `LD-139`. Las 16
filas de la segunda tanda (`docs/plan/LECTURAS_DIRIGIDAS.md`, lineas 327 a 518)
**se quedan sin numero un dia mas, enteras y sin tocar una palabra**, que es
mejor que ganarlo mal.

**LO QUE HACE FALTA PARA CERRARLA CABE EN UNA DECISION, Y VA EN `P.1` Y `PD.1`:**
decir si `docs/loop/reportes/REPORTE_V<N>.md` entra en la lista de exclusiones
del contador con la misma vara que los tres narrativos del bucle, y que hacer con
los `LD` que una entrada de la serie `R.n` nombra al glosar una adjudicacion que
habla de ellos. **Con eso resuelto, la TAREA 3 es una corrida y cabe entera en la
vuelta siguiente.**

### TAREA 4. LAS DOS DEUDAS DE REGISTRO (adjudicaciones 6.4 y 6.11)

Instrumento `scripts/loop/vuelta171_tarea4_deudas_de_registro.py`, salida
`docs/loop/SALIDA_V171_T4_DEUDAS_DE_REGISTRO.txt`, **exit 0**. **La fecha de
corte tampoco se teclea:** la lee del reloj del sistema y da **5 sep 2026**.

**4.a EL AGUJERO DEL `R.38`, PAGADO POR EL CARRIL DEL BANCO `9.10`.**

| celda | de donde sale | valor |
|---|---|---:|
| `R.38` acotado | cabecera y siguiente `## R.n.` | `docs/PENDIENTES.md`, lineas 12.081 a 12.166 |
| veces que la clausula falsa aparece DENTRO de `R.38` | barrido | **1** |
| veces que aparece en el fichero ENTERO | barrido | **1** |
| arneses de mutacion de registro que existen hoy | `ls scripts/loop/ \| grep mutacion_registro` | **7** |
| vueltas representadas | del nombre de cada fichero | 164, 165, 166, 167, 168, 170, **171** |
| ¿existe el de la vuelta 169? | del mismo barrido | **NO** |

**QUE SE TACHA Y QUE NO, Y ES UNA DECISION QUE DECLARO.** La oracion empieza
diciendo *"Lo que lo impide es el espacio final del patron"*, **y eso es
CIERTO**. Lo falso es la clausula que viene detras. **Tache la clausula falsa
entera y deje en pie la parte cierta**: enterrar una afirmacion buena para tapar
una mala no es corregir. Va como `D.3`.

La correccion adosada dice las tres cosas que hacen falta: que **cuando esa
entrada se escribio el arnes no existia** (el registrador de la 169 se quedo sin
`prueba_de_mutacion`), **la nomina medida hoy pegada entera**, y **quien lo trajo
y quien lo corrige**, porque las dos cosas cuentan: lo hallo el ejecutor de la
170 como su `D.8` y no lo corrigio; la `6.4` dice que *"no es mio"* no vale para
una afirmacion falsa en la serie. **Y dice lo que la correccion NO hace:** no
toca el `R.39` ni el `R.40`, donde la misma frase **si** es cierta.

**4.b EL `81` DE `docs/plan/00_INDICE.md:644`, ADOSADO POR `9.21`.**

| celda | de donde sale | valor |
|---|---|---:|
| filas que casan con el ancla de la celda | barrido del fichero | **1**, la 644 |
| la cifra vieja que la celda publica | leida de la propia celda | **81** |
| el corte que la celda declara | leido de la propia celda | **19 ago 2026** |
| lecturas dirigidas HECHAS hoy | `vuelta48_contar_ld.py` corrido en esta vuelta, exit 0 | **82** |
| la diferencia | computada | **1** |

**LA LETRA VIEJA NO SE TOCA** y la comprobacion lo mide: `exit 0): 81**` sigue
entero en el fichero despues de escribir.

**Y LA FILA DE AL LADO NO RECIBE SU CIFRA DE HOY, Y ESO ES UNA DECISION MIA QUE
DECLARO.** *"Lecturas dirigidas encargadas y sin hacer"* publica **CERO** con su
corte, y el barrido de hoy da **8**. **Ese 8 esta contaminado**: la TAREA 2 midio
que seis de esos ocho salen de dos ficheros que ha escrito esta misma vuelta.
**Adosarlo seria meter una cifra envenenada en una pagina del plan**, que es peor
que dejar la celda vieja con su corte escrito. El instrumento tiene una guarda
que comprueba que esa fila no se toco y que el 8 no se colo. Va como `D.4`.

**LAS DIEZ COMPROBACIONES DE RELECTURA DEL DISCO PASAN, 0 FALLAN**, incluidas
*"la frase falsa sigue ENTERA en el fichero"*, *"y ahora esta TACHADA"* y *"y no
se le colo la cifra contaminada"*.

### TAREA 5. LOS TRES INSTRUMENTOS QUE FALTAN (adjudicaciones 6.6, 6.9 y 6.12)

**5.a EL ARCHIVADOR SE ENCHUFA, Y SE ENTREGO ANTES QUE EL RESTO PORQUE VIVE
DENTRO DEL ESQUELETO.** Nace `scripts/loop/paso0_archivar_anterior.py`, **con
nombre estable y sin numero de vuelta** para que el enchufe no se pierda en el
proximo clon, y `vuelta171_esqueleto_reporte.py` lo llama como **PASO 0**. **El
esqueleto se niega a escribir** si el reporte anterior no esta a salvo, y la
guarda tiene cuatro clausulas:

| clausula | que mira |
|---|---|
| (a) | el archivador no sale VERDE para la vuelta anterior |
| (b) | no existe `docs/loop/reportes/REPORTE_V<N>.md` |
| (c) | ese fichero existe pero lleva el reporte de OTRA vuelta |
| **(d)** | **el `REPORTE.md` que se va a PISAR no esta guardado byte a byte en el archivo**, cotejando los dos sha256 |

**LA (d) ES LA QUE CONVIERTE ESTO EN UNA GUARDA Y NO EN UN RECORDATORIO:** las
tres primeras se cumplen con un archivo VIEJO, y solo la cuarta mira lo que se va
a destruir.

**CASO POSITIVO POR MUTACION:**
`scripts/loop/vuelta171_tarea5a_mutacion_enchufe.py`, salida
`docs/loop/SALIDA_V171_T5A_MUTACION_ENCHUFE.txt`, **exit 0**: **10 casos, 10
pasan, 10 caen al mutar el esperado**. Tumba la guarda en sus modos (b), (c) y
(d), comprueba que **un solo byte de diferencia ya la tumba**, y corre el caso
verde contra el repo real en modo solo comprobacion, sin escribir. **Y la corrida
real lo confirmo en la 1.d**: los dos sha256 dieron `0b85f30e9c78e2b4` y el
esqueleto escribio.

**5.b EL CENSO DEL CAMPO `forma`, Y LA RESPUESTA ES QUE NO HAY VOCABULARIO.**
Instrumento `scripts/loop/vuelta171_tarea5_censo_y_barrido.py`, salida
`docs/loop/SALIDA_V171_T5BC_CENSO_Y_BARRIDO.txt`, **exit 0**. **672 entradas,
672 con `forma` no vacio, 0 sin el.** Tres varas, para no depender de una sola
forma de mirar:

**Vara (i), la CABEZA del campo: 22 cabezas distintas, y solo OCHO abren en
mayusculas.**

| cabeza | entradas |
|---|---:|
| `MEZCLADO` | 5 |
| `MEDIDO` | 3 |
| `DOS` | 2 |
| `PURO` | 2 |
| `SUB-PURO` | 2 |
| `FUNDIDA` | **1** |
| `PROVISIONAL` | 1 |
| `SIETE` | 1 |
| las otras 14 cabezas abren en minusculas | **655** (`componente` 556, `ids` 53, `defecto` 14, `figura` 13, `cribado` 10, y nueve mas con 1 cada una) |

**Vara (ii), todo token en mayusculas de 4 letras o mas en CUALQUIER sitio del
campo: 43 tokens distintos**, y la lista incluye palabras que no son formas
(`VIVOS`, `SOLO`, `TIENE`, `MISMA`, `HABLAN`).

**Vara (iii), la nomina escrita en las paginas de doctrina: NO EXISTE, y esta vez
la busqueda esta corrida y se publica.** En `docs/BANCO_DE_TEXTOS.md` y
`docs/plan/BANCO_DEL_PLAN.md`, las frases *"nomina de formas"*, *"el campo
`forma`"*, *"campo forma"*, *"formas posibles"* y *"valores de `forma`"* dan
**0 apariciones cada una en las dos paginas**.

**LO QUE EL CENSO SOSTIENE, Y NI UNA PALABRA MAS: NO HAY VOCABULARIO CERRADO
PARA EL CAMPO `forma`.** No es que `FUNDIDA` este fuera de una nomina: **es que
no hay nomina**. El campo es prosa libre en el **97,5 por ciento** de las
entradas (655 de 672 abren en minusculas). **Sube al fundador como hallazgo, que
es la rama que la `6.9` deja abierta**, y **la palabra se queda** como la propia
adjudicacion manda: describe un hecho verificado y ninguna regla escrita la
prohibe.

**Y UNA CORRECCION QUE EL CENSO OBLIGA A HACERLE AL `D.5` DE LA VUELTA 170**,
que decia que el vocabulario de la casa era *"`MEZCLADO`, `SUB-PURO`, `PARTIDO`,
`PROVISIONAL`, `REPITE`"*: medido, **`REPITE` no aparece en NINGUNA de las 672
entradas**, ni como cabeza ni como token. **La lista que se cito como vocabulario
de la casa traia una palabra que la casa no usa.** No mueve ninguna cifra
publicada; se declara y ya.

**5.c LOS 8 PARES SIN LEER: NINGUNA OPERACION LOS RECOGE, Y AHORA ESTA MEDIDO.**
Los 8 pares **no se teclean**: se computan con el resolutor delante (`P.1`) desde
los 10 miembros escritos del racimo, que colapsan a **7 vivos** (3 colapsos,
todos a `comprension_capacidades_limitaciones_ia`), **21 pares posibles, 13
leidos, 8 sin veredicto**. Los ocho, uno a uno:

| # | par |
|---:|---|
| 1 | `alineacion_etica_ia_negocio` contra `comprension_capacidades_limitaciones_ia` |
| 2 | `comprender_alineacion_etica_ia` contra `comprension_capacidades_limitaciones_ia` |
| 3 | `comprender_alineacion_etica_ia` contra `human_in_the_loop_ia` |
| 4 | `comprender_alineacion_etica_ia` contra `mitigar_falling_asleep_wheel` |
| 5 | `comprender_alineacion_etica_ia` contra `principio_humano_en_el_loop` |
| 6 | `comprender_alineacion_etica_ia` contra `riesgo_sobredependencia_ia` |
| 7 | `comprension_capacidades_limitaciones_ia` contra `mitigar_falling_asleep_wheel` |
| 8 | `comprension_capacidades_limitaciones_ia` contra `riesgo_sobredependencia_ia` |

**EL RESULTADO: 0 de los 8 pares aparece ENTERO en ninguna de las 71 fichas**, y
mas fuerte todavia, **ninguno de los 7 nodos aparece en `nodos`, `preservar`,
`eliminar` ni `superviviente` de ninguna ficha**.

**Y UN CERO SOLO VALE SI EL BARRIDO SABIA BUSCAR** (`EJECUTOR.md` 9), asi que va
con contraprueba (`docs/loop/SALIDA_V171_T5C_CONTRAPRUEBA.txt` y
`docs/loop/SALIDA_V171_T5C_BARRIDO_CORREGIDO.txt`): **los 7 ids existen en el
grafo, 7 de 7, y ninguno esta deprecado**; el barrido si encuentra fichas cuando
las hay; y el universo real de los cuatro campos son **251 ids distintos tras
resolver** de **416 valores** que resuelven a id.

**LA CONTRAPRUEBA DESTAPO ADEMAS DOS COSAS QUE MI PRIMERA PASADA NO DECIA, Y LAS
DOS SE PUBLICAN:**

1. **`comprender_alineacion_etica_ia` SI esta nombrado en una ficha**, aunque no
   en los cuatro campos operativos: en `OP-E-02.nota`, como *"el SUELTO del
   racimo de la supervision de la IA"*. O sea que **el nodo esta visto, pero no
   recogido por ninguna operacion**.
2. **El racimo, por su nombre, aparece en CINCO fichas**: `OP-F-02.evidencia`,
   `OP-E-02.nota`, `OP-L-01.verificacion`, `OP-L-02.nota` y `OP-I-01.nota`.
   **Un cero de ids no es un cero de menciones**, y decir solo lo primero habria
   sido cierto y engañoso a la vez.

**LO QUE NO DIGO, PORQUE NO LO HE MEDIDO: si son backlog nuevo.** Lo medido es
que **ninguna operacion escrita los recoge en sus campos operativos**. Ponerles
la etiqueta *backlog* es una decision de doctrina y va en `P.3`.

**Y UNA CAIDA MIA, DECLARADA CON SU NOMBRE Y CON EL TEXTO VIEJO SIN TOCAR** (va
como `CAIDA 1` de la seccion 8): mi primera version del barrido publico *"345
nodos distintos que esos cuatro campos nombran"*. **Esa cifra no es de nodos**:
`preservar` y `eliminar` guardan **prosa** ademas de ids (94 de 510 valores no
resuelven a ningun id, y `preservar` no trae **ni uno** real), y mi propio caso
de control lo destapo al imprimir como *nodo* una frase entera. **La cifra de
aciertos, 0 de 8, no se mueve** (una prosa nunca iba a ser igual a un id); lo que
cambia es lo que se puede DECIR del universo. La salida vieja se queda entera y
sin tocar.

<!-- FIN ANEXO DE TAREAS -->
