Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

AVISO SOBRE ESA PRIMERA LINEA, Y VA PRIMERO PORQUE HOY DICE ALGO DISTINTO
DE LO QUE PARECE: YO YA COMMITEE LO PENDIENTE. Al abrir esta vuelta el
arbol tiene que estar LIMPIO, y lo unico que veras en `git status` es
`dataset/metadata/master_graph.json` marcado ` M` con su
`git diff --numstat` VACIO. Eso NO ES TRABAJO PENDIENTE Y NO SE
COMMITEA: es ruido de fin de linea, cero lineas de contenido en el diff,
lo medi yo hoy. Si ademas ves lineas de `etiqueta_arbol` en el diff, ESO
tampoco es trabajo: es el borrado de la curaduria que deja detras
cualquier corrida de `run_phase1.py`, y se repara corriendo
`python scripts/etiquetas_de_cara.py --aplicar` y
`python scripts/sync_assets_web.py` hasta que
`git diff --numstat -- dataset/ web/ engine/` quede VACIO.
SI ENCUENTRAS CUALQUIER OTRA COSA SIN COMMITEAR, PARAS Y LA TRAES: no
deberia haber nada, y si la hay es que algo paso entre mi acta y tu
apertura.

Esta es la VUELTA 130. LA 129 NO ENTREGO, Y ES LA CUARTA DE LA CAMPANA
(81, 114, 127, 129). PERO NO FUE COMO LA 127 Y ESTO IMPORTA QUE LO SEPAS:
NO HUBO NI UN ROJO. La 129 abrio bien (bloque de apertura en UN solo
commit, hijo directo de mi acta, `verificar_apertura_sellada.py --vuelta
129` VERDE a la primera y sin rebase), corrio las nueve guardas de su
TAREA 1 enteras y verdes, escribio LAS DOS PIEZAS DE CODIGO QUE LE
ENCARGUE, y se apago a las 02:58:29 con todo eso colgando del arbol sin
commitear. Doce minutos de corrida, un solo commit, seis minutos y medio
de trabajo bueno huerfano.

LO VERIFIQUE PIEZA POR PIEZA CON MIS COMANDOS Y ESTA TODO BIEN HECHO, ASI
QUE LO RESCATE YO EN COMMIT PROPIO (acta 129, secciones 3.2 y 3.3). NO LO
REHAGAS. Lo que ya esta en la rama y verde, medido hoy por mi:

  - `scripts/loop/verificar_cierre_sellado.py`, la guarda nueva del sello
    de cierre (era la 1.h de la 129). La corri en CUATRO estados: `--vuelta
    129` ROJO por fichero ausente, `--vuelta 128` VERDE sellando
    `e9413240`, y sus dos casos positivos sinteticos ROJOS por sus dos
    motivos. Y LE ANADI UNA PRUEBA QUE NO PEDI Y QUE VALE MAS: `9c222986`,
    el commit que el rebase de la 128 saco de la rama, SIGUE VIVO en la
    base de objetos, asi que lo puse como sello de cierre en fichero
    temporal y la guarda dio ROJO nombrando "no esta en la rama
    pasada-unica". CAZA EL CASO HISTORICO EXACTO PARA EL QUE NACIO.
  - `scripts/loop/vuelta129_tarea1h_casos_positivos.py`, sus dos casos por
    mutacion sobre repo temporal.
  - EL ENSANCHE DE `scripts/loop/verificar_citas_del_reporte.py` (era la
    1.i): todo fichero citado tiene que traer medicion ademas de su linea
    de codigo de salida, con la excepcion declarada de los `_TSC_`. Lo
    corri sobre el `REPORTE.md` de la 128 y da ROJO nombrando
    `SALIDA_V128_REBASE_ARBOL_IDENTICO.txt`, que es su caso positivo real,
    y las DOS mutaciones viejas de citas (122 y 123) SIGUEN dando ROJO.
  - Las DIECISEIS salidas `SALIDA_V129_1E/1F/1G/1H/1I_*` y
    `SALIDA_V129_APERTURA_SELLADA.txt`.

Y COMO ESAS DOS PIEZAS YA EXISTEN, LA TAREA 1 DE ESTA VUELTA NO TIENE
TRABAJO DE CODIGO NUEVO: son instrumentos que se corren, no que se
escriben. Tu vuelta empieza de verdad en la TAREA 3.

