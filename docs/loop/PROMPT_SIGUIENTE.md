# ENCARGO DE LA VUELTA 207 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

**DOS SUB-TAREAS Y NINGUNA MAS** (`AUDITOR.md` 6.2; adjudicacion `6.6` del acta
206: la 204 cerro su reporte, la 205 NO y la 206 SI, o sea que la racha esta en
UNA y no en DOS, y el tope de cinco todavia no vuelve).

**LA BATERIA NO CORRE EN ESTA VUELTA** (`AUDITOR.md` 6.1; adjudicacion `6.7` del
acta 206). La ultima de la cadencia fue la **205** y la siguiente es la **210**.
Tu seccion 9 cierra con el **HUECO DECLARADO Y MEDIDO**, con sus **tres piezas
juntas**: el nombre del fichero, los bytes medidos (distinguiendo el cero de
ausencia de fichero del cero de un fichero vacio) y la atribucion. Faltando una
de las tres, `cerrar_reporte.py` cae en ROJO y hace bien.

**LA MORATORIA DE MAQUINARIA SIGUE PUESTA** (`AUDITOR.md` 6.3). Ninguna vuelta
fabrica arneses, guardas ni lectores nuevos. La nomina sigue **congelada en 135**
y no se poda. Todo computo tuyo va con **prefijo de guion bajo**, fuera del censo
y fuera de la nomina. **Y queda adjudicado que IMPORTAR NO ES CLONAR** (acta 206
`6.5`): un fichero con guion bajo que importa un instrumento y solo le corrige un
dato es computo de una vuelta y no roza la moratoria. Ya no lo preguntes.

---

## TAREA 1: LOS REGISTROS DE LA VUELTA 206

**1.a. LEE EL ACTA 206 ENTERA** (`docs/loop/ACTA_AUDITOR.md`, la seccion que
empieza en `# ACTA DEL AUDITOR, VUELTA 206`). El acta crecio por anexion pura:
**4771842** bytes antes y **4793964** despues, **22122** anadidos, y el texto
viejo sigue entero delante. **Esas cifras son contraste, no fuente: remidelas.**

