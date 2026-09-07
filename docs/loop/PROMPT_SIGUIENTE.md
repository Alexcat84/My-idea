# ENCARGO DE LA VUELTA 204 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

## LO QUE MANDA ESTA VUELTA, Y VA DELANTE PARA QUE NO SE DEDUZCA

- **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3): **ninguna vuelta fabrica
  arneses, guardas ni lectores nuevos QUE SE QUEDEN VIGILANDO**, y esa linea ya esta
  adjudicada en el `4.5` del acta 199: **un fichero `_v204_*` con prefijo de guion bajo,
  fuera del censo y fuera de la nomina, ES un computo de una vuelta y NO roza la
  moratoria.** **La nomina sigue CONGELADA en 135.**
- **NO ES VUELTA DE BATERIA. LE TOCA A LA 205**, por la cadencia de cinco de
  `AUDITOR.md` 6.1. Tu seccion 9 cierra con el **hueco declarado y medido**: **nombre,
  bytes medidos y atribucion, las tres juntas**.
- **LA RACHA DE CIERRES VALE 5** si el auditor confirma el cierre de la 203, contada con
  `scripts/loop/vuelta192_racha_de_cierres.py`. **CUENTALA TU, NO LA COPIES DE AQUI**, y
  si el instrumento dice otra cosa, **declara la discrepancia**. Con racha por encima de
  dos el tope es de **CINCO** sub-tareas; **este encargo trae CUATRO**.
- **NO SE MUEVE NINGUN CAMPO `estado`.** La vara del trabajo pendiente es
  `scripts/loop/vuelta150_3_relectura_expediente.py`, nunca el campo (`AUDITOR.md` 0).
- **NO SE MUEVE NINGUNA CLASE NI NINGUN VEREDICTO.** El `sha256` de
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra igual, y al cerrar la 203 valia
  `0a77b5a35a962621` por las dos convenciones. **Publica las dos y remidelas tu.**
- **`dataset/`, `web/` y `engine/` en cero filas de `numstat`.** Y si corres el Gate 0,
  corre **el ciclo entero**, nunca `run_phase1.py` a secas.
- **DOS CIFRAS MIAS QUE TE AHORRAN UN SUSTO, LAS DOS APRENDIDAS EN ROJO EN LA 203.**
  **(a)** Una pareja de bytes **completa puede ser FALSA**: si pegas a una ruta el tamano
  que tenia **en mitad de la vuelta** y otra tarea vuelve a mover esa sede, la guarda
  recomputa del disco al cierre y **te tumba, con razon**. **Detras de cada ruta va SU
  tamano al cierre**; el intermedio se dice **sin nombrar la ruta**. **(b)** El markdown
  **parte la frase donde le cabe el ancho** y deja el numero solo en su renglon sin su
  pareja: **junta la cifra con su pareja en el MISMO renglon**. Las dos me tumbaron el
  cierre y las dos estan en la `C.6` de mi reporte.

## LO QUE EL ACTA 202 ADJUDICO Y SIGUE VIGENTE, PARA QUE NO SE VUELVA A LEVANTAR

- **LA VARA DE LAS ACTAS ANTERIORES A LA 184** (acta 202, `4.1`, por extension del `4.7`
  del acta 201): **el numeral se toma de la seccion cuyo PROPIO TITULO lo nombra, NUNCA
  del numero de seccion, y dentro de ella las claves se cuentan por su propia numeracion
  `N.M`, lleve o no comillas inversas. Y la entrada declara que uso esa vara.**
- **`OP-L-02` QUEDA EN 3 DE 3 Y AUN ASI NO SE CIERRA** (acta 202, `4.3`), porque mientras
  el instrumento siga diffeando contra `46208790` la clausula 2 **daria `NO CUMPLIDA` con
  el fallo o sin el**. **No la vuelvas a levantar y no toques su `estado`.**
- **`OP-L-01` NO SE CIERRA** (acta 202, `4.4`), y su correccion de `verificacion` ya esta
  escrita por la 203 en su TAREA 2. **No se repite.**

## TAREA 1: LOS REGISTROS. `R.67` Y `R.68`, LAS ACTAS 177 Y 178

**Por el `4.9` del acta 201: la deuda son las 177 a 180, DOS POR VUELTA, de la mas vieja
a la mas nueva. Eran 8, quedaban 6 y quedan 4.** Va **PRIMERA** porque `AUDITOR.md` 1.4
pone los registros en la TAREA 1.

- **`R.67` para el acta 177 y `R.68` para el acta 178**, en `docs/PENDIENTES.md`.
- **COMPRUEBA TU DE QUE CONVENCION SON**, no lo supongas: la 184 es la frontera, y si
  alguna de las dos ya escribe sus claves con comillas inversas **el lector heredado
  basta y se dice**. **La vara del `4.1` se declara igual, use la plantilla que use.**
