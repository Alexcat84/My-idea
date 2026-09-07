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

**EL VEREDICTO DE UNA LINEA: LA VUELTA 202 CIERRA SUS CUATRO TAREAS CON TODAS SUS CIFRAS SALIDAS DE INSTRUMENTOS CORRIDOS HOY, CON UNA SOLA PARADA QUE ES DE MEDICION Y NO DE CODIGO, y las TRES CAIDAS que cometi van con su nombre y las tres se cazaron ANTES de publicarse.**
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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 202`, y su salida
cruda vive en `docs/loop/SALIDA_V202_TALLADOR_CABECERA.txt` (2513 bytes en disco y 2493 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `ebe04895` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 201: LA UNICA PARADA QUE EL REPORTE LEVANTA NO ES PARADA, Y SE DISUELVE MIDIENDO CON INSTRUMENTOS QUE YA EXISTIAN. El ejecutor cierra sus cuatro tareas con TODAS sus cifras reproducidas al digito y una sola caida, que no es de cifra.'), HEAD real de apertura `ebe04895` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `9b29f754` (leido de `SALIDA_V202_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LA CORRECCION DECLARADA DE LA `evidencia` DE `OP-L-03`, EN SU SEDE, adjudicada por el acta 201 en su `4.3`. **EL CARRIL ES EL DE `OP-I-01` DE LA VUELTA 201**: banco `9.10`, **POR ADICION**, como **un elemento mas de la misma lista `evidencia`**, **sin clave nueva de esquema** y **sin tocar ni tachar el texto viejo**, que es la via de la gemela `OP-L-01` en la vuelta 166 que el **acta 71, seccion 6, adjudicacion 3** adjudico con las palabras **NO ES PARADA**. Tiene que decir **TRES cosas**: que el documento que la `evidencia` nombra trae **0** veces `reparto por acto` y **0** menciones de `OP-L-03`, **medidas aqui**; que el reparto por acto vive en `docs/plan/OP_L_03_LECTURAS.jsonl` y `docs/plan/OP_L_03_TRIANGULOS.jsonl`, **nombrados los dos** y con **sus bytes exactos** (`P.2`); y **la cobertura real con su fecha de corte**, porque la evidencia promete **55 pares en 29 actos** y el fichero trae otra cifra. **GUARDA OBLIGATORIA Y CORRIDA DOS VECES**, la misma que la 201 uso para `OP-I-01`. **NINGUN campo `estado` se mueve** | **CERRADA** | `docs/loop/SALIDA_V202_T1_CORRECCION_OP_L_03.txt`, `_IDEM.txt`, `docs/loop/SALIDA_V202_T1_GUARDA_ESTADO.txt`, `_IDEM.txt`, `docs/loop/SALIDA_V202_T1_MUTACION_GUARDA.txt`, `docs/plan/OPERACIONES.jsonl` (linea 43, elemento 4 de `evidencia`) |
| **TAREA 2** | `OP-L-02` CONTRA EL CRITERIO DE HECHO, ahora que su clausula 1 esta medida por el acta 201 en su `4.1`. **LO PRIMERO Y SIN CLONAR NADA**: se **importan** y se corren `scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py` y `scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py`, comprobado ANTES que **ninguno escribe ficheros**, y **ninguno se toca**. Las tres clausulas se miden contra el criterio de hecho de `docs/plan/08_VERIFICACION.md` **citado por linea**, y se citan por **linea 42 mas indice**. **LA CLAUSULA 2 TRAE UNA TRAMPA YA MEDIDA** (acta 201, `4.2`): el instrumento la da `NO CUMPLIDA` porque diffea contra `46208790`, un HEAD de la vuelta 170. **Se remide contra el HEAD de apertura de ESTA vuelta**, leido del sello, y **se publican las dos lecturas juntas** con la discrepancia declarada. **NO SE ARREGLA EL INSTRUMENTO: LA MORATORIA LO PROHIBE.** Si las tres quedan cumplidas, **SE PROPONE Y NO SE CIERRA** | **CERRADA COMO LECTURA MEDIDA. PROPUESTA, NO CIERRE** | `docs/loop/SALIDA_V202_T2_COBERTURA_169.txt`, `docs/loop/SALIDA_V202_T2_VEREDICTO_170.txt`, `docs/loop/SALIDA_V202_T2_OP_L_02.txt`, `docs/plan/OPERACIONES.jsonl` (linea 42) |
| **TAREA 3** | `OP-L-01` CONTRA EL CRITERIO DE HECHO, Y EL HUECO DE LA VIGENCIA, adjudicada por el acta 201 en su `4.8`. Sus **cuatro pruebas de cobertura** estan cubiertas y el auditor las reprodujo las cuatro, pero **eso es PRESENCIA y no CALIDAD**. Se mide contra el criterio de hecho de `docs/plan/08_VERIFICACION.md` **citado por linea**, con su `verificacion` citada por **linea 41 mas indice**. **Y SE MIDE EL HUECO QUE LA 201 NOMBRO Y NADIE HA MEDIDO**: la **TABLA VIVA DE LOS PUROS** de `docs/BANCO_DE_TEXTOS.md` (linea **938**) declara `vigente al puesto 1157` y el marcador de hoy vale otra cosa; **las dos cifras se recuentan aqui**, y se mide **cuantas filas de esa tabla siguen en pie al corte de hoy y cuantas no**, con el **resolutor delante por `P.1`** si el conteo toca ids. **SI EL HUECO PIDE MOVER UNA CLASE, NO SE MUEVE**: mover una clase es del RECOMPUTO, se nombra y se para ahi. **PROPONE, NO CIERRA** | **CERRADA COMO LECTURA MEDIDA. DOS PROPUESTAS, NINGUN CIERRE** | `docs/loop/SALIDA_V202_T3_CLAUSULAS_12_166.txt`, `docs/loop/SALIDA_V202_T3_CLAUSULA_3_169.txt`, `docs/loop/SALIDA_V202_T3_OP_L_01.txt`, `docs/plan/OPERACIONES.jsonl` (linea 41), `docs/BANCO_DE_TEXTOS.md` (linea 938) |
| **TAREA 4** | LOS REGISTROS. `R.63` Y `R.64`, LAS DOS MAS VIEJAS DE LA DEUDA, adjudicada por el acta 201 en su `4.9`: la deuda son **8 actas seguidas, las 173 a 180**, y se pagan **DE LA MAS VIEJA A LA MAS NUEVA, DOS POR VUELTA**. Va **DETRAS** del trabajo de plan y nunca delante. `R.63` para el **acta 173** y `R.64` para el **acta 174**, en `docs/PENDIENTES.md`. **NINGUN LECTOR NUEVO**: los que el computo necesita **se importan**, como hizo la 201. **Cada acta se acota EN ESTA VUELTA** por linea de inicio y fin, con su reparto de adjudicaciones, hallazgos, preguntas, caidas del auditor y caidas del ejecutor. **SI EL REPORTE ARCHIVADO NO EXISTE, NO SE FABRICA**: se declara la ausencia medida con `os.path.isfile` y `os.path.getsize`, y se usa la vara que el acta 201 dejo escrita en su `4.7`. **Cierra con la serie medida**: entradas, colisiones, huecos y siguiente libre | **CERRADA, CON UNA PARADA DE MEDICION DECLARADA** | `docs/loop/SALIDA_V202_T4_REGISTROS.txt`, `docs/loop/SALIDA_V202_T4_REGISTROS_IDEM.txt`, `docs/PENDIENTES.md` (lineas 15766 y 15865) |
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
que en `docs/plan/LECTURAS_DIRIGIDAS.md` mide **214916 bytes en disco y 214916 bytes normalizados a LF** y **2230 lineas** por `count(NL)`, trae **0 apariciones
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
**IDEMPOTENTE**, **4 elementos de `evidencia` al entrar** y **crecimiento de 0 bytes en disco y de 0 bytes normalizados a LF**. **El orden de las guardas viene heredado ya arreglado de la
caida declarada de la 201**: la de idempotencia va **delante** de las de cifra,
porque la propia correccion **cita esas cifras verbatim** y una guarda de cifra
puesta delante caeria en la segunda corrida **por el motivo equivocado**.

