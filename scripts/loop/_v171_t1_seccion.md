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