LO QUE COBRA LA 129, Y LO DIGO CORTO PORQUE NO HAY REPORTE QUE JUZGAR:

  UNA VUELTA NO ENTREGADA (acta 129, 4.1). No cuenta en ninguna racha por
  la letra del acta 82: las rachas estan escritas sobre caidas de clase,
  de cifra publicada y de reporte, y sin reporte no hay afirmacion. Y NO
  son dos seguidas: la 128 entrego entera y verde.

  UNA CAIDA DE INCUMPLIMIENTO DE ENCARGO (acta 129, 4.2). Mi encargo de la
  129 decia literal "en cuanto la guarda nueva de 1.h este escrita y
  verde, commit y push". Lo medi con los mtimes: la 1.h quedo verde a las
  02:56:58 y no se commiteo, ni ella ni las once salidas anteriores. La
  orden tenia disparador y hora, y no se cumplio.

  UNA CAIDA DE EXPEDIENTE (acta 129, 4.3), y se corrige abajo en la 2.d.
  La cabecera de `verificar_cierre_sellado.py` dice que su caso positivo
  (a) "usa `74d55f9e` (commit real de la rama `main`)". EL REGISTRO PEGADO
  AL LADO USA OTRA COSA: `SALIDA_V129_1H_CIERRE_SELLADO_MUTACION.txt` dice
  `ce51aa27`, un commit sintetico de un repo temporal que NO EXISTE en
  este repositorio (`git cat-file -t ce51aa27` da "Not a valid object
  name"). Verifique la afirmacion aparte y ES CIERTA (`74d55f9e` existe,
  es de `main`, y `merge-base --is-ancestor` contra `pasada-unica` da exit
  1), pero el expediente esta describiendo una prueba que no se corrio
  asi. Ramal (ii) al pie de la letra.

  Y UNA CAIDA MIA, DE ENCARGO, QUE ES LA QUE EXPLICA LAS DOS VUELTAS
  PERDIDAS (acta 129, 4.4). En la 128 y en la 129 puse la orden de
  commitear por tramo AL FINAL DEL ENCARGO, en un parrafo suelto detras de
  las tareas. Las dos veces se batcheo: la 128 commiteo catorce veces y
  pusheo una sola, la 129 commiteo una sola vez. UNA ORDEN QUE VIVE AL
  FINAL DEL ENCARGO SE EJECUTA AL FINAL O NO SE EJECUTA. Es mia y la
  reparo en la forma: desde esta vuelta CADA TAREA NUMERADA CIERRA CON SU
  PROPIA LINEA DE COMMIT Y PUSH, dentro de la tarea, como su ultimo paso.
  No hay parrafo de commit al final de este encargo, a proposito.

EL CHOQUE QUE ADJUDIQUE HOY Y QUE TE HABRIA MORDIDO (acta 129, 3.2), para
que sepas por que el arbol te llega limpio: la primera linea fija de todo
encargo dice "commitea lo pendiente antes de tocar nada", y
`verificar_apertura_sellada.py` exige que los once `*_APERTURA.txt` nazcan
en el commit HIJO DIRECTO del commit del acta. Si TU commiteabas las
dieciocho huerfanas de la 129, ese commit se metia entre mi acta y tu bloque de
apertura Y LA GUARDA SE TE PONIA ROJA SIN QUE HUBIERAS HECHO NADA MAL. Se
resuelve por ORDEN y sin tocar la guarda (ramal (iii): ninguna guarda se
estrecha en silencio): EL TRABAJO HUERFANO DE LA VUELTA N LO COMMITEA EL
AUDITOR, EN COMMIT PROPIO, ANTES DEL COMMIT DE SU ACTA. Ya esta hecho.

EL TRAMO QUE SE RELEE AL DOBLE ESTA VUELTA (acta 129 seccion 5), por
DECIMA vez, y sigue vivo porque la 129 no leyo nada. Siguen los ramales
(i) NINGUNA MEDICION SE ATRIBUYE A UN ESTADO QUE NO ES EL SUYO, (ii) EL
EXPEDIENTE NO PUEDE DECIR MAS QUE EL REGISTRO ESCRITO A SU LADO, (iii)
NINGUNA GUARDA SE ESTRECHA EN SILENCIO, (iv) TODA CIFRA SOBRE UN ARTEFACTO
CONTABLE SE LEE DE LA SALIDA DEL INSTRUMENTO PEGADA AL LADO, el (v) de la
123 NINGUNA VARA SE ESTRECHA EN EL ENCARGO, el (vi) de la 124 UN
SUPERVIVIENTE SE RAZONA COMO SE RAZONA UNA CLASE, el (vii) de la 125 UNA
FUSION NO ACABA CUANDO EL ALIAS QUEDA ESCRITO SINO CUANDO LA ULTIMA ARISTA
DEL ABSORBIDO ESTA RECONSTRUIDA, el (viii) de la 126 UNA CIFRA DE PASIVO
SE PARTE SIEMPRE EN DOS ANTES DE REMITIRLA, el (ix) de la 126 TODA CIFRA
DE PASIVO O DE CENSO SE PUBLICA CON SU UNIDAD Y SU ESTADO PEGADOS, el (x)
de la 127 UN ORDEN DE MEDICION SE PRUEBA CORRIENDOLO ENTERO SOBRE ARBOL
LIMPIO ANTES DE MANDARLO, y el (xi) de la 128 UNA NOMINA DE IDS SE
RESUELVE ANTES DE DECLARARLA COMPLETA. Le anado UNO, y sale de mi propia
caida:
  (xii) UNA ORDEN QUE VIVE AL FINAL DEL ENCARGO NO ES UNA ORDEN DE TRAMO.
  El commit y el push van escritos DENTRO de cada tarea, como su ultimo
  paso numerado, o el tramo entero se pierde el dia que la sesion se acaba
  antes que la lista. Dos vueltas de esta campana (127 y 129) murieron con
  el trabajo hecho y sin commitear, y las dos veces la orden estaba
  escrita: estaba escrita en el sitio equivocado.

