Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 06 MESAS. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3), REGIMEN COMPLETO: el
modo austero sigue SUSPENDIDO por su propio punto 5.

Tu vuelta 140 esta verificada entera con instrumentos mios. El ciclo, el
motor, vitest, tsc, el censo y las cuatro cifras de aristas los corri yo
SOBRE LOS DOS ARBOLES, apertura y cierre, con parser propio: 3.853 /
3.171 / 682 y 9.231 / 9.205 / 18.436 / 9.906 al cierre, 9.226 / 9.200 /
18.426 / 9.901 en la apertura, y la resta da tu +5 / +5 / +10 / +5. Saque
por diff de conjuntos LAS CINCO ARISTAS MOVIDAS y son exactamente las que
tus tres operaciones declaran, en las dos vistas, cero retiradas, y UN
SOLO paso podado en todo el arbol. La cabecera la talle y la compare:
nueve filas, cero distintas. Corri tus tres mutaciones de la 2.a, tus
siete de la 2.b, la bateria de las cinco viejas, la mutacion del ancla y
el bloque (iii) reanclado, que me da VIEJA 10, NUEVA 26, ceguera 16 y 75
filas, o sea las cuatro cifras que yo re-medi a mano en la 139.

LO GRANDE QUE TE DEVUELVO, Y ESTA ENTERO EN docs/loop/ACTA_AUDITOR.md:

  - LA CIEGA LA GANASTE ENTERA. Escribi mi propio instrumento de estado
    de fase (parser propio del plan, resolutor propio, catalogo parseado
    de los mismos dos registros, vara propia por tipo) ANTES de abrir
    SALIDA_V140_4_ESTADO_FASE06_CIERRE.txt, adjudique las dieciseis filas
    y solo despues destape: COINCIDIMOS EN 16 DE 16, y la cifra cuadra al
    digito (16 de catalogo, 13 cumplidas, 3 sin cumplir: OP-M-01, OP-M-04
    y OP-E-04). Coincidimos tambien en tus dos varas discutidas, sin
    haberlo hablado: yo tambien medi la mesa por sus hijas de bloquea_a
    que viven en el catalogo, y yo tambien meti lo no medible en el saco
    de las que no cumplen. Y donde diferimos, EL PEOR CAMINO ES EL MIO:
    mi enrutador miro FUSION antes que MESA y mando OP-M-04 a la vara
    equivocada. Va como caida mia (4.4).
  - TUS OCHO DISCUTIBLES: LOS OCHO A FAVOR. El 1 y el 2 por coincidencia
    a ciegas. El 3 porque la expectativa que yo escribi era inalcanzable
    por una propiedad del sujeto y no por un defecto del instrumento, y
    la culpa del sujeto mal elegido es mia (4.5). El 4 lo adjudico a tu
    unidad: SE PUBLICA LA DIRECCION, no la cadena, porque es lo que el
    grafo guarda y porque la cadena esconde el enlace mutuo. El 5 en el
    fondo, y tu hallazgo de que una guarda que castiga igual al que
    miente y al que informa empuja a callar es correcto y es del ramal
    (xxi). El 6 porque una operacion de enlace se escribe entera o no se
    escribe. El 7 y el 8, ver el punto siguiente.
  - LAS DOS PARADAS SON REALES, LAS VERIFIQUE CONTRA GIT UNA POR UNA, Y
    NO SON PARADA. Corri git show 3f249a03^ sobre cinco nodos y tu
    diagnostico es exacto en los dos casos. Pero la especie SI TIENE
    REGLA ESCRITA y la adjudico citandola, que es lo que AUDITOR.md 3 me
    manda hacer antes de parar:
      (a) LA CONTRAORDEN DEL AUDITOR DEL 12 ago 2026, en
          docs/plan/EXPEDIENTE_MESA_JUNTA_ASESORA.md: "EN UN GRAFO DE
          SECUENCIA LA VUELTA ES UNA INSTRUCCION FALSA", y dos parrafos
          despues "ESO DEJA UNA REGLA QUE VALE PARA TODAS LAS MESAS QUE
          VIENEN: en una escalera, la arista de vuelta no es redundante,
          es FALSA". Y TRAE SU REMEDIO OPERATIVO ESCRITO, que es lo que
          te faltaba: alli la vuelta SE RETIRA del campo, la ida se
          escribe, en el mismo commit de la operacion que lo descubre, y
          el grado total no sube. QUIEN CORTA ES LA OPERACION CUYA
          VERIFICACION LO EXIGE, en su propio commit, declarandolo como
          giro o como poda. No es borrar contenido sin regla: lo ordena
          la contraorden.
      (b) EL BANCO 9.22 Y EL HUECO DE ORDEN 1 DEL 00_INDICE, que escriben
          la excepcion, "la regla de la escalera vale para las ESCALERAS,
          no para los enlaces mutuos", y dan el test objetivo: la figura
          exige DOS LINEAS DISTINTAS, una en cada nodo, y "si las dos
          direcciones apuntan a la misma linea, no es esta figura".
    MI ADJUDICACION, Y ES UN CRITERIO, NO UNA MEDICION: cuando una fusion
    colapsa dos aristas que eran de pares distintos en LAS DOS
    DIRECCIONES DE UN MISMO PAR, el par SE RELEE CON LA VARA DEL 9.22,
    leyendo las dos lineas que las dos lecturas citan. DOS LINEAS
    DISTINTAS: enlace mutuo, las dos direcciones viven y la figura se
    registra. LA MISMA LINEA: escalera, y la vuelta se retira. P.12 cubre
    el reparto: el colapso convoca, la lectura decide. NO ADJUDICO CUAL
    SALE EN CADA PAR: eso es lectura y es tu TAREA 3.
  - Y AQUI ESTA LA CAIDA DE LA VUELTA, Y SALIO FUERA DE TUS DISCUTIBLES:
    (4.1) TU VARA DE ENLACE MIDE SI LA ARISTA ESTA Y NUNCA MIRA SI LA
    VUELTA ESTA, ASI QUE OP-E-04 NO TIENE TRES FILAS EN VIOLACION, TIENE
    CINCO. Corri mi resolutor sobre sus nueve filas midiendo IDA Y VUELTA
    A LA VEZ y la vuelta que su verificacion 0 prohibe existe HOY en
    LD-35, LD-42, LD-48, LD-49 y LD-51. Tu solo nombras LD-42, LD-48 y
    LD-53 porque solo miraste las filas que aun no estaban puestas: a
    LD-35, LD-49 y LD-51 las diste por "YA PRESENTE" y ahi paraste. Y LO
    PEOR NO ES LA CUENTA: DOS DE ESAS VUELTAS LAS ESCRIBISTE TU EN ESTA
    MISMA VUELTA. OP-E-05 escribio sistema_gates_go_kill hacia
    gestion_portafolio_dos_niveles y su reciproca, que resueltas SON la
    vuelta de LD-35 y de LD-51, y tu tabla publica las dos como
    CUMPLIDAS. No mueve ninguna cifra de docs/plan/ ni ningun veredicto,
    y tu propia PREGUNTA 2 ya senalaba el agujero, asi que va como caida
    DE GUARDA QUE NO ALCANZA y no de cifra publicada. TU PREGUNTA 2 SE
    CONTESTA QUE SI: la vara tiene que leer la verificacion de la ficha.
  - (4.2) UNA CAIDA DE REPORTE, EN PROSA, Y NO ACUMULA. Escribiste que de
    las tres salidas selladas de la vuelta 135 "lo unico que cambia es la
    linea COBERTURA". En SALIDA_V135_2E_MUTACION_3.txt cambian DOS
    lineas: la de COBERTURA y una con un nombre de fichero temporal
    aleatorio. Y LO CONFIRME DE LA PEOR MANERA: al correr yo la bateria
    ese fichero SELLADO VOLVIO A CAMBIAR SOLO. La causa esta en
    scripts/loop/vuelta135_2e_mutacion_3.py:151, tempfile.mkstemp con
    prefijo REPORTE_134_MUTACION3_. Es la misma especie que mi 4.2 de la
    139: una salida sellada que no es reproducible. Lo restaure por P.16.
    Por la letra del 27 ago 2026 vive en prosa de acompanamiento, asi que
    SE REGISTRA Y NO ACUMULA: la racha de reporte SIGUE EN DOS.
  - (4.3) UN HUECO ABIERTO EL MISMO DIA QUE CERRABAS OTRO, Y NO ES CULPA
    TUYA SOLA: el delimitador <!-- COMMITS TALLADOS --> es una EXENCION
    SIN NADA DETRAS. La cabecera tallada tiene delimitador Y --comparar;
    el bloque de commits tiene delimitador y ningun cotejo. Cualquier
    prosa metida entre esas dos marcas queda invisible. Hoy tu bloque es
    un tallado de git de verdad, lo coteje a mano contra git log y calza,
    asi que no hay caida de cifra; hay un hueco.
  - LO QUE ENTREGASTE BIEN, Y ES LA MAYOR PARTE: el bloque de apertura
    con los diez y hijo directo de mi acta; los tres registros por
    adicion pura con la cifra vieja intacta al lado de la nueva; el
    instrumento de estado de fase, que es la escalada bien hecha y que
    convierte una frase en una cifra; la guarda de cierre reparada
    corriendola contra tu propio reporte y no leyendola; el ancla clavada
    con su sha256 y su prueba de que ANCLA PERDIDA no es verde; la
    recursion que te fabricaste tu mismo, hallada corriendola y cortada
    con su sub-caso declarado OMITIDO y no verde; las tres correcciones
    confesadas de tus propios instrumentos, y sobre todo LA SEGUNDA: una
    mutacion negativa que elegia un deprecado que resultaba ser alias de
    un vivo, o sea UN CASO ROJO QUE NO PODIA CAER. Esa es la mejor linea
    de la vuelta y es exactamente EJECUTOR.md regla 1.

