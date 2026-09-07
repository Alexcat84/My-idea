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
| **TAREA 3** | LA MEDICION DE `OP-L-02` CONTRA SU `verificacion`, NO CONTRA SU `evidencia`, adjudicada por el acta 199 en su `4.2`. Es la unica de las cuatro fichas reales **SIN DOCUMENTO QUE MEDIR**: su evidencia entera es prosa. Se lee la ficha entera, se **cita su `verificacion` por linea**, y se responde con medicion: **que pide exactamente, que parte se puede comprobar hoy contra el repo y que parte no**. Si su `verificacion` tampoco alcanza para ejecutarla sin decidir, **eso es un hallazgo medido y va como PARADA** (`AUDITOR.md` 3), no como improvisacion | **CERRADA CON PARADA** | `docs/loop/SALIDA_V201_T3_OP_L_02.txt` (9199 bytes), `docs/plan/OPERACIONES.jsonl` linea 42 (leida, NO tocada) |
| **TAREA 4** | LAS OTRAS DOS FICHAS REALES, `OP-L-01` Y `OP-L-03`, LEIDAS CONTRA SU VARA. Es el trabajo que la moratoria `6.3` manda: **EL PLAN HASTA AGOTARLO**. **LO PRIMERO: la vara se vuelve a correr AQUI** con el corte de esta vuelta y **se publican sus cifras de hoy**; si discrepan de las del encargo, **la discrepancia se declara y no se resuelve copiando** (`AUDITOR.md` 1.1). Por cada ficha: **se cita su `verificacion` por linea**, se **miden sus documentos en bytes exactos de disco y LF** (`P.2`), y se dice **si el documento cubre lo que la ficha describe**, con la cita que lo sostenga o con el hueco nombrado. **NO SE MUEVE NINGUN `estado`** y **no se cierra ninguna ficha**: lo que produce esta tarea es **lectura medida** | **CERRADA** | `docs/loop/SALIDA_V201_T4_VARA.txt` (17849 bytes en disco, 17565 LF), `docs/loop/SALIDA_V201_T4_LECTURA.txt` (13224 bytes en disco y LF), `docs/plan/OPERACIONES.jsonl` lineas 41 y 43 (leidas, NO tocadas) |
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

### TAREA 3: `OP-L-02` MEDIDA CONTRA SU `verificacion`. TERMINA EN PARADA, Y LA PARADA ES LA MEDICION

**ADJUDICADA POR EL ACTA 199 EN SU `4.2`.** Comando corrido en esta vuelta, con su
salida sellada en `docs/loop/SALIDA_V201_T3_OP_L_02.txt` (**9199 bytes**):

```
python scripts/loop/_v201_t3_medir_op_l_02.py
```

**POR QUE SE MIDE CONTRA `verificacion` Y NO CONTRA `evidencia`, CONTADO AQUI Y
NO HEREDADO DEL ENCARGO:** la ficha vive en la **linea 42** de
`docs/plan/OPERACIONES.jsonl`, su `evidencia` tiene **1 solo elemento**
(*"MEDIDO el 11 ago 2026: 205 pares fuera de cola, 11 leidos, 194 pendientes"*) y
de ese elemento **0 nombran un fichero**. **Sin fichero nombrado no hay documento
que medir.**

**LA `verificacion` SE CITA POR LINEA, Y LA COORDENADA VA ENTERA.** La ficha es
**una linea de JSONL**, asi que la cita es **la linea 42 mas el indice del
elemento**, y las dos van juntas. **4 elementos**:

| coordenada | que pide, verbatim |
|---|---|
| linea 42, `verificacion[1]` | `las tres nominas afectadas quedan con cobertura COMPLETA y su forma reescrita` |
| linea 42, `verificacion[2]` | `el marcador del cribado no se mueve: sigue en 2.117` |
| linea 42, `verificacion[3]` | `cada grupo del backlog lleva su motivo escrito, no solo su cuenta` |
| linea 42, `verificacion[4]` | la CORRECCION DECLARADA de la vuelta 170 sobre la clausula 2, **1486 caracteres** |

**QUE SE PUEDE COMPROBAR HOY Y QUE NO, CLAUSULA A CLAUSULA:**

- **`verificacion[1]`: NO ALCANZA PARA EJECUTAR SIN DECIDIR.** Pide **dos** cosas,
  no una: **cobertura COMPLETA** y **forma reescrita**. Y el motivo es medido, no
  opinado: la clausula escribe el numeral **`tres`**, y el campo `nota` **de esta
  misma ficha** escribe el literal **`SEIS nominas`** **1 vez** y **`TRES
  nominas`** **1 vez**. Las dos frases estan en la misma ficha, hablan de las
  mismas nominas y dan numeros distintos. **Y ninguna de las dos las nombra por
  id:** los campos `nodos`, `preservar`, `eliminar` y `superviviente` de la ficha
  miden **0, 0, 0 y `None`**. **Elegir cuales son las tres afectadas es DECIDIR,
  no medir.**