LA ESCALADA de AUDITOR.md 1.2 se dispara con la racha de reporte en DOS.
Estamos en CERO. NO TOCA, y la dejo dicha entera para que nadie la de por
gastada.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2 trabajo;
la casa viene escribiendo TAREA 1 guardas, TAREA 2 registros, TAREA 3
trabajo, y lo mantengo porque las guardas son bloqueantes y van delante.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES
  DE TOCAR NADA MAS. ESTA VUELTA NO TIENE CODIGO NUEVO EN ESTA TAREA:
  TODOS SUS INSTRUMENTOS EXISTEN Y ESTAN VERDES.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V130_HEAD_APERTURA.txt. Al terminar la ultima operacion
  y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V130_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 130 tiene que
  dar VERDE EXIT 0, y su salida se cita en el reporte. La linea de
  identidad del reporte mantiene los TRES rotulos de la 126 y la 128:
  "HEAD sellado de apertura", "commit de nacimiento de las salidas de
  apertura" y "HEAD sellado de cierre".
  EL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) VA EN UN SOLO COMMIT Y NO SE
  PUSHEA SOLO (regla compuesta del acta 128, seccion 3.4). El push por
  tramo empieza DESPUES de ese bloque, con el primer commit de operacion.
  Esa es la UNICA excepcion a la linea de commit y push de cada tarea.
  (1.b) EL ORDEN DE CAPTURA, EL DE LA 128 Y LA 129, QUE FUNCIONO Y NO SE
  TOCA. REGLA UNICA: `python scripts/run_phase1.py --reaplico-curaduria`
  NO SE CORRE NUNCA SUELTO COMO MEDICION. Su Gate 0 compara el snapshot de
  ANTES del paso 6 y por eso sale verde sobre un estado que el mismo acaba
  de desalinear; el motor si lo ve.
  POR CADA LADO (APERTURA, CIERRE, y el POST de cada operacion) SE HACE
  ESTO Y EN ESTE ORDEN, UNA SOLA VEZ:
    1) `python scripts/run_phase1.py --reaplico-curaduria`, ENTERA, y su
       salida ES la salida de Gate 0 de ese lado, escrita directamente en
       docs/loop/SALIDA_V130_GATE0_CMD1_<LADO>.txt. NO hay fichero
       CICLO_RUN_PHASE1 aparte: es la MISMA corrida y la MISMA salida.
    2) `python scripts/etiquetas_de_cara.py --aplicar` ->
       docs/loop/SALIDA_V130_CICLO_ETIQUETAS_<LADO>.txt
    3) `python scripts/sync_assets_web.py` ->
       docs/loop/SALIDA_V130_CICLO_SYNC_<LADO>.txt
    4) EL CIERRE DEL CICLO, PEGADO: `git diff --numstat -- dataset/ web/
       engine/` VACIO (o, si la operacion de ese lado escribio de verdad,
       SOLO los ficheros que esa operacion escribio;
       `dataset/metadata/master_graph.json` con diff de puras lineas
       `etiqueta_arbol` NUNCA es escritura legitima, es el borrado).
       Salida a docs/loop/SALIDA_V130_CICLO_NUMSTAT_<LADO>.txt con su
       EXITCODE.
    5) SOLO ENTONCES se capturan las demas salidas del lado.
  Si el numstat no cierra, NO MIDAS: repite el ciclo, dilo en el reporte,
  y si a la segunda tampoco cierra PARAS y lo traes escrito.
  (1.c) LOS NOMBRES CANONICOS DE LAS SALIDAS DE APERTURA Y DE CIERRE, con
  <LADO> = APERTURA o CIERRE, exactamente estos siete:
    docs/loop/SALIDA_V130_GATE0_CMD1_<LADO>.txt   (la corrida 1 del ciclo de 1.b, entera)
    docs/loop/SALIDA_V130_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V130_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V130_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V130_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V130_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V130_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  mas las tres del ciclo de 1.b (ETIQUETAS, SYNC, NUMSTAT) por lado.
  El formato del tsc es EXIT=<n> sin dos puntos y sin espacio, sigue
  prohibido el fichero de cero bytes, y el marcador de codigo de salida de
  las demas salidas es la linea literal EXITCODE: <n>. Y EL EXITCODE SE LEE
  DEL INSTRUMENTO, NUNCA DE UN `$?` PUESTO DETRAS DE UNA TUBERIA.
  >>> COMMIT DEL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) EN UN SOLO
  >>> COMMIT, SIN PUSH. Es el unico commit de la vuelta que no se pushea
  >>> en el acto.
  (1.d) LA BATERIA POR OPERACION. Se escribe la operacion N, se corre su
  ciclo de 1.b entero, se miden sus cuatro salidas, Y SOLO ENTONCES empieza
  la N+1. Esta vuelta hay UNA sola operacion de REGIMEN B, con <OP> =
  OPS10REP1 (el nodo que le falta a OP-S-10):
    docs/loop/SALIDA_V130_<OP>_GATE0_POST.txt   (= la corrida 1 del ciclo de esa operacion)
    docs/loop/SALIDA_V130_<OP>_CONTEO_POST.txt
    docs/loop/SALIDA_V130_<OP>_MOTOR_POST.txt
    docs/loop/SALIDA_V130_<OP>_WEB_POST.txt
    docs/loop/SALIDA_V130_<OP>_TSC_POST.txt
  mas las de etiquetas, sync y numstat del ciclo con el mismo prefijo.
  Antes de escribir el reporte corres cmp -s sobre CADA par de salidas
  homologas y vuelcas el resultado literal a
  docs/loop/SALIDA_V130_BATERIAS_CMP.txt, una linea por par, IDENTICOS o
  DISTINTOS, mas la linea RESUMEN por familia como en la 128.
  Y LA LETRA DE LA 129, QUE SIGUE VIGENTE PORQUE NADIE LA GASTO: EL REPORTE
  DA CUENTA DE CADA FAMILIA CON EL PAR NOMBRADO. No basta con decir "N
  identicos y M distintos": SI UNA FAMILIA TIENE UN SOLO IDENTICO O UN SOLO
  DISTINTO, SE NOMBRA ESE PAR EXACTO, LEIDO DEL FICHERO, Y SE EXPLICA POR
  QUE ESE Y NO OTRO. Un par nombrado de memoria en vez de leido es la caida
  4.1 de la 128 repetida. EL CONTEO TIENE QUE SUBIR CERO ARISTAS: esta
  vuelta no mueve ninguna, y si mueve alguna ES ROJO y paras.
  (1.e) LAS GUARDAS DE CITAS Y DE TITULOS SE CORREN Y NO SE TOCAN:
  verificar_citas_del_reporte.py (YA ENSANCHADA, no la vuelvas a tocar),
  verificar_titulos_normalizados.py y sus autopruebas
  (vuelta122_tarea1e_mutacion_citas.py,
  vuelta123_tarea1e_mutacion_fila_tabla.py, y
  verificar_titulos_normalizados.py --autoprueba), y se pegan. Las dos
  mutaciones viejas TIENEN que seguir dando ROJO con el ensanche puesto: lo
  verifique yo hoy y dan ROJO, asi que si a ti te salen verdes hay algo
  distinto en tu arbol y PARAS. La excepcion declarada de
  sistema_responsabilidad_gerencial se queda EXACTAMENTE como esta.
  (1.f) LA GUARDA DE CIFRAS DEL PLAN, TAMPOCO SE TOCA. Se corre
  verificar_cifras_del_plan.py y sus dos casos positivos
  (vuelta123_tarea1f_caso_positivo.py y
  vuelta124_tarea1f_caso_positivo_ventana.py), pegados.
  (1.g) LAS TRES GUARDAS DE ARISTAS SE CORREN Y NO SE TOCAN:
  verificar_fusion_ops09.py con su --autoprueba, verificar_aristas_vivas.py
  con su --autoprueba, y verificar_huerfanas_por_fusion.py con su caso
  positivo por mutacion. Tras la operacion de 3.a,
  verificar_aristas_vivas.py --antes <HEAD sellado de apertura> --despues
  WORK tiene que dar PERDIDAS 0 y NUEVAS 0 (un reencuadre de texto no mueve
  aristas), y verificar_huerfanas_por_fusion.py tiene que seguir en TOTAL
  29 / FABRICADAS 0. MI CONTRASTE, MEDIDO HOY: aristas vivas entre
  a77f67f7 y WORK da 7.296 contra 7.296, PERDIDAS 0 NUEVAS 0; huerfanas da
  TOTAL 29 HEREDADAS 29 REPARADAS 1 FABRICADAS 0.
  (1.h) LA GUARDA DEL SELLO DE CIERRE SE CORRE, NO SE ESCRIBE: YA EXISTE.
  `python scripts/loop/verificar_cierre_sellado.py --vuelta 130` tiene que
  dar VERDE EXIT 0 una vez escrito tu SALIDA_V130_HEAD_CIERRE.txt, y su
  salida se pega. Corre tambien
  `python scripts/loop/vuelta129_tarea1h_casos_positivos.py` y pega su
  VERDE GENERAL: los casos por mutacion se re-corren cada vuelta, como los
  demas. NO renombres ese script por llevar 129 en el nombre: es el caso
  positivo de una guarda estable y su nombre dice de que vuelta nacio.
  (1.i) LA GUARDA DE CITAS YA ESTA ENSANCHADA Y SU CASO POSITIVO YA ESTA
  CORRIDO. Lo unico que queda de la 1.i de la 129 es que la corras sobre TU
  reporte de la 130 y de VERDE. Si te da ROJO nombrando un fichero tuyo,
  ESO ES LA GUARDA HACIENDO SU TRABAJO: arreglas el fichero pegandole la
  medicion que le falta, no la cita del reporte.
  (1.j) ANTES DEL COMMIT DEL REPORTE, LAS CINCO COMPROBACIONES, y las cinco
  salidas se pegan CITADAS POR SU PROPIO NOMBRE DE FICHERO:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 130 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
    python scripts/loop/verificar_cierre_sellado.py --vuelta 130
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR y las otras cuatro
  VERDE EXIT 0.
  (1.k) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE. wc -l docs/loop/REPORTE.md
  tiene que dar 80 o menos y esa cifra se escribe en el propio reporte,
  medida, con su salida.
  (1.l) LOS DOS REGIMENES DE ESCRITURA SIGUEN COMO ESTAN Y NO SE TOCAN:
    - REGIMEN A, TEXTO: un instrumento que solo anade TEXTO a docs/plan/ o
      a docs/ se mide con git diff --numstat y con grep -c "^-[^-]" sobre
      el diff en cero, mas git diff --word-diff=porcelain pegado si toca
      una linea vieja. NO necesita las tres guardas.
    - REGIMEN B, DATO: un instrumento que escribe en dataset/, o que
      EJECUTA una operacion, lleva LAS TRES GUARDAS COMPLETAS: (i)
      SIMULACION PREVIA sobre copia en memoria con su salida pegada, (ii)
      SU MUTACION NEGATIVA corrida y pegada, y (iii) SU ROJO REAL EN
      SEGUNDA PASADA, con git status --porcelain PEGADO DETRAS TAL CUAL
      SALGA. Un instrumento de REGIMEN B sin las tres NO SE CORRE.
    - EL REPORTE DICE, POR CADA INSTRUMENTO QUE ESCRIBIO, BAJO QUE REGIMEN
      FUE. Un instrumento sin regimen declarado no existe para el
      expediente.
  >>> COMMIT Y PUSH de 1.d a 1.l en cuanto las guardas de 1.e, 1.f, 1.g y
  >>> 1.h esten corridas y pegadas. NO ESPERES A 3.a. Esto es exactamente
  >>> lo que la 129 no hizo y por eso perdio la vuelta.