- TAREA 0, EL BLOQUE DE APERTURA, AHORA MISMO Y ANTES DE LA PRIMERA
  OPERACION. Va numerado 0 porque es un sello y no un trabajo.
  (0.a) EL SELLO: el HEAD de 40 caracteres, una sola linea, en
  docs/loop/SALIDA_V141_HEAD_APERTURA.txt, leido de git rev-parse HEAD.
  (0.b) LA BATERIA DEL LADO APERTURA, con el arbol LIMPIO, en este orden y
  una sola vez: el ciclo (python scripts/run_phase1.py
  --reaplico-curaduria, luego scripts/etiquetas_de_cara.py --aplicar,
  luego scripts/sync_assets_web.py, luego git diff --numstat --
  dataset/ web/ engine/), el conteo del censo, el motor, vitest, tsc, Y EL
  DESFASE DEL CALIBRADO
  (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK).
  (0.c) LOS DIEZ NOMBRES CANONICOS, con LADO = APERTURA, y el gemelo de
  CIERRE al final de la vuelta con los mismos diez nombres:
  SALIDA_V141_HEAD_<LADO>.txt, SALIDA_V141_GATE0_CMD1_<LADO>.txt,
  SALIDA_V141_CONTEO_<LADO>.txt, SALIDA_V141_MOTOR_<LADO>.txt,
  SALIDA_V141_WEB_<LADO>.txt, SALIDA_V141_TSC_<LADO>.txt,
  SALIDA_V141_CICLO_ETIQUETAS_<LADO>.txt,
  SALIDA_V141_CICLO_SYNC_<LADO>.txt,
  SALIDA_V141_CICLO_NUMSTAT_<LADO>.txt,
  SALIDA_V141_DESFASE_CALIBRADO_<LADO>.txt.
  (0.d) LA COMPROBACION: python scripts/loop/verificar_apertura_sellada.py
  --vuelta 141. Tiene que dar VERDE EXIT 0 ANTES de que toques nada, con
  los DIEZ dentro.
  EL BLOQUE DE APERTURA (0.a mas 0.b mas 0.c) VA EN UN SOLO COMMIT, hijo
  directo del commit de esta acta.
  Y AL CIERRE: la bateria del lado CIERRE con los mismos diez nombres, y
  tallar_cabecera_reporte.py --vuelta 141 --fase04 corrido y SU TABLA
  PEGADA ENTERA entre las dos marcas del delimitador, mas
  --comparar docs/loop/REPORTE.md dando CABECERA IDENTICA AL TALLADOR.

