### TAREA 5, LAS SEIS ABIERTAS POR LA VARA DEL INSTRUMENTO

**Salida:** `docs/loop/SALIDA_V168_T5_LAS_SEIS.txt`. **Instrumento:**
`scripts/loop/vuelta168_tarea5_abrir_las_seis.py`, que **no reimplementa la vara:
invoca** `scripts/loop/vuelta150_3_relectura_expediente.py` y lee su salida.
**Cero nodos tocados, cero estados movidos, cero fichas editadas por esta tarea.**

**LA VARA, CORRIDA EN ESTA VUELTA** (seccion 0), comando pegado al lado:
`python scripts/loop/vuelta150_3_relectura_expediente.py --corte edbc1a48
--apertura 36bafc1a`, exit 0.

| lo que mide el instrumento | cifra de hoy | cifra del acta 167 |
|---|---:|---:|
| fichas del expediente | **71** | 71 |
| fichas que NO CALZAN | **37** | 37 |
| congeladas DECLARADAS | **24** | 24 |
| congeladas EN SILENCIO | **12** | 12 |
| `HECHA` sin ninguna prueba | **1** | 1 |
| `LISTA` sin ninguna prueba de ejecucion | **6** | 6 |

**LAS SEIS SE LEYERON DE LA SALIDA DEL INSTRUMENTO, NO DE UNA LISTA MIA**, y el
instrumento nombra: `OP-L-01`, `OP-L-02`, `OP-L-03`, `OP-I-01`,
`OP-M-02-MEDIOS`, `OP-M-02-ADMIT`. **MISMO CONJUNTO que el encargo: SI.** Si
hubieran discrepado, el instrumento paraba.

**5.b LA VALVULA DE VIGENCIA, CORRIDA ANTES DE TOCAR NADA, Y LAS DOS SALEN
CUMPLIDAS POR CONSUNCION.** La medicion **no se copio de la nota de las fichas**
(que la traen desde la vuelta 64): se re corrio hoy con
`scripts/loop/vuelta64_consumidas.py`, porque una nota vieja es contraste y nunca
fuente.

| ficha | sus dos miembros resueltos contra el grafo de HOY | veredicto |
|---|---|---|
| `OP-M-02-MEDIOS` | `seis_medios_comunicacion_cliente` DEPRECADO va a `estrategia_multicanal_bienvenida`, que esta VIVO: **UN solo vivo** | **CUMPLIDA POR CONSUNCION, NO SE EJECUTA** |
| `OP-M-02-ADMIT` | `fase_admit` DEPRECADO va a `fase_admit_celebracion`, que esta VIVO: **UN solo vivo** | **CUMPLIDA POR CONSUNCION, NO SE EJECUTA** |

**QUIEN CONSUMIO EL ACTO, CON SU LINEA:** `OP-U-01` TRAMO 3, vuelta 56, acto 32,
lote B, `docs/plan/03_FUSIONES.md` **linea 2091** para MEDIOS; y `OP-U-01` TRAMO
2, vuelta 55, acto 38, lote B, **linea 1840** para ADMIT. **Las cinco
`OP-M-02-*` resuelven a un solo vivo (5 de 5).** Y la valvula publica ademas lo
que ninguna de las dos fichas puede tapar: **DIVERGEN**, porque cada ficha
adjudico el 12 ago 2026 el superviviente OPUESTO al que el tramo dejo vivo. **Eso
no se deshace y no se copia: se declara**, como ya hizo la vuelta 64.

**5.c LOS `depende_de`, LEIDOS POR EL INSTRUMENTO Y NO POR EL CAMPO.** El
encargo avisa: *"Si el instrumento dice otra cosa, paras y lo traes."* **No dice
otra cosa.**

| `OP-D-*` | estado (CAMPO, historico) | pruebas (INSTRUMENTO) | por la vara nueva |
|---|---|---|---|
| `OP-D-01` | LISTA | P2+P3a | **CUMPLIDA** |
| `OP-D-02` | LISTA | P1+P2+P3a | **CUMPLIDA** |
| `OP-D-03` | LISTA | P3a | **CUMPLIDA** |
| `OP-D-04` | LISTA | P2+P3a | **CUMPLIDA** |
| `OP-D-05` | LISTA | P1+P3a | **CUMPLIDA** |
| `OP-D-06` | LISTA | P3a | **CUMPLIDA** |

**6 de 6 con prueba, 0 sin prueba**, asi que **`OP-L-02` y `OP-L-03` dejan de
estar bloqueadas**. **Y LA DIFERENCIA ENTRE LAS DOS VARAS SE PUBLICA EN VEZ DE
DISIMULARSE:** por el campo `estado` las seis siguen en `LISTA`, y la seccion
3.c del propio instrumento, que **lee el campo**, no las lista como
desbloqueadas. Es exactamente el caso que la decision del fundador zanja.