- **`verificacion[2]`: SE PUEDE MEDIR EL MARCADOR, PERO NO ES CRITERIO DE HECHO.**
  Recontado hoy, linea a linea, de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
  (**4054129 bytes en disco y 4054129 normalizados a LF**): **3388 filas**, **3388
  puestos distintos**, **maximo 3388**, **0 huecos**, y el reparto por clase **A
  551, B 72, C 5, D 2760**, que suma **3388**. **Este conteo NO pasa por el
  resolutor y se dice por que:** `P.1` lo manda para **todo conteo que toque ids**,
  y contar **puestos** no toca ninguno. Lo que la clausula pide es que **la
  operacion** no mueva el marcador, y eso solo se comprueba **corriendo la
  operacion**, que no se ha corrido. **El 3388 de hoy es un ESTADO, no el
  cumplimiento de la clausula**, y el `2.117` es **testigo y no condicion**, como
  ya dice la correccion declarada de la vuelta 170 que vive en esta misma lista.
- **`verificacion[3]`: SE COMPRUEBA HOY Y SALE CUMPLIDA.** Leido del campo `nota`
  de la propia ficha: **189 pares** de backlog en **4 grupos**, **126 esperan
  destejido**, **55 son resto sin mesa ni nomina**, **5 de sales roadmap con clase
  ya decidida** y **3 ya leidas en la primera tanda**. **La suma de los grupos da
  189 contra el total escrito 189 y CALZA**, y **los 4 de 4 llevan motivo
  escrito**.
- **`verificacion[4]`: NO ES CRITERIO.** Es la correccion por adicion de la
  clausula 2, y por eso no se mide como tal.

**LAS RUTAS QUE LA FICHA PROMETE COMO PRUEBA, MEDIDAS UNA A UNA** (`EJECUTOR.md`
1, LA RUTA QUE PROMETE PRUEBA ES CIFRA): **8 rutas distintas**, **8 vivas**, **0
inexistentes** y **0 de cero bytes**. Ninguna caida de cifra por ahi.

**LA CORRECCION DE MI PROPIO COMPUTO, DECLARADA Y NO TAPADA.** La primera version
del lector del backlog casaba `(\d+)\s+(.*)` contra cada trozo separado por coma,
y **el cuarto grupo de la `nota` empieza por `y 3 ya leidas...`**: el patron no
casaba, la cuenta salia 0, el motivo salia vacio, y este computo publicaba **`3 de
4 grupos con motivo`** y **`186 contra 189, NO CALZA`**. **La ficha estaba bien y
el lector estaba mal.** Se quita la conjuncion antes de leer la cifra, queda
escrito dentro del fichero, y **con el arreglo salen 4 de 4 y 189 contra 189**.

**Y LO QUE ESTA TAREA NO HIZO:** no movio ningun `estado` (la ficha entra y sale en
`LISTA`), no cerro la ficha, no adjudico ninguna clase, no toco ni un veredicto,
**no escribio una sola linea en `docs/plan/`** y no ejecuto la operacion.

> **PARADA `1` DE ESTA VUELTA, Y NO LA ARREGLO YO.** `OP-L-02` **no se puede
> ejecutar hoy sin decidir**, por su `verificacion[1]`: su propio texto da **tres**
> y **seis** para las mismas nominas y **no las nombra por id en ningun sitio**.
> `AUDITOR.md` 3 dice que una operacion cuyo texto no alcanza para ejecutarse sin
> decidir **es PARADA, no una improvisacion**. **No la improviso y no la declaro
> hecha.** Lo que hace falta para desbloquearla es una sola decision escrita:
> **cuales son las nominas afectadas, nombradas por id**, y si son **tres** o
> **seis**. **Esa decision no es mia.**

### TAREA 4: `OP-L-01` Y `OP-L-03`, LEIDAS CONTRA SU VARA. LECTURA MEDIDA, SIN MOVER NADA

**LO PRIMERO Y SIN SALTARSELO: LA VARA CORRIDA POR MI, CON EL CORTE DE ESTA
VUELTA.** El corte es **el HEAD de apertura**, `405123f1`, leido del sello
`docs/loop/SALIDA_V201_HEAD_APERTURA.txt` y no tecleado. **La vara no se clona y
no se toca: se invoca.** Salidas selladas en `docs/loop/SALIDA_V201_T4_VARA.txt`
(**17849 bytes en disco y 17565 normalizados a LF**, y las dos van porque la
convencion sigue sin fijar) y `docs/loop/SALIDA_V201_T4_LECTURA.txt` (**13224
bytes en disco y 13224 normalizados a LF**).

