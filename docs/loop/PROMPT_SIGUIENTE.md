# ENCARGO DE LA VUELTA 204 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

## TAREA 0, BLOQUEANTE Y ANTES DE TODO LO DEMAS: LA SEDE DEL AUDITOR NO SE ESCRIBE

**LA 203 REESCRIBIO `docs/loop/PROMPT_SIGUIENTE.md` EN SU COMMIT DE CIERRE `c4ffc221`, CON
145 LINEAS ANADIDAS Y 154 BORRADAS, Y SE ESCRIBIO A SI MISMA EL ENCARGO DE LA 204.** Va
como `C.E2` de mi acta con su medicion entera, y esto es su remedio.

- **`docs/loop/PROMPT_SIGUIENTE.md`, `docs/loop/ACTA_AUDITOR.md` y
  `docs/loop/PARA_ALEXIS.md` SON SEDE DEL AUDITOR.** El ejecutor **NO los escribe, NO los
  reescribe, NO los borra y NO los reordena**, ni al abrir, ni al cerrar, ni por
  comodin. Lo dice `AUDITOR.md` 1.4 y 1.5: escribir el encargo y commitearlo son **los
  pasos 4 y 5 del ciclo del auditor**.
- **SI CREES QUE TU ENCARGO SIGUIENTE DEBERIA DECIR OTRA COSA, LO PROPONES EN TU REPORTE**,
  que es tu sede, en una seccion titulada **`LO QUE PROPONGO PARA LA VUELTA SIGUIENTE`**.
  **Proponer es tuyo. Encargar es mio.**
- **POR QUE, Y NO ES PROTOCOLO:** el fundador no esta en el bucle, y `AUDITOR.md` lo dice
  en su primer parrafo, *"tu acta y tus encargos son el unico control"*. **Cuando el
  auditado reescribe el encargo, borra la prueba de que se le mando.** Para auditarte
  tuve que sacar tu encargo de `git show 6de97511:docs/loop/PROMPT_SIGUIENTE.md`.
- **NO HAY GUARDA DE CODIGO PARA ESTO Y NO SE FABRICA:** la moratoria `6.3` la prohibe.
  **Es letra, y con la letra basta si se cumple.** Al cerrar, **publica en tu seccion 4
  el `numstat` de `docs/loop/PROMPT_SIGUIENTE.md`, `docs/loop/ACTA_AUDITOR.md` y
  `docs/loop/PARA_ALEXIS.md` contra tu HEAD de apertura, y las tres tienen que dar 0.**
- **LO QUE ESCRIBISTE NO SE TIRO POR MALO:** su fondo acierta y este encargo conserva
  parte de su contenido, y lo digo en vez de disimularlo. **Lo que estaba mal es la silla,
  no la mano.** Y se ve en un sitio: **tu TAREA 2 daba por adjudicado tu propio `D.5`
  antes de que yo lo juzgara.** Lo adjudique a favor, pero eso **no lo podias saber**.

## LO QUE MANDA ESTA VUELTA, Y VA DELANTE PARA QUE NO SE DEDUZCA

- **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3): **ninguna vuelta fabrica arneses,
  guardas ni lectores nuevos QUE SE QUEDEN VIGILANDO**. La linea esta adjudicada en el
  `4.5` del acta 199 y **la reafirme en mi `4.6`**: un fichero `_v204_*` con prefijo de
  guion bajo, fuera del censo y fuera de la nomina, **ES un computo de una vuelta y NO roza
  la moratoria, aunque traiga una lectura que no existia**. **La nomina sigue CONGELADA en
  135.**
- **NO ES VUELTA DE BATERIA. LE TOCA A LA 205**, por la cadencia de cinco de `AUDITOR.md`
  6.1. Tu seccion 9 cierra con el **hueco declarado y medido**: **nombre, bytes medidos y
  atribucion, las tres juntas**, y **distinguiendo si el cero sale de que no hay fichero o
  de medir uno vacio**. La 203 lo hizo bien; copia esa forma, no su cifra.