**5.a `OP-I-01`, ABIERTA Y MEDIDA CLAUSULA A CLAUSULA.** No escribe nada en el
grafo (0 elementos entre `nodos`, `preservar`, `eliminar` y `aristas_nuevas`).
El inventario de hoy, contado de `docs/plan/INVENTARIO.jsonl`: **672 entradas**
(556 actos, 54 familias de ids, 20 figuras, 19 defectos, 13 racimos, 10
dominios), en **4 fechas de corte** (11 ago = 323, 12 ago = 11, 13 ago = 337, 14
ago = 1).

- **CLAUSULA 1**, *toda entrada lleva su `fecha_corte`*: **SE CUMPLE**, 0
  entradas sin corte.
- **CLAUSULA 2**, *toda forma con cobertura incompleta va marcada PROVISIONAL*:
  **NO ES MEDIBLE POR CONTEO Y SE DICE en vez de darla por buena.** Se pueden
  contar las **2** que SI estan marcadas; para saber si estan TODAS haria falta
  la lista de las incompletas, y el inventario no la trae como campo.
- **CLAUSULA 3**, *todo hueco va NOMBRADO, nunca rellenado*: **119** entradas
  nombran un hueco, y la nota de la ficha nombra los suyos.
- **CLAUSULA 4**, *el inventario se recomputa entero con el disparador de
  `08_VERIFICACION`*: **ESTA ES LA QUE NO SE PUEDE EJECUTAR SIN DECIDIR.** La
  nota de la ficha declara **335 actos (280 CERRADOS, 55 ABIERTOS)** al corte
  3.388, medidos en la vuelta 14. **Medido hoy sobre
  `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`: 332 lineas, 278 CERRADOS, 54
  ABIERTOS.** **La discrepancia se declara y NO se resuelve copiando.** Y se
  dice de donde viene, trazada commit a commit con `git show` sobre ese fichero:
  **335 en `7f4ec6d9`** (vuelta 11), **334 en `7cec9ecc`**, **333 en
  `97552714`**, **332 en `70878328`** (vuelta 40, `OP-D-05`), cada bajada
  declarada en el asunto de su propio commit. **La cifra de la nota no es falsa:
  es de su corte.** Lo que no existe es **un instrumento que regenere el
  inventario**: sus dos formas se escribieron a mano entre las vueltas 17 y 20, y
  la ficha no escribe el procedimiento. **Recomputarlo entero hoy exigiria
  decidir su alcance**, y `AUDITOR.md` 3 dice que una operacion cuyo texto no
  alcanza para ejecutarse sin decidir es **PARADA, no una improvisacion**.

**5.a `OP-L-01`, ABIERTA Y MEDIDA CLAUSULA A CLAUSULA.** 5 clausulas, 2 de ellas
`CORRECCION DECLARADA` de la vuelta 166; no escribe nada en el grafo.

- **CLAUSULA 1: CERRADA** por la correccion de la vuelta 166, verificada por el
  acta 166 y adjudicada en su `6.8`. No se reabre.
- **CLAUSULA 2: CERRADA** por la correccion de la vuelta 166: el `2.117` es
  **TESTIGO de su corte, no condicion**. Medido hoy, contado del fichero, el
  marcador vale **3.388**.
- **CLAUSULA 3**, *cada nomina afectada se re-mide con su cobertura al lado
  (banco 9.26)*: **SIGUE ABIERTA, y con la medicion delante.** Para re-medir
  *"cada nomina afectada"* hay que saber cuales son, y la ficha no las escribe:
  sus cuatro listas de escritura estan **vacias**. La sede que nombra miembros es
  el inventario, o sea `OP-I-01`, cuya clausula 4 acaba de quedar declarada no
  ejecutable sin decidir. **La cadena es real y no una excusa: sin inventario
  recomputado no hay nomina que re-medir.**

**EL SALDO DE LAS SEIS, CONTADO:** **2 cumplidas por consuncion y no
ejecutadas** (`OP-M-02-MEDIOS`, `OP-M-02-ADMIT`); **2 desbloqueadas por la vara
nueva y no ejecutadas en esta vuelta** (`OP-L-02`, `OP-L-03`); **2 abiertas,
medidas clausula a clausula y con su ultima clausula bloqueada por la misma
cadena** (`OP-I-01` clausula 4, `OP-L-01` clausula 3). **Ninguna se cierra
declarandola cerrada, y ninguna se improvisa.**