#### LO QUE NO SE MOVIO, MEDIDO Y NO AFIRMADO

`docs/plan/OPERACIONES.jsonl` mide AL SALIR **501883 bytes en disco y 501883 bytes normalizados a LF**, y ANTES de esta correccion media **499474 bytes en disco y 499474 bytes normalizados a LF**, con un **crecimiento de 2409 bytes en disco y de 2409 bytes normalizados a LF**; tiene **71 lineas no vacias antes y despues** y
**0 lineas que no sean JSON valido**. `git diff HEAD --numstat` da **0 filas en
`dataset/`, 0 en `web/` y 0 en `engine/`**, y en `docs/plan/` da **1 anadida y 1
borrada** en `OPERACIONES.jsonl`, que es lo que un `jsonl` da siempre al
reescribir una linea. **Y ningun veredicto se movio:**
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` mide **4054129 bytes en disco y 4054129 bytes normalizados a LF**, y su `sha256` vale **0a77b5a35a962621** por la convencion de disco y **0a77b5a35a962621** por la de LF, que es el mismo valor que el sello de apertura.

### TAREA 2. `OP-L-02` CONTRA EL CRITERIO DE HECHO. SE PROPONE Y NO SE CIERRA

**LO PRIMERO, Y SIN CLONAR NADA.** Los dos instrumentos se **importaron y se
corrieron tal cual**, y **ninguno se toco**: `scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py`
mide **9310 bytes en disco y 9310 bytes normalizados a LF**, y
`scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py` mide **13487 bytes en disco y 13487 bytes normalizados a LF**. **Se comprobo ANTES de correrlos que ninguno
escribe ficheros**: **0 lineas con marca de escritura en disco** en cada uno, y
despues de correrlos **0 lineas de `git status` que no sean salidas de esta
tarea**. Selladas con nombre de esta vuelta en
`docs/loop/SALIDA_V202_T2_COBERTURA_169.txt` (**5559 bytes en disco y 5449 bytes normalizados a LF**) y `docs/loop/SALIDA_V202_T2_VEREDICTO_170.txt` (**5880 bytes en disco y 5789 bytes normalizados a LF**). La lectura entera vive en `docs/loop/SALIDA_V202_T2_OP_L_02.txt`.

#### EL CRITERIO DE HECHO, CITADO POR LINEA

`docs/plan/08_VERIFICACION.md` mide **69068 bytes en disco y 69068 bytes
normalizados a LF** y trae **913 lineas**. Su cabecera esta en la **linea 7**, con
**1 solo acierto**, y el criterio, verbatim:

- **linea 9**: *UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE CAERIA SI EL FALLO
  VOLVIERA.*
- **linea 11**: *No cuando pasa verde: cuando se CAERIA.*
- **lineas 13 a 15**: *Es el criterio del CASO POSITIVO de la FASE 0, aplicado a
  todo el plan. Y tiene una comprobacion barata: correr la prueba ANTES del
  arreglo. Si pasa, no prueba nada.*

Y en ese mismo documento `OP-L-02` se nombra en **1 sola linea, la 409**, que
dice *"DECISION PENDIENTE"* y *"el universo de 205 se remide"*. **Esa fila es del
apartado del recomputo y no es la verificacion de la ficha**, que es lo que aqui
se mide.

#### LAS TRES CLAUSULAS, CITADAS POR LINEA MAS INDICE

La ficha vive en la **linea 42** de `docs/plan/OPERACIONES.jsonl`, con **1 solo
acierto**. Su `verificacion` tiene **4 elementos**, de los cuales **3 son
clausulas** y **1 es una CORRECCION DECLARADA**, que no es una clausula que
cumplir. Su `evidencia` tiene **1 elemento**.

| coordenada | caracteres | literal |
|---|---:|---|
| linea 42 + indice 0 (elemento 1) | 77 | `las tres nominas afectadas quedan con cobertura COMPLETA y su forma reescrita` |
| linea 42 + indice 1 (elemento 2) | 51 | `el marcador del cribado no se mueve: sigue en 2.117` |
| linea 42 + indice 2 (elemento 3) | 65 | `cada grupo del backlog lleva su motivo escrito, no solo su cuenta` |
| linea 42 + indice 3 (elemento 4) | 1486 | CORRECCION DECLARADA, no es clausula |

**LA PARADA DE LA 201 NO SE VUELVE A LEVANTAR**, porque el acta 201 la disolvio en
su `4.1`: la clausula 1 **si se puede medir sin decidir**, y el instrumento la
mide. Sus seis nominas viven **por id** en la constante `NOMINAS_OP_L_02`, y su
salida de hoy da **6 nominas parseadas** y **0 pares SIN veredicto** en las seis.

#### LOS VEREDICTOS, LEIDOS DE LA SELLADA Y NO TECLEADOS

| clausula | veredicto del instrumento | de donde sale la cifra |
|---|---|---|
| 1, cobertura completa y forma reescrita | **CUMPLIDA** | **0** pares sin veredicto en las seis nominas; las tres nominas con su `forma` reescrita y el corte dentro |
| 2, el marcador no se mueve | **NO CUMPLIDA** | **1** fila de `numstat`, y esa es la trampa que se remide abajo |
| 3, cada grupo con su motivo | **CUMPLIDA** | **4** grupos del backlog y **0** sin motivo escrito |

**CIFRA clausulas cumplidas segun el instrumento, tal cual se corrio: 2 de 3.**

#### LA CLAUSULA 2, REMEDIDA. LAS DOS LECTURAS JUNTAS Y LA DISCREPANCIA DECLARADA

**LOS DOS HEAD SE LEEN DE SU SELLO Y NINGUNO SE TECLEA.** El instrumento lee
`docs/loop/SALIDA_V170_HEAD_APERTURA.txt`, que dice **`46208790`**; esta vuelta
lee su propio `docs/loop/SALIDA_V202_HEAD_APERTURA.txt`, que dice **`ebe04895`**.

| lectura | comando | filas de `numstat` | sin commitear | veredicto |
|---|---|---:|---:|---|
| la del instrumento | `git diff 46208790 HEAD --numstat -- docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **1** | 0 | **NO CUMPLIDA** |
| la de esta vuelta | `git diff ebe04895 HEAD --numstat -- docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **0** | 0 | **CUMPLIDA** |

**LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO.** El acta 201 ya la
adjudico en su `4.2`: es **FALSO ROJO**, porque el instrumento diffea contra un
HEAD sellado en la vuelta **170** y desde entonces han pasado vueltas que **si**
movieron el fichero. **Su reparacion es de codigo, la moratoria la prohibe hoy y
va a la auditoria integral. AQUI NO SE ARREGLA.**

**EL MARCADOR, RECONTADO AQUI Y NO COPIADO:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
mide **4054129 bytes en disco y 4054129 bytes normalizados a LF**, con **3388
filas no vacias**, **0 lineas que no sean JSON valido**, reparto **A 551, B 72, C
5 y D 2760** que **suma 3388**, **3388 puestos distintos**, **maximo 3388** y **0
huecos**. **NO PASA POR EL RESOLUTOR, Y ESO SE DICE EN VEZ DE CALLARLO:** `P.1`
manda pasar por el resolutor todo conteo que **toque ids**, y contar filas, clases
y puestos **no toca ninguno**. **La clausula pide que la OPERACION no lo mueva, no
que valga 2.117 hoy**, y su propia CORRECCION DECLARADA lo dice: el 2.117 es el
valor en la `fecha_corte` de la ficha, **testigo y no condicion**.

#### EL CRITERIO DE HECHO APLICADO: LOS TRES VEREDICTOS SE PUEDEN CAER

El criterio pide que **la verificacion se caeria si el fallo volviera**, y trae su
propia comprobacion barata. Aqui se comprueba **leyendo el codigo del instrumento
y sin tocarlo** que cada veredicto sale de **una expresion computada y no de un
literal**, que es lo que `EJECUTOR.md` 1 llama **un caso rojo que no puede
fallar**:

| clausula | linea de `vuelta170_tarea5b_veredicto_op_l_02.py` | asignacion | sale de un literal |
|---|---:|---|---|
| 1 | 166 | `cumple1 = (sin_total == 0 and con_corte == len(LAS_TRES))` | **NO** |
| 2 | 195 | `cumple2 = (len(filas) == 0 and len(filas2) == 0)` | **NO** |
| 3 | 222 | `cumple3 = (len(grupos) > 0 and not sin_motivo)` | **NO** |

**Las tres se caerian**: si un par de las seis nominas perdiera su veredicto,
`sin_total` dejaria de ser 0; si la operacion moviera el archivo, el `numstat`
dejaria de ser 0; si un grupo del backlog perdiera su motivo, `sin_motivo` dejaria
de estar vacio.

#### LA PROPUESTA, QUE NO CIERRA NADA

**CON LA CLAUSULA 2 REMEDIDA CONTRA EL HEAD DE ESTA VUELTA, LAS TRES QUEDAN
CUMPLIDAS: 3 de 3.** **Y AUN ASI NO SE CIERRA.** El encargo dice **PROPONLO Y NO
LO CIERRES**, y `AUDITOR.md` 0 dice que **el campo `estado` no es la vara**. El
`estado` de `OP-L-02` **entra y sale en `LISTA`**, y este computo cambia **0
lineas** de `docs/plan/OPERACIONES.jsonl`.

**LA EVIDENCIA DE LA PROPUESTA, ENTERA:** `docs/loop/SALIDA_V202_T2_COBERTURA_169.txt`,
`docs/loop/SALIDA_V202_T2_VEREDICTO_170.txt` y
`docs/loop/SALIDA_V202_T2_OP_L_02.txt`, mas la ficha en la **linea 42** de
`docs/plan/OPERACIONES.jsonl`. **Lo adjudica el auditor.**

**DISCUTIBLE, MARCADO ANTES DE SABER SI ACIERTO:** la propuesta descansa en una
lectura de la clausula 2 que **el instrumento de la casa da como NO CUMPLIDA**. Yo
sostengo que el 0 contra `ebe04895` es la lectura correcta **porque la clausula
pide que la operacion no mueva el archivo y la operacion es esta vuelta**, y el
acta 201 ya llamo falso rojo al otro. **Pero quien decide si una clausula se puede
dar por cumplida contra una vara distinta de la que el instrumento usa no soy yo.**

### TAREA 3. `OP-L-01` CONTRA EL CRITERIO DE HECHO, Y EL HUECO DE LA VIGENCIA MEDIDO

**ADJUDICADA POR EL ACTA 201 EN SU `4.8`.** Sus **cuatro pruebas de cobertura
estan cubiertas** y el auditor las reprodujo las cuatro. **Eso es PRESENCIA, no
CALIDAD**, y por eso no se cierra. **Esta tarea mide la CALIDAD**, y lo que
encuentra no estaba medido.

**LOS DOS INSTRUMENTOS SE IMPORTARON Y SE CORRIERON EN MODO MEDICION, SIN
`--aplicar`**, y **ninguno se toco**: `scripts/loop/vuelta166_tarea2_correccion_op_l_01.py`
para las clausulas 1 y 2, y `scripts/loop/vuelta169_tarea4_op_l_01_clausula3.py`
para la 3. **El `sha256` de `docs/plan/OPERACIONES.jsonl` entra y sale igual en
las dos corridas**, medido antes y despues: `6006fd16dc08dc58` las dos veces.
Selladas en `docs/loop/SALIDA_V202_T3_CLAUSULAS_12_166.txt` (**32943 bytes en disco y 32684 bytes normalizados a LF**) y `docs/loop/SALIDA_V202_T3_CLAUSULA_3_169.txt` (**4028 bytes en disco y 3963 bytes normalizados a LF**). La lectura entera esta en
`docs/loop/SALIDA_V202_T3_OP_L_01.txt`.

#### EL CRITERIO DE HECHO Y LA `verificacion`, CITADOS POR LINEA

El criterio vive en `docs/plan/08_VERIFICACION.md`, cabecera en la **linea 7**
con **1 solo acierto**, literal en las **lineas 9 y 11**, y su comprobacion barata
en las **13 a 15**. **Y en ese documento `OP-L-01` no se nombra ni una sola vez:
0 lineas.** Eso se dice en vez de callarse: **el criterio que se le aplica es el
general, no una fila suya.**

La ficha vive en la **linea 41** de `docs/plan/OPERACIONES.jsonl`, con **1 solo
acierto**. Su `verificacion` tiene **6 elementos**: **3 clausulas** y **3
CORRECCIONES DECLARADAS**, que no son clausulas que cumplir. Su `evidencia` tiene
**4 elementos**.

| coordenada | caracteres | que es |
|---|---:|---|
| linea 41 + indice 0 (elemento 1) | 78 | clausula: `ninguna de las once aparece en INTRA_DOMINIO_VEREDICTOS.jsonl: viven solo aqui` |
| linea 41 + indice 1 (elemento 2) | 51 | clausula: `el marcador del cribado no se mueve: sigue en 2.117` |
| linea 41 + indice 2 (elemento 3) | 69 | clausula: `cada nomina afectada se re-mide con su cobertura al lado (banco 9.26)` |
| linea 41 + indice 3 (elemento 4) | 3326 | CORRECCION DECLARADA de la vuelta 166 |
| linea 41 + indice 4 (elemento 5) | 1993 | CORRECCION DECLARADA de la vuelta 166 |
| linea 41 + indice 5 (elemento 6) | 2376 | CORRECCION DECLARADA de la vuelta 169 |

#### EL CRITERIO APLICADO: LA CIFRA CONGELADA NO AGUANTA, Y ESO SE MIDE

El criterio pregunta si la verificacion **se caeria si el fallo volviera**. Aqui
se le hace la pregunta mas dura y mas barata que el propio criterio nombra:
**volver a correr el instrumento hoy y cotejar sus cifras contra las que la ficha
tiene congeladas**. **7 cifras cotejadas, 3 DISCREPAN:**

| cifra | corrida sellada del 2026-09-04 | corrida de hoy, 2026-09-07 | |
|---|---:|---:|---|
| cabeceras `LD` leidas de `LECTURAS_DIRIGIDAS.md` | **11** | **27** | **DISCREPA** |
| de esas, las que aparecen en comparacion LITERAL | 0 | 0 | CALZA |
| de esas, las que aparecen en comparacion RESUELTA | **3** | **11** | **DISCREPA** |
| puestos implicados en total | **5** | **61** | **DISCREPA** |
| alias en el mapa del resolutor | 761 | 761 | CALZA |
| filas de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 3388 | 3388 | CALZA |
| marcador del cribado | 3388 | 3388 | CALZA |

**QUE SIGNIFICA, DICHO CON LA MEDICION DELANTE Y SIN ARREGLARLO.** La funcion que
el instrumento llama `las_once()` **no devuelve once**: devuelve **toda cabecera
`LD` que haya hoy en `docs/plan/LECTURAS_DIRIGIDAS.md`**, y ese documento **paso
de 11 a 27 cabeceras** entre el 4 y el 7 de septiembre de 2026. La ficha tiene
congelado, en su elemento 4, **EN COMPARACION RESUELTA APARECEN 3**, y hoy el
mismo instrumento sobre el mismo archivo dice **11**: los **3** de siempre
(`LD-01`, `LD-05` y `LD-11`) mas **8 nuevos** (`LD-139` a `LD-146`), que **no son
de la tanda de las once**.

**LA CIFRA VIEJA NO ES UNA MENTIRA:** viaja con su corte, el **2026-09-04**, y con
ese corte era cierta. **Lo que envejecio es el universo que la produce.** Es la
misma especie que la 201 corrigio en `OP-I-01` y que esta vuelta corrigio en
`OP-L-03`. **PERO AQUI NO SE ESCRIBE, SE PROPONE:** el encargo de esta tarea dice
**PROPON, NO CIERRES**, y esta correccion **no esta adjudicada**.

**Y LA CLAUSULA 1 NO SE CAE POR ESTO, Y SE DICE PARA NO EXAGERAR:** en comparacion
**LITERAL** siguen apareciendo **0**, que es lo que la clausula pregunta. Lo que
no aguanta es **la cifra de la excepcion nombrada**, no el veredicto.

**UN INVARIANTE ROJO QUE NO ES UN FALLO, DECLARADO PARA QUE NADIE LO LEA MAL:** la
corrida de hoy imprime **5 invariantes, 4 pasan y 1 falla**, y el que falla es
`3_verificacion_crece_en_exactamente_dos`, *de 6 a 6, delta 0*. **Falla porque la
correccion YA ESTA en la ficha y el modo medicion no escribe nada**, no porque
algo este mal.

#### EL HUECO DE LA VIGENCIA, MEDIDO POR PRIMERA VEZ

**LA VARA VA DECLARADA ANTES DE CORRERSE**, en la constante `VARA_DE_LA_VIGENCIA`
del propio fichero, **porque una aguja que se elige despues de mirar no mide
nada**. Dice: una fila **sigue en pie** si **todos los puestos que ella misma cita
existen hoy** en el archivo; una fila que **no cita ningun puesto** es **NO
MEDIBLE POR ESTA VARA** y se cuenta aparte, **ni en pie ni caida**; y la vara mide
**PRESENCIA DEL PUESTO, no calidad de la fila**.

**LAS DOS CIFRAS SE RECUENTAN AQUI.** La cabecera esta en la **linea 938** de
`docs/BANCO_DE_TEXTOS.md`, que mide **182228 bytes en disco y 182228 bytes
normalizados a LF**, y dice literalmente *TABLA VIVA DE LOS PUROS, al 14 ago 2026
(vigente al puesto 1157)*: **vigencia 1157, leida de la cabecera**. Y
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, que mide **4054129 bytes en disco y 4054129 bytes normalizados a LF**, trae **3388 filas**, **0 lineas que no sean
JSON valido**, **3388 puestos distintos** y **maximo 3388**. **La diferencia es de
2231 puestos.**

**LA TABLA SE ACOTA AL BLOQUE CONTIGUO** de lineas que empiezan por barra tras la
cabecera, **lineas 953 a 965**, y dentro de esa cota hay **11 filas numeradas**.

| lo que se cuenta | cifra |
|---|---:|
| filas de la TABLA VIVA dentro de la cota | **11** |
| filas EN PIE al corte 3388 (todos sus puestos existen hoy) | **6** |
| filas CAIDAS (citan un puesto que hoy no existe) | **0** |
| filas NO MEDIBLES POR ESTA VARA (no citan puesto) | **5** |
| filas que citan un puesto MAS ALLA de la vigencia declarada 1157 | **4** |
| filas que citan un puesto igual o mayor que el marcador de hoy 3388 | **0** |

**EL HUECO, NOMBRADO Y NO ARREGLADO.** La cabecera declara **vigencia al puesto
1157** y **4 de las 11 filas citan un puesto por encima de esa vigencia** (la 5 al
2117, la 7 al 1190, la 9 al 1600 y la 11 al 1517): **la cabecera ya esta desmentida
por sus propias celdas**, y eso se ve sin salir del documento. Ademas, **ninguna
fila lleva recuento al corte de hoy**, que vale **3388**. **NINGUNA CLASE SE MUEVE
AQUI: mover una clase es del RECOMPUTO**, y aqui se nombra y se para.

**LO QUE LA VARA NO CAZA VA PUBLICADO Y NO CONTADO**, que es lo que la propia vara
manda: cinco filas mencionan numerales de tres o cuatro cifras que la expresion no
recoge, entre ellos el **862** de la fila 4 y los **197, 222 y 463** de la fila 10.
**Y ahi mismo se ve por que la vara es de `puesto N` y no de numerales sueltos:**
el numeral **2026** aparece en cinco filas y **es el ano de una fecha**, mientras el
archivo tiene ademas un puesto 2026 que no tiene nada que ver.

#### LA CORRECCION DE MI PROPIO COMPUTO, DECLARADA Y NO TAPADA

**Mi primer extractor de filas cogia toda linea `| **N** |` posterior a la
cabecera y sacaba 32 filas**, que no son las de la TABLA VIVA sino las de esa
tabla **mas las de otras tablas de mas abajo del banco** (lineas 1056, 1674, 2024
y 2591 entre otras). **La TABLA VIVA tiene 11.** Con el extractor malo el reparto
salia **9 en pie, 0 caidas y 23 no medibles**, y con el bueno sale **6, 0 y 5**.
Arreglado acotando al bloque contiguo, **y el texto viejo queda escrito dentro del
fichero**.

#### LA PROPUESTA, QUE NO CIERRA NADA

**DOS COSAS SE PROPONEN Y NINGUNA SE ESCRIBE:**

1. **UNA CORRECCION DECLARADA MAS EN LA `verificacion` DE `OP-L-01`**, por el
   mismo carril del banco `9.10` y por adicion, que diga que el universo del
   instrumento paso de **11** a **27** cabeceras `LD` y que la comparacion
   resuelta pasa de **3** a **11**, con sus dos fechas de corte. **Es la misma
   especie que `OP-I-01` en la 201 y `OP-L-03` en esta vuelta.**
2. **LA VIGENCIA DE LA CABECERA DE LA TABLA VIVA**, que hoy dice **1157** y esta
   desmentida por **4** de sus propias **11** filas. **Actualizarla es tocar el
   banco, y eso no lo decide el ejecutor.**

**NINGUN campo `estado` se movio**, y este computo cambia **0 lineas** de
`docs/plan/OPERACIONES.jsonl`. **Lo adjudica el auditor.**

**DISCUTIBLE, MARCADO ANTES DE SABER SI ACIERTO:** sostengo que la discrepancia
de `las_once()` **no tumba la clausula 1**, porque en comparacion literal el
resultado sigue siendo **0** y eso es lo que la clausula pregunta. **Quien decida
que una excepcion mal contada si tumba la clausula tendra un argumento, y no soy
yo quien lo cierra.**

### TAREA 4. LOS REGISTROS `R.63` Y `R.64`, LAS DOS MAS VIEJAS DE LA DEUDA

**ADJUDICADA POR EL ACTA 201 EN SU `4.9`:** la deuda son **8 actas seguidas, las
173 a las 180**, y se pagan **DE LA MAS VIEJA A LA MAS NUEVA, DOS POR VUELTA**.
**Esta tarea fue DETRAS del trabajo de plan y nunca delante**, que es lo que la
moratoria `6.3` manda al decir que **el trabajo es el plan hasta agotarlo**: las
tareas 1, 2 y 3 cerraron y se commitearon antes de que esta empezara.

**NINGUN LECTOR NUEVO.** Los cinco que el computo usa se **importan**, como hizo
la 201: `serie_de_registros.siguiente_libre()`, `R84.claves_entrecomilladas()`,
`R94.caidas_propias_entrecomilladas()`, `R92.caidas_por_lead_heredado()` y
`R92.titulo_de_la_entrada()`, mas `R95.cifras_de_la_fila_de_puestos()`. El
computo vive en `scripts/loop/_v202_t4_registrar_actas.py`, con **prefijo de
guion bajo**, fuera del censo y fuera de la nomina, y es **CLON DECLARADO** de
`scripts/loop/_v201_t1_registrar_actas.py` generado con
`scripts/loop/_gen_v202_t4.py`: de sus **636 lineas**, **515 vienen sin tocar de
la fuente** y **121 son nuevas**, contadas con `difflib` y no a ojo.

#### LA PRUEBA POR MUTACION, ANTES DE ESCRIBIR NADA

**No hay lector nuevo que mutar, y eso se declara en vez de fabricar un caso que
se apruebe solo** (`EJECUTOR.md` 1). Lo que si se vuelve a probar es **la guarda
de idempotencia**, porque esta vuelta escribe **dos entradas seguidas**, que es
el escenario exacto en que la guarda vieja cayo. **8 casos, los 8 pasan**, y la
guarda vieja corre **al lado y entera** sobre los mismos textos: **discrepa de la
nueva en 2 de los 8**, que son justo los dos que miran el **sujeto** y no el
numero. **La segunda pasada muta el valor esperado y los 8 CAEN.** El repo no se
toca: los casos se fabrican en un temporal y se limpia (`P.16`).

#### LAS DOS ACTAS, ACOTADAS EN ESTA VUELTA

| acta | lineas de inicio y fin, contadas hoy | lineas | reporte archivado |
|---|---|---:|---|
| **173** | 58941 a 59447 | 507 | `docs/loop/reportes/REPORTE_V173.md` **NO EXISTE** |
| **174** | 59448 a 59994 | 547 | `docs/loop/reportes/REPORTE_V174.md` **existe, 32568 bytes en disco y 32568 bytes normalizados a LF** |

`docs/loop/ACTA_AUDITOR.md` mide **4680981 bytes en disco y 4680981 bytes
normalizados a LF**. **La ausencia del reporte de la 173 se midio con
`os.path.isfile` y `os.path.getsize`** y **NO SE FABRICO**: el bloque `H.2` del
sello de apertura ya lo habia contado sobre el rango entero, y en la **168 a la
199 faltan DOS**, la **173** y la **198**. **El encargo mandaba comprobarlo y no
suponerlo: comprobado.**

#### LA PARADA, Y ES DE MEDICION: EL REPARTO NO SE PUEDE COMPUTAR HOY

**LOS CINCO LECTORES HEREDADOS DEVUELVEN CERO SOBRE LAS DOS ACTAS**, y **ese cero
es DE CONVENCION Y NO DE AUSENCIA**. Medido, no supuesto:

| lector | acta 173 | acta 174 |
|---|---:|---:|
| `R84.claves_entrecomilladas()` con prefijo `4.` | 0 | 0 |
| `R84.claves_entrecomilladas()` con prefijo `5.` | 0 | 0 |
| `R84.claves_entrecomilladas()` con prefijo `C.A` | 0 | 0 |
| `R94.caidas_propias_entrecomilladas()` | 0 | 0 |
| `R92.caidas_por_lead_heredado()`, ejecutor y auditor y huerfanas | 0, 0, 0 | 0, 0, 0 |

**POR QUE DAN CERO, LEIDO DEL ACTA Y NO DEDUCIDO.** Las actas **173 y 174 son
ANTERIORES a la 184** y escriben sus claves como **cabeceras markdown** `### 4.1`,
no como ``**`4.1` ...``, que es la forma que esos lectores buscan. Y ademas **su
estructura es otra**: en las dos, **la seccion 4 es LOS HALLAZGOS** (con `4.1` a
`4.5`), **LAS ADJUDICACIONES viven en la seccion 6** y **sin clave numerada**, y
**las caidas propias del auditor viven en la seccion 3**. En la convencion nueva
la seccion 4 es la de adjudicaciones y la 5 la de hallazgos: **estan cruzadas**.

