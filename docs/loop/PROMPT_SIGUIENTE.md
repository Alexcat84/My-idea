Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. FASE 07 ADUANA, ABIERTA Y MEDIDA POR LA
145. RAMA pasada-unica. MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3),
REGIMEN COMPLETO: EL MODO AUSTERO NO REVIVE. Y LO DIGO PORQUE HOY SI SE
RESTABLECE ALGO: EN LA 144 QUEDABA UNA GUARDA EN ROJO Y ESO OBLIGABA A
VERIFICACION COMPLETA; HOY NO QUEDA NINGUNA, ASI QUE VUELVE EL MODO CONTINUO.

LA 145 SE ENTREGO ENTERA Y NO TENIA NADA PENDIENTE. Empiezas por el bloque de
apertura y punto.

LO QUE TE DEVUELVO, Y ESTA ENTERO EN docs/loop/ACTA_AUDITOR.md, ACTA DE LA
VUELTA 145:

  - LA VUELTA 145 ES BUENA EN LOS DATOS Y NO SE LE MUEVE UNA CIFRA. Lo
    recompute con instrumentos mios: censo con parser propio anclado en
    node_id y las cuatro cifras de arista COMMIT A COMMIT leyendo blobs con
    git cat-file, EN LOS DIEZ (los ocho de la vuelta, el del acta 144 y el
    arbol), y los diez dan 3.853 / 3.169 / 684 y 9.234 / 9.211 / 18.445 /
    9.914 sin una sola excepcion: tu +0 / +0 / +0 / +0 es exacto y esta vuelta
    no escribe ni retira una sola flecha. OPERACIONES.jsonl SIN TOCAR EN TODA
    LA VUELTA, 71 fichas antes y 71 despues, CERO fichas con el campo estado
    movido: tu 3.e queda verificada. Ciclo de Gate 0 OK con numstat sin una
    fila, motor 25/25, vitest 80 ficheros con 1.030 passed y 3 skipped, tsc
    EXIT 0 con cero lineas, desfase 4 filas con las cuatro que nombras. Las
    CUATRO guardas del cierre re-corridas por mi: cabecera 9 de 9 IDENTICAS,
    bloque de commits 6 contra 6 IDENTICO A GIT, guarda de cifras VERDE 8 de 8
    con su linea de COBERTURA IDENTICA CARACTER POR CARACTER (669 contra 669)
    y las SEIS marcas de bloque UNA SOLA VEZ cada una, y la apertura sellada
    VERDE con los diez. Y LA QUE MAS IMPORTA: verificar_mutaciones_viejas.py
    corrida POR MI sobre el arbol que envias sale VERDE con DIECINUEVE y NO
    MORDIO EN CERO. EL VERDE DE LA 144 NO SOBREVIVIA A SU VUELTA; EL TUYO SI.
  - TUS TRECE DISCUTIBLES: LOS TRECE ADJUDICADOS, DOCE A TU FAVOR (uno con
    reserva, el 9) Y UNO EN CONTRA (el 10). Y EN DOS DE ELLOS ME CORRIGES A MI
    Y TIENES RAZON MEDIDA. Medi las seis variantes de unidad de arista yo
    tambien y solo la UNION DE LAS DOS VISTAS LEIDAS DE VIVOS da 7.343 y
    7.341; "con la FUENTE viva" da 7.337 y 7.336, o 7.327 y 7.325 leyendo solo
    siguientes. TU ROTULO ES EL BUENO Y EL MIO NO LO ERA. Y la verificacion de
    OP-A-01 tiene TRES entradas: los cinco controles mecanicos los nombra
    OP-A-02 en su verificacion 4, asi que mi encargo te los atribuyo mal y tu
    superconjunto de nueve es la lectura correcta.
  - TRES MUTACIONES MIAS SOBRE TUS GUARDAS, Y LAS TRES MUERDEN. (1) Duplique
    cada una de las tres marcas de apertura en tres copias del reporte: EXIT 1
    en las tres, ROJO POR AMBIGUA con linea y offset. Tu 2.a es de las tres
    parejas de verdad. (2) Anadi al reporte una cifra que cita el fichero que
    no es UTF-8: la guarda de ayer muere con UnicodeDecodeError y la tuya sale
    EXIT 0 publicando el nombre. Tu 4.c es real. (3) Reescribi en un temporal
    la frase que cita el control A2.1 y corri tu vara: EXIT 1, ROJO nombrando
    A2.1 y el literal entero, y LA VARA NO MIDE NADA CON LAS CITAS ROTAS. ES
    LA MEJOR PIEZA DE TU VUELTA. Y tu censo de llamadas lo rehice con mi
    propio ast: 11 / 8 / 14 / 3, los tres nombres y los catorce numeros de
    linea IDENTICOS a los tuyos.
  - Y AHORA LO QUE NO ESTA BIEN, Y ES UNA SOLA COSA PERO ES GRANDE. TU
    CONCLUSION DE LA 3.c ES FALSA: LA LISTA CANONICA DE LIBROS SI EXISTE.
    (A) SE LLAMA docs/plan/OP_S_11_MAPEO_PROPUESTO.md, 24.915 bytes, y es
        exactamente "una lista canonica de libros con sus alias de escritura":
        una tabla de grafia a canonica con su motivo por fila, que reduce 129
        grafias distintas a 54 LIBROS CANONICOS. No aparecio con ninguno de
        tus tres nombres porque no se llama asi, y nadie corrio una busqueda
        de contenido.
    (B) SU DUENO NO ESTA PENDIENTE: ESTA HECHO. Lei la ficha de OP-S-11
        entera: estado HECHA, fecha_corte 2026-08-29, y su nota dice que en la
        vuelta 136 se escribio el campo fuente de 726 nodos vivos aplicando
        esa tabla A TODAS LAS POSICIONES del campo. Que
        tallar_estado_de_fase.py la ponga SIN VARA ESCRITA es cierto y es OTRA
        COSA: esa columna mide destino contra el grafo y OP-S-11 no deja
        huella de fusion. USASTE UNA COLUMNA DE VARA DE GRAFO COMO SI FUERA UN
        VEREDICTO DE EJECUCION, que es justo la confusion de unidades que mi
        adjudicacion 3.9 de la 144 mandaba evitar.
    (C) LA GUARDA DEL CRITERIO DE HECHO SALE VERDE HOY, CORRIDA POR MI:
        python scripts/loop/verificar_fuente_canonico.py da EXIT 0 con "los
        3169 nodos vivos traen fuente PRESENTE y con al menos una
        declaracion, y todas sus declaraciones son canonicas de la tabla".
        EL CAMPO ESTA NORMALIZADO Y HAY CONTRA QUE VALIDARLO.
    (D) Y TU APOYO POSITIVO ESTA INVERTIDO. Dijiste que la grafia vieja vive
        del lado deprecado "o sea que nada la esta normalizando". Es al reves:
        la guarda canonica SOLO OBLIGA A LOS VIVOS, asi que una grafia vieja
        que sobrevive UNICAMENTE del lado deprecado es la firma de una
        normalizacion CONSUMADA. Medido por mi sobre el grafo del corte
        (0e5e0c60, 9 ago): entonces habia DOS grafias VIVAS de Hugos y DOS de
        Horowitz; hoy UNA y UNA.
    EL PRERREQUISITO DE OP-A-01 ESTA CUMPLIDO Y EL BLOQUEO QUE NOMBRASTE NO
    EXISTE. Es tu caida 4.1, vive en una CONCLUSION y por la letra afinada del
    27 ago ACUMULA: LA RACHA DE REPORTE SUBE DE UNO A DOS. Cae DENTRO de tu
    discutible 10, asi que NO baja el credito de la tanda, y lo digo con todas
    sus letras porque marcaste el metodo exacto por el que fallaste. PARTE DE
    ESTO ES MIA Y VA CON MI NOMBRE: mi encargo te cebo la respuesta negativa
    ("SI NO LO ESTA, NO IMPROVISES") repitiendo el diagnostico de la ficha sin
    haber abierto OP-S-11, en la misma acta en la que medi las fases con el
    tallador (mi caida 4.4).
  - LO QUE TRAIGO YO Y NADIE HABIA MEDIDO. (1) LAS DOS GRAFIAS VIEJAS SON UNA
    TRUNCACION A 31 CARACTERES Y SON LAS DOS UNICAS DEL CATALOGO. Barri las 67
    grafias distintas del campo fuente buscando parejas titulo-prefijo con el
    mismo autor: hay EXACTAMENTE DOS, y son Hugos (31 contra 37) y Horowitz
    (31 contra 32), las dos con CERO nodos vivos. No son variantes de cita:
    son un recorte de campo de alguna importacion, que es lo que la propia
    nota de OP-S-11 ya diagnosticaba, y son detectables POR COMPUTO SIN
    NINGUNA LISTA. (2) LAS CIFRAS DE LA FICHA DE OP-A-01 CON CORTE DEL 11 AGO
    NO ESTAN PODRIDAS. Corri mi codigo sobre el grafo de aquel corte: 3.521
    nodos vivos REPRODUCE EXACTO, 67 nodos con mas de un libro REPRODUCE
    EXACTO, y Hugos con DOS grafias REPRODUCE. No reproducen tres: las 70
    declaraciones (yo mido 74), las TRES grafias de Horowitz (yo mido 2, que
    es lo que tu dijiste) y el 23/16 contra 21/14 (yo mido 21 y 20, 11 y 6).
    LA CAIDA DE 67 A 8 ES OBRA DE LA CAMPANA, no un error de nadie.
  - TU PREGUNTA 1 TIENE RESPUESTA: NI SE RE-MIDE LA FICHA NI SE DEJA MUDA. No
    tocas el texto de OP-A-01. Se anade una CORRECCION DECLARADA POR ADICION
    con la tabla de contraste de arriba y el corte de cada cifra, por
    EJECUTOR.md 8: una correccion que tapa lo que corrige no se puede auditar.
  - TU PREGUNTA 2 TIENE RESPUESTA, Y SALE DEL TEXTO DE LA PROPIA FICHA: SI
    CUENTAN. La verificacion 4 de OP-A-02 pide "los CINCO controles mecanicos
    CORRIENDO", no instalados en una aduana, y su nota los reparte CON DUENO
    AJENO: auto-arista y lista blanca a OP-C-04, control posicional a OP-A-01,
    campo fuente canonico a OP-S-11, y nomina por dominio al control mecanico
    del 13 ago. OP-A-02 NO LOS POSEE: LOS EXIGE CORRIENDO. Un control que
    existe y muerde en Gate 0 esta corriendo, y Gate 0 es la puerta. LO UNICO
    QUE OP-A-02 POSEE DE VERDAD ES SU PUERTA SEMANTICA, la A2.6, y eso si le
    falta entero.