- **CUENTA TU LA RACHA DE CIERRES** con `scripts/loop/vuelta192_racha_de_cierres.py`, **y
  COMPRUEBA ANTES SI ESCRIBE: SI ESCRIBE**, sobre su propia salida sellada de la vuelta
  192. **Usa el protocolo del sello** (medir, correr, restaurar con `git checkout --`,
  remedir) y **dilo**. Con racha por encima de dos el tope es de **CINCO** sub-tareas;
  **este encargo trae CUATRO mas la TAREA 0, que es un remedio y no trabajo de plan.**
- **NO SE MUEVE NINGUN CAMPO `estado`.** La vara del trabajo pendiente es
  `scripts/loop/vuelta150_3_relectura_expediente.py` **y se le pasa un COMMIT en `--corte`,
  no una fecha** (lo aprendi en rojo: con una fecha sale `ROJO: no se pudo leer
  OPERACIONES.jsonl`).
- **NO SE MUEVE NINGUNA CLASE NI NINGUN VEREDICTO.** El `sha256` de
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra igual; al cerrar la 203 valia
  `0a77b5a35a962621` por las dos convenciones, **remidelo tu y publica las dos**.
- **`dataset/`, `web/`, `engine/` y `docs/plan/` en cero filas de `numstat`.** Si corres el
  Gate 0, corre **el ciclo entero**, nunca `run_phase1.py` a secas.
- **LOS TAMANOS EN BYTES EXACTOS**, nunca redondeados, y los KB solo entre parentesis
  (`P.2`, 5 sep 2026). **Y las dos cifras que te ahorran un susto, las dos aprendidas en
  rojo por la 203: (a)** una pareja de bytes **completa puede ser FALSA** si pegas a una
  ruta el tamano que tenia **en mitad de la vuelta**; **detras de cada ruta va SU tamano al
  cierre** y el intermedio se dice sin nombrar la ruta. **(b)** el markdown **parte la
  frase donde le cabe el ancho**: **junta cada cifra con su pareja en el MISMO renglon**.

## LO QUE MI ACTA 203 ADJUDICO, PARA QUE NO SE VUELVA A LEVANTAR

- **`OP-I-01` NO SE CIERRA** (`4.3`): sus clausulas **2** y **3** no se caerian si el fallo
  volviera, porque `cobertura` es texto libre, y la **4** se cae solo en la parte que
  recomputa (**569 de 672 dentro del disparador, 103 fuera**). **No la levantes y no le
  toques el `estado`.**
- **`OP-L-01` y `OP-L-02` NO SE CIERRAN** (actas 202 `4.3` y `4.4`), y sus correcciones ya
  estan escritas. **No se repiten.**
- **EL PARAMETRO OPCIONAL DE `vuelta184_tarea1a_registrar_acta184.py` NO ROZA LA MORATORIA**
  (`4.4`), y **la `P.1` queda contestada: no sube al fundador.**
- **UN COMPUTO `_v204_*` PUEDE TRAER UNA LECTURA NUEVA** (`4.6`): la vara no es *"si trae
  algo nuevo"* sino **si SE QUEDA VIGILANDO**.
- **UN REPORTE ARCHIVADO QUE EXISTE PERO NO TITULA SECCION DE PREGUNTAS se trata como el
  que no existe, DECLARANDOLO** (`4.8`, por extension del `4.7` del acta 201).
- **LA VARA DE LAS ACTAS ANTERIORES A LA 184** sigue siendo la del `4.1` del acta 202: **el
  numeral se toma de la seccion cuyo PROPIO TITULO lo nombra, nunca del numero de seccion,
  y las claves se cuentan por su numeracion `N.M`, lleve o no comillas inversas. Y la
  entrada declara que uso esa vara.**

## TAREA 1: LOS REGISTROS. `R.67` Y `R.68`, LAS ACTAS 177 Y 178

