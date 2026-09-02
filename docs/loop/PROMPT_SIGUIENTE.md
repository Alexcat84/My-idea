Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 06 MESAS. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3), REGIMEN COMPLETO: el
modo austero sigue SUSPENDIDO por su propio punto 5.

ESTA VEZ NO HAY NADA PENDIENTE DE LA VUELTA ANTERIOR: la 143 se entrego
entera, con sus cinco tareas, su sello de cierre y su reporte, y el arbol
quedo limpio. Empiezas por el bloque de apertura y punto.

LO QUE TE DEVUELVO, Y ESTA ENTERO EN docs/loop/ACTA_AUDITOR.md, ACTA DE LA
VUELTA 143:

  - LA VUELTA 143 ES BUENA Y NO SE LE MUEVE UNA CIFRA. Lo recompute todo
    con instrumentos mios: censo con parser propio anclado en node_id
    (3.853 / 3.171 / 682) y las cuatro cifras de arista COMMIT A COMMIT
    leyendo blobs de git cat-file, que da 9.230 / 9.204 / 18.434 / 9.905
    en los cinco primeros y 9.234 / 9.208 / 18.442 / 9.909 en los tres
    ultimos: tu apertura, tu cierre y tu +4 / +4 / +8 / +4 son exactos, y
    el movimiento cae entero en un solo commit. Ciclo de Gate 0 OK con
    numstat sin una fila, motor 25/25, vitest 80 ficheros con 1.030 passed
    y 3 skipped, tsc EXIT 0 con cero lineas. Las tres guardas del cierre
    re-corridas por mi: cabecera 9 de 9 filas IDENTICAS, bloque de commits
    7 contra 7 en el mismo orden, guarda de cifras VERDE con 10 de 10. Las
    seis baterias corridas por mi: 7 viejas VERDE, 17 de 17, caso positivo
    CALZA, 5 de 5, 3 de 3, 5 de 5. La vara de la fase 06 sale BYTE A BYTE
    identica a tu sellada. Y tus aristas: las 8 direcciones que OP-E-04
    propone estan las 8 presentes, la unica retirada es la vuelta de LD-42
    que la propia ficha declara falsa, y ESCRITAS QUE LA FICHA NO PROPONGA:
    NINGUNA. Cero guiones largos y cero medios en todo lo anadido.
  - TU PARADA DE LA 0.d ES BUENA Y GANA, Y ES CAIDA MIA. Mi encargo pidio
    VERDE en verificar_apertura_sellada.py y en el mismo parrafo ordeno la
    desviacion que lo vuelve imposible. Hiciste lo correcto: no tocaste la
    guarda y lo trajiste. LA GUARDA NO SE TOCA NUNCA, y la regla que queda
    es MIA: un encargo no ordena una desviacion de una guarda y su VERDE a
    la vez; cuando la desviacion sea necesaria, el encargo declara el ROJO
    como resultado esperado y nombra la medicion que lo compensa. En esta
    vuelta no hay desviacion ninguna y la 0.d tiene que salir VERDE.
  - TUS OCHO DISCUTIBLES: LOS OCHO ADJUDICADOS, SEIS A TU FAVOR. La guarda
    5 del escritor NO es alcance indebido (adjudicacion 3.9 del acta 141,
    y la lees con la MISMA funcion que la vara). La comprobacion (B) del
    caso positivo es correcta y necesaria: tu propia mutacion prueba que
    (A) sola es ciega. Dejar la expectativa vieja midiendose es EJECUTOR.md
    8 literal. El grafo simulado es el patron que la 142 ya estreno. El
    instrumento nuevo para el giro es la decision correcta. Y restringir
    la ventana de la excepcion tambien lo es, y era necesaria.
  - LO QUE TRAIGO YO, Y ES LO QUE MANDA EN TU TAREA 2: TU VENTANA TIENE
    DOS AGUJEROS, LOS DOS MEDIDOS POR MUTACION MIA, LOS DOS SILENCIOSOS Y
    LOS DOS HACIA EL LADO PERMISIVO.
    (A) EL CIERRE. En pares_exceptuados_de la linea es
        `ventana = linea[ini:fin] if fin > ini else linea[ini:]`. Si falta
        el literal de cierre, find da -1 y LA VENTANA SE ENSANCHA HASTA EL
        FINAL DE LA LINEA SIN DECIR NADA. Medido: quitado "y ESCALERA" de
        la verificacion 5 en memoria, los pares exceptuados suben de 4 a 5
        y el que entra es revision_portafolio_periodica con
        sistema_gates_go_kill, o sea EXACTAMENTE EL PAR QUE LA EXCEPCION
        NIEGA POR ESCRITO, con CERO fallos declarados. Hay fallo ruidoso
        para la apertura ausente y para el caso de cero pares; para el
        cierre ausente no lo hay.
    (B) LA APERTURA. bajo.find(MARCA_ABRE_EXCEPCION) toma la PRIMERA
        ocurrencia. Medido con re.finditer sobre esa misma linea: "doble
        linea" aparece en las posiciones 381 y 859. LA VENTANA REAL
        ARRANCA EN 381, dentro de la prosa del punto (1) ("...NO para los
        enlaces de doble linea, por el banco 9.22..."), NO en 859, que es
        donde vive "adjudico DOBLE LINEA". Son 571 caracteres que se
        tragan el punto (1) entero, una cita a la CORRECCION 14, una ruta
        y un nombre de fichero. El comentario de tu codigo (lineas 541 a
        543) y tu discutible 1 describen una ventana que el codigo NO lee.
        Hoy sale bien POR SUERTE: en ese tramo no hay ningun LD-nn ni
        ningun patron de arista. El dia que una excepcion cite un LD en su
        encabezado, se cuela sola.
    (C) Y UNO MAS, ESTE FUERA DE LO QUE MARCASTE: en
        vuelta143_3c_girar_arista.py:222 la guarda 5 llama
        T.pares_exceptuados_de(op, resolver, []) y TIRA LOS FALLOS. El
        escritor no hace eso (vuelta140_3_escribir_aristas.py:149-164 los
        recoge, los imprime y ABORTA con ellos). Si el parseo falla, el
        conjunto sale vacio, exceptuado sale False, la guarda 5 dice OK y
        EL GIRO PROCEDE A BORRAR UNA ARISTA. El unico de los tres que se
        come sus fallos es el unico que destruye.
    NINGUNO MUEVE UNA CIFRA HOY. Los tres son guarda que no alcanza, y van
    a la casa, no a ti. Pero (C) cae mas alla de lo que marcaste, asi que
    EL TRAMO DE LECTURA DE LA EXCEPCION Y EL DEL GIRO SE RELEEN AL DOBLE
    EN ESTA VUELTA, y va escrito en la TAREA 2.
  - UNA CAIDA TUYA, DE REPORTE, Y NO ACUMULA: la linea de COBERTURA que
    pegaste dice "18 palabra(s)" fuera del vocabulario y hoy, corrida por
    mi sobre el REPORTE.md commiteado, da 30. Las doce nuevas son TODAS
    del propio bloque que pegaste (cotejadas, exentas, commit, bloque,
    cabecera, cifra, cifras, asunto, asuntos, palabra, viven, contra):
    pegar la salida dentro del fichero que la salida mide cambia la
    medida. El 18 era cierto al leerlo y falso al commitearlo, y eso no lo
    declaraste. El resto de la linea reproduce identico. NO acumula (letra
    del 27 ago 2026: no vive en tabla, cabecera ni conclusion), y el
    remedio es de la casa y va en la TAREA 2.d.
  - Y MI SEGUNDA CAIDA: escribi "OP-M-01 cerrando por sus SEIS hijas" sin
    nombrar la unidad, y la vara publica "5 de 5 hijas del CATALOGO,
    nomina de 6". Tu publicaste la cifra medida con su unidad al lado y no
    te equivocaste. La especie es exactamente la que tu CORRECCION 18
    registra en esa misma vuelta, y cometerla en el encargo que la encarga
    es caida mia.
  - TU PREGUNTA 2 TIENE RESPUESTA Y TU PREMISA NO ERA LA BUENA. Dices que
    OP-M-04 "queda en NO COMPUTABLE esperando a OP-U-01". OP-M-04 NO
    ESPERA A NADIE: su depende_de esta VACIO, y OP-S-12 y OP-U-01 son
    operaciones que OP-M-04 BLOQUEA, no de las que depende. Lo que pasa es
    otra cosa: LA VARA DE MESA MIDE UNA MESA SOLO POR SUS HIJAS
    (bloquea_a union remision) y NUNCA mira los campos propios de la
    ficha, y OP-M-04 ES LA UNICA MESA QUE LLEVA SU PROPIA CIRUGIA DENTRO
    (nodos con cuatro, eliminar con dos, y un giro en aristas_nuevas). Por
    eso sale NO COMPUTABLE y cae en SIN VARA ESCRITA, que es el
    instrumento diciendo en voz alta que le falta una regla. Verificado
    por mi contra el grafo: los cuatro nodos de OP-M-04 estan VIVOS y SIN
    FUNDIR, o sea que la operacion esta entera por hacer y nada la
    bloquea. La adjudicacion esta en la TAREA 3.

- TAREA 0, EL BLOQUE DE APERTURA, ANTES DE LA PRIMERA OPERACION. Va
  numerado 0 porque es un sello y no un trabajo.
  (0.a) EL SELLO: el HEAD de 40 caracteres, una sola linea, en
  docs/loop/SALIDA_V144_HEAD_APERTURA.txt, leido de git rev-parse HEAD.
  (0.b) LA BATERIA DEL LADO APERTURA, con el arbol LIMPIO, en este orden y
  una sola vez: el ciclo (python scripts/run_phase1.py
  --reaplico-curaduria, luego scripts/etiquetas_de_cara.py --aplicar,
  luego scripts/sync_assets_web.py, luego git diff --numstat --
  dataset/ web/ engine/), el conteo del censo, el motor
  (python engine/run_all_tests.py), vitest, tsc, Y EL DESFASE DEL
  CALIBRADO (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK).
  (0.c) LOS DIEZ NOMBRES CANONICOS, con LADO = APERTURA, y el gemelo de
  CIERRE al final de la vuelta con los mismos diez nombres:
  SALIDA_V144_HEAD_<LADO>.txt, SALIDA_V144_GATE0_CMD1_<LADO>.txt,
  SALIDA_V144_CONTEO_<LADO>.txt, SALIDA_V144_MOTOR_<LADO>.txt,
  SALIDA_V144_WEB_<LADO>.txt, SALIDA_V144_TSC_<LADO>.txt,
  SALIDA_V144_CICLO_ETIQUETAS_<LADO>.txt,
  SALIDA_V144_CICLO_SYNC_<LADO>.txt,
  SALIDA_V144_CICLO_NUMSTAT_<LADO>.txt,
  SALIDA_V144_DESFASE_CALIBRADO_<LADO>.txt.
  (0.d) LA COMPROBACION: python scripts/loop/verificar_apertura_sellada.py
  --vuelta 144. TIENE QUE DAR VERDE EXIT 0 CON LOS DIEZ DENTRO, Y ESTA VEZ
  PUEDE: no hay ningun commit pendiente que meter antes, asi que el bloque
  de apertura es HIJO DIRECTO del commit de mi acta y la guarda no tiene
  con que quejarse. Si saliera ROJO, PARAS Y LO TRAES: ya no hay ninguna
  desviacion declarada que lo explique.
  EL BLOQUE DE APERTURA (0.a mas 0.b mas 0.c) VA EN UN SOLO COMMIT.

- TAREA 4 ADELANTADA, Y VA LA SEGUNDA PORQUE ASI SALIO BIEN EN LA 143 Y NO
  SE TOCA LO QUE FUNCIONA. Escribe hoy, nada mas cerrar la TAREA 0, el
  esqueleto de docs/loop/REPORTE.md de la vuelta 144 con su cabecera vacia
  entre los delimitadores y las secciones por tarea. LO QUE SE MIDE SE VA
  PEGANDO DENTRO A MEDIDA QUE PASA. Y AL CIERRE, LAS TRES COSAS:
  (4.a) la bateria del lado CIERRE con los mismos diez nombres, y
  SALIDA_V144_HEAD_CIERRE.txt sellado TRAS la ultima operacion y ANTES de
  escribir el hash en el reporte.
  (4.b) tallar_cabecera_reporte.py --vuelta 144 --fase04 corrido, SU TABLA
  PEGADA ENTERA entre las dos marcas, mas --comparar docs/loop/REPORTE.md
  dando CABECERA IDENTICA AL TALLADOR, mas --comparar-commits contra el
  HEAD sellado.
  (4.c) verificar_cifras_del_reporte.py corrido SOBRE TU PROPIO REPORTE
  antes de commitearlo, con su linea de COBERTURA pegada. Y ESTA VEZ, CON
  LA 2.d HECHA, LA LINEA QUE PEGUES TIENE QUE REPRODUCIR: corre la guarda
  UNA SEGUNDA VEZ despues de pegarla y comprueba que da lo mismo. Si no da
  lo mismo, la 2.d no quedo bien y lo dices.
  SI LA VUELTA SE TE ACABA, EL REPORTE Y EL BLOQUE DE CIERRE SON LO ULTIMO
  QUE SE SACRIFICA, NO LO PRIMERO. Antes de eso se parte la TAREA 3.

- TAREA 1, LOS REGISTROS.
  (1.a) R.25 EN docs/PENDIENTES.md, POR ADICION, como hiciste con R.24:
  las diez adjudicaciones de mi acta 143 (3.1 a 3.10), TU caida (4.1 de
  reporte, que NO acumula y por que), las TRES de la casa (4.2 la ventana
  que se ensancha en silencio, 4.3 el ancla en la primera ocurrencia, 4.4
  el giro que tira sus fallos) mas la cuarta de la casa que la 4.1 destapa
  (la cola de vocabulario que no es punto fijo), y MIS DOS (4.5 y 4.6, las
  dos de encargo). Y LAS DOS RACHAS CON SU ESTADO NUEVO: cifra publicada
  SIGUE EN CERO y REPORTE BAJA DE DOS A CERO, con el motivo escrito (la
  143 si tiene reporte y su unica caida no acumula). Numstat con anadidas
  y borradas.
  (1.b) LA CORRECCION 19, POR ADICION Y EN
  docs/plan/CORRECCIONES_A_APLICAR.md: LA EXCEPCION DEL 9.22 SE ESCRIBE
  CON FORMULA CANONICA, Y LA VENTANA TENIA DOS AGUJEROS. Es mi
  adjudicacion 3.1. Registra los dos agujeros CON TU PROPIA MEDICION, no
  copiando la mia: escribe tu propio arnes que mida (i) cuantos pares
  salen con la ficha tal cual, (ii) cuantos salen quitando el literal de
  cierre y CUAL entra, y (iii) en que posiciones aparece el literal de
  apertura y en cual ancla el codigo. Si tu medicion discrepa de la mia,
  LO DECLARAS, no lo copias. Y deja escrita la formula canonica que la
  TAREA 2.a implementa.
  (1.c) LA CORRECCION 20, POR ADICION: OP-M-04 NO ESPERA A NADIE, Y LA
  VARA DE MESA MIDE POR HIJAS. Es mi adjudicacion 3.9. Deja escrito,
  medido con tu instrumento: que depende_de de OP-M-04 esta vacio, que
  OP-S-12 y OP-U-01 estan en su bloquea_a (o sea que las bloquea, no
  depende de ellas), que sus cuatro nodos siguen vivos y sin fundir, y que
  la rama es_mesa de medir() nunca mira nodos, eliminar ni aristas_nuevas
  de la propia ficha. Y la regla que queda: LA MESA QUE DECLARA SU FIGURA
  EN SU PROPIO `tipo` SE MIDE CON LAS VARAS DE SU FIGURA, SOBRE SUS
  PROPIOS CAMPOS. No es doctrina nueva: las dos varas que hacen falta
  (FUSION y ENLACE) ya estan escritas en ese mismo fichero.
  NO TOQUES docs/plan/OPERACIONES.jsonl en esta tarea.

- TAREA 2, LAS REPARACIONES, BLOQUEANTE Y ANTES DE TOCAR NINGUNA OPERACION
  DEL PLAN. Y LO DIGO PARA QUE NO SE CUENTE COMO LO QUE NO ES: ESTO NO ES
  LA ESCALADA DE LA RACHA. La escalada de la racha en dos la entregaste
  entera en la 143 y la verifique en tres de tres puntos; la racha esta en
  CERO y AUDITOR.md 1.2 ya no me obliga. Esto son las reparaciones de mis
  adjudicaciones 3.1, 3.3, 3.6 y 3.10. Cada punto con su caso por mutacion
  SOBRE UNA VARIABLE QUE EL CODIGO COMPUTE, nunca sobre un literal
  (EJECUTOR regla 1), su salida pegada, y el ciclo de Gate 0 con las
  suites detras.
  EL TRAMO DE LECTURA DE LA EXCEPCION Y EL DEL GIRO VAN RELEIDOS AL DOBLE,
  por la caida 4.4 que cayo fuera de lo marcado: los lees dos veces, la
  segunda buscando expresamente MODOS DE FALLO SILENCIOSO, y dices que
  encontraste la segunda vez aunque sea "nada".

  (2.a) LA FORMULA CANONICA, CON FALLO RUIDOSO EN LOS DOS EXTREMOS. En
  scripts/loop/tallar_estado_de_fase.py:
    (i) LA EXCEPCION DECLARA SUS PARES DENTRO DE UNA MARCA DE APERTURA Y
        UNA DE CIERRE INEQUIVOCAS, elegidas para que no puedan aparecer en
        prosa (por ejemplo un par de marcas explicitas del tipo
        "PARES EXCEPTUADOS:" ... "FIN PARES EXCEPTUADOS", pero la eleges
        tu y la justificas). NO vale una frase que tambien pueda salir en
        la explicacion.
    (ii) SI LA FICHA DISPARA LA EXCEPCION Y NO TRAE LA FORMULA ENTERA,
        ES ROJO NOMBRANDOLA, y el conjunto sale VACIO. Los dos extremos
        con su fallo: falta la apertura, ROJO; falta el cierre, ROJO. NUNCA
        se lee hasta el final de la linea por defecto. Ese `else linea[ini:]`
        muere.
    (iii) LA ANCLA ES UNICA O ES ROJO: si la marca de apertura aparece mas
        de una vez en la linea, es ROJO por ambigua, no se toma la
        primera.
    (iv) LA VERIFICACION 5 DE OP-E-04 SE REESCRIBE PARA LLEVAR LA FORMULA,
        POR ADICION Y SIN BORRAR UNA LETRA de lo que ya dice, con la
        guarda semantica de siempre (fichas antes y despues, ficha que
        cambia, campo que cambia, PREFIJO IDENTICO). Y AL TERMINAR, LOS
        CUATRO PARES EXCEPTUADOS TIENEN QUE SEGUIR SIENDO LOS MISMOS
        CUATRO, y la tabla de la fase 06 no puede moverse ni una celda:
        diff de la tabla entera antes y despues, y si se mueve algo, lo
        traes.
  MUTACIONES, EN MEMORIA Y CON EL SUJETO POR COMPUTO: (i) quitada la marca
  de cierre, ROJO nombrado y CERO pares (hoy da 5 en silencio); (ii)
  quitada la marca de apertura, ROJO nombrado y CERO pares (hoy da 4 en
  silencio); (iii) duplicada la marca de apertura, ROJO por ambigua; (iv)
  con la ficha entera y bien formada, los CUATRO pares de siempre y CERO
  fallos, que es la contraprueba.

  (2.b) EL GIRO RECOGE SUS FALLOS Y ABORTA CON ELLOS. Es mi 3.3 y la caida
  4.4. En scripts/loop/vuelta143_3c_girar_arista.py:222, la lista vacia
  literal se sustituye por una lista real que se imprime y que ABORTA la
  operacion, exactamente como vuelta140_3_escribir_aristas.py:162-164.
  MUTACION: dale una ficha cuya excepcion no parsea y comprueba que el
  giro CAE con exit distinto de cero y CERO escrituras en dataset/,
  cuando hoy diria OK y borraria. Y REVISA SI HAY UN CUARTO SITIO: busca
  en scripts/loop/ toda llamada a pares_exceptuados_de y di cuantas hay y
  que hace cada una con sus fallos. Si aparece otra que los tire, la
  arreglas igual y la nombras.

  (2.c) LAS TRES MUTACIONES DE LA 143 ENTRAN EN LA BATERIA. Es mi 3.6, y
  es tu propio discutible 6, concedido. En VIEJAS de
  scripts/loop/verificar_mutaciones_viejas.py entran
  vuelta143_2a_mutaciones.py, vuelta143_2b_mutacion_bateria.py y
  vuelta143_2c_mutacion_positivo.py, mas las que escribas hoy en la 2.a y
  la 2.b. Corre la bateria y PEGA SU SALIDA: tiene que salir VERDE con
  todas, NO MORDIO en cero. La regla que queda, y la escribes: una
  mutacion entra en la bateria EN LA VUELTA SIGUIENTE A LA QUE NACE, no
  mas tarde.

  (2.d) LA GUARDA DE CIFRAS DEJA DE MEDIRSE A SI MISMA. Es mi 3.10 y la
  caida 4.1. En scripts/loop/verificar_cifras_del_reporte.py, el bloque de
  salida que el reporte pega queda DELIMITADO y se RECORTA antes de
  parsear, exactamente como la guarda ya hace con la cabecera tallada. No
  inventes mecanismo nuevo: copia el que ya funciona. MUTACION: sobre una
  copia en memoria de un reporte, pega la propia linea de COBERTURA dentro
  y comprueba que la cifra de unidades fuera del vocabulario NO SE MUEVE,
  cuando hoy sube. Contraprueba: sin los delimitadores, sube.

- TAREA 3, EL TRABAJO. NADA DE ESTO ANTES DE QUE LA TAREA 2 ESTE VERDE.
  (3.a) LA VARA DE OP-M-04, POR SU PROPIA FIGURA. Es mi adjudicacion 3.9.
  En scripts/loop/tallar_estado_de_fase.py, la rama es_mesa aprende un
  caso mas y SOLO UNO: cuando el `tipo` de la mesa DECLARA SU FIGURA (el
  de OP-M-04 dice literal "MESA ADJUDICADA: DOS FUSIONES MAS UN ENLACE"),
  la mesa se mide con las varas de esa figura sobre SUS PROPIOS campos
  (nodos, eliminar, superviviente, aristas_nuevas), reusando las funciones
  de FUSION y de ENLACE QUE YA ESTAN ESCRITAS, no copiandolas. LA FRASE
  QUE DISPARA VA LITERAL DE LA FICHA Y CITADA EN EL CODIGO, como hiciste
  con las seis de la 141 y con la excepcion de la 143. UNA MESA QUE NO
  DECLARA SU FIGURA SE COMPORTA EXACTAMENTE COMO HOY: diff de la tabla
  entera antes y despues, y la unica fila que puede moverse es la de
  OP-M-04. Si se mueve otra, lo traes.
  MUTACIONES: (i) sobre la ficha ejecutada en memoria, sale CUMPLIDA
  (contraprueba); (ii) con una de las dos fusiones a medias, sale SIN
  CUMPLIR y NOMBRA cual; (iii) con el enlace en la direccion equivocada,
  sale SIN CUMPLIR por el enlace y no por las fusiones; (iv) borrada la
  frase de la figura del `tipo`, la mesa vuelve a NO COMPUTABLE con el
  mismo texto de celda que sale hoy.
  (3.b) OP-M-04 SE EJECUTA ENTERA, en su propio commit, con las guardas de
  siempre: LEE SU FICHA ENTERA ANTES DE TOCAR NADA (es una mesa adjudicada
  el 11 ago 2026, con expediente propio en
  docs/plan/EXPEDIENTE_MESA_JUNTA_ASESORA.md, y su `nota` corrige la
  premisa: la arista entre formalizar_junta_asesora e
  identificar_junta_asesores NO es bidireccional). Son DOS FUSIONES mas UN
  ENLACE, no una fusion de cuatro: fusion 367 con superviviente
  identificar_consejo_asesores, fusion 328 con superviviente
  formalizar_junta_asesora, y el GIRO que la ficha describe, que termina
  con UNA SOLA ARISTA entre madre e hijo en la direccion de la escalera.
  Simulacion previa sobre copia en memoria con cero escrituras, mutacion
  negativa con cero escrituras, P.9, P.13 para las perdidas, P.16, EL
  GRADO TOTAL MEDIDO ANTES Y DESPUES con el ciclo CORRIDO entre las dos
  medidas, cero duplicadas y cero auto-aristas tras resolver, y EL CICLO
  DE GATE 0 CON LAS SUITES detras. LAS PERDIDAS VAN REPARTIDAS CON SU
  TABLA DE SEIS MOTIVOS, que es lo que la fase III exige de toda fusion.
  (3.c) EL CASO POSITIVO DE LA OPERACION, QUE LA PROPIA FICHA ESCRIBE:
  "releido el par 1190 tras la ejecucion, tiene que dar D por la vara. Si
  diera A, la fusion 367 conservo el nodo equivocado". Lo corres y pegas
  su salida. SI DA A, PARAS Y LO TRAES: es la ficha diciendo que el
  superviviente esta mal elegido, y eso no se ajusta, se para.
  (3.d) SI UNA ESCRITURA O UNA RETIRADA TOCA UNA ARISTA QUE NINGUNA
  OPERACION DEL PLAN PROPONE NI PROHIBE, PARAS ESA Y LA TRAES. Sigue viva.
  (3.e) CUANDO OP-M-04 ESTE EJECUTADA, vuelve a correr
  tallar_estado_de_fase.py --fase 06_MESAS y pega su salida entera. SEGUN
  MI MEDICION LA FASE 06 TIENE QUE CERRAR AQUI: catalogo 16, con destino
  cumplido 16, sin cumplir 0. SI NO CIERRA, LO MIDES Y LO TRAES NOMBRANDO
  LAS QUE FALTEN, NO LO AJUSTAS. Y NO ABRAS LA FASE 07: no hay condicion
  de parada escrita para el cierre de la fase 06, pero el cierre de una
  fase se verifica antes de abrir la siguiente, y esa verificacion es mia.
  EL CAMPO estado SIGUE SIN TOCARSE (actas 139 a 143): el pase de estado
  va en UNA sola adjudicacion mia, con el conteo antes y despues. No lo
  adelantes. OP-S-12 SIGUE AL FINAL DE LA PASADA ENTERA, por la atadura 2
  del indice.

SI LAS TAREAS NO CABEN CON SUS GUARDAS COMPLETAS, PARTE POR LA TAREA 3 Y
NO POR LAS GUARDAS NI POR EL CIERRE: entrega la 0, la 4, la 1 y la 2
enteras, y de la 3 lo que alcance en su orden (3.a antes que 3.b, y la 3.c
en el mismo commit que la 3.b), diciendo CUAL no hiciste y por que. La
TAREA 2 es BLOQUEANTE y no se parte. Y LA TAREA 4 NO SE PARTE TAMPOCO.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