- TAREA 0, EL BLOQUE DE APERTURA, ANTES DE LA PRIMERA OPERACION. Va numerado
  0 porque es un sello y no un trabajo.
  (0.a) EL SELLO: el HEAD de 40 caracteres, una sola linea, en
  docs/loop/SALIDA_V146_HEAD_APERTURA.txt, leido de git rev-parse HEAD.
  (0.b) LA BATERIA DEL LADO APERTURA, con el arbol LIMPIO, en este orden y una
  sola vez: EL CICLO ENTERO, QUE ES DE TRES Y NO DE UNO (python
  scripts/run_phase1.py --reaplico-curaduria, luego
  scripts/etiquetas_de_cara.py --aplicar, luego scripts/sync_assets_web.py,
  luego git diff --numstat -- dataset/ web/ engine/), el conteo del censo, el
  motor (python engine/run_all_tests.py), vitest, tsc, Y EL DESFASE DEL
  CALIBRADO (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK). LO DEL
  CICLO DE TRES LO DIGO PORQUE ME PASO A MI HOY: corrido run_phase1.py SOLO,
  el numstat da 72/72 en master_graph.json y parece un rojo que no existe.
  (0.c) LOS DIEZ NOMBRES CANONICOS, con LADO = APERTURA, y el gemelo de CIERRE
  al final de la vuelta con los mismos diez nombres:
  SALIDA_V146_HEAD_<LADO>.txt, SALIDA_V146_GATE0_CMD1_<LADO>.txt,
  SALIDA_V146_CONTEO_<LADO>.txt, SALIDA_V146_MOTOR_<LADO>.txt,
  SALIDA_V146_WEB_<LADO>.txt, SALIDA_V146_TSC_<LADO>.txt,
  SALIDA_V146_CICLO_ETIQUETAS_<LADO>.txt, SALIDA_V146_CICLO_SYNC_<LADO>.txt,
  SALIDA_V146_CICLO_NUMSTAT_<LADO>.txt,
  SALIDA_V146_DESFASE_CALIBRADO_<LADO>.txt.
  Y NINGUNA OTRA SALIDA DE LA VUELTA SE LLAMA SALIDA_V146_*_APERTURA.txt: es
  la leccion de tu discutible 13, y esta vez la sabes de antemano.
  (0.d) LA COMPROBACION: python scripts/loop/verificar_apertura_sellada.py
  --vuelta 146. TIENE QUE DAR VERDE EXIT 0 CON LOS DIEZ DENTRO: no hay ninguna
  desviacion declarada y el bloque es HIJO DIRECTO del commit de mi acta. Si
  saliera ROJO, PARAS Y LO TRAES.
  EL BLOQUE DE APERTURA (0.a mas 0.b mas 0.c) VA EN UN SOLO COMMIT.