**POR ESO EL TITULO HEREDADO NO SE USA, Y SE PUBLICA COMO CONTRASTE.**
`R92.titulo_de_la_entrada()` produce, sobre estas cifras, *"Registro de las cero
adjudicaciones numeradas, los cero hallazgos de la seccion 5, las cero preguntas
contestadas, las cero caidas propias del auditor y las cero caidas del ejecutor
del acta de la vuelta 173"*. **Ese titulo se leeria como que el acta no adjudico
nada, y es falso.** La vuelta 201 ya rechazo un cero de esta misma especie en su
entrada de la 198, con estas palabras: *lo dice en vez de publicar un cero que se
leeria como que el acta 198 no contesto ninguna pregunta*. **Aqui se sigue ese
precedente**: el titulo heredado va escrito en la salida **como contraste**, y el
titulo que se escribe dice que **los cinco numerales NO SON COMPUTABLES POR LOS
LECTORES HEREDADOS**.

**Y AQUI PARO, PORQUE SEGUIR SERIA DECIDIR Y NO MEDIR.** Computar el reparto de
estas dos actas pide **una de dos cosas y las dos me estan cerradas**: **un lector
para la convencion anterior a la 184**, que la moratoria `AUDITOR.md` 6.3
**prohibe fabricar**; **o decidir que seccion del acta vieja cuenta como cada
numeral**, que es **DECIDIR y no medir**, y `AUDITOR.md` 3 llama a eso **PARADA y
no improvisacion**. **No lo arreglo yo.**