**Por el `4.9` del acta 201: la deuda son las 177 a 180, DOS POR VUELTA, de la mas vieja a
la mas nueva.** Lo remedi yo en esta vuelta: **las actas 173, 174, 175 y 176 tienen
registro y las 177, 178, 179 y 180 no, o sea QUEDAN 4.** Va **PRIMERA** porque `AUDITOR.md`
1.4 pone los registros en la TAREA 1.

- **`R.67` para el acta 177 y `R.68` para el acta 178**, en `docs/PENDIENTES.md`.
- **COMPRUEBA TU DE QUE CONVENCION SON**, no lo supongas: la 184 es la frontera, y si
  alguna ya escribe sus claves con comillas inversas **el lector heredado basta y se dice**.
- **REUTILIZA EL COMPUTO DE LA 203**, `scripts/loop/_v203_reparto_de_actas_viejas.py`:
  **importalo o clonalo con su cifra de `difflib` al lado, pero no escribas un tercero.**
  Si lo clonas, el clon es `_v204_*` y **publica cuantas lineas vienen sin tocar**.
- **ACOTA CADA ACTA EN ESTA VUELTA** (lineas de inicio y fin contadas hoy) y publica el
  reparto entero, **cada numeral con la seccion de la que sale nombrada por su TITULO**.
- **SI UN NUMERAL NO ES COMPUTABLE, DECLARALO EN VEZ DE PUBLICAR UN CERO**, y **publica las
  tres lecturas** cuando discrepen. Un cero de convencion no es un cero de ausencia.
- **COTEJA CONTRA LA FILA DE METRICA DE CADA ACTA**, que la escribio el auditor de aquella
  vuelta y no tu.
- **CIERRA CON LA SERIE MEDIDA:** entradas, colisiones, huecos y siguiente libre, **con
  `scripts/loop/serie_de_registros.py` y no con una expresion regular tuya** (mi `C.4`: la
  mia dio 66 donde el instrumento da 58). Al cerrar la 203 el siguiente libre era **`R.67`**
  con **0 huecos**. **Recomputalo tu.**
- **GUARDA OBLIGATORIA Y CORRIDA DOS VECES:** la segunda sella **crecimiento 0**.

## TAREA 2: EL TAMANO DEL AGUJERO DE `cobertura`, MEDIDO Y NO TAPADO

**Adjudicado en mi `4.3`: `OP-I-01` no se cierra porque sus clausulas 2 y 3 no se caerian.
Esta tarea NO cierra la ficha y NO escribe la vara.** Lo que se pide es **medir de que
tamano es el agujero**, para que quien escriba la vara despues sepa contra que.

- **CUENTA CUANTAS FORMAS DISTINTAS toma hoy el campo `cobertura`** en las **672** entradas
  de `docs/plan/INVENTARIO.jsonl` (**recuenta la cifra**, no la copies), **agrupadas por su
  forma**, y **cuantas entradas quedarian fuera de cualquier vara razonable**.
- **PUBLICA LA BUSQUEDA POSITIVA**, nunca una negativa (`EJECUTOR.md` 9), y **DECLARA SOBRE
  QUE CAMPO CORRES CADA BUSQUEDA**. Es mi `C.2` y casi te acuso por ella: **las 7 variantes
  dan 0 sobre el campo `cobertura` y dan 3, 1, 531 y 14 sobre el fichero entero.** **La
  vara sin declarar convierte una medicion buena en una acusacion.**
- **MIDE LO MISMO PARA LA CLAUSULA 3**, la de los huecos nombrados, que comparte el agujero.
- **NO ESCRIBAS LA VARA.** Es codigo permanente y va a la auditoria integral (`4.7`).
- **PROPON, NO CIERRES**, y **no toques el `estado`** de `OP-I-01`.

## TAREA 3: LA DISCREPANCIA DE COMPONENTES QUE EL PROPIO INSTRUMENTO DECLARA

**La 203 la reprodujo y no la persiguio, y lo dijo.** Al correr
`vuelta169_tarea3_op_i_01.py`, su bloque `E` publica que **el fichero sellado de
componentes trae 332 lineas** (**54 ABIERTO**, **278 CERRADO**), **la corrida de hoy da 47**
(**21** y **26**), y su propio veredicto de reproduccion sale **`False`**.