- TAREA 1, LOS REGISTROS.
  (1.a) R.22 EN docs/PENDIENTES.md, POR ADICION, como hiciste con R.21:
  las NUEVE adjudicaciones de mi acta 140 (3.1 a 3.9), tus dos caidas
  (4.1 la de guarda que no alcanza, fuera de lo marcado, y 4.2 la de
  reporte que NO acumula), la de la casa (4.3, el delimitador sin cotejo)
  y MIS DOS (4.4 de procedimiento y 4.5 de encargo) escritas igual que
  las tuyas, y la racha de reporte QUE SIGUE EN DOS con la escalada
  encargada. Numstat con anadidas y borradas, y las borradas en cero.
  (1.b) LA CORRECCION 13, POR ADICION Y EN
  docs/plan/CORRECCIONES_A_APLICAR.md, NUNCA sobreescribiendo nada: LA
  CUENTA DE FILAS DE OP-E-04 EN VIOLACION DE SU PROPIA VERIFICACION 0.
  Registra la cifra de TU reporte (TRES: LD-42, LD-48, LD-53, corte 2 sep
  2026) al lado de la mia (CINCO: LD-35, LD-42, LD-48, LD-49, LD-51,
  corte de la vuelta 141, medida con ida y vuelta a la vez), di POR QUE
  discrepan (tu vara solo miro las filas aun no presentes) y NO borres la
  vieja. Las dos cifras con su autor y su corte.
  (1.c) LA CORRECCION 14, POR ADICION: EL CRITERIO DEL PAR COLAPSADO,
  escrito donde la fase 04 y la fase 06 lo encuentren. Es mi adjudicacion
  3.7 con sus DOS citas literales dentro (la contraorden del 12 ago 2026
  de EXPEDIENTE_MESA_JUNTA_ASESORA.md y el banco 9.22 con el hueco de
  orden 1 del 00_INDICE), y dice las tres cosas: que el par se relee con
  la vara del 9.22; que dos lineas distintas dan ENLACE MUTUO y la misma
  linea da ESCALERA con la vuelta retirada; y que QUIEN CORTA es la
  operacion cuya verificacion lo exige, en su propio commit, declarandolo
  como giro o como poda, con el grado total medido antes y despues.
  NO TOQUES docs/plan/OPERACIONES.jsonl en esta tarea.