**LO QUE SI SE PUDO MEDIR SI ENTRO EN LAS DOS ENTRADAS**, y no es poco: la cota
por linea, los bytes de la sede y del acta por las dos convenciones, la existencia
o ausencia del reporte con su medicion, y **la metrica de credito PEGADA ENTERA
con su numero de linea**, que es cita y no celda tecleada. De ahi salen, sin
teclear nada: el acta 173 declara en su linea 59360 **3 caidas propias del
auditor** y en su linea 59357 **8 puestos**, y el acta 174 declara en su linea
59909 **2 caidas propias del auditor** y en su linea 59906 **8 puestos**.

#### LAS DOS ENTRADAS, ESCRITAS Y RE-CORRIDAS

**Ningun numero esta tecleado:** `siguiente_libre()` se recomputa **antes de cada
entrada**, que es la unica forma de que el segundo numero no se teclee. Salieron
**`R.63` para el acta 173** y **`R.64` para el acta 174**, y viven en
`docs/PENDIENTES.md` en las **lineas 15766 y 15865**.

`docs/PENDIENTES.md` mide AL SALIR **1101602 bytes en disco y 1101602 bytes normalizados a LF**, y ANTES de estas dos entradas media **1091080 bytes en disco y 1091080 bytes normalizados a LF**, con un **crecimiento de 10522 bytes en disco y de 10522 bytes normalizados a LF**. **La segunda corrida sella IDEMPOTENTE**: **0 entradas escritas** y **crecimiento de 0 bytes en disco y de 0 bytes normalizados a LF**, con la guarda
diciendo *NO SE ESCRIBE: la entrada ya estaba* las **2** veces. Selladas en
`docs/loop/SALIDA_V202_T4_REGISTROS.txt` y
`docs/loop/SALIDA_V202_T4_REGISTROS_IDEM.txt`.

