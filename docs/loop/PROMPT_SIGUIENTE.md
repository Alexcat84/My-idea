# ENCARGO DE LA VUELTA 213 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

## LO QUE RIGE EN ESTA VUELTA, Y SE DICE ANTES DE LAS TAREAS

- **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). **Ningun arnes, guarda ni lector
  nuevo, y ninguno reparado.** Todo lo que escribas en `scripts/loop/` lleva prefijo
  `_v213_`, muere con la vuelta y esta fuera del censo y de la nomina. **La nomina de la
  bateria sigue CONGELADA EN 135 y nadie la poda.**
- **LA 213 NO ES VUELTA DE BATERIA.** La cadencia de cinco de `AUDITOR.md` 6.1 pone la
  siguiente en la **215**; la **210** corrio la ultima con sus **once** tramos, leidos de
  git. Tu seccion 9 cierra con el **HUECO DECLARADO Y MEDIDO**, con sus **tres** piezas:
  nombre, bytes medidos y atribucion.
- **EL TOPE DE SUB-TAREAS VUELVE A CINCO** (adjudicacion `6.8` del acta 212). El disparador
  de salida de `AUDITOR.md` 6.2 se cumplio: **la 210, la 211 y la 212 cerraron su propio
  reporte con `cerrar_reporte.py` en VERDE**, medido en disco y en git. **Este encargo
  lleva DOS igualmente**, y no por el tope: porque es lo que queda del plan.
- **SIGUE VIGENTE LA OBLIGACION DE DICTADO DEL `6.6` DEL ACTA 210:** toda cita de un acta
  anterior lleva **LA LINEA** de `docs/loop/ACTA_AUDITOR.md` donde vive el texto citado, y
  **la linea se LEE, no se recuerda**. La cumpliste entera en la 212, once de once.
- **SIGUE VIGENTE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
  filas de una salida declara, EN LA MISMA LINEA, cuantas filas armo; y si al lado va una
  cifra de cuantas deberia haber, **las dos se escriben juntas**. **En la 212 fueron 18
  parejas y las 18 calzaron con sus tablas.** Es la que mata la especie de la `2.e` de la
  211.

### TRES OBLIGACIONES DE DICTADO NUEVAS, LAS TRES SIN CODIGO Y LAS TRES DEL ACTA 212

1. **NINGUN REPORTE CITA UN DIRECTORIO A SECAS COMO RUTA** (adjudicacion `6.2`). Si hay que
   nombrar un arbol, se nombra **sin comillas inversas** o se nombra un fichero suyo.
   Motivo medido: `vuelta186_rutas_del_reporte.py`, en su `main()`, usa `os.path.exists`, y
   un directorio pasa esa puerta y revienta el `read()` de la linea siguiente. **NO LO
   REPARES: rige la moratoria, y el cierre no se cae por esto porque `cerrar_reporte.py`
   importa `medir_en_disco()` (su linea 154), que usa `os.path.isfile`.**
2. **UNA SECCION SUPLEMENTARIA VA DETRAS DE LA QUE AMPLIA, NUNCA DETRAS DE UNA MAYOR**
   (hallazgo `7.1`). Tu `## 7 BIS.` de la 212 quedo detras de la `## 8.`, y
   `secciones_fuera_de_orden()` **no puede verla**: su `PATRON_SECCION` es `^##\s+(\d+)\.`
   y exige el punto pegado al numero. **No es cifra falsa y no acumula, pero el punto ciego
   existe y esta levantado.**
3. **EL TALLADOR DE CABECERA CORRIDO EN APERTURA ESCRIBE EN UN NOMBRE CON `_RECHAZO`**, no
   en el nombre que usa el fichero del cierre. Es tu propio remedio de la `C.1` de la 212 y
   lo adopto como obligacion.

---

## TAREA 1: LOS REGISTROS Y EL BARRIDO DEL `9.10` QUE EL ACTA 212 ADJUDICA

### `1.a` LOS REGISTROS

Lee el acta del auditor que cubre la vuelta 212. **Abre en la linea 74821 de
`docs/loop/ACTA_AUDITOR.md`.** Registra en tu reporte, cada una con **su linea leida hoy**:

- **`6.1`**: la `P.1` adjudicada. Es lo que ejecutas en la `1.b`.
- **`6.2`**: la `P.2` contestada. El crash **espera**, la obligacion de dictado va puesta.
- **`6.3`**: tu `D.1` resuelta, y **la marca se te paga**: estabas equivocado en una de las
  dos mitades y la marca es lo que permitio verlo.
- **`6.4`**: tu `D.2`, el `474`. **NO SE MUEVE**, y tu decision de no moverlo es correcta.
- **`6.5`**: tu `D.3`. **Tenias razon**: las nueve cifras de cerco tuyas reproducen al
  digito y las dos del acta 211 no. **Queda registrada contra el acta 211, no contra ti.**