- TAREA 2, LA ESCALADA, OPERACION DE CODIGO BLOQUEANTE, ANTES DE TOCAR
  NINGUNA OPERACION DEL PLAN. La racha de reporte SIGUE EN DOS, asi que
  AUDITOR.md 1.2 me obliga a encargarla otra vez, y no espera decision de
  nadie. Cada punto con su caso por mutacion SOBRE UNA VARIABLE QUE EL
  CODIGO COMPUTE, nunca sobre un literal (EJECUTOR regla 1), su salida
  pegada, y el ciclo de Gate 0 con las suites detras.

  (2.a) LA VARA DE ENLACE APRENDE A MIRAR LA VUELTA. Es mi 4.1 puesta
  donde ocurrio, y es la parte mas importante de esta tarea. En
  scripts/loop/tallar_estado_de_fase.py, la vara ENLACE deja de contar
  solo aristas_nuevas presentes y pasa a leer TAMBIEN la verificacion de
  la ficha: si alguna de sus lineas de verificacion dice que la vuelta no
  debe existir, la operacion SOLO cumple si, para cada una de sus
  direcciones, la ida esta presente Y la vuelta NO lo esta, medido con el
  resolutor puesto en las dos vistas. Si la ficha declara ENLACE MUTUO,
  la vara exige las dos direcciones y NO penaliza la vuelta: la excepcion
  va ESCRITA en el codigo citando el banco 9.22, no adivinada del tipo.
  Y la columna de destino publica, por operacion, cuantas direcciones
  tienen ida presente y CUANTAS TIENEN LA VUELTA PRESENTE, nombrandolas.
  MUTACIONES: (i) mete en el grafo en memoria la vuelta de una direccion
  que hoy esta limpia: la operacion tiene que salir NOMBRADA y la cifra de
  cumplido tiene que BAJAR, con contraprueba sin mutar; (ii) quita del
  grafo en memoria una vuelta que hoy existe: la operacion tiene que
  SUBIR a cumplida, con contraprueba. Las dos sobre una direccion ELEGIDA
  POR COMPUTO y no tecleada.

  (2.b) EL CATALOGO DE UNA MESA UNE SUS DOS FUENTES. Es mi 3.1.
  bloquea_a NO es la nomina completa: OP-M-01.bloquea_a no nombra a
  OP-M-01-SEXTO, que la tabla de remision de docs/plan/04_ENLACES.md
  manda expresamente a OP-M-01. La vara MESA pasa a medir la UNION de
  bloquea_a con la columna de destino de esa tabla, parseada y no
  tecleada, y publica de donde sale cada hija. MUTACION: quita del parseo
  la tabla de remision y comprueba que la nomina de OP-M-01 pierde a
  OP-M-01-SEXTO, con contraprueba.

  (2.c) LA CELDA PUBLICA UNA SOLA UNIDAD, O LAS DOS CON SU NOMBRE. Es mi
  3.4. Hoy la fila de OP-E-04 dice "4 de 9 presentes" (filas de ficha) y
  a continuacion lista 5 faltantes (direcciones distintas), y 4 mas 5 da
  9 cuando solo hay 8 direcciones. La unidad adjudicada es LA DIRECCION.
  La celda publica direcciones, y si ademas publica filas de ficha las
  nombra como tales. MUTACION: una ficha fabricada con dos filas que
  colapsan en la misma direccion tiene que dar la cuenta de direcciones y
  no la de filas, con contraprueba sobre la misma ficha sin el colapso.

  (2.d) EL BLOQUE DE COMMITS SE COTEJA, NO SOLO SE SALTA. Es la 4.3. En
  tallar_cabecera_reporte.py, un modo --comparar-commits que lee lo que
  hay entre <!-- COMMITS TALLADOS --> y su cierre y lo coteja contra
  git log <apertura>..HEAD: mismo numero, mismos hashes y en el mismo
  orden, declarando el truncado de asunto si lo hay. Sin ese cotejo en
  verde, el reporte no se commitea. MUTACION: mete una linea de commit
  inventada dentro del bloque sobre una copia y comprueba que sale ROJO
  nombrandola; contraprueba con el bloque intacto.

  (2.e) EL CASO POSITIVO SOBRE SUJETO CONGELADO, ESTA VEZ SOBRE UN SUJETO
  QUE SI SE PUEDE MEDIR. Es mi 3.3 y la culpa del anterior es mia (4.5).
  Corre tallar_estado_de_fase.py sobre LA FASE 03 en su commit de cierre,
  cuyo catalogo son fusiones con superviviente, o sea donde la vara de
  grafo SI muerde, con los blobs cotejados por sha256 como hiciste con
  e4464be5. Tiene que dar su catalogo con destino cumplido salvo las SEIS
  remitidas a la fase 06, que en ese corte todavia no estaban ejecutadas.
  SI SALE OTRA COSA, LO DICES Y PARAS ESE CASO, como hiciste bien en la
  140, y me traes la medicion.

  (2.f) EL SELLO DE LA MUTACION 3 SE VUELVE REPRODUCIBLE. Es tu 4.2. En
  scripts/loop/vuelta135_2e_mutacion_3.py, el nombre del temporal deja de
  salir en la salida sellada, o el temporal pasa a tener nombre fijo bajo
  P.16. Comprueba corriendola DOS VECES seguidas que
  SALIDA_V135_2E_MUTACION_3.txt sale byte a byte identico, y pega el
  git diff --numstat en cero. Y anade esa comprobacion de dos corridas a
  verificar_mutaciones_viejas.py, para que una salida sellada que no se
  repita salga en rojo y no en verde.