#### LA SERIE MEDIDA AL CIERRE, RECOMPUTADA Y NO HEREDADA

| lo que se mide | al abrir esta vuelta | al cerrar esta tarea |
|---|---:|---:|
| entradas de la serie | **54** | **56** |
| colisiones | **0** | **0** |
| huecos | **0** | **0** |
| siguiente libre | **R.63** | **R.65** |

Y **la deuda se remide al cierre en vez de heredarse**: de la **173** a la **200**
quedan **6 actas sin entrada propia**, y son las **175, 176, 177, 178, 179 y 180**.
**Eran 8 y quedan 6**, que es lo que dos por vuelta significa. `dataset/`,
`web/` y `engine/` siguen en **0 filas de `numstat`**: la unica sede que esta
tarea toca es `docs/PENDIENTES.md`.

**DISCUTIBLE, MARCADO ANTES DE SABER SI ACIERTO:** decidi **escribir las dos
entradas igualmente**, con el reparto declarado como no computable, en vez de
**no escribirlas y traer solo la parada**. Sostengo que una entrada que paga la
deuda con todo lo medible y **nombra en voz alta lo que no pudo medir** vale mas
que un hueco; **pero quien prefiera que una entrada sin reparto no se escriba
tendra un argumento, y no lo cierro yo.**

