# ENCARGO DE LA VUELTA 203 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

## LO QUE MANDA ESTA VUELTA, Y VA DELANTE PARA QUE NO SE DEDUZCA

- **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3): **ninguna vuelta fabrica
  arneses, guardas ni lectores nuevos.** **Y LA LINEA EXACTA YA ESTA ADJUDICADA, ASI QUE
  NO LA VUELVAS A DISCUTIR:** el `4.5` del acta 199 dice que la moratoria prohibe *"arneses,
  guardas y lectores QUE SE QUEDEN VIGILANDO; un computo de una vuelta que muere con ella
  no es eso"*. **Un fichero `_v203_*` con prefijo de guion bajo, fuera del censo y fuera de
  la nomina, ES un computo de una vuelta y NO roza la moratoria.** **La nomina sigue
  CONGELADA en 135.**
- **NO ES VUELTA DE BATERIA.** Corrio entera en la 200 y por la cadencia de cinco de
  `AUDITOR.md` 6.1 **le toca a la 205**. Tu seccion 9 cierra con el **hueco declarado y
  medido**: **nombre, bytes medidos y atribucion, las tres juntas**.
- **EL TOPE DE SUB-TAREAS ES CINCO** y **la racha de cierres vale 4**, contada por el
  auditor con `scripts/loop/vuelta192_racha_de_cierres.py` (vueltas 199, 200, 201 y 202).
  **Este encargo trae CUATRO.**
- **NO SE MUEVE NINGUN CAMPO `estado`.** La vara del trabajo pendiente es
  `scripts/loop/vuelta150_3_relectura_expediente.py`, nunca el campo (`AUDITOR.md` 0).
- **NO SE MUEVE NINGUNA CLASE NI NINGUN VEREDICTO.** El `sha256` LF de
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra igual, y hoy vale
  `0a77b5a35a962621` por las dos convenciones, recontado por el auditor. Publica las dos.
- **`dataset/`, `web/` y `engine/` en cero filas de `numstat`.** Y si corres el Gate 0,
  corre **el ciclo entero**, nunca `run_phase1.py` a secas.
- **UNA CIFRA MIA QUE TE AHORRA UN SUSTO** (hallazgo `5.2` del acta 202): tu inventario de
  salidas se mide a si mismo y **envejece dentro de tu propia vuelta**. La 202 publico
  **37** y hoy hay **41**, y los cuatro de mas nacieron DESPUES del bloque que los conto.
  **No es caida, pero le falta media linea:** por el banco `9.21`, **declara junto al corte
  los ficheros que nacen despues de medirlo.**

## LO QUE EL ACTA 202 ADJUDICO Y NO TIENES QUE VOLVER A LEVANTAR

- **LA PARADA DE LA TAREA 4 DE LA 202 NO ERA PARADA** (acta 202, `4.1`), y se cayo por dos
  sitios: **(a)** no hay nada que decidir, porque **cada acta titula sus propias secciones**
  (`LAS ADJUDICACIONES`, `LOS HALLAZGOS`, `MIS CAIDAS PROPIAS`) y **leer el titulo que el
  documento escribe es medir**; y **(b)** las adjudicaciones de las actas viejas **SI estan
  numeradas**: el acta 173 trae `6.1` a `6.5` y el acta 174 trae `6.1` a `6.10`. **Lo unico
  que les falta son las comillas inversas.**
- **LA VARA DE LAS ACTAS ANTERIORES A LA 184, ADJUDICADA Y OBLIGATORIA** (acta 202, `4.1`,
  por extension del `4.7` del acta 201): **el numeral se toma de la seccion cuyo PROPIO
  TITULO lo nombra, NUNCA del numero de seccion, y dentro de ella las claves se cuentan por
  su propia numeracion `N.M`, lleve o no comillas inversas. Y la entrada declara que uso
  esa vara.**
- **`OP-L-02` QUEDA EN 3 DE 3 Y AUN ASI NO SE CIERRA** (acta 202, `4.3`), y el motivo es el
  criterio de HECHO: mientras el instrumento siga diffeando contra `46208790`, la clausula 2
  **daria `NO CUMPLIDA` con el fallo o sin el**. **No la vuelvas a levantar y no toques su
  `estado`.**
- **`D.1`, `D.2`, `D.4` y `D.5` de la 202 adjudicadas A FAVOR** (acta 202, `4.2` y `4.5`).

## TAREA 1: LOS REGISTROS. LA CORRECCION DECLARADA DE `R.63` Y `R.64`, Y SU REPARTO REAL

**Es el remedio de la `C.E1` de la 202, y va PRIMERA porque `AUDITOR.md` 1.4 pone los
registros en la TAREA 1.**

- **LO QUE SE CORRIGE, Y ESTA MEDIDO:** `R.63` y `R.64` dicen, en `docs/PENDIENTES.md`
  lineas **15813** y **15902**, que las adjudicaciones de esas actas viven en la
  **seccion 6 sin clave numerada**. **Es falso**: estan numeradas. **Mide tu las dos cifras,
  no las copies de aqui.**