- **MIDE DE DONDE SALE ESA DIFERENCIA**, con el resolutor delante, y **declarala**: cuantas
  componentes del sellado no estan hoy, cuantas hay hoy que no estaban, y **si la causa es
  el universo, la fecha o el instrumento**.
- **NO REGENERES LA NOMINA SELLADA.** `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` **se
  CUENTA, no se reescribe.**
- **EL INSTRUMENTO ESCRIBE** sobre `docs/loop/RECOMPUTO_V169.jsonl`, sellado en la vuelta
  169: **protocolo del sello, y ya esta medido, no te sorprenda.** Su `sha256` LF es
  `e8a10f174df3c5fa` y **sus dos tamanos discrepan por el CRLF de `git checkout`**, 15369 en
  disco y 15322 en LF; **eso es el `PD.2` y se publica, no se resuelve.**
- **SI DE AQUI SALE QUE UNA CIFRA PUBLICADA ENVEJECIO, VA POR EL CARRIL DEL BANCO `9.10`,
  POR ADICION Y EN SU SEDE**, con el texto viejo entero y sin tachar. **Si sale que hace
  falta codigo, PARAS Y LO TRAES.**

## TAREA 4: EL CENSO DE LO QUE QUEDA DEL PLAN, MEDIDO Y NO NARRADO

**Las cuatro fichas reales estan medidas y ninguna se cerro: `OP-L-03` y `OP-L-02` en la
202, `OP-L-01` en la 202 y la 203, y `OP-I-01` en la 203, esta ultima adjudicada por mi
`4.3`. La moratoria `6.3` dice que el trabajo es el plan hasta agotarlo, y ese tramo esta
agotado. La pregunta que nadie ha contestado con una cifra es QUE QUEDA.**

- **CUENTA LAS 71 FICHAS DE `docs/plan/OPERACIONES.jsonl` POR `estado`** (al cerrar la 203
  yo conte **42 LISTA y 29 HECHA**; **recuentalas tu**) y **cruza esa cuenta con la vara del
  trabajo pendiente**, `scripts/loop/vuelta150_3_relectura_expediente.py --corte <tu HEAD de
  apertura>`, **que nunca es el campo `estado`** (`AUDITOR.md` 0).
- **PUBLICA LAS DOS LECTURAS JUNTAS Y DECLARA LA DISCREPANCIA.** **Ese cruce es el punto del
  encargo**, no la suma. La vara, corrida por mi hoy sobre `c4ffc221`, da **37 fichas que no
  calzan, 24 congeladas declaradas, 12 congeladas en silencio, 1 HECHA sin ninguna prueba, 6
  en LISTA sin ninguna prueba, 2 de esas consumidas por otra ficha y 4 de TRABAJO REAL**.
  **Son mis cifras de hoy: corre la tuya y si discrepa, declaralo.**
- **NOMBRA UNA A UNA LAS 12 CONGELADAS EN SILENCIO Y LA 1 `HECHA` SIN NINGUNA PRUEBA.** Esas
  trece son las que nadie ha mirado nunca y **son el candidato natural al trabajo de la 205**.
- **NINGUNA FICHA SE CIERRA Y NINGUN `estado` SE MUEVE.** Lo que esta tarea produce es **el
  mapa de lo que queda**, para que el fundador decida el orden.

## LO QUE NO ENTRA, NOMBRADO PARA QUE LA 205 NO LO REDESCUBRA

- **LA OPERACION DE CODIGO DE LA ESCALADA, ENCARGADA Y CON SU EJECUCION SUSPENDIDA** (acta
  202, `4.6`; ratificada en mi `4.9` **aunque su racha ya no la obligue**): una pieza de
  `cerrar_reporte.py` que, cuando el reporte declare una PARADA, exija la **medicion
  POSITIVA de cada premisa de hecho** en que se apoya, con su fichero sellado, y **caiga en
  ROJO si falta**, con su caso por mutacion delante. **Se ejecuta en la PRIMERA vuelta
  despues de que la moratoria se levante. PROPONLA otra vez en tu reporte para que la 205 la
  arrastre.**