<!-- FIN ANEXO DE TAREAS -->

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE ESTA SECCION CITA EL FICHERO DEL QUE SALE Y SE RECONSTRUYO
CONTANDO ESE FICHERO ANTES DE PUBLICARLA** (`EJECUTOR.md` 1, LA TABLA SE CUENTA
DE SU FICHERO).

| lo que se mide | cifra de hoy | fichero del que sale |
|---|---|---|
| ficheros `SALIDA_V202_*` en `docs/loop/` | **37**, de ellos **37 vivos** y **0 de cero bytes** | `docs/loop/SALIDA_V202_CIERRE_MEDICIONES.txt` bloque `G` |
| racha de cierres al abrir | **3**, con las vueltas 199, 200 y 201 | `docs/loop/SALIDA_V202_APERTURA.txt` bloque `E` |
| nomina de la bateria, al abrir y al cerrar | **135** y **135**, contra el congelado **135** | bloques `F` del sello y `D` de las mediciones |
| arneses del censo fuera de la nomina | **2** con la vara **148** y **62** sin vara | los mismos dos bloques |
| serie de registros, al abrir y al cerrar | **54** y **56** entradas, **0** y **0** colisiones, **0** y **0** huecos | `SALIDA_V202_SERIE_APERTURA.txt` y `SALIDA_V202_CIERRE_MEDICIONES.txt` bloque `F` |
| siguiente libre, al abrir y al cerrar | **R.63** y **R.65** | los mismos dos ficheros |
| deuda de actas sin entrada propia, 173 a 200 | **6**, las 175 a 180 | `docs/loop/SALIDA_V202_T4_REGISTROS.txt` |
| marcador del cribado, recontado | **3388** filas, **A 551, B 72, C 5 y D 2760**, que suma **3388** | `docs/loop/SALIDA_V202_T2_OP_L_02.txt` bloque `E` |
| puestos del archivo | **3388** distintos, maximo **3388**, **0** huecos | el mismo fichero |
| vara del trabajo pendiente | **71** fichas, **37** que no calzan, **6** en LISTA sin prueba, **4** de trabajo real, **2** consumidas | `docs/loop/SALIDA_V202_VARA_DEL_PLAN.txt` |
| casos de la prueba de mutacion de la guarda de la TAREA 1 | **6 casos**, y **los 6 pasan** | `docs/loop/SALIDA_V202_T1_MUTACION_GUARDA.txt` |
| ficheros con reporte archivado ausente, rango 168 a 199 | **2**, la **173** y la **198** | `docs/loop/SALIDA_V202_APERTURA.txt` bloque `H.2` |

**LAS CIFRAS DEL PLAN QUE ESTA VUELTA MIDIO Y NADIE HABIA MEDIDO, todas con
fecha de corte 2026-09-07:**

| medicion | cifra | donde |
|---|---|---|
| `LECTURAS_DIRIGIDAS.md`, apariciones de `reparto por acto` y de `OP-L-03` | **0** y **0**, con **8** variantes de busqueda positiva en cero | `SALIDA_V202_T1_CORRECCION_OP_L_03.txt` |
| cobertura real de `OP-L-03` contra su promesa de **55 pares en 29 actos** | **14** actos con ficha, **11** con `leido` en true, **19** pares leidos | el mismo fichero |
| `OP-L-02`, clausulas cumplidas | **2 de 3** segun el instrumento, **3 de 3** con la clausula 2 remedida | `SALIDA_V202_T2_OP_L_02.txt` |
| `OP-L-01`, cifras de la corrida vieja contra la de hoy | **7** cotejadas y **3** que discrepan | `SALIDA_V202_T3_OP_L_01.txt` |
| TABLA VIVA DE LOS PUROS al corte 3388 | **11** filas: **6** en pie, **0** caidas y **5** no medibles; **4** citan un puesto por encima de su vigencia | el mismo fichero |

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO EN ESTA PROSA.**
`docs/loop/SALIDA_V202_APERTURA.txt`, bloque `C`, publica las dos cifras del
estado del arbol con la redaccion exacta que la guarda coteja, y aqui se repiten
LEIDAS de ella:

`git status --porcelain` 3 lineas al entrar, que eran el propio bloque de
apertura y sus dos piezas de generacion, todavia sin commitear.

`git diff --numstat -- dataset/` 0 filas al entrar.

**La apertura sellada no se toco al cierre ni una vez.**

**LO QUE SE TOCO:**

- `docs/plan/OPERACIONES.jsonl`: **un elemento mas** en la `evidencia` de
  `OP-L-03`, en su linea **43**. **1 linea anadida y 1 borrada**, que es lo que un
  `jsonl` da siempre al reescribir una linea, y es **la unica escritura de esta
  vuelta en `docs/plan/`**. Va con su guarda medida contra `HEAD` y corrida dos
  veces.
- `docs/PENDIENTES.md`: las entradas **`R.63`** (acta 173) y **`R.64`** (acta
  174), anadidas al final. **188 lineas anadidas y 0 borradas**, contadas con
  `git diff --numstat` contra el HEAD de apertura.
- `docs/loop/reportes/REPORTE_V201.md`: el reporte de la 201 **archivado byte a
  byte** antes de pisarlo, **745 lineas anadidas y 0 borradas**.