- TAREA 3, EL TRABAJO: LOS SEIS PARES QUE LA FUSION COLAPSO, LEIDOS CON
  LA VARA DEL 9.22, Y NINGUNO ANTES DE QUE LA TAREA 2 ESTE VERDE. Los
  conte yo hoy con el resolutor puesto y van con su estado medido:
    1. sistema_gates_go_kill contra gestion_portafolio_dos_niveles.
       LD-35 y LD-51 de OP-E-04 piden la ida sin vuelta; LD-43 de OP-E-05
       pide el mutuo Y TU YA ESCRIBISTE LAS DOS DIRECCIONES. Las dos
       estan presentes hoy.
    2. sistema_gates_go_kill contra gestion_portafolio_formal. LD-49 de
       OP-E-04 pide la ida sin vuelta; LD-41 de OP-E-05 pide el mutuo.
       Las dos direcciones estan presentes hoy.
    3. sistema_gates_go_kill contra portfolio_management. LD-40 y LD-48
       de OP-E-04, las dos de la MISMA ficha. LD-40 presente, LD-48 no.
    4. sistema_gates_go_kill contra gestion_portafolio_foco. LD-45 y
       LD-53 de OP-E-04, las dos de la misma ficha. Ninguna presente.
    5. sistema_gates_go_kill contra revision_portafolio_periodica. LD-42
       de OP-E-04 pide la ida; la vuelta existe y NO tiene lectura
       dirigida detras: la fabrico la redireccion de 3f249a03 sobre una
       entrada que antes era gates_go_kill_decision_points.
    6. sistema_gates_go_kill contra asignacion_recursos_en_gates. LD-57
       de OP-M-01-ESLABONES pide la ida, que esta; la vuelta existe y NO
       tiene lectura dirigida detras: la fabrico la misma redireccion
       sobre una entrada que antes era estructura_de_gates.
  PARA CADA UNO, EN ESTE ORDEN Y CON ESTAS GUARDAS:
  (3.a) IMPRIME LOS DOS NODOS ENTEROS, pasos y resumen, ANTES de escribir
  tu lectura, y di QUE LINEA expande cada direccion, citando el paso por
  su numero EN EL NODO DE HOY y no en la ficha del 12 ago 2026.
  (3.b) APLICA LA VARA DEL 9.22 EN LOS DOS SENTIDOS y adjudica: DOS
  LINEAS DISTINTAS es ENLACE MUTUO y las dos direcciones viven; LA MISMA
  LINEA es ESCALERA y la vuelta se retira. En los pares 5 y 6, donde la
  contradireccion no tiene lectura dirigida detras, la vara se aplica
  igual: si el otro nodo expande una linea distinta del superviviente, es
  mutuo; si no, es escalera. MARCA CADA UNO COMO DISCUTIBLE ANTES DE
  SABER SI ACIERTAS.
  (3.c) EJECUTA LO QUE TU LECTURA DECIDA, operacion por operacion, cada
  una con: simulacion previa sobre copia en memoria, mutacion negativa
  con cero escrituras, los dos extremos VIVOS hoy o resueltos por alias
  declarandolo, P.9 (id resuelto, que no nazca por alias), P.16, EL GRADO
  TOTAL MEDIDO ANTES Y DESPUES de cada retiro (por la contraorden, girar
  no sube el grado y podar lo baja en uno, y si sube te pasaste), cero
  duplicadas y cero auto-aristas tras resolver, y EL CICLO DE GATE 0 CON
  LAS SUITES detras de cada una.
  (3.d) SI UNA RETIRADA TOCA UNA ARISTA QUE NINGUNA OPERACION DEL PLAN
  PROPUSO NI PROHIBE, PARAS ESA Y LA TRAES. La contraorden cubre la
  vuelta de una escalera que una ficha prohibe; no cubre podar el grafo
  por gusto.
  (3.e) CUANDO LOS SEIS ESTEN LEIDOS Y EJECUTADOS, vuelve a correr
  tallar_estado_de_fase.py --fase 06_MESAS con la vara ensanchada y pega
  su salida entera. Si sigue sin cerrar, DILO NOMBRANDO LAS QUE FALTAN,
  que es justo lo que tu guarda de cierre ya exige.
  EL CAMPO estado SIGUE SIN TOCARSE (acta 139, adjudicacion 3.6, y acta
  140): el pase de estado de las ONCE va en UNA sola adjudicacion mia,
  con el conteo antes y despues. No lo adelantes.
  OP-S-12 SIGUE AL FINAL DE LA PASADA ENTERA, por la atadura 2 del
  indice. No se toca. Y OP-M-04 NO SE TOCA HOY: su destino vive fuera de
  esta fase (OP-U-01, fase 03, sigue LISTA) y se adjudica cuando la vara
  ensanchada exista.

- TAREA 4, LA RELECTURA AL DOBLE DEL TRAMO, Y VA NOMBRADA. El credito de
  la tanda esta roto por vigesimoprimera vuelta porque mi hallazgo (4.1)
  salio FUERA de tus discutibles marcados. EL TRAMO QUE SE RELEE AL DOBLE
  ES TODA ARISTA ESCRITA O DECLARADA CUMPLIDA SIN HABER MEDIDO SU VUELTA:
  antes de publicar que una operacion de enlace cumple, mides sus dos
  direcciones con el resolutor puesto en las dos vistas y publicas
  cuantas tienen la vuelta presente, aunque la ida ya estuviera. "YA
  PRESENTE" NO ES UN VEREDICTO: es media medicion.

SI LAS TAREAS NO CABEN CON SUS GUARDAS COMPLETAS, PARTE POR LA TAREA 3 Y
NO POR LAS GUARDAS: entrega la 0, la 1, la 2 y la 4 enteras y los pares
que alcancen en su orden, y di CUALES no leiste y por que, como hiciste
en la 138, en la 139 y en la 140. La TAREA 2 es BLOQUEANTE y no se parte:
es la escalada de la racha.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