```
python scripts/loop/_v201_t4_leer_op_l_01_y_03.py --corte 405123f1b49cde57f4ce4f05a1d1cd5ab4d7e065
```

**LAS CIFRAS DE HOY, LEIDAS DE SU SALIDA Y CONTRASTADAS UNA A UNA CON LAS DEL
ENCARGO.** Exitcode **0**. Contado de `docs/loop/SALIDA_V201_T4_VARA.txt`:

| cifra de la vara | encargo | hoy | veredicto |
|---|---:|---:|---|
| fichas del expediente | 71 | 71 | CALZA |
| fichas que no calzan | 37 | 37 | CALZA |
| fichas en LISTA sin ninguna prueba | 6 | 6 | CALZA |
| de esas, TRABAJO REAL | 4 | 4 | CALZA |
| de esas, CONSUMIDAS por otra ficha | 2 | 2 | CALZA |

**CIFRA cifras del encargo que discrepan de las de hoy: 0.** Y las que el encargo
no trae y la vara si publica, para que la tabla no se lea como si fueran todas:
**24 congeladas declaradas**, **12 congeladas en silencio**, **1 HECHA sin ninguna
prueba**, **6 fichas de tipo MESA** de las cuales **5 en LISTA**.

**LA PRUEBA DE COBERTURA VA DECLARADA ANTES DE CORRERSE**, en la constante
`PRUEBAS` del propio fichero, **para que la aguja no se elija despues de mirar**. Y
**es prueba de PRESENCIA de lo que la ficha dice que hay, no de calidad de la
mesa**, que es exactamente lo que la propia vara advierte y aqui no se mejora.

#### `OP-L-01`, LINEA 41. LOS TRES DOCUMENTOS CUBREN LO QUE LA FICHA DESCRIBE

`estado` **LISTA** (leido, no movido), `fecha_corte` **2026-08-11**, tipo **MESA**,
`depende_de` **vacio**, y `nodos`, `preservar`, `eliminar` y `superviviente` en
**0, 0, 0 y `None`**.

**SU `verificacion`, CITADA POR LINEA.** La ficha es **una linea de JSONL**, asi que
la coordenada es **la linea 41 mas el indice**, y las dos van juntas. **6
elementos**: `verificacion[1]` (78 caracteres), `[2]` (51), `[3]` (69), y
`[4]`, `[5]` y `[6]` son **CORRECCIONES DECLARADAS POR ADICION** de **3326, 1993 y
2376 caracteres**, escritas por las vueltas 166 y 169.

| evidencia | documento | disco | LF | que se busco | aciertos | veredicto |
|---|---|---:|---:|---|---:|---|
| `[1]` | `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 | las cabeceras `LD-01` a `LD-11` | 11 | CUBIERTA |
| `[1]` | `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 | la cabecera `LAS ONCE, una por una` | 1 | CUBIERTA |
| `[2]` | `docs/INTRA_DOMINIO_INFORME.md` | 943970 | 943970 | la seccion 52 con su titulo entero | 1 | CUBIERTA |
| `[3]` | `docs/BANCO_DE_TEXTOS.md` | 182228 | 182228 | `TABLA VIVA DE LOS PUROS` | 1 | CUBIERTA |

**LAS CITAS QUE LO SOSTIENEN, pegadas de su linea:** la **74** de
`LECTURAS_DIRIGIDAS.md` dice `## LAS ONCE, una por una` y detras van las once, de
la **76** a la **268**; la **10055** de `INTRA_DOMINIO_INFORME.md` dice `## 52. LAS
PAREJAS QUE EL EJERCICIO NO PUEDE CERRAR`, **palabra por palabra lo que la
`evidencia` promete**; y la **938** de `BANCO_DE_TEXTOS.md` dice `#### TABLA VIVA DE
LOS PUROS, al 14 ago 2026 (vigente al puesto 1157)`.

**Y LO QUE ESA TERCERA CITA TRAE DENTRO SE NOMBRA EN VEZ DE PASARSE POR ALTO:** su
propio titulo declara vigencia **al puesto 1157**, y el marcador del cribado
recontado en la TAREA 3 de esta misma vuelta vale **3388**. **La tabla existe y
cubre la presencia que la ficha promete; su corte es viejo, y eso es una medicion,
no una acusacion.** `[4]` es prosa y no nombra fichero: por esa via no hay
documento que medir.