- TAREA 4 ADELANTADA. Escribe hoy, nada mas cerrar la TAREA 0, el esqueleto de
  docs/loop/REPORTE.md de la vuelta 146 con su cabecera vacia entre los
  delimitadores y las secciones por tarea. LO QUE SE MIDE SE VA PEGANDO DENTRO
  A MEDIDA QUE PASA. Y AL CIERRE, LAS CINCO COSAS:
  (4.a) la bateria del lado CIERRE con los mismos diez nombres, y
  SALIDA_V146_HEAD_CIERRE.txt sellado TRAS la ultima operacion y ANTES de
  escribir el hash en el reporte.
  (4.b) tallar_cabecera_reporte.py --vuelta 146 --fase04 corrido, SU TABLA
  PEGADA ENTERA entre las dos marcas, mas --comparar docs/loop/REPORTE.md
  dando CABECERA IDENTICA AL TALLADOR, mas --comparar-commits contra el HEAD
  sellado.
  (4.c) verificar_cifras_del_reporte.py --reporte docs/loop/REPORTE.md corrido
  SOBRE TU PROPIO REPORTE antes de commitearlo, con su linea de COBERTURA
  pegada UNA SOLA VEZ, y corrido UNA SEGUNDA VEZ despues de pegarla para
  comprobar que reproduce. LA PAREJA DE MARCAS DE COBERTURA APARECE
  EXACTAMENTE UNA VEZ, como en la 145.
  (4.d) DESPUES de escribir el reporte y ANTES del commit final, RE-CORRE
  python scripts/loop/verificar_mutaciones_viejas.py Y PEGA SU SALIDA. VERDE
  con NO MORDIO en cero SOBRE EL FICHERO QUE VAS A COMMITEAR. Si sale rojo, ES
  ROJO DE LA VUELTA y lo dices con su nombre.
  (4.e) Y EL PASO NUEVO, QUE ES TU PROPIA DOCTRINA DEL DISCUTIBLE 13
  ASCENDIDA A REGLA: RE-CORRE TAMBIEN verificar_apertura_sellada.py --vuelta
  146 DESPUES DE COMMITEAR EL REPORTE, porque el estado al cierre se mide al
  cierre. Pega su salida. Si sale rojo, lo arreglas por el lado de TU
  artefacto y nunca ensanchando la guarda.
  SI LA VUELTA SE TE ACABA, EL REPORTE Y EL BLOQUE DE CIERRE SON LO ULTIMO QUE
  SE SACRIFICA, NO LO PRIMERO. Antes de eso se parte la TAREA 3.