- TAREA 2, LOS REGISTROS Y CORRECCIONES. REGIMEN A. Aditivos puros,
  medidos con git diff --numstat y con grep -c "^-[^-]" sobre el diff en
  cero. Son CUATRO, y 2.a se escribe DESPUES de que 3.a este verde porque
  cita su resultado medido.
  (2.a) EL REGISTRO LARGO EN docs/PENDIENTES.md, seccion nueva R.11 de la
  vuelta 128, como correcciones declaradas, con estas seis cosas: (1) la
  caida de reporte del parrafo de baterias de la 128, con las DOS lineas
  del fichero cmp que la desmienten pegadas literales y la razon correcta
  del identico (los dos lados sellados sobre arbol limpio), y que NO
  acumula por la letra del fundador del 27 ago; (2) la caida de expediente
  del fichero de rebase con una sola linea, con el hash viejo 9c222986
  ESCRITO AHI para que deje de vivir solo en un reflog, y la constancia de
  que el auditor verifico el arbol identico y el "sin nada pusheado" con
  sus comandos; (3) la caida de procedimiento del push unico al final, con
  la REGLA COMPUESTA adjudicada (acta 128, 3.4) escrita entera; (4) LAS DOS
  GUARDAS QUE NO ALCANZAN, con lo que se hizo con cada una (la nueva de
  cierre y el ensanche de la de citas) Y CON LA CONSTANCIA DE QUE LAS DOS
  QUEDARON ESCRITAS Y VERDES EN LA 129 Y RESCATADAS POR EL AUDITOR EN LA
  129; (5) LA CAIDA DEL AUDITOR, DE ENCARGO, escrita con todas sus letras:
  pedi medir "los 31" sin mandar resolver la nomina por P.1, y por eso la
  lectura corta llego al reporte; y (6) el ramal (xi) del tramo que se
  relee al doble, escrito entero.
  (2.b) LA CORRECCION DECLARADA EN LA NOTA DE OP-S-10, en
  docs/plan/05_SANEO.md, aditiva y sin borrar nada, con LA MEDICION QUE TU
  HAGAS (no la mia) de la verificacion 1 resuelta por P.1: cuantos ids
  historicos, a cuantos vivos resuelven, cuales son los tres deprecados y a
  que superviviente va cada uno, y cual de esos supervivientes NO estaba
  cubierto. Cita P.1 por su linea (docs/plan/BANCO_DEL_PLAN.md:11) y la
  frase de la propia nota que ya la invocaba. Y di, con esa cifra delante,
  que la verificacion 1 pasa a VERDE tras 3.a, o que no pasa y por que.
  (2.c) LA FICHA `aristas-huerfanas-por-fusion` de docs/PENDIENTES.md
  recibe UNA linea aditiva mas: que el auditor remidio las cifras
  (par-resuelto WORK 29/29/1/0 en la vuelta 128 y otra vez en la 129,
  par-resuelto en 9ef3705d 32/29, par-crudo en 7150339f 39) y que cuadran
  al digito. Es constancia de contraste, no correccion: nada se retracta.
  (2.d) LA CORRECCION DE LA CABECERA DE `verificar_cierre_sellado.py`,
  REGIMEN A, Y ES LA CAIDA 4.3 DE LA 129. La cabecera dice que el caso
  positivo (a) usa `74d55f9e`; el registro pegado usa `ce51aa27`, sintetico
  y ajeno a este repositorio. ANADE (no reescribas, no borres) un parrafo
  al final del docstring que diga QUE SE CORRIO DE VERDAD: repo temporal
  construido con `git init`, rama lateral divergente del commit del acta
  sintetica, y el hash del lateral cambia en cada corrida por diseno.
  Deja tambien escrito que `74d55f9e` SI es un commit real de `main` ajeno
  a `pasada-unica` (yo lo verifique hoy: `git cat-file -t` da commit,
  `merge-base --is-ancestor 74d55f9e pasada-unica` da exit 1), y que
  NO SE USO. El codigo no se toca: solo el docstring, y solo anadiendo.
  >>> COMMIT Y PUSH de 2.b, 2.c y 2.d en cuanto esten escritas. 2.a va
  >>> despues de 3.a, con su propio commit y push.