- **`6.6`** y **`6.7`**: tu `D.4`, tu `PD.1` y tu `PD.2`, cerradas sin doctrina nueva.
- **`4.1`**: tu `C.1`. **Se te acepta la declaracion y NO ACUMULA**, por dos motivos
  medidos que el acta escribe. **Tu remedio se adopta como obligacion.**

**Registra tambien, sin ejecutarlas, las CUATRO cosas que suben al fundador** en la
seccion 8 del acta 212, y **di en voz alta cual de ellas bloquea el cierre de la campaña**.

### `1.b` EL BARRIDO DEL `9.10`, Y ES UNA SOLA LINEA

La adjudicacion `6.1` del acta 212 resuelve tu `P.1`: **de las dos citas vivas del 730, una
se toca y la otra no.**

- **`docs/INTRA_DOMINIO_INFORME.md` linea 6941 NO SE TOCA.** Dice *"El puesto 730 es el
  primer veredicto nuevo emitido despues de que el choque de la seccion 19 quedara
  escrito"*, que es un hecho historico y **sigue siendo verdadero**.
- **`docs/plan/03_FUSIONES.md` linea 5424 SE CORRIGE.** Dice que el 730 *"deja anotado en
  vez de elegir"*, y **eso ya es falso: la fila eligio en la vuelta 212.**

**COMO SE HACE, Y ES EL CARRIL QUE YA USASTE DOS VECES:** correccion **DECLARADA** por el
banco `9.10`, **con el texto viejo entero encima y sin tachar**, citando en la propia
correccion la vuelta y el commit en que el 730 paso de `A` a `D`. **Lee la linea del disco
antes de escribirla y pega lo que leiste.**

**GUARDAS OBLIGATORIAS DE LA `1.b`, TODAS EN TU SALIDA SELLADA:**
- **simulacion en memoria antes de tocar el disco**, y su cifra de fallos en 0;
- **caso rojo por mutacion corrido ANTES de escribir**, con al menos estos mutantes: uno
  que tape el texto viejo, uno que toque una segunda linea del fichero y uno que escriba
  una cita que no calza. **Todos tienen que caer.**
- **sede al entrar y al salir por las dos convenciones**, con `sha256`, y **el `sha256`
  tiene que cambiar**;
- **`git diff --numstat` acotado a ese fichero: 1 fila, y 0 en cualquier otro sitio de
  `docs/plan`**;
- **el `sha256` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO se mueve** en toda la TAREA 1,
  y lo publicas al entrar y al salir para probarlo.

**LO QUE ESTA PROHIBIDO EXPRESAMENTE EN LA `1.b`:** tocar la linea 6941 del informe; tocar
el reporte archivado `REPORTE_V179.md` ni ningun otro reporte archivado; tocar la clase o
la razon de ninguna fila del archivo; y **abrir un barrido general de citas de otros
veredictos**. **Es UNA linea. Si encuentras mas citas envejecidas de OTROS puestos, NO las
toques: las mides, las nombras y las traes marcadas.**

---

## TAREA 2: EL CIERRE DE LA FASE III, MEDIDO. LA BASE DE LA AUDITORIA INTEGRAL

**POR QUE ESTA TAREA Y NO OTRA, Y ES UNA CIFRA.** La vara del trabajo pendiente
(`scripts/loop/vuelta150_3_relectura_expediente.py --corte HEAD`, corrida por el auditor en
la 212) mide **3** fichas en `LISTA` sin ninguna prueba: **`OP-M-02-MEDIOS` y
`OP-M-02-ADMIT`, las dos CONSUMIDAS por `OP-U-01`**, y **`OP-I-01`, la unica de trabajo
real**, que el acta 211 adjudico en su `6.3` como **no cerrable** por el bucle. **El plan
esta agotado.** Lo que queda es **el cierre**, y el cierre necesita una base medida que hoy
no existe en ningun sitio.

**LO QUE HAY QUE PRODUCIR: UN INVENTARIO DE CIERRE DE LA FASE III, DE LAS 71 FICHAS, LEIDO
DEL REPO Y NO DEL CAMPO `estado`.** Va en tu reporte como seccion propia y su salida cruda
sellada en `docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`.

**LA FUENTE ES LA VARA, NUNCA EL CAMPO.** El recuadro 0 de `AUDITOR.md` es tajante: para
saber **que queda por ejecutar** se corre la vara y se lee su salida; **el campo `estado`
es HISTORICO y no se usa para eso**. **Corres la vara en ESTA vuelta y publicas su salida
tal como sale.** El campo `estado` se publica **al lado**, como contraste, y **cuando los
dos discrepen se dice, no se resuelve.**

**LA TABLA, UNA FILA POR FICHA, LAS 71, Y SIN CORTAR:**

| columna | de donde sale |
|---|---|
| `id_op` | `docs/plan/OPERACIONES.jsonl`, contado y no tecleado |
| `fase` | la ficha |
| `tipo` | la ficha |
| `estado` HISTORICO | la ficha, **etiquetado como historico en la propia cabecera** |
| pruebas que da positivo (P1 / P2 / P3a / P3b / documental) | **la salida de la vara de esta vuelta** |
| veredicto del repo | **EJECUTADA**, **CONSUMIDA por `<id_op>`** o **SIN EJECUTAR** |
| calza el campo con el repo | SI / NO |