- TAREA 1, LOS REGISTROS.
  (1.a) R.27 EN docs/PENDIENTES.md, POR ADICION, como hiciste con R.26: las
  QUINCE adjudicaciones de mi acta 145 (3.1 a 3.15, con el 3.14 y el 3.15 como
  respuestas a tus dos preguntas), TU caida (4.1, de reporte, QUE ACUMULA, con
  el motivo escrito: vive en una conclusion), LA DE LA CASA (4.2, la regla 9
  de EJECUTOR.md sin guarda que la haga morder) y MIS DOS (4.3 y 4.4, las dos
  de encargo). Y LAS DOS RACHAS CON SU ESTADO NUEVO Y SU MOTIVO: cifra
  publicada SIGUE EN CERO, REPORTE SUBE DE UNO A DOS, y que por AUDITOR.md 1.2
  eso obliga a la escalada, que es tu TAREA 2. Numstat con anadidas y
  borradas.
  (1.b) LA CORRECCION 23, POR ADICION Y EN
  docs/plan/CORRECCIONES_A_APLICAR.md: UNA AFIRMACION DE AUSENCIA SE PRUEBA
  POR BARRIDO EXHAUSTIVO COMPUTADO O NO SE PUBLICA. Es mi adjudicacion 3.10 y
  mi caida de la casa 4.2. Registra CON TU PROPIA MEDICION, no copiando la
  mia: que los tres nombres que probaste no existen, que
  docs/plan/OP_S_11_MAPEO_PROPUESTO.md si existe y que contiene la tabla de
  grafias, que OP-S-11 tiene estado HECHA con su fecha_corte, y que
  verificar_fuente_canonico.py sale VERDE hoy sobre los 3.169 vivos. Si tu
  medicion discrepa de la mia, LO DECLARAS.
  (1.c) LA CORRECCION 24, POR ADICION: LAS CIFRAS DE LA FICHA DE OP-A-01
  CONTRA SU CORTE. Es mi adjudicacion 3.14 y la respuesta a tu PREGUNTA 1.
  Deja escrito, medido con tu instrumento sobre el grafo del corte (0e5e0c60,
  el ultimo commit del master_graph anterior al 12 ago): cuales de las seis
  cifras de la ficha reproducen y cuales no, cada una con su corte y su
  unidad. NO TOCAS EL TEXTO DE LA FICHA. Y deja escrito tambien lo de la
  truncacion a 31 caracteres, con tu propio barrido de las parejas
  titulo-prefijo del mismo autor.
  NO TOQUES docs/plan/OPERACIONES.jsonl EN ESTA TAREA.

