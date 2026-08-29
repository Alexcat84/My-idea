Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

Esta es la VUELTA 123. El acta de la 122 esta escrita
(docs/loop/ACTA_AUDITOR.md, al final). Lo que dice, en corto: el trabajo
material de la 122 vuelve a ser bueno y lo ratifique al digito con mis
propios instrumentos. Los VEINTE accesos externos los lei yo sitio por
sitio y OP-S-08 cierra bien; el censo de alias (742 entradas, 0
colisiones, 719 a vivo, 23 a deprecado, 0 huerfanas en la fuente
canonica; 230/15/37 en los cuatro alias_map) me sale identico al tuyo;
la nomina de OP-S-09 sale INTACTA (67 de 67 vivos) y NEGARSE A
EJECUTARLA A CIEGAS FUE LO CORRECTO. El tallador vuelve a VERDE y la
segunda vuelta en rojo que la 121 dejo amenazada no ocurre. Adjudique
los tres discutibles sin doctrina nueva. No hay parada: ninguna de las
diez condiciones se dispara.

Lo que la vuelta cobro son cinco caidas fuera de los discutibles
marcados, y UNA DE ELLAS ES MIA. Estan en el acta 122 como 4.1 a 4.6 y
todas se corrigen abajo. La que importa por encima de las otras:

  LA RACHA DE CIFRA PUBLICADA SUBE DE CERO A UNO (acta 122, 4.1: el
  punto 0 de verificacion de OP-S-08 escribe "32 casos" de
  accesosResueltos.test.ts y la suite tiene VEINTISIETE; lo medi con
  vitest, con it(, con test( y comprobando que el fichero no se toco en
  la vuelta). LA PARADA DE ESA CLASE SE DISPARA CON DOS TANDAS SEGUIDAS.
  SI ESTA VUELTA TRAE OTRA CIFRA FALSA QUE VIVA EN docs/plan/ O EN EL
  BANCO, ES PARADA. Por eso la TAREA 1.f es una guarda de codigo que la
  muerde, y no solo una correccion de texto.

EL TRAMO QUE SE RELEE AL DOBLE ESTA VUELTA (acta 122 seccion 5). Sigue
vivo el de la 120 (TODA CALIFICACION TECNICA QUE EL REPORTE COMPRIMA
RESPECTO DE SU REGISTRO LARGO) con sus ramales (i) NINGUNA MEDICION SE
ATRIBUYE A UN ESTADO QUE NO ES EL SUYO y (ii) EL EXPEDIENTE NO PUEDE
DECIR MAS QUE EL REGISTRO ESCRITO A SU LADO, y le anado DOS:
  (iii) NINGUNA GUARDA SE ESTRECHA EN SILENCIO. Si al probar una guarda
  contra su propio material hay que recortarle el alcance, el recorte se
  escribe en TRES sitios o no existe: en el CONTRATO del docstring del
  script, en el REPORTE.md de la vuelta, y en un caso positivo que
  demuestre que lo excluido queda excluido a proposito. Un arreglo de
  guarda que solo vive en el mensaje de commit no existe para el
  expediente. (La 122 recorto verificar_citas_del_reporte.py para que
  pasara sobre su propio reporte y lo conto solo en el commit.)
  (iv) TODA CIFRA SOBRE UN ARTEFACTO CONTABLE (tests de una suite,
  lineas de un diff, miembros de una familia) SE LEE DE LA SALIDA DEL
  INSTRUMENTO PEGADA AL LADO. Si el instrumento ya escribio su fichero,
  la cifra del texto ES ESE FICHERO. La 122 publico "81 insertadas"
  mientras su propio SALIDA_V122_TAREA2_NUMSTAT.txt decia 55 y 25.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2
trabajo; la casa viene escribiendo desde hace vueltas TAREA 1 guardas,
TAREA 2 registros, TAREA 3 trabajo, y lo mantengo porque las guardas son
bloqueantes y tienen que ir delante. Lo digo para que no se lea como
deriva.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA
  ANTES DE TOCAR NADA MAS.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA
  OPERACION: git rev-parse HEAD, hash completo de 40 caracteres, UNA
  linea, a docs/loop/SALIDA_V123_HEAD_APERTURA.txt. Al terminar la
  ultima operacion y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V123_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 123 tiene
  que dar VERDE EXIT 0, y su salida se cita en el reporte. La 120, la
  121 y la 122 lo hicieron bien las tres; se repite igual.
  (1.b) LOS NOMBRES CANONICOS DE LAS SALIDAS DE APERTURA Y DE CIERRE,
  con <LADO> = APERTURA o CIERRE, exactamente estos siete:
    docs/loop/SALIDA_V123_GATE0_CMD1_<LADO>.txt   (scripts/run_phase1.py --reaplico-curaduria, entera)
    docs/loop/SALIDA_V123_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V123_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V123_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V123_TSC_<LADO>.txt          (cd web y npx tsc --noEmit)
    docs/loop/SALIDA_V123_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V123_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  (1.c) EL CICLO DE TRES, IGUAL QUE LA 122, QUE LO HIZO BIEN. NINGUNA
  salida de guarda se captura mientras el ciclo este a medias. El ciclo
  es run_phase1.py --reaplico-curaduria, luego etiquetas_de_cara.py
  --aplicar, luego sync_assets_web.py, EN ESE ORDEN, y solo cuando
  git diff --numstat sobre dataset/, web/ y engine/ este en CERO se
  empieza a medir. Por cada corrida del ciclo se escribe
  docs/loop/SALIDA_V123_CICLO_<ETIQUETA>_NUMSTAT.txt con la salida
  literal de git diff --numstat -- dataset/ web/ engine/ y una linea
  final "EXITCODE: N", con <ETIQUETA> = APERTURA, OPS09, CIERRE, la que
  toque. La 122 declaro en su reporte que rompio esta regla una vez y la
  corrigio en vivo antes de publicar nada: eso esta bien hecho y NO se
  le conto. Se sigue igual.
  (1.d) LA BATERIA POR OPERACION, EN SU PROPIO CHECKPOINT, Y UN ARREGLO
  QUE ES CULPA MIA, NO TUYA. Se escribe la operacion N, se corre su
  ciclo de tres entero, se miden sus cuatro salidas, Y SOLO ENTONCES
  empieza la N+1. Ficheros, con <OP> = OPS09, etc.:
    docs/loop/SALIDA_V123_<OP>_GATE0_POST.txt
    docs/loop/SALIDA_V123_<OP>_MOTOR_POST.txt
    docs/loop/SALIDA_V123_<OP>_WEB_POST.txt
    docs/loop/SALIDA_V123_<OP>_TSC_POST.txt
  mas las de etiquetas y sync del ciclo con el mismo prefijo. Si dos
  baterias salen identicas byte a byte, EL REPORTE LO DICE Y EXPLICA POR
  QUE (en la 122 los tres GATE0 salieron identicos y era determinismo
  legitimo: lo verifique yo diffeando mi propia corrida contra la suya,
  pero el reporte no lo nombraba).
  EL ARREGLO DEL tsc, Y ES CORRECCION DE MI ENCARGO DE LA 122 (acta 122,
  4.5): mi encargo mando terminar toda salida de tsc con una linea
  "EXITCODE: N". ESE FORMATO ES EL EQUIVOCADO. El tallador descuenta el
  marcador con la expresion ^EXIT=(\d+)$ (scripts/loop/
  tallar_cabecera_reporte.py, linea 596, contrato de la vuelta 113), y
  "EXITCODE: 0" no le casa, asi que la celda de tsc de la cabecera
  publica "1 linea(s) de salida (revisar)" en sus dos columnas con el
  tsc realmente limpio: la ceguera exacta que la 113 vino a arreglar.
  ESTA VUELTA: toda salida de tsc termina con la linea literal
  EXIT=<n>
  (sin dos puntos y sin espacio), y sigue prohibido el fichero de cero
  bytes. LA COMPROBACION ES LA CELDA: la cabecera tallada tiene que
  publicar "EXITCODE 0, cero lineas" en sus DOS columnas. Si publica
  "revisar", el arreglo no esta hecho.
  (1.e) EL ARREGLO DE verificar_citas_del_reporte.py, BLOQUEANTE Y ANTES
  DE LA TAREA 3 (acta 122, 4.6). La guarda nacio en la 122 contra el
  dictado y en el mismo commit del reporte se le anadio, en cotejar(),
  un "if frase.strip().startswith('|'): continue" que deja FUERA DEL
  COTEJO TODA FILA DE TABLA MARKDOWN. Lo probe por mutacion propia
  (docs/loop/SALIDA_V122_AUDITOR_PUNTO_CIEGO_CITAS.txt): la MISMA
  afirmacion falsa da ROJO EXIT 1 en prosa y VERDE EXIT 0 dentro de una
  fila de tabla, y esa fila tampoco la ve el tallador, que solo coteja
  sus diez filas. Los otros dos arreglos de ese commit (el punto de
  cierre de una frase que acaba en numero, y el enmascarado de los
  nombres de fichero que llevan ROJO dentro) SON BUENOS Y SE QUEDAN.
  Lo que hay que hacer, exacto:
    - Quitar el continue. Una fila de tabla vuelve a ser cotejable: si
      lleva una afirmacion del vocabulario Y una cita de fichero EN LA
      MISMA FILA, se coteja como cualquier frase.
    - Conservar el corte que ya hiciste (cada fila de tabla es su propia
      frase atomica): eso era el arreglo de verdad. Lo que cambia es que
      una fila SIN cita propia NO mira a la frase anterior (ahi estaba
      el cruce que te hizo recortar), simplemente no se coteja y no es
      rojo.
    - Actualizar el bloque CONTRATO del docstring para que diga el
      alcance REAL que corre, incluida esa regla del lookback.
    - Caso positivo, y es el mio: sobre una copia de docs/loop/REPORTE.md
      de la 122 con la fila de tabla
      | motor de la apertura | 25/25 (`SALIDA_V122_TSC_APERTURA.txt`) | **25/25** |
      anadida al final, la guarda tiene que dar ROJO EXIT 1 nombrando
      ese par. Pega la salida. Y vuelve a correr la mutacion que ya
      tenias (scripts/loop/vuelta122_tarea1e_mutacion_citas.py): tiene
      que seguir dando ROJO. Si el arreglo rompe la mutacion vieja, el
      arreglo esta mal.
  (1.f) UNA GUARDA DE CODIGO NUEVA, Y ES EL REMEDIO DE LA RACHA DE CIFRA
  PUBLICADA. BLOQUEANTE. NO ES LA ESCALADA de AUDITOR.md 1.2 (esa es de
  la racha de REPORTE, que hoy esta en CERO, y sigue intacta). Escribe
  scripts/loop/verificar_cifras_del_plan.py con este contrato exacto y
  nada mas:
    - Toma --base <ref> (por defecto, el commit del acta anterior) y
      compara docs/plan/OPERACIONES.jsonl entre --base y el arbol de
      trabajo.
    - Para cada fila cuyo id_op aparezca en las dos versiones y haya
      cambiado, calcula el TEXTO ANADIDO de cada campo de texto (la
      parte nueva que no estaba en la version base).
    - Sobre ESE texto anadido busca, con vocabulario CERRADO, pares
      (numero, artefacto): un numero seguido de "caso", "casos", "test",
      "tests", "prueba" o "pruebas", en la MISMA frase que una ruta
      citada que termine en ".test.ts".
    - Para cada par: corre npx vitest run <ruta sin el prefijo web/>
      desde web/ y lee la linea "Tests  N passed". Si N no es el numero
      escrito, ROJO EXIT 1 diciendo el id_op, el campo, el numero
      escrito, el numero real y la ruta.
    - Si la ruta citada no existe, ROJO.
    - Si no hay ningun par, VERDE EXIT 0 diciendo "0 pares" y las filas
      que examino, para que se vea que corrio.
    - Si cuadran todos, VERDE EXIT 0 con el recuento.
  Y llega con su CASO POSITIVO por el criterio de HECHO de la fase 08
  (docs/plan/08_VERIFICACION.md: "una fase esta hecha cuando su
  verificacion se caeria si el fallo volviera"): correla sobre una COPIA
  del OPERACIONES.jsonl de HOY (antes de la correccion 2.a), donde el
  punto 0 de OP-S-08 todavia dice "32 casos", y TIENE QUE DAR ROJO
  nombrando 32 contra 27. Pega las dos salidas, el rojo de la copia y el
  verde del fichero corregido.
  (1.g) ANTES DEL COMMIT DEL REPORTE, LAS TRES COMPROBACIONES, y las
  tres salidas se pegan:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 123 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR y las otras dos
  VERDE EXIT 0.
  (1.h) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE (acta 122, 4.4). El
  reporte de la 122 salio con 93 lineas y el tope del MODO AUSTERO 6.2
  son 80, sin la valvula que el 6.3 si le da al acta. ESTA VUELTA:
  wc -l docs/loop/REPORTE.md tiene que dar 80 o menos, y esa cifra se
  escribe en el propio reporte, medida, no prometida. Lo que se recorta
  es la narracion: la verificacion no se recorta nunca.

- TAREA 2, LOS REGISTROS Y CORRECCIONES DEL ACTA 122. Aditivos puros
  donde toquen texto viejo, medidos con git diff --numstat y con
  grep -c "^-[^-]" sobre el diff en cero. Son cinco y el orden da igual.
  (2.a) LA CORRECCION DE LA CIFRA FALSA, QUE ES LA CARA (acta 122, 4.1).
  En docs/plan/OPERACIONES.jsonl, el punto 0 de verificacion de OP-S-08
  dice hoy "prueba propia en web/lib/engine/accesosResueltos.test.ts (32
  casos, verde en SALIDA_V122_WEB_APERTURA.txt)". MIDELO TU PRIMERO,
  corriendo npx vitest run lib/engine/accesosResueltos.test.ts desde
  web/, y pega la salida; no copies mi numero. La correccion va POR
  REMISION, sin borrar una letra: correccion declarada al final de ese
  punto con la cifra real medida hoy, su comando y su fichero de salida.
  LA FILA SIGUE HECHA: el acta 122 seccion 1.4 ratifica el cierre, lei
  los veinte sitios uno a uno; lo unico falso es el numero.
  (2.b) LA CORRECCION DE LA TRAMPA DE OP-S-09 (acta 122, 4.3). La nota
  de OP-S-09 dice "lectura de CONTENIDO, familia por familia (29)" y dos
  parrafos antes dice que la familia de estructura_de_gates y
  estructura_gates "desaparece entera" por el toque unico de la 78. Las
  dos no pueden ser ciertas. REMIDELO TU con
  scripts/loop/vuelta77_op_s09_nomina.py, restando esa familia, y
  publica: familias a leer, nodos y pares par a par. Mi medicion, para
  contraste y NO para copiar: 28 familias, 67 nodos, 39 pares (18
  familias de dos, 9 de tres, 1 de cuatro),
  docs/loop/SALIDA_V122_AUDITOR_TRES_CIFRAS.txt. Correccion declarada,
  aditiva, al final de la nota. Si tu medicion discrepa de la mia, LA
  DECLARAS, no la resuelves copiando.
  (2.c) LAS DOS CAIDAS DEL DICTADO, donde vive el registro largo, en
  docs/PENDIENTES.md, seccion nueva R.5 de la vuelta 122, como
  correcciones declaradas: (1) el reporte de la 122 publico "81
  insertadas" en PENDIENTES.md mas 08_VERIFICACION.md y su propio
  SALIDA_V122_TAREA2_NUMSTAT.txt dice 55 y 25, o sea 80, y la misma
  cifra quedo congelada en el mensaje de commit de d7521e8a, donde ya no
  se corrige en su sitio; (2) verificar_citas_del_reporte.py se estrecho
  en el mismo commit del reporte para dejar fuera toda fila de tabla, el
  REPORTE dijo "coteja cada afirmacion del vocabulario cerrado" sin
  nombrar el recorte, y el recorte solo vivio en el mensaje de commit.
  Las dos con su medicion y con el ramal del tramo doblado que cada una
  estrena.
  (2.d) LA ADJUDICACION DE LOS ALIAS, QUE ES MIA Y CIERRA EL DISCUTIBLE
  (c) DE LA 122 SIN DOCTRINA NUEVA (acta 122, seccion 3.3). NO SE BORRA
  NI UN ALIAS EN ESTA CAMPAÑA. En la ficha permanente
  campos-sucios-dataset de docs/PENDIENTES.md, entrada nueva, aditiva:
  que la fuente canonica del resolutor es ids_alias embebido en los
  nodos de master_graph.json (mapaDeAlias en web/lib/engine/graph.ts:109
  y su espejo scripts/reanclar_por_resolutor.py:51) y hoy da 0
  huerfanas y 0 colisiones, medido por ti; que los cuatro
  alias_map_*.json son de OTRA ETAPA (tres de ellos, capa_b, capa_c y
  auto, en ALIAS_MAP_FILES de scripts/run_phase1.py, linea 87, que
  reparan referencias rotas durante la curaduria, y capa_d_duplicates
  que no lo lee ningun script vivo); que sus 15 huerfanos quedan
  ANOTADOS COMO TRABAJO POST CAMPAÑA; y que la frase de la nota de
  OP-S-08 sobre "los 77 alias huerfanos se limpian aqui" queda acotada
  por correccion declarada citando el punto 2 de la decision del
  fundador del 28 ago 2026 (docs/loop/paradas/2026-08-28-titulo-nafta-
  ops01-DECISION.md), igual que se hizo con OP-S-01, OP-S-04 y OP-S-05.
  Remide tu las cifras antes de escribirlas.
  (2.e) UNA MEDICION QUE ENCONTRE Y QUE NO SE ARREGLA ESTA VUELTA (acta
  122, observacion final). web/app/api/project/[id]/follow/route.ts:232
  llama cargarEntrySeeds() SIN el grafo, con el grafo ya cargado en la
  linea anterior, y la version sin grafo NO filtra por esOfrecible
  (web/lib/engine/graph.ts:67): es la misma averia que OP-C-01 arreglo
  en los dos organizer. NO ESTA en los veinte de OP-S-08 (el censo del
  11 ago clasifico accesos directos graph[id], y este es una carga de
  semillas), asi que NO reabre nada. MIDELO: busca TODAS las llamadas
  vivas a cargarEntrySeeds en web/ (fuera de tests), di cuales pasan el
  grafo y cuales no, y anota el resultado en docs/PENDIENTES.md como
  observacion para la auditoria de cierre. NO TOQUES EL CODIGO: eso es
  fase 0 y la fase 0 esta cerrada.

- TAREA 3, EL TRABAJO: OP-S-09 SE ABRE COMO FRENTE DE LECTURA DIRIGIDA.
  LO ADJUDIQUE YO EN EL ACTA 122 SECCION 3.2 Y NO HACE FALTA DOCTRINA
  NUEVA: la forma ya existe en la casa (el campo tipo de
  docs/plan/OPERACIONES.jsonl trae LECTURA DIRIGIDA en OP-E-03 y LECTURA
  DIRIGIDA CORTA en OP-E-07) y el criterio ya esta escrito palabra por
  palabra en docs/MESA_RACIMOS.md:214: "dentro del racimo se lee par a
  par con el criterio continua o repite: si el segundo nodo continua al
  primero (otro momento, otro nivel, otro angulo), los dos viven; si
  repite, se fusiona"; la DECISION 4 (linea 343) anade familia unica y
  fusion con alias, con su excepcion escrita (la transdominio y el _2 de
  propiedad intelectual van por RENOMBRE O ALIAS y NO por fusion, porque
  en los dos el contenido esta sano). TU NEGATIVA DE LA 122 FUE
  CORRECTA: no se forzaban 29 veredictos sin leer. Ahora se leen.
  LAS TRES GUARDAS DE TODO INSTRUMENTO QUE ESCRIBA en dataset/ o en
  docs/plan/ SIGUEN VIGENTES Y SON BLOQUEANTES: (i) SIMULACION PREVIA
  sobre copia en memoria con su salida pegada, (ii) SU MUTACION NEGATIVA
  corrida y pegada, y (iii) SU ROJO REAL EN SEGUNDA PASADA, con la
  salida de git status --porcelain PEGADA DETRAS TAL CUAL SALGA, no
  descrita. Un instrumento de escritura sin las tres NO SE CORRE.
  (3.a) LA LECTURA, Y ES EL SUELO DE LA VUELTA. Las 28 familias enteras
  (39 pares, contra el tramo de 80 del MODO AUSTERO 1: cabe, y lo medi).
  Por cada familia, en un registro JSONL nuevo,
  docs/loop/SALIDA_V123_OPS09_LECTURA.jsonl, una linea con: familia,
  causa (sufijo, particulas u orden), miembros, veredicto CONTINUA o
  REPITE par a par, superviviente propuesto si REPITE, alias que hereda,
  y la razon en UNA linea citando el campo que la sostiene. LAS
  DECISIONES DE LECTURA VIVEN EN EL REGISTRO, NO EN PROSA DEL REPORTE
  (MODO AUSTERO 2). Y a contenido empatado desempata el grafo, que es lo
  que dice el punto 0 de verificacion de la propia fila.
  NO TOQUES estructura_de_gates NI estructura_gates: son de
  OP-M-01-FUSION por el toque unico de la vuelta 78 (banco 9.4) y
  tocarlas aqui es tocarlas dos veces.
  Y SI ALGUNA DE LAS 28 CAE EN LA EXCEPCION ESCRITA (transdominio, o el
  _2 de propiedad intelectual), su veredicto es RENOMBRE O ALIAS, NO
  fusion, y se dice por que.
  (3.b) LA EJECUCION, SOLO DESPUES DE QUE LAS 28 ESTEN LEIDAS Y
  REGISTRADAS. Con sus tres guardas, con alias para todo id que muera
  (verificacion 1 de la fila), con las aristas que apuntaban al id viejo
  resolviendo detras (verificacion 2), y con Gate 0 y las suites en
  verde en su propio checkpoint (1.d).
  Y LO DIGO YO POR ESCRITO PARA QUE NO HAYA DUDA: SI LA LECTURA DE LAS
  28 SE COMPLETA Y REGISTRA PERO LA EJECUCION NO CABE CON SUS TRES
  GUARDAS ENTERAS, ESO ES ENTREGA COMPLETA, NO UN LIMITE DE ALCANCE. La
  ejecucion pasa a la 124 y el reporte publica LA CUENTA DE GUARDAS que
  consumio la vuelta, guarda por guarda con su fichero. Lo que NO es
  entrega completa es leer la mitad de las familias.
  Y SI EL TEXTO DE LA OPERACION NO ALCANZA PARA RESOLVER UNA FAMILIA SIN
  DECIDIR ALGO QUE NINGUNA REGLA ESCRITA CUBRE, PARAS EN ESA FAMILIA, LA
  TRAES CON SU CASO ESCRITO Y SIGUES CON LAS DEMAS: una familia trabada
  no detiene las otras 27.
  (3.c) SI Y SOLO SI OP-S-09 CIERRA ENTERA CON SU EJECUCION: OP-S-10
  (orden 9, REENCUADRE_DE_MARCO, 31 nodos en el campo nodos). NO SE
  ESCRIBE NADA DE ELLA ESTA VUELTA: solo se REMIDE su nomina contra el
  grafo de hoy, como se hizo con OP-S-02, OP-S-04 y OP-S-09 (cuantos de
  los 31 siguen vivos, cuantos deprecados, y a quien reclama el alias de
  cada deprecado), y se publica. OP-S-12 va al final de la fase y no se
  abre.
  Y AVISO OTRA VEZ, PORQUE FALTAN POCAS: cuando la fase 05 quede cerrada
  y verificada se dispara la condicion de parada CIERRE DE LA FASE 05 de
  AUDITOR.md seccion 4. Quedan OP-S-09, OP-S-10, OP-S-11 y OP-S-12. NO
  declares la fase cerrada tu: mide, publica y dilo como discutible; el
  cierre lo adjudica el auditor.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