- **REUTILIZA EL COMPUTO DE LA 203**, `scripts/loop/_v203_reparto_de_actas_viejas.py`:
  **impórtalo o clónalo con su cifra de difflib al lado, pero no escribas un tercero.**
  Si lo clonas, el clon es `_v204_*` y **publica cuantas lineas vienen sin tocar**.
- **ACOTA CADA ACTA EN ESTA VUELTA** (lineas de inicio y fin contadas hoy) y publica el
  reparto entero, **cada numeral con la seccion de la que sale nombrada por su TITULO**.
- **SI UN NUMERAL NO ES COMPUTABLE, DECLARALO EN VEZ DE PUBLICAR UN CERO.** La 203 midio
  que el acta 176 titula `LA CAIDA DEL EJECUTOR, CON SU NOMBRE` y escribe su caida como
  ``**CAIDA DE REPORTE 1:``, que ninguna de las dos formas numeradas ve: **publicar el 0
  habria sido un cero falso.** **Publica las tres lecturas** cuando discrepen.
- **COTEJA CONTRA LA FILA DE METRICA DE CADA ACTA**, que la escribio el auditor de
  aquella vuelta y no tu. En la 203 calzo en las cuatro actas y es la mejor prueba de que
  el computo no inventa nada.
- **SI EL REPORTE ARCHIVADO NO EXISTE, NO LO FABRIQUES**, y **si existe pero NO TITULA
  seccion de PREGUNTAS, tampoco vale el filtro**: eso es el `PD.1` de mi reporte, y hasta
  que se adjudique **se usa la vara del `4.7` del acta 201 DECLARANDOLO**.
- **CIERRA CON LA SERIE MEDIDA:** entradas, colisiones, huecos y siguiente libre. Al
  cerrar la 203 valia **58, 0, 0 y `R.67`**. **Recomputala tu.**
- **GUARDA OBLIGATORIA Y CORRIDA DOS VECES:** la segunda sella **crecimiento 0**.

## TAREA 2: LAS DOS CLAUSULAS DE `OP-I-01` QUE NO SE CAERIAN, MEDIDAS SIN FABRICAR VARA

**Adjudicado o no, esto NO cierra la ficha.** La 203 midio en su TAREA 3 que las clausulas
**2** (`toda forma con cobertura incompleta va marcada PROVISIONAL`) y **3** (`todo hueco
va NOMBRADO, nunca rellenado`) **no se caerian si el fallo volviera**, porque la clave
`cobertura` de `docs/plan/INVENTARIO.jsonl` es **texto libre**.

- **LO QUE SE PIDE ES MEDIR EL TAMANO DEL AGUJERO, NO TAPARLO.** Cuenta **cuantas formas
  distintas** toma hoy el campo `cobertura` en las **672** entradas (recuenta la cifra),
  **agrupadas por su forma**, y **cuantas entradas quedarian fuera de cualquier vara
  razonable**. **Publica la busqueda positiva**, nunca una negativa.
- **NO ESCRIBAS LA VARA.** Escribir la vara es maquinaria y la moratoria la prohibe: es
  la `P.3` de mi reporte. **Lo que esta vuelta produce es la MEDICION del agujero, para
  que quien la escriba despues sepa de que tamano es.**
- **EL INSTRUMENTO SE IMPORTA Y SE CORRE TAL CUAL, COMPROBANDO ANTES SI ESCRIBE.** Y si
  escribe, **dilo y usa el protocolo del sello**: medir, correr, restaurar con
  `git checkout --` y remedir. `vuelta169_tarea3_op_i_01.py` **SI escribe**, sobre
  `docs/loop/RECOMPUTO_V169.jsonl`, sellado en la vuelta 169. **Ya esta medido: no te
  sorprenda.**
- **PROPON, NO CIERRES.** Y **no toques el `estado`** de `OP-I-01`.

## TAREA 3: LA DISCREPANCIA DE COMPONENTES QUE EL PROPIO INSTRUMENTO DECLARA

**La 203 la reprodujo y no la persiguio, y eso se dice:** al correr
`vuelta169_tarea3_op_i_01.py` en esta vuelta, su bloque `E` publica que **el fichero
sellado de componentes trae 332 lineas** (**54 ABIERTO**, **278 CERRADO**) y **la corrida
de hoy da 47** (**21** y **26**), y su propio veredicto de reproduccion sale **`False`**.

- **MIDE DE DONDE SALE ESA DIFERENCIA**, con el resolutor delante por `P.1`, y
  **declarala**: cuantas componentes del sellado no estan hoy, cuantas hay hoy que no
  estaban, y **si la causa es el universo, la fecha o el instrumento**.
- **NO REGENERES LA NOMINA SELLADA.** `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` **se
  CUENTA, no se reescribe**, y esa es la letra del propio instrumento.
- **SI DE AQUI SALE QUE UNA CIFRA PUBLICADA ENVEJECIO, VA POR EL CARRIL DEL BANCO `9.10`,
  POR ADICION Y EN SU SEDE**, con el texto viejo entero y sin tachar. **Si sale que hace
  falta codigo, PARA Y LO TRAES.**

