# REPORTE DE LA VUELTA 202 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta202_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA.** La
> 200 lo fue y cerro entera; `AUDITOR.md` 6.1 dice que la bateria corre **cada
> cinco vueltas**, en vuelta propia, y por esa cadencia **le toca a la 205**. Aqui
> la **seccion 9 cierra igual**, con el **HUECO DECLARADO Y MEDIDO** por el carril
> de `cerrar_reporte.py`, que lleva **su nombre, sus bytes medidos y su atribucion,
> las tres juntas, o no vale**. El bloque `I` del sello de apertura ya lo midio:
> **0 ficheros `SALIDA_V202_BATERIA_TRAMO_N.txt`** y
> **`docs/loop/SALIDA_V202_BATERIA.txt` NO EXISTE**.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026): **no se fabrican arneses, guardas ni lectores nuevos**, y **esta
> vuelta NO TIENE NINGUNA EXCEPCION**. Lo que hace falta **se importa**, y los dos
> instrumentos de `OP-L-02` se corren **sin clonarlos y sin tocarlos**. **La nomina
> queda CONGELADA EN 135**, y el bloque `F` del sello de apertura la midio contra
> ese congelado sin tocarla. **EL TRABAJO ES EL PLAN**, que es para lo que el bucle
> existe.
>
> **EL TOPE DE SUB-TAREAS ES CINCO, Y LA CIFRA QUE LO MANDA NO SE TECLEA.**
> El bloque `E` del sello de apertura de esta vuelta corrio el instrumento de la
> racha sobre el inventario ENTERO y **la racha de cierres vale 3**, con las
> vueltas **199, 200, 201**. `AUDITOR.md` 6.2 apaga el regimen temporal de dos
> sub-tareas cuando **DOS vueltas seguidas** cierran su propio reporte con
> `cerrar_reporte.py`, y con **3** **SE APAGA**. **Este encargo trae CUATRO,
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
> **LO QUE EL ACTA 201 ADJUDICO NO SE VUELVE A LEVANTAR AQUI.** Su `4.1` disuelve
> la unica parada que la 201 levanto: `OP-L-02` **si se puede medir sin decidir**,
> porque sus seis nominas viven **por id** en la constante `NOMINAS_OP_L_02`. Su
> `4.2` declara **FALSO ROJO** el `NO CUMPLIDA` de la clausula 2, porque el
> instrumento diffea contra un HEAD sellado en la vuelta 170. Y su `4.4` fija la
> convencion: **la coordenada de una ficha JSONL es LINEA MAS INDICE**, y aqui se
> usa **publicando las dos numeraciones del indice** para que ninguna cita quede
> ambigua.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina**, ni **mover
> un solo campo `estado`** (la vara del trabajo pendiente es
> `scripts/loop/vuelta150_3_relectura_expediente.py`, nunca el campo, por el
> recuadro de `AUDITOR.md` 0), ni **cerrar ninguna ficha por cuenta del ejecutor**:
> lo que estas tareas producen es **lectura medida**, y si de ella sale que una
> ficha esta cumplida, **se propone con su evidencia y lo adjudica el auditor**. **Y
> siguen fuera, nombradas para que la 203 no las redescubra:** la **reparacion del
> HEAD envejecido** de `vuelta170_tarea5b_veredicto_op_l_02.py`; el **cierre del
> turno del auditor que se reabre despues de declarar las clases**; los **dos
> arneses que el censo ve y la nomina congelada no tiene**
> (`vuelta197_tarea2_mutacion_orden_del_turno.py` y
> `vuelta199_tarea1_mutacion_guardas_revividas.py`); **las dos paradas que levanto
> la 200**; y **QUE HACER CON LAS FILAS `B` DEL ARCHIVO**. **Las tres primeras son
> de codigo y van a la auditoria integral: la moratoria las prohibe hoy.**
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor,
> y **las dos convenciones se publican**. **Y no se toca `dataset/` a mano**: el
> `numstat` de `dataset/`, `web/`, `engine/` y `docs/plan/` se mide al entrar y al
> salir y **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta202_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 201: `ebe04895`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 201: LA UNICA PARADA QUE EL REPORTE LEVANTA NO ES PARADA, Y SE DISUELVE MIDIENDO CON INSTRUMENTOS QUE YA EXISTIAN. El ejecutor cierra sus cuatro tareas con TODAS sus cifras reproducidas al digito y una sola caida, que no es de cifra.'
```
- **EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y SE MIDE EN VEZ DE
  SUPONERSE.** `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la **201**,
  y **el acta que ORDENA esta vuelta ES la 201**: el bloque `H` del sello de
  apertura conto **1 acierto para la cabecera de la 201 y 0 para la 202**. El
  `D.2` del reporte de la 184 sigue vivo como especie, y aqui **no muerde**. Lo
  que si se sigue contando, porque es cifra de inventario y envejece sola: **12 reportes archivados traen el literal
  `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`, `REPORTE_V194.md`, `REPORTE_V195.md`, `REPORTE_V196.md`, `REPORTE_V197.md`, `REPORTE_V199.md`, `REPORTE_V200.md`, `REPORTE_V201.md`), contados por `reportes_con_el_literal()`
  de este mismo fichero, **con FECHA DE CORTE 2026-09-07** (banco `9.21`, TODA
  CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Un inventario que crece cada vuelta
  sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V202_HEAD_APERTURA.txt`: `ebe04895`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `ebb8c737`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **201**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 202`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 19 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **0 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LA CORRECCION DECLARADA DE LA `evidencia` DE `OP-L-03`, EN SU SEDE, adjudicada por el acta 201 en su `4.3`. **EL CARRIL ES EL DE `OP-I-01` DE LA VUELTA 201**: banco `9.10`, **POR ADICION**, como **un elemento mas de la misma lista `evidencia`**, **sin clave nueva de esquema** y **sin tocar ni tachar el texto viejo**, que es la via de la gemela `OP-L-01` en la vuelta 166 que el **acta 71, seccion 6, adjudicacion 3** adjudico con las palabras **NO ES PARADA**. Tiene que decir **TRES cosas**: que el documento que la `evidencia` nombra trae **0** veces `reparto por acto` y **0** menciones de `OP-L-03`, **medidas aqui**; que el reparto por acto vive en `docs/plan/OP_L_03_LECTURAS.jsonl` y `docs/plan/OP_L_03_TRIANGULOS.jsonl`, **nombrados los dos** y con **sus bytes exactos** (`P.2`); y **la cobertura real con su fecha de corte**, porque la evidencia promete **55 pares en 29 actos** y el fichero trae otra cifra. **GUARDA OBLIGATORIA Y CORRIDA DOS VECES**, la misma que la 201 uso para `OP-I-01`. **NINGUN campo `estado` se mueve** | **CERRADA** | `docs/loop/SALIDA_V202_T1_CORRECCION_OP_L_03.txt`, `_IDEM.txt`, `docs/loop/SALIDA_V202_T1_GUARDA_ESTADO.txt`, `_IDEM.txt`, `docs/loop/SALIDA_V202_T1_MUTACION_GUARDA.txt`, `docs/plan/OPERACIONES.jsonl` (linea 43, elemento 4 de `evidencia`) |
| **TAREA 2** | `OP-L-02` CONTRA EL CRITERIO DE HECHO, ahora que su clausula 1 esta medida por el acta 201 en su `4.1`. **LO PRIMERO Y SIN CLONAR NADA**: se **importan** y se corren `scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py` y `scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py`, comprobado ANTES que **ninguno escribe ficheros**, y **ninguno se toca**. Las tres clausulas se miden contra el criterio de hecho de `docs/plan/08_VERIFICACION.md` **citado por linea**, y se citan por **linea 42 mas indice**. **LA CLAUSULA 2 TRAE UNA TRAMPA YA MEDIDA** (acta 201, `4.2`): el instrumento la da `NO CUMPLIDA` porque diffea contra `46208790`, un HEAD de la vuelta 170. **Se remide contra el HEAD de apertura de ESTA vuelta**, leido del sello, y **se publican las dos lecturas juntas** con la discrepancia declarada. **NO SE ARREGLA EL INSTRUMENTO: LA MORATORIA LO PROHIBE.** Si las tres quedan cumplidas, **SE PROPONE Y NO SE CIERRA** | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | `OP-L-01` CONTRA EL CRITERIO DE HECHO, Y EL HUECO DE LA VIGENCIA, adjudicada por el acta 201 en su `4.8`. Sus **cuatro pruebas de cobertura** estan cubiertas y el auditor las reprodujo las cuatro, pero **eso es PRESENCIA y no CALIDAD**. Se mide contra el criterio de hecho de `docs/plan/08_VERIFICACION.md` **citado por linea**, con su `verificacion` citada por **linea 41 mas indice**. **Y SE MIDE EL HUECO QUE LA 201 NOMBRO Y NADIE HA MEDIDO**: la **TABLA VIVA DE LOS PUROS** de `docs/BANCO_DE_TEXTOS.md` (linea **938**) declara `vigente al puesto 1157` y el marcador de hoy vale otra cosa; **las dos cifras se recuentan aqui**, y se mide **cuantas filas de esa tabla siguen en pie al corte de hoy y cuantas no**, con el **resolutor delante por `P.1`** si el conteo toca ids. **SI EL HUECO PIDE MOVER UNA CLASE, NO SE MUEVE**: mover una clase es del RECOMPUTO, se nombra y se para ahi. **PROPONE, NO CIERRA** | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LOS REGISTROS. `R.63` Y `R.64`, LAS DOS MAS VIEJAS DE LA DEUDA, adjudicada por el acta 201 en su `4.9`: la deuda son **8 actas seguidas, las 173 a 180**, y se pagan **DE LA MAS VIEJA A LA MAS NUEVA, DOS POR VUELTA**. Va **DETRAS** del trabajo de plan y nunca delante. `R.63` para el **acta 173** y `R.64` para el **acta 174**, en `docs/PENDIENTES.md`. **NINGUN LECTOR NUEVO**: los que el computo necesita **se importan**, como hizo la 201. **Cada acta se acota EN ESTA VUELTA** por linea de inicio y fin, con su reparto de adjudicaciones, hallazgos, preguntas, caidas del auditor y caidas del ejecutor. **SI EL REPORTE ARCHIVADO NO EXISTE, NO SE FABRICA**: se declara la ausencia medida con `os.path.isfile` y `os.path.getsize`, y se usa la vara que el acta 201 dejo escrita en su `4.7`. **Cierra con la serie medida**: entradas, colisiones, huecos y siguiente libre | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LA CORRECCION DECLARADA DE LA `evidencia` DE `OP-L-03`, EN SU SEDE Y POR ADICION

**ADJUDICADA POR EL ACTA 201 EN SU `4.3`.** El ejecutor de la 201 la propuso y no
la escribio sin adjudicacion; **ahora esta adjudicada y esta escrita**.

**EL CARRIL ES EL DE `OP-I-01` DE LA VUELTA 201 Y NO OTRO:** banco `9.10`, **POR
ADICION**, como **un elemento mas de la misma lista `evidencia`**, **sin clave
nueva de esquema** y **sin tocar ni tachar el texto viejo**. Es la via de la
gemela `OP-L-01` en la vuelta 166, que el **acta 71, seccion 6, adjudicacion 3**
adjudico **con las palabras NO ES PARADA**. Instrumento:
`scripts/loop/_v202_t1_correccion_op_l_03.py`, salida sellada en
`docs/loop/SALIDA_V202_T1_CORRECCION_OP_L_03.txt`.

**LA COORDENADA VA POR LINEA MAS INDICE** (acta 201, `4.4`), **y se publican las
dos numeraciones** para que ninguna cita quede ambigua: la ficha `OP-L-03` vive
en **la linea 43** de `docs/plan/OPERACIONES.jsonl`, con **1 solo acierto** de las
**71** lineas no vacias, y su `evidencia` tenia **3** elementos.

| elemento | indice base 0 | literal, citado verbatim de la ficha |
|---|---|---|
| 1 | 0 | `BANCO_DEL_PLAN.md P.5` |
| 2 | 1 | `MEDIDO el 11 ago 2026: 55 pares en 29 actos, corte puesto 2117` |
| 3 | 2 | `LECTURAS_DIRIGIDAS.md, el reparto por acto` |

#### LAS TRES COSAS OBLIGATORIAS, MEDIDAS AQUI Y NO COPIADAS DEL ENCARGO

**(1) EL DOCUMENTO QUE LA `evidencia` NOMBRA NO TRAE LO QUE PROMETE.** El
elemento **3** (indice **2**) nombra `LECTURAS_DIRIGIDAS.md`, y ese documento,
que en `docs/plan/LECTURAS_DIRIGIDAS.md` mide **214916 bytes en disco y 214916
bytes normalizados a LF** y **2230 lineas** por `count(NL)`, trae **0 apariciones
del literal `reparto por acto`** y **0 menciones de `OP-L-03`**. **LAS DOS CIFRAS
SE CONTARON AQUI.** Y la busqueda se corrio tambien **POSITIVA sobre 8
variantes**, porque `EJECUTOR.md` 9 dice que **una busqueda negativa no se puede
citar sola**: `reparto por acto`, `reparto por`, `por acto`, `OP-L-03`,
`OP_L_03`, `OP L 03`, `OP_L_03_LECTURAS` y `OP_L_03_TRIANGULOS`, **las 8 en
cero**.

**(2) DONDE VIVE DE VERDAD EL REPARTO POR ACTO, LOS DOS NOMBRADOS Y CON SUS
BYTES EXACTOS** (`P.2`: bytes exactos, nunca redondeados, KB solo entre
parentesis y detras del byte):

| fichero | bytes | filas | actos distintos | lineas no JSON |
|---|---|---|---|---|
| `docs/plan/OP_L_03_LECTURAS.jsonl` | **51368** en disco (50.2 KB) y **51368** en LF | 14 | 14 | 0 |
| `docs/plan/OP_L_03_TRIANGULOS.jsonl` | **55705** en disco (54.4 KB) y **55705** en LF | 19 | 8 | 0 |

**(3) LA COBERTURA REAL CON SU FECHA DE CORTE, QUE ES LA CIFRA QUE NO PODIA
FALTAR.** El elemento **2** promete **55 pares en 29 actos** con corte **11 ago
2026** y **puesto 2117**, leido de la propia ficha y no tecleado.
`docs/plan/OP_L_03_LECTURAS.jsonl`, recontado hoy, trae **14 actos distintos**,
de los cuales **11 tienen `leido` en true y 3 en false**, y sus campos
`cifra_pares_leidos` **suman 19 pares**. O sea: **15 de los 29 actos prometidos
siguen sin ficha de lectura** y **36 de los 55 pares prometidos siguen sin
lectura registrada**, con **fecha de corte 2026-09-07**.

**LA PROMESA VIEJA NO ES UNA MENTIRA Y NO SE RETIRA.** Con su corte era lo que se
iba a hacer. **Lo que la correccion anade es CUANTO DE ESO EXISTE HOY**, con su
propio corte, porque **una evidencia corregida que prometa mas de lo que existe
es exactamente lo que la regla LA RUTA QUE PROMETE PRUEBA ES CIFRA vino a
cazar**. La correccion escrita mide **2405 caracteres** y **0 guiones largos o
medios**.

#### LA GUARDA, CORRIDA DOS VECES Y PROBADA POR MUTACION ANTES DE PUBLICARSE

**LA GUARDA NO ES NUEVA:** es **la misma que la 201 corrio para `OP-I-01`**, y
aqui se escribe en `scripts/loop/_v202_t1_guarda_estado.py` con **prefijo de
guion bajo**, fuera del censo y fuera de la nomina, porque `EJECUTOR.md` 1 exige
que **el caso rojo se pruebe por mutacion** y para mutarla hay que poder llamarla
con datos fabricados. **EL REPO NO SE TOCA EN LA MUTACION:** los casos se
fabrican mutando las lineas **en memoria** y llamando a la funcion pura
`veredicto()`.

**LA PRUEBA DE MUTACION VA DELANTE DE LA PUBLICACION, no detras:** **6 casos** de
mutacion en `docs/loop/SALIDA_V202_T1_MUTACION_GUARDA.txt`, y **los 6 pasan**,
con el caso de control quedando **VERDE 1 de 1**. Los seis: dos lineas difieren
en vez de una; cambia una clave que no es `evidencia`; el `estado` de la ficha se
mueve; el `estado` de otra ficha se mueve; un elemento viejo de `evidencia` se
reescribe en vez de anadirse; y ninguna linea difiere.

**Y LA GUARDA SALE VERDE LAS DOS CORRIDAS**, medida contra `HEAD` con
`git show HEAD:docs/plan/OPERACIONES.jsonl`:

| lo que la guarda mide | corrida 1 | corrida 2 |
|---|---|---|
| lineas no vacias en `HEAD` y en el arbol | 71 y 71 | 71 y 71 |
| lineas que difieren | **1**, la **43** | **1**, la **43** |
| claves de esa ficha que cambian | **1**, y es `evidencia` | **1**, y es `evidencia` |
| `estado` de `OP-L-03` antes y despues | `LISTA` y `LISTA` | `LISTA` y `LISTA` |
| elementos de `evidencia` antes y despues | 3 y 4 | 3 y 4 |
| los 3 viejos identicos y en su orden | SI | SI |
| fichas de las 71 que mueven `estado` | **0** | **0** |
| veredicto | **VERDE** | **VERDE** |

Selladas en `docs/loop/SALIDA_V202_T1_GUARDA_ESTADO.txt` y
`docs/loop/SALIDA_V202_T1_GUARDA_ESTADO_IDEM.txt`.

**LA SEGUNDA CORRIDA DE LA CORRECCION SELLA CRECIMIENTO 0**, que es lo que el
encargo pide: `docs/loop/SALIDA_V202_T1_CORRECCION_OP_L_03_IDEM.txt` dice
**IDEMPOTENTE**, **4 elementos de `evidencia` al entrar** y **crecimiento en
disco 0 bytes**. **El orden de las guardas viene heredado ya arreglado de la
caida declarada de la 201**: la de idempotencia va **delante** de las de cifra,
porque la propia correccion **cita esas cifras verbatim** y una guarda de cifra
puesta delante caeria en la segunda corrida **por el motivo equivocado**.

#### LO QUE NO SE MOVIO, MEDIDO Y NO AFIRMADO

`docs/plan/OPERACIONES.jsonl` entra midiendo **499474 bytes en disco y 499474 en
LF** y sale midiendo **501883 bytes en disco y 501883 en LF**, con un
**crecimiento de 2409 bytes**; tiene **71 lineas no vacias antes y despues** y
**0 lineas que no sean JSON valido**. `git diff HEAD --numstat` da **0 filas en
`dataset/`, 0 en `web/` y 0 en `engine/`**, y en `docs/plan/` da **1 anadida y 1
borrada** en `OPERACIONES.jsonl`, que es lo que un `jsonl` da siempre al
reescribir una linea. **Y ningun veredicto se movio:**
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` mide **4054129 bytes en disco y 4054129 en
LF**, y su `sha256` vale **0a77b5a35a962621** por la convencion de disco y
**0a77b5a35a962621** por la de LF, que es el mismo valor que el sello de apertura.

<!-- FIN ANEXO DE TAREAS -->