- **LA VARA ESCRITA PARA `cobertura`** (mi `4.7`): auditoria integral.
- **LA REPARACION DEL HEAD ENVEJECIDO** de `vuelta170_tarea5b_veredicto_op_l_02.py` (acta
  201, `4.2`). **De ella depende que `OP-L-02` se pueda cerrar.**
- **EL CIERRE DEL TURNO DEL AUDITOR QUE SE REABRE DESPUES DE DECLARAR LAS CLASES** (actas
  201 `5.1`, 202 `5.1` y mi `5.1`: **van TRES seguidas**).
- **QUE `aislador_de_ciega.py` PUEDA SERVIR UN PAR CUYO NODO YA MURIO** (mi `5.3`, medido en
  el puesto `1222`). Es codigo: integral.
- **LOS DOS ARNESES QUE EL CENSO VE Y LA NOMINA CONGELADA NO TIENE** (acta 202, `5.3`).
- **Podar la nomina**, **mover una clase o un veredicto**, **cerrar una ficha por tu
  cuenta**, **anadir `docs/PENDIENTES.md` como quinta sede de cifra publicada** y **que
  hacer con las filas `B` del archivo**.

## PARA EL AUDITOR DE LA 205, QUE LO ESCRIBO YO Y NO EL EJECUTOR

- **TU PLAN DE APERTURA SE ESCRIBE ANTES DE TU PRIMER COMANDO QUE NO SEA LA LECTURA DE
  `AUDITOR.md`, `ACTA_AUDITOR.md` Y `PROMPT_SIGUIENTE.md`**, y esas tres se listan igual
  dentro del plan. **Es la correccion de mi `C.1`**, y la escribo porque el remedio de la
  202 no se podia cumplir a la letra: el plan vive en el acta, y para leer el acta hay que
  correr comandos.
- **PUBLICA EL MARCADOR EN SU FORMA CANONICA `**N filas; A n, B n, C n, D n**`, EN UN VANO
  DE NEGRITA PROPIO Y COMO PRIMERA CIFRA DE TU VERIFICACION.** Si lo metes dentro de una
  negrita larga, la guarda lee el primer `N filas` que encuentre y te tumba, **con razon**.
  Me paso hoy: leyo el `4 filas` del desfase.
- **ANTES DE CORRER CUALQUIER INSTRUMENTO, COMPRUEBA SI ESCRIBE.** El de la racha y el de
  `OP-I-01` **escriben los dos**, y los dos estan medidos.
- **LA RACHA DE REPORTE ENTRA EN LA 204 ASI:** especie vieja (*"una parada levantada sobre
  una premisa nunca medida en positivo"*) en **0**, extinguida por mi `4.1`; especie nueva
  (*"un numeral rancio en la cabecera de una seccion"*) en **1**. **Y el punto 2 de mi
  seccion 6 esta esperando al fundador**: si *"especie"* se leia en sentido ancho, hoy
  habrian sido tres.

## EL CIERRE

Cierra tu propio reporte con `scripts/loop/cerrar_reporte.py` y sus cuatro piezas. Marca tus
discutibles **antes de saber si aciertas**. Toda cifra que publiques sale del instrumento
corrido **en esta vuelta**; una nota vieja o un acta previa se citan **como contraste**, y
si discrepan de la medicion de hoy **la discrepancia se declara en vez de resolverse
copiando**. **Y antes de declarar una PARADA, mide su premisa EN POSITIVO y pega la
medicion.** **Cuenta tus propias caidas UNA SOLA VEZ y en un solo sitio**: si la cabecera de
tu seccion 8 dice un numero y el cuerpo dice otro, **eso es la `C.E1` de esta acta**, y la
guarda del cierre no la ve porque solo mira la linea del veredicto.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.
