Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 06 MESAS. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3), REGIMEN COMPLETO: el
modo austero sigue SUSPENDIDO por su propio punto 5.

EMPIEZA POR AHI Y NO ES UNA FORMULA: tu vuelta 142 dejo la TAREA 3.a HECHA
Y SIN COMMITEAR en docs/plan/OPERACIONES.jsonl. Lo verifique y el trabajo
es bueno (adicion pura, medida abajo), pero mientras siga fuera de un
commit ensucia la guarda P.16 de vuelta142_2c_mutaciones.py, que hoy sale
4 de 5 solo por eso. Ese commit es lo primero de la vuelta, ANTES incluso
del bloque de apertura, y va con la guarda semantica de la TAREA 3.a de
abajo pegada en su mensaje.

LO QUE TE DEVUELVO, Y ESTA ENTERO EN docs/loop/ACTA_AUDITOR.md, ACTA DE LA
VUELTA 142:

  - LO QUE ENTREGASTE ESTA BIEN Y LO VERIFIQUE ENTERO CON INSTRUMENTOS
    MIOS. Ciclo de Gate 0 OK con sus quince comprobaciones, motor 25/25,
    vitest 80 ficheros y 1.030 passed con 3 skipped, tsc EXIT 0 y cero
    lineas, desfase del calibrado 468 filas con 4 de desfase. Censo con
    parser propio sobre dataset/nodos/: 3.853 / 3.171 / 682 y
    9.230 / 9.204 / 18.434 / 9.905, IDENTICO a tu conteo de apertura, o
    sea CERO aristas movidas, que es lo coherente con que la 3.b no
    corriera. La apertura sellada VERDE con los diez dentro y hija directa
    de fd020d71. Los tres numstat por adicion pura: 221/0 y 152/0, y
    OPERACIONES.jsonl sin tocar en ningun commit. Cero guiones largos y
    cero medios en las lineas anadidas.
  - LA TAREA 2 MUERDE, PUNTO POR PUNTO, Y LA CORRI YO. La guarda de cifras
    sale hoy ROJO EXIT 1 con COBERTURA CERO nombrada, el vocabulario paso
    de 8 a 24 palabras y la nomina de unidades fuera se publica; y muerde
    donde tenia que morder, porque entre sus nueve rojos estan las dos
    lineas del "18 direcciones". El bloque de commits anclado al sello
    sale VERDE sobre el reporte de la 141 (11 contra 11, mismo orden)
    donde antes daba ROJO con 13, y ROJO por fichero ausente con --vuelta
    142. La vara FUSION publica su tercer veredicto sin mover NI UNA cifra
    de la fase 06: mi diff contra tu sellada de la 141 da UNA sola
    diferencia, los dos sub-sacos nuevos, los dos en cero. Y las cuatro
    baterias: 4 de 4, 3 de 3, 5 de 5 en tu sellada con el arbol limpio, y
    3 de 3.
  - TU CORRECCION AL ENCARGO SOBRE EL ANCLA ES CORRECTA Y LA MEDI:
    git rev-parse 5a82ce38^ da exactamente 84e4d861. El hash sellado es el
    PADRE del commit que lo lleva, asi que el rango bueno acaba en el
    commit que lo lleva, leido con --diff-filter=A. Bien traida.
  - LA CIEGA LA GANASTE EN LA UNIDAD QUE IMPORTA. Escribi mi propio
    instrumento (parser de prosa, resolutor propio, colapso por alias) y
    lo corri ANTES de abrir la CORRECCION 15: me dan tus mismos 17
    direcciones sobre las cinco (2+8+4+2+1) y 18 sobre las seis, con
    OP-M-05-APERTURA aportando exactamente 1. Donde NO coincidimos fue en
    "filas": yo conte 16 y tu 18. Lo mordi hasta el fondo y TU 18 ES EL
    BUENO: "fila de ficha" es la direccion escrita ANTES de resolver, que
    es la convencion que tallar_estado_de_fase.py sostiene desde la 141
    (OP-E-05 son 2 entradas JSON que el parser abre en 4 filas;
    OP-M-05-APERTURA es 1 entrada que abre en 2). Yo contaba entradas del
    array JSON, que es una TERCERA unidad que ningun documento nombra. Lo
    declaro en vez de resolverlo copiando, y la TAREA 1.c lo registra.
  - TUS DOS PARADAS: LAS DOS BIEN TRAIDAS, Y LAS DOS SON CAIDAS DE MI
    ENCARGO. La del 2.e tiene razon entera: pedi que los cuatro de mas
    bajaran a DOS, y eso contradice mi propia adjudicacion 3.5 de la 141,
    que dice NUNCA CUMPLIDO. Si DIVERGENTE saliera de "sin cumplir", una
    fase con una operacion EJECUTADA AL REVES dentro publicaria
    "sin cumplir: 0" y la frase "la fase cierra" pasaria la guarda. Tu
    docstring lo dice mejor que mi encargo. Lo que se arregla es LA
    EXPECTATIVA, no la vara. La del 2.a.ii tambien: el ROJO es exactamente
    el que yo pedi con esas palabras, y tu descarte por computo esta bien
    razonado. Lo que no puede quedarse asi es que la bateria entera quede
    en ROJO PERMANENTE.
  - Y LA GRANDE, QUE LA TRAIGO YO Y ES LA QUE MANDA EN ESTA VUELTA: LA
    VARA DE ENLACE NO LEE LA EXCEPCION QUE TU 3.a ACABA DE ESCRIBIR, Y NO
    PUEDE LEERLA. Lo medi con el arbol en las dos posiciones: corri
    tallar_estado_de_fase.py --fase 06_MESAS con tu 3.a puesta y con tu
    3.a guardada en git stash, y la celda de OP-E-04 sale IDENTICA en las
    dos, "regimen de vuelta PROHIBE por la ficha (verificacion 0): la
    vuelta presente IMPIDE cumplir". La causa esta en el codigo:
    regimen_de_vuelta() clasifica POR OPERACION contra seis frases
    literales, y el texto de tu excepcion no lleva ninguna de las de
    MUTUO. Y si la llevara SALDRIA AMBIGUO CON FALLO, porque la
    verificacion 0 sigue entera. O sea que NO HAY REDACCION POSIBLE que
    arregle esto mientras el regimen sea por operacion. Consecuencia
    medida: OP-E-04 no puede llegar a CUMPLIDA ni ejecutando la 3.b
    entera, "sin cumplir" nunca baja de 1 y LA FASE 06 NO PUEDE CERRAR
    NUNCA. No es doctrina nueva: el banco 9.22 define la figura POR PAR
    ("La figura exige dos lineas distintas, una en cada nodo", "El par es
    sano") y el hueco de orden 1 del 00_INDICE:482 exige literal "LA
    GUARDA TIENE QUE LLEVAR LA EXCEPCION ESCRITA". Hoy no la lleva.
  - UNA CAIDA TUYA GRANDE Y NO ES DE CIFRA (4.1): LA VUELTA 142 NO TIENE
    REPORTE, NI BLOQUE DE CIERRE, NI CABECERA TALLADA. REPORTE.md sigue
    siendo el de la 141, no existe ningun SALIDA_V142_*_CIERRE.txt y
    verificar_cierre_sellado.py --vuelta 142 sale ROJO por fichero
    ausente. Sin reporte no hay donde vivan la particion ("diciendo CUAL
    no hiciste y por que") ni la TAREA 4. Quinta vuelta no entregada
    entera (81, 114, 127, 129 y esta). Y una de procedimiento (4.2), la
    3.a sin commitear. NINGUNA de cifra ni de clase: recompute todo y
    cuadra al digito, y la racha de cifra publicada SIGUE EN CERO.
  - Y LAS MIAS, TRES, TODAS DE ENCARGO Y TODAS TUYAS DE RAZON: los cuatro
    de mas que no podian bajar a dos (4.6); el "CERO BORRADAS" que pedi en
    un JSONL donde cada ficha es UNA LINEA, inalcanzable por construccion
    porque cualquier adicion da 1/1 (4.7); y medir el vocabulario sobre
    "el reporte de esta vuelta" en una TAREA 2 que corre ANTES de que el
    reporte exista, circular por construccion (4.8).

- TAREA 0, EL BLOQUE DE APERTURA, DESPUES DEL COMMIT DE LA 3.a Y ANTES DE
  LA PRIMERA OPERACION NUEVA. Va numerado 0 porque es un sello y no un
  trabajo.
  (0.a) EL SELLO: el HEAD de 40 caracteres, una sola linea, en
  docs/loop/SALIDA_V143_HEAD_APERTURA.txt, leido de git rev-parse HEAD.
  (0.b) LA BATERIA DEL LADO APERTURA, con el arbol LIMPIO, en este orden y
  una sola vez: el ciclo (python scripts/run_phase1.py
  --reaplico-curaduria, luego scripts/etiquetas_de_cara.py --aplicar,
  luego scripts/sync_assets_web.py, luego git diff --numstat --
  dataset/ web/ engine/), el conteo del censo, el motor
  (python engine/run_all_tests.py), vitest, tsc, Y EL DESFASE DEL
  CALIBRADO (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK).
  (0.c) LOS DIEZ NOMBRES CANONICOS, con LADO = APERTURA, y el gemelo de
  CIERRE al final de la vuelta con los mismos diez nombres:
  SALIDA_V143_HEAD_<LADO>.txt, SALIDA_V143_GATE0_CMD1_<LADO>.txt,
  SALIDA_V143_CONTEO_<LADO>.txt, SALIDA_V143_MOTOR_<LADO>.txt,
  SALIDA_V143_WEB_<LADO>.txt, SALIDA_V143_TSC_<LADO>.txt,
  SALIDA_V143_CICLO_ETIQUETAS_<LADO>.txt,
  SALIDA_V143_CICLO_SYNC_<LADO>.txt,
  SALIDA_V143_CICLO_NUMSTAT_<LADO>.txt,
  SALIDA_V143_DESFASE_CALIBRADO_<LADO>.txt.
  (0.d) LA COMPROBACION: python scripts/loop/verificar_apertura_sellada.py
  --vuelta 143. Tiene que dar VERDE EXIT 0 ANTES de que toques nada mas,
  con los DIEZ dentro.
  EL BLOQUE DE APERTURA (0.a mas 0.b mas 0.c) VA EN UN SOLO COMMIT.
  EL COMMIT DE LA 3.a DE LA 142 VA ANTES QUE EL, Y LO DIGO EXPRESAMENTE
  PARA QUE verificar_apertura_sellada.py no te obligue a elegir: el sello
  de apertura es hijo del commit de la 3.a, no del commit del acta, y esa
  desviacion queda DECLARADA aqui por mi, con su motivo, que es que el
  trabajo ya estaba hecho y no se tira.

- TAREA 4 ADELANTADA, Y VA LA SEGUNDA PORQUE ES LO QUE FALLO: EL CIERRE DE
  LA VUELTA SE PREPARA AHORA, NO AL FINAL. Escribe hoy, nada mas cerrar la
  TAREA 0, el esqueleto de docs/loop/REPORTE.md de la vuelta 143 con su
  cabecera vacia entre los delimitadores y las secciones por tarea. LO QUE
  SE MIDE SE VA PEGANDO DENTRO A MEDIDA QUE PASA. Y AL CIERRE, LAS TRES
  COSAS, LAS TRES OBLIGATORIAS:
  (4.a) la bateria del lado CIERRE con los mismos diez nombres, y
  SALIDA_V143_HEAD_CIERRE.txt sellado TRAS la ultima operacion y ANTES de
  escribir el hash en el reporte.
  (4.b) tallar_cabecera_reporte.py --vuelta 143 --fase04 corrido, SU TABLA
  PEGADA ENTERA entre las dos marcas, mas --comparar docs/loop/REPORTE.md
  dando CABECERA IDENTICA AL TALLADOR, mas --comparar-commits contra el
  HEAD sellado.
  (4.c) verificar_cifras_del_reporte.py corrido SOBRE TU PROPIO REPORTE
  antes de commitearlo, con su linea de COBERTURA pegada: cuantas cifras
  vio, cuantas cotejo, cuantas se quedaron fuera y con que unidades. UNA
  GUARDA QUE SALE VERDE SOBRE CERO NO ES UNA GUARDA, Y AHORA YA NO PUEDE
  SALIR VERDE SOBRE CERO: usala.
  SI LA VUELTA SE TE ACABA, EL REPORTE Y EL BLOQUE DE CIERRE SON LO ULTIMO
  QUE SE SACRIFICA, NO LO PRIMERO. Antes de eso se parte la TAREA 3.

- TAREA 1, LOS REGISTROS.
  (1.a) R.24 EN docs/PENDIENTES.md, POR ADICION, como hiciste con R.23:
  las seis adjudicaciones de mi acta 142 (3.1 a 3.6), tus DOS caidas (4.1
  de incumplimiento de encargo por la vuelta sin reporte ni cierre, y 4.2
  de procedimiento por la 3.a sin commitear), las TRES de la casa (4.3 la
  vara que no lee la excepcion, 4.4 la bateria en rojo permanente, 4.5 la
  expectativa inalcanzable) y MIS TRES (4.6, 4.7 y 4.8, todas de encargo),
  escritas igual que las tuyas, mas la racha de reporte QUE SIGUE EN DOS
  con la escalada encargada y la de cifra publicada QUE SIGUE EN CERO.
  Numstat con anadidas y borradas, y las borradas en cero.
  (1.b) LA CORRECCION 17, POR ADICION Y EN
  docs/plan/CORRECCIONES_A_APLICAR.md: EL 00_INDICE DICE "LAS UNICAS" Y
  HOY SON EL DOBLE. Es mi adjudicacion 3.4. docs/plan/00_INDICE.md:478
  dice literal "Los dos enlaces mutuos del banco 9.22 son las UNICAS
  aristas del plan que van en las dos direcciones a proposito". Registra
  al lado, MEDIDO CON TU INSTRUMENTO Y NO TECLEADO, cuantos pares del plan
  llevan hoy sus DOS direcciones escritas en su propio aristas_nuevas,
  nombrandolos con su LD y su operacion. Mi medicion de contraste, para
  que la coteges y declares la discrepancia si la hay: CUATRO pares y OCHO
  aristas, dos de OP-E-05 (sistema_gates_go_kill con
  gestion_portafolio_formal por LD-41, y con gestion_portafolio_dos_niveles
  por LD-43) y dos de OP-E-04 (con portfolio_management por LD-40 y LD-48,
  y con gestion_portafolio_foco por LD-45 y LD-53). NO BORRES LA FRASE DEL
  00_INDICE ni la reescribas: la correccion la coloca al lado con su
  fuente. Cada cifra con su autor, su corte y su fichero.
  (1.c) LA CORRECCION 18, POR ADICION: LA TERCERA UNIDAD QUE NADIE NOMBRA.
  Es mi seccion 2. Deja escrito, con las tres cifras medidas por tu
  instrumento sobre las cinco remitidas, que conviven TRES unidades:
  ENTRADA DE aristas_nuevas (el elemento del array JSON), FILA DE FICHA
  (la direccion escrita ANTES de resolver, que es lo que
  tallar_estado_de_fase.py llama fila y publica desde la 141) y DIRECCION
  (tras resolver por alias, P.1, que es la unidad adjudicada por el acta
  140). Da los tres totales medidos hoy y el ejemplar de cada salto:
  OP-E-05, que es 2 entradas, 4 filas y 4 direcciones; y OP-M-05-APERTURA,
  que es 1 entrada, 2 filas y 1 direccion. Y deja la regla que queda: una
  cifra de esta familia se publica SIEMPRE con su unidad nombrada, y
  "filas de ficha" NUNCA significa filas del array JSON.
  NO TOQUES docs/plan/OPERACIONES.jsonl en esta tarea.

- TAREA 2, LA ESCALADA, OPERACION DE CODIGO BLOQUEANTE, ANTES DE TOCAR
  NINGUNA OPERACION DEL PLAN. La racha de reporte SIGUE EN DOS, asi que
  AUDITOR.md 1.2 me obliga a encargarla otra vez y no espera decision de
  nadie. Cada punto con su caso por mutacion SOBRE UNA VARIABLE QUE EL
  CODIGO COMPUTE, nunca sobre un literal (EJECUTOR regla 1), su salida
  pegada, y el ciclo de Gate 0 con las suites detras.

  (2.a) EL REGIMEN DE VUELTA PASA A SER POR PAR, Y ES LA PARTE MAS
  IMPORTANTE DE TODA LA VUELTA. Es mi adjudicacion 3.3 y la caida 4.3. En
  scripts/loop/tallar_estado_de_fase.py:
    (i) LA FICHA PUEDE DECLARAR PARES EXCEPTUADOS, Y LA VARA LOS LEE. La
        excepcion se lee de la `verificacion` de la ficha, NUNCA del campo
        `tipo` y NUNCA adivinada: se parsea la lista de pares que la
        excepcion nombra, por sus ids o por sus LD, y se resuelven por
        alias (P.1) antes de comparar. La frase que la dispara va LITERAL
        de la ficha y citada en el codigo, como ya hiciste con las seis de
        la 141.
    (ii) EL REGIMEN DEJA DE SER UNO POR OPERACION. Una operacion con
        excepcion tiene regimen PROHIBE para las direcciones cuyo par NO
        esta exceptuado, y MUTUO para las de los pares que SI lo estan.
        Una operacion sin excepcion se comporta EXACTAMENTE como hoy.
        LLEVAR PROHIBE Y UNA EXCEPCION NOMBRADA A LA VEZ DEJA DE SER
        AMBIGUO: eso es justo lo que el hueco de orden 1 del 00_INDICE
        manda que exista. AMBIGUO se reserva para la ficha que prohibe y
        exige la vuelta SIN nombrar pares.
    (iii) LA CELDA PUBLICA EL DESGLOSE Y NO UN TOTAL PELADO: cuantas
        direcciones bajo PROHIBE con la vuelta presente (que impiden
        cumplir), cuantas bajo MUTUO con las dos direcciones (que se
        exigen), y la NOMINA de los pares exceptuados que la ficha nombra,
        para que se vea crecer.
  MUTACIONES, TODAS EN MEMORIA Y CON EL SUJETO ELEGIDO POR COMPUTO:
  (i) sobre una ficha con excepcion, meter la vuelta de una direccion
  cuyo par NO esta exceptuado y comprobar que la operacion sale NOMBRADA
  en SIN CUMPLIR y la cifra baja, con contraprueba sin mutar; (ii) sobre
  esa misma ficha, quitar una direccion de un par SI exceptuado y
  comprobar que la operacion sale SIN CUMPLIR por FALTA, no por vuelta;
  (iii) borrar de la ficha la linea de la excepcion y comprobar que la
  operacion vuelve al regimen PROHIBE de hoy, con el mismo texto de celda
  que sale ahora, para probar que el comportamiento viejo no se rompio.

  (2.b) LA BATERIA VUELVE A PODER ESTAR VERDE. Es mi 3.2 y la caida 4.4.
  En scripts/loop/vuelta141_2_mutaciones.py, el caso 2.a.ii deja de
  depender de que exista un sujeto real y FABRICA EL SUYO EN MEMORIA,
  exactamente como vuelta142_2c_mutaciones.py hace con OP-M-02-PROG:
  elige POR COMPUTO una operacion ENLACE con regimen PROHIBE, le mete en
  memoria la vuelta de una de sus direcciones para tener el defecto que
  quiere probar, y ENTONCES la quita y comprueba que la cifra sube. Si
  tampoco asi hay sujeto, sigue siendo ROJO y se dice por que. Despues
  vuelve a correr verificar_mutaciones_viejas.py y PEGA SU SALIDA: tiene
  que salir VERDE con las SIETE, NO MORDIO en cero. MUTACION: rompe a
  proposito el caso fabricado y comprueba que la bateria lo marca.

  (2.c) LA EXPECTATIVA DEL CASO POSITIVO SE RECOMPUTA. Es mi 3.1 y la
  caida 4.5. En scripts/loop/vuelta141_2e_caso_positivo_fase03.py, la
  expectativa deja de ser "cumplido igual a catalogo menos las seis
  remitidas" y pasa a ser, con las tres cuentas que la vara si puede
  producir: cumplido MAS consumidas con superviviente divergente MAS sin
  vara escrita igual a catalogo menos las seis remitidas, con las tres
  NOMBRADAS y no solo contadas. Las seis remitidas se siguen leyendo del
  00_INDICE de 62d4f28e, no se teclean, y los cuatro blobs se siguen
  cotejando por sha256. Con eso tiene que salir VERDE EXIT 0 sobre el
  grafo de hoy. Si sale otra cosa, LO DICES Y PARAS ESE CASO con la
  medicion encima, como hiciste bien en la 140, en la 141 y en la 142.
  MUTACION: mueve una de las dos divergentes al saco de cumplidas en
  memoria y comprueba que la expectativa vuelve a fallar nombrandola.

- TAREA 3, EL TRABAJO. NADA DE ESTO ANTES DE QUE LA TAREA 2 ESTE VERDE.
  (3.a) EL COMMIT DE LA 3.a DE LA VUELTA 142, QUE YA ESTA HECHO EN EL
  ARBOL Y SOLO LE FALTA EL COMMIT. Ya lo verifique yo y te doy la
  medicion para que la pegues en el mensaje, RE-CORRIDA POR TI y no
  copiada: 71 fichas antes y 71 despues, la unica que cambia es OP-E-04,
  el unico campo es `verificacion`, que pasa de 5 a 6 lineas, y las cinco
  viejas son PREFIJO IDENTICO de las seis nuevas. ESA ES LA GUARDA BUENA
  Y NO EL NUMSTAT: mi "cero borradas" de la 141 era inalcanzable en un
  JSONL de una linea por ficha, y va como caida mia (4.7). Pega tambien
  el git show --numstat, que dara 1/1, y di al lado por que 1/1 es lo
  correcto aqui. Si al releerlo encuentras que el texto de la excepcion
  no dice alguna de las cinco cosas que el encargo de la 142 pedia, lo
  dices y lo traes ANTES de commitear, no lo reescribes sin declararlo.
  (3.b) OP-E-04 SE EJECUTA ENTERA, en su propio commit, con las guardas de
  siempre: simulacion previa sobre copia en memoria, mutacion negativa con
  cero escrituras, los dos extremos VIVOS hoy o resueltos por alias
  declarandolo, P.9 (id resuelto, que no nazca por alias), P.16, EL GRADO
  TOTAL MEDIDO ANTES Y DESPUES con el ciclo CORRIDO entre las dos medidas,
  cero duplicadas y cero auto-aristas tras resolver, y EL CICLO DE GATE 0
  CON LAS SUITES detras.
  (3.c) EL GIRO DEL PAR 5 VA EN EL MISMO COMMIT QUE SU IDA. La contraorden
  del 12 ago 2026 lo exige: la vuelta
  revision_portafolio_periodica -> sistema_gates_go_kill se retira Y la ida
  sistema_gates_go_kill -> revision_portafolio_periodica se escribe, en el
  mismo commit, y EL GRADO TOTAL NO SUBE NI BAJA porque es un giro y no una
  poda. Si sube o baja, te pasaste y lo dices.
  (3.d) SI UNA ESCRITURA O UNA RETIRADA TOCA UNA ARISTA QUE NINGUNA
  OPERACION DEL PLAN PROPONE NI PROHIBE, PARAS ESA Y LA TRAES. Sigue viva.
  (3.e) CUANDO OP-E-04 ESTE EJECUTADA, vuelve a correr
  tallar_estado_de_fase.py --fase 06_MESAS con la vara nueva y pega su
  salida entera. Segun mi medicion de hoy, con OP-E-04 cumplida deberian
  quedar OP-M-01 cerrando por sus seis hijas y OP-M-04 en NO COMPUTABLE
  esperando a OP-U-01. SI ESO NO SE CUMPLE, LO MIDES Y LO TRAES, NO LO
  AJUSTAS. Y si la fase sigue sin cerrar, DILO NOMBRANDO LAS QUE FALTAN.
  EL CAMPO estado SIGUE SIN TOCARSE (actas 139 a 142): el pase de estado
  de las ONCE va en UNA sola adjudicacion mia, con el conteo antes y
  despues. No lo adelantes. OP-S-12 SIGUE AL FINAL DE LA PASADA ENTERA,
  por la atadura 2 del indice. Y OP-M-04 NO SE TOCA HOY.

SI LAS TAREAS NO CABEN CON SUS GUARDAS COMPLETAS, PARTE POR LA TAREA 3 Y
NO POR LAS GUARDAS NI POR EL CIERRE: entrega la 0, la 4, la 1 y la 2
enteras, y de la 3 lo que alcance en su orden (3.a antes que 3.b, y 3.c en
el mismo commit que su ida), diciendo CUAL no hiciste y por que. La TAREA
2 es BLOQUEANTE y no se parte: es la escalada de la racha. Y LA TAREA 4 NO
SE PARTE TAMPOCO: una vuelta sin reporte ni sello de cierre es una vuelta
que nadie puede leer, y eso fue lo unico que salio mal en la 142.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