- `scripts/loop/`: el bloque de apertura, el esqueleto, el bloque de cierre y el
  registrador de la TAREA 4 (los cuatro **clones declarados**, y tres de ellos
  generados programaticamente para que su codigo vaya byte a byte), **seis
  computos de un solo uso con prefijo de guion bajo**, **cuatro moldes de
  generacion** y **cuatro cuerpos de tarea**.
- `docs/loop/`: las salidas selladas de esta vuelta y el reporte.

**LO QUE NO SE TOCO, Y SE MIDE EN VEZ DE PROMETERSE:**

- **`dataset/` no se toco a mano.** El `numstat` contra `HEAD` sale con **0
  filas** al entrar y **0 al salir**, medido en
  `SALIDA_V202_CICLO_NUMSTAT_APERTURA.txt` y en
  `SALIDA_V202_CICLO_NUMSTAT_CIERRE.txt`, y **contra el HEAD de apertura tambien
  sale en 0 filas**, medido en `SALIDA_V202_CIERRE_MEDICIONES.txt` bloque `C`.
- **`web/` y `engine/` en cero filas de `numstat`** por las dos varas, la de
  `HEAD` y la del HEAD de apertura `ebe04895`, leido de su sello y no tecleado.
- **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se movio.** **4054129 bytes en disco y 4054129 bytes normalizados a LF**, con `sha256` `0a77b5a35a962621` de disco y `0a77b5a35a962621` de LF, **al entrar y al salir**. **Ninguna clase y ningun
  veredicto se mueven, porque mover una clase es del RECOMPUTO.**
- **NINGUN CAMPO `estado` SE MOVIO**, y no se afirma: se mide contra `HEAD` en
  `SALIDA_V202_T1_GUARDA_ESTADO.txt` y en su gemela `_IDEM`, que salen **VERDE**
  las dos con **0 de 71 fichas** cambiando su `estado`. La vara del trabajo
  pendiente es el instrumento, nunca el campo (recuadro de `AUDITOR.md` 0).
- **La nomina no crecio ni se podo**: **135** al entrar y **135** al salir, con
  `CASOS_DECLARADOS` en **2** y el censo en **197** las dos veces. **Los dos
  arneses que quedan fuera con la vara 148 siguen fuera**, y son
  `vuelta197_tarea2_mutacion_orden_del_turno.py` y
  `vuelta199_tarea1_mutacion_guardas_revividas.py`.
- **NINGUN INSTRUMENTO AJENO SE TOCO NI SE CLONO.** Los cuatro que esta vuelta
  necesitaba se **importaron y se corrieron tal cual**: los dos de `OP-L-02` y los
  dos de `OP-L-01`. **El `sha256` de `docs/plan/OPERACIONES.jsonl` vale
  `6006fd16dc08dc58` antes y despues** de las dos corridas de la TAREA 3, que
  corrieron **en modo medicion y sin `--aplicar`**.
- **`AUDITOR.md`, `EJECUTOR.md` y `docs/BANCO_DE_TEXTOS.md` no se tocaron.** El
  hueco de la vigencia de la TABLA VIVA **se nombra y se mide, y no se corrige**:
  actualizar esa cabecera es tocar el banco y no lo decide el ejecutor.
- **`OP-L-01`, `OP-L-02` y `OP-L-03` se LEYERON y no se cerraron:** las tres
  entran y salen en `LISTA` y **ninguna ficha se cerro por cuenta del ejecutor**.
- **Las dos paradas que la 200 levanto y las que el acta 201 adjudico no se
  volvieron a levantar.**

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` LA CLAUSULA 2 DE `OP-L-02`, DADA POR CUMPLIDA CONTRA UNA VARA DISTINTA DE
LA DEL INSTRUMENTO.** El instrumento la da **NO CUMPLIDA** porque diffea contra
`46208790`, un HEAD de la vuelta 170; remedida contra el HEAD de apertura de esta
vuelta sale **CUMPLIDA**. Sostengo que la segunda lectura es la correcta **porque
la clausula pide que la OPERACION no mueva el archivo y la operacion es esta
vuelta**, y el acta 201 ya llamo falso rojo al otro en su `4.2`. **Pero quien
decida que una clausula no se puede dar por cumplida contra una vara distinta de
la que el instrumento usa tendra un argumento, y no lo cierro yo.**

**`D.2` LA DISCREPANCIA DE `las_once()` NO TUMBA LA CLAUSULA 1 DE `OP-L-01`.** El
universo del instrumento paso de **11** a **27** cabeceras `LD` y su comparacion
resuelta de **3** a **11**. Sostengo que **la clausula sigue cumplida** porque en
comparacion **LITERAL** siguen apareciendo **0**, que es lo que la clausula
pregunta, y lo que envejecio es **la cifra de la excepcion nombrada**. **Quien
sostenga que una excepcion mal contada si tumba la clausula tendra un argumento.**

**`D.3` ESCRIBI `R.63` Y `R.64` AUNQUE SU REPARTO NO SE PUDIERA COMPUTAR.**
Podia no escribirlas y traer solo la parada. Elegi **pagar la deuda con todo lo
medible y nombrar en voz alta lo que no pude medir**. **Quien prefiera que una
entrada sin reparto no se escriba tendra un argumento, y no lo cierro yo.**

**`D.4` LA VARA DEL HUECO DE LA VIGENCIA MIDE PRESENCIA Y NO CALIDAD.** La escribi
**antes de correrla**, en una constante del propio fichero, y con ella **5 de las
11 filas salen NO MEDIBLES**. Una vara mas ancha, de numerales sueltos, mediria
mas filas **y confundiria el ano 2026 con el puesto 2026**, que es justo lo que la
salida muestra. **Sostengo que es mejor medir menos y bien; quien prefiera una
vara mas ancha con sus falsos positivos declarados tendra un argumento.**

**`D.5` LOS CUATRO CLONES DE ESTA VUELTA SON MAQUINARIA O NO LO SON.** El bloque
de apertura, el esqueleto, el bloque de cierre y el registrador de la TAREA 4 son
**instancias de un computo ordenado**, y la adjudicacion `4.5` del acta 199 dice
que eso **no es maquinaria**. **Sostengo que la moratoria no los prohibe porque
sin ellos no hay vuelta; quien lea la moratoria mas estrecha tendra un argumento.**

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` LA VIGENCIA DE LA TABLA VIVA DE LOS PUROS DICE `1157` Y SUS PROPIAS
CELDAS LA DESMIENTEN.** **4 de sus 11 filas** citan un puesto por encima de esa
vigencia, y el marcador de hoy vale **3388**, **2231 puestos mas alla**.
**Actualizar esa cabecera es tocar `docs/BANCO_DE_TEXTOS.md`, y no se hace sin
decirlo. Que se hace con ella.**

**`P.2` LA CORRECCION DE LA `verificacion` DE `OP-L-01` ESTA MEDIDA Y NO
ESCRITA.** Es la misma especie que `OP-I-01` en la 201 y `OP-L-03` en esta vuelta,
y va **por el carril del banco `9.10` y por adicion**. **El encargo de la TAREA 3
decia PROPON, NO CIERRES, asi que no la escribi. Se adjudica o no.**

**`P.3` `OP-L-02` QUEDA EN 3 DE 3 CON LA CLAUSULA 2 REMEDIDA.** **No la cerre y no
movi su `estado`.** La propuesta va con su evidencia entera en la TAREA 2. **Se
adjudica o no.**

