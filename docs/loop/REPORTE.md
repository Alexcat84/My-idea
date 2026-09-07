# REPORTE DE LA VUELTA 201 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta201_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA.** La
> 200 lo fue y cerro entera; `AUDITOR.md` 6.1 dice que la bateria corre **cada
> cinco vueltas**, en vuelta propia. Aqui la **seccion 9 cierra igual**, con el
> **HUECO DECLARADO Y MEDIDO** por el carril de `cerrar_reporte.py`, que lleva
> **su medicion, su atribucion y su corrida, o no vale**. El bloque `I` del sello
> de apertura ya lo midio: **0 ficheros `SALIDA_V201_BATERIA_TRAMO_N.txt`** y
> **`docs/loop/SALIDA_V201_BATERIA.txt` NO EXISTE**.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026): **no se fabrican arneses, guardas ni lectores nuevos**, y **esta
> vuelta NO TIENE NINGUNA EXCEPCION**. **La nomina queda CONGELADA EN 135**, y el
> bloque `F` del sello de apertura la midio contra ese congelado sin tocarla.
> **EL TRABAJO ES EL PLAN**, que es para lo que el bucle existe.
>
> **EL TOPE DE SUB-TAREAS VUELVE A CINCO, Y LA CIFRA QUE LO MANDA NO SE TECLEA.**
> El bloque `E` del sello de apertura de esta vuelta corrio el instrumento de la
> racha sobre el inventario ENTERO y **la racha de cierres vale 2**, con las
> vueltas **199, 200**. `AUDITOR.md` 6.2 apaga el regimen temporal de dos
> sub-tareas cuando **DOS vueltas seguidas** cierran su propio reporte con
> `cerrar_reporte.py`, y con **2** **SE APAGA**. **Este encargo trae CUATRO,
> y cabe.**
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y su bloque `F`
> publica la cifra de arneses del censo fuera de la nomina **con su vara al lado y
> las dos medidas**: con vara **148** salen **2** y sin vara salen
> **62**. **Esas son las cifras de HOY.**
>
> **LAS DOS PARADAS QUE LA 200 LEVANTO NO SE VUELVEN A LEVANTAR AQUI.** El acta
> 200 las adjudica en su `4.1` y su `4.2`: el rojo de los once tramos es **FALSO
> ROJO DE CENSO** y el bloque `F` de
> `vuelta185_tarea1c_mutacion_bateria_continuada.py` es **un arnes cuya premisa
> envejecio**. **Las dos reparaciones son de codigo y van a la auditoria integral:
> la moratoria las prohibe hoy.**
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina** (la poda se
> decide en la auditoria integral), ni **mover un solo campo `estado`** (la vara del
> trabajo pendiente es el instrumento, nunca el campo, por el recuadro de
> `AUDITOR.md` 0), ni **cerrar ninguna ficha por cuenta del ejecutor**: lo que estas
> tareas producen es **lectura medida**, y si de ella sale que una ficha esta
> cumplida, **se propone con su evidencia y lo adjudica el auditor**. **Y siguen
> fuera, nombradas para que la 202 no las redescubra:** la guarda de codigo del
> hallazgo `5.3` del acta 194; `acumulan()` que lea la tabla; el cotejo de clon
> declarado; **QUE HACER CON LAS FILAS `B` DEL ARCHIVO**; y **los puestos que dos o
> tres lectores independientes fallaron**, nombrados y medidos y **no resueltos,
> porque mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` de `dataset/`, `web/`, `engine/`
> y `docs/plan/` se mide al entrar y al salir y **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta201_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 200: `405123f1`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 200, SIN PARADA: EL EJECUTOR CIERRA CON CERO CAIDAS Y LAS DOS PARADAS QUE LEVANTA SE ADJUDICAN CON REGLA ESCRITA; LAS CUATRO CAIDAS DE ESTA ACTA SON MIAS.'
```
- **EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y SE MIDE EN VEZ DE
  SUPONERSE.** `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la **200**,
  y **el acta que ORDENA esta vuelta ES la 200**: el bloque `H` del sello de
  apertura conto **1 acierto para la cabecera de la 200 y 0 para la 201**. El
  `D.2` del reporte de la 184 sigue vivo como especie, y aqui **no muerde**. Lo
  que si se sigue contando, porque es cifra de inventario y envejece sola: **11 reportes archivados traen el literal
  `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`, `REPORTE_V194.md`, `REPORTE_V195.md`, `REPORTE_V196.md`, `REPORTE_V197.md`, `REPORTE_V199.md`, `REPORTE_V200.md`), contados por `reportes_con_el_literal()`
  de este mismo fichero, **con FECHA DE CORTE 2026-09-07** (banco `9.21`, TODA
  CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Un inventario que crece cada vuelta
  sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V201_HEAD_APERTURA.txt`: `405123f1`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `bc761e0e`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **200**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 201`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 19 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **0 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. (1.a) El **acta 200** entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, **computado y no tecleado**, y su cuerpo se acota EN ESTA VUELTA y no con las cifras del encargo. (1.b) **LA ENTRADA DE LA VUELTA 198**, por la adjudicacion `4.7` del acta 200: sigue sin entrada propia y sin reporte archivado, y su entrada **DECLARA LA AUSENCIA** con el instrumento que la midio. **NO SE FABRICA EL REPORTE.** (1.c) **UNA CORRECCION DE CITA, DE UNA LINEA, EN SU SEDE**: la seccion 8 de `docs/loop/reportes/REPORTE_V200.md` atribuye a `AUDITOR.md` 0 unas palabras que son del **acta 185**, y el aviso se anade **con el texto viejo entero y sin tachar**, por el carril del banco `9.10` mas `EJECUTOR.md` 8. **NO ES CAIDA Y NO SE COBRA.** Y **no se escribe ningun lector nuevo**: la moratoria lo prohibe | **CERRADA** | `docs/loop/SALIDA_V201_T1_REGISTROS.txt`, `docs/loop/SALIDA_V201_T1_REGISTROS_IDEM.txt`, `docs/loop/SALIDA_V201_T1C_CORRECCION_DE_CITA.txt`, `docs/PENDIENTES.md` (R.61 en la linea 15595 y R.62 en la 15681), `docs/loop/reportes/REPORTE_V200.md` (aviso en la linea 590) |
| **TAREA 2** | LA CORRECCION DECLARADA DE LA EVIDENCIA DE `OP-I-01`, adjudicada por el acta 199 en su `4.1`. La ficha promete **323** entradas y `docs/plan/INVENTARIO.jsonl` tiene otra cifra. La vieja **no es una mentira**: viaja con su fecha de corte, y lo que envejecio es la evidencia. La correccion va **EN SU SEDE**, con el texto viejo entero y sin tachar, y **las dos cifras con su fecha de corte cada una** (banco `9.21`). **NINGUNA DE LAS DOS SE TECLEA**: la del fichero se recuenta en esta vuelta y se pega su salida, la de la ficha se lee de la ficha y se cita por linea. Y se publica **el reparto por tipo recontado hoy**. **NINGUN CAMPO `estado` SE MUEVE** | **CERRADA** | `docs/loop/SALIDA_V201_T2_CORRECCION_OP_I_01.txt`, `docs/loop/SALIDA_V201_T2_CORRECCION_OP_I_01_IDEM.txt`, `docs/loop/SALIDA_V201_T2_GUARDA_ESTADO.txt`, `docs/plan/OPERACIONES.jsonl` (linea 44, elemento 4 de `evidencia`) |
| **TAREA 3** | LA MEDICION DE `OP-L-02` CONTRA SU `verificacion`, NO CONTRA SU `evidencia`, adjudicada por el acta 199 en su `4.2`. Es la unica de las cuatro fichas reales **SIN DOCUMENTO QUE MEDIR**: su evidencia entera es prosa. Se lee la ficha entera, se **cita su `verificacion` por linea**, y se responde con medicion: **que pide exactamente, que parte se puede comprobar hoy contra el repo y que parte no**. Si su `verificacion` tampoco alcanza para ejecutarla sin decidir, **eso es un hallazgo medido y va como PARADA** (`AUDITOR.md` 3), no como improvisacion | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LAS OTRAS DOS FICHAS REALES, `OP-L-01` Y `OP-L-03`, LEIDAS CONTRA SU VARA. Es el trabajo que la moratoria `6.3` manda: **EL PLAN HASTA AGOTARLO**. **LO PRIMERO: la vara se vuelve a correr AQUI** con el corte de esta vuelta y **se publican sus cifras de hoy**; si discrepan de las del encargo, **la discrepancia se declara y no se resuelve copiando** (`AUDITOR.md` 1.1). Por cada ficha: **se cita su `verificacion` por linea**, se **miden sus documentos en bytes exactos de disco y LF** (`P.2`), y se dice **si el documento cubre lo que la ficha describe**, con la cita que lo sostenga o con el hueco nombrado. **NO SE MUEVE NINGUN `estado`** y **no se cierra ninguna ficha**: lo que produce esta tarea es **lectura medida** | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1 (BLOQUEANTE): LOS REGISTROS. `R.61` Y `R.62` ESCRITAS, Y LA CORRECCION DE CITA EN SU SEDE

**LOS DOS NUMEROS SON COMPUTADOS Y NINGUNO ESTA TECLEADO.** Comando corrido en
esta vuelta, con su salida sellada en
`docs/loop/SALIDA_V201_T1_REGISTROS.txt`:

```
python scripts/loop/_v201_t1_registrar_actas.py --escribir
```

**NINGUN LECTOR NUEVO SE ESCRIBIO, QUE ES LA MITAD DEL ENCARGO BAJO LA
MORATORIA.** Los cinco que este computo usa se IMPORTAN:
`serie_de_registros.siguiente_libre()` da el numero,
`R84.claves_entrecomilladas()` lee las `4.n`, las `5.n` y las `C.An`,
`R94.caidas_propias_entrecomilladas()` las `C.n` del ejecutor,
`R92.caidas_por_lead_heredado()` corre al lado como contraste y
`R92.titulo_de_la_entrada()` compone el titulo con sus cinco numerales. El
fichero lleva **prefijo de guion bajo** y por eso queda fuera del censo y fuera
de la nomina, que sigue **congelada en 135**.

**1.a . EL ACTA 200 ENTRA COMO `R.61`.** El cuerpo se acoto **en esta vuelta** y
no con las cifras del encargo: **lineas 70230 a 70549 de
`docs/loop/ACTA_AUDITOR.md`, 320 lineas**, sobre un fichero de **4657056 bytes en
disco y 4657056 normalizados a LF**. Numerales contados de ese cuerpo: **8
adjudicaciones** (`4.1` a `4.8`), **4 hallazgos** de la seccion 5, **2 preguntas
contestadas**, **4 caidas propias del auditor** (`C.A1` a `C.A4`) y **0 caidas
del ejecutor**. **El contraste heredado se publica al lado y la discrepancia se
declara:** `R92.caidas_por_lead_heredado()` da **1 del ejecutor y 0 del auditor**
sobre el mismo cuerpo, y las cifras que la entrada publica son las de los
lectores que leen la NEGRITA QUE ABRE cada caida.

**1.b . LA VUELTA 198 ENTRA COMO `R.62`, Y SU ENTRADA DECLARA UNA AUSENCIA.**
`docs/loop/reportes/REPORTE_V198.md` **NO EXISTE**, medido en esta vuelta con
`os.path.isfile` y `os.path.getsize` desde el propio registrador y ademas por el
bloque `H` del sello de apertura. **El cero de bytes sale de que no hay fichero,
no de medir uno.** **NO SE RECONSTRUYE Y NO SE FABRICA.** Cuerpo del acta 198
acotado hoy: **lineas 69636 a 69877, 242 lineas**; **3 adjudicaciones**, **5
hallazgos**, **3 preguntas**, **2 caidas propias del auditor** y **0 del
ejecutor**.

**Y LA CONSECUENCIA DE LA AUSENCIA SE MIDE EN VEZ DE TAPARSE:** la via del
registrador de la 200 filtra las claves `P.n` de los titulos `4.n` del acta
contra la seccion de PREGUNTAS del reporte archivado. **Sin reporte no hay
filtro**, asi que el numeral de `R.62` usa **las 3 claves `P.n` nombradas en los
titulos `4.n` del acta** (`P.2`, `P.3`, `P.1`), y la entrada **lo dice** en vez
de publicar un cero que se leeria como que el acta 198 no contesto ninguna
pregunta.

**LA GUARDA DE IDEMPOTENCIA SE VOLVIO A PROBAR POR MUTACION, Y NO POR
CORTESIA:** esta vuelta escribe **DOS entradas seguidas**, que es exactamente el
escenario en que la guarda vieja de la 200 cayo. **8 casos, 8 verdes, 0 rojos**,
la guarda vieja corriendo al lado sobre los mismos textos y **discrepando en 2**,
y **los 8 CAEN al mutar el esperado**. Contado de
`docs/loop/SALIDA_V201_T1_REGISTROS.txt`.

**LA SEGUNDA CORRIDA ES LA PRUEBA DE QUE NO DUPLICA**, sellada aparte en
`docs/loop/SALIDA_V201_T1_REGISTROS_IDEM.txt`: **0 entradas escritas** y
**crecimiento 0 bytes**.

**LA SERIE, REMEDIDA AL CERRAR CON `serie_de_registros.py` Y NO HEREDADA:** **54
entradas**, **0 colisiones**, **0 huecos**, siguiente libre **`R.63`**.
`docs/PENDIENTES.md` crece por **171 lineas anadidas y 0 borradas**, contadas con
`git diff --numstat`. **La deuda de la serie baja de 9 actas a 8**: siguen sin
entrada propia las de las vueltas **173, 174, 175, 176, 177, 178, 179 y 180**.

**1.c . LA CORRECCION DE CITA, DE UNA LINEA, EN SU SEDE.** Comando corrido en
esta vuelta, sellado en `docs/loop/SALIDA_V201_T1C_CORRECCION_DE_CITA.txt`:

```
python scripts/loop/_v201_t1c_correccion_de_cita.py --escribir
```

**LAS DOS MEDICIONES QUE LA SOSTIENEN SE HICIERON AQUI Y NO SE HEREDARON, Y SI
CUALQUIERA FALLA EL COMPUTO NO ESCRIBE NADA.** El literal `se corrige es la
guarda` sale en **0 lineas** de `docs/loop/AUDITOR.md` y en **4** de
`docs/loop/ACTA_AUDITOR.md` (**64775, 65217, 70302 y 70412**); de esas, **1 cae
dentro del cuerpo del acta 185**, acotado hoy en las **lineas 64434 a 64907**, y
**por debajo de la cabecera de su punto `6.2`**, que esta en la **linea 64753**.

**EL TEXTO VIEJO SE QUEDA ENTERO Y SIN TACHAR** (banco `9.10` mas `EJECUTOR.md`
8): el aviso se ANADE detras del parrafo de la PARADA `1`. Medido con
`git diff --numstat`: **2 lineas anadidas y 0 borradas** en
`docs/loop/reportes/REPORTE_V200.md`, que pasa de **137433 bytes en disco y LF** a
**138307 bytes en disco y LF**. **NO ES CAIDA Y NO SE COBRA:** es la forma en que
la casa lo cita desde el acta 185, y lo que el aviso corrige es **de donde sale la
regla**, no la regla.

**LO QUE ESTA TAREA NO TOCA, DICHO PORQUE EL ENCARGO LO MANDA:** **las dos
paradas que la 200 levanto no se vuelven a levantar y no se arreglan.** El acta
200 las adjudica en su `4.1` y su `4.2`, **las dos reparaciones son de codigo**, y
**la moratoria `6.3` las prohibe hoy**. Van a la auditoria integral.

### TAREA 2: LA CORRECCION DECLARADA DE LA EVIDENCIA DE `OP-I-01`, EN SU SEDE

**ADJUDICADA POR EL ACTA 199 EN SU `4.1`. NO ES PARADA.** Comando corrido en esta
vuelta, con su salida sellada en
`docs/loop/SALIDA_V201_T2_CORRECCION_OP_I_01.txt`:

```
python scripts/loop/_v201_t2_correccion_op_i_01.py --escribir
```

**NINGUNA DE LAS DOS CIFRAS ESTA TECLEADA, Y CADA UNA VIAJA CON SU FECHA DE
CORTE** (banco `9.21`):

- **323 entradas, corte 2026-08-11.** No se busco a ojo: se **cita por linea**.
  Vive en la **linea 44** de `docs/plan/OPERACIONES.jsonl`, en el **elemento 1**
  de la lista `evidencia` de la ficha, verbatim `INVENTARIO.jsonl, 323 entradas`,
  y el `2026-08-11` es el `fecha_corte` de la propia ficha. El computo **cae en
  rojo si el 323 no esta en exactamente un elemento**, para que la cifra vieja no
  se elija a dedo. **El 323 aparece TAMBIEN en el campo `nota`**, y ese campo **no
  se toca**.
- **672 entradas, corte 2026-09-07.** Recontadas **en esta vuelta**, leyendo
  `docs/plan/INVENTARIO.jsonl` linea a linea y parseando cada una como JSON:
  **672 lineas no vacias**, **0 lineas que no son JSON valido**, **584554 bytes en
  disco y 584554 normalizados a LF**.

**EL REPARTO POR TIPO, RECONTADO HOY Y NO COPIADO DE NINGUNA ACTA NI DEL ACTA
199.** Contado de `docs/loop/SALIDA_V201_T2_CORRECCION_OP_I_01.txt`:

| tipo | entradas, corte 2026-09-07 |
|---|---:|
| `acto` | 556 |
| `familia_de_ids` | 54 |
| `figura` | 20 |
| `defecto` | 19 |
| `racimo` | 13 |
| `dominio` | 10 |
| **suma** | **672** |

**LA SUMA DEL REPARTO CALZA CON LAS ENTRADAS: SI.** Y **el reparto viejo (221
actos, 53 familias de ids, 14 defectos, 13 racimos, 12 figuras y 10 dominios)
sigue escrito en el campo `nota` de la ficha y no se toca**, que es lo que
significa **el texto viejo entero y sin tachar**.

**LA CIFRA VIEJA NO ES UNA MENTIRA Y NO SE RETIRA.** Con su corte era cierta. **Lo
que envejecio es la evidencia**, y por eso la correccion entra **POR ADICION**,
como un **elemento mas de la misma lista `evidencia`** y **sin clave nueva de
esquema**: es la via que la ficha gemela `OP-L-01` uso en la vuelta 166 y que el
acta 71, seccion 6, adjudicacion 3, adjudico **CON LAS PALABRAS NO ES PARADA**.

**NINGUN CAMPO `estado` SE MOVIO, Y NO SE AFIRMA: SE MIDE CONTRA `HEAD`.** Salida
sellada en `docs/loop/SALIDA_V201_T2_GUARDA_ESTADO.txt`, que sale **VERDE**: **1
sola linea difiere** de las 71 y es la **44**; de esa ficha cambia **1 sola clave**
y es `evidencia`; el `estado` de `OP-I-01` entra y sale en `LISTA`; los **3
elementos viejos siguen identicos y en su orden** y ahora son **4**; y **0 de las
71 fichas** cambian su campo `estado`. `git diff --numstat` sobre `docs/plan/`
da **1 anadida y 1 borrada** en `docs/plan/OPERACIONES.jsonl`, que es lo que
`jsonl` da siempre al reescribir una linea, y el fichero pasa de **498085 bytes en
disco y LF** a **499474 bytes en disco y LF**, con **71 lineas no vacias antes y
despues** y **0 lineas que no sean JSON valido**.

**UNA CORRECCION DE MI PROPIO COMPUTO, HECHA EN ESTA MISMA VUELTA Y DECLARADA EN
VEZ DE CALLADA.** En su primera version la guarda del 323 corria **delante** de la
de idempotencia, y la segunda corrida caia en **ROJO** diciendo *"el 323 no esta
en exactamente un elemento de `evidencia`"*. **Era cierto**, porque **la propia
correccion cita el 323 verbatim** y despues de escribirla hay **dos** elementos con
esa cifra. **No escribia nada, que es lo que se queria, pero lo decia por el motivo
equivocado**, y un instrumento que acierta por el motivo equivocado no vale. Se
reordeno, se dejo escrito dentro del fichero, y la segunda corrida esta sellada
aparte en `docs/loop/SALIDA_V201_T2_CORRECCION_OP_I_01_IDEM.txt`: **IDEMPOTENTE**,
**4 elementos de `evidencia` al entrar** y **crecimiento 0 bytes**.

<!-- FIN ANEXO DE TAREAS -->