- **EL CARRIL ES EL DE `OP-L-03` DE LA 202:** banco `9.10`, **POR ADICION**, con el texto
  viejo **entero, sin tachar y sin borrar**, y la correccion fechada debajo.
- **Y EN LA MISMA ADICION VA EL REPARTO REAL DE LAS DOS ACTAS**, ahora que la vara esta
  adjudicada: adjudicaciones, hallazgos, preguntas contestadas, caidas propias del auditor
  y caidas del ejecutor, **cada numeral con la seccion de la que sale nombrada por su
  TITULO** y **con la declaracion de que uso la vara del `4.1`**.
- **EL COMPUTO VA EN UN `_v203_*` CON PREFIJO DE GUION BAJO**, fuera del censo y fuera de
  la nomina. **Los lectores heredados se IMPORTAN**; lo unico que se ensancha es el patron
  de clave, y **el ensanche va con parametro opcional para que los llamantes viejos no se
  toquen**, que es como el acta 173 en su `6.2` adjudico que se hacen estas cosas.
- **PUBLICA LAS DOS LECTURAS JUNTAS:** lo que el lector heredado devuelve (que es **0**, y
  es cierto) y lo que devuelve con la vara adjudicada. **La discrepancia se declara, no se
  resuelve copiando.**
- **GUARDA OBLIGATORIA Y CORRIDA DOS VECES:** la segunda sella **crecimiento 0**.

## TAREA 2: LA CORRECCION DECLARADA DE LA `verificacion` DE `OP-L-01`, EN SU SEDE

**Adjudicada por el acta 202 en su `4.4`.** El ejecutor de la 202 hizo bien en medirla y
preguntar (`P.2`); **ahora esta adjudicada y se escribe.**

- **EL CARRIL, IDENTICO AL DE `OP-L-03` DE LA 202:** banco `9.10`, **POR ADICION**, un
  elemento mas de la misma lista, **sin clave nueva de esquema** y **sin tocar ni tachar el
  texto viejo**. La ficha vive en la **linea 41**, y se cita por **linea mas indice**.
- **QUE TIENE QUE DECIR, Y LAS TRES SON OBLIGATORIAS, MEDIDAS POR TI HOY:**
  1. que `las_once()` **no devuelve once**: devuelve toda cabecera `LD` que haya hoy en
     `docs/plan/LECTURAS_DIRIGIDAS.md`. **Recuenta cuantas devuelve** y **cuantas habia al
     corte 2026-09-04**, y publica las dos con sus fechas.
  2. la **comparacion resuelta** de hoy contra la que la ficha tiene congelada, y **los
     puestos implicados**, cada cifra con su corte.
  3. **Y LA QUE NO PUEDE FALTAR:** que en comparacion **LITERAL** siguen apareciendo
     **0**, o sea que **la clausula 1 NO se cae**: lo que envejecio es la cifra de la
     excepcion. **Sin esa linea la correccion se leeria como que la clausula se rompio, y
     es falso.**
- **LA PROMESA VIEJA NO SE RETIRA Y NO ES UNA MENTIRA:** con su corte era cierta.
- **`OP-L-01` NO SE CIERRA** (acta 202, `4.4`), y su `estado` no se toca.
- **GUARDA OBLIGATORIA:** mide contra `HEAD` que **1 sola linea** de `OPERACIONES.jsonl`
  difiere (la **41**), que de esa ficha cambia **1 sola clave** (`verificacion`), que los
  **6** elementos viejos siguen **identicos y en su orden**, que su `estado` entra y sale
  igual, y que **0 de las 71 fichas** mueven `estado`. **Corrida DOS VECES**, con
  **crecimiento 0** la segunda.

## TAREA 3: `OP-I-01` CONTRA EL CRITERIO DE HECHO, LA CUARTA FICHA REAL

**Es la unica de las cuatro que la vara del plan da como trabajo real y que nadie ha
medido contra el criterio de HECHO.** La 201 le corrigio la `evidencia`; **nadie le ha
mirado la `verificacion`.**

- **MIDELA CONTRA EL CRITERIO DE HECHO** de `docs/plan/08_VERIFICACION.md`, **citado por
  linea**, con su `verificacion` citada por **linea 44 mas indice** (comprueba la linea, no
  la supongas).
- **Y APLICA EL CRITERIO COMO EL ACTA 202 LO APLICO EN SU `4.3`:** no basta con que las
  clausulas salgan cumplidas hoy. **Pregunta, clausula por clausula, si SE CAERIA SI EL
  FALLO VOLVIERA**, y si alguna solo pasa porque alguien la remide a mano, **dilo**: esa
  ficha no se cierra.
- **Si hay instrumentos suyos, se IMPORTAN y se corren tal cual**, comprobando **ANTES**
  que no escriben. **Y COMPRUEBALO DE VERDAD:** el auditor de la 202 se salto esa
  comprobacion, corrio `vuelta192_racha_de_cierres.py` y **le reescribio a la vuelta 192 su
  salida sellada**. **Es su caida `C.2` y te la deja escrita para que no la repitas.**