- TAREA 3, EL TRABAJO. SON DOS, Y LA SEGUNDA ES LA GRANDE.
  (3.a) EL NODO QUE LE FALTA A OP-S-10. REGIMEN B, LAS TRES GUARDAS
  COMPLETAS (1.l). BLOQUEANTE Y VA PRIMERA.
  ANTES DE ESCRIBIR NADA, MIDELO TU con codigo propio: resuelve los 31 ids
  del campo `nodos` de OP-S-10 por `ids_alias` de `dataset/nodos/`, quedate
  con los vivos distintos, y mira cuales NO nombran el pais en
  `condiciones_activacion`.
  MI CONTRASTE, MEDIDO HOY POR MI Y NO PARA COPIAR (acta 129, 3.5;
  resolutor de 746 alias): 31 ids resuelven a 29 vivos, cero deprecados y
  cero ausentes TRAS resolver; el resolutor mueve tres
  (cinco_categorias_costos_franquicia a
  estimacion_inversion_inicial_franquiciador, elaboracion_fdd a
  preparar_fdd, estructuras_combinadas_franquicia a
  prevenir_franquicias_inadvertidas); 28 de 29 cubiertos; el unico sin
  cubrir es `prevenir_franquicias_inadvertidas`, con sus cuatro condiciones
  de activacion y ninguna nombrando el pais. SI TU MEDICION TE DA OTRA
  COSA, MANDA LA TUYA Y DECLARAS LA DISCREPANCIA, no la resuelves copiando.
  Sobre el que te salga, antepone la MISMA FORMA LITERAL de siempre, "Solo
  aplica si vendes o piensas vender franquicias en Estados Unidos", como
  PRIMERA condicion de activacion, con las viejas enteras y en su orden.
  Guardas propias ademas de las tres: ningun otro campo cambia, cero
  aristas movidas (verificar_aristas_vivas.py en PERDIDAS 0 y NUEVAS 0),
  cero guiones largos y cero guiones medios. Detras, su bateria de 1.d
  entera con etiqueta OPS10REP1.
  ANTES DE ESCRIBIRLO, LEELO ENTERO y comprueba que el contenido sostiene
  la condicion, como se comprobo en la 126 y en la 128. SI AL LEERLO
  CONCLUYES QUE NO LA SOSTIENE, NO LO ESCRIBAS: paras en ese, lo traes con
  su caso escrito, y sigues con la TAREA 3.b.
  Y DESPUES, MIDE LA VERIFICACION 1 OTRA VEZ Y PUBLICA LA CIFRA RESUELTA.
  Si te sale entera, DILO Y MARCALO COMO DISCUTIBLE: el cierre de OP-S-10
  lo adjudico yo en el acta 130, no tu. NO LE CAMBIES EL ESTADO EN
  OPERACIONES.jsonl.
  >>> COMMIT Y PUSH en cuanto 3.a este verde con su bateria. Y detras, 2.a
  >>> con su propio commit y push.
  (3.b) LA PRIMERA MITAD DE OP-S-11, LA QUE NO DECIDE NADA. REGIMEN A
  ESTRICTO: NO SE TOCA UN SOLO NODO NI UN SOLO FICHERO DE dataset/ EN ESTA
  TAREA. Si te descubres editando dataset/, es que te saliste.
  EL PORQUE, RE-VERIFICADO POR MI HOY (acta 129, 3.7): la verificacion 1 de
  OP-S-11 pide que el campo `fuente` "resuelva contra una lista CANONICA de
  libros", y la adjudicacion de la operacion dice que la tabla de mapeo "va
  DENTRO de ella". NO ESTA. Mi `grep -rln` sobre docs/ por "grafia" da
  veinte ficheros y ninguno trae la correspondencia; RECORTE_POSICIONAL.md
  trae el total 55 en su tabla y nada mas. VERIFICALO TU ANTES DE NADA, y
  si la encuentras donde yo no mire, DILO Y USALA: manda tu medicion.
  Y AHORA LO QUE ES EL NUDO DE ESTA TAREA, Y LO MEDI YO HOY PARA QUE NO TE
  LO ENCUENTRES A MITAD (acta 129, 3.6): EL NUMERO DE GRAFIAS DEPENDE DEL
  SEPARADOR Y SE MUEVE EN SIETE. Con `;` solo salen 135 grafias distintas
  en primera posicion; con `;` y `|` salen 128. Ninguno de los dos es el
  129 del 11 ago 2026. Y el separador NO es opinable: los datos traen `;`
  en 264 nodos y ` | ` en 8, y las cadenas del `|` separan libros distintos
  de verdad (`The Startup Owner's Manual - Steve Blank | Traction - Gabriel
  Weinberg`). ASI QUE "DI COMO LOS SEPARAS Y POR QUE" NO ES FORMALIDAD: ES
  LA DECISION QUE MANDA SOBRE LA CIFRA, Y VA ARGUMENTADA CON LOS DATOS
  DELANTE, NO ELEGIDA.
  LO QUE SE HACE, y es medir y proponer, no decidir:
    (i) Escribe scripts/loop/vuelta130_censo_fuente.py, que sobre los nodos
    VIVOS de hoy extraiga el campo `fuente`, separe las declaraciones (di
    en el propio script COMO las separas y por que ese separador, leido de
    los datos y no supuesto, y PEGA EL RECUENTO DE CADA SEPARADOR
    CANDIDATO que te llevo a elegirlo), y saque el censo de GRAFIAS
    DISTINTAS EN PRIMERA POSICION con su recuento. Salida a
    docs/loop/SALIDA_V130_3B_CENSO_FUENTE.txt. PUBLICA LA CIFRA QUE TE
    SALGA, sea 128, 135 o ninguna de las dos, CON EL SEPARADOR QUE USASTE
    PEGADO A LA CIFRA. La de 129 es del 11 ago 2026 y el catalogo se ha
    movido desde entonces: si difiere NO ES UN ERROR, ES EL CORTE NUEVO, y
    se declara como tal con los dos cortes y las dos unidades escritos.
    (ii) Sobre ese censo, agrupa MECANICAMENTE y solo lo mecanico: las
    grafias TRUNCADAS (una es prefijo estricto de otra, que es el patron
    que la operacion documenta) y las que solo difieren en espacios,
    mayusculas o puntuacion final. Cada grupo con su candidata a canonica
    (la mas larga del grupo) y el recuento de cada miembro. Salida a
    docs/loop/SALIDA_V130_3B_GRUPOS_MECANICOS.txt. AVISO MEDIDO POR MI: con
    `;` solo, el prefijo estricto me dio 32 pares, y VARIOS DE ELLOS NO SON
    LA MISMA OBRA sino una obra y una cadena de dos obras unidas por `|`
    (`Venture Deals` contra `Venture Deals - Brad Feld | The Founder's
    Dilemmas`). SI TU SEPARADOR NO INCLUYE EL `|`, ESOS PARES TE VAN A
    ENSUCIAR EL AGRUPAMIENTO: dilo y trata la cadena como lo que es.
    (iii) LO QUE NO AGRUPE MECANICAMENTE SE LISTA APARTE Y NO SE TOCA:
    docs/loop/SALIDA_V130_3B_SIN_AGRUPAR.txt, una linea por grafia con su
    recuento. Esas son las que piden decision, y la decision es mia.
    (iv) Escribe la TABLA PROPUESTA en un fichero NUEVO,
    docs/plan/OP_S_11_MAPEO_PROPUESTO.md, aditivo puro (fichero nuevo, no
    toca ninguno viejo), con tres columnas: grafia, canonica propuesta,
    motivo (mecanico y cual, o SIN AGRUPAR). Y en su cabecera, con estas
    palabras: que es una PROPUESTA MEDIDA, que NO se ha aplicado a ningun
    nodo, que el separador elegido es tal y por que, y que la adjudica el
    auditor. NO cambies el estado de OP-S-11.
    (v) LOS DOS CASOS PROBADOS DE LA OPERACION, REMEDIDOS Y CON SU UNIDAD
    DELANTE, QUE ES DONDE ESTA LA TRAMPA. La nota de la operacion dice
    Hugos "23 contra 21" y Horowitz "16 contra 14", Y ESAS CIFRAS SON DEL
    RECORTE POSICIONAL (67 nodos), no del catalogo entero. Mi medicion de
    hoy sobre el CATALOGO ENTERO da Hugos 2 grafias / 95 declaraciones y
    Horowitz 3 grafias / 71. SON UNIDADES DISTINTAS Y NO SE COMPARAN. Mide
    LAS DOS unidades tu, cada una con su nombre y su corte, y di cual es
    cual. Casi publico yo la comparacion mala y la cace a tiempo: es el
    ramal (ix) mordiendo al que lo escribio.
  Y SI AL MEDIR CONCLUYES QUE NI SIQUIERA PROPONER LA TABLA SE PUEDE SIN
  DECIDIR, PARAS EN 3.b, LO TRAES ESCRITO CON SU CASO, Y ENTREGAS LA VUELTA
  CON 3.a HECHA. Eso no es fracasar: es la letra de AUDITOR.md seccion 3, y
  para eso esta escrita.
  >>> COMMIT Y PUSH DETRAS DE CADA UNA DE LAS CINCO SALIDAS DE 3.b, no al
  >>> final de la tarea. Cinco commits, cinco pushes.
  (3.c) LO QUE NO SE TOCA ESTA VUELTA, DICHO PARA QUE NO HAYA DUDA:
  OP-S-12 NO SE ABRE. Va al final de la pasada entera, no al final de su
  fase, por la atadura 2 de docs/plan/00_INDICE.md ("OP-S-12 va AL FINAL,
  despues de la ultima fusion, porque cada fusion fabrica sus duplicadas").
  Y LA FASE 05 NO SE DECLARA CERRADA POR NADIE ESTA VUELTA: cuando quede
  cerrada y verificada se dispara la condicion de parada CIERRE DE LA FASE
  05 de AUDITOR.md seccion 4, que es del fundador, y esa la disparo yo en
  mi acta, no tu en tu reporte. MARCALO COMO DISCUTIBLE si con 3.a y 3.b
  hechas la fase queda a una sola operacion con trabajo (OP-S-11) mas
  OP-S-12 remitida al final, para que yo adjudique si cierra CON REMISION
  como cerraron la fase 03 y la fase 04.
  TAMPOCO SE TOCA la fase 00_CODIGO. `OP-C-01` a `OP-C-05`, `OP-S-06` y
  `OP-S-07` figuran LISTA en OPERACIONES.jsonl y ESO NO ES UN HALLAZGO: el
  acta 25 declaro la fase 0 cerrada y el acta 119 adjudico que cumple su
  criterio con OP-C-01 a OP-C-04 en verde y OP-C-05 DIFERIDA POR SU PROPIA
  FICHA. Lo consulte hoy. Si tropiezas con esos estados, no abras nada: ya
  esta adjudicado.
  >>> El commit y push del REPORTE va al final, despues de las cinco
  >>> comprobaciones de 1.j y de la medida de 1.k, y despues del sello de
  >>> cierre de 1.a. Ese es el ultimo commit de la vuelta.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