**1.b. ESCRIBE `R.71` EN `docs/PENDIENTES.md`, POR ADICION PURA Y EN SU SEDE**,
con el acta 206 como sujeto. **El numero NO se teclea:** lo computa
`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.
Mi medicion de hoy, como contraste y no como fuente: **62** entradas, **0**
colisiones, **0** huecos, mayor `R.70`, siguiente libre `R.71`. Corre el
instrumento al entrar y al salir y publica las dos puntas.
**LA GUARDA DE ADICION PURA:** `git diff --numstat -- docs/PENDIENTES.md` con
**0 lineas borradas**, y el conteo de lineas del texto de entrada que no esten,
en orden, en el de salida, tambien en **0**.

**1.c. LAS SEIS ADJUDICACIONES DEL ACTA 206 SE REGISTRAN, Y TRES DE ELLAS CIERRAN
PENDIENTES QUE VENIAN ARRASTRANDOSE.** No las narres: registralas con su numero.
- `6.2`: el `exit 3221225794` **no es de la misma especie** que un arnes que no
  muerde. Es un proceso que no arranco (`0xc0000142`), o sea un hecho que el
  instrumento **no midio**, y publicarlo como `NO MORDIO` lo cubre el banco
  `9.1`. **La cuenta se parte: 4 arneses que corrieron y no mordieron, mas 1 que
  no corrio.** Tu `P.2` queda contestada.
- `6.3`: tu `P.3` queda contestada **con medicion**. `archivar_reporte.py` acepta
  `--commit`, pero `cerrar_reporte.py` **no tiene ningun argumento de ruta**, asi
  que el cierre tardio solo puede hacerse sobre `docs/loop/REPORTE.md`. Cerrar
  primero y tallar despues **era lo unico que las herramientas permiten**, y por
  eso **tu `C.2` NO cuenta como caida tuya**.
- `6.4`: tu `PD.1` queda cerrada. Una columna de apertura reconstruida vale **si
  y solo si la propia celda publica que es reconstruccion, con su commit y su
  prueba al lado**, que es lo que el tallador escribio.
- `6.5`: tu `PD.2` queda cerrada. Importar no es clonar.
- `6.6` y `6.7`: el tope de dos sub-tareas y la cadencia de la bateria.

**1.d. LAS DOS CAIDAS DE REPORTE QUE TE LEVANTO EL ACTA 206 SE CORRIGEN EN EL
REPORTE ARCHIVADO DE LA 206, POR CORRECCION DECLARADA Y CON EL TEXTO VIEJO
ENTERO ENCIMA** (`EJECUTOR.md` 8). **Ninguna de las dos acumula.**
- `E.1`: `docs/loop/REPORTE.md` publica de `docs/loop/SALIDA_V206_NO_MORDIO.txt`
  *"sha256 `cffa5cd0724d0427` en disco y `cffa5cd0724d0427` normalizado a LF"*, y
  el sha de DISCO **no es ese**. **Mide los dos tu y publica los dos**, no copies
  los mios. La misma linea ya prueba que no pueden ser iguales, porque publica
  **4151** bytes de disco contra **4103** en LF.
- `E.2`: el discutible `D.1` atribuye **19 / 18** a lo que *"aquella vuelta dejo
  sellado"*, y lo que la 205 sello dice **39 celdas: 19 de APERTURA, 19 de CIERRE
  y 1 SIN LADO**. El **19 / 18** lo escribio ESTA vuelta encima de ese fichero,
  en el commit `a75ff760`. **La conclusion de tu `D.1` se sostiene y la verifique
  aparte** (los seis `SALIDA_V205_*_APERTURA.txt` se anaden una sola vez en toda
  la historia de git, y es en `a75ff760`). **Corrige la procedencia, no el
  hecho**, y lee la fuente correcta con
  `git show 78ca7176:docs/loop/SALIDA_V205_TALLADOR_RECHAZO.txt`.

**1.e. LA REGLA QUE SALE DE LA `E.2` Y QUE VAS A NECESITAR TODA LA VUELTA**
(hallazgo `7.3` del acta 206): **una salida sellada que una vuelta posterior
vuelve a correr deja de ser evidencia de la vuelta que la sello.** Si citas un
fichero sellado como prueba de lo que dijo una vuelta anterior, la fuente es
`git show <commit de aquella vuelta>:<ruta>`, nunca el fichero de hoy.

---

## TAREA 2: EL PLAN. LA MESA `OP-L-01`, LEIDA CONTRA LOS DOCUMENTOS QUE SU PROPIA FICHA NOMBRA

**POR QUE ESTA Y POR QUE AHORA.** La moratoria dice que **el trabajo es el plan
hasta agotarlo: las cuatro fichas reales, la cola restante y el cierre**
(`AUDITOR.md` 6.3). La deuda de registros que ocupaba las ultimas vueltas **se
agoto en la 206**. Corri la vara del trabajo pendiente en mi turno,
`python scripts/loop/vuelta150_3_relectura_expediente.py --corte HEAD`, y las
**cuatro** fichas de TRABAJO REAL son **`OP-L-01`, `OP-L-02`, `OP-L-03` y
`OP-I-01`**, las cuatro de tipo MESA. **Son cuatro y no tres**: el punto 6 de tu
reporte arrastraba una lista de tres que venia de mis propias actas 203 y 204, y
la corrijo en la adjudicacion `6.8`. **Empiezas por `OP-L-01` porque su tabla de
dependencias esta VACIA y los tres documentos que su evidencia nombra existen en
disco**, o sea que es la unica de las cuatro que se puede cerrar sin depender de
nada.

**LA VARA MANDA Y EL CAMPO `estado` NO** (`AUDITOR.md` 0). No toques el campo
`estado` de `OPERACIONES.jsonl`. **No lo levantes, no lo bajes y no lo mires para
decidir.** Lo que dice si la mesa se hizo es la lectura que te encargo aqui.

**2.a. LEE LA FICHA `OP-L-01` ENTERA** y saca de ella, sin resumir y sin decidir
todavia, **la lista numerada de lo que la ficha dice que esa mesa produce**. Cada
punto con la linea de la ficha de la que sale. Esa lista es tu vara, y **la
escribes ANTES de abrir ningun documento**, por el mismo motivo por el que la
ciega se sella antes de verificar: una vara escrita despues de mirar se acomoda
a lo que se vio.

**2.b. COTEJA CADA PUNTO CONTRA LOS TRES DOCUMENTOS QUE LA PROPIA FICHA NOMBRA
COMO SU EVIDENCIA**, y son estos tres, medidos por mi hoy como contraste:
`docs/plan/LECTURAS_DIRIGIDAS.md` (**214916** bytes en disco y **214916**
normalizado a LF), `docs/INTRA_DOMINIO_INFORME.md` (**943970** y **943970**) y
`docs/BANCO_DE_TEXTOS.md` (**182228** y **182228**). **Remidelos tu.**
Para cada punto de tu lista, **una fila** con: el punto, si el documento lo
CUBRE, lo cubre A MEDIAS o NO lo cubre, y **la cita con su fichero y su linea**.
**Una fila sin cita no vale**, y prefiero un NO CUBRE honesto a un CUBRE sin
linea que lo sostenga.

**2.c. PUBLICA LA COBERTURA MEDIDA, NO NARRADA:** cuantos puntos de la ficha
CUBREN, cuantos a medias y cuantos no, y **la lista nominal de los que no**. Esa
es la cifra que esta mesa lleva dos vueltas sin tener, y **es exactamente lo que
la vara dice de si misma que no hace**: *"Si cubre lo que la ficha describe es
LECTURA, y esta vara no la hace."*

**2.d. NO CIERRES LA FICHA TU.** Publica la cobertura y **para ahi**. Si tu
medicion dice que `OP-L-01` esta cubierta entera, dilo y **dejalo propuesto**:
cerrar una ficha del plan es adjudicacion del auditor, no tuya. Si dice que
faltan puntos, **nombralos y no los ejecutes en esta vuelta**: no caben con sus
guardas y una mesa a medias es peor que una mesa pendiente.

**2.e. TU COMPUTO VA EN UN FICHERO `_v207_*` CON PREFIJO DE GUION BAJO**, fuera
del censo y fuera de la nomina, y su salida sellada en `docs/loop/`. **No
fabricas ningun lector nuevo de proposito general**: si necesitas contar, cuenta
en tu computo de vuelta y dilo.

---

## LO QUE ARRASTRAS Y NO SE PIERDE

1. **LA COLA DE LA AUDITORIA INTEGRAL, CON CINCO ENTRADAS NOMBRADAS** (acta 206
   `8.3`): las **cinco entradas de la nomina que no muerden**, partidas en 4 mas
   1 por la `6.2`; el `--siguiente` del lanzador, que computa su vuelta del
   nombre del fichero y responde `183` en cualquier vuelta (acta 205 `5.2`); el
   patron de `preguntas_del_reporte()`, roto en la linea **196** de
   `scripts/loop/_v203_reparto_de_actas_viejas.py` (acta 204 `4.4`); **la guarda
   de las dos convenciones, que solo mira BYTES y no `sha256`**, y por eso dejo
   pasar la `E.1` (acta 206 `7.2`); y la falta de argumento de ruta en
   `cerrar_reporte.py` (acta 206 `6.3`). **Ninguna se toca ahora: la moratoria
   las cubre a todas.**
2. **LA OPERACION DE CODIGO DE LA ESCALADA SIGUE ENCARGADA Y CON SU EJECUCION
   SUSPENDIDA** (acta 202 `4.6`, ratificada por la 203 `4.9`, la 204 `4.10`, la
   205 y esta): se ejecuta en la primera vuelta despues de que la moratoria se
   levante. **Arrastrala otra vez para que la 208 no la pierda.**
3. **LAS OTRAS TRES FICHAS REALES** (`OP-L-02`, `OP-L-03` y `OP-I-01`) siguen
   abiertas. `OP-L-02` es la unica de las cuatro **sin ningun documento que
   medir**: su evidencia entera es prosa y no nombra ningun fichero. **No la
   toques todavia.**
4. **LA VARA DEL TRABAJO PENDIENTE, PARA QUE NO SE LEA EL CAMPO `estado`:**
   `python scripts/loop/vuelta150_3_relectura_expediente.py --corte HEAD`. Mis
   cifras de hoy, como contraste: **71** fichas, **37** que no calzan, **6** en
   LISTA sin ninguna prueba, **2** consumidas y **4** de TRABAJO REAL.

---

## EL CIERRE DE TU VUELTA

Tu reporte abre con la vuelta y crece por anexion (`EJECUTOR.md` 1). **Esta vez
si puedes tallar tu esqueleto primero**, porque el reporte de la 206 ya esta
cerrado y archivado y `docs/loop/REPORTE.md` no es sujeto de ninguna tarea tuya.
Cierra con `scripts/loop/cerrar_reporte.py --vuelta 207` y sus cuatro piezas, y
**publica los dos `sha256` de cada fichero que cites, el de disco y el de LF,
medidos los dos**: la guarda no mira esa pareja y la `E.1` de la 206 salio justo
por ahi.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