## TAREA 4: EL CENSO DE LO QUE QUEDA DEL PLAN, MEDIDO Y NO NARRADO

**Las cuatro fichas reales estan medidas: `OP-L-03` (202), `OP-L-02` (202), `OP-L-01`
(202 y 203) y `OP-I-01` (203). Ninguna se cerro, y las cuatro con su motivo escrito.**
**La pregunta que nadie ha contestado con una cifra es: QUE QUEDA.**

- **CUENTA LAS 71 FICHAS DE `docs/plan/OPERACIONES.jsonl` POR `estado`**, y **cruza esa
  cuenta con la vara del trabajo pendiente**, que es
  `scripts/loop/vuelta150_3_relectura_expediente.py` **y nunca el campo `estado`**.
- **PUBLICA LAS DOS LECTURAS JUNTAS Y DECLARA LA DISCREPANCIA** si la hay. **Ese cruce es
  el punto del encargo**, no la suma.
- **NINGUNA FICHA SE CIERRA Y NINGUN `estado` SE MUEVE.** Lo que esta tarea produce es
  **el mapa de lo que queda**, para que el fundador decida el orden.
- **NOMBRA, SIN RESOLVERLAS, LAS QUE YA ESTAN MEDIDAS Y NO SE PUEDEN CERRAR HOY**, con la
  linea del acta que lo adjudico al lado.

## LO QUE NO ENTRA, NOMBRADO PARA QUE LA 205 NO LO REDESCUBRA

- **LA OPERACION DE CODIGO DE LA ESCALADA, ENCARGADA Y CON SU EJECUCION SUSPENDIDA**
  (acta 202, `4.6`), **ARRASTRADA AQUI PARA QUE NO SE PIERDA**: una pieza de
  `cerrar_reporte.py` que, cuando el reporte declare una PARADA, exija la **medicion
  POSITIVA de cada premisa de hecho** en que se apoya, con su fichero sellado, y **caiga
  en ROJO si falta**, con su caso por mutacion delante. `AUDITOR.md` 1.2 obliga a
  encargarla y la moratoria `6.3` prohibe fabricarla porque **es una guarda que se queda
  vigilando**. **Se ejecuta en la PRIMERA vuelta despues de que la moratoria se levante.**
  **VUELVE A ARRASTRARLA EN TU ENCARGO A LA 205.**
- **LA VARA ESCRITA PARA `cobertura`**, que las clausulas 2 y 3 de `OP-I-01` necesitan
  para caerse. Es codigo permanente: **auditoria integral**.
- **La reparacion del HEAD envejecido** de `vuelta170_tarea5b_veredicto_op_l_02.py`
  (acta 201, `4.2`). **De ella depende que `OP-L-02` se pueda cerrar.**
- **El cierre del turno del auditor que se reabre despues de declarar las clases**
  (acta 201, `5.1`; acta 202, `5.1`).
- **Los dos arneses que el censo ve y la nomina congelada no tiene** (acta 202, `5.3`).
- **Podar la nomina**, **mover una clase**, **cerrar una ficha por tu cuenta**, **anadir
  `docs/PENDIENTES.md` como quinta sede de cifra publicada** y **que hacer con las filas
  `B` del archivo**.

## PARA EL AUDITOR DE LA 204

**LA 203 NO TOCO `REPORTE.md` FUERA DEL CARRIL Y NO LEVANTO NINGUNA PARADA**, asi que el
remedio bloqueante de la `C.1` de tu acta anterior **solo se repite si la 203 reincidio**;
**mide antes de exigirlo.** **Publica el marcador en su forma canonica como PRIMERA cifra
de tu verificacion.** Y **ANTES DE CORRER CUALQUIER INSTRUMENTO, COMPRUEBA SI ESCRIBE**:
el de la racha y el de `OP-I-01` **los dos escriben**, y los dos estan medidos por la 203.

**Y HAY TRES COSAS DE LA 203 QUE PIDEN ADJUDICACION, NO OPINION:** el `D.1` (un parametro
opcional en un fichero permanente bajo la moratoria, que el encargo mando), el `D.3` (la
regla de cuando un numeral de caidas es computable) y el `PD.1` (un reporte archivado que
existe pero no titula seccion de PREGUNTAS).

## EL CIERRE

Cierra tu propio reporte con `scripts/loop/cerrar_reporte.py` y sus cuatro piezas. Marca
tus discutibles **antes de saber si aciertas**. Toda cifra que publiques sale del
instrumento corrido **en esta vuelta**; una nota vieja o un acta previa se citan **como
contraste**, y si discrepan de la medicion de hoy **la discrepancia se declara en vez de
resolverse copiando**. **Y antes de declarar una PARADA, mide su premisa EN POSITIVO y
pega la medicion.**

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.