**LAS CUATRO CIFRAS QUE LA SECCION CIERRA, CADA UNA CONTADA DE LA TABLA Y NO TECLEADA:**
1. **cuantas de las 71 tienen prueba de ejecucion en el repo**;
2. **cuantas estan CONSUMIDAS y por quien**;
3. **cuantas estan SIN EJECUTAR**, con su lista entera;
4. **cuantas tienen el campo `estado` en desacuerdo con el repo**, en las dos direcciones
   (`HECHA` sin prueba, y `LISTA` con prueba), **con las dos listas enteras**.

**Y LA CUARTA LLEVA SU CAUTELA ESCRITA AL LADO, que es la `6.8` del acta 211:** si cada
ficha va poniendo su campo al dia, la vara tiende a cero sin que se haya ejecutado nada
mas. **La cifra se publica con esa cautela pegada, no suelta.**

### `2.b` LA UNICA QUE QUEDA ABIERTA, ESCRITA PARA QUE EL FUNDADOR PUEDA DECIDIR

Una sub-seccion sobre **`OP-I-01`** y nada mas, con esto y en este orden:
- sus **cuatro** puntos de `verificacion` **pegados enteros del fichero**, cada uno con su
  estado (`CUBRE`, `A MEDIAS`, `NO CUBRE`) tal como la ficha lo escribe;
- **el punto que esta en `NO CUBRE`, aparte y entero**, y **que haria falta exactamente
  para que dejara de estarlo**, citando la adjudicacion `6.4` del acta 211 con su linea;
- **la cifra de las 95 entradas del inventario con cobertura incompleta, RECONTADA POR TI
  en esta vuelta** de `docs/plan/INVENTARIO.jsonl`, con el comando que la cuenta; si tu
  cifra no es 95, **lo dices en vez de copiar la vieja**;
- **la frase, en una linea, de que decide el fundador y que no**: marcar esas entradas es
  edicion de datos de `docs/plan/` que **ninguna regla ordena hoy**, y las filas que faltan
  en `08_VERIFICACION.md` para las fases 09 y 10 **cambian la forma del plan**.

**PROHIBICIONES EXPRESAS DE LA TAREA 2, Y SON CINCO:**
1. **NO cambies el campo `estado` de ninguna ficha.** Ni una. Esta tarea **MIDE**, no
   escribe en `OPERACIONES.jsonl`. El `sha256` de ese fichero al terminar la TAREA 2 tiene
   que ser **el mismo con el que empezo**, y lo publicas para probarlo.
2. **NO marques las 95 entradas del inventario.** Se cuentan y se dejan.
3. **NO escribas ni una fila nueva en `docs/plan/08_VERIFICACION.md`.**
4. **NO declares la campaña consumada ni escribas `PARA_ALEXIS.md`.** Eso es del auditor y
   **hoy no se puede**: `OP-I-01` esta abierta y lo que necesita es del fundador.
5. **NO toques el grafo.** `git diff HEAD --numstat` en **0 filas** en los dos lados del
   ciclo de Gate 0.

---

## LO QUE SE MIDE Y SE SELLA EN LAS DOS TAREAS, COMO SIEMPRE

- **Apertura sellada ANTES de la primera operacion**, con su HEAD y su `git status`, y el
  **ciclo entero de Gate 0 lado APERTURA**. Nunca `run_phase1.py` a secas: los ocho
  comandos en su orden.
- **Esqueleto del reporte tallado antes de tocar ninguna tarea**, con sus DOS filas
  diciendo `ABIERTA, SIN CERRAR`, y cada tarea anexando su fila al cerrarse.
- **Ciclo entero de Gate 0 lado CIERRE**, con su peor exitcode y su `numstat`.
- **Cierre con `scripts/loop/cerrar_reporte.py`**, salida sellada, y la cabecera tallada
  por `tallar_cabecera_reporte.py --fase04 --vuelta 213` **cotejada contra el reporte**.
- **`scripts/loop/vuelta186_rutas_del_reporte.py` corrido DESPUES del cierre**, sobre el
  reporte cerrado, y **su salida commiteada**. Con la obligacion 1 de arriba puesta, tiene
  que llegar a imprimir.
- **Archiva el reporte de la 212** en `docs/loop/reportes/` al abrir, como hiciste con el
  de la 211.

## LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE IMPROVISE

- **No se abre cola de re-cribado.** La TAREA 2 de la 212 midio que **ninguno** de los tres
  que quedan en `A` cuelga de la silueta. **El cerco del cero-enlazados esta cerrado.**
- **No se repara `vuelta186_rutas_del_reporte.py`** ni `secciones_fuera_de_orden()`. Los
  dos estan levantados y los dos esperan a la integral.
- **No se corre la bateria.** La 213 no es su vuelta.
- **No se editan reportes archivados.** Ninguno, por ningun motivo.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.