**CIFRA pruebas de cobertura de `OP-L-01`: 4 CUBIERTAS y 0 NO CUBIERTAS.**

#### `OP-L-03`, LINEA 43. UNO CUBRE, Y EL HUECO NO ES QUE FALTE EL TRABAJO

`estado` **LISTA** (leido, no movido), `fecha_corte` **2026-08-11**, tipo **MESA**,
`depende_de` **`OP-D-01` a `OP-D-06`**, y `nodos`, `preservar`, `eliminar` y
`superviviente` en **0, 0, 0 y `None`**.

**SU `verificacion`, CITADA POR LINEA (linea 43 mas indice). 4 elementos:**
`[1]` (53 caracteres), `[2]` (85), `[3]` (83), y `[4]` es una **CORRECCION
DECLARADA POR ADICION de 3455 caracteres**, escrita por la vuelta 72.

| evidencia | documento | disco | LF | que se busco | aciertos | veredicto |
|---|---|---:|---:|---|---:|---|
| `[1]` | `docs/plan/BANCO_DEL_PLAN.md` | 61554 | 61554 | la cabecera `P.5` | 1 | CUBIERTA |
| `[3]` | `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 | el literal `reparto por acto` | 0 | NO CUBIERTA |
| `[3]` | `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 | el propio `OP-L-03` nombrado en el documento | 0 | NO CUBIERTA |

**LA CITA QUE SOSTIENE LA CUBIERTA:** la linea **239** de `BANCO_DEL_PLAN.md` dice
`## P.5 REGLA DE ORDEN: CADA ACTO QUE VAYA A FUNDIRSE SE LEE ENTERO`.

**EL HUECO VA NOMBRADO, Y MEDIDO HASTA EL FINAL EN VEZ DE DEJARLO EN NO CUBIERTA.**
Una busqueda negativa no se puede citar sin haberla corrido (`EJECUTOR.md` 9), asi
que **se corrio tambien la positiva**: hay **2 ficheros `docs/plan/OP_L_03_*` en
disco**, `OP_L_03_LECTURAS.jsonl` (**51368 bytes en disco y LF**, **14 filas no
vacias**, **0 lineas no JSON**, **14 valores distintos del campo `acto`**) y
`OP_L_03_TRIANGULOS.jsonl` (**55705 bytes en disco y LF**, **19 filas**, **0 lineas
no JSON**, **8 valores distintos del campo `acto`**). **La `evidencia` de la ficha
no nombra ninguno de los dos.**

> **LA FRASE ENTERA, Y LAS DOS MITADES SE MIDEN: el documento que la `evidencia` de
> `OP-L-03` NOMBRA no trae ni el literal `reparto por acto` ni una sola mencion de
> `OP-L-03`; y los ficheros que SI traen un reparto por acto de esta ficha EXISTEN
> en disco y su `evidencia` NO LOS NOMBRA. EL HUECO NO ES QUE FALTE EL TRABAJO: ES
> QUE LA EVIDENCIA APUNTA AL DOCUMENTO EQUIVOCADO.**

**CIFRA pruebas de cobertura de `OP-L-03`: 1 CUBIERTA y 2 NO CUBIERTAS.**

#### LO QUE SE PROPONE Y LO QUE NO SE DECIDE

**NO SE MOVIO NINGUN `estado`, NO SE CERRO NINGUNA FICHA, no se adjudico ninguna
clase, no se toco ni un nodo ni un veredicto y NO SE ESCRIBIO UNA SOLA LINEA EN
`docs/plan/` en esta tarea.** Lo que produce es **lectura medida**. Y de ella salen
**dos propuestas**, que **propongo con su evidencia y adjudica el auditor**:

1. **`OP-L-01`:** sus **tres documentos existen y cubren la presencia que su
   `evidencia` promete**, 4 pruebas de 4. **Eso NO dice que su mesa se hiciera
   bien**, y por eso no la cierro: **propongo que se mire si el criterio de HECHO
   de `docs/plan/08_VERIFICACION.md` se da**, y **el corte del puesto 1157 de la
   TABLA VIVA queda nombrado** como lo que habria que remirar.
2. **`OP-L-03`:** propongo **una correccion declarada de su `evidencia`**, del
   mismo carril que la que esta vuelta escribio para `OP-I-01`, **que nombre
   `docs/plan/OP_L_03_LECTURAS.jsonl` y `docs/plan/OP_L_03_TRIANGULOS.jsonl`**, que
   existen y traen el reparto por acto. **No la escribo yo en esta vuelta**: el
   encargo manda **lectura medida** para esta tarea, y una correccion en su sede es
   escritura en `docs/plan/` que nadie me adjudico aqui.

<!-- FIN ANEXO DE TAREAS -->