**`P.4` EL REPARTO DE LAS ACTAS ANTERIORES A LA 184 NO SE PUEDE COMPUTAR CON LOS
LECTORES DE HOY.** Quedan **6 actas de la deuda** y **todas son de esa
convencion**: las **175 a 180**. **O se autoriza un lector para la convencion
vieja, y eso es codigo bajo moratoria, o se decide que seccion cuenta como cada
numeral, y eso es una decision. Las dos me estan cerradas.**

## 7. PENDIENTES DE DOCTRINA

**Ninguno nuevo en esta vuelta.** Todo lo que esta vuelta midio se resolvio con
doctrina ya escrita: el banco `9.10` para las correcciones por adicion, el `9.21`
para las cifras con su corte, `P.1` para el resolutor, `P.2` para los bytes
exactos, `AUDITOR.md` 0 para el campo `estado`, `AUDITOR.md` 3 para la parada, y
`AUDITOR.md` 6.1, 6.2 y 6.3 para la cadencia, el tope y la moratoria.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE

**Las tres se cazaron ANTES de publicarse y las tres van escritas con el texto
viejo entero, que es lo que `EJECUTOR.md` 8 manda: una correccion que tapa lo que
corrige no se puede auditar.**

**`C.1`. MI RECUENTO DEL MARCADOR BUSCABA UNA CLAVE QUE NO EXISTE.** En
`scripts/loop/_v202_t2_op_l_02.py` miraba la clave `puesto` de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y publicaba **0 puestos distintos**. La
clave de ese archivo se llama **`puesto_intra`**: el **0** no era una medicion,
era **el sintoma de mirar donde no hay nada**. Contado bien son **3388 puestos
distintos, maximo 3388 y 0 huecos**. **La correccion queda escrita dentro del
fichero y no solo aqui.**

**`C.2`. MI EXTRACTOR DE FILAS DE LA TABLA VIVA COGIA CINCO TABLAS EN VEZ DE
UNA.** En `scripts/loop/_v202_t3_op_l_01.py` tomaba **toda** linea de tabla
posterior a la cabecera de la linea 938 y sacaba **32 filas**, que eran las de la
TABLA VIVA **mas las de otras tablas de mas abajo del banco** (lineas 1056, 1674,
2024 y 2591 entre otras). Con el extractor malo el reparto salia **9 en pie, 0
caidas y 23 no medibles**; acotado al bloque contiguo, la tabla tiene **11 filas**
y el reparto real es **6, 0 y 5**. **La cifra mala no se borra: va escrita dentro
del fichero y en la seccion de la TAREA 3.**

**`C.3`. ESCRIBI DOS CIFRAS DE BYTES SIN HABERLAS CONTADO.** En el cuerpo de la
TAREA 3 publique las selladas de los dos instrumentos como **32752** y **3971**
bytes normalizados a LF. Contadas, miden **32684** y **3963**. **Se corrigieron
contando los ficheros antes de anexar la tarea**, asi que la cifra mala **no llego
al reporte**, pero **la escribi**, y eso es una caida de cifra igual: la unica
diferencia es que la caze yo.

**Y UNA QUE NO CUENTO COMO CAIDA DE CIFRA, DICHA PARA NO ESCONDERLA:**
`scripts/loop/_v202_t3_op_l_01.py` **se cayo con un error de formato** en su
primera corrida, un `%` sin su hueco. **No publico ninguna cifra falsa porque no
publico nada**, y por eso no lleva numero de caida; queda dicho porque un
instrumento que revienta y se arregla en silencio tambien envejece mal.

**Y UNA CORRECCION MAS, DECLARADA, QUE NO ES CAIDA DE CIFRA SINO DE FORMA, Y QUE
NO CAZE YO SINO UNA GUARDA DE LA CASA:** al cerrar este reporte,
`scripts/loop/cerrar_reporte.py` lo **reprobo DOS VECES antes de dejarme
cerrar**. **La primera, con 12 cifras publicadas sin su pareja**: las 12 cifras
eran correctas, y lo que fallaba es que **el markdown parte la frase donde le cabe
el ancho** y dejaba el numero solo en su renglon, sin la segunda convencion al
lado. **La segunda, con 2 parejas que estaban COMPLETAS y eran FALSAS**: la frase
publicaba, **pegado a la ruta, el tamano de ANTES**, y la guarda lo leia como el
tamano de esa ruta, **con razon**, porque lo que va detras de una ruta es el
tamano de esa ruta. **Las dos veces se arreglo JUNTANDO la cifra con su pareja o
poniendo detras de cada ruta SU tamano medido, y NUNCA quitando una cifra**, con
`scripts/loop/_v202_juntar_parejas.py`, que lleva **13 arreglos declarados** y los
aplica **igual en el reporte y en las fuentes de las que salio**, para que las dos
sedes no se separen. **Es la misma especie que tumbo el cierre de la 201 dos
veces, y el remedio es el mismo que aquella dejo escrito.**

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 202 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V202_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: NADIE la corrio, y NO tocaba: es LA CADENCIA de AUDITOR.md 6.1, que pone la bateria CADA CINCO VUELTAS y en vuelta propia. La 200 fue la vuelta de bateria y la corrio ENTERA, asi que por esa cadencia le toca a la 205 y la 202 es vuelta intermedia: su hueco se declara y se mide en vez de rellenarse. El encargo de esta vuelta lo dice con esas palabras y su sello de apertura lo escribe en el bloque I, que mide CERO ficheros de tramo de ESTA vuelta en disco al entrar, sobre 40 selladas por tramo que si hay en docs/loop/ repartidas entre las vueltas 176, 183, 189 y 194. Y LO QUE ESTA VUELTA SI MIDIO DEL RADIO DE LA BATERIA, sin correrla, dos veces y con el mismo resultado, en el bloque F del sello de apertura y en el bloque D de docs/loop/SALIDA_V202_CIERRE_MEDICIONES.txt: la nomina de verificar_mutaciones_viejas.py entra y sale en 135 entradas y CALZA con el congelado que manda AUDITOR.md 6.3, con CASOS_DECLARADOS en 2; el censo reconoce 197 arneses; LA VARA DEL CENSO VALE 148 y es la que decide, y CON ESA VARA hay 2 arneses del censo fuera de la nomina, pero SIN VARA hay 62, y las dos cifras se publican juntas porque un numero solo al lado de un censo de 197 y una nomina de 135 se lee como cobertura total y es cobertura desde la vara para arriba; hay ademas 0 entradas invisibles al censo y 0 entradas sin sujeto congelado. LOS DOS ARNESES QUE QUEDAN FUERA CON LA VARA 148 VAN NOMBRADOS: vuelta197_tarea2_mutacion_orden_del_turno.py y vuelta199_tarea1_mutacion_guardas_revividas.py, los dos escritos por vueltas anteriores y ninguno metido en la nomina porque el congelado lo impide, asi que la 205 tampoco los va a correr, y eso es consecuencia de una regla escrita y no un descuido. NO SE PODO NI UNA ENTRADA Y NO SE ANADIO NINGUNA: los seis computos nuevos de esta vuelta llevan prefijo de guion bajo y quedan fuera del censo y fuera de la nomina, por el mismo congelado. Y DONDE QUEDO SELLADA LA CORRIDA DE LA 200 NO SE NOMBRA AQUI A PROPOSITO, porque nombrar el fichero de otra vuelta dentro de este hueco es justo lo que la guarda de la pieza 4 prohibe y hace bien: esa medicion, con su ruta y su commit, vive en el bloque E de docs/loop/SALIDA_V202_CIERRE_MEDICIONES.txt.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