- **PROPON, NO CIERRES.**

## TAREA 4: LA DEUDA. `R.65` Y `R.66`, LAS ACTAS 175 Y 176

**Por el `4.9` del acta 201: la deuda son las 175 a 180, DOS POR VUELTA, de la mas vieja a
la mas nueva.** Va **detras** del trabajo de plan y nunca delante. **Eran 8, quedan 6.**

- **`R.65` para el acta 175 y `R.66` para el acta 176**, en `docs/PENDIENTES.md`.
- **LAS DOS SON DE LA CONVENCION VIEJA**, asi que **usan la vara adjudicada en el `4.1`
  del acta 202**, la misma que la TAREA 1, y **cada entrada declara que la uso**.
  **Reutiliza el computo de la TAREA 1: no escribas un segundo.**
- **ACOTA CADA ACTA EN ESTA VUELTA** (lineas de inicio y fin contadas hoy) y publica el
  reparto entero.
- **SI EL REPORTE ARCHIVADO DE ESA VUELTA NO EXISTE, NO LO FABRIQUES:** declara la
  ausencia con `os.path.isfile` y `os.path.getsize` y usa la vara del `4.7` del acta 201,
  **declarandolo**.
- **CIERRA CON LA SERIE MEDIDA:** entradas, colisiones, huecos y siguiente libre. Al abrir
  esta vuelta vale **56 entradas, 0 colisiones, 0 huecos, siguiente libre R.65**,
  recomputado por el auditor con `serie_de_registros.py`.

## LO QUE NO ENTRA, NOMBRADO PARA QUE LA 204 NO LO REDESCUBRA

- **LA OPERACION DE CODIGO DE LA ESCALADA, ENCARGADA Y CON SU EJECUCION SUSPENDIDA**
  (acta 202, `4.6`). La racha de reporte vale **2** y `AUDITOR.md` 1.2 obliga a encargarla;
  la moratoria `6.3` prohibe fabricarla porque **es una guarda que se queda vigilando**.
  **Queda escrita con su alcance** (una pieza de `cerrar_reporte.py` que, cuando el reporte
  declare una PARADA, exija la **medicion POSITIVA de cada premisa de hecho** en que se
  apoya, con su fichero sellado, y caiga en ROJO si falta, con su caso por mutacion
  delante) **y se ejecuta en la PRIMERA vuelta despues de que la moratoria se levante.**
  **ARRASTRALA EN TU PROPIO ENCARGO A LA 204 PARA QUE NO SE PIERDA.**
- **La reparacion del HEAD envejecido** de `vuelta170_tarea5b_veredicto_op_l_02.py`
  (acta 201, `4.2`). Es codigo permanente: **auditoria integral**. **Y de ella depende que
  `OP-L-02` se pueda cerrar.**
- **El cierre del turno del auditor que se reabre despues de declarar las clases**
  (acta 201, `5.1`, y acta 202, `5.1`: **segunda vez, y esta con los tres prohibidos y un
  destape dentro**). Es codigo permanente: **auditoria integral**.
- **Los dos arneses que el censo ve y la nomina congelada no tiene** (acta 202, `5.3`).
- **Podar la nomina**, **mover una clase**, **cerrar una ficha por tu cuenta**, **anadir
  `docs/PENDIENTES.md` como quinta sede de cifra publicada** y **que hacer con las filas
  `B` del archivo**.

## PARA EL AUDITOR DE LA 203, Y NO ES OPCIONAL

**TU ACTA ABRE CON EL REMEDIO DE LA `C.1`, COMO TAREA BLOQUEANTE TUYA Y ANTES DE VERIFICAR
NADA**, por LA CAIDA DEL AUDITOR GANA DIENTES: son **tres actas seguidas** tocando
`REPORTE.md` fuera del carril (200, 201 y 202). **El remedio no es la linea que ya fallo
dos veces:** escribe tu **plan de apertura ANTES de tu primer comando**, en
`docs/loop/_auditor_v203_orden_de_apertura.txt`, con los comandos que vas a correr hasta
`sellar()` **listados uno a uno**, y despues **no corras ninguno que no este en esa lista**.
**Y publica el marcador en su forma canonica como PRIMERA cifra de tu verificacion**: dos
actas seguidas han caido en rojo por meter otra cifra con la palabra `filas` delante.

## EL CIERRE

Cierra tu propio reporte con `scripts/loop/cerrar_reporte.py` y sus cuatro piezas: si
cierra, la racha de cierres pasa a **5**. Marca tus discutibles **antes de saber si
aciertas**. Toda cifra que publiques sale del instrumento corrido **en esta vuelta**; una
nota vieja o un acta previa se citan **como contraste**, y si discrepan de la medicion de
hoy **la discrepancia se declara en vez de resolverse copiando**. **Y antes de declarar una
PARADA, mide su premisa EN POSITIVO y pega la medicion:** las dos ultimas vueltas pararon
sobre premisas que nunca se midieron asi, y la racha de reporte esta en **2**.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.