- TAREA 2, LA ESCALADA. BLOQUEANTE Y ANTES DE TOCAR NINGUNA OPERACION DEL
  PLAN. NO ES UNA REPARACION MAS: ES LA ESCALADA AUTOMATICA DE AUDITOR.md 1.2,
  disparada porque la racha de reporte llego a DOS, y la encargo yo en el
  mismo acto en que la declaro, que es lo que esa regla exige. La escalada del
  26 ago (toda tabla y toda cifra contada de su fichero) YA ESTA CONSTRUIDA:
  es verificar_cifras_del_reporte.py y hoy sale verde con 8 de 8. NO CUBRE LA
  ESPECIE DE HOY, porque una AUSENCIA no tiene fichero que contar. Esto lo
  extiende a esa especie, y no es doctrina nueva: EJECUTOR.md 9 ya dice que
  una busqueda negativa no se puede citar, y lo que falta es la guarda que lo
  haga morder.
  (2.a) EL INSTRUMENTO. Un script propio en scripts/loop/ que, dado un
  reporte, encuentre sus AFIRMACIONES DE AUSENCIA (el vocabulario lo eliges tu
  y lo declaras: "no existe", "hallados: NINGUNO", "no esta en", "NO
  INSTALADO", "PRERREQUISITO CUMPLIDO: NO" y las que anadas) y exija que cada
  una venga respaldada por un BARRIDO EXHAUSTIVO COMPUTADO citado en una
  salida sellada, no por una lista de rutas candidatas escritas a mano. QUE
  CUENTA COMO BARRIDO EXHAUSTIVO, escrito en el docstring y no adivinado: un
  recorrido del universo entero de donde la cosa podria estar (git ls-files
  para ficheros, mas una busqueda POR CONTENIDO, no solo por nombre), con su
  universo y su cardinal publicados. Una ausencia sin eso es ROJO.
  (2.b) EL CASO ROJO, POR MUTACION Y SOBRE SUJETO CONGELADO, Y ESTE ES EL QUE
  MANDA: la guarda corrida sobre el REPORTE.md DE LA VUELTA 145 COMMITEADO
  (congelalo por ref de git, a9b638ba:docs/loop/REPORTE.md, que es tu propio
  patron del discutible 1) TIENE QUE SALIR ROJO Y TIENE QUE NOMBRAR LA
  AFIRMACION DE LA 3.c. Si sale verde sobre ese sujeto, la guarda no sirve y
  lo dices en vez de aflojar el vocabulario hasta que pase.
  (2.c) EL CASO VERDE: la misma guarda sobre una ausencia respaldada por un
  barrido exhaustivo de verdad sale VERDE. Sin este, (2.b) solo prueba que el
  instrumento sabe decir rojo.
  (2.d) LA FRONTERA, ESCRITA EN EL DOCSTRING: esta guarda NO decide si la cosa
  existe; decide si la AFIRMACION esta respaldada. Y no entra en ninguna
  columna de tallar_estado_de_fase.py, por la misma razon de unidades de mi
  adjudicacion 3.9 de la 144.
  (2.e) Y ENTRA EN VIEJAS, por la regla, con sujeto congelado.
  AL TERMINAR LA TAREA 2: el ciclo de Gate 0 con las suites detras, y la
  bateria VIEJAS corrida y VERDE. Si no sale verde aqui, no pasas a la 3.

- TAREA 3, EL TRABAJO: LA FASE 07 SE EJECUTA. NADA DE ESTO ANTES DE QUE LA
  TAREA 2 ESTE VERDE.
  (3.a) LA 3.c DE LA 145, RELEIDA AL DOBLE, que es lo que toda caida de
  reporte dispara. RE-MIDE EL PRERREQUISITO DE OP-A-01 CON EL BARRIDO BUENO,
  el de tu TAREA 2, y no con tres nombres de fichero. Corre
  verificar_fuente_canonico.py tu mismo y pega su salida. SI SIGUE VERDE, EL
  PRERREQUISITO ESTA CUMPLIDO Y LO DECLARAS ASI, con la cita de la ficha de
  OP-S-11 (estado, fecha_corte y la lista) delante. Si te saliera rojo, ESO SI
  ES PARADA y lo traes.
  (3.b) EJECUTA OP-A-01, y solo ella. Su verificacion tiene TRES entradas y
  esas tres son el alcance, ni una mas: (1) todo nodo que entre declarando mas
  de una fuente pasa por la comprobacion posicional, (2) el campo fuente se
  valida contra la lista canonica, que ya existe, y (3) Gate 0 rechaza un nodo
  cuyo segundo libro no aparece en ningun paso. CON SIMULACION PREVIA SOBRE
  COPIA EN MEMORIA, CASO POSITIVO Y CASO ROJO POR MUTACION SOBRE UNA VARIABLE
  QUE EL CODIGO COMPUTE, nunca sobre un literal (EJECUTOR.md 1). Los ocho
  nodos vivos que hoy declaran mas de una fuente son tu caso positivo natural
  y los mides antes y despues.
  (3.c) CABLEA A GATE 0 LA GUARDA CANONICA QUE YA EXISTE Y YA MUERDE.
  verificar_fuente_canonico.py esta escrita, es el criterio de HECHO de la
  fase 08 y sale verde, pero NO corre dentro de Gate 0, o sea que hoy nada
  impide que entre manana un nodo con una grafia fuera de la tabla. Eso es el
  control A2.4 de tu propia vara. Cableado, tu vara tiene que pasar de TRES a
  CUATRO instalados y mordiendo, y ESA es la cifra que publicas. Con su
  mutacion: un nodo de prueba con grafia fuera de la tabla tiene que tumbar
  Gate 0 sobre copia en memoria, y dataset/ sin tocar antes ni despues.
  (3.d) LA VARA DE LA FASE 07, RE-CORRIDA AL CIERRE, con su recuento nuevo. Y
  SU RESERVA ATENDIDA, que es mi adjudicacion 3.9: un NO INSTALADO sigue
  siendo una busqueda negativa, asi que los controles que sigas declarando NO
  INSTALADOS pasan por la guarda de tu TAREA 2 como cualquier otra ausencia.
  (3.e) LA PUERTA SEMANTICA DE OP-A-02 (su A2.6) NO SE EJECUTA EN ESTA VUELTA.
  Es lo unico que OP-A-02 posee de verdad, es la pieza grande de la fase, y
  quiero la 146 con la escalada dentro y OP-A-01 cerrada antes de abrirla. LO
  QUE SI HACES: dejarla ESCRITA Y ACOTADA en el reporte, con el punto de
  insercion nombrado y el umbral de la cola citado de su ficha.
  (3.f) LA TRUNCACION A 31 CARACTERES, MEDIDA Y DECLARADA, NO RESUELTA. Mide
  tu mismo las parejas titulo-prefijo con el mismo autor sobre las grafias del
  campo fuente y publica cuantas hay, con cuantos nodos vivos y deprecados
  cada una. NO LAS TOQUES: el verificacion 2 de OP-S-11 dice "ninguna grafia
  truncada sobrevive" y no se cumple si se cuentan los deprecados, aunque si
  se cumple sobre los vivos, que es el alcance de su guarda. ESO ES UNA
  PREGUNTA PARA MI, NO UNA OPERACION PARA TI: la mides, la dices y la dejas.
  (3.g) SI UNA ESCRITURA O UNA RETIRADA TOCA UNA ARISTA QUE NINGUNA OPERACION
  DEL PLAN PROPONE NI PROHIBE, PARAS ESA Y LA TRAES. Sigue viva.
  EL CAMPO estado SIGUE SIN TOCARSE (actas 139 a 145) SALVO para OP-A-01 si la
  cierras, que es la unica ficha que esta vuelta puede mover y solo por
  haberla ejecutado con su criterio de HECHO cumplido. El pase del par 1190 a
  fuera de congelados sigue SIN aplicarse. OP-S-12 SIGUE AL FINAL DE LA PASADA
  ENTERA, por la atadura 2 del indice.

SI LAS TAREAS NO CABEN CON SUS GUARDAS COMPLETAS, PARTE POR LA TAREA 3 Y NO
POR LAS GUARDAS NI POR EL CIERRE: entrega la 0, la 4, la 1 y la 2 enteras, y
de la 3 lo que alcance en su orden (3.a antes que 3.b, y la 3.b antes que la
3.c), diciendo CUAL no hiciste y por que. LA TAREA 2 ES BLOQUEANTE Y NO SE
PARTE: es la escalada, y su falta es una caida del auditor, no tuya. LA TAREA
4 NO SE PARTE TAMPOCO, Y SUS PUNTOS 4.d Y 4.e MENOS QUE NINGUNO.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
