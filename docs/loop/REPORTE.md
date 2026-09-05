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
| **TAREA 4** | LAS DOS DEUDAS DE REGISTRO (adjudicaciones 6.4 y 6.11): 4.a el agujero del `R.38` corregido por el carril del `9.10` con la frase vieja entera y tachada, 4.b el `81` de `docs/plan/00_INDICE.md:644` con la cifra de hoy adosada por `9.21` y sin tocar la letra vieja | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LOS TRES INSTRUMENTOS QUE FALTAN (adjudicaciones 6.6, 6.9 y 6.12): 5.a el archivador ENCHUFADO como paso 0 del esqueleto, 5.b el CENSO del campo `forma` sobre las 672 entradas del inventario, 5.c el barrido MEDIDO de los 8 pares sin leer de `la supervision de la IA` sobre las 71 fichas | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
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

<!-- FIN ANEXO DE TAREAS -->
